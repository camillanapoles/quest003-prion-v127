#!/usr/bin/env python3
"""A9 — PENDÊNCIAS: ledger garantista da Quest 003 (fonte única: PENDENCIAS.md na raiz).

Checks determinísticos (stdlib-only, offline — contrato do guardião):
  1. Tabela parseável com colunas fixas: ID|TODOID|PENDÊNCIA|DONO|STATUS|EVIDÊNCIA/ARTEFATO|ORIGEM
  2. STATUS ∈ taxonomia válida
  3. Contagem do LEDGER-RESUMO == contagem computada (anti-drift)
  4. Artefatos de EVIDÊNCIA existem para EXECUTADA_NAO_MERGADA/FECHADA
  5. ZERO-DÉBITO AGENTE: DONO=AGENTE + STATUS=PLANEJADA exige {{DEFER:...}} explícito
     (planejada sem deferação visível = FAIL: executa ou defere — nunca morre silenciosa)
  6. TODO-registry (cruzamento {{TODO:ID:...}} × ledger nas superfícies vivas):
     a. TODOID no ledger com STATUS≠FECHADA ⇒ marcador deve existir em alguma superfície
     b. TODOID no ledger com STATUS=FECHADA ⇒ marcador deve TER SIDO removido (resolver=remover)
     c. Marcador em superfície ⇒ TODOID deve estar no ledger

FAIL ⇒ exit 1 (bloqueia pre-commit/AST). Superfícies vivas: raiz/*.md,
paper/*.md (nível topo), experiments/*.md, literature/*.md, analysis/*.md.
"""
import os, re, sys, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LEDGER = os.path.join(ROOT, "PENDENCIAS.md")

TAXONOMY = {"PLANEJADA", "EM_EXECUCAO", "EXECUTADA_NAO_MERGADA", "FECHADA",
            "DORMANT", "BLOQUEADA_EXTERNA", "AGUARDANDO_AUTORA",
            "AGUARDANDO_LAB", "AGUARDANDO_EXECUTOR"}
FECHADAS = {"FECHADA", "DORMANT"}
TODO_RE = re.compile(r"\{\{TODO:([A-Za-z0-9][A-Za-z0-9-]*):")

def surfaces():
    pats = ["*.md", "paper/*.md", "experiments/*.md", "experiments/part2_results/*.md",
            "literature/*.md", "analysis/*.md"]
    out = []
    for p in pats:
        out += glob.glob(os.path.join(ROOT, p))
    return sorted(set(out))

def parse_ledger():
    rows, header_counts = [], None
    for line in open(LEDGER, encoding="utf-8"):
        m = re.search(r"<!-- LEDGER-RESUMO (.+?) -->", line)
        if m:
            header_counts = dict(kv.split("=") for kv in m.group(1).split())
            continue
        if line.startswith("| P-"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 7:
                rows.append(cells)
    return rows, header_counts

def main():
    errs, warns = [], []
    if not os.path.exists(LEDGER):
        print("FAIL: PENDENCIAS.md ausente na raiz"); sys.exit(1)
    rows, hc = parse_ledger()
    if not rows:
        print("FAIL: nenhuma linha 'P-*' parseável no ledger"); sys.exit(1)

    # 2. taxonomia
    for r in rows:
        if r[4] not in TAXONOMY:
            errs.append(f"taxonomia inválida {r[0]}: {r[4]}")

    # 3. anti-drift do resumo
    abertas = [r for r in rows if r[4] not in FECHADAS]
    planej_ag = [r for r in rows if r[1 + 0] and r[3] == "AGENTE" and r[4] == "PLANEJADA"]
    fech = [r for r in rows if r[4] == "FECHADA"]
    dorm = [r for r in rows if r[4] == "DORMANT"]
    if hc:
        exp = {"total": str(len(rows)), "abertas": str(len(abertas)),
               "planejadas_agente": str(len(planej_ag)),
               "fechadas": str(len(fech)), "dormant": str(len(dorm))}
        for k, v in exp.items():
            if hc.get(k) != v:
                errs.append(f"drift resumo[{k}]: header={hc.get(k)} computado={v}")
    else:
        errs.append("LEDGER-RESUMO ausente")

    # 4. evidência existe (status com artefato exigido)
    for r in rows:
        if r[4] in {"EXECUTADA_NAO_MERGADA", "FECHADA"}:
            for tok in r[5].split():
                if "/" in tok or tok.endswith((".md", ".csv", ".json", ".py", ".pdf")):
                    p = tok if os.path.isabs(tok) else os.path.normpath(os.path.join(ROOT, tok))
                    if not os.path.exists(p):
                        errs.append(f"evidência ausente {r[0]}: {tok}")

    # 5. zero-débito agente
    for r in rows:
        if r[3] == "AGENTE" and r[4] == "PLANEJADA" and "{{DEFER:" not in r[2]:
            errs.append(f"zero-débito: {r[0]} PLANEJADA-AGENTE sem {{{{DEFER:...}}}}")

    # 6. TODO-registry cross-check
    found = {}
    for sf in surfaces():
        try:
            txt = open(sf, encoding="utf-8").read()
        except OSError:
            continue
        for tid in TODO_RE.findall(txt):
            if tid.lower() == "id":
                continue  # especificação de formato, não pendência
            found.setdefault(tid, []).append(os.path.relpath(sf, ROOT))
    ledger_ids = {r[1] for r in rows if r[1] and r[1] != "-"}
    for r in rows:
        tid = r[1]
        if tid == "-":
            continue
        if r[4] != "FECHADA" and tid not in found:
            errs.append(f"TODOID {tid} ({r[0]}) aberto mas marcador não existe")
        if r[4] == "FECHADA" and tid in found:
            errs.append(f"TODOID {tid} ({r[0]}) FECHADA mas marcador ainda existe em {found[tid][0]} (resolver=remover)")
    for tid, locs in sorted(found.items()):
        if tid not in ledger_ids:
            errs.append(f"marcador {{TODO:{tid}:}} em {locs[0]} sem linha no ledger")

    n_open = len(abertas)
    print(f"RESUMO: {len(rows)} itens · {n_open} abertas · agente-planejadas-deferidas={len(planej_ag)} · fechadas={len(fech)} · dormant={len(dorm)} · marcadores-vivos={len(found)}")
    for w in warns:
        print("WARN:", w)
    for e in errs:
        print("FAIL:", e)
    print("VEREDITO:", "PASS" if not errs else f"FAIL ({len(errs)})")
    sys.exit(0 if not errs else 1)

if __name__ == "__main__":
    main()
