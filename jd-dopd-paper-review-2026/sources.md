# 京东 DOPD 论文 Review 2026：来源说明

证据复核时间：2026-07-07，北京时间。本文评审对象为 arXiv:2606.30626v1 `DOPD: Dual On-policy Distillation`。论文于 2026-06-29 提交至 arXiv，主题分类为 cs.AI。本文将 OPD 译作“在线/在策略蒸馏”，将 privileged information 译作“特权信息”或“训练期特权上下文”。

## 证据分层

| 等级 | 含义 | 使用方式 |
|---|---|---|
| A | 原始论文、官方论文页面、官方技术报告或官方产品发布页 | 可支撑题名、作者、方法定义、实验结果、数据规模和官方模型事实 |
| B | 综述论文、二级研究材料或社区材料 | 只用于背景定位，不作为核心实验结论的独立验证 |
| C | 媒体、社交平台、个人解读 | 仅用于发现线索；本评审未使用 C 级证据支撑正文结论 |

## 主来源

| ID | 来源 | 日期 | 等级 | 本文使用的事实边界 |
|---|---|---:|---|---|
| S01 | Yu et al., [DOPD: Dual On-policy Distillation](https://arxiv.org/abs/2606.30626) | 2026-06-29 | A | 论文题名、作者、摘要、方法、实验结果、局限和提交版本。 |
| S02 | Yu et al., [DOPD PDF](https://arxiv.org/pdf/2606.30626) | 2026-06-29 | A | 表格数字、实验配置、附录提示词与特权输入细节；本地归档见 `sources/`。 |
| S03 | Yu et al., [DOPD HTML experimental](https://arxiv.org/html/2606.30626) | 2026-06-29 | A | 用于交叉核对表格、章节结构和公式位置。 |
| S04 | OpenAI, [Introducing GPT-5.4](https://openai.com/index/introducing-gpt-5-4/) | 2026-03-05 | A | 仅用于确认论文引用的 GPT-5.4 官方发布时间和模型存在性，不用于背书 DOPD 实验结果。 |
| S05 | Qwen Team, [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) | 2025-05-14 | A | 用作 Qwen3 系列后训练与 OPD 背景，不用于替代 DOPD 论文自身实验。 |
| S06 | Song and Zheng, [A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626) | 2026-04-01 | B | 用于 OPD 研究谱系定位；评审结论仍以 DOPD 原论文为准。 |

## 本地归档

- `sources/dopd-dual-on-policy-distillation-2606.30626.pdf`
- `sources/dopd-dual-on-policy-distillation-2606.30626.html`
- `sources/dopd-dual-on-policy-distillation-2606.30626.txt`

## 口径与不确定性

- 本评审没有获得作者代码、训练数据和完整日志，因此不把论文实验结果表述为独立复现结果。
- 论文使用 GPT-5.4 生成并复核特权输入。该步骤具有成本、可得性和潜在数据偏置风险，正文已将其列为复现边界。
- VA-OPD 在论文表 2 中标注为作者复现版本，因为官方代码未发布。本文按论文原始口径报告，不把该数字视为原方法官方结果。
- DOPD 的路由阈值、outlier 去除、Top-K 策略和 full-vocabulary JS 只在论文给定实验环境下被验证。跨模型、跨 tokenizer、跨任务长度迁移时仍需重新校准。
