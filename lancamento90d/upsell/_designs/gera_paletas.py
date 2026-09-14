# -*- coding: utf-8 -*-
"""
Gera o rumo 12 (Capítulos) em todas as paletas de `designs_e.PALETAS` e monta
uma prancha só delas.

    python3 gera_paletas.py [destino.html] [--artifact]

Layout, tipografia e copy são IDÊNTICOS nas oito. A única variável é a cor.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from designs_e import PALETAS, d12                  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '12-paletas')
_args = [a for a in sys.argv[1:] if not a.startswith('--')]
OUT = _args[0] if _args else os.path.join(BASE, 'prancha.html')

CSS = r"""
:root{
  --board:#E4E1DA; --plate:#FAF9F6; --ink:#191816; --mut:#6E6A62;
  --line:#CBC6BC; --ox:#7A2018; --focus:#7A2018;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --board:#151614; --plate:#1E201D; --ink:#EDEBE5; --mut:#928D83;
    --line:#33352F; --ox:#D4776A; --focus:#D4776A;
  }
}
:root[data-theme="dark"]{
  --board:#151614; --plate:#1E201D; --ink:#EDEBE5; --mut:#928D83;
  --line:#33352F; --ox:#D4776A; --focus:#D4776A;
}
*{box-sizing:border-box}
body{margin:0;background:var(--board);color:var(--ink);
  font:400 16px/1.6 Newsreader,Georgia,serif;-webkit-font-smoothing:antialiased}
.w{max-width:1560px;margin:0 auto;padding:0 clamp(18px,3vw,40px)}
header{border-bottom:1px solid var(--line);padding:clamp(30px,4vw,52px) 0 22px}
.eyebrow{font-family:'DM Mono',ui-monospace,monospace;font-size:11.5px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--ox);margin:0 0 14px;display:flex;gap:12px;align-items:center}
.eyebrow:after{content:'';flex:1;height:1px;background:var(--line)}
h1{margin:0;font-family:'Bricolage Grotesque',ui-sans-serif,system-ui,sans-serif;font-weight:800;
  font-size:clamp(30px,4.6vw,54px);line-height:1.02;letter-spacing:-.038em;text-wrap:balance;
  max-width:20ch}
.brief{margin:18px 0 0;max-width:68ch;font-size:17.5px;color:var(--mut)}
.brief b{color:var(--ink);font-weight:600}
.specs{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 0;padding:0;list-style:none}
.specs li{font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.05em;
  border:1px solid var(--line);border-radius:2px;padding:6px 10px;color:var(--mut)}
.specs li b{color:var(--ink);font-weight:500}

.board{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,380px),1fr));
  gap:clamp(18px,2.2vw,30px);padding:clamp(24px,3.4vw,44px) 0 clamp(50px,7vw,90px)}
.plate{background:var(--plate);border:1px solid var(--line);display:flex;flex-direction:column;
  position:relative}
.plate:before,.plate:after{content:'';position:absolute;width:9px;height:9px;pointer-events:none;
  border-color:var(--ox);opacity:.5}
.plate:before{top:-1px;left:-1px;border-top:1px solid;border-left:1px solid}
.plate:after{bottom:-1px;right:-1px;border-bottom:1px solid;border-right:1px solid}
.ph{display:flex;align-items:baseline;gap:11px;padding:13px 15px 11px;border-bottom:1px solid var(--line)}
.ph .no{font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.14em;color:var(--ox);
  text-transform:uppercase}
.ph h2{margin:0;font-family:'Bricolage Grotesque',sans-serif;font-weight:700;font-size:19px;
  letter-spacing:-.028em}
.win{position:relative;height:430px;overflow:hidden;background:#fff;border-bottom:1px solid var(--line)}
.win iframe{position:absolute;top:0;left:0;width:1320px;height:1400px;border:0;
  transform:scale(var(--s,.3333));transform-origin:0 0}
.win button.open{position:absolute;inset:0;z-index:2;width:100%;border:0;background:transparent;
  cursor:zoom-in;padding:0;font:inherit;color:transparent}
.win button.open:focus-visible{outline:3px solid var(--focus);outline-offset:-3px}
.pf{padding:14px 15px 15px;display:flex;flex-direction:column;gap:12px;flex:1}
.tese{margin:0;font-size:16px;line-height:1.5}
.meta{display:flex;align-items:center;gap:10px;margin-top:auto;padding-top:12px;
  border-top:1px solid var(--line);flex-wrap:wrap}
.chip{display:flex;align-items:center;gap:7px;font-family:'DM Mono',monospace;font-size:10px;
  color:var(--mut);letter-spacing:.04em}
.chip i{display:block;width:17px;height:17px;border:1px solid rgba(120,115,105,.45);border-radius:2px}
footer{border-top:1px solid var(--line);padding:26px 0 40px;color:var(--mut);
  font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.05em}

.viewer{position:fixed;inset:0;z-index:50;background:rgba(12,12,11,.9);
  display:grid;grid-template-rows:auto 1fr}
.viewer[hidden]{display:none!important}
.vbar{display:flex;align-items:center;gap:14px;padding:11px clamp(12px,2vw,22px);
  background:var(--plate);border-bottom:1px solid var(--line)}
.vbar .no{font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.14em;color:var(--ox);
  text-transform:uppercase}
.vbar h3{margin:0;font-family:'Bricolage Grotesque',sans-serif;font-weight:700;font-size:18px;
  letter-spacing:-.028em;flex:1}
.vbar button{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.06em;
  background:transparent;border:1px solid var(--line);color:var(--ink);padding:8px 12px;
  cursor:pointer;border-radius:2px}
.vbar button:hover{border-color:var(--ox);color:var(--ox)}
.vbar button:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
.vbar .x{border-color:var(--ox);color:var(--ox)}
.viewer .stage{background:#fff;overflow:hidden}
.viewer iframe{width:100%;height:100%;border:0;display:block}
@media (prefers-reduced-motion:no-preference){
  .plate{transition:border-color .18s ease,transform .18s ease}
  .plate:hover{border-color:var(--ox);transform:translateY(-2px)}
}
@media (max-width:640px){.win{height:330px}}
"""

JS = r"""
(function(){
  var plates=[].slice.call(document.querySelectorAll('.plate'));
  function fonte(slug){
    var el=document.getElementById('src-'+slug);
    return el ? el.textContent.split('<\\/script').join('</script') : '';
  }
  plates.forEach(function(p){
    var fr=p.querySelector('.win iframe');
    if(fr) fr.srcdoc=fonte(p.dataset.slug);
  });
  function escala(){
    plates.forEach(function(p){
      var win=p.querySelector('.win'), w=win.clientWidth;
      if(w>0) win.style.setProperty('--s',(w/1320).toFixed(4));
    });
  }
  escala(); addEventListener('load',escala); addEventListener('resize',escala);
  var v=document.getElementById('viewer'), vfr=document.getElementById('vframe'),
      vno=document.getElementById('vno'), vtt=document.getElementById('vtt'), volta=null, i=-1;
  function mostra(n){
    i=(n+plates.length)%plates.length;
    var p=plates[i];
    vno.textContent=p.dataset.no; vtt.textContent=p.dataset.nome;
    vfr.srcdoc=fonte(p.dataset.slug);
    v.hidden=false; document.body.style.overflow='hidden';
    document.getElementById('vx').focus();
  }
  function fecha(){ v.hidden=true; vfr.srcdoc=''; document.body.style.overflow='';
    if(volta) volta.focus(); }
  plates.forEach(function(p,n){
    p.querySelector('.open').addEventListener('click',function(e){volta=e.currentTarget;mostra(n)});
  });
  document.getElementById('vx').addEventListener('click',fecha);
  document.getElementById('vp').addEventListener('click',function(){mostra(i-1)});
  document.getElementById('vn').addEventListener('click',function(){mostra(i+1)});
  document.addEventListener('keydown',function(e){
    if(v.hidden) return;
    if(e.key==='Escape') fecha();
    if(e.key==='ArrowLeft') mostra(i-1);
    if(e.key==='ArrowRight') mostra(i+1);
  });
})();
"""


def main():
    os.makedirs(BASE, exist_ok=True)
    plates, fontes = '', ''
    for slug, nome, tese, pal in PALETAS:
        d = os.path.join(BASE, slug)
        os.makedirs(d, exist_ok=True)
        html = d12(pal)
        io.open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(html)
        print('  %-18s %6d bytes  %s' % (slug, len(html.encode('utf-8')), nome))

        chips = ''.join(
            '<span class="chip"><i style="background:%s"></i>%s</span>' % (pal[k], r)
            for k, r in [('pa', 'fundo'), ('ac', 'acento'), ('acf', 'tarja'), ('off', 'oferta')])
        plates += (
            '<article class="plate" data-slug="%s" data-no="%s" data-nome="%s">'
            '<div class="ph"><span class="no">%s</span><h2>%s</h2></div>'
            '<div class="win"><iframe title="Prévia: %s" scrolling="no" loading="lazy"></iframe>'
            '<button class="open" type="button">Abrir a paleta %s</button></div>'
            '<div class="pf"><p class="tese">%s</p><div class="meta">%s</div></div></article>'
            % (slug, slug.split('-')[0], nome, slug.split('-')[0], nome, nome, nome, tese, chips))
        fontes += ('<script type="text/plain" id="src-%s">%s</script>'
                   % (slug, html.replace('</script', '<\\/script')))

    page = (
        '<title>Paletas dos Capítulos</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&'
        'family=Newsreader:wght@400;600&family=DM+Mono:wght@400;500&display=swap">'
        '<style>' + CSS + '</style>'
        '<div class="w"><header><p class="eyebrow">Rumo 12 · Capítulos · upsell do 90D</p>'
        '<h1>A mesma página, oito temperaturas</h1>'
        '<p class="brief">Layout, tipografia e copy são <b>idênticos</b> nas oito. A única '
        'variável é a cor, então o que estiver diferente aos seus olhos é a paleta e mais nada. '
        'Cada uma declara quatro papéis: <b>fundo</b>, <b>acento em texto</b> (precisa passar '
        'contraste), <b>tarja</b> (só preenchimento) e o <b>bloco da oferta</b>. Clique para '
        'abrir em tamanho real.</p>'
        '<ul class="specs"><li><b>' + str(len(PALETAS)) + '</b> paletas</li>'
        '<li><b>1</b> layout</li><li><b>1</b> copy</li>'
        '<li>← → e Esc no visor</li></ul></header>'
        '<div class="board">' + plates + '</div>'
        '<footer>Protótipos. Nenhum botão leva a checkout.</footer></div>'
        '<div class="viewer" id="viewer" hidden role="dialog" aria-modal="true" '
        'aria-label="Paleta em tamanho real">'
        '<div class="vbar"><span class="no" id="vno"></span><h3 id="vtt"></h3>'
        '<button type="button" id="vp">← anterior</button>'
        '<button type="button" id="vn">próxima →</button>'
        '<button type="button" id="vx" class="x">fechar ✕</button></div>'
        '<div class="stage"><iframe id="vframe" title="Paleta em tamanho real"></iframe></div></div>'
        + fontes + '<script>' + JS + '</script>')

    if '--artifact' not in sys.argv:
        page = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1">'
                '<meta name="robots" content="noindex"></head><body>' + page + '</body></html>')
    io.open(OUT, 'w', encoding='utf-8').write(page)
    print('  prancha -> %s  (%.0f KB)' % (OUT, len(page.encode('utf-8')) / 1024.0))


if __name__ == '__main__':
    main()
