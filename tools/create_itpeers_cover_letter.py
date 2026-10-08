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
OUTPUT = ROOT / "output" / "pdf" / "Carta_Apresentacao_IT_PEERS_Junior_Systems_Administrator_Miguel_Magalhaes.pdf"

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
    canvas.drawRightString(width - 20 * mm, 11.5 * mm, "Candidatura - Junior Systems Administrator | ITS0048")
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
        title="Carta de Apresentação - Junior Systems Administrator | IT PEERS",
        author="Miguel Magalhães",
        subject="Candidatura - Ref. ITS0048",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="letter", frames=[frame], onPage=draw_page)])

    styles = getSampleStyleSheet()
    name = ParagraphStyle("Name", parent=styles["Normal"], fontName="Arial-Bold", fontSize=20, leading=23, textColor=NAVY, spaceAfter=2)
    role = ParagraphStyle("Role", parent=styles["Normal"], fontName="Arial", fontSize=9.2, leading=12, textColor=MUTED)
    small = ParagraphStyle("Small", parent=styles["Normal"], fontName="Arial", fontSize=8.4, leading=11.5, textColor=TEXT)
    date_style = ParagraphStyle("Date", parent=small, alignment=TA_LEFT, textColor=MUTED)
    subject = ParagraphStyle("Subject", parent=styles["Normal"], fontName="Arial-Bold", fontSize=10.4, leading=13, textColor=NAVY, spaceAfter=7)
    body = ParagraphStyle("Body", parent=styles["Normal"], fontName="Arial", fontSize=9.7, leading=14.5, textColor=TEXT, alignment=TA_LEFT, spaceAfter=8.5)
    body_bold = ParagraphStyle("BodyBold", parent=body, fontName="Arial-Bold")

    story = []
    header = Table(
        [
            [Paragraph("Miguel Magalhães", name), Paragraph("Porto, 25 de setembro de 2026", date_style)],
            [Paragraph("Engenharia Informática · Sistemas · Redes e Cibersegurança", role), ""],
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

    story.append(Paragraph("À Equipa de Recrutamento da IT PEERS", body_bold))
    story.append(Paragraph("<b>Assunto:</b> Candidatura a Junior Systems Administrator - Ref. ITS0048", subject))
    story.append(Paragraph("Exmos. Senhores,", body))

    paragraphs = [
        "Venho apresentar a minha candidatura à vertente <b>Junior Systems Administrator</b> da oportunidade identificada pela referência ITS0048. A possibilidade de integrar a equipa responsável pela implementação de soluções e pelo apoio técnico a clientes, participando em projetos cloud e on-premises, corresponde diretamente ao percurso que pretendo consolidar nas áreas de sistemas, redes, virtualização e cibersegurança.",
        "Sou licenciado em <b>Engenharia Informática</b>, possuo um CTeSP em Redes e Sistemas Informáticos e frequento atualmente, em regime pós-laboral, o Mestrado em Cibersegurança e Auditoria de Sistemas Informáticos. Esta formação proporcionou-me bases em administração de sistemas, redes TCP/IP, serviços de infraestrutura, segurança, virtualização e desenvolvimento de soluções, permitindo-me analisar problemas de forma estruturada e compreender a relação entre sistemas, aplicações e necessidades operacionais.",
        "Na NewCoffee, prestei suporte técnico a diferentes departamentos e localizações, intervindo em equipamentos Windows, Active Directory, contas e permissões, VPN, DHCP, conectividade, impressoras, Microsoft 365 e aplicações empresariais. Efetuei diagnóstico e resolução de incidentes, preparação e gestão de equipamentos, documentação das intervenções e articulação com fornecedores externos sempre que era necessária uma escalada técnica. Desenvolvi também uma plataforma interna de ITSM para gerir tickets, ativos, utilizadores e indicadores, reforçando a minha experiência na organização do suporte e na melhoria de processos.",
        "Tenho experiência prática e académica com <b>Linux, máquinas virtuais, linha de comandos, análise de configurações e troubleshooting de redes</b>. Num projeto internacional de cibersegurança, configurei ambientes de rede virtualizados e utilizei Wireshark, tcpdump e Snort para analisar tráfego e validar alertas. Possuo ainda conhecimentos fundamentais de VMware, Docker e serviços cloud AWS e Azure. Embora ainda esteja a desenvolver experiência aprofundada com Red Hat e OpenShift Virtualization, compreendo os princípios subjacentes e estou motivado para evoluir nestas tecnologias através de trabalho prático, documentação e certificação.",
        "Acredito que posso contribuir com uma combinação de fundamentos técnicos sólidos, experiência de suporte, capacidade analítica, comunicação e vontade contínua de aprender. Trabalho de forma organizada e responsável, valorizo a colaboração entre equipas e comunico em inglês em contextos técnicos. A oportunidade de crescer na IT PEERS, apoiando clientes e participando em soluções inovadoras cloud e on-premises, representa para mim um passo especialmente motivador.",
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
