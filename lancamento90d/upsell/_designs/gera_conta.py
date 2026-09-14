# -*- coding: utf-8 -*-
"""
Dez maneiras de desenhar A CONTA (a matemágica) na página do upsell.

    python3 gera_conta.py [destino.html] [--artifact]

Regra que vale para as dez, e que é o motivo desta rodada: as três contas
ficam UMA EMBAIXO DA OUTRA. Lado a lado elas viram três cartões independentes
e a comparação se perde, que é justamente onde está o argumento.

As três têm a mesma estrutura de leitura: o par de condições, depois o
resultado. O que muda entre as versões é como o olho percorre isso.

Paleta e tipos são os da página real (Noite + Space Grotesk / DM Sans /
Fraunces). Aqui as fontes vêm do Google porque é uma prancha de comparação;
na página de verdade elas são auto-hospedadas.
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_args = [a for a in sys.argv[1:] if not a.startswith('--')]
OUT = _args[0] if _args else os.path.join(HERE, 'conta.html')

# (condição A, condição B, resultado, é a que ganha)
CONTAS = [
    ('Livro bom', 'lançamento ruim', 'Ninguém descobre.', 0),
    ('Lançamento bom', 'livro ruim', 'Vende no lançamento. Depois, esquecido.', 0),
    ('Lançamento bom', 'livro bom', 'Muda a vida do autor.', 1),
]

BASE = r"""
:root{--pa:#101012;--pa2:#17171A;--ink:#EFEDE8;--mut:#9A958D;--dim:#6B675F;--ru:#27272B;
  --ac:#EAB82D;--off:#F3F0E8;--offtx:#141312;
  --ff:'DM Sans',system-ui,sans-serif;--fd:'Space Grotesk','DM Sans',sans-serif;
  --fs:Fraunces,Georgia,serif;--r:14px}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);font:400 16px/1.6 var(--ff);
  -webkit-font-smoothing:antialiased}
.w{max-width:1120px;margin:0 auto;padding:0 22px}
h1,h2,h3{margin:0;font-family:var(--fd);font-weight:700;letter-spacing:-.03em;line-height:1.1}
.serifa{font-family:var(--fs);font-style:italic;font-weight:500;letter-spacing:-.02em}
.eyebrow{font-family:var(--fd);font-size:.78rem;font-weight:700;letter-spacing:.18em;
  text-transform:uppercase;color:var(--ac);margin:0 0 16px}
header{padding:56px 0 30px;border-bottom:1px solid var(--ru)}
header h1{font-size:clamp(1.9rem,4vw,3rem)}
header p{margin:18px 0 0;max-width:66ch;color:var(--mut)}
header p b{color:var(--ink)}
.item{border-bottom:1px solid var(--ru);padding:52px 0}
.cab{display:flex;align-items:baseline;gap:12px;margin:0 0 8px}
.cab .no{font-family:var(--fd);font-weight:700;font-size:.78rem;letter-spacing:.16em;color:var(--ac)}
.cab h2{font-size:1.3rem}
.tese{margin:0 0 30px;color:var(--mut);max-width:70ch;font-size:.97rem}
.palco{max-width:720px}
footer{padding:34px 0 60px;color:var(--dim);font-size:.85rem}
"""

# ═══════════════════════════════════════════════ as dez versões
V = []


def add(slug, nome, tese, css, html):
    V.append((slug, nome, tese, css, html))


# ── 01 Linha e fio ────────────────────────────────────────────
add('01', 'Linha e fio',
    'A tabela mais nua possível: par, igual, resultado. O fio âmbar e o resultado '
    'aceso marcam a única que presta. É o que menos chama atenção e o que mais deixa comparar.',
    r"""
.v1 .l{display:grid;grid-template-columns:1fr 34px 1fr;gap:0 18px;align-items:baseline;
  padding:20px 0;border-top:1px solid var(--ru)}
.v1 .l:last-child{border-bottom:1px solid var(--ru)}
.v1 .a{font-family:var(--fd);font-weight:700;font-size:1.05rem;letter-spacing:-.02em;color:var(--mut)}
.v1 .s{color:var(--dim);text-align:center}
.v1 .b{color:var(--dim);font-size:.97rem}
.v1 .ganha{border-top-color:var(--ac)}
.v1 .ganha .a{color:var(--ink)}
.v1 .ganha .b{color:var(--ac);font-weight:700}
""",
    lambda: '<div class="v1">' + ''.join(
        '<div class="l%s"><span class="a">%s + %s</span><span class="s">=</span>'
        '<span class="b">%s</span></div>' % (' ganha' if w else '', a, b, r)
        for a, b, r, w in CONTAS) + '</div>')


# ── 02 Conta armada ───────────────────────────────────────────
add('02', 'Conta armada',
    'Armada como no papel: as duas parcelas, o traço, e o resultado embaixo. '
    'É a versão que mais parece uma conta de verdade, que é o nome do bloco.',
    r"""
.v2 .c{padding:24px 0 26px;border-top:1px solid var(--ru)}
.v2 .c:last-child{border-bottom:1px solid var(--ru)}
.v2 .p{font-family:var(--fd);font-weight:700;font-size:1.16rem;letter-spacing:-.025em;
  color:var(--mut);text-align:right;max-width:420px}
.v2 .p.dois{position:relative;padding-bottom:10px;border-bottom:2px solid var(--ru)}
.v2 .p.dois:before{content:'+';position:absolute;left:0;color:var(--dim);font-weight:400}
.v2 .r{margin:12px 0 0;max-width:420px;text-align:right;color:var(--dim);font-size:1rem}
.v2 .ganha .p{color:var(--ink)}
.v2 .ganha .p.dois{border-bottom-color:var(--ac)}
.v2 .ganha .r{color:var(--ac);font-weight:700;font-size:1.12rem}
""",
    lambda: '<div class="v2">' + ''.join(
        '<div class="c%s"><p class="p">%s</p><p class="p dois">%s</p>'
        '<p class="r">%s</p></div>' % (' ganha' if w else '', a, b, r)
        for a, b, r, w in CONTAS) + '</div>')


# ── 03 Dois sinais ────────────────────────────────────────────
add('03', 'Dois sinais',
    'Cada linha mostra as DUAS variáveis como sinal: o livro e o lançamento, cada um '
    'certo ou errado. Só a terceira tem os dois sinais acesos, e isso se vê antes de ler.',
    r"""
.v3 .l{display:grid;grid-template-columns:auto 1fr;gap:20px;align-items:center;padding:18px 0;
  border-top:1px solid var(--ru)}
.v3 .l:last-child{border-bottom:1px solid var(--ru)}
.v3 .sig{display:flex;gap:8px}
.v3 .sig i{display:flex;align-items:center;gap:6px;padding:7px 11px;border-radius:9px;
  font-style:normal;font-family:var(--fd);font-weight:700;font-size:.78rem;letter-spacing:.04em;
  border:1px solid var(--ru);color:var(--dim);white-space:nowrap}
.v3 .sig i:before{content:'✗';font-size:.9rem}
.v3 .sig i.ok{border-color:var(--ac);color:var(--ac);background:rgba(234,184,45,.07)}
.v3 .sig i.ok:before{content:'✓'}
.v3 .a{font-family:var(--fd);font-weight:700;font-size:1.02rem;letter-spacing:-.02em;color:var(--mut)}
.v3 .b{margin:4px 0 0;color:var(--dim);font-size:.95rem}
.v3 .ganha{border-top-color:var(--ac)}
.v3 .ganha .a{color:var(--ink)}
.v3 .ganha .b{color:var(--ac);font-weight:700}
""",
    lambda: '<div class="v3">' + ''.join(
        '<div class="l%s"><span class="sig"><i class="%s">Livro</i>'
        '<i class="%s">Lançamento</i></span>'
        '<div><p class="a">%s + %s</p><p class="b">%s</p></div></div>'
        % (' ganha' if w else '',
           'ok' if 'livro bom' in (a + ' ' + b).lower() else '',
           'ok' if 'lançamento bom' in (a + ' ' + b).lower() else '',
           a, b, r)
        for a, b, r, w in CONTAS) + '</div>')


# ── 04 Seta ───────────────────────────────────────────────────
add('04', 'Seta',
    'Troca o sinal de igual por uma seta: deixa de ser aritmética e vira consequência. '
    'A seta da terceira é a única cheia.',
    r"""
.v4 .l{display:grid;grid-template-columns:1fr auto 1fr;gap:0 22px;align-items:center;
  padding:22px 0;border-top:1px solid var(--ru)}
.v4 .l:last-child{border-bottom:1px solid var(--ru)}
.v4 .a{font-family:var(--fd);font-weight:700;font-size:1.05rem;letter-spacing:-.02em;color:var(--mut)}
.v4 .seta{width:52px;height:2px;background:var(--ru);position:relative}
.v4 .seta:after{content:'';position:absolute;right:-1px;top:-4px;border-left:9px solid var(--ru);
  border-top:5px solid transparent;border-bottom:5px solid transparent}
.v4 .b{color:var(--dim);font-size:.98rem}
.v4 .ganha .a{color:var(--ink)}
.v4 .ganha .seta{background:var(--ac);height:3px}
.v4 .ganha .seta:after{border-left-color:var(--ac);top:-5px;border-top-width:6px;border-bottom-width:6px}
.v4 .ganha .b{color:var(--ac);font-weight:700;font-size:1.08rem}
""",
    lambda: '<div class="v4">' + ''.join(
        '<div class="l%s"><span class="a">%s + %s</span><span class="seta"></span>'
        '<span class="b">%s</span></div>' % (' ganha' if w else '', a, b, r)
        for a, b, r, w in CONTAS) + '</div>')


# ── 05 Só tipo ────────────────────────────────────────────────
add('05', 'Só tipo',
    'Sem fio, sem caixa, sem sinal: só tipografia. As duas que falham ficam em cinza de '
    'apoio, a terceira sobe de corpo e vai pro itálico da marca. O contraste faz o trabalho.',
    r"""
.v5 .l{padding:16px 0}
.v5 .a{font-family:var(--fd);font-weight:700;font-size:clamp(1.1rem,2.2vw,1.4rem);
  letter-spacing:-.03em;color:#55524D;line-height:1.25}
.v5 .b{margin:2px 0 0;color:#44413D;font-size:1rem}
.v5 .ganha{padding-top:26px}
.v5 .ganha .a{color:var(--ink);font-size:clamp(1.5rem,3.2vw,2.1rem)}
.v5 .ganha .b{font-family:var(--fs);font-style:italic;font-weight:500;color:var(--ac);
  font-size:clamp(1.3rem,2.8vw,1.8rem);letter-spacing:-.02em;margin-top:6px}
""",
    lambda: '<div class="v5">' + ''.join(
        '<div class="l%s"><p class="a">%s + %s</p><p class="b">%s</p></div>'
        % (' ganha' if w else '', a, b, r) for a, b, r, w in CONTAS) + '</div>')


# ── 06 Cartão largo ───────────────────────────────────────────
add('06', 'Cartão largo',
    'Os cartões que já existiam, mas empilhados e ocupando a largura toda. O da vez '
    'inverte para creme, igual à caixa da oferta: a página passa a ter duas coisas claras, '
    'a conta certa e o preço.',
    r"""
.v6 .c{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;
  background:var(--pa2);border:1px solid var(--ru);border-radius:var(--r);padding:22px 26px;
  margin-bottom:12px}
.v6 .a{font-family:var(--fd);font-weight:700;font-size:1.06rem;letter-spacing:-.02em;color:var(--mut)}
.v6 .b{font-size:.98rem;color:var(--dim);text-align:right}
.v6 .ganha{background:var(--off);border-color:var(--off);margin-bottom:0}
.v6 .ganha .a{color:var(--offtx)}
.v6 .ganha .b{color:var(--offtx);font-weight:700}
""",
    lambda: '<div class="v6">' + ''.join(
        '<div class="c%s"><span class="a">%s + %s</span><span class="b">%s</span></div>'
        % (' ganha' if w else '', a, b, r) for a, b, r, w in CONTAS) + '</div>')


# ── 07 Riscado ────────────────────────────────────────────────
add('07', 'Riscado',
    'As duas que não servem estão literalmente cortadas. É a versão mais direta e a mais '
    'arriscada: risco em cima de texto atrapalha a leitura de quem lê rápido.',
    r"""
.v7 .l{padding:18px 0;border-top:1px solid var(--ru)}
.v7 .l:last-child{border-bottom:1px solid var(--ru)}
.v7 .a{font-family:var(--fd);font-weight:700;font-size:1.08rem;letter-spacing:-.02em;color:#5E5B56;
  position:relative;display:inline-block}
.v7 .l:not(.ganha) .a:after{content:'';position:absolute;left:-4px;right:-4px;top:52%;height:2px;
  background:#5E5B56;opacity:.9}
.v7 .b{margin:6px 0 0;color:#4E4B47;font-size:.96rem}
.v7 .ganha{border-top-color:var(--ac)}
.v7 .ganha .a{color:var(--ink);font-size:1.3rem}
.v7 .ganha .b{color:var(--ac);font-weight:700;font-size:1.04rem}
""",
    lambda: '<div class="v7">' + ''.join(
        '<div class="l%s"><span class="a">%s + %s</span><p class="b">%s</p></div>'
        % (' ganha' if w else '', a, b, r) for a, b, r, w in CONTAS) + '</div>')


# ── 08 Barra de alcance ───────────────────────────────────────
add('08', 'Barra de alcance',
    'Cada linha ganha uma barra que mede até onde aquele cenário leva o livro. Dá uma '
    'grandeza que o texto sozinho não dá, e a terceira é a única que enche.',
    r"""
.v8 .l{padding:18px 0;border-top:1px solid var(--ru)}
.v8 .l:last-child{border-bottom:1px solid var(--ru)}
.v8 .top{display:flex;justify-content:space-between;gap:18px;align-items:baseline}
.v8 .a{font-family:var(--fd);font-weight:700;font-size:1.04rem;letter-spacing:-.02em;color:var(--mut)}
.v8 .b{color:var(--dim);font-size:.95rem;text-align:right}
.v8 .bar{margin:12px 0 0;height:6px;border-radius:99px;background:var(--ru);overflow:hidden}
.v8 .bar i{display:block;height:100%;background:#55524D;border-radius:99px}
.v8 .ganha .a{color:var(--ink)}
.v8 .ganha .b{color:var(--ac);font-weight:700}
.v8 .ganha .bar i{background:var(--ac)}
""",
    lambda: '<div class="v8">' + ''.join(
        '<div class="l%s"><div class="top"><span class="a">%s + %s</span>'
        '<span class="b">%s</span></div><div class="bar"><i style="width:%s"></i></div></div>'
        % (' ganha' if w else '', a, b, r, larg)
        for (a, b, r, w), larg in zip(CONTAS, ['8%', '34%', '100%'])) + '</div>')


# ── 09 Os dois lados ──────────────────────────────────────────
add('09', 'Os dois lados',
    'Separa as duas variáveis em duas colunas fixas, LIVRO e LANÇAMENTO, para a terceira '
    'linha ser a única com as duas acesas. É a que explica melhor POR QUE só uma funciona.',
    r"""
.v9 .cab{display:grid;grid-template-columns:1fr 1fr 1.2fr;gap:14px;padding:0 0 10px;
  font-family:var(--fd);font-weight:700;font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--dim);border-bottom:1px solid var(--ru)}
.v9 .l{display:grid;grid-template-columns:1fr 1fr 1.2fr;gap:14px;align-items:center;padding:14px 0;
  border-bottom:1px solid var(--ru)}
.v9 .cel{font-family:var(--fd);font-weight:700;font-size:.98rem;letter-spacing:-.02em;
  padding:10px 12px;border-radius:9px;border:1px solid var(--ru);color:var(--dim);text-align:center}
.v9 .cel.ok{border-color:var(--ac);color:var(--ac);background:rgba(234,184,45,.07)}
.v9 .b{color:var(--dim);font-size:.95rem}
.v9 .ganha .b{color:var(--ink);font-weight:700}
""",
    lambda: '<div class="v9"><div class="cab"><span>O livro</span><span>O lançamento</span>'
            '<span>O que acontece</span></div>' + ''.join(
        '<div class="l%s"><span class="cel %s">%s</span><span class="cel %s">%s</span>'
        '<span class="b">%s</span></div>'
        % (' ganha' if w else '',
           'ok' if bom_l else '', 'Bom' if bom_l else 'Ruim',
           'ok' if bom_c else '', 'Bom' if bom_c else 'Ruim', r)
        for (a, b, r, w), (bom_l, bom_c) in zip(CONTAS, [(1, 0), (0, 1), (1, 1)])) + '</div>')


# ── 10 Degraus ────────────────────────────────────────────────
add('10', 'Degraus',
    'As três em degrau, subindo. A leitura vira movimento: cada linha avança um passo e a '
    'terceira é o topo. Funciona no desktop e some no celular, onde vira lista reta.',
    r"""
.v10 .l{padding:20px 24px;border-left:2px solid var(--ru);margin-bottom:10px}
.v10 .l:nth-child(2){margin-left:40px}
.v10 .l:nth-child(3){margin-left:80px}
.v10 .a{font-family:var(--fd);font-weight:700;font-size:1.05rem;letter-spacing:-.02em;color:var(--mut)}
.v10 .b{margin:6px 0 0;color:var(--dim);font-size:.96rem}
.v10 .ganha{border-left-color:var(--ac);border-left-width:3px}
.v10 .ganha .a{color:var(--ink);font-size:1.26rem}
.v10 .ganha .b{color:var(--ac);font-weight:700;font-size:1.04rem}
@media(max-width:700px){.v10 .l{margin-left:0!important}}
""",
    lambda: '<div class="v10">' + ''.join(
        '<div class="l%s"><p class="a">%s + %s</p><p class="b">%s</p></div>'
        % (' ganha' if w else '', a, b, r) for a, b, r, w in CONTAS) + '</div>')


def main():
    css = BASE + ''.join(v[3] for v in V)
    itens = ''.join(
        '<section class="item"><div class="w">'
        '<div class="cab"><span class="no">%s</span><h2>%s</h2></div>'
        '<p class="tese">%s</p>'
        '<div class="palco">%s</div></div></section>' % (slug, nome, tese, html())
        for slug, nome, tese, _, html in V)

    page = (
        '<title>Dez contas</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@400;700&'
        'family=Fraunces:ital,wght@1,500&display=swap">'
        '<style>' + css + '</style>'
        '<header><div class="w"><p class="eyebrow">Upsell do 90D · o bloco da conta</p>'
        '<h1>Dez maneiras de desenhar<br><span class="serifa">a mesma conta.</span></h1>'
        '<p>Nas dez as três contas ficam <b>uma embaixo da outra</b>. Lado a lado elas viram '
        'três cartões soltos e a comparação se perde, que é exatamente onde mora o argumento. '
        'Texto, paleta e tipos são os da página real; o que muda é só como o olho percorre.</p>'
        '</div></header>' + itens +
        '<footer><div class="w">The Book Business · protótipos do bloco da conta</div></footer>')

    if '--artifact' not in sys.argv:
        page = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1">'
                '<meta name="robots" content="noindex"></head><body>' + page + '</body></html>')
    io.open(OUT, 'w', encoding='utf-8').write(page)
    print('  %d versões -> %s  (%.0f KB)' % (len(V), OUT, len(page.encode('utf-8')) / 1024.0))


if __name__ == '__main__':
    main()
