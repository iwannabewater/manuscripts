# Sources and Boundaries

## Method

本手册在 `2026-06-02` 完成资料收集与核验。事实优先来自 Apple 支持文档和各项目官方文档；Homebrew API 用于确认 Brewfile 标识；Linux.do 公开讨论用于发现候选工具、使用场景和反例。社区内容不作为安全边界或高风险命令的唯一依据。

逐条链接保存在 `data/source-map.tsv`。以下为正文使用频率最高的来源。

## Apple

- [Find out which macOS your Mac is using](https://support.apple.com/en-us/109033)：系统版本口径。Apple 在 `2026-05-11` 发布的页面中列出 `macOS Tahoe 26.5`。
- [Mac keyboard shortcuts](https://support.apple.com/en-us/102650)：修饰键、应用切换、Finder、截图、锁屏和文本编辑快捷键。
- [Take actions and shortcuts in Spotlight](https://support.apple.com/guide/mac-help/take-actions-and-shortcuts-in-spotlight-mchl4953dfeb/mac)：Spotlight 能力。
- [Trackpad gestures](https://support.apple.com/guide/mac-help/mh35869/mac)、[three finger drag](https://support.apple.com/en-us/102482) 与 [Hot Corners](https://support.apple.com/guide/mac-help/use-hot-corners-mchlp3000/mac)：触控板和桌面动作。
- [Window tiling settings](https://support.apple.com/guide/mac-help/change-window-tiling-settings-mchl118087b0/mac)：原生窗口平铺设置。
- [FileVault](https://support.apple.com/guide/mac-help/mh11785/mac) 与 [Time Machine](https://support.apple.com/en-us/102307)：磁盘加密和备份。
- [Privacy & Security](https://support.apple.com/guide/mac-help/mchl211c911f/mac)、[Accessibility](https://support.apple.com/guide/mac-help/mh43185/mac) 与 [screen recording](https://support.apple.com/guide/mac-help/mchld6aa7d23/mac)：权限治理。

## Workstation Contract

- [Homebrew Installation](https://docs.brew.sh/Installation)：默认前缀、Command Line Tools 和支持系统。
- [Brew Bundle and Brewfile](https://docs.brew.sh/Brew-Bundle-and-Brewfile)：`brew bundle check`、`dump`、`cleanup` 与版本控制工作流。
- [Homebrew Analytics](https://docs.brew.sh/Analytics)：匿名统计说明和关闭命令。
- [Ghostty binary install](https://ghostty.org/docs/install/binary)、[configuration](https://ghostty.org/docs/config) 与 [shell integration](https://ghostty.org/docs/features/shell-integration)：安装、零配置理念和配置文件路径。
- [mise getting started](https://mise.jdx.dev/getting-started.html)、[configuration](https://mise.jdx.dev/configuration.html)、[tasks](https://mise.jdx.dev/tasks/) 与 [lockfile](https://mise.jdx.dev/dev-tools/mise-lock.html)：运行时、任务与锁文件。
- [uv installation](https://docs.astral.sh/uv/getting-started/installation/)、[projects](https://docs.astral.sh/uv/guides/projects/) 与 [tools](https://docs.astral.sh/uv/guides/tools/)：Python 项目工作流。
- [GitHub CLI auth login](https://cli.github.com/manual/gh_auth_login)：GitHub CLI 登录。
- [chezmoi install](https://www.chezmoi.io/install/) 与 [quick start](https://www.chezmoi.io/quick-start/)：dotfiles 管理。

## Containers and Maintenance

- [OrbStack quick start](https://docs.orbstack.dev/quick-start)、[Docker](https://docs.orbstack.dev/docker/)、[Linux machines](https://docs.orbstack.dev/machines/)、[Kubernetes](https://docs.orbstack.dev/kubernetes/)、[efficiency](https://docs.orbstack.dev/efficiency) 与 [licensing](https://docs.orbstack.dev/licensing)：容器、Linux、资源行为、安全和商业许可。
- [Mole README](https://github.com/tw93/mole/blob/main/README.md) 与 [security policy](https://github.com/tw93/mole/blob/main/SECURITY.md)：清理命令、`--dry-run`、操作日志和保护边界。

## Optional Tools

- [Raycast window management](https://manual.raycast.com/window-management)、[clipboard history](https://manual.raycast.com/clipboard-history)、[Quicklinks](https://manual.raycast.com/quicklinks)、[Snippets](https://manual.raycast.com/snippets) 与 [security and privacy](https://manual.raycast.com/security-and-privacy)。
- [Ice](https://github.com/jordanbaird/Ice)、[Stats](https://github.com/exelban/stats)、[IINA](https://github.com/iina/iina)、[Keka](https://www.keka.io/en/)、[LocalSend](https://github.com/localsend/localsend)、[Maccy](https://github.com/p0deje/Maccy)。
- [BetterDisplay](https://github.com/waydabber/BetterDisplay)、[Rectangle](https://github.com/rxhanson/Rectangle)、[Loop](https://github.com/MrKai77/Loop)、[AeroSpace](https://github.com/nikitabobko/AeroSpace)。
- [Pearcleaner](https://github.com/alienator88/Pearcleaner)、[Applite](https://github.com/milanvarady/Applite)、[mas](https://github.com/mas-cli/mas)。

## Linux.do Community Reading

- [macOS 软件与配置讨论](https://linux.do/t/topic/2293064)
- [沉淀数月使用，我推荐的 Mac 软件](https://linux.do/t/topic/878250)
- [Mac 软件推荐分享](https://linux.do/t/topic/3528)
- [Mac 效率与软件讨论](https://linux.do/t/topic/1381877)
- [开发环境管理迁移讨论](https://linux.do/t/topic/1470285)
- [新机一键安装讨论](https://linux.do/t/topic/1407819)
- [第一台 MacBook 软件讨论](https://linux.do/t/topic/2193673)
- [Mac App 推荐讨论](https://linux.do/t/topic/244759)

## Boundaries

- 本手册不是 Apple、Homebrew 或任何第三方项目的官方出版物。
- 推荐项不等于永久安装项。团队许可、组织 MDM、合规要求和实际工作负载优先。
- 软件界面、价格、许可和系统菜单会变化。安装前应再次阅读对应官方页面。
- 文中示例不会替代备份、权限复核和代码审阅。
