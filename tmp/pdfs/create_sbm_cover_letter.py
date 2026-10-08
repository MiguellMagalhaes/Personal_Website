from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether


OUTPUT = "/Users/miguelmagalhaes/Documents/GitHub/Personal_Website/output/pdf/Cover_Letter_Miguel_Magalhaes_SBM_Offshore.pdf"

NAVY = HexColor("#17324D")
TEAL = HexColor("#2B7A78")
TEXT = HexColor("#263238")
MUTED = HexColor("#5F6B73")
LIGHT = HexColor("#D9E3E8")


def header_footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setFillColor(NAVY)
    canvas.rect(0, height - 7 * mm, width, 7 * mm, stroke=0, fill=1)
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.5)
    canvas.line(22 * mm, 15 * mm, width - 22 * mm, 15 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(22 * mm, 10.5 * mm, "Miguel Magalhães | Application for IT Support Technician")
    canvas.drawRightString(width - 22 * mm, 10.5 * mm, "Porto, Portugal")
    canvas.restoreState()


doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=22 * mm,
    leftMargin=22 * mm,
    topMargin=18 * mm,
    bottomMargin=22 * mm,
    title="Cover Letter - Miguel Magalhães - SBM Offshore",
    author="Miguel Magalhães",
    subject="Application for IT Support Technician",
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
    spaceAfter=0,
)
role_style = ParagraphStyle(
    "Role",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=12.5,
    leading=16,
    textColor=TEAL,
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

story = []
story.append(Paragraph("Miguel Magalhães", name_style))
story.append(Paragraph(
    "(+351) 918 860 342 &nbsp;&nbsp;|&nbsp;&nbsp; miguel.softeng@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; "
    "miguelangelodiasmagalhaes.online",
    contact_style,
))
story.append(Spacer(1, 4 * mm))
story.append(HRFlowable(width="100%", thickness=1.1, color=TEAL, spaceBefore=0, spaceAfter=7))
story.append(Paragraph("Application for IT Support Technician", role_style))
story.append(Paragraph("SBM Offshore | Porto | 6 October 2026", meta_style))

paragraphs = [
    "Dear Hiring Team,",
    "I am writing to express my interest in the IT Support Technician position at SBM Offshore. With a degree in Computer Engineering, specialised training in Computer Networks and Systems, and practical experience in end-user support, I believe my background aligns strongly with the technical and service-oriented nature of this role.",
    "At NewCoffee, I provided first-line support to hundreds of users across five locations, handling approximately 20 to 40 daily requests. My responsibilities included diagnosing hardware, software and connectivity issues; preparing and configuring Windows computers, laptops, printers and mobile devices; managing user accounts, groups, permissions and access through Active Directory; and supporting Microsoft 365, VPNs and business applications. I also registered and followed incidents through the support process, maintained asset information and escalated complex cases to the appropriate internal teams or external providers.",
    "My experience at Staples further strengthened my ability to communicate clearly with non-technical users, diagnose equipment problems and install or configure software. I understand the importance of listening carefully, explaining solutions in accessible language and following each request through to completion.",
    "In addition to support experience, I have worked with Windows and Linux systems, TCP/IP networks, DNS, DHCP, VPNs, SQL databases and technical documentation. I also contributed to an internal ITSM and asset-management platform, giving me a broader understanding of ticket management, inventories and support workflows. I am currently pursuing a Master's degree in Cybersecurity and Computer Systems Auditing, which is strengthening my knowledge of security practices and risk awareness.",
    "I am particularly attracted to SBM Offshore because of its international environment, operational focus and commitment to reliable and safe infrastructure. I would welcome the opportunity to apply my technical abilities, customer-service mindset and willingness to learn while supporting your users and business operations.",
    "Thank you for considering my application. I would be pleased to discuss how my experience and motivation could contribute to SBM Offshore's IT team.",
]

for paragraph in paragraphs:
    story.append(Paragraph(paragraph, body_style))

story.append(Spacer(1, 1 * mm))
story.append(KeepTogether([
    Paragraph("Kind regards,", closing_style),
    Spacer(1, 2 * mm),
    Paragraph("<b>Miguel Magalhães</b>", closing_style),
]))

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
