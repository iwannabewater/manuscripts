# Sources

作者：Winston
文档快照：2026-06-02
版本复核：截至 2026-06-09

## Method

本手册优先使用 mise 官方仓库、mise 官方文档站和 GitHub Releases API。为了核对迁移、PATH 与 CI 相关判断，补充使用 asdf、direnv 和 GitHub Actions 官方文档。正文中的建议分为三类：

- **官方事实**：命令行为、配置字段、文件优先级、实验性状态和 release 版本。
- **工程建议**：基于官方事实整理出的推荐顺序，例如交互 Shell 用 `mise activate`，脚本和 CI 优先用 `mise exec`、`mise run` 或 shims。
- **边界提醒**：不能从工具文档推出的结论，例如组织内部 secret 管理、合规要求和发布权限。

官网页面快照保存在 `sources/raw/`，从官方仓库复制的 Markdown 原稿保存在 `sources/official-docs/`。正文中的命令以官方仓库提交 `310e325909893b6af5fb1aa6a42653eaa7f35131` 为基础；稳定版本与安全状态已在 2026-06-09 通过 GitHub Releases 再次复核。

## Current Versions

- mise 最新稳定版：`v2026.6.1`，发布于 2026-06-07
  https://github.com/jdx/mise/releases/tag/v2026.6.1
- `jdx/mise-action` 最新 release：`v4.1.0`，发布于 2026-06-04
  https://github.com/jdx/mise-action/releases/tag/v4.1.0

## Documentation Drift

mise 官网 CI 页面仍展示 `jdx/mise-action@v3`，而 `jdx/mise-action` 仓库 README 已展示 `jdx/mise-action@v4`。本文以 action 仓库为准。

`tips-and-tricks.md` 仍出现通过 `touch mise.lock` 启用锁文件的旧式示例。当前专门的 lockfile 文档提供 `mise lock`，本文采用 `mise lock`。

## Primary Sources: mise

- GitHub repository: https://github.com/jdx/mise
- Latest release API: https://api.github.com/repos/jdx/mise/releases/latest
- Official documentation: https://mise.jdx.dev/
- Getting Started: https://mise.jdx.dev/getting-started.html
- Installing mise: https://mise.jdx.dev/installing-mise.html
- Walkthrough: https://mise.jdx.dev/walkthrough.html
- About: https://mise.jdx.dev/about.html
- Configuration: https://mise.jdx.dev/configuration.html
- Configuration Environments: https://mise.jdx.dev/configuration/environments.html
- Dev Tools: https://mise.jdx.dev/dev-tools/
- Backends: https://mise.jdx.dev/dev-tools/backends/
- Registry: https://mise.jdx.dev/registry.html
- `mise.lock`: https://mise.jdx.dev/dev-tools/mise-lock.html
- Shims: https://mise.jdx.dev/dev-tools/shims.html
- Environments: https://mise.jdx.dev/environments/
- Secrets: https://mise.jdx.dev/environments/secrets/
- Tasks: https://mise.jdx.dev/tasks/
- TOML Tasks: https://mise.jdx.dev/tasks/toml-tasks.html
- Running Tasks: https://mise.jdx.dev/tasks/running-tasks.html
- Task Configuration: https://mise.jdx.dev/tasks/task-configuration.html
- Continuous Integration: https://mise.jdx.dev/continuous-integration.html
- Hooks: https://mise.jdx.dev/hooks.html
- Trust CLI: https://mise.jdx.dev/cli/trust.html
- Paranoid mode: https://mise.jdx.dev/paranoid.html
- Tips & Tricks: https://mise.jdx.dev/tips-and-tricks.html
- Troubleshooting: https://mise.jdx.dev/troubleshooting.html
- Comparison to asdf: https://mise.jdx.dev/dev-tools/comparison-to-asdf.html
- Security policy: https://github.com/jdx/mise/blob/main/SECURITY.md

## Primary Sources: CI and Cross-checks

- `jdx/mise-action`: https://github.com/jdx/mise-action
- `jdx/mise-action` latest release API: https://api.github.com/repos/jdx/mise-action/releases/latest
- asdf Introduction: https://asdf-vm.com/guide/introduction.html
- asdf Getting Started: https://asdf-vm.com/guide/getting-started.html
- direnv Shell Hook Setup: https://direnv.net/docs/hook.html
- GitHub Actions dependency caching: https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching
- GitHub Actions security: https://docs.github.com/en/actions/how-tos/security-for-github-actions

## Boundaries

本文不是 mise 官方文档的替代品，也不承诺覆盖每个后端、插件和实验性配置。正式接入前，应复核目标操作系统、Shell、CI 平台、网络环境、组织 secret 管理规则和供应链策略。

`hooks`、monorepo root、SOPS 和 direct age encryption 在官方文档中带有实验性标记。本文会解释它们的用途，但不把它们放进默认配置。
