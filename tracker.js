// MTBB tracker — eventos de funil enviados pro Supabase
// Eventos: quiz_view | stage_click | hotmart_click | form_submit | whatsapp_click | purchase (via webhook)
// Auto-detecta stage + variant a partir do filename da página
// Exposed: window.MTBB_TRACK(eventType, extra)

(function () {
  var SUPABASE_URL = 'https://jsqtpsxpaclslakafmvd.supabase.co';
  var SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpzcXRwc3hwYWNsc2xha2FmbXZkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUzMTY5NTMsImV4cCI6MjA5MDg5Mjk1M30.6f3CmgozaE3fTORF0SBSeRDzZNZ1E27tcdQ9h6tKLgc';
  var ENDPOINT = SUPABASE_URL + '/rest/v1/mtbb_pv_events';

  function rand() { return Math.random().toString(36).substr(2, 10); }

  function getVisitorId() {
    try {
      var v = localStorage.getItem('mtbb_visitor');
      if (!v) {
        v = 'v_' + rand() + Date.now().toString(36);
        localStorage.setItem('mtbb_visitor', v);
      }
      return v;
    } catch (e) { return 'v_anon_' + Date.now(); }
  }

  function getSessionId() {
    try {
      var s = sessionStorage.getItem('mtbb_session');
      if (!s) {
        s = 's_' + rand() + Date.now().toString(36);
        sessionStorage.setItem('mtbb_session', s);
      }
      return s;
    } catch (e) { return 's_anon_' + Date.now(); }
  }

  // Captura UTMs/click-ids da URL, persiste (sobrevive à navegação) e retorna sempre.
  var UTM_KEYS = ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','utm_test','utm_id','fbclid','gclid','ttclid','xcod','sck'];
  function getUTMs() {
    var stored = {};
    try { stored = JSON.parse(localStorage.getItem('mtbb_utms') || '{}') || {}; } catch (e) {}
    var params = new URLSearchParams(window.location.search);
    var fromUrl = {}, hasAny = false;
    UTM_KEYS.forEach(function (k) {
      var v = params.get(k);
      if (v) { fromUrl[k] = v; hasAny = true; }
    });
    if (hasAny) {
      var merged = {};
      UTM_KEYS.forEach(function (k) { if (stored[k]) merged[k] = stored[k]; });
      UTM_KEYS.forEach(function (k) { if (fromUrl[k]) merged[k] = fromUrl[k]; });
      try { localStorage.setItem('mtbb_utms', JSON.stringify(merged)); } catch (e) {}
      return merged;
    }
    return stored;
  }
  window.MTBB_UTMS = getUTMs;

  function detectStageVariant() {
    var file = (window.location.pathname.split('/').pop() || 'index.html').toLowerCase();
    var m = file.match(/^(escrevendo|lancando|publicado)(-lista)?\.html$/);
    if (m) return { stage: m[1], variant: m[2] ? 'lista' : 'preco' };
    if (file.indexOf('obrigado-') === 0) {
      var params = new URLSearchParams(window.location.search);
      var ut = params.get('utm_test') || '';
      var um = ut.match(/^(preco|lista)-(escrevendo|lancando|publicado)$/);
      if (um) return { stage: um[2], variant: um[1] };
    }
    return { stage: null, variant: null };
  }

  // Mapeia eventos do funil pro Meta Pixel (pixel.js init os 2 IDs + PageView)
  function firePixel(eventType, variant) {
    if (typeof window.fbq !== 'function') return;
    if (eventType === 'form_submit') {
      // página de venda não tem lead, só venda → InitiateCheckout; lista de espera = Lead
      if (variant === 'checkout') window.fbq('track', 'InitiateCheckout');
      else window.fbq('track', 'Lead');
    } else if (eventType === 'whatsapp_click') {
      window.fbq('track', 'Contact');
    }
  }

  // Mapeia eventos do funil pro Google (GA4 + Ads via gtag.js)
  function fireGtag(eventType, variant) {
    if (typeof window.gtag !== 'function') return;
    if (eventType === 'form_submit') {
      if (variant === 'checkout') window.gtag('event', 'begin_checkout');
      else window.gtag('event', 'generate_lead');
    } else if (eventType === 'whatsapp_click') {
      window.gtag('event', 'contact');
    }
  }

  function track(eventType, extra) {
    extra = extra || {};
    var utms = (window.MTBB_UTMS && window.MTBB_UTMS()) || {};
    var auto = detectStageVariant();
    var meta = extra.meta || {};
    if (window.MTBB_OBRIGADO_VARIANT && !meta.obrigado_variant) meta.obrigado_variant = window.MTBB_OBRIGADO_VARIANT;
    var payload = {
      event_type: eventType,
      stage: (extra.stage !== undefined) ? extra.stage : auto.stage,
      variant: (extra.variant !== undefined) ? extra.variant : auto.variant,
      session_id: getSessionId(),
      visitor_id: getVisitorId(),
      utm_test: utms.utm_test || null,
      utm_source: utms.utm_source || null,
      utm_medium: utms.utm_medium || null,
      utm_campaign: utms.utm_campaign || null,
      utm_content: utms.utm_content || null,
      utm_term: utms.utm_term || null,
      fbclid: utms.fbclid || null,
      gclid: utms.gclid || null,
      referrer: document.referrer || null,
      user_agent: (navigator.userAgent || '').substr(0, 240),
      page: window.location.pathname,
      meta: meta
    };
    try { firePixel(eventType, payload.variant); } catch (e) {}
    try { fireGtag(eventType, payload.variant); } catch (e) {}
    try {
      fetch(ENDPOINT, {
        method: 'POST',
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': 'Bearer ' + SUPABASE_KEY,
          'Content-Type': 'application/json',
          'Prefer': 'return=minimal'
        },
        body: JSON.stringify(payload),
        keepalive: true
      });
    } catch (e) {}
  }

  window.MTBB_TRACK = track;

  // Auto-fire: quiz_view no index
  function autoFire() {
    var file = (window.location.pathname.split('/').pop() || '').toLowerCase();
    if (file === '' || file === 'index.html') {
      track('quiz_view');
    }
    if (window.MTBB_OBRIGADO_VARIANT) {
      track('obrigado_view');
    }
    // ViewContent nas páginas de venda (preço e lista)
    if (/^(escrevendo|lancando|publicado)(-lista)?\.html$/.test(file)) {
      if (typeof window.fbq === 'function') window.fbq('track', 'ViewContent');
      if (typeof window.gtag === 'function') window.gtag('event', 'view_item');
    }
  }

  // Hooks automáticos: hotmart_click, whatsapp_click
  function hookClicks() {
    document.addEventListener('click', function (e) {
      var a = e.target && e.target.closest && e.target.closest('a[href]');
      if (!a) return;
      var href = a.getAttribute('href') || '';
      if (href.indexOf('pay.hotmart.com') >= 0) {
        track('hotmart_click');
      } else if (href.indexOf('api.whatsapp.com') >= 0 || href.indexOf('wa.me') >= 0) {
        track('whatsapp_click');
      }
    }, true);
  }

  function init() {
    autoFire();
    hookClicks();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
