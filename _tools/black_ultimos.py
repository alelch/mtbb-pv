"""13/11 (cliente): "vamos terminar a Black na segunda, coloca a tarja de últimos dias no topo" + "fundo vermelho".
A tarja do topo (fase 'depois' da escada) vira: ÚLTIMOS DIAS · A BLACK TERMINA EM + contagem até 16/11 23h59 (Brasília).
Idempotente."""
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD = '<p class="after-only">Inscrições abertas · <b>Black Week Motorizada</b></p>'
NEW = '<p class="after-only ult">Últimos dias · <b>Black Week Motorizada</b></p>'  # 13/11: sem timer (cliente)
CSS = ('<style>/*ult*/.m-depois .obar{background:#d62828;color:#fff}.obar p.ult{max-width:none;padding:5px 0;font-weight:800;color:#fff}'
       '.obar [data-fim] span{background:#111;color:#fff}.obar [data-fim] small{color:#ffd6d6}</style>')
JS = ("<script>/*ult*/(function(){var FIM=new Date('2026-11-16T23:59:59-03:00').getTime();function p(n){return(n<10?'0':'')+n}"
      "function t(){var s=Math.max(0,Math.floor((FIM-Date.now())/1000)),d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60),x=s%60;"
      "var html=(d>0?'<span>'+d+'<small>'+(d>1?'dias':'dia')+'</small></span>':'')+'<span>'+p(h)+'<small>horas</small></span><span>'+p(m)+'<small>min</small></span>'+(d>0?'':'<span>'+p(x)+'<small>seg</small></span>');"
      "document.querySelectorAll('[data-fim]').forEach(function(c){c.innerHTML=html})}"
      "if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',t);else t();setInterval(t,1000)})();</script>")
for d in ("black-liberada", "black-liberada-alunos", "black-liberada-vitalicio", "black-oferta"):
    p = f"{R}/{d}/index.html"; s = open(p, encoding="utf-8").read()
    if "/*ult*/" in s: print("já tinha:", d); continue
    assert s.count(OLD) == 1, d
    s = s.replace(OLD, NEW).replace("</head>", CSS + "</head>", 1)
    open(p, "w", encoding="utf-8").write(s); print("últimos dias:", d)
