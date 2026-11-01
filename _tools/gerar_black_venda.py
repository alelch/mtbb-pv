# 01/11/2026 · Página de VENDA da Black Week Motorizada, feita do zero (cliente: "você está muito apegado ao que a gente
# tinha antes"; "quero uma coisa magnânima, onde o autor fale: nossa, essa é a melhor chance possível!").
# Nada da página de cadastro: abertura de oferta, a pilha de tudo o que entra (pacote do Aniversário sem o Retiro),
# o LOMBADA em telas reais, bônus do dia 9, Dany, preço, dúvidas, fecho.
# Só o logo da Black e o wordmark do LOMBADA vêm da black-week/ (marca). Saída: black-week-oferta/index.html
# Modo: até 23h59 de 9/11 (Brasília) = "dia 9" (LOMBADA 6 anos + Playbooks + relógio); depois = LOMBADA 3 anos.
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
    ("Método The&nbsp;Book&nbsp;Business", "Nova versão 2026. Toda a estratégia, do primeiro livro ao décimo.", "Vitalício"),
    ("Autoridade Digital para Escritores", "Quais redes usar, o que postar e como ser descoberto.", "Vitalício"),
    ("Gerador de Posts Magnéticos", "Ideias ilimitadas, feitas para o seu livro.", "Vitalício"),
    ("Calendário Estratégico do Autor", "O ano inteiro mapeado, mês a mês.", "Vitalício"),
    ("Comunidade The&nbsp;Book&nbsp;Business", "Mais de 2.000 escritores. A sua nova turma.", "Vitalício"),
    ("Workshop MasterClass Best-Seller de Verdade", "", "Vitalício"),
    ("Workshop Redes Sociais para Autores", "", "Vitalício"),
    ("Workshop Prêmios e Concursos Literários", "", "Vitalício"),
    ("Workshop Escrita Criativa", "", "Vitalício"),
    ("Workshop Planejamento Anual", "", "Vitalício"),
    ("Gravação de 100% das lives, encontros e eventos", "Com roteiristas premiadas, agentes literárias e publishers das maiores editoras.", "Vitalício"),
    ("Encontros em grupo ao vivo com a Dany", "Todo mês, para ajustar a estratégia do seu livro.", "3 anos"),
    ("Projeto Especial Prêmio Jabuti", "", "Vitalício"),
    ("Projeto Especial Autopublicação Profissional", "", "Vitalício"),
    ("Projeto Especial Editora Perfeita", "", "Vitalício"),
    ("Projeto Especial Destaque Amazon", "", "Vitalício"),
]
rows = "\n".join(
    f'        <li class="row rv"><span class="row__n">{i:02d}</span><span class="row__t"><b>{t}</b>{f"<small>{d}</small>" if d else ""}</span><span class="row__k">{k}</span></li>'
    for i, (t, d, k) in enumerate(PILHA, 1))
N = len(PILHA) + 1  # + LOMBADA
rows += f'''
        <li class="row row--lmb rv"><span class="row__n">{N:02d}</span><span class="row__t"><b>{LMB}</b><small>O personal trainer do seu livro. Todo dia, o que fazer.</small></span><span class="row__k"><span class="d9-only">6 anos</span><span class="after-only">3 anos</span></span></li>
        <li class="row row--bonus rv d9-only"><span class="row__n">{N+1:02d}</span><span class="row__t"><b>Playbooks MTBB físicos, na sua casa</b><small>Só para quem entrar hoje.</small></span><span class="row__k">Bônus</span></li>'''

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


BILL = "".join(f'<div class="bill__row"><span>{n.replace("The Book Business", "The&nbsp;Book&nbsp;Business")}</span><b>{v}</b></div>' for n, v in [('Método The Book Business', 'R$ 1.500,00'), ('Autoridade Digital para Escritores', 'R$ 1.500,00'), ('Gerador de Posts Magnéticos', 'R$ 297,00'), ('Calendário Estratégico do Autor', 'R$ 297,00'), ('Comunidade The Book Business', 'R$ 500,00'), ('Workshops Mão na Massa (5)', 'R$ 2.500,00'), ('Projeto Especial Prêmio Jabuti', 'R$ 1.200,00'), ('Projeto Especial Destaque Amazon', 'R$ 1.200,00'), ('Projeto Especial Autopublicação', 'R$ 1.200,00'), ('Projeto Especial Editora Perfeita', 'R$ 1.200,00')])
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
  ("Acesso vitalício", "Gerador de Posts Magnéticos", "Ideias ilimitadas, feitas pelo gênero do seu livro, pela fase e pelo seu jeito de falar. Posts em minutos."),
  ("Acesso vitalício", "Calendário Estratégico do Autor", "O ano inteiro mapeado, com datas comemorativas e ideias de posts mês a mês."),
  ("Acesso vitalício", "Comunidade The&nbsp;Book&nbsp;Business", "A maior comunidade de autores do Brasil, com mais de 2.000 escritores. A sua nova turma."),
  ("Acesso vitalício", "Workshops Mão na Massa", "<ul><li>MasterClass Best-Seller de Verdade</li><li>Redes Sociais para Autores</li><li>Prêmios e Concursos Literários</li><li>Escrita Criativa</li><li>Planejamento Anual</li></ul>"),
  ("Acesso vitalício", "Gravação de 100% das lives, encontros e eventos", "Para rever quando quiser. Com roteiristas premiadas, agentes literárias e publishers das maiores editoras do país."),
  ("3 anos", "Encontros em grupo ao vivo com a Dany", "36 encontros ao vivo com a Dany para tirar dúvidas e ajustar a estratégia do seu livro. O que muitos chamam de mentoria, aqui está incluído."),
  ("Projeto Especial", "Prêmio Jabuti", "A inscrição certa, na categoria certa, no maior prêmio literário do país."),
  ("Projeto Especial", "Autopublicação Profissional", "Revisão, capa, diagramação, ISBN e distribuição, com padrão de mercado."),
  ("Projeto Especial", "Editora Perfeita", "Como analisar propostas e escolher a editora certa para o seu livro."),
  ("Projeto Especial", "Destaque Amazon", "Título, descrição, categorias e palavras-chave para o seu livro aparecer na Amazon."),
]
LEVA = "".join(f'<div class="lv rv"><span class="lv__k">{k}</span><h3>{t}</h3>{d if d.startswith("<ul>") else f"<p>{d}</p>"}</div>' for k, t, d in _LEVA)

HTML = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Black Week Motorizada · A maior oferta de todos os tempos</title>
<meta name="description" content="Tudo o que a Dany Sakugawa criou para autores, pra sempre. E o LOMBADA, o personal trainer do seu livro. Na Black Week Motorizada.">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#000000">
<link rel="canonical" href="https://metodo.thebookbusiness.com.br/black-week-oferta/">
<link rel="icon" type="image/webp" href="../lancamento90d/favicon.webp">
<meta property="og:type" content="website">
<meta property="og:title" content="Black Week Motorizada · Inscrições liberadas">
<meta property="og:description" content="Tudo o que a Dany criou para autores, pra sempre. E o LOMBADA.">
<meta property="og:image" content="https://metodo.thebookbusiness.com.br/black-week/assets/og-black-week.jpg">
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
.h__t {{ margin: 18px auto 0; max-width: 1080px; animation: rise 1.1s var(--ease) .25s both; }}
.h__a {{ display: block; font-size: clamp(30px, 8.6vw, 74px); font-weight: 800; line-height: 1.02; letter-spacing: -.035em; text-wrap: balance; }}
.h__b {{ display: block; margin-top: 4px; padding-bottom: .08em; font-size: clamp(76px, 24vw, 200px); line-height: .9; }}
.h__plus {{ margin-top: 18px; font-size: clamp(16px, 4.5vw, 22px); color: var(--ink2); animation: rise 1s var(--ease) .45s both; text-wrap: balance; }}
.h__plus .lmb {{ color: var(--ink); font-size: 1.35em; vertical-align: -.12em; }}
.h__price {{ display: inline-flex; align-items: baseline; gap: 8px; margin-top: 28px; padding: 10px 20px; border-radius: 99px; background: rgba(250, 171, 0, .1); box-shadow: inset 0 0 0 1px rgba(250, 171, 0, .5); animation: rise 1s var(--ease) .55s both; }}
.h__price span {{ font-size: 14px; color: var(--ink2); }}
.h__price b {{ font-size: clamp(22px, 6vw, 28px); font-weight: 800; }}
.h .cta {{ max-width: 480px; margin: 22px auto 0; animation: rise 1s var(--ease) .65s both; }}
.h__cue {{ display: inline-flex; flex-direction: column; align-items: center; gap: 6px; margin-top: 34px; font-size: 12px; font-weight: 600; letter-spacing: .2em; text-transform: uppercase; color: var(--ink3); text-decoration: none; }}
.h__cue svg {{ width: 20px; height: 20px; animation: bob 1.8s ease-in-out infinite; }}

/* LOMBADA: a semana e o "ele ainda te dá" */
.lv.lv--lmb .lv__big {{ margin: 14px auto 0; max-width: 760px; font-size: clamp(28px, 8vw, 52px); font-weight: 800; line-height: 1.05; letter-spacing: -.03em; color: var(--paper-ink); text-wrap: balance; }}
.lv.lv--lmb .lv__lead {{ margin-top: 12px; font-size: clamp(15px, 4.2vw, 18px); font-weight: 600; letter-spacing: .14em; text-transform: uppercase; color: #8a5a00; }}
.wk {{ display: flex; justify-content: center; gap: 6px; margin-top: 18px; flex-wrap: wrap; }}
.wk button {{ min-width: 54px; padding: 9px 10px; border: 0; border-radius: 99px; background: #fff; color: var(--paper-soft); box-shadow: 0 0 0 1px #e3ded2; font: 700 13px/1 "Poppins", sans-serif; letter-spacing: .06em; text-transform: uppercase; cursor: pointer; transition: background .25s, color .25s; }}
.wk button.on {{ background: var(--paper-ink); color: var(--amber); box-shadow: none; }}
.lv.lv--lmb .story {{ margin-top: 22px; }}
.lv.lv--lmb .lv__mais {{ color: var(--paper-ink); margin-top: 44px; font-size: clamp(22px, 6vw, 32px); font-weight: 800; letter-spacing: -.02em; }}
.tiles {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 860px; margin: 18px auto 0; text-align: left; }}
@media (min-width: 860px) {{ .tiles {{ grid-template-columns: 1fr 1fr 1fr; }} }}
.tile {{ padding: 16px 14px; border-radius: 16px; background: #fff; box-shadow: 0 0 0 1px #e3ded2; }}
.tile i {{ display: grid; place-items: center; width: 40px; height: 40px; border-radius: 12px; background: var(--paper-ink); color: var(--amber); }}
.tile svg {{ width: 21px; height: 21px; }}
.tile b {{ display: block; margin-top: 12px; font-size: 15px; font-weight: 800; line-height: 1.2; color: var(--paper-ink); }}
.tile span {{ display: block; margin-top: 4px; font-size: 13px; line-height: 1.45; color: var(--paper-soft); }}

/* abertura emendada na oferta (ordem do Aniversário) */
.hk {{ max-width: 560px; margin: 26px auto 0; list-style: none; display: grid; gap: 12px; text-align: left; }}
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
.price {{ margin-top: 64px; }}
.price__big {{ margin-top: 14px; line-height: 1; }}
.price__big small {{ display: block; font-size: 18px; font-weight: 500; color: var(--ink2); }}
.price__big span {{ display: block; margin-top: 6px; font-size: clamp(60px, 18vw, 104px); font-weight: 800; letter-spacing: -.04em; background: var(--gold); background-size: 220% 100%; -webkit-background-clip: text; background-clip: text; color: transparent; animation: gold 6s linear infinite; }}
.price__cash {{ margin-top: 8px; font-size: 16px; color: var(--ink2); }}
.price__cta {{ max-width: 480px; margin: 26px auto 0; }}
.resumo .card__list {{ margin-top: 22px; }}
.bon2 {{ display: grid; grid-template-columns: minmax(0, 1fr); gap: 16px; max-width: 900px; margin: 34px auto 0; }}
@media (min-width: 760px) {{ .bon2 {{ grid-template-columns: 1fr 1fr; }} }}
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
.casos {{ display: grid; grid-template-columns: minmax(0, 1fr); gap: 10px; max-width: 980px; margin: 40px auto 0; }}
@media (min-width: 700px) {{ .casos {{ grid-template-columns: 1fr 1fr; }} }}
@media (min-width: 1000px) {{ .casos {{ grid-template-columns: 1fr 1fr 1fr; }} }}
.caso {{ display: flex; align-items: center; gap: 14px; padding: 14px 16px; border-radius: 14px; background: #121114; box-shadow: inset 0 0 0 1px #222126; }}
.caso img {{ flex: none; width: 56px; height: 56px; border-radius: 50%; object-fit: cover; border: 1.5px solid rgba(250, 171, 0, .5); }}
.caso figcaption {{ min-width: 0; line-height: 1.25; }}
.caso strong {{ display: block; font-size: 15px; font-weight: 700; color: var(--amber); }}
.caso b {{ display: block; margin-top: 4px; font-size: 13px; font-weight: 600; }}
.caso span {{ display: block; font-size: 12px; color: var(--ink3); }}
.casos__more {{ margin-top: 18px; text-align: center; font-size: 15px; color: var(--ink2); }}

/* abertura: a maior oferta */
.h__big {{ display: block; font-size: clamp(46px, 13.6vw, 100px); font-weight: 800; line-height: .94; letter-spacing: -.035em; text-transform: uppercase; text-wrap: balance; padding-bottom: .04em; }}
.h__sub {{ display: block; margin-top: 18px; font-size: clamp(24px, 7vw, 52px); font-weight: 700; line-height: 1.1; letter-spacing: -.02em; color: var(--ink); text-wrap: balance; }}
.h__sub b {{ color: var(--amber); font-weight: 800; margin-right: .2em; }}
.h .h__sub {{ display: flex; justify-content: center; align-items: center; font-size: clamp(40px, 12vw, 84px); }}
.h__sub .lmb {{ color: var(--ink); }}
.h__tag {{ display: block; margin-top: 12px; font-size: clamp(20px, 5.8vw, 36px); font-weight: 600; line-height: 1.2; letter-spacing: -.01em; color: var(--ink2); text-wrap: balance; }}

/* story do LOMBADA */
.story {{ display: grid; grid-template-columns: minmax(0, 1fr); gap: 18px; align-items: center; max-width: 940px; margin: 48px auto 0; }}
@media (min-width: 860px) {{ .story {{ grid-template-columns: 340px 1fr; gap: 64px; }} }}
.story__ph {{ position: relative; width: min(64vw, 320px); margin: 0 auto; padding: 10px; border-radius: 40px; background: linear-gradient(160deg, #2b2a2f, #0e0e10 60%); box-shadow: 0 40px 70px -30px rgba(0, 0, 0, .6); cursor: pointer; }}
.story__bars {{ position: absolute; left: 24px; right: 24px; top: 20px; z-index: 3; display: flex; gap: 4px; }}
.story__bars i {{ flex: 1; height: 3px; border-radius: 3px; background: rgba(0, 0, 0, .18); overflow: hidden; }}
.story__bars b {{ display: block; height: 100%; width: 0; background: var(--paper-ink); }}
.story__bars i.done b {{ width: 100%; }}
.story__bars i.run b {{ animation: bar var(--dur, 4.5s) linear forwards; }}
.story__scr {{ position: relative; aspect-ratio: 716 / 1300; overflow: hidden; border-radius: 30px; background: #fff; }}
.story__scr img {{ position: absolute; left: 0; top: 0; width: 100%; height: auto; opacity: 0; transition: opacity .45s ease; }}
.story__scr img.on {{ opacity: 1; animation: pan var(--dur, 4.5s) ease-in-out forwards; }}
.story__txt {{ position: relative; min-height: 150px; order: -1; }}
@media (min-width: 860px) {{ .story__txt {{ order: 0; min-height: 190px; }} }}
.st {{ position: absolute; inset: 0 0 auto; opacity: 0; transform: translateY(14px); transition: opacity .45s ease, transform .45s var(--ease); pointer-events: none; text-align: center; }}
.st.on {{ position: relative; opacity: 1; transform: none; }}
@media (min-width: 860px) {{ .st {{ text-align: left; }} }}
.st__n {{ font-size: 13px; font-weight: 800; letter-spacing: .2em; color: #8a5a00; }}
.st__t, .lv .st__t {{ margin-top: 8px; font-size: clamp(24px, 6.6vw, 46px); font-weight: 800; line-height: 1.08; letter-spacing: -.025em; text-wrap: balance; }}
.st__d, .lv .st__d {{ margin-top: 8px; font-size: clamp(15px, 4.1vw, 20px); line-height: 1.5; color: var(--paper-soft); text-wrap: balance; }}

/* contador de dias */
.days {{ overflow: hidden; isolation: isolate; text-align: center; }}
.days::before {{ content: ""; position: absolute; left: 50%; top: 50%; width: 900px; height: 900px; z-index: -1; transform: translate(-50%, -50%); border-radius: 50%; background: radial-gradient(closest-side, rgba(250, 171, 0, .2), transparent); }}
.days__n, .lv .days__n {{ font-size: clamp(110px, 34vw, 280px); font-weight: 800; line-height: .85; letter-spacing: -.05em; font-variant-numeric: tabular-nums; }}
.days__a, .lv .days__a {{ margin: 18px auto 0; max-width: 720px; font-size: clamp(26px, 7.4vw, 50px); font-weight: 800; line-height: 1.08; letter-spacing: -.025em; text-wrap: balance; }}
.days__b {{ margin-top: 16px; font-size: clamp(15px, 4.2vw, 19px); color: var(--ink2); }}

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

/* 2. a pilha */
.pile {{ background: linear-gradient(var(--bg), var(--bg2)); border-top: 1px solid var(--line); }}
.pile__lede {{ margin: 18px auto 0; max-width: 560px; font-size: clamp(16px, 4.4vw, 20px); color: var(--ink2); text-wrap: balance; }}
.rows {{ max-width: 860px; margin: 48px auto 0; list-style: none; border-top: 1px solid var(--line); }}
.row {{ display: grid; grid-template-columns: 30px minmax(0, 1fr) auto; gap: 12px; align-items: center; padding: 18px 2px; border-bottom: 1px solid var(--line); }}
.row__n {{ font-size: 13px; font-weight: 700; color: var(--ink3); font-variant-numeric: tabular-nums; }}
.row__t b {{ display: block; font-size: clamp(17px, 4.6vw, 23px); font-weight: 700; line-height: 1.2; letter-spacing: -.01em; }}
.row__t small {{ display: block; margin-top: 3px; font-size: 14px; line-height: 1.4; color: var(--ink3); }}
.row__k {{ padding: 5px 10px; border-radius: 99px; background: rgba(250, 171, 0, .12); color: var(--amber); font-size: 10px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; white-space: nowrap; }}
.row--lmb {{ margin: 10px -12px 0; padding: 24px 12px; border: 0; border-radius: 16px; background: radial-gradient(ellipse 80% 120% at 50% 0%, rgba(250, 171, 0, .2), transparent 70%), #100d07; box-shadow: inset 0 0 0 1.5px rgba(250, 171, 0, .6); }}
.row--lmb .row__t b {{ font-size: clamp(30px, 8.4vw, 44px); }}
.row--lmb .lmb {{ color: var(--ink); }}
.row--lmb .row__n {{ color: var(--amber); }}
.row--lmb .row__k {{ background: var(--amber); color: #111; font-size: 12px; }}
.row--bonus {{ margin: 10px -12px 0; padding: 20px 12px; border: 0; border-radius: 16px; background: #0f1a0c; box-shadow: inset 0 0 0 1.5px rgba(30, 187, 0, .55); }}
.row--bonus .row__k {{ background: var(--green); color: #fff; }}
.rv {{ opacity: 0; transform: translateY(26px); transition: opacity .7s var(--ease), transform .7s var(--ease); }}
.rv.in {{ opacity: 1; transform: none; }}
.total {{ margin-top: 64px; text-align: center; }}
.total__n {{ font-size: clamp(120px, 40vw, 300px); font-weight: 800; line-height: .82; letter-spacing: -.06em; }}
.total__a {{ margin-top: 10px; font-size: clamp(24px, 7vw, 46px); font-weight: 800; line-height: 1.1; letter-spacing: -.02em; text-wrap: balance; }}
.total__b {{ margin-top: 10px; font-size: clamp(34px, 10vw, 64px); line-height: 1.05; }}
.total .cta {{ max-width: 480px; margin: 34px auto 0; }}

/* 3. LOMBADA em telas reais */
.lmbs {{ background: var(--paper); color: var(--paper-ink); overflow: hidden; }}
.lmbs .kick {{ color: #8a5a00; }}
.lmbs__mark {{ margin-top: 18px; font-size: clamp(46px, 13vw, 140px); line-height: 1; }}
.lmbs__mark .lmb {{ color: var(--paper-ink); }}
.lmbs__p {{ margin: 22px auto 0; max-width: 600px; font-size: clamp(18px, 5vw, 26px); font-weight: 500; line-height: 1.4; text-wrap: balance; }}
.lmbs__pair {{ display: inline-grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 26px; }}
.lmbs__pair span {{ padding: 14px 18px; border-radius: 12px; background: #fff; box-shadow: 0 0 0 1px #e3ded2; font-size: clamp(14px, 4vw, 18px); font-weight: 700; }}
.lmbs__pair span:last-child {{ background: var(--paper-ink); color: var(--amber); box-shadow: none; }}
.telas {{ display: flex; gap: 18px; margin-top: 52px; padding: 10px 20px 26px; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }}
.telas::-webkit-scrollbar {{ display: none; }}
@media (min-width: 1100px) {{ .telas {{ justify-content: center; overflow: visible; }} }}
.tela {{ flex: none; width: min(68vw, 250px); scroll-snap-align: center; }}
.tela__ph {{ position: relative; padding: 9px; border-radius: 34px; background: linear-gradient(160deg, #2b2a2f, #0e0e10 60%); box-shadow: 0 30px 60px -28px rgba(0, 0, 0, .55); }}
.tela__ph img {{ width: 100%; aspect-ratio: 716 / 1300; object-fit: cover; object-position: top; border-radius: 26px; background: #fff; }}
.tela figcaption {{ margin-top: 14px; text-align: center; }}
.tela figcaption b {{ display: block; font-size: 16px; font-weight: 700; }}
.tela figcaption span {{ display: block; margin-top: 2px; font-size: 13.5px; line-height: 1.4; color: var(--paper-soft); }}
.lmbs__note {{ margin-top: 6px; font-size: 12px; color: var(--paper-soft); text-align: center; }}
.lmbs__swipe {{ margin-top: 4px; font-size: 12px; font-weight: 600; color: #8a5a00; text-align: center; }}
@media (min-width: 1100px) {{ .lmbs__swipe {{ display: none; }} }}

/* 4. bônus do dia 9 */
.d9 {{ overflow: hidden; isolation: isolate; border-top: 1px solid var(--line); }}
.d9::before {{ content: ""; position: absolute; inset: 0; z-index: -1; background: radial-gradient(ellipse 70% 60% at 50% 30%, rgba(250, 171, 0, .22), transparent 70%); }}
.d9__big {{ margin-top: 10px; font-size: clamp(100px, 32vw, 240px); font-weight: 800; line-height: .85; letter-spacing: -.05em; }}
.d9__sub {{ margin-top: 8px; font-size: clamp(22px, 6vw, 36px); font-weight: 800; letter-spacing: -.02em; }}
.d9__p {{ margin: 14px auto 0; max-width: 520px; font-size: clamp(16px, 4.4vw, 20px); color: var(--ink2); text-wrap: balance; }}
.d9__plus {{ margin: 40px auto 0; font-size: clamp(36px, 10vw, 56px); font-weight: 800; line-height: 1; color: var(--amber); }}
.d9__pb {{ display: grid; grid-template-columns: minmax(0, 1fr); gap: 20px; align-items: center; max-width: 860px; margin: 16px auto 0; text-align: left; }}
@media (min-width: 760px) {{ .d9__pb {{ grid-template-columns: 1fr 1fr; }} }}
.d9__pb img {{ width: 100%; max-width: 380px; margin: 0 auto; filter: drop-shadow(0 30px 40px rgba(0, 0, 0, .7)); }}
.d9__pb h3 {{ font-size: clamp(24px, 6.4vw, 34px); font-weight: 800; line-height: 1.1; letter-spacing: -.02em; }}
.d9__pb p {{ margin-top: 12px; font-size: 16px; line-height: 1.55; color: var(--ink2); }}
.d9__pb ul {{ margin-top: 14px; list-style: none; display: flex; flex-wrap: wrap; gap: 8px; }}
.d9__pb li {{ padding: 6px 12px; border-radius: 99px; background: #15120c; box-shadow: inset 0 0 0 1px #3a3226; font-size: 13px; font-weight: 600; }}
.d9__end {{ margin-top: 48px; }}
.d9__end p {{ margin-bottom: 14px; font-size: 14px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--amber); }}

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

/* 7. dúvidas */
.faq {{ border-top: 1px solid var(--line); }}
.faq__l {{ max-width: 720px; margin: 36px auto 0; }}
.faq details {{ border-bottom: 1px solid var(--line); }}
.faq summary {{ display: flex; justify-content: space-between; gap: 14px; padding: 20px 2px; cursor: pointer; list-style: none; font-size: clamp(16px, 4.4vw, 19px); font-weight: 600; }}
.faq summary::-webkit-details-marker {{ display: none; }}
.faq summary::after {{ content: "+"; flex: none; color: var(--amber); font-size: 24px; line-height: 1; transition: transform .2s; }}
.faq details[open] summary::after {{ transform: rotate(45deg); }}
.faq details p {{ padding: 0 2px 20px; font-size: 16px; line-height: 1.55; color: var(--ink2); }}

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
<div class="obar"><p class="d9-only">O dobro do LOMBADA e os bônus terminam em</p>{CLOCK.replace('class="clock"', 'class="clock d9-only"')}<p class="after-only">Inscrições abertas · <b>Black Week Motorizada</b></p></div>

<main>
  <!-- 1. abertura (a única seção que ficou da versão anterior), já emendada na oferta -->
  <section class="h" id="topo">
    <div class="wrap h__in">
      {BWLOGO}
      <p class="kick h__kick">Inscrições liberadas</p>
      <h1 class="h__t"><span class="h__big gold">A maior oferta de todos os tempos</span><span class="h__sub"><b>+</b> {LMB}</span><span class="h__tag">A ferramenta que leva o seu livro cada vez mais longe.</span></h1>
      <ul class="hk">
        <li>{CK}<span><b class="amber">Acesso vitalício</b> a toda a estratégia que já transformou milhares de autores em referência.</span></li>
        <li>{CK}<span>O <b>LOMBADA</b>, o personal trainer do seu livro, por <b class="d9-only">6 anos</b><b class="after-only">3 anos</b>.</span></li>
        <li class="d9-only">{CK}<span>Os bônus mais poderosos já criados dentro da melhor estratégia literária do Brasil.</span></li>
        <li class="after-only">{CK}<span><b>3 anos de encontros em grupo</b> ao vivo com a Dany.</span></li>
      </ul>

      <!-- 2. quanto custaria por um ano -->
      <div class="blk">
        <p class="q1">Para ter acesso <u>por um ano</u> a todos os produtos dessa oferta, você <u>precisaria</u> investir:</p>
        <div class="bill">
          {BILL}
          <div class="bill__row bill__row--lmb"><span>{LMB}</span><b>nunca foi vendido</b></div>
          <div class="bill__tot"><span>Total</span><b>R$ 10.594,00</b></div>
        </div>
      </div>

      <!-- 3. ao longo do tempo -->
      <div class="blk">
        <p class="q1">Agora, as contas de quanto você investiria para ter acesso a tudo isso ao longo do tempo:</p>
        <div class="bill">
          <div class="bill__row"><span>Todos os produtos · 1º ano</span><b>R$ 10.594,00</b></div>
          <div class="bill__row"><span>Todos os produtos · 2º ano</span><b>R$ 5.297,00</b></div>
          <div class="bill__row"><span>Todos os produtos · 3º ano</span><b>R$ 5.297,00</b></div>
          <div class="bill__row"><span>Todos os produtos · 4º ano</span><b>R$ 5.297,00</b></div>
          <div class="bill__tot"><span>Total investido</span><b>R$ 26.485,00</b></div>
        </div>
      </div>

      <!-- 4. o preço -->
      <div class="blk price">
        <p class="q2">Mas comprando hoje, você não vai investir tudo isso.<br>Você só vai investir:</p>
        <p class="price__big"><small>12x de</small><span>R$ 249,51</span></p>
        <p class="price__cash">ou R$ 2.500 à vista</p>
        <div class="cta price__cta">{CTA}<p class="fine">Garantia de 15 dias. Não gostou, devolvemos tudo.</p></div>
      </div>
    </div>
  </section>

  <!-- 5. bônus de hoje -->
  <section class="sec d9 d9-only" id="hoje">
    <div class="wrap center">
      <p class="q2 rv">E ainda por cima, quem entrar <b class="amber">hoje</b> vai ganhar:</p>
      <div class="bon2">
        <div class="bon2__c rv">
          <span class="lv__k">Bônus 1</span>
          <p class="bon2__big gold">6 anos</p>
          <h3>de {LMB}. O dobro.</h3>
          <p>Amanhã volta a ser 3. Quem entra hoje leva o LOMBADA ao lado do seu livro por 6 anos.</p>
        </div>
        <div class="bon2__c rv">
          <span class="lv__k">Bônus 2</span>
          <img src="assets/playbooks.webp" alt="Playbooks MTBB" width="475" height="592" loading="lazy" decoding="async">
          <h3>Playbooks MTBB, entregues fisicamente na sua casa.</h3>
          <p>A nova extensão prática do Método The&nbsp;Book&nbsp;Business, criada pessoalmente pela Dany. Pra anotar ideias, organizar estratégias e acompanhar a evolução do seu livro.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 6. resumo + botão -->
  <section class="sec resumo" id="oferta">
    <div class="wrap center">
      <div class="card rv">
        <p class="q2">Resumindo: na Black Week Motorizada você leva tudo isso, mais o LOMBADA<span class="d9-only"> e os bônus de hoje</span>.</p>
        <ul class="card__list">
          <li>{CK}<span><b>Método The&nbsp;Book&nbsp;Business</b>, produtos, workshops e Projetos Especiais, <b>vitalícios</b></span></li>
          <li>{CK}<span><b>LOMBADA</b> por <b class="d9-only">6 anos</b><b class="after-only">3 anos</b></span></li>
          <li>{CK}<span><b>Encontros em grupo</b> ao vivo com a Dany por 3 anos</span></li>
          <li>{CK}<span>Gravação de <b>100% das lives</b>, encontros e eventos</span></li>
          <li class="d9-only">{CK}<span><b>Playbooks MTBB físicos</b> na sua casa</span></li>
        </ul>
        <p class="resumo__de">De <s>R$ 26.485,00</s></p>
        <p class="resumo__por">por apenas</p>
        <p class="price__big"><small>12x de</small><span>R$ 249,51</span></p>
        <p class="price__cash">ou R$ 2.500 à vista</p>
        <div class="card__clock d9-only"><p><b>6 anos de LOMBADA e os Playbooks</b> terminam à meia-noite.</p>{CLOCK}</div>
        {CTA}
        <div class="seal"><i>15<small>dias</small></i><p><b>Garantia de 15 dias.</b> Entre, use, conheça tudo. Se não for pra você, devolvemos 100%.</p></div>
      </div>
      <div class="warn rv d9-only"><b>Atenção:</b> os 6 anos de LOMBADA e os Playbooks são só para quem entrar hoje. A partir de amanhã, o LOMBADA volta a ser 3 anos e os bônus saem da oferta.</div>
    </div>
  </section>

  <!-- 7. o que você leva: o LOMBADA primeiro, em story, e depois cada produto -->
  <section class="sec leva">
    <div class="wrap">
      <div class="center rv"><p class="kick">Quem aproveitar essa oferta agora</p><h2 class="h2">Vai levar:</h2></div>
      <div class="lv lv--lmb rv" id="ferramenta">
        <span class="lv__k"><span class="d9-only">6 anos hoje</span><span class="after-only">3 anos</span></span>
        <h3 class="lv__lmb">{LMB}</h3>
        <p class="lv__big">A ferramenta que nunca deixa o seu livro parar.</p>
        <p class="lv__lead">Veja uma semana com ele.</p>
        <div class="wk" role="tablist" aria-label="Dias da semana">{STORY_TABS}</div>
        <div class="story" id="story">
          <div class="story__ph" role="button" tabindex="0" aria-label="Próximo dia">
            <div class="story__bars">{STORY_BARS}</div>
            <div class="story__scr">{STORY_IMGS}</div>
          </div>
          <div class="story__txt" aria-live="polite">{STORY_TXT}</div>
        </div>
        <p class="lv__mais">E ele ainda te dá:</p>
        <div class="tiles"><div class="tile rv"><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 7h8M8 11h8M8 15h5"/></svg></i><b>A página do seu livro</b><span>No ar, montada a partir do seu cadastro. Com 4 visuais para escolher.</span></div><div class="tile rv"><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21h18M5 21V8l7-5 7 5v13"/><path d="M9 21v-6h6v6"/></svg></i><b>O guia de fornecedores</b><span>Revisão, capa, diagramação e gráfica: quem a gente indica.</span></div><div class="tile rv"><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg></i><b>A agenda literária</b><span>Datas comemorativas e o calendário literário do ano inteiro.</span></div><div class="tile rv"><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12a8 8 0 0 1 14-5.3M20 12a8 8 0 0 1-14 5.3"/><path d="M18 3v4h-4M6 21v-4h4"/></svg></i><b>O plano se adapta a você</b><span>Não deu essa semana? Adie ou troque a tarefa. O ritmo é o seu.</span></div><div class="tile rv"><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="9" r="6"/><path d="M9 14.5 8 22l4-2 4 2-1-7.5"/></svg></i><b>Selos de evolução</b><span>Cada conquista do seu livro vira um selo.</span></div><div class="tile rv"><i><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></i><b>Travou? A equipe fica sabendo</b><span>Um toque em "Tive dificuldade" e a equipe te ajuda.</span></div></div>
        <div class="days"><p class="days__n gold" data-to-d9="2190" data-to-depois="1095">0</p><p class="days__a">manhãs. Nenhuma sem saber o que fazer pelo seu livro.</p></div>
      </div>
      <div class="leva__g">{LEVA}</div>
      <div class="cta leva__cta rv">{CTA}</div>
    </div>
  </section>

  <!-- 8. casos -->
  <section class="sec casos-sec">
    <div class="wrap">
      <div class="center rv"><h2 class="h2">A estratégia que mais transforma autores comuns em <span class="serif gold">best-sellers de verdade.</span></h2></div>
      <div class="casos">{CASOS}</div>
      <p class="casos__more rv">E muito mais.</p>
      <div class="cta leva__cta rv">{CTA}</div>
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
    </div>
  </section>

  <!-- 7. dúvidas -->
  <section class="sec faq">
    <div class="wrap">
      <div class="center rv"><p class="kick">Dúvidas</p><h2 class="h2">Antes de entrar.</h2></div>
      <div class="faq__l rv">
        <details><summary>“Não tenho tempo.”</summary><p>Uma ação por dia já conta. O LOMBADA monta o plano pelo tempo que você tem.</p></details>
        <details><summary>“Meu livro é antigo. Ou ainda estou escrevendo.”</summary><p>O plano começa pela fase em que o seu livro está. Livro antigo é o que mais ganha quando volta a aparecer.</p></details>
        <details><summary>“Posso parcelar?”</summary><p>Sim. Em até 12x de R$ 249,51, ou R$ 2.500 à vista.</p></details>
        <details><summary>“E se não for pra mim?”</summary><p>Você tem 15 dias. Não gostou, devolvemos tudo.</p></details>
      </div>
    </div>
  </section>

  <!-- 8. fecho -->
  <section class="sec end">
    <div class="wrap rv">
      <p class="kick">Black Week Motorizada</p>
      <p class="end__a">Essa é a sua <span class="serif gold">chance.</span></p>
      <p class="end__b">Tudo o que a Dany criou, pra sempre. E o LOMBADA ao lado do seu livro, todo dia.</p>
      <div class="cta">{CTA}<p class="fine">Garantia de 15 dias. Não gostou, devolvemos tudo.</p></div>
    </div>
  </section>
</main>

<footer>
  <p>© 2026 The Book Business. Todos os direitos reservados.</p>
  <p><a href="https://thebookbusiness.com.br/wp-content/uploads/2026/07/Politica-de-Privacidade_6514.pdf" target="_blank" rel="noopener">Política de Privacidade</a></p>
  <p class="legal"><b>Aviso Legal:</b> “Nenhuma informação contida neste site deve ser interpretada como uma afirmação de resultados ou de retornos financeiros. Qualquer referência a desempenho passado ou potencial é uma estratégia elaborada no contexto individual de cada autor, e não deve ser interpretada como recomendação ou garantia de resultados específicos.”</p>
</footer>

<div class="dock" id="dock"><a class="btn" href="#oferta" data-cta>Quero entrar na Black {SETA}</a></div>

<script>
(function () {{
  'use strict';
  var $$ = function (s) {{ return [].slice.call(document.querySelectorAll(s)); }};
  var q = new URLSearchParams(location.search);

  // modo: dia 9 até 23h59 de Brasília (02h59 UTC do dia 10); depois, LOMBADA 3 anos e sem bônus
  var FIM_D9 = Date.UTC(2026, 10, 10, 2, 59, 59);
  var modo = q.get('modo') || (Date.now() <= FIM_D9 ? 'd9' : 'depois');
  document.body.classList.add(modo === 'depois' ? 'm-depois' : 'm-d9');

  // checkout (Hotmart): o cliente manda os links. Repassa src/sck/utm até o checkout.
  var CHECKOUT = {{ d9: '', depois: '' }}, url = CHECKOUT[modo === 'depois' ? 'depois' : 'd9'];
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

  // entrada dos blocos: a pilha entra item por item
  if ('IntersectionObserver' in window) {{
    var io = new IntersectionObserver(function (es) {{ es.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }}); }}, {{ rootMargin: '0px 0px -10% 0px' }});
    $$('.rv').forEach(function (el) {{ io.observe(el); }});
  }} else $$('.rv').forEach(function (el) {{ el.classList.add('in'); }});

  // botão fixo no celular: aparece depois da abertura, some na oferta
  var dock = document.getElementById('dock'), passou = false, naOferta = false;
  function upd() {{ dock.classList.toggle('on', passou && !naOferta); }}
  if ('IntersectionObserver' in window) {{
    new IntersectionObserver(function (es) {{ passou = !es[0].isIntersecting && es[0].boundingClientRect.top < 0; upd(); }}).observe(document.querySelector('.price'));
    new IntersectionObserver(function (es) {{ naOferta = es[0].isIntersecting; upd(); }}).observe(document.getElementById('oferta'));
  }}
}})();
</script>
</body>
</html>
'''
open(f"{R}/black-week-oferta/index.html", "w", encoding="utf-8").write(HTML)
print("ok", len(HTML))
