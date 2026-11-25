"""25/11 (cliente: "publica desde agora a página"): REABERTURA RELÂMPAGO de qua 25/11 (noite, na hora da publicação) a dom 29/11 23h59 (Brasília).
Dentro da janela: tarja do topo e aviso antes do preço dizem "REABERTURA RELÂMPAGO" (caixa alta, SEM contagem) e os botões
de compra voltam ao normal (o /*encerrado*/ não age). Fora da janela tudo segue como estava (ENCERRADO). Idempotente."""
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INI, FIM = '2026-11-25T00:00:00-03:00', '2026-11-30T00:00:00-03:00'
FLAG = ("<script>/*relampago*/window.__RLP=(function(){var n=Date.now();return n>=new Date('" + INI + "').getTime()&&n<new Date('" + FIM + "').getTime()})();"
        "if(window.__RLP)document.documentElement.classList.add('rlp');</script>")
CSS = ('<style>/*relampago*/.rlp .obar [data-esc-clk],.rlp .esc [data-esc-clk],.rlp .obar [data-clock]{display:none!important}'
       '.rlp .obar p.ult[data-esc-tarja]{max-width:none!important;text-transform:uppercase;letter-spacing:.04em;font-weight:800}'
       '.rlp .esc__t{text-transform:uppercase}</style>')
# dentro do /*esc*/: na janela, escreve a tarja e o aviso e para (sem relógio)
ESC_OLD = "function t(){var s=Math.floor((FIM-Date.now())/1000);"
ESC_NEW = ("function t(){if(window.__RLP){document.querySelectorAll('[data-esc-tarja]').forEach(function(e){e.innerHTML=(new Date().toLocaleDateString('en-CA',{timeZone:'America/Sao_Paulo'})==='2026-11-29')?'Último dia · acaba hoje, para sempre':'Pode acabar a qualquer momento'});"
           "document.querySelectorAll('[data-esc-t]').forEach(function(e){e.textContent='Reabertura relâmpago'});"
           "document.querySelectorAll('.esc__s').forEach(function(e){e.textContent='Pode acabar a qualquer momento.'});return}"
           "var s=Math.floor((FIM-Date.now())/1000);")
ENC_OLD = "if(Date.now()<F)return;"
ENC_NEW = "if(Date.now()<F||window.__RLP)return;"
for d in ("black-liberada", "black-liberada-alunos", "black-liberada-vitalicio", "black-oferta"):
    p = f"{R}/{d}/index.html"
    if not os.path.exists(p): print("não existe:", d); continue
    s = open(p, encoding="utf-8").read()
    if "/*relampago*/" in s: print("já tinha:", d); continue
    if ESC_OLD not in s or ENC_OLD not in s: print("PULADO (sem esc/encerrado):", d, ESC_OLD in s, ENC_OLD in s); continue
    s = s.replace("</head>", FLAG + CSS + "</head>", 1).replace(ESC_OLD, ESC_NEW, 1).replace(ENC_OLD, ENC_NEW, 1)
    open(p, "w", encoding="utf-8").write(s); print("relâmpago:", d)

# 25/11 (cliente): na janela, o "Inscrições liberadas" do topo vira "Reabertura relâmpago" (a classe .kick põe em caixa alta).
KICK = ("<script>/*rlpkick*/(function(){if(!window.__RLP)return;function f(){document.querySelectorAll('.h__kick').forEach(function(e){if(/inscri/i.test(e.textContent))e.textContent='Reabertura relâmpago'})}"
        "if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',f);else f()})();</script>")
for d in ("black-liberada", "black-liberada-alunos", "black-liberada-vitalicio", "black-oferta"):
    p = f"{R}/{d}/index.html"; s = open(p, encoding="utf-8").read()
    if "/*rlpkick*/" not in s: open(p, "w", encoding="utf-8").write(s.replace("</body>", KICK + "</body>", 1)); print("kick:", d)

# 25/11 (cliente): na janela, um raio grande no fundo do topo no lugar dos raios de luz girando.
RAIO = '<style>/*rlpraio*/.rlp .h::before{top:6px;width:min(620px,92vw);height:min(860px,128vw);margin-left:calc(min(620px,92vw) / -2);background:url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 60 90\'%3E%3Cpath d=\'M36 0 L4 52 H27 L20 90 L56 34 H33 Z\' fill=\'%23faab00\'/%3E%3C/svg%3E") center/contain no-repeat;opacity:.17;-webkit-mask-image:none;mask-image:none;animation:none}</style>'
for d in ("black-liberada", "black-liberada-alunos", "black-liberada-vitalicio", "black-oferta"):
    p = f"{R}/{d}/index.html"; s = open(p, encoding="utf-8").read()
    if "/*rlpraio*/" not in s: open(p, "w", encoding="utf-8").write(s.replace("</head>", RAIO + "</head>", 1)); print("raio:", d)

# 25/11 (cliente): raio piscando como relâmpago e tarja do topo amarelo sol.
BRILHO = '<style>/*rlpbrilho*/.rlp.m-depois .obar,.rlp .obar{background:#ffcc00!important;color:#111!important}.rlp .obar p{color:#111!important}@keyframes rlpflash{0%,40%,100%{opacity:.16;filter:drop-shadow(0 0 0 rgba(250,171,0,0))}42%{opacity:.55;filter:drop-shadow(0 0 40px rgba(255,204,0,.9))}44%{opacity:.2}46%{opacity:.6;filter:drop-shadow(0 0 60px rgba(255,204,0,1))}52%{opacity:.22;filter:drop-shadow(0 0 20px rgba(255,204,0,.5))}70%{opacity:.18}}.rlp .h::before{animation:rlpflash 4.5s ease-in-out infinite!important}@media (prefers-reduced-motion:reduce){.rlp .h::before{animation:none!important}}</style>'
for d in ("black-liberada", "black-liberada-alunos", "black-liberada-vitalicio", "black-oferta"):
    p = f"{R}/{d}/index.html"; s = open(p, encoding="utf-8").read()
    if "/*rlpbrilho*/" not in s: open(p, "w", encoding="utf-8").write(s.replace("</head>", BRILHO + "</head>", 1)); print("brilho:", d)
