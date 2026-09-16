from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from build_one_logic_cover_letter import register_fonts


OUTPUT = Path(
    "output/pdf/Guia_Entrevista_Konica_Minolta_IT_Service_Desk_Junior_Miguel_Magalhaes.pdf"
)

NAVY = colors.HexColor("#14213D")
NAVY_2 = colors.HexColor("#20345B")
TEAL = colors.HexColor("#00A7B5")
BLUE = colors.HexColor("#2878C8")
INK = colors.HexColor("#1D2733")
MUTED = colors.HexColor("#5C6878")
PALE = colors.HexColor("#EEF7FA")
PALE_BLUE = colors.HexColor("#EEF4FB")
PALE_GOLD = colors.HexColor("#FFF7E5")
PALE_GREEN = colors.HexColor("#ECF8F3")
PALE_RED = colors.HexColor("#FDEEEF")
RULE = colors.HexColor("#D9E1EA")
WHITE = colors.white

PAGE_W, PAGE_H = A4
LEFT = 17 * mm
RIGHT = 17 * mm
TOP = 22 * mm
BOTTOM = 17 * mm
CONTENT_W = PAGE_W - LEFT - RIGHT


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="GuideBody",
        fontName="Verdana",
        fontSize=8.7,
        leading=12.2,
        textColor=INK,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        name="GuideSmall",
        parent=styles["GuideBody"],
        fontSize=7.55,
        leading=10.4,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="GuideH1",
        fontName="Verdana-Bold",
        fontSize=17.5,
        leading=21,
        textColor=NAVY,
        spaceBefore=0,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="GuideH2",
        fontName="Verdana-Bold",
        fontSize=11.3,
        leading=14.2,
        textColor=NAVY,
        spaceBefore=8,
        spaceAfter=5,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="GuideH3",
        fontName="Verdana-Bold",
        fontSize=9.3,
        leading=12,
        textColor=NAVY_2,
        spaceBefore=5,
        spaceAfter=3,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="GuideBullet",
        parent=styles["GuideBody"],
        leftIndent=10,
        firstLineIndent=-7,
        bulletIndent=1,
        spaceAfter=2.6,
    )
)
styles.add(
    ParagraphStyle(
        name="GuideNumber",
        parent=styles["GuideBody"],
        leftIndent=15,
        firstLineIndent=-13,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="GuideQuote",
        parent=styles["GuideBody"],
        fontSize=8.45,
        leading=12.1,
        leftIndent=2,
        rightIndent=2,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="GuideEnglish",
        parent=styles["GuideQuote"],
        textColor=NAVY_2,
    )
)
styles.add(
    ParagraphStyle(
        name="GuideTable",
        parent=styles["GuideBody"],
        fontSize=7.6,
        leading=10.2,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        name="GuideTableHead",
        parent=styles["GuideTable"],
        fontName="Verdana-Bold",
        textColor=WHITE,
        alignment=TA_LEFT,
    )
)
styles.add(
    ParagraphStyle(
        name="CoverKicker",
        fontName="Verdana-Bold",
        fontSize=9,
        leading=12,
        textColor=TEAL,
        tracking=1.2,
    )
)
styles.add(
    ParagraphStyle(
        name="CoverTitle",
        fontName="Verdana-Bold",
        fontSize=27,
        leading=31,
        textColor=NAVY,
        spaceAfter=7,
    )
)
styles.add(
    ParagraphStyle(
        name="CoverSub",
        fontName="Verdana",
        fontSize=12,
        leading=17,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="CoverName",
        fontName="Verdana-Bold",
        fontSize=12.5,
        leading=16,
        textColor=NAVY,
    )
)


def P(text: str, style: str = "GuideBody") -> Paragraph:
    return Paragraph(text, styles[style])


def H1(text: str) -> Paragraph:
    return P(text, "GuideH1")


def H2(text: str) -> Paragraph:
    return P(text, "GuideH2")


def H3(text: str) -> Paragraph:
    return P(text, "GuideH3")


def bullet(text: str) -> Paragraph:
    return Paragraph(f"• {text}", styles["GuideBullet"])


def num(n: int, text: str) -> Paragraph:
    return Paragraph(f"<b>{n}.</b> {text}", styles["GuideNumber"])


def box(title: str, body: str, fill=PALE, title_color=NAVY) -> Table:
    content = []
    if title:
        content.append(P(f"<font color='{title_color.hexval()}'><b>{title}</b></font>", "GuideBody"))
    content.append(P(body, "GuideQuote"))
    t = Table([[content]], colWidths=[CONTENT_W], hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), fill),
                ("BOX", (0, 0), (-1, -1), 0.55, RULE),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return t


def bilingual(question: str, pt: str, en: str) -> list:
    return [
        KeepTogether(
            [
                H3(question),
                box("RESPOSTA EM PORTUGUÊS", pt, PALE_GREEN, TEAL),
                Spacer(1, 3),
                box("ANSWER IN ENGLISH", en, PALE_BLUE, BLUE),
                Spacer(1, 4),
            ]
        )
    ]


def section_title(story: list, n: str, title: str, subtitle: str = "") -> None:
    story.append(P(f"GUIÃO {n}", "CoverKicker"))
    story.append(H1(title))
    if subtitle:
        story.append(P(subtitle, "GuideSmall"))
        story.append(Spacer(1, 4))


def table(data, widths, header=True, font_size=7.5) -> Table:
    rows = []
    for r, row in enumerate(data):
        rows.append(
            [
                Paragraph(str(cell), styles["GuideTableHead"] if header and r == 0 else styles["GuideTable"])
                for cell in row
            ]
        )
    t = Table(rows, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    commands = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    if header:
        commands += [("BACKGROUND", (0, 0), (-1, 0), NAVY)]
        start = 1
    else:
        start = 0
    for r in range(start, len(rows)):
        if (r - start) % 2:
            commands.append(("BACKGROUND", (0, r), (-1, r), colors.HexColor("#F8FAFC")))
    t.setStyle(TableStyle(commands))
    return t


def page_header_footer(c, doc):
    page = c.getPageNumber()
    if page == 1:
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, PAGE_H - 16 * mm, PAGE_W, 16 * mm, stroke=0, fill=1)
        c.setFillColor(TEAL)
        c.rect(0, PAGE_H - 16 * mm, 46 * mm, 3.5 * mm, stroke=0, fill=1)
        c.setFillColor(BLUE)
        c.rect(46 * mm, PAGE_H - 16 * mm, 22 * mm, 3.5 * mm, stroke=0, fill=1)
        c.restoreState()
        return
    c.saveState()
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 13 * mm, PAGE_W, 13 * mm, stroke=0, fill=1)
    c.setFont("Verdana-Bold", 7.1)
    c.setFillColor(WHITE)
    c.drawString(LEFT, PAGE_H - 8.4 * mm, "KONICA MINOLTA | IT SERVICE DESK JUNIOR")
    c.setFont("Verdana", 7.1)
    c.drawRightString(PAGE_W - RIGHT, PAGE_H - 8.4 * mm, "GUIÃO DE ENTREVISTA")
    c.setStrokeColor(RULE)
    c.setLineWidth(0.55)
    c.line(LEFT, 12.2 * mm, PAGE_W - RIGHT, 12.2 * mm)
    c.setFont("Verdana", 6.8)
    c.setFillColor(MUTED)
    c.drawString(LEFT, 8.2 * mm, "Miguel Magalhães • Entrevista: 15/09/2026 às 11:00")
    c.drawRightString(PAGE_W - RIGHT, 8.2 * mm, f"p. {page}")
    c.restoreState()


class GuideDocTemplate(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=LEFT,
            rightMargin=RIGHT,
            topMargin=TOP,
            bottomMargin=BOTTOM,
            title="Guia de Preparação - Konica Minolta IT Service Desk Junior",
            author="Miguel Magalhães",
            subject="Guia personalizado para entrevista",
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
            id="main",
        )
        self.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=page_header_footer)])


def make_story():
    s = []

    # Cover
    s += [
        Spacer(1, 27 * mm),
        P("ENTREVISTA • 15 SETEMBRO 2026 • 11:00", "CoverKicker"),
        Spacer(1, 4 * mm),
        P("Guia de preparação<br/>IT Service Desk Junior", "CoverTitle"),
        P("Konica Minolta Business Solutions Portugal", "CoverSub"),
        Spacer(1, 18 * mm),
        box(
            "OBJETIVO",
            "Entrar na entrevista com uma mensagem clara: tens experiência prática de suporte, fundamentos sólidos, método, responsabilidade e capacidade para aprofundar L2, Microsoft 365 e Intune sem exagerar o que ainda não fizeste em produção.",
            PALE_BLUE,
            BLUE,
        ),
        Spacer(1, 8 * mm),
        Table(
            [
                [P("FORMATO", "GuideSmall"), P("FUNÇÃO", "GuideSmall"), P("LOCAL", "GuideSmall")],
                [P("Entrevista", "GuideBody"), P("1.ª e 2.ª linha", "GuideBody"), P("Presencial / cliente", "GuideBody")],
            ],
            colWidths=[CONTENT_W / 3] * 3,
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                    ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#F8FAFC")),
                    ("BOX", (0, 0), (-1, -1), 0.5, RULE),
                    ("INNERGRID", (0, 0), (-1, -1), 0.4, RULE),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ]
            ),
        ),
        Spacer(1, 24 * mm),
        P("Miguel Magalhães", "CoverName"),
        P("Engenharia Informática • Redes e Sistemas • Suporte Técnico", "CoverSub"),
        Spacer(1, 8 * mm),
        P("Não memorizes frases palavra por palavra. Memoriza a estrutura, os factos e dois ou três exemplos reais.", "GuideSmall"),
        PageBreak(),
    ]

    # Quick strategy
    section_title(s, "01", "Estratégia de entrevista", "O mapa mental que deve orientar todas as respostas.")
    s += [
        box(
            "A TUA PROPOSTA DE VALOR EM UMA FRASE",
            "Sou um profissional júnior com experiência real de suporte a utilizadores, Windows, Active Directory, equipamentos, conectividade e tickets; investigo de forma estruturada, documento bem, respeito segurança e tenho base técnica para aprofundar L2, Microsoft 365 e Intune rapidamente.",
            PALE_GREEN,
            TEAL,
        ),
        H2("As quatro mensagens que o entrevistador deve reter"),
        num(1, "<b>Já fizeste suporte real.</b> NewCoffee, Staples e estágio deram-te contacto com utilizadores, equipamentos, contas, acessos, impressão, conectividade e aplicações."),
        num(2, "<b>Não és apenas reativo.</b> Criaste uma plataforma interna de ITSM e valorizas tickets completos, documentação, indicadores e melhoria de processos."),
        num(3, "<b>Trabalhas com método e segurança.</b> Primeiro defines impacto e âmbito, recolhes evidência, testas por camadas, validas, documentas e escalas com contexto."),
        num(4, "<b>És honesto sobre as lacunas.</b> Não apresentas Intune nem administração avançada de Microsoft 365 como experiência de produção; mostras conhecimento conceptual e aprendizagem rápida."),
        H2("Como responder bem"),
        table(
            [
                ["Tipo de pergunta", "Estrutura recomendada"],
                ["Sobre ti / motivação", "Presente -> experiência relevante -> prova -> razão para esta função."],
                ["Experiência", "Situação -> tarefa -> ações concretas -> resultado verdadeiro -> aprendizagem."],
                ["Cenário técnico", "Âmbito/impacto -> evidência -> hipóteses por camadas -> testes -> correção segura -> validação/documentação."],
                ["Ferramenta desconhecida", "Admitir limite -> explicar finalidade/conceitos -> descrever abordagem de aprendizagem e investigação."],
                ["Salário / prevenção", "Clarificar pacote e regras -> falar em bruto anual/base -> separar disponibilidade de intervenções."],
            ],
            [47 * mm, CONTENT_W - 47 * mm],
        ),
        H2("Regra de ouro"),
        box(
            "",
            "Sê específico sem inventar. É mais forte dizer «usei Active Directory para operações básicas de contas, grupos e permissões» do que dizer apenas «domino AD». É mais credível dizer «ainda não administrei Intune autonomamente em produção» do que tentar parecer sénior.",
            PALE_GOLD,
            colors.HexColor("#996B00"),
        ),
        PageBreak(),
    ]

    # Fit matrix
    section_title(s, "02", "Leitura da vaga e compatibilidade", "O anúncio pede um júnior operacional, rigoroso e orientado para o utilizador.")
    s += [
        table(
            [
                ["Necessidade da vaga", "A tua evidência", "Como posicionar"],
                ["Background em IT", "Licenciatura em Engenharia Informática; CTeSP em Redes e Sistemas; mestrado pós-laboral em Cibersegurança.", "Correspondência forte."],
                ["1+ ano em suporte", "NewCoffee, Staples e estágio com tarefas de suporte e sistemas.", "Explicar cronologia e tarefas, sem somar experiências como se fossem todas full-time."],
                ["Windows / hardware", "Preparação e suporte de desktops, laptops, impressoras, periféricos e equipamentos Windows.", "Usar um incidente real."],
                ["Active Directory", "Operações de contas, grupos, permissões e acessos na NewCoffee.", "Dizer «operações básicas/práticas», não arquitetura avançada."],
                ["Microsoft 365", "Contacto com ambientes e ferramentas Microsoft; base de troubleshooting.", "Mostrar método; não reclamar administração avançada se não ocorreu."],
                ["Ticketing / SLA / KB", "Atendimento e acompanhamento de pedidos; plataforma interna de ITSM; documentação técnica.", "Excelente diferenciador."],
                ["TCP/IP, DNS, DHCP", "CTeSP em redes; troubleshooting de DHCP, VPN, conectividade e acesso remoto.", "Explicar diagnóstico por testes progressivos."],
                ["MFA / phishing / passwords", "Formação em redes e cibersegurança; mestrado em curso.", "Ligar sempre a identidade, autorização e evidência."],
                ["Intune", "Conhecimento conceptual, sem administração autónoma confirmada em produção.", "Lacuna assumida + plano de aprendizagem."],
                ["On-call 24/7", "Disponibilidade não deve ser presumida.", "Confirmar apenas se for verdade; pedir regras, volume, escalamento e compensação."],
                ["Inglês / condução", "Inglês B2; carta de condução B.", "Preparar apresentação e resposta técnica curta em inglês."],
            ],
            [43 * mm, 73 * mm, CONTENT_W - 116 * mm],
        ),
        Spacer(1, 6),
        box(
            "AVALIAÇÃO HONESTA",
            "Tens boa adequação a uma função júnior de Service Desk. A entrevista deverá testar menos «conhecimento enciclopédico» e mais: método de diagnóstico, comunicação, segurança, qualidade do ticket, autonomia responsável e reação à prevenção.",
            PALE_BLUE,
            BLUE,
        ),
        PageBreak(),
    ]

    # Company research
    section_title(s, "03", "Konica Minolta: o que saber", "Pesquisa orientada para a função - não é apenas uma empresa de impressão.")
    s += [
        H2("Mensagem curta sobre a empresa"),
        box(
            "",
            "Sei que a Konica Minolta nasceu da área de imagem e impressão, mas hoje a operação portuguesa é muito mais ampla: Digital Workplace, infraestrutura e cloud, Managed Services, BPO, segurança e automação. A área de serviços de IT acompanha ambientes de clientes, utiliza SLAs e valoriza suporte, monitorização, documentação e melhoria contínua.",
            PALE_GREEN,
            TEAL,
        ),
        H2("Factos úteis"),
        bullet("A empresa apresenta-se como fornecedora global de serviços de IT e processos documentais, com soluções de Digital Workplace, cloud, infraestrutura, segurança, automação e gestão da informação."),
        bullet("Os Managed IT Services incluem manutenção de PCs e servidores, suporte a utilizadores, monitorização e remediação 24/7, administração alinhada com ITIL e SLAs."),
        bullet("No modelo BPO, equipas dedicadas trabalham no ambiente do cliente; são acompanhados indicadores como tempo de resposta, resolução de tickets e cumprimento de SLA."),
        bullet("Em Portugal, a organização comunica cerca de 200 colaboradores e escritórios em Lisboa, Porto, Coimbra e Faro; refere também cinco anos consecutivos entre as 100 melhores empresas para trabalhar."),
        bullet("Valores oficiais: abertura e honestidade, foco no cliente, inovação, paixão, inclusão/colaboração e responsabilidade."),
        H2("Porque queres trabalhar aqui?"),
    ]
    s += bilingual(
        "Resposta modelo",
        "Esta oportunidade interessa-me porque junta suporte de primeira e segunda linha, contacto direto com utilizadores, ambiente Microsoft, redes, documentação e melhoria contínua. Gosto também da transformação da Konica Minolta numa empresa de Digital Workplace e serviços de IT. Vejo aqui um contexto estruturado, com acompanhamento e plano de evolução, no qual posso contribuir desde cedo e aprofundar competências em Microsoft 365, Intune e suporte L2.",
        "This opportunity interests me because it combines first- and second-line support, direct user contact, Microsoft environments, networking, documentation and continuous improvement. I am also interested in Konica Minolta's evolution into a Digital Workplace and IT services provider. I see a structured environment where I can contribute from the beginning while developing deeper Microsoft 365, Intune and L2 support skills.",
    )
    s += [
        box(
            "PERGUNTA IMPORTANTE",
            "Como o anúncio diz «para alocar ao nosso cliente», pergunta qual é o setor, a localização concreta, a dimensão da equipa, quem define prioridades e como funciona o acompanhamento entre o cliente e a Konica Minolta.",
            PALE_GOLD,
            colors.HexColor("#996B00"),
        ),
        PageBreak(),
    ]

    # Intro scripts
    section_title(s, "04", "A tua apresentação", "Objetivo: 75-90 segundos, segura, natural e ligada à vaga.")
    s += bilingual(
        "Fala-me um pouco sobre ti / Tell me about yourself",
        "Sou licenciado em Engenharia Informática e tenho também um CTeSP em Redes e Sistemas Informáticos. Atualmente frequento um mestrado em Cibersegurança e Auditoria de Sistemas Informáticos, em regime pós-laboral. A minha experiência combina suporte técnico, sistemas, redes e desenvolvimento. Na NewCoffee prestei suporte de primeira linha a diferentes departamentos e localizações, resolvendo incidentes relacionados com Windows, equipamentos, contas, permissões, VPN, DHCP, conectividade, impressão e aplicações empresariais. Trabalhei também com Active Directory, inventário e articulação com fornecedores externos. Antes disso, tive experiência de suporte na Staples. Desenvolvi ainda uma plataforma interna de ITSM para tickets, ativos, utilizadores e indicadores. Procuro agora consolidar a minha carreira em Service Desk, aprofundar o suporte de primeira e segunda linha e contribuir para um serviço organizado, seguro e orientado para o utilizador.",
        "I hold a Bachelor's degree in Computer Engineering and a higher technical qualification in Computer Networks and Systems. I am currently pursuing a Master's degree in Cybersecurity and Computer Systems Auditing through an evening programme. My experience combines technical support, systems, networking and development. At NewCoffee, I provided first-line support across different departments and company locations, handling incidents involving Windows, equipment, accounts, permissions, VPN, DHCP, connectivity, printing and business applications. I also worked with Active Directory, IT asset management and external IT providers. Before that, I gained additional support experience at Staples. I also developed an internal ITSM platform for tickets, assets, users and operational indicators. I am now looking to consolidate my career in Service Desk, deepen my L1 and L2 support experience and contribute to a structured, secure and user-focused service.",
    )
    s += [
        H2("Versão de 30 segundos"),
        box(
            "PORTUGUÊS",
            "Sou licenciado em Engenharia Informática, com formação adicional em Redes e Sistemas e experiência prática em suporte a utilizadores, Windows, Active Directory, equipamentos, conectividade e tickets. Na NewCoffee apoiei diferentes departamentos e localizações e articulei incidentes mais complexos com fornecedores. Procuro agora aprofundar Service Desk L1/L2 num ambiente estruturado como o da Konica Minolta.",
            PALE_GREEN,
            TEAL,
        ),
        Spacer(1, 3),
        box(
            "ENGLISH",
            "I am a Computer Engineering graduate with additional training in Networks and Systems and hands-on experience supporting users, Windows devices, Active Directory, connectivity and tickets. At NewCoffee, I supported different departments and locations and coordinated more complex issues with external providers. I am now looking to deepen my L1/L2 Service Desk experience in a structured environment such as Konica Minolta.",
            PALE_BLUE,
            BLUE,
        ),
        H2("Entrega"),
        bullet("Fala devagar; faz uma pausa curta entre formação, experiência e motivação."),
        bullet("Não enumeres todas as tecnologias do CV. Escolhe apenas as que a vaga pede."),
        bullet("Termina no futuro: o que procuras e como podes contribuir."),
        PageBreak(),
    ]

    # HR questions
    section_title(s, "05", "Perguntas de RH e motivação", "Respostas prontas, mas ajustáveis ao tom da conversa.")
    s += bilingual(
        "Porque devemos contratar-te? / Why should we hire you?",
        "Porque reúno a base técnica necessária, experiência real de contacto com utilizadores e uma forma estruturada de investigar problemas. Já trabalhei com Windows, Active Directory, equipamentos, aplicações, redes e tickets, e sei comunicar com utilizadores e fornecedores. Também tenho iniciativa para documentar e melhorar processos, como demonstrei ao desenvolver uma plataforma interna de ITSM. Não afirmo dominar todas as ferramentas da vaga, nomeadamente o Intune em produção, mas tenho as bases e a capacidade de aprendizagem necessárias para evoluir rapidamente.",
        "You should hire me because I combine the required technical foundation with real end-user support experience and a structured troubleshooting approach. I have worked with Windows, Active Directory, equipment, applications, networking and tickets, and I am comfortable communicating with users and external providers. I also take initiative to document and improve processes, as demonstrated by the internal ITSM platform I developed. I would not claim production-level expertise in every tool, particularly Intune, but I have the foundations and learning ability to become productive quickly.",
    )
    s += bilingual(
        "Qual é uma lacuna tua para esta função?",
        "Ainda não administrei Microsoft Intune de forma autónoma num ambiente empresarial de produção. Conheço a finalidade da plataforma - gestão de dispositivos, políticas, aplicações e conformidade - e tenho experiência relacionada com Windows, utilizadores, equipamentos e segurança. Quero transformar essa base em experiência prática através da formação e dos procedimentos da equipa.",
        "I have not yet independently administered Microsoft Intune in an enterprise production environment. I understand its purpose, including device management, policies, application deployment and compliance, and I have related experience with Windows, users, equipment and security. I want to turn that foundation into hands-on experience through training and the team's procedures.",
    )
    s += bilingual(
        "Como lidas com um utilizador frustrado?",
        "Escuto sem interromper, reconheço o impacto do problema e recolho factos concretos. Explico o que vou verificar, evito prometer um prazo que não consigo garantir e mantenho o utilizador informado. Mesmo quando não consigo resolver imediatamente, assumo o acompanhamento e comunico claramente o próximo passo.",
        "I listen without interrupting, acknowledge the impact and collect objective information. I explain what I will check, avoid promising a deadline I cannot guarantee and keep the user informed. Even when I cannot resolve the issue immediately, I take ownership of the follow-up and communicate the next step clearly.",
    )
    s += bilingual(
        "Como geres várias solicitações?",
        "Priorizo por impacto, urgência, risco de segurança, criticidade do serviço e SLA, e não apenas pela ordem de chegada. Confirmo se existe um incidente generalizado, comunico expectativas, mantenho os tickets atualizados e reavalio prioridades quando surge nova informação.",
        "I prioritise according to impact, urgency, security risk, service criticality and SLA, rather than simply following the order of arrival. I check for a widespread incident, communicate expectations, keep tickets updated and reassess priorities when new information becomes available.",
    )
    # Let the final bilingual answer and the next short section share a page.

    # HR continued
    section_title(s, "06", "Perguntas pessoais delicadas", "Prepara factos; não improvises justificações que possam contradizer o CV.")
    s += [
        H2("Porque saíste da NewCoffee / Staples / estágio?"),
        box(
            "REGRA",
            "Usa apenas o motivo verdadeiro. Responde em três partes: facto breve, aprendizagem positiva e ligação ao próximo passo. Exemplo de estrutura: «A colaboração terminou por [motivo real]. Foi uma experiência importante porque [aprendizagem]. Agora procuro [função estável/Service Desk/L1-L2]». Não critiques pessoas nem reveles informação confidencial.",
            PALE_GOLD,
            colors.HexColor("#996B00"),
        ),
        H2("O mestrado interfere com o horário?"),
        box(
            "RESPOSTA",
            "O mestrado decorre em regime pós-laboral e organizei-o precisamente para ser compatível com uma função full-time. Consigo gerir as duas responsabilidades com planeamento. Se existir prevenção, quero apenas conhecer a escala para me organizar antecipadamente.",
            PALE_GREEN,
            TEAL,
        ),
        H2("Disponibilidade para começar"),
        box(
            "RESPOSTA SEGURA",
            "Tenho interesse em iniciar assim que for possível, respeitando o processo e a data acordada. Posso confirmar uma data concreta depois de compreender as etapas seguintes. <br/><br/><b>Não inventes disponibilidade imediata</b> se tiveres compromissos que a impeçam.",
            PALE_BLUE,
            BLUE,
        ),
        H2("Carta de condução"),
        box("RESPOSTA", "Sim, tenho carta de condução válida, categoria B.", PALE_GREEN, TEAL),
        H2("Três forças que podes defender"),
        bullet("<b>Método de troubleshooting:</b> defines âmbito, testas hipóteses e documentas."),
        bullet("<b>Comunicação:</b> ajustas a linguagem ao utilizador e acompanhas até à validação."),
        bullet("<b>Iniciativa:</b> além do suporte, criaste uma plataforma de ITSM e procuraste melhorar organização e visibilidade."),
        H2("Uma fraqueza bem escolhida"),
        box(
            "",
            "Por vezes tenho tendência a querer compreender o problema com bastante detalhe. Tenho aprendido a equilibrar profundidade com impacto e SLA: primeiro restauro o serviço de forma segura, depois aprofundo a causa quando o contexto o permite.",
            PALE_BLUE,
            BLUE,
        ),
    ]

    # Method
    section_title(s, "07", "Método universal de troubleshooting", "Serve para quase todos os cenários técnicos da entrevista.")
    s += [
        table(
            [
                ["Passo", "O que fazer", "O que demonstra"],
                ["1. Acolher", "Confirmar utilizador, contacto e impacto; reconhecer urgência sem prometer o impossível.", "Comunicação e ownership."],
                ["2. Definir âmbito", "Um utilizador, vários, uma localização ou serviço global? Quando começou? Houve alterações?", "Prioridade e raciocínio."],
                ["3. Recolher evidência", "Mensagem exata, hora, equipamento, screenshots/logs, configuração e passos de reprodução.", "Precisão."],
                ["4. Isolar por camadas", "Hardware -> Windows -> rede -> identidade/permissões -> aplicação/serviço.", "Método."],
                ["5. Testar", "Uma alteração de cada vez; começar por ações de baixo risco e reversíveis.", "Segurança operacional."],
                ["6. Resolver / contornar", "Aplicar correção autorizada ou workaround seguro; não mascarar risco de segurança.", "Eficiência."],
                ["7. Validar", "Confirmar com o utilizador e, se aplicável, verificar logs/monitorização.", "Qualidade."],
                ["8. Documentar / escalar", "Sintomas, testes, resultados, causa, resolução e próximo passo; escalar antes do SLA estar em risco.", "Continuidade e colaboração."],
            ],
            [22 * mm, 102 * mm, CONTENT_W - 124 * mm],
        ),
        Spacer(1, 6),
    ]
    s += bilingual(
        "Resposta universal",
        "Começo por confirmar o impacto e o âmbito: um utilizador, vários utilizadores ou todo o serviço. Recolho a mensagem de erro, quando começou e alterações recentes. Tento reproduzir, verifico primeiro as causas mais simples e depois avanço por camadas: equipamento, sistema operativo, rede, identidade e aplicação. Consulto logs quando aplicável, faço uma alteração controlada de cada vez e valido o resultado com o utilizador. No final, documento sintomas, testes, causa, resolução e medidas preventivas. Se ultrapassar o meu nível de acesso ou conhecimento, escalo com toda a evidência recolhida.",
        "I first confirm the impact and scope: one user, several users or the entire service. I collect the exact error, when it started and any recent changes. I try to reproduce the issue, check the simplest causes first and then work through the layers: equipment, operating system, network, identity and application. I review logs when relevant, make one controlled change at a time and validate the result with the user. Finally, I document the symptoms, tests, cause, resolution and preventive actions. If the issue exceeds my access or knowledge level, I escalate it with all the evidence collected.",
    )
    s += [
        box(
            "ERRO A EVITAR",
            "Nunca respondas apenas «reiniciava o computador». Um reinício pode ser um teste legítimo, mas explica primeiro o âmbito, a hipótese que estás a testar, o impacto e a validação posterior.",
            PALE_RED,
            colors.HexColor("#A02B33"),
        ),
        PageBreak(),
    ]

    # Ticketing
    section_title(s, "08", "Ticketing, SLA, prioridade e Knowledge Base", "Esta área liga diretamente a vaga à tua plataforma interna de ITSM.")
    s += [
        H2("O que é um SLA?"),
        P("Um <b>Service Level Agreement</b> define níveis e tempos esperados, como resposta, atualização e resolução. Cumprir SLA não é apenas «fechar depressa»: exige classificação correta, prioridade por impacto e urgência, comunicação, escalamento atempado e registos completos."),
        H2("Como priorizar"),
        table(
            [
                ["Prioridade", "Exemplo", "Ação"],
                ["P1 - Crítica", "Serviço essencial indisponível para muitos utilizadores ou incidente grave de segurança.", "Resposta imediata, comunicação frequente, escalamento e coordenação."],
                ["P2 - Alta", "Função importante afetada, sem alternativa adequada, impacto relevante.", "Diagnóstico rápido e escalamento antes do risco de incumprimento."],
                ["P3 - Média", "Um utilizador afetado, trabalho condicionado, workaround possível.", "Tratar dentro do SLA e manter o utilizador informado."],
                ["P4 - Baixa / pedido", "Pedido planeado, informação ou melhoria sem impacto imediato.", "Agendar e executar com aprovação."],
            ],
            [29 * mm, 86 * mm, CONTENT_W - 115 * mm],
        ),
        H2("O que deve conter um bom ticket"),
        bullet("Utilizador, contacto, equipamento, localização, data e hora."),
        bullet("Serviço afetado, sintomas, mensagem de erro exata, impacto e prioridade."),
        bullet("Alterações recentes, passos para reproduzir, testes efetuados e resultados."),
        bullet("Comunicações, aprovações, causa quando conhecida, resolução/workaround e validação final."),
        H2("Quando escalar"),
        P("Quando faltam permissões ou conhecimento, existe risco elevado, segurança, impacto alargado, dependência de fornecedor, mudança não autorizada ou risco de incumprir SLA. O escalamento deve levar contexto, e não apenas «não funciona»."),
        H2("Knowledge Base"),
        P("Título pesquisável; sintomas e âmbito; causa conhecida; pré-requisitos; passos numerados; evidência; validação; rollback e riscos; data/versão. Outro técnico deve conseguir repetir a solução sem depender da tua memória."),
        box(
            "A TUA PROVA",
            "A plataforma ITSM que desenvolveste centralizava tickets, ativos, utilizadores, departamentos e indicadores. Usa-a para demonstrar que compreendes o processo, não apenas a ferramenta.",
            PALE_GREEN,
            TEAL,
        ),
        PageBreak(),
    ]

    # Windows Hardware
    section_title(s, "09", "Windows, hardware e periféricos", "Diagnosticar é isolar a camada com evidência.")
    s += [
        H2("Ferramentas Windows úteis"),
        table(
            [
                ["Ferramenta", "Serve para"],
                ["Task Manager", "Processos, recursos, arranque, aplicações bloqueadas e utilização anormal."],
                ["Event Viewer", "Eventos de aplicação, sistema, segurança e códigos de erro com data/hora."],
                ["Reliability Monitor", "Histórico visual de falhas, atualizações e alterações."],
                ["Device Manager", "Estado de hardware, drivers, códigos de erro e dispositivos desconhecidos."],
                ["Services", "Estado e arranque de serviços, por exemplo Print Spooler."],
                ["Windows Update", "Patches, reinícios pendentes, drivers e falhas de atualização."],
                ["Disk / storage", "Espaço livre, saúde, permissões e risco antes de alterações."],
            ],
            [49 * mm, CONTENT_W - 49 * mm],
        ),
        H2("Cenário: monitor na docking station sem imagem"),
        P("Confirmar alimentação da dock, cabos, entrada selecionada e deteção no Windows. Testar outro cabo, porta e monitor; ligar diretamente ao portátil; verificar drivers/firmware. O objetivo é distinguir monitor, cabo, porta, dock, driver ou computador."),
        H2("Cenário: computador não arranca"),
        P("Verificar alimentação, carregador, bateria, cabos e indicadores; retirar periféricos; identificar se existe POST, se chega ao Windows e se há código de erro. Usar diagnóstico do fabricante ou recuperação do Windows, protegendo dados antes de ações com risco."),
        H2("Cenário: impressora não imprime"),
        P("Determinar se afeta um utilizador ou todos; verificar estado físico/rede, fila, impressora predefinida, trabalhos bloqueados e serviço de spooler; confirmar IP, conectividade e driver; imprimir página de teste; escalar falha física com evidência."),
        H2("Cenário: Windows bloqueia repetidamente"),
        P("Recolher código/hora, alterações recentes, Event Viewer e Reliability Monitor; verificar atualizações, drivers, espaço e integridade; testar correção controlada; avaliar impacto e dados antes de rollback ou recuperação."),
        box(
            "FRASE FORTE",
            "Tentaria reproduzir e comparar com um equipamento funcional. Faria uma alteração de cada vez para saber qual hipótese foi confirmada, e validaria o resultado antes de fechar o ticket.",
            PALE_BLUE,
            BLUE,
        ),
        PageBreak(),
    ]

    # Networking
    section_title(s, "10", "Redes: o essencial para Service Desk", "Explica o que cada teste prova; não recites comandos sem objetivo.")
    s += [
        table(
            [
                ["Conceito", "Definição prática"],
                ["TCP/IP", "Conjunto base de protocolos que permite comunicação entre dispositivos em rede."],
                ["DHCP", "Atribui automaticamente IP, máscara, gateway e DNS."],
                ["DNS", "Traduz nomes como empresa.pt para endereços IP."],
                ["Gateway", "Encaminha tráfego da rede local para outras redes."],
                ["VPN", "Cria um túnel protegido para acesso remoto a recursos autorizados."],
                ["APIPA", "Endereço 169.254.x.x atribuído pelo Windows quando não obtém configuração do DHCP."],
                ["TCP vs UDP", "TCP privilegia entrega ordenada/fiável; UDP reduz overhead e é comum em tempo real."],
            ],
            [42 * mm, CONTENT_W - 42 * mm],
        ),
        H2("Diagnóstico progressivo: «tenho Wi-Fi, mas não Internet»"),
        num(1, "Confirmar âmbito e obter configuração com <b>ipconfig /all</b>: IP, máscara, gateway, DNS e DHCP."),
        num(2, "Testar <b>127.0.0.1</b> e o IP local se houver suspeita da pilha/adaptador."),
        num(3, "Testar o <b>gateway</b>. Se falhar, investigar ligação local, Wi-Fi, VLAN, adaptador ou porta."),
        num(4, "Testar um <b>IP externo</b>. Se falhar após o gateway, investigar routing, firewall, NAT ou fornecedor."),
        num(5, "Testar um <b>nome de domínio</b> e usar <b>nslookup</b>. Se o IP funcionar e o nome não, suspeitar de DNS."),
        num(6, "Comparar com outro utilizador/dispositivo e verificar alertas/alterações; corrigir ou escalar com resultados."),
        H2("Comandos que deves reconhecer"),
        table(
            [
                ["Comando", "Hipótese que ajuda a testar"],
                ["ipconfig /all", "Configuração recebida, DHCP, gateway e DNS."],
                ["ping", "Alcance e latência básica; não prova sozinho que a aplicação funciona."],
                ["tracert", "Onde o caminho deixa de responder."],
                ["nslookup", "Resolução DNS e servidor consultado."],
                ["arp -a", "Relação local entre endereços IP e MAC."],
                ["route print", "Rotas e gateway usados pelo computador."],
                ["netstat -ano", "Ligações, portas e PID local."],
            ],
            [42 * mm, CONTENT_W - 42 * mm],
        ),
        PageBreak(),
    ]

    # M365
    section_title(s, "11", "Microsoft 365: cenários prováveis", "Começa sempre por distinguir cliente local, conta, rede e serviço cloud.")
    s += [
        H2("Outlook não envia nem recebe"),
        num(1, "Âmbito, conectividade e mensagem exata; verificar modo offline e sincronização."),
        num(2, "Testar <b>Outlook Web</b>: se funcionar, suspeitar do cliente/perfil local; se não, conta, licença, serviço ou rede."),
        num(3, "Confirmar credenciais/MFA, quota, add-ins, atualizações e saúde do Microsoft 365, se houver acesso."),
        num(4, "Só reparar ou recriar perfil depois de excluir causas simples e proteger dados locais."),
        H2("Teams sem áudio ou microfone"),
        P("Confirmar dispositivo de entrada/saída no Teams, permissões do Windows, mute físico e volume; fazer chamada de teste; testar outro dispositivo; comparar desktop com web; verificar drivers, rede e saúde do serviço se vários utilizadores forem afetados."),
        H2("OneDrive não sincroniza"),
        P("Verificar pausa, conta/tenant, espaço, nomes/caminhos/tipos inválidos, ícone e erro do cliente; testar web e reiniciar cliente. Antes de desvincular ou fazer reset, proteger ficheiros locais."),
        H2("Access denied no SharePoint"),
        P("Confirmar URL, conta/tenant e recurso; perceber se é site, biblioteca ou ficheiro; verificar grupos, permissões e herança. Não conceder acesso sem aprovação do proprietário/responsável; aplicar menor privilégio."),
        H2("Muitos utilizadores afetados"),
        P("Tratar como incidente de maior impacto: correlacionar tickets, confirmar serviços/localizações, verificar rede, DNS e service health; comunicar; não alterar individualmente cada PC; escalar como falha de tenant, rede ou fornecedor."),
        box(
            "RESPOSTA HONESTA",
            "Tenho experiência de suporte em ambientes Windows e com utilizadores/aplicações empresariais. Em Microsoft 365 aplicaria este método de isolamento. Onde a operação exigir privilégios ou conhecimento específico do tenant, seguiria os runbooks e escalaria com evidência.",
            PALE_GOLD,
            colors.HexColor("#996B00"),
        ),
        PageBreak(),
    ]

    # AD and Intune
    section_title(s, "12", "Active Directory, identidade e Intune", "A velocidade nunca justifica saltar autorização ou menor privilégio.")
    s += [
        H2("Reset de password / conta bloqueada"),
        P("Verificar identidade pelo procedimento; confirmar se a conta está bloqueada, desativada ou expirada; investigar bloqueios recorrentes; fazer reset com permissão adequada; exigir mudança no próximo login quando aplicável; nunca enviar credenciais por canal inseguro; validar e documentar."),
        H2("Novo colaborador"),
        P("Começar por pedido aprovado com função, responsável e data; seguir convenção e template; colocar na OU correta; atribuir apenas grupos e acessos autorizados; preparar licenças/aplicações/equipamento; validar e registar."),
        H2("Pedido para adicionar a grupo"),
        P("Confirmar finalidade, proprietário e aprovação. Só depois alterar; validar acesso e registar quem aprovou, o que mudou e quando."),
        H2("O que sabes sobre Intune?"),
    ]
    s += bilingual(
        "Resposta segura",
        "O Intune é uma plataforma cloud de gestão de endpoints e aplicações. Permite inscrever dispositivos, distribuir aplicações e configurações, aplicar políticas de segurança e conformidade e suportar acesso condicional em conjunto com o Entra ID. Conheço estes conceitos, mas ainda não administrei Intune autonomamente em produção. Perante um dispositivo não conforme, começaria pela política que falhou, estado e sincronização do dispositivo, atribuição ao utilizador e logs, seguindo os procedimentos da organização.",
        "Intune is a cloud-based endpoint and application management platform. It supports device enrolment, application and configuration deployment, security and compliance policies, and Conditional Access together with Entra ID. I understand these concepts, but I have not yet independently administered Intune in production. For a non-compliant device, I would begin by reviewing the failed policy, device status and synchronisation, user assignment and logs, following the organisation's procedures.",
    )
    s += [
        H2("Conceitos associados"),
        bullet("<b>MDM:</b> gestão de dispositivos; <b>MAM:</b> gestão/proteção de aplicações e dados."),
        bullet("<b>Compliance:</b> dispositivo cumpre requisitos definidos; não é sinónimo de estar totalmente seguro."),
        bullet("<b>Conditional Access:</b> decisões de acesso baseadas em identidade, dispositivo, localização, risco e outras condições."),
        bullet("<b>Entra ID:</b> serviço cloud de identidade e acesso anteriormente designado Azure AD."),
        PageBreak(),
    ]

    # Security
    section_title(s, "13", "Segurança, MFA e phishing", "Service Desk é uma linha de defesa: verifica identidade, autorização e evidência.")
    s += [
        H2("O que é MFA?"),
        P("Autenticação multifator exige fatores de categorias diferentes, por exemplo password e confirmação numa aplicação autenticadora. Reduz a probabilidade de uma password comprometida ser suficiente para entrar."),
        H2("Utilizador deixou de receber pedidos de MFA"),
        P("Verificar identidade; rede, data/hora e notificações do dispositivo; método registado; seguir procedimento de re-registo ou método alternativo autorizado. Nunca desativar ou contornar MFA apenas para resolver depressa."),
        H2("Email suspeito de phishing"),
        num(1, "Pedir para não clicar, responder ou abrir anexos; preservar a mensagem."),
        num(2, "Recolher remetente, assunto, links/cabeçalhos e hora segundo o processo definido."),
        num(3, "Se houve interação, confirmar exatamente o que aconteceu e escalar imediatamente para contenção."),
        num(4, "Ações possíveis pela equipa autorizada: reset de credenciais, revogação de sessões, bloqueio e análise do dispositivo."),
        num(5, "Documentar sem destruir evidência e comunicar os próximos passos ao utilizador."),
        H2("Princípios a mencionar"),
        table(
            [
                ["Princípio", "Aplicação no Service Desk"],
                ["Menor privilégio", "Conceder apenas o acesso necessário e aprovado."],
                ["Need-to-know", "Não expor dados ou detalhes a quem não está autorizado."],
                ["Verificação de identidade", "Obrigatória antes de resets e alterações sensíveis."],
                ["Defesa em profundidade", "Password, MFA, endpoint, rede, monitorização e processos combinados."],
                ["Auditabilidade", "Registar aprovação, alteração, hora, responsável e resultado."],
            ],
            [45 * mm, CONTENT_W - 45 * mm],
        ),
        box(
            "NÃO FAZER",
            "Não desativar MFA, não partilhar passwords, não dar privilégios por pedido informal, não apagar evidência de phishing e não instalar software não autorizado.",
            PALE_RED,
            colors.HexColor("#A02B33"),
        ),
        PageBreak(),
    ]

    # Scenario drills
    section_title(s, "14", "Simulação técnica rápida", "Treina cada resposta em 60-90 segundos.")
    scenario_rows = [
        ["Cenário", "Resposta em tópicos"],
        ["Utilizador sem Internet", "Âmbito -> ipconfig /all -> gateway -> IP externo -> DNS -> comparar -> corrigir/escalar -> validar."],
        ["Outlook não sincroniza", "Web vs desktop -> conectividade -> offline/erro -> conta/MFA/quota -> add-ins/saúde -> proteção de dados -> repair/escalamento."],
        ["Teams sem microfone", "Dispositivo selecionado -> permissões/mute -> test call -> outro hardware -> web vs app -> drivers/rede."],
        ["OneDrive parado", "Conta/tenant -> pausa/quota -> nomes/caminhos -> erro -> web -> reinício -> proteger dados antes de reset."],
        ["Conta AD bloqueada", "Verificar identidade -> estado/causa -> autorização -> desbloquear/reset -> não expor password -> validar/documentar."],
        ["Dock sem imagem", "Energia/entrada/cabo -> detetar no Windows -> trocar componente -> direto ao portátil -> driver/firmware -> isolar."],
        ["Possível phishing", "Não interagir -> preservar -> recolher evidência -> determinar interação -> escalar/conter -> documentar."],
        ["Vários utilizadores afetados", "Correlacionar e priorizar -> alterações/service health/rede -> comunicação -> evitar alterações individuais -> escalamento."],
        ["SLA perto do limite", "Atualizar diagnóstico -> avisar utilizador/responsável -> escalar antes da violação -> próximo passo -> nunca aplicar correção insegura."],
    ]
    s += [
        table(scenario_rows, [51 * mm, CONTENT_W - 51 * mm]),
        Spacer(1, 6),
        H2("Perguntas de aprofundamento que podem seguir"),
        bullet("Que informação colocarias no ticket?"),
        bullet("Como distingues um problema local de um incidente geral?"),
        bullet("Que risco existe antes de recriar um perfil, desvincular o OneDrive ou fazer reset?"),
        bullet("Quando deixas de investigar e escalas?"),
        bullet("Como comunicas a um utilizador que ainda não tens solução?"),
        H2("Resposta quando não sabes"),
    ]
    s += bilingual(
        "Frase de proteção",
        "Não tenho segurança suficiente para dar uma resposta exata sem confirmar. Começaria por validar estes pontos, consultaria a documentação e os procedimentos internos e, se existisse impacto ou risco, escalaria com a evidência recolhida.",
        "I am not confident enough to give an exact answer without verifying it. I would begin by checking these points, consult the documentation and internal procedures and, if there were impact or risk, escalate with the evidence collected.",
    )
    s.append(PageBreak())

    # STAR stories
    section_title(s, "15", "Histórias STAR do teu CV", "Escolhe três e preenche hoje com factos concretos. Não inventes métricas.")
    s += [
        table(
            [
                ["História", "Situação / tarefa", "Ações e resultado a preparar"],
                ["Conectividade na NewCoffee", "Incidente real de DHCP, VPN, acesso remoto ou rede.", "Âmbito; configuração; gateway/DNS; comparação; comunicação; escalamento; resultado verdadeiro."],
                ["Preparação de posto", "Novo utilizador/equipamento precisava de ficar operacional.", "Windows; periféricos; conta/grupos aprovados; aplicações; rede; impressão; inventário; validação."],
                ["Plataforma ITSM", "Necessidade de organizar tickets, ativos, utilizadores e indicadores.", "Levantamento; fluxos; React/PHP/SQL Server/IIS; o que centralizou ou tornou visível."],
                ["Escalamento a fornecedor", "Incidente excedeu acesso ou âmbito interno.", "Reproduzir; evidência; utilizadores/equipamentos; handoff estruturado; acompanhamento; validação."],
                ["Plataforma da clínica", "Incidente ou comportamento a investigar numa aplicação real.", "Logs; testes; causa; correção; validação; documentação. Explicar que foi projeto freelance."],
                ["Projeto IDS", "Projeto académico/internacional de rede e segurança.", "VirtualBox, Kali/Ubuntu, Wireshark, tcpdump, Snort; análise e aprendizagem. Não apresentar como produção."],
            ],
            [41 * mm, 61 * mm, CONTENT_W - 102 * mm],
        ),
        H2("Folha de preparação - história principal"),
        box(
            "S - SITUAÇÃO",
            "Onde e quando aconteceu? Quem foi afetado? Qual era o impacto? ________________________________________________",
            colors.white,
            NAVY,
        ),
        Spacer(1, 3),
        box(
            "T - TAREFA",
            "Qual era a tua responsabilidade e limite de acesso? _________________________________________________________",
            colors.white,
            NAVY,
        ),
        Spacer(1, 3),
        box(
            "A - AÇÕES",
            "Que perguntas, testes, ferramentas, comunicação e decisões foram teus? ______________________________________",
            colors.white,
            NAVY,
        ),
        Spacer(1, 3),
        box(
            "R - RESULTADO",
            "O que ficou resolvido/encaminhado? Como validaste? O que aprendeste? _________________________________________",
            colors.white,
            NAVY,
        ),
        PageBreak(),
    ]

    # On-call
    section_title(s, "16", "Prevenção remota 24/7", "Disponibilidade é uma responsabilidade operacional; esclarece as regras antes de aceitar.")
    s += bilingual(
        "Tens disponibilidade para prevenção? (usar apenas se for verdade)",
        "Sim, tenho disponibilidade para integrar uma escala de prevenção remota aproximadamente uma semana por mês. Gostaria de compreender como funciona a rotação, quais são os tempos de resposta, a frequência média de chamadas, o processo de escalamento e a respetiva compensação.",
        "Yes, I am available to participate in a remote on-call rotation for approximately one week per month. I would like to understand the rotation model, expected response times, average call frequency, escalation process and the applicable compensation.",
    )
    s += [
        H2("Se receberes um alerta crítico de madrugada"),
        P("Confirmar identidade/contacto, impacto, âmbito e criticidade; abrir/atualizar incidente; consultar alertas e alterações; seguir runbook; executar apenas ações autorizadas e reversíveis; manter cronologia; escalar pela matriz; validar recuperação; comunicar e fazer handover/RCA."),
        H2("Perguntas essenciais"),
        num(1, "A escala é exatamente uma semana em quatro? De que hora/dia a que hora/dia? Inclui feriados?"),
        num(2, "Qual é o tempo máximo de resposta e posso circular normalmente enquanto estou de prevenção?"),
        num(3, "Qual foi a média real de chamadas e intervenções por semana nos últimos três meses?"),
        num(4, "É sempre remoto ou pode exigir deslocação? Quem suporta custos e qual é o tempo de chegada?"),
        num(5, "Existe sempre L2/L3 ou gestor disponível para escalamento? Quando começa a escala após o onboarding?"),
        num(6, "Existe valor fixo por semana? As intervenções são registadas e pagas separadamente? Há mínimo por chamada?"),
        num(7, "Após uma intervenção noturna, como ajustam a entrada e o descanso no dia seguinte?"),
        H2("Ponto jurídico prudente"),
        box(
            "",
            "Não existe um subsídio universal fixo para mera disponibilidade remota. Confirma contrato, política interna ou instrumento coletivo. Trabalho efetivamente prestado fora do horário pode enquadrar-se como trabalho suplementar, dependendo das circunstâncias; o descanso diário é normalmente de 11 horas. Isto é orientação geral, não aconselhamento jurídico.",
            PALE_GOLD,
            colors.HexColor("#996B00"),
        ),
        PageBreak(),
    ]

    # Salary
    section_title(s, "17", "Negociação salarial", "Fala sempre em salário-base bruto anual ou mensal × 14; separa benefícios e prevenção.")
    s += [
        table(
            [
                ["Zona", "Valor", "Como usar"],
                ["Âncora", "€23.800 brutos/ano (€1.700 × 14)", "Abertura defensável pelo L1/L2, presencialidade e prevenção; excluir alimentação e on-call."],
                ["Bom objetivo", "€21.000-€22.400 (€1.500-€1.600 × 14)", "Resultado equilibrado se prevenção for paga separadamente e houver bom pacote."],
                ["Piso interno", "€19.600 (€1.400 × 14)", "Não revelar. Só considerar com prevenção separada, evolução e revisão claras."],
                ["Piso pragmático", "€18.200 (€1.300 × 14)", "Apenas se o projeto/formação forem muito fortes e as condições de prevenção forem boas."],
            ],
            [34 * mm, 48 * mm, CONTENT_W - 82 * mm],
        ),
        Spacer(1, 6),
        box(
            "NOTA",
            "Referências públicas para funções júnior de helpdesk/suporte em Portugal apontam frequentemente para cerca de €17k-€22k brutos/ano, mas esta vaga acrescenta L2, presença física e prevenção 24/7. O teu valor pedido deve refletir o âmbito completo.",
            PALE_BLUE,
            BLUE,
        ),
    ]
    s += bilingual(
        "Se perguntarem expectativas",
        "Pelo âmbito de primeira e segunda linha, pela componente presencial e pela participação na prevenção, estou a apontar para cerca de 23 a 24 mil euros brutos anuais de salário-base, excluindo o subsídio de alimentação e a compensação da prevenção. Naturalmente, gostaria de compreender o pacote completo e a forma como a escala é remunerada.",
        "Considering the first- and second-line scope, the on-site component and the on-call rotation, I am targeting a base salary of approximately 23 to 24 thousand euros gross per year, excluding meal allowance and on-call compensation. Naturally, I would like to understand the full package and how the rotation is compensated.",
    )
    s += bilingual(
        "Se apresentarem um valor baixo",
        "Obrigado por partilhar a proposta. Pelo âmbito de primeira e segunda linha e pela responsabilidade da prevenção, o valor fica abaixo da minha expectativa inicial. Existe flexibilidade no salário-base? E a prevenção e as intervenções são remuneradas separadamente? Se o orçamento inicial for fixo, podemos definir por escrito uma revisão ao fim de seis meses com objetivos concretos?",
        "Thank you for sharing the proposal. Considering the first- and second-line scope and the on-call responsibility, the amount is below my initial expectation. Is there flexibility in the base salary, and are standby and actual interventions paid separately? If the initial budget is fixed, could we define a written six-month salary review based on specific objectives?",
    )
    s += [
        H2("Se te obrigarem a propor a compensação da prevenção"),
        P("Podes usar <b>€250 brutos por semana de escala + todas as intervenções registadas e pagas separadamente</b> como abertura negocial, ajustando ao tempo de resposta, volume e deslocações. Não o apresentes como direito legal nem como referência de mercado robusta; pergunta primeiro qual é a política existente."),
        PageBreak(),
    ]

    # Questions
    section_title(s, "18", "Perguntas inteligentes para fazer", "Escolhe 5-7; não transformes o final num interrogatório.")
    s += [
        H2("Função, cliente e equipa"),
        bullet("Podem explicar o setor, localização e dimensão do cliente ao qual a função ficará alocada?"),
        bullet("Como se distribui o trabalho entre primeira e segunda linha, e onde começa o escalamento para L3?"),
        bullet("Quantos utilizadores e localizações são suportados? Quais são os canais e o volume médio de tickets?"),
        bullet("Quais são as ferramentas de ticketing, gestão remota, inventário e Microsoft usadas no serviço?"),
        bullet("Quem define prioridades no dia a dia e como é feito o acompanhamento pela Konica Minolta?"),
        H2("Onboarding e sucesso"),
        bullet("Existe formação inicial e período de shadowing antes de assumir tickets e prevenção?"),
        bullet("Qual é o nível de autonomia esperado nos primeiros três meses?"),
        bullet("Quais são os incidentes mais frequentes e os SLAs/KPIs mais importantes?"),
        bullet("O que significaria ter sucesso nesta função ao fim de seis meses?"),
        H2("Prevenção e condições"),
        bullet("Como funciona concretamente a semana de prevenção, o escalamento, o volume e a compensação?"),
        bullet("As intervenções, noites, fins de semana e feriados ficam registados e pagos separadamente?"),
        bullet("Qual é o intervalo salarial e o pacote de benefícios definido para a posição?"),
        H2("As cinco que não podem faltar"),
        box(
            "",
            "1) cliente/setor/local; 2) divisão L1/L2 e escalamento; 3) ferramentas e incidentes; 4) onboarding/sucesso aos 6 meses; 5) regras e compensação da prevenção.",
            PALE_GREEN,
            TEAL,
        ),
        PageBreak(),
    ]

    # Acronyms
    section_title(s, "19", "Acrónimos e conceitos de revisão", "Consegue explicar cada termo numa frase simples.")
    s += [
        table(
            [
                ["Sigla", "Significado", "Aplicação"],
                ["L1 / L2 / L3", "Níveis de suporte", "Triagem/resolução comum -> análise aprofundada -> especialista/fabricante."],
                ["ITSM", "IT Service Management", "Processos e ferramentas para incidentes, pedidos, mudanças, ativos e conhecimento."],
                ["SLA", "Service Level Agreement", "Tempos e níveis de resposta/resolução acordados."],
                ["KB", "Knowledge Base", "Artigos reutilizáveis de diagnóstico e resolução."],
                ["RCA", "Root Cause Analysis", "Análise da causa de um incidente para prevenir recorrência."],
                ["KPI", "Key Performance Indicator", "Métrica como SLA cumprido, tempo de resposta ou resolução."],
                ["AD", "Active Directory", "Diretório on-premises de identidades, computadores, grupos e políticas."],
                ["Entra ID", "Microsoft cloud identity", "Identidade e acesso cloud; antigo Azure AD."],
                ["GPO", "Group Policy Object", "Configurações aplicadas a utilizadores/computadores num domínio."],
                ["MFA", "Multi-Factor Authentication", "Autenticação com mais de um tipo de fator."],
                ["MDM / MAM", "Device / App Management", "Gestão de dispositivos e de aplicações/dados."],
                ["TCP/IP", "Protocol suite", "Base da comunicação em rede."],
                ["DNS", "Domain Name System", "Nomes para IP."],
                ["DHCP", "Dynamic Host Configuration Protocol", "Entrega IP, máscara, gateway e DNS."],
                ["VPN", "Virtual Private Network", "Túnel protegido para acesso remoto."],
                ["APIPA", "Automatic Private IP Addressing", "169.254.x.x quando DHCP falha."],
                ["P1-P4", "Prioridades", "Impacto e urgência, não apenas ordem de chegada."],
            ],
            [27 * mm, 57 * mm, CONTENT_W - 84 * mm],
        ),
        PageBreak(),
    ]

    # Closing and checklist
    section_title(s, "20", "Fecho da entrevista e checklist", "Termina com interesse concreto, não apenas «obrigado».")
    s += bilingual(
        "Fecho recomendado",
        "Obrigado por explicarem melhor a função e o contexto do cliente. A conversa reforçou o meu interesse porque a posição combina suporte a utilizadores, Windows, Microsoft 365, Active Directory, redes e melhoria de processos. Acredito que a minha experiência prática, método de diagnóstico e capacidade de aprendizagem me permitiriam contribuir e evoluir com a equipa. Há algum ponto do meu perfil sobre o qual gostariam que eu esclarecesse ou aprofundasse antes de terminarmos?",
        "Thank you for explaining the role and client environment in more detail. The conversation has strengthened my interest because the position combines user support, Windows, Microsoft 365, Active Directory, networking and process improvement. I believe my hands-on experience, troubleshooting method and learning ability would allow me to contribute and grow with the team. Is there any aspect of my profile that you would like me to clarify or expand on before we finish?",
    )
    s += [
        H2("Na véspera"),
        bullet("Escolher e completar três histórias STAR reais."),
        bullet("Treinar apresentação de 90 s e 30 s em português e inglês."),
        bullet("Rever método universal, Outlook, AD, 169.254, MFA e ticket/SLA."),
        bullet("Definir âncora salarial, objetivo e piso privado."),
        bullet("Escrever cinco perguntas prioritárias."),
        H2("30 minutos antes"),
        bullet("CV, anúncio e este guião abertos; bloco e caneta."),
        bullet("Câmara, microfone, ligação e nome de apresentação testados."),
        bullet("Água, local silencioso, notificações desligadas e telemóvel em silêncio."),
        bullet("Entrar 8-10 minutos antes."),
        H2("Durante"),
        bullet("Ouvir até ao fim; pedir clarificação se a pergunta for ambígua."),
        bullet("Responder primeiro à pergunta e depois dar contexto; evitar monólogos."),
        bullet("Não inventar experiência, números, incidentes ou ferramentas."),
        bullet("Anotar cliente, equipa, ferramentas, prevenção, remuneração e próximos passos."),
        H2("Mensagem final para ti"),
        box(
            "",
            "Não precisas de parecer sénior. Precisas de mostrar que já sabes apoiar, pensar, comunicar e aprender com responsabilidade. A melhor versão da tua candidatura é técnica, honesta e calma.",
            PALE_GREEN,
            TEAL,
        ),
        PageBreak(),
    ]

    # Sources
    section_title(s, "21", "Fontes e notas", "Consultadas para contextualizar empresa, salário e prevenção. A decisão final depende da proposta contratual.")
    sources = [
        ("Konica Minolta Portugal - página principal e áreas de negócio", "https://www.konicaminolta.pt/pt-pt"),
        ("Sobre a Konica Minolta", "https://www.konicaminolta.pt/pt-pt/informacoes-corporativas/sobre-a-konica-minolta"),
        ("Managed IT Services", "https://www.konicaminolta.pt/pt-pt/solucoes-de-it/managed-services"),
        ("Business Process Outsourcing", "https://www.konicaminolta.pt/pt-pt/solucoes-de-it/business-process-outsourcing"),
        ("Gestão de IT, NOC/SOC e suporte", "https://www.konicaminolta.pt/pt-pt/verticais/it"),
        ("Carreiras e desenvolvimento", "https://www.konicaminolta.pt/pt-pt/informacoes-corporativas/carreiras"),
        ("Valores e código de ética", "https://www.konicaminolta.pt/pt-pt/informacoes-corporativas/codigo-de-etica-e-conduta-empresarial"),
        ("Adecco Portugal Salary Guide 2026", "https://www.adecco.com/pt-pt/-/media/project/adecco/adeccopt/pdfs/guia-salarial-2026-en.pdf"),
        ("Adecco SSC Salary Guide 2026", "https://www.adecco.com/pt-pt/-/media/project/adecco/adeccopt/pdfs/guiasalarialssc_2026.pdf"),
        ("Landing.Jobs Tech Talent Trends 2025", "https://campaign.landing.jobs/hubfs/Tech%20Talent%20Trends%20Report%202025.pdf?hsLang=en"),
        ("Código do Trabalho consolidado", "https://diariodarepublica.pt/dr/legislacao-consolidada/lei/2009-34546475"),
    ]
    for i, (name, url) in enumerate(sources, 1):
        s.append(P(f"<b>{i}. {esc(name)}</b><br/><link href='{url}' color='#2878C8'>{url}</link>", "GuideSmall"))
        s.append(Spacer(1, 3))
    s += [
        Spacer(1, 5),
        HRFlowable(width="100%", thickness=0.6, color=RULE),
        Spacer(1, 5),
        P(
            "Este documento foi preparado a partir do anúncio fornecido, da carta de apresentação e do currículo de Miguel Magalhães. Os exemplos assinalados como histórias pessoais devem ser completados apenas com factos que o candidato consiga sustentar.",
            "GuideSmall",
        ),
    ]
    return s


def build():
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = GuideDocTemplate(str(OUTPUT))
    doc.build(make_story())
    print(OUTPUT.resolve())


if __name__ == "__main__":
    build()
