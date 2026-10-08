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
OUTPUT = ROOT / "output" / "pdf" / "Carta_Motivacao_OMD_Tecnico_Informatica_Miguel_Magalhaes.pdf"

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
    canvas.drawRightString(width - 20 * mm, 11.5 * mm, "Candidatura - OMD - Técnico de Informática")
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
        title="Carta de Motivação - Técnico de Informática | Ordem dos Médicos Dentistas",
        author="Miguel Magalhães",
        subject="OMD - Técnico de Informática",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="letter", frames=[frame], onPage=draw_page)])

    styles = getSampleStyleSheet()
    name = ParagraphStyle("Name", parent=styles["Normal"], fontName="Arial-Bold", fontSize=20, leading=23, textColor=NAVY, spaceAfter=2)
    role = ParagraphStyle("Role", parent=styles["Normal"], fontName="Arial", fontSize=9.2, leading=12, textColor=MUTED)
    small = ParagraphStyle("Small", parent=styles["Normal"], fontName="Arial", fontSize=8.4, leading=11.5, textColor=TEXT)
    date_style = ParagraphStyle("Date", parent=small, alignment=TA_LEFT, textColor=MUTED)
    subject = ParagraphStyle("Subject", parent=styles["Normal"], fontName="Arial-Bold", fontSize=10.4, leading=13, textColor=NAVY, spaceAfter=7)
    body = ParagraphStyle("Body", parent=styles["Normal"], fontName="Arial", fontSize=9.35, leading=13.8, textColor=TEXT, alignment=TA_LEFT, spaceAfter=7.4)
    body_bold = ParagraphStyle("BodyBold", parent=body, fontName="Arial-Bold")

    story = []
    header = Table(
        [
            [Paragraph("Miguel Magalhães", name), Paragraph("Porto, 25 de setembro de 2026", date_style)],
            [Paragraph("Engenharia Informática · Suporte IT · Automação e Cibersegurança", role), ""],
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
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph("À Ordem dos Médicos Dentistas", body_bold))
    story.append(Paragraph("<b>Assunto:</b> OMD - Técnico de Informática", subject))
    story.append(Paragraph("Exmos. Senhores,", body))

    paragraphs = [
        "É com grande motivação que apresento a minha candidatura à posição de <b>Técnico de Informática</b> da Ordem dos Médicos Dentistas. Identifico-me particularmente com uma função que alia suporte próximo aos utilizadores, continuidade operacional, adoção de ferramentas digitais e melhoria de processos, num contexto institucional onde a qualidade do serviço, a ética e a proteção da informação assumem especial importância.",
        "Sou licenciado em <b>Engenharia Informática</b>, possuo um CTeSP em Redes e Sistemas Informáticos e frequento atualmente, em regime pós-laboral, o Mestrado em Cibersegurança e Auditoria de Sistemas Informáticos. Esta formação proporciona-me uma visão integrada de suporte, sistemas, redes, cloud, segurança e desenvolvimento, permitindo-me abordar incidentes e necessidades organizacionais de forma estruturada e responsável.",
        "Na NewCoffee, prestei suporte técnico a diferentes departamentos e localizações, presencialmente e à distância. Resolvi incidentes relacionados com equipamentos Windows, contas e permissões, Active Directory, VPN, DHCP, conectividade, impressoras, Microsoft 365 e aplicações empresariais. Apoiei os utilizadores na adoção e utilização das ferramentas, documentei intervenções e articulei a resolução de situações mais complexas com fornecedores externos, mantendo sempre uma comunicação clara e orientada para o serviço.",
        "Desenvolvi também uma plataforma interna de <b>ITSM</b> para gerir tickets, ativos, utilizadores e indicadores operacionais. Este projeto envolveu levantamento de requisitos, análise de processos, desenvolvimento web, base de dados e criação de mecanismos de acompanhamento. Reforçou a minha capacidade de identificar constrangimentos, propor soluções digitais ajustadas e colaborar nos testes e implementação de novas aplicações, integrações e fluxos internos.",
        "Tenho vindo a aprofundar a aplicação prática de <b>Inteligência Artificial e automação</b> no apoio à documentação, pesquisa, organização da informação e otimização de tarefas repetitivas. Procuro fazê-lo de forma responsável, validando resultados e respeitando os princípios de confidencialidade, minimização de dados e segurança. Possuo experiência no ecossistema Microsoft e facilidade em aprender novas plataformas, o que me permitirá evoluir rapidamente em ferramentas como Google Workspace, Microsoft Dynamics e soluções de suporte remoto.",
        "Considero que posso contribuir como facilitador digital, criando manuais simples, orientando utilizadores e aproximando as necessidades das diferentes áreas das soluções tecnológicas disponíveis. Sou organizado, autónomo, proativo e comunicativo, valorizando o planeamento, a colaboração e o compromisso com a missão da organização.",
        "A possibilidade de contribuir para a evolução tecnológica da Ordem dos Médicos Dentistas representa para mim um desafio profissional com significado e impacto. Agradeço a consideração da minha candidatura e coloco-me à disposição para uma entrevista.",
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
