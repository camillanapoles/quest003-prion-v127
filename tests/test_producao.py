"""HP-Cap gate — produção por capítulo em ordem topológica + fila do revisor hostil.

3 gates por capítulo (objetivo·coesão·gaps), revisão CUMULATIVA, YELLOW→fila hostil.
Calibrado no canônico 94b792a: HARD=0 · YELLOW=17 (agenda real do revisor).
"""
import pytest
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.experiments import ingest_experiments
from thesis_engine.ingest.graphify import ingest_graphify
from thesis_engine.ingest.plano import ingest_plano
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.revisoes import ingest_revisoes
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.models import PlanChapter, RevisaoHostil
from thesis_engine.producao import ORDEM_PRODUCAO, assert_producao_ok, check_producao


@pytest.fixture(scope="module")
def loaded(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    for fn in (ingest_registro, ingest_tese, ingest_experiments, ingest_graphify, ingest_plano):
        fn(db_path=db_path)
    return db_path


def test_ordem_topologica(loaded):
    assert ORDEM_PRODUCAO[0] == "c00"
    assert ORDEM_PRODUCAO[1:14] == [f"c{i:02d}" for i in range(1, 14)]  # c01→c13 na ordem lógica
    assert ORDEM_PRODUCAO[-3:] == ["c14", "c15", "c16"]


def test_canonico_hard_zero_yellow_real(loaded):
    """Pós-emenda v1 (T1): HARD=0; YELLOW=4 decisões documentadas (fila respondida)."""
    r = check_producao(loaded)
    assert r["ok"] is True and not r["hard"]
    assert 3 <= len(r["yellow"]) <= 8  # 4 pós-emenda: TESE-FICHA · forward §8 · C040 · TODO-c08
    joined = " ".join(r["yellow"])
    for achado in ("TODO", "C040", "forward-ref"):
        assert achado in joined, f"decisão esperada ausente: {achado}"
    # os 13 termos foram EMENDADOS na LISTA DE SIGLAS (v1) — não podem mais flaggear
    for resolvido in ("AD", "SAP", "DSMB", "PBPK", "IDW"):
        assert f"termo novo sem definição prévia: {resolvido}" not in joined


def test_cumulativo_revalida_producao_ate_o_momento(loaded):
    """check_producao(upto=c05) revisa c00..c05 — cumulatividade."""
    r = check_producao(loaded, upto_key="c05")
    assert r["capitulos"] == ORDEM_PRODUCAO.index("c05") + 1 == 6
    caps = [c["cap"] for c in r["relatorio"]]
    assert caps == ORDEM_PRODUCAO[:6]


def test_gate_detecta_secao_fantasma(loaded):
    """Plano prometendo seção inexistente → HARD (bloqueia produção)."""
    with Session(create_db(loaded)) as s:
        p = s.get(PlanChapter, "c05")
        original = list(p.topicos)
        p.topicos = original + ["5.99 seção fantasma para o teste"]
        s.add(p)
        s.commit()
    try:
        with pytest.raises(ValueError, match="5.99"):
            assert_producao_ok(loaded)
    finally:
        with Session(create_db(loaded)) as s:
            p2 = s.get(PlanChapter, "c05")
            p2.topicos = original
            s.add(p2)
            s.commit()
    assert assert_producao_ok(loaded)["ok"] is True


def test_fila_hostil_auto_populada(loaded):
    rev = ingest_revisoes(loaded)
    assert rev["total"] >= 4  # pós-emenda v1: 4 decisões (13 termos já emendados no canônico)
    with Session(create_db(loaded)) as s:
        itens = s.exec(select(RevisaoHostil)).all()
    assert any(i.cap_key == "c00" and "TODO" in i.achado for i in itens)
    assert any("C040" in i.achado for i in itens)
    # idempotente: re-sincronizar não duplica
    rev2 = ingest_revisoes(loaded)
    assert rev2["novos"] == 0 and rev2["total"] == rev["total"]
