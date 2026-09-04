"""ESCRITOR V2 — geração de texto DO ZERO a partir do banco (branch tese-escrita-zero).

Missão deste branch: produzir a tese SEM converter o texto canônico (Modo A).
Fonte de escrita = SOMENTE o banco: registro probatório (claims/fontes/N-fatos) ·
JSONs (NumberValue c/ lineage) · grafo canon · PLANO GLOBAL (objetivo/tópicos/
elementos/simplificação por capítulo). Ciclo HP-Cap completo: brief → rascunho →
write-guard → gates → revisor hostil → aprovação humana.
"""
import re
from pathlib import Path

from sqlmodel import Session, select

from thesis_engine.categorize import validate_block_write
from thesis_engine.db import create_db
from thesis_engine.ingest.experiments import ingest_experiments
from thesis_engine.ingest.graphify import ingest_graphify
from thesis_engine.ingest.plano import ingest_plano
from thesis_engine.ingest.registro import ingest_registro
from thesis_engine.ingest.tese import extract_meta, parse_blocks
from thesis_engine.models import Block, Chapter, Claim, NumberValue, PlanChapter, RevisaoHostil, Section, Source

REPO = Path(__file__).resolve().parents[1]  # escritor.py está em thesis_engine/ (1 nível)
V2_DB = str(REPO / "tese_v2.db")

# Títulos estruturais (metadados da arquitetura — não são "o texto")
V2_TITLES: dict[str, str] = {
    "c00": "ETRIZAÇÃO COMPUTACIONAL EM DOENÇAS PRIÔNICAS: APLICADA À PLATAFORMA TERAPÊUTICA PrP-V127",
    "c01": "CAPÍTULO 1 — NOTA INTRODUTÓRIA À BANCA",
    "c02": "CAPÍTULO 2 — INTRODUÇÃO",
    "c03": "CAPÍTULO 3 — FUNDAMENTAÇÃO",
    "c04": "CAPÍTULO 4 — BASE COMUM DE DADOS",
    "c05": "CAPÍTULO 5 — FUNDAMENTO: A INARIÂNCIA DE θ*",
    "c06": "CAPÍTULO 6 — APLICAÇÃO: O DESENHO TERAPÊUTICO EMERGE",
    "c07": "CAPÍTULO 7 — MÉTODOS: A ETRIZAÇÃO FORMALIZADA",
    "c08": "CAPÍTULO 8 — RESULTADOS COMO VALIDAÇÃO",
    "c09": "CAPÍTULO 9 — ACHADOS, IMPACTOS E ÁREAS CORRELATAS",
    "c10": "CAPÍTULO 10 — DISCUSSÃO",
    "c11": "CAPÍTULO 11 — CAMADA CLÍNICA",
    "c12": "CAPÍTULO 12 — LIMITAÇÕES COMO FRUTO",
    "c13": "CAPÍTULO 13 — CONCLUSÕES POR OBJETIVO",
    "c14": "REFERÊNCIAS",
    "c15": "APÊNDICE A — INVENTÁRIO E CONCORDÂNCIA",
    "c16": "APÊNDICE B — MAPA DA LÓGICA",
}


def setup_v2(db_path: str = V2_DB) -> dict:
    """DB v2: registro + dados + grafo + plano + ESTRUTURA VAZIA (nenhum texto)."""
    from sqlalchemy import text as sa_text
    from sqlmodel import SQLModel

    ingest_registro(db_path=db_path)
    ingest_experiments(db_path=db_path)
    ingest_graphify(db_path=db_path)
    ingest_plano(db_path=db_path)
    engine = create_db(db_path)
    with engine.connect() as conn:
        for tbl in ("block", "section", "chapter"):
            conn.execute(sa_text(f'DROP TABLE IF EXISTS "{tbl}"'))
        conn.commit()
    SQLModel.metadata.create_all(engine)
    with Session(engine) as s:
        for i, (k, title) in enumerate(sorted(V2_TITLES.items())):
            s.add(Chapter(chap_id=k, order_idx=i, title=title, level=1))
        s.commit()
        n = len(s.exec(select(Chapter)).all())
    return {"estrutura": n, "texto": "ZERO — nenhum bloco canônico ingerido"}


def brief_capitulo(db_path: str, key: str) -> dict:
    """O BRIEF do escritor: tudo que o banco sabe sobre este capítulo."""
    engine = create_db(db_path)
    with Session(engine) as s:
        plano = s.get(PlanChapter, key)
        claims = s.exec(select(Claim).order_by(Claim.claim_id)).all()
        sources = s.exec(select(Source)).all()
        nums = s.exec(select(NumberValue)).all()
    src_by_id = {x.evidence_id: x.title for x in sources}
    # claims cuja seção pertence ao capítulo (campo section: "1", "1.1", "1/3.1"…)
    cnum = str(int(key[1:]))  # c01 → "1" (normaliza zero à esquerda)
    mias = []
    for c in claims:
        secs = re.split(r"[/;,]", c.section)
        for sec in secs:
            sec = sec.strip()
            if sec == cnum or sec.startswith(f"{cnum}."):
                mias.append(c)
                break
    # âncoras numéricas do capítulo (NumberValue dos JSONs, amostra)
    ancoras = [n for n in nums if n.json_path.startswith("summary.")][:12]
    return {
        "cap": key,
        "titulo": V2_TITLES.get(key, key),
        "objetivo": plano.objetivo,
        "funcao": plano.funcao,
        "topicos": plano.topicos,
        "elementos": plano.elementos,
        "complicado": plano.complicado,
        "simplificar": plano.simplificar,
        "claims": [
            {
                "id": c.claim_id,
                "texto": c.claim_text,
                "evidencias": [src_by_id.get(e, e) for e in c.evidence_ids],
                "incerteza": c.uncertainty,
            }
            for c in mias
        ],
        "amostra_numeros": [
            {"path": a.json_path, "valor": a.value_float, "fonte": a.source_file} for a in ancoras
        ],
    }


def ingest_rascunho(db_path: str, key: str, markdown: str) -> dict:
    """Rascunho escrito → blocos DRAFT guardados (write-guard + claims⊆registro)."""
    engine = create_db(db_path)
    parsed = parse_blocks(markdown)
    with Session(engine) as s:
        plan = s.get(PlanChapter, key)
        known = set(s.exec(select(Claim.claim_id)).all())
        max_seq = s.exec(select(Block.seq)).all()
        seq = max(max_seq) if max_seq else 0
        n_sec = 0
        cur_sec = None
        criados = []
        for d in parsed:
            if d["block_type"] == "blank":
                continue
            seq += 1
            if d["block_type"] == "heading" and d["heading_level"] and d["heading_level"] >= 2:
                n_sec += 1
                cur_sec = f"{key}s{n_sec - 1:02d}"
                label_m = re.match(r"^(\d+\.\d[A-Za-z0-9.\-]*)", d["heading_text"] or "")
                s.add(
                    Section(
                        sec_id=cur_sec,
                        chap_id=key,
                        order_idx=n_sec - 1,
                        level=d["heading_level"],
                        label=label_m.group(1) if label_m else None,
                        title=d["heading_text"],
                    )
                )
            meta = extract_meta(d["content"])
            ghosts = set(meta["claim_ids"]) - known
            if ghosts:
                raise ValueError(f"rascunho cita claims sem registro: {sorted(ghosts)}")
            validate_block_write(
                function="exposition",  # padrão do escritor; recategorização na aprovação
                blueprint=plano_blueprint(key),
                status="draft",
                block_type=d["block_type"],
            )
            nb = Block(
                block_id=f"D{seq:04d}",
                seq=seq,
                block_type=d["block_type"],
                chap_id=key,
                sec_id=cur_sec,
                content=d["content"],
                heading_level=d.get("heading_level"),
                heading_text=d.get("heading_text"),
                claim_ids=meta["claim_ids"],
                evidence_ids=meta["evidence_ids"],
                cross_refs=meta["cross_refs"],
                tiers=meta["tiers"],
                status="draft",
                function="exposition",
                blueprint=plano_blueprint(key),
            )
            s.add(nb)
            criados.append(nb.block_id)
        s.commit()
    return {"rascunho": len(criados), "blocos": criados[:5] + (["…"] if len(criados) > 5 else [])}


def hostil_aprova(db_path: str, key: str) -> dict:
    """Condição de saída do LOOP (cycle-new): zero itens hostis ABERTOS do capítulo
    + 3 gates verdes. Só então render→RELATORIO→commit."""
    from thesis_engine.producao import GATES

    engine = create_db(db_path)
    with Session(engine) as s:
        itens = [i for i in s.exec(select(RevisaoHostil)).all() if i.cap_key == key]
    abertos = [i.item_id for i in itens if i.status == "aberto"]
    gates = {g: gfn(db_path, key) for g, gfn in GATES.items()}
    ok = not abertos and all(g["ok"] for g in gates.values())
    return {"aprova": ok, "abertos": abertos, "gates": {g: v["ok"] for g, v in gates.items()}}


def reingest_capitulo(db_path: str, key: str, markdown: str) -> dict:
    """Rodada do LOOP: substitui o rascunho do capítulo (wipe+ingest guardado)."""
    engine = create_db(db_path)
    with Session(engine) as s:
        for b in s.exec(select(Block).where(Block.chap_id == key)).all():
            s.delete(b)
        for x in s.exec(select(Section).where(Section.chap_id == key)).all():
            s.delete(x)
        s.commit()
    return ingest_rascunho(db_path, key, markdown)


def plano_blueprint(key: str) -> str:
    from thesis_engine.categorize import blueprint_for_chapter

    return blueprint_for_chapter(V2_TITLES.get(key, ""))


def save_brief(db_path: str, key: str, out_dir: str = None) -> str:
    """Salva o brief do capítulo em escrita-zero/briefs/ (folder único de saídas)."""
    b = brief_capitulo(db_path, key)
    out = Path(out_dir or (REPO / "escrita-zero" / "briefs"))
    out.mkdir(parents=True, exist_ok=True)
    L = [f"# BRIEF {b['cap']} — {b['titulo']}", "",
         f"**Objetivo:** {b['objetivo']}", f"**Função no arco:** {b['funcao']}", "",
         f"**Tópicos:** {' · '.join(b['topicos'])}", "",
         f"**Elementos:** {' · '.join(b['elementos'])}",
         f"**Complicado:** {b['complicado']}", f"**Simplificar:** {b['simplificar']}", "",
         "## Claims do capítulo (do registro)", ""]
    for c in b["claims"]:
        L.append(f"- **{c['id']}** ({c['incerteza']}): {c['texto']}")
        L.append(f"  ← {', '.join(e[:70] for e in c['evidencias'])}")
    if b["amostra_numeros"]:
        L += ["", "## Números âncora (lineage)", ""]
        for a in b["amostra_numeros"]:
            L.append(f"- `{a['fonte'].split('/')[-1]}::{a['path']}` = {a['valor']}")
    p = out / f"{key}_brief.md"
    p.write_text("\n".join(L) + "\n", encoding="utf-8")
    return str(p)


def render_v2(db_path: str, out_dir: str = None) -> dict:
    """Render do ramo v2: DRAFTS são o produto — FOLDER ÚNICO escrita-zero/render."""
    engine = create_db(db_path)
    out = Path(out_dir or (REPO / "escrita-zero" / "render"))
    out.mkdir(parents=True, exist_ok=True)
    with Session(engine) as s:
        chapters = s.exec(select(Chapter).order_by(Chapter.order_idx)).all()
        blocks = s.exec(select(Block).order_by(Block.seq)).all()
    by = {}
    for b in blocks:
        by.setdefault(b.chap_id, []).append(b)
    files = []
    for c in chapters:
        cb = by.get(c.chap_id, [])
        if not cb:
            continue
        fname = f"{c.order_idx:02d}-{re.sub(r'[^a-z0-9]+', '-', c.title.lower()).strip('-')[:40]}.md"
        (out / fname).write_text("".join(b.content for b in cb), encoding="utf-8")
        files.append(fname)
    return {"arquivos": files, "blocos": len(blocks)}
