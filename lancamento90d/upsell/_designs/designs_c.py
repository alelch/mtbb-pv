# -*- coding: utf-8 -*-
"""
Os dois rumos escolhidos (Suíço e Cinema), agora com passe de acabamento,
mais o cruzamento dos dois.

Por que existem aqui e não em designs_b.py: o 06 e o 09 foram escritos como
um entre dez. Depois de escolhidos ganharam estrutura de verdade (cabeçalho de
seção, índice, ardósia de cena) e viraram outra coisa. As versões originais
continuam em designs_b.py como referência.
"""
from copy_base import C, doc

G = 'https://fonts.googleapis.com/css2?family='

SECOES = [('01', 'A conta'), ('02', 'A oferta'), ('03', 'Garantia'),
          ('04', 'A sua hora'), ('05', 'Entrega'), ('06', 'Prova'), ('07', 'Fecho')]


# ══════════════════════════════════════════ 06 SUÍÇO (acabado)
def d06():
    css = r"""
:root{--pa:#fff;--ink:#0B0B0B;--red:#DC2B14;--mut:#76736E;--ru:#DCDAD5;--ru2:#B9B6B0}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);
  font:400 16.5px/1.54 Inter,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;
  letter-spacing:-.012em}
.w{max-width:1240px;margin:0 auto;padding:0 26px}
.g{display:grid;grid-template-columns:repeat(12,1fr);gap:26px}
h1,h2,h3{font-weight:700;letter-spacing:-.04em;margin:0;text-wrap:balance}
.lbl{font:700 11px/1 Inter;letter-spacing:.1em;text-transform:uppercase}
.num{font:700 11px/1 Inter;letter-spacing:.06em;color:var(--red);font-variant-numeric:tabular-nums}

/* fita de passos */
.tp{border-bottom:1px solid var(--ink)}
.tp .w{display:flex;justify-content:space-between;align-items:center;gap:18px;
  flex-wrap:wrap;padding:13px 26px}
.tp ol{display:flex;gap:20px;list-style:none;margin:0;padding:0;font:700 11px/1 Inter;
  letter-spacing:.08em;text-transform:uppercase;color:var(--ru2)}
.tp .on{color:var(--red)}.tp .ok{color:var(--ink)}

/* indice: as sete seções da página, que é o que a página realmente tem */
.ix{border-bottom:1px solid var(--ru);padding:10px 0}
.ix ol{display:flex;flex-wrap:wrap;gap:0 26px;list-style:none;margin:0;padding:0}
.ix li{font:500 11.5px/1.9 Inter;letter-spacing:.02em;color:var(--mut);
  font-variant-numeric:tabular-nums}
.ix b{color:var(--red);font-weight:700;margin-right:6px}

/* cabeçalho de seção: número + rótulo + fio, sempre igual */
.sh{display:grid;grid-template-columns:46px 1fr;gap:0 14px;align-items:baseline;
  border-top:2px solid var(--ink);padding-top:11px;margin-bottom:30px}
.sh .num{padding-top:2px}
.sh .lbl{display:flex;gap:14px;align-items:center}
.sh .lbl:after{content:'';flex:1;height:1px;background:var(--ru)}
.sec{padding:46px 0}

/* hero */
.hero{padding:52px 0 40px;align-items:end}
.hero h1{grid-column:1/9;font-size:clamp(38px,7vw,96px);line-height:.97}
.hero h1 em{font-style:normal;color:var(--red)}
.hero .fi{grid-column:9/13;border-top:2px solid var(--ink);padding-top:0}
.fr{display:grid;grid-template-columns:74px 1fr;gap:12px;padding:10px 0;
  border-bottom:1px solid var(--ru);align-items:baseline}
.fr dt{font:700 10px/1.5 Inter;letter-spacing:.1em;text-transform:uppercase;color:var(--mut)}
.fr dd{margin:0;font-size:14.5px;line-height:1.42}
.fr dd b{font-weight:700}
.fr.k dd{color:var(--red);font-weight:600}
.play{aspect-ratio:16/9;background:var(--ink);position:relative;margin-bottom:6px}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:26px solid #fff;border-top:17px solid transparent;border-bottom:17px solid transparent}

/* equações */
.eq{display:grid;grid-template-columns:46px 1fr 30px 1fr;gap:0 14px;padding:19px 0;
  border-bottom:1px solid var(--ru);align-items:baseline}
.eq .n{font:700 11px/1.7 Inter;color:var(--ru2);font-variant-numeric:tabular-nums}
.eq .a{font-size:clamp(17px,2.1vw,25px);font-weight:700;letter-spacing:-.035em;line-height:1.14}
.eq .s{color:var(--ru2);text-align:center;font-weight:400}
.eq .b{font-size:16px;color:var(--mut);line-height:1.4}
.eq.win{background:var(--ink);color:#fff;margin:0 -16px;padding:19px 16px;border-bottom-color:var(--ink)}
.eq.win .n{color:var(--red)}
.eq.win .b{color:#fff}
.eq.win .s{color:#ffffff59}
.para{grid-column:1/9;margin:32px 0 0;font-size:clamp(18px,2vw,24px);line-height:1.4;
  letter-spacing:-.028em;font-weight:500}
.para b{color:var(--red);font-weight:700}

/* preço */
.buy{background:var(--ink);color:#fff}
.buy .w{padding-top:46px;padding-bottom:46px}
.buy .g{align-items:end}
.buy .l{grid-column:1/7}
.buy .r{grid-column:8/13}
.buy .sh{border-top-color:#fff;margin-bottom:24px}
.buy .sh .lbl:after{background:#ffffff2e}
.buy h2{font-size:clamp(27px,3.4vw,44px)}
.buy .fr{border-bottom-color:#ffffff26}
.buy .fr dt{color:#ffffff73}
.pz{font-size:clamp(84px,13.5vw,172px);line-height:.8;font-weight:700;letter-spacing:-.062em;
  margin:0;text-align:right;font-variant-numeric:tabular-nums}
.pz sup{font-size:.2em;vertical-align:super;font-weight:500;color:#ffffff8c}
.buy .sm{margin:14px 0 0;font-size:14px;color:#ffffffa6;text-align:right}
.buy .sm.t{font-size:11.5px;color:#ffffff6b;margin-top:5px}
.btn{display:block;width:100%;margin:22px 0 0;background:var(--red);color:#fff;text-decoration:none;
  text-align:center;font:700 16.5px/1 Inter;letter-spacing:-.015em;padding:23px;border:0;cursor:pointer;
  transition:background .15s,color .15s}
.btn:hover,.btn:focus-visible{background:#fff;color:var(--ink)}

/* garantia */
.gar{align-items:center}
.gar .n100{grid-column:1/4;font-size:clamp(54px,7.6vw,104px);font-weight:700;letter-spacing:-.058em;
  line-height:.86;color:var(--red)}
.gar .n100 i{display:block;font-style:normal;font-size:.14em;letter-spacing:.14em;color:var(--ink);
  margin-top:10px}
.gar .tx{grid-column:4/11}
.gar h3{font-size:clamp(21px,2.4vw,30px)}
.gar p{margin:9px 0 0;color:var(--mut)}

/* hora */
.hr{display:grid;grid-template-columns:46px 88px 1fr;gap:0 14px;padding:19px 0;
  border-bottom:1px solid var(--ru)}
.hr .n{font:700 11px/1.9 Inter;color:var(--ru2);font-variant-numeric:tabular-nums}
.hr .m{font:700 clamp(19px,2.2vw,26px)/1.05 Inter;letter-spacing:-.045em;color:var(--red);
  font-variant-numeric:tabular-nums}
.hr h3{font-size:clamp(17px,1.9vw,21px)}
.hr p{margin:7px 0 0;color:var(--mut);font-size:15.5px;max-width:58ch}
ul.e{list-style:none;padding:0;margin:0}
ul.e li{border-bottom:1px solid var(--ru);padding:15px 0;font-size:16px}
ul.e li:first-child{border-top:1px solid var(--ru)}

/* prova */
.pv3{display:grid;grid-template-columns:repeat(3,1fr);gap:0}
.pc{padding:16px 22px 22px 0;border-top:2px solid var(--ink);border-right:1px solid var(--ru);
  display:flex;flex-direction:column;gap:11px}
.pc:last-child{border-right:0}
.pc:not(:first-child){padding-left:22px}
.pc .n{font-size:18.5px;font-weight:700;letter-spacing:-.035em;margin:0}
.pc .a{margin:0;font-size:14.5px;color:var(--mut);line-height:1.45}
.pc .d{margin:0;font-size:16.5px;font-weight:500;line-height:1.4;letter-spacing:-.022em}
.pc a{margin-top:auto;padding-top:8px;color:var(--red);font:700 11.5px/1 Inter;
  letter-spacing:.08em;text-transform:uppercase;text-decoration:none;align-self:flex-start;
  border-bottom:1px solid currentColor;padding-bottom:3px}
.nota{margin:22px 0 0;font-size:14px;color:var(--mut);max-width:64ch}

/* fecho */
.recusa{display:block;width:100%;margin:12px 0 0;background:none;border:0;color:#ffffff8c;
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer;text-align:center}
.esc{margin:22px 0 0;font-size:13.5px;color:#ffffff96;line-height:1.68;max-width:60ch}
details{border-bottom:1px solid var(--ru)}
details:first-of-type{border-top:1px solid var(--ru)}
summary{cursor:pointer;padding:19px 0;font:700 clamp(17px,2vw,21px)/1.3 Inter;letter-spacing:-.035em;
  list-style:none;display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary:after{content:'+';color:var(--red)}
details[open] summary:after{content:'–'}
details p{margin:0 0 22px;color:var(--mut);max-width:68ch}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid var(--red);
  outline-offset:3px}
footer{border-top:2px solid var(--ink);padding:20px 0;font:700 11px/1 Inter;letter-spacing:.1em;
  text-transform:uppercase}
@media(max-width:880px){
 .g{grid-template-columns:repeat(6,1fr);gap:16px}
 .hero h1,.hero .fi,.para,.buy .l,.buy .r,.gar .n100,.gar .tx{grid-column:1/-1}
 .hero .fi{margin-top:26px}
 .eq{grid-template-columns:1fr;gap:5px}.eq .n,.eq .s{display:none}
 .eq.win{margin:0 -12px;padding:19px 12px}
 .hr{grid-template-columns:64px 1fr}.hr .n{display:none}
 .pz,.buy .sm{text-align:left}
 .pv3{grid-template-columns:1fr}
 .pc{border-right:0;padding:16px 0 22px!important}
 .tp ol{gap:11px;font-size:9.5px}.ix{display:none}}
"""

    def sh(n, t, dark=False):
        return ('<div class="sh"><span class="num">%s</span>'
                '<span class="lbl">%s</span></div>' % (n, t))

    b = ('<div class="tp"><div class="w"><span class="lbl">The Book Business</span><ol>' +
         ''.join('<li class="%s">%s · %s</li>' % (
             'ok' if k == 'feito' else ('on' if k == 'agora' else ''), a, t)
             for n, a, t, k in C['passos']) + '</ol></div></div>'
         '<div class="ix"><div class="w"><ol>' +
         ''.join('<li><b>%s</b>%s</li>' % s for s in SECOES) + '</ol></div></div>'
         '<div class="w"><header class="hero g"><h1>' + C['h1a'] + ' <em>' + C['h1b'] + '</em></h1>'
         '<div class="fi">'
         '<dl class="fr"><dt>Situação</dt><dd>' + C['parabens1'] + '</dd></dl>'
         '<dl class="fr"><dt>Pendência</dt><dd><b>' + C['parabens2'] + '</b></dd></dl>'
         '<dl class="fr k"><dt>Agora</dt><dd>' + C['lead'] + '</dd></dl>'
         '</div></header><div class="play"></div>'
         '<section class="sec">' + sh('01', 'A conta') +
         ''.join('<div class="eq%s"><span class="n">%d</span><span class="a">%s</span>'
                 '<span class="s">=</span><span class="b">%s</span></div>'
                 % (' win' if w else '', i + 1, a, bb)
                 for i, (a, bb, w) in enumerate(C['mate'])) +
         '<div class="g"><p class="para"><b>' + C['erro_a'] + '</b> ' + C['erro_b'] + ' <b>' +
         C['erro_c'] + '</b> ' + C['erro_d'] + '</p></div></section></div>'
         '<section class="buy"><div class="w"><div class="g"><div class="l">' +
         sh('02', C['rot']) + '<h2>' + C['nome'] + '</h2>'
         '<dl class="fr" style="margin-top:22px"><dt>Formato</dt><dd>Uma hora no Zoom, '
         'só sobre o seu livro</dd></dl>'
         '<dl class="fr"><dt>Crédito</dt><dd>' + C['abate'] + '</dd></dl></div>'
         '<div class="r"><p class="pz"><sup>R$</sup>' + C['preco'] + '</p>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a></div></div></div></section>'
         '<div class="w"><section class="sec">' + sh('03', 'Garantia') +
         '<div class="g gar"><div class="n100">100%<i>DE VOLTA</i></div>'
         '<div class="tx"><h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div></div></section>'
         '<section class="sec">' + sh('04', C['hora_h']) +
         ''.join('<div class="hr"><span class="n">%d</span><span class="m">%s</span>'
                 '<div><h3>%s</h3>%s</div></div>'
                 % (i + 1, m, h, ('<p>' + d + '</p>') if d else '')
                 for i, (m, h, d) in enumerate(C['hora'])) + '</section>'
         '<section class="sec">' + sh('05', 'Entrega') +
         '<div class="g"><h3 style="grid-column:1/5;font-size:clamp(19px,2.2vw,27px)">' +
         C['entr_h'] + '</h3><ul class="e" style="grid-column:5/13">' +
         ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul></div></section>'
         '<section class="sec">' + sh('06', C['prova_h']) +
         '<div class="pv3">' + ''.join(
             '<div class="pc"><p class="n">%s</p><p class="a">%s</p><p class="d">%s</p>'
             '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>' % x
             for x in C['provas']) + '</div><p class="nota">' + C['nota_prova'] + '</p></section></div>'
         '<section class="buy"><div class="w"><div class="g"><div class="l">' +
         sh('07', C['recap_h']) + '<ul class="e">' +
         ''.join('<li style="border-color:#ffffff26">%s</li>' % r for r in C['recap']) + '</ul>'
         '<p class="esc">' + C['escassez'] + '</p></div>'
         '<div class="r"><p class="pz"><sup>R$</sup>' + C['preco'] + '</p>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa">' + C['recusa'] + '</button></div></div></div></section>'
         '<div class="w"><section class="sec" style="padding-top:40px">' + ''.join(
             '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</section></div><footer><div class="w">' + C['rodape'] + '</div></footer>')
    return doc(css, b, G + 'Inter:wght@400;500;600;700&display=swap')


# ══════════════════════════════════════════ 09 CINEMA (acabado)
def d09():
    css = r"""
:root{--bg:#09090B;--tx:#F2EFE9;--am:#E9B949;--mut:#8E8A84;--dim:#5C5852;--li:#1E1E21}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);
  font:400 17px/1.68 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
body:before{content:'';position:fixed;inset:0;z-index:60;pointer-events:none;opacity:.26;
  background-image:radial-gradient(rgba(255,255,255,.075) 1px,transparent 1px);background-size:3px 3px}
.w{max-width:1180px;margin:0 auto;padding:0 28px}
h1,h2,h3{margin:0;letter-spacing:-.01em}
.anton{font-family:'Anton',Impact,sans-serif;font-weight:400;text-transform:uppercase}
.kick{font:600 10.5px/1 Inter;letter-spacing:.34em;text-transform:uppercase;color:var(--am);margin:0}
.dimk{color:var(--dim)}

/* ardósia de cena: número, nome e duração. É a estrutura real da página. */
.slate{display:flex;align-items:center;gap:16px;border-top:1px solid #ffffff1f;padding-top:14px;
  margin-bottom:34px;font:600 10.5px/1 Inter;letter-spacing:.24em;text-transform:uppercase}
.slate .n{background:var(--am);color:#0B0A08;padding:6px 9px;font-weight:700;letter-spacing:.14em}
.slate .t{color:var(--tx)}
.slate .r{margin-left:auto;color:var(--dim);letter-spacing:.18em}

/* abertura */
.open{position:relative;min-height:76vh;display:grid;place-content:center;text-align:center;
  padding:72px 28px 54px;overflow:hidden}
.open:before,.open:after{content:'';position:absolute;left:0;right:0;height:34px;background:#000;z-index:2}
.open:before{top:0}.open:after{bottom:0}
.glow{position:absolute;inset:0;z-index:0;background:
  radial-gradient(56% 44% at 50% 36%,rgba(233,185,73,.19),transparent 62%),
  radial-gradient(68% 58% at 80% 90%,rgba(28,84,112,.3),transparent 66%)}
.open>*{position:relative;z-index:3}
.open h1{font-family:'Anton',Impact,sans-serif;font-weight:400;text-transform:uppercase;
  font-size:clamp(36px,7.4vw,98px);line-height:1.08;max-width:15ch;text-wrap:balance}
.open h1 span{display:block;color:var(--am)}
.open .sub{margin:26px auto 0;max-width:38ch;color:var(--mut);font-size:17px}
.open .top{margin:0 0 30px}
.play{max-width:940px;margin:0 auto;aspect-ratio:16/9;background:#08080A;position:relative;
  border:1px solid #ffffff24;box-shadow:0 40px 120px -54px rgba(233,185,73,.45)}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:28px solid var(--tx);border-top:19px solid transparent;border-bottom:19px solid transparent}
/* perfuração de película nas bordas do trecho de projeção */
.reel{position:relative;padding:26px 0}
.reel:before,.reel:after{content:'';position:absolute;top:0;bottom:0;width:11px;
  background-image:linear-gradient(#ffffff1c 0 0);background-size:11px 17px;
  background-repeat:repeat-y;background-position:0 9px;opacity:.55}
.reel:before{left:-2px}.reel:after{right:-2px}
@media(max-width:1240px){.reel:before,.reel:after{display:none}}

.act{padding:clamp(66px,8.4vw,116px) 0}
.big{font-family:'Anton',Impact,sans-serif;text-transform:uppercase;
  font-size:clamp(27px,4.6vw,58px);line-height:1.07;max-width:18ch;text-wrap:balance}
.big em{font-style:normal;color:var(--am)}

/* equações */
.eqs{margin:40px 0 0}
.eq{padding:24px 0;border-top:1px solid #ffffff17;display:grid;
  grid-template-columns:34px 1fr auto 1fr;gap:0 18px;align-items:baseline}
.eq .n{font:700 11px/1.8 Inter;color:var(--dim);font-variant-numeric:tabular-nums}
.eq .a{font-family:'Anton',sans-serif;text-transform:uppercase;font-size:clamp(16px,2.1vw,25px);
  color:#7E7A74;letter-spacing:-.005em;line-height:1.18}
.eq .s{color:#3E3B37}
.eq .b{color:#7E7A74;font-size:15.5px}
.eq.win{border-top-color:var(--am)}
.eq.win .n{color:var(--am)}
.eq.win .a{color:var(--tx)}
.eq.win .b{color:var(--am);font-weight:600;font-size:17px}
.para{margin:40px 0 0;max-width:60ch;font-size:clamp(17px,1.9vw,21px);color:#B6B1AA;line-height:1.6}
.para strong{color:var(--tx);font-weight:600}

/* cartela de preço */
.card{min-height:78vh;display:grid;place-content:center;text-align:center;padding:70px 28px;
  position:relative;overflow:hidden;border-top:1px solid #ffffff17}
.card .glow{background:radial-gradient(50% 44% at 50% 50%,rgba(233,185,73,.16),transparent 64%)}
.card>*{position:relative;z-index:3}
.card h2{font-family:'Anton',sans-serif;text-transform:uppercase;
  font-size:clamp(26px,4vw,52px);margin:14px 0 0}
.pz{display:block;font-family:'Anton',sans-serif;font-size:clamp(88px,18vw,220px);line-height:.84;
  letter-spacing:-.045em;margin:26px 0 0;font-variant-numeric:tabular-nums}
.pz sup{font-size:.2em;vertical-align:super;color:var(--mut)}
.sm{color:var(--mut);font-size:14.5px;margin:18px 0 0}
.sm.t{font-size:11.5px;color:var(--dim);margin-top:5px}
.btn{display:inline-block;margin:36px 0 0;background:var(--am);color:#100E0A;text-decoration:none;
  font:700 14px/1 Inter;letter-spacing:.14em;text-transform:uppercase;padding:23px 52px;
  border:0;cursor:pointer;transition:background .22s,transform .22s}
.btn:hover,.btn:focus-visible{background:#fff;transform:translateY(-2px)}
.ab{margin:24px auto 0;max-width:44ch;font-size:13.5px;color:var(--mut)}
.gar{margin:52px auto 0;max-width:560px;border:1px solid #ffffff24;padding:26px;display:grid;
  grid-template-columns:auto 1fr;gap:22px;align-items:center;text-align:left}
.gar .s{width:90px;height:90px;border:1px solid var(--am);border-radius:50%;display:grid;
  place-content:center;text-align:center;color:var(--am)}
.gar .s b{display:block;font-family:'Anton',sans-serif;font-size:25px;line-height:1}
.gar .s i{font-style:normal;font:600 8.5px/1 Inter;letter-spacing:.16em}
.gar h3{font-size:20px;font-weight:600}.gar p{margin:7px 0 0;color:var(--mut);font-size:15px}

/* hora */
.hl{display:grid;grid-template-columns:34px 104px 1fr;gap:0 22px;padding:22px 0;
  border-top:1px solid #ffffff17}
.hl .n{font:700 11px/2 Inter;color:var(--dim);font-variant-numeric:tabular-nums}
.hl .m{font-family:'Anton',sans-serif;font-size:25px;color:var(--am);font-variant-numeric:tabular-nums}
.hl h3{font-size:clamp(17px,2vw,22px);font-weight:600}
.hl p{margin:9px 0 0;color:var(--mut);font-size:15.5px;max-width:56ch}
ul.e{list-style:none;padding:0;margin:20px 0 0}
ul.e li{padding:14px 0;border-top:1px solid #ffffff17;color:var(--mut);font-size:16px}
ul.e b{color:var(--tx);font-weight:600}

/* prova */
.pv3{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:#ffffff1c;margin-top:36px}
.pc{background:var(--li);padding:28px 24px;display:flex;flex-direction:column;gap:12px}
.pc .n{font-family:'Anton',sans-serif;text-transform:uppercase;font-size:19px;margin:0}
.pc .a{margin:0;font-size:14.5px;color:var(--mut);line-height:1.48}
.pc .d{margin:0;font-size:17px;color:var(--tx);line-height:1.48}
.pc a{margin-top:auto;padding-top:10px;color:var(--am);font:600 11.5px/1 Inter;
  letter-spacing:.16em;text-transform:uppercase;text-decoration:none;align-self:flex-start}
.nota{margin:22px 0 0;font-size:13.5px;color:var(--dim);max-width:60ch}

.recusa{display:block;margin:20px auto 0;background:none;border:0;color:var(--dim);
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer}
.esc{margin:28px auto 0;max-width:52ch;font-size:13px;color:var(--dim);line-height:1.78}
.faq{max-width:720px;margin:0 auto}
details{border-top:1px solid #ffffff17}
summary{cursor:pointer;padding:21px 0;font-family:'Anton',sans-serif;text-transform:uppercase;
  font-size:clamp(16px,2vw,21px);list-style:none;display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary:after{content:'+';color:var(--am);font-family:Inter,sans-serif}
details[open] summary:after{content:'–'}
details p{margin:0 0 24px;color:var(--mut);font-size:15.5px}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--am);outline-offset:4px}
footer{border-top:1px solid #ffffff17;padding:32px 0;text-align:center;font:600 10.5px/1 Inter;
  letter-spacing:.34em;text-transform:uppercase;color:#494540}
@media(max-width:880px){.pv3{grid-template-columns:1fr}
 .eq{grid-template-columns:1fr;gap:5px}.eq .n,.eq .s{display:none}
 .hl{grid-template-columns:72px 1fr}.hl .n{display:none}.hl .m{font-size:21px}
 .slate{gap:10px;font-size:9px;letter-spacing:.14em}}
"""

    def slate(n, t, r):
        return ('<div class="slate"><span class="n">%s</span><span class="t">%s</span>'
                '<span class="r">%s</span></div>' % (n, t, r))

    b = ('<header class="open"><div class="glow"></div>'
         '<p class="kick top">' + C['parabens2'] + '</p>'
         '<h1>' + C['h1a'] + '<span>' + C['h1b'] + '</span></h1>'
         '<p class="sub">' + C['lead'] + '</p></header>'
         '<div class="w reel"><div class="play"></div></div>'
         '<section class="act"><div class="w">' + slate('01', 'A conta', 'três cenários') +
         '<h2 class="big">Só uma das três <em>muda a sua vida</em>.</h2><div class="eqs">' +
         ''.join('<div class="eq%s"><span class="n">%d</span><span class="a">%s</span>'
                 '<span class="s">=</span><span class="b">%s</span></div>'
                 % (' win' if w else '', i + 1, a, bb)
                 for i, (a, bb, w) in enumerate(C['mate'])) +
         '</div><p class="para"><strong>' + C['erro_a'] + '</strong> ' + C['erro_b'] + ' <strong>' +
         C['erro_c'] + '</strong> ' + C['erro_d'] + '</p></div></section>'
         '<section class="card"><div class="glow"></div><p class="kick">' + C['rot'] + '</p>'
         '<h2>' + C['nome'] + '</h2><span class="pz"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a><p class="ab">' + C['abate'] + '</p>'
         '<div class="gar"><div class="s"><b>100%</b><i>DE VOLTA</i></div><div>'
         '<h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div></div></section>'
         '<section class="act"><div class="w">' + slate('02', C['hora_h'], '60 minutos') +
         '<h2 class="big">O que acontece <em>na sua hora</em>.</h2><div style="margin-top:30px">' +
         ''.join('<div class="hl"><span class="n">%d</span><span class="m">%s</span>'
                 '<div><h3>%s</h3>%s</div></div>'
                 % (i + 1, m, h, ('<p>' + d + '</p>') if d else '')
                 for i, (m, h, d) in enumerate(C['hora'])) + '</div>'
         '<h3 style="margin-top:38px;font-size:clamp(19px,2.4vw,26px);font-weight:600">' +
         C['entr_h'] + '</h3><ul class="e">' +
         ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul></div></section>'
         '<section class="act"><div class="w">' + slate('03', 'Prova', 'três autores') +
         '<h2 class="big">' + C['prova_h'] + '</h2><div class="pv3">' + ''.join(
             '<div class="pc"><p class="n">%s</p><p class="a">%s</p><p class="d">%s</p>'
             '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>' % x
             for x in C['provas']) + '</div><p class="nota">' + C['nota_prova'] + '</p></div></section>'
         '<section class="card"><div class="glow"></div><p class="kick">' + C['recap_h'] + '</p>'
         '<ul class="e" style="max-width:440px;margin:18px auto 0;text-align:left">' +
         ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul>'
         '<span class="pz"><sup>R$</sup>' + C['preco'] + '</span>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa">' + C['recusa'] + '</button>'
         '<p class="esc">' + C['escassez'] + '</p></section>'
         '<section class="act"><div class="w"><div class="faq">' +
         slate('04', 'Antes de decidir', 'três dúvidas') + ''.join(
             '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</div></div></section><footer>' + C['rodape'] + '</footer>')
    return doc(css, b, G + 'Inter:wght@400;600;700&family=Anton&display=swap')


# ══════════════════════════════════════════ 11 SUÍÇO NOTURNO (o cruzamento)
def _corpo_suico():
    """
    Markup compartilhado pelo 11 (noturno) e pelo 13 (diurno).

    Os dois sao a MESMA pagina: mesma grade de 12, mesmos cabecalhos de secao,
    mesma ficha lateral, Anton so no H1 e no preco. O que muda e' so a paleta,
    entao tem que viver num lugar so ou um vai envelhecer sem o outro.
    """
    def sh(n, t):
        return '<div class="sh"><span class="num">%s</span><span class="lbl">%s</span></div>' % (n, t)

    b = ('<div class="tp"><div class="w"><span class="lbl">The Book Business</span><ol>' +
         ''.join('<li class="%s">%s · %s</li>' % (
             'ok' if k == 'feito' else ('on' if k == 'agora' else ''), a, t)
             for n, a, t, k in C['passos']) + '</ol></div></div>'
         '<div class="w"><header class="hero g"><h1>' + C['h1a'] + ' <em>' + C['h1b'] + '</em></h1>'
         '<div class="fi">'
         '<dl class="fr"><dt>Situação</dt><dd>' + C['parabens1'] + '</dd></dl>'
         '<dl class="fr"><dt>Pendência</dt><dd><b>' + C['parabens2'] + '</b></dd></dl>'
         '<dl class="fr k"><dt>Agora</dt><dd>' + C['lead'] + '</dd></dl>'
         '</div></header><div class="play"></div>'
         '<section class="sec">' + sh('01', 'A conta') +
         ''.join('<div class="eq%s"><span class="n">%d</span><span class="a">%s</span>'
                 '<span class="s">=</span><span class="b">%s</span></div>'
                 % (' win' if w else '', i + 1, a, bb)
                 for i, (a, bb, w) in enumerate(C['mate'])) +
         '<div class="g"><p class="para"><b>' + C['erro_a'] + '</b> ' + C['erro_b'] + ' <b>' +
         C['erro_c'] + '</b> ' + C['erro_d'] + '</p></div></section></div>'
         '<section class="buy"><div class="w"><div class="g"><div class="l">' +
         sh('02', C['rot']) + '<h2>' + C['nome'] + '</h2>'
         '<dl class="fr" style="margin-top:22px"><dt>Formato</dt><dd>Uma hora no Zoom, '
         'só sobre o seu livro</dd></dl>'
         '<dl class="fr"><dt>Crédito</dt><dd>' + C['abate'] + '</dd></dl></div>'
         '<div class="r"><p class="pz"><sup>R$</sup>' + C['preco'] + '</p>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a></div></div></div></section>'
         '<div class="w"><section class="sec">' + sh('03', 'Garantia') +
         '<div class="g gar"><div class="n100">100%<i>DE VOLTA</i></div>'
         '<div class="tx"><h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div></div></section>'
         '<section class="sec">' + sh('04', C['hora_h']) +
         ''.join('<div class="hr"><span class="n">%d</span><span class="m">%s</span>'
                 '<div><h3>%s</h3>%s</div></div>'
                 % (i + 1, m, h, ('<p>' + d + '</p>') if d else '')
                 for i, (m, h, d) in enumerate(C['hora'])) + '</section>'
         '<section class="sec">' + sh('05', 'Entrega') +
         '<div class="g"><h3 style="grid-column:1/5;font-size:clamp(19px,2.2vw,27px)">' +
         C['entr_h'] + '</h3><ul class="e" style="grid-column:5/13">' +
         ''.join('<li>%s</li>' % e for e in C['entregas']) + '</ul></div></section>'
         '<section class="sec">' + sh('06', C['prova_h']) + '<div class="pv3">' + ''.join(
             '<div class="pc"><p class="n">%s</p><p class="a">%s</p><p class="d">%s</p>'
             '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>' % x
             for x in C['provas']) + '</div><p class="nota">' + C['nota_prova'] + '</p></section></div>'
         '<section class="buy"><div class="w"><div class="g"><div class="l">' +
         sh('07', C['recap_h']) + '<ul class="e">' +
         ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul>'
         '<p class="esc">' + C['escassez'] + '</p></div>'
         '<div class="r"><p class="pz"><sup>R$</sup>' + C['preco'] + '</p>'
         '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
         '<a class="btn" href="#">' + C['cta'] + '</a>'
         '<button class="recusa">' + C['recusa'] + '</button></div></div></div></section>'
         '<div class="w"><section class="sec">' + ''.join(
             '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
         '</section></div><footer><div class="w">' + C['rodape'] + '</div></footer>')
    return b


# ══════════════════════════════════════════ 11 SUÍÇO NOTURNO (o cruzamento)
def d11():
    css = r"""
:root{--bg:#0A0A0B;--tx:#EFEBE1;--am:#E3B04B;--mut:#8C877D;--dim:#5A564F;--ru:#232326}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);
  font:400 16.5px/1.56 Inter,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;
  letter-spacing:-.012em}
.w{max-width:1240px;margin:0 auto;padding:0 26px}
.g{display:grid;grid-template-columns:repeat(12,1fr);gap:26px}
h1,h2,h3{margin:0;font-weight:700;letter-spacing:-.04em;text-wrap:balance}
.anton{font-family:'Anton',Impact,sans-serif;font-weight:400;text-transform:uppercase;letter-spacing:-.02em}
.lbl{font:700 11px/1 Inter;letter-spacing:.1em;text-transform:uppercase}
.num{font:700 11px/1 Inter;letter-spacing:.06em;color:var(--am);font-variant-numeric:tabular-nums}
.sh{display:grid;grid-template-columns:46px 1fr;gap:0 14px;align-items:baseline;
  border-top:1px solid var(--am);padding-top:11px;margin-bottom:30px}
.sh .lbl{display:flex;gap:14px;align-items:center;color:var(--tx)}
.sh .lbl:after{content:'';flex:1;height:1px;background:var(--ru)}
.sec{padding:clamp(44px,5.6vw,72px) 0}

.tp{border-bottom:1px solid var(--ru)}
.tp .w{display:flex;justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap;
  padding:13px 26px}
.tp ol{display:flex;gap:20px;list-style:none;margin:0;padding:0;font:700 11px/1 Inter;
  letter-spacing:.08em;text-transform:uppercase;color:var(--dim)}
.tp .on{color:var(--am)}.tp .ok{color:var(--tx)}
.tp .lbl{color:var(--mut)}

/* abertura: a grade do suíço, o escuro do cinema, Anton só aqui e no preço */
.hero{padding:clamp(44px,6vw,74px) 0 40px;align-items:end}
.hero h1{grid-column:1/9;font-family:'Anton',Impact,sans-serif;font-weight:400;
  text-transform:uppercase;font-size:clamp(36px,6.6vw,92px);line-height:1.04;letter-spacing:-.018em}
.hero h1 em{font-style:normal;color:var(--am)}
.hero .fi{grid-column:9/13;border-top:1px solid var(--am)}
.fr{display:grid;grid-template-columns:74px 1fr;gap:12px;padding:10px 0;
  border-bottom:1px solid var(--ru);align-items:baseline}
.fr dt{font:700 10px/1.5 Inter;letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.fr dd{margin:0;font-size:14.5px;line-height:1.42;color:var(--mut)}
.fr dd b{color:var(--tx);font-weight:700}
.fr.k dd{color:var(--am);font-weight:600}
.play{aspect-ratio:16/9;background:#000;position:relative;border:1px solid var(--ru)}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:26px solid var(--am);border-top:17px solid transparent;border-bottom:17px solid transparent}

.eq{display:grid;grid-template-columns:46px 1fr 30px 1fr;gap:0 14px;padding:19px 0;
  border-bottom:1px solid var(--ru);align-items:baseline}
.eq .n{font:700 11px/1.7 Inter;color:var(--dim);font-variant-numeric:tabular-nums}
.eq .a{font-size:clamp(17px,2.1vw,25px);font-weight:700;letter-spacing:-.035em;line-height:1.14;
  color:#89847C}
.eq .s{color:var(--dim);text-align:center;font-weight:400}
.eq .b{font-size:16px;color:#89847C;line-height:1.4}
.eq.win{border-bottom-color:var(--am)}
.eq.win .n{color:var(--am)}
.eq.win .a{color:var(--tx)}
.eq.win .b{color:var(--am);font-weight:600}
.para{grid-column:1/9;margin:32px 0 0;font-size:clamp(18px,2vw,24px);line-height:1.42;
  letter-spacing:-.028em;font-weight:500;color:#B8B2A8}
.para b{color:var(--am);font-weight:700}

.buy{border-top:1px solid var(--ru);border-bottom:1px solid var(--ru);
  background:linear-gradient(180deg,#0D0D0F,#0A0A0B)}
.buy .w{padding-top:clamp(44px,5.6vw,68px);padding-bottom:clamp(44px,5.6vw,68px)}
.buy .g{align-items:end}
.buy .l{grid-column:1/7}.buy .r{grid-column:8/13}
.buy h2{font-size:clamp(27px,3.4vw,44px)}
.pz{font-family:'Anton',Impact,sans-serif;font-weight:400;font-size:clamp(86px,13.5vw,176px);
  line-height:.82;letter-spacing:-.048em;margin:0;text-align:right;color:var(--am);
  font-variant-numeric:tabular-nums}
.pz sup{font-size:.2em;vertical-align:super;color:var(--mut)}
.sm{margin:14px 0 0;font-size:14px;color:var(--mut);text-align:right}
.sm.t{font-size:11.5px;color:var(--dim);margin-top:5px}
.btn{display:block;width:100%;margin:22px 0 0;background:var(--am);color:#0A0A0B;text-decoration:none;
  text-align:center;font:700 16.5px/1 Inter;letter-spacing:-.015em;padding:23px;border:0;cursor:pointer;
  transition:background .15s}
.btn:hover,.btn:focus-visible{background:#fff}

.gar{align-items:center}
.gar .n100{grid-column:1/4;font-family:'Anton',sans-serif;font-size:clamp(54px,7.6vw,104px);
  line-height:.88;color:var(--am)}
.gar .n100 i{display:block;font-family:Inter,sans-serif;font-style:normal;font-size:.13em;
  font-weight:700;letter-spacing:.16em;color:var(--mut);margin-top:10px}
.gar .tx{grid-column:4/11}
.gar h3{font-size:clamp(21px,2.4vw,30px)}
.gar p{margin:9px 0 0;color:var(--mut)}

.hr{display:grid;grid-template-columns:46px 88px 1fr;gap:0 14px;padding:19px 0;
  border-bottom:1px solid var(--ru)}
.hr .n{font:700 11px/1.9 Inter;color:var(--dim);font-variant-numeric:tabular-nums}
.hr .m{font:700 clamp(19px,2.2vw,26px)/1.05 Inter;letter-spacing:-.045em;color:var(--am);
  font-variant-numeric:tabular-nums}
.hr h3{font-size:clamp(17px,1.9vw,21px)}
.hr p{margin:7px 0 0;color:var(--mut);font-size:15.5px;max-width:58ch}
ul.e{list-style:none;padding:0;margin:0}
ul.e li{border-bottom:1px solid var(--ru);padding:15px 0;font-size:16px;color:var(--mut)}
ul.e li:first-child{border-top:1px solid var(--ru)}
ul.e b{color:var(--tx);font-weight:600}

.pv3{display:grid;grid-template-columns:repeat(3,1fr);gap:0}
.pc{padding:16px 22px 22px 0;border-top:1px solid var(--am);border-right:1px solid var(--ru);
  display:flex;flex-direction:column;gap:11px}
.pc:last-child{border-right:0}
.pc:not(:first-child){padding-left:22px}
.pc .n{font-size:18.5px;font-weight:700;letter-spacing:-.035em;margin:0}
.pc .a{margin:0;font-size:14.5px;color:var(--mut);line-height:1.45}
.pc .d{margin:0;font-size:16.5px;font-weight:500;line-height:1.4;letter-spacing:-.022em;color:var(--tx)}
.pc a{margin-top:auto;padding-top:8px;color:var(--am);font:700 11.5px/1 Inter;letter-spacing:.08em;
  text-transform:uppercase;text-decoration:none;align-self:flex-start;
  border-bottom:1px solid currentColor;padding-bottom:3px}
.nota{margin:22px 0 0;font-size:14px;color:var(--dim);max-width:64ch}

.recusa{display:block;width:100%;margin:12px 0 0;background:none;border:0;color:var(--dim);
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer;text-align:center}
.esc{margin:22px 0 0;font-size:13.5px;color:var(--mut);line-height:1.68;max-width:60ch}
details{border-bottom:1px solid var(--ru)}
details:first-of-type{border-top:1px solid var(--ru)}
summary{cursor:pointer;padding:19px 0;font:700 clamp(17px,2vw,21px)/1.3 Inter;letter-spacing:-.035em;
  list-style:none;display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary:after{content:'+';color:var(--am)}
details[open] summary:after{content:'–'}
details p{margin:0 0 22px;color:var(--mut);max-width:68ch}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--am);outline-offset:4px}
footer{border-top:1px solid var(--ru);padding:20px 0;font:700 11px/1 Inter;letter-spacing:.1em;
  text-transform:uppercase;color:var(--dim)}
@media(max-width:880px){
 .g{grid-template-columns:repeat(6,1fr);gap:16px}
 .hero h1,.hero .fi,.para,.buy .l,.buy .r,.gar .n100,.gar .tx{grid-column:1/-1}
 .hero .fi{margin-top:26px}
 .eq{grid-template-columns:1fr;gap:5px}.eq .n,.eq .s{display:none}
 .hr{grid-template-columns:64px 1fr}.hr .n{display:none}
 .pz,.sm{text-align:left}
 .pv3{grid-template-columns:1fr}.pc{border-right:0;padding:16px 0 22px!important}
 .tp ol{gap:11px;font-size:9.5px}}
"""
    return doc(css, _corpo_suico(),
               G + 'Inter:wght@400;500;600;700&family=Anton&display=swap')


# ══════════════════════════════════════════ 13 SUÍÇO DIURNO (o mesmo, no claro)
def d13():
    css = r"""
/* O gêmeo claro do 11: mesma grade, mesmo Anton no H1 e no preço.
   O ouro não vira texto sobre branco (não passa contraste): vira TARJA.
   Quem carrega o acento no claro é o ocre; o ouro só preenche. */
:root{--bg:#FCFBF8;--tx:#12110F;--oc:#8A5E12;--am:#E9BE63;--mut:#6B665C;
      --dim:#A29B8D;--ru:#E3DED2;--pan:#F3EFE4}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);
  font:400 16.5px/1.56 Inter,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;
  letter-spacing:-.012em}
.w{max-width:1240px;margin:0 auto;padding:0 26px}
.g{display:grid;grid-template-columns:repeat(12,1fr);gap:26px}
h1,h2,h3{margin:0;font-weight:700;letter-spacing:-.04em;text-wrap:balance}
.lbl{font:700 11px/1 Inter;letter-spacing:.1em;text-transform:uppercase}
.num{font:700 11px/1 Inter;letter-spacing:.06em;color:var(--oc);font-variant-numeric:tabular-nums}
.sh{display:grid;grid-template-columns:46px 1fr;gap:0 14px;align-items:baseline;
  border-top:2px solid var(--tx);padding-top:11px;margin-bottom:30px}
.sh .lbl{display:flex;gap:14px;align-items:center;color:var(--tx)}
.sh .lbl:after{content:'';flex:1;height:1px;background:var(--ru)}
.sec{padding:clamp(44px,5.6vw,72px) 0}

.tp{border-bottom:1px solid var(--tx)}
.tp .w{display:flex;justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap;
  padding:13px 26px}
.tp ol{display:flex;gap:20px;list-style:none;margin:0;padding:0;font:700 11px/1 Inter;
  letter-spacing:.08em;text-transform:uppercase;color:var(--dim)}
.tp .on{color:var(--oc)}.tp .ok{color:var(--tx)}
.tp .lbl{color:var(--mut)}

.hero{padding:clamp(44px,6vw,74px) 0 40px;align-items:end}
.hero h1{grid-column:1/9;font-family:'Anton',Impact,sans-serif;font-weight:400;
  text-transform:uppercase;font-size:clamp(34px,6.2vw,86px);line-height:1.16;letter-spacing:-.018em}
/* a tarja NAO pode ser background com padding: a caixa de conteudo do Anton tem
   1,51em de altura, entao a faixa invadia a linha de cima. Aqui ela e' um traco
   de marcador com altura fixa, posicionado sobre as maiusculas. */
.hero h1 em{font-style:normal;padding:0 .08em;margin:0 -.08em;
  background:linear-gradient(var(--am),var(--am)) no-repeat;
  background-size:100% .95em;background-position:0 .32em;
  box-decoration-break:clone;-webkit-box-decoration-break:clone}
.hero .fi{grid-column:9/13;border-top:2px solid var(--tx)}
.fr{display:grid;grid-template-columns:74px 1fr;gap:12px;padding:10px 0;
  border-bottom:1px solid var(--ru);align-items:baseline}
.fr dt{font:700 10px/1.5 Inter;letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.fr dd{margin:0;font-size:14.5px;line-height:1.42;color:var(--mut)}
.fr dd b{color:var(--tx);font-weight:700}
.fr.k dd{color:var(--oc);font-weight:600}
.play{aspect-ratio:16/9;background:var(--tx);position:relative}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:26px solid var(--am);border-top:17px solid transparent;border-bottom:17px solid transparent}

.eq{display:grid;grid-template-columns:46px 1fr 30px 1fr;gap:0 14px;padding:19px 0;
  border-bottom:1px solid var(--ru);align-items:baseline}
.eq .n{font:700 11px/1.7 Inter;color:var(--dim);font-variant-numeric:tabular-nums}
.eq .a{font-size:clamp(17px,2.1vw,25px);font-weight:700;letter-spacing:-.035em;line-height:1.14;
  color:var(--mut)}
.eq .s{color:var(--dim);text-align:center;font-weight:400}
.eq .b{font-size:16px;color:var(--mut);line-height:1.4}
.eq.win{background:var(--am);margin:0 -16px;padding:19px 16px;border-bottom-color:var(--oc)}
.eq.win .n{color:#5E3F08}
.eq.win .a{color:#17140C}
.eq.win .b{color:#3D2E10;font-weight:600}
.eq.win .s{color:#8A6B22}
.para{grid-column:1/9;margin:32px 0 0;font-size:clamp(18px,2vw,24px);line-height:1.42;
  letter-spacing:-.028em;font-weight:500;color:#2E2B25}
.para b{color:var(--oc);font-weight:700}

.buy{background:var(--pan);border-top:1px solid var(--ru);border-bottom:1px solid var(--ru)}
.buy .w{padding-top:clamp(44px,5.6vw,68px);padding-bottom:clamp(44px,5.6vw,68px)}
.buy .g{align-items:end}
.buy .l{grid-column:1/7}.buy .r{grid-column:8/13}
.buy h2{font-size:clamp(27px,3.4vw,44px)}
.buy .fr{border-bottom-color:#D8D2C3}
.pz{font-family:'Anton',Impact,sans-serif;font-weight:400;font-size:clamp(86px,13.5vw,176px);
  line-height:.82;letter-spacing:-.048em;margin:0;text-align:right;color:var(--tx);
  font-variant-numeric:tabular-nums}
.pz sup{font-size:.2em;vertical-align:super;color:var(--oc)}
.sm{margin:14px 0 0;font-size:14px;color:var(--mut);text-align:right}
.sm.t{font-size:11.5px;color:var(--dim);margin-top:5px}
.btn{display:block;width:100%;margin:22px 0 0;background:var(--tx);color:var(--bg);
  text-decoration:none;text-align:center;font:700 16.5px/1 Inter;letter-spacing:-.015em;
  padding:23px;border:0;cursor:pointer;transition:background .15s,color .15s}
.btn:hover,.btn:focus-visible{background:var(--oc);color:#fff}

.gar{align-items:center}
.gar .n100{grid-column:1/4;font-family:'Anton',sans-serif;font-size:clamp(54px,7.6vw,104px);
  line-height:.88;color:var(--oc)}
.gar .n100 i{display:block;font-family:Inter,sans-serif;font-style:normal;font-size:.13em;
  font-weight:700;letter-spacing:.16em;color:var(--mut);margin-top:10px}
.gar .tx{grid-column:4/11}
.gar h3{font-size:clamp(21px,2.4vw,30px)}
.gar p{margin:9px 0 0;color:var(--mut)}

.hr{display:grid;grid-template-columns:46px 88px 1fr;gap:0 14px;padding:19px 0;
  border-bottom:1px solid var(--ru)}
.hr .n{font:700 11px/1.9 Inter;color:var(--dim);font-variant-numeric:tabular-nums}
.hr .m{font:700 clamp(19px,2.2vw,26px)/1.05 Inter;letter-spacing:-.045em;color:var(--oc);
  font-variant-numeric:tabular-nums}
.hr h3{font-size:clamp(17px,1.9vw,21px)}
.hr p{margin:7px 0 0;color:var(--mut);font-size:15.5px;max-width:58ch}
ul.e{list-style:none;padding:0;margin:0}
ul.e li{border-bottom:1px solid var(--ru);padding:15px 0;font-size:16px;color:var(--mut)}
ul.e li:first-child{border-top:1px solid var(--ru)}
ul.e b{color:var(--tx);font-weight:600}

.pv3{display:grid;grid-template-columns:repeat(3,1fr);gap:0}
.pc{padding:16px 22px 22px 0;border-top:2px solid var(--oc);border-right:1px solid var(--ru);
  display:flex;flex-direction:column;gap:11px}
.pc:last-child{border-right:0}
.pc:not(:first-child){padding-left:22px}
.pc .n{font-size:18.5px;font-weight:700;letter-spacing:-.035em;margin:0}
.pc .a{margin:0;font-size:14.5px;color:var(--mut);line-height:1.45}
.pc .d{margin:0;font-size:16.5px;font-weight:500;line-height:1.4;letter-spacing:-.022em;color:var(--tx)}
.pc a{margin-top:auto;padding-top:8px;color:var(--oc);font:700 11.5px/1 Inter;letter-spacing:.08em;
  text-transform:uppercase;text-decoration:none;align-self:flex-start;
  border-bottom:1px solid currentColor;padding-bottom:3px}
.nota{margin:22px 0 0;font-size:14px;color:var(--dim);max-width:64ch}

.recusa{display:block;width:100%;margin:12px 0 0;background:none;border:0;color:var(--mut);
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer;text-align:center}
.esc{margin:22px 0 0;font-size:13.5px;color:var(--mut);line-height:1.68;max-width:60ch}
details{border-bottom:1px solid var(--ru)}
details:first-of-type{border-top:1px solid var(--ru)}
summary{cursor:pointer;padding:19px 0;font:700 clamp(17px,2vw,21px)/1.3 Inter;letter-spacing:-.035em;
  list-style:none;display:flex;justify-content:space-between;gap:16px}
summary::-webkit-details-marker{display:none}
summary:after{content:'+';color:var(--oc)}
details[open] summary:after{content:'–'}
details p{margin:0 0 22px;color:var(--mut);max-width:68ch}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--oc);outline-offset:4px}
footer{border-top:2px solid var(--tx);padding:20px 0;font:700 11px/1 Inter;letter-spacing:.1em;
  text-transform:uppercase;color:var(--mut)}
@media(max-width:880px){
 .g{grid-template-columns:repeat(6,1fr);gap:16px}
 .hero h1,.hero .fi,.para,.buy .l,.buy .r,.gar .n100,.gar .tx{grid-column:1/-1}
 .hero .fi{margin-top:26px}
 .eq{grid-template-columns:1fr;gap:5px}.eq .n,.eq .s{display:none}
 .eq.win{margin:0 -12px;padding:19px 12px}
 .hr{grid-template-columns:64px 1fr}.hr .n{display:none}
 .pz,.sm{text-align:left}
 .pv3{grid-template-columns:1fr}.pc{border-right:0;padding:16px 0 22px!important}
 .tp ol{gap:11px;font-size:9.5px}}
"""
    return doc(css, _corpo_suico(),
               G + 'Inter:wght@400;500;600;700&family=Anton&display=swap')
