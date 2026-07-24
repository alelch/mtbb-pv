/* VSL da Imersão: mantém a página lancamento-v1 inteira (copy/cores/seções/checkout/countdown).
   Primeira dobra vira: eyebrow -> título -> subhead -> VÍDEO (padrão da master-v1b2-vsl-1),
   respeitando o tema escuro/dourado. Sem foto, sem botão/progresso/stats no head. 1 player só.
   Usa o hero empilhado (mobile) em TODAS as larguras (esconde o hero de 2 colunas do desktop). */
(function(){
  var PLAYER_SRC='https://scripts.converteai.net/6b353be1-c671-4a98-af52-02bc731efaae/players/6a5f7822551c549be7ce3ea7/v4/player.js';
  var PLAYER_ID='vid-6a5f7822551c549be7ce3ea7';
  var loaded=false, styled=false;

  /* ATRIBUIÇÃO: esta página VSL só é servida pra variante B do teste de página (sck_tag pv).
     O botão do player VTurb é criado async e NÃO recebe o marcador do appendParams — e ainda
     manda um sck curto próprio ("26E12-LAL2_VD11", que NÃO começa com lancamento-v1).
     No clique, garante |pvB em QUALQUER link Hotmart desta página (é sempre B) que ainda não tenha |pv. */
  document.addEventListener('click', function(e){
    var a = e.target && e.target.closest ? e.target.closest('a[href*="hotmart.com"]') : null;
    if(!a) return;
    try{
      var u = new URL(a.href, location.href), ch = false;
      ['sck','src'].forEach(function(k){
        var v = u.searchParams.get(k);
        if(!v || v.indexOf('|pv') >= 0) return;                        // vazio ou já marcado
        if(v.indexOf('lancamento-v1') !== 0) v = 'lancamento-v1|' + v; // sck curto da VTurb (ex "26E12-LAL2_VD11") -> vira sck da página
        u.searchParams.set(k, v + '|pvB'); ch = true;                  // a trigger ancora no slug 'lancamento-v1' e acha o |pvB
      });
      if(ch) a.setAttribute('href', u.toString());
    }catch(err){}
  }, true);

  function injectCSS(){
    if(styled) return; styled=true;
    var st=document.createElement('style');
    st.textContent=[
      '[data-vsl-hero]{display:block!important}',
      '[data-vsl-hide]{display:none!important}',
      /* eyebrow centralizado */
      '[data-vsl] > div:first-child{margin-bottom:8px!important;flex-wrap:nowrap!important;white-space:nowrap!important;justify-content:center!important}',
      '[data-vsl] > div:first-child span{font-size:10.5px!important;letter-spacing:.14em!important;white-space:nowrap!important}',
      /* título e subhead centralizados */
      '[data-vsl] h1{text-align:center!important;font-size:26px!important;line-height:1.14!important;margin-bottom:10px!important}',
      '[data-vsl] > p{text-align:center!important;font-size:14px!important;line-height:1.36!important;margin:0 auto!important;max-width:34ch}',
      /* fix: títulos de seção com whitespace-nowrap vazam -> deixa quebrar linha */
      'main h1.whitespace-nowrap,main h2.whitespace-nowrap,main h3.whitespace-nowrap{white-space:normal!important;text-wrap:balance}',
      /* MOBILE (<640px): vídeo FULL-WIDTH sem 100vw/break-out (à prova de overflow) */
      '@media(max-width:639px){'
        +'[data-vsl]{padding-left:0!important;padding-right:0!important;margin-top:0!important}'
        +'[data-vsl] > div:first-child,[data-vsl] > h1,[data-vsl] > p{padding-left:20px!important;padding-right:20px!important}'
        +'.vsl-video{width:100%!important;max-width:100%!important;margin-left:0!important;margin-right:0!important}'
        +'.vsl-video vturb-smartplayer{width:100%!important;max-width:100%!important;border-radius:0!important;box-shadow:none!important}'
      +'}',
      /* DESKTOP (>=640px): hero numa coluna estreita centralizada */
      '@media(min-width:640px){'
        +'[data-vsl-hero]{max-width:640px;margin:0 auto}'
        +'[data-vsl]{max-width:600px!important;margin:0 auto!important}'
        +'[data-vsl] > div:first-child span{font-size:12px!important}'
        +'[data-vsl] h1{font-size:36px!important;line-height:1.12!important}'
        +'[data-vsl] > p{font-size:16px!important;line-height:1.4!important}'
        +'.vsl-video{width:auto!important;max-width:380px!important;margin:0 auto!important}'
        +'.vsl-video vturb-smartplayer{max-width:380px!important;border-radius:14px!important;box-shadow:0 12px 40px rgba(0,0,0,.55)!important}'
      +'}'
    ].join('\n');
    document.head.appendChild(st);
  }

  /* Barra amarela fixa do topo: escondida na 1ª dobra (vídeo manda), aparece ao rolar
     até "Como será o dia" — mesmo comportamento do master-v1b2-vsl-1 (setupBars). */
  var barsSet=false;
  function setupTopBar(){
    if(barsSet) return;
    var bar=document.querySelector('div.fixed.top-0'); if(!bar) return;
    var sec=[].slice.call(document.querySelectorAll('h1,h2,h3,h4')).filter(function(e){return /como ser[áa].*dia/i.test((e.textContent||''));})[0];
    barsSet=true;
    var st=document.createElement('style');
    st.textContent='.vsl-topbar{transition:opacity .3s ease,transform .3s ease!important}'
      +'html:not(.vsl-topbar-on) .vsl-topbar{opacity:0!important;pointer-events:none!important;transform:translateY(-100%)!important}';
    document.head.appendChild(st);
    bar.classList.add('vsl-topbar');
    function upd(){
      var top=sec?(sec.getBoundingClientRect().top+window.scrollY):800;
      document.documentElement.classList.toggle('vsl-topbar-on', window.scrollY >= (top - window.innerHeight*0.5));
    }
    window.addEventListener('scroll',upd,{passive:true});
    window.addEventListener('resize',upd);
    upd();
  }

  function videoHTML(){
    return '<div class="vsl-video" style="max-width:300px;margin:0 auto">'
      +'<vturb-smartplayer id="'+PLAYER_ID+'" style="display:block;margin:0 auto;width:100%;max-width:300px;border-radius:14px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,.55)"><div style="position:relative;width:100%;padding:177.77777777777777% 0 0;background:#000"></div></vturb-smartplayer>'
      +'</div>';
  }

  function go(){
    var mob=document.querySelector('main > .sm\\:hidden'); if(!mob) return false;   // hero empilhado (mobile)
    var h1=mob.querySelector('h1'); if(!h1) return false;
    injectCSS();
    setupTopBar();
    mob.style.paddingTop='0';   // sem a barra amarela no topo, some o respiro reservado pra ela (pt-[48px])

    var par=h1.parentElement;                                              // bloco de conteúdo (px-6 pb-6 -mt-8)
    par.setAttribute('data-vsl','1');
    mob.setAttribute('data-vsl-hero','1');                                 // força visível + centraliza em todas as larguras
    var desk=document.querySelector('main > .hidden.sm\\:block'); if(desk) desk.setAttribute('data-vsl-hide','1'); // esconde hero 2 colunas
    if(mob.querySelector('.vsl-video')) return true;                       // já injetado (robusto contra re-render)

    // subhead = primeiro <p> depois do título
    var subs=h1, k=h1;
    while(k=k.nextElementSibling){ if(k.tagName==='P'){ subs=k; break; } }

    // insere o VÍDEO logo depois do subhead
    var v=document.createElement('div');
    v.style.cssText='margin:14px auto 4px';
    v.innerHTML=videoHTML();
    subs.parentNode.insertBefore(v, subs.nextSibling);

    // esconde tudo depois do vídeo no bloco: botão + barra 71% + infos + countdown + stats
    var sib=v.nextElementSibling;
    while(sib){ sib.style.display='none'; sib=sib.nextElementSibling; }

    // esconde a foto do topo do hero (o bloco irmão antes do conteúdo)
    var pic=mob.querySelector('picture'); if(pic){ var block=pic.closest('div.relative.w-full')||pic.parentElement; if(block) block.style.display='none'; }
    // esconde os blocos-irmãos DEPOIS do conteúdo (ex.: stats +800/+10M/+4.400) -> vídeo sozinho na dobra (padrão master)
    var msib=par.nextElementSibling; while(msib){ msib.style.display='none'; msib=msib.nextElementSibling; }
    par.style.marginTop='0'; par.style.paddingTop='32px'; par.style.paddingBottom='32px';  // some o -mt-8, dá respiro

    // carrega o player A/B do vturb (1 só)
    if(!loaded){ loaded=true; var s=document.createElement('script'); s.src=PLAYER_SRC; s.async=true; document.head.appendChild(s); }
    return true;
  }

  var n=0, iv=setInterval(function(){ n++; if(go()||n>40) clearInterval(iv); },200);
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', go); else go();
})();
