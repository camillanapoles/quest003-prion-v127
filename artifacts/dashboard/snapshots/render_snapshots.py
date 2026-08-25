#!/usr/bin/env python3
"""Regenera snapshots PNG do grafo (história 8 passos + mapa completo).
Uso: python3 render_snapshots.py  (a partir de artifacts/dashboard/)"""
import json, math, os, sys, traceback
from PIL import Image, ImageDraw, ImageFont

HERE=os.path.dirname(os.path.abspath(__file__))
D=json.load(open(os.path.join(HERE,'..','data.json')))

GROUPS=[('molecular','① Fundamento molecular'),('classe','② Classe terapêutica'),('celular','③ Modelo celular'),('entrega','④ Entrega cirúrgica'),('traducao','⑤ Tradução')]
TIER={'molecular':'MOLECULAR','classe':'CLASSE','celular':'CELULAR','entrega':'ENTREGA','traducao':'TRADUÇÃO'}
OUT={'valid':('#22c55e','✓','VÁLIDO'),'invalid':('#ef4444','×','INVÁLIDO'),'gray_light':('#c9d4e5','◐','POSSÍVEL'),'gray_dark':('#74809a','◑','BAIXA')}
VALIDS={'confirmed':'valid','constraint':'valid','refuted':'invalid'}
FD='/usr/share/fonts/truetype/dejavu/'
def F(sz,b=False):
    p=FD+('DejaVuSans-Bold.ttf' if b else 'DejaVuSans.ttf')
    return ImageFont.truetype(p,int(max(8,sz)))
def outlook(n): return n.get('outlook') or VALIDS.get(n['status']) or 'gray_light'
def wrap(t,n=30):
    L=[];cur=''
    for w in t.split():
        if len((cur+' '+w).strip())<=n: cur=(cur+' '+w).strip()
        else:
            L.append(cur);cur=w
            if len(L)>=3: break
    if cur and len(L)<3: L.append(cur)
    if len(t)>100 and len(L)==3: L[2]=L[2][:26]+'…'
    return L[:3]
NW,NH,GX,GY,MARG,LABELY=250,96,56,120,70,44

def bez(p0,p1,p2,p3,N=50):
    P=[]
    for k in range(N+1):
        t=k/N;mt=1-t
        P.append((mt**3*p0[0]+3*mt*mt*t*p1[0]+3*mt*t*t*p2[0]+t**3*p3[0],
                  mt**3*p0[1]+3*mt*mt*t*p1[1]+3*mt*t*t*p2[1]+t**3*p3[1]))
    return P

def render(nodes,edges,label,out,scale=0.9):
    layers=[[n for n in nodes if n['group']==g[0]] for g in GROUPS]
    layers=[L for L in layers if L]
    byId={n['id']:n for n in nodes}
    rowW=lambda L:len(L)*NW+(len(L)-1)*GX
    W=MARG*2+max(max(rowW(L) for L in layers),760)
    H=30+len(layers)*(NH+GY)+LABELY+70
    img=Image.new('RGB',(int(W*scale),int(H*scale)),'#0b1020')
    dr=ImageDraw.Draw(img);dr.fontmode='1'
    S=lambda v:v*scale
    dr.text((S(14),S(8)),D['meta']['title'],font=F(19*scale,True),fill='#e5eaf5')
    dr.text((S(W-14),S(10)),D['meta']['version']+' · '+D['meta']['updated'],font=F(12*scale),fill='#8b96b3',anchor='ra')
    for li,L in enumerate(layers):
        yy=20+li*(NH+GY)+LABELY
        x0=(W-rowW(L))/2
        for i,n in enumerate(L):
            n['x']=x0+i*(NW+GX);n['y']=yy;n['cx']=n['x']+NW/2;n['cy']=n['y']+NH/2
    # edges
    for e in edges:
        if e['from'] not in byId or e['to'] not in byId: continue
        s=byId[e['from']];t=byId[e['to']]
        oa,ob=outlook(s),outlook(t)
        if oa=='invalid' or ob=='invalid': col='#ef4444'
        elif oa=='valid' and ob=='valid': col='#22c55e'
        elif oa=='valid' or ob=='valid': col='#3b82f6'
        else: col='#8b9bb8'
        if abs(s['y']-t['y'])>1:
            my=(s['y']+NH+t['y'])/2
            pts=bez((s['cx'],s['y']+NH),(s['cx'],my),(t['cx'],my),(t['cx'],t['y']))
        else:
            dip=s['y']+NH+40
            pts=bez((s['cx'],s['y']+NH),(s['cx'],dip),(t['cx'],dip),(t['cx'],t['y']+NH))
        for i in range(len(pts)-1):
            dr.line([(S(pts[i][0]),S(pts[i][1])),(S(pts[i+1][0]),S(pts[i+1][1]))],fill=col,width=2)
        (x1,y1),(x2,y2)=pts[-2],pts[-1]
        a=math.atan2(y2-y1,x2-x1)
        dr.polygon([(S(x2),S(y2)),(S(x2-9*math.cos(a-.45)),S(y2-9*math.sin(a-.45))),(S(x2-9*math.cos(a+.45)),S(y2-9*math.sin(a+.45)))],fill=col)
    # cards
    for n in nodes:
        col,ico,_=OUT[outlook(n)];foc=n.get('focal')
        dr.rounded_rectangle([S(n['x']),S(n['y']),S(n['x']+NW),S(n['y']+NH)],radius=12,fill=(35,26,18) if foc else (20,29,58),outline=col,width=3 if foc else 2)
        dr.rectangle([S(n['x']),S(n['y']+6),S(n['x']+5),S(n['y']+NH-6)],fill=col)
        if foc:
            dr.text((S(n['x']+NW-10),S(n['y']-14)),'◆ TESE' if n['id']=='secretor' else '◆ CHAVE',font=F(10*scale,True),fill='#ff8a5c',anchor='ra')
        if n.get('step'):
            dr.ellipse([S(n['x']+2),S(n['y']-24),S(n['x']+26),S(n['y'])],fill=col)
            dr.text((S(n['x']+14),S(n['y']-17)),str(n['step']),font=F(13*scale,True),fill='#0b1020',anchor='ma')
        if n.get('title'):
            dr.text((S(n['x']+16),S(n['y']+12)),n['title'][:26],font=F(14*scale,True),fill='#ffffff')
            for i,ln in enumerate(wrap(n['label'],34)[:2]):
                dr.text((S(n['x']+16),S(n['y']+34+i*14)),ln,font=F(10.5*scale),fill='#8b96b3')
        else:
            for i,ln in enumerate(wrap(n['label'],30)):
                dr.text((S(n['x']+16),S(n['y']+16+i*15)),ln,font=F(12.5*scale),fill='#e5eaf5')
        dr.text((S(n['x']+NW-24),S(n['y']+8)),ico,font=F(13*scale,True),fill=col)
        if n.get('delta') in ('up','down'):
            dr.text((S(n['x']+NW-24),S(n['y']+26)),'▲' if n['delta']=='up' else '▼',font=F(11*scale),fill='#22c55e' if n['delta']=='up' else '#ef4444')
    last_y=max((n['y'] for n in nodes),default=0)+NH+18
    dr.text((S(14),S(min(last_y,H-16))),label,font=F(11*scale),fill='#5f6c8f')
    img.save(out);print('OK',out,img.size)

views={v['id']:v for v in D['meta']['views']}
ex=views['executivo']
ns=[dict(n) for n in D['nodes'] if n['id'] in ex['nodes']]
ids={n['id'] for n in ns}
es=[e for e in D['edges'] if e['from'] in ids and e['to'] in ids]
st=1
for nid in ex['nodes']:
    n=next(x for x in ns if x['id']==nid);n['step']=st;st+=1
render(ns,es,'Vista: A HISTÓRIA EM 8 PASSOS (comece aqui)',os.path.join(HERE,'graph_historia.png'),0.95)
render([dict(n) for n in D['nodes']],D['edges'],'Mapa completo: 39 achados · VÁLIDO/POSSÍVEL/BAIXA/INVÁLIDO · arestas por classe',os.path.join(HERE,'graph_completo.png'),0.6)
