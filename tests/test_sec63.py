"""T2/G6 gate — escada de dose §6.3 ↔ cadeia m31 (banda GUM por el)."""
import pytest
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.experiments import ingest_experiments
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.integrity import check_sec63
from thesis_engine.models import Block


@pytest.fixture(scope="module")
def loaded(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    ingest_registro(db_path=db_path)
    ingest_tese(db_path=db_path)
    ingest_experiments(db_path=db_path)
    return db_path


def test_sec63_verde(loaded):
    r = check_sec63(loaded)
    assert r["ok"] is True and len(r["ancoras"]) == 8
    labels = {a["label"] for a in r["ancoras"]}
    assert "dose-humana-hi" in labels and "mw-nosso-dado" in labels


def test_sec63_anti_tamper(loaded):
    """Dose editada à mão em TODO o cap.6 → gate FALHA (número nunca digitado)."""
    with Session(create_db(loaded)) as s:
        alvo = [x for x in s.exec(select(Block).where(Block.chap_id == "c06")).all() if "2,6" in x.content]
        assert alvo, "âncora 2,6 deveria existir em c06"
        originais = [(x.block_id, x.content) for x in alvo]
        for x in alvo:
            x.content = x.content.replace("2,6", "9,9")
            s.add(x)
        s.commit()
    try:
        with pytest.raises(ValueError, match="2,6|9,9"):
            check_sec63(loaded)
    finally:
        with Session(create_db(loaded)) as s:
            for bid, cont in originais:
                t = s.get(Block, bid)
                t.content = cont
                s.add(t)
            s.commit()
    assert check_sec63(loaded)["ok"] is True
