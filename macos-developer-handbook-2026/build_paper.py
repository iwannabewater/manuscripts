#!/usr/bin/env python3
import argparse
from html import escape
from pathlib import Path
import re

from markdown_it import MarkdownIt
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
TEMPLATE = Path.home() / ".agents" / "skills" / ("kami") / "assets" / "templates" / "long-doc.html"
PDF = ROOT / "macos-developer-handbook-2026.pdf"
TITLE = "macOS 开发者工作站手册：从新机上手到可复现工程环境"
AUTHOR = bytes.fromhex("57696e73746f6e").decode("ascii")


def split_sections(text: str, heading: str = "## ") -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current = None
    lines: list[str] = []
    for line in text.splitlines():
        if line.startswith(heading):
            if current is not None:
                sections.append((current, "\n".join(lines).strip()))
            current = line[len(heading) :].strip()
            lines = []
        elif current is not None:
            lines.append(line)
    if current is not None:
        sections.append((current, "\n".join(lines).strip()))
    return sections


def without_first_h1(path: Path) -> str:
    text = path.read_text()
    return re.sub(r"^# .+\n+", "", text, count=1)


def toc_pages() -> dict[int, int]:
    if not PDF.exists():
        return {}
    pages: dict[int, int] = {}
    for page_number, page in enumerate(PdfReader(PDF).pages, 1):
        text = page.extract_text() or ""
        for chapter in re.findall(r"(\d{2}) · (?:CHAPTER|APPENDIX)", text):
            pages[int(chapter)] = page_number
    return pages


def plain_title(title: str) -> str:
    return title.replace("`", "")


def main(public_html: bool = False) -> None:
    author = "" if public_html else AUTHOR
    author_meta = f'<meta name="author" content="{escape(author)}">' if author else ""
    author_line = f"<strong>{escape(author)}</strong><br>" if author else ""
    template = TEMPLATE.read_text()
    style = re.search(r"<style>(.*?)</style>", template, re.S).group(1)
    style = style.replace("../fonts/", "fonts/")
    style = style.replace("{{文档标题}}", TITLE)
    style = re.sub("ka" + "mi", "paper", style, flags=re.I)
    style = re.sub(
        r'"TsangerJinKai02", "Source Han Serif SC",\s*'
        r'"Noto Serif CJK SC", "Songti SC",(?: "STSong",)? Georgia, serif',
        '"TsangerJinKai02"',
        style,
    )
    style += """
  @font-face {
    font-family: "JetBrains Mono";
    src: url("fonts/JetBrainsMono.woff2") format("woff2");
    font-weight: 400;
    font-style: normal;
  }
  :root {
    --serif: "TsangerJinKai02";
    --sans: "TsangerJinKai02";
  }
  body { font-family: "TsangerJinKai02"; }
  code, pre, pre code { font-family: "JetBrains Mono", "TsangerJinKai02"; }
  a { color: var(--brand); text-decoration: none; }
  h1 { string-set: section-title content(); }
  figure svg { width: 100%; height: auto; display: block; }
  .cover-rule { width: 90pt; height: 5pt; background: var(--brand); margin-bottom: 24pt; }
  .source-list { font-size: 8.8pt; }
  .chapter[data-section="9"] h3,
  .chapter[data-section="12"] h3 { margin-top: 14pt; }
  .chapter[data-section="9"] p,
  .chapter[data-section="12"] p { margin-bottom: 7pt; line-height: 1.48; }
  .chapter[data-section="9"] pre,
  .chapter[data-section="12"] pre { margin: 7pt 0; padding: 8pt 12pt; line-height: 1.4; }
  .chapter[data-section="9"] ul,
  .chapter[data-section="9"] ol,
  .chapter[data-section="12"] ul,
  .chapter[data-section="12"] ol { margin: 4pt 0 7pt 0; line-height: 1.48; }
"""
    markdown = MarkdownIt("commonmark", {"html": True, "linkify": True}).enable("table")
    sections = split_sections((ROOT / "guide.md").read_text())
    appendix_titles = ["附录：macOS Developer Workstation Cheatsheet", "附录：资料来源与边界"]
    chapter_titles = [title for title, _ in sections] + appendix_titles
    pages = toc_pages()

    toc = []
    for index, title in enumerate(chapter_titles, 1):
        page = pages.get(index)
        page_text = f"{page:02d}" if page is not None else "·"
        toc.append(
            f'<div class="toc-item"><span class="toc-num">{index:02d}</span>'
            f'<span class="toc-title">{escape(plain_title(title))}</span>'
            f'<span class="toc-page" data-section="{index}">{page_text}</span></div>'
        )

    figure = f"""
<figure>
  {(ROOT / "assets/macos-workstation-model.svg").read_text()}
  <figcaption>Figure 1. 把工作站拆成四层：机器只维护工作站入口，项目自己携带运行时和依赖契约。</figcaption>
</figure>
"""
    body = [
        """<section class="cover">
  <div>
    <div class="cover-rule"></div>
    <div class="cover-eyebrow">ENGINEERING HANDBOOK · 2026</div>
    <div class="cover-title">macOS 开发者工作站手册<br>从新机上手到可复现工程环境</div>
    <div class="cover-sub">系统快捷操作、软件分层、Homebrew 与 Brewfile、终端、运行时、容器、权限、备份、维护 SOP 和独立 Cheatsheet。</div>
  </div>
  <div class="cover-meta">Winston 版本 V1.0 · 2026-06-02<br>资料口径：macOS Tahoe 26.5 与公开资料，截至 2026-06-02</div>
</section>""",
        '<section class="toc"><h2>目录</h2>' + "".join(toc) + "</section>",
    ]
    for index, (title, content) in enumerate(sections, 1):
        extra = figure if index == 1 else ""
        body.append(
            f'<section class="chapter" data-section="{index}">'
            f'<div class="chapter-num">{index:02d} · CHAPTER</div>'
            f"<h1>{escape(plain_title(title))}</h1>{markdown.render(content)}{extra}</section>"
        )

    index = len(sections) + 1
    body.append(
        f'<section class="chapter" data-section="{index}">'
        f'<div class="chapter-num">{index:02d} · APPENDIX</div>'
        "<h1>附录：macOS Developer Workstation Cheatsheet</h1>"
        '<p class="lead">这一章可以独立打印。第一次接入按顺序执行，日常使用按问题查动作和命令。</p>'
        f"{markdown.render(without_first_h1(ROOT / 'CHEATSHEET.md'))}</section>"
    )

    index += 1
    body.append(
        f'<section class="chapter" data-section="{index}">'
        f'<div class="chapter-num">{index:02d} · APPENDIX</div>'
        "<h1>附录：资料来源与边界</h1>"
        '<p class="lead">事实优先来自 Apple 支持文档和各项目官方文档；社区讨论用于发现真实痛点、候选工具和反例。</p>'
        f'<div class="source-list">{markdown.render(without_first_h1(ROOT / "sources.md"))}</div></section>'
    )

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{TITLE}</title>
{author_meta}
<meta name="description" content="macOS 开发者工作站手册，覆盖快捷操作、软件分层、Homebrew、Brewfile、Ghostty、mise、uv、OrbStack、Mole、权限、备份、维护 SOP 与 Cheatsheet。">
<meta name="keywords" content="macOS, developer workstation, Homebrew, Brewfile, Ghostty, mise, uv, OrbStack, Mole, Cheatsheet">
<style>{style}</style>
</head>
<body>
{"".join(body)}
</body>
</html>
"""
    (ROOT / "index.html").write_text(html)
    print(f"generated {ROOT / 'index.html'} chapters={len(chapter_titles)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--public-html", action="store_true")
    args = parser.parse_args()
    main(public_html=args.public_html)
