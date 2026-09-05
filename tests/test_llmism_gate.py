"""Regressão: termo 'verbatim' (e outros LLM-isms) deve ser PEGO pelo gate de estilo.
Incidente: a sessão anterior usou 'verbatim' em resposta hostil → entrou na tese →
o gate só bania 'promissor/futuros estudos' → passou. Nunca mais.
"""
import pytest
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.integrity import check_style
from thesis_engine.models import Block


@pytest.fixture(scope="module")
def db(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "t.db")
    ingest_registro(db_path=db_path)
    ingest_tese(db_path=db_path)
    return db_path


def _primeiro_paragrafo(db_path):
    with Session(create_db(db_path)) as s:
        return s.exec(
            select(Block).where(Block.block_type == "paragraph")
        ).first()


def test_verbatim_banido(db):
    """'verbatim' no bloco → gate VERMELHO."""
    with Session(create_db(db)) as s:
        b = _primeiro_paragrafo(db)
        original = b.content
        bid = b.block_id
        b.content = original + " Citação verbatim entre aspas."
        s.add(b)
        s.commit()
    try:
        with pytest.raises(ValueError, match="verbatim"):
            check_style(db)
    finally:
        with Session(create_db(db)) as s:
            t = s.get(Block, bid)
            t.content = original
            s.add(t)
            s.commit()
    assert check_style(db)["ok"] is True


def test_outros_llmisms_banidos(db):
    """Comprehensive, delve, robust — também pegos."""
    with Session(create_db(db)) as s:
        b = _primeiro_paragrafo(db)
        original = b.content
        bid = b.block_id
        b.content = original + " A comprehensive framework delves into the robust problem."
        s.add(b)
        s.commit()
    try:
        with pytest.raises(ValueError, match="comprehensive|delve|robust"):
            check_style(db)
    finally:
        with Session(create_db(db)) as s:
            t = s.get(Block, bid)
            t.content = original
            s.add(t)
            s.commit()
    assert check_style(db)["ok"] is True
