"""Interface graphique de la veille IA : une page web locale qui affiche les articles du jour.

Lancement : uv run python interface.py      (la page s'ouvre ; Ctrl+C pour arrêter)

N'utilise que la bibliothèque standard de Python : un petit serveur web sert la page
(interface.html) et trois adresses lues par la page :
    GET  /api/veilles                            -> les jours disponibles et leurs régions
    GET  /api/veille?region=fr&date=AAAA-MM-JJ   -> la veille d'une région un jour donné
                                                    (la plus récente sans date)
    POST /api/actualiser                         -> relance l'agent pour toutes les régions
    GET  /api/sources                            -> sources suivies et propositions
    POST /api/sources/chercher                   -> lance l'agent de découverte de sources
    POST /api/sources/decision                   -> ajouter / refuser / retirer une source
"""

import argparse
import json
import re
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from dotenv import load_dotenv

import sources
from agent import DOSSIER_RAPPORTS, REGIONS, lancer_veilles

PAGE = Path(__file__).parent / "interface.html"
NOMBRE_ARTICLES = 50
HEURES = 24

# Une seule veille (et une seule recherche de sources) à la fois : deux clics rapides
# ne doivent pas lancer deux collectes.
VEILLE_EN_COURS = threading.Lock()
RECHERCHE_EN_COURS = threading.Lock()
MAX_CORPS = 10_000  # taille maximale d'une requête POST acceptée


def etat_sources() -> dict:
    """Ce que la page affiche : sources intégrées, ajoutées, et propositions en attente."""
    donnees = sources.charger()
    return {
        "integrees": {code: sorted(r.flux_medias) for code, r in REGIONS.items()},
        "ajoutees": {
            code: [{"nom": nom, "flux": url, "domaine": sources._domaine(url)}
                   for nom, url in donnees["ajoutees"].get(code, {}).items()]
            for code in REGIONS
        },
        "propositions": donnees["propositions"],
        "nombre_refusees": len(donnees["refusees"]),
    }


FORMAT_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
NOM_FICHIER = re.compile(r"veille-ia-(?P<region>[a-z]+)-(?P<date>\d{4}-\d{2}-\d{2})\.json")


def _fichiers_veille() -> list[tuple[str, str, Path]]:
    """(date, région, fichier) de chaque veille, de la plus récente à la plus ancienne."""
    trouves = []
    for fichier in DOSSIER_RAPPORTS.glob("veille-ia-*.json"):
        m = NOM_FICHIER.fullmatch(fichier.name)
        if m and m["region"] in REGIONS:
            trouves.append((m["date"], m["region"], fichier))
    return sorted(trouves, reverse=True)


def liste_veilles() -> list[dict]:
    """Un élément par jour, avec un résumé de chaque région disponible ce jour-là."""
    jours: dict[str, dict] = {}
    for date, region, fichier in _fichiers_veille():
        try:
            donnees = json.loads(fichier.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue  # fichier abîmé : on l'ignore plutôt que de casser la liste
        jours.setdefault(date, {"date": date, "regions": {}})["regions"][region] = {
            "genere_a": donnees.get("genere_a"),
            "nombre_articles": donnees.get("nombre_articles", 0),
            "nombre_themes": len(donnees.get("themes", [])),
        }
    return list(jours.values())


def lire_veille(region: str, date: str | None = None) -> dict | None:
    """Veille d'une région un jour donné, ou sa plus récente si date est None."""
    if region not in REGIONS:
        return None
    if date is None:
        fichiers = [f for _, r, f in _fichiers_veille() if r == region]
        fichier = fichiers[0] if fichiers else None
    else:
        # Format strict : empêche de remonter dans les dossiers avec « ../ ».
        if not FORMAT_DATE.fullmatch(date):
            return None
        fichier = DOSSIER_RAPPORTS / f"veille-ia-{region}-{date}.json"
    if fichier is None or not fichier.is_file():
        return None
    return json.loads(fichier.read_text(encoding="utf-8"))


class Gestionnaire(BaseHTTPRequestHandler):
    def _hote_autorise(self) -> bool:
        # Refuse les requêtes adressées sous un autre nom (protection « DNS rebinding »).
        port = self.server.server_address[1]
        return self.headers.get("Host") in {f"127.0.0.1:{port}", f"localhost:{port}"}

    def _repondre(self, code: int, contenu: bytes, type_contenu: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", type_contenu)
        self.send_header("Content-Length", str(len(contenu)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(contenu)

    def _json(self, code: int, donnees: dict) -> None:
        self._repondre(code, json.dumps(donnees, ensure_ascii=False).encode("utf-8"),
                       "application/json; charset=utf-8")

    def do_GET(self) -> None:
        if not self._hote_autorise():
            return self._json(403, {"erreur": "Hôte non autorisé"})
        adresse = urlsplit(self.path)
        if adresse.path == "/":
            self._repondre(200, PAGE.read_bytes(), "text/html; charset=utf-8")
        elif adresse.path == "/api/veilles":
            self._json(200, {"veilles": liste_veilles()})
        elif adresse.path == "/api/sources":
            self._json(200, etat_sources())
        elif adresse.path == "/api/veille":
            parametres = parse_qs(adresse.query)
            date = parametres.get("date", [None])[0]
            veille = lire_veille(parametres.get("region", ["fr"])[0], date)
            if veille is None:
                self._json(200 if date is None else 404, {"vide": True})
            else:
                self._json(200, veille)
        else:
            self._json(404, {"erreur": "Page introuvable"})

    def do_POST(self) -> None:
        # L'en-tête X-Veille oblige le navigateur à demander une autorisation préalable
        # pour toute requête venant d'un autre site : une page piégée ne peut donc pas
        # déclencher de veille (et consommer ton quota Groq) à ta place.
        if not self._hote_autorise() or self.headers.get("X-Veille") != "1":
            return self._json(403, {"erreur": "Requête refusée"})
        if self.path == "/api/sources/chercher":
            return self._chercher_sources()
        if self.path == "/api/sources/decision":
            return self._decider_source()
        if self.path != "/api/actualiser":
            return self._json(404, {"erreur": "Page introuvable"})
        if not VEILLE_EN_COURS.acquire(blocking=False):
            return self._json(409, {"erreur": "Une veille est déjà en cours."})
        try:
            print("Veille en cours (toutes les régions)…")
            etats = lancer_veilles(list(REGIONS), NOMBRE_ARTICLES, HEURES)
            print("Veille terminée.")
            self._json(200, {"regions": {e["region"]: len(e["articles"]) for e in etats}})
        except Exception as exc:  # réseau, quota Groq… : on l'affiche dans la page
            self._json(500, {"erreur": f"{type(exc).__name__} : {exc}"})
        finally:
            VEILLE_EN_COURS.release()

    def _chercher_sources(self) -> None:
        if not RECHERCHE_EN_COURS.acquire(blocking=False):
            return self._json(409, {"erreur": "Une recherche de sources est déjà en cours."})
        try:
            print("Recherche de nouvelles sources…")
            etat = sources.chercher()
            print("Recherche terminée.")
            self._json(200, {**etat_sources(), "nouvelles": len(etat.get("propositions", []))})
        except Exception as exc:
            self._json(500, {"erreur": f"{type(exc).__name__} : {exc}"})
        finally:
            RECHERCHE_EN_COURS.release()

    def _decider_source(self) -> None:
        try:
            longueur = int(self.headers.get("Content-Length", "0"))
            if not 0 < longueur <= MAX_CORPS:
                raise ValueError("Requête vide ou trop grande.")
            corps = json.loads(self.rfile.read(longueur))
            message = sources.decider(str(corps["domaine"]), str(corps["decision"]))
        except (ValueError, KeyError, TypeError) as exc:  # JSON invalide, domaine inconnu…
            return self._json(400, {"erreur": str(exc)})
        self._json(200, {**etat_sources(), "message": message})

    def log_message(self, format: str, *args) -> None:
        pass  # pas de ligne dans le terminal à chaque requête


def main() -> None:
    parser = argparse.ArgumentParser(description="Interface de la veille IA.")
    parser.add_argument("--port", type=int, default=8000, help="port local (défaut : 8000)")
    args = parser.parse_args()

    load_dotenv()
    # 127.0.0.1 : la page n'est accessible que depuis cet ordinateur.
    serveur = ThreadingHTTPServer(("127.0.0.1", args.port), Gestionnaire)
    adresse = f"http://127.0.0.1:{args.port}/"
    print(f"Interface de veille : {adresse}  (Ctrl+C pour arrêter)")
    webbrowser.open(adresse)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt.")
    finally:
        serveur.server_close()


if __name__ == "__main__":
    main()
