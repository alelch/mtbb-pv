# -*- coding: utf-8 -*-
"""
A conta em ESCALA: a versão 05 (só tipo) com as três linhas crescendo.

    python3 gera_escala.py [destino.html] [--artifact]

O pedido: a primeira pequena, a segunda normal, a terceira grande. Isso tem
muita margem, então aqui vão seis calibragens do MESMO princípio, mudando o
que cresce e quanto.

⚠️ Uma observação sobre o conteúdo, não sobre o desenho: não existe uma conta
"ruim + ruim" no texto. As três são "bom + ruim", "bom + ruim" (na outra
ordem) e "bom + bom". A escala aqui é de CONSEQUÊNCIA, do pior resultado ao
melhor, que é o que a página argumenta. Se você quiser mesmo a quarta linha
(livro ruim + lançamento ruim), é copy nova e precisa passar pela Dany.
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_args = [a for a in sys.argv[1:] if not a.startswith('--')]
OUT = _args[0] if _args else os.path.join(HERE, 'escala.html')

CONTAS = [
    ('Livro bom + lançamento ruim', 'Ninguém descobre.'),
    ('Lançamento bom + livro ruim', 'Vende no lançamento. Depois, esquecido.'),
    ('Lançamento bom + livro bom', 'Muda a vida do autor.'),
]

BASE = r"""
:root{--pa:#101012;--pa2:#17171A;--ink:#EFEDE8;--mut:#9A958D;--dim:#6B675F;--ru:#27272B;
  --ac:#EAB82D;--fraco:#55524D;--fraquissimo:#44413D;
  --ff:'DM Sans',system-ui,sans-serif;--fd:'Space Grotesk','DM Sans',sans-serif;
  --fs:Fraunces,Georgia,serif}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);font:400 16px/1.6 var(--ff);
  -webkit-font-smoothing:antialiased}
.w{max-width:1120px;margin:0 auto;padding:0 22px}
h1,h2{margin:0;font-family:var(--fd);font-weight:700;letter-spacing:-.03em;line-height:1.1}
.serifa{font-family:var(--fs);font-style:italic;font-weight:500;letter-spacing:-.02em}
.eyebrow{font-family:var(--fd);font-size:.78rem;font-weight:700;letter-spacing:.18em;
  text-transform:uppercase;color:var(--ac);margin:0 0 16px}
header{padding:56px 0 30px;border-bottom:1px solid var(--ru)}
header h1{font-size:clamp(1.9rem,4vw,3rem)}
header p{margin:18px 0 0;max-width:68ch;color:var(--mut)}
header p b{color:var(--ink)}
header .aviso{margin-top:16px;padding:14px 18px;border-left:2px solid var(--ac);
  background:rgba(234,184,45,.05);font-size:.94rem;max-width:68ch}
.item{border-bottom:1px solid var(--ru);padding:56px 0}
.cab{display:flex;align-items:baseline;gap:12px;margin:0 0 8px}
.cab .no{font-family:var(--fd);font-weight:700;font-size:.78rem;letter-spacing:.16em;color:var(--ac)}
.cab h2{font-size:1.3rem}
.tese{margin:0 0 34px;color:var(--mut);max-width:72ch;font-size:.97rem}
.palco{max-width:820px}
footer{padding:34px 0 60px;color:var(--dim);font-size:.85rem}

/* o comum das seis: a linha é sempre condição em cima, resultado embaixo */
.e .l{padding:14px 0}
.e .a{font-family:var(--fd);font-weight:700;letter-spacing:-.03em;line-height:1.2;margin:0}
.e .b{margin:4px 0 0;line-height:1.3}
"""

V = []


def add(slug, nome, tese, css):
    V.append((slug, nome, tese, css))


# ── A · só o corpo cresce ─────────────────────────────────────
add('A', 'Escala limpa',
    'Só o tamanho muda. Condição e resultado crescem juntos, na mesma proporção, e a cor '
    'segue a do 05: as duas primeiras apagadas, a terceira acesa. É a leitura mais direta '
    'do seu pedido, sem nenhum outro truque.',
    r"""
.eA .l1 .a{font-size:1rem;color:var(--fraco)}
.eA .l1 .b{font-size:.92rem;color:var(--fraquissimo)}
.eA .l2 .a{font-size:1.45rem;color:var(--mut)}
.eA .l2 .b{font-size:1.15rem;color:var(--fraco)}
.eA .l3{padding-top:22px}
.eA .l3 .a{font-size:2.2rem;color:var(--ink)}
.eA .l3 .b{font-size:1.7rem;color:var(--ac);font-weight:700}
""")

# ── B · o corpo e o ar ────────────────────────────────────────
add('B', 'Escala com respiro',
    'A mesma escala de corpo, mas o espaço em volta cresce junto. A primeira linha fica '
    'espremida, a última tem ar de sobra. O olho lê a importância antes de ler a palavra.',
    r"""
.eB .l1{padding:6px 0}
.eB .l1 .a{font-size:1rem;color:var(--fraco)}
.eB .l1 .b{font-size:.92rem;color:var(--fraquissimo)}
.eB .l2{padding:22px 0}
.eB .l2 .a{font-size:1.45rem;color:var(--mut)}
.eB .l2 .b{font-size:1.15rem;color:var(--fraco)}
.eB .l3{padding:44px 0 10px}
.eB .l3 .a{font-size:2.3rem;color:var(--ink)}
.eB .l3 .b{font-size:1.8rem;color:var(--ac);font-weight:700}
""")

# ── C · a escala só no resultado ──────────────────────────────
add('C', 'Escala só na consequência',
    'As três condições ficam do mesmo tamanho, porque as três são igualmente possíveis. '
    'Quem cresce é só o RESULTADO. Diz que a diferença não está no que você faz, está no '
    'que acontece depois.',
    r"""
.eC .l{border-top:1px solid var(--ru);padding:20px 0}
.eC .a{font-size:1.02rem;color:var(--mut)}
.eC .l1 .b{font-size:1rem;color:var(--fraquissimo)}
.eC .l2 .b{font-size:1.4rem;color:var(--fraco)}
.eC .l3{border-top-color:var(--ac)}
.eC .l3 .a{color:var(--ink)}
.eC .l3 .b{font-size:2.2rem;color:var(--ac);font-weight:700;letter-spacing:-.03em}
""")

# ── D · a serifa só no fim ────────────────────────────────────
add('D', 'Escala com a serifa no fim',
    'Cresce e troca de voz: as duas primeiras são a sans de trabalho, a terceira chega no '
    'itálico da marca. É a que mais parece com o resto da página, porque é o mesmo par de '
    'tipos que os títulos usam.',
    r"""
.eD .l1 .a{font-size:1rem;color:var(--fraco)}
.eD .l1 .b{font-size:.92rem;color:var(--fraquissimo)}
.eD .l2 .a{font-size:1.45rem;color:var(--mut)}
.eD .l2 .b{font-size:1.15rem;color:var(--fraco)}
.eD .l3{padding-top:26px}
.eD .l3 .a{font-size:2.1rem;color:var(--ink)}
.eD .l3 .b{font-family:var(--fs);font-style:italic;font-weight:500;font-size:2rem;
  color:var(--ac);letter-spacing:-.025em;margin-top:8px}
""")

# ── E · escala extrema ────────────────────────────────────────
add('E', 'Escala extrema',
    'O salto no talo: a primeira quase uma nota de rodapé, a terceira uma manchete. É a '
    'mais forte e a mais arriscada, porque a primeira linha fica tão pequena que pode não '
    'ser lida, e ela é parte do argumento.',
    r"""
.eE .l1 .a{font-size:.86rem;color:#4A4743;font-weight:500;letter-spacing:0}
.eE .l1 .b{font-size:.82rem;color:#403D3A}
.eE .l2 .a{font-size:1.5rem;color:var(--fraco)}
.eE .l2 .b{font-size:1.18rem;color:var(--fraco)}
.eE .l3{padding-top:30px}
.eE .l3 .a{font-size:clamp(2rem,4.6vw,3.1rem);color:var(--ink);line-height:1.05}
.eE .l3 .b{font-size:clamp(1.6rem,3.4vw,2.3rem);color:var(--ac);font-weight:700;margin-top:10px}
""")

# ── F · escala com fio embaixo ────────────────────────────────
add('F', 'Escala com o fio do total',
    'A escala do A, mais um fio âmbar antes da última linha, como o traço de uma conta '
    'antes do total. Junta o crescimento com a leitura de soma: as duas de cima são '
    'parcelas, a de baixo é o resultado.',
    r"""
.eF .l1 .a{font-size:1rem;color:var(--fraco)}
.eF .l1 .b{font-size:.92rem;color:var(--fraquissimo)}
.eF .l2 .a{font-size:1.45rem;color:var(--mut)}
.eF .l2 .b{font-size:1.15rem;color:var(--fraco)}
.eF .l3{border-top:2px solid var(--ac);margin-top:22px;padding-top:26px}
.eF .l3 .a{font-size:2.2rem;color:var(--ink)}
.eF .l3 .b{font-size:1.7rem;color:var(--ac);font-weight:700}
""")


def linhas(cls):
    return ('<div class="e %s">' % cls) + ''.join(
        '<div class="l l%d"><p class="a">%s</p><p class="b">%s</p></div>' % (i + 1, a, b)
        for i, (a, b) in enumerate(CONTAS)) + '</div>'


def main():
    css = BASE + ''.join(v[3] for v in V)
    itens = ''.join(
        '<section class="item"><div class="w">'
        '<div class="cab"><span class="no">%s</span><h2>%s</h2></div>'
        '<p class="tese">%s</p><div class="palco">%s</div></div></section>'
        % (slug, nome, tese, linhas('e' + slug))
        for slug, nome, tese, _ in V)

    page = (
        '<title>A conta em escala</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@400;700&'
        'family=Fraunces:ital,wght@1,500&display=swap">'
        '<style>' + css + '</style>'
        '<header><div class="w"><p class="eyebrow">Upsell do 90D · o bloco da conta</p>'
        '<h1>A versão 05,<br><span class="serifa">agora em escala.</span></h1>'
        '<p>Seis calibragens do mesmo princípio: a primeira pequena, a segunda normal, a '
        'terceira grande. O que muda entre elas é <b>o que cresce</b> e <b>quanto</b>.</p>'
        '<p class="aviso">Uma observação sobre o texto, não sobre o desenho: não existe uma '
        'conta <b>"ruim + ruim"</b> aqui. As três são bom+ruim, bom+ruim na outra ordem, e '
        'bom+bom. A escala é de <b>consequência</b>, do pior resultado ao melhor. Se você '
        'quiser mesmo a quarta linha (livro ruim + lançamento ruim), é copy nova.</p>'
        '</div></header>' + itens +
        '<footer><div class="w">The Book Business · calibragens do bloco da conta</div></footer>')

    if '--artifact' not in sys.argv:
        page = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1">'
                '<meta name="robots" content="noindex"></head><body>' + page + '</body></html>')
    io.open(OUT, 'w', encoding='utf-8').write(page)
    print('  %d calibragens -> %s  (%.0f KB)' % (len(V), OUT, len(page.encode('utf-8')) / 1024.0))


if __name__ == '__main__':
    main()
