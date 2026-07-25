/* mtbb-antigo — interações vanilla (substitui jQuery + Elementor frontend ~400KB)
   Comportamento portado 1:1 da página original thebookbusiness.com.br/v2/ */
(function () {
  'use strict';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- 1. lazy background (.e-con.e-parent) ---------- */
  function lazyBg() {
    var els = $$('.e-con.e-parent:not(.e-lazyloaded)');
    if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.add('e-lazyloaded'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('e-lazyloaded'); io.unobserve(en.target); } });
    }, { rootMargin: '200px' });
    els.forEach(function (e) { io.observe(e); });
  }

  /* ---------- 2. popup (id 31122) ---------- */
  var modal = document.getElementById('elementor-popup-modal-31122');
  function openPopup(e) {
    if (e) e.preventDefault();
    modal.style.display = 'flex';
    var content = $('.dialog-widget-content', modal);
    content.classList.remove('animated', 'fadeInUp'); void content.offsetWidth;
    content.classList.add('animated', 'fadeInUp');
    fillHidden();
    var first = $('input[name="form_fields[name]"]', modal);
    if (first) setTimeout(function () { first.focus(); }, 350);
  }
  function closePopup(e) {
    if (e) e.preventDefault();
    modal.style.display = 'none';
  }
  // original: prevent_close_on_background_click + prevent_close_on_esc_key = só fecha no X
  $$('a[href*="elementor-action"]').forEach(function (a) {
    if (/popup/i.test(decodeURIComponent(a.getAttribute('href')))) a.addEventListener('click', openPopup);
  });
  if (modal) $('.dialog-close-button', modal).addEventListener('click', closePopup);

  /* ---------- 3. form (porta o fluxo do Elementor Pro + WP admin-ajax) ---------- */
  var AJAX = 'https://thebookbusiness.com.br/wp-admin/admin-ajax.php';
  var CHECKOUT = 'https://pay.hotmart.com/B73928367P?off=h0n7diwh&checkoutMode=10';
  var CELULAR_BR = /^[1-9][0-9]9\d{8}$/;
  var form = document.getElementById('iniciou_pre_checkout_v3');

  function urlParam(k) { try { return new URLSearchParams(location.search).get(k) || ''; } catch (e) { return ''; } }
  function fillHidden() {
    if (!form) return;
    var f = function (n) { return form.querySelector('input[name="form_fields[' + n + ']"]'); };
    var domain = location.hostname.split('.')[0];
    var pagePath = location.pathname.replace(/^\/|\/$/g, '').replace(/\//g, '|') || 'mtbb-antigo';
    if (f('dominio')) f('dominio').value = domain;
    if (f('pagina')) f('pagina').value = pagePath;
    ['sck', 'src', 'utm_source'].forEach(function (k) { if (f(k) && !f(k).value) f(k).value = urlParam(k); });
  }

  function mascara(v) {
    v = v.replace(/\D/g, '');
    if (v.length > 11) v = v.slice(0, 11);
    if (v.length > 6) v = v.replace(/^(\d{2})(\d{5})(\d{0,4}).*/, '($1) $2-$3');
    else if (v.length > 2) v = v.replace(/^(\d{2})(\d{0,5}).*/, '($1) $2');
    else if (v.length > 0) v = v.replace(/^(\d{0,2}).*/, '($1');
    return v;
  }
  function digitosLimpos(v) {
    var d = (v || '').replace(/\D/g, '');
    if (d.indexOf('55') === 0 && d.length > 11) d = d.slice(2);
    return d;
  }
  function mostrarErro(campo, msg) {
    campo.setCustomValidity(msg);
    if (campo.reportValidity) campo.reportValidity();
    setTimeout(function () { campo.setCustomValidity(''); }, 3000);
  }

  var tel = form && form.querySelector('input[name="form_fields[telefone]"]');
  if (tel) {
    tel.setAttribute('maxlength', 15); tel.setAttribute('inputmode', 'tel'); tel.setAttribute('autocomplete', 'tel');
    tel.addEventListener('input', function () {
      tel.value = mascara(tel.value);
      try { tel.setSelectionRange(tel.value.length, tel.value.length); } catch (e) { }
    });
    tel.addEventListener('blur', function () {
      var digits = digitosLimpos(tel.value);
      if (!digits.length) return;
      if (!CELULAR_BR.test(digits)) { mostrarErro(tel, 'Celular inválido. Use DDD + 9 + 8 dígitos. Ex: (11) 99999-9999'); return; }
      tel.value = '55' + digits;
    });
  }

  // captura parcial (porta do script original: GET beacon no keyup/blur do email)
  var lastSent = { email: null };
  function isValidEmail(s) { s = String(s || '').trim(); return s.length > 5 && s.indexOf('@') > -1 && s.indexOf('.') > -1; }
  function maybeRequest() {
    var emailEl = form && form.querySelector('input[name="form_fields[email]"]');
    if (!emailEl) return;
    var email = String(emailEl.value || '').trim().toLowerCase();
    if (!isValidEmail(email) || email === lastSent.email) return;
    var p = new URLSearchParams(); p.set('csv_test', '1'); p.set('email', email);
    var nameEl = form.querySelector('input[name="form_fields[name]"]');
    if (nameEl && nameEl.value.trim()) p.set('name', nameEl.value.trim());
    ['sck', 'src', 'utm_source', 'utm_campaign', 'utm_content', 'utm_medium', 'utm_term'].forEach(function (k) {
      var el = form.querySelector('input[name="form_fields[' + k + ']"]');
      var v = el ? el.value : urlParam(k);
      if (v && v.trim()) p.set(k, v.trim());
    });
    new Image().src = 'https://thebookbusiness.com.br/?' + p.toString();
    lastSent.email = email;
  }
  var debT;
  if (form) {
    form.addEventListener('keyup', function (e) {
      if (e.target.name === 'form_fields[email]') { clearTimeout(debT); debT = setTimeout(maybeRequest, 600); }
    });
    form.addEventListener('blur', function (e) {
      if (e.target.name === 'form_fields[email]') maybeRequest();
    }, true);
  }

  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var digits = digitosLimpos(tel ? tel.value : '');
    if (!CELULAR_BR.test(digits)) { mostrarErro(tel, 'Celular inválido. Use DDD + 9 + 8 dígitos. Ex: (11) 99999-9999'); tel.focus(); return; }
    if (tel) tel.value = '55' + digits;
    fillHidden();

    var btn = form.querySelector('button[type="submit"]');
    if (btn) { btn.disabled = true; btn.style.opacity = '.6'; }

    // mesmo POST que o Elementor Pro faria (mantém ações server-side: AC, webhooks)
    var fd = new FormData(form);
    fd.set('action', 'elementor_pro_forms_send_form');
    try { fetch(AJAX, { method: 'POST', body: fd, mode: 'no-cors', keepalive: true }); } catch (err) { }

    // redirect idêntico ao redirect_url do servidor (+ prefill de telefone no formato correto da Hotmart)
    var g = function (n) { var el = form.querySelector('[name="form_fields[' + n + ']"]'); return el ? el.value : ''; };
    var full = '55' + digits;
    var url = CHECKOUT +
      '&src=' + encodeURIComponent(g('dominio') + '|' + g('pagina')) +
      '&sck=' + encodeURIComponent(g('sck')) +
      '&name=' + encodeURIComponent(g('name')) +
      '&email=' + encodeURIComponent(g('email')) +
      '&phoneac=' + digits.slice(0, 2) +
      '&phonenumber=' + digits.slice(2);
    setTimeout(function () { location.href = url; }, 300);
  });

  /* ---------- 4. repassa querystring pros links Hotmart (porta 1:1) ---------- */
  (function () {
    var prefix = ['https://payment.hotmart.com', 'https://pay.hotmart.com'];
    var searchParams = new URLSearchParams(location.search).toString();
    if (!searchParams) return;
    var url = new URL(location.href);
    var gp = function (k) { return url.searchParams.get(k) || ''; };
    var tail = gp('utm_source') + '|' + gp('utm_medium') + '|' + gp('utm_campaign') + '|' + gp('utm_term') + '|' + gp('utm_content');
    var extra = '&src=' + tail + '&sck=' + tail;
    $$('a').forEach(function (link) {
      prefix.forEach(function (p) {
        if (link.href.indexOf(p) !== -1) {
          var sep = link.href.indexOf('?') === -1 ? '?' : '&';
          link.href += sep + searchParams + extra;
        }
      });
    });
  })();

  /* ---------- 5. FAQ toggle ---------- */
  $$('.elementor-toggle-item').forEach(function (item) {
    var title = $('.elementor-tab-title', item);
    var content = $('.elementor-tab-content', item);
    if (!title || !content) return;
    title.addEventListener('click', function () {
      var open = title.classList.contains('elementor-active');
      title.classList.toggle('elementor-active', !open);
      content.classList.toggle('elementor-active', !open);
      title.setAttribute('aria-expanded', String(!open));
      if (open) {
        content.style.maxHeight = content.scrollHeight + 'px'; void content.offsetWidth;
        content.style.maxHeight = '0px';
        setTimeout(function () { content.style.display = 'none'; content.style.maxHeight = ''; }, 300);
      } else {
        content.style.display = 'block'; content.style.overflow = 'hidden';
        content.style.maxHeight = '0px'; void content.offsetWidth;
        content.style.maxHeight = content.scrollHeight + 'px';
        setTimeout(function () { content.style.maxHeight = ''; content.style.overflow = ''; }, 320);
      }
    });
    content.style.display = 'none';
    content.style.transition = 'max-height .3s ease';
  });

  /* ---------- 6. vídeos YouTube (facade: iframe só no clique) ---------- */
  $$('.elementor-widget-video').forEach(function (w) {
    var overlay = $('.elementor-custom-embed-image-overlay', w);
    var holder = $('.elementor-video', w);
    if (!overlay || !holder) return;
    var st = {};
    try { st = JSON.parse(w.getAttribute('data-settings') || '{}'); } catch (e) { }
    var yt = (st.youtube_url || '').match(/(?:youtu\.be\/|v=)([\w-]{11})/);
    if (!yt) return;
    function play() {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + yt[1] + '?autoplay=1&rel=0';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      f.allowFullscreen = true;
      f.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;border:0';
      holder.style.cssText = 'position:relative;padding-bottom:56.25%;height:0';
      holder.appendChild(f);
      overlay.style.display = 'none';
    }
    overlay.addEventListener('click', play);
    var btn = $('.elementor-custom-embed-play', overlay);
    if (btn) btn.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); play(); } });
  });

  /* ---------- 7. carrossel de depoimentos (substitui Swiper) ---------- */
  $$('.elementor-widget-testimonial-carousel').forEach(function (w) {
    var st = {};
    try { st = JSON.parse(w.getAttribute('data-settings') || '{}'); } catch (e) { }
    var swiper = $('.swiper', w) || $('.swiper-container', w);
    var wrap = $('.swiper-wrapper', w);
    if (!wrap) return;
    var slides = $$('.swiper-slide', wrap);
    var n = slides.length;
    if (!n) return;
    // lazy imgs
    $$('img.swiper-lazy', wrap).forEach(function (img) {
      if (img.dataset.src) { img.src = img.dataset.src; img.classList.add('swiper-lazy-loaded'); }
      var pre = img.parentNode.querySelector('.swiper-lazy-preloader'); if (pre) pre.remove();
    });
    function perView() {
      var W = window.innerWidth;
      if (W < 768) return 1;
      if (W < 1025) return 2;
      return parseInt(st.slides_per_view || 3, 10);
    }
    function gap() { return window.innerWidth < 1025 ? 10 : (st.space_between && st.space_between.size || 0); }
    // clona para loop
    slides.forEach(function (s) { wrap.appendChild(s.cloneNode(true)); });
    var all = $$('.swiper-slide', wrap);
    var idx = 0, timer = null, speed = st.speed || 500, auto = st.autoplay_speed || 3000;
    wrap.style.display = 'flex';
    function layout() {
      var pv = perView(), g = gap();
      var cw = swiper.clientWidth;
      var sw = (cw - g * (pv - 1)) / pv;
      all.forEach(function (s) { s.style.flex = '0 0 ' + sw + 'px'; s.style.maxWidth = sw + 'px'; s.style.marginRight = g + 'px'; });
      go(idx, true);
    }
    function go(i, instant) {
      var pv = perView(), g = gap();
      var sw = (swiper.clientWidth - g * (pv - 1)) / pv + g;
      wrap.style.transition = instant ? 'none' : 'transform ' + speed + 'ms';
      wrap.style.transform = 'translateX(' + (-i * sw) + 'px)';
      idx = i;
    }
    function next() {
      go(idx + 1);
      if (idx >= n) setTimeout(function () { go(idx - n, true); }, speed + 20);
    }
    function prev() {
      if (idx === 0) { go(n, true); void wrap.offsetWidth; }
      go(idx === 0 ? n - 1 : idx - 1);
    }
    function start() { stop(); timer = setInterval(next, auto); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    var prevBtn = $('.elementor-swiper-button-prev', w), nextBtn = $('.elementor-swiper-button-next', w);
    if (prevBtn) prevBtn.addEventListener('click', function () { prev(); stop(); });
    if (nextBtn) nextBtn.addEventListener('click', function () { next(); stop(); });
    w.addEventListener('mouseenter', stop);
    w.addEventListener('mouseleave', function () { if (timer !== null || !w.dataset.stopped) start(); });
    [prevBtn, nextBtn].forEach(function (b) { if (b) b.addEventListener('click', function () { w.dataset.stopped = '1'; }); });
    window.addEventListener('resize', layout);
    layout();
    if (st.autoplay === 'yes') start();
  });

  /* ---------- 8. headlines animadas (highlight, loop 8s — CSS desenha) ---------- */
  $$('.elementor-widget-animated-headline').forEach(function (w) {
    var head = $('.elementor-headline', w);
    if (!head || !$('svg', $('.elementor-headline-dynamic-wrapper', w) || w)) {
      // svg é injetado estático no build; sem svg não anima
    }
    if (!head) return;
    var st = {};
    try { st = JSON.parse(w.getAttribute('data-settings') || '{}'); } catch (e) { }
    var delay = st.highlight_iteration_delay || 8000;
    var dur = st.highlight_animation_duration || 1200;
    head.style.setProperty('--animation-duration', (dur / 1000) + 's');
    function cycle() {
      head.classList.remove('e-hide-highlight');
      head.classList.add('e-animated');
      if (st.loop === 'yes') setTimeout(function () {
        head.classList.add('e-hide-highlight');
        setTimeout(function () { head.classList.remove('e-animated', 'e-hide-highlight'); setTimeout(cycle, 60); }, 450);
      }, delay);
    }
    // começa quando visível
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (en) {
        if (en[0].isIntersecting) { cycle(); io.disconnect(); }
      }, { threshold: .5 });
      io.observe(head);
    } else cycle();
  });

  lazyBg();
  fillHidden();
})();
