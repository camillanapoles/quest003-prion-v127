"""F5 gate — render MD modular (1 arquivo/capítulo + índice) + integração total do grafo.

Regras:
  - A partição modular é EXATA: concat(files) == render_md single-file (byte a byte).
  - SUMARIO.md lista capítulos com links, contagens de blocos/seções/claims/tiers.
  - check_bindings: FKs válidas · claims ⊆ registro · evidências ⊆ fontes · §refs
    resolvem (labels ∪ nº-capítulos ∪ 2 refs-legadas documentadas do braço-paper).
"""
from pathlib import Path

import pytest
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.integrity import check_bindings
from thesis_engine.models import Block
from thesis_engine.render.md import render_md
from thesis_engine.render.modular import render_modular


@pytest.fixture(scope="module")
def loaded(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    ingest_registro(db_path=db_path)
    ingest_tese(db_path=db_path)
    return db_path


@pytest.fixture(scope="module")
def rendered(loaded, tmp_path_factory):
    out_dir = str(tmp_path_factory.mktemp("build") / "tese")
    report = render_modular(loaded, out_dir)
    return out_dir, report


def test_particao_modular_exata(loaded, rendered):
    """GATE: concat dos arquivos de capítulo == render single (byte a byte)."""
    out_dir, report = rendered
    files = sorted(Path(out_dir).glob("[0-9][0-9]-*.md"))
    concat = "".join(f.read_text(encoding="utf-8") for f in files)
    assert concat == render_md(loaded)


def test_um_arquivo_por_capitulo_e_sumario(rendered):
    out_dir, report = rendered
    files = sorted(f.name for f in Path(out_dir).glob("[0-9][0-9]-*.md"))
    assert len(files) == 17
    assert (Path(out_dir) / "SUMARIO.md").exists()
    names = " ".join(files)
    assert "07-capitulo-7-metodos" in names and "05-capitulo-5-fundamento" in names
    assert "12-capitulo-12-limitacoes" in names and "apendice" in names


def test_sumario_integrado(rendered):
    """Índice liga todos os capítulos e reporta claims/tiers (blocos integrados)."""
    out_dir, report = rendered
    sumario = (Path(out_dir) / "SUMARIO.md").read_text(encoding="utf-8")
    for f in sorted(Path(out_dir).glob("[0-9][0-9]-*.md")):
        assert f.name in sumario, f"SUMARIO sem link para {f.name}"
    # capítulo da dose traz suas claims e tier
    assert "C058" in sumario and "SIM-planejamento" in sumario
    # totais batem com o grafo
    assert report["total_claims"] >= 27  # 27 claims distintas citadas no canônico


def test_gate_bindings_verde_com_legado_documentado(loaded):
    report = check_bindings(loaded)
    assert report["ok"] is True
    assert set(report["refs"]["legacy"]) == {"1-bis", "2-bis"}  # validadas PR#2
    assert not report["refs"]["dangling"]


def test_gate_bindings_detecta_ref_fantasma(loaded):
    """§ref nova sem header → gate FALHA (anti-dangling; o fix do fractal, mecânico)."""
    with Session(create_db(loaded)) as s:
        b = s.exec(select(Block).where(Block.block_id == "B0001")).one()
        original = list(b.cross_refs)
        b.cross_refs = original + ["9.9"]
        s.add(b)
        s.commit()
    try:
        with pytest.raises(ValueError, match="9.9"):
            check_bindings(loaded)
    finally:
        with Session(create_db(loaded)) as s:
            b2 = s.get(Block, "B0001")
            b2.cross_refs = original
            s.add(b2)
            s.commit()
    assert check_bindings(loaded)["ok"] is True


def test_drafts_nao_vazam_no_modular(loaded, rendered):
    with Session(create_db(loaded)) as s:
        max_seq = s.exec(select(Block.seq)).all()
        nb = Block(
            block_id="D9999",
            seq=max(max_seq) + 1,
            block_type="paragraph",
            chap_id="c06",
            sec_id="c06s02",
            content="DRAFT-NAO-VAZA modular\n",
            status="draft",
            function="result",
            blueprint="B4",
        )
        s.add(nb)
        s.commit()
    try:
        out_dir2 = rendered[0] + "_x"
        render_modular(loaded, out_dir2)
        all_text = "".join(
            f.read_text(encoding="utf-8") for f in Path(out_dir2).glob("*.md")
        )
        assert "DRAFT-NAO-VAZA" not in all_text
    finally:
        with Session(create_db(loaded)) as s:
            d = s.get(Block, "D9999")
            s.delete(d)
            s.commit()
