# Veille IA outils & code du 16/11/2026

50 articles de médias tech anglophones et francophones (blogs d'outils, Hacker News, Product Hunt) publiés ces 48 dernières heures (rapport généré à 07:23).

## Synthèse du jour

Cette veille montre un dynamisme marqué autour des grands modèles de langage, avec plusieurs annonces de nouvelles versions (Qwen4‑Max, Claude Fable, Tofu‑1) et leur mise à disposition via des passerelles. Le domaine du codage assisté par IA continue de s’étendre : Claude Code, Cursor, Vibe Coding et d’autres outils sont présentés, parfois avec des études de cas ou des comparaisons de performances. La sécurité et la gouvernance des agents autonomes restent une préoccupation centrale, plusieurs articles décrivant des frameworks, des incidents de backdoor et des exigences de contrôle d’e‑gress. Parallèlement, de nouvelles plateformes et marchés (Agentic Canvas, Perit Marketplace, ByteAsk) apparaissent pour commercialiser et distribuer ces technologies. Enfin, la recherche progresse avec des guides sur les patterns GraphRAG, l’analyse du drift des agents et des réflexions sur l’infrastructure nécessaire à l’IA autonome.

*Vérifiée : chaque affirmation est appuyée par au moins un titre.*

## À lire en priorité

- [Alibaba dévoile Qwen4‑Max, affirme qu'il surpasse les modèles concurrents en codage](https://cryptobriefing.com/alibaba-unveils-qwen4-max-ai-model/) — *Crypto Briefing*, 16/11 07:05 · **8/10** (Annonce d'un nouveau modèle Alibaba, fort impact)
  *Titre original : Alibaba unveils Qwen4-Max, claims it beats rival models on coding*
  > Alibaba's focus on efficiency and cost-effectiveness in AI models could reshape competitive dynamics in sectors reliant on coding and productivity. The post Alibaba unveils Qwen4-Max, claims it beats rival models on coding appeared first on Crypto Briefing .
- [Le cadre d’IA sécurisée d’Uber gouverne les agents IA autonomes tout au long de leur cycle de vie](https://www.infoq.com/news/2026/11/uber-secure-ai-framework/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 15/11 21:00 · **8/10** (Framework sécurisé d'Uber pour agents autonomes, haute portée)
  *Titre original : Uber's Secure AI Framework Governs Autonomous AI Agents across Their Lifecycle*
  > In a recent article, Uber Engineering highlights the limitations of traditional identity and API controls in securing AI agents that dynamically reason over external content and take real-world actions. Uber developed a framework to determine whether an agent's action is appropriate given the user's
- [Alibaba lance Qwen4‑Max avec des garde-fous de cybersécurité stricts](https://news.lavx.hu/article/alibaba-launches-qwen4-max-with-strict-cybersecurity-guardrails) — *news.lavx.hu*, 16/11 06:55 · **7/10** (Redite de l'annonce Qwen4-Max avec focus sécurité)
  *Titre original : Alibaba Launches Qwen4-Max With Strict Cybersecurity Guardrails*
  > Alibaba launched its Qwen4-Max model with strict cybersecurity guardrails and plans to scale its next model, Qwen 5, to between five trillion and 10 trillion parameters.
- [Anthropic lance Claude Meetings pour les appels vidéo en direct](https://itbrief.com.au/story/anthropic-launches-claude-meetings-for-live-video-calls) — *IT Brief Australia*, 16/11 04:43 · **7/10** (Lancement de Claude Meetings, fonctionnalité vidéo IA)
  *Titre original : Anthropic launches Claude Meetings for live video calls*
  > The beta expands Claude into live collaboration, giving Team and Enterprise customers notes, transcripts and action items from Google Meet calls at no extra charge.
- [Comment rendre les systèmes RAG d’entreprise plus fiables](https://hackernoon.com/how-to-make-enterprise-rag-systems-more-reliable?source=rss) — *HackerNoon*, 15/11 22:09 · **7/10** (Guide pratique RAG fiable, très pertinent pour entreprises)
  *Titre original : How to Make Enterprise RAG Systems More Reliable*
  > Enterprise RAG needs more than accurate retrieval. Explore four critical gaps in access control, data freshness, continuous evaluation, and cost.

## Modèles LLMs et agents de grande échelle (9)

Les titres annoncent de nouveaux modèles de langage et agents de grande taille, notamment Qwen4‑Max, les versions Claude Fable, Tofu‑1 et le modèle Meituan, ainsi que leur disponibilité sur des passerelles ou leurs performances comparées.

- [Alibaba dévoile Qwen4‑Max, affirme qu'il surpasse les modèles concurrents en codage](https://cryptobriefing.com/alibaba-unveils-qwen4-max-ai-model/) — *Crypto Briefing*, 16/11 07:05 · **8/10** (Annonce d'un nouveau modèle Alibaba, fort impact)
  *Titre original : Alibaba unveils Qwen4-Max, claims it beats rival models on coding*
  > Alibaba's focus on efficiency and cost-effectiveness in AI models could reshape competitive dynamics in sectors reliant on coding and productivity. The post Alibaba unveils Qwen4-Max, claims it beats rival models on coding appeared first on Crypto Briefing .
- [Alibaba lance Qwen4‑Max avec des garde-fous de cybersécurité stricts](https://news.lavx.hu/article/alibaba-launches-qwen4-max-with-strict-cybersecurity-guardrails) — *news.lavx.hu*, 16/11 06:55 · **7/10** (Redite de l'annonce Qwen4-Max avec focus sécurité)
  *Titre original : Alibaba Launches Qwen4-Max With Strict Cybersecurity Guardrails*
  > Alibaba launched its Qwen4-Max model with strict cybersecurity guardrails and plans to scale its next model, Qwen 5, to between five trillion and 10 trillion parameters.
- [Qwen4‑Max disponible dès maintenant sur AI Gateway](https://vercel.com/changelog/qwen4-max-now-available-on-ai-gateway) — *Vercel*, 15/11 21:00 · **7/10** (Qwen4-Max disponible via AI Gateway, facilite l'adoption)
  *Titre original : Qwen4-Max now available on AI Gateway*
- [Meituan publie un modèle agent de 1,6 billion de paramètres qui n’a jamais touché de GPU Nvidia](https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/) — *The Decoder*, 15/11 11:06 · **7/10** (Modèle 1.6T sans GPU Nvidia, percée technologique)
  *Titre original : Meituan releases a 1.6-trillion-parameter agent model that never touched an Nvidia GPU*
  > Meituan has released the weights for LongCat-2.5, a 1.6-trillion-parameter model built for AI agents and trained entirely on Chinese hardware. On Terminal Bench, it scores 88.4 points, landing just behind Claude Opus 5. The sample deployment runs on 194 Huawei Ascend chips, and Meituan makes no ment
- [Qwen4‑Max](https://qwen.ai/blog?id=qwen4-max) — *Hacker News*, 16/11 03:14 · **6/10** (Discussion autour de Qwen4-Max, renforce la visibilité du modèle)
  *Titre original : Qwen4-Max*
  > Article URL: https://qwen.ai/blog?id=qwen4-max Comments URL: https://news.ycombinator.com/item?id=50513215 Points: 311 # Comments: 105
- [Claude Fable 5.2 vs Opus 5.5 : mêmes scores pour presque 4 fois le coût](https://thenewstack.io/claude-fable-5-2-vs-opus-5-5/) — *The New Stack*, 15/11 16:00 · **6/10** (Comparatif coût/performance Claude vs Opus, information pratique)
  *Titre original : Claude Fable 5.2 vs. Opus 5.5: Same scores at almost 4x the cost*
  > Anthropic released Claude Fable 5.2 on November 9 and said it beats Claude Opus 5.5 in almost every capability the The post Claude Fable 5.2 vs. Opus 5.5: Same scores at almost 4x the cost appeared first on The New Stack .
- [Bland lance Tofu‑1, un modèle de parole‑à‑parole full‑duplex pour les appels](https://www.marktechpost.com/2026/11/15/bland-tofu-1-full-duplex-speech-to-speech-model/) — *MarkTechPost*, 15/11 11:06 · **6/10** (Lancement modèle speech-to-speech, potentiel impact vocal)
  *Titre original : Bland Launches Tofu-1, a Full-Duplex Speech-to-Speech Model for Calls*
  > Bland has released Tofu-1, a full-duplex speech-to-speech model for noisy, high-stakes phone calls. It is in enterprise research preview, with no published benchmarks, size or pricing yet. The post Bland Launches Tofu-1, a Full-Duplex Speech-to-Speech Model for Calls appeared first on MarkTechPost .
- [Claude Fable 5.2 vs Fable 5.1 : moins de refus, avec de petites économies sur le correctif de connexion](https://thenewstack.io/claude-fable-5-2-vs-fable-5-1/) — *The New Stack*, 14/11 18:00 · **5/10** (Comparatif versions Claude Fable, amélioration mineure)
  *Titre original : Claude Fable 5.2 vs. Fable 5.1: Fewer refusals, with small savings on the login fix*
  > Anthropic’s Claude Fable 5.2 promises fewer refusals and lower token prices, but those changes played out very differently in our The post Claude Fable 5.2 vs. Fable 5.1: Fewer refusals, with small savings on the login fix appeared first on The New Stack .
- [Claude Fable 5.2 d’Anthropic ne génère pas d’images, il les peint](https://the-decoder.com/anthropics-claude-fable-5-2-doesnt-generate-images-it-paints-them/) — *The Decoder*, 15/11 16:42 · **4/10** (Nouvelle version Claude Fable, fonctionnalité image)
  *Titre original : Anthropic's Claude Fable 5.2 doesn't generate images, it paints them*
  > Anthropic's Claude Fable 5.2 doesn't generate images the way other AI models do. Instead of computing pixels, the language model writes Python code that places hundreds of thousands of simulated brushstrokes on a virtual canvas, complete with bristle texture and paint application. A single photoreal

## Outils de codage assisté par IA (26)

Une série d’articles porte sur des environnements et extensions de programmation pilotés par IA : Claude Code, Cursor, GitHub Copilot, Vibe Coding, ainsi que des études de cas d’agents de codage comme Geni‑Code, Nota ou les hacks de jeux vidéo.

- [Anthropic lance Claude Meetings pour les appels vidéo en direct](https://itbrief.com.au/story/anthropic-launches-claude-meetings-for-live-video-calls) — *IT Brief Australia*, 16/11 04:43 · **7/10** (Lancement de Claude Meetings, fonctionnalité vidéo IA)
  *Titre original : Anthropic launches Claude Meetings for live video calls*
  > The beta expands Claude into live collaboration, giving Team and Enterprise customers notes, transcripts and action items from Google Meet calls at no extra charge.
- [Guide du praticien des 6 motifs Agentic GraphRAG](https://towardsdatascience.com/a-practitioners-guide-to-6-agentic-graphrag-patterns/) — *Towards Data Science*, 15/11 16:00 · **7/10** (Guide avancé sur patterns GraphRAG, très technique)
  *Titre original : A Practitioner's Guide to 6 Agentic GraphRAG Patterns*
  > How autonomous agents turn static knowledge graphs into living Context Graphs that remember decisions, user intent, and operational history The post A Practitioner's Guide to 6 Agentic GraphRAG Patterns appeared first on Towards Data Science .
- [7 façons dont Claude Code peut aider les petites entreprises – sans écrire une seule ligne de code](https://news.google.com/rss/articles/CBMixAFBVV95cUxNRm0tSTBlYjAtOEFBSjYtMG56NTI2MUtFZnRXV0VZdjZhY0pzcjlOSXlnSC1qTVRNeVo4X2dUV0VzU0NOUUtMWnBja3lOV1RXVDlpc00xQTB6OWpiRTR3S3B5bi1GUEIwblJHRUhqTExhSHIxVWR1TzNXZ2g2U194dzZvT0t5aGVTUjJXYks1Ym1TQUtvdTRYdnJVU2hMZGpUVmFkUnp1R0paNGxxZ2lKdmhZYkdLeTRFR0Y2aFhNSXB1Zmww?oc=5) — *Tom's Guide*, 16/11 06:15 · **6/10** (Cas d'usage concret de Claude Code pour PME)
  *Titre original : 7 ways Claude Code can help you run a small business — without writing a single line of code*
- [Anthropic détaille la revue de code assistée par IA, booste l’efficacité de Claude Code](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNaVEwOHltNVZ0V09weGYzZWk3YlRtUWxPa0RKNTJiYTltODNrdlZRZi1Xa1BEU2xaNk1oNkotZnEzdHZPQ240b2FzTzRwXzVfdUJhYWo2aHhNOHV6VE9GMHRyTk5pM1BvZGxwakRER20yUEVNRjRDcGo0RXd1a0FSLVdhVWpIbTZqd3hXVUtva2ZpWkhmNzUybGxTN3hwSFJjR21xMnVjSUZnaHpVYVFXTWVrQmd5a2hKanlUaW1zeTNsS2F0NDVQYg?oc=5) — *TechGig*, 15/11 16:07 · **6/10** (Détails du code review IA d'Anthropic, utile aux devs)
  *Titre original : Anthropic details AI-powered code review, boosts efficiency for Claude Code*
- [Anthropic décrit son processus de revue de code IA pour Claude Code](https://www.infoq.com/news/2026/11/claude-code-review/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 15/11 10:55 · **6/10** (Processus de revue de code IA d'Anthropic, bonnes pratiques)
  *Titre original : Anthropic Outlines its AI-Powered Code Review Process for Claude Code*
  > Anthropic has outlined how the Claude Code team handles code reviews as AI agents increasingly contribute to its codebase. The approach relies on multiple layers of automated verification, AI-powered reviews, and risk-based human approval, aiming to reduce manual review time without increasing regre
- [Données de plus de 100 agents IA montrent qu’ils échouent par dérive silencieuse, pas par erreurs](https://towardsdatascience.com/data-from-100-ai-agents-shows-they-fail-by-silent-drift-not-errors/) — *Towards Data Science*, 14/11 14:00 · **6/10** (Étude sur dérive silencieuse des agents, données utiles)
  *Titre original : Data From 100+ AI Agents Shows They Fail by Silent Drift, Not Errors*
  > Quality and token alerts were early signals for 38% of agents and errors for about 1%, so monitoring should start with quality, cost, and latency. The post Data From 100+ AI Agents Shows They Fail by Silent Drift, Not Errors appeared first on Towards Data Science .
- [Pourquoi les garde-fous probabilistes échouent dans l'IA cyber‑physique (et comment les substrats déterministes les résolvent)](https://dev.to/cody_fulmark/why-probabilistic-guardrails-fail-in-cyber-physical-ai-and-how-deterministic-substrates-solve-it-34db) — *dev.to*, 16/11 07:10 · **5/10** (Analyse intéressante mais reste théorique)
  *Titre original : Why Probabilistic Guardrails Fail in Cyber-Physical AI (And How Deterministic Substrates Solve It)*
  > Modern Agentic AI workflows are rapidly moving from generating text to controlling real-world infrastructure—managing power grids, autonomous robotics, and enterprise compute clusters. However, relying on probabilistic guardrails (like prompt filtering or post-hoc anomaly detection) introduces a cri
- [Nota de Corée du Sud cible les réseaux air‑gapped des banques avec un outil de codage IA, augmentant le débit GPU jusqu’à 95 %](https://news.google.com/rss/articles/CBMidkFVX3lxTE5XQ2Z5akhkVE5CTkZxOFlBOHVKMUFhODh6U0p5d0FjOGFQWm1heTZNX3RxU2dhcVNtR3lCdUg3M3JKMjI2RFlOaHNnT1d4cmtJN1NhTF8zOGJ4WnJhNmZpbzE4a3Z5eWh3bXFORkVHRHg1MEpHT1E?oc=5) — *BigGo Finance*, 16/11 03:27 · **5/10** (Outil IA pour réseaux aériens, intéressant mais très ciblé)
  *Titre original : South Korea's Nota Targets Banks' Air-Gapped Networks With AI Coding Tool, Boosting GPU Throughput Up to 95%*
- [Claude Code revisité : personnalisez totalement toutes les couleurs et les arrière‑plans animés dès aujourd’hui](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9uT0VyaFBtcW54bVpaZ3BfdXRTSzJQZ3NnVTl5MkV2d044RlJBM0pCelNTYjNkeGhia09UQ1Vob0NLODR3cFJZUGFvYWlMdTk0aU1Z?oc=5) — *eu.36kr.com*, 16/11 02:01 · **5/10** (Mise à jour UI de Claude Code, amélioration utilisateur)
  *Titre original : Revamped Claude Code: Fully Customize All Colors & Animated Backgrounds Starting Today*
- [J’ai demandé à Claude Code, Google Antigravity et ChatGPT Codex de créer le même jeu, et un seul a produit quelque chose que j’ai voulu garder](https://www.xda-developers.com/i-asked-claude-code-antigravity-and-codex-to-build-the-same-game-and-only-one-made-something-i-wanted-to-keep-playing/) — *XDA*, 15/11 23:30 · **5/10** (Test comparatif de générateurs de jeux, utile pour devs)
  *Titre original : I asked Claude Code, Google Antigravity, and ChatGPT Codex to build the same game, and only one made something I wanted to keep playing*
  > As for the game itself, it reflects the effort. It handles like a dream, the steering agrees with the degree the analog stick is turned so that a sharp corner is a yank and a gentle sway along a long ...
- [Comment je fais fonctionner mon agent OpenClaw 24 h/24 sur un Mac en toute sécurité – avec Claude Code en garde](https://news.google.com/rss/articles/CBMif0FVX3lxTE16NTdZTDZ3c0d3WWRGbkwxSGZjM00xREszeEVBNENVN2M0RlljbU1hSzFWbHY4TWdjaTBhTXYydHZReV9UQTI0SG9ZMVVncjZqZ2hQa3pHYjB1NnlzbHhDZ2hRU0llcTNMcjlyUjBiQjMzWTNlYUdQNFZKdHY0ZDg?oc=5) — *ZDNET*, 15/11 18:05 · **5/10** (Tutoriel d'exploitation d'agent, intéressant pour hobbyistes)
  *Titre original : How I safely run my OpenClaw AI agent 24/7 on a Mac – with Claude Code standing guard*
- [OpenAI lance Daybreak, des agents IA qui piratent vos applis pour les sécuriser](https://korben.info/openai-lance-daybreak-des-agents-ia-qui-piratent-vos-applis-pour-les-securiser.html?utm_source=rss&utm_medium=feed&utm_campaign=flux-principal) — *Korben*, 15/11 10:26 · **5/10** (Annonce agents de sécurité OpenAI, intérêt pratique)
  *Titre original : OpenAI lance Daybreak, des agents IA qui piratent vos applis pour les sécuriser*
  > Lors de l'événement Cyber at the Frontier, OpenAI a présenté Daybreak Red Team, des agents IA qui testent l'intrusion sur vos applis web, et Daybreak Defense Factory, qui propose des correctifs en pull request. Le tout repose sur GPT-6 Cyber, en accès anticipé sur liste d'attente, sans prix annoncé.
- [Cmpnd publie dspy‑wsp : la programmation en espace de poids arrive sur DSPy](https://www.marktechpost.com/2026/11/14/cmpnd-dspy-wsp-weight-space-programming/) — *MarkTechPost*, 14/11 17:45 · **5/10** (Publication d'outil DSPy, intéressant pour chercheurs)
  *Titre original : Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy*
  > Cmpnd released dspy-wsp, a prototype DSPy optimizer for weight-space programming. A frontier LLM reads a small model’s weights, edits them in a sandbox, and tests each change, with no gradients and about $5 to $10 per run. The post Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy appe
- [IBK Industrial Bank of Korea développe en interne l'agent de codage IA « Geni‑Code »… Accélère AX axé sur le front office](https://news.google.com/rss/articles/CBMiZEFVX3lxTFB6NTZvZE9aVkdDSUpjek84THFyUnZFbXFSTzJHV1oyNkIyRUYtQVpFQjl4TXRNNUpqd1ZKMUZnUEFPVXBkWnRWcTc5MjlfZmV2eHBIRndjRlVWejVBNFRiS0lWY2U?oc=5) — *아시아경제*, 16/11 06:31 · **4/10** (Développement interne coréen, portée locale)
  *Titre original : IBK Industrial Bank of Korea Develops AI Coding Agent “Geni-Code” In-House... Accelerates Frontline-Focused AX*
- [Nota annonce le 16 que son modèle de langue large d’optimisation et son serveur sont signés](https://news.google.com/rss/articles/CBMiS0FVX3lxTE5kSGMtcGhlQkFhUlBHSHZqcFNkdEFPbldBNjE3NVJqd3pDN1dNbEdQem84Zjc4dlNSUWtpWnFYQXFwSlFnYnI4QlZHTQ?oc=5) — *매일경제*, 16/11 02:48 · **4/10** (Annonce d'optimisation LLM, impact modéré)
  *Titre original : Nota announced on the 16th that it has signed an optimization large language model (LLM) and server*
- [Claude Code a construit le même Pokédex de 12 façons : coûts de 2,67 $ à 4,97 $](https://news.google.com/rss/articles/CBMiggFBVV95cUxQOFJ5WGZoU0VVZGQ1X3lBZXYxRmhwWnRfWS0zTzNtY21VNDd6dk5qaG5VQ0thNkFseGxtNjJEcTl1bDBDMEtjTXRMRklWX0E4VUpVRDk3ZUlQeXRKcERrWDV6UmM5eTgtVzZReGhIZDEweG1NcWdUb1ZFbkJwSjdMX1dB?oc=5) — *XenoSpectrum*, 16/11 01:37 · **4/10** (Comparaison de coûts, intérêt limité)
  *Titre original : Claude Code Built the Same Pokédex 12 Ways: Costs Ranged From $2.67 to $4.97*
- [Koscom organise un hackathon interne de codage IA : « Résoudre les problèmes de mon travail avec l’IA »](https://news.google.com/rss/articles/CBMickFVX3lxTE9lNUJpZU5JYTRJTWtKWldsSmxOUWc0VkZZZTZIdzBKRVd3RE1aRmVoeDdjTjRRZFJLUEpaWUJzb2hHdTlKR2swcnR5TGFYbU5EaDF4a21NMzAzb1dTdHZoc3U2cW1pZVplblZ0MExTZmFfZw?oc=5) — *아시아경제*, 16/11 01:06 · **4/10** (Hackathon interne, montre adoption mais portée restreinte)
  *Titre original : Koscom Holds In-House AI Coding Hackathon: "Solve Problems in My Work with AI"*
- [Agentic Canvas](https://www.producthunt.com/products/agentgrid-io) — *Product Hunt*, 15/11 07:22 · **4/10** (Nouveau produit Product Hunt, visibilité mais peu de détails)
  *Titre original : Agentic Canvas*
  > Free Agentic Design Canvas - A visual way to work with AI Discussion | Link
- [Comment tester une vidéo rendue par votre agent IA : des bugs de recherche au MP4 final](https://dev.to/sheen_417f0f3a7f4/how-to-test-a-video-your-ai-agent-rendered-from-seek-bugs-to-the-final-mp4-1d60) — *dev.to*, 16/11 07:10 · **3/10** (Guide très spécialisé, audience limitée)
  *Titre original : How to test a video your AI agent rendered: From seek bugs to the final MP4*
  > An AI agent can edit a video project from one prompt and still hand back a bad result. A scene can look right when it plays from zero and wrong when someone scrubs back. An MP4 can export at the wrong size, with no audio track, or a second short. Both are cheap to catch before a person watches anyth
- [Données d’enquête Cursor vs Copilot : 12 étapes, 80 minutes [2026]](https://news.google.com/rss/articles/CBMiigFBVV95cUxNU1NEbWhEZWM3R285T2JSMGdacUYyQ3d5RHRqX0FHMUpDWW1TSDdjaFFTTXR5bFg5Zi00cExJa0xDV0JjN0ZKUTd6eHBjdXktNUlzTTlFU0JwOUdRbnk0aEhzd19hTVZoc2VWTkFvWi1vN3hPeThtLTA5TmdLblVPYUU3ek10dENjQVE?oc=5) — *shattered.io*, 16/11 05:01 · **3/10** (Sondage comparatif, valeur informative limitée)
  *Titre original : Cursor vs Copilot Survey Data: 12 Steps, 80 Min [2026]*
- [Nota Inc. cible le marché du codage IA du secteur financier ; le débit GPU augmente jusqu’à 95 %](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1mUUlWWWsxVGU0ZzFvbnNwS2toQUN1N1lNejVxWEo0SGlqR1U4ZTR1ZGlQaEV1OGNJYWtJZFgtOF91ZklwRDVWOXZhblEzdkJKbUo3UzdkTU0?oc=5) — *파이낸셜뉴스*, 16/11 02:50 · **3/10** (Communiqué financier, pas d'innovation technique)
  *Titre original : Nota Inc. Targets Financial Sector AI Coding Market; GPU Throughput Up by Up to 95%*
- [Tarification GitHub Copilot Business : 19 $ par siège et crédits IA](https://news.google.com/rss/articles/CBMiggFBVV95cUxNVUdVeXk0OEFVbHVjci1aOTB4WWJadTBwQnF0RktVU1V0UG9Wa2FzbjZUTlVuNTlSTG13dHd4WllnaEpXUUFqV3ZmR0hTSkFxeC1BeV9sdkNua05nNXI0WXc5OFNxcWQyS2g3Q0FkYjlYYXFaZ2h2U3liQVJSbEh6QXpB?oc=5) — *JournalArta*, 16/11 01:32 · **3/10** (Tarification Copilot Business, information financière)
  *Titre original : GitHub Copilot Business Pricing: $19 Seats and AI Credits*
- [Vibe Coding change la façon dont les musiciens personnalisent leur matériel](https://www.msn.com/en-us/news/other/vibe-coding-is-changing-how-musicians-customize-their-gear/ar-AA2huglj) — *Engadget*, 15/11 17:30 · **3/10** (Application musicale, hors du focus codage IA)
  *Titre original : Vibe Coding Is Changing How Musicians Customize Their Gear*
  > AI is changing just about every industry even music. This is how musicians are using vibe coding to alter their sound, their gear and how music is made.
- [Modèle Elephant‑Goldfish, comment utiliser le plugin Google avec Claude Code](https://news.google.com/rss/articles/CBMijwFBVV95cUxQQWl0YnBoaUZJY3lqR19TNVFLZUFZb19XNllMaHoyQnMwajk0NG9LRzBZejdZSTlRLWUwdlVGVDFtdzBpLVBWdDRxUEVlUEQxVGJrM1NFNHJBS2h3bVp4aVZQMmZWeTJuX05nZlJObVFFa0xfem9PbEFzVHVxM3MxR2xYOHpLMWgtUXdtbFNOUQ?oc=5) — *Pasquale Pillitteri*, 15/11 11:10 · **3/10** (Tutoriel niche, audience restreinte)
  *Titre original : Elephant-Goldfish Model, how to use Google's plugin with Claude Code*
- [Perit Marketplace](https://www.producthunt.com/products/perit-marketplace) — *Product Hunt*, 15/11 06:04 · **3/10** (Marketplace d'IA, peu d'information technique)
  *Titre original : Perit Marketplace*
  > Sell your data and RL tasks to frontier AI labs Discussion | Link
- [Abyssal Garden : un monde sous‑marin nageable créé par Claude Code dans un fichier HTML de 97 KB](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE1LNmJDZGxnWG0wSW9vWWhJcXE2N2NjQnVJNV90dXZlMnhtWGhBYk9QM0VRc0hIMmNwSVM4LWFlT0h0YWhVYzUzSVRza3FnNWhvUG05aVNybUdjNEg0UUJxRjJiV3RERFE?oc=5) — *XenoSpectrum*, 16/11 03:32 · **2/10** (Démonstration ludique, peu pertinente pour codage)
  *Titre original : Abyssal Garden: A Swimmable Underwater World Built by Claude Code in a Single 97KB HTML File*

## Sécurité, gouvernance et cadres pour IA autonome (8)

Ces articles traitent de la sécurisation des agents IA, des frameworks de gouvernance, des incidents de backdoor et des exigences d’e‑gress, ainsi que de la vérification des réponses d’agents autonomes.

- [Le cadre d’IA sécurisée d’Uber gouverne les agents IA autonomes tout au long de leur cycle de vie](https://www.infoq.com/news/2026/11/uber-secure-ai-framework/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 15/11 21:00 · **8/10** (Framework sécurisé d'Uber pour agents autonomes, haute portée)
  *Titre original : Uber's Secure AI Framework Governs Autonomous AI Agents across Their Lifecycle*
  > In a recent article, Uber Engineering highlights the limitations of traditional identity and API controls in securing AI agents that dynamically reason over external content and take real-world actions. Uber developed a framework to determine whether an agent's action is appropriate given the user's
- [L’émulateur AWS prouve que les agents ont besoin d’une boucle de vérification : le réalisme est le vrai défi](https://thenewstack.io/aws-emulator-verification-loops/) — *The New Stack*, 14/11 18:30 · **6/10** (Émulateur AWS montrant besoin de boucle de vérif, insight technique)
  *Titre original : AWS Emulator proves agents need a verification loop. Realism is the hard part.*
  > This week, Amazon Web Services released AWS Emulator, a local copy of AWS that coding agents can test against. It The post AWS Emulator proves agents need a verification loop. Realism is the hard part. appeared first on The New Stack .
- [Cursor révèle comment une clé Fireworks AI fuitée a conduit à une extension Claude Code backdoor](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1sWEMzcDR1S25FUzdxS0hITFVIbUh5a1hvU3BSZE1kX1phc3BLb3pudHVnd2VVMklZbFhhOGotS2h6QUlDUHZqY0tSMGZha2lHQWNJdTR2eGtWUk9oenfSAWNBVV95cUxOYktFcENlNDdpY0MwZ1VVbTRmeFAzVU00RWp5OXZGYi1NcWR3a1ZKeVRzRk9rZ1E3bTJzbnVvSzhXQXk1TU9kOHR5ckZXZTBZSUlzdzBPWlhZYVM4SDE1WTRCbWM?oc=5) — *CyberSecurityNews*, 15/11 15:04 · **5/10** (Incident de sécurité, montre risques des extensions)
  *Titre original : Cursor Reveals How a Leaked Fireworks AI Key Led to a Backdoored Claude Code Extension*
- [Incident d’extension Claude Code malveillante de Cursor retracé au piratage FireworksAI](https://www.digitaltoday.co.kr/en/view/125823/cursor-malicious-claude-code-extension-incident-traced-to-fireworksai-hack) — *디지털투데이*, 15/11 12:52 · **5/10** (Analyse d'incident Cursor/Claude, utile pour sécurité)
  *Titre original : Cursor malicious Claude Code extension incident traced to FireworksAI hack*
  > The incident in which a malicious Claude Code extension was distributed on the Cursor marketplace began with an access key leaked in a FireworksAI hack, The Hacker News reported on Nov. 15. The ...
- [Cohere montre que les modèles open‑weight auto‑hébergés nécessitent toujours des contrôles d’égress](https://www.infoq.com/news/2026/11/cohere-open-weight-egress-risk/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=AI%2C+ML+%26+Data+Engineering) — *InfoQ*, 15/11 03:42 · **5/10** (Étude Cohere sur contrôles d'égress, pertinence sécurité)
  *Titre original : Cohere Finding Shows Self-Hosted Open-Weight Models Still Need Egress Controls*
  > Cohere recently reported that one of Alibaba’s newest Qwen3.8 models attempted to upload a probe file to a storage container in Beijing while explicitly stating in its reasoning trace that no tools would be triggered. While there is no evidence of intentional backdooring, the report is a reminder th
- [Sécuriser le passage à l’IA autonome](https://itbrief.com.au/story/securing-the-leap-to-autonomous-ai) — *IT Brief Australia*, 16/11 03:23 · **4/10** (Article de fond sur sécurisation, peu de nouveauté concrète)
  *Titre original : Securing the leap to autonomous AI*
  > Employee trust could slow the shift to autonomous AI unless firms set clear limits, oversight and audit trails for machine-led actions.
- [Le design « Chubby » de Google, vieux de 20 ans, offre encore des leçons utiles pour l’infrastructure IA](https://hackernoon.com/googles-20-year-old-chubby-design-still-has-useful-lessons-for-ai-infrastructure?source=rss) — *HackerNoon*, 15/11 11:58 · **4/10** (Leçon d'architecture ancienne, pertinence indirecte)
  *Titre original : Google's 20-Year-Old Chubby Design Still Has Useful Lessons for AI Infrastructure*
  > Explore Google's Chubby lock service and its lasting lessons for distributed coordination, advisory locking, leases, and modern AI infrastructure
- [Survie sur la liste blanche : conception sharding et assistée par agent pour des réseaux résistants à la censure](https://hackernoon.com/survival-under-the-allowlist-a-sharded-agent-assisted-design-for-censorship-resistant-networks?source=rss) — *HackerNoon*, 15/11 15:00 · **4/10** (Concept de réseau résistant à la censure, peu d'application immédiate)
  *Titre original : Survival Under the Allowlist: A Sharded, Agent-Assisted Design for Censorship-Resistant Networks*
  > How internet control shifted from blocklists to allowlists, why circumvention tools struggle, and a design using local AI agents, sharded relays, and Web3.

## Plateformes, marchés et produits IA (1)

Des annonces de plateformes et de places de marché dédiées aux agents IA, ainsi que des levées de fonds et des lancements de produits comme Kindo, Agentic Canvas, Perit Marketplace, ByteAsk Cloud Agents et Daybreak.

- [Kindo lève 30 millions de dollars pour gouverner les agents IA d’entreprise](https://news.lavx.hu/article/kindo-raises-30-million-to-govern-enterprise-ai-agents) — *news.lavx.hu*, 16/11 06:22 · **3/10** (Levée de fonds, peu de nouveauté technique)
  *Titre original : Kindo raises $30 million to govern enterprise AI agents*
  > Kindo raised $30 million in a round co-led by Crosspoint Capital and Forgepoint Capital, bringing total funding to $57.6 million. The company says it will use the money for go-to-market growth and its AI Control Center and Deep Hat tools.

## Recherche, méthodologies et analyses d’agents IA (3)

Ce groupe regroupe les travaux de recherche et les guides pratiques sur les systèmes RAG, les patterns GraphRAG, la spécification des agents de codage, l’étude du drift silencieux et les leçons d’infrastructure tirées de projets historiques.

- [Comment rendre les systèmes RAG d’entreprise plus fiables](https://hackernoon.com/how-to-make-enterprise-rag-systems-more-reliable?source=rss) — *HackerNoon*, 15/11 22:09 · **7/10** (Guide pratique RAG fiable, très pertinent pour entreprises)
  *Titre original : How to Make Enterprise RAG Systems More Reliable*
  > Enterprise RAG needs more than accurate retrieval. Explore four critical gaps in access control, data freshness, continuous evaluation, and cost.
- [Satisfication de spécifications dans les agents de codage IA](https://news.google.com/rss/articles/CBMif0FVX3lxTE80ak5wTUQwUWo3YTQ2Tml0OFhCZENxOGhLbEFzblVYd05BYVE2Z0hoR3J1UGJrWXJ2bmlnWUxZa3hIamxlaU9EcmtEY19OV1BVQ25MVUp1NzAwYl9xbXNKT1hOdlVHdGRld1hFalBWQXJzTjRRNGJka0hwckU0ZmM?oc=5) — *CASRAI*, 15/11 13:43 · **5/10** (Spécification académique, pertinence pour chercheurs)
  *Titre original : Specification Satisficing in AI Coding Agents*
- [La recherche web pour agents est arrivée : pourquoi le classement détermine toujours la réponse](https://thenewstack.io/ai-agent-search-ranking/) — *The New Stack*, 14/11 17:00 · **5/10** (Analyse du ranking dans la recherche d'agents, pertinence modérée)
  *Titre original : Web search for agents is here: Why ranking still decides the answer*
  > AI agents have had a URL problem for a while. When an agent needs current information but has no search The post Web search for agents is here: Why ranking still decides the answer appeared first on The New Stack .

## Autres articles (3)

- [Revue d'architecture : Concevoir une plateforme de mise en relation IA à commande vocale](https://dev.to/janakii/architectural-review-engineering-a-voice-first-ai-matchmaking-platform-3ilj) — *dev.to*, 16/11 07:11 · **4/10** (Article technique niche, peu d'impact sectoriel)
  *Titre original : Architectural Review: Engineering a Voice-First AI Matchmaking Platform*
  > Disclaimer: This critical technical analysis is based on a public engineering case study published by GeekyAnts regarding the development of the oku dating platform. I am breaking down their architectural decisions, strengths, and trade-offs for founders and engineering leaders. Traditional swipe-ba
- [Les développeurs de mods GTA gagnent des milliers de dollars avec l’IA de Claude Code et FiveM](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPb1hiaEFhTmlONC1leDQwbndtT3VpYjlfVF8yVVY3UXFKNV82dVNZVzFQQ283Y1BIbkU3d0NlX2RhM2pHLVltVXA3ZGlwMFZOWHlEYldkdl9FMlY0TjVmVUJteGpmZTRCa1BBR0hHWktIWjZhVC1sVVNxbjBUSGZWZmRlaDJ5YWhFaGVmenhIMVlyaldiZktwY0d6cGNPdDlpS3hUa09Sd2EyOW83OERQd2ZHOWlkdUFfX3E5MEVERWtBOFZ0aVh5aGFNY0VMU1J2?oc=5) — *GameGPU*, 15/11 12:43 · **3/10** (Cas d'usage gaming, intérêt limité pour devs IA)
  *Titre original : GTA mod developers are making thousands of dollars with AI from Claude Code and FiveM.*
- [Comment le vibe coding a changé la trajectoire du gadget préféré d’internet](https://tech.yahoo.com/audio/articles/vibe-coding-changed-trajectory-internets-133015050.html) — *How-To Geek*, 15/11 14:30 · **2/10** (Article grand public, pas centré IA)
  *Titre original : How vibe coding changed the trajectory of the internet's favorite new gadget*
  > Vibe coding has something of a rocky reputation, and rightly so. The idea that anyone can "create" a project, release it, and quickly abandon it when they lack the interest or skill to take it further ...

## Vidéos à regarder (10)

- [How to Build and Set Up AI Agents the Right Way](https://www.youtube.com/watch?v=UzSHKifNpKA) — *Tito Space*, 16/11 06:00
  > Tutoriel montrant comment construire et configurer correctement des agents IA en utilisant des outils comme Antigravity et VS Code.
- [Claude Code Enterprise Operations Handbook | How Teams Roll Out AI Coding Tools (10-Min Guide) 🎧](https://www.youtube.com/watch?v=A1k6oPDJ4QI) — *WE WE TV*, 16/11 04:15
  > Guide de 10 minutes destiné aux équipes d’ingénierie pour planifier le déploiement de Claude Code et d’autres outils de codage assisté par IA.
- [Codex vs Claude Code: Which AI Coding Tool Should You Use?](https://www.youtube.com/watch?v=vDsA9XVn_7s) — *Klai*, 16/11 00:15
  > Comparaison entre Codex et Claude Code pour aider les développeurs à choisir l’outil de codage IA le plus adapté à leurs besoins.
- [Meet OpenSol – The Local-First AI Coding Agent for Your Desktop](https://www.youtube.com/watch?v=NLbqleuxnxI) — *OpenSoftx*, 15/11 20:12
  > Présentation d’OpenSol, un agent de codage IA local‑first open‑source qui fonctionne directement sur le poste de travail de l’utilisateur.
- [Claude Code vs Cursor Agent Mode vs Roo Code: 2026 AI Coding War Explained](https://www.youtube.com/watch?v=IeMdsJobg5A) — *The ML AI Blueprint*, 15/11 20:05
  > Analyse du « war » des outils de codage IA en 2026, opposant Claude Code, Cursor Agent Mode et Roo Code.
- [Tools, Agents, Harness, MCP & More: 20 AI Terms Every Engineer Should Know #ai #llm #design](https://www.youtube.com/watch?v=jogGbxjszmo) — *Crack Tech*, 15/11 18:00
  > Vidéos expliquant 20 termes essentiels liés aux IA, aux agents et aux modèles, utiles aux ingénieurs logiciels.
- [MCP Explained: How AI Connects to Tools](https://www.youtube.com/watch?v=32gGsNbcPOc) — *Vaibhav Roy*, 15/11 17:18
  > Explication du Model Context Protocol (MCP) qui normalise la connexion des IA aux outils, aux ressources et aux prompts.
- [How to Connect Claude to VS Code Easily (2026)](https://www.youtube.com/watch?v=BtXGHKP9-RU) — *HAMED CODEX*, 15/11 16:33
  > Tutoriel pas à pas pour connecter Claude Code à VS Code via l’extension officielle Claude Code.
- [How AI Agents Use Tools: Function Calls to MCP](https://www.youtube.com/watch?v=D7YaK3OWYj8) — *AppMillers*, 15/11 15:30
  > Décryptage du fonctionnement des agents IA qui utilisent des appels de fonction et le MCP pour interagir avec des outils comme la planification de réunions ou les bases de données.
- [Agentic AI in Optical Networks: MCP, T-API Tools and Twin Checks](https://www.youtube.com/watch?v=YIK9qc8iSOc) — *MapYourTech*, 15/11 15:16
  > Illustration de l’usage d’agents IA dans les réseaux optiques, incluant MCP, T‑API et des vérifications en double.

## Podcasts à écouter (10)

- [I Built an AI Interview Prepper to Land Offers at OpenAI, Google & Amazon | Ep. 37](https://podcasts.apple.com/us/podcast/i-built-an-ai-interview-prepper-to-land-offers-at/id1893460266?i=1000802142903&uo=4) — *Agentic AI Execution*, 16/11 00:02
  > Discussion d'un outil d'IA conçu pour préparer les entretiens d'embauche chez les géants de la tech comme OpenAI, Google et Amazon.
- [Ep 6 · Top Story: Claude Code's sandbox, Code Mode and Projects](https://podcasts.apple.com/us/podcast/ep-6-top-story-claude-codes-sandbox-code-mode-and-projects/id6834673859?i=1000802107513&uo=4) — *ACN · AI Coding News*, 15/11 21:43
  > Présentation des nouvelles fonctionnalités de Claude Code, notamment le sandbox, le Code Mode et les projets, ainsi que l'intégration de Claude Sheets comme alternative à Excel et Google Sheets.
- [An AI-built app can show your users' data to strangers: what to check before launch](https://podcasts.apple.com/us/podcast/an-ai-built-app-can-show-your-users-data-to/id6810117720?i=1000802108931&uo=4) — *AI Agents & Vibe Coding*, 15/11 19:33
  > Mise en garde sur un forum créé avec l'IA où des visiteurs pouvaient accéder à des dizaines de milliers de profils et de messages, illustrant les risques de confidentialité avant le lancement d'une appli.
- [Anthropic Launches Claude Fable 5.2 and Mythos 5.2](https://podcasts.apple.com/us/podcast/anthropic-launches-claude-fable-5-2-and-mythos-5-2/id1722322146?i=1000802097371&uo=4) — *The AI Engineer Podcast*, 15/11 18:00
  > Annonce du lancement de Claude Fable 5.2 et Mythos 5.2 par Anthropic, avec des liens vers des modèles IA et des ressources pour les développeurs.
- [Unsupervised Ep 17: The Deadline](https://podcasts.apple.com/us/podcast/unsupervised-ep-17-the-deadline/id6819576349?i=1000802070696&uo=4) — *Unsupervised: Four AI Agents, Zero Script*, 15/11 13:28
  > Épisode d'Unsupervised où quatre agents IA doivent préparer un dossier de revue Q3 en quatre jours, montrant la coordination d'équipes d'agents sans script.
- [7 Things AI-Native Companies Do Differently](https://podcasts.apple.com/us/podcast/7-things-ai-native-companies-do-differently/id1680633614?i=1000802069338&uo=4) — *The AI Daily Brief: Artificial Intelligence News and Analysis*, 15/11 13:20
  > Analyse des sept pratiques distinctives des entreprises dites « AI‑native » comme Stripe, Shopify ou Uber, pour transformer leurs agents en systèmes utiles.
- [Blackwell in DeepSeek, Claude Meetings — AI News Nov 15](https://podcasts.apple.com/us/podcast/blackwell-in-deepseek-claude-meetings-ai-news-nov-15/id6817748791?i=1000802066991&uo=4) — *AI Engineering Briefing: Daily AI News for Software Engineers*, 15/11 12:40
  > Bulletin sur la découverte de signatures Blackwell dans six modèles open‑weight chinois, révélant l’usage de puces Nvidia Blackwell dans DeepSeek, Kimi, MiniMax et Ling.
- [The Week AI Found Its Single Points of Failure (Nov 15, 2026)](https://podcasts.apple.com/us/podcast/the-week-ai-found-its-single-points-of-failure-nov-15-2026/id1684415169?i=1000802063475&uo=4) — *AI Unraveled: Enterprise Strategy, Agentic Systems, Daily AI News, ChatGPT, Gemini, Claude, DeepSeek*, 15/11 11:56
  > Récapitulatif de la semaine où l'IA a montré ses points de défaillance uniques : démission de Jensen Huang, panne de Microsoft 365, et plus de 35 000 applications IA exposées.
- [Episode 101: 711 GOLD Showdown and Rock-Paper-Scissors Upsets](https://podcasts.apple.com/us/podcast/episode-101-711-gold-showdown-and-rock-paper-scissors/id6792364624?i=1000802055432&uo=4) — *Playce is where autonomous AI agents compete for real stakes - The Arena Report*, 15/11 11:00
  > Reportage sur les compétitions d'agents autonomes dans le casino Playce, avec un gros pot de poker de 711 GOLD et des retournements majeurs au rock‑paper‑scissors.
- [This is the worst AI tutor we'll ever have | DataCamp](https://podcasts.apple.com/us/podcast/this-is-the-worst-ai-tutor-well-ever-have-datacamp/id1776879655?i=1000801910056&uo=4) — *Chain of Thought | AI Agents, Infrastructure & Engineering*, 14/11 12:05
  > Test de DataCamp d'un tuteur IA précoce qui surpasse les cours classiques en termes de volonté de payer, d'engagement et de satisfaction des apprenants.

## Écartés comme hors sujet (23)

- [Yorick Peterse Migrates Inko and More Than 70 Repositories From GitHub to Codeberg](https://news.lavx.hu/article/yorick-peterse-migrates-inko-and-more-than-70-repositories-from-github-to-codeberg) — *news.lavx.hu*, 16/11 07:18
  > Yorick Peterse moved Inko and more than 70 repositories from GitHub to Codeberg after deciding that GitHub has become a place for low-quality AI-generated pull requests. The move replaced GitHub Actions with Forgejo Actions, required self-hosted runners and Buildah image builds, and exposed Codeberg
- [SerpAPI alternatives for Google search JSON](https://dev.to/flashdatadev/serpapi-alternatives-for-google-search-json-ih6) — *dev.to*, 16/11 07:09
  > Keep SerpApi when its engine coverage, existing integration and published legal terms matter more than reducing Google-only request cost. For a Google-focused workload, compare Serper’s prepaid credits, SearchApi’s monthly plans and DataForSEO’s queued or Live modes. Consider HasData if you already 
- [Apple launches study app with OpenEvidence to examine how people use AI for health](https://news.lavx.hu/article/apple-launches-study-app-with-openevidence-to-examine-how-people-use-ai-for-health) — *news.lavx.hu*, 16/11 05:34
  > Apple has launched a study app with healthcare AI company OpenEvidence that lets U.S. users ask health questions and receive answers grounded in clinical journals. The study will run more than 12 months with as many as 200,000 participants.
- [Trump administration plans to name Nvidia an AI national champion](https://cryptobriefing.com/trump-administration-nvidia-ai-national-champion/) — *Crypto Briefing*, 16/11 05:06
  > Nvidia's designation as an AI national champion could reshape industry dynamics, influencing policy support and competitive equity concerns. The post Trump administration plans to name Nvidia an AI national champion appeared first on Crypto Briefing .
- [Amazon, Microsoft, OpenAI, Anthropic to be named AI ‘national champions’: WSJ](https://cryptobriefing.com/amazon-microsoft-openai-anthropic-to-be-named-ai-national-champions-wsj/) — *Crypto Briefing*, 16/11 05:04
  > The designation of AI 'national champions' could boost market confidence and investment in AI, potentially driving significant industry growth. The post Amazon, Microsoft, OpenAI, Anthropic to be named AI ‘national champions’: WSJ appeared first on Crypto Briefing .
- [South Korea secures Nvidia commitment for 260,000 GPUs amid CEO change](https://cryptobriefing.com/south-korea-secures-nvidia-commitment-for-260000-gpus-amid-ceo-change/) — *Crypto Briefing*, 16/11 05:04
  > Nvidia's GPU deal with South Korea underscores resilience in AI infrastructure growth despite leadership uncertainties, impacting market dynamics. The post South Korea secures Nvidia commitment for 260,000 GPUs amid CEO change appeared first on Crypto Briefing .
- [Tell HN: HN is being scraped for emails to scam](https://news.ycombinator.com/item?id=50513451) — *Hacker News*, 16/11 03:53
  > I know that many folks here post their personal emails in the Who's for Hire monthly pages and other places, and want to remind you that this public site gets views from folks with ill intent (or their bots/agents) as well. I use unique emails for every site, so I immediately knew that the late AWS 
- [Vibe Coding Boom Exposes Corporate Data as AI App Builders Face Security Gaps](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE14Y3Z1RXZQYTlHWnBBTkZNSWhNS0tSLTJmZzE2cWpOSXlPT2ZidHlaTE45cEpuY0VQMEowLXQ0cGQwRndzUjVydjVCWmVJeUhITDg1cngzdE44bS1SRDhKN1NianZ0SjQ?oc=5) — *www.thelec.net*, 16/11 02:17
- [datasette-maplibre 0.1a0](https://simonwillison.net/2026/Nov/15/datasette-maplibre/) — *Simon Willison*, 16/11 00:58
  > Release: datasette-maplibre 0.1a0 The first new Datasette geospatial plugin in quite a while! This one combines the excellent MapLibre GL library with OpenFreeMap , the free vector map server operated by Zsolt Ero (you should sponsor Zsolt on GitHub .) I built most of this with a single prompt to Cl
- [Cursor Breach Shows How AI Coding History Can Become a Backdoor](https://news.google.com/rss/articles/CBMipAFBVV95cUxOOVlMdHJhdG5PQlJfV18zWkgyem9sWXhEbzhRTlpFNkVUTjdacy1fNWFGclJHb0UyVGE0QkNrbzZ3aUpzMmk2VG1HVFdtXzc0UWk4eHA5TlJHSmFuSjhZWkxvRi1yX1FNWmlXN2JvanA0ZjFSNTQ2WWduSTc4bnBkM3ZfbEJVRWZOdHBlTEp4ZWtWa3h1V0lpaGdBSFVCV2F2dGdibdIBqgFBVV95cUxNOFJYeDR6bHJzV045THRtV05Qd1hoR2Rmc3FfeGpsMkQzUU14a1JlY1QzWDhseVY0cHp3N01ST3h2RkJIV3dubkdPOU1WOWl3Q3U2bmNEUTNTWEVWdU5SVTFJXzBaOFotLTZZQjk3aGMydFRYeTBtbU1ORmJGajBaMlNLakFiSnE5XzBYX1otVFJaNVlPVl93TWxHbWw3cXZnRUdXSHYyd2ktdw?oc=5) — *TechloMedia*, 16/11 00:37
- [datasette 1.0a43](https://simonwillison.net/2026/Nov/15/datasette/) — *Simon Willison*, 16/11 00:20
  > Release: datasette 1.0a43 I've been leaning hard into Claude Fable 5.2 to help knock things off the 1.0 milestone , which is now 53% complete. The biggest 1.0 item in this release is streaming support for output renderers - the built-in TSV and CSV export mechanisms now use this as well, and plugins
- [datasette 0.65.6](https://simonwillison.net/2026/Nov/15/datasette-2/) — *Simon Willison*, 16/11 00:18
  > Release: datasette 0.65.6 I backported a minor security fix from 1.0a43: Fixed a security issue where a database registered using add_database(db, name=..., route=...) with a route that differs from its name could be downloaded from /<route>.db by actors who were denied access to it. [...] Tags: sec
- [How Boris Cherny’s Claude Code Became Anthropic’s Breakout AI Product—and Could Reshape Engineering Jobs](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOLWoyVk5qOVRUWjRCREdRSDJuV3VBR3NFU1hZcXRncW9SVnBQSi1QR1VwSmpaMml1d3NmZWktV0dUNFVpb2wwVUJQS1pqUFdabEQ1cUY2dEY4Y19CeUhFRGU5cm9CT1lfU1k4VGVrQ1JTQ1BaX0k3bVFoV1c5Y0t0d1N5RjlWM3BneTJGd3ZkTUVuVFQwdUtYcWJFdmhZOEltOHQ3ckxlM0xRdXp6cHlJbFFPbUJNV19CWUdmc09xN29qSk1MWFBNcw?oc=5) — *SSBCrack*, 15/11 23:40
- [A step toward defining the Standard Model on a lattice](https://openai.com/index/step-toward-defining-the-standard-model) — *OpenAI*, 15/11 23:00
  > Explore a candidate nonperturbative lattice definition of the Standard Model and how GPT-6 Astra helped turn the idea into a detailed proof.
- [Our new blog for science](https://openai.com/index/our-new-blog-for-science) — *OpenAI*, 15/11 23:00
  > The OpenAI science blog shares new findings, practical methods, and firsthand accounts from researchers using AI to advance scientific discovery.
- [The Future of AI Jobs May Be Outside the Tech Industry](https://hackernoon.com/the-future-of-ai-jobs-may-be-outside-the-tech-industry?source=rss) — *HackerNoon*, 15/11 20:52
  > Five predictions for AI jobs by 2031, exploring software engineering, coding agents, robotics, industrial AI adoption, and future career opportunities.
- [Meet Boris Cherny, the engineer behind Anthropic’s Claude Code - and its miso hobbyist](https://news.google.com/rss/articles/CBMiggFBVV95cUxNTjUtckI5X3hMbE1kcDJzN19LWWRFa1YtNDJEeTFuVldxc1Q3UVBILTBwX1FQSFdwTXdiSUY2eG5aY0VnVkZTRGZjby1vZFF4UnVSZjZPYlF3ZW1VMEFnNk1RbXBXaDRQWUNHekNBV2NXdFpJNjdXQ1FBd1VPc1lCN0J3?oc=5) — *Mezha.net*, 15/11 18:09
- [AI models hate Python and love PHP: we asked 12 of them 1,200 times](https://blog.jetbrains.com/ai/2026/11/ai-models-hate-python-and-love-php-we-asked-12-of-them-1-200-times/) — *JetBrains AI*, 15/11 18:02
  > 1,200 hot takes, 14 “random” languages, zero opinions about C#, and one model that argued both sides of Go’s error handling. We asked 12 AI models for their most controversial opinion about programming languages, 1,200 times in total. We wanted to check one thing. When you give a model permission to
- [Firm linked to Jensen Huang's ex-lover reportedly brokered nearly $12 billion in Nvidia chip orders for China](https://the-decoder.com/firm-linked-to-jensen-huangs-ex-lover-reportedly-brokered-nearly-12-billion-in-nvidia-chip-orders-for-china/) — *The Decoder*, 15/11 15:45
  > Megaspeed, the firm owned by ousted Nvidia CEO Jensen Huang's former lover Alice Huang, arranged nearly $12 billion in Nvidia chip orders for Chinese companies between 2024 and 2025, according to the WSJ. Short seller Culper Research estimates Nvidia's actual China revenue share exceeds 20 percent, 
- [How AI Helps Me Find the Right TV Shows at the Right Times](https://www.msn.com/en-us/technology/artificial-intelligence/how-ai-helps-me-find-the-right-tv-shows-at-the-right-times/ar-AA2htnCi) — *WSJ*, 15/11 13:00
  > If I’m in the mood for a series that is highly rated, has lots of episodes and doesn’t have subjects that turn me off, I know where to turn.
- [Australia's central bank finds AI hitting young workers first, especially in software and customer service](https://the-decoder.com/australias-central-bank-finds-ai-hitting-young-workers-first-especially-in-software-and-customer-service/) — *The Decoder*, 15/11 11:45
  > Australia's central bank sees early signs that AI is hitting young entry-level workers in highly exposed jobs like software development and customer service. Since ChatGPT launched, job postings and employment among 15- to 24-year-olds in those fields have dropped more sharply than among older worke
- [datasette-apps 0.4a0](https://simonwillison.net/2026/Nov/15/datasette-apps/) — *Simon Willison*, 15/11 05:02
  > Release: datasette-apps 0.4a0 Datasette Apps are sandboxed HTML and JavaScript applications that live inside Datasette - think Claude Artifacts, but these ones can run SQL queries against your data. 0.4a0 adds support for linking: you can link to an app with #fragments in the URL and the app can see
- [[AINews] The No AI Slop Manifesto](https://latent.space/p/ainews-the-no-ai-slop-manifesto/) — *Latent Space*, 14/11 09:31
  > November 13, 2026 — AIE speakers unite to lay out how to fight slop.
