# Harness Engineering 2026 Sources

Source check date: 2026-06-20 (Asia/Shanghai).

本文优先使用论文原文、标准规范、官方工程文章和官方开源仓库。2026 年 Harness 研究大多仍是预印本；其中的性能数字只表示论文设置下的结果。厂商内部评测、生产率和客户案例用于理解公开实践，不等同于第三方验证。仓库能力按固定提交快照描述，不以 Star 数或营销文案衡量成熟度。

## Evidence levels

- **A**：正式同行评审论文或最终会议版本。本研究核心 Harness 论文截至证据日尚无 A 级来源。
- **B**：公开预印本，包含方法、实验和局限，尚需独立复现。
- **C**：正式规范、官方文档、官方工程文章或固定开源提交，可证明公开设计和能力边界。
- **D**：厂商内部 Benchmark、生产率或效果数字，只作实践信号。

完整的 28 项来源、日期、固定提交、正文用途和限制见 `data/source-map.tsv`；关键主张与证据组合见 `data/evidence-matrix.tsv`。研究原文快照保存在 `sources/research/`、`sources/labs/` 和 `sources/ecosystem/`。

## Core evidence set

| ID | Level | Source | Main use |
|---|---|---|---|
| S01 | B | Harness-Bench | 定义、配置级评测、106 个任务与 5,194 条轨迹 |
| S02 | B | HarnessX | 类型化组件、轨迹驱动进化、模型协同训练 |
| S03 | B | Claw-SWE-Bench | 适配器契约、模型与 Harness 效应、成本披露 |
| S04 | B | SWE-Skills-Bench | Skill 的边际价值、版本冲突和 Token 开销 |
| S05 | B | Meta-Harness | 用完整历史搜索 Harness 代码、跨模型迁移 |
| S06 | B | Retrospective Harness Optimization | 无标签轨迹、自验证、自一致性和自偏好 |
| S07 | B | Natural-Language Agent Harnesses | 策略与机制分离、可读 Harness、模块消融 |
| S08 | B | Self-Harness | 弱点挖掘、候选修改和 held-out 回归 |
| S09-S18 | C/D | Anthropic、OpenAI、Google 官方材料 | 长程状态、工具、沙箱、协议、评测和任务控制面 |
| S19-S22 | C | MCP、Agent Skills、A2A | 生态协议的职责与安全边界 |
| S23-S28 | C | LangGraph、OpenHands、DeerFlow、Trae Agent、Qwen-Agent、AgentScope | 社区与国内实践的公开组件形态 |

## Conflicts and interpretation boundaries

- **Harness 还没有唯一公认定义。** S01 强调上下文、工具、状态、约束、权限、追踪和恢复；S07 进一步加入验证、停止、预算与多次 Agent 调用。正文采用两者公共集，并把任务契约、资源调度和评测纳入工程组件，不声称这是标准定义。
- **完整 Harness 差异不能直接归因到单一组件。** S01 和 S03 保留各 Harness 的原生执行行为，适合比较配置，不足以证明某个 Prompt、工具或恢复策略的因果增益。
- **Skills 的证据同时有正有负。** S21 证明开放格式与渐进披露已经存在；S04 发现 39/49 Skills 没有提高通过率，且版本冲突会退化。正文据此把 Skill 写成需要选择、锁版本和回归的依赖。
- **多 Agent 的收益依赖任务结构与预算。** S10 报告内部研究评测提高 90.2%，同时使用约 15 倍普通聊天 Token，并明确指出强依赖任务不适合并行。正文不把多 Agent 写成默认架构。
- **自动 Harness 优化仍处前沿信号期。** S02 截至证据日尚未公开完整代码；S05、S06、S08 的任务和反馈机制不同。正文不横向比较绝对增益，不声称任何方法已经形成生产共识。
- **协议状态需要按日期区分。** S19 是截至证据日的稳定 MCP 2025-11-25 规范；S20 是计划于 2026-07-28 发布版本的 Release Candidate。正文明确标注 RC，不写成稳定发布。
- **厂商数字不横向排名。** OpenAI 的 1,500 个 PR、500% 增长与 Anthropic 的 90.2%、40% 等结果都来自各自内部环境，用于观察工程机制，不代表独立复测。

## Deliberately excluded claims

- 不声称 Harness 比模型更重要；当前证据支持两者共同决定结果，且不同任务的相对贡献不同。
- 不声称增加 Skills、工具、Memory 或 Subagent 必然提高表现。
- 不根据产品体验反推未公开内部架构，也不把 GitHub Star 数当作能力或生产成熟度。
- 不把协议兼容等同于安全、可靠或语义兼容。
- 不把预印本的单任务增益写成跨模型、跨领域或长期稳定结论。
- 不把厂商内部生产率数字用于人员规划、财务预测或采购决策。

## Reproducibility notes

- 论文页面通过 `read` 抓取 arXiv HTML 快照，保留摘要、方法、实验口径与公开限制。
- 官方网页通过 `read` 本地提取器归档；原始 URL 保存在每个快照的 YAML Frontmatter。
- 开源仓库使用 `gh api` 查询北京时间 2026-06-20 结束前的最后提交，并在来源表和正文引用中固定 SHA。
- 网络核验只证明 URL 在核验时可访问，不证明页面的主张正确。
