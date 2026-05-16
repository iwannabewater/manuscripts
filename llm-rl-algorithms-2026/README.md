# 大模型强化学习算法全景

从 RLHF、DPO 到 GRPO、DAPO、GSPO 的公式化理解与工程判据

This directory contains an independently designed Chinese slide deck on reinforcement learning algorithms for large language model post-training. It covers RLHF, RLAIF, RLVR, PPO, RLOO, ReMax, REINFORCE++, DPO, IPO, KTO, ORPO, SimPO, GRPO, Dr.GRPO, DAPO, GSPO, CISPO, VAPO, RAFT, ReST, RRHF, SLiC-HF and representative industrial recipes.

## Artifacts

- `index.html` — source slide deck for browser and PDF rendering.
- `llm-rl-algorithms-2026.pdf` — printable PDF deck.
- `llm-rl-algorithms-2026.pptx` — PowerPoint export with rendered LaTeX formula images.
- `sources.md` — source map and references.
- `assets/formulas/` — LaTeX-generated SVG and PNG formula assets.

## Build

```bash
python3 build_deck.py
python3 -c "from weasyprint import HTML; HTML('index.html').write_pdf('llm-rl-algorithms-2026.pdf')"
```

The formula assets are compiled with `latex` and `dvisvgm`; PPTX export uses `python-pptx`.
