# -*- coding: utf-8 -*-
"""
Per-page content for the 6 MTBB sales pages.
Edit copy HERE, then run:  python3 build/generate.py

Each page maps slug -> dict of token values.
"variant" picks the template (template-preco.html / template-lista.html).
HTML-fragment tokens use triple-quoted strings.
"""

PAGES = {
    'publicado': {
        "variant": 'preco',
        "STAGE_SLUG": 'publicado',
        "SEO_HEAD": """<title>MTBB · Faça seu livro voltar a ser lido</title>
<meta name="description" content="Seu livro foi lançado, mas precisa voltar a ser lido. O método de Dany Sakugawa pra reativar livros que pararam de circular. Testado em 800 lançamentos.">
<meta property="og:type" content="website">
<meta property="og:title" content="MTBB · Faça seu livro voltar a ser lido">
<meta property="og:description" content="Seu livro foi lançado, mas precisa voltar a ser lido. O método de Dany Sakugawa pra reativar livros que pararam de circular. Testado em 800 lançamentos.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="MTBB · Faça seu livro voltar a ser lido">
<meta name="twitter:description" content="Seu livro foi lançado, mas precisa voltar a ser lido. O método de Dany Sakugawa pra reativar livros que pararam de circular. Testado em 800 lançamentos.">
<link rel="canonical" href="https://metodo.thebookbusiness.com.br/publicado">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Dany Sakugawa">
<meta property="og:url" content="https://metodo.thebookbusiness.com.br/publicado">""",
        "LDJSON": """{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://metodo.thebookbusiness.com.br/#org","name":"The Book Business","url":"https://thebookbusiness.com.br","logo":"https://metodo.thebookbusiness.com.br/assets/og-mtbb.jpg","sameAs":["https://www.instagram.com/dany.sakugawa"],"founder":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}},{"@type":"Person","@id":"https://metodo.thebookbusiness.com.br/#dany","name":"Dany Sakugawa","jobTitle":"Especialista em marketing literário","image":"https://metodo.thebookbusiness.com.br/assets/dany-sakugawa.webp","worksFor":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"sameAs":["https://www.instagram.com/dany.sakugawa"]},{"@type":"WebSite","@id":"https://metodo.thebookbusiness.com.br/#website","url":"https://metodo.thebookbusiness.com.br/","name":"Método The Book Business","inLanguage":"pt-BR","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"Course","@id":"https://metodo.thebookbusiness.com.br/publicado#course","name":"Método The Book Business (MTBB)","description":"Seu livro foi lançado, mas precisa voltar a ser lido. O método de Dany Sakugawa pra reativar livros que pararam de circular. Testado em 800 lançamentos.","inLanguage":"pt-BR","provider":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"hasCourseInstance":{"@type":"CourseInstance","courseMode":"Online","instructor":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}},"offers":{"@type":"Offer","price":"2500.00","priceCurrency":"BRL","availability":"https://schema.org/InStock","url":"https://metodo.thebookbusiness.com.br/publicado"}},{"@type":"VideoObject","name":"Aula gratuita — Método The Book Business","description":"Seu livro foi lançado, mas precisa voltar a ser lido. O método de Dany Sakugawa pra reativar livros que pararam de circular. Testado em 800 lançamentos.","thumbnailUrl":["https://metodo.thebookbusiness.com.br/assets/aula-metodo-the-book-business.webp"],"uploadDate":"2025-01-15","contentUrl":"https://cdn.converteai.net/6b353be1-c671-4a98-af52-02bc731efaae/6a47c99aa63e151eb8ef0c44/main.m3u8","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"FAQPage","@id":"https://metodo.thebookbusiness.com.br/publicado#faq","mainEntity":[{"@type":"Question","name":"Meu livro foi lançado há tempos. Ainda dá pra recuperar?","acceptedAnswer":{"@type":"Answer","text":"Sim. Boa parte dos alunos chegam exatamente nessa situação. O método identifica o que não foi feito e começa a preencher essas lacunas. O mercado está cheio de livros que só começaram a vender de verdade dois ou três anos depois do lançamento, quando o autor encontrou a estratégia certa."}},{"@type":"Question","name":"O lançamento foi fraco. O método consegue reverter?","acceptedAnswer":{"@type":"Answer","text":"Reverter, sim. Mas não com truque. O método trata o livro como ele é hoje: um livro lançado que ainda não encontrou seus leitores certos. A partir daí, reconstrói posicionamento, ativa canais que ficaram parados e cria os pontos de contato que faltaram. Lançamento é um momento. A construção do livro como negócio é contínua."}},{"@type":"Question","name":"R$ 249 é muito. Como sei que vai valer?","acceptedAnswer":{"@type":"Answer","text":"Quanto custa uma capa mal feita? Quanto custa um lançamento sem cronograma que vende só para amigos e família? Quanto custa mais um ano com o livro encalhado? O método tem garantia de 15 dias: se não estiver satisfeito, devolvemos sem perguntas."}},{"@type":"Question","name":"Já tentei divulgar antes e não funcionou. Por que seria diferente agora?","acceptedAnswer":{"@type":"Answer","text":"Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade."}},{"@type":"Question","name":"Não tenho seguidores. Funciona pra mim?","acceptedAnswer":{"@type":"Answer","text":"Funciona, e talvez melhor. Seguidor nunca foi o objetivo, leitor é. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram audiência certa, não audiência grande. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida."}},{"@type":"Question","name":"Preciso de editora para o método funcionar?","acceptedAnswer":{"@type":"Answer","text":"Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora."}},{"@type":"Question","name":"Quanto tempo por semana eu preciso dedicar?","acceptedAnswer":{"@type":"Answer","text":"Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim."}},{"@type":"Question","name":"Minha editora já cuida do marketing. Ainda faz sentido?","acceptedAnswer":{"@type":"Answer","text":"Sim, e talvez mais do que para quem é independente. A maioria das editoras faz o lançamento e segue em frente. Quem sustenta o livro vendendo nos meses seguintes é o autor. O método te dá autonomia para não depender do ciclo da editora."}}]}]}""",
        "HERO_BADGE_H1": """    <div class="hero-badge">Para autores com livro lançado</div>
    <h1>Seu livro já foi lançado.<br><span class="hero-italic" style="font-family:'Poppins',sans-serif; font-style:normal; font-weight:700;"><span class="hl-grifo">Os próximos passos</span> decidem se ele será lido… ou <span class="hl-risco">esquecido</span>.</span></h1>""",
        "HERO_WATCH": """Assista à aula abaixo e veja como ser lido de verdade.""",
        "CTA_POSVIDEO": """Seu livro merece ser lido.""",
        "AGITATION_BLOCK": """
<!-- BLOCO 5 — AGITAÇÃO -->
<section class="agitation">
  <div class="container">
    <h2>Você pode ter lançado um livro <span class="hl-grifo">incrível</span>.</h2>
    <p class="agi-sub">E ainda assim ele parar de <span class="hl-risco">ser lido</span>.</p>
    <p class="agitation-quote"><span class="hw-line">Ninguém lê um livro</span><span class="hw-line">que ninguém lembra.</span></p>
    <p class="agitation-closing">Esperança não muda isso.<br><span class="italic">Estratégia sim.</span></p>
  </div>
</section>

<!-- TESE — citação (blockquote) -->
<section class="tese-faixa">
  <figure class="tese-quote">
    <blockquote>
      <span class="l1"><span class="qm">&ldquo;</span>Seu livro não precisa nascer de novo.</span>
      <span class="l2">Precisa voltar a ser encontrado.</span>
    </blockquote>
    <cite>Dany Sakugawa</cite>
  </figure>
</section>

""",
        "JOURNEY_TITLE": """Do livro lançado ao livro lido de verdade""",
        "JOURNEY_STEPS": """      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">1</span></div>
        <div class="journey-step-marker" aria-hidden="true">Você está aqui.
          <svg class="arrow" viewBox="0 0 72 44" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6,6 Q20,2 38,16 Q54,26 64,38" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/>
            <path d="M52,34 L66,40 L60,28" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="card">
          <h3 class="card__title"><span>Parar de aceitar que o livro perdeu força</span></h3>
          <div class="card__body"><div><p class="card__desc">Livro publicado. Lançamento já passou. E a sensação incômoda de que ele parou antes de encontrar quem precisava ler.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">2</span></div>
        <div class="card">
          <h3 class="card__title"><span>Diagnosticar o livro na Matriz do Autor Estratégico</span></h3>
          <div class="card__body"><div><p class="card__desc">Ver com clareza por que ele parou de circular: onde está forte, onde está vulnerável, e o que ainda precisa de ajuste.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">3</span></div>
        <div class="card">
          <h3 class="card__title"><span>Reencontrar o leitor certo</span></h3>
          <div class="card__body"><div><p class="card__desc">E onde ele está hoje. Sem postar em grupo aleatório. Sem implorar para influenciador. Sem chutar. É descobrir quem ainda vai desejar, comprar e recomendar.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">4</span></div>
        <div class="card">
          <h3 class="card__title"><span>Montar o plano de reativação do livro</span></h3>
          <div class="card__body"><div><p class="card__desc">Um plano claro do que fazer pra colocar o livro de volta na rua. Sem improviso. Sem pular etapa.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">5</span></div>
        <div class="card">
          <h3 class="card__title"><span>Reativar demanda em ciclos curtos</span></h3>
          <div class="card__body"><div><p class="card__desc">Cada ciclo tem começo, meio e fim. Cada um gera tração. E a tração não some, acumula.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">6</span></div>
        <div class="card">
          <h3 class="card__title"><span>Fazer o livro voltar a circular</span></h3>
          <div class="card__body"><div><p class="card__desc">Sem silêncio. Sem improviso. Com plano, com demanda, com estratégia.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">7</span></div>
        <div class="card">
          <h3 class="card__title"><span>Sustentar o livro vivo no longo prazo</span></h3>
          <div class="card__body"><div><p class="card__desc">O trabalho do autor nunca termina no lançamento. Continua aqui. Sem isso, o livro volta a apagar.</p></div></div>
        </div>
      </li>""",
        "PC_TEXT": """Você lançou seu livro.<br>Se sozinho não foi o suficiente, <em class="hl-risco">e agora?</em>""",
        "MENTORIA": """Você valida cada decisão (reativar o livro, ajustar posicionamento ou planejar o próximo) com quem já guiou 800 lançamentos.""",
        "GARANTIA_CLOSE": """          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</section>

""",
        "FAQ_LIST": """      <details class="faq-item">
        <summary>Meu livro foi lançado há tempos. Ainda dá pra recuperar?</summary>
        <div class="answer">Sim. Boa parte dos alunos chegam exatamente nessa situação. O método identifica o que não foi feito e começa a preencher essas lacunas. O mercado está cheio de livros que só começaram a vender de verdade dois ou três anos depois do lançamento, quando o autor encontrou a estratégia certa.</div>
      </details>
      <details class="faq-item">
        <summary>O lançamento foi fraco. O método consegue reverter?</summary>
        <div class="answer">Reverter, sim. Mas não com truque. O método trata o livro como ele é hoje: um livro lançado que ainda não encontrou seus leitores certos. A partir daí, reconstrói posicionamento, ativa canais que ficaram parados e cria os pontos de contato que faltaram. Lançamento é um momento. A construção do livro como negócio é contínua.</div>
      </details>
      <details class="faq-item">
        <summary>R$ 249 é muito. Como sei que vai valer?</summary>
        <div class="answer">Quanto custa uma capa mal feita? Quanto custa um lançamento sem cronograma que vende só para amigos e família? Quanto custa mais um ano com o livro encalhado? O método tem garantia de 15 dias: se não estiver satisfeito, devolvemos sem perguntas.</div>
      </details>
      <details class="faq-item">
        <summary>Já tentei divulgar antes e não funcionou. Por que seria diferente agora?</summary>
        <div class="answer">Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade.</div>
      </details>
      <details class="faq-item">
        <summary>Não tenho seguidores. Funciona pra mim?</summary>
        <div class="answer">Funciona, e talvez melhor. Seguidor nunca foi o objetivo, <strong>leitor é</strong>. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram <strong>audiência certa, não audiência grande</strong>. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida.</div>
      </details>
      <details class="faq-item">
        <summary>Preciso de editora para o método funcionar?</summary>
        <div class="answer">Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora.</div>
      </details>
      <details class="faq-item">
        <summary>Quanto tempo por semana eu preciso dedicar?</summary>
        <div class="answer">Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim.</div>
      </details>
      <details class="faq-item">
        <summary>Minha editora já cuida do marketing. Ainda faz sentido?</summary>
        <div class="answer">Sim, e talvez mais do que para quem é independente. A maioria das editoras faz o lançamento e segue em frente. Quem sustenta o livro vendendo nos meses seguintes é o autor. O método te dá autonomia para não depender do ciclo da editora.</div>
      </details>""",
        "FINAL_CTA": """<h2>Você foi longe demais<br><span class="italic">pra ver o livro parar.</span></h2>
    <p style="font-size:17px; color:rgba(255,255,255,0.65); line-height:1.6; max-width:480px; margin:0 auto 36px;">O método está aqui. O livro está lançado. O único passo que falta é o seu.</p>""",
    },
    'escrevendo': {
        "variant": 'preco',
        "STAGE_SLUG": 'escrevendo',
        "SEO_HEAD": """<title>MTBB · Construa leitores enquanto escreve seu livro</title>
<meta name="description" content="Você está escrevendo. Os leitores podem já estar esperando. O método de Dany Sakugawa pra construir leitores enquanto se escreve. Testado em 800 lançamentos.">
<meta property="og:type" content="website">
<meta property="og:title" content="MTBB · Construa leitores enquanto escreve seu livro">
<meta property="og:description" content="Você está escrevendo. Os leitores podem já estar esperando. O método de Dany Sakugawa pra construir leitores enquanto se escreve. Testado em 800 lançamentos.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="MTBB · Construa leitores enquanto escreve seu livro">
<meta name="twitter:description" content="Você está escrevendo. Os leitores podem já estar esperando. O método de Dany Sakugawa pra construir leitores enquanto se escreve. Testado em 800 lançamentos.">
<link rel="canonical" href="https://metodo.thebookbusiness.com.br/escrevendo">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Dany Sakugawa">
<meta property="og:url" content="https://metodo.thebookbusiness.com.br/escrevendo">""",
        "LDJSON": """{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://metodo.thebookbusiness.com.br/#org","name":"The Book Business","url":"https://thebookbusiness.com.br","logo":"https://metodo.thebookbusiness.com.br/assets/og-mtbb.jpg","sameAs":["https://www.instagram.com/dany.sakugawa"],"founder":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}},{"@type":"Person","@id":"https://metodo.thebookbusiness.com.br/#dany","name":"Dany Sakugawa","jobTitle":"Especialista em marketing literário","image":"https://metodo.thebookbusiness.com.br/assets/dany-sakugawa.webp","worksFor":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"sameAs":["https://www.instagram.com/dany.sakugawa"]},{"@type":"WebSite","@id":"https://metodo.thebookbusiness.com.br/#website","url":"https://metodo.thebookbusiness.com.br/","name":"Método The Book Business","inLanguage":"pt-BR","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"Course","@id":"https://metodo.thebookbusiness.com.br/escrevendo#course","name":"Método The Book Business (MTBB)","description":"Você está escrevendo. Os leitores podem já estar esperando. O método de Dany Sakugawa pra construir leitores enquanto se escreve. Testado em 800 lançamentos.","inLanguage":"pt-BR","provider":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"hasCourseInstance":{"@type":"CourseInstance","courseMode":"Online","instructor":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}},"offers":{"@type":"Offer","price":"2500.00","priceCurrency":"BRL","availability":"https://schema.org/InStock","url":"https://metodo.thebookbusiness.com.br/escrevendo"}},{"@type":"VideoObject","name":"Aula gratuita — Método The Book Business","description":"Você está escrevendo. Os leitores podem já estar esperando. O método de Dany Sakugawa pra construir leitores enquanto se escreve. Testado em 800 lançamentos.","thumbnailUrl":["https://metodo.thebookbusiness.com.br/assets/aula-metodo-the-book-business.webp"],"uploadDate":"2025-01-15","contentUrl":"https://cdn.converteai.net/6b353be1-c671-4a98-af52-02bc731efaae/6a47c99aa63e151eb8ef0c44/main.m3u8","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"FAQPage","@id":"https://metodo.thebookbusiness.com.br/escrevendo#faq","mainEntity":[{"@type":"Question","name":"Ainda não terminei o livro. É cedo demais pra entrar?","acceptedAnswer":{"@type":"Answer","text":"Pelo contrário. Esse é o momento ideal. Quando o livro fica pronto, a estratégia precisa estar pronta também. Começar agora significa chegar no lançamento com leitores esperando, posicionamento testado e canais funcionando. Quem deixa pra começar depois do livro pronto sempre corre atrás do prejuízo."}},{"@type":"Question","name":"Vou conseguir escrever e construir audiência ao mesmo tempo?","acceptedAnswer":{"@type":"Answer","text":"Sim, porque o método foi construído pra isso. Entre 1 e 3 horas por semana de trabalho estratégico, em paralelo à escrita. A maioria dos alunos relata que a clareza sobre o leitor melhora até o próprio processo criativo. Estratégia não rouba tempo da escrita. Dá direção pra ela."}},{"@type":"Question","name":"R$ 249 é muito. Como sei que vai valer?","acceptedAnswer":{"@type":"Answer","text":"Quanto custa uma capa mal feita? Quanto custa um lançamento sem cronograma que vende só para amigos e família? Quanto custa mais um ano com o livro encalhado? O método tem garantia de 15 dias: se não estiver satisfeito, devolvemos sem perguntas."}},{"@type":"Question","name":"Já tentei divulgar antes e não funcionou. Por que seria diferente agora?","acceptedAnswer":{"@type":"Answer","text":"Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade."}},{"@type":"Question","name":"Não tenho seguidores. Funciona pra mim?","acceptedAnswer":{"@type":"Answer","text":"Funciona, e talvez melhor. Seguidor nunca foi o objetivo, leitor é. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram audiência certa, não audiência grande. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida."}},{"@type":"Question","name":"Preciso de editora para o método funcionar?","acceptedAnswer":{"@type":"Answer","text":"Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora."}},{"@type":"Question","name":"Quanto tempo por semana eu preciso dedicar?","acceptedAnswer":{"@type":"Answer","text":"Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim."}},{"@type":"Question","name":"Devo procurar editora ou autopublicar? O método me ajuda nisso?","acceptedAnswer":{"@type":"Answer","text":"Ajuda. O método te dá os critérios pra escolher o caminho com clareza, não por insegurança. Editora não é prêmio nem solução automática. É uma das vias possíveis. Os bastidores editoriais que a Dany compartilha mostram o que cada modelo entrega de fato, e o que sempre fica nas mãos do autor."}}]}]}""",
        "HERO_BADGE_H1": """    <div class="hero-badge">Para autores escrevendo</div>
    <h1>Você está escrevendo seu livro.<br><span class="hero-italic" style="font-family:'Poppins',sans-serif; font-style:normal; font-weight:700;"><span class="hl-grifo">Os próximos passos</span> decidem se ele será lido… ou <span class="hl-risco">esquecido</span>.</span></h1>""",
        "HERO_WATCH": """Assista à aula abaixo e veja como atrair seus leitores.""",
        "CTA_POSVIDEO": """Seu livro merece ser lido.""",
        "AGITATION_BLOCK": """
<!-- BLOCO 5 — AGITAÇÃO -->
<section class="agitation">
  <div class="container">
    <h2>Você pode estar escrevendo um livro <span class="hl-grifo">incrível</span>.</h2>
    <p class="agi-sub">E ainda assim terminar sem <span class="hl-risco">leitores esperando</span>.</p>
    <p class="agitation-quote"><span class="hw-line">Ninguém compra um livro</span><span class="hw-line">que não conhece.</span></p>
    <p class="agitation-closing">Esperança não muda isso.<br><span class="italic">Estratégia sim.</span></p>
  </div>
</section>

<!-- TESE — citação (blockquote) -->
<section class="tese-faixa">
  <figure class="tese-quote">
    <blockquote>
      <span class="l1"><span class="qm">&ldquo;</span>O lançamento não começa quando o livro fica pronto.</span>
      <span class="l2">Começa nas decisões que você toma enquanto escreve.</span>
    </blockquote>
    <cite>Dany Sakugawa</cite>
  </figure>
</section>

""",
        "JOURNEY_TITLE": """Da escrita estratégica ao livro lido""",
        "JOURNEY_STEPS": """      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">1</span></div>
        <div class="journey-step-marker" aria-hidden="true">Você está aqui.
          <svg class="arrow" viewBox="0 0 72 44" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6,6 Q20,2 38,16 Q54,26 64,38" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/>
            <path d="M52,34 L66,40 L60,28" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="card">
          <h3 class="card__title"><span>Parar de escrever sem pensar no leitor</span></h3>
          <div class="card__body"><div><p class="card__desc">Capítulos avançando. Vontade enorme. E a sensação incômoda de que ninguém estará esperando quando o livro ficar pronto.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">2</span></div>
        <div class="card">
          <h3 class="card__title"><span>Diagnosticar a ideia do livro na Matriz do Autor Estratégico</span></h3>
          <div class="card__body"><div><p class="card__desc">Antes de seguir escrevendo, ver com clareza onde o projeto está forte, onde está vulnerável, e o que ainda precisa de ajuste.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">3</span></div>
        <div class="card">
          <h3 class="card__title"><span>Encontrar o leitor certo desde já</span></h3>
          <div class="card__body"><div><p class="card__desc">E onde ele está. Sem postar em grupo aleatório. Sem implorar para influenciador. Sem chutar. É descobrir quem vai desejar, comprar e recomendar.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">4</span></div>
        <div class="card">
          <h3 class="card__title"><span>Montar o cronograma estratégico do livro</span></h3>
          <div class="card__body"><div><p class="card__desc">Um plano claro do que fazer enquanto escreve, antes de publicar, e depois do livro sair. Sem improviso. Sem pular etapa.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">5</span></div>
        <div class="card">
          <h3 class="card__title"><span>Construir audiência enquanto o livro nasce</span></h3>
          <div class="card__body"><div><p class="card__desc">Ciclos curtos de presença com começo, meio e fim. Cada um gera tração. E a tração não some, acumula.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">6</span></div>
        <div class="card">
          <h3 class="card__title"><span>Lançar com leitores esperando</span></h3>
          <div class="card__body"><div><p class="card__desc">Sem silêncio. Sem improviso. Com plano, com demanda, com estratégia.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">7</span></div>
        <div class="card">
          <h3 class="card__title"><span>Continuar vendendo depois do lançamento</span></h3>
          <div class="card__body"><div><p class="card__desc">O trabalho do autor não termina no dia da publicação. Começa ali. Sem isso, o livro morre na segunda semana.</p></div></div>
        </div>
      </li>""",
        "PC_TEXT": """Você só lança seu livro <em>uma vez</em>.<br>Se for sozinho e der errado, <em class="hl-risco">e aí?</em>""",
        "MENTORIA": """Você valida cada decisão (capa, editora, data de lançamento) com quem já guiou 800 lançamentos.""",
        "GARANTIA_CLOSE": """          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</section>

""",
        "FAQ_LIST": """      <details class="faq-item">
        <summary>Ainda não terminei o livro. É cedo demais pra entrar?</summary>
        <div class="answer">Pelo contrário. Esse é o momento ideal. Quando o livro fica pronto, a estratégia precisa estar pronta também. Começar agora significa chegar no lançamento com leitores esperando, posicionamento testado e canais funcionando. Quem deixa pra começar depois do livro pronto sempre corre atrás do prejuízo.</div>
      </details>
      <details class="faq-item">
        <summary>Vou conseguir escrever e construir audiência ao mesmo tempo?</summary>
        <div class="answer">Sim, porque o método foi construído pra isso. Entre 1 e 3 horas por semana de trabalho estratégico, em paralelo à escrita. A maioria dos alunos relata que a clareza sobre o leitor melhora até o próprio processo criativo. Estratégia não rouba tempo da escrita. Dá direção pra ela.</div>
      </details>
      <details class="faq-item">
        <summary>R$ 249 é muito. Como sei que vai valer?</summary>
        <div class="answer">Quanto custa uma capa mal feita? Quanto custa um lançamento sem cronograma que vende só para amigos e família? Quanto custa mais um ano com o livro encalhado? O método tem garantia de 15 dias: se não estiver satisfeito, devolvemos sem perguntas.</div>
      </details>
      <details class="faq-item">
        <summary>Já tentei divulgar antes e não funcionou. Por que seria diferente agora?</summary>
        <div class="answer">Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade.</div>
      </details>
      <details class="faq-item">
        <summary>Não tenho seguidores. Funciona pra mim?</summary>
        <div class="answer">Funciona, e talvez melhor. Seguidor nunca foi o objetivo, <strong>leitor é</strong>. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram <strong>audiência certa, não audiência grande</strong>. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida.</div>
      </details>
      <details class="faq-item">
        <summary>Preciso de editora para o método funcionar?</summary>
        <div class="answer">Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora.</div>
      </details>
      <details class="faq-item">
        <summary>Quanto tempo por semana eu preciso dedicar?</summary>
        <div class="answer">Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim.</div>
      </details>
      <details class="faq-item">
        <summary>Devo procurar editora ou autopublicar? O método me ajuda nisso?</summary>
        <div class="answer">Ajuda. O método te dá os critérios pra escolher o caminho com clareza, não por insegurança. Editora não é prêmio nem solução automática. É uma das vias possíveis. Os bastidores editoriais que a Dany compartilha mostram o que cada modelo entrega de fato, e o que sempre fica nas mãos do autor.</div>
      </details>""",
        "FINAL_CTA": """<h2>Você foi longe demais<br><span class="italic">pra terminar sem leitores.</span></h2>
    <p style="font-size:17px; color:rgba(255,255,255,0.65); line-height:1.6; max-width:480px; margin:0 auto 36px;">O método está aqui. O livro está vindo. O único passo que falta é o seu.</p>""",
    },
    'lancando': {
        "variant": 'preco',
        "STAGE_SLUG": 'lancando',
        "SEO_HEAD": """<title>MTBB · Faça seu livro chegar aos leitores certos</title>
<meta name="description" content="Seu livro está pronto, mas os leitores precisam saber disso. O método de Dany Sakugawa pra fazer livros chegarem aos leitores certos. Testado em 800 lançamentos.">
<meta property="og:type" content="website">
<meta property="og:title" content="MTBB · Faça seu livro chegar aos leitores certos">
<meta property="og:description" content="Seu livro está pronto, mas os leitores precisam saber disso. O método de Dany Sakugawa pra fazer livros chegarem aos leitores certos. Testado em 800 lançamentos.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="MTBB · Faça seu livro chegar aos leitores certos">
<meta name="twitter:description" content="Seu livro está pronto, mas os leitores precisam saber disso. O método de Dany Sakugawa pra fazer livros chegarem aos leitores certos. Testado em 800 lançamentos.">
<link rel="canonical" href="https://metodo.thebookbusiness.com.br/lancando">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Dany Sakugawa">
<meta property="og:url" content="https://metodo.thebookbusiness.com.br/lancando">""",
        "LDJSON": """{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://metodo.thebookbusiness.com.br/#org","name":"The Book Business","url":"https://thebookbusiness.com.br","logo":"https://metodo.thebookbusiness.com.br/assets/og-mtbb.jpg","sameAs":["https://www.instagram.com/dany.sakugawa"],"founder":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}},{"@type":"Person","@id":"https://metodo.thebookbusiness.com.br/#dany","name":"Dany Sakugawa","jobTitle":"Especialista em marketing literário","image":"https://metodo.thebookbusiness.com.br/assets/dany-sakugawa.webp","worksFor":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"sameAs":["https://www.instagram.com/dany.sakugawa"]},{"@type":"WebSite","@id":"https://metodo.thebookbusiness.com.br/#website","url":"https://metodo.thebookbusiness.com.br/","name":"Método The Book Business","inLanguage":"pt-BR","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"Course","@id":"https://metodo.thebookbusiness.com.br/lancando#course","name":"Método The Book Business (MTBB)","description":"Seu livro está pronto, mas os leitores precisam saber disso. O método de Dany Sakugawa pra fazer livros chegarem aos leitores certos. Testado em 800 lançamentos.","inLanguage":"pt-BR","provider":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"hasCourseInstance":{"@type":"CourseInstance","courseMode":"Online","instructor":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}},"offers":{"@type":"Offer","price":"2500.00","priceCurrency":"BRL","availability":"https://schema.org/InStock","url":"https://metodo.thebookbusiness.com.br/lancando"}},{"@type":"VideoObject","name":"Aula gratuita — Método The Book Business","description":"Seu livro está pronto, mas os leitores precisam saber disso. O método de Dany Sakugawa pra fazer livros chegarem aos leitores certos. Testado em 800 lançamentos.","thumbnailUrl":["https://metodo.thebookbusiness.com.br/assets/aula-metodo-the-book-business.webp"],"uploadDate":"2025-01-15","contentUrl":"https://cdn.converteai.net/6b353be1-c671-4a98-af52-02bc731efaae/6a47c99aa63e151eb8ef0c44/main.m3u8","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"FAQPage","@id":"https://metodo.thebookbusiness.com.br/lancando#faq","mainEntity":[{"@type":"Question","name":"Por que entrar agora e não depois do lançamento?","acceptedAnswer":{"@type":"Answer","text":"Porque depois que o livro é publicado, você já perdeu parte da janela mais importante. O lançamento é o momento de maior atenção, e ele precisa ser construído antes, não improvisado depois. O MTBB te ajuda a chegar nesse momento com posicionamento claro, audiência aquecida e estratégia pronta. Entrar depois é tentar corrigir o tiro depois que o alvo passou."}},{"@type":"Question","name":"Meu livro já foi lançado. Ainda funciona?","acceptedAnswer":{"@type":"Answer","text":"Sim. Boa parte dos alunos chegam exatamente nessa situação. O método identifica o que não foi feito e começa a preencher essas lacunas. O mercado está cheio de escritores cujos livros só fizeram sucesso dois ou mais anos depois do lançamento."}},{"@type":"Question","name":"R$ 249 é muito. Como sei que vai valer?","acceptedAnswer":{"@type":"Answer","text":"Quanto custa uma capa mal feita? Quanto custa um lançamento sem cronograma que vende só para amigos e família? Quanto custa mais um ano com o livro encalhado? O método tem garantia de 15 dias: se não estiver satisfeito, devolvemos sem perguntas."}},{"@type":"Question","name":"Já tentei divulgar antes e não funcionou. Por que seria diferente agora?","acceptedAnswer":{"@type":"Answer","text":"Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade."}},{"@type":"Question","name":"Não tenho seguidores. Funciona pra mim?","acceptedAnswer":{"@type":"Answer","text":"Funciona, e talvez melhor. Seguidor nunca foi o objetivo, leitor é. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram audiência certa, não audiência grande. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida."}},{"@type":"Question","name":"Preciso de editora para o método funcionar?","acceptedAnswer":{"@type":"Answer","text":"Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora."}},{"@type":"Question","name":"Quanto tempo por semana eu preciso dedicar?","acceptedAnswer":{"@type":"Answer","text":"Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim."}},{"@type":"Question","name":"Minha editora já cuida do marketing. Ainda faz sentido?","acceptedAnswer":{"@type":"Answer","text":"Sim, e talvez mais do que para quem é independente. A maioria das editoras faz o lançamento e segue em frente. Quem sustenta o livro vendendo nos meses seguintes é o autor. O método te dá autonomia para não depender do ciclo da editora."}}]}]}""",
        "HERO_BADGE_H1": """    <div class="hero-badge">Para autores prestes a lançar</div>
    <h1>Seu livro está pronto.<br><span class="hero-italic" style="font-family:'Poppins',sans-serif; font-style:normal; font-weight:700;"><span class="hl-grifo">Os próximos passos</span> decidem se ele será lido… ou <span class="hl-risco">esquecido</span>.</span></h1>""",
        "HERO_WATCH": """Assista à aula abaixo e veja como chegar aos leitores certos.""",
        "CTA_POSVIDEO": """Seu livro merece ser lido.""",
        "AGITATION_BLOCK": """
<!-- BLOCO 3 — NÚMEROS -->



<!-- BLOCO 5 — AGITAÇÃO -->
<section class="agitation">
  <div class="container">
    <h2>Você pode ter escrito um livro <span class="hl-grifo">incrível</span>.</h2>
    <p class="agi-sub">E ainda assim não chegar aos <span class="hl-risco">leitores certos</span>.</p>
    <p class="agitation-quote"><span class="hw-line">Ninguém compra um livro</span><span class="hw-line">que não conhece.</span></p>
    <p class="agitation-closing">Esperança não muda isso.<br><span class="italic">Estratégia sim.</span></p>
  </div>
</section>

""",
        "JOURNEY_TITLE": """Do livro pronto ao livro lido""",
        "JOURNEY_STEPS": """      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">1</span></div>
        <div class="journey-step-marker" aria-hidden="true">Você está aqui.
          <svg class="arrow" viewBox="0 0 72 44" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6,6 Q20,2 38,16 Q54,26 64,38" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/>
            <path d="M52,34 L66,40 L60,28" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="card">
          <h3 class="card__title"><span>Parar de tratar o lançamento como sorte</span></h3>
          <div class="card__body"><div><p class="card__desc">Manuscrito pronto. Capa pronta. Vontade enorme. E a sensação incômoda de que, sem plano real, o livro vai sumir em silêncio.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">2</span></div>
        <div class="card">
          <h3 class="card__title"><span>Diagnosticar o livro na Matriz do Autor Estratégico</span></h3>
          <div class="card__body"><div><p class="card__desc">Antes de lançar, ver com clareza onde o livro está forte, onde está vulnerável, e o que ainda precisa de ajuste.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">3</span></div>
        <div class="card">
          <h3 class="card__title"><span>Encontrar o leitor certo</span></h3>
          <div class="card__body"><div><p class="card__desc">E onde ele está. Sem postar em grupo aleatório. Sem implorar para influenciador. Sem chutar. É descobrir quem vai desejar, comprar e recomendar.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">4</span></div>
        <div class="card">
          <h3 class="card__title"><span>Montar o cronograma estratégico do livro</span></h3>
          <div class="card__body"><div><p class="card__desc">Um plano claro do que fazer 90 dias antes, durante e depois do lançamento. Sem improviso. Sem pular etapa.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">5</span></div>
        <div class="card">
          <h3 class="card__title"><span>Construir demanda antes do livro sair</span></h3>
          <div class="card__body"><div><p class="card__desc">Ciclos curtos de pré-venda com começo, meio e fim. Cada um gera tração. E a tração não some, acumula.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">6</span></div>
        <div class="card">
          <h3 class="card__title"><span>Lançar com leitores esperando</span></h3>
          <div class="card__body"><div><p class="card__desc">Sem silêncio. Sem improviso. Com plano, com demanda, com estratégia.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">7</span></div>
        <div class="card">
          <h3 class="card__title"><span>Continuar vendendo depois do lançamento</span></h3>
          <div class="card__body"><div><p class="card__desc">O trabalho do autor não termina no dia da publicação. Começa ali. Sem isso, o livro morre na segunda semana.</p></div></div>
        </div>
      </li>""",
        "PC_TEXT": """Você só lança seu livro <em>uma vez</em>.<br>Se for sozinho e der errado, <em class="hl-risco">e aí?</em>""",
        "MENTORIA": """Você valida cada decisão (capa, editora, data de lançamento) com quem já guiou 800 lançamentos.""",
        "GARANTIA_CLOSE": """          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</section>

 </div>
</div>
</section>

""",
        "FAQ_LIST": """      <details class="faq-item">
        <summary>Por que entrar agora e não depois do lançamento?</summary>
        <div class="answer">Porque depois que o livro é publicado, você já perdeu parte da janela mais importante. O lançamento é o momento de maior atenção, e ele precisa ser construído antes, não improvisado depois. O MTBB te ajuda a chegar nesse momento com posicionamento claro, audiência aquecida e estratégia pronta. Entrar depois é tentar corrigir o tiro depois que o alvo passou.</div>
      </details>
      <details class="faq-item">
        <summary>Meu livro já foi lançado. Ainda funciona?</summary>
        <div class="answer">Sim. Boa parte dos alunos chegam exatamente nessa situação. O método identifica o que não foi feito e começa a preencher essas lacunas. O mercado está cheio de escritores cujos livros só fizeram sucesso dois ou mais anos depois do lançamento.</div>
      </details>
      <details class="faq-item">
        <summary>R$ 249 é muito. Como sei que vai valer?</summary>
        <div class="answer">Quanto custa uma capa mal feita? Quanto custa um lançamento sem cronograma que vende só para amigos e família? Quanto custa mais um ano com o livro encalhado? O método tem garantia de 15 dias: se não estiver satisfeito, devolvemos sem perguntas.</div>
      </details>
      <details class="faq-item">
        <summary>Já tentei divulgar antes e não funcionou. Por que seria diferente agora?</summary>
        <div class="answer">Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade.</div>
      </details>
      <details class="faq-item">
        <summary>Não tenho seguidores. Funciona pra mim?</summary>
        <div class="answer">Funciona, e talvez melhor. Seguidor nunca foi o objetivo, <strong>leitor é</strong>. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram <strong>audiência certa, não audiência grande</strong>. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida.</div>
      </details>
      <details class="faq-item">
        <summary>Preciso de editora para o método funcionar?</summary>
        <div class="answer">Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora.</div>
      </details>
      <details class="faq-item">
        <summary>Quanto tempo por semana eu preciso dedicar?</summary>
        <div class="answer">Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim.</div>
      </details>
      <details class="faq-item">
        <summary>Minha editora já cuida do marketing. Ainda faz sentido?</summary>
        <div class="answer">Sim, e talvez mais do que para quem é independente. A maioria das editoras faz o lançamento e segue em frente. Quem sustenta o livro vendendo nos meses seguintes é o autor. O método te dá autonomia para não depender do ciclo da editora.</div>
      </details>""",
        "FINAL_CTA": """<h2>Você foi longe demais<br><span class="italic">pra deixar o livro encalhar.</span></h2>
    <p style="font-size:17px; color:rgba(255,255,255,0.65); line-height:1.6; max-width:480px; margin:0 auto 36px;">O método está aqui. O livro está pronto. O único passo que falta é o seu.</p>""",
    },
    'publicado-lista': {
        "variant": 'lista',
        "STAGE_SLUG": 'publicado',
        "SEO_HEAD": """<title>MTBB · Entre na lista de espera</title>
<meta name="description" content="Seu livro foi lançado, mas precisa voltar a ser lido. Entre na lista de espera do Método The Book Business.">
<meta property="og:type" content="website">
<meta property="og:title" content="MTBB · Entre na lista de espera">
<meta property="og:description" content="Seu livro foi lançado, mas precisa voltar a ser lido. Entre na lista de espera do Método The Book Business.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="MTBB · Entre na lista de espera">
<meta name="twitter:description" content="Seu livro foi lançado, mas precisa voltar a ser lido. Entre na lista de espera do Método The Book Business.">
<link rel="canonical" href="https://metodo.thebookbusiness.com.br/publicado-lista">
<meta name="robots" content="noindex, follow">
<meta name="author" content="Dany Sakugawa">
<meta property="og:url" content="https://metodo.thebookbusiness.com.br/publicado-lista">""",
        "LDJSON": """{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://metodo.thebookbusiness.com.br/#org","name":"The Book Business","url":"https://thebookbusiness.com.br","logo":"https://metodo.thebookbusiness.com.br/assets/og-mtbb.jpg","sameAs":["https://www.instagram.com/dany.sakugawa"],"founder":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}},{"@type":"Person","@id":"https://metodo.thebookbusiness.com.br/#dany","name":"Dany Sakugawa","jobTitle":"Especialista em marketing literário","image":"https://metodo.thebookbusiness.com.br/assets/dany-sakugawa.webp","worksFor":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"sameAs":["https://www.instagram.com/dany.sakugawa"]},{"@type":"WebSite","@id":"https://metodo.thebookbusiness.com.br/#website","url":"https://metodo.thebookbusiness.com.br/","name":"Método The Book Business","inLanguage":"pt-BR","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"Course","@id":"https://metodo.thebookbusiness.com.br/publicado-lista#course","name":"Método The Book Business (MTBB)","description":"Seu livro foi lançado, mas precisa voltar a ser lido. Entre na lista de espera do Método The Book Business.","inLanguage":"pt-BR","provider":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"hasCourseInstance":{"@type":"CourseInstance","courseMode":"Online","instructor":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}}},{"@type":"VideoObject","name":"Aula gratuita — Método The Book Business","description":"Seu livro foi lançado, mas precisa voltar a ser lido. Entre na lista de espera do Método The Book Business.","thumbnailUrl":["https://metodo.thebookbusiness.com.br/assets/aula-metodo-the-book-business.webp"],"uploadDate":"2025-01-15","contentUrl":"https://cdn.converteai.net/6b353be1-c671-4a98-af52-02bc731efaae/6a47c99aa63e151eb8ef0c44/main.m3u8","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"FAQPage","@id":"https://metodo.thebookbusiness.com.br/publicado-lista#faq","mainEntity":[{"@type":"Question","name":"Meu livro foi lançado há tempos. Ainda dá pra recuperar?","acceptedAnswer":{"@type":"Answer","text":"Sim. Boa parte dos alunos chegam exatamente nessa situação. O método identifica o que não foi feito e começa a preencher essas lacunas. O mercado está cheio de livros que só começaram a vender de verdade dois ou três anos depois do lançamento, quando o autor encontrou a estratégia certa."}},{"@type":"Question","name":"O lançamento foi fraco. O método consegue reverter?","acceptedAnswer":{"@type":"Answer","text":"Reverter, sim. Mas não com truque. O método trata o livro como ele é hoje: um livro lançado que ainda não encontrou seus leitores certos. A partir daí, reconstrói posicionamento, ativa canais que ficaram parados e cria os pontos de contato que faltaram. Lançamento é um momento. A construção do livro como negócio é contínua."}},{"@type":"Question","name":"Quanto vai custar?","acceptedAnswer":{"@type":"Answer","text":"O valor é divulgado primeiro pra lista de espera, antes da venda pública. A lista recebe também condições especiais que não vão estar na página de vendas. Por isso entrar agora é estratégico, mesmo se a decisão final ainda não estiver tomada."}},{"@type":"Question","name":"Já tentei divulgar antes e não funcionou. Por que seria diferente agora?","acceptedAnswer":{"@type":"Answer","text":"Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade."}},{"@type":"Question","name":"Não tenho seguidores. Funciona pra mim?","acceptedAnswer":{"@type":"Answer","text":"Funciona, e talvez melhor. Seguidor nunca foi o objetivo, leitor é. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram audiência certa, não audiência grande. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida."}},{"@type":"Question","name":"Preciso de editora para o método funcionar?","acceptedAnswer":{"@type":"Answer","text":"Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora."}},{"@type":"Question","name":"Quanto tempo por semana eu preciso dedicar?","acceptedAnswer":{"@type":"Answer","text":"Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim."}},{"@type":"Question","name":"Minha editora já cuida do marketing. Ainda faz sentido?","acceptedAnswer":{"@type":"Answer","text":"Sim, e talvez mais do que para quem é independente. A maioria das editoras faz o lançamento e segue em frente. Quem sustenta o livro vendendo nos meses seguintes é o autor. O método te dá autonomia para não depender do ciclo da editora."}}]}]}""",
        "HERO_BADGE_H1": """    <div class="hero-badge">Para autores com livro lançado</div>
    <h1>Seu livro já foi lançado.<br><span class="hero-italic" style="font-family:'Poppins',sans-serif; font-style:normal; font-weight:700;"><span class="hl-grifo">Os próximos passos</span> decidem se ele será lido… ou <span class="hl-risco">esquecido</span>.</span></h1>""",
        "HERO_WATCH": """Assista à aula abaixo e veja como ser lido de verdade.""",
        "CTA_POSVIDEO": """Seu livro merece ser lido.""",
        "AGITATION_BLOCK": """
<!-- BLOCO 5 — AGITAÇÃO -->
<section class="agitation">
  <div class="container">
    <h2>Você pode ter lançado um livro <span class="hl-grifo">incrível</span>.</h2>
    <p class="agi-sub">E ainda assim ele parar de <span class="hl-risco">ser lido</span>.</p>
    <p class="agitation-quote"><span class="hw-line">Ninguém lê um livro</span><span class="hw-line">que ninguém lembra.</span></p>
    <p class="agitation-closing">Esperança não muda isso.<br><span class="italic">Estratégia sim.</span></p>
  </div>
</section>

<!-- TESE — citação (blockquote) -->
<section class="tese-faixa">
  <figure class="tese-quote">
    <blockquote>
      <span class="l1"><span class="qm">&ldquo;</span>Seu livro não precisa nascer de novo.</span>
      <span class="l2">Precisa voltar a ser encontrado.</span>
    </blockquote>
    <cite>Dany Sakugawa</cite>
  </figure>
</section>

""",
        "JOURNEY_TITLE": """Do livro lançado ao livro lido de verdade""",
        "JOURNEY_STEPS": """      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">1</span></div>
        <div class="journey-step-marker" aria-hidden="true">Você está aqui.
          <svg class="arrow" viewBox="0 0 72 44" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6,6 Q20,2 38,16 Q54,26 64,38" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/>
            <path d="M52,34 L66,40 L60,28" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="card">
          <h3 class="card__title"><span>Parar de aceitar que o livro perdeu força</span></h3>
          <div class="card__body"><div><p class="card__desc">Livro publicado. Lançamento já passou. E a sensação incômoda de que ele parou antes de encontrar quem precisava ler.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">2</span></div>
        <div class="card">
          <h3 class="card__title"><span>Diagnosticar o livro na Matriz do Autor Estratégico</span></h3>
          <div class="card__body"><div><p class="card__desc">Ver com clareza por que ele parou de circular: onde está forte, onde está vulnerável, e o que ainda precisa de ajuste.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">3</span></div>
        <div class="card">
          <h3 class="card__title"><span>Reencontrar o leitor certo</span></h3>
          <div class="card__body"><div><p class="card__desc">E onde ele está hoje. Sem postar em grupo aleatório. Sem implorar para influenciador. Sem chutar. É descobrir quem ainda vai desejar, comprar e recomendar.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">4</span></div>
        <div class="card">
          <h3 class="card__title"><span>Montar o plano de reativação do livro</span></h3>
          <div class="card__body"><div><p class="card__desc">Um plano claro do que fazer pra colocar o livro de volta na rua. Sem improviso. Sem pular etapa.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">5</span></div>
        <div class="card">
          <h3 class="card__title"><span>Reativar demanda em ciclos curtos</span></h3>
          <div class="card__body"><div><p class="card__desc">Cada ciclo tem começo, meio e fim. Cada um gera tração. E a tração não some, acumula.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">6</span></div>
        <div class="card">
          <h3 class="card__title"><span>Fazer o livro voltar a circular</span></h3>
          <div class="card__body"><div><p class="card__desc">Sem silêncio. Sem improviso. Com plano, com demanda, com estratégia.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">7</span></div>
        <div class="card">
          <h3 class="card__title"><span>Sustentar o livro vivo no longo prazo</span></h3>
          <div class="card__body"><div><p class="card__desc">O trabalho do autor nunca termina no lançamento. Continua aqui. Sem isso, o livro volta a apagar.</p></div></div>
        </div>
      </li>""",
        "PC_TEXT": """Você lançou seu livro.<br>Se sozinho não foi o suficiente, <em class="hl-risco">e agora?</em>""",
        "MENTORIA": """Você valida cada decisão (reativar o livro, ajustar posicionamento ou planejar o próximo) com quem já guiou 800 lançamentos.""",
        "GARANTIA_CLOSE": """  </div>
</section>

""",
        "FAQ_LIST": """      <details class="faq-item">
        <summary>Meu livro foi lançado há tempos. Ainda dá pra recuperar?</summary>
        <div class="answer">Sim. Boa parte dos alunos chegam exatamente nessa situação. O método identifica o que não foi feito e começa a preencher essas lacunas. O mercado está cheio de livros que só começaram a vender de verdade dois ou três anos depois do lançamento, quando o autor encontrou a estratégia certa.</div>
      </details>
      <details class="faq-item">
        <summary>O lançamento foi fraco. O método consegue reverter?</summary>
        <div class="answer">Reverter, sim. Mas não com truque. O método trata o livro como ele é hoje: um livro lançado que ainda não encontrou seus leitores certos. A partir daí, reconstrói posicionamento, ativa canais que ficaram parados e cria os pontos de contato que faltaram. Lançamento é um momento. A construção do livro como negócio é contínua.</div>
      </details>
      <details class="faq-item">
        <summary>Quanto vai custar?</summary>
        <div class="answer">O valor é divulgado primeiro pra lista de espera, antes da venda pública. A lista recebe também condições especiais que não vão estar na página de vendas. Por isso entrar agora é estratégico, mesmo se a decisão final ainda não estiver tomada.</div>
      </details>
      <details class="faq-item">
        <summary>Já tentei divulgar antes e não funcionou. Por que seria diferente agora?</summary>
        <div class="answer">Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade.</div>
      </details>
      <details class="faq-item">
        <summary>Não tenho seguidores. Funciona pra mim?</summary>
        <div class="answer">Funciona, e talvez melhor. Seguidor nunca foi o objetivo, <strong>leitor é</strong>. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram <strong>audiência certa, não audiência grande</strong>. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida.</div>
      </details>
      <details class="faq-item">
        <summary>Preciso de editora para o método funcionar?</summary>
        <div class="answer">Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora.</div>
      </details>
      <details class="faq-item">
        <summary>Quanto tempo por semana eu preciso dedicar?</summary>
        <div class="answer">Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim.</div>
      </details>
      <details class="faq-item">
        <summary>Minha editora já cuida do marketing. Ainda faz sentido?</summary>
        <div class="answer">Sim, e talvez mais do que para quem é independente. A maioria das editoras faz o lançamento e segue em frente. Quem sustenta o livro vendendo nos meses seguintes é o autor. O método te dá autonomia para não depender do ciclo da editora.</div>
      </details>""",
        "FINAL_CTA": """<h2>Você foi longe demais<br><span class="italic">pra ver o livro parar.</span></h2>
    <p style="font-size:17px; color:rgba(255,255,255,0.65); line-height:1.6; max-width:480px; margin:0 auto 36px;">O método está aqui. O livro está lançado. O único passo que falta é o seu.</p>""",
    },
    'escrevendo-lista': {
        "variant": 'lista',
        "STAGE_SLUG": 'escrevendo',
        "SEO_HEAD": """<title>MTBB · Entre na lista de espera</title>
<meta name="description" content="Você está escrevendo. Os leitores podem já estar esperando. Entre na lista de espera do Método The Book Business.">
<meta property="og:type" content="website">
<meta property="og:title" content="MTBB · Entre na lista de espera">
<meta property="og:description" content="Você está escrevendo. Os leitores podem já estar esperando. Entre na lista de espera do Método The Book Business.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="MTBB · Entre na lista de espera">
<meta name="twitter:description" content="Você está escrevendo. Os leitores podem já estar esperando. Entre na lista de espera do Método The Book Business.">
<link rel="canonical" href="https://metodo.thebookbusiness.com.br/escrevendo-lista">
<meta name="robots" content="noindex, follow">
<meta name="author" content="Dany Sakugawa">
<meta property="og:url" content="https://metodo.thebookbusiness.com.br/escrevendo-lista">""",
        "LDJSON": """{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://metodo.thebookbusiness.com.br/#org","name":"The Book Business","url":"https://thebookbusiness.com.br","logo":"https://metodo.thebookbusiness.com.br/assets/og-mtbb.jpg","sameAs":["https://www.instagram.com/dany.sakugawa"],"founder":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}},{"@type":"Person","@id":"https://metodo.thebookbusiness.com.br/#dany","name":"Dany Sakugawa","jobTitle":"Especialista em marketing literário","image":"https://metodo.thebookbusiness.com.br/assets/dany-sakugawa.webp","worksFor":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"sameAs":["https://www.instagram.com/dany.sakugawa"]},{"@type":"WebSite","@id":"https://metodo.thebookbusiness.com.br/#website","url":"https://metodo.thebookbusiness.com.br/","name":"Método The Book Business","inLanguage":"pt-BR","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"Course","@id":"https://metodo.thebookbusiness.com.br/escrevendo-lista#course","name":"Método The Book Business (MTBB)","description":"Você está escrevendo. Os leitores podem já estar esperando. Entre na lista de espera do Método The Book Business.","inLanguage":"pt-BR","provider":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"hasCourseInstance":{"@type":"CourseInstance","courseMode":"Online","instructor":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}}},{"@type":"VideoObject","name":"Aula gratuita — Método The Book Business","description":"Você está escrevendo. Os leitores podem já estar esperando. Entre na lista de espera do Método The Book Business.","thumbnailUrl":["https://metodo.thebookbusiness.com.br/assets/aula-metodo-the-book-business.webp"],"uploadDate":"2025-01-15","contentUrl":"https://cdn.converteai.net/6b353be1-c671-4a98-af52-02bc731efaae/6a47c99aa63e151eb8ef0c44/main.m3u8","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"FAQPage","@id":"https://metodo.thebookbusiness.com.br/escrevendo-lista#faq","mainEntity":[{"@type":"Question","name":"Ainda não terminei o livro. É cedo demais pra entrar?","acceptedAnswer":{"@type":"Answer","text":"Pelo contrário. Esse é o momento ideal. Quando o livro fica pronto, a estratégia precisa estar pronta também. Começar agora significa chegar no lançamento com leitores esperando, posicionamento testado e canais funcionando. Quem deixa pra começar depois do livro pronto sempre corre atrás do prejuízo."}},{"@type":"Question","name":"Vou conseguir escrever e construir audiência ao mesmo tempo?","acceptedAnswer":{"@type":"Answer","text":"Sim, porque o método foi construído pra isso. Entre 1 e 3 horas por semana de trabalho estratégico, em paralelo à escrita. A maioria dos alunos relata que a clareza sobre o leitor melhora até o próprio processo criativo. Estratégia não rouba tempo da escrita. Dá direção pra ela."}},{"@type":"Question","name":"Quanto vai custar?","acceptedAnswer":{"@type":"Answer","text":"O valor é divulgado primeiro pra lista de espera, antes da venda pública. A lista recebe também condições especiais que não vão estar na página de vendas. Por isso entrar agora é estratégico, mesmo se a decisão final ainda não estiver tomada."}},{"@type":"Question","name":"Já tentei divulgar antes e não funcionou. Por que seria diferente agora?","acceptedAnswer":{"@type":"Answer","text":"Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade."}},{"@type":"Question","name":"Não tenho seguidores. Funciona pra mim?","acceptedAnswer":{"@type":"Answer","text":"Funciona, e talvez melhor. Seguidor nunca foi o objetivo, leitor é. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram audiência certa, não audiência grande. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida."}},{"@type":"Question","name":"Preciso de editora para o método funcionar?","acceptedAnswer":{"@type":"Answer","text":"Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora."}},{"@type":"Question","name":"Quanto tempo por semana eu preciso dedicar?","acceptedAnswer":{"@type":"Answer","text":"Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim."}},{"@type":"Question","name":"Devo procurar editora ou autopublicar? O método me ajuda nisso?","acceptedAnswer":{"@type":"Answer","text":"Ajuda. O método te dá os critérios pra escolher o caminho com clareza, não por insegurança. Editora não é prêmio nem solução automática. É uma das vias possíveis. Os bastidores editoriais que a Dany compartilha mostram o que cada modelo entrega de fato, e o que sempre fica nas mãos do autor."}}]}]}""",
        "HERO_BADGE_H1": """    <div class="hero-badge">Para autores escrevendo</div>
    <h1>Você está escrevendo seu livro.<br><span class="hero-italic" style="font-family:'Poppins',sans-serif; font-style:normal; font-weight:700;"><span class="hl-grifo">Os próximos passos</span> decidem se ele será lido… ou <span class="hl-risco">esquecido</span>.</span></h1>""",
        "HERO_WATCH": """Assista à aula abaixo e veja como atrair seus leitores.""",
        "CTA_POSVIDEO": """Seu livro merece ser lido.""",
        "AGITATION_BLOCK": """
<!-- BLOCO 5 — AGITAÇÃO -->
<section class="agitation">
  <div class="container">
    <h2>Você pode estar escrevendo um livro <span class="hl-grifo">incrível</span>.</h2>
    <p class="agi-sub">E ainda assim terminar sem <span class="hl-risco">leitores esperando</span>.</p>
    <p class="agitation-quote"><span class="hw-line">Ninguém compra um livro</span><span class="hw-line">que não conhece.</span></p>
    <p class="agitation-closing">Esperança não muda isso.<br><span class="italic">Estratégia sim.</span></p>
  </div>
</section>

<!-- TESE — citação (blockquote) -->
<section class="tese-faixa">
  <figure class="tese-quote">
    <blockquote>
      <span class="l1"><span class="qm">&ldquo;</span>O lançamento não começa quando o livro fica pronto.</span>
      <span class="l2">Começa nas decisões que você toma enquanto escreve.</span>
    </blockquote>
    <cite>Dany Sakugawa</cite>
  </figure>
</section>

""",
        "JOURNEY_TITLE": """Da escrita estratégica ao livro lido""",
        "JOURNEY_STEPS": """      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">1</span></div>
        <div class="journey-step-marker" aria-hidden="true">Você está aqui.
          <svg class="arrow" viewBox="0 0 72 44" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6,6 Q20,2 38,16 Q54,26 64,38" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/>
            <path d="M52,34 L66,40 L60,28" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="card">
          <h3 class="card__title"><span>Parar de escrever sem pensar no leitor</span></h3>
          <div class="card__body"><div><p class="card__desc">Capítulos avançando. Vontade enorme. E a sensação incômoda de que ninguém estará esperando quando o livro ficar pronto.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">2</span></div>
        <div class="card">
          <h3 class="card__title"><span>Diagnosticar a ideia do livro na Matriz do Autor Estratégico</span></h3>
          <div class="card__body"><div><p class="card__desc">Antes de seguir escrevendo, ver com clareza onde o projeto está forte, onde está vulnerável, e o que ainda precisa de ajuste.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">3</span></div>
        <div class="card">
          <h3 class="card__title"><span>Encontrar o leitor certo desde já</span></h3>
          <div class="card__body"><div><p class="card__desc">E onde ele está. Sem postar em grupo aleatório. Sem implorar para influenciador. Sem chutar. É descobrir quem vai desejar, comprar e recomendar.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">4</span></div>
        <div class="card">
          <h3 class="card__title"><span>Montar o cronograma estratégico do livro</span></h3>
          <div class="card__body"><div><p class="card__desc">Um plano claro do que fazer enquanto escreve, antes de publicar, e depois do livro sair. Sem improviso. Sem pular etapa.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">5</span></div>
        <div class="card">
          <h3 class="card__title"><span>Construir audiência enquanto o livro nasce</span></h3>
          <div class="card__body"><div><p class="card__desc">Ciclos curtos de presença com começo, meio e fim. Cada um gera tração. E a tração não some, acumula.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">6</span></div>
        <div class="card">
          <h3 class="card__title"><span>Lançar com leitores esperando</span></h3>
          <div class="card__body"><div><p class="card__desc">Sem silêncio. Sem improviso. Com plano, com demanda, com estratégia.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">7</span></div>
        <div class="card">
          <h3 class="card__title"><span>Continuar vendendo depois do lançamento</span></h3>
          <div class="card__body"><div><p class="card__desc">O trabalho do autor não termina no dia da publicação. Começa ali. Sem isso, o livro morre na segunda semana.</p></div></div>
        </div>
      </li>""",
        "PC_TEXT": """Você só lança seu livro <em>uma vez</em>.<br>Se for sozinho e der errado, <em class="hl-risco">e aí?</em>""",
        "MENTORIA": """Você valida cada decisão (capa, editora, data de lançamento) com quem já guiou 800 lançamentos.""",
        "GARANTIA_CLOSE": """  </div>
</section>

""",
        "FAQ_LIST": """      <details class="faq-item">
        <summary>Ainda não terminei o livro. É cedo demais pra entrar?</summary>
        <div class="answer">Pelo contrário. Esse é o momento ideal. Quando o livro fica pronto, a estratégia precisa estar pronta também. Começar agora significa chegar no lançamento com leitores esperando, posicionamento testado e canais funcionando. Quem deixa pra começar depois do livro pronto sempre corre atrás do prejuízo.</div>
      </details>
      <details class="faq-item">
        <summary>Vou conseguir escrever e construir audiência ao mesmo tempo?</summary>
        <div class="answer">Sim, porque o método foi construído pra isso. Entre 1 e 3 horas por semana de trabalho estratégico, em paralelo à escrita. A maioria dos alunos relata que a clareza sobre o leitor melhora até o próprio processo criativo. Estratégia não rouba tempo da escrita. Dá direção pra ela.</div>
      </details>
      <details class="faq-item">
        <summary>Quanto vai custar?</summary>
        <div class="answer">O valor é divulgado primeiro pra lista de espera, antes da venda pública. A lista recebe também condições especiais que não vão estar na página de vendas. Por isso entrar agora é estratégico, mesmo se a decisão final ainda não estiver tomada.</div>
      </details>
      <details class="faq-item">
        <summary>Já tentei divulgar antes e não funcionou. Por que seria diferente agora?</summary>
        <div class="answer">Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade.</div>
      </details>
      <details class="faq-item">
        <summary>Não tenho seguidores. Funciona pra mim?</summary>
        <div class="answer">Funciona, e talvez melhor. Seguidor nunca foi o objetivo, <strong>leitor é</strong>. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram <strong>audiência certa, não audiência grande</strong>. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida.</div>
      </details>
      <details class="faq-item">
        <summary>Preciso de editora para o método funcionar?</summary>
        <div class="answer">Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora.</div>
      </details>
      <details class="faq-item">
        <summary>Quanto tempo por semana eu preciso dedicar?</summary>
        <div class="answer">Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim.</div>
      </details>
      <details class="faq-item">
        <summary>Devo procurar editora ou autopublicar? O método me ajuda nisso?</summary>
        <div class="answer">Ajuda. O método te dá os critérios pra escolher o caminho com clareza, não por insegurança. Editora não é prêmio nem solução automática. É uma das vias possíveis. Os bastidores editoriais que a Dany compartilha mostram o que cada modelo entrega de fato, e o que sempre fica nas mãos do autor.</div>
      </details>""",
        "FINAL_CTA": """<h2>Você foi longe demais<br><span class="italic">pra terminar sem leitores.</span></h2>
    <p style="font-size:17px; color:rgba(255,255,255,0.65); line-height:1.6; max-width:480px; margin:0 auto 36px;">O método está aqui. O livro está vindo. O único passo que falta é o seu.</p>""",
    },
    'lancando-lista': {
        "variant": 'lista',
        "STAGE_SLUG": 'lancando',
        "SEO_HEAD": """<title>MTBB · Entre na lista de espera</title>
<meta name="description" content="Seu livro está pronto, mas os leitores precisam saber disso. Entre na lista de espera do Método The Book Business.">
<meta property="og:type" content="website">
<meta property="og:title" content="MTBB · Entre na lista de espera">
<meta property="og:description" content="Seu livro está pronto, mas os leitores precisam saber disso. Entre na lista de espera do Método The Book Business.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="MTBB · Entre na lista de espera">
<meta name="twitter:description" content="Seu livro está pronto, mas os leitores precisam saber disso. Entre na lista de espera do Método The Book Business.">
<link rel="canonical" href="https://metodo.thebookbusiness.com.br/lancando-lista">
<meta name="robots" content="noindex, follow">
<meta name="author" content="Dany Sakugawa">
<meta property="og:url" content="https://metodo.thebookbusiness.com.br/lancando-lista">""",
        "LDJSON": """{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://metodo.thebookbusiness.com.br/#org","name":"The Book Business","url":"https://thebookbusiness.com.br","logo":"https://metodo.thebookbusiness.com.br/assets/og-mtbb.jpg","sameAs":["https://www.instagram.com/dany.sakugawa"],"founder":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}},{"@type":"Person","@id":"https://metodo.thebookbusiness.com.br/#dany","name":"Dany Sakugawa","jobTitle":"Especialista em marketing literário","image":"https://metodo.thebookbusiness.com.br/assets/dany-sakugawa.webp","worksFor":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"sameAs":["https://www.instagram.com/dany.sakugawa"]},{"@type":"WebSite","@id":"https://metodo.thebookbusiness.com.br/#website","url":"https://metodo.thebookbusiness.com.br/","name":"Método The Book Business","inLanguage":"pt-BR","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"Course","@id":"https://metodo.thebookbusiness.com.br/lancando-lista#course","name":"Método The Book Business (MTBB)","description":"Seu livro está pronto, mas os leitores precisam saber disso. Entre na lista de espera do Método The Book Business.","inLanguage":"pt-BR","provider":{"@id":"https://metodo.thebookbusiness.com.br/#org"},"hasCourseInstance":{"@type":"CourseInstance","courseMode":"Online","instructor":{"@id":"https://metodo.thebookbusiness.com.br/#dany"}}},{"@type":"VideoObject","name":"Aula gratuita — Método The Book Business","description":"Seu livro está pronto, mas os leitores precisam saber disso. Entre na lista de espera do Método The Book Business.","thumbnailUrl":["https://metodo.thebookbusiness.com.br/assets/aula-metodo-the-book-business.webp"],"uploadDate":"2025-01-15","contentUrl":"https://cdn.converteai.net/6b353be1-c671-4a98-af52-02bc731efaae/6a47c99aa63e151eb8ef0c44/main.m3u8","publisher":{"@id":"https://metodo.thebookbusiness.com.br/#org"}},{"@type":"FAQPage","@id":"https://metodo.thebookbusiness.com.br/lancando-lista#faq","mainEntity":[{"@type":"Question","name":"Por que entrar agora e não depois do lançamento?","acceptedAnswer":{"@type":"Answer","text":"Porque depois que o livro é publicado, você já perdeu parte da janela mais importante. O lançamento é o momento de maior atenção, e ele precisa ser construído antes, não improvisado depois. O MTBB te ajuda a chegar nesse momento com posicionamento claro, audiência aquecida e estratégia pronta. Entrar depois é tentar corrigir o tiro depois que o alvo passou."}},{"@type":"Question","name":"Meu livro já foi lançado. Ainda funciona?","acceptedAnswer":{"@type":"Answer","text":"Sim. Boa parte dos alunos chegam exatamente nessa situação. O método identifica o que não foi feito e começa a preencher essas lacunas. O mercado está cheio de escritores cujos livros só fizeram sucesso dois ou mais anos depois do lançamento."}},{"@type":"Question","name":"Quanto vai custar?","acceptedAnswer":{"@type":"Answer","text":"O valor é divulgado primeiro pra lista de espera, antes da venda pública. A lista recebe também condições especiais que não vão estar na página de vendas. Por isso entrar agora é estratégico, mesmo se a decisão final ainda não estiver tomada."}},{"@type":"Question","name":"Já tentei divulgar antes e não funcionou. Por que seria diferente agora?","acceptedAnswer":{"@type":"Answer","text":"Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade."}},{"@type":"Question","name":"Não tenho seguidores. Funciona pra mim?","acceptedAnswer":{"@type":"Answer","text":"Funciona, e talvez melhor. Seguidor nunca foi o objetivo, leitor é. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram audiência certa, não audiência grande. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida."}},{"@type":"Question","name":"Preciso de editora para o método funcionar?","acceptedAnswer":{"@type":"Answer","text":"Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora."}},{"@type":"Question","name":"Quanto tempo por semana eu preciso dedicar?","acceptedAnswer":{"@type":"Answer","text":"Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim."}},{"@type":"Question","name":"Minha editora já cuida do marketing. Ainda faz sentido?","acceptedAnswer":{"@type":"Answer","text":"Sim, e talvez mais do que para quem é independente. A maioria das editoras faz o lançamento e segue em frente. Quem sustenta o livro vendendo nos meses seguintes é o autor. O método te dá autonomia para não depender do ciclo da editora."}}]}]}""",
        "HERO_BADGE_H1": """    <div class="hero-badge">Para autores prestes a lançar</div>
    <h1>Seu livro está pronto.<br><span class="hero-italic" style="font-family:'Poppins',sans-serif; font-style:normal; font-weight:700;"><span class="hl-grifo">Os próximos passos</span> decidem se ele será lido… ou <span class="hl-risco">esquecido</span>.</span></h1>""",
        "HERO_WATCH": """Assista à aula abaixo e veja como chegar aos leitores certos.""",
        "CTA_POSVIDEO": """Seu livro merece ser lido.""",
        "AGITATION_BLOCK": """
<!-- BLOCO 5 — AGITAÇÃO -->
<section class="agitation">
  <div class="container">
    <h2>Você pode ter escrito um livro <span class="hl-grifo">incrível</span>.</h2>
    <p class="agi-sub">E ainda assim não chegar aos <span class="hl-risco">leitores certos</span>.</p>
    <p class="agitation-quote"><span class="hw-line">Ninguém compra um livro</span><span class="hw-line">que não conhece.</span></p>
    <p class="agitation-closing">Esperança não muda isso.<br><span class="italic">Estratégia sim.</span></p>
  </div>
</section>

""",
        "JOURNEY_TITLE": """Do livro pronto ao livro lido""",
        "JOURNEY_STEPS": """      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">1</span></div>
        <div class="journey-step-marker" aria-hidden="true">Você está aqui.
          <svg class="arrow" viewBox="0 0 72 44" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6,6 Q20,2 38,16 Q54,26 64,38" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round"/>
            <path d="M52,34 L66,40 L60,28" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <div class="card">
          <h3 class="card__title"><span>Parar de tratar o lançamento como sorte</span></h3>
          <div class="card__body"><div><p class="card__desc">Manuscrito pronto. Capa pronta. Vontade enorme. E a sensação incômoda de que, sem plano real, o livro vai sumir em silêncio.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">2</span></div>
        <div class="card">
          <h3 class="card__title"><span>Diagnosticar o livro na Matriz do Autor Estratégico</span></h3>
          <div class="card__body"><div><p class="card__desc">Antes de lançar, ver com clareza onde o livro está forte, onde está vulnerável, e o que ainda precisa de ajuste.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">3</span></div>
        <div class="card">
          <h3 class="card__title"><span>Encontrar o leitor certo</span></h3>
          <div class="card__body"><div><p class="card__desc">E onde ele está. Sem postar em grupo aleatório. Sem implorar para influenciador. Sem chutar. É descobrir quem vai desejar, comprar e recomendar.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">4</span></div>
        <div class="card">
          <h3 class="card__title"><span>Montar o cronograma estratégico do livro</span></h3>
          <div class="card__body"><div><p class="card__desc">Um plano claro do que fazer 90 dias antes, durante e depois do lançamento. Sem improviso. Sem pular etapa.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">5</span></div>
        <div class="card">
          <h3 class="card__title"><span>Construir demanda antes do livro sair</span></h3>
          <div class="card__body"><div><p class="card__desc">Ciclos curtos de pré-venda com começo, meio e fim. Cada um gera tração. E a tração não some, acumula.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">6</span></div>
        <div class="card">
          <h3 class="card__title"><span>Lançar com leitores esperando</span></h3>
          <div class="card__body"><div><p class="card__desc">Sem silêncio. Sem improviso. Com plano, com demanda, com estratégia.</p></div></div>
        </div>
      </li>
      <li class="step">
        <div class="step__node" aria-hidden="true"><span class="num">7</span></div>
        <div class="card">
          <h3 class="card__title"><span>Continuar vendendo depois do lançamento</span></h3>
          <div class="card__body"><div><p class="card__desc">O trabalho do autor não termina no dia da publicação. Começa ali. Sem isso, o livro morre na segunda semana.</p></div></div>
        </div>
      </li>""",
        "PC_TEXT": """Você só lança seu livro <em>uma vez</em>.<br>Se for sozinho e der errado, <em class="hl-risco">e aí?</em>""",
        "MENTORIA": """Você valida cada decisão (capa, editora, data de lançamento) com quem já guiou 800 lançamentos.""",
        "GARANTIA_CLOSE": """  </div>
</section>

""",
        "FAQ_LIST": """      <details class="faq-item">
        <summary>Por que entrar agora e não depois do lançamento?</summary>
        <div class="answer">Porque depois que o livro é publicado, você já perdeu parte da janela mais importante. O lançamento é o momento de maior atenção, e ele precisa ser construído antes, não improvisado depois. O MTBB te ajuda a chegar nesse momento com posicionamento claro, audiência aquecida e estratégia pronta. Entrar depois é tentar corrigir o tiro depois que o alvo passou.</div>
      </details>
      <details class="faq-item">
        <summary>Meu livro já foi lançado. Ainda funciona?</summary>
        <div class="answer">Sim. Boa parte dos alunos chegam exatamente nessa situação. O método identifica o que não foi feito e começa a preencher essas lacunas. O mercado está cheio de escritores cujos livros só fizeram sucesso dois ou mais anos depois do lançamento.</div>
      </details>
      <details class="faq-item">
        <summary>Quanto vai custar?</summary>
        <div class="answer">O valor é divulgado primeiro pra lista de espera, antes da venda pública. A lista recebe também condições especiais que não vão estar na página de vendas. Por isso entrar agora é estratégico, mesmo se a decisão final ainda não estiver tomada.</div>
      </details>
      <details class="faq-item">
        <summary>Já tentei divulgar antes e não funcionou. Por que seria diferente agora?</summary>
        <div class="answer">Porque divulgação sem método é perseguir borboleta. Você vai tendo ideias aqui e ali, tentando coisas que funcionaram para outros autores, e nada encaixa. O método dá estrutura, sequência e previsibilidade.</div>
      </details>
      <details class="faq-item">
        <summary>Não tenho seguidores. Funciona pra mim?</summary>
        <div class="answer">Funciona, e talvez melhor. Seguidor nunca foi o objetivo, <strong>leitor é</strong>. Existem autores com presença mínima no Instagram que são amplamente lidos porque construíram <strong>audiência certa, não audiência grande</strong>. O caminho real não é inflar Instagram pra ser notado por editora. É dominar posicionamento, leitor ideal e fundamentos. O método ensina isso, usando o próprio livro como ponto de partida.</div>
      </details>
      <details class="faq-item">
        <summary>Preciso de editora para o método funcionar?</summary>
        <div class="answer">Não. Do ponto de vista do marketing, toda publicação é uma autopublicação. Quem leva o leitor até o livro é o autor, com ou sem editora.</div>
      </details>
      <details class="faq-item">
        <summary>Quanto tempo por semana eu preciso dedicar?</summary>
        <div class="answer">Entre 1 e 3 horas por semana é suficiente pra avançar de forma consistente. Tem aluno que concentra em fins de semana, tem quem prefere 30 minutos por dia. O método foi construído pra respeitar isso. E como o acesso é por 2 anos, ninguém fica pra trás por causa de uma semana ruim.</div>
      </details>
      <details class="faq-item">
        <summary>Minha editora já cuida do marketing. Ainda faz sentido?</summary>
        <div class="answer">Sim, e talvez mais do que para quem é independente. A maioria das editoras faz o lançamento e segue em frente. Quem sustenta o livro vendendo nos meses seguintes é o autor. O método te dá autonomia para não depender do ciclo da editora.</div>
      </details>""",
        "FINAL_CTA": """<h2>Você foi longe demais<br><span class="italic">pra deixar o livro encalhar.</span></h2>
    <p style="font-size:17px; color:rgba(255,255,255,0.65); line-height:1.6; max-width:480px; margin:0 auto 36px;">O método está aqui. O livro está pronto. O único passo que falta é o seu.</p>""",
    },
}
