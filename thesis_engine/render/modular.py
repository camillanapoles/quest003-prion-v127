"""Render MD modular — 1 arquivo por capítulo + SUMARIO.md integrado.

A partição é exata: o conjunto dos arquivos de capítulo concatenados em ordem
== render_md single-file (byte a byte). Só blocos status='canonico'.
"""
import re
import unicodedata
from pathlib import Path

from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.models import Block, Chapter, Section

_CAP_NUM = re.compile(r"CAPÍTULO (\d+)")


def _slug(title: str) -> str:
    norm = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    norm = re.sub(r"[^A-Za-z0-9]+", "-", norm).strip("-").lower()
    return norm[:44].rstrip("-")


def render_modular(db_path: str, out_dir: str) -> dict:
    engine = create_db(db_path)
    with Session(engine) as s:
        chapters = s.exec(select(Chapter).order_by(Chapter.order_idx)).all()
        blocks = s.exec(
            select(Block).where(Block.status == "canonico").order_by(Block.seq)
        ).all()
        sections = s.exec(select(Section)).all()

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    by_chap: dict[str, list[Block]] = {}
    for b in blocks:
        by_chap.setdefault(b.chap_id or "c00", []).append(b)

    secs_by_chap: dict[str, list[Section]] = {}
    for sec in sections:
        secs_by_chap.setdefault(sec.chap_id, []).append(sec)

    filenames: list[str] = []
    sumario_rows: list[str] = ["# SUMÁRIO MODULAR — tese canônica (render do grafo)", ""]
    total_claims: set[str] = set()

    for c in chapters:
        cblocks = by_chap.get(c.chap_id, [])
        csecs = secs_by_chap.get(c.chap_id, [])
        claims = sorted({cid for b in cblocks for cid in b.claim_ids})
        tiers = sorted({t for b in cblocks for t in b.tiers})
        total_claims.update(claims)
        fname = f"{c.order_idx:02d}-{_slug(c.title)}.md"
        filenames.append(fname)
        (out / fname).write_text(
            "".join(b.content for b in cblocks), encoding="utf-8"
        )
        m = _CAP_NUM.search(c.title)
        num = f"Cap.{m.group(1)} · " if m else ""
        sumario_rows.append(
            f"- [{c.title}]({fname}) — {num}"
            f"{len(csecs)} seções · {len(cblocks)} blocos · "
            f"claims: {', '.join(claims) if claims else '—'}"
            + (f" · tiers: {', '.join(tiers)}" if tiers else "")
        )

    (out / "SUMARIO.md").write_text("\n".join(sumario_rows) + "\n", encoding="utf-8")
    return {
        "files": len(filenames) + 1,
        "chapters": len(chapters),
        "total_claims": len(total_claims),
        "chars": sum(len(b.content) for b in blocks),
    }
