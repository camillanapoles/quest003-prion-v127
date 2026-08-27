#!/usr/bin/env python3
"""Figuras v5 (fig2/fig3) geradas EXCLUSIVAMENTE dos JSONs reais do repositório.
Fontes: experiments/ws_9_results/ws_9_v4_human.json (run da autora, Colab)
        experiments/bayes_results/bayes_success.json
Paleta Okabe-Ito (colorblind-safe); 300 dpi; sem valor digitado à mão."""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
WS9 = json.load(open(os.path.join(REPO, "experiments/ws_9_results/ws_9_v4_human.json")))
BAY = json.load(open(os.path.join(REPO, "experiments/bayes_results/bayes_success.json")))

# Okabe-Ito
BLUE, ORANGE, VERM, GRAY, SKY = "#0072B2", "#E69F00", "#D55E00", "#999999", "#56B4E9"

# ─── FIG 2: resposta θ — frente R(κ) vs baseline + tiers T2/T3 ───
sweep = WS9["sweep_MV2"]                       # [{kappa, theta, R_mm}...]
ks   = [s["kappa"] for s in sweep]
Rs   = [s["R_mm"] for s in sweep]
th   = [s["theta"] for s in sweep]
R0   = WS9["MV1"]["baseline_R_mm"]             # 2.83 (baseline compartilhado)
theta_star = WS9["theta_star"]                 # 0.333

fig, ax = plt.subplots(figsize=(4.6, 3.4))
ax.axhline(R0, color=GRAY, ls=":", lw=1.2)
ax.text(1.02, R0, f"disease baseline {R0:.2f} mm", va="bottom", fontsize=7, color=GRAY)
ax.axhline(R0/2, color=VERM, ls="--", lw=1.1)
ax.text(1.02, R0/2, f"T3 informative tier ({R0/2:.2f} mm = 50%)", va="bottom", fontsize=7, color=VERM)
ax.axhline(0.9*R0, color=SKY, ls="--", lw=1.0)
ax.text(1.02, 0.9*R0, "T2 minimal screening (90%)", va="bottom", fontsize=7, color=SKY)
ax.plot(ks, Rs, "o-", color=BLUE, lw=1.8, ms=6)
for k, r, t in zip(ks, Rs, th):
    ax.annotate(f"θ={t:.3f}", (k, r), textcoords="offset points", xytext=(6, 7),
                fontsize=7, color=BLUE)
ax.set_xscale("log", base=2)
ax.set_xticks(ks); ax.set_xticklabels([str(int(k)) for k in ks])
ax.set_xlabel("capping strength κ")
ax.set_ylabel("asymptotic front radius R (mm)")
ax.set_title(f"Containment response — humanized clock (θ* = {theta_star}; all κ≥2 pass T3)",
             fontsize=8.5)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig2_theta_response.png"), dpi=300)

# ─── FIG 3: consistência de subtipos MV2/MV1 ───
mv2_k4 = next(s["R_mm"] for s in sweep if s["kappa"] == 4.0)
mv1_k4 = WS9["MV1"]["kappa4_R_mm"]
t_mv2, t_mv1 = WS9["anchors"]["titer_MV2"], WS9["anchors"]["titer_MV1"]
ratio = t_mv2 / t_mv1

fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.8, 3.0))
# (a) raio contido por subtipo
bars = a1.bar(["MV2-like", "MV1-like"], [mv2_k4, mv1_k4],
              color=[ORANGE, BLUE], width=0.55)
a1.axhline(R0, color=GRAY, ls=":", lw=1.2)
a1.text(-0.4, R0, f"baseline {R0:.2f} mm", fontsize=7, color=GRAY, va="bottom")
for b, v in zip(bars, [mv2_k4, mv1_k4]):
    a1.text(b.get_x()+b.get_width()/2, v+0.03, f"{v:.2f}", ha="center", fontsize=8)
a1.set_ylabel("contained front radius at κ=4 (mm)")
a1.set_title("(a) both subtypes contained\n(MV2 > MV1 hierarchy preserved)", fontsize=8.5)
a1.spines[["top", "right"]].set_visible(False)
# (b) âncoras de semente (log)
a2.bar(["MV2 seed", "MV1 seed"], [t_mv2, t_mv1], color=[ORANGE, BLUE], width=0.55)
a2.set_yscale("log")
for x, v in [(0, t_mv2), (1, t_mv1)]:
    a2.text(x, v*1.35, f"{v:.2e}", ha="center", fontsize=8)
a2.set_ylabel("titer at 169 dpi (SD50/mg)")
a2.set_title(f"(b) seed anchors (ratio {ratio:.0f}×, Groveman 2019)\nunfitted input of the run", fontsize=8.5)
a2.spines[["top", "right"]].set_visible(False)
fig.suptitle("Emergent qualitative consistency: hierarchy was never fitted", fontsize=9, y=1.02)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "fig3_subtypes.png"), dpi=300, bbox_inches="tight")

print("fig2_theta_response.png + fig3_subtypes.png geradas de:",
      os.path.basename(str(WS9.get('motor'))), "| θ* =", theta_star,
      "| baseline", R0, "| MV2/MV1", round(mv2_k4, 2), "/", round(mv1_k4, 2))
