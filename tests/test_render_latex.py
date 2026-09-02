"""F6 gate — render LaTeX determinístico em 3 variantes (abnt · prova · kappa).

Gates: determinismo (render×2 byte-idêntico) · estrutura por variante ·
mesmo conteúdo canônico nas 3 (spine de headings idêntico) · variante inválida rejeitada.
"""
import pytest

from thesis_engine.ingest.experiments import ingest_experiments
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.render.latex import render_latex, render_latex_all


@pytest.fixture(scope="module")
def loaded(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    ingest_registro(db_path=db_path)
    ingest_tese(db_path=db_path)
    ingest_experiments(db_path=db_path)
    return db_path


@pytest.mark.parametrize("fmt", ["abnt", "prova", "kappa"])
def test_determinismo_byte_a_byte(loaded, fmt):
    """MESMA entrada → .tex IDÊNTICO (gate central da F6)."""
    assert render_latex(loaded, fmt) == render_latex(loaded, fmt)


def test_variante_abnt(loaded):
    tex = render_latex(loaded, "abnt")
    assert "\\documentclass[12pt,a4paper,twoside]{abntex2}" in tex
    assert "\\imprimircapa" in tex and "\\imprimirfolhaderosto" in tex
    assert tex.count("\\chapter{") == 17  # 17 H1 → 17 chapters ABNT
    assert "\\audit{" in tex  # evidence-binding auditável (camada top-5 nº5)
    assert "\\includegraphics" in tex  # Fig.4/5 auditáveis
    assert "\\begin{tabular}" in tex  # tabelas convertidas (não verbatim)
    assert "\\end{document}" in tex


def test_variante_prova(loaded):
    tex = render_latex(loaded, "prova")
    assert "{memoir}" in tex
    assert tex.count("\\section*{") == 17  # capítulos → seções compactas publicação-grade
    assert "\\textsuperscript{[C" in tex  # audit como superscript, não \audit
    assert "\\chapter" not in tex


def test_variante_kappa(loaded):
    tex = render_latex(loaded, "kappa")
    assert "{article}" in tex and "\\appendix" in tex
    # núcleo kappa: c14+ viram apêndices-paper DEPOIS do núcleo (rindex: a 1ª ocorrência
    # de REFER está no SUMÁRIO de c00; a última é o capítulo real)
    assert tex.index("\\appendix") < tex.rindex("REFER")
    assert tex.count("\\section{") + tex.count("\\section*{") >= 17


def test_mesma_fonte_tres_saidas(loaded):
    """As 3 variantes derivam do MESMO grafo: spine de headings idêntico."""
    import re

    def spine(tex):
        return re.findall(r"CAP[ÍI]TULO \d+", tex)

    assert spine(render_latex(loaded, "abnt")) == spine(render_latex(loaded, "prova")) == spine(
        render_latex(loaded, "kappa")
    )


def test_variante_invalida(loaded):
    with pytest.raises(ValueError, match="abnt, prova, kappa"):
        render_latex(loaded, "pdf")


def test_render_all_escreve_tres(loaded, tmp_path):
    paths = render_latex_all(loaded, str(tmp_path / "latex"))
    assert set(paths) == {"abnt", "prova", "kappa"}
    for p in paths.values():
        assert open(p, encoding="utf-8").read().startswith("\\documentclass")
