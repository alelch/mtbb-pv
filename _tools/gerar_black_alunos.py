"""Gera /black-week-alunos/ (cashback R$1.500) e /black-week-vitalicio/ (LOMBADA, cashback R$2.000) a partir da longa
(/black-week-misterio/). NÃO editar as geradas à mão: edite a longa ou este script e rode de novo.
Molde (cliente, 22/10): página de alunos da BF-25 (título do cupom, cupom com a Dany, formulário, cartão da aula, formulário).
Diferenças das geradas: sem o miolo da longa (sonho, segredo, casos, Dany/mídia), cadastro manda publico=aluno|vitalicio,
o pv-lead confere o e-mail na base de compradores e devolve email_nao_aluno (a página mostra "Esse e-mail não é válido.")."""
import re, sys
from pathlib import Path

R = Path(__file__).resolve().parent.parent
BASE = (R / 'black-week-misterio/index.html').read_text()

PUBLICOS = {
    'alunos': dict(
        publico='aluno', valor='R$1.500', grupo='https://sndflw.com/i/Re69lZi7NOj6jo8A42B9',  # Sendflow "BF 2026 - Alunos" (22/10)
        title='Black Week Motorizada · Cashback de alunos',
        desc='Cashback de R$1.500 para alunos do Método The Book Business na Black Week Motorizada. Aula ao vivo dia 9 de novembro, às 20h.',
        topbar='Exclusivo para <b>alunos</b> do Método',
        h1a='Cashback exclusivo', h1b='para alunos',
        lead='Aluno do <b>Método The&nbsp;Book&nbsp;Business</b> tem <b class="amber">R$1.500 de cashback</b> na maior oferta que o The&nbsp;Book&nbsp;Business já fez.',
        t_eyebrow='Cupom de aluno', selo='Aluno', var='AL', grupo_nome='grupo exclusivo dos alunos',
        obg_oferta='na <b>maior oferta já feita</b> pelo Método The Book Business',
        obg_estrela='Ao vivo, <b>segunda, 09/11, às 20h</b>: os seus <b>R$1.500 de cashback</b> na maior oferta já feita pelo Método The&nbsp;Book&nbsp;Business', t_oferta='de cashback na oferta da Black Week Motorizada',
        fecho_eyebrow='Somente para alunos',
        fecho_t='<span class="fecho__t-a">Método The&nbsp;Book&nbsp;Business</span><span class="fecho__t-b gold">vitalício</span><span class="fecho__t-c">+ {LMB}</span>',
    ),
    'vitalicio': dict(
        publico='vitalicio', valor='R$2.000', grupo='https://sndflw.com/i/d8qM9OZ11Gv2BtwFvR1N',  # Sendflow "BF 2026 - Vitalícios" (22/10)
        title='Black Week Motorizada · Cashback de alunos vitalícios',
        desc='Cashback de R$2.000 para alunos vitalícios do Método The Book Business na Black Week Motorizada. Aula ao vivo dia 9 de novembro, às 20h.',
        topbar='Exclusivo para <b>alunos vitalícios</b> do Método',
        h1a='Cashback exclusivo', h1b='para alunos vitalícios',
        lead='Você já tem o <b>Método The&nbsp;Book&nbsp;Business</b> para sempre. Na Black Week, você leva junto o <b>LOMBADA</b>, a ferramenta que todo autor sonhou. E tem <b class="amber">R$2.000 de cashback</b>.',
        t_eyebrow='Cupom de aluno vitalício', selo='Vitalício', var='VT', grupo_nome='grupo exclusivo dos alunos vitalícios',
        obg_oferta='na <b>Black Week Motorizada</b>, com o LOMBADA junto',
        obg_estrela='Ao vivo, <b>segunda, 09/11, às 20h</b>: os seus <b>R$2.000 de cashback</b> na Black Week, com o LOMBADA junto', t_oferta='de cashback na Black Week Motorizada',
        fecho_eyebrow='Somente para alunos vitalícios',
        fecho_t='<span class="fecho__t-a">A ferramenta que todo autor sonhou</span><span class="fecho__t-c">{LMB}</span>',
    ),
}

CSS = """
/* ---------- páginas de alunos: título curto + cupom dourado com a Dany (molde: alunos da BF-25) ---------- */
.al-h { margin-top: 24px; text-transform: none; }
.al-h .a { display: block; font-size: clamp(26px, 7.4vw, 40px); font-weight: 700; line-height: 1.08; letter-spacing: -.01em; }
.al-h .b { display: block; font-size: clamp(24px, 6.6vw, 36px); font-weight: 500; line-height: 1.12; color: var(--ink); }
.al-lead { max-width: 30em; margin: 12px auto 0; font-size: clamp(14px, 3.9vw, 16px); font-weight: 400; line-height: 1.5; color: var(--ink); text-wrap: pretty; }
.al-lead b { font-weight: 700; }
.al-lead .amber { color: var(--amber); }
.cupom { --tink: #1d1406; --g1: #ffe39a; --g2: #faab00; --g3: #c97a00; position: relative; margin: 20px auto 0; max-width: 400px; text-align: left; color: var(--tink);
  filter: drop-shadow(0 12px 28px rgba(250,171,0,.2)); }
.cupom .c-top, .cupom .c-bot { position: relative; overflow: hidden; background: linear-gradient(125deg, var(--g1) 0%, #ffd060 30%, var(--g2) 65%, var(--g3) 100%); }
.cupom .c-top { border-radius: 14px 14px 0 0; padding: 14px 16px 16px;
  -webkit-mask: radial-gradient(circle 11px at 0 100%, #0000 98%, #000) left / 51% 100% no-repeat, radial-gradient(circle 11px at 100% 100%, #0000 98%, #000) right / 51% 100% no-repeat;
          mask: radial-gradient(circle 11px at 0 100%, #0000 98%, #000) left / 51% 100% no-repeat, radial-gradient(circle 11px at 100% 100%, #0000 98%, #000) right / 51% 100% no-repeat; }
.cupom .c-bot { border-radius: 0 0 14px 14px; padding: 11px 16px 12px; display: flex; align-items: center; gap: 10px;
  -webkit-mask: radial-gradient(circle 11px at 0 0, #0000 98%, #000) left / 51% 100% no-repeat, radial-gradient(circle 11px at 100% 0, #0000 98%, #000) right / 51% 100% no-repeat;
          mask: radial-gradient(circle 11px at 0 0, #0000 98%, #000) left / 51% 100% no-repeat, radial-gradient(circle 11px at 100% 0, #0000 98%, #000) right / 51% 100% no-repeat; }
.cupom .c-bot::before { content: ""; position: absolute; left: 18px; right: 18px; top: 0; border-top: 2px dashed rgba(29,20,6,.32); }
.cupom .c-top::after { content: ""; position: absolute; top: -40%; bottom: -40%; width: 34%; left: -60%; transform: skewX(-18deg);
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.45), transparent); animation: cbrilho 5s ease-in-out infinite 1.4s; }
@keyframes cbrilho { 0% { left: -60%; } 45%, 100% { left: 130%; } }
.c-eyebrow { position: relative; z-index: 1; font-weight: 700; font-size: 10px; letter-spacing: .2em; text-transform: uppercase; opacity: .72; }
.c-valor { position: relative; z-index: 1; margin-top: 4px; font: 900 italic clamp(40px, 12vw, 54px)/1 "Montserrat", sans-serif; letter-spacing: -.03em; }
.c-oferta { position: relative; z-index: 1; max-width: 60%; margin-top: 6px; font-weight: 500; font-size: 13px; line-height: 1.3; }
.c-dany { position: absolute; z-index: 0; right: -4px; bottom: 0; width: 38%; max-width: 150px; height: auto; }
.c-bot b { font-weight: 700; font-size: 14px; letter-spacing: -.01em; }
.c-stamp { flex: none; margin-left: auto; padding: 4px 8px 3px; border: 2px solid rgba(29,20,6,.75); border-radius: 6px; font: 900 italic 11px/1 "Montserrat", sans-serif;
  letter-spacing: .08em; transform: rotate(-4deg); text-transform: uppercase; background: rgba(255,235,190,.45); }
.hero .lead-form[data-pos=topo] { margin-top: 26px; }
.al-aviso { margin-top: 10px; font-size: 12px; color: var(--soft, #a9a296); }
/* computador: tudo centrado (como a referência); a Dany já está no cupom, então sai a foto grande e a frase do lado */
@media (min-width: 900px) { .dany-d, .dany-q { display: none !important; } }
@media (prefers-reduced-motion: reduce) { .cupom .c-top::after { animation: none; } }
"""


def troca(s, a, b, n=1):
    k = s.count(a)
    if k != n: sys.exit(f'gerar_black_alunos: esperava {n}x, achei {k}x: {a[:70]!r}')
    return s.replace(a, b)


m = re.search(r'<span class="lmb" role="img" aria-label="LOMBADA">.*?</span>', BASE)
if not m: sys.exit('gerar_black_alunos: logo do LOMBADA não achado')
LMB = m.group(0)

for pasta, P in PUBLICOS.items():
    s = BASE
    # cabeçalho
    s = re.sub(r'<title>.*?</title>', f'<title>{P["title"]}</title>', s, count=1)
    s = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda x: x.group(1) + P['desc'], s)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{P["title"]}">', s)
    s = troca(s, 'href="https://metodo.thebookbusiness.com.br/black-week-misterio/"', f'href="https://metodo.thebookbusiness.com.br/black-week-{pasta}/"')
    s = troca(s, 'url("assets/estante.webp")', 'url("../black-week-misterio/assets/estante.webp")')
    s = troca(s, '</style>', CSS + '</style>')
    s = re.sub(r'<div class="topbar">.*?</div>', f'<div class="topbar">{P["topbar"]}</div>', s, count=1)

    # topo: título + cupom no lugar do "sonhou" e da Dany falando (a Dany vai dentro do cupom)
    hero = (f'<h1 class="al-h"><span class="a gold">{P["h1a"]}</span><span class="b">{P["h1b"]}</span></h1>\n'
            f'          <p class="al-lead">{P["lead"]}</p>\n'
            f'          <div class="cupom" aria-label="Cupom de {P["valor"]} de cashback">\n'
            f'            <div class="c-top"><div class="c-eyebrow">{P["t_eyebrow"]}</div><p class="c-valor">{P["valor"]}</p>'
            f'<p class="c-oferta">{P["t_oferta"]}</p><img class="c-dany" src="../black-week/assets/dany-bw-m.webp" alt="" width="408" height="378" decoding="async"></div>\n'
            f'            <div class="c-bot"><b>Aula ao vivo · 09/11 · 20h</b><span class="c-stamp">{P["selo"]}</span></div>\n'
            f'          </div>\n'
            f'          <div class="aula"><p class="aula__k">Abre ao vivo na aula</p><p class="aula__t">Seu livro vendendo cada vez mais</p><p class="aula__d">09 de novembro, segunda-feira | 20h</p></div>\n\n'
            f'          ')
    s, k = re.subn(r'<h1 class="h1">.*?(?=<div class="lead-form" data-pos="topo")', hero, s, count=1, flags=re.S)
    if k != 1: sys.exit('gerar_black_alunos: topo não achado')
    s, k = re.subn(r'\s*<!-- celular: a frase da Dany.*?<p class="pitch pitch--m".*?</p>', '', s, count=1, flags=re.S)
    if k != 1: sys.exit('gerar_black_alunos: frase da Dany no celular não achada')

    # sai o miolo (sonho, segredo, casos, 1º-10º, Dany, mídia): fica topo + cartão final
    s, k = re.subn(r'  <!-- 2\. o sonho.*?(?=  <!-- 8\. fecho)', '', s, count=1, flags=re.S)
    if k != 1: sys.exit('gerar_black_alunos: miolo não achado')

    # formulários
    s = troca(s, '<p class="hint">Cadastre-se gratuitamente e participe</p>', '<p class="hint">Cadastre o e-mail que você usou na compra do Método</p>')
    s = troca(s, '<h3 class="fecho__h">Cadastre-se gratuitamente e participe</h3>', '<h3 class="fecho__h">Garanta o seu cashback</h3><p class="al-aviso">Use o e-mail da sua compra do Método The&nbsp;Book&nbsp;Business.</p>')
    s = troca(s, 'Quero liberar meu acesso <svg', 'Quero meu cashback <svg', 3)
    s = troca(s, '<p class="msg">Confira o e-mail.</p>', '<p class="msg">Esse e-mail não é válido.<br>Use o mesmo e-mail de compra do Método The&nbsp;Book&nbsp;Business.</p>', 2)

    # cartão final
    s = troca(s, '<p class="eyebrow">Somente na Black Week Motorizada</p>', f'<p class="eyebrow">{P["fecho_eyebrow"]}</p>')
    s, k = re.subn(r'<h3 class="fecho__t">.*?</h3>', '<h3 class="fecho__t">' + P['fecho_t'].replace('{LMB}', LMB) + '</h3>', s, count=1, flags=re.S)
    if k != 1: sys.exit('gerar_black_alunos: título do cartão final não achado')
    s = troca(s, '<p class="aula__k">Revelada ao vivo na aula</p>', '<p class="aula__k">Abre ao vivo na aula</p>')
    s = troca(s, 'href="https://thebookbusiness.com.br/black-grupo"', f'href="{P["grupo"]}"', 2)

    # cadastro: público, conferência do e-mail, sem teste A/B, evento próprio no pixel, obrigado com o grupo certo
    s = troca(s, "variant: 'black-week',", f"variant: 'black-week',\n        publico: '{P['publico']}',")
    s = troca(s, "posicao: 'misterio-' + box.getAttribute('data-pos')", f"posicao: '{P['publico']}-' + box.getAttribute('data-pos')")
    s = troca(s, "      if (window.__bf26ab) payload.ab = window.__bf26ab;\n", '')
    s = troca(s, "var GRUPO = 'https://thebookbusiness.com.br/black-grupo';", f"var GRUPO = '{P['grupo']}';")
    s = troca(s, "if (!r.ok) throw new Error('http ' + r.status);",
              "if (r.status === 403) return r.json().catch(function () { return {}; }).then(function (j) { throw j && j.error === 'email_nao_aluno' ? 'email' : 'http'; });\n"
              "        if (!r.ok) throw new Error('http ' + r.status);")
    s = troca(s, "fbq('trackCustom', 'CadastroBlackWeek');", "fbq('trackCustom', 'CadastroBlackWeekAluno', { publico: '" + P['publico'] + "' });")
    s = troca(s, "location.href = '/black-week-obrigado/';", f"location.href = '/black-week-{pasta}/obrigado/';")
    s = troca(s, """      }).catch(function () {
        btn.disabled = false; btn.innerHTML = btnHTML;
        err.style.display = 'block';""", """      }).catch(function (e) {
        btn.disabled = false; btn.innerHTML = btnHTML;
        // e-mail fora da base de compradores: marca o campo, sem mensagem de erro geral
        if (e === 'email') { $('[data-f=email]', form).classList.add('invalid'); form.email.focus(); return; }
        err.style.display = 'block';""")

    cab = f'<!-- GERADA por _tools/gerar_black_alunos.py a partir de /black-week-misterio/. Não editar aqui. -->\n'
    out = R / f'black-week-{pasta}/index.html'
    out.parent.mkdir(exist_ok=True)
    out.write_text(cab + s)
    print('ok', out.relative_to(R))

# ---------------------------------------------------------------------------------------------------------------
# obrigado de cada público (/black-week-<pasta>/obrigado/): mesmo mecanismo do obrigado da Black (abre o grupo em 3 s,
# "Não conseguiu entrar?" na volta), mas o cupom é o cashback e o grupo é o do público. Eventos com variante AL / VT.
OBG = (R / 'black-week-obrigado/index.html').read_text()
PROG_CSS = (R / '_tools/obrigado_progresso.css').read_text()
for pasta, P in PUBLICOS.items():
    s = OBG
    s = troca(s, '<title>Falta 1 passo · Black Week Motorizada</title>', '<title>Falta 1 passo · Cashback · Black Week Motorizada</title>')
    s = troca(s, '<p class="kicker">Cadastro recebido</p>', '<p class="kicker">Cashback reservado</p>')
    s = troca(s, 'para garantir o seu lugar!</h1>', 'para garantir o seu cashback!</h1>')
    # cliente (22/10): no obrigado dos alunos vai o "progresso" (a versão B que perdeu no público geral), pra não repetir o cupom
    # da página de cadastro. Aluno já tem motivo pra entrar; aqui basta mostrar que avançou.
    prog = (f'<div class="prog" aria-label="Cashback 50% garantido">\n'
            f'    <div class="prog-top"><span>Seu cashback</span><b>50%</b></div>\n'
            f'    <div class="bar"><i id="barra"></i></div>\n'
            f'    <ul class="lista">\n'
            f'      <li class="ok"><span class="ic">✓</span>{"Aluno vitalício" if P["publico"] == "vitalicio" else "Aluno"} confirmado</li>\n'
            f'      <li class="falta"><span class="ic">2</span>Entrar no {P["grupo_nome"]}</li>\n'
            f'      <li class="grupo"><span class="ic">★</span><span>{P["obg_estrela"]}</span></li>\n'
            f'    </ul>\n'
            f'  </div>\n  </div>\n  <div class="col2">')
    s, k = re.subn(r'<div class="ticket".*?</div>\s*</div>\s*</div>\s*<div class="col2">', prog, s, count=1, flags=re.S)
    if k != 1: sys.exit('gerar_black_alunos: ingresso do obrigado não achado')
    s = troca(s, '</style>', PROG_CSS + '</style>')
    s = troca(s, 'entre no grupo para <b>confirmar sua inscrição</b>. <span class="lead-esc">A Black só funciona para quem está no grupo.</span>',
              f'entre no grupo para <b>confirmar o seu cashback</b>. <span class="lead-esc">Os avisos do cashback saem só no grupo.</span>')
    s = troca(s, 'https://thebookbusiness.com.br/black-grupo', P['grupo'], 3)
    s = troca(s, "var VAR = 'C',", f"var VAR = '{P['var']}',")
    s = troca(s, '../black-week-obrigado/assets/qr-grupo.svg', 'assets/qr-grupo.svg')  # QR do grupo do público (gerado em 22/10)
    s = troca(s, 'href="../', 'href="../../', s.count('href="../')) if s.count('href="../') else s
    s = s.replace('src="../', 'src="../../').replace('url("../', 'url("../../').replace("url('../", "url('../../")
    out = R / f'black-week-{pasta}/obrigado/index.html'
    out.parent.mkdir(exist_ok=True)
    out.write_text('<!-- GERADA por _tools/gerar_black_alunos.py a partir de /black-week-obrigado/. Não editar aqui. -->\n' + s)
    print('ok', out.relative_to(R))
