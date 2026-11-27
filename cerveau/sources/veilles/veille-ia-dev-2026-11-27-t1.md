# Veille Outils & code 2026-11-27 : Modèles et décodage avancé

Région : Outils & code · Date : 2026-11-27

Ces articles portent sur de nouveaux modèles de grande taille, des techniques de décodage spéculatif et des benchmarks de performances, offrant des gains d’efficacité pour les charges de travail IA.

- **vLLM vs TensorRT-LLM vs SGLang: Serving Throughput, KV-Cache Paging & Speculative Decoding** (dev.to, note 8/10)
  vLLM vs TensorRT-LLM vs SGLang: Serving Throughput, KV-Cache Paging & Speculative Decoding LLM serving cost is dominated by a single resource: HBM bandwidth. A 70B parameter model in FP8 needs ~9.5ms per forward pass just to stream weights off an H100's 3.35 TB/s memory bus, yet a single user decodi
- **Tencent Open-Sources DFly2: Speculative Decoding That Reuses the Target’s Sparse KV Cache** (MarkTechPost, note 7/10)
  Tencent open-sourced DFly2, a speculative decoding drafter for sparse-attention LLMs. Each draft layer reuses the target's KV cache and top-k indexer picks, adding no draft KV memory and lifting 64K serving throughput by up to 81%. The post Tencent Open-Sources DFly2: Speculative Decoding That Reuse
- **Sakana AI Releases Namazu Small, a 30B Model Built on Nemotron 3 Nano** (MarkTechPost, note 7/10)
  Sakana AI released Sakana Namazu Small, a 30B-A3B reasoning model built on NVIDIA Nemotron 3 Nano. It averages 60.1 across 25 benchmarks, ahead of the 120B Nemotron 3 Super at 56.2. The post Sakana AI Releases Namazu Small, a 30B Model Built on Nemotron 3 Nano appeared first on MarkTechPost .
- **Local AI Coding Model Jumps From 60.8 to 75.6 on SWE-bench Verified at Same Size, PrismML Says** (Tech Times, note 7/10)
  Local AI coding model Ternary Bonsai 2.5 27B from PrismML reports 75.6 on SWE-bench Verified, up from 60.8 at the same 5.93 GB file size, against 80.6 for full-precision Qwen3.8 27B. The smallest ...
- **Microsoft’s Aion 1.0 Instruct: A better on-device language model for Windows** (InfoWorld, note 7/10)
  Swapping the in-OS AI inference engine in Windows 11 is much like swapping out the tires of a car — while in the middle of a Grand Prix race. But Microsoft’s embedded Phi Silica small language model soon will be replaced by the company’s new Aion series of models , first through the Windows Insider
- **DeepMind's Gemini Robotics 2.5 Aims to Make Robots Safer, More Dexterous, and Faster Learners** (InfoQ, note 7/10)
  Google DeepMind introduced Gemini Robotics 2.5, a vision-language-action (VLA) model designed to improve robots' dexterity, reliability, and learning speed, while enabling safer operation in unstructured real-world environments. By Sergio De Simone
- **Tests Reveal Which Cheap AI Models Match Claude Code on Five Jobs** (Geeky Gadgets, note 6/10)
  Free Anthropic Claude Code alternatives outscore the paid subscription in a five-job benchmark test where OpenCode and DeepSeek reached a 100.6% score.
- **Shuffle the Questions to Catch an LLM That Memorized Its Benchmark** (Towards Data Science, note 6/10)
  Two short Python functions and a free Colab GPU score a model in about half an hour; a z above 3 merits a look, while a near-zero score is more of a shrug. The post Shuffle the Questions to Catch an LLM That Memorized Its Benchmark appeared first on Towards Data Science .
- **Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon** (Hugging Face, note 6/10)
- **Building on Nemotron 3.5 Parse: Open Data, Fine-Tuning, and Faster Inference** (Hugging Face, note 6/10)
- **After OpenAI and Anthropic shut the door on their data, a Chinese AI developer is turning to Google and Meta instead** (The Decoder, note 5/10)
  Chinese AI companies Z.AI and Moonshot AI have to delay their next flagship models and are looking for new sources of training data. The article After OpenAI and Anthropic shut the door on their data, a Chinese AI developer is turning to Google and Meta instead appeared first on The Decoder .
- **Anthropic says it moved its Claude API from Python to Rust with no downtime** (InfoWorld, note 5/10)
  When Anthropic decided to port its Messages API from Python to Rust, Claude wrote the code in about a week. But proving the new system worked as well as the old one, post-migration, was the real project. Anthropic engineers addressed this validation problem by turning the production Messages API its
- **GPT-6.2 Astra: AI Solves 200-Year Math Secrets** (dev.to, note 3/10)
  Chapter 1: The 22-Minute Miracle The Hook: Narrative scene of GPT-6.2 Astra cracking a two-century-old historical and mathematical mystery in less time than it takes to order lunch. Break down what actually happened: contrasting the centuries of human frustration with 1,320 seconds of raw machine sy
