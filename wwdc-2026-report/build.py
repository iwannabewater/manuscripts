from __future__ import annotations

import html
import re
from pathlib import Path

import markdown
from weasyprint import HTML


ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "report.md"
SOURCES = ROOT / "sources.md"
OUTPUT_HTML = ROOT / "index.html"
OUTPUT_PDF = ROOT / "wwdc-2026-report.pdf"


TOC_NOTES = {
    "01. 执行摘要": "六个结论与关键数字",
    "02. 大会事实与时间边界": "会议规模、日程与发布节奏",
    "03. 发布主线：先修地基，再把 AI 接进系统": "可靠性与 AI 的同一条主线",
    "04. Siri AI：产品能力、系统架构与开放节奏": "个人上下文、应用动作与隐私架构",
    "05. 开发者 AI 栈：从模型调用到可测试代理": "Foundation Models、Core AI、MLX、Evaluations",
    "06. Xcode 27、Swift 6.4 与 SwiftUI": "代理、语言与 UI 框架更新",
    "07. OS 27 平台更新": "iPhone、iPad、Mac、Watch、Vision Pro 与 TV",
    "08. 性能、搜索、网络与 Liquid Glass": "官方基准与测试边界",
    "09. 儿童安全与平台治理": "内容、联系人、时间与开发者责任",
    "10. App Store：从单应用订阅走向组织、群组与跨开发者组合": "增长、发现、订阅与审核",
    "11. 兼容性与可用性矩阵": "系统、AI、设备、语言与地区",
    "12. 对用户、开发者和 Apple 的意义": "行动建议与成败标准",
    "13. 仍未知的事项": "后续 beta 需要验证的问题",
    "14. 建议阅读顺序": "官方资料的高效入口",
    "附录：证据等级": "事实、测量、分析与媒体语境",
    "来源与使用边界": "官方来源、媒体来源与方法限制",
}


ARCHITECTURE = """
<figure class="architecture">
  <svg viewBox="0 0 960 560" xmlns="http://www.w3.org/2000/svg" role="img"
       aria-label="Siri AI 四层系统架构">
    <defs>
      <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
        <circle cx="1" cy="1" r="0.9" fill="#E3E2DC"/>
      </pattern>
    </defs>
    <rect width="960" height="560" fill="#f5f4ed"/>
    <rect width="960" height="560" fill="url(#dots)" opacity="0.55"/>
    <text x="80" y="40" fill="#1B365D" font-size="14" font-weight="600"
          font-family="JetBrains Mono" letter-spacing="3">FIGURE  1</text>
    <text x="224" y="40" fill="#504e49" font-size="14"
          font-family="JetBrains Mono" letter-spacing="3">SIRI AI SYSTEM ARCHITECTURE</text>
    <line x1="80" y1="56" x2="880" y2="56" stroke="#1B365D" stroke-width="1"/>

    <rect x="80" y="88" width="800" height="76" rx="6" fill="#faf9f5"
          stroke="#6b6a64" stroke-width="1"/>
    <text x="108" y="116" fill="#6b6a64" font-size="14" font-family="JetBrains Mono"
          letter-spacing="2">INTERACTION</text>
    <text font-family="TsangerJinKai02" x="108" y="148" fill="#141413" font-size="23" font-weight="600">
      语音 · 键盘 · 相机 · 截图 · 视线 · Spotlight
    </text>

    <path d="M480 164 L480 184" stroke="#504e49" stroke-width="1.5"/>
    <path d="M474 178 L480 184 L486 178" fill="none" stroke="#504e49"
          stroke-width="1.5" stroke-linecap="round"/>

    <rect x="80" y="188" width="800" height="76" rx="6" fill="#EEF2F7"
          stroke="#1B365D" stroke-width="1.5"/>
    <text x="108" y="216" fill="#1B365D" font-size="14" font-family="JetBrains Mono"
          letter-spacing="2">ORCHESTRATION</text>
    <text font-family="TsangerJinKai02" x="108" y="248" fill="#141413" font-size="23" font-weight="600">
      系统编排器：理解意图，选择数据、工具与执行路径
    </text>

    <path d="M480 264 L480 284" stroke="#1B365D" stroke-width="1.5"/>
    <path d="M474 278 L480 284 L486 278" fill="none" stroke="#1B365D"
          stroke-width="1.5" stroke-linecap="round"/>

    <rect x="80" y="288" width="800" height="76" rx="6" fill="#faf9f5"
          stroke="#6b6a64" stroke-width="1"/>
    <text x="108" y="316" fill="#6b6a64" font-size="14" font-family="JetBrains Mono"
          letter-spacing="2">DATA &amp; ACTIONS</text>
    <text font-family="TsangerJinKai02" x="108" y="348" fill="#141413" font-size="23" font-weight="600">
      Spotlight 索引 · App Toolbox · App Intents · 屏幕实体
    </text>

    <path d="M480 364 L480 384" stroke="#504e49" stroke-width="1.5"/>
    <path d="M474 378 L480 384 L486 378" fill="none" stroke="#504e49"
          stroke-width="1.5" stroke-linecap="round"/>

    <rect x="80" y="388" width="384" height="84" rx="6" fill="#faf9f5"
          stroke="#141413" stroke-width="1"/>
    <text x="108" y="416" fill="#6b6a64" font-size="14" font-family="JetBrains Mono"
          letter-spacing="2">ON DEVICE</text>
    <text font-family="TsangerJinKai02" x="108" y="448" fill="#141413" font-size="22" font-weight="600">
      Apple Foundation Models
    </text>
    <rect x="496" y="388" width="384" height="84" rx="6" fill="#EEEDE6"
          stroke="#6b6a64" stroke-width="1"/>
    <text x="524" y="416" fill="#6b6a64" font-size="14" font-family="JetBrains Mono"
          letter-spacing="2">PRIVATE CLOUD</text>
    <text font-family="TsangerJinKai02" x="524" y="448" fill="#141413" font-size="22" font-weight="600">
      Private Cloud Compute
    </text>

    <text font-family="TsangerJinKai02" x="80" y="516" fill="#504e49" font-size="16">
      请求先在设备上编排；需要更强推理时，只把必要部分交给可验证的私有云。
    </text>
  </svg>
  <figcaption>图 1：根据 Apple 官方说明整理。架构边界仍需后续安全研究与真实设备测试验证。</figcaption>
</figure>
"""


CSS = r"""
@font-face {
  font-family: "Tsanger";
  src: url("../assets/fonts/TsangerJinKai02-W04.ttf") format("truetype"),
       url("https://cdn.jsdelivr.net/gh/tw93/Kami@main/assets/fonts/TsangerJinKai02-W04.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "Tsanger";
  src: url("../assets/fonts/TsangerJinKai02-W05.ttf") format("truetype"),
       url("https://cdn.jsdelivr.net/gh/tw93/Kami@main/assets/fonts/TsangerJinKai02-W05.ttf") format("truetype");
  font-weight: 600;
}
@font-face {
  font-family: "JetBrains Mono";
  src: url("../assets/fonts/JetBrainsMono.woff2") format("woff2");
  font-weight: 400 700;
}
@page {
  size: A4;
  margin: 18mm 19mm 19mm;
  background: #f5f4ed;
  @top-right {
    content: string(chapter-title);
    font-family: "Tsanger";
    font-size: 7.5pt;
    color: #6b6a64;
  }
  @bottom-left {
    content: "WWDC 2026 · RESEARCH REPORT";
    font-family: "JetBrains Mono";
    font-size: 6.5pt;
    letter-spacing: 0.08em;
    color: #6b6a64;
  }
  @bottom-right {
    content: counter(page);
    font-family: "Tsanger";
    font-size: 8pt;
    color: #6b6a64;
  }
}
@page:first {
  @top-right { content: ""; }
  @bottom-left { content: ""; }
  @bottom-right { content: ""; }
}
:root {
  --paper: #f5f4ed;
  --ivory: #faf9f5;
  --ink: #141413;
  --warm: #3d3d3a;
  --olive: #504e49;
  --stone: #6b6a64;
  --brand: #1B365D;
  --brand-soft: #E4ECF5;
  --line: #dedcd2;
}
* { box-sizing: border-box; }
html { background: var(--paper); }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: "Tsanger";
  font-size: 10.3pt;
  line-height: 1.66;
  letter-spacing: 0.15pt;
  widows: 3;
  orphans: 3;
}
main { width: 100%; }
a { color: var(--brand); text-decoration: none; }
p { margin: 0 0 9pt; }
strong { font-weight: 600; }
code {
  font-family: "JetBrains Mono", "Tsanger";
  font-size: 8.3pt;
  padding: 1pt 3pt;
  border-radius: 2pt;
  background: var(--ivory);
}
.cover {
  min-height: 259mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  break-after: page;
  padding: 5mm 0 1mm;
}
.cover-topline {
  display: flex;
  justify-content: space-between;
  padding-bottom: 4mm;
  border-bottom: 0.5pt solid var(--line);
  color: var(--brand);
  font-family: "JetBrains Mono";
  font-size: 7pt;
  letter-spacing: 0.14em;
}
.cover-copy { padding-top: 11mm; }
.cover-eyebrow {
  color: var(--brand);
  font-family: "JetBrains Mono";
  font-size: 8pt;
  letter-spacing: 0.14em;
}
.cover h1 {
  margin: 6mm 0 4mm;
  max-width: 174mm;
  font-size: 35pt;
  line-height: 1.14;
  letter-spacing: 0.02em;
}
.cover h1 span {
  display: block;
  margin-top: 2.5mm;
  color: var(--brand);
  font-size: 21pt;
  line-height: 1.35;
}
.cover-deck {
  max-width: 164mm;
  color: var(--olive);
  font-size: 12.3pt;
  line-height: 1.62;
}
.cover-visual {
  overflow: hidden;
  margin: 10mm 0 7mm;
  border: 0.7pt solid #282828;
  border-radius: 4pt;
  background: #000;
}
.cover-visual img {
  display: block;
  width: 100%;
  height: auto;
}
.cover-caption {
  padding: 2.6mm 3mm;
  color: #d7d7d7;
  background: #080808;
  font-size: 7.2pt;
}
.cover-meta {
  display: flex;
  justify-content: space-between;
  padding-top: 4mm;
  border-top: 0.5pt solid var(--line);
  color: var(--stone);
  font-size: 8.5pt;
}
.cover-meta strong { color: var(--warm); }
.toc {
  min-height: 252mm;
  break-after: page;
}
.toc h2 {
  margin: 0 0 8mm;
  padding-left: 8pt;
  border-left: 2.5pt solid var(--brand);
  font-size: 23pt;
}
.toc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0 10mm;
}
.toc-item {
  display: grid;
  grid-template-columns: 10mm 1fr;
  min-height: 20mm;
  padding: 4mm 0;
  border-bottom: 0.4pt solid var(--line);
}
.toc-num {
  color: var(--brand);
  font-family: "JetBrains Mono";
  font-size: 8pt;
  letter-spacing: 0.08em;
}
.toc-title { font-size: 10.8pt; line-height: 1.35; }
.toc-note {
  display: block;
  margin-top: 1.5mm;
  color: var(--stone);
  font-size: 7.8pt;
  line-height: 1.4;
}
.chapter {
  break-before: page;
}
.chapter-07 {
  font-size: 9.6pt;
  line-height: 1.55;
}
.chapter-07 h2 { margin-top: 14pt; }
.chapter-07 li { margin: 1.4pt 0; }
.chapter-11 ul {
  columns: 2;
  column-gap: 8mm;
}
.chapter-11 li {
  break-inside: avoid;
  margin: 1.5pt 0;
}
.chapter-kicker {
  margin-bottom: 3mm;
  color: var(--brand);
  font-family: "JetBrains Mono";
  font-size: 7.2pt;
  letter-spacing: 0.14em;
}
.chapter > h1 {
  string-set: chapter-title content();
  margin: 0 0 7mm;
  padding: 0 0 4mm 8pt;
  border-left: 2.5pt solid var(--brand);
  border-bottom: 0.5pt solid var(--line);
  font-size: 22pt;
  line-height: 1.25;
}
h2 {
  margin: 20pt 0 7pt;
  color: var(--ink);
  font-size: 15pt;
  line-height: 1.32;
  break-after: avoid;
}
h3 {
  margin: 15pt 0 6pt;
  color: var(--brand);
  font-size: 12pt;
  line-height: 1.35;
  break-after: avoid;
}
blockquote {
  margin: 10pt 0 14pt;
  padding: 9pt 13pt;
  border-left: 2pt solid var(--brand);
  border-radius: 3pt;
  background: var(--ivory);
  color: var(--warm);
  break-inside: avoid;
}
blockquote p { margin: 0; font-size: 11.3pt; line-height: 1.58; }
ul, ol { margin: 5pt 0 10pt; padding-left: 18pt; }
li { margin: 2.5pt 0; }
li::marker { color: var(--brand); }
hr {
  height: 0;
  margin: 15pt 0;
  border: 0;
  border-top: 0.5pt solid var(--line);
}
table {
  width: 100%;
  margin: 11pt 0 14pt;
  border-collapse: collapse;
  font-size: 8.35pt;
  line-height: 1.43;
  break-inside: avoid;
}
thead { display: table-header-group; }
th {
  padding: 5.5pt 6pt;
  color: #f8f7f2;
  background: var(--brand);
  text-align: left;
  font-weight: 600;
}
td {
  padding: 5pt 6pt;
  border-bottom: 0.35pt solid var(--line);
  vertical-align: top;
}
tbody tr:nth-child(even) td { background: var(--ivory); }
sup.cite {
  margin-left: 1pt;
  color: var(--brand);
  font-family: "JetBrains Mono";
  font-size: 5.8pt;
  letter-spacing: 0;
}
figure {
  margin: 14pt 0 16pt;
  break-inside: avoid;
}
figure svg, figure img { display: block; width: 100%; height: auto; }
figcaption {
  margin-top: 5pt;
  color: var(--stone);
  font-size: 7.6pt;
  text-align: center;
}
.architecture {
  padding: 3mm;
  border: 0.5pt solid var(--line);
  border-radius: 4pt;
  background: var(--paper);
}
.source-index h2 { margin-top: 16pt; }
.source-index ul { padding-left: 16pt; }
.source-index li { margin-bottom: 4pt; }
.source-index a { overflow-wrap: anywhere; }
.colophon {
  margin-top: 12mm;
  padding-top: 5mm;
  border-top: 0.5pt solid var(--line);
  color: var(--stone);
  font-size: 8pt;
}
@media screen {
  html { background: #e8e7e1; }
  body {
    max-width: 210mm;
    margin: 0 auto;
    padding: 18mm 19mm;
    box-shadow: 0 0 35px rgba(20, 20, 19, 0.12);
  }
  .cover, .toc { min-height: auto; padding-bottom: 20mm; }
}
"""


def render_markdown(text: str) -> str:
    rendered = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )
    rendered = re.sub(
        r"\[S(\d{2})\]",
        lambda match: f'<sup class="cite">[S{match.group(1)}]</sup>',
        rendered,
    )
    return rendered


def chapterize(rendered: str) -> tuple[str, list[str]]:
    parts = re.split(r"(?=<h2>)", rendered)
    chapters: list[str] = []
    titles: list[str] = []
    for part in parts:
        if not part.strip():
            continue
        match = re.match(r"<h2>(.*?)</h2>", part, flags=re.S)
        if not match:
            continue
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = html.unescape(title)
        titles.append(title)
        number_match = re.match(r"(\d{2})\.", title)
        number = number_match.group(1) if number_match else "APPENDIX"
        body = part[match.end() :]
        body = body.replace("<hr>", "")
        body = body.replace("<h3>", "<h2>").replace("</h3>", "</h2>")
        body = body.replace("<h4>", "<h3>").replace("</h4>", "</h3>")
        if title.startswith("04. Siri AI"):
            body = body.replace("<h2>4.3 Personal Context", ARCHITECTURE + "<h2>4.3 Personal Context", 1)
        chapters.append(
            f'<section class="chapter chapter-{number.lower()}"><div class="chapter-kicker">'
            f'{number} · WWDC 2026</div><h1>{match.group(1)}</h1>{body}</section>'
        )
    return "\n".join(chapters), titles


def build_toc(titles: list[str]) -> str:
    items = []
    for index, title in enumerate(titles, start=1):
        note = TOC_NOTES.get(title, "")
        items.append(
            '<div class="toc-item">'
            f'<div class="toc-num">{index:02d}</div>'
            f'<div class="toc-title">{html.escape(title)}'
            f'<span class="toc-note">{html.escape(note)}</span></div>'
            "</div>"
        )
    return '<section class="toc"><h2>目录</h2><div class="toc-grid">' + "".join(items) + "</div></section>"


def source_chapter() -> tuple[str, str]:
    source_text = SOURCES.read_text(encoding="utf-8")
    source_text = re.sub(r"^# 来源与使用边界\s*", "", source_text)
    rendered = render_markdown(source_text)
    return (
        '<section class="chapter source-index">'
        '<div class="chapter-kicker">SOURCES · METHODOLOGY</div>'
        '<h1>来源与使用边界</h1>'
        f"{rendered}"
        '<div class="colophon">'
        "研究与撰写：Winston · 版本 1.0 · 2026-06-09"
        "</div></section>",
        "来源与使用边界",
    )


def build() -> None:
    report_text = REPORT.read_text(encoding="utf-8")
    report_body = report_text[report_text.index("## 01. 执行摘要") :]
    rendered = render_markdown(report_body)
    chapters, titles = chapterize(rendered)
    sources_html, source_title = source_chapter()
    titles.append(source_title)

    document = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>WWDC 2026 全景报告</title>
  <meta name="author" content="Winston">
  <meta name="description" content="WWDC 2026 官方信息与开发者技术全景报告，覆盖 Siri AI、Apple Intelligence、OS 27、Xcode 27、Swift 6.4、App Store 与可用性边界。">
  <meta name="keywords" content="WWDC 2026,Siri AI,Apple Intelligence,OS 27,Xcode 27">
  <style>{CSS}</style>
<link rel="stylesheet" href="../assets/styles/publication-fonts.css">
</head>
<body>
<main>
  <section class="cover">
    <div>
      <div class="cover-topline"><span>APPLE DEVELOPER RESEARCH</span><span>2026 · 06 · 09</span></div>
      <div class="cover-copy">
        <div class="cover-eyebrow">WWDC26 · OFFICIAL INFORMATION &amp; ANALYSIS</div>
        <h1>WWDC 2026 全景报告
          <span>Siri AI 进入开发者测试，OS 27 重建可靠性与平台能力</span>
        </h1>
        <p class="cover-deck">基于 Apple Newsroom、Apple Developer、六大操作系统产品页及权威媒体报道，拆解 Siri AI、开发者 AI 栈、OS 27、平台治理和真实可用性边界。</p>
      </div>
      <figure class="cover-visual">
        <img src="assets/apple-platforms-siri-ai.jpg" alt="Apple 官方展示的 Mac、iPhone、iPad、Apple Watch 与 Apple Vision Pro">
        <figcaption class="cover-caption">Apple 官方跨设备主视觉。原图来自 macOS 27 产品页，用于评论与研究说明。</figcaption>
      </figure>
    </div>
    <div class="cover-meta">
      <div><strong>Winston</strong><br>版本 1.0 · 北京时间 2026-06-09</div>
      <div>官方事实优先<br>媒体观点单独标注</div>
    </div>
  </section>
  {build_toc(titles)}
  {chapters}
  {sources_html}
</main>
</body>
</html>
"""
    OUTPUT_HTML.write_text(document, encoding="utf-8")
    HTML(filename=str(OUTPUT_HTML), base_url=str(ROOT)).write_pdf(str(OUTPUT_PDF))


if __name__ == "__main__":
    build()
