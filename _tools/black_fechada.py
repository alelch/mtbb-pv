"""18/11 (cliente: "a página tem que estar fechada agora, encerrou a Black"). A partir de 18/11 01h (Brasília) as 4 páginas da
Black mostram "A Black encerrou". Exceção: quem chega pelo link pessoal de 20 min das IAs (crm-mtbb /l/<código>, que acrescenta
?lp=<código>) e o link ainda está valendo (link_prazo_abrir = ativo) vê a oferta. Idempotente."""
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = ('<style>/*fechada*/html.bf-fech main,html.bf-fech .obar,html.bf-fech .dock,html.bf-fech .zap,html.bf-cheq main,html.bf-cheq .dock{display:none!important}'
       '#bffech{display:none}html.bf-fech #bffech,html.bf-cheq #bffech{display:flex}'
       '#bffech{min-height:100vh;align-items:center;justify-content:center;padding:32px 20px;text-align:center;font-family:Poppins,sans-serif;color:#f4efe4}'
       '#bffech .in{max-width:520px}#bffech h1{margin:18px 0 10px;font-size:clamp(26px,7vw,38px);font-weight:800;line-height:1.15}'
       '#bffech p{margin:0 0 22px;font-size:16px;line-height:1.5;color:#cfc9bc}'
       '#bffech a{display:block;margin:10px auto 0;max-width:360px;padding:15px 18px;border-radius:10px;font-weight:700;text-decoration:none}'
       '#bffech a.b1{background:#faab00;color:#111}#bffech a.b2{border:1.5px solid rgba(255,255,255,.35);color:#fff}'
       'html.bf-cheq #bffech .msg{display:none}#bffech .spin{display:none;margin:0 auto;width:34px;height:34px;border:3px solid rgba(255,255,255,.2);border-top-color:#faab00;border-radius:50%;animation:bfg 1s linear infinite}'
       'html.bf-cheq #bffech .spin{display:block}@keyframes bfg{to{transform:rotate(360deg)}}</style>')
HEAD_JS = ("<script>/*fechada*/(function(){var F=new Date('2026-11-18T01:00:00-03:00').getTime();if(Date.now()<F)return;"
           "var q=new URLSearchParams(location.search),lp=(q.get('lp')||'').replace(/[^A-Za-z0-9]/g,''),h=document.documentElement;"
           "if(!lp){h.classList.add('bf-fech');return}h.classList.add('bf-cheq');"
           "var K='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpzcXRwc3hwYWNsc2xha2FmbXZkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUzMTY5NTMsImV4cCI6MjA5MDg5Mjk1M30.6f3CmgozaE3fTORF0SBSeRDzZNZ1E27tcdQ9h6tKLgc';"
           "fetch('https://jsqtpsxpaclslakafmvd.supabase.co/rest/v1/rpc/link_prazo_abrir',{method:'POST',headers:{apikey:K,Authorization:'Bearer '+K,'Content-Type':'application/json'},body:JSON.stringify({p_codigo:lp})})"
           ".then(function(r){return r.json()}).then(function(r){h.classList.remove('bf-cheq');"
           "if(r&&r.status==='ativo'&&/black-liberada/.test(r.destino||''))return;"
           "h.classList.add('bf-fech');window.__bfExp=true;var e=document.getElementById('bfsub');if(e)e.textContent='O seu link pessoal expirou. A Black Week Motorizada terminou terça, 17/11, à meia-noite.'})"
           ".catch(function(){h.classList.remove('bf-cheq');h.classList.add('bf-fech')})})();</script>")
BOX = ('<div id="bffech"><div class="in"><div class="spin"></div><div class="msg">'
       '<h1>A Black Week Motorizada encerrou.</h1>'
       '<p id="bfsub">A oferta terminou terça, 17/11, à meia-noite.</p>'
       '<a class="b1" href="https://metodo.thebookbusiness.com.br/">Conhecer o Método The Book Business</a>'
       '<a class="b2" href="https://thebookbusiness.com.br/dezza" target="_blank" rel="noopener">Falar com a equipe</a>'
       '</div></div></div>')
for d in ("black-liberada", "black-liberada-alunos", "black-liberada-vitalicio", "black-oferta"):
    p = f"{R}/{d}/index.html"; s = open(p, encoding="utf-8").read()
    if "/*fechada*/" in s: print("já tinha:", d); continue
    i = s.find("<head>"); assert i >= 0
    s = s[:i+6] + HEAD_JS + s[i+6:]
    s = s.replace("</head>", CSS + "</head>", 1)
    j = s.find("<body>"); assert j >= 0
    s = s[:j+6] + BOX + s[j+6:]
    open(p, "w", encoding="utf-8").write(s); print("fechada:", d)
