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
| DeepSeek V4 Technical Report 2026 | DeepSeek V4 官方 technical report 的完整中文深度解读，覆盖百万上下文、CSA/HCA、mHC、Muon、系统工程、后训练与代际对比 | `deepseek-v4-technical-report-2026/index.html` / `deepseek-v4-technical-report-2026/deepseek-v4-technical-report-2026.pdf` |
| ms-swift Training Framework 2026 | 大模型训练框架 ms-swift 的完整架构、训练链路、源码路径、RL 后训练、Megatron 并行、评测部署与扩展排障 | `ms-swift-training-framework-2026/index.html` / `ms-swift-training-framework-2026/ms-swift-training-framework-2026.pdf` |
| verl RL Training Framework 2026 | 大模型强化学习训练框架 verl 的完整架构、训练链路、算法配置、性能调优与源码路线 | `verl-rl-training-framework-2026/index.html` / `verl-rl-training-framework-2026/verl-rl-training-framework-2026.pdf` |
| LLM RL Algorithms 2026 | 大模型强化学习算法全景，覆盖 RLHF、RLAIF、RLVR、DPO、PPO、GRPO、DAPO、GSPO 等主流算法 | `llm-rl-algorithms-2026/index.html` / `llm-rl-algorithms-2026/llm-rl-algorithms-2026.pdf` |
| AI Training Frameworks 2026 | 大模型、多模态大模型与生成模型训练框架技术图谱 | `ai-training-frameworks-2026/index.html` / `ai-training-frameworks-2026/ai-training-frameworks-2026.pdf` |
| AI Inference Frameworks 2026 | 大模型、多模态大模型与生成模型推理框架技术图谱 | `ai-inference-frameworks-2026/index.html` / `ai-inference-frameworks-2026/ai-inference-frameworks-2026.pdf` |
| Generative Recommendation 2026 | 生成式推荐的发展史、主流算法、产业落地与趋势判断 | `generative-recommendation-2026/index.html` / `generative-recommendation-2026/generative-recommendation-2026.pdf` |
| World Models 2026 | 世界模型的发展史、主流算法、产业落地与趋势判断 | `world-models-2026/index.html` / `world-models-2026/world-models-2026.pdf` |
| slime RL Scaling Guide | THUDM/slime 上手实操与源码级技术详解 | `slime-rl-scaling-guide/index.html` / `slime-rl-scaling-guide/slime-rl-scaling-guide.pdf` |
| Claude Code Project Workflow | 面向工程团队的 Claude Code 项目工作流手册 | `claude-code-project-workflow/index.html` / `claude-code-project-workflow/claude-code-project-workflow.pdf` |
| Zero to GitHub Pages Website | 从 0 构建网站并部署到 GitHub Pages 的完整工程链路 | `zero-to-github-pages-website/index.html` / `zero-to-github-pages-website/zero-to-github-pages-website.pdf` |

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

本项目所有作品及资料均采用 [MIT License](LICENSE) 许可。除字体之外，你可以自由使用、修改、分发，但需保留原始的版权声明和许可声明。
