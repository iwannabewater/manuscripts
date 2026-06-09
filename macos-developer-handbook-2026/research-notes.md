# macOS Developer Handbook 2026 Research Notes

资料收集日期：`2026-06-02`。

## Research Question

目标不是制作一张不断增长的软件清单，而是回答四个问题：

1. 一台新 Mac 如何在一小时内达到可工作的状态？
2. 哪些能力应优先使用 macOS 原生功能，哪些痛点值得引入第三方工具？
3. 开发工具如何从手工安装转为可复现契约？
4. 清理、权限、备份、升级和恢复如何形成长期 SOP？

## Evidence Order

1. Apple 支持文档：系统版本、快捷键、窗口、权限、FileVault、Time Machine。
2. 项目官方文档：安装方式、配置路径、行为边界、许可和安全提示。
3. Homebrew API：确认正文 Brewfile 中使用的 formula 与 cask 标识存在。
4. Linux.do 社区讨论：发现真实使用场景、候选工具和踩坑案例。

社区讨论只作为候选发现与痛点证据，不作为高风险命令、下载地址或系统修改脚本的权威来源。

## Community Signals

本轮阅读覆盖八个公开讨论：

| 讨论 | 主要信号 | 文中处理 |
|---|---|---|
| `linux.do/t/topic/2293064` | OrbStack、Mole、Raycast、Loop、Keka、IINA | 纳入候选矩阵，按痛点分层 |
| `linux.do/t/topic/878250` | Raycast、OrbStack、IINA、Keka、LocalSend、uv | 与官方文档交叉验证后纳入 |
| `linux.do/t/topic/3528` | 长期软件分享，剪贴板需求突出 | 不引用第三方分发链接 |
| `linux.do/t/topic/1381877` | Mole、Pearcleaner、Dock 修改、清理误伤反馈 | 保留 `--dry-run` 与备份前置，不默认执行深度清理 |
| `linux.do/t/topic/1470285` | JDK、Python、Node 分散管理，迁移到 mise 与 uv | 转化为工具职责边界 |
| `linux.do/t/topic/1407819` | 新机安装时容易遗漏 Node、Docker、常用软件 | 转化为 Brewfile 和验收清单 |
| `linux.do/t/topic/2193673` | Keka、Raycast、AlDente 等常见候选 | 电池工具降为条件项，原生优化充电优先 |
| `linux.do/t/topic/244759` | 商业清理工具、代理、效率软件 | 不设为默认基线 |

## Decisions

### Default Baseline

- macOS 原生：Spotlight、原生窗口平铺、Finder、Quick Look、FileVault、Time Machine。
- 包管理：Homebrew 与受版本控制的 Brewfile。
- 开发工具：GitHub CLI、`ripgrep`、`fd`、`fzf`、`jq`、`bat`、`eza`、`zoxide`、`mise`、`uv`。
- 终端：Ghostty 作为推荐项，但保留 Terminal.app 作为零安装兜底。
- 容器：有容器或 Linux 需求时安装 OrbStack；商业使用先确认许可。
- 维护：Mole 先使用只读能力，任何删除操作先 `--dry-run`。

### Install Only When the Pain Exists

- Raycast：当原生 Spotlight 不足以覆盖动作、Quicklinks、Snippets 或窗口命令时安装。
- Loop、Rectangle、AeroSpace：只选一个窗口增强工具。
- Maccy：只在没有使用 Raycast 剪贴板历史时安装。
- Ice：菜单栏拥挤时安装。
- Stats：需要持续观察资源时安装，并关闭不需要的 Sensors 和 Bluetooth 模块。
- IINA、Keka、LocalSend、BetterDisplay：按媒体、压缩、跨平台传输、外接显示器场景安装。
- chezmoi、mas、Applite、Pearcleaner：按 dotfiles、App Store、图形化安装、图形化卸载需求安装。

### Deliberately Excluded from the Default

- 非官方软件分发、旧版安装包、破解或激活脚本。
- 未审阅的一键安装脚本和大段 `defaults write` 集合。
- 默认开启 Docker 未认证 TCP 端口。
- 定时运行深度清理工具。
- 同时安装多个剪贴板管理器、窗口管理器和启动器。
- 把代理、VPN、电池控制或商业清理工具视为所有人的必装项。

## Current Version Context

Apple 在 `2026-05-11` 更新的版本页中列出 `macOS Tahoe 26.5` 为 Tahoe 最新版本。本手册的系统截图路径和快捷键口径以 `2026-06-02` 可公开访问资料为准。旧系统上的菜单名称可能不同。
