"""Ingest do grafo graphify (3 worktrees) → SQLite (GraphNode/GraphEdge).

Fonte: data/graphify_3trees.json (slim commitado — self-contained, CI incluso).
"""
import hashlib
import json
from pathlib import Path

from sqlalchemy import text as sa_text
from sqlmodel import Session, SQLModel

from thesis_engine.db import create_db
from thesis_engine.models import GraphEdge, GraphNode

REPO = Path(__file__).resolve().parents[2]
DEFAULT_JSON = REPO / "data" / "graphify_3trees.json"


def ingest_graphify(db_path: str, json_path: str = str(DEFAULT_JSON)) -> dict[str, int]:
    data = json.load(open(json_path, encoding="utf-8"))
    nodes = [
        GraphNode(
            node_id=n["id"],
            label=n["label"],
            community_id=str(n.get("community", "")),
            community_name=n.get("community_name", ""),
            file_type=n.get("file_type", ""),
            source_file=n.get("source_file", ""),
            source_location=n.get("source_location"),
            origin=n.get("origin", ""),
            is_callable=bool(n.get("callable", False)),
        )
        for n in data["nodes"]
    ]
    edges = []
    seen: set[str] = set()
    for l in data["links"]:
        eid = hashlib.sha1(f'{l["source"]}|{l["relation"]}|{l["target"]}'.encode()).hexdigest()[:16]
        if eid in seen:
            continue
        seen.add(eid)
        edges.append(
            GraphEdge(
                edge_id=eid,
                source_id=l["source"],
                target_id=l["target"],
                relation=l.get("relation", ""),
                origin=l.get("origin", ""),
                confidence=float(l.get("confidence", 0) or 0),
                source_file=l.get("source_file", ""),
            )
        )
    engine = create_db(db_path)
    with engine.connect() as conn:
        for tbl in ("graphedge", "graphnode"):
            conn.execute(sa_text(f'DROP TABLE IF EXISTS "{tbl}"'))
        conn.commit()
    SQLModel.metadata.create_all(engine)
    with Session(engine) as s:
        for obj in (*nodes, *edges):
            s.add(obj)
        s.commit()
        return {"graph_nodes": len(nodes), "graph_edges": len(edges)}
