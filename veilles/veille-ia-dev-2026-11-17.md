# Veille IA outils & code du 17/11/2026

49 articles de médias tech anglophones et francophones (blogs d'outils, Hacker News, Product Hunt) publiés ces 48 dernières heures (rapport généré à 08:54).

**Attention : seulement 49 articles trouvés sur les 50 demandés.**

Sources inaccessibles : Google Actualités.

## Synthèse du jour

La veille révèle un fort dynamisme autour des agents IA, avec plusieurs publications détaillant des cadres de conception, des patterns multi‑agents et des implémentations concrètes sur Bedrock. Le secteur des assistants de codage continue d’évoluer, notamment via GitHub Copilot, des bibliothèques de compétences et de nouveaux outils comme ByteVoice. Du côté des modèles, les géants publient de nouvelles versions (Claude, GPT‑6, Qwen4‑Max) et des benchmarks soulignent des gains de performance. La sécurité reste une préoccupation majeure, plusieurs articles signalent l’émergence d’attaques autonomes et la nécessité de cadres de gouvernance. Enfin, les plateformes cloud enrichissent leurs offres avec des services d’inférence privée, d’émulation et de distribution de modèles, facilitant l’accès aux IA pour les développeurs et les chercheurs.

*Vérifiée : chaque affirmation est appuyée par au moins un titre.*

## À lire en priorité

- [Alibaba publie Qwen4‑Max : 2,4 T MoE, 71 B actifs, 1 M de contexte](https://www.marktechpost.com/2026/11/16/alibaba-qwen4-max-release/) — *MarkTechPost*, 16/11 10:44 · **9/10** (Lancement Qwen4‑Max d'Alibaba, modèle très puissant)
  *Titre original : Alibaba Releases Qwen4-Max: 2.4T MoE, 71B Active, 1M Context*
  > Alibaba released Qwen4-Max, a proprietary 2.4T-parameter MoE model with 71B active parameters, native vision and a 1M-token context. It costs $1.5/M input tokens and cuts Work360 cost per task by 62%. The post Alibaba Releases Qwen4-Max: 2.4T MoE, 71B Active, 1M Context appeared first on MarkTechPos
- [Construire des agents IA sensibles à la mémoire avec Agentic Retrieve sur Amazon Bedrock Managed Knowledge Base](https://aws.amazon.com/blogs/machine-learning/build-memory-aware-ai-agents-with-agentic-retrieve-on-amazon-bedrock-managed-knowledge-base/) — *AWS Machine Learning*, 16/11 23:43 · **8/10** (Framework mémoire‑aware sur Bedrock, très utile pour agents concrets)
  *Titre original : Build memory-aware AI agents with Agentic Retrieve on Amazon Bedrock Managed Knowledge Base*
  > Amazon Bedrock Managed Knowledge Base and Amazon Bedrock AgentCore memory now store conversations, extract facts, and bring long-term memory into a single AgenticRetrieveStream call. This post shows how to build a memory-aware, multi-user assistant where each user sees only the documents they may re
- [Google découvre des hackers utilisant des agents IA autonomes pour transformer des correctifs de sécurité en exploits](https://thenewstack.io/autonomous-ai-exploit-agents/) — *The New Stack*, 16/11 22:27 · **8/10** (Incident sécurité majeur avec agents autonomes, très pertinent)
  *Titre original : Google found hackers using autonomous AI agents to turn security patches into exploits*
  > Google’s Threat Intelligence Group says attackers are using autonomous AI agents to reverse-engineer security patches, generate exploits, and attempt to The post Google found hackers using autonomous AI agents to turn security patches into exploits appeared first on The New Stack .
- [Gemini 4 Hydrogen de Google transforme le choix du modèle en décision de routage](https://devops.com/googles-gemini-4-hydrogen-turns-model-choice-into-a-routing-decision) — *DevOps.com*, 16/11 08:30 · **8/10** (Gemini 4 Hydrogen de Google, routage dynamique des modèles)
  *Titre original : Google’s Gemini 4 Hydrogen Turns Model Choice Into a Routing Decision*
  > Google is expanding its Gemini 4 family with Hydrogen, a speed-focused model designed for AI coding agents and multi-step workflows. Alongside it, the new Orchestrator capability in Google Antigravity routes tasks between faster execution models and more powerful reasoning models. Google claims the 
- [Le cadre d’IA sécurisée d’Uber régit les agents IA autonomes tout au long de leur cycle de vie](https://www.infoq.com/news/2026/11/uber-secure-ai-framework/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 15/11 21:00 · **8/10** (Framework Secure AI d'Uber, gouvernance complète des agents autonomes)
  *Titre original : Uber's Secure AI Framework Governs Autonomous AI Agents across Their Lifecycle*
  > In a recent article, Uber Engineering highlights the limitations of traditional identity and API controls in securing AI agents that dynamically reason over external content and take real-world actions. Uber developed a framework to determine whether an agent's action is appropriate given the user's

## Agents IA et cadres de conception (17)

Ces articles portent sur les agents intelligents, leurs compétences, les patterns de conception multi‑agents et les implémentations sur des plateformes comme Amazon Bedrock. Ils décrivent aussi des cas d’usage concrets d’agents dans le domaine juridique ou financier.

- [Construire des agents IA sensibles à la mémoire avec Agentic Retrieve sur Amazon Bedrock Managed Knowledge Base](https://aws.amazon.com/blogs/machine-learning/build-memory-aware-ai-agents-with-agentic-retrieve-on-amazon-bedrock-managed-knowledge-base/) — *AWS Machine Learning*, 16/11 23:43 · **8/10** (Framework mémoire‑aware sur Bedrock, très utile pour agents concrets)
  *Titre original : Build memory-aware AI agents with Agentic Retrieve on Amazon Bedrock Managed Knowledge Base*
  > Amazon Bedrock Managed Knowledge Base and Amazon Bedrock AgentCore memory now store conversations, extract facts, and bring long-term memory into a single AgenticRetrieveStream call. This post shows how to build a memory-aware, multi-user assistant where each user sees only the documents they may re
- [Gemini 4 Hydrogen de Google transforme le choix du modèle en décision de routage](https://devops.com/googles-gemini-4-hydrogen-turns-model-choice-into-a-routing-decision) — *DevOps.com*, 16/11 08:30 · **8/10** (Gemini 4 Hydrogen de Google, routage dynamique des modèles)
  *Titre original : Google’s Gemini 4 Hydrogen Turns Model Choice Into a Routing Decision*
  > Google is expanding its Gemini 4 family with Hydrogen, a speed-focused model designed for AI coding agents and multi-step workflows. Alongside it, the new Orchestrator capability in Google Antigravity routes tasks between faster execution models and more powerful reasoning models. Google claims the 
- [Le cadre d’IA sécurisée d’Uber régit les agents IA autonomes tout au long de leur cycle de vie](https://www.infoq.com/news/2026/11/uber-secure-ai-framework/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 15/11 21:00 · **8/10** (Framework Secure AI d'Uber, gouvernance complète des agents autonomes)
  *Titre original : Uber's Secure AI Framework Governs Autonomous AI Agents across Their Lifecycle*
  > In a recent article, Uber Engineering highlights the limitations of traditional identity and API controls in securing AI agents that dynamically reason over external content and take real-world actions. Uber developed a framework to determine whether an agent's action is appropriate given the user's
- [Taxonomie des modèles de conception multi‑agents, anti‑patterns et leçons tirées de la fabrication](https://aws.amazon.com/blogs/machine-learning/taxonomy-of-multi-agent-design-patterns-anti-patterns-and-lessons-from-manufacturing/) — *AWS Machine Learning*, 16/11 22:53 · **7/10** (Taxonomie design patterns multi‑agents, guide pratique)
  *Titre original : Taxonomy of multi-agent design patterns, anti-patterns, and lessons from manufacturing*
  > Multi-agent coordination is a distributed systems problem, not a model problem. This post gives a field-tested taxonomy of multi-agent design patterns and anti-patterns, a framework for deciding when multiple agents are warranted, and how to build cost-efficient, reliable systems on AWS.
- [L’agent juridique d’Uber réduit de 20 % le temps d’examen des contrats grâce aux règles et au RAG](https://www.infoq.com/news/2026/11/uber-legal-redlining-agent/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 16/11 15:37 · **7/10** (Agent juridique Uber réduisant le temps de revue de contrats de 20 %)
  *Titre original : Uber’s Legal AI Agent Cuts Contract Review Time by 20% with Rules and RAG*
  > Uber’s Legal Redlining Agent reviews contract changes in Microsoft Word using RAG, historical lawyer feedback, and deterministic policy rules. Built with LangGraph, OpenSearch, and Redis, the system reports more than 20% lower average contract review time and 91% accuracy in AI-generated decisions. 
- [Airbnb lance CASTLE pour entraîner des modèles de recherche en langage naturel avec des données synthétiques](https://www.infoq.com/news/2026/11/airbnb-castle/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 16/11 13:25 · **7/10** (CASTLE d'Airbnb pour données synthétiques, outil de formation novateur)
  *Titre original : Airbnb Introduces CASTLE for Training Natural Language Search Models with Synthetic Data*
  > Airbnb researchers have introduced CASTLE, a framework designed to address the cold-start problem in natural language search. The approach uses de-identified booking sessions and large language models (LLMs) to jointly generate synthetic search queries and relevance labels, enabling model training b
- [AWS publie en open source un émulateur pour tester localement plus de 200 services par des agents de codage](https://www.infoq.com/news/2026/11/aws-emulator-agents/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 16/11 11:40 · **7/10** (Émulateur open‑source AWS pour tests agents, très utile)
  *Titre original : AWS Open-Sources Emulator for Local Testing of 200+ Services by Coding Agents*
  > AWS Emulator is a generally available local HTTPS endpoint, generated from public Smithy API models, that lets developers and coding agents test against more than 200 AWS services without an account, with published fidelity scores and documented limits around IAM, regions, and in-memory state. By Da
- [Prise en main d’AG‑UI — le protocole d’interaction agent‑utilisateur](https://www.infoworld.com/article/4248550/getting-started-with-ag-ui-the-agent-user-interaction-protocol.html) — *InfoWorld*, 16/11 10:00 · **7/10** (Guide de démarrage AG‑UI, protocole d'interaction agent‑utilisateur)
  *Titre original : Getting started with AG-UI — the agent-user interaction protocol*
  > While AI agents, which can perform long-running work autonomously, have supplanted simple chats for serious work with large (and small) language models, agents have a last-mile problem: How do you display what an agent is doing in front of a user and let the user act on it, without forcing every tea
- [Les agents IA étaient omniprésents à KubeCon. La production est une autre histoire](https://thenewstack.io/cncf-bryce-ai-agents/) — *The New Stack*, 16/11 23:08 · **6/10** (Retour d'expérience KubeCon, production d'agents IA)
  *Titre original : AI agents were all over KubeCon. Production is another story*
  > AI agents are testing systems that were originally built for people, and Jonathan Bryce thinks the cloud-native community has a The post AI agents were all over KubeCon. Production is another story appeared first on The New Stack .
- [Comment MoEngage a construit un engagement client agentique sur Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/how-moengage-built-agentic-customer-engagement-on-amazon-bedrock-agentcore/) — *AWS Machine Learning*, 16/11 19:16 · **6/10** (Cas d'usage MoEngage sur Bedrock, exemple concret d'engagement)
  *Titre original : How MoEngage built agentic customer engagement on Amazon Bedrock AgentCore*
  > MoEngage built Merlin AI, a set of AI agents on Amazon Bedrock and Amazon Bedrock AgentCore that let marketing and product teams draft, analyze, and adjust campaigns from a single conversation. Learn how MoEngage turned its existing APIs into MCP tools and kept each tenant's data isolated while givi
- [Hark lance Handoff², un agent d’utilisation d’ordinateur deux fois plus rapide pour Hark Pro](https://www.marktechpost.com/2026/11/16/hark-handoff-2-computer-use-agent-2x-faster/) — *MarkTechPost*, 16/11 10:08 · **6/10** (Handoff², agent de usage ordinateur deux fois plus rapide)
  *Titre original : Hark Releases Handoff², a 2x Faster Computer-Use Agent for Hark Pro*
  > Hark has released Handoff², the computer-use agent inside Hark Pro. It averages 2x faster than v1, completes 82% of 478 internal web tasks, and learned to batch actions through latency-penalized RL. The post Hark Releases Handoff², a 2x Faster Computer-Use Agent for Hark Pro appeared first on MarkTe
- [Qu’est-ce que les compétences des agents IA et comment elles fonctionnent](https://dev.to/keshav_af7403d92948605d98/what-ai-agent-skills-are-and-how-they-work-30ap) — *dev.to*, 17/11 08:45 · **5/10** (Article explicatif sur les compétences des agents IA, utile mais peu novateur)
  *Titre original : What AI Agent Skills Are and How They Work*
  > AI Agent Skills: The Missing Piece of Procedural Knowledge TL;DR AI agents are great at reasoning and recalling facts, but they struggle with step‑by‑step workflows. Skills solve this by packaging procedural knowledge into lightweight, open‑standard Markdown files that agents load on demand. They’re
- [Agents IA pour les entreprises : ce qu’ils sont et leur mode de fonctionnement](https://dev.to/gex_melk_8e5bfbf8b7477871/ai-agents-for-business-what-they-are-and-how-they-work-4jc5) — *dev.to*, 17/11 08:41 · **5/10** (Vue d'ensemble des agents IA pour le business, intéressant mais déjà vu)
  *Titre original : AI agents for business: what they are and how they work*
  > "AI agent" has become one of those terms that means everything and nothing. Vendors use it for chat widgets, for Zapier flows with a GPT step in the middle, and for systems that genuinely plan and act on their own. If you are a developer asked to "add an agent" to a business process, it helps to hav
- [Claude Code est déjà un harnais IA. Pourquoi créer un enregistreur de vol ?](https://dev.to/bargan/claude-code-is-already-an-ai-harness-why-build-a-flight-recorder-2mlm) — *dev.to*, 17/11 08:42 · **4/10** (Promotion d'un outil existant, peu d'impact réel)
  *Titre original : Claude Code Is Already an AI Harness. Why Build a Flight Recorder?*
  > A coding agent can say it finished a task. That does not tell you whether the last test passed. A log can show that a shell command ran. It cannot, by itself, tell you whether the result is correct. And when a terminal goes quiet, you may be looking at a permission prompt, a long-running tool, or a 
- [llm 0.37.3](https://simonwillison.net/2026/Nov/16/llm/) — *Simon Willison*, 17/11 00:57 · **4/10** (Mise à jour mineure de version LLM, intérêt limité)
  *Titre original : llm 0.37.3*
  > Release: llm 0.37.3 A bug fix release for LLM , mainly to cover a problem with the most recent Homebrew package of the software. Homebrew now ships the latest SQLite, 3.54.1 , which includes a fix that broke LLM's logging code . Short version: in SQLite 3.54.0 the following SQL: select json_object('
- [Les agents héritent de votre désordre](https://devops.com/agents-inherit-your-mess) — *DevOps.com*, 16/11 14:44 · **4/10** (Opinion sur la dette technique des agents, peu de données concrètes)
  *Titre original : Agents Inherit Your Mess*
  > AI agents need more than raw logs. Discover how stateless ingestion, asynchronous enrichment and semantic context improve observability, reliability and cost.
- [Instinct, l’agent IA qui valait 10 milliards](https://www.blogdumoderateur.com/instinct-agent-ia-10-milliards/) — *Blog du Modérateur*, 17/11 07:00 · **3/10** (Focus sur valorisation financière, peu de valeur technique)
  *Titre original : Instinct, l’agent IA qui valait 10 milliards*
  > Des prouesses qui font le tour des réseaux, des invitations revendues à prix d'or, une valorisation à 10 milliards de dollars : Instinct, l'agent IA que l'on commande via WhatsApp ou iMessage, est devenu un phénomène en quelques semaines. Pourquoi ?

## Outils d’assistance au codage (15)

Cette catégorie regroupe les nouveautés autour des assistants de programmation, des extensions IDE, des bibliothèques de compétences d’agents et des plateformes de génération de code comme GitHub Copilot, ByteVoice ou les kits de compétences de Cuttlefish.

- [Modèles GitHub Copilot retirés le 16 novembre 2026](https://github.blog/changelog/2026-11-16-github-copilot-models-deprecated-on-november-16-2026) — *GitHub Changelog*, 16/11 21:25 · **7/10** (Dépréciation de modèles Copilot, impact sur les utilisateurs)
  *Titre original : GitHub Copilot models deprecated on November 16, 2026*
  > As of today, November 16, 2026, we have deprecated the following models across most GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions). Note… The post GitHub Copilot models deprecated on November 16, 2026 appeared first on The GitHub Blog .
- [Tokendoctor – le même Claude Code pour jusqu’à 38 % moins cher](https://github.com/localixai/tokendoctor) — *Hacker News*, 17/11 03:19 · **6/10** (Nouvel outil de réduction de coût pour Claude Code, utile aux développeurs)
  *Titre original : Tokendoctor – the same Claude Code for up to 38% less*
  > Article URL: https://github.com/localixai/tokendoctor Comments URL: https://news.ycombinator.com/item?id=50526584 Points: 20 # Comments: 8
- [Faire tourner des agents de codage sans leur remettre mes identifiants](https://blog.antonio.cx/running-agents-with-lend) — *Hacker News*, 17/11 02:18 · **6/10** (Solution de sécurité pour agents de codage, sujet pertinent)
  *Titre original : Running coding agents without handing them my credentials*
  > Article URL: https://blog.antonio.cx/running-agents-with-lend Comments URL: https://news.ycombinator.com/item?id=50526152 Points: 99 # Comments: 54
- [Comment Duco transforme l’automatisation des données financières avec Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/how-duco-transforms-financial-data-automation-with-amazon-bedrock-agentcore/) — *AWS Machine Learning*, 16/11 23:06 · **6/10** (Cas d'usage financier avec Bedrock AgentCore, bonne illustration)
  *Titre original : How Duco transforms financial data automation with Amazon Bedrock AgentCore*
  > Duco, a data automation platform for tier-one banks, rebuilt its agentic AI stack on Amazon Bedrock and Amazon Bedrock AgentCore. With strict per-tenant isolation, a multi-model strategy, and an MCP skills architecture that cut context overhead by 90%, Duco cut reconciliation deployment time 10x and
- [Développement de l’apprentissage automatique : comment les entreprises transforment les données en décisions intelligentes](https://dev.to/venkatesh_bfcc04c25b5570e/machine-learning-development-how-businesses-can-turn-data-into-intelligent-decisions-ngn) — *dev.to*, 17/11 08:44 · **5/10** (Guide pratique sur le ML en entreprise, pertinence modérée)
  *Titre original : Machine Learning Development: How Businesses Can Turn Data Into Intelligent Decisions*
  > Businesses generate enormous amounts of data every day. Customer interactions, online transactions, website activity, inventory records, and operational processes all produce information that can help organizations make better decisions. However, collecting data is only the first step. The real chal
- [Versions hebdomadaires de GitHub Copilot — 9 novembre](https://github.blog/changelog/2026-11-16-github-copilot-weekly-releases-november-9) — *GitHub Changelog*, 16/11 22:34 · **5/10** (Mises à jour hebdomadaires Copilot, informations opérationnelles)
  *Titre original : GitHub Copilot weekly releases — November 9*
  > This week, bring GitHub Enterprise Server repositories into the Copilot app and see which agent sessions need you first in VS Code. You can also try two new models, Claude… The post GitHub Copilot weekly releases — November 9 appeared first on The GitHub Blog .
- [Contrôler la provenance des personnalisations de GitHub Copilot](https://github.blog/changelog/2026-11-16-control-where-github-copilot-customizations-come-from) — *GitHub Changelog*, 16/11 20:48 · **5/10** (Fonctionnalité de contrôle des personnalisations Copilot)
  *Titre original : Control where GitHub Copilot customizations come from*
  > As an enterprise administrator, you can now require selected GitHub Copilot customizations to come from plugins or managed settings, rather than standalone user or project configuration. Combined with marketplace restrictions,… The post Control where GitHub Copilot customizations come from appeared 
- [VS Code retire le harnais Local en février 2027](https://github.blog/changelog/2026-11-16-vs-code-retires-the-local-harness-in-february-2027) — *GitHub Changelog*, 16/11 20:22 · **5/10** (Retrait du Local harness VS Code, changement d'infrastructure)
  *Titre original : VS Code retires the Local harness in February 2027*
  > Visual Studio Code 1.146 deprecates the Local harness, the older software that coordinates the model, context, and tools for GitHub Copilot agent sessions in the editor. The Local harness will… The post VS Code retires the Local harness in February 2027 appeared first on The GitHub Blog .
- [Superpowers Plus : les compétences Swarm de Thomas Ricouard — 31 compétences d’agent pour un codage discipliné](https://hackernoon.com/superpowers-plus-thomas-ricouards-swarm-skills-31-agent-skills-for-disciplined-coding?source=rss) — *HackerNoon*, 16/11 16:15 · **5/10** (Catalogue de compétences Swarm pour codage, ressource pratique)
  *Titre original : Superpowers Plus Thomas Ricouard's Swarm Skills: 31 Agent Skills for Disciplined Coding*
  > Two builders' skill sets make AI coding agents work like disciplined engineers. Jesse Vincent's Superpowers adds 15 skills that make the agent brainstorm.
- [The TechBeat : la bibliothèque de compétences Cuttlefish.MD met à profit 2 806 compétences d’agent vérifiées (16/11/2026)](https://hackernoon.com/11-16-2026-techbeat?source=rss) — *HackerNoon*, 16/11 16:00 · **5/10** (Bibliothèque de compétences Cuttlefish.MD, grande collection)
  *Titre original : The TechBeat: Cuttlefish.MD Skills Library Puts 2,806 License-Checked Agent Skills to Work (11/16/2026)*
  > 11/16/2026: Trending stories on Hackernoon today!
- [ByteVoice](https://www.producthunt.com/products/bytevoice) — *Product Hunt*, 16/11 02:45 · **4/10** (Produit ByteVoice, peu d'informations techniques)
  *Titre original : ByteVoice*
  > Talk to your coding agents and hear them back Discussion | Link
- [StateWeave](https://www.producthunt.com/products/stateweave) — *Product Hunt*, 15/11 21:32 · **4/10** (Produit StateWeave, peu de détails sur l'utilité IA)
  *Titre original : StateWeave*
  > Test your AI agent on working clones of the apps it uses Discussion | Link
- [datasette‑maplibre 0.1a0](https://simonwillison.net/2026/Nov/15/datasette-maplibre/) — *Simon Willison*, 16/11 00:58 · **3/10** (Version alpha de datasette‑maplibre, impact limité)
  *Titre original : datasette-maplibre 0.1a0*
  > Release: datasette-maplibre 0.1a0 The first new Datasette geospatial plugin in quite a while! This one combines the excellent MapLibre GL library with OpenFreeMap , the free vector map server operated by Zsolt Ero (you should sponsor Zsolt on GitHub .) I built most of this with a single prompt to Cl
- [datasette 1.0a43](https://simonwillison.net/2026/Nov/15/datasette/) — *Simon Willison*, 16/11 00:20 · **3/10** (Version alpha de datasette, changements mineurs)
  *Titre original : datasette 1.0a43*
  > Release: datasette 1.0a43 I've been leaning hard into Claude Fable 5.2 to help knock things off the 1.0 milestone , which is now 53% complete. The biggest 1.0 item in this release is streaming support for output renderers - the built-in TSV and CSV export mechanisms now use this as well, and plugins
- [Puffin](https://www.producthunt.com/products/puffin-2) — *Product Hunt*, 15/11 20:51 · **3/10** (Produit Puffin, information insuffisante pour évaluer pertinence)
  *Titre original : Puffin*
  > Identity and inboxes for AI agents Discussion | Link

## Lancements de modèles et benchmarks (6)

Ces titres annoncent la sortie ou l’évaluation de grands modèles de langage (Claude, GPT‑6, Qwen4‑Max, etc.) ainsi que des comparaisons de performances sur des benchmarks spécialisés.

- [Alibaba publie Qwen4‑Max : 2,4 T MoE, 71 B actifs, 1 M de contexte](https://www.marktechpost.com/2026/11/16/alibaba-qwen4-max-release/) — *MarkTechPost*, 16/11 10:44 · **9/10** (Lancement Qwen4‑Max d'Alibaba, modèle très puissant)
  *Titre original : Alibaba Releases Qwen4-Max: 2.4T MoE, 71B Active, 1M Context*
  > Alibaba released Qwen4-Max, a proprietary 2.4T-parameter MoE model with 71B active parameters, native vision and a 1M-token context. It costs $1.5/M input tokens and cuts Work360 cost per task by 62%. The post Alibaba Releases Qwen4-Max: 2.4T MoE, 71B Active, 1M Context appeared first on MarkTechPos
- [Anthropic affirme que Claude Mythos a porté le logiciel GPU AMD en trois jours, sapant le fossé CUDA de Nvidia](https://news.lavx.hu/article/anthropic-says-claude-mythos-ported-amd-gpu-software-in-three-days-chipping-at-nvidia-s-cuda-moat) — *news.lavx.hu*, 17/11 06:04 · **7/10** (Annonce technique majeure d'Anthropic, impact sur l'écosystème GPU)
  *Titre original : Anthropic says Claude Mythos ported AMD GPU software in three days, chipping at Nvidia's CUDA moat*
  > Anthropic told IPO investors that its Claude Mythos Preview model wrote almost all the code needed to run one of its models on AMD GPUs in about three days, a job it says used to take six to 12 months. The claim is narrow, but it challenges the software lock-in that has protected Nvidia.
- [Nvidia domine sept références d’entraînement IA avec les résultats Vera Rubin](https://cryptobriefing.com/nvidia-vera-rubin-mlperf-training-benchmarks/) — *Crypto Briefing*, 17/11 02:16 · **7/10** (Benchmarks Nvidia, influence forte sur le hardware IA)
  *Titre original : Nvidia leads seven AI training benchmarks with Vera Rubin results*
  > Nvidia's AI advancements could accelerate innovation across industries, enhancing efficiency and capabilities in AI-driven applications. The post Nvidia leads seven AI training benchmarks with Vera Rubin results appeared first on Crypto Briefing .
- [ChatGPT Wallet : les agents d’OpenAI peuvent désormais régler les achats en ligne](https://www.blogdumoderateur.com/chatgpt-wallet-agents-ia-openai-achats-en-ligne/) — *Blog du Modérateur*, 16/11 10:35 · **7/10** (ChatGPT Wallet permettant paiements via agents, nouvelle fonctionnalité)
  *Titre original : ChatGPT Wallet : les agents d’OpenAI peuvent désormais régler les achats en ligne*
  > OpenAI ouvre le paiement à ses agents IA avec un portefeuille conçu avec Visa, Mastercard et American Express, réservé pour l’instant aux abonnés Pro américains.
- [Construire l’intelligence visuelle — Andreas Blattmann & Dustin Podell, Black Forest Labs](https://latent.space/p/bfl/) — *Latent Space*, 16/11 22:38 · **6/10** (Publication recherche vision IA, contribution scientifique)
  *Titre original : Building Visual Intelligence — Andreas Blattmann & Dustin Podell, Black Forest Labs*
  > Black Forest Labs’ case for learning AGI from pixels, motion and sound.
- [Les meilleurs modèles pour piloter des agents IA en novembre 2026](https://www.blogdumoderateur.com/meilleurs-modeles-piloter-agents-ia-novembre-2026/) — *Blog du Modérateur*, 16/11 10:49 · **5/10** (Sélection de modèles IA pour agents, guide d'achat)
  *Titre original : Les meilleurs modèles pour piloter des agents IA en novembre 2026*
  > Les modèles d'Anthropic dominent toujours l'Agent Arena, un benchmark collaboratif qui mesure l'aptitude des IA à orchestrer des tâches agentiques.

## Sécurité, cyberdéfense et gouvernance (4)

Les articles de ce thème traitent des risques liés aux agents autonomes, des attaques automatisées, de la fuite de crédentiels et des cadres de gouvernance pour sécuriser l’usage des IA dans les entreprises.

- [Google découvre des hackers utilisant des agents IA autonomes pour transformer des correctifs de sécurité en exploits](https://thenewstack.io/autonomous-ai-exploit-agents/) — *The New Stack*, 16/11 22:27 · **8/10** (Incident sécurité majeur avec agents autonomes, très pertinent)
  *Titre original : Google found hackers using autonomous AI agents to turn security patches into exploits*
  > Google’s Threat Intelligence Group says attackers are using autonomous AI agents to reverse-engineer security patches, generate exploits, and attempt to The post Google found hackers using autonomous AI agents to turn security patches into exploits appeared first on The New Stack .
- [Windows 11 collecte des données sur les agents de codage et les outils de développeur que vous utilisez](https://xusheng.dev/posts/windows-coding-agent-telemetry/) — *Hacker News*, 16/11 23:58 · **5/10** (Collecte de données Windows 11, question de confidentialité)
  *Titre original : Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use*
  > Article URL: https://xusheng.dev/posts/windows-coding-agent-telemetry/ Comments URL: https://news.ycombinator.com/item?id=50524736 Points: 513 # Comments: 354
- [Les identifiants fuités sont un problème d’entreprise : GitGuardian élargit son programme du bon samaritain](https://hackernoon.com/leaked-credentials-are-an-enterprise-problem-gitguardian-extends-its-good-samaritan-program?source=rss) — *HackerNoon*, 16/11 20:12 · **5/10** (Problème de credentials fuité, sujet sécurité d'entreprise)
  *Titre original : Leaked Credentials Are an Enterprise Problem: GitGuardian Extends Its Good Samaritan Program*
  > Combining AI-powered attribution with expert security analysis, the program identifies high-impact credential leaks that could give attackers a path
- [Linux Foundation : les outils de codage IA dépassent les défenses de cybersécurité](https://devops.com/linux-foundation-ai-coding-tools-are-outpacing-cybersecurity-defenses) — *DevOps.com*, 16/11 21:03 · **4/10** (Opinion sur la course IA vs cybersécurité, peu de faits concrets)
  *Titre original : Linux Foundation: AI Coding Tools Are Outpacing Cybersecurity Defenses*
  > A new Linux Foundation report finds that 58% of software development teams are releasing code faster than their security staff can review it, raising major concerns about vulnerabilities introduced by AI coding tools. The report, State of AI Impact on Software Security and Cybersecurity 2026, survey

## Services cloud, infrastructure et plateformes IA (7)

Cette catégorie rassemble les annonces de services cloud (AWS Bedrock, Vercel AI Gateway, Hugging Face/OpenRouter) ainsi que les outils d’émulation, d’inférence privée et de gestion de modèles destinés aux développeurs et aux chercheurs.

- [Élargir l’accès à l’IA pour les scientifiques](https://openai.com/index/expanding-chatgpt-for-academic-researchers) — *OpenAI*, 16/11 18:00 · **6/10** (Ouverture d'accès IA pour scientifiques, initiative importante)
  *Titre original : Broadening access to AI for scientists*
  > We’re expanding our ChatGPT for Academic Researchers program to offer 200,000 researchers worldwide free access to our frontier models.
- [Renforcer la lutte contre les abus sexuels en ligne sur enfants grâce à de nouveaux outils et soutiens](https://openai.com/index/strengthening-online-child-safety) — *OpenAI*, 16/11 18:00 · **6/10** (Outils contre l'abus sexuel en ligne, impact sociétal)
  *Titre original : Strengthening the fight against online child sexual abuse with new tools and support*
  > New tools, practical guidance, and partnerships will help prevent, detect and respond to online child sexual exploitation and abuse.
- [Découvrez les JiTTests de Meta : tests générés par LLM conçus pour échouer avant que du code risqué ne soit déployé](https://www.marktechpost.com/2026/11/16/meta-jittests-llm-catching-tests-privacy-bugs/) — *MarkTechPost*, 16/11 11:39 · **6/10** (JiTTests de Meta, génération de tests LLM, amélioration CI)
  *Titre original : Meet Meta’s JiTTests: LLM-Generated Tests Designed to Fail Before Risky Code Lands*
  > Meta has moved Catching JiTTests into production. The LLM system writes tests designed to fail on risky diffs, and caught 74 privacy SEVs before landing in H1 2026, with a 60% engineer-reported true-positive rate. The post Meet Meta’s JiTTests: LLM-Generated Tests Designed to Fail Before Risky Code 
- [AI Gateway prend en charge l’inférence privée](https://vercel.com/changelog/ai-gateway-now-supports-private-inference) — *Vercel*, 16/11 08:47 · **6/10** (Support inference privée sur AI Gateway, renforce confidentialité)
  *Titre original : AI Gateway now supports Private Inference*
- [Hugging Face et OpenRouter s’associent pour simplifier l’exécution de modèles à poids ouvert](https://huggingface.co/blog/openrouter) — *Hugging Face*, 16/11 01:00 · **6/10** (Partenariat Hugging Face & OpenRouter, facilite déploiement modèles)
  *Titre original : Hugging Face and OpenRouter join forces to make open-weight models easy to run*
- [Hy4 Flash disponible sur AI Gateway avec 50 % de réduction](https://vercel.com/changelog/hy4-flash-now-available-on-ai-gateway-for-50-off) — *Vercel*, 16/11 18:00 · **5/10** (Promotion Hy4 Flash sur AI Gateway, offre intéressante)
  *Titre original : Hy4 Flash now available on AI Gateway for 50% off*
- [Seedance 2.5 Flash disponible sur AI Gateway](https://vercel.com/changelog/seedance-2-5-flash-now-available-on-ai-gateway) — *Vercel*, 16/11 01:00 · **4/10** (Mise à jour Seedance 2.5 Flash, amélioration mineure)
  *Titre original : Seedance 2.5 Flash now available on AI Gateway*

## Vidéos à regarder (10)

- [Skills vs Plugins vs Mods: Claude Code](https://www.youtube.com/watch?v=r7wI-L0zxJo) — *Code Cuts*, 17/11 08:30
  > Comparaison des compétences, plugins et mods de Claude Code, avec explication de l’impact de chaque plugin sur le contexte.
- [MCP Explained: The USB-C for AI Agents (Model Context Protocol in 70 Seconds)](https://www.youtube.com/watch?v=f9wIploVars) — *Abolfazl Mashhadi *, 17/11 08:02
  > Présentation du Model Context Protocol (MCP) comme norme unique pour connecter les IA aux outils, remplaçant le code personnalisé.
- [33 Tools Give Your AI Agent Eyes | Chrome DevTools MCP](https://www.youtube.com/watch?v=XqXinoL7Aes) — *Huzaifa Rehan*, 17/11 08:00
  > Démonstration de Chrome DevTools MCP qui donne aux agents de codage IA un véritable navigateur Chrome avec console et outils de développement.
- [Why AI Agents Never Actually Run Their Own Tools](https://www.youtube.com/watch?v=ziytA9y-FRk) — *Farzad*, 17/11 07:08
  > Analyse du fait que les agents IA ne peuvent jamais exécuter directement leurs propres outils, ils ne font que lire et écrire du texte.
- [AI Agents with n8n – Complete Full Course for Beginners | Build AI Automation Workflows |Agentic AI|](https://www.youtube.com/watch?v=N_xtd1a4J5w) — *Tech Guy*, 17/11 04:30
  > Cours complet pour débutants sur la création d’agents IA avec n8n, incluant la construction de workflows d’automatisation.
- [MCP vs A2A Explained in 60 Seconds! | AI Agent Protocols](https://www.youtube.com/watch?v=4ClH4Mr3T5U) — *AIARCHITECTLAB*, 17/11 01:58
  > Explication concise des différences entre le protocole MCP et le protocole A2A, et quand les utiliser pour les agents IA.
- [AI Coding Agents: Planner, Coder, Reviewer](https://www.youtube.com/watch?v=haQudCfdFXo) — *NeilX Tech*, 17/11 01:00
  > Illustration du fonctionnement d’une équipe d’agents IA composée d’un planificateur, d’un codeur et d’un relecteur pour créer un logiciel.
- [Why 90% of AI Agents Fail (And How to Build One That Works)](https://www.youtube.com/watch?v=26XzIA3-IPM) — *Code Camp*, 16/11 22:00
  > Tutoriel détaillé montrant comment construire un agent IA fonctionnel en 10 minutes, en suivant un processus pas à pas.
- [How Claude Code Works: Context, Tools and the Agent Loop | Claude Code for QA Leads #02](https://www.youtube.com/watch?v=5JAPvdRjIhY) — *AI Test Automation Hub*, 16/11 19:35
  > Décomposition du fonctionnement de Claude Code : gestion du contexte, outils et boucle d’agent, destiné aux responsables QA.
- [How to Connect Your API to AI Tools Using MCP & OpenAPI | Octri.dev](https://www.youtube.com/watch?v=G2bIr_TVoHs) — *Octri Dev*, 16/11 16:19
  > Guide pas à pas pour connecter une API aux outils IA via MCP et OpenAPI, avec démonstration sur Octri.dev.

## Podcasts à écouter (9)

- [Prime Agent + V4 Flash,Claude,Codex: This is OPEN and TECHNICALLY the BEST AGENT HARNESS YET!](https://podcasts.apple.com/us/podcast/prime-agent-v4-flash-claude-codex-this-is-open-and/id6826122006?i=1000801829594&uo=4) — *AICodeKing*, 17/11 08:28
  > Présentation du nouvel agent open-source le plus performant à ce jour, incluant Prime Agent et V4 Flash, ainsi que les modèles Claude et Codex.
- [FREE Mode Coder: This is LITERALLY $0 - NO SUBSCRIPTION FREE CODER!](https://podcasts.apple.com/us/podcast/free-mode-coder-this-is-literally-%240-no-subscription/id6826122006?i=1000797739903&uo=4) — *AICodeKing*, 17/11 08:00
  > Annonce d'un mode de codage gratuit sans abonnement, offrant un environnement de développement IA à zéro coût.
- [Building Visual Intelligence — Andreas Blattmann & Dustin Podell, Black Forest Labs](https://podcasts.apple.com/us/podcast/building-visual-intelligence-andreas-blattmann-dustin/id1674008350?i=1000802354527&uo=4) — *Latent Space: The AI Engineer Podcast*, 16/11 22:27
  > Discussion sur l'apprentissage visuel des modèles IA en combinant vidéo, images et audio, avec le projet FLUX 3 de Black Forest Labs.
- [AI Infrastructure Crisis: Why Billions Can't Fix Everything](https://podcasts.apple.com/us/podcast/ai-infrastructure-crisis-why-billions-cant-fix-everything/id1794862407?i=1000802347389&uo=4) — *TechDaily.ai*, 16/11 22:00
  > Analyse de la crise d'infrastructure IA : pourquoi des milliards d'investissements ne suffisent pas face aux contraintes physiques, réglementaires et humaines.
- [Ep 7 · Daily Brief: Monday, November 16, 2026](https://podcasts.apple.com/us/podcast/ep-7-daily-brief-monday-november-16-2026/id6834673859?i=1000802343989&uo=4) — *ACN · AI Coding News*, 16/11 21:12
  > Brief quotidien sur les dernières menaces de sécurité IA, incluant la réduction du délai de divulgation d'Anthropic et les outils de hacking IA signalés par le FBI.
- [AI agents already get jobs and money. Where this leads in a few years and how to prepare](https://podcasts.apple.com/us/podcast/ai-agents-already-get-jobs-and-money-where-this-leads/id6810117720?i=1000802288704&uo=4) — *AI Agents & Vibe Coding*, 16/11 15:51
  > Examen de l'impact actuel des agents IA sur l'emploi et les perspectives futures, avec des conseils pour préparer les projets d'agents.
- [AI agents can now pay, OpenAI says. Will your checkout turn them away? Plus a Gemini Gems deadline](https://podcasts.apple.com/us/podcast/ai-agents-can-now-pay-openai-says-will-your-checkout/id6790021778?i=1000802270672&uo=4) — *AI Industry Report*, 16/11 14:00
  > Annonce d'agents IA capables de payer, et discussion des implications pour les systèmes de paiement ainsi que des nouveautés Gemini Gems.
- [Qwen4-Max lands, LongCat-2.5 goes open — AI News Nov 16](https://podcasts.apple.com/us/podcast/qwen4-max-lands-longcat-2-5-goes-open-ai-news-nov-16/id6817748791?i=1000802260637&uo=4) — *AI Engineering Briefing: Daily AI News for Software Engineers*, 16/11 12:37
  > Lancement officiel de Qwen4‑Max (2,4 T paramètres, 1 M de contexte) et mise à disposition des poids de LongCat‑2.5 sous licence MIT.
- [Writing Code Was Never the Bottleneck | CloudBees CEO Moritz Plassnig](https://podcasts.apple.com/us/podcast/writing-code-was-never-the-bottleneck-cloudbees-ceo/id1776879655?i=1000802253865&uo=4) — *Chain of Thought | AI Agents, Infrastructure & Engineering*, 16/11 12:05
  > Entretien avec le CEO de CloudBees sur le coût des tokens IA pour les entreprises et l'optimisation du cycle de développement logiciel.

## Écartés comme hors sujet (26)

- [AMD’s Scott Tease says high-precision HPC will outlast the AI surge](https://news.lavx.hu/article/amd-s-scott-tease-says-high-precision-hpc-will-outlast-the-ai-surge) — *news.lavx.hu*, 17/11 07:33
  > AMD’s Scott Tease argues that supercomputing will keep depending on double-precision math as AI spreads, and that the next generation of research systems will combine HPC, AI, and quantum hardware in one fleet. AMD, IBM, and Oak Ridge National Laboratory are testing that model now.
- [Quoting Go Proverbs](https://simonwillison.net/2026/Nov/17/go-proverbs/) — *Simon Willison*, 17/11 07:16
  > A little copying is better than a little dependency. — Go Proverbs , via Tags: go , programming
- [Nvidia Implications on Supply Chains](https://itbrief.com.au/story/nvidia-implications-on-supply-chains) — *IT Brief Australia*, 17/11 05:57
  > Supply constraints and tighter scrutiny could hit lead times, pricing and order fulfilment across the AI chip market if disruptions persist.
- [Google warns of autonomous AI attacks finding flaws](https://itbrief.com.au/story/google-warns-of-autonomous-ai-attacks-finding-flaws) — *IT Brief Australia*, 17/11 05:53
  > Attackers are compressing intrusion timelines to minutes as autonomous AI systems identify flaws and draft exploits without human help.
- [Aschenbrenner's Situational Awareness rebuilds AI stock bets as holdings slide](https://news.lavx.hu/article/aschenbrenner-s-situational-awareness-rebuilds-ai-stock-bets-as-holdings-slide) — *news.lavx.hu*, 17/11 05:33
  > Leopold Aschenbrenner's AI-themed hedge fund returned to public markets with a concentrated book of AI-linked stocks and options after nearly collapsing in July. Every holding has lost value since the end of September, according to its latest 13F filing.
- [US extends AI chip export limits to five more countries in Asia and Brazil](https://news.lavx.hu/article/us-extends-ai-chip-export-limits-to-five-more-countries-in-asia-and-brazil) — *news.lavx.hu*, 17/11 05:30
  > The Commerce Department's export regulator bans remote access to certain GPUs in datacenters in Indonesia, Malaysia, Singapore, Thailand and Brazil, and requires licenses for advanced AI chip sales there. Cloud operators must now prove their compute isn't reaching embargoed nations.
- [Ascendion named Leader in ISG's AI services reports](https://itbrief.com.au/story/ascendion-named-leader-in-isg-s-ai-services-reports) — *IT Brief Australia*, 17/11 04:15
  > The recognition strengthens Ascendion's pitch that enterprise AI needs governance and controls to move from pilots into production use.
- [TCS study finds AI productivity gains but trust gap](https://itbrief.com.au/story/tcs-study-finds-ai-productivity-gains-but-trust-gap) — *IT Brief Australia*, 17/11 04:15
  > Despite widespread productivity gains, most firms remain unwilling to let AI act independently, as security and governance concerns slow deployment.
- [OpenAI CFO sees Anthropic IPO as beneficial for future valuation](https://cryptobriefing.com/openai-cfo-sees-anthropic-ipo-as-beneficial-for-future-valuation/) — *Crypto Briefing*, 17/11 03:02
  > Anthropic's IPO could set a valuation benchmark, influencing OpenAI's strategic decisions and market perceptions for its future public offering. The post OpenAI CFO sees Anthropic IPO as beneficial for future valuation appeared first on Crypto Briefing .
- [OpenAI CFO Sarah Friar says a raise at a $1.25T valuation wasn’t planned](https://cryptobriefing.com/openai-cfo-sarah-friar-says-a-raise-at-a-125t-valuation-wasnt-planned/) — *Crypto Briefing*, 17/11 02:42
  > OpenAI's unplanned fundraising highlights strong investor demand, suggesting robust future market prospects despite cooling AI sentiment. The post OpenAI CFO Sarah Friar says a raise at a $1.25T valuation wasn’t planned appeared first on Crypto Briefing .
- [Treasury, NSC bypass Commerce to restrict Chinese AI-chip access](https://cryptobriefing.com/treasury-nsc-bypass-commerce-to-restrict-chinese-ai-chip-access/) — *Crypto Briefing*, 17/11 02:09
  > The bypass of Commerce in restricting Chinese AI-chip access may signal internal U.S. policy discord, affecting market stability perceptions. The post Treasury, NSC bypass Commerce to restrict Chinese AI-chip access appeared first on Crypto Briefing .
- [Strengthening NATO and allied cyber defenses with AI](https://openai.com/index/strengthening-nato-allied-cyber-defences-ai) — *OpenAI*, 17/11 01:00
  > How OpenAI is working with NATO and allied cyber agencies to help trusted defenders find vulnerabilities, test fixes and protect essential systems.
- [Google warns that fully automated cyberattacks have arrived and will get worse fast](https://the-decoder.com/google-warns-that-fully-automated-cyberattacks-have-arrived-and-will-get-worse-fast/) — *The Decoder*, 16/11 20:42
  > Google's Threat Intelligence Group has for the first time caught attackers finding and exploiting security vulnerabilities with no human involvement at all. An AI framework called "exploit_agent," found on an exposed server, automatically compared code before and after patches, built exploits, and r
- [OpenAI's GPT-6 Astra tackles the Standard Model's toughest math problem on a lattice](https://the-decoder.com/openais-gpt-6-astra-tackles-the-standard-models-toughest-math-problem-on-a-lattice/) — *The Decoder*, 16/11 20:19
  > OpenAI physicist Nathaniel Craig used GPT-6 Astra to tackle a problem that had stumped particle physicists for over 25 years. The AI model took Craig's strategy for defining the full Standard Model on a computational lattice and turned it into a working proof. Craig says a lot of work remains before
- [Moonshot AI pivots Kimi models from coding to science as benchmark gains flatten](https://the-decoder.com/moonshot-ai-pivots-kimi-models-from-coding-to-science-as-benchmark-gains-flatten/) — *The Decoder*, 16/11 19:52
  > Moonshot AI is done chasing coding benchmarks, it says. The Beijing startup is pivoting its Kimi language models toward biology, chemistry, and pharma research, arguing that science demands smarter AI than law, finance, or code. The article Moonshot AI pivots Kimi models from coding to science as be
- [Alibaba's Qwen4-Max takes on Opus 5.5, GPT-6, and Kimi K3.1 Pro at much lower prices](https://the-decoder.com/alibabas-qwen4-max-takes-on-opus-5-5-gpt-6-and-kimi-k3-1-pro-at-much-lower-prices/) — *The Decoder*, 16/11 17:56
  > Alibaba launches Qwen4-Max, a new flagship model with 2.4 trillion parameters that activates only 71 billion per token. A hybrid architecture sharply cuts costs on long contexts. Qwen4-Max lands just behind Kimi K3.1 Pro on the Artificial Analysis Intelligence Index, and Alibaba plans to release sma
- [After 10 Heads in a Row, Small LLMs Bet Up to 82% on an 11th](https://towardsdatascience.com/after-10-heads-in-a-row-small-llms-bet-up-to-82-on-an-11th/) — *Towards Data Science*, 16/11 17:30
  > Telling eight base and instruction-tuned open models that the coin is fair and the flips are independent trims their streak bias by only a few points. The post After 10 Heads in a Row, Small LLMs Bet Up to 82% on an 11th appeared first on Towards Data Science .
- [Why Human in the Loop AI Oversight Fails and How to Fix It](https://towardsdatascience.com/why-human-in-the-loop-ai-oversight-fails-and-how-to-fix-it/) — *Towards Data Science*, 16/11 16:00
  > Kahneman's System 1 and System 2, plus the ODPS, ODCS, and Ossie standards, show how to wake reviewers up only when a check fails. The post Why Human in the Loop AI Oversight Fails and How to Fix It appeared first on Towards Data Science .
- [Dreamteam Raises $53M Led by Accel to Rebuild the $100B CRM Market Around AI Teammates](https://hackernoon.com/dreamteam-raises-$53m-led-by-accel-to-rebuild-the-$100b-crm-market-around-ai-teammates?source=rss) — *HackerNoon*, 16/11 15:22
  > Dreamteam raises $53M led by Accel to build an AI-native CRM that learns from every customer conversation and puts AI teammates to work on deals.
- [How to Avoid AI Replacement as an Analytics Professional in 2027](https://towardsdatascience.com/how-to-avoid-ai-replacement-as-an-analytics-professional-in-2027/) — *Towards Data Science*, 16/11 14:30
  > Lessons from manufacturing and logistics projects: follow data from input to output, then turn vague requests into deterministic tools teams trust. The post How to Avoid AI Replacement as an Analytics Professional in 2027 appeared first on Towards Data Science .
- [Science at the Frontier: How scientists use ChatGPT](https://openai.com/index/science-at-the-frontier) — *OpenAI*, 16/11 13:00
  > Explore how more than 1,800 scientists use ChatGPT in research. See findings on daily workflows, reported productivity, and expectations for discovery.
- [Local LLMs Handle Textbook RAG but Fail on New Research Papers](https://towardsdatascience.com/local-llms-handle-textbook-rag-but-fail-on-new-research-papers/) — *Towards Data Science*, 16/11 13:00
  > Five setups, one blind grading pack: textbook scores ran 12 to 20 of 20, but a paper published this year dropped them to 0 to 9 of 15. The post Local LLMs Handle Textbook RAG but Fail on New Research Papers appeared first on Towards Data Science .
- [LinkedIn s’attaque enfin aux commentaires générés par IA](https://www.blogdumoderateur.com/linkedin-commentaires-generes-ia/) — *Blog du Modérateur*, 16/11 10:31
  > LinkedIn étend sa lutte contre l’AI slop aux commentaires. Les réponses génériques perdent en visibilité, et les créateurs ne reçoivent plus que les notifications des commentaires de qualité.
- [How AI is warping both developers and developer tools](https://www.infoworld.com/article/4247952/how-ai-is-warping-both-developers-and-developer-tools.html) — *InfoWorld*, 16/11 10:00
  > By now you’ve no doubt heard of the ArtCraft software collection , where a group of developers used AI-powered software development tools to build feature-exact clones of the Adobe Creative Suite — and the Microsoft Office suite, and the AutoDesk CAD applications, and the list goes on. But for me th
- [How AI agents are changing the rules of software governance](https://www.infoworld.com/article/4248100/how-ai-agents-are-changing-the-rules-of-software-governance.html) — *InfoWorld*, 16/11 10:00
  > The conversation around AI governance is already happening. Organizations have spent the past few years accelerating AI adoption across software development. Now they face a different problem. AI systems can act faster than the organizations responsible for them can understand or govern what is happ
- [Agents are users, so your software needs evals](https://vercel.com/blog/agent-evals) — *Vercel*, 16/11 06:00
