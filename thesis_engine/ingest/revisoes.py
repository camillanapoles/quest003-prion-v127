"""Fila do REVISOR HOSTIL — auto-populada dos achados YELLOW/HARD dos gates de produção.

Protocolo: HOSTILE_REVIEW_PROTOCOL.md (persona + obrigação de elaboração).
"""
from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.models import RevisaoHostil
from thesis_engine.producao import check_producao


def ingest_revisoes(
    db_path: str, upto_key: str | None = None, restore_from: str | None = "default"
) -> dict[str, int]:
    """Sincroniza a fila hostil com os achados atuais dos gates (idempotente por achado).
    upto_key: revisão CUMULATIVA até um capítulo (branch escrita-zero: só o escrito).
    restore_from: 'default' → data/revisoes_hostis.json (produção canônica) ·
    caminho alternativo (ex.: revisoes_hostis_v2.json) · None → não restaura."""
    import json
    from pathlib import Path

    r = check_producao(db_path, upto_key=upto_key)
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
    # restaura respostas do arquivo versionado — POR produção (canônica × v2)
    if restore_from == "default":
        src = Path(__file__).resolve().parents[2] / "data" / "revisoes_hostis.json"
    else:
        src = Path(restore_from) if restore_from else None
    if src and src.exists():
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
    """Upsert do arquivo versionado → DB (respostas persistem entre rebuilds).
    IDs do arquivo NÃO são confiados: colisão aloca próximo H#### livre."""
    import json
    from pathlib import Path

    rows = json.loads(Path(src).read_text(encoding="utf-8"))
    engine = create_db(db_path)
    restaurados = 0
    with Session(engine) as s:
        by_achado = {x.achado: x for x in s.exec(select(RevisaoHostil)).all()}
        used_ids = {x.item_id for x in s.exec(select(RevisaoHostil)).all()}

        def _next_id() -> str:
            n = len(used_ids) + 1
            while f"H{n:04d}" in used_ids:
                n += 1
            nid = f"H{n:04d}"
            used_ids.add(nid)
            return nid

        for r in rows:
            alvo = by_achado.get(r["achado"])
            if alvo is None:
                alvo = RevisaoHostil(
                    item_id=_next_id(),
                    cap_key=r["cap_key"],
                    tipo=r.get("tipo", "hostil"),
                    achado=r["achado"],
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
