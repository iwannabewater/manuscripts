# RAG Frontiers 2026 Sources

Source check date: 2026-06-22 (Asia/Shanghai).

本文优先使用论文原文、正式论文页面、官方产品文档与厂商发布。论文中的性能数字只表示该论文设置下的结果；厂商页面中的能力描述按「厂商公开能力」呈现，不等同于独立复测。2026 年预印本统一标注为前沿信号，不写成已经形成共识的结论。

## Evidence levels

- **A**：正式会议或期刊论文，或论文最终公开版本。
- **B**：研究团队预印本，已公开方法、实验与局限，但未必完成同行评审。
- **C**：云平台、实验室或产品团队官方文档，可证明公开能力与产品边界。
- **D**：厂商自报 benchmark 或产品效果，只作实践信号，不作独立验证。

| ID | Level | Source | URL | Main use |
|---|---|---|---|---|
| S01 | A | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | https://arxiv.org/abs/2005.11401 | RAG 原始定义、参数化与非参数化记忆 |
| S02 | A | Dense Passage Retrieval for Open-Domain Question Answering | https://arxiv.org/abs/2004.04906 | 双塔稠密检索与开放域 QA |
| S03 | A | ColBERTv2 | https://arxiv.org/abs/2112.01488 | late interaction、检索质量与索引压缩 |
| S04 | A | HyDE | https://arxiv.org/abs/2212.10496 | 假设文档式查询扩展 |
| S05 | A | FLARE | https://arxiv.org/abs/2305.06983 | 生成过程中的主动检索 |
| S06 | A | Self-RAG | https://arxiv.org/abs/2310.11511 | 按需检索、自我批评与可控解码 |
| S07 | B | Corrective Retrieval Augmented Generation | https://arxiv.org/abs/2401.15884 | 检索质量判断、纠错与外部搜索 |
| S08 | A | RAPTOR | https://arxiv.org/abs/2401.18059 | 递归摘要树与多粒度检索 |
| S09 | B | From Local to Global: A Graph RAG Approach | https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/ | 全局语料问题与社区摘要 |
| S10 | A | Retrieval Augmented Generation or Long-Context LLMs? | https://arxiv.org/abs/2407.16833 | RAG、长上下文与 Self-Route |
| S11 | A | Search-R1 | https://arxiv.org/abs/2503.09516 | 用强化学习训练多轮搜索策略 |
| S12 | B | ReSearch | https://arxiv.org/abs/2503.19470 | 无过程监督的搜索推理训练 |
| S13 | B | DeepResearcher | https://arxiv.org/abs/2504.03160 | 真实网页环境中的深度研究训练 |
| S14 | B | A-RAG | https://arxiv.org/abs/2602.03442 | 分层检索接口与 test-time scaling |
| S15 | A | ColPali | https://arxiv.org/abs/2407.01449 | 文档页面视觉检索与 ViDoRe |
| S16 | A | VisRAG | https://arxiv.org/abs/2410.10594 | 绕过 OCR 的视觉原生 RAG |
| S17 | B | M2RAG Benchmark | https://arxiv.org/abs/2502.17297 | 多模态检索增强生成评测 |
| S18 | A | T2-RAGBench | https://aclanthology.org/2026.eacl-long.8/ | 文本与表格的真实检索、数值推理评测 |
| S19 | A | RAGAS | https://arxiv.org/abs/2309.15217 | 忠实度、答案相关性、上下文相关性 |
| S20 | A | PoisonedRAG | https://arxiv.org/abs/2402.07867 | 知识库投毒攻击面 |
| S21 | A | Retrieval Enhancements for RAG: Insights from a Deployed Customer Support Chatbot | https://aclanthology.org/2026.eacl-industry.13/ | 生产客服语料中的检索、融合与重排 |
| S22 | C | Azure AI Search Agentic Retrieval | https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-concept | 查询分解、并行检索、语义重排、日志与计费 |
| S23 | C | Vertex AI RAG Engine overview | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview | 托管摄取、转换、索引、检索与生成 |
| S24 | C | Amazon Bedrock Knowledge Bases parsing | https://docs.aws.amazon.com/en_us/bedrock/latest/userguide/kb-advanced-parsing.html | 多模态解析、图表与来源归因 |
| S25 | C | 阿里云百炼知识库 | https://help.aliyun.com/zh/model-studio/user-guide/rag-knowledge-base/ | 文档、表格、图像、多知识库召回与重排 |
| S26 | C | 腾讯云 Agentic RAG | https://cloud.tencent.com/document/product/1759/132211 | 反思、策略切换与多轮迭代检索 |
| S27 | C | 百度智能云千帆 AppBuilder | https://cloud.baidu.com/doc/AppBuilder/s/create-database | 企业级 RAG、Agent、工作流与 AI 搜索组件 |
| S28 | C/D | OpenAI Deep Research | https://openai.com/index/introducing-deep-research/ | 多步网页研究、工具使用与端到端 RL 的厂商描述 |
| S29 | C/D | Anthropic Research | https://www.anthropic.com/news/research | 多轮搜索、内部与外部知识协同、可核验引用 |
| S30 | B | WebDancer | https://arxiv.org/abs/2505.22648 | 自主信息检索 Agent 的训练流水线 |

## Conflicts and interpretation boundaries

- **稠密检索并不普遍优于 BM25。** DPR 在开放域 QA 中报告了相对 BM25 的明显优势 [S02]；T2-RAGBench 在文本与表格场景中发现混合 BM25 最强 [S18]；已部署客服研究则发现，把 BM25 与强稠密模型融合会降低其四个数据集的表现 [S21]。正文据此把「混合检索」写成待评测配置，不写成默认真理。
- **长上下文不是 RAG 的简单替代品。** 2024 年对比研究在资源充足时观察到长上下文平均更强，但 RAG 成本更低，且输入远超窗口时仍有优势 [S10]。这项结论依赖当时模型和数据集，正文只提炼「路由优于二选一」。
- **Agentic RAG 仍处于证据分层期。** Search-R1 已有正式会议版本 [S11]，A-RAG 仍是 2026 年预印本 [S14]；Azure、腾讯等产品文档证明能力已进入平台，但不证明所有真实任务都优于经典 RAG [S22, S26]。
- **Search-R1 的公开版本存在数字冲突。** COLM 2025 PDF 的摘要与结论写 24% 与 20% 的平均相对提升，结果概述与 arXiv 页面则写 41% 与 20%。正文采用较低的 24% 口径，并把差异保留在主张附近 [S11]。
- **厂商 benchmark 不作横向排名。** OpenAI 与 Anthropic 的产品页用于观察深度研究产品形态 [S28, S29]；文中不把其自报效果与学术论文数字直接比较。

## Deliberately excluded claims

- 不声称 RAG 可以消除幻觉；它新增了检索错误、上下文误用和知识库投毒等失败路径。
- 不声称 GraphRAG、HyDE、reranker 或 agent loop 对所有语料有效；不同论文和生产研究给出了相反或条件化结果。
- 不根据没有公开架构细节的产品体验反推厂商内部实现。
- 不把 2026 年尚未充分复现的预印本增益写成行业定论。
