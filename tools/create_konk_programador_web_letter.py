from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, KeepTogether, PageTemplate, Paragraph, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Carta_Apresentacao_Konk_Consulting_Programador_Web_Miguel_Magalhaes.pdf"

NAVY = colors.HexColor("#173B62")
BLUE = colors.HexColor("#2E6DA4")
TEXT = colors.HexColor("#252A30")
MUTED = colors.HexColor("#5F6872")
LIGHT = colors.HexColor("#E7EEF5")


def register_fonts():
    pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))


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
    canvas.drawRightString(width - 20 * mm, 11.5 * mm, "Candidatura - Programador Web")
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
        title="Carta de Apresentação - Programador Web | konkconsulting",
        author="Miguel Magalhães",
        subject="Candidatura à posição de Programador Web",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="letter", frames=[frame], onPage=draw_page)])

    styles = getSampleStyleSheet()
    name = ParagraphStyle("Name", parent=styles["Normal"], fontName="Arial-Bold", fontSize=20, leading=23, textColor=NAVY, spaceAfter=2)
    role = ParagraphStyle("Role", parent=styles["Normal"], fontName="Arial", fontSize=9.2, leading=12, textColor=MUTED)
    small = ParagraphStyle("Small", parent=styles["Normal"], fontName="Arial", fontSize=8.4, leading=11.5, textColor=TEXT)
    date_style = ParagraphStyle("Date", parent=small, alignment=TA_LEFT, textColor=MUTED)
    subject = ParagraphStyle("Subject", parent=styles["Normal"], fontName="Arial-Bold", fontSize=10.4, leading=13, textColor=NAVY, spaceAfter=7)
    body = ParagraphStyle("Body", parent=styles["Normal"], fontName="Arial", fontSize=9.55, leading=14.2, textColor=TEXT, alignment=TA_LEFT, spaceAfter=8)
    body_bold = ParagraphStyle("BodyBold", parent=body, fontName="Arial-Bold")

    story = []
    header = Table(
        [
            [Paragraph("Miguel Magalhães", name), Paragraph("Porto, 25 de setembro de 2026", date_style)],
            [Paragraph("Engenharia Informática · Desenvolvimento Web · APIs e Bases de Dados", role), ""],
        ],
        colWidths=[112 * mm, 52 * mm],
    )
    header.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
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
    contact.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F7FA")),
        ("BOX", (0, 0), (-1, -1), 0.5, LIGHT),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(contact)
    story.append(Spacer(1, 5 * mm))

    story.append(Paragraph("À Equipa de Recrutamento da konkconsulting", body_bold))
    story.append(Paragraph("<b>Assunto:</b> Candidatura à posição de Programador Web", subject))
    story.append(Paragraph("Exmos. Senhores,", body))

    paragraphs = [
        "Venho apresentar a minha candidatura à posição de <b>Programador Web</b>. A oportunidade de participar no desenvolvimento de aplicações orientadas a serviços, colaborar na definição de arquiteturas e integrar projetos internacionais inovadores corresponde às áreas técnicas em que tenho vindo a construir o meu percurso e nas quais pretendo continuar a evoluir.",
        "Sou licenciado em <b>Engenharia Informática</b>, possuo um CTeSP em Redes e Sistemas Informáticos e frequento atualmente, em regime pós-laboral, o Mestrado em Cibersegurança e Auditoria de Sistemas Informáticos. Ao longo da minha formação e dos projetos desenvolvidos, adquiri experiência com JavaScript e TypeScript, React e Next.js, Node.js, C# e .NET, Java, SQL, Git e desenvolvimento de aplicações web com componentes frontend, backend e bases de dados relacionais.",
        "Entre os projetos que melhor demonstram a minha adequação à função está o desenvolvimento de uma plataforma interna de <b>ITSM</b> para gestão de tickets, ativos, utilizadores e indicadores operacionais. Participei na análise de requisitos, estruturação da solução, modelação da base de dados, implementação da interface e da lógica de backend, controlo de acessos e integração das funcionalidades. Esta experiência reforçou a minha capacidade de transformar necessidades do negócio em soluções web organizadas, funcionais e sustentáveis.",
        "Tenho conhecimentos de desenvolvimento e integração de <b>APIs REST</b>, desenho e utilização de bases de dados SQL, nomeadamente MySQL e PostgreSQL, e utilização de Docker para criação de ambientes consistentes. Estou familiarizado com os princípios de CI/CD, controlo de versões, revisão de código, pipelines de build e release e metodologias Agile/Scrum. Embora a minha experiência principal em SPA esteja associada a React, os conceitos de componentização, gestão de estado, consumo de APIs e separação de responsabilidades permitem-me adaptar rapidamente esses conhecimentos a Angular.",
        "O meu percurso profissional em suporte IT e aplicações empresariais desenvolveu igualmente a minha capacidade analítica, orientação para o utilizador e compreensão dos processos de negócio. Estou habituado a diagnosticar problemas, documentar soluções, organizar prioridades e colaborar com diferentes interlocutores. Possuo inglês de nível B2 e experiência de colaboração em contexto internacional, sentindo-me motivado para integrar uma equipa dinâmica e tecnologicamente exigente.",
        "Acredito que a combinação entre formação técnica, experiência prática em desenvolvimento e vontade contínua de aprender me permitirá contribuir para os projetos da konkconsulting e crescer de forma consistente nas tecnologias utilizadas pela equipa.",
        "Agradeço a consideração da minha candidatura e coloco-me à disposição para uma entrevista, na qual terei todo o gosto em aprofundar a minha experiência, motivação e adequação à função.",
    ]
    for paragraph in paragraphs:
        story.append(Paragraph(paragraph, body))

    story.append(KeepTogether([
        Spacer(1, 1.5 * mm),
        Paragraph("Com os melhores cumprimentos,", body),
        Paragraph("<b>Miguel Magalhães</b>", body),
    ]))

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
