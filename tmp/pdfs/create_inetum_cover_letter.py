from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    KeepTogether,
)


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "pdf" / "Cover_Letter_Miguel_Magalhaes_Inetum.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)


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
NAVY = colors.HexColor("#17324D")
TEAL = colors.HexColor("#00A6A6")
INK = colors.HexColor("#263442")
MUTED = colors.HexColor("#607080")
PALE = colors.HexColor("#E8F4F4")


class LetterDocTemplate(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=A4,
            rightMargin=21 * mm,
            leftMargin=21 * mm,
            topMargin=18 * mm,
            bottomMargin=17 * mm,
            title="Cover Letter - Miguel Magalhães - Inetum",
            author="Miguel Magalhães",
            subject="Application for Desktop Support Technician",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="letter",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(PageTemplate(id="main", frames=[frame], onPage=self.decorate))

    def decorate(self, canvas, doc):
        width, height = A4
        canvas.saveState()
        canvas.setFillColor(NAVY)
        canvas.rect(0, height - 7 * mm, width, 7 * mm, stroke=0, fill=1)
        canvas.setFillColor(TEAL)
        canvas.rect(0, height - 8.5 * mm, width, 1.5 * mm, stroke=0, fill=1)
        canvas.setStrokeColor(colors.HexColor("#CBD5DF"))
        canvas.setLineWidth(0.5)
        canvas.line(21 * mm, 13 * mm, width - 21 * mm, 13 * mm)
        canvas.setFont(REGULAR, 7.6)
        canvas.setFillColor(MUTED)
        canvas.drawString(21 * mm, 8.8 * mm, "Miguel Magalhães | Desktop Support Technician")
        canvas.drawRightString(width - 21 * mm, 8.8 * mm, "Porto, Portugal")
        canvas.restoreState()


styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name",
    fontName=BOLD,
    fontSize=22,
    leading=25,
    textColor=NAVY,
    spaceAfter=2,
)

role_style = ParagraphStyle(
    "Role",
    fontName=REGULAR,
    fontSize=10.5,
    leading=13,
    textColor=TEAL,
    spaceAfter=5,
)

contact_style = ParagraphStyle(
    "Contact",
    fontName=REGULAR,
    fontSize=8.5,
    leading=12,
    textColor=MUTED,
    spaceAfter=8,
)

meta_style = ParagraphStyle(
    "Meta",
    fontName=REGULAR,
    fontSize=9.2,
    leading=13,
    textColor=INK,
    spaceAfter=1,
)

subject_style = ParagraphStyle(
    "Subject",
    fontName=BOLD,
    fontSize=11.5,
    leading=15,
    textColor=NAVY,
    backColor=PALE,
    borderPadding=(6, 8, 6, 8),
    spaceBefore=9,
    spaceAfter=11,
)

body_style = ParagraphStyle(
    "Body",
    fontName=REGULAR,
    fontSize=9.45,
    leading=13.35,
    textColor=INK,
    alignment=TA_LEFT,
    spaceAfter=7.5,
)

salutation_style = ParagraphStyle(
    "Salutation",
    parent=body_style,
    spaceAfter=8,
)

signature_style = ParagraphStyle(
    "Signature",
    fontName=BOLD,
    fontSize=10,
    leading=13,
    textColor=NAVY,
    spaceBefore=1,
)


story = [
    Paragraph("Miguel Magalhães", name_style),
    Paragraph("Computer Engineering Graduate | IT Support and Systems", role_style),
    Paragraph(
        "Valongo, Portugal &nbsp;&nbsp;|&nbsp;&nbsp; (+351) 918 860 342 &nbsp;&nbsp;|&nbsp;&nbsp; "
        "miguel.softeng@gmail.com<br/>"
        "miguelangelodiasmagalhaes.online",
        contact_style,
    ),
    HRFlowable(width="100%", thickness=1.1, color=TEAL, spaceBefore=0, spaceAfter=10),
    Paragraph("5 October 2026", meta_style),
    Spacer(1, 4),
    Paragraph("Hiring Team", meta_style),
    Paragraph("Inetum", meta_style),
    Paragraph("Porto, Portugal", meta_style),
    Paragraph("APPLICATION FOR DESKTOP SUPPORT TECHNICIAN", subject_style),
    Paragraph("Dear Hiring Team,", salutation_style),
    Paragraph(
        "I am writing to apply for the Desktop Support Technician position at Inetum. "
        "With a degree in Computer Engineering, technical training in Computer Networks and Systems, "
        "and practical experience in end-user support, incident management and workplace technologies, "
        "I believe my background is strongly aligned with this role.",
        body_style,
    ),
    Paragraph(
        "At NewCoffee, I provided first-line technical support to hundreds of users across five locations, "
        "handling approximately 20 to 40 daily requests. I diagnosed and resolved hardware, software, account, "
        "access, printing and connectivity incidents; prepared Windows computers and mobile devices; and supported "
        "corporate applications and network services. I also installed software, managed user accounts and permissions, "
        "and escalated cases to internal teams or external providers when additional intervention was required.",
        body_style,
    ),
    Paragraph(
        "I also contributed to an internal ITSM and asset-management platform used to organize incidents, requests, "
        "users, equipment and operational information. This strengthened my ability to document troubleshooting steps, "
        "maintain asset records, prioritize requests and follow incidents through to resolution. My previous positions "
        "at Staples EasyTech and Aquário Eletrónica further developed my customer-service skills and hands-on experience "
        "supporting and configuring end-user equipment.",
        body_style,
    ),
    Paragraph(
        "I work effectively both independently and with technical teams, and I communicate clearly with users at "
        "different levels of technical knowledge. I am motivated to deepen my experience with ServiceNow, macOS and "
        "enterprise support practices. My current Master's degree in Cybersecurity and Computer Systems Auditing also "
        "reinforces my awareness of security, access control and responsible handling of organizational information.",
        body_style,
    ),
    Paragraph(
        "I am available to work on-site in Porto, support different office locations and participate in shift rotations "
        "when required. I would welcome the opportunity to contribute my technical knowledge, customer-oriented approach "
        "and commitment to continuous improvement to Inetum.",
        body_style,
    ),
    Paragraph(
        "Thank you for considering my application. I would be pleased to discuss my experience and motivation in an interview.",
        body_style,
    ),
    KeepTogether([
        Paragraph("Yours faithfully,", body_style),
        Spacer(1, 1),
        Paragraph("Miguel Magalhães", signature_style),
    ]),
]


doc = LetterDocTemplate(str(OUT))
doc.build(story)
print(OUT)
