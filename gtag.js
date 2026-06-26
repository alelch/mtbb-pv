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
  ['scroll', 'pointerdown', 'keydown', 'touchstart'].forEach(function (ev) {
    window.addEventListener(ev, load, { once: true, passive: true });
  });
  if ('requestIdleCallback' in window) { requestIdleCallback(load, { timeout: 3000 }); }
  else { setTimeout(load, 2500); }
})();
