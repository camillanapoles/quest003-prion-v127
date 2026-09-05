"""Ledger de débitos F2.5 — cada bug capturado vira teste de regressão PERMANENTE.

R1 colisão de prefixo CAPÍTULO 1×10/11/12 (mapa de blueprint)
R2 extrator perdia tier [SIM-planejamento] do heading §6.3 (hífen interno)
R3 G3 devia discriminar saída-de-dose (B4) de menção narrativa
"""
import pytest
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.integrity import check_style
from thesis_engine.models import Block, Chapter


@pytest.fixture(scope="module")
def loaded(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    ingest_registro(db_path=db_path)
    ingest_tese(db_path=db_path)
    return db_path


def _chapters(db_path):
    with Session(create_db(db_path)) as s:
        return s.exec(select(Chapter)).all()


def test_R1_prefixo_capitulo_nao_colide(loaded):
    """CAPÍTULO 1 NÃO pode capturar CAPÍTULO 10/11/12/13 (c10→B6, c13→B8)."""
    with Session(create_db(loaded)) as s:
        blocks = s.exec(select(Block)).all()
        by_frag = {}
        for c in _chapters(loaded):
            bp = {b.blueprint for b in blocks if b.chap_id == c.chap_id}
            by_frag[c.title[:11]] = bp
    assert by_frag["CAPÍTULO 10"] == {"B6"}  # era B1 (colisão)
    assert by_frag["CAPÍTULO 11"] == {"B7"}
    assert by_frag["CAPÍTULO 12"] == {"B8"}
    assert by_frag["CAPÍTULO 13"] == {"B8"}


def test_R2_tier_do_heading_63_extraido(loaded):
    """O heading §6.3 termina em [SIM-planejamento] (hífen interno) — DEVE extrair."""
    with Session(create_db(loaded)) as s:
        h = s.exec(
            select(Block).where(
                Block.block_type == "heading", Block.heading_text.contains("6.3")
            )
        ).one()
        assert "SIM-planejamento" in h.tiers, f"tier perdido de novo: {h.heading_text!r}"
        assert h.sec_id == "c06s02"


def test_R3_g3_protege_b4_e_nao_flagga_narrativa(loaded):
    """G3: menção narrativa (§1.2, B1) NÃO exige tier; B4 sem tier FALHA."""
    # canônico: verde (menções em B1/B6/B7 não travam; B4 tem tier no heading §6.3)
    assert check_style(loaded)["ok"] is True
    # tamper ADVERSARIAL: zerar tiers de TODOS os blocos da c06s02
    # (redundância: remover um só NÃO quebra — por design; todos → G3 FALHA)
    with Session(create_db(loaded)) as s:
        sec_blocks = s.exec(select(Block).where(Block.sec_id == "c06s02")).all()
        originais = [(b.block_id, list(b.tiers)) for b in sec_blocks]
        assert any(t for _, t in originais), "c06s02 deveria ter tiers no canônico"
        for b in sec_blocks:
            b.tiers = []
            s.add(b)
        s.commit()
    try:
        with pytest.raises(ValueError, match="c06s02|tier"):
            check_style(loaded)
    finally:
        with Session(create_db(loaded)) as s:
            for bid, tiers in originais:
                b = s.get(Block, bid)
                b.tiers = tiers
                s.add(b)
            s.commit()
    assert check_style(loaded)["ok"] is True
