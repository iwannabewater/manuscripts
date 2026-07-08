#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "assets" / "math"


FORMULAS: dict[str, str] = {
    "task-recall": r"""
\begin{aligned}
\mathcal{D} &= \{\mathrm{d}_i\}_{i=1}^{L}, \qquad L \approx 10^9,\\
\mathcal{D}_{\mathrm{cand}} &=
\mathop{\mathrm{arg\,top}\text{-}N}_{\mathrm{d}_i \in \mathcal{D}}
\mathrm{sim}\!\left(\Phi_{\mathrm{embd}}(\mathrm{q}),\Phi_{\mathrm{embd}}(\mathrm{d}_i)\right),
\qquad N \approx 10^2 .
\end{aligned}
""",
    "mrl-objective": r"""
\begin{aligned}
\mathcal{G} &= \{256,512,1024,2048,3072\},\\
\mathcal{L}_{\mathrm{embd}}^{\mathrm{mrl}}
&= \sum_{g \in \mathcal{G}}\lambda_g
\left(
-\frac{1}{|\mathcal{B}|}\sum_{i \in \mathcal{B}}
\log
\frac{
\exp\!\left(\mathrm{sim}(\mathbf{h}^{\mathrm{que}}_{i,1:g},
\mathbf{h}^{\mathrm{doc}+}_{i,1:g})/\tau\right)
}{
\sum_{j \in \mathcal{B}}
\exp\!\left(\mathrm{sim}(\mathbf{h}^{\mathrm{que}}_{i,1:g},
\mathbf{h}^{\mathrm{doc}}_{j,1:g})/\tau\right)
}
\right).
\end{aligned}
""",
    "angular-margin": r"""
\begin{aligned}
\theta_{i,u} &= \arccos(\mathbf{h}_i^{\top}\mathbf{w}_u),\\
P(\mathrm{y}_i \mid \mathbf{h}_i)
&=
\frac{
\exp\!\left(\mathrm{sim}(\theta_{i,\mathrm{y}_i}+\mathrm{margin})/\tau\right)
}{
\exp\!\left(\mathrm{sim}(\theta_{i,\mathrm{y}_i}+\mathrm{margin})/\tau\right)
+ \sum_{u \ne \mathrm{y}_i}\exp\!\left(\mathrm{sim}(\theta_{i,u})/\tau\right)
},\\
\mathcal{L}_{\mathrm{embd}}^{\mathrm{joint}}
&=
\sum_{g \in \mathcal{G}}\lambda_g
\left(
-\frac{1}{|\mathcal{B}|}\sum_{i \in \mathcal{B}}
\log P(\mathrm{y}_i \mid \mathbf{h}_{i,1:g})
\right).
\end{aligned}
""",
    "pointwise": r"""
\begin{aligned}
\mathcal{E}_i &=
\mathrm{Concat}\!\left(
\mathcal{T}_{\mathrm{inst}},
\mathrm{q}_{\mathrm{txt}},\mathrm{q}_{\mathrm{img}},
\mathrm{d}_{i,\mathrm{txt}},\mathrm{d}_{i,\mathrm{img}}
\right),\\
\mathrm{s}_i
&= P\!\left(\texttt{Yes}\mid \mathcal{E}_i;
\Phi_{\mathrm{rank}}^{\mathrm{point}}\right),\\
\mathcal{L}_{\mathrm{rank}}^{\mathrm{point}}
&=
-\frac{1}{|\mathcal{B}|}\sum_{i \in \mathcal{B}}
\left[
\mathrm{y}_i\log \mathrm{s}_i
+(1-\mathrm{y}_i)\log(1-\mathrm{s}_i)
\right].
\end{aligned}
""",
    "chunk-input": r"""
\begin{aligned}
K &= \lceil N/M\rceil,\qquad
\mathcal{C}^{k}=\{\mathrm{d}_1,\ldots,\mathrm{d}_m\},\quad m \le M,\\
\mathcal{E} &=
\mathrm{Concat}\!\left(
\mathcal{T}_{\mathrm{inst}},
\mathrm{q}_{\mathrm{txt}},\mathrm{q}_{\mathrm{img}},
\mathrm{d}_{1,\mathrm{txt}},\mathrm{d}_{1,\mathrm{img}},
\ldots,
\mathrm{d}_{m,\mathrm{txt}},\mathrm{d}_{m,\mathrm{img}}
\right),\\
\mathbf{s} &=
\left(\mathrm{s}_1,\ldots,\mathrm{s}_m,\mathrm{s}_{\texttt{null}}\right)
\in \mathbb{R}^{m+1}.
\end{aligned}
""",
    "chunk-losses": r"""
\begin{aligned}
\mathcal{P} &= \{(i,j)\mid \mathrm{y}_i>\mathrm{y}_j\},\\
\mathcal{L}_{\mathrm{rank}}^{\mathrm{pair}}
&=
\frac{1}{|\mathcal{P}|}\sum_{(i,j)\in\mathcal{P}}
w_{ij}\log\!\left(
1+\exp\!\left(-\frac{\mathrm{s}_j-\mathrm{s}_i}{\tau}\right)
\right),\\
w_{ij} &= \max(\mathrm{y}_i-\mathrm{y}_j,1),\\
\mathcal{S} &= \{i\mid \mathrm{y}_i=0\},\qquad
\mathcal{O}=\{i\mid \mathrm{y}_i>0\},\\
\mathcal{L}_{\mathrm{rank}}^{\mathrm{null}}
&=
\frac{1}{|\mathcal{S}|}\sum_{i\in\mathcal{S}}
\log\!\left(1+\exp\!\left(-\frac{\mathrm{s}_i-\mathrm{s}_{\texttt{null}}}{\tau}\right)\right)\\
&\quad+
\frac{1}{|\mathcal{O}|}\sum_{i\in\mathcal{O}}
\log\!\left(1+\exp\!\left(-\frac{\mathrm{s}_{\texttt{null}}-\mathrm{s}_i}{\tau}\right)\right),\\
\mathcal{L}_{\mathrm{rank}}^{\mathrm{chunk}}
&=
\frac{1}{K}\sum_{k=1}^{K}
\left(
\mathcal{L}_{\mathrm{rank}}^{k,\mathrm{pair}}
+\mathcal{L}_{\mathrm{rank}}^{k,\mathrm{null}}
\right).
\end{aligned}
""",
    "absolute-relevance": r"""
\begin{aligned}
\mathrm{p}_i &=
\Phi_{\mathrm{MLP}}\!\left(
\left[\mathbf{z}_0 \,\middle\|\, \mathbf{z}_i\right]
\right)
\in \mathbb{R}^{4},
\qquad
\mathrm{r}_i=\mathrm{softmax}(\mathrm{p}_i),\\
\mathcal{L}_{\mathrm{rank}}^{\mathrm{abs}}
&=
-\frac{1}{|\mathcal{B}|}\sum_{i\in\mathcal{B}}
\log \mathrm{r}_{i,\mathrm{y}_i},\\
\mathcal{L}_{\mathrm{rank}}
&=
\mathcal{L}_{\mathrm{rank}}^{\mathrm{ntp}}
+\mathcal{L}_{\mathrm{rank}}^{\mathrm{chunk}}
+\mathcal{L}_{\mathrm{rank}}^{\mathrm{abs}}.
\end{aligned}
""",
    "hybrid-merge": r"""
\begin{aligned}
\mathrm{d}^{k}_1,\mathrm{d}^{k}_2,\ldots,\mathrm{d}^{k}_m
&\quad\text{s.t.}\quad
\mathrm{s}^{k}_1 \ge \mathrm{s}^{k}_2 \ge \cdots \ge \mathrm{s}^{k}_m,\\
k^\star
&=
\arg\max_{k:\,\mathrm{t}_k\le m}
\mathrm{r}^{k}_{\mathrm{t}_k}.
\end{aligned}
""",
}


TEMPLATE = r"""
\documentclass[12pt]{article}
\usepackage[paperwidth=180mm,paperheight=95mm,margin=0mm]{geometry}
\usepackage{amsmath,amssymb,bm}
\usepackage[active,tightpage]{preview}
\PreviewEnvironment{equation*}
\PreviewBorder=1pt
\pagestyle{empty}
\begin{document}
\begin{equation*}
%s
\end{equation*}
\end{document}
"""


def require(cmd: str) -> str:
    resolved = shutil.which(cmd)
    if not resolved:
        raise SystemExit(f"missing required command: {cmd}")
    return resolved


def render_formula(name: str, formula: str) -> None:
    latex = require("latex")
    dvisvgm = require("dvisvgm")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"pailitao-{name}-") as tmp:
        tmp_path = Path(tmp)
        tex_path = tmp_path / f"{name}.tex"
        dvi_path = tmp_path / f"{name}.dvi"
        out_path = OUT_DIR / f"{name}.svg"
        tex_path.write_text(TEMPLATE % formula.strip(), encoding="utf-8")
        subprocess.run(
            [latex, "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
            cwd=tmp_path,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )
        subprocess.run(
            [
                dvisvgm,
                "--no-fonts",
                "--exact-bbox",
                f"--output={out_path}",
                str(dvi_path),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )


def main() -> None:
    for name, formula in FORMULAS.items():
        render_formula(name, formula)
    print(f"rendered {len(FORMULAS)} formula SVGs in {OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
