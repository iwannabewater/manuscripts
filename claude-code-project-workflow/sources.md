# Sources

作者：Winston
资料口径：截至 2026-05-04

## Method

本手册优先采用 Claude Code 官方文档与 Anthropic 工程博客。正文中的方法论判断以官方能力模型为边界：Claude Code 能读取代码库、编辑文件、运行命令、使用工具并验证结果；项目工作流围绕这个 agentic loop 设计，而不是围绕单轮对话技巧设计。

由于 Claude Code 更新较快，正式落地前应复核目标版本、组织策略、权限设置、MCP 服务器来源、hooks 行为、skills 结构、subagents 定义和团队安全要求。本文不讨论通用代码规范、不评价具体模型能力，也不把云端托管产品、IDE 插件体验或组织采购策略作为主体。

## Primary Sources

- Claude Code overview: https://code.claude.com/docs/en/overview
- Quickstart: https://code.claude.com/docs/en/quickstart
- How Claude Code works: https://code.claude.com/docs/en/how-claude-code-works
- Common workflows: https://code.claude.com/docs/en/common-workflows
- Best practices: https://code.claude.com/docs/en/best-practices
- Store instructions and memories: https://code.claude.com/docs/en/memory
- Permission modes: https://code.claude.com/docs/en/permission-modes
- Security: https://code.claude.com/docs/en/security
- Model Context Protocol: https://code.claude.com/docs/en/mcp
- Hooks reference: https://code.claude.com/docs/en/hooks
- Custom subagents: https://code.claude.com/docs/en/sub-agents
- Skills: https://code.claude.com/docs/en/skills
- Anthropic Engineering Blog, Claude Code best practices: https://www.anthropic.com/engineering/claude-code-best-practices
