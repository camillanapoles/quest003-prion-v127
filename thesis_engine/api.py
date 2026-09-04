"""FastAPI do thesis_engine — CRUD guardado + queries + gates + render.

Regras:
  - Registro probatório (claims/sources/nfacts/numbervalues) é READ-ONLY (imutabilidade).
  - Escritas só em Block, ciclo Modo B: create→draft · PATCH edita draft ·
    POST /status transiciona (sempre p/ frente); author_approved exige `approver` (humana).
  - Toda escrita valida via write-guard §3.5 e claims citadas ⊆ registro.
  - GET /render/md devolve SÓ blocos canônicos (drafts nunca vazam).
"""
from typing import Optional

from fastapi import FastAPI, HTTPException, Response
from datetime import datetime
from pydantic import BaseModel
from sqlmodel import Session, func, select

from thesis_engine.categorize import validate_block_write
from thesis_engine.db import create_db
from thesis_engine.ingest.tese import extract_meta
from thesis_engine.integrity import check_plano, check_sec43, check_style
from thesis_engine.models import (
    Block,
    Chapter,
    Claim,
    GraphNode,
    MethodFact,
    NFact,
    NumberValue,
    PlanChapter,
    ResultFact,
    Section,
    Source,
)
from thesis_engine.render.md import render_md


class BlockIn(BaseModel):
    chap_id: str
    sec_id: Optional[str] = None
    block_type: str = "paragraph"
    content: str
    function: Optional[str] = None
    blueprint: str
    tiers: Optional[list[str]] = None


class BlockPatch(BaseModel):
    content: Optional[str] = None
    function: Optional[str] = None
    blueprint: Optional[str] = None


class StatusIn(BaseModel):
    status: str
    approver: Optional[str] = None  # obrigatório p/ author_approved (humana)


def create_app(db_path: str) -> FastAPI:
    app = FastAPI(title="thesis_engine", version="0.1.0")
    app.state.db_path = db_path

    def sess() -> Session:
        return Session(create_db(app.state.db_path))

    # ---------------- health ----------------
    @app.get("/health")
    def health():
        with sess() as s:
            counts = {
                "claims": s.exec(select(func.count()).select_from(Claim)).one(),
                "sources": s.exec(select(func.count()).select_from(Source)).one(),
                "nfacts": s.exec(select(func.count()).select_from(NFact)).one(),
                "blocks": s.exec(select(func.count()).select_from(Block)).one(),
                "numbervalues": s.exec(select(func.count()).select_from(NumberValue)).one(),
            }
        return {"ok": True, "counts": counts}

    # ---------------- registro (READ-ONLY) ----------------
    @app.get("/chapters")
    def chapters():
        with sess() as s:
            return s.exec(select(Chapter).order_by(Chapter.order_idx)).all()

    @app.get("/sections")
    def sections(chap_id: Optional[str] = None):
        with sess() as s:
            q = select(Section).order_by(Section.chap_id, Section.order_idx)
            if chap_id:
                q = q.where(Section.chap_id == chap_id)
            return s.exec(q).all()

    @app.get("/blocks")
    def blocks(
        sec_id: Optional[str] = None,
        chap_id: Optional[str] = None,
        block_type: Optional[str] = None,
        claim_id: Optional[str] = None,
        blueprint: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
    ):
        with sess() as s:
            q = select(Block).order_by(Block.seq)
            if sec_id:
                q = q.where(Block.sec_id == sec_id)
            if chap_id:
                q = q.where(Block.chap_id == chap_id)
            if block_type:
                q = q.where(Block.block_type == block_type)
            if blueprint:
                q = q.where(Block.blueprint == blueprint)
            rows = s.exec(q).all()
        if claim_id:
            rows = [b for b in rows if claim_id in b.claim_ids]
        return rows[offset : offset + limit]

    @app.get("/blocks/{block_id}")
    def block(block_id: str):
        with sess() as s:
            b = s.get(Block, block_id)
        if not b:
            raise HTTPException(404, f"bloco {block_id} inexistente")
        return b

    @app.get("/claims")
    def claims(section: Optional[str] = None):
        with sess() as s:
            q = select(Claim).order_by(Claim.claim_id)
            if section:
                q = q.where(Claim.section.contains(section))
            return s.exec(q).all()

    @app.get("/claims/{claim_id}")
    def claim(claim_id: str):
        with sess() as s:
            c = s.get(Claim, claim_id)
        if not c:
            raise HTTPException(404)
        return c

    @app.get("/sources")
    def sources(source_type: Optional[str] = None):
        with sess() as s:
            q = select(Source).order_by(Source.evidence_id)
            if source_type:
                q = q.where(Source.source_type == source_type)
            return s.exec(q).all()

    @app.get("/sources/{evidence_id}")
    def source(evidence_id: str):
        with sess() as s:
            e = s.get(Source, evidence_id)
        if not e:
            raise HTTPException(404)
        return e

    @app.get("/nfacts")
    def nfacts(evidence_id: Optional[str] = None):
        with sess() as s:
            rows = s.exec(select(NFact).order_by(NFact.fact_id)).all()
        if evidence_id:
            rows = [n for n in rows if evidence_id in n.evidence_ids]
        return rows

    @app.get("/numbervalues")
    def numbervalue(stem: str, path: str):
        with sess() as s:
            rows = s.exec(
                select(NumberValue).where(NumberValue.json_path == path)
            ).all()
        rows = [v for v in rows if stem in v.source_file]
        if not rows:
            raise HTTPException(404, f"lineage ausente: {stem} · {path}")
        return rows[0]

    # ---------------- escrita Modo B (Block) ----------------
    def _claims_registradas(s: Session, ids: list[str]) -> set[str]:
        known = set()
        for cid in ids:
            if s.get(Claim, cid) is None:
                known.add(cid)
        return known  # devolve as DESCONHECIDAS

    @app.post("/blocks", status_code=201)
    def create_block(b: BlockIn):
        meta = extract_meta(b.content)
        with sess() as s:
            ghosts = _claims_registradas(s, meta["claim_ids"])
            if ghosts:
                raise HTTPException(422, f"claims sem registro: {sorted(ghosts)}")
            max_seq = s.exec(select(func.max(Block.seq))).one() or 0
            try:
                validate_block_write(
                    function=b.function,
                    blueprint=b.blueprint,
                    status="draft",
                    block_type=b.block_type,
                )
            except ValueError as e:
                raise HTTPException(422, str(e))
            nb = Block(
                block_id=f"D{max_seq + 1:04d}",
                seq=max_seq + 1,
                block_type=b.block_type,
                chap_id=b.chap_id,
                sec_id=b.sec_id,
                content=b.content,
                claim_ids=meta["claim_ids"],
                evidence_ids=meta["evidence_ids"],
                cross_refs=meta["cross_refs"],
                tiers=b.tiers or meta["tiers"],
                status="draft",
                function=b.function,
                blueprint=b.blueprint,
            )
            s.add(nb)
            s.commit()
            s.refresh(nb)
            return nb

    @app.patch("/blocks/{block_id}")
    def patch_block(block_id: str, p: BlockPatch):
        with sess() as s:
            b = s.get(Block, block_id)
            if not b:
                raise HTTPException(404)
            if b.status == "canonico":
                raise HTTPException(409, "bloco canônico é conservação (Modo A): não editável")
            meta = extract_meta(p.content) if p.content is not None else None
            if meta:
                ghosts = _claims_registradas(s, meta["claim_ids"])
                if ghosts:
                    raise HTTPException(422, f"claims sem registro: {sorted(ghosts)}")
            try:
                validate_block_write(
                    function=p.function if p.function is not None else b.function,
                    blueprint=p.blueprint if p.blueprint is not None else b.blueprint,
                    status=b.status,
                    prev_status=b.status,
                    block_type=b.block_type,
                )
            except ValueError as e:
                raise HTTPException(422, str(e))
            if p.content is not None:
                b.content = p.content
                b.claim_ids = meta["claim_ids"]
                b.evidence_ids = meta["evidence_ids"]
                b.cross_refs = meta["cross_refs"]
                if not b.tiers:
                    b.tiers = meta["tiers"]
            if p.function is not None:
                b.function = p.function
            if p.blueprint is not None:
                b.blueprint = p.blueprint
            s.add(b)
            s.commit()
            s.refresh(b)
            return b

    @app.post("/blocks/{block_id}/status")
    def set_status(block_id: str, body: StatusIn):
        with sess() as s:
            b = s.get(Block, block_id)
            if not b:
                raise HTTPException(404)
            is_human = bool(body.approver)
            try:
                validate_block_write(
                    function=b.function,
                    blueprint=b.blueprint,
                    status=body.status,
                    prev_status=b.status,
                    is_human=is_human,
                    block_type=b.block_type,
                )
            except ValueError as e:
                raise HTTPException(422, str(e))
            if body.status == "author_approved" and not body.approver:
                raise HTTPException(422, "approver é obrigatório (aprovação humana)")
            b.status = body.status
            s.add(b)
            s.commit()
            s.refresh(b)
            return b

    # ---------------- WRITING CYCLE (API-driven, não mais documento-driven) ----------------
    from thesis_engine.models import ReviewQuestion, StyleRule, WritingCycle

    @app.get("/cycle/questions")
    def cycle_questions():
        """As 7 perguntas do revisor hostil — DO BANCO (não de markdown)."""
        with sess() as s:
            return s.exec(select(ReviewQuestion).order_by(ReviewQuestion.letra)).all()

    @app.get("/cycle/style-rules")
    def cycle_style_rules():
        """Regras de estilo — DO BANCO (não de hardcode Python)."""
        with sess() as s:
            return s.exec(select(StyleRule).order_by(StyleRule.rule_id)).all()

    @app.post("/cycle/{cap_key}/start")
    def cycle_start(cap_key: str):
        """Inicia o ciclo de escrita de um capítulo → retorna BRIEF + cria WritingCycle."""
        from thesis_engine.escritor import brief_capitulo

        brief = brief_capitulo(app.state.db_path, cap_key)
        with sess() as s:
            existing = s.exec(
                select(WritingCycle).where(WritingCycle.cap_key == cap_key)
            ).first()
            if existing:
                return {
                    "cycle": existing,
                    "brief": brief,
                    "message": "ciclo já existe — use /submit ou /status",
                }
            cycle = WritingCycle(
                cycle_id=f"CY-{cap_key}-{datetime.now():%H%M%S}",
                cap_key=cap_key,
                estado="brief",
                created_at=str(datetime.now()),
            )
            s.add(cycle)
            s.commit()
            s.refresh(cycle)
        return {"cycle": cycle, "brief": brief}

    @app.post("/cycle/{cap_key}/submit")
    def cycle_submit(cap_key: str, body: dict):
        """Submete rascunho → guarda no DB → roda guard → transiciona para 'hostile'."""
        from thesis_engine.escritor import reingest_capitulo

        markdown = body.get("markdown", "")
        if not markdown:
            raise HTTPException(422, "markdown obrigatório")
        try:
            r = reingest_capitulo(app.state.db_path, cap_key, markdown)
        except ValueError as e:
            raise HTTPException(422, str(e))
        with sess() as s:
            cycle = s.exec(
                select(WritingCycle).where(WritingCycle.cap_key == cap_key)
            ).first()
            if cycle:
                cycle.estado = "hostile"
                cycle.updated_at = str(datetime.now())
                s.add(cycle)
                s.commit()
        return {"ingested": r, "estado": "hostile"}

    @app.get("/cycle/{cap_key}/status")
    def cycle_status(cap_key: str):
        """Estado completo: ciclo + gates + hostil + ações + style rules aplicáveis."""
        from thesis_engine.escritor import hostil_aprova

        with sess() as s:
            cycle = s.exec(
                select(WritingCycle).where(WritingCycle.cap_key == cap_key)
            ).first()
            if not cycle:
                raise HTTPException(404, f"ciclo de {cap_key} não iniciado — use /start")
        aprov = hostil_aprova(app.state.db_path, cap_key)
        return {"cycle": cycle, "aprovacao": aprov}

    @app.post("/cycle/{cap_key}/approve")
    def cycle_approve(cap_key: str, body: dict):
        """Tenta aprovar — só se TODAS as condições verdes. Caso contrário, bloqueia com motivo."""
        from thesis_engine.escritor import hostil_aprova

        r = hostil_aprova(app.state.db_path, cap_key)
        if not r["aprova"]:
            motivos = []
            if r["abertos"]:
                motivos.append(f"itens hostis abertos: {r['abertos']}")
            if not all(r["gates"].values()):
                motivos.append(f"gates vermelhos: {[g for g, v in r['gates'].items() if not v]}")
            if r["acoes_pendentes_no_local"]:
                motivos.append(f"ações pendentes: {r['acoes_pendentes_no_local']}")
            if not r["hostil_falou"]:
                motivos.append("hostil nunca questionou a prosa deste capítulo")
            raise HTTPException(409, "APROVAÇÃO BLOQUEADA: " + "; ".join(motivos))
        with sess() as s:
            cycle = s.exec(
                select(WritingCycle).where(WritingCycle.cap_key == cap_key)
            ).first()
            if cycle:
                cycle.estado = "approved"
                cycle.updated_at = str(datetime.now())
                s.add(cycle)
                s.commit()
        return {"aprovado": True, "cycle": cycle}

    # ---------------- plano global + grafo ----------------
    @app.get("/plano")
    def plano():
        with sess() as s:
            return s.exec(select(PlanChapter).order_by(PlanChapter.ordem)).all()

    @app.get("/graph")
    def graph(community: Optional[str] = None, q: Optional[str] = None, limit: int = 50):
        """Consulta o grafo dos 3 worktrees (canon/guardian/knowledge)."""
        with sess() as s:
            rows = s.exec(select(GraphNode)).all()
        if community:
            rows = [n for n in rows if community.lower() in n.community_name.lower()]
        if q:
            rows = [n for n in rows if q.lower() in n.label.lower() or q.lower() in n.source_file.lower()]
        return rows[:limit]

    # ---------------- HP-Cap: produção + fila hostil ----------------
    @app.get("/producao")
    def producao(upto: Optional[str] = None):
        from thesis_engine.producao import check_producao

        return check_producao(app.state.db_path, upto_key=upto)

    @app.get("/revisoes")
    def revisoes(cap_key: Optional[str] = None, status: Optional[str] = None):
        from thesis_engine.models import RevisaoHostil

        with sess() as s:
            rows = s.exec(select(RevisaoHostil)).all()
        if cap_key:
            rows = [r for r in rows if r.cap_key == cap_key]
        if status:
            rows = [r for r in rows if r.status == status]
        return rows

    class RespostaIn(BaseModel):
        resposta: str
        respondido_por: str  # quem elabora (critical thinking) — humana fecha definitivo
        emenda: bool = False  # True → status emendado

    @app.post("/revisoes/{item_id}/responder")
    def responder(item_id: str, body: RespostaIn):
        from thesis_engine.models import RevisaoHostil

        with sess() as s:
            item = s.get(RevisaoHostil, item_id)
            if not item:
                raise HTTPException(404)
            if item.status != "aberto":
                raise HTTPException(409, f"item já {item.status}")
            item.resposta = body.resposta
            item.respondido_por = body.respondido_por
            item.status = "emendado" if body.emenda else "respondido"
            s.add(item)
            s.commit()
            s.refresh(item)
            return item

    # ---------------- gates + render ----------------
    @app.get("/integrity")
    def integrity():
        out = {"ok": True, "sec43": None, "style": None, "plano": None}
        for name, fn in (
            ("sec43", check_sec43),
            ("style", check_style),
            ("plano", check_plano),
        ):
            try:
                out[name] = fn(app.state.db_path)
            except ValueError as e:
                out[name] = {"ok": False, "erro": str(e)}
                out["ok"] = False
        return out

    @app.get("/render/md")
    def render_md_endpoint():
        return Response(content=render_md(app.state.db_path), media_type="text/markdown")

    @app.get("/render/latex")
    def render_latex_endpoint(fmt: str = "abnt"):
        from thesis_engine.render.latex import render_latex

        if fmt not in ("abnt", "prova", "kappa"):
            raise HTTPException(422, "fmt ∈ {abnt, prova, kappa}")
        return Response(
            content=render_latex(app.state.db_path, fmt),
            media_type="application/x-tex",
        )

    return app
