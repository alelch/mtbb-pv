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

HTML = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Black Week Motorizada · Tudo, pra sempre + LOMBADA</title>
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
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@1,6..72,500&display=swap" rel="stylesheet">
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
  --serif: "Newsreader", Georgia, serif;
}}
*, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
html {{ -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }}
body {{ background: var(--bg); color: var(--ink); font: 400 16px/1.5 "Poppins", system-ui, sans-serif; -webkit-font-smoothing: antialiased; overflow-x: clip; }}
img {{ display: block; max-width: 100%; height: auto; }}
a {{ color: inherit; }}
p, li, small {{ text-wrap: pretty; }}
.wrap {{ width: 100%; max-width: 1120px; margin: 0 auto; padding: 0 20px; }}
.gold {{ background: var(--gold); background-size: 220% 100%; -webkit-background-clip: text; background-clip: text; color: transparent; animation: gold 6s linear infinite; -webkit-box-decoration-break: clone; box-decoration-break: clone; }}
.serif {{ font-family: var(--serif); font-style: italic; font-weight: 500; letter-spacing: -.01em; text-transform: none; }}
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
.h {{ position: relative; min-height: calc(100svh - 52px); display: flex; align-items: center; overflow: hidden; isolation: isolate; padding: 40px 0 70px; text-align: center; }}
.h::before {{ content: ""; position: absolute; left: 50%; top: -60vmax; width: 160vmax; height: 160vmax; margin-left: -80vmax; z-index: -1; pointer-events: none;
  background: repeating-conic-gradient(from 0deg, rgba(250, 171, 0, .13) 0deg 5deg, transparent 5deg 18deg);
  -webkit-mask-image: radial-gradient(closest-side, #000 10%, transparent 70%); mask-image: radial-gradient(closest-side, #000 10%, transparent 70%); animation: rays 90s linear infinite; }}
.h::after {{ content: ""; position: absolute; left: 50%; top: 0; width: 120vmax; height: 70vmax; z-index: -1; transform: translate(-50%, -45%); border-radius: 50%; background: radial-gradient(closest-side, rgba(250, 171, 0, .22), transparent); pointer-events: none; }}
.h__in {{ width: 100%; }}
.h .bwlogo {{ font-size: clamp(30px, 8vw, 46px); animation: rise 1s var(--ease) both; }}
.h__kick {{ display: flex; justify-content: center; margin-top: 28px; animation: rise 1s var(--ease) .15s both; }}
.h__t {{ margin: 18px auto 0; max-width: 980px; animation: rise 1.1s var(--ease) .25s both; }}
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
  <!-- 1. abertura -->
  <section class="h" id="topo">
    <div class="wrap h__in">
      {BWLOGO}
      <p class="kick h__kick">Inscrições liberadas</p>
      <h1 class="h__t"><span class="h__a">Tudo o que a Dany criou para autores.</span><span class="h__b serif gold">Pra sempre.</span></h1>
      <p class="h__plus">E, pela primeira vez, o {LMB} ao seu lado todo dia.</p>
      <p class="h__price"><span>12x de</span><b>R$249,51</b></p>
      <div class="cta">{CTA}<p class="fine">Garantia de 15 dias. Não gostou, devolvemos tudo.</p></div>
      <a class="h__cue" href="#tudo">Veja tudo o que entra<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg></a>
    </div>
  </section>

  <!-- 2. a pilha: tudo o que entra -->
  <section class="sec pile" id="tudo">
    <div class="wrap">
      <div class="center rv">
        <p class="kick">Na Black Week Motorizada</p>
        <h2 class="h2">Olha tudo o que <span class="serif gold">entra.</span></h2>
        <p class="pile__lede">Nada fica de fora. Cada produto, cada workshop, cada projeto especial. E o LOMBADA.</p>
      </div>
      <ol class="rows">
{rows}
      </ol>
      <div class="total rv">
        <p class="total__n gold"><span class="after-only">{N}</span><span class="d9-only">{N+1}</span></p>
        <p class="total__a">entregas para o seu livro ir mais longe.</p>
        <p class="total__b serif gold">Um preço só.</p>
        <div class="cta">{CTA}</div>
      </div>
    </div>
  </section>

  <!-- 3. o LOMBADA, em telas reais -->
  <section class="sec lmbs">
    <div class="wrap center">
      <div class="rv">
        <p class="kick">A grande novidade</p>
        <p class="lmbs__mark">{LMB}</p>
        <p class="lmbs__p">Todo dia ele abre com o próximo passo do seu livro. Montado pela fase, pelo gênero e pelo tempo que você tem.</p>
        <div class="lmbs__pair"><span>Ele monta o treino.</span><span>Você executa.</span></div>
      </div>
    </div>
    <div class="telas">
{telas}
    </div>
    <p class="lmbs__swipe">Deslize para ver mais →</p>
    <p class="lmbs__note">Telas reais do LOMBADA, com um livro de exemplo.</p>
  </section>

  <!-- 4. bônus de hoje (só dia 9) -->
  <section class="sec d9 d9-only" id="hoje">
    <div class="wrap center">
      <div class="rv">
        <p class="kick">Só para quem entrar hoje</p>
        <p class="d9__big gold">6 anos</p>
        <p class="d9__sub">de LOMBADA. O dobro.</p>
        <p class="d9__p">Amanhã volta a ser 3. Quem entra hoje leva o LOMBADA ao lado do seu livro por 6 anos.</p>
      </div>
      <p class="d9__plus rv">+</p>
      <div class="d9__pb rv">
        <img src="assets/playbooks.webp" alt="Playbooks MTBB" width="475" height="592" loading="lazy" decoding="async">
        <div>
          <h3>Playbooks MTBB físicos, entregues na sua casa.</h3>
          <p>A extensão prática do Método The&nbsp;Book&nbsp;Business, criada pessoalmente pela Dany. Pra anotar ideias, organizar estratégias e acompanhar a evolução do seu livro.</p>
          <ul><li>Fundamentos</li><li>Método</li><li>Ativações</li></ul>
        </div>
      </div>
      <div class="d9__end rv"><p>Termina à meia-noite</p>{CLOCK}</div>
    </div>
  </section>

  <!-- 5. Dany -->
  <section class="sec dany">
    <div class="wrap">
      <div class="dany__g">
        <figure class="dany__pic rv"><img src="../black-week/assets/dany-palco.webp" alt="Dany Sakugawa" width="680" height="1207" loading="lazy" decoding="async"></figure>
        <div class="rv">
          <p class="kick">Uma carta da Dany</p>
          <h2 class="dany__h">Isso foi feito <span class="serif gold">pra você.</span></h2>
          <div class="dany__l">
            <p><b>Meu sonho sempre foi que o autor acordasse todo dia sabendo o que fazer pelo livro.</b></p>
            <p>Por isso criei o Método The&nbsp;Book&nbsp;Business: tudo o que aprendi em 15 anos nos bastidores das editoras, organizado para o autor.</p>
            <p>Mas eu queria ir além. Queria estar ao lado de cada aluno, todo dia, dizendo o que fazer, quando e por quê.</p>
            <p><b>Foi assim que nasceu o LOMBADA.</b> E agora ele pode ser seu.</p>
          </div>
          <p class="dany__sig serif">Dany Sakugawa</p>
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

  <!-- 6. a oferta -->
  <section class="sec offer" id="oferta">
    <div class="wrap">
      <div class="card rv">
        {BWLOGO}
        <h2 class="card__t">Tudo o que a Dany criou. <span class="serif gold">Pra sempre.</span><span class="lmb-row">+ {LMB}</span></h2>
        <ul class="card__list">
          <li>{CK}<span><b>Método The&nbsp;Book&nbsp;Business</b> e todos os produtos, workshops e Projetos Especiais, <b>vitalícios</b></span></li>
          <li>{CK}<span>Gravação de <b>100% das lives</b>, encontros e eventos</span></li>
          <li>{CK}<span><b>Encontros em grupo</b> ao vivo com a Dany por 3 anos</span></li>
          <li>{CK}<span><b>LOMBADA</b> por <b class="d9-only">6 anos</b><b class="after-only">3 anos</b></span></li>
          <li class="d9-only">{CK}<span><b>Playbooks MTBB físicos</b> na sua casa</span></li>
          <li>{CK}<span>Garantia de <b>15 dias</b></span></li>
        </ul>
        <div class="card__price">
          <p class="pre">Tudo isso por 12x de</p>
          <p class="big"><small>R$</small>249,51</p>
          <p class="cash">ou R$2.500 à vista</p>
        </div>
        <div class="card__clock d9-only"><p><b>6 anos de LOMBADA e os Playbooks</b> terminam à meia-noite.</p>{CLOCK}</div>
        {CTA}
        <div class="seal"><i>15<small>dias</small></i><p><b>Garantia de 15 dias.</b> Entre, use, conheça tudo. Se não for pra você, devolvemos 100% em até 15 dias.</p></div>
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

  // entrada dos blocos: a pilha entra item por item
  if ('IntersectionObserver' in window) {{
    var io = new IntersectionObserver(function (es) {{ es.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }}); }}, {{ rootMargin: '0px 0px -10% 0px' }});
    $$('.rv').forEach(function (el) {{ io.observe(el); }});
  }} else $$('.rv').forEach(function (el) {{ el.classList.add('in'); }});

  // botão fixo no celular: aparece depois da abertura, some na oferta
  var dock = document.getElementById('dock'), passou = false, naOferta = false;
  function upd() {{ dock.classList.toggle('on', passou && !naOferta); }}
  if ('IntersectionObserver' in window) {{
    new IntersectionObserver(function (es) {{ passou = !es[0].isIntersecting && es[0].boundingClientRect.top < 0; upd(); }}).observe(document.querySelector('.h .cta'));
    new IntersectionObserver(function (es) {{ naOferta = es[0].isIntersecting; upd(); }}).observe(document.getElementById('oferta'));
  }}
}})();
</script>
</body>
</html>
'''
open(f"{R}/black-week-oferta/index.html", "w", encoding="utf-8").write(HTML)
print("ok", len(HTML))
