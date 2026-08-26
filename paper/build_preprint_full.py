#!/usr/bin/env python3
"""PREPRINT COMPLETO v4 — 16-20 páginas, bilíngue (EN+PT), IMRaD, com TODOS os workstreams.
Fontes: review_verdicts.md, solution_branches.md, fractal_review.md, analogy_map.md,
ws_7_transport.md, ws_9 (v2/v4 results), bayes_success.json, g0_protocol.md, 42 refs.
Uso: /workspace/.venv-numpy/bin/python build_preprint_full.py"""
import os, json, re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, Image as RLImage, PageBreak, NextPageTemplate,
                                KeepTogether, HRFlowable)

HERE=os.path.dirname(os.path.abspath(__file__))
Q=os.path.join(HERE,'..')
OUT_EN=os.path.join(HERE,'preprint_v4_EN.pdf')
OUT_PT=os.path.join(HERE,'preprint_v4_PT.pdf')

INK=HexColor('#101426'); MUT=HexColor('#4a5570'); ACC=HexColor('#0f6b4f'); ACC2=HexColor('#8a3f12')
LINE=HexColor('#c8d2c8')
ss=getSampleStyleSheet()
def st(name,**kw):
    base=dict(fontName='Helvetica',fontSize=9.5,leading=13.8,textColor=INK,alignment=4,spaceAfter=5)
    base.update(kw); return ParagraphStyle(name,parent=ss['Normal'],**base)
S_TITLE=st('T',fontName='Helvetica-Bold',fontSize=16.5,leading=20,alignment=1,textColor=INK,spaceAfter=8)
S_SUB=st('S',fontSize=9.5,alignment=1,textColor=MUT,leading=13)
S_H1=st('H1',fontName='Helvetica-Bold',fontSize=13,leading=16,textColor=ACC,spaceBefore=14,spaceAfter=6)
S_H2=st('H2',fontName='Helvetica-Bold',fontSize=11,leading=14,textColor=INK,spaceBefore=9,spaceAfter=4)
S_H3=st('H3',fontName='Helvetica-BoldOblique',fontSize=9.8,leading=13,textColor=ACC2,spaceBefore=7,spaceAfter=3)
S_B=st('B')
S_ABS=st('AB',fontSize=9.2,leading=13.2,leftIndent=14,rightIndent=14,textColor=MUT)
S_KW=st('KW',fontSize=8.6,leading=11,textColor=MUT,leftIndent=14)
S_REF=st('R',fontSize=7.8,leading=10.6,textColor=MUT,leftIndent=10,spaceAfter=2,alignment=0)
S_TN=st('TN',fontSize=7.8,leading=10,textColor=MUT)
S_CAP=st('CAP',fontSize=8.2,leading=11,textColor=MUT,alignment=1,spaceBefore=2)

def fmt(t):
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t); t=re.sub(r'\*(.+?)\*',r'<i>\1</i>',t)
    for a,b in [('→','&rarr;'),('≥','&ge;'),('≤','&le;;'.replace(';','')),('×','&times;'),('≈','&asymp;'),
                ('Δ','&Delta;'),('κ','&kappa;'),('θ','&theta;'),('ℓ','&#8467;'),('¹','&sup1;'),('²','&sup2;'),
                ('³','&sup3;'),('⁵','&#8309;'),('⁶','&#8310;'),('–','–'),('α','&alpha;'),('λ','&lambda;'),
                ('µ','&micro;'),('π','&pi;'),('∈','&isin;'),('√','&radic;'),('₀','&#8320;'),('¹⁰','&#185;&#8304;'),
                ('‖','&#8214;'),('"','"'),('<sub>','<sub>'),('β','&beta;'),('ξ','&xi;'),('₁','&#8321;')]:
        t=t.replace(a,b)
    return t

def T(data, widths, header=True, fs=8.0):
    tb=Table([[Paragraph(fmt(c) if isinstance(c,str) else c,st('td',fontSize=fs,leading=fs+3,alignment=0,spaceAfter=0)) for c in row] for row in data],
             colWidths=widths,repeatRows=1 if header else 0)
    sty=[('GRID',(0,0),(-1,-1),0.35,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),
         ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]
    if header: sty.append(('BACKGROUND',(0,0),(-1,0),HexColor('#e8f0ea')))
    tb.setStyle(TableStyle(sty)); return tb

def fig_block(path,caption,w=15.5*cm):
    if not os.path.exists(path): return Paragraph(fmt(f'*[{caption} — arquivo: {os.path.basename(path)} não encontrado]*'),S_TN)
    return KeepTogether([RLImage(path,width=w,height=w*0.42 if 'compare' in path or 'v2' in path or 'panel' in path else w*0.62),
                         Paragraph(fmt(caption),S_CAP)])

# ---------- dados reais dos workstreams ----------
W7=json.load(open(os.path.join(Q,'experiments/ws_7_results/ws_7_results.json'))) if os.path.exists(os.path.join(Q,'experiments/ws_7_results/ws_7_results.json')) else {}
W9V4={'days_per_simunit':144.02,'t_double_human_days':12.1,'theta_star':0.333,
      'sweep':[{'kappa':2.0,'theta':0.333,'R_mm':0.82},{'kappa':3.0,'theta':0.25,'R_mm':0.80},
               {'kappa':4.0,'theta':0.2,'R_mm':0.78},{'kappa':8.0,'theta':0.111,'R_mm':0.76},
               {'kappa':32.0,'theta':0.03,'R_mm':0.70}],
      'MV1':{'kappa4_R_mm':0.69,'baseline_R_mm':2.83}}
BAYES=json.load(open(os.path.join(Q,'experiments/bayes_results/bayes_success.json'))) if os.path.exists(os.path.join(Q,'experiments/bayes_results/bayes_success.json')) else {}

SNAP=os.path.join(Q,'artifacts/dashboard/snapshots')
WS9PNG=os.path.join(SNAP,'ws9_curva_resposta.png')

# =====================================================================
def build(lang):
    L=lang
    txt=TEXTS[L]
    doc=BaseDocTemplate(OUT_EN if L=='EN' else OUT_PT, pagesize=A4,
        leftMargin=1.9*cm,rightMargin=1.9*cm,topMargin=2.0*cm,bottomMargin=1.9*cm,
        title=txt['title'],author='Prion & Molecular Engineering Consortium (Quest 003)')
    frame=Frame(doc.leftMargin,doc.bottomMargin,doc.width,doc.height,id='n')
    def deco(canv,doc_):
        canv.saveState()
        canv.setFont('Helvetica',7.2); canv.setFillColor(MUT)
        canv.drawString(1.9*cm,1.15*cm,txt['footer'])
        canv.drawRightString(A4[0]-1.9*cm,1.15*cm,txt['footer2'] % {'p':canv.getPageNumber()})
        canv.setStrokeColor(LINE); canv.line(1.9*cm,1.45*cm,A4[0]-1.9*cm,1.45*cm)
        canv.restoreState()
    doc.addPageTemplates([PageTemplate(id='n',frames=[frame],onPage=deco)])
    E=[]
    P=lambda t,s=S_B: E.append(Paragraph(fmt(t),s))
    PB=lambda: E.append(PageBreak())

    # ---- título ----
    P(txt['title'],S_TITLE); P(txt['subtitle'],S_SUB); P(txt['authors'],S_SUB); Spacer(1,6)
    E.append(HRFlowable(width='100%',thickness=1,color=ACC,spaceAfter=8))

    P(txt['abstract_h'],S_H1); P(txt['abstract'],S_ABS); P(txt['keywords'],S_KW)

    # 1 intro
    P(txt['s1_h'],S_H1)
    for t in txt['s1']: P(t)
    # 2 método do programa
    P(txt['s2_h'],S_H1); P(txt['s2_p'])
    E.append(T(txt['s2_t1'],[3.2*cm,5.4*cm,7.2*cm])); P(txt['s2_tn'],S_TN)
    P(txt['s2b_h'],S_H2)
    E.append(T(txt['s2_t2'],[4.6*cm,11.2*cm]))
    # 3 molecular
    P(txt['s3_h'],S_H1)
    for t in txt['s3']: P(t)
    E.append(T(txt['s3_t1'],[5.4*cm,10.4*cm]))
    # 4 refutações/ramos
    P(txt['s4_h'],S_H1); P(txt['s4_p'])
    E.append(T(txt['s4_t1'],[2.2*cm,6.6*cm,6.2*cm]))
    P(txt['s4_p2'])
    # 5 vetores
    P(txt['s5_h'],S_H1); P(txt['s5_p'])
    E.append(T(txt['s5_t1'],[3.4*cm,4.4*cm,4.2*cm,3.2*cm]))
    P(txt['s5_p2'])
    # 6 G0
    P(txt['s6_h'],S_H1); P(txt['s6_p'])
    E.append(T(txt['s6_t1'],[1.7*cm,6.5*cm,7.2*cm]))
    P(txt['s6_p2'])
    # 7 WS-7
    P(txt['s7_h'],S_H1)
    for t in txt['s7']: P(t)
    P(txt['s7_rh'],S_H2)
    E.append(T(txt['s7_t1'],[4.8*cm,3.2*cm,3.4*cm,4.2*cm]))
    P(txt['s7_rules'],S_H3)
    E.append(T(txt['s7_t2'],[1.1*cm,8.4*cm,6.0*cm]))
    # 8 WS-9
    P(txt['s8_h'],S_H1)
    for t in txt['s8_intro']: P(t)
    P(txt['s8_eq'],st('EQ',fontName='Courier',fontSize=9,alignment=1,textColor=INK,spaceBefore=4,spaceAfter=4))
    E.append(T(txt['s8_t1'],[4.5*cm,11.3*cm]))
    P(txt['s8_rh'],S_H2); P(txt['s8_clock'])
    E.append(T([[h]+row for h,row in zip(txt['s8_t2_h'],
        [['35 dpi','2.13&times;10&#8309;','~12.1 d','0.82 mm @ &kappa;=2'],
         ['169 dpi','1.69&times;10&sup3;','(126&times; ratio)','0.69 mm @ &kappa;=4']])],[3.2*cm,3.4*cm,3.6*cm,5.6*cm]))
    P(txt['s8_emerg'])
    if os.path.exists(WS9PNG): E.append(fig_block(WS9PNG,txt['s8_fig']))
    P(txt['s8_pred'],st('BOX',fontSize=9.2,leading=13.4,leftIndent=10,rightIndent=10,
                        borderColor=ACC,borderWidth=0.8,spaceBefore=6,spaceAfter=8))
    # 9 bayes
    P(txt['s9_h'],S_H1)
    for t in txt['s9']: P(t)
    E.append(T(txt['s9_t1'],[6.4*cm,4.6*cm,4.8*cm]))
    # 10 analogias
    P(txt['s10_h'],S_H1); P(txt['s10_p'])
    E.append(T(txt['s10_t1'],[7.4*cm,8.4*cm]))
    # 11 ética/regulatório
    P(txt['s11_h'],S_H1)
    for t in txt['s11']: P(t)
    E.append(T(txt['s11_t1'],[4.6*cm,11.2*cm]))
    # 12 limitações
    P(txt['s12_h'],S_H1)
    E.append(T(txt['s12_t1'],[3.6*cm,6.2*cm,5.8*cm]))
    # 13 síntese fractal
    P(txt['s13_h'],S_H1)
    for t in txt['s13']: P(t)
    # refs
    P(txt['refs_h'],S_H1)
    for i,r in enumerate(txt['refs'],1): P(f'[{i}] {r}',S_REF)
    PB()
    P(txt['data_h'],S_H1); P(txt['data_p'])
    doc.build(E)
    print('OK', OUT_EN if L=='EN' else OUT_PT, os.path.getsize(OUT_EN if L=='EN' else OUT_PT),'bytes')

import preprint_texts, preprint_texts_pt
TEXTS={'EN':preprint_texts.EN,'PT':preprint_texts_pt.PT}
TEXTS['EN']=preprint_texts.EN
TEXTS['PT']=preprint_texts_pt.PT

build('EN'); build('PT')
