# Research Notes

作者：Winston
资料口径：截至 2026-06-02

## 1. 研究目标

这份教程要回答一个工程问题：开发者如何用 mise 统一管理项目工具版本、环境变量和常用任务，并让本地开发、脚本与 CI 使用同一份约定。

文章不追求罗列所有 CLI 参数。目标是让读者读完后可以完成三件事：

1. 在个人电脑上正确安装和激活 mise。
2. 为一个真实项目写出可提交的 `mise.toml`、`mise.lock` 和任务定义。
3. 在团队与 CI 中使用同一套工具链，同时知道哪些安全边界不能省略。

## 2. 一手资料

本次调研归档了 25 份 mise 官方仓库 Markdown 文档、25 份对应官网页面快照、GitHub 仓库元数据、最新 release API、`jdx/mise-action` README 与最新 release API。交叉验证来源包括 asdf 官方文档、direnv 官方文档和 GitHub Actions 官方文档。

mise 官方仓库浅克隆提交：

```text
310e325909893b6af5fb1aa6a42653eaa7f35131
2026-06-01T11:58:59+10:00
fix(spm): track artifact bundle options in lock identity (#10160)
```

截至 2026-06-02，GitHub Releases API 返回的最新稳定版：

```text
v2026.5.18
published_at: 2026-05-31T21:43:15Z
```

截至 2026-06-02，`jdx/mise-action` 最新 release：

```text
v4.0.1
published_at: 2026-03-22T16:06:57Z
```

## 3. 核心判断

### mise 的价值不止是切换 Node 或 Python

官方 README 把 mise 定义为一个统一 CLI：项目工具、环境变量和任务放在同一个 `mise.toml` 中。教程必须围绕这三个能力展开，不能写成 `asdf` 替代品的命令翻译表。

### `mise use` 是个人上手的核心命令

官方 Walkthrough 强调：`mise install` 只安装工具，不会让工具自动进入当前项目配置；`mise use` 同时安装并写入配置。新手路径应优先教 `mise use`，团队成员拉取项目后再用 `mise install`。

### 交互 Shell、脚本与 CI 应采用不同接入方式

官方 Shims 文档区分三种方式：

- 交互 Shell：优先 `mise activate`。
- 脚本和 CI：优先 `mise exec`、`mise run` 或 shims。
- 单项目、偏显式工作流：可以完全不改 Shell rc 文件，只用 `mise exec` 和 `mise run`。

把 `mise activate` 直接放进 CI 或非交互脚本会造成 PATH 未及时刷新的问题。教程必须把这一点放到前面。

### 锁文件是团队落地的关键

`mise.lock` 不会自动创建，需要执行 `mise lock`。一旦存在，`mise install`、`mise use` 和 `mise upgrade` 会维护它。锁文件可以保存精确版本，并在后端支持时记录 checksum、size、URL 与 provenance 信息。团队项目应提交 `mise.lock`；本地覆盖文件 `mise.local.toml` 和 `mise.local.lock` 应加入 `.gitignore`。

### 后端选择会影响安全与复现能力

mise Registry 文档明确给出新 registry entry 的优先级：`aqua` 最优先，随后是 `github` 和 `gitlab`。新 `vfox` 与 `asdf` registry entry 因供应链风险不再接受。教程应建议读者优先使用 registry shorthand，必要时显式指定 `aqua:` 或 `github:`，对 `asdf:` 插件保持审慎。

### 环境变量管理需要区分公开配置和秘密

`mise.toml` 通常进入版本控制，不应写入 secret。公开环境变量放 `[env]`；本机 secret 可放入 `mise.local.toml`、预先存在的系统环境变量或专门 secret 管理器。`redact = true` 只能降低日志泄漏风险，不能替代 secret 管理。

### 任务系统值得作为主线能力讲解

mise tasks 支持 TOML 任务和文件任务，默认最多并发执行 4 个 job。`depends`、`sources`、`outputs`、`mise watch`、参数与补全让任务系统不只是 npm scripts 的另一种写法。教程需要给出一个真实的 `ci` 任务图。

## 4. 文档漂移与冲突处理

### mise-action 主版本漂移

mise 官网 `continuous-integration.md` 仍展示：

```yaml
- uses: jdx/mise-action@v3
```

`jdx/mise-action` 仓库 README 已展示：

```yaml
- uses: jdx/mise-action@v4
```

GitHub release API 返回 `v4.0.1`。本文以 action 仓库为准，示例使用 `jdx/mise-action@v4`，并在 `sources.md` 记录漂移。

### 旧 Tips 页面中的锁文件说明

`tips-and-tricks.md` 仍出现 `touch mise.lock` 的旧式启用说明。当前 `dev-tools/mise-lock.md` 已提供专门的 `mise lock` 命令与设置说明。本文采用 `mise lock` 作为默认生成路径。

### direnv 兼容性

direnv 官方文档说明它通过 Shell hook 管理环境。mise 官方文档明确建议不要把 direnv 与 mise 组合用于同一套 PATH 管理。本文不给出 `use mise` 方案作为默认配置，仅保留迁移提示。

## 5. 冻结提纲

1. 先说结论：mise 把工具、环境和任务放回项目。
2. 15 分钟上手：安装、激活、`mise use`、`mise run`、`mise doctor`。
3. 心智模型：配置发现、版本解析、后端选择、安装检查、环境装配。
4. 工具管理：`use`、`install`、`exec`、后端、registry、升级。
5. 配置组织：层级、环境配置、`.tool-versions`、idiomatic version files。
6. 环境变量：`[env]`、`_.file`、`_.path`、required、redact、secret 边界。
7. 任务：TOML 任务、文件任务、依赖图、sources/outputs、watch。
8. 团队与 CI：`mise.lock`、GitHub Actions、缓存、安全设置。
9. 最佳实践：个人、团队、单仓、多语言仓库的推荐做法。
10. 迁移与排障：asdf、direnv、PATH、缓存、诊断命令。
11. Cheatsheet：命令、配置片段和检查清单。
