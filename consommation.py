"""Compteur de tokens consommés chaque jour par la veille, chez Groq et chez Gemini.

Chaque appel à un modèle passe par un « callback » LangChain (Compteur) branché sur les
clients créés dans agent.py ; Graphify, qui appelle Gemini lui-même, est compté à partir de
son propre registre (cost.json) par cerveau.py.

Un fichier par jour, mis à jour après chaque appel (rien n'est perdu si un script plante) :
    veilles/consommation-AAAA-MM-JJ.json
    {"date": ..., "fournisseurs": {"groq": {"entree", "sortie", "appels"}, "gemini": {...}},
     "etapes": {"agent": {"groq": {...}, "gemini": {...}}, "cerveau": {...}, ...}}

La date est celle de Paris (la mission GitHub tourne avec TZ=Europe/Paris).
"""

import json
import re
import sys
import threading
from datetime import datetime
from pathlib import Path

from langchain_core.callbacks import BaseCallbackHandler

import os

# Sur GitHub (mission de nuit), le compteur est enregistré avec la veille. Sur le PC
# (chat, relances, essais), il va dans un dossier à part, ignoré par Git : sinon le
# fichier local entrerait en conflit avec celui de la mission au prochain « git pull ».
DOSSIER_MISSION = Path(__file__).parent / "veilles"
DOSSIER_LOCAL = Path(__file__).parent / "consommation-locale"
DOSSIER = DOSSIER_MISSION if os.environ.get("GITHUB_ACTIONS") else DOSSIER_LOCAL
FORMAT = re.compile(r"consommation-(\d{4}-\d{2}-\d{2})\.json")
VERROU = threading.Lock()
# Limite gratuite de Groq pour gpt-oss-120b (tokens par jour, entrée + sortie). Gemini
# limite surtout le nombre de requêtes par jour, variable selon le modèle : pas de %.
QUOTA_GROQ_JOUR = 200_000


def _etape() -> str:
    """Nom du script lancé (agent, memoire, redacteur, cerveau, interface…)."""
    nom = Path(sys.argv[0]).stem if sys.argv and sys.argv[0] else ""
    return nom if nom and nom not in ("-c", "-") else "autre"


def _fichier(jour: str) -> Path:
    return DOSSIER / f"consommation-{jour}.json"


def _vide() -> dict:
    return {"entree": 0, "sortie": 0, "appels": 0}


def enregistrer(fournisseur: str, entree: int, sortie: int, appels: int = 1,
                etape: str | None = None) -> None:
    """Ajoute une consommation au fichier du jour."""
    if not (entree or sortie):
        return
    jour = datetime.now().strftime("%Y-%m-%d")
    etape = etape or _etape()
    with VERROU:
        chemin = _fichier(jour)
        try:
            donnees = json.loads(chemin.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            donnees = {"date": jour, "fournisseurs": {}, "etapes": {}}
        for cible in (donnees["fournisseurs"].setdefault(fournisseur, _vide()),
                      donnees["etapes"].setdefault(etape, {}).setdefault(fournisseur, _vide())):
            cible["entree"] += int(entree)
            cible["sortie"] += int(sortie)
            cible["appels"] += appels
        try:
            DOSSIER.mkdir(parents=True, exist_ok=True)
            chemin.write_text(json.dumps(donnees, ensure_ascii=False, indent=1), encoding="utf-8")
        except OSError:
            pass  # le compteur ne doit jamais faire échouer la veille


class Compteur(BaseCallbackHandler):
    """Callback LangChain : relève les tokens de chaque réponse d'un fournisseur."""

    def __init__(self, fournisseur: str):
        self.fournisseur = fournisseur

    def on_llm_end(self, response, **kwargs) -> None:
        try:
            for generations in response.generations:
                for g in generations:
                    usage = getattr(getattr(g, "message", None), "usage_metadata", None)
                    if usage:
                        enregistrer(self.fournisseur, usage.get("input_tokens", 0),
                                    usage.get("output_tokens", 0))
                        return
            # Repli : certains clients ne remplissent que llm_output.
            usage = (response.llm_output or {}).get("token_usage") or {}
            enregistrer(self.fournisseur, usage.get("prompt_tokens", 0),
                        usage.get("completion_tokens", 0))
        except Exception:
            pass  # idem : jamais bloquant


COMPTEUR_GROQ = Compteur("groq")
COMPTEUR_GEMINI = Compteur("gemini")


def _ajouter(cible: dict, source: dict) -> None:
    for cle in ("entree", "sortie", "appels"):
        cible[cle] = cible.get(cle, 0) + source.get(cle, 0)


def historique(jours: int = 30) -> list[dict]:
    """Les derniers jours, du plus récent au plus ancien (mission de nuit + usage du PC),
    avec le % du quota Groq."""
    par_jour: dict[str, dict] = {}
    for dossier in {DOSSIER_MISSION, DOSSIER_LOCAL}:
        for chemin in dossier.glob("consommation-*.json"):
            if not FORMAT.fullmatch(chemin.name):
                continue
            try:
                d = json.loads(chemin.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            total = par_jour.setdefault(d["date"], {"date": d["date"], "fournisseurs": {}, "etapes": {}})
            for f, v in d.get("fournisseurs", {}).items():
                _ajouter(total["fournisseurs"].setdefault(f, _vide()), v)
            for etape, fs in d.get("etapes", {}).items():
                for f, v in fs.items():
                    _ajouter(total["etapes"].setdefault(etape, {}).setdefault(f, _vide()), v)
    for d in par_jour.values():
        groq = d["fournisseurs"].get("groq", _vide())
        d["quota_groq"] = QUOTA_GROQ_JOUR
        d["part_quota_groq"] = round(100 * (groq["entree"] + groq["sortie"]) / QUOTA_GROQ_JOUR, 1)
    return sorted(par_jour.values(), key=lambda d: d["date"], reverse=True)[:jours]


if __name__ == "__main__":
    def n(x: int) -> str:
        return f"{x:,}".replace(",", " ")

    for d in historique(7):
        f = d["fournisseurs"]
        g, m = f.get("groq", _vide()), f.get("gemini", _vide())
        print(f"{d['date']} · Groq {n(g['entree'] + g['sortie'])} tokens ({d['part_quota_groq']} % du "
              f"quota, {g['appels']} appels) · Gemini {n(m['entree'] + m['sortie'])} tokens "
              f"({m['appels']} appels)")
