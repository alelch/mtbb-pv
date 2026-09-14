# -*- coding: utf-8 -*-
"""
Cinco direções para a seção "Por que sozinho não dá" do upsell do 90D.

    python3 gera_porque.py [destino.html] [--artifact]

O DIAGNÓSTICO DA SEÇÃO ATUAL: ela AFIRMA que você não enxerga o próprio erro
e não mostra nada. É a ponte entre a conta e a oferta, carrega o argumento
que justifica a call inteira (alguém de fora olhando), e hoje é um parágrafo
centralizado logo depois do momento mais forte da página.

Além disso ela empilha DOIS argumentos diferentes num bloco só:
  (a) você não enxerga o seu próprio erro;
  (b) não é sobre a escrita, é sobre tudo que decide se o livro é encontrado.
Cada alternativa abaixo escolhe qual dos dois carregar, e por qual mecanismo.

As cinco não são a mesma coisa repintada. Os mecanismos são:
  01 escala      o mesmo objeto muda de tamanho e o defeito aparece
  02 tempo       uma contagem de dez segundos que termina em marcações
  03 inventário  a quantidade é o argumento
  04 contraste   dois pontos de vista lado a lado
  05 prova       três pessoas que não viam, em vez de argumento

⚠️ COPY: o que é do texto atual está marcado [atual]. O resto é proposta
minha e precisa passar pela Dany antes de ir pro ar.
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_args = [a for a in sys.argv[1:] if not a.startswith('--')]
OUT = _args[0] if _args else os.path.join(HERE, 'porque.html')

CSS = r"""
:root{--pa:#101012;--pa2:#17171A;--ink:#EFEDE8;--mut:#9A958D;--dim:#6B675F;--ru:#27272B;
  --ac:#EAB82D;--vm:#E0574A;--off:#F3F0E8;--offtx:#141312;
  --ff:'DM Sans',system-ui,sans-serif;--fd:'Space Grotesk','DM Sans',sans-serif;
  --fs:Fraunces,Georgia,serif;--r:14px}
*{box-sizing:border-box}
body{margin:0;background:var(--pa);color:var(--ink);font:400 16px/1.6 var(--ff);
  -webkit-font-smoothing:antialiased}
.w{max-width:1120px;margin:0 auto;padding:0 22px}
h1,h2,h3{margin:0;font-family:var(--fd);font-weight:700;letter-spacing:-.03em;line-height:1.1}
.serifa{font-family:var(--fs);font-style:italic;font-weight:500;letter-spacing:-.02em}
.eyebrow{font-family:var(--fd);font-size:.78rem;font-weight:700;letter-spacing:.18em;
  text-transform:uppercase;color:var(--ac);margin:0 0 16px}
header{padding:56px 0 34px;border-bottom:1px solid var(--ru)}
header h1{font-size:clamp(1.9rem,4vw,3rem)}
header p{margin:18px 0 0;max-width:72ch;color:var(--mut)}
header p b{color:var(--ink)}
header .nota{margin-top:16px;padding:14px 18px;border-left:2px solid var(--vm);
  background:rgba(224,87,74,.06);font-size:.94rem;max-width:72ch}
.item{border-bottom:1px solid var(--ru);padding:56px 0}
.cab{display:flex;align-items:baseline;gap:12px;margin:0 0 8px;flex-wrap:wrap}
.cab .no{font-family:var(--fd);font-weight:700;font-size:.78rem;letter-spacing:.16em;color:var(--ac)}
.cab h2{font-size:1.3rem}
.cab .mec{font-family:var(--fd);font-weight:700;font-size:.66rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--dim);border:1px solid var(--ru);padding:4px 8px;border-radius:99px}
.tese{margin:0 0 30px;color:var(--mut);max-width:76ch;font-size:.97rem}
.tese b{color:var(--ink)}
.palco{background:var(--pa2);border:1px solid var(--ru);border-radius:18px;
  padding:clamp(28px,4vw,52px) clamp(20px,3vw,44px)}
.meio{text-align:center;max-width:760px;margin:0 auto}
.h2{font-size:clamp(1.5rem,3.2vw,2.3rem)}
.sub{margin:18px auto 0;max-width:58ch;color:var(--mut);font-size:1.02rem;line-height:1.62}
.sub b{color:var(--ink);font-weight:700}
.atual{font-family:var(--fd);font-weight:700;font-size:.6rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--dim);vertical-align:super}
footer{padding:34px 0 60px;color:var(--dim);font-size:.85rem}

/* ── 01 escala: a mesma capa, dois tamanhos ── */
.capas{display:flex;gap:clamp(24px,5vw,72px);align-items:flex-end;justify-content:center;
  flex-wrap:wrap;margin:34px 0 0}
.capa{background:#1D2A24;border-radius:4px;display:flex;flex-direction:column;justify-content:center;
  padding:8% 9%;box-shadow:0 22px 50px -28px #000;position:relative}
.capa .t{font-family:var(--fd);font-weight:700;color:#EDE7D8;line-height:1.05;letter-spacing:-.03em}
.capa .st{color:#9FB0A6;line-height:1.2;margin-top:.5em}
.capa .a{color:#C9A227;margin-top:auto;letter-spacing:.14em;text-transform:uppercase;font-weight:700}
.capa.g{width:min(260px,62vw);aspect-ratio:2/3}
.capa.g .t{font-size:26px}.capa.g .st{font-size:11px}.capa.g .a{font-size:8px}
.capa.p{width:86px;aspect-ratio:2/3}
.capa.p .t{font-size:8.6px}.capa.p .st{font-size:3.6px}.capa.p .a{font-size:2.6px}
.leg{text-align:center;margin:12px 0 0;font-family:var(--fd);font-weight:700;font-size:.7rem;
  letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}
.leg.mal{color:var(--vm)}

/* ── 02 tempo ── */
.crono{display:grid;grid-template-columns:auto 1fr;gap:clamp(22px,4vw,48px);align-items:center;
  margin:30px 0 0}
.relogio{width:132px;height:132px;border-radius:50%;border:2px solid var(--ru);display:grid;
  place-content:center;font-family:var(--fd);font-weight:700;font-size:2.6rem;color:var(--ac);
  position:relative;font-variant-numeric:tabular-nums}
.marcas{display:grid;gap:12px}
.marca{display:grid;grid-template-columns:22px 1fr;gap:12px;align-items:start;opacity:.2;
  transition:opacity .5s ease}
.marca.on{opacity:1}
.marca i{width:22px;height:22px;border-radius:50%;border:1.5px solid var(--vm);color:var(--vm);
  display:grid;place-content:center;font-style:normal;font-size:.7rem;font-weight:700}
.marca p{margin:0;font-size:1rem}
.marca p b{font-family:var(--fd);font-weight:700}

/* ── 03 inventário ── */
.inv{display:flex;flex-wrap:wrap;gap:9px;margin:30px 0 0;justify-content:center}
.inv span{font-family:var(--fd);font-weight:700;font-size:clamp(.92rem,1.9vw,1.14rem);
  letter-spacing:-.02em;border:1px solid var(--ru);border-radius:99px;padding:9px 16px;color:var(--mut)}
.inv span.escrita{color:var(--ink);border-color:var(--ac);background:rgba(234,184,45,.08)}
.conta-itens{text-align:center;margin:26px 0 0;font-family:var(--fd);font-weight:700;
  font-size:clamp(1.1rem,2.4vw,1.5rem);letter-spacing:-.03em}
.conta-itens b{color:var(--ac)}

/* ── 04 contraste ── */
.dois{display:grid;grid-template-columns:1fr 1fr;gap:0;margin:32px 0 0;border:1px solid var(--ru);
  border-radius:16px;overflow:hidden}
.lado{padding:clamp(20px,3vw,32px)}
.lado+.lado{border-left:1px solid var(--ru)}
.lado .k{font-family:var(--fd);font-weight:700;font-size:.72rem;letter-spacing:.16em;
  text-transform:uppercase;margin:0 0 18px}
.lado.voce .k{color:var(--dim)}
.lado.fora{background:rgba(234,184,45,.05)}
.lado.fora .k{color:var(--ac)}
.lado ul{list-style:none;margin:0;padding:0;display:grid;gap:14px}
.lado li{font-size:1rem;line-height:1.45;color:var(--mut);padding-left:20px;position:relative}
.lado li:before{content:'';position:absolute;left:0;top:.6em;width:8px;height:1px;background:var(--ru)}
.lado.fora li{color:var(--ink)}
.lado.fora li:before{background:var(--ac)}

/* ── 05 prova ── */
.tres{display:grid;gap:0;margin:30px 0 0}
.quem{display:grid;grid-template-columns:minmax(120px,190px) 1fr;gap:clamp(16px,3vw,34px);
  padding:24px 0;border-top:1px solid var(--ru);align-items:baseline}
.quem:last-child{border-bottom:1px solid var(--ru)}
.quem .n{font-family:var(--fd);font-weight:700;font-size:1.02rem;letter-spacing:-.02em}
.quem .n small{display:block;font-family:var(--ff);font-weight:400;font-size:.82rem;
  color:var(--dim);letter-spacing:0;margin-top:4px}
.quem .f{margin:0;font-size:clamp(1.02rem,2.1vw,1.24rem);line-height:1.42}
.quem .f b{color:var(--ac);font-weight:700}
.fecho{margin:30px auto 0;max-width:56ch;text-align:center;font-family:var(--fd);font-weight:700;
  font-size:clamp(1.15rem,2.4vw,1.5rem);letter-spacing:-.03em;line-height:1.25}
@media(max-width:760px){.dois{grid-template-columns:1fr}.lado+.lado{border-left:0;border-top:1px solid var(--ru)}
 .crono{grid-template-columns:1fr}.quem{grid-template-columns:1fr;gap:8px}}
"""

JS = r"""
(function(){
  var cs = [].slice.call(document.querySelectorAll('.crono'));
  cs.forEach(function(c){
    var rel = c.querySelector('.relogio'), ms = [].slice.call(c.querySelectorAll('.marca'));
    var n = 10, rodando = false;
    function roda(){
      if (rodando) return; rodando = true; n = 10; rel.textContent = n;
      ms.forEach(function(m){ m.classList.remove('on'); });
      var t = setInterval(function(){
        n--; rel.textContent = n > 0 ? n : 0;
        if (n === 6) ms[0] && ms[0].classList.add('on');
        if (n === 3) ms[1] && ms[1].classList.add('on');
        if (n <= 0){ ms[2] && ms[2].classList.add('on'); clearInterval(t); rodando = false; }
      }, 700);
    }
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){ if (e.isIntersecting) roda(); });
    }, {threshold:.5});
    io.observe(c);
  });
})();
"""

V = []


def add(no, nome, mec, tese, html):
    V.append((no, nome, mec, tese, html))


A = '<span class="atual">atual</span>'

# ── 01 ─────────────────────────────────────────────────────────
add('01', 'O ponto cego, à escala', 'escala',
    'A seção para de <b>afirmar</b> que você não vê o próprio erro e passa a <b>mostrar</b>. '
    'A mesma capa aparece do tamanho que você a vê (na sua tela, enorme) e do tamanho que o '
    'leitor a vê (miniatura na Amazon). Nada muda na capa: muda o tamanho, e o defeito aparece '
    'sozinho. É a demonstração mais barata que existe e é uma aula real do Método.',
    '<div class="meio"><p class="eyebrow">O ponto cego</p>'
    '<h2 class="h2">Você olha mil vezes<br><span class="serifa">e está tudo certo.</span></h2>'
    '<p class="sub">Só que você olha assim.<br>O seu leitor olha assado.</p></div>'
    '<div class="capas">'
    '<div><div class="capa g"><span class="t">Estratégia e liderança em tempos de profundas '
    'mudanças</span><span class="st">o caminho do sucesso na organização pública</span>'
    '<span class="a">Robson Leite</span></div><p class="leg">Como você vê</p></div>'
    '<div><div class="capa p"><span class="t">Estratégia e liderança em tempos de profundas '
    'mudanças</span><span class="st">o caminho do sucesso na organização pública</span>'
    '<span class="a">Robson Leite</span></div><p class="leg mal">Como o leitor vê</p></div>'
    '</div>'
    '<p class="sub" style="text-align:center">Outra pessoa olha dez segundos e aponta o que estava '
    'na sua cara. ' + A + '</p>')

# ── 02 ─────────────────────────────────────────────────────────
add('02', 'Os dez segundos', 'tempo',
    'A frase "outra pessoa olha dez segundos" ' + A.replace('<span class="atual">', '<span class="atual">') +
    ' deixa de ser figura de linguagem e vira o relógio da seção. A contagem roda quando o bloco '
    'entra na tela e, a cada intervalo, aparece uma coisa que alguém de fora veria. No fim dos dez '
    'segundos, três. <b>Risco:</b> se a pessoa rola rápido, perde a contagem.',
    '<div class="meio"><p class="eyebrow">Dez segundos</p>'
    '<h2 class="h2">É o tempo que alguém de fora leva<br>'
    '<span class="serifa">para ver o que você não vê.</span></h2></div>'
    '<div class="crono"><div class="relogio">10</div><div class="marcas">'
    '<div class="marca"><i>1</i><p><b>A capa não diz do que é o livro.</b> Bonita, muda.</p></div>'
    '<div class="marca"><i>2</i><p><b>O título não é procurado por ninguém.</b> Ninguém digita isso.</p></div>'
    '<div class="marca"><i>3</i><p><b>A sinopse fala de você, não do leitor.</b></p></div>'
    '</div></div>'
    '<p class="sub" style="text-align:center;max-width:52ch">Você olha mil vezes e está tudo '
    'certo. ' + A + '</p>')

# ── 03 ─────────────────────────────────────────────────────────
add('03', 'Tudo que decide', 'inventário',
    'Pega o segundo argumento do texto atual, <b>"não é sobre a escrita"</b> ' + A + ', e o torna '
    'concreto. A escrita vira UM item numa lista de doze, e a quantidade é o argumento: não é que '
    'a escrita não importe, é que ela é um doze avos da conta. Quem escreveu sozinho reconhece na '
    'hora quantos desses itens nunca olhou.',
    '<div class="meio"><p class="eyebrow">Não é sobre a escrita</p>'
    '<h2 class="h2">A escrita é uma das doze coisas<br>'
    '<span class="serifa">que decidem se o seu livro vende.</span></h2></div>'
    '<div class="inv">'
    '<span class="escrita">A escrita</span><span>A capa</span><span>O título</span>'
    '<span>O subtítulo</span><span>A quarta capa</span><span>A sinopse</span>'
    '<span>A categoria</span><span>As palavras-chave</span><span>O preço</span>'
    '<span>O formato</span><span>Para quem é</span><span>O lançamento</span></div>'
    '<p class="conta-itens">Você cuidou de <b>uma</b>.<br>Alguém precisa olhar as outras onze.</p>')

# ── 04 ─────────────────────────────────────────────────────────
add('04', 'Os dois lados da capa', 'contraste',
    'Duas colunas: o que passa na sua cabeça quando você olha o seu livro, e o que passa na cabeça '
    'de quem nunca ouviu falar dele. O argumento do ponto cego fica evidente sem precisar ser dito, '
    'porque as duas listas não têm um item em comum. É a versão mais fria e a mais fácil de ler no '
    'celular.',
    '<div class="meio"><p class="eyebrow">O ponto cego</p>'
    '<h2 class="h2">Você e o seu leitor<br><span class="serifa">não estão olhando a mesma coisa.</span></h2></div>'
    '<div class="dois">'
    '<div class="lado voce"><p class="k">O que você vê</p><ul>'
    '<li>Dois anos de trabalho</li><li>O capítulo que te custou caro</li>'
    '<li>A frase que você não deixou cortarem</li><li>Tudo que você já sabe sobre o assunto</li>'
    '<li>O livro inteiro, de uma vez</li></ul></div>'
    '<div class="lado fora"><p class="k">O que o leitor vê</p><ul>'
    '<li>Uma miniatura entre outras trinta</li><li>Um título que ele não estava procurando</li>'
    '<li>Três linhas de sinopse, se tanto</li><li>Nada sobre você</li>'
    '<li>Quatro segundos, e a próxima capa</li></ul></div></div>'
    '<p class="sub" style="text-align:center">É sobre tudo que decide se o leitor certo encontra, '
    'escolhe e recomenda. ' + A + '</p>')

# ── 05 ─────────────────────────────────────────────────────────
add('05', 'Três que não viam', 'prova',
    'Troca o argumento por <b>prova</b>. Os três autores que já estão na página, mas aqui usados '
    'pelo que têm em comum: os três tinham o livro pronto e nenhum dos três enxergava o que estava '
    'errado. <b>Vantagem:</b> resolve de uma vez a repetição, porque o bloco de prova mais adiante '
    'passa a ser dispensável. <b>Risco:</b> gasta a prova antes do preço.',
    '<div class="meio"><p class="eyebrow">Por que sozinho não dá</p>'
    '<h2 class="h2">Nenhum dos três estava errado sobre o livro.<br>'
    '<span class="serifa">Os três estavam cegos para uma coisa só.</span></h2></div>'
    '<div class="tres">'
    '<div class="quem"><p class="n">Robson Leite<small>Livro pronto, conteúdo elogiado</small></p>'
    '<p class="f">“Às vezes a sua capa <b>não comunica o conteúdo</b> do seu livro.”</p></div>'
    '<div class="quem"><p class="n">Cláudio Yamaguchi<small>Anos escrevendo</small></p>'
    '<p class="f">Faltava ele na própria obra. Um toque de fora: <b>“coloca mais você”</b>.</p></div>'
    '<div class="quem"><p class="n">Luiz Valério<small>Nove livros publicados</small></p>'
    '<p class="f">Ligou para a editora no meio da produção: <b>“terei de refazer a capa, a '
    'contracapa e a sinopse”</b>.</p></div></div>'
    '<p class="fecho">Você olha mil vezes e está tudo certo. ' + A + '<br>'
    '<span class="serifa" style="color:var(--ac)">Outra pessoa olha dez segundos.</span></p>')


def main():
    itens = ''.join(
        '<section class="item"><div class="w">'
        '<div class="cab"><span class="no">%s</span><h2>%s</h2><span class="mec">%s</span></div>'
        '<p class="tese">%s</p><div class="palco">%s</div></div></section>'
        % (no, nome, mec, tese, html) for no, nome, mec, tese, html in V)

    page = (
        '<title>Por que sozinho não dá</title>'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@400;700&'
        'family=Fraunces:ital,wght@1,500&display=swap">'
        '<style>' + CSS + '</style>'
        '<header><div class="w"><p class="eyebrow">Upsell do 90D · a seção da ponte</p>'
        '<h1>Cinco jeitos de provar<br><span class="serifa">que sozinho não dá.</span></h1>'
        '<p>A seção de hoje <b>afirma</b> que você não enxerga o próprio erro e não mostra nada. '
        'Ela é a ponte entre a conta e a oferta, carrega o argumento que justifica a call inteira, '
        'e é um parágrafo centralizado logo depois do momento mais forte da página. Além disso '
        'empilha dois argumentos diferentes: <b>você não vê o seu erro</b> e <b>não é sobre a '
        'escrita</b>. Cada alternativa escolhe qual carregar, e por qual mecanismo.</p>'
        '<p class="nota">O que está marcado <span class="atual">atual</span> é texto que já existe '
        'na página. O resto é proposta minha e precisa passar pela Dany antes de ir pro ar.</p>'
        '</div></header>' + itens +
        '<footer><div class="w">The Book Business · alternativas para a seção da ponte</div></footer>'
        '<script>' + JS + '</script>')

    if '--artifact' not in sys.argv:
        page = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1">'
                '<meta name="robots" content="noindex"></head><body>' + page + '</body></html>')
    io.open(OUT, 'w', encoding='utf-8').write(page)
    print('  %d direções -> %s  (%.0f KB)' % (len(V), OUT, len(page.encode('utf-8')) / 1024.0))


if __name__ == '__main__':
    main()
