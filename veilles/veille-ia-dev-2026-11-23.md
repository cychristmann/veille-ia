# Veille IA outils & code du 23/11/2026

50 articles de médias tech anglophones et francophones (blogs d'outils, Hacker News, Product Hunt) publiés ces 48 dernières heures (rapport généré à 08:35).

Sources inaccessibles : Hacker News.

## Synthèse du jour

Les dernières heures ont été marquées par une avalanche d’annonces autour des modèles de langage et des infrastructures IA, avec notamment GLM‑5.4, GPT‑6.2, Claude Fable 5.2 et la nouvelle Agent Compute Engine de Google. Le paysage des outils de codage assisté s’est enrichi : Claude Code, Cursor, Copilot et leurs extensions font l’objet de guides, comparaisons et retours d’expérience, tandis que des projets comme SecondBrain VoicePad ou des intégrations via MCP montrent la diffusion de ces agents dans des produits concrets. En parallèle, la sécurité des assistants de programmation est sous les projecteurs, plusieurs articles signalant fuites de secrets, malwares ciblant ces outils et mesures de vérification. Enfin, des courants novateurs comme le "vibe‑coding" émergent, promettant de transformer la création logicielle et même la fabrication grâce à l’IA.

*Vérifiée : chaque affirmation est appuyée par au moins un titre.*

## À lire en priorité

- [Le mathématicien d'Anthropic Levent Alpöge affirme que Claude a aidé à prouver l'hypothèse de Riemann, vérification en cours](https://cryptobriefing.com/claude-riemann-hypothesis-proof-claim/) — *Crypto Briefing*, 23/11 06:04 · **8/10** (Affirmation majeure sur Riemann, même si vérification en attente)
  *Titre original : Anthropic mathematician Levent Alpöge says Claude helped prove the Riemann hypothesis, verification pending*
  > If verified, this breakthrough could revolutionize AI's role in solving complex mathematical problems, impacting future research methodologies. The post Anthropic mathematician Levent Alpöge says Claude helped prove the Riemann hypothesis, verification pending appeared first on Crypto Briefing .
- [NVIDIA lance Alpamayo 2 Edge : un VLA de raisonnement 2 M de paramètres pour DRIVE Thor](https://www.marktechpost.com/2026/11/22/nvidia-alpamayo-2-edge-2b-reasoning-vla-drive-thor/) — *MarkTechPost*, 22/11 19:37 · **8/10** (NVIDIA lance Alpamayo 2 Edge, modèle de raisonnement 2 B)
  *Titre original : NVIDIA Releases Alpamayo 2 Edge: A 2B Reasoning VLA for DRIVE Thor*
  > NVIDIA released Alpamayo 2 Edge, a 2B-class reasoning vision-language-action model that plans driving trajectories and explains them on DRIVE AGX Thor, at 160 to 190 ms pixel-to-trajectory latency. The post NVIDIA Releases Alpamayo 2 Edge: A 2B Reasoning VLA for DRIVE Thor appeared first on MarkTech
- [Ant rend open source les modèles d'IA médicale pour une utilisation en santé](https://itbrief.com.au/story/ant-open-sources-medical-ai-models-for-healthcare-use) — *IT Brief Australia*, 23/11 08:31 · **7/10** (Nouveau modèle médical open‑source, impact potentiel important)
  *Titre original : Ant open-sources medical AI models for healthcare use*
  > The move puts two core models into public hands as Ant expands healthcare AI across an app used by 150 million people.
- [Together AI révèle une fuite de prompts après l’étude de Dragos](https://news.google.com/rss/articles/CBMijwFBVV95cUxNSURBLXVrRHVYYW9Xbm1zUzVaOXVJeUM2Ulh4VGVRcEMtTkFPVTkzWUlPUktadUxHQVBPVVRpTWVXV0czUnVXX2tpdDVOMTVnTWlncWVNQ2NKRWlyeWdmRjl2d1cxQjkxM3NIM3hVUEhHNU5KdTNROXFBbFU5Zy1RRzQtaVlCeGJoVXZjT0JEZw?oc=5) — *The Defiant*, 22/11 21:52 · **7/10** (Fuite de prompts d’une IA majeure, incident notable)
  *Titre original : Together AI Discloses Prompt Leak After Dragos Study*
- [Unreal Engine 6 abandonnera une fonctionnalité de script clé plus tôt que prévu au profit du codage IA](https://news.google.com/rss/articles/CBMizgFBVV95cUxQMGJZb0E4NWI2MnB2OUJvYm83eDZwWmt2X3hJRkNJejg4MmNNV1dSdEdsTnE0Y19WS3ZieXY0WW52Wm1fbzVmWTc0NmlYU2FCLWF5SkhMSTNWMGNodF81VndRUFRfU0FrWGY5a05ZTUNwRlMwODU4NjFibDRscWdxcmd2cFd1UXZCMklwSG42LXRFX2hWZktveXZGMlRDZi1Ra0pWcjZVM09XZlhaSUp3RTVEeEZCZG1SLXRqbUJ4TkFXUXA5YXVOY3p3RHVMZw?oc=5) — *PC Gamer*, 22/11 21:33 · **7/10** (Unreal Engine 6 supprime script, mise en avant IA coding)
  *Titre original : Unreal Engine 6 to jettison key scripting feature earlier than planned in favor of AI coding*

## Modèles et frameworks IA (10)

Plusieurs articles annoncent ou décrivent de nouveaux modèles, frameworks ou infrastructures IA, allant de modèles de langage (GLM‑5.4, GPT‑6.2, Claude Fable 5.2) à des plateformes de calcul spécialisées (Agent Compute Engine, Alpamayo 2 Edge). On retrouve également des travaux sur le déploiement local d’IA (RDMA over USB4, modèles open‑weight sur PC domestiques).

- [NVIDIA lance Alpamayo 2 Edge : un VLA de raisonnement 2 M de paramètres pour DRIVE Thor](https://www.marktechpost.com/2026/11/22/nvidia-alpamayo-2-edge-2b-reasoning-vla-drive-thor/) — *MarkTechPost*, 22/11 19:37 · **8/10** (NVIDIA lance Alpamayo 2 Edge, modèle de raisonnement 2 B)
  *Titre original : NVIDIA Releases Alpamayo 2 Edge: A 2B Reasoning VLA for DRIVE Thor*
  > NVIDIA released Alpamayo 2 Edge, a 2B-class reasoning vision-language-action model that plans driving trajectories and explains them on DRIVE AGX Thor, at 160 to 190 ms pixel-to-trajectory latency. The post NVIDIA Releases Alpamayo 2 Edge: A 2B Reasoning VLA for DRIVE Thor appeared first on MarkTech
- [Ant rend open source les modèles d'IA médicale pour une utilisation en santé](https://itbrief.com.au/story/ant-open-sources-medical-ai-models-for-healthcare-use) — *IT Brief Australia*, 23/11 08:31 · **7/10** (Nouveau modèle médical open‑source, impact potentiel important)
  *Titre original : Ant open-sources medical AI models for healthcare use*
  > The move puts two core models into public hands as Ant expands healthcare AI across an app used by 150 million people.
- [Google annonce Agent Compute Engine pour l’exécution sécurisée d’agents IA](https://www.infoq.com/news/2026/11/google-agent-compute-engine/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 22/11 07:30 · **7/10** (Google lance Agent Compute Engine, infrastructure clé pour agents IA)
  *Titre original : Google Announces Agent Compute Engine for Secure AI Agent Execution*
  > Google recently announced Agent Compute Engine, a managed service that runs AI agents in isolated microVMs, with checkpointing capabilities to suspend and resume execution environments. The design keeps credentials, API keys, and OAuth refresh tokens outside the agent sandbox, using an external Agen
- [Microsoft teste le RDMA sur USB4 pour l'IA locale distribuée sous Windows 11](https://news.lavx.hu/article/microsoft-tests-rdma-over-usb4-for-distributed-local-ai-on-windows-11) — *news.lavx.hu*, 23/11 06:01 · **6/10** (Test RDMA over USB4, avancée technique pour IA distribuée)
  *Titre original : Microsoft tests RDMA over USB4 for distributed local AI on Windows 11*
  > Microsoft is testing Remote Direct Memory Access over USB4 in Windows 11, letting PCs share memory for local AI model runs. The developer preview cut small-message latency by about four times versus Ethernet in early tests, but it requires multiple USB4 ports, NetworkDirect app support and manual ha
- [Les modèles à poids ouvert apportent des assistants IA privés sur les PC domestiques](https://news.lavx.hu/article/open-weight-models-bring-private-ai-assistants-to-home-pcs) — *news.lavx.hu*, 23/11 05:13 · **6/10** (Modèles open‑weight pour assistants privés, tendance forte)
  *Titre original : Open-weight models bring private AI assistants to home PCs*
  > Desktop tools like Unsloth Desktop and open-weight models from Qwen and Thinking Machines Lab let users run private AI chatbots on consumer hardware, though cost and memory limits keep the setup out of reach for many.
- [GLM‑5.4 arrive sur le plan de codage de Z.ai : aucun benchmark pour l’instant](https://news.google.com/rss/articles/CBMia0FVX3lxTE9iNktnU3JGMUdTamh3RlhTN2RacGR2dGVSYnV5Sm9hblVZUFZ5OUxsQmxOMUZHbVRXNXVNUC1rTHhOOEdrVnZkQmFZMkhKcWxrQkp0VjdnNUdtWm91MWoyUUVQNGNMYkFNaVNR?oc=5) — *OrcaRouter*, 23/11 07:52 · **5/10** (Arrivée du modèle GLM‑5.4, nouveauté mais peu de benchmarks)
  *Titre original : GLM-5.4 Arrives on Z.ai's Coding Plan: No Benchmarks Yet*
- [GPT‑6.2 Astra vs Claude Fable 5.2 : le lancement d’Astra a reçu des avis partagés, mais ses performances sont bonnes ici](https://thenewstack.io/gpt-6-2-astra-vs-claude-fable-5-2/) — *The New Stack*, 22/11 16:00 · **5/10** (Comparatif GPT‑6.2 vs Claude Fable, avis mitigés)
  *Titre original : GPT-6.2 Astra vs. Claude Fable 5.2: Astra’s launch got mixed reviews, but it tested well here*
  > When I compared Anthropic’s Fable 5.2 vs. OpenAI’s GPT-6 Astra last week, Fable 5.2 was slightly more accurate (149 points The post GPT-6.2 Astra vs. Claude Fable 5.2: Astra’s launch got mixed reviews, but it tested well here appeared first on The New Stack .
- [Google AI prévisualise la récupération d’outils dans l’API Gemini pour les grandes bibliothèques d’outils](https://www.marktechpost.com/2026/11/22/google-gemini-api-tool-retrieval/) — *MarkTechPost*, 22/11 11:03 · **5/10** (Preview d’outil de récupération Gemini, fonctionnalité intéressante)
  *Titre original : Google AI Previews Tool Retrieval in the Gemini API for Large Tool Libraries*
  > Google launched Gemini API Tool Retrieval in preview. Agents keep a large tool library on standby and load each parameter schema only when needed, inside one Interactions API request. The post Google AI Previews Tool Retrieval in the Gemini API for Large Tool Libraries appeared first on MarkTechPost
- [Réseaux de neurones graphiques : fonctionnement et applications](https://dev.to/o2soft/graph-neural-networks-how-they-work-and-their-uses-ajc) — *dev.to*, 23/11 08:31 · **4/10** (Article pédagogique sur GNN, peu de nouveauté concrète)
  *Titre original : Graph Neural Networks: How They Work and Their Uses?*
  > Graph Neural Networks (GNNs) are changing how artificial intelligence understands complex relationships between connected data points. Unlike traditional machine learning models that process information as rows, tables, or independent data points, Graph Neural Networks analyze connections between en
- [Muru](https://simonwillison.net/2026/Nov/21/muru/) — *Simon Willison*, 22/11 00:56 · **2/10** (Référence obscure, pas de valeur informative)
  *Titre original : Muru*
  > Muru Graham Dumpleton started mod_wsgi 20 years ago, and has been thinking about the ideal way to serve Python web applications in production ever since. Muru is his new, AI-assisted Rust server that aims to provide the best possible tools for running ASGI and WSGI Python apps both in development an

## Outils de codage assisté par IA (17)

Cette catégorie regroupe les outils et agents de programmation IA ainsi que leurs guides d’utilisation : Claude Code (débutants, prompts, leçons, fuites), Cursor, Copilot, Codex, ainsi que des projets qui les intègrent (SecondBrain VoicePad, projets personnels, comparaisons de prix).

- [Le mathématicien d'Anthropic Levent Alpöge affirme que Claude a aidé à prouver l'hypothèse de Riemann, vérification en cours](https://cryptobriefing.com/claude-riemann-hypothesis-proof-claim/) — *Crypto Briefing*, 23/11 06:04 · **8/10** (Affirmation majeure sur Riemann, même si vérification en attente)
  *Titre original : Anthropic mathematician Levent Alpöge says Claude helped prove the Riemann hypothesis, verification pending*
  > If verified, this breakthrough could revolutionize AI's role in solving complex mathematical problems, impacting future research methodologies. The post Anthropic mathematician Levent Alpöge says Claude helped prove the Riemann hypothesis, verification pending appeared first on Crypto Briefing .
- [Outils de coordination des agents de code Codex et Claude, comparatif](https://dev.to/maxz411/tools-for-coordinating-codex-and-claude-code-agents-compared-n95) — *dev.to*, 23/11 08:28 · **6/10** (Comparaison d’outils de coordination Codex/Claude, usage direct)
  *Titre original : Tools for coordinating Codex and Claude Code agents, compared*
  > Which tool fits depends on three questions: do your agents include Codex as well as Claude Code, do they run on one computer or several, and is it just you or a team? If you only use Claude Code, its built-in agent teams and cross-session messaging cost nothing extra. For Codex and Claude Code on on
- [Comment installer Claude Code sur Android avec Termux](https://hackernoon.com/how-to-install-claude-code-on-android-with-termux?source=rss) — *HackerNoon*, 22/11 17:32 · **6/10** (Guide d’installation Android, couverture par deux médias, utilité pratique)
  *Titre original : How to Install Claude Code on Android With Termux*
  > Learn how to run Claude Code on Android using Termux, Ubuntu, and proot-distro, with installation steps, troubleshooting tips, and limitations.
- [Claude Code fuit des secrets via sa fonction « Don’t Ask Again »](https://www.infoq.com/news/2026/11/claude-code-leaking-secrets/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 22/11 12:00 · **6/10** (Fuite de secrets via fonction « Don’t Ask Again », problème de confidentialité)
  *Titre original : Claude Code Has Been Leaking Secrets through its "Don't Ask Again" Feature*
  > Agentic security firm Apiiro found that Claude Code has been exposing secrets in public repositories due to how it stores them in local file on developers' machines to implement "Don't Ask Again". The company identified 1,122 secrets in claude/settings.local.json files and another 1,160 in git histo
- [US AI Pulse : l'IA a transformé les preuves papier de Raft en code fonctionnel](https://dev.to/rpgbyters/us-ai-pulse-ai-just-helped-turn-rafts-paper-proofs-into-working-code-4aia) — *dev.to*, 23/11 08:31 · **5/10** (Démo de conversion papier‑preuve → code, intéressant pour développeurs)
  *Titre original : US AI Pulse: AI Just Helped Turn Raft’s Paper Proofs Into Working Code*
  > US AI Pulse: AI Just Helped Turn Raft’s Paper Proofs Into Working Code The Raft consensus protocol had already earned an unusually respectable paper trail: extensively studied, formally specified, and rigorously proven correct under certain assumptions. The catch was that production implementations 
- [Un ingénieur d'Anthropic explique comment éviter les limites de jetons de Claude Code](https://news.google.com/rss/articles/CBMia0FVX3lxTE9rWGg5MVJZVU1jM000NGhfLXRVZkRsczlKbjJCcGt4MG5UQnZXSk5vcm8tYVI0WmJDbWxxR0hMdzVvRF9Gdm55WC03LU1laWxSN0NtZUUzZTRhbkN4WGxMYVZ4aG1pSjQyRHdn?oc=5) — *Geeky Gadgets*, 23/11 08:13 · **5/10** (Conseils pratiques d’Anthropic, améliore l’usage de Claude Code)
  *Titre original : Anthropic Engineer Shares How to Avoid Hitting Claude Code Token Limits*
- [Claude Code pour débutants : comment commencer et 5 prompts puissants à tester](https://news.google.com/rss/articles/CBMirwFBVV95cUxPRVQtT1IwSzdId1VsNU8wQTlHZVFSRlRBX0EtVXFRd2hYbVJpWGFjSzl6N0tVQUJsbjdtOFUwNXg0aFE3Zk1CUmNmMzdBajl4dVd2MF9ZbDk3aTZLRHgzWFU1WTl3clBfZTc1bEo5WDh6QnYxLTV5M1dRTDlDVFZJb1NfMlhpdXU1WXNCTkxGRXlkbEZVWUF1R1N0RHdNcktsWXFKRXhxVENSY0JPMXFZ?oc=5) — *Tom's Guide*, 23/11 07:36 · **4/10** (Guide débutant Claude Code, utile mais pas novateur)
  *Titre original : Claude Code for beginners — how to get started and 5 powerful prompts to try*
- [Cursor vs Copilot : chevauchement – 12 étapes, 70 minutes](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOX293SXJpYUFsLXBFMlVlbzNYSmYxc1BLZ1BRSnBhUThBUmhXSG9XaGRZemQ1UTY0SkwxWnZ6WjludW1KUk9idXpqajl6anVORGRrQ1pRclJ0aWZiRWNJeGVZaDAwc2wzQXF6UlMtdVBZTjJMTTlZVUNqYTZ1dE1GUHE2VGxBYXVQ?oc=5) — *shattered.io*, 23/11 04:19 · **4/10** (Comparaison Cursor vs Copilot, intérêt limité)
  *Titre original : Cursor vs Copilot Overlap: 12 Steps, 70 Min*
- [Cline vs Claude Code : forfaits à 9,99 $ contre 20 $](https://news.google.com/rss/articles/CBMickFVX3lxTE5KV3d0a3JrWGI3N2pxT3A0ZklFdHlWbnVOcDNianRtNnNtQS1RNzdTU0FmQTBhZjA0OC1pRHRkTzNRb1JkRXpRczU0ZXhQR2ZZM1FQOU5LeHJvVVl4bGJxeFkwYUxzRVl2MkZVY1ZIVkRPZw?oc=5) — *shattered.io*, 22/11 15:59 · **4/10** (Comparaison tarifaire, peu d’impact technique)
  *Titre original : Cline vs Claude Code: $9.99 vs $20 Plans*
- [Utiliser Claude Code gratuitement ? Test de Freebuff, qui promet un codage IA quasi illimité](https://www.notebookcheck.net/Use-Claude-Code-for-free-I-test-Freebuff-which-promises-virtually-unlimited-AI-coding.1455441.0.html) — *Notebookcheck*, 22/11 15:30 · **4/10** (Test d’accès gratuit Claude Code, intérêt limité)
  *Titre original : Use Claude Code for free? I test Freebuff, which promises virtually unlimited AI coding*
  > A free AI coding agent as an alternative to Claude Code and OpenCode. How well does it work, and what privacy risks should you be aware of?
- [Mode Code de Claude Code : 62 entrées de changelog en 8 jours](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPM21sVmlia1EzY1B6WFU0dXdBV0ZmeThFVURaeVk0TGNHSERBdEFqOC1DbTRZZ3cxbTloR3IwNWRONjBPMWJ4aFN2ZUJ3MzJ2MTk5bjNGQ040NUdYZmxyNFhCZ2w0Ry14dGU4ZnFqbk15Mm80OFpRTm5fYUYtaXVVcjJ3b3NsZ3Zx?oc=5) — *FourWeekMBA*, 22/11 12:37 · **4/10** (Changelog de Code Mode, évolution rapide mais peu stratégique)
  *Titre original : Claude Code’s Code Mode: 62 Changelog Entries in 8 Days*
- [Mod multijoueur de The Last of Us Part 2 : douze semaines de lancement gratuit, Claude Code utilisé pour la majeure partie](https://www.msn.com/en-us/gaming/action-adventure-games/the-last-of-us-part-2-multiplayer-mod-twelve-weeks-launches-free-claude-code-used-for-most-of-it/ar-AA2i1Gjq) — *Tech Times*, 23/11 07:05 · **3/10** (Mod de jeu utilisant Claude Code, anecdote de niche)
  *Titre original : The Last of Us Part 2 Multiplayer Mod: Twelve Weeks Launches Free, Claude Code Used for Most of It*
  > The Last of Us Part 2 multiplayer mod Twelve Weeks launched free on Nov. 20 as a clan-based 4v4 Factions-style mode for Part II Remastered on PC. It needs your own Steam copy, runs on Windows, Linux ...
- [Quelqu'un a utilisé Claude Code pour créer un sablier bloquant les applications distrayantes, l'un des 5 projets fous](https://www.xda-developers.com/someone-used-claude-code-to-build-hourglass-one-of-five-projects/) — *XDA*, 23/11 01:30 · **3/10** (Projet ludique avec Claude Code, peu d’impact général)
  *Titre original : Someone used Claude Code to build an hourglass that blocks distracting apps, and that's just one of 5 wild projects*
  > The side where people are using AI to bring ideas to life that they probably wouldn't have had the skills, resources, or time to build otherwise. So, here are some really cool projects I came across ...
- [LiberNT GitHub : AI + AGENTS.md pour le fork du système d'exploitation Windows 11](https://news.google.com/rss/articles/CBMihwFBVV95cUxQSjNjd0lLTndEaXVEaVZlMEtsMkQ3Ylowc0VhR3Rha0o5SVVRdHdSVzRScnFTM1JXbUFsUHNhb0FfZDJFcVBRckltRl9reVBQeVdublRaZzNDX21WYkJNR0sxM1hCbklvT0JNVXJibEdJMmVzN28wc3JWb3VGdTdJZ2FtQURvWFU?oc=5) — *explainx.ai*, 23/11 01:00 · **3/10** (Fork GitHub, peu de visibilité)
  *Titre original : LiberNT GitHub: AI + AGENTS.md for Windows 11 OS Fork*
- [J’ai reconstruit le même site web deux fois avec Claude Code, et une compétence de design gratuite a tout changé](https://www.xda-developers.com/built-the-same-website-twice-with-claude-code-one-free-design-skill-made-all-the-difference/) — *XDA*, 22/11 23:31 · **3/10** (Répétition de projet web, anecdote)
  *Titre original : I built the same website twice with Claude Code, and one free design skill made all the difference*
  > Fortunately, I found one free design skill that works across Claude Code, Codex, Cursor and OpenCode that seems to have made its entire mission to put an end of AI-generated design slop. The problem I ...
- [Meilleurs agents IA personnels en 2026 : OpenClaw, Hermes Agent, Gemini Spark et autres, comparés sur la mémoire, la sécurité et le coût](https://www.marktechpost.com/2026/11/22/best-personal-ai-agents-2026/) — *MarkTechPost*, 22/11 11:36 · **3/10** (Classement d’agents personnels, plus opinion que nouveauté)
  *Titre original : Best Personal AI Agents in 2026: OpenClaw, Hermes Agent, Gemini Spark and More, Compared on Memory, Security and Cost*
  > Hermes Agent, OpenClaw, Gemini Spark, OpenAI dots, Meta Muse and Perplexity Personal Computer ranked on memory, security defaults and real cost. The post Best Personal AI Agents in 2026: OpenClaw, Hermes Agent, Gemini Spark and More, Compared on Memory, Security and Cost appeared first on MarkTechPo
- [oovi](https://www.producthunt.com/products/oovi) — *Product Hunt*, 21/11 21:02 · **2/10** (Mention d’un produit inconnu, aucune donnée exploitable)
  *Titre original : oovi*
  > Your own team of AI on your desktop Discussion | Link

## Sécurité, conformité et fuites liées aux IA (9)

Plusieurs titres portent sur les risques de sécurité associés aux assistants de codage IA : fuites de secrets, malwares ciblant les assistants, prompts compromis, vérifications de code, et protocoles de protection (Bitdefender, recherches sur les fuites de Claude Code, NordLayer, etc.).

- [Together AI révèle une fuite de prompts après l’étude de Dragos](https://news.google.com/rss/articles/CBMijwFBVV95cUxNSURBLXVrRHVYYW9Xbm1zUzVaOXVJeUM2Ulh4VGVRcEMtTkFPVTkzWUlPUktadUxHQVBPVVRpTWVXV0czUnVXX2tpdDVOMTVnTWlncWVNQ2NKRWlyeWdmRjl2d1cxQjkxM3NIM3hVUEhHNU5KdTNROXFBbFU5Zy1RRzQtaVlCeGJoVXZjT0JEZw?oc=5) — *The Defiant*, 22/11 21:52 · **7/10** (Fuite de prompts d’une IA majeure, incident notable)
  *Titre original : Together AI Discloses Prompt Leak After Dragos Study*
- [Bitdefender signale un malware ciblant les assistants de codage IA](https://news.google.com/rss/articles/CBMilgFBVV95cUxNY2lpR1dpMndaUEwzUmhwZTF0QmV3U0Yta09ZZUI5NW0xVno2WG1GSjNIcFdhaGxnR2hTdTVGdzEydk10Snk2dW4wYzhoSmN3ZTFjYVMxb1BwdUY0UFdmTjZWZlFySUk0aTRVbDVwUHVOSHM2bjJiZDFHT1B0SE1Kdzk5dHRsanhmQVRNOW42NEhSTjlKaGc?oc=5) — *SecurityBrief Australia*, 23/11 02:35 · **6/10** (Malware ciblant assistants IA, sécurité cruciale)
  *Titre original : Bitdefender flags malware targeting AI coding assistants*
- [Des chercheurs découvrent plus de 2 000 secrets exposés liés aux règles d’approbation de Claude Code](https://www.online-tech-tips.com/claude-code-secrets-exposed-approval-rules/) — *Online Tech Tips*, 22/11 18:38 · **6/10** (Exposition de >2 000 secrets liés à Claude Code, problème de sécurité)
  *Titre original : Researchers find more than 2,000 exposed secrets linked to Claude Code approval rules*
  > Claude Code secrets exposed: a 'don't ask again' approval setting left thousands of passwords and API keys in public GitHub repos. Here's what to check now.
- [Des chercheurs en sécurité montrent comment les fournisseurs d’inférence IA bon marché volent les clés et espionnent les utilisateurs](https://the-decoder.com/security-researchers-show-how-cheap-ai-inference-providers-steal-keys-and-snoop-on-users/) — *The Decoder*, 22/11 13:07 · **6/10** (Recherche sur vol de clés par fournisseurs IA low‑cost, enjeu sécurité)
  *Titre original : Security researchers show how cheap AI inference providers steal keys and snoop on users*
  > Security researchers at Dragos used two million fake AI requests to uncover serious vulnerabilities in the AI supply chain, finding at least three compromised providers, hundreds of stolen AWS keys, and marketplace resellers who were simply reading customer requests. OpenRouter responded by removing
- [Boucles de vérification dans Claude Code : comment Anthropic contrôle le code des agents](https://news.google.com/rss/articles/CBMipwFBVV95cUxNbTNqVHZRancwV2p4X0pFdWpHWUpYWWlad29BSV9lbFVhZFdnbUpiM1E5THdNc1BBMWJwaDUzZS1qNl9reWR6TDR1dGFLUWpNWi1WM3FITF9XRzVFY29PZExhMmlNV3NXSVFGbl9JSFJFYjBxNW5qVzBMZG9vTGRDTXhUSWRPOEdoendEMnNpOUwxTEJuTUgwbkhTNGx3TklTYXZJWTlVbw?oc=5) — *Pasquale Pillitteri*, 22/11 15:10 · **5/10** (Boucles de vérification Claude Code, transparence technique)
  *Titre original : Verification loops in Claude Code, how Anthropic checks agent code*
- [NordLayer AI Scout détecte des fuites de mots de passe par un assistant de codage lors de 10 sessions](https://news.google.com/rss/articles/CBMimgFBVV95cUxQZzhES3hrM3ppLTJWLXg3S3FLWWZyaW5HTW5NZEs1NXRYWnJuaEdmdmtvdS1Na255TUdWeFAyckx0ZFFUWDNRYnVVSmxQZTdMLWpXc2lkTnh6dVhfLW82NE94U3VVbmM1TDR0WHhreHpheHNMekQxZ2twT3lpYzBQeE1rNnlfcFNBM1NGSnFZRGI2Y2RFODFhOGN3?oc=5) — *Qoo Media*, 22/11 10:17 · **5/10** (Détection de fuites de mots‑de‑passe par assistant IA, alerte sécurité)
  *Titre original : NordLayer AI Scout Finds Coding Assistant Leaked Passwords in 10 Sessions*
- [Fuite de prompts chez Together AI : 3 modèles, 4 jours, 1 credential](https://news.google.com/rss/articles/CBMijgFBVV95cUxQbjBXUTRDUkhhclRQOG1TLWRadFgtZ0l2Y1otQ1JNbWpINTh5dHpJc25DaFlGVFRfNGFocVdaWk9BWWNqN2E1QllkRTFJa2V3MWVrSzRkZzdyb2dJTXp0dlQzZFc1V0FCbkY2U2xybDVqcThiUkt1SzI5OEtKcVE0cDE3SWxRWk1XZ1k1aTNR?oc=5) — *shattered.io*, 22/11 09:49 · **5/10** (Nouvelle fuite de prompts, incident technique)
  *Titre original : Together AI Prompt Leak: 3 Models, 4 Days, 1 Credential*
- [RunPod retire la commande MCP demandant aux agents IA de cacher un sondage aux utilisateurs](https://news.google.com/rss/articles/CBMinAFBVV95cUxOcTV4bFVGVzQzWWdRdWhSQVZNYkxHdDRQSVpkSXdhdTBDWE5HMzU0alJaSVowUzZoS0dtUlZzZ2NmQ1ZFeFpxY2w5X2MySGcxS0ljV19SaTJjNG5JSVRRT0tTTHJKTkFOZTRmUG5iQk53SmFEMnN4WW5uTEpEbmRyc0lpZUpTNl9rQXBfWG1MLU13am9oaV9jeGM4SFo?oc=5) — *Pasquale Pillitteri*, 22/11 08:34 · **3/10** (Retrait de commande MCP, peu d’impact)
  *Titre original : RunPod withdraws MCP order telling AI agents to hide a survey from users*
- [Résumé : les commerçants d’Adyen peuvent désormais proposer Klarna à la caisse avec un agent IA](https://www.01net.it/riassunto-i-commercianti-di-adyen-ora-possono-offrire-klarna-alla-cassa-con-agente-ai/) — *01net*, 22/11 08:22 · **3/10** (Annonce commerciale locale, peu pertinent pour le dev IA)
  *Titre original : Riassunto: I commercianti di Adyen ora possono offrire Klarna alla cassa con agente AI*
  > Klarna è il primo metodo di pagamento locale, senza carta, di Adyen per il commercio agenticoNEW YORK--(BUSINESS WIRE)--Klarna (NYSE: KLAR), la rete finanziaria per tutti i giorni, e Adyen (AMS: ADYEN) oggi hanno annunciato che ora i consumatori posso... L'articolo Riassunto: I commercianti di Adyen

## Nouvelles approches de développement (vibe‑coding, AI‑driven) (4)

Des articles introduisent ou explorent des concepts émergents comme le « vibe‑coding », une façon de coder assistée par IA, ainsi que des mouvements de design et de fabrication pilotés par IA. Ces initiatives visent à réinventer le processus créatif et de production.

- [Les outils de codage IA transforment l’ingénierie logicielle, et certains développeurs regrettent la difficulté](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNUmpMQ2xKQkRLMjFaRkpTRWxnWWlxaTJZRFltcDAyN0FQRzRuZVJJckFYM01mbEZrYWRodFE4T0gtMGRqM1RqcU9BVmtJRFF3MTZiem83aG5Gal95OFg5dElsWnhjMHd0TndZMzR0OWNEZEtsTVJZdUpEWkZ5Y2JxWGEwMkkzclZvQ0hnUXlaZUxKTUd0SnA2Q21uWC1jYWJLakNYUTduQ1hMVWtnU0lxaUY0aExaR3Q0SGZj?oc=5) — *kalkine.com*, 22/11 18:39 · **5/10** (Discussion sur changement de pratiques, intérêt modéré)
  *Titre original : AI Coding Tools Change Software Engineering, and Some Developers Miss the Struggle*
- [Qu’est‑ce que le Vibe Coding et comment démarrer](https://news.google.com/rss/articles/CBMiVEFVX3lxTE8wLWtTbzBlU2JvRk8xaWd6NnFkSV9DVFlodlczM1ZXNGVxYnlNaHg2OEZhbW1SQlB4d2JLOUlrazlCQ0stalhjZHJ6UkMweXJ5YVRaeQ?oc=5) — *Knup.com*, 22/11 22:21 · **4/10** (Introduction au Vibe‑coding, concept émergent)
  *Titre original : What Is Vibe Coding and How Do You Start*
- [La révolution du vibe‑coding arrive sur tous les appareils](https://www.theverge.com/column/1039139/vibe-coding-gadgets-tv-camera) — *The Verge*, 22/11 14:00 · **4/10** (Annonce vague du Vibe‑coding, peu de détails)
  *Titre original : The vibe-coding revolution is coming to all the gadgets*
  > Large language models can now redesign your TV and upgrade your camera for you. Is the physical world ready to be Claude Code-d?﻿ ...
- [« C’est des montagnes russes » : Angie Jones de l’Agentic AI Foundation sur le rythme effréné des agents IA](https://thenewstack.io/junior-developers-ai-agents-block/) — *The New Stack*, 21/11 22:58 · **4/10** (Interview sur IA agentic, perspective intéressante mais non technique)
  *Titre original : “It is a rollercoaster ride”: Angie Jones of the Agentic AI Foundation on keeping up with AI agents*
  > Only a few years ago, it would have been impossible to picture this scenario: A lead developer once gave 10 The post “It is a rollercoaster ride”: Angie Jones of the Agentic AI Foundation on keeping up with AI agents appeared first on The New Stack .

## Intégrations, plateformes et écosystèmes IA (5)

Cette catégorie recense les annonces d’intégrations d’agents IA dans des plateformes variées (MCP, agents personnels, agents de recherche), ainsi que les acquisitions et partenariats (Cursor acheté par SpaceX, Unolabs & NovTek, etc.) et les services cloud liés à l’IA.

- [Unolabs et NovTek s'associent pour la sécurité des données IA](https://itbrief.com.au/story/unolabs-novtek-join-forces-on-data-ai-security) — *IT Brief Australia*, 23/11 08:00 · **5/10** (Partenariat sur IA sécurité des données, applicabilité sectorielle)
  *Titre original : Unolabs & NovTek join forces on data AI security*
  > Businesses rolling out data and AI projects could face fewer delays, as the firms will add security checks during development rather than after launch.
- [Les agents IA transforment le développement logiciel](https://news.google.com/rss/articles/CBMidkFVX3lxTE1lYl8yTXFSME9yQnY2OENzSWFna0ZtdXJCdHpqUFY5cGZKdzJ1aVkzNVBkNmVVYTZXYUowLWx0a2JFektJQzFOY2tpbFN5ejJRbHJrZVF4NUZoTTAzX0tqd1lHN1psZnpDbkRQSHlmUW9uN05aS0E?oc=5) — *Medya Press*, 23/11 04:16 · **5/10** (Analyse de l’impact des agents IA sur le dev, pertinence moyenne)
  *Titre original : AI Agents Are Changing Software Development*
- [Seedeo MCP ajoute Suno, Kling et Veo aux connecteurs ChatGPT et Claude](https://www.jsonline.com/press-release/story/272680/seedeo-mcp-adds-suno-kling-and-veo-to-chatgpt-and-claude-connectors/) — *The Northwest Florida Daily News*, 22/11 15:41 · **4/10** (Ajout de connecteurs MCP, évolution fonctionnelle)
  *Titre original : Seedeo MCP Adds Suno, Kling and Veo to ChatGPT and Claude Connectors*
  > One hosted MCP server and API for video, image and music: sign in from ChatGPT or Claude, see the cost before you run, ...
- [SpaceX (SPCX) achète Cursor pour 60 milliards de dollars, dix jours après l’introduction en bourse — le flottement d’août mettra‑t‑il fin à la hausse ?](https://news.google.com/rss/articles/CBMivgFBVV95cUxON0pJalA1ajU5TXJoeW93cTI4c01fckR6MF9kUHJxd3hpaG9zbE54dmJudW5VZ1ZsWWNBSVEzR0dNUDg1MDduUzQyX0tFTnJ5T3lfUGd2TVhfWUtSTVA3Sm1FN1ZBQzkzUlY0eXZMMU9JZkJGRFlGZVplTFpKWkhoeWc3UmNRblhUTW1iald0dWdya2dOU2l2QmpMMUE0czl2dGx3cEd4eTFkX3JHQ01mdTZUOVh1bVBoZFYyUlFB?oc=5) — *TradingKey*, 22/11 12:29 · **2/10** (Annonce financière, hors focus pratique)
  *Titre original : SpaceX (SPCX) Buys Cursor for $60B Days After IPO — Will the August Float Unlock End the Rally?*
- [Perplexity et Intelligence](https://openai.com/index/perplexity-and-intelligence) — *OpenAI*, 22/11 01:00 · **2/10** (Titre vague, aucune information concrète)
  *Titre original : Perplexity and Intelligence*
  > How perplexity measures progress in AI models, and why it could help developers establish a shared approach to evaluating emerging capabilities.

## Autres articles (5)

- [Unreal Engine 6 abandonnera une fonctionnalité de script clé plus tôt que prévu au profit du codage IA](https://news.google.com/rss/articles/CBMizgFBVV95cUxQMGJZb0E4NWI2MnB2OUJvYm83eDZwWmt2X3hJRkNJejg4MmNNV1dSdEdsTnE0Y19WS3ZieXY0WW52Wm1fbzVmWTc0NmlYU2FCLWF5SkhMSTNWMGNodF81VndRUFRfU0FrWGY5a05ZTUNwRlMwODU4NjFibDRscWdxcmd2cFd1UXZCMklwSG42LXRFX2hWZktveXZGMlRDZi1Ra0pWcjZVM09XZlhaSUp3RTVEeEZCZG1SLXRqbUJ4TkFXUXA5YXVOY3p3RHVMZw?oc=5) — *PC Gamer*, 22/11 21:33 · **7/10** (Unreal Engine 6 supprime script, mise en avant IA coding)
  *Titre original : Unreal Engine 6 to jettison key scripting feature earlier than planned in favor of AI coding*
- [Les agents de codage IA réussissent les tests isolés mais accomplissent moins d’un sur dix tâches en environnement de travail simulé](https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace/) — *The Decoder*, 22/11 16:15 · **7/10** (Évaluation réaliste des agents IA en contexte travail, donnée clé)
  *Titre original : AI coding agents ace isolated tests but complete fewer than one in ten tasks in a simulated workplace*
  > A new real-world test puts AI coding agents in a simulated developer job with colleagues, project boards, and incomplete handoffs, where they have to keep developing software on their own and reliably close open tickets in a messy daily workflow. Even Opus 5.5 and Astra fall far short, solving fewer
- [Genspark lance SecondBrain VoicePad sur Kickstarter](https://itbrief.com.au/story/genspark-to-launch-secondbrain-voicepad-on-kickstarter) — *IT Brief Australia*, 23/11 08:28 · **5/10** (Lancement d’un dispositif vocal sur Kickstarter, outil concret)
  *Titre original : Genspark to launch SecondBrain VoicePad on Kickstarter*
  > The desktop AI device is expected to undercut its $169 retail price on Kickstarter, with early backers set to pay $119 to $149.
- [Série IA : comment le codage IA pourrait être responsable des récentes pannes](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9SZHlscUg0emp1bTFsMkRLNEVVdVF4QURkaWVMSk55MUNPTjJ6eklxcHIwSzlCSEw4elRHSlp3emExdFV4blE2SHlza1k3T0MwUklqRlR2cGcxUQ?oc=5) — *CBC*, 22/11 15:32 · **5/10** (Série sur pannes liées au code IA, pertinence modérée)
  *Titre original : Artificial intelligence series: how AI coding could be responsilble for recent outages*
- [La nouvelle API Monitor de Perplexity transforme la recherche web d’une requête ponctuelle en veille permanente](https://the-decoder.com/perplexitys-new-monitor-api-turns-web-search-from-a-one-off-query-into-a-nonstop-watchdog/) — *The Decoder*, 22/11 15:20 · **5/10** (API Monitor de Perplexity, amélioration d’usage)
  *Titre original : Perplexity's new Monitor API turns web search from a one-off query into a nonstop watchdog*
  > Perplexity is launching a Monitor API that searches the web on a schedule and alerts agents via webhook only when relevant changes occur. Its own decision model filters out unimportant results. For Perplexity, the API is part of a broader strategy to stand out from an increasingly interchangeable ch

## Vidéos à regarder (10)

- [MCP vs UTCP Explained! 🚀 How AI Agents Call Tools | AI Architecture](https://www.youtube.com/watch?v=bkLdMOGGFE4) — *AIARCHITECTLAB*, 23/11 04:01
  > Explication du protocole MCP vs UTCP et comment les agents IA appellent réellement des outils externes.
- [Playwright MCP vs CLI: Which One Should Your AI Agent Use?](https://www.youtube.com/watch?v=Y9rdiAgNVdU) — *Testing Funda by Zeeshan Asghar*, 23/11 03:29
  > Comparaison entre Playwright MCP et la CLI pour choisir la meilleure interface pour les agents IA qui pilotent un navigateur.
- [How does your AI agent find a new tool?](https://www.youtube.com/watch?v=Vx2aoEaav2I) — *System Design Simple*, 23/11 02:30
  > Présentation du processus de découverte de nouveaux outils par un agent IA via la définition de l’outil et les endpoints list et listChanged.
- [Build an AI Agent Part by Part (TypeScript + Mastra)](https://www.youtube.com/watch?v=NnzJQDNJkls) — *Agentic Recipe*, 22/11 21:48
  > Tutoriel pas à pas pour construire un agent IA en TypeScript, en assemblant modèle, outil de données en temps réel, mémoire et harness.
- [MCP Explained: How AI Agents Connect to Tools](https://www.youtube.com/watch?v=Xr_q4EvNKoc) — *Flas Educates*, 22/11 21:19
  > Description technique du protocole MCP montrant comment une application IA se connecte à des outils comme fichiers, calendrier ou bases de données.
- [How AI Agents Work: Build One From Scratch in Python | How It Runs](https://www.youtube.com/watch?v=-sqA1OrpwD4) — *HowItRuns*, 22/11 19:33
  > Construction d’un agent IA depuis zéro en Python : modèle local, quatre outils et boucle d’agent de 20 lignes, sans dépendances externes.
- [How AI Agents Thinks | Multi-Agent Orchestration, LangGraph & MCP](https://www.youtube.com/watch?v=olp-e7DaVw0) — *FalconSpark Infotech*, 22/11 18:51
  > Analyse du fonctionnement interne des agents IA multi‑agents, de l’orchestration LangGraph et du rôle du MCP.
- [Claude Code 2.1.321 fixes an MCP token leak](https://www.youtube.com/watch?v=IIBB-N5l3As) — *Stefan Rows*, 22/11 18:00
  > Annonce de la version 2.1.321 de Claude Code qui corrige une fuite de token MCP OAuth lors de redirections serveur.
- [Add Social Media Tools to Your AI Agent with Juicer MCP](https://www.youtube.com/watch?v=hiTYGC7UlQg) — *Juicer*, 22/11 17:45
  > Guide pour ajouter rapidement des outils de réseaux sociaux à un agent IA via le serveur MCP de Juicer, avec OAuth ou clé API.
- [Why does an AI agent need a loop? #llm #ai #mcp #python #programming #aiagents #softwaredevelopment](https://www.youtube.com/watch?v=WjrChzSAJgc) — *nononsenseai*, 22/11 15:30
  > Explication de la nécessité d’une boucle d’exécution pour les agents IA : le modèle demande un outil, le code l’exécute et renvoie le résultat.

## Podcasts à écouter (10)

- [Gemini 4 Argon (In-depth benchmark analysis): Did Google make a big comeback?](https://podcasts.apple.com/us/podcast/gemini-4-argon-in-depth-benchmark-analysis-did-google/id6826122006?i=1000797739908&uo=4) — *AICodeKing*, 23/11 06:30
  > Analyse approfondie du benchmark Gemini 4 Argon, évaluant si Google a réalisé un grand retour avec cet outil d'IA.
- [ContinueDev + CodeQwen : STOP PAYING for Github's Copilot with this LOCAL and OPENSOURCE Alternative](https://podcasts.apple.com/us/podcast/continuedev-codeqwen-stop-paying-for-githubs-copilot/id6826122006?i=1000800249366&uo=4) — *AICodeKing*, 23/11 06:00
  > Présentation de ContinueDev + CodeQwen, une alternative locale et open‑source à GitHub Copilot pour le codage assisté par IA.
- [Episode 11 - Decision Intelligence (Track A - System Architecture)](https://podcasts.apple.com/us/podcast/episode-11-decision-intelligence-track-a-system/id6813299554?i=1000803478687&uo=4) — *The Agentic Enterprise: a practitioner's guide to building agentic systems*, 22/11 23:10
  > Épisode sur la Decision Intelligence, expliquant la couche trois de l'architecture à neuf niveaux des systèmes agentiques.
- [First Code, Then AGI: 18 Months Later | Poolside Founders](https://podcasts.apple.com/us/podcast/first-code-then-agi-18-months-later-poolside-founders/id1776879655?i=1000803467410&uo=4) — *Chain of Thought | AI Agents, Infrastructure & Engineering*, 22/11 21:30
  > Discussion avec les fondateurs de Poolside sur l'idée que le code est la voie vers l'AGI, illustrée par leurs expériences de développement.
- [The $0.23 Pitch: When AI Agents Lobby ChatGPT For Your Brand](https://podcasts.apple.com/us/podcast/the-%240-23-pitch-when-ai-agents-lobby-chatgpt-for-your-brand/id1884409947?i=1000803467074&uo=4) — *Answer Engine Optimization (AEO): The AI Search Podcast*, 22/11 21:20
  > Analyse du pitch à 0,23 $, où un agent IA place une marque dans les sources citées de ChatGPT, impact sur le SEO et la visibilité AI‑search.
- [AI Engineer in 10 | 23 November 2026 — vLLM 0.34, Transformers Cache Migration & More](https://podcasts.apple.com/us/podcast/ai-engineer-in-10-23-november-2026-vllm-0-34-transformers/id6832433690?i=1000803465452&uo=4) — *AI Engineer in 10*, 22/11 21:10
  > Couverture des nouveautés de vLLM 0.34, de la migration du cache de Transformers et du support expérimental de Google Live Interactions SDK.
- [Daily AI briefing · Nov 22, 2026](https://podcasts.apple.com/us/podcast/daily-ai-briefing-nov-22-2026/id6828679411?i=1000803423943&uo=4) — *Jadid for Engineers: Daily AI Briefing*, 22/11 14:00
  > Brief quotidien soulignant les failles de sécurité du « plumbing » autour des modèles IA, avec des fuites de clés AWS chez plusieurs fournisseurs.
- [Riemann certified, OpenAI locks traces — AI News Nov 22](https://podcasts.apple.com/us/podcast/riemann-certified-openai-locks-traces-ai-news-nov-22/id6817748791?i=1000803414088&uo=4) — *AI Engineering Briefing: Daily AI News for Software Engineers*, 22/11 13:02
  > Actualités IA pour les ingénieurs : certification Riemann, verrouillage des traces de raisonnement par OpenAI et nouvelles revendications mathématiques.
- [The Week AI Got Checked: ANT, the SEC and Riemann (Nov 22, 2026)](https://podcasts.apple.com/us/podcast/the-week-ai-got-checked-ant-the-sec-and-riemann-nov-22-2026/id1684415169?i=1000803406570&uo=4) — *AI Unraveled: Enterprise Strategy, Agentic Systems, Daily AI News, ChatGPT, Gemini, Claude, DeepSeek*, 22/11 11:39
  > Récapitulatif hebdomadaire des contrôles réglementaires et financiers sur l’IA, incluant l’IPO d’Anthropic et la vérification de preuves massives.
- [When Agents Act on Your Data, Everyone Becomes a Data Steward - Billy Shea](https://podcasts.apple.com/us/podcast/when-agents-act-on-your-data-everyone-becomes-a/id1730788353?i=1000803404947&uo=4) — *Agent Stack Masters*, 22/11 11:12
  > Entretien avec Billy Shea sur la responsabilité des données lorsqu’un agent IA agit sur celles‑ci, et l’émergence du rôle de steward de données.

## Écartés comme hors sujet (34)

- [Your client says the automation stopped working. The delivery record that ends that conversation.](https://dev.to/rambozambo/your-client-says-the-automation-stopped-working-the-delivery-record-that-ends-that-conversation-47ak) — *dev.to*, 23/11 08:30
  > The message It lands at 11pm, and it always has the same shape: hey. the automation stopped working again That word "again" is doing the damage. It says this has happened before, it says the client has been keeping count, and it says the next hour of your life is unpaid. You will open the chat threa
- [Japan Exchange Group CEO sees limited impact from AI stock selloff](https://cryptobriefing.com/japan-exchange-ceo-ai-stock-selloff/) — *Crypto Briefing*, 23/11 08:18
  > Japan's resilience amid AI stock volatility highlights its potential as a diversification strategy, contrasting with US tech market dependency. The post Japan Exchange Group CEO sees limited impact from AI stock selloff appeared first on Crypto Briefing .
- [5 formations pour monter des vidéos avec Premiere Pro, DaVinci Resolve ou l’IA](https://www.blogdumoderateur.com/selection-formation-montage-video-327/) — *Blog du Modérateur*, 23/11 08:00
  > Une sélection de formations pour apprendre à dérusher, à étalonner, à mixer le son et à animer ses contenus, du tournage jusqu’à leur diffusion sur les réseaux sociaux.
- [Taiwan tightens short-selling rules amid AI stock decline](https://cryptobriefing.com/taiwan-tightens-short-selling-rules-amid-ai-stock-decline/) — *Crypto Briefing*, 23/11 07:15
  > Taiwan's regulatory actions may destabilize global tech supply chains, impacting major players like Nvidia and altering market dynamics. The post Taiwan tightens short-selling rules amid AI stock decline appeared first on Crypto Briefing .
- [AI answers have no page one, so stop reporting them as if they did](https://itbrief.com.au/story/ai-answers-have-no-page-one-so-stop-reporting-them-as-if-they-did) — *IT Brief Australia*, 23/11 07:12
  > Single-run AI visibility checks can mislead marketers, because the brands named change by query, language and assistant from one minute to the next.
- [Researchers warn AI could expose nuclear systems to cyberattacks](https://cryptobriefing.com/china-warns-ai-nuclear-systems-us-attacks/) — *Crypto Briefing*, 23/11 07:05
  > AI's potential to compromise nuclear systems underscores the urgent need for robust human oversight and international cooperation to prevent escalation. The post Researchers warn AI could expose nuclear systems to cyberattacks appeared first on Crypto Briefing .
- [IA en production, souveraineté, réversibilité : les nouveaux chantiers des CTO](https://www.blogdumoderateur.com/ia-production-souverainete-reversibilite-nouveaux-chantiers-cto/) — *Blog du Modérateur*, 23/11 07:00
  > Le Tech.Rocks Summit fête ses dix ans les 30 novembre et 1er décembre. Sa directrice générale revient sur une décennie de tech et sur l’état des CTO en 2026.
- [How the United States destroyed its chemical weapons stockpile](https://news.lavx.hu/article/how-the-united-states-destroyed-its-chemical-weapons-stockpile) — *news.lavx.hu*, 23/11 06:52
  > The United States destroyed its last chemical weapon in July 2023, ending a 37-year effort that began with a 1986 congressional mandate. The program dismantled 31,100 metric tons of agents across a dozen sites, using incinerators, neutralization plants, and portable systems.
- [Researchers find Great Firewall evasion methods for less than $1 in GPT-5.1 tokens](https://news.lavx.hu/article/researchers-find-great-firewall-evasion-methods-for-less-than-1-in-gpt-5-1-tokens) — *news.lavx.hu*, 23/11 05:01
  > Six researchers from the University of Massachusetts Amherst, the University of Colorado Boulder and the Great Firewall Report built CircumVolve, a system that used GPT-5.1 to generate working censorship circumvention techniques in four countries.
- [AI Firms Form Foundation for Autonomous Agent Protocols](https://news.google.com/rss/articles/CBMilAFBVV95cUxPT1cyd0NQWXFrb0lzNWljTVlKOEQzUUZES2xhQmJPWEI5NVcyY2dtR2JfMm0wc19iRUgzNVpvdGJvd2RxUGtJNDdHZzhhMkJDS0tURmphR3NzYVRMSzNCQjZOb3hXdkhRR29DWHc4WGt3OVNrVE1MWlVxWS10RzNCWmYwUDBCbHpwc0FVRU1XZlF0Mjdt?oc=5) — *Wisevoter*, 23/11 02:44
- [fast-anything: Rewrite the Slow 5% in Rust (116x Demo)](https://news.google.com/rss/articles/CBMinAFBVV95cUxPUGxNLXFoUVF3OGFmU0lvWmNtTXdKZ1VBTjRKSEFES0lEbjRlcUp5YWdSSUUwT2dRUU1YaFBodDNVcFBwZVJBRjI2cG9Cekcwb0JnY1NUcnduRVd4VHFMaVk1WGZPTlBVREVwRVNReXIxYWR3cEJoQ09QX2xjTXd6WVF1MlFvSlBHQmQtUVZKNnVHdjA1MUkxcFlacEU?oc=5) — *explainx.ai*, 23/11 01:00
- [QCon San Francisco 2026: The Harness Is the New Operating System](https://www.infoq.com/news/2026/11/harness-new-operating-system/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 22/11 23:44
  > At QCon San Francisco 2026, Mad Labs founder and CEO Manju Rajashekhar opened the conference arguing that the harness around an AI model, rather than the model itself, decides what an agent can do and how safely it does it. The keynote mapped the parts of a harness, including context, tools, state, 
- ["The thing that hit us": Satya Nadella admits VS Code faded in six months after a decade on top because of Claude Code, and some developers say they've stopped opening it](https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/) — *Windows Latest*, 22/11 23:30
  > Satya Nadella says IDEs faded six months after Claude Code arrived, and Microsoft is now turning VS Code into a hub for AI coding agents.
- [AI stock sell-off spreads fear as trader sees potential for sharp rebound](https://www.tokenpost.com/news/investing/62418) — *TOKENPOST*, 22/11 22:40
  > Gareth Soloway says market fear could set the stage for a sharp rebound after AI stocks fell, while cautioning that further declines remain possible over the longer term.
- [Armin Ronacher: 141 New Projects, 15 Still Maintained — Why AI Coding's Real Bottleneck Is Human Attention](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5KVEozZnh2RU5vVUswY29sb0xVWXRuR2E0RWZSWGJQWnhLSThsMFQxbktTREREVFJObGRUNkxxUXZqaDY4MzhiQngtdTZZZ3lMTWFLWXA5eG1jZ2c?oc=5) — *BigGo Finance*, 22/11 22:08
- [What is vibe manufacturing? AI-designed products explained](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1jWnFNUWZVVUthYjctaWVGWjN6OGtaTWwwYVFESDc4aWlsdHBoOGRkU19tc1RyTndjTnlTOFFRbHRlZGVkVDNmcHZ2X0ltLUoxOVgxakVrNXk3LUdSWHhwQTF3?oc=5) — *Mashable*, 22/11 21:12
- [Select Styling Specimens](https://simonwillison.net/2026/Nov/22/select-styling/) — *Simon Willison*, 22/11 20:45
  > Tool: Select Styling Specimens I got frustrated at how HTML <select> boxes default to looking different in different browsers, and are (I think) quite ugly in Chrome: So I had Claude Fable 5.2 build me this page showing all of the ways they can be styled: Build an HTML page that shows all of the way
- [CleanYourTV: Artificial intelligence is changing televisions, with the risk of damage](https://news.google.com/rss/articles/CBMid0FVX3lxTFBGZUlJbHFMdmd1amVsSGZQc2ZiVVRVMTR1QzkxemhGQ1BncTVFckdfUmh3ZERmV0tYUTV0WmFkdjM2X3U0U0lwVlJaTDQ3SG5uenk1RFJVN1c2T3VQeENfMjRRT1FaZC1paWc0QnJZa1N4UmtzdnNv?oc=5) — *SecNews.gr*, 22/11 17:42
- [The Benefits and Risks of Updating Multiple Programs Through a Shared Handler](https://hackernoon.com/the-benefits-and-risks-of-updating-multiple-programs-through-a-shared-handler?source=rss) — *HackerNoon*, 22/11 17:13
  > One handler update changed 40 reports at once; a faulty one broke 35 totals. What a shared DSL handler costs: checks, rollback, devices, and AI.
- [6 Handy Ways You Can Use Your Old Mini PC](https://www.engadget.com/2310723/handy-ways-use-old-mini-pc/) — *Engadget*, 22/11 17:00
  > From retro gaming consoles to home media servers, discover six handy ways to repurpose your old mini PC and give the hardware a new lease on life.
- [I finally found a use for my old Android phone, and it's now my PC's control panel](https://www.msn.com/en-us/news/other/i-finally-found-a-use-for-my-old-android-phone-and-its-now-my-pcs-control-panel/ar-AA2hZXlm) — *MakeUseOf*, 22/11 16:30
  > If you've got an old phone and a few minutes to spare, PhoneBox is what you need.
- [AI is getting better faster than experts can reliably test whether new systems are safe, METR warns](https://the-decoder.com/ai-is-getting-better-faster-than-experts-can-reliably-test-whether-new-systems-are-safe-metr-warns/) — *The Decoder*, 22/11 14:00
  > METR reports that leading AI models like Opus 5.5 and GPT-6 Astra are improving rapidly at research tasks but getting harder to measure. Current data can't rule out a dangerous acceleration in AI development, the organization warns, though it also says common tests may overestimate what the models c
- [How AI Changes the Four Types of Analytics for Data Scientists](https://towardsdatascience.com/how-ai-changes-the-four-types-of-analytics-for-data-scientists/) — *Towards Data Science*, 22/11 14:00
  > Treat AI agents as junior teammates and move up the abstraction ladder, owning problem framing, model evaluation, and business partnership. The post How AI Changes the Four Types of Analytics for Data Scientists appeared first on Towards Data Science .
- [PostgreSQL 19 Released with Online Table Repacking and Query Planning Controls](https://www.infoq.com/news/2026/11/postgresql-19-released/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 22/11 13:54
  > The PostgreSQL Global Development Group released PostgreSQL 19, introducing changes to database maintenance, query planning, replication, and application development. The release focuses on reducing administrative overhead and improving performance, with new tools for reorganizing tables without dow
- [How to spot the next fake "fired from Rockstar" post before it fools you](https://www.msn.com/en-in/news/other/how-to-spot-the-next-fake-fired-from-rockstar-post-before-it-fools-you/ar-AA2hYqg0) — *The Pioneer*, 22/11 12:37
  > India, Nov. 22 -- Two posts went viral on X this month, each claiming to be a Rockstar North engineer fired the day before Grand Theft Auto VI's November 19, 2026 launch. One, in English, said the ...
- [Microsoft (MSFT) Surged 8% After Earnings - Azure Hit 43%, Copilot 30M Seats, Capex Steady](https://news.google.com/rss/articles/CBMi1gFBVV95cUxPaF9pM0tpSHRxU3cyUjR3cng0bElLN09DQlR0QmJLZkptZ3FSUDQwZG9BR3lCdGtyckdjenRQYjR3V2pFdFZsSjJ5aldIM1RiTXFDZjlzTy1XckdramlEZ0pSSmpNdG1jbktESU9JR25wVWQycHNWVnIxY183blRURzU2Q0l0SHlwcXRQNW9xdmcwRkJWWFlzeVBNVUpIcFYyVWVWQWxUc0lWTVpGVE5LejExUjJfcUVBT0NMel96ckpyWDVuSUdXX0FpLUlmekhRTi1YSUpB?oc=5) — *TradingKey*, 22/11 09:59
- [Meta ads is now available in AWS Quick](https://aws.amazon.com/blogs/machine-learning/meta-ads-is-now-available-in-aws-quick/) — *AWS Machine Learning*, 22/11 02:59
  > AWS Quick now has a Meta ads AI connector. Meta advertisers can use natural language in Quick to create, manage, and analyze campaigns while staying connected to the Meta ad management network, and combine Meta ad data with first- and third-party sources to build dashboards, documents, slide decks, 
- [A Team of Researchers from Columbia and CertiK Introduce TensorLean for Formal Verification of GPU Kernels](https://www.marktechpost.com/2026/11/21/columbia-certik-tensorlean-formal-verification-gpu-kernels/) — *MarkTechPost*, 22/11 02:51
  > TensorLean, from Columbia University and CertiK, formally verifies production GPU kernels at the PTX level using Lean. It checked 149 kernel instances, proved 83 correct, and found 38 bugs in FlashAttention, DeepGEMM and more. The post A Team of Researchers from Columbia and CertiK Introduce TensorL
- [Anthropic IPO draws mixed market response as Google and custom AI chips come into focus](https://www.tokenpost.com/news/insights/62400) — *TOKENPOST*, 21/11 23:40
  > Ejaaz called Anthropic's early trading reasonable as investors assess its IPO. He also highlighted Google's AI models and the push by leading labs to develop custom chips.
- [AI threatens long-term investing and business advantages, Visser says](https://www.tokenpost.com/news/insights/62399) — *TOKENPOST*, 21/11 22:40
  > James Visser says rapid AI development is making long-term investment decisions harder and eroding the time businesses have to establish competitive advantages. He also sees cyber concerns weighing on markets.
- [Tech stocks slump on AI spending concerns as investor fear prompts short covering](https://www.tokenpost.com/news/investing/62397) — *TOKENPOST*, 21/11 20:40
  > Dan Niles said extreme investor fear prompted him to cover short positions after a tech selloff. He also cited data center constraints and AI companies' rising costs as concerns.
- [Plex lâche TheTVDB](https://korben.info/plex-abandonne-thetvdb.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 21/11 19:19
  > Le 3 décembre, Plex ne récupère plus rien chez TheTVDB. Rien n'est effacé, mais l'ancien agent cesse de fonctionner, et les séries en cours suivies en ordre DVD ou absolu risquent de mal ranger leurs nouveaux épisodes. Voici quoi régler, et quoi laisser tranquille.
- [The HackerNoon Newsletter: Fridges, Hackers, AI and La Flemme (11/21/2026)](https://hackernoon.com/11-21-2026-newsletter?source=rss) — *HackerNoon*, 21/11 17:02
  > 11/21/2026: Top 5 stories on the HackerNoon homepage!
- [AI Made Us Faster. So Why Do Designers Have Less Time?](https://hackernoon.com/ai-made-us-faster-so-why-do-designers-have-less-time?source=rss) — *HackerNoon*, 21/11 15:00
  > AI makes design execution faster, yet workloads keep growing. Studies from METR, Upwork and MIT show where the saved time actually goes, and how to get it back
