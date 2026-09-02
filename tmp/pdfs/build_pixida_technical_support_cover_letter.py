from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from build_one_logic_cover_letter import (
    BLUE,
    BODY,
    BOX_FILL,
    CONTENT_W,
    LEFT,
    MUTED,
    NAVY,
    PAGE_H,
    PAGE_W,
    RIGHT,
    RULE,
    TEAL,
    draw_paragraph,
    draw_text_top,
    register_fonts,
)


OUTPUT = Path("output/pdf/Cover_Letter_Pixida_Technical_Support_Engineer_Miguel_Magalhaes.pdf")


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Application for Technical Support Engineer - Pixida")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Application for the Technical Support Engineer position in Porto")

    # Header band and accent segments.
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 39.69, PAGE_W, 39.69, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.rect(0, PAGE_H - 39.69, 130.39, 8.51, stroke=0, fill=1)
    c.setFillColor(BLUE)
    c.rect(130.39, PAGE_H - 39.69, 62.37, 8.51, stroke=0, fill=1)

    # Candidate header.
    draw_text_top(c, "APPLICATION", LEFT, 75.73, "Verdana-Bold", 8.2, TEAL)
    draw_text_top(c, "2 September 2026", RIGHT, 75.73, "Verdana", 8.7, MUTED, True)
    draw_text_top(c, "Miguel Magalhães", LEFT, 92.58, "Verdana-Bold", 22.0, NAVY)
    draw_text_top(c, "Technical Support Engineer - Porto", LEFT, 120.10, "Verdana", 10.1, MUTED)

    # Recipient block.
    box_top = 160.38
    box_bottom = 202.38
    c.setFillColor(BOX_FILL)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.rect(LEFT, PAGE_H - box_bottom, CONTENT_W, box_bottom - box_top, stroke=1, fill=1)
    draw_text_top(c, "Marc Ehlerding and the Hiring Team", LEFT + 9.0, 169.26, "Verdana", 9.1, BODY)
    draw_text_top(c, "Pixida Portugal", LEFT + 9.0, 183.26, "Verdana", 9.1, BODY)

    draw_text_top(
        c,
        "Subject: Application for Technical Support Engineer - Porto",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Dear Pixida Hiring Team,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "I am writing to apply for the Technical Support Engineer position in Porto. "
            "The opportunity to support Teleservices and aftersales features for upcoming vehicle "
            "generations strongly appeals to me because it combines production support, structured "
            "incident analysis, technical coordination and continuous learning in a technology-driven environment."
        ),
        (
            "I hold a Bachelor's degree in Computer Engineering and a Higher Professional Technical "
            "Course in Computer Networks and Systems, and I am currently pursuing a Master's degree "
            "in Cybersecurity and Computer Systems Auditing. My background combines IT support, "
            "systems, networks, databases and software development."
        ),
        (
            "At NewCoffee, I provided first-line support across departments and company locations, "
            "diagnosing hardware, software, access, connectivity and business-application incidents. "
            "I managed users, groups and permissions in Active Directory, maintained Windows equipment, "
            "documented support requests and coordinated escalations with external IT providers until resolution."
        ),
        (
            "I also developed an internal ITSM platform for tickets, assets, users and operational "
            "indicators. Built with React, PHP and Microsoft SQL Server, it strengthened my understanding "
            "of incident categorisation, KPI visibility, data quality, process documentation and the "
            "importance of reliable technical records in day-to-day operations."
        ),
        (
            "My technical foundation includes SQL, Python and Java, together with TCP/IP, DNS, DHCP and "
            "connectivity troubleshooting. In an international network-security project, I used Wireshark "
            "and tcpdump to capture and analyse traffic and Snort to validate alerts, reinforcing a "
            "methodical, evidence-based approach to trace analysis and root-cause investigation."
        ),
        (
            "I am keen to apply this experience to automotive telematics and to learn Pixida's systems, "
            "market configurations and support processes. I am available to start immediately. Portuguese "
            "is my native language and my English level is B2, with confidence in technical documentation "
            "and international collaboration. My salary expectation is EUR 25,000-27,000 gross per year, "
            "negotiable according to the overall package and responsibilities."
        ),
        (
            "I would welcome the opportunity to discuss how my support experience, technical versatility "
            "and sense of ownership could contribute to Pixida's team and customers."
        ),
    ]

    top = 267.01
    for paragraph in paragraphs:
        top = draw_paragraph(c, paragraph, top)

    draw_text_top(c, "Kind regards,", LEFT, top + 3.0, "Verdana", 9.3, BODY)
    draw_text_top(c, "Miguel Magalhães", LEFT, top + 31.3, "Verdana-Bold", 10.2, NAVY)

    # Footer.
    footer_y = PAGE_H - 790.87
    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    c.line(62.36, footer_y, 532.91, footer_y)
    draw_text_top(c, "Miguel Magalhães", 62.36, 802.25, "Verdana", 7.8, MUTED)
    draw_text_top(
        c,
        "Application - Technical Support Engineer",
        532.91,
        802.25,
        "Verdana",
        7.8,
        MUTED,
        True,
    )

    c.showPage()
    c.save()


if __name__ == "__main__":
    build()
