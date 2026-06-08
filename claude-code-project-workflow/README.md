# Claude Code Project Workflow

署名：Winston
资料口径：截至 2026-05-04
交付形态：横向 A4 工程手册

本目录收录《Claude Code 项目工程工作流手册》。手册面向需要在项目交付中使用 Claude Code 的工程团队，讨论任务边界、上下文治理、规格化、实现闭环、验证门禁、交付审查和团队治理。

## Files

| 文件 | 说明 |
|---|---|
| `index.html` | 手册排版源文件 |
| `claude-code-project-workflow.pdf` | PDF 成品 |
| `sources.md` | 官方来源、资料口径与边界说明 |
| `data/source-map.tsv` | 来源页面与正文用途映射 |

## Scope

本文基于 Claude Code 官方文档、Anthropic 工程博客和项目交付实践编写，整理为一套可审查、可验证的团队协作流程。本文不代表 Anthropic 官方流程，也不替代官方文档；涉及版本能力、权限策略、MCP、hooks、skills 和 subagents 的落地方案，应以目标环境的官方文档和组织安全要求为准。

## Rebuild

```bash
cd claude-code-project-workflow
weasyprint index.html claude-code-project-workflow.pdf
```
