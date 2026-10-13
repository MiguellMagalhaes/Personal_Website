from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUT = Path(
    "/Users/miguelmagalhaes/Documents/GitHub/Personal_Website/output/pdf/"
    "Carta_Apresentacao_Cleva_Solutions_Technical_Support_Miguel_Magalhaes.pdf"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor("#14324A")
TEAL = colors.HexColor("#0E8E91")
TEXT = colors.HexColor("#26343F")
MID = colors.HexColor("#667580")
LINE = colors.HexColor("#CFDCE2")
PALE = colors.HexColor("#EEF6F6")

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="NameX", fontName="Arial-Bold", fontSize=22, leading=25, textColor=NAVY, spaceAfter=2*mm))
styles.add(ParagraphStyle(name="RoleX", fontName="Arial", fontSize=10.5, leading=14, textColor=TEAL, spaceAfter=4*mm))
styles.add(ParagraphStyle(name="ContactX", fontName="Arial", fontSize=8.6, leading=11.5, textColor=MID))
styles.add(ParagraphStyle(name="DateX", fontName="Arial", fontSize=9, leading=11.5, textColor=MID, alignment=TA_RIGHT, spaceAfter=5*mm))
styles.add(ParagraphStyle(name="BodyX", fontName="Arial", fontSize=9.2, leading=13.1, textColor=TEXT, spaceAfter=2.8*mm))
styles.add(ParagraphStyle(name="SubjectX", fontName="Arial-Bold", fontSize=10.2, leading=13.5, textColor=NAVY, spaceAfter=4.5*mm))


def P(text, style="BodyX"):
    return Paragraph(text, styles[style])


def decorate(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, height - 10*mm, width, 10*mm, fill=1, stroke=0)
    canvas.setFillColor(TEAL)
    canvas.rect(0, height - 12*mm, width, 2*mm, fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.line(20*mm, 17*mm, width - 20*mm, 17*mm)
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MID)
    canvas.drawString(20*mm, 11.5*mm, "Miguel Magalhães | Candidatura a Technical Support")
    canvas.drawRightString(width - 20*mm, 11.5*mm, "Porto, Portugal")
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(OUT),
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=21*mm,
    bottomMargin=21*mm,
    title="Carta de Apresentação - Cleva Solutions - Technical Support",
    author="Miguel Magalhães",
    subject="Candidatura a Technical Support",
)

story = [
    P("Miguel Magalhães", "NameX"),
    P("Técnico de Suporte Informático e Aplicacional", "RoleX"),
]

contact = Table(
    [
        [P("Porto, Portugal", "ContactX"), P("(+351) 918 860 342", "ContactX")],
        [P("miguel.softeng@gmail.com", "ContactX"), P("miguelangelodiasmagalhaes.online", "ContactX")],
    ],
    colWidths=[83*mm, 83*mm],
)
contact.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), PALE),
            ("BOX", (0, 0), (-1, -1), 0.6, LINE),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE),
            ("LEFTPADDING", (0, 0), (-1, -1), 3*mm),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3*mm),
            ("TOPPADDING", (0, 0), (-1, -1), 2.2*mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2*mm),
        ]
    )
)

story += [
    contact,
    Spacer(1, 4*mm),
    P("11 de outubro de 2026", "DateX"),
    P("Equipa de Recrutamento<br/>Cleva Solutions<br/>Porto, Portugal", "BodyX"),
    Spacer(1, 0.5*mm),
    P("Candidatura - Technical Support", "SubjectX"),
    P("Exmos. Senhores,"),
    P(
        "Venho apresentar a minha candidatura à oportunidade de <b>Technical Support</b> na Cleva Solutions. "
        "Sou licenciado em Engenharia Informática, frequento atualmente um mestrado em Cibersegurança e possuo "
        "experiência prática em suporte técnico, diagnóstico de incidentes, instalação e configuração de software, "
        "gestão de contas e acessos e apoio a utilizadores de diferentes departamentos e localizações."
    ),
    P(
        "Na NewCoffee, prestei suporte de primeira linha a centenas de utilizadores distribuídos por cinco instalações, "
        "tratando diariamente pedidos relacionados com hardware, software, Windows, Active Directory, Microsoft 365, "
        "VPN, conectividade, impressão e aplicações empresariais. Registava e acompanhava os incidentes, comunicava o "
        "respetivo estado aos utilizadores e encaminhava os casos mais complexos para as equipas ou fornecedores "
        "responsáveis, incluindo a informação técnica necessária para facilitar a análise e a resolução."
    ),
    P(
        "A minha experiência inclui também a instalação, configuração e validação de aplicações, o acompanhamento de "
        "sistemas ERP e ferramentas internas, a manutenção de registos de equipamentos e utilizadores e a elaboração de "
        "documentação técnica. Participei ainda no desenvolvimento e manutenção de uma plataforma interna de ITSM e "
        "gestão de ativos, trabalhando com Microsoft SQL Server e tecnologias web. Esta experiência permitiu-me consolidar "
        "conhecimentos de SQL, análise de problemas, integração entre sistemas e melhoria de processos de suporte."
    ),
    P(
        "Embora ainda não tenha experiência profissional direta no setor segurador nem com DB2, tenho facilidade de "
        "aprendizagem e interesse em compreender os processos, produtos e módulos aplicacionais utilizados pela Cleva "
        "Solutions. Estou igualmente motivado para aprofundar os meus conhecimentos de ITIL e evoluir no suporte a "
        "aplicações críticas em contexto empresarial."
    ),
    P(
        "Considero que a minha capacidade de análise, sentido de responsabilidade, organização e facilidade de comunicação "
        "poderão contribuir positivamente para a equipa. Tenho particular interesse numa função que combine investigação "
        "técnica, contacto com clientes, documentação de conhecimento e colaboração com diferentes equipas."
    ),
    P(
        "A Cleva Solutions desperta o meu interesse pela sua especialização tecnológica no setor dos seguros, pela solidez "
        "da organização e pela importância atribuída à aprendizagem contínua, à partilha de conhecimento e ao desenvolvimento "
        "dos seus profissionais."
    ),
    P(
        "Agradeço a consideração da minha candidatura e manifesto total disponibilidade para uma entrevista, durante a "
        "qual poderei apresentar com maior detalhe a minha experiência e motivação."
    ),
    Spacer(1, 0),
    P("Com os melhores cumprimentos,<br/><b>Miguel Magalhães</b>"),
]

doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
print(OUT)
