# -*- coding: utf-8 -*-
"""Rumos 06 a 10."""
from copy_base import C, doc

G = 'https://fonts.googleapis.com/css2?family='


# ══════════════════════════════════════════ 06 SUÍÇO
def d06():
    css = r"""
:root{--pa:#fff;--ink:#0B0B0B;--red:#E8341C;--mut:#7A7A7A;--ru:#D8D8D8}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);
  font:400 16px/1.55 'Inter',Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;
  letter-spacing:-.011em}
.w{max-width:1180px;margin:0 auto;padding:0 24px}
.g{display:grid;grid-template-columns:repeat(12,1fr);gap:24px}
h1,h2,h3{font-weight:700;letter-spacing:-.038em;margin:0}
.num{font:700 12px/1 Inter;letter-spacing:0;color:var(--red)}
hr{border:0;border-top:1px solid var(--ink);margin:0}
hr.t{border-top-width:2px}
.sec{padding:52px 0;border-top:1px solid var(--ru)}
.sec.k{border-top:2px solid var(--ink)}
.lbl{font:700 11px/1 Inter;letter-spacing:.08em;text-transform:uppercase}
/* topo */
.tp{border-bottom:2px solid var(--ink)}
.tp .w{display:flex;justify-content:space-between;align-items:baseline;padding:14px 24px;gap:20px;flex-wrap:wrap}
.tp ol{display:flex;gap:22px;list-style:none;margin:0;padding:0;font:700 11px/1 Inter;
  letter-spacing:.06em;text-transform:uppercase;color:#B4B4B4}
.tp .on{color:var(--red)}.tp .ok{color:var(--ink)}
/* hero */
.hero{padding:60px 0 46px}
.hero h1{grid-column:1/9;font-size:clamp(40px,7.4vw,104px);line-height:.94}
.hero h1 em{font-style:normal;color:var(--red)}
.hero .as{grid-column:9/13;align-self:end;border-top:2px solid var(--ink);padding-top:12px}
.hero .as p{margin:0;font-size:15px;color:var(--mut)}
.hero .as .st{display:block;margin-top:14px;font:700 13px/1.35 Inter;color:var(--ink)}
.play{margin:0;aspect-ratio:16/9;background:var(--ink);position:relative}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:26px solid #fff;border-top:17px solid transparent;border-bottom:17px solid transparent}
/* equacoes */
.eq{display:grid;grid-template-columns:repeat(12,1fr);gap:24px;padding:22px 0;border-top:1px solid var(--ru);
  align-items:baseline}
.eq .n{grid-column:1/2;font:700 11px/1.6 Inter;color:var(--mut)}
.eq .a{grid-column:2/7;font-size:clamp(18px,2.2vw,26px);font-weight:700;letter-spacing:-.03em}
.eq .b{grid-column:7/13;font-size:16px;color:var(--mut)}
.eq.win{background:var(--red);color:#fff;margin:0 -14px;padding:22px 14px;border-top-color:var(--red)}
.eq.win .n,.eq.win .b{color:#fff}
.para{grid-column:2/9;margin:30px 0 0;font-size:clamp(18px,2vw,23px);line-height:1.42;
  letter-spacing:-.024em;font-weight:500}
.para b{color:var(--red)}
/* preco */
.buy{background:var(--ink);color:#fff;padding:56px 0}
.buy .g{align-items:end}
.buy .l{grid-column:1/7}
.buy .r{grid-column:7/13}
.buy .lbl{color:var(--red)}
.buy h2{font-size:clamp(28px,3.6vw,46px);margin:14px 0 0}
.pz{font-size:clamp(90px,15vw,190px);line-height:.82;font-weight:700;letter-spacing:-.06em;margin:0;
  text-align:right}
.pz sup{font-size:.2em;vertical-align:super;font-weight:500;color:#ffffff8c}
.buy .sm{margin:16px 0 0;font-size:14px;color:#ffffffa6;text-align:right}
.buy .sm.t{font-size:11.5px;color:#ffffff6b;margin-top:5px}
.btn{display:block;width:100%;margin:26px 0 0;background:var(--red);color:#fff;text-decoration:none;
  text-align:center;font:700 16px/1 Inter;letter-spacing:-.01em;padding:24px;border:0;cursor:pointer}
.btn:hover{background:#fff;color:var(--ink)}
.ab{margin:18px 0 0;font-size:13.5px;color:#ffffffa6;max-width:46ch}
/* garantia */
.gar{display:grid;grid-template-columns:repeat(12,1fr);gap:24px;align-items:center}
.gar .n100{grid-column:1/4;font-size:clamp(50px,7vw,92px);font-weight:700;letter-spacing:-.05em;
  line-height:.9;color:var(--red)}
.gar .tx{grid-column:4/10}
.gar h3{font-size:clamp(20px,2.3vw,28px)}
.gar p{margin:8px 0 0;color:var(--mut)}
/* hora */
.hr{display:grid;grid-template-columns:repeat(12,1fr);gap:24px;padding:20px 0;border-top:1px solid var(--ru)}
.hr .m{grid-column:1/3;font:700 clamp(20px,2.4vw,30px)/1 Inter;letter-spacing:-.04em;color:var(--red)}
.hr .c{grid-column:3/11}
.hr h3{font-size:clamp(17px,1.9vw,22px)}
.hr p{margin:7px 0 0;color:var(--mut);font-size:15.5px}
ul.e{list-style:none;padding:0;margin:0}
ul.e li{border-top:1px solid var(--ru);padding:14px 0;font-size:16px}
/* prova */
.pv3{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:2px solid var(--ink)}
.pc{padding:22px 20px;border-right:1px solid var(--ru)}
.pc:last-child{border-right:0}
.pc .n{font-size:18px;font-weight:700;letter-spacing:-.03em;margin:0 0 12px}
.pc .a{margin:0 0 12px;font-size:14.5px;color:var(--mut)}
.pc .d{margin:0;font-size:16px;font-weight:500;line-height:1.42;letter-spacing:-.02em}
.pc a{display:inline-block;margin-top:14px;color:var(--red);font:700 12px/1 Inter;
  letter-spacing:.05em;text-transform:uppercase;text-decoration:none}
.nota{margin:20px 0 0;font-size:14px;color:var(--mut);max-width:62ch}
/* fecho */
.recusa{display:block;width:100%;margin:12px 0 0;background:none;border:0;color:#ffffff8c;
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer}
.esc{margin:22px 0 0;font-size:13.5px;color:#ffffff96;line-height:1.66;max-width:58ch}
details{border-top:1px solid var(--ru)}
summary{cursor:pointer;padding:20px 0;font:700 clamp(17px,2vw,21px)/1.3 Inter;letter-spacing:-.03em;
  list-style:none;display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary:after{content:'+';color:var(--red)}
details[open] summary:after{content:'–'}
details p{margin:0 0 22px;color:var(--mut);max-width:66ch}
footer{border-top:2px solid var(--ink);padding:22px 0;font:700 11px/1 Inter;letter-spacing:.08em;
  text-transform:uppercase}
@media(max-width:860px){.g,.eq,.gar,.hr{grid-template-columns:repeat(6,1fr);gap:14px}
 .hero h1,.eq .a,.eq .b,.para,.buy .l,.buy .r,.gar .n100,.gar .tx,.hr .m,.hr .c{grid-column:1/-1}
 .eq .n{display:none}.pz,.buy .sm{text-align:left}.pv3{grid-template-columns:1fr}
 .pc{border-right:0;border-bottom:1px solid var(--ru)}.tp ol{gap:10px;font-size:9px}}
"""
    b = ('<div class="tp"><div class="w"><span class="lbl">The Book Business</span><ol>' +
         ''.join('<li class="%s">%s/%s</li>' % (
             'ok' if k == 'feito' else ('on' if k == 'agora' else ''), n, t)
             for n, a, t, k in C['passos']) + '</ol></div></div>'
         '<div class="w"><header class="hero g"><h1>' + C['h1a'] + ' <em>' + C['h1b'] + '</em></h1>'
         '<div class="as"><p>' + C['parabens1'] + '</p><span class="st">' + C['parabens2'] + '</span>'
         '<span class="st" style="color:var(--red)">' + C['lead'] + '</span></div></header>'
         '<div class="play"></div>'
         '<section class="sec k"><span class="num">01</span> <span class="lbl">A conta</span>' +
         ''.join('<div class="eq%s"><span class="n">0%d</span><span class="a">%s</span>'
                 '<span class="b">= %s</span></div>' % (' win' if w else '', i + 1, a, bb)
                 for i, (a, bb, w) in enumerate(C['mate'])) +
         '<div class="g"><p class="para"><b>' + C['erro_a'] + '</b> ' + C['erro_b'] + ' <b>' +
         C['erro_c'] + '</b> ' + C['erro_d'] + '</p></div></section></div>'
         '<section class="buy"><div class="w"><div class="g"><div class="l">'
         '<span class="num">02</span> <span class="lbl">' + C['rot'] + '</span>'
         '<h2>' + C['nome'] + '</h2><p class="ab">' + C['abate'] + '</p></div>'
         '<div class="r"><p class="pz"><sup>R$</sup>' + C['preco'] + '</p>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a></div></div></div></section>'
         '<div class="w"><section class="sec"><span class="num">03</span> '
         '<span class="lbl">Garantia</span><div class="gar" style="margin-top:22px">'
         '<div class="n100">100%</div><div class="tx"><h3>' + C['gar_h'] + '</h3>'
         '<p>' + C['gar_p'] + '</p></div></div></section>'
         '<section class="sec"><span class="num">04</span> <span class="lbl">' + C['hora_h'] +
         '</span><div style="margin-top:22px">' + ''.join(
             '<div class="hr"><span class="m">%s</span><div class="c"><h3>%s</h3>%s</div></div>'
             % (m, h, ('<p>' + d + '</p>') if d else '') for m, h, d in C['hora']) + '</div></section>'
         '<section class="sec"><span class="num">05</span> <span class="lbl">Entrega</span>'
         '<div class="g" style="margin-top:22px"><h3 style="grid-column:1/5;font-size:clamp(19px,2.2vw,26px)">' +
         C['entr_h'] + '</h3><ul class="e" style="grid-column:5/13">' +
         ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul></div></section>'
         '<section class="sec"><span class="num">06</span> <span class="lbl">' + C['prova_h'] +
         '</span><div class="pv3" style="margin-top:22px">' + ''.join(
             '<div class="pc"><p class="n">%s</p><p class="a">%s</p><p class="d">%s</p>'
             '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>' % x
             for x in C['provas']) + '</div><p class="nota">' + C['nota_prova'] + '</p></section></div>'
         '<section class="buy"><div class="w"><div class="g"><div class="l">'
         '<span class="num">07</span> <span class="lbl">' + C['recap_h'] + '</span>'
         '<ul class="e" style="margin-top:16px">' +
         ''.join('<li style="border-color:#ffffff2e">%s</li>' % r for r in C['recap']) + '</ul>'
         '<p class="esc">' + C['escassez'] + '</p></div>'
         '<div class="r"><p class="pz"><sup>R$</sup>' + C['preco'] + '</p>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa">' + C['recusa'] + '</button></div></div></div></section>'
         '<div class="w"><section class="sec">' + ''.join(
             '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</section></div><footer><div class="w">' + C['rodape'] + '</div></footer>')
    return doc(css, b, G + 'Inter:wght@400;500;700&display=swap')


# ══════════════════════════════════════════ 07 MARGINALIA
def d07():
    css = r"""
:root{--pa:#F6F2E8;--pg:#FDFBF5;--ink:#221F1A;--pen:#C0392B;--blue:#2C4A7C;--mut:#6E675C;--ru:#DED6C5}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);
  font:400 17px/1.82 'Lora',Georgia,serif;-webkit-font-smoothing:antialiased}
.pen{font-family:'Caveat',cursive;color:var(--pen);line-height:1.25}
.page{max-width:960px;margin:26px auto;background:var(--pg);padding:0;
  box-shadow:0 3px 0 rgba(34,31,26,.05),0 26px 60px -34px rgba(34,31,26,.4);
  border:1px solid var(--ru);position:relative}
.page:before{content:'';position:absolute;left:16.5%;top:0;bottom:0;width:1px;
  background:rgba(192,57,43,.16);pointer-events:none}
.rows{display:grid;grid-template-columns:17% 1fr;gap:0}
.mg{padding:26px 16px 26px 22px;border-right:0;text-align:right}
.mg .pen{font-size:20px;rotate:-3deg;display:block}
.mg .pen.b{rotate:2deg}
.bd{padding:26px 44px 26px 30px}
h1,h2,h3{font-family:'Lora',Georgia,serif;font-weight:600;letter-spacing:-.012em;margin:0}
.hdr{border-bottom:1px solid var(--ru);padding:14px 30px;display:flex;justify-content:space-between;
  gap:14px;flex-wrap:wrap;font:400 11.5px/1 'Lora',serif;letter-spacing:.14em;text-transform:uppercase;
  color:var(--mut)}
.hdr .on{color:var(--pen)}
h1{font-size:clamp(29px,4.2vw,50px);line-height:1.14}
mark{background:none;box-shadow:inset 0 -.5em 0 rgba(192,57,43,.16);padding:0 .06em}
.circ{position:relative;display:inline-block}
.circ:after{content:'';position:absolute;inset:-7px -12px;border:2px solid var(--pen);
  border-radius:52% 48% 46% 54%/58% 42% 56% 44%;opacity:.75;pointer-events:none}
.lead{color:var(--mut);font-size:18px;margin:16px 0 0}
.play{margin:24px 0 0;aspect-ratio:16/9;background:#1D1A16;position:relative;
  box-shadow:6px 6px 0 rgba(192,57,43,.16)}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:24px solid var(--pa);border-top:16px solid transparent;border-bottom:16px solid transparent}
.rule{border:0;border-top:1px solid var(--ru);margin:0}
.kick{font:400 11.5px/1 'Lora',serif;letter-spacing:.2em;text-transform:uppercase;color:var(--pen);margin:0 0 16px}
/* equacoes = trecho anotado */
.eq{padding:16px 0;border-bottom:1px dotted var(--ru);display:flex;gap:12px;flex-wrap:wrap;
  align-items:baseline}
.eq .a{font-size:clamp(18px,2.1vw,23px);font-weight:600}
.eq .s{color:var(--ru)}
.eq .b{color:var(--mut);font-size:16px}
.eq.win .a{color:var(--pen)}
.eq.win .b{color:var(--ink)}
.eq.win{border-bottom:2px solid var(--pen)}
.ann{margin:22px 0 0;padding:16px 20px;border-left:3px solid var(--pen);background:rgba(192,57,43,.045)}
.ann strong{font-weight:600}
/* preco = nota colada */
.buy{margin:0;padding:34px 30px;background:#F1EADA;border-top:1px solid var(--ru);
  border-bottom:1px solid var(--ru);text-align:center;position:relative}
.buy .tape{position:absolute;top:-11px;left:50%;translate:-50%;width:130px;height:22px;
  background:rgba(192,57,43,.14);border:1px dashed rgba(192,57,43,.4);rotate:-1.5deg}
.buy .rot{font-size:15px;color:var(--mut);margin:0}
.buy .nm{font-size:clamp(24px,3vw,34px);margin:8px 0 16px}
.pz{font-size:clamp(56px,9vw,88px);line-height:1;font-weight:600;letter-spacing:-.03em;display:block}
.pz sup{font-size:.26em;vertical-align:super;color:var(--mut)}
.sm{color:var(--mut);font-size:14.5px;margin:12px 0 0}.sm.t{font-size:11.5px;margin-top:5px;opacity:.85}
.btn{display:inline-block;margin:22px 0 0;background:var(--pen);color:#FDFBF5;text-decoration:none;
  font:600 15px/1 'Lora',serif;letter-spacing:.02em;padding:18px 40px;border:0;cursor:pointer;
  box-shadow:4px 4px 0 rgba(34,31,26,.22);transition:.14s}
.btn:hover{translate:-2px -2px;box-shadow:6px 6px 0 rgba(34,31,26,.26)}
.ab{margin:18px auto 0;max-width:46ch;font-size:14px;color:var(--mut)}
.gar{display:grid;grid-template-columns:auto 1fr;gap:20px;align-items:center;
  padding:24px 30px;border-bottom:1px solid var(--ru)}
.gar .s{width:88px;height:88px;border:2px solid var(--pen);border-radius:50%;display:grid;
  place-content:center;text-align:center;color:var(--pen);rotate:-7deg}
.gar .s b{display:block;font-size:23px;font-weight:600;line-height:1}
.gar .s i{font-style:normal;font-family:'Caveat',cursive;font-size:15px}
.gar h3{font-size:20px}.gar p{margin:6px 0 0;color:var(--mut);font-size:15px}
.hl{display:grid;grid-template-columns:76px 1fr;gap:18px;padding:15px 0;border-top:1px dotted var(--ru)}
.hl .m{font-family:'Caveat',cursive;font-size:26px;color:var(--pen);line-height:1.2}
.hl h3{font-size:19px}.hl p{margin:6px 0 0;color:var(--mut);font-size:15.5px}
ul.e{list-style:none;padding:0;margin:14px 0 0}
ul.e li{padding:10px 0 10px 28px;position:relative;border-top:1px dotted var(--ru);font-size:16px}
ul.e li:before{content:'✓';position:absolute;left:2px;font-family:'Caveat',cursive;
  font-size:22px;color:var(--pen)}
.pv{display:grid;gap:18px}
.pc{border:1px solid var(--ru);padding:18px 20px;background:#FBF8F0}
.pc .n{font-size:17px;font-weight:600;margin:0 0 8px}
.pc .a{margin:0 0 8px;font-size:15px;color:var(--mut)}
.pc .d{margin:0;font-size:16.5px}
.pc a{display:inline-block;margin-top:10px;color:var(--pen);font-size:14px}
.nota{margin:16px 0 0;font-size:14px;color:var(--mut)}
.recusa{display:block;margin:14px auto 0;background:none;border:0;color:var(--mut);
  font:400 13.5px 'Lora',serif;text-decoration:underline;cursor:pointer}
.esc{margin:20px auto 0;max-width:54ch;font-size:13.5px;color:var(--mut);line-height:1.7}
details{border-top:1px dotted var(--ru)}
summary{cursor:pointer;padding:16px 0;font-size:18px;font-weight:600;list-style:none}
summary::-webkit-details-marker{display:none}
summary:before{content:'? ';font-family:'Caveat',cursive;color:var(--pen);font-size:22px}
details p{margin:0 0 18px;color:var(--mut);font-size:16px}
footer{padding:22px 30px;text-align:center;font-size:12px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);border-top:1px solid var(--ru)}
@media(max-width:820px){.rows{grid-template-columns:1fr}.page:before{display:none}
 .mg{text-align:left;padding:18px 24px 0}.bd{padding:18px 24px 24px}}
"""

    def row(marg, body):
        return ('<div class="rows"><div class="mg">' + marg + '</div><div class="bd">' + body + '</div></div>')

    b = ('<div class="page"><div class="hdr"><span>The Book Business · caderno do autor</span>'
         '<span class="on">Passo 2 de 3</span></div>' +
         row('<span class="pen">alguém precisa ler isso de fora ↘</span>',
             '<p class="kick">' + C['parabens1'] + ' ' + C['parabens2'] + '</p>'
             '<h1>' + C['h1a'] + ' <mark>' + C['h1b'] + '</mark></h1>'
             '<p class="lead">' + C['lead'] + '</p><div class="play"></div>') +
         '<hr class="rule">' +
         row('<span class="pen">as três contas<br>possíveis</span>'
             '<span class="pen b" style="color:#2C4A7C;font-size:17px;margin-top:14px">'
             'você já resolveu<br>metade ✓</span>',
             ''.join('<div class="eq%s"><span class="a">%s</span><span class="s">=</span>'
                     '<span class="b">%s</span></div>' % (' win' if w else '', a, bb)
                     for a, bb, w in C['mate']) +
             '<p class="ann"><strong>' + C['erro_a'] + '</strong> ' + C['erro_b'] +
             ' <strong class="circ">' + C['erro_c'] + '</strong> ' + C['erro_d'] + '</p>') +
         '<div class="buy"><div class="tape"></div><p class="rot">' + C['rot'] + '</p>'
         '<p class="nm">' + C['nome'] + '</p><span class="pz"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a><p class="ab">' + C['abate'] + '</p></div>'
         '<div class="gar"><div class="s"><b>100%</b><i>de volta</i></div><div>'
         '<h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div></div>' +
         row('<span class="pen">uma hora.<br>sem enrolação.</span>',
             '<p class="kick">' + C['hora_h'] + '</p>' + ''.join(
                 '<div class="hl"><span class="m">%s</span><div><h3>%s</h3>%s</div></div>'
                 % (m, h, ('<p>' + d + '</p>') if d else '') for m, h, d in C['hora']) +
             '<h3 style="margin-top:28px;font-size:20px">' + C['entr_h'] + '</h3>'
             '<ul class="e">' + ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul>') +
         '<hr class="rule">' +
         row('<span class="pen">três livros que<br>alguém leu<br>de fora</span>',
             '<p class="kick">' + C['prova_h'] + '</p><div class="pv">' + ''.join(
                 '<div class="pc"><p class="n">%s</p><p class="a">%s</p><p class="d">%s</p>'
                 '<a href="%s" target="_blank" rel="noopener">ver depoimento →</a></div>' % x
                 for x in C['provas']) + '</div><p class="nota">' + C['nota_prova'] + '</p>') +
         '<div class="buy"><p class="kick" style="margin-bottom:10px">' + C['recap_h'] + '</p>'
         '<ul class="e" style="max-width:420px;margin:0 auto;text-align:left">' +
         ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul>'
         '<span class="pz" style="margin-top:22px"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa">' + C['recusa'] + '</button>'
         '<p class="esc">' + C['escassez'] + '</p></div>' +
         row('<span class="pen">dúvidas<br>honestas</span>',
             ''.join('<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq'])) +
         '<footer>' + C['rodape'] + '</footer></div>')
    return doc(css, b, G + 'Lora:wght@400;600&family=Caveat:wght@500;600&display=swap')


# ══════════════════════════════════════════ 08 NEO-BRUTALISTA
def d08():
    css = r"""
:root{--pa:#F4F0E4;--ink:#11100D;--el:#2B4BF2;--ye:#FFD23F;--pk:#FF5C43;--mut:#5F5B52}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);
  font:500 17px/1.6 'Space Grotesk',ui-sans-serif,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.w{max-width:1060px;margin:0 auto;padding:0 20px}
h1,h2,h3{font-family:'Archivo Black',Impact,sans-serif;font-weight:400;letter-spacing:-.028em;
  margin:0;text-transform:uppercase;line-height:.96}
.bx{border:3px solid var(--ink);background:#fff;box-shadow:7px 7px 0 var(--ink)}
.tag{display:inline-block;border:3px solid var(--ink);background:var(--ye);padding:7px 12px;
  font:700 12px/1 'Space Grotesk';letter-spacing:.06em;text-transform:uppercase;
  box-shadow:3px 3px 0 var(--ink)}
/* topo */
.tp{background:var(--ink);color:var(--pa);padding:11px 0}
.tp ol{display:flex;gap:10px;list-style:none;margin:0;padding:0;flex-wrap:wrap;
  font:700 11px/1 'Space Grotesk';letter-spacing:.05em;text-transform:uppercase}
.tp li{padding:6px 10px;border:2px solid #ffffff2e;border-radius:0}
.tp .ok{background:#ffffff1a;border-color:#ffffff4d}
.tp .on{background:var(--ye);color:var(--ink);border-color:var(--ye)}
/* hero */
.hero{padding:44px 0 34px}
.hero .tag{rotate:-2deg;margin-bottom:22px}
.hero h1{font-size:clamp(36px,7.6vw,88px);line-height:1.16}
.hero h1 u{text-decoration:none;background:var(--ye);box-decoration-break:clone;padding:0 .06em;
  border:3px solid var(--ink)}
.hero .lead{margin:24px 0 0;font-size:19px;font-weight:600;max-width:34ch}
.play{margin:26px 0 0;aspect-ratio:16/9;background:var(--ink);position:relative;
  border:3px solid var(--ink);box-shadow:10px 10px 0 var(--el)}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:30px solid var(--ye);border-top:20px solid transparent;border-bottom:20px solid transparent}
/* equacoes */
.sec{padding:34px 0}
.h2{font-size:clamp(22px,3.2vw,34px);margin-bottom:20px}
.eqs{display:grid;gap:14px}
.eq{border:3px solid var(--ink);background:#fff;padding:18px 20px;display:grid;
  grid-template-columns:1fr auto;gap:14px;align-items:center;box-shadow:5px 5px 0 var(--ink)}
.eq .a{font-family:'Archivo Black',sans-serif;font-size:clamp(16px,2.1vw,22px);text-transform:uppercase;
  letter-spacing:-.02em;line-height:1.1}
.eq .b{font-weight:600;text-align:right;font-size:16px;color:var(--mut);max-width:22ch}
.eq.win{background:var(--el);color:#fff;box-shadow:7px 7px 0 var(--ink)}
.eq.win .b{color:#fff}
.ann{margin:22px 0 0;border:3px solid var(--ink);background:var(--pk);color:#fff;padding:22px;
  box-shadow:7px 7px 0 var(--ink);font-weight:600;font-size:18px;line-height:1.5}
.ann b{background:var(--ink);padding:1px 6px}
/* preco */
.buy{margin:0 0 0;padding:30px;background:var(--ye);text-align:center}
.buy .rot{margin:0;font-weight:700;font-size:15px;text-transform:uppercase;letter-spacing:.06em}
.buy h2{font-size:clamp(26px,4vw,42px);margin:12px 0 18px}
.pz{font-family:'Archivo Black',sans-serif;font-size:clamp(76px,14vw,150px);line-height:.86;
  letter-spacing:-.05em;display:block}
.pz sup{font-size:.24em;vertical-align:super}
.sm{margin:14px 0 0;font-weight:600;font-size:15px}.sm.t{font-size:12px;opacity:.7;margin-top:5px}
.btn{display:block;max-width:520px;margin:24px auto 0;background:var(--ink);color:var(--ye);
  text-decoration:none;font-family:'Archivo Black',sans-serif;font-size:clamp(17px,2.4vw,24px);
  text-transform:uppercase;letter-spacing:-.02em;padding:22px;border:3px solid var(--ink);
  box-shadow:7px 7px 0 var(--pk);cursor:pointer;transition:.12s}
.btn:hover{translate:-3px -3px;box-shadow:10px 10px 0 var(--pk)}
.ab{margin:20px auto 0;max-width:48ch;font-weight:600;font-size:14.5px}
.gar{margin:20px 0 0;padding:22px;display:grid;grid-template-columns:auto 1fr;gap:20px;align-items:center}
.gar .s{width:96px;height:96px;background:var(--el);color:#fff;border:3px solid var(--ink);
  display:grid;place-content:center;text-align:center;rotate:-4deg;box-shadow:4px 4px 0 var(--ink)}
.gar .s b{display:block;font-family:'Archivo Black',sans-serif;font-size:23px;line-height:1}
.gar .s i{font-style:normal;font:700 9px/1 'Space Grotesk';letter-spacing:.1em}
.gar h3{font-size:clamp(17px,2.2vw,23px)}.gar p{margin:8px 0 0;color:var(--mut);font-weight:600;font-size:15px}
/* hora */
.hl{border:3px solid var(--ink);background:#fff;padding:16px 18px;margin-bottom:12px;
  display:grid;grid-template-columns:84px 1fr;gap:16px;box-shadow:4px 4px 0 var(--ink)}
.hl .m{font-family:'Archivo Black',sans-serif;font-size:19px;color:var(--el)}
.hl h3{font-size:17px}.hl p{margin:7px 0 0;color:var(--mut);font-weight:500;font-size:15.5px}
ul.e{list-style:none;padding:0;margin:0;display:grid;gap:10px}
ul.e li{border:3px solid var(--ink);background:#fff;padding:14px 16px;font-weight:600;font-size:16px;
  box-shadow:4px 4px 0 var(--ink)}
/* prova */
.pv3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.pc{border:3px solid var(--ink);background:#fff;padding:18px;box-shadow:5px 5px 0 var(--ink)}
.pc .n{font-family:'Archivo Black',sans-serif;font-size:16px;text-transform:uppercase;margin:0 0 12px}
.pc .a{margin:0 0 10px;font-size:14.5px;color:var(--mut);font-weight:500}
.pc .d{margin:0;font-size:16px;font-weight:600;line-height:1.45}
.pc a{display:inline-block;margin-top:12px;background:var(--ink);color:var(--ye);text-decoration:none;
  font:700 11.5px/1 'Space Grotesk';letter-spacing:.06em;text-transform:uppercase;padding:9px 12px}
.nota{margin:16px 0 0;font-weight:600;font-size:14.5px;color:var(--mut)}
.recusa{display:block;width:100%;margin:14px 0 0;background:none;border:0;color:var(--mut);
  font:600 14px 'Space Grotesk';text-decoration:underline;cursor:pointer}
.esc{margin:20px auto 0;max-width:56ch;font-weight:500;font-size:14px;line-height:1.65}
details{border:3px solid var(--ink);background:#fff;margin-bottom:12px;box-shadow:4px 4px 0 var(--ink)}
summary{cursor:pointer;padding:16px 18px;font-family:'Archivo Black',sans-serif;font-size:16px;
  text-transform:uppercase;list-style:none;display:flex;justify-content:space-between;gap:14px}
summary::-webkit-details-marker{display:none}
summary:after{content:'+';color:var(--el)}
details[open] summary:after{content:'–'}
details p{margin:0 18px 18px;color:var(--mut);font-weight:500;font-size:15.5px}
footer{background:var(--ink);color:var(--pa);padding:22px 0;text-align:center;
  font:700 12px/1 'Space Grotesk';letter-spacing:.16em;text-transform:uppercase}
@media(max-width:840px){.pv3{grid-template-columns:1fr}.eq{grid-template-columns:1fr}
 .eq .b{text-align:left;max-width:none}.gar{grid-template-columns:1fr}}
"""
    b = ('<div class="tp"><div class="w"><ol>' + ''.join(
            '<li class="%s">%s · %s</li>' % ('ok' if k == 'feito' else ('on' if k == 'agora' else ''), a, t)
            for n, a, t, k in C['passos']) + '</ol></div></div>'
         '<div class="w"><header class="hero"><span class="tag">' + C['parabens2'] + '</span>'
         '<h1>' + C['h1a'] + ' <u>' + C['h1b'] + '</u></h1>'
         '<p class="lead">' + C['lead'] + '</p><div class="play"></div></header>'
         '<section class="sec"><h2 class="h2">A conta que decide tudo</h2><div class="eqs">' +
         ''.join('<div class="eq%s"><span class="a">%s</span><span class="b">%s</span></div>'
                 % (' win' if w else '', a, bb) for a, bb, w in C['mate']) +
         '</div><p class="ann"><b>' + C['erro_a'] + '</b> ' + C['erro_b'] + ' <b>' + C['erro_c'] +
         '</b> ' + C['erro_d'] + '</p></section>'
         '<section class="sec"><div class="bx buy"><p class="rot">' + C['rot'] + '</p>'
         '<h2>' + C['nome'] + '</h2><span class="pz"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a><p class="ab">' + C['abate'] + '</p></div>'
         '<div class="bx gar"><div class="s"><b>100%</b><i>DE VOLTA</i></div><div>'
         '<h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div></div></section>'
         '<section class="sec"><h2 class="h2">' + C['hora_h'] + '</h2>' + ''.join(
             '<div class="hl"><span class="m">%s</span><div><h3>%s</h3>%s</div></div>'
             % (m, h, ('<p>' + d + '</p>') if d else '') for m, h, d in C['hora']) +
         '<h3 style="margin:26px 0 14px;font-size:clamp(18px,2.4vw,24px)">' + C['entr_h'] + '</h3>'
         '<ul class="e">' + ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul></section>'
         '<section class="sec"><h2 class="h2">' + C['prova_h'] + '</h2><div class="pv3">' +
         ''.join('<div class="pc"><p class="n">%s</p><p class="a">%s</p><p class="d">%s</p>'
                 '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>' % x
                 for x in C['provas']) +
         '</div><p class="nota">' + C['nota_prova'] + '</p></section>'
         '<section class="sec"><div class="bx buy" style="background:var(--el);color:#fff">'
         '<p class="rot">' + C['recap_h'] + '</p><ul class="e" style="max-width:440px;margin:16px auto 0">' +
         ''.join('<li style="background:#fff;color:var(--ink)">%s</li>' % r for r in C['recap']) + '</ul>'
         '<span class="pz" style="margin-top:22px"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa" style="color:#ffffffc4">' + C['recusa'] + '</button>'
         '<p class="esc">' + C['escassez'] + '</p></div></section>'
         '<section class="sec">' + ''.join(
             '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</section></div><footer>' + C['rodape'] + '</footer>')
    return doc(css, b, G + 'Archivo+Black&family=Space+Grotesk:wght@500;600;700&display=swap')


# ══════════════════════════════════════════ 09 CINEMA
def d09():
    css = r"""
:root{--bg:#0A0A0C;--tx:#F2EFE9;--am:#E9B949;--mut:#8E8A84}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);
  font:400 17px/1.7 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
body:before{content:'';position:fixed;inset:0;z-index:60;pointer-events:none;opacity:.3;
  background-image:radial-gradient(rgba(255,255,255,.07) 1px,transparent 1px);background-size:3px 3px}
.w{max-width:1120px;margin:0 auto;padding:0 26px}
h1,h2,h3{margin:0;font-family:'Anton',Impact,sans-serif;font-weight:400;text-transform:uppercase;
  letter-spacing:-.005em;line-height:.94}
.kick{font:600 10.5px/1 Inter;letter-spacing:.38em;text-transform:uppercase;color:var(--am);margin:0}
/* cena 1 */
.scene{position:relative;min-height:96vh;display:grid;place-content:center;text-align:center;
  padding:90px 26px;overflow:hidden}
.scene:before,.scene:after{content:'';position:absolute;left:0;right:0;height:48px;background:#000;z-index:2}
.scene:before{top:0}.scene:after{bottom:0}
.glow{position:absolute;inset:0;background:
  radial-gradient(58% 46% at 50% 38%,rgba(233,185,73,.2),transparent 62%),
  radial-gradient(70% 60% at 78% 88%,rgba(30,90,120,.28),transparent 66%);z-index:0}
.scene>*{position:relative;z-index:3}
.scene h1{font-size:clamp(38px,7.8vw,104px);line-height:1.08;max-width:15ch}
.scene h1 span{display:block;color:var(--am)}
.scene .sub{margin:30px auto 0;max-width:38ch;color:var(--mut);font-size:17px}
.scene .top{margin:0 0 34px}
.arrow{margin:46px auto 0;width:1px;height:54px;background:linear-gradient(var(--am),transparent)}
.play{max-width:940px;margin:0 auto;aspect-ratio:16/9;background:#08080A;position:relative;
  border:1px solid #ffffff1f;box-shadow:0 40px 120px -50px rgba(233,185,73,.4)}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:28px solid var(--tx);border-top:19px solid transparent;border-bottom:19px solid transparent}
/* cenas seguintes */
.act{padding:clamp(74px,10vw,140px) 0;border-top:1px solid #ffffff14;position:relative}
.act .n{position:absolute;top:26px;right:26px;font:700 11px/1 Inter;letter-spacing:.3em;color:#3C3A37}
.big{font-size:clamp(28px,4.8vw,62px);line-height:1.06;max-width:17ch}
.big em{font-style:normal;color:var(--am)}
.eqs{margin:44px 0 0;display:grid;gap:0}
.eq{padding:26px 0;border-top:1px solid #ffffff14;display:grid;grid-template-columns:1fr auto 1fr;
  gap:20px;align-items:baseline}
.eq .a{font-family:'Anton',sans-serif;text-transform:uppercase;font-size:clamp(17px,2.3vw,27px);
  color:#78746E;letter-spacing:-.01em}
.eq .s{color:#3C3A37}
.eq .b{color:#78746E;font-size:15.5px}
.eq.win .a{color:var(--tx)}.eq.win .b{color:var(--am);font-weight:600;font-size:17px}
.para{margin:44px 0 0;max-width:60ch;font-size:clamp(17px,1.9vw,21px);color:#B4AFA8;line-height:1.62}
.para strong{color:var(--tx);font-weight:600}
/* preco = cartela */
.card{min-height:88vh;display:grid;place-content:center;text-align:center;padding:80px 26px;
  position:relative;overflow:hidden;border-top:1px solid #ffffff14}
.card .glow{background:radial-gradient(52% 46% at 50% 50%,rgba(233,185,73,.17),transparent 64%)}
.card>*{position:relative;z-index:3}
.card h2{font-size:clamp(28px,4.4vw,58px);margin:16px 0 0}
.pz{display:block;font-family:'Anton',sans-serif;font-size:clamp(96px,20vw,240px);line-height:.82;
  letter-spacing:-.045em;margin:30px 0 0}
.pz sup{font-size:.2em;vertical-align:super;color:var(--mut)}
.sm{color:var(--mut);font-size:14.5px;margin:20px 0 0}.sm.t{font-size:11.5px;color:#5F5C57;margin-top:5px}
.btn{display:inline-block;margin:40px 0 0;background:var(--am);color:#100E0A;text-decoration:none;
  font:700 14px/1 Inter;letter-spacing:.14em;text-transform:uppercase;padding:24px 54px;
  border:0;cursor:pointer;transition:.22s}
.btn:hover{background:#fff;transform:translateY(-2px)}
.ab{margin:26px auto 0;max-width:44ch;font-size:13.5px;color:var(--mut)}
.gar{margin:60px auto 0;max-width:560px;border:1px solid #ffffff1f;padding:28px;display:grid;
  grid-template-columns:auto 1fr;gap:22px;align-items:center;text-align:left}
.gar .s{width:92px;height:92px;border:1px solid var(--am);border-radius:50%;display:grid;
  place-content:center;text-align:center;color:var(--am)}
.gar .s b{display:block;font-family:'Anton',sans-serif;font-size:25px;line-height:1}
.gar .s i{font-style:normal;font:600 8.5px/1 Inter;letter-spacing:.16em}
.gar h3{font-size:20px}.gar p{margin:7px 0 0;color:var(--mut);font-size:15px}
/* hora */
.hl{display:grid;grid-template-columns:110px 1fr;gap:28px;padding:24px 0;border-top:1px solid #ffffff14}
.hl .m{font-family:'Anton',sans-serif;font-size:26px;color:var(--am)}
.hl h3{font-size:clamp(17px,2vw,23px)}
.hl p{margin:9px 0 0;color:var(--mut);font-size:15.5px;max-width:56ch}
ul.e{list-style:none;padding:0;margin:22px 0 0}
ul.e li{padding:14px 0;border-top:1px solid #ffffff14;color:var(--mut);font-size:16px}
ul.e b{color:var(--tx);font-weight:600}
/* prova */
.pv3{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:#ffffff14;margin-top:40px}
.pc{background:var(--bg);padding:30px 24px}
.pc .n{font-family:'Anton',sans-serif;text-transform:uppercase;font-size:19px;margin:0 0 16px}
.pc .a{margin:0 0 12px;font-size:14.5px;color:#78746E}
.pc .d{margin:0;font-size:17px;color:#E3DFD8;line-height:1.5}
.pc a{display:inline-block;margin-top:16px;color:var(--am);font:600 11.5px/1 Inter;
  letter-spacing:.16em;text-transform:uppercase;text-decoration:none}
.nota{margin:24px 0 0;font-size:13.5px;color:#5F5C57;max-width:58ch}
.recusa{display:block;margin:22px auto 0;background:none;border:0;color:#5F5C57;
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer}
.esc{margin:30px auto 0;max-width:52ch;font-size:13px;color:#5F5C57;line-height:1.78}
.faq{max-width:700px;margin:0 auto}
details{border-top:1px solid #ffffff14}
summary{cursor:pointer;padding:22px 0;font-family:'Anton',sans-serif;text-transform:uppercase;
  font-size:clamp(16px,2vw,21px);list-style:none}
summary::-webkit-details-marker{display:none}
details p{margin:0 0 24px;color:var(--mut);font-size:15.5px}
footer{border-top:1px solid #ffffff14;padding:34px 0;text-align:center;font:600 10.5px/1 Inter;
  letter-spacing:.34em;text-transform:uppercase;color:#45423E}
@media(max-width:860px){.pv3{grid-template-columns:1fr}.eq{grid-template-columns:1fr;gap:6px}
 .eq .s{display:none}.hl{grid-template-columns:74px 1fr;gap:16px}.hl .m{font-size:20px}}
"""
    b = ('<header class="scene"><div class="glow"></div>'
         '<p class="kick top">' + C['parabens2'] + '</p>'
         '<h1>' + C['h1a'] + '<span>' + C['h1b'] + '</span></h1>'
         '<p class="sub">' + C['lead'] + '</p><div class="arrow"></div></header>'
         '<div class="w" style="margin-top:-40px;position:relative;z-index:4"><div class="play"></div></div>'
         '<section class="act"><div class="w"><span class="n">Cena 01</span>'
         '<p class="kick">A conta</p><h2 class="big" style="margin-top:20px">Só uma das três '
         '<em>muda a sua vida</em>.</h2><div class="eqs">' + ''.join(
             '<div class="eq%s"><span class="a">%s</span><span class="s">=</span>'
             '<span class="b">%s</span></div>' % (' win' if w else '', a, bb)
             for a, bb, w in C['mate']) +
         '</div><p class="para"><strong>' + C['erro_a'] + '</strong> ' + C['erro_b'] + ' <strong>' +
         C['erro_c'] + '</strong> ' + C['erro_d'] + '</p></div></section>'
         '<section class="card"><div class="glow"></div><p class="kick">' + C['rot'] + '</p>'
         '<h2>' + C['nome'] + '</h2><span class="pz"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a><p class="ab">' + C['abate'] + '</p>'
         '<div class="gar"><div class="s"><b>100%</b><i>DE VOLTA</i></div><div>'
         '<h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div></div></section>'
         '<section class="act"><div class="w"><span class="n">Cena 02</span>'
         '<p class="kick">A hora</p><h2 class="big" style="margin-top:20px">' + C['hora_h'] + '</h2>'
         '<div style="margin-top:34px">' + ''.join(
             '<div class="hl"><span class="m">%s</span><div><h3>%s</h3>%s</div></div>'
             % (m, h, ('<p>' + d + '</p>') if d else '') for m, h, d in C['hora']) + '</div>'
         '<h3 style="margin-top:40px;font-size:clamp(19px,2.4vw,27px)">' + C['entr_h'] + '</h3>'
         '<ul class="e">' + ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul></div></section>'
         '<section class="act"><div class="w"><span class="n">Cena 03</span>'
         '<p class="kick">Prova</p><h2 class="big" style="margin-top:20px">' + C['prova_h'] + '</h2>'
         '<div class="pv3">' + ''.join(
             '<div class="pc"><p class="n">%s</p><p class="a">%s</p><p class="d">%s</p>'
             '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>' % x
             for x in C['provas']) + '</div><p class="nota">' + C['nota_prova'] + '</p></div></section>'
         '<section class="card"><div class="glow"></div><p class="kick">' + C['recap_h'] + '</p>'
         '<ul class="e" style="max-width:440px;margin:20px auto 0;text-align:left">' +
         ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul>'
         '<span class="pz"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa">' + C['recusa'] + '</button>'
         '<p class="esc">' + C['escassez'] + '</p></section>'
         '<section class="act"><div class="w"><div class="faq">' + ''.join(
             '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</div></div></section><footer>' + C['rodape'] + '</footer>')
    return doc(css, b, G + 'Inter:wght@400;600;700&family=Anton&display=swap')


# ══════════════════════════════════════════ 10 CARTA
def d10():
    css = r"""
:root{--pa:#fff;--ink:#1B1B19;--lk:#0B5B4F;--mut:#66635D;--ru:#E4E1DA}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);
  font:400 18.5px/1.78 Charter,Georgia,'Times New Roman',serif;-webkit-font-smoothing:antialiased}
.w{max-width:640px;margin:0 auto;padding:0 24px}
h1,h2,h3{font-weight:600;letter-spacing:-.014em;margin:0;font-size:inherit}
p{margin:0 0 22px}
a{color:var(--lk)}
.top{padding:26px 0 0;font-size:13.5px;color:var(--mut)}
.top b{color:var(--ink);font-weight:600}
h1{font-size:clamp(26px,4.4vw,36px);line-height:1.26;margin:30px 0 20px}
.play{margin:0 0 30px;aspect-ratio:16/9;background:#17171A;position:relative}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:22px solid #fff;border-top:15px solid transparent;border-bottom:15px solid transparent}
.eqs{margin:0 0 26px;padding:2px 0}
.eq{padding:9px 0;font-size:17.5px;color:var(--mut)}
.eq b{color:var(--ink);font-weight:600}
.eq.win{color:var(--ink)}
.eq.win b{box-shadow:inset 0 -.42em 0 rgba(11,91,79,.14)}
hr{border:0;border-top:1px solid var(--ru);margin:38px 0}
h2{font-size:20.5px;margin:0 0 16px}
ul{margin:0 0 24px;padding-left:22px}
li{margin:0 0 9px}
.price{margin:0 0 8px;font-size:clamp(28px,5vw,40px);font-weight:600;letter-spacing:-.03em}
.price small{font-size:.48em;font-weight:400;color:var(--mut);letter-spacing:0}
.sm{font-size:14.5px;color:var(--mut);margin:0 0 4px}
.sm.t{font-size:12.5px;margin-bottom:20px}
.btn{display:inline-block;background:var(--lk);color:#fff;text-decoration:none;
  font:600 17px/1 Charter,Georgia,serif;padding:17px 30px;border-radius:4px;border:0;cursor:pointer}
.btn:hover{background:#084A40}
.q{margin:0 0 24px;padding:0 0 0 20px;border-left:2px solid var(--ru)}
.q .n{display:block;font-size:14px;color:var(--mut);margin-bottom:5px}
.q p{margin:0 0 7px;font-size:17px}
.q a{font-size:14.5px}
.recusa{display:block;margin:18px 0 0;background:none;border:0;padding:0;color:var(--mut);
  font:400 15.5px Charter,Georgia,serif;text-decoration:underline;cursor:pointer;text-align:left}
.esc{font-size:15px;color:var(--mut);line-height:1.72}
.sig{margin:34px 0 0;font-size:16.5px;color:var(--mut)}
.sig b{display:block;color:var(--ink);font-weight:600;font-size:18px}
details{margin:0 0 4px}
summary{cursor:pointer;padding:11px 0;font-weight:600;list-style:none}
summary::-webkit-details-marker{display:none}
summary:before{content:'▸ ';color:var(--lk)}
details[open] summary:before{content:'▾ '}
details p{margin:0 0 18px;color:var(--mut);font-size:17px}
footer{padding:34px 0 50px;font-size:13.5px;color:var(--mut);border-top:1px solid var(--ru);margin-top:40px}
"""
    b = ('<div class="w"><p class="top"><b>Passo 2 de 3.</b> ' + C['parabens1'] + ' ' +
         C['parabens2'] + '</p><h1>' + C['h1a'] + '<br>' + C['h1b'] + '</h1>'
         '<p>' + C['lead'] + '</p><div class="play"></div>'
         '<p>Tem uma conta simples por trás disso:</p><div class="eqs">' +
         ''.join('<div class="eq%s"><b>%s</b> = %s</div>' % (' win' if w else '', a, bb)
                 for a, bb, w in C['mate']) + '</div>'
         '<p><b>' + C['erro_a'] + '</b> ' + C['erro_b'] + ' <b>' + C['erro_c'] + '</b> ' +
         C['erro_d'] + '</p><hr>'
         '<h2>' + C['nome'] + '</h2><p>' + C['rot'] + '</p>'
         '<p class="price">R$' + C['preco'] + ' <small>' + C['avista'] + '</small></p>'
         '<p class="sm t">' + C['obs'] + '</p>'
         '<p><a class="btn" href="#">' + C['cta'] + '</a></p>'
         '<p class="sm">' + C['abate'] + '</p>'
         '<p class="sm"><b>100% de volta:</b> ' + C['gar_h'].lower() + '. ' + C['gar_p'] + '</p><hr>'
         '<h2>' + C['hora_h'] + '</h2><ul>' +
         ''.join('<li><b>%s</b> · %s%s</li>' % (m, h, (' ' + d) if d else '') for m, h, d in C['hora']) +
         '</ul><p><b>' + C['entr_h'] + '</b></p><ul>' +
         ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul><hr>'
         '<h2>' + C['prova_h'] + '</h2>' + ''.join(
             '<div class="q"><span class="n">%s</span><p>%s</p><p>%s</p>'
             '<a href="%s" target="_blank" rel="noopener">ver o depoimento</a></div>' % x
             for x in C['provas']) +
         '<p class="sm">' + C['nota_prova'] + '</p><hr>'
         '<h2>' + C['recap_h'] + '</h2><ul>' +
         ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul>'
         '<p class="price">R$' + C['preco'] + ' <small>' + C['avista'] + '</small></p>'
         '<p class="sm t">' + C['obs'] + '</p>'
         '<p><a class="btn" href="#">' + C['cta'] + '</a></p>'
         '<button class="recusa">' + C['recusa'] + '</button>'
         '<p class="esc" style="margin-top:24px">' + C['escassez'] + '</p><hr>' +
         ''.join('<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '<p class="sig">Um abraço,<b>Dany Sakugawa</b></p>'
         '<footer>' + C['rodape'] + '</footer></div>')
    return doc(css, b)
