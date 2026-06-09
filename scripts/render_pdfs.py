#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from weasyprint import HTML


ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def work_dirs() -> list[Path]:
    return sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir()
        and not path.name.startswith(".")
        and path.name not in {"assets", "scripts", "sources", "research"}
        and (path / "index.html").exists()
    )


def rebuild_generated_sources() -> None:
    for relative in [
        "llm-rl-algorithms-2026/build_deck.py",
        "wwdc-2026-report/build.py",
        "macos-developer-handbook-2026/build_paper.py",
        "mise-complete-guide-2026/build_paper.py",
    ]:
        script = ROOT / relative
        if script.exists():
            run([sys.executable, script.name], script.parent)


def render_pdf(work_dir: Path) -> None:
    output = work_dir / f"{work_dir.name}.pdf"
    HTML(filename=str(work_dir / "index.html"), base_url=str(work_dir)).write_pdf(str(output))
    print(f"rendered {output.relative_to(ROOT)}")


def main() -> None:
    rebuild_generated_sources()
    for work_dir in work_dirs():
        render_pdf(work_dir)


if __name__ == "__main__":
    main()
