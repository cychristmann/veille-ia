# Veille Outils & code 2026-11-22 : Optimisation d'inférence et GPU

Région : Outils & code · Date : 2026-11-22

Les titres portent sur l'accélération de l'inférence grâce aux GPU, la réduction des coûts et de la latence, ainsi que sur des techniques de tuning spécifiques aux modèles Claude et aux grands modèles de Nvidia.

- **AWS Lambda Now Runs GPU Inference with 48 Concurrent Invocations Sharing One Model per GPU** (InfoQ, note 8/10)
  AWS Lambda now runs Event Functions on EC2 G-series GPU instances through Lambda Managed Instances, with up to 48 concurrent invocations sharing one model per GPU, vLLM and SGLang base images that need no handler code, and 90-minute asynchronous timeouts. Billing is the instance price plus a 9.75 pe
- **Nvidia launches desk-side DGX Spark cluster for researchers** (IT Brief Australia, note 8/10)
  Researchers could cut queue times with a four-node desk cluster that lets them test AI and simulation workloads locally before scaling up.
- **Nvidia used 20,000 training examples to fix its AI’s mistakes. Its coding score jumped.** (The New Stack, note 7/10)
  Nvidia used Factory’s Droid coding-agent harness to generate roughly 20,000 rows of post-training data for Nemotron 3 Ultra, the 550-billion-parameter The post Nvidia used 20,000 training examples to fix its AI’s mistakes. Its coding score jumped. appeared first on The New Stack .
- **Meta TLX, a Native GPU Compiler Extension Supporting Advanced Hardware Capabilities** (InfoQ, note 7/10)
  Meta developed Triton Low-Level Extensions (TLX), designed to bridge the gap between high-level GPU programming abstractions and the low-level execution control required to fully exploit modern GPU architectures. By Sergio De Simone
- **Alibaba entrenaba Qwen con chips T-Head, según informes** (NeoTeo, note 7/10)
  Alibaba entrenaba su Qwen insignia de próxima generación con chips T-Head, según informes; Eddie Wu también habló de inferencia y planes de suministro.
- **Inference Optimisation Skill: Claude Code LLM Tuning** (explainx.ai, note 6/10)
- **Cut self-hosted LLM cost and latency with the distributed KV caching agent skill** (AWS Machine Learning, note 6/10)
  Self-hosting LLMs on GPUs means paying to recompute the same context on every turn. Distributed KV caching with Amazon ElastiCache can cut inference cost by up to 40% and time to first token by up to 80%. This post walks through the distributed KV caching skill in the Agent Toolkit for AWS, which ev
