/* ============================================================
   OFERTA — motor compartilhado do upsell e do downsell do 90D.

   O que ele faz, e por quê:

   1. REPASSE DA QUERY STRING. A cadeia de 1 clique da Hotmart identifica o
      comprador por parâmetros que chegam na URL desta página. Se a gente
      perder esses parâmetros no caminho upsell -> downsell -> obrigado, o
      clique deixa de ser "1 clique" e a pessoa cai num checkout pedindo
      cartão de novo, que é exatamente o que essa página existe pra evitar.
      Por isso TODO link de saída sai com a query string inteira colada.

   2. TRAVA DE PLACEHOLDER. Enquanto a URL de aceite tiver "SUBSTITUIR", o
      botão não navega: ele avisa na própria página. Mesma trava do front,
      pelo mesmo motivo (não jogar comprador num link quebrado da Hotmart).

   3. EVENTOS. Pixel dos dois IDs + evento próprio por degrau, pra dar pra
      medir taxa de aceite de cada um separado.
   ============================================================ */
(function(){
  var CFG = window.OFERTA || {};
  var SIM  = CFG.aceite  || '';
  var NAO  = CFG.recusa  || '';
  var SKU  = CFG.sku     || '';
  var VAL  = CFG.valor   || 0;

  /* Cola a query string desta página na URL de destino, sem sobrescrever o
     que o destino já traz escrito nele. */
  function comQuery(base){
    if(!base) return base;
    if(!location.search) return base;
    var aqui = new URLSearchParams(location.search);
    var u;
    try { u = new URL(base, location.href); } catch(e){ return base; }
    aqui.forEach(function(v,k){ if(!u.searchParams.get(k)) u.searchParams.set(k,v); });
    return u.toString();
  }

  function avisaPlaceholder(el){
    el.textContent = 'Link de checkout ainda não configurado';
    el.style.pointerEvents = 'none';
    el.style.opacity = '.6';
  }

  function vai(url, evento, el){
    if(/SUBSTITUIR/.test(url)){ avisaPlaceholder(el); return; }
    try{ if(window.fbq) fbq('track', evento,
      {content_ids:[SKU], content_type:'product', currency:'BRL', value:VAL}); }catch(e){}
    try{ if(window.MTBB_TRACK) MTBB_TRACK('oferta_click',{acao:evento, produto:SKU}); }catch(e){}
    window.location.href = comQuery(url);
  }

  document.addEventListener('click', function(ev){
    var a = ev.target.closest('[data-aceita],[data-recusa]');
    if(!a) return;
    ev.preventDefault();
    if(a.hasAttribute('data-aceita')) vai(SIM, 'InitiateCheckout', a);
    else                              vai(NAO, 'ViewContent', a);
  });

  /* href real nos botões: serve pro clique do meio, pro "copiar endereço do
     link" e pra quem estiver sem JS. O clique normal remonta na hora. */
  document.querySelectorAll('[data-aceita]').forEach(function(a){
    if(SIM && !/SUBSTITUIR/.test(SIM)) a.setAttribute('href', comQuery(SIM));
  });
  document.querySelectorAll('[data-recusa]').forEach(function(a){
    if(NAO && !/SUBSTITUIR/.test(NAO)) a.setAttribute('href', comQuery(NAO));
  });

  try{ if(window.fbq) fbq('track','ViewContent',
    {content_ids:[SKU], content_type:'product', currency:'BRL', value:VAL}); }catch(e){}
})();
