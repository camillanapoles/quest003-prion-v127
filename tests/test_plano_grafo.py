"""F5.7 gate — graphify→SQL + PLANO GLOBAL como dado (PlanChapter) + gate G7.

O grafo dos 3 worktrees vira tabela consultável; o plano metodológico antecipado
vira single-source OO (plano_data → SQL + MD + gate). G7: plano↔tese congruentes.
"""
import pytest
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.experiments import ingest_experiments
from thesis_engine.ingest.graphify import ingest_graphify
from thesis_engine.ingest.plano import ingest_plano, render_plano_md
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.integrity import check_plano
from thesis_engine.models import GraphEdge, GraphNode, PlanChapter


@pytest.fixture(scope="module")
def loaded(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    ingest_registro(db_path=db_path)
    ingest_tese(db_path=db_path)
    ingest_experiments(db_path=db_path)
    g = ingest_graphify(db_path=db_path)
    p = ingest_plano(db_path=db_path)
    return db_path, g, p


def test_grafo_no_sql(loaded):
    db_path, g, _ = loaded
    assert g == {"graph_nodes": 884, "graph_edges": 1145}
    with Session(create_db(db_path)) as s:
        assert s.exec(select(GraphNode).where(GraphNode.source_file.contains("THETA_STAR"))).first()
        f44 = s.exec(select(GraphNode).where(GraphNode.label.contains("F-44"))).first()
        assert f44 and "Cenário B" in f44.label
        n_coms = len({n.community_name for n in s.exec(select(GraphNode)).all() if n.community_name})
        assert n_coms > 100
        assert s.exec(select(GraphEdge).where(GraphEdge.relation == "calls")).first()


def test_plano_no_sql(loaded):
    db_path, _, p = loaded
    assert p == {"plano_capitulos": 17}
    with Session(create_db(db_path)) as s:
        plan = s.exec(select(PlanChapter).order_by(PlanChapter.ordem)).all()
    assert [x.ordem for x in plan] == list(range(17))
    c05 = next(x for x in plan if x.chap_key == "c05")
    assert "invariância" in c05.objetivo and c05.simplificar


def test_gate_plano_verde(loaded):
    db_path, _, _ = loaded
    report = check_plano(db_path)
    assert report["ok"] is True
    assert report["capitulos"] == 17 and report["fontes_validadas"] >= 30


def test_gate_plano_detecta_ghost(loaded):
    db_path, _, _ = loaded
    with Session(create_db(db_path)) as s:
        p = s.get(PlanChapter, "c05")
        original = list(p.fontes)
        p.fontes = original + [{"tipo": "claim", "ref": "C999 fantasma"}]
        s.add(p)
        s.commit()
    try:
        with pytest.raises(ValueError, match="C999"):
            check_plano(db_path)
    finally:
        with Session(create_db(db_path)) as s:
            p2 = s.get(PlanChapter, "c05")
            p2.fontes = original
            s.add(p2)
            s.commit()
    assert check_plano(db_path)["ok"] is True


def test_render_plano_md(loaded, tmp_path):
    out = str(tmp_path / "PLANO_GLOBAL.md")
    render_plano_md(out)
    text = open(out, encoding="utf-8").read()
    for section in (
        "Ordem lógica",
        "Ranking de valor",
        "O que garante o quê",
        "O incomum",
        "Definido previamente",
        "Plano por capítulo",
    ):
        assert section in text
    assert "c05 — o alicerce" in text and "c11 — tradução clínica" in text
