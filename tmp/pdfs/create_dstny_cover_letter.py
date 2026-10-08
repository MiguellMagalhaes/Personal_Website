from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, HRFlowable, KeepTogether, PageTemplate, Paragraph, Spacer


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "output" / "pdf" / "Cover_Letter_Miguel_Magalhaes_Dstny.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)


def register_fonts():
    options = [
        (
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        ),
        (
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        ),
    ]
    for regular, bold in options:
        if Path(regular).exists() and Path(bold).exists():
            pdfmetrics.registerFont(TTFont("LetterSans", regular))
            pdfmetrics.registerFont(TTFont("LetterSans-Bold", bold))
            return "LetterSans", "LetterSans-Bold"
    return "Helvetica", "Helvetica-Bold"


REGULAR, BOLD = register_fonts()
NAVY = colors.HexColor("#142A43")
PURPLE = colors.HexColor("#7157D9")
INK = colors.HexColor("#263442")
MUTED = colors.HexColor("#647486")
PALE = colors.HexColor("#EEEAFB")


class CoverLetter(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=21 * mm,
            rightMargin=21 * mm,
            topMargin=18 * mm,
            bottomMargin=17 * mm,
            title="Cover Letter - Miguel Magalhães - Dstny",
            author="Miguel Magalhães",
            subject="Application for Infrastructure & Platform Engineer",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="main",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(PageTemplate(id="letter", frames=[frame], onPage=self.decorate))

    def decorate(self, canvas, doc):
        width, height = A4
        canvas.saveState()
        canvas.setFillColor(NAVY)
        canvas.rect(0, height - 7 * mm, width, 7 * mm, stroke=0, fill=1)
        canvas.setFillColor(PURPLE)
        canvas.rect(0, height - 8.5 * mm, width, 1.5 * mm, stroke=0, fill=1)
        canvas.setStrokeColor(colors.HexColor("#CCD4DE"))
        canvas.setLineWidth(0.5)
        canvas.line(21 * mm, 13 * mm, width - 21 * mm, 13 * mm)
        canvas.setFont(REGULAR, 7.6)
        canvas.setFillColor(MUTED)
        canvas.drawString(21 * mm, 8.8 * mm, "Miguel Magalhães | Infrastructure & Platform Engineer")
        canvas.drawRightString(width - 21 * mm, 8.8 * mm, "Porto, Portugal")
        canvas.restoreState()


styles = getSampleStyleSheet()
name = ParagraphStyle(
    "Name",
    fontName=BOLD,
    fontSize=22,
    leading=25,
    textColor=NAVY,
    spaceAfter=2,
)
headline = ParagraphStyle(
    "Headline",
    fontName=REGULAR,
    fontSize=10.5,
    leading=13,
    textColor=PURPLE,
    spaceAfter=5,
)
contact = ParagraphStyle(
    "Contact",
    fontName=REGULAR,
    fontSize=8.5,
    leading=12,
    textColor=MUTED,
    spaceAfter=8,
)
meta = ParagraphStyle(
    "Meta",
    fontName=REGULAR,
    fontSize=9.2,
    leading=13,
    textColor=INK,
    spaceAfter=1,
)
subject = ParagraphStyle(
    "Subject",
    fontName=BOLD,
    fontSize=11.5,
    leading=15,
    textColor=NAVY,
    backColor=PALE,
    borderPadding=(6, 8, 6, 8),
    spaceBefore=9,
    spaceAfter=10,
)
body = ParagraphStyle(
    "Body",
    fontName=REGULAR,
    fontSize=9.15,
    leading=12.8,
    textColor=INK,
    alignment=TA_LEFT,
    spaceAfter=7,
)
signature = ParagraphStyle(
    "Signature",
    fontName=BOLD,
    fontSize=10,
    leading=13,
    textColor=NAVY,
)


story = [
    Paragraph("Miguel Magalhães", name),
    Paragraph("Computer Engineering Graduate | IT Operations, Systems and Automation", headline),
    Paragraph(
        "Valongo, Portugal &nbsp;&nbsp;|&nbsp;&nbsp; (+351) 918 860 342 &nbsp;&nbsp;|&nbsp;&nbsp; "
        "miguel.softeng@gmail.com<br/>miguelangelodiasmagalhaes.online",
        contact,
    ),
    HRFlowable(width="100%", thickness=1.1, color=PURPLE, spaceBefore=0, spaceAfter=9),
    Paragraph("5 October 2026", meta),
    Spacer(1, 4),
    Paragraph("Hiring Team", meta),
    Paragraph("Dstny", meta),
    Paragraph("Ramalde, Porto, Portugal", meta),
    Paragraph("APPLICATION FOR INFRASTRUCTURE & PLATFORM ENGINEER", subject),
    Paragraph("Dear Hiring Team,", body),
    Paragraph(
        "I am writing to apply for the Infrastructure & Platform Engineer position at Dstny. I hold a degree "
        "in Computer Engineering, completed technical training in Computer Networks and Systems, and am currently "
        "pursuing a Master's degree in Cybersecurity and Computer Systems Auditing.",
        body,
    ),
    Paragraph(
        "My experience combines IT operations, systems support, networking, databases, scripting and application "
        "troubleshooting. At NewCoffee, I provided first-line technical support to hundreds of users across five "
        "locations, handling approximately 20 to 40 daily requests involving business applications, hardware, "
        "software, accounts, permissions and network connectivity.",
        body,
    ),
    Paragraph(
        "I worked with Windows environments, Active Directory, DNS, DHCP, VPN, Microsoft 365, Microsoft SQL Server "
        "and IIS. I reproduced problems where possible, collected technical evidence, analysed system and application "
        "dependencies, documented the actions performed and escalated complex cases with a structured handover. I also "
        "contributed to an internal ITSM and asset-management platform using React, JavaScript, PHP, Python, SQL Server "
        "and REST APIs.",
        body,
    ),
    Paragraph(
        "During my internship at Aquário Eletrónica, I developed Python scripts for data collection and task automation "
        "and supported Microsoft SQL Server, Primavera ERP and local network infrastructure. More recently, I delivered "
        "a production appointment-booking platform using React, TypeScript, REST APIs and serverless functions. I "
        "configured its deployment and diagnosed integration issues through logs, HTTP responses, environment settings "
        "and end-to-end data flows.",
        body,
    ),
    Paragraph(
        "I have practical knowledge of Windows and Linux, Active Directory, DNS, DHCP, IIS, TCP/IP, SQL, Python, Git, "
        "APIs and application deployment. I am motivated to deepen my experience in production Linux administration, "
        "server lifecycle management, patching, hardening, backup and recovery, monitoring, containers and CI/CD. While "
        "I am still developing hands-on experience with Foreman, RabbitMQ, Kubernetes, Prometheus and Grafana, I bring "
        "a solid systems foundation, structured troubleshooting habits and strong learning agility.",
        body,
    ),
    Paragraph(
        "Dstny's international environment and focus on reliable cloud and telecommunications platforms strongly match "
        "the direction in which I want to develop my career. I value operational ownership, clear runbooks, reusable "
        "procedures and the automation of repetitive work, and I would welcome the opportunity to contribute while "
        "expanding my infrastructure and platform-engineering capabilities alongside your team.",
        body,
    ),
    Paragraph(
        "Thank you for considering my application. I would be pleased to discuss my experience and motivation in an interview.",
        body,
    ),
    KeepTogether([
        Paragraph("Yours faithfully,", body),
        Spacer(1, 1),
        Paragraph("Miguel Magalhães", signature),
    ]),
]


doc = CoverLetter(str(OUTPUT))
doc.build(story)
print(OUTPUT)
