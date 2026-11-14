# Veille Outils & code 2026-11-14 : Plateformes et infrastructures IA

Région : Outils & code · Date : 2026-11-14

Les fournisseurs cloud (AWS, Google, Amazon Bedrock) publient des guides, des architectures et des optimisations pour le déploiement d’agents IA, incluant SageMaker Canvas, Bedrock AgentCore, Gemini 4 Hydrogen et des outils TPU.

- **Production MLOps at GS Caltex with Amazon SageMaker Canvas, part 1** (AWS Machine Learning, note 7/10)
  GS Caltex connects Amazon SageMaker Canvas to Amazon SageMaker Pipelines so process engineers' no-code models run in production. This post shows how ML engineers reuse validated preprocessing flows and models, cutting deployment from about a week to a few hours and running batch inference every 30 m
- **Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime** (AWS Machine Learning, note 7/10)
  Amazon Bedrock AgentCore runtime V2 snapshots your initialized environment and restores it for each new session, so session start no longer grows with image size. This post explains how V2 starts a session, how to measure session start time, and four patterns to keep work off the first request.
- **OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures** (AWS Machine Learning, note 7/10)
  Deploy OpenFold3-preview from Amazon SageMaker JumpStart to predict 3D structures of proteins, DNA, RNA, and ligand complexes in your own AWS account. The post covers asynchronous inference, multi-GPU parallelism, bringing your own MSAs for accuracy and privacy, and scaling to zero to reduce cost.
- **llama.cpp v1.0.0 : A stronger foundation for the local AI ecosystem** (Hugging Face, note 6/10)
- **Google adds multi-model Orchestrator, Gemini 4 Hydrogen, to Antigravity** (InfoWorld, note 6/10)
  Google is adding a new feature, Orchestrator, to Antigravity, its AI-powered development environment, to help enterprises improve software development efficiency by automatically coordinating multiple Gemini models, including the newly introduced Gemini 4 Hydrogen. The new feature, which allows deve
- **Google Releases TPU Sync: Open-Source KV Cache Transfer for TPUs** (MarkTechPost, note 6/10)
  Google released TPU Sync, an open-source C++ library that moves KV caches and weights across TPU HBM, host DRAM, storage and network. Google reports over 90% lower KV transfer latency on 235B to 480B MoE models. The post Google Releases TPU Sync: Open-Source KV Cache Transfer for TPUs appeared first
- **Google Releases Gemini 4 Hydrogen: 2.5x Faster Than Gemini 3.8 Flash** (MarkTechPost, note 6/10)
  Google released Gemini 4 Hydrogen, a fast agentic model with a 1M-token window, 4 thinking levels and $1.50/$7.50 pricing. Google reports a 51 Artificial Analysis score and 57% on Terminal-Bench 4.1. The post Google Releases Gemini 4 Hydrogen: 2.5x Faster Than Gemini 3.8 Flash appeared first on Mark
- **Gemini 4 Hydrogen in GitHub Copilot** (GitHub Changelog, note 5/10)
  Gemini 4 Hydrogen, Google’s latest Flash model, is now generally available in GitHub Copilot. It is designed for fast, efficient agentic coding, tool use, and multistep workflows, with improved instruction… The post Gemini 4 Hydrogen in GitHub Copilot appeared first on The GitHub Blog .
- **Avec Gemini 4 Hydrogen, Google Search s’offre une mise à jour majeure** (Blog du Modérateur, note 4/10)
  Google assure que son moteur de recherche traite mieux les requêtes complexes grâce à Gemini 4 Hydrogen. Le modèle débarque aussi dans l’application Gemini, dans l’API et dans Antigravity.
