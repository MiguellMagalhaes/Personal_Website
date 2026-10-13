from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


OUT = Path("/Users/miguelmagalhaes/Documents/GitHub/Personal_Website/output/pdf/Cover_Letter_Decskill_Junior_Application_Support_Miguel_Magalhaes.pdf")
OUT.parent.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor("#123A5A")
BLUE = colors.HexColor("#1676B8")
TEXT = colors.HexColor("#26343F")
MID = colors.HexColor("#667580")
LINE = colors.HexColor("#CFDCE5")
PALE = colors.HexColor("#EFF6FA")

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="NameX", fontName="Arial-Bold", fontSize=22, leading=25,
    textColor=NAVY, spaceAfter=2*mm,
))
styles.add(ParagraphStyle(
    name="RoleX", fontName="Arial", fontSize=10.5, leading=14,
    textColor=BLUE, spaceAfter=4*mm,
))
styles.add(ParagraphStyle(
    name="ContactX", fontName="Arial", fontSize=8.6, leading=11.5,
    textColor=MID,
))
styles.add(ParagraphStyle(
    name="DateX", fontName="Arial", fontSize=9, leading=11.5,
    textColor=MID, alignment=TA_RIGHT, spaceAfter=6*mm,
))
styles.add(ParagraphStyle(
    name="BodyX", fontName="Arial", fontSize=9.6, leading=14.1,
    textColor=TEXT, spaceAfter=3.5*mm,
))
styles.add(ParagraphStyle(
    name="SubjectX", fontName="Arial-Bold", fontSize=10.3, leading=14,
    textColor=NAVY, spaceAfter=6*mm,
))
styles.add(ParagraphStyle(
    name="FooterX", fontName="Arial", fontSize=7.8, leading=10,
    textColor=MID,
))


def P(text, style="BodyX"):
    return Paragraph(text, styles[style])


def decorate(canvas, doc):
    w, h = A4
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, h-10*mm, w, 10*mm, fill=1, stroke=0)
    canvas.setFillColor(BLUE)
    canvas.rect(0, h-12*mm, w, 2*mm, fill=1, stroke=0)
    canvas.setStrokeColor(LINE)
    canvas.line(20*mm, 17*mm, w-20*mm, 17*mm)
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MID)
    canvas.drawString(20*mm, 11.5*mm, "Miguel Magalhães | Junior Application Support")
    canvas.drawRightString(w-20*mm, 11.5*mm, "Reference: DA / JAS")
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(OUT), pagesize=A4,
    leftMargin=22*mm, rightMargin=22*mm,
    topMargin=22*mm, bottomMargin=22*mm,
    title="Cover Letter - Decskill Junior Application Support",
    author="Miguel Magalhães",
    subject="Application for Junior Application Support - DA / JAS",
)

story = []
story += [P("Miguel Magalhães", "NameX"), P("IT Support and Systems Technician", "RoleX")]

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
story += [contact, Spacer(1, 5*mm), P("8 October 2026", "DateX")]

story += [
    P("Daniela Adão<br/>Talent Acquisition Team Leader<br/>Decskill", "BodyX"),
    Spacer(1, 1*mm),
    P("Application for Junior Application Support - Reference DA / JAS", "SubjectX"),
    P("Dear Ms Adão,"),
    P("I am writing to apply for the Junior Application Support position in Porto. I hold a degree in Computer Engineering and I am currently pursuing a Master's degree in Cybersecurity and Computer Systems Auditing. The opportunity strongly matches my practical background in user and application support, incident troubleshooting, SQL, scripting and business systems."),
    P("At NewCoffee, I provided first-line technical support to hundreds of users across five locations, handling approximately 20 to 40 requests per day. I diagnosed hardware, software, account, access and connectivity issues in Windows environments and worked with Active Directory, Microsoft 365, VPN, DHCP, business applications and Microsoft SQL Server. I also contributed to the development and maintenance of an internal ITSM and asset-management platform, supporting data validation, issue resolution and technical documentation."),
    P("My broader experience includes Python scripting, SQL Server, ERP support, networking fundamentals and diagnosing integrations in a production web platform. These responsibilities strengthened my ability to collect evidence, analyse logs and errors, reproduce issues, communicate clearly with users and collaborate with technical teams until resolution."),
    P("I am particularly motivated by the role's focus on business-critical applications, monitoring, batch operations and continuous improvement. While my direct database experience is primarily with Microsoft SQL Server, I have solid SQL fundamentals and am keen to deepen my knowledge of Oracle, Linux, scheduling tools such as Control-M, Power BI, Jira and Confluence. I bring a proactive learning mindset and a careful, structured approach to production support."),
    P("I am available for a hybrid working model in Porto and would welcome the opportunity to discuss how my support experience, technical foundation and motivation can contribute to Decskill and its client project."),
    P("Thank you for your time and consideration. I look forward to the possibility of speaking with you."),
    Spacer(1, 2*mm),
    P("Kind regards,<br/><b>Miguel Magalhães</b>"),
]

doc.build(story, onFirstPage=decorate, onLaterPages=decorate)
print(OUT)
