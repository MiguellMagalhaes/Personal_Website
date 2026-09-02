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


OUTPUT = Path("output/pdf/Cover_Letter_Inetum_Service_Desk_Technician_Miguel_Magalhaes.pdf")


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Application for Service Desk Technician - Inetum Portugal")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Application for the Service Desk Technician position in Porto")

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
    draw_text_top(c, "Service Desk Technician - Porto", LEFT, 120.10, "Verdana", 10.1, MUTED)

    # Recipient block.
    box_top = 160.38
    box_bottom = 202.38
    c.setFillColor(BOX_FILL)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.rect(LEFT, PAGE_H - box_bottom, CONTENT_W, box_bottom - box_top, stroke=1, fill=1)
    draw_text_top(c, "Hiring Team", LEFT + 9.0, 169.26, "Verdana", 9.1, BODY)
    draw_text_top(c, "Inetum Portugal", LEFT + 9.0, 183.26, "Verdana", 9.1, BODY)

    draw_text_top(
        c,
        "Subject: Application for Service Desk Technician - Porto",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Dear Inetum Hiring Team,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "I am writing to apply for the Service Desk Technician position in Porto. Inetum's "
            "scale, client proximity and focus on practical digital services appeal to me because "
            "this role combines structured incident management with direct user support and service continuity."
        ),
        (
            "At NewCoffee, I provided first-line technical support to users across different "
            "departments and company locations. I diagnosed and resolved incidents involving "
            "hardware, software, user accounts, access permissions, printing, connectivity and "
            "business applications, while logging, monitoring and following support requests "
            "through to resolution."
        ),
        (
            "I prepared and maintained Windows desktops and laptops, printers, mobile devices and "
            "peripherals. I also created and managed accounts, groups and permissions through "
            "Active Directory, supported VPN and DHCP connectivity issues, and collaborated with "
            "external IT providers when an incident required escalation or specialist intervention."
        ),
        (
            "My previous support experience at Staples further developed my customer-facing "
            "troubleshooting skills. I learned to clarify the real problem, explain technical steps "
            "to non-technical users and remain calm, organised and solution-focused throughout the interaction."
        ),
        (
            "I also developed an internal ITSM platform for managing tickets, assets, users, "
            "departments and operational indicators. This gave me a broader understanding of ticket "
            "categorisation, prioritisation, accurate documentation and the importance of reliable "
            "records for efficient support. I take ownership of issues, communicate progress clearly "
            "and escalate with the relevant diagnostic information when necessary."
        ),
        (
            "I would welcome the opportunity to discuss how my service desk experience, methodical "
            "approach and user-oriented communication could contribute to Inetum and its clients."
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
        "Application - Service Desk Technician",
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
