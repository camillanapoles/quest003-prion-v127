"""Render LaTeX determinístico — 3 contratos (abnt · prova · kappa) do mesmo grafo.

Regra de ouro: .tex é artefato DESCARTÁVEL, regenerado a cada build; nunca editado à mão.
Determinismo por construção: mesma entrada (blocos canonico, ordem seq) → byte-idêntico.
Contratos e mapeamentos: PADRAO_F6_ESTILO.md.
"""
import re
from pathlib import Path

from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.models import Block

_ESC = {"&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}"}
_MATH = re.compile(r"\$\$(.+?)\$\$", re.S)
_CLAIM = re.compile(r"\[claim:([^\]]+)\]")
_EVID = re.compile(r"\[evidence:([^\]]+)\]")
_LIST_ITEM = re.compile(r"^(?:- |\* |(\d+)\. )")


def _esc(text: str) -> str:
    out = []
    for ch in text:
        out.append(_ESC.get(ch, ch))
    return "".join(out).replace("~", r"\textasciitilde{}").replace("^", r"\textasciicircum{}")


def _inline(text: str, audit: bool) -> str:
    """Escapa texto preservando math $$ e convertendo tags de auditoria."""
    math_parts: list[str] = []

    def _stash(m):
        math_parts.append(m.group(1))
        return f"\x00MATH{len(math_parts) - 1}\x00"

    t = _MATH.sub(_stash, text)
    t = _esc(t)
    if audit:
        t = _CLAIM.sub(lambda m: r"\audit{" + m.group(1).replace("–", "-") + "}", t)
        t = _EVID.sub(lambda m: r"\evref{" + m.group(1) + "}", t)
    else:
        t = _CLAIM.sub(lambda m: r"\textsuperscript{[" + m.group(1).replace("–", "-") + "]}", t)
        t = _EVID.sub(lambda m: r"\textsuperscript{[" + m.group(1) + "]}", t)
    for i, mp in enumerate(math_parts):
        t = t.replace(f"\x00MATH{i}\x00", f"${_esc_math(mp)}$")
    return t


def _esc_math(m: str) -> str:
    return m  # conteúdo $$ já é LaTeX do canônico


def _table_latex(content: str, audit: bool) -> str:
    lines = [l for l in content.strip().split("\n") if l.strip().startswith("|")]
    if not lines:
        return ""
    rows = []
    for l in lines:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue  # separador
        rows.append(cells)
    if not rows:
        return ""
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    spec = "|" + "l|" * ncols
    body = " \\\\\n    ".join(
        " & ".join(_inline(c, audit) for c in r) for r in rows
    )
    return (
        "\\begin{center}\n\\small\n\\begin{tabular}{" + spec + "}\n    \\hline\n    "
        + body + " \\\\\n    \\hline\n\\end{tabular}\n\\end{center}\n"
    )


def _figure_latex(content: str) -> str:
    m = re.match(r"!\[(.*)\]\((.*)\)", content.strip())
    if not m:
        return _inline(content.strip(), True) + "\n"
    alt, path = m.group(1), m.group(2)
    return (
        "\\begin{figure}[htbp]\n\\centering\n"
        f"\\includegraphics[width=0.92\\linewidth]{{{path}}}\n"
        f"\\caption{{{_inline(alt, True)}}}\n\\end{{figure}}\n"
    )


def _blocks_to_body(blocks: list[Block], h1: str, h2: str, h3: str, audit: bool) -> str:
    out: list[str] = []
    for b in blocks:
        c = b.content
        if b.block_type == "blank":
            continue
        if b.block_type == "heading":
            lvl = b.heading_level or 1
            cmd = {1: h1, 2: h2, 3: h3}.get(lvl, h3)
            out.append(f"\\{cmd}{{{_inline(b.heading_text or '', False)}}}\n")
        elif b.block_type == "table":
            out.append(_table_latex(c, audit))
        elif b.block_type == "figure":
            out.append(_figure_latex(c))
        elif b.block_type == "math":
            inner = c.strip().strip("$")
            out.append(f"\\[{inner}\\]\n")
        elif b.block_type == "quote":
            q = "\n".join(l.lstrip("> ").rstrip() for l in c.strip().split("\n"))
            out.append("\\begin{quote}\n" + _inline(q, audit) + "\n\\end{quote}\n")
        elif b.block_type == "hr":
            out.append("\\noindent\\rule{\\linewidth}{0.4pt}\n")
        elif b.block_type == "list":
            ordered = bool(re.match(r"^\s*\d+\. ", c))
            env = "enumerate" if ordered else "itemize"
            items = []
            for l in c.strip().split("\n"):
                l = l.strip()
                m = _LIST_ITEM.match(l)
                if m:
                    items.append("  \\item " + _inline(l[m.end():], audit))
                elif l and items:
                    items[-1] += " " + _inline(l, audit)
            out.append(f"\\begin{{{env}}}\n" + "\n".join(items) + f"\n\\end{{{env}}}\n")
        else:  # paragraph
            out.append(_inline(c.strip(), audit) + "\n")
    return "\n".join(out)


# ---------------- contratos ----------------

def _preamble_abnt() -> str:
    return (
        "\\documentclass[12pt,a4paper,twoside]{abntex2}\n"
        "\\usepackage{graphicx,booktabs,longtable}\n"
        "\\usepackage[brazil]{babel}\n"
        "\\newcommand{\\audit}[1]{\\textsuperscript{[cl:#1]}}\n"
        "\\newcommand{\\evref}[1]{\\textsuperscript{[ev:#1]}}\n"
        "\\begin{document}\n"
        "\\pretextual\n\\imprimircapa\n\\imprimirfolhaderosto\n"
    )


def _preamble_prova() -> str:
    return (
        "\\documentclass[11pt,oneside]{memoir}\n"
        "\\usepackage[brazil]{babel}\n"
        "\\usepackage{graphicx,booktabs}\n"
        "\\pagestyle{ruled}\n"
        "\\begin{document}\n"
    )


def _preamble_kappa() -> str:
    return (
        "\\documentclass[11pt,a4paper]{article}\n"
        "\\usepackage[brazil]{babel}\n"
        "\\usepackage{graphicx,booktabs,appendix}\n"
        "\\newcommand{\\audit}[1]{\\textsuperscript{[cl:#1]}}\n"
        "\\newcommand{\\evref}[1]{\\textsuperscript{[ev:#1]}}\n"
        "\\begin{document}\n"
    )


def render_latex(db_path: str, fmt: str = "abnt") -> str:
    """Gera o .tex completo de uma variante. fmt ∈ {abnt, prova, kappa}."""
    engine = create_db(db_path)
    with Session(engine) as s:
        blocks = s.exec(
            select(Block).where(Block.status == "canonico").order_by(Block.seq)
        ).all()
    by_chap: dict[str, list[Block]] = {}
    for b in blocks:
        by_chap.setdefault(b.chap_id or "c00", []).append(b)
    order = sorted(by_chap, key=lambda k: int(k[1:]))

    if fmt == "abnt":
        doc = [_preamble_abnt()]
        for k in order:
            doc.append(_blocks_to_body(by_chap[k], "chapter", "section", "subsection", True))
        doc.append("\\postextual\n\\end{document}\n")
    elif fmt == "prova":
        doc = [_preamble_prova()]
        for k in order:
            doc.append(_blocks_to_body(by_chap[k], "section*", "subsection*", "subsubsection*", False))
        doc.append("\\end{document}\n")
    elif fmt == "kappa":
        doc = [_preamble_kappa()]
        for k in order:
            if k in ("c14", "c15", "c16"):  # apêndices elevados a "papers"
                doc.append("\\appendix\n")
                doc.append(_blocks_to_body(by_chap[k], "section", "subsection", "subsubsection", True))
            else:
                doc.append(_blocks_to_body(by_chap[k], "section", "subsection", "subsubsection", True))
        doc.append("\\end{document}\n")
    else:
        raise ValueError(f"variante desconhecida: {fmt!r} ∈ {{abnt, prova, kappa}}")
    return "".join(doc)


def render_latex_all(db_path: str, out_dir: str = "build/latex") -> dict[str, str]:
    out = Path(out_dir)
    paths: dict[str, str] = {}
    for fmt in ("abnt", "prova", "kappa"):
        d = out / fmt
        d.mkdir(parents=True, exist_ok=True)
        p = d / "main.tex"
        p.write_text(render_latex(db_path, fmt), encoding="utf-8")
        paths[fmt] = str(p)
    return paths
