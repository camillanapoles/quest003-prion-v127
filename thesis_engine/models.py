"""Modelos OO do registro probatório (SQLModel/Pydantic v2).

Escopo F1: entidades do registro. Chapter/Section/Block/Figure chegam em F2/F3.
"""
from typing import Any, Optional

from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel


class Source(SQLModel, table=True):
    """Fonte verificada E001–E058 (source_manifest.json)."""

    evidence_id: str = Field(primary_key=True)
    source_type: str
    title: str
    authors: str = "[]"  # JSON list
    year: Optional[int] = None
    identifiers: str = "{}"  # JSON dict (doi/pmid/pmcid)
    locator: Optional[str] = None
    confidentiality: str = "public"
    verification_status: str = "unverified"
    verified_on: Optional[str] = None

    def authors_list(self) -> list[Any]:
        import json

        return json.loads(self.authors)

    def identifiers_dict(self) -> dict[str, Any]:
        import json

        return json.loads(self.identifiers)


class Claim(SQLModel, table=True):
    """Claim C001–C060 (claims.csv + claim_texts.md). Imutável: sha256 do texto."""

    claim_id: str = Field(primary_key=True)
    section: str
    claim_kind: str
    claim_text_sha256: str
    claim_text: str
    evidence_ids: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    verification_status: str
    uncertainty: str
    analysis_intent: str


class NFact(SQLModel, table=True):
    """N-fato numérico N001–N065 (consistency_manifest.json)."""

    fact_id: str = Field(primary_key=True)
    concept: str
    section: Optional[str] = None
    value: str  # preserva exatidão textual ("1.25e-10", "0,333")
    unit: str
    numerator: Optional[str] = None
    denominator: Optional[str] = None
    sample_size: Optional[str] = None
    analysis_set: Optional[str] = None
    evidence_ids: list[str] = Field(default_factory=list, sa_column=Column(JSON))


class MethodFact(SQLModel, table=True):
    """Método M001–M004 (consistency_manifest.json)."""

    method_id: str = Field(primary_key=True)
    name: str
    analysis_intent: str
    protocol_status: str
    outcome_ids: list[str] = Field(default_factory=list, sa_column=Column(JSON))


class ResultFact(SQLModel, table=True):
    """Resultado R001–R005 (consistency_manifest.json)."""

    result_id: str = Field(primary_key=True)
    method_id: str
    outcome_id: str
    analysis_intent: str
    sample_size: Optional[str] = None
    evidence_ids: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    reported_sections: list[str] = Field(default_factory=list, sa_column=Column(JSON))
