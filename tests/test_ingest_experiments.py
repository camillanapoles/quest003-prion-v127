"""F3 gate — JSONs experimentais → NumberValue com lineage + reconciliação §4.3.

"Número nunca digitado": toda cifra da tabela §4.3 da tese deve existir como
NumberValue vindo de um JSON do registro (arquivo→caminho→valor), e o bloco-tabela
canônico deve conter a forma PT-BR correspondente.
"""
from pathlib import Path

import pytest
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.experiments import REGISTRY_JSONS, get_value, ingest_experiments
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.integrity import check_sec43
from thesis_engine.models import Block, Section

REPO = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def loaded(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    ingest_registro(db_path=db_path)
    ingest_tese(db_path=db_path)
    ingest_experiments(db_path=db_path)
    return db_path


def test_registry_jsons_existem():
    for rel in REGISTRY_JSONS:
        assert (REPO / rel).exists(), f"JSON do registro ausente: {rel}"


def test_flatten_popula_numbervalues(loaded):
    from thesis_engine.models import NumberValue

    with Session(create_db(loaded)) as s:
        vals = s.exec(select(NumberValue)).all()
    assert len(vals) > 200  # p024×4 + m31 + ws_9 + ws_7 + part2
    # lineage completa em TODAS as linhas
    assert all(v.source_file and v.json_path for v in vals)


def test_ancoras_do_registro(loaded):
    """Âncoras §4.3 existem nos JSONs com lineage (arquivo→caminho→valor)."""
    # Cenário B humano: banda 0,333–0,400 (θ* é o piso exato)
    assert get_value(loaded, "p024_human", "summary.theta_range[0]") == pytest.approx(0.333)
    assert get_value(loaded, "p024_human", "summary.theta_range[1]") == pytest.approx(0.4)
    # θ* v1.0 travado = referência murina presente nas 4 espécies
    for sp in ("mouse", "hamster", "human", "vole"):
        assert get_value(loaded, f"p024_{sp}", "summary.theta_mouse_ref") == pytest.approx(0.333)
    # κ_min humano: 1,5 (Kt≤1) e 2,0 (Kt=2)
    assert get_value(loaded, "p024_human", "rows[0].kappa_min") == pytest.approx(1.5)
    assert get_value(loaded, "p024_human", "rows[1].kappa_min") == pytest.approx(1.5)
    assert get_value(loaded, "p024_human", "rows[2].kappa_min") == pytest.approx(2.0)
    # titulação κ_req: Kt 1→1,5 · 2→2 · 3→3 · 4→8
    assert get_value(loaded, "m31_u1u2", "u1_kreq.1") == pytest.approx(1.5)
    assert get_value(loaded, "m31_u1u2", "u1_kreq.2") == pytest.approx(2.0)
    assert get_value(loaded, "m31_u1u2", "u1_kreq.3") == pytest.approx(3.0)
    assert get_value(loaded, "m31_u1u2", "u1_kreq.4") == pytest.approx(8.0)
    # hamster: predição refutada 0,659 mm @ κ=2/Kt=2
    assert get_value(loaded, "p024_hamster", "rows[1].R_by_kappa.2.0") == pytest.approx(0.659)
    # MW do nosso dado (M3.1/U2)
    assert get_value(loaded, "m31_u1u2", "u2_mw.mw_kDa") == pytest.approx(22.83)


def test_tabela_43_contem_formas_ptbr(loaded):
    """O bloco-tabela §4.3 canônico carrega as formas PT-BR das âncoras."""
    with Session(create_db(loaded)) as s:
        sec = s.exec(select(Section).where(Section.label == "4.3")).one()
        table = s.exec(
            select(Block).where(Block.sec_id == sec.sec_id, Block.block_type == "table")
        ).one()
    for fragmento in ("0,333", "0,400", "1,5", "2,0", "0,659", "4→8"):
        assert fragmento in table.content, f"§4.3 sem o número {fragmento!r}"


def test_gate_check_sec43_verde(loaded):
    """Gate completo: JSONs ↔ tabela §4.3 — retorna relatório, falha se divergir."""
    report = check_sec43(loaded)
    assert report["ok"] is True
    assert len(report["ancoras"]) >= 10


def test_gate_detecta_divergencia(loaded):
    """O gate FALHA quando a tabela cita número fora do registro (anti-edição-à-mão)."""
    with Session(create_db(loaded)) as s:
        sec = s.exec(select(Section).where(Section.label == "4.3")).one()
        table = s.exec(
            select(Block).where(Block.sec_id == sec.sec_id, Block.block_type == "table")
        ).one()
        original = table.content
        bid = table.block_id
        table.content = original.replace("0,659", "0,999")  # número digitado à mão
        s.add(table)
        s.commit()
    try:
        with pytest.raises(ValueError, match="0,999|0,659"):
            check_sec43(loaded)
    finally:  # restaura o canônico
        with Session(create_db(loaded)) as s:
            t = s.get(Block, bid)
            t.content = original
            s.add(t)
            s.commit()
    assert check_sec43(loaded)["ok"] is True
