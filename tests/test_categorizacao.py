"""F2.5 gate — categorização OBRIGATÓRIA (§3.5) + write-guard + gates de estilo.

Contrato de dados para F4: todo bloco de conteúdo tem function∈ENUM e blueprint∈B0–B9;
escritas validam status; máquina JAMAIS seta author_approved; estilo calibrado no
canônico (94b792a — adversarialmente validado pela autora) e com detector de regressão.
"""
import pytest
from sqlmodel import Session, select

from thesis_engine.categorize import (
    BLUEPRINTS,
    FUNCTIONS,
    STATUS,
    apply_categorization,
    validate_block_write,
)
from thesis_engine.db import create_db
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.integrity import check_style
from thesis_engine.models import Block, Chapter


@pytest.fixture(scope="module")
def loaded(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    ingest_registro(db_path=db_path)
    ingest_tese(db_path=db_path)  # agora aplica categorização no fim do ingest
    return db_path


def _blocks(db_path):
    with Session(create_db(db_path)) as s:
        return s.exec(select(Block)).all(), s.exec(select(Chapter)).all()


STRUCTURAL = {"heading", "blank", "hr"}


def test_cobertura_total_da_categorizacao(loaded):
    """Todo bloco: blueprint∈B0–B9; todo bloco de CONTEÚDO: function∈ENUM."""
    blocks, _ = _blocks(loaded)
    assert blocks
    for b in blocks:
        assert b.blueprint in BLUEPRINTS, f"{b.block_id} blueprint={b.blueprint!r}"
        if b.block_type not in STRUCTURAL:
            assert b.function in FUNCTIONS, f"{b.block_id} function={b.function!r}"
        else:
            assert b.function is None


def test_blueprint_por_capitulo(loaded):
    blocks, chapters = _blocks(loaded)
    by_title = {c.title: c.chap_id for c in chapters}

    def bp_of(fragment):
        cid = next(v for k, v in by_title.items() if fragment in k)
        return {b.blueprint for b in blocks if b.chap_id == cid}

    assert bp_of("CAPÍTULO 4") == {"B2"}  # base comum
    assert bp_of("CAPÍTULO 5") == {"B3"}  # fundamento θ*
    assert bp_of("CAPÍTULO 6") == {"B4"}  # aplicação
    assert bp_of("CAPÍTULO 7") == {"B5"}  # etrização formalizada
    assert bp_of("CAPÍTULO 8") == {"B6"}  # resultados-validação
    assert bp_of("CAPÍTULO 11") == {"B7"}  # camada clínica
    assert bp_of("CAPÍTULO 12") == {"B8"}  # limitações-fruto
    assert bp_of("APÊNDICE B") == {"B9"}


def test_functions_inferidas(loaded):
    blocks, _ = _blocks(loaded)
    openers = [b for b in blocks if b.function == "clinical-opener"]
    assert len(openers) >= 3  # calibrado no canônico (c05/c06/c07)
    assert all(b.content.lstrip("*").startswith("Em linguagem clínica") for b in openers)
    # limitações: parágrafos do cap.12 → limitation
    lim = [b for b in blocks if b.function == "limitation"]
    assert lim and all(b.chap_id and "CAPÍTULO 12" for b in lim)
    # figuras são resultados
    figs = [b for b in blocks if b.block_type == "figure"]
    assert figs and all(b.function == "result" for b in figs)
    # blocos com claim fora dos caps dominados por nota/método/conclusão → result
    exempt = {"B1", "B5", "B8"}  # nota-à-banca, métodos e conclusões têm função própria
    assert all(
        b.function == "result"
        for b in blocks
        if b.claim_ids and b.block_type == "paragraph" and b.blueprint not in exempt
    )


def test_write_guard_status(loaded):
    """Máquina NUNCA seta author_approved; humana pode; enums inválidos rejeitados."""
    with pytest.raises(ValueError, match="author_approved"):
        validate_block_write(
            function="result", blueprint="B4", status="author_approved", is_human=False
        )
    # humana pode
    validate_block_write(
        function="result", blueprint="B4", status="author_approved", is_human=True
    )
    # enums inválidos
    with pytest.raises(ValueError, match="function"):
        validate_block_write(function="genial", blueprint="B4", status="draft")
    with pytest.raises(ValueError, match="blueprint"):
        validate_block_write(function="result", blueprint="B99", status="draft")
    with pytest.raises(ValueError, match="status"):
        validate_block_write(function="result", blueprint="B4", status="pronto")
    # bloco de conteúdo SEM function é rejeitado (categorização obrigatória)
    with pytest.raises(ValueError, match="function"):
        validate_block_write(function=None, blueprint="B4", status="draft", block_type="paragraph")
    # estrutural sem function passa
    validate_block_write(function=None, blueprint="B0", status="canonico", block_type="heading")
    # máquina não reverte author_approved
    with pytest.raises(ValueError, match="reverter"):
        validate_block_write(
            function="result", blueprint="B4", status="draft", prev_status="author_approved"
        )


def test_style_gates_canonico_verde(loaded):
    report = check_style(loaded)
    assert report["ok"] is True
    assert report["clinical_openers"] >= 3
    assert report["proibicoes"] == 0


def test_style_gate_detecta_regressao(loaded):
    """Palavra proibida injetada → gate FALHA (anti-regressão de estilo)."""
    from sqlmodel import Session as S

    with S(create_db(loaded)) as s:
        b = s.exec(select(Block).where(Block.block_type == "paragraph")).first()
        original = b.content
        b.content = original + " Resultado promissor para futuros estudos."
        s.add(b)
        s.commit()
        bid = b.block_id
    try:
        with pytest.raises(ValueError, match="promissor|futuros estudos"):
            check_style(loaded)
    finally:
        with S(create_db(loaded)) as s:
            t = s.get(Block, bid)
            t.content = original
            s.add(t)
            s.commit()
    assert check_style(loaded)["ok"] is True
