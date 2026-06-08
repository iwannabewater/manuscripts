# WWDC 2026 全景报告

本目录收录 WWDC 2026 的完整研究稿、来源索引、主张映射、HTML 长文版与打印级 PDF。

## 交付文件

- `report.md`：完整研究稿。
- `index.html`：A4 长文排版版。
- `wwdc-2026-report.pdf`：A4 打印级 PDF。
- `sources.md`：官方与媒体来源、使用边界。
- `data/claim-map.tsv`：核心主张、证据与置信度映射。
- `assets/`：Apple 官方页面视觉素材。

## 时间边界

报告完成于北京时间 2026 年 6 月 9 日。WWDC26 于美国太平洋时间 6 月 8 日开幕，会议持续至 6 月 12 日。因此，本文覆盖 Keynote、Platforms State of the Union、Apple 首批官方页面与当时已上线的开发者视频，不把会议后续几天可能新增或修订的内容写成既定事实。

## 生成 PDF

```bash
python3 -m venv /tmp/wwdc26-report-venv
/tmp/wwdc26-report-venv/bin/pip install weasyprint pypdf pymupdf markdown
/tmp/wwdc26-report-venv/bin/python wwdc-2026-report/build.py
```

`build.py` 会从 `report.md` 与 `sources.md` 重新生成 `index.html` 和 PDF。

## 研究原则

事实优先使用 Apple Newsroom、Apple Developer 与 Apple 操作系统产品页。媒体报道只用于补充发布语境和外部评价，不替代 Apple 对功能、设备、区域和时间的官方口径。
