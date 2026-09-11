# -*- coding: utf-8 -*-
"""
Gera as 10 propostas de design da PV do upsell + a galeria de comparação.

    python3 gera.py

Copy identica nas dez (vem de copy_base.py), entao o que muda e' SO' o design.
Sao prototipos: o botao nao leva a checkout nenhum e nao ha JS de oferta.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from copy_base import C, RUMOS                      # noqa: E402
import designs_a as A                               # noqa: E402
import designs_b as B                               # noqa: E402

FN = [A.d01, A.d02, A.d03, A.d04, A.d05, B.d06, B.d07, B.d08, B.d09, B.d10]
HERE = os.path.dirname(os.path.abspath(__file__))

GAL_CSS = r"""
:root{--bg:#0E0E10;--cd:#17171A;--tx:#EFEDE8;--mut:#8C8880;--ac:#E9B949;--bd:#2A2A2E}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);
  font:400 15px/1.6 ui-sans-serif,system-ui,-apple-system,sans-serif;-webkit-font-smoothing:antialiased}
.w{max-width:1500px;margin:0 auto;padding:0 26px}
header{padding:46px 0 30px;border-bottom:1px solid var(--bd)}
h1{margin:0;font-size:clamp(26px,3.4vw,40px);letter-spacing:-.03em}
header p{margin:12px 0 0;color:var(--mut);max-width:70ch}
header code{background:#000;padding:2px 6px;border-radius:4px;font-size:.86em;color:var(--ac)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:26px;padding:34px 0 70px}
.it{background:var(--cd);border:1px solid var(--bd);border-radius:14px;overflow:hidden;
  display:flex;flex-direction:column;transition:border-color .2s,transform .2s}
.it:hover{border-color:var(--ac);transform:translateY(-3px)}
.fr{position:relative;height:420px;overflow:hidden;background:#fff;border-bottom:1px solid var(--bd)}
.fr iframe{position:absolute;top:0;left:0;width:1280px;height:1400px;border:0;
  transform:scale(.33);transform-origin:0 0;pointer-events:none}
.fr a{position:absolute;inset:0;z-index:2}
.mt{padding:16px 18px 18px}
.mt .n{display:flex;align-items:baseline;gap:9px}
.mt .n b{font-size:12px;color:var(--ac);font-variant-numeric:tabular-nums}
.mt h2{margin:0;font-size:18.5px;letter-spacing:-.02em}
.mt p{margin:7px 0 0;color:var(--mut);font-size:13.6px;line-height:1.55}
.mt .go{display:inline-block;margin-top:13px;color:var(--tx);font-size:12.5px;font-weight:600;
  letter-spacing:.04em;text-transform:uppercase;text-decoration:none;
  border-bottom:1px solid var(--ac);padding-bottom:2px}
footer{border-top:1px solid var(--bd);padding:26px 0 50px;color:var(--mut);font-size:13px}
"""


def galeria():
    cards = ''
    for i, (slug, nome, tese) in enumerate(RUMOS, 1):
        cards += (
            '<article class="it"><div class="fr">'
            '<iframe src="%s/index.html" loading="lazy" title="%s" scrolling="no"></iframe>'
            '<a href="%s/index.html" target="_blank" rel="noopener" aria-label="Abrir %s"></a>'
            '</div><div class="mt"><div class="n"><b>%02d</b><h2>%s</h2></div>'
            '<p>%s</p><a class="go" href="%s/index.html" target="_blank" rel="noopener">'
            'Abrir em tela cheia</a></div></article>' % (slug, nome, slug, nome, i, nome, tese, slug))
    return ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="robots" content="noindex"><title>10 rumos de design · Upsell 90D</title>'
            '<style>' + GAL_CSS + '</style></head><body><div class="w">'
            '<header><h1>Dez rumos de design para a mesma página</h1>'
            '<p>A copy é <b>idêntica</b> nas dez (sai de <code>copy_base.py</code>), então a única '
            'coisa que muda é o design. São protótipos: nenhum botão leva a checkout e nenhum '
            'tem o JS da oferta. Abra em tela cheia para julgar de verdade, a miniatura só serve '
            'para escolher qual abrir.</p></header>'
            '<div class="grid">' + cards + '</div>'
            '<footer>The Book Business · gerado por <code>_designs/gera.py</code></footer>'
            '</div></body></html>')


def main():
    for (slug, nome, _), fn in zip(RUMOS, FN):
        d = os.path.join(HERE, slug)
        os.makedirs(d, exist_ok=True)
        html = fn()
        io.open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(html)
        print('  %-16s %6d bytes  %s' % (slug, len(html.encode('utf-8')), nome))
    io.open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(galeria())
    print('  galeria          -> _designs/index.html')


if __name__ == '__main__':
    main()
