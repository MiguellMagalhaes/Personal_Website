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


OUTPUT = Path("output/pdf/Cover_Letter_Maple_Networks_Cyber_Security_Analyst_Nights_Miguel_Magalhaes.pdf")
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
c.setTitle("Cover Letter - Cyber Security Analyst - Nights - Maple Networks")
c.setAuthor("Miguel Magalhães")
c.setSubject("Application for Cyber Security Analyst - Nights")

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
c.drawString(LEFT, PAGE_H - 62 * mm, "Cyber Security Analyst | Security Operations Centre")
c.setFont("Arial", 9.5)
c.drawRightString(PAGE_W - RIGHT, PAGE_H - 40 * mm, "1 October 2026")

# Recipient panel
panel_y = PAGE_H - 100 * mm
panel_h = 20 * mm
c.setFillColor(PALE)
c.setStrokeColor(LINE)
c.rect(LEFT, panel_y, WIDTH, panel_h, fill=1, stroke=1)
c.setFillColor(TEXT)
c.setFont("Arial", 9.5)
c.drawString(LEFT + 5 * mm, panel_y + 11.5 * mm, "Recruitment Team")
c.drawString(LEFT + 5 * mm, panel_y + 6 * mm, "Maple Networks")

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
    leading=11.0,
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
    "Subject: Application for Cyber Security Analyst - Nights",
    y,
    subject_style,
    gap=7,
)

paragraphs = [
    "Dear Recruitment Team,",
    (
        "I am writing to apply for the Cyber Security Analyst - Nights position at Maple Networks. The "
        "opportunity to begin and develop my Security Operations Centre career within a managed security "
        "services environment strongly appeals to me, particularly because it combines proactive "
        "monitoring, incident response, customer support and continuous learning."
    ),
    (
        "I hold a Bachelor's degree in Computer Engineering and a Higher Professional Technical Diploma "
        "in Computer Networks and Systems, and I am currently pursuing a Master's degree in Cybersecurity "
        "and Information Systems Auditing. My education has provided a solid foundation in Windows and "
        "Linux systems, TCP/IP networking, access control, cryptography, risk, data protection and secure "
        "systems administration."
    ),
    (
        "At NewCoffee's Information Systems Department, I acted as a first point of contact for users "
        "across different departments and locations. I logged, investigated and followed technical "
        "incidents involving Windows devices, accounts and permissions, Active Directory, VPN, DHCP, "
        "connectivity, business applications and endpoint hardware. I documented actions, coordinated with "
        "external providers when escalation was required, and validated outcomes with users. I also "
        "developed an internal ITSM platform for tickets, assets and operational indicators, strengthening "
        "my understanding of incident workflows, prioritisation, traceability and service levels."
    ),
    (
        "My most relevant cybersecurity project was an international AI-based network intrusion detection "
        "laboratory. I helped configure isolated virtual environments, generate baseline traffic, capture "
        "and analyse packets with Wireshark, simulate controlled attacks and validate alerts using Snort. "
        "The project combined network security, Python-based data processing and machine learning to "
        "support the identification of malicious activity. Additional projects covered security policies, "
        "cryptographic protections, secure proxy configuration and access control."
    ),
    (
        "Although I am at the beginning of my professional SOC career, I bring practical IT operations "
        "experience, an analytical and methodical approach, and a strong sense of ownership. I am keen to "
        "develop hands-on expertise with Microsoft Sentinel, SIEM and SOAR workflows, vulnerability "
        "management and public cloud security. I understand the importance of clear escalation, accurate "
        "documentation, SLA follow-up and calm communication when supporting customers during incidents."
    ),
    (
        "I have professional working proficiency in English and experience collaborating in an "
        "international team. I understand the schedule required for this role and am prepared to work "
        "flexible overnight and weekend shifts in a remote environment. I would welcome the opportunity "
        "to discuss how my technical background, cybersecurity training and motivation to learn could "
        "contribute to Maple Networks and its customers."
    ),
    "Kind regards,",
]

for index, text in enumerate(paragraphs):
    gap = 3.5 if index in {0, 6} else 4.0
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
c.drawRightString(PAGE_W - RIGHT + 3 * mm, footer_y, "Cyber Security Analyst")

c.save()
print(OUTPUT.resolve())
