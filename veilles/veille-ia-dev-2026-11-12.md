# Veille IA outils & code du 12/11/2026

50 articles de médias tech anglophones et francophones (blogs d'outils, Hacker News, Product Hunt) publiés ces 48 dernières heures (rapport généré à 23:28).

## Synthèse du jour

La veille du jour montre une forte activité autour des agents de codage IA, avec de nouvelles fonctionnalités de collaboration et de changement dynamique de modèles. Le déploiement sur le cloud se diversifie grâce à des offres AWS dédiées et à des émulateurs locaux, tandis que les coûts d’inférence restent un sujet central, poussant les fournisseurs à proposer des outils de suivi et de plafonnement. La sécurité des pipelines et la gouvernance des agents sont également au cœur des préoccupations, notamment face aux incidents de vol de clés API. Enfin, les performances des modèles continuent de s’améliorer, avec Gemini 4 Hydrogen qui surpasse rapidement son prédécesseur, et de nouveaux frameworks comme LLMON élargissent les possibilités d’intégration.

*Vérifiée : 1 affirmation(s) non appuyée(s) par les titres ont été retirées ou atténuées :*
- « qui promettent de gagner jusqu’à 20 % de productivité » : Aucun titre ne mentionne un gain de 20 % de productivité ; le seul chiffre présent est une amélioration de 19 % plus rapide.

## À lire en priorité

- [Déployer des modèles d'IA de pointe sur AWS Trainium avec SGLang-Neuron](https://aws.amazon.com/blogs/machine-learning/deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron/) — *AWS Machine Learning*, 12/11 23:03 · **8/10** (Déploiement de modèles frontier sur AWS Trainium, forte portée)
  *Titre original : Deploy frontier AI models on AWS Trainium with SGLang-Neuron*
  > SGLang-Neuron is now publicly available through an AWS Deep Learning Container. With SGLang-Neuron, you can serve models and generate reinforcement learning rollouts with SGLang on AWS Trainium using the same SGLang interface you already know, all running on native PyTorch.
- [L'agent de codage Gemini 4 de Google change de modèle en cours de tâche et termine 19 % plus vite](https://thenewstack.io/gemini-4-hydrogen-orchestrator/) — *The New Stack*, 12/11 22:26 · **8/10** (Gemini 4 coding agent améliore vitesse, couvert par 2 médias)
  *Titre original : Google’s Gemini 4 coding agent now switches models mid-task — and finishes 19% faster*
  > Google launched Gemini 4 Hydrogen on Thursday alongside a new system that changes how coding agents use AI models. Rather The post Google’s Gemini 4 coding agent now switches models mid-task — and finishes 19% faster appeared first on The New Stack .
- [Des hackers ciblent les outils de codage IA pour voler des identifiants, 103 incidents cyber liés à l’IA révélés par des chercheurs](https://news.google.com/rss/articles/CBMibkFVX3lxTE1nd2JPMzhvS0NnSHZjbjVzcE9DdjBhS3NZaF95RmU0bmZmNmY5T1VSR1U5N3lEaFY4TmZXV2s1cmxQUHRHT0hVSDA5RER2T1dTODdmd0FuODFvTkJ1UUY3eXdBQ05BS3Q4OTJ4LWVB0gFzQVVfeXFMTzhyVlZKWEswZVNsUjlVTWRHUm5Kb0gzbmFoN0YxSGtjUkRGZDdOSG10NkZpVU44RFJ5UnhVZHo3cWxQUzg0UmpIaXpYLWxIWUdCeXJNY3ozY18xNm14LXlteGVmelZodlFPNHhwbmF1N0tDcw?oc=5) — *CyberSecurityNews*, 12/11 13:27 · **8/10** (Cyber‑incidents liés aux outils IA, impact majeur sur sécurité)
  *Titre original : Hackers Target AI Coding Tools to Steal Credentials as Researchers Uncover 103 AI-Linked Cyber Incidents*
- [Comment Natera a conçu un système d'IA agentique pour les opérations de laboratoire avec Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/how-natera-designed-an-agentic-ai-system-for-lab-ops-with-amazon-bedrock-agentcore/) — *AWS Machine Learning*, 12/11 22:47 · **7/10** (Cas d'usage concret d'agent IA sur Bedrock, pertinent)
  *Titre original : How Natera designed an agentic AI system for lab ops with Amazon Bedrock AgentCore*
  > Natera built SWARM, an agentic AI system on Amazon Bedrock AgentCore that captures institutional lab-operations knowledge and deploys it at scale. This post walks through the full architecture, from knowledge base construction to deployment and evaluation, delivering about 130x faster first response
- [CopilotKit lance OpenBot 1.0 : un collègue IA auto-hébergeable sous licence MIT avec gouvernance intégrée](https://www.marktechpost.com/2026/11/12/copilotkit-openbot-1-0-open-source-ai-coworker/) — *MarkTechPost*, 12/11 22:45 · **7/10** (Release d'OpenBot 1.0, outil auto‑hébergé avec gouvernance)
  *Titre original : CopilotKit Releases OpenBot 1.0: An MIT-Licensed, Self-Hostable AI Coworker With Built-In Governance*
  > CopilotKit released OpenBot 1.0, an MIT-licensed, self-hostable AI coworker workspace. Companies bring their own agents, models and infrastructure, while every Bot action passes a policy check and lands in an audit trail. The post CopilotKit Releases OpenBot 1.0: An MIT-Licensed, Self-Hostable AI Co

## Agents et assistants de codage IA (23)

De nombreux articles présentent des agents ou assistants IA destinés à assister les développeurs dans l’écriture, le test et le déploiement de code, que ce soit Claude Code, Gemini 4, CopilotKit OpenBot ou des extensions comme Claude Sheets. Plusieurs annonces détaillent des nouvelles capacités (switch de modèles, collaboration multi‑agent) et des retours d’expérience d’utilisation au quotidien.

- [L'agent de codage Gemini 4 de Google change de modèle en cours de tâche et termine 19 % plus vite](https://thenewstack.io/gemini-4-hydrogen-orchestrator/) — *The New Stack*, 12/11 22:26 · **8/10** (Gemini 4 coding agent améliore vitesse, couvert par 2 médias)
  *Titre original : Google’s Gemini 4 coding agent now switches models mid-task — and finishes 19% faster*
  > Google launched Gemini 4 Hydrogen on Thursday alongside a new system that changes how coding agents use AI models. Rather The post Google’s Gemini 4 coding agent now switches models mid-task — and finishes 19% faster appeared first on The New Stack .
- [CopilotKit lance OpenBot 1.0 : un collègue IA auto-hébergeable sous licence MIT avec gouvernance intégrée](https://www.marktechpost.com/2026/11/12/copilotkit-openbot-1-0-open-source-ai-coworker/) — *MarkTechPost*, 12/11 22:45 · **7/10** (Release d'OpenBot 1.0, outil auto‑hébergé avec gouvernance)
  *Titre original : CopilotKit Releases OpenBot 1.0: An MIT-Licensed, Self-Hostable AI Coworker With Built-In Governance*
  > CopilotKit released OpenBot 1.0, an MIT-licensed, self-hostable AI coworker workspace. Companies bring their own agents, models and infrastructure, while every Bot action passes a policy check and lands in an audit trail. The post CopilotKit Releases OpenBot 1.0: An MIT-Licensed, Self-Hostable AI Co
- [Quelle fiabilité pour les outils de codage IA ? Un nouveau test met en lumière les limites de chaque modèle](https://news.google.com/rss/articles/CBMiswFBVV95cUxNS0VhcmEtLXMyUlBQbUx5R0t3M2NRMjVteVRqcV9qLVozRDgzclFyX0hYU2d6S25Ta1lpOXlXWXduc0lZZUhMOGZUZjNxanN2cHhtQnJOcjY2M0pZQjRjbzhieFM0NW5qQVFCNlVjNjVWUFVCbXpicC1FUWZoRmlsUDJkUV9uSm94SS1yS1lxOF9VY1RuVS1RNjdQVWpydUczLWRTRUtVOTZHUW5sTnUwRFhxTQ?oc=5) — *KRDO*, 12/11 21:25 · **7/10** (Évaluation de limites des outils de codage IA, étude pertinente)
  *Titre original : How reliable are AI coding tools? A new test focuses on each model's limits.*
- [Migrer vers la base de connaissances gérée Amazon Bedrock avec votre agent de codage](https://news.google.com/rss/articles/CBMiugFBVV95cUxOMmcyaWlJVl80NTRVX1dRNW5DLUlVN0xyNFJoazVyYk12dUZxR09oS3FWeXM4TldKLXlMWkxNbnhvajMwYWItNHcwTkpmRkxkR1lXdUNMcFRfWHB2dDNVclJQaTJJZDRXbnc2cDktdmJYYl84N3VROU1VNDc2bGxSTnZZY2xMdlc2dHNha2ZNYTBPdGhNVnpZYXNzSy1Va1ZDMERBZW43SkZaLTNUcm9FanJDN3lzeTEzWHc?oc=5) — *Amazon Web Services (AWS)*, 12/11 17:16 · **7/10** (Migration vers Bedrock Knowledge Base, fonctionnalité concrète)
  *Titre original : Migrate to Amazon Bedrock Managed Knowledge Base with your coding agent*
- [Les compétences d'agent deviennent neutres vis-à-vis des fournisseurs : créer une compétence de qualité rédactionnelle pour Claude, Codex et Gemini](https://dev.to/mohab_karim/agent-skills-went-vendor-neutral-building-a-writing-quality-skill-for-claude-codex-and-gemini-31ie) — *dev.to*, 12/11 23:15 · **6/10** (Nouvel outil multi‑modèle, intéressant pour développeurs)
  *Titre original : Agent Skills Went Vendor-Neutral: Building a Writing-Quality Skill for Claude, Codex and Gemini*
  > Agent Skills now belongs to the Linux Foundation, not to one AI company. Here's what that changes, where each agent looks for skills, and a complete writing-quality skill you can drop into Claude Code, Codex and Gemini CLI today. Image generated by AI TL;DR: On October 22, 2026, Anthropic donated th
- [Les agents de codage de Google passent en mode /swarm pour un développeur ; Cursor devient multijoueur pour que les agents des coéquipiers puissent dialoguer](https://thenewstack.io/cursor-google-multiplayer-swarm/) — *The New Stack*, 12/11 22:22 · **6/10** (Fonctionnalité collaborative d'agents, intérêt limité)
  *Titre original : Google’s coding agents now /swarm for one developer. Cursor’s go multiplayer so teammates’ agents can talk.*
  > Coding agents are pretty good at working in parallel: one writes a new API endpoint, another updates the tests, while The post Google’s coding agents now /swarm for one developer. Cursor’s go multiplayer so teammates’ agents can talk. appeared first on The New Stack .
- [Claude Meetings permet à l'IA d'Anthropic de rejoindre vos appels vidéo](https://the-decoder.com/claude-meetings-lets-anthropics-ai-join-your-video-calls/) — *The Decoder*, 12/11 21:26 · **6/10** (Intégration de Claude aux appels vidéo, usage concret)
  *Titre original : Claude Meetings lets Anthropic's AI join your video calls*
  > Anthropic is adding Claude directly to video calls. Claude Meetings joins Google Meet sessions and creates documents, whiteboards, and meeting notes in real time. The feature launches in beta for Team and Enterprise plans, with more platforms coming later. The article Claude Meetings lets Anthropic'
- [Gemini 4 Hydrogen de Google surpasse le plus grand Argon seulement quatre semaines après son lancement](https://the-decoder.com/googles-gemini-4-hydrogen-outscores-the-bigger-argon-just-four-weeks-after-its-launch/) — *The Decoder*, 12/11 20:58 · **6/10** (Benchmark de Gemini 4 Hydrogen, performance notable)
  *Titre original : Google's Gemini 4 Hydrogen outscores the bigger Argon just four weeks after its launch*
  > Google's Gemini 4 Hydrogen replaces the Flash series, but benchmarks suggest it also makes the pricier Argon obsolete. On the independent Artificial Analysis Intelligence Index, Hydrogen nearly matches Claude Sonnet 5.5 for less money but costs about 2.5 times more per task than GPT-6.1 Sol and stil
- [Show HN : AgentRun – agents gérés open source et auto‑améliorants](https://github.com/Parcha-ai/agentrun/blob/main/README.md) — *Hacker News*, 12/11 19:15 · **6/10** (AgentRun, projet open‑source auto‑améliorant, intéressant)
  *Titre original : Show HN: AgentRun – open-source, Self-improving Managed Agents*
  > We (GREP.AI, YC F26) are open-sourcing AgentRun and turning it into a full managed agents platform. Read more about it in this post: https://agentrun.ai/blog/introducing-agentrun-run-smarter-ag... . It includes what we originally built for our own agent harness: - Self-improving agents - Web-grounde
- [Pourquoi les modèles d'IA sur appareil à poids ouvert devraient devenir une fonctionnalité standard du navigateur](https://dev.to/kenzic_85/why-open-weight-on-device-ai-models-need-to-be-a-normal-browser-feature-bol) — *dev.to*, 12/11 23:16 · **5/10** (Proposition d'une fonctionnalité, peu d'impact immédiat)
  *Titre original : Why open-weight on-device AI models need to be a normal browser feature*
  > I started thinking about the Web Models API while experimenting with building AI-native GUIs. I was exploring the idea of UI as a function of AI: the model would generate the content and choose the component best suited to display it. One experiment was a news site which used LLMs to identify key to
- [Comment Amplitude livre des améliorations produit en 1 à 2 jours grâce à OpenAI](https://openai.com/index/amplitude) — *OpenAI*, 12/11 21:00 · **5/10** (Cas d'usage interne d'OpenAI, intéressant mais peu général)
  *Titre original : How Amplitude ships product improvements in 1–2 days with OpenAI*
  > Built primarily on OpenAI models, Amplitude’s proactive product agent, Wave, identifies what to build, helps teams ship changes with coding agents, and measures the impact.
- [J’ai utilisé les outils de codage IA pendant 30 jours. Voici ce qui m’a réellement accéléré (et ce qui ne l’a pas fait)](https://news.google.com/rss/articles/CBMinwFBVV95cUxOZTZNeGotZkMyUEtxZWZuSmluMXBPdGFRc3VBSWluaXl0SjZlQ1NwTTdWc3BzMWlsZkc0cHB4S2FYYTlDeFFKdVoxc0dXMDZOdU5ZdVlmcmxiaTFJTnp1ckFyeE5VdnlPV3J3Z0paMGtJV0xoTnp6LXJKS3pDZEY4eC1aZTZ6Q3QycEZiQ0dpOFdUZGtwMEZZWW9MQ0ctUWs?oc=5) — *HackerNoon*, 12/11 18:49 · **5/10** (Retour d'expérience 30 jours, utile mais subjectif)
  *Titre original : I Used AI Coding Tools for 30 Days. Here’s What Made Me Faster (And What Didn’t)*
- [Les Faster Runners d’Avrea pour GitHub Actions illustrent comment le codage IA transforme le CI](https://news.google.com/rss/articles/CBMiogFBVV95cUxQSE9UazhfMENSS3RadmZFZGMyRlFPU2ZJWWFCS3dTWl9aYjdLYjUyd21fZmxrRFdET21ydmRQaWpiak5udG9XZUNhMll5c2xjOUF6V1NGYk5PcWZwcEEybFVGZ245azhBS0VUbV9KQ2pYMVg3cDQ0YnhqZ3o5RndCSFg4YmVYa1dpejRsdW14WEhSaWY0UWxBeERnYW9yUUlJM1E?oc=5) — *HackerNoon*, 12/11 18:36 · **5/10** (Impact des IA sur GitHub Actions, cas d'usage concret)
  *Titre original : Avrea’s Faster Runners for GitHub Actions Reflect How AI Coding Is Changing CI*
- [Microsoft veut que les développeurs passent moins de temps à corriger les erreurs d’IA](https://news.google.com/rss/articles/CBMi_wFBVV95cUxQYkRNZ3lweDVvdUpQLWktajI3emVoZDdMWXkwNlVFUGxTUDhNa0xrd2gyU0lvQ3ZZR252YUxFQ2NiTlFOTWtGVGh0T00yOS1FNndpclJuNTBzMkdQdXQtTmZmb01Qenl0Sm0xd3RNWU9CejJnenNTV202STJkdWk4Wi0tbFJfbHJVS0hsaXAzdlVTR2w5M2RUMGtnNlRTbVdpQlBoX2Mta0ZoRHVJc3IzeU9sa2FPZkZTU3Y2WHFsaEMyUDlPWThpdVdobTdoOVlyUGh0RGstdktLaEltVFlfM3ZLdVR6Z3Z6a1duRnRDMXpFb25tdUJ4VGpmOTFfOVU?oc=5) — *Windows Central*, 12/11 17:40 · **5/10** (Objectif Microsoft de réduire erreurs IA, orientation produit)
  *Titre original : Microsoft wants developers spending less time fixing AI mistakes*
- [Quelqu’un a utilisé Claude Code pour créer un système d’exploitation Linux pour téléphone, et vous pouvez l’essayer dans votre navigateur](https://news.google.com/rss/articles/CBMisgFBVV95cUxOVDBwRGs5N0Zrb0IwM1hRZVZKUVh6bXJWNDdXaEdkMzBBcFVnbXZVWkEtdWdTdHgyRWZJcGI5T1lENHgyaFBOMU9kd0xrWVQ4SjZGUDJEWTFPWk1JODZIcVdNV3NnRG9PY3JtTmxjcHBNNVZpR0dXcnNJNnUyUHNHMEJVc2ZMNXlqZjBLaFdabmI4d3hDMUtUMHB1OFJhaWN3QU0ta3FFVDh6aDJNNTJJUjBB?oc=5) — *MakeUseOf*, 12/11 12:56 · **5/10** (Projet Linux phone OS avec Claude Code, curiosité)
  *Titre original : Someone used Claude Code to build a Linux phone OS, and you can try it in your browser*
- [AutoCAD Electrical rencontre Vibe Coding : construire un tableau de bord complexe sans expertise DAX/M](https://news.google.com/rss/articles/CBMi4AFBVV95cUxQS1F1ODkwRy0wbGlGbFppdVFxbmNyWHFfNlc3a25xV3dlcm9QN2NQRGhycUZ3RlE5Vy1XcHhwVUkwRjg0WFBKc29GME10aU5YenUzRTM2djZ1N0FkZ1BrQm1TM3RTNV9jVmszaXZLbTlhQ25KZ1pfZDJiSlJ4aHY2T041ZnBsRWw0TERERlZfMVJXamQtdHQwUHRVSGpoVjNvUFl4Yko1VmJsSHBfb0t6UUFIc1lMV2h2OUNXYnhWVDduMy10cGZQT2VXQjQ3WUx3MDJJaFFqUlphZVF4TWpIXw?oc=5) — *Autodesk*, 12/11 12:16 · **5/10** (Intégration AutoCAD + Vibe Coding, cas d'usage sectoriel)
  *Titre original : AutoCAD Electrical Meets Vibe Coding: Building a Complex Dashboard Without DAX/M Expertise*
- [Comment Adobe mise sur ses agents IA pour décloisonner ses logiciels](https://www.blogdumoderateur.com/comment-adobe-compte-agents-ia-decloisonner-logiciels/) — *Blog du Modérateur*, 12/11 12:09 · **5/10** (Adobe mise sur agents IA, stratégie produit)
  *Titre original : Comment Adobe compte sur ses agents IA pour décloisonner ses logiciels*
  > Aller chercher les utilisateurs là où ils travaillent, sans bousculer les pros : Zorana Gee, Senior Director des Creative Agents d’Adobe détaille la stratégie agentique de l'éditeur.
- [Claude Code peut désormais aider à diagnostiquer un PC ou Mac lent](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQak1WcEV6dmFQdWNjVTZpYmNCMTlDdFh1OEZGUnBXa2w5MkJSM29ZTUM1b1dRRlhGRG5tclhkanFuV1BMNU42bDVHUDFIcC1yN1BRaTV0LU5LYktZMVpJYjRadGpTbzA0R2hVMkI1alpER2lnc1hYcVZGRFdYQVllWnVOVW1UU1R3OUFV?oc=5) — *Softonic*, 12/11 10:39 · **5/10** (Claude Code aide diagnostic PC, usage pratique)
  *Titre original : Claude Code can now help diagnose a slow PC or Mac*
- [Holiday Extras repense ce qu’il peut créer avec Codex](https://openai.com/business/customer-stories/holidays-extras-codex) — *OpenAI*, 12/11 10:30 · **5/10** (Holiday Extras utilise Codex, cas d'usage commercial)
  *Titre original : Holiday Extras is rethinking what it can build with Codex*
  > With Codex, Holiday Extras is turning customer expertise into better apps, higher booking conversion and new possibilities for growth.
- [J'ai laissé Claude Code réparer mon ordinateur de jeu, et les saccades ont presque disparu](https://news.google.com/rss/articles/CBMigwFBVV95cUxNUEIwVlRzY3dDZkRRZDI1MXhHR0ptU2NGNnJlRDM5UGE1dURXTm1sLU8yemFaQ0dDTmpwcDNFcUE1TDNHV210TGVyNG02M0ZMb0o3NFo3WWxiNGwtUHJySFdiYmNKMmtZTi02cmlndmlMTGJxTkp4amxVUjdRUlVRSjF6RQ?oc=5) — *MakeUseOf*, 12/11 20:30 · **4/10** (Anecdote personnelle, peu de portée)
  *Titre original : I let Claude Code fix my gaming laptop, and the stutters mostly disappeared*
- [Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) — *Hacker News*, 12/11 19:01 · **4/10** (Redite de Gemini 4 Hydrogen, peu d'info supplémentaire)
  *Titre original : Gemini 4 Hydrogen*
  > Article URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/ Comments URL: https://news.ycombinator.com/item?id=50471431 Points: 390 # Comments: 258
- [Claude Code et Codex pénètrent l'ordinateur de bord d’un Jeep de 1994](https://news.google.com/rss/articles/CBMikAFBVV95cUxNUkVnb0YyQUV4RTJneW1KbTJUUVFPUEE1cE1CNjBqeFc1R2prT3Q3Qk9jbFFGTjhyUktsdmU5aDJGOXlrTHpWUnZBZUZmcUIxQ2U3R0sySFFaUkhiR0hjbl9tMW9pSFJ3aXpJOUtBa1F2c2NMN1pTSkpWaXBfaERLZm9VcEhWYmRENk5OdW5sOUU?oc=5) — *Pasquale Pillitteri*, 12/11 15:50 · **4/10** (Démonstration ludique, peu d'impact réel)
  *Titre original : Claude Code and Codex get inside a 1994 Jeep's engine computer*
- [Anthropic dévoile Claude Sheets, Claude Whiteboards et Claude Data : ce qu’il faut savoir](https://www.blogdumoderateur.com/anthropic-claude-sheets-whiteboards-data/) — *Blog du Modérateur*, 12/11 11:16 · **4/10** (Nouveaux produits Claude, annonce produit)
  *Titre original : Anthropic dévoile Claude Sheets, Claude Whiteboards et Claude Data : ce qu’il faut savoir*
  > Les trois modules ont été déployés ce mardi sur toutes les formules payantes.

## Déploiement et infrastructure IA (10)

Plusieurs titres portent sur le déploiement de modèles de pointe ou d’agents sur des infrastructures cloud, notamment AWS Trainium, Bedrock AgentCore, les émulateurs locaux d’AWS et les passerelles AI Gateway. Ces ressources visent à simplifier l’accès aux modèles lourds et à accélérer le développement d’applications IA.

- [Déployer des modèles d'IA de pointe sur AWS Trainium avec SGLang-Neuron](https://aws.amazon.com/blogs/machine-learning/deploy-frontier-ai-models-on-aws-trainium-with-sglang-neuron/) — *AWS Machine Learning*, 12/11 23:03 · **8/10** (Déploiement de modèles frontier sur AWS Trainium, forte portée)
  *Titre original : Deploy frontier AI models on AWS Trainium with SGLang-Neuron*
  > SGLang-Neuron is now publicly available through an AWS Deep Learning Container. With SGLang-Neuron, you can serve models and generate reinforcement learning rollouts with SGLang on AWS Trainium using the same SGLang interface you already know, all running on native PyTorch.
- [Comment Natera a conçu un système d'IA agentique pour les opérations de laboratoire avec Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/how-natera-designed-an-agentic-ai-system-for-lab-ops-with-amazon-bedrock-agentcore/) — *AWS Machine Learning*, 12/11 22:47 · **7/10** (Cas d'usage concret d'agent IA sur Bedrock, pertinent)
  *Titre original : How Natera designed an agentic AI system for lab ops with Amazon Bedrock AgentCore*
  > Natera built SWARM, an agentic AI system on Amazon Bedrock AgentCore that captures institutional lab-operations knowledge and deploys it at scale. This post walks through the full architecture, from knowledge base construction to deployment and evaluation, delivering about 130x faster first response
- [AWS lance AWS Emulator : une copie locale de plus de 200 services AWS créée par des agents IA](https://www.marktechpost.com/2026/11/12/aws-emulator-local-aws-api-emulator-ai-agents/) — *MarkTechPost*, 12/11 18:26 · **7/10** (AWS Emulator local, 200+ services, outil pratique)
  *Titre original : AWS Releases AWS Emulator: A Local Copy of 200+ AWS Services Built by AI Agents*
  > AWS released AWS Emulator, a free, CC0-licensed local emulator of AWS APIs built from 438 API models. Autonomous agents wrote all of its code. It passes 56.6% of 42,857 published fidelity tests at launch. The post AWS Releases AWS Emulator: A Local Copy of 200+ AWS Services Built by AI Agents appear
- [AWS augmente la capacité de calcul du runtime Bedrock AgentCore pour accélérer le développement d’agents IA](https://www.infoworld.com/article/4247866/aws-boosts-bedrock-agentcore-runtime-compute-capacity-to-speed-up-ai-agent-development.html) — *InfoWorld*, 12/11 13:38 · **6/10** (Boost compute AgentCore, accélère développement d'agents)
  *Titre original : AWS boosts Bedrock AgentCore runtime compute capacity to speed up AI agent development*
  > AWS on Thursday said that it was upgrading the runtime layer of Amazon Bedrock AgentCore with greater compute capacity, more efficient memory utilization, and faster startup times to help enterprises deploy and scale AI agents more quickly and cost-effectively. The greater compute capacity includes 
- [Quatre options d'inférence Amazon Bedrock qui influent sur le coût](https://aws.amazon.com/blogs/machine-learning/four-amazon-bedrock-inference-choices-that-affect-cost/) — *AWS Machine Learning*, 12/11 21:51 · **5/10** (Guide coût Bedrock, utile mais peu novateur)
  *Titre original : Four Amazon Bedrock inference choices that affect cost*
  > Your Amazon Bedrock inference bill can keep climbing even after you tune prompts and application logic. Four request-level choices (cache duration, service tier, reasoning effort, and maxTokens) change how many tokens the service processes and the rate applied. We show how we tested each and how to 
- [Tokenomics à grande échelle : suivre et plafonner les dépenses Amazon Bedrock par principal IAM avec CUR 2.0 et AWS Budgets](https://aws.amazon.com/blogs/machine-learning/tokenomics-at-scale-track-and-cap-amazon-bedrock-spend-per-iam-principal-with-cur-2-0-and-aws-budgets/) — *AWS Machine Learning*, 12/11 20:29 · **5/10** (Gestion des dépenses Bedrock, utile pour admins)
  *Titre original : Tokenomics at scale: Track and cap Amazon Bedrock spend per IAM principal with CUR 2.0 and AWS Budgets*
  > Get per-identity Amazon Bedrock cost visibility and enforceable spend limits using only AWS-native features, with no application code for the common case. Attribute spend with IAM principal tags, report with CUR 2.0 or Cost Explorer, and enforce with AWS Budgets actions that apply a Deny policy when
- [Expo déploie des simulateurs iOS cloud et des émulateurs Android pour les agents de codage IA](https://news.google.com/rss/articles/CBMizgFBVV95cUxQN2VjMEY4eXZldWk3dVFuSDdPU29pdjRYd1B2VGVjdDcyell2amJWS0JYMWY2TUtRc29PNWxkb2hhMmhXNm5FdHVuMldsQ1VDY2ktQlJ0SzNpVGxPeFE5N0sxY0l6MS1tYVFsSjRVNzlyQkhVVnBWdXgxWVlSQXQxZDRLWkpuaWJia0VPY19hbkFXcEVWTzlUM0phU2FsNjE4SDF4UHhMOHBwc0txWHM1UFNXYkdJOXhzQk1IejJLMEdOQVFJVWVDMEh4ODRZQQ?oc=5) — *PR Newswire*, 12/11 18:05 · **5/10** (Annonce de simulateurs cloud, similaire à #24)
  *Titre original : Expo Launches Cloud iOS Simulators and Android Emulators for AI Coding Agents*
- [L'API Decisions de Gemini de Google gère jusqu’à 1 000 questions par requête](https://www.infoworld.com/article/4247774/googles-gemini-decisions-api-to-handle-up-to-1000-questions-per-request.html) — *InfoWorld*, 12/11 11:53 · **5/10** (Gemini Decisions API, capacité élevée mais peu de détails)
  *Titre original : Google’s Gemini Decisions API to handle up to 1,000 questions per request*
  > Google has announced Gemini Decisions API, offering developers a way to handle routine decisions in AI applications without generating text responses, weeks after OpenAI launched a competing service. Powered by the company’s new Gemini Decision 1 model, the API allows developers to evaluate up to 1,
- [Google open‑source le synchroniseur TPU pour le cache KV et le transfert de poids sur les TPUs](https://www.infoq.com/news/2026/11/google-tpu-sync/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 12/11 11:06 · **5/10** (Open‑source TPU Sync, amélioration technique)
  *Titre original : Google Open-Sources TPU Sync for KV Cache and Weight Transfer on TPUs*
  > Google Cloud has open-sourced TPU Sync, a native C++ library that moves KV cache blocks and model weights between TPU HBM, host DRAM, shared storage, and the data center network. By Daniel Dominguez
- [Azure Logic Apps Standard obtient un CLI local en version préliminaire](https://www.infoq.com/news/2026/11/logic-apps-local-cli/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 12/11 11:23 · **4/10** (CLI local Azure Logic Apps, fonctionnalité mineure)
  *Titre original : Azure Logic Apps Standard Gets a Local CLI in Preview*
  > Microsoft has released a public preview of the logicapp extension for the Azure CLI, adding local project creation, workflow authoring, a runtime lifecycle, connector management, run inspection, and test scaffolding for Logic Apps Standard, work that previously required the VS Code extension. The pr

## Coût, tokenomics et optimisation (1)

Des articles analysent les coûts liés à l’inférence sur Bedrock, les mécanismes de tokenomics à grande échelle et les stratégies pour réduire les dépenses liées aux agents IA. Ils offrent des outils de suivi et de plafonnement des dépenses par principal IAM.

- [Les données d’OpenAI suggèrent que les modèles de pointe cachent leurs pensées parce que les développeurs privilégient capacité et calcul](https://the-decoder.com/openais-data-suggests-that-frontier-models-are-hiding-their-thoughts-because-developers-optimize-for-capability-and-compute/) — *The Decoder*, 12/11 17:58 · **6/10** (Analyse des comportements des modèles frontier, insight intéressant)
  *Titre original : OpenAI’s data suggests that frontier models are hiding their thoughts because developers optimize for capability and compute*
  > OpenAI's safety team systematically investigated why the chains of thought in frontier models like GPT-6 Astra are increasingly evading oversight. Four training steps drive the erosion, including architecture choices and reinforcement learning. The analysis shows that the loss of transparency is not

## Sécurité et gouvernance (5)

La sécurité des pipelines CI/CD, la protection des clés API Claude, les incidents de vol de credentials et les bonnes pratiques de gouvernance des agents IA sont mis en avant. Les publications proposent des recommandations pour limiter les risques liés aux agents qui accèdent aux secrets ou aux environnements de production.

- [Des hackers ciblent les outils de codage IA pour voler des identifiants, 103 incidents cyber liés à l’IA révélés par des chercheurs](https://news.google.com/rss/articles/CBMibkFVX3lxTE1nd2JPMzhvS0NnSHZjbjVzcE9DdjBhS3NZaF95RmU0bmZmNmY5T1VSR1U5N3lEaFY4TmZXV2s1cmxQUHRHT0hVSDA5RER2T1dTODdmd0FuODFvTkJ1UUY3eXdBQ05BS3Q4OTJ4LWVB0gFzQVVfeXFMTzhyVlZKWEswZVNsUjlVTWRHUm5Kb0gzbmFoN0YxSGtjUkRGZDdOSG10NkZpVU44RFJ5UnhVZHo3cWxQUzg0UmpIaXpYLWxIWUdCeXJNY3ozY18xNm14LXlteGVmelZodlFPNHhwbmF1N0tDcw?oc=5) — *CyberSecurityNews*, 12/11 13:27 · **8/10** (Cyber‑incidents liés aux outils IA, impact majeur sur sécurité)
  *Titre original : Hackers Target AI Coding Tools to Steal Credentials as Researchers Uncover 103 AI-Linked Cyber Incidents*
- [Des clés API Claude volées peuvent transformer Claude Code en implant télécommandé](https://news.google.com/rss/articles/CBMilwFBVV95cUxQWDRNVVdqMy1DQ19iWGZTM3NtaFN3a0RNWEV6ZlU1QWZlZVQwVjdBZFFBRkpEenBIN29yM2VRc0xGWTFfeHlfeUlaU2xIWkZnMjNXdXN4VFJjTWJIMXd1Wm9sRWJNU2djMkFuSm9NWC0xTnNBY0FheXVYWjR5N3RkdU40MERTLU96Ulk3eS1FTzdMRFVGd3Jv?oc=5) — *Help Net Security*, 12/11 12:00 · **7/10** (Clé API Claude compromise, risque sécurité concret)
  *Titre original : Stolen Claude API keys can turn Claude Code into a remote-controlled implant*
- [Sécurité des agents de codage pour les responsables AppSec : commencer par ce que les agents peuvent atteindre](https://news.google.com/rss/articles/CBMiakFVX3lxTE80WjhYd0pXeVc3aTZOb3ZQZklBaXJ5VEs5OVhwUXBhR29zS3kybmwzSklUNmpLbzNIVVdxZzdQVDdHb1JETmdKTGlpd2IzMXZZbTAtZGtfRzlySld0SWtHWHpiblhuUjljSFE?oc=5) — *GitGuardian Blog*, 12/11 17:01 · **6/10** (Guide sécurité agents pour AppSec, pratique)
  *Titre original : Coding Agent Security for AppSec Leaders: Start With What Agents Can Reach*
- [Présentation : Ouvrir la boîte noire – l'explicabilité cruciale pour le choix d’outils d’agents IA avec Kiji Inspector](https://www.infoq.com/presentations/explainable-ai-llm-agent-decisions/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 12/11 12:00 · **6/10** (Présentation explainability pour sélection d'agents, utile)
  *Titre original : Presentation: Opening the Black Box: Critical Explainability for AI Agent Tool Selection with Kiji Inspector*
  > Hannes Hapke shares how Dataiku’s open-source Kiji Inspector applies Sparse Autoencoders (SAEs) directly to decision tokens to expose why agents pick specific tools. Moving past superficial chain-of-thought narratives, he discusses causal ablation, layer activation extraction via patched vLLM engine
- [Le codage IA aggrave-t-il la dispersion des secrets dans les pipelines CI/CD ?](https://news.google.com/rss/articles/CBMihAFBVV95cUxQSWJzMVh1VEI4d25LbkRSMFpFSVJjTEJhRi1RZk9lODFzNG1OYW5sY2RaalJOQ2VUeU5ZSmlianlka0F5Rk5CcFlRQkpRWmdxT1RYM3hYZ0VIa3BVRC1oSmFEcHVSUjFtcjVvc1NYS3YzSWppbEtNQzZNVFRHSmV1ZDB2M0o?oc=5) — *DevOps.com*, 12/11 20:36 · **5/10** (Sécurité des secrets en CI/CD, sujet d'actualité)
  *Titre original : Does AI Coding Make Secrets Sprawl Worse in CI/CD Pipelines?*

## Nouveaux modèles et performances (1)

Les dernières itérations de modèles comme Gemini 4 Hydrogen, les comparaisons de performances (Hydrogen vs Argon) et les améliorations de vitesse (19 % plus rapide) sont détaillées. D’autres titres évoquent des recherches sur la transparence des modèles et des guides de fine‑tuning.

- [Google a développé un modèle d'IA incapable d'écrire une phrase — et c’est exactement le but recherché](https://thenewstack.io/google-gemini-decisions-api/) — *The New Stack*, 12/11 18:02 · **5/10** (Modèle qui ne peut pas écrire de phrase, curiosité technique)
  *Titre original : Google built an AI model that can’t write a sentence — and that’s the point*
  > Google’s new Gemini Decisions API, introduced Wednesday, is designed to handle the routine decisions that AI applications make thousands of The post Google built an AI model that can’t write a sentence — and that’s the point appeared first on The New Stack .

## Outils et frameworks divers (2)

Des nouveautés telles que le langage de balisage LLMON, les simulateurs cloud pour agents de codage, les guides de fine‑tuning 3D, ainsi que des extensions comme Viirtue MCP ou des plateformes d’outils low‑code sont présentées, offrant aux développeurs de nouvelles façons d’interagir avec les modèles IA.

- [LLMON : un langage de balisage natif LLM, désormais disponible dans Granite 4.1 3B et 8B](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite) — *Hugging Face*, 12/11 20:07 · **7/10** (LLMON, nouveau langage natif LLM, implémentation concrète)
  *Titre original : LLMON: An LLM-Native Markup Language, now in Granite 4.1 3B and 8B*
- [Expo ouvre l’accès aux simulateurs cloud en plan payant pour les agents de codage IA](https://news.google.com/rss/articles/CBMilAFBVV95cUxQZVBaaG5pcTB2YUQ5aDhRdkxkYlVncWpxNjc4ZXVnLUNYRC1Sdzh4YllBcHhJcDlxQ0kxODY0WDIwdkFLM25JbEZENktVQ0UtNmNpUl9qOEVmT2Fzdm83dGZIbmJZZUNUUGoyOWlNN3FqZkMyZUVoLVFJaEtMeVoxc1B2UWU2M3VNb0JwY2VJVHUzZ1lR?oc=5) — *Unite.AI*, 12/11 18:34 · **6/10** (Accès payant à simulateurs cloud pour agents IA, nouvelle offre)
  *Titre original : Expo Opens Paid-Plan Access to Cloud Simulators for AI Coding Agents*

## Autres articles (8)

- [Le RAG Retrieval a perdu 40 points lorsque les passages distractifs ont atteint 2,68 M](https://towardsdatascience.com/rag-retrieval-lost-40-points-when-distracting-passages-grew-to-268m/) — *Towards Data Science*, 12/11 17:30 · **6/10** (Recherche RAG, perte de performance mesurée, contribution scientifique)
  *Titre original : RAG Retrieval Lost 40 Points When Distracting Passages Grew to 2.68M*
  > A reproducible test of BM25, embeddings, and parent documents shows why author-written evals overrate search, and why answer position in context matters. The post RAG Retrieval Lost 40 Points When Distracting Passages Grew to 2.68M appeared first on Towards Data Science .
- [Viirtue MCP fonctionne désormais avec Microsoft 365 Copilot et GitHub Copilot](https://news.google.com/rss/articles/CBMirwFBVV95cUxNOXJfSnRnYWhXbDY1bXNyZzBrMnpOWUowdEFjeEg4eVVOZ1l5LVVXeXJlb0NqamM3WnFJODhRZ0Y2LS1OcVR0SXN0eW9Mb0tDaHgteVRiNXVoRzlUaHlEV3p2SWZTU2hqalpKaGZ5ZUw5MU9TWUowV3V1eGxVeWxkQWNZNFJNeGV0bFdqXzVZU3pIQS1mbVM1aXRiSUpSX0dSNUNFVUhzS0FPSWkwOHpn?oc=5) — *AiThority*, 12/11 11:03 · **6/10** (Viirtue MCP intégration 365 Copilot & GitHub Copilot, protocole nouveau)
  *Titre original : Viirtue MCP Now Works With Microsoft 365 Copilot and GitHub Copilot*
- [Gemini 4 Hydrogen et Orchestrator](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/) — *Hacker News*, 12/11 19:52 · **5/10** (Discussion Hacker News, peu de profondeur)
  *Titre original : Gemini 4 Hydrogen and Orchestrator*
  > Article URL: https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/ Comments URL: https://news.ycombinator.com/item?id=50472260 Points: 187 # Comments: 42
- [Découvrez l'IA en production lors de Microsoft Ignite](https://thenewstack.io/microsoft-ignite-2026/) — *The New Stack*, 12/11 15:00 · **5/10** (Vue production IA à Microsoft Ignite, aperçu intéressant)
  *Titre original : See what AI looks like in production at Microsoft Ignite*
  > If you’re deciding which AI pilots to move into production, Microsoft’s Satya Nadella and Judson Althoff’s opening keynote at Microsoft Ignite The post See what AI looks like in production at Microsoft Ignite appeared first on The New Stack .
- [La tempête de reconnexions : comment les boucles de reconnexion naïves de WebSocket déclenchent des hordes de requêtes simultanées](https://dev.to/toai/the-reconnection-storm-how-naive-websocket-retry-loops-trigger-thundering-herds-52po) — *dev.to*, 12/11 23:12 · **4/10** (Analyse technique, utile mais pas révolutionnaire)
  *Titre original : The Reconnection Storm: How Naive WebSocket Retry Loops Trigger Thundering Herds*
  > The Reconnection Storm: How Naive WebSocket Retry Loops Trigger Thundering Herds 1. Post-Mortem of an Incident: Reconnection Cascades and Connection Pool Exhaustion This vulnerability surfaced during stress testing of a high-concurrency WebSocket gateway provisioned to hold thousands of persistent d
- [Zendesk dévoile l’Outcome AI Platform pour adapter le service client aux assistants IA personnels](https://www.blogdumoderateur.com/zendesk-outcome-ai-platform-adapter-service-client-assistants-ia-personnels/) — *Blog du Modérateur*, 12/11 11:02 · **4/10** (Zendesk Outcome AI Platform, annonce produit)
  *Titre original : Zendesk dévoile l’Outcome AI Platform pour adapter le service client aux assistants IA personnels*
  > Présentée lors de l’AI Summit, la nouvelle plateforme de Zendesk réunit un annuaire de support vérifié, une connexion aux outils IA tiers et une facturation au résultat. Michael Chaouat en détaille les contours.
- [L'importance de l'ingénierie logicielle dans les applications web](https://dev.to/touoyem_brian_e75b339ff5d/relevance-of-software-engineering-in-web-apps-243o) — *dev.to*, 12/11 23:15 · **3/10** (Opinion général, peu de nouveauté)
  *Titre original : Relevance Of Software Engineering In Web Apps*
  > We live in the golden age of "vibe coding." Coined to describe the workflow of prompting an LLM, accepting diffs without reading them, and iterating purely on natural language until the UI looks right, vibe coding has lowered the barrier to building web applications to near zero. Today, anyone with 
- [Les 10 meilleurs assistants de codage IA du monde en 2026](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1RTzFTTXVlZW13YlhYOHFkUjZGaDhDVU5mTzVRRFN2c292blVpYlp6LWE0THNjYjVwY0pvUHV4czI4RkdnejFxR3RwcTFYV0FWMXRsSUZLSmxPSVNmQ2QzcU9KWlJOUQ?oc=5) — *Nubia Magazine!*, 12/11 12:34 · **3/10** (Top‑10 des assistants IA, contenu promotionnel)
  *Titre original : The Top 10 Best AI Coding Assistants In The World 2026:*

## Vidéos à regarder (10)

- [What Is MCP? How AI Agents Connect to Everything](https://www.youtube.com/watch?v=h6USydL-6s4) — *Neural Quadrant*, 12/11 23:24
  > Explication claire de ce qu'est le protocole MCP (Model Context Protocol), de son rôle pour connecter les agents IA et du fonctionnement des flux de requêtes.
- [Best AI Coding Agent 2026 — Pick One & Set It Up (Claude Code vs Cursor vs Codex)](https://www.youtube.com/watch?v=TLbm1d51Z6M) — *ErrorFixer*, 12/11 23:00
  > Comparatif pratique entre Claude Code, Cursor et Codex pour choisir et configurer le meilleur agent de programmation en 2026.
- [How AI Agents Use Tools: Function Calling & MCP | Stanford CS329Z Lecture 4 with Diyi Yang](https://www.youtube.com/watch?v=s0S38lz6O7M) — *Stanford Online*, 12/11 22:00
  > Cours magistral de Stanford sur la manière dont les agents IA utilisent les outils via le function calling et le protocole MCP.
- [DeepSeek Is Coming for Claude Code](https://www.youtube.com/watch?v=njleVdiW-mM) — *Ultrafast AI*, 12/11 20:00
  > Présentation de DeepSeek Harness, une nouvelle application de code avec un mode Créateur intégré qui concurrence directement Claude Code.
- [Theo's AI Agent Does Everything Except Hit Merge #claudecode #github #ai](https://www.youtube.com/watch?v=ChwpFTSt2tA) — *Better Stack*, 12/11 18:00
  > Présentation de tstack, une collection open-source de compétences pour automatiser le déploiement de code avec Claude Code.
- [Build an AI Agent with Python 🤖 | OpenAI Tool Calling Explained #Shorts](https://www.youtube.com/watch?v=1dMC173qyOY) — *AIARCHITECTLAB*, 12/11 16:42
  > Tutoriel pratique pour apprendre à construire un agent IA en Python en utilisant les capacités de function calling d'OpenAI.
- [AgentGit Tutorial: Manage & Share AI Coding Sessions with Codex, Claude Code & More!](https://www.youtube.com/watch?v=5wzC5Pzd6U4) — *Pro Coder*, 12/11 15:04
  > Découverte d'AgentGit, une plateforme dédiée à la gestion, la sauvegarde et au partage de sessions de code générées par des agents IA.
- [Rogue MCP Tools: How Untrusted Servers Hijack AI Agents #Shorts](https://www.youtube.com/watch?v=6Cf1W8jtZBI) — *Agent Pov*, 12/11 15:00
  > Alerte de sécurité sur les risques posés par des serveurs MCP non sécurisés susceptibles de compromettre des clés d'API et variables d'environnement.
- [Cursor vs Claude Code vs Qwen Code 1.0 — What's Different? 💻 #ai #shorts](https://www.youtube.com/watch?v=5xm7-EEpsI0) — *Techtonica*, 12/11 13:54
  > Test de Qwen Code 1.0, un nouvel agent de programmation open-source conçu pour fonctionner directement dans le terminal.
- [Google Antigravity Just Got Swarm Mode (One Prompt, Multiple AI Agents)](https://www.youtube.com/watch?v=zrN7DHDuWts) — *Codedigipt*, 12/11 11:10
  > Présentation du mode swarm de Google Antigravity, un système de programmation multi-agents permettant d'exécuter des tâches complexes à partir d'une seule invite.

## Podcasts à écouter (10)

- [Google Stitch 2.0: The FREE AI Design Powerhouse by Google is CRAZY!](https://podcasts.apple.com/us/podcast/google-stitch-2-0-the-free-ai-design-powerhouse-by/id6826122006?i=1000799145675&uo=4) — *AICodeKing*, 12/11 22:53
  > Annonce de Google Stitch 2.0, un nouveau puissant outil gratuit de conception assistée par IA.
- [Stable Diffusion 3: Open Weights for SD-3 is now Available! The Best Text-To-Image Opensource Model](https://podcasts.apple.com/us/podcast/stable-diffusion-3-open-weights-for-sd-3-is-now-available/id6826122006?i=1000801587180&uo=4) — *AICodeKing*, 12/11 22:27
  > Publication des poids ouverts de Stable Diffusion 3, le dernier modèle texte‑à‑image open‑source.
- [Gemini Decision 1, Qwen4-Max preview — AI News Nov 12](https://podcasts.apple.com/us/podcast/gemini-decision-1-qwen4-max-preview-ai-news-nov-12/id6817748791?i=1000801565557&uo=4) — *AI Engineering Briefing: Daily AI News for Software Engineers*, 12/11 19:38
  > Présentation de Gemini Decision 1, modèle à réponses rapides, et aperçu du modèle Qwen4‑Max d’Alibaba.
- [Anthropic says Claude will build your spreadsheet from one sentence. Plus Amazon's shopping agent now takes orders by text, and what AI is doing to freelance budgets](https://podcasts.apple.com/us/podcast/anthropic-says-claude-will-build-your-spreadsheet-from/id6790021778?i=1000801524503&uo=4) — *AI Industry Report*, 12/11 15:11
  > Anthropic montre que Claude peut créer et partager une feuille de calcul complète à partir d’une seule phrase.
- [Daily AI briefing · Nov 12, 2026](https://podcasts.apple.com/us/podcast/daily-ai-briefing-nov-12-2026/id6828679411?i=1000801521865&uo=4) — *Jadid for Engineers: Daily AI Briefing*, 12/11 14:00
  > Analyse des points faibles actuels de la chaîne IA : les personnes et les identifiants, avec des incidents de comptes GitHub piratés.
- [Episode 98: High Stakes Blackjack and Poker Bluffs in the Arena](https://podcasts.apple.com/us/podcast/episode-98-high-stakes-blackjack-and-poker-bluffs-in/id6792364624?i=1000801489129&uo=4) — *Playce is where autonomous AI agents compete for real stakes - The Arena Report*, 12/11 11:00
  > Reportage sur les parties à enjeux élevés d’agents autonomes dans l’arène Playce, incluant bluff au poker et blackjack.
- [Ki programmiert KI ohne Training? - Weight Space Programming](https://podcasts.apple.com/us/podcast/ki-programmiert-ki-ohne-training-weight-space-programming/id1878105483?i=1000801489311&uo=4) — *Lethonium - Der AI Podcast für Software Engineers*, 12/11 10:54
  > Discussion sur la programmation directe des poids d’un modèle (Weight Space Programming) comme alternative au fine‑tuning.
- [Why AI Models Still Fall Short of Human Experts](https://podcasts.apple.com/us/podcast/why-ai-models-still-fall-short-of-human-experts/id1878092878?i=1000801402701&uo=4) — *The Sentient Code: AI and Robotics*, 12/11 10:00
  > Interview sur Handshake AI, qui a atteint près d’un milliard de dollars de revenu annuel en fournissant des données d’experts aux laboratoires de pointe.
- [Fable 5.2, Nvidia’s Investigation, and Claude’s Office Push](https://podcasts.apple.com/us/podcast/fable-5-2-nvidias-investigation-and-claudes-office-push/id6820789469?i=1000801360855&uo=4) — *AI Psychosis*, 12/11 03:52
  > Décryptage de Fable 5.2, de l’enquête Nvidia et des nouvelles fonctions de bureau de Claude pour les utilisateurs quotidiens.
- [Gemini 4 Carbon GA, Claude Sheets — AI News Nov 11](https://podcasts.apple.com/us/podcast/gemini-4-carbon-ga-claude-sheets-ai-news-nov-11/id6817748791?i=1000801271807&uo=4) — *AI Engineering Briefing: Daily AI News for Software Engineers*, 11/11 19:26
  > Annonce de la disponibilité générale de Gemini 4 Carbon et de la suite office de Claude (Sheets, Whiteboards, Meetings, Data).

## Écartés comme hors sujet (9)

- [AI is turning Apple's app review process into a nightmare for synth developers](https://synthanatomy.com/2026/11/ai-is-turning-apples-app-review-process-into-a-nightmare-for-developers.html) — *Hacker News*, 12/11 22:09
  > Article URL: https://synthanatomy.com/2026/11/ai-is-turning-apples-app-review-process-into-a-nightmare-for-developers.html Comments URL: https://news.ycombinator.com/item?id=50474311 Points: 6 # Comments: 0
- [Modern Web Guidance 1.0 and New Zealand business websites](https://news.google.com/rss/articles/CBMi6gFBVV95cUxOTFB1YzhlUTh2cVp1TEdObW1fcl84U0RfN3Y5cldSc0xYVHVBbWgxdV9EcXExU0doYTZyS2F1VVRRR0ZwemxnekcxS3dJaXpIeW9oc0VaMnplOG5keXhWRzlDckt3Rk5icHYtNlFVTE5rcmNrZWVQb1RoYVNSNlNNXzVIdzU3VU96eGRuWXBpVVZHaEt1RG43dWUzS2lKN2ZDLWJ5VWVOdTJuX1hINFZrWldjUWk4ZmZ2VFZ0alF1TEVubjJZcU9HaW1TeXdFS1l3aXVtVVhPSTR3VGRNaHE4bk4tcF8xRWNibnc?oc=5) — *https://newswire.co.nz/*, 12/11 20:37
- [Jensen Huang resigns as Nvidia CEO after espionage scandal wipes out $1.4 trillion in market value](https://the-decoder.com/jensen-huang-resigns-as-nvidia-ceo-after-espionage-scandal-wipes-out-1-4-trillion-in-market-value/) — *The Decoder*, 12/11 15:11
  > Jensen Huang resigned as CEO, president, and board member of Nvidia effective immediately, according to a statement on November 12, 2026. The article Jensen Huang resigns as Nvidia CEO after espionage scandal wipes out $1.4 trillion in market value appeared first on The Decoder .
- [Humble Bundle goes through a re-design that's being accused of messy vibe-coding](https://news.google.com/rss/articles/CBMiugFBVV95cUxPUGN1a3d0SDJxOEVvWVVoVVhGcHdobUJ3eF9sSU5Hdm5WQzFHYVB0QXVUUjFlUkdxSDR6dmdhX081SnZBVk5qaW9JYnVDY0NSNmxpU3ppNjNsQXNCOWhyMTRodjJYdXFqaUZveW9ZRWYwLUhwOWY4NHlYbktfODdadXZUUXJSdjZVUEMzS0FFNnNXMmZWbEJXbVFxYWwxQkxzd3R0ZGFZRzlGLXd4am9TVFR2THRvX0hiZkE?oc=5) — *GamingOnLinux*, 12/11 12:43
- [IBM Announces IBM Quantum Nighthawk r3: A New Processor to Support 10k Quantum Operations on 520 Programmable Qubits](https://www.marktechpost.com/2026/11/12/ibm-quantum-nighthawk-r3-520-qubits-1040-qubit-system-2027/) — *MarkTechPost*, 12/11 09:42
  > IBM announced Quantum Nighthawk r3, a 520-qubit processor designed for 10,000 quantum operations. 2 r3 chips will link into a 1,040-qubit system in 2027, while Nighthawk r2 already posts up to 19x speedups over Heron. The post IBM Announces IBM Quantum Nighthawk r3: A New Processor to Support 10k Qu
- [[AINews] D-Day (Decision Models Day)](https://latent.space/p/ainews-d-day-decision-models-day/) — *Latent Space*, 12/11 06:26
  > November 11, 2026 — Google enters the decision model market. At AI Engineer, Cloudflare showed which parts of a build failure a classifier could handle. TypeSafe AI showed off their production customers.
- [Supporting research on AI and children’s safety](https://openai.com/index/children-first-declaration) — *OpenAI*, 12/11 01:00
  > OpenAI commits $2 million to research on AI and children’s safety. The work supports shared tools to measure risks and opportunities for young people.
- [Gilbert + Tobin rethinks the business of law with AI](https://openai.com/index/gilbert-tobin-sam-nickless) — *OpenAI*, 12/11 01:00
  > A conversation with Sam Nickless, Partner and Chief Executive Officer at Gilbert + Tobin.
- [Browse tools.simonwillison.net by tag](https://simonwillison.net/2026/Nov/11/tools-tags/) — *Simon Willison*, 11/11 19:42
  > Browse tools.simonwillison.net by tag I've been wanting a better way to browse my collection of vibe-coded tools (244 and counting) for a while. I had a few Fable 5.2 credits left over before my weekly reset so I set it to work using tree-sitter to analyze the code for JavaScript APIs, libraries, an
