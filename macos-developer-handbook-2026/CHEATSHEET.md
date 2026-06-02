# macOS Developer Workstation Cheatsheet

## 1. 新机 60 分钟

| 时间 | 动作 | 验收 |
|---|---|---|
| 0 - 10 分钟 | 系统更新、登录账户、开启 FileVault | `系统设置 > 通用 > 软件更新` 无待处理更新 |
| 10 - 20 分钟 | 连接 Time Machine，确认恢复密钥保存位置 | 备份菜单能看到最近备份时间 |
| 20 - 30 分钟 | 安装 Command Line Tools 与 Homebrew | `xcode-select -p`、`brew --version` |
| 30 - 40 分钟 | 应用基础 Brewfile | `brew bundle check --file=./Brewfile` |
| 40 - 50 分钟 | 配置 Git、GitHub CLI、zsh、mise、uv | `gh auth status`、`mise doctor`、`uv --version` |
| 50 - 60 分钟 | 按需安装 Ghostty、OrbStack，完成冒烟测试 | `docker run --rm hello-world` |

```bash
xcode-select --install

# Homebrew 安装完成后，根据安装器提示执行 shellenv。
eval "$(/opt/homebrew/bin/brew shellenv)"

brew bundle check --file=./Brewfile || brew bundle install --file=./Brewfile
gh auth login
```

## 2. 键位图例

| 符号 | 名称 | 常见语义 |
|---|---|---|
| `⌘` | Command | 应用级主修饰键 |
| `⌥` | Option / Alt | 替代动作、按词移动、显示细粒度选项 |
| `⌃` | Control | 系统动作、终端动作、桌面切换 |
| `⇧` | Shift | 反向、范围选择、组合动作 |
| `fn` / `Globe` | Function / Globe | 功能键、输入源和系统动作 |

## 3. 每天都值得记住的快捷键

| 快捷键 | 动作 |
|---|---|
| `⌘ Space` | Spotlight 搜索 |
| `⌘ Tab` | 切换应用 |
| ``⌘ ` `` | 切换当前应用的窗口 |
| `⌘ W` | 关闭窗口或标签 |
| `⌘ Q` | 退出应用 |
| `⌘ ,` | 打开当前应用设置 |
| `⌥ ⌘ Esc` | 强制退出应用 |
| `⌃ ⌘ Q` | 锁定屏幕 |
| `Space` | Finder 中 Quick Look 预览 |
| `⇧ ⌘ 3` | 截取全屏 |
| `⇧ ⌘ 4` | 截取选区 |
| `⇧ ⌘ 5` | 截图与录屏面板 |
| `⌃ ↑` | Mission Control |
| `⌃ ↓` | 当前应用的所有窗口 |

## 4. Finder

| 快捷键 | 动作 |
|---|---|
| `⇧ ⌘ G` | 前往文件夹 |
| `⇧ ⌘ H` | 打开用户目录 |
| `⌥ ⌘ L` | 打开下载目录 |
| `⇧ ⌘ U` | 打开实用工具目录 |
| `⇧ ⌘ N` | 新建文件夹 |
| `⌘ I` | 显示简介 |
| `⌘ Delete` | 移到废纸篓 |
| `⌥ ⌘ V` | 将剪贴板中的文件移动到当前位置 |
| `⌥ ⌘ P` | 显示或隐藏路径栏 |
| `⌘ 1 / 2 / 3 / 4` | 图标、列表、分栏、画廊视图 |
| `⌘ ↑` | 上级目录 |
| `⌘ ↓` | 打开所选项目 |
| `⌘ [` / `⌘ ]` | 后退 / 前进 |

## 5. 文本编辑

| 快捷键 | 动作 |
|---|---|
| `⌥ ←` / `⌥ →` | 按词移动 |
| `⌘ ←` / `⌘ →` | 行首 / 行尾 |
| `⌘ ↑` / `⌘ ↓` | 文首 / 文末 |
| `⌥ Delete` | 删除左侧一个词 |
| `fn Delete` | 向右删除 |
| `⇧` 加移动键 | 扩展选择范围 |
| `⌘ Z` | 撤销 |
| `⇧ ⌘ Z` | 重做 |

## 6. Homebrew 与 Brewfile

```bash
# 日常查询
brew search <name>
brew info <name>
brew list
brew outdated

# 应用契约
brew bundle check --file=./Brewfile
brew bundle install --file=./Brewfile

# 维护
brew update
brew upgrade
brew cleanup
brew doctor

# 导出现状，必须审阅 diff
brew bundle dump --global --force --describe

# 危险：只看差异，不要直接加 --force
brew bundle cleanup --file=./Brewfile
```

Apple Silicon 默认 Homebrew 前缀为 `/opt/homebrew`，Intel Mac 默认前缀为 `/usr/local`。

## 7. 推荐基础 Brewfile

```ruby
brew "bat"
brew "eza"
brew "fd"
brew "fzf"
brew "gh"
brew "git-delta"
brew "jq"
brew "mise"
brew "mole"
brew "ripgrep"
brew "uv"
brew "zoxide"

cask "ghostty"
# cask "orbstack" # 有容器或 Linux 需求时启用
# cask "raycast"  # 原生 Spotlight 不够用时启用
```

## 8. zsh 最小配置

```zsh
# ~/.zshrc
if [[ -x /opt/homebrew/bin/brew ]]; then
  eval "$(/opt/homebrew/bin/brew shellenv)"
fi

eval "$(mise activate zsh)"
eval "$(zoxide init zsh)"

alias ll='eza -lah --group-directories-first'
alias cat='bat --paging=never'
```

## 9. Git 与 GitHub CLI

```bash
git config --global --edit
git config --global init.defaultBranch main
git config --global pull.ff only
git config --global fetch.prune true

gh auth login
gh auth status
ssh -T git@github.com
```

## 10. mise

```bash
# 交互 shell 已在 ~/.zshrc 中激活
mise doctor
mise ls
mise current

# 全局默认，只保留少量通用项
mise use --global node@lts

# 项目内写入 mise.toml
mise use node@lts
mise use python@3.12
mise install
mise run test

# 团队可复现
mise settings lockfile=true
mise lock
git add mise.toml mise.lock
```

拉取陌生项目后，先审阅 `mise.toml`、任务和 hooks，再执行信任操作。

## 11. uv

```bash
brew install uv

uv init hello-world
cd hello-world
uv add requests
uv run python -c 'import requests; print(requests.__version__)'

uv lock
uv sync
uv tool install ruff
```

Python 项目依赖写入 `pyproject.toml` 与 `uv.lock`。不要把项目依赖堆到全局 Python。

## 12. OrbStack

```bash
brew install orbstack

docker context show
docker run --rm hello-world
docker compose up -d
docker compose ps
docker compose down

orb create ubuntu devbox
orb -m devbox uname -a
orb logs devbox
```

| 场景 | 做法 |
|---|---|
| 容器持久数据 | 优先 volume；需要从 Mac 观察时使用 `~/OrbStack/docker` |
| Apple Silicon 运行 x86 镜像 | 显式使用 `--platform linux/amd64`，只在确有需要时启用 |
| Linux 中访问 Mac 文件 | 使用 `/mnt/mac` |
| Mac 中访问 Linux 文件 | 使用 `~/OrbStack` 或 Finder 集成 |
| 商业使用 | 先阅读官方 licensing 页面 |
| Docker TCP | 不开放未认证的 `0.0.0.0:2375` |

## 13. Mole

```bash
brew install mole

# 默认从只读动作开始
mo status
mo analyze

# 删除动作先预演
mo clean --dry-run
mo uninstall --dry-run
mo purge --dry-run

# 回看日志
mo history
mo history --json
```

不要把深度清理写进定时任务。删除前先备份，阅读列表，确认 VPN、开发缓存、模拟器和挂载卷等工作资产不会受影响。

## 14. 按痛点安装

| 痛点 | 先试原生 | 第三方候选 |
|---|---|---|
| 启动、动作、Quicklinks、Snippets | Spotlight | Raycast |
| 窗口排列 | macOS 原生平铺 | Loop / Rectangle / AeroSpace 三选一 |
| 菜单栏拥挤 | 系统设置精简 | Ice |
| 剪贴板历史 | 无 | Raycast Clipboard 或 Maccy 二选一 |
| 系统状态 | 活动监视器 | Stats |
| 媒体播放 | QuickTime Player | IINA |
| 压缩解压 | Finder | Keka |
| 跨平台局域网传输 | AirDrop | LocalSend |
| 外接显示器 | 系统显示器设置 | BetterDisplay |
| GUI 卸载 | 手工移除 | Pearcleaner |
| GUI 安装 Homebrew cask | Brewfile | Applite |

## 15. 日常 SOP

### 每天

```bash
git status --short --branch
mise current
docker compose ps
```

### 每周

```bash
brew update
brew outdated
brew bundle check --file=./Brewfile
mo status
```

### 每月

```bash
brew upgrade
brew cleanup
brew doctor
mo analyze
```

同时检查 Time Machine 最近备份、权限列表、登录项、磁盘余量和不再使用的菜单栏模块。

### 大版本升级前

1. 完成一次 Time Machine 备份。
2. 导出并审阅 Brewfile。
3. 提交 dotfiles 与项目变更。
4. 记录关键应用许可、VPN、证书和组织策略。
5. 暂停高风险清理与批量修改。

## 16. 排障顺序

| 现象 | 第一检查 | 第二检查 |
|---|---|---|
| `brew` 找不到 | `which brew` | `eval "$(/opt/homebrew/bin/brew shellenv)"` |
| 项目工具版本错 | `mise current` | 审阅 `mise.toml` 与 `mise.lock` |
| Python 包找不到 | `uv run python -V` | `uv sync` |
| Docker 命令异常 | `docker context show` | 打开 OrbStack，检查容器与 volume |
| 菜单栏监控不显示 | 模块是否开启 | `系统设置 > 菜单栏` 权限 |
| 快捷键失效 | 系统快捷键冲突 | 启动器、输入法和窗口工具冲突 |
| 磁盘空间紧张 | `mo analyze` | 审阅大目录，再决定是否删除 |
| shell 变慢 | `zsh -xlic exit` | 暂时移除插件，保留最小配置 |
