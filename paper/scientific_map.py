#!/usr/bin/env python3
"""SCIENTIFIC MAP — diagrama de como o projeto foi executado (pipeline metodológico)
Para: coorientador / banca doutoral. Render PIL 1600x1150."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "/root/DeepScientist/quests/003/artifacts/dashboard/snapshots/scientific_map.png"
FD = "/usr/share/fonts/truetype/dejavu/"
def F(sz, b=False): return ImageFont.truetype(FD + ("DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf"), int(sz))

W, H = 1650, 1200
img = Image.new("RGB", (W, H), "#0b1020")
d = ImageDraw.Draw(img)
d.fontmode = "1"

PHASES = [
    ("FASE 1 — AUDITORIA DA LITERATURA", "#22c55e", 60,
     ["~90 buscas científicas", "9 blocos de evidência (60 achados)", "~30 papers lidos na íntegra",
      "42 refs verificadas por abertura", "ERROS CORRIGIDOS: citação retratada, links errados,", "linhagem celular impossível, fábrica SVZ"]),
    ("FASE 2 — FÍSICA DE TRANSPORTE (WS-7)", "#3b82f6", 415,
     ["solver ADR auto-testado", "massa 100% · Thiele 0.5%", "REGRA 1: anel 8-12mm", "REGRA 2: hidrogel ξ≥5·rp",
      "REGRA 3: redose ≤7 dias", "casca de contenção 4-9mm"]),
    ("FASE 3 — PROBABILIDADE (WS-8)", "#a78bfa", 770,
     ["Bayes hierárquico 10 análogos", "inclui 6/6 falhas do campo", "G0-go: 36.6% [14.6-60.5]", "desaceleração: 5% vs 30-45%",
      "duas lentes rotuladas (sem fabricação)", ""]),
    ("FASE 4 — MODELO IN-SILICO (WS-9)", "#f59e0b", 1125,
     ["kernel Igel 2024 (código aberto)", "decodificação findreac: C→2C motor", "capping V127ΔGPI (nosso, inédito)",
      "relógio humano: 144d/unid (Groveman)", "θ* = 0.333 · MV2>MV1 emergente", "v1 falhou → documentado → pivot v2/v4"]),
]

TOP = [
    ("INPUT: protocolo V127 v0\n(revisão solicitada)", 60, 280),
    ("VALIDAÇÃO REGULATÓRIA\n(tofersen·nusinersen·Lund·tafamidis)", 60, 620),
    ("OUTPUT: PROGRAMA G0-G4\npredições pré-registradas", 60, 980),
]

for title, color, x in [(p[0], p[1], p[2]) for p in PHASES]:
    d.rounded_rectangle([x-12, 130, x+330, 560], radius=12, fill="#101830", outline=color, width=2)
    d.text((x+8, 145), title.split(" — ")[0], font=F(13, True), fill=color)
    d.text((x+8, 165), title.split(" — ")[1] if " — " in title else "", font=F(11), fill="#8b96b3")
    for i, line in enumerate(PHASES[[p[0] for p in PHASES].index(title)][3]):
        d.text((x+10, 200+i*22), line, font=F(11), fill="#c9d2e8")

d.text((60, 620), "VALIDAÇÃO REGULATÓRIA", font=F(13, True), fill="#7cc4ff")
d.text((60, 644), "tofersen · nusinersen · Lund 2026 · tafamidis", font=F(11), fill="#8b96b3")
d.text((60, 668), "→ nenhuma categoria inédita exigida", font=F(11), fill="#c9d2e8")

d.text((60, 740), "GARANTIAS (harness skill scientific-writing)", font=F(13, True), fill="#7cc4ff")
guar = ["33 fontes E-ID · 43 claims C-ID · 23 fatos numéricos N-ID",
        "4 validadores oficiais: ZERO erros",
        "binding linha-a-linha [claim:]→[evidence:]→sha256→DOI",
        "cross-artefato 13/13 · AST 20/20 · PRISMA 5/5 (gap GRADE declarado)",
        "repositório público com timestamp — predições ANTES de experimento"]
for i, g in enumerate(guar):
    d.text((60, 768+i*22), g, font=F(11), fill="#c9d2e8")

d.text((60, 920), "ENTREGAS PARA COORIENTADOR/BANCA", font=F(13, True), fill="#7cc4ff")
ent = ["1. Manuscrito EN+PT (reivindicações rastreadas) — manuscript_{EN,PT}_v4.md",
       "2. Preprint PDF EN/PT — preprint_v4_{EN,PT}.pdf",
       "3. LaTeX Cambridge 2-col pós-revisão hostil — paper/latex/manuscript_v41.tex",
       "4. Revisão hostil (8 major endereçados) — hostile_review_v4.md",
       "5. Evidence workspace (manifestos+claims+consistência) — paper/evidence_workspace/",
       "6. Grafo de conhecimento vivo — dashboard 8137 + graphify",
       "7. ESTE MAPA — scientific_map.png (pipeline de execução)"]
for i, e in enumerate(ent):
    d.text((60, 948+i*22), e, font=F(11), fill="#c9d2e8")

# fluxo horizontal das fases
ys = 345
for i in range(3):
    x1, x2 = PHASES[i][2]+330, PHASES[i+1][2]-12
    d.line([x1, ys, x2, ys], fill="#5f6c8f", width=3)
    d.polygon([(x2-14, ys-8), (x2, ys), (x2-14, ys+8)], fill="#5f6c8f")

# fluxo input → fase1
d.line([300, 155, 300, 130], fill="#22c55e", width=3)
d.text((1200, 590), "PREDIÇÃO PRÉ-REGISTRADA DO G0:", font=F(15, True), fill="#ff8a5c")
d.text((1200, 620), "θ_medido < 0.33 ⇒ contenção in situ", font=F(13, True), fill="#ffffff")
d.text((1200, 648), "halo 4-6mm · anel 8-12mm · leitura 90-120d", font=F(12), fill="#c9d2e8")
d.text((1200, 684), "Próximo gate: organoide G0 (8 braços, 10 meses)", font=F(12), fill="#8b96b3")
d.text((1200, 714), "Cenários: desaceleração 30-45% | compassivo mRNA 50-70%", font=F(12), fill="#8b96b3")

# arcos fase→garantias e fase→output
d.arc([440, 560, 1000, 900], 20, 160, fill="#3b82f6", width=2)
d.text((690, 880), "todo número → JSON → claim → fonte", font=F(11), fill="#3b82f6")

img.save(OUT)
print("MAPA SALVO:", OUT, img.size)
