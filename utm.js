// UTM propagation — MTBB
// 1) Captura UTMs da URL atual
// 2) Persiste em sessionStorage (sobrevive navegação interna)
// 3) Anexa em todos os links externos automaticamente (ex: Hotmart)
// 4) Expõe window.MTBB_UTMS() para uso em forms

(function () {
  var UTM_KEYS = [
    'utm_source', 'utm_medium', 'utm_campaign',
    'utm_content', 'utm_term', 'utm_id',
    'gclid', 'fbclid', 'ttclid', 'xcod', 'sck'
  ];

  function captureUTMs() {
    var params = new URLSearchParams(window.location.search);
    var stored = {};
    try { stored = JSON.parse(sessionStorage.getItem('mtbb_utm') || '{}'); } catch (e) {}
    UTM_KEYS.forEach(function (k) {
      var v = params.get(k);
      if (v) stored[k] = v;
    });
    try { sessionStorage.setItem('mtbb_utm', JSON.stringify(stored)); } catch (e) {}
    return stored;
  }

  function utmQueryString(utms) {
    var parts = [];
    UTM_KEYS.forEach(function (k) {
      if (utms[k]) parts.push(encodeURIComponent(k) + '=' + encodeURIComponent(utms[k]));
    });
    return parts.join('&');
  }

  function decorateLinks(utms) {
    var qs = utmQueryString(utms);
    if (!qs) return;
    document.querySelectorAll('a[href]').forEach(function (a) {
      var href = a.getAttribute('href');
      if (!href) return;
      if (href.startsWith('#') || href.startsWith('mailto:') ||
          href.startsWith('tel:') || href.startsWith('javascript:')) return;
      if (a.classList.contains('open-modal')) return;
      if (/[?&]utm_/.test(href)) return;
      var sep = href.indexOf('?') >= 0 ? '&' : '?';
      a.setAttribute('href', href + sep + qs);
    });
  }

  function init() {
    var utms = captureUTMs();
    decorateLinks(utms);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // expõe pra forms (modal) lerem as UTMs no submit
  window.MTBB_UTMS = function () {
    try { return JSON.parse(sessionStorage.getItem('mtbb_utm') || '{}'); }
    catch (e) { return {}; }
  };
})();
