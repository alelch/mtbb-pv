/* ============================================================
   OFERTA — motor do upsell do 90D (Diagnóstico do Autor).

   O que ele faz, e por quê:

   1. REPASSE DA QUERY STRING. A cadeia de 1 clique da Hotmart identifica o
      comprador por parâmetros que chegam na URL desta página. Se a gente
      perder esses parâmetros no caminho (no redirect do teste ou no link de
      saída), o clique deixa de ser "1 clique" e a pessoa cai num checkout
      pedindo cartão de novo, que é exatamente o que esta página evita.
      Por isso TUDO que sai daqui sai com a query string colada.

   2. SPLIT DO TESTE DE PREÇO, POR REDIRECT. A página A sorteia 50/50 e manda
      metade para a B. A B não sorteia nada (redirect nas duas = loop por
      construção, incidente real de 23/07) e FORÇA a variante, para quem cair
      direto nela não sair carimbado como A vendo o preço de B.
      O checkout é FIXO no HTML de cada página. Nunca trocar href em runtime:
      foi override de href que apagou o xcod da VTurb na master em 01/08, e
      esta página vai ter player com botão de compra.

   3. MARCADOR NO SCK. A venda sai carimbada com `pdA` ou `pdB`, que é como o
      dash separa os dois braços depois.

   4. TRAVA. Enquanto OFERTA.AO_VIVO for false, o botão avisa em vez de
      navegar. Hoje os dois checkouts respondem "Produto indisponível".
   ============================================================ */
(function(){
  var CFG = window.OFERTA || {};
  var VAR = CFG.variante || 'A';
  var TAG = CFG.sckTag || 'pd';
  var COOKIE = 'l90d_pd';

  function ck(n, v, dias){
    if (v === undefined){
      var m = document.cookie.match('(^|;)\\s*' + n + '\\s*=\\s*([^;]+)');
      return m ? decodeURIComponent(m[2]) : null;
    }
    var e = new Date(); e.setTime(e.getTime() + dias * 864e5);
    document.cookie = n + '=' + encodeURIComponent(v) + ';expires=' + e.toUTCString() + ';path=/;SameSite=Lax';
  }

  /* ---------- 1. SPLIT ----------
     Roda antes de tudo. Na A, sorteia e pode sair da página; na B, só fixa. */
  (function split(){
    if (VAR === 'B'){ ck(COOKIE, 'B', 30); return; }        /* a B nunca redireciona */
    var v = ck(COOKIE);
    if (!v){ v = Math.random() < 0.5 ? 'A' : 'B'; ck(COOKIE, v, 30); }
    if (v === 'B' && CFG.outraUrl && CFG.AO_VIVO){
      /* a query string TEM que ir junto: é ela que carrega o comprador */
      location.replace(CFG.outraUrl + location.search + location.hash);
    }
  })();

  function comQuery(base){
    if (!base) return base;
    if (!location.search) return base;
    var u; try { u = new URL(base, location.href); } catch(e){ return base; }
    new URLSearchParams(location.search).forEach(function(v, k){
      if (!u.searchParams.get(k)) u.searchParams.set(k, v);
    });
    return u.toString();
  }

  /* carimba a variante no sck, que é como o dash separa os dois braços */
  function comMarcador(url){
    var u; try { u = new URL(url, location.href); } catch(e){ return url; }
    if (!/^https?:\/\/pay\.hotmart\.com/.test(u.origin + u.pathname)) return u.toString();
    var marcador = TAG + VAR;
    var sck = u.searchParams.get('sck') || '';
    if (sck.indexOf(marcador) === -1) u.searchParams.set('sck', sck ? sck + '|' + marcador : marcador);
    return u.toString();
  }

  function destino(url){ return comMarcador(comQuery(url)); }

  function avisa(el, texto){
    el.textContent = texto;
    el.style.pointerEvents = 'none';
    el.style.opacity = '.6';
  }

  function vai(url, evento, el){
    if (!CFG.AO_VIVO){ avisa(el, 'Checkout ainda não publicado'); return; }
    if (!url || /SUBSTITUIR/.test(url)){ avisa(el, 'Link ainda não configurado'); return; }
    try { if (window.fbq) fbq('track', evento,
      {content_ids:[CFG.sku], content_type:'product', currency:'BRL', value:CFG.valor}); } catch(e){}
    try { if (window.MTBB_TRACK) MTBB_TRACK('oferta_click',
      {acao:evento, produto:CFG.sku, variante:VAR}); } catch(e){}
    window.location.href = destino(url);
  }

  document.addEventListener('click', function(ev){
    var a = ev.target.closest('[data-aceita],[data-recusa]');
    if (!a) return;
    ev.preventDefault();
    if (a.hasAttribute('data-aceita')) vai(CFG.aceite, 'InitiateCheckout', a);
    else                               vai(CFG.recusa, 'ViewContent', a);
  });

  /* href real nos botões: serve pro clique do meio, pro "copiar endereço do
     link" e pra quem estiver sem JS. O clique normal remonta na hora. */
  if (CFG.AO_VIVO){
    document.querySelectorAll('[data-aceita]').forEach(function(a){
      if (CFG.aceite && !/SUBSTITUIR/.test(CFG.aceite)) a.setAttribute('href', destino(CFG.aceite));
    });
    document.querySelectorAll('a[data-recusa]').forEach(function(a){
      if (CFG.recusa && !/SUBSTITUIR/.test(CFG.recusa)) a.setAttribute('href', destino(CFG.recusa));
    });
  }

  try { if (window.fbq) fbq('track','ViewContent',
    {content_ids:[CFG.sku], content_type:'product', currency:'BRL', value:CFG.valor}); } catch(e){}
})();
