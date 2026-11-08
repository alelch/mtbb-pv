// Google Analytics 4 (G-FB4Q08G55Z). <head> das páginas públicas.
// (Google Ads removido: não há campanha no Ads.) Eventos do funil disparam pelo tracker.js (GA4).
// PERF: o stub gtag() é síncrono (js/config/eventos vão pro dataLayer); o gtag/js (pesado) só
// carrega no requestIdleCallback (ou no 1º gesto), saindo do load crítico do mobile. O dataLayer
// é processado quando o script carrega.
window.dataLayer = window.dataLayer || [];
window.gtag = function () { dataLayer.push(arguments); };
gtag('js', new Date());
gtag('config', 'G-FB4Q08G55Z');

(function () {
  var loaded = false;
  function load() {
    if (loaded) return; loaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=G-FB4Q08G55Z';
    document.head.appendChild(s);
  }
  // 08/11: só depois que a página termina de abrir (+2,5 s) ou no 1º toque/clique; a rolagem não dispara mais,
  // porque no celular a pessoa rola logo e o gtag pesado (177 KB) disputava o processador com a abertura.
  ['pointerdown', 'keydown'].forEach(function (ev) {
    window.addEventListener(ev, load, { once: true, passive: true });
  });
  function depois() { setTimeout(function () { if ('requestIdleCallback' in window) requestIdleCallback(load, { timeout: 2000 }); else load(); }, 2500); }
  if (document.readyState === 'complete') depois(); else window.addEventListener('load', depois, { once: true });
})();
