# 01/11/2026 · Página de VENDA da Black Week Motorizada (oferta geral: Método The Book Business vitalício + LOMBADA).
# Parte da black-week/index.html (visual da Black + telas interativas do LOMBADA) e troca o conteúdo pela copy aprovada.
# Saída: black-week-oferta/index.html. Rodar: python3 _tools/gerar_black_venda.py
# Modo: até 23h59 de 9/11 (Brasília) = "dia 9" (LOMBADA 6 anos + bônus + contagem); depois = LOMBADA 3 anos, sem bônus.
# Prévia: ?modo=d9 ou ?modo=depois força o modo.
import os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(f"{R}/black-week/index.html", encoding="utf-8").read()

head, rest = src.split("</style>", 1)
script = rest[rest.index("<script>\n(function"):]

# caminhos: a página nova mora em outra pasta
head = head.replace('url("assets/', 'url("../black-week/assets/').replace('href="assets/', 'href="../black-week/assets/')
head = re.sub(r"<title>.*?</title>", "<title>Black Week Motorizada · Método The Book Business + LOMBADA</title>", head)
head = re.sub(r'<link rel="canonical"[^>]*>', '<link rel="canonical" href="https://metodo.thebookbusiness.com.br/black-week-oferta/">', head)
head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Método The Book Business vitalício + LOMBADA, o personal trainer do seu livro. Na Black Week Motorizada da Dany Sakugawa.">', head)
if 'name="robots"' not in head:
    head = head.replace('<meta name="theme-color"', '<meta name="robots" content="noindex, nofollow">\n<meta name="theme-color"', 1)

LMB = '<span class="lmb" role="img" aria-label="LOMBADA"><svg class="lmb-ic" viewBox="8 10 84 82" aria-hidden="true"><rect x="8" y="30" width="20" height="62" rx="3" fill="#14523e"/><rect x="30" y="16" width="22" height="76" rx="3" fill="#faab00"/><rect x="54" y="24" width="18" height="68" rx="3" fill="#b5402e"/><rect x="74" y="10" width="18" height="82" rx="3" fill="currentColor"/><rect x="12" y="78" width="12" height="3" fill="#f3f0e8" opacity=".85"/><rect x="12" y="84" width="12" height="3" fill="#f3f0e8" opacity=".85"/><rect x="34" y="78" width="14" height="3" fill="#fff" opacity=".85"/><rect x="34" y="84" width="14" height="3" fill="#fff" opacity=".85"/><circle cx="63" cy="36" r="4" fill="#f3f0e8"/><rect x="78" y="78" width="10" height="3" fill="#faab00"/><rect x="78" y="84" width="10" height="3" fill="#faab00"/></svg>LOMBADA</span>'
SETA = '<svg viewBox="0 0 30 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12h25M21 6l6 6-6 6"/></svg>'
CK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
CTA = f'<a class="btn" href="#oferta" data-cta>Quero entrar na Black {SETA}</a>'

# telas reais do LOMBADA (test drive, oportunidades, ideias de post, esteira) e o bloco da Dany: copiados da página original
body = src[src.index("<main>"):src.index("</main>")]
def bloco(ini, fim):
    a = body.index(ini); return body[a:body.index(fim, a)]
drive = bloco('<section class="blk drive"', '<!-- 4.')
motor = bloco('<section class="blk" id="mais-motor">', '<!-- 5.')
belt = bloco('<section class="blk" style="border-top', '<!-- 6.')
dany = bloco('<!-- 7. quem colocou o motor -->', '<!-- 8.')
dream = bloco('<section class="dream" id="reveal">', '<!-- 3.')
fix = lambda s: s.replace('src="assets/', 'src="../black-week/assets/')
drive, motor, belt, dany, dream = map(fix, (drive, motor, belt, dany, dream))
dream = dream.replace('<a class="dx__cue" href="#test-drive">Faça um test drive', '<a class="dx__cue" href="#test-drive">Veja por dentro')
drive = drive.replace('<p class="eyebrow">Test drive</p>', '<p class="eyebrow">Teste agora</p>')
belt = belt.replace('Saiba o que fazer, quando fazer, em cada etapa do seu livro.', 'Do primeiro livro ao décimo, o que fazer em cada etapa.')
dany = dany.replace('<p><b>Agora, colocou um motor nele.</b></p>', '<p><b>Depois, colocou o Método inteiro na palma da sua mão.</b></p>'.replace('o Método inteiro', 'o Método The&nbsp;Book&nbsp;Business inteiro'))

mis = open(f"{R}/black-week-misterio/index.html", encoding="utf-8").read()
casos = mis[mis.index('<div class="casos">'):mis.index('<!-- depois dos alunos')].replace('src="assets/casos/', 'src="../black-week-misterio/assets/casos/')
casos_css = "\n".join(l for l in mis.split("\n") if l.startswith((".casos", ".caso", ".rm .casos")) or l.startswith("  -webkit-mask-image: linear-gradient(90deg, transparent, #000 7%"))

CSS = casos_css + """
@keyframes belt { to { transform: translateX(-50%); } }

/* ===================== PÁGINA DE VENDA ===================== */
.gold { background: var(--gold); background-size: 220% 100%; -webkit-background-clip: text; background-clip: text; color: transparent; animation: gold 6s linear infinite; -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.rm .gold { animation: none; }
body:not(.m-d9) .d9-only, body:not(.m-depois) .after-only { display: none !important; }
.h1__b.vit { font-size: clamp(56px, 17vw, 112px); }
.h1-plus { margin-top: 10px; font-size: clamp(30px, 8.6vw, 52px); text-align: center; }
.h1-plus .lmb { color: var(--ink); }
.h1-plus small { display: block; margin-top: 10px; font: 500 clamp(13px, 3.6vw, 17px)/1.3 "Poppins", sans-serif; letter-spacing: .14em; text-transform: uppercase; color: var(--ink-2); }
/* faixa do dia 9: o dobro do LOMBADA + bônus + relógio */
.d9band { margin: 0 auto 14px; max-width: 440px; padding: 14px 16px; border-radius: 12px; text-align: center;
  background: rgba(250, 171, 0, .1); box-shadow: inset 0 0 0 1.5px rgba(250, 171, 0, .6); }
.d9band p { font-size: clamp(14px, 3.9vw, 16px); line-height: 1.4; color: var(--ink); text-wrap: balance; }
.d9band b { color: var(--amber); }
.clock { display: flex; justify-content: center; gap: 6px; margin-top: 10px; font-variant-numeric: tabular-nums; }
.clock span { min-width: 54px; padding: 6px 4px; border-radius: 8px; background: #000; box-shadow: inset 0 0 0 1px #3a362c; font-size: 22px; font-weight: 700; line-height: 1; }
.clock small { display: block; margin-top: 4px; font-size: 9px; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; color: var(--ink-3); }
.hero .cta-box { order: 1; width: 100%; max-width: 440px; margin: 26px auto 0; }
.cta-box .fine { margin-top: 10px; text-align: center; font-size: 13px; color: var(--ink-2); }
@media (min-width: 900px) { .hero .cta-box { max-width: 594px; } .hero .cta-box .btn { min-height: 61px; font-size: 23px; } }

/* esquecido aos poucos: o problema, frase a frase */
.slow { border-top: 1px solid var(--line); }
.slow__in { max-width: 680px; margin: 0 auto; text-align: center; }
.slow__big { font-size: clamp(28px, 8vw, 50px); font-weight: 600; line-height: 1.12; letter-spacing: -.02em; text-wrap: balance; }
.slow__big + .slow__big { margin-top: 6px; }
.slow__p { margin-top: 26px; font-size: clamp(17px, 4.7vw, 22px); line-height: 1.5; color: var(--ink-2); text-wrap: balance; }
.slow__p + .slow__p { margin-top: 6px; }
.slow__p b { color: var(--ink); font-weight: 600; }
.slow__lmb { margin-top: 30px; font-size: clamp(24px, 7vw, 40px); font-weight: 600; line-height: 1.2; }
.slow .lmb { color: var(--ink); }
.slow__pair { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 440px; margin: 32px auto 0; }
.slow__pair p { padding: 16px 10px; border-radius: 12px; background: var(--bg-2); box-shadow: inset 0 0 0 1px var(--line); font-size: clamp(15px, 4.2vw, 18px); font-weight: 600; }
.slow__pair p:last-child { box-shadow: inset 0 0 0 1.5px rgba(250, 171, 0, .6); color: var(--amber); }

/* o que tem dentro: papel do LOMBADA */
.inside { background: var(--app-paper); color: var(--app-ink); }
.inside .eyebrow { color: var(--app-ochre); }
.inside .eyebrow::before { background: var(--app-ochre); }
.inside .h2 .lmb { color: var(--app-ink); }
.inside__grid { display: grid; grid-template-columns: minmax(0, 1fr); gap: 12px; max-width: 980px; margin: 40px auto 0; list-style: none; }
@media (min-width: 700px) { .inside__grid { grid-template-columns: 1fr 1fr; } }
.inside__grid li { display: flex; gap: 14px; align-items: flex-start; padding: 18px; border-radius: 14px; background: #fff; box-shadow: 0 0 0 1px var(--app-line); }
.inside__grid i { flex: none; display: grid; place-items: center; width: 38px; height: 38px; border-radius: 10px; font-style: normal; font-size: 18px; }
.inside__grid li:nth-child(3n+1) i { background: #dff1e8; } .inside__grid li:nth-child(3n+2) i { background: #ffe5d8; } .inside__grid li:nth-child(3n) i { background: #fff1c7; }
.inside__grid b { display: block; font-size: 16px; font-weight: 700; line-height: 1.3; }
.inside__grid span { display: block; margin-top: 3px; font-size: 14px; line-height: 1.45; color: var(--app-soft); }
.inside__shot { max-width: 980px; margin: 36px auto 0; display: grid; grid-template-columns: minmax(0, 1fr); gap: 16px; align-items: center; }
.inside__end { margin-top: 40px; text-align: center; font-size: clamp(22px, 6vw, 34px); font-weight: 600; line-height: 1.2; text-wrap: balance; }
.inside__end span { display: block; color: var(--app-soft); font-weight: 500; font-size: .7em; margin-top: 6px; }

/* método */
.met__grid { display: grid; grid-template-columns: minmax(0, 1fr); gap: 12px; max-width: 760px; margin: 40px auto 0; }
@media (min-width: 700px) { .met__grid { grid-template-columns: 1fr 1fr; } }
.met__c { padding: 26px 22px; border-radius: 16px; background: var(--bg-2); box-shadow: inset 0 0 0 1px var(--line); text-align: left; }
.met__c .k { font-size: 11px; font-weight: 600; letter-spacing: .2em; text-transform: uppercase; color: var(--amber); }
.met__c .v { margin-top: 10px; font-size: clamp(26px, 7vw, 36px); font-weight: 700; line-height: 1.05; }
.met__c p { margin-top: 10px; font-size: 15px; line-height: 1.5; color: var(--ink-2); }

/* bônus do dia 9 */
.bonus { border-top: 1px solid var(--line); background: radial-gradient(ellipse 70% 60% at 50% 0%, rgba(250, 171, 0, .12), rgba(0, 0, 0, 0) 70%); }
.bonus__grid { display: grid; grid-template-columns: minmax(0, 1fr); gap: 14px; max-width: 860px; margin: 40px auto 0; }
@media (min-width: 760px) { .bonus__grid { grid-template-columns: 1fr 1fr; } }
.bon { position: relative; padding: 24px 22px; border-radius: 16px; background: #0d0c0e; box-shadow: inset 0 0 0 1.5px rgba(250, 171, 0, .45); text-align: left; }
.bon__tag { display: inline-block; padding: 5px 10px; border-radius: 99px; background: var(--amber); color: #111; font-size: 10px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.bon h3 { margin-top: 14px; font-size: clamp(20px, 5.4vw, 26px); font-weight: 700; line-height: 1.15; }
.bon p { margin-top: 10px; font-size: 15px; line-height: 1.5; color: var(--ink-2); }
.bon ul { margin-top: 12px; list-style: none; display: grid; gap: 8px; }
.bon li { display: flex; gap: 10px; align-items: center; font-size: 15px; font-weight: 500; }
.bon li::before { content: ""; flex: none; width: 7px; height: 7px; border-radius: 50%; background: var(--amber); }
.bonus__end { margin-top: 26px; text-align: center; font-size: 15px; font-weight: 600; color: var(--amber); }

/* casos */
.casos-sec { border-top: 1px solid var(--line); }

/* oferta */
.offer { border-top: 1px solid var(--line); padding: calc(var(--sec) + 10px) 0 var(--sec); }
.offer__card { position: relative; max-width: 560px; margin: 0 auto; padding: 34px 22px 26px; border-radius: 18px; background: #000; text-align: center;
  box-shadow: 0 0 0 1px rgba(250, 171, 0, .4), 0 0 44px rgba(250, 171, 0, .32); }
.offer__k { font-size: 11px; letter-spacing: .22em; text-transform: uppercase; color: var(--ink-2); }
.offer__t { margin-top: 12px; }
.offer__t .a { display: block; font-size: clamp(14px, 4vw, 18px); letter-spacing: .16em; text-transform: uppercase; }
.offer__t .b { display: block; margin-top: 2px; font-size: clamp(50px, 15vw, 80px); font-weight: 700; line-height: .95; letter-spacing: -.02em; }
.offer__t .c { display: block; margin-top: 10px; font-size: clamp(22px, 6vw, 30px); }
.offer__t .c .lmb { color: var(--ink); }
.offer__list { margin: 26px 0 0; list-style: none; display: grid; gap: 12px; text-align: left; }
.offer__list li { display: flex; gap: 12px; align-items: flex-start; font-size: clamp(15px, 4.1vw, 17px); line-height: 1.4; }
.offer__list li svg { flex: none; width: 22px; height: 22px; padding: 4px; margin-top: 1px; border-radius: 50%; background: var(--green); color: #fff; }
.offer__list b { font-weight: 700; }
.offer__list .x { color: var(--ink-3); font-size: .88em; }
.offer__price { margin-top: 28px; padding-top: 24px; border-top: 1px solid var(--line); }
.offer__price .pre { font-size: 15px; color: var(--ink-2); }
.offer__price .big { margin-top: 4px; font-size: clamp(46px, 13vw, 66px); font-weight: 700; line-height: 1; letter-spacing: -.02em; }
.offer__price .big small { font-size: .42em; font-weight: 600; letter-spacing: 0; }
.offer__price .cash { margin-top: 8px; font-size: 15px; color: var(--ink-2); }
.offer .btn { margin-top: 22px; gap: 8px; padding: 0 14px; font-size: clamp(15px, 4.5vw, 20px); }
.offer__safe { display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 16px; font-size: 13px; color: var(--ink-2); }
.offer__safe svg { flex: none; width: 26px; height: 26px; color: var(--amber); }
.offer .d9band { margin-top: 22px; margin-bottom: 0; }

/* dúvidas */
.faq { border-top: 1px solid var(--line); }
.faq__list { max-width: 720px; margin: 36px auto 0; }
.faq details { border-bottom: 1px solid var(--line); }
.faq summary { display: flex; justify-content: space-between; gap: 14px; padding: 20px 2px; cursor: pointer; list-style: none; font-size: clamp(16px, 4.4vw, 19px); font-weight: 600; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after { content: "+"; flex: none; color: var(--amber); font-size: 24px; line-height: 1; transition: transform .2s; }
.faq details[open] summary::after { transform: rotate(45deg); }
.faq details p { padding: 0 2px 20px; font-size: 16px; line-height: 1.55; color: var(--ink-2); }

/* fechamento */
.end { border-top: 1px solid var(--line); text-align: center; }
.end__a { font-size: clamp(20px, 5.6vw, 28px); color: var(--ink-2); line-height: 1.35; text-wrap: balance; }
.end__b { margin-top: 26px; font-size: clamp(36px, 10vw, 64px); font-weight: 700; line-height: 1.02; letter-spacing: -.02em; text-wrap: balance; }
.end__c { margin-top: 10px; font-size: clamp(16px, 4.5vw, 20px); color: var(--amber); }
.end .btn { max-width: 440px; margin-top: 30px; }
"""

MAIN = f"""<main>
  <!-- 1. abertura: a oferta inteira em uma tela -->
  <section class="hero" id="topo">
    <div class="wrap">
      <div class="hero__in">
        <div class="hero__main">
          <div class="proof"><img src="../black-week/assets/alunos.webp" alt="" width="118" height="26"><span><b>+4.400 autores</b> impactando vidas</span></div>
          {bloco('<div class="logo-box">', '<h1').strip().replace('src="assets/', 'src="../black-week/assets/')}
          <h1 class="h1"><span class="h1__a">Método The&nbsp;Book&nbsp;Business</span> <span class="h1__b vit">vitalício</span></h1>
          <p class="h1-plus">+ {LMB}<small>O personal trainer do seu livro</small></p>
          <div class="speak">
          <span class="dany-glow" aria-hidden="true"></span><img class="dany-m" src="../black-week/assets/dany-bw-m.webp" alt="Dany Sakugawa" width="408" height="378" decoding="async">
          <p class="pitch"><i>Seu livro <b class="amber">não vai parar</b>.<br><b>Todo dia, o que fazer.</b></i><span class="pitch__by">Dany Sakugawa</span></p>
          </div>
          <div class="cta-box">
            <div class="d9band d9-only"><p><b>Só hoje:</b> LOMBADA por <b>6 anos</b> (o dobro) + os bônus de quem esteve ao vivo.</p><div class="clock" data-clock></div></div>
            {CTA}
            <p class="fine">Garantia de 15 dias. Não gostou, devolvemos tudo.</p>
          </div>
        </div>
        <p class="dany-q"><i>“Eu queria que o autor abrisse a segunda-feira e já soubesse o que fazer pelo livro. Agora ele sabe, sempre.”</i><span>Dany Sakugawa</span></p>
        <img class="dany-d" src="../black-week/assets/dany-bw.webp" alt="Dany Sakugawa" width="840" height="1135" loading="lazy" decoding="async">
      </div>
    </div>
  </section>

  <!-- 2. o sonho: cada frase acende na rolagem e termina em "Agora existe." -->
  {dream}

  <!-- 2b. foi feito pra você -->
  <section class="blk slow">
    <div class="wrap">
      <div class="slow__in rv">
        <p class="slow__big">Isso foi feito <span class="gold">pra você.</span></p>
        <p class="slow__p">Todo dia o {LMB} abre com o próximo passo do seu livro. Montado pela fase dele, pelo gênero e pelo tempo que você tem.</p>
        <div class="slow__pair"><p>Ele monta o treino.</p><p>Você executa.</p></div>
        <p class="slow__p"><b>E o seu livro vai mais longe a cada dia.</b></p>
      </div>
    </div>
  </section>

  <!-- 3. telas reais do LOMBADA -->
  {drive}
  {motor}

  <!-- 4. o que tem dentro, no papel do LOMBADA -->
  <section class="blk inside">
    <div class="wrap">
      <div class="center rv">
        <p class="eyebrow">O que tem dentro</p>
        <h2 class="h2">Tudo o que o seu livro precisa, <span style="white-space:nowrap">em um lugar só.</span></h2>
      </div>
      <ul class="inside__grid rv">
        <li><i>📅</i><div><b>O plano do seu livro</b><span>As ações do dia, uma por vez.</span></div></li>
        <li><i>✍️</i><div><b>O texto pronto</b><span>Post, mensagem, ideia. Com o nome do seu livro.</span></div></li>
        <li><i>🎓</i><div><b>A aula por trás de cada ação</b><span>Você nunca faz sem entender por quê.</span></div></li>
        <li><i>🏆</i><div><b>As oportunidades</b><span>Prêmios, feiras e editais do seu gênero, com o prazo na tela.</span></div></li>
        <li><i>📖</i><div><b>A página do seu livro</b><span>No ar, nascida do seu cadastro.</span></div></li>
        <li><i>🤝</i><div><b>O guia de fornecedores</b><span>Revisão, capa, gráfica. Quem a gente indica.</span></div></li>
        <li><i>📓</i><div><b>O diário</b><span>A prova de que o seu livro não parou.</span></div></li>
        <li><i>💡</i><div><b>Ideias de post ilimitadas</b><span>Responda 3 perguntas e gere quantas quiser.</span></div></li>
      </ul>
      <p class="inside__end rv">Ele não faz por você.<span>Ele não deixa você parar.</span></p>
    </div>
  </section>

  {belt}

  <!-- 5. o Método The Book Business -->
  <section class="blk" style="border-top:1px solid var(--line)">
    <div class="wrap center">
      <div class="rv">
        <p class="eyebrow">E junto vem</p>
        <h2 class="h2">O Método The&nbsp;Book&nbsp;Business. <span class="gold">As aulas, pra sempre.</span></h2>
        <p class="lede">Do primeiro livro ao décimo. Da escrita ao lançamento, do lançamento à permanência.</p>
      </div>
      <div class="met__grid rv">
        <div class="met__c"><p class="k">Aulas</p><p class="v gold">Vitalício</p><p>Todo o Método The&nbsp;Book&nbsp;Business, para você voltar quantas vezes quiser, livro após livro.</p></div>
        <div class="met__c"><p class="k">Com a Dany</p><p class="v gold">3 anos</p><p>Encontros em grupo com a Dany Sakugawa durante 3 anos.</p></div>
      </div>
    </div>
  </section>

  <!-- 6. bônus de quem esteve ao vivo (só dia 9) -->
  <section class="blk bonus d9-only" id="bonus">
    <div class="wrap center">
      <div class="rv">
        <p class="eyebrow">Só para quem esteve ao vivo</p>
        <h2 class="h2">Os bônus <span class="gold">de hoje.</span></h2>
      </div>
      <div class="bonus__grid">
        <div class="bon rv"><span class="bon__tag">Bônus 1</span><h3>3 Playbooks MTBB físicos, entregues na sua casa</h3><p>A extensão prática do Método The&nbsp;Book&nbsp;Business, criada pela Dany. Pra anotar ideias, organizar estratégias e acompanhar a evolução do seu livro.</p></div>
        <div class="bon rv"><span class="bon__tag">Bônus 2</span><h3>Projetos Especiais</h3><ul><li>Autopublicação Profissional</li><li>Destaque Amazon</li><li>Editora Perfeita</li><li>Prêmio Jabuti</li></ul></div>
      </div>
      <p class="bonus__end rv">Esses bônus saem da página à meia-noite.</p>
    </div>
  </section>

  <!-- 7. casos -->
  <section class="blk casos-sec">
    <div class="wrap">
      <div class="center rv">
        <p class="eyebrow">Alunos do Método The&nbsp;Book&nbsp;Business</p>
        <h2 class="h2">O LOMBADA nasceu do Método. <span class="gold">Veja até onde ele já levou autores.</span></h2>
      </div>
    </div>
    {casos}
  </section>

  {dany}

  <!-- 8. a oferta -->
  <section class="offer" id="oferta">
    <div class="wrap">
      <div class="offer__card rv">
        <p class="offer__k">Na Black Week Motorizada</p>
        <h2 class="offer__t"><span class="a">Método The&nbsp;Book&nbsp;Business</span><span class="b gold">vitalício</span><span class="c">+ {LMB}</span></h2>
        <ul class="offer__list">
          <li>{CK}<span>Aulas do Método The&nbsp;Book&nbsp;Business, <b>acesso vitalício</b></span></li>
          <li>{CK}<span><b>Encontros em grupo</b> com a Dany por 3 anos</span></li>
          <li class="d9-only">{CK}<span>LOMBADA por <b>6 anos</b> <span class="x">(depois de hoje: 3 anos)</span></span></li>
          <li class="after-only">{CK}<span>LOMBADA por <b>3 anos</b></span></li>
          <li class="d9-only">{CK}<span><b>3 Playbooks MTBB físicos</b> + <b>Projetos Especiais</b> <span class="x">(só hoje)</span></span></li>
          <li>{CK}<span>Garantia de <b>15 dias</b></span></li>
        </ul>
        <div class="offer__price">
          <p class="pre">12x de</p>
          <p class="big"><small>R$</small>249,51</p>
          <p class="cash">ou R$2.500 à vista</p>
        </div>
        <div class="d9band d9-only"><p><b>O dobro do LOMBADA e os bônus</b> terminam à meia-noite.</p><div class="clock" data-clock></div></div>
        {CTA}
        <p class="offer__safe"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg><span>15 dias de garantia. Não gostou, devolvemos tudo.</span></p>
      </div>
    </div>
  </section>

  <!-- 9. dúvidas -->
  <section class="blk faq">
    <div class="wrap">
      <div class="center rv"><p class="eyebrow">Dúvidas</p><h2 class="h2">Antes de entrar.</h2></div>
      <div class="faq__list rv">
        <details><summary>“Não tenho tempo.”</summary><p>Uma ação por dia já conta. Você escolhe o ritmo, e o LOMBADA monta o plano pelo tempo que você tem.</p></details>
        <details><summary>“Não sou de rede social.”</summary><p>Boa parte do plano não é post: é livraria, leitor, evento, edital.</p></details>
        <details><summary>“Meu livro é antigo.”</summary><p>Livro antigo é o que mais precisa voltar a aparecer.</p></details>
        <details><summary>“Ainda estou escrevendo.”</summary><p>O plano começa pela fase em que o seu livro está.</p></details>
        <details><summary>“E se não for pra mim?”</summary><p>Você tem 15 dias. Não gostou, devolvemos tudo.</p></details>
      </div>
    </div>
  </section>

  <!-- 10. fechamento -->
  <section class="blk end">
    <div class="wrap rv">
      <p class="end__a">Lido. Desejado. Lembrado.<br><b style="color:var(--ink)">É possível. E começa hoje.</b></p>
      <p class="end__b">Seu livro <span class="gold">não vai parar.</span></p>
      <p class="end__c">Todo dia, o que fazer.</p>
      {CTA}
    </div>
  </section>
</main>
"""

FOOT = rest[rest.index("<footer>"):rest.index('<div class="dock"')].replace('src="assets/', 'src="../black-week/assets/')
DOCK = f'<div class="dock" id="dock"><a class="btn" href="#oferta" data-cta>Quero entrar na Black {SETA}</a></div>\n\n'

# JS: mantém utilidades + telas do LOMBADA + Dany; tira cadastro/abertura; põe modo do dia 9, relógio e botão fixo
js = script
a = js.index("  /* ================= 6b. DEPOIMENTOS"); b = js.index("  /* ================= 7. DANY NA MÍDIA")
js = js[:a] + js[b:]
a = js.index("  /* ================= ABERTURA")
js = js[:a] + """  /* ================= MODO: dia 9 (até 23h59 de Brasília = 02h59 UTC do dia 10) ou depois ================= */
  var FIM_D9 = Date.UTC(2026, 10, 10, 2, 59, 59), q = new URLSearchParams(location.search);
  var modo = q.get('modo') || (Date.now() <= FIM_D9 ? 'd9' : 'depois');
  document.body.classList.add(modo === 'depois' ? 'm-depois' : 'm-d9');
  // link do checkout (Hotmart) vem do cliente; ate lá os botões levam à oferta. Repassa src/sck/utm.
  var CHECKOUT = { d9: '', depois: '' }, url = CHECKOUT[modo === 'depois' ? 'depois' : 'd9'];
  if (url) {
    var KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'sck', 'src'], u = new URL(url);
    KEYS.forEach(function (k) { if (q.get(k)) u.searchParams.set(k, q.get(k)); });
    $$('[data-cta]').forEach(function (el) { el.href = u.toString(); });
  }
  // relógio até a meia-noite do dia 9 (na prévia antes do dia, conta até lá)
  var clocks = $$('[data-clock]');
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function tick() {
    var s = Math.max(0, Math.floor((FIM_D9 - Date.now()) / 1000)), h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), ss = s % 60;
    var html = (h >= 24 ? '<span>' + Math.floor(h / 24) + '<small>dias</small></span>' : '') + '<span>' + pad(h % 24) + '<small>horas</small></span><span>' + pad(m) + '<small>min</small></span><span>' + pad(ss) + '<small>seg</small></span>';
    clocks.forEach(function (c) { c.innerHTML = html; });
  }
  if (modo !== 'depois') { tick(); setInterval(tick, 1000); }

  /* ================= ENTRADA DOS BLOCOS ================= */
  reversivel($$('.rv'), 'in', '0px 0px -8% 0px');

  /* ================= BOTÃO FIXO (celular): some no topo e na oferta ================= */
  var dock = $('#dock'), seenTop = true, seenOffer = false;
  function dockUpdate() { dock.classList.toggle('on', !seenTop && !seenOffer); }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) { seenTop = es[0].isIntersecting || es[0].boundingClientRect.top > 0; dockUpdate(); }).observe($('.cta-box'));
    new IntersectionObserver(function (es) { seenOffer = es[0].isIntersecting; dockUpdate(); }).observe($('#oferta'));
  }
})();
</script>
</body>
</html>
"""
# o test drive mandava a fase/livro no cadastro: aqui não há cadastro
out = head + CSS + "</style>\n</head>\n<body class=\"no-js\">\n<script>document.body.classList.remove('no-js'); if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) document.body.classList.add('rm');</script>\n\n" \
      + '<div class="topbar">Black Week Motorizada · <b>a oferta está aberta</b></div>\n\n' + MAIN + "\n" + FOOT + DOCK + js
os.makedirs(f"{R}/black-week-oferta", exist_ok=True)
open(f"{R}/black-week-oferta/index.html", "w", encoding="utf-8").write(out)
print("ok", len(out))
