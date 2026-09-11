# -*- coding: utf-8 -*-
"""Rumos 01 a 05."""
from copy_base import C, doc

G = 'https://fonts.googleapis.com/css2?family='


# ══════════════════════════════════════════ 01 EDITORIAL
def d01():
    css = r"""
:root{--pa:#FBF9F3;--ink:#1A1814;--ox:#78231C;--mut:#6E6860;--ru:#DDD6C8}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);
  font:400 17px/1.72 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.w{max-width:1080px;margin:0 auto;padding:0 28px}
.n{max-width:660px}
h1,h2,h3,.pz{font-family:'Playfair Display',Georgia,serif;font-weight:400;letter-spacing:-.01em}
.kick{font:600 11px/1 Inter,sans-serif;letter-spacing:.22em;text-transform:uppercase;
  color:var(--ox);display:flex;align-items:center;gap:14px;margin:0 0 20px}
.kick:after{content:'';flex:1;height:1px;background:var(--ru)}
hr.f{border:0;border-top:1px solid var(--ru);margin:0}
/* topo */
.bar{border-bottom:1px solid var(--ru);background:#fff}
.bar ol{display:flex;gap:34px;list-style:none;margin:0;padding:14px 0;
  font:500 11px/1 Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#A49B8C}
.bar .on{color:var(--ox)}.bar .ok{color:var(--ink)}
.bar b{font-weight:700;margin-right:7px}
.hd{padding:20px 0;text-align:center;font-size:14px;color:var(--mut);border-bottom:1px solid var(--ru)}
.hd i{font-style:normal;color:var(--ink);font-weight:600}
/* hero */
.hero{padding:74px 0 8px;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:end}
.hero h1{font-size:clamp(38px,5.1vw,68px);line-height:1.03;margin:0}
.hero h1 em{font-style:italic;color:var(--ox)}
.hero .side{border-left:1px solid var(--ru);padding-left:32px;padding-bottom:8px}
.hero .side p{margin:0;font-size:19px;line-height:1.6;color:var(--mut)}
.play{margin:46px 0 0;aspect-ratio:16/9;background:#15130F;position:relative;overflow:hidden}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:26px solid var(--pa);border-top:17px solid transparent;border-bottom:17px solid transparent}
/* matematica */
.mate{padding:78px 0}
.eqs{display:grid;gap:0;border-top:1px solid var(--ru)}
.eq{display:grid;grid-template-columns:1fr auto 1fr;gap:22px;align-items:baseline;
  padding:24px 0;border-bottom:1px solid var(--ru)}
.eq .a{font-family:'Playfair Display',serif;font-size:clamp(19px,2.3vw,27px)}
.eq .s{color:var(--ru);font-size:22px}
.eq .b{color:var(--mut);font-size:16px}
.eq.win .a,.eq.win .b{color:var(--ox)}
.eq.win .b{font-weight:600}
.dropc p:first-letter{float:left;font-family:'Playfair Display',serif;font-size:66px;
  line-height:.78;padding:6px 12px 0 0;color:var(--ox)}
.mate .dropc{margin-top:42px;max-width:62ch}
.mate .dropc strong{font-weight:600}
/* preco */
.buy{background:#fff;border-top:1px solid var(--ru);border-bottom:1px solid var(--ru);padding:66px 0}
.card{max-width:520px;margin:0 auto;text-align:center;border:1px solid var(--ink);padding:44px 34px;
  position:relative}
.card:before{content:'';position:absolute;inset:5px;border:1px solid var(--ru);pointer-events:none}
.card .rot{font:500 12px/1.5 Inter;letter-spacing:.13em;text-transform:uppercase;color:var(--mut);margin:0}
.card .nm{font-family:'Playfair Display',serif;font-size:31px;margin:12px 0 20px}
.pz{font-size:72px;line-height:1;display:block}
.pz sup{font-size:22px;vertical-align:super;margin-right:4px;color:var(--mut)}
.sm{font-size:14px;color:var(--mut);margin:12px 0 0}
.sm.tiny{font-size:11.5px;opacity:.8;margin-top:5px}
.btn{display:block;margin:26px auto 0;background:var(--ox);color:#fff;text-decoration:none;
  font:600 15px/1 Inter;letter-spacing:.04em;padding:19px 26px;text-align:center;
  transition:background .2s}
.btn:hover{background:#5D1A14}
.abate{margin:22px auto 0;font-size:14px;color:var(--mut);max-width:44ch}
/* garantia */
.gar{display:grid;grid-template-columns:104px 1fr;gap:26px;align-items:center;
  max-width:660px;margin:70px auto;padding:0}
.seal{width:104px;height:104px;border:1px solid var(--ox);border-radius:50%;display:grid;
  place-content:center;text-align:center;color:var(--ox)}
.seal b{display:block;font-family:'Playfair Display',serif;font-size:27px;line-height:1}
.seal i{font-style:normal;font:600 9px/1 Inter;letter-spacing:.16em}
.gar h3{margin:0 0 6px;font-size:23px}
.gar p{margin:0;color:var(--mut);font-size:16px}
/* hora */
.hora{padding:78px 0;border-top:1px solid var(--ru)}
.hora h2{font-size:clamp(28px,3.4vw,42px);margin:0 0 34px}
.hl{display:grid;grid-template-columns:96px 1fr;gap:28px;padding:24px 0;border-top:1px solid var(--ru)}
.hl .m{font-family:'Playfair Display',serif;font-size:25px;color:var(--ox)}
.hl h3{margin:0;font-size:21px;font-weight:400}
.hl p{margin:8px 0 0;color:var(--mut);font-size:16px;max-width:56ch}
.entr{margin-top:48px;max-width:640px}
.entr h3{font-size:22px;margin:0 0 14px}
.entr ul{list-style:none;padding:0;margin:0}
.entr li{padding:12px 0 12px 26px;border-top:1px solid var(--ru);position:relative;font-size:16px}
.entr li:before{content:'';position:absolute;left:0;top:21px;width:9px;height:1px;background:var(--ox)}
/* prova */
.pv{background:#fff;border-top:1px solid var(--ru);padding:72px 0}
.pv h2{font-size:clamp(26px,3vw,38px);margin:0 0 38px}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:38px}
.col{border-top:2px solid var(--ink);padding-top:18px}
.col .q{font:600 12px/1 Inter;letter-spacing:.14em;text-transform:uppercase;margin:0 0 14px}
.col p{margin:0 0 12px;font-size:15.5px;color:var(--mut)}
.col .dp{font-family:'Playfair Display',serif;font-style:italic;font-size:19px;color:var(--ink);line-height:1.45}
.col a{color:var(--ox);font:600 12px/1 Inter;letter-spacing:.1em;text-transform:uppercase;text-decoration:none;
  border-bottom:1px solid currentColor;padding-bottom:3px}
.nota{margin:34px 0 0;font-size:14px;color:var(--mut);max-width:60ch}
/* fecho */
.end{padding:74px 0}
.recap{max-width:520px;margin:0 auto 40px}
.recap .kick{justify-content:center}.recap .kick:after{display:none}
.recap ul{list-style:none;padding:0;margin:0;text-align:center}
.recap li{padding:11px 0;border-bottom:1px solid var(--ru);font-size:16.5px}
.recusa{display:block;margin:18px auto 0;background:none;border:0;color:var(--mut);
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer}
.esc{max-width:52ch;margin:26px auto 0;text-align:center;font-size:13.5px;color:var(--mut);line-height:1.65}
.faq{max-width:660px;margin:62px auto 0;border-top:1px solid var(--ru)}
.faq details{border-bottom:1px solid var(--ru)}
.faq summary{cursor:pointer;padding:20px 0;font-family:'Playfair Display',serif;font-size:20px;
  list-style:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary:before{content:'+ ';color:var(--ox)}
.faq details[open] summary:before{content:'– '}
.faq p{margin:0 0 22px;color:var(--mut);font-size:16px;max-width:62ch}
footer{border-top:1px solid var(--ru);padding:30px 0;text-align:center;font-size:12px;
  letter-spacing:.14em;text-transform:uppercase;color:#A49B8C}
@media(max-width:860px){.hero{grid-template-columns:1fr;gap:26px}.hero .side{border:0;padding:0}
 .cols{grid-template-columns:1fr;gap:30px}.bar ol{gap:16px;font-size:9.5px;overflow:auto}
 .hl{grid-template-columns:72px 1fr;gap:16px}}
"""
    p = C['provas']
    b = ('<div class="bar"><div class="w"><ol>' +
         ''.join('<li class="%s"><b>%s</b>%s · %s</li>' % (
             'ok' if k == 'feito' else ('on' if k == 'agora' else ''), n, a, t)
             for n, a, t, k in C['passos']) +
         '</ol></div></div>'
         '<div class="hd"><div class="w">' + C['parabens1'] + ' <i>' + C['parabens2'] + '</i></div></div>'
         '<div class="w"><header class="hero"><div><p class="kick">Passo 2 de 3</p>'
         '<h1>' + C['h1a'] + '<br><em>' + C['h1b'] + '</em></h1></div>'
         '<div class="side"><p>' + C['lead'] + '</p></div></header>'
         '<div class="play"></div>'
         '<section class="mate"><div class="eqs">' +
         ''.join('<div class="eq%s"><span class="a">%s</span><span class="s">=</span>'
                 '<span class="b">%s</span></div>' % (' win' if w else '', a, bb)
                 for a, bb, w in C['mate']) +
         '</div><div class="dropc"><p><strong>' + C['erro_a'] + '</strong> ' + C['erro_b'] +
         ' <strong>' + C['erro_c'] + '</strong> ' + C['erro_d'] + '</p></div></section></div>'
         '<section class="buy"><div class="w"><div class="card">'
         '<p class="rot">' + C['rot'] + '</p><p class="nm">' + C['nome'] + '</p>'
         '<span class="pz"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm tiny">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<p class="abate">' + C['abate'] + '</p></div>'
         '<div class="gar"><div class="seal"><b>100%</b><i>DE VOLTA</i></div>'
         '<div><h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div></div></div></section>'
         '<div class="w"><section class="hora"><p class="kick">A hora</p><h2>' + C['hora_h'] + '</h2>' +
         ''.join('<div class="hl"><span class="m">%s</span><div><h3>%s</h3>%s</div></div>' % (
             m, h, ('<p>' + d + '</p>') if d else '') for m, h, d in C['hora']) +
         '<div class="entr"><h3>' + C['entr_h'] + '</h3><ul>' +
         ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul></div></section></div>'
         '<section class="pv"><div class="w"><h2>' + C['prova_h'] + '</h2><div class="cols">' +
         ''.join('<div class="col"><p class="q">%s</p><p>%s</p><p class="dp">%s</p>'
                 '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>' % x for x in p) +
         '</div><p class="nota">' + C['nota_prova'] + '</p></div></section>'
         '<section class="end"><div class="w"><div class="recap"><p class="kick">' + C['recap_h'] + '</p><ul>' +
         ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul></div>'
         '<div class="card"><span class="pz"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm tiny">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa">' + C['recusa'] + '</button></div>'
         '<p class="esc">' + C['escassez'] + '</p>'
         '<div class="faq">' +
         ''.join('<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</div></div></section><footer>' + C['rodape'] + '</footer>')
    return doc(css, b, G + 'Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap')


# ══════════════════════════════════════════ 02 CAPA DE LIVRO
def d02():
    css = r"""
:root{--fo:#0F2A1E;--fo2:#16382796;--cr:#F3EEE1;--go:#C9A227;--mut:#9FB0A6}
*{box-sizing:border-box}
body{margin:0;background:var(--fo);color:var(--cr);
  font:400 17px/1.7 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.w{max-width:900px;margin:0 auto;padding:0 26px}
h1,h2,h3,.big{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500}
/* lombada */
.spine{position:fixed;left:0;top:0;bottom:0;width:58px;background:#0A2016;
  border-right:1px solid rgba(201,162,39,.34);display:grid;place-content:center;z-index:5}
.spine span{writing-mode:vertical-rl;font:600 11px/1 Inter;letter-spacing:.4em;
  text-transform:uppercase;color:var(--go)}
.pg{margin-left:58px}
@media(max-width:760px){.spine{display:none}.pg{margin-left:0}}
/* capa */
.cover{min-height:92vh;display:grid;place-content:center;text-align:center;padding:70px 26px;
  position:relative}
.cover:before{content:'';position:absolute;inset:26px;border:1px solid rgba(201,162,39,.36);
  pointer-events:none}
.cover:after{content:'';position:absolute;inset:33px;border:1px solid rgba(201,162,39,.16);
  pointer-events:none}
.tag{font:600 10.5px/1 Inter;letter-spacing:.34em;text-transform:uppercase;color:var(--go);margin:0 0 30px}
.cover h1{font-size:clamp(40px,6.4vw,82px);line-height:1.02;margin:0;max-width:15ch}
.cover h1 i{font-style:italic}
.rule{width:74px;height:1px;background:var(--go);margin:34px auto}
.cover .sub{margin:0 auto;color:var(--mut);font-size:18px;max-width:40ch}
.autor{margin:46px 0 0;font:600 11px/1 Inter;letter-spacing:.3em;text-transform:uppercase;color:var(--cr)}
.play{max-width:760px;margin:0 auto;aspect-ratio:16/9;background:#081A12;
  border:1px solid rgba(201,162,39,.3);position:relative}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:24px solid var(--go);border-top:16px solid transparent;border-bottom:16px solid transparent}
/* orelha = claro */
.flap{background:var(--cr);color:#15251C;padding:78px 0}
.flap .lbl{font:600 10.5px/1 Inter;letter-spacing:.3em;text-transform:uppercase;color:#8A6B14;margin:0 0 26px}
.flap h2{font-size:clamp(28px,3.8vw,44px);margin:0 0 28px;line-height:1.1}
.eq{display:grid;grid-template-columns:1fr 26px 1fr;gap:14px;align-items:baseline;
  padding:20px 0;border-bottom:1px solid rgba(21,37,28,.16)}
.eq:first-of-type{border-top:1px solid rgba(21,37,28,.16)}
.eq .a{font-family:'Cormorant Garamond',serif;font-size:clamp(20px,2.4vw,28px)}
.eq .s{color:#B6AC93;text-align:center}
.eq .b{font-size:15.5px;color:#4C5C53}
.eq.win{background:rgba(15,42,30,.05)}
.eq.win .a,.eq.win .b{color:#0F2A1E}.eq.win .b{font-weight:600}
.flap .txt{margin:32px 0 0;max-width:62ch;color:#3E4D45}
.flap .txt strong{color:#15251C}
/* etiqueta de preco */
.price{padding:82px 0;text-align:center}
.sticker{width:min(290px,74vw);aspect-ratio:1;margin:0 auto;border-radius:50%;
  background:var(--go);color:#12231A;display:grid;place-content:center;
  box-shadow:0 22px 60px rgba(0,0,0,.4)}
.sticker .k{font:700 10px/1 Inter;letter-spacing:.22em;text-transform:uppercase;opacity:.72}
.sticker .v{font-family:'Cormorant Garamond',serif;font-size:74px;line-height:1;margin:8px 0 2px}
.sticker .v sup{font-size:23px;vertical-align:super}
.sticker .p{font:600 12px/1.4 Inter;opacity:.8}
.price .nm{font-family:'Cormorant Garamond',serif;font-size:32px;margin:30px 0 4px}
.price .rot{color:var(--mut);font-size:15px;margin:0}
.sm{color:var(--mut);font-size:14px;margin:16px 0 0}.sm.t{font-size:11.5px;opacity:.75;margin-top:5px}
.btn{display:inline-block;margin:26px 0 0;background:var(--go);color:#12231A;text-decoration:none;
  font:700 14px/1 Inter;letter-spacing:.06em;padding:20px 42px;border-radius:2px;transition:.2s}
.btn:hover{filter:brightness(1.08);transform:translateY(-1px)}
.abate{margin:22px auto 0;max-width:44ch;font-size:14px;color:var(--mut)}
.gar{max-width:620px;margin:56px auto 0;border:1px solid rgba(201,162,39,.32);padding:26px;
  display:grid;grid-template-columns:auto 1fr;gap:22px;align-items:center;text-align:left}
.gar .s{width:86px;height:86px;border-radius:50%;border:1px solid var(--go);display:grid;
  place-content:center;color:var(--go);text-align:center}
.gar .s b{display:block;font-family:'Cormorant Garamond',serif;font-size:26px;line-height:1}
.gar .s i{font-style:normal;font:600 8.5px/1 Inter;letter-spacing:.16em}
.gar h3{margin:0 0 5px;font-size:21px}.gar p{margin:0;color:var(--mut);font-size:15px}
/* quarta capa */
.back{background:#0A2016;padding:78px 0;border-top:1px solid rgba(201,162,39,.24)}
.back h2{font-size:clamp(26px,3.4vw,38px);margin:0 0 8px}
.back .lbl{font:600 10.5px/1 Inter;letter-spacing:.3em;text-transform:uppercase;color:var(--go);margin:0 0 22px}
.blurbs{display:grid;gap:26px;margin-top:30px}
.bl{border-left:2px solid var(--go);padding-left:22px}
.bl .q{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:22px;line-height:1.4;margin:0 0 10px}
.bl .a{margin:0;color:var(--mut);font-size:14.5px}
.bl .n{font:700 11px/1 Inter;letter-spacing:.16em;text-transform:uppercase;margin:12px 0 0}
.bl a{color:var(--go);font-size:13px;text-decoration:none;border-bottom:1px solid rgba(201,162,39,.4)}
.nota{margin:28px 0 0;color:var(--mut);font-size:14px;max-width:60ch}
/* hora */
.hora{padding:76px 0}
.hora h2{font-size:clamp(26px,3.4vw,40px);margin:0 0 30px}
.hl{display:grid;grid-template-columns:88px 1fr;gap:24px;padding:20px 0;
  border-top:1px solid rgba(243,238,225,.12)}
.hl .m{font-family:'Cormorant Garamond',serif;font-size:24px;color:var(--go)}
.hl h3{margin:0;font-size:20px;font-weight:500}
.hl p{margin:7px 0 0;color:var(--mut);font-size:15.5px;max-width:56ch}
.entr{margin-top:42px;max-width:620px}.entr h3{font-size:21px;margin:0 0 12px}
.entr ul{list-style:none;padding:0;margin:0}
.entr li{padding:11px 0;border-top:1px solid rgba(243,238,225,.12);font-size:15.5px;color:var(--mut)}
.entr b{color:var(--cr)}
/* barcode + fecho */
.bc{display:flex;gap:2px;align-items:flex-end;height:46px;justify-content:center;margin:0 0 14px}
.bc i{display:block;width:2px;background:var(--cr);opacity:.75}
.recap{max-width:500px;margin:0 auto 34px;text-align:center}
.recap ul{list-style:none;padding:0;margin:0}
.recap li{padding:10px 0;border-bottom:1px solid rgba(243,238,225,.12);font-size:16px}
.recusa{display:block;margin:16px auto 0;background:none;border:0;color:var(--mut);
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer}
.esc{max-width:52ch;margin:24px auto 0;font-size:13.5px;color:var(--mut);line-height:1.65;text-align:center}
.faq{max-width:640px;margin:56px auto 0}
.faq details{border-top:1px solid rgba(243,238,225,.14)}
.faq summary{cursor:pointer;padding:18px 0;font-family:'Cormorant Garamond',serif;font-size:21px;list-style:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary:before{content:'+ ';color:var(--go)}
.faq details[open] summary:before{content:'– '}
.faq p{margin:0 0 20px;color:var(--mut);font-size:15.5px}
footer{border-top:1px solid rgba(201,162,39,.24);padding:28px 0;text-align:center;
  font:600 10.5px/1 Inter;letter-spacing:.26em;text-transform:uppercase;color:var(--mut)}
"""
    bars = ''.join('<i style="height:%d%%"></i>' % h for h in
                   [100, 55, 88, 40, 72, 96, 48, 80, 36, 92, 60, 100, 44, 76, 88, 52,
                    96, 40, 68, 100, 56, 84, 44, 92, 72, 48, 100, 60, 88, 36])
    b = ('<div class="spine"><span>Diagnóstico do Autor</span></div><div class="pg">'
         '<header class="cover"><p class="tag">Passo 2 de 3 · ' + C['parabens2'] + '</p>'
         '<h1>' + C['h1a'] + ' <i>' + C['h1b'] + '</i></h1>'
         '<div class="rule"></div><p class="sub">' + C['lead'] + '</p>'
         '<p class="autor">The Book Business</p></header>'
         '<div class="w"><div class="play"></div></div>'
         '<section class="flap"><div class="w"><p class="lbl">A conta que decide tudo</p>' +
         ''.join('<div class="eq%s"><span class="a">%s</span><span class="s">=</span>'
                 '<span class="b">%s</span></div>' % (' win' if w else '', a, bb)
                 for a, bb, w in C['mate']) +
         '<p class="txt"><strong>' + C['erro_a'] + '</strong> ' + C['erro_b'] + ' <strong>' +
         C['erro_c'] + '</strong> ' + C['erro_d'] + '</p></div></section>'
         '<section class="price"><div class="w"><div class="sticker"><span class="k">Só nesta página</span>'
         '<span class="v"><sup>R$</sup>' + C['preco'] + '</span><span class="p">ou 12x no cartão</span></div>'
         '<p class="nm">' + C['nome'] + '</p><p class="rot">' + C['rot'] + '</p>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a><p class="abate">' + C['abate'] + '</p>'
         '<div class="gar"><div class="s"><b>100%</b><i>DE VOLTA</i></div><div>'
         '<h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div></div></div></section>'
         '<div class="w"><section class="hora"><h2>' + C['hora_h'] + '</h2>' +
         ''.join('<div class="hl"><span class="m">%s</span><div><h3>%s</h3>%s</div></div>' % (
             m, h, ('<p>' + d + '</p>') if d else '') for m, h, d in C['hora']) +
         '<div class="entr"><h3>' + C['entr_h'] + '</h3><ul>' +
         ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul></div></section></div>'
         '<section class="back"><div class="w"><p class="lbl">Quarta capa</p>'
         '<h2>' + C['prova_h'] + '</h2><div class="blurbs">' +
         ''.join('<div class="bl"><p class="q">%s</p><p class="a">%s</p><p class="n">%s</p>'
                 '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>'
                 % (dp, an, nm, u) for nm, an, dp, u in C['provas']) +
         '</div><p class="nota">' + C['nota_prova'] + '</p></div></section>'
         '<section class="price"><div class="w"><div class="bc">' + bars + '</div>'
         '<div class="recap"><ul>' + ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul></div>'
         '<span class="v" style="font-family:\'Cormorant Garamond\',serif;font-size:66px">'
         '<sup style="font-size:21px">R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p><br>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa">' + C['recusa'] + '</button>'
         '<p class="esc">' + C['escassez'] + '</p><div class="faq">' +
         ''.join('<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</div></div></section><footer>' + C['rodape'] + '</footer></div>')
    return doc(css, b, G + 'Inter:wght@400;500;600;700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap')


# ══════════════════════════════════════════ 03 FICHA CATALOGRÁFICA
def d03():
    css = r"""
:root{--pa:#EEEAE0;--ink:#131210;--red:#B5241C;--mut:#6B665C;--ru:#C9C2B4}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);
  font:400 15px/1.68 'IBM Plex Mono',ui-monospace,monospace;-webkit-font-smoothing:antialiased;
  background-image:linear-gradient(rgba(19,18,16,.035) 1px,transparent 1px);
  background-size:100% 30px}
.w{max-width:880px;margin:0 auto;padding:0 24px}
.sheet{background:#F7F4EC;border:1px solid var(--ink);margin:26px auto;max-width:880px;
  box-shadow:6px 6px 0 rgba(19,18,16,.1)}
.hd{border-bottom:1px solid var(--ink);padding:12px 22px;display:flex;justify-content:space-between;
  flex-wrap:wrap;gap:10px;font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.hd .r{color:var(--red)}
.pad{padding:32px 22px}
.f{display:grid;grid-template-columns:130px 1fr;gap:0;border-top:1px dashed var(--ru)}
.f:last-of-type{border-bottom:1px dashed var(--ru)}
.f dt{padding:11px 0;font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--mut)}
.f dd{margin:0;padding:11px 0}
h1{font-size:clamp(23px,3.4vw,36px);line-height:1.24;margin:0;font-weight:600;letter-spacing:-.02em}
h1 u{text-decoration:none;box-shadow:inset 0 -.42em 0 rgba(181,36,28,.2)}
.stamp{display:inline-block;border:2px solid var(--red);color:var(--red);padding:8px 14px;
  font:700 12px/1 'IBM Plex Mono',monospace;letter-spacing:.2em;text-transform:uppercase;
  rotate:-4deg;opacity:.9}
.play{margin:26px 0 0;aspect-ratio:16/9;background:var(--ink);position:relative;border:1px solid var(--ink)}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:22px solid var(--pa);border-top:15px solid transparent;border-bottom:15px solid transparent}
.play:before{content:'[ REPRODUZIR ]';position:absolute;left:16px;bottom:12px;color:#fff9;
  font-size:10px;letter-spacing:.2em}
h2{font-size:13px;letter-spacing:.22em;text-transform:uppercase;margin:0 0 16px;font-weight:700}
h2:after{content:'';display:block;height:1px;background:var(--ink);margin-top:9px}
table{width:100%;border-collapse:collapse;font-size:14px}
td{padding:13px 10px;border-bottom:1px dashed var(--ru);vertical-align:top}
td.s{width:28px;text-align:center;color:var(--mut)}
td.b{color:var(--mut)}
tr.win td{background:rgba(181,36,28,.06);color:var(--ink);font-weight:600;border-bottom:1px solid var(--red)}
.note{margin:24px 0 0;padding:16px 18px;border-left:3px solid var(--red);background:rgba(181,36,28,.05);
  font-size:14.5px;max-width:70ch}
.note b{background:rgba(181,36,28,.16)}
/* preco = formulario */
.buy{border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);background:#F0ECE2}
.rowf{display:grid;grid-template-columns:150px 1fr;border-bottom:1px dashed var(--ru)}
.rowf:last-child{border:0}
.rowf .k{padding:14px 22px;font-size:11px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--mut);border-right:1px dashed var(--ru)}
.rowf .v{padding:14px 22px}
.big{font-size:46px;font-weight:700;letter-spacing:-.03em;line-height:1}
.big sup{font-size:16px;vertical-align:super;color:var(--mut)}
.btn{display:block;width:100%;background:var(--ink);color:var(--pa);text-decoration:none;
  text-align:center;font:700 14px/1 'IBM Plex Mono',monospace;letter-spacing:.1em;
  text-transform:uppercase;padding:20px;border:0;cursor:pointer}
.btn:hover{background:var(--red)}
.mini{font-size:11.5px;color:var(--mut)}
.gar{display:grid;grid-template-columns:auto 1fr;gap:18px;align-items:center;padding:24px 22px;
  border-top:1px solid var(--ink)}
.gar .s{width:78px;height:78px;border:2px solid var(--red);border-radius:50%;display:grid;
  place-content:center;text-align:center;color:var(--red);rotate:-6deg}
.gar .s b{display:block;font-size:20px;font-weight:700;line-height:1}
.gar .s i{font-style:normal;font-size:8px;letter-spacing:.14em}
.gar h3{margin:0 0 4px;font-size:15px}.gar p{margin:0;color:var(--mut);font-size:13.5px}
.hl{display:grid;grid-template-columns:70px 1fr;gap:16px;padding:14px 0;border-top:1px dashed var(--ru)}
.hl .m{color:var(--red);font-weight:700;font-size:13px}
.hl h3{margin:0;font-size:15px;font-weight:600}
.hl p{margin:6px 0 0;color:var(--mut);font-size:13.5px}
ul.ck{list-style:none;padding:0;margin:14px 0 0}
ul.ck li{padding:9px 0 9px 24px;position:relative;border-top:1px dashed var(--ru);font-size:14px}
ul.ck li:before{content:'▸';position:absolute;left:4px;color:var(--red)}
.pvs{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border:1px solid var(--ink)}
.pvc{padding:18px;border-right:1px dashed var(--ru)}
.pvc:last-child{border-right:0}
.pvc .n{font-weight:700;font-size:13px;letter-spacing:.06em;text-transform:uppercase;margin:0 0 10px}
.pvc p{margin:0 0 9px;font-size:13px;color:var(--mut)}
.pvc .d{color:var(--ink)}
.pvc a{color:var(--red);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase}
.recusa{display:block;width:100%;background:none;border:0;border-top:1px dashed var(--ru);
  padding:15px;color:var(--mut);font:400 12.5px 'IBM Plex Mono',monospace;cursor:pointer;text-decoration:underline}
.esc{padding:18px 22px;font-size:12.5px;color:var(--mut);line-height:1.7;border-top:1px dashed var(--ru)}
details{border-top:1px dashed var(--ru)}
summary{cursor:pointer;padding:14px 0;font-size:14px;font-weight:600;list-style:none}
summary::-webkit-details-marker{display:none}
summary:before{content:'[+] ';color:var(--red)}
details[open] summary:before{content:'[–] '}
details p{margin:0 0 16px;color:var(--mut);font-size:13.5px}
footer{text-align:center;padding:24px;font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--mut)}
@media(max-width:720px){.f,.rowf{grid-template-columns:1fr}.f dt,.rowf .k{padding-bottom:0;border:0}
 .pvs{grid-template-columns:1fr}.pvc{border-right:0;border-bottom:1px dashed var(--ru)}}
"""
    b = ('<div class="sheet"><div class="hd"><span>The Book Business · Ficha do autor</span>'
         '<span class="r">Passo 2/3 · pedido em aberto</span></div>'
         '<div class="pad"><dl class="f"><dt>Situação</dt><dd>' + C['parabens1'] + ' ' +
         C['parabens2'] + '</dd></dl>'
         '<dl class="f"><dt>Assunto</dt><dd><h1>' + C['h1a'] + ' <u>' + C['h1b'] + '</u></h1></dd></dl>'
         '<dl class="f"><dt>Instrução</dt><dd>' + C['lead'] + '</dd></dl>'
         '<div class="play"></div></div>'
         '<div class="pad" style="border-top:1px solid var(--ink)"><h2>Tabela de resultados possíveis</h2>'
         '<table>' + ''.join(
             '<tr class="%s"><td>%s</td><td class="s">=</td><td class="b">%s</td></tr>'
             % ('win' if w else '', a, bb) for a, bb, w in C['mate']) + '</table>'
         '<p class="note"><b>' + C['erro_a'] + '</b> ' + C['erro_b'] + ' <b>' + C['erro_c'] +
         '</b> ' + C['erro_d'] + '</p></div>'
         '<div class="buy"><div class="rowf"><div class="k">Item</div><div class="v">' + C['nome'] +
         '<br><span class="mini">' + C['rot'] + '</span></div></div>'
         '<div class="rowf"><div class="k">Valor</div><div class="v"><span class="big">'
         '<sup>R$</sup>' + C['preco'] + '</span><br><span class="mini">' + C['avista'] + ' · ' +
         C['obs'] + '</span></div></div>'
         '<div class="rowf"><div class="k">Crédito</div><div class="v mini">' + C['abate'] + '</div></div>'
         '<div class="rowf"><div class="k">Vaga</div><div class="v"><span class="stamp">vaga aberta este mês</span></div></div>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<div class="gar"><div class="s"><b>100%</b><i>DE VOLTA</i></div><div><h3>' + C['gar_h'] +
         '</h3><p>' + C['gar_p'] + '</p></div></div></div>'
         '<div class="pad"><h2>' + C['hora_h'] + '</h2>' +
         ''.join('<div class="hl"><span class="m">%s</span><div><h3>%s</h3>%s</div></div>'
                 % (m, h, ('<p>' + d + '</p>') if d else '') for m, h, d in C['hora']) +
         '<h2 style="margin-top:30px">' + C['entr_h'] + '</h2><ul class="ck">' +
         ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul></div>'
         '<div class="pad" style="border-top:1px solid var(--ink)"><h2>' + C['prova_h'] + '</h2>'
         '<div class="pvs">' + ''.join(
             '<div class="pvc"><p class="n">%s</p><p>%s</p><p class="d">%s</p>'
             '<a href="%s" target="_blank" rel="noopener">ver depoimento →</a></div>' % x
             for x in C['provas']) + '</div>'
         '<p class="mini" style="margin-top:16px">' + C['nota_prova'] + '</p></div>'
         '<div class="buy"><div class="rowf"><div class="k">Recapitulando</div><div class="v"><ul class="ck" style="margin:0">' +
         ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul></div></div>'
         '<div class="rowf"><div class="k">Total</div><div class="v"><span class="big">'
         '<sup>R$</sup>' + C['preco'] + '</span> <span class="mini">' + C['avista'] + '</span></div></div>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa">' + C['recusa'] + '</button>'
         '<p class="esc">' + C['escassez'] + '</p></div>'
         '<div class="pad">' + ''.join(
             '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</div></div><footer>' + C['rodape'] + '</footer>')
    return doc(css, b, G + 'IBM+Plex+Mono:wght@400;600;700&display=swap')


# ══════════════════════════════════════════ 04 NOIR PREMIUM
def d04():
    css = r"""
:root{--bg:#09090A;--tx:#EDEAE3;--go:#C6A254;--mut:#8A857C}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);
  font:300 17px/1.8 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.w{max-width:1000px;margin:0 auto;padding:0 30px}
.n{max-width:640px;margin:0 auto}
h1,h2,h3,.pz{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;letter-spacing:-.005em}
.k{font:500 10px/1 Inter;letter-spacing:.42em;text-transform:uppercase;color:var(--go);margin:0}
.hair{width:64px;height:1px;background:var(--go);margin:0 auto;opacity:.8}
.hair.l{margin:0}
section{padding:clamp(80px,11vw,150px) 0}
/* topo */
.top{padding:0;border-bottom:1px solid rgba(237,234,227,.08)}
.top ol{display:flex;gap:40px;justify-content:center;list-style:none;margin:0;padding:20px 0;
  font:400 10px/1 Inter;letter-spacing:.24em;text-transform:uppercase;color:#4E4A44}
.top .on{color:var(--go)}.top .ok{color:var(--mut)}
/* hero */
.hero{text-align:center;padding-top:clamp(70px,9vw,120px)}
.hero .pre{color:var(--mut);font-size:14px;letter-spacing:.06em;margin:0 0 40px}
.hero h1{font-size:clamp(40px,7vw,88px);line-height:1.12;margin:0 auto;max-width:14ch}
.hero h1 span{display:block;color:var(--go);font-style:italic}
.hero .sub{color:var(--mut);font-size:17px;margin:42px auto 0;max-width:36ch}
.play{max-width:820px;margin:64px auto 0;aspect-ratio:16/9;background:#0E0E10;
  border:1px solid rgba(198,162,84,.22);position:relative}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:22px solid rgba(198,162,84,.9);border-top:15px solid transparent;border-bottom:15px solid transparent}
/* equacoes */
.eqs{margin:0 auto;max-width:760px}
.eq{padding:34px 0;border-bottom:1px solid rgba(237,234,227,.08);text-align:center}
.eq:first-child{border-top:1px solid rgba(237,234,227,.08)}
.eq .a{display:block;font-family:'Cormorant Garamond',serif;font-size:clamp(21px,2.7vw,31px);
  color:var(--mut)}
.eq .b{display:block;margin-top:9px;font-size:15px;color:#5E5A54;letter-spacing:.04em}
.eq.win .a{color:var(--tx)}
.eq.win .b{color:var(--go);font-size:17px}
.para{margin:66px auto 0;max-width:56ch;text-align:center;color:var(--mut);font-size:17.5px}
.para strong{color:var(--tx);font-weight:400}
/* preco */
.buy{text-align:center;border-top:1px solid rgba(237,234,227,.08)}
.buy .nm{font-size:clamp(26px,3.4vw,40px);margin:22px 0 0}
.pz{display:block;font-size:clamp(78px,14vw,168px);line-height:.94;margin:34px 0 0;
  font-weight:200;letter-spacing:-.04em}
.pz sup{font-size:.22em;vertical-align:super;color:var(--mut);letter-spacing:0;margin-right:.08em}
.sm{color:var(--mut);font-size:14px;margin:18px 0 0}
.sm.t{font-size:11.5px;color:#56524C;margin-top:6px}
.btn{display:inline-block;margin:44px 0 0;border:1px solid var(--go);color:var(--go);
  text-decoration:none;font:500 11px/1 Inter;letter-spacing:.28em;text-transform:uppercase;
  padding:22px 52px;transition:.3s}
.btn:hover{background:var(--go);color:#09090A}
.abate{margin:30px auto 0;max-width:42ch;font-size:13.5px;color:#5E5A54}
.gar{margin:0 auto;max-width:520px;text-align:center}
.gar .n100{font-family:'Cormorant Garamond',serif;font-size:64px;color:var(--go);line-height:1}
.gar .d{font:500 9px/1 Inter;letter-spacing:.3em;color:var(--mut);margin:6px 0 26px}
.gar h3{font-size:24px;margin:0 0 10px}.gar p{margin:0;color:var(--mut);font-size:15px}
/* hora */
.hora h2{font-size:clamp(28px,4vw,50px);text-align:center;margin:0 0 12px}
.hl{display:grid;grid-template-columns:120px 1fr;gap:34px;padding:30px 0;
  border-top:1px solid rgba(237,234,227,.08);max-width:760px;margin:0 auto}
.hl .m{font-family:'Cormorant Garamond',serif;font-size:27px;color:var(--go);text-align:right}
.hl h3{margin:0;font-size:21px}
.hl p{margin:9px 0 0;color:var(--mut);font-size:15.5px}
.entr{max-width:760px;margin:56px auto 0;text-align:center}
.entr h3{font-size:23px;margin:0 0 22px}
.entr ul{list-style:none;padding:0;margin:0;display:grid;gap:1px;background:rgba(237,234,227,.08)}
.entr li{background:var(--bg);padding:18px;font-size:15px;color:var(--mut)}
.entr b{color:var(--tx);font-weight:400}
/* prova */
.pv h2{font-size:clamp(26px,3.4vw,42px);text-align:center;margin:0 0 54px}
.tri{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(237,234,227,.08)}
.tc{background:var(--bg);padding:32px 26px}
.tc .n{font:500 10px/1 Inter;letter-spacing:.24em;text-transform:uppercase;color:var(--go);margin:0 0 18px}
.tc p{margin:0 0 14px;font-size:14.5px;color:#5E5A54}
.tc .d{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:19px;color:var(--tx);line-height:1.45}
.tc a{color:var(--mut);font:400 11px/1 Inter;letter-spacing:.16em;text-transform:uppercase;text-decoration:none}
.tc a:hover{color:var(--go)}
.nota{text-align:center;margin:40px auto 0;max-width:56ch;font-size:13.5px;color:#56524C}
/* fecho */
.recap{max-width:460px;margin:0 auto 56px;text-align:center}
.recap li{list-style:none;padding:14px 0;border-bottom:1px solid rgba(237,234,227,.08);
  font-size:16px;color:var(--mut)}
.recap ul{padding:0;margin:0}
.recusa{display:block;margin:26px auto 0;background:none;border:0;color:#56524C;
  font:300 13px Inter;text-decoration:underline;cursor:pointer}
.esc{max-width:50ch;margin:34px auto 0;text-align:center;font-size:13px;color:#56524C;line-height:1.8}
.faq{max-width:640px;margin:80px auto 0}
details{border-top:1px solid rgba(237,234,227,.08)}
summary{cursor:pointer;padding:24px 0;font-family:'Cormorant Garamond',serif;font-size:22px;list-style:none}
summary::-webkit-details-marker{display:none}
details p{margin:0 0 26px;color:var(--mut);font-size:15.5px}
footer{border-top:1px solid rgba(237,234,227,.08);padding:36px 0;text-align:center;
  font:400 10px/1 Inter;letter-spacing:.34em;text-transform:uppercase;color:#413E39}
@media(max-width:820px){.tri{grid-template-columns:1fr}.hl{grid-template-columns:80px 1fr;gap:18px}
 .hl .m{text-align:left;font-size:22px}.top ol{gap:16px;font-size:8.5px}}
"""
    b = ('<nav class="top"><ol>' + ''.join(
            '<li class="%s">%s · %s</li>' % ('ok' if k == 'feito' else ('on' if k == 'agora' else ''), a, t)
            for n, a, t, k in C['passos']) + '</ol></nav>'
         '<header class="hero"><div class="w"><p class="pre">' + C['parabens1'] + ' ' +
         C['parabens2'] + '</p><h1>' + C['h1a'] + '<span>' + C['h1b'] + '</span></h1>'
         '<p class="sub">' + C['lead'] + '</p><div class="play"></div></div></header>'
         '<section><div class="w"><div class="eqs">' + ''.join(
             '<div class="eq%s"><span class="a">%s</span><span class="b">%s</span></div>'
             % (' win' if w else '', a, bb) for a, bb, w in C['mate']) +
         '</div><p class="para"><strong>' + C['erro_a'] + '</strong> ' + C['erro_b'] +
         ' <strong>' + C['erro_c'] + '</strong> ' + C['erro_d'] + '</p></div></section>'
         '<section class="buy"><div class="w"><p class="k">' + C['rot'] + '</p>'
         '<p class="nm">' + C['nome'] + '</p><span class="pz"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a><p class="abate">' + C['abate'] + '</p></div></section>'
         '<section><div class="w"><div class="gar"><div class="n100">100%</div>'
         '<div class="d">DE VOLTA</div><h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a></div></div></section>'
         '<section class="hora"><div class="w"><h2>' + C['hora_h'] + '</h2>'
         '<div class="hair" style="margin-bottom:44px"></div>' + ''.join(
             '<div class="hl"><span class="m">%s</span><div><h3>%s</h3>%s</div></div>'
             % (m, h, ('<p>' + d + '</p>') if d else '') for m, h, d in C['hora']) +
         '<div class="entr"><h3>' + C['entr_h'] + '</h3><ul>' +
         ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul></div></div></section>'
         '<section class="pv"><div class="w"><h2>' + C['prova_h'] + '</h2><div class="tri">' +
         ''.join('<div class="tc"><p class="n">%s</p><p>%s</p><p class="d">%s</p>'
                 '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>' % x
                 for x in C['provas']) +
         '</div><p class="nota">' + C['nota_prova'] + '</p></div></section>'
         '<section class="buy"><div class="w"><div class="recap"><p class="k">' + C['recap_h'] +
         '</p><ul style="margin-top:24px">' + ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul></div>'
         '<span class="pz"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa">' + C['recusa'] + '</button>'
         '<p class="esc">' + C['escassez'] + '</p>'
         '<div class="faq">' + ''.join(
             '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</div></div></section><footer>' + C['rodape'] + '</footer>')
    return doc(css, b, G + 'Inter:wght@300;400;500&family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&display=swap')


# ══════════════════════════════════════════ 05 RELATÓRIO CLÍNICO
def d05():
    css = r"""
:root{--bg:#EEF1F4;--cd:#fff;--ink:#0F1B24;--sl:#5B6B7A;--bd:#DCE3E9;
      --ac:#0F5E73;--ok:#12795E;--wr:#C0662B;--bad:#B23A2F}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:400 15.5px/1.65 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.w{max-width:1000px;margin:0 auto;padding:0 22px}
h1,h2,h3{letter-spacing:-.022em;font-weight:650}
.mono{font-family:'IBM Plex Mono',ui-monospace,monospace;font-variant-numeric:tabular-nums}
/* barra de progresso */
.tb{background:var(--ink);color:#fff;position:sticky;top:0;z-index:9}
.tb .w{display:flex;align-items:center;gap:18px;padding:11px 22px;flex-wrap:wrap}
.tb .br{font:700 11px/1 Inter;letter-spacing:.16em;text-transform:uppercase;opacity:.6}
.tb ol{display:flex;gap:8px;list-style:none;margin:0;padding:0;flex:1;min-width:220px}
.tb li{flex:1;font:600 10px/1 Inter;letter-spacing:.06em;text-transform:uppercase;
  padding:7px 9px;border-radius:5px;background:rgba(255,255,255,.08);color:#fff8;white-space:nowrap;
  overflow:hidden;text-overflow:ellipsis}
.tb li.ok{background:rgba(18,121,94,.32);color:#8FD9C1}
.tb li.on{background:#fff;color:var(--ink)}
/* cabeca */
.head{padding:44px 0 30px}
.pill{display:inline-block;font:700 10.5px/1 Inter;letter-spacing:.14em;text-transform:uppercase;
  background:rgba(15,94,115,.1);color:var(--ac);padding:7px 12px;border-radius:99px}
.head h1{font-size:clamp(27px,3.9vw,44px);line-height:1.14;margin:18px 0 0;max-width:19ch}
.head h1 span{color:var(--ac)}
.head .lead{margin:14px 0 0;color:var(--sl);font-size:17px}
.card{background:var(--cd);border:1px solid var(--bd);border-radius:14px;
  box-shadow:0 1px 2px rgba(15,27,36,.04),0 12px 30px -18px rgba(15,27,36,.22)}
.play{margin:24px 0 0;aspect-ratio:16/9;background:var(--ink);border-radius:14px;position:relative;overflow:hidden}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:22px solid #fff;border-top:15px solid transparent;border-bottom:15px solid transparent}
/* matriz 2x2 */
.sec{padding:34px 0}
.ttl{display:flex;align-items:center;gap:10px;margin:0 0 16px}
.ttl h2{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--sl);margin:0;font-weight:700}
.ttl:after{content:'';flex:1;height:1px;background:var(--bd)}
.mtx{padding:22px}
.grid4{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.q{border:1px solid var(--bd);border-radius:11px;padding:18px;min-height:126px;display:flex;
  flex-direction:column;justify-content:space-between}
.q .t{font:700 10.5px/1.4 'IBM Plex Mono',monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--sl)}
.q .r{font-size:17px;font-weight:600;line-height:1.3;margin-top:12px}
.q.bad{border-color:rgba(178,58,47,.3);background:rgba(178,58,47,.045)}
.q.bad .r{color:var(--bad)}
.q.wr{border-color:rgba(192,102,43,.32);background:rgba(192,102,43,.05)}
.q.wr .r{color:var(--wr)}
.q.ok{border-color:var(--ok);background:rgba(18,121,94,.07);box-shadow:0 0 0 3px rgba(18,121,94,.09)}
.q.ok .r{color:var(--ok)}
.q.na{border-style:dashed;opacity:.55}
.st{display:inline-flex;align-items:center;gap:6px;font:700 9.5px/1 Inter;letter-spacing:.1em;
  text-transform:uppercase;padding:5px 9px;border-radius:99px;margin-bottom:10px;align-self:flex-start}
.st.bad{background:rgba(178,58,47,.12);color:var(--bad)}
.st.wr{background:rgba(192,102,43,.13);color:var(--wr)}
.st.ok{background:rgba(18,121,94,.13);color:var(--ok)}
.laudo{margin:14px 0 0;padding:18px 20px;border-left:3px solid var(--ac);background:rgba(15,94,115,.05);
  border-radius:0 10px 10px 0;font-size:15.5px}
.laudo b{font-weight:650}
/* oferta */
.offer{display:grid;grid-template-columns:1.15fr 1fr;gap:0;overflow:hidden}
.ol{padding:30px}
.ol .k{font:700 10.5px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:var(--sl);margin:0 0 8px}
.ol h3{font-size:25px;margin:0 0 18px}
.ol ul{list-style:none;padding:0;margin:0}
.ol li{padding:9px 0 9px 26px;position:relative;font-size:14.6px;color:var(--sl)}
.ol li:before{content:'';position:absolute;left:0;top:14px;width:15px;height:8px;
  border-left:2px solid var(--ok);border-bottom:2px solid var(--ok);rotate:-45deg}
.orr{background:var(--ink);color:#fff;padding:30px;display:flex;flex-direction:column;justify-content:center}
.orr .pv{font:700 10.5px/1 Inter;letter-spacing:.14em;text-transform:uppercase;opacity:.55;margin:0}
.orr .big{font-size:58px;font-weight:700;letter-spacing:-.04em;line-height:1;margin:10px 0 0}
.orr .big sup{font-size:.36em;vertical-align:super;opacity:.6;margin-right:3px}
.orr .sm{margin:10px 0 0;font-size:13.5px;opacity:.7}
.orr .sm.t{font-size:11px;opacity:.45;margin-top:4px}
.btn{display:block;margin:20px 0 0;background:var(--ok);color:#fff;text-decoration:none;text-align:center;
  font:650 15px/1 Inter;padding:17px;border-radius:9px;border:0;cursor:pointer;transition:.18s}
.btn:hover{filter:brightness(1.07)}
.orr .ab{margin:14px 0 0;font-size:12.5px;opacity:.62;line-height:1.55}
/* garantia */
.gar{display:grid;grid-template-columns:auto 1fr auto;gap:20px;align-items:center;padding:20px 24px}
.gar .s{width:62px;height:62px;border-radius:50%;background:rgba(18,121,94,.1);color:var(--ok);
  display:grid;place-content:center;text-align:center}
.gar .s b{display:block;font:700 16px/1 Inter}.gar .s i{font-style:normal;font:700 7.5px/1 Inter;letter-spacing:.1em}
.gar h3{margin:0 0 3px;font-size:16.5px}.gar p{margin:0;color:var(--sl);font-size:14px}
/* agenda */
.tl{padding:8px 22px 22px}
.tr{display:grid;grid-template-columns:64px 1fr;gap:16px;padding:15px 0;border-top:1px solid var(--bd)}
.tr:first-child{border-top:0}
.bar{height:7px;border-radius:99px;background:var(--ac);opacity:.85;margin-top:8px}
.tr .mm{font:700 13px/1 'IBM Plex Mono',monospace;color:var(--ac);padding-top:3px}
.tr h3{margin:0;font-size:16.5px}
.tr p{margin:6px 0 0;color:var(--sl);font-size:14.4px}
/* prova */
.pvs{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.pc{padding:20px}
.pc .n{font-size:15px;font-weight:650;margin:0 0 12px}
.pc .a{margin:0 0 10px;font-size:13.8px;color:var(--sl)}
.pc .d{margin:0;font-size:14.4px;padding:11px 13px;background:rgba(15,94,115,.055);border-radius:9px}
.pc a{display:inline-block;margin-top:12px;color:var(--ac);font:650 12.5px/1 Inter;text-decoration:none}
.nota{margin:14px 0 0;font-size:13px;color:var(--sl)}
/* fecho */
.recusa{display:block;width:100%;margin:12px 0 0;background:none;border:0;color:var(--sl);
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer}
.esc{margin:16px 0 0;padding:16px 20px;background:rgba(192,102,43,.07);border:1px solid rgba(192,102,43,.22);
  border-radius:11px;font-size:13.4px;color:#7A4A1E;line-height:1.62}
details{border-top:1px solid var(--bd)}
summary{cursor:pointer;padding:16px 22px;font-weight:600;font-size:15.5px;list-style:none;
  display:flex;justify-content:space-between;gap:14px}
summary::-webkit-details-marker{display:none}
summary:after{content:'+';color:var(--ac);font-weight:700}
details[open] summary:after{content:'–'}
details p{margin:0 22px 18px;color:var(--sl);font-size:14.5px}
footer{padding:30px 0;text-align:center;font-size:12px;color:var(--sl)}
@media(max-width:840px){.offer{grid-template-columns:1fr}.pvs{grid-template-columns:1fr}
 .grid4{grid-template-columns:1fr}.gar{grid-template-columns:auto 1fr}}
"""
    m = C['mate']
    b = ('<div class="tb"><div class="w"><span class="br">The Book Business</span><ol>' +
         ''.join('<li class="%s">%s · %s</li>' % (
             'ok' if k == 'feito' else ('on' if k == 'agora' else ''), a, t)
             for n, a, t, k in C['passos']) + '</ol></div></div>'
         '<div class="w"><header class="head"><span class="pill">' + C['parabens2'] + '</span>'
         '<h1>' + C['h1a'] + ' <span>' + C['h1b'] + '</span></h1>'
         '<p class="lead">' + C['lead'] + '</p><div class="play"></div></header>'
         '<section class="sec"><div class="ttl"><h2>Matriz de resultado</h2></div>'
         '<div class="card mtx"><div class="grid4">'
         '<div class="q bad"><span class="st bad">Risco</span><div><div class="t">' + m[0][0] +
         '</div><div class="r">' + m[0][1] + '</div></div></div>'
         '<div class="q wr"><span class="st wr">Risco</span><div><div class="t">' + m[1][0] +
         '</div><div class="r">' + m[1][1] + '</div></div></div>'
         '<div class="q ok"><span class="st ok">Alvo</span><div><div class="t">' + m[2][0] +
         '</div><div class="r">' + m[2][1] + '</div></div></div>'
         '<div class="q na"><div class="t">Livro ruim + lançamento ruim</div>'
         '<div class="r" style="font-size:15px;color:#8A97A3">fora de avaliação</div></div>'
         '</div><p class="laudo"><b>' + C['erro_a'] + '</b> ' + C['erro_b'] + ' <b>' + C['erro_c'] +
         '</b> ' + C['erro_d'] + '</p></div></section>'
         '<section class="sec"><div class="ttl"><h2>Recomendação</h2></div>'
         '<div class="card offer"><div class="ol"><p class="k">' + C['rot'] + '</p>'
         '<h3>' + C['nome'] + '</h3><ul>' +
         ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul></div>'
         '<div class="orr"><p class="pv">Valor do procedimento</p>'
         '<p class="big"><sup>R$</sup>' + C['preco'] + '</p>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<p class="ab">' + C['abate'] + '</p></div></div>'
         '<div class="card gar" style="margin-top:14px"><div class="s"><b>100%</b><i>VOLTA</i></div>'
         '<div><h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div>'
         '<a class="btn" style="margin:0;padding:14px 22px" href="#">' + C['cta2'] + '</a></div></section>'
         '<section class="sec"><div class="ttl"><h2>' + C['hora_h'] + '</h2></div>'
         '<div class="card tl">' + ''.join(
             '<div class="tr"><div><div class="mm">%s</div><div class="bar" style="width:%s"></div></div>'
             '<div><h3>%s</h3>%s</div></div>' % (m2, w, h, ('<p>' + d + '</p>') if d else '')
             for (m2, h, d), w in zip(C['hora'], ['16%', '16%', '100%', '30%'])) +
         '</div>'
         '<div class="card" style="margin-top:14px;padding:22px"><h3 style="margin:0 0 12px;font-size:17px">' +
         C['entr_h'] + '</h3><ul class="ol" style="list-style:none;padding:0;margin:0">' +
         ''.join('<li style="padding:8px 0;color:var(--sl);font-size:14.6px">%s</li>' % e
                 for e in C['entregas']) + '</ul></div></section>'
         '<section class="sec"><div class="ttl"><h2>' + C['prova_h'] + '</h2></div>'
         '<div class="pvs">' + ''.join(
             '<div class="card pc"><p class="n">%s</p><p class="a">%s</p><p class="d">%s</p>'
             '<a href="%s" target="_blank" rel="noopener">Ver depoimento →</a></div>' % x
             for x in C['provas']) + '</div><p class="nota">' + C['nota_prova'] + '</p></section>'
         '<section class="sec"><div class="card offer"><div class="ol"><p class="k">' + C['recap_h'] +
         '</p><h3>' + C['nome'] + '</h3><ul>' +
         ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul></div>'
         '<div class="orr"><p class="big"><sup>R$</sup>' + C['preco'] + '</p>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa" style="color:#fff9">' + C['recusa'] + '</button></div></div>'
         '<p class="esc">' + C['escassez'] + '</p>'
         '<div class="card" style="margin-top:16px">' + ''.join(
             '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</div></section><footer>' + C['rodape'] + '</footer></div>')
    return doc(css, b, G + 'Inter:wght@400;500;600;650;700&family=IBM+Plex+Mono:wght@400;700&display=swap')
