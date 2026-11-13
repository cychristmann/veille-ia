# Veille Outils & code 2026-11-12 : Déploiement et infrastructure IA

Région : Outils & code · Date : 2026-11-12

Plusieurs titres portent sur le déploiement de modèles de pointe ou d’agents sur des infrastructures cloud, notamment AWS Trainium, Bedrock AgentCore, les émulateurs locaux d’AWS et les passerelles AI Gateway. Ces ressources visent à simplifier l’accès aux modèles lourds et à accélérer le développement d’applications IA.

- **Deploy frontier AI models on AWS Trainium with SGLang-Neuron** (AWS Machine Learning, note 8/10)
  SGLang-Neuron is now publicly available through an AWS Deep Learning Container. With SGLang-Neuron, you can serve models and generate reinforcement learning rollouts with SGLang on AWS Trainium using the same SGLang interface you already know, all running on native PyTorch.
- **How Natera designed an agentic AI system for lab ops with Amazon Bedrock AgentCore** (AWS Machine Learning, note 7/10)
  Natera built SWARM, an agentic AI system on Amazon Bedrock AgentCore that captures institutional lab-operations knowledge and deploys it at scale. This post walks through the full architecture, from knowledge base construction to deployment and evaluation, delivering about 130x faster first response
- **AWS Releases AWS Emulator: A Local Copy of 200+ AWS Services Built by AI Agents** (MarkTechPost, note 7/10)
  AWS released AWS Emulator, a free, CC0-licensed local emulator of AWS APIs built from 438 API models. Autonomous agents wrote all of its code. It passes 56.6% of 42,857 published fidelity tests at launch. The post AWS Releases AWS Emulator: A Local Copy of 200+ AWS Services Built by AI Agents appear
- **AWS boosts Bedrock AgentCore runtime compute capacity to speed up AI agent development** (InfoWorld, note 6/10)
  AWS on Thursday said that it was upgrading the runtime layer of Amazon Bedrock AgentCore with greater compute capacity, more efficient memory utilization, and faster startup times to help enterprises deploy and scale AI agents more quickly and cost-effectively. The greater compute capacity includes
- **Four Amazon Bedrock inference choices that affect cost** (AWS Machine Learning, note 5/10)
  Your Amazon Bedrock inference bill can keep climbing even after you tune prompts and application logic. Four request-level choices (cache duration, service tier, reasoning effort, and maxTokens) change how many tokens the service processes and the rate applied. We show how we tested each and how to
- **Tokenomics at scale: Track and cap Amazon Bedrock spend per IAM principal with CUR 2.0 and AWS Budgets** (AWS Machine Learning, note 5/10)
  Get per-identity Amazon Bedrock cost visibility and enforceable spend limits using only AWS-native features, with no application code for the common case. Attribute spend with IAM principal tags, report with CUR 2.0 or Cost Explorer, and enforce with AWS Budgets actions that apply a Deny policy when
- **Expo Launches Cloud iOS Simulators and Android Emulators for AI Coding Agents** (PR Newswire, note 5/10)
- **Google’s Gemini Decisions API to handle up to 1,000 questions per request** (InfoWorld, note 5/10)
  Google has announced Gemini Decisions API, offering developers a way to handle routine decisions in AI applications without generating text responses, weeks after OpenAI launched a competing service. Powered by the company’s new Gemini Decision 1 model, the API allows developers to evaluate up to 1,
- **Google Open-Sources TPU Sync for KV Cache and Weight Transfer on TPUs** (InfoQ, note 5/10)
  Google Cloud has open-sourced TPU Sync, a native C++ library that moves KV cache blocks and model weights between TPU HBM, host DRAM, shared storage, and the data center network. By Daniel Dominguez
- **Azure Logic Apps Standard Gets a Local CLI in Preview** (InfoQ, note 4/10)
  Microsoft has released a public preview of the logicapp extension for the Azure CLI, adding local project creation, workflow authoring, a runtime lifecycle, connector management, run inspection, and test scaffolding for Logic Apps Standard, work that previously required the VS Code extension. The pr
