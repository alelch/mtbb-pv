# -*- coding: utf-8 -*-
"""
A conta, OITO MECANISMOS diferentes (3ª rodada).

    python3 gera_conta3.py [destino.html]

A 1ª rodada deu dez arranjos do mesmo empilhamento e a 2ª deu seis
calibragens de escala. O cliente disse, com razão, que variação em GRAU não
é variação. Aqui cada versão muda o MECANISMO: o que faz a conta ser
entendida é outro em cada uma (uma grade, uma tabela, um eixo de alinhamento,
um interruptor, um objeto, a cor, um gráfico).

⚠️ ORDEM DOS TERMOS (corrigida aqui e na página, 14/09): o LIVRO vem sempre
primeiro e o LANÇAMENTO sempre depois do +. Antes a 1ª linha era
"livro + lançamento" e as outras duas "lançamento + livro", e isso quebrava
a leitura: o olho não sabia qual dos dois estava sendo julgado.

⚠️ A conta "livro ruim + lançamento ruim" NÃO EXISTE na copy da página. Ela
só aparece na versão D (interruptores), onde o lead pode chegar nela sozinho,
e ali a frase é COPY NOVA, marcada como tal. Precisa passar pela Dany antes
de qualquer uma dessas versões ir pro ar.
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_args = [a for a in sys.argv[1:] if not a.startswith('--')]
OUT = _args[0] if _args else os.path.join(HERE, 'conta3.html')

# (livro, lançamento, resultado)
C = [
    ('bom',  'ruim', 'Ninguém descobre.'),
    ('ruim', 'bom',  'Vende no lançamento. Depois, esquecido.'),
    ('bom',  'bom',  'Muda a vida do autor.'),
]

def cond(i):
    l, n, _ = C[i]
    return 'Livro %s + lançamento %s' % (l, n)

def cond_cor(i, tag='span'):
    """a condição com bom em âmbar e ruim em vermelho"""
    l, n, _ = C[i]
    return ('Livro <%s class="v-%s">%s</%s> <i class="op">+</i> lançamento '
            '<%s class="v-%s">%s</%s>') % (tag, l, l, tag, tag, n, n, tag)

BASE = r"""
:root{
  /* a paleta nova da página (14/09): os dois fundos afastados */
  --pa:#0B0B0D;--pa2:#191920;--ink:#EFEDE8;--mut:#9A958D;--dim:#868178;--ru:#2C2C33;
  --ac:#EAB82D;--rx:#E0574A;--apaga:#55524D;
  --ff:'DM Sans',system-ui,sans-serif;--fd:'Space Grotesk','DM Sans',sans-serif;
  --fs:Fraunces,Georgia,serif}
*{box-sizing:border-box}
body{margin:0;background:#0F0F11;color:var(--ink);font:400 16px/1.6 var(--ff);
  -webkit-font-smoothing:antialiased}
.w{max-width:1120px;margin:0 auto;padding:0 22px}
h1,h2,h3{margin:0;font-family:var(--fd);font-weight:700;letter-spacing:-.03em;line-height:1.1}
.serifa,.fs{font-family:var(--fs);font-style:italic;font-weight:500;letter-spacing:-.02em}
header{padding:54px 0 32px}
header h1{font-size:clamp(1.9rem,4vw,2.8rem)}
header p{margin:16px 0 0;max-width:70ch;color:var(--mut)}
header p b{color:var(--ink)}
.aviso{margin:18px 0 0;padding:14px 18px;border-left:2px solid var(--ac);
  background:rgba(234,184,45,.05);font-size:.94rem;max-width:70ch}
.aviso.vermelho{border-color:var(--rx);background:rgba(224,87,74,.06)}
.item{border-top:1px solid var(--ru);padding:46px 0 10px}
.cab{display:flex;align-items:baseline;gap:12px;margin:0 0 6px}
.cab .no{font-family:var(--fd);font-weight:700;font-size:.78rem;letter-spacing:.16em;color:var(--ac)}
.cab h2{font-size:1.25rem}
.tese{margin:0 0 26px;color:var(--mut);max-width:74ch;font-size:.95rem}
/* o palco é o fundo real da seção, pra comparação ser honesta */
.palco{background:var(--pa);border:1px solid var(--ru);border-radius:16px;
  padding:clamp(34px,6vw,64px) clamp(18px,4vw,44px);overflow:hidden}
.palco > .tit{text-align:center;margin:0 0 clamp(30px,5vw,54px);
  font-size:clamp(1.5rem,3.4vw,2.3rem)}
.tit .risco{position:relative;white-space:nowrap}
.tit .risco:after{content:"";position:absolute;left:-2px;right:-2px;bottom:-.08em;height:.09em;
  background:var(--ac);border-radius:2px}
footer{padding:40px 0 70px;color:var(--dim);font-size:.85rem;border-top:1px solid var(--ru);margin-top:46px}

/* cores dos julgamentos, comuns a quase todas */
.v-bom{color:var(--ac)}
.v-ruim{color:var(--rx)}
.op{font-style:normal;color:var(--dim);font-weight:400}

/* ─────────── A · MATRIZ ─────────── */
.mx{display:grid;grid-template-columns:auto 1fr 1fr;max-width:820px;margin:0 auto}
.mx .canto{border:0}
.mx .eixo{font:700 .68rem/1.2 var(--fd);letter-spacing:.15em;text-transform:uppercase;
  color:var(--dim);display:flex;align-items:center;justify-content:center;padding:0 0 16px}
.mx .eixoy{writing-mode:vertical-rl;transform:rotate(180deg);padding:0 16px 0 0}
.mx .cel{border:1px solid var(--ru);padding:clamp(18px,3vw,28px);min-height:150px;
  display:flex;flex-direction:column;justify-content:center;gap:10px}
.mx .cel + .cel{border-left:0}
.mx .fila2 .cel{border-top:0}
.mx .cel .q{font:700 .92rem/1.32 var(--fd);letter-spacing:-.02em;color:var(--mut);margin:0}
.mx .cel .r{margin:0;font-size:1.02rem;line-height:1.35;color:var(--ink)}
.mx .cel.fraca .r{color:var(--mut)}
.mx .cel.vazia{color:var(--apaga);align-items:center;justify-content:center;font-size:1.6rem}
.mx .cel.ok{border-color:rgba(234,184,45,.5);
  background:radial-gradient(120% 120% at 70% 30%,rgba(234,184,45,.12),rgba(234,184,45,0) 70%)}
.mx .cel.ok .q{color:var(--ink)}
.mx .cel.ok .r{font-family:var(--fs);font-style:italic;font-weight:500;
  font-size:clamp(1.25rem,2.6vw,1.6rem);color:var(--ac);text-shadow:0 0 26px rgba(234,184,45,.3)}
@media(max-width:620px){
  .mx .cel{min-height:126px;padding:14px}
  .mx .cel .q{font-size:.76rem}.mx .cel .r{font-size:.86rem}
  .mx .eixo{font-size:.58rem;letter-spacing:.1em}
}

/* ─────────── B · PLACAR ─────────── */
.pl{width:100%;max-width:800px;margin:0 auto;border-collapse:collapse;text-align:left}
.pl th{font:700 .68rem/1 var(--fd);letter-spacing:.16em;text-transform:uppercase;color:var(--dim);
  padding:0 14px 15px 0;border-bottom:1px solid var(--ru);font-weight:700}
.pl td{padding:19px 14px 19px 0;border-bottom:1px solid var(--ru);vertical-align:middle}
.pl td:last-child,.pl th:last-child{padding-right:0}
.ch{display:inline-block;font:700 .78rem/1 var(--fd);letter-spacing:.01em;padding:7px 13px;
  border-radius:999px;border:1px solid}
.ch.bom{color:var(--ac);border-color:rgba(234,184,45,.42);background:rgba(234,184,45,.09)}
.ch.ruim{color:var(--rx);border-color:rgba(224,87,74,.36);background:rgba(224,87,74,.09)}
.pl .res{color:var(--mut);font-size:.98rem}
.pl tr.fim td{border-bottom:0;padding-top:26px;padding-bottom:0}
.pl tr.fim .res{font-family:var(--fs);font-style:italic;font-weight:500;color:var(--ac);
  font-size:clamp(1.3rem,3vw,1.95rem);text-shadow:0 0 30px rgba(234,184,45,.26)}
@media(max-width:560px){
  .pl th{font-size:.58rem;letter-spacing:.1em}
  .ch{font-size:.68rem;padding:6px 9px}
  .pl td{padding:14px 8px 14px 0}.pl .res{font-size:.9rem}
}

/* ─────────── C · EQUAÇÃO ALINHADA ─────────── */
.eq{max-width:860px;margin:0 auto}
.eq .li{padding:clamp(20px,3vw,30px) 0;border-bottom:1px solid var(--ru)}
.eq .li:last-child{border-bottom:0;padding-bottom:0}
.eq .cd{display:grid;grid-template-columns:1fr auto 1fr;align-items:baseline;
  gap:clamp(12px,2.4vw,26px);font-family:var(--fd);font-weight:700;letter-spacing:-.03em;
  line-height:1.15;font-size:clamp(1rem,2.4vw,1.5rem);color:var(--mut)}
.eq .cd .a{text-align:right}
.eq .cd .b{text-align:left}
.eq .cd .mais{color:var(--ac);font-weight:400;font-size:1.25em;line-height:1}
.eq .rs{margin:14px 0 0;text-align:center;color:var(--mut);font-size:1rem}
.eq .li.fim .cd{font-size:clamp(1.35rem,3.6vw,2.35rem);color:var(--ink)}
.eq .li.fim .rs{margin-top:18px;font-family:var(--fs);font-style:italic;font-weight:500;
  color:var(--ac);font-size:clamp(1.4rem,3.6vw,2.1rem);text-shadow:0 0 30px rgba(234,184,45,.28)}

/* ─────────── D · INTERRUPTORES ─────────── */
.sw{max-width:640px;margin:0 auto}
.sw .linha{display:flex;align-items:center;justify-content:space-between;gap:18px;
  padding:18px 0;border-bottom:1px solid var(--ru)}
.sw .rot{font:700 .74rem/1.2 var(--fd);letter-spacing:.15em;text-transform:uppercase;color:var(--dim)}
.tog{display:inline-flex;border:1px solid var(--ru);border-radius:999px;padding:3px;gap:3px}
.tog button{appearance:none;border:0;background:none;cursor:pointer;color:var(--dim);
  font:700 .88rem/1 var(--fd);letter-spacing:-.01em;padding:11px 20px;border-radius:999px;
  transition:background .2s ease,color .2s ease}
.tog button[data-v="ruim"].on{background:rgba(224,87,74,.16);color:var(--rx)}
.tog button[data-v="bom"].on{background:rgba(234,184,45,.16);color:var(--ac)}
.sw .placa{margin:34px 0 0;text-align:center;min-height:120px;display:flex;
  flex-direction:column;align-items:center;justify-content:center;gap:10px;
  border-radius:14px;padding:26px 18px;transition:background .45s ease,box-shadow .45s ease}
.sw .placa .q{margin:0;font:700 .74rem/1.2 var(--fd);letter-spacing:.15em;text-transform:uppercase;
  color:var(--dim)}
.sw .placa .r{margin:0;font-size:clamp(1.15rem,3vw,1.7rem);line-height:1.25;color:var(--mut);
  font-family:var(--fd);font-weight:700;letter-spacing:-.03em}
.sw.ganhou .placa{background:radial-gradient(90% 130% at 50% 40%,rgba(234,184,45,.14),rgba(234,184,45,0) 72%)}
.sw.ganhou .placa .r{font-family:var(--fs);font-style:italic;font-weight:500;
  font-size:clamp(1.5rem,4vw,2.4rem);color:var(--ac);text-shadow:0 0 34px rgba(234,184,45,.34)}
.sw .nova{margin:14px 0 0;text-align:center;font-size:.76rem;color:var(--rx);opacity:0;
  transition:opacity .3s ease}
.sw.copianova .nova{opacity:1}
@media(max-width:480px){
  .sw .linha{flex-direction:column;align-items:flex-start;gap:12px}
  .tog button{padding:10px 16px}
}

/* ─────────── E · LOMBADAS ─────────── */
.est{display:flex;align-items:flex-end;justify-content:center;gap:clamp(16px,5vw,56px);
  padding-bottom:26px;position:relative}
.est:after{content:"";position:absolute;left:8%;right:8%;bottom:20px;height:1px;
  background:linear-gradient(90deg,transparent,var(--ru) 18%,var(--ru) 82%,transparent)}
.pe{display:flex;flex-direction:column;align-items:center;gap:16px;max-width:180px}
.lomb{width:clamp(56px,11vw,86px);height:clamp(190px,30vw,268px);border-radius:2px 5px 5px 2px;
  display:flex;align-items:center;justify-content:center;position:relative}
.lomb span{writing-mode:vertical-rl;transform:rotate(180deg);font:700 .76rem/1 var(--fd);
  letter-spacing:.06em;white-space:nowrap}
.lomb.l1{background:#141417;border:1px solid #1D1D21}
.lomb.l1 span{color:#2E2E32}
.lomb.l2{background:linear-gradient(180deg,#3B382F,#131315 78%);border:1px solid #2A2823}
.lomb.l2 span{color:#7D786E}
.lomb.l3{background:linear-gradient(180deg,#F0C544,#C89A17);border:1px solid #F5D77A;box-shadow:0 0 46px rgba(234,184,45,.3)}
.lomb.l3 span{color:#141312}
.est .pe .cap{text-align:center}
.est .pe .q{margin:0;font:700 .76rem/1.3 var(--fd);letter-spacing:-.01em;color:var(--mut)}
.est .pe .r{margin:6px 0 0;font-size:.92rem;line-height:1.35;color:var(--dim)}
.est .pe.fim .r{font-family:var(--fs);font-style:italic;font-weight:500;color:var(--ac);
  font-size:clamp(1.05rem,2.4vw,1.3rem)}
@media(max-width:560px){.lomb span{font-size:.62rem}.est .pe .q{font-size:.66rem}.est .pe .r{font-size:.76rem}}

/* ─────────── F · CORES ─────────── */
.cr{max-width:720px;margin:0 auto;display:flex;flex-direction:column;gap:clamp(26px,4vw,40px)}
.cr .li{text-align:center}
.cr .cd{margin:0;font-family:var(--fd);font-weight:700;letter-spacing:-.03em;
  font-size:clamp(1.1rem,2.7vw,1.6rem);line-height:1.25;color:var(--mut)}
.cr .cd .v-ruim{text-decoration:line-through;text-decoration-thickness:2px;
  text-decoration-color:rgba(224,87,74,.75)}
.cr .rs{margin:8px 0 0;font-size:clamp(1rem,2.2vw,1.2rem);color:var(--dim)}
.cr .li.fim .rs{font-family:var(--fs);font-style:italic;font-weight:500;color:var(--ac);
  font-size:clamp(1.35rem,3.2vw,1.9rem);text-shadow:0 0 30px rgba(234,184,45,.28)}

/* ─────────── G · CURVA ─────────── */
.cv{max-width:820px;margin:0 auto;display:flex;flex-direction:column;gap:clamp(24px,3.6vw,38px)}
.cv .li{display:grid;grid-template-columns:1fr minmax(180px,320px);gap:clamp(16px,3vw,34px);
  align-items:center}
.cv .q{margin:0;font:700 clamp(.95rem,2.2vw,1.2rem)/1.3 var(--fd);letter-spacing:-.03em;color:var(--mut)}
.cv .r{margin:6px 0 0;font-size:.95rem;line-height:1.4;color:var(--dim)}
.cv .li.fim .q{color:var(--ink);font-size:clamp(1.1rem,2.8vw,1.5rem)}
.cv .li.fim .r{font-family:var(--fs);font-style:italic;font-weight:500;color:var(--ac);
  font-size:clamp(1.2rem,2.8vw,1.5rem)}
.cv svg{width:100%;height:auto;display:block;overflow:visible}
.cv .eixo{stroke:var(--ru);stroke-width:1}
.cv .tempo{font:700 .6rem/1 var(--fd);letter-spacing:.16em;text-transform:uppercase;
  fill:var(--apaga)}
@media(max-width:620px){.cv .li{grid-template-columns:1fr}}

/* ─────────── H · ESCALA (a que está no ar) ─────────── */
.es{position:relative;text-align:center}
.es .luz{position:absolute;left:50%;top:64%;width:min(760px,112%);height:340px;
  transform:translate(-50%,-50%);pointer-events:none;
  background:radial-gradient(52% 50% at 50% 50%,rgba(234,184,45,.13),rgba(234,184,45,0) 70%)}
.es .li{position:relative}
.es .li + .li{margin-top:clamp(22px,3.4vw,36px)}
.es .q{margin:0;font-family:var(--fd);font-weight:700;letter-spacing:-.03em;line-height:1.16}
.es .r{margin:5px 0 0;line-height:1.4}
.es .um .q{font-size:1rem;color:var(--rx)}
.es .um .r{font-size:.9rem;color:#B5736B}
.es .dois .q{font-size:clamp(1.15rem,2.2vw,1.35rem);color:#ACA69B}
.es .dois .r{font-size:1rem;color:var(--mut)}
.es .tres{margin-top:clamp(34px,5vw,54px)}
.es .tres .q{font-size:clamp(1.8rem,4.6vw,3rem);color:var(--ink)}
.es .tres .r{margin-top:10px;font-family:var(--fs);font-style:italic;font-weight:500;
  font-size:clamp(1.4rem,3.4vw,2rem);color:var(--ac);text-shadow:0 0 34px rgba(234,184,45,.32)}
.es .tres:after{content:"";display:block;width:min(340px,66%);height:1px;margin:26px auto 0;
  background:linear-gradient(90deg,transparent,rgba(234,184,45,.5),transparent)}
"""

TIT = '<h2 class="tit">A conta que <span class="risco">ninguém</span> te conta</h2>'


def a_matriz():
    return """<div class="mx">
  <div class="canto"></div>
  <div class="eixo">Lançamento ruim</div>
  <div class="eixo">Lançamento bom</div>
  <div class="eixo eixoy">Livro bom</div>
  <div class="cel"><p class="q">%s</p><p class="r">%s</p></div>
  <div class="cel ok"><p class="q">%s</p><p class="r">%s</p></div>
  <div class="eixo eixoy fila2">Livro ruim</div>
  <div class="cel vazia fila2" aria-hidden="true">·</div>
  <div class="cel fraca fila2"><p class="q">%s</p><p class="r">%s</p></div>
</div>""" % (cond(0), C[0][2], cond(2), C[2][2], cond(1), C[1][2])


def b_placar():
    linhas = []
    for i, (l, n, r) in enumerate(C):
        fim = ' class="fim"' if i == 2 else ''
        linhas.append(
            '<tr%s><td><span class="ch %s">%s</span></td>'
            '<td><span class="ch %s">%s</span></td>'
            '<td class="res">%s</td></tr>' % (fim, l, l, n, n, r))
    return ('<table class="pl"><thead><tr><th>O livro</th><th>O lançamento</th>'
            '<th>O que acontece</th></tr></thead><tbody>%s</tbody></table>'
            % ''.join(linhas))


def c_equacao():
    linhas = []
    for i, (l, n, r) in enumerate(C):
        fim = ' fim' if i == 2 else ''
        linhas.append(
            '<div class="li%s"><div class="cd"><span class="a">Livro <b class="v-%s">%s</b></span>'
            '<span class="mais">+</span>'
            '<span class="b">lançamento <b class="v-%s">%s</b></span></div>'
            '<p class="rs">%s</p></div>' % (fim, l, l, n, n, r))
    return '<div class="eq">%s</div>' % ''.join(linhas)


def d_interruptores():
    return """<div class="sw" id="sw">
  <div class="linha"><span class="rot">O seu livro</span>
    <span class="tog" data-g="livro">
      <button type="button" data-v="ruim">ruim</button>
      <button type="button" data-v="bom" class="on">bom</button></span></div>
  <div class="linha"><span class="rot">O seu lançamento</span>
    <span class="tog" data-g="lanc">
      <button type="button" data-v="ruim" class="on">ruim</button>
      <button type="button" data-v="bom">bom</button></span></div>
  <div class="placa"><p class="q" id="swq"></p><p class="r" id="swr"></p></div>
  <p class="nova">⚠️ copy nova: esta combinação não existe na página. Precisa passar pela Dany.</p>
</div>"""


def e_lombadas():
    pes = []
    cls = ['l1', 'l2', 'l3']
    rot = ['ninguém descobre', 'vende e some', 'muda a vida do autor']
    ordem = [0, 1, 2]
    for k, i in enumerate(ordem):
        fim = ' fim' if i == 2 else ''
        pes.append('<div class="pe%s"><span class="lomb %s"><span>%s</span></span>'
                   '<span class="cap"><p class="q">%s</p><p class="r">%s</p></span></div>'
                   % (fim, cls[k], rot[k], cond(i), C[i][2]))
    return '<div class="est">%s</div>' % ''.join(pes)


def f_cores():
    linhas = []
    for i, (l, n, r) in enumerate(C):
        fim = ' fim' if i == 2 else ''
        linhas.append('<div class="li%s"><p class="cd">%s</p><p class="rs">%s</p></div>'
                      % (fim, cond_cor(i, 'b'), r))
    return '<div class="cr">%s</div>' % ''.join(linhas)


CURVAS = [
    ('M2 50 C70 51 150 52 318 53', '#6A665F', 0),
    ('M2 58 C26 58 40 6 66 6 C96 6 112 52 176 56 C242 60 280 58 318 58', 'var(--mut)', 0),
    ('M2 58 C62 55 112 45 162 33 C216 20 266 10 318 2', 'var(--ac)', 1),
]


def g_curva():
    linhas = []
    for i, (l, n, r) in enumerate(C):
        d, cor, brilha = CURVAS[i]
        fim = ' fim' if i == 2 else ''
        filtro = (' style="filter:drop-shadow(0 0 10px rgba(234,184,45,.55))"' if brilha else '')
        linhas.append(
            '<div class="li%s"><div><p class="q">%s</p><p class="r">%s</p></div>'
            '<svg viewBox="0 0 320 70" fill="none" aria-hidden="true">'
            '<line class="eixo" x1="2" y1="62" x2="318" y2="62"></line>'
            '<path d="%s" stroke="%s" stroke-width="2" stroke-linecap="round"%s></path>'
            '<text class="tempo" x="2" y="70">tempo</text></svg></div>'
            % (fim, cond(i), r, d, cor, filtro))
    return '<div class="cv">%s</div>' % ''.join(linhas)


def h_escala():
    nomes = ['um', 'dois', 'tres']
    linhas = ['<span class="luz" aria-hidden="true"></span>']
    for i, (l, n, r) in enumerate(C):
        linhas.append('<div class="li %s"><p class="q">%s</p><p class="r">%s</p></div>'
                      % (nomes[i], cond(i), r))
    return '<div class="es">%s</div>' % ''.join(linhas)


RUMOS = [
    ('A', 'Matriz', 'A conta vira uma grade de duas entradas: o livro num eixo, o '
     'lançamento no outro. A lógica deixa de ser lida e passa a ser vista, e a '
     'casa que ninguém preenche (ruim + ruim) fica ali, vazia, sem precisar de '
     'frase. É o arranjo mais honesto do argumento.', a_matriz),
    ('B', 'Placar', 'Uma tabela de três colunas: o livro, o lançamento, o que '
     'acontece. Quem lê varre a coluna do meio e entende sozinho por que só uma '
     'linha acende. Formato de relatório, que é o tom de quem diagnostica.', b_placar),
    ('C', 'Equação alinhada', 'Nada de caixa nem de cor pra separar: quem organiza '
     'é o alinhamento. Os três "+" caem no mesmo eixo vertical e o olho desce por '
     'ele. Suíço, silencioso, e o único que cresce é o último.', c_equacao),
    ('D', 'Interruptores', 'O lead mexe. Dois botões, livro e lançamento, e o '
     'veredito muda na hora. A conta deixa de ser afirmada e passa a ser '
     'descoberta: ele tenta as combinações e vê que só uma acende. ⚠️ É o segundo '
     'momento interativo da página (o outro é o "Mostrar o erro") e os dois ficam '
     'a menos de uma tela de distância.', d_interruptores),
    ('E', 'Lombadas', 'Três livros na estante, que é a linguagem da casa. O '
     'primeiro está no escuro e ninguém lê o título. O segundo acende em cima e '
     'apaga embaixo. O terceiro brilha inteiro. O argumento vira objeto.', e_lombadas),
    ('F', 'Cores', 'Sem grade, sem tabela, sem escala: as três linhas têm o mesmo '
     'tamanho e quem faz a conta é a cor. "bom" em âmbar, "ruim" riscado em '
     'vermelho. O leitor soma sozinho e a última linha é a única com resposta em '
     'itálico.', f_cores),
    ('G', 'Curva', 'Cada conta vira a vida do livro no tempo. A primeira nunca '
     'sobe. A segunda dispara e morre. A terceira sobe e sai pela direita. É a '
     'tese da marca desenhada: o risco não é vender pouco, é ser esquecido.', g_curva),
    ('H', 'Escala (a que está no ar)', 'A versão atual, só com a ordem dos termos '
     'corrigida, pra comparação ser justa. O que organiza aqui é o tamanho: a '
     'primeira pequena e vermelha, a segunda no meio, a terceira grande e acesa.',
     h_escala),
]

JS = r"""
(function(){
  /* D · interruptores. O mapa é a copy da página; a combinação ruim+ruim não
     existe nela, então aparece marcada como copy nova. */
  var sw = document.getElementById('sw');
  if (!sw) return;
  var q = document.getElementById('swq'), r = document.getElementById('swr');
  var MAPA = {
    'bom|ruim':  ['Livro bom + lançamento ruim',  'Ninguém descobre.', 0],
    'ruim|bom':  ['Livro ruim + lançamento bom',  'Vende no lançamento. Depois, esquecido.', 0],
    'bom|bom':   ['Livro bom + lançamento bom',   'Muda a vida do autor.', 0],
    'ruim|ruim': ['Livro ruim + lançamento ruim', 'Nem chega a existir.', 1]
  };
  var estado = {livro:'bom', lanc:'ruim'};
  var pinta = function(){
    var k = estado.livro + '|' + estado.lanc, m = MAPA[k];
    q.textContent = m[0]; r.textContent = m[1];
    sw.classList.toggle('ganhou', k === 'bom|bom');
    sw.classList.toggle('copianova', !!m[2]);
  };
  [].forEach.call(sw.querySelectorAll('.tog'), function(t){
    t.addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      estado[t.getAttribute('data-g')] = b.getAttribute('data-v');
      [].forEach.call(t.querySelectorAll('button'), function(o){ o.classList.toggle('on', o === b); });
      pinta();
    });
  });
  pinta();
})();
"""

# --artifact: sem <html>/<head>/<body>, porque o Artifact embrulha o arquivo
# num esqueleto proprio (mesma convencao do build_prancha.py).
ARTIFACT = '--artifact' in sys.argv
FONTES = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
          '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
          '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700'
          '&family=Space+Grotesk:wght@400;500;700'
          '&family=Fraunces:ital,opsz,wght@1,9..144,500&display=swap" rel="stylesheet">')
TITULO = '<title>A conta, oito mecanismos</title>'
HEAD = (TITULO + FONTES + '<style>%s</style>') if ARTIFACT else (
    '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    + TITULO + FONTES + '<style>%s</style></head><body>')


def doc():
    partes = [HEAD % BASE]
    partes.append("""<div class="w"><header>
<h1>A conta, oito mecanismos</h1>
<p>Oito jeitos de fazer a mesma conta ser entendida. Não são oito ajustes do
mesmo empilhamento: em cada um, <b>a coisa que organiza a informação é outra</b>
(uma grade, uma tabela, um eixo de alinhamento, um interruptor, um objeto,
a cor, um gráfico). A copy é idêntica nas oito.</p>
<p class="aviso"><b>Ordem corrigida.</b> O livro vem sempre primeiro e o
lançamento sempre depois do +. Antes a primeira linha era livro + lançamento e
as outras duas vinham invertidas, e por isso a conta não fechava na leitura.
Isso já está no ar.</p>
<p class="aviso vermelho"><b>Uma ressalva de copy.</b> A conta
"livro ruim + lançamento ruim" não existe na página. Ela só aparece na versão D,
onde o lead pode chegar nela sozinho, e a frase ali é nova: precisa passar pela
Dany antes de qualquer versão ir pro ar.</p>
</header>""")
    for letra, nome, tese, fn in RUMOS:
        partes.append('<section class="item"><div class="cab"><span class="no">%s</span>'
                      '<h2>%s</h2></div><p class="tese">%s</p>'
                      '<div class="palco">%s%s</div></section>'
                      % (letra, nome, tese, TIT, fn()))
    partes.append('<footer>Protótipo de design. Nenhum botão leva a checkout e '
                  'nenhuma versão está no ar. Gerado por <code>gera_conta3.py</code>.'
                  '</footer></div><script>%s</script>%s'
                  % (JS, '' if ARTIFACT else '</body></html>'))
    return ''.join(partes)


io.open(OUT, 'w', encoding='utf-8').write(doc())
print('%s  (%s bytes)' % (OUT, format(os.path.getsize(OUT), ',d')))
