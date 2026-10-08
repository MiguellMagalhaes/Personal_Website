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


OUTPUT = Path("output/pdf/Cover_Letter_Infineon_Cyber_Security_Consultant_IAM_Miguel_Magalhaes.pdf")
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
c.setTitle("Cover Letter - Cyber Security Consultant - Identity and Access Management - Infineon")
c.setAuthor("Miguel Magalhães")
c.setSubject("Application for Cyber Security Consultant - Identity and Access Management")

# Top band
c.setFillColor(NAVY)
c.rect(0, PAGE_H - 15 * mm, PAGE_W, 15 * mm, fill=1, stroke=0)
c.setFillColor(BLUE)
c.rect(0, PAGE_H - 19 * mm, 54 * mm, 4 * mm, fill=1, stroke=0)

# Header
c.setFillColor(BLUE)
c.setFont("Arial-Bold", 9.5)
c.drawString(LEFT, PAGE_H - 40 * mm, "APPLICATION")

c.setFillColor(NAVY)
c.setFont("Arial-Bold", 23)
c.drawString(LEFT, PAGE_H - 53 * mm, "Miguel Magalhães")

c.setFillColor(MUTED)
c.setFont("Arial", 10.5)
c.drawString(LEFT, PAGE_H - 62 * mm, "Cyber Security Consultant | Identity and Access Management")
c.setFont("Arial", 9.5)
c.drawRightString(PAGE_W - RIGHT, PAGE_H - 40 * mm, "1 October 2026")

# Recipient
panel_y = PAGE_H - 100 * mm
panel_h = 20 * mm
c.setFillColor(PALE)
c.setStrokeColor(LINE)
c.rect(LEFT, panel_y, WIDTH, panel_h, fill=1, stroke=1)
c.setFillColor(TEXT)
c.setFont("Arial", 9.5)
c.drawString(LEFT + 5 * mm, panel_y + 11.5 * mm, "Recruitment Team")
c.drawString(LEFT + 5 * mm, panel_y + 6 * mm, "Infineon Technologies | Porto")

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
    fontSize=9.15,
    leading=11.75,
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
    "Subject: Application for Cyber Security Consultant - Identity and Access Management",
    y,
    subject_style,
    gap=7,
)

paragraphs = [
    "Dear Recruitment Team,",
    (
        "I am writing to apply for the Cyber Security Consultant - Identity and Access Management "
        "position in Porto. Infineon's focus on secure, resilient and future-ready identity services is "
        "closely aligned with the direction in which I am developing my career: combining practical "
        "systems experience with cybersecurity, risk awareness and continuous improvement."
    ),
    (
        "I hold a Bachelor's degree in Computer Engineering and a Higher Professional Technical Diploma "
        "in Computer Networks and Systems, and I am currently pursuing a Master's degree in Cybersecurity "
        "and Information Systems Auditing. This academic path has strengthened my foundations in network "
        "security, access control, cryptography, systems administration, risk and data protection."
    ),
    (
        "At NewCoffee's Information Systems Department, I supported users across different departments "
        "and locations and worked directly with identity and access tasks in Microsoft Active Directory. "
        "I created and managed user accounts, groups, permissions and access rights, supported VPN and "
        "business application access, investigated authentication and connectivity incidents, and "
        "documented changes and resolutions. This experience gave me a practical understanding of identity "
        "lifecycle activities, least-privilege decisions and the operational impact of access controls."
    ),
    (
        "My cybersecurity projects have included an international AI-based network intrusion detection "
        "laboratory using Python, Wireshark and Snort, as well as the design of security policies, network "
        "controls, cryptographic protections and data-protection measures for a simulated corporate "
        "environment. Through full-stack projects, I have also implemented authentication, role-based "
        "permissions, protected APIs, validation and secure handling of application data."
    ),
    (
        "My professional IAM exposure is currently grounded in hands-on identity administration and user "
        "support rather than enterprise-scale IAM architecture. I am nevertheless highly motivated to "
        "deepen my knowledge of Entra ID, federation, privileged access management, Zero Trust, threat "
        "modelling and IAM governance. I would bring a structured problem-solving approach, clear "
        "communication, customer focus and the discipline to challenge assumptions while learning from "
        "experienced architecture, engineering and security teams."
    ),
    (
        "I have professional working proficiency in English and experience collaborating in an "
        "international academic team. I am available for the hybrid working model in Porto and would "
        "welcome the opportunity to discuss how my technical foundation, cybersecurity studies and "
        "commitment to growth could contribute to Infineon's Corporate Cyber Security and Privacy team."
    ),
    "Kind regards,",
]

for index, text in enumerate(paragraphs):
    gap = 4 if index in {0, 6} else 5.5
    y = draw_paragraph(c, text, y, body_style, gap=gap)

y = draw_paragraph(c, "Miguel Magalhães", y - 2, signature_style, gap=0)

if y < 29 * mm:
    raise RuntimeError(f"Content too close to footer: y={y:.1f}")

# Footer
footer_y = 17 * mm
c.setStrokeColor(LINE)
c.setLineWidth(0.6)
c.line(LEFT - 3 * mm, footer_y + 8 * mm, PAGE_W - RIGHT + 3 * mm, footer_y + 8 * mm)
c.setFillColor(MUTED)
c.setFont("Arial", 8.1)
c.drawString(LEFT - 3 * mm, footer_y, "Miguel Magalhães  |  miguel.softeng@gmail.com  |  +351 918 860 342")
c.drawRightString(PAGE_W - RIGHT + 3 * mm, footer_y, "Cyber Security | IAM")

c.save()
print(OUTPUT.resolve())
