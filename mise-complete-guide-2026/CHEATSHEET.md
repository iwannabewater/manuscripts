# mise Cheatsheet

文档快照：2026-06-02
版本复核：截至 2026-06-09，mise `v2026.6.1`，mise-action `v4.1.0`

## 1. 安装

```bash
# macOS
brew install mise

# Linux/macOS quick install
curl https://mise.run | sh

# Windows
scoop install mise

# Verify
mise --version
# 或 ~/.local/bin/mise --version
```

## 2. Shell 激活

```bash
# bash
echo 'eval "$(mise activate bash)"' >> ~/.bashrc

# zsh
echo 'eval "$(mise activate zsh)"' >> ~/.zshrc

# fish
echo 'mise activate fish | source' >> ~/.config/fish/config.fish

# Verify setup
mise doctor
```

交互 Shell 优先 `mise activate`。CI、IDE 和脚本优先 `mise exec`、`mise run` 或 shims。

## 3. 最常用命令

| 目标 | 命令 |
|---|---|
| 为项目安装并启用 Node.js | `mise use node@26` |
| 设置全局默认 Node.js | `mise use --global node@26` |
| 安装项目声明的所有工具 | `mise install` |
| 临时运行特定 Python | `mise exec python@3.14 -- python` |
| 在项目环境中执行命令 | `mise exec -- npm test` |
| 运行任务 | `mise run test` |
| 查看当前工具 | `mise ls --current` |
| 查看工具详情 | `mise tool ripgrep` |
| 查找真实可执行文件 | `mise which node` |
| 查看可用远端版本 | `mise ls-remote node` |
| 查看可升级工具 | `mise outdated` |
| 范围内升级 | `mise upgrade` |
| 提升主版本范围 | `mise upgrade --bump node` |
| 查看加载的配置 | `mise config` |
| 诊断安装 | `mise doctor` |
| 清除版本缓存 | `mise cache clear` |

## 4. 新项目最小配置

```toml
# mise.toml
[tools]
node = "26"
python = "3.14"

[env]
NODE_ENV = "development"

[tasks.test]
run = "npm test"
```

```bash
mise trust
mise install
mise run test
```

## 5. `use`、`install`、`exec`、`run`

| 命令 | 安装工具 | 写 `mise.toml` | 加载项目环境 |
|---|---|---|---|
| `mise use node@26` | 是 | 是 | 是 |
| `mise install` | 是 | 否 | 安装阶段 |
| `mise exec -- <cmd>` | 按需 | 否 | 是 |
| `mise run <task>` | 按需 | 否 | 是 |

新增工具用 `mise use`。clone 项目后用 `mise install`。脚本和 CI 用 `mise exec` 或 `mise run`。

## 6. 配置层级

```text
~/.config/mise/config.toml      # 用户全局
~/work/mise.toml                # 工作目录共享
~/work/project/mise.toml        # 项目共享
~/work/project/mise.local.toml  # 项目本地，不提交
```

查看真实加载顺序：

```bash
mise config
mise config ls
```

环境专用配置：

```text
mise.toml
mise.test.toml
mise.local.toml
mise.test.local.toml
```

```bash
MISE_ENV=test mise run test
mise -E test run test
```

## 7. 工具版本

```toml
[tools]
node = "26"              # 允许 26.x
python = "3.14"          # 允许 3.14.x
ruby = "latest"          # 每次解析最新可用版本
go = "prefix:1.25"       # 允许 1.25.x
```

常用后端显式写法：

```bash
mise use github:BurntSushi/ripgrep
mise use aqua:aws/aws-cli
mise use npm:prettier
mise use pipx:black
mise use cargo:starship
```

默认使用 Registry shorthand；需要显式选择后端时，使用 `aqua:`、`github:` 或 `gitlab:`。对 `asdf:` 插件保持审慎。

## 8. 环境变量

```toml
[env]
NODE_ENV = "development"
_.path = "./node_modules/.bin"
_.file = ".env"
```

多个文件：

```toml
[env]
_.file = [
  ".env",
  ".env.local",
  { path = ".secrets.yaml", redact = true },
]
```

Required variables：

```toml
[env]
DATABASE_URL = { required = "Set DATABASE_URL in mise.local.toml" }
API_KEY = { required = "Get API_KEY from the team secret manager" }
```

Redaction：

```toml
redactions = ["SECRET_*", "*_TOKEN", "PASSWORD"]

[env]
API_TOKEN = { value = "token-value", redact = true }
```

CLI：

```bash
mise set NODE_ENV=development
mise set
mise env
mise env --redacted
mise unset NODE_ENV
```

## 9. Secret 边界

共享 `mise.toml` 不写真实 secret。

```text
推荐来源：
1. mise.local.toml
2. 系统环境变量
3. 组织 secret manager
4. CI 平台 secret
```

`.gitignore`：

```text
mise.local.toml
mise.local.lock
mise.*.local.toml
mise.*.local.lock
.env
.env.local
```

## 10. 任务

简单任务：

```toml
[tasks]
build = "npm run build"
test = "npm test"
lint = "npm run lint"
```

详细任务：

```toml
[tasks.test]
description = "Run tests"
run = [
  "npm test",
  "uv run pytest",
]
```

依赖并发：

```toml
[tasks.ci]
description = "Run CI checks"
depends = ["lint", "test", "build"]
```

输入输出缓存：

```toml
[tasks.build]
run = "npm run build"
sources = ["src/**/*.ts", "!src/**/*.test.ts", "tsconfig.json"]
outputs = ["dist/**/*.js"]
```

监视文件：

```bash
mise use --global watchexec@latest
mise watch build
```

危险任务确认：

```toml
[tasks.deploy]
confirm = { message = "Deploy production?", default = "no" }
run = "./scripts/deploy.sh"
```

注意：`confirm` 不会阻止 `depends` 在提示前执行。

## 11. `mise.lock`

启用：

```bash
mise settings lockfile=true
mise lock
mise install
git add mise.toml mise.lock
```

项目配置：

```toml
[settings]
lockfile = true
```

Strict mode：

```bash
MISE_LOCKED=1 mise install
```

多平台：

```bash
mise lock --platform linux-x64,macos-arm64
```

团队提交：

```text
提交：mise.toml、mise.lock、mise.<env>.toml、mise.<env>.lock
忽略：mise.local.toml、mise.local.lock、mise.<env>.local.toml、mise.<env>.local.lock
```

## 12. GitHub Actions

截至 2026-06-09，`jdx/mise-action` 最新 release 是 `v4.1.0`：

```yaml
name: test
on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: jdx/mise-action@v4
      - run: mise run ci
```

`v4.1.0` 起，当前目录或父目录存在仓库级 `mise.lock` 时，mise-action 会自动执行 `mise install --locked`；动态传入 `mise_toml` 或 `tool_versions` 时不适用。

## 13. CI 和脚本

推荐：

```bash
mise install
mise exec -- npm test
mise run ci
```

Shims：

```bash
export PATH="$HOME/.local/share/mise/shims:$PATH"
```

不要在非交互脚本中依赖 prompt 刷新 PATH。

## 14. 安全设置

Trust：

```bash
mise trust
mise trust --show
mise untrust
```

Paranoid mode：

```bash
mise settings paranoid=1
MISE_PARANOID=1 mise install
```

最小发布时间：

```toml
[settings]
minimum_release_age = "7d"
```

Hooks 带实验性标记。默认优先显式任务：

```bash
mise run setup
```

## 15. asdf 迁移

```bash
# 保留现有 .tool-versions
mise install

# 需要时生成 mise 配置
mise config generate

# 启用 lockfile
mise settings lockfile=true
mise lock
```

mise 能读 `.tool-versions`，但不会直接复用 asdf 数据目录。

## 16. direnv 边界

direnv 和 mise 都会通过 Shell hook 管理环境。不要让两者同时管理同一套 PATH，尤其是 Python virtualenv 和运行时版本。

## 17. 排障

```bash
# 总体诊断
mise doctor
mise --version
mise config
mise ls --current

# PATH
which -a node
mise which node
mise ls node

# 缓存
mise cache clear
mise ls-remote node

# 调试日志
MISE_DEBUG=1 mise install
MISE_TRACE=1 mise install

# Prompt 性能
mise deactivate
MISE_TIMINGS=1 mise hook-env -s bash 2>&1 >/dev/null
```

## 18. 推荐项目模板

```toml
min_version = "2026.5.18"

[settings]
lockfile = true
minimum_release_age = "7d"

[tools]
node = "26"
python = "3.14"
uv = "latest"
ripgrep = "latest"

[env]
NODE_ENV = "development"
DATABASE_URL = { required = "Set DATABASE_URL in mise.local.toml" }
_.path = "./node_modules/.bin"

[tasks.setup]
run = [
  "npm install",
  "uv sync",
]

[tasks.lint]
run = [
  "npm run lint",
  "uv run ruff check .",
]

[tasks.test]
run = [
  "npm test",
  "uv run pytest",
]

[tasks.ci]
depends = ["lint", "test"]
```
