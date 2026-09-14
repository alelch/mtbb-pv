# -*- coding: utf-8 -*-
"""
Rumo 14: a linguagem visual do LOMBADA aplicada à página do 90D.

Vem de ~/Claude Code/plataforma-do-autor (área do autor), direção aprovada em
13/09 como "FIRE com paleta MTBB". O que foi trazido, com os mesmos valores:

  · fundo SEMPRE branco, painéis de cor CHAPADA (nada de gradiente, nada de sombra)
  · corte diagonal de 26px sempre pro mesmo lado, painel vizinho entrando 44px
    por baixo (as classes corte-d / -ml-[44px] do index.css de lá)
  · Archivo 900 caixa alta, letter-spacing -.03em, line-height .92, + Montserrat
  · paleta MTBB: tinta #1a1a1a, âmbar #faab00, laranja #fc783c, verde #14523e,
    creme #f3f0e8, areia #f4f1ec, fio #e6e1da
  · texto sobre âmbar/laranja = preto; sobre verde/preto = creme
  · grade de círculos no cabeçalho, um deles é o anel vazado
  · botão com corte-btn (aresta direita inclinada que abre no hover)
  · blocos de apoio com border-top de 3px em vez de cartão

O encaixe que fez valer a pena: as três contas da matemágica viram os três
painéis diagonais que no LOMBADA são as três FASES, e a gramática de cor da
PV do 90D (escuro=risco, laranja=os que fracassam, verde=o 1%) cai exatamente
nos três. Não foi adaptação, foi a mesma figura.

O que NÃO veio: o wordmark L○MBADA e o anel de estado das ações. São marca e
gramática da área do autor, não desta página.
"""
from copy_base import C, doc

G = 'https://fonts.googleapis.com/css2?family='

CORES = {'tinta': '#1a1a1a', 'apoio': '#4a4644', 'mudo': '#7a7472', 'fio': '#e6e1da',
         'areia': '#f4f1ec', 'creme': '#f3f0e8', 'ambar': '#faab00',
         'laranja': '#fc783c', 'verde': '#14523e', 'alerta': '#cc3333'}


def d14():
    css = r"""
:root{--tinta:#1a1a1a;--apoio:#4a4644;--mudo:#7a7472;--fio:#e6e1da;--areia:#f4f1ec;
      --creme:#f3f0e8;--ambar:#faab00;--laranja:#fc783c;--verde:#14523e;--alerta:#cc3333;
      --corte:26px}
*{box-sizing:border-box}
body{margin:0;background:#fff;color:var(--tinta);
  font:400 15px/1.55 Montserrat,ui-sans-serif,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.w{max-width:1060px;margin:0 auto;padding:0 24px}
.display{font-family:Archivo,'Arial Black',Impact,sans-serif;font-weight:900;
  text-transform:uppercase;letter-spacing:-.03em;line-height:.92}
h1,h2,h3{margin:0}
.rot{font:800 12px/1 Montserrat;letter-spacing:.12em;text-transform:uppercase}

/* o corte: 26px sempre pro mesmo lado, deslizando devagar e junto em todos os
   paineis. O vizinho entra 44px por baixo, entao o corte nunca vaza o branco. */
@property --corte{syntax:'<length>';inherits:true;initial-value:26px}
@keyframes corte-desliza{0%,100%{--corte:26px}50%{--corte:42px}}
.corte-d{clip-path:polygon(0 0,100% 0,calc(100% - var(--corte)) 100%,0 100%);
  animation:corte-desliza 14s ease-in-out infinite}
@keyframes flutuar{0%,100%{transform:translate3d(0,0,0)}50%{transform:translate3d(0,-9px,0)}}
@keyframes flutuar-x{0%,100%{transform:translate3d(0,0,0)}50%{transform:translate3d(6px,-5px,0)}}
@keyframes girar{to{transform:rotate(360deg)}}
.flutua{animation:flutuar 6s ease-in-out infinite}
.flutua-x{animation:flutuar-x 7.5s ease-in-out infinite}
.gira{animation:girar 18s linear infinite}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}

/* topo */
.tp{border-bottom:2px solid var(--tinta)}
.tp .w{display:flex;align-items:center;justify-content:space-between;gap:16px;
  flex-wrap:wrap;padding-top:14px;padding-bottom:14px}
.tp ol{display:flex;gap:18px;list-style:none;margin:0;padding:0;
  font:800 11px/1 Montserrat;letter-spacing:.1em;text-transform:uppercase;color:var(--mudo)}
.tp .ok{color:var(--tinta)}
.tp .on{color:var(--laranja)}

/* abertura: painel preto cortado + painel âmbar com a grade de círculos */
.hero{display:grid;grid-template-columns:1.3fr 1fr;min-height:360px;margin-top:26px}
.hero .esq{background:var(--tinta);color:#fff;padding:38px 34px;position:relative;z-index:10}
.hero .esq .rot{color:var(--ambar)}
.hero h1{font-family:Archivo,'Arial Black',sans-serif;font-weight:900;text-transform:uppercase;
  letter-spacing:-.03em;line-height:.92;font-size:clamp(30px,4.4vw,54px);margin:14px 0 0;
  text-wrap:balance}
.hero h1 em{font-style:normal;color:var(--ambar)}
.hero .sub{margin:16px 0 0;max-width:44ch;font-size:15px;color:rgba(255,255,255,.75)}
.hero .dir{background:var(--ambar);margin-left:-44px;position:relative;overflow:hidden;
  min-height:220px}
.bolas{position:absolute;inset:0;display:grid;grid-template-columns:repeat(2,1fr);
  grid-template-rows:repeat(3,1fr);gap:12px;padding:24px 24px 24px 56px}
.bolas i{display:block;border-radius:50%;aspect-ratio:1;width:min(100%,76px);
  align-self:center;justify-self:center}
.btn{display:inline-flex;align-items:center;gap:8px;border:0;cursor:pointer;
  font:800 15px/1 Montserrat;padding:16px 30px 16px 22px;background:var(--ambar);
  color:var(--tinta);text-decoration:none;
  clip-path:polygon(0 0,100% 0,calc(100% - 8px) 100%,0 100%);
  transition:clip-path .35s cubic-bezier(.2,.7,.2,1),transform .35s cubic-bezier(.2,.7,.2,1)}
.btn:hover,.btn:focus-visible{clip-path:polygon(0 0,100% 0,calc(100% - 18px) 100%,0 100%);
  transform:translateX(2px)}
.btn.preto{background:var(--tinta);color:#fff}
.btn.bloco{display:flex;width:100%;justify-content:center;padding-left:30px}
.mini{font-size:12px;color:rgba(255,255,255,.5);margin:12px 0 0}

.play{aspect-ratio:16/9;background:var(--tinta);position:relative;margin-top:26px}
.play:after{content:'';position:absolute;left:50%;top:50%;translate:-42% -50%;
  border-left:26px solid var(--ambar);border-top:17px solid transparent;
  border-bottom:17px solid transparent}

/* as três contas = os três painéis diagonais */
.contas{display:grid;grid-template-columns:repeat(3,1fr);margin-top:42px}
.cta3{padding:26px 26px 30px;position:relative}
.cta3:nth-child(1){background:var(--tinta);color:var(--creme);z-index:20}
.cta3:nth-child(2){background:var(--laranja);color:var(--tinta);z-index:10;
  margin-left:-44px;padding-left:70px}
.cta3:nth-child(3){background:var(--verde);color:var(--creme);margin-left:-44px;padding-left:70px}
.cta3 .k{font:800 11px/1 Montserrat;letter-spacing:.14em;text-transform:uppercase;opacity:.75}
.cta3 .a{font-family:Archivo,'Arial Black',sans-serif;font-weight:900;text-transform:uppercase;
  letter-spacing:-.03em;line-height:.96;font-size:clamp(17px,1.9vw,23px);margin:10px 0 0}
.cta3 .b{margin:12px 0 0;font-size:14px;font-weight:600;opacity:.92}
.cta3.ganha .b{opacity:1}

/* citação */
.cit{background:var(--areia);margin-top:0;padding:44px 34px}
.cit p{margin:0 auto;max-width:52ch;font-family:Archivo,'Arial Black',sans-serif;font-weight:900;
  text-transform:uppercase;letter-spacing:-.03em;line-height:.98;
  font-size:clamp(21px,3.1vw,38px);text-wrap:balance}
.cit .p2{margin:20px auto 0;font-family:Montserrat,sans-serif;font-weight:400;text-transform:none;
  letter-spacing:0;line-height:1.55;font-size:15.5px;color:var(--apoio);max-width:60ch}
.cit .p2 b{color:var(--tinta);font-weight:800}

/* oferta */
.of{display:grid;grid-template-columns:1.15fr 1fr;margin-top:42px}
.of .l{background:var(--tinta);color:var(--creme);padding:34px 30px;position:relative;z-index:10}
.of .l .rot{color:var(--ambar)}
.of .l h2{font-family:Archivo,'Arial Black',sans-serif;font-weight:900;text-transform:uppercase;
  letter-spacing:-.03em;line-height:.94;font-size:clamp(24px,3.2vw,38px);margin:12px 0 0}
.of .l ul{list-style:none;padding:0;margin:20px 0 0}
.of .l li{padding:9px 0 9px 22px;position:relative;font-size:14.5px;color:rgba(243,240,232,.82)}
.of .l li:before{content:'';position:absolute;left:0;top:15px;width:11px;height:2px;
  background:var(--ambar)}
.of .r{background:var(--ambar);color:var(--tinta);margin-left:-44px;padding:34px 30px 34px 66px;
  display:flex;flex-direction:column;justify-content:center}
.of .r .k{font:800 11px/1 Montserrat;letter-spacing:.14em;text-transform:uppercase;opacity:.72}
.pz{font-family:Archivo,'Arial Black',sans-serif;font-weight:900;letter-spacing:-.045em;
  line-height:.86;font-size:clamp(62px,9.5vw,116px);margin:10px 0 0;font-variant-numeric:tabular-nums}
.pz sup{font-size:.26em;vertical-align:super}
.sm{margin:12px 0 0;font-size:13.5px;font-weight:600}
.sm.t{font-size:11.5px;opacity:.7;margin-top:4px;font-weight:500}
.ab{margin:18px 0 0;font-size:13px;font-weight:600;opacity:.82}

/* garantia: o anel */
.gar{display:grid;grid-template-columns:auto 1fr;gap:26px;align-items:center;
  border-top:3px solid var(--tinta);padding-top:24px;margin-top:42px}
.anel{width:104px;height:104px;border-radius:50%;border:9px solid var(--verde);
  border-right-color:transparent;display:grid;place-content:center;text-align:center;
  font-family:Archivo,'Arial Black',sans-serif;font-weight:900;color:var(--verde);
  font-size:23px;letter-spacing:-.03em}
.gar h3{font-family:Archivo,'Arial Black',sans-serif;font-weight:900;text-transform:uppercase;
  letter-spacing:-.03em;line-height:.96;font-size:clamp(19px,2.3vw,27px)}
.gar p{margin:9px 0 0;color:var(--apoio);font-size:14.5px}

/* a hora */
.sec{margin-top:48px}
.tit{font-family:Archivo,'Arial Black',sans-serif;font-weight:900;text-transform:uppercase;
  letter-spacing:-.03em;line-height:.94;font-size:clamp(23px,3vw,36px)}
.hora{margin-top:22px}
.hl{display:grid;grid-template-columns:56px 86px 1fr;gap:18px;align-items:start;
  border-top:1px solid var(--fio);padding:18px 0}
.hl .bola{width:42px;height:42px;border-radius:50%;background:var(--ambar);color:var(--tinta);
  display:grid;place-content:center;font:900 15px/1 Archivo,'Arial Black',sans-serif}
.hl .m{font-family:Archivo,'Arial Black',sans-serif;font-weight:900;letter-spacing:-.03em;
  font-size:20px;color:var(--laranja);padding-top:8px}
.hl h3{font-size:17px;font-weight:800;padding-top:8px}
.hl p{margin:7px 0 0;color:var(--apoio);font-size:14.5px;max-width:56ch}

/* blocos com fio de 3px (nada de cartão) */
.tres{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;margin-top:26px}
.blk{border-top:3px solid var(--tinta);padding-top:16px}
.blk .n{font-weight:800;font-size:15.5px;margin:0}
.blk p{margin:8px 0 0;color:var(--apoio);font-size:14px;line-height:1.5}
.blk .d{color:var(--tinta);font-weight:600}
.blk a{display:inline-block;margin-top:12px;color:var(--tinta);font:800 12px/1 Montserrat;
  letter-spacing:.08em;text-transform:uppercase;text-decoration:none;
  border-bottom:2px solid var(--ambar);padding-bottom:3px}
.nota{margin:20px 0 0;font-size:13.5px;color:var(--mudo);max-width:62ch}

.recusa{display:block;width:100%;margin:14px 0 0;background:none;border:0;
  font:600 13.5px Montserrat;color:var(--tinta);text-decoration:underline;cursor:pointer;opacity:.7}
.esc{margin:20px 0 0;font-size:13px;line-height:1.62;font-weight:600;opacity:.8}

.faq{margin-top:48px}
details{border-top:1px solid var(--fio)}
details:last-of-type{border-bottom:1px solid var(--fio)}
summary{cursor:pointer;padding:18px 0;list-style:none;display:flex;justify-content:space-between;
  gap:16px;font-family:Archivo,'Arial Black',sans-serif;font-weight:900;text-transform:uppercase;
  letter-spacing:-.03em;font-size:clamp(15px,1.9vw,19px)}
summary::-webkit-details-marker{display:none}
summary:after{content:'+';color:var(--laranja);font-family:Montserrat,sans-serif;font-weight:800}
details[open] summary:after{content:'–'}
details p{margin:0 0 20px;color:var(--apoio);font-size:14.5px;max-width:66ch}
:focus-visible{outline:3px solid var(--ambar);outline-offset:2px}
footer{border-top:2px solid var(--tinta);margin-top:56px;padding:20px 0;
  font:800 11px/1 Montserrat;letter-spacing:.12em;text-transform:uppercase;color:var(--mudo)}

@media(max-width:860px){
 .hero,.of{grid-template-columns:1fr}
 .hero .dir,.of .r{margin-left:0;padding-left:26px}
 .hero .esq,.of .l{clip-path:none;animation:none}
 .bolas{grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,1fr);padding:22px}
 .contas{grid-template-columns:1fr}
 .cta3{clip-path:none!important;animation:none!important;margin-left:0!important;
   padding-left:26px!important}
 .tres{grid-template-columns:1fr;gap:20px}
 .hl{grid-template-columns:44px 1fr;gap:12px}
 .hl .m{grid-column:2;padding-top:0;font-size:17px}
 .hl h3{grid-column:2;padding-top:2px}
 .hl p{grid-column:2}
 .tp ol{gap:10px;font-size:9px}
 .pz{text-align:left}}
"""
    bolas = ''.join(
        '<i class="%s" style="%s;animation-delay:%.1fs"></i>' % (
            'gira' if c == 'anel' else ('flutua-x' if i % 2 else 'flutua'),
            ('border:7px solid %s;border-right-color:transparent' % CORES['tinta'])
            if c == 'anel' else 'background:%s' % c,
            (i * .9) % 3)
        for i, c in enumerate([CORES['verde'], CORES['laranja'], CORES['tinta'],
                               'anel', CORES['creme'], CORES['tinta']]))

    contas = ''
    for i, (a, bb, w) in enumerate(C['mate']):
        contas += ('<div class="cta3%s%s"><p class="k">Conta %d</p>'
                   '<p class="a">%s</p><p class="b">%s</p></div>'
                   % (' ganha' if w else '', ' corte-d' if i < 2 else '', i + 1, a, bb))

    b = (
     '<div class="tp"><div class="w"><span class="display" style="font-size:17px">'
     'The Book Business</span><ol>' +
     ''.join('<li class="%s">%s · %s</li>' % (
         'ok' if k == 'feito' else ('on' if k == 'agora' else ''), a, t)
         for n, a, t, k in C['passos']) + '</ol></div></div>'

     '<div class="w"><header class="hero">'
     '<div class="esq corte-d"><p class="rot">Passo 2 de 3 · ' + C['parabens2'] + '</p>'
     '<h1>' + C['h1a'] + ' <em>' + C['h1b'] + '</em></h1>'
     '<p class="sub">' + C['lead'] + '</p>'
     '<p style="margin:26px 0 0"><a class="btn" href="#oferta">' + C['cta2'] + '</a></p>'
     '<p class="mini">' + C['parabens1'] + '</p></div>'
     '<div class="dir"><div class="bolas">' + bolas + '</div></div></header>'
     '<div class="play"></div>'

     '<section class="contas">' + contas + '</section>'
     '<section class="cit"><p>' + C['erro_a'] + '</p>'
     '<p class="p2">' + C['erro_b'] + ' <b>' + C['erro_c'] + '</b> ' + C['erro_d'] + '</p></section>'

     '<section class="of" id="oferta"><div class="l corte-d">'
     '<p class="rot">' + C['rot'] + '</p><h2>' + C['nome'] + '</h2><ul>' +
     ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul></div>'
     '<div class="r"><p class="k">Investimento</p>'
     '<p class="pz"><sup>R$</sup>' + C['preco'] + '</p>'
     '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
     '<p style="margin:22px 0 0"><a class="btn preto bloco" href="#">' + C['cta'] + '</a></p>'
     '<p class="ab">' + C['abate'] + '</p></div></section>'

     '<section class="gar"><div class="anel">100%</div><div>'
     '<h3>' + C['gar_h'] + '</h3><p>' + C['gar_p'] + '</p></div></section>'

     '<section class="sec"><h2 class="tit">' + C['hora_h'] + '</h2><div class="hora">' +
     ''.join('<div class="hl"><span class="bola">%d</span><span class="m">%s</span>'
             '<div><h3>%s</h3>%s</div></div>'
             % (i + 1, m, h, ('<p>' + d + '</p>') if d else '')
             for i, (m, h, d) in enumerate(C['hora'])) + '</div></section>'

     '<section class="sec"><h2 class="tit">' + C['entr_h'] + '</h2><div class="tres">' +
     ''.join('<div class="blk"><p class="n">%s</p></div>' % e for e in C['entregas']) +
     '</div></section>'

     '<section class="sec"><h2 class="tit">' + C['prova_h'] + '</h2><div class="tres">' +
     ''.join('<div class="blk"><p class="n">%s</p><p>%s</p><p class="d">%s</p>'
             '<a href="%s" target="_blank" rel="noopener">Ver depoimento</a></div>' % x
             for x in C['provas']) +
     '</div><p class="nota">' + C['nota_prova'] + '</p></section>'

     '<section class="of" style="margin-top:48px"><div class="l corte-d">'
     '<p class="rot">' + C['recap_h'] + '</p><ul style="margin-top:16px">' +
     ''.join('<li>%s</li>' % r for r in C['recap']) + '</ul>'
     '<p class="esc" style="color:rgba(243,240,232,.72)">' + C['escassez'] + '</p></div>'
     '<div class="r"><p class="pz"><sup>R$</sup>' + C['preco'] + '</p>'
     '<p class="sm">' + C['avista'] + '</p><p class="sm t">' + C['obs'] + '</p>'
     '<p style="margin:22px 0 0"><a class="btn preto bloco" href="#">' + C['cta'] + '</a></p>'
     '<button class="recusa">' + C['recusa'] + '</button></div></section>'

     '<section class="faq">' + ''.join(
         '<details><summary>%s</summary><p>%s</p></details>' % f for f in C['faq']) +
     '</section>'
     '<footer>' + C['rodape'] + '</footer></div>')

    return doc(css, b, G + 'Archivo:wght@900&family=Montserrat:wght@400;500;600;800&display=swap')
