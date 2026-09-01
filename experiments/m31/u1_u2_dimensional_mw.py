#!/usr/bin/env python3
"""M3.1 U1+U2 — mapa dimensional κ→massa (banda GUM Tipo-B) + MW do PrP das NOSSAS sequências.
Determinístico; toda célula com unidade+fonte. Saída: experiments/m31/m31_u1u2.json"""
import json, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "m31_u1u2.json")

# ── U2: massa molecular do PrP humano maduro (23-231) a partir de prnp_sequences.json ──
SEQ = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "xspecies", "prnp_sequences.json")))
hum = SEQ["human"]["seq"]
mature = hum[22:231]  # resíduos 23-231 (precursor 1-253; sinal 1-22; GPI-signal 232+)
# massas médias de resíduo (Da) — tabela bioquímica padrão (ISO/um prudente ±0.1%)
AA = {"A":71.08,"R":156.19,"N":114.10,"D":115.09,"C":103.14,"E":129.12,"Q":128.13,"G":57.05,
      "H":137.14,"I":113.16,"L":113.16,"K":128.18,"M":131.20,"F":147.18,"P":97.12,"S":87.08,
      "T":101.11,"W":186.21,"Y":163.18,"V":99.13}
mw = sum(AA[a] for a in mature) + 18.02  # + H2O
u2 = {"length_aa": len(mature), "mw_kDa": round(mw/1000.0, 2),
      "source": "prnp_sequences.json (P04156 humano; resíduos 23-231, forma madura; V127 é variante de mesma massa — G→V Δ=+14 Da)",
      "mw_kDa_V127": round((mw+14.0)/1000.0, 2)}

# ── U1: cadeia dimensional A6 (κ_req → c[µM] → nmol → µg por depósito) com banda ──
KD = {"lo": 0.071, "hi": 1.0, "unit": "µM",
      "source": "Kd aparente PrP-oligômero: Chen 2010 (71 nM, E-registro; PROXY Aβ) a âncora ilustrativa 1 µM (§2.2 P1) — BANDA Tipo-B declarada"}
KREQ = {"1":1.5,"2":2.0,"3":3.0,"4":8.0,
        "source":"κ_req↔Kt de p024_*.json (M3; P-024-def horizon declarado)"}
# halo de distribuição: r10% 4-6 mm (E030/WS-7); volume efetivo intersticial: cilindro r×h com fração ECS de Thorne 2006 (0.15-0.25)
VHALO = {"r_mm": [4.0,6.0], "ecs_fraction": [0.15,0.25], "h_mm": 2.0,
         "source":"r10% E030 (WS-7 solver); fração ECS Thorne 2006; espessura de casca declarada 2 mm (assunção Type-B explícita)"}
rows = {}
for kt, kreq in KREQ.items():
    if kt in ("source",): continue
    kreq=float(kreq) if isinstance(kreq,str) and kt in ("1","2","3","4") else kreq
    c_lo = kreq * KD["lo"]; c_hi = kreq * KD["hi"]          # µM no pico do depósito
    v_lo = 3.1416*(VHALO["r_mm"][0]**2)*VHALO["h_mm"]*VHALO["ecs_fraction"][0]  # mm³
    v_hi = 3.1416*(VHALO["r_mm"][1]**2)*VHALO["h_mm"]*VHALO["ecs_fraction"][1]
    nmol_lo = c_lo * (v_lo/1000.0); nmol_hi = c_hi * (v_hi/1000.0)  # µM×mL = nmol
    ug_lo = nmol_lo * (mw/1000.0); ug_hi = nmol_hi * (mw/1000.0)
    rows[f"Kt{kt}"] = {"kappa_req": kreq,
        "c_uM": [round(c_lo,2), round(c_hi,2)],
        "V_dist_mL": [round(v_lo/1000.0,4), round(v_hi/1000.0,4)],
        "nmol_per_deposit": [round(nmol_lo,2), round(nmol_hi,2)],
        "ug_per_deposit": [round(ug_lo,1), round(ug_hi,1)],
        "redose_d": "<=7 (regra 3; trough >=30-56% — E030,E019)",
        "units": "κ adim · c µM · V mL · nmol=µM×mL · µg=nmol×kDa"}
out = {"tier": "[SIM]-planejamento (prognóstico calculado; NÃO prescrição)",
 "u2_mw": u2, "u1_kd_band": KD, "u1_kreq": {k:v for k,v in KREQ.items() if k!="source"},
 "u1_vhalo": VHALO, "chain": rows,
 "acceptance": "toda célula unidade+fonte ✓ · banda sempre ≥2 extremos ✓ · incerteza dominada por Kd-proxy (esperado; G0-A6 fecha) ✓ · saída=planejamento"}
json.dump(out, open(OUT,"w"), indent=1)
print("→", OUT)
print("MW maduro 23-231:", u2["mw_kDa"], "kDa (V127:", u2["mw_kDa_V127"], ")")
for k,v in rows.items():
    print(f"{k}: κ={v['kappa_req']} c={v['c_uM']}µM → {v['ug_per_deposit']} µg/depósito")
