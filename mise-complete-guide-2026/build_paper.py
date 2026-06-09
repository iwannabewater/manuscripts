#!/usr/bin/env python3
from html import escape
from pathlib import Path
import re

from markdown_it import MarkdownIt
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
TEMPLATE = Path.home() / ".agents/skills/kami/assets/templates/long-doc.html"
TITLE = "mise 完整使用指南：开发环境、工具链与工程任务的统一管理"


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


def body_without_title(path: Path, first_heading: str) -> str:
    text = path.read_text()
    return first_heading + re.split(rf"^{re.escape(first_heading)}\s*$", text, flags=re.M)[1]


def toc_pages() -> dict[int, int]:
    pdf = ROOT / "mise-complete-guide-2026.pdf"
    if not pdf.exists():
        return {}
    pages: dict[int, int] = {}
    for page_number, page in enumerate(PdfReader(pdf).pages, 1):
        text = page.extract_text() or ""
        for chapter in re.findall(r"(\d{2}) · (?:CHAPTER|APPENDIX)", text):
            pages[int(chapter)] = page_number
    return pages


def plain_title(title: str) -> str:
    return title.replace("`", "")


def main() -> None:
    template = TEMPLATE.read_text()
    style = re.search(r"<style>(.*?)</style>", template, re.S).group(1)
    style = style.replace("../fonts/", "fonts/")
    style = style.replace("{{文档标题}}", TITLE)
    style += """
  a { color: var(--brand); text-decoration: none; }
  h1 { string-set: section-title content(); }
  figure svg { width: 100%; height: auto; display: block; }
  .cover-logo { width: 52pt; height: auto; margin-bottom: 18pt; }
  .source-list { font-size: 9pt; }
"""
    markdown = MarkdownIt("commonmark", {"html": True, "linkify": True}).enable("table")
    sections = split_sections((ROOT / "guide.md").read_text())
    appendix_titles = ["附录：mise Cheatsheet", "附录：资料来源与边界"]
    chapter_titles = [title for title, _ in sections] + appendix_titles
    pages = toc_pages()

    toc = []
    for index, title in enumerate(chapter_titles, 1):
        page = pages.get(index)
        page_text = f"{page:02d}" if page is not None else "..."
        toc.append(
            f'<div class="toc-item"><span class="toc-num">{index:02d}</span>'
            f'<span class="toc-title">{escape(plain_title(title))}</span>'
            f'<span class="toc-page" data-section="{index}">{page_text}</span></div>'
        )

    figure = f"""
<figure>
  {(ROOT / "assets/mise-project-model.svg").read_text()}
  <figcaption>Figure 1. 团队只需维护一份项目契约，差异留在入口，不留在安装说明里。</figcaption>
</figure>
"""
    body = [
        """<section class="cover">
  <div>
    <img class="cover-logo" src="assets/mise-logo.svg" alt="mise logo">
    <div class="cover-eyebrow">ENGINEERING HANDBOOK · 2026</div>
    <div class="cover-title">mise 完整使用指南<br>开发环境、工具链与工程任务的统一管理</div>
    <div class="cover-sub">从安装、工具版本、环境变量和任务，到锁文件、CI、安全边界与团队落地。</div>
  </div>
  <div class="cover-meta"><strong>Winston</strong><br>版本 V1.0 · 2026-06-02<br>基于 mise v2026.5.18 官方资料</div>
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
    cheat = body_without_title(ROOT / "CHEATSHEET.md", "## 1. 安装")
    body.append(
        f'<section class="chapter" data-section="{index}">'
        f'<div class="chapter-num">{index:02d} · APPENDIX</div>'
        "<h1>附录：mise Cheatsheet</h1>"
        '<p class="lead">这一章可以独立打印。第一次接入按顺序执行，日常使用按问题查命令。</p>'
        f"{markdown.render(cheat)}</section>"
    )

    index += 1
    sources = body_without_title(ROOT / "sources.md", "## Method")
    body.append(
        f'<section class="chapter" data-section="{index}">'
        f'<div class="chapter-num">{index:02d} · APPENDIX</div>'
        "<h1>附录：资料来源与边界</h1>"
        '<p class="lead">教程中的版本、命令与边界以 mise 官方仓库、官方文档和 GitHub Releases API 为准。交叉验证只使用对应项目的官方文档。</p>'
        f'<div class="source-list">{markdown.render(sources)}</div></section>'
    )

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{TITLE}</title>
<meta name="author" content="Winston">
<meta name="description" content="mise 完整中文使用指南，覆盖安装、工具版本、环境变量、任务、锁文件、CI、安全边界、迁移、排障与 Cheatsheet。">
<meta name="keywords" content="mise, mise-en-place, 开发环境, 工具链, CI, Cheatsheet">
<meta name="generator" content="Kami">
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
    main()
