"""18/11 (cliente: "não muda a página... muda só o botão, coloca encerrado, e embaixo um botão para falar com a equipe, para dar
uma abertura"). A partir de 18/11 01h (Brasília): o botão verde vira ENCERRADO (sem clique), o azul do Parcelado Hotmart some e
entra embaixo "Falar com a equipe" (WhatsApp da Natália, que abre a exceção do link de 20 min). Exceção: quem chega pelo link pessoal de 20 min das IAs (?lp=<código>,
crm-mtbb /l/) e o link ainda vale (link_prazo_abrir = ativo) vê os botões normais. Idempotente."""
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = ('<style>/*encerrado*/a.btn.enc{background:#3a3733!important;color:#bdb6a9!important;box-shadow:none!important;cursor:default;filter:none!important;transform:none!important}'
       'a.eqp{display:flex;align-items:center;justify-content:center;max-width:520px;min-height:52px;margin:12px auto 0;padding:0 16px;border-radius:10px;'
       'background:#25d366;color:#fff;font-family:Poppins,sans-serif;font-weight:800;font-size:16px;text-decoration:none}'
       '.dock a.eqp{margin:0;max-width:none;min-height:54px}</style>')
JS = ("<script>/*encerrado*/(function(){var F=new Date('2026-11-18T01:00:00-03:00').getTime();if(Date.now()<F)return;"
      "var Z='https://wa.me/5511924693585?text=Oi%21%20Vi%20que%20a%20Black%20Week%20Motorizada%20encerrou.%20Ainda%20consigo%20entrar%3F';"
      "function fecha(){document.querySelectorAll('a.rec').forEach(function(e){e.remove()});"
      "document.querySelectorAll('a.btn[data-cta]').forEach(function(a){var dock=a.closest('.dock');a.removeAttribute('data-cta');"
      "if(dock){a.className='eqp';a.href=Z;a.target='_blank';a.rel='noopener';a.textContent='Falar com a equipe';return}"
      "a.classList.add('enc');a.href='#';a.setAttribute('aria-disabled','true');a.textContent='Encerrado';a.addEventListener('click',function(e){e.preventDefault()});"
      "var t=document.createElement('a');t.className='eqp';t.href=Z;t.target='_blank';t.rel='noopener';t.textContent='Falar com a equipe';a.insertAdjacentElement('afterend',t)})}"
      "var lp=(new URLSearchParams(location.search).get('lp')||'').replace(/[^A-Za-z0-9]/g,'');"
      "if(!lp){fecha();return}"
      "var K='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpzcXRwc3hwYWNsc2xha2FmbXZkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUzMTY5NTMsImV4cCI6MjA5MDg5Mjk1M30.6f3CmgozaE3fTORF0SBSeRDzZNZ1E27tcdQ9h6tKLgc';"
      "fetch('https://jsqtpsxpaclslakafmvd.supabase.co/rest/v1/rpc/link_prazo_abrir',{method:'POST',headers:{apikey:K,Authorization:'Bearer '+K,'Content-Type':'application/json'},body:JSON.stringify({p_codigo:lp})})"
      ".then(function(r){return r.json()}).then(function(r){if(!(r&&r.status==='ativo'&&/black-liberada/.test(r.destino||'')))fecha()}).catch(fecha)})();</script>")
for d in ("black-liberada", "black-liberada-alunos", "black-liberada-vitalicio", "black-oferta"):
    p = f"{R}/{d}/index.html"; s = open(p, encoding="utf-8").read()
    if "/*encerrado*/" in s: print("já tinha:", d); continue
    s = s.replace("</head>", CSS + "</head>", 1).replace("</body>", JS + "</body>", 1)
    open(p, "w", encoding="utf-8").write(s); print("encerrado:", d)
