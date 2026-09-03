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
    assert all(r["status"] in ("respondido", "emendado") for r in rows), "fila git com itens abertos!"
    assert all(r.get("resposta") for r in rows), "item fechado sem resposta elaborada"


def test_db_novo_restaura_respostas_do_git(tmp_path):
    """Persistência REAL: DB zerado → ingest_revisoes restaura fila+respostas do arquivo."""
    db = str(tmp_path / "fresh.db")
    _build_fresh(db)
    rev = ingest_revisoes(db)  # populou achados E restaurou respostas do git
    assert rev["total"] >= 4
    with Session(create_db(db)) as s:
        itens = s.exec(select(RevisaoHostil)).all()
    abertos = [i for i in itens if i.status == "aberto"]
    assert not abertos, f"respostas perdidas em rebuild: {[i.item_id for i in abertos]}"
    assert any("TESE-FICHA" in i.achado and i.respondido_por for i in itens)


def test_roundtrip_export_load(tmp_path):
    db = str(tmp_path / "rt.db")
    _build_fresh(db)
    ingest_revisoes(db)
    out = str(tmp_path / "exp.json")
    n = export_revisoes(db, out)
    assert n >= 4
    # zera status no DB e restaura do arquivo
    with Session(create_db(db)) as s:
        for i in s.exec(select(RevisaoHostil)).all():
            i.status, i.resposta, i.respondido_por = "aberto", None, None
            s.add(i)
        s.commit()
    restaurados = load_revisoes(db, out)
    assert restaurados >= 4
    with Session(create_db(db)) as s:
        assert all(i.status != "aberto" for i in s.exec(select(RevisaoHostil)).all())
