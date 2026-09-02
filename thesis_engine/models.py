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


class Chapter(SQLModel, table=True):
    """Container nível-1 (título, CAPÍTULO 1–13, REFERÊNCIAS, APÊNDICES)."""

    chap_id: str = Field(primary_key=True)  # c00, c01, ...
    order_idx: int
    title: str
    level: int = 1


class Section(SQLModel, table=True):
    """Seção nível-2/3 sob um capítulo (label numerado ou None)."""

    sec_id: str = Field(primary_key=True)  # c01s00, ...
    chap_id: str = Field(foreign_key="chapter.chap_id")
    order_idx: int
    level: int  # 2 ou 3
    label: Optional[str] = None  # "7.1", "5.1-bis", "B.1", None p/ não-numeradas
    title: str


class Block(SQLModel, table=True):
    """Bloco tipado — partição verbatim do MD canônico (Modo A: conservação).

    content cobre o arquivo inteiro contiguamente: render = ''.join(contents em seq).
    Categorização §3.5: function/blueprint preenchidos em F2.5; status='canonico'
    para texto preservado (Modo A) — 'draft/revised/validated/author_approved' no Modo B.
    """

    block_id: str = Field(primary_key=True)  # B0001... (determinístico por posição)
    seq: int
    block_type: str  # heading|paragraph|math|table|figure|list|quote|hr|blank
    chap_id: Optional[str] = Field(default=None, foreign_key="chapter.chap_id")
    sec_id: Optional[str] = Field(default=None, foreign_key="section.sec_id")
    content: str  # verbatim, inclui \n final
    heading_level: Optional[int] = None
    heading_text: Optional[str] = None
    claim_ids: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    evidence_ids: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    cross_refs: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    tiers: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    status: str = "canonico"
    function: Optional[str] = None  # F2.5 (motivation/method/result/...)
    blueprint: Optional[str] = None  # F2.5 (B0–B9)


class NumberValue(SQLModel, table=True):
    """Número com lineage: arquivo JSON do registro → caminho pontuado → valor.

    Convenção de caminho: chaves de dict com pontos/caracteres não-ident → aspas
    (`rows[1].R_by_kappa["2.0"]`); índices de lista → `[i]`.
    """

    value_id: str = Field(primary_key=True)  # V0001... determinístico por ordem
    source_file: str  # experiments/xspecies/p024_human.json
    json_path: str  # summary.theta_range[0]
    raw: str  # repr exato do JSON
    value_float: Optional[float] = None


class GraphNode(SQLModel, table=True):
    """Nó do grafo graphify dos 3 worktrees (canon/guardian/knowledge) — F5.7."""

    node_id: str = Field(primary_key=True)
    label: str
    community_id: str = ""
    community_name: str = ""
    file_type: str = ""
    source_file: str = ""
    source_location: Optional[str] = None
    origin: str = ""  # ast|extracted|inferred
    is_callable: bool = False


class GraphEdge(SQLModel, table=True):
    edge_id: str = Field(primary_key=True)  # hash determinístico source|rel|target
    source_id: str
    target_id: str
    relation: str
    origin: str
    confidence: float = 0.0
    source_file: str = ""


class PlanChapter(SQLModel, table=True):
    """Plano global da tese por capítulo (plano_data.py → SQL; single-source OO)."""

    chap_key: str = Field(primary_key=True)  # c00..c16 == Chapter.chap_id
    ordem: int
    funcao: str
    objetivo: str
    fontes: list[dict] = Field(default_factory=list, sa_column=Column(JSON))
    topicos: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    elementos: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    complicado: str = ""
    simplificar: str = ""


class RevisaoHostil(SQLModel, table=True):
    """Fila do revisor hostil (persona: gênio da área, coordenador de revista).

    Itens YELLOW dos gates de produção + questionamentos do próprio revisor.
    Cada item EXIGE elaboração (critical thinking) ou emenda antes de fechar.
    """

    item_id: str = Field(primary_key=True)  # H0001…
    cap_key: str
    tipo: str  # objetivo|coesao|gaps|hostil
    achado: str
    status: str = "aberto"  # aberto→respondido|emendado
    resposta: Optional[str] = None
    respondido_por: Optional[str] = None


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
