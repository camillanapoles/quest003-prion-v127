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
from thesis_engine.models import AcaoDevedora, Block, Chapter, Claim, NumberValue, PlanChapter, RevisaoHostil, Section, Source

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
    "c17": "APÊNDICES C–F — SAP · DECISÃO · CUSTO · LINHAGEM",
}


def _seed_table_registry(db_path: str) -> int:
    """Registra TODAS as tabelas com categoria (setup vs execution) — DB auto-descritivo."""
    from thesis_engine._tables import _TABLES
    from thesis_engine.models import TableRegistry

    engine = create_db(db_path)
    with Session(engine) as s:
        for tbl, cat, desc in _TABLES:
            if not s.get(TableRegistry, tbl):
                s.add(TableRegistry(table_name=tbl, categoria=cat, descricao=desc))
        s.commit()
        return len(s.exec(select(TableRegistry)).all())


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
    _nreg = _seed_table_registry(db_path)
    from thesis_engine.guard import _seed_all_environment_rules
    _seed_all_environment_rules(db_path)
    return {"estrutura": n, "texto": "ZERO — nenhum bloco canônico ingerido", "table_registry": _nreg}


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
    """Condição de saída do LOOP (cycle-new): zero itens ABERTOS + 3 gates verdes +
    zero ações pendentes NO local + **HOSTIL FALOU** (≥1 item tipo 'hostil' no capítulo
    — sem isso um capítulo escrito 'por demonstração' seria aprovado sem revisão da
    prosa: brecha flagrada pela autora no RESUMO de c00)."""
    from thesis_engine.producao import GATES

    engine = create_db(db_path)
    with Session(engine) as s:
        itens = [i for i in s.exec(select(RevisaoHostil)).all() if i.cap_key == key]
        acoes_pendentes = [
            a.acao_id
            for a in s.exec(select(AcaoDevedora)).all()
            if a.cap_destino == key and a.status == "pendente"
        ]
    abertos = [i.item_id for i in itens if i.status == "aberto"]
    hostil_falou = any(i.tipo == "hostil" for i in itens)
    gates = {g: gfn(db_path, key) for g, gfn in GATES.items()}
    ok = not abertos and all(g["ok"] for g in gates.values()) and not acoes_pendentes and hostil_falou
    return {
        "aprova": ok,
        "abertos": abertos,
        "gates": {g: v["ok"] for g, v in gates.items()},
        "acoes_pendentes_no_local": acoes_pendentes,
        "hostil_falou": hostil_falou,
    }


def registrar_acao(db_path: str, origem_item_id: str, cap_destino: str, acao: str) -> str:
    """Resposta hostil prometeu ação em local → registro executável com id único."""
    engine = create_db(db_path)
    with Session(engine) as s:
        used = {a.acao_id for a in s.exec(select(AcaoDevedora)).all()}
        n = len(used) + 1
        while f"A{n:04d}" in used:
            n += 1
        aid = f"A{n:04d}"
        s.add(AcaoDevedora(acao_id=aid, origem_item_id=origem_item_id, cap_destino=cap_destino, acao=acao))
        s.commit()
        return aid


def fechar_acao(db_path: str, acao_id: str, evidencia: str, dispensa: bool = False) -> dict:
    engine = create_db(db_path)
    with Session(engine) as s:
        a = s.get(AcaoDevedora, acao_id)
        if not a:
            raise KeyError(acao_id)
        a.status = "dispensada" if dispensa else "executada"
        a.evidencia = evidencia
        s.add(a)
        s.commit()
        return {"acao_id": acao_id, "status": a.status, "evidencia": evidencia}


def check_acoes(db_path: str, cap: str | None = None) -> list[dict]:
    """Painel de ações devedoras (todas ou de um local/destino)."""
    engine = create_db(db_path)
    with Session(engine) as s:
        rows = s.exec(select(AcaoDevedora)).all()
    out = [
        {
            "acao_id": a.acao_id,
            "origem": a.origem_item_id,
            "local": a.cap_destino,
            "acao": a.acao,
            "status": a.status,
            "evidencia": a.evidencia,
        }
        for a in rows
        if cap is None or a.cap_destino == cap
    ]
    return out


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


def bootstrap_v2(db_path: str = V2_DB, archive: bool = True) -> dict:
    """BOOTSTRAP DO RECOMEÇO: arquiva → DB novo → semeia ações + REGRAS DE ESTILO +
    PERGUNTAS DO REVISOR (tudo como DADO OO, não documento)."""
    import json
    import shutil
    from datetime import datetime

    base = Path(REPO) / "escrita-zero"
    if archive and (base / "render").exists():
        dest = base / "arquivo" / f"rodada-{datetime.now():%Y%m%d-%H%M}"
        dest.mkdir(parents=True, exist_ok=True)
        for sub in ("render", "briefs"):
            if (base / sub).exists():
                shutil.copytree(base / sub, dest / sub, dirs_exist_ok=True)
        for f in ("fila_hostil.json", "acoes_devedoras.json", "RELATORIO.md"):
            if (base / f).exists():
                shutil.copy2(base / f, dest / f)
        if (Path(REPO) / "rascunhos").exists():
            shutil.copytree(Path(REPO) / "rascunhos", dest / "rascunhos", dirs_exist_ok=True)
    setup = setup_v2(db_path)

    # ---- semeia AÇÕES-mestra ----
    semeadas = [
        registrar_acao(db_path, "SEED", "c15",
            "Anexo: folhas de pré-registro + versão do motor/solver com datas impressas"),
        registrar_acao(db_path, "SEED", "c00",
            "LISTA DE SIGLAS consolidada + FICHA ACADÊMICA (ficha: EXCLUSIVA da autora)"),
        registrar_acao(db_path, "SEED", "c03",
            "Citar C027 (kindreds E200K); mapa visual de camadas se a autora optar"),
        registrar_acao(db_path, "SEED", "plano",
            "Refinar mapeamento section-do-registro→caps-v2 no brief"),
    ]

    # ---- semeia REGRAS DE ESTILO (StyleRule) — substitui _TERMONS_LLM hardcoded ----
    from thesis_engine.models import StyleRule

    _LLM_TERMS = [
        "verbatim", "delve", "furthermore", "moreover", "notably", "salient",
        "comprehensive", "multifaceted", "nuanced", "paradigm shift", "holistic",
        "it is worth noting", "in essence", "crucially", "pivotal", "landscape",
        "tapestry", "testament to", "underscores", "leverage", "robust framework",
        "seamlessly", "delineate", "elucidate", "underscore", "unprecedented",
        "myriad", "plethora", "instrumental in", "in conjunction with",
        "aforementioned", "henceforth", "whilst", "amongst", "notwithstanding",
    ]
    _PT_BANS = ["promissor", "futuros estudos"]

    engine = create_db(db_path)
    n_rules = 0
    with Session(engine) as s:
        for i, term in enumerate(_LLM_TERMS + _PT_BANS, 1):
            tipo = "llm_ban" if term in _LLM_TERMS else "pt_ban"
            s.add(StyleRule(rule_id=f"SR{i:04d}", tipo=tipo, valor=term,
                          descricao=f"{'Termo LLM' if tipo == 'llm_ban' else 'Proibição PT'}: {term}",
                          origem="bootstrap"))
            n_rules += 1
        s.commit()

    # ---- semeia PERGUNTAS DO REVISOR (ReviewQuestion) ----
    from thesis_engine.models import ReviewQuestion

    _QUESTIONS = [
        ("a", "A afirmação é factual e verificável no documento?", "claim tem E-ID · número tem lineage"),
        ("b", "A ligação premissa→conclusão é válida?", "sem salto lógico · sem petição de princípio"),
        ("c", "Há confundidores ou vieses não declarados?", "alternativas consideradas · incerteza dita"),
        ("d", "O número tem lineage?", "cifra via [claim:] ou NumberValue"),
        ("e", "O termo está definido antes do uso?", "LISTA DE SIGLAS ou 1ª ocorrência"),
        ("f", "A cronologia alegada tem prova no papel?", "folhas de registro no anexo · datas impressas"),
        ("g", "SOA HUMANO? (não SOA DE MÁQUINA?)", "sem termos LLM · linguagem de doutoranda brasileira"),
    ]
    with Session(engine) as s:
        for letra, pergunta, criterio in _QUESTIONS:
            s.add(ReviewQuestion(question_id=f"RQ-{letra}", letra=letra,
                               pergunta=pergunta, criterio_verificacao=criterio))
        s.commit()

    from sqlmodel import func
    from thesis_engine.models import AcaoDevedora, Block, Chapter, Claim

    with Session(engine) as s:
        estado = {
            "setup": setup,
            "blocos_texto": s.exec(select(func.count()).select_from(Block)).one(),
            "chapters": s.exec(select(func.count()).select_from(Chapter)).one(),
            "claims": s.exec(select(func.count()).select_from(Claim)).one(),
            "acoes_semeadas": len(s.exec(select(AcaoDevedora)).all()),
            "style_rules": s.exec(select(func.count()).select_from(StyleRule)).one(),
            "review_questions": s.exec(select(func.count()).select_from(ReviewQuestion)).one(),
        }
    return estado


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
