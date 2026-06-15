# WWDC 2026 闭幕后全景报告

本目录收录 WWDC 2026 的完整研究稿、来源索引、主张映射、HTML 长文版与打印级 PDF。

## 交付文件

- `report.md`：完整研究稿。
- `index.html`：A4 长文排版版。
- `wwdc-2026-report.pdf`：A4 打印级 PDF。
- `sources.md`：官方与媒体来源、使用边界。
- `data/claim-map.tsv`：核心主张、证据与置信度映射。
- `assets/`：Apple 官方页面视觉素材。

## 时间边界

报告于北京时间 2026 年 6 月 16 日完成闭幕后复核。WWDC26 已于 6 月 12 日结束；Apple Developer 视频索引当时有 137 个去重条目，其中 134 个可播放、3 个仍标记为即将上线。报告对动态页面、beta 状态、地区和额度条件保留明确的证据日期。

## 生成 PDF

```bash
make fonts
.venv/bin/python wwdc-2026-report/build.py
make verify
```

`build.py` 会从 `report.md` 与 `sources.md` 重新生成 `index.html` 和 PDF。

## 研究原则

事实使用 Apple Newsroom、Apple Developer、操作系统产品页与官方会话。页面测量、Apple 自报数据、分析判断和未知事项分别标注，不把 beta 计划、基准峰值或平台数据改写成稳定交付和独立验证。
