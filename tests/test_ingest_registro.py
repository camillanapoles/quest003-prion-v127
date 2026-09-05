"""F1 gate — ingest do registro probatório canônico.

Fontes (read-only): paper/evidence_workspace/
  claims.csv (60 C-IDs, norm→sha256) · claim_texts.md · source_manifest.json (58 E-IDs)
  · consistency_manifest.json (65 N-fatos, 4 métodos, 5 resultados)
"""
import pytest
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.models import Claim, Source, NFact, MethodFact, ResultFact
from thesis_engine.norm import sha


@pytest.fixture(scope="module")
def loaded(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    return db_path, ingest_registro(db_path=db_path)


def test_carga_completa(loaded):
    """Gate F1: 60 claims · 58 fontes · 65 N-fatos · 4 métodos · 5 resultados."""
    _, counts = loaded
    assert counts == {
        "claims": 60,
        "sources": 58,
        "nfacts": 65,
        "methods": 4,
        "results": 5,
    }


def test_sha256_de_toda_claim_conferido(loaded):
    """Gate de imutabilidade: sha256(norm(texto)) == claims.csv, para TODAS."""
    db_path, _ = loaded
    with Session(create_db(db_path)) as s:
        claims = s.exec(select(Claim)).all()
    assert len(claims) == 60
    for c in claims:
        assert sha(c.claim_text) == c.claim_text_sha256, f"hash divergente: {c.claim_id}"


def test_integridade_referencial_evidencias(loaded):
    """Toda evidence_id citada por claim/N-fato existe em sources."""
    db_path, _ = loaded
    with Session(create_db(db_path)) as s:
        sources = {src.evidence_id for src in s.exec(select(Source)).all()}
        claims = s.exec(select(Claim)).all()
        nfacts = s.exec(select(NFact)).all()
    for c in claims:
        for e in c.evidence_ids:
            assert e in sources, f"{c.claim_id} cita fonte ausente: {e}"
    for n in nfacts:
        for e in n.evidence_ids:
            assert e in sources, f"{n.fact_id} cita fonte ausente: {e}"


def test_campos_minimos_populados(loaded):
    db_path, _ = loaded
    with Session(create_db(db_path)) as s:
        c001 = s.get(Claim, "C001")
        e058 = s.get(Source, "E058")
        n001 = s.get(NFact, "N001")
        m001 = s.get(MethodFact, "M001")
        r001 = s.get(ResultFact, "R001")
    assert c001.verification_status and c001.claim_kind
    assert e058.title and e058.source_type
    assert n001.value is not None and n001.unit
    assert m001.name
    assert r001.method_id == "M001"


def test_ingest_idempotente_rebuild(loaded):
    """DB é derivado: re-ingest produz as mesmas contagens (rebuild limpo)."""
    db_path, counts1 = loaded
    counts2 = ingest_registro(db_path=db_path)
    assert counts1 == counts2
