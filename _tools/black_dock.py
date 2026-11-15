"""15/11 (cliente: "o botão verde fixo embaixo tá estranho"): no celular o texto ia de borda a borda e o brilho verde
borrava a barra. Barra fixa mais limpa: botão um pouco menor, texto menor com respiro, brilho contido. Idempotente."""
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = ('<style>/*dock*/.dock .btn{min-height:54px!important;padding:0 14px;font-size:clamp(14px,4.1vw,18px)!important;'
       'letter-spacing:.01em;box-shadow:0 0 0 1px rgba(255,255,255,.08) inset,0 6px 16px -6px rgba(38,192,61,.55)!important}'
       '.dock{box-shadow:0 -8px 20px rgba(0,0,0,.55)!important;padding:8px 14px calc(8px + env(safe-area-inset-bottom))!important}</style>')
for d in ("black-liberada", "black-liberada-alunos", "black-liberada-vitalicio", "black-oferta"):
    p = f"{R}/{d}/index.html"; s = open(p, encoding="utf-8").read()
    if "/*dock*/" in s: print("já tinha:", d); continue
    s = s.replace("</head>", CSS + "</head>", 1); open(p, "w", encoding="utf-8").write(s); print("dock:", d)
