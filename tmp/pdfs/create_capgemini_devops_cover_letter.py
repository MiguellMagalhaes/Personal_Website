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
OUTPUT = ROOT / "output" / "pdf" / "Cover_Letter_Miguel_Magalhaes_Capgemini_Junior_DevOps.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)


def register_fonts():
    candidates = [
        (
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        ),
        (
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        ),
    ]
    for regular, bold in candidates:
        if Path(regular).exists() and Path(bold).exists():
            pdfmetrics.registerFont(TTFont("LetterSans", regular))
            pdfmetrics.registerFont(TTFont("LetterSans-Bold", bold))
            return "LetterSans", "LetterSans-Bold"
    return "Helvetica", "Helvetica-Bold"


REGULAR, BOLD = register_fonts()
NAVY = colors.HexColor("#123A5A")
BLUE = colors.HexColor("#0070AD")
CYAN = colors.HexColor("#12ABDB")
INK = colors.HexColor("#263442")
MUTED = colors.HexColor("#617385")
PALE = colors.HexColor("#E7F5FA")


class CoverLetter(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=21 * mm,
            rightMargin=21 * mm,
            topMargin=18 * mm,
            bottomMargin=17 * mm,
            title="Cover Letter - Miguel Magalhães - Capgemini Junior DevOps Engineer",
            author="Miguel Magalhães",
            subject="Application for Junior DevOps Engineer",
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
        canvas.setFillColor(CYAN)
        canvas.rect(0, height - 8.5 * mm, width, 1.5 * mm, stroke=0, fill=1)
        canvas.setStrokeColor(colors.HexColor("#CBD7E0"))
        canvas.setLineWidth(0.5)
        canvas.line(21 * mm, 13 * mm, width - 21 * mm, 13 * mm)
        canvas.setFont(REGULAR, 7.6)
        canvas.setFillColor(MUTED)
        canvas.drawString(21 * mm, 8.8 * mm, "Miguel Magalhães | Junior DevOps Engineer")
        canvas.drawRightString(width - 21 * mm, 8.8 * mm, "Vila Nova de Gaia / Porto")
        canvas.restoreState()


styles = getSampleStyleSheet()
name = ParagraphStyle(
    "Name", fontName=BOLD, fontSize=22, leading=25, textColor=NAVY, spaceAfter=2
)
headline = ParagraphStyle(
    "Headline", fontName=REGULAR, fontSize=10.5, leading=13, textColor=BLUE, spaceAfter=5
)
contact = ParagraphStyle(
    "Contact", fontName=REGULAR, fontSize=8.5, leading=12, textColor=MUTED, spaceAfter=8
)
meta = ParagraphStyle(
    "Meta", fontName=REGULAR, fontSize=9.2, leading=13, textColor=INK, spaceAfter=1
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
    fontSize=9.2,
    leading=12.85,
    textColor=INK,
    alignment=TA_LEFT,
    spaceAfter=7,
)
signature = ParagraphStyle(
    "Signature", fontName=BOLD, fontSize=10, leading=13, textColor=NAVY
)


story = [
    Paragraph("Miguel Magalhães", name),
    Paragraph("Computer Engineering Graduate | DevOps, Automation and IT Operations", headline),
    Paragraph(
        "Valongo, Portugal &nbsp;&nbsp;|&nbsp;&nbsp; (+351) 918 860 342 &nbsp;&nbsp;|&nbsp;&nbsp; "
        "miguel.softeng@gmail.com<br/>miguelangelodiasmagalhaes.online",
        contact,
    ),
    HRFlowable(width="100%", thickness=1.1, color=CYAN, spaceBefore=0, spaceAfter=9),
    Paragraph("5 October 2026", meta),
    Spacer(1, 4),
    Paragraph("Hiring Team", meta),
    Paragraph("Capgemini Portugal", meta),
    Paragraph("Vila Nova de Gaia, Porto, Portugal", meta),
    Paragraph("APPLICATION FOR JUNIOR DEVOPS ENGINEER", subject),
    Paragraph("Dear Hiring Team,", body),
    Paragraph(
        "I am writing to apply for the Junior DevOps Engineer position at Capgemini. I hold a degree in Computer "
        "Engineering, completed technical training in Computer Networks and Systems, and am currently pursuing a "
        "Master's degree in Cybersecurity and Computer Systems Auditing.",
        body,
    ),
    Paragraph(
        "As a freelance developer, I delivered a production appointment-booking platform using React, TypeScript, REST "
        "APIs and serverless functions. I configured its deployment and environment variables, used Git throughout the "
        "development lifecycle, and diagnosed integration issues by analysing logs, HTTP responses and end-to-end data "
        "flows between the frontend, serverless layer and an external clinical API.",
        body,
    ),
    Paragraph(
        "At NewCoffee, I supported hundreds of users across five locations and handled approximately 20 to 40 daily "
        "requests involving applications, systems, accounts, access and connectivity. I also contributed to an internal "
        "ITSM and asset-management platform using React, JavaScript, PHP, Python, Microsoft SQL Server, REST APIs and IIS. "
        "My work included troubleshooting, reviewing SQL queries, correcting errors, documenting recurring issues and "
        "coordinating structured escalations with technical teams and external providers.",
        body,
    ),
    Paragraph(
        "During my internship at Aquário Eletrónica, I developed Python scripts for data collection and task automation "
        "and supported Microsoft SQL Server, Primavera ERP and local network infrastructure. These experiences strengthened "
        "my understanding of automation, repeatable processes, system dependencies and reliable operational documentation.",
        body,
    ),
    Paragraph(
        "I have practical knowledge of Windows and Linux, Python, Git, SQL, APIs, networking, deployment and application "
        "lifecycle concepts. My current Master's degree also reinforces my awareness of security, access control, risk and "
        "compliance. I am actively developing my knowledge of Docker, Kubernetes, Microsoft Azure, Terraform, Bash and "
        "GitHub Actions, with the goal of applying these technologies to automated, observable and secure delivery workflows.",
        body,
    ),
    Paragraph(
        "Capgemini's new Porto Tech Hub, international engineering environment and Career Acceleration Programs make this "
        "a particularly motivating opportunity. I would bring structured troubleshooting, hands-on development experience, "
        "curiosity and a continuous-improvement mindset while growing into a dependable DevOps engineer who contributes "
        "across development, testing and production environments.",
        body,
    ),
    Paragraph(
        "Thank you for considering my application. I would welcome the opportunity to discuss how my background and "
        "motivation could contribute to Capgemini and its mobility technology project.",
        body,
    ),
    KeepTogether([
        Paragraph("Yours faithfully,", body),
        Spacer(1, 1),
        Paragraph("Miguel Magalhães", signature),
    ]),
]


CoverLetter(str(OUTPUT)).build(story)
print(OUTPUT)
