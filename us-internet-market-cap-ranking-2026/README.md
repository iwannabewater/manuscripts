# 美国互联网公司市值排名 2026

这是一份 A4 横版单页研究作品，以 2026-06-10 收盘数据比较美国上市互联网平台公司的整体权益市值，并用统一口径呈现头部集中度、梯队断层与样本边界。

## Files

- `index.html`: 可读、可打印的单页源码。
- `us-internet-market-cap-ranking-2026.pdf`: PDF 成品。
- `sources.md`: 来源、证据等级、样本边界与计算方法。
- `data/company-ranking.csv`: 排名、市值、业务分类与来源编号。
- `data/candidate-screen.csv`: 接近入榜门槛的候选公司复核。
- `data/source-map.tsv`: 来源编号、URL 与支持事实映射。

## Rebuild

```bash
cd us-internet-market-cap-ranking-2026
../.venv/bin/python - <<'PY'
from weasyprint import HTML
HTML("index.html", base_url=".").write_pdf(
    "us-internet-market-cap-ranking-2026.pdf"
)
PY
```

## Scope

样本限于总部及主要经营基础在美国、以互联网平台、在线市场、数字内容、广告技术或互联网基础设施为核心的上市公司。半导体与硬件、传统电信、金融平台、纯企业软件、数据中心 REIT 和库存驱动型零售商不纳入。报告不构成投资建议。
