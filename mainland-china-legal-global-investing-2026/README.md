# 大陆居民合规配置港股、美股与境外基金

单页 A4 横版速查：大陆居民完全合法合规配置港股、美股敞口与境外基金的路径地图、红线、从 0 到 1 动作流、税费与风控检查。

## 文件

- `index.html`：Winston one-pager 源文件
- `mainland-china-legal-global-investing-2026.pdf`：可直接分享/打印的 PDF
- `sources.md`：官方来源与事实核对说明

## 生成

```bash
cd mainland-china-legal-global-investing-2026
python3 - <<'PY'
from weasyprint import HTML
HTML('index.html').write_pdf('mainland-china-legal-global-investing-2026.pdf')
PY
```
