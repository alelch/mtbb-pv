# -*- coding: utf-8 -*-
"""
Copy REAL da pagina de upsell (Diagnostico do Autor), extraida de
../index.html em 10/09/2026. As 10 propostas de design usam ESTE arquivo,
entao o texto e' identico nas dez e a comparacao e' so' de DESIGN.

Se a copy mudar na pagina de verdade, mudar aqui e rodar gera.py de novo.
"""

C = {
 'title': 'Diagnóstico do Autor | The Book Business',
 'passos': [('✓', 'Passo 1', '90D garantido', 'feito'),
            ('2', 'Passo 2', 'Acelere o resultado', 'agora'),
            ('3', 'Passo 3', 'Acesso liberado', '')],
 'parabens1': 'Parabéns! Você já tem o caminho para o seu livro estrear vendendo,',
 'parabens2': 'mas o seu pedido ainda não está finalizado.',
 'h1a': 'Você já sabe como lançar.',
 'h1b': 'Mas o seu livro está bom de verdade?',
 'lead': 'Aperta o play que eu tenho um recado rápido para você.',
 'mate': [('Livro bom + lançamento ruim', 'ninguém descobre.', 0),
          ('Lançamento bom + livro ruim', 'vende no lançamento. Depois, esquecido.', 0),
          ('Lançamento bom + livro bom', 'muda a vida do autor.', 1)],
 'erro_a': 'Um erro só pode fazer o seu livro inteiro falhar.',
 'erro_b': ('E ninguém enxerga o próprio erro: você olha mil vezes e está tudo certo, '
            'outra pessoa olha dez segundos e aponta o que estava na sua cara.'),
 'erro_c': 'Não é sobre a escrita.',
 'erro_d': 'É sobre tudo que decide se o leitor certo encontra, escolhe e recomenda.',
 'rot': 'A gente, trabalhando junto no seu livro. Quer?',
 'nome': 'Diagnóstico do Autor',
 'preco': '697',
 'avista': 'à vista, ou em até <b>12x no cartão</b>',
 'obs': '* parcelado no cartão, com juros',
 'cta': 'Sim! Adicione ao meu pedido',
 'cta2': 'Eu quero o meu diagnóstico',
 'abate': ('Se depois você entrar no <b>Direcionamento Estratégico</b>, '
           'os R$697 são abatidos integralmente.'),
 'gar_h': 'Se ao fim da hora você achar que não valeu, devolvemos',
 'gar_p': 'Sem justificar. E o material continua seu.',
 'gar_pre': 'Agora ficou mais fácil decidir, né?',
 'hora_h': 'A sua hora, por dentro',
 'hora': [('5 min', 'Quem é você e onde o livro está', ''),
          ('5 min', 'O que já está certo', ''),
          ('40 min', 'Os seus próximos passos',
           'O que falta, o tipo de publicação certo, e <b>as três frentes de lançamento '
           'do seu livro</b>, escolhidas entre quinze.'),
          ('10 min', 'Dúvidas, e uma conversa honesta',
           'Se o seu caso for de algo que a gente faz, a gente conta. Se não for, não conta.')],
 'entr_h': 'Você sai com um plano de ação e os próximos passos mapeados.',
 'entregas': ['<b>O que consertar primeiro</b>, e o que deixar pra depois',
              '<b>As três frentes escolhidas</b> para o seu livro',
              '<b>A gravação</b>, sua mesmo se pedir o dinheiro de volta'],
 'prova_h': 'Quem já passou por essa leitura',
 'provas': [
   ('Robson Leite',
    'Livro pronto, <b>conteúdo elogiado</b> por quem leu.',
    '“Às vezes a sua capa <b>não comunica o conteúdo</b> do seu livro.”',
    'https://youtu.be/hW7NjsY2WrA'),
   ('Cláudio Yamaguchi',
    'Anos escrevendo sobre comportamento humano. <b>“Não é isso que eu queria fazer.”</b>',
    'Um toque de fora: <b>“coloca mais você”</b>. Hoje os leitores dizem: “eu vejo você nessa obra”.',
    'https://youtu.be/6mhrEgy2Uvc'),
   ('Luiz Valério',
    'Nove livros publicados. <b>Nenhum pensado para vender.</b>',
    'Ligou para a editora no meio da produção: <b>“terei de refazer a capa, a contracapa e a sinopse”</b>.',
    'https://youtu.be/6pMViMbw6GA')],
 'nota_prova': ('Alunos do Método. A leitura que alguém fez do caso deles é a que '
                'acontece na sua hora.'),
 'recap_h': 'Recapitulando',
 'recap': ['Uma hora no Zoom só sobre o seu livro',
           'Um plano de ação, com o que fazer primeiro',
           'Três frentes de lançamento escolhidas para você',
           'A gravação, para sempre'],
 'recusa': 'Não quero o diagnóstico. Seguir só com o Lançamento 90D.',
 'escassez': ('Esta oferta só existe aqui, para quem acabou de comprar o 90D. E ela só está '
              'na sua frente porque ainda há vaga este mês. Cada diagnóstico é uma hora de '
              'agenda do time: quando as vagas acabam, esta página deixa de aparecer. Se você '
              'fechar, a vaga fica para o próximo autor que chegar aqui.'),
 'faq': [
   ('A call é com a Dany?',
    'Não. É com um especialista do time dela, com o critério dela. Por isso custa isto, '
    'e não alguns milhares de reais.'),
   ('Vocês vão ler o meu livro?',
    'Não o manuscrito inteiro. O que a gente olha é o que decide se ele vai ser encontrado, '
    'escolhido e lembrado: para quem ele é, como se apresenta, como foi publicado e como vai '
    'ser lançado. É aí que mora a diferença entre livro profissional e livro amador.'),
   ('Isso não é uma reunião de vendas disfarçada?',
    'Cinquenta minutos são sobre o seu caso. Dez são de conversa, e só se o seu caso for de '
    'algo que a gente faz. Está escrito acima, antes de você pagar.')],
 'rodape': 'The Book Business · Dany Sakugawa',
}

# os 10 rumos: (pasta, nome, uma linha de tese)
RUMOS = [
 ('01-editorial',   'Editorial',        'Revista literária: serifa grande, fio fino, muito respiro.'),
 ('02-jacket',      'Capa de livro',    'A página inteira é a sobrecapa: lombada, orelha, quarta capa.'),
 ('03-ficha',       'Ficha catalográfica', 'Catálogo de biblioteca: monoespaçada, campos, carimbo.'),
 ('04-noir',        'Noir premium',     'Quase preto, fio de ouro, tipo leve e enorme. Silêncio caro.'),
 ('05-relatorio',   'Relatório clínico','A página vira o próprio diagnóstico: matriz, status, laudo.'),
 ('06-suico',       'Suíço',            'Grade rígida, preto e um vermelho, numeração 01–07.'),
 ('07-marginalia',  'Marginalia',       'Alguém leu o seu livro e anotou na margem, à caneta.'),
 ('08-brutal',      'Neo-brutalista',   'Borda preta grossa, sombra dura, tipo gigante, um acento elétrico.'),
 ('09-cinema',      'Cinema',           'Tela cheia, letterbox, grão, sequência de planos.'),
 ('10-carta',       'Carta',            'Sem design: uma coluna, texto preto, assinatura. Parece pessoal.'),
]


def doc(css, body, fonts='', extra_head=''):
    """Esqueleto comum. Cada rumo manda o SEU css e o SEU markup."""
    f = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="' + fonts + '">') if fonts else ''
    return ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="robots" content="noindex">'
            '<title>' + C['title'] + '</title>' + f + extra_head +
            '<style>' + css + '</style></head><body>' + body +
            '<div class="proto-tag">protótipo de design · sem checkout</div>'
            '<style>.proto-tag{position:fixed;left:10px;bottom:10px;z-index:99;'
            'font:600 10px/1 ui-sans-serif,system-ui;letter-spacing:.1em;text-transform:uppercase;'
            'background:#111;color:#fff;padding:7px 10px;border-radius:99px;opacity:.55}</style>'
            '</body></html>')
