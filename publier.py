"""Construit la version en ligne de l'app (dossier site/), publiée sur GitHub Pages.

Pas de serveur en ligne : la page lit des fichiers JSON. Ce script les prépare à partir
des veilles enregistrées dans veilles/ et de sources.json, puis ajoute ce qui fait de
la page une app installable (manifeste, icônes, service worker).

Lancement : uv run python publier.py        (puis ouvrir site/ avec un serveur web)
"""

import json
import shutil
from pathlib import Path

from interface import _fichiers_veille, etat_sources, liste_veilles

RACINE = Path(__file__).parent
SITE = RACINE / "site"
PWA = RACINE / "pwa"

# Ajouts dans <head> : mode statique, manifeste, icônes, couleur de la barre du téléphone.
TETE = """<script>window.VEILLE_STATIQUE = true;</script>
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#163b7c">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Veille IA">
<link rel="icon" type="image/png" href="icones/icone-192.png">
<link rel="apple-touch-icon" href="icones/apple-touch-icon.png">
</head>"""

# Avant </body> : enregistrement du service worker (lecture hors connexion).
PIED = """<script>
if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
</script>
</body>"""


def _ecrire_json(chemin: Path, donnees) -> None:
    chemin.write_text(json.dumps(donnees, ensure_ascii=False), encoding="utf-8")


def construire() -> int:
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "donnees").mkdir(parents=True)

    page = (RACINE / "interface.html").read_text(encoding="utf-8")
    assert page.count("</head>") == 1 and page.count("</body>") == 1, "interface.html inattendu"
    page = page.replace("</head>", TETE).replace("</body>", PIED)
    (SITE / "index.html").write_text(page, encoding="utf-8")

    shutil.copy(PWA / "manifest.json", SITE / "manifest.json")
    shutil.copy(PWA / "sw.js", SITE / "sw.js")
    shutil.copytree(PWA / "icones", SITE / "icones")
    (SITE / ".nojekyll").write_text("")  # GitHub Pages : servir les fichiers tels quels

    fichiers = _fichiers_veille()
    for _, _, fichier in fichiers:
        shutil.copy(fichier, SITE / "donnees" / fichier.name)
    _ecrire_json(SITE / "donnees" / "veilles.json", {"veilles": liste_veilles()})
    _ecrire_json(SITE / "donnees" / "sources.json", etat_sources())
    return len(fichiers)


if __name__ == "__main__":
    n = construire()
    print(f"Site construit dans {SITE} ({n} fichiers de veille).")
