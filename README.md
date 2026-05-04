# Manuscripts

本 Repo 为 Winston 对于一些工程技术的搜集与总结沉淀，于此处进行版本化归档。每项产出内容独立成目录，目录内保留排版源文件、PDF 成品、资料来源、数据文件及复现所需字体。

## Repository Scope

- 收录范围：公开技术长文、工程报告和配套资料。
- 交付形态：以 `index.html` 作为可读与可打印源文件，以 PDF 作为正式成品。
- 资料边界：每项作品通过 `sources.md` 说明来源、口径、方法和不覆盖的范围。
- 数据文件：涉及公开仓库、资料映射或统计口径的内容，统一放入作品目录下的 `data/`。

## Published Works

| 作品 | 主题 | 文件 |
|---|---|---|
| AI Training Frameworks 2026 | 大模型、多模态大模型与生成模型训练框架技术图谱 | `ai-training-frameworks-2026/index.html` / `ai-training-frameworks-2026/ai-training-frameworks-2026.pdf` |
| AI Inference Frameworks 2026 | 大模型、多模态大模型与生成模型推理框架技术图谱 | `ai-inference-frameworks-2026/index.html` / `ai-inference-frameworks-2026/ai-inference-frameworks-2026.pdf` |
| Claude Code Project Workflow | 面向工程团队的 Claude Code 项目工作流手册 | `claude-code-project-workflow/index.html` / `claude-code-project-workflow/claude-code-project-workflow.pdf` |

## Directory Contract

```text
<work-slug>/
  README.md
  index.html
  <work-slug>.pdf
  sources.md
  data/
  fonts/
```

HTML 源文件与 PDF 成品保存在同级目录，便于逐项审阅、复现与迁移。作品目录应保持自足，不依赖根目录下的临时状态或未纳入版本控制的生成文件。

## License

本项目所有作品及资料均采用 [MIT License](LICENSE) 许可。你可以自由使用、修改、分发，但需保留原始的版权声明和许可声明。
