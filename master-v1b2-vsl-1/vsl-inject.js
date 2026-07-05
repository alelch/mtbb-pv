/* VSL: mantém a página master-v1b2 inteira (copy/cores/seções/checkout).
   Só reordena o hero:  título → subs → VÍDEO vertical → badges → como visto em.
   Sem foto no topo. Sem botão nessa parte. */
(function(){
  var PLAYER_HOST='https://scripts.converteai.net/6b353be1-c671-4a98-af52-02bc731efaae/players/';
  var VIDID='6a4979919663a03956fef748';   // <<< 1 variável por página (VSL-1/2/3)
  var loaded=false, styled=false, barsSet=false;

  // barras fixas (topo "AO VIVO" + inferior CTA) só aparecem a partir da seção "Como será o dia"
  function setupBars(){
    if(barsSet) return;
    var sec=[].slice.call(document.querySelectorAll('h1,h2,h3,h4')).filter(function(e){return /como ser[áa].*dia/i.test((e.textContent||''));})[0];
    if(!sec) return;
    barsSet=true;
    var st=document.createElement('style');
    st.textContent=[
      '.fixed.top-0.bg-primary,.fixed.bottom-0.z-50{transition:opacity .3s ease,transform .3s ease!important}',
      'html:not(.vsl-bars-on) .fixed.top-0.bg-primary{opacity:0!important;pointer-events:none!important;transform:translateY(-100%)!important}',
      'html:not(.vsl-bars-on) .fixed.bottom-0.z-50{opacity:0!important;pointer-events:none!important;transform:translateY(100%)!important}'
    ].join('\n');
    document.head.appendChild(st);
    function upd(){
      var top=sec.getBoundingClientRect().top+window.scrollY;
      var on=window.scrollY >= (top - window.innerHeight*0.5);
      document.documentElement.classList.toggle('vsl-bars-on', on);
    }
    window.addEventListener('scroll', upd, {passive:true});
    window.addEventListener('resize', upd);
    upd();
  }

  function injectCSS(){
    if(styled) return; styled=true;
    var st=document.createElement('style');
    st.textContent=[
      /* eyebrow em 1 linha só */
      '[data-vsl] > div:first-child{margin-bottom:6px!important;flex-wrap:nowrap!important;white-space:nowrap!important}',
      '[data-vsl] > div:first-child *{font-size:10.5px!important;letter-spacing:.1em!important;white-space:nowrap!important}',
      /* título um pouco maior, ainda compacto na vertical */
      '[data-vsl] h1{font-size:25px!important;line-height:1.12!important;margin-bottom:10px!important}',
      /* subs compactos */
      '[data-vsl] > p{font-size:13.5px!important;line-height:1.34!important;margin:0!important}',
      /* fix layout: títulos de seção com whitespace-nowrap vazam (ex: "É sobre ninguém conhecer o seu livro.") -> deixa quebrar linha */
      'main h1.whitespace-nowrap,main h2.whitespace-nowrap,main h3.whitespace-nowrap{white-space:normal!important;text-wrap:balance}'
    ].join('\n');
    document.head.appendChild(st);
  }

  function videoHTML(){
    return '<div class="vsl-video" style="max-width:290px;margin:0 auto">'
      +'<vturb-smartplayer id="vid-'+VIDID+'" style="display:block;margin:0 auto;width:100%;max-width:300px;border-radius:14px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,.5)"><div style="position:relative;width:100%;padding:177.77777777777777% 0 0;background:#000"></div></vturb-smartplayer>'
      +'</div>';
  }

  function go(){
    var sec=document.querySelector('main section'); if(!sec) return false;
    var h1s=sec.querySelectorAll('h1'); if(!h1s.length) return false;
    injectCSS();
    setupBars();
    var did=false;

    h1s.forEach(function(h1){
      var par=h1.parentElement;
      if(par.getAttribute('data-vsl')) return;
      par.setAttribute('data-vsl','1');

      // subs = primeiro <p> depois do título
      var subs=h1, k=h1;
      while(k=k.nextElementSibling){ if(k.tagName==='P'){ subs=k; break; } }

      // insere o VÍDEO logo depois dos subs
      var v=document.createElement('div');
      v.style.cssText='margin:12px auto 4px';
      v.innerHTML=videoHTML();
      subs.parentNode.insertBefore(v, subs.nextSibling);

      // deleta tudo depois do vídeo dentro do bloco: botão + barra "72%" + infos (12 Julho/8h/vagas) + badges (+800/+10M/+4.400)
      // fica só: eyebrow -> título -> subs -> vídeo. Depois do bloco vem direto "COMO VISTO EM".
      var sib=v.nextElementSibling;
      while(sib){ sib.style.display='none'; sib=sib.nextElementSibling; }

      did=true;
    });

    // esconde a FOTO do topo do hero
    sec.querySelectorAll('picture').forEach(function(p){ var b=p.parentElement; if(b) b.style.display='none'; });
    // a foto dava o respiro abaixo da barra fixa (35px); recoloca esse espaço
    if(getComputedStyle(sec).paddingTop==='0px') sec.style.paddingTop='40px';

    if(did && !loaded){ loaded=true; var s=document.createElement('script'); s.src=PLAYER_HOST+VIDID+'/v4/player.js'; s.async=true; document.head.appendChild(s); }
    return did;
  }

  var n=0, iv=setInterval(function(){ n++; go(); if(n>40) clearInterval(iv); },250);
})();
