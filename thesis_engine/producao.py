"""HP-Cap — Harness de Produção por Capítulo (ordem topológica dos eventos).

Para cada capítulo NA ORDEM topológica (ORDEM_LOGICA), 3 gates:
  1. gate_objetivo  — cumpriu o objetivo dele na tese (plano↔realizado do capítulo)?
  2. gate_coesao    — manteve contexto/coesão com o que foi produzido ANTES dele
                      (termos definidos antes-ou-no-capítulo; refs anteriores resolvem)?
  3. gate_gaps      — gaps · dúvidas possíveis · termos novos sem definição ·
                      seções/elementos planejados realizados?

Achados HARD → gate VERMELHO (bloqueia). Achados SOFT (YELLOW) → viram ITENS da
fila do REVISOR HOSTIL (tabela revisaohostil) — que questiona apontamentos; a
elaboração da resposta usa critical-thinking (protocolo HOSTILE_REVIEW_PROTOCOL.md).
A revisão é CUMULATIVA: cada capítulo revalida a produção inteira até ele.
"""
import re
import unicodedata
from pathlib import Path

from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.models import Block, Chapter, Claim, PlanChapter, Section
from thesis_engine.plano_data import ORDEM_LOGICA

REPO = Path(__file__).resolve().parents[2]

ORDEM_PRODUCAO: list[str] = ["c00"] + [k for k, _, _ in ORDEM_LOGICA] + ["c14", "c15", "c16"]

# siglas genéricas acadêmicas que não exigem definição na tese
_ALLOWLIST = frozenset(
    {"ABNT", "NBR", "DOI", "PMID", "PMCID", "EN", "PT", "PDF", "CI", "DNA", "RNA", "URL", "ID"}
)
# fragmentos caps de prosa/refs PT que não são siglas (calibrado no canônico)
_STOPLIST = frozenset(
    {"AL", "DE", "EM", "BR", "HA", "HU", "EA", "IC", "AS", "OS", "AN", "IM", "IF",
      "COMO", "FINAL", "NOTA", "ANTES", "SEM", "TODO"}
)
# nomes internos do programa no padrão letra+dígito (A6, G0, T1, F1, R0, C0…) e famílias
_INTERNAL = re.compile(r"^[A-Z]\d[0-9A-Za-z-]*$")
_PROG = re.compile(r"^(WS|MV|OE|GATE)[-A-Z0-9.]*$")
_ACRONYM = re.compile(r"\b[A-Z]{2,6}[0-9A-Z-]*\b")
# placeholder REAL é TODO/TBD solto; {{TODO:...}} é marcador template documentado
# (ficha-da-autora / mecanismo guardião citado) → vira item de fila, não bloqueio
_PLACEHOLDER = re.compile(r"(?<!\{)\bTODO\b(?!:)|\bTBD\b|\bXXX\b|\bPLACEHOLDER\b")
_TPL_TODO = re.compile(r"\{\{TODO:[^}]*\}\}")


def _norm(t: str) -> str:
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()


def _siglas_definidas(blocks: list[Block]) -> set[str]:
    """Tokens definidos no bloco LISTA DE SIGLAS (c00)."""
    siglas: set[str] = set()
    for b in blocks:
        if b.block_type == "paragraph" and "—" in b.content and (
            "θ" in b.content or "tiers" in b.content or "GUM" in b.content
        ):
            siglas.update(_ACRONYM.findall(b.content))
    return siglas


def _cap_num(chap_key: str) -> int:
    return int(chap_key[1:])


def gate_objetivo(db_path: str, key: str) -> dict:
    """Tópicos numerados do plano ↔ seções realizadas; elementos prometidos presentes."""
    engine = create_db(db_path)
    with Session(engine) as s:
        plan = s.get(PlanChapter, key)
        secs = s.exec(select(Section).where(Section.chap_id == key)).all()
        chap_blocks = s.exec(select(Block).where(Block.chap_id == key)).all()
    body = "\n".join(b.content for b in chap_blocks)
    labels = {x.label for x in secs if x.label}
    faltando_secoes: list[str] = []
    keywords_total = keywords_ok = 0
    for topico in plan.topicos:
        m = re.match(r"^(\d+\.\d[A-Za-z0-9.\-]*)", topico)
        if m:
            want = m.group(1)
            if not any(l == want or l.startswith(want) for l in labels):
                faltando_secoes.append(want)
        else:
            keywords_total += 1
            tokens = [w for w in re.split(r"[^a-z0-9]+", _norm(topico)) if len(w) > 5]
            if not tokens or any(t in _norm(body) for t in tokens):
                keywords_ok += 1
    elementos_faltando = []
    for el in plan.elementos:
        for fig in re.findall(r"Fig\.(\d)", el):
            if f"Figura {fig}" not in body:
                elementos_faltando.append(f"Fig.{fig}")
    # Fig.1–3 são legado do braço-paper (figure_asset_map) — não cobardas pela tese
    elementos_faltando = [
        e for e in elementos_faltando if e not in {"Fig.1", "Fig.2", "Fig.3"}
    ]
    ok = not faltando_secoes and not elementos_faltando and (
        keywords_total == 0 or keywords_ok / keywords_total >= 0.8
    )
    yellow = []
    if keywords_total and keywords_ok / keywords_total < 0.8 and not faltando_secoes:
        yellow.append(
            f"cobertura de tópicos-chave {keywords_ok}/{keywords_total} < 80% — objetivo parcialmente cumprido"
        )
    return {
        "ok": ok,
        "hard": [f"seção planejada ausente: {x}" for x in faltando_secoes]
        + [f"elemento prometido ausente: {x}" for x in elementos_faltando],
        "yellow": yellow,
        "cobertura_keywords": f"{keywords_ok}/{keywords_total}",
    }


def gate_coesao(db_path: str, key: str) -> dict:
    """Termos-sigla usados no capítulo devem estar: na LISTA DE SIGLAS, definidos em
    capítulo ANTERIOR, ou definidos no próprio capítulo. FORWARD-refs: informativo."""
    engine = create_db(db_path)
    with Session(engine) as s:
        blocks = s.exec(select(Block).order_by(Block.seq)).all()
    ordem_atual = ORDEM_PRODUCAO.index(key)
    anteriores = set(ORDEM_PRODUCAO[: ordem_atual + 1])
    body_atual = "\n".join(
        b.content
        for b in blocks
        if b.chap_id == key and b.block_type in ("paragraph", "list")
    )
    body_anteriores = "\n".join(
        b.content
        for b in blocks
        if b.chap_id in ORDEM_PRODUCAO[:ordem_atual] and b.chap_id != "c14"
    )
    # recorrência: sigla de verdade aparece ≥2× na tese (one-off em refs é ruído)
    todo_corpo = "\n".join(
        b.content for b in blocks if b.chap_id != "c14" and b.block_type != "heading"
    )
    from collections import Counter

    contagem = Counter(_ACRONYM.findall(todo_corpo))
    siglas_c00 = _siglas_definidas([b for b in blocks if b.chap_id == "c00"])
    usados = set(_ACRONYM.findall(body_atual))
    nao_definidos = sorted(
        t
        for t in usados
        if t not in siglas_c00
        and t not in _ALLOWLIST
        and t not in _STOPLIST
        and not _INTERNAL.match(t)
        and not _PROG.match(t)
        and contagem.get(t, 0) >= 2
        and len(t) <= 5
        and t.rstrip("-") not in siglas_c00  # SLR- ≡ SLR (quebra de hífen)
        and t.rstrip("-") not in _ALLOWLIST
        and f"({t})" not in body_atual  # definido NO capítulo: "expansão (ACRÔNIMO)"
        and f"[{t}]:" not in body_atual  # ou tag-de-tier definida: "[SIM]: simulação…"
        and t not in body_anteriores  # já apareceu antes (contexto estabelecido)
    )
    forward_refs = sorted(
        {
            r
            for b in blocks
            if b.chap_id == key
            for r in b.cross_refs
            if r.rstrip(".").isdigit() and int(r.rstrip(".")) > _cap_num(key)
        }
    )
    return {
        "ok": not nao_definidos,
        "yellow": [f"termo novo sem definição prévia: {t}" for t in nao_definidos]
        + [f"forward-ref (promessa): §{r}" for r in forward_refs],
        "hard": [],
    }


def gate_gaps(db_path: str, key: str) -> dict:
    """Dúvidas prováveis: placeholders/TODOs, '?' em títulos de tabela, claims órfãs
    do capítulo (citadas no plano e ausentes do corpo)."""
    engine = create_db(db_path)
    with Session(engine) as s:
        plan = s.get(PlanChapter, key)
        chap_blocks = s.exec(select(Block).where(Block.chap_id == key)).all()
        blocks_all = s.exec(select(Block)).all()
        claim_ids = set(s.exec(select(Claim.claim_id)).all())
    body = "\n".join(b.content for b in chap_blocks)
    tpl_todos = _TPL_TODO.findall(body)  # fichas/mecanismos documentados → fila hostil
    placeholders = _PLACEHOLDER.findall(body)
    # marcador ** não-pareado no próprio bloco = markdown malformado no canônico
    nao_pareados = [
        b.block_id for b in chap_blocks if b.content.count("**") % 2 == 1
    ]
    claims_planejadas = {
        c for f in plan.fontes if f.get("tipo") == "claim" for c in re.findall(r"C\d{3}", f["ref"])
    }
    claims_no_corpo = {c for b in chap_blocks for c in b.claim_ids}
    # tags curtas [Cxxx] (tabelas §7.2/concordância) contam como presença NA TESE
    corpo_tese = "\n".join(b.content for b in blocks_all)
    orfas_reais = []  # ausente do capítulo E da tese = HARD; só do capítulo = YELLOW
    fora = sorted(claims_planejadas - claims_no_corpo)
    for c in fora:
        if f"claim:{c}" not in corpo_tese and f"[{c}]" not in corpo_tese:
            orfas_reais.append(c)
    em_outro_lugar = [c for c in fora if c not in orfas_reais]
    return {
        "ok": not placeholders and not orfas_reais,
        "hard": [f"placeholder no corpo: {p}" for p in placeholders]
        + [f"claim planejada ausente da TESE: {c}" for c in orfas_reais],
        "yellow": [f"{{{{TODO}}}} template a preencher: {t[:60]}" for t in tpl_todos]
        + [
            f"claim planejada p/ o capítulo realizada em outro (ou tag curta): {c}"
            for c in em_outro_lugar
        ]
        + [f"marcador ** não-pareado no bloco {bid} (markdown malformado)" for bid in nao_pareados],
    }


GATES = {"objetivo": gate_objetivo, "coesao": gate_coesao, "gaps": gate_gaps}


def check_producao(db_path: str, upto_key: str | None = None) -> dict:
    """Revisão CUMULATIVA: roda os 3 gates para cada capítulo na ordem topológica,
    até `upto_key` (inclusive). Retorna relatório; HARD→ok False; YELLOW→fila hostil."""
    keys = ORDEM_PRODUCAO if upto_key is None else ORDEM_PRODUCAO[: ORDEM_PRODUCAO.index(upto_key) + 1]
    relatorio: list[dict] = []
    hard_total: list[str] = []
    yellow_total: list[str] = []
    for key in keys:
        chap: dict = {"cap": key, "gates": {}}
        for gname, gfn in GATES.items():
            r = gfn(db_path, key)
            chap["gates"][gname] = r
            hard_total += [f"{key}/{gname}: {h}" for h in r.get("hard", [])]
            yellow_total += [f"{key}/{gname}: {y}" for y in r.get("yellow", [])]
        chap["ok"] = all(g["ok"] for g in chap["gates"].values())
        relatorio.append(chap)
    return {
        "ok": not hard_total,
        "capitulos": len(relatorio),
        "relatorio": relatorio,
        "hard": hard_total,
        "yellow": yellow_total,
    }


def assert_producao_ok(db_path: str) -> dict:
    """Modo GATE (CLI/CI): levanta ValueError se houver HARD; YELLOW vai à fila hostil."""
    r = check_producao(db_path)
    if r["hard"]:
        raise ValueError(
            f"gates de produção FALHARAM (HARD):\n  - " + "\n  - ".join(r["hard"])
        )
    return {"ok": True, "capitulos": r["capitulos"], "yellow": len(r["yellow"])}
