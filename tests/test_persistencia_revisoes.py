"""Persistência da fila hostil — feedback vira ARQUIVO versionado (regra GAN anti-pattern #2).

Incidente registrado: respostas T1 viviam só no thesis.db local (gitignored) →
DB novo nasceria com fila vazia SEM ERRO (perda silenciosa). Fix: data/revisoes_hostis.json
é a fonte persistente; ingest restaura; teste prova em DB zerado.
"""
import json
from pathlib import Path

from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.experiments import ingest_experiments
from thesis_engine.ingest.graphify import ingest_graphify
from thesis_engine.ingest.plano import ingest_plano
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.revisoes import export_revisoes, ingest_revisoes, load_revisoes
from thesis_engine.ingest.tese import ingest_tese
from thesis_engine.models import RevisaoHostil

SRC = Path(__file__).resolve().parents[1] / "data" / "revisoes_hostis.json"


def _build_fresh(db_path: str):
    for fn in (ingest_registro, ingest_tese, ingest_experiments, ingest_graphify, ingest_plano):
        fn(db_path=db_path)


def test_arquivo_versionado_existe_e_fechado():
    rows = json.loads(SRC.read_text(encoding="utf-8"))
    assert len(rows) >= 4
    fechados = [r for r in rows if r["status"] in ("respondido", "emendado")]
    assert len(fechados) >= 4, "as decisões T1 devem estar fechadas no arquivo"
    assert all(r.get("resposta") for r in fechados), "item fechado sem resposta elaborada"


def test_db_novo_restaura_respostas_do_git(tmp_path):
    """Persistência REAL: DB zerado → ingest_revisoes restaura fila+respostas do arquivo.
    Achados NOVOS (pós-export) podem estar abertos — é o fluxo; os do arquivo, nunca."""
    db = str(tmp_path / "fresh.db")
    _build_fresh(db)
    rev = ingest_revisoes(db)
    assert rev["total"] >= 4
    from sqlmodel import Session, select

    from thesis_engine.models import RevisaoHostil

    with Session(create_db(db)) as s:
        itens = s.exec(select(RevisaoHostil)).all()
        fechados = [i for i in itens if i.status != "aberto"]
    assert any("TESE-FICHA" in i.achado and i.respondido_por for i in fechados)
    assert len(fechados) >= 4, "respostas T1 perdidas em rebuild"
    abertos = [i.achado for i in itens if i.status == "aberto"]
    assert all("não-pareado" in a for a in abertos), f"aberto inesperado: {abertos}"


def test_roundtrip_export_load(tmp_path):
    db = str(tmp_path / "rt.db")
    _build_fresh(db)
    ingest_revisoes(db)
    out = str(tmp_path / "exp.json")
    assert export_revisoes(db, out) >= 4
    src_rows = {r["achado"]: r for r in json.loads(Path(out).read_text(encoding="utf-8"))}
    fechados_no_export = {a for a, r in src_rows.items() if r["status"] != "aberto"}
    # zera TUDO no DB e restaura do arquivo — os fechados do export re-fecham
    with Session(create_db(db)) as s:
        for i in s.exec(select(RevisaoHostil)).all():
            i.status, i.resposta, i.respondido_por = "aberto", None, None
            s.add(i)
        s.commit()
    load_revisoes(db, out)
    with Session(create_db(db)) as s:
        for i in s.exec(select(RevisaoHostil)).all():
            if i.achado in fechados_no_export:
                assert i.status != "aberto", f"resposta perdida no roundtrip: {i.item_id}"
