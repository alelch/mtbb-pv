# -*- coding: utf-8 -*-
# Gera as 3 PVs em ESPANHOL (es/<estagio>.html) a partir das PVs PT geradas (build/generate.py).
# Uso: python3 build/es/build_es.py
# Produto internacional = OUTRA ESTRUTURA: so versao com preco, entregavel so digital (Metodo completo
# 2 anos + Aceleradores/plantillas), US$ 249, checkout placeholder off=REEMPLAZAR, modal internacional
# (lang=es, sem DDD/+55, sem mtbb_pv_origem_set), eventos em mtbb_pv_events_es (tracker roteia por /es/),
# noindex enquanto rascunho. Gate: 0 marcador SO-PT visivel e aninhamento HTML <= ao do PT original.
import re, sys
from pathlib import Path
from html.parser import HTMLParser
sys.path.insert(0, str(Path(__file__).parent))
from dados_es import *
ROOT = Path(__file__).resolve().parents[2]
PT_RE = re.compile(r"(\bvocê\b|\bnão\b|ção\b|ções\b|\btambém\b|\bainda\b|\bentão\b|\bninguém\b|\bnenhum|\bdepois\b|\bmuito\b|\bhoje\b|lançament|\blivro|\bleitor|\bpra\b|\bsem\b|\bcom\b|\bonde\b|\bquando\b|\bisso\b|\besse\b|\bessa\b|\bjá\b|\bsó\b|\bseu\b|\bsua\b|\bseus\b|\bsuas\b|\bé\b|\bsão\b|\bmas\b|\bmais\b)", re.I)

class Bal(HTMLParser):
    VOID = {'br','img','input','meta','link','hr','source','wbr','path','circle','rect','line'}
    def __init__(s): super().__init__(); s.st=[]; s.err=0
    def handle_starttag(s,t,a):
        if t not in s.VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in s.VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        elif t in s.st:
            while s.st and s.st[-1]!=t: s.err+=1; s.st.pop()
            if s.st: s.st.pop()
        else: s.err+=1

def visible(h):
    b = re.sub(r'<style[^>]*>.*?</style>','',h,flags=re.S|re.I)
    b = re.sub(r'<script[^>]*>.*?</script>','',b,flags=re.S|re.I)
    b = re.sub(r'<svg[^>]*>.*?</svg>','',b,flags=re.S|re.I)
    t = re.sub(r'<[^>]+>','\n',b); out=[]; seen=set()
    for l in (x.strip() for x in t.split('\n')):
        if not l or l in seen or re.fullmatch(r'[\W\d]+',l): continue
        seen.add(l); out.append(l)
    return out

def rep(h, old, new, must=True):
    if old not in h:
        if must: raise SystemExit('nao achou: '+old[:70])
        return h
    return h.replace(old, new)

def patch_modal(h, stage):
    h = rep(h, "        variant: 'checkout'\n      };", "        variant: 'checkout',\n        lang: 'es'\n      };")
    h = rep(h, "window.MTBB_TRACK('form_submit', {\n          stage: '"+stage+"', variant: 'checkout',",
               "window.MTBB_TRACK('form_submit', {\n          stage: 'es-"+stage+"', variant: 'checkout',")
    h2 = re.sub(r"      // Atribuição: grava a origem.*?\n      \} catch \(e\) \{\}\n",
                "      // ES: nao grava origem no Supabase (fluxo Natalia/WhatsApp e so do PT)\n", h, count=1, flags=re.S)
    if h2 == h: raise SystemExit('bloco origem_set nao achado')
    h = h2
    h2 = re.sub(r"          // Hotmart separa telefone.*?\n          \} else if \(phd\) \{\n.*?\n          \}\n",
                "          // ES: sem pre-fill de telefone (formato internacional; o checkout em dolar define)\n", h, count=1, flags=re.S)
    if h2 == h: raise SystemExit('bloco phone prefill nao achado')
    h = h2
    h = rep(h, "'sck=' + encodeURIComponent('preco-' + payload.stage)", "'sck=' + encodeURIComponent('es-preco-' + payload.stage)")
    return h

ok = True
for stage, cfg in STAGES.items():
    h = (ROOT / (stage + '.html')).read_text(encoding='utf-8')
    h = rep(h, '<html lang="pt-BR">', '<html lang="es">')
    for a, b in [('src="assets/','src="../assets/'),('href="assets/','href="../assets/'),("url('assets/","url('../assets/"),('srcset="assets/','srcset="../assets/'),('src="tracker.js','src="../tracker.js'),('src="pixel.js','src="../pixel.js'),('src="gtag.js','src="../gtag.js')]:
        h = h.replace(a, b)
    h = rep(h, '<title>'+cfg['title_pt']+'</title>', '<title>'+cfg['title_es']+'</title>')
    h = rep(h, cfg['desc_pt'], cfg['desc_es'])
    h = rep(h, 'content="'+cfg['title_pt']+'"', 'content="'+cfg['title_es']+'"')
    h = rep(h, 'https://metodo.thebookbusiness.com.br/'+stage, 'https://metodo.thebookbusiness.com.br/es/'+stage)
    h = rep(h, 'content="index, follow, max-image-preview:large"', 'content="noindex, nofollow"')
    h = rep(h, 'content="pt_BR"', 'content="es_ES"')
    h = rep(h, 'Método The Book Business — Dany Sakugawa', 'Método The Book Business · Dany Sakugawa')
    h = h.replace('"price":"1500.00"','"price":"249.00"').replace('"priceCurrency":"BRL"','"priceCurrency":"USD"')
    h = rep(h, PRICE_OLD, PRICE_NEW); h = rep(h, STACK_OLD, STACK_NEW); h = rep(h, URG, ''); h = rep(h, GL_OLD, GL_NEW)
    s = h.find('<div class="deliverables-grid">'); e = h.find('<p class="del-closing">')
    if not (s > 0 and e > s): raise SystemExit('grid nao achado')
    h = h[:s] + GRID_NEW + h[e:]
    h = rep(h, 'off=h0n7diwh', 'off=REEMPLAZAR'); h = rep(h, PHONE_OLD, PHONE_NEW); h = rep(h, VZAP_OLD, VZAP_NEW); h = rep(h, MASK_OLD, MASK_NEW)
    for k, v in JSMSG.items(): h = rep(h, k, v, must=False)
    allmap = {**M_SHARED, **STAGE_COMMON, **cfg['M']}
    for k in sorted(allmap, key=len, reverse=True):
        if k in h: h = h.replace(k, allmap[k])
    h = patch_modal(h, stage)
    h = h.replace('Especialista em marketing literário', 'Especialista en marketing literario')
    h = h.replace('Aula gratuita — Método The Book Business', 'Clase gratuita · Método The Book Business')
    h = h.replace('tracker.js?v=12', 'tracker.js?v=13')
    (ROOT / 'es').mkdir(exist_ok=True)
    (ROOT / 'es' / (stage + '.html')).write_text(h, encoding='utf-8')
    vis = visible(h); pt = [l for l in vis if PT_RE.search(l) and not re.search(r'\bcada\b', l, re.I)]
    b = Bal(); b.feed(h); bo = Bal(); bo.feed((ROOT / (stage + '.html')).read_text(encoding='utf-8'))
    checks = {'sem origem_set': 'mtbb_pv_origem_set' not in h, 'sem phoneac': 'phoneac' not in h, "lang:'es'": "lang: 'es'" in h,
              'sck es-preco': "es-preco-" in h, 'tracker v13': 'tracker.js?v=13' in h, 'US$249': 'op-amount">249' in h, 'noindex': 'noindex' in h}
    bad = [k for k, v in checks.items() if not v]
    print('== %s: %d bytes | PT real: %d | tags abertas: %d | aninhamento ES=%d vs PT=%d | checks falhos: %s' % (stage, len(h), len(pt), len(b.st), b.err, bo.err, bad or 'nenhum'))
    for l in pt: print('   PT?', l[:120])
    if pt or b.st or b.err > bo.err or bad: ok = False
sys.exit(0 if ok else 1)
