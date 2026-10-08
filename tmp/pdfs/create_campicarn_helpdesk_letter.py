from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


OUTPUT = Path("output/pdf/Carta_Apresentacao_Campicarn_Tecnico_Informatica_Help_Desk_Miguel_Magalhaes.pdf")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = A4
NAVY = HexColor("#17233D")
BLUE = HexColor("#0087C9")
TEXT = HexColor("#273650")
MUTED = HexColor("#687892")
PALE = HexColor("#EAF4FA")
LINE = HexColor("#D5E0E8")

LEFT = 31 * mm
RIGHT = 31 * mm
WIDTH = PAGE_W - LEFT - RIGHT

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))


def draw_paragraph(c, text, y, style, width=WIDTH, gap=5):
    paragraph = Paragraph(text, style)
    _, height = paragraph.wrap(width, PAGE_H)
    paragraph.drawOn(c, LEFT, y - height)
    return y - height - gap


c = canvas.Canvas(str(OUTPUT), pagesize=A4)
c.setTitle("Carta de Apresentação - Técnico de Informática / Help Desk - Campicarn")
c.setAuthor("Miguel Magalhães")
c.setSubject("Candidatura a Técnico de Informática / Help Desk na Campicarn")

# Faixa superior
c.setFillColor(NAVY)
c.rect(0, PAGE_H - 15 * mm, PAGE_W, 15 * mm, fill=1, stroke=0)
c.setFillColor(BLUE)
c.rect(0, PAGE_H - 19 * mm, 54 * mm, 4 * mm, fill=1, stroke=0)

# Cabeçalho
c.setFillColor(BLUE)
c.setFont("Arial-Bold", 9.5)
c.drawString(LEFT, PAGE_H - 40 * mm, "CANDIDATURA")

c.setFillColor(NAVY)
c.setFont("Arial-Bold", 23)
c.drawString(LEFT, PAGE_H - 53 * mm, "Miguel Magalhães")

c.setFillColor(MUTED)
c.setFont("Arial", 10.5)
c.drawString(LEFT, PAGE_H - 62 * mm, "Técnico de Informática / Help Desk")
c.setFont("Arial", 9.5)
c.drawRightString(PAGE_W - RIGHT, PAGE_H - 40 * mm, "1 de outubro de 2026")

# Destinatário
panel_y = PAGE_H - 100 * mm
panel_h = 20 * mm
c.setFillColor(PALE)
c.setStrokeColor(LINE)
c.rect(LEFT, panel_y, WIDTH, panel_h, fill=1, stroke=1)
c.setFillColor(TEXT)
c.setFont("Arial", 9.5)
c.drawString(LEFT + 5 * mm, panel_y + 11.5 * mm, "Departamento de Recursos Humanos")
c.drawString(LEFT + 5 * mm, panel_y + 6 * mm, "Campicarn")

subject_style = ParagraphStyle(
    "subject",
    fontName="Arial-Bold",
    fontSize=10.0,
    leading=12.5,
    textColor=NAVY,
    alignment=TA_LEFT,
)
body_style = ParagraphStyle(
    "body",
    fontName="Arial",
    fontSize=9.0,
    leading=11.35,
    textColor=TEXT,
    alignment=TA_LEFT,
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
    "Assunto: Candidatura à posição de Técnico de Informática / Help Desk",
    y,
    subject_style,
    gap=7,
)

paragraphs = [
    "Exmos. Senhores,",
    (
        "Apresento a minha candidatura à posição de Técnico de Informática / Help Desk na Campicarn. "
        "A missão de garantir o correto funcionamento dos equipamentos, sistemas, redes e aplicações da "
        "empresa está diretamente alinhada com a experiência prática que desenvolvi em suporte técnico, "
        "infraestruturas e apoio a utilizadores."
    ),
    (
        "Sou licenciado em Engenharia Informática, possuo um CTeSP em Redes e Sistemas Informáticos e "
        "frequento atualmente o Mestrado em Cibersegurança e Auditoria de Sistemas Informáticos. Esta "
        "formação deu-me bases sólidas em ambientes Windows, redes TCP/IP, hardware, bases de dados, "
        "segurança, administração de sistemas e diagnóstico estruturado de incidentes."
    ),
    (
        "Na Direção de Sistemas de Informação da NewCoffee, uma empresa industrial, fui primeiro ponto de "
        "contacto para utilizadores de diferentes departamentos e instalações, presencialmente e à "
        "distância. Resolvi incidentes de hardware, software, Microsoft 365, contas e permissões, Active "
        "Directory, impressão, conectividade, VPN, DHCP e aplicações empresariais. Preparei e mantive "
        "computadores, portáteis, dispositivos móveis e periféricos, atualizei informação sobre ativos e "
        "colaborei com fornecedores externos na resolução de situações mais complexas."
    ),
    (
        "Na Staples EasyTech, reforcei a vertente hands-on através do diagnóstico e resolução de problemas "
        "em equipamentos, software e periféricos, do suporte a terminais POS e da comunicação de soluções "
        "a utilizadores sem perfil técnico. Esta experiência consolidou a minha orientação para o cliente, "
        "empatia, capacidade de priorização e acompanhamento dos pedidos até à sua resolução."
    ),
    (
        "Durante o estágio na Aquário Eletrónica, apoiei infraestruturas de rede e sistemas, trabalhei com "
        "Microsoft SQL Server e o ERP Primavera e desenvolvi automatizações em Python. Na NewCoffee tive "
        "também contacto com o ERP PHC. Embora ainda não tenha trabalhado diretamente com SAGE X3, tenho "
        "facilidade em aprender novas aplicações empresariais e em compreender os processos que suportam."
    ),
    (
        "Trabalho de forma metódica, proativa e orientada para o utilizador: procuro compreender o impacto "
        "do problema, recolher evidências, testar hipóteses de forma segura, documentar a intervenção e "
        "validar o resultado. Valorizo o trabalho em equipa e aplico princípios de cibersegurança na gestão "
        "de acessos, equipamentos e informação."
    ),
    (
        "Tenho disponibilidade para trabalhar presencialmente em Vila Nova de Famalicão e teria muito "
        "gosto em apresentar, numa entrevista, de que forma a minha experiência e motivação podem "
        "contribuir para a Direção de Sistemas de Informação da Campicarn."
    ),
    "Com os melhores cumprimentos,",
]

for index, text in enumerate(paragraphs):
    gap = 4 if index in {0, 7} else 4.5
    y = draw_paragraph(c, text, y, body_style, gap=gap)

y = draw_paragraph(c, "Miguel Magalhães", y - 2, signature_style, gap=0)

if y < 29 * mm:
    raise RuntimeError(f"Conteúdo demasiado próximo do rodapé: y={y:.1f}")

# Rodapé
footer_y = 17 * mm
c.setStrokeColor(LINE)
c.setLineWidth(0.6)
c.line(LEFT - 3 * mm, footer_y + 8 * mm, PAGE_W - RIGHT + 3 * mm, footer_y + 8 * mm)
c.setFillColor(MUTED)
c.setFont("Arial", 8.1)
c.drawString(LEFT - 3 * mm, footer_y, "Miguel Magalhães  |  miguel.softeng@gmail.com  |  +351 918 860 342")
c.drawRightString(PAGE_W - RIGHT + 3 * mm, footer_y, "Técnico de Informática / Help Desk")

c.save()
print(OUTPUT.resolve())
