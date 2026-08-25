#!/usr/bin/env python3
"""Gera estado_atual.html a partir de data.json — rodar a cada sessão da quest 003."""
import json, html, sys
d=json.load(open(__file__.replace('gen_estado.py','data.json')))
N={n['id']:n for n in d['nodes']}
S={'confirmed':('#22c55e','✓','VALIDADO'),'constraint':('#f59e0b','⚠','RESTRIÇÃO'),'refuted':('#ef4444','✕','REFUTADO'),'proposed':('#3b82f6','⏳','PENDENTE'),'active':('#a78bfa','▶','ATIVO')}
IV={'+':('#22c55e','▲'),'-':('#ef4444','▼'),'±':('#f59e0b','◆'),'o':('#8b96b3','·')}
conf=[n for n in d['nodes'] if n['status']=='confirmed']
rest=[n for n in d['nodes'] if n['status']=='constraint']
refu=[n for n in d['nodes'] if n['status']=='refuted']
pend=[n for n in d['nodes'] if n['status'] in ('proposed','active')]
def card(n):
    c,ico,_=S[n['status']]
    iv=n.get('implies',{})
    col,sym=IV.get(iv.get('val','-'),('#8b96b3','·'))
    imp=html.escape(iv.get('text','')) if iv else ''
    return f'''<div class="card" style="border-color:{c}"><span class="ico" style="color:{c}">{ico}</span><b>{html.escape(n['label'])}</b><span class="ev">📄 o que diz: {html.escape(n.get('evidence',''))}</span><div class="imp" style="border-left-color:{col}"><span style="color:{col}">➞ diretriz {sym}</span><br>{imp}</div></div>'''
ramos=[
 ("R1 · NSC não gera micróglia","#ef4444",[("✔ RESOLVIDO — co-enxerto iMG (Abud 2017 Neuron, ~5 sem); iMG entra em G1+, G0 segue limpo","#22c55e","")]),
 ("R2 · Fábrica SVZ impossível como prometida","#ef4444",[
   ("(a) depósito parede ventricular — DEFAULT · P=0.45 · G1 · kill: <20% viáveis @90d","#8b96b3",""),
   ("(b) depósitos multi-nó em hubs de rede (sem SVZ) · P=0.40 · G1 paralelo","#8b96b3",""),
   ("⭐ (c) mRNA-LNP intratecal V127ΔGPI — Xue/Dong 2025 · P=0.35-0.50 · resolve R2+R3+R4 · braço G0-A7 · kill: expressão <nível DN >7d","#ff8a5c","focal")]),
 ("R3 · Contenção espacial <20%","#ef4444",[
   ("(a) anel + nós de rede (tratografia) · P(freio)=0.35-0.50","#8b96b3",""),
   ("(b) ASO-ponte intratecal periop + enxerto · P=0.45-0.55 (sinergia inédita)","#8b96b3",""),
   ("⭐ (c) mRNA global (R2c) base + enxerto focal pico · P=0.40-0.55 — gradiente vira dose/frequência","#ff8a5c","")]),
 ("R4 · Janela esporádica × produção celular","#ef4444",[
   ("(a) E200K/D178N pré-sintomáticos autólogos — DEFAULT · P=0.80","#22c55e",""),
   ("⭐ (b) banco hipoimune HLA-KO+CD47 (Han 2019; Hu 2024: CD47 N&S contra NK) · P=0.50-0.60 · G1.5 (cérebro inflamado)","#ff8a5c",""),
   ("(c) mRNA-LNP: ciclo de dias, sem célula · P=0.60-0.70 compassivo","#8b96b3","")]),
 ("R5 · Enxerto morre em microambiente hostil (15-30%)","#ef4444",[
   ("⭐ (a) hidrogel HA macio pró-sobrevivência (Liang 2013; Chen 2023) · P=0.45 · porosidade resolve WS-7","#ff8a5c",""),
   ("(b) anti-inflamatório: MINADO — Shah 2017 RETRACTED; Cheng 2015 sem ganho; micróglia defensora · P=0.20 (só ponte 48-72h)","#f59e0b",""),
   ("(c) hibernação metabólica/hipóxia in vitro · P=0.25 · nicho","#8b96b3","")]),
 ("R6 · Rejeição de aloenxerto","#ef4444",[
   ("(a) autólogo E200K — DEFAULT · CEP/CONEP desenhado","#22c55e",""),
   ("(b) iPSC hipoimune (R4b) · P=0.50-0.60 · G1.5","#8b96b3",""),
   ("(c) banco HLA-homozigoto (modelo CiRA) · P=0.35 no BR","#8b96b3","")]),
 ("R7 · Regeneração do núcleo morto","#ef4444",[("→ REFRAME permanente: alvo = penumbra (Williams 2023) + conter progressão — 'cura do núcleo' fora do escopo","#f59e0b","")]),
 ("R8 · Margem DTI não resolve microfoco","#ef4444",[
   ("(a) RT-QuIC intraop em biópsias de borda · (b) IHC rápida PrP-res (20-30min) · P=0.5","#8b96b3",""),
   ("(c) PET-tracer de PrPSc: NÃO EXISTE validado → GAP DO CAMPO (oportunidade)","#a78bfa","")]),
]
r_html=''.join(f'''<div class="ref"><div class="rtitle" style="border-color:{col}">{html.escape(t)}</div>{''.join(f'<div class="branch {"focal" if f else ""}" style="border-left-color:{bc}">{html.escape(b)}</div>' for b,bc,f in brs)}</div>''' for t,col,brs in ramos)
insights=[
 ("🏆 INSIGHT TRANSVERSAL","mRNA-LNP intratecal ataca 3 refutações simultâneas (fábrica+janela+cobertura) — e Gatdula (persistência pós-cessação) neutraliza sua fraqueza (durabilidade). G0-A7 = menor custo, maior informação."),
 ("🛡️ Segurança de dado","CD47 'necessário e suficiente' contra NK (Hu 2024) — gate do banco universal é binário e rápido (G1.5)."),
 ("🧩 Reciclagem correta","Hidrogel do colaborador reabilitado como carreador HA macio — porosidade vira input do WS-7."),
 ("⚠️ Contraintuição","Micróglia é DEFENSORA no príon (depleção acelera; De Lucia 2016) — iMG racional; anti-inflamatório sistêmico é armadilha; Shah 2017 RETRACTED."),
 ("🕳️ Gap do campo","Não existe PET-tracer de PrPSc — margem cirúrgica hoje é inferida. Radiotracer = colaboração futura."),
 ("📉 Calibração","PRN100: seguro ≠ eficaz. Desfecho primário honesto = desaceleração (30-45%)."),
]
i_html=''.join(f'<div class="insight"><b>{t}</b><p>{txt}</p></div>' for t,txt in insights)
gates=''.join(f'''<div class="gate {'r' if g['tone']=='ready' else 'w'}"><b>{g['id']} · {html.escape(g['name'])}</b><span class="st">{g['status']}</span><div class="dt">{html.escape(g['detail'])}</div></div>''' for g in d['gates'])
css='''
:root{--bg:#0b1020;--ink:#e5eaf5;--mut:#8b96b3;--line:#26304f;--focal:#ff8a5c}
*{margin:0;box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,"Segoe UI",Roboto,sans-serif;padding:0 0 60px}
header{padding:18px 22px 12px;border-bottom:1px solid var(--line)}
h1{font-size:19px}.sub{color:var(--mut);font-size:12.5px;margin-top:2px}
.msg{font-family:Georgia,serif;font-style:italic;color:#ffd9c7;padding:10px 22px;border-bottom:1px solid var(--line);background:linear-gradient(90deg,rgba(255,138,92,.07),transparent 70%)}
.stats{display:flex;gap:14px;flex-wrap:wrap;padding:10px 22px;border-bottom:1px solid var(--line);font-size:13px;color:var(--mut)}.stats b{color:var(--ink)}
section{padding:16px 22px;border-bottom:1px solid var(--line)}
h2{font-size:13px;letter-spacing:1.6px;text-transform:uppercase;margin-bottom:12px}
h2 .n{color:var(--mut);font-weight:400}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:10px}
.card{border:1px solid;border-radius:10px;background:#141d3a;padding:10px 12px;position:relative}
.card b{display:block;font-size:13px;margin:2px 0 4px;padding-right:22px}
.card .ev{font-size:11px;color:var(--mut);display:block;margin-bottom:6px}
.card .ico{position:absolute;top:10px;right:10px;font-size:14px}
.card .imp{font-size:12px;color:#c9d2e8;border-left:3px solid;padding:4px 8px;background:#101830;border-radius:0 6px 6px 0}
.ref{margin-bottom:14px}.rtitle{font-size:13.5px;font-weight:650;border-left:4px solid;padding:4px 10px;background:#151d38;border-radius:0 8px 8px 0;margin-bottom:6px}
.branch{font-size:12.5px;padding:6px 10px 6px 26px;border-left:2px solid var(--line);margin:3px 0 3px 14px;color:#c9d2e8;border-radius:0 8px 8px 0;background:#101830}
.branch.focal{border-left-color:var(--focal);background:#1d1626;color:#ffd9c7}
.gates{display:flex;flex-wrap:wrap;gap:10px}
.gate{border:1px solid var(--line);border-radius:10px;padding:10px 12px;min-width:230px;flex:1;background:#141d3a}
.gate.r{border-color:#2e5e43}.gate.w{border-color:#5e4a2e}
.gate b{font-size:13px}.gate .st{display:block;font-size:11px;color:#22c55e;margin:4px 0}
.gate .dt{font-size:11px;color:var(--mut)}
.insight{border:1px dashed var(--line);border-radius:10px;padding:10px 12px;margin-bottom:8px;background:#111a33}
.insight b{font-size:13px;color:#7cc4ff}.insight p{font-size:12.5px;color:#c9d2e8;margin-top:4px}
'''
htmlout=f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Quest 003 — Estado Atual da Pesquisa</title><style>{css}</style></head><body>
<header><h1>Quest 003 · Estado Atual — DCJ / PrP-G127V</h1><div class="sub">{html.escape(d['meta']['subtitle'])} · {d['meta']['version']} · {d['meta']['updated']} · gerado de data.json por gen_estado.py</div></header>
<div class="msg">📌 {html.escape(d['meta']['message'])}</div>
<div class="stats"><span><b>{len(conf)}</b> validados</span><span><b>{len(rest)}</b> restrições</span><span><b>{len(refu)}</b> refutados → <b>8</b> árvores</span><span><b>{len(pend)}</b> pendentes</span><span><b>5</b> gates</span><span>implicações: <b style="color:#22c55e">21 ▲</b> <b style="color:#ef4444">9 ▼</b> <b style="color:#f59e0b">3 ◆</b> <b>5 ·</b></span><span>desaceleração composta <b>30-45%</b></span></div>
<section><h2>✓ Validado <span class="n">— 📄 o que o paper diz ➞ ▲▼ o que implica para a tese</span></h2><div class="grid">{''.join(card(n) for n in conf)}</div></section>
<section><h2>⚠ Restrições <span class="n">— verdades com condição</span></h2><div class="grid">{''.join(card(n) for n in rest)}</div></section>
<section><h2>✕→🌿 Refutado e ramos de solução <span class="n">— ⭐ = adotado · P = probabilidade estruturada</span></h2>{r_html}</section>
<section><h2>▶ Pendências <span class="n">— esperando gate</span></h2><div class="grid">{''.join(card(n) for n in pend)}</div></section>
<section><h2>⚙ Gates <span class="n">— o programa com kill-switches</span></h2><div class="gates">{gates}</div></section>
<section><h2>💡 Insights &amp; oportunidades</h2>{i_html}</section>
</body></html>'''
open(__file__.replace('gen_estado.py','estado_atual.html'),'w').write(htmlout)
print('estado_atual.html regenerado:',len(conf),'val ·',len(pend),'pend ·',d['meta']['version'])
