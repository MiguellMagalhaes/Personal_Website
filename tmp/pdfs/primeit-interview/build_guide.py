from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)


OUT = Path("/Users/miguelmagalhaes/Documents/GitHub/Personal_Website/output/pdf/Guiao_Entrevista_PrimeIT_Miguel_Magalhaes.pdf")
OUT.parent.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = A4
GREEN = colors.HexColor("#45E300")
GREEN_DARK = colors.HexColor("#258A16")
CHARCOAL = colors.HexColor("#263129")
MID = colors.HexColor("#5F6B63")
LIGHT = colors.HexColor("#F1F5F1")
PALE_GREEN = colors.HexColor("#EAF9E6")
PALE_YELLOW = colors.HexColor("#FFF7DA")
PALE_RED = colors.HexColor("#FDECEC")
LINE = colors.HexColor("#D5DDD6")

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", "/System/Library/Fonts/Supplemental/Arial Italic.ttf"))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", fontName="Arial-Bold", fontSize=25, leading=29,
    textColor=CHARCOAL, spaceAfter=7 * mm,
))
styles.add(ParagraphStyle(
    name="CoverSub", fontName="Arial", fontSize=13, leading=17,
    textColor=MID, spaceAfter=8 * mm,
))
styles.add(ParagraphStyle(
    name="H1x", fontName="Arial-Bold", fontSize=17, leading=21,
    textColor=CHARCOAL, spaceAfter=5 * mm,
))
styles.add(ParagraphStyle(
    name="H2x", fontName="Arial-Bold", fontSize=11.5, leading=14,
    textColor=GREEN_DARK, spaceBefore=3 * mm, spaceAfter=2 * mm,
))
styles.add(ParagraphStyle(
    name="Bodyx", fontName="Arial", fontSize=9.4, leading=13,
    textColor=CHARCOAL, spaceAfter=2.2 * mm,
))
styles.add(ParagraphStyle(
    name="Smallx", fontName="Arial", fontSize=8, leading=10.5,
    textColor=MID, spaceAfter=1.6 * mm,
))
styles.add(ParagraphStyle(
    name="Bulletx", fontName="Arial", fontSize=9.1, leading=12.5,
    textColor=CHARCOAL, leftIndent=5 * mm, firstLineIndent=-3.5 * mm,
    bulletIndent=1.5 * mm, spaceAfter=1.5 * mm,
))
styles.add(ParagraphStyle(
    name="Qx", fontName="Arial-Bold", fontSize=9.6, leading=12.5,
    textColor=CHARCOAL, spaceBefore=2 * mm, spaceAfter=1 * mm,
))
styles.add(ParagraphStyle(
    name="Answerx", fontName="Arial", fontSize=9, leading=12.3,
    textColor=CHARCOAL, leftIndent=4 * mm, borderColor=GREEN,
    borderWidth=1.5, borderPadding=(0, 0, 0, 4 * mm), spaceAfter=2.5 * mm,
))
styles.add(ParagraphStyle(
    name="Quote", fontName="Arial-Italic", fontSize=9.2, leading=13,
    textColor=CHARCOAL, leftIndent=5 * mm, rightIndent=4 * mm,
    spaceAfter=2.5 * mm,
))
styles.add(ParagraphStyle(
    name="Codex", fontName="Courier", fontSize=7.7, leading=10,
    textColor=CHARCOAL, leftIndent=4 * mm, rightIndent=4 * mm,
    backColor=LIGHT, borderColor=LINE, borderWidth=0.5,
    borderPadding=4 * mm, spaceAfter=3 * mm,
))
styles.add(ParagraphStyle(
    name="Foot", fontName="Arial", fontSize=7.2, leading=9,
    textColor=MID,
))


def P(text, style="Bodyx"):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph("- " + text, styles["Bulletx"])


def callout(title, body, color=PALE_GREEN):
    table = Table([[P(title, "Qx"), P(body, "Bodyx")]], colWidths=[42 * mm, 122 * mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
    ]))
    return table


def qa(question, answer):
    return KeepTogether([P(question, "Qx"), P(answer, "Answerx")])


def on_page(canvas, doc):
    page = canvas.getPageNumber()
    canvas.saveState()
    if page == 1:
        canvas.setFillColor(GREEN)
        canvas.rect(0, PAGE_H - 18 * mm, PAGE_W, 18 * mm, fill=1, stroke=0)
        canvas.setFillColor(CHARCOAL)
        canvas.rect(0, PAGE_H - 21 * mm, PAGE_W, 3 * mm, fill=1, stroke=0)
    else:
        canvas.setFillColor(GREEN)
        canvas.rect(0, PAGE_H - 7 * mm, PAGE_W, 7 * mm, fill=1, stroke=0)
        canvas.setStrokeColor(LINE)
        canvas.line(18 * mm, 15 * mm, PAGE_W - 18 * mm, 15 * mm)
        canvas.setFont("Arial", 7.5)
        canvas.setFillColor(MID)
        canvas.drawString(18 * mm, 9.5 * mm, "Miguel Magalhães | Preparação PrimeIT")
        canvas.drawRightString(PAGE_W - 18 * mm, 9.5 * mm, str(page))
    canvas.restoreState()


doc = BaseDocTemplate(
    str(OUT), pagesize=A4,
    leftMargin=18 * mm, rightMargin=18 * mm,
    topMargin=20 * mm, bottomMargin=20 * mm,
    title="Guião de Preparação para Entrevista PrimeIT",
    author="Miguel Magalhães",
    subject="Entrevista para IT Support - Murex",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=on_page)])

story = []

# Cover
story += [
    Spacer(1, 20 * mm),
    P("GUIÃO DE PREPARAÇÃO", "Smallx"),
    P("Entrevista PrimeIT<br/>IT Support - Murex", "CoverTitle"),
    P("Miguel Magalhães | 8 de outubro de 2026 | 11h30 | Microsoft Teams", "CoverSub"),
]
facts = [
    [P("Entrevistadora", "Smallx"), P("Mafalda Romãozinho - Talent Recruiter", "Bodyx")],
    [P("Formato", "Smallx"), P("Entrevista de 30 minutos, provavelmente focada em perfil, motivação, experiência, disponibilidade e enquadramento salarial.", "Bodyx")],
    [P("Local / modelo", "Smallx"), P("Porto | Híbrido | Tempo integral", "Bodyx")],
    [P("Pontos centrais", "Smallx"), P("Suporte L1/L2, SQL, inglês B2 e interesse em aprender Murex.", "Bodyx")],
]
t = Table(facts, colWidths=[35 * mm, 129 * mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), LIGHT),
    ("BOX", (0, 0), (-1, -1), 0.6, LINE),
    ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm),
    ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
    ("TOPPADDING", (0, 0), (-1, -1), 2.5 * mm),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
]))
story += [t, Spacer(1, 7 * mm), P("Objetivo da entrevista", "H2x")]
story += [P(
    "Mostrar que tens bases práticas sólidas para suporte e aplicações, comunicas com clareza, és transparente sobre a experiência que ainda não tens e tens capacidade para aprender rapidamente num projeto mais exigente.",
    "Bodyx",
)]
story += [P("As três mensagens que devem ficar", "H2x")]
story += [
    bullet("Já trabalhaste com volume real: centenas de utilizadores, cinco localizações e cerca de 20 a 40 pedidos diários."),
    bullet("Tens experiência transferível para suporte aplicacional: incidentes, escalonamento, Active Directory, Microsoft 365, SQL Server, ERP, VPN e documentação."),
    bullet("Não utilizaste Murex, mas compreendes a função da plataforma e estás preparado para aprender sem fingir experiência que não tens."),
    Spacer(1, 5 * mm),
    callout("Regra principal", "Responde com exemplos concretos e frases curtas. Não tentes compensar a diferença de anos de experiência com exageros.", PALE_YELLOW),
    PageBreak(),
]

# Page 2
story += [P("1. Leitura estratégica da vaga", "H1x")]
story += [P("O que a PrimeIT procura", "H2x")]
role_rows = [
    [P("Requisito", "Smallx"), P("Como te posicionar", "Smallx")],
    [P("Mais de 4 anos em L1/L2", "Bodyx"), P("Reconhecer que tens cerca de dois anos combinados e mais de um ano diretamente focado em suporte. Compensar com escala, diversidade e aprendizagem rápida.", "Bodyx")],
    [P("Consultas SQL", "Bodyx"), P("Referir Microsoft SQL Server, consultas para validação e análise de dados, apoio à plataforma ITSM e integração com ERP.", "Bodyx")],
    [P("Murex como vantagem", "Bodyx"), P("Dizer claramente que ainda não usaste. Demonstrar preparação sobre MX.3 e relacionar com suporte aplicacional, dados, integrações e incidentes.", "Bodyx")],
    [P("Inglês B2", "Bodyx"), P("Estar preparado para responder durante dois ou três minutos em inglês sobre o teu percurso e uma situação de suporte.", "Bodyx")],
]
rt = Table(role_rows, colWidths=[48 * mm, 116 * mm], repeatRows=1)
rt.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), CHARCOAL),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
    ("BOX", (0, 0), (-1, -1), 0.6, LINE),
    ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm),
    ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
    ("TOPPADDING", (0, 0), (-1, -1), 2.3 * mm),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2.3 * mm),
]))
story += [rt, Spacer(1, 4 * mm), P("Pontos fortes confirmados pelo teu dossier", "H2x")]
story += [
    bullet("Suporte de primeira linha num ambiente empresarial distribuído."),
    bullet("Gestão de utilizadores, grupos, permissões e acessos em Active Directory."),
    bullet("Windows, Microsoft 365, VPN, DHCP, equipamentos, periféricos e aplicações empresariais."),
    bullet("Registo, priorização, documentação, acompanhamento e escalonamento de incidentes."),
    bullet("Microsoft SQL Server, SQL, ERP e desenvolvimento de plataforma interna ITSM/ativos."),
    bullet("Comunicação com utilizadores técnicos e não técnicos."),
]
story += [P("Riscos a gerir", "H2x")]
story += [
    callout("Experiência", "A vaga está classificada como Mid e pede mais de quatro anos. Não escondas a diferença. Mostra potencial e pergunta se existem projetos compatíveis com o teu nível.", PALE_RED),
    Spacer(1, 2 * mm),
    callout("Murex", "Nunca digas que tens experiência prática. O anúncio apresenta Murex como uma vantagem, não como requisito obrigatório.", PALE_YELLOW),
    PageBreak(),
]

# Page 3
story += [P("2. Apresentação inicial", "H1x")]
story += [P("Versão recomendada - cerca de 60 segundos", "H2x")]
story += [P(
    "Sou o Miguel Magalhães, licenciado em Engenharia Informática e atualmente frequento o Mestrado em Cibersegurança e Auditoria de Sistemas Informáticos. A minha experiência principal foi na NewCoffee, onde prestei suporte de primeira linha a centenas de utilizadores distribuídos por cinco localizações, tratando aproximadamente 20 a 40 pedidos por dia. Trabalhei com ambientes Windows, Active Directory, Microsoft 365, VPN, DHCP, equipamentos, aplicações empresariais e Microsoft SQL Server. Também participei no desenvolvimento e manutenção de uma plataforma interna de ITSM e gestão de ativos. Anteriormente, trabalhei em suporte ao cliente na Staples e realizei um estágio na Aquário Eletrónica, com Python, SQL Server, ERP Primavera e redes. Procuro agora evoluir para suporte L1/L2 e suporte aplicacional, num contexto mais estruturado e exigente, e esta oportunidade interessa-me pela componente de SQL, pela possibilidade de aprender Murex e pelo contacto com projetos nacionais ou internacionais.",
    "Quote",
)]
story += [P("Versão curta - cerca de 30 segundos", "H2x")]
story += [P(
    "Sou licenciado em Engenharia Informática e tenho experiência prática em suporte técnico, sistemas, redes e SQL. Na NewCoffee apoiei centenas de utilizadores em cinco localizações e tratei diariamente incidentes de hardware, software, acessos, conectividade e aplicações empresariais. Quero agora consolidar essa experiência num projeto L1/L2 e suporte aplicacional, aprofundando SQL e aprendendo ferramentas como Murex.",
    "Quote",
)]
story += [P("English introduction", "H2x")]
story += [P(
    "My name is Miguel Magalhães. I have a degree in Computer Engineering and I am currently studying for a Master's degree in Cybersecurity and Computer Systems Auditing. At NewCoffee, I provided first-line support to hundreds of users across five locations and handled around twenty to forty requests per day. My experience includes Windows, Active Directory, Microsoft 365, VPN, networking, business applications and Microsoft SQL Server. I also contributed to an internal ITSM and asset-management platform. I am now looking to progress into L1/L2 and application support, improve my technical skills and learn platforms such as Murex.",
    "Quote",
)]
story += [P("Como apresentar", "H2x")]
story += [
    bullet("Mantém contacto visual com a câmara e não leias palavra por palavra."),
    bullet("Fala mais devagar do que numa conversa normal."),
    bullet("Termina a apresentação explicando por que esta vaga é o próximo passo lógico."),
    bullet("Evita começar com dados pessoais sem relação com a função."),
    PageBreak(),
]

# Page 4
story += [P("3. Perguntas de recrutamento", "H1x")]
story += [
    qa("Porque tens interesse na PrimeIT?", "A PrimeIT permite contacto com projetos nacionais e internacionais e trabalha em áreas como IT, telecomunicações e engenharia. Interessa-me a possibilidade de evoluir num ambiente de consultoria, com diferentes desafios e aprendizagem contínua. Também me identifico com a valorização de competência, compromisso e atitude apresentada pela empresa."),
    qa("Porque te candidataste a esta vaga?", "A função junta áreas em que já tenho experiência - suporte, incidentes, Windows, Active Directory, Microsoft 365 e SQL - com áreas em que quero crescer, sobretudo suporte L2 e suporte aplicacional. A componente Murex também representa uma oportunidade de entrar num contexto tecnológico ligado ao setor financeiro."),
    qa("Que tipo de oportunidade procuras?", "Procuro uma função de suporte técnico ou aplicacional em que possa usar a minha experiência de primeira linha, assumir gradualmente incidentes mais complexos e desenvolver competências em sistemas, bases de dados, monitorização e cibersegurança."),
    qa("Quais são os teus principais pontos fortes?", "Destaco a capacidade de diagnóstico, a organização em ambientes com muitos pedidos, a comunicação com utilizadores não técnicos e a preocupação em documentar e acompanhar cada caso. Também tenho facilidade em aprender ferramentas e em relacionar suporte com redes, dados e desenvolvimento."),
    qa("Qual é uma área que ainda precisas de desenvolver?", "Quero aprofundar suporte de segunda linha, administração de sistemas e ferramentas empresariais especializadas. Tenho bases técnicas e experiência operacional, mas procuro um contexto em que possa consolidar metodologias mais avançadas de análise e resolução."),
    qa("Porque devemos considerar o teu perfil?", "Apesar de ainda não ter os quatro anos indicados, já trabalhei com utilizadores reais, múltiplas localizações, volume diário significativo, incidentes variados e escalonamento. Trago bases técnicas amplas, formação superior, responsabilidade e uma motivação concreta para evoluir rapidamente."),
    PageBreak(),
]

# Page 5
story += [P("4. Perguntas difíceis", "H1x"), Spacer(1, 4 * mm)]
story += [P("A vaga pede mais de quatro anos. Tu tens essa experiência?", "Qx")]
story += [P(
    "Ainda não tenho quatro anos diretamente em L1/L2. Tenho aproximadamente dois anos de experiência combinada em funções e projetos de TI, incluindo mais de um ano diretamente focado em suporte. Na NewCoffee trabalhei com centenas de utilizadores, cinco localizações e cerca de 20 a 40 pedidos diários. Sei que o requisito aponta para um perfil mais experiente, mas acredito que a diversidade da minha experiência e a minha capacidade de aprendizagem me permitem contribuir e evoluir rapidamente. Caso este projeto exija rigidamente mais senioridade, também tenho interesse noutras oportunidades da PrimeIT adequadas ao meu nível.",
    "Answerx",
)]
story += [P("Já trabalhaste com Murex?", "Qx")]
story += [P(
    "Ainda não trabalhei diretamente com Murex e prefiro ser transparente. Preparei-me para compreender o contexto: o MX.3 é uma plataforma integrada para mercados de capitais, utilizada em trading, risco, tesouraria, operações e processos pós-negociação. A minha experiência com SQL Server, ERP, aplicações empresariais, incidentes, integrações e documentação dá-me uma base transferível. Estou disponível para formação e motivado para aprender a plataforma de forma estruturada.",
    "Answerx",
)]
story += [callout(
    "O que saber sobre MX.3",
    "É uma plataforma empresarial de mercados de capitais. Integra front office, risco, operações e finanças. Pode envolver autenticação, serviços, monitorização, logs, integrações e bases de dados, incluindo Microsoft SQL Server. O teu objetivo na entrevista não é parecer especialista; é mostrar que percebes o contexto de suporte.",
    PALE_GREEN,
)]
story += [Spacer(1, 3 * mm), P("Qual é a tua expectativa salarial?", "Qx")]
story += [P(
    "Gostaria primeiro de compreender melhor o projeto, as responsabilidades e o pacote global. Considerando a faixa anunciada e o meu nível de experiência, vejo como razoável uma base entre 1.400 e 1.600 euros brutos mensais, acrescida dos benefícios, mas estou disponível para analisar a proposta da PrimeIT.",
    "Answerx",
)]
story += [P("Quando podes começar?", "Qx")]
story += [P(
    "Resposta a completar antes da entrevista: 'Tenho disponibilidade para iniciar a partir de __________. Caso exista uma necessidade diferente, estou disponível para conversar e tentar ajustar.'",
    "Answerx",
)]
story += [P("Tens disponibilidade para o regime híbrido no Porto?", "Qx")]
story += [P(
    "Sim, tenho disponibilidade para trabalhar em regime híbrido no Porto. Gostaria apenas de compreender quantos dias presenciais estão previstos e se existe alguma necessidade de deslocação adicional ao cliente.",
    "Answerx",
)]
story += [PageBreak()]

# Page 6
story += [P("5. Revisão técnica de suporte", "H1x")]
story += [P("Diferença entre L1 e L2", "H2x")]
story += [
    bullet("L1: receção, categorização, recolha de evidências, resolução de incidentes conhecidos, contas, configurações básicas e encaminhamento."),
    bullet("L2: diagnóstico mais aprofundado, análise de logs, redes, permissões, aplicações e serviços; reprodução do erro; aplicação de correções e articulação com L3 ou fornecedores."),
]
story += [P("Método para diagnosticar um incidente", "H2x")]
steps = [
    ["1", "Clarificar", "Quem é afetado, qual o impacto, quando começou e o que mudou."],
    ["2", "Recolher", "Mensagem de erro, capturas, logs, equipamento, utilizador, rede e passos para reproduzir."],
    ["3", "Isolar", "Distinguir conta, dispositivo, aplicação, rede, servidor ou integração."],
    ["4", "Testar", "Começar por verificações seguras e reversíveis; comparar com um caso funcional."],
    ["5", "Resolver", "Aplicar a correção, validar com o utilizador e confirmar que não houve efeitos secundários."],
    ["6", "Registar", "Documentar causa, ações, resultado e escalonamento, quando necessário."],
]
st = Table([[P("Etapa", "Smallx"), P("Ação", "Smallx"), P("O que fazer", "Smallx")]] + [[P(a, "Bodyx"), P(b, "Bodyx"), P(c, "Bodyx")] for a,b,c in steps], colWidths=[14*mm, 31*mm, 119*mm], repeatRows=1)
st.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), CHARCOAL), ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("ALIGN", (0,1), (0,-1), "CENTER"),
    ("LEFTPADDING", (0,0), (-1,-1), 2.5*mm), ("RIGHTPADDING", (0,0), (-1,-1), 2.5*mm),
    ("TOPPADDING", (0,0), (-1,-1), 2*mm), ("BOTTOMPADDING", (0,0), (-1,-1), 2*mm),
]))
story += [st, Spacer(1, 3 * mm), P("Revisão rápida", "H2x")]
story += [
    bullet("Active Directory: conta bloqueada ou desativada, password, grupos, permissões e princípio do menor privilégio."),
    bullet("Rede: endereço IP, gateway, DHCP, DNS, VPN, teste ao gateway e diferença entre falha local e geral."),
    bullet("Windows: serviços, atualizações, drivers, espaço em disco, Event Viewer e testes com outro utilizador ou dispositivo."),
    bullet("Microsoft 365: autenticação, licenças, Outlook, Teams, OneDrive e sincronização."),
    bullet("Escalonamento: enviar impacto, prioridade, evidências, testes efetuados, resultados e próximo passo recomendado."),
    PageBreak(),
]

# Page 7
story += [P("6. Revisão de SQL", "H1x"), Spacer(1, 4 * mm)]
story += [callout("Posicionamento correto", "Diz que tens experiência prática com consultas em Microsoft SQL Server para pesquisa, validação e apoio a aplicações. Não te apresentes como DBA avançado.", PALE_YELLOW)]
story += [Spacer(1, 3 * mm), P("Conceitos a rever", "H2x")]
story += [
    bullet("SELECT e WHERE para consultar e filtrar dados."),
    bullet("JOIN para relacionar tabelas, por exemplo utilizadores, equipamentos e incidentes."),
    bullet("GROUP BY e funções como COUNT para produzir indicadores."),
    bullet("ORDER BY para ordenar resultados e TOP para limitar a pesquisa."),
    bullet("UPDATE e DELETE apenas com WHERE validado, idealmente dentro de transação e após um SELECT de confirmação."),
]
story += [P("Exemplo 1 - incidentes abertos e respetivos utilizadores", "H2x")]
story += [Preformatted(
    "SELECT i.id, i.subject, i.priority, u.name\n"
    "FROM incidents AS i\n"
    "INNER JOIN users AS u ON u.id = i.user_id\n"
    "WHERE i.status = 'Open'\n"
    "ORDER BY i.priority DESC, i.created_at ASC;",
    styles["Codex"],
)]
story += [P("Exemplo 2 - contagem de incidentes por estado", "H2x")]
story += [Preformatted(
    "SELECT status, COUNT(*) AS total\n"
    "FROM incidents\n"
    "GROUP BY status\n"
    "ORDER BY total DESC;",
    styles["Codex"],
)]
story += [P("Exemplo 3 - atualização segura", "H2x")]
story += [Preformatted(
    "BEGIN TRANSACTION;\n"
    "SELECT id, status FROM incidents WHERE id = 1254;\n"
    "UPDATE incidents SET status = 'Resolved' WHERE id = 1254;\n"
    "-- Validar o resultado antes de confirmar\n"
    "COMMIT; -- ou ROLLBACK;",
    styles["Codex"],
)]
story += [P("Se perguntarem por otimização ou EXPLAIN", "H2x")]
story += [P(
    "Resposta segura: 'Ainda não fiz análise avançada de planos de execução em contexto profissional. Sei que um plano de execução ajuda a perceber como a base de dados acede às tabelas, utiliza índices e executa joins. A minha experiência foi sobretudo em consultas, validação de dados e apoio às aplicações.'",
    "Answerx",
)]
story += [PageBreak()]

# Page 8
story += [P("7. Exemplos comportamentais - método STAR", "H1x")]
story += [P("1. Gestão de volume na NewCoffee", "H2x")]
story += [
    bullet("Situação: centenas de utilizadores distribuídos por cinco localizações."),
    bullet("Tarefa: gerir aproximadamente 20 a 40 pedidos diários sem perder prioridades e informação."),
    bullet("Ação: classificar impacto e urgência, recolher evidências, resolver na primeira linha quando possível e escalar com notas completas."),
    bullet("Resultado: suporte mais organizado, continuidade do acompanhamento e comunicação clara com utilizadores e equipas técnicas."),
]
story += [P("2. Incidente que exigia escalonamento", "H2x")]
story += [
    bullet("Situação: pedido que não podia ser resolvido apenas na primeira linha."),
    bullet("Tarefa: evitar repetição de testes e garantir que o responsável recebia informação útil."),
    bullet("Ação: registar sintomas, utilizador, equipamento, impacto, testes realizados e resultados; encaminhar para equipa interna ou fornecedor e acompanhar."),
    bullet("Resultado: passagem de contexto mais completa e utilizador informado até ao encerramento."),
]
story += [P("3. Plataforma interna de ITSM e ativos", "H2x")]
story += [
    bullet("Situação: necessidade de centralizar informação de utilizadores, equipamentos, pedidos, incidentes e avisos."),
    bullet("Tarefa: contribuir para a aplicação e apoiar a qualidade dos dados."),
    bullet("Ação: trabalhar com tecnologias web e Microsoft SQL Server, consultar e validar dados e corrigir problemas na aplicação."),
    bullet("Resultado: informação de suporte e ativos mais acessível e organizada para a equipa."),
]
story += [P("4. Diagnóstico numa aplicação em produção", "H2x")]
story += [
    bullet("Situação: plataforma de marcações com API externa, API serverless e deployment na Vercel."),
    bullet("Tarefa: validar disponibilidade e marcações e investigar falhas de integração."),
    bullet("Ação: analisar logs e variáveis de ambiente, reproduzir o comportamento e testar a comunicação entre componentes."),
    bullet("Resultado: maior estabilidade da integração e plataforma entregue em produção."),
]
story += [callout("Preparação", "Escolhe um incidente real de hardware, software, acesso ou conectividade e acrescenta detalhes concretos: mensagem de erro, testes, solução e resultado. Não inventes percentagens.", PALE_YELLOW), PageBreak()]

# Page 9
story += [P("8. Inglês e perguntas à recrutadora", "H1x")]
story += [P("Perguntas prováveis em inglês", "H2x")]
english_qas = [
    ("Why are you interested in this role?", "I am interested because the role combines IT support, SQL and application support. It would allow me to use my current experience and develop toward more complex L2 responsibilities."),
    ("How do you handle an incident?", "I first assess the impact and urgency, collect evidence and try to reproduce the issue. I isolate the affected layer, apply a safe solution, validate it with the user and document the result."),
    ("What is your SQL experience?", "I have used Microsoft SQL Server to query and validate data and to support internal applications. I am comfortable with SELECT, filters, joins and basic aggregations."),
    ("Do you have Murex experience?", "I have not used Murex directly yet. I understand that MX.3 supports trading, risk, treasury and post-trade operations. I am motivated to learn it and I have transferable experience in SQL, business applications and incident support."),
]
for q, a in english_qas:
    story += [qa(q, a)]
story += [P("Perguntas inteligentes para fazer", "H2x")]
story += [
    bullet("Esta oportunidade está associada a um cliente ou setor específico?"),
    bullet("Qual é a distribuição aproximada entre suporte ao utilizador, suporte aplicacional e tarefas relacionadas com Murex?"),
    bullet("Que tipo de onboarding ou formação em Murex está previsto para alguém sem experiência direta na plataforma?"),
    bullet("Quais são as ferramentas de ITSM, monitorização e bases de dados utilizadas no projeto?"),
    bullet("Existe trabalho por turnos, prevenção ou suporte fora do horário normal?"),
    bullet("Quais são as próximas etapas do processo e o prazo previsto para decisão?"),
]
story += [callout("Escolha", "Faz duas ou três perguntas, não todas. Prioriza o projeto, as tarefas reais e a formação em Murex.", PALE_GREEN), PageBreak()]

# Page 10
story += [P("9. Checklist final", "H1x")]
story += [P("Na noite anterior", "H2x")]
story += [
    bullet("Testar Microsoft Teams, câmara, microfone, auscultadores e ligação à internet."),
    bullet("Ter o CV, Dossier de Competências, anúncio e este guião abertos, mas sem ler respostas completas."),
    bullet("Definir a data real de disponibilidade e a expectativa salarial mínima aceitável."),
    bullet("Treinar a apresentação de 60 segundos em português e inglês."),
    bullet("Escolher um incidente real para explicar através do método STAR."),
]
story += [P("Dez minutos antes", "H2x")]
story += [
    bullet("Entrar no Teams com antecedência e usar o nome completo."),
    bullet("Silenciar notificações e manter telemóvel disponível apenas como alternativa de ligação."),
    bullet("Ter água, bloco de notas e caneta."),
    bullet("Câmara ao nível dos olhos, iluminação frontal e fundo simples."),
]
story += [P("Durante a entrevista", "H2x")]
story += [
    bullet("Responder primeiro à pergunta e só depois acrescentar contexto."),
    bullet("Usar exemplos concretos; respostas entre 45 e 90 segundos."),
    bullet("Se não souberes: admitir, explicar como investigarias e relacionar com o que já sabes."),
    bullet("Não afirmar experiência em Murex, L2 avançado ou administração de sistemas que ainda não tenhas."),
]
story += [P("Resumo de bolso", "H2x")]
summary_rows = [
    [P("Experiência", "Smallx"), P("Cerca de 2 anos combinados; mais de 1 ano diretamente em suporte.", "Bodyx")],
    [P("Maior prova", "Smallx"), P("Centenas de utilizadores, 5 localizações, 20 a 40 pedidos/dia.", "Bodyx")],
    [P("Stack-chave", "Smallx"), P("Windows, AD, M365, VPN, DHCP, ERP, SQL Server, SQL, ITSM.", "Bodyx")],
    [P("Murex", "Smallx"), P("Sem experiência direta; preparado sobre o contexto e motivado para formação.", "Bodyx")],
    [P("Objetivo", "Smallx"), P("Evoluir para L1/L2 e suporte aplicacional num projeto estruturado.", "Bodyx")],
]
sm = Table(summary_rows, colWidths=[35 * mm, 129 * mm])
sm.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,-1), PALE_GREEN), ("GRID", (0,0), (-1,-1), 0.5, LINE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 3*mm), ("RIGHTPADDING", (0,0), (-1,-1), 3*mm),
    ("TOPPADDING", (0,0), (-1,-1), 2.3*mm), ("BOTTOMPADDING", (0,0), (-1,-1), 2.3*mm),
]))
story += [sm, Spacer(1, 4 * mm), P("Fontes consultadas", "H2x")]
story += [
    P("- Dossier de Competências de Miguel Magalhães, versão fornecida em 7 de outubro de 2026.", "Foot"),
    P('- PrimeIT, "About": <link href="https://www.primeit.pt/en/about" color="#258A16">https://www.primeit.pt/en/about</link>', "Foot"),
    P('- Murex, visão geral do MX.3: <link href="https://www.murex.com/en" color="#258A16">https://www.murex.com/en</link>', "Foot"),
    P('- Murex, arquitetura do MX.3: <link href="https://www.murex.com/en/solutions/technology/mx3-architecture" color="#258A16">https://www.murex.com/en/solutions/technology/mx3-architecture</link>', "Foot"),
]

doc.build(story)
print(OUT)
