"""Ingest do registro probatório canônico (read-only) → SQLite.

Arquivos-fonte (paper/evidence_workspace/):
  - claims.csv            (60 C-IDs, norm→sha256)
  - claim_texts.md        (textos completos, 1 linha por claim)
  - source_manifest.json  (58 E-IDs)
  - consistency_manifest.json (65 N-fatos, 4 métodos, 5 resultados)

Gates (falham com ValueError):
  - sha256(norm(texto)) deve bater com claims.csv para TODA claim;
  - toda evidence_id citada deve existir em sources.
"""
import csv
import json
import re
from pathlib import Path

from sqlmodel import Session, SQLModel, select

from thesis_engine.db import create_db
from thesis_engine.models import Claim, MethodFact, NFact, ResultFact, Source
from thesis_engine.norm import sha

REPO = Path(__file__).resolve().parents[2]
EVIDENCE = REPO / "paper" / "evidence_workspace"

_CLAIM_LINE = re.compile(
    r"^- \*\*(C\d+)\*\* \(([^,]+),([^)]+)\) \[([^\]]+)\]: (.+)$", re.MULTILINE
)


def _load_claims() -> list[Claim]:
    rows = list(csv.DictReader(open(EVIDENCE / "claims.csv", encoding="utf-8")))
    texts = dict(_parse_claim_texts())
    claims: list[Claim] = []
    for r in rows:
        cid = r["claim_id"]
        if cid not in texts:
            raise ValueError(f"claim_texts.md sem texto para {cid}")
        text = texts[cid]
        digest = sha(text)
        if digest != r["claim_text_sha256"]:
            raise ValueError(f"sha256 divergente para {cid}: registro={r['claim_text_sha256']} recomputado={digest}")
        claims.append(
            Claim(
                claim_id=cid,
                section=r["section"],
                claim_kind=r["claim_kind"],
                claim_text_sha256=r["claim_text_sha256"],
                claim_text=text,
                evidence_ids=r["evidence_ids"].split(";"),
                verification_status=r["verification_status"],
                uncertainty=r["uncertainty"],
                analysis_intent=r["analysis_intent"],
            )
        )
    # claim_texts.md não pode ter claims fora do CSV
    orphans = set(texts) - {c.claim_id for c in claims}
    if orphans:
        raise ValueError(f"claim_texts.md contém claims fora do registro: {sorted(orphans)}")
    return claims


def _parse_claim_texts() -> list[tuple[str, str]]:
    md = (EVIDENCE / "claim_texts.md").read_text(encoding="utf-8")
    return [(m.group(1), m.group(5).strip()) for m in _CLAIM_LINE.finditer(md)]


def _load_sources() -> list[Source]:
    data = json.load(open(EVIDENCE / "source_manifest.json", encoding="utf-8"))
    sources: list[Source] = []
    for s in data["sources"]:
        ver = s.get("verification", {}) or {}
        sources.append(
            Source(
                evidence_id=s["evidence_id"],
                source_type=s.get("source_type", "unknown"),
                title=s.get("title", ""),
                authors=json.dumps(s.get("authors", []), ensure_ascii=False),
                year=s.get("year"),
                identifiers=json.dumps(s.get("identifiers", {}), ensure_ascii=False),
                locator=s.get("locator"),
                confidentiality=s.get("confidentiality", "public"),
                verification_status=ver.get("status", "unverified"),
                verified_on=ver.get("verified_on"),
            )
        )
    return sources


def _load_consistency() -> tuple[list[NFact], list[MethodFact], list[ResultFact]]:
    d = json.load(open(EVIDENCE / "consistency_manifest.json", encoding="utf-8"))
    nfacts = [
        NFact(
            fact_id=n["fact_id"],
            concept=n.get("concept", ""),
            section=n.get("section"),
            value=str(n["value"]),
            unit=n.get("unit", ""),
            numerator=(str(n["numerator"]) if n.get("numerator") is not None else None),
            denominator=(str(n["denominator"]) if n.get("denominator") is not None else None),
            sample_size=(str(n["sample_size"]) if n.get("sample_size") is not None else None),
            analysis_set=n.get("analysis_set"),
            evidence_ids=list(n.get("evidence_ids", [])),
        )
        for n in d["numeric_facts"]
    ]
    methods = [
        MethodFact(
            method_id=m["method_id"],
            name=m.get("name", ""),
            analysis_intent=m.get("analysis_intent", ""),
            protocol_status=m.get("protocol_status", ""),
            outcome_ids=list(m.get("outcome_ids", [])),
        )
        for m in d["methods"]
    ]
    results = [
        ResultFact(
            result_id=r["result_id"],
            method_id=r.get("method_id", ""),
            outcome_id=r.get("outcome_id", ""),
            analysis_intent=r.get("analysis_intent", ""),
            sample_size=(str(r["sample_size"]) if r.get("sample_size") is not None else None),
            evidence_ids=list(r.get("evidence_ids", [])),
            reported_sections=list(r.get("reported_sections", [])),
        )
        for r in d["results"]
    ]
    return nfacts, methods, results


def ingest_registro(db_path: str) -> dict[str, int]:
    """Carrega o registro canônico no SQLite (rebuild limpo). Retorna contagens."""
    claims = _load_claims()
    sources = _load_sources()
    nfacts, methods, results = _load_consistency()

    known = {s.evidence_id for s in sources}
    for c in claims:
        missing = set(c.evidence_ids) - known
        if missing:
            raise ValueError(f"{c.claim_id} cita fonte ausente: {sorted(missing)}")
    for n in nfacts:
        missing = set(n.evidence_ids) - known
        if missing:
            raise ValueError(f"{n.fact_id} cita fonte ausente: {sorted(missing)}")

    engine = create_db(db_path)
    # rebuild determinístico: derruba e recria tabelas do registro
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as s:
        for obj in (*sources, *claims, *nfacts, *methods, *results):
            s.add(obj)
        s.commit()
        counts = {
            "claims": len(s.exec(select(Claim)).all()),
            "sources": len(s.exec(select(Source)).all()),
            "nfacts": len(s.exec(select(NFact)).all()),
            "methods": len(s.exec(select(MethodFact)).all()),
            "results": len(s.exec(select(ResultFact)).all()),
        }
    return counts
