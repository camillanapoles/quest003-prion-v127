"""Gates de integridade — regras de ouro da autora, agora mecânicas.

check_sec43: reconciliação JSONs do registro ↔ tabela §4.3 da tese.
  Para cada âncora (arquivo→caminho→valor esperado↔forma PT-BR na tabela):
    1. o valor EXISTE no NumberValue com o valor exato;
    2. a forma PT-BR aparece no bloco-tabela canônico de §4.3.
  Falha (ValueError) se qualquer âncora sumir ou divergir — mata número digitado.
"""
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
