#!/usr/bin/env python3
"""AST — Assertion Self-Test consolidado da tese (Parte 1 + Parte 2).
Um comando = estado de garantia inteiro. Saída: tabela PASS/FAIL + veredito.
Componentes: A1 solver WS-7 (massa/Thiele) · A2 gate parte 1 · A3 gate parte 2 ·
A4 validate_manifest (38 fontes) · A5 contagem de registro · A6 drift de artefatos-chave."""
import subprocess, sys, os, json, csv
FAST = "--fast" in sys.argv  # pula A1 (solver ~3min); releases usam 9/9 completo

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
G = os.path.join(R, "paper", "guardian")

def _skill_scripts():
    """Scripts da skill scientific-writing — ordem: env > repo-local > original > ~/.agents."""
    cands = []
    if os.environ.get("SCIENTIFIC_SKILLS_SCRIPTS"):
        cands.append(os.environ["SCIENTIFIC_SKILLS_SCRIPTS"])
    cands += [os.path.join(R, "scripts", "validators"),
              "/workspace/projects/scientific-agent-skills/skills/scientific-writing/scripts",
              os.path.expanduser("~/.agents/skills/scientific-agent-skills/skills/scientific-writing/scripts")]
    for c in cands:
        if os.path.isdir(c):
            return c
    return cands[-1]

S = _skill_scripts()
results = []

def run(name, fn):
    try:
        ok, detail = fn()
        results.append((name, ok, detail))
    except Exception as e:
        results.append((name, False, f"exceção: {e}"))

def a1_ws7():
    p = subprocess.run([sys.executable, os.path.join(R, "experiments", "ws_7_solver.py")],
                       capture_output=True, text=True, timeout=600)
    out = p.stdout + p.stderr
    mass = "100.0 %" in out or "'mass_conservation_pct': np.float64(100.0)" in out
    thiele = "0.5 %" in out or "'ell_err_pct': 0.5" in out
    return mass and thiele, f"massa={'100%' if mass else 'X'} · ℓ-err={'0.5%' if thiele else 'X'}"

def _gate(profile, md, tex, reg):
    def f():
        cmd = [sys.executable, os.path.join(G, "guardian.py"), "--round", "3",
               "--profile", profile, "--md", md, "--tex", tex,
               "--claims", os.path.join(G, "..", "evidence_workspace", "claims.csv"),
               "--manifest", os.path.join(G, "..", "evidence_workspace", "source_manifest.json"),
               "--consistency", os.path.join(G, "..", "evidence_workspace", "consistency_manifest.json"),
               "--registry", reg, "--report", reg.replace(".json", "_report.md")]
        p = subprocess.run(cmd, cwd=G, capture_output=True, text=True, timeout=300)
        return (p.returncode == 0), p.stdout.strip().splitlines()[-1] if p.stdout.strip() else p.stderr[:80]
    return f

def a4_manifest():
    p = subprocess.run([sys.executable, os.path.join(S, "validate_manifest.py"),
                        os.path.join(R, "paper", "evidence_workspace", "source_manifest.json"),
                        "--kind", "source", "--require-verified"],
                       capture_output=True, text=True, timeout=120)
    return ('"errors": 0' in p.stdout or '"errors":0' in p.stdout.replace(" ", "").replace("\n","")), \
           [l for l in p.stdout.splitlines() if "errors" in l or "records" in l][:2].join(" ") if False else ("errors=0" if '"errors": 0' in p.stdout else p.stdout[-100:])

def a5_registro():
    rows = list(csv.DictReader(open(os.path.join(R, "paper", "evidence_workspace", "claims.csv"))))
    n = len(json.load(open(os.path.join(R, "paper", "evidence_workspace", "source_manifest.json")))["sources"])
    nf = len(json.load(open(os.path.join(R, "paper", "evidence_workspace", "consistency_manifest.json")))["numeric_facts"])
    expect = (54, 38, 48)
    got = (len(rows), n, nf)
    return got == expect or got >= expect, f"claims={len(rows)} fontes={n} N-fatos={nf} (esperado ≥ {expect})"

def a6_artefatos():
    need = ["paper/manuscript_EN_v5.md", "paper/manuscript_PT_v5.md", "paper/manuscript_Parte2_v1.md",
            "paper/latex/manuscript_v5_EN.pdf", "paper/latex/manuscript_v5_PT.pdf",
            "paper/latex/manuscript_Parte2_v1.pdf", "guardian.md", "guardian2.md",
            "THESIS_ROADMAP.md", "KNOWLEDGE_CANON.md",
            "experiments/part2_results/part2_theta_obs_v1.json",
            "experiments/part2_results/part2_theta_obs_pooled.json",
            "experiments/part2_results/part2_theta_obs_v11.json",
            "experiments/part2_results/part2_derived_summary.json"]
    miss = [f for f in need if not os.path.exists(os.path.join(R, f))]
    return not miss, f"faltando: {miss}" if miss else f"{len(need)}/{len(need)} presentes"

if not FAST:
    run("A1 WS-7 self-tests", a1_ws7)
elif False:
    pass
run("A2 Gate Parte 1 (0 BLOCKED)", _gate("part1", "../manuscript_EN_v5.md", "../latex/manuscript_v5_EN.tex", "guardian_registry_v5_final.json"))
run("A3 Gate Parte 2 (0 BLOCKED)", _gate("part2", "../manuscript_Parte2_v1.md", "../latex/manuscript_Parte2_v1.tex", "guardian_registry_parte2.json"))
run("A4 validate_manifest", a4_manifest)
run("A5 registro ≥54/38/48", a5_registro)
run("A6 artefatos-chave", a6_artefatos)

def a7_consistency():
    p = subprocess.run([sys.executable, os.path.join(S, "check_consistency.py"),
                        os.path.join(R, "paper", "evidence_workspace", "consistency_manifest.json")],
                       capture_output=True, text=True, timeout=120)
    ok = '"errors": 0' in p.stdout
    return ok, "errors=0 (48 N-fatos)" if ok else p.stdout[-200:]

def a8_references():
    p = subprocess.run([sys.executable, os.path.join(S, "check_references.py"),
                        os.path.join(R, "paper", "evidence_workspace", "source_manifest.json")],
                       capture_output=True, text=True, timeout=120)
    ok = '"errors": 0' in p.stdout and '"warnings": 0' in p.stdout
    return ok, "38 fontes 0/0" if ok else p.stdout[-200:]

run("A7 check_consistency (bateria)", a7_consistency)
run("A8 check_references (bateria)", a8_references)

def a9_pendencias():
    p = subprocess.run([sys.executable, os.path.join(R, "scripts", "pendencias_check.py")],
                       capture_output=True, text=True, timeout=120)
    line = [l for l in (p.stdout + p.stderr).splitlines() if l.startswith(("RESUMO", "VEREDITO"))]
    return (p.returncode == 0), (" · ".join(line) if line else (p.stdout or p.stderr)[-120:])
run("A9 pendências (garantista)", a9_pendencias)

print("═" * 62)
print("AST — ASSERTION SELF-TEST CONSOLIDADO (Parte 1 + Parte 2)")
print("═" * 62)
ok_all = True
for name, ok, det in results:
    print(f" [{'PASS' if ok else 'FAIL'}] {name:34s} {det}")
    ok_all &= ok
print("─" * 62)
print(f" VEREDITO: {len([r for r in results if r[1]])}/{len(results)} — {'AST VERDE' if ok_all else 'AST FALHOU'}")
sys.exit(0 if ok_all else 1)
