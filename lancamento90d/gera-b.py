#!/usr/bin/env python3
"""Gera a /upsell-b/ (variante B, R$597) a partir da /upsell/ (variante A, R$697).

Por que um gerador em vez de duas páginas mantidas na mão: a lição registrada
do teste da Imersão é que duas páginas irmãs SEMPRE divergem quando alguém
edita uma e esquece a outra. Aqui a A é a fonte e a B é derivada. Editar a A e
rodar `python3 gera-b.py`.

As quatro diferenças da B, e o motivo de cada uma:
  1. preço 697 -> 597 e a oferta n740dj0b -> 8rn7djuk (é o teste em si)
  2. variante 'B' FORÇADA: quem cai direto na B (link compartilhado, cookie
     expirado) não pode sair carimbado como A vendo o preço de B
  3. `outraUrl` sai: a B NUNCA redireciona. Redirect nas duas = loop por
     construção, incidente real de 23/07 no teste da Imersão
  4. canonical aponta pra /upsell/, que é o setup correto de teste A/B
"""
import pathlib, re, sys

BASE = pathlib.Path(__file__).parent
A = BASE / "upsell" / "index.html"
B = BASE / "upsell-b" / "index.html"

s = A.read_text(encoding="utf-8")
antes = s

TROCAS = [
    # 1. preço e oferta
    ('<span class="cur">R$</span>697', '<span class="cur">R$</span>597'),
    ('os R$697 são abatidos', 'os R$597 são abatidos'),
    ('R$697 por uma conversa é caro', 'R$597 por uma conversa é caro'),
    ('<div class="p">R$697<small>', '<div class="p">R$597<small>'),
    ('não custa seiscentos reais', 'não custa quinhentos reais'),
    ('?off=n740dj0b', '?off=8rn7djuk'),
    # 2, 3. identidade da variante
    ("  variante: 'A',", "  variante: 'B',"),
    ('  preco:    697,', '  preco:    597,'),
    ('  valor:    697,', '  valor:    597,'),
    ("  outraUrl: '../upsell-b/',\n", ""),
    # 4. canonical
    ('<meta name="robots" content="noindex,nofollow">',
     '<meta name="robots" content="noindex,nofollow">\n<link rel="canonical" href="https://metodo.thebookbusiness.com.br/lancamento90d/upsell/">'),
    # aviso no topo do arquivo
    ('<!doctype html>',
     '<!doctype html>\n<!-- ⚠️⚠️ ARQUIVO GERADO. NÃO EDITAR NA MÃO.\n     Fonte: ../upsell/index.html. Para mudar qualquer coisa aqui, edite a\n     /upsell/ e rode `python3 gera-b.py`. Esta é a VARIANTE B do teste de\n     preço: R$597, oferta 8rn7djuk, e SEM o branch de redirect. -->'),
    ('💰 ESTA É A VARIANTE A DO TESTE DE PREÇO: R$697 (oferta n740dj0b).',
     '💰 ESTA É A VARIANTE B DO TESTE DE PREÇO: R$597 (oferta 8rn7djuk).'),
]

faltou = []
for a, b in TROCAS:
    if a not in s:
        faltou.append(a[:60])
    s = s.replace(a, b)

if faltou:
    print("ERRO: trecho nao encontrado na /upsell/ (a pagina mudou?):", file=sys.stderr)
    for f in faltou:
        print("  -", f, file=sys.stderr)
    sys.exit(1)

# Guardas. Rodam sobre o arquivo SEM comentarios: os comentarios descrevem o
# teste inteiro e citam as duas variantes de proposito, entao 697 e n740dj0b
# aparecem la legitimamente. O que nao pode e sobrar no conteudo servido.
sem_comentario = re.sub(r"<!--.*?-->", "", s, flags=re.S)
sem_comentario = re.sub(r"/\*.*?\*/", "", sem_comentario, flags=re.S)
sem_comentario = re.sub(r"^\s*//.*$", "", sem_comentario, flags=re.M)

sobrou = re.findall(r"R\$\s*697|>697|n740dj0b|697,", sem_comentario)
if sobrou:
    print("ERRO: sobrou 697/oferta A no conteudo da variante B:", set(sobrou), file=sys.stderr)
    sys.exit(1)
if "outraUrl" in sem_comentario:
    print("ERRO: a B ficou com outraUrl, vai virar loop de redirect", file=sys.stderr)
    sys.exit(1)
if "variante: 'A'" in sem_comentario:
    print("ERRO: a B ficou marcada como variante A", file=sys.stderr)
    sys.exit(1)

B.parent.mkdir(exist_ok=True)
B.write_text(s, encoding="utf-8")
print(f"/upsell-b/ gerada  ({len(s):,} bytes, {len(TROCAS)} trocas)")
