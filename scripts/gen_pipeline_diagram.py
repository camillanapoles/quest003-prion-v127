"""Gera diagrama Archify do pipeline FSM a partir do DB — para CI/CD atualizar."""
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

from sqlmodel import Session, select
from thesis_engine.db import create_db
from thesis_engine.escritor import V2_DB
from thesis_engine.models import PlanChapter, WritingCycle
from thesis_engine.producao import check_producao
from thesis_engine.integrity import check_sec43, check_sec63, check_style, check_bindings, check_plano

def gate_status(fn, db):
    try:
        r = fn(db)
        return "pass"
    except ValueError:
        return "fail"

def generate():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Coleta estados dos gates
    db = V2_DB
    gates = {
        "sec43": gate_status(check_sec43, db),
        "sec63": gate_status(check_sec63, db),
        "estilo": gate_status(check_style, db),
        "bindings": gate_status(check_bindings, db),
        "plano": gate_status(check_plano, db),
    }
    
    # Coleta estado dos capítulos
    with Session(create_db(db)) as s:
        caps = s.exec(select(PlanChapter).order_by(PlanChapter.ordem)).all()
        cycles = {c.cap_key: c for c in s.exec(select(WritingCycle)).all()}
    
    cap_states = {}
    for cap in caps:
        wc = cycles.get(cap.chap_key)
        cap_states[cap.chap_key] = wc.estado if wc else "brief"
    
    aprovados = sum(1 for s in cap_states.values() if s in ("approved", "rendered", "committed"))
    total = len(caps)
    
    # Cor: gray=neutral, green=pass, red=fail, blue=in-progress
    def color(status):
        if status == "pass": return "#3fb950"
        if status == "fail": return "#f85149"
        return "#484f58"  # gray
    
    def cap_color(estado):
        if estado in ("approved", "rendered", "committed"): return "#3fb950"
        if estado in ("drafting", "guard", "gates", "hostile", "emenda"): return "#d29922"
        return "#484f58"
    
    # Gera HTML com SVG inline (self-contained, no dependencies)
    gate_nodes = "".join(
        f'<circle cx="{120+i*140}" cy="60" r="25" fill="{color(st)}" stroke="#30363d" stroke-width="2"/>'
        f'<text x="{120+i*140}" y="65" text-anchor="middle" fill="#c9d1d9" font-size="11">{name}</text>'
        f'<text x="{120+i*140}" y="105" text-anchor="middle" fill="#8b949e" font-size="9">{st}</text>'
        for i, (name, st) in enumerate(gates.items())
    )
    
    cap_nodes = "".join(
        f'<rect x="{40+i*62}" y="160" width="52" height="70" rx="8" fill="{cap_color(st)}" stroke="#30363d" stroke-width="1" opacity="0.85"/>'
        f'<text x="{66+i*62}" y="185" text-anchor="middle" fill="#fff" font-size="10" font-weight="bold">{key}</text>'
        f'<text x="{66+i*62}" y="200" text-anchor="middle" fill="#ddd" font-size="7">{st[:8]}</text>'
        for i, (key, st) in enumerate(cap_states.items())
    )
    
    pct = round(aprovados / total * 100) if total else 0
    progress_fill = "#3fb950" if pct == 100 else "#58a6ff"
    
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"><title>Thesis Engine — Pipeline CI/CD</title>
<style>
body{{font-family:system-ui;background:#0d1117;color:#c9d1d9;margin:0;padding:20px;display:flex;justify-content:center}}
.container{{max-width:1200px;width:100%}}
h1{{font-size:1.2rem;color:#58a6ff}}
.meta{{font-size:.75rem;color:#484f58;margin-bottom:16px}}
.svg-wrap{{background:#161b22;border:1px solid #30363d;border-radius=12px;padding=16px}}
</style></head>
<body><div class="container">
<h1>🔬 Thesis Engine — Pipeline CI/CD</h1>
<div class="meta">Gerado: {now} · {aprovados}/{total} aprovados ({pct}%)</div>
<div class="svg-wrap">
<svg viewBox="0 0 1200 280" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">
<!-- Barra de progresso -->
<rect x="40" y="10" width="1120" height="14" rx="7" fill="#21262d"/>
<rect x="40" y="10" width="{max(pct*11.2, 4)}" height="14" rx="7" fill="{progress_fill}"/>
<text x="600" y="32" text-anchor="middle" fill="#8b949e" font-size="11">{aprovados}/{total} capítulos aprovados</text>
<!-- Gates -->
<text x="40" y="55" fill="#8b949e" font-size="10">GATES:</text>
{gate_nodes}
<!-- Linha conectora dos gates -->
<line x1="120" y1="60" x2="{120+len(gates)*140-140}" y2="60" stroke="#30363d" stroke-width="1" stroke-dasharray="4"/>
<!-- Capítulos -->
<text x="40" y="150" fill="#8b949e" font-size="10">CAPÍTULOS (FSM):</text>
{cap_nodes}
<!-- Linha conectora dos caps -->
<line x1="66" y1="160" x2="{66+(total-1)*62}" y2="160" stroke="#30363d" stroke-width="1" stroke-dasharray="4"/>
<!-- Legenda -->
<text x="40" y="260" fill="#484f58" font-size="9">
<tspan fill="#3fb950">●</tspan> aprovado/pass · <tspan fill="#d29922">●</tspan> em processo · <tspan fill="#484f58">●</tspan> não iniciado · <tspan fill="#f85149">●</tspan> erro</text>
</svg></div></div></body></html>'''
    
    out = REPO / "build" / "pipeline_diagram.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"✓ {out} ({len(html)} bytes · {aprovados}/{total} aprovados)")

if __name__ == "__main__":
    generate()
