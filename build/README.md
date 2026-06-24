# build/ — gerador das 6 páginas de venda

As 6 PVs (`publicado`, `escrevendo`, `lancando` + variantes `-lista`) são ~85-98%
idênticas. Em vez de editar 6 arquivos de ~4.500 linhas na mão, edite **um** arquivo
de conteúdo e rode **um** script.

## Como editar a copy

1. Abra `build/content.py`.
2. Encontre a página (`"publicado"`, `"escrevendo"`, `"lancando"`,
   `"publicado-lista"`, `"escrevendo-lista"`, `"lancando-lista"`).
3. Edite o valor do token desejado (são strings triple-quoted, fáceis de mexer).
4. Regere (passo abaixo).

## Como regerar

```
python3 build/generate.py
```

Isso reescreve os 6 `.html` na raiz do repositório a partir de:

- `build/template-preco.html`  — molde da variante PREÇO (checkout Hotmart)
- `build/template-lista.html`  — molde da variante LISTA (lista de espera)
- `build/content.py`           — a copy de cada página, por token

O gerador é **self-contained**: lê apenas os 2 templates + `content.py`. Ele NÃO lê
os 6 HTML originais. Ele falha com erro claro se sobrar qualquer `{{TOKEN}}` sem
substituir, ou se algum token do conteúdo não tiver placeholder no template.

## Garantia byte-idêntica

Os templates foram extraídos dos arquivos `publicado.html` (preço) e
`publicado-lista.html` (lista) usando âncoras estáveis. Rodar `generate.py` sem
mudar `content.py` reproduz os 6 arquivos **byte a byte** (verificável com
`git diff --stat`, que fica vazio).

## Tokens (por página)

`variant` (escolhe o template) + `STAGE_SLUG` (slug usado no JS) + os blocos de copy:

| Token | O que é |
|---|---|
| `SEO_HEAD` | Bloco do `<head>`: title, description, og/twitter, canonical, og:url |
| `LDJSON` | O `<script application/ld+json>` (schema; lista não tem `offers`) |
| `HERO_BADGE_H1` | `hero-badge` + `<h1>` |
| `HERO_WATCH` | Texto do `<p class="hero-watch">` |
| `CTA_POSVIDEO` | Texto do `<p>` do CTA pós-vídeo |
| `AGITATION_BLOCK` | Bloco inteiro da AGITAÇÃO + pull-quote da TESE (cobre a variância estrutural de `lancando`) |
| `JOURNEY_TITLE` | `<h2 class="section-title">` da Jornada |
| `JOURNEY_STEPS` | Os 7 passos (`journey-steps` inner) |
| `PC_TEXT` | `<h2 class="pc-text">` |
| `MENTORIA` | `<p>` "Você valida cada decisão…" |
| `GARANTIA_CLOSE` | Markup de fechamento antes de BLOCO 12 (cobre o wrapper extra de `lancando`) |
| `FAQ_LIST` | Itens `<details>` do `faq-list` |
| `FINAL_CTA` | `<h2>` + `<p>` do CTA final |

## Bootstrap (referência)

`build/_extract.py` é o script **one-off** que extraiu os templates + `content.py`
dos 6 HTML reais. Não é usado em runtime; fica só como documentação de como os
moldes foram derivados. Para refazer o bootstrap a partir dos HTML atuais:
`python3 build/_extract.py`.
