# Veille Outils & code 2026-11-17 : Agents IA et cadres de conception

Région : Outils & code · Date : 2026-11-17

Ces articles portent sur les agents intelligents, leurs compétences, les patterns de conception multi‑agents et les implémentations sur des plateformes comme Amazon Bedrock. Ils décrivent aussi des cas d’usage concrets d’agents dans le domaine juridique ou financier.

- **Build memory-aware AI agents with Agentic Retrieve on Amazon Bedrock Managed Knowledge Base** (AWS Machine Learning, note 8/10)
  Amazon Bedrock Managed Knowledge Base and Amazon Bedrock AgentCore memory now store conversations, extract facts, and bring long-term memory into a single AgenticRetrieveStream call. This post shows how to build a memory-aware, multi-user assistant where each user sees only the documents they may re
- **Google’s Gemini 4 Hydrogen Turns Model Choice Into a Routing Decision** (DevOps.com, note 8/10)
  Google is expanding its Gemini 4 family with Hydrogen, a speed-focused model designed for AI coding agents and multi-step workflows. Alongside it, the new Orchestrator capability in Google Antigravity routes tasks between faster execution models and more powerful reasoning models. Google claims the
- **Uber's Secure AI Framework Governs Autonomous AI Agents across Their Lifecycle** (InfoQ, note 8/10)
  In a recent article, Uber Engineering highlights the limitations of traditional identity and API controls in securing AI agents that dynamically reason over external content and take real-world actions. Uber developed a framework to determine whether an agent's action is appropriate given the user's
- **Taxonomy of multi-agent design patterns, anti-patterns, and lessons from manufacturing** (AWS Machine Learning, note 7/10)
  Multi-agent coordination is a distributed systems problem, not a model problem. This post gives a field-tested taxonomy of multi-agent design patterns and anti-patterns, a framework for deciding when multiple agents are warranted, and how to build cost-efficient, reliable systems on AWS.
- **Uber’s Legal AI Agent Cuts Contract Review Time by 20% with Rules and RAG** (InfoQ, note 7/10)
  Uber’s Legal Redlining Agent reviews contract changes in Microsoft Word using RAG, historical lawyer feedback, and deterministic policy rules. Built with LangGraph, OpenSearch, and Redis, the system reports more than 20% lower average contract review time and 91% accuracy in AI-generated decisions.
- **Airbnb Introduces CASTLE for Training Natural Language Search Models with Synthetic Data** (InfoQ, note 7/10)
  Airbnb researchers have introduced CASTLE, a framework designed to address the cold-start problem in natural language search. The approach uses de-identified booking sessions and large language models (LLMs) to jointly generate synthetic search queries and relevance labels, enabling model training b
- **AWS Open-Sources Emulator for Local Testing of 200+ Services by Coding Agents** (InfoQ, note 7/10)
  AWS Emulator is a generally available local HTTPS endpoint, generated from public Smithy API models, that lets developers and coding agents test against more than 200 AWS services without an account, with published fidelity scores and documented limits around IAM, regions, and in-memory state. By Da
- **Getting started with AG-UI — the agent-user interaction protocol** (InfoWorld, note 7/10)
  While AI agents, which can perform long-running work autonomously, have supplanted simple chats for serious work with large (and small) language models, agents have a last-mile problem: How do you display what an agent is doing in front of a user and let the user act on it, without forcing every tea
- **AI agents were all over KubeCon. Production is another story** (The New Stack, note 6/10)
  AI agents are testing systems that were originally built for people, and Jonathan Bryce thinks the cloud-native community has a The post AI agents were all over KubeCon. Production is another story appeared first on The New Stack .
- **How MoEngage built agentic customer engagement on Amazon Bedrock AgentCore** (AWS Machine Learning, note 6/10)
  MoEngage built Merlin AI, a set of AI agents on Amazon Bedrock and Amazon Bedrock AgentCore that let marketing and product teams draft, analyze, and adjust campaigns from a single conversation. Learn how MoEngage turned its existing APIs into MCP tools and kept each tenant's data isolated while givi
- **Hark Releases Handoff², a 2x Faster Computer-Use Agent for Hark Pro** (MarkTechPost, note 6/10)
  Hark has released Handoff², the computer-use agent inside Hark Pro. It averages 2x faster than v1, completes 82% of 478 internal web tasks, and learned to batch actions through latency-penalized RL. The post Hark Releases Handoff², a 2x Faster Computer-Use Agent for Hark Pro appeared first on MarkTe
- **What AI Agent Skills Are and How They Work** (dev.to, note 5/10)
  AI Agent Skills: The Missing Piece of Procedural Knowledge TL;DR AI agents are great at reasoning and recalling facts, but they struggle with step‑by‑step workflows. Skills solve this by packaging procedural knowledge into lightweight, open‑standard Markdown files that agents load on demand. They’re
- **AI agents for business: what they are and how they work** (dev.to, note 5/10)
  "AI agent" has become one of those terms that means everything and nothing. Vendors use it for chat widgets, for Zapier flows with a GPT step in the middle, and for systems that genuinely plan and act on their own. If you are a developer asked to "add an agent" to a business process, it helps to hav
- **Claude Code Is Already an AI Harness. Why Build a Flight Recorder?** (dev.to, note 4/10)
  A coding agent can say it finished a task. That does not tell you whether the last test passed. A log can show that a shell command ran. It cannot, by itself, tell you whether the result is correct. And when a terminal goes quiet, you may be looking at a permission prompt, a long-running tool, or a
- **llm 0.37.3** (Simon Willison, note 4/10)
  Release: llm 0.37.3 A bug fix release for LLM , mainly to cover a problem with the most recent Homebrew package of the software. Homebrew now ships the latest SQLite, 3.54.1 , which includes a fix that broke LLM's logging code . Short version: in SQLite 3.54.0 the following SQL: select json_object('
- **Agents Inherit Your Mess** (DevOps.com, note 4/10)
  AI agents need more than raw logs. Discover how stateless ingestion, asynchronous enrichment and semantic context improve observability, reliability and cost.
- **Instinct, l’agent IA qui valait 10 milliards** (Blog du Modérateur, note 3/10)
  Des prouesses qui font le tour des réseaux, des invitations revendues à prix d'or, une valorisation à 10 milliards de dollars : Instinct, l'agent IA que l'on commande via WhatsApp ou iMessage, est devenu un phénomène en quelques semaines. Pourquoi ?
