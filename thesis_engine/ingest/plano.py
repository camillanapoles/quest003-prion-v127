"""Plano global da tese → SQL (PlanChapter) + render MD (PLANO_GLOBAL_DA_TESE.md).

Single-source OO: thesis_engine/plano_data.py alimenta ambos + o gate check_plano.
"""
from pathlib import Path

from sqlalchemy import text as sa_text
from sqlmodel import Session, SQLModel

from thesis_engine.db import create_db
from thesis_engine.models import PlanChapter
from thesis_engine.plano_data import (
    GARANTIAS,
    INCOMUM_PARA_MEDICOS,
    ORDEM_LOGICA,
    PLANO_CAPITULOS,
    PRE_DEFINIR,
    VALOR_RANKING,
)

REPO = Path(__file__).resolve().parents[2]


def ingest_plano(db_path: str) -> dict[str, int]:
    rows = [
        PlanChapter(
            chap_key=p["key"],
            ordem=p["ordem"],
            funcao=p["funcao"],
            objetivo=p["objetivo"],
            fontes=p["fontes"],
            topicos=p["topicos"],
            elementos=p["elementos"],
            complicado=p["complicado"],
            simplificar=p["simplificar"],
        )
        for p in PLANO_CAPITULOS
    ]
    engine = create_db(db_path)
    with engine.connect() as conn:
        conn.execute(sa_text('DROP TABLE IF EXISTS "planchapter"'))
        conn.commit()
    SQLModel.metadata.create_all(engine)
    with Session(engine) as s:
        for r in rows:
            s.add(r)
        s.commit()
        return {"plano_capitulos": len(rows)}


def render_plano_md(out: str = str(REPO / "PLANO_GLOBAL_DA_TESE.md")) -> str:
    """Render humano do plano (mesma fonte do SQL — nunca diverge)."""
    L: list[str] = ["# PLANO GLOBAL DA TESE — planejamento metodológico antecipado", ""]
    L.append("> Single-source: `thesis_engine/plano_data.py` → SQL (`planchapter`) → este MD + gate `check_plano`.")
    L.append("> Fundamentos: blueprints B0–B9 · rationale R0–R9 · style_profile · canon (grafo 3-trees) · roadmap.")
    L.append("")
    L.append("## 1 · Ordem lógica (o que antecede o quê — e por quê)")
    L.append("")
    for key, funcao, porque in ORDEM_LOGICA:
        L.append(f"1. **{key} · {funcao}** — {porque}")
    L.append("")
    L.append("## 2 · Ranking de valor (o mais valioso primeiro)")
    L.append("")
    for pos, item, porque in VALOR_RANKING:
        L.append(f"{pos}. **{item}** — {porque}")
    L.append("")
    L.append("## 3 · O que garante o quê")
    L.append("")
    L.append("| Mecanismo | Garante | Implica |")
    L.append("|---|---|---|")
    for a, b, c in GARANTIAS:
        L.append(f"| {a} | {b} | {c} |")
    L.append("")
    L.append("## 4 · O incomum — mesmo para médicos (traduzir no Cap.11)")
    L.append("")
    for item in INCOMUM_PARA_MEDICOS:
        L.append(f"- {item}")
    L.append("")
    L.append("## 5 · Definido previamente (invariantes de escrita)")
    L.append("")
    for item in PRE_DEFINIR:
        L.append(f"- {item}")
    L.append("")
    L.append("## 6 · Plano por capítulo (objetivo · fontes · tópicos · elementos · simplificação)")
    L.append("")
    for p in sorted(PLANO_CAPITULOS, key=lambda x: x["ordem"]):
        L.append(f"### {p['key']} — {p['funcao']}")
        L.append("")
        L.append(f"**Objetivo da seção:** {p['objetivo']}")
        L.append("")
        L.append("**Onde está a informação (e como aplicar):**")
        for f in p["fontes"]:
            L.append(f"- [{f['tipo']}] {f['ref']}")
        L.append("")
        L.append(f"**Tópicos/subtópicos:** {' · '.join(p['topicos'])}")
        L.append("")
        L.append(f"**Elementos:** {' · '.join(p['elementos'])}")
        L.append("")
        L.append(f"**O que é complicado:** {p['complicado']}")
        L.append("")
        L.append(f"**Como simplificar visualmente:** {p['simplificar']}")
        L.append("")
    Path(out).write_text("\n".join(L), encoding="utf-8")
    return out
