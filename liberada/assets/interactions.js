/* liberada — interações vanilla (substitui jQuery + Elementor frontend ~500KB)
   Comportamento portado 1:1 da página original thebookbusiness.com.br/liberada/ */
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
  lazyBg();

  /* ---------- 2. countdown (mesma conta do Elementor: horas %24, sem dias) ---------- */
  $$('.elementor-countdown-wrapper[data-date]').forEach(function (w) {
    var end = parseInt(w.getAttribute('data-date'), 10) * 1000;
    var eh = $('.elementor-countdown-hours', w), em = $('.elementor-countdown-minutes', w), es = $('.elementor-countdown-seconds', w);
    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function tick() {
      var t = Math.max(0, Math.floor((end - Date.now()) / 1000));
      if (eh) eh.textContent = pad(Math.floor(t / 3600) % 24);
      if (em) em.textContent = pad(Math.floor(t / 60) % 60);
      if (es) es.textContent = pad(t % 60);
    }
    tick(); setInterval(tick, 1000);
  });

  /* ---------- 3. entrance animations (elementor-invisible → animated) ---------- */
  function reveal() {
    var els = $$('.elementor-invisible');
    if (!('IntersectionObserver' in window)) { els.forEach(function (e) { e.classList.remove('elementor-invisible'); }); return; }
    var mobile = matchMedia('(max-width:767px)').matches;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target, st = {};
        try { st = JSON.parse(el.getAttribute('data-settings') || '{}'); } catch (e) {}
        var anim = (mobile && st._animation_mobile) || st._animation || 'fadeIn';
        el.classList.remove('elementor-invisible');
        el.classList.add('animated', anim);
        io.unobserve(el);
      });
    }, { rootMargin: '-40px' });
    els.forEach(function (e) { io.observe(e); });
  }
  reveal();

  /* ---------- 4. swiper (carrosséis) — carrega o bundle só quando precisa ---------- */
  var swiperLoaded = null;
  function loadSwiper() {
    if (swiperLoaded) return swiperLoaded;
    swiperLoaded = new Promise(function (res) {
      var s = document.createElement('script');
      s.src = 'assets/swiper8.min.js';
      s.onload = res; document.head.appendChild(s);
    });
    return swiperLoaded;
  }
  function initCarousels() {
    /* materializa imagens lazy do swiper (data-src -> src, lazy nativo do browser) */
    $$('img.swiper-lazy[data-src]').forEach(function (img) {
      img.src = img.getAttribute('data-src');
      img.setAttribute('loading', 'lazy');
      img.classList.add('swiper-lazy-loaded');
    });
    $$('.swiper-lazy-preloader').forEach(function (el) { el.remove(); });
    /* depoimentos (media-carousel coverflow — settings do widget original) */
    $$('.elementor-widget-media-carousel .elementor-main-swiper').forEach(function (el) {
      new Swiper(el, {
        effect: 'coverflow', centeredSlides: true, loop: true, grabCursor: true,
        speed: 800, autoplay: { delay: 500, pauseOnMouseEnter: true, disableOnInteraction: true },
        spaceBetween: 10,
        slidesPerView: 1,
        breakpoints: { 768: { slidesPerView: 2 }, 1024: { slidesPerView: 3 } },
        coverflowEffect: { rotate: 50, stretch: 0, depth: 100, modifier: 1, slideShadows: true },
        pagination: { el: el.querySelector('.swiper-pagination'), clickable: true },
        navigation: {
          nextEl: el.parentElement.querySelector('.elementor-swiper-button-next'),
          prevEl: el.parentElement.querySelector('.elementor-swiper-button-prev')
        }
      });
    });
    /* prints das aulas (image-carousel: 2 por vez, dots, autoplay 2s) */
    $$('.elementor-widget-image-carousel .elementor-image-carousel-wrapper').forEach(function (el) {
      new Swiper(el, {
        loop: true, speed: 800, autoplay: { delay: 2000, pauseOnMouseEnter: true, disableOnInteraction: true },
        spaceBetween: 20, slidesPerView: 1,
        breakpoints: { 768: { slidesPerView: 2 } },
        pagination: { el: el.querySelector('.swiper-pagination'), clickable: true }
      });
    });
  }
  (function bootCarousels() {
    if (!$$('.elementor-widget-media-carousel, .elementor-widget-image-carousel').length) return;
    var fired = false;
    function go() { if (fired) return; fired = true; loadSwiper().then(initCarousels); }
    /* como o original: monta já no load (mas fora do caminho crítico) */
    if ('requestIdleCallback' in window) requestIdleCallback(go, { timeout: 1500 });
    else setTimeout(go, 800);
    ['scroll', 'touchstart', 'click'].forEach(function (ev) { addEventListener(ev, go, { once: true, passive: true }); });
  })();

  /* ---------- 5. lightbox de vídeo dos depoimentos ---------- */
  var lb = null;
  function openVideo(src) {
    if (!lb) {
      lb = document.createElement('div');
      lb.id = 'lb-video';
      lb.innerHTML = '<div class="lb-back"></div><div class="lb-box"><button class="lb-x" aria-label="Fechar">&times;</button><div class="lb-frame"></div></div>';
      document.body.appendChild(lb);
      lb.addEventListener('click', function (e) {
        if (e.target.classList.contains('lb-back') || e.target.classList.contains('lb-x')) closeVideo();
      });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeVideo(); });
    }
    $('.lb-frame', lb).innerHTML = '<iframe src="' + src + '" frameborder="0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
    lb.classList.add('on');
    document.body.style.overflow = 'hidden';
  }
  function closeVideo() {
    if (!lb) return;
    lb.classList.remove('on');
    $('.lb-frame', lb).innerHTML = '';
    document.body.style.overflow = '';
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-elementor-lightbox-video]');
    if (!a) return;
    e.preventDefault();
    openVideo(a.getAttribute('data-elementor-lightbox-video'));
  });

  /* ---------- 6. toggle (FAQ) ---------- */
  $$('.elementor-toggle-item').forEach(function (item) {
    var title = $('.elementor-tab-title', item), content = $('.elementor-tab-content', item);
    if (!title || !content) return;
    content.style.display = 'none';
    title.setAttribute('role', 'button'); title.setAttribute('tabindex', '0');
    function toggle() {
      var open = title.classList.toggle('elementor-active');
      content.style.display = open ? 'block' : 'none';
      title.setAttribute('aria-expanded', open ? 'true' : 'false');
    }
    title.addEventListener('click', toggle);
    title.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });
  });

  /* ---------- 7. UTMs/sck → checkout Hotmart (padrão do repo) ---------- */
  var PAGE_ID = 'PV-Liberada';
  function appendParams(a) {
    try {
      var q = new URLSearchParams(location.search);
      var url = new URL(a.href);
      q.forEach(function (v, k) {
        if (/^utm_|^fbclid$|^gclid$|^ttclid$/.test(k) && !url.searchParams.has(k)) url.searchParams.set(k, v);
      });
      if (!url.searchParams.has('sck')) url.searchParams.set('sck', PAGE_ID);
      if (!url.searchParams.has('src')) url.searchParams.set('src', PAGE_ID);
      a.href = url.toString();
    } catch (e) {}
  }
  function hookCheckout() { $$('a[href*="pay.hotmart.com"]').forEach(appendParams); }
  hookCheckout();
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href*="pay.hotmart.com"]');
    if (a) appendParams(a);
  }, true);
})();
