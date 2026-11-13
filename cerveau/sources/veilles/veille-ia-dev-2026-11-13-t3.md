# Veille Outils & code 2026-11-13 : Infrastructure, déploiement et coût

Région : Outils & code · Date : 2026-11-13

Ces articles traitent de l’utilisation d’AWS (Trainium, Bedrock, Budgets), de l’émulation locale de services cloud et des considérations de coût liées aux modèles de frontier AI.

- **How Natera designed an agentic AI system for lab ops with Amazon Bedrock AgentCore** (AWS Machine Learning, note 6/10)
  Natera built SWARM, an agentic AI system on Amazon Bedrock AgentCore that captures institutional lab-operations knowledge and deploys it at scale. This post walks through the full architecture, from knowledge base construction to deployment and evaluation, delivering about 130x faster first response
- **Tokenomics at scale: Track and cap Amazon Bedrock spend per IAM principal with CUR 2.0 and AWS Budgets** (AWS Machine Learning, note 6/10)
  Get per-identity Amazon Bedrock cost visibility and enforceable spend limits using only AWS-native features, with no application code for the common case. Attribute spend with IAM principal tags, report with CUR 2.0 or Cost Explorer, and enforce with AWS Budgets actions that apply a Deny policy when
- **Four Amazon Bedrock inference choices that affect cost** (AWS Machine Learning, note 5/10)
  Your Amazon Bedrock inference bill can keep climbing even after you tune prompts and application logic. Four request-level choices (cache duration, service tier, reasoning effort, and maxTokens) change how many tokens the service processes and the rate applied. We show how we tested each and how to
