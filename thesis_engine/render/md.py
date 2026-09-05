"""Render MD canônico — blocos → tese_unificada.md.

Modo A (conservação): a partição de blocos cobre o arquivo inteiro; portanto
render = concatenação dos `content` em ordem de `seq`. Gate F2 garante byte-a-byte.
"""
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.models import Block


def render_md(db_path: str) -> str:
    """Render canônico: apenas blocos status='canonico' (drafts Modo B ficam de fora)."""
    engine = create_db(db_path)
    with Session(engine) as s:
        blocks = s.exec(
            select(Block).where(Block.status == "canonico").order_by(Block.seq)
        ).all()
    return "".join(b.content for b in blocks)
