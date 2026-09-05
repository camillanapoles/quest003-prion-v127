"""Ingest dos JSONs experimentais do registro → NumberValue com lineage.

REGISTRY_JSONS = lista curada dos JSONs que o registro probatório cita como
fonte dos números da tese (evidence_bank/figure_asset_map). Flatten recursivo:
cada folha numérica (int/float, exceto bool) vira uma linha arquivo→caminho→valor.
"""
import json
import re
from pathlib import Path

from sqlalchemy import text as sa_text
from sqlmodel import Session, SQLModel, select

from thesis_engine.db import create_db
from thesis_engine.models import NumberValue

REPO = Path(__file__).resolve().parents[2]

REGISTRY_JSONS: tuple[str, ...] = (
    "experiments/xspecies/p024_mouse.json",
    "experiments/xspecies/p024_hamster.json",
    "experiments/xspecies/p024_human.json",
    "experiments/xspecies/p024_vole.json",
    "experiments/xspecies/species_params.json",
    "experiments/m31/m31_u1u2.json",
    "experiments/ws_9_results/ws_9_v4_human.json",
    "experiments/ws_7_results/ws_7_results.json",
    "experiments/part2_results/part2_theta_obs_pooled.json",
)

_IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _key_part(key: str) -> str:
    # Sem aspas: caminho é chave de busca exata (string única por folha nos JSONs
    # do registro); chaves numéricas como "1" entram literais (u1_kreq.1)
    return key


def _flatten(obj, path: str, out: list[tuple[str, str]]) -> None:
    if isinstance(obj, bool):
        return
    if isinstance(obj, (int, float)):
        out.append((path, obj))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            _flatten(v, f"{path}.{_key_part(k)}" if path else _key_part(k), out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _flatten(v, f"{path}[{i}]", out)


def ingest_experiments(db_path: str) -> dict[str, int]:
    """Flattena os JSONs do registro → tabelas numbervalue (rebuild F3)."""
    rows: list[NumberValue] = []
    n = 0
    for rel in REGISTRY_JSONS:
        data = json.load(open(REPO / rel, encoding="utf-8"))
        flat: list[tuple[str, str]] = []
        _flatten(data, "", flat)
        for path, val in flat:
            n += 1
            rows.append(
                NumberValue(
                    value_id=f"V{n:04d}",
                    source_file=rel,
                    json_path=path,
                    raw=repr(val),
                    value_float=float(val),
                )
            )
    engine = create_db(db_path)
    with engine.connect() as conn:  # drop apenas da tabela F3
        conn.execute(sa_text('DROP TABLE IF EXISTS "numbervalue"'))
        conn.commit()
    SQLModel.metadata.create_all(engine)
    with Session(engine) as s:
        for r in rows:
            s.add(r)
        s.commit()
    return {"numbervalues": len(rows), "files": len(REGISTRY_JSONS)}


def get_value(db_path: str, file_stem: str, json_path: str) -> float:
    """Busca um valor por radical do arquivo + caminho pontuado.

    file_stem: 'p024_human' casa com 'experiments/xspecies/p024_human.json'.
    json_path aceita a mesma convenção do flatten (chaves não-ident entre aspas).
    """
    needle = json_path  # match exato pela string completa do caminho
    engine = create_db(db_path)
    with Session(engine) as s:
        rows = s.exec(
            select(NumberValue).where(NumberValue.json_path == needle)  # fallback exato
        ).all()
        if not rows:
            rows = [
                v
                for v in s.exec(
                    select(NumberValue).where(NumberValue.source_file.contains(file_stem))
                ).all()
                if v.json_path == needle
            ]
    matches = [v for v in rows if file_stem in v.source_file]
    if not matches:
        raise KeyError(f"NumberValue ausente: {file_stem} · {json_path}")
    return matches[0].value_float
