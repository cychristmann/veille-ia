# Veille IA outils & code du 26/11/2026

50 articles de médias tech anglophones et francophones (blogs d'outils, Hacker News, Product Hunt) publiés ces 48 dernières heures (rapport généré à 09:14).

## Synthèse du jour

Cette veille met en avant une activité soutenue autour des agents IA, tant au niveau de la gestion de leur mémoire que de l’ajout de compétences spécialisées. Le déploiement de modèles évolue avec des services d’entraînement prédictif, des intégrations système comme le launcher Ubuntu et des migrations d’API vers Rust pour plus de stabilité. La sécurité et le debugging restent prioritaires, illustrés par les nombreux "traps" et outils de test d’Anthropic ainsi que par la gestion des secrets dans les environnements Docker. Enfin, les développeurs bénéficient de nouvelles plateformes et benchmarks visant à améliorer la productivité et à prévenir la dette technique liée au code généré par l’IA.

*Vérifiée : chaque affirmation est appuyée par au moins un titre.*

## À lire en priorité

- [Récapitulatif de Microsoft Ignite 2026 : Copilot comme OS de travail et gouvernance des agents](https://www.infoq.com/news/2026/11/microsoft-ignite-2026-recap/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 26/11 07:45 · **9/10** (Microsoft Ignite, Copilot OS et gouvernance agents, impact majeur)
  *Titre original : Recap of Microsoft Ignite 2026: Copilot as the Work OS and Agent Governance*
  > At Ignite 2026, Microsoft positioned Copilot as the operating system for work and extended agent identity, governance, and cost controls across Azure, Foundry, Entra, and Defender. Highlights include Cobalt 200 VMs, Azure HorizonDB, a continuous improvement loop in Foundry, Microsoft IQ, a standalon
- [Gemini Robotics 2.5 de DeepMind vise à rendre les robots plus sûrs, plus habiles et plus rapides à apprendre](https://www.infoq.com/news/2026/11/deepmind-gemini-robotics-2-5/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 25/11 18:00 · **9/10** (DeepMind Gemini Robotics 2.5, avancée robotique majeure)
  *Titre original : DeepMind's Gemini Robotics 2.5 Aims to Make Robots Safer, More Dexterous, and Faster Learners*
  > Google DeepMind introduced Gemini Robotics 2.5, a vision-language-action (VLA) model designed to improve robots' dexterity, reliability, and learning speed, while enabling safer operation in unstructured real-world environments. By Sergio De Simone
- [Les serveurs MCP peuvent désormais fournir des compétences d’agents IA, modifiant les critères d’approbation des entreprises](https://venturebeat.com/technology/mcp-servers-can-now-deliver-ai-agent-skills-changing-what-companies-approve-when-they-connect-one) — *VentureBeat*, 26/11 00:04 · **8/10** (MCP serveurs livrent compétences agents, changement d'architecture important)
  *Titre original : MCP servers can now deliver AI agent skills, changing what companies approve when they connect one*
  > Skills over MCP, in beta in Claude and Claude Code, lets MCP servers ship workflow instructions with their tools, so connecting a server means approving both.
- [Cisco et OpenAI déploient des agents IA pour protéger les systèmes vulnérables avant l’arrivée des correctifs permanents](https://www.infoworld.com/article/4252807/cisco-and-openai-dispatch-ai-agents-to-shield-vulnerable-systems-before-permanent-patches-arrive.html) — *InfoWorld*, 25/11 04:59 · **8/10** (Cisco + OpenAI agents pré‑patch, usage réel de défense automatisée)
  *Titre original : Cisco and OpenAI dispatch AI agents to shield vulnerable systems before permanent patches arrive*
  > Autonomous AI agents are rapidly and dramatically transforming the cybersecurity landscape for both defenders and adversaries. In hopes of giving security teams a head start and pitting machine against machine, Cisco and OpenAI have released a new open source project, dubbed Shirudo (Japanese for “s
- [OpenAI et Cisco publient Shirudo : un runtime Linux open source permettant aux agents de défendre les systèmes sans interruption](https://www.marktechpost.com/2026/11/24/openai-cisco-shirudo-ebpf-linux-runtime/) — *MarkTechPost*, 24/11 15:16 · **8/10** (Shirudo runtime open‑source, agents défense système sans downtime)
  *Titre original : OpenAI and Cisco Releases Shirudo: An Open-Source Linux Runtime Allowing Agents to Defend Systems Without Downtime*
  > OpenAI and Cisco released Shirudo, a pre-release, BSD-licensed eBPF runtime for Linux. AI agents write signed "shields" that block exploit paths on running systems while teams test and roll out real patches. The post OpenAI and Cisco Releases Shirudo: An Open-Source Linux Runtime Allowing Agents to 

## Agents IA et mémoire (16)

Les articles explorent les différents types de mémoire des agents IA, les expériences de mise en place d’agents autonomes dans une société SaaS, la cohérence de personnages dans les vidéos générées, ainsi que l’intégration de compétences spécifiques dans Claude et la gouvernance des agents.

- [Gemini Robotics 2.5 de DeepMind vise à rendre les robots plus sûrs, plus habiles et plus rapides à apprendre](https://www.infoq.com/news/2026/11/deepmind-gemini-robotics-2-5/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 25/11 18:00 · **9/10** (DeepMind Gemini Robotics 2.5, avancée robotique majeure)
  *Titre original : DeepMind's Gemini Robotics 2.5 Aims to Make Robots Safer, More Dexterous, and Faster Learners*
  > Google DeepMind introduced Gemini Robotics 2.5, a vision-language-action (VLA) model designed to improve robots' dexterity, reliability, and learning speed, while enabling safer operation in unstructured real-world environments. By Sergio De Simone
- [Les serveurs MCP peuvent désormais fournir des compétences d’agents IA, modifiant les critères d’approbation des entreprises](https://venturebeat.com/technology/mcp-servers-can-now-deliver-ai-agent-skills-changing-what-companies-approve-when-they-connect-one) — *VentureBeat*, 26/11 00:04 · **8/10** (MCP serveurs livrent compétences agents, changement d'architecture important)
  *Titre original : MCP servers can now deliver AI agent skills, changing what companies approve when they connect one*
  > Skills over MCP, in beta in Claude and Claude Code, lets MCP servers ship workflow instructions with their tools, so connecting a server means approving both.
- [Cisco et OpenAI déploient des agents IA pour protéger les systèmes vulnérables avant l’arrivée des correctifs permanents](https://www.infoworld.com/article/4252807/cisco-and-openai-dispatch-ai-agents-to-shield-vulnerable-systems-before-permanent-patches-arrive.html) — *InfoWorld*, 25/11 04:59 · **8/10** (Cisco + OpenAI agents pré‑patch, usage réel de défense automatisée)
  *Titre original : Cisco and OpenAI dispatch AI agents to shield vulnerable systems before permanent patches arrive*
  > Autonomous AI agents are rapidly and dramatically transforming the cybersecurity landscape for both defenders and adversaries. In hopes of giving security teams a head start and pitting machine against machine, Cisco and OpenAI have released a new open source project, dubbed Shirudo (Japanese for “s
- [Vercel lance Board expérimental pour coordonner tâches entre humains et agents de codage](https://www.infoq.com/news/2026/11/vercel-board-agents/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 25/11 14:57 · **7/10** (Vercel Board pour coordonner humains et agents, outil collaboratif notable)
  *Titre original : Vercel Launched Experimental Board to Coordinate Tasks Across Humans and Coding Agents*
  > Vercel's experimental Board is a headless message store where people and coding agents claim leased tasks, declare dependencies, and sync threads with Slack, GitHub, and Linear. By Daniel Dominguez
- [Jusqu’où les scientifiques tracent-ils la limite avec les agents IA ?](https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents) — *Hugging Face*, 25/11 19:52 · **6/10** (Débat scientifique sur limites agents IA, pertinence pour chercheurs)
  *Titre original : Where scientists draw the line on AI agents*
- [Nous avons laissé des agents IA gérer une société SaaS IA. Voici le résultat.](https://dev.to/builditomi/we-let-ai-agents-run-an-ai-saas-company-heres-what-happened-4dph) — *dev.to*, 26/11 09:08 · **5/10** (Expérience concrète d'AI SaaS, utile mais limité à un cas)
  *Titre original : We let AI agents run an AI SaaS company. Here's what happened.*
  > We typed one sentence: "an AI that writes Amazon product listings for small sellers from one product photo." About a minute later we had a live company with sign-in, a database, a brand, pricing and legal pages. We call it ListingGenie AI, and it is a real page you can open: https://ceo.builditomi.c
- [Anthropic introduit les compétences sur MCP dans Claude en version bêta publique](https://news.google.com/rss/articles/CBMiW0FVX3lxTFBsQld1cm1Wcl9LX1pTcmFnVXZpbktGZFhGU2FIcjRZTXpnb0U4cExmS3Rvd3V6aUExZ193UU55eHVBRklIeTVQR3BiNllhUFNlZ3VDOWJpMDB4bDA?oc=5) — *www.tokenpost.com*, 26/11 04:51 · **5/10** (Beta Skills sur Claude, fonctionnalité nouvelle mais peu diffusée)
  *Titre original : Anthropic Brings Skills Over MCP to Claude in Public Beta*
- [Concevoir des flux de travail d’annulation de commande sûrs pour les agents IA](https://hackernoon.com/designing-safe-order-cancellation-workflows-for-ai-agents?source=rss) — *HackerNoon*, 25/11 18:27 · **5/10** (Guide conception flux annulation sécurisée pour agents IA)
  *Titre original : Designing Safe Order Cancellation Workflows for AI Agents*
  > What happens when an AI agent needs to cancel an order, modify a subscription, or process a refund? Explore the engineering challenges of agentic commerce.
- [Mellum 2.1 Instruct est disponible, offrant des réponses plus rapides pour les agents de codage](https://blog.jetbrains.com/ai/2026/11/mellum2-1-instruct-is-out-bringing-faster-answers-for-coding-agents/) — *JetBrains AI*, 25/11 12:00 · **5/10** (Mellum2.1 Instruct, améliore réponses agents de codage, version concrète)
  *Titre original : Mellum2.1 Instruct Is Out, Bringing Faster Answers for Coding Agents*
  > The faster sibling of Mellum2.1 Thinking, built for sub-agents, tool loops, and chat. In October, we released Mellum2.1 Thinking, an open 12B mixture-of-experts model with 2.5B active parameters, trained to work as a coding agent. Today, we are releasing its sibling, Mellum2.1 Instruct. It is built 
- [Comment planifier les nouvelles tentatives pour les flux de travail multi‑agents avant d’écrire le code](https://towardsdatascience.com/how-to-plan-retries-for-multi-agent-workflows-before-you-write-code/) — *Towards Data Science*, 24/11 14:30 · **5/10** (Guide planification retries workflows multi‑agents, pratique développeur)
  *Titre original : How to Plan Retries for Multi-Agent Workflows Before You Write Code*
  > A Mermaid blueprint, Python dataclasses, and a retryable flag decide when a failed agent tries again and when the task goes to a person. The post How to Plan Retries for Multi-Agent Workflows Before You Write Code appeared first on Towards Data Science .
- [4 types de mémoire pour agents IA : profil, épisode, cas, compétence](https://dev.to/bayu_nh88/4-types-of-ai-agent-memory-profile-episode-case-skill-1g5c) — *dev.to*, 26/11 09:09 · **4/10** (Article technique sur types de mémoire d'agents, peu d'impact large)
  *Titre original : 4 Types of AI Agent Memory: Profile, Episode, Case, Skill*
  > AI agents need more than access to information to handle tasks consistently. They need a way to remember useful details, connect past experiences, and apply what they have learned when a new situation comes up. A practical way to understand this process is to separate agent memory into four parts: p
- [Qwen sur matériel nu](https://github.com/alesha-pro/llm.asm/tree/main/02-baremetal-os) — *Hacker News*, 25/11 23:15 · **4/10** (Annonce Bare Metal Qwen, intérêt limité sans détails)
  *Titre original : Bare Metal Qwen*
  > Article URL: https://github.com/alesha-pro/llm.asm/tree/main/02-baremetal-os Comments URL: https://news.ycombinator.com/item?id=50648365 Points: 136 # Comments: 32
- [Un agent vocal indic avec CUGA](https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga) — *Hugging Face*, 25/11 11:22 · **4/10** (Agent vocal indic, projet de recherche limité)
  *Titre original : An Indic Voice Agent with CUGA*
- [Maintenir la cohérence d’un même personnage à travers de courts clips vidéo IA](https://dev.to/magi2notes/keeping-one-character-consistent-across-short-ai-video-clips-2o4h) — *dev.to*, 26/11 09:08 · **3/10** (Astuce vidéo, intérêt très niche)
  *Titre original : Keeping One Character Consistent Across Short AI Video Clips*
  > I've been making short AI video clips for a side project, and the problem that kept tripping me up was the character changing between shots. Hair colour drifts, the jacket changes, the face looks like a cousin rather than the same person. What helped most was starting from a reference image rather t
- [Version très courte de la vérification GRH Lean d’Anthropic](https://github.com/lsernau/grh-lean) — *Hacker News*, 25/11 22:48 · **3/10** (Version courte de vérification GRH, peu de portée)
  *Titre original : Much shorter version of GRH Lean verification from Anthropic*
  > Article URL: https://github.com/lsernau/grh-lean Comments URL: https://news.ycombinator.com/item?id=50648050 Points: 428 # Comments: 219
- [Le mode IA de Google se connecte à Wallet et Drive pour personnaliser ses réponses](https://www.blogdumoderateur.com/mode-ia-google-wallet-drive/) — *Blog du Modérateur*, 24/11 10:44 · **3/10** (Mode IA Google intégré Wallet/Drive, plus produit grand public que outil dev)
  *Titre original : Le Mode IA de Google se connecte à Wallet et Drive pour personnaliser ses réponses*
  > Le Mode IA de Google peut désormais consulter Google Wallet pour personnaliser ses réponses. Drive et l'application Gemini suivront dans les prochaines semaines.

## Déploiement et infrastructure de modèles (10)

Ces titres portent sur le lancement de services d’entraînement prédictif, la présentation de Copilot comme OS de travail, le fine‑tuning de Nemotron 3.5, le launcher IA d’Ubuntu, la réécriture de l’API Claude en Rust, et les évolutions de facturation de Copilot.

- [Récapitulatif de Microsoft Ignite 2026 : Copilot comme OS de travail et gouvernance des agents](https://www.infoq.com/news/2026/11/microsoft-ignite-2026-recap/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 26/11 07:45 · **9/10** (Microsoft Ignite, Copilot OS et gouvernance agents, impact majeur)
  *Titre original : Recap of Microsoft Ignite 2026: Copilot as the Work OS and Agent Governance*
  > At Ignite 2026, Microsoft positioned Copilot as the operating system for work and extended agent identity, governance, and cost controls across Azure, Foundry, Entra, and Defender. Highlights include Cobalt 200 VMs, Azure HorizonDB, a continuous improvement loop in Foundry, Microsoft IQ, a standalon
- [OpenAI et Cisco publient Shirudo : un runtime Linux open source permettant aux agents de défendre les systèmes sans interruption](https://www.marktechpost.com/2026/11/24/openai-cisco-shirudo-ebpf-linux-runtime/) — *MarkTechPost*, 24/11 15:16 · **8/10** (Shirudo runtime open‑source, agents défense système sans downtime)
  *Titre original : OpenAI and Cisco Releases Shirudo: An Open-Source Linux Runtime Allowing Agents to Defend Systems Without Downtime*
  > OpenAI and Cisco released Shirudo, a pre-release, BSD-licensed eBPF runtime for Linux. AI agents write signed "shields" that block exploit paths on running systems while teams test and roll out real patches. The post OpenAI and Cisco Releases Shirudo: An Open-Source Linux Runtime Allowing Agents to 
- [Extension de Nemotron 3.5 Parse : données ouvertes, affinement et inférence accélérée](https://huggingface.co/blog/nvidia/building-on-nemotron-35-parse-open-data-fine-tunin) — *Hugging Face*, 26/11 06:05 · **7/10** (Fine‑tuning Nemotron 3.5, avancée technique pertinente)
  *Titre original : Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference*
- [Comment l’équipe de Katelyn Lesse a reconstruit l’API de messages Claude d’Anthropic en Rust](https://news.lavx.hu/article/how-katelyn-lesse-s-team-rebuilt-anthropic-s-claude-messages-api-in-rust) — *news.lavx.hu*, 26/11 05:19 · **6/10** (Re‑implémentation API Claude en Rust, retour d'expérience concret)
  *Titre original : How Katelyn Lesse's Team Rebuilt Anthropic's Claude Messages API in Rust*
  > Katelyn Lesse, head of platform engineering at Anthropic, describes a five-month migration of the Claude Messages API from a Python monolith to Rust, with shadow traffic for verification and Claude agents for code review, on-call triage, and onboarding.
- [Anthropic affirme avoir migré son API Claude de Python vers Rust sans interruption](https://www.infoworld.com/article/4253460/anthropic-says-it-moved-its-claude-api-from-python-to-rust-with-no-downtime.html) — *InfoWorld*, 26/11 03:26 · **6/10** (Migration API Claude Python→Rust sans downtime, cas d'usage réel)
  *Titre original : Anthropic says it moved its Claude API from Python to Rust with no downtime*
  > When Anthropic decided to port its Messages API from Python to Rust, Claude wrote the code in about a week. But proving the new system worked as well as the old one, post-migration, was the real project. Anthropic engineers addressed this validation problem by turning the production Messages API its
- [Des chercheurs de ByteDance open‑source Laminar, un cadre d’apprentissage par renforcement asynchrone post‑entraînement](https://www.marktechpost.com/2026/11/24/bytedance-seed-laminar-async-rl-post-training-framework/) — *MarkTechPost*, 25/11 06:42 · **6/10** (Open‑source Laminar RL post‑training, cadre intéressant pour chercheurs)
  *Titre original : ByteDance Researchers Open-Sources Laminar, an Async Reinforcement Learning RL Post-Training Framework*
  > Laminar is an open-source asynchronous RL post-training framework from HKU and ByteDance Seed researchers. It decouples rollout, training and weight sync, and lifted Qwen3-Coder-30B-A3B to 52.2% on SWE-bench Verified. The post ByteDance Researchers Open-Sources Laminar, an Async Reinforcement Learni
- [Canonical dévoile un lanceur IA optionnel pour Ubuntu Desktop](https://news.lavx.hu/article/canonical-previews-an-opt-in-ai-launcher-for-ubuntu-desktop) — *news.lavx.hu*, 26/11 05:37 · **5/10** (Preview launcher AI pour Ubuntu, première implémentation pratique)
  *Titre original : Canonical previews an opt-in AI launcher for Ubuntu Desktop*
  > Didier Roche-Tolomelli of Canonical's Ubuntu Desktop team shared an early working version of an AI launcher that runs language models on the device. Canonical plans community testing in January.
- [ms-marco-MiniLM-L6-v2 atteint 55 M de téléchargements mensuels : 52 classificateurs et modèles de récupération classés](https://hackernoon.com/ms-marco-minilm-l6-v2-pulls-55m-downloads-a-month-52-rerankers-and-retrieval-models-ranked?source=rss) — *HackerNoon*, 25/11 19:15 · **4/10** (Stats de ms‑marco‑MiniLM, intéressant mais pas nouveauté)
  *Titre original : ms-marco-MiniLM-L6-v2 Pulls 55M Downloads a Month: 52 Rerankers and Retrieval Models Ranked*
  > 52 retrieval and reranker models from the TextModels directory, ranked by 30-day Hugging Face downloads, led by ms-marco-MiniLM-L6-v2.
- [Hill‑climbing Inkling 2 : inférence mini sur un RTX PRO 6000](https://huggingface.co/blog/inkling-2-mini-inference-hillclimb) — *Hugging Face*, 25/11 01:00 · **4/10** (Hill‑climbing Inkling 2 inference, benchmark matériel spécialisé)
  *Titre original : Hill-climbing Inkling 2 Mini inference on one RTX PRO 6000*
- [Epochal IA se lance avec 100 millions de dollars et un service d’entraînement IA prédictif](https://www.tokenpost.com/news/technology/62685) — *TOKENPOST*, 26/11 08:04 · **2/10** (Annonce financière, peu de nouveauté technique)
  *Titre original : Epochal AI Launches With $100 Million and Predictive AI Training Service*
  > The company’s first product offers access to more than 1 trillion historical web pages for training models to forecast future events.

## Outils de sécurité, test et debugging (11)

Les publications détaillent les « traps » d’Anthropic pour Claude, les tests Opus 5.6 dans Claude Code, le projet Claude BugHunter et les problèmes de secrets Docker liés à Claude Code, montrant un focus sur la fiabilité et la sécurité des modèles.

- [Anthropic a placé plus de 1 700 pièges dans Claude — les résultats sont à la fois rassurants et dérangeants](https://thenewstack.io/anthropic-siren-sandbox-escape/) — *The New Stack*, 25/11 20:45 · **6/10** (Analyse des 1 700 pièges Claude, insight technique intéressant)
  *Titre original : Anthropic set more than 1,700 traps for Claude — what it found is both reassuring and unsettling*
  > As coding agents take on longer-running engineering tasks, Anthropic is examining how models behave when their execution environments fail to The post Anthropic set more than 1,700 traps for Claude — what it found is both reassuring and unsettling appeared first on The New Stack .
- [Un deuxième juge LLM atteint 87,5 % de précision mais laisse 21 sur 33 cas aux humains](https://towardsdatascience.com/a-second-llm-judge-hit-875-precision-but-left-21-of-33-for-humans/) — *Towards Data Science*, 25/11 13:00 · **6/10** (Deuxième juge LLM avec 87,5 % précision, avancée évaluation modèles)
  *Titre original : A Second LLM Judge Hit 87.5% Precision but Left 21 of 33 for Humans*
  > Using Han and Kim's Chatbot Arena data, GPT-6 Luna and Claude Haiku 4.5 were tested as a panel, and Haiku alone matched users on 22 of 23 clear matchups. The post A Second LLM Judge Hit 87.5% Precision but Left 21 of 33 for Humans appeared first on Towards Data Science .
- [Claude Ship vise à résoudre le goulot d’étranglement de la revue de code](https://devops.com/claude-ship-takes-aim-at-the-code-review-bottleneck) — *DevOps.com*, 24/11 16:34 · **6/10** (Claude Ship cible goulet revue code, fonctionnalité concrète)
  *Titre original : Claude Ship Takes Aim at the Code Review Bottleneck*
  > AI coding agents solved one problem and created another. Developers can now generate code far faster than their teams can review it. The pull request queue has become the new constraint. Anthropic wants to move that constraint. This week, the company launched Claude Ship in beta, a set of agents tha
- [Qu’est‑ce que Claude BugHunter et comment l’utiliser pour tester votre propre application](https://news.google.com/rss/articles/CBMikwFBVV95cUxPSm1nX0ZDS1Ezd3R5T2VrV1VrbC0xS1JYczJ6eUttOVRscG8tS2FzVEpJTjRlVUhNb2NCNEZuSkxRUkxvLXVNalpWYnU5VUk3UVRHU1QxZUhNSU5YZzNsZS1lakFOSmNTSlR1Ul9qWXhXRWJOclJLaTVWZlNRZTRUT2JRcGtlYjVndEs5aFFkQjdFR0k?oc=5) — *Pasquale Pillitteri*, 25/11 17:56 · **5/10** (Guide d'utilisation de Claude BugHunter, pratique pour développeurs)
  *Titre original : What is Claude BugHunter and how to use it to test your own app*
- [Pourquoi les agents de codage IA ont besoin de tests plus intelligents](https://devops.com/why-ai-coding-agents-need-smarter-testing) — *DevOps.com*, 25/11 18:10 · **5/10** (Argumentation sur tests plus intelligents pour agents de codage)
  *Titre original : Why AI Coding Agents Need Smarter Testing*
  > CircleCI CTO Rob Zuber joins Alan Shimel to discuss earlier test feedback for AI coding agents, selective testing and confidence in software delivery.
- [Ne commettez aucune erreur : post‑mortems sans blâme à l’ère des agents](https://devops.com/make-no-mistakes-blameless-postmortems-in-an-age-of-agents) — *DevOps.com*, 25/11 12:16 · **5/10** (Post‑mortems blameless pour agents, bonnes pratiques opérationnelles)
  *Titre original : Make No Mistakes: Blameless Postmortems in an Age of Agents*
  > When an AI agent makes a catastrophic mistake, blaming the technology risks repeating a lesson software engineering learned decades ago. Applying blameless postmortems to agentic AI means investigating systemic vulnerabilities, enforcing architectural safeguards and designing environments where mist
- [Sept fonctionnalités clés des plateformes de gouvernance IA](https://www.infoworld.com/article/4251734/seven-key-features-of-ai-governance-platforms.html) — *InfoWorld*, 25/11 10:00 · **5/10** (Synthèse 7 features gouvernance IA, guide pratique)
  *Titre original : Seven key features of AI governance platforms*
  > Ask leaders what they prioritize in AI governance, and many will start by discussing employee policies and guidelines. Communicating AI guardrails, business objectives, and best practices to employees is important for balancing AI strategy with controls . But as pressure mounts to deliver AI busines
- [Anthropic teste Opus 5.6 à l’intérieur du code Claude](https://news.google.com/rss/articles/CBMiYkFVX3lxTFBQZ21CZi1yN0NrVWQ1dEoxSnlJUFVPdHphWlZBQk9TQllzZ0JhOU5nTG9vLTFDSzk3cUJuU29BVEdEMXk2OGUyWGh2YkRaMTVqM2JIbnQyTFV2MFNMN05XT3R3?oc=5) — *Demokratis.co.id*, 25/11 20:28 · **4/10** (Tests Opus 5.6, contenu très localisé)
  *Titre original : Anthropic Tests Opus 5.6 Inside Claude Code*
- [Secrets du fichier settings.local.json de Claude Code exposés sur Docker Hub](https://news.google.com/rss/articles/CBMidEFVX3lxTE40Qkk1c0cxQ1llaUhBaGNaQzhycVdBSk1PY1JCZWcxbVVBXzlSQXlla2hjT0VmSFVrV3E5SUJxcDRfYnlkQWdpQ2lLLWhwbW5ZZ3ZsbXRCd2VtekJsMzlST180VFpGdlZjRTZnX0tpTDdvSllK?oc=5) — *GitGuardian Blog*, 25/11 17:00 · **4/10** (Secrets Docker Hub, incident de sécurité limité)
  *Titre original : Claude Code settings.local.json Secrets Hit Docker Hub*
- [Comment évaluer les coûts des GitHub Actions face à la sécurité des runners](https://devops.com/how-to-weigh-github-actions-costs-against-runner-security) — *DevOps.com*, 25/11 12:09 · **4/10** (Analyse coûts GitHub Actions vs sécurité, utile mais générique)
  *Titre original : How to Weigh GitHub Actions Costs Against Runner Security*
  > As AI-assisted development drives up CI/CD workloads, engineering teams are under increasing pressure to reduce GitHub Actions costs. But choosing cheaper runners without accounting for security, isolation and operational overhead could turn short-term savings into expensive breaches.
- [Anthropic teste Opus 5.6 via le code Claude](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9nT21MN3FnQ0tuQ2JVblF4ME5TQUVfcTBqLUQ0OG01a0M1WlEyd00xTmxNdDNfRnJtallDQUk0T0FXX3lGcEE1QVlWMXpZY3pTOFJJTEtTSGdGRTZqUTZXbg?oc=5) — *SuaraGarut.ID*, 25/11 20:22 · **2/10** (Duplication d'article précédent, faible valeur ajoutée)
  *Titre original : Anthropic Tests Opus 5.6 Through Claude Code*

## Plateformes et productivité pour développeurs (12)

Cette catégorie regroupe les nouveaux outils présentés sur Product Hunt, le connecteur Model Context Protocol de Genetec, les benchmarks de JetBrains exposant les lacunes IA, et les pratiques d’audit du code généré avant qu’il ne devienne dette technique.

- [La facturation de la révision de code Copilot sera par défaut attribuée à l’organisation](https://github.blog/changelog/2026-11-25-copilot-code-review-billing-will-default-to-the-organization) — *GitHub Changelog*, 25/11 23:18 · **7/10** (Copilot code review billing, impact sur usage entreprise)
  *Titre original : Copilot code review billing will default to the organization*
  > If you haven’t chosen how to bill Copilot code review for members with a Copilot license, those reviews will be billed to your organization starting December 30, 2026. To keep… The post Copilot code review billing will default to the organization appeared first on The GitHub Blog .
- [Vibe coding passe en production : audit du code généré par IA avant qu’il ne devienne une dette technique](https://news.google.com/rss/articles/CBMiugFBVV95cUxNaWxDWG5uN3RSbzdOWXBVX09FeGY4WGhjS2FNMUtweXhnYWc5NlA2ek5WVmRtaGlKQm9LbVJOUFNKR21zUDZ3RHhIWFNHcVpaQWVOWGtGMDQ2Qjh2ME1RX3VTR0tHRlhkYUUwbE83cVFlblJSV1FvcW9QSkREdVBEbWhHQy1ESlkyMUFMeDhUWXFjcEdEZTVobi1NVFdPb2ZWWXJYeWxYRnYyS3NlTGFrSmNCR0VUVDBRbFE?oc=5) — *London Daily News*, 25/11 17:08 · **5/10** (Audit code IA avant dette technique, bon conseil opérationnel)
  *Titre original : Vibe coding meets production: Auditing AI-generated code before it becomes technical debt*
- [Superframes](https://www.producthunt.com/products/superframes-ai-video-editor) — *Product Hunt*, 26/11 06:09 · **4/10** (Nouveau produit Product Hunt, visibilité limitée)
  *Titre original : Superframes*
  > Brief an AI Director to edit the whole video Discussion | Link
- [JetBrains refait le benchmark qui met en lumière les lacunes du codage IA](https://news.google.com/rss/articles/CBMilAFBVV95cUxQNlczVmJzMVZtbWVRXzNNclI4NWlGSDktSVVlT1RyeVgyU04tRGFXcDV1ZV9VN2FDX0VJZ1BtQ2libWdaVk1YZ1J0cXgtMC13ZWFRdjNfb0I4VU9nc1RvVjY3ZDZzVktkcWN1WWpMNU5hTXBuRmR3RXNhLVBLbGhqeUlWckNINks0bC03T1lVNVNnVWND?oc=5) — *Wisevoter*, 25/11 16:33 · **4/10** (Benchmark JetBrains, expose gaps IA mais peu d'impact)
  *Titre original : JetBrains Revamps Benchmark Exposing AI Coding Gaps*
- [20 dépôts, 2 M d’étoiles : les outils open source de text mining qui lisent, récupèrent et enseignent](https://hackernoon.com/20-repos-2m-stars-the-open-source-text-mining-tools-that-read-retrieve-and-teach?source=rss) — *HackerNoon*, 25/11 19:01 · **4/10** (Recensement outils texte open source, bonne ressource mais pas nouveauté)
  *Titre original : 20 Repos, 2M Stars: The Open Source Text Mining Tools That Read, Retrieve and Teach.*
  > From PaddleOCR to LangChain to free LLM courses: 20 open source text mining repos with 2M GitHub stars, grouped by the job they do.
- [L’art du jeu à l’ère de l’IA](https://github.blog/news-insights/company-news/art-of-play-in-the-age-of-ai/) — *GitHub Blog*, 25/11 17:00 · **4/10** (Essai artistique IA, plus culturel que technique)
  *Titre original : Art of play in the age of AI*
  > Now that code ships faster than ever, you have more time to spend on projects just for the fun of it. Here's what we can learn through that process as developers. The post Art of play in the age of AI appeared first on The GitHub Blog .
- [Genetec publie le connecteur Model Context Protocol pour Security Center](https://www.msspalert.com/brief/genetec-releases-model-context-protocol-connector-for-security-center) — *MSSP Alert*, 25/11 16:39 · **3/10** (Connecteur Model Context Protocol, niche sécurité)
  *Titre original : Genetec releases Model Context Protocol connector for security center*
  > Genetec has launched a new Model Context Protocol (MCP) connector for its Security Center platform, allowing systems integrators and administrators to utilize artificial intelligence assistants for ...
- [Flurra](https://www.producthunt.com/products/flurra) — *Product Hunt*, 25/11 17:34 · **3/10** (Nouveau produit Flurra, visibilité faible)
  *Titre original : Flurra*
  > Ask Claude or ChatGPT to edit your videos Discussion | Link
- [NEXUS](https://www.producthunt.com/products/nexus-42) — *Product Hunt*, 25/11 13:41 · **3/10** (Produit NEXUS, peu d'informations techniques)
  *Titre original : NEXUS*
  > Map codebase locally and AI changes only what you approved Discussion | Link
- [Ubuntu - Le nouveau lanceur sera boosté à l’IA](https://korben.info/ubuntu-lanceur-ia-local.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 25/11 07:42 · **3/10** (Annonce lanceur IA Ubuntu en français, peu de détails techniques)
  *Titre original : Ubuntu - Le nouveau lanceur sera boosté à l'IA*
  > Canonical montre son futur lanceur Ubuntu en train de tourner : un point d'entrée pour les applis et les fichiers, avec une IA en opt-in et locale d'abord. Ce qui est promis, ce qui ne l'est pas, et pourquoi il faudra attendre janvier pour tester.
- [Hub](https://www.producthunt.com/products/hub-20) — *Product Hunt*, 24/11 19:34 · **3/10** (Produit Hub, visibilité très limitée)
  *Titre original : Hub*
  > Run 100 Claude Code or Codex sessions like 5 Discussion | Link
- [datasette-charts 0.3a0](https://simonwillison.net/2026/Nov/25/datasette-charts/) — *Simon Willison*, 25/11 19:16 · **2/10** (Mise à jour datasette-charts, intérêt très restreint)
  *Titre original : datasette-charts 0.3a0*
  > Release: datasette-charts 0.3a0 I added chart annotations to datasette-charts ! You can now render a chart and then annotate it with lines, shaded areas, labels, or a combination of the three. A chart with annotations looks like this: Here's that same chart in Datasette Lite , where you can tweak th

## Autres articles (1)

- [Un ingénieur utilise Claude Code pour détecter ce que le logiciel CAM a manqué](https://news.google.com/rss/articles/CBMipAFBVV95cUxNMUEzeHd0UDNFOU5sbEkyakdBQUtJSGRoVndQdkJ2elIzRGZUZnY2eXFWMkZjZ09XTnVSMXBkQVlWWXNsdDFrOEVjUmlTTktwTWpocWV2ZlRqQU9BeHIzNHh5VEdhbEtaek1Gd3hCeFNKZEI1b3E5el9EazNhVktBQ1ZmMkZBX09VNEpobnFQYzNJRGQ4dFktRDk4dDJTd0lIUWhiNw?oc=5) — *AIM Media House*, 25/11 16:31 · **5/10** (Utilisation Claude Code pour détecter erreurs CAM, cas d'usage concret)
  *Titre original : An Engineer Used Claude Code to Catch What CAM Software Missed*

## Vidéos à regarder (10)

- [What's Claude Code running in the background?](https://www.youtube.com/watch?v=KAz5W056WnY) — *Stack Shortcuts*, 26/11 08:01
  > Cette vidéo montre ce que Claude Code exécute en arrière-plan à l'aide de la commande /tasks.
- [Make Claude Code Ask Before It Codes: AI-DLC Setup Tutorial](https://www.youtube.com/watch?v=JnOWK9t1R5E) — *SHAJAM*, 26/11 06:48
  > Ce tutoriel présente la configuration AI-DLC d'AWS pour obliger l'assistant de code Claude à poser des questions avant d'écrire du code.
- [Google Workspace MCP Servers Are Live: New Rules for AI Agents in Gmail & Drive (Feb 2027)](https://www.youtube.com/watch?v=bUQGuLlGuj8) — *AI Inbox Academy*, 26/11 03:00
  > Cette vidéo aborde l'arrivée des serveurs MCP Google Workspace et du CLI officiel pour les agents IA dans Gmail et Drive.
- [AI Agents Tutorial 4 – Memory and Context Engineering | Full Course 2026](https://www.youtube.com/watch?v=g8LSgxfJBJM) — *iTV*, 26/11 01:30
  > Ce tutoriel complet explore la gestion de la mémoire et l'ingénierie du contexte pour les agents IA en Python.
- [Claude Code vs Codex: The Payment Bug](https://www.youtube.com/watch?v=zaD90WvnIPg) — *Prune Labs Co*, 26/11 01:00
  > Cette vidéo compare les performances de Claude Code et Codex sur la résolution d'un vrai bug de paiement.
- [WhipDesk: Control AI Coding Agents From Your Phone (Claude Code, Codex, Cursor) | Open Source](https://www.youtube.com/watch?v=pU5wnXukC4g) — *Binary Banana - Games & Apps*, 25/11 22:25
  > Cet outil open source permet de contrôler et d'interagir avec des agents de codage IA comme Claude Code, Codex et Cursor directement depuis son téléphone.
- [Claude Ship: AI That Approves Your Code](https://www.youtube.com/watch?v=-W-v1wcTeFU) — *Built This Week*, 25/11 21:08
  > Cette vidéo présente Claude Ship, un outil d'Anthropic où des agents examinent les pull requests, corrigent les échecs et approuvent les modifications de routine.
- [I tested n8n's new AI Assistant Nod vs Hermes Agent (Full Comparison)](https://www.youtube.com/watch?v=0T2TxAt2G5c) — *Serop | AI Automation*, 25/11 17:00
  > Ce contenu propose une comparaison complète entre l'assistant IA Nod de n8n et le robot Hermes Agent.
- [I Tested 4 Claude Code Alternatives for a Month — One Won (Antigravity, Aider, Codex, OpenCode)](https://www.youtube.com/watch?v=pTdyYq1tfCM) — *AdiCodeHub*, 25/11 16:30
  > Cette vidéo résume un test d'un mois comparant quatre alternatives à Claude Code : Google Antigravity, Aider, Codex et OpenCode.
- [Build Your First AI Agent with Canva MCP, Python & LangGraph | Full Hands-On](https://www.youtube.com/watch?v=i2Ay5UE_3CU) — *Manifold AI Learning*, 25/11 16:00
  > Ce tutoriel pratique montre comment construire un premier agent IA en combinant le protocole MCP de Canva, Python et LangGraph.

## Podcasts à écouter (10)

- [Ep 31 · Daily Wrap: Wednesday, November 25, 2026](https://podcasts.apple.com/us/podcast/ep-31-daily-wrap-wednesday-november-25-2026/id6834673859?i=1000804146612&uo=4) — *ACN · AI Coding News*, 26/11 08:43
  > Un récapitulatif quotidien d'AI Coding News avec un focus sur les limites d’usage de ChatGPT et une démonstration pratique des applications desktop de Claude.
- [MicroAgent : This Coding Agent can Generate Code and Test, But is it better than Aider? (w/ Ollama)](https://podcasts.apple.com/us/podcast/microagent-this-coding-agent-can-generate-code-and/id6826122006?i=1000804144705&uo=4) — *AICodeKing*, 26/11 08:37
  > Présentation de MicroAgent, un agent de codage capable de générer et tester du code, comparé à l'outil Aider, avec utilisation d'Ollama.
- [Nov 26 · DeepMind's AI-assisted proof checks Signal's encryption engine](https://podcasts.apple.com/us/podcast/nov-26-deepminds-ai-assisted-proof-checks-signals-encryption/id6830641736?i=1000804135961&uo=4) — *The DAIly — the Jump Daily AI podcast*, 26/11 07:20
  > Le podcast The DAIly explique comment DeepMind a utilisé l'IA pour vérifier les preuves de chiffrement de Signal.
- [Ep 30 · Midday Update: Wednesday, November 25, 2026](https://podcasts.apple.com/us/podcast/ep-30-midday-update-wednesday-november-25-2026/id6834673859?i=1000804097237&uo=4) — *ACN · AI Coding News*, 26/11 01:52
  > Mise à jour d'AI Coding News sur le déplacement de l'API d'Anthropic vers Rust, les nouvelles règles de Google pour les agents IA, et d’autres actualités techniques.
- [Who Fixes It When AI Breaks? Microsoft's Code Red (Nov 25, 2026)](https://podcasts.apple.com/us/podcast/who-fixes-it-when-ai-breaks-microsofts-code-red-nov-25-2026/id1684415169?i=1000804051132&uo=4) — *AI Unraveled: Enterprise Strategy, Agentic Systems, Daily AI News, ChatGPT, Gemini, Claude, DeepSeek*, 25/11 20:09
  > Discussion autour du « Code Red » de Microsoft après une panne majeure et de l’utilisation d’agents IA pour prévenir de futurs incidents.
- [With an agent you can build almost anything, but selling is harder](https://podcasts.apple.com/us/podcast/with-an-agent-you-can-build-almost-anything-but/id6810117720?i=1000804028909&uo=4) — *AI Agents & Vibe Coding*, 25/11 17:50
  > Tutoriel sur la création d’un système d’analyse d’appels et d’analytics avec Claude Code ou Codex, sans besoin de développeurs.
- [Shortwave vs Fyxer vs Tasklet for a 3-Person Agency’s Client Inbox](https://podcasts.apple.com/us/podcast/shortwave-vs-fyxer-vs-tasklet-for-a-3-person/id1894868302?i=1000804021023&uo=4) — *Agentic AI at Work: The Future of Workflow Automation*, 25/11 16:31
  > Comparaison de trois outils (Shortwave, Fyxer, Tasklet) pour automatiser la boîte de réception d’une petite agence, illustrant l’automatisation de workflows avec l’IA.
- [Anthropic says your Claude page can now be a desktop app. How much access should it get? Plus Perplexity inside your Chrome](https://podcasts.apple.com/us/podcast/anthropic-says-your-claude-page-can-now-be-a/id6790021778?i=1000804009691&uo=4) — *AI Industry Report*, 25/11 15:52
  > Anthropic annonce que les pages Claude peuvent désormais être transformées en applications desktop, avec un aperçu des nouvelles possibilités.
- [GPT-6 designs proteins, Neon tops LiveBench — AI News Nov 25](https://podcasts.apple.com/us/podcast/gpt-6-designs-proteins-neon-tops-livebench-ai-news-nov-25/id6817748791?i=1000803976126&uo=4) — *AI Engineering Briefing: Daily AI News for Software Engineers*, 25/11 12:51
  > Bulletin d’ingénierie IA présentant les dernières avancées : GPT‑6.2 conçoit des protéines, Gemini 4 Neon domine le benchmark LiveBench, et les implications pour les développeurs d’agents.
- [How OpenClaw Cut Their $1.27M CI Bill by 95% and Unlocked Multiplayer AI with Chief Architect Vincent Koc](https://podcasts.apple.com/us/podcast/how-openclaw-cut-their-%241-27m-ci-bill-by-95-and/id1776879655?i=1000803975037&uo=4) — *Chain of Thought | AI Agents, Infrastructure & Engineering*, 25/11 12:45
  > Interview de Vincent Koc d’OpenClaw sur la réduction de 95 % de leur facture CI grâce à l’IA et le lancement du multijoueur IA.

## Écartés comme hors sujet (70)

- [If you can't measure AI by feature, you can't measure ROI](https://itbrief.com.au/story/if-you-can-t-measure-ai-by-feature-you-can-t-measure-roi) — *IT Brief Australia*, 26/11 09:10
  > Businesses can no longer judge AI spend by bill alone, as leaders need feature-level costs linked to outcomes to prove return on investment.
- [OpenAI's custom GPT shutdown is a warning about who owns your firm's AI](https://itbrief.com.au/story/openai-s-custom-gpt-shutdown-is-a-warning-about-who-owns-your-firm-s-ai) — *IT Brief Australia*, 26/11 09:10
  > The deadline could leave firms scrambling to track down AI workflows built in personal accounts before client work is disrupted.
- [Can LED Displays Get Burn-In? What You Should Know](https://dev.to/linsnled/can-led-displays-get-burn-in-what-you-should-know-40i7) — *dev.to*, 26/11 09:08
  > LED displays are designed for long-term use, but they can still develop uneven brightness after thousands of operating hours. Unlike OLED screens, direct-view LED displays do not typically suffer from the same type of permanent burn-in. Instead, their LEDs gradually lose brightness over time. When s
- [How businesses can prepare their engineering talent for AI-driven change](https://itbrief.com.au/story/how-businesses-can-prepare-their-engineering-talent-for-ai-driven-change) — *IT Brief Australia*, 26/11 09:03
  > Companies risk wasted AI spend unless engineers are reskilled to judge outputs, protect delivery and turn context into business value.
- [Is innovation moving faster than accountability?](https://itbrief.com.au/story/is-innovation-moving-faster-than-accountability) — *IT Brief Australia*, 26/11 09:01
  > As AI moves into core business processes, CIOs face growing pressure to keep decision-making visible, auditable and under control.
- [AI’s relentless goal pursuit raises a new safety risk, Mo Bitar says](https://www.tokenpost.com/news/technology/62693) — *TOKENPOST*, 26/11 08:24
  > YouTube creator Mo Bitar said AI models that relentlessly pursue goals could pose a greater safety risk than highly intelligent systems, citing cases involving denied access and prolonged operation.
- [Anthropic Finds Claude Models Reached Outside Sandboxes in Siren Tests](https://www.tokenpost.com/news/technology/62692) — *TOKENPOST*, 26/11 08:21
  > Recent Claude models reached beyond insecure test environments in roughly one-fifth to one-third of scenarios, while misaligned use remained below 2%.
- [Google anuncia el despliegue de Wallet en AI Mode en EE. UU.](https://www.neoteo.com/es/google-anuncia-el-despliegue-de-wallet-en-ai-mode-en-ee-uu) — *NeoTeo*, 26/11 08:12
  > Google anunció el despliegue optativo de Wallet en AI Mode en Estados Unidos y explicó qué contexto puede usar y qué integraciones llegarían después.
- [Shirudo para proteger Linux: Java4Shell no usó eBPF](https://www.neoteo.com/es/shirudo-para-proteger-linux-java4shell-no-uso-ebpf) — *NeoTeo*, 26/11 08:12
  > OpenAI y Cisco anunciaron Shirudo para Linux el 23 de noviembre de 2026. La demo Java4Shell descrita usó bytecode Java en una JVM activa, no un escudo eBPF.
- [Anthropic loses another Claude Code engineer to OpenAI, and the internet is asking why everyone is leaving](https://www.msn.com/en-in/news/other/anthropic-loses-another-claude-code-engineer-to-openai-and-the-internet-is-asking-why-everyone-is-leaving/ar-AA2ig6Ad) — *India Today*, 26/11 08:05
  > Another key engineer behind Anthropic's Claude Code has jumped ship to OpenAI, leaving the tech world wondering what is happening inside the company.
- [India Electronics and IT Secretary S. Krishnan Says US AI Chip Export Controls Spare India](https://casrai.org/news/india-meity-secretary-krishnan-us-ai-chip-export-controls-impact-2026) — *CASRAI*, 26/11 08:00
  > India’s domestic AI compute and research hubs will not face disruption from tightened US GPU export controls, MeitY Secretary S. Krishnan confirmed.
- [Según Axios, algunos empleados dudan de que Anthropic y OpenAI puedan lanzar ciertos modelos con seguridad](https://www.neoteo.com/es/segun-axios-algunos-empleados-dudan-de-que-anthropic-y-openai-puedan-lanzar-ciertos-modelos-con-seguridad) — *NeoTeo*, 26/11 07:41
  > Axios informó de dudas en Anthropic y OpenAI sobre la seguridad de modelos inéditos y opciones debatidas para limitar el acceso o frenar el entrenamiento.
- [Grabaciones de OpenAI: la orden de libertad de Alfozan y las alegaciones sobre Codex](https://www.neoteo.com/es/grabaciones-de-openai-la-orden-de-libertad-de-alfozan-y-las-alegaciones-sobre-codex) — *NeoTeo*, 26/11 07:41
  > The New York Times informó de la orden de libertad bajo fianza de Abdulrahman Alfozan; la fiscalía atribuye a Codex y Dropbox un papel en las grabaciones.
- [Venice AI faces privacy allegations as VVV drops over 15%](https://cryptobriefing.com/venice-ai-privacy-allegations-vvv-drops/) — *Crypto Briefing*, 26/11 07:38
  > Privacy concerns could erode trust in Venice AI, impacting user engagement and token value, while regulatory scrutiny may intensify. The post Venice AI faces privacy allegations as VVV drops over 15% appeared first on Crypto Briefing .
- [Universities Expand Spoken Thesis Defenses and Oral Assessments to Counter Generative AI Misconduct](https://casrai.org/news/universities-expand-oral-defenses-spoken-thesis-assessments-counter-ai-2026) — *CASRAI*, 26/11 07:30
  > Universities are expanding mandatory spoken thesis defenses and oral exams to verify student authorship as generative AI challenges written evaluations.
- [ARK Invest Sells Crypto-Linked Shares, Buys $26.3M in Anthropic Stock](https://www.tokenpost.com/news/investing/62672) — *TOKENPOST*, 26/11 07:23
  > The firm sold Bullish, Robinhood and two staking ETFs in Wednesday trades while increasing its Anthropic position.
- [sqlite3_rsync: Database Remote-Copy Tool For SQLite](https://simonwillison.net/2026/Nov/26/sqlite3-rsync/) — *Simon Willison*, 26/11 07:08
  > sqlite3_rsync: Database Remote-Copy Tool For SQLite This additional SQLite tool has been around for a while now - it was added as "experimental" in SQLite 3.47.0 in October 2024 and enhanced in SQLite 3.50.0 in May 2025 . It was only today that I understood one of its most attractive characteristics
- [KIOXIA GP2 Series SSD Delivers New Levels of Performance for GPU Memory Expansion](https://www.01net.it/kioxia-gp2-series-ssd-delivers-new-levels-of-performance-for-gpu-memory-expansion/) — *01net*, 26/11 07:00
  > Next-Generation Super High IOPS SSD Featuring KIOXIA XL-FLASH Generation 3 Memory Enables Direct GPU Access to Larger Datasets in AI ArchitecturesSAN JOSE, Calif.--(BUSINESS WIRE)--KIOXIA America, Inc. today announced the KIOXIA GP2 Series Super High I... L'articolo KIOXIA GP2 Series SSD Delivers Ne
- [University at Buffalo Secures DOE Early Career Grant for AI Urban Sewer Overflow Modeling](https://casrai.org/news/university-at-buffalo-doe-early-career-grant-ai-combined-sewer-overflow-2026) — *CASRAI*, 26/11 06:01
  > The University at Buffalo secured an $875,000 DOE Early Career grant to train physics-informed AI models on urban sewer data to predict overflows.
- [Anthropic Expands Zurich AI Research Hub at Fraumunsterpost Building Near ETH Zurich](https://casrai.org/news/anthropic-expands-zurich-ai-research-office-fraumunsterpost-eth-zurich-2026) — *CASRAI*, 26/11 06:00
  > Anthropic has leased 2,500 square meters at Zurich’s Fraumunsterpost building for up to 150 AI researchers collaborating with ETH Zurich.
- [China’s domestic AI chip output could rise nearly sixfold by 2030, UBS says](https://cryptobriefing.com/china-ai-chip-output-sixfold-2030-ubs/) — *Crypto Briefing*, 26/11 05:28
  > China's AI chip industry growth could enhance technological self-reliance, challenging global market dynamics and impacting international trade. The post China’s domestic AI chip output could rise nearly sixfold by 2030, UBS says appeared first on Crypto Briefing .
- [Apple pulls Talkie from App Store after children receive abusive AI chats](https://news.lavx.hu/article/apple-pulls-talkie-from-app-store-after-children-receive-abusive-ai-chats) — *news.lavx.hu*, 26/11 05:08
  > Characters on Talkie, an AI roleplay app owned by Shanghai-based MiniMax, sent degrading and sexualized messages to children. The case shows gaps in rules for Chinese-owned companion apps used outside China.
- [OpenAI merges ChatGPT Chat and Work under one usage meter](https://news.lavx.hu/article/openai-merges-chatgpt-chat-and-work-under-one-usage-meter) — *news.lavx.hu*, 26/11 05:05
  > The change combines Chat and Work into a shared usage limit in ChatGPT. OpenAI says most subscribers will see no difference, but the heaviest users may reach their caps sooner.
- [OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster](https://twitter.com/thsottiaux/status/2125784147889393806) — *Hacker News*, 26/11 04:36
  > Article URL: https://twitter.com/thsottiaux/status/2125784147889393806 Comments URL: https://news.ycombinator.com/item?id=50651117 Points: 189 # Comments: 94
- [AI coding agents risk loss of engineering knowledge, says Stack Overflow](https://news.google.com/rss/articles/CBMirgFBVV95cUxNVUxBcUhzeGlMTW5zMjhTM2k4LWl4bk16YlZmbUtHZ2tTTXk0VWFyVXJFdmVBTHRDNkJneEc5b1ViRWZjWEJYUjFrX1h4eUYxMmJ4M2ZCRDczcWtPWmRPaU96aUItYnlZWVJhZFcxQU9fc1JIN1dpRHdmTG94dUJCU3JvUU5xTWVmbXVCaExUSmI1UW42YXJ0Zzd4UGhwS1dEU0ZkSHA5NUFfOXByT1E?oc=5) — *TechGig*, 26/11 04:32
- [OpenAI Codex, Astra Flag Exoplanet Candidates; SETI Astronomer Matches Two Signals, None Confirmed](https://www.msn.com/en-us/news/other/openai-codex-astra-flag-exoplanet-candidates-seti-astronomer-matches-two-signals-none-confirmed/ar-AA2ifFga) — *Tech Times*, 26/11 04:06
  > Exoplanet candidates from OpenAI Codex and Astra searches include two Kepler signals that a SETI Institute astronomer also found, but OpenAI says none is confirmed. Eclipsing binary stars can mimic ...
- [Anthropic and OpenAI proofs fuel speculation about AI’s threat to encryption](https://cryptobriefing.com/ai-impact-on-cryptography-threats/) — *Crypto Briefing*, 26/11 03:47
  > AI advancements in solving complex mathematical problems could undermine current encryption systems, posing significant security risks. The post Anthropic and OpenAI proofs fuel speculation about AI’s threat to encryption appeared first on Crypto Briefing .
- [Dropbox to Present at the 2026 UBS Global Technology and AI Conference](https://www.01net.it/dropbox-to-present-at-the-2026-ubs-global-technology-and-ai-conference/) — *01net*, 26/11 01:04
  > SAN FRANCISCO--(BUSINESS WIRE)--Dropbox, Inc. (NASDAQ: DBX) Chief Financial Officer Ross Tennenbaum will participate in a fireside chat at the 2026 UBS Global Technology and AI Conference in Scottsdale, Arizona on Thursday, December 3, 2026 at 10:55 p.... L'articolo Dropbox to Present at the 2026 UB
- [Cycode Grows UK Team As Demand For AI Coding Security Takes Off](https://news.google.com/rss/articles/CBMijwFBVV95cUxONWZHNUt6OUhmUmdNYzVna3Q2LXk0V01iQ1lEMFdoOTJQTkstVEZ1YU5JV2taTWRpSlU4WjVYS0ZWaE8wR1pWdXRMSVFaYi1jU2FfVHB1WVM2SkV3b09kVEhTc2xZM1I3MHFlZUdtSEpLd1I3QWZ6Z3lfOURHb25ETUJRcjNoa3E3Q2tpcUJrMA?oc=5) — *TechRound*, 26/11 00:48
- [Riassunto: IQM Quantum Computers collabora con QAI, un’azienda sudcoreana specializzata in Quantum-AI per installare un computer quantistico nel proprio centro dati di AI privato in Corea](https://www.01net.it/riassunto-iqm-quantum-computers-collabora-con-qai-unazienda-sudcoreana-specializzata-in-quantum-ai-per-installare-un-computer-quantistico-nel-proprio-centro-dati-di-ai-privato-in-corea/) — *01net*, 26/11 00:42
  > IQM consegnerà un IQM Radiance R3, un computer quantistico da 54 qubit, a QAI, società sudcoreana specializzata in data center e infrastrutture cloud per l'AI quantistica entro la fine del 2027. Una volta operativo, QAI prevede di offrire il sistema... L'articolo Riassunto: IQM Quantum Computers col
- [GDS Holdings tops expectations with Q3 revenue of about $477 million as AI bookings climb](https://cryptobriefing.com/gds-holdings-q3-revenue-beats-expectations/) — *Crypto Briefing*, 26/11 00:40
  > GDS Holdings' strong AI-driven revenue growth amid reduced spending highlights potential for sustained profitability despite thin net income. The post GDS Holdings tops expectations with Q3 revenue of about $477 million as AI bookings climb appeared first on Crypto Briefing .
- [Quoting Scott Aaronson](https://simonwillison.net/2026/Nov/25/scott-aaronson/) — *Simon Willison*, 26/11 00:26
  > It’s now obvious that we’ll be getting, not one-off solutions to this or that complexity question, but a whole new continent of mathematical truth, one that we’d previously only glimpsed through fog. Picture van Leeuwenhoek first training a microscope on pondwater, or Galileo first training his tele
- [The Revolution vs The Renaissance — Thariq Shihipar, OpenAI](https://latent.space/p/the_revolution_vs_the_renaissance_thariq_shihipar_openai/) — *Latent Space*, 25/11 23:28
  > AI can make software cheap enough to produce by the thousand and still give you more time to make one thing feel right. At AI Engineer CODE, Thariq Shihipar shows how those two futures can coexist. In his fighting game, he edits the size of a rock in t...
- [[AINews] Math Proofs Are Landing Faster Than We Can Read Them](https://latent.space/p/ainews-math-proofs-are-landing-faster-than-we-can-read-them/) — *Latent Space*, 25/11 23:23
  > November 25, 2026 — From Erdős problems to new bounds for matrix multiplication and Fourier transforms.
- [Riassunto: Infobip: nel 2027 gli agenti IA svolgeranno più attività incentrate sui clienti](https://www.01net.it/riassunto-infobip-nel-2027-gli-agenti-ia-svolgeranno-piu-attivita-incentrate-sui-clienti/) — *01net*, 25/11 22:35
  > Agenti IA personali, identità degli agenti e risultati quantificabili sono pronti a riplasmare il coinvolgimento dei clientiDIGNANO, Croazia--(BUSINESS WIRE)--La piattaforma IA cloud globale per le comunicazioni Infobip oggi ha condiviso cinque previs... L'articolo Riassunto: Infobip: nel 2027 gli a
- [Claude Code Exits: Cat Wu Took 27 Hours, Shihipar 32 Days](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOZzJuSG85a0tQbDBUQ0h0Q1JvcHJrN3VfaFdxaXV5T2R3aUpON3psQ1NuSDlCRlNiNFRDeXVrRzRKQ0h6T2xxMVkzZl84dkpwVEVzY08yY1lIN0F4MzE3NnlaMEdZYzVOX1VnZDktUUtfMUVRcjZ6YV9VSlBTOW8wN1h3MTROLXpWUG9r?oc=5) — *FourWeekMBA*, 25/11 22:32
- [The New York Times warns photographers not to update Photoshop over AI features](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features) — *Hacker News*, 25/11 22:18
  > https://archive.ph/pcUgy Comments URL: https://news.ycombinator.com/item?id=50647673 Points: 341 # Comments: 289
- [While the U.S. Treasury was under attack, its CIO was busy vibe coding a game](https://www.howtogeek.com/us-treasury-attack-cio-was-vibe-coding-game/) — *How-To Geek*, 25/11 21:54
  > Wednesday, November 25, morning ET: 404 Media reported the overlap and said the Treasury didn’t respond to its request for comment. By 9:42 a.m. ET, Reuters reported the Treasury was working with the ...
- [US chip-access curbs and anti-distillation measures are reportedly already slowing Chinese AI labs](https://the-decoder.com/us-chip-access-curbs-and-anti-distillation-measures-are-reportedly-already-slowing-chinese-ai-labs/) — *The Decoder*, 25/11 21:51
  > Chip restrictions, anti-distillation measures, and shrinking access to Nvidia hardware abroad are putting growing pressure on Deepseek, Moonshot AI, and Alibaba, according to a report. Deepseek researchers internally estimate they're already up to nine months behind US models, and the gap is widenin
- [Claude Code’s Thariq Shihipar Joins OpenAI After 32 Days](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPWlN2NElId2ZjbzJFaDltWlBuV1RiV01aZWNYRjdkaElRMzQ0TjFvalpUZVJkZGtTbmtqQ2EtTlR4dGRPLUNKQWdyYUgyTWpoandQekN5RDZ1T0VLTkRTeUJ4dEtleEw5OEU5eWppUjVjSXlDa214THc1T29WNHpJQXlxNjRZdEh1WC1B?oc=5) — *FourWeekMBA*, 25/11 21:38
- [Treasury CIO Vibe Codes Video Game Amid Cyberattack](https://news.google.com/rss/articles/CBMirwFBVV95cUxQWm8zZEItLXdnY3c4S3ptZjNZMkpwNW9DSVZ0WTJpQl9FOGRqb2czRXBQYTU3bzAwVWdDQV9jMHFnUjJwOE1PbHpscUF3NFdLQVlGMVRfWXJwekc4YlRCTzFmYld6MDhnbU51Y3V4V191MW1NcWlWZG93XzM3bEF2R3FtdEI1TzFwZ25pNE5uUU55YmRJNkU0UTdNMk52eUNvN1hNemhBcU5iZ2sydnVR?oc=5) — *Gizmodo*, 25/11 21:30
- [Anthropic CEO Dario Amodei says letting AI govern society would be "a bad idea"](https://the-decoder.com/anthropic-ceo-dario-amodei-says-letting-ai-govern-society-would-be-a-bad-idea/) — *The Decoder*, 25/11 21:15
  > Anthropic CEO Dario Amodei is pushing back on an Axios report saying some employees believe humanity will hand power to superintelligent systems. Amodei says "turning over governance to AI is a bad idea." The article Anthropic CEO Dario Amodei says letting AI govern society would be "a bad idea" app
- [How CAD Software Thinks: B-rep, CSG, NURBS, and Their Role in AI-Generated Designs](https://hackernoon.com/how-cad-software-thinks-b-rep-csg-nurbs-and-their-role-in-ai-generated-designs?source=rss) — *HackerNoon*, 25/11 20:54
  > Learn how CAD stores shapes with B-rep, CSG, and NURBS, and why these ideas decide whether an AI-written CAD script produces a usable part.
- [Cycode Expands UK Operations as Enterprise Adoption of AI Coding Accelerates](https://news.google.com/rss/articles/CBMiowFBVV95cUxPVy1ZZ2EydnB2aXYtUkZReHQ1aDF0VzBCeUdncERzZXVPNm5vLTNpdHMwYmo5MTZZZEh6QnpzSTZvWmp6WXNpR1pxbWZMS0d1VU0xdl9Zc3pvQ005eFRRZDVIclVnVHJENTBKSGJPT3lOWUh3a05DSjR5alZnWjc1czdBWHNubFlsUUFYTTdNWDdab1BhN2lkN0NYZi1TTlR5VDVR?oc=5) — *VMblog*, 25/11 20:26
- [While the Treasury Department is dealing with a hack, one of its head honchos is vibe-coding a Civ clone](https://www.msn.com/en-us/gaming/general/while-the-treasury-department-is-dealing-with-a-hack-one-of-its-head-honchos-is-vibe-coding-a-civ-clone/ar-AA2iepio) — *Destructoid*, 25/11 20:20
  > Yikes. The post While the Treasury Department is dealing with a hack, one of its head honchos is vibe-coding a Civ clone appeared first on Destructoid.
- [Treasury CIO Is Vibe Coding a ‘Civilization’ Clone During Treasury Department Hack](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPNXduaURLWWF6c0VKdjdDNUIyVE1TTjZJeW9WUGtoZmxTN1EwWEk3VWJ1NjRYeFY4RENicFVFdEgyT092SXdBVWk5a1F2alFSYmJHV1FRTVdYaDhvd2cyLVdUODlETmg5SjZ5cWttc0dNdFNvUTB3TzZiNnZyTnpRUWJwVzBTSEtrMHBETmctTGZ5YWFYZE9RNndJTjlfcThNLU4wSklZQ3c5SkRMbUxKX2NGRDVIY3ZkTDdZVm1wallGUQ?oc=5) — *404 Media*, 25/11 20:01
- [Treasury CIO Sam Corcos is vibe coding a Civ rip-off](https://news.google.com/rss/articles/CBMifEFVX3lxTE91aElCUmtKY0ZwalhkTHNjMXJsbkRYcUltQmY1dExob2JPMHVhRmRGS05YOXJ3WVFEM3FyQWdFa1NFX3dkZEo1V1ZEakF6d1ZpNzVZdk1XYk5uQ1Z6RDFGREt6NC1NRDdQTms0SXdZX2hsZUM2OWZwdVMxMjY?oc=5) — *Protos | Informed crypto news*, 25/11 19:50
- [After the SaaSpocalypse, Xero says AI is a tailwind not a threat](https://www.afr.com/technology/after-the-saaspocalypse-xero-says-ai-is-a-tailwind-not-a-threat-20261126-p61foh) — *AFR*, 25/11 19:00
  > Predictions that established software companies would be knocked off by cheap clones appear overblown as the cost of security, compliance and tokens pile up.
- [Music Gear Makers Embrace Open-Source Modding Amid AI Coding Boom](https://news.google.com/rss/articles/CBMilwFBVV95cUxPalpNOEFIUDJSOXpON0dCOV9TMWRoXzdXWDVkMEJfdllBZW55UXgxWFVGdm9JaVRBSmloZFllRFd5Q3ZseUs5cFJrOEJQdlk5Q0d5M2t1eGZsaHV5VGpaTGVqQWY5a3FVa2E5SGRkZk5oMXZ6RGhpVzdELXdrN3MzMHlSbzFtelNYZEhUQU5iMDl4dmszNWtV?oc=5) — *SSBCrack*, 25/11 18:10
- [The Hidden Cost of AI Coding: Why Context Matters More Than Tokens](https://www.unite.ai/ai-token-costs-software-delivery/) — *Unite.AI*, 25/11 16:54
  > Over the past year, my conversations with technology leaders have shifted noticeably. Back then, we asked: Can large language models write faster and better code, generate documentation and run tests?
- [Trump official caught vibe coding 'Civilization' game clone as hackers hit his department](https://www.msn.com/en-us/technology/cybersecurity/trump-official-caught-vibe-coding-civilization-game-clone-as-hackers-hit-his-department/ar-AA2icFrs) — *Raw Story*, 25/11 15:42
  > Treasury Department Chief Information Officer Sam Corcos kept making changes to a video game he's building with AI after a Treasury bureau disclosed a cyberattack, 404 Media reported Wednesday. The ...
- [OpenAI wants companies to trust it with sensitive work by promising not to look at their data](https://the-decoder.com/openai-wants-companies-to-trust-it-with-sensitive-work-by-promising-not-to-look-at-their-data/) — *The Decoder*, 25/11 19:22
  > OpenAI is testing a new feature called "Private Inference" that lets companies run queries on its most powerful models without OpenAI being able to access the data. The article OpenAI wants companies to trust it with sensitive work by promising not to look at their data appeared first on The Decoder
- [OpenAI claims to have solved a 57-year-old math problem at the heart of AI computation](https://thenewstack.io/openai-matrix-multiplication-exponent/) — *The New Stack*, 25/11 19:14
  > OpenAI claims to have solved a problem that has occupied theoretical computer scientists since 1969. In a preprint published Tuesday The post OpenAI claims to have solved a 57-year-old math problem at the heart of AI computation appeared first on The New Stack .
- [Amazon and Meta are in talks to end the block on Meta's AI shopping agent Muse in Amazon's online store.](https://the-decoder.com/amazon-and-meta-are-in-talks-to-end-the-block-on-metas-ai-shopping-agent-muse-in-amazons-online-store/) — *The Decoder*, 25/11 17:44
  > Amazon and Meta are in talks to bring back Muse, Meta's AI shopping agent that Amazon kicked off its platform in September. The two sides are stuck on ad revenue and who gets to control search results. That matters because Amazon's ad business generates $68.6 billion a year, and Muse already command
- [How to choose the next safe step in application modernization](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/) — *GitHub Blog*, 25/11 16:00
  > Learn how to assess a legacy application, choose a bounded modernization step, and reuse the method with a GitHub Copilot agent skill. The post How to choose the next safe step in application modernization appeared first on The GitHub Blog .
- [DoorDash Scales Dispatch 10x While Maintaining 99.99% Peak Availability](https://www.infoq.com/news/2026/11/doordash-dispatch-redesign/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 25/11 15:44
  > DoorDash has redesigned its real-time dispatch platform, replacing a monolithic optimization engine with a distributed architecture that separates coordination from computation. The new system delivers 10x higher throughput and more than 99.99% peak availability. It also supports hybrid machine lear
- [Prompting AI to be ‘thorough’ can drive sandbox escapes, Anthropic says](https://www.infoworld.com/article/4253057/prompting-ai-to-be-thorough-can-drive-sandbox-escapes-anthropic-says-2.html) — *InfoWorld*, 25/11 13:09
  > Prompt wording meant to make AI agents more resourceful, such as telling them to search thoroughly or invoking authority, sharply raises the odds they will reach outside a poorly secured sandbox, Anthropic has found in its latest evaluation. The evaluation, called Siren, gives Claude models routine 
- [Google-Agent : comment éviter de bloquer l’agent IA sur votre site](https://www.blogdumoderateur.com/google-agent-comment-eviter-bloquer-agent-ia-site/) — *Blog du Modérateur*, 25/11 08:30
  > Google détaille comment reconnaître Google-Agent, son agent qui navigue et agit sur les sites pour le compte des internautes, et comment le laisser passer sans affaiblir vos protections anti-bots.
- [E-commerce : comment l’IA accompagne l’acheteur de la recherche à la décision d’achat](https://www.blogdumoderateur.com/e-commerce-ia-accompagne-acheteur-recherche-decision-achat/) — *Blog du Modérateur*, 25/11 08:00
  > Recherches sans résultat, questions restées sans réponse : sur un site e-commerce, l'hésitation coûte des ventes. Longtemps associé à la recherche interne, Doofinder mise désormais sur un assistant IA et des outils de découverte pour accompagner l'acheteur jusqu'à l'achat.
- [[AINews] Gemini 4 Neon marks GDM's full return as a Frontier Lab](https://latent.space/p/ainews-gemini-4-neon-marks-gdm-s-full-return-as-a-frontier-lab/) — *Latent Space*, 25/11 05:29
  > November 24, 2026 — Neon beats Astra and Fable on LiveBench and cuts Theo’s TS Rust benchmark runtime by 48.6%.
- [Meet Facebook’s Your Algorithm: How Meta Turns Plain-Language Preferences Into Ranking](https://www.marktechpost.com/2026/11/24/meta-facebook-your-algorithm-llm-recommendations/) — *MarkTechPost*, 25/11 00:06
  > Meta's engineering team explains how Facebook's Your Algorithm turns plain-language interests into ranking signals for Feed and Reels, using LLM validation, 4 retrieval sources, layered filtering and a fine-tuned LLM reranker. The post Meet Facebook’s Your Algorithm: How Meta Turns Plain-Language Pr
- [Three LLM inflection points in twelve months](https://simonwillison.net/2026/Nov/24/llm-inflection-points/) — *Simon Willison*, 25/11 00:02
  > I gave a keynote at the AI Engineer Code Summit a couple of weeks ago, constructed around the idea that there have been three significant inflection points in the abilities of LLMs and coding agents in the past twelve months. Here's the video of the talk. In this post I'm going to pull out the major
- [Please don’t give the robot my SSH keys: How to keep AI out of trouble](https://thenewstack.io/teleport-agent-delegated-identity/) — *The New Stack*, 24/11 22:57
  > Say a developer asks an AI agent to find out why a Kubernetes pod keeps crashing. The agent needs logs. The post Please don’t give the robot my SSH keys: How to keep AI out of trouble appeared first on The New Stack .
- [Move fast, don’t break 100 apps: Dan Garfield on keeping AI-powered coding on the rails](https://thenewstack.io/ai-coding-delivery-bottleneck/) — *The New Stack*, 24/11 20:48
  > An AI coding agent can give a product manager a working prototype before the next planning meeting. Which is great! The post Move fast, don’t break 100 apps: Dan Garfield on keeping AI-powered coding on the rails appeared first on The New Stack .
- [GPT-6 models demonstrate intrinsic protein-design capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities) — *OpenAI*, 24/11 14:00
  > GPT-6 models design protein structures and sequences using reasoning and code. Lab tests found evidence of binding across five targets.
- [Searching for distant planets with Astra](https://openai.com/index/searching-for-distant-planets-with-astra) — *OpenAI*, 24/11 12:00
  > See how two amateur astronomers used Codex and Astra to find potential exoplanets in public data from NASA’s Kepler and TESS space telescopes.
- [Vibe coding pushes music gear makers toward open source](https://news.google.com/rss/articles/CBMigwFBVV95cUxOWTBiNkR4U0JwWWU1UlA1NmdqaUNpSkR1b1NIMXZXMEFaVzZud3lyREpSZmh6dEhBZXp2Q0pUYm1GSFBlM1cycDBIZW91SlRpZ0hOWWh2X05DSTdYUmxfV2ItNzlMNDRCc0o1X0pGMmtLRWcxLWJEV2FKOVdtMTV2RjhGMA?oc=5) — *Mezha.net*, 25/11 14:09
- [Has vibe coding made open source the new normal for synths?](https://www.theverge.com/ai-artificial-intelligence/1040081/vibe-coding-open-source-music-firmware) — *The Verge*, 25/11 14:00
  > Companies like Akai have decided to embrace the modding community rather than resist vibe coders.
- [AI coding tools are generating "disposable" software. Their impact might linger](https://news.google.com/rss/articles/CBMirgFBVV95cUxOdWsyY3FvZnprbzB2NlBwSHlpbWN2RWllb0lEVW9CSzdiMng4Y1B0YXhkX0U5ZjhNeERBS3pVdVZlSXpxd3RyQXZLVzBsckdXc0VSYVpYY2cxbGMybVg4QjQ3QXNxR1ltaDJ5bkZxOTRwYnNuREVINUpiaG5fUG1fM3lzVDdERVl3YkFvT1g5TzA2MnBpYVFZdFN4QllGRjE1cjRMNXE5dmhFLVNVaFE?oc=5) — *www.thestack.technology*, 25/11 09:18
- [Below Issue Price Isn’t the Worst: OpenAI’s Frenetic Poaching of Claude Code’s Core Team Hits Anthropic — Is Its Programming AI Throne Hanging in the Balance?](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBza3gtaFFTTXRtNllGeDI2VmQ4TE1yWHNHM3A0dXc4V3g5YzFfbndncm50SDBIdVlJemtVQ3VpN0R0c3ZCTDhwUC1ZaFdYV1kzb1Rn?oc=5) — *36Kr*, 25/11 09:12
