# Veille IA outils & code du 14/11/2026

50 articles de médias tech anglophones et francophones (blogs d'outils, Hacker News, Product Hunt) publiés ces 48 dernières heures (rapport généré à 07:16).

## Synthèse du jour

Les dernières heures sont marquées par une série d’incidents affectant les services Claude, soulignant les défis de fiabilité des assistants de codage. Parallèlement, de nombreux acteurs annoncent de nouveaux agents ou améliorations d’assistants IA, notamment autour de Claude Code, Codex et DeepSeek, tandis que les grands fournisseurs cloud publient des architectures et des optimisations pour le déploiement d’agents à grande échelle. Le paysage open‑source continue de s’enrichir avec des bibliothèques dédiées à la visualisation, au benchmarking et à l’intégration de modèles LLM. Enfin, la gouvernance du code IA gagne en visibilité avec des annonces de dépréciation de modèles, de scans de sécurité et d’outils de mitigation des risques.

*Vérifiée : chaque affirmation est appuyée par au moins un titre.*

## À lire en priorité

- [Routage des requêtes d’agent de codage vers le bon modèle sur Amazon Bedrock avec NVIDIA NeMo Switchyard](https://aws.amazon.com/blogs/machine-learning/route-coding-agent-requests-to-the-right-model-on-amazon-bedrock-with-nvidia-nemo-switchyard/) — *AWS Machine Learning*, 13/11 23:30 · **8/10** (Routing dynamique sur Bedrock + NeMo, solution concrète pour agents)
  *Titre original : Route coding agent requests to the right model on Amazon Bedrock with NVIDIA NeMo Switchyard*
  > Coding agents work in tasks, and the number that matters is cost per solved task, not price per token. In this post, you use the AWS CDK to deploy LiteLLM with the NVIDIA NeMo Switchyard routing plugin on Amazon Bedrock, then measure cost per solved task for a routed model group against single-model
- [Comment gérer la dégradation du contexte lorsqu’on enchaîne plusieurs outils dans un agent IA ?](https://dev.to/kling4ai-production/how-do-you-handle-context-degradation-when-chaining-multiple-tools-in-an-ai-agent-4o38) — *dev.to*, 14/11 07:05 · **7/10** (Nouvelle problématique technique sur les agents IA, utile aux développeurs)
  *Titre original : How do you handle context degradation when chaining multiple tools in an AI Agent?*
  > As tool ecosystems grow and agents call multiple external tools in sequence, prompt bloat and verbose tool returns start degrading context rapidly. In your workflows, do you prefer: Truncating or summarizing previous tool outputs before sending the next turn? Spawning isolated subagents and passing 
- [MLOps en production chez GS Caltex avec Amazon SageMaker Canvas, partie 1](https://aws.amazon.com/blogs/machine-learning/production-mlops-at-gs-caltex-with-amazon-sagemaker-canvas-part-1/) — *AWS Machine Learning*, 14/11 00:22 · **7/10** (Cas d'usage MLOps réel avec SageMaker Canvas, très concret)
  *Titre original : Production MLOps at GS Caltex with Amazon SageMaker Canvas, part 1*
  > GS Caltex connects Amazon SageMaker Canvas to Amazon SageMaker Pipelines so process engineers' no-code models run in production. This post shows how ML engineers reuse validated preprocessing flows and models, cutting deployment from about a week to a few hours and running batch inference every 30 m
- [Patrons d’architecture pour un démarrage de session rapide sur le runtime Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime/) — *AWS Machine Learning*, 13/11 23:02 · **7/10** (Patrons d'architecture pour démarrage rapide, guide pratique)
  *Titre original : Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime*
  > Amazon Bedrock AgentCore runtime V2 snapshots your initialized environment and restores it for each new session, so session start no longer grows with image size. This post explains how V2 starts a session, how to measure session start time, and four patterns to keep work off the first request.
- [OpenFold3 sur Amazon SageMaker JumpStart : prédire les structures biomoléculaires](https://aws.amazon.com/blogs/machine-learning/openfold3-on-amazon-sagemaker-jumpstart-predict-biomolecular-structures/) — *AWS Machine Learning*, 13/11 22:53 · **7/10** (OpenFold3 sur SageMaker, outil de recherche biomoléculaire exploitable)
  *Titre original : OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures*
  > Deploy OpenFold3-preview from Amazon SageMaker JumpStart to predict 3D structures of proteins, DNA, RNA, and ligand complexes in your own AWS account. The post covers asynchronous inference, multi-GPU parallelism, bringing your own MSAs for accuracy and privacy, and scaling to zero to reduce cost.

## Fiabilité et incidents des services IA (8)

De nombreux titres signalent des pannes, des problèmes d’authentification ou des dégradations de disponibilité sur les services Claude et d’autres assistants de codage, montrant que la fiabilité reste un enjeu critique.

- [Anthropic confirme des échecs d’authentification sur Claude.ai et Claude Code](https://news.google.com/rss/articles/CBMirwFBVV95cUxPYmhFRUJlYzRLeGJ5aFVUTkhrTENzdlZ0RWw4OU9fY0JhcDByd3l1TjN2NkhqdDktTjdfRzY4bzl3ZUFzRnBfRGtMQnY5WW1yMUc4ZHZ0a28zaEpHVTU3a0dscWota0dTbnBmaGxNaV91cTc4MGpCSlJ6X2ZUMVpSUmdPQ3BpVDdXd2ZVR0dxeGtPSHFhbW44aUtBdE93c1cxalotRGpwck5qZ2swLUtv?oc=5) — *Foro3D*, 14/11 00:01 · **5/10** (Problème d'authentification, important pour disponibilité mais pas nouveauté)
  *Titre original : Anthropic confirms authentication failures in Claude.ai and Claude Code*
- [Anthropic enquête sur les problèmes de connexion à Claude.ai et Claude Code](https://news.google.com/rss/articles/CBMikgFBVV95cUxNMGtzWDZ6QWxWaHJoektabThHTHZrc0liWXI4ckRzT0hOVDB5MHFoY3c1SHZmU1dweFdPbHZtZVFETzRYMzktZTRVanpYNTk5Z1JhZ1lPX1Y5WXhJNVVtclYtNmttOUM1dlg5cEZWMHF5a1dfVHpRZnJPZ25PYldZQW1WTnpZSVhfXzcybG5QRWZfdw?oc=5) — *JournalArta*, 13/11 21:16 · **4/10** (Investigation de problèmes de login, incident de service)
  *Titre original : Anthropic Investigates Login Problems for Claude.ai and Claude Code*
- [Claude en panne le 13 novembre : ce qui s’est passé](https://news.google.com/rss/articles/CBMitAFBVV95cUxNVU1vN3ZYc0NaUzdXQlh5bjFPemZXWC0wTmpXVUo4OTl2aGdpakNVN1Jua0hvaDdmV0hRMmNqTjByVHVYbGtQOUdpSm9NNUxoSWItUGR4LUt2bmIzTjJuQnJaTlpqMENJcnY2Q1JFQkwzUURubHdfM0s1dWlqX1p0MHk2dFRGdUFYZXA4S2dpUmM3a0Rvc05qcDBkUjB1T3ZsUkVNQ3RTVUZHa2dER1NmYjJKTnE?oc=5) — *Meteora Web*, 13/11 18:12 · **4/10** (Annonce d'indisponibilité, information ponctuelle)
  *Titre original : Claude Down on November 13, What Happened*
- [Claude signale une hausse des erreurs sur claude.ai, l’API et Claude Code](https://news.google.com/rss/articles/CBMickFVX3lxTE9KLW8xU0NaUlpzbWdYSHdFb1Zfbmh6YnFpN2g5S05HQ3R0NnBRMGFwVTNVR0I3bk85d0dHTEJ3RXJTWTFPMXdZakJXOW9RS1pPLWRZN1lhNFVsMlFya0xTYXBNOTJrNTloOVFUeGdWLWlQUQ?oc=5) — *Technobezz*, 13/11 16:59 · **4/10** (Rapport d'erreurs Claude, incident de service)
  *Titre original : Claude reports elevated errors across claude.ai, API and Claude Code*
- [Claude IA en panne ? Anthropic confirme des problèmes d’authentification sur plusieurs services](https://news.google.com/rss/articles/CBMitgFBVV95cUxNU3pha0xaNFc0YVlCVkRaOWJYdWZNbEFsUEZxOXlFUFZUSzF2ekgwQjRXLUpodWtwY2hrWEJnamZER1FMblVZNHI5RHh3d2diX2c1d05MY3JURk5yWUFBSWNINUdpMUtFcFI5eERrU3FJd1RmbllIOEJmVmRxOHNYN0ExU0x0ZGJidHlFY3Q3eEJxQnRrR3JrbjNvMVQyMWo4aDF2MVRDUjRkWVBQSmNQNnB6SnQxUdIBvAFBVV95cUxQOUVKQl9nQm5MdnBFeUxDM0RVMmdnYVl3TUtNY0NCZWIyY1lySjJSWlFISFUtdW9FNkFUN09SMS1obVE1a1EtU2RJTTVzajZxZVpqOHdpc2hEMVpKMVRxRkRwUGE1eDQ4WmNoQmhZUXlSNlc3cnNGaHJ5SnJMRjhPb1dQYUxVODBGcVo0YVRadkpWSnl2N2ZuOUVONGp3OWFPRjMxVzFqVnpTOVdPeEJZd0s5Zi1iaEFJbEYwMg?oc=5) — *Jagran Josh*, 13/11 15:13 · **4/10** (Annonce d'incident Claude AI, peu de profondeur)
  *Titre original : Is Claude AI Down? Anthropic Confirms Authentication Issues Across Multiple Services*
- [Claude IA en panne, mise à jour du statut : services incluant Claude API, Claude Code et les connecteurs indisponibles](https://news.google.com/rss/articles/CBMi5wFBVV95cUxOZTdnUkxqa3VTT3JMdVF5SnVkN0lKRUVVTTRSbmc3OGhKZUlVSnZCVTNrWDdra2hXOExXX04ybDV6MWRZOXRtMXlVSG52WE9LRTNpSDFsYjVncnlWc2Z3OG1tUVpwQWtueEE0R3ZMbzVwbXhyZnN6dGRVREdId3BCZHJkdW1Xd180RUdzZmg4a2N0a2UtcV80RlY3S2gybThBdG0zMTM0OGNGcmpqbmdsdFk3Y0JSY1ZXN2pxZ0YzSlhWUFlEeGdSOU9Ucll3MmdseWsxaEo2U2JVNFNlcmxWUnNMdGJoN0nSAewBQVVfeXFMTnpvYmdxVm9WUElxYVh3cXdtc1FSaWJTOVZCVDBtSkhHTlpjalRJaHM1ZmQ4d2NsTXdWcUJWYi1aTUZLWmJXX2lkb090MWNvX3JaMF9GRDhjc2pTTlhtT0xyMnV2Qm5tdDJpZE9GMUVwUzdHRzhIeXdyX0pWQXFCcEVxdWh6NEJZMzlscC1NWVFpWlMzaW1hNDZMU1NSR2FUTWtORHg0Xzg2TnRvRmVFekVnTkZnTTd2TmNEbnF2Q3RFUHRld2xHWjBHaFRocFVKVmlvWVJwT1UwanRzMGNTT1RxdzhFRnAzQmpjSkE?oc=5) — *Livemint*, 13/11 15:11 · **4/10** (Mise à jour d'état de service, information de disponibilité)
  *Titre original : Anthropic Claude AI down, Status update: Services including Claude API, Claude Code, connectors down*
- [Panne de Claude : Anthropic confirme des problèmes d’authentification affectant Claude.ai, Claude Code et la console](https://news.google.com/rss/articles/CBMi7wFBVV95cUxObTRkYXJBX1NLOWl0dDFKSC1GUGFlNjBxTWF0NFVlWHRUbDhrUjZnYjNQenQ2TDlUdGtlcDZRT2NLTmhGTWRoSHJCOXRRSUpOS2RLa25TT1FVcVdoMDZvSHdROUlPV0VZV1VfZ2NaTEtlbEFkb1Btc1V6ald4dHJiNjV2MFN5ZHlMOGhjaTNvU3E5OS1RRHd1TTlqbDJxeUdISXNCQmd1bmxmajVSRkRMcmJrcE01R2prZUlBbVZqY3FqNGl2UldZdW1hXzhnVGk4VlhtSXhIXzJQMEtxbjBmUDlXb3pVQ0x3bkR3dlA4VdIB9AFBVV95cUxNYldBOHhBVUMzdTJwcTJDX3hFbkZva1I3WldBUjZ1LUdJYTROT1BYV3llQWtTWWVBNGhfbmN1V3c3eVlSaDdPSmNlU1d5NG9vVEF4Z1IwYkpsaVpIM2F6bjJWZWVOTjVPZkN2Tm04TFRkN0g4TW44QXdHUGxEd0VKbEY0a3ItNzZKRWlKVlV3R3pudkZmWE9NOXluY21sdTBDUVVzcjg5V3EwWG5LWngxSmZDUEQ4dFpzbXJtLTRhMkM4OXgxSW9IZGQwcG9JdWZmcDdSaWhRN3Y2ZEV5V1htdWlvenIyTy1MeWNtQzNGSEpkcE1R?oc=5) — *Moneycontrol.com*, 13/11 13:10 · **4/10** (Outage Claude, information de disponibilité)
  *Titre original : Claude outage: Anthropic confirms authentication issues affecting Claude.ai, Claude Code and Console*
- [GitHub Copilot a connu une disponibilité réduite pour certains modèles GPT](https://news.google.com/rss/articles/CBMickFVX3lxTE9mWS1BSDBtSHhUNlJxbHlyZlk4RnZ6WWxMVEQ4Xzd2WkV5cS1oUjZVX250SE5DcEM4d0VIRVlvdWM2SWJKVEtnSTRMekppYWVkZjlJcjk5LVZsWTRTZy1xLUFKTzZmVXJtWTJpN2NvUk9TUQ?oc=5) — *Technobezz*, 13/11 22:27 · **4/10** (Dégradation de disponibilité Copilot, incident ponctuel)
  *Titre original : GitHub Copilot experienced degraded availability for some GPT models*

## Agents et assistants de codage (19)

Une vague d’annonces porte sur des agents de programmation ou des assistants basés sur Claude, Codex, DeepSeek, ou d’autres modèles, avec des améliorations de performances, de nouvelles fonctionnalités ou des études de marché.

- [Routage des requêtes d’agent de codage vers le bon modèle sur Amazon Bedrock avec NVIDIA NeMo Switchyard](https://aws.amazon.com/blogs/machine-learning/route-coding-agent-requests-to-the-right-model-on-amazon-bedrock-with-nvidia-nemo-switchyard/) — *AWS Machine Learning*, 13/11 23:30 · **8/10** (Routing dynamique sur Bedrock + NeMo, solution concrète pour agents)
  *Titre original : Route coding agent requests to the right model on Amazon Bedrock with NVIDIA NeMo Switchyard*
  > Coding agents work in tasks, and the number that matters is cost per solved task, not price per token. In this post, you use the AWS CDK to deploy LiteLLM with the NVIDIA NeMo Switchyard routing plugin on Amazon Bedrock, then measure cost per solved task for a routed model group against single-model
- [Comment gérer la dégradation du contexte lorsqu’on enchaîne plusieurs outils dans un agent IA ?](https://dev.to/kling4ai-production/how-do-you-handle-context-degradation-when-chaining-multiple-tools-in-an-ai-agent-4o38) — *dev.to*, 14/11 07:05 · **7/10** (Nouvelle problématique technique sur les agents IA, utile aux développeurs)
  *Titre original : How do you handle context degradation when chaining multiple tools in an AI Agent?*
  > As tool ecosystems grow and agents call multiple external tools in sequence, prompt bloat and verbose tool returns start degrading context rapidly. In your workflows, do you prefer: Truncating or summarizing previous tool outputs before sending the next turn? Spawning isolated subagents and passing 
- [Le problème de contexte : la vraie cause de la rupture des agents IA à grande échelle](https://thenewstack.io/elastic-ai-context-gap/) — *The New Stack*, 13/11 19:15 · **7/10** (Analyse du problème de contexte, enjeu clé pour les agents à grande échelle)
  *Titre original : The context problem: It’s what’s really breaking AI agents at scale*
  > AI models are getting smarter, tokens are getting cheaper, and agents are improving. But the context gap sits between the The post The context problem: It’s what’s really breaking AI agents at scale appeared first on The New Stack .
- [La distillation de brouillon en parallèle de branches accélère la génération de texte de 3,6 fois](https://dev.to/olaughter/branch-parallel-draft-distillation-speeds-text-generation-36x-1efk) — *dev.to*, 14/11 07:00 · **6/10** (Amélioration de génération texte, mais impact limité pour le code)
  *Titre original : Branch‑parallel draft distillation speeds text generation 3.6*
  > SpecOPD stretches the viable draft window by over 40 %, as reported by the authors. The same mechanism also collapses inference latency to a fraction of its autoregressive baseline, delivering roughly a 3.6× speed boost in real‑world settings. Until now, speculative decoding has been bottlenecked by
- [Artificial Analysis étend l’index des agents de codage à 322 tâches dans la version 2.1](https://news.google.com/rss/articles/CBMiW0FVX3lxTE4yQUdrTDY2czRLYUthRGRoamlUbFdSQUE4S0F3WEt0cmN0VUU2RHIyZERXZ2ZWV0xvekdsUWFVaFhlMEFlVFBsUjAwMl9USkhFcjk1clR6TDBZZDg?oc=5) — *www.tokenpost.com*, 14/11 01:23 · **6/10** (Extension de l'index des tâches d'un agent, pertinence pour les praticiens)
  *Titre original : Artificial Analysis Expands Coding Agent Index to 322 Tasks in V2.1*
- [Artificial Analysis Coding Agent Index v2.1 rafraîchit ses tests, et deux modèles Claude partagent la première place](https://news.google.com/rss/articles/CBMie0FVX3lxTE8yTkFXUk0wVEtZd2NDMEdDZWc4Z1FEQ0duazJoNVc0eUVranl5bU1xS0xSNjIyZVVvUkJDWTZadHd1cnlvOEJ5dFNhYWtnR0tuc2F0V1llc3JBUnhUTGF1SE5DUWtDTDN3Wno4czBfcE9uSXBsUi0zVFV5SQ?oc=5) — *Crypto Briefing*, 14/11 01:10 · **6/10** (Mise à jour de tests, deux modèles Claude en tête, intérêt pour benchmark)
  *Titre original : Artificial Analysis Coding Agent Index v2.1 refreshes its tests, and two Claude models tie at the top*
- [Autonomous (YC F25) recrute des MTS pour créer des agents IA qui gèrent votre patrimoine](https://atg.science/careers) — *Hacker News*, 13/11 22:01 · **6/10** (Startup qui recrute pour agents de gestion patrimoniale, appli pratique)
  *Titre original : Autonomous (YC F25) is hiring MTS to build AI agents that manage your wealth*
  > Article URL: https://atg.science/careers Comments URL: https://news.ycombinator.com/item?id=50489589 Points: 0 # Comments: 0
- [Revue de OpenAI Codex : il a corrigé chaque bug que je lui ai soumis](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBVd00yMXR4X3U4SVdRemVDWEZ6RHl5RGdteHJiYTQxRGZ3VG1kRGdIVWluQWN0N1Y0YkxLSzR4VjF2LUV1Q3ZDOWVkNUVWWUNjRWFF?oc=5) — *Unite.AI*, 13/11 19:23 · **6/10** (Revue de Codex montrant robustesse, utile aux développeurs)
  *Titre original : OpenAI Codex Review: It Fixed Every Bug I Threw at It*
- [L’agent de codage de DeepSeek est trop propre pour son propre bien – et les benchmarks le pénalisent](https://thenewstack.io/deepseek-harness-cleanup-benchmark/) — *The New Stack*, 13/11 18:56 · **6/10** (Benchmarks DeepSeek, mise en lumière de limites de propreté du code)
  *Titre original : DeepSeek’s coding agent is too tidy for its own good — and benchmarks are punishing it*
  > DeepSeek’s open-source coding agent is losing points on a major benchmark for a habit developers usually treat as good practice: The post DeepSeek’s coding agent is too tidy for its own good — and benchmarks are punishing it appeared first on The New Stack .
- [Claude for Manufacturing d’Anthropic intègre directement l’IA aux logiciels d’usine pour automatiser les flux de travail industriels](https://the-decoder.com/anthropics-claude-for-manufacturing-plugs-ai-directly-into-factory-software-to-automate-industrial-workflows/) — *The Decoder*, 13/11 17:37 · **6/10** (Claude pour manufacturing, intégration industrielle concrète)
  *Titre original : Anthropic's Claude for Manufacturing plugs AI directly into factory software to automate industrial workflows*
  > Anthropic's new Claude for Manufacturing plugin connects the AI directly to Autodesk Fusion, Oracle NetSuite, and Infor. Its 17 specialized skills let the AI draft quotes, compare suppliers, and place backup orders when deliveries are delayed, all after human approval. The plugin doesn't control phy
- [Gondola double son chiffre d’affaires grâce à Codex et ChatGPT d’OpenAI](https://news.google.com/rss/articles/CBMicEFVX3lxTE04T2l2TEJFajQ5azdZUmFoMmszRnJqTm1WU0szSDZDNVNhOXAyeGR2RjhWNFhLSlJaMVM3NUpDQWY4RTZ1MUR2UVAyMERfY0kwcWREdjB3Mkp5cC1TWVcxNDhOSkpBc2h3Ry01SGJ2Nmc?oc=5) — *blockchain.news*, 14/11 06:56 · **5/10** (Cas d'usage commercial, peu de portée technique)
  *Titre original : Gondola Doubles Revenue Using OpenAI's Codex and ChatGPT*
- [J’ai installé un studio de design de 42 postes dans mon agent de codage](https://news.google.com/rss/articles/CBMigAFBVV95cUxPSUlrdXJMdFh2V3JyMEF4UjJDVEJCV2tOem41V2hoNkczaVVqYlFFcUp0UkctQWdMY01sRXh5V3otd0hPQXduNnJpU1pWNU14eEstV3VBb2V3bjFhWXVkQkg2QzlraVhFLTcwV2VxRUJteDAySEk3UnNXd0lyWXBfUQ?oc=5) — *HackerNoon*, 14/11 05:41 · **5/10** (Expérience personnelle, intéressante mais peu généralisable)
  *Titre original : I Put a 42-Desk Design Studio Inside My Coding Agent*
- [ArmourCode publie l’outil Hooks pour bloquer les risques de Claude Code](https://news.google.com/rss/articles/CBMijAFBVV95cUxPOFRRX2RTN3F4aWx4U3FJeEFwRnhTcVhQaTRfekR0V09seEVEVHQ3UnJ0cE9jbmtpYXh0SFVGV3BSeDcyR3pfbFRtSnQ4Ny1BZ21ncDhralBEQmtPS1NDck1DRlVRaVFpa2RIeGV5aW14MzlfVjNNVmgzQ2g0allRTTBSbTRMTjdYRWg1Yg?oc=5) — *IT Brief UK*, 13/11 18:15 · **5/10** (Outil hooks pour bloquer risques Claude Code, appli pratique)
  *Titre original : ArmourCode releases hooks tool to block Claude Code risk*
- [Top 12 des assistants de codage IA pour les entreprises en 2027 : GitHub Copilot, Claude Code, Codex, Cursor et AWS Kiro comparés](https://news.google.com/rss/articles/CBMihAJBVV95cUxQS01QbnhrNWFKOGFidENBNnFOVnE2WUhMdEFzSkVESkJab3ZjeHpaZEw2WTNVVDdJSmJ6Y3J6aUFWalBLZkQ3MUhvcV9sMUJPRThva3FUbUZrblZQRUlMcFRqS3pJUF9jVWsyczdjU2tiV0lQNl9rdzYxWktZZXBNNmZGSk1wNU52akRMUWYyaVZodVVQYWxBdVEwbHJrREpSTFc3b3ZveFVQd2ZBZTRNQUtPMXM1WU1NaU5UTE90NXJkQ1ZnTFhTaFNlSHlOVF84Ymw2ZUVQMHl3YkpKUzhzMmpjemxGRXJYM0lkTm5lX19zS2hnbExRSHpQZHRYemRWN280SNIBhAJBVV95cUxQS01QbnhrNWFKOGFidENBNnFOVnE2WUhMdEFzSkVESkJab3ZjeHpaZEw2WTNVVDdJSmJ6Y3J6aUFWalBLZkQ3MUhvcV9sMUJPRThva3FUbUZrblZQRUlMcFRqS3pJUF9jVWsyczdjU2tiV0lQNl9rdzYxWktZZXBNNmZGSk1wNU52akRMUWYyaVZodVVQYWxBdVEwbHJrREpSTFc3b3ZveFVQd2ZBZTRNQUtPMXM1WU1NaU5UTE90NXJkQ1ZnTFhTaFNlSHlOVF84Ymw2ZUVQMHl3YkpKUzhzMmpjemxGRXJYM0lkTm5lX19zS2hnbExRSHpQZHRYemRWN280SA?oc=5) — *InfotechLead*, 13/11 17:35 · **5/10** (Comparatif d'assistants IA, vue d'ensemble mais peu de nouveauté)
  *Titre original : Top 12 AI Coding Assistants for Enterprises in 2027: GitHub Copilot, Claude Code, Codex, Cursor and AWS Kiro Compared*
- [Keyword Search associe un modèle d’embedding 8 B au choix des outils d’agent](https://towardsdatascience.com/keyword-search-tied-an-8b-embedding-model-at-picking-agent-tools/) — *Towards Data Science*, 13/11 17:30 · **5/10** (Recherche par mots‑clés vs embedding, résultat intéressant mais technique)
  *Titre original : Keyword Search Tied an 8B Embedding Model at Picking Agent Tools*
  > On 200 ToolRet questions and up to 3,794 tools, BM25 ran about 40x faster than BGE-large on just a CPU, and full tool docs made it the best setup tested. The post Keyword Search Tied an 8B Embedding Model at Picking Agent Tools appeared first on Towards Data Science .
- [Perplexity lance Decider v1.3 : modèles de décision à poids ouverts avec fonction Locate](https://www.marktechpost.com/2026/11/13/perplexity-decider-v1-3-open-weight-decision-models-locate/) — *MarkTechPost*, 13/11 17:10 · **5/10** (Décision model Decider v1.3, ajout fonctionnel)
  *Titre original : Perplexity Releases Decider v1.3: Open-Weight Decision Models Add Locate*
  > Perplexity Decider v1.3 and Flash v1.3 are open-weight decision models that return probabilities, not text. Version 1.3 adds Locate for span extraction and reports 91.6% mean accuracy on 63 query-classification tasks. The post Perplexity Releases Decider v1.3: Open-Weight Decision Models Add Locate 
- [xAI mise en avant des outils de codage IA et de son produit d’agent Grok Bot](https://news.google.com/rss/articles/CBMib0FVX3lxTE5JajZVajVuWGxZRW55Z0ZSaHFGZFFSNXc4R3pRSmttbjRWNjN2ZnUzTzNnZzYwMUZKa0hyNGU0cEE4b01rN1oxUFU1TmRBa21KbkR4TU0zclFvWlBWeXhLaEVyd0V1WHU1TkhwOHBGRQ?oc=5) — *Crypto Briefing*, 13/11 15:09 · **5/10** (Priorisation des outils de codage par xAI, orientation produit)
  *Titre original : xAI prioritizes AI coding tools and its Grok Bot agent product*
- [Shield aide les techniciens à transférer le travail des portails hérités à OpenAI](https://openai.com/business/customer-stories/shield) — *OpenAI*, 13/11 09:00 · **5/10** (Shield facilite migration legacy avec OpenAI, usage concret)
  *Titre original : Shield helps technicians hand off legacy portal work with OpenAI*
  > Shield uses OpenAI to help IT technicians hand off work in legacy portals. Its Forge agents navigate systems so technicians can focus on issues needing their judgment.
- [Vibe coding pour les créatifs : créez vos propres outils sans programmer](https://news.google.com/rss/articles/CBMisgFBVV95cUxNeWp0ZHFUTnhNZk5sdmhfblZreDVIdWV5YTVwb3lrYS1NT1FpeVVpVllVWnJsOGFQZ0FHWFdjZHJGSUFtaU16bWZ0Z3pxeTlJSFotbFR4dGFHVEFpVjVqUmFuZXNuOUNONzBVUVEzS0FOVTV6N3EzSEIybDFBZlJoWXFJZThHVDh3WHdlTzF4MGltSVFJUmx1V2IwMEZEWXV4ZEgtOEVISkItTGJOSFJxQ2p3?oc=5) — *Foro3D*, 13/11 14:15 · **4/10** (Outil low‑code pour créatifs, peu centré IA)
  *Titre original : Vibe coding for creatives: build your own tools without programming*

## Plateformes et infrastructures IA (9)

Les fournisseurs cloud (AWS, Google, Amazon Bedrock) publient des guides, des architectures et des optimisations pour le déploiement d’agents IA, incluant SageMaker Canvas, Bedrock AgentCore, Gemini 4 Hydrogen et des outils TPU.

- [MLOps en production chez GS Caltex avec Amazon SageMaker Canvas, partie 1](https://aws.amazon.com/blogs/machine-learning/production-mlops-at-gs-caltex-with-amazon-sagemaker-canvas-part-1/) — *AWS Machine Learning*, 14/11 00:22 · **7/10** (Cas d'usage MLOps réel avec SageMaker Canvas, très concret)
  *Titre original : Production MLOps at GS Caltex with Amazon SageMaker Canvas, part 1*
  > GS Caltex connects Amazon SageMaker Canvas to Amazon SageMaker Pipelines so process engineers' no-code models run in production. This post shows how ML engineers reuse validated preprocessing flows and models, cutting deployment from about a week to a few hours and running batch inference every 30 m
- [Patrons d’architecture pour un démarrage de session rapide sur le runtime Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime/) — *AWS Machine Learning*, 13/11 23:02 · **7/10** (Patrons d'architecture pour démarrage rapide, guide pratique)
  *Titre original : Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime*
  > Amazon Bedrock AgentCore runtime V2 snapshots your initialized environment and restores it for each new session, so session start no longer grows with image size. This post explains how V2 starts a session, how to measure session start time, and four patterns to keep work off the first request.
- [OpenFold3 sur Amazon SageMaker JumpStart : prédire les structures biomoléculaires](https://aws.amazon.com/blogs/machine-learning/openfold3-on-amazon-sagemaker-jumpstart-predict-biomolecular-structures/) — *AWS Machine Learning*, 13/11 22:53 · **7/10** (OpenFold3 sur SageMaker, outil de recherche biomoléculaire exploitable)
  *Titre original : OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures*
  > Deploy OpenFold3-preview from Amazon SageMaker JumpStart to predict 3D structures of proteins, DNA, RNA, and ligand complexes in your own AWS account. The post covers asynchronous inference, multi-GPU parallelism, bringing your own MSAs for accuracy and privacy, and scaling to zero to reduce cost.
- [llama.cpp v1.0.0 : une base plus solide pour l’écosystème IA local](https://huggingface.co/blog/ggml-org/llama-cpp-v1) — *Hugging Face*, 13/11 15:05 · **6/10** (llama.cpp v1.0.0, base solide pour IA locale, impact développeurs)
  *Titre original : llama.cpp v1.0.0 : A stronger foundation for the local AI ecosystem*
- [Google ajoute l’orchestrateur multi-modèle Gemini 4 Hydrogen à Antigravity](https://www.infoworld.com/article/4248403/google-adds-multi-model-orchestrator-gemini-4-hydrogen-to-antigravity.html) — *InfoWorld*, 13/11 13:37 · **6/10** (Orchestrateur multi‑modèle Gemini 4 Hydrogen, nouveauté majeure)
  *Titre original : Google adds multi-model Orchestrator, Gemini 4 Hydrogen, to Antigravity*
  > Google is adding a new feature, Orchestrator, to Antigravity, its AI-powered development environment, to help enterprises improve software development efficiency by automatically coordinating multiple Gemini models, including the newly introduced Gemini 4 Hydrogen. The new feature, which allows deve
- [Google lance TPU Sync : transfert de cache KV open‑source pour les TPU](https://www.marktechpost.com/2026/11/13/google-tpu-sync-kv-cache-transfer-library/) — *MarkTechPost*, 13/11 11:32 · **6/10** (TPU Sync open‑source, améliore performances TPUs, intérêt technique)
  *Titre original : Google Releases TPU Sync: Open-Source KV Cache Transfer for TPUs*
  > Google released TPU Sync, an open-source C++ library that moves KV caches and weights across TPU HBM, host DRAM, storage and network. Google reports over 90% lower KV transfer latency on 235B to 480B MoE models. The post Google Releases TPU Sync: Open-Source KV Cache Transfer for TPUs appeared first
- [Google publie Gemini 4 Hydrogen : 2,5 fois plus rapide que Gemini 3.8 Flash](https://www.marktechpost.com/2026/11/13/google-gemini-4-hydrogen/) — *MarkTechPost*, 13/11 10:45 · **6/10** (Gemini 4 Hydrogen plus rapide, amélioration de modèle clé)
  *Titre original : Google Releases Gemini 4 Hydrogen: 2.5x Faster Than Gemini 3.8 Flash*
  > Google released Gemini 4 Hydrogen, a fast agentic model with a 1M-token window, 4 thinking levels and $1.50/$7.50 pricing. Google reports a 51 Artificial Analysis score and 57% on Terminal-Bench 4.1. The post Google Releases Gemini 4 Hydrogen: 2.5x Faster Than Gemini 3.8 Flash appeared first on Mark
- [Gemini 4 Hydrogen intégré à GitHub Copilot](https://github.blog/changelog/2026-11-13-gemini-4-hydrogen-in-github-copilot) — *GitHub Changelog*, 13/11 19:23 · **5/10** (Intégration Gemini 4 Hydrogen, nouveauté mais peu de détails)
  *Titre original : Gemini 4 Hydrogen in GitHub Copilot*
  > Gemini 4 Hydrogen, Google’s latest Flash model, is now generally available in GitHub Copilot. It is designed for fast, efficient agentic coding, tool use, and multistep workflows, with improved instruction… The post Gemini 4 Hydrogen in GitHub Copilot appeared first on The GitHub Blog .
- [Avec Gemini 4 Hydrogen, Google Search s’offre une mise à jour majeure](https://www.blogdumoderateur.com/gemini-4-hydrogen/) — *Blog du Modérateur*, 13/11 10:52 · **4/10** (Mise à jour Google Search via Gemini, peu de détails techniques)
  *Titre original : Avec Gemini 4 Hydrogen, Google Search s’offre une mise à jour majeure*
  > Google assure que son moteur de recherche traite mieux les requêtes complexes grâce à Gemini 4 Hydrogen. Le modèle débarque aussi dans l’application Gemini, dans l’API et dans Antigravity.

## Bibliothèques, outils et releases open‑source (2)

Des projets open‑source et des bibliothèques spécialisées (datasette‑cluster‑map, datasette‑leaflet, llm‑gemini, SimReady, XYBench) sont publiés, offrant de nouvelles capacités pour la visualisation, le benchmarking ou l’intégration de modèles LLM.

- [XYBench : aider à résoudre le problème derrière la question](https://huggingface.co/blog/allenai/xybench) — *Hugging Face*, 13/11 18:02 · **5/10** (XYBench, approche méthodologique pour questions, intérêt limité)
  *Titre original : XYBench: Helping with the problem behind the question*
- [Agent‑desktop pilote vos applications sans que vous ayez à regarder l’écran](https://korben.info/agent-desktop.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 13/11 11:57 · **3/10** (Produit grand public, peu d'IA centrale)
  *Titre original : Agent-desktop pilote vos applis sans regarder l'écran*
  > agent-desktop, de Vercel Labs, fait piloter vos applications de bureau par un agent IA en lisant l'arbre d'accessibilité plutôt que des captures d'écran. Essai sur Mac, avec TextEdit et une appli Electron, et la limite qui compte.

## Gestion et gouvernance du code IA (4)

Des annonces portent sur la dépréciation de modèles, la gestion des scans de sécurité, les hooks de blocage de risques et les politiques de mise à jour, reflétant une prise de conscience croissante de la gouvernance du code généré par IA.

- [Dépréciation prochaine de certains modèles GitHub Copilot en décembre](https://github.blog/changelog/2026-11-13-upcoming-deprecation-of-selected-github-copilot-models-in-december) — *GitHub Changelog*, 13/11 21:40 · **5/10** (Dépréciation de modèles Copilot, impact limité)
  *Titre original : Upcoming deprecation of selected GitHub Copilot models in December*
  > We will deprecate the following models across all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions) on December 14, 2026: Model Deprecation date… The post Upcoming deprecation of selected GitHub Copilot models in December appeared first on T
- [Prise en charge de GitHub Enterprise Server dans l’application GitHub Copilot](https://github.blog/changelog/2026-11-13-github-enterprise-server-support-in-the-github-copilot-app) — *GitHub Changelog*, 13/11 19:27 · **5/10** (Support Enterprise Server dans l'app Copilot, fonctionnalité ciblée)
  *Titre original : GitHub Enterprise Server support in the GitHub Copilot app*
  > You can now bring your work on GitHub Enterprise Server (GHES) into the GitHub Copilot app. Add your GHES account to work with remote repositories, issues, and pull requests. This… The post GitHub Enterprise Server support in the GitHub Copilot app appeared first on The GitHub Blog .
- [Gestion du scan IA des dépôts via l’API REST](https://github.blog/changelog/2026-11-13-manage-ai-scan-for-repositories-using-the-rest-api) — *GitHub Changelog*, 13/11 13:22 · **5/10** (API pour scan IA, fonctionnalité pratique)
  *Titre original : Manage AI Scan for repositories using the REST API*
  > You can now turn GitHub code scanning’s AI Scan for repositories on or off with the REST API at the organization and repository levels. This public preview adds a repository_scan… The post Manage AI Scan for repositories using the REST API appeared first on The GitHub Blog .
- [Ce que les agents IA accélèrent dans la recherche de doctorat, et ce qu’ils ne peuvent pas](https://towardsdatascience.com/what-ai-agents-speed-up-in-phd-research-and-what-they-cant/) — *Towards Data Science*, 13/11 14:30 · **5/10** (Analyse usage agents en recherche PhD, perspectives limitées)
  *Titre original : What AI Agents Speed Up in PhD Research, and What They Can't*
  > A PhD student in ML and ecology on why faster code, experiments, and drafts don't fix data with a backstory, and three predictions for how labs will change. The post What AI Agents Speed Up in PhD Research, and What They Can't appeared first on Towards Data Science .

## Autres articles (8)

- [Comment apprendre aux agents IA à rechercher comme des experts humains](https://thenewstack.io/ai-agents-retrieval-agent-ready-schema/) — *The New Stack*, 13/11 15:50 · **7/10** (Guide pour enseigner la recherche aux agents, pratique et applicable)
  *Titre original : Here’s how to teach AI agents to search like human experts*
  > Agentic retrieval is a hot topic for a reason: Every company wants to automate work, but they often just are The post Here’s how to teach AI agents to search like human experts appeared first on The New Stack .
- [Google publie en open source Ambient Quality Agent (AQuA) pour diagnostiquer les pannes d’agents IA en production](https://www.infoq.com/news/2026/11/google-ambient-agent-prod/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 13/11 14:53 · **7/10** (Open source d'AQuA pour diagnostiquer pannes d'agents, outil précieux)
  *Titre original : Google Open Sources Ambient Quality Agent (AQuA) to Diagnose Production AI Agent Failures*
  > Google has open-sourced AQuA, a reference implementation that analyzes production AI agent sessions, verifies recurring failure patterns, and investigates root causes against deployed source snapshots. In a 32-session replay, developers reduced seat selection bypasses from 15 sessions to two and die
- [Anthropic permet maintenant l’auto‑hébergement des Claude Managed Agents ; contrainte : 8 heures d’attente si un risque de sécurité est détecté](https://thenewstack.io/self-hosted-claude-managed-agents/) — *The New Stack*, 13/11 22:29 · **6/10** (Self‑host de Claude Managed Agents, contrainte de latence notable)
  *Titre original : Anthropic now lets you self-host Claude Managed Agents. The catch? 8 hours to act if it flags a safety risk*
  > Anthropic has unveiled a self-hosted version of its platform for building and running AI agents. Self-hosted Claude Managed Agents, as The post Anthropic now lets you self-host Claude Managed Agents. The catch? 8 hours to act if it flags a safety risk appeared first on The New Stack .
- [Enquête exhaustive : cartographie des capacités et des lacunes des agents IA de codage autonomes](https://news.google.com/rss/articles/CBMisAFBVV95cUxNQzh6YnhoaUU3dXRLY2YtM0JwUXVwZjVXX01uYjk0aDJWaW5PZ2Y2ZWVlR2J6bzFFSmIxWC1oWEhKTE1yaWI1c0VwMC0weE94VFQ5RUtpTVdtTDFXRFEtWEdjeXlSbElDZE5wZi0ycVJkS1U1R0s3SmtVXy1xdXd5X0UtNk8xWmdJVkJISnRjaTZGM0Uxc2c3UndWcGhCak1EMV94NXREMjJ3UlgybVNZQQ?oc=5) — *Bioengineer.org*, 13/11 15:25 · **6/10** (Enquête exhaustive sur capacités des agents de codage autonomes)
  *Titre original : Comprehensive Scoping Survey Maps Capabilities and Gaps in Autonomous AI Coding Agents*
- [Claude Code Projects Beta propose les offres Pro à 20 $ et Max à 100 $](https://news.google.com/rss/articles/CBMijgFBVV95cUxPVFZGcFotSnB0bDhlczY0R1VhSEw1VkZhLU1Oc0ZGdEdsMldHTWRpNTRjYmdWWmk5UE1vbW40a0t5cHhmVE8tYzJYdFZDTFVQMDhyZXEyX3lmV2pmaWhlU3gyemxBMEdkVTdKQlA0VHpyamlTeUowNUgzX0tlNk5mN3pFY0VIS2k0TnVfMnV3?oc=5) — *FourWeekMBA*, 14/11 00:16 · **5/10** (Annonce tarifaire, peu d'impact technique)
  *Titre original : Claude Code Projects Beta Covers $20 Pro and $100 Max Plans*
- [Atelier Claude Code avec Provectus – Seattle](https://news.google.com/rss/articles/CBMijAFBVV95cUxQNV9pUFRCbzZWLWN5X3o3ZHVhOGFIaEFwWXZINXFpcXR3TmhsYjBsMVdySl9sQkloX1NMZ1pYSWJHTUhWYVV5b3Jua1hWc1czLVVFMFUwa0NOaTRsQzVqMWlaQXdmWlUtNWUydDB1SkozeFBKMXkwZjRRcGw5UnZNdkZQSmE0VEpXckhiVA?oc=5) — *GeekWire*, 13/11 15:36 · **5/10** (Workshop Claude Code, formation ciblée)
  *Titre original : Claude Code Workshop with Provectus – Seattle*
- [Comment vérifier la sortie d’un LLM local avec Ollama, Gemma 4 et Nimble](https://towardsdatascience.com/how-to-check-local-llm-output-with-ollama-gemma-4-and-nimble/) — *Towards Data Science*, 13/11 13:00 · **5/10** (Guide vérification sortie LLM locale, utile aux praticiens)
  *Titre original : How to Check Local LLM Output with Ollama, Gemma 4, and Nimble*
  > Gemma 4 E2B drafts the replies, Bespoke Labs' Nimble 9B picks accept, revise, or human review, and only flagged questions get a focused retry. The post How to Check Local LLM Output with Ollama, Gemma 4, and Nimble appeared first on Towards Data Science .
- [Meilleure formation Claude Code pour les équipes de développement : Paloren place les modifications révisées avant le code généré](https://news.google.com/rss/articles/CBMiqwJBVV95cUxQbDZrR2NSUjNmbHB6U2NybjNMSEwtTVdIcTlrUm9RX05HRWgwWkRnM1k0TXI3clpwbHhWbmJ6ZjRNMVVsWTRtVkNwLTRhbUhuQXJqOHVGX0ZLdkpyWHgyX2gtNEg3VkY5VjNvSDZ2OExaWHlBS3FNbVRSRTRnOWVtRzlHNnVUNHZoZXh0NUFMWlpCZ3ZJYzFTdzZiTnhMeF9CU2dfUGVnc3gzdkh2NTBzQTExYy1XVXZXWkNrOFZuOVdWNTRFR3YzeFpfcTJvbmJLWGFJeVBvYlFrZVhpN1BjQXV3Yy1XVUVMT090Q3JVN3U3MVUycGVsQTE5Vlg0WjlrWmRNNDdoREQ2SWtvc2I3QXZOS1lPNDFPNVNoN0RPdFBDc1A3QUtZZl9Faw?oc=5) — *WBOC TV*, 14/11 02:00 · **4/10** (Annonce produit, peu de nouveauté technique)
  *Titre original : Best Claude Code Training for Development Teams: Paloren Puts Reviewed Changes Ahead of Generated Code*

## Vidéos à regarder (10)

- [Build an AI Agent for $0! 🤖 | Complete AI Architecture Stack in 2026 #Shorts](https://www.youtube.com/watch?v=8jG2nEdfeoY) — *AWS with Jaymit*, 14/11 04:36
  > Présentation d'une architecture d'agents IA totalement gratuite en 2026, avec les outils et services nécessaires pour construire et déployer des agents sans frais.
- [Two AI coding tools, one rules file: Claude Code and Codex](https://www.youtube.com/watch?v=0b3YmZzZPaM) — *Linnet Builds*, 14/11 03:35
  > Démonstration de l'utilisation conjointe de Claude Code et Codex grâce à un seul fichier de règles, évitant la duplication du code de configuration.
- [AI open source models surge with new tools and memory frameworks](https://www.youtube.com/watch?v=6vP3SBiIXZc) — *Jake Parker*, 14/11 02:23
  > Analyse des nouveaux modèles IA open source et des frameworks de mémoire, incluant la mise à jour Pagemark 2.0 pour l'évaluation de pages web.
- [NCP-AAI 08/34: Tools, Function Calling and MCP | NVIDIA Agentic AI Professional](https://www.youtube.com/watch?v=GKGqMx-6Qrk) — *Core Concept Learning*, 14/11 01:06
  > Cours sur les outils, l'appel de fonctions et le protocole MCP pour l'examen NVIDIA Agentic AI Professional, expliquant comment les agents utilisent les outils.
- [MCP Explained in 40s. One Plug for Every AI Tool](https://www.youtube.com/watch?v=GF94f67Ph_E) — *AnbuZ HobbieZ*, 13/11 23:20
  > Explication du protocole MCP en 40 secondes, montrant comment il connecte les agents IA à des outils, API et bases de données externes.
- [Compare Claude Code, Codex and Hermes on One Model with Unity Gateway](https://www.youtube.com/watch?v=uaqFF0N9R9E) — *Databricks*, 13/11 21:57
  > Comparaison de Claude Code, Codex et Hermes via Unity Gateway sur Databricks, permettant d'exécuter plusieurs agents de codage sur un même modèle.
- [Guide to the AI Garage Plugin: The Only Plugin Your Agent Needs](https://www.youtube.com/watch?v=259sKoskxBU) — *Tonbi's AI Garage*, 13/11 21:29
  > Guide du plugin AI Garage, qui donne aux agents un accès direct aux contenus et bases de connaissances du créateur.
- [Why AI Coding Agents Are Making Rust More Popular](https://www.youtube.com/watch?v=dhbn05v-7cI) — *Roy Derks*, 13/11 16:00
  > Discussion sur l'impact des agents de codage IA sur la popularité croissante du langage Rust, grâce à leurs capacités de génération de code fiable.
- [AI Engineer Master Course | RAG, GraphRAG, MCP, LangGraph, Deep Agents & Databricks, Neo4j, Langfuse](https://www.youtube.com/watch?v=BXY7mAFN21k) — *Tech With Mala*, 13/11 16:00
  > Cours complet d'ingénierie IA couvrant RAG, GraphRAG, MCP, LangGraph, Deep Agents et l'intégration avec Databricks, Neo4j et Langfuse.
- [Google ADK + MCP: Connect Any Tool to Your AI Agents | CampusX](https://www.youtube.com/watch?v=XDFit6a2Inw) — *CampusX*, 13/11 15:31
  > Tutoriel Google ADK + MCP montrant comment connecter n'importe quel outil à des agents IA via le protocole MCP.

## Podcasts à écouter (10)

- [Reor: OPENSOURCE and 100% LOCAL Obsidian Alternative AI Note-taking app with RAG Support (w/ Llama 3)](https://podcasts.apple.com/us/podcast/reor-opensource-and-100-local-obsidian-alternative-ai/id6826122006?i=1000797739965&uo=4) — *AICodeKing*, 14/11 06:33
  > Présentation de Reor, une application de prise de notes locale et open‑source intégrant le modèle Llama 3 pour le RAG.
- [MinimalChat : STOP PAYING for ChatGPT with this NEW, EASY and LOCAL Alternative!](https://podcasts.apple.com/us/podcast/minimalchat-stop-paying-for-chatgpt-with-this-new-easy/id6826122006?i=1000801873414&uo=4) — *AICodeKing*, 14/11 06:27
  > MinimalChat, une alternative locale à ChatGPT qui permet de ne plus dépendre d’un service payant.
- [The Infrastructure Behind Agents That Run for Months](https://podcasts.apple.com/us/podcast/the-infrastructure-behind-agents-that-run-for-months/id1776879655?i=1000801598222&uo=4) — *Chain of Thought | AI Agents, Infrastructure & Engineering*, 12/11 22:08
  > Tony Holdstock‑Brown explique l’infrastructure derrière les agents qui fonctionnent pendant des mois grâce à Inngest.
- [OpenAI Bought Odessia: A Travel Agency Run by Eight People and AI Agents](https://podcasts.apple.com/us/podcast/openai-bought-odessia-a-travel-agency-run-by-eight/id6810117720?i=1000801581970&uo=4) — *AI Agents & Vibe Coding*, 12/11 22:01
  > OpenAI a acquis Odessia, une agence de voyage gérée par huit personnes et des agents IA.
- [Gemini Decision 1, Qwen4-Max preview — AI News Nov 12](https://podcasts.apple.com/us/podcast/gemini-decision-1-qwen4-max-preview-ai-news-nov-12/id6817748791?i=1000801565557&uo=4) — *AI Engineering Briefing: Daily AI News for Software Engineers*, 12/11 19:38
  > Google dévoile Gemini Decision 1, un modèle décisionnel ultra‑rapide, et Alibaba pré‑visualise Qwen4‑Max.
- [Anthropic says Claude will build your spreadsheet from one sentence. Plus Amazon's shopping agent now takes orders by text, and what AI is doing to freelance budgets](https://podcasts.apple.com/us/podcast/anthropic-says-claude-will-build-your-spreadsheet-from/id6790021778?i=1000801524503&uo=4) — *AI Industry Report*, 12/11 15:11
  > Anthropic montre que Claude peut créer un tableau‑excel complet à partir d’une simple phrase.
- [I Moved 85% of My Work to Grok Bot. Then This Happened.](https://podcasts.apple.com/us/podcast/i-moved-85-of-my-work-to-grok-bot-then-this-happened/id1493486101?i=1000801572673&uo=4) — *Build Income Streams: AI Agents for Small Business, AI Business Ideas & No-Code AI Automation.*, 12/11 20:14
  > L’auteur raconte comment il a déplacé 85 % de son travail de Claude Code vers Grok Bot et les conséquences.
- [Unsupervised Ep 16: One-Word Replies, Decoded](https://podcasts.apple.com/us/podcast/unsupervised-ep-16-one-word-replies-decoded/id6819576349?i=1000801506452&uo=4) — *Unsupervised: Four AI Agents, Zero Script*, 12/11 13:03
  > Un épisode d’Unsupervised où quatre agents IA échangent des réponses d’un mot, illustrant la simplicité des interactions.
- [OpenAI Launches ChatGPT Wallet and More AI News](https://podcasts.apple.com/us/podcast/openai-launches-chatgpt-wallet-and-more-ai-news/id1722322146?i=1000801816966&uo=4) — *The AI Engineer Podcast*, 14/11 00:15
  > L’AI Engineer Podcast couvre le lancement du ChatGPT Wallet d’OpenAI et d’autres actualités IA.
- [Jensen resigns, Nvidia buys Hugging Face — AI News Nov 13](https://podcasts.apple.com/us/podcast/jensen-resigns-nvidia-buys-hugging-face-ai-news-nov-13/id6817748791?i=1000801717265&uo=4) — *AI Engineering Briefing: Daily AI News for Software Engineers*, 13/11 12:38
  > Analyse de la démission de Jensen Huang, l’achat de Hugging Face et les nouvelles capacités de Google Gemini 4 Hydrogen.

## Écartés comme hors sujet (23)

- [NZ Hansard Research with ztab + MCP — Lake Onslow](https://dev.to/cosmkiwi/nz-hansard-research-with-ztab-mcp-lake-onslow-44hh) — *dev.to*, 14/11 07:10
  > Query: How has the debate on lake onslow, and in general dry year battery storage, shifted over the years? Have party positions changed? The parliamentary debate over Lake Onslow and dry-year battery storage between 2020 and 2024 reveals ideological consistency across all major parties , alongside s
- [Jensen Huang’s resignation casts shadow over Trump-Xi AI talks](https://dev.to/the_daily_flare/jensen-huangs-resignation-casts-shadow-over-trump-xi-ai-talks-4m3p) — *dev.to*, 14/11 07:01
  > Originally published on The Daily Flare . Jensen Huang’s resignation as Nvidia chief has cast a shadow over US-China AI safety talks scheduled for November 18-19 in Shenzhen, AFP reported on November 14. US President Donald Trump and Chinese President Xi Jinping are expected to discuss a technology 
- [Nvidia Allegedly Engineered Scarcity by Funding AI Startups to Buy Its GPUs](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus) — *Hacker News*, 14/11 03:52
  > Article URL: https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus Comments URL: https://news.ycombinator.com/item?id=50493251 Points: 269 # Comments: 138
- [datasette-cluster-map 0.19](https://simonwillison.net/2026/Nov/13/datasette-cluster-map/) — *Simon Willison*, 14/11 00:02
  > Release: datasette-cluster-map 0.19 One of the oldest Datasette plugins, and still one of my favorites. It now works with Datasette 1.0a42, and depends on the new datasette-leaflet to ensure OpenStreetMap tiles are requested with a referrer header. Here's a map of power plants owned by California's 
- [datasette-leaflet 0.3](https://simonwillison.net/2026/Nov/13/datasette-leaflet/) — *Simon Willison*, 13/11 23:30
  > Release: datasette-leaflet 0.3 OpenStreetMap have a very reasonable policy that hits to their hosted tile server should send a referrer header . Datasette table pages used the Referrer-Policy: no-referrer HTTP header, causing plugins that loaded tiles from OpenStreetMap to violate that policy. datas
- [AI coding tools are sold on speed, and nobody seems to be selling accountability for the code they ship](https://news.google.com/rss/articles/CBMizAFBVV95cUxPM3ZIOE0xUks5elVUNHFrLXA3LXU0V0N3c09fb1ViQk5FczdTclBOUTloNnBYNVhLT0stbVpITkF3amJJZzBJc09oQW1yRTQ0UTdkY0FrMlpnZjdRWEtRVHg2cmdvajlpRF96MjhSWllEbWlmdzJZb29WNko4UFprX3VYeE9fMF84M3NTemJxWkhaMWgyTjNpVDNWbzgwelhSWVlsRG0ydDN4cnpPbTJsbjlzcjVaSVM2bXZvNlBldXE5Y0JlRmJBVTRlMTc?oc=5) — *The Sociable*, 13/11 21:08
- [Jensen Huang's ouster likely traces back to Nvidia's risky business practices more than his personal life](https://the-decoder.com/jensen-huangs-ouster-likely-traces-back-to-nvidias-risky-business-practices-more-than-his-personal-life/) — *The Decoder*, 13/11 21:07
  > Jensen Huang likely left Nvidia more because of risky business practices than anything else, a Wall Street Journal report suggests. At the very least, those practices made him enemies internally. The company offered cloud providers billions in financial guarantees for chip purchases, including a pla
- [AI Coding’s Real Bottleneck Isn’t Code Review](https://news.google.com/rss/articles/CBMib0FVX3lxTE9fYkZFaHM4cGRFYUdPaXo1TkgwNzMxZHRtQnFDVnNndnlmWkNSUTluSXhQTGl1Zm5ZaHBJcjVqRmVOQzdfZ2FDTzcxLWtpNXRkb3VQNGhIcDBnbkQ0NWNFMUFfa0trZEFfVzBiMHhSVQ?oc=5) — *DevOps.com*, 13/11 20:34
- [OpenAI rebuilt AI shopping from scratch with ChatGPT Wallet](https://the-decoder.com/openai-rebuilt-ai-shopping-from-scratch-with-chatgpt-wallet/) — *The Decoder*, 13/11 19:55
  > OpenAI is taking a second shot at AI-powered shopping with ChatGPT Wallet after scrapping its first approach, Instant Checkout. Users register a card once and confirm each purchase through Face ID or a fingerprint, while actual card details stay hidden behind payment tokens. Rivals such as Anthropic
- [Banks bar Chinese and Hong Kong investors from Anthropic IPO over US export controls](https://the-decoder.com/banks-bar-chinese-and-hong-kong-investors-from-anthropic-ipo-over-us-export-controls/) — *The Decoder*, 13/11 19:01
  > Chinese investors are shut out of Anthropic's IPO, Bloomberg reports. Banks are rejecting buy orders from mainland China and Hong Kong, citing U.S. export control rules known as ITAR. Similar restrictions applied during SpaceX's IPO, and Anthropic's products aren't available in either region anyway.
- [Build a Robot Pick-and-Place Simulation with SimReady Assets](https://huggingface.co/blog/nvidia/simready-assets-robot-pick-and-place) — *Hugging Face*, 13/11 19:00
- [Amodei Puts AI Coding Market at $34 Billion, With Claude Code and Codex Holding 70%](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5BVTRYdnJROXVjSTIzREQ3eTllVVNFTlB6cXRubXk5QzNOXzdKdGVtZEdLcDFlODZkWnZCalRrb0hvbkNhX3BMRFVMSWNkRWhUM2ZETUQ0MW92aFU?oc=5) — *www.tokenpost.com*, 13/11 18:50
- [Anthropic’s Amodei says AI coding market is maturing](https://news.google.com/rss/articles/CBMiekFVX3lxTE05TnI5MFBZM1JDUFIxQ09RYTJOTnBWQmxsV3RGbHZWMHgtN0NnenpDWGhNMFlqT3hEb2NtMXpWWWJ1bTJRTkMzVzhsRXpVQ1hYSmVmWk41MDFNR3piaENlVVZwOGxsLXlmODhmWTBXUHdOd1dESkttaGJR?oc=5) — *Crypto Briefing*, 13/11 18:36
- [Best AI Video Generation Models in 2026: Elo, Price per Second, Open Weights](https://www.marktechpost.com/2026/11/13/best-ai-video-generation-models-2026/) — *MarkTechPost*, 13/11 18:23
  > The AI video leaderboard looks very different from 12 months ago. Native audio is now table stakes. Clips run 15–30 seconds. And an open-weights model sits in the top 3. This ranking (as of Nov 13, 2026) uses one quality signal: blind human-preference Elo from the Artificial Analysis Video Arena. We
- [Cloud reports measure the wrong thing](https://www.infoworld.com/article/4248511/cloud-reports-measure-the-wrong-thing.html) — *InfoWorld*, 13/11 17:21
  > Flexera’s 2026 State of the Cloud Report agrees with many other cloud reports these days: Cloud is more strategic, cloud is more complex, AI makes everything harder, and better governance is the answer. This report, based on a survey of 753 cloud decision-makers and users, argues that enterprise clo
- [AI coding: Humans remain accountable for generated code](https://news.google.com/rss/articles/CBMirgFBVV95cUxObUhCR1RyOTlIY1JQUV9aRnkzUkx3blZXTEEwbmZraU02RjlpM2VHX29MSmhSQi1wZC0tOFliTV9PYmt6dkFfVUs2cjlvYVM5aW93WGZWUERzaFdZOTEwSWs0cEFSbElmTF9YRDZ3SURrekNrY3pXUnJGZjBGUzI4M3VfTU1VVlBTNnUtT01nMFpDVnUtY01CTVVteDRhdjZiT3dsU3R6eU9tMG5CeUE?oc=5) — *TechGig*, 13/11 16:07
- [Introducing ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet) — *OpenAI*, 13/11 16:00
  > Introducing ChatGPT Wallet, a secure way for agents in ChatGPT Work, Codex, and dots to complete purchases with user approval and existing card protections.
- [Netflix Turns Operational Data Into a Knowledge Graph for AI-Driven Observability](https://www.infoq.com/news/2026/11/netflix-ai-driven-observability/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 13/11 13:00
  > Netflix is developing an ontology-driven knowledge graph to accelerate production investigations and provide AI agents with a shared understanding of its operational environment. By Craig Risi
- [[AINews] Jensen Huang resigns after 33 years leading NVIDIA](https://latent.space/p/ainews-jensen-huang-resigns-after-33-years-leading-nvidia/) — *Latent Space*, 13/11 10:04
  > November 12, 2026 — Colette Kress takes over as interim CEO. What happens to open source/American AI leadership?
- [Se former en alternance dès le début 2027](https://www.blogdumoderateur.com/se-former-alternance-debut-2027/) — *Blog du Modérateur*, 13/11 09:10
  > Démarrer en entreprise dès janvier et rejoindre en mars la rentrée d’une majeure consacrée à l’IA et à la data, c’est possible. Vincent Montet, fondateur et directeur du MBADMB de l’EFAP, détaille les atouts de ce calendrier et partage ses conseils aux candidats.
- [Pourquoi toutes les IA ont des mascottes mignonnes ?](https://www.blogdumoderateur.com/pourquoi-ia-mascottes-mignonnes/) — *Blog du Modérateur*, 13/11 07:00
  > Alors que les incidents liés aux agents IA et les modèles à accès restreint nourrissent l’inquiétude, les géants de la tech misent sur des personnages mignons pour rassurer leurs utilisateurs. Analyse.
- [AI Ambition: ArtCraft Cloned Photoshop and Now Wants to "Rebuild Everything"](https://latent.space/p/artcraft/) — *Latent Space*, 13/11 05:17
  > ArtCraft used AI to rewrite Photoshop as open source software. For CEO Brandon Thomas, the vision is even bigger: to take back the internet!
- [Replicate](https://www.producthunt.com/products/replicate-10) — *Product Hunt*, 13/11 03:06
  > Turn Webflow/Framer app into a Claude/Codex project for free Discussion | Link
