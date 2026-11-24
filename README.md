# Veille IA

Une veille quotidienne sur l'intelligence artificielle, **entièrement automatique et
gratuite**. Chaque nuit, des agents IA (LangChain + LangGraph) lisent la presse
francophone, américaine et chinoise ainsi que les blogs d'outils pour développeurs. Ils
retiennent et notent les meilleurs articles, écrivent des dossiers et un briefing audio,
puis publient le tout dans une app pour téléphone.

**L'app : <https://cychristmann.github.io/veille-ia/>**. Elle s'installe sur l'écran
d'accueil du téléphone (PWA) et se lit hors connexion.

---

## Ce que tu trouves dans l'app

| Rubrique | Contenu |
|---|---|
| **4 sections** | France, États-Unis, Chine, Outils & code : environ 50 articles chacune, notés de 1 à 10, regroupés par thème. Les titres étrangers sont traduits. |
| **Rubrique éphémère ⚡** | Ouverte seule par le pilote quand un sujet explose (ex. Jensen Huang, 24/11), puis fermée quand il retombe. |
| **Briefing audio** | La veille du jour racontée en 2 à 3 minutes. Le dimanche, l'édition de la semaine. |
| **À lire en priorité** | Les articles les mieux notés. |
| **Dossiers du jour** | Enquêtes du rédacteur en chef sur les sujets qui comptent. |
| **Ce qui change** | Ce que le graphe des connaissances révèle : sujets qui montent, nouveautés, liens nouveaux. |
| **Feuilletons** | Les histoires suivies d'un jour à l'autre. |
| **Cette semaine** | Tendances sur 7 jours : ce qui monte, ce qui retombe. |
| **Vidéos et podcasts** | 10 vidéos YouTube et 10 épisodes choisis par l'IA. |
| **Pilote automatique** | Ce que la veille a décidé seule cette nuit, et ses paris sur l'actualité. |
| **Favoris** | Tes articles étoilés, et l'export de tes goûts. |

Deux gestes utiles :
- **Partager vers l'app** (Android, app installée) : depuis n'importe quelle app,
  « Partager » > « Veille IA » affiche *« Qu'en dit ma veille ? »*.
- **👎 sur un article** (« moins de sujets comme celui-ci ») : avec tes étoiles, cela
  oriente doucement la notation (voir *Tes goûts* plus bas).

---

## Comment ça marche, chaque nuit

La mission tourne sur GitHub Actions (`.github/workflows/veille.yml`) vers 1 h du matin,
avec une seconde tentative à 5 h si la première n'a rien produit.

```
agent.py        les 4 sections : collecte -> tri -> traduction -> vérification -> notation
memoire.py      met à jour les feuilletons
redacteur.py    choisit les sujets du jour, enquête, rédige les dossiers
tendances.py    ce qui monte et retombe sur 7 jours
cerveau.py      verse la veille dans le graphe des connaissances (Graphify + Obsidian)
interprete.py   lit le graphe : « Ce qui change »
briefing.py     écrit le texte du briefing audio, puis vérifie ses liens de cause
pilote.py       bilan de la nuit, réglages, paris (voir plus bas)
publier.py      construit le site ; la voix Piper lit le briefing (MP3)
```

Les étapes facultatives (cerveau, interprète, briefing, pilote) peuvent échouer sans
bloquer la publication. Le voyant « État de la nuit » de l'app (`sante.py`) le signale
alors.

### Le pilote automatique (`pilote.py`)

Une « mini AGI » qui fait vivre la veille seule. Chaque nuit, elle **observe** ses propres
résultats, **décide** (l'IA accepte ou refuse les actions préparées par le code),
**agit**, puis tient un journal :

- **Médias** : il met en pause un média en panne, abandonné ou hors sujet. Un blog calme
  n'est pas mis en pause. Il cherche de nouveaux médias chaque semaine, et tout de suite
  pour une section qui manque de liens directs 3 nuits de suite. Il garde ou retire les
  médias à l'essai après 7 jours.
- **Relance** d'une section ratée.
- **Expériences** sur les réglages (fenêtre de collecte, part de Google Actualités…),
  gardées seulement si le score mesuré progresse.
- **Rubrique éphémère** sur un sujet en éruption.
- **Paris** (`paris.py`) sur l'actualité des jours suivants, tranchés par les veilles
  suivantes. Chaque pari est comparé au passé, et un pari que l'historique donne perdant
  est refusé.

Garde-fous : plafonds d'actions par nuit, verdicts mesurés imposés, retour arrière si une
pause fait perdre des articles, mode sans IA si l'IA est indisponible.

### Tes goûts (`gouts.py`)

Tes étoiles, les articles que tu ouvres et tes 👎 restent sur ton téléphone. Pour les
transmettre à la veille :

1. Dans l'app, ouvre la vue Favoris et touche **« Exporter mes goûts »**.
2. Dépose le fichier `mes-gouts-AAAA-MM-JJ.json` dans le dossier `preferences/` du projet.
   Il n'est **pas** envoyé sur GitHub, car le dépôt est public.
3. Lance `uv run python gouts.py`. L'IA en tire un profil de sujets
   (`preferences/profil.json`), seul fichier publié.

La notation bouge alors d'un point au plus selon tes goûts, et une nouvelle majeure n'est
jamais écartée.

---

## Sur ton PC

Le projet utilise **uv**. Jamais pip, jamais le Python du système.

```bash
uv sync                                  # installer les dépendances
uv run python agent.py                   # lancer une veille (4 sections)
uv run python interface.py               # l'app en local, avec le chat sur l'historique
uv run python briefing.py                # écrire le briefing du jour
uv run python briefing.py --audio b.mp3  # l'écouter
uv run python paris.py                   # trancher et faire les paris du jour
uv run python gouts.py                   # mettre à jour ton profil de goûts
uv run pytest -q                         # les tests automatiques
uv add paquet                            # ajouter une dépendance (jamais autrement)
```

Les clés vont dans un fichier `.env`, jamais envoyé sur GitHub :

```
GROQ_API_KEY=...      # obligatoire (modèle gpt-oss-120b, gratuit)
GEMINI_API_KEY=...    # secours gratuit quand Groq refuse, et extraction du graphe
YOUTUBE_API_KEY=...   # facultatif : rubrique Vidéos
```

Sur GitHub, les mêmes clés se règlent dans *Settings > Secrets and variables > Actions*.

### Les tests (`tests/`)

29 tests sans réseau ni IA vérifient la logique du pilote, des paris, de la rubrique
éphémère, du garde-fou de quota, du briefing, des goûts et de la sécurité de la page.
Ils tournent sur GitHub à chaque envoi de code. Si l'un d'eux échoue, rien n'est publié :
l'ancienne version du site reste en ligne.

---

## Les fichiers

| Dossier ou fichier | Rôle |
|---|---|
| `veilles/` | Historique : veilles, dossiers, briefings, feuilletons (`memoire.json`), tendances, consommation d'IA. |
| `cerveau/` | Deuxième cerveau : coffre Obsidian (`coffre/`), graphe Graphify (`graphify-out/`), analyses. |
| `pilote/` | État du pilote (`etat.json`), journaux de chaque nuit, paris (`paris.json`). |
| `sources.json` | Médias ajoutés par la découverte, et propositions. |
| `preferences/` | Ton profil de goûts. Tes exports bruts restent sur ton PC. |
| `interface.html` | L'app, dans un seul fichier. `pwa/` contient le manifeste, les icônes et le service worker. |
| `consommation.py`, `sante.py` | Compteur de tokens et bilan de santé de chaque nuit. |
| `multimedia.py`, `sources.py`, `chat.py` | Vidéos et podcasts, découverte de médias, chat sur l'historique (local). |

## Coûts et limites

**Tout est gratuit :**
- Groq (offre gratuite : 200 000 tokens par jour) et Gemini (secours) pour l'IA ;
- GitHub Actions et GitHub Pages pour la mission de nuit et le site ;
- Piper pour la voix (sur la machine, sans service extérieur).

**Garde-fou de quota :** au-delà de 85 % du quota Groq du jour, toutes les étapes sauf la
veille des 4 sections passent d'abord par Gemini.

**Contenus :** les titres et les articles sont toujours traités comme des données. Une
politique de sécurité (CSP) empêche un titre piégé d'exécuter du code dans l'app. Aucune
protection de site n'est contournée : seuls les flux RSS publics et les API officielles
sont lus.
