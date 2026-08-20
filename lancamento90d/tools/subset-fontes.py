#!/usr/bin/env python3
"""Regera os subsets das fontes decorativas (Caveat e Fraunces).

Rode da pasta lancamento90d/ sempre que a copy de .mao ou .serifa mudar.
Ele lê os glifos direto do index.html, então não precisa manter lista à mão.

    python3 tools/subset-fontes.py
"""
import re, os
from fontTools.ttLib import TTFont
from fontTools import subset

AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = open(os.path.join(AQUI, 'index.html'), encoding='utf-8').read()

def texto_das(classes):
    fora = ''
    for c in classes:
        for m in re.finditer(r'class="[^"]*\b' + c + r'\b[^"]*"[^>]*>([\s\S]*?)</', s):
            fora += re.sub(r'<[^>]+>', '', m.group(1))
    return set(fora)

ALVOS = [
    ('caveat.woff2',              'caveat-sub.woff2',              ['mao', 'lin']),
    ('fraunces-italic-500.woff2', 'fraunces-italic-500-sub.woff2', ['serifa', 'fala']),
]

for orig, saida, classes in ALVOS:
    src = os.path.join(AQUI, 'assets/fonts', orig)
    dst = os.path.join(AQUI, 'assets/fonts', saida)
    ch = texto_das(classes)
    f = TTFont(src)
    o = subset.Options(); o.layout_features = ['*']; o.notdef_outline = True
    sub = subset.Subsetter(options=o)
    sub.populate(unicodes=[ord(c) for c in ch])
    sub.subset(f)
    f.flavor = 'woff2'
    f.save(dst)
    print('%-32s %6d -> %6d B   %d glifos: %s' % (
        saida, os.path.getsize(src), os.path.getsize(dst),
        len(ch), ''.join(sorted(c for c in ch if c.strip()))))
