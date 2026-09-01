/* =============================================================================
   ROLETA DE ÂNCORA — módulo para embutir na PV da MasterClass
   Piso R$29 (preço atual). Degraus R$97 e R$47 acima.
   NÃO é desconto: é âncora. Ninguém paga menos do que já pagaria hoje.

   Como usar:  <script src="roleta-embed.js" defer></script>
   Desligar:   basta remover a tag. Nada mais no HTML depende disso.
   Forçar:     ?roleta=1 abre na hora (para revisão)
   ============================================================================= */
(function () {
  'use strict';

  var CFG = {
    // ordem: pior -> melhor. o último é o prêmio máximo.
    escada: [
      { id: '97', label: 'R$ 97', num: 97, off: 'COLE_OFF_97' },
      { id: '47', label: 'R$ 47', num: 47, off: 'COLE_OFF_47' },
      { id: '29', label: 'R$ 29', num: 29, off: '', max: true }   // '' = preço base do produto
    ],
    fatias: ['29', '97', '47', '97', '29', '47', '97', '47'],
    chances: 3,
    chanceDePularProMax: 0.55,   // no 2º giro; o resto chega no 3º. nunca no 1º.
    minutosDeReserva: 10,
    precoCheio: 'R$ 97',

    // gatilhos (mobile é 91% do tráfego, então mouseleave é o menos importante)
    segundosNaPagina: 45,   // só considera abrir depois disso
    segundosParado: 12,     // sem toque/scroll/clique por esse tempo
    scrollUpPx: 420,        // subiu isso de uma vez = sinal de saída no mobile
    usarBotaoVoltar: true,  // intercepta o "voltar" (instável em WebView do IG/FB)
    umaVezPorDia: true
  };

  /* ---------- não mostrar pra quem não deve ---------- */
  var KEY = 'mc_roleta_pv_v1';
  var S = null;
  try { S = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { }
  if (!S || S.v !== 1) S = { v: 1, giros: 0, nivel: -1, fechado: false, prazo: 0, visto: 0, pula: Math.random() < CFG.chanceDePularProMax };
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { } }

  var FORCADO = /[?&]roleta=1/.test(location.search);
  var HOJE = new Date().toISOString().slice(0, 10);
  function podeAbrir() {
    if (FORCADO) return true;
    if (jaFoiPraCheckout) return false;                       // já clicou em comprar
    if (CFG.umaVezPorDia && S.vistoEm === HOJE) return false;  // já viu hoje
    return true;
  }

  var jaFoiPraCheckout = false;
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href*="hotmart"]');
    if (a && !a.closest('#rlt')) jaFoiPraCheckout = true;
  }, true);

  /* ---------- link de checkout: herda o da página (preserva sck/hdA/hdB/utm) ---------- */
  function linkBase() {
    var a = document.querySelector('a[href*="pay.hotmart.com"]');
    return a ? a.href : 'https://pay.hotmart.com/M98923280L?checkoutMode=10';
  }
  function link(premio) {
    var u;
    try { u = new URL(linkBase()); } catch (e) { return linkBase(); }
    if (premio && premio.off && premio.off.indexOf('COLE_') !== 0) u.searchParams.set('off', premio.off);
    else u.searchParams.delete('off');
    var sck = u.searchParams.get('sck') || '';
    u.searchParams.set('sck', sck + (sck ? '|' : '') + 'rl' + (premio ? premio.id : 'exp'));
    return u.toString();
  }
  function temOferta(p) { return !p.off || p.off.indexOf('COLE_') !== 0; }

  /* ---------- markup ---------- */
  var byId = {}; CFG.escada.forEach(function (p, i) { p.i = i; byId[p.id] = p; });
  var N = CFG.fatias.length, PASSO = 360 / N;
  var el = {}, girando = false, montado = false;

  var CSS = ''
    + '@import url("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=DM+Sans:wght@400;500;700&display=swap");'
    + '#rlt{--bg:#0b0e13;--line:#242c38;--txt:#f4f5f1;--muted:#8b95a7;--dim:#5c6675;'
    +   '--lime:#b3ff00;--lime2:#8fd400;--ink:#0b0e13;--red:#ff5a5a;'
    +   "--disp:'Space Grotesk',ui-sans-serif,system-ui,sans-serif;--body:'DM Sans',ui-sans-serif,system-ui,sans-serif}"
    + '#rlt,#rlt *{box-sizing:border-box;margin:0;padding:0}'
    + '#rlt{position:fixed;inset:0;z-index:2147483000;display:none;align-items:center;justify-content:center;'
    +   'background:rgba(4,6,10,.86);backdrop-filter:blur(7px);-webkit-backdrop-filter:blur(7px);'
    +   'padding:14px;font-family:var(--body);color:var(--txt);line-height:1.5;opacity:0;transition:opacity .24s ease;'
    +   'overflow-y:auto;-webkit-font-smoothing:antialiased}'
    + '#rlt.on{display:flex;opacity:1}'
    + '#rlt .cx{width:100%;max-width:400px;margin:auto;background:linear-gradient(168deg,#151b24,#0d1218);'
    +   'border:1px solid var(--line);border-radius:24px;padding:22px 18px 20px;text-align:center;position:relative;'
    +   'box-shadow:0 28px 80px rgba(0,0,0,.66),inset 0 1px 0 rgba(255,255,255,.05);'
    +   'transform:translateY(16px) scale(.97);transition:transform .3s cubic-bezier(.18,1.2,.35,1)}'
    + '#rlt.on .cx{transform:none}'
    + '#rlt .x{position:absolute;top:11px;right:13px;width:34px;height:34px;border:0;background:transparent;'
    +   'color:var(--dim);font-size:26px;line-height:1;cursor:pointer;border-radius:50%}'
    + '#rlt .x:hover{color:var(--txt);background:rgba(255,255,255,.06)}'
    + '#rlt .kick{font-family:var(--disp);font-size:10.5px;letter-spacing:.17em;text-transform:uppercase;'
    +   'font-weight:700;color:var(--lime);margin-bottom:9px}'
    + '#rlt h3{font-family:var(--disp);font-size:23px;line-height:1.14;letter-spacing:-.03em;font-weight:700;'
    +   'margin-bottom:7px;text-wrap:balance}'
    + '#rlt h3 span{color:var(--lime)}'
    + '#rlt .sub{font-size:14px;color:var(--muted);max-width:320px;margin:0 auto}'
    + '#rlt .sub b{color:var(--txt);font-weight:700}#rlt .sub s{opacity:.6}'
    + '#rlt .chances{display:flex;gap:7px;justify-content:center;margin:16px 0 2px}'
    + '#rlt .chip{display:flex;align-items:center;gap:5px;padding:5px 11px 5px 7px;border-radius:99px;'
    +   'border:1px solid var(--line);color:var(--dim);font-family:var(--disp);font-size:11px;font-weight:700}'
    + '#rlt .chip i{width:13px;height:13px;border-radius:50%;border:1.5px solid currentColor;display:block}'
    + '#rlt .chip.on{border-color:var(--lime);color:var(--lime);background:rgba(179,255,0,.09)}'
    + '#rlt .chip.used i{background:rgba(179,255,0,.85);border-color:transparent}'
    + '#rlt .stage{position:relative;width:min(252px,64vw);margin:12px auto 0;aspect-ratio:1}'
    + '#rlt .rays{position:absolute;inset:-14%;border-radius:50%;opacity:0;transition:opacity .7s;pointer-events:none;'
    +   'background:radial-gradient(circle,rgba(179,255,0,.22) 42%,rgba(179,255,0,.07) 62%,transparent 72%)}'
    + '#rlt .stage.hot .rays{opacity:.85}'
    + '#rlt svg.whl{width:100%;height:100%;display:block;position:relative;z-index:1}'
    + '#rlt #rltDisc{transform-origin:100px 100px;transition:transform 5.2s cubic-bezier(.1,.72,.06,1)}'
    + '#rlt .hub{position:absolute;left:50%;top:50%;width:23%;height:23%;transform:translate(-50%,-50%);'
    +   'border-radius:50%;z-index:5;cursor:pointer;border:2px solid rgba(179,255,0,.85);'
    +   'background:radial-gradient(circle at 34% 28%,#222b36,#0b0e13);color:var(--lime);'
    +   'font-family:var(--disp);font-size:11.5px;font-weight:700;letter-spacing:.08em;'
    +   'box-shadow:0 0 22px rgba(179,255,0,.28),inset 0 1px 0 rgba(255,255,255,.14)}'
    + '#rlt .hub:active{transform:translate(-50%,-50%) scale(.94)}'
    + '#rlt .hub:disabled{color:var(--dim);border-color:var(--line);box-shadow:none;cursor:default}'
    + '#rlt .ptr{position:absolute;left:50%;top:-3.5%;transform:translateX(-50%);z-index:6;width:9%;'
    +   'filter:drop-shadow(0 3px 5px rgba(0,0,0,.6))}'
    + '#rlt .ticket{position:relative;margin:18px auto 0;background:linear-gradient(165deg,#1a212b,#11161d);'
    +   'border:1px solid rgba(179,255,0,.34);border-radius:20px;padding:22px 18px 18px;display:none;'
    +   'box-shadow:0 20px 50px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.05)}'
    + '#rlt .ticket.show{display:block;animation:rltpop .5s cubic-bezier(.18,1.5,.42,1)}'
    + '@keyframes rltpop{from{opacity:0;transform:scale(.88) translateY(10px)}to{opacity:1;transform:none}}'
    + '#rlt .tk-lbl{font-family:var(--disp);font-size:10px;letter-spacing:.17em;text-transform:uppercase;'
    +   'color:var(--lime);font-weight:700}'
    + '#rlt .tk-val{font-family:var(--disp);font-size:46px;font-weight:700;letter-spacing:-.045em;line-height:1;'
    +   'margin:8px 0 3px;text-shadow:0 0 42px rgba(179,255,0,.3)}'
    + '#rlt .tk-was{color:var(--muted);font-size:13px}#rlt .tk-was s{opacity:.65}'
    + '#rlt .cut{height:1px;margin:15px -18px;border-top:1px dashed rgba(255,255,255,.14)}'
    + '#rlt .timer{font-size:13px;color:var(--muted)}'
    + '#rlt .timer b{font-family:var(--disp);font-variant-numeric:tabular-nums;color:var(--red);'
    +   'font-size:19px;font-weight:700;margin-left:4px}'
    + '#rlt .acoes{display:flex;flex-direction:column;gap:10px;margin-top:14px}'
    + '#rlt .btn{display:block;width:100%;border:0;cursor:pointer;text-decoration:none;text-align:center;'
    +   'border-radius:99px;font-family:var(--disp);font-weight:700;position:relative;overflow:hidden;'
    +   'line-height:1.25;text-wrap:balance;transition:transform .12s,box-shadow .25s}'
    + '#rlt .btn:active{transform:scale(.98)}'
    + '#rlt .btn.pri{order:1;padding:17px 16px;font-size:16px;letter-spacing:.02em;color:var(--ink);'
    +   'background:linear-gradient(180deg,#cfff4d,var(--lime2));'
    +   'box-shadow:0 10px 30px rgba(179,255,0,.34),inset 0 1px 0 rgba(255,255,255,.5)}'
    + '#rlt .btn.sec{order:2;padding:13px 14px;font-size:13.5px;color:var(--muted);'
    +   'background:transparent;border:1px solid var(--line);font-weight:500}'
    + '#rlt .fine{font-size:12px;color:var(--dim);margin-top:11px;line-height:1.45}'
    + '@keyframes rltlamp{0%,100%{opacity:.16}50%{opacity:1;filter:drop-shadow(0 0 3px #b3ff00)}}'
    + '@media (prefers-reduced-motion:reduce){#rlt #rltDisc{transition-duration:.7s}#rlt,#rlt .cx,#rlt .rays{transition:none;animation:none}}';

  function montar() {
    if (montado) return; montado = true;
    var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
    var d = document.createElement('div'); d.id = 'rlt'; d.setAttribute('role', 'dialog');
    d.setAttribute('aria-modal', 'true'); d.setAttribute('aria-label', 'Gire e descubra o preço do seu ingresso');
    d.innerHTML =
      '<div class="cx">' +
      '<button class="x" id="rltX" aria-label="Fechar">&times;</button>' +
      '<p class="kick">antes de você ir</p>' +
      '<h3 id="rltH">Gire e descubra <span>o preço do seu ingresso</span></h3>' +
      '<p class="sub" id="rltS">O ingresso custa <s>' + CFG.precoCheio + '</s>. Você tem até <b>3 giros</b> para chegar em <b>R$ 29</b>.</p>' +
      '<div class="chances" id="rltChips"></div>' +
      '<div class="stage" id="rltStage">' +
        '<div class="rays"></div>' +
        '<svg class="ptr" viewBox="0 0 24 30" aria-hidden="true"><path d="M12 30 L1 6 A12 12 0 0 1 23 6 Z" fill="#b3ff00"/>' +
        '<circle cx="12" cy="9" r="3.4" fill="#0b0e13" opacity=".55"/></svg>' +
        '<svg class="whl" viewBox="0 0 200 200" aria-hidden="true">' +
          '<defs>' +
            '<radialGradient id="rltRim" cx="35%" cy="22%"><stop offset="0" stop-color="#4a5563"/>' +
            '<stop offset=".55" stop-color="#242c37"/><stop offset="1" stop-color="#0e1218"/></radialGradient>' +
            '<linearGradient id="rltMax" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d8ff5e"/>' +
            '<stop offset="1" stop-color="#8fd400"/></linearGradient>' +
            '<linearGradient id="rltMid" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3d4757"/>' +
            '<stop offset="1" stop-color="#2b3340"/></linearGradient>' +
            '<linearGradient id="rltLow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#232b36"/>' +
            '<stop offset="1" stop-color="#171d25"/></linearGradient>' +
            '<radialGradient id="rltGlass" cx="32%" cy="20%" r="72%"><stop offset="0" stop-color="#fff" stop-opacity=".16"/>' +
            '<stop offset=".55" stop-color="#fff" stop-opacity=".03"/><stop offset="1" stop-color="#000" stop-opacity=".17"/></radialGradient>' +
          '</defs>' +
          '<circle cx="100" cy="100" r="99" fill="url(#rltRim)"/>' +
          '<circle cx="100" cy="100" r="99" fill="none" stroke="rgba(255,255,255,.10)" stroke-width="1"/>' +
          '<g id="rltBulbs"></g>' +
          '<circle cx="100" cy="100" r="86.5" fill="none" stroke="rgba(0,0,0,.5)" stroke-width="3"/>' +
          '<g id="rltDisc"></g>' +
          '<circle cx="100" cy="100" r="85" fill="url(#rltGlass)" pointer-events="none"/>' +
        '</svg>' +
        '<button class="hub" id="rltHub">GIRAR</button>' +
      '</div>' +
      '<div class="ticket" id="rltTk">' +
        '<div class="tk-lbl" id="rltTkL">Seu preço agora</div>' +
        '<div class="tk-val" id="rltTkV">—</div>' +
        '<div class="tk-was" id="rltTkW"></div>' +
        '<div class="cut"></div>' +
        '<div class="timer" id="rltTkT"></div>' +
        '<div class="acoes">' +
          '<a class="btn pri" id="rltCta" href="#" style="display:none">Garantir meu ingresso</a>' +
          '<button class="btn sec" id="rltAgain" style="display:none">Quero girar de novo</button>' +
        '</div>' +
        '<p class="fine" id="rltFine"></p>' +
      '</div>' +
      '</div>';
    document.body.appendChild(d);
    ['rltX', 'rltHub', 'rltChips', 'rltTk', 'rltTkL', 'rltTkV', 'rltTkW', 'rltTkT', 'rltCta', 'rltAgain', 'rltFine', 'rltH', 'rltS']
      .forEach(function (id) { el[id.replace('rlt', '').toLowerCase() || 'root'] = document.getElementById(id); });
    el.root = d;
    desenhar(); chips();
    el.x.onclick = fechar;
    d.addEventListener('click', function (e) { if (e.target === d) fechar(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && d.classList.contains('on')) fechar(); });
    el.hub.onclick = girar;
    el.again.onclick = function () { el.tk.classList.remove('show'); setTimeout(girar, 140); };
    el.cta.addEventListener('click', function () {
      px('InitiateCheckout', { value: S.nivel >= 0 ? CFG.escada[S.nivel].num : 29 });
    });
  }

  function pt(a, r) { var d = (a - 90) * Math.PI / 180; return [100 + r * Math.cos(d), 100 + r * Math.sin(d)]; }
  function desenhar() {
    var fill = { '29': 'url(#rltMax)', '47': 'url(#rltMid)', '97': 'url(#rltLow)' };
    var cor = { '29': '#0b0e13', '47': '#e6ebf2', '97': '#9aa5b5' };
    var s = '';
    for (var i = 0; i < N; i++) {
      var id = CFG.fatias[i], p = byId[id], max = !!p.max;
      var a0 = i * PASSO, a1 = a0 + PASSO, q0 = pt(a0, 85), q1 = pt(a1, 85);
      s += '<path d="M100 100 L' + q0[0].toFixed(2) + ' ' + q0[1].toFixed(2) + ' A85 85 0 0 1 ' +
        q1[0].toFixed(2) + ' ' + q1[1].toFixed(2) + ' Z" fill="' + fill[id] +
        '" stroke="rgba(0,0,0,.45)" stroke-width="1.1"/>';
      var mid = a0 + PASSO / 2, tp = pt(mid, 54), sp2 = pt(mid, 76);
      var ang = (mid > 90 && mid < 270) ? mid + 180 : mid;
      s += '<text x="' + tp[0].toFixed(2) + '" y="' + tp[1].toFixed(2) + '" fill="' + cor[id] +
        '" font-family="Space Grotesk, sans-serif" font-size="' + (max ? 15 : 12.5) +
        '" font-weight="700" letter-spacing="-.4" text-anchor="middle" dominant-baseline="middle"' +
        ' transform="rotate(' + ang + ' ' + tp[0].toFixed(2) + ' ' + tp[1].toFixed(2) + ')">' +
        '<tspan font-size="8" font-weight="500" opacity=".62">R$ </tspan>' + p.id + '</text>';
      if (max) {
        s += '<text x="' + sp2[0].toFixed(2) + '" y="' + sp2[1].toFixed(2) + '" fill="#0b0e13" font-size="10"' +
          ' opacity=".7" text-anchor="middle" dominant-baseline="middle" transform="rotate(' + ang + ' ' +
          sp2[0].toFixed(2) + ' ' + sp2[1].toFixed(2) + ')">&#9733;</text>';
      }
    }
    document.getElementById('rltDisc').innerHTML = s;
    var b = '';
    for (var k = 0; k < 20; k++) {
      var bp = pt(k * 18, 92.5);
      b += '<circle cx="' + bp[0].toFixed(2) + '" cy="' + bp[1].toFixed(2) + '" r="2.5" fill="#b3ff00"' +
        ' style="animation:rltlamp 1.4s ' + (k * .07).toFixed(2) + 's infinite"/>';
    }
    document.getElementById('rltBulbs').innerHTML = b;
  }
  function chips() {
    var h = '';
    for (var i = 0; i < CFG.chances; i++) {
      var usado = i < S.giros;
      h += '<span class="chip' + (usado ? ' used' : ' on') + '"><i></i>' + (i + 1) + '\u00ba giro</span>';
    }
    el.chips.innerHTML = h;
  }
  // fatias que valem como alvo: as do prêmio, ou as vizinhas de um prêmio (parece "quase")
  function alvos(id) {
    var max = [], perto = [];
    CFG.fatias.forEach(function (x, i) {
      if (x !== id) return;
      if (byId[id].max) { max.push(i); return; }
      var e = byId[CFG.fatias[(i + N - 1) % N]].max, d = byId[CFG.fatias[(i + 1) % N]].max;
      (e || d ? perto : max).push(i);
    });
    return perto.length ? perto : max;
  }
  function proximoNivel() {
    if (S.giros === 0) return 0;                                  // 1º giro nunca dá o máximo
    if (S.giros === 1) return S.pula ? CFG.escada.length - 1 : 1;
    return CFG.escada.length - 1;
  }

  var giroAcum = 0;
  function girar() {
    if (girando || S.fechado || S.giros >= CFG.chances) return;
    girando = true; el.hub.disabled = true; el.again.style.display = 'none'; el.tk.classList.remove('show');
    var nivel = proximoNivel(), premio = CFG.escada[nivel];
    var lista = alvos(premio.id), alvo = lista[Math.floor(Math.random() * lista.length)];
    var centro = alvo * PASSO + PASSO / 2;
    var atual = ((giroAcum % 360) + 360) % 360;
    giroAcum += (360 * 5) + (((360 - centro) - atual) % 360);
    document.getElementById('rltDisc').style.transform = 'rotate(' + giroAcum + 'deg)';
    document.getElementById('rltStage').classList.add('hot');
    px('RoletaGiro', { giro: S.giros + 1 });
    setTimeout(function () {
      girando = false; S.giros++; S.nivel = nivel;
      S.fechado = !!premio.max || S.giros >= CFG.chances;
      if (S.fechado && !S.prazo) S.prazo = Date.now() + CFG.minutosDeReserva * 60000;
      save(); chips(); mostrar(premio);
    }, 5250);
  }

  function mostrar(premio) {
    var falta = CFG.chances - S.giros, ok = temOferta(premio);
    el.tk.classList.add('show');
    el.tkl.textContent = premio.max ? 'Melhor preço liberado' : 'Seu preço agora';
    el.tkv.textContent = premio.label;
    el.tkw.innerHTML = premio.max ? 'no lugar de <s>' + CFG.precoCheio + '</s>' : '';
    el.cta.href = link(premio);
    if (S.fechado) {
      el.hub.style.display = 'none'; el.again.style.display = 'none';
      el.cta.style.display = ok ? 'block' : 'none';
      el.cta.className = 'btn pri';
      el.cta.textContent = 'Garantir meu ingresso por ' + premio.label.replace(' ', ' ');
      el.fine.textContent = ok ? 'Vale só nesta visita.' : 'Preço indisponível no momento.';
      relogio();
    } else {
      el.hub.disabled = false;
      el.again.style.display = 'block';
      el.again.textContent = falta === 1 ? 'Quero meu último giro' : 'Quero girar de novo (faltam ' + falta + ')';
      el.cta.style.display = ok ? 'block' : 'none';
      el.cta.className = 'btn sec';
      el.cta.textContent = 'Prefiro parar aqui e pagar ' + premio.label.replace(' ', ' ');
      el.fine.textContent = 'Você ainda pode melhorar esse preço.';
    }
    px('RoletaPremio', { value: premio.num, content_name: premio.label, giro: S.giros });
  }

  var relogioOn = false;
  function relogio() {
    if (relogioOn) return; relogioOn = true;
    (function t() {
      var s = Math.max(0, Math.round((S.prazo - Date.now()) / 1000));
      el.tkt.innerHTML = 'Reservado por <b>' + ((s / 60) | 0) + ':' + ('0' + (s % 60)).slice(-2) + '</b>';
      if (s > 0) return setTimeout(t, 1000);
      S.fechado = true; save();
      el.tkt.textContent = 'A reserva expirou.';
      el.tkl.textContent = 'Preço normal'; el.tkv.textContent = CFG.precoCheio; el.tkw.textContent = '';
      el.cta.href = link(null); el.cta.textContent = 'Continuar mesmo assim';
    })();
  }

  function px(nome, extra) {
    try {
      if (typeof fbq === 'function') fbq('trackSingleCustom', '1665265050801984', nome,
        Object.assign({ currency: 'BRL', source: 'roleta-pv' }, extra || {}));
    } catch (e) { }
  }

  /* ---------- abrir / fechar ---------- */
  var aberto = false;
  function abrir(motivo) {
    if (aberto || !podeAbrir()) return;
    montar(); aberto = true;
    S.vistoEm = HOJE; S.visto++; save();
    el.root.classList.add('on');
    document.documentElement.style.overflow = 'hidden';
    px('RoletaAbriu', { motivo: motivo });
  }
  function fechar() {
    if (!aberto) return; aberto = false;
    el.root.classList.remove('on');
    document.documentElement.style.overflow = '';
    px('RoletaFechou', { giros: S.giros });
  }

  /* ---------- GATILHOS ----------
     91% do tráfego é mobile e 78% está no navegador do Instagram/Facebook.
     Por isso mouseleave é o gatilho MENOS importante aqui.                     */
  var t0 = Date.now(), ultimo = Date.now(), armado = false, ultY = 0;
  function maduro() { return (Date.now() - t0) / 1000 >= CFG.segundosNaPagina; }
  function toque() { ultimo = Date.now(); }
  ['touchstart', 'touchmove', 'scroll', 'keydown', 'click', 'pointerdown'].forEach(function (ev) {
    window.addEventListener(ev, toque, { passive: true });
  });

  // 1. inatividade depois de um tempo de página
  setInterval(function () {
    if (!maduro()) return;
    if ((Date.now() - ultimo) / 1000 >= CFG.segundosParado) abrir('parado');
  }, 2000);

  // 2. scroll pra cima rápido (sinal de saída no mobile)
  window.addEventListener('scroll', function () {
    var y = window.scrollY || 0;
    if (maduro() && ultY - y >= CFG.scrollUpPx) abrir('scroll-cima');
    ultY = y;
  }, { passive: true });

  // 3. voltou pra aba depois de sair (troca de app no celular)
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'visible' && maduro()) abrir('voltou');
  });

  // 4. botão voltar (funciona no Chrome mobile; instável no WebView do IG/FB)
  if (CFG.usarBotaoVoltar) {
    try {
      history.pushState({ rlt: 1 }, '');
      window.addEventListener('popstate', function () {
        if (!aberto && podeAbrir()) { history.pushState({ rlt: 1 }, ''); abrir('voltar'); }
      });
    } catch (e) { }
  }

  // 5. mouse saindo pelo topo (só desktop, 7,5% do tráfego)
  document.addEventListener('mouseout', function (e) {
    if (!e.relatedTarget && e.clientY <= 0 && maduro()) abrir('mouse-saiu');
  });

  // revisão
  if (FORCADO) { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { abrir('forcado'); }); else abrir('forcado'); }
  window.__roleta = { abrir: abrir, fechar: fechar, cfg: CFG, reset: function () { try { localStorage.removeItem(KEY); } catch (e) { } location.reload(); } };
})();
