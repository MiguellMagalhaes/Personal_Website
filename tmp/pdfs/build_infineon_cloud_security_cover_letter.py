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


OUTPUT = Path("output/pdf/Cover_Letter_Infineon_Cloud_Security_Specialist_Miguel_Magalhaes.pdf")


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Application for Cloud Security Specialist - Infineon Technologies")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Application for the Cloud Security Specialist position in Maia")

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
    draw_text_top(c, "Cloud Security Specialist - Maia", LEFT, 120.10, "Verdana", 10.1, MUTED)

    # Recipient block.
    box_top = 160.38
    box_bottom = 202.38
    c.setFillColor(BOX_FILL)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.rect(LEFT, PAGE_H - box_bottom, CONTENT_W, box_bottom - box_top, stroke=1, fill=1)
    draw_text_top(c, "Talent Acquisition Team", LEFT + 9.0, 169.26, "Verdana", 9.1, BODY)
    draw_text_top(c, "Infineon Technologies", LEFT + 9.0, 183.26, "Verdana", 9.1, BODY)

    draw_text_top(
        c,
        "Subject: Application for Cloud Security Specialist - Maia",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Dear Infineon Hiring Team,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "I am writing to apply for the Cloud Security Specialist position in Maia. Infineon's "
            "work in secure IoT, efficient energy and digitalisation is especially meaningful to me, "
            "and I am motivated by the opportunity to help strengthen the controls that support "
            "trusted and resilient technology."
        ),
        (
            "I hold a degree in Computer Engineering and a Higher Professional Technical Course in "
            "Computer Networks and Systems, and I am currently pursuing a Master's in Cybersecurity "
            "and Computer Systems Auditing. My foundation includes Windows and Linux systems, Active "
            "Directory, Microsoft 365, network security, access management, log analysis, data "
            "protection and basic system hardening."
        ),
        (
            "At NewCoffee, I managed user accounts, groups, permissions and access rights, supported "
            "Windows endpoints, VPN services and network connectivity, and investigated incidents "
            "affecting users and business applications. I documented interventions, coordinated with "
            "external providers and translated technical findings into clear information for "
            "colleagues with different levels of technical knowledge."
        ),
        (
            "In an international network intrusion detection project, I configured isolated Linux "
            "environments, generated and analysed network traffic and worked with Wireshark, Snort "
            "and structured security logs. This experience reinforced a control-oriented approach: "
            "collect evidence, validate alerts, isolate causes, document findings and verify that "
            "changes improve security without disrupting legitimate activity."
        ),
        (
            "My current strength is the systems and security foundation behind effective cloud "
            "posture management. I am now deliberately deepening my knowledge of AWS, Azure and GCP "
            "security controls, CSPM, CIS benchmarks, compliance monitoring and automation. I am "
            "particularly interested in learning to configure and optimise platforms such as Wiz and "
            "CIS Security Suite beyond standard templates and to turn governance requirements into "
            "measurable technical controls."
        ),
        (
            "I would welcome the opportunity to discuss how my analytical approach, practical security "
            "background and commitment to continuous learning could contribute to Infineon's cloud security team."
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
        "Application - Cloud Security Specialist",
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
