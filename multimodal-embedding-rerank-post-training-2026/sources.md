# Sources

Evidence reviewed through 2026-07-07. The article separates source facts, author-reported model claims, company product documentation and author analysis.

## Evidence Scale

- **A**: paper, official repository, benchmark paper or survey with inspectable method details.
- **B**: company research article, industrial paper, product blog or author-reported online experiment. Useful for deployment signals, but not independently audited.
- **C**: product documentation or model usage page. Useful for API scope, modality support and operational limits, not for training recipe claims.

## Primary Research And Official Technical Sources

1. **S01, A**: VLM2Vec, arXiv, 2024-10-07. https://arxiv.org/abs/2410.05160
   Used for instruction-conditioned contrastive training, MMEB scope, and multimodal embedding baseline evidence.

2. **S02, A**: VLM2Vec-V2, arXiv, 2025-07-07. https://arxiv.org/abs/2507.04590
   Used for MMEB-V2 and the expansion from image-text tasks to video and visual-document tasks.

3. **S03, A**: Qwen3 Embedding and Reranker, arXiv and official repository, 2025-06-05. https://arxiv.org/abs/2506.05176 and https://github.com/QwenLM/Qwen3-Embedding
   Used for the text embedding/reranker analogue: unsupervised pretraining, SFT, multilingual data synthesis, Matryoshka Representation Learning and reranker scoring pattern.

4. **S04, A**: Qwen3-VL-Embedding and Reranker, arXiv and official repository, 2026-01-08. https://arxiv.org/abs/2601.04720 and https://github.com/QwenLM/Qwen3-VL-Embedding
   Used for multimodal embedding/reranker multi-stage training, contrastive pretraining, reranker distillation and 32k-context support. The paper abstract contains a date typo around "Jan 8, 2025"; this article treats the arXiv submission date as 2026-01-08.

5. **S05, A**: ColPali, arXiv and official repository, 2024-07-01. https://arxiv.org/abs/2407.01449 and https://github.com/illuin-tech/colpali
   Used for visual document retrieval, page-image multi-vector embedding, late interaction and ViDoRe-style evaluation.

6. **S06, A**: MM-R5, arXiv, 2025-06-14. https://arxiv.org/abs/2506.12364
   Used for SFT plus RL reranking evidence: reasoning chain supervision, task-specific reranking reward and reasoning-format reward.

7. **S07, A**: Think Then Embed, arXiv, 2025-10-06. https://arxiv.org/abs/2510.05014
   Used for the reason-before-embed pattern and embedding-centric reasoning trace supervision.

8. **S13, B**: On-Policy Distillation, Thinking Machines Lab, 2025-10. https://thinkingmachines.ai/blog/on-policy-distillation/
   Used for OPD mechanics: student on-policy trajectories, teacher token-level feedback, and the distinction between SFT, RL and OPD.

9. **S14, A**: A Survey on Online Policy Distillation, arXiv, 2026-04-01. https://arxiv.org/abs/2604.00626
   Used for OPD taxonomy and exposure-bias framing.

10. **S15, A**: PRISM, arXiv and repository, 2026-04-30. https://arxiv.org/abs/2604.28123 and https://github.com/XIAO4579/PRISM
    Used for SFT to OPD pre-alignment to RLVR in multimodal reasoning.

11. **S16, A**: Vision-OPD, arXiv and repository, 2026-05-18. https://arxiv.org/abs/2605.18740 and https://github.com/VisionOPD/Vision-OPD
    Used for fine-grained visual understanding with crop-conditioned teacher and full-image student rollouts.

## Industrial And Product Sources

12. **S08, B**: Pailitao-VL, arXiv industrial paper, 2026-02-14. https://arxiv.org/abs/2602.13704
    Used for large-scale visual commerce retrieval and rerank evidence. Reported online and business metrics are treated as company-authored claims.

13. **S09, B**: Gemini Embedding 2, arXiv and Google blog, 2026-05-26. https://arxiv.org/abs/2605.27295 and https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2/
    Used for native multimodal embedding product and closed-model training signal. Benchmark results are author-reported.

14. **S10, C**: Amazon Nova Multimodal Embeddings documentation, 2025-10-28. https://docs.aws.amazon.com/nova/latest/nova2-userguide/embeddings.html
    Used for product-surface evidence: unified semantic space, modality coverage, and context limits.

15. **S11, B**: PinCLIP, arXiv and Pinterest Labs publication listing, 2026-03-05. https://arxiv.org/abs/2603.03544 and https://labs.pinterest.com/publications
    Used for industrial retrieval, ranking and recommendation representation learning.

16. **S12, B**: Amazon MML-TP, Amazon Science, 2025-10. https://www.amazon.science/publications/multimodal-learning-with-online-text-cleaning-for-e-commerce-product-search
    Used for online text cleaning and token pruning in noisy e-commerce product search.

17. **S17, C**: Cohere multimodal embeddings documentation, 2026. https://docs.cohere.com/docs/multimodal-embeddings
    Used as product-interface evidence for multimodal business document embedding.

18. **S18, C**: Voyage multimodal embeddings documentation, 2026. https://www.mongodb.com/docs/voyageai/models/multimodal-embeddings/
    Used as product-interface evidence for hosted multimodal embeddings.

## Method Boundary

The article does not treat a hosted product page as proof of its training recipe unless the training method is described in an accompanying paper or official technical report. Vendor-reported benchmark and A/B results are marked as author-reported evidence and are not presented as audited third-party measurements.
