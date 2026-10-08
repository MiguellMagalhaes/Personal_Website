from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Carta_Apresentacao_Yunit_Consultor_IT_Junior_Miguel_Magalhaes.pdf"

NAVY = colors.HexColor("#173B62")
BLUE = colors.HexColor("#2E6DA4")
TEXT = colors.HexColor("#252A30")
MUTED = colors.HexColor("#5F6872")
LIGHT = colors.HexColor("#E7EEF5")


def register_fonts():
    pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Italic", "/System/Library/Fonts/Supplemental/Arial Italic.ttf"))


def draw_page(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, height - 9 * mm, width, 9 * mm, stroke=0, fill=1)
    canvas.setFillColor(BLUE)
    canvas.rect(0, 0, width, 3 * mm, stroke=0, fill=1)
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.7)
    canvas.line(20 * mm, 17 * mm, width - 20 * mm, 17 * mm)
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(20 * mm, 11.5 * mm, "Miguel Magalhães")
    canvas.drawRightString(width - 20 * mm, 11.5 * mm, "Candidatura — Consultor IT Junior")
    canvas.restoreState()


def build_pdf():
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
        topMargin=17 * mm,
        bottomMargin=22 * mm,
        title="Carta de Apresentação — Consultor IT Junior | Yunit Consulting",
        author="Miguel Magalhães",
        subject="Candidatura à posição de Consultor IT Junior",
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="main",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc.addPageTemplates([PageTemplate(id="letter", frames=[frame], onPage=draw_page)])

    styles = getSampleStyleSheet()
    name = ParagraphStyle(
        "Name",
        parent=styles["Normal"],
        fontName="Arial-Bold",
        fontSize=20,
        leading=23,
        textColor=NAVY,
        spaceAfter=2,
    )
    role = ParagraphStyle(
        "Role",
        parent=styles["Normal"],
        fontName="Arial",
        fontSize=9.2,
        leading=12,
        textColor=MUTED,
    )
    small = ParagraphStyle(
        "Small",
        parent=styles["Normal"],
        fontName="Arial",
        fontSize=8.4,
        leading=11.5,
        textColor=TEXT,
    )
    date_style = ParagraphStyle(
        "Date",
        parent=small,
        alignment=TA_LEFT,
        textColor=MUTED,
    )
    subject = ParagraphStyle(
        "Subject",
        parent=styles["Normal"],
        fontName="Arial-Bold",
        fontSize=10.4,
        leading=13,
        textColor=NAVY,
        borderColor=BLUE,
        borderWidth=0,
        borderPadding=(0, 0, 0, 0),
        spaceAfter=7,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Arial",
        fontSize=9.55,
        leading=14.25,
        textColor=TEXT,
        alignment=TA_LEFT,
        spaceAfter=8,
    )
    body_bold = ParagraphStyle(
        "BodyBold",
        parent=body,
        fontName="Arial-Bold",
    )

    story = []
    header = Table(
        [
            [Paragraph("Miguel Magalhães", name), Paragraph("Porto, 25 de setembro de 2026", date_style)],
            [
                Paragraph("Engenharia Informática · Suporte IT · Automação e Transformação Digital", role),
                "",
            ],
        ],
        colWidths=[112 * mm, 52 * mm],
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.append(header)
    story.append(Spacer(1, 4 * mm))

    contact = Table(
        [[
            Paragraph("<b>Telefone</b><br/>(+351) 918 860 342", small),
            Paragraph("<b>Email</b><br/><link href='mailto:miguel.softeng@gmail.com' color='#2E6DA4'>miguel.softeng@gmail.com</link>", small),
            Paragraph("<b>Website</b><br/><link href='https://miguelangelodiasmagalhaes.online' color='#2E6DA4'>miguelangelodiasmagalhaes.online</link>", small),
        ]],
        colWidths=[43 * mm, 58 * mm, 63 * mm],
    )
    contact.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F7FA")),
                ("BOX", (0, 0), (-1, -1), 0.5, LIGHT),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, LIGHT),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(contact)
    story.append(Spacer(1, 5 * mm))

    story.append(Paragraph("À Equipa de Recrutamento da Yunit Consulting", body_bold))
    story.append(Paragraph("<b>Assunto:</b> Candidatura à posição de Consultor IT Junior", subject))
    story.append(Paragraph("Exmos. Senhores,", body))

    paragraphs = [
        "Venho apresentar a minha candidatura à posição de <b>Consultor IT Junior</b>. A oportunidade de participar num projeto que combina gestão de infraestrutura, suporte às várias unidades de negócio, transformação digital, automação e Inteligência Artificial desperta-me particular interesse, por reunir áreas nas quais já possuo uma base prática e que pretendo continuar a desenvolver num contexto orientado à criação de valor para o negócio.",
        "Sou licenciado em <b>Engenharia Informática</b>, possuo um CTeSP em Redes e Sistemas Informáticos e frequento atualmente, em regime pós-laboral, o Mestrado em Cibersegurança e Auditoria de Sistemas Informáticos. Na NewCoffee, prestei suporte técnico a diferentes departamentos e localizações, intervindo em equipamentos Windows, Microsoft 365, contas e permissões, Active Directory, conectividade, VPN, impressoras e aplicações empresariais. Trabalhei também com o <b>ERP PHC</b>, apoiando utilizadores, analisando necessidades e contribuindo para a ligação entre os processos operacionais e a vertente tecnológica.",
        "Um dos projetos que melhor demonstra a minha adequação à função foi o desenvolvimento de uma plataforma interna de <b>ITSM</b> para gestão de tickets, ativos, utilizadores e indicadores operacionais. Este trabalho exigiu levantamento de requisitos, análise e estruturação de processos, modelação de dados, desenvolvimento web e backend, integração de funcionalidades e criação de mecanismos de acompanhamento. Permitiu-me consolidar uma abordagem prática à melhoria de processos e à construção de soluções digitais ajustadas às necessidades reais dos utilizadores.",
        "Tenho conhecimentos do ecossistema Microsoft, incluindo Microsoft 365, Teams e SharePoint, bem como experiência com JavaScript/TypeScript, Python, SQL, APIs e Git. Tenho vindo igualmente a aprofundar automação, ferramentas low-code e aplicações de IA ao negócio, estando particularmente motivado para evoluir em <b>Power Automate, Power Apps, workflows, integração entre sistemas e agentes de IA</b>. Valorizo, em especial, a possibilidade de colaborar com equipas técnicas e operacionais, monitorizar a qualidade e segurança dos fluxos implementados e apoiar a evolução contínua do ecossistema tecnológico da Yunit.",
        "Considero que posso contribuir com uma combinação equilibrada de suporte IT, desenvolvimento, capacidade analítica e compreensão dos processos de negócio. Sou organizado, proativo, comunicativo e orientado à resolução de problemas, mantendo uma atitude de aprendizagem contínua e responsabilidade perante os resultados. A possibilidade de crescer numa consultora com uma visão integrada de inovação, melhoria de processos e transformação empresarial representa para mim um desafio especialmente motivador.",
        "Agradeço a consideração da minha candidatura e coloco-me à disposição para uma entrevista, na qual terei todo o gosto em aprofundar a forma como o meu perfil e motivação poderão contribuir para a Yunit Consulting.",
    ]
    for paragraph in paragraphs:
        story.append(Paragraph(paragraph, body))

    closing = KeepTogether(
        [
            Spacer(1, 1.5 * mm),
            Paragraph("Com os melhores cumprimentos,", body),
            Paragraph("<b>Miguel Magalhães</b>", body),
        ]
    )
    story.append(closing)

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
