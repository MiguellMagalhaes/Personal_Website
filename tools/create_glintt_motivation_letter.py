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
OUTPUT = ROOT / "output" / "pdf" / "Carta_Motivacao_Glintt_Global_Tecnico_Suporte_Informatico_Miguel_Magalhaes.pdf"

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
    canvas.drawRightString(width - 20 * mm, 11.5 * mm, "Candidatura - Técnico de Suporte Informático")
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
        title="Carta de Motivação - Técnico de Suporte Informático | Glintt Global",
        author="Miguel Magalhães",
        subject="Candidatura à posição de Técnico de Suporte Informático",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="letter", frames=[frame], onPage=draw_page)])

    styles = getSampleStyleSheet()
    name = ParagraphStyle("Name", parent=styles["Normal"], fontName="Arial-Bold", fontSize=20, leading=23, textColor=NAVY, spaceAfter=2)
    role = ParagraphStyle("Role", parent=styles["Normal"], fontName="Arial", fontSize=9.2, leading=12, textColor=MUTED)
    small = ParagraphStyle("Small", parent=styles["Normal"], fontName="Arial", fontSize=8.4, leading=11.5, textColor=TEXT)
    date_style = ParagraphStyle("Date", parent=small, alignment=TA_LEFT, textColor=MUTED)
    subject = ParagraphStyle("Subject", parent=styles["Normal"], fontName="Arial-Bold", fontSize=10.4, leading=13, textColor=NAVY, spaceAfter=7)
    body = ParagraphStyle("Body", parent=styles["Normal"], fontName="Arial", fontSize=9.3, leading=13.65, textColor=TEXT, alignment=TA_LEFT, spaceAfter=7.2)
    body_bold = ParagraphStyle("BodyBold", parent=body, fontName="Arial-Bold")

    story = []
    header = Table(
        [
            [Paragraph("Miguel Magalhães", name), Paragraph("Porto, 25 de setembro de 2026", date_style)],
            [Paragraph("Engenharia Informática · Suporte IT · Sistemas e Redes", role), ""],
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

    story.append(Paragraph("À Equipa de Recrutamento da Glintt Global", body_bold))
    story.append(Paragraph("<b>Assunto:</b> Candidatura à posição de Técnico de Suporte Informático - Porto", subject))
    story.append(Paragraph("Exmos. Senhores,", body))

    paragraphs = [
        "É com grande motivação que apresento a minha candidatura à posição de <b>Técnico de Suporte Informático</b> na Glintt Global. A possibilidade de integrar uma equipa que assegura a continuidade das operações tecnológicas das farmácias e contribui para a proteção dos seus ativos digitais desperta-me particular interesse, por combinar suporte técnico, resolução de problemas e tecnologia aplicada a um setor com impacto direto na qualidade de vida das pessoas.",
        "Sou licenciado em <b>Engenharia Informática</b>, possuo um CTeSP em Redes e Sistemas Informáticos e frequento atualmente, em regime pós-laboral, o Mestrado em Cibersegurança e Auditoria de Sistemas Informáticos. O meu percurso proporcionou-me bases sólidas em suporte a utilizadores, plataformas Windows, redes TCP/IP, hardware, bases de dados, segurança e diagnóstico estruturado de incidentes.",
        "Na NewCoffee, prestei suporte técnico a diferentes departamentos e localizações, presencialmente e à distância. Resolvi incidentes relacionados com equipamentos Windows, conectividade, VPN, DHCP, contas e permissões, Active Directory, impressoras, Microsoft 365 e aplicações empresariais. Trabalhei também com o <b>ERP PHC</b>, apoiando utilizadores em processos operacionais e de faturação, analisando dificuldades reportadas e articulando a resolução de situações mais complexas com fornecedores externos. Esta experiência ensinou-me a comunicar com clareza, gerir prioridades e acompanhar cada pedido até à sua resolução.",
        "Desenvolvi ainda uma plataforma interna de <b>ITSM</b> para o registo e acompanhamento de tickets, ativos, utilizadores e indicadores operacionais. Este projeto reforçou a minha compreensão do ciclo de vida dos incidentes, da documentação técnica, do cumprimento de níveis de serviço e da identificação de problemas recorrentes. A minha formação em desenvolvimento de software e bases de dados permite-me também comunicar eficazmente com equipas de desenvolvimento, reunir evidências técnicas e contribuir para a análise da causa dos problemas.",
        "Embora ainda não tenha trabalhado diretamente com software farmacêutico, estou habituado a aprender aplicações empresariais e a traduzir questões técnicas em orientações simples para os utilizadores. Sinto-me motivado para conhecer os fluxos específicos de agendamentos, registos clínicos, faturação e prescrições eletrónicas, bem como para apoiar ações de formação. Identifico-me com uma função que exige espírito analítico, organização, colaboração e sentido de responsabilidade perante serviços essenciais.",
        "A reputação e a experiência da Glintt Global em tecnologia e saúde tornam esta oportunidade especialmente relevante para o meu desenvolvimento profissional. Acredito que a minha experiência prática em suporte, a capacidade de aprendizagem e a orientação para o utilizador me permitirão contribuir positivamente para a equipa Customer Support & IT Equipment.",
        "Agradeço a consideração da minha candidatura e coloco-me à disposição para uma entrevista, na qual terei todo o gosto em aprofundar a minha motivação e adequação à função.",
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
