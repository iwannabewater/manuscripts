# DeepSeek V4 Technical Report 2026

DeepSeek V4 官方 technical report 的中文深度解读报告，覆盖模型架构、CSA/HCA 混合注意力、mHC、Muon、系统工程、预训练、后训练、评测对比、代际演进和实践判断。

## Files

- `index.html`: 可读与可打印的报告源码。
- `deepseek-v4-technical-report-2026.pdf`: PDF 成品。
- `sources.md`: 一手来源、核验口径与边界。
- `data/source-map.tsv`: 正文来源编号与 URL 映射。
- `fonts/`: PDF 使用的本地中文字体。

## Scope

报告以 DeepSeek 官方透明中心、DeepSeek-V4 technical report、DeepSeek V4 model card、DeepSeek-V3.2、DeepSeek-V3 与 DeepSeek-R1 官方论文为事实依据。正文重点解释 V4 如何从 V3/V3.2 的 MLA、MoE、MTP、DSA 与后训练体系演进到 1M context、CSA/HCA、mHC、Muon、FP4 QAT、OPD 和长程 Agent 基础设施。报告不把官方内部 benchmark 等同于第三方复现结果；涉及设计动机和工程判断的部分均为基于公开材料的分析。
