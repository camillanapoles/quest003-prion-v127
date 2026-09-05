"""Categorização obrigatória (§3.5 do plano) + write-guard.

ENUMs canônicos · inferência determinística (Modo A: backfill por posição/tags) ·
validação de escrita (Modo B: função/blueprint obrigatórios; author_approved só humano).
"""
import re

FUNCTIONS = frozenset(
    {
        "motivation",
        "method",
        "result",
        "interpretation",
        "limitation",
        "transition",
        "clinical-opener",
        "nota-banca",
        "exposition",
    }
)
BLUEPRINTS = frozenset({f"B{i}" for i in range(10)})
STATUS = frozenset({"canonico", "draft", "revised", "validated", "author_approved"})
_ORDER = ["canonico", "draft", "revised", "validated", "author_approved"]

STRUCTURAL = frozenset({"heading", "blank", "hr"})
_CLINICAL_OPENER = re.compile(r"^\*Em linguagem clínica", re.IGNORECASE)

# capítulo (por trecho do título h1) → blueprint — espelha section_blueprints.md
# NB: espaço final em "CAPÍTULO N " evita colisão de prefixo (CAPÍTULO 1 × CAPÍTULO 10)
_CHAPTER_BLUEPRINT: tuple[tuple[str, str], ...] = (
    ("CAPÍTULO 1 ", "B1"),   # nota à banca (M1)
    ("CAPÍTULO 2 ", "B0"),   # introdução/arquitetura da tese
    ("CAPÍTULO 3 ", "B1"),   # fundamentação (câmara)
    ("CAPÍTULO 4 ", "B2"),   # base comum de dados
    ("CAPÍTULO 5 ", "B3"),   # fundamento: invariância θ*
    ("CAPÍTULO 6 ", "B4"),   # aplicação: desenho emerge
    ("CAPÍTULO 7 ", "B5"),   # métodos: etrização formalizada
    ("CAPÍTULO 8 ", "B6"),   # resultados-como-validação
    ("CAPÍTULO 9 ", "B6"),   # achados/impactos (família resultados)
    ("CAPÍTULO 10 ", "B6"),  # discussão (família resultados)
    ("CAPÍTULO 11 ", "B7"),  # camada clínica
    ("CAPÍTULO 12 ", "B8"),  # limitações como fruto
    ("CAPÍTULO 13 ", "B8"),  # conclusões (fechamento)
    ("REFERÊNCIAS", "B9"),
    ("APÊNDICE", "B9"),
)


def blueprint_for_chapter(title: str) -> str:
    for fragment, bp in _CHAPTER_BLUEPRINT:
        if fragment in title:
            return bp
    return "B0"  # título/front-matter


def function_for_block(block, chapter_title: str):
    """Inferência determinística (Modo A). Estruturais → None."""
    if block.block_type in STRUCTURAL:
        return None
    if block.block_type == "paragraph" and _CLINICAL_OPENER.match(block.content.lstrip()):
        return "clinical-opener"
    if "NOTA INTRODUTÓRIA" in chapter_title:
        return "nota-banca"
    if "LIMITAÇÕES" in chapter_title:
        return "limitation"
    if "CONCLUSÕES" in chapter_title:
        return "interpretation"
    if "MÉTODOS" in chapter_title:
        return "method"
    if block.block_type == "figure":
        return "result"
    if block.block_type == "math":
        return "method" if "MÉTODOS" in chapter_title else "result"
    if block.claim_ids:
        return "result"
    if block.block_type == "table":
        return "result"
    if "INTRODUÇÃO" in chapter_title:
        return "motivation"
    return "exposition"


def apply_categorization(session, blocks, chapters) -> None:
    """Backfill Modo A: preenche blueprint/function/status IN PLACE (não toca content)."""
    titles = {c.chap_id: c.title for c in chapters}
    for b in blocks:
        title = titles.get(b.chap_id, "")
        b.blueprint = blueprint_for_chapter(title)
        b.function = function_for_block(b, title)
        b.status = "canonico"
    session.add_all(blocks)


def validate_block_write(
    *,
    function,
    blueprint,
    status,
    prev_status=None,
    is_human=False,
    block_type="paragraph",
) -> None:
    """Gate de escrita (chamado pelo CRUD/API em F4). Levanta ValueError se inválido."""
    if status not in STATUS:
        raise ValueError(f"status inválido: {status!r} ∉ {sorted(STATUS)}")
    if blueprint not in BLUEPRINTS:
        raise ValueError(f"blueprint inválido: {blueprint!r} ∉ B0–B9")
    if function is not None and function not in FUNCTIONS:
        raise ValueError(f"function inválida: {function!r} ∉ {sorted(FUNCTIONS)}")
    if block_type not in STRUCTURAL and function is None:
        raise ValueError("function é OBRIGATÓRIA em bloco de conteúdo (categorização §3.5)")
    if status == "author_approved" and not is_human:
        raise ValueError("author_approved só pode ser setado por humano (is_human=True)")
    if prev_status == "author_approved" and status != "author_approved" and not is_human:
        raise ValueError("máquina não pode reverter author_approved")
    if prev_status is not None and _ORDER.index(status) < _ORDER.index(prev_status):
        raise ValueError(f"transição regressiva proibida: {prev_status} → {status}")
