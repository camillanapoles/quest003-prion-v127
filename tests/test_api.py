"""F4 gate — FastAPI CRUD guardado pelo write-guard + queries + render + CLI.

Registro probatório é READ-ONLY por design (imutabilidade). Escritas só em Block,
via ciclo Modo B (draft→…→author_approved), sempre validadas. Render canônico
exclui drafts.
"""
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from thesis_engine.api import create_app
from thesis_engine.ingest.experiments import ingest_experiments
from thesis_engine.ingest.graphify import ingest_graphify
from thesis_engine.ingest.plano import ingest_plano
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import ingest_tese

TESE_MD = Path(__file__).resolve().parents[1] / "paper_rewriting_output" / "final_paper" / "tese_unificada.md"


@pytest.fixture(scope="module")
def client(tmp_path_factory):
    db_path = str(tmp_path_factory.mktemp("db") / "tese.db")
    ingest_registro(db_path=db_path)
    ingest_tese(db_path=db_path)
    ingest_experiments(db_path=db_path)
    ingest_graphify(db_path=db_path)
    ingest_plano(db_path=db_path)
    return TestClient(create_app(db_path))


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    counts = r.json()["counts"]
    assert counts["claims"] == 60 and counts["sources"] == 58
    assert counts["blocks"] == 524 and counts["numbervalues"] > 200


def test_listagens_e_queries(client):
    assert len(client.get("/chapters").json()) == 17
    assert len(client.get("/sections", params={"chap_id": "c07"}).json()) == 5
    assert len(client.get("/blocks", params={"block_type": "figure"}).json()) == 2
    # query por claim citada em bloco
    r = client.get("/blocks", params={"claim_id": "C060"})
    assert r.status_code == 200 and r.json()
    # numbervalue com lineage
    r = client.get(
        "/numbervalues", params={"stem": "p024_human", "path": "summary.theta_range[0]"}
    )
    assert r.status_code == 200
    assert r.json()["value_float"] == pytest.approx(0.333)
    # nfacts por evidência
    assert client.get("/nfacts", params={"evidence_id": "E030"}).json()


def test_entidades_registro_readonly(client):
    assert client.get("/claims/C001").status_code == 200
    body = client.get("/claims/C001").json()
    assert body["claim_text_sha256"] and body["evidence_ids"] == ["E001"]
    assert client.get("/sources/E058").status_code == 200
    # imutabilidade por design: registro não tem escrita
    assert client.post("/claims", json={}).status_code == 405
    assert client.delete("/sources/E001").status_code == 405


def test_post_block_modo_b_validado(client):
    payload = {
        "chap_id": "c06",
        "sec_id": "c06s02",
        "block_type": "paragraph",
        "content": "Rascunho Modo B citando [claim:C058] com tier [SIM]-planejamento.\n",
        "function": "result",
        "blueprint": "B4",
    }
    r = client.post("/blocks", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["status"] == "draft" and body["block_id"].startswith("D")
    assert body["claim_ids"] == ["C058"]  # extraído do conteúdo
    assert "SIM-planejamento" in body["tiers"]
    # write-guard: function inválida / ausente → 422
    bad = dict(payload, function="genial")
    assert client.post("/blocks", json=bad).status_code == 422
    nof = dict(payload); nof.pop("function")
    assert client.post("/blocks", json=nof).status_code == 422
    # claim inexistente no registro → 422 (régua: claim sem registro é inaceitável)
    ghost = dict(payload, content="cita [claim:C999] inexistente\n")
    assert client.post("/blocks", json=ghost).status_code == 422


def test_canonico_imutavel_e_draft_editavel(client):
    r = client.get("/blocks/B0001")
    assert r.status_code == 200
    # canônico é conservação: PATCH bloqueado
    assert client.patch("/blocks/B0001", json={"content": "x"}).status_code == 409
    # draft editável, metadata re-extraída
    r = client.post(
        "/blocks",
        json={
            "chap_id": "c06",
            "sec_id": "c06s02",
            "block_type": "paragraph",
            "content": "v1\n",
            "function": "result",
            "blueprint": "B4",
        },
    )
    did = r.json()["block_id"]
    r = client.patch(f"/blocks/{did}", json={"content": "v2 com [claim:C060]\n"})
    assert r.status_code == 200
    assert r.json()["claim_ids"] == ["C060"]
    assert client.patch(f"/blocks/{did}", json={"content": "v3\n", "function": "limitation"}).json()[
        "function"
    ] == "limitation"


def test_ciclo_de_status_com_aprovacao_humana(client):
    r = client.post(
        "/blocks",
        json={
            "chap_id": "c13",
            "block_type": "paragraph",
            "content": "conclusão rascunhada\n",
            "function": "interpretation",
            "blueprint": "B8",
        },
    )
    did = r.json()["block_id"]
    # máquina não seta author_approved
    r = client.post(f"/blocks/{did}/status", json={"status": "author_approved"})
    assert r.status_code == 422
    # fluxo válido: draft→revised→validated→author_approved (com aprovadora)
    for st in ("revised", "validated"):
        assert client.post(f"/blocks/{did}/status", json={"status": st}).status_code == 200
    r = client.post(
        f"/blocks/{did}/status", json={"status": "author_approved", "approver": "Camilla"}
    )
    assert r.status_code == 200 and r.json()["status"] == "author_approved"
    # regressão proibida
    assert client.post(f"/blocks/{did}/status", json={"status": "draft"}).status_code == 422


def test_integrity_endpoint(client):
    r = client.get("/integrity")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True and body["sec43"]["ok"] and body["style"]["ok"]
    assert body["plano"]["ok"]  # G7 no endpoint
    # grafo consultável pela API
    r = client.get("/graph", params={"q": "THETA_STAR"})
    assert r.status_code == 200 and r.json()
    r = client.get("/plano")
    assert len(r.json()) == 17


def test_render_md_canonico_exclui_drafts(client):
    # garante ≥1 draft existente no DB deste client
    client.post(
        "/blocks",
        json={
            "chap_id": "c06",
            "block_type": "paragraph",
            "content": "draft que NÃO pode vazar no render\n",
            "function": "result",
            "blueprint": "B4",
        },
    )
    r = client.get("/render/md")
    assert r.status_code == 200
    assert r.text == TESE_MD.read_text(encoding="utf-8")
    assert "draft que NÃO pode vazar" not in r.text
