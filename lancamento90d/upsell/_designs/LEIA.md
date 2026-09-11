# 10 rumos de design · PV do upsell (Diagnóstico do Autor)

Abrir `index.html` desta pasta: é a galeria com as dez lado a lado.

**A copy é idêntica nas dez.** Sai toda de `copy_base.py`, que é uma cópia fiel
da copy que está no ar em `../index.html` (extraída em 10/09/2026). Quem muda é
só o design, então a comparação é honesta.

## Como mexer

```
python3 gera.py
```

- `copy_base.py` — a copy + a lista dos dez rumos + o esqueleto do HTML.
- `designs_a.py` — rumos 01 a 05.
- `designs_b.py` — rumos 06 a 10.
- `gera.py` — escreve as dez pastas + a galeria.

Nunca editar os `index.html` gerados à mão: a próxima rodada do `gera.py` apaga.

## O que estes arquivos NÃO são

Protótipos de **design**, não páginas prontas:

- nenhum botão leva a checkout (todos são `href="#"`),
- não têm o `oferta.js` (aceite, recusa, redirect do teste A/B, VTurb),
- não têm o teste de preço A/B (`gera-b.py`),
- não têm os comentários de decisão que o `../index.html` carrega.

Quando um rumo for escolhido, o caminho é portar o CSS dele para a página real,
não promover a pasta.

## Os dez

| # | rumo | tese |
|---|---|---|
| 01 | Editorial | Revista literária: serifa grande, fio fino, muito respiro. |
| 02 | Capa de livro | A página inteira é a sobrecapa: lombada, orelha, quarta capa. |
| 03 | Ficha catalográfica | Catálogo de biblioteca: monoespaçada, campos, carimbo. |
| 04 | Noir premium | Quase preto, fio de ouro, tipo leve e enorme. Silêncio caro. |
| 05 | Relatório clínico | A página vira o próprio diagnóstico: matriz, status, laudo. |
| 06 | Suíço | Grade rígida, preto e um vermelho, numeração 01–07. |
| 07 | Marginalia | Alguém leu o seu livro e anotou na margem, à caneta. |
| 08 | Neo-brutalista | Borda preta grossa, sombra dura, tipo gigante, acento elétrico. |
| 09 | Cinema | Tela cheia, letterbox, grão, sequência de planos. |
| 10 | Carta | Sem design: uma coluna, texto preto, assinatura. Parece pessoal. |
