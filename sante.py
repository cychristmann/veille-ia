"""Bilan de santé d'une nuit de veille : chaque étape a-t-elle vraiment produit son résultat ?

Le bilan est calculé à partir des fichiers réellement produits (et non de ce que les scripts
disent d'eux-mêmes) : c'est ce qui révèle les pannes silencieuses, comme le cerveau resté
figé deux jours en novembre 2026 alors que son étape « réussissait ».

    bilan("2026-11-14") -> {"date", "statut": "ok" | "attention" | "echec",
                            "controles": [{"nom", "statut", "detail"}, ...]}

Usage : uv run python sante.py [AAAA-MM-JJ]
"""

import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).parent
VEILLES = RACINE / "veilles"
CERVEAU = RACINE / "cerveau"
SECTIONS = {"fr": "France", "us": "États-Unis", "cn": "Chine", "dev": "Outils & code"}
ORDRE = {"ok": 0, "attention": 1, "echec": 2}
# Avant cette date, toutes les étapes n'existaient pas encore (4e section, interprète) :
# un bilan y signalerait de fausses pannes.
DEBUT = "2026-11-13"


def _lire(chemin: Path):
    try:
        return json.loads(chemin.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _controle(nom: str, statut: str, detail: str) -> dict:
    return {"nom": nom, "statut": statut, "detail": detail}


def _sections(jour: str) -> list[dict]:
    controles = []
    for code, nom in SECTIONS.items():
        v = _lire(VEILLES / f"veille-ia-{code}-{jour}.json")
        if v is None:
            controles.append(_controle(f"Veille {nom}", "echec", "Aucune veille produite."))
            continue
        articles, voulus = v.get("nombre_articles", 0), v.get("nombre_demande", 50)
        soucis = []
        if articles < 0.8 * voulus:
            soucis.append(f"seulement {articles} articles sur {voulus}")
        if not v.get("themes"):
            soucis.append("analyse par thèmes absente")
        if v.get("articles_notes", 0) < articles:
            soucis.append(f"{articles - v.get('articles_notes', 0)} articles sans note")
        echecs = v.get("sources_en_echec") or []
        if echecs:
            soucis.append(f"{len(echecs)} source(s) en panne : {', '.join(echecs[:3])}")
        for rubrique in ("videos", "podcasts"):
            if (v.get(rubrique) or {}).get("statut") not in ("ok", None):
                soucis.append(f"{rubrique} indisponibles")
        grave = articles == 0 or not v.get("themes")
        detail = f"{articles} articles, {v.get('liens_google', 0)} sans lien direct"
        controles.append(_controle(f"Veille {nom}", "echec" if grave else "attention" if soucis else "ok",
                                   detail + (" · " + " ; ".join(soucis) if soucis else "")))
    return controles


def _dernier_jour_du_graphe() -> str | None:
    g = _lire(CERVEAU / "graphify-out" / "graph.json")
    if not g:
        return None
    jours = set()
    for n in g.get("nodes", []):
        for s in n.get("sources", [n.get("source_file")]):
            m = re.search(r"veille-ia-[a-z]+-(\d{4}-\d{2}-\d{2})", s or "")
            if m:
                jours.add(m.group(1))
    return max(jours) if jours else None


def bilan(jour: str) -> dict:
    controles = _sections(jour)

    memoire = _lire(VEILLES / "memoire.json") or {}
    a_jour = (memoire.get("maj") or "") >= jour
    controles.append(_controle("Mémoire des feuilletons", "ok" if a_jour else "attention",
                               f"{len(memoire.get('feuilletons', []))} feuilletons suivis" if a_jour
                               else f"Dernière mise à jour : {memoire.get('maj') or 'jamais'}."))

    dossiers = _lire(VEILLES / f"dossiers-{jour}.json")
    n = len((dossiers or {}).get("dossiers", []))
    controles.append(_controle("Rédacteur en chef", "ok" if n else "attention",
                               f"{n} dossier(s), {(dossiers or {}).get('appels', 0)} appels à l'IA" if dossiers
                               else "Aucun dossier ce jour-là."))

    tendances = _lire(VEILLES / "tendances.json") or {}
    frais = str(tendances.get("genere_a", ""))[:10] >= jour
    controles.append(_controle("Tendances de la semaine", "ok" if frais else "attention",
                               "À jour." if frais else f"Dernier calcul : {str(tendances.get('genere_a', 'jamais'))[:10]}."))

    etapes = _lire(VEILLES / f"etapes-{jour}.json") or {}  # résultat des étapes facultatives
    dernier = _dernier_jour_du_graphe()
    if dernier is None:
        controles.append(_controle("Deuxième cerveau", "echec", "Graphe introuvable."))
    elif dernier < jour or etapes.get("cerveau") == "failure":
        controles.append(_controle("Deuxième cerveau", "echec",
                                   f"Graphe pas à jour : dernier jour intégré, {dernier}."))
    else:
        g = _lire(CERVEAU / "graphify-out" / "graph.json")
        controles.append(_controle("Deuxième cerveau", "ok", f"{len(g['nodes'])} entités dans le graphe."))

    analyse = _lire(CERVEAU / "analyses" / f"analyse-{jour}.json")
    n = len((analyse or {}).get("analyses", []))
    if analyse is None or etapes.get("interprete") == "failure":
        controles.append(_controle("Interprète", "echec", "Pas d'analyse produite."))
    else:
        controles.append(_controle("Interprète", "ok" if n else "attention",
                                   f"{n} analyse(s)." if n else (analyse.get("rien") or "Aucun signal retenu.")))

    try:
        import consommation
        conso = next((d for d in consommation.historique(60) if d["date"] == jour), None)
    except Exception:
        conso = None
    if conso:
        part = conso["part_quota_groq"]
        controles.append(_controle("Quota Groq", "attention" if part >= 80 else "ok",
                                   f"{part} % du quota gratuit quotidien utilisé."))

    statut = max((c["statut"] for c in controles), key=ORDRE.get)
    return {"date": jour, "statut": statut, "controles": controles}


def historique(jours: int = 14) -> list[dict]:
    """Bilans des derniers jours de veille, du plus récent au plus ancien."""
    dates = sorted({m.group(1) for f in VEILLES.glob("veille-ia-*.json")
                    for m in [re.search(r"(\d{4}-\d{2}-\d{2})\.json$", f.name)] if m}, reverse=True)
    return [bilan(d) for d in dates[:jours] if d >= DEBUT]


if __name__ == "__main__":
    jour = sys.argv[1] if len(sys.argv) > 1 else (historique(1) or [{"date": ""}])[0]["date"]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", jour):
        sys.exit("Aucune veille trouvée, ou date invalide (AAAA-MM-JJ).")
    b = bilan(jour)
    print(f"Bilan du {b['date']} : {b['statut']}")
    for c in b["controles"]:
        print(f"  [{c['statut']:9}] {c['nom']} — {c['detail']}")
