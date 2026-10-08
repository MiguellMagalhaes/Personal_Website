from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "output"
    / "pdf"
    / "Cover_Letter_TeamViewer_Full_Stack_Software_Engineer_Miguel_Magalhaes.pdf"
)

NAVY = colors.HexColor("#173B62")
BLUE = colors.HexColor("#2E6DA4")
TEXT = colors.HexColor("#252A30")
MUTED = colors.HexColor("#5F6872")
LIGHT = colors.HexColor("#E7EEF5")


def register_fonts():
    pdfmetrics.registerFont(
        TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf")
    )
    pdfmetrics.registerFont(
        TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf")
    )


def draw_page(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, height - 9 * mm, width, 9 * mm, stroke=0, fill=1)
    canvas.setFillColor(BLUE)
    canvas.rect(0, 0, width, 3 * mm, stroke=0, fill=1)
    canvas.setStrokeColor(LIGHT)
    canvas.setLineWidth(0.7)
    canvas.line(20 * mm, 17 * mm, width - 20 * mm, 17 * mm)
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(20 * mm, 11.5 * mm, "Miguel Magalhães")
    canvas.drawRightString(
        width - 20 * mm,
        11.5 * mm,
        "Application - Full Stack Software Engineer",
    )
    canvas.restoreState()


def build_pdf():
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=22 * mm,
        rightMargin=22 * mm,
        topMargin=17 * mm,
        bottomMargin=22 * mm,
        title="Cover Letter - Full Stack Software Engineer | TeamViewer",
        author="Miguel Magalhães",
        subject="Application for Full Stack Software Engineer - React / Java Spring Boot",
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="main",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc.addPageTemplates([PageTemplate(id="letter", frames=[frame], onPage=draw_page)])

    styles = getSampleStyleSheet()
    name = ParagraphStyle(
        "Name",
        parent=styles["Normal"],
        fontName="Arial-Bold",
        fontSize=20,
        leading=23,
        textColor=NAVY,
        spaceAfter=2,
    )
    role = ParagraphStyle(
        "Role",
        parent=styles["Normal"],
        fontName="Arial",
        fontSize=9.2,
        leading=12,
        textColor=MUTED,
    )
    small = ParagraphStyle(
        "Small",
        parent=styles["Normal"],
        fontName="Arial",
        fontSize=8.4,
        leading=11.5,
        textColor=TEXT,
    )
    date_style = ParagraphStyle(
        "Date", parent=small, alignment=TA_LEFT, textColor=MUTED
    )
    subject = ParagraphStyle(
        "Subject",
        parent=styles["Normal"],
        fontName="Arial-Bold",
        fontSize=10.4,
        leading=13,
        textColor=NAVY,
        spaceAfter=7,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Arial",
        fontSize=9.0,
        leading=13.0,
        textColor=TEXT,
        alignment=TA_LEFT,
        spaceAfter=6.4,
    )
    body_bold = ParagraphStyle("BodyBold", parent=body, fontName="Arial-Bold")

    story = []
    header = Table(
        [
            [
                Paragraph("Miguel Magalhães", name),
                Paragraph("Porto, 27 September 2026", date_style),
            ],
            [
                Paragraph(
                    "Software Engineering · Full Stack Development · Systems &amp; Security",
                    role,
                ),
                "",
            ],
        ],
        colWidths=[112 * mm, 52 * mm],
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.append(header)
    story.append(Spacer(1, 4 * mm))

    contact = Table(
        [
            [
                Paragraph("<b>Phone</b><br/>(+351) 918 860 342", small),
                Paragraph(
                    "<b>Email</b><br/><link href='mailto:miguel.softeng@gmail.com' "
                    "color='#2E6DA4'>miguel.softeng@gmail.com</link>",
                    small,
                ),
                Paragraph(
                    "<b>Website</b><br/><link "
                    "href='https://miguelangelodiasmagalhaes.online' "
                    "color='#2E6DA4'>miguelangelodiasmagalhaes.online</link>",
                    small,
                ),
            ]
        ],
        colWidths=[43 * mm, 58 * mm, 63 * mm],
    )
    contact.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F7FA")),
                ("BOX", (0, 0), (-1, -1), 0.5, LIGHT),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, LIGHT),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(contact)
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph("TeamViewer Talent Acquisition Team", body_bold))
    story.append(
        Paragraph(
            "<b>Subject:</b> Application for Full Stack Software Engineer - "
            "React / Java Spring Boot",
            subject,
        )
    )
    story.append(Paragraph("Dear Hiring Team,", body))

    paragraphs = [
        "I am writing to apply for the <b>Full Stack Software Engineer - React / Java Spring Boot</b> position in Porto. TeamViewer's ambition to connect people with technology and the Frontline platform's combination of real-time workflows, mobile devices, smart glasses, and industrial use cases make this an especially compelling opportunity for me.",
        "I hold a degree in <b>Computer Engineering</b> and a Higher Professional Technical Diploma in Computer Networks and Systems. I am also pursuing a Master's degree in Cybersecurity and Computer Systems Auditing in an evening programme. This combination has given me a broad foundation across software development, databases, systems, networks, and secure engineering practices.",
        "Through academic, personal, and practical projects, I have worked with <b>Java, JavaScript, TypeScript, React, Node.js, relational databases, REST APIs, Git, and Docker</b>. I understand the importance of component-based interfaces, clear API contracts, data modelling, maintainable code, version control, and testing. I am continuing to deepen my knowledge of Spring Boot, distributed systems, CI/CD, and container-based delivery.",
        "I also designed and developed an internal <b>ITSM platform</b> to manage tickets, users, assets, and operational indicators. Building this solution required me to translate operational needs into data structures, application workflows, user-facing functionality, and reporting capabilities. It strengthened my ability to approach a problem end to end rather than viewing frontend, backend, and business requirements in isolation.",
        "During my experience with NewCoffee's Information Systems department, I supported users across different teams and locations, worked with business applications and databases, documented incidents, and collaborated with external providers. That environment developed my ownership, communication, prioritisation, and troubleshooting skills, as well as my awareness of the reliability and security expected from software used in real operations.",
        "I am particularly attracted to TeamViewer's emphasis on clean and testable code, architecture, peer reviews, pair programming, technical discussion, and individual ownership. I would welcome the opportunity to learn from an experienced engineering team while contributing curiosity, disciplined problem-solving, and a strong willingness to improve the platform across the full stack.",
        "Although I am at an earlier stage of my professional career than the experience range stated in the advertisement, I believe my technical education, practical breadth, project work, and learning capacity provide a strong foundation for growth. I communicate effectively in English at B2 level and am comfortable working in an international, hybrid environment in Porto.",
        "Thank you for considering my application. I would welcome the opportunity to discuss my projects, technical foundations, and motivation to contribute to the next generation of TeamViewer Frontline.",
    ]
    for paragraph in paragraphs:
        story.append(Paragraph(paragraph, body))

    story.append(
        KeepTogether(
            [
                Spacer(1, 1.5 * mm),
                Paragraph("Kind regards,", body),
                Paragraph("<b>Miguel Magalhães</b>", body),
            ]
        )
    )

    doc.build(story)
    print(OUTPUT)


if __name__ == "__main__":
    build_pdf()
