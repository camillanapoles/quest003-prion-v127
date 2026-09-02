"""F2 gate — parser tese_unificada.md → blocos tipados + round-trip idêntico.

Regra de ouro do Modo A (conservação): a partição de blocos cobre o arquivo INTEIRO,
byte a byte; render = concatenação em ordem. Qualquer divergência = gate FALHA.
"""
from pathlib import Path

import pytest
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.models import Block, Chapter, Claim, Section
from thesis_engine.render.md import render_md

TESE_MD = Path(__file__).resolve().parents[1] / "paper_rewriting_output" / "final_paper" / "tese_unificada.md"


@pytest.fixture(scope="module")
def loaded(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    ingest_registro(db_path=db_path)  # registro primeiro (F1)
    ingest_tese(db_path=db_path)  # blocos (F2) — não toca nas tabelas do registro
    return db_path


def test_round_trip_byte_identico(loaded):
    """GATE CENTRAL: MD → parse → DB → render == original (byte a byte)."""
    original = TESE_MD.read_text(encoding="utf-8")
    assert render_md(loaded) == original


def test_particao_cobre_arquivo_inteiro(loaded):
    original = TESE_MD.read_text(encoding="utf-8")
    with Session(create_db(loaded)) as s:
        blocks = s.exec(select(Block).order_by(Block.seq)).all()
    assert sum(len(b.content) for b in blocks) == len(original)
    assert "".join(b.content for b in blocks) == original  # contígua, sem sobreposição


def test_estrutura_e_contagens(loaded):
    with Session(create_db(loaded)) as s:
        chapters = s.exec(select(Chapter).order_by(Chapter.order_idx)).all()
        sections = s.exec(select(Section)).all()
        blocks = s.exec(select(Block)).all()
        by_type: dict[str, int] = {}
        for b in blocks:
            by_type[b.block_type] = by_type.get(b.block_type, 0) + 1
    assert len(chapters) == 17  # título + 13 caps + REFERÊNCIAS + APÊNDICE A + B + C–F
    assert len(sections) == 59  # h2 + h3
    assert by_type.get("heading") == 17 + 59
    assert by_type.get("figure") == 2
    assert by_type.get("table") >= 10
    assert by_type.get("math") >= 1
    assert by_type.get("quote") >= 1
    assert by_type.get("list") >= 10
    assert by_type.get("hr") == 24
    # capítulos-chave presentes com títulos íntegros
    titles = " | ".join(c.title for c in chapters)
    assert "CAPÍTULO 7" in titles and "REFERÊNCIAS" in titles and "APÊNDICE B" in titles


def test_claims_citadas_existem_no_registro(loaded):
    """Vínculo no grafo: todo [claim:] da tese é uma claim registrada (F1)."""
    with Session(create_db(loaded)) as s:
        registered = {c.claim_id for c in s.exec(select(Claim)).all()}
        blocks = s.exec(select(Block)).all()
    cited = {cid for b in blocks for cid in b.claim_ids}
    assert cited  # não-vazio
    orphan = cited - registered
    assert not orphan, f"claims citadas sem registro: {sorted(orphan)}"


def test_tags_expandidas_e_extraidas(loaded):
    """Ranges C058–C060 → C058,C059,C060 · [evidence:] · tiers · §refs."""
    with Session(create_db(loaded)) as s:
        blocks = s.exec(select(Block)).all()
    # range expandida em algum bloco
    expanded = [b for b in blocks if set(b.claim_ids) >= {"C058", "C059", "C060"}]
    assert expanded, "range C058–C060 não foi expandida"
    # evidence tags
    assert any(b.evidence_ids for b in blocks)
    # tier SIM-planejamento detectado (não pode colapsar para [SIM])
    assert any("SIM-planejamento" in b.tiers for b in blocks)
    assert any("ORGANOID" in b.tiers for b in blocks)
    # §refs extraídas
    assert any(b.cross_refs for b in blocks)
    # blocos ficam dentro de capítulo/seção (exceto título e front-matter h1)
    assert all(b.chap_id for b in blocks if b.block_type == "heading" and b.seq > 0)


def test_secoes_numeradas_com_label(loaded):
    with Session(create_db(loaded)) as s:
        labels = {sec.label for sec in s.exec(select(Section)).all() if sec.label}
    assert {"7.1", "7.2", "5.1-bis", "B.1"} <= labels


def test_ingest_tese_idempotente(loaded):
    db_path = loaded
    with Session(create_db(db_path)) as s:
        n1 = len(s.exec(select(Block)).all())
    ingest_tese(db_path=db_path)
    with Session(create_db(db_path)) as s:
        n2 = len(s.exec(select(Block)).all())
        # tabelas do registro intactas
        from sqlmodel import func, col

        n_claims = len(s.exec(select(Claim)).all())
    assert n1 == n2 and n_claims == 60
