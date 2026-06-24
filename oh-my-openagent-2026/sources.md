# Sources

本文采用 evidence-first 口径：所有版本号、计数、安装路径、许可和外部生态事实都来自一手来源或明确标注的项目自述。证据截至 2026-06-25，北京时间。

## Primary Sources

| ID | 来源 | 用途 |
|---|---|---|
| S01 | GitHub API: `repos/code-yeongyu/oh-my-openagent` | 仓库身份、默认分支、公开计数、许可证分类、更新时间 |
| S02 | GitHub API languages endpoint | 语言字节分布 |
| S03 | Local checkout at `881e612f825cd44a29e4def46b5618035be13f61` | 代码结构、包数量、组件计数 |
| S04 | Target `README.md` | 两种 edition、安装命令、命名提醒、功能主张、遥测摘要 |
| S05 | `docs/guide/installation.md` | OpenCode Ultimate、Codex Light、marketplace 与降级模式 |
| S06 | `docs/guide/overview.md` | 总体架构与 agent 角色 |
| S07 | `docs/guide/orchestration.md` | planning、execution、workers、delegation categories 与 notepad 系统 |
| S08 | `docs/guide/team-mode.md` | Team Mode 默认状态、工具、上限和关闭协议 |
| S09 | `docs/reference/features.md` | agents、hooks、MCP tiers 与功能模块 |
| S10 | `docs/reference/configuration.md` | 配置优先级、兼容命名、环境变量与安全边界 |
| S11 | `docs/reference/codex-telemetry.md` | Codex Light 遥测事件、哈希、状态文件和 opt-out |
| S12 | `ROADMAP.md` | package layering refactor、多 harness 方向与抽象谨慎态度 |
| S13 | `LICENSE.md` | Sustainable Use License 的授权与限制 |
| S14 | `package.json` | npm 包名、版本、scripts、workspaces、bin aliases 与 license |
| S15 | `packages/omo-codex/plugin/.codex-plugin/plugin.json` | Codex plugin 元数据、hooks 与 capability |
| S16 | `packages/omo-codex/plugin/.mcp.json` | Codex plugin MCP server 列表 |
| S17 | `packages/omo-opencode/src/agents/builtin-agents.ts` | OpenCode 内置 agent 清单 |
| S18 | `packages/omo-opencode/src/mcp/index.ts` | OpenCode 内置 MCP 清单 |
| S19 | npm registry views | `oh-my-opencode`、`oh-my-openagent`、`lazycodex-ai` 的发布信息 |
| S20 | GitHub Releases API | 最新正式产品 release `v4.13.0` |
| S21 | OpenAI Codex CLI official docs | Codex CLI 的本地 coding agent 定位 |
| S22 | OpenAI Codex plugin official docs | plugin marketplace 与 build model |
| S23 | OpenAI Codex skills official docs | open agent skills packaging model |
| S24 | OpenAI AGENTS.md official docs | Codex 项目指令分层 |
| S25 | OpenCode official docs | OpenCode agent、plugin 与 config model |

完整机器可读映射见 [data/source-map.tsv](data/source-map.tsv)。

## Evidence Levels

- `primary`: 项目代码、项目文档、官方 API、官方 registry、官方产品文档。
- `project-authored claim`: 项目 README、guide、release body 中由项目作者给出的定位、体验和能力描述。
- `author analysis`: 本文基于多项来源做出的结构化解释和采用建议。

当项目文档和代码快照存在轻微不一致时，本文优先使用代码快照给出的计数，并在正文说明差异来源。

## Not Covered

- 未运行 `bunx oh-my-openagent install` 或 `npx lazycodex-ai install`。
- 未连接真实 OpenCode、Codex、模型供应商或 Git Bash 环境做端到端安装测试。
- 未验证 README 中社区评价、star 增长叙述或 benchmark 外推。
- 未审计目标项目全部源码安全性，也不构成法律、合规或商业建议。

## Primary URLs

- https://github.com/code-yeongyu/oh-my-openagent
- https://api.github.com/repos/code-yeongyu/oh-my-openagent
- https://registry.npmjs.org/oh-my-opencode
- https://registry.npmjs.org/oh-my-openagent
- https://registry.npmjs.org/lazycodex-ai
- https://developers.openai.com/codex/cli
- https://developers.openai.com/codex/plugins
- https://developers.openai.com/codex/skills
- https://developers.openai.com/codex/guides/agents-md
- https://opencode.ai/docs/
