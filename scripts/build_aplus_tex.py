#!/usr/bin/env python3
"""build_aplus_tex.py — edição A+ (padrão-publicação) da tese unificada.
Determinístico: md-mestre (gated) → pandoc → cirurgia-de-texto → main.tex (classe report,
capítulos, TOC/LOF/LOT, \\cite reais em thebibliography, tags-da-casa como superscript de auditoria).
Regras hard do paper-spine/latex.md: \\title+\\maketitle ✓ · \\cite em toda citação numérica ✓ · paper.pdf alias no CI ✓."""
import os, re, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FP = ROOT / "paper_rewriting_output" / "final_paper"
MD = FP / "tese_unificada.md"
OUT = FP / "main.tex"

md = MD.read_text(encoding="utf-8")

# ── 1. fatias estruturais do mestre ──
def cut(text, start, end=None):
    i = text.index(start)
    j = text.index(end) if end else len(text)
    return text[i:j]

front_nota = cut(md, "> ## NOTA À LEITURA", "\n## RESUMO")
front_resumo = cut(md, "## RESUMO", "\n## ABSTRACT")
front_siglas = cut(md, "## LISTA DE SIGLAS", "\n---\n\n# CAPÍTULO 1")
body = cut(md, "# CAPÍTULO 1 — NOTA INTRODUTÓRIA", "\n# REFERÊNCIAS")
refs_block = cut(md, "# REFERÊNCIAS", "\n### Fontes complementares")
tail = md[md.index("\n### Concordância claims"):]  # concordância + apêndices

# ── 2. transformações comuns ──
def common(text):
    text = re.sub(r"\{\{TODO:([^:}]+):[^}]*\}\}", r"〔a preencher pela autora: \1〕", text)
    # tags-da-casa → macro de auditoria: [claim:Cxxx] [evidence:E1, E2] → \audit{Cxxx}{E1,E2}
    def audit(m):
        tag = "C" + m.group(1)
        ev = m.group(2) or ""
        return "\\audit{%s}{%s}" % (tag, ev)
    text = re.sub(r"\[claim:C(\d+)\](?:\s*\[evidence:([^\]]+)\])?", audit, text)
    text = re.sub(r"\[evidence:([^\]]+)\]", lambda m: "\\audit{E}{%s}" % m.group(1), text)
    # citações numéricas literais → \cite{eN} (regra hard: nunca colchete morto)
    text = re.sub(r"\[(\d{1,2})\]", lambda m: r"\cite{e%s}" % m.group(1), text)
    return text

front_nota, front_resumo, front_siglas, body, tail = map(common,
    (front_nota, front_resumo, front_siglas, body, tail))

# ── 3. extrai as [n] refs do bloco CRU (antes de qualquer transformação) → thebibliography ──
entries = re.findall(r"^\[(\d{1,2})\]\s+(.+)$", refs_block, re.M)
bib_lines = []
for n, rest in sorted(entries, key=lambda x: int(x[0])):
    txt = rest.strip()
    txt = txt.replace(r"\&", "&").replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")
    bib_lines.append("\\bibitem{e%s} %s" % (n, txt))
bibliography = ("\\begin{thebibliography}{99}\n\\setlength{\\itemsep}{1pt}\n"
                + "\n".join(bib_lines) + "\n\\end{thebibliography}")

# ── 4. pandoc por fatia (matemática $$ preservada; --top-level-division=chapter) ──
def pandoc(text, extra=None):
    p = subprocess.run(["pandoc", "-f", "markdown", "-t", "latex", "--top-level-division=chapter"]
                       + (extra or []), input=text.encode(), capture_output=True, check=True)
    return p.stdout.decode()

tex_nota = pandoc(front_nota)
tex_resumo = pandoc(front_resumo)
tex_siglas = pandoc(front_siglas)
tex_body = pandoc(body)
tex_tail = pandoc(tail)

# pós: figuras com largura controlada + glifos ausentes já no preamble
for tex in [tex_body]:
    pass
tex_body = tex_body.replace("\\includegraphics{", "\\includegraphics[width=0.92\\textwidth]{")
tex_tail = tex_tail.replace("\\includegraphics{", "\\includegraphics[width=0.92\\textwidth]{")

# ── 5. monta o main.tex A+ ──
main = r"""% =====================================================================
% EDITION A+ (padrão-publicação) — gerado DETERMINISTICAMENTE por
% scripts/build_aplus_tex.py a partir de tese_unificada.md (mestre gated).
% Não editar à mão: regenerar (local ou CI) após mudar o mestre.
% =====================================================================
\documentclass[12pt,a4paper]{report}
\usepackage{polyglossia}\setmainlanguage{brazil}\setmainfont{TeX Gyre Termes}
\usepackage[a4paper,top=3cm,bottom=2cm,left=3cm,right=2cm]{geometry}
\usepackage{amsmath,amssymb}\usepackage{graphicx}\usepackage{booktabs}\usepackage{longtable}
\usepackage{caption}\captionsetup{font=small,labelfont=bf,skip=6pt}
\usepackage{fancyhdr}\pagestyle{fancy}\fancyhf{}
\fancyhead[LE]{\small\itshape Etrização computacional em doenças priônicas}
\fancyhead[RO]{\small\itshape\nouppercase{\leftmark}}\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0.3pt}\setlength{\headheight}{15pt}
\usepackage{microtype}
\usepackage{newunicodechar}
\newunicodechar{↔}{\ensuremath{\leftrightarrow}}\newunicodechar{∂}{\ensuremath{\partial}}
\newunicodechar{∇}{\ensuremath{\nabla}}\newunicodechar{✅}{\ensuremath{\checkmark}}
\newunicodechar{⚠}{\textbf{!}}\newunicodechar{️}{}
\newunicodechar{〔}{}\newunicodechar{〕}{}
\definecolor{auditcol}{gray}{0.45}
\newcommand{\audit}[2]{\textsuperscript{\tiny\textcolor{auditcol}{#1·#2}}}
\usepackage[colorlinks=true,linkcolor=black,citecolor=black,urlcolor=blue,
pdftitle={Etrização Computacional em Doenças Priônicas: Aplicada à Plataforma Terapêutica PrP-V127},
pdfauthor={Camilla N.}]{hyperref}
\title{Etrização Computacional em Doenças Priônicas:\\Aplicada à Plataforma Terapêutica PrP-V127}
\author{Camilla N.}
\date{2026}
\begin{document}
\maketitle
\begin{abstract}""" + tex_resumo.replace("\\section{RESUMO}", "").replace("\\section*{RESUMO}", "") + r"""\end{abstract}
""" + tex_nota + r"""
\tableofcontents
\listoffigures
\listoftables
""" + tex_siglas + r"""
""" + tex_body + r"""
""" + bibliography + r"""
\appendix
""" + tex_tail + r"""
\end{document}
"""
OUT.write_text(main, encoding="utf-8")
print("→", OUT, f"({len(main.splitlines())} linhas; {len(bib_lines)} bibitems; \\cite no corpo: {tex_body.count(chr(92)+'cite{')+tex_tail.count(chr(92)+'cite{')})")
