/* L90D · upsell e downsell (29/09): quem comprou o front passa por aqui? Quanto tempo fica?
   Até onde vê o vídeo? Grava em mtbb_pv_events pelo tracker.js (carregar ele ANTES deste).
   Eventos: <etapa>_tempo nos marcos (10s 30s 1 2 5 10 15 min de página VISÍVEL) e
   <etapa>_saiu ao esconder/fechar a aba (pode vir mais de um; vale o maior seg).
   meta.vid = o mesmo id que o front põe no sck da compra (|v<vid>): é por ele que a visita
   daqui casa com o comprador. A visita em si o tracker grava sozinho (quiz_view).        */
(function(){
  var ETAPA = location.pathname.indexOf('downsell') >= 0 ? 'downsell' : 'upsell';
  function vid(){
    try { return String(localStorage.getItem('ab_vid') || '').toLowerCase().replace(/[^a-z0-9]/g, '').slice(0, 16) || null; }
    catch(e){ return null; }
  }
  function video(){
    try {
      var sp = window.smartplayer && window.smartplayer.instances && window.smartplayer.instances[0];
      var el = document.querySelector('vturb-smartplayer');
      var cfg = (sp && sp.config) || (el && el.config) || {};
      return { seg: sp && sp.video ? Math.round(sp.video.currentTime || 0) : null,
               lead: el ? (el.getAttribute('original-id') || el.id) : null,
               nome: cfg.name || null };
    } catch(e){ return {}; }
  }
  var vis = 0, last = Date.now(), visivel = !document.hidden, enviados = {};
  function conta(){ var agora = Date.now(); if (visivel) vis += (agora - last) / 1000; last = agora; }
  function envia(tipo, marco){
    try {
      if (!window.MTBB_TRACK) return;
      var v = video();
      window.MTBB_TRACK(ETAPA + '_' + tipo, { meta: { etapa: ETAPA, seg: Math.round(vis), marco: marco || null,
        vid: vid(), video_seg: v.seg, vsl: v.lead, vsl_nome: v.nome } });
    } catch(e){}
  }
  document.addEventListener('visibilitychange', function(){ conta(); visivel = !document.hidden; if (document.hidden) envia('saiu'); });
  window.addEventListener('pagehide', function(){ conta(); envia('saiu'); });
  var MARCOS = [10, 30, 60, 120, 300, 600, 900];
  setInterval(function(){
    conta();
    MARCOS.forEach(function(m){ if (vis >= m && !enviados[m]) { enviados[m] = 1; envia('tempo', m); } });
  }, 2000);
})();
