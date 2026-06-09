# slime 上手实操与技术详解

本目录收录面向 THUDM/slime 的中文工程技术报告，覆盖从 Docker 快速跑通到源码级训练闭环的关键实现。

## Files

- `index.html`: Kami 排版源文件，可直接在浏览器中阅读或重新打印。
- `slime-rl-scaling-guide.pdf`: PDF 成品。
- `sources.md`: 资料来源、口径和不覆盖范围。
- `data/source-map.tsv`: 主要资料映射表。

## Scope

报告基于 2026-05-06 抓取的 THUDM/slime 上游快照撰写：

- Repository: `https://github.com/THUDM/slime`
- Commit: `82007faf4b398abd32bd8e07f9638f6cfeb70729`
- Latest release at capture time: `v0.2.4`
- Release recheck on 2026-06-09: `v0.3.0`

重点内容包括 quick start、脚本参数拆解、Ray 编排、SGLang rollout、Megatron 训练、Sample 数据结构、优势估计、loss、权重同步、低精度、容错、调试和扩展接口。
