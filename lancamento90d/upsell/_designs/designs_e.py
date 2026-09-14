# -*- coding: utf-8 -*-
"""
Rumo 12 (Capítulos), escolhido pelo cliente, agora com a PALETA parametrizada.

A estrutura é a mesma em todas as variações (numeral fantasma por capítulo,
faixa em marquise, sublinhado à mão, fita de progresso, linha do tempo
numerada, bloco de oferta cheio, FAQ em cartão). O que muda é só a paleta,
então dá pra julgar cor sem ruído de layout.

Cada paleta define estes papéis, e todos eles TÊM que estar presentes:

  pa    fundo principal            ru    fio/borda
  pa2   fundo alternado            ac    acento em TEXTO (tem que passar contraste)
  alttx texto sobre o alternado    acf   acento em PREENCHIMENTO (tarja, traço)
  ink   tinta                      off*  o bloco da oferta (fundo/texto/cartão/borda)
  mut   texto de apoio             pill* o botão (fundo/texto e o estado hover)
  dim   texto fraco

Regra que não pode ser quebrada: `ac` é cor de texto, `acf` é cor de fundo.
Trocar um pelo outro é como o amarelo vira ilegível.
"""
from copy_base import C, doc

G = 'https://fonts.googleapis.com/css2?family='


def _p(pa, pa2, ink, mut, dim, ru, ac, acf, off, offtx, offc, offb,
       pill, pilltx, pillh, pillhtx, alttx=None, ghost=None,
       play=None, playtx=None, band=None, bandtx=None):
    return dict(pa=pa, pa2=pa2, ink=ink, mut=mut, dim=dim, ru=ru, ac=ac, acf=acf,
                off=off, offtx=offtx, offc=offc, offb=offb, pill=pill, pilltx=pilltx,
                pillh=pillh, pillhtx=pillhtx, alttx=alttx or ink,
                ghost=ghost or 'rgba(11,11,12,.055)',
                play=play or ink, playtx=playtx or pa,
                band=band or ink, bandtx=bandtx or pa)


# ordem = ordem na prancha de paletas
PALETAS = [
 ('a-tinta', 'Tinta', 'Preto e branco puro, como a referência. Zero cor. O controle.',
  _p(pa='#FFFFFF', pa2='#F4F4F5', ink='#0B0B0C', mut='#6B6B70', dim='#9A9AA0', ru='#E4E4E7',
     ac='#0B0B0C', acf='#0B0B0C',
     off='#0B0B0C', offtx='#FFFFFF', offc='#17171A', offb='#2A2A2E',
     pill='#0B0B0C', pilltx='#FFFFFF', pillh='#3A3A40', pillhtx='#FFFFFF')),

 ('b-verde', 'Verde MTBB', 'O que está na prancha 12. Um verde da marca, em dois lugares só.',
  _p(pa='#FFFFFF', pa2='#F4F4F5', ink='#0B0B0C', mut='#6B6B70', dim='#9A9AA0', ru='#E4E4E7',
     ac='#14523E', acf='#1C6B51',
     off='#0B0B0C', offtx='#FFFFFF', offc='#17171A', offb='#2A2A2E',
     pill='#0B0B0C', pilltx='#FFFFFF', pillh='#14523E', pillhtx='#FFFFFF')),

 ('c-marfim', 'Marfim', 'O papel da PV do 90D. Fundo quente, tinta carvão, verde no acento.',
  _p(pa='#F7F4EC', pa2='#EFEADF', ink='#242320', mut='#6B655B', dim='#9C9488', ru='#DFD8C9',
     ac='#14523E', acf='#1C6B51',
     off='#242320', offtx='#F3F0E8', offc='#2E2C28', offb='#403C35',
     pill='#242320', pilltx='#F3F0E8', pillh='#14523E', pillhtx='#F3F0E8',
     ghost='rgba(36,35,32,.06)')),

 ('d-ambar', 'Âmbar', 'O amarelo do MIOLO e do LOMBADA. Ocre no texto, âmbar na tarja.',
  _p(pa='#FFFFFF', pa2='#F6F4EF', ink='#16150F', mut='#6A665B', dim='#9C978A', ru='#E6E2D8',
     ac='#8A6206', acf='#FAAB00',
     off='#16150F', offtx='#FBF8F0', offc='#211F17', offb='#333024',
     pill='#FAAB00', pilltx='#16150F', pillh='#16150F', pillhtx='#FAAB00',
     ghost='rgba(22,21,15,.055)')),

 ('e-laranja', 'Laranja', 'A cor de lançamento da marca. Quente e barulhenta.',
  _p(pa='#FFFFFF', pa2='#F6F3F1', ink='#151211', mut='#6B6461', dim='#9C9490', ru='#E7E2DF',
     ac='#C24A15', acf='#FC783C',
     off='#151211', offtx='#FBF6F3', offc='#201B19', offb='#332B27',
     pill='#FC783C', pilltx='#151211', pillh='#151211', pillhtx='#FC783C',
     ghost='rgba(21,18,17,.055)')),

 ('f-oxblood', 'Oxblood', 'O vermelho fechado que a PV já usa no play. Sério, editorial.',
  _p(pa='#FBF9F6', pa2='#F2EEE9', ink='#191614', mut='#6C645E', dim='#9D958E', ru='#E3DCD4',
     ac='#7D1E14', acf='#9A2A1C',
     off='#191614', offtx='#F6F1EC', offc='#231F1C', offb='#372F2A',
     pill='#7D1E14', pilltx='#FFFFFF', pillh='#191614', pillhtx='#FFFFFF',
     ghost='rgba(25,22,20,.06)')),

 ('g-verde-chapado', 'Verde chapado', 'O fundo alternado deixa de ser cinza e vira verde cheio.',
  _p(pa='#FFFFFF', pa2='#14523E', ink='#0B0B0C', mut='#6B6B70', dim='#9A9AA0', ru='#E4E4E7',
     ac='#14523E', acf='#EAB82D',
     off='#0B0B0C', offtx='#FFFFFF', offc='#17171A', offb='#2A2A2E',
     pill='#0B0B0C', pilltx='#FFFFFF', pillh='#EAB82D', pillhtx='#0B0B0C',
     alttx='#F3F0E8')),

 ('h-noite', 'Noite', 'A página inteira no escuro, e o bloco da oferta inverte pra creme.',
  _p(pa='#101012', pa2='#17171A', ink='#EFEDE8', mut='#9A958D', dim='#6B675F', ru='#27272B',
     ac='#EAB82D', acf='#EAB82D',
     off='#F3F0E8', offtx='#141312', offc='#FFFFFF', offb='#DBD6CA',
     pill='#EAB82D', pilltx='#141312', pillh='#141312', pillhtx='#EAB82D',
     ghost='rgba(239,237,232,.055)',
     play='#000000', playtx='#EFEDE8', band='#EAB82D', bandtx='#141312')),
]

PALETA_PADRAO = PALETAS[1][3]          # o verde, que é o da prancha 12


def d12(paleta=None):
    p = paleta or PALETA_PADRAO
    css = r"""
:root{--pa:%(pa)s;--pa2:%(pa2)s;--ink:%(ink)s;--mut:%(mut)s;--dim:%(dim)s;--ru:%(ru)s;
      --ac:%(ac)s;--acf:%(acf)s;--alttx:%(alttx)s;--ghost:%(ghost)s;
      --off:%(off)s;--offtx:%(offtx)s;--offc:%(offc)s;--offb:%(offb)s;
      --pill:%(pill)s;--pilltx:%(pilltx)s;--pillh:%(pillh)s;--pillhtx:%(pillhtx)s;
      --play:%(play)s;--playtx:%(playtx)s;--band:%(band)s;--bandtx:%(bandtx)s}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);
  font:400 17px/1.62 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.w{max-width:1060px;margin:0 auto;padding:0 28px}
h1,h2,h3{margin:0;font-family:'Instrument Sans',Inter,Helvetica,sans-serif;font-weight:700;
  letter-spacing:-.038em;line-height:1.06;text-wrap:balance}
.eyebrow{font-family:'DM Mono',ui-monospace,monospace;font-size:11px;letter-spacing:.24em;
  text-transform:uppercase;color:var(--dim);margin:0 0 14px}

.prog{position:fixed;top:0;left:0;height:3px;background:var(--ac);width:0;z-index:40}

.tp{border-bottom:1px solid var(--ru);background:var(--pa)}
.tp ol{display:flex;gap:26px;list-style:none;margin:0;padding:13px 0;flex-wrap:wrap;
  font-family:'DM Mono',monospace;font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--dim)}
.tp .ok{color:var(--ink)}.tp .on{color:var(--ac)}

.hero{position:relative;text-align:center;padding:clamp(56px,8vw,104px) 0 clamp(40px,5vw,64px);
  overflow:hidden}
.hero:before{content:'';position:absolute;inset:-30%% -10%% auto;height:150%%;z-index:0;
  background:radial-gradient(46%% 42%% at 50%% 34%%,var(--ghost),transparent 70%%)}
.hero>*{position:relative;z-index:1}
.hero h1{font-size:clamp(34px,6.4vw,78px);max-width:16ch;margin:0 auto}
.hero h1 .u{position:relative;white-space:nowrap}
.hero h1 .u svg{position:absolute;left:-2%%;bottom:-.16em;width:104%%;height:.3em;overflow:visible}
.hero h1 .u path{fill:none;stroke:var(--acf);stroke-width:7;stroke-linecap:round}
.hero .sub{margin:24px auto 0;max-width:46ch;color:var(--mut);font-size:18px}
.pill{display:inline-block;margin:30px 0 0;background:var(--pill);color:var(--pilltx);
  text-decoration:none;font:600 15.5px/1 Inter;padding:18px 34px;border-radius:999px;border:0;
  cursor:pointer;transition:transform .16s,background .16s,color .16s}
.pill:hover,.pill:focus-visible{background:var(--pillh);color:var(--pillhtx);transform:translateY(-1px)}
.cue{margin:clamp(34px,5vw,60px) 0 0;font-family:'DM Mono',monospace;font-size:10.5px;
  letter-spacing:.22em;text-transform:uppercase;color:var(--dim)}
.play{max-width:880px;margin:clamp(30px,4vw,48px) auto 0;aspect-ratio:16/9;background:var(--play);
  border-radius:16px;position:relative;overflow:hidden}
.play:after{content:'';position:absolute;left:50%%;top:50%%;translate:-42%% -50%%;
  border-left:26px solid var(--playtx);border-top:17px solid transparent;
  border-bottom:17px solid transparent}

.mq{background:var(--band);color:var(--bandtx);overflow:hidden;padding:15px 0}
.mq div{display:flex;gap:34px;white-space:nowrap;width:max-content;
  font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.24em;text-transform:uppercase;
  animation:slide 34s linear infinite}
.mq span{opacity:.9}.mq i{font-style:normal;opacity:.42}
@keyframes slide{from{transform:translateX(0)}to{transform:translateX(-50%%)}}
@media (prefers-reduced-motion:reduce){.mq div{animation:none}}

.cap{position:relative;padding:clamp(56px,7.4vw,104px) 0}
.cap.alt{background:var(--pa2);color:var(--alttx)}
.cap.alt .eyebrow,.cap.alt .cue{color:color-mix(in srgb,var(--alttx) 55%%,transparent)}
.cap.alt .tx,.cap.alt .st p{color:color-mix(in srgb,var(--alttx) 74%%,transparent)}
.cap .ghost{position:absolute;right:clamp(10px,4vw,60px);top:clamp(30px,4vw,54px);
  font-family:'Instrument Sans',sans-serif;font-weight:700;font-size:clamp(72px,12vw,150px);
  line-height:.8;letter-spacing:-.06em;color:var(--ghost);pointer-events:none;
  font-variant-numeric:tabular-nums}
.cap.alt .ghost{color:color-mix(in srgb,var(--alttx) 12%%,transparent)}
.cap h2{font-size:clamp(25px,3.6vw,42px);max-width:19ch}
.cap .tx{margin:22px 0 0;max-width:58ch;color:var(--mut);font-size:17.5px}

.eqs{margin:34px 0 0;max-width:760px}
.eq{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:baseline;
  padding:18px 0;border-top:1px solid var(--ru)}
.eq:last-child{border-bottom:1px solid var(--ru)}
.eq .a{font-family:'Instrument Sans',sans-serif;font-weight:700;letter-spacing:-.032em;
  font-size:clamp(16px,2vw,22px);color:var(--mut)}
.eq .s{color:var(--dim)}
.eq .b{font-size:15.5px;color:var(--mut)}
.eq.win .a{color:var(--ink)}
.eq.win .b{color:var(--ac);font-weight:600}
.eq.win{border-top-color:var(--ac)}

.pq{text-align:center;padding:clamp(50px,6.4vw,86px) 0}
.pq .m{font-family:'Instrument Sans',sans-serif;font-weight:700;font-size:44px;
  color:color-mix(in srgb,var(--alttx) 22%%,transparent);line-height:.6;display:block;margin-bottom:20px}
.pq p{margin:0 auto;max-width:22ch;font-family:'Instrument Sans',sans-serif;font-weight:700;
  font-size:clamp(24px,3.8vw,44px);line-height:1.1;letter-spacing:-.038em;text-wrap:balance}
.pq .sm{margin:22px auto 0;max-width:58ch;font-family:Inter,sans-serif;font-weight:400;
  font-size:16.5px;line-height:1.6;letter-spacing:0}

.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:30px 0 0}
.cd{background:var(--pa);border:1px solid var(--ru);border-radius:14px;padding:20px;color:var(--ink)}
.cd .ck{width:26px;height:26px;border-radius:50%%;border:1px solid var(--ru);display:grid;
  place-content:center;color:var(--ac);font-size:13px;margin-bottom:14px}
.cd p{margin:0;font-size:15.5px;line-height:1.5}
.cd p b{font-weight:600}

.tl{margin:32px 0 0;max-width:700px}
.st{display:grid;grid-template-columns:40px 1fr;gap:18px;position:relative;padding-bottom:26px}
.st:last-child{padding-bottom:0}
.st:not(:last-child):before{content:'';position:absolute;left:19px;top:38px;bottom:2px;width:1px;
  background:color-mix(in srgb,var(--alttx) 20%%,transparent)}
.st .no{width:40px;height:40px;border-radius:50%%;
  border:1px solid color-mix(in srgb,var(--alttx) 26%%,transparent);display:grid;place-content:center;
  font-family:'DM Mono',monospace;font-size:11.5px;
  color:color-mix(in srgb,var(--alttx) 70%%,transparent);background:transparent}
.st h3{font-size:18px}
.st .m{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--ac);margin:0 0 5px}
.cap.alt .st .m{color:var(--acf)}
.st p{margin:7px 0 0;color:var(--mut);font-size:15.5px}

.pv{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:30px 0 0}
.pc{background:var(--pa);border:1px solid var(--ru);border-radius:14px;padding:22px;
  display:flex;flex-direction:column;gap:11px;color:var(--ink)}
.pc .n{margin:0;font-family:'Instrument Sans',sans-serif;font-weight:700;font-size:17px;
  letter-spacing:-.03em}
.pc .a{margin:0;font-size:14.5px;color:var(--mut);line-height:1.5}
.pc .d{margin:0;font-size:16px;line-height:1.48}
.pc a{margin-top:auto;padding-top:6px;color:var(--ac);font:600 13px/1 Inter;text-decoration:none;
  align-self:flex-start;border-bottom:1px solid color-mix(in srgb,var(--ac) 34%%,transparent);
  padding-bottom:3px}
.nota{margin:18px 0 0;font-size:14px;color:var(--dim);max-width:62ch}

.offer{background:var(--off);color:var(--offtx);padding:clamp(56px,7vw,96px) 0}
.offer .eyebrow{color:color-mix(in srgb,var(--offtx) 55%%,transparent)}
.offer h2{font-size:clamp(26px,3.8vw,44px);max-width:16ch}
.offer .tx{margin:18px 0 0;max-width:52ch;font-size:17px;
  color:color-mix(in srgb,var(--offtx) 72%%,transparent)}
.obox{margin:34px 0 0;background:var(--offc);border:1px solid var(--offb);border-radius:18px;
  padding:28px;display:grid;grid-template-columns:1fr auto;gap:28px;align-items:end}
.obox .lst{list-style:none;margin:0;padding:0;display:grid;gap:9px}
.obox .lst li{font-size:15.5px;padding-left:22px;position:relative;
  color:color-mix(in srgb,var(--offtx) 80%%,transparent)}
.obox .lst li:before{content:'';position:absolute;left:0;top:8px;width:12px;height:6px;
  border-left:1.6px solid var(--offtx);border-bottom:1.6px solid var(--offtx);rotate:-45deg}
.obox .rt{text-align:right;min-width:240px}
.obox .kk{font-family:'DM Mono',monospace;font-size:10.5px;letter-spacing:.2em;
  text-transform:uppercase;margin:0;color:color-mix(in srgb,var(--offtx) 58%%,transparent)}
.obox .pz{font-family:'Instrument Sans',sans-serif;font-weight:700;font-size:clamp(48px,7vw,80px);
  line-height:.94;letter-spacing:-.05em;margin:8px 0 0;font-variant-numeric:tabular-nums}
.obox .pz sup{font-size:.34em;vertical-align:super;
  color:color-mix(in srgb,var(--offtx) 62%%,transparent)}
.obox .sm{margin:10px 0 0;font-size:13.5px;color:color-mix(in srgb,var(--offtx) 70%%,transparent)}
.obox .sm.t{font-size:11.5px;color:color-mix(in srgb,var(--offtx) 48%%,transparent);margin-top:4px}
.obox .pill{margin-top:18px;display:block;text-align:center}
.ab{margin:18px 0 0;font-size:13.5px;max-width:52ch;
  color:color-mix(in srgb,var(--offtx) 62%%,transparent)}
.gar{margin:22px 0 0;display:grid;grid-template-columns:auto 1fr;gap:18px;align-items:center;
  border-top:1px solid color-mix(in srgb,var(--offtx) 16%%,transparent);padding-top:22px}
.gar .s{width:66px;height:66px;border-radius:50%%;
  border:1px solid color-mix(in srgb,var(--offtx) 30%%,transparent);display:grid;place-content:center;
  text-align:center}
.gar .s b{display:block;font-family:'Instrument Sans',sans-serif;font-weight:700;font-size:17px;
  line-height:1}
.gar .s i{font-style:normal;font-family:'DM Mono',monospace;font-size:7.5px;letter-spacing:.12em;
  color:color-mix(in srgb,var(--offtx) 62%%,transparent)}
.gar h3{font-size:17px}
.gar p{margin:5px 0 0;font-size:14.5px;color:color-mix(in srgb,var(--offtx) 72%%,transparent)}
.recusa{display:block;width:100%%;margin:16px 0 0;background:none;border:0;
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer;
  color:color-mix(in srgb,var(--offtx) 58%%,transparent)}
.esc{margin:18px 0 0;font-size:13.5px;line-height:1.68;max-width:62ch;
  color:color-mix(in srgb,var(--offtx) 62%%,transparent)}

.faq{display:grid;gap:10px;margin:28px 0 0;max-width:760px}
details{background:var(--pa);border:1px solid var(--ru);border-radius:14px;color:var(--ink)}
summary{cursor:pointer;padding:17px 20px;font-weight:600;font-size:16.5px;list-style:none;
  display:flex;justify-content:space-between;gap:16px;align-items:center}
summary::-webkit-details-marker{display:none}
summary:after{content:'+';color:var(--mut);font-size:19px;font-weight:400}
details[open] summary:after{content:'–'}
details p{margin:0 20px 18px;color:var(--mut);font-size:15.5px}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--ac);
  outline-offset:3px}
footer{border-top:1px solid var(--ru);padding:26px 0;text-align:center;
  font-family:'DM Mono',monospace;font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--dim)}
@media(max-width:820px){.pv{grid-template-columns:1fr}
 .obox{grid-template-columns:1fr}.obox .rt{text-align:left;min-width:0}
 .eq{grid-template-columns:1fr;gap:4px}.eq .s{display:none}
 .tp ol{gap:13px;font-size:9px}}
""" % p

    UND = ('<svg viewBox="0 0 200 12" preserveAspectRatio="none" aria-hidden="true">'
           '<path d="M2 8.4C34 3.6 78 2.4 116 4.2c26 1.2 52 3.6 82 1.4"/></svg>')
    mq = ''.join('<span>%s</span><i>·</i>' % s for s in
                 ['Uma hora no Zoom', 'Só sobre o seu livro', 'Plano de ação',
                  'Três frentes de lançamento', 'Gravação sua'] * 2)

    b = (
     '<div class="prog" id="prog"></div>'
     '<div class="tp"><div class="w"><ol>' +
     ''.join('<li class="%s">%s · %s</li>' % (
         'ok' if k == 'feito' else ('on' if k == 'agora' else ''), a, t)
         for n, a, t, k in C['passos']) + '</ol></div></div>'

     '<header class="hero"><div class="w"><p class="eyebrow">' + C['parabens2'] + '</p>'
     '<h1>' + C['h1a'] + ' Mas o seu livro está <span class="u">bom de verdade' + UND +
     '</span>?</h1>'
     '<p class="sub">' + C['lead'] + '</p>'
     '<a class="pill" href="#oferta">' + C['cta2'] + '</a>'
     '<div class="play"></div>'
     '<p class="cue">Role para ver a conta ↓</p></div></header>'

     '<div class="mq"><div>' + mq + '</div></div>'

     '<section class="cap"><div class="w"><span class="ghost">01</span>'
     '<p class="eyebrow">Capítulo um</p><h2>Só uma das três contas muda a sua vida</h2>'
     '<div class="eqs">' + ''.join(
         '<div class="eq%s"><span class="a">%s</span><span class="s">=</span>'
         '<span class="b">%s</span></div>' % (' win' if w else '', a, bb)
         for a, bb, w in C['mate']) + '</div>'
     '<p class="tx">' + C['erro_b'] + '</p></div></section>'

     '<section class="pq cap alt"><div class="w"><span class="m">“</span>'
     '<p>' + C['erro_a'] + '</p>'
     '<p class="sm tx"><b>' + C['erro_c'] + '</b> ' + C['erro_d'] + '</p></div></section>'

     '<section class="cap"><div class="w"><span class="ghost">02</span>'
     '<p class="eyebrow">Capítulo dois</p><h2>' + C['entr_h'] + '</h2>'
     '<div class="cards">' + ''.join(
         '<div class="cd"><span class="ck">✓</span><p>%s</p></div>' % e for e in C['entregas']) +
     '</div></div></section>'

     '<section class="cap alt"><div class="w"><span class="ghost">03</span>'
     '<p class="eyebrow">Capítulo três</p><h2>' + C['hora_h'] + '</h2>'
     '<div class="tl">' + ''.join(
         '<div class="st"><span class="no">%02d</span><div><p class="m">%s</p><h3>%s</h3>%s</div></div>'
         % (i + 1, m, h, ('<p>' + d + '</p>') if d else '')
         for i, (m, h, d) in enumerate(C['hora'])) + '</div></div></section>'

     '<section class="cap"><div class="w"><span class="ghost">04</span>'
     '<p class="eyebrow">Quem já passou</p><h2>' + C['prova_h'] + '</h2>'
     '<div class="pv">' + ''.join(
         '<div class="pc"><p class="n">%s</p><p class="a">%s</p><p class="d">%s</p>'
         '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>' % x
         for x in C['provas']) + '</div>'
     '<p class="nota">' + C['nota_prova'] + '</p></div></section>'

     '<section class="offer" id="oferta"><div class="w">'
     '<p class="eyebrow">A oferta</p><h2>' + C['nome'] + '</h2>'
     '<p class="tx">' + C['rot'] + '</p>'
     '<div class="obox"><ul class="lst">' +
     ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul>'
     '<div class="rt"><p class="kk">Investimento</p>'
     '<p class="pz"><sup>R$</sup>' + C['preco'] + '</p>'
     '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
     '<a class="pill" href="#">' + C['cta'] + '</a>'
     '<button class="recusa">' + C['recusa'] + '</button></div></div>'
     '<p class="ab">' + C['abate'] + '</p>'
     '<div class="gar"><div class="s"><b>100%</b><i>DE VOLTA</i></div>'
     '<div><h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div></div>'
     '<p class="esc">' + C['escassez'] + '</p></div></section>'

     '<section class="cap alt"><div class="w"><p class="eyebrow">Dúvidas</p>'
     '<h2>Perguntas frequentes</h2><div class="faq">' + ''.join(
         '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
     '</div></div></section><footer>' + C['rodape'] + '</footer>'

     '<script>(function(){var p=document.getElementById("prog");'
     'function u(){var h=document.documentElement;'
     'p.style.width=(h.scrollTop/(h.scrollHeight-h.clientHeight)*100)+"%";}'
     'addEventListener("scroll",u,{passive:true});u();})();</script>')

    return doc(css, b, G + 'Inter:wght@400;500;600&family=Instrument+Sans:wght@600;700&'
                          'family=DM+Mono:wght@400;500&display=swap')
