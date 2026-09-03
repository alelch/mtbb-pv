/* VSL VARIANTE C — PREÇO TRAVADO (master-v1b2-vsl-2).
   Igual à página VSL (B), MAS tudo abaixo do vídeo fica oculto até o vídeo revelar o preço
   da MasterClass (3:52 = 232s). A VTurb libera via displayHiddenElements no tempo de vídeo assistido.
   Hero: eyebrow -> título -> subs -> VÍDEO. Carimbo de atribuição = |pvC. */
(function(){
  // player A/B do Vturb: ele roda o teste entre os vídeos e rastreia as vendas dos vídeos
  var PLAYER_SRC='https://scripts.converteai.net/6b353be1-c671-4a98-af52-02bc731efaae/ab-test/6a70e5541534153a07bee48b/player.js';
  var PLAYER_ID='ab-6a70e5541534153a07bee48b';
  var loaded=false, styled=false, barsSet=false;

  /* ATRIBUIÇÃO: esta página VSL só é servida pra variante C do teste de página.
     O botão do player VTurb é criado async e não recebe o marcador |pv do appendParams.
     No clique, garante |pvC no sck/src de qualquer link Hotmart (não duplica se já tiver |pv). */
  document.addEventListener('click', function(e){
    var a = e.target && e.target.closest ? e.target.closest('a[href*="hotmart.com"]') : null;
    if(!a) return;
    try{
      var u = new URL(a.href, location.href), ch = false;
      ['sck','src'].forEach(function(k){
        var v = u.searchParams.get(k);
        if(v && v.indexOf('|pv') >= 0) return;                    // já marcado
        if(v){ if(v.indexOf('master-v1b2') !== 0) return; }       // sck de outra origem: não mexe
        else { if(k !== 'sck') return; v = 'master-v1b2|vsl'; }   // botão do VÍDEO abre checkout SEM sck -> cria do zero
        u.searchParams.set(k, v + '|pvC'); ch = true;
      });
      if(ch) a.setAttribute('href', u.toString());
    }catch(err){}
  }, true);

  // barras fixas (topo "AO VIVO" + inferior CTA) só a partir da seção "Como será o dia"
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
      /* usa só o hero empilhado (mobile) em todas as larguras; esconde o hero de 2 colunas */
      '[data-vsl-hero]{display:block!important}',
      '[data-vsl-hide]{display:none!important}',
      /* eyebrow em 1 linha, centralizado */
      '[data-vsl] > div:first-child{margin-bottom:6px!important;flex-wrap:nowrap!important;white-space:nowrap!important;justify-content:center!important}',
      '[data-vsl] > div:first-child *{font-size:10.5px!important;letter-spacing:.1em!important;white-space:nowrap!important}',
      /* título compacto (mobile) */
      '[data-vsl] h1{font-size:25px!important;line-height:1.12!important;margin-bottom:10px!important}',
      /* subs compactos (mobile) */
      '[data-vsl] > p{font-size:13.5px!important;line-height:1.34!important;margin:0!important}',
      /* fix: títulos de seção com whitespace-nowrap vazam -> deixa quebrar linha */
      'main h1.whitespace-nowrap,main h2.whitespace-nowrap,main h3.whitespace-nowrap{white-space:normal!important;text-wrap:balance}',
      /* aproxima a faixa "Como visto em" do vídeo (menos respiro entre vídeo e prova social) */
      'main section.border-y{padding-top:8px!important;margin-top:-10px!important}',
      /* MOBILE (<640px): vídeo FULL-WIDTH sem 100vw/break-out (à prova de overflow): zera o padding lateral do container e devolve só pro texto */
      '@media(max-width:639px){'
        +'[data-vsl]{padding-left:0!important;padding-right:0!important}'
        +'[data-vsl] > div:first-child,[data-vsl] > h1,[data-vsl] > p{padding-left:20px!important;padding-right:20px!important}'
        +'.vsl-video{width:100%!important;max-width:100%!important;margin-left:0!important;margin-right:0!important}'
        +'.vsl-video vturb-smartplayer{width:100%!important;max-width:100%!important;border-radius:0!important;box-shadow:none!important}'
      +'}',
      /* DESKTOP (>=640px): centraliza o hero numa coluna estreita; título/subs/vídeo/eyebrow maiores */
      '@media(min-width:640px){'
        +'[data-vsl-hero]{max-width:640px;margin-left:auto;margin-right:auto}'
        +'[data-vsl]{max-width:600px!important;margin-left:auto!important;margin-right:auto!important}'
        +'[data-vsl] > div:first-child *{font-size:12px!important}'
        +'[data-vsl] h1{font-size:34px!important;line-height:1.12!important}'
        +'[data-vsl] > p{font-size:16px!important;line-height:1.4!important}'
        +'.vsl-video{width:auto!important;max-width:380px!important;margin-left:auto!important;margin-right:auto!important}'
        +'.vsl-video vturb-smartplayer{max-width:380px!important;border-radius:14px!important;box-shadow:0 12px 40px rgba(0,0,0,.5)!important}'
      +'}'
    ].join('\n');
    document.head.appendChild(st);
  }

  function videoHTML(){
    return '<div class="vsl-video" style="max-width:290px;margin:0 auto">'
      +'<vturb-smartplayer id="'+PLAYER_ID+'" style="display:block;margin:0 auto;width:100%;max-width:300px;border-radius:14px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,.5)"><div style="position:relative;width:100%;padding:177.77777777777777% 0 0;background:#000"></div></vturb-smartplayer>'
      +'</div>';
  }

  function go(){
    var sec=document.querySelector('main section'); if(!sec) return false;
    var mob=sec.querySelector('.sm\\:hidden'); if(!mob) return false;   // hero empilhado
    var h1=mob.querySelector('h1'); if(!h1) return false;
    injectCSS();
    setupBars();

    var par=h1.parentElement;
    par.setAttribute('data-vsl','1');                                     // idempotente (marca p/ CSS)
    mob.setAttribute('data-vsl-hero','1');                                // força visível + centraliza
    var desk=sec.querySelector('.hidden.sm\\:block'); if(desk) desk.setAttribute('data-vsl-hide','1'); // esconde hero 2 colunas
    if(mob.querySelector('.vsl-video')) return true;   // vídeo já injetado (robusto contra re-render)

    // subs = primeiro <p> depois do título
    var subs=h1, k=h1;
    while(k=k.nextElementSibling){ if(k.tagName==='P'){ subs=k; break; } }

    // insere o VÍDEO (único) logo depois dos subs
    var v=document.createElement('div');
    v.style.cssText='margin:12px auto 4px';
    v.innerHTML=videoHTML();
    subs.parentNode.insertBefore(v, subs.nextSibling);

    // deleta tudo depois do vídeo no bloco: botão + barra "72%" + infos + badges (fica eyebrow->título->subs->vídeo)
    var sib=v.nextElementSibling;
    while(sib){ sib.style.display='none'; sib=sib.nextElementSibling; }

    // esconde a foto do topo do hero
    mob.querySelectorAll('picture').forEach(function(p){ var b=p.parentElement; if(b) b.style.display='none'; });
    // respiro no topo (a foto dava esse espaço)
    if(getComputedStyle(sec).paddingTop==='0px') sec.style.paddingTop='40px';

    // carrega o player A/B do vturb (1 só)
    if(!loaded){ loaded=true; var s=document.createElement('script'); s.src=PLAYER_SRC; s.async=true; document.head.appendChild(s); }
    return true;
  }

  /* ===== 26-E13: ESCASSEZ DINÂMICA — % de ingressos sobe dia a dia até 100% no dia do evento (08/08) ===== */
  var EVENT_E13=new Date('2026-09-06T08:00:00-03:00');   // aula ao vivo: 08/08 às 8h
  /* rotulo do countdown gerado a partir da PROPRIA data do evento.
     Antes era texto cravado e ficou mentindo quando a data do evento mudou. */
  function _evLabel(){ try{
      var d=EVENT_E13, tz={timeZone:'America/Sao_Paulo'};
      var dia=d.toLocaleDateString('pt-BR',Object.assign({day:'numeric'},tz));
      var mes=d.toLocaleDateString('pt-BR',Object.assign({month:'long'},tz));
      var h=d.toLocaleTimeString('pt-BR',Object.assign({hour:'numeric',hour12:false},tz));
      return 'Aula ao vivo \u00b7 '+dia+' de '+mes+', '+parseInt(h,10)+'h';
    }catch(e){ return 'Aula ao vivo'; } }

  var RAMP_DAYS=12, START_PCT=72;                        // começa hoje (~12 dias antes) em 72% -> 100% no evento
  function _e13now(){ try{ var q=new URLSearchParams(location.search).get('cdnow'); if(q){ var d=new Date(q); if(!isNaN(d)) return d; } }catch(e){} return new Date(); }
  function _e13pct(){ var now=_e13now().getTime(), ev=EVENT_E13.getTime(), ini=ev-RAMP_DAYS*864e5;
    var f=Math.max(0,Math.min(1,(now-ini)/(ev-ini))); return Math.round(START_PCT+(100-START_PCT)*f); }
  /* NÃO injeta barra de escassez embaixo do vídeo (o cliente não quer). Só mantém dinâmicas as
     menções "% dos ingressos vendidos" que já existem no resto da página (as do 1º fold ficam
     ocultas no layout VSL). */
  function _e13scarcity(){ var pct=_e13pct();
    [].forEach.call(document.querySelectorAll('p'),function(p){
      if(!/dos ingressos vendidos/i.test(p.textContent||'')) return;
      p.textContent=pct+'% dos ingressos vendidos por R$ 29,00';
      var tr=p.previousElementSibling, fill=tr&&tr.querySelector?tr.querySelector('[style*="width"]'):null;
      if(fill) fill.style.width=pct+'%';
    }); }
  _e13scarcity(); setTimeout(_e13scarcity,1200); setTimeout(_e13scarcity,3000); setInterval(_e13scarcity,300000);

  /* ===== 26-E13: CONTAGEM REGRESSIVA — aparece só nos últimos dias, abaixo do vídeo ===== */
  var CD_SHOW_DAYS=7;
  function _e13cdHTML(){
    var box=function(k,l){ return '<span style="display:inline-flex;flex-direction:column;align-items:center;min-width:34px"><b data-e13-'+k+' style="font-size:20px;font-weight:800;font-variant-numeric:tabular-nums">00</b><small style="font-size:8px;letter-spacing:.06em;text-transform:uppercase;opacity:.75">'+l+'</small></span>'; };
    var sep='<span style="font-size:16px;opacity:.5;margin-top:2px">:</span>';
    return '<div class="e13-cd" style="display:none;margin:14px auto 0;max-width:340px;text-align:center;background:rgba(250,171,0,.08);border:1px solid rgba(250,171,0,.35);border-radius:12px;padding:10px 12px">'
      +'<div style="font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#FAAB00;font-weight:700">'+_evLabel()+'</div>'
      +'<div class="e13-cd-boxes" style="display:none;gap:6px;justify-content:center;align-items:flex-start;margin-top:6px;color:#fff">'+box('d','dias')+sep+box('h','h')+sep+box('m','min')+sep+box('s','s')+'</div>'
      +'<div class="e13-cd-live" style="display:none;font-size:15px;font-weight:800;color:#FAAB00;margin-top:2px">🔴 AO VIVO AGORA</div>'
    +'</div>';
  }
  function _e13cdPlace(){
    // countdown no FIM DO BLOCO, só na OFERTA (#inscricao) e no ÚLTIMO botão da página
    var first=document.querySelector('main section');
    var btns=[].slice.call(document.querySelectorAll('a[href*="hotmart"]')).filter(function(a){
      if(a.offsetParent===null) return false;                          // invisível
      if(a.closest('vturb-smartplayer')) return false;                 // botão do player
      if(a.closest('.fixed')||a.closest('#sticky-cta')) return false;  // CTA fixo/sticky
      if(a.closest('section')===first) return false;                   // botão do hero
      return a.getBoundingClientRect().height>=10;                     // sem altura real -> fora
    });
    if(!btns.length) return false;
    var alvos=[];
    var oferta=btns.filter(function(a){return !!a.closest('#inscricao');})[0];
    if(oferta) alvos.push(oferta);
    var ultimo=btns[btns.length-1];
    if(ultimo && alvos.indexOf(ultimo)<0) alvos.push(ultimo);
    var placed=false;
    alvos.forEach(function(a){
      var bloco=a.parentElement;
      if(bloco.querySelector(':scope > .e13-cd')) return;              // bloco já tem countdown
      var tmp=document.createElement('div'); tmp.innerHTML=_e13cdHTML();
      var cd=tmp.firstChild; cd.style.margin='16px auto 0';
      bloco.appendChild(cd);                                           // fim do bloco (abaixo de tudo)
      placed=true;
    });
    return placed;
  }
  function _e13cdTick(){
    var els=document.querySelectorAll('.e13-cd'); if(!els.length) return;
    var t=_e13now().getTime(), ev=EVENT_E13.getTime(), fim=ev+4*36e5, de=ev-CD_SHOW_DAYS*864e5;
    var r=Math.max(0,ev-t), d=Math.floor(r/864e5), h=Math.floor(r%864e5/36e5), mi=Math.floor(r%36e5/6e4), s=Math.floor(r%6e4/1e3);
    [].forEach.call(els,function(el){
      var bx=el.querySelector('.e13-cd-boxes'), lv=el.querySelector('.e13-cd-live');
      if(t<de || t>=fim){ el.style.display='none'; return; }
      el.style.display='';
      if(t>=ev){ bx.style.display='none'; lv.style.display=''; return; }
      bx.style.display='flex'; lv.style.display='none';
      var set=function(k,v){ var e=el.querySelector('[data-e13-'+k+']'); if(e) e.textContent=(v<10?'0':'')+v; };
      set('d',d); set('h',h); set('m',mi); set('s',s);
    });
  }
  var _pn=0,_pmax=0,_piv=setInterval(function(){ _pmax++; var did=_e13cdPlace(); _pn=did?0:_pn+1; if(_pn>=3||_pmax>30) clearInterval(_piv); },500);
  setInterval(_e13cdTick,1000);

  var n=0, iv=setInterval(function(){ n++; go(); if(n>40) clearInterval(iv); },250);

  /* ===== VARIANTE C — PREÇO TRAVADO: tudo abaixo do vídeo fica oculto (.hide) até o vídeo
     chegar no preço (3:52 = 232s). A VTurb revela via displayHiddenElements (tempo de vídeo
     assistido, respeita pausa, persist p/ quem já assistiu e volta). Roda já no parse. ===== */
  (function(){
    var PRICE_SECONDS=229, revealed=false;
    var st=document.createElement('style'); st.textContent='.hide{display:none}'; (document.head||document.documentElement).appendChild(st);
    function reveal(){ if(revealed) return; revealed=true;
      [].forEach.call(document.querySelectorAll('.hide'),function(el){ el.classList.remove('hide'); el.style.display=''; }); }
    function lock(){
      var sec=document.querySelector('main section'); if(!sec){ return setTimeout(lock,50); }
      // a faixa "Como visto em" (prova social) FICA visível logo abaixo do vídeo; o resto trava
      function keepVisible(el){ return /como visto|visto em/i.test(el.textContent||'')
        || !!el.querySelector('img[src*="radio-senado"],img[src*="band-news"],img[src*="cbn"],img[src*="valor-economico"]'); }
      var sib=sec.nextElementSibling; while(sib){ if(!keepVisible(sib)) sib.classList.add('hide'); sib=sib.nextElementSibling; }  // seções + barra fixa inferior
      var top=sec.previousElementSibling; if(top) top.classList.add('hide');                                 // barra fixa superior
      var sticky=document.getElementById('sticky-cta'); if(sticky) sticky.classList.add('hide');
      // reveal OFICIAL da VTurb (espera o player existir/ficar pronto)
      var wired=false, tries=0;
      var w=setInterval(function(){ tries++;
        var p=document.querySelector('vturb-smartplayer');
        if(p && typeof p.displayHiddenElements==='function'){
          wired=true; clearInterval(w);
          var call=function(){ try{ p.displayHiddenElements(PRICE_SECONDS,['.hide'],{persist:true}); }catch(e){} };
          p.addEventListener('player:ready', call); call();
        } else if(tries>30){ clearInterval(w); if(!wired) reveal(); }  // ~15s sem player pronto = falha técnica -> libera (nunca trava a venda)
      },500);
      // BACKUP pelo relógio do próprio vídeo (mesmo motor da VTurb): garante o reveal aos 232s
      var b=setInterval(function(){ try{
        var inst=window.smartplayer && window.smartplayer.instances && window.smartplayer.instances[0];
        var ct=inst && inst.video ? inst.video.currentTime : null;
        if(typeof ct==='number' && ct>=PRICE_SECONDS){ reveal(); clearInterval(b); }
      }catch(e){} },1000);
    }
    lock();
  })();
})();
