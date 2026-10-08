from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether


OUTPUT = "/Users/miguelmagalhaes/Documents/GitHub/Personal_Website/output/pdf/Cover_Letter_Miguel_Magalhaes_Data_Center_Technician.pdf"

NAVY = HexColor("#142B45")
ORANGE = HexColor("#D46B28")
TEXT = HexColor("#263238")
MUTED = HexColor("#5F6B73")
LIGHT = HexColor("#D9E3E8")


def header_footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setFillColor(NAVY)
    canvas.rect(0, height - 7 * mm, width, 7 * mm, stroke=0, fill=1)
    canvas.setFillColor(ORANGE)
    canvas.rect(0, height - 8.2 * mm, width, 1.2 * mm, stroke=0, fill=1)
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.5)
    canvas.line(22 * mm, 15 * mm, width - 22 * mm, 15 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(22 * mm, 10.5 * mm, "Miguel Magalhães | Application for Data Center Technician")
    canvas.drawRightString(width - 22 * mm, 10.5 * mm, "Porto, Portugal")
    canvas.restoreState()


doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=22 * mm,
    leftMargin=22 * mm,
    topMargin=19 * mm,
    bottomMargin=22 * mm,
    title="Cover Letter - Miguel Magalhães - Data Center Technician",
    author="Miguel Magalhães",
    subject="Application for Data Center Technician",
)

styles = getSampleStyleSheet()
name_style = ParagraphStyle(
    "Name",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=20,
    leading=23,
    textColor=NAVY,
    alignment=TA_LEFT,
    spaceAfter=3,
)
contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9,
    leading=13,
    textColor=MUTED,
)
role_style = ParagraphStyle(
    "Role",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=12.5,
    leading=16,
    textColor=ORANGE,
    spaceBefore=5,
    spaceAfter=3,
)
meta_style = ParagraphStyle(
    "Meta",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.5,
    leading=13,
    textColor=MUTED,
    spaceAfter=8,
)
body_style = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=10.1,
    leading=14.4,
    textColor=TEXT,
    alignment=TA_LEFT,
    spaceAfter=7.5,
)
closing_style = ParagraphStyle(
    "Closing",
    parent=body_style,
    spaceBefore=1,
    spaceAfter=2,
)

story = [
    Paragraph("Miguel Magalhães", name_style),
    Paragraph(
        "(+351) 918 860 342 &nbsp;&nbsp;|&nbsp;&nbsp; miguel.softeng@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; "
        "miguelangelodiasmagalhaes.online",
        contact_style,
    ),
    Spacer(1, 4 * mm),
    HRFlowable(width="100%", thickness=1.1, color=ORANGE, spaceBefore=0, spaceAfter=7),
    Paragraph("Application for Data Center Technician", role_style),
    Paragraph("Porto, Portugal | 6 October 2026", meta_style),
]

paragraphs = [
    "Dear Hiring Team,",
    "I am writing to express my interest in the freelance Data Center Technician opportunity in Porto. I hold a degree in Computer Engineering, have specialised technical training in Computer Networks and Systems, and bring practical experience in IT support, hardware configuration, network troubleshooting and infrastructure operations.",
    "During my experience at NewCoffee, I provided technical support to hundreds of users across five locations. My responsibilities included preparing and configuring computers, laptops, printers, mobile devices and peripherals; diagnosing hardware, software and connectivity incidents; supporting network infrastructure; maintaining asset records; and coordinating complex cases with internal teams and external providers.",
    "My technical foundation includes Windows and Linux systems, TCP/IP networking, DNS, DHCP, VPNs, hardware diagnostics and basic server administration. I am comfortable following technical procedures, validating connectivity, identifying faults and documenting the actions performed. I understand the importance of accurate labelling, detailed records, photographic evidence and clear communication when carrying out remote hands activities on behalf of NOC and client teams.",
    "Although my direct professional experience has primarily involved workplace and network support rather than dedicated data center operations, my education and practical background have prepared me to work carefully with hardware and infrastructure. I am motivated to develop further experience in server installation, rack and stack activities, structured cabling, cross-connects, migrations and decommissioning procedures.",
    "I am based in the Porto area, have experience working independently and communicating with technical and non-technical stakeholders, and am comfortable with freelance and project-based assignments. I approach technical work with responsibility, organisation and attention to detail, particularly when supporting business-critical infrastructure.",
    "Thank you for considering my application. I would welcome the opportunity to discuss my availability and how my technical background could support your data center projects in Porto.",
]

for paragraph in paragraphs:
    story.append(Paragraph(paragraph, body_style))

story.extend([
    Spacer(1, 1 * mm),
    KeepTogether([
        Paragraph("Kind regards,", closing_style),
        Spacer(1, 2 * mm),
        Paragraph("<b>Miguel Magalhães</b>", closing_style),
    ]),
])

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)

