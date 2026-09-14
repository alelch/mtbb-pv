# -*- coding: utf-8 -*-
"""
A CURVA, três acabamentos.

    python3 gera_curva.py [destino.html] [--artifact]

O cliente escolheu o mecanismo G da rodada anterior (a conta vira a vida do
livro no tempo) e pediu mais desenho. O mecanismo está fechado; o que muda
aqui é o tratamento.

As três curvas são as mesmas nos três, desenhadas no MESMO sistema de
coordenadas (640×112, linha de base em y=104), porque só assim a comparação
é honesta: o pico do lançamento bom com livro ruim é MAIS ALTO que o do
livro bom, e mesmo assim termina embaixo. Essa é a frase da seção desenhada.

⚠️ Não é gráfico de dados. É diagrama. A página diz isso em letra miúda, e
tem que continuar dizendo: inventar número aqui seria mentir.
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_args = [a for a in sys.argv[1:] if not a.startswith('--')]
OUT = _args[0] if _args else os.path.join(HERE, 'curva.html')
ARTIFACT = '--artifact' in sys.argv

C = [
    ('Livro bom + lançamento ruim', 'Ninguém descobre.'),
    ('Livro ruim + lançamento bom', 'Vende no lançamento. Depois, esquecido.'),
    ('Livro bom + lançamento bom',  'Muda a vida do autor.'),
]

# O traço de cada conta. x=92 é o lançamento nas três.
# ⚠️ O PICO DO BOM+BOM TEM QUE SER >= O DO RUIM+BOM (erro corrigido em 14/09,
# o cliente pegou): o lançamento é igualmente bom nos dois, e com o livro bom
# ele converte MAIS, não menos. A diferença entre as duas contas não está no
# lançamento, está no que vem depois dele. Desenhar o pico do livro bom mais
# baixo dizia, sem querer, que livro bom vende menos.
P = [
    'M0 100 L92 100 C110 100 116 90 130 90 C144 90 152 99 170 100 L640 101',
    'M0 100 L92 100 C114 100 122 26 152 26 C184 26 198 72 240 87 C300 104 350 96 420 98 L640 99',
    'M0 100 L92 100 C112 100 119 11 150 11 C176 11 188 42 214 46 C278 51 330 40 402 30 '
    'C482 19 560 9 640 2',
]
FIM_Y = [101, 99, 2]          # onde cada uma termina, pro ponto final
# UMA COR POR CONTA, e cada uma diz o que aconteceu:
#   frio azulado  o livro que ninguém encontra (nunca chegou a acender)
#   vermelho      o que acende e morre. É o mesmo vermelho do erro da seção
#                 de baixo, de propósito: ali e aqui ele quer dizer a mesma
#                 coisa, "isto deu errado"
#   âmbar         o que fica. É a cor da marca e da oferta, e na página só
#                 ela brilha
COR = ['#5F7184', '#E0574A', '#EAB82D']
# o rótulo de cada conta puxa a cor da sua curva, num tom que passa em
# contraste no fundo escuro (o traço pode ser fraco, o texto não)
COR_ROT = ['#93A6B8', '#E0574A', '#EAB82D']
LANC = 92.0 / 640.0 * 100.0   # a marca do lançamento, em %


def area(d):
    """o traço vira área fechando na linha de base"""
    return d + ' L640 104 L0 104 Z'


BASE = r"""
:root{
  --pa:#0B0B0D;--ink:#EFEDE8;--mut:#9A958D;--dim:#868178;--ru:#2C2C33;
  --ac:#EAB82D;--apaga:#3A3A3F;
  --ff:'DM Sans',system-ui,sans-serif;--fd:'Space Grotesk','DM Sans',sans-serif;
  --fs:Fraunces,Georgia,serif}
*{box-sizing:border-box}
body{margin:0;background:#0F0F11;color:var(--ink);font:400 16px/1.62 var(--ff);
  -webkit-font-smoothing:antialiased}
.w{max-width:1120px;margin:0 auto;padding-inline:22px}
h1,h2,h3{margin:0;font-family:var(--fd);font-weight:700;letter-spacing:-.03em;line-height:1.1;
  text-wrap:balance}
header{padding-block:54px 30px}
header h1{font-size:clamp(1.9rem,4vw,2.8rem)}
header p{margin:16px 0 0;max-width:68ch;color:var(--mut)}
header p b{color:var(--ink)}
.item{border-top:1px solid var(--ru);padding-block:44px 8px}
.cab{display:flex;align-items:baseline;gap:12px;margin:0 0 6px}
.cab .no{font-family:var(--fd);font-weight:700;font-size:.78rem;letter-spacing:.16em;color:var(--ac)}
.cab h2{font-size:1.25rem}
.tese{margin:0 0 26px;color:var(--mut);max-width:74ch;font-size:.95rem}
.palco{--pad:clamp(18px,4vw,44px);background:var(--pa);border:1px solid var(--ru);
  border-radius:16px;padding:clamp(32px,5vw,58px) var(--pad);overflow:hidden}
.tit{text-align:center;margin:0 0 clamp(34px,5vw,52px);font-size:clamp(1.5rem,3.4vw,2.3rem)}
.tit .risco{position:relative;white-space:nowrap}
.tit .risco:after{content:"";position:absolute;left:-2px;right:-2px;bottom:-.08em;height:.09em;
  background:var(--ac);border-radius:2px}
.miudo{margin:26px auto 0;max-width:56ch;text-align:center;font-size:.78rem;color:var(--dim)}
footer{padding-block:38px 70px;color:var(--dim);font-size:.85rem;border-top:1px solid var(--ru);
  margin-top:44px}
svg{display:block;width:100%;height:auto;overflow:visible}

/* ── OS RÓTULOS DE EIXO, EM TODOS OS GRÁFICOS ──
   Cada um colado na linha que nomeia: "vendas" e "lançamento" na vertical,
   porque as linhas deles são verticais, e "tempo" logo abaixo da linha de
   base. Sem bold e em caixa baixa: são mobília do gráfico, não título.
   (Foi assim que foi pro ar na página, em 14/09.) */
.corpo{position:relative}
.graf{position:relative;padding-bottom:16px}
.graf svg{display:block;width:100%;height:auto;overflow:visible}
.eixoy,.tempo,.marca{position:absolute;font-family:var(--fd);font-weight:400;
  font-size:.62rem;line-height:1;letter-spacing:.06em;white-space:nowrap;pointer-events:none}
.eixoy,.marca{top:0;display:flex;align-items:center;
  writing-mode:vertical-rl;transform:rotate(180deg)}
.eixoy{bottom:16px}
.marca{bottom:0}
/* em escrita vertical o eixo principal do flex é o vertical, e o
   rotate(180deg) inverte as pontas: flex-end é o TOPO na tela.
   "vendas" fica no meio da sua linha, "lançamento" no topo da dela. */
.eixoy{justify-content:center}
.marca{justify-content:flex-end}
.eixoy{left:-24px;color:var(--dim)}
.marca{right:85.625%;margin-right:6px;color:var(--ac);opacity:.85}
.tempo{right:0;bottom:0;color:var(--dim)}
@media(max-width:560px){
  .eixoy{left:-20px}
  .eixoy,.marca,.tempo{font-size:.55rem;letter-spacing:.02em}
  .marca{margin-right:4px}
}

/* ── G1 · TRÊS FAIXAS, UM SÓ TEMPO ── */
.g1 .corpo{padding-left:26px}
.g1 .faixa + .faixa{margin-top:clamp(26px,3.6vw,40px)}
.g1 .q{margin:0 0 8px;font:700 clamp(.92rem,2vw,1.12rem)/1.25 var(--fd);letter-spacing:-.03em;
  color:var(--cor)}
.g1 .r{margin:8px 0 0;font-size:.95rem;line-height:1.4;color:var(--dim)}
.g1 .faixa.fim .q{font-size:clamp(1.05rem,2.5vw,1.4rem)}
.g1 .faixa.fim .r{color:var(--ac);font-size:clamp(1rem,2.2vw,1.2rem)}
.g1 .base{stroke:var(--ru);stroke-width:1}

/* ── G2 · UMA CURVA SÓ ── */
.g2 .corpo{padding-left:26px}
.g2 .rot{position:absolute;font:700 .72rem/1.28 var(--fd);letter-spacing:-.01em;
  white-space:nowrap;pointer-events:none}
.g2 .r1{color:#93A6B8}
.g2 .r2{color:#E0574A}
.g2 .r3{color:var(--ac)}
.g2 .veredito{margin:26px 0 0;text-align:center;font-family:var(--fs);font-style:italic;
  font-weight:500;color:var(--ac);font-size:clamp(1.3rem,3.2vw,1.9rem);
  text-shadow:0 0 30px rgba(234,184,45,.3)}
.g2 .leg{display:none;list-style:none;margin:18px 0 0;padding:0;gap:9px}
.g2 .leg li{display:flex;align-items:center;gap:10px;font:700 .82rem/1.2 var(--fd);
  letter-spacing:-.02em;color:var(--mut)}
.g2 .leg i{width:20px;height:2px;border-radius:2px;flex:none}
/* abaixo de 700px os rótulos em cima do gráfico se atropelam entre si e com o
   eixo. Viram legenda, que é o mesmo dado sem a colisão. */
@media(max-width:700px){.g2 .rot{display:none}.g2 .leg{display:grid}}

/* ── G3 · A FAIXA CHEIA ── */
.g3 .faixa{border-top:1px solid var(--ru);padding-block:clamp(24px,3.4vw,34px) 0}
.g3 .faixa:first-child{border-top:0;padding-top:0}
/* sangra até a borda do cartão: é isso que faz a faixa ser cheia */
.g3 .desenho{margin:16px calc(-1 * var(--pad)) 0;pointer-events:none}
.g3 .desenho svg{height:clamp(78px,12vw,112px)}
.g3 .txt{max-width:34ch}
.g3 .q{margin:0;font:700 clamp(.95rem,2.1vw,1.2rem)/1.25 var(--fd);letter-spacing:-.03em;
  color:var(--cor)}
.g3 .r{margin:7px 0 0;font-size:.95rem;line-height:1.4;color:var(--dim)}
.g3 .faixa.fim .q{font-size:clamp(1.15rem,2.8vw,1.55rem)}
.g3 .faixa.fim .r{font-family:var(--fs);font-style:italic;font-weight:500;color:var(--ac);
  font-size:clamp(1.25rem,2.9vw,1.6rem)}
"""

TIT = '<h2 class="tit">A conta que <span class="risco">ninguém</span> te conta</h2>'
MIUDO = ('<p class="miudo">Não é gráfico de dados: é o desenho do que acontece '
         'com as vendas do livro depois que o lançamento acaba.</p>')
ROTULOS = ('<span class="eixoy">vendas</span><span class="marca">lançamento</span>'
           '<span class="tempo">tempo</span>')
# o pontilhado do lançamento, em coordenadas do gráfico
RETA = ('<line x1="1" y1="2" x2="1" y2="104" stroke="#2C2C33" stroke-width="1"></line>'
        '<line x1="1" y1="104" x2="640" y2="104" stroke="#2C2C33" stroke-width="1"></line>'
        '<line x1="92" y1="2" x2="92" y2="104" stroke="rgba(234,184,45,.34)" stroke-width="1" '
        'stroke-dasharray="4 5"></line>')



def _defs():
    """um gradiente de área por conta"""
    g = []
    for i, cor in enumerate(COR):
        g.append('<linearGradient id="gr%d" x1="0" y1="0" x2="0" y2="1">'
                 '<stop offset="0" stop-color="%s" stop-opacity="%s"></stop>'
                 '<stop offset="1" stop-color="%s" stop-opacity="0"></stop></linearGradient>'
                 % (i, cor, ('.13', '.20', '.26')[i], cor))
    return '<defs>%s</defs>' % ''.join(g)


def _traco(i, ghost=False, fill=True):
    cor = COR[i] if not ghost else COR[i]
    largura = 1.5 if ghost else (2.6 if i == 2 else 2)
    op = ' stroke-opacity=".34"' if ghost else ''
    brilho = (' filter="drop-shadow(0 0 9px rgba(234,184,45,.5))"'
              if (i == 2 and not ghost) else '')
    s = ''
    if fill and not ghost:
        s += '<path d="%s" fill="url(#gr%d)"></path>' % (area(P[i]), i)
    s += ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round"%s%s>'
          '</path>' % (P[i], cor, largura, op, brilho))
    if not ghost:
        if i == 2:
            s += ('<circle cx="638" cy="%s" r="4.5" fill="%s"'
                  ' filter="drop-shadow(0 0 10px rgba(234,184,45,.85))"></circle>' % (FIM_Y[i], COR[i]))
        else:
            s += ('<circle cx="632" cy="%s" r="3.5" fill="var(--pa)" stroke="%s"'
                  ' stroke-width="1.5"></circle>' % (FIM_Y[i], COR[i]))
    return s


# ─────────────────────────── G1 ───────────────────────────
def g1():
    fx = []
    for i, (q, r) in enumerate(C):
        fim = ' fim' if i == 2 else ''
        # AS CURVAS SE SOMAM: cada faixa desenha todas as anteriores por baixo,
        # apagadas mas na cor delas. Quem chega na terceira está vendo as três
        # no mesmo eixo, e a ultrapassagem acontece na frente da pessoa em vez
        # de ser afirmada por escrito.
        fantasmas = ''.join(_traco(j, ghost=True) for j in range(i))
        fx.append(
            '<div class="faixa%s" style="--cor:%s"><p class="q">%s</p>'
            '<div class="graf">%s'
            '<svg viewBox="0 0 640 112" fill="none" aria-hidden="true">%s'
            '<line class="base" x1="0" y1="104" x2="640" y2="104"></line>%s%s%s</svg>'
            '</div><p class="r">%s</p></div>'
            % (fim, COR_ROT[i], q, ROTULOS,
               _defs() if i == 0 else '', RETA, fantasmas, _traco(i), r))
    return ('<div class="g1"><div class="corpo">%s</div>%s</div>'
            % (''.join(fx), MIUDO))


# ─────────────────────────── G2 ───────────────────────────
# os rótulos entram em HTML, não em <text>: dentro do SVG eles esticariam
# junto com o viewBox e virariam outro tamanho em cada largura de tela.
ROTS = [
    ('r1', 62.0, 86.0, 'Livro bom +<br>lançamento ruim'),
    ('r2', 26.5, 10.0, 'Livro ruim +<br>lançamento bom'),
    ('r3', 70.0, 8.0,  'Livro bom +<br>lançamento bom'),
]


def g2():
    tracos = (_defs() + '<line x1="0" y1="104" x2="640" y2="104" stroke="#2C2C33"></line>' + RETA)
    for i in (0, 1, 2):
        tracos += _traco(i)
    rot = ''.join('<span class="rot %s" style="left:%.1f%%;top:%.1f%%">%s</span>' % r for r in ROTS)
    leg = ''.join('<li><i style="background:%s"></i>%s</li>' % (COR[i], C[i][0])
                  for i in (0, 1, 2))
    return ('<div class="g2"><div class="corpo"><div class="graf">%s'
            '<svg viewBox="0 0 640 112" fill="none" aria-hidden="true">%s</svg>%s</div></div>'
            '<ul class="leg">%s</ul>'
            '<p class="veredito">%s</p>%s</div>'
            % (ROTULOS, tracos, rot, leg, C[2][1], MIUDO))


# ─────────────────────────── G3 ───────────────────────────
def g3():
    fx = []
    for i, (q, r) in enumerate(C):
        fim = ' fim' if i == 2 else ''
        # o texto vem ANTES do desenho: com o desenho em cima, a curva parecia
        # pertencer à conta de cima e o bloco perdia o pé.
        fx.append(
            '<div class="faixa%s" style="--cor:%s">'
            '<div class="txt"><p class="q">%s</p><p class="r">%s</p></div>'
            '<div class="desenho">'
            '<svg viewBox="0 0 640 104" preserveAspectRatio="none" fill="none" aria-hidden="true">'
            '%s%s</svg></div></div>'
            % (fim, COR_ROT[i], q, r, _defs() if i == 0 else '', _traco(i)))
    return '<div class="g3">%s</div>%s' % (''.join(fx), MIUDO)


RUMOS = [
    ('G1', 'Três faixas, um só tempo',
     'As três curvas empilhadas no mesmo sistema de eixos, e uma linha pontilhada '
     'de lançamento atravessando as três no mesmo ponto. É isso que transforma três '
     'rabiscos numa história só. Na terceira faixa as duas primeiras aparecem de '
     'fantasma, e dá pra ver a ultrapassagem acontecer.', g1),
    ('G2', 'Uma curva só',
     'Os três traços no mesmo gráfico. O pico do livro ruim é o mais alto da página, '
     'e mesmo assim ele termina embaixo: a comparação deixa de ser argumento e vira '
     'evidência. Só a última conta ainda precisa de frase, porque as outras duas o '
     'desenho já respondeu.', g2),
    ('G3', 'A faixa cheia',
     'A curva sai da caixa e vira o fundo da própria linha de texto. Menos gráfico, '
     'mais atmosfera: a pessoa lê a frase em cima do desenho do que está sendo dito.',
     g3),
]

FONTES = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
          '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
          '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700'
          '&family=Space+Grotesk:wght@400;500;700'
          '&family=Fraunces:ital,opsz,wght@1,9..144,500&display=swap" rel="stylesheet">')
TITULO = '<title>A curva, três acabamentos</title>'
HEAD = (TITULO + FONTES + '<style>%s</style>') if ARTIFACT else (
    '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    + TITULO + FONTES + '<style>%s</style></head><body>')


def doc():
    p = [HEAD % BASE, '<div class="w"><header><h1>A curva, três acabamentos</h1>'
         '<p>O mecanismo está escolhido: a conta vira a vida do livro no tempo. '
         'O que muda aqui é o <b>desenho</b>.</p>'
         '<p>As três curvas são idênticas nos três acabamentos e vivem no mesmo '
         'sistema de eixos, porque é aí que está a frase da seção: <b>o pico do '
         'lançamento bom com livro ruim é o mais alto da página, e ainda assim ele '
         'termina embaixo de todos.</b></p></header>']
    for letra, nome, tese, fn in RUMOS:
        p.append('<section class="item"><div class="cab"><span class="no">%s</span><h2>%s</h2></div>'
                 '<p class="tese">%s</p><div class="palco">%s%s</div></section>'
                 % (letra, nome, tese, TIT, fn()))
    p.append('<footer>Protótipo de design. Nenhuma versão está no ar. Gerado por '
             '<code>gera_curva.py</code>.</footer></div>')
    if not ARTIFACT:
        p.append('</body></html>')
    return ''.join(p)


io.open(OUT, 'w', encoding='utf-8').write(doc())
print('%s  (%s bytes)' % (OUT, format(os.path.getsize(OUT), ',d')))
