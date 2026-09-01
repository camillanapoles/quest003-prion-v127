#!/usr/bin/env python3
"""FIGURA 4 — θ* multi-espécie (PARTE 3) · auditável: lê APENAS os JSONs p024_* (número nunca digitado).
Saída: paper/latex/figs/fig4_theta_species.png (+ .json de dados plotados para rastreio)."""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FIGS = os.path.join(R, "paper", "latex", "figs")
os.makedirs(FIGS, exist_ok=True)

SPEC = ["mouse", "human", "hamster", "vole"]
LBL = {"mouse": "Camundongo", "human": "Humano", "hamster": "Hamster", "vole": "Bank vole"}
data = {s: json.load(open(os.path.join(R, "experiments", "xspecies", f"p024_{s}.json"))) for s in SPEC}

fig, ax = plt.subplots(figsize=(8.6, 4.6), dpi=200)
bands = {"mouse": ["#4477aa"], "human": ["#77aadd", "#4477aa", "#224466"],
         "hamster": ["#ee7777", "#cc4444", "#882222"], "vole": ["#99cc99", "#66aa66", "#336633"]}
w = 0.22
plot_data = {}
for i, s in enumerate(SPEC):
    rows = [r for r in data[s]["rows"]]
    for j, r in enumerate(rows):
        x = i + (j - (len(rows) - 1) / 2) * w
        th = r["theta_star"]
        if th is None:
            ax.scatter(x, 0.02, marker="x", color="k", s=42)
            plot_data[f"{s}_kt{r['Kt_scale']}"] = "escape_em_todas"
            continue
        ax.bar(x, th, width=w * 0.9, color=bands[s][j % len(bands[s])],
               edgecolor="white", linewidth=0.6)
        ax.text(x, th + 0.008, f"{th:.3f}", ha="center", fontsize=6.6)
        plot_data[f"{s}_kt{r['Kt_scale']}"] = {"kappa_min": r["kappa_min"], "theta": th}
# banda Cenário B central (0.333-0.400)
ax.axhspan(0.333, 0.400, color="#dddddd", alpha=0.55, zorder=0)
ax.text(3.62, 0.367, "banda central\nCenário B", fontsize=7, color="#444444", ha="right")
ax.axhline(0.333, color="#333333", lw=0.8, ls="--")
ax.text(-0.62, 0.336, "θ*=0,333 (v1.0 travado)", fontsize=7, color="#333333")

ax.set_xticks(range(len(SPEC)))
ax.set_xticklabels([f"{LBL[s]}\n(banda Kt {min(r['Kt_scale'] for r in data[s]['rows'])}–{max(r['Kt_scale'] for r in data[s]['rows'])}×)" for s in SPEC], fontsize=8.5)
ax.set_ylabel("θ* = 1/(1+κ_min)  [adimensional]", fontsize=9)
ax.set_title("Figura 4 — Contenção por espécie: θ* nos pontos de banda de cinética (Kt)\n"
             "Barras escuras = bandas centrais (todas em 0,333–0,400 = Cenário B); extremos degradam (hamster 4×: θ*=0,111 ⇒ κ=8)\n"
             "× = escape em todo o κ varrido · defs pré-registradas P-024 [SIM]", fontsize=9)
ax.set_ylim(0, 0.48)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
out = os.path.join(FIGS, "fig4_theta_species.png")
plt.savefig(out, bbox_inches="tight")
json.dump(plot_data, open(os.path.join(FIGS, "fig4_theta_species_data.json"), "w"), indent=1)
print("→", out)
