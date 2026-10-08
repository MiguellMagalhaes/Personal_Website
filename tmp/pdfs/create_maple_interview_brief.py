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
    Spacer,
    Table,
    TableStyle,
)


OUTPUT = Path("output/pdf/Preparacao_Entrevista_Maple_Networks_Cyber_Security_Analyst_Miguel_Magalhaes.pdf")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = A4
NAVY = colors.HexColor("#17233D")
BLUE = colors.HexColor("#0087C9")
TEXT = colors.HexColor("#273650")
MUTED = colors.HexColor("#687892")
PALE = colors.HexColor("#EAF4FA")
PALE2 = colors.HexColor("#F5F8FA")
LINE = colors.HexColor("#D5E0E8")
GREEN = colors.HexColor("#167A5A")
AMBER = colors.HexColor("#A66400")

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", "/System/Library/Fonts/Supplemental/Arial Italic.ttf"))


class InterviewBrief(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=18 * mm,
            rightMargin=18 * mm,
            topMargin=20 * mm,
            bottomMargin=16 * mm,
            title="Preparação para entrevista - Maple Networks - Cyber Security Analyst Nights",
            author="Miguel Magalhães",
            subject="Guia prático de preparação para entrevista",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(PageTemplate(id="brief", frames=frame, onPage=self._decorate))

    def _decorate(self, canvas, doc):
        canvas.saveState()
        canvas.setFillColor(NAVY)
        canvas.rect(0, PAGE_H - 8 * mm, PAGE_W, 8 * mm, fill=1, stroke=0)
        canvas.setFillColor(BLUE)
        canvas.rect(0, PAGE_H - 10.5 * mm, 47 * mm, 2.5 * mm, fill=1, stroke=0)
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(18 * mm, 11 * mm, PAGE_W - 18 * mm, 11 * mm)
        canvas.setFont("Arial", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(18 * mm, 6.5 * mm, "Miguel Magalhães | Maple Networks | Interview brief")
        canvas.drawRightString(PAGE_W - 18 * mm, 6.5 * mm, f"Página {doc.page}")
        canvas.restoreState()


styles = getSampleStyleSheet()
title = ParagraphStyle(
    "Title",
    parent=styles["Title"],
    fontName="Arial-Bold",
    fontSize=22,
    leading=25,
    textColor=NAVY,
    alignment=TA_LEFT,
    spaceAfter=5,
)
subtitle = ParagraphStyle(
    "Subtitle",
    fontName="Arial",
    fontSize=11,
    leading=14,
    textColor=MUTED,
    spaceAfter=9,
)
h1 = ParagraphStyle(
    "H1",
    fontName="Arial-Bold",
    fontSize=14,
    leading=17,
    textColor=NAVY,
    spaceBefore=7,
    spaceAfter=5,
)
h2 = ParagraphStyle(
    "H2",
    fontName="Arial-Bold",
    fontSize=10.8,
    leading=13,
    textColor=BLUE,
    spaceBefore=5,
    spaceAfter=3,
)
body = ParagraphStyle(
    "Body",
    fontName="Arial",
    fontSize=9.1,
    leading=12.1,
    textColor=TEXT,
    spaceAfter=4,
)
small = ParagraphStyle(
    "Small",
    fontName="Arial",
    fontSize=8.1,
    leading=10.4,
    textColor=TEXT,
)
tiny = ParagraphStyle(
    "Tiny",
    fontName="Arial",
    fontSize=7.1,
    leading=9,
    textColor=MUTED,
)
bullet = ParagraphStyle(
    "Bullet",
    parent=body,
    leftIndent=11,
    firstLineIndent=-7,
    bulletIndent=0,
    spaceAfter=2.5,
)
quote = ParagraphStyle(
    "Quote",
    fontName="Arial-Italic",
    fontSize=8.8,
    leading=11.6,
    textColor=TEXT,
    leftIndent=8,
    rightIndent=8,
    spaceAfter=5,
)
table_head = ParagraphStyle(
    "TableHead",
    fontName="Arial-Bold",
    fontSize=8.2,
    leading=10,
    textColor=colors.white,
    alignment=TA_LEFT,
)
table_text = ParagraphStyle(
    "TableText",
    fontName="Arial",
    fontSize=7.9,
    leading=10,
    textColor=TEXT,
)
table_text_bold = ParagraphStyle(
    "TableTextBold",
    fontName="Arial-Bold",
    fontSize=7.9,
    leading=10,
    textColor=TEXT,
)


def P(text, style=body):
    return Paragraph(text, style)


def B(text):
    return Paragraph(f"• {text}", bullet)


def section(title_text, items):
    return KeepTogether([P(title_text, h2), *items])


def info_table(rows, widths):
    data = [[P(a, table_text_bold), P(b, table_text)] for a, b in rows]
    table = Table(data, colWidths=widths, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), PALE),
                ("BACKGROUND", (1, 0), (1, -1), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


story = []

# PAGE 1
story += [
    P("Preparação rápida para a entrevista", title),
    P("Cyber Security Analyst Nights | Maple Networks | 5 de outubro de 2026", subtitle),
    P("Objetivo: chegares à chamada com uma apresentação clara, conhecimento real da empresa e respostas honestas para os pontos fortes e lacunas do teu perfil.", body),
    P("Plano para os próximos 30 minutos", h1),
]

timeline = Table(
    [
        [P("0-7 min", table_head), P("Empresa e função", table_head), P("Lê a página 1 e fixa três ideias sobre a Maple.", table_head)],
        [P("7-17 min", table_text_bold), P("Apresentação", table_text_bold), P("Repete em voz alta o pitch e as respostas principais da página 2.", table_text)],
        [P("17-25 min", table_text_bold), P("Perguntas", table_text_bold), P("Treina as perguntas da página 3 sem decorar palavra por palavra.", table_text)],
        [P("25-30 min", table_text_bold), P("Técnica e setup", table_text_bold), P("Revê a página 4, testa Teams, água, câmara e entra cinco minutos antes.", table_text)],
    ],
    colWidths=[24 * mm, 40 * mm, 108 * mm],
)
timeline.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("BOX", (0, 0), (-1, -1), 0.5, LINE),
            ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE2]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]
    )
)
story += [timeline, Spacer(1, 3 * mm), P("O que é a Maple Networks", h1)]
story += [
    B("Empresa britânica privada de serviços tecnológicos, com escritórios em Londres e Orlando e clientes internacionais."),
    B("Trabalha em três pilares: <b>Security, Data e Cloud</b>, através de consultoria, projetos e serviços geridos."),
    B("Serve organizações dos setores público e privado, incluindo saúde, ensino superior, finanças, indústria e grandes empresas."),
    B("Na cibersegurança oferece SOC/MDR 24/7, resposta a incidentes, testes de intrusão, gestão de vulnerabilidades, IAM, firewalls geridas e orientação de governance e compliance."),
    B("A abordagem comercial enfatiza parceria, comunicação clara, resultados práticos e atuação como extensão da equipa do cliente."),
    B("Acreditações relevantes: <b>CREST SOC</b>, <b>CREST Incident Response</b>, CREST Pen Testing, ISO 27001, Cyber Essentials Plus e capacidades reconhecidas pelo NCSC."),
    P("Frase para usar: <i>What attracted me to Maple is the combination of 24/7 security operations, recognised standards and a strong focus on customer outcomes.</i>", quote),
    P("O que vais fazer nesta função", h1),
]
story += [
    B("Monitorizar plataformas de segurança e investigar alertas durante noites e fins de semana."),
    B("Gerir incidentes, realizar threat hunting e apoiar clientes durante ataques ou situações de vulnerabilidade."),
    B("Acompanhar remediações, recolher atualizações e garantir o cumprimento de SLAs."),
    B("Contribuir para a melhoria dos serviços e trabalhar segundo políticas, CREST e normas ISO."),
    B("Aprender num ambiente MSSP/SOC rápido, com clientes dos setores público e privado."),
]

story.append(PageBreak())

# PAGE 2
story += [
    P("A tua mensagem principal", title),
    P("Não és um analista SOC experiente. És um candidato júnior com base real em operações IT, redes, suporte, incidentes e projetos de deteção, preparado para aprender rapidamente.", subtitle),
    P("Apresentação de 60 segundos em inglês", h1),
    P(
        "I'm a Computer Engineering graduate with a technical background in computer networks and systems, and I'm currently pursuing a Master's degree in Cybersecurity and Information Systems Auditing. At NewCoffee, I worked as a first point of contact for users across different departments, handling incidents involving Windows systems, accounts, Active Directory, VPN, connectivity, business applications and hardware. I also developed an internal ITSM platform for tickets and assets. My most relevant cybersecurity project was an international network intrusion detection laboratory using Wireshark, Snort, Python and machine learning. I'm now looking for my first professional SOC opportunity, where I can apply my operational experience, learn from experienced analysts and develop in incident response and threat detection.",
        quote,
    ),
    P("Porque esta função e esta empresa", h1),
    P(
        "I'm interested in this role because it offers a structured entry into security operations while building on my IT support and networking experience. Maple's focus on 24/7 monitoring, incident response, threat hunting and customer success matches the areas I want to develop. I also value that the company is CREST accredited and works with recognised standards such as ISO 27001, because I want to learn in an environment with mature processes and clear accountability.",
        quote,
    ),
    P("Porque aceitas noites e fins de semana", h1),
    P(
        "I understand that security monitoring must operate continuously and that the night shift requires reliability, focus and good handovers. I am comfortable with the schedule and I see it as an opportunity to take responsibility, develop my judgement and contribute when customers need continuous coverage. I would also like to understand the exact shift pattern and how the team manages handovers and support during nights.",
        quote,
    ),
    P("Como o teu perfil encaixa", h1),
]

fit_rows = [
    [P("O que eles procuram", table_head), P("A tua evidência", table_head)],
    [P("Formação em cyber/IT", table_text_bold), P("Licenciatura em Engenharia Informática, CTeSP em Redes e Sistemas e mestrado atual em Cibersegurança.", table_text)],
    [P("Windows e Linux", table_text_bold), P("Suporte prático a Windows; utilização de Linux em laboratórios, redes, servidores e projetos académicos.", table_text)],
    [P("Ticketing e SLAs", table_text_bold), P("Gestão e acompanhamento de pedidos na NewCoffee e Staples; plataforma ITSM própria para tickets, ativos e indicadores.", table_text)],
    [P("Incidentes e clientes", table_text_bold), P("Triagem, diagnóstico, documentação, escalada e validação com utilizadores de vários departamentos e locais.", table_text)],
    [P("Threat detection", table_text_bold), P("Laboratório de IDS: tráfego baseline, Wireshark, ataques controlados, Snort, Python e machine learning.", table_text)],
    [P("Inglês e equipa", table_text_bold), P("Nível profissional B2 e experiência num projeto académico internacional COIL.", table_text)],
]
fit = Table(fit_rows, colWidths=[47 * mm, 125 * mm], repeatRows=1)
fit.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE2]),
            ("BOX", (0, 0), (-1, -1), 0.5, LINE),
            ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]
    )
)
story += [fit, Spacer(1, 3 * mm), P("Lacunas a apresentar com honestidade", h1)]
story += [
    B("<b>Sentinel/SIEM/SOAR:</b> ainda sem experiência profissional. Diz que conheces o objetivo e o fluxo de triagem e queres ganhar prática supervisionada."),
    B("<b>Cloud:</b> fundamentos, mas pouca experiência operacional. Não inventes projetos Azure/AWS/GCP."),
    B("<b>Vulnerability tooling:</b> compreendes prioridade, impacto e remediação, mas ainda não operaste uma plataforma empresarial."),
    P("Resposta segura: <i>I haven't used Microsoft Sentinel in production yet. My closest hands-on experience is analysing network traffic and validating Snort alerts. I understand the purpose of SIEM triage, and I'm ready to learn your platform and procedures quickly.</i>", quote),
]

story.append(PageBreak())

# PAGE 3
story += [
    P("Perguntas prováveis e respostas", title),
    P("Mantém cada resposta entre 30 e 75 segundos. Estrutura: contexto, o que fizeste, resultado e aprendizagem.", subtitle),
    P("1  Tell me about yourself", h2),
    P("Usa o pitch da página anterior. Não contes o CV inteiro. Liga suporte IT, redes, mestrado e projeto de IDS ao objetivo de entrar num SOC.", body),
    P("2  Why do you want to work in cybersecurity", h2),
    P("I enjoy structured investigation: understanding what happened, separating symptoms from causes, assessing impact and documenting the response. My support experience gave me the operational discipline, and my cybersecurity studies and intrusion detection project confirmed that I want to develop professionally in security operations.", quote),
    P("3  Tell me about an incident you handled", h2),
    P("Usa o incidente NewCoffee: falha relacionada com SQL/PHC, documentos em falta, identificação por numeração sequencial, contacto com utilizadores, acesso remoto aos tablets, reenvio e validação progressiva. Fecha com a aprendizagem: uma operação técnica só termina quando a integridade do resultado é confirmada.", body),
    P("4  How do you prioritise multiple alerts or tickets", h2),
    P("I prioritise by business impact, urgency, number of affected users, security risk and whether a workaround exists. I acknowledge critical incidents quickly, preserve relevant information, communicate the current status and escalate when the required authority or expertise is outside my scope.", quote),
    P("5  What would you do when receiving a suspicious alert", h2),
    P("I would validate the alert, identify the affected user or asset, check the timeline and available evidence, assess scope and severity, and follow the playbook. I would avoid making disruptive changes without authority, preserve evidence, escalate when necessary, communicate clearly and document every action.", quote),
    P("6  What experience do you have with Windows and Linux", h2),
    P("My strongest professional experience is with Windows endpoints, Active Directory, user accounts, permissions, VPN, connectivity and business applications. I have used Linux in networking, server and cybersecurity laboratories, including command-line investigation and service configuration. I am comfortable with the fundamentals and want to deepen my production experience.", quote),
    P("7  How do you communicate with a customer during an incident", h2),
    P("I keep the message factual and calm: what we know, the current impact, what is being investigated, any safe action the customer can take, and when they can expect the next update. I avoid speculation and do not promise a resolution time I cannot guarantee.", quote),
    P("8  What are your strengths", h2),
    P("My main strengths are structured troubleshooting, clear documentation, patience with users and ownership of follow-up. I am also comfortable admitting when I need to escalate, while making sure the next person receives useful context and evidence.", quote),
    P("9  What is an area you need to develop", h2),
    P("I need more hands-on experience with enterprise SIEM/SOAR platforms and public cloud security. I have the underlying networking, systems and alert-analysis foundations, and I am actively looking for an environment where I can apply them under mature processes and mentorship.", quote),
    P("10  Are you currently available and comfortable with the schedule", h2),
    P("Yes. I have completed my freelance projects and I am currently available. I understand that the role covers nights and weekends, and I am comfortable with that responsibility. I would like to understand the exact rotation, rest periods and handover process.", quote),
]

story.append(PageBreak())

# PAGE 4
story += [
    P("Revisão técnica e perguntas finais", title),
    P("O objetivo não é parecer sénior. É mostrar raciocínio seguro, vontade de aprender e disciplina operacional.", subtitle),
    P("Conceitos rápidos", h1),
]

tech_rows = [
    ("SOC", "Equipa que monitoriza, deteta, investiga e responde a eventos e incidentes de segurança."),
    ("SIEM", "Centraliza e correlaciona logs para gerar alertas, permitir investigação e produzir evidência."),
    ("SOAR", "Automatiza e orquestra tarefas e playbooks de resposta entre várias ferramentas."),
    ("Microsoft Sentinel", "SIEM/SOAR cloud-native da Microsoft, integrado no ecossistema Azure."),
    ("Threat hunting", "Pesquisa proativa de sinais de atividade maliciosa que pode não ter produzido um alerta claro."),
    ("Vulnerabilidade", "Fraqueza explorável. Risco depende também da ameaça, exposição, impacto e controlos existentes."),
    ("False positive", "Alerta que parece malicioso mas resulta de atividade legítima; deve ser validado e documentado."),
    ("EDR / NDR", "EDR observa endpoints; NDR analisa comportamento e tráfego de rede. Ambos alimentam a visibilidade do SOC."),
    ("SLA", "Compromisso de tempos de resposta, atualização ou resolução. Exige acompanhamento e comunicação."),
]
story.append(info_table(tech_rows, [35 * mm, 137 * mm]))
story += [
    Spacer(1, 3 * mm),
    P("Fluxo de resposta que deves repetir", h1),
    P("Validar alerta → identificar ativo/utilizador → recolher contexto e evidência → avaliar impacto e severidade → seguir playbook → conter ou escalar com autorização → comunicar → documentar → confirmar remediação e fechar.", body),
    P("Perguntas inteligentes para fazer", h1),
]
story += [
    B("What does the night-shift pattern look like, and how are handovers managed between shifts?"),
    B("What security platforms are used day to day - Microsoft Sentinel, EDR, NDR and vulnerability management tools?"),
    B("What training and mentoring are provided during the first three months?"),
    B("What would success look like for a junior analyst after 30, 60 and 90 days?"),
    B("How does the SOC communicate and escalate incidents to customers and senior analysts?"),
    B("As the role is remote from Portugal, what is the employment arrangement and which time zone governs the shifts?"),
    P("Últimos cinco minutos", h1),
]
story += [
    B("Abre o CV, a descrição da vaga e este guia. Fecha notificações e aplicações desnecessárias."),
    B("Testa Teams, microfone, câmara e ligação. Entra cinco minutos antes."),
    B("Tem água e papel. Mantém o telemóvel em silêncio."),
    B("Fala devagar em inglês. Se não perceberes: <i>Could you please repeat or rephrase the question?</i>"),
    B("Se não souberes: <i>I haven't worked with that directly yet, but this is how I would approach it...</i>"),
    B("Fecha com interesse: <i>Based on what we've discussed, the role sounds closely aligned with the direction I want to take.</i>"),
    P("Fontes consultadas", h1),
    P(
        "Descrição da vaga fornecida pela Maple Networks; páginas oficiais About Us, Managed Services, Managed Detection and Response, Solutions, Contact e ISO Policy. Consultadas em 5 de outubro de 2026. https://www.maple-networks.com/en-us/about-us/ | https://www.maple-networks.com/en-us/managed-services/ | https://www.maple-networks.com/en-us/managed-services/security/mdr/ | https://www.maple-networks.com/en-us/our-solutions/ | https://www.maple-networks.com/contact/ | https://www.maple-networks.com/iso-policy/",
        tiny,
    ),
]

doc = InterviewBrief(str(OUTPUT))
doc.build(story)
print(OUTPUT.resolve())
