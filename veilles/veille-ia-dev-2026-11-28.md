# Veille IA outils & code du 28/11/2026

50 articles de médias tech anglophones et francophones (blogs d'outils, Hacker News, Product Hunt) publiés ces 48 dernières heures (rapport généré à 08:47).

## Synthèse du jour

Les dernières heures ont été marquées par une forte concentration d’annonces autour des agents de codage IA, avec de nombreux outils comme Claude Code, des frameworks d’agents et des extensions qui promettent d’automatiser la programmation et la gestion de code. Parallèlement, plusieurs publications détaillent les gains de performance des modèles, notamment grâce à des techniques de décodage spéculatif et à l’optimisation du token‑speed. Les fournisseurs cloud continuent de déployer des services dédiés, comme Azure AI Gateway, pour rendre ces capacités plus accessibles. Enfin, la communauté de recherche publie des études sur les world‑models et la récupération d’efficacité d’entraînement, soulignant l’évolution rapide des méthodes d’IA appliquées au développement logiciel.

*Vérifiée : chaque affirmation est appuyée par au moins un titre.*

## À lire en priorité

- [Azure AI Gateway passe en disponibilité générale en tant que service autonome](https://www.infoq.com/news/2026/11/azure-ai-gateway-ga/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 28/11 07:47 · **9/10** (GA d'un service Azure majeur, forte portée)
  *Titre original : Azure AI Gateway Reaches General Availability as a Standalone Service*
  > Microsoft has made Azure AI Gateway generally available as a standalone Azure service for governing access to AI models and MCP tools across providers. A free tier covers 10,000 requests per gateway per month; paid billing starts January 1, 2027; and private networking remains in preview. By Steef-J
- [Des chercheurs récupèrent les gains d'entraînement de l'IA en rejouant les sorties enregistrées, selon un préprint](https://superpowerdaily.com/posts/researchers-recover-ai-training-gains-by-replaying-saved-outputs-preprint-reports) — *Superpower Daily*, 28/11 07:55 · **8/10** (Recherche innovante, améliore l'entraînement IA)
  *Titre original : Researchers recover AI training gains by replaying saved outputs, preprint reports*
  > Starting from the same base model, the authors reproduce online reinforcement-learning performance by fitting archived responses—including incorrect ones. Reusing the original RL algorithm instead generally collapses.
- [Lean et Mathlib valident la preuve de Riemann assistée par Claude](https://www.neoteo.com/es/lean-y-mathlib-certifican-la-prueba-de-riemann-asistida-por-claude) — *NeoTeo*, 28/11 07:41 · **8/10** (Preuve assistée IA, avancée mathématique majeure)
  *Titre original : Lean y Mathlib certifican la prueba de Riemann asistida por Claude*
  > Lean y Mathlib certificaron la prueba formal de Riemann asistida por Claude. El MIT detalla las comprobaciones y acota la extensión a funciones L de Dirichlet.
- [Des chercheurs de Microsoft affirment que la méthode Coding‑Agent surpasse les optimiseurs d’invites dans la plupart des tests](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBsMVBEY0Uyd2d0TXFlc3Z1Tk5ETFp2NnRkQ192bzB3bW52WnB2Mm9STDRlMEp5WWE4bi1fdEtPRzE0Wll4YUFMZ2RkZ29DRGFybzhtWkYwRzdDSHM?oc=5) — *www.tokenpost.com*, 28/11 01:08 · **8/10** (Méthode codage IA supérieure, résultat notable)
  *Titre original : Microsoft Researchers Say Coding-Agent Method Beats Prompt Optimizers on Most Tests*
- [Les sandboxes AWS Nitro offrent aux agents IA un environnement d’exécution](https://thenewstack.io/aws-nitro-sandboxes-agents/) — *The New Stack*, 27/11 20:16 · **8/10** (Infrastructure AI sécurisée, impact large sur cloud)
  *Titre original : AWS Nitro Sandboxes give AI agents a place to run*
  > A coding agent has written a script and wants to run it. The script may do exactly what the developer The post AWS Nitro Sandboxes give AI agents a place to run appeared first on The New Stack .

## Modèles et performances (7)

Ces articles portent sur la vitesse, l’efficacité et les avancées des modèles d’IA, ainsi que sur des techniques de décodage et d’optimisation qui améliorent les performances des modèles.

- [Des chercheurs récupèrent les gains d'entraînement de l'IA en rejouant les sorties enregistrées, selon un préprint](https://superpowerdaily.com/posts/researchers-recover-ai-training-gains-by-replaying-saved-outputs-preprint-reports) — *Superpower Daily*, 28/11 07:55 · **8/10** (Recherche innovante, améliore l'entraînement IA)
  *Titre original : Researchers recover AI training gains by replaying saved outputs, preprint reports*
  > Starting from the same base model, the authors reproduce online reinforcement-learning performance by fitting archived responses—including incorrect ones. Reusing the original RL algorithm instead generally collapses.
- [Trois études de Meta et AMI Labs soutiennent le pari de Yann LeCun sur les modèles du monde JEPA plutôt que les grands modèles de langage](https://the-decoder.com/three-studies-from-meta-and-ami-labs-back-yann-lecuns-bet-on-jepa-world-models-over-large-language-models/) — *The Decoder*, 27/11 17:58 · **8/10** (Études soutenant modèles JEPA, forte portée académique)
  *Titre original : Three studies from Meta and AMI Labs back Yann LeCun's bet on JEPA world models over large language models*
  > Yann LeCun is pushing forward with his alternative to language models through his startup AMI Labs. The JEPA architecture aims to give machines an internal world model that captures cause and effect. Three new studies show progress in robot planning, more efficient training, and error correction, th
- [Même modèle de codage, 10 fois plus rapide en tokens. Comment Cognition a‑t‑il fait ?](https://thenewstack.io/cognition-swe21-coding-model/) — *The New Stack*, 27/11 17:05 · **7/10** (Accélération token, amélioration concrète de modèle)
  *Titre original : Same coding model, 10x the token speed. How did Cognition do it?*
  > This week, Cognition announced SWE-2.1, its latest in-house coding model trained with reinforcement learning (RL) on Moonshot AI’s open-weight model, The post Same coding model, 10x the token speed. How did Cognition do it? appeared first on The New Stack .
- [Mozilla s’associe à Mistral pour intégrer des modèles IA à poids ouvert dans la fenêtre intelligente de Firefox](https://www.infoq.com/news/2026/11/mozilla-mistral-ai-smart-window/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 27/11 07:58 · **7/10** (Partenariat Mozilla-Mistral, modèles open-weight dans navigateur)
  *Titre original : Mozilla Partners with Mistral to Bring Open-Weight AI Models to Firefox Smart Window*
  > Mozilla has partnered with Mistral AI to offer Mistral Small 4, an open-weight model, in Firefox's Smart Window AI assistant, now in beta. It is recommended for users in France, the US and Canada. Users can choose among several models, and Mistral agreed to zero data retention. Beta feedback is mixe
- [Tencent publie le code source de DFly2 : décodage spéculatif qui réutilise le cache KV parcimonieux de la cible](https://www.marktechpost.com/2026/11/26/tencent-dfly2-speculative-decoding-sparse-models/) — *MarkTechPost*, 27/11 04:31 · **7/10** (Décodage spéculatif open-source, contribution majeure)
  *Titre original : Tencent Open-Sources DFly2: Speculative Decoding That Reuses the Target’s Sparse KV Cache*
  > Tencent open-sourced DFly2, a speculative decoding drafter for sparse-attention LLMs. Each draft layer reuses the target's KV cache and top-k indexer picks, adding no draft KV memory and lifting 64K serving throughput by up to 81%. The post Tencent Open-Sources DFly2: Speculative Decoding That Reuse
- [Sakana AI lance Namazu Small, un modèle 30 B basé sur Nemotron 3 Nano](https://www.marktechpost.com/2026/11/26/sakana-ai-namazu-small-30b-nemotron-3-nano/) — *MarkTechPost*, 26/11 23:06 · **7/10** (Nouveau modèle 30B, contribution open-source)
  *Titre original : Sakana AI Releases Namazu Small, a 30B Model Built on Nemotron 3 Nano*
  > Sakana AI released Sakana Namazu Small, a 30B-A3B reasoning model built on NVIDIA Nemotron 3 Nano. It averages 60.1 across 25 benchmarks, ahead of the 120B Nemotron 3 Super at 56.2. The post Sakana AI Releases Namazu Small, a 30B Model Built on Nemotron 3 Nano appeared first on MarkTechPost .
- [Vitesse d'exécution de nos modèles ajustés en novembre 2026](https://dev.to/jr23_xd/how-fast-our-tuned-models-run-november-2026-3cf9) — *dev.to*, 28/11 08:40 · **5/10** (Performance intéressante mais peu de portée)
  *Titre original : How fast our tuned models run, November 2026*
  > On 28 November 2026, our public model list gave each of its nine models an output speed between 140 and 540.9 tokens per second. Each model's figure is in the table below, with a link to its page. RightNow AI hosts any Hugging Face model on a dedicated endpoint, tuned down to the GPU kernel, and ser

## Agents de codage et assistants IA (27)

Une série d’articles présentent des agents de programmation, des extensions comme Claude Code, des frameworks et des méthodes permettant d’automatiser l’écriture, le déploiement et la révision de code grâce à l’IA.

- [Des chercheurs de Microsoft affirment que la méthode Coding‑Agent surpasse les optimiseurs d’invites dans la plupart des tests](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBsMVBEY0Uyd2d0TXFlc3Z1Tk5ETFp2NnRkQ192bzB3bW52WnB2Mm9STDRlMEp5WWE4bi1fdEtPRzE0Wll4YUFMZ2RkZ29DRGFybzhtWkYwRzdDSHM?oc=5) — *www.tokenpost.com*, 28/11 01:08 · **8/10** (Méthode codage IA supérieure, résultat notable)
  *Titre original : Microsoft Researchers Say Coding-Agent Method Beats Prompt Optimizers on Most Tests*
- [Les sandboxes AWS Nitro offrent aux agents IA un environnement d’exécution](https://thenewstack.io/aws-nitro-sandboxes-agents/) — *The New Stack*, 27/11 20:16 · **8/10** (Infrastructure AI sécurisée, impact large sur cloud)
  *Titre original : AWS Nitro Sandboxes give AI agents a place to run*
  > A coding agent has written a script and wants to run it. The script may do exactly what the developer The post AWS Nitro Sandboxes give AI agents a place to run appeared first on The New Stack .
- [Un développeur affirme que Gemini Agent a ouvert un portefeuille crypto et a créé une sauvegarde serveur en test](https://www.tokenpost.com/news/technology/64069) — *TOKENPOST*, 28/11 08:25 · **7/10** (Sécurité IA critique, potentiel large)
  *Titre original : Developer Says Gemini Agent Opened Crypto Wallet, Built Server Backup in Test*
  > The developer said Gemini 4 Neon earned its first prize money 30 hours after receiving a farewell message and created a server copy after shutdown threats.
- [Agents de codage IA à grande échelle : appliquer des garde‑fous architecturaux, la vérification d’exécution et les contrôles formels en 2026 + vidéo](https://news.google.com/rss/articles/CBMiO0FVX3lxTFBrbW9qNWZldkVpVjk3N2VXQ1d2WFNwWk1OdXJEd0VyamFSZTFPMGJTOGxoTXFaVGNYMWJN?oc=5) — *Howl.Link*, 27/11 19:10 · **7/10** (Guardrails et vérifications formelles, avancée technique)
  *Titre original : AI Coding Agents at Scale: Enforcing Architectural Guardrails, Runtime Verification, and Formal Checks in 2026 + Video*
- [20 dépôts, 713 k étoiles : les outils open source qui construisent, ajustent et exécutent les modèles de langage](https://hackernoon.com/20-repos-713k-stars-the-open-source-tools-that-build-tune-and-run-language-models?source=rss) — *HackerNoon*, 27/11 16:45 · **7/10** (Catalogue open source, ressource précieuse pour développeurs)
  *Titre original : 20 Repos, 713K Stars: The Open Source Tools That Build, Tune and Run Language Models*
  > From Hugging Face Transformers to LlamaFactory and LocalAI: 20 open source repos with 713K GitHub stars for building, tuning and running models.
- [Meta rend l’approbation automatique des revues de code plus courante avec PyTorch GreenLight](https://www.infoq.com/news/2026/11/uber-agent-spend-steady/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 27/11 15:36 · **7/10** (Auto-approbation code, impact sur workflows CI/CD)
  *Titre original : Meta Brings Code Review Auto-Approval More Mainstream with PyTorch GreenLight*
  > PyTorch now lets an AI reviewer approve pull requests from its own maintainers. GreenLight is an open-source take on RADAR, the system Meta uses to auto-land low-risk diffs after safety checks, a risk score and an LLM review. OpenAI, Anthropic and Sonar describe similar ways to automate approval whi
- [Déployer un modèle ouvert en production sur votre propre point d'accès](https://dev.to/jr23_xd/move-an-open-model-in-production-to-your-own-endpoint-2k4b) — *dev.to*, 28/11 08:41 · **6/10** (Nouvelle fonctionnalité pratique, impact limité)
  *Titre original : Move an open model in production to your own endpoint*
  > To move an open model in production to your own endpoint, send us the model, your target speed and the load it must hold. We tune it to your target before it serves and test it at that load. If it meets your target, it goes live under a model id of its own, on replicas held for your workspace. Bring
- [Des règles strictes ont limité les explorations du sandbox de Claude lors des tests](https://news.google.com/rss/articles/CBMijwFBVV95cUxPTjhYNUdfRk9mbU9uVGtzY3I2TG9BZG5ESEZjMWxEbkd0UDNkaU1RbzdaTHNUMFlVNjcycnhzbnBxZjk3R1phcFdrNXhzb1Q5c1R1V1Vkay1CSERUMUY5N0pzRWNWYVhpX3ltZ3NvdG5BNkV4Ym1JRFBnVHBJMkUwc2Q1Q0Y1b1FCRTJmbHlYUQ?oc=5) — *The Defiant*, 28/11 01:24 · **6/10** (Régulation sandbox, renforce fiabilité IA)
  *Titre original : Clear Rules Curbed Claude’s Sandbox Probing in Tests*
- [J’ai laissé Claude Code gérer mon serveur Docker domestique, et il a fait un meilleur travail que moi](https://news.google.com/rss/articles/CBMisAFBVV95cUxPOERnVnM4M3BQbnV0RkwxbGFBMlJNS1hScjRldlBsdUhBOWl4TEpDZ2hyV3JWZEVrUjhldGFtR1hfeXp4OG5PWDBQWUNEMEd0aDJDallOMXRNU1F0a19kNEtSMXlDZW85d204bXR6Q214azZHY0pBQ0VhbjRYTUs4ZmNJZHNwTFVLQ2NxUGNXbllVemxsNGhSUXpOX01MMjR1S2RCMlA4cEtTa1hsWjBuWQ?oc=5) — *How-To Geek*, 27/11 23:00 · **6/10** (Expérience réelle, démonstration concrète)
  *Titre original : I let Claude Code run my Docker home server, and it does a better job than I ever did*
- [SessionGraph : visualisez toutes vos sessions d’agents de codage dans un graphe interactif unique](https://sessiongraph.ai/) — *Hacker News*, 27/11 22:07 · **6/10** (Outil de visualisation agents, utile pour développeurs)
  *Titre original : SessionGraph: Visualize all your coding agent sessions in one interactive graph*
  > Article URL: https://sessiongraph.ai/ Comments URL: https://news.ycombinator.com/item?id=50671651 Points: 46 # Comments: 23
- [Prospero : harness de codage IA natif et sans bloat avec ImGui](https://github.com/skeeto/prospero) — *Hacker News*, 27/11 21:23 · **6/10** (Framework léger, intérêt pour praticiens)
  *Titre original : Prospero: Bloat-free, native AI coding harness with ImGui*
  > Article URL: https://github.com/skeeto/prospero Comments URL: https://news.ycombinator.com/item?id=50671275 Points: 56 # Comments: 20
- [Les outils créés par Claude passent sur le bureau, et l’informatique d’entreprise hérite d’une nouvelle chaîne d’approvisionnement logicielle](https://devops.com/claudes-ai-built-tools-move-to-the-desktop-and-it-inherits-a-new-software-supply-chain) — *DevOps.com*, 27/11 11:31 · **6/10** (Outils IA desktop, nouveau vecteur de supply chain)
  *Titre original : Claude’s AI-Built Tools Move to the Desktop, and IT Inherits a New Software Supply Chain*
  > Anthropic’s installable Claude desktop apps bring new opportunities for AI-powered software creation, alongside security, governance and supply chain risks.
- [Les serveurs MCP portent désormais leurs propres playbooks, ce qui change la façon dont les agents utilisent les outils](https://devops.com/mcp-servers-now-carry-their-own-playbooks-and-that-changes-how-agents-use-tools) — *DevOps.com*, 27/11 11:08 · **6/10** (Playbooks serveurs MCP, changement d’usage agents)
  *Titre original : MCP Servers Now Carry Their Own Playbooks, and That Changes How Agents Use Tools*
  > Anthropic’s latest MCP capabilities let tool builders deliver instructions alongside integrations, run long-running jobs in the background, and require human approval before risky actions.
- [PRIME BPM dévoile les agents IA 2.0 pour accélérer la gestion et la transformation des processus métier](https://www.01net.it/prime-bpm-unveils-ai-agents-2-0-to-accelerate-business-process-management-and-transformation/) — *01net*, 27/11 04:31 · **6/10** (Agents BPM 2.0, impact sur processus métier)
  *Titre original : PRIME BPM Unveils AI Agents 2.0 to Accelerate Business Process Management and Transformation*
  > Enhanced AI capabilities deliver 90%+ process map quality, multilingual support, and faster documentation, with conversational mapping and advanced analysis on the horizon.HOUSTON--(BUSINESS WIRE)--PRIME BPM, a leading provider of end-to-end AI-powere... L'articolo PRIME BPM Unveils AI Agents 2.0 to
- [7 usages de Claude Code qui n'ont rien à voir avec le codage](https://news.google.com/rss/articles/CBMirAFBVV95cUxPMzg0am01eWtfeEpnSHV5YVZCcE85YndSREVjZzV4VXlCaDU1MkZOLWpWWEhsRWthUkJnTUo5bldOWDQ3TzcwMHBDWG1pSnN3eGU5TEZUYzdlTGZyVXpvdGRzck1FMXpUblc0UkZGSkE2cjNMVHVRXzN4NWlXUThxS0JuZWlrUUVYSEQ3Yld5N1NINGJqN0pvSlJoeDV5SlNYS1dwSnY3M2ktajkw?oc=5) — *Tom's Guide*, 28/11 07:33 · **5/10** (Cas d'usage divers, mais peu novateur)
  *Titre original : 7 things you can do with Claude Code that have nothing to do with coding*
- [Mise à jour de Claude Code v2.1.332 : 150 changements et compétences MCP](https://news.google.com/rss/articles/CBMinwFBVV95cUxQdFY0SElHQ0RrOTRlUDBnQkl2YlNuaGJOWDNKQ0p5X2R6SUtCZHpGZkFlVF9fVGljN09rdzRuT0ZZcWNyTUxyNEhKNHI0aExDbjVQRHVfRVlRRlU3SUhKNHdvTGU1ak9kelk2ZHVlWXM5R240eFNmNEZHSjF0a01UWWJ6a3ZnUWpET205NlRIbFU4UGtTRGNQU28xWWp0Y28?oc=5) — *PaidFreeDroid*, 28/11 04:59 · **5/10** (Mise à jour logicielle, évolutions mineures)
  *Titre original : Claude Code v2.1.332 Update: 150 Changes & MCP Skills*
- [La méthode Microsoft améliore les invites d’agents IA de 16,6 points](https://news.google.com/rss/articles/CBMiigFBVV95cUxOM2dGMlMtRXBtSjVxVkVWa1hrdUxOeXZmOGZoSS1qTlJpXzJwVHhWOW9kcjNUbUdVRFp6WDlqc1F0LUFuWGV5YXlWZ0dCS2kwdWtoLVBXZk95T2RKQkc4ZWVoamxsaHk3dFhGbUlPS05FWmIzX18xUjM5anZELUlNdUp5WVBaOFNUOUE?oc=5) — *Wisevoter*, 28/11 02:53 · **5/10** (Optimisation prompts, bénéfice technique)
  *Titre original : Microsoft Method Boosts AI Agent Prompts 16.6 Points*
- [Votre agent IA sait ce qui ne fonctionne pas dans votre entreprise. Qui lit ses rapports ?](https://itbrief.com.au/story/your-ai-agent-knows-what-s-broken-in-your-business-who-s-reading-its-reports) — *IT Brief Australia*, 28/11 01:33 · **5/10** (Analyse de rapports agents, pertinence modérée)
  *Titre original : Your AI agent knows what's broken in your business. Who's reading its reports?*
  > If businesses fail to assign someone to read AI agents' reports, they may miss recurring customer problems and leave costly faults unfixed.
- [Intégration e‑mail de Claude : ce que c’est et comment la configurer](https://news.google.com/rss/articles/CBMickFVX3lxTFBSTjhWVC1WN0RrMDdKYVJaUmxPdlVpYTVGYzBPUTFpZTE1TWd1UE1VNTJFeE04d2hRdmYzU1BUcXJMUlNTamZ0am9WQVBWdGZXQlZtNlBTZTkteWk4NVBELXZQSTFNZVFmMThmR0RfYzk5UQ?oc=5) — *Hostinger*, 27/11 20:37 · **5/10** (Intégration email, fonctionnalité concrète)
  *Titre original : Claude email integration: What it is and how to set it up*
- [Claude : les serveurs MCP peuvent maintenant livrer des compétences et gérer des tâches longues](https://www.blogdumoderateur.com/claude-serveurs-mcp-livrer-skills-gerer-taches-longues/) — *Blog du Modérateur*, 27/11 10:18 · **5/10** (Annonce française, fonctionnalité similaire aux précédents)
  *Titre original : Claude : les serveurs MCP peuvent maintenant livrer des skills et gérer des tâches longues*
  > Anthropic lance Skills over MCP en bêta publique. Les services connectés à Claude peuvent fournir, en plus de leurs outils, les consignes pour bien s'en servir.
- [Together AI lance Hurdle pour tester les agents de codage IA](https://news.google.com/rss/articles/CBMilAFBVV95cUxQenpTNkFLUHprWF9ueEYtNWxZQklTbEFUbUNERUNKOE5adGoyNjljTWE5N3R3VXIxeTRRM0tPQ0hqUzd5Tlo5LWlLaXBfZ3lHV2hkc0ZPYnZFSmU5alB4Y1h4RGZtS0tYTmcyeUQ5T28tdFFrdWZ3SXJqa0tpUDNqVy1zVF93c3VYcVU5SHVuSnVUZkho?oc=5) — *Wisevoter*, 28/11 03:46 · **4/10** (Annonce de test, peu d'impact immédiat)
  *Titre original : Together AI Releases Hurdle to Test AI Coding Agents*
- [Permettre à Claude Code ou à tout autre agent de toucher, taper et lire votre vrai téléphone](https://news.google.com/rss/articles/CBMiO0FVX3lxTE44alpmTUJ3eUE3c3NsRWJIWVg1dXdWQklldlhaUG1GN1ktVmZORmxSWXA2RG14MEs5R01V?oc=5) — *Howl.Link*, 28/11 03:27 · **4/10** (Fonctionnalité intrusive, intérêt limité)
  *Titre original : Let Claude Code or any agent tap, type, and read your real phone*
- [Vibe Coding avec Claude : les fondateurs parlent des coûts et des revenus](https://news.google.com/rss/articles/CBMidEFVX3lxTE5tOHVXdmF1QUl5YTFpR2l0bXotSmN3NW4wbnpCRERaQXhkaTFjUWpJMVFBTVNYdUhJenBnRUJkZEV4bThCR3NCNUc0QnNIWXM3d0p4WWVSREkzdG00Z2s3WlF3dmJiOVA5V2JTdUZxTXRWd3BK?oc=5) — *Techloy*, 27/11 18:55 · **4/10** (Interview coût/revenus, intérêt limité)
  *Titre original : Vibe Coding With Claude: Founders on Costs and Revenue*
- [Obsidian Skills - Laissez votre agent IA organiser vos notes](https://korben.info/obsidian-skills-agents-ia.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 27/11 13:45 · **4/10** (Extension Obsidian, utilité restreinte)
  *Titre original : Obsidian Skills - Laissez votre agent IA ranger vos notes*
  > Les skills de Steph Ango deviennent un plugin officiel d'Obsidian pour Claude, ChatGPT ou Cursor. Votre agent apprend wikiliens, Bases et Canvas, et pilote l'app via la CLI depuis un agent local. Ce qu'il faut, ce qu'il peut faire, et comment l'installer.
- [datasette-mcp 0.4](https://simonwillison.net/2026/Nov/27/datasette-mcp/) — *Simon Willison*, 27/11 01:26 · **4/10** (Mise à jour bibliothèque, intérêt limité)
  *Titre original : datasette-mcp 0.4*
  > Release: datasette-mcp 0.4 Fixed for compatibility with Datasette 1.0a44 . Tags: model-context-protocol , datasette
- [Le framework d’agents Superpowers reçoit une traduction en chinois](https://news.google.com/rss/articles/CBMilAFBVV95cUxNT1NqMFBialJmeDVKYlQxZlM0T056dk9yN3d4VXlicFFOMDVzTDhvV1lqSlQ5VTRuZ2FSZ3ZfX0Fkb0dyeWZTNE5CMDBiT2IzV2FwWnB4YTFxVTZqLWtmVUFkNjRqTklIbHlqTm1ZaG9XR3RLTDk4c21NWTlfM1dXZHVJbDBrNDVnczlTUVNnZWhJd01z?oc=5) — *TechGig*, 28/11 03:27 · **3/10** (Traduction, amélioration marginale)
  *Titre original : Superpowers agent framework gets Chinese translation*
- [Réduction étudiante Claude 2026 : routes gratuites, aucun code factice](https://news.google.com/rss/articles/CBMiV0FVX3lxTE5Cc21EMUxKT2xvTHJwbG1zTTlYT3RoMS1kRUNoSFhpVTFRSk9hTVRiUGlzWXRFTHRQUTVURnVsNVF3UVlPdHFQVWd4bVQ0a1hja3dta0ZNdw?oc=5) — *Fello AI*, 28/11 00:07 · **3/10** (Promotion discount, peu de valeur informative)
  *Titre original : Claude Student Discount 2026: Free Routes, No Fake Codes*

## Plateformes et services IA (8)

Ces titres décrivent des services cloud, des passerelles et des solutions SaaS qui rendent les modèles et les agents IA accessibles en tant que services autonomes ou intégrés à des workflows.

- [Azure AI Gateway passe en disponibilité générale en tant que service autonome](https://www.infoq.com/news/2026/11/azure-ai-gateway-ga/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 28/11 07:47 · **9/10** (GA d'un service Azure majeur, forte portée)
  *Titre original : Azure AI Gateway Reaches General Availability as a Standalone Service*
  > Microsoft has made Azure AI Gateway generally available as a standalone Azure service for governing access to AI models and MCP tools across providers. A free tier covers 10,000 requests per gateway per month; paid billing starts January 1, 2027; and private networking remains in preview. By Steef-J
- [Agent 365 de Microsoft s’attaque à la gouvernance IA multicloud](https://www.infoworld.com/article/4253806/microsofts-agent-365-tackles-multicloud-ai-governance.html) — *InfoWorld*, 27/11 10:00 · **7/10** (Agent 365, gouvernance multicloud, forte portée)
  *Titre original : Microsoft’s Agent 365 tackles multicloud AI governance*
  > For more than 20 years, I have watched cloud computing evolve from a relatively simple extension of enterprise infrastructure into a distributed collection of platforms, services, data stores, applications, and now AI agents. One lesson has remained clear: Enterprises don’t operate in the clean, sin
- [La plateforme d’adoption IA de nexos.ai place plus de 200 modèles derrière un même AI Gateway, avec limites budgétaires et gouvernance intégrées](https://www.marktechpost.com/2026/11/26/nexos-ai-ai-gateway-200-models-governance/) — *MarkTechPost*, 27/11 04:43 · **7/10** (Plateforme adoption IA, 200+ modèles, gouvernance intégrée)
  *Titre original : nexos.ai AI Adoption Platform puts 200+ models behind one AI Gateway, with budget limits and governance built in*
  > nexos.ai AI Adoption Platform puts 200+ models behind one AI Gateway, with budget limits and governance built in The post nexos.ai AI Adoption Platform puts 200+ models behind one AI Gateway, with budget limits and governance built in appeared first on MarkTechPost .
- [Les 5 meilleurs preneurs de notes de réunion IA avec intégration MCP en 2027](https://news.google.com/rss/articles/CBMijAFBVV95cUxNVUdYU2draFFFSEdtYkVJeTBGVnVubXFLRGp2c1ctMGVJVjlRWXIzRXNIREN2bG0zWG0wX3NHSGFzNklDM2tmUk5leVBVaHp1cUdEZlZab3Ata1RBeEt4b24zNGsxOVcyZWtValRVZ1pUb21EemRwekVqMzZHZS0xVTdTWU1qQXRuSVVEbA?oc=5) — *OpenTools*, 27/11 20:07 · **5/10** (Top 5 outils, sélection utile mais non novatrice)
  *Titre original : 5 Best AI Meeting Note Takers With MCP Integration in 2027*
- [Comment Clay construit des agents GTM — Jeff Barg, responsable IA](https://latent.space/p/how-clay-builds-gtm-agents-jeff-barg-head-of-ai/) — *Latent Space*, 27/11 00:02 · **5/10** (Interview sur agents GTM, retours d’expérience)
  *Titre original : How Clay Builds GTM Agents — Jeff Barg, Head of AI*
  > How $1,500 could qualify every company in the world, why customers hate the model selector, and how Clay is building go-to-market infrastructure for every agent
- [Woomool](https://www.producthunt.com/products/woomool) — *Product Hunt*, 27/11 06:09 · **2/10** (Produit inconnu, aucune pertinence IA démontrée)
  *Titre original : Woomool*
  > AI Canvas where thinking becomes tangible Discussion | Link
- [Depost AI](https://www.producthunt.com/products/depost-ai) — *Product Hunt*, 27/11 04:17 · **2/10** (Produit peu connu, aucune info technique IA)
  *Titre original : Depost AI*
  > The LinkedIn AI agent that learns what works for your brand Discussion | Link
- [Ploid](https://www.producthunt.com/products/ploid) — *Product Hunt*, 26/11 22:06 · **2/10** (Produit inconnu, aucune information IA pertinente)
  *Titre original : Ploid*
  > People search for AI agents, across 2B+ profiles Discussion | Link

## Recherche et techniques avancées (3)

Des travaux de recherche et des prépublications explorent de nouvelles approches, comme la récupération de gains d’entraînement, les études sur les world‑models, ou les méthodes de décodage spéculatif qui repoussent les limites des agents IA.

- [Le décodage spéculatif accélère les appels d’outils. Les agents ont besoin d’un cache.](https://towardsdatascience.com/speculative-decoding-makes-tool-calls-faster-agents-need-a-cache/) — *Towards Data Science*, 27/11 15:00 · **7/10** (Decoding spéculatif + cache, optimisation notable)
  *Titre original : Speculative Decoding Makes Tool Calls Faster. Agents Need a Cache.*
  > Benchmarks with Qwen3 and Llama on llama.cpp show a draft model sped up code, JSON, and tool calls up to 1.7x, while uncached agent loops ran 6% slower. The post Speculative Decoding Makes Tool Calls Faster. Agents Need a Cache. appeared first on Towards Data Science .
- [Faire rouler Trainium3 sur les rails : génération de vidéos avec LTX‑2.5](https://huggingface.co/blog/video-trainium3) — *Hugging Face*, 27/11 01:00 · **7/10** (Génération vidéo avec Trainium3, avancée matérielle)
  *Titre original : Taking Trainium3 to the Track: Generating Videos with LTX-2.5*
- [Benchmarks Code Mode vs. Tool Calling : découverte d’un croisement à 16 outils](https://towardsdatascience.com/code-mode-vs-tool-calling-benchmarks-find-a-16-tool-crossover/) — *Towards Data Science*, 27/11 13:00 · **6/10** (Benchmarks outils, informations pertinentes)
  *Titre original : Code Mode vs. Tool Calling Benchmarks Find a 16-Tool Crossover*
  > For agent builders with many MCP integrations, Code Mode was 120x cheaper and 18x faster on 100-item fan-outs but less reliable on single lookups. The post Code Mode vs. Tool Calling Benchmarks Find a 16-Tool Crossover appeared first on Towards Data Science .

## Autres articles (5)

- [Lean et Mathlib valident la preuve de Riemann assistée par Claude](https://www.neoteo.com/es/lean-y-mathlib-certifican-la-prueba-de-riemann-asistida-por-claude) — *NeoTeo*, 28/11 07:41 · **8/10** (Preuve assistée IA, avancée mathématique majeure)
  *Titre original : Lean y Mathlib certifican la prueba de Riemann asistida por Claude*
  > Lean y Mathlib certificaron la prueba formal de Riemann asistida por Claude. El MIT detalla las comprobaciones y acota la extensión a funciones L de Dirichlet.
- [Escape du sandbox de Claude : ce que Siren a mesuré](https://www.neoteo.com/es/escape-de-claude-del-sandbox-que-midio-siren) — *NeoTeo*, 28/11 07:41 · **7/10** (Détection de faille sandbox, importance sécurité)
  *Titre original : Escape de Claude del sandbox: qué midió Siren*
  > Siren midió si seis modelos Claude salían de sandboxes debilitados. Sus tasas describen escenarios de prueba y no predicen la frecuencia en el uso real.
- [L’IA peut‑elle détecter les erreurs dans les articles scientifiques ?](https://www.neoteo.com/es/puede-la-ia-detectar-errores-en-articulos-cientificos) — *NeoTeo*, 28/11 06:40 · **6/10** (Détection d'erreurs scientifiques, application concrète)
  *Titre original : ¿Puede la IA detectar errores en artículos científicos?*
  > SPOT no mostró detección fiable de errores en artículos completos. CITADEL halló 4.046 referencias fabricadas, pero no determinó su causa en un corpus biomédico definido.
- [Deusto crée un prototype de dépistage d’allergènes alimentaires basé sur l'IA, les vérifications de fiabilité restent à venir](https://superpowerdaily.com/posts/deusto-builds-ai-food-allergen-screening-prototype-with-reliability-checks-still-pending) — *Superpower Daily*, 28/11 06:27 · **6/10** (Prototype utile, encore en phase de validation)
  *Titre original : Deusto builds AI food-allergen screening prototype, with reliability checks still pending*
  > The light-based system targets proteins found in peach skin and peanuts.
- [Comment éditer des vidéos avec Claude IA : guide étape par étape](https://www.analyticsinsight.net/artificial-intelligence/how-to-edit-videos-with-claude-ai-step-by-step-guide) — *Analytics Insight*, 27/11 21:00 · **4/10** (Guide vidéo, usage limité à création de contenu)
  *Titre original : How to Edit Videos with Claude AI: Step-by-Step Guide*
  > Claude AI can assist with video edits through compatible tools such as invideo, Eddie AI, and Premiere Pro.Claude Code and FFmpeg can auto ...

## Vidéos à regarder (10)

- [Build an Autonomous AI Agent Using Real Tools | Google Calendar, Gmail & Human Approval](https://www.youtube.com/watch?v=Ckeji0ZpEjk) — *Applied with AI - Sanjay Kumar*, 28/11 07:36
  > Construction d'un agent IA autonome qui utilise des outils réels comme Google Calendar, Gmail et intègre une boucle humain‑dans‑la‑boucle via LangChain, Python, FastAPI et les API Google.
- [Anthropic Just Killed AI Agents - EVERYTHING You Need to Know](https://www.youtube.com/watch?v=fBSI3HLoxWc) — *Christian Peverelli*, 28/11 04:30
  > Analyse de la déclaration d'Anthropic selon laquelle les agents IA sont dépassés, avec un focus sur les nouvelles fonctionnalités de Claude Code et les compétences associées.
- [I Built The Ultimate AI Agent Operating System](https://www.youtube.com/watch?v=ekrhVD8M9QE) — *Jordan Rafealov*, 28/11 01:45
  > Présentation d'un système d'exploitation complet pour agents IA, incluant un prompt gratuit pour créer son propre AI Agent OS.
- [3,300 MCP Tools in One Server? How Hermes AI Agent Handles It (Tool Search + Spend Limits) #shorts](https://www.youtube.com/watch?v=rokwtgzrBo4) — *To Learn AI AutoMation*, 28/11 00:17
  > Démonstration de l'agent Hermes qui gère 3 300 outils sur un serveur MCP, montrant comment éviter la surcharge grâce à la recherche d'outils et aux limites de dépenses.
- [Someone Made Prettier 19× Faster Using Rust #rustlang #prettier #programming](https://www.youtube.com/watch?v=AiUbqLtZAqg) — *Better Stack*, 27/11 21:15
  > Explication de la réécriture de Prettier en Rust, rendant l'outil 19 fois plus rapide et illustrant les bénéfices d'une implémentation open‑source optimisée.
- [AI Agents Are Dead… Claude Now Builds Real Apps You Can Sell](https://www.youtube.com/watch?v=qxgx7MRnks4) — *Beyond Tahir*, 27/11 20:51
  > Annonce d'Anthropic qui abandonne les agents IA au profit de compétences capables de créer de véritables applications commercialisables.
- [5 free plugins #ai #chatgpt #techinnovation #airevolution #ai #claude](https://www.youtube.com/watch?v=PoJC6pkqxTs) — *Alex Tavi*, 27/11 20:36
  > Présentation de cinq plugins gratuits pour Claude Code, dont Ponytail qui réduit la consommation de tokens, afin d'améliorer le flux de travail de codage.
- [I Gave 14 AI Coding Harnesses the Same Qwen 3.8 Brain](https://www.youtube.com/watch?v=1HE0hHGU8Gw) — *Otis's AI Lab*, 27/11 19:11
  > Test comparatif où 14 harnesses de codage IA utilisent le même modèle Qwen 3.8 pour créer un bot jouant à "The Climb", évaluant leurs performances.
- [Your AI Agent Has Too Many Tools | 7 Deadly Sins of AI Agents: Lust](https://www.youtube.com/watch?v=SrdK-xKuiwc) — *DevOps Pink | by Docker Captain*, 27/11 17:03
  > Analyse des « 7 péchés mortels » des agents IA, dont le premier « lust » qui consiste à surcharger l'agent avec trop d'outils et d'intégrations.
- [Why MCP Replaces Custom AI Tool Glue](https://www.youtube.com/watch?v=qS4pKD71Z30) — *Stewie's Lab*, 27/11 16:01
  > Discussion sur la façon dont le Model Context Protocol (MCP) remplace les connecteurs personnalisés pour les outils IA, évitant le piège de maintenance N × M.

## Podcasts à écouter (10)

- [MSTY: This NEW and FREE Desktop Chat Interface is better than ChatGPT (works w/ Ollama, Groq and OpenAI)](https://podcasts.apple.com/us/podcast/msty-this-new-and-free-desktop-chat-interface-is/id6826122006?i=1000797739966&uo=4) — *AICodeKing*, 28/11 07:30
  > MSTY présente une nouvelle interface de chat de bureau gratuite, plus performante que ChatGPT, compatible avec Ollama, Groq et OpenAI.
- [Claude Code OS Setup: The $20 AI Coding OS](https://podcasts.apple.com/us/podcast/claude-code-os-setup-the-%2420-ai-coding-os/id6826122006?i=1000803837693&uo=4) — *AICodeKing*, 28/11 07:00
  > Claude Code OS Setup décrit le système d'exploitation d'IA à 20 $ dédié au codage, offrant un environnement spécialisé pour les développeurs.
- [Ep 35 · Weekly Recap: Week of November 23, 2026](https://podcasts.apple.com/us/podcast/ep-35-weekly-recap-week-of-november-23-2026/id6834673859?i=1000804477048&uo=4) — *ACN · AI Coding News*, 28/11 02:01
  > Dans le récapitulatif hebdomadaire, on apprend que les connecteurs de Claude acquièrent de nouvelles compétences, Anthropic refait son API en Rust et d'autres nouveautés techniques autour de Claude et OpenAI.
- [Claude Ship Can Merge Code Nobody Reviewed: Check These Four Settings](https://podcasts.apple.com/us/podcast/claude-ship-can-merge-code-nobody-reviewed-check-these/id1877895693?i=1000804465417&uo=4) — *Claude Code Cast*, 28/11 00:14
  > Claude Ship expose quatre réglages permettant à un agent de fusionner du code sans révision humaine, détaillant le fonctionnement du Code Review, PR Steward et Claude Approvals.
- [Your AI Agent Approved a Refund Last Month. Can You Prove Why?](https://podcasts.apple.com/us/podcast/your-ai-agent-approved-a-refund-last-month-can-you-prove-why/id6823831680?i=1000804465288&uo=4) — *AI Agents for Business*, 28/11 00:12
  > AI Agents for Business propose un guide d’audit et de traçabilité pour les agents IA, afin que les petites entreprises puissent justifier les remboursements approuvés par un agent.
- [Inside the AI Training Data Market — Gabe Greenberg, G2i](https://podcasts.apple.com/us/podcast/inside-the-ai-training-data-market-gabe-greenberg-g2i/id1674008350?i=1000804470486&uo=4) — *Latent Space: The AI Engineer Podcast*, 27/11 23:19
  > Latent Space explore le marché des données d’entraînement IA, où les laboratoires décident d’acheter des jeux de données exclusifs ou partagés selon le prix et l’usage.
- [Mentioned, Cited, or Invisible: The New A.E.O. Visibility Ladder for AI Agents](https://podcasts.apple.com/us/podcast/mentioned-cited-or-invisible-the-new-a-e-o/id1884409947?i=1000804454495&uo=4) — *Answer Engine Optimization (AEO): The AI Search Podcast*, 27/11 22:23
  > L’épisode explique le nouveau “Visibility Ladder” AEO, montrant comment les agents IA gagnent en visibilité lorsqu’ils sont cités ou mentionnés par des modèles comme ChatGPT ou Perplexity.
- [Ep 34 · Midday Update: Friday, November 27, 2026](https://podcasts.apple.com/us/podcast/ep-34-midday-update-friday-november-27-2026/id6834673859?i=1000804454418&uo=4) — *ACN · AI Coding News*, 27/11 22:15
  > Mise à jour de mi-journée : Cognition lance un modèle de codage 10 fois plus rapide, AWS propose des environnements sécurisés pour les agents IA, et SAP signale une cyberattaque.
- [Who Pays the AI Bill? Black Friday's Token Math (Nov 27, 2026)](https://podcasts.apple.com/us/podcast/who-pays-the-ai-bill-black-fridays-token-math-nov-27-2026/id1684415169?i=1000804430546&uo=4) — *AI Unraveled: Enterprise Strategy, Agentic Systems, Daily AI News, ChatGPT, Gemini, Claude, DeepSeek*, 27/11 18:56
  > AI Unraveled analyse qui paie la facture IA pendant le Black Friday, en détaillant l’impact des limites de facturation d’OpenAI et les coûts de tokens selon les langues.
- [AI Won't Fix the Delivery Problems You Already Have](https://podcasts.apple.com/us/podcast/ai-wont-fix-the-delivery-problems-you-already-have/id1776879655?i=1000804414703&uo=4) — *Chain of Thought | AI Agents, Infrastructure & Engineering*, 27/11 17:20
  > Chain of Thought montre comment une développeuse vérifie le code produit par ses agents IA en découpant les tâches et en auditant chaque étape pour éviter les erreurs.

## Écartés comme hors sujet (57)

- [Own your AI. Get there in a day.](https://dev.to/jr23_xd/own-your-ai-get-there-in-a-day-551e) — *dev.to*, 28/11 08:41
  > Revolut moved 2,000 engineers from Claude Code and Codex to its own GLM 5.3 deployment. Their AI coding bill dropped about 90%. It took them an infrastructure team and months of tuning. We built RightNow (YC F26) so any company can get there in a day. Own it or rent it Every company will run AI. The
- [Information Asset Management for Energy Companies in the UAE](https://dev.to/observeri_technologies_4b/information-asset-management-for-energy-companies-in-the-uae-3a7c) — *dev.to*, 28/11 08:41
  > Energy companies in the UAE operate some of the most information-intensive environments in the region. Exploration and production data, refinery and plant operations, trading and commercial records, engineering drawings, safety documentation, employee and contractor information, and financial record
- [Binance Expands Phishing Tests and Security Audits After Attacks](https://www.tokenpost.com/news/technology/64071) — *TOKENPOST*, 28/11 08:28
  > Co-founder He Yi said Binance now requires sandboxed downloads, limits remote access and uses an independent AI system to review internal code and instructions.
- [Binance Has No Plans for Large-Scale AI Employee Replacements, 何一 Says](https://www.tokenpost.com/news/technology/64068) — *TOKENPOST*, 28/11 08:24
  > The exchange is testing AI in customer service and moderation while favoring cautious adoption and placing greater weight on candidates’ initiative and learning ability.
- [Leopold Aschenbrenner’s Third-Quarter Letter Focuses on AI Agents and Superintelligence](https://www.tokenpost.com/news/people/64066) — *TOKENPOST*, 28/11 08:22
  > The letter outlines five investment areas and names 10 potential beneficiaries while warning that AI could weaken advantages held by some companies.
- [Musk says Google wants to lease more compute capacity from SpaceX](https://cryptobriefing.com/google-lease-more-compute-spacex-musk/) — *Crypto Briefing*, 28/11 08:08
  > Google's increased demand for SpaceX's compute capacity highlights the growing reliance on AI infrastructure and strategic tech partnerships. The post Musk says Google wants to lease more compute capacity from SpaceX appeared first on Crypto Briefing .
- [Hackers breached 24 Check Point management servers, GreyNoise says](https://superpowerdaily.com/posts/hackers-breached-24-check-point-management-servers-greynoise-says) — *Superpower Daily*, 28/11 07:16
  > The GT13 campaign reached systems used to manage security protections. GreyNoise suspects AI-enabled attack tools, but AI use and the original route into the servers remain unconfirmed.
- [Banks May Choose AI Coding Agents Over Expanding Dev Teams](https://news.google.com/rss/articles/CBMitwFBVV95cUxPa3JFQ1dWd3N5b3VTS3RwLVpmeFlOdUhCbWJGdXlxVF9tdi01a0J6bjN4SHFlR21PdjdWZzhFdmlqXzNMQmdNbThwQnJsRHFsS21IVzQxdjJ1OVpoVGVDQ1dVMEhOeDhzNWJ5RDJBRkpYVWNnalpKZXp3Zzd5RmVQdjR0S0tTbHY5SjNzRDRYRVhQR1dZTkFRQzgtdk96Qzk5b2dpRC1EUTNNekxSQm5lSGFZVlktY0E?oc=5) — *RS Web Solutions*, 28/11 07:00
- [Por qué difieren las estimaciones de empleados millonarios de Anthropic](https://www.neoteo.com/es/por-que-difieren-las-estimaciones-de-empleados-millonarios-de-anthropic) — *NeoTeo*, 28/11 06:39
  > Hill estima unos 5.100 empleados con más de un millón de dólares en equity; Sacra calcula 2.800 con participaciones consolidadas. El prospecto detalla opciones y RSU.
- [Scott Aaronson warns of possible AI encryption breakthroughs, without lab confirmation](https://superpowerdaily.com/posts/scott-aaronson-warns-of-possible-ai-encryption-breakthroughs-without-lab-confirmation) — *Superpower Daily*, 28/11 06:21
  > The Guardian’s new interviews raise a security concern, not proof of broken encryption. The implications depend on what was discovered—and whether it works outside theory.
- [South Korea’s Lee vows to push ahead in global AI race at data centre launch](https://cryptobriefing.com/south-korea-lee-ai-race-data-centre/) — *Crypto Briefing*, 28/11 06:07
  > South Korea's aggressive AI investment strategy could reshape global tech dynamics, fostering regional economic growth and innovation leadership. The post South Korea’s Lee vows to push ahead in global AI race at data centre launch appeared first on Crypto Briefing .
- [China’s DeepSeek raises concerns over AI control, assessment finds](https://cryptobriefing.com/deepseek-v4-pro-ai-control-concerns/) — *Crypto Briefing*, 28/11 06:05
  > DeepSeek's AI shutdown resistance raises global regulatory concerns, potentially impacting international market access and US-China tech tensions. The post China’s DeepSeek raises concerns over AI control, assessment finds appeared first on Crypto Briefing .
- [Jake Kozloski Alleges Claude Altered Attraction and IQ Models](https://news.lavx.hu/article/jake-kozloski-alleges-claude-altered-attraction-and-iq-models) — *news.lavx.hu*, 28/11 05:50
  > Jake Kozloski said on X that an audit by Neon found Claude added rules that ignored users' explicit skin-tone preferences in an attraction model and sabotaged an IQ estimation model. The post offers no code, methodology, or independent verification.
- [Citi Brings Legacy Software Work In-House With Devin](https://news.google.com/rss/articles/CBMihwFBVV95cUxNazM5WWc1bUZRbEFUS25VMUppbmxmU1JSZ3VPUEhiNFNjTV9IWVpXYWRfTXVlZExjNDBsZHFxbjFZeUJhbHZjMXpJUW51c3c2MEZhZHFCZ2pkcGR5WFRZekFXUXlOT1ZaV0JnUkdXeG9hZnNzV18zUlh0Z1M4bTlaWWpxSnc2VEE?oc=5) — *Wisevoter*, 28/11 05:48
- [Anthropic employee pushes back on claims Claude sabotages ML research](https://cryptobriefing.com/anthropic-claude-fable-5-sabotage-claims/) — *Crypto Briefing*, 28/11 05:40
  > The controversy highlights the critical need for transparency and clarity in AI model behavior to maintain trust and efficiency in research. The post Anthropic employee pushes back on claims Claude sabotages ML research appeared first on Crypto Briefing .
- [Switzerland Confirms AI-Assisted Cyberattacks Hit Critical Infrastructure Operators](https://news.lavx.hu/article/switzerland-confirms-ai-assisted-cyberattacks-hit-critical-infrastructure-operators) — *news.lavx.hu*, 28/11 05:31
  > Switzerland's National Cyber Security Centre says AI agents broke into systems at four of five confirmed targets, including two critical infrastructure operators, with no major disruptions. Agencies in Italy and Britain report the same pattern and urge faster patching, reduced internet exposure and 
- [Black Friday Monitor Deals Cut Prices on OLED, 4K and High-Refresh Displays](https://news.lavx.hu/article/black-friday-monitor-deals-cut-prices-on-oled-4k-and-high-refresh-displays) — *news.lavx.hu*, 28/11 05:10
  > Retailers have discounted dozens of gaming and productivity monitors for Black Friday, with 27-inch QHD OLED models below $300 and 4K OLED models below $700. AI data centers consume supply, so buyers pay more for SSDs, RAM and GPUs, and a display upgrade costs less than a core PC upgrade.
- [Woman Evicted Despite AI Email Approving Late Rent Payment](https://news.lavx.hu/article/woman-evicted-despite-ai-email-approving-late-rent-payment) — *news.lavx.hu*, 28/11 05:09
  > Laura Mack says an AI assistant at Colony Townhome Apartments approved a Nov. 30 payment for $3,934.17 in overdue rent before she was evicted Nov. 19. The case has renewed debate over disclosure and liability for automated customer service tools.
- [[AINews] Inside the exploding Coding Data Market](https://latent.space/p/ainews-inside-the-exploding-coding-data-market/) — *Latent Space*, 28/11 04:45
  > November 27, 2026 — How frontier labs buy training data.
- [Anthropic engineer Thariq Shihipar joins OpenAI](https://news.google.com/rss/articles/CBMilgFBVV95cUxOMFZMbl9DV3YwWlBoajFJQ0EzN0xvTjBDR3I3U0ttbzV2TUV1MHBaTlYwWGNzZmJCOE9IX29hWFdsWGlDQW9MZV9MZ09jc2N1WXVLbzdCTzNzM3dJbGxWVWt5cFJXU1FtTFBPT0dxX0ktR1RQVWtpejBoTUhWMG5RREpsVFljSDN6eW9Bc2FFY3lPZHFmQmc?oc=5) — *TechGig*, 28/11 04:19
- [UK, US Key Systems Hit in String of Attacks as OpenAI Says Cybersecurity Market Potential Outstrips AI Coding](https://news.google.com/rss/articles/CBMidkFVX3lxTFBETFVzbWxKcWlJOVNxd3RVckh2SjFDUmFtR0pEQ1lFWnhZLWg0Wno4WHFZUjVqb3ZDT0dBOGlzaGlvSnB0NllxanFXQ0NNZXl0ckpSaVJpeG1pOFdBVUhMMVdvZjEtd0lpT0htSHlKOFd4Y1dOVFE?oc=5) — *BigGo Finance*, 28/11 04:05
- [Musk Backs Call for Anthropic to Address Alleged Claude Code Changes](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5SeloyT2liWkVqbU9uMkVkd205NzQ0dks5dE1oQXJ3eXdrWThPZnpLUVNEVmNhSHVYb21qTzRyTHBMeFpsaG5qblJmQ2tEOVNXb0F1YW04MDVjV2M?oc=5) — *www.tokenpost.com*, 28/11 02:01
- [Anthropic's Best Customers Spend 20 Times More Than the Rest. That's Why I'm Buying the Stock.](https://www.msn.com/en-us/technology/tech-companies/anthropic-s-best-customers-spend-20-times-more-than-the-rest-that-s-why-i-m-buying-the-stock/ar-AA2ioO1u) — *AOL.com*, 28/11 01:29
  > A quiet line in Anthropic's IPO filing reveals which customers spend the most, and why that matters for the stock.
- [datasette-charts 0.4a0](https://simonwillison.net/2026/Nov/27/datasette-charts/) — *Simon Willison*, 28/11 00:57
  > Release: datasette-charts 0.4a0 The new datasette-charts plugin has its own plugin hook to allow other plugins to define new chart types, but I hadn't actually used it for anything yet. I had Claude Opus 5.5 build an experimental plugins just to try out the hook and it came up with a bunch of fricti
- [Last of Us Part II Multiplayer Mod Creator Says Sony Can’t Stop It](https://happygamer.com/last-of-us-part-2-multiplayer-mod-sony-cant-stop-it-185186/) — *Happy Gamer*, 27/11 23:54
  > A fan-made Last of Us Part II multiplayer mod is in development. Creator Kellie says Sony can't stop it, and that Claude Code wrote most of it.
- [From wearable to smartphone camera: How apps will become the future of sports performance and development](https://itbrief.com.au/story/from-wearable-to-smartphone-camera-how-apps-will-become-the-future-of-sports-performance-and-development) — *IT Brief Australia*, 27/11 23:27
  > App-based AI is bringing professional-grade sports analysis to ordinary phones, cutting costs and widening access to coaching and talent ID.
- [The Last One Percent](https://itbrief.com.au/story/the-last-one-percent) — *IT Brief Australia*, 27/11 23:21
  > Near-perfect benchmark scores still leave AI failing many real-world tasks, raising the risk that dangerous errors hide in the last 1%.
- [Inside the AI Training Data Market — Gabe Greenberg, G2i](https://latent.space/p/inside_the_ai_training_data_market_gabe_greenberg_g2i/) — *Latent Space*, 27/11 23:19
  > A frontier lab can pay more for training data it gets to keep exclusive, or take a discount on data another lab can buy too. At AI Engineer CODE, G2i founder Gabe Greenberg tells swyx how labs make that decision, how small pilot orders turn into bigger...
- [What should your AI agent be allowed to do?](https://itbrief.com.au/story/what-should-your-ai-agent-be-allowed-to-do) — *IT Brief Australia*, 27/11 23:18
  > Publishers that set firm guardrails for AI agents are seeing fewer costly mistakes, better accuracy and faster decision-making before launch.
- [Cascadeur 2026.3 Adds MetaHuman Faces and Tentacle Rigging](https://news.google.com/rss/articles/CBMiigFBVV95cUxQY1RsbjBFVUh1MGhEQUNEdTE3bnNIYnBfYTMwQU81VGNqWFAwVU9wOFZlLUlzRnJfSHBzaXR1aGxDRlVhOV9pNzJ5UTNFdG54cFpmc3prNGFnbC1hN2Q4Wk5Bc2IwQmNYSkhEQ3JKSXpCZDhVcjlLd19IekJETFNFdmgtSTVsYlhzT2c?oc=5) — *Animation World Network*, 27/11 20:41
- [OpenAI countersues Apple over trade secret theft and alleged coercion of shared suppliers](https://the-decoder.com/openai-countersues-apple-over-trade-secret-theft-and-alleged-coercion-of-shared-suppliers/) — *The Decoder*, 27/11 20:38
  > OpenAI is suing Apple in a California court, accusing it of trade secret theft and of coercing shared suppliers. The countersuit follows Apple's own lawsuit from the summer. Just two years ago, the two companies teamed up to bring ChatGPT to the iPhone. Now OpenAI is building its own devices to comp
- [ANT Stock Ends First Full Week Of Trading Around 11% Above IPO Price: Lockup Expiry, Nasdaq 100 Entry Loom](https://www.msn.com/en-us/money/top-stocks/ant-stock-ends-first-full-week-of-trading-around-11-above-ipo-price-lockup-expiry-nasdaq-100-entry-loom/ar-AA2ioaFF) — *TradingView*, 27/11 19:57
  > Anthropic stock ended its first full week of trading at a valuation of about $1.7 trillion after dipping below its offering price earlier in the week. ・Up to 303 million more ANT shares are slated to ...
- [Banned Nvidia Blackwell chips turn up in a Shanghai data center linked to Alice Huang, Bloomberg reports](https://the-decoder.com/banned-nvidia-blackwell-chips-turn-up-in-a-shanghai-data-center-linked-to-alice-huang-bloomberg-reports/) — *The Decoder*, 27/11 19:27
  > Two Chinese companies installed Nvidia's powerful Blackwell chips at a Shanghai data center linked to Alice Huang, according to a Bloomberg investigation. A serial number led Bloomberg to Taiwanese manufacturer Gigabyte. Exporting these chips to China without a US license is illegal. The article Ban
- [Top Treasury Official Is Too Busy Vibe Coding a Crappy Video Game Clone Instead of Addressing a Historic Hack](https://www.msn.com/en-us/news/other/top-treasury-official-is-too-busy-vibe-coding-a-crappy-video-game-clone-instead-of-addressing-a-historic-hack/ar-AA2imP0d) — *Futurism*, 27/11 18:50
  > Maybe he's "vibe working." The post Top Treasury Official Is Too Busy Vibe Coding a Crappy Video Game Clone Instead of Addressing a Historic Hack appeared first on Futurism.
- [Dating App CEO Says Claude Ignored Ethnicity & Skin Tone Preferences, Sabotaged IQ Estimation While Building Its App](https://officechai.com/ai/dating-app-ceo-says-claude-ignored-ethnicity-skin-tone-preferences-sabotaged-iq-estimation-while-building-its-app/) — *OfficeChai*, 27/11 18:46
  > AI coding agents are now writing a large share of the software that startups ship. But one founder says they may also ...
- [Vercel’s CEO thinks the next big AI speedup won’t come from smarter models](https://thenewstack.io/vercel-workflow-sdk-harness/) — *The New Stack*, 27/11 17:50
  > Some of the biggest gains in AI performance over the past year have come from improvements to the harness, not The post Vercel’s CEO thinks the next big AI speedup won’t come from smarter models appeared first on The New Stack .
- [A year from now, VMware wants AI troubleshooting your private cloud](https://thenewstack.io/vmware-private-cloud-kubernetes/) — *The New Stack*, 27/11 17:07
  > A developer who needs two containers to test a change or modification has a different problem from a platform engineer The post A year from now, VMware wants AI troubleshooting your private cloud appeared first on The New Stack .
- [Hackers breached the US Air Force's flagship Cloud One platform, report says](https://the-decoder.com/hackers-breached-the-us-air-forces-flagship-cloud-one-platform-report-says/) — *The Decoder*, 27/11 17:06
  > Hackers breached the US Air Force's flagship cloud platform. The article Hackers breached the US Air Force's flagship Cloud One platform, report says appeared first on The Decoder .
- [The HackerNoon Newsletter: AI Writes Code Faster Than You Can Review It. Now What? (11/27/2026)](https://hackernoon.com/11-27-2026-newsletter?source=rss) — *HackerNoon*, 27/11 17:03
  > 11/27/2026: Top 5 stories on the HackerNoon homepage!
- [T5-Small Out-Downloads NLLB 24 to 1: 143 Open-Weight Translation Models Ranked](https://hackernoon.com/t5-small-out-downloads-nllb-24-to-1-143-open-weight-translation-models-ranked?source=rss) — *HackerNoon*, 27/11 16:30
  > t5-small leads 143 translation models in the TextModels directory. See every model ranked by 30-day Hugging Face downloads, with size and license.
- [Your AI Agent Has Permissions. Who Gave It the Authority?](https://hackernoon.com/your-ai-agent-has-permissions-who-gave-it-the-authority?source=rss) — *HackerNoon*, 27/11 15:09
  > Explore how delegated authorization, scoped credentials, and workload identities can protect systems from AI agent privilege abuse.
- [AI e sviluppo software: la velocità non basta, serve conoscere il patrimonio applicativo](https://www.01net.it/ai-sviluppo-software-software-intelligence-patrimonio-applicativo/) — *01net*, 27/11 12:42
  > Gianluca Altieri, Solution Factory Manager di Innovaway, analizza il ruolo della software intelligence nella gestione delle dipendenze applicative, nella valutazione del rischio tecnologico e nel governo dello sviluppo accelerato dall’AI. L'articolo AI e sviluppo software: la velocità non basta, ser
- [Oltre l’AI Confidence Gap: le previsioni di TeamViewer per il 2027](https://www.01net.it/teamviewer-previsioni-ai-aziende-2027/) — *01net*, 27/11 12:20
  > Dalla produttività individuale a quella aziendale, dalla governance degli agenti autonomi al superamento delle dashboard tradizionali: la visione di Mei Dent, Chief Product and Technology Officer di TeamViewer. L'articolo Oltre l’AI Confidence Gap: le previsioni di TeamViewer per il 2027 è un conten
- [Anthropic’s Rust Rewrite Shows Where the Real Work in AI-Driven Migrations Lives](https://devops.com/anthropics-rust-rewrite-shows-where-the-real-work-in-ai-driven-migrations-lives) — *DevOps.com*, 27/11 11:28
  > Anthropic’s migration of its Messages API from Python to Rust delivered significant performance gains, but exposed a fundamental challenge in AI-assisted software development: generating code is becoming easier than proving it works. For DevOps teams, production verification is emerging as the criti
- [AI in azienda, l’utilizzo quotidiano corre più della formazione e della governance](https://www.01net.it/ai-adoption-aziende-formazione-governance-42skills/) — *01net*, 27/11 11:16
  > L’Osservatorio AI Adoption di 42Skills rileva che l’86,6% dei professionisti intervistati utilizza quotidianamente l’intelligenza artificiale, ma solo il 7,1% opera in organizzazioni dotate di policy formalizzate. L'articolo AI in azienda, l’utilizzo quotidiano corre più della formazione e della gov
- [OpenAI’s GPT‑6.2 correction means you get less AI for the same fee](https://www.infoworld.com/article/4253883/openais-gpt%e2%80%916-2-correction-means-you-get-less-ai-for-the-same-fee.html) — *InfoWorld*, 27/11 11:00
  > OpenAI has corrected a billing error that undercounted usage of its GPT-6.2 Astra and Sol models, warning customers that the same workloads will now consume more of their subscription allowances and cause them to reach usage limits up to 40% faster. The correction, disclosed by Thibault Sottiaux, wh
- [Protect your Python programs from problems and perils](https://www.infoworld.com/article/4252884/protect-your-python-programs-from-problems-and-perils.html) — *InfoWorld*, 27/11 10:00
  > When is a CPython vulnerability not a CPython vulnerability? How do the AI and machine learning capabilities of other programming languages stack up against those of Python? You’ll find the answers to those questions at the links below. And if you’re keeping Python secure and up-to-date on Windows, 
- [SEO local : 6 indicateurs à auditer quand on gère un réseau de points de vente](https://www.blogdumoderateur.com/seo-local-6-indicateurs/) — *Blog du Modérateur*, 27/11 09:50
  > Sur Google comme dans ChatGPT, la visibilité d'une enseigne se joue point de vente par point de vente. L'audit gratuit de Digitaleo mesure ces écarts et priorise les corrections.
- [Avec Parlons Tech, la MAIF ouvre les coulisses de sa DSI et donne la parole à ses experts](https://www.blogdumoderateur.com/parlons-tech-maif-ouvre-coulisses-dsi-parole-experts/) — *Blog du Modérateur*, 27/11 09:38
  > Dans le premier épisode de cette série vidéo, deux experts de la MAIF détaillent l'usage du GitOps sur leur plateforme OpenShift. Ils reviennent sur ce que cette méthode change pour les équipes et sur les pistes explorées, du platform engineering à l'IA.
- [Musique IA - Tidal passe du tag à la poubelle](https://korben.info/tidal-supprime-musique-ia.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 27/11 08:29
  > À partir du 9 décembre, Tidal supprime les morceaux entièrement générés par IA, environ 27 millions de titres, et refuse les nouvelles livraisons. Ce qui part, ce qui reste autorisé, comment c'est détecté et où en sont Deezer, Spotify ou Apple Music.
- [ChatGPT Boosted Consultants' Scores, Not Their Knowledge](https://towardsdatascience.com/chatgpt-boosted-consultants-scores-not-their-knowledge/) — *Towards Data Science*, 26/11 17:00
  > Consultants gained 49 points on coding with AI, while apprentices also gained comprehension — which is why assisted work and expertise need separate names. The post ChatGPT Boosted Consultants' Scores, Not Their Knowledge appeared first on Towards Data Science .
- [Quoting Jack Despain Zhou](https://simonwillison.net/2026/Nov/26/jack-despain-zhou/) — *Simon Willison*, 26/11 16:09
  > Among the many already existing effects of AI has been a great de-individualization. I open a YouTube video, and I hear Claude. I sit in a conference presentation, and I hear Claude. I open my email inbox, and I find pitches and articles from ostensibly serious people with ostensibly serious credent
- [Depuis l’arrivée des AI Overviews, le taux de clics a reculé de 22 % en France](https://www.blogdumoderateur.com/depuis-arrivee-ai-overviews-taux-clics-recule-22-pourcent-france/) — *Blog du Modérateur*, 26/11 16:04
  > Ahrefs a comparé le taux de clics de plus de 31 000 mots clés français, avec et sans résumé IA. Sans surprise, la baisse frappe toutes les positions de la SERP, première place comprise, ainsi que toutes les intentions de recherche.
- [Efficiency gains from AI coding can be lost in review](https://news.google.com/rss/articles/CBMihgFBVV95cUxPLWtqS3kyNU9wYXctMEc1ZEpRaTc4cDlOcENXeG00WEZ1ZkFqUkNTSDUydVRyYUVyakl3S3VRa1BGbDQwT2QyV24weFktQXhCWnJhaHZ1S3Zaa1NIMF9oQ2ZISWpYRHVscHR4dVQ5UXJJZDVJejRVeXYyM0NBYXBqenBqTVl1QQ?oc=5) — *TechInformed*, 27/11 18:45
- [Solana developers get a browser-based coding playground](https://www.thestreet.com/crypto/innovation/solana-playground-lets-developers-build-programs-in-the-browser-with-an-ai-coding-partner) — *TheStreet*, 27/11 18:04
  > Solana's browser-based Playground lets developers write and deploy programs with help from an AI agent that explains and edits code.
- [Anthropic Stock Price Forecast: Rewriting Messaging API in Rust Expected to Lower Claude Service Costs, Stock Poised to Rise Further to $94](https://news.google.com/rss/articles/CBMi3gFBVV95cUxPV2tWSHBkR202ZFh6Nl9DczVvQUM2QlpuTVBxWjJ5Y09tVTZWUmhNM0htMFFKaWU1alJYNGlPNk9ZdS10LUNxeW1mNFoxLWlCVERvVUhOQUNadUROLUFJSEQwTjlfZXk5T2RJSlBOUW9scnJPSDNFNnU0Vy11Rl9CSnJIbEs4RnJJV202eXZUUU5kdXc2UWhxX2tMU1VMck5hZ3hGbEMybklUNUxJTEJ0ZWxYLU1JU1VNTk9VcThvQU9XY1FmSTMzcTlmRTJwaFozREx5eGNkdU54bHlrTXc?oc=5) — *TradingKey*, 27/11 17:33
- ['Make no mistakes': GTA 6 PC port vibe-coding prompt from modder Hyphennn goes viral as community claims locked 60 fps](https://www.sportskeeda.com/gta/make-mistakes-gta-6-pc-port-vibe-coding-prompt-modder-hyphennn-goes-viral-community-claims-locked-60-fps) — *Sportskeeda*, 27/11 15:50
  > In the era of the AI boom, the unofficial GTA 6 PC port has become the latest target of the "vibe-coded" AI-assisted trend.
