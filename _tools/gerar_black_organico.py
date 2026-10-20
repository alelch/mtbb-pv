#!/usr/bin/env python3
"""Gera /black-week-organico/ a partir da longa (/black-week-misterio/). NÃO editar a orgânica à mão: edite a longa
e rode este script (o pre-commit do repo roda sozinho quando a longa muda).
Diferenças da orgânica: fora do teste A/B (sem sorteio/redirecionamento), cadastro marcado posicao=organico-* e
src = ?src= do link (ou utm_source, ou 'direto'); não herda UTM de anúncio guardada no navegador."""
import re, sys, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
src = (R / 'black-week-misterio/index.html').read_text()
h = src

def troca(a, b, n=1, regex=False):
    global h
    novo, k = (re.subn(a, b, h, flags=re.S) if regex else (h.replace(a, b), h.count(a)))
    if k != n: sys.exit(f'gerar_black_organico: esperava {n}x, achei {k}x: {a[:70]!r}')
    h = novo

# 20/10: o teste A/B de página acabou e o script saiu da longa (antes era removido aqui)
troca('<link rel="canonical" href="https://metodo.thebookbusiness.com.br/black-week-misterio/">',
      '<link rel="canonical" href="https://metodo.thebookbusiness.com.br/black-week-organico/">')
# arquivos locais da longa: aponta para a pasta dela (não duplica imagem)
h, k = re.subn(r'(["\'(\s,])assets/', r'\1../black-week-misterio/assets/', h)
if k < 10: sys.exit(f'gerar_black_organico: poucos caminhos assets/ ({k})')
troca("""  var utms = {};
  try { utms = JSON.parse(localStorage.getItem('mtbb_utms') || '{}') || {}; } catch (e) {}
  var qs = new URLSearchParams(location.search);
  KEYS.forEach(function (k) { var v = qs.get(k); if (v) utms[k] = v; });
  try { localStorage.setItem('mtbb_utms', JSON.stringify(utms)); } catch (e) {}""",
"""  // ORGÂNICA: só o que veio no link (não herda UTM de anúncio guardada no navegador). A origem é a própria página.
  var utms = {};
  var qs = new URLSearchParams(location.search);
  KEYS.forEach(function (k) { var v = qs.get(k); if (v) utms[k] = v; });
  utms.src = (utms.src || utms.utm_source || 'direto').toLowerCase().slice(0, 40);""")
troca("posicao: 'misterio-' + box.getAttribute('data-pos')", "posicao: 'organico-' + box.getAttribute('data-pos')")
troca('if (window.__bf26ab) payload.ab = window.__bf26ab;', '')
cab = '<!-- GERADA por _tools/gerar_black_organico.py a partir de /black-week-misterio/. Não editar aqui. -->\n'
out = R / 'black-week-organico/index.html'
out.parent.mkdir(exist_ok=True)
novo = cab + h
if not out.exists() or out.read_text() != novo:
    out.write_text(novo); print('black-week-organico/index.html atualizada')
else:
    print('black-week-organico/index.html já estava igual')
