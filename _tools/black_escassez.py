"""16/11 (cliente: "coloque escassez na página"). A Black fecha terça 17/11 23h59 (as páginas ficam no ar até 22/11
para a exceção das IAs). Texto muda sozinho pela data de Brasília:
  até 16/11: ACABA AMANHÃ · 17/11: ACABA HOJE · depois: condição por tempo limitado.
Entra na tarja do topo e num aviso antes dos dois blocos de preço. Idempotente."""
import os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARJA_OLD = '<p class="after-only ult">Vai acabar · <b>Black Week Motorizada</b></p>'
TARJA_NEW = ('<p class="after-only ult" data-esc-tarja>A Black termina em</p>'
             '<div class="clock after-only" data-esc-clk></div>')
BOX = ('<div class="esc" data-esc-box><p class="esc__t" data-esc-t>A Black termina em</p><div class="clock esc__clk" data-esc-clk></div>'
       '<p class="esc__s">Depois disso, esta condição sai do ar.</p></div>')
CSS = ('<style>/*esc*/.esc{max-width:640px;margin:0 auto 28px;padding:14px 18px;border:2px solid #d62828;border-radius:12px;'
       'background:rgba(214,40,40,.12);text-align:center;font-family:Poppins,sans-serif}'
       '.esc__t{margin:0;color:#ff5a5a;font-size:clamp(17px,4.8vw,22px);font-weight:800;text-transform:uppercase;letter-spacing:.02em;line-height:1.2}'
       '.esc__clk{margin:10px 0 2px}.esc__clk span{background:#111;color:#fff}.obar [data-esc-clk] span{background:#111;color:#fff}.obar [data-esc-clk] small{color:#ffd6d6}.obar p.ult[data-esc-tarja]{max-width:150px}'
       '.resumo .btn{font-size:clamp(13px,3.8vw,18px)!important;padding:0 10px}'
       '.esc__s{margin:6px 0 0;color:#f4efe4;font-size:14.5px;line-height:1.45}</style>')
JS = ("<script>/*esc*/(function(){var FIM=new Date('2026-11-17T23:59:59-03:00').getTime();function p(n){return(n<10?'0':'')+n}"
      "function t(){var s=Math.floor((FIM-Date.now())/1000);"
      "if(s<=0){document.querySelectorAll('[data-esc-tarja]').forEach(function(e){e.innerHTML='Condição da Black · <b>por tempo limitado</b>';e.style.maxWidth='none'});"
      "document.querySelectorAll('[data-esc-clk]').forEach(function(e){e.style.display='none'});"
      "document.querySelectorAll('[data-esc-t]').forEach(function(e){e.textContent='Condição liberada por tempo limitado'});"
      "document.querySelectorAll('.esc__s').forEach(function(e){e.textContent='A Black Week Motorizada encerrou em 17/11. Esta condição vale só pelo link que você recebeu.'});return}"
      "var d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60),x=s%60;"
      "var html=(d>0?'<span>'+d+'<small>'+(d>1?'dias':'dia')+'</small></span>':'')+'<span>'+p(h)+'<small>horas</small></span><span>'+p(m)+'<small>min</small></span><span>'+p(x)+'<small>seg</small></span>';"
      "document.querySelectorAll('[data-esc-clk]').forEach(function(c){c.innerHTML=html})}"
      "t();setInterval(t,1000)})();</script>")
for d in ("black-liberada", "black-liberada-alunos", "black-liberada-vitalicio", "black-oferta"):
    p = f"{R}/{d}/index.html"; s = open(p, encoding="utf-8").read()
    if "/*esc*/" in s: print("já tinha:", d); continue
    assert s.count(TARJA_OLD) == 1, d
    s = s.replace(TARJA_OLD, TARJA_NEW)
    # aviso antes do 1º bloco de preço e antes do "por apenas" do resumo
    # 16/11 (cliente): sem o aviso vermelho no meio da página; só a tarja do topo com contagem
    s = s.replace("</head>", CSS + "</head>", 1).replace("</body>", JS + "</body>", 1)
    open(p, "w", encoding="utf-8").write(s); print("escassez:", d, s.count("data-esc-clk"))
