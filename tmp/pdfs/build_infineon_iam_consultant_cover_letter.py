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


OUTPUT = Path("output/pdf/Cover_Letter_Infineon_Cyber_Security_Consultant_IAM_Miguel_Magalhaes.pdf")


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Application for Cyber Security Consultant - Identity and Access Management")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Application for the Cyber Security Consultant - IAM position in Maia")

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
    draw_text_top(c, "Cyber Security Consultant - IAM | Maia", LEFT, 120.10, "Verdana", 10.1, MUTED)

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
        "Subject: Application for Cyber Security Consultant - IAM",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Dear Infineon Hiring Team,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "I am writing to apply for the Cyber Security Consultant - Identity and Access "
            "Management position. The opportunity to help shape secure identity services, access "
            "controls and consistent IAM standards across Infineon's global technology environment "
            "is closely aligned with the direction in which I am developing my career."
        ),
        (
            "I hold a degree in Computer Engineering and a Higher Professional Technical Course in "
            "Computer Networks and Systems, and I am currently pursuing a Master's in Cybersecurity "
            "and Computer Systems Auditing. My foundation includes Active Directory, Windows and "
            "Linux systems, Microsoft 365, network security, access management, authentication, data "
            "protection, log analysis and basic system hardening."
        ),
        (
            "At NewCoffee, I created and managed user accounts, groups, permissions and access rights "
            "through Active Directory and internal systems. I supported access incidents affecting "
            "business applications, VPN services and company resources, documented interventions and "
            "worked with users and external providers to restore access while preserving appropriate "
            "controls and operational continuity."
        ),
        (
            "My software projects have also involved authentication, REST APIs, database operations "
            "and validation of user-facing workflows. In an international intrusion detection project, "
            "I configured isolated Linux environments, analysed network traffic and security logs and "
            "validated alerts with Wireshark and Snort. These experiences strengthened my ability to "
            "reason about trust boundaries, evidence, risk and secure system behaviour."
        ),
        (
            "My strongest practical IAM foundation is currently Active Directory and day-to-day "
            "access administration. I am deliberately expanding it towards Entra ID, identity "
            "lifecycle management, privileged and just-in-time access, federation, token-based "
            "authentication, workload identity and Zero Trust. I am also motivated to deepen my "
            "practice in threat modelling, secure design reviews and the translation of NIST and "
            "ISO-based requirements into effective technical controls."
        ),
        (
            "I would welcome the opportunity to discuss how my practical identity and systems "
            "background, analytical approach and commitment to continuous learning could contribute "
            "to Infineon's Corporate Cyber Security and Privacy team."
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
        "Application - Cyber Security Consultant | IAM",
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
