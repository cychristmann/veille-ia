# Veille Outils & code 2026-11-15 : Modèles et frameworks émergents

Région : Outils & code · Date : 2026-11-15

Les publications couvrent plusieurs nouveaux modèles (Gemini 4 Carbon, DeepSeek V3, Claude Opus 5.5) et des frameworks (NVIDIA NeMo Switchyard, dspy‑wsp, DuckLake) qui élargissent les capacités de génération de code et de calcul à grande échelle.

- **Cohere Finding Shows Self-Hosted Open-Weight Models Still Need Egress Controls** (InfoQ, note 8/10)
  Cohere recently reported that one of Alibaba’s newest Qwen3.8 models attempted to upload a probe file to a storage container in Beijing while explicitly stating in its reasoning trace that no tools would be triggered. While there is no evidence of intentional backdooring, the report is a reminder th
- **Show HN: DeepSeek V3 in ~200 lines of pure Jax** (Hacker News, note 8/10)
  Article URL: https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax Comments URL: https://news.ycombinator.com/item?id=50497589 Points: 213 # Comments: 12
- **Route coding agent requests to the right model on Amazon Bedrock with NVIDIA NeMo Switchyard** (AWS Machine Learning, note 8/10)
  Coding agents work in tasks, and the number that matters is cost per solved task, not price per token. In this post, you use the AWS CDK to deploy LiteLLM with the NVIDIA NeMo Switchyard routing plugin on Amazon Bedrock, then measure cost per solved task for a routed model group against single-model
- **Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime** (AWS Machine Learning, note 8/10)
  Amazon Bedrock AgentCore runtime V2 snapshots your initialized environment and restores it for each new session, so session start no longer grows with image size. This post explains how V2 starts a session, how to measure session start time, and four patterns to keep work off the first request.
- **Gemini 4 Carbon takes the MathArena crown but costs 15 times more than GPT-6.1 Sol** (The Decoder, note 7/10)
  For the first time in a while, no OpenAI model leads the MathArena AI math benchmark. Google's Gemini 4 Carbon and Anthropic's Fable 5.2 have knocked GPT-6.1 Sol from the top, though both cost significantly more. Gemini ignored the time limit in testing and almost never gave up on a task. The articl
- **DuckLake 1.1 solves the absurd complexity of data lakes at AI scale** (The New Stack, note 7/10)
  How much simpler could a data lakehouse get if an ordinary SQL database kept track of its files? That’s the The post DuckLake 1.1 solves the absurd complexity of data lakes at AI scale appeared first on The New Stack .
- **OpenFold3 on Amazon SageMaker JumpStart: Predict biomolecular structures** (AWS Machine Learning, note 7/10)
  Deploy OpenFold3-preview from Amazon SageMaker JumpStart to predict 3D structures of proteins, DNA, RNA, and ligand complexes in your own AWS account. The post covers asynchronous inference, multi-GPU parallelism, bringing your own MSAs for accuracy and privacy, and scaling to zero to reduce cost.
- **Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy** (MarkTechPost, note 6/10)
  Cmpnd released dspy-wsp, a prototype DSPy optimizer for weight-space programming. A frontier LLM reads a small model’s weights, edits them in a sandbox, and tests each change, with no gradients and about $5 to $10 per run. The post Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy appe
- **Anthropic says outdated prompting habits are slowing down Claude Opus 5.5** (The Decoder, note 5/10)
  Anthropic has made Claude Opus 5.5 the default model on all paid plans and published a guide that does away with old prompting habits. The main takeaway is to drop "think hard" and start at Medium effort. The article Anthropic says outdated prompting habits are slowing down Claude Opus 5.5 appeared
- **Upcoming deprecation of selected GitHub Copilot models in December** (GitHub Changelog, note 5/10)
  We will deprecate the following models across all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions) on December 14, 2026: Model Deprecation date… The post Upcoming deprecation of selected GitHub Copilot models in December appeared first on T
- **Cursor vs GitHub Copilot Market Share: 12 Steps [2026]** (shattered.io, note 4/10)
