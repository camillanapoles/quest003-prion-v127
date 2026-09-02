"""CLI do thesis_engine — ingest · check · build · serve."""
from pathlib import Path

import typer

from thesis_engine.db import _DEFAULT_DB

app = typer.Typer(help="Motor modular da tese (MD canônico + registro probatório)")
REPO = Path(__file__).resolve().parents[1]


@app.command()
def ingest(db: str = _DEFAULT_DB):
    """Rebuild completo: registro F1 + tese F2/F2.5 + experimentos F3 + grafo + plano."""
    from thesis_engine.ingest.experiments import ingest_experiments
    from thesis_engine.ingest.graphify import ingest_graphify
    from thesis_engine.ingest.plano import ingest_plano
    from thesis_engine.ingest.registro import ingest_registro
    from thesis_engine.ingest.tese import ingest_tese

    typer.echo(f"registro: {ingest_registro(db_path=db)}")
    typer.echo(f"tese:     {ingest_tese(db_path=db)}")
    typer.echo(f"dados:    {ingest_experiments(db_path=db)}")
    typer.echo(f"grafo:    {ingest_graphify(db_path=db)}")
    typer.echo(f"plano:    {ingest_plano(db_path=db)}")


@app.command()
def plano(db: str = _DEFAULT_DB, out: str = str(REPO / "PLANO_GLOBAL_DA_TESE.md")):
    """Injeta o plano global no DB e renderiza PLANO_GLOBAL_DA_TESE.md."""
    from thesis_engine.ingest.plano import ingest_plano, render_plano_md

    typer.echo(ingest_plano(db_path=db))
    typer.echo(f"plano MD → {render_plano_md(out)}")


@app.command()
def producao(db: str = _DEFAULT_DB):
    """HP-Cap: revisão cumulativa por capítulo (ordem topológica) + fila hostil."""
    from thesis_engine.ingest.revisoes import ingest_revisoes
    from thesis_engine.producao import assert_producao_ok, check_producao

    r = check_producao(db)
    for chap in r["relatorio"]:
        marks = {g: ("✓" if v["ok"] else "✗") for g, v in chap["gates"].items()}
        typer.echo(
            f"{chap['cap']}: objetivo={marks['objetivo']} coesao={marks['coesao']} "
            f"gaps={marks['gaps']} → {'OK' if chap['ok'] else 'DÉBITO'}"
        )
    gate = assert_producao_ok(db)  # HARD=0 exigido
    rev = ingest_revisoes(db)
    typer.echo(
        f"HARD=0 ✓ · YELLOW={len(r['yellow'])} → fila hostil: {rev['total']} itens "
        f"({rev['novos']} novos) — protocolo: HOSTILE_REVIEW_PROTOCOL.md"
    )


@app.command()
def check(db: str = _DEFAULT_DB):
    """Roda TODOS os gates (§4.3 + estilo + bindings + plano + produção). Exit 1 se falhar."""
    from thesis_engine.integrity import (
        check_bindings,
        check_plano,
        check_sec43,
        check_sec63,
        check_style,
    )
    from thesis_engine.producao import assert_producao_ok

    ok = True
    for name, fn in (
        ("sec43", check_sec43),
        ("sec63", check_sec63),
        ("estilo", check_style),
        ("bindings", check_bindings),
        ("plano", check_plano),
        ("producao", assert_producao_ok),
    ):
        try:
            r = fn(db)
            typer.echo(f"[gate:{name}] VERDE — {r}")
        except ValueError as e:
            ok = False
            typer.echo(f"[gate:{name}] VERMELHO:\n{e}", err=True)
    raise typer.Exit(code=0 if ok else 1)


@app.command()
def build(
    db: str = _DEFAULT_DB,
    out: str = str(REPO / "build" / "tese_unificada.md"),
    modular_dir: str = str(REPO / "build" / "tese"),
):
    """Renderiza o MD canônico: single-file + modular (1 arquivo/capítulo + SUMARIO)."""
    from thesis_engine.render.md import render_md
    from thesis_engine.render.modular import render_modular

    text = render_md(db)
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(text, encoding="utf-8")
    typer.echo(f"render canônico → {out} ({len(text)} chars)")
    report = render_modular(db, modular_dir)
    typer.echo(
        f"render modular  → {modular_dir} ({report['chapters']} caps · "
        f"{report['files']} arquivos · {report['total_claims']} claims citadas)"
    )


@app.command()
def serve(db: str = _DEFAULT_DB, host: str = "127.0.0.1", port: int = 8000):
    """Sobe a API (docs em /docs)."""
    import os

    os.environ["THESIS_DB"] = db
    import uvicorn

    uvicorn.run("thesis_engine.api_live:app", host=host, port=port)


if __name__ == "__main__":
    app()
