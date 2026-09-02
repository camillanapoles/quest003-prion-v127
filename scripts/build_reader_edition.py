#!/usr/bin/env python3
"""build_reader_edition.py — A EDIÇÃO DE LEITURA (o produto textual da tese).
Transforma o mestre-gated (tese_unificada.md, superfície de auditoria) num LIVRO:
  1. Numeração só do LaTeX: títulos perdem "CAPÍTULO N —" e "N.M";
  2. ZERO tags no corpo: [claim/evidence] → removidas (provenance = apêndice concordância);
  3. Working-docs fora do corpo (B.1-B.4 cortados; B.5 objeções mantidas como apêndice);
  4. Floats [htbp] + raggedbottom (sem páginas órfãs);
  5. Citações numéricas → \\cite reais (regra hard paper-spine).
O mestre NÃO é alterado — guardian/AST continuam valendo nele."""
import re, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FP = ROOT / "paper_rewriting_output" / "final_paper"
MD = FP / "tese_unificada.md"
OUT = FP / "main.tex"

md = MD.read_text(encoding="utf-8")

# ── 1. fatia corpo vs apêndices ──
body = md[md.index("# CAPÍTULO 1 — NOTA INTRODUTÓRIA"):md.index("# REFERÊNCIAS")]
refs = md[md.index("# REFERÊNCIAS"):md.index("### Fontes complementares")]
apA = md[md.index("# APÊNDICE A"):md.index("### Fontes complementares")] if "# APÊNDICE A" in md else ""
apB5 = ""
if "## B.5 Prejulgando objeções" in md:
    apB5 = md[md.index("## B.5 Prejulgando objeções"):]
    apB5 = apB5[:apB5.index("\n---\n")] if "\n---\n" in apB5 else apB5

front_nota = md[md.index("> ## NOTA À LEITURA"):md.index("\n## RESUMO")]
front_resumo = md[md.index("## RESUMO"):md.index("\n## ABSTRACT")]
front_siglas = md[md.index("## LISTA DE SIGLAS"):md.index("\n---\n\n# CAPÍTULO 1")]

# ── 2. LIMPEZA DE LEITURA ──
def reader(text):
    # 2a. títulos sem número (LaTeX numera)
    text = re.sub(r"^# CAPÍTULO \d+ — ", "# ", text, flags=re.M)
    text = re.sub(r"^#{2,3} \d+\.\d+(?:-bis)?\s+", "", text, flags=re.M)  # remove "## N.M " do título
    # 2b. ZERO tags no corpo (audit trail vive no registro+concordância)
    text = re.sub(r"\s*\[claim:[^\]]+\]", "", text)
    text = re.sub(r"\s*\[evidence:[^\]]+\]", "", text)
    # 2c. refs a seções: "§N.M" → "\S N.M" (bate com auto-numeração LaTeX)
    text = re.sub(r"§(\d+\.\d+(?:-bis)?)", r"seção \1", text)
    # 2d. citações numéricas → \cite{eN} (regra hard: nunca colchete morto)
    text = re.sub(r"\[(\d{1,2})\]", lambda m: "\\cite{e%s}" % m.group(1), text)
    # 2e. TODO da casa → display-safe
    text = re.sub(r"\{\{TODO:([^:}]+):[^}]*\}\}", r"〔a preencher pela autora: \1〕", text)
    return text

body, front_nota, front_resumo, front_siglas, apB5 = map(reader, (body, front_nota, front_resumo, front_siglas, apB5))

# ── 3. refs: [n] → \cite{eN}; lista → thebibliography ──
refs_cited = re.sub(r"\[(\d{1,2})\]", lambda m: r"\cite{e%s}" % m.group(1), reader(body))
entries = re.findall(r"^\[(\d{1,2})\]\s+(.+)$", refs, re.M)
bib = ["\\bibitem{e%s} %s" % (n, t.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_"))
       for n, t in sorted(entries, key=lambda x: int(x[0]))]

# ── 4. pandoc (capítulos; math $$ preservado) ──
def pandoc(text):
    return subprocess.run(["pandoc", "-f", "markdown", "-t", "latex", "--top-level-division=chapter"],
                          input=text.encode(), capture_output=True, check=True).stdout.decode()

tex_nota, tex_resumo, tex_siglas, tex_body, tex_b5 = map(pandoc, (front_nota, front_resumo, front_siglas, body, apB5))
for tex in (tex_body,):
    pass
# floats [htbp] (lambda: replacement literal — \b de "\begin" não pode passar pelo motor de escapes)
tex_body = re.sub(r"\\begin\{figure\}(?!\[)", lambda m: "\\begin{figure}[htbp]", tex_body)
tex_body = re.sub(r"\\begin\{table\}(?!\[)", lambda m: "\\begin{table}[htbp]", tex_body)
# includegraphics: garante width; remove chaves/keys não-graphicx do pandoc (alt=)
def _gfx(m):
    opts = m.group(1) or ""
    opts = re.sub(r"alt=\{[^}]*\},?", "", opts).strip().rstrip(",")
    if "width" not in opts:
        opts = ("width=0.9\\textwidth," + opts).rstrip(",")
    return "\\includegraphics[" + opts + "]{"
tex_body = re.sub(r"\\includegraphics(?:\[([^\]]*)\])?\{", _gfx, tex_body)

main = r"""% ══════════════════════════════════════════════════════════════════
% ETRIZAÇÃO COMPUTACIONAL EM DOENÇAS PRIÔNICAS — EDIÇÃO DE LEITURA
% Gerado por scripts/build_reader_edition.py a partir do mestre-gated
% (tese_unificada.md · guardian 0/0 · AST 10/10). NÃO editar à mão.
% Numeração: só LaTeX · zero tags no corpo · provenance no apêndice.
% ══════════════════════════════════════════════════════════════════
\documentclass[12pt,a4paper,oneside]{report}
\usepackage[brazil]{babel}\usepackage{fontspec}\setmainfont{TeX Gyre Termes}
\usepackage[a4paper,top=3cm,bottom=2cm,left=3cm,right=2cm]{geometry}
\usepackage{amsmath,amssymb,graphicx,booktabs,longtable,microtype}
\usepackage{array,calc,xcolor}
\providecommand{\tightlist}{\setlength{\itemsep}{2pt}\setlength{\parskip}{0pt}}
\usepackage{caption}\captionsetup{font=small,labelfont=bf,skip=6pt}
\usepackage[htbp]{float}
\usepackage{fancyhdr}\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small\itshape Etrização computacional em doenças priônicas}
\fancyhead[R]{\small\thepage}\renewcommand{\headrulewidth}{0.3pt}\setlength{\headheight}{15pt}
\raggedbottom
\providecommand{\pandocbounded}[1]{#1}
\usepackage{newunicodechar}
\newunicodechar{↔}{\ensuremath{\leftrightarrow}}\newunicodechar{∂}{\ensuremath{\partial}}
\newunicodechar{∇}{\ensuremath{\nabla}}\newunicodechar{✅}{\ensuremath{\checkmark}}
\newunicodechar{⚠}{\textbf{!}}\newunicodechar{⁻}{\ensuremath{^{-}}}\newunicodechar{⇒}{\ensuremath{\Rightarrow}}\newunicodechar{→}{\ensuremath{\to}}\newunicodechar{↦}{\ensuremath{\mapsto}}\newunicodechar{∝}{\ensuremath{\propto}}\newunicodechar{≈}{\ensuremath{\approx}}\newunicodechar{≡}{\ensuremath{\equiv}}\newunicodechar{∴}{\therefore}\newunicodechar{️}{}\newunicodechar{〔}{}\newunicodechar{〕}{}
\usepackage[colorlinks=true,linkcolor=black,citecolor=black,urlcolor=blue,
pdftitle={Etrização Computacional em Doenças Priônicas: Aplicada à Plataforma Terapêutica PrP-V127},
pdfauthor={Camilla N.}]{hyperref}
\title{Etrização Computacional em Doenças Priônicas:\\Aplicada à Plataforma Terapêutica PrP-V127}
\author{Camilla N.}\date{2026}
\begin{document}
\maketitle
""" + tex_resumo.replace("\\chapter{RESUMO}", "\\chapter*{Resumo}").replace("\\section{RESUMO}", "\\chapter*{Resumo}") + r"""
""" + tex_nota.replace("\\chapter{NOTA", "\\chapter*{Nota") + r"""
\tableofcontents
\listoffigures
\listoftables
""" + tex_siglas + r"""
""" + tex_body + r"""
\nocite{*}
\begin{thebibliography}{99}\setlength{\itemsep}{1pt}
""" + "\n".join(bib) + r"""
\end{thebibliography}
\appendix
""" + tex_b5 + r"""
\end{document}
"""
OUT.write_text(main, encoding="utf-8")
n_ch = len(re.findall(r"\\chapter\{", main))
print(f"→ {OUT.name}: {len(main.splitlines())} linhas · {n_ch} capítulos (títulos SEM número) · {len(bib)} refs · "
      f"tags no corpo: {len(re.findall(r'claim:|evidence:', main))}")
