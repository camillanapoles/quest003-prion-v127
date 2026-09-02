"""CLI do thesis_engine — ingest · check · build · serve."""
from pathlib import Path

import typer

from thesis_engine.db import _DEFAULT_DB

app = typer.Typer(help="Motor modular da tese (MD canônico + registro probatório)")
REPO = Path(__file__).resolve().parents[1]


@app.command()
def ingest(db: str = _DEFAULT_DB):
    """Rebuild completo: registro F1 + tese F2/F2.5 + experimentos F3 → SQLite."""
    from thesis_engine.ingest.experiments import ingest_experiments
    from thesis_engine.ingest.registro import ingest_registro
    from thesis_engine.ingest.tese import ingest_tese

    c1 = ingest_registro(db_path=db)
    c2 = ingest_tese(db_path=db)
    c3 = ingest_experiments(db_path=db)
    typer.echo(f"registro: {c1}")
    typer.echo(f"tese:     {c2}")
    typer.echo(f"dados:    {c3}")


@app.command()
def check(db: str = _DEFAULT_DB):
    """Roda TODOS os gates (§4.3 + estilo). Exit 1 se qualquer um falhar."""
    from thesis_engine.integrity import check_sec43, check_style

    ok = True
    for name, fn in (("sec43", check_sec43), ("estilo", check_style)):
        try:
            r = fn(db)
            typer.echo(f"[gate:{name}] VERDE — {r}")
        except ValueError as e:
            ok = False
            typer.echo(f"[gate:{name}] VERMELHO:\n{e}", err=True)
    raise typer.Exit(code=0 if ok else 1)


@app.command()
def build(db: str = _DEFAULT_DB, out: str = str(REPO / "build" / "tese_unificada.md")):
    """Renderiza o MD canônico (bloco status=canonico, na ordem) → arquivo."""
    from thesis_engine.render.md import render_md

    text = render_md(db)
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(text, encoding="utf-8")
    typer.echo(f"render canônico → {out} ({len(text)} chars)")


@app.command()
def serve(db: str = _DEFAULT_DB, host: str = "127.0.0.1", port: int = 8000):
    """Sobe a API (docs em /docs)."""
    import os

    os.environ["THESIS_DB"] = db
    import uvicorn

    uvicorn.run("thesis_engine.api_live:app", host=host, port=port)


if __name__ == "__main__":
    app()
