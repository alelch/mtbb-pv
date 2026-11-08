# 01/11/2026 · Página de VENDA da Black Week Motorizada, feita do zero (cliente: "você está muito apegado ao que a gente
# tinha antes"; "quero uma coisa magnânima, onde o autor fale: nossa, essa é a melhor chance possível!").
# Nada da página de cadastro: abertura de oferta, a pilha de tudo o que entra (pacote do Aniversário sem o Retiro),
# o LOMBADA em telas reais, bônus do dia 9, Dany, preço, dúvidas, fecho.
# Só o logo da Black e o wordmark do LOMBADA vêm da black-week/ (marca). Saída: ae8a9e17e350/index.html
# Modo: até 23h59 de 9/11 (Brasília) = "dia 9" (LOMBADA 6 anos + relógio); depois = LOMBADA 3 anos. Os Playbooks ficam
# na oferta nos dois modos (cliente 02/11: "os playbooks não terminam meia-noite, só o dobro de acesso ao LOMBADA").
# Prévia: ?modo=d9 ou ?modo=depois força o modo.
import os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bw = open(f"{R}/black-week/index.html", encoding="utf-8").read()
BWLOGO = re.search(r'<div class="bwlogo".*?MOTORIZADA</span></span></div>', bw).group(0)
BWCSS = "\n".join(l for l in bw.split("\n")[132:142])

LMB = '<span class="lmb" role="img" aria-label="LOMBADA"><svg class="lmb-ic" viewBox="8 10 84 82" aria-hidden="true"><rect x="8" y="30" width="20" height="62" rx="3" fill="#14523e"/><rect x="30" y="16" width="22" height="76" rx="3" fill="#faab00"/><rect x="54" y="24" width="18" height="68" rx="3" fill="#b5402e"/><rect x="74" y="10" width="18" height="82" rx="3" fill="currentColor"/><rect x="12" y="78" width="12" height="3" fill="#f3f0e8" opacity=".85"/><rect x="12" y="84" width="12" height="3" fill="#f3f0e8" opacity=".85"/><rect x="34" y="78" width="14" height="3" fill="#fff" opacity=".85"/><rect x="34" y="84" width="14" height="3" fill="#fff" opacity=".85"/><circle cx="63" cy="36" r="4" fill="#f3f0e8"/><rect x="78" y="78" width="10" height="3" fill="#faab00"/><rect x="78" y="84" width="10" height="3" fill="#faab00"/></svg>LOMBADA</span>'
SETA = '<svg viewBox="0 0 30 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12h25M21 6l6 6-6 6"/></svg>'
CK = '<svg class="ck" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
CTA = f'<a class="btn" href="#oferta" data-cta>Quero entrar na Black {SETA}</a>'
CLOCK = '<div class="clock" data-clock aria-label="Tempo até a meia-noite"></div>'

# a pilha: o pacote do Aniversário (thebookbusiness.com.br/aula-8-semanas), sem o Retiro; encontros por 3 anos
PILHA = [
    ("Método The&nbsp;Book&nbsp;Business", "Toda a estratégia, do primeiro livro ao décimo.", "Vitalício"),
    ("Autoridade Digital para Escritores", "Quais redes usar, o que postar e como ser descoberto.", "Vitalício"),
    ("Comunidade The&nbsp;Book&nbsp;Business", "Mais de 2.000 escritores. A sua nova turma.", "Vitalício"),
    ("Workshop MasterClass Best-Seller de Verdade", "", "Vitalício"),
    ("Workshop Redes Sociais para Autores", "", "Vitalício"),
    ("Workshop Prêmios e Concursos Literários", "", "Vitalício"),
    ("Workshop Escrita Criativa", "", "Vitalício"),
    ("Workshop Planejamento Anual", "", "Vitalício"),
    ("Gravação de 100% das lives, encontros e eventos", "Com roteiristas premiadas, agentes literárias e publishers das maiores editoras.", "Vitalício"),
    ("Encontros em grupo ao vivo com a Dany", "Todo mês, para ajustar a estratégia do seu livro.", "3 anos"),
]
rows = "\n".join(
    f'        <li class="row rv"><span class="row__n">{i:02d}</span><span class="row__t"><b>{t}</b>{f"<small>{d}</small>" if d else ""}</span><span class="row__k">{k}</span></li>'
    for i, (t, d, k) in enumerate(PILHA, 1))
N = len(PILHA) + 1  # + LOMBADA
rows += f'''
        <li class="row row--lmb rv"><span class="row__n">{N:02d}</span><span class="row__t"><b>{LMB}</b><small>O personal trainer do seu livro. Todo dia, o que fazer.</small></span><span class="row__k"><span class="d9-only">6 anos</span><span class="after-only">3 anos</span></span></li>
        <li class="row row--bonus rv"><span class="row__n">{N+1:02d}</span><span class="row__t"><b>Playbooks MTBB físicos, na sua casa</b></span><span class="row__k">Bônus</span></li>'''

TELAS = [
    ("tela-semana", "A semana do seu livro", "Ele abre com as ações da semana, feitas para o seu livro."),
    ("tela-acoes", "Uma ação por vez", "Com o tempo de cada uma e a aula por trás."),
    ("tela-oportunidades", "Prêmios, feiras e editais", "Do gênero do seu livro, com o prazo na tela."),
    ("tela-evolucao", "A sua evolução", "Selo por selo, a prova de que o seu livro anda."),
    ("tela-posts", "Ideias de post ilimitadas", "Responda 3 perguntas e gere quantas quiser."),
]
telas = "\n".join(
    f'''        <figure class="tela rv"><div class="tela__ph"><img src="assets/{f}.webp" alt="Tela do LOMBADA: {t}" width="716" height="1440" loading="lazy" decoding="async"></div><figcaption><b>{t}</b><span>{d}</span></figcaption></figure>'''
    for f, t, d in TELAS)


BILL = "".join(f'<div class="bill__row"><span>{n.replace("The Book Business", "The&nbsp;Book&nbsp;Business")}</span><b>{v}</b></div>' for n, v in [('Método The Book Business', 'R$ 1.500,00'), ('Autoridade Digital para Escritores', 'R$ 1.500,00'), ('Comunidade The Book Business', 'R$ 500,00'), ('Workshop MasterClass Best-Seller de Verdade', 'R$ 797,00'), ('Workshop Redes Sociais para Autores', 'R$ 797,00'), ('Workshop Prêmios e Concursos Literários', 'R$ 797,00'), ('Workshop Escrita Criativa', 'R$ 797,00'), ('Workshop Planejamento Anual', 'R$ 797,00')])  # 08/11 cliente: workshops R$797/ano cada, só no 1º ano
_ST = [
  ("tela-semana", "Segunda, 9h", "O seu celular avisa. E o plano da semana já está pronto.", "Montado pela fase do seu livro, pelo gênero e pelo tempo que você tem."),
  ("tela-acoes", "Terça", "Uma ação por vez. Com o texto pronto e a aula por trás.", "O texto já vem com o nome do seu livro. E a aula do Método The Book Business explica o porquê."),
  ("tela-posts", "Quarta", "O post da semana, pronto. E ideias sem fim.", "3 ideias de post toda semana e um gerador ilimitado, feito para o seu livro."),
  ("tela-oportunidades", "Quinta", "Um prêmio do seu gênero aparece. Com o prazo na tela.", "Prêmios, feiras, editais e datas literárias. Nenhuma chance passa por você."),
  ("tela-evolucao", "Sexta", "Você marca como feito. E vê o seu livro andando.", "Uma lombada nova na sua estante a cada ação. Selo por selo, a prova de que ele não parou."),
]
STORY_BARS = "".join('<i><b></b></i>' for _ in _ST)
STORY_TABS = "".join(f'<button type="button" class="{"on" if not i else ""}" data-i="{i}">{d.split(",")[0][:3]}</button>' for i, (f, d, t, x) in enumerate(_ST))
_LZ = ' loading="lazy"'
_ON = ' class="on"'
STORY_IMGS = "".join(f'<img src="assets/{f}.webp" alt="Tela do LOMBADA" width="716" height="1440" decoding="async"{_LZ if i else ""}{"" if i else _ON}>' for i, (f, dia, t, d) in enumerate(_ST))
STORY_TXT = "".join(f'<div class="st{" on" if not i else ""}"><span class="st__n">{dia}</span><p class="st__t">{t}</p><p class="st__d">{d}</p></div>' for i, (f, dia, t, d) in enumerate(_ST))

_CASOS = [("c0","Vinicius Profinho","11 mil cópias vendidas","O Guia da Redação Nota 1000"),("c9","Emília Nunez","Ganhadora do Prêmio Jabuti","Capaz"),("c33","Candice Pascoal","Mais de 50 mil exemplares","Seu Sonho Tem Futuro"),("c3","Lelo Apovian","Best-seller Veja, Amazon e PublishNews","Muito Acima da Média"),("c6","Tom Orgado","Destaque de vendas na Bienal do Rio","Baque"),("c16","Maíra Metelo","6º mais vendido da Amazon","Se Ninguém Soubesse Quem Sou"),("c18","Maria Gravina Ogata","8 prêmios literários","As bambinas e os samurais brasileiros"),("c30","Larissa Cruvinel","Leitores em 7 países","A Serenidade da Renúncia"),("c28","Susana Arbex","1º lugar em negócios na PublishNews","Sua Marca Pessoal"),("c35","Léo Dicker","Adotado por escolas","Clara e Guto, os segredos de Londres"),("c34","Simone Simon","Nas livrarias de aeroportos","Faça Ser Fácil"),("c7","Ingrid Azevedo","Quase 600 na pré-venda","O caminho do despertar")]
CASOS = "".join(f'<figure class="caso rv"><img src="../black-week-misterio/assets/casos/{f}.webp" alt="{n}" width="56" height="56" loading="lazy" decoding="async"><figcaption><strong>{r}</strong><b>{n}</b><span>{l}</span></figcaption></figure>' for f, n, r, l in _CASOS)
_LEVA = [
  ("Acesso vitalício", "Método The&nbsp;Book&nbsp;Business", "O ecossistema completo de marketing literário. Aulas práticas, passo a passo claro e modelos prontos para transformar o seu livro em referência, com leitores de verdade."),
  ("Acesso vitalício", "Autoridade Digital para Escritores", "Quais redes usar, o que postar e com que frequência para multiplicar o seu alcance e ser descoberto por novos leitores."),
  ("Acesso vitalício", "Comunidade The&nbsp;Book&nbsp;Business", "A maior comunidade de autores do Brasil, com mais de 2.000 escritores. A sua nova turma."),
  ("Acesso vitalício", "Workshops Mão na Massa", "<ul><li>MasterClass Best-Seller de Verdade</li><li>Redes Sociais para Autores</li><li>Prêmios e Concursos Literários</li><li>Escrita Criativa</li><li>Planejamento Anual</li></ul>"),
  ("Acesso vitalício", "Gravação de 100% das lives, encontros e eventos", "Para rever quando quiser. Com roteiristas premiadas, agentes literárias e publishers das maiores editoras do país."),
  ("3 anos", "Encontros em grupo ao vivo com a Dany", "36 encontros ao vivo com a Dany para tirar dúvidas e ajustar a estratégia do seu livro. O que muitos chamam de mentoria, aqui está incluído."),
]
_IMG = ["p-metodo", "p-autoridade", "p-comunidade", "p-workshops", "p-gravacoes", "p-encontros"]
def _tag(k):
    return k
LEVA = "".join(f'<div class="lv rv"><img class="lv__img" src="assets/{_IMG[n]}.webp" alt="" width="720" height="567" loading="lazy" decoding="async"><div class="lv__b"><span class="lv__k">{_tag(k)}</span><h3>{t}</h3>{d if d.startswith("<ul>") else f"<p>{d}</p>"}</div></div>' for n, (k, t, d) in enumerate(_LEVA) if n > 0)
# cupons dos parceiros (valores e regras passados pelo cliente em 01/11; Literare R$2.000 confirmada no mesmo dia: total R$6.700)
_CUP = [("Gráfica Renograf", "Impressão do seu livro", "até R$ 1.200", "Desconto progressivo pelo valor da impressão. Vale reimpressão."),
        ("Histórias Bem Contadas", "Leitura crítica", "R$ 250", "Válido por 24 meses."),
        ("Histórias Bem Contadas", "Edição de texto", "R$ 250", "Válido por 24 meses."),
        ("Jimenes Comunicação", "Assessoria de imprensa", "R$ 2.000", "Projeto semestral. Válido por 24 meses."),
        ("Editora Labrador", "Publicação do seu livro solo", "R$ 1.000", "Válido por 12 meses."),
        ("Editora Literare", "Publicação do seu livro solo", "R$ 2.000", "Válido por 12 meses.")]
CUPONS = "".join(f'<div class="cup rv"><div class="cup__v"><small>Cupom de</small><b>{v}</b></div><div class="cup__t"><span>{q}</span><h3>{n}</h3><p>{d}</p></div></div>' for n, q, v, d in _CUP)

# 01/11 (cliente: "a parte do test drive da primeira versão era legal, só a parte do LOMBADA volta"):
# test drive + oportunidades + ideias de post da black-week/ voltam como estavam (markup, CSS e JS próprios)
_BL = bw.split("\n")
_body = bw[bw.index("<main>"):bw.index("</main>")]
def _bloco(a, b):
    x = _body.index(a); return _body[x:_body.index(b, x)]
DEMO_DRIVE = _bloco('<section class="blk drive"', '<!-- 4.').replace('class="blk drive"', 'class="lmbx drive"')
DEMO_DRIVE = DEMO_DRIVE.replace('<p class="eyebrow">Test drive</p>', '<p class="eyebrow">1 · Seu livro não para</p>') \
    .replace('Instale um motor no seu livro.', 'Toda semana, o seu livro anda.') \
    .replace('Escreva o nome dele. Escolha a fase. A sua segunda-feira aparece na hora.', 'O LOMBADA monta o plano da semana do seu livro. Você só executa. Escreva o nome dele e veja a sua semana aparecer.')
DEMO_MOTOR = _bloco('<section class="blk" id="mais-motor">', '<!-- 5.').replace('class="blk" id="mais-motor"', 'class="lmbx" id="mais-motor"')
_KW = ('drive', 'feat', 'panel', 'phone', 'screen', 'app-', 'ops', 'idea', '.seg', 'ctrl', 'try', 'pills', 'q__l', 'gen-btn', 'ideas', '.op', '.act', '.ia', '.chip', 'td-', 'pulse', 'caret', '.bk', '.vr')
def _media(a, b, cond):
    ls = [l for l in _BL[a-1:b] if l.startswith('  .') and any(k in l for k in _KW)]
    return f"@media {cond} {{\n" + "\n".join(ls) + "\n}" if ls else ""
DEMO_MOTOR = DEMO_MOTOR.replace('<p class="eyebrow">E não para na segunda</p>', '<p class="eyebrow">E o seu livro</p>') \
    .replace('<h2 class="h2">Tem mais motor aí dentro.</h2>', '<h2 class="h2">Vai mais longe. <span class="amber">E é lido.</span></h2>') \
    .replace('<p class="feat__k">Oportunidades</p>', '<p class="feat__k">2 · Seu livro vai mais longe</p>') \
    .replace('Prêmios, feiras e editais. <span class="amber">Não perca nenhuma chance de ver o seu livro brilhar.</span>', 'Prêmios, feiras e editais levam o seu livro a lugares novos. <span class="amber">E você nunca perde o prazo.</span>') \
    .replace('<p class="feat__k">Ideias de post ilimitadas</p>', '<p class="feat__k">3 · Seu livro é lido</p>') \
    .replace('Faça suas redes sociais <span class="amber">decolarem.</span>', 'Novos leitores encontram o seu livro. <span class="amber">Toda semana.</span>')
DEMO_CSS = "\n".join([
    "\n".join(_BL[97:102]),            # .eyebrow e .lede
    "\n".join(_BL[180:205]),           # telas do app
    "\n".join(_BL[289:396]),           # test drive + tem mais motor
    _media(495, 548, "(min-width: 900px)"),
    _media(549, 562, "(min-width: 900px) and (max-width: 1179px)"),
    _media(563, 586, "(max-width: 899px)"),
    _media(587, 600, "(max-width: 520px)"),
    "\n".join(l for l in _BL[601:617] if l.startswith("@keyframes") and "gold" not in l),
    ".lmbx { position: relative; padding: var(--sec) 0; }",
])
_i = bw.index("  /* ================= utilidades"); _j = bw.index("  /* ================= 5. ESTEIRA")
DEMO_JS = "<script>\n(function () {\n  'use strict';\n" + bw[_i:_j] + "})();\n</script>"

_mis = open(f"{R}/black-week-misterio/index.html", encoding="utf-8").read()
CASOS_BELT = _mis[_mis.index('<div class="casos">'):_mis.index('<!-- depois dos alunos')].replace('src="assets/casos/', 'src="../black-week-misterio/assets/casos/')
CASOS_CSS = "\n".join(l for l in _mis.split("\n") if l.startswith(('.casos', '.caso', '.rm .casos')) or l.startswith('  -webkit-mask-image: linear-gradient(90deg, transparent, #000 7%'))
_VID = [("MVWV1r5AFqM", "Lelo Apovian"), ("ffBPbjjEWd4", "Vinicius Profinho"), ("FKATT3aFxOM", "Emília Nunez"), ("dwfYj5r0-Gs", "Candice Pascoal"),
        ("bOgr78gqu5w", "Susana Arbex"), ("6Zpwi9VAtMg", "Tonia Casarin"), ("0wa0Zg28OUw", "Arnoni Caldart"), ("RGlPbXowLWw", "Léo Dicker"),
        ("2jrXvu11h78", "Simone Simon"), ("hW7NjsY2WrA", "Robson Leite"), ("E8K6Bd2A12w", "Cibele Lauretino"), ("8vlXq0HOO6Q", "José Julio Cerquetane")]
VIDEOS = "".join(f'<button type="button" class="vid" data-yt="{v}" aria-label="Assistir ao depoimento de {n}"><img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="Depoimento de {n}" width="480" height="360" loading="lazy" decoding="async"><span class="vid__play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="currentColor"/></svg></span><span class="vid__n">{n}</span></button>' for v, n in _VID)
_MID = [("band", "Band"), ("sbt", "SBT"), ("bienal-do-livro", "Bienal do Livro"), ("premio-publishnews", "Prêmio PublishNews"), ("hotmart-festival", "Hotmart Festival"), ("mauricio-de-sousa", "Com Maurício de Sousa"), ("band-entrevista", "Band Entrevista")]
MIDIA = "".join(f'<figure><img src="../black-week/assets/midia/{f}.webp" alt="Dany Sakugawa: {n}" width="220" height="140" loading="lazy" decoding="async"><figcaption>{n}</figcaption></figure>' for f, n in _MID)
_ji = bw.index("  var ALL = '*';"); _jj = bw.index("  var MES = [")
_ki = bw.index("  var IDEIAS = {"); _kj = bw.index("  var IC = {")
JN_DADOS = bw[_ji:_jj] + bw[_ki:_kj]
LMB_S = '<span class="ap__lmb">' + LMB + '</span>'
SPINES = '<div class="spines" aria-hidden="true"><i style="--h:62%;--c:#14523e"></i><i style="--h:84%;--c:#faab00"></i><i style="--h:70%;--c:#b5402e"></i><i style="--h:100%;--c:#f3f0e8"></i><i style="--h:56%;--c:#fc783c"></i><i style="--h:78%;--c:#3a3530"></i></div>'
HTML = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Black Week Motorizada · A maior oferta de todos os tempos</title>
<meta name="description" content="Tudo o que a Dany Sakugawa criou para autores, pra sempre. E o LOMBADA, o personal trainer do seu livro. Na Black Week Motorizada.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#000000">
<link rel="canonical" href="https://metodo.thebookbusiness.com.br/ae8a9e17e350/">
<link rel="icon" type="image/webp" href="../lancamento90d/favicon.webp">
<meta property="og:type" content="website">
<meta property="og:url" content="https://metodo.thebookbusiness.com.br/ae8a9e17e350/">
<meta property="og:site_name" content="The Book Business">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="A maior oferta de todos os tempos + LOMBADA">
<meta property="og:description" content="Inscrições liberadas na Black Week Motorizada. Método The Book Business vitalício + LOMBADA: leva o seu livro cada vez mais longe.">
<meta property="og:image" content="https://metodo.thebookbusiness.com.br/ae8a9e17e350/assets/og-oferta.jpg">
<meta property="og:image:secure_url" content="https://metodo.thebookbusiness.com.br/ae8a9e17e350/assets/og-oferta.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Black Week Motorizada: a maior oferta de todos os tempos + LOMBADA">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://metodo.thebookbusiness.com.br/ae8a9e17e350/assets/og-oferta.jpg">
<link rel="preload" as="font" type="font/woff2" crossorigin href="../assets/fonts/poppins-800.woff2">
<script src="../pixel.js"></script>
<script src="../gtag.js" defer></script>
<style>
@font-face {{ font-family: "Poppins"; font-weight: 400; font-display: swap; src: url("../assets/fonts/poppins-400.woff2") format("woff2"); }}
@font-face {{ font-family: "Poppins"; font-weight: 500; font-display: swap; src: url("../assets/fonts/poppins-500.woff2") format("woff2"); }}
@font-face {{ font-family: "Poppins"; font-weight: 600; font-display: swap; src: url("../assets/fonts/poppins-600.woff2") format("woff2"); }}
@font-face {{ font-family: "Poppins"; font-weight: 700; font-display: swap; src: url("../assets/fonts/poppins-700.woff2") format("woff2"); }}
@font-face {{ font-family: "Poppins"; font-weight: 800; font-display: swap; src: url("../assets/fonts/poppins-800.woff2") format("woff2"); }}
@font-face {{ font-family: "Montserrat"; font-weight: 500; font-display: swap; src: url("../black-week/assets/fonts/montserrat-500-latin.woff2") format("woff2"); }}
@font-face {{ font-family: "Montserrat"; font-style: italic; font-weight: 900; font-display: swap; src: url("../black-week/assets/fonts/montserrat-900i-latin.woff2") format("woff2"); }}
@font-face {{ font-family: "Archivo LMB"; font-weight: 900; font-display: swap; src: url("../black-week/assets/fonts/archivo-900-latin.woff2") format("woff2"); }}

:root {{
  --bg: #000; --bg2: #0b0a09; --ink: #fff; --ink2: #cfc9bd; --ink3: #8a8478; --line: #24211c;
  --amber: #faab00; --yellow: #ffcc00; --green: #1ebb00;
  --paper: #f3f0e8; --paper-ink: #1a1a1a; --paper-soft: #6b665d;
  --gold: linear-gradient(100deg, #9c5414 0%, #e08a12 18%, #faab00 32%, #ffe6a8 46%, #faab00 58%, #c9731a 78%, #8a4a12 100%);
  --ease: cubic-bezier(.22, 1, .36, 1);
  --pop: cubic-bezier(.34, 1.56, .64, 1);
  --ink-2: #d2cec6; --ink-3: #8b877f; --bg-2: #0a0a0b; --sec: 64px; --gutter: 20px;
  --f-construcao: #3fae84; --f-lancamento: #fc783c; --f-permanencia: #faab00;
  --app-paper: #f3f0e8; --app-ink: #1a1a1a; --app-soft: #6b665d; --app-line: #e3ded2; --app-chip: #efe9dc; --app-ochre: #8a5a00;
}}
*, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
html {{ -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }}
body {{ background: var(--bg); color: var(--ink); font: 400 16px/1.5 "Poppins", system-ui, sans-serif; -webkit-font-smoothing: antialiased; overflow-x: clip; }}
img {{ display: block; max-width: 100%; height: auto; }}
a {{ color: inherit; }}
p, li, small {{ text-wrap: pretty; }}
.wrap {{ width: 100%; max-width: 1120px; margin: 0 auto; padding: 0 20px; }}
.gold {{ background: var(--gold); background-size: 220% 100%; -webkit-background-clip: text; background-clip: text; color: transparent; animation: gold 6s linear infinite; -webkit-box-decoration-break: clone; box-decoration-break: clone; }}
.serif {{ font-style: normal; font-weight: 800; }}
.kick {{ display: inline-flex; align-items: center; gap: 10px; font-size: 12px; font-weight: 600; letter-spacing: .26em; text-transform: uppercase; color: var(--amber); }}
.kick::before, .kick::after {{ content: ""; width: 22px; height: 1.5px; background: currentColor; opacity: .7; }}
.sec {{ position: relative; padding: 88px 0; }}
@media (min-width: 900px) {{ .sec {{ padding: 130px 0; }} }}
.center {{ text-align: center; }}
.h2 {{ margin-top: 16px; font-size: clamp(34px, 9.4vw, 72px); font-weight: 800; line-height: 1.02; letter-spacing: -.03em; text-wrap: balance; }}
body:not(.m-d9) .d9-only, body:not(.m-depois) .after-only {{ display: none !important; }}

/* marca */
{BWCSS}
.lmb {{ display: inline-flex; align-items: center; white-space: nowrap; font: 900 1em/1 "Archivo LMB", "Arial Black", Impact, sans-serif; letter-spacing: -.03em; }}
.lmb-ic {{ flex: none; width: .84em; height: .82em; margin-right: .26em; position: relative; top: -.03em; }}

/* botão */
.btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 10px; width: 100%; min-height: 62px; padding: 0 18px; border: 0; border-radius: 8px;
  background: var(--green); color: #fff; text-decoration: none; cursor: pointer; font: 700 clamp(17px, 4.8vw, 22px)/1 "Poppins", sans-serif; letter-spacing: .01em; text-transform: uppercase;
  box-shadow: 0 18px 40px -18px rgba(30, 187, 0, .9); transition: transform .15s, filter .2s; }}
.btn:hover {{ filter: brightness(1.07); transform: translateY(-2px); }}
.btn svg {{ flex: none; width: 26px; height: 20px; }}
.fine {{ margin-top: 12px; font-size: 13px; color: var(--ink2); text-align: center; }}

/* relógio */
.clock {{ display: flex; justify-content: center; gap: 6px; font-variant-numeric: tabular-nums; }}
.clock span {{ min-width: 56px; padding: 8px 4px 6px; border-radius: 8px; background: #000; box-shadow: inset 0 0 0 1px #3d372a; font-size: 24px; font-weight: 800; line-height: 1; text-align: center; }}
.clock small {{ display: block; margin-top: 4px; font-size: 9px; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; color: var(--ink3); }}

/* barra do topo */
.obar {{ position: sticky; top: 0; z-index: 50; display: flex; align-items: center; justify-content: center; gap: 12px; padding: 8px 12px; background: var(--yellow); color: #111; }}
.obar p {{ max-width: 150px; font-size: 11px; font-weight: 800; line-height: 1.2; letter-spacing: .04em; text-transform: uppercase; }}
.obar p.after-only {{ max-width: none; padding: 5px 0; font-weight: 600; }}
.obar .clock {{ gap: 4px; }}
.obar .clock span {{ min-width: 40px; padding: 4px 3px; background: #111; color: #fff; box-shadow: none; font-size: 17px; border-radius: 6px; }}
.obar .clock small {{ margin-top: 2px; font-size: 7.5px; color: #bbb; }}
@media (min-width: 900px) {{ .obar p {{ max-width: none; font-size: 13px; }} .obar .clock span {{ min-width: 48px; font-size: 20px; }} }}

/* 1. abertura */
.h {{ position: relative; overflow: hidden; isolation: isolate; padding: 34px 0 80px; text-align: center; }}
.h::before {{ content: ""; position: absolute; left: 50%; top: -110vmax; width: 160vmax; height: 160vmax; margin-left: -80vmax; z-index: -1; pointer-events: none;
  background: repeating-conic-gradient(from 0deg, rgba(250, 171, 0, .13) 0deg 5deg, transparent 5deg 18deg);
  -webkit-mask-image: radial-gradient(closest-side, #000 10%, transparent 70%); mask-image: radial-gradient(closest-side, #000 10%, transparent 70%); animation: rays 90s linear infinite; }}
.h::after {{ content: ""; position: absolute; left: 50%; top: 0; width: 120vmax; height: 70vmax; z-index: -1; transform: translate(-50%, -45%); border-radius: 50%; background: radial-gradient(closest-side, rgba(250, 171, 0, .22), transparent); pointer-events: none; }}
.h__in {{ width: 100%; }}
.h .bwlogo {{ font-size: clamp(30px, 8vw, 46px); animation: rise 1s var(--ease) both; }}
.h__kick {{ display: flex; justify-content: center; margin-top: 28px; animation: rise 1s var(--ease) .15s both; }}
/* 08/11 (cliente): "Inscrições liberadas" mais forte */
.h__kick {{ margin-top: 30px; font-size: clamp(13px, 3.6vw, 17px); font-weight: 800; letter-spacing: .24em; gap: 14px; text-shadow: 0 0 18px rgba(250,171,0,.35); }}
.h__kick::before, .h__kick::after {{ width: clamp(26px, 6vw, 44px); height: 2px; opacity: 1; }}
.h__t {{ margin: 18px auto 0; max-width: 1080px; animation: rise 1.1s var(--ease) .25s both; }}
.h__a {{ display: block; font-size: clamp(30px, 8.6vw, 74px); font-weight: 800; line-height: 1.02; letter-spacing: -.035em; text-wrap: balance; }}
.h__b {{ display: block; margin-top: 4px; padding-bottom: .08em; font-size: clamp(76px, 24vw, 200px); line-height: .9; }}
.h__plus {{ margin-top: 18px; font-size: clamp(16px, 4.5vw, 22px); color: var(--ink2); animation: rise 1s var(--ease) .45s both; text-wrap: balance; }}
.h__plus .lmb {{ color: var(--ink); font-size: 1.35em; vertical-align: -.12em; }}
.h__price {{ display: inline-flex; align-items: baseline; gap: 8px; margin-top: 28px; padding: 10px 20px; border-radius: 99px; background: rgba(250, 171, 0, .1); box-shadow: inset 0 0 0 1px rgba(250, 171, 0, .5); animation: rise 1s var(--ease) .55s both; }}
.h__price span {{ font-size: 14px; color: var(--ink2); }}
.h__price b {{ font-size: clamp(22px, 6vw, 28px); font-weight: 800; }}
.h .cta {{ max-width: 480px; margin: 22px auto 0; }}
.h__cue {{ display: inline-flex; flex-direction: column; align-items: center; gap: 6px; margin-top: 34px; font-size: 12px; font-weight: 600; letter-spacing: .2em; text-transform: uppercase; color: var(--ink3); text-decoration: none; }}
.h__cue svg {{ width: 20px; height: 20px; animation: bob 1.8s ease-in-out infinite; }}

/* bônus com o mesmo peso: mesma largura, mesma área de imagem, mesmo título */

.bon2__c {{ display: flex; flex-direction: column; align-items: center; }}
.bon2__vis {{ display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; height: 280px; margin-top: 14px; }}
.bon2__c .bon2__vis img {{ width: auto; max-width: 100%; height: 100%; margin: 0; object-fit: contain; }}
.bon2__vis .dbl {{ margin-top: 0; }}
.bon2__vis .dbl b {{ font-size: clamp(26px, 7vw, 40px); }}
.bon2__vis .dbl__b b {{ font-size: clamp(46px, 13vw, 72px); }}
.bon2__vis .spines {{ height: 110px; margin-top: 22px; }}
.bon2__c h3 {{ font-size: clamp(20px, 5.4vw, 28px); }}
/* bônus lado a lado, com o mesmo peso (cliente: "preferia lado a lado") */
@media (min-width: 760px) {{ .bon2.bon2 {{ grid-template-columns: repeat(2, minmax(0, 1fr)); max-width: 980px; }} }}
/* depois do dia 9 sobra só o cartão dos Playbooks: uma coluna, centralizada */
@media (min-width: 760px) {{ body.m-depois .bon2.bon2 {{ grid-template-columns: minmax(0, 1fr); max-width: 480px; }} }}
.bon2__txt {{ display: contents; }}
.bon2__c > .bon2__txt > .lv__k, .bon2__c .bon2__txt .lv__k {{ order: -1; }}
.bon2__txt h3 {{ margin-top: 12px; }}
/* vídeos dos alunos e garantia */
.vids {{ display: flex; gap: 12px; margin: 36px -20px 0; padding: 0 20px 8px; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; }}
.vids::-webkit-scrollbar {{ display: none; }}
@media (min-width: 900px) {{ .vids {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 40px auto 0; padding: 0; overflow: visible; max-width: 1080px; }} }}
.vid {{ position: relative; flex: none; width: 82vw; max-width: 420px; aspect-ratio: 16 / 9; overflow: hidden; border: 0; border-radius: 14px; padding: 0; background: #111; cursor: pointer; scroll-snap-align: center; box-shadow: 0 0 0 1px #2a2620; }}
@media (min-width: 900px) {{ .vid {{ width: auto; max-width: none; }} }}
.vid img {{ width: 100%; height: 100%; object-fit: cover; transition: transform .4s var(--ease); }}
.vid:hover img {{ transform: scale(1.04); }}
.vid__play {{ position: absolute; left: 50%; top: 50%; display: grid; place-items: center; width: 58px; height: 58px; margin: -29px 0 0 -29px; border-radius: 50%; background: rgba(0, 0, 0, .6); color: #fff; box-shadow: 0 0 0 2px rgba(250, 171, 0, .9); }}
.vid__play svg {{ width: 26px; height: 26px; margin-left: 3px; }}
.vid__n {{ position: absolute; left: 10px; bottom: 10px; padding: 4px 10px; border-radius: 99px; background: rgba(0, 0, 0, .7); font-size: 12px; font-weight: 700; color: #fff; }}
.vid iframe {{ position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }}
.vids__k {{ margin-top: 40px; text-align: center; font-size: clamp(17px, 4.6vw, 22px); font-weight: 700; }}
.gar {{ border-top: 1px solid var(--line); }}
.gar__c {{ display: grid; grid-template-columns: minmax(0, 1fr); gap: 22px; align-items: center; max-width: 820px; margin: 0 auto; padding: 30px 22px; border-radius: 22px; background: radial-gradient(ellipse 80% 120% at 0% 50%, rgba(250, 171, 0, .16), transparent 70%), #0d0b08; box-shadow: inset 0 0 0 1.5px rgba(250, 171, 0, .45); text-align: center; }}
@media (min-width: 760px) {{ .gar__c {{ grid-template-columns: 200px 1fr; text-align: left; padding: 36px 40px; }} }}
.gar__seal {{ display: flex; flex-direction: column; align-items: center; justify-content: center; width: 170px; height: 170px; margin: 0 auto; border-radius: 50%; background: var(--gold); color: #111; box-shadow: 0 0 0 8px rgba(250, 171, 0, .15), 0 20px 40px -16px rgba(250, 171, 0, .6); }}
.gar__seal b {{ font-size: 72px; font-weight: 800; line-height: .9; letter-spacing: -.04em; }}
.gar__seal span {{ margin-top: 4px; font-size: 12px; font-weight: 800; line-height: 1.2; letter-spacing: .14em; text-transform: uppercase; text-align: center; }}
.gar__t h2 {{ font-size: clamp(28px, 7.6vw, 44px); font-weight: 800; line-height: 1.05; letter-spacing: -.03em; }}
.gar__t p {{ margin-top: 12px; font-size: clamp(15px, 4.2vw, 18px); line-height: 1.6; color: var(--ink2); }}

/* bônus em dobro, lombadinhas e o quadro especial do LOMBADA */
.dbl {{ display: flex; align-items: center; justify-content: center; gap: 14px; margin-top: 18px; }}
.dbl > div {{ text-align: center; }}
.dbl b {{ display: block; white-space: nowrap; font-size: clamp(26px, 7.4vw, 46px); font-weight: 800; line-height: 1; letter-spacing: -.03em; }}
.dbl__a b {{ color: var(--ink3); text-decoration: line-through; text-decoration-thickness: 3px; text-decoration-color: rgba(214, 72, 60, .9); }}
.dbl__b b {{ font-size: clamp(46px, 13.5vw, 84px); }}
.dbl small {{ display: block; margin-top: 4px; font-size: 11px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: var(--ink3); }}
.dbl__b small {{ color: var(--amber); }}
.dbl__ar {{ font-size: 30px; font-weight: 800; color: var(--amber); }}
.spines {{ display: flex; align-items: flex-end; justify-content: center; gap: 6px; height: 92px; margin: 18px auto 0; }}
.spines i {{ width: 26px; height: var(--h); border-radius: 4px 4px 0 0; background: var(--c); box-shadow: inset 0 -10px 0 rgba(0, 0, 0, .12); }}
.lmbc {{ display: grid; grid-template-columns: minmax(0, 1fr); max-width: 980px; margin: 40px auto 12px; overflow: hidden; border-radius: 22px; background: var(--paper); color: var(--paper-ink); box-shadow: 0 0 0 2px rgba(250, 171, 0, .7), 0 0 60px rgba(250, 171, 0, .25); }}
@media (min-width: 760px) {{ .lmbc {{ grid-template-columns: 5fr 7fr; }} }}
.lmbc__art {{ display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 34px 20px 26px; background: #16110c; }}
.lmbc__art .spines {{ height: 120px; margin: 0; }}
.lmbc__art .spines i {{ width: 30px; }}
.lmbc__mark {{ margin-top: 16px; font-size: clamp(34px, 9vw, 46px); line-height: 1; }}
.lmbc__mark .lmb {{ color: #f3f0e8; }}
.lmbc__b {{ padding: 26px 22px 28px; text-align: left; }}
.lmbc__b .lv__k {{ background: var(--paper-ink); color: var(--amber); }}
.lmbc__b h3 {{ margin-top: 12px; font-size: clamp(24px, 6.4vw, 32px); font-weight: 800; line-height: 1.1; letter-spacing: -.02em; }}
.lmbc__b ul {{ margin-top: 14px; list-style: none; display: grid; gap: 9px; }}
.lmbc__b li {{ position: relative; padding-left: 26px; font-size: 15px; line-height: 1.45; color: var(--paper-soft); }}
.lmbc__b li::before {{ content: ""; position: absolute; left: 0; top: .2em; width: 16px; height: 16px; border-radius: 50%; background: var(--green) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 12.5l4 4L18 8'/%3E%3C/svg%3E") center / 12px no-repeat; }}
.lmbc__btn {{ white-space: nowrap; display: inline-flex; align-items: center; gap: 8px; margin-top: 20px; padding: 13px 18px; border-radius: 99px; background: var(--paper-ink); color: var(--amber); font-size: 13px; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; text-decoration: none; }}
.lmbc__btn svg {{ width: 18px; height: 18px; animation: bob 1.8s ease-in-out infinite; }}
.lmbsec {{ border-top: 1px solid var(--line); padding-bottom: 0; scroll-margin-top: 56px; }}

/* revisão final: ritmo, prova e acabamento */
.lmbx .eyebrow {{ font-size: 12px; letter-spacing: .26em; }}
.lmbx .eyebrow::before {{ height: 1.5px; opacity: .7; }}
.lmbx .h2 {{ font-weight: 800; letter-spacing: -.03em; line-height: 1.04; }}
.lmbx .feat__h {{ font-weight: 800; letter-spacing: -.02em; }}
@media (min-width: 900px) {{ :root {{ --sec: 110px; }} }}
/* prova logo abaixo da abertura */
.proof2 {{ display: flex; width: max-content; max-width: 100%; margin: 0 auto 22px; align-items: center; gap: 10px; padding: 8px 16px 8px 8px; border-radius: 99px; background: rgba(255, 255, 255, .04); box-shadow: inset 0 0 0 1px #2a2620; }}
.proof2 img {{ width: 96px; height: auto; }}
.proof2 span {{ white-space: nowrap; font-size: 12px; color: var(--ink2); text-align: left; line-height: 1.3; }}
.proof2 b {{ color: var(--ink); }}
/* a conta: o total cresce e o preço cai como um golpe */
.bill__tot b {{ transition: transform .6s var(--pop); }}
.bill.in .bill__tot b, .rv.in .bill__tot b {{ transform: scale(1.04); }}
.price__day {{ display: inline-block; margin-top: 14px; padding: 6px 14px; border-radius: 99px; background: rgba(30, 187, 0, .12); color: #7be26a; font-size: 14px; font-weight: 600; }}
/* Dany na mídia */
.midia {{ margin-top: 48px; overflow: hidden; -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); }}
.midia__k {{ margin-top: 56px; text-align: center; }}
.midia__t {{ display: flex; gap: 12px; width: max-content; animation: belt 60s linear infinite; }}
.midia:hover .midia__t {{ animation-play-state: paused; }}
.midia figure {{ flex: none; width: 220px; }}
.midia img {{ width: 220px; height: 140px; object-fit: cover; border-radius: 12px; box-shadow: 0 0 0 1px #2a2620; }}
.midia figcaption {{ margin-top: 8px; font-size: 12px; font-weight: 600; color: var(--ink3); text-align: center; }}
/* fecho com o preço e o relógio */
.end__price {{ margin-top: 26px; }}
.end__price .price__big span {{ font-size: clamp(48px, 13vw, 84px); }}
.end .card__clock {{ max-width: 480px; margin: 22px auto 0; }}
/* seções alternam um fundo levemente mais quente para dar ritmo */
.cups, .gar, .lmbsec {{ background: linear-gradient(180deg, #050403, #000 70%); }}

.d9 {{ overflow: hidden; isolation: isolate; border-top: 1px solid var(--line); }}
.d9::before {{ content: ""; position: absolute; inset: 0; z-index: -1; background: radial-gradient(ellipse 70% 60% at 50% 30%, rgba(250, 171, 0, .2), transparent 70%); }}

/* imagens dos produtos, bônus e cupons */
.lv {{ overflow: hidden; padding: 0 !important; }}
.lv__img {{ width: 100%; aspect-ratio: 720 / 567; object-fit: cover; }}
.lv__b {{ padding: 20px 20px 24px; }}
.bon2__ph {{ width: 46%; max-width: 190px; margin: 18px auto 0; padding: 6px; border-radius: 26px; background: linear-gradient(160deg, #2b2a2f, #0e0e10 60%); box-shadow: 0 24px 40px -18px rgba(0, 0, 0, .8), 0 0 0 1px #3a3226; }}
.bon2__c .bon2__ph img {{ max-width: none; margin: 0; filter: none; width: 100%; aspect-ratio: 716 / 1200; object-fit: cover; object-position: top; border-radius: 21px; }}
.cups {{ border-top: 1px solid var(--line); }}
.cups__l {{ margin: 16px auto 0; max-width: 560px; font-size: clamp(16px, 4.4vw, 20px); color: var(--ink2); text-wrap: balance; }}
.cupg {{ display: grid; grid-template-columns: minmax(0, 1fr); gap: 12px; max-width: 900px; margin: 36px auto 0; text-align: left; }}
@media (min-width: 760px) {{ .cupg {{ grid-template-columns: 1fr 1fr; }} }}
.cup {{ position: relative; display: grid; grid-template-columns: 112px 1fr; min-height: 118px; border-radius: 14px; background: #f7f1e3; color: #1a1a1a; box-shadow: 0 14px 30px -18px rgba(0, 0, 0, .8); }}
.cup::before, .cup::after {{ content: ""; position: absolute; left: 104px; width: 16px; height: 16px; border-radius: 50%; background: var(--bg); }}
.cup::before {{ top: -8px; }} .cup::after {{ bottom: -8px; }}
.cup__v {{ display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 12px 8px; border-right: 2px dashed #cbbf9f; border-radius: 14px 0 0 14px; background: var(--gold); text-align: center; }}
.cup__v small {{ font-size: 9px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: #3a2200; }}
.cup__v b {{ margin-top: 4px; font-size: 20px; font-weight: 800; line-height: 1.05; color: #111; }}
.cup__t {{ padding: 14px 16px; }}
.cup__t span {{ font-size: 10.5px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: #8a5a00; }}
.cup__t h3 {{ margin-top: 4px; font-size: 17px; font-weight: 800; line-height: 1.2; }}
.cup__t p {{ margin-top: 4px; font-size: 13px; line-height: 1.4; color: #5c574e; }}
.cups__fine {{ margin: 18px auto 0; max-width: 640px; font-size: 12px; line-height: 1.5; color: var(--ink3); }}

/* Método: produto principal, largura total */
.mtc {{ display: grid; grid-template-columns: minmax(0, 1fr); max-width: 980px; margin: 40px auto 0; overflow: hidden; border-radius: 22px; background: #0d0b08; box-shadow: 0 0 0 2px rgba(250, 171, 0, .7), 0 0 60px rgba(250, 171, 0, .2); text-align: left; }}
@media (min-width: 760px) {{ .mtc {{ grid-template-columns: 5fr 7fr; }} }}
.mtc__img {{ width: 100%; height: 100%; aspect-ratio: 720 / 567; object-fit: cover; }}
.mtc__b {{ padding: 26px 22px 28px; align-self: center; }}
.mtc__k {{ background: var(--gold) !important; color: #111 !important; }}
.mtc__b h3 {{ margin-top: 12px; font-size: clamp(26px, 7vw, 36px); font-weight: 800; line-height: 1.08; letter-spacing: -.02em; }}
.mtc__b p {{ margin-top: 12px; font-size: 15.5px; line-height: 1.6; color: var(--ink2); }}
.mtc__b ul {{ margin-top: 12px; list-style: none; display: grid; gap: 8px; }}
.mtc__b li {{ position: relative; padding-left: 18px; font-size: 15px; color: var(--ink2); }}
.mtc__b li::before {{ content: ""; position: absolute; left: 0; top: .55em; width: 7px; height: 7px; border-radius: 50%; background: var(--amber); }}
.lmbc {{ margin-top: 14px !important; }}

/* LOMBADA em uma história só */
.jorn {{ border-top: 1px solid var(--line); scroll-margin-top: 56px; background: radial-gradient(ellipse 70% 40% at 50% 0%, rgba(250, 171, 0, .12), transparent 70%); }}
.jn__head .h2 {{ max-width: 820px; margin-left: auto; margin-right: auto; }}
.jn__in {{ display: block; max-width: 520px; margin: 28px auto 0; text-align: left; }}
.jn__in span {{ display: block; margin-bottom: 8px; font-size: 11px; font-weight: 700; letter-spacing: .2em; text-transform: uppercase; color: var(--amber); }}
.jn__in input {{ width: 100%; height: 60px; padding: 0 18px; border: 2px solid var(--amber); border-radius: 12px; outline: none; background: #0d0b08; color: #fff; font: 600 20px/1 "Poppins", sans-serif; box-shadow: 0 0 0 6px rgba(250, 171, 0, .08); }}
.jn__in input::placeholder {{ color: #7a746a; font-weight: 500; }}
.jn__in input:focus {{ box-shadow: 0 0 0 6px rgba(250, 171, 0, .2); }}
.jn__hint {{ margin-top: 12px; font-size: 14px; color: var(--ink3); }}
.jl {{ color: var(--amber); }}
.jn {{ position: relative; max-width: 1000px; margin: 56px auto 0; list-style: none; display: grid; gap: 56px; }}
.jn::before {{ content: ""; position: absolute; left: 19px; top: 10px; bottom: 10px; width: 2px; background: linear-gradient(var(--amber), rgba(250, 171, 0, .15)); }}
.jn__s {{ position: relative; display: grid; grid-template-columns: minmax(0, 1fr); gap: 18px; padding-left: 58px; }}
@media (min-width: 900px) {{ .jn__s {{ grid-template-columns: 5fr 6fr; gap: 44px; align-items: center; }} }}
.jn__n {{ position: absolute; left: 0; top: 0; display: grid; place-items: center; width: 40px; height: 40px; border-radius: 50%; background: var(--gold); color: #111; font-size: 17px; font-weight: 800; box-shadow: 0 0 0 6px #000; }}
.jn__t h3 {{ font-size: clamp(24px, 6.4vw, 36px); font-weight: 800; line-height: 1.1; letter-spacing: -.025em; text-wrap: balance; }}
.jn__t p {{ margin-top: 10px; font-size: clamp(15px, 4.2vw, 18px); line-height: 1.55; color: var(--ink2); }}
.jn__app {{ padding: 16px; border-radius: 20px; background: var(--paper); color: var(--paper-ink); box-shadow: 0 30px 60px -30px rgba(0, 0, 0, .9), 0 0 0 1px #2e2a24; }}
.ap__top {{ display: flex; align-items: center; justify-content: space-between; gap: 10px; }}
.ap__lmb {{ font-size: 14px; }} .ap__lmb .lmb {{ color: var(--paper-ink); }}
.ap__tg {{ font-size: 10px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: var(--paper-soft); }}
.ap__ti {{ margin-top: 10px; font-size: 22px; font-weight: 800; line-height: 1.15; color: #8a5a00; }}
.ap__pr {{ display: flex; align-items: center; gap: 10px; margin-top: 8px; font-size: 12px; font-weight: 600; color: var(--paper-soft); }}
.ap__pr i {{ flex: 1; height: 6px; border-radius: 6px; background: #e3ded2; overflow: hidden; }}
.ap__pr b {{ display: block; height: 100%; width: 0; background: var(--green); transition: width .5s var(--ease); }}
.ap__acts {{ display: grid; gap: 8px; margin-top: 12px; }}
.ap__act {{ display: flex; gap: 12px; align-items: flex-start; width: 100%; padding: 12px; border: 0; border-radius: 12px; background: #fff; box-shadow: 0 0 0 1px #e3ded2; text-align: left; cursor: pointer; font: inherit; color: inherit; transition: background .2s; }}
.ap__act i {{ flex: none; display: grid; place-items: center; width: 24px; height: 24px; margin-top: 1px; border-radius: 50%; box-shadow: inset 0 0 0 2px #c9c1b0; color: transparent; font-style: normal; font-size: 14px; font-weight: 800; transition: background .2s, color .2s; }}
.ap__act b {{ display: block; font-size: 14.5px; line-height: 1.35; }}
.ap__act small {{ display: block; margin-top: 3px; font-size: 12px; color: var(--paper-soft); }}
.ap__act.ok {{ background: #eef8ea; }}
.ap__act.ok i {{ background: var(--green); box-shadow: none; color: #fff; }}
.ap__act.ok b {{ text-decoration: line-through; text-decoration-color: rgba(0, 0, 0, .35); }}
.ap__txt {{ margin-top: 12px; padding: 14px; border-radius: 12px; background: #fff; box-shadow: 0 0 0 1px #e3ded2; font-size: 14.5px; line-height: 1.6; white-space: pre-line; }}
.ap__txt .vr {{ padding: 0 4px; border-radius: 4px; background: #efe9dc; color: var(--paper-soft); }}
.ap__txt .jl, .ap__ideas .jl {{ color: #8a5a00; font-weight: 700; }}
.ap__copy {{ display: block; width: 100%; margin-top: 10px; padding: 13px; border: 0; border-radius: 12px; background: var(--paper-ink); color: var(--amber); font: 700 14px/1 "Poppins", sans-serif; letter-spacing: .04em; text-transform: uppercase; cursor: pointer; }}
.ap__pills {{ display: flex; gap: 6px; margin-top: 12px; overflow-x: auto; scrollbar-width: none; }}
.ap__pills button {{ flex: none; padding: 8px 12px; border: 1px solid #d3ccbd; border-radius: 99px; background: #fff; color: #3a3833; font: 600 12px/1 "Poppins", sans-serif; cursor: pointer; }}
.ap__pills button[aria-pressed="true"] {{ background: var(--paper-ink); border-color: var(--paper-ink); color: #fff; }}
.ap__ops {{ display: grid; gap: 8px; margin-top: 12px; }}
.ap__op {{ display: flex; gap: 12px; align-items: center; padding: 10px 12px; border-radius: 12px; background: #fff; box-shadow: 0 0 0 1px #e3ded2; }}
.ap__op .d {{ flex: none; width: 46px; padding: 6px 0; border-radius: 10px; background: var(--paper-ink); color: #fff; text-align: center; line-height: 1; }}
.ap__op .d b {{ display: block; font-size: 18px; }} .ap__op .d small {{ display: block; margin-top: 2px; font-size: 10px; text-transform: uppercase; color: var(--amber); }}
.ap__op p {{ font-size: 14px; font-weight: 700; line-height: 1.3; }}
.ap__op span {{ display: inline-block; margin-top: 3px; margin-right: 6px; font-size: 11px; font-weight: 600; color: var(--paper-soft); }}
.ap__op span.cd {{ color: #b5402e; }}
.ap__ideas {{ display: grid; gap: 8px; margin-top: 12px; max-height: 330px; overflow-y: auto; }}
.ap__idea {{ padding: 12px; border-radius: 12px; background: #fff; box-shadow: 0 0 0 1px #e3ded2; animation: rise .5s var(--ease) both; }}
.ap__idea small {{ font-size: 10.5px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: #8a5a00; }}
.ap__idea p {{ margin-top: 4px; font-size: 15px; font-weight: 700; line-height: 1.35; }}
.ap__idea span {{ display: block; margin-top: 3px; font-size: 12.5px; color: var(--paper-soft); }}
.jn__end {{ margin-top: 72px; text-align: center; }}
.jn__e1 {{ font-size: clamp(20px, 5.6vw, 30px); font-weight: 600; color: var(--ink2); }}
.jn__e2 {{ margin: 6px auto 0; max-width: 900px; font-size: clamp(34px, 9.6vw, 72px); font-weight: 800; line-height: 1.02; letter-spacing: -.035em; text-wrap: balance; }}
.jn__dep {{ max-width: 680px; margin: 34px auto 0; padding: 24px 26px; border-radius: 18px; background: rgba(255, 255, 255, .04); box-shadow: inset 0 0 0 1.5px rgba(250, 171, 0, .45); text-align: left; }}
.jn__dep blockquote {{ position: relative; padding-left: 34px; font-size: clamp(17px, 4.6vw, 21px); font-weight: 600; line-height: 1.45; color: #fff; }}
.jn__dep blockquote::before {{ content: "“"; position: absolute; left: 0; top: -14px; font-size: 56px; font-weight: 800; line-height: 1; color: var(--amber); }}
.jn__dep figcaption {{ margin-top: 12px; padding-left: 34px; font-size: 14px; color: var(--ink2); }}
.jn__dep figcaption b {{ color: var(--amber); }}
.jn__end .cta {{ max-width: 480px; margin: 32px auto 0; }}

/* mais ar entre os cartões do "vai levar" e dos bônus */
.leva__g {{ gap: 28px !important; margin-top: 28px !important; }}
@media (min-width: 760px) {{ .leva__g {{ gap: 32px !important; }} }}
.lv__b {{ padding: 24px 22px 28px !important; }}
.lv__b h3 {{ margin-top: 14px !important; }}
.lv__b p, .lv__b ul {{ margin-top: 12px !important; }}
.lmbc {{ margin-top: 28px !important; }}
.bon2 {{ gap: 28px !important; }}
.cupg {{ gap: 18px !important; }}

.jn__vid {{ max-width: 860px; margin: 26px auto 48px; overflow: hidden; border-radius: 18px; background: #000; box-shadow: 0 0 0 2px rgba(250, 171, 0, .6), 0 30px 70px -30px rgba(250, 171, 0, .45); }}
.jn__vid vturb-smartplayer {{ display: block; width: 100%; min-height: 200px; }}

/* passo 6: a vitrine como ela é (estante de capas, filtros de gênero) */
.vt2 {{ background: #16110c !important; color: #fff !important; box-shadow: 0 30px 60px -30px rgba(0, 0, 0, .9), 0 0 0 1px #3a3226 !important; }}
.vt2__top {{ display: flex; align-items: center; gap: 10px; padding-bottom: 12px; border-bottom: 1px solid #2c241b; }}
.vt2__top .lmb {{ color: #f3f0e8 !important; }}
.vt2__top span:last-child {{ font-size: 10px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: var(--amber); }}
.vt2__chips {{ display: flex; gap: 6px; margin-top: 12px; overflow: hidden; }}
.vt2__chips i {{ flex: none; padding: 6px 11px; border-radius: 99px; box-shadow: inset 0 0 0 1px #3a3226; font-style: normal; font-size: 11px; font-weight: 600; color: #e9e2d4; }}
.vt2__chips i.on {{ background: var(--amber); color: #111; box-shadow: none; }}
.vt2__grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px 10px; margin-top: 16px; }}
.vb {{ position: relative; min-width: 0; }}
.vb__c {{ position: relative; padding: 0 6% 6px; border-bottom: 5px solid #4a3a2a; }}
.vb__c img, .vb__capa {{ display: block; width: 100%; aspect-ratio: 164 / 240; border-radius: 2px 5px 5px 2px; box-shadow: 0 8px 16px -8px rgba(0, 0, 0, .8); }}
.vb__capa {{ display: flex; flex-direction: column; justify-content: space-between; padding: 12% 10% 8%; background: linear-gradient(160deg, #fe7743, #b5402e); box-shadow: inset 5px 0 0 rgba(0, 0, 0, .18), 0 0 0 2px #faab00, 0 0 24px rgba(250, 171, 0, .6); overflow: hidden; }}
.vb__capa b {{ font-size: 12px; font-weight: 800; line-height: 1.1; color: #fff; text-align: center; overflow-wrap: anywhere; }}
.vb__capa small {{ font-size: 7px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: rgba(255, 255, 255, .8); text-align: center; }}
.vb__t {{ margin-top: 8px; overflow: hidden; font-size: 11.5px; font-weight: 700; line-height: 1.2; white-space: nowrap; text-overflow: ellipsis; }}
.vb__a {{ margin-top: 2px; font-size: 10.5px; color: #a8a090; }}
.vb--me .vb__t {{ color: var(--amber); }}
.vb__tag {{ position: absolute; left: 50%; top: -9px; z-index: 2; padding: 3px 8px; border-radius: 99px; background: var(--amber); color: #111; font-size: 9px; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; white-space: nowrap; transform: translateX(-50%); }}

/* passo 5: página do livro · passo 6: vitrine */
.pg {{ margin-top: 12px; overflow: hidden; border-radius: 12px; background: #fff; box-shadow: 0 0 0 1px #e3ded2; }}
.pg__bar {{ display: flex; align-items: center; gap: 5px; padding: 8px 10px; background: #efe9dc; }}
.pg__bar i {{ width: 8px; height: 8px; border-radius: 50%; background: #d3ccbd; }}
.pg__bar span {{ flex: 1; min-width: 0; margin-left: 6px; padding: 4px 10px; overflow: hidden; border-radius: 99px; background: #fff; font-size: 11px; color: var(--paper-soft); white-space: nowrap; text-overflow: ellipsis; }}
.pg__bar span b {{ color: #8a5a00; }}
.pg__b {{ display: grid; grid-template-columns: 96px 1fr; gap: 14px; padding: 16px; }}
.pg__capa {{ display: flex; align-items: flex-end; aspect-ratio: 2 / 3; padding: 8px; border-radius: 4px 8px 8px 4px; background: linear-gradient(160deg, #b5402e, #6e2418); box-shadow: inset 6px 0 0 rgba(0, 0, 0, .18), 0 10px 20px -10px rgba(0, 0, 0, .5); color: #fff; font-size: 11px; font-weight: 800; line-height: 1.15; overflow: hidden; }}
.pg__ti {{ font-size: 18px; font-weight: 800; line-height: 1.15; }}
.pg__au {{ margin-top: 2px; font-size: 12px; color: var(--paper-soft); }}
.pg__si {{ margin-top: 8px; font-size: 12.5px; line-height: 1.45; color: var(--paper-soft); }}
.pg__btn {{ display: inline-block; margin-top: 10px; padding: 8px 14px; border-radius: 8px; background: var(--paper-ink); color: var(--amber); font-size: 12px; font-weight: 700; }}
.vt {{ background: #fe7743 !important; }}
.vt .ap__tg {{ color: #3a1a08; }}
.vt__stage {{ position: relative; margin-top: 14px; padding-top: 70px; }}
.vt__shelf {{ display: flex; align-items: flex-end; justify-content: center; gap: 4px; height: 200px; padding: 0 6px; }}
.vt__shelf i {{ position: relative; flex: none; width: var(--w); height: var(--h); border-radius: 3px 3px 0 0; background: var(--c); box-shadow: inset -4px 0 0 rgba(0, 0, 0, .12), inset 0 -14px 0 rgba(0, 0, 0, .1); }}
.vt__shelf i::before, .vt__shelf i::after {{ content: ""; position: absolute; left: 22%; right: 22%; height: 3px; border-radius: 2px; background: rgba(255, 255, 255, .55); }}
.vt__shelf i::before {{ bottom: 22px; }} .vt__shelf i::after {{ bottom: 30px; }}
.vt__me {{ position: relative; flex: none; display: flex; align-items: center; justify-content: center; width: 50px; height: 100%; border-radius: 4px 4px 0 0; background: #1a1a1a; transform: translateY(-14px); box-shadow: 0 0 0 3px #faab00, 0 14px 30px rgba(0, 0, 0, .35), 0 0 30px rgba(250, 171, 0, .7); animation: vtsobe 3.6s var(--ease) infinite; }}
.vt__me span {{ writing-mode: vertical-rl; transform: rotate(180deg); max-height: 90%; overflow: hidden; color: #faab00; font-size: 13px; font-weight: 800; white-space: nowrap; text-overflow: ellipsis; }}
.vt__wood {{ height: 12px; border-radius: 0 0 6px 6px; background: linear-gradient(#5a2a0e, #3a1a08); box-shadow: 0 10px 18px -8px rgba(0, 0, 0, .5); }}
.vt__pop {{ position: absolute; left: 50%; top: 0; display: flex; align-items: center; gap: 10px; max-width: 92%; padding: 8px 14px 8px 8px; border-radius: 12px; background: #fff; box-shadow: 0 14px 28px -12px rgba(0, 0, 0, .5); transform: translateX(-50%); animation: vtpop 3.6s var(--ease) infinite; }}
.vt__pop::after {{ content: ""; position: absolute; left: 50%; bottom: -6px; width: 12px; height: 12px; background: #fff; transform: translateX(-50%) rotate(45deg); }}
.vt__pc {{ flex: none; width: 30px; height: 42px; border-radius: 2px 5px 5px 2px; background: linear-gradient(160deg, #b5402e, #6e2418); box-shadow: inset 4px 0 0 rgba(0, 0, 0, .2); }}
.vt__pop small {{ display: block; font-size: 10px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: #8a5a00; }}
.vt__pop b {{ display: block; max-width: 190px; overflow: hidden; font-size: 14px; font-weight: 800; white-space: nowrap; text-overflow: ellipsis; color: #1a1a1a; }}
@media (max-width: 520px) {{ .vt__shelf {{ gap: 3px; padding: 0; }} .vt__shelf i {{ width: calc(var(--w) * .7); }} .vt__me {{ width: 40px; }} .vt__me span {{ font-size: 11.5px; }} }}
@keyframes vtsobe {{ 0%, 15% {{ transform: translateY(0); }} 35%, 85% {{ transform: translateY(-14px); }} 100% {{ transform: translateY(0); }} }}
@keyframes vtpop {{ 0%, 100% {{ transform: translate(-50%, 0); }} 50% {{ transform: translate(-50%, -6px); }} }}
/* garantia: sem as linhas de separação, com mais presença */
.gar {{ border-top: 0 !important; background: none !important; padding-top: 24px; }}
.gar + .dany {{ border-top: 0; padding-top: 24px; }}
.gar__c {{ max-width: 900px; padding: 34px 24px; background: radial-gradient(ellipse 70% 120% at 0% 50%, rgba(250, 171, 0, .24), transparent 70%), linear-gradient(135deg, #17120a, #0a0806) !important; box-shadow: 0 0 0 2px rgba(250, 171, 0, .75), 0 0 80px rgba(250, 171, 0, .25) !important; }}
@media (min-width: 760px) {{ .gar__c {{ grid-template-columns: 230px 1fr !important; padding: 44px 48px; }} }}
.gar__seal {{ width: 190px !important; height: 190px !important; }}
.gar__seal b {{ font-size: 84px !important; }}
.gar__k {{ font-size: 12px; font-weight: 700; letter-spacing: .24em; text-transform: uppercase; color: var(--amber); }}
.gar__t h2 {{ margin-top: 8px; }}

/* LOMBADA: os 3 benefícios */
.tri {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 22px; list-style: none; }}
.tri li {{ display: inline-flex; align-items: center; gap: 10px; padding: 10px 18px 10px 10px; border-radius: 99px; background: #15120c; box-shadow: inset 0 0 0 1.5px rgba(250, 171, 0, .5); font-size: clamp(17px, 4.6vw, 22px); font-weight: 800; }}
.tri b {{ display: grid; place-items: center; width: 32px; height: 32px; border-radius: 50%; background: var(--gold); color: #111; font-size: 15px; }}
.lmbc__b li b {{ color: var(--paper-ink); }}
.lmbx .feat__k {{ color: var(--amber); }}

/* LOMBADA: título antes do test drive */
.lmbh {{ max-width: 860px; margin: 40px auto 0; text-align: center; }}
.lmbh__mark {{ margin-top: 16px; font-size: clamp(46px, 13vw, 110px); line-height: 1; }}
.lmbh__mark .lmb {{ color: var(--ink); }}
.lmbh__t {{ margin-top: 14px; font-size: clamp(26px, 7.4vw, 50px); font-weight: 800; line-height: 1.06; letter-spacing: -.03em; text-wrap: balance; }}
.leva--resto {{ border-top: 0; padding-top: 40px; }}
.lmbx .h2 {{ font-size: clamp(30px, 8vw, 48px); }}
/* abertura emendada na oferta (ordem do Aniversário) */
/* 08/11 (cliente): a frase alinhada certinho embaixo do logo do LOMBADA */
.h .h__sub {{ align-items: flex-start; }}
.h__col {{ display: inline-flex; flex-direction: column; align-items: flex-start; }}
.h__col .h__tag {{ display: block; text-align: left; white-space: nowrap; letter-spacing: 0; text-transform: none; }}
.h .h__sub > b {{ align-self: flex-start; line-height: 1; margin-top: .2em; }}
.h .h__col .h__tag {{ margin-top: 8px; }}
@media (max-width: 719px) {{ .h h1.h__t .h__sub {{ font-size: clamp(32px, 9.4vw, 40px); }} }}
/* 08/11 (cliente): bandeirinha diagonal "Novo" no LOMBADA do topo */
.h__col {{ position: relative; }}
.novo-h {{ position: absolute; top: -.78em; right: -.7em; transform: rotate(12deg); font-style: normal; font-size: clamp(10px, 2.6vw, 14px); font-weight: 800; letter-spacing: .16em; text-transform: uppercase; line-height: 1; padding: .45em .8em .38em; background: #d62f24; color: #fff; border-radius: 3px; box-shadow: 0 3px 10px rgba(0,0,0,.45); z-index: 2; }}
/* 08/11 (cliente): a trilha do Aniversário abaixo do LOMBADA */
.trilha {{ margin: 34px auto 0; font-size: clamp(9.5px, 2.7vw, 15px); font-weight: 700; letter-spacing: .1em; line-height: 2; text-transform: uppercase; color: #f4efe4; }}
.trilha span {{ white-space: nowrap; }} .trilha .l1, .trilha .l2 {{ display: block; }}
.trilha i {{ font-style: normal; color: var(--amber); margin: 0 .35em; }}
@media (min-width: 720px) {{ .trilha {{ letter-spacing: .18em; }} .trilha .l1, .trilha .l2 {{ display: inline; }} }}
.trilha + .hk2 {{ margin-top: 26px; }}
/* 08/11 (cliente): os 2 destaques em colunas com divisória, como no Aniversário */
.hk2 {{ display: grid; grid-template-columns: 1fr; gap: 12px; max-width: 820px; margin: 40px auto 0; text-align: left; }}
.hk2 p {{ display: flex; gap: 12px; align-items: flex-start; font-size: clamp(15px, 3.9vw, 17px); line-height: 1.5; color: #e9e3d6; }}
.hk2 .ck {{ flex: 0 0 22px; width: 22px; height: 22px; margin-top: 3px; }}
.hk2 b {{ color: var(--ink); }} .hk2 b.amber {{ color: var(--amber); }}
@media (min-width: 720px) {{ .hk2 {{ grid-template-columns: 1fr 1fr; gap: 0; }} .hk2 p {{ padding: 2px 30px; }} .hk2 p + p {{ border-left: 1px solid rgba(255,255,255,.18); }} }}
.hk {{ max-width: 560px; margin: 48px auto 0; list-style: none; display: grid; gap: 12px; text-align: left; }}
.hk li {{ display: flex; gap: 12px; align-items: flex-start; font-size: clamp(15px, 4.2vw, 18px); line-height: 1.45; color: var(--ink2); }}
.hk b {{ color: var(--ink); }} .hk b.amber {{ color: var(--amber); }}
.amber {{ color: var(--amber); }}
.blk {{ max-width: 640px; margin: 56px auto 0; }}
.q1 {{ font-size: clamp(18px, 5vw, 24px); font-weight: 500; line-height: 1.4; color: var(--ink2); text-wrap: balance; }}
.q1 u {{ color: var(--ink); font-weight: 700; text-decoration-color: var(--amber); text-underline-offset: 4px; }}
.q2 {{ font-size: clamp(20px, 5.6vw, 28px); font-weight: 700; line-height: 1.3; text-wrap: balance; }}
.blk .bill {{ margin-top: 22px; text-align: left; }}
.bill__row--lmb span .lmb {{ color: var(--ink); font-size: 1.05em; }}
.bill__row--lmb b {{ color: var(--amber) !important; font-weight: 700; }}
.bill__row--lmb > span {{ display: inline-flex; align-items: center; gap: 10px; }}
.bill__row--lmb {{ position: relative; overflow: hidden; margin: 0 -20px; padding-left: 20px !important; padding-right: 20px !important; background: linear-gradient(90deg, rgba(250,171,0,.07), rgba(250,171,0,0) 70%); }}
.novo {{ position: absolute; top: 9px; left: -30px; width: 104px; transform: rotate(-45deg); font-style: normal; font-size: 9px; font-weight: 800; letter-spacing: .16em; text-transform: uppercase; line-height: 1; padding: 4px 0 3px; text-align: center; background: #d62f24; color: #fff; box-shadow: 0 2px 6px rgba(0,0,0,.4); }}
.bill__row--lmb > span {{ padding-left: 26px; }}
.price {{ margin-top: 64px; }}
.price__big {{ margin-top: 14px; line-height: 1; }}
.price__big small {{ display: block; font-size: 18px; font-weight: 500; color: var(--ink2); }}
.price__big span {{ display: block; white-space: nowrap; margin-top: 6px; font-size: clamp(52px, 15.5vw, 104px); font-weight: 800; letter-spacing: -.04em; background: var(--gold); background-size: 220% 100%; -webkit-background-clip: text; background-clip: text; color: transparent; animation: gold 6s linear infinite; }}
.price__cash {{ margin-top: 8px; font-size: 16px; color: var(--ink2); }}
.price__cta {{ max-width: 480px; margin: 26px auto 0; }}
.resumo .card__list {{ margin-top: 22px; }}
.bon2 {{ display: grid; grid-template-columns: minmax(0, 1fr); gap: 16px; max-width: 900px; margin: 34px auto 0; }}

.bon2__c {{ padding: 26px 22px; border-radius: 18px; background: #0d0b08; box-shadow: inset 0 0 0 1.5px rgba(250, 171, 0, .5); text-align: center; }}
.bon2__c img {{ width: 70%; max-width: 260px; margin: 16px auto 0; filter: drop-shadow(0 24px 30px rgba(0, 0, 0, .7)); }}
.bon2__c .bon2__big {{ margin-top: 14px; font-size: clamp(84px, 26vw, 140px); font-weight: 800; line-height: .9; letter-spacing: -.05em; }}
.bon2__c h3 {{ margin-top: 12px; font-size: clamp(20px, 5.4vw, 26px); font-weight: 800; line-height: 1.2; }}
.bon2__c h3 .lmb {{ color: var(--ink); }}
.bon2__c > p:not(.bon2__big) {{ margin-top: 10px; font-size: 15px; line-height: 1.55; color: var(--ink2); }}
.resumo {{ border-top: 1px solid var(--line); }}
.resumo .card {{ padding-top: 34px; }}
.resumo__de {{ margin-top: 22px; font-size: 18px; color: var(--ink2); }}
.resumo__de s {{ color: var(--ink3); }}
.resumo__por {{ margin-top: 4px; font-size: 16px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--amber); }}
.warn {{ max-width: 600px; margin: 22px auto 0; padding: 16px 18px; border-radius: 14px; background: #1a0f05; box-shadow: inset 0 0 0 1px rgba(250, 171, 0, .4); font-size: 15px; line-height: 1.5; color: var(--ink2); text-align: left; }}
.warn b {{ color: var(--amber); }}
.leva {{ border-top: 1px solid var(--line); }}
.lv__k {{ display: inline-block; padding: 5px 11px; border-radius: 99px; background: rgba(250, 171, 0, .14); color: var(--amber); font-size: 10.5px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }}
.lv.lv--lmb {{ max-width: 980px; margin: 40px auto 0; padding: 30px 20px 34px; border-radius: 24px; background: var(--paper); color: var(--paper-ink); text-align: center; }}
.lv.lv--lmb .lv__k {{ background: var(--paper-ink); color: var(--amber); }}
.lv.lv--lmb .lv__lmb {{ margin-top: 14px; font-size: clamp(38px, 11vw, 110px); line-height: 1; }}
.lv.lv--lmb .lv__lmb .lmb {{ color: var(--paper-ink); }}
.lv.lv--lmb .lv__lead {{ margin: 14px auto 0; max-width: 560px; font-size: clamp(16px, 4.4vw, 20px); font-weight: 500; line-height: 1.45; color: var(--paper-soft); text-wrap: balance; }}
.lv.lv--lmb .story {{ margin-top: 30px; }}
.lv.lv--lmb .days {{ margin-top: 30px; padding: 26px 10px 6px; border-top: 1px solid #e3ded2; }}
.lv.lv--lmb .days::before {{ display: none; }}
.lv.lv--lmb p.days__n {{ font-size: clamp(84px, 26vw, 200px); }}
.lv.lv--lmb p.days__a {{ margin-top: 10px; font-size: clamp(22px, 6vw, 38px); color: var(--paper-ink); }}
.leva__g {{ display: grid; grid-template-columns: minmax(0, 1fr); gap: 12px; max-width: 980px; margin: 14px auto 0; }}
@media (min-width: 760px) {{ .leva__g {{ grid-template-columns: 1fr 1fr; }} }}
.lv {{ padding: 24px 20px; border-radius: 18px; background: var(--bg2); box-shadow: inset 0 0 0 1px var(--line); }}
.lv h3 {{ margin-top: 12px; font-size: clamp(21px, 5.6vw, 26px); font-weight: 800; line-height: 1.15; letter-spacing: -.015em; }}
.lv > p {{ margin-top: 10px; font-size: 15px; line-height: 1.6; color: var(--ink2); }}
.lv ul {{ margin-top: 12px; list-style: none; display: grid; gap: 8px; }}
.lv ul li {{ position: relative; padding-left: 18px; font-size: 15px; color: var(--ink2); }}
.lv ul li::before {{ content: ""; position: absolute; left: 0; top: .55em; width: 7px; height: 7px; border-radius: 50%; background: var(--amber); }}
.leva__cta {{ max-width: 480px; margin: 40px auto 0; }}
.casos-sec {{ border-top: 1px solid var(--line); }}
{CASOS_CSS}
.casos__more {{ margin-top: 18px; text-align: center; font-size: 15px; color: var(--ink2); }}

/* abertura: a maior oferta */
.h__big {{ display: block; font-size: clamp(46px, 13.6vw, 100px); font-weight: 800; line-height: .94; letter-spacing: -.035em; text-transform: uppercase; text-wrap: balance; padding-bottom: .04em; }}
.h__sub {{ display: block; margin-top: 18px; font-size: clamp(24px, 7vw, 52px); font-weight: 700; line-height: 1.1; letter-spacing: -.02em; color: var(--ink); text-wrap: balance; }}
.h__sub b {{ color: var(--amber); font-weight: 800; margin-right: .2em; }}
.h .h__sub {{ display: flex; justify-content: center; align-items: center; gap: .1em; margin-top: 22px; font-size: clamp(26px, 7.4vw, 46px); font-weight: 800; letter-spacing: .01em; }}
.h .h__sub b {{ font-size: .8em; }}
@media (min-width: 1000px) {{ .h .h__sub {{ font-size: 64px; margin-top: 26px; }} .h__tag {{ font-size: 28.4px; margin-top: 10px; }} }}
.h__sub .lmb {{ color: var(--ink); }}
.h__tag {{ display: block; margin-top: 10px; font-size: clamp(16px, 4.4vw, 22px); font-weight: 600; line-height: 1.2; letter-spacing: -.01em; color: var(--ink2); text-wrap: balance; }}

/* a conta */
.conta {{ border-top: 1px solid var(--line); }}
.bill {{ max-width: 640px; margin: 40px auto 0; padding: 8px 20px; border-radius: 18px; background: #0d0c0a; box-shadow: inset 0 0 0 1px var(--line); }}
.bill__row {{ display: flex; justify-content: space-between; gap: 14px; padding: 14px 0; border-bottom: 1px dashed #2c2822; font-size: clamp(14px, 4vw, 17px); color: var(--ink2); }}
.bill__row b {{ flex: none; color: var(--ink); font-weight: 600; font-variant-numeric: tabular-nums; }}
.bill__tot {{ display: flex; justify-content: space-between; align-items: baseline; gap: 14px; padding: 18px 0 14px; font-size: clamp(15px, 4.2vw, 18px); font-weight: 700; }}
.bill__tot b {{ white-space: nowrap; font-size: clamp(22px, 6.2vw, 32px); font-weight: 800; color: var(--amber); font-variant-numeric: tabular-nums; }}
.bill--anos {{ margin-top: 18px; }}
.strike {{ position: relative; }}
.conta__q {{ margin-top: 48px; font-size: clamp(20px, 5.6vw, 30px); font-weight: 700; line-height: 1.2; text-wrap: balance; }}
.conta__lmb {{ max-width: 640px; margin: 28px auto 0; padding: 20px; border-radius: 16px; text-align: center; font-size: clamp(22px, 6vw, 30px); font-weight: 800; background: radial-gradient(ellipse 80% 120% at 50% 0%, rgba(250, 171, 0, .18), transparent 70%), #100d07; box-shadow: inset 0 0 0 1.5px rgba(250, 171, 0, .55); }}
.conta__lmb .lmb {{ color: var(--ink); }}
.conta__lmb .q {{ display: inline-flex; align-items: center; gap: .3em; white-space: nowrap; }}
.conta__lmb .d {{ display: block; margin-top: 8px; font-size: clamp(15px, 4.2vw, 18px); font-weight: 500; color: var(--ink2); }}
.card__price .pre s {{ color: var(--ink3); }}

/* 5. Dany */
.dany {{ border-top: 1px solid var(--line); }}
.dany__g {{ display: grid; grid-template-columns: minmax(0, 1fr); gap: 36px; align-items: center; max-width: 1000px; margin: 0 auto; }}
@media (min-width: 860px) {{ .dany__g {{ grid-template-columns: 5fr 7fr; gap: 64px; }} }}
.dany__pic {{ position: relative; isolation: isolate; max-width: 250px; margin: 0 auto; }}
@media (min-width: 860px) {{ .dany__pic {{ max-width: 360px; }} }}
.dany__pic::before {{ content: ""; position: absolute; inset: 12% -10% 0; z-index: -1; border-radius: 50%; background: radial-gradient(closest-side, rgba(250, 171, 0, .28), transparent); }}
.dany__pic img {{ -webkit-mask-image: linear-gradient(#000 78%, transparent); mask-image: linear-gradient(#000 78%, transparent); }}
.dany__h {{ margin-top: 16px; font-size: clamp(38px, 10.4vw, 64px); font-weight: 800; line-height: 1; letter-spacing: -.03em; }}
.dany__l {{ margin-top: 22px; display: grid; gap: 14px; font-size: clamp(16px, 4.3vw, 19px); line-height: 1.6; color: var(--ink2); }}
.dany__l b {{ color: var(--ink); font-weight: 600; }}
.dany__sig {{ margin-top: 18px; font-size: 28px; color: var(--amber); }}
.stats {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 30px; }}
.stat {{ padding: 16px; border-radius: 14px; background: var(--bg2); box-shadow: inset 0 0 0 1px var(--line); }}
.stat b {{ display: block; font-size: clamp(28px, 7.6vw, 38px); font-weight: 800; line-height: 1; color: var(--amber); }}
.stat span {{ display: block; margin-top: 6px; font-size: 13px; line-height: 1.35; color: var(--ink2); }}

/* 6. oferta */
.offer {{ border-top: 1px solid var(--line); background: radial-gradient(ellipse 60% 50% at 50% 40%, rgba(250, 171, 0, .14), transparent 70%); }}
.card {{ position: relative; max-width: 600px; margin: 0 auto; padding: 40px 22px 28px; border-radius: 24px; background: #050403; text-align: center;
  box-shadow: 0 0 0 1.5px rgba(250, 171, 0, .6), 0 0 80px rgba(250, 171, 0, .28); }}
.card .bwlogo {{ font-size: 26px; }}
.card__t {{ margin-top: 22px; font-size: clamp(28px, 8vw, 44px); font-weight: 800; line-height: 1.05; letter-spacing: -.03em; text-wrap: balance; }}
.card__t .serif {{ display: block; font-size: 1.4em; line-height: 1.05; }}
.card__t .lmb-row {{ display: block; margin-top: 12px; font-size: .9em; }}
.card__t .lmb {{ color: var(--ink); }}
.card__list {{ margin: 28px 0 0; list-style: none; display: grid; gap: 12px; text-align: left; }}
.card__list li {{ display: flex; gap: 12px; align-items: flex-start; font-size: clamp(15px, 4.1vw, 17px); line-height: 1.4; color: var(--ink2); }}
.card__list b {{ color: var(--ink); }}
.ck {{ flex: none; width: 22px; height: 22px; padding: 4px; margin-top: 1px; border-radius: 50%; background: var(--green); color: #fff; }}
.card__price {{ margin-top: 30px; padding-top: 26px; border-top: 1px solid var(--line); }}
.card__price .pre {{ font-size: 16px; color: var(--ink2); }}
.card__price .big {{ font-size: clamp(64px, 19vw, 104px); font-weight: 800; line-height: .95; letter-spacing: -.04em; }}
.card__price .big small {{ font-size: .36em; letter-spacing: 0; vertical-align: .9em; margin-right: 4px; }}
.card__price .cash {{ margin-top: 8px; font-size: 16px; color: var(--ink2); }}
.card__clock {{ margin-top: 24px; padding: 16px 12px; border-radius: 14px; background: rgba(250, 171, 0, .08); box-shadow: inset 0 0 0 1px rgba(250, 171, 0, .45); }}
.card__clock p {{ margin-bottom: 10px; font-size: 14px; color: var(--ink); }}
.card__clock p b {{ color: var(--amber); }}
.card .btn {{ margin-top: 22px; gap: 8px; padding: 0 12px; font-size: clamp(15px, 4.4vw, 20px); }}
.seal {{ display: flex; gap: 14px; align-items: center; margin-top: 22px; padding: 14px; border-radius: 14px; background: var(--bg2); text-align: left; }}
.seal i {{ flex: none; display: flex; flex-direction: column; align-items: center; justify-content: center; width: 58px; height: 58px; border-radius: 50%; font-style: normal; font-size: 22px; font-weight: 800; line-height: .9; color: #111; background: var(--gold); }}
.seal i small {{ display: block; margin-top: 2px; font-size: 8px; letter-spacing: .1em; text-transform: uppercase; }}
.seal p {{ font-size: 14px; line-height: 1.45; color: var(--ink2); }}
.seal b {{ color: var(--ink); }}

/* 8. fecho */
.end {{ overflow: hidden; isolation: isolate; border-top: 1px solid var(--line); text-align: center; }}
.end::before {{ content: ""; position: absolute; left: 50%; top: 40%; width: 900px; height: 900px; z-index: -1; transform: translate(-50%, -50%); border-radius: 50%; background: radial-gradient(closest-side, rgba(250, 171, 0, .2), transparent); }}
.end__a {{ margin-top: 18px; font-size: clamp(44px, 13vw, 110px); font-weight: 800; line-height: .95; letter-spacing: -.04em; text-wrap: balance; }}
.end__b {{ margin: 22px auto 0; max-width: 560px; font-size: clamp(17px, 4.6vw, 22px); color: var(--ink2); text-wrap: balance; }}
.end .cta {{ max-width: 480px; margin: 34px auto 0; }}

footer {{ padding: 40px 20px 110px; border-top: 1px solid var(--line); text-align: center; font-size: 12px; line-height: 1.6; color: var(--ink3); }}
footer p + p {{ margin-top: 8px; }}
footer .legal {{ max-width: 720px; margin: 14px auto 0; }}
.dock {{ position: fixed; left: 0; right: 0; bottom: 0; z-index: 40; padding: 10px 16px calc(10px + env(safe-area-inset-bottom)); background: linear-gradient(transparent, rgba(0, 0, 0, .9) 30%);
  transform: translateY(110%); transition: transform .35s var(--ease); }}
.dock.on {{ transform: none; }}
.dock .btn {{ min-height: 56px; }}
@media (min-width: 900px) {{ .dock {{ display: none; }} footer {{ padding-bottom: 40px; }} }}
/* 02/11 (cliente): botão flutuante para falar com a Dezza no WhatsApp; sobe quando a barra de compra aparece */
.zap {{ position: fixed; right: 16px; bottom: calc(16px + env(safe-area-inset-bottom)); z-index: 45; display: flex; align-items: center; justify-content: center; width: 58px; height: 58px; border-radius: 50%; background: #25d366; color: #fff; box-shadow: 0 6px 20px rgba(0, 0, 0, .35); transition: bottom .35s var(--ease); }}
.zap svg {{ width: 32px; height: 32px; }}
.dock.on ~ .zap {{ bottom: calc(92px + env(safe-area-inset-bottom)); }}
@media (min-width: 900px) {{ .zap, .dock.on ~ .zap {{ right: 28px; bottom: 28px; }} }}

@keyframes bar {{ to {{ width: 100%; }} }}
@keyframes pan {{ 0%, 12% {{ transform: translateY(0); }} 100% {{ transform: translateY(var(--pan, 0px)); }} }}
@keyframes gold {{ from {{ background-position: 120% 0; }} to {{ background-position: -100% 0; }} }}
@keyframes rise {{ from {{ opacity: 0; transform: translateY(24px); }} to {{ opacity: 1; transform: none; }} }}
@keyframes rays {{ to {{ transform: rotate(360deg); }} }}
@keyframes bob {{ 50% {{ transform: translateY(5px); }} }}
@keyframes rev {{ 0%, 100% {{ transform: translateX(0); opacity: 1; }} 50% {{ transform: translateX(-6px); opacity: .75; }} }}
@media (prefers-reduced-motion: reduce) {{ *, *::before, *::after {{ animation: none !important; transition: none !important; }} .rv {{ opacity: 1; transform: none; }} }}
</style>
</head>
<body>
<div class="obar"><p class="d9-only">O dobro do LOMBADA termina em</p>{CLOCK.replace('class="clock"', 'class="clock d9-only"')}<p class="after-only">Inscrições abertas · <b>Black Week Motorizada</b></p></div>

<main>
  <!-- 1. abertura (a única seção que ficou da versão anterior), já emendada na oferta -->
  <section class="h" id="topo">
    <div class="wrap h__in">
      {BWLOGO}
      <p class="kick h__kick">Inscrições liberadas</p>
      <h1 class="h__t"><span class="h__big gold">A maior oferta de todos os tempos</span><span class="h__sub"><b>+</b> <span class="h__col"><i class="novo-h">Novo</i>{LMB}<span class="h__tag">Seu livro, em movimento todo dia.</span></span></span></h1>
      <p class="trilha"><span class="l1"><span>Construa autoridade <i>›</i></span> <span>Seja lido de verdade <i>›</i></span></span> <span class="l2"><span>Gere impacto real <i>›</i></span> <span>Para sempre</span></span></p>
      <div class="hk2">
        <p>{CK}<span><b class="amber">Acesso vitalício</b> a toda a estratégia que já transformou milhares de autores em referência.</span></p>
        <p>{CK}<span>Os bônus mais poderosos já criados dentro da melhor estratégia literária do Brasil.</span></p>
      </div>

      <!-- 2. quanto custaria por um ano -->
      <div class="blk">
        <p class="q1">Para ter acesso <u>por um ano</u>, você <u>precisaria</u> investir:</p>
        <div class="bill">
          {BILL}
          <div class="bill__row bill__row--lmb"><span>{LMB}</span><b>R$ 2.000,00</b><i class="novo">Novo</i></div>
          <div class="bill__tot"><span>Total</span><b>R$ 9.485,00</b></div>
        </div>
      </div>

      <!-- 3. ao longo do tempo -->
      <div class="blk">
        <p class="q1">Agora, as contas de quanto você investiria para ter acesso a tudo isso ao longo do tempo:</p>
        <div class="bill">
          <!-- 08/11 (cliente): a conta segue o prazo do LOMBADA (6 anos no dia 9, 3 depois). 1º ano R$9.485; renova por ano Método + Autoridade + LOMBADA = R$5.000 (Comunidade e Workshops só no 1º ano) -->
          <div class="bill__row"><span>1º ano</span><b>R$ 9.485,00</b></div>
          <div class="bill__row"><span>2º ano</span><b>R$ 5.000,00</b></div>
          <div class="bill__row"><span>3º ano</span><b>R$ 5.000,00</b></div>
          <div class="bill__row d9-only"><span>4º ano</span><b>R$ 5.000,00</b></div>
          <div class="bill__row d9-only"><span>5º ano</span><b>R$ 5.000,00</b></div>
          <div class="bill__row d9-only"><span>6º ano</span><b>R$ 5.000,00</b></div>
          <div class="bill__tot"><span>Total investido</span><b><span class="d9-only">R$ 34.485,00</span><span class="after-only">R$ 19.485,00</span></b></div>
        </div>
      </div>

      <!-- 4. o preço -->
      <div class="blk price">
        <p class="q2">Mas comprando hoje, você não vai investir tudo isso.<br>Você só vai investir:</p>
        <p class="price__big"><small>12x de</small><span>R$ 249,51</span></p>
        <p class="price__cash">ou R$ 2.500 à vista</p>
        <p class="price__day">Menos de R$ 7 por dia no primeiro ano. E o Método é seu pra sempre.</p>
        <div class="cta price__cta">{CTA}<p class="fine">Garantia de 15 dias. Não gostou, devolvemos tudo.</p></div>
      </div>
    </div>
  </section>

  <!-- 5. bônus: o LOMBADA em dobro só hoje; os Playbooks ficam depois também -->
  <section class="sec d9" id="hoje">
    <div class="wrap center">
      <p class="q2 rv d9-only">E ainda por cima, quem entrar <b class="amber">hoje</b> vai ganhar:</p><p class="q2 rv after-only">E ainda por cima, você vai ganhar:</p>
      <div class="bon2">
        <div class="bon2__c rv d9-only">
          <div class="bon2__vis"><div class="dbl"><div class="dbl__a"><b>3 anos</b><small>normal</small></div><span class="dbl__ar" aria-hidden="true">→</span><div class="dbl__b"><b class="gold">6 anos</b><small>hoje</small></div></div>{SPINES}</div>
          <div class="bon2__txt">
          <span class="lv__k">Bônus 1</span>
          <h3>LOMBADA em dobro: 6 anos no lugar de 3.</h3>
          <p>Hoje você recebe o dobro: 6 anos com o LOMBADA ao lado do seu livro, todo dia. Amanhã volta a ser 3.</p>
                  </div>
        </div>
        <div class="bon2__c rv">
          <div class="bon2__vis"><img src="assets/playbooks.webp" alt="Playbooks MTBB" width="475" height="592" loading="lazy" decoding="async"></div>
          <div class="bon2__txt">
          <span class="lv__k"><span class="d9-only">Bônus 2</span><span class="after-only">Bônus</span></span>
          <h3>Playbooks MTBB físicos, entregues na sua casa.</h3>
          <p>A extensão prática do Método The&nbsp;Book&nbsp;Business, criada pela Dany, para organizar as estratégias e acompanhar a evolução do seu livro.</p>
                  </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 5b. cupons dos parceiros -->
  <section class="sec cups">
    <div class="wrap center">
      <div class="rv">
        <p class="kick">E tem mais</p>
        <h2 class="h2">Até <span class="gold">R$ 6.700</span> em cupons de desconto com parceiros.</h2>
        <p class="cups__l">Se você vai imprimir, publicar ou divulgar o seu livro, a Black já se paga.</p>
      </div>
      <div class="cupg">{CUPONS}</div>
      <p class="cups__fine rv">Cupons intransferíveis, de uso único, só para novos projetos e não cumulativos. Resgate com o e-mail de compra.</p>
    </div>
  </section>

  <!-- 6. resumo + botão -->
  <section class="sec resumo" id="oferta">
    <div class="wrap center">
      <div class="card rv">
        <p class="q2">Tudo o que você leva na Black Week Motorizada:</p>
        <ul class="card__list">
          <li>{CK}<span><b>Método The&nbsp;Book&nbsp;Business</b>, produtos e workshops, <b>vitalícios</b></span></li>
          <li>{CK}<span><b>LOMBADA</b> por <b class="d9-only">6 anos</b><b class="after-only">3 anos</b></span></li>
          <li>{CK}<span><b>Encontros em grupo</b> ao vivo com a Dany por 3 anos</span></li>
          <li>{CK}<span>Gravação de <b>100% das lives</b>, encontros e eventos</span></li>
          <li>{CK}<span><b>Playbooks MTBB físicos</b> na sua casa</span></li>
          <li>{CK}<span>Até <b>R$ 6.700 em cupons</b> de desconto com parceiros</span></li>
        </ul>
        <p class="resumo__de">De <s><span class="d9-only">R$ 34.485,00</span><span class="after-only">R$ 19.485,00</span></s></p>
        <p class="resumo__por">por apenas</p>
        <p class="price__big"><small>12x de</small><span>R$ 249,51</span></p>
        <p class="price__cash">ou R$ 2.500 à vista</p>
        <div class="card__clock d9-only"><p>O <b>dobro do LOMBADA</b> termina à meia-noite.</p>{CLOCK}</div>
        {CTA}
        <div class="seal"><i>15<small>dias</small></i><p><b>Garantia de 15 dias.</b> Entre, use, conheça tudo. Se não for pra você, devolvemos 100%.</p></div>
      </div>
      <div class="warn rv d9-only"><b>Atenção:</b> os 6 anos de LOMBADA são só para quem entrar hoje. A partir de amanhã, o LOMBADA volta a ser 3 anos.</div>
    </div>
  </section>

  <!-- 7. o que você leva: o LOMBADA num quadro especial (botão leva às telas), depois cada produto -->
  <section class="sec leva">
    <div class="wrap">
      <div class="center rv"><p class="kick">Quem aproveitar essa oferta agora</p><h2 class="h2">Vai levar:</h2></div>
      <div class="mtc rv">
        <img class="mtc__img" src="assets/p-metodo.webp" alt="Método The Book Business" width="720" height="567" loading="lazy" decoding="async">
        <div class="mtc__b">
          <span class="lv__k mtc__k">Acesso vitalício</span>
          <h3>Método The&nbsp;Book&nbsp;Business</h3>
          <p>O ecossistema completo de marketing literário. Tudo o que a Dany aprendeu em 15 anos nos bastidores das editoras, organizado para o autor: aulas práticas, passo a passo claro e modelos prontos para o seu livro ser lido, desejado e lembrado.</p>
          <ul>
            <li>Do primeiro livro ao décimo, da escrita à permanência.</li>
          </ul>
        </div>
      </div>
      <div class="lmbc rv">
        <div class="lmbc__art">{SPINES}<p class="lmbc__mark">{LMB}</p></div>
        <div class="lmbc__b">
          <span class="lv__k"><span class="d9-only">6 anos de acesso hoje</span><span class="after-only">3 anos de acesso</span></span>
          <h3>A ferramenta que nunca deixa o seu livro parar.</h3>
          <ul>
            <li><b>Seu livro não para:</b> toda semana, o plano pronto, com o texto e a aula por trás.</li>
            <li><b>Seu livro vai mais longe:</b> prêmios, feiras e editais do seu gênero, com o prazo na tela.</li>
            <li><b>Seu livro é lido:</b> ideias de post ilimitadas para novos leitores te encontrarem.</li>
          </ul>
          <a class="lmbc__btn" href="#ferramenta">Entender melhor o LOMBADA <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg></a>
        </div>
      </div>
      <div class="leva__g">{LEVA}</div>
      <div class="cta leva__cta rv">{CTA}</div>
    </div>
  </section>

  <!-- 7b. o LOMBADA em uma história só: a pessoa escreve o nome do livro e acompanha ele ir longe -->
  <section class="sec jorn" id="ferramenta">
    <div class="wrap">
      <div class="jn__head center rv">
        <p class="lmbh__mark">{LMB}</p>
        <div class="jn__vid" id="jn-vid"><vturb-smartplayer id="vid-6ae9e43f36e9cc736abb97c1" style="display:block;margin:0 auto;width:100%"></vturb-smartplayer></div>
        <h2 class="h2">Agora escreva o nome do seu livro. <span class="gold">E veja ele ir longe.</span></h2>
        <label class="jn__in"><span>O nome do seu livro</span><input id="jn-livro" type="text" maxlength="48" placeholder="Ex.: A Casa das Marés" autocomplete="off" enterkeyhint="done"></label>
        <p class="jn__hint">Experimente. É assim que o LOMBADA trabalha pelo seu livro.</p>
      </div>
      <ol class="jn">
        <li class="jn__s rv">
          <div class="jn__t"><span class="jn__n">1</span><h3>Segunda-feira, <b class="jl" data-l>o seu livro</b> já tem o que fazer.</h3><p>O plano da semana chega pronto, montado pela fase do livro, pelo gênero e pelo tempo que você tem. Você só executa.</p></div>
          <div class="jn__app">
            <div class="ap__top">{LMB_S}<span class="ap__tg">Plano da semana</span></div>
            <p class="ap__ti" data-l-cap>O seu livro</p>
            <div class="ap__pr"><span id="jn-cont">0 de 3 feitas</span><i><b id="jn-bar"></b></i></div>
            <div class="ap__acts" id="jn-acts"></div>
          </div>
        </li>
        <li class="jn__s rv">
          <div class="jn__t"><span class="jn__n">2</span><h3>O texto já vem escrito.</h3><p>Cada ação traz o texto pronto, com o nome do seu livro, e a aula do Método The&nbsp;Book&nbsp;Business explicando o porquê.</p></div>
          <div class="jn__app">
            <div class="ap__top">{LMB_S}<span class="ap__tg">Texto pronto</span></div>
            <div class="ap__txt" id="jn-txt"></div>
            <button type="button" class="ap__copy" id="jn-copy">Copiar texto</button>
          </div>
        </li>
        <li class="jn__s rv">
          <div class="jn__t"><span class="jn__n">3</span><h3><b class="jl" data-l-cap>O seu livro</b> chega a lugares novos.</h3><p>Prêmios, feiras e editais do gênero do seu livro, com o prazo na tela. Nenhuma chance passa por você.</p></div>
          <div class="jn__app">
            <div class="ap__top">{LMB_S}<span class="ap__tg">Oportunidades</span></div>
            <div class="ap__pills" id="jn-gen" role="group" aria-label="Gênero do livro"><button type="button" aria-pressed="true" data-g="Romance">Romance</button><button type="button" aria-pressed="false" data-g="Infantil">Infantil</button><button type="button" aria-pressed="false" data-g="Negócios">Negócios</button><button type="button" aria-pressed="false" data-g="Poesia">Poesia</button><button type="button" aria-pressed="false" data-g="Biografia e memórias">Memórias</button></div>
            <div class="ap__ops" id="jn-ops"></div>
          </div>
        </li>
        <li class="jn__s rv">
          <div class="jn__t"><span class="jn__n">4</span><h3>E encontra leitores.</h3><p>Ideias de post sem fim, feitas para o seu livro. Toque e gere mais: elas nunca acabam.</p></div>
          <div class="jn__app">
            <div class="ap__top">{LMB_S}<span class="ap__tg">Ideias de post</span></div>
            <div class="ap__ideas" id="jn-ideas"></div>
            <button type="button" class="ap__copy" id="jn-more">Gerar mais ideias</button>
          </div>
        </li>
        <li class="jn__s rv">
          <div class="jn__t"><span class="jn__n">5</span><h3><b class="jl" data-l-cap>O seu livro</b> ganha uma página só dele.</h3><p>No ar, montada a partir do seu cadastro, com a capa, a sinopse e o link para comprar. Pronta para mandar para leitores, imprensa e livrarias.</p></div>
          <div class="jn__app">
            <div class="ap__top">{LMB_S}<span class="ap__tg">Página do livro</span></div>
            <div class="pg">
              <div class="pg__bar"><i></i><i></i><i></i><span>lombada.thebookbusiness.com.br/<b id="jn-slug">o-seu-livro</b></span></div>
              <div class="pg__b">
                <div class="pg__capa"><span data-l-cap>O seu livro</span></div>
                <div class="pg__t"><p class="pg__ti" data-l-cap>O seu livro</p><p class="pg__au">por você</p><p class="pg__si">A sinopse do seu livro aparece aqui, do jeito que você escreveu no cadastro.</p><span class="pg__btn">Comprar o livro</span></div>
              </div>
            </div>
          </div>
        </li>
        <li class="jn__s rv">
          <div class="jn__t"><span class="jn__n">6</span><h3>E entra na vitrine, para vender mais.</h3><p>O seu livro entra na vitrine dos autores do LOMBADA, com a capa ao lado de outros autores e filtro por gênero. Cada capa leva direto para a página do livro.</p></div>
          <div class="jn__app vt2">
            <div class="vt2__top">{LMB_S}<span>Vitrine dos autores</span></div>
            <div class="vt2__chips"><i class="on">Todos</i><i>Romance</i><i>Infantojuvenil</i><i>Fantasia</i><i>Contos</i></div>
            <div class="vt2__grid"><div class="vb"><div class="vb__c"><img src="assets/vt-mar.webp" alt="" width="164" height="240" loading="lazy" decoding="async"></div><p class="vb__t">Mar de Dentro</p><p class="vb__a">Clara Moura</p></div><div class="vb vb--me"><span class="vb__tag">Seu livro</span><div class="vb__c"><div class="vb__capa"><b data-l-cap>O seu livro</b><small>você</small></div></div><p class="vb__t" data-l-cap>O seu livro</p><p class="vb__a">Você</p></div><div class="vb"><div class="vb__c"><img src="assets/vt-liderar.webp" alt="" width="164" height="240" loading="lazy" decoding="async"></div><p class="vb__t">Liderar sem Gritar</p><p class="vb__a">Caio Nunes</p></div><div class="vb"><div class="vb__c"><img src="assets/vt-raizes.webp" alt="" width="164" height="240" loading="lazy" decoding="async"></div><p class="vb__t">Raízes</p><p class="vb__a">Marta Dias</p></div><div class="vb"><div class="vb__c"><img src="assets/vt-mapa.webp" alt="" width="164" height="240" loading="lazy" decoding="async"></div><p class="vb__t">O Mapa</p><p class="vb__a">Sofia Lins</p></div><div class="vb"><div class="vb__c"><img src="assets/vt-verao.webp" alt="" width="164" height="240" loading="lazy" decoding="async"></div><p class="vb__t">O Último Verão</p><p class="vb__a">Inês Lago</p></div></div>
          </div>
        </li>
      </ol>
      <div class="jn__end rv">
        <p class="jn__e1">Daqui a <span class="d9-only">6</span><span class="after-only">3</span> anos,</p>
        <p class="jn__e2"><b class="jl" data-l>o seu livro</b> ainda vai estar sendo lido.</p>
        <figure class="jn__dep"><blockquote>A ideia de construir o hábito de trabalhar no livro diariamente, por meio de pequenas ações, foi especialmente motivadora.</blockquote><figcaption><b>Georgiana Leite</b>, autora de <i>Vai Brilhar!</i>, usou o LOMBADA no piloto</figcaption></figure>
        <div class="cta">{CTA}</div>
      </div>
    </div>
  </section>

  <!-- 8. casos -->
  <section class="sec casos-sec">
    <div class="wrap">
      <div class="center rv"><h2 class="h2">A estratégia que mais transforma autores comuns em <span class="serif gold"><span style="white-space:nowrap">best-sellers</span> de verdade.</span></h2></div>
      <div class="vids">{VIDEOS}</div>
      <p class="vids__k rv">E tem muito mais autor chegando longe:</p>
    </div>
    {CASOS_BELT}
    <div class="wrap">
      <p class="casos__more rv">E muito mais.</p>
      <div class="cta leva__cta rv">{CTA}</div>
    </div>
  </section>

  <!-- 8b. garantia -->
  <section class="sec gar">
    <div class="wrap">
      <div class="gar__c rv">
        <div class="gar__seal"><b>15</b><span>dias de<br>garantia</span></div>
        <div class="gar__t">
          <p class="gar__k">Risco zero para você</p>
          <h2>Entre, use, conheça tudo.</h2>
          <p>Você tem 15 dias para entrar no Método The&nbsp;Book&nbsp;Business, abrir o LOMBADA e testar com o seu livro. Se não for pra você, devolvemos 100% do valor. Sem pergunta.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 9. quem é a Dany -->
  <section class="sec dany">
    <div class="wrap">
      <div class="dany__g">
        <figure class="dany__pic rv"><img src="../black-week/assets/dany-palco.webp" alt="Dany Sakugawa" width="680" height="1207" loading="lazy" decoding="async"></figure>
        <div class="rv">
          <h2 class="dany__h">Quem é a <span class="serif gold">Dany Sakugawa?</span></h2>
          <div class="dany__l">
            <p>Uma das maiores referências em marketing editorial do país. Mais de 15 anos nos bastidores das grandes editoras, por trás de lançamentos que ultrapassaram <b>10 milhões de exemplares vendidos</b>.</p>
            <p>Deixou o cargo de diretora de marketing em uma das maiores editoras do Brasil para guiar autores pelo melhor caminho, com ou sem editora.</p>
            <p><b>Criou o Método The&nbsp;Book&nbsp;Business. E agora, o LOMBADA.</b></p>
          </div>
          <div class="stats">
            <div class="stat"><b>+15</b><span>anos nos bastidores das editoras</span></div>
            <div class="stat"><b>+800</b><span>autores lançados</span></div>
            <div class="stat"><b>+10M</b><span>livros vendidos em lançamentos</span></div>
            <div class="stat"><b>+4.400</b><span>alunos no Método The&nbsp;Book&nbsp;Business</span></div>
          </div>
        </div>
      </div>
      <div class="midia__k rv"><p class="kick">Dany na mídia</p></div>
      <div class="midia rv"><div class="midia__t">{MIDIA}{MIDIA}</div></div>
    </div>
  </section>

  <!-- 8. fecho -->
  <section class="sec end">
    <div class="wrap rv">
      <p class="kick">Black Week Motorizada</p>
      <p class="end__a">Essa é a sua <span class="serif gold">chance.</span></p>
      <p class="end__b">Tudo o que a Dany criou, pra sempre. E o LOMBADA ao lado do seu livro, todo dia.</p>
      <div class="end__price"><p class="price__big"><small>12x de</small><span>R$ 249,51</span></p><p class="price__cash">ou R$ 2.500 à vista</p></div>
      <div class="card__clock d9-only"><p>O <b>dobro do LOMBADA</b> termina à meia-noite.</p>{CLOCK}</div>
      <div class="cta">{CTA}<p class="fine">Garantia de 15 dias. Não gostou, devolvemos tudo.</p></div>
    </div>
  </section>
</main>

<footer>
  <p>© 2026 The Book Business. Todos os direitos reservados.</p>
  <p><a href="https://thebookbusiness.com.br/contrato-vitalicio-26" target="_blank" rel="noopener">Termos da oferta</a> · <a href="https://thebookbusiness.com.br/wp-content/uploads/2026/07/Politica-de-Privacidade_6514.pdf" target="_blank" rel="noopener">Política de Privacidade</a></p>
  <p class="legal"><b>Aviso Legal:</b> “Nenhuma informação contida neste site deve ser interpretada como uma afirmação de resultados ou de retornos financeiros. Qualquer referência a desempenho passado ou potencial é uma estratégia elaborada no contexto individual de cada autor, e não deve ser interpretada como recomendação ou garantia de resultados específicos.”</p>
</footer>

<div class="dock" id="dock"><a class="btn" href="#oferta" data-cta>Quero entrar na Black {SETA}</a></div>
<a class="zap" href="https://thebookbusiness.com.br/dezza" target="_blank" rel="noopener" aria-label="Falar com a Dezza no WhatsApp"><svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.04 3C8.86 3 3.02 8.83 3.02 16c0 2.3.6 4.53 1.74 6.5L3 29l6.68-1.75A12.95 12.95 0 0 0 16.04 29C23.2 29 29.04 23.17 29.04 16S23.2 3 16.04 3Zm0 23.62c-1.98 0-3.92-.53-5.61-1.54l-.4-.24-3.97 1.04 1.06-3.86-.26-.4a10.6 10.6 0 0 1-1.63-5.64c0-5.86 4.78-10.63 10.66-10.63 5.87 0 10.64 4.77 10.64 10.63 0 5.87-4.78 10.64-10.49 10.64Zm5.83-7.96c-.32-.16-1.89-.93-2.18-1.04-.29-.11-.5-.16-.72.16-.21.32-.82 1.04-1.01 1.25-.19.21-.37.24-.69.08-.32-.16-1.35-.5-2.57-1.59-.95-.85-1.59-1.9-1.78-2.22-.19-.32-.02-.49.14-.65.14-.14.32-.37.48-.56.16-.19.21-.32.32-.53.11-.21.05-.4-.03-.56-.08-.16-.72-1.73-.98-2.37-.26-.62-.52-.54-.72-.55h-.61c-.21 0-.56.08-.85.4-.29.32-1.12 1.09-1.12 2.66s1.14 3.09 1.3 3.3c.16.21 2.25 3.43 5.45 4.81.76.33 1.36.53 1.82.67.77.24 1.46.21 2.01.13.61-.09 1.89-.77 2.15-1.52.27-.74.27-1.38.19-1.52-.08-.13-.29-.21-.61-.37Z"/></svg></a>

<script>
(function () {{
  'use strict';
  var $$ = function (s) {{ return [].slice.call(document.querySelectorAll(s)); }};
  var q = new URLSearchParams(location.search);

  // modo: dia 9 até 23h59 de Brasília (02h59 UTC do dia 10); depois, LOMBADA 3 anos (os Playbooks continuam)
  var FIM_D9 = Date.UTC(2026, 10, 10, 2, 59, 59);
  var modo = q.get('modo') || (Date.now() <= FIM_D9 ? 'd9' : 'depois');
  document.body.classList.add(modo === 'depois' ? 'm-depois' : 'm-d9');

  // checkout (Hotmart): oferta R$2.500 do combo novo da Black (8902433, off=lyfitc09, pela máscara oferta-black26 com repasse de parâmetros, cliente 06/11; antes D102625845Q off=ntrx21f9). Repassa src/sck/utm até o checkout.
  var CHECKOUT = {{ d9: 'https://thebookbusiness.com.br/oferta-black26', depois: 'https://thebookbusiness.com.br/oferta-black26' }}, url = CHECKOUT[modo === 'depois' ? 'depois' : 'd9'];
  if (url) {{
    var u = new URL(url);
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'sck', 'src'].forEach(function (k) {{ if (q.get(k)) u.searchParams.set(k, q.get(k)); }});
    $$('[data-cta]').forEach(function (a) {{ a.href = u.toString(); }});
  }}

  // relógio até a meia-noite do dia 9
  var clocks = $$('[data-clock]');
  function pad(n) {{ return (n < 10 ? '0' : '') + n; }}
  function tick() {{
    var s = Math.max(0, Math.floor((FIM_D9 - Date.now()) / 1000)), h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60);
    var html = (h >= 24 ? '<span>' + Math.floor(h / 24) + '<small>dias</small></span>' : '') + '<span>' + pad(h % 24) + '<small>horas</small></span><span>' + pad(m) + '<small>min</small></span><span>' + pad(s % 60) + '<small>seg</small></span>';
    clocks.forEach(function (c) {{ c.innerHTML = html; }});
  }}
  if (modo !== 'depois') {{ tick(); setInterval(tick, 1000); }}

  // story do LOMBADA: troca de tela sozinha (4,5 s), a imagem desce devagar; toque passa para a próxima
  (function () {{
    var box = document.getElementById('story'); if (!box) return;
    var imgs = [].slice.call(box.querySelectorAll('.story__scr img')), txt = [].slice.call(box.querySelectorAll('.st')), bars = [].slice.call(box.querySelectorAll('.story__bars i'));
    var scr = box.querySelector('.story__scr'), i = 0, t = null, DUR = 5000;
    var tabs = [].slice.call(document.querySelectorAll('.wk button'));
    tabs.forEach(function (b, k) {{ b.addEventListener('click', function () {{ started = true; show(k); }}); }});
    function show(n) {{
      i = (n + imgs.length) % imgs.length;
      imgs.forEach(function (im, k) {{ im.classList.remove('on'); if (k === i) {{ void im.offsetWidth; var d = im.offsetHeight - scr.offsetHeight; im.style.setProperty('--pan', (d > 0 ? -d : 0) + 'px'); im.classList.add('on'); }} }});
      txt.forEach(function (x, k) {{ x.classList.toggle('on', k === i); }});
      tabs.forEach(function (x, k) {{ x.classList.toggle('on', k === i); x.setAttribute('aria-selected', k === i); }});
      bars.forEach(function (b, k) {{ b.classList.remove('run'); b.classList.toggle('done', k < i); if (k === i) {{ void b.offsetWidth; b.classList.add('run'); }} }});
      clearTimeout(t); t = setTimeout(function () {{ show(i + 1); }}, DUR);
    }}
    box.querySelector('.story__ph').addEventListener('click', function () {{ show(i + 1); }});
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) DUR = 9000;
    var started = false;
    function go() {{ if (!started) {{ started = true; show(0); }} }}
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) {{ if (es[0].isIntersecting) go(); }}, {{ threshold: .3 }}).observe(box); else go();
  }})();

  // contador de dias: sobe quando aparece
  (function () {{
    var el = document.querySelector('.days__n'); if (!el) return;
    var to = +el.getAttribute(modo === 'depois' ? 'data-to-depois' : 'data-to-d9'), done = false;
    function fmt(v) {{ return Math.round(v).toLocaleString('pt-BR'); }}
    function run() {{ if (done) return; done = true; var t0 = performance.now(), dur = 2200;
      (function step(now) {{ var k = Math.min(1, (now - t0) / dur); el.textContent = fmt(to * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(step); }})(t0); }}
    if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {{ el.textContent = fmt(to); return; }}
    new IntersectionObserver(function (es) {{ if (es[0].isIntersecting) run(); }}, {{ threshold: .5 }}).observe(el);
  }})();

  // casos: 3 faixas rolando, cada uma para um lado (cliente: "três linhas, uma indo para cada lado")
  (function () {{
    var belts = $$('.casos-belt');
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    belts.forEach(function (belt) {{
      var track = belt.querySelector('.casos-track');
      track.style.animationDuration = Math.round(track.scrollWidth / 28) + 's';
      track.insertAdjacentHTML('beforeend', track.innerHTML.replace(/<figure class="caso">/g, '<figure class="caso" aria-hidden="true">'));
      belt.addEventListener('touchstart', function () {{ belt.classList.add('hold'); }}, {{ passive: true }});
      belt.addEventListener('touchend', function () {{ setTimeout(function () {{ belt.classList.remove('hold'); }}, 1200); }}, {{ passive: true }});
    }});
  }})();

  // vídeos: só carrega o YouTube quando a pessoa clica
  $$('.vid').forEach(function (b) {{
    b.addEventListener('click', function () {{
      if (b.querySelector('iframe')) return;
      b.insertAdjacentHTML('beforeend', '<iframe src="https://www.youtube-nocookie.com/embed/' + b.getAttribute('data-yt') + '?autoplay=1&rel=0" title="Depoimento" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>');
    }});
  }});

  // o LOMBADA em uma história: o nome que a pessoa escreve vira o personagem da seção inteira
  (function () {{
    var inp = document.getElementById('jn-livro'); if (!inp) return;
    {JN_DADOS}
    function esc(x) {{ return String(x).replace(/[&<>"']/g, function (c) {{ return {{ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }}[c]; }}); }}
    function nome() {{ return inp.value.trim(); }}
    function L(cap) {{ var n = nome(); return n ? n : (cap ? 'O seu livro' : 'o seu livro'); }}
    function T(sx) {{ return esc(sx).replace(/\{{T\}}/g, '<b class="jl">' + esc(L(false)) + '</b>'); }}
    var ACTS = [['Republique um trecho de {{T}} como post', '20 min · com texto pronto'], ['Peça avaliação a quem comprou {{T}}', '30 min · com texto pronto'], ['Busque uma audiência nova para falar de {{T}}', '45 min · com a aula por trás']];
    var TXT = '"[o seu trecho favorito]"\\n\\nEsse é um trecho de {{T}}. Escrevi para [quem vai ler], e é a parte que mais recebo mensagem.\\n\\nSe essa frase mexeu com você, o livro inteiro está aqui: [link do seu livro]';
    var feitas = {{}}, acts = document.getElementById('jn-acts'), cont = document.getElementById('jn-cont'), bar = document.getElementById('jn-bar');
    function rActs() {{
      acts.innerHTML = ACTS.map(function (a, i) {{ return '<button type="button" class="ap__act' + (feitas[i] ? ' ok' : '') + '" data-i="' + i + '"><i>✓</i><span><b>' + T(a[0]) + '</b><small>' + a[1] + '</small></span></button>'; }}).join('');
      var n = Object.keys(feitas).filter(function (k) {{ return feitas[k]; }}).length;
      cont.textContent = n + ' de 3 feitas'; bar.style.width = (n / 3 * 100) + '%';
    }}
    acts.addEventListener('click', function (e) {{ var b = e.target.closest('.ap__act'); if (!b) return; var i = b.getAttribute('data-i'); feitas[i] = !feitas[i]; rActs(); }});
    var txt = document.getElementById('jn-txt');
    function rTxt() {{ txt.innerHTML = T(TXT).replace(/\[(.+?)\]/g, '<span class="vr">$1</span>'); }}
    document.getElementById('jn-copy').addEventListener('click', function () {{
      var b = this, plain = TXT.replace(/\{{T\}}/g, L(false));
      var ok = function () {{ b.textContent = 'Copiado'; setTimeout(function () {{ b.textContent = 'Copiar texto'; }}, 1600); }};
      if (navigator.clipboard) navigator.clipboard.writeText(plain).then(ok, ok); else ok();
    }});
    var MES = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'], hoje = new Date(); hoje.setHours(0, 0, 0, 0);
    var gen = 'Romance', opsBox = document.getElementById('jn-ops'), genBox = document.getElementById('jn-gen');
    function serve(gs, g) {{ return gs === ALL || gs.indexOf(g) !== -1; }}
    function dias(d) {{ return Math.round((d - hoje) / 864e5); }}
    function rOps() {{
      var it = OPS.filter(function (o) {{ return serve(o[5], gen); }}).map(function (o) {{ return {{ d: new Date(o[0] + 'T00:00:00'), n: o[4], ty: o[3], tp: o[1] }}; }});
      it = it.filter(function (o) {{ return dias(o.d) >= 0; }}).sort(function (a, b) {{ return a.d - b.d; }}).slice(0, 4);
      opsBox.innerHTML = it.map(function (o) {{ var n = dias(o.d), ev = o.tp === 'evento' || o.tp === 'data';
        return '<div class="ap__op"><div class="d"><b>' + o.d.getDate() + '</b><small>' + MES[o.d.getMonth()] + '</small></div><div><p>' + esc(o.n) + '</p><span>' + o.ty + '</span><span class="cd">' + (ev ? 'Em ' : 'Vence em ') + n + ' dias</span></div></div>'; }}).join('');
    }}
    genBox.addEventListener('click', function (e) {{ var b = e.target.closest('button'); if (!b) return; [].forEach.call(genBox.children, function (x) {{ x.setAttribute('aria-pressed', x === b); }}); gen = b.getAttribute('data-g'); rOps(); }});
    var TONS = ['inspirador', 'provocativo', 'educativo', 'humor'], ideias = [], ideasBox = document.getElementById('jn-ideas'), k = 0;
    function mais() {{ for (var j = 0; j < 3; j++) {{ var tom = TONS[k % 4], lista = IDEIAS[tom]; ideias.unshift([tom, lista[Math.floor(k / 4) % lista.length]]); k++; }} rIdeas(); ideasBox.scrollTop = 0; }}
    function rIdeas() {{ ideasBox.innerHTML = ideias.map(function (x, i) {{ return '<div class="ap__idea"><small>Ideia ' + (ideias.length - i) + ' · ' + x[0] + '</small><p>' + T(x[1][0]) + '</p><span>' + esc(x[1][1]) + '</span></div>'; }}).join(''); }}
    document.getElementById('jn-more').addEventListener('click', mais);
    function slug(x) {{ return (x || 'o seu livro').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''); }}
    function rNome() {{
      document.getElementById('jn-slug').textContent = slug(nome());
      [].forEach.call(document.querySelectorAll('[data-l]'), function (el) {{ el.textContent = L(false); }});
      [].forEach.call(document.querySelectorAll('[data-l-cap]'), function (el) {{ el.textContent = L(true); }});
      rActs(); rTxt(); rIdeas();
    }}
    inp.addEventListener('input', rNome);
    mais(); rOps(); rNome();
  }})();

  // vídeo do LOMBADA no vturb (player 6ae9e43f36e9cc736abb97c1): o script só carrega quando a seção chega perto da tela
  (function () {{
    var box = document.getElementById('jn-vid'); if (!box) return;
    function carrega() {{ if (box._ok) return; box._ok = 1; var sc = document.createElement('script'); sc.src = 'https://scripts.converteai.net/6b353be1-c671-4a98-af52-02bc731efaae/players/6ae9e43f36e9cc736abb97c1/v4/player.js'; sc.async = true; document.head.appendChild(sc); }}
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) {{ if (es[0].isIntersecting) carrega(); }}, {{ rootMargin: '900px 0px' }}).observe(box); else carrega();
  }})();

  // entrada dos blocos: a pilha entra item por item
  if ('IntersectionObserver' in window) {{
    var io = new IntersectionObserver(function (es) {{ es.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }}); }}, {{ rootMargin: '0px 0px -10% 0px' }});
    $$('.rv').forEach(function (el) {{ io.observe(el); }});
  }} else $$('.rv').forEach(function (el) {{ el.classList.add('in'); }});

  // botão fixo no celular: aparece depois do primeiro preço e some quando um botão da página já está na tela
  var dock = document.getElementById('dock'), passou = false, vis = 0;
  function upd() {{ dock.classList.toggle('on', passou && vis === 0); }}
  if ('IntersectionObserver' in window) {{
    var preco = document.querySelector('.price');
    addEventListener('scroll', function () {{ var p = preco.getBoundingClientRect().bottom < 0; if (p !== passou) {{ passou = p; upd(); }} }}, {{ passive: true }});
    var io2 = new IntersectionObserver(function (es) {{ es.forEach(function (e) {{ vis += e.isIntersecting ? 1 : (e.target._v ? -1 : 0); e.target._v = e.isIntersecting; }}); vis = Math.max(0, vis); upd(); }});
    $$('main .btn').forEach(function (b) {{ io2.observe(b); }});
  }}
}})();
</script>
</body>
</html>
'''
# 05/11 (cliente: "teste ab"): os anúncios de venda mandam para a longa; metade de quem vem do anúncio (utm_source=meta-ads)
# vai para a curta, sempre a mesma pessoa na mesma versão (localStorage bf26pg). Quem chega por e-mail/WhatsApp fica na longa.
# O sck do checkout ganha |pgL ou |pgC para ler a venda por versão na Hotmart.
# 05/11 (cliente: "tem dash desse teste ab?" → "sim agora"): o teste vira o ab_testes 'bf26-oferta-pagina' (painel da Black no Miolo).
# Só quem está no teste (bf26pg) grava visita ('view') e clique no checkout ('initiate') em ab_eventos e leva a marca |bfpL/|bfpC no sck;
# a venda entra sozinha pelo gatilho ab_purchase_from_venda (sck_tag 'bfp', pagina '' porque o sck do anúncio começa pelo id da campanha).
# Sem sck no link (volta pelo e-mail), usa o sck guardado da 1ª visita do anúncio.
AB_LONGA = ("<script>(function(){try{var q=new URLSearchParams(location.search);if(q.get('utm_source')!=='meta-ads')return;"
            "var v=localStorage.getItem('bf26pg');if(v!=='L'&&v!=='C'){v=Math.random()<.5?'L':'C';localStorage.setItem('bf26pg',v)}"
            "if(v==='C')location.replace('/5c0424242e97/'+location.search+location.hash)}catch(e){}})();</script>\n")
AB_CURTA = "<script>try{localStorage.setItem('bf26pg','C')}catch(e){}</script>\n"
_px = '<script src="../pixel.js"></script>'
_ck = "$$('[data-cta]').forEach(function (a) { a.href = u.toString(); });"
assert HTML.count(_px) == 1 and HTML.count(_ck) == 1
AB_TRACK = ("var ABV = 'L', abIn = false; try { abIn = localStorage.getItem('bf26pg') === ABV; } catch (e) {}\n"
  "    if (abIn) {\n"
  "      var abVid, abSck = q.get('sck');\n"
  "      try { abVid = localStorage.getItem('bf26vid'); if (!abVid) { abVid = Date.now().toString(36) + Math.random().toString(36).slice(2, 10); localStorage.setItem('bf26vid', abVid); }\n"
  "        if (abSck) localStorage.setItem('bf26sck', abSck); else abSck = localStorage.getItem('bf26sck'); } catch (e) {}\n"
  "      u.searchParams.set('sck', (abSck || 'bf26oferta') + '|bfp' + ABV);\n"
  "      var abEv = function (ev) { try { fetch('https://jsqtpsxpaclslakafmvd.supabase.co/rest/v1/ab_eventos', { method: 'POST', keepalive: true,\n"
  "        headers: { apikey: AK_AB, Authorization: 'Bearer ' + AK_AB, 'Content-Type': 'application/json', Prefer: 'return=minimal' },\n"
  "        body: JSON.stringify({ teste_slug: 'bf26-oferta-pagina', variante: ABV, evento: ev, visitor_id: abVid || null, sck: abSck || null }) }); } catch (e) {} };\n"
  "      var abSeen = null; try { abSeen = localStorage.getItem('bf26pg_view'); } catch (e) {}\n"
  "      if (abSeen !== ABV) { try { localStorage.setItem('bf26pg_view', ABV); } catch (e) {} abEv('view'); }\n"
  "      $$('[data-cta]').forEach(function (a) { a.addEventListener('click', function () { abEv('initiate'); }); });\n"
  "    }\n    ").replace("AK_AB", "'" + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpzcXRwc3hwYWNsc2xha2FmbXZkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUzMTY5NTMsImV4cCI6MjA5MDg5Mjk1M30.6f3CmgozaE3fTORF0SBSeRDzZNZ1E27tcdQ9h6tKLgc" + "'")
HTML = HTML.replace(_px, AB_LONGA + _px).replace(_ck, AB_TRACK + _ck)
HTML = HTML.replace('</main>', "<script>(function(){function fit(){var t=document.querySelector('.h__col .h__tag'),l=document.querySelector('.h__col .lmb');if(!t||!l)return;t.style.fontSize='20px';var w=l.getBoundingClientRect().width,n=t.getBoundingClientRect().width;if(!w||!n)return;var f=Math.max(12,Math.min(32,20*w/n));t.style.fontSize=f+'px';}if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit);window.addEventListener('load',fit);window.addEventListener('resize',fit);fit();})();</script>\n" + '</main>', 1)
# 08/11 (cliente): a capa do "seu livro" igual na página do livro e na vitrine
_CAPA_OLD = '<div class="pg__capa"><span data-l-cap>O seu livro</span></div>'
assert _CAPA_OLD in HTML
HTML = HTML.replace(_CAPA_OLD, '<div class="pg__capa"><b data-l-cap>O seu livro</b><small>você</small></div>')
HTML = HTML.replace('</style>\n</head>', '.pg__capa { flex-direction: column; justify-content: space-between; align-items: stretch; padding: 12% 10% 8%; background: linear-gradient(160deg, #fe7743, #b5402e) !important; }\n.pg__capa b { font-size: 15px; font-weight: 800; line-height: 1.1; color: #fff; text-align: center; overflow-wrap: anywhere; }\n.pg__capa small { font-size: 8px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: rgba(255,255,255,.8); text-align: center; }\n</style>\n</head>', 1)
EQV_BLOCO = '\n<!-- 08/11 (cliente): verificador de número da equipe (anti-golpe), mesma lista de verificar-numero-equipe/widget_rodape.html -->\n<section class="eqv-wrap" style="padding:0 16px">\n<div id="eqv-card">\n  <h2 class="eqv-title">Verifique o número do nosso time</h2>\n  <p class="eqv-sub">Preencha o campo abaixo com o número de whatsapp e valide se faz parte da nossa equipe.</p>\n\n  <div class="eqv-row">\n    <div class="eqv-inputwrap">\n      <span class="eqv-flag">🇧🇷 <span class="eqv-ddi">+55</span></span>\n      <input id="eqv-phone" type="tel" inputmode="tel" autocomplete="off"\n             placeholder="(00) 0 0000-0000" maxlength="16" />\n    </div>\n    <button id="eqv-btn" type="button">Verificar Número</button>\n  </div>\n\n  <div id="eqv-result" class="eqv-result" hidden></div>\n</div>\n\n</section>\n<style>\n  #eqv-card{ max-width:640px; margin:8px auto 36px; background:#121212; border:1px solid #2a2a2a; border-radius:20px; padding:32px 22px; text-align:center; font-family:inherit; box-sizing:border-box; }\n  .eqv-title{ font-size:24px; line-height:1.2; font-weight:800; color:#fff; margin:0 0 10px; }\n  .eqv-sub{ font-size:14.5px; color:#a8a399; margin:0 auto 22px; max-width:520px; line-height:1.5; }\n  .eqv-row{ display:flex; align-items:stretch; max-width:500px; margin:0 auto; background:#0a0a0a; border:1px solid #333; border-radius:999px; padding:6px; }\n  .eqv-inputwrap{ display:flex; align-items:center; flex:1; padding-left:14px; min-width:0; }\n  .eqv-flag{ font-size:14px; color:#8d887f; white-space:nowrap; margin-right:8px; }\n  #eqv-phone{ flex:1; border:0; outline:0; background:transparent; font:inherit; font-size:16px; font-weight:500; color:#fff; min-width:0; padding:10px 4px; }\n  #eqv-phone::placeholder{ color:#5c5850; }\n  #eqv-btn{ border:0; cursor:pointer; background:#1ebb00; color:#fff; font:inherit; font-weight:800; font-size:15px; padding:0 26px; border-radius:999px; white-space:nowrap; }\n  #eqv-btn:hover{ background:#19a300; }\n  .eqv-result{ margin:18px auto 0; max-width:520px; padding:14px 18px; border-radius:14px; font-size:17px; font-weight:700; line-height:1.4; }\n  .eqv-result.ok{ background:rgba(30,187,0,.14); color:#6fe35a; }\n  .eqv-result.no{ background:rgba(226,75,74,.14); color:#ff8a89; }\n  .eqv-result.neutral{ background:#1c1c1c; color:#a8a399; font-weight:500; font-size:15px; }\n  @media (max-width:600px){ .eqv-row{ flex-direction:column; border-radius:16px; gap:8px; padding:10px; } .eqv-inputwrap{ justify-content:center; padding:6px 4px; } #eqv-btn{ padding:14px; width:100%; } }\n</style>\n<script>\n(function () {\n  \'use strict\';\n  if (window.__eqvInit) return; window.__eqvInit = true;\n\n  /* ============ EQUIPE — editar só aqui pra atualizar ============ */\n  var EQUIPE = [\n    { num: \'38 98848-7665\', nome: \'Aira\'    },\n    { num: \'81 98637-0023\', nome: \'Dezza\'   },\n    { num: \'11 92469-3585\', nome: \'Natália\' },\n    { num: \'11 94083-3397\', nome: \'Mariana\' },\n    { num: \'11 97829-5602\', nome: \'Bianca\'  },\n    { num: \'11 91519-4847\', nome: \'Time\'    }\n  ];\n  /* ============================================================== */\n\n  function canon(p) {\n    var d = String(p || \'\').replace(/\\D/g, \'\');\n    if (d.length < 10) return \'\';\n    if (d.length === 10 || d.length === 11) d = \'55\' + d;\n    if (d.length === 12 && \'6789\'.indexOf(d.charAt(4)) > -1) d = d.slice(0, 4) + \'9\' + d.slice(4);\n    return d;\n  }\n\n  var MAPA = {};\n  EQUIPE.forEach(function (e) { var c = canon(e.num); if (c) MAPA[c] = e.nome; });\n\n  var inp = document.getElementById(\'eqv-phone\');\n  var btn = document.getElementById(\'eqv-btn\');\n  var box = document.getElementById(\'eqv-result\');\n  if (!inp || !btn || !box) return;\n\n  function digits(s) { return String(s || \'\').replace(/\\D/g, \'\'); }\n\n  function mascara(v) {\n    v = digits(v);\n    if (v.indexOf(\'55\') === 0 && v.length > 11) v = v.slice(2);\n    v = v.slice(0, 11);\n    if (v.length > 7)      v = v.replace(/^(\\d{2})(\\d{1})(\\d{4})(\\d{0,4}).*/, \'($1) $2 $3-$4\');\n    else if (v.length > 3) v = v.replace(/^(\\d{2})(\\d{1})(\\d{0,4}).*/, \'($1) $2 $3\');\n    else if (v.length > 2) v = v.replace(/^(\\d{2})(\\d{0,1}).*/, \'($1) $2\');\n    else if (v.length > 0) v = v.replace(/^(\\d{0,2}).*/, \'($1\');\n    return v;\n  }\n  inp.addEventListener(\'input\', function () { inp.value = mascara(inp.value); });\n\n  function show(cls, text) { box.hidden = false; box.className = \'eqv-result \' + cls; box.textContent = text; }\n\n  function verificar() {\n    var c = canon(inp.value);\n    if (c === \'\') { show(\'neutral\', \'Digite o número completo, com DDD.\'); return; }\n    if (MAPA[c]) show(\'ok\', \'✓ Sim! Este número é da nossa equipe (\' + MAPA[c] + \').\');\n    else         show(\'no\', \'Este número não faz parte do Time\');\n  }\n\n  btn.addEventListener(\'click\', verificar);\n  inp.addEventListener(\'keydown\', function (e) { if (e.key === \'Enter\') { e.preventDefault(); verificar(); } });\n})();\n</script>\n'
assert '</main>\n\n<footer>' in HTML
HTML = HTML.replace('</main>\n\n<footer>', '</main>\n' + EQV_BLOCO + '\n<footer>', 1)
open(f"{R}/ae8a9e17e350/index.html", "w", encoding="utf-8").write(HTML)
print("ok", len(HTML))

# 02/11 (cliente): versão CURTA, igual à oferta mas sem a demo do LOMBADA (seção 7b) e sem o botão que leva até ela.
# Mesmos arquivos da oferta (assets apontam para ../ae8a9e17e350/). Saída: 5c0424242e97/index.html
_a = HTML.index('  <!-- 7b. o LOMBADA em uma história só')
_b = HTML.index('  <!-- 8. casos -->')
CURTA = HTML[:_a] + HTML[_b:]
_btn = CURTA.index('<a class="lmbc__btn" href="#ferramenta">')
CURTA = CURTA[:_btn] + CURTA[CURTA.index('</a>', _btn) + 4:]
CURTA = (CURTA.replace('src="assets/', 'src="../ae8a9e17e350/assets/')
              .replace('url("../assets/', 'url("../assets/')
              .replace('<link rel="canonical" href="https://metodo.thebookbusiness.com.br/ae8a9e17e350/">',
                       '<link rel="canonical" href="https://metodo.thebookbusiness.com.br/5c0424242e97/">')
              .replace('<meta property="og:url" content="https://metodo.thebookbusiness.com.br/ae8a9e17e350/">',
                       '<meta property="og:url" content="https://metodo.thebookbusiness.com.br/5c0424242e97/">'))
CURTA = CURTA.replace(AB_LONGA, AB_CURTA).replace("var ABV = 'L'", "var ABV = 'C'")
assert 'id="ferramenta"' not in CURTA and 'href="#ferramenta"' not in CURTA and 'bf26pg' in CURTA and "var ABV = 'C'" in CURTA
os.makedirs(f"{R}/5c0424242e97", exist_ok=True)
open(f"{R}/5c0424242e97/index.html", "w", encoding="utf-8").write(CURTA)
print("curta", len(CURTA))

# 08/11 (cliente): versões de ALUNO (R$ 1.000) e VITALÍCIO (R$ 500) da oferta longa, nos endereços escondidos que os links
# finais black-liberada-alunos / black-liberada-vitalicio abrem a partir de 09/11 20h. Sem o teste A/B (não sorteia
# para a curta de R$ 2.500, não grava em ab_eventos); checkout pela máscara de cada uma, repassando src/sck/utm.
VARIANTES = {
    'eda7d6898635': dict(rot='aluno', checkout='https://thebookbusiness.com.br/oferta-black-alunos', preco='R$ 1.000',
                         dia='Menos de R$ 3 por dia no primeiro ano. E o Método é seu pra sempre.',
                         kick='Condição exclusiva de aluno do Método', title='Black Week Motorizada · Alunos'),
    'c966d3cc27f2': dict(rot='vitalício', checkout='https://thebookbusiness.com.br/oferta-black-vitalicio', preco='R$ 500',
                         dia='Menos de R$ 1,50 por dia no primeiro ano. O Método você já tem pra sempre.',
                         kick='Condição exclusiva de aluno vitalício', title='Black Week Motorizada · Alunos vitalícios'),
}
for slug, v in VARIANTES.items():
    P = HTML.replace(AB_LONGA, '').replace(AB_TRACK, '')
    P = P.replace("var CHECKOUT = { d9: 'https://thebookbusiness.com.br/oferta-black26', depois: 'https://thebookbusiness.com.br/oferta-black26' }",
                  "var CHECKOUT = { d9: '%s', depois: '%s' }" % (v['checkout'], v['checkout']))
    P = P.replace('<p class="price__big"><small>12x de</small><span>R$ 249,51</span></p>', '<p class="price__big"><small>por</small><span>%s</span></p>' % v['preco'])
    P = P.replace('<p class="price__cash">ou R$ 2.500 à vista</p>', '<p class="price__cash">à vista ou parcelado no cartão</p>')
    P = P.replace('<p class="price__day">Menos de R$ 7 por dia no primeiro ano. E o Método é seu pra sempre.</p>', '<p class="price__day">%s</p>' % v['dia'])
    P = P.replace('<p class="kick h__kick">Inscrições liberadas</p>', '<p class="kick h__kick">%s</p>' % v['kick'])
    P = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % v['title'], P, count=1)
    P = (P.replace('src="assets/', 'src="../ae8a9e17e350/assets/')
          .replace('https://metodo.thebookbusiness.com.br/ae8a9e17e350/"', 'https://metodo.thebookbusiness.com.br/%s/"' % slug))
    assert 'bf26pg' not in P and 'oferta-black26' not in P.split('var CHECKOUT')[1][:300] and v['preco'] in P and '249,51' not in P and 'R$ 2.500 à vista' not in P, slug
    os.makedirs(f"{R}/{slug}", exist_ok=True)
    open(f"{R}/{slug}/index.html", "w", encoding="utf-8").write(P)
    print(v['rot'], slug, len(P))
