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
from thesis_engine.ingest.experiments import get_value
from thesis_engine.models import Block, Section

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
