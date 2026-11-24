"""Construit la version en ligne de l'app (dossier site/), publiée sur GitHub Pages.

Pas de serveur en ligne : la page lit des fichiers JSON. Ce script les prépare à partir
des veilles enregistrées dans veilles/ et de sources.json, puis ajoute ce qui fait de
la page une app installable (manifeste, icônes, service worker).

Lancement : uv run python publier.py        (puis ouvrir site/ avec un serveur web)
"""

import base64
import briefing
import hashlib
import json
import re
import shutil
from pathlib import Path

from agent import DOSSIER_RAPPORTS
import consommation
import paris
import pilote
import sante
from interface import (DOSSIER_ANALYSES, _fichiers_veille, etat_sources, index_recherche,
                       lire_tendances, liste_veilles)

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

# Avant </body> : service worker (lecture hors connexion) et détection d'une nouvelle version.
PIED = """<script>
if ("serviceWorker" in navigator) {
  // Un changement de contrôleur alors qu'il y en avait déjà un = nouvelle version installée.
  let dejaControle = !!navigator.serviceWorker.controller;
  navigator.serviceWorker.addEventListener("controllerchange", () => {
    if (dejaControle && typeof signalerNouvelleVersion === "function") signalerNouvelleVersion();
    dejaControle = true;
  });
  navigator.serviceWorker.register("sw.js").catch(() => {});
}
</script>
</body>"""


# Politique de sécurité du contenu (CSP) : le navigateur refuse tout ce qui n'est pas
# listé ici. Seuls les scripts écrits dans la page (identifiés par leur empreinte), les
# données du site lui-même et les images de YouTube et d'Apple sont autorisés. Si un
# titre piégé réussissait à injecter du code, le navigateur refuserait de l'exécuter.
CSP = (
    "default-src 'none'; "
    "script-src {empreintes}; "
    "style-src 'unsafe-inline'; "  # styles écrits dans la page (aucun code exécutable)
    "img-src 'self' https://i.ytimg.com https://*.mzstatic.com; "
    "media-src 'self' blob:; "  # briefing audio (lu depuis le cache, hors connexion)
    "connect-src 'self'; "
    "manifest-src 'self'; "
    "worker-src 'self'; "
    "base-uri 'none'; "
    "form-action 'none'"
)


def _avec_csp(page: str) -> str:
    """Ajoute la CSP en tête de page, avec l'empreinte SHA-256 de chaque script de la page."""
    scripts = re.findall(r"<script>(.*?)</script>", page, flags=re.DOTALL)
    assert scripts and "<script " not in page, "script inattendu : la CSP ne le couvrirait pas"
    empreintes = " ".join(
        f"'sha256-{base64.b64encode(hashlib.sha256(s.encode('utf-8')).digest()).decode()}'"
        for s in scripts
    )
    balise = f'<meta http-equiv="Content-Security-Policy" content="{CSP.format(empreintes=empreintes)}">'
    # Juste après <meta charset> : la CSP doit précéder tous les scripts.
    assert page.count('<meta charset="utf-8">') == 1, "interface.html inattendu"
    return page.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + balise)


def _ecrire_json(chemin: Path, donnees) -> None:
    chemin.write_text(json.dumps(donnees, ensure_ascii=False), encoding="utf-8")


def _briefing_audio() -> None:
    """Dernier briefing : son texte, et sa version lue par la voix Piper (MP3). Une panne
    de la voix ne doit jamais empêcher la publication : le texte reste lisible."""
    b = briefing.dernier_briefing()
    if not b:
        _ecrire_json(SITE / "donnees" / "briefing.json", {"vide": True})
        return
    mp3 = f"briefing-{b['date']}.mp3"
    try:
        b["duree"] = briefing.synthetiser(b["texte"], SITE / "donnees" / mp3)
        b["audio"] = f"donnees/{mp3}"
        print(f"Briefing audio : {b['duree']} secondes.")
    except Exception as erreur:
        print(f"Briefing audio impossible ({type(erreur).__name__} : {erreur}) : texte seul.")
    _ecrire_json(SITE / "donnees" / "briefing.json", b)


def construire() -> int:
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "donnees").mkdir(parents=True)

    page = (RACINE / "interface.html").read_text(encoding="utf-8")
    assert page.count("</head>") == 1 and page.count("</body>") == 1, "interface.html inattendu"
    page = _avec_csp(page.replace("</head>", TETE).replace("</body>", PIED))
    (SITE / "index.html").write_text(page, encoding="utf-8", newline="\n")

    shutil.copy(PWA / "manifest.json", SITE / "manifest.json")
    shutil.copy(PWA / "sw.js", SITE / "sw.js")
    shutil.copytree(PWA / "icones", SITE / "icones")
    (SITE / ".nojekyll").write_text("")  # GitHub Pages : servir les fichiers tels quels

    fichiers = _fichiers_veille()
    for _, _, fichier in fichiers:
        shutil.copy(fichier, SITE / "donnees" / fichier.name)
    _ecrire_json(SITE / "donnees" / "veilles.json", {"veilles": liste_veilles()})
    _ecrire_json(SITE / "donnees" / "sources.json", etat_sources())
    _ecrire_json(SITE / "donnees" / "index.json", {"articles": index_recherche()})
    _ecrire_json(SITE / "donnees" / "tendances.json", lire_tendances() or {"vide": True})
    # Mémoire des feuilletons et dossiers du rédacteur en chef.
    for fichier in list(DOSSIER_RAPPORTS.glob("dossiers-*.json")) + [DOSSIER_RAPPORTS / "memoire.json"]:
        if fichier.is_file():
            shutil.copy(fichier, SITE / "donnees" / fichier.name)
    # Compteur de tokens Groq / Gemini (consommation.py).
    _ecrire_json(SITE / "donnees" / "consommation.json", {"jours": consommation.historique()})
    # Bilan de santé des dernières nuits (sante.py).
    _ecrire_json(SITE / "donnees" / "sante.json", {"jours": sante.historique()})
    # Journaux du pilote automatique (pilote.py).
    _ecrire_json(SITE / "donnees" / "pilote.json", {"jours": pilote.historique()})
    _ecrire_json(SITE / "donnees" / "paris.json", paris.historique())
    _briefing_audio()
    # Analyses de l'agent interprète (« Ce qui change »).
    for fichier in DOSSIER_ANALYSES.glob("analyse-*.json"):
        shutil.copy(fichier, SITE / "donnees" / fichier.name)
    return len(fichiers)


if __name__ == "__main__":
    n = construire()
    print(f"Site construit dans {SITE} ({n} fichiers de veille).")
