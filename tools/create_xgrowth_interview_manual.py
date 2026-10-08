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
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Manual_Entrevista_xGrowth_Tecnico_Junior_TI_Miguel_Magalhaes.pdf"

NAVY = colors.HexColor("#102A43")
BLUE = colors.HexColor("#1F6F8B")
TEAL = colors.HexColor("#2CB1A6")
INK = colors.HexColor("#1F2933")
MUTED = colors.HexColor("#5B6770")
LIGHT = colors.HexColor("#EAF2F5")
PALE = colors.HexColor("#F6F9FA")
GREEN = colors.HexColor("#DDF4EA")
AMBER = colors.HexColor("#FFF2CC")
RED = colors.HexColor("#FBE1E1")
WHITE = colors.white


def register_fonts():
    pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Italic", "/System/Library/Fonts/Supplemental/Arial Italic.ttf"))


def draw_cover(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, width, height, fill=1, stroke=0)
    canvas.setFillColor(BLUE)
    canvas.rect(0, height - 21 * mm, width, 7 * mm, fill=1, stroke=0)
    canvas.setFillColor(TEAL)
    canvas.rect(0, 0, width, 6 * mm, fill=1, stroke=0)
    canvas.setStrokeColor(colors.HexColor("#49677F"))
    canvas.setLineWidth(0.8)
    canvas.line(22 * mm, 34 * mm, width - 22 * mm, 34 * mm)
    canvas.setFont("Arial", 8)
    canvas.setFillColor(colors.HexColor("#C8D8E4"))
    canvas.drawString(22 * mm, 25 * mm, "Preparado a partir do exercício técnico submetido e da descrição atual da função")
    canvas.drawRightString(width - 22 * mm, 25 * mm, "27 de setembro de 2026")
    canvas.restoreState()


def draw_body(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, height - 7 * mm, width, 7 * mm, fill=1, stroke=0)
    canvas.setFillColor(TEAL)
    canvas.rect(0, 0, width, 2.5 * mm, fill=1, stroke=0)
    canvas.setStrokeColor(colors.HexColor("#D5E1E7"))
    canvas.setLineWidth(0.6)
    canvas.line(18 * mm, 14 * mm, width - 18 * mm, 14 * mm)
    canvas.setFont("Arial", 7.2)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 9.2 * mm, "Miguel Magalhães | Entrevista xGrowth Tech")
    canvas.drawRightString(width - 18 * mm, 9.2 * mm, f"Página {canvas.getPageNumber() - 1}")
    canvas.restoreState()


def make_styles():
    s = getSampleStyleSheet()
    return {
        "cover_kicker": ParagraphStyle("cover_kicker", parent=s["Normal"], fontName="Arial-Bold", fontSize=10, leading=13, textColor=TEAL, spaceAfter=7),
        "cover_title": ParagraphStyle("cover_title", parent=s["Title"], fontName="Arial-Bold", fontSize=31, leading=35, textColor=WHITE, spaceAfter=8),
        "cover_sub": ParagraphStyle("cover_sub", parent=s["Normal"], fontName="Arial", fontSize=14, leading=19, textColor=colors.HexColor("#D9E7EF"), spaceAfter=18),
        "cover_meta": ParagraphStyle("cover_meta", parent=s["Normal"], fontName="Arial", fontSize=10, leading=15, textColor=WHITE, spaceAfter=5),
        "h1": ParagraphStyle("h1", parent=s["Heading1"], fontName="Arial-Bold", fontSize=20, leading=24, textColor=NAVY, spaceAfter=9),
        "kicker": ParagraphStyle("kicker", parent=s["Normal"], fontName="Arial-Bold", fontSize=8, leading=10, textColor=TEAL, spaceAfter=3),
        "h2": ParagraphStyle("h2", parent=s["Heading2"], fontName="Arial-Bold", fontSize=12.5, leading=15.5, textColor=BLUE, spaceBefore=7, spaceAfter=5),
        "h3": ParagraphStyle("h3", parent=s["Heading3"], fontName="Arial-Bold", fontSize=10.3, leading=13, textColor=NAVY, spaceBefore=5, spaceAfter=3),
        "body": ParagraphStyle("body", parent=s["BodyText"], fontName="Arial", fontSize=9.25, leading=13.3, textColor=INK, spaceAfter=6),
        "small": ParagraphStyle("small", parent=s["BodyText"], fontName="Arial", fontSize=7.8, leading=10.5, textColor=MUTED, spaceAfter=3),
        "qa_q": ParagraphStyle("qa_q", parent=s["BodyText"], fontName="Arial-Bold", fontSize=9.4, leading=12.5, textColor=NAVY, spaceAfter=2),
        "qa_a": ParagraphStyle("qa_a", parent=s["BodyText"], fontName="Arial", fontSize=8.9, leading=12.7, textColor=INK),
        "quote": ParagraphStyle("quote", parent=s["BodyText"], fontName="Arial-Italic", fontSize=9, leading=13, textColor=INK, leftIndent=6, rightIndent=4),
        "table_head": ParagraphStyle("table_head", parent=s["BodyText"], fontName="Arial-Bold", fontSize=8.1, leading=10, textColor=WHITE),
        "table": ParagraphStyle("table", parent=s["BodyText"], fontName="Arial", fontSize=7.75, leading=10.2, textColor=INK),
        "code": ParagraphStyle("code", parent=s["Code"], fontName="Courier", fontSize=7.7, leading=10.4, textColor=colors.HexColor("#172B4D")),
        "cheat": ParagraphStyle("cheat", parent=s["BodyText"], fontName="Arial", fontSize=8.1, leading=11.2, textColor=INK),
    }


STYLES = None


def P(text, style="body"):
    return Paragraph(text, STYLES[style])


def title(kicker, heading, intro=None):
    items = [P(kicker.upper(), "kicker"), P(heading, "h1")]
    if intro:
        items.append(P(intro, "body"))
    return items


def bullets(items, level=0, compact=False):
    return ListFlowable(
        [ListItem(P(x, "small" if compact else "body"), leftIndent=8) for x in items],
        bulletType="bullet",
        start="circle",
        leftIndent=15 + level * 7,
        bulletFontName="Arial",
        bulletFontSize=6,
        bulletColor=TEAL,
        spaceAfter=4,
    )


def callout(title_text, body_text, color=LIGHT):
    t = Table([[P(title_text, "qa_q")], [P(body_text, "qa_a")]], colWidths=[169 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#C3D5DE")),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return KeepTogether([t, Spacer(1, 4)])


def qa(question, answer, color=PALE):
    t = Table([[P(question, "qa_q")], [P(answer, "qa_a")]], colWidths=[169 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("LINEBEFORE", (0, 0), (0, -1), 3, TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return KeepTogether([t, Spacer(1, 4)])


def code_block(text):
    pre = Preformatted(text.strip("\n"), STYLES["code"])
    t = Table([[pre]], colWidths=[169 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EEF3F7")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#C8D6DF")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return KeepTogether([t, Spacer(1, 5)])


def info_table(headers, rows, widths):
    data = [[P(h, "table_head") for h in headers]]
    data.extend([[P(str(cell), "table") for cell in row] for row in rows])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.45, colors.HexColor("#CAD8E0")),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(data)):
        style.append(("BACKGROUND", (0, i), (-1, i), WHITE if i % 2 else PALE))
    t.setStyle(TableStyle(style))
    return t


def new_page(kicker_text, heading, intro=None):
    return [PageBreak(), *title(kicker_text, heading, intro)]


def build_story():
    story = []

    # Cover
    story.extend([
        Spacer(1, 38 * mm),
        P("XGROWTH TECH · PREPARAÇÃO FINAL", "cover_kicker"),
        P("Manual de Entrevista", "cover_title"),
        P("Técnico Júnior de TI", "cover_sub"),
        Spacer(1, 12 * mm),
        P("Miguel Magalhães", "cover_meta"),
        P("Terça-feira, 29 de setembro de 2026 · 10:00", "cover_meta"),
        P("Google Meet · 25 minutos", "cover_meta"),
        Spacer(1, 16 * mm),
        callout(
            "Objetivo do manual",
            "Defender com segurança o exercício técnico, resolver um incidente simples em voz alta, avaliar as condições propostas e demonstrar potencial para evoluir de primeira linha para DBRE/SRE.",
            colors.HexColor("#DCE9F0"),
        ),
        NextPageTemplate("body"),
        PageBreak(),
    ])

    # 1
    story.extend(title("1. Estratégia", "O que esta entrevista realmente avalia", "O exercício já foi aprovado. Agora Fernando Castro quer confirmar autoria, raciocínio, segurança operacional, comunicação e compatibilidade com uma equipa pequena e exigente."))
    story.append(info_table(
        ["Bloco", "Tempo provável", "O que deves demonstrar"],
        [
            ["Função e condições", "5-7 min", "Escutar, tomar notas e esclarecer contrato, salário, remoto e progressão."],
            ["Defesa do exercício", "6-8 min", "Explicar decisões e pressupostos sem recitar o PDF."],
            ["Incidente simples", "6-8 min", "Pensar em voz alta, começar pelo impacto e evitar ações arriscadas."],
            ["Perguntas finais", "3-5 min", "Mostrar interesse por aprendizagem, DBRE/SRE e forma de trabalho."],
        ],
        [36 * mm, 29 * mm, 104 * mm],
    ))
    story.append(Spacer(1, 6))
    story.append(P("O que Fernando provavelmente procura", "h2"))
    story.append(bullets([
        "Uma pessoa que <b>pergunta cedo</b> quando existe dúvida, em vez de improvisar em produção.",
        "Capacidade de organizar pedidos por impacto, urgência e risco.",
        "Escrita clara em português e inglês para clientes internacionais.",
        "Noções sólidas de SQL e Linux, acompanhadas de prudência operacional.",
        "Uso real de IA, mas com validação, confidencialidade e responsabilidade humana.",
        "Humildade técnica: saber o que consegue fazer sozinho e quando deve escalar.",
    ]))
    story.append(callout("Regra de ouro", "Nunca tentes impressionar executando uma ação rápida. Impressiona mostrando que sabes proteger produção, recolher evidência, comunicar e validar.", GREEN))
    story.append(P("Probabilidade dos temas", "h2"))
    story.append(info_table(
        ["Probabilidade", "Tema"],
        [
            ["Muito alta", "Incidente NewCoffee; disco Linux a 98%; EXPLAIN vs. EXPLAIN ANALYZE; uso de IA."],
            ["Alta", "Prioridade do incidente de faturação; pedido de acesso a produção; verificações antes de executar."],
            ["Média", "Explicação linha a linha da query; email da janela de manutenção; plano de carreira a dois anos."],
        ],
        [34 * mm, 135 * mm],
    ))

    # 2
    story.extend(new_page("2. Empresa e função", "O que deves saber sobre a xGrowth", "A xGrowth apresenta-se como uma boutique portuguesa de engenharia sénior que moderniza, opera e escala plataformas críticas."))
    story.append(bullets([
        "Áreas principais: <b>SRE, DBRE, DevOps, CloudOps, FinOps, observabilidade e operações geridas de IT</b>.",
        "Atuação cloud-agnostic: AWS, Azure, GCP e ambientes on-premises.",
        "Clientes em Portugal, União Europeia, Reino Unido e Brasil, com operação remota.",
        "Equipa pequena e sénior; o anúncio identifica esta contratação como o <b>primeiro técnico júnior</b>.",
        "Trabalho direto com o fundador, revisão próxima, formação paga e caminho para DBA/SRE.",
        "A escrita e organização são centrais: triagem, respostas a clientes, queries, procedimentos, runbooks e automação com IA.",
    ]))
    story.append(P("Resposta: Conheces a empresa?", "h2"))
    story.append(qa(
        "Pergunta provável",
        "Sim. Estive a pesquisar a xGrowth e percebi que é uma boutique de engenharia sénior focada em operar e modernizar plataformas críticas, sobretudo nas áreas de bases de dados, SRE, DevOps e cloud. Trabalha de forma cloud-agnostic e presta operações geridas com SLA, monitorização, runbooks e handover documentado. O que mais me atrai é poder começar na triagem e suporte, trabalhando perto de profissionais séniores, e evoluir gradualmente para bases de dados e fiabilidade sem perder a responsabilidade pelo serviço ao cliente."
    ))
    story.append(P("Porque esta função?", "h2"))
    story.append(qa(
        "Resposta recomendada",
        "Esta função combina três aspetos que procuro: contacto com utilizadores e clientes, trabalho operacional estruturado e progressão técnica para SQL, Linux e fiabilidade. Na NewCoffee gostei especialmente de ser o primeiro ponto de contacto, organizar prioridades e acompanhar problemas até à resolução. Quero aproveitar essa base para ganhar experiência real com produção, procedimentos, monitorização e bases de dados, com responsabilidade crescente."
    ))
    story.append(callout("Leitura estratégica", "Numa equipa pequena, autonomia não significa trabalhar sem apoio. Significa recolher informação, tentar o que é seguro, documentar e pedir ajuda cedo com uma pergunta bem preparada.", AMBER))

    # 3
    story.extend(new_page("3. Abertura", "Apresentação de 60 a 90 segundos", "A tua introdução deve ligar formação, experiência, exercício e objetivo profissional. Não recites todo o currículo."))
    story.append(P("Versão principal", "h2"))
    story.append(callout(
        "Resposta em português",
        "Sou licenciado em Engenharia Informática, tenho um CTeSP em Redes e Sistemas Informáticos e frequento o Mestrado em Cibersegurança e Auditoria de Sistemas Informáticos em regime pós-laboral. Na Direção de Sistemas de Informação da NewCoffee fui primeiro ponto de contacto para utilizadores de diferentes departamentos e localizações, tratando incidentes de sistemas, redes, acessos, equipamentos e aplicações empresariais. Também trabalhei com PHC e SQL e desenvolvi uma plataforma interna de ITSM para tickets, ativos e indicadores. O que procuro agora é aprofundar Linux, SQL e sistemas de produção, mantendo a componente de suporte e responsabilidade operacional. Foi por isso que o caminho de evolução para DBRE e SRE desta função me interessou particularmente.",
        GREEN,
    ))
    story.append(P("Possível passagem para inglês", "h2"))
    story.append(callout(
        "English version",
        "I am a Computer Engineering graduate with additional technical education in Computer Networks and Systems, and I am currently pursuing a Master's degree in Cybersecurity and Information Systems Auditing. At NewCoffee, I was a first point of contact for users across different departments and locations, handling incidents involving systems, networks, access, equipment and business applications. I also worked with PHC and SQL and developed an internal ITSM platform for tickets, assets and operational indicators. I am now looking to deepen my knowledge of Linux, databases and production reliability while continuing to take ownership of customer issues.",
        colors.HexColor("#E8F0F8"),
    ))
    story.append(P("Se te interromper", "h2"))
    story.append(P("Não tentes terminar o discurso preparado. Responde diretamente à pergunta. Uma conversa técnica é melhor do que um monólogo perfeito.", "body"))
    story.append(P("Mensagens que devem ficar", "h2"))
    story.append(bullets([
        "Já estiveste confortável com dias de 20 a 40 pedidos.",
        "Gostas de resolver problemas e de acompanhar utilizadores.",
        "Queres aprender produção real, SQL, Linux, DBRE e SRE.",
        "És prudente: não improvisas alterações em produção.",
        "Sabes usar IA como apoio, sem delegar nela a responsabilidade.",
    ]))

    # 4
    story.extend(new_page("4. Parte 1", "Triagem: defender as cinco classificações", "A chave não é decorar as etiquetas. É explicar impacto, urgência, risco e próximo passo."))
    story.append(info_table(
        ["Pedido", "Classificação", "Primeiro passo e racional"],
        [
            ["Confirmar backup", "Verificação operacional", "Consultar job, alertas e logs; confirmar execução, artefacto esperado e ausência de erros."],
            ["Faturação indisponível", "Incidente crítico/alto", "Confirmar âmbito e impacto; iniciar triagem e comunicação segundo o runbook."],
            ["Reenviar fatura", "Pedido administrativo", "Validar o pedido e encaminhar para o fluxo ou responsável adequado."],
            ["Novo campo na tabela", "Change request", "Clarificar requisito, dependências, risco, aprovação, teste, janela e rollback."],
            ["Acesso à BD de produção", "Acesso privilegiado", "Validar identidade, aprovação e necessidade; aplicar menor privilégio e auditoria."],
        ],
        [45 * mm, 38 * mm, 86 * mm],
    ))
    story.append(Spacer(1, 6))
    story.append(qa("Porque trataste primeiro o ponto 2?", "Porque existe indisponibilidade atual, todos os utilizadores estão impedidos de faturar e há impacto direto no negócio. O tempo aumenta o prejuízo, por isso inicio de imediato triagem, comunicação e eventual escalada. Os restantes pedidos devem ser registados, mas não têm o mesmo impacto imediato."))
    story.append(qa("E se o backup também tiver falhado?", "A prioridade depende do contexto. Um backup falhado pode representar risco elevado, sobretudo se for o último ponto de recuperação ou se houver um incidente em curso. Contudo, com a informação fornecida, a faturação já está indisponível e causa impacto confirmado; o backup é ainda um pedido de verificação. Registaria ambos e reavaliaria assim que tivesse novos factos."))
    story.append(qa("O pedido 5 pode ser um incidente de segurança?", "Sim. Se a identidade, origem ou comportamento forem suspeitos, deixaria de ser apenas um pedido de acesso e seguiria o procedimento de segurança. Não enviaria credenciais nem detalhes sensíveis e confirmaria a identidade por um canal autorizado."))
    story.append(callout("Frase forte", "Prioridade não é a ordem de chegada. É a combinação de impacto, urgência, risco e compromissos de serviço.", GREEN))

    # 5
    story.extend(new_page("5. Parte 1", "Perguntas de aprofundamento sobre triagem"))
    story.append(qa("Qual é a diferença entre incidente, pedido e alteração?", "Um incidente é uma interrupção ou degradação não planeada de um serviço. Um pedido é uma solicitação normal e prevista, como informação ou acesso. Uma alteração modifica um sistema ou configuração e deve ser avaliada, testada, aprovada e preparada para reversão."))
    story.append(qa("O que significa não tratar sozinho?", "Significa reconhecer que posso recolher requisitos, evidência e preparar o trabalho, mas não executar uma ação que exige aprovação, privilégios superiores ou revisão técnica. Escalar não é abandonar o ticket: mantenho ownership, contexto e comunicação."))
    story.append(qa("Como atribuirias severidade ao incidente de faturação?", "Confirmaria primeiro número de utilizadores, existência de workaround, impacto financeiro, cliente afetado e duração. Se toda a organização estiver impedida de faturar sem alternativa, justificaria prioridade alta ou crítica, conforme a matriz interna."))
    story.append(qa("O que verificarias num backup além de 'completed'?", "Hora de início e fim, volume esperado, ficheiros ou bases incluídos, mensagens de warning, destino, retenção, consistência e capacidade de restauração. Um job verde não prova sozinho que o backup é recuperável."))
    story.append(qa("Que detalhes pedirias para o novo campo?", "Nome e objetivo do campo, tabela correta, tipo de dados, tamanho, obrigatoriedade, valor por omissão, dados históricos, validações, impacto em aplicações, APIs, relatórios, integrações, índices e requisitos de auditoria."))
    story.append(qa("Que acesso concederias ao novo responsável de IT?", "Apenas depois de autorização formal. Preferiria conta individual, MFA, acesso temporário quando possível, permissões mínimas e inicialmente read-only se suficiente. Evitaria contas partilhadas e garantiria logging e revisão posterior."))
    story.append(P("O que não dizer", "h2"))
    story.append(bullets([
        "'É urgente porque o cliente disse que é urgente.'",
        "'Dou acesso e depois confirmo.'",
        "'Faço primeiro e documento no fim.'",
        "'Se não souber, passo logo para outra pessoa.'",
    ]))

    # 6
    story.extend(new_page("6. Parte 2", "Email da janela de manutenção", "O objetivo era gerir expectativas sem prometer uma alteração insegura nem responder apenas 'não'."))
    story.append(P("Porque a resposta funciona", "h2"))
    story.append(bullets([
        "Reconhece o pedido e comunica claramente que quinta-feira não é viável.",
        "Explica o motivo operacional: é necessária uma maintenance window.",
        "Propõe uma próxima ação concreta: terça-feira.",
        "Abre espaço para clarificar impacto e procurar uma alternativa aprovada.",
        "Não promete uma solução antes da análise e mantém tom profissional.",
    ]))
    story.append(qa("Why did you not simply say no?", "Because the goal is not only to reject an unsafe deadline. The customer needs a clear next step. I proposed the next available window and asked for the business impact in case there was an approved alternative that could meet the underlying need without rushing the production change."))
    story.append(qa("What would you do if Thursday were business-critical?", "I would clarify the required outcome, identify whether a temporary workaround could satisfy it, assess risk with the technical owner and follow the emergency-change process if one existed. I would not bypass approval or testing merely because the deadline was important."))
    story.append(qa("How would you communicate during a delay?", "I would state what is known, what is being investigated, who owns the next action and when the next update will be provided. I would avoid speculative causes or unrealistic resolution times."))
    story.append(P("Expressões úteis em inglês", "h2"))
    story.append(info_table(
        ["Objetivo", "Expressão"],
        [
            ["Confirmar impacto", "Could you confirm the affected users and the business impact?"],
            ["Gerir expectativa", "I cannot confirm the deadline until the risk and dependencies have been assessed."],
            ["Dar próximo passo", "The next update will be provided by 11:30, even if the investigation is still ongoing."],
            ["Escalar", "I am escalating this with the evidence collected so far and will retain ownership of the communication."],
        ],
        [42 * mm, 127 * mm],
    ))

    # 7
    story.extend(new_page("7. Parte 3.1", "Query SQL: explicação linha a linha"))
    story.append(code_block("""
SELECT
    c.country,
    COUNT(DISTINCT o.customer_id) AS customers_with_paid_orders,
    SUM(o.total_eur) AS total_paid_eur
FROM orders AS o
JOIN customers AS c ON c.id = o.customer_id
WHERE o.status = 'paid'
  AND o.created_at >= CURRENT_TIMESTAMP - INTERVAL '90 days'
GROUP BY c.country
ORDER BY total_paid_eur DESC;
"""))
    story.append(info_table(
        ["Elemento", "Explicação verbal"],
        [
            ["JOIN", "Associa cada order ao customer para obter o país."],
            ["WHERE", "Restringe a encomendas pagas criadas nos últimos 90 dias."],
            ["COUNT DISTINCT", "Conta clientes únicos, evitando duplicar quem tem várias encomendas."],
            ["SUM", "Soma o valor de todas as encomendas pagas do período."],
            ["GROUP BY", "Produz uma linha agregada por país."],
            ["ORDER BY", "Apresenta primeiro os países com maior valor total pago."],
        ],
        [42 * mm, 127 * mm],
    ))
    story.append(qa("Porque assumiste PostgreSQL?", "O enunciado não indicava o motor. Declarei explicitamente a suposição porque a sintaxe do intervalo temporal varia. A lógica é portátil; em SQL Server, por exemplo, adaptaria a expressão para DATEADD."))
    story.append(qa("Existe alguma ambiguidade nos 90 dias?", "Sim. A query usa uma janela contínua de 90 dias a partir do instante atual. Se o requisito pretendesse 90 dias civis completos, fuso horário específico ou exclusão do dia atual, confirmaria antes de implementar."))
    story.append(qa("E se total_eur puder ser NULL?", "SUM ignora valores NULL. Eu confirmaria se NULL é válido no modelo. Se o requisito fosse tratá-lo como zero, poderia usar COALESCE, mas preferia compreender primeiro por que existem valores nulos."))

    # 8
    story.extend(new_page("8. Parte 3.2", "Query com 20 milhões de linhas: diagnóstico"))
    story.append(P("Sequência recomendada", "h2"))
    story.append(info_table(
        ["Passo", "O que verificar", "Porquê"],
        [
            ["1", "Plano estimado com EXPLAIN", "Identificar scans, joins, estimativas e custos sem executar novamente a query."],
            ["2", "Volume e seletividade", "Perceber quantas linhas são paid e quantas pertencem aos 90 dias."],
            ["3", "Índices e estatísticas", "Confirmar PK, índices nas colunas de filtro/join e estatísticas atualizadas."],
            ["4", "I/O, memória e spill", "Ver se agregação ou ordenação está a escrever para disco."],
            ["5", "Teste controlado", "Validar mudanças num ambiente seguro ou janela adequada."],
            ["6", "Medição antes/depois", "Provar melhoria e evitar regressões."],
        ],
        [14 * mm, 63 * mm, 92 * mm],
    ))
    story.append(qa("Porque não criarias imediatamente um índice?", "Porque um índice tem custo de armazenamento e escrita e pode nem ser utilizado. Primeiro preciso de perceber o plano, seletividade e padrão de acesso. Um sequential scan pode ser correto se os 90 dias representarem uma grande parte da tabela."))
    story.append(qa("Que índice considerarias?", "Em PostgreSQL, poderia avaliar um índice parcial para rows com status = 'paid', começando por created_at e incluindo customer_id e, se fizer sentido, total_eur. Outra opção seria um índice composto em status, created_at e customer_id. A ordem final depende da distribuição, das queries reais e do plano."))
    story.append(code_block("""
-- Exemplo a avaliar, não executar cegamente:
CREATE INDEX CONCURRENTLY idx_orders_paid_recent
ON orders (created_at, customer_id)
INCLUDE (total_eur)
WHERE status = 'paid';
"""))
    story.append(qa("E se a consulta for executada muitas vezes?", "Além de índices, avaliaria particionamento temporal, pré-agregação ou uma materialized view, dependendo da necessidade de frescura. A solução deve refletir frequência, SLA, volume e custo de manutenção."))
    story.append(callout("Armadilha", "EXPLAIN ANALYZE executa a query. Em produção, avalia impacto, locks, carga e duração antes de o utilizar.", RED))

    # 9
    story.extend(new_page("9. Parte 3.3", "Servidor Linux com disco a 98%"))
    story.append(P("Explicação principal", "h2"))
    story.append(code_block("""
df -hT
sudo du -xhd1 <mountpoint> | sort -h
sudo lsof +L1
"""))
    story.append(info_table(
        ["Comando", "O que responde"],
        [
            ["df -hT", "Qual filesystem está cheio, dimensão, espaço disponível e tipo."],
            ["du -xhd1", "Que diretórios visíveis consomem espaço no filesystem afetado."],
            ["lsof +L1", "Que ficheiros apagados continuam abertos e a ocupar blocos."],
            ["df -i", "Se existe esgotamento de inodes, mesmo com blocos ainda disponíveis."],
        ],
        [38 * mm, 131 * mm],
    ))
    story.append(qa("Porque pode df mostrar 98% e du muito menos?", "Uma causa típica são ficheiros eliminados que continuam abertos por processos. Já não aparecem na árvore de diretórios, mas os blocos só são libertados quando o processo fecha o descritor. Também podem existir diferenças por permissões, reserved blocks ou mount points."))
    story.append(qa("O que farias depois de encontrar um log enorme?", "Identificaria o serviço, política de retenção e motivo do crescimento. Avaliaria rotação, compressão, arquivo ou expansão. Não apagaria nem truncaria o ficheiro sem procedimento, porque poderia perder evidência, causar falha ou esconder a causa."))
    story.append(qa("E um ficheiro deleted, mas aberto?", "Identificaria o processo com lsof, confirmaria o serviço e pediria aprovação para uma ação segura, normalmente restart controlado ou rotação adequada. Não terminaria o processo apenas para libertar espaço."))
    story.append(P("O que nunca fazer", "h2"))
    story.append(bullets([
        "Executar <font name='Courier'>rm -rf</font> sobre diretórios desconhecidos.",
        "Apagar backups, logs ou dados apenas por serem grandes.",
        "Reiniciar serviços críticos sem validar impacto e rollback.",
        "Analisar o diretório errado porque se assumiu que o problema era em <font name='Courier'>/</font>.",
    ]))

    # 10
    story.extend(new_page("10. Parte 3.4", "Antes de executar num servidor de cliente"))
    story.append(P("Usa a sequência S-A-R-V-C", "h2"))
    story.append(info_table(
        ["Letra", "Verificação", "Perguntas"],
        [
            ["S", "Sistema certo", "Cliente, hostname, ambiente, utilizador e região estão corretos?"],
            ["A", "Autorização", "Existe ticket, aprovação, runbook e janela?"],
            ["R", "Risco e rollback", "Qual o impacto? Como parar e reverter? Existe backup/snapshot válido?"],
            ["V", "Validação", "Que teste provará que a intervenção resultou?"],
            ["C", "Comunicação", "Quem precisa de saber antes, durante e depois?"],
        ],
        [13 * mm, 40 * mm, 116 * mm],
    ))
    story.append(qa("E se o runbook não corresponder ao ambiente real?", "Paro. Registo a diferença, recolho evidência e peço validação. Um procedimento aprovado para outra versão, servidor ou topologia não é automaticamente seguro."))
    story.append(qa("O comando está correto, mas estás no servidor errado. O que aconteceu?", "É um incidente operacional. O contexto faz parte da correção do comando. Por isso confirmo hostname, ambiente e identidade antes de qualquer alteração."))
    story.append(qa("Como validas depois?", "Executo os testes definidos previamente: estado do serviço, health checks, logs sem novos erros, métrica relevante, teste funcional e confirmação do cliente quando aplicável. Só depois atualizo e encerro o ticket."))
    story.append(callout("Resposta curta perfeita", "Confirmo onde estou, se estou autorizado, qual o impacto, como volto atrás e como vou provar que o sistema ficou saudável.", GREEN))
    story.append(P("Mudança normal vs. emergência", "h2"))
    story.append(P("Uma mudança de emergência pode reduzir etapas ou tempos, mas não elimina autorização, registo, avaliação de risco, comunicação e plano de recuperação. Urgência não transforma improviso em procedimento.", "body"))

    # 11
    story.extend(new_page("11. Parte 4", "Uso de IA: transparência e responsabilidade"))
    story.append(qa("Que partes foram feitas com IA?", "Usei IA como segunda revisão para desafiar a priorização, melhorar a clareza do email em inglês e rever a lógica da query e da sequência Linux. As decisões, pressupostos e exemplos profissionais são meus. Validei cada comando e mantive a responsabilidade pela resposta final."))
    story.append(qa("Copiarias um comando sugerido por IA para produção?", "Não. Confirmaria documentação oficial, versão, parâmetros, permissões, efeitos laterais, impacto e rollback. Testaria num ambiente seguro sempre que possível e seguiria o processo interno de aprovação."))
    story.append(qa("Colocarias logs de clientes numa IA pública?", "Não sem política e autorização explícitas. Logs podem conter nomes, emails, IPs, identificadores, queries, credenciais ou dados de negócio. Removeria ou mascararia informação sensível e utilizaria apenas ferramentas aprovadas."))
    story.append(qa("Dá um exemplo de automação com IA", "Usaria IA para ajudar a transformar notas técnicas validadas num primeiro rascunho de runbook ou para classificar pedidos com base em campos já autorizados. A classificação teria regras, revisão humana e métricas de erro; nenhuma ação destrutiva seria executada automaticamente."))
    story.append(P("Princípios a memorizar", "h2"))
    story.append(bullets([
        "IA acelera análise e escrita; não substitui autorização.",
        "Nunca expor segredos, dados pessoais ou informação de clientes.",
        "Validar comandos, versões, fontes e pressupostos.",
        "Manter humano responsável por produção e comunicação.",
        "Medir qualidade e guardar audit trail quando a IA participa no processo.",
    ]))
    story.append(callout("Frase forte", "A IA pode sugerir. A responsabilidade por compreender, validar e executar continua a ser minha.", GREEN))

    # 12
    story.extend(new_page("12. Parte 5.1", "O incidente NewCoffee em formato STAR"))
    story.append(info_table(
        ["Parte", "Conteúdo"],
        [
            ["Situação", "Incidente SQL/PHC afetou a operação e deixou informação de um dia por recuperar."],
            ["Tarefa", "Apoiar a identificação e recuperação dos documentos que não tinham sido restaurados."],
            ["Ação", "Usar numeração sequencial, identificar lacunas, contactar utilizadores, aceder aos tablets por QuickSupport, reenviar/sincronizar e validar documento a documento."],
            ["Resultado", "A equipa recuperou praticamente toda a informação em falta, apesar de lentidão e timeouts."],
            ["Aprendizagem", "Não assumir que restore concluído significa recuperação completa; validar dados e comunicar com utilizadores."],
        ],
        [28 * mm, 141 * mm],
    ))
    story.append(P("Resposta oral recomendada", "h2"))
    story.append(callout(
        "60 a 75 segundos",
        "Durante o estágio na DSI da NewCoffee ocorreu um incidente relacionado com SQL e PHC que deixou documentos de um dia por recuperar. A recuperação pelos backups não devolveu imediatamente toda a informação. A minha contribuição foi identificar documentos em falta através da numeração sequencial, contactar os utilizadores e aceder remotamente aos tablets com QuickSupport para reenviar e sincronizar os documentos ainda disponíveis localmente. O processo teve de ser repetido com vários utilizadores e houve lentidão e timeouts, por isso fui validando progressivamente o que já estava recuperado. No final, a equipa conseguiu recuperar praticamente toda a informação. A principal aprendizagem foi que não basta uma operação técnica terminar: é necessário validar a integridade do resultado com os dados e os utilizadores.",
        colors.HexColor("#E8F0F8"),
    ))
    story.append(qa("Qual foi exatamente a tua contribuição?", "Identifiquei lacunas, coordenei o contacto com os utilizadores, acedi aos dispositivos e apoiei o reenvio e validação. Não afirmo que recuperei sozinho a base de dados; foi um trabalho de equipa."))
    story.append(qa("O que farias diferente hoje?", "Definiria uma checklist de reconciliação, registaria documentos esperados e recuperados, criaria atualizações regulares de estado e analisaria com a equipa por que razão o processo de backup/restore não garantiu recuperação integral."))

    # 13
    story.extend(new_page("13. Partes 5.2 e 5.3", "Trabalho reativo e plano a dois anos"))
    story.append(qa("Como te sentes com trabalho reativo e repetitivo?", "Estou confortável porque já fui primeiro ponto de contacto e tive dias com 20 a 40 pedidos. Não escolho a ordem pelo interesse pessoal: priorizo impacto, urgência e risco. Gosto de receber um problema, perceber o que acontece e levá-lo a uma solução ou escalada correta. Quando algo se repete, procuro documentação, melhoria de processo ou automação segura."))
    story.append(qa("Não te vais cansar do suporte?", "Não vejo o suporte como algo a abandonar rapidamente. É onde se aprende o comportamento real dos sistemas e dos clientes. Quero crescer a partir dessa base, assumindo gradualmente incidentes, mudanças e problemas mais complexos."))
    story.append(qa("Onde queres estar daqui a dois anos?", "Quero ser tecnicamente mais autónomo em SQL, Linux, monitorização e sistemas de produção, capaz de executar e validar procedimentos com maior responsabilidade. Gostaria de estar a evoluir para DBRE/SRE, compreendendo risco, rollback, recuperação e fiabilidade, sem perder a disciplina operacional aprendida na primeira linha."))
    story.append(qa("Porque cibersegurança se a função é operações?", "Vejo a cibersegurança como complemento. Acesso mínimo, proteção de dados, logging, alterações controladas, backup e resposta a incidentes fazem parte de uma operação fiável. Não estou a usar esta função apenas como passagem para outra área."))
    story.append(P("Ponto de equilíbrio", "h2"))
    story.append(callout("O que deves transmitir", "Ambição técnica sem desprezar o trabalho inicial. Queres crescer, mas aceitas dominar triagem, escrita, procedimentos e suporte antes de receber acesso e autonomia superiores.", AMBER))

    # 14
    story.extend(new_page("14. Comportamental", "Perguntas prováveis e respostas-modelo"))
    story.append(qa("O que fazes quando não sabes?", "Defino primeiro o que sei e o que falta saber, consulto documentação e evidência disponível, faço verificações seguras e estabeleço um limite de tempo. Se continuar bloqueado ou existir risco, pergunto cedo, apresentando contexto, testes efetuados e uma pergunta concreta."))
    story.append(qa("Conta um erro teu", "Escolhe um exemplo real e de baixo impacto. Explica como o detetaste, comunicaste, corrigiste e evitaste repetição. Não uses um erro inventado nem escolhas uma falha grave de segurança que não consigas defender."))
    story.append(qa("Como lidas com feedback direto?", "Separo o feedback da minha identidade, procuro compreender o exemplo concreto e confirmo o comportamento esperado. Aplico a correção e, se for um tema repetível, atualizo a minha checklist ou documentação."))
    story.append(qa("Como organizas 20 a 40 pedidos?", "Registo todos, separo incidente de pedido, avalio impacto, urgência, SLA e dependências, agrupo tarefas repetidas e mantenho comunicação. Se a carga ultrapassar a capacidade, sinalizo cedo em vez de deixar tickets silenciosamente atrasados."))
    story.append(qa("Como trabalhas com pouca supervisão?", "Avanço autonomamente nas ações reversíveis e dentro do procedimento. Mantenho notas, identifico riscos e peço validação antes de ultrapassar permissões ou fazer mudanças relevantes. Autonomia inclui saber quando parar."))
    story.append(qa("Qual é o teu maior ponto forte?", "A combinação de comunicação com troubleshooting estruturado. Consigo ouvir o utilizador, organizar informação, testar hipóteses por etapas e documentar o resultado de forma que outra pessoa consiga continuar o trabalho."))
    story.append(qa("Que área precisas de desenvolver?", "Quero aprofundar experiência real em administração Linux e tuning de bases de dados em produção. Tenho fundamentos e prática em laboratório/projetos, mas procuro agora aprender com procedimentos, revisão sénior e incidentes reais, sem apresentar-me como especialista."))

    # 15
    story.extend(new_page("15. Incidente ao vivo", "Método universal: I-M-P-A-C-T-O", "Fala em voz alta. O avaliador precisa de ouvir como decides, não apenas a resposta final."))
    story.append(info_table(
        ["Letra", "Ação", "Exemplo"],
        [
            ["I", "Impacto", "Quem está afetado? Existe paragem total?"],
            ["M", "Momento", "Quando começou? Houve alteração recente?"],
            ["P", "Prioridade", "Qual é a urgência, risco, SLA e workaround?"],
            ["A", "Análise", "Monitorização, logs, estado e dependências."],
            ["C", "Controlo", "Runbook, ações reversíveis, autorização e limites."],
            ["T", "Transparência", "Atualizar cliente e equipa com factos e próximo update."],
            ["O", "Outcome", "Validar recuperação, documentar causa e próximos passos."],
        ],
        [13 * mm, 44 * mm, 112 * mm],
    ))
    story.append(P("Abertura perfeita", "h2"))
    story.append(callout("Primeira resposta", "Antes de sugerir uma alteração, começaria por confirmar o impacto, o âmbito e a hora de início. Depois verificaria monitorização, logs, dependências e alterações recentes, seguindo o runbook e comunicando um próximo ponto de situação.", GREEN))
    story.append(P("Perguntas que podes fazer ao entrevistador", "h2"))
    story.append(bullets([
        "O problema afeta um utilizador, um cliente ou todos?",
        "Existe mensagem de erro ou alerta de monitorização?",
        "Quando funcionou pela última vez?",
        "Houve deploy, mudança, crescimento de dados ou manutenção?",
        "Existe workaround? Qual é o impacto no negócio?",
        "Tenho acesso aos logs e ao runbook?",
        "Que ações estou autorizado a executar?",
    ]))
    story.append(callout("Não é uma prova de adivinhação", "Se faltarem dados, pede-os. Formular as perguntas certas é parte da solução.", AMBER))

    # 16
    story.extend(new_page("16. Simulação 1", "A aplicação de faturação está indisponível"))
    story.append(P("Resposta-modelo", "h2"))
    story.append(callout(
        "Raciocínio verbal",
        "Confirmaria se todos os utilizadores estão afetados, desde quando e se existe alternativa manual. Registaria o incidente com prioridade proporcional ao impacto. Verificaria a monitorização e o estado da aplicação, servidor, base de dados, storage, rede e serviços dependentes. Consultaria logs e alterações recentes. Seguiria o runbook e começaria por verificações de baixo risco. Não reiniciaria imediatamente serviços nem faria alterações na base de dados sem evidência e autorização. Comunicaria um próximo update, escalaria com os dados recolhidos se ultrapassasse a minha autonomia e, no fim, validaria uma operação real de faturação antes de encerrar.",
        colors.HexColor("#E8F0F8"),
    ))
    story.append(P("Perguntas de seguimento", "h2"))
    story.append(qa("A aplicação responde, mas dá erro de base de dados. O que verificas?", "Conectividade até à BD, DNS, porta, estado do serviço, pool de ligações, credenciais expiradas, limites de conexões, storage, locks e logs. Evito executar queries corretivas antes de compreender a causa."))
    story.append(qa("Um restart resolveria?", "Pode restaurar temporariamente, mas não é a primeira resposta automática. Preciso de saber impacto, autorização, dependências e se existe risco de perda de estado. Se o runbook recomendar restart, recolho evidência antes e valido depois."))
    story.append(qa("O cliente exige ETA?", "Daria um tempo para o próximo update, não um tempo de resolução inventado. Explicaria o estado conhecido, ações em curso e dependência da investigação."))
    story.append(qa("O serviço voltou sozinho. Fechas?", "Não imediatamente. Confirmo estabilidade, verifico logs e métricas, valido com o cliente, documento o período de impacto e abro análise de causa se necessário."))

    # 17
    story.extend(new_page("17. Simulações 2 a 4", "Backup, acesso e alteração"))
    story.append(P("Cenário A - Backup terminou com warning", "h2"))
    story.append(qa("O que fazes?", "Confirmo qual objeto ou etapa gerou warning, se o conjunto esperado está completo, destino, volume, retenção e último backup saudável. Avalio risco de recuperação e sigo o procedimento de retry/escalada. Nunca respondo apenas 'correu bem' por o job ter terminado."))
    story.append(P("Cenário B - Diretor pede acesso urgente à produção", "h2"))
    story.append(qa("O que fazes?", "Mesmo sendo diretor, valido identidade, aprovação e necessidade. Proponho acesso individual, mínimo, temporário e auditado. Se a urgência tiver causa operacional, procuro também uma alternativa em que a equipa execute a consulta ou forneça o resultado sem conceder acesso amplo."))
    story.append(P("Cenário C - Alteração de coluna antes de quinta-feira", "h2"))
    story.append(qa("Que riscos existem?", "Locks, duração, reescrita da tabela, impacto em aplicação e ORM, nulls, defaults, APIs, relatórios, replicação, backups e rollback. O risco depende do motor, versão, tamanho da tabela e forma da alteração."))
    story.append(qa("Existe alternativa?", "Talvez um campo numa tabela auxiliar, configuração, view, exportação ou operação manual temporária. Primeiro confirmo o resultado de negócio pretendido; não assumo que alterar o schema é a única solução."))
    story.append(P("Cenário D - Disco cresce novamente após limpeza", "h2"))
    story.append(qa("Próximo passo", "Trato a causa, não apenas o sintoma: identifico produtor, taxa de crescimento, retenção, rotação, alertas e capacidade. Crio ação preventiva e documento o threshold e a resposta."))

    # 18
    story.extend(new_page("18. Rápidas técnicas", "Perguntas curtas que podem aparecer"))
    story.append(info_table(
        ["Pergunta", "Resposta curta"],
        [
            ["O que é SLA?", "Compromisso de serviço: tempos, disponibilidade ou resposta acordados com o cliente."],
            ["O que é SLO?", "Objetivo interno mensurável de fiabilidade usado para gerir o serviço."],
            ["Runbook?", "Procedimento operacional repetível, com pré-condições, passos, validação e rollback."],
            ["Rollback?", "Plano para regressar a um estado seguro se a mudança falhar."],
            ["RTO?", "Tempo máximo desejado para restaurar o serviço."],
            ["RPO?", "Quantidade máxima aceitável de dados perdidos, medida em tempo."],
            ["DBRE?", "Aplicação de práticas de reliability engineering a bases de dados."],
            ["SRE?", "Engenharia focada em fiabilidade, automação, SLOs e redução de trabalho manual repetitivo."],
            ["Idempotência?", "Executar a mesma operação várias vezes produz o mesmo estado final esperado."],
            ["Menor privilégio?", "Conceder apenas o acesso necessário, durante o tempo necessário."],
            ["Índice?", "Estrutura que acelera certas leituras, com custo de espaço e escrita."],
            ["Lock?", "Mecanismo que coordena acesso concorrente e pode causar espera ou bloqueio."],
        ],
        [53 * mm, 116 * mm],
    ))
    story.append(P("Linux: comandos úteis", "h2"))
    story.append(code_block("""
uptime                 # carga e tempo ligado
free -h                # memória
df -hT / df -i         # espaço e inodes
ps aux --sort=-%cpu    # processos por CPU
systemctl status NAME  # estado do serviço
journalctl -u NAME     # logs do serviço
ss -lntp               # portas TCP em escuta
"""))
    story.append(callout("Cuidado", "Saber um comando não autoriza executá-lo. Contexto, permissões e procedimento continuam a mandar.", AMBER))

    # 19
    story.extend(new_page("19. Condições", "Salário, contrato e disponibilidade", "O anúncio atual publica condições objetivas. Escuta primeiro a proposta do Fernando e só depois negocia."))
    story.append(info_table(
        ["Componente publicada", "Valor/condição"],
        [
            ["Base", "1.300 € a 1.500 € brutos por mês, 14 meses, conforme experiência."],
            ["Variável", "Prémio trimestral por objetivos, até 15%."],
            ["Revisão", "Revisão salarial após 12 meses, ligada a evolução técnica e objetivos."],
            ["Modelo", "Remoto; possível passagem futura a híbrido no Porto."],
            ["Desenvolvimento", "Formação paga, tempo alocado e progressão para DBA/SRE."],
        ],
        [52 * mm, 117 * mm],
    ))
    story.append(P("Posicionamento recomendado", "h2"))
    story.append(info_table(
        ["Nível", "Base mensal x14", "Leitura"],
        [
            ["Pedido", "1.500 €", "Justificável pela licenciatura, CTeSP, experiência relevante e exercício aprovado."],
            ["Bom", "1.400-1.450 €", "Equilíbrio forte entre entrada júnior e valor já demonstrado."],
            ["Chão", "1.300 €", "Mínimo do intervalo; avaliar contrato, variável, formação e revisão."],
        ],
        [31 * mm, 39 * mm, 99 * mm],
    ))
    story.append(qa("Qual é a tua expectativa salarial?", "Tendo em conta o intervalo anunciado, a minha formação e a experiência relevante em suporte, PHC/SQL, documentação e contacto com utilizadores, gostaria de ficar próximo do topo, nos 1.500 euros brutos mensais, em catorze meses. Naturalmente, quero compreender o pacote completo, o variável e os objetivos associados."))
    story.append(qa("Se propuserem 1.300 €?", "Agradeço a transparência. Considerando o alinhamento do meu perfil e a qualidade reconhecida do exercício, existe margem para aproximarmos a base de 1.400 ou 1.450 euros? Se a base estiver fechada, gostaria de perceber se é possível uma revisão formal aos seis meses mediante objetivos definidos."))
    story.append(P("Confirma obrigatoriamente", "h2"))
    story.append(bullets([
        "Tipo e duração do contrato, entidade empregadora e período experimental.",
        "Subsídio de alimentação, seguro, despesas de teletrabalho e equipamento.",
        "Como se calcula o prémio de 15%, métricas, período e histórico de pagamento.",
        "Horário, prevenção, incidentes fora de horas e respetiva compensação.",
        "Condições da eventual transição de remoto para híbrido.",
    ], compact=True))

    # 20
    story.extend(new_page("20. Situação atual", "Como falar sobre disponibilidade e outros compromissos", "Na data da entrevista poderás já ter iniciado a oportunidade anteriormente aceite. Não mintas nem prometas uma data sem confirmar as tuas obrigações."))
    story.append(qa("Quando poderias começar?", "Entretanto iniciei recentemente um compromisso profissional que já estava acordado. A oportunidade da xGrowth continua a interessar-me muito pelo alinhamento com bases de dados e fiabilidade. Se concluirmos que existe interesse mútuo, confirmarei as minhas obrigações contratuais e darei uma data realista, garantindo uma transição profissional."))
    story.append(qa("Porque continuaste neste processo?", "Porque este processo já estava em curso e a função está particularmente alinhada com o caminho técnico que pretendo construir em SQL, Linux, DBRE e SRE. Quis concluir a conversa com transparência e avaliar as condições concretas antes de tomar qualquer decisão."))
    story.append(qa("Tens outra proposta?", "Sim, tenho outro compromisso profissional em curso. Não quero utilizá-lo como pressão; quero avaliar a xGrowth pelo conteúdo da função, aprendizagem, responsabilidades e condições. Se avançarmos, lidarei com qualquer decisão de forma correta e profissional."))
    story.append(callout("Importante", "Não abandones nem alteres o compromisso atual durante a entrevista. Primeiro recebe uma proposta escrita completa, compara e só depois decide.", RED))
    story.append(P("Critérios de decisão", "h2"))
    story.append(info_table(
        ["Critério", "O que procurar"],
        [
            ["Aprendizagem", "Revisão real por séniores, tempo de formação, acesso progressivo."],
            ["Segurança", "Runbooks, aprovações, backups, ambientes e limites de autonomia."],
            ["Carga", "Volume de pedidos, clientes, prevenção, horários e cobertura."],
            ["Progressão", "Marcos concretos para SQL/Linux/DBRE/SRE, não apenas promessa genérica."],
            ["Pacote", "Base, variável, refeição, contrato, revisão, remoto e despesas."],
        ],
        [42 * mm, 127 * mm],
    ))

    # 21
    story.extend(new_page("21. Perguntas finais", "O que perguntar ao Fernando"))
    story.append(P("Escolhe quatro", "h2"))
    story.append(bullets([
        "Como será dividido o dia entre triagem, respostas a clientes, SQL/Linux, documentação e automação?",
        "Que acompanhamento e revisão terá o primeiro técnico júnior durante os primeiros três meses?",
        "Que ações poderei executar autonomamente no início e quais exigirão sempre aprovação?",
        "Que stack de bases de dados, monitorização e ticketing é usada com maior frequência?",
        "Como funciona na prática a progressão para DBA/DBRE/SRE e que marcos técnicos esperam no primeiro ano?",
        "Existe prevenção ou resposta a incidentes fora do horário? Como é organizada e compensada?",
        "Como são definidos e medidos os objetivos do prémio trimestral de até 15%?",
        "Qual é o principal problema que gostariam que esta pessoa resolvesse nos primeiros 90 dias?",
    ]))
    story.append(P("A melhor pergunta", "h2"))
    story.append(callout("Pergunta estratégica", "Referiste a evolução para bases de dados e fiabilidade. Que resultados concretos fariam dizer, ao fim de seis ou doze meses, que eu estou preparado para assumir tarefas de DBRE/SRE com mais autonomia?", GREEN))
    story.append(P("Fecho recomendado", "h2"))
    story.append(callout(
        "Últimos 30 segundos",
        "Obrigado por explicares a função e as condições. A conversa reforçou o meu interesse porque a posição combina o trabalho de suporte que já conheço com a evolução técnica que procuro em SQL, Linux e fiabilidade. Gostei especialmente da responsabilidade gradual e do contacto próximo com a equipa sénior. Acredito que consigo contribuir desde o início na triagem, comunicação e documentação, enquanto desenvolvo autonomia nas componentes mais técnicas.",
        colors.HexColor("#E8F0F8"),
    ))

    # 22
    story.extend(new_page("22. Preparação", "Plano para as 24 horas anteriores"))
    story.append(info_table(
        ["Quando", "Ação"],
        [
            ["Dia anterior", "Reler o exercício; explicar cada resposta sem olhar; rever query, EXPLAIN, df/du/lsof e STAR."],
            ["30 min", "Abrir PDF, anúncio e notas; testar Meet, câmara, áudio e ligação; fechar notificações."],
            ["10 min", "Água, papel, caneta; respirar; recordar IMPACTO e S-A-R-V-C."],
            ["Durante", "Tomar notas das condições; pensar em voz alta; perguntar quando faltam dados."],
            ["Depois", "Enviar agradecimento curto e registar condições, dúvidas e prazo de decisão."],
        ],
        [33 * mm, 136 * mm],
    ))
    story.append(P("Material aberto", "h2"))
    story.append(bullets([
        "Exercício técnico enviado.",
        "Anúncio da vaga e intervalo salarial.",
        "Este manual na folha de revisão rápida.",
        "CV submetido.",
        "Quatro perguntas finais escolhidas.",
    ]))
    story.append(P("Estado mental", "h2"))
    story.append(callout("Recorda", "Eles já gostaram da tua resolução. Não precisas de provar que és sénior. Precisas de mostrar que a resolução é tua, que raciocinas com segurança e que és alguém em quem vale a pena investir.", GREEN))
    story.append(P("Erros a evitar", "h2"))
    story.append(bullets([
        "Responder depressa antes de confirmar o âmbito.",
        "Inventar comandos, experiência ou resultados.",
        "Dizer apenas 'escalava' sem recolher evidência.",
        "Tratar restart, delete ou índice como solução automática.",
        "Aceitar condições verbalmente sem pedir proposta escrita.",
        "Falar demasiado e consumir o tempo destinado ao incidente.",
    ]))

    # 23
    story.extend(new_page("23. Revisão rápida", "Folha de bolso para os últimos 10 minutos"))
    story.append(callout("Mensagem central", "Sou forte em suporte, comunicação, organização e ownership. Tenho fundamentos de SQL e Linux. Quero aprender produção real com prudência e evoluir para DBRE/SRE.", colors.HexColor("#DCE9F0")))
    story.append(info_table(
        ["Tema", "Recordar"],
        [
            ["Prioridade", "Impacto + urgência + risco + SLA; faturação indisponível primeiro."],
            ["Produção", "Servidor certo, autorização, risco, rollback, validação, comunicação."],
            ["SQL", "JOIN, paid, 90 dias, COUNT DISTINCT, SUM, GROUP BY."],
            ["Performance", "EXPLAIN primeiro; seletividade, índices, stats, I/O; medir."],
            ["Linux", "df -hT; du -xhd1; lsof +L1; df -i; não apagar cegamente."],
            ["IA", "Revisão e aceleração; sem dados sensíveis; validar tudo."],
            ["NewCoffee", "Lacunas sequenciais, QuickSupport, reenvio, validação, equipa."],
            ["Incidente", "IMPACTO: impacto, momento, prioridade, análise, controlo, transparência, outcome."],
            ["Salário", "Pedir 1.500; bom 1.400-1.450; confirmar variável, contrato e benefícios."],
        ],
        [36 * mm, 133 * mm],
    ))
    story.append(P("Três frases de segurança", "h2"))
    story.append(bullets([
        "Com a informação disponível, a minha primeira hipótese seria esta, mas confirmaria antes de agir.",
        "Essa ação pode ter impacto em produção; antes de a executar validaria autorização e rollback.",
        "Se ultrapassasse a minha autonomia, escalaria com logs, testes, impacto e estado atual bem documentados.",
    ]))
    story.append(P("Três perguntas finais", "h2"))
    story.append(bullets([
        "Quais são os objetivos dos primeiros 90 dias?",
        "Como funciona a revisão e progressão para DBRE/SRE?",
        "Como são organizados acompanhamento, horário e incidentes fora de horas?",
    ]))
    story.append(callout("Última nota", "Pausa dois segundos antes de responder. Estrutura vale mais do que velocidade.", AMBER))

    # 24
    story.extend(new_page("24. Fontes", "Documentos e páginas consultadas"))
    story.append(P("Fonte principal", "h2"))
    story.append(P("Exercício Técnico - Técnico Júnior de TI, respostas submetidas por Miguel Magalhães, seis páginas. O manual preserva os pressupostos e exemplos apresentados no documento.", "body"))
    story.append(P("Informação pública da empresa e da função", "h2"))
    story.append(bullets([
        "xGrowth Tech - Sobre: <link href='https://xgrowth.tech/sobre/' color='#1F6F8B'>https://xgrowth.tech/sobre/</link>",
        "Anúncio Técnico Júnior de TI: <link href='https://pt.linkedin.com/jobs/view/4468220876' color='#1F6F8B'>LinkedIn, referência 4468220876</link>",
        "Página institucional: <link href='https://www.linkedin.com/company/xgrowthtech' color='#1F6F8B'>https://www.linkedin.com/company/xgrowthtech</link>",
    ]))
    story.append(P("Notas metodológicas", "h2"))
    story.append(bullets([
        "As respostas-modelo são guias de raciocínio, não textos para decorar palavra por palavra.",
        "Os exemplos de índices e comandos são hipóteses de análise; não constituem autorização para execução em produção.",
        "Condições salariais e de trabalho refletem o anúncio consultado em 27 de setembro de 2026 e devem ser confirmadas na proposta escrita.",
        "Qualquer decisão sobre disponibilidade deve respeitar as obrigações contratuais efetivamente aplicáveis.",
    ]))
    story.append(Spacer(1, 20 * mm))
    story.append(callout("Boa entrevista, Miguel", "O teu exercício já demonstrou método, prudência e capacidade de escrita. A entrevista serve para tornar visível o raciocínio que já está no documento.", GREEN))

    return story


def build_pdf():
    global STYLES
    register_fonts()
    STYLES = make_styles()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=16 * mm,
        bottomMargin=19 * mm,
        title="Manual de Entrevista xGrowth Tech - Técnico Júnior de TI",
        author="Miguel Magalhães",
        subject="Preparação para entrevista de 29 de setembro de 2026",
    )
    cover_frame = Frame(22 * mm, 36 * mm, A4[0] - 44 * mm, A4[1] - 64 * mm, id="cover", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    body_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover),
        PageTemplate(id="body", frames=[body_frame], onPage=draw_body),
    ])
    doc.build(build_story())
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
