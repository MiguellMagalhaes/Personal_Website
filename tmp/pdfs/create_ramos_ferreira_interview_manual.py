from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path('/Users/miguelmagalhaes/Documents/GitHub/Personal_Website')
OUTPUT = ROOT / 'output/pdf/Manual_Entrevista_Ramos_Ferreira_Miguel_Magalhaes.pdf'
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = A4
NAVY = colors.HexColor('#152238')
BLUE = colors.HexColor('#2563EB')
LIGHT_BLUE = colors.HexColor('#EAF1FF')
PALE = colors.HexColor('#F5F7FA')
TEXT = colors.HexColor('#1F2937')
MUTED = colors.HexColor('#5B6472')
GREEN = colors.HexColor('#147D64')
ORANGE = colors.HexColor('#D97706')
RED = colors.HexColor('#B42318')
LINE = colors.HexColor('#D7DDE7')


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='CoverTitle', parent=styles['Title'], fontName='Helvetica-Bold',
    fontSize=25, leading=30, textColor=NAVY, alignment=TA_LEFT,
    spaceAfter=12,
))
styles.add(ParagraphStyle(
    name='CoverSub', parent=styles['Normal'], fontName='Helvetica',
    fontSize=12.5, leading=18, textColor=MUTED, spaceAfter=9,
))
styles.add(ParagraphStyle(
    name='H1x', parent=styles['Heading1'], fontName='Helvetica-Bold',
    fontSize=17, leading=21, textColor=NAVY, spaceBefore=4, spaceAfter=9,
))
styles.add(ParagraphStyle(
    name='H2x', parent=styles['Heading2'], fontName='Helvetica-Bold',
    fontSize=11.5, leading=15, textColor=BLUE, spaceBefore=7, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name='Bodyx', parent=styles['BodyText'], fontName='Helvetica',
    fontSize=9.4, leading=13.4, textColor=TEXT, spaceAfter=5,
))
styles.add(ParagraphStyle(
    name='Smallx', parent=styles['BodyText'], fontName='Helvetica',
    fontSize=7.8, leading=10.5, textColor=MUTED, spaceAfter=3,
))
styles.add(ParagraphStyle(
    name='Bulletx', parent=styles['BodyText'], fontName='Helvetica',
    fontSize=9.2, leading=13, textColor=TEXT, leftIndent=12,
    firstLineIndent=-7, bulletIndent=0, spaceAfter=3,
))
styles.add(ParagraphStyle(
    name='Quotex', parent=styles['BodyText'], fontName='Helvetica-Oblique',
    fontSize=9.4, leading=13.8, textColor=NAVY, leftIndent=12,
    rightIndent=8, borderColor=BLUE, borderWidth=0, borderPadding=7,
    backColor=LIGHT_BLUE, spaceBefore=4, spaceAfter=7,
))
styles.add(ParagraphStyle(
    name='BoxTitle', parent=styles['BodyText'], fontName='Helvetica-Bold',
    fontSize=10.2, leading=13, textColor=colors.white, spaceAfter=0,
))
styles.add(ParagraphStyle(
    name='TableHead', parent=styles['BodyText'], fontName='Helvetica-Bold',
    fontSize=8.1, leading=10, textColor=colors.white, alignment=TA_CENTER,
))
styles.add(ParagraphStyle(
    name='TableCell', parent=styles['BodyText'], fontName='Helvetica',
    fontSize=7.9, leading=10.2, textColor=TEXT,
))
styles.add(ParagraphStyle(
    name='TableCellCenter', parent=styles['BodyText'], fontName='Helvetica',
    fontSize=7.9, leading=10.2, textColor=TEXT, alignment=TA_CENTER,
))


def P(text, style='Bodyx'):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph(f'- {text}', styles['Bulletx'])


def section_title(text):
    return Paragraph(text, styles['H1x'])


def label_box(title, body, color=BLUE):
    data = [
        [Paragraph(title, styles['BoxTitle'])],
        [Paragraph(body, styles['Bodyx'])],
    ]
    t = Table(data, colWidths=[174 * mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), color),
        ('BACKGROUND', (0, 1), (-1, -1), PALE),
        ('BOX', (0, 0), (-1, -1), 0.7, LINE),
        ('LEFTPADDING', (0, 0), (-1, -1), 9),
        ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 7),
    ]))
    return t


def draw_page(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setFillColor(NAVY)
        canvas.rect(0, PAGE_H - 12 * mm, PAGE_W, 12 * mm, stroke=0, fill=1)
        canvas.setFillColor(colors.white)
        canvas.setFont('Helvetica-Bold', 8.2)
        canvas.drawString(18 * mm, PAGE_H - 7.7 * mm, 'MANUAL DE ENTREVISTA | RAMOS FERREIRA')
        canvas.setFont('Helvetica', 8)
        canvas.drawRightString(PAGE_W - 18 * mm, PAGE_H - 7.7 * mm, 'Miguel Magalhães')
    canvas.setStrokeColor(LINE)
    canvas.line(18 * mm, 13 * mm, PAGE_W - 18 * mm, 13 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont('Helvetica', 7.5)
    canvas.drawString(18 * mm, 8.5 * mm, 'Analista Programador de Sistemas de Negócio')
    canvas.drawRightString(PAGE_W - 18 * mm, 8.5 * mm, f'Página {doc.page}')
    canvas.restoreState()


doc = BaseDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    leftMargin=18 * mm,
    rightMargin=18 * mm,
    topMargin=18 * mm,
    bottomMargin=18 * mm,
    title='Manual de Entrevista - Analista Programador de Sistemas de Negócio',
    author='Miguel Magalhães',
    subject='Preparação para entrevista no Grupo Ramos Ferreira',
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
doc.addPageTemplates(PageTemplate(id='main', frames=frame, onPage=draw_page))

story = []

# Cover
story.extend([
    Spacer(1, 24 * mm),
    P('MANUAL DE PREPARAÇÃO', 'Smallx'),
    P('Analista Programador de<br/>Sistemas de Negócio', 'CoverTitle'),
    P('Grupo Ramos Ferreira Engenharia | Vila Nova de Gaia', 'CoverSub'),
    Spacer(1, 5 * mm),
    label_box(
        'OBJETIVO DA ENTREVISTA',
        '<b>Demonstrar que sabes ligar tecnologia ao negócio.</b> A tua combinação de Engenharia Informática, desenvolvimento, suporte a utilizadores e experiência prática com PHC permite-te compreender necessidades, investigar problemas e transformar pedidos em soluções úteis.',
        NAVY,
    ),
    Spacer(1, 8 * mm),
    Table([
        [P('<b>Compatibilidade estimada</b><br/><font color="#147D64">8,5 / 10</font>', 'Bodyx'),
         P('<b>Mensagem principal</b><br/>Já trabalhei com PHC na NewCoffee e desempenhei funções semelhantes às de um consultor júnior.', 'Bodyx')],
        [P('<b>Âncora salarial</b><br/>1.500 euros brutos x 14 + alimentação + variável', 'Bodyx'),
         P('<b>Chão privado</b><br/>1.300 euros brutos x 14 + alimentação separada', 'Bodyx')],
    ], colWidths=[86 * mm, 86 * mm], style=TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), PALE),
        ('BOX', (0, 0), (-1, -1), 0.6, LINE),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, LINE),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ])),
    Spacer(1, 14 * mm),
    P('<b>Preparado para:</b> apresentação pessoal, motivação, PHC, processos de negócio, SQL, integrações, Power BI, perguntas comportamentais, remuneração e fecho da entrevista.', 'CoverSub'),
    Spacer(1, 20 * mm),
    P('Miguel Magalhães | setembro de 2026', 'Smallx'),
    PageBreak(),
])

# Page 2 - positioning
story.extend([
    section_title('1. Leitura estratégica da oportunidade'),
    P('A função não é apenas de programação. O objetivo é compreender como trabalham as diferentes áreas da empresa e apoiar a melhoria dos processos através de aplicações, ERP PHC, bases de dados e reporting.'),
    P('<b>Fluxo mental que deves transmitir:</b> problema de negócio - requisitos - dados - solução - testes - entrega - acompanhamento.'),
    P('A empresa atua desde 1981, tem mais de 800 colaboradores e presença internacional. Uma operação multiempresa e multipaís aumenta a importância de informação consistente, permissões, integrações, reporting e processos normalizados.'),
    P('O Grupo apresenta a melhoria contínua, a tecnologia, a formação e o desenvolvimento das pessoas como valores centrais. Liga a tua motivação a estes pontos.', 'Smallx'),
    P('A tua apresentação de 60 segundos', 'H2x'),
    P('Sou licenciado em Engenharia Informática e tenho também formação técnica em Redes e Sistemas Informáticos. A minha experiência combina suporte aos utilizadores, sistemas, bases de dados e desenvolvimento de soluções internas.<br/><br/>Na NewCoffee, trabalhei diretamente com PHC e desempenhei funções próximas das de um consultor júnior: apoiava utilizadores, compreendia necessidades operacionais, investigava problemas e ajudava a traduzir pedidos em soluções no sistema. Desenvolvi também uma plataforma interna de ITSM para gerir tickets, utilizadores, equipamentos e indicadores.<br/><br/>Tenho experiência com desenvolvimento web, backend, APIs, bases de dados e Git. Esta oportunidade interessa-me porque combina precisamente análise de negócio, PHC, desenvolvimento e reporting num contexto internacional.', 'Quotex'),
    P('Porque a Ramos Ferreira?', 'H2x'),
    P('Interessa-me a possibilidade de trabalhar numa empresa sólida e internacional, onde os sistemas de informação têm impacto real em várias empresas e geografias. A combinação de PHC, desenvolvimento aplicacional, análise de processos e Power BI corresponde às áreas em que já tenho bases e nas quais quero crescer.' , 'Quotex'),
    label_box(
        'IDEIA QUE O ENTREVISTADOR DEVE RETER',
        '“O Miguel já conhece PHC, comunica bem com utilizadores, compreende tecnologia e tem potencial para crescer como analista-programador orientado ao negócio.”',
        GREEN,
    ),
    PageBreak(),
])

# Page 3 - strengths and gaps
story.extend([
    section_title('2. Pontos fortes e lacunas controladas'),
    P('Pontos fortes a repetir durante a entrevista', 'H2x'),
    bullet('<b>Experiência prática com PHC:</b> contacto com utilizadores, necessidades operacionais e resolução de problemas num contexto real.'),
    bullet('<b>Perfil técnico e funcional:</b> consegues compreender tanto o sistema como a perspetiva do utilizador.'),
    bullet('<b>Desenvolvimento de soluções internas:</b> a plataforma ITSM demonstra iniciativa, análise, implementação e foco na operação.'),
    bullet('<b>Bases de dados e desenvolvimento:</b> conhecimentos de SQL, web, backend, APIs, C#/.NET, JavaScript/TypeScript, React/Next.js ou tecnologias equivalentes usadas nos teus projetos.'),
    bullet('<b>Formação:</b> Licenciatura em Engenharia Informática, CTeSP em Redes e Sistemas e evolução contínua em cibersegurança.'),
    bullet('<b>Comunicação:</b> experiência a apoiar diferentes departamentos e a adaptar a linguagem ao interlocutor.'),
    P('Como apresentar a experiência de PHC', 'H2x'),
    P('Na NewCoffee não tive apenas contacto pontual com o PHC. Apoiei utilizadores e necessidades relacionadas com o sistema e desempenhei um papel semelhante ao de um consultor júnior. Procurava compreender o processo, identificar o problema e apoiar a utilização ou a resolução adequada. Essa experiência deu-me uma base funcional importante, que quero aprofundar agora num contexto mais estruturado.', 'Quotex'),
    P('<b>Prepara antes da entrevista um exemplo real:</b> módulo ou área do PHC, pedido recebido, investigação realizada, pessoas envolvidas, solução e resultado. Não inventes funcionalidades ou parametrizações que não executaste.', 'Bodyx'),
    P('Lacunas e respostas seguras', 'H2x'),
    Table([
        [P('Tema', 'TableHead'), P('Como responder', 'TableHead')],
        [P('Power BI', 'TableCell'), P('Tenho bases em dados, reporting e indicadores. Estou a aprofundar Power Query, modelação e DAX e consigo transferir rapidamente os meus conhecimentos de bases de dados.', 'TableCell')],
        [P('T-SQL avançado', 'TableCell'), P('Tenho experiência com SQL relacional e compreendo joins, agregações, relações e transações. Estou a consolidar stored procedures, otimização e particularidades de SQL Server.', 'TableCell')],
        [P('Experiência profissional', 'TableCell'), P('Estou numa fase inicial, mas já trabalhei com utilizadores, PHC e soluções internas. Compenso a menor antiguidade com capacidade de aprendizagem, iniciativa e bases técnicas abrangentes.', 'TableCell')],
    ], colWidths=[35 * mm, 139 * mm], style=TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.5, LINE),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 7),
        ('RIGHTPADDING', (0, 0), (-1, -1), 7),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, PALE]),
    ])),
    Spacer(1, 5 * mm),
    label_box('REGRA DE OURO', 'Distingue sempre entre “usei profissionalmente”, “utilizei em projetos” e “tenho conhecimentos”. Honestidade acompanhada de aprendizagem rápida transmite mais confiança do que domínio exagerado.', ORANGE),
    PageBreak(),
])

# Page 4 - technical cheat sheet
story.extend([
    section_title('3. Revisão técnica essencial'),
    P('Análise e levantamento de requisitos', 'H2x'),
    bullet('Identificar stakeholders e compreender o processo atual - AS-IS.'),
    bullet('Clarificar problema, impacto, objetivo, exceções e dados necessários.'),
    bullet('Definir processo futuro - TO-BE - e critérios de aceitação.'),
    bullet('Priorizar, validar com o utilizador, desenvolver, testar, documentar e acompanhar.'),
    P('SQL Server', 'H2x'),
    bullet('<b>JOIN:</b> relaciona dados de tabelas diferentes. <b>GROUP BY:</b> agrega resultados.'),
    bullet('<b>PK/FK:</b> garantem identificação e relações. <b>Índice:</b> acelera leitura, mas tem custo de escrita.'),
    bullet('<b>Transação:</b> conjunto de operações que deve ser concluído ou revertido como unidade.'),
    bullet('<b>Stored procedure:</b> rotina SQL guardada na base de dados, reutilizável e parametrizável.'),
    P('ERP PHC', 'H2x'),
    bullet('Integra dados e processos como clientes, fornecedores, compras, vendas, stocks, faturação, projetos e contabilidade.'),
    bullet('Antes de alterar: perceber impacto entre módulos, permissões, validações, auditoria, testes e possibilidade de reversão.'),
    bullet('O valor do consultor está em compreender o processo, não apenas em conhecer menus.'),
    P('Power BI', 'H2x'),
    bullet('<b>Power Query:</b> extração e transformação. <b>Modelo:</b> tabelas e relações.'),
    bullet('<b>DAX:</b> medidas e cálculos. <b>RLS:</b> controlo de acesso por utilizador.'),
    bullet('Um dashboard deve responder a perguntas de negócio, usar indicadores claros e ter dados confiáveis.'),
    P('Desenvolvimento e integração', 'H2x'),
    bullet('Frontend: React/Next.js. Backend: Node.js ou .NET/C#. Comunicação: APIs REST e JSON.'),
    bullet('Integrações: autenticação, validação, mapeamento, logs, tratamento de erros, testes e prevenção de duplicados.'),
    bullet('Git: branches, commits claros, pull requests e revisão antes de integrar alterações.'),
    label_box('CENÁRIO PROVÁVEL', '<b>“Um departamento pede uma nova funcionalidade no PHC.”</b><br/>Ouço o utilizador, documento o processo e objetivo, verifico se a necessidade já é suportada, avalio impactos e dados, proponho solução, valido critérios, implemento primeiro em testes, obtenho validação e só depois promovo para produção com documentação e plano de reversão.', BLUE),
    PageBreak(),
])

# Page 5 - interview Q&A
story.extend([
    section_title('4. Perguntas prováveis e respostas'),
    P('“Conta-me uma situação em que melhoraste um processo.”', 'H2x'),
    P('Usa a plataforma ITSM. Estrutura STAR: existia necessidade de organizar tickets, equipamentos, utilizadores ou indicadores; analisaste o processo; desenvolveste a solução; o resultado foi maior centralização, rastreabilidade e visibilidade operacional.', 'Quotex'),
    P('“Como levantas requisitos?”', 'H2x'),
    P('Começo por ouvir os utilizadores e compreender o processo atual, o problema e o impacto. Identifico stakeholders, dados, exceções e prioridades. Depois documento os requisitos e critérios de aceitação, valido o entendimento e só então avanço para proposta técnica, implementação e testes.', 'Quotex'),
    P('“Como geres prioridades concorrentes?”', 'H2x'),
    P('Avalio impacto, urgência, risco, utilizadores afetados e dependências. Quando existem conflitos, apresento a análise aos responsáveis, alinho a decisão e documento a prioridade acordada.', 'Quotex'),
    P('“Porque devemos contratar-te?”', 'H2x'),
    P('Porque reúno três dimensões importantes para esta função: formação em Engenharia Informática, experiência prática com PHC e utilizadores, e capacidade de desenvolver soluções e trabalhar com dados. Consigo comunicar com as áreas de negócio, investigar tecnicamente e aprender rapidamente. Quero transformar essa base numa especialização sólida em sistemas de negócio.', 'Quotex'),
    P('“O que fazes quando não sabes resolver?”', 'H2x'),
    P('Primeiro reúno evidência e delimito o problema. Consulto documentação, logs e histórico, testo hipóteses de forma controlada e evito alterações arriscadas em produção. Se precisar de escalar, entrego contexto, testes realizados e resultados, para não transferir apenas o problema.', 'Quotex'),
    P('Apresentação curta em inglês', 'H2x'),
    P('I am a Computer Engineering graduate with additional technical education in Computer Networks and Systems. At NewCoffee, I worked directly with PHC and supported users in a role similar to a junior functional consultant. My experience also includes databases, web and backend development, APIs, Git and an internal ITSM platform. I am interested in this position because it combines business analysis, ERP, application development and reporting.', 'Quotex'),
    PageBreak(),
])

# Page 6 - salary and closing
story.extend([
    section_title('5. Remuneração, perguntas e fecho'),
    P('O anúncio indica 17.500 a 22.900 euros anuais com componente fixa e variável. Confirma se são 14 pagamentos, se a alimentação está fora do intervalo e quanto da remuneração depende de objetivos.'),
    Table([
        [P('Patamar', 'TableHead'), P('Base mensal x 14', 'TableHead'), P('Base anual', 'TableHead'), P('Estratégia', 'TableHead')],
        [P('<b>Muito bom</b>', 'TableCell'), P('<b>1.550 €</b>', 'TableCellCenter'), P('21.700 €', 'TableCellCenter'), P('Alimentação + variável até ao topo anunciado.', 'TableCell')],
        [P('<b>Bom / objetivo</b>', 'TableCell'), P('<b>1.450 €</b>', 'TableCellCenter'), P('20.300 €', 'TableCellCenter'), P('Alimentação e variável separadas.', 'TableCell')],
        [P('<b>Chão privado</b>', 'TableCell'), P('<b>1.300 €</b>', 'TableCellCenter'), P('18.200 €', 'TableCellCenter'), P('Não revelar. Alimentação sempre separada.', 'TableCell')],
    ], colWidths=[36 * mm, 37 * mm, 34 * mm, 67 * mm], style=TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('GRID', (0, 0), (-1, -1), 0.5, LINE),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#EAF8F3'), LIGHT_BLUE, colors.HexColor('#FFF3E8')]),
    ])),
    P('Resposta salarial recomendada', 'H2x'),
    P('Considerando as responsabilidades da função, o intervalo divulgado e o alinhamento da posição com a minha formação e experiência prática em PHC, procuro uma componente fixa próxima dos 1.500 euros brutos mensais, pagos em 14 meses, acrescida do subsídio de alimentação e da componente variável. Estou disponível para compreender melhor a estrutura do pacote e discutir o valor global.', 'Quotex'),
    P('Perguntas a fazer', 'H2x'),
    bullet('Como se divide a função entre PHC, levantamento de requisitos, desenvolvimento e Power BI?'),
    bullet('Que módulos e versão do PHC utilizam? Existem customizações internas?'),
    bullet('Como é composta a equipa e o que esperam nos primeiros três meses?'),
    bullet('Existe formação em PHC, Power BI ou processos internos?'),
    bullet('Como funciona a componente variável e quais são os critérios?'),
    bullet('O intervalo anual inclui variável e alimentação? Qual é o tipo de contrato?'),
    P('Se perguntarem pela disponibilidade', 'H2x'),
    P('Tenho um compromisso profissional com início previsto nos próximos dias. No entanto, esta oportunidade está especialmente alinhada com desenvolvimento, PHC e sistemas de negócio, pelo que tenho muito interesse em compreender o calendário do processo. Quero ser transparente e tomar uma decisão responsável.', 'Quotex'),
    P('Fecho', 'H2x'),
    P('Obrigado por me explicarem melhor a função. A conversa reforçou o meu interesse porque a posição reúne PHC, análise de processos, desenvolvimento, bases de dados e reporting. Acredito que a minha experiência prática com PHC, capacidade de aprendizagem e facilidade em trabalhar com utilizadores me permitirão contribuir e evoluir rapidamente dentro da equipa.', 'Quotex'),
    label_box('ÚLTIMOS 10 MINUTOS', 'CV e anúncio abertos. Um exemplo real de PHC preparado. Um exemplo da plataforma ITSM em formato STAR. Confirmar câmara, microfone e ligação. Entrar 8 a 10 minutos antes. Falar devagar, responder com estrutura e nunca inventar.', GREEN),
    Spacer(1, 5 * mm),
    P('Fontes institucionais consultadas: ramosferreira.com - Mensagem do Presidente; Missão, Visão e Valores; Política do Sistema de Gestão. Estimativas líquidas não incluídas por dependerem da situação fiscal individual.', 'Smallx'),
])

doc.build(story)
print(OUTPUT)
