# ms-swift Training Framework 2026

署名：Winston
版本：V1.0
资料口径：截至 2026-05-19

本目录收录《ms-swift 大模型训练框架全景与源码级指南 2026》。报告聚焦 ModelScope 社区 ms-swift 的训练框架逻辑，覆盖定位、源码架构、CLI 与参数、数据与模板、CPT/SFT、LoRA/QLoRA、RL 后训练、Megatron-SWIFT、多模态与 Agent、评测部署、扩展与排障。

## Files

| 文件 | 说明 |
|---|---|
| `index.html` | 报告排版源文件 |
| `ms-swift-training-framework-2026.pdf` | PDF 成品 |
| `sources.md` | 资料来源、口径与边界说明 |
| `data/source-map.tsv` | 来源映射与核对口径 |

## Rebuild

```bash
cd ms-swift-training-framework-2026
weasyprint index.html ms-swift-training-framework-2026.pdf
```
