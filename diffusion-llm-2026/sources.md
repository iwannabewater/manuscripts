# Diffusion LLM 2026 Sources

Source check date: 2026-05-22.

The report uses primary or near-primary sources where available: arXiv pages, official project repositories, official lab/product pages, and model cards. Secondary media is intentionally excluded from the main citation set unless it merely helps locate an original source.

| ID | Source | URL | Notes |
|---|---|---|---|
| S01 | Structured Denoising Diffusion Models in Discrete State-Spaces | https://arxiv.org/abs/2107.03006 | D3PM; discrete transition matrices and absorbing-state diffusion. |
| S02 | Diffusion-LM Improves Controllable Text Generation | https://arxiv.org/abs/2205.14217 | Continuous diffusion over word vectors; controllable text generation. |
| S03 | Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution | https://arxiv.org/abs/2310.16834 | SEDD; score entropy for discrete diffusion language modeling. |
| S04 | Simple and Effective Masked Diffusion Language Models | https://arxiv.org/abs/2406.07524 | MDLM; simplified masked diffusion objective and training recipe. |
| S05 | Large Language Diffusion Models | https://arxiv.org/abs/2502.09992 | LLaDA paper; large masked diffusion model trained from scratch. |
| S06 | ML-GSAI/LLaDA official repository | https://github.com/ML-GSAI/LLaDA | LLaDA model release, inference and evaluation code. |
| S07 | LLaDA 1.5: Variance-Reduced Preference Optimization for Large Language Diffusion Models | https://arxiv.org/abs/2505.19223 | VRPO and preference optimization for LLaDA. |
| S08 | LLaDA-MoE: A Sparse MoE Diffusion Language Model | https://arxiv.org/abs/2509.24389 | Sparse MoE diffusion language model. |
| S09 | Gaoling School of Artificial Intelligence and Ant Group co-launch LLaDA-MoE model series | https://en.ruc.edu.cn/2025-09/26/c_2822.htm | Institution announcement for RUC and Ant Group LLaDA-MoE collaboration. |
| S10 | inclusionAI/LLaDA2.X official repository | https://github.com/inclusionAI/LLaDA2.X | InclusionAI / Ant Group LLaDA2.0 series and open-source claims. |
| S11 | DreamLM/Dream official repository | https://github.com/DreamLM/Dream | Dream 7B, Dream-Coder, DreamOn, inference parameters and training code. |
| S11a | Dream 7B: Diffusion Large Language Models | https://arxiv.org/abs/2508.15487 | Dream paper. |
| S12 | Introducing Mercury, the World's First Commercial-Scale Diffusion Large Language Model | https://www.inceptionlabs.ai/blog/introducing-mercury | Mercury Coder announcement and benchmark table. |
| S13 | Introducing Mercury, our General Chat Diffusion Large Language Model | https://www.inceptionlabs.ai/blog/introducing-mercury-our-general-chat-model | General chat model, API access and benchmark table. |
| S13a | Mercury 2 and the Rise of Real-time Subagents | https://www.inceptionlabs.ai/blog/rise-of-realtime-subagents | Mercury 2 enterprise subagent use case. |
| S14 | Gemini Diffusion | https://deepmind.google/models/gemini-diffusion/ | Google DeepMind official Gemini Diffusion page and benchmark table. |
| S15 | Scaling Diffusion Language Models via Adaptation from Autoregressive Models | https://machinelearning.apple.com/research/scaling-diffusion-language-models | Apple ML Research page; AR-to-DLM adaptation and Tencent AI Lab coauthor line. |
| S16 | DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Generation | https://machinelearning.apple.com/research/diffucoder | Apple ML Research page; code dLLM and coupled-GRPO. |
| S17 | Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding | https://arxiv.org/abs/2505.22618 | Approximate KV cache and confidence-aware parallel decoding. |
| S18 | Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models | https://arxiv.org/abs/2503.09573 | Block-wise hybrid diffusion/autoregressive language modeling. |
| S19 | DPad: Efficient Diffusion Language Models with Suffix Dropout | https://arxiv.org/abs/2508.14148 | Suffix dropout and long-sequence diffusion inference acceleration. |
| S20 | CoDA: Coding LM via Diffusion Adaptation | https://arxiv.org/abs/2510.03270 | Salesforce AI Research code diffusion model paper. |
| S20a | Salesforce/CoDA-v0-Instruct model card | https://huggingface.co/Salesforce/CoDA-v0-Instruct | Model card, performance table and serving notes. |
| S21 | MMaDA: Multimodal Large Diffusion Language Models | https://arxiv.org/abs/2505.15809 | Multimodal diffusion foundation model. |
| S22 | LLaDA-V: Large Language Diffusion Models with Visual Instruction Tuning | https://arxiv.org/abs/2505.16933 | Diffusion-based multimodal LLM with visual instruction tuning. |
| S23 | LaViDa: A Large Diffusion Language Model for Multimodal Understanding | https://arxiv.org/abs/2505.16839 | Diffusion language backbone for multimodal understanding. |
| S24 | d1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement Learning | https://arxiv.org/abs/2504.12216 | diffu-GRPO and reasoning post-training. |
| S25 | TiDAR: Think in Diffusion, Talk in Autoregression | https://arxiv.org/abs/2511.08923 | Hybrid diffusion drafting and AR output architecture. |
| S26 | dLLM: Simple Diffusion Language Modeling | https://arxiv.org/abs/2602.22661 | Unified open-source diffusion language modeling framework. |

## Claims Kept Deliberately Narrow

- The report does not claim that OpenAI, Anthropic, Meta or Microsoft have released a public diffusion LLM product, because the source set did not contain official public releases for that claim.
- Vendor benchmark numbers are presented as vendor- or project-reported values unless independently verified in the same source set.
- LLaDA2.0 scale and openness claims are attributed to the official inclusionAI repository, not independently re-benchmarked.
