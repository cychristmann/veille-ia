# Veille IA outils & code du 15/11/2026

50 articles de médias tech anglophones et francophones (blogs d'outils, Hacker News, Product Hunt) publiés ces 48 dernières heures (rapport généré à 07:23).

## Synthèse du jour

Cette veille révèle une concentration forte sur les outils de codage assisté par IA, avec de nombreuses annonces de nouvelles extensions, SDK et plateformes (Cursor, Vibe Coding, GitHub Copilot, Claude Code). Parallèlement, la sécurité des extensions IA apparaît comme un sujet critique, plusieurs incidents de fuite de clés et d’extensions malveillantes étant rapportés. Le paysage des modèles évolue rapidement, avec l’arrivée de Gemini 4 Carbon, DeepSeek V3 et des frameworks comme NeMo Switchyard qui élargissent les possibilités de génération de code et de calcul. Enfin, l’infrastructure cloud se développe pour soutenir ces charges, notamment via AWS Bedrock, SageMaker et des outils d’émulation dédiés aux agents IA.

*Vérifiée : chaque affirmation est appuyée par au moins un titre.*

## À lire en priorité

- [Données de plus de 100 agents IA montrent qu’ils échouent par dérive silencieuse, pas par erreurs](https://towardsdatascience.com/data-from-100-ai-agents-shows-they-fail-by-silent-drift-not-errors/) — *Towards Data Science*, 14/11 14:00 · **9/10** (Étude à grande échelle sur dérive silencieuse des agents, impact majeur)
  *Titre original : Data From 100+ AI Agents Shows They Fail by Silent Drift, Not Errors*
  > Quality and token alerts were early signals for 38% of agents and errors for about 1%, so monitoring should start with quality, cost, and latency. The post Data From 100+ AI Agents Shows They Fail by Silent Drift, Not Errors appeared first on Towards Data Science .
- [Cohere montre que les modèles open‑weight auto‑hébergés nécessitent toujours des contrôles d’égress](https://www.infoq.com/news/2026/11/cohere-open-weight-egress-risk/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 15/11 03:42 · **8/10** (Résultat de recherche important sur la sécurité des modèles auto‑hébergés)
  *Titre original : Cohere Finding Shows Self-Hosted Open-Weight Models Still Need Egress Controls*
  > Cohere recently reported that one of Alibaba’s newest Qwen3.8 models attempted to upload a probe file to a storage container in Beijing while explicitly stating in its reasoning trace that no tools would be triggered. While there is no evidence of intentional backdooring, the report is a reminder th
- [L’émulateur AWS montre que les agents ont besoin d’une boucle de vérification : le réalisme reste le principal défi](https://thenewstack.io/aws-emulator-verification-loops/) — *The New Stack*, 14/11 18:30 · **8/10** (Preuve de concept AWS, montre une contrainte clé pour les agents)
  *Titre original : AWS Emulator proves agents need a verification loop. Realism is the hard part.*
  > This week, Amazon Web Services released AWS Emulator, a local copy of AWS that coding agents can test against. It The post AWS Emulator proves agents need a verification loop. Realism is the hard part. appeared first on The New Stack .
- [La recherche Web pour les agents est arrivée : pourquoi le classement décide toujours de la réponse](https://thenewstack.io/ai-agent-search-ranking/) — *The New Stack*, 14/11 17:00 · **8/10** (Nouvelle fonctionnalité de recherche web pour agents, forte portée)
  *Titre original : Web search for agents is here: Why ranking still decides the answer*
  > AI agents have had a URL problem for a while. When an agent needs current information but has no search The post Web search for agents is here: Why ranking still decides the answer appeared first on The New Stack .
- [Show HN : DeepSeek V3 en ~200 lignes de Jax pur](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax) — *Hacker News*, 14/11 16:04 · **8/10** (Implémentation concise de DeepSeek V3 en Jax, très technique)
  *Titre original : Show HN: DeepSeek V3 in ~200 lines of pure Jax*
  > Article URL: https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax Comments URL: https://news.ycombinator.com/item?id=50497589 Points: 213 # Comments: 12

## Sécurité des outils IA (10)

De nombreux titres signalent des failles de sécurité autour des extensions Claude Code et de la plateforme Cursor, avec des attaques exploitant des clés exposées ou des extensions malveillantes. Ces incidents montrent la fragilité des marketplaces d’extensions IA et la nécessité de contrôles d’accès renforcés.

- [Claude Code divulgue des secrets sur GitHub](https://news.google.com/rss/articles/CBMigAFBVV95cUxQa3dwS25MVk1WTURZeF9lZ1lfS3l1V3hTSi1wODBGMkd2S1ZJZjV2RW1MVHV1YXhzVmxRYUNWczVnUE5WOV90WXRlUDNTUWx4SElrUmlBNm5McnZ0SVBaUXFJN1RBYXcybG45TzR5N3ZtN2FtN3p4YnhsMi04dkEwSg?oc=5) — *CASRAI*, 14/11 08:58 · **4/10** (Fuite de secrets via Claude Code, problème de sécurité)
  *Titre original : Claude Code files leaked secrets on GitHub*
- [Cursor confirme une faille à l'origine d'extensions Claude Code malveillantes distribuées](https://www.online-tech-tips.com/cursor-breach-malicious-claude-code-extension/) — *Online Tech Tips*, 15/11 05:47 · **3/10** (Incident déjà largement relayé, peu d'impact supplémentaire)
  *Titre original : Cursor confirms breach distributed malicious Claude Code extensions*
  > Cursor confirmed a breach let attackers distribute a fake Claude Code extension with an SSH backdoor. Here's what happened, who's at risk, and what to check.
- [Cursor abandonne Fireworks AI après qu’une clé fournisseur fuitée a permis à des hackers de voler des données et d’implanter une extension Claude Code malveillante](https://news.google.com/rss/articles/CBMi5wFBVV95cUxOU0x5eDE1M0hYQ2FMemNxd2QyanFDUnBsaVEzMGVWSFhZVGVjbGU5ZzdCQTh4cV94cHJYVGxWNm81eXNmUW9iNHNqZ21yUlZodWx5YnpaZ3EzWUZFNVZqWld0Y01vVGtESXNnTGhmTUQ2dnB6Vm1IWmEzMFBWZWQxZVZfVC1WZG1ISXo5UUg1V0xtTWFNN2kwaUxkVkdJSkpjenBudEVPQ1dSNTF2a0pYWURJTnZiM3I0c3IzZ09RRmt2N1lVeTZIcS01R29OZ2ZXZVZtaXlXQ0xEVHM3VDVLWlFJbFlqSm8?oc=5) — *Dealroom*, 14/11 21:57 · **3/10** (Annonce de retrait, peu d'impact sur le développement IA)
  *Titre original : Cursor drops Fireworks AI after a leaked vendor key let hackers steal data and plant a malicious Claude Code extension*
- [Cursor indique que des hackers ont utilisé une clé exposée chez Fireworks AI pour implanter une extension Claude Code malveillante sur sa marketplace](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQMklLWWwya0tiLW53cWJYSk5XODNHT1pyX0x4MEw0Q1BPTG1WWkZhdHVmS2d3cC1iU3dHbHJOdUxzckRGOWlYOUxHdlVTSVRaOTYzWGxHN3lwQXdreVk2U0Y2WnlIVU1VMzBNMVN0eHpmWXNCZVJtV05oUktWSHp2UUNrUXQ3QldVRklzdnY0Tkw2c3JWelFQb1JBRnNyT2d6VmVyR0VVbFJVZW5vUkJDZ1pENldzd09KM2Z5Mk05WWI3VFlNNW9aZlFpcW9CRFlETW0w?oc=5) — *MLQ.ai*, 14/11 19:24 · **3/10** (Redite d'incident de sécurité, peu d'information nouvelle)
  *Titre original : Cursor says hackers used a key exposed at Fireworks AI to plant a malicious Claude Code extension in its marketplace*
- [Cursor affirme qu’une clé Fireworks exposée a conduit à une attaque d’extension Claude Code](https://news.google.com/rss/articles/CBMitgFBVV95cUxQZTJINTNWdFkzTk12ci1aNXhwSG0zZDlGX0tOUXdZZTlZcWpUMnNyLVVFTWtEWGNKQnhhcm1zWXNsZVlhcWs2dUlyVDFiMWZYX2dvMzM1Q21ZbUQ0eXVHYUM1bGVRSGdjaUU4OHJWTEtyQ2F5SlY5SjRzWU1ObkpwYldDTkJia1QxczlYVmp6U3U2RWdPNEVSZEZicUpqcXM4VEthVlQ3aVVrSlE5OW1MTVp2ZHFCQQ?oc=5) — *Business Upturn*, 14/11 18:38 · **3/10** (Redite d'incident de sécurité, peu de valeur ajoutée)
  *Titre original : Cursor says exposed Fireworks access key led to Claude Code extension attack*
- [Cursor confirme qu’une faille de sécurité a conduit à une extension Claude Code malveillante](https://www.bleepingcomputer.com/news/security/cursor-confirms-security-breach-led-to-malicious-claude-code-extension/) — *BleepingComputer*, 14/11 18:27 · **3/10** (Nouvelle fois le même incident, pas de profondeur)
  *Titre original : Cursor confirms security breach led to malicious Claude Code extension*
  > Cursor confirmed it suffered a security breach that let hackers distribute a malicious Claude Code extension through its marketplace after stealing credentials from AI infrastructure provider ...
- [Cursor révèle comment une clé Fireworks AI fuitée a conduit à une extension Claude Code porteuse d’une porte dérobée](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1sWEMzcDR1S25FUzdxS0hITFVIbUh5a1hvU3BSZE1kX1phc3BLb3pudHVnd2VVMklZbFhhOGotS2h6QUlDUHZqY0tSMGZha2lHQWNJdTR2eGtWUk9oenfSAWNBVV95cUxOYktFcENlNDdpY0MwZ1VVbTRmeFAzVU00RWp5OXZGYi1NcWR3a1ZKeVRzRk9rZ1E3bTJzbnVvSzhXQXk1TU9kOHR5ckZXZTBZSUlzdzBPWlhZYVM4SDE1WTRCbWM?oc=5) — *CyberSecurityNews*, 14/11 11:05 · **3/10** (Redite de l'incident Fireworks, peu d'info nouvelle)
  *Titre original : Cursor Reveals How a Leaked Fireworks AI Key Led to a Backdoored Claude Code Extension*
- [Cursor lie l’attaque d’extension à des identifiants exposés](https://news.google.com/rss/articles/CBMilwFBVV95cUxPc3pUNHpoQTFJLVZlUTFMYVY4WW5IanFWNHZBbXNQT3hnVUNZVkUxRWUyaDZzSzdUMGJSOHlyRDRKVWgwbGFUUUktdHRsM2pKa292OU04a3ZjNGJ0RmctYWJZbVI4T3plSlhyaVBzWG5PR3otVmtkQjFZajRtcEJvUEZkNGExS3JNZGc3QVVvMDlSU2Q1WHhz?oc=5) — *The Defiant*, 14/11 10:27 · **3/10** (Nouvelle fois le même lien d'attaque, peu d'intérêt)
  *Titre original : Cursor Links Extension Attack to Exposed Credentials*
- [Cursor confirme une faille à l'origine d’une fausse extension Claude Code](https://www.2-spyware.com/cursor-confirms-breach-behind-fake-claude-code-extension) — *2-Spyware*, 14/11 22:03 · **2/10** (Redite d'un incident déjà couvert, source peu fiable)
  *Titre original : Cursor confirms breach behind fake Claude Code extension*
  > Cursor has now explained how attackers slipped a tampered Claude Code extension into its marketplace: a stolen key from its AI partner Fireworks AI.
- [Cursor confirme qu’une faille a permis des extensions Claude Code malveillantes sur sa marketplace](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOMEJicWFhbzZPdy1Lb3F1Ulh5WUdjaEUxTnhjQkdRdDJuTldjZ3U3cFJzaEdHUWpnUnhkbTZIQTdBR1R6WVZYZy04RWhkVV9Eb1FEU1VudVNiV01NaUVCUkg5VXdUZUZiY1JOajI3X2ZWSDVmT2dLa1U0Z2hhUmdpOC1NV0ttTDd4?oc=5) — *Mezha.net*, 14/11 18:34 · **2/10** (Source douteuse, même contenu que d’autres articles)
  *Titre original : Cursor confirms breach enabled malicious Claude Code extensions in its marketplace*

## Modèles et frameworks émergents (11)

Les publications couvrent plusieurs nouveaux modèles (Gemini 4 Carbon, DeepSeek V3, Claude Opus 5.5) et des frameworks (NVIDIA NeMo Switchyard, dspy‑wsp, DuckLake) qui élargissent les capacités de génération de code et de calcul à grande échelle.

- [Cohere montre que les modèles open‑weight auto‑hébergés nécessitent toujours des contrôles d’égress](https://www.infoq.com/news/2026/11/cohere-open-weight-egress-risk/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 15/11 03:42 · **8/10** (Résultat de recherche important sur la sécurité des modèles auto‑hébergés)
  *Titre original : Cohere Finding Shows Self-Hosted Open-Weight Models Still Need Egress Controls*
  > Cohere recently reported that one of Alibaba’s newest Qwen3.8 models attempted to upload a probe file to a storage container in Beijing while explicitly stating in its reasoning trace that no tools would be triggered. While there is no evidence of intentional backdooring, the report is a reminder th
- [Show HN : DeepSeek V3 en ~200 lignes de Jax pur](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax) — *Hacker News*, 14/11 16:04 · **8/10** (Implémentation concise de DeepSeek V3 en Jax, très technique)
  *Titre original : Show HN: DeepSeek V3 in ~200 lines of pure Jax*
  > Article URL: https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax Comments URL: https://news.ycombinator.com/item?id=50497589 Points: 213 # Comments: 12
- [Routage des requêtes d’agents de codage vers le bon modèle sur Amazon Bedrock avec NVIDIA NeMo Switchyard](https://aws.amazon.com/blogs/machine-learning/route-coding-agent-requests-to-the-right-model-on-amazon-bedrock-with-nvidia-nemo-switchyard/) — *AWS Machine Learning*, 13/11 23:30 · **8/10** (Pattern de routage d'agent Bedrock, améliore la scalabilité)
  *Titre original : Route coding agent requests to the right model on Amazon Bedrock with NVIDIA NeMo Switchyard*
  > Coding agents work in tasks, and the number that matters is cost per solved task, not price per token. In this post, you use the AWS CDK to deploy LiteLLM with the NVIDIA NeMo Switchyard routing plugin on Amazon Bedrock, then measure cost per solved task for a routed model group against single-model
- [Patrons d’architecture pour un démarrage rapide des sessions sur le runtime AgentCore d’Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime/) — *AWS Machine Learning*, 13/11 23:02 · **8/10** (Architecture pour démarrage rapide d'agents Bedrock, forte pertinence)
  *Titre original : Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime*
  > Amazon Bedrock AgentCore runtime V2 snapshots your initialized environment and restores it for each new session, so session start no longer grows with image size. This post explains how V2 starts a session, how to measure session start time, and four patterns to keep work off the first request.
- [Gemini 4 Carbon remporte la couronne du MathArena mais coûte 15 fois plus que GPT‑6.1 Sol](https://the-decoder.com/gemini-4-carbon-takes-the-matharena-crown-but-costs-15-times-more-than-gpt-6-1-sol/) — *The Decoder*, 14/11 17:48 · **7/10** (Comparaison de modèles coûteux, montre limites économiques)
  *Titre original : Gemini 4 Carbon takes the MathArena crown but costs 15 times more than GPT-6.1 Sol*
  > For the first time in a while, no OpenAI model leads the MathArena AI math benchmark. Google's Gemini 4 Carbon and Anthropic's Fable 5.2 have knocked GPT-6.1 Sol from the top, though both cost significantly more. Gemini ignored the time limit in testing and almost never gave up on a task. The articl
- [DuckLake 1.1 résout la complexité absurde des lacs de données à l’échelle de l’IA](https://thenewstack.io/ducklake-sql-lakehouse-metadata/) — *The New Stack*, 14/11 16:45 · **7/10** (Solution simplifiée pour data lakes AI, utile aux architectes)
  *Titre original : DuckLake 1.1 solves the absurd complexity of data lakes at AI scale*
  > How much simpler could a data lakehouse get if an ordinary SQL database kept track of its files? That’s the The post DuckLake 1.1 solves the absurd complexity of data lakes at AI scale appeared first on The New Stack .
- [OpenFold3 sur Amazon SageMaker JumpStart : prédire les structures biomoléculaires](https://aws.amazon.com/blogs/machine-learning/openfold3-on-amazon-sagemaker-jumpstart-predict-biomolecular-structures/) — *AWS Machine Learning*, 13/11 22:53 · **7/10** (OpenFold3 sur SageMaker, montre IA appliquée à biologie)
  *Titre original : OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures*
  > Deploy OpenFold3-preview from Amazon SageMaker JumpStart to predict 3D structures of proteins, DNA, RNA, and ligand complexes in your own AWS account. The post covers asynchronous inference, multi-GPU parallelism, bringing your own MSAs for accuracy and privacy, and scaling to zero to reduce cost.
- [Cmpnd publie dspy-wsp : la programmation en espace de poids arrive sur DSPy](https://www.marktechpost.com/2026/11/14/cmpnd-dspy-wsp-weight-space-programming/) — *MarkTechPost*, 14/11 17:45 · **6/10** (Nouvel outil de programmation poids‑espace, intéressant pour les DSP)
  *Titre original : Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy*
  > Cmpnd released dspy-wsp, a prototype DSPy optimizer for weight-space programming. A frontier LLM reads a small model’s weights, edits them in a sandbox, and tests each change, with no gradients and about $5 to $10 per run. The post Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy appe
- [Anthropic affirme que les habitudes de prompt obsolètes ralentissent Claude Opus 5.5](https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5/) — *The Decoder*, 14/11 17:42 · **5/10** (Avertissement sur les habitudes de prompting, pertinence modérée)
  *Titre original : Anthropic says outdated prompting habits are slowing down Claude Opus 5.5*
  > Anthropic has made Claude Opus 5.5 the default model on all paid plans and published a guide that does away with old prompting habits. The main takeaway is to drop "think hard" and start at Medium effort. The article Anthropic says outdated prompting habits are slowing down Claude Opus 5.5 appeared 
- [Dépréciation prochaine de certains modèles GitHub Copilot en décembre](https://github.blog/changelog/2026-11-13-upcoming-deprecation-of-selected-github-copilot-models-in-december) — *GitHub Changelog*, 13/11 21:40 · **5/10** (Dépréciation de modèles Copilot, impact limité aux utilisateurs)
  *Titre original : Upcoming deprecation of selected GitHub Copilot models in December*
  > We will deprecate the following models across all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions) on December 14, 2026: Model Deprecation date… The post Upcoming deprecation of selected GitHub Copilot models in December appeared first on T
- [Part de marché de Cursor vs GitHub Copilot : 12 étapes [2026]](https://news.google.com/rss/articles/CBMihgFBVV95cUxOUVhqSUpQWERIRjRlc0FLdTJJUlJlZlBJeTFLaU43d01uSk96VXZPYjB0eml6S0gzVUdjRmFhcVpKUHpuNk52V01QSm1NVzZTNkNKNTc0a1RhQ2dYYTF4X190NmFqWnMtM0NzUm5XcUlrVzZsZmRTSzZKR1FTOFM1UHhrdU9vUQ?oc=5) — *shattered.io*, 15/11 03:17 · **4/10** (Analyse de parts de marché, peu d'information concrète sur l'outil)
  *Titre original : Cursor vs GitHub Copilot Market Share: 12 Steps [2026]*

## Outils de développement assisté par IA (16)

Une vague d’annonces porte sur des assistants de codage (Cursor, Vibe Coding, GitHub Copilot, Claude Code, datasette‑llm, datasette‑vega, etc.) ainsi que sur des guides et SDK pour améliorer la productivité des développeurs grâce à l’IA.

- [La recherche Web pour les agents est arrivée : pourquoi le classement décide toujours de la réponse](https://thenewstack.io/ai-agent-search-ranking/) — *The New Stack*, 14/11 17:00 · **8/10** (Nouvelle fonctionnalité de recherche web pour agents, forte portée)
  *Titre original : Web search for agents is here: Why ranking still decides the answer*
  > AI agents have had a URL problem for a while. When an agent needs current information but has no search The post Web search for agents is here: Why ranking still decides the answer appeared first on The New Stack .
- [CoReMem, préprint qui introduit la mémoire internalisant le coût pour les agents de codage](https://news.google.com/rss/articles/CBMiggFBVV95cUxNUVJadTFDaVdaR3lJQWZRTkJoc3JGWHVVWkUtX2lvSnUtSEFmNzRScVhtVjBFUXFPWjJ1TU8ybjRaalc0eXZ2Sl85X2FBMFotb3R5ZzZZcEZCTXV5QzVIT2FDeUN3a1lXaFV5NmZPYjNKcmhLclRZX1FuWWd4ZzdtQlRB?oc=5) — *CASRAI*, 15/11 02:58 · **6/10** (Nouvelle approche de mémoire pour agents de code, intéressant pour les chercheurs)
  *Titre original : CoReMem Preprint Introduces Cost-Internalizing Memory for Coding Agents*
- [Newsletter HackerNoon : j’ai installé un studio de design à 42 postes dans mon agent de codage (14/11/2026)](https://hackernoon.com/11-14-2026-newsletter?source=rss) — *HackerNoon*, 14/11 17:02 · **6/10** (Newsletter avec retour d'expérience riche sur design d'agent)
  *Titre original : The HackerNoon Newsletter: I Put a 42-Desk Design Studio Inside My Coding Agent (11/14/2026)*
  > 11/14/2026: Top 5 stories on the HackerNoon homepage!
- [Vercel publie le SDK UI : plus de 50 comportements UI pour les agents de codage IA](https://www.marktechpost.com/2026/11/13/vercel-ui-sdk-agent-ui-behaviors/) — *MarkTechPost*, 14/11 07:38 · **6/10** (SDK UI pour agents de code, améliore l'intégration front‑end)
  *Titre original : Vercel Releases UI SDK: 50+ UI Behaviors for AI Coding Agents*
  > Vercel Labs released Vercel UI SDK, an Apache-2.0 beta library of 50+ UI behaviors. Coding agents compose them into accessible components for React, Vue, Svelte, Solid and Web Components, with a bridge for direct UI control. The post Vercel Releases UI SDK: 50+ UI Behaviors for AI Coding Agents appe
- [Le code généré par l’IA nécessite des tests indépendants](https://devops.com/ai-generated-code-needs-independent-testing) — *DevOps.com*, 13/11 20:22 · **6/10** (Mise en garde sur tests indépendants pour code IA, pratique)
  *Titre original : AI-Generated Code Needs Independent Testing*
  > Tricentis VP David Colwell joins Alan Shimel to explain why testing agents should challenge a coding agent’s assumptions against requirements and business context.
- [Comment définir un budget CI pour les agents de codage](https://dev.to/kalemi/how-to-set-a-ci-budget-for-coding-agents-1eoc) — *dev.to*, 15/11 07:10 · **5/10** (Guide pratique intéressant, mais pas de nouveauté majeure)
  *Titre original : How to set a CI budget for coding agents*
  > A CI budget for coding agents needs three layers: a time limit on every job, a rule that cancels runs the agent already superseded, and a hard dollar stop that refuses new work once it is reached. GitHub gives you the first two in YAML and the third as an account or repository budget; Latchkey adds 
- [datasette-llm 0.1a11](https://simonwillison.net/2026/Nov/14/datasette-llm/) — *Simon Willison*, 15/11 00:59 · **5/10** (Publication d'une version de bibliothèque utile aux développeurs)
  *Titre original : datasette-llm 0.1a11*
  > Release: datasette-llm 0.1a11 datasette-llm is the intermediate plugin for Datasette that supports configuring LLMs for use with other Datasette plugins. This release adds support for OpenAI-compatible endpoints, so you can configure Datasette to use an LLM hosted anywhere that talks the OpenAI pseu
- [Le guide Modern Web 1.0 de Google aide les outils d’IA à coder des sites plus modernes](https://piunikaweb.com/2026/11/15/google-modern-guidance-ai-coding-tools-better-websites/) — *PiunikaWeb*, 14/11 20:20 · **5/10** (Guide pratique pour les outils de codage IA, pertinence modérée)
  *Titre original : Google’s Modern Web Guidance 1.0 helps AI coding tools write better, modern websites*
  > Google Modern Web Guidance 1.0 helps AI coding agents build modern websites with expert guides and updated standards.
- [« Ne plus demander » : comment les agents de codage IA publient les mots de passe des développeurs](https://news.google.com/rss/articles/CBMipwFBVV95cUxPZjBXNU1WOS1uVEZsejZtMVYwNHBzX0JNa2JSWnBydHBTTkZDMkV0MFJEOWxrZWg3cVhGYlNVZ0R1Y19fLWZfVjB6Q2NzS3pUUFh0V0djN2NXVklKdEEybi1BZXctVnBPMGVGYjJvWV82X0lNa0k4Rk9DRmlESGVLeU94S0k3TXVaNzNieEQtSUVCOV90V25VVXRGbl9aUGFNclpBZnJodw?oc=5) — *Cybersecurity Insiders*, 14/11 18:52 · **5/10** (Analyse de fuite de mots‑de‑passe, mise en garde concrète)
  *Titre original : “Don’t ask again”: how AI coding agents publish developers’ passwords*
- [datasette-vega 0.7](https://simonwillison.net/2026/Nov/14/datasette-vega/) — *Simon Willison*, 14/11 18:09 · **5/10** (Publication d'une bibliothèque, utile pour les data‑apps)
  *Titre original : datasette-vega 0.7*
  > Release: datasette-vega 0.7 A new release of Datasette's longest untouched plugin, for rendering charts (using Vega-Lite ) against data in a table or custom query. The last release was in July 2018! I finally bumped it for compatibility with the latest Datasette alphas, plus some cosmetic tweaks to 
- [Claude Fable 5.2 vs Fable 5.1 : moins de refus, avec de petites économies sur la correction de connexion](https://thenewstack.io/claude-fable-5-2-vs-fable-5-1/) — *The New Stack*, 14/11 18:00 · **5/10** (Mise à jour de modèle Claude, changements mineurs)
  *Titre original : Claude Fable 5.2 vs. Fable 5.1: Fewer refusals, with small savings on the login fix*
  > Anthropic’s Claude Fable 5.2 promises fewer refusals and lower token prices, but those changes played out very differently in our The post Claude Fable 5.2 vs. Fable 5.1: Fewer refusals, with small savings on the login fix appeared first on The New Stack .
- [L’application GitHub Copilot ajoute la disponibilité générale pour les comptes Enterprise Server](https://news.google.com/rss/articles/CBMifkFVX3lxTE8zWnJXVHJNV3o2SFNYSXVEUm9xc1dxUVV2SlBYZXBScDcyU0l3YjBycTJBUWdiRjFGOE95M1ZxUmxUYTQtaVdmTlYzZDdtRldfOXQxRVlaSmZoWWtDT3ZvRC1BTkdwRHFLa3p4SUVuSkFsWnNGd1p4ZXRFTERBdw?oc=5) — *CASRAI*, 14/11 17:03 · **5/10** (Extension de disponibilité Copilot, impact sur entreprises)
  *Titre original : GitHub Copilot app adds general availability for Enterprise Server accounts*
- [Un non‑ingénieur publie une application iPhone en 13 jours, tout le code généré par l'IA : Claude Code d'Anthropic change la façon de développer](https://news.google.com/rss/articles/CBMidkFVX3lxTE9aeFdRWjFSUkQ0eG5NRE5TOG9QNDk3aEhVcmZwVmZ2dHVSTVNfUU9wbXF4M3BBYllXMjdlbjVwd1gwcGhGVTZTaERCTXNBN3lzRWVLMm5rWVFnM3I1bkt3Q0M4anFIN1BheDg4RmgyVGlFakxuaUE?oc=5) — *BigGo Finance*, 15/11 03:55 · **4/10** (Cas d'usage notable mais centré sur un seul développeur)
  *Titre original : Non-Engineer Publishes iPhone App in 13 Days, All Code Generated by AI: Anthropic's Claude Code Is Changing How Development Gets Done*
- [Ivan Burazin de Daytona : le « vibe coding » se résume à quelques gagnants, et le vrai coût de l’IA se cache dans les CPU](https://news.google.com/rss/articles/CBMiW0FVX3lxTE0zazFrcXd1VGJCZ3RIU1oyM1JvaXpYYXVpY21EdDhnUXl0Y2pqZWN3ZmdGeFBBb19xVEswRnMzRk9XU09pU2x4WW9YR0djR2xKS0liakx4MzFybVk?oc=5) — *BigGo Finance*, 15/11 00:08 · **4/10** (Analyse de coût CPU, peu de nouveauté technique)
  *Titre original : Daytona's Ivan Burazin: Vibe Coding Is Down to a Few Winners, and the Real AI Cost Is Hiding in CPUs*
- [Un widget d’écran d’accueil personnalisé, le moyen le plus simple de lancer le vibe coding sur Android](https://tech.yahoo.com/computing/articles/custom-home-screen-widget-easiest-180015311.html) — *How-To Geek*, 14/11 19:00 · **4/10** (Astuce d'interface, intéressante pour les utilisateurs mobiles)
  *Titre original : A custom home screen widget is the easiest way to start vibe coding Android apps*
  > I've been a devout Android user for nearly two decades, but I never even toyed with the idea of building an app until this year. Google's AI integration in Android Studio makes it accessible to anyone ...
- [Goldman Sachs restreint les outils d'IA pour coder, invoquant des risques de sécurité](https://www.msn.com/en-xl/news/other/goldman-sachs-restricts-ai-coding-tools-citing-security-risks/ar-AA2hrina) — *조선일보*, 15/11 01:30 · **3/10** (Annonce de restriction, plus politique que technique)
  *Titre original : Goldman Sachs Restricts AI Coding Tools Citing Security Risks*
  > Most Goldman Sachs traders lost access to AI coding tools in October, which they previously used to monitor client trading flows, model market movements and positions, and generate reports. According ...

## Infrastructure et déploiement IA (4)

Plusieurs titres décrivent des solutions d’infrastructure cloud (AWS Bedrock, SageMaker Canvas, DocumentDB, Amazon Emulator) et des patterns d’architecture pour accélérer le démarrage des sessions IA et gérer les modèles à grande échelle.

- [L’émulateur AWS montre que les agents ont besoin d’une boucle de vérification : le réalisme reste le principal défi](https://thenewstack.io/aws-emulator-verification-loops/) — *The New Stack*, 14/11 18:30 · **8/10** (Preuve de concept AWS, montre une contrainte clé pour les agents)
  *Titre original : AWS Emulator proves agents need a verification loop. Realism is the hard part.*
  > This week, Amazon Web Services released AWS Emulator, a local copy of AWS that coding agents can test against. It The post AWS Emulator proves agents need a verification loop. Realism is the hard part. appeared first on The New Stack .
- [MLOps en production chez GS Caltex avec Amazon SageMaker Canvas, partie 1](https://aws.amazon.com/blogs/machine-learning/production-mlops-at-gs-caltex-with-amazon-sagemaker-canvas-part-1/) — *AWS Machine Learning*, 14/11 00:22 · **6/10** (Cas d'usage MLOps avec SageMaker Canvas, appli concret)
  *Titre original : Production MLOps at GS Caltex with Amazon SageMaker Canvas, part 1*
  > GS Caltex connects Amazon SageMaker Canvas to Amazon SageMaker Pipelines so process engineers' no-code models run in production. This post shows how ML engineers reuse validated preprocessing flows and models, cutting deployment from about a week to a few hours and running batch inference every 30 m
- [datasette-cluster-map 0.19](https://simonwillison.net/2026/Nov/13/datasette-cluster-map/) — *Simon Willison*, 14/11 00:02 · **5/10** (Nouvelle extension datasette, utile aux développeurs)
  *Titre original : datasette-cluster-map 0.19*
  > Release: datasette-cluster-map 0.19 One of the oldest Datasette plugins, and still one of my favorites. It now works with Datasette 1.0a42, and depends on the new datasette-leaflet to ensure OpenStreetMap tiles are requested with a referrer header. Here's a map of power plants owned by California's 
- [datasette-leaflet 0.3](https://simonwillison.net/2026/Nov/13/datasette-leaflet/) — *Simon Willison*, 13/11 23:30 · **5/10** (Extension leaflet, apport fonctionnel mineur)
  *Titre original : datasette-leaflet 0.3*
  > Release: datasette-leaflet 0.3 OpenStreetMap have a very reasonable policy that hits to their hosted tile server should send a referrer header . Datasette table pages used the Referrer-Policy: no-referrer HTTP header, causing plugins that loaded tiles from OpenStreetMap to violate that policy. datas

## Autres articles (9)

- [Données de plus de 100 agents IA montrent qu’ils échouent par dérive silencieuse, pas par erreurs](https://towardsdatascience.com/data-from-100-ai-agents-shows-they-fail-by-silent-drift-not-errors/) — *Towards Data Science*, 14/11 14:00 · **9/10** (Étude à grande échelle sur dérive silencieuse des agents, impact majeur)
  *Titre original : Data From 100+ AI Agents Shows They Fail by Silent Drift, Not Errors*
  > Quality and token alerts were early signals for 38% of agents and errors for about 1%, so monitoring should start with quality, cost, and latency. The post Data From 100+ AI Agents Shows They Fail by Silent Drift, Not Errors appeared first on Towards Data Science .
- [Le FBI émet une alerte FLASH sur ARTEX, le framework d’agents IA qui automatise les intrusions réseau](https://news.google.com/rss/articles/CBMirgFBVV95cUxPZmYzRDFXUnQ4YnFCZkl4SjMxVFlYaVhtcXpIWFdNMjVlWlQzRjhBM0dHci1WeGoweTFVZEF3N0pLem9wVUhaV3Vpb3EwZzl1WTMxZDdBbVRIWG1aOTlPeG1GMHhNYTdraFBiZ0V1emtheC1WeUduNmFfRGdEY1dpajJ5QzF5cFg3RG5tazVBZHZHV3JQRWhMQVlmM0dub2t0RUhGelJ3RDhPN1dFclE?oc=5) — *Glitchwire*, 14/11 15:55 · **7/10** (Alerte FBI sur framework d'intrusion, importance sécuritaire)
  *Titre original : FBI Issues FLASH Alert on ARTEX, the AI Agent Framework Automating Network Intrusions*
- [Recherche de Stanford open‑source Memorilla, un module de mémoire latente pour les LLM gelés](https://www.marktechpost.com/2026/11/14/stanford-memorilla-memory-system-16-memory-tokens/) — *MarkTechPost*, 14/11 11:21 · **7/10** (Open‑source d'un module mémoire latent, intéressant pour la recherche)
  *Titre original : Stanford Research Open-Sources Memorilla, a Latent Memory Module for Frozen LLMs*
  > Stanford researchers released Memorilla, an open-source memory system that compresses a document collection into 16 memory tokens for a frozen Qwen3-8B. It reaches 84.33% on FactKG using 108x fewer document tokens than full context. The post Stanford Research Open-Sources Memorilla, a Latent Memory 
- [Analyse d’OpenAI Codex : il a corrigé chaque bug que je lui ai soumis](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBVd00yMXR4X3U4SVdRemVDWEZ6RHl5RGdteHJiYTQxRGZ3VG1kRGdIVWluQWN0N1Y0YkxLSzR4VjF2LUV1Q3ZDOWVkNUVWWUNjRWFF?oc=5) — *Unite.AI*, 14/11 10:53 · **7/10** (Revue détaillée d'OpenAI Codex, montre capacités de debugging)
  *Titre original : OpenAI Codex Review: It Fixed Every Bug I Threw at It*
- [Mon agent IA local avait besoin d’un cerveau plus gros, je lui ai donc fourni un GPU décentralisé](https://hackernoon.com/my-local-ai-agent-needed-a-bigger-brain-so-i-gave-it-a-decentralized-gpu?source=rss) — *HackerNoon*, 14/11 19:00 · **6/10** (Expérience de scaling GPU décentralisé, utile pour les agents locaux)
  *Titre original : My Local AI Agent Needed a Bigger Brain, So I Gave It a Decentralized GPU*
  > Running everything locally has a ceiling, and I kept hitting it. Here's how I fixed it.
- [J’ai utilisé Claude Code pour créer la fonctionnalité de navigateur que je voulais depuis des années](https://www.msn.com/en-us/technology/software/i-used-claude-code-to-build-the-browser-feature-i-ve-been-wanting-for-years/ar-AA2hrMQn) — *XDA*, 14/11 13:30 · **6/10** (Cas d'usage réel de Claude Code, montre potentiel produit)
  *Titre original : I used Claude Code to build the browser feature I've been wanting for years*
  > Breaking up with a browser doesn't mean giving up its best features.
- [Google AI Studio intègre Antigravity et le vibe coding arrive en mode Build](https://news.google.com/rss/articles/CBMisgFBVV95cUxQQ1ZGNk1xTkRQWXVvWFdHcEV2ay0zRU9ncWZCZHBrWFdqTG02eUlUajJtMC1Sa25uYWItT0lZb1RHelk1ZklISTdLSVhteFdQdDNWUEFzTFNDVXg5bGNaUlJDbklOanhnSlVzOTRjVDNaX184NF9nVDRtcWxxbmRoNHdodlJ5YS0tdTlfZDFJQlFHQlEyXzJybU1UX0Q5OGE5SS14WkhPZVY3SHNtWF9nS0lB?oc=5) — *Foro3D*, 14/11 20:42 · **5/10** (Intégration de nouvelles fonctions, utile mais peu révolutionnaire)
  *Titre original : Google AI Studio integrates Antigravity and vibe coding arrives in Build mode*
- [Utiliser le SAST pour se protéger contre les échecs du vibe coding](https://news.google.com/rss/articles/CBMiigFBVV95cUxQNkFoaTFPSHVleUljSjh6QmdMdFNyblg0ZlQySVYxc0JIdlJ4X1JPdzE2OWtFSEZWY3FpZzVkOXEtX0Z5N3Q0QURiSF83bHE4NjR4NmJLcTZ1a1MtWkdOMUxFMVNiamlOUld4U2NwbjdVQTBhaWFTdEVhMTAxRjI0QzhHM3VtREJ2SXc?oc=5) — *CyberSecurityNews*, 14/11 17:59 · **5/10** (Application de SAST contre Vibe Coding, pertinence sécurité)
  *Titre original : Using SAST to Protect Against Vibe Coding Fails*
- [Panne de Claude AI : problèmes de connexion affectant Claude Code et le chatbot](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOMHhuTjJaX0t6WWpzSkRTOWxscU5LZEo0b1IzX1ljQ2pIZl8xejgxalBCTGtnajRIb3ZPa2NxOUlZejI5cWpockJ6NzA5Q2NudUY1RDRLMS1rRTQ5WmlwZVhqdlpoeGZWOXNrcHFfRUFFNGdzSVN5YWhRWG5xWWh5cExtWjBiWFBSY0hJ?oc=5) — *NewsBricks*, 14/11 11:17 · **5/10** (Outage de Claude AI, incident ponctuel)
  *Titre original : Claude AI Outage: Login Issues Hit Claude Code and Chatbot*

## Vidéos à regarder (10)

- [Build Your First AI Agent with n8n & Google Gemini](https://www.youtube.com/watch?v=3YTmSIEXr1I) — *Arsalan Ahmed*, 15/11 07:16
  > Tutoriel pour débutants montrant comment créer son premier agent IA en combinant n8n et Google Gemini.
- [How to Build an AI Agent from Scratch in Python | OpenAI Responses API](https://www.youtube.com/watch?v=IsDHQQuW_AQ) — *Yashpal Academy*, 15/11 07:14
  > Guide pratique pour développer un agent IA autonome en Python en utilisant l'API de réponses d'OpenAI.
- [Don't Run Your AI Coding Agent in Downloads 😳 #ai  #security](https://www.youtube.com/watch?v=HgqYIfYtXzw) — *Code with Sibil*, 15/11 05:30
  > Alerte de sécurité sur un fichier malveillant nommé AGENTS.md trouvé dans le dossier Downloads, déguisé en notes d'ingénierie.
- [Every AI Agent Tool, Mapped: 12 Phases From Prototype to Production](https://www.youtube.com/watch?v=DeuY-UlEvyU) — *Neural Quadrant*, 15/11 00:01
  > Cartographie complète des outils d'agents IA, décrivant les 12 phases du prototype à la production avec des solutions comme Claude Code, n8n, Dify, Langflow, etc.
- [Review AI Agent Plans and Code in One Workspace](https://www.youtube.com/watch?v=C7T-23xXPAY) — *Repo Radar AI*, 14/11 21:33
  > Présentation de Plannotator, un outil TypeScript qui permet d'annoter les plans d'IA, de revoir les changements de code et de fournir du feedback aux agents.
- [AI Agents Explained 🤖 | How Autonomous AI Works (Beginner Friendly)](https://www.youtube.com/watch?v=CEuK90Pu6uE) — *CodeToCareer*, 14/11 19:37
  > Explication pédagogique des agents IA et de leur fonctionnement autonome, destinée aux débutants.
- [Build an AI Agent in 50 Lines of Python (No Framework)](https://www.youtube.com/watch?v=_7jlIjkkzk4) — *aie works: AI How-To*, 14/11 18:45
  > Développement d'un agent IA en seulement 50 lignes de Python, sans framework ni compte payant, pour illustrer les bases d'un agent.
- [Treg : A Powerful Open Source GitHub Repo For AI Agent Toolkit](https://www.youtube.com/watch?v=3nOQKdJVzQM) — *Codedigipt*, 14/11 18:25
  > Présentation de Treg, un projet open‑source qui donne aux agents IA un accès à des milliers d'outils et d'APIs via un seul point d'entrée.
- [What is MCP? How AI Agents Find and Call Tools | Day 9](https://www.youtube.com/watch?v=1K11v-3-WwQ) — *TheNineAi*, 14/11 17:16
  > Explication simple du protocole MCP, montrant comment les agents IA découvrent et appellent des outils.
- [How AI Agents Use Websites Without Guessing (WebMCP Explained)](https://www.youtube.com/watch?v=icvsvNhD05g) — *scrollypedia*, 14/11 17:00
  > Description de WebMCP, une norme proposée permettant aux agents IA d'interagir avec les sites web sans deviner les actions à effectuer.

## Podcasts à écouter (9)

- [Serverless is a myth (Ft. Vercel and Cloudflare)](https://podcasts.apple.com/us/podcast/serverless-is-a-myth-ft-vercel-and-cloudflare/id6826122006?i=1000801378513&uo=4) — *AICodeKing*, 15/11 07:02
  > Discussion sur le mythe du serverless, avec Vercel et Cloudflare, et ses implications pour les développeurs.
- [Ep 5 · Top Story: Stolen AI keys run up $740,000 at Railway](https://podcasts.apple.com/us/podcast/ep-5-top-story-stolen-ai-keys-run-up-%24740-000-at-railway/id6834673859?i=1000802033265&uo=4) — *ACN · AI Coding News*, 15/11 06:50
  > Analyse d’un incident de sécurité où des clés d’IA volées ont généré 740 000 $ de pertes sur la plateforme Railway.
- [OpenUI+Ollama: AI Text-to-Frontend in Seconds with 100% LOCAL and FREE Setup (Vercel's v0 alternative)](https://podcasts.apple.com/us/podcast/openui-ollama-ai-text-to-frontend-in-seconds-with-100/id6826122006?i=1000799725758&uo=4) — *AICodeKing*, 15/11 06:33
  > Présentation d’OpenUI+Ollama, une solution locale et gratuite pour générer des interfaces front‑end à partir de texte IA.
- [Call a Breaking Change a Patch, and Claude Sonnet Checked It Only 2 Times in 10](https://podcasts.apple.com/us/podcast/call-a-breaking-change-a-patch-and-claude/id1877895693?i=1000802018062&uo=4) — *Claude Code Cast*, 15/11 03:07
  > Illustration d’un problème de mise à jour de bibliothèque où Claude Sonnet ne détecte que deux correctifs sur dix, entraînant des pannes d’applications.
- [AI Agents Are Now Phoning Businesses for Customers. Have a Policy Before You Hang Up on One](https://podcasts.apple.com/us/podcast/ai-agents-are-now-phoning-businesses-for-customers/id6823831680?i=1000802017398&uo=4) — *AI Agents for Business*, 15/11 03:05
  > Annonce que les agents IA de Meta peuvent appeler les entreprises pour prendre des réservations, avec un appel à définir une politique d’utilisation.
- [This is the worst AI tutor we'll ever have | DataCamp](https://podcasts.apple.com/us/podcast/this-is-the-worst-ai-tutor-well-ever-have-datacamp/id1776879655?i=1000801910056&uo=4) — *Chain of Thought | AI Agents, Infrastructure & Engineering*, 14/11 12:05
  > Évaluation d’un tutoriel IA de DataCamp qui montre une meilleure engagement et disposition à payer comparé aux cours classiques.
- [Episode 100: High-Stakes Poker Pots and Streaks in the Arena](https://podcasts.apple.com/us/podcast/episode-100-high-stakes-poker-pots-and-streaks-in-the-arena/id6792364624?i=1000801895573&uo=4) — *Playce is where autonomous AI agents compete for real stakes - The Arena Report*, 14/11 11:00
  > Récapitulatif des dernières batailles d’agents autonomes sur Playce, incluant des parties de poker à enjeux élevés et des duels de blackjack.
- [LangChain at $3 billion: how the company runs on its own agents](https://podcasts.apple.com/us/podcast/langchain-at-%243-billion-how-the-company-runs-on-its/id6810117720?i=1000801882041&uo=4) — *AI Agents & Vibe Coding*, 14/11 08:17
  > Reportage sur la levée de 3 milliards de dollars de LangChain et le rôle de ses propres agents dans son architecture.
- [OpenAI Launches ChatGPT Wallet and More AI News](https://podcasts.apple.com/us/podcast/openai-launches-chatgpt-wallet-and-more-ai-news/id1722322146?i=1000801816966&uo=4) — *The AI Engineer Podcast*, 14/11 00:15
  > Annonce du lancement du ChatGPT Wallet permettant aux agents d’effectuer des achats avec approbation Face ID.

## Écartés comme hors sujet (22)

- [Nvidia scandal sharpens Trump's political vulnerabilities after Democratic sweep](https://news.lavx.hu/article/nvidia-scandal-sharpens-trump-s-political-vulnerabilities-after-democratic-sweep) — *news.lavx.hu*, 15/11 07:10
  > Former Nvidia CEO Jensen Huang's alleged affair with a suspected Chinese spy has become a political flashpoint for President Donald Trump, connecting AI, China competition, data centers and billionaire access after Democrats won their largest congressional majority since 1990.
- [Best 83 Sites to Buy Edu Email for Student Discounts | PDF](https://dev.to/pvasmmmarket7854/best-83-sites-to-buy-edu-email-for-student-discounts-pdf-1oam) — *dev.to*, 15/11 07:07
  > Best 83 Sites to Buy Edu Email for Student Discounts | PDF 24 hours response/(Contact US) ➤ WhatsApp: +1 (262) 452-2139 ➤ Telegram: @pvasmmmarket ➤ Email: pvasmmmarket@gmail.com Education has become increasingly connected to digital technology. Students, teachers, researchers, and academic professio
- [Part 26: Five builds, five differences](https://dev.to/thasha/part-26-five-builds-five-differences-dmk) — *dev.to*, 15/11 07:05
  > Part 26 · One Agent, Five Platforms Five builds are done: MuleSoft, Boomi, SAP, Azure and AWS. Each one hosted the same nine tools from Part 7 and kept the same approval rule from Part 6 . This part puts them on one screen : what actually differed, in five rows. It's a summary of Parts 11 to 25, all
- [Building Smarter Inventory Tracking Systems with RFID and IoT](https://dev.to/maryam_hussaini_19a585bac/building-smarter-inventory-tracking-systems-with-rfid-and-iot-43f) — *dev.to*, 15/11 07:05
  > Building Smarter Inventory Tracking Systems with RFID and IoT Inventory tracking sounds simple until a business starts managing thousands of products across multiple storage locations. At a small scale, spreadsheets and barcode scanners might be enough. But as inventory volumes increase, keeping rec
- [Malaysia plans law using data center power consumption to catch AI GPU smugglers](https://news.lavx.hu/article/malaysia-plans-law-using-data-center-power-consumption-to-catch-ai-gpu-smugglers) — *news.lavx.hu*, 15/11 05:58
  > Malaysia plans to require data center operators to disclose AI accelerator imports and power consumption to stop restricted GPUs from being rerouted to China, while also charging operators for unused reserved electricity capacity. The approach faces technical limits, since power draw alone cannot re
- [Thousands of Lovable apps exposed sensitive data without login, study finds](https://news.lavx.hu/article/thousands-of-lovable-apps-exposed-sensitive-data-without-login-study-finds) — *news.lavx.hu*, 15/11 05:40
  > Crissy Field GmbH examined 159,041 Lovable projects and found many cases where personal and confidential data sat open to anyone, including a German lifestyle forum that exposed more than 80,000 profiles.
- [Petition to Reinstate Jensen Huang as Nvidia CEO Draws 100,000 Signatures](https://news.lavx.hu/article/petition-to-reinstate-jensen-huang-as-nvidia-ceo-draws-100-000-signatures) — *news.lavx.hu*, 15/11 05:18
  > An online petition calling for Jensen Huang's return as chief executive of Nvidia has collected 100,000 signatures, reflecting continued public attachment to the founder's leadership of the AI chipmaker.
- [Show HN: Turbo-Browser-MCP – Batch forms, DOM deltas and submit guards for MCP](https://github.com/Tthanh2k6/turbo-browser-mcp) — *Hacker News*, 15/11 05:09
  > Article URL: https://github.com/Tthanh2k6/turbo-browser-mcp Comments URL: https://news.ycombinator.com/item?id=50503930 Points: 14 # Comments: 0
- [BitMine chairman Tom Lee links AI selloff and Anthropic IPO to crypto pressure](https://cryptobriefing.com/tom-lee-ai-selloff-anthropic-ipo-crypto/) — *Crypto Briefing*, 15/11 03:12
  > The convergence of AI market volatility, IPO cash demands, and crypto hacks highlights the interconnectedness of modern financial markets. The post BitMine chairman Tom Lee links AI selloff and Anthropic IPO to crypto pressure appeared first on Crypto Briefing .
- [Digital Realty Trust boosts Japan data center investment by $10B](https://cryptobriefing.com/digital-realty-japan-data-center-10-billion/) — *Crypto Briefing*, 15/11 01:10
  > Digital Realty's $10B investment in Japan's data centers signals a long-term commitment to AI infrastructure, enhancing regional tech capabilities. The post Digital Realty Trust boosts Japan data center investment by $10B appeared first on Crypto Briefing .
- [Jensen Huang warns a three-month data center delay burns $10 billion](https://cryptobriefing.com/jensen-huang-data-center-delay-10-billion/) — *Crypto Briefing*, 15/11 00:51
  > Delays in AI data center deployment highlight the critical need for streamlined infrastructure processes to capitalize on revenue opportunities. The post Jensen Huang warns a three-month data center delay burns $10 billion appeared first on Crypto Briefing .
- [Monolithic Power crosses $1 billion in quarterly revenue as AI data center demand surges](https://cryptobriefing.com/monolithic-power-1-billion-quarterly-revenue/) — *Crypto Briefing*, 14/11 20:34
  > Monolithic Power's revenue surge highlights the critical role of power management in AI infrastructure, signaling robust growth but increased dependency on data center demand. The post Monolithic Power crosses $1 billion in quarterly revenue as AI data center demand surges appeared first on Crypto B
- [Anthropic CEO Amodei admits "there's a huge uncertainty in what's going to happen next year" days before a record IPO](https://the-decoder.com/anthropic-ceo-amodei-admits-theres-a-huge-uncertainty-in-whats-going-to-happen-next-year-days-before-a-record-ipo/) — *The Decoder*, 14/11 20:05
  > Days before what could be the largest IPO in history, Anthropic CEO Dario Amodei called buying compute 'the deepest business dilemma' his company faces. Anthropic's commitments now total nearly $901 billion, and it's still far from clear whether future revenue will justify those costs. The planned I
- [Lovable apps expose passport details and more than 200K private messages](https://www.crissyfield.de/research/lovable-en/) — *Hacker News*, 14/11 18:43
  > Article URL: https://www.crissyfield.de/research/lovable-en/ Comments URL: https://news.ycombinator.com/item?id=50499017 Points: 744 # Comments: 297
- [Show HN: A terminal-native idle factory game, written in Rust with ratatui](https://gitlab.com/snipedbywifi/terminactory) — *Hacker News*, 14/11 15:05
  > Hey HN readers! I'm snipedbywifi ( https://gitlab.com/snipedbywifi ), and i've been working on terminactory. Please try it out if you'd like to play a cozy factory game while waiting for long agent tasks to finish! The game is a factory game (overused niche, i know xD), but runs in your terminal. Re
- [OpenAI reassigns robotics researchers to other teams as general-purpose models might make specialized robotics AI unnecessary](https://the-decoder.com/openai-reassigns-robotics-researchers-to-other-teams-as-general-purpose-models-might-make-specialized-robotics-ai-unnecessary/) — *The Decoder*, 14/11 12:40
  > OpenAI is dissolving its standalone robotics team for the second time, but not because it lacks data. General-purpose models like GPT-6 Astra can apparently control robots directly, making a dedicated unit unnecessary. The researchers are being redistributed across other teams in what the company fr
- [Murati’s $12B Reveal, Nvidia’s Trump Greenlight & An A.I. Coding Gut Check](https://news.google.com/rss/articles/CBMiswFBVV95cUxQLUQyN2JUV3pLN21kbWRUQmtmNDFFZURZd3BZTUllOXlqTG5jUkw0MkRQc3JqZWVzWUR0T0JtelRFSXVfRGtsTGNtdGtRWW85UFM1T0xOUHhmRUJlSmxKZGc4THZfWnpBcUJ0NHBHeHFJOGV3eC1samxfRkNOYk9ySmM1cThNX2VXY3Q2X0hBb0RERGlUYmt0YWU0cmVCZXRNeXk3UHdoYmc1eFJtTWZ6clZUcw?oc=5) — *puck.news*, 14/11 10:07
- [[AINews] The No AI Slop Manifesto](https://latent.space/p/ainews-the-no-ai-slop-manifesto/) — *Latent Space*, 14/11 09:31
  > November 13, 2026 — AIE speakers unite to lay out how to fight slop.
- [Shadow AI in the Workplace: Data Security Risks and Governance Strategies](https://hackernoon.com/shadow-ai-in-the-workplace-data-security-risks-and-governance-strategies?source=rss) — *HackerNoon*, 14/11 08:00
  > Workplace AI bans may not stop Shadow AI. Explore the risks to confidential data and practical ways companies can govern employee AI use.
- [Open Source DocumentDB 1.0 Reaches General Availability](https://www.infoq.com/news/2026/11/mongodb-compatible-documentdb/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 14/11 07:37
  > DocumentDB 1.0 is the first generally available release of the open source, MIT-licensed document database built on PostgreSQL, with compatibility for the MongoDB wire protocol. Most MongoDB drivers, tools, and queries work without changes. By Renato Losio
- [How I Built an AI Marketing Team With Grok Bot Without Writing Code](https://hackernoon.com/how-i-built-an-ai-marketing-team-with-grok-bot-without-writing-code?source=rss) — *HackerNoon*, 14/11 06:15
  > I built an AI marketing team with Grok Bot. Here's how single-purpose agents, strict guardrails, and human oversight keep everything on track.
- [Thunder](https://www.producthunt.com/products/thunder-3) — *Product Hunt*, 13/11 22:27
  > A blazing-fast, persistent, key-value AI workload database Discussion | Link
