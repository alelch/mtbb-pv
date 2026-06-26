// Meta Pixel — MTBB perpétuo (2 pixels). Carregado no <head> das páginas públicas.
// Eventos avançados (Lead / InitiateCheckout / Contact / ViewContent) disparam pelo tracker.js.
// PERF: o stub fbq() é síncrono (init/PageView/eventos ficam na fila); o fbevents.js (pesado)
// só carrega no requestIdleCallback (ou no 1º gesto), saindo do load crítico do mobile.
// A fila é reproduzida quando o fbevents carrega. Conversões continuam medidas via CAPI (servidor).
!function (f, b, e) {
  if (f.fbq) return;
  var n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
  if (!f._fbq) f._fbq = n;
  n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
}(window, document, 'script');

fbq('init', '1665265050801984');
fbq('init', '617884976680212');
fbq('track', 'PageView');

(function () {
  var loaded = false;
  function load() {
    if (loaded) return; loaded = true;
    var t = document.createElement('script');
    t.async = true;
    t.src = 'https://connect.facebook.net/en_US/fbevents.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(t, s);
  }
  ['scroll', 'pointerdown', 'keydown', 'touchstart'].forEach(function (ev) {
    window.addEventListener(ev, load, { once: true, passive: true });
  });
  if ('requestIdleCallback' in window) { requestIdleCallback(load, { timeout: 3000 }); }
  else { setTimeout(load, 2500); }
})();
