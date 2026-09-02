"""Fila do REVISOR HOSTIL — auto-populada dos achados YELLOW/HARD dos gates de produção.

Protocolo: HOSTILE_REVIEW_PROTOCOL.md (persona + obrigação de elaboração).
"""
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.models import RevisaoHostil
from thesis_engine.producao import check_producao


def ingest_revisoes(db_path: str) -> dict[str, int]:
    """Sincroniza a fila hostil com os achados atuais dos gates (idempotente por achado)."""
    r = check_producao(db_path)
    engine = create_db(db_path)
    with Session(engine) as s:
        existentes = {(x.cap_key, x.achado) for x in s.exec(select(RevisaoHostil)).all()}
        n = 0
        items = [(a, "hostil-hard" if a in r["hard"] else "hostil-yellow") for a in r["hard"] + r["yellow"]]
        seq = len(existentes)
        for achado, tipo in items:
            # achado vem como "cNN/gate: texto"
            cap = achado.split("/", 1)[0]
            texto = achado.split(": ", 1)[-1]
            chave = (cap, texto)
            if chave in existentes:
                continue
            seq += 1
            s.add(RevisaoHostil(item_id=f"H{seq:04d}", cap_key=cap, tipo=tipo, achado=texto))
            n += 1
        s.commit()
        total = len(s.exec(select(RevisaoHostil)).all())
    return {"novos": n, "total": total}
