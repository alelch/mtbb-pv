/* Interações da MasterClass (cópia estática de /v1b2) — vanilla JS, sem React */
(function () {
  "use strict";

  /* ---------- FAQ (sanfona) ---------- */
  document.querySelectorAll('[data-faq-btn]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var panel = btn.nextElementSibling;
      if (!panel || panel.getAttribute('data-faq-panel') === null) return;
      var open = panel.style.display !== 'none';
      panel.style.display = open ? 'none' : 'block';
      var chev = btn.querySelector('svg');
      if (chev) chev.classList.toggle('rotate-180', !open);
    });
  });

  /* ---------- CTA fixo (aparece ao rolar > 600px) ---------- */
  var sticky = document.getElementById('sticky-cta');
  if (sticky) {
    var onScroll = function () {
      sticky.style.display = window.scrollY > 600 ? '' : 'none';
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Modal de vídeo (depoimentos com YouTube) ---------- */
  function openVideo(id) {
    var ov = document.createElement('div');
    ov.className = 'fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm';
    ov.innerHTML =
      '<div class="relative w-full max-w-4xl aspect-video rounded-2xl overflow-hidden" style="box-shadow:0 0 0 1px hsl(var(--border)),0 32px 80px hsl(0 0% 0% / 0.8)">' +
        '<button type="button" data-close class="absolute top-3 right-3 z-10 w-9 h-9 rounded-full bg-black/60 border border-white/20 flex items-center justify-center text-white hover:bg-black/80 transition-colors" aria-label="Fechar">' +
          '<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>' +
        '</button>' +
        '<iframe src="https://www.youtube.com/embed/' + id + '?autoplay=1&rel=0" title="Depoimento" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="w-full h-full"></iframe>' +
      '</div>';
    var close = function () { ov.remove(); document.removeEventListener('keydown', onKey); };
    var onKey = function (e) { if (e.key === 'Escape') close(); };
    ov.addEventListener('click', function (e) {
      if (e.target === ov || (e.target.closest && e.target.closest('[data-close]'))) close();
    });
    document.addEventListener('keydown', onKey);
    document.body.appendChild(ov);
  }

  document.querySelectorAll('[data-video-id]').forEach(function (card) {
    card.addEventListener('click', function () { openVideo(card.getAttribute('data-video-id')); });
  });
})();
