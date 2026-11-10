"""10/11 (cliente): segundo botão "Parcelado Hotmart" (recorrência) só na página geral e na de aluno.
O cartão normal não tem mais Parcelado Hotmart; quem clica no botão de recorrência passa pelo mesmo formulário
e vai para a oferta de recorrência do seu público: geral va4f27ws, aluno ye3d1313 (vitalício não tem: segue o normal).
Idempotente: pode rodar de novo."""
import os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CTA = '<a class="btn" href="#oferta" data-cta>Clique para garantir sua vaga</a>'
REC = ('<a class="rec" href="#oferta" data-cta data-rec><b>Parcelado Hotmart</b>'
       '<span>Parcele sem usar o seu limite</span></a>')
CSS = ('<style>/*rec*/a.rec{display:block;max-width:520px;margin:12px auto 0;padding:12px 16px;border:1.5px solid rgba(255,255,255,.35);'
       'border-radius:12px;color:#fff;text-decoration:none;text-align:center;font-family:Poppins,sans-serif;line-height:1.3}'
       'a.rec b{display:block;font-size:15px;font-weight:700}a.rec span{display:block;margin-top:3px;font-size:14px;font-weight:600;color:#fff}'
       'a.rec:hover{background:#1a5fd0}</style>')
JS = ("<script>/*rec*/window.__REC=false;document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-cta],[data-trv]');"
      "if(a)window.__REC=a.hasAttribute('data-rec')},true);"
      "window.recUrl=function(q,h){var O={geral:'va4f27ws',aluno:'ye3d1313'};if(!window.__REC||!O[q])return h;"
      "var u=new URL(h,location.href),v=new URL('https://pay.hotmart.com/A108368040G');v.searchParams.set('off',O[q]);v.searchParams.set('checkoutMode','10');"
      "u.searchParams.forEach(function(x,k){if(k!=='off'&&k!=='checkoutMode')v.searchParams.set(k,x)});return v.toString()};</script>")
for d in ("black-liberada", "black-liberada-alunos"):
    p = f"{R}/{d}/index.html"; s = open(p, encoding="utf-8").read()
    if "/*rec*/" in s: print("já tinha:", d); continue
    n = s.count(CTA)
    s = s.replace('<div class="dock" id="dock">' + CTA, '<div class="dock" id="dock">@@DOCK@@')
    s = s.replace(CTA, CTA + REC).replace('@@DOCK@@', CTA)
    assert s.count("return u.toString()}") == 1
    s = s.replace("return u.toString()}", "return recUrl(qual,u.toString())}")
    s = s.replace("</head>", CSS + JS + "</head>", 1)
    open(p, "w", encoding="utf-8").write(s); print("rec:", d, "botões", s.count("data-rec>"), "de", n)
