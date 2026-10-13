from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


OUT = Path("/Users/miguelmagalhaes/Documents/GitHub/Personal_Website/output/pdf/Cover_Letter_Dorel_Juvenile_Systems_Administrator_Miguel_Magalhaes.pdf")
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
styles.add(ParagraphStyle(name="DateX", fontName="Arial", fontSize=9, leading=11.5, textColor=MID, alignment=TA_RIGHT, spaceAfter=6*mm))
styles.add(ParagraphStyle(name="BodyX", fontName="Arial", fontSize=9.35, leading=13.5, textColor=TEXT, spaceAfter=3*mm))
styles.add(ParagraphStyle(name="SubjectX", fontName="Arial-Bold", fontSize=10.2, leading=13.5, textColor=NAVY, spaceAfter=5*mm))


def P(text, style="BodyX"):
    return Paragraph(text, styles[style])


def decorate(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, height-10*mm, width, 10*mm, fill=1, stroke=0)
    canvas.setFillColor(TEAL)
    canvas.rect(0, height-12*mm, width, 2*mm, fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.line(20*mm, 17*mm, width-20*mm, 17*mm)
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MID)
    canvas.drawString(20*mm, 11.5*mm, "Miguel Magalhães | Systems Administrator Application")
    canvas.drawRightString(width-20*mm, 11.5*mm, "Vila do Conde, Portugal")
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(OUT), pagesize=A4,
    leftMargin=22*mm, rightMargin=22*mm,
    topMargin=21*mm, bottomMargin=21*mm,
    title="Cover Letter - Dorel Juvenile Systems Administrator",
    author="Miguel Magalhães",
    subject="Application for Systems Administrator",
)

story = [
    P("Miguel Magalhães", "NameX"),
    P("IT Support and Systems Technician", "RoleX"),
]

contact = Table([
    [P("Porto, Portugal", "ContactX"), P("(+351) 918 860 342", "ContactX")],
    [P("miguel.softeng@gmail.com", "ContactX"), P("miguelangelodiasmagalhaes.online", "ContactX")],
], colWidths=[83*mm, 83*mm])
contact.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), PALE),
    ("BOX", (0,0), (-1,-1), 0.6, LINE),
    ("INNERGRID", (0,0), (-1,-1), 0.3, LINE),
    ("LEFTPADDING", (0,0), (-1,-1), 3*mm),
    ("RIGHTPADDING", (0,0), (-1,-1), 3*mm),
    ("TOPPADDING", (0,0), (-1,-1), 2.2*mm),
    ("BOTTOMPADDING", (0,0), (-1,-1), 2.2*mm),
]))

story += [
    contact,
    Spacer(1, 4*mm),
    P("10 October 2026", "DateX"),
    P("Hiring Team<br/>Dorel Juvenile<br/>Vila do Conde, Portugal", "BodyX"),
    Spacer(1, 0.5*mm),
    P("Application for Systems Administrator (M/F/D)", "SubjectX"),
    P("Dear Hiring Team,"),
    P("I am writing to apply for the Systems Administrator position at Dorel Juvenile. I hold a degree in Computer Engineering and I am currently pursuing a Master's degree in Cybersecurity and Computer Systems Auditing. I am motivated by the opportunity to support reliable, secure and well-documented technology services within an international organisation whose products reach families across more than 100 countries."),
    P("At NewCoffee, I provided first-line technical support to hundreds of users across five locations, handling approximately 20 to 40 requests per day. I diagnosed hardware, software, account, access, printing and connectivity issues in Windows environments and worked with Active Directory, Microsoft 365, VPN, DNS, DHCP, business applications, mobile devices and peripherals. I also installed and configured software, maintained asset information, documented incidents and escalated complex cases with complete technical evidence."),
    P("I contributed to the development and maintenance of an internal ITSM and asset-management platform using web technologies and Microsoft SQL Server. This experience strengthened my understanding of system dependencies, data quality, access management, operational documentation and collaboration with internal teams and external suppliers. My current cybersecurity studies reinforce a security-conscious approach based on least privilege, traceability, risk awareness and careful change validation."),
    P("I recognise that this role requests broader direct experience in enterprise server administration than I currently possess. My strongest practical areas are Windows support, Active Directory, Microsoft 365, networking fundamentals, SQL and structured incident troubleshooting. I am actively developing my knowledge of Windows Server, Group Policy, Azure and Entra, Intune, PowerShell, virtualization, monitoring and backup practices. I would bring an honest assessment of my limits, a disciplined approach to change management and the ability to learn unfamiliar systems quickly."),
    P("Dorel Juvenile's emphasis on team spirit, personal drive and accountability strongly appeals to me. I am comfortable working independently, collaborating in English, communicating clearly with users and technical colleagues, and following tasks through to validation and documentation. I am available for a remote or hybrid arrangement and for the stated Monday-to-Friday business schedule."),
    P("Thank you for considering my application. I would welcome the opportunity to discuss how my support experience, technical foundation and commitment to professional growth could contribute to Dorel Juvenile's Technology team."),
    Spacer(1, 0),
    P("Kind regards,<br/><b>Miguel Magalhães</b>"),
]

doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
print(OUT)
