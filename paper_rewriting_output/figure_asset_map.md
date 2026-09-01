# Figure Asset Map — tese unificada (braço-B)

Todas as figuras são **auditáveis**: número nunca digitado; scripts determinísticos leem JSONs do registro.

| Figura | Script gerador (determinístico) | Dados-fonte (JSON do registro) | Capítulo/blueprint | Saída | Status CI |
|---|---|---|---|---|---|
| Fig.1 — Mapa científico | `paper/latex/figs/make_figs_v5.py` | registro v5 | B1 (fundamento) | `fig1_scientific_map.png` | pré-existente |
| Fig.2 — θ-resposta | `paper/latex/figs/make_figs_v5.py` | ws_9_v4_human.json | B3 (G0-sim) | `fig2_theta_response.png` | pré-existente |
| Fig.3 — Subtipos | `paper/latex/figs/make_figs_v5.py` | ws_9 (MV1/MV2) | B6 (validação) | `fig3_subtypes.png` | pré-existente |
| Fig.4 — θ* multi-espécie | `experiments/xspecies/make_fig4_thetaspecies.py` | p024_{species}.json (4 espécies) | B6 + B7 (leito clínico) | `fig4_theta_species.png` + `_data.json` | tese-abnt.yml ✓ |
| **Fig.5 — Escada de dose A6 (M3.1)** | **`experiments/m31/make_fig5_doseladder.py`** | **`experiments/m31/m31_u1u2.json` (U1+U2)** | **B4 (aplicação: o desenho emerge)** | `fig5_dose_ladder.png` + `_data.json` | **tese-abnt.yml ✓ (adicionado nesta sessão, PR #6)** |

## Fig.5 — especificação probatória

- **Conteúdo**: banda GUM µg/depósito por banda-Kt (Kt1 κ=1,5 → Kt4 κ=8 pior-caso destacado); banda humana Kt {0,5–2} sombreada; largura ≈53× constante (κ cancela: 14× Kd-proxy × 3,7× V-halo) — computada do JSON.
- **Anotação de tier no título**: [SIM]-planejamento (NÃO prescrição) + redose ≤7 d + "a largura É o achado até G0-A6".
- **Binding**: claims C058–C060 · N-fatos N060–N065 · E057/E058/E032/E010/E030/E019.
- **Acessibilidade**: eixo-y linear com bandas explícitas (evita compressão log de valores arredondados a 0,0); anotações não-dependem só de cor (hatch no pior-caso; rótulos κ por barra).
