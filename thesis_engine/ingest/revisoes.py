"""Fila do REVISOR HOSTIL — auto-populada dos achados YELLOW/HARD dos gates de produção.

Protocolo: HOSTILE_REVIEW_PROTOCOL.md (persona + obrigação de elaboração).
"""
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.models import RevisaoHostil
from thesis_engine.producao import check_producao


def ingest_revisoes(db_path: str) -> dict[str, int]:
    """Sincroniza a fila hostil com os achados atuais dos gates (idempotente por achado).
    Após sincronizar, RESTAURA respostas do arquivo versionado (se existir) —
    feedback persiste em git (regra GAN), não em DB local."""
    import json
    from pathlib import Path

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
    # restaura respostas do arquivo versionado (data/revisoes_hostis.json)
    src = Path(__file__).resolve().parents[2] / "data" / "revisoes_hostis.json"
    if src.exists():
        load_revisoes(db_path, str(src))
    return {"novos": n, "total": total}


_EXPORT_FIELDS = ("item_id", "cap_key", "tipo", "achado", "status", "resposta", "respondido_por")


def export_revisoes(db_path: str, out: str) -> int:
    """Dump da fila (com respostas) → JSON versionado. Retorna nº de itens."""
    import json
    from pathlib import Path

    engine = create_db(db_path)
    with Session(engine) as s:
        rows = [
            {f: getattr(x, f) for f in _EXPORT_FIELDS}
            for x in s.exec(select(RevisaoHostil).order_by(RevisaoHostil.item_id)).all()
        ]
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(rows)


def load_revisoes(db_path: str, src: str) -> int:
    """Upsert do arquivo versionado → DB (respostas persistem entre rebuilds)."""
    import json
    from pathlib import Path

    rows = json.loads(Path(src).read_text(encoding="utf-8"))
    engine = create_db(db_path)
    restaurados = 0
    with Session(engine) as s:
        by_achado = {x.achado: x for x in s.exec(select(RevisaoHostil)).all()}
        for r in rows:
            alvo = by_achado.get(r["achado"])
            if alvo is None:
                alvo = RevisaoHostil(
                    item_id=r["item_id"], cap_key=r["cap_key"], tipo=r.get("tipo", "hostil"), achado=r["achado"]
                )
                s.add(alvo)
            elif r.get("status") and r["status"] != "aberto" and alvo.status == "aberto":
                alvo.status = r["status"]
                alvo.resposta = r.get("resposta")
                alvo.respondido_por = r.get("respondido_por")
                s.add(alvo)
                restaurados += 1
        s.commit()
    return restaurados
