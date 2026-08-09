// MTBB tracker — eventos de funil enviados pro Supabase
// Eventos: quiz_view | stage_click | hotmart_click | form_submit | whatsapp_click | purchase (via webhook)
// Auto-detecta stage + variant a partir do filename da página
// Exposed: window.MTBB_TRACK(eventType, extra)

(function () {
  // Preview do dashboard (?preview=1): não registra nada, pra não poluir as métricas do A/B.
  try { if (new URLSearchParams(location.search).get('preview')) { window.MTBB_TRACK = function () {}; return; } } catch (e) {}
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
  var UTM_KEYS = ['utm_source','utm_medium','utm_campaign','utm_content','utm_term','utm_test','utm_id','fbclid','gclid','ttclid','xcod','sck','src'];
  // Origem do tráfego SEM UTM (mesma ideia do evento especial): 1º toque sem src/utm_source
  // ganha um src derivado do referrer/click-id, que viaja pro PV, form e checkout.
  // fbclid sem UTM = anúncio Meta que perdeu o carimbo → 'meta-fbclid' (sinal de PAGO).
  function deriveOrigem(fbclid, gclid) {
    if (fbclid) return 'meta-fbclid';
    if (gclid) return 'google-gads';
    try {
      var r = document.referrer || '';
      if (!r) return 'org-direto';
      var h = new URL(r).hostname.replace(/^www\./, '').toLowerCase();
      if (h.indexOf('metodo.thebookbusiness') >= 0) return '';      // navegação interna: não carimba
      if (h.indexOf('instagram') >= 0) return 'org-instagram';
      if (h.indexOf('facebook') >= 0 || h === 'fb.com' || h === 'fb.me') return 'org-facebook';
      if (h.indexOf('google') >= 0) return 'org-google';
      if (h.indexOf('youtube') >= 0) return 'org-youtube';
      if (h.indexOf('tiktok') >= 0) return 'org-tiktok';
      if (h === 't.co' || h.indexOf('twitter') >= 0 || h === 'x.com') return 'org-twitter';
      if (h.indexOf('thebookbusiness') >= 0) return 'org-site';     // site/blog principal
      return 'org-ref-' + h.replace(/[^a-z0-9.]/g, '').slice(0, 20);
    } catch (e) { return 'org-direto'; }
  }
  function getUTMs() {
    var stored = {};
    try { stored = JSON.parse(localStorage.getItem('mtbb_utms') || '{}') || {}; } catch (e) {}
    var params = new URLSearchParams(window.location.search);
    var fromUrl = {}, hasAny = false;
    UTM_KEYS.forEach(function (k) {
      var v = params.get(k);
      if (v) { fromUrl[k] = v; hasAny = true; }
    });
    var merged = stored;
    if (hasAny) {
      merged = {};
      UTM_KEYS.forEach(function (k) { if (stored[k]) merged[k] = stored[k]; });
      UTM_KEYS.forEach(function (k) { if (fromUrl[k]) merged[k] = fromUrl[k]; });
    }
    // sem src e sem utm_source (nem agora nem guardado) → carimba a origem no 1º toque
    if (!merged.src && !merged.utm_source) {
      var org = deriveOrigem(merged.fbclid, merged.gclid);
      if (org) { merged.src = org; hasAny = true; }
    }
    if (hasAny) { try { localStorage.setItem('mtbb_utms', JSON.stringify(merged)); } catch (e) {} }
    return merged;
  }
  window.MTBB_UTMS = getUTMs;

  function detectStageVariant() {
    var file = (window.location.pathname.split('/').pop() || 'index.html').toLowerCase();
    var m = file.match(/^(escrevendo|lancando|publicado)(-lista)?(\.html)?$/);
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
      if (variant === 'checkout') window.fbq('track', 'InitiateCheckout', { content_type: 'product', content_ids: ['PPTO'], currency: 'BRL', value: 2500 });
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
    if (window.MTBB_QUIZ_VARIANT && !meta.quiz_variant) meta.quiz_variant = window.MTBB_QUIZ_VARIANT;
    if (window.MTBB_QUIZ_COPY && !meta.quiz_copy) meta.quiz_copy = window.MTBB_QUIZ_COPY;
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
    if (file === '' || file === 'index.html' || file === 'index') {
      // Se o head adiou a decisão de copy (visitante novo sem config), espera o footer
      // finalizar antes de contar o quiz_view, senao o evento sai com o copy provisorio.
      var fireQV = function () { if (!window.__mtbbQVfired) { window.__mtbbQVfired = 1; track('quiz_view'); } };
      if (window.MTBB_QUIZ_COPY_DEFER) {
        window.MTBB_QUIZVIEW_READY = fireQV;
        setTimeout(fireQV, 3000);
      } else {
        fireQV();
      }
    }
    if (window.MTBB_OBRIGADO_VARIANT) {
      track('obrigado_view');
    }
    // ViewContent nas páginas de venda (preço e lista)
    if (/^(escrevendo|lancando|publicado)(-lista)?(\.html)?$/.test(file)) {
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
