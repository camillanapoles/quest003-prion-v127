"""Gates de integridade — regras de ouro da autora, agora mecânicas.

check_sec43: reconciliação JSONs do registro ↔ tabela §4.3 da tese.
  Para cada âncora (arquivo→caminho→valor esperado↔forma PT-BR na tabela):
    1. o valor EXISTE no NumberValue com o valor exato;
    2. a forma PT-BR aparece no bloco-tabela canônico de §4.3.
  Falha (ValueError) se qualquer âncora sumir ou divergir — mata número digitado.
"""
import re

from sqlmodel import Session, select

from thesis_engine.db import create_db
from thesis_engine.ingest.experiments import REGISTRY_JSONS, get_value
from thesis_engine.models import (
    Block,
    Chapter,
    Claim,
    GraphNode,
    PlanChapter,
    Section,
    Source,
)

# (label, file_stem, json_path, valor_esperado, fragmento PT-BR na tabela §4.3)
_ANCORA43: tuple[tuple[str, str, str, float, str], ...] = (
    ("cenárioB-piso", "p024_human", "summary.theta_range[0]", 0.333, "0,333"),
    ("cenárioB-teto", "p024_human", "summary.theta_range[1]", 0.400, "0,400"),
    ("kmin-humano-KtLe1", "p024_human", "rows[0].kappa_min", 1.5, "1,5"),
    ("kmin-humano-Kt2", "p024_human", "rows[2].kappa_min", 2.0, "2,0"),
    ("titulacao-Kt1", "m31_u1u2", "u1_kreq.1", 1.5, "1,5"),
    ("titulacao-Kt2", "m31_u1u2", "u1_kreq.2", 2.0, "2→2"),
    ("titulacao-Kt4-superlinear", "m31_u1u2", "u1_kreq.4", 8.0, "4→8"),
    ("hamster-refutada-0.659", "p024_hamster", "rows[1].R_by_kappa.2.0", 0.659, "0,659"),
    ("θ*-mouse-ref", "p024_mouse", "summary.theta_mouse_ref", 0.333, "0,333"),
    ("θ*-hamster-ref", "p024_hamster", "summary.theta_mouse_ref", 0.333, "0,333"),
    ("θ*-human-ref", "p024_human", "summary.theta_mouse_ref", 0.333, "0,333"),
    ("θ*-vole-ref", "p024_vole", "summary.theta_mouse_ref", 0.333, "0,333"),
)


def check_sec43(db_path: str) -> dict:
    engine = create_db(db_path)
    with Session(engine) as s:
        sec = s.exec(select(Section).where(Section.label == "4.3")).first()
        if not sec:
            raise ValueError("seção §4.3 não encontrada no grafo")
        table = s.exec(
            select(Block).where(Block.sec_id == sec.sec_id, Block.block_type == "table")
        ).first()
        if not table:
            raise ValueError(f"bloco-tabela ausente em §4.3 (sec_id={sec.sec_id})")
        content = table.content

    problemas: list[str] = []
    ancoras: list[dict] = []
    for label, stem, path, expected, ptbr in _ANCORA43:
        try:
            got = get_value(db_path, stem, path)
        except KeyError as e:
            problemas.append(f"{label}: ausente no registro ({e})")
            continue
        if abs(got - expected) > 1e-9:
            problemas.append(f"{label}: registro={got} ≠ esperado={expected}")
        if ptbr not in content:
            problemas.append(f"{label}: forma PT-BR {ptbr!r} não está na tabela §4.3")
        ancoras.append(
            {"label": label, "stem": stem, "path": path, "valor": got, "ptbr": ptbr}
        )
    if problemas:
        raise ValueError("gate §4.3 FALHOU:\n  - " + "\n  - ".join(problemas))
    return {"ok": True, "ancoras": ancoras, "table_block": table.block_id}


# ============ F2.5 — gates de estilo (style_profile.md, calibrados no canônico) ============

_PROIBIDAS = ("promissor", "futuros estudos")
_DOI = re.compile(r"10\.\d{4,}/\S+")
_VERSAO = re.compile(r"\bv\d+\.\d+\b")
_SREF = re.compile(r"§\s?\d+(?:\.\d+)?")
_MILHAR = re.compile(r"\b\d{1,2}\.\d{3}(?=\s|anos|\b)")
_PAREN_REF = re.compile(r"\(\d+\.\d+[^)]*\)")
_DECIMAL = re.compile(r"\b(\d+)\.(\d+)\b")


def _section_like(m: re.Match) -> bool:
    """2.7/9.3/1.2 = ref de seção em prosa (tese tem 13 capítulos: N.M com N≤13, M de 1 dígito)."""
    left, right = m.group(1), m.group(2)
    return len(right) == 1 and 1 <= int(left) <= 13


def check_style(db_path: str) -> dict:
    """G1 proibições · G2 openers clínicos ≥3 · G3 tier na seção com dose µg · G4 decimais PT-BR."""
    engine = create_db(db_path)
    with Session(engine) as s:
        blocks = s.exec(select(Block)).all()

    problemas: list[str] = []
    proib: list[tuple[str, str]] = []
    for b in blocks:
        low = b.content.lower()
        for w in _PROIBIDAS:
            if w in low:
                proib.append((b.block_id, w))
    if proib:
        problemas.append(f"proibições ativas: {proib}")

    openers = [b for b in blocks if b.function == "clinical-opener"]
    if len(openers) < 3:
        problemas.append(f"openers clínicos < 3 (achados {len(openers)}) — convenção quebrada")

    # G3: saída de dose no B4 (aplicação — onde a dose é PRODUZIDA) exige tier na
    # seção (padrão da autora: tier no título — §6.3 [SIM-planejamento]). Menções
    # narrativas em outros blueprints são referências, não saída de dose.
    _DOSE_SIG = re.compile(r"µg\s+(?:de\s+)?V127|\d+(?:[,.]\d+)?\s*[–-]?\s*\d*(?:[,.]\d+)?\s*µg")
    key_of = lambda b: b.sec_id or b.chap_id or "?"
    dose_secs = {
        key_of(b) for b in blocks if b.blueprint == "B4" and _DOSE_SIG.search(b.content)
    }
    tiers_by_sec: dict[str, set] = {}
    for b in blocks:
        k = key_of(b)
        if k in dose_secs:
            tiers_by_sec.setdefault(k, set()).update(b.tiers)
    for sec, tiers in tiers_by_sec.items():
        if not tiers:
            problemas.append(f"seção {sec} tem saída de dose (µg) sem tier em nenhum bloco")

    for b in blocks:
        if b.block_type != "paragraph":
            continue
        txt = _DOI.sub("", b.content)
        txt = _VERSAO.sub("", txt)
        txt = _SREF.sub("", txt)
        txt = _MILHAR.sub("", txt)
        txt = _PAREN_REF.sub("", txt)
        hits = [m.group(0) for m in _DECIMAL.finditer(txt) if not _section_like(m)]
        if hits:
            problemas.append(f"{b.block_id}: decimal com ponto em prosa PT-BR: {hits}")

    if problemas:
        raise ValueError("gate de estilo FALHOU:\n  - " + "\n  - ".join(problemas))
    return {
        "ok": True,
        "clinical_openers": len(openers),
        "proibicoes": len(proib),
        "secoes_com_dose": len(tiers_by_sec),
    }


# ============ F5 — integração total do grafo (refs/FKs/bindings) ============

_CAP_NUM = re.compile(r"CAPÍTULO (\d+)")
# Refs-legadas ao braço-paper (paper/manuscript), validadas EXPRESSAMENTE pela
# autora em 28/08 no merge do PR #2 (linha 136 do canônico). Não são quebras.
_LEGACY_REFS = frozenset({"1-bis", "2-bis"})


def check_bindings(db_path: str) -> dict:
    """Blocos 100% integrados: FKs válidas · claims ⊆ registro · evidências ⊆ fontes
    · toda §ref resolve (label de seção ∪ nº de capítulo ∪ legado documentado)."""
    engine = create_db(db_path)
    with Session(engine) as s:
        blocks = s.exec(select(Block)).all()
        chapters = s.exec(select(Chapter)).all()
        sections = s.exec(select(Section)).all()
        claim_ids = set(s.exec(select(Claim.claim_id)).all())
        source_ids = set(s.exec(select(Source.evidence_id)).all())

    problemas: list[str] = []
    chap_ids = {c.chap_id for c in chapters}
    sec_ids = {x.sec_id for x in sections}
    for b in blocks:
        if b.chap_id and b.chap_id not in chap_ids:
            problemas.append(f"{b.block_id}: chap_id inválido {b.chap_id!r}")
        if b.sec_id and b.sec_id not in sec_ids:
            problemas.append(f"{b.block_id}: sec_id inválido {b.sec_id!r}")
        ghosts = set(b.claim_ids) - claim_ids
        if ghosts:
            problemas.append(f"{b.block_id}: claims sem registro {sorted(ghosts)}")
        ev_ghosts = set(b.evidence_ids) - source_ids
        if ev_ghosts:
            problemas.append(f"{b.block_id}: evidências sem fonte {sorted(ev_ghosts)}")

    labels = {x.label for x in sections if x.label}
    chap_nums = {m.group(1) for c in chapters if (m := _CAP_NUM.search(c.title))}
    resolved: set[str] = set()
    legacy: set[str] = set()
    dangling: list[str] = []
    for b in blocks:
        for r in b.cross_refs:
            ref = r.rstrip(".")
            if ref in _LEGACY_REFS:
                legacy.add(ref)
            elif ref in labels or ref in chap_nums:
                resolved.add(ref)
            else:
                dangling.append(f"{b.block_id}:§{ref}")
    if dangling:
        problemas.append(f"§refs penduradas (sem header correspondente): {sorted(dangling)}")

    if problemas:
        raise ValueError("gate de bindings FALHOU:\n  - " + "\n  - ".join(problemas))
    return {
        "ok": True,
        "refs": {"resolved": sorted(resolved), "legacy": sorted(legacy), "dangling": []},
        "claims_citadas": len({c for b in blocks for c in b.claim_ids}),
    }


# ============ F5.7 — gate G7: plano global ↔ tese realizada ============

# Figuras do braço-paper, pré-existentes à tese (figure_asset_map.md) — não cobardas
_LEGACY_FIGS = frozenset({"Fig.1", "Fig.2", "Fig.3"})
_CANON_TOKENS = ("F-43", "F-44", "H-P3", "THETA_STAR")


def check_plano(db_path: str) -> dict:
    """Congruência plano↔realizado: 17↔17 capítulos · ordem contínua · toda fonte
    do plano resolve (claims⊆registro · figuras na tese · JSONs do registro ·
    tokens-canon no grafo · comunidades citadas existem)."""
    engine = create_db(db_path)
    with Session(engine) as s:
        plan = s.exec(select(PlanChapter)).all()
        chapters = s.exec(select(Chapter)).all()
        blocks = s.exec(select(Block)).all()
        claim_ids = set(s.exec(select(Claim.claim_id)).all())
        graph_nodes = s.exec(select(GraphNode)).all()

    problemas: list[str] = []
    plan_keys = {p.chap_key for p in plan}
    chap_keys = {c.chap_id for c in chapters}
    if plan_keys != chap_keys:
        problemas.append(
            f"plan↔capítulos divergem: só-no-plano={sorted(plan_keys - chap_keys)} "
            f"só-na-tese={sorted(chap_keys - plan_keys)}"
        )
    ordens = sorted(p.ordem for p in plan)
    if ordens != list(range(len(plan))):
        problemas.append(f"ordem do plano não é contínua 0..{len(plan) - 1}: {ordens}")

    body = "\n".join(b.content for b in blocks)
    graph_text = " ".join(f"{n.label} {n.source_file} {n.community_name}" for n in graph_nodes)
    communities = {n.community_name for n in graph_nodes if n.community_name}

    for p in plan:
        for f in p.fontes:
            tipo, ref = f.get("tipo", ""), f.get("ref", "")
            if tipo == "claim":
                for cid in re.findall(r"C\d{3}", ref):
                    if cid not in claim_ids:
                        problemas.append(f"{p.chap_key}: plano cita claim sem registro {cid}")
            elif tipo == "figura":
                for fig in re.findall(r"Fig\.\d", ref):
                    if fig in _LEGACY_FIGS:
                        continue
                    n = fig.split(".")[1]
                    if f"Figura {n}" not in body:
                        problemas.append(f"{p.chap_key}: plano cita {fig} ausente da tese")
            elif tipo == "json":
                for jf in re.findall(r"[\w]+(?:_\{[^}]*\})?\.json", ref):
                    stem = jf.split("{")[0].replace(".json", "")
                    if not any(stem in src for src in REGISTRY_JSONS):
                        problemas.append(f"{p.chap_key}: plano cita JSON fora do registro {stem}")
            elif tipo == "canon":
                if graph_nodes:
                    for tok in (t for t in _CANON_TOKENS if t in ref):
                        if tok not in graph_text:
                            problemas.append(f"{p.chap_key}: token-canon {tok} ausente do grafo")
            elif tipo == "grafo":
                m = re.search(r"comunidade\s+'([^']+)'", ref)
                if m and m.group(1) not in communities:
                    problemas.append(f"{p.chap_key}: comunidade inexistente {m.group(1)!r}")

    if problemas:
        raise ValueError("gate do PLANO FALHOU:\n  - " + "\n  - ".join(problemas))
    return {
        "ok": True,
        "capitulos": len(plan),
        "fontes_validadas": sum(len(p.fontes) for p in plan),
        "comunidades_citadas": len(communities),
    }
