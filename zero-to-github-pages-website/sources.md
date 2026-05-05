# Sources

资料核验日期：2026-05-05  
写作目标：从 0 构建网站并部署到 GitHub Pages 的工程全流程  
来源原则：优先使用官方文档、工具维护者文档和规范性资料；避免二手教程作为事实依据。

## Primary Sources

| 来源 | URL | 正文用途 |
|---|---|---|
| GitHub Docs · Creating a GitHub Pages site | https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site | Pages 入口文件、静态文件发布、GitHub Actions 构建建议、服务端语言边界、发布延迟说明 |
| GitHub Docs · Using custom workflows with GitHub Pages | https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages | `configure-pages`、`upload-pages-artifact`、`deploy-pages`、Pages 部署权限与环境要求 |
| GitHub Docs · Configuring a publishing source | https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site | 分支发布与 GitHub Actions 发布源的区别 |
| GitHub Docs · REST API endpoints for GitHub Pages | https://docs.github.com/en/rest/pages/pages | `build_type=workflow`、Pages 创建与更新接口口径 |
| GitHub Docs · GitHub Pages limits | https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits | 1 GB、10 分钟、100 GB/月、10 builds/hour 等限制 |
| GitHub Docs · Securing GitHub Pages with HTTPS | https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https | HTTPS、敏感交易边界、混合内容排查 |
| GitHub Docs · Custom domains for GitHub Pages | https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages | 自定义域名、验证域名、防接管风险 |
| GitHub Docs · Managing remote repositories | https://docs.github.com/en/get-started/git-basics/managing-remote-repositories | `git remote add origin` 与远端 URL 管理 |
| GitHub Docs · Pushing commits to a remote repository | https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository | `git push origin main` 与 push protection 入口 |
| GitHub Docs · About push protection | https://docs.github.com/en/code-security/concepts/secret-security/about-push-protection | secret scanning push protection 的行为与边界 |
| GitHub CLI Manual · gh repo create | https://cli.github.com/manual/gh_repo_create | `gh repo create --source --remote --push` 参数说明 |
| Vite Docs · Getting Started | https://vite.dev/guide/ | Node 版本要求、脚手架命令、默认脚本与项目入口 |
| Vite Docs · Deploying a Static Site | https://vite.dev/guide/static-deploy.html | `dist` 产物、`base` 配置、GitHub Pages 工作流示例 |
| npm Docs · npm ci | https://docs.npmjs.com/cli/v11/commands/npm-ci/ | CI 干净安装、锁文件要求、不会改写 package 文件 |
| npm Docs · package.json | https://docs.npmjs.com/cli/v11/configuring-npm/package-json/ | `scripts` 字段、依赖声明和项目元数据 |
| MDN · HTML | https://developer.mozilla.org/en-US/docs/Web/HTML | HTML 作为网页结构与语义基础 |
| MDN · HTML: A good basis for accessibility | https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML | 语义 HTML、alt、label、键盘访问、源顺序 |
| web.dev · Web Vitals | https://web.dev/articles/vitals?hl=en | Core Web Vitals 指标、75 百分位口径、测量工具 |
| actions/checkout | https://github.com/actions/checkout | 当前 checkout action 主版本与说明 |
| actions/setup-node | https://github.com/actions/setup-node | 当前 setup-node action 主版本与 npm 缓存说明 |
| actions/configure-pages | https://github.com/actions/configure-pages | 当前 configure-pages action 主版本 |
| actions/upload-pages-artifact | https://github.com/actions/upload-pages-artifact | 当前 upload-pages-artifact action 主版本 |
| actions/deploy-pages | https://github.com/actions/deploy-pages | 当前 deploy-pages action 主版本 |

## Research Notes

- GitHub Pages 官方文档和 Vite 官方文档均建议：需要构建步骤的静态站点使用 GitHub Actions 发布构建产物。
- GitHub Pages 文档示例中的 action 主版本与 action 仓库最新主版本存在更新节奏差异；正文采用 2026-05-05 时 Vite 部署文档与 action 仓库核验到的主版本。通过 GitHub API 核验到的最新标签为：`actions/checkout` v6.0.2、`actions/setup-node` v6.4.0、`actions/configure-pages` v6.0.0、`actions/upload-pages-artifact` v5.0.0、`actions/deploy-pages` v5.0.0。
- GitHub Pages 限制、Actions 主版本、REST API 版本与 Vite Node 版本要求都可能随时间变化。生产使用前应再次核对官方文档。
- 本文没有使用社区教程作为事实来源；社区经验只作为常见故障形态的背景判断，未进入引用表。

## Boundaries

- 本文覆盖静态网站与需要前端构建的静态站，不覆盖 SSR、服务端 API、数据库、登录、支付和企业合规发布。
- 本文中的命令以 Linux/macOS shell 为主，Windows 用户应使用 PowerShell 等价命令或 Git Bash。
- 文中的示例仓库名、域名和路径均为示例，实际使用时需要替换为自己的 GitHub 用户名和仓库名。
