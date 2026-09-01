#!/usr/bin/env python3
"""FIGURA 5 — Escada de dose A6 (M3.1) · auditável: lê APENAS m31_u1u2.json (número nunca digitado).
Saída: paper/latex/figs/fig5_dose_ladder.png (+ .json de dados plotados para rastreio).
Padrão Fig.4: determinístico, sem entrada manual; toda célula vem do registro U1+U2."""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FIGS = os.path.join(R, "paper", "latex", "figs")
os.makedirs(FIGS, exist_ok=True)

D = json.load(open(os.path.join(R, "experiments", "m31", "m31_u1u2.json")))
KT = ["Kt1", "Kt2", "Kt3", "Kt4"]

# ── dados da escada (SÓ do JSON) ──
ladder = {}
for kt in KT:
    ch = D["chain"][kt]
    c_lo, c_hi = ch["c_uM"]
    v_lo, v_hi = ch["V_dist_mL"]
    ratio = (c_hi / c_lo) * (v_hi / v_lo)          # largura da banda µg (κ cancela) — do JSON
    ladder[kt] = {"kappa_req": ch["kappa_req"],
                  "c_uM": ch["c_uM"], "V_dist_mL": ch["V_dist_mL"],
                  "ug_per_deposit": ch["ug_per_deposit"], "band_ratio_x": round(ratio, 1)}
    assert ch["ug_per_deposit"][1] > ch["ug_per_deposit"][0], "banda precisa de ≥2 extremos"

# self-check: largura da banda constante entre Kt (κ cancela na razão) — tolerância de arred.
ratios = [ladder[k]["band_ratio_x"] for k in KT]
assert max(ratios) / min(ratios) < 1.15, f"largura devia ser ~constante: {ratios}"

MW = D["u2_mw"]["mw_kDa"]
assert 22.0 < MW < 23.5  # guarda contra regeneração acidental com sequência errada

# ── plot ──
kd_ratio = D["u1_kd_band"]["hi"] / D["u1_kd_band"]["lo"]   # 14× — do JSON
v_ratio = ladder["Kt1"]["V_dist_mL"][1] / ladder["Kt1"]["V_dist_mL"][0]  # 3,7× — do JSON
ratio_mean = sum(ratios) / len(ratios)

fig, ax = plt.subplots(figsize=(8.6, 4.8), dpi=200)
colors = {"Kt1": "#77aadd", "Kt2": "#4477aa", "Kt3": "#88bbaa", "Kt4": "#aa3333"}
ymax = max(ladder[k]["ug_per_deposit"][1] for k in KT)

for i, kt in enumerate(KT):
    lo, hi = ladder[kt]["ug_per_deposit"]
    hatch = "///" if kt == "Kt4" else None
    ax.bar(i, hi - lo, bottom=lo, width=0.58, color=colors[kt],
           edgecolor="white", linewidth=0.6, hatch=hatch, zorder=3, alpha=0.92)
    ax.text(i, hi + ymax * 0.03, f"{lo:.1f}–{hi:.1f}", ha="center", fontsize=8.5, fontweight="bold")
    ax.text(i, ymax * 0.02 + lo, f"κ={ladder[kt]['kappa_req']:.4g}", ha="center", fontsize=7.2, color="#222222")

# banda humana (Kt 0,5–2 ⇒ colunas Kt1-Kt2; canon M3) e pior caso declarado (C057)
ax.axvspan(-0.5, 1.5, color="#ddeeff", alpha=0.5, zorder=0)
ax.text(0.5, ymax * 0.94, "banda humana Kt {0,5–2}", ha="center", fontsize=7.4, color="#336699")
ax.annotate("pior caso declarado\n(κ=8 cobre Kt=4; C057)", xy=(3, ladder["Kt4"]["ug_per_deposit"][1]),
            xytext=(2.42, ymax * 0.80), fontsize=7.2, color="#882222",
            arrowprops=dict(arrowstyle="->", color="#882222", lw=0.8))

ax.set_xticks(range(len(KT)))
ax.set_xticklabels([f"{kt}\n(c {ladder[kt]['c_uM'][0]:.2f}–{ladder[kt]['c_uM'][1]:.1f} µM no pico)" for kt in KT], fontsize=8.5)
ax.set_ylabel("µg de V127ΔGPI por depósito (banda GUM)", fontsize=9)
ax.set_title("Figura 5 — Escada de dose A6 (proteína recombinante): banda µg/depósito por banda-Kt do hospedeiro\n"
             f"Barras = banda [otimista, pior-caso] da cadeia κ→µM→nmol→µg de m31_u1u2.json (MW {MW:.2f} kDa, das sequências próprias P023)\n"
             f"Largura da banda ≈{ratio_mean:.0f}× em TODAS as bandas (κ cancela; dominada pelo Kd-proxy {kd_ratio:.0f}× e V-halo {v_ratio:.1f}×) — "
             "a largura É o achado até G0-A6 · redose ≤7 d\n"
             "[SIM]-planejamento (prognóstico calculado; NÃO prescrição)", fontsize=8.6)
ax.set_ylim(0, ymax * 1.12)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
out = os.path.join(FIGS, "fig5_dose_ladder.png")
plt.savefig(out, bbox_inches="tight")

plot_data = {"tier": D["tier"], "mw_kDa": MW, "ladder": ladder,
             "sources": "m31_u1u2.json (U1+U2); κ_req↔Kt p024 (M3, C057); banda humana Kt canon M3"}
json.dump(plot_data, open(os.path.join(FIGS, "fig5_dose_ladder_data.json"), "w"), indent=1)
print("→", out)
for kt in KT:
    print(f"{kt}: κ={ladder[kt]['kappa_req']} banda={ladder[kt]['ug_per_deposit']} µg/depósito (razão {ladder[kt]['band_ratio_x']}×)")
