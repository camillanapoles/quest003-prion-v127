"""Parser do MD canônico → blocos tipados (Modo A: conservação byte a byte).

A partição cobre o arquivo INTEIRO: cada caractere pertence a exatamente um bloco
(blanks incluídos como blocos 'blank'). Round-trip garantido por construção:
render = ''.join(block.content por seq).

Vinculação no grafo:
  - [claim:Cxxx] · [claim:C055, C057] · [claim:C058–C060] → claim_ids expandidas
  - [evidence:Exxx(,Eyyy)] → evidence_ids
  - tiers: [SIM]-planejamento | [SIM] | [ORGANOID] (match mais longo primeiro)
  - §refs: §2 · §5.1 · §2-bis → cross_refs
Estrutura: h1 → Chapter · h2/h3 → Section (label numerado ou None).
"""
import re
from pathlib import Path

from sqlalchemy import text as sa_text
from sqlmodel import Session

from thesis_engine.db import create_db
from thesis_engine.models import Block, Chapter, Section

REPO = Path(__file__).resolve().parents[2]
TESE_MD = REPO / "paper_rewriting_output" / "final_paper" / "tese_unificada.md"

_HEADING = re.compile(r"^(#{1,6}) (.+)$")
_LIST = re.compile(r"^(?:- |\* |\d+\. )")
_TIER_ORDER = (
    (re.compile(r"\[SIM\]-planejamento"), "SIM-planejamento"),
    (re.compile(r"\[SIM-planejamento\]"), "SIM-planejamento"),
    (re.compile(r"\[SIM\]"), "SIM"),
    (re.compile(r"\[ORGANOID\]"), "ORGANOID"),
)
_CLAIM_TAG = re.compile(r"\[claim:([^\]]+)\]")
_EVID_TAG = re.compile(r"\[evidence:([^\]]+)\]")
_SREF = re.compile(r"§\s?([0-9A-B][0-9]*(?:\.[0-9]+)?(?:-bis)?)")
_SEC_LABEL = re.compile(r"^([0-9]+\.[0-9A-Za-z0-9]*(?:-bis)?|B\.[0-9]+|[A-F]\.[0-9]+)(?=\.|\s|$)")


def _expand_claims(inner: str) -> list[str]:
    """'C038, C055–C057' → ['C038','C055','C056','C057'] (en-dash e hyphen)."""
    out: list[str] = []
    for item in inner.split(","):
        item = item.strip()
        if not item:
            continue
        m = re.fullmatch(r"C(\d{3})\s*[–-]\s*C(\d{3})", item)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            out.extend(f"C{i:03d}" for i in range(a, b + 1))
        else:
            out.append(item)
    return out


def extract_meta(content: str) -> dict:
    """Extrai claim/evidence/tier/§ref de um conteúdo (usado no parse E na escrita F4)."""
    claims: list[str] = []
    for m in _CLAIM_TAG.finditer(content):
        claims.extend(_expand_claims(m.group(1)))
    evid = [e.strip() for m in _EVID_TAG.finditer(content) for e in m.group(1).split(",") if e.strip()]
    tiers = []
    for pat, name in _TIER_ORDER:
        if pat.search(content) and name not in tiers:
            tiers.append(name)
    return {
        "claim_ids": sorted(set(claims)),
        "evidence_ids": sorted(set(evid)),
        "tiers": tiers,
        "cross_refs": _SREF.findall(content),
    }


def _classify(lines: list[str], start: int) -> tuple[str, int]:
    """Classifica o bloco começando em `start`; retorna (tipo, nº de linhas)."""
    line = lines[start]
    stripped = line.strip()
    if not stripped:
        n = 0
        while start + n < len(lines) and not lines[start + n].strip():
            n += 1
        return "blank", n
    m = _HEADING.match(line)
    if m:
        return "heading", 1
    if stripped == "---":
        return "hr", 1
    if line.startswith("|"):
        n = 0
        while start + n < len(lines) and lines[start + n].startswith("|"):
            n += 1
        return "table", n
    if line.startswith(">"):
        n = 0
        while start + n < len(lines) and lines[start + n].startswith(">"):
            n += 1
        return "quote", n
    if line.startswith("$$"):
        if stripped.endswith("$$") and len(stripped) > 2:
            return "math", 1
        n = 1
        while start + n < len(lines):
            if lines[start + n].startswith("$$"):
                n += 1
                break
            n += 1
        return "math", n
    if line.startswith("!["):
        return "figure", 1
    if _LIST.match(line):
        n = 0
        while start + n < len(lines):
            nxt = lines[start + n]
            if not nxt.strip() or not (_LIST.match(nxt) or nxt.startswith((" ", "\t"))):
                break
            if _LIST.match(nxt) or (nxt.startswith((" ", "\t")) and nxt.strip()):
                n += 1
            else:
                break
        return "list", max(n, 1)
    n = 0
    while start + n < len(lines):
        nxt = lines[start + n]
        if (
            not nxt.strip()
            or _HEADING.match(nxt)
            or nxt.lstrip().startswith(("|", ">", "$$", "![", "---"))
            or _LIST.match(nxt)
        ):
            break
        n += 1
    return "paragraph", max(n, 1)


def parse_blocks(md_text: str) -> list[dict]:
    """Partição completa do MD em blocos verbatim, em ordem."""
    lines = md_text.split("\n")
    # o último elemento após split pode ser '' se termina com \n; lines cobre tudo
    blocks: list[dict] = []
    i = 0
    while i < len(lines):
        btype, n = _classify(lines, i)
        raw = "\n".join(lines[i : i + n])
        # preserva o \n SEPARADOR entre blocos quando não é o fim do arquivo
        end = i + n
        if end < len(lines):
            raw += "\n"
        meta = {} if btype in ("blank",) else extract_meta(raw)
        d = {"block_type": btype, "content": raw, **meta}
        if btype == "heading":
            m = _HEADING.match(lines[i])
            d["heading_level"] = len(m.group(1))
            d["heading_text"] = m.group(2).strip()
        blocks.append(d)
        i = end
    return blocks


def ingest_tese(db_path: str, md_path: str = str(TESE_MD)) -> dict[str, int]:
    """Parseia o MD canônico → Chapter/Section/Block (rebuild das tabelas F2)."""
    md_text = Path(md_path).read_text(encoding="utf-8")
    parsed = parse_blocks(md_text)

    engine = create_db(db_path)
    with engine.connect() as conn:  # drop apenas das tabelas F2 (registro intacto)
        for tbl in ("block", "section", "chapter"):
            conn.execute(sa_text(f'DROP TABLE IF EXISTS "{tbl}"'))
        conn.commit()
    from sqlmodel import SQLModel

    SQLModel.metadata.create_all(engine)

    chapters: list[Chapter] = []
    sections: list[Section] = []
    blocks: list[Block] = []
    cur_chap: str | None = None
    cur_sec: str | None = None
    n_sec = 0

    with Session(engine) as s:
        for seq, d in enumerate(parsed, start=1):
            if d["block_type"] == "heading":
                if d["heading_level"] == 1:
                    cid = f"c{len(chapters):02d}"
                    chapters.append(
                        Chapter(chap_id=cid, order_idx=len(chapters), title=d["heading_text"], level=1)
                    )
                    cur_chap, cur_sec, n_sec = cid, None, 0
                else:
                    n_sec += 1
                    sid = f"{cur_chap}s{n_sec - 1:02d}"
                    label_m = _SEC_LABEL.match(d["heading_text"])
                    sections.append(
                        Section(
                            sec_id=sid,
                            chap_id=cur_chap,
                            order_idx=n_sec - 1,
                            level=d["heading_level"],
                            label=label_m.group(1) if label_m else None,
                            title=d["heading_text"],
                        )
                    )
                    cur_sec = sid
            blocks.append(
                Block(
                    block_id=f"B{seq:04d}",
                    seq=seq,
                    block_type=d["block_type"],
                    chap_id=cur_chap,
                    sec_id=cur_sec,
                    content=d["content"],
                    heading_level=d.get("heading_level"),
                    heading_text=d.get("heading_text"),
                    claim_ids=d.get("claim_ids", []),
                    evidence_ids=d.get("evidence_ids", []),
                    cross_refs=d.get("cross_refs", []),
                    tiers=d.get("tiers", []),
                )
            )
        for obj in (*chapters, *sections, *blocks):
            s.add(obj)
        from thesis_engine.categorize import apply_categorization

        apply_categorization(s, blocks, chapters)  # F2.5: backfill §3.5 (metadata only)
        s.commit()
        return {
            "chapters": len(chapters),
            "sections": len(sections),
            "blocks": len(blocks),
        }
