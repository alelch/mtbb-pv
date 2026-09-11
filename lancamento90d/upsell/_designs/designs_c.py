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
    return doc(css, b, G + 'Inter:wght@400;500;600;700&family=Anton&display=swap')


# ══════════════════════════════════════════ 12 CAPÍTULOS (a referência da Hotmart)
def d12():
    """
    O rumo da referência que o cliente mandou (hotmart.build, rascunho da
    própria Call de Diagnóstico). O que foi copiado de lá, de propósito:

      · numeral fantasma gigante por capítulo, rótulo mono "CAPÍTULO UM"
      · fundos alternando branco e cinza-claro, sem moldura
      · faixa preta em marquise com as palavras da oferta
      · sublinhado à mão na frase-chave do H1
      · fita de progresso no topo, dica "role para ver"
      · linha do tempo numerada com círculos ligados por fio
      · bloco de oferta em preto cheio, com o cartão de preço dentro
      · FAQ em cartão arredondado com "+"

    O que NÃO foi copiado, e por quê:

      · o fade-in ao rolar. A referência esconde cada bloco até ele entrar na
        tela. Numa página pós-compra, que a pessoa lê com pressa e muitas vezes
        no celular com conexão ruim, isso troca leitura por efeito. Aqui tudo
        já nasce visível.
      · a ausência de acento. A referência é preto e branco puro. Entra UM
        verde da marca, e só em dois lugares: a conta que ganha e o sublinhado.
    """
    css = r"""
:root{--pa:#fff;--pa2:#F4F4F5;--ink:#0B0B0C;--mut:#6B6B70;--dim:#9A9AA0;
      --ru:#E4E4E7;--vd:#14523E;--vd2:#1C6B51}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);
  font:400 17px/1.62 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.w{max-width:1060px;margin:0 auto;padding:0 28px}
.n{max-width:720px}
h1,h2,h3{margin:0;font-family:'Instrument Sans',Inter,Helvetica,sans-serif;font-weight:700;
  letter-spacing:-.038em;line-height:1.06;text-wrap:balance}
.mono{font-family:'DM Mono',ui-monospace,monospace}
.eyebrow{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.24em;
  text-transform:uppercase;color:var(--dim);margin:0 0 14px}

/* fita de progresso */
.prog{position:fixed;top:0;left:0;height:3px;background:var(--ink);width:0;z-index:40}

/* passos */
.tp{border-bottom:1px solid var(--ru);background:var(--pa)}
.tp ol{display:flex;gap:26px;list-style:none;margin:0;padding:13px 0;flex-wrap:wrap;
  font-family:'DM Mono',monospace;font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--dim)}
.tp .ok{color:var(--ink)}.tp .on{color:var(--vd)}

/* abertura */
.hero{position:relative;text-align:center;padding:clamp(56px,8vw,104px) 0 clamp(40px,5vw,64px);
  overflow:hidden}
.hero:before{content:'';position:absolute;inset:-30% -10% auto;height:150%;z-index:0;
  background:radial-gradient(46% 42% at 50% 34%,rgba(11,11,12,.09),transparent 70%)}
.hero>*{position:relative;z-index:1}
.hero h1{font-size:clamp(34px,6.4vw,78px);max-width:16ch;margin:0 auto}
.hero h1 .u{position:relative;white-space:nowrap}
.hero h1 .u svg{position:absolute;left:-2%;bottom:-.16em;width:104%;height:.3em;overflow:visible}
.hero h1 .u path{fill:none;stroke:var(--vd2);stroke-width:7;stroke-linecap:round}
.hero .sub{margin:24px auto 0;max-width:46ch;color:var(--mut);font-size:18px}
.pill{display:inline-block;margin:30px 0 0;background:var(--ink);color:#fff;text-decoration:none;
  font:600 15.5px/1 Inter;padding:18px 34px;border-radius:999px;border:0;cursor:pointer;
  transition:transform .16s,background .16s}
.pill:hover,.pill:focus-visible{background:var(--vd);transform:translateY(-1px)}
.cue{margin:clamp(34px,5vw,60px) 0 0;font-family:'DM Mono',monospace;font-size:10.5px;
  letter-spacing:.22em;text-transform:uppercase;color:var(--dim)}
.play{max-width:880px;margin:clamp(30px,4vw,48px) auto 0;aspect-ratio:16/9;background:var(--ink);
  border-radius:16px;position:relative;overflow:hidden}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:26px solid #fff;border-top:17px solid transparent;border-bottom:17px solid transparent}

/* marquise */
.mq{background:var(--ink);color:#fff;overflow:hidden;padding:15px 0}
.mq div{display:flex;gap:34px;white-space:nowrap;width:max-content;
  font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.24em;text-transform:uppercase;
  animation:slide 34s linear infinite}
.mq span{opacity:.9}.mq i{font-style:normal;opacity:.42}
@keyframes slide{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@media (prefers-reduced-motion:reduce){.mq div{animation:none}}

/* capítulos */
.cap{position:relative;padding:clamp(56px,7.4vw,104px) 0}
.cap.alt{background:var(--pa2)}
.cap .ghost{position:absolute;right:clamp(10px,4vw,60px);top:clamp(30px,4vw,54px);
  font-family:'Instrument Sans',sans-serif;font-weight:700;font-size:clamp(72px,12vw,150px);
  line-height:.8;letter-spacing:-.06em;color:rgba(11,11,12,.055);pointer-events:none;
  font-variant-numeric:tabular-nums}
.cap h2{font-size:clamp(25px,3.6vw,42px);max-width:19ch}
.cap .tx{margin:22px 0 0;max-width:58ch;color:var(--mut);font-size:17.5px}

/* as três contas */
.eqs{margin:34px 0 0;max-width:760px}
.eq{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:baseline;
  padding:18px 0;border-top:1px solid var(--ru)}
.eq:last-child{border-bottom:1px solid var(--ru)}
.eq .a{font-family:'Instrument Sans',sans-serif;font-weight:700;letter-spacing:-.032em;
  font-size:clamp(16px,2vw,22px);color:var(--mut)}
.eq .s{color:var(--dim)}
.eq .b{font-size:15.5px;color:var(--mut)}
.eq.win .a{color:var(--ink)}
.eq.win .b{color:var(--vd);font-weight:600}
.eq.win{border-top-color:var(--vd)}

/* citação */
.pq{text-align:center;padding:clamp(50px,6.4vw,86px) 0}
.pq .m{font-family:'Instrument Sans',sans-serif;font-weight:700;font-size:44px;color:var(--ru);
  line-height:.6;display:block;margin-bottom:20px}
.pq p{margin:0 auto;max-width:22ch;font-family:'Instrument Sans',sans-serif;font-weight:700;
  font-size:clamp(24px,3.8vw,44px);line-height:1.1;letter-spacing:-.038em;text-wrap:balance}
.pq .sm{margin:22px auto 0;max-width:58ch;font-family:Inter,sans-serif;font-weight:400;
  font-size:16.5px;color:var(--mut);line-height:1.6;letter-spacing:0}

/* cartões */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:30px 0 0}
.cd{background:var(--pa);border:1px solid var(--ru);border-radius:14px;padding:20px}
.cap.alt .cd{background:#fff}
.cd .ck{width:26px;height:26px;border-radius:50%;border:1px solid var(--ru);display:grid;
  place-content:center;color:var(--vd);font-size:13px;margin-bottom:14px}
.cd p{margin:0;font-size:15.5px;line-height:1.5}
.cd p b{font-weight:600}

/* linha do tempo */
.tl{margin:32px 0 0;max-width:700px}
.st{display:grid;grid-template-columns:40px 1fr;gap:18px;position:relative;padding-bottom:26px}
.st:last-child{padding-bottom:0}
.st:not(:last-child):before{content:'';position:absolute;left:19px;top:38px;bottom:2px;width:1px;
  background:var(--ru)}
.st .no{width:40px;height:40px;border-radius:50%;border:1px solid var(--ru);display:grid;
  place-content:center;font-family:'DM Mono',monospace;font-size:11.5px;color:var(--mut);
  background:var(--pa)}
.cap.alt .st .no{background:var(--pa2)}
.st h3{font-size:18px}
.st .m{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--vd);margin:0 0 5px}
.st p{margin:7px 0 0;color:var(--mut);font-size:15.5px}

/* prova */
.pv{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:30px 0 0}
.pc{background:#fff;border:1px solid var(--ru);border-radius:14px;padding:22px;
  display:flex;flex-direction:column;gap:11px}
.pc .n{margin:0;font-family:'Instrument Sans',sans-serif;font-weight:700;font-size:17px;
  letter-spacing:-.03em}
.pc .a{margin:0;font-size:14.5px;color:var(--mut);line-height:1.5}
.pc .d{margin:0;font-size:16px;line-height:1.48}
.pc a{margin-top:auto;padding-top:6px;color:var(--vd);font:600 13px/1 Inter;text-decoration:none;
  align-self:flex-start;border-bottom:1px solid rgba(20,82,62,.3);padding-bottom:3px}
.nota{margin:18px 0 0;font-size:14px;color:var(--dim);max-width:62ch}

/* oferta em preto */
.offer{background:var(--ink);color:#fff;padding:clamp(56px,7vw,96px) 0}
.offer .eyebrow{color:#ffffff70}
.offer h2{font-size:clamp(26px,3.8vw,44px);max-width:16ch}
.offer .tx{margin:18px 0 0;max-width:52ch;color:#ffffffa8;font-size:17px}
.obox{margin:34px 0 0;background:#17171A;border:1px solid #2A2A2E;border-radius:18px;padding:28px;
  display:grid;grid-template-columns:1fr auto;gap:28px;align-items:end}
.obox .lst{list-style:none;margin:0;padding:0;display:grid;gap:9px}
.obox .lst li{font-size:15.5px;color:#ffffffbd;padding-left:22px;position:relative}
.obox .lst li:before{content:'';position:absolute;left:0;top:8px;width:12px;height:6px;
  border-left:1.6px solid #fff;border-bottom:1.6px solid #fff;rotate:-45deg}
.obox .rt{text-align:right;min-width:240px}
.obox .kk{font-family:'DM Mono',monospace;font-size:10.5px;letter-spacing:.2em;
  text-transform:uppercase;color:#ffffff70;margin:0}
.obox .pz{font-family:'Instrument Sans',sans-serif;font-weight:700;font-size:clamp(48px,7vw,80px);
  line-height:.94;letter-spacing:-.05em;margin:8px 0 0;font-variant-numeric:tabular-nums}
.obox .pz sup{font-size:.34em;vertical-align:super;color:#ffffff8a}
.obox .sm{margin:10px 0 0;font-size:13.5px;color:#ffffff9e}
.obox .sm.t{font-size:11.5px;color:#ffffff63;margin-top:4px}
.obox .pill{background:#fff;color:var(--ink);margin-top:18px;display:block;text-align:center}
.obox .pill:hover{background:var(--vd2);color:#fff}
.ab{margin:18px 0 0;font-size:13.5px;color:#ffffff8a;max-width:52ch}
.gar{margin:22px 0 0;display:grid;grid-template-columns:auto 1fr;gap:18px;align-items:center;
  border-top:1px solid #ffffff1f;padding-top:22px}
.gar .s{width:66px;height:66px;border-radius:50%;border:1px solid #ffffff3d;display:grid;
  place-content:center;text-align:center}
.gar .s b{display:block;font-family:'Instrument Sans',sans-serif;font-weight:700;font-size:17px;
  line-height:1}
.gar .s i{font-style:normal;font-family:'DM Mono',monospace;font-size:7.5px;letter-spacing:.12em;
  color:#ffffff8a}
.gar h3{font-size:17px}.gar p{margin:5px 0 0;color:#ffffffa8;font-size:14.5px}
.recusa{display:block;width:100%;margin:16px 0 0;background:none;border:0;color:#ffffff82;
  font:400 13.5px Inter;text-decoration:underline;cursor:pointer}
.esc{margin:18px 0 0;font-size:13.5px;color:#ffffff8a;line-height:1.68;max-width:62ch}

/* faq */
.faq{display:grid;gap:10px;margin:28px 0 0;max-width:760px}
details{background:var(--pa);border:1px solid var(--ru);border-radius:14px}
.cap.alt details{background:#fff}
summary{cursor:pointer;padding:17px 20px;font-weight:600;font-size:16.5px;list-style:none;
  display:flex;justify-content:space-between;gap:16px;align-items:center}
summary::-webkit-details-marker{display:none}
summary:after{content:'+';color:var(--mut);font-size:19px;font-weight:400}
details[open] summary:after{content:'–'}
details p{margin:0 20px 18px;color:var(--mut);font-size:15.5px}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--vd);
  outline-offset:3px}
footer{border-top:1px solid var(--ru);padding:26px 0;text-align:center;
  font-family:'DM Mono',monospace;font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--dim)}
@media(max-width:820px){.pv{grid-template-columns:1fr}
 .obox{grid-template-columns:1fr}.obox .rt{text-align:left;min-width:0}
 .eq{grid-template-columns:1fr;gap:4px}.eq .s{display:none}
 .tp ol{gap:13px;font-size:9px}}
"""

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
     '<p class="sm"><b>' + C['erro_c'] + '</b> ' + C['erro_d'] + '</p></div></section>'

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
