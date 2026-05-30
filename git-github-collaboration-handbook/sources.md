# Sources

作者：Winston
资料口径：截至 2026-05-30

## Method

本手册优先采用官方文档和公开一手材料：Git 官方参考、GitHub 官方文档、Google Engineering Practices、Meta Engineering Blog、OpenAI 官方 GitHub 仓库贡献说明、CloudWeGo / ByteDance 开源项目贡献说明，以及 Conventional Commits、SemVer、Keep a Changelog 等公开规范。

正文中的“大厂实践”只使用公开可验证原则，不推断任何公司的非公开内部制度。Google 资料用于 code review、小变更和测试门禁原则；Meta 资料用于大规模仓库、stacked diffs 和高信号工具链思路；OpenAI 与 CloudWeGo 资料用于开源贡献、生成代码边界、测试 / lint / 发布管线和 contributor 管理；GitHub 文档用于 PR、Issue、CODEOWNERS、branch protection、merge queue、fork workflow 和 Actions。

本文不替代目标团队的安全、合规、发布、数据治理或知识产权制度。正式落地前应复核目标仓库的许可证、分支保护、权限模型、CI 供应链、密钥管理、代码所有权和发布规则。

## Primary Sources

- Git reference: https://git-scm.com/docs
- Git branching workflows: https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows
- Git rebase reference: https://git-scm.com/docs/git-rebase
- GitHub Flow: https://docs.github.com/en/get-started/using-github/github-flow
- GitHub contributing to a project: https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project
- GitHub issues: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
- GitHub issue and pull request templates: https://docs.github.com/articles/about-issue-and-pull-request-templates
- GitHub pull request reviews: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews
- GitHub protected branches: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub merge queue: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- GitHub CODEOWNERS: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- GitHub Actions documentation: https://docs.github.com/en/actions/
- Google Engineering Practices, Code Review Standard: https://google.github.io/eng-practices/review/reviewer/standard.html
- Google Engineering Practices, Small CLs: https://google.github.io/eng-practices/review/developer/small-cls.html
- Google Engineering Practices, What to look for in a code review: https://google.github.io/eng-practices/review/reviewer/looking-for.html
- Google Engineering Practices, How to handle reviewer comments: https://google.github.io/eng-practices/review/developer/handling-comments.html
- Google Research, Modern Code Review, A Case Study at Google: https://research.google/pubs/modern-code-review-a-case-study-at-google/
- Meta Engineering, Sapling source control: https://engineering.fb.com/2022/11/15/open-source/sapling-source-control-scalable/
- Meta Engineering, Developer tools working at scale: https://engineering.fb.com/2023/06/27/developer-tools/meta-developer-tools-open-source/
- OpenAI openai-python CONTRIBUTING: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md
- OpenAI Cookbook CONTRIBUTING: https://github.com/openai/openai-cookbook/blob/main/CONTRIBUTING.md
- CloudWeGo about: https://www.cloudwego.io/about/
- CloudWeGo Kitex CONTRIBUTING: https://github.com/cloudwego/kitex/blob/develop/CONTRIBUTING.md
- CloudWeGo Hertz CONTRIBUTING: https://github.com/cloudwego/hertz/blob/develop/CONTRIBUTING.md
- Conventional Commits 1.0.0: https://www.conventionalcommits.org/en/v1.0.0/
- Semantic Versioning 2.0.0: https://semver.org/lang/zh-CN/spec/v2.0.0.html
- Keep a Changelog 1.1.0: https://keepachangelog.com/en/1.1.0/
