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


OUTPUT = Path("output/pdf/Cover_Letter_DBServices_Machine_Learning_Data_Engineer_Miguel_Magalhaes.pdf")


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Application for Machine Learning Engineer | Data Engineer - DBServices Portugal")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Application for the Machine Learning Engineer | Data Engineer position in Porto")

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
    draw_text_top(
        c,
        "Machine Learning Engineer | Data Engineer - Porto",
        LEFT,
        120.10,
        "Verdana",
        10.1,
        MUTED,
    )

    # Recipient block.
    box_top = 160.38
    box_bottom = 202.38
    c.setFillColor(BOX_FILL)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.rect(LEFT, PAGE_H - box_bottom, CONTENT_W, box_bottom - box_top, stroke=1, fill=1)
    draw_text_top(c, "Hiring Team", LEFT + 9.0, 169.26, "Verdana", 9.1, BODY)
    draw_text_top(c, "DBServices Portugal", LEFT + 9.0, 183.26, "Verdana", 9.1, BODY)

    draw_text_top(
        c,
        "Subject: Application for Machine Learning Engineer | Data Engineer - Porto",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Dear DBServices Hiring Team,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "I am writing to apply for the Machine Learning Engineer | Data Engineer position in "
            "Porto. DBServices' work in digital transformation, cloud, DevOps and rapid "
            "prototyping is particularly appealing to me because it connects software engineering "
            "discipline with the delivery of practical, production-oriented solutions."
        ),
        (
            "I hold a degree in Computer Engineering and a Higher Professional Technical Course "
            "in Computer Networks and Systems, and I am currently pursuing a Master's in "
            "Cybersecurity and Computer Systems Auditing. My technical foundation includes Python, "
            "SQL, PostgreSQL, Microsoft SQL Server, REST APIs, Git, Linux, data modelling and "
            "automation, supported by experience building applications that depend on reliable data flows."
        ),
        (
            "In an international COIL project on network intrusion detection, I helped configure "
            "isolated test environments, generate and capture network traffic, structure logs and "
            "prepare datasets for preprocessing and model evaluation. Using Python, pandas, NumPy "
            "and scikit-learn, I worked with KNN, SVM, decision trees and Random Forest, gaining a "
            "practical understanding of the data lifecycle surrounding machine learning workflows."
        ),
        (
            "At Aquário Eletrónica, I developed Python scripts for web scraping, data collection "
            "and task automation, while supporting SQL Server administration and its integration "
            "with Primavera ERP. At NewCoffee, I built an ITSM platform that combined ticket, asset, "
            "user and operational data through SQL Server, REST APIs and dashboards. These projects "
            "strengthened my approach to validation, traceability, documentation and systematic troubleshooting."
        ),
        (
            "My experience spans software, data, systems and cybersecurity, and I am now deliberately "
            "focusing on the engineering side of data and machine learning. I am motivated to deepen "
            "hands-on experience with Spark, Databricks, Airflow, MLflow, Kafka, Delta Lake, Azure "
            "ADLS and Azure DevOps, building on my current strengths in Python, SQL, APIs, Git and "
            "technical problem-solving."
        ),
        (
            "I would welcome the opportunity to discuss how my practical foundation, curiosity and "
            "disciplined approach could contribute to DBServices and to reliable data and machine "
            "learning platforms for its clients."
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
        "Application - Machine Learning | Data Engineer",
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
