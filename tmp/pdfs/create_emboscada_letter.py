from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


OUTPUT = Path("output/pdf/Carta_Apresentacao_Emboscada_Full_Stack_Developer_Junior_Miguel_Magalhaes.pdf")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = A4
NAVY = HexColor("#17233D")
BLUE = HexColor("#0087C9")
TEXT = HexColor("#273650")
MUTED = HexColor("#687892")
PALE = HexColor("#EAF4FA")
LINE = HexColor("#D5E0E8")
WHITE = HexColor("#FFFFFF")

LEFT = 31 * mm
RIGHT = 31 * mm
WIDTH = PAGE_W - LEFT - RIGHT

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))


def draw_paragraph(c, text, y, style, width=WIDTH, gap=5):
    p = Paragraph(text, style)
    _, height = p.wrap(width, PAGE_H)
    p.drawOn(c, LEFT, y - height)
    return y - height - gap


c = canvas.Canvas(str(OUTPUT), pagesize=A4)
c.setTitle("Carta de Apresentação - Full Stack Developer Júnior - Grupo Emboscada")
c.setAuthor("Miguel Magalhães")
c.setSubject("Candidatura a Full Stack Developer Júnior - Projeto de IA e Transformação Digital")

# Header band
c.setFillColor(NAVY)
c.rect(0, PAGE_H - 15 * mm, PAGE_W, 15 * mm, fill=1, stroke=0)
c.setFillColor(BLUE)
c.rect(0, PAGE_H - 19 * mm, 54 * mm, 4 * mm, fill=1, stroke=0)

# Header content
c.setFillColor(BLUE)
c.setFont("Arial-Bold", 9.5)
c.drawString(LEFT, PAGE_H - 40 * mm, "CANDIDATURA")

c.setFillColor(NAVY)
c.setFont("Arial-Bold", 23)
c.drawString(LEFT, PAGE_H - 53 * mm, "Miguel Magalhães")

c.setFillColor(MUTED)
c.setFont("Arial", 10.5)
c.drawString(LEFT, PAGE_H - 62 * mm, "Full Stack Developer Júnior | Vila Nova de Gaia")

c.setFont("Arial", 9.5)
date_text = "1 de outubro de 2026"
c.drawRightString(PAGE_W - RIGHT, PAGE_H - 40 * mm, date_text)

# Recipient panel
panel_y = PAGE_H - 100 * mm
panel_h = 20 * mm
c.setFillColor(PALE)
c.setStrokeColor(LINE)
c.rect(LEFT, panel_y, WIDTH, panel_h, fill=1, stroke=1)
c.setFillColor(TEXT)
c.setFont("Arial", 9.5)
c.drawString(LEFT + 5 * mm, panel_y + 11.5 * mm, "Equipa de Recrutamento")
c.drawString(LEFT + 5 * mm, panel_y + 6 * mm, "Grupo Emboscada")

# Styles
subject_style = ParagraphStyle(
    "subject",
    fontName="Arial-Bold",
    fontSize=10.0,
    leading=12.5,
    textColor=NAVY,
    alignment=TA_LEFT,
    spaceAfter=0,
)
body_style = ParagraphStyle(
    "body",
    fontName="Arial",
    fontSize=9.2,
    leading=12.0,
    textColor=TEXT,
    alignment=TA_LEFT,
    spaceAfter=0,
)
signature_style = ParagraphStyle(
    "signature",
    fontName="Arial-Bold",
    fontSize=9.6,
    leading=12.5,
    textColor=NAVY,
)

y = panel_y - 13 * mm
y = draw_paragraph(
    c,
    "Assunto: Candidatura a Full Stack Developer Júnior — Projeto de IA e Transformação Digital",
    y,
    subject_style,
    gap=7,
)

paragraphs = [
    "Exmos. Senhores,",
    (
        "Apresento a minha candidatura à posição de Full Stack Developer Júnior. Identifico-me "
        "particularmente com a oportunidade de participar num projeto de Inteligência Artificial e "
        "Transformação Digital orientado para ligar sistemas, automatizar processos e criar ferramentas "
        "com impacto real nas equipas do Grupo Emboscada."
    ),
    (
        "Sou licenciado em Engenharia Informática e frequento atualmente o Mestrado em Cibersegurança e "
        "Auditoria de Sistemas Informáticos. Durante a minha experiência na Direção de Sistemas de "
        "Informação da NewCoffee, desenvolvi uma plataforma interna de IT Service Management para gerir "
        "tickets, ativos, utilizadores, departamentos e indicadores operacionais. Implementei o frontend "
        "com React, Vite, Bootstrap e Chart.js, criei endpoints REST em PHP, integrei a solução com "
        "Microsoft SQL Server e apoiei a sua disponibilização em Windows Server e IIS."
    ),
    (
        "Desenvolvi também, para um cliente real da área da saúde, uma plataforma de marcação de consultas "
        "com React, TypeScript, Supabase e APIs REST. Fui responsável pela interface, autenticação, "
        "validação de formulários, disponibilidade dinâmica, integração com sistemas clínicos externos e "
        "deployment na Vercel. O acompanhamento da utilização permitiu-me recolher feedback e melhorar os "
        "fluxos entregues."
    ),
    (
        "Tenho contacto prático com o ERP PHC e outros sistemas empresariais, bem como experiência com SQL, "
        "Git, Docker, autenticação, permissões, tratamento de erros, testes funcionais e documentação. A "
        "participação num projeto internacional de deteção de intrusões com Python e machine learning "
        "reforçou ainda o meu interesse pela aplicação responsável de Inteligência Artificial a problemas reais."
    ),
    (
        "Motiva-me a possibilidade de trabalhar proximamente com as equipas do grupo, com a área de dados e "
        "Business Intelligence e com a liderança técnica do projeto. Valorizo ambientes em que seja possível "
        "compreender os processos, testar soluções com utilizadores, assumir progressivamente mais "
        "responsabilidade e acompanhar o impacto das funcionalidades desenvolvidas."
    ),
    (
        "Tenho disponibilidade para trabalhar presencialmente em Vila Nova de Gaia/Porto e teria muito "
        "gosto em conversar sobre a forma como a minha experiência e vontade de evoluir podem contribuir "
        "para este projeto de longo prazo."
    ),
    "Com os melhores cumprimentos,",
]

for idx, paragraph in enumerate(paragraphs):
    gap = 5 if idx in {0, 6} else 6
    y = draw_paragraph(c, paragraph, y, body_style, gap=gap)

y = draw_paragraph(c, "Miguel Magalhães", y - 2, signature_style, gap=0)

if y < 31 * mm:
    raise RuntimeError(f"Conteúdo demasiado próximo do rodapé: y={y:.1f}")

# Footer
footer_y = 17 * mm
c.setStrokeColor(LINE)
c.setLineWidth(0.6)
c.line(LEFT - 3 * mm, footer_y + 8 * mm, PAGE_W - RIGHT + 3 * mm, footer_y + 8 * mm)
c.setFillColor(MUTED)
c.setFont("Arial", 8.2)
c.drawString(LEFT - 3 * mm, footer_y, "Miguel Magalhães  |  miguel.softeng@gmail.com  |  +351 918 860 342")
c.drawRightString(PAGE_W - RIGHT + 3 * mm, footer_y, "Full Stack Developer Júnior")

c.save()
print(OUTPUT.resolve())
