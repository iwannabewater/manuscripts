# AI Training Frameworks 2026

署名：Winston
版本：V3.0
资料口径：截至 2026-05-04

本目录收录《大模型与多模态生成模型训练框架技术图谱 2026》。报告聚焦训练框架本身，覆盖预训练、继续预训练、SFT、LoRA/QLoRA、偏好优化、RL 后训练、多模态训练、图像与视频生成模型训练栈。推理服务框架不作为本次主题，仅在 RL rollout、导出验证或训练加速依赖中被提及。

## Files

| 文件 | 说明 |
|---|---|
| `index.html` | 报告排版源文件 |
| `ai-training-frameworks-2026.pdf` | PDF 成品 |
| `sources.md` | 资料来源、口径与边界说明 |
| `data/repository-metadata.tsv` | 代表性项目公开仓库元数据 |
| `fonts/` | 中文排版字体 |

## Rebuild

```bash
cd ai-training-frameworks-2026
weasyprint index.html ai-training-frameworks-2026.pdf
```
