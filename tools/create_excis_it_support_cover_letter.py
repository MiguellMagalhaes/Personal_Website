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
OUTPUT = (
    ROOT
    / "output"
    / "pdf"
    / "Carta_Apresentacao_Excis_Especialista_Suporte_IT_L2_Miguel_Magalhaes.pdf"
)

NAVY = colors.HexColor("#173B62")
BLUE = colors.HexColor("#2E6DA4")
TEXT = colors.HexColor("#252A30")
MUTED = colors.HexColor("#5F6872")
LIGHT = colors.HexColor("#E7EEF5")


def register_fonts():
    pdfmetrics.registerFont(
        TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf")
    )
    pdfmetrics.registerFont(
        TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf")
    )


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
    canvas.drawRightString(
        width - 20 * mm,
        11.5 * mm,
        "Candidatura - Especialista de Suporte IT (L2)",
    )
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
        title="Carta de Apresentação - Especialista de Suporte IT (L2) | Excis Compliance",
        author="Miguel Magalhães",
        subject="Candidatura à posição de Especialista de Suporte IT (L2)",
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
        "Date", parent=small, alignment=TA_LEFT, textColor=MUTED
    )
    subject = ParagraphStyle(
        "Subject",
        parent=styles["Normal"],
        fontName="Arial-Bold",
        fontSize=10.4,
        leading=13,
        textColor=NAVY,
        spaceAfter=7,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Arial",
        fontSize=9.1,
        leading=13.2,
        textColor=TEXT,
        alignment=TA_LEFT,
        spaceAfter=6.6,
    )
    body_bold = ParagraphStyle("BodyBold", parent=body, fontName="Arial-Bold")

    story = []
    header = Table(
        [
            [
                Paragraph("Miguel Magalhães", name),
                Paragraph("Porto, 27 de setembro de 2026", date_style),
            ],
            [
                Paragraph(
                    "Engenharia Informática · Suporte IT · Sistemas e Redes", role
                ),
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
        [
            [
                Paragraph("<b>Telefone</b><br/>(+351) 918 860 342", small),
                Paragraph(
                    "<b>Email</b><br/><link href='mailto:miguel.softeng@gmail.com' "
                    "color='#2E6DA4'>miguel.softeng@gmail.com</link>",
                    small,
                ),
                Paragraph(
                    "<b>Website</b><br/><link "
                    "href='https://miguelangelodiasmagalhaes.online' "
                    "color='#2E6DA4'>miguelangelodiasmagalhaes.online</link>",
                    small,
                ),
            ]
        ],
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
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph("À Equipa de Recrutamento da Excis Compliance", body_bold))
    story.append(
        Paragraph(
            "<b>Assunto:</b> Candidatura à posição de Especialista de Suporte IT "
            "(L2) - Desktop &amp; Client Services",
            subject,
        )
    )
    story.append(Paragraph("Exmos. Senhores,", body))

    paragraphs = [
        "É com grande interesse que apresento a minha candidatura à posição de <b>Especialista de Suporte IT (L2)</b> na Excis Compliance. A oportunidade de prestar suporte tecnológico a um cliente global do setor automóvel, num contexto internacional e orientado por níveis de serviço, está diretamente alinhada com a experiência que tenho vindo a desenvolver em suporte técnico, sistemas e redes.",
        "Sou licenciado em <b>Engenharia Informática</b>, possuo um CTeSP em Redes e Sistemas Informáticos e frequento atualmente, em regime pós-laboral, o Mestrado em Cibersegurança e Auditoria de Sistemas Informáticos. O meu percurso deu-me bases sólidas em plataformas Windows, Microsoft Office, hardware, redes TCP/IP, DNS, DHCP, segurança e diagnóstico estruturado de incidentes.",
        "Na Direção de Sistemas de Informação da NewCoffee, prestei suporte técnico a utilizadores de diferentes departamentos e instalações, presencialmente e à distância. Resolvi pedidos relacionados com equipamentos Windows, aplicações empresariais, Microsoft Office, contas e permissões, Active Directory, conectividade, VPN, DHCP, impressão e periféricos. Colaborei também com fornecedores externos no tratamento de situações mais complexas, reunindo evidências, acompanhando o incidente e validando a solução com o utilizador.",
        "Desenvolvi ainda uma plataforma interna de <b>ITSM</b> para a gestão de tickets, ativos, utilizadores e indicadores operacionais. Este projeto reforçou a minha compreensão do ciclo de vida dos incidentes, da definição de prioridades, da documentação técnica, do cumprimento de SLAs e da importância de manter uma base de conhecimento clara e reutilizável.",
        "Trabalho de forma metódica: começo por compreender o impacto e o âmbito do problema, recolho informação, testo hipóteses progressivamente e documento as ações realizadas. Quando uma situação ultrapassa a minha autonomia, escalo-a com contexto técnico suficiente para acelerar a resolução. Tenho também facilidade em comunicar com utilizadores sem conhecimentos técnicos, mantendo uma postura profissional, tranquila e orientada para o serviço.",
        "Tenho domínio nativo da língua portuguesa e capacidade de comunicação em inglês de nível B2, sentindo-me confortável para colaborar num ambiente internacional e realizar a entrevista técnica em inglês. Acredito que a minha experiência prática, capacidade de aprendizagem, atenção ao detalhe e sentido de responsabilidade me permitirão contribuir positivamente para a equipa da Excis e continuar a evoluir no suporte L2.",
        "Agradeço a consideração da minha candidatura e coloco-me à disposição para uma entrevista, na qual terei todo o gosto em aprofundar a minha experiência, motivação e adequação à função.",
    ]
    for paragraph in paragraphs:
        story.append(Paragraph(paragraph, body))

    story.append(
        KeepTogether(
            [
                Spacer(1, 1.5 * mm),
                Paragraph("Com os melhores cumprimentos,", body),
                Paragraph("<b>Miguel Magalhães</b>", body),
            ]
        )
    )

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
