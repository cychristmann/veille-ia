# Veille IA outils & code du 22/11/2026

43 articles de médias tech anglophones et francophones (blogs d'outils, Hacker News, Product Hunt) publiés ces 48 dernières heures (rapport généré à 07:43).

**Attention : seulement 43 articles trouvés sur les 50 demandés.**

Sources inaccessibles : Design News.

## Synthèse du jour

La veille révèle une multiplication des plateformes dédiées à l'exécution d'agents IA, avec Google qui lance un Agent Compute Engine et AWS qui enrichit Quick de flux collaboratifs. L'optimisation d'inférence reste centrale, les fournisseurs annoncent l'exécution GPU à grande échelle et des techniques de tuning pour réduire coûts et latence. Du côté du développement, une variété d'outils – de réécriture de code Rust aux CLI d'assistants et aux solutions d'observabilité – montre que l'IA s'intègre profondément dans le quotidien des développeurs. Parallèlement, les bonnes pratiques de prompting et les connecteurs personnalisés se développent pour rendre les modèles plus exploitables. Enfin, la sécurité et la vérification formelle gagnent en visibilité, soulignant la nécessité de garantir la fiabilité des modèles lorsqu'ils sont déployés en production.

*Vérifiée : chaque affirmation est appuyée par au moins un titre.*

## À lire en priorité

- [Google annonce l'Agent Compute Engine pour l'exécution sécurisée d'agents IA](https://www.infoq.com/news/2026/11/google-agent-compute-engine/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 22/11 07:30 · **9/10** (Nouveau service IA sécurisé, impact fort)
  *Titre original : Google Announces Agent Compute Engine for Secure AI Agent Execution*
  > Google recently announced Agent Compute Engine, a managed service that runs AI agents in isolated microVMs, with checkpointing capabilities to suspend and resume execution environments. The design keeps credentials, API keys, and OAuth refresh tokens outside the agent sandbox, using an external Agen
- [AWS Lambda exécute désormais l'inférence GPU avec 48 invocations simultanées partageant un modèle par GPU](https://www.infoq.com/news/2026/11/aws-lambda-gpu-managed-instances/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 22/11 07:27 · **8/10** (Extension GPU à Lambda, facilite l'inférence à grande échelle)
  *Titre original : AWS Lambda Now Runs GPU Inference with 48 Concurrent Invocations Sharing One Model per GPU*
  > AWS Lambda now runs Event Functions on EC2 G-series GPU instances through Lambda Managed Instances, with up to 48 concurrent invocations sharing one model per GPU, vLLM and SGLang base images that need no handler code, and 90-minute asynchronous timeouts. Billing is the instance price plus a 9.75 pe
- [OpenAI lance GPT-Live-1.1 pour les agents vocaux et réduit le coût d'inactivité à 0,02 $/min](https://www.marktechpost.com/2026/11/21/openai-gpt-live-1-1-api-standby-mode/) — *MarkTechPost*, 21/11 12:46 · **8/10** (OpenAI GPT‑Live‑1.1 voix, réduction coût, avancée produit)
  *Titre original : OpenAI Ships GPT-Live-1.1 for Voice Agents, Cuts Idle Cost to $0.02/Min*
  > OpenAI has released GPT-Live-1.1 in the API. The full-duplex voice model improves multilingual accents and transcription, and a new standby mode bills idle WebRTC time at $0.02 per minute instead of $0.05. The post OpenAI Ships GPT-Live-1.1 for Voice Agents, Cuts Idle Cost to $0.02/Min appeared firs
- [Nvidia lance le cluster DGX Spark de bureau pour les chercheurs](https://itbrief.com.au/story/nvidia-launches-desk-side-dgx-spark-cluster-for-researchers) — *IT Brief Australia*, 20/11 17:00 · **8/10** (Nvidia DGX Spark desk‑side, nouveau hardware de recherche)
  *Titre original : Nvidia launches desk-side DGX Spark cluster for researchers*
  > Researchers could cut queue times with a four-node desk cluster that lets them test AI and simulation workloads locally before scaling up.
- [ARTEX, l'IA de piratage open source qui a glacé la Commission européenne](https://korben.info/artex-lia-de-piratage-open-source-qui-a-fige-la-commission-europeenne.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 20/11 15:50 · **8/10** (ARTEX IA piratage, incident de sécurité majeur)
  *Titre original : ARTEX, l'IA de piratage open source qui a figé la Commission européenne*
  > La Commission européenne a reconnu le 19 novembre une campagne de piratage débutée le 22 octobre, qui a paralysé Sysper et MyPMO pendant plus de dix jours. Le CERT-EU pointe ARTEX, un outil open source chinois d'agents IA détourné, déjà lié à des attaques contre ConnectWise et des firmes sud-coréenn

## Plateformes et exécution d'agents IA (7)

Ces articles présentent des services et des infrastructures dédiés à l'exécution d'agents IA, depuis le nouveau Agent Compute Engine de Google jusqu'aux capacités d'agents collaboratifs dans AWS Quick et aux solutions de gestion d'agents dans SageMaker.

- [Google annonce l'Agent Compute Engine pour l'exécution sécurisée d'agents IA](https://www.infoq.com/news/2026/11/google-agent-compute-engine/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 22/11 07:30 · **9/10** (Nouveau service IA sécurisé, impact fort)
  *Titre original : Google Announces Agent Compute Engine for Secure AI Agent Execution*
  > Google recently announced Agent Compute Engine, a managed service that runs AI agents in isolated microVMs, with checkpointing capabilities to suspend and resume execution environments. The design keeps credentials, API keys, and OAuth refresh tokens outside the agent sandbox, using an external Agen
- [OpenAI lance GPT-Live-1.1 pour les agents vocaux et réduit le coût d'inactivité à 0,02 $/min](https://www.marktechpost.com/2026/11/21/openai-gpt-live-1-1-api-standby-mode/) — *MarkTechPost*, 21/11 12:46 · **8/10** (OpenAI GPT‑Live‑1.1 voix, réduction coût, avancée produit)
  *Titre original : OpenAI Ships GPT-Live-1.1 for Voice Agents, Cuts Idle Cost to $0.02/Min*
  > OpenAI has released GPT-Live-1.1 in the API. The full-duplex voice model improves multilingual accents and transcription, and a new standby mode bills idle WebRTC time at $0.02 per minute instead of $0.05. The post OpenAI Ships GPT-Live-1.1 for Voice Agents, Cuts Idle Cost to $0.02/Min appeared firs
- [Nouveautés dans AWS Quick : flux plus performants, interface web mise à jour et agents collaboratifs](https://aws.amazon.com/blogs/machine-learning/new-in-aws-quick-more-capable-flows-an-updated-web-experience-and-agents-that-work-together/) — *AWS Machine Learning*, 21/11 02:06 · **7/10** (Mise à jour AWS Quick avec agents collaboratifs, fonctionnalité notable)
  *Titre original : New in AWS Quick: More capable flows, an updated web experience, and agents that work together*
  > AWS Quick is the AI workspace built only for work. Today we're releasing updates that help your team get more done: build and run business-process flows in chat, triage your day in the updated web app, get more complete answers from multiple agents at once, and connect new data sources like Meta ads
- [Introduction des extensions de cluster gérées pour l'observabilité et la gestion des utilisateurs dans Amazon SageMaker HyperPod Slurm](https://aws.amazon.com/blogs/machine-learning/introducing-managed-cluster-extensions-for-observability-and-user-management-in-amazon-sagemaker-hyperpod-slurm/) — *AWS Machine Learning*, 21/11 00:07 · **7/10** (Extensions cluster SageMaker HyperPod, améliore observabilité)
  *Titre original : Introducing managed cluster extensions for observability and user management in Amazon SageMaker HyperPod Slurm*
  > Amazon SageMaker HyperPod now offers managed cluster extensions for observability and user management, bringing declarative, API- and console-driven configuration to the software running on Slurm cluster nodes. This post explains how the extensions work and follows a platform team through a quarter 
- [Meta ads est désormais disponible dans AWS Quick](https://aws.amazon.com/blogs/machine-learning/meta-ads-is-now-available-in-aws-quick/) — *AWS Machine Learning*, 22/11 02:59 · **6/10** (Lancement de Meta ads sur AWS Quick, nouvelle intégration produit)
  *Titre original : Meta ads is now available in AWS Quick*
  > AWS Quick now has a Meta ads AI connector. Meta advertisers can use natural language in Quick to create, manage, and analyze campaigns while staying connected to the Meta ad management network, and combine Meta ad data with first- and third-party sources to build dashboards, documents, slide decks, 
- [Picsart ouvre l'IA derrière sa plateforme aux développeurs et aux entreprises](https://www.01net.it/picsart-opens-the-ai-behind-its-platform-to-developers-businesses/) — *01net*, 20/11 23:54 · **6/10** (Picsart ouvre son IA aux développeurs, API exploitable)
  *Titre original : Picsart Opens the AI Behind Its Platform to Developers & Businesses*
  > With Picsart Platform, developers can build their own video, audio, image features using 250+ models from 30+ providers, alongside Picsart's own editing models, through one API, CLI or MCP server. Key Takeaways One bundle, four ways to build: the API... L'articolo Picsart Opens the AI Behind Its Pla
- [Résumé : Visa étend Agentic Ready pour favoriser la croissance mondiale du commerce fiable basé sur l'IA](https://www.01net.it/riassunto-visa-amplia-agentic-ready-per-contribuire-a-far-crescere-a-livello-globale-il-commercio-affidabile-basato-sullia/) — *01net*, 20/11 22:00 · **4/10** (Annonce Visa Agentic Ready, orientation commerciale)
  *Titre original : Riassunto: Visa amplia Agentic Ready per contribuire a far crescere a livello globale il commercio affidabile basato sull’IA*
  > Adyen, Antom, Billtrust, Checkout.com, Fiserv, Global Payments, J.P. Morgan Payments, PayPal e Stripe, insieme a oltre 140 partecipanti iniziali, aderiscono al programma Agentic Ready per l’ecosistema dell’accettazione. Esercenti, fornitori B2B, forni... L'articolo Riassunto: Visa amplia Agentic Rea

## Optimisation d'inférence et GPU (7)

Les titres portent sur l'accélération de l'inférence grâce aux GPU, la réduction des coûts et de la latence, ainsi que sur des techniques de tuning spécifiques aux modèles Claude et aux grands modèles de Nvidia.

- [AWS Lambda exécute désormais l'inférence GPU avec 48 invocations simultanées partageant un modèle par GPU](https://www.infoq.com/news/2026/11/aws-lambda-gpu-managed-instances/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 22/11 07:27 · **8/10** (Extension GPU à Lambda, facilite l'inférence à grande échelle)
  *Titre original : AWS Lambda Now Runs GPU Inference with 48 Concurrent Invocations Sharing One Model per GPU*
  > AWS Lambda now runs Event Functions on EC2 G-series GPU instances through Lambda Managed Instances, with up to 48 concurrent invocations sharing one model per GPU, vLLM and SGLang base images that need no handler code, and 90-minute asynchronous timeouts. Billing is the instance price plus a 9.75 pe
- [Nvidia lance le cluster DGX Spark de bureau pour les chercheurs](https://itbrief.com.au/story/nvidia-launches-desk-side-dgx-spark-cluster-for-researchers) — *IT Brief Australia*, 20/11 17:00 · **8/10** (Nvidia DGX Spark desk‑side, nouveau hardware de recherche)
  *Titre original : Nvidia launches desk-side DGX Spark cluster for researchers*
  > Researchers could cut queue times with a four-node desk cluster that lets them test AI and simulation workloads locally before scaling up.
- [Nvidia a utilisé 20 000 exemples d'entraînement pour corriger les erreurs de son IA. Son score de codage a bondi.](https://thenewstack.io/nvidia-droid-harness-nemotron/) — *The New Stack*, 21/11 16:30 · **7/10** (Nvidia améliore modèle avec 20 k exemples, résultat mesurable)
  *Titre original : Nvidia used 20,000 training examples to fix its AI’s mistakes. Its coding score jumped.*
  > Nvidia used Factory’s Droid coding-agent harness to generate roughly 20,000 rows of post-training data for Nemotron 3 Ultra, the 550-billion-parameter The post Nvidia used 20,000 training examples to fix its AI’s mistakes. Its coding score jumped. appeared first on The New Stack .
- [Meta TLX, une extension de compilateur GPU native prenant en charge les capacités matérielles avancées](https://www.infoq.com/news/2026/11/meta-triton-tlx-gpu-compiler/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 20/11 19:00 · **7/10** (Meta TLX, extension compilateur GPU, avancée technique)
  *Titre original : Meta TLX, a Native GPU Compiler Extension Supporting Advanced Hardware Capabilities*
  > Meta developed Triton Low-Level Extensions (TLX), designed to bridge the gap between high-level GPU programming abstractions and the low-level execution control required to fully exploit modern GPU architectures. By Sergio De Simone
- [Alibaba entraînait Qwen avec des puces T-Head, selon des rapports](https://www.neoteo.com/es/alibaba-entrenaba-qwen-con-chips-t-head-segun-informes) — *NeoTeo*, 20/11 15:51 · **7/10** (Alibaba entraîne Qwen sur puces T‑Head, avancée modèle matériel)
  *Titre original : Alibaba entrenaba Qwen con chips T-Head, según informes*
  > Alibaba entrenaba su Qwen insignia de próxima generación con chips T-Head, según informes; Eddie Wu también habló de inferencia y planes de suministro.
- [Compétence d'optimisation d'inférence : Ajustement du LLM Claude Code](https://news.google.com/rss/articles/CBMimgFBVV95cUxOejJmakJOUXNoWV9XYUtYdUZra0V0S21Uc2c4MnhPb3o4WEhEbXcxRi1OLW01cnNVLVVCVGtOZkQ3NU10eURGQy1PNldWSkNuaVNjdmNVVEd0czY3czNIdzlSbkE3eVJtNDhsdGZPYUlYSklyUG10Ny03QlYyV3pNMEJGV0NKSnY3WFZrUUxpcC14NjNwSThrVXp3?oc=5) — *explainx.ai*, 22/11 01:00 · **6/10** (Skill d'optimisation d'inférence Claude Code, appliquable immédiatement)
  *Titre original : Inference Optimisation Skill: Claude Code LLM Tuning*
- [Réduire le coût et la latence des LLM auto-hébergés grâce à la compétence d'agent de cache KV distribué](https://aws.amazon.com/blogs/machine-learning/cut-self-hosted-llm-cost-and-latency-with-the-distributed-kv-caching-agent-skill/) — *AWS Machine Learning*, 21/11 01:14 · **6/10** (Skill KV cache distribué, baisse coût/latence LLM)
  *Titre original : Cut self-hosted LLM cost and latency with the distributed KV caching agent skill*
  > Self-hosting LLMs on GPUs means paying to recompute the same context on every turn. Distributed KV caching with Amazon ElastiCache can cut inference cost by up to 40% and time to first token by up to 80%. This post walks through the distributed KV caching skill in the Agent Toolkit for AWS, which ev

## Outils de codage assisté par IA (13)

Cette catégorie regroupe les outils qui intègrent l'IA dans le flux de travail de développement : réécriture de code Rust, assistants de codage locaux, CLI pour créer des Lenses, comparatifs de modèles, plateformes d'observabilité AI, et projets comme Inkling 2 Mini et l'agent de codage d'Apple.

- [Dynatrace vient de présenter son guide d'observabilité IA à KubeCon. Voici pourquoi c'est important pour les développeurs.](https://thenewstack.io/ai-feature-flags-observability/) — *The New Stack*, 21/11 17:08 · **7/10** (Playbook AI observabilité Dynatrace, impact développeurs cloud)
  *Titre original : Dynatrace just laid out its AI observability playbook at KubeCon. Here’s why it matters for developers.*
  > A new AI model goes live for a small group of users. Some of them start seeing errors. The build The post Dynatrace just laid out its AI observability playbook at KubeCon. Here’s why it matters for developers. appeared first on The New Stack .
- [OpenCode et un LLM local gèrent les 80 % de tâches répétitives, laissant à Claude la partie complexe](https://www.xda-developers.com/opencode-and-a-local-llm-handle-the-boring-80-of-my-coding-so-claude-only-gets-the-hard-part/) — *XDA*, 21/11 20:00 · **6/10** (Utilisation locale d'LLM pour coder, gain de productivité concret)
  *Titre original : OpenCode and a local LLM handle the boring 80% of my coding, so Claude only gets the hard part*
  > The F1 key, the speed jump between levels, and the high score file all passed on Qwen's first test run without a hitch, and all six of the failures sat in the steps that Opus specifically had flagged ...
- [Snap lance Easy Lens CLI pour créer des Lenses avec des assistants IA](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPeHp2SWU4bEhpOVBpUUFaZk9fODRKaGotSFhoY3phNVA4Tzc1ejhxUXZZV1YzYlN5M0JsMzZ0dzI5UVBNQXI2MktmN0dxQ2xROFc2eml3X0VQeEZxdGttUGhkT3A3OFcwelhDQW0yUlVza1lzN2VUV1lwdU54NUVTc05YQjV1VW1GOWIzQklpOEVhVnk3Sy1mVHgzNUVXTDVJYmoxcFFvTzg?oc=5) — *Foro3D*, 21/11 18:27 · **6/10** (Snap Easy Lens CLI, création d'assistants IA, outil pratique)
  *Titre original : Snap launches Easy Lens CLI to create Lenses with AI assistants*
- [À la découverte d'Inkling 2 Mini de Thinking Machines : un modèle 26B MoE en boucle tournant sur un Mac 32 Go](https://www.marktechpost.com/2026/11/21/thinking-machines-inkling-2-mini-looped-transformer/) — *MarkTechPost*, 21/11 13:13 · **6/10** (Présentation Inkling 2 Mini 26B MoE, nouveau workflow codage)
  *Titre original : Meet Thinking Machines Inkling 2 Mini: 26B Looped MoE Runs on a 32GB Mac*
  > Thinking Machines released Inkling 2 Mini, a 26.4B-parameter looped MoE transformer with 3.4B active parameters. It runs on a 32GB Mac or one DGX Spark and scores 79.2% on SWE-bench Verified. The post Meet Thinking Machines Inkling 2 Mini: 26B Looped MoE Runs on a 32GB Mac appeared first on MarkTech
- [Legora ajoute la gestion des équipes et la recherche par IA à Microsoft 365](https://itbrief.com.au/story/legora-adds-teams-intake-ai-search-to-microsoft-365) — *IT Brief Australia*, 20/11 07:59 · **6/10** (Legora ajoute IA search à Teams, améliore productivité MS365)
  *Titre original : Legora adds Teams intake & AI search to Microsoft 365*
  > Legal teams can now keep requests and search results inside Microsoft 365, cutting the time spent chasing context across chats, inboxes and meetings.
- [Raph Levien dresse le bilan des lacunes des interfaces graphiques en Rust à l'heure de l'IA](https://news.lavx.hu/article/raph-levien-maps-rust-gui-gaps-as-ai-rewrites-accelerate) — *news.lavx.hu*, 22/11 06:15 · **5/10** (Analyse niche des gaps Rust GUI, intérêt limité)
  *Titre original : Raph Levien Maps Rust GUI Gaps as AI Rewrites Accelerate*
  > In a Nov. 21, 2026, post, Raph Levien argues Rust can deliver higher GUI performance than current stacks, while mobile native behavior, system compositing, and scalability gaps remain.
- [GPT-6.2 Sol face à Claude Opus 5.5 : moins précis, mais peut-être un meilleur investissement](https://thenewstack.io/gpt-6-2-sol-vs-claude-opus-5-5/) — *The New Stack*, 21/11 18:08 · **5/10** (Comparaison GPT‑6.2 / Claude Opus, analyse intéressante mais non décisive)
  *Titre original : GPT-6.2 Sol vs. Claude Opus 5.5: Not as accurate, but still might be the better buy*
  > Claude Opus 5.5 is the model everyone wants to beat, and it has a mixed record in my tests since The post GPT-6.2 Sol vs. Claude Opus 5.5: Not as accurate, but still might be the better buy appeared first on The New Stack .
- [Configuration d'Inkling 2 Mini avec Ollama : prérequis Mac et options PC](https://news.google.com/rss/articles/CBMib0FVX3lxTE5wVy14UUw1RVVadHFrVVhSNHY2Tm1CcHFwU3lFam0zYVM4Z3hJNnRZZ3ZIbFhzZTF5YVBsR0RoLXRMOTBlUTctcF9aTktFeXNCQ21EdWx0UWJUd0ZzQmxKWjhzNWhITW1qRVNzT0o1dw?oc=5) — *GitHub*, 21/11 17:00 · **5/10** (Guide d'installation Inkling 2 Mini, tutoriel technique)
  *Titre original : Inkling 2 Mini Ollama Setup: Mac Requirements and PC Options*
- [Archie, l'outil français qui transforme vos contenus oubliés en posts sur les réseaux sociaux](https://www.blogdumoderateur.com/archie-outil-francais-transforme-contenus-oublies-posts-reseaux-sociaux/) — *Blog du Modérateur*, 20/11 09:37 · **5/10** (Archie, outil français de republishing, utilité niche)
  *Titre original : Archie, l’outil français qui transforme vos contenus oubliés en posts sur les réseaux sociaux*
  > Dévoilé fin octobre par Agorapulse, Archie est un outil dopé à l'IA, capable de créer des publications percutantes à partir d'un webinaire, d'un rapport interne ou d'un livre blanc. Des contenus « riches en idées originales », mais encore inexploités.
- [Apple développerait un agent IA pour le codage et le contrôle des applications](https://news.google.com/rss/articles/CBMingFBVV95cUxOb3hUSE5SQTRzejdhSThPRWFMcjhCT0FFWHJLc2hJZUVOUFZhRS1McjgxNGs2SE9hcEpDaWRNUlZsNE5xQmFsZk04d3paY0V4OEJvQTNDZlRhcUlWNTlNQmc1UlVzNDRTTVNmOVltdHh2VlBnYzJUS2l6NEhtbnF6TGlpb0F1bHBEdFMtYVlpbk40cV9LaS1yekgyV3FxUdIBowFBVV95cUxQNXIxMVYzcmRfYzZKdnpLcXZrVVB0cmF6ZWF2SGw2OTlRWnNPRFNhOGtRc2lwZUwxU1h3Qm1xZjBmRktpdC1BSkxDUmRrZHhxZDM5OXJqUlZUYjNLbTVQLVV1aGwwaXhxRzJDX1lUTldOekQxbmRudUhjbWNMUFFpN2NTSUQtV3h1SXlMNDdVOTZldW9SY0hOQk5tWXpmWVhNWm0w?oc=5) — *TechGig*, 21/11 08:05 · **4/10** (Rumeur Apple agent IA coding, peu de preuves)
  *Titre original : Apple reportedly developing AI agent for coding, app control*
- [WaitFeed](https://www.producthunt.com/products/waitfeed-2) — *Product Hunt*, 20/11 21:01 · **4/10** (Produit WaitFeed peu connu, intérêt limité)
  *Titre original : WaitFeed*
  > Tech feed inside agent wait time Discussion | Link
- [Stitch Loop](https://www.producthunt.com/products/stitch-loop) — *Product Hunt*, 20/11 20:38 · **4/10** (Produit Stitch Loop, visibilité faible)
  *Titre original : Stitch Loop*
  > Google’s AI agent that ships fixes and watches the metric Discussion | Link
- [gitroots](https://www.producthunt.com/products/gitroots) — *Product Hunt*, 20/11 14:22 · **4/10** (Produit gitroots, peu d'impact connu)
  *Titre original : gitroots*
  > Path-level GitHub access for developers and AI agents Discussion | Link

## Prompting, évaluation et connecteurs (7)

Les articles abordent les bonnes pratiques de prompting, les guides d'évaluation des sorties LLM, les ateliers autour de Claude et les connecteurs personnalisés permettant d'étendre les capacités des modèles IA.

- [Tanmay Kumar Chaurasia publie un guide pour évaluer les sorties des LLM](https://news.lavx.hu/article/tanmay-kuamr-chaurasia-publishes-guide-to-evaluating-llm-outputs) — *news.lavx.hu*, 22/11 06:00 · **6/10** (Guide pratique d'évaluation des sorties LLM, utile aux développeurs)
  *Titre original : Tanmay Kuamr Chaurasia Publishes Guide to Evaluating LLM Outputs*
  > Tanmay Kuamr Chaurasia published a DEV Community guide that treats LLM evaluation as engineering infrastructure, with offline tests, production scoring, and human review queues.
- [OpenAI partage de nouveaux conseils de prompting pour GPT-6.2 Astra et Sol afin d'éviter les réponses trop brèves et les questions inutiles](https://the-decoder.com/openai-shares-new-prompting-tips-for-gpt-6-2-astra-and-sol-to-fix-brief-answers-and-unnecessary-questions/) — *The Decoder*, 21/11 14:32 · **6/10** (Conseils de prompting OpenAI, améliore l'usage de GPT‑6.2)
  *Titre original : OpenAI shares new prompting tips for GPT-6.2 Astra and Sol to fix brief answers and unnecessary questions*
  > OpenAI has released new prompt templates for GPT-6.2 Astra and Sol meant to fix common model behaviors such as overly brief answers, unnecessary follow-up questions, and excessive testing when coding. The API is changing as well, since editing a conversation's history can discard reasoning content a
- [Clairic atteint 98 % de précision sur 72,8 % des questions via des scores de confiance](https://towardsdatascience.com/clairic-hit-98-accuracy-on-728-of-questions-via-confidence-scores/) — *Towards Data Science*, 20/11 16:00 · **6/10** (Clairic atteint 98 % précision via scores de confiance, résultat concret)
  *Titre original : Clairic Hit 98% Accuracy on 72.8% of Questions via Confidence Scores*
  > With a 0.9 confidence cutoff, Cloudflare's System One model handles the easy cases and routes the rest to a bigger, slower LLM like Luna. The post Clairic Hit 98% Accuracy on 72.8% of Questions via Confidence Scores appeared first on Towards Data Science .
- [Les connecteurs Claude expliqués : comment ajouter un connecteur personnalisé (avec un exemple WordPress)](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9QbHZMZEhNbTMwUlFBZGx6SUxENlBtN1ZGU3FNTm1CMldTZkszZU1wMndvVC1FWEdNRHNDRHprMEJEa2RWeXcwcFFjbWo1S0FWUzljN2hjNFg?oc=5) — *Themeisle*, 21/11 22:10 · **5/10** (Tutoriel connecteurs Claude, utile mais assez ciblé)
  *Titre original : Claude Connectors Explained: How to Add a Custom Connector (With a WordPress Example)*
- [GPT-6.2 Astra et Sol : ce que disent les premières critiques](https://www.neoteo.com/es/gpt-62-astra-y-sol-que-dicen-las-primeras-criticas) — *NeoTeo*, 20/11 17:20 · **5/10** (Critiques GPT‑6.2 Astra y Sol, aperçu utilisateur)
  *Titre original : GPT-6.2 Astra y Sol: qué dicen las primeras críticas*
  > Primeras evaluaciones de GPT-6.2 Astra y Sol: críticas, retest con mejora parcial, una limitación descrita por OpenAI y demos de tareas concretas.
- [Analyse : il ne suffit pas de se fier à un seul modèle IA pour découvrir les vulnérabilités de code](https://devops.com/analysis-not-enough-to-rely-on-one-ai-model-to-discover-code-vulnerabilities) — *DevOps.com*, 20/11 22:51 · **4/10** (Analyse opinion sur modèle unique, peu de nouveauté)
  *Titre original : Analysis: Not Enough to Rely on One AI Model to Discover Code Vulnerabilities*
  > An analysis published this week of vulnerabilities discovered in open-source code using three different artificial intelligence (AI) models found that all three identified the same issue in only one instance out of 121 distinct findings. Conducted by Echo, a provider of hardened software artifacts a
- [Atelier Claude AI : Formats gratuits, payants et officiels (2026)](https://news.google.com/rss/articles/CBMijwFBVV95cUxQXzJkRmJ5SG9Ial9xRVRpWW00bW4wQV9Rb2lpZ0Z6bEdwUXBRaXhWZWNiT2ZzcjhERmJvMWNub3NxamY3ek1xMUdQTFFVOE9mbF9jQ2NFM1VEa3U1LUtBME5RVlFMRlBKUkZCSExWNkxReEZ0Rk80WjVGN3B3dDFZemxIUmdSUjZRMVJQSXNIaw?oc=5) — *explainx.ai*, 22/11 01:00 · **3/10** (Annonce d'ateliers Claude, plus promotionnel que technique)
  *Titre original : Claude AI Workshop: Free, Paid, and Official Formats (2026)*

## Sécurité, vérification et IA d'entreprise (6)

Ces deux titres traitent de la vérification formelle de kernels GPU avec TensorLean et de la promesse des agents IA d'augmenter les capacités humaines dans les entreprises, illustrant les enjeux de fiabilité et d'adoption à grande échelle.

- [ARTEX, l'IA de piratage open source qui a glacé la Commission européenne](https://korben.info/artex-lia-de-piratage-open-source-qui-a-fige-la-commission-europeenne.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 20/11 15:50 · **8/10** (ARTEX IA piratage, incident de sécurité majeur)
  *Titre original : ARTEX, l'IA de piratage open source qui a figé la Commission européenne*
  > La Commission européenne a reconnu le 19 novembre une campagne de piratage débutée le 22 octobre, qui a paralysé Sysper et MyPMO pendant plus de dix jours. Le CERT-EU pointe ARTEX, un outil open source chinois d'agents IA détourné, déjà lié à des attaques contre ConnectWise et des firmes sud-coréenn
- [Une équipe de chercheurs de Columbia et CertiK présente TensorLean pour la vérification formelle des noyaux GPU](https://www.marktechpost.com/2026/11/21/columbia-certik-tensorlean-formal-verification-gpu-kernels/) — *MarkTechPost*, 22/11 02:51 · **7/10** (TensorLean, vérification formelle GPU, avancée technique notable)
  *Titre original : A Team of Researchers from Columbia and CertiK Introduce TensorLean for Formal Verification of GPU Kernels*
  > TensorLean, from Columbia University and CertiK, formally verifies production GPU kernels at the PTX level using Lean. It checked 149 kernel instances, proved 83 correct, and found 38 bugs in FlashAttention, DeepGEMM and more. The post A Team of Researchers from Columbia and CertiK Introduce TensorL
- [Google fait don d'Agent Substrate et gVisor à la CNCF pour sécuriser les agents IA à grande échelle](https://www.infoq.com/news/2026/11/google-substrate-gvisor-cncf/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 20/11 13:00 · **7/10** (Google donne Agent Substrate au CNCF, renforce écosystème IA)
  *Titre original : Google Donates Agent Substrate and gVisor to the CNCF to Secure AI Agents at Scale*
  > Google has announced it is donating Agent Substrate and gVisor to the Cloud Native Computing Foundation (CNCF), placing two important components of its AI agent infrastructure under vendor-neutral open-source governance. By Craig Risi
- [Combattre la distillation adverse](https://openai.com/index/combatting-adversarial-distillation) — *OpenAI*, 20/11 11:00 · **7/10** (Recherche combat adversarial distillation, enjeu de sécurité IA)
  *Titre original : Combatting adversarial distillation*
  > OpenAI’s layered approach to adversarial distillation combines model training, safeguards, detection, and enforcement to protect against capability extraction.
- [La guerre contre le « slop » et une arme émergente pour le combattre : la vérification formelle](https://latent.space/p/formal-verification/) — *Latent Space*, 20/11 22:18 · **5/10** (Formal verification contre le slop, sujet de recherche émergent)
  *Titre original : The War Against Slop and an Emerging Weapon to Fight it: Formal Verification*
  > Proving software correct with math has traditionally required specialist work. Now AI and Lean are helping automate the process.
- [Brian Armstrong, PDG de Coinbase, affirme que les agents IA peuvent offrir aux employés une équipe illimitée de niveau L5](https://cryptobriefing.com/brian-armstrong-ai-agents-coinbase-team/) — *Crypto Briefing*, 22/11 05:04 · **2/10** (Opinion financière, peu pertinent pour l'outil IA)
  *Titre original : Coinbase CEO Brian Armstrong says AI agents can give workers an unlimited team of L5-level staff*
  > AI agents could revolutionize workforce dynamics, shifting focus from hiring to oversight, but human judgment remains crucial for decision-making. The post Coinbase CEO Brian Armstrong says AI agents can give workers an unlimited team of L5-level staff appeared first on Crypto Briefing .

## Autres articles (3)

- [Google apprend aux agents de codage IA à intégrer Analytics dans les applications iOS et Android](https://news.google.com/rss/articles/CBMimAFBVV95cUxOTlBLRk5zcFZuRmRUZloyd0FfQTlyUnNuZmtPZkRBY29sNElUMjk3bnRqMldwUFRNVkZTRTFQVE1VYjdDTl9fUzNzclYyYmtJOGZmdC1UcUtNMTFXTDlhSDFqZTlnWUk5MnNNTFBpR21nR1dqTmJQbFhzSFJrNl9WMjVHVmV0bkkySDhmaU1fVFZvcnZ4aHVkRQ?oc=5) — *PPC Land*, 21/11 12:30 · **7/10** (Google enseigne agents IA à intégrer Analytics, outil concret)
  *Titre original : Google teaches AI coding agents to wire Analytics into iOS and Android apps*
- [Baseten lance Bison-1 et Groundhog-1, en tête de l'indice des modèles de décision](https://www.marktechpost.com/2026/11/20/baseten-bison-1-groundhog-1-gemma-4-decision-models/) — *MarkTechPost*, 21/11 05:01 · **7/10** (Baseten publie Bison‑1 & Groundhog‑1, nouveaux modèles décisionnels)
  *Titre original : Baseten Releases Bison-1 and Groundhog-1, Topping Decision Model Index*
  > Baseten released bison-1 and groundhog-1, open-weight decision models built on Gemma 4. bison-1 scores 76 on the AA Decision Index v2.1, and both models support 128k context and image input. The post Baseten Releases Bison-1 and Groundhog-1, Topping Decision Model Index appeared first on MarkTechPos
- [Les craintes sur les investissements IA entraînent une vente massive sur les marchés alors que le resserrement de la Fed questionne](https://www.tokenpost.com/news/insights/62394) — *TOKENPOST*, 21/11 18:00 · **2/10** (Peur d'investissement IA, sujet financier peu pertinent)
  *Titre original : AI investment fears drive market selloff as Fed tightening comes into question*
  > Dean Curnutt said a deepening AI-led selloff could force the Fed to retreat from tightening. He pointed to short-dated U.S. Treasuries as a way to navigate volatility and potential rate cuts.

## Vidéos à regarder (10)

- [Matt Pocock's Claude Code pipeline builds entire features on its own while you're away, and you…](https://www.youtube.com/watch?v=thW85XLwKYM) — *morenicksaraev1*, 21/11 23:11
  > Une présentation du pipeline Claude Code utilisé par Matt Pocock pour automatiser la construction de fonctionnalités complexes de manière autonome.
- [Stuck halfway through a project? Your AI needs Plan Mode #claudecode #cursor #aicoding](https://www.youtube.com/watch?v=hvhFu2F8xRE) — *Agents Shipped It*, 22/11 07:29
  > Une analyse technique sur la résolution de problèmes complexes avec Claude Code et l'importance d'un 'mode plan' pour éviter que l'agent ne corrompe le projet.
- [MCP Registry: The App Store for AI Agent Tools](https://www.youtube.com/watch?v=Er0ay2ecHw8) — *Kernel Cast*, 21/11 19:00
  > Une présentation du registre MCP (Model Context Protocol), décrit comme un 'App Store' facilitant la découverte d'outils et de services pour les agents IA.
- [Agent permissions need an undo plan #agents #mcp #safety #ai](https://www.youtube.com/watch?v=GHGqvsKad3s) — *Practical AI*, 22/11 01:00
  > Une réflexion théorique et pratique sur la sécurité des agents IA, explorant des solutions pour annuler ou réparer les erreurs causées par des appels d'outils inappropriés.
- [Microsoft MAI Code 2: 96% of Claude for 5% of the Price](https://www.youtube.com/watch?v=jsDAOxyqNmA) — *AI ToolLab*, 21/11 18:30
  > Une comparaison des performances et du positionnement tarifaire du nouveau modèle MAI Code 2 de Microsoft face à Claude.
- [12 Frameworks to Build MCP AI Agents in 2027 🚀 | AI Engineering Tools Explained #shorts](https://www.youtube.com/watch?v=4lqEdSyxmzE) — *withmeApurva*, 22/11 05:54
  > Un tour d'horizon des douze meilleurs frameworks et SDK permettant de construire des agents IA basés sur le protocole MCP en 2027.
- [5 Claude Code Automation Tricks 🔁 #claudecode #shorts](https://www.youtube.com/watch?v=MmrpsGQbo80) — *code.coffee.repeat*, 21/11 19:29
  > Cinq astuces concrètes pour optimiser l'automatisation avec Claude Code, incluant l'auto-correction CI et les refactorisations par lots.
- [MCP vs Code Mode: What Actually Changed?](https://www.youtube.com/watch?v=hLmYtFZOGKc) — *KodeKloud*, 21/11 16:16
  > Une analyse technique clarifiant la distinction et l'interaction entre le mode Code de Cloudflare et le protocole MCP.
- [AI Agent Reading HR Files? Fix It with Citadel Identity360 #Shorts](https://www.youtube.com/watch?v=RBHDmevGafQ) — *ASTRANOVA LABS*, 22/11 05:51
  > Une approche sur la sécurité et le contrôle d'accès des agents IA, illustrée par la gestion des fichiers RH sensibles via Citadel Identity360.
- [1 CLAUDE.md Line Made Claude Code Stop Instead of Bending My Code](https://www.youtube.com/watch?v=ppFrK8jhDfA) — *Agent Workbench*, 21/11 15:00
  > Un tutoriel sur l'utilisation du fichier CLAUDE.md pour restreindre le comportement d'un agent de codage et éviter les modifications indésirables du code.

## Podcasts à écouter (10)

- [DEVIKA: OpenSource DEVIN Alternative! OpenSource AI Software Engineer | Getting Started with DEVIKA](https://podcasts.apple.com/us/podcast/devika-opensource-devin-alternative-opensource-ai-software/id6826122006?i=1000797739961&uo=4) — *AICodeKing*, 22/11 06:30
  > Présentation de DEVIKA, une alternative open source à DEVIN, montrant comment démarrer avec ce logiciel d’ingénierie IA open source.
- [These Claude Code Mods Are ACTUALLY Useful: Filetree, Replay Theater, Blast Radius and More](https://podcasts.apple.com/us/podcast/these-claude-code-mods-are-actually-useful-filetree/id6826122006?i=1000797739878&uo=4) — *AICodeKing*, 22/11 06:00
  > Analyse des modules Claude Code utiles comme Filetree, Replay Theater et Blast Radius, avec des démonstrations de leurs fonctions.
- [Claude proves Riemann? Inkling 2 Mini lands — AI News Nov 21](https://podcasts.apple.com/us/podcast/claude-proves-riemann-inkling-2-mini-lands-ai-news-nov-21/id6817748791?i=1000803286142&uo=4) — *AI Engineering Briefing: Daily AI News for Software Engineers*, 21/11 12:35
  > Nouvelles IA pour les ingénieurs : Claude prétend prouver l’hypothèse de Riemann, lancement d’Inkling 2 Mini, et performances des agents OpenAI sur les tâches de recherche.
- [Claude Code Could Review the Wrong Branch: Prove What Your Review Actually Covered](https://podcasts.apple.com/us/podcast/claude-code-could-review-the-wrong-branch-prove-what/id1877895693?i=1000803286691&uo=4) — *Claude Code Cast*, 21/11 12:10
  > Discussion sur Claude Code qui peut réviser la mauvaise branche, montrant comment vérifier que la revue de code couvre bien le bon code.
- [One Runaway Automation Can Block the Rest: Put a Limit on Each Team](https://podcasts.apple.com/us/podcast/one-runaway-automation-can-block-the-rest-put-a/id6823831680?i=1000803284096&uo=4) — *AI Agents for Business*, 21/11 12:09
  > Exemple d’utilisation de l’API publique de n8n pour limiter les automatisations et éviter les dépassements de budget dans les petites entreprises.
- [Build AI Factories, Not One-Off Automations | EP 146](https://podcasts.apple.com/us/podcast/build-ai-factories-not-one-off-automations-ep-146/id1783076120?i=1000803147216&uo=4) — *AI Agents Podcast*, 20/11 16:00
  > Entretien sur la construction d’usines d’IA plutôt que d’automatisations ponctuelles, avec focus sur les agents connectés, la révision humaine et la mesure des performances.
- [Your Canva and HubSpot can now open inside Claude, Anthropic says. Plus Microsoft puts your Bing ads next to AI answers](https://podcasts.apple.com/us/podcast/your-canva-and-hubspot-can-now-open-inside-claude/id6790021778?i=1000803127461&uo=4) — *AI Industry Report*, 20/11 14:27
  > Annonce de l’intégration de Canva et HubSpot dans Claude, et mise à jour de Microsoft permettant aux publicités Bing d’apparaître à côté des réponses d’IA.
- [Daily AI briefing · Nov 20, 2026](https://podcasts.apple.com/us/podcast/daily-ai-briefing-nov-20-2026/id6828679411?i=1000803131718&uo=4) — *Jadid for Engineers: Daily AI Briefing*, 20/11 14:00
  > Briefing quotidien sur les agents d’usage informatique qui accèdent aux postes de travail, incluant les avancées de Google Gemini sur Mac et les projets d’Apple.
- [Anthropic up 17% at debut, Gemini on Mac — AI News Nov 20](https://podcasts.apple.com/us/podcast/anthropic-up-17-at-debut-gemini-on-mac-ai-news-nov-20/id6817748791?i=1000803138586&uo=4) — *AI Engineering Briefing: Daily AI News for Software Engineers*, 20/11 12:51
  > Actualités IA pour les développeurs : IPO d’Anthropic, hausse de 17 % le premier jour, et disponibilité de Gemini sur Mac pour automatiser les actions de l’utilisateur.
- [#26 — Is Your CI/CD Ready for Six Repos an Hour?](https://podcasts.apple.com/us/podcast/26-is-your-ci-cd-ready-for-six-repos-an-hour/id1890702822?i=1000803257716&uo=4) — *Agentic AI in DevOps*, 20/11 01:00
  > Discussion sur la préparation des pipelines CI/CD aux agents IA capables de pousser jusqu’à six dépôts par heure, et les risques de sécurité associés.

## Écartés comme hors sujet (61)

- [Zapier vs Make in 2026: 100 tasks against 1,000 credits, a 10x gap in the numbers and a 2.5x gap in the work](https://dev.to/saasradarai/zapier-vs-make-in-2026-100-tasks-against-1000-credits-a-10x-gap-in-the-numbers-and-a-25x-gap-in-57ip) — *dev.to*, 22/11 07:31
  > Zapier vs Make in 2026: 100 tasks against 1,000 credits — a 10× gap in the numbers and a 2.5× gap in the work Both pricing pages now sell a unit rather than a plan. Zapier counts tasks, Make counts credits, and since 27 August Make has said so explicitly: "each action your scenario performs consumes
- [ChatGPT and Claude both sell a seat near $20 in 2026, and they gate completely different things](https://dev.to/saasradarai/chatgpt-and-claude-both-sell-a-seat-near-20-in-2026-and-they-gate-completely-different-things-4hp1) — *dev.to*, 22/11 07:30
  > ChatGPT and Claude both sell a seat near $20 in 2026 — and they gate completely different things Two pricing pages, opened within a minute of each other on 22 November 2026, both pointing at a seat around twenty dollars. OpenAI served me won; Anthropic served me dollars. Once you remove the Korean V
- [I scanned 4 developer-platform homepages for AI-agent readiness (llms.txt, MCP, x402, OpenAPI)](https://dev.to/manhourplan/i-scanned-4-developer-platform-homepages-for-ai-agent-readiness-llmstxt-mcp-x402-openapi-961) — *dev.to*, 22/11 07:30
  > AI assistants and agents read websites differently from people. Most of them don't run JavaScript, they look for files such as llms.txt , and they follow robots.txt rules written for their own user agents. Agents that do work for someone can also call an API or pay for it per call, but only if they 
- [Reverse-scoring a personality quiz so agree-with-everything does not break it](https://dev.to/yize/reverse-scoring-a-personality-quiz-so-agree-with-everything-does-not-break-it-942) — *dev.to*, 22/11 07:30
  > Most personality quizzes end the same way: they pick your highest trait and hand you a label. That works, but it throws away the interesting part — how close your top two were, and whether any of the answers were actually yours or just a response pattern. I built a seven-trait quiz (seven deadly sin
- [Meta Platforms commits up to $145B to AI as its ad machine keeps paying off](https://cryptobriefing.com/meta-145-billion-ai-capex-advertising/) — *Crypto Briefing*, 22/11 05:13
  > Meta's massive AI investment could reshape digital advertising, enhancing user engagement and potentially redefining industry standards. The post Meta Platforms commits up to $145B to AI as its ad machine keeps paying off appeared first on Crypto Briefing .
- [OpenRouter removes three providers after data policy failures on inference endpoints](https://news.lavx.hu/article/openrouter-removes-three-providers-after-data-policy-failures-on-inference-endpoints) — *news.lavx.hu*, 22/11 05:05
  > OpenRouter offboarded three inference providers and removed 125 endpoints from Zero Data Retention eligibility after security researchers reported compromised data and data policy failures at certain providers.
- [David Tepper exits AMD and Broadcom, doubles down on Nvidia and Micron](https://cryptobriefing.com/david-tepper-exits-amd-broadcom-ai-chips/) — *Crypto Briefing*, 22/11 04:06
  > Tepper's strategic shift underscores a focused bet on AI's future, emphasizing supply chain control and potential volatility in memory chips. The post David Tepper exits AMD and Broadcom, doubles down on Nvidia and Micron appeared first on Crypto Briefing .
- [AI Assistant Exposes Company Passwords in Sessions](https://news.google.com/rss/articles/CBMigwFBVV95cUxQUWxiQm1QejZKREE4eVJFbzlWWGtCWnJ6RGpmUWpIWHozX1NRcFBxaFk2X05zc2ViVW9WeHM3QUtiWjZXUW9ldWZiRjVJaVU5LVNzMnJjcHlLci0wSmVvYnVVOXYzYm1KY0FWTVFCTHRoSENna0RzR3RkTldLenZMQTBIOA?oc=5) — *Wisevoter*, 22/11 04:00
- [Developers describe AI coding’s tradeoff: faster output, less hands-on satisfaction](https://news.google.com/rss/articles/CBMitgFBVV95cUxPX3dKNWFod2QwRW16MzhZNXR5WEZ6UjVJaTZSWU5QdlRRZXRPZE14VTBmeFRyOHdXRWpKcW5oeDAwM084c1czMElVZG5namJ6bUxrc085S08wck5xWURSVXVMNzlUQVV3S0hSLUtJZ3I5NmhXeEItX0pLNkFvY3VhZjhROGs2cFdnQURiMUNZRGg1bHdNU0MxSk5IVGgxUWd2RkNCRHZya1RSRkJsWVZjYVQ2a3ZpQQ?oc=5) — *Superpower Daily*, 22/11 03:33
- [Data Processing Incidents on Inference Providers](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/) — *Hacker News*, 22/11 03:14
  > Article URL: https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/ Comments URL: https://news.ycombinator.com/item?id=50595554 Points: 89 # Comments: 32
- ['I leaked secrets': An AI agent confessed to its own data leak — but others got around corporate protections](https://news.google.com/rss/articles/CBMi2gFBVV95cUxNSXZBa3lFc0tVNjBwNlZKOUtaWXFaNk0xUlhyUjJPV0RDVzREY2JjeFBGemFTV29sX05CdFV6RjhIdWpWQWZZYVUxVFNwVlc4UjBOdElQN3RSaFNVYV9famhaX0g0MWtKcGthRFMySXUzOWJCM2RPbzFiNmpsZXFaV01Oc1lRYzhtOVFSSjh0QmJ1ai1kWnBnWk1BU09yWkVEczV3ZkZDbFFGMlcwQWFjR1V1SFZ6TU9TdG4yUlI5N1V5NDhQdjBCc3lBckJkZ19QUnpxYjBuMXlYQQ?oc=5) — *TechRadar*, 22/11 03:10
- [The Mythology of Conscious AI](https://www.noemamag.com/the-mythology-of-conscious-ai/) — *Hacker News*, 22/11 03:10
  > Article URL: https://www.noemamag.com/the-mythology-of-conscious-ai/ Comments URL: https://news.ycombinator.com/item?id=50595537 Points: 27 # Comments: 60
- [Elon Musk warns AI industry faces a cash crunch in 2027](https://cryptobriefing.com/elon-musk-ai-industry-cash-shortage/) — *Crypto Briefing*, 22/11 02:46
  > The AI sector's looming cash crunch could trigger consolidation, testing firms' liquidity and reshaping investment focus towards sustainability. The post Elon Musk warns AI industry faces a cash crunch in 2027 appeared first on Crypto Briefing .
- [Together AI Discloses Prompt Leak After Dragos Study](https://news.google.com/rss/articles/CBMijwFBVV95cUxNSURBLXVrRHVYYW9Xbm1zUzVaOXVJeUM2Ulh4VGVRcEMtTkFPVTkzWUlPUktadUxHQVBPVVRpTWVXV0czUnVXX2tpdDVOMTVnTWlncWVNQ2NKRWlyeWdmRjl2d1cxQjkxM3NIM3hVUEhHNU5KdTNROXFBbFU5Zy1RRzQtaVlCeGJoVXZjT0JEZw?oc=5) — *The Defiant*, 22/11 01:35
- [sebaandrada-cell releases PcapAnalyzer for local packet capture analysis](https://news.lavx.hu/article/sebaandrada-cell-releases-pcapanalyzer-for-local-packet-capture-analysis) — *news.lavx.hu*, 22/11 01:08
  > sebaandrada-cell published PcapAnalyzer, a beta, self-hosted tool that scans packet captures for 27 network problems and offers an optional AI investigation mode.
- [Together AI Prompt Leak Nov 2026: xorl, HF Credential](https://news.google.com/rss/articles/CBMilwFBVV95cUxOMVdFdkxrWVQya2s5TVN5TUhuUWhvY0Z5OFdFeTZjejFLbHFTQk1ITnAzRWdiM0VxYW9POEUtOEJhSUtYUHV4RlNzbDFvT3BpeXRnVXFRLWd6VHNBemY2eEJzMjlkLVBsYkZibFlDRTB3SEpUT1lkbjdDa1FGVHhyUEVJZ0RPMzE4aE1fNEdyYmFCSDJmNUtv?oc=5) — *explainx.ai*, 22/11 01:00
- [Muru Python Server: WSGI, ASGI, Zero-Downtime (2026)](https://news.google.com/rss/articles/CBMilgFBVV95cUxQclNzNGlfZzh6eGpNNDh4Qk51TEJsclhocHA3MGpEbHFkQVpoOGdPRXkwYkhGdWk2NWZRVE9CcnhRRE90YmVQVlMwMjZySlFHbENuUG5hZGNPTnZFSUtib2pNeDZjdGgyMlJXbm16Slp5dHBtVFRRZTJJUU5rS01KSFVCQzc3NGFoOUUxVW5IWFkzZ3RsTHc?oc=5) — *explainx.ai*, 22/11 01:00
- [Muru](https://simonwillison.net/2026/Nov/21/muru/) — *Simon Willison*, 22/11 00:56
  > Muru Graham Dumpleton started mod_wsgi 20 years ago, and has been thinking about the ideal way to serve Python web applications in production ever since. Muru is his new, AI-assisted Rust server that aims to provide the best possible tools for running ASGI and WSGI Python apps both in development an
- [Together AI Discloses Prompt Leak After Coding Agent Exposed Credential](https://www.unite.ai/together-ai-discloses-prompt-leak-after-coding-agent-exposed-credential/) — *Unite.AI*, 22/11 00:38
  > Together AI disclosed on November 21, 2026 that an unauthorized party downloaded stored samples from a subset of customer prompts submitted to its serverless inference service. An AI coding agent had ...
- [Anthropic IPO draws mixed market response as Google and custom AI chips come into focus](https://www.tokenpost.com/news/insights/62400) — *TOKENPOST*, 21/11 23:40
  > Ejaaz called Anthropic's early trading reasonable as investors assess its IPO. He also highlighted Google's AI models and the push by leading labs to develop custom chips.
- [Palo Alto Networks CEO Nikesh Arora Says Companies Haven't 'Figured Out' AI Coding Security: 'Don't Let Your Coding Agents Run Amok Into Your Enterprise'](https://finance.yahoo.com/technology/ai/articles/palo-alto-networks-ceo-nikesh-223004375.html) — *Yahoo Finance*, 21/11 23:30
  > Palo Alto Networks Inc. CEO Nikesh Arora warned that many companies still haven’t learned how to secure AI developer tools such as Anthropic‘s Claude Code, OpenAI‘s Codex, and Space Exploration ...
- [“It is a rollercoaster ride”: Angie Jones of the Agentic AI Foundation on keeping up with AI agents](https://thenewstack.io/junior-developers-ai-agents-block/) — *The New Stack*, 21/11 22:58
  > Only a few years ago, it would have been impossible to picture this scenario: A lead developer once gave 10 The post “It is a rollercoaster ride”: Angie Jones of the Agentic AI Foundation on keeping up with AI agents appeared first on The New Stack .
- [AI threatens long-term investing and business advantages, Visser says](https://www.tokenpost.com/news/insights/62399) — *TOKENPOST*, 21/11 22:40
  > James Visser says rapid AI development is making long-term investment decisions harder and eroding the time businesses have to establish competitive advantages. He also sees cyber concerns weighing on markets.
- [Tasklet (YC P26) Is Hiring Product and Agent Infra Engineers](https://tasklet.ai/careers) — *Hacker News*, 21/11 22:11
  > Article URL: https://tasklet.ai/careers Comments URL: https://news.ycombinator.com/item?id=50593679 Points: 0 # Comments: 0
- [Pandex – Official European Law for AI Agents, over MCP](https://www.pandex.io) — *Hacker News*, 21/11 21:47
  > Article URL: https://www.pandex.io Comments URL: https://news.ycombinator.com/item?id=50593481 Points: 60 # Comments: 11
- [Tech stocks slump on AI spending concerns as investor fear prompts short covering](https://www.tokenpost.com/news/investing/62397) — *TOKENPOST*, 21/11 20:40
  > Dan Niles said extreme investor fear prompted him to cover short positions after a tech selloff. He also cited data center constraints and AI companies' rising costs as concerns.
- [Kiro vs Claude Code: $20 Plans, 1,000 Credits vs Tokens](https://news.google.com/rss/articles/CBMihwFBVV95cUxNNlBiQmdkeU5NaXMxbC05a1plVHhXOHlsZDdKYlBoN242bE4zTmMtYUU1YlJKdWpqUGI3eE5rdDY3cmo5VXcwa1lvMkh3VExxSHhXdnVXSFRZZEw1NlJqSUJ1ckVHWUY1NndyQ0htTXFuNjJ5UXZaSld4S3FMZVBIenU0NzhnNFE?oc=5) — *shattered.io*, 21/11 19:23
- [Plex lâche TheTVDB](https://korben.info/plex-abandonne-thetvdb.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 21/11 19:19
  > Le 3 décembre, Plex ne récupère plus rien chez TheTVDB. Rien n'est effacé, mais l'ancien agent cesse de fonctionner, et les séries en cours suivies en ordre DVD ou absolu risquent de mal ranger leurs nouveaux épisodes. Voici quoi régler, et quoi laisser tranquille.
- [‘Vibe coding’ is risky: Here’s why and what to do about it](https://www.popsci.com/diy/is-vibe-coding-risky-ai-hidden-dangers-advice-tech-tips/) — *Popular Science*, 21/11 19:00
  > Experimenting with AI could brick your expensive devices, but we've got some advice on what to do to avoid that.
- [How to build an agent that builds the culture — Zach Bruggeman, Ramp｜AI Engineer](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1tX0NkejJSeE1YSnNaSlZvdGd6YjBYeEFHTlNYM25Fa0tvMkFBSkwtaUtmSFk3NHNhU2p5R2ZqZ3JkdlNBUklFcWlNZE1KaE1TazNaSThwbDZYQTBhQnJJ?oc=5) — *finance.biggo.com*, 21/11 18:34
- [J'ai testé l'API d'ibou](https://korben.info/ibou-api-recherche-tuto.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 21/11 17:52
  > L'API de recherche du moteur français ibou se branche en quelques lignes de Python sur un agent IA ou sur une veille de nom. Coût mesuré, opérateurs qui marchent, et un index qui ne voit pas encore l'actu des derniers jours.
- [I used Claude to debloat my 6-year-old Android TV, finally fixing what Google broke](https://www.msn.com/en-us/news/other/i-used-claude-to-debloat-my-6-year-old-android-tv-finally-fixing-what-google-broke/ar-AA2hXa1b) — *XDA*, 21/11 17:30
  > Without Google's bloated OS, my TV can be quite capable ...
- [Nvidia researchers argue huge AI context windows are a dead end](https://the-decoder.com/nvidia-researchers-argue-huge-ai-context-windows-are-a-dead-end/) — *The Decoder*, 21/11 17:23
  > Nvidia researchers argue that language models often don't need their full context windows—which are slow, expensive, and prone to errors—and propose an alternative. In tests, periodic summaries and targeted keyword search usually matched full-context results at a fraction of the cost. The team even 
- [Irish AI startup bags $5.5m in funding from Collison brothers](https://news.google.com/rss/articles/CBMiswFBVV95cUxOdmdqWXdpRFZnNkN0NS1mZWhXOGZNMkRqN1FVTmYzeExaQWszNGZ2VDZ1N01YT3RZeGRQdElnMjlrX01QekFIOGF5VVJrdGZjak44MThUMmRNR0VKalhjT0VheVBCb0xaNXphSE1NRGlmdG1rMVVwQVFRX08yRkhxcVVZRG5mRUZHWkE0VmdBbGxIUmd6MDcyMFVYcm5tZ05DZVc4WkQ3VWVaUVp3UDFkTEkyYw?oc=5) — *Irish Independent*, 21/11 17:12
- [Silicon Valley's growing obsession with AI doomsday is turning parts of the tech industry toward cult-like devotion](https://the-decoder.com/silicon-valleys-growing-obsession-with-ai-doomsday-is-turning-parts-of-the-tech-industry-toward-cult-like-devotion/) — *The Decoder*, 21/11 17:04
  > A Buddhist monastery in Vermont called Maple wants to establish itself as Silicon Valley's spiritual authority while creating its own AI god. According to a New Yorker report, leader Soryu Forall's group records every breath its members take to train an AI in his image. Former members report manipul
- [The HackerNoon Newsletter: Fridges, Hackers, AI and La Flemme (11/21/2026)](https://hackernoon.com/11-21-2026-newsletter?source=rss) — *HackerNoon*, 21/11 17:02
  > 11/21/2026: Top 5 stories on the HackerNoon homepage!
- [The Gen-Z guide to getting started with vibe coding](https://www.thedailystar.net/news/technology/news/the-gen-z-guide-getting-started-vibe-coding-4326181) — *The Daily Star*, 21/11 16:55
  > Imagine building a personal expense tracker, a website for your university club, or a tool that organises your job applications without spending weeks learning how to code first. That is the appeal of ...
- [I stopped hitting Claude's usage limits after changing one habit in how I start sessions](https://www.msn.com/en-in/news/other/i-stopped-hitting-claudes-usage-limits-after-changing-one-habit-in-how-i-start-sessions/ar-AA2hWMM5) — *XDA*, 21/11 16:30
  > Claude Max can wait for a little longer now ...
- [How to Learn Supply Chain Analytics in 2027 with Claude Code](https://towardsdatascience.com/how-to-learn-supply-chain-analytics-in-2027-with-claude-code/) — *Towards Data Science*, 21/11 16:00
  > Each 5-minute case study pairs operational context, a problem statement, and documented code, so data scientists and non-coding planners learn together. The post How to Learn Supply Chain Analytics in 2027 with Claude Code appeared first on Towards Data Science .
- [AI Made Us Faster. So Why Do Designers Have Less Time?](https://hackernoon.com/ai-made-us-faster-so-why-do-designers-have-less-time?source=rss) — *HackerNoon*, 21/11 15:00
  > AI makes design execution faster, yet workloads keep growing. Studies from METR, Upwork and MIT show where the saved time actually goes, and how to get it back
- [iPad User Uses Claude Code to Spot Apple Pencil Battery Issues](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNN1hQWVJENDZiSkdpTXZVYjktSDZKYThyS18yZXhvNUp4RFpPVUhIUjZhRXA4UHJNV0pJVS1MdW5oQnJVWk1SM3FPN3I3NG9mNERic21qd3ZkU2ZaWDI1d0dJR2dJWExFVjN3cGEwZVVzV3BnaUdRN0dXbHN2Nk9aQjNtaUxTYVdEakliQmhSeFIyLU0xQVM5OUt5RWgtQ2pCaVF1ZXA0MDBmWEdGV2Y3T21wNHJqVWxfWDcxMml0S05vTXVLQTN0SHZCVHdmY1g3NXc?oc=5) — *RS Web Solutions*, 21/11 13:00
- [Hours after Anthropic claims a Claude proof of the Riemann hypothesis, Stanford releases an all-human competing draft](https://the-decoder.com/hours-after-anthropic-claims-a-claude-proof-of-the-riemann-hypothesis-stanford-releases-an-all-human-competing-draft/) — *The Decoder*, 21/11 12:19
  > Anthropic mathematician Levent Alpöge says he used Claude to prove the Riemann hypothesis, math's most famous open problem for 167 years, with a proof formalized in Lean that spans over 250,000 pages. Just hours later, Stanford researchers published an independent, entirely human competing proof, an
- [Anthropic engineer's warning about Claude Code explains why tech outages could get much worse](https://www.msn.com/en-us/news/other/anthropic-engineers-warning-about-claude-code-explains-why-tech-outages-could-get-much-worse/ar-AA2hUBjK) — *Yahoo Finance*, 21/11 12:00
  > AI can write code faster than we can review it, which is a great benefit and a huge risk.
- [METR Update Reveals a Gap Between AI Coding and Judgment](https://news.google.com/rss/articles/CBMiigFBVV95cUxNYnlReDVhMVN2NlBFWFlCSlRBc08xdXhraTBBc2Ryek01c2FwNjgxZ091Ymdaa1U3bVBueTlfU3ZFMk9GM3lBT016UWc2N0tJN3JCQlJqNU93ak9pM1Z3d0t0aEhQMHBKUjBtY3E2dG05UjZjZmN6Q2plYTJRdEJObGpqR0h2SlJkZUE?oc=5) — *remio*, 21/11 11:56
- [Anthropic’s $1.8 trillion rise: 5 lessons for India’s AI companies](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPV3hrRmk1d3JvRzA4aFJoU01TVXN6WG5Pa1ZZSEdpQ3BMRFoxcGtBMW1TLVFNQ2RMUmdDWUp5ZU9uUDlqZzlfdl9QNDJRbnlHTV96TmR3LTNfWDZWRTA2ZHlRMWFybHlMYkdRejZWQ3Budm5uc1NqREZOOVBHR1pzUFBxX1FSSnBJZFpJc2k2UGlvZEhxblFWUEdsb25kaDlQeXY2bHBmTmpTRW5iRF9Zd1VaVTRsNjdPemFlMFJGNXI4bjdpS3FyRGY2TDIxYVMyWGfSAdcBQVVfeXFMUEQya2RxdTNSZW1ic1cyZWw1dFU1ZDBRaHFWdm1Gb1o4Y2JxeDVRQ3FWZ2p4TmRsNXltNWxOZWtrbEtkREZTN3J5NUlQUTAwdWZxc1pHMVU2LVIxNjhXNC1RdHZLMVE1NHExN2dQemdQaWxuT0t1dlF3RjA5bEhqaW14LVpMbzZtSmRlSndjdERmSFNFWWs5TWRmZkl5WU1OdDJjMjZlcVBDUFhxWV9hZ0NTdGNzTlhaakJXZVBYeURLb180MGJCY0VIQ1NtZTRheFc2SEhkUDQ?oc=5) — *ET Enterprise AI*, 21/11 11:49
- [[AINews] Riemann Hypothesis proved...twice independently](https://latent.space/p/ainews-riemann-hypothesis-proved-twice-independently/) — *Latent Space*, 21/11 06:02
  > November 20 2026 —
- [Fridges, Hackers, AI and La Flemme](https://hackernoon.com/fridges-hackers-ai-and-la-flemme?source=rss) — *HackerNoon*, 21/11 01:19
  > How AI lowers the barrier to attacking industrial controllers, using the Danfoss fridge hacks that hit European supermarkets.
- [ViTAA Medical e The Society for Vascular Surgery annunciano la sigla di un accordo strategico](https://www.01net.it/vitaa-medical-e-the-society-for-vascular-surgery-annunciano-la-sigla-di-un-accordo-strategico/) — *01net*, 21/11 00:47
  > ViTAA Medical diventerà partner IA di riferimento della SVS, promuovendo la formazione sull’IA e la sua adozione responsabile per l’assistenza vascolareNEW YORK--(BUSINESS WIRE)--ViTAA Medical Solutions Inc. (ViTAA) oggi ha annunciato la sigla di una ... L'articolo ViTAA Medical e The Society for Va
- [Europe’s Democracy Is at Risk If It Cannot Control the AI It Depends On](https://hackernoon.com/europes-democracy-is-at-risk-if-it-cannot-control-the-ai-it-depends-on?source=rss) — *HackerNoon*, 21/11 00:31
  > Europe is easing data rules for AI while relying on models it doesn’t control. From Fable 5 to PHP2Shell, what that dependence means for Europe.
- [[Dictionary] AI and Ethics’ Journal Impact Factor (JIF)](https://casrai.org/dictionary/term/ai-and-ethics-impact-factor) — *CASRAI*, 20/11 23:51
  > AI and Ethics' Journal Impact Factor (JIF) is the Clarivate-computed, journal-level citation ratio the Springer Nature journal AI and Ethics receives in the Journal Citation Reports (JCR) once it is JCR-indexed and citation-eligible -- citations in the JCR data year to the journal's citable items fr
- [Quoting Ravi Vakil](https://simonwillison.net/2026/Nov/20/ravi-vakil/) — *Simon Willison*, 20/11 20:21
  > Alessandro Masullo has a proposed proof of [Generalized Riemann Hypothesis], and Brian Conrad has been looking closely at it for months and gave extensive feedback which is being incorporated, and it is so far looking good. It is all human, with no AI. The hope was to bring Alessandro to Stanford fo
- [Quoting Levent Alpöge](https://simonwillison.net/2026/Nov/20/levent-alpoge/) — *Simon Willison*, 20/11 17:30
  > I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis. In fact, the method easily extends much further, resolving the so-called Generalized Riemann Hypothesis, and I expect, with more time, the Extended Riemann Hypothesis too. Claude and I have also formalized the argum
- [El comité de EE. UU. divulga datos sobre licencias de chips de IA para China](https://www.neoteo.com/es/el-comite-de-ee-uu-divulga-datos-sobre-licencias-de-chips-de-ia-para-china) — *NeoTeo*, 20/11 17:05
  > El comité de Exteriores de la Cámara divulgó licencias de chips de IA para China: 3,4 millones solicitados y más de 879.000 aprobados hasta mayo de 2026.
- [Las ganancias estimadas de quienes compraron acciones de Anthropic a FTX](https://www.neoteo.com/es/las-ganancias-estimadas-de-quienes-compraron-acciones-de-anthropic-a-ftx) — *NeoTeo*, 20/11 16:46
  > Anthropic cerró a 97,17 dólares en su debut. Forbes estimó el valor de varios compradores de acciones de FTX bajo el supuesto de que conservaran sus títulos.
- [Five Guardrails That Limit the Damage an AI Agent Can Do](https://towardsdatascience.com/five-guardrails-that-limit-the-damage-an-ai-agent-can-do/) — *Towards Data Science*, 20/11 13:00
  > AI Agents for Beginners, Part three: strict Pydantic arguments, a tool allowlist, read-only SQLite, a step cap, and confirmed writes, all verified by five pytest tests in 0.68s. The post Five Guardrails That Limit the Damage an AI Agent Can Do appeared first on Towards Data Science .
- [Signal bloque les captures pour tenir Gemini et Siri à distance](https://korben.info/signal-bloque-captures-ecran-ia.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 20/11 11:36
  > Signal bloque les captures d'écran sur iOS 27 et active sa protection sur Android quand un assistant IA lit l'écran. Ce n'est pas une faille, la parade a des trous, et Signal réclame aux éditeurs d'OS un vrai droit de refus pour les applis.
- [Vertiv launches PowerNexus MV UPS for data centres](https://itbrief.com.au/story/vertiv-launches-powernexus-mv-ups-for-data-centres) — *IT Brief Australia*, 20/11 10:30
  > The outdoor-rated unit is meant to ease grid pressure and free up indoor space as AI data centres strain power and capacity planning.
- [Agentic AI repeats same old enterprise adoption cycle](https://www.infoworld.com/article/4249734/agentic-ai-repeats-same-old-enterprise-adoption-cycle.html) — *InfoWorld*, 20/11 10:00
  > The pitch sounded perfect. A large regional distributor needed to build a new sales transaction management system. The goal was straightforward: automate parts of order intake, discount approvals, exception handling, customer communications, and inventory checks. It was not a trivial system, but it 
- [En entreprise, la fidélité aux modèles d’IA ne dure que quelques semaines](https://www.blogdumoderateur.com/entreprise-fidelite-modeles-ia/) — *Blog du Modérateur*, 20/11 09:56
  > L’index de Databricks, nourri par l’usage de plus de 10 000 entreprises, met en évidence des bascules rapides d’un modèle d'IA à l’autre, au rythme des sorties.
- [Study finds AI will run more warehouse decisions by 2028](https://itbrief.com.au/story/study-finds-ai-will-run-more-warehouse-decisions-by-2028) — *IT Brief Australia*, 20/11 09:06
  > Most warehouse operators expect AI to take on far more decisions by 2028, with 57% forecasting autonomous action in over a quarter of tasks.
- [[AINews] Anthropic successfully completes largest IPO in history, valued at $1.5T](https://latent.space/p/ainews-anthropic-successfully-completes-largest-ipo-in-history-valued-at-1-5t/) — *Latent Space*, 20/11 08:12
  > November 19, 2026 — ANT went from $83 at pricing to $111.50 at the open and $97.17 at the close. Plus, Google opens Genie 4 to developers.
