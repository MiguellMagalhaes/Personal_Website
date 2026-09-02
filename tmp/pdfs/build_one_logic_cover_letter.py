from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


OUTPUT = Path("output/pdf/Cover_Letter_One_Logic_Data_Engineer_Junior_Miguel_Magalhaes.pdf")

PAGE_W, PAGE_H = A4
LEFT = 68.03
RIGHT = 527.24
CONTENT_W = RIGHT - LEFT

FONT_REGULAR_PATH = "/System/Library/Fonts/Supplemental/Verdana.ttf"
FONT_BOLD_PATH = "/System/Library/Fonts/Supplemental/Verdana Bold.ttf"

NAVY = HexColor("#15334A")
BODY = HexColor("#2B394B")
MUTED = HexColor("#66778B")
TEAL = HexColor("#1AA7A1")
BLUE = HexColor("#3C86C8")
BOX_FILL = HexColor("#EAF7F6")
RULE = HexColor("#D3E5E4")


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("Verdana", FONT_REGULAR_PATH))
    pdfmetrics.registerFont(TTFont("Verdana-Bold", FONT_BOLD_PATH))


def baseline_for_top(top: float, font_name: str, font_size: float) -> float:
    ascent, _ = pdfmetrics.getAscentDescent(font_name, font_size)
    return PAGE_H - top - ascent


def draw_text_top(
    c: canvas.Canvas,
    text: str,
    x: float,
    top: float,
    font_name: str,
    font_size: float,
    color,
    right_aligned: bool = False,
) -> None:
    c.setFont(font_name, font_size)
    c.setFillColor(color)
    y = baseline_for_top(top, font_name, font_size)
    if right_aligned:
        c.drawRightString(x, y, text)
    else:
        c.drawString(x, y, text)


def wrap_lines(text: str, font_name: str, font_size: float, width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if pdfmetrics.stringWidth(candidate, font_name, font_size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_paragraph(
    c: canvas.Canvas,
    text: str,
    top: float,
    font_name: str = "Verdana",
    font_size: float = 9.3,
    leading: float = 14.55,
    color=BODY,
    space_after: float = 8.4,
) -> float:
    lines = wrap_lines(text, font_name, font_size, CONTENT_W)
    c.setFont(font_name, font_size)
    c.setFillColor(color)
    ascent, _ = pdfmetrics.getAscentDescent(font_name, font_size)
    first_baseline = PAGE_H - top - ascent
    for index, line in enumerate(lines):
        c.drawString(LEFT, first_baseline - index * leading, line)
    return top + len(lines) * leading + space_after


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Application for Data Engineer Junior - One Logic Consulting")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Application for the Data Engineer Junior position in Porto")

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
    draw_text_top(c, "Data Engineer Junior - Porto", LEFT, 120.10, "Verdana", 10.1, MUTED)

    # Recipient block.
    box_top = 160.38
    box_bottom = 202.38
    c.setFillColor(BOX_FILL)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.rect(LEFT, PAGE_H - box_bottom, CONTENT_W, box_bottom - box_top, stroke=1, fill=1)
    draw_text_top(c, "Hiring Team", LEFT + 9.0, 169.26, "Verdana", 9.1, BODY)
    draw_text_top(c, "One Logic Consulting", LEFT + 9.0, 183.26, "Verdana", 9.1, BODY)

    draw_text_top(
        c,
        "Subject: Application for Data Engineer Junior - Porto",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Dear One Logic Hiring Team,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "I am writing to apply for the Data Engineer Junior position in Porto. One Logic's "
            "developer-led culture, current engineering practices and commitment to continuous "
            "learning appeal to me as I build my career around data and reliable software."
        ),
        (
            "I hold a degree in Computer Engineering and a Higher Professional Technical Course "
            "in Computer Networks and Systems, and I am currently pursuing a Master's in "
            "Cybersecurity and Computer Systems Auditing. My practical foundation includes Python, "
            "SQL, Microsoft SQL Server, MySQL, PostgreSQL, REST APIs, data modelling and Git."
        ),
        (
            "At Aquário Eletrónica, I developed Python scripts for web scraping, data collection "
            "and task automation, while supporting SQL Server administration and its integration "
            "with Primavera ERP. More recently, I built an internal ITSM platform that brought "
            "together data on tickets, assets, users, departments and operational indicators "
            "through SQL Server and dashboards. These projects required structured data modelling, "
            "validation, query work, integration logic and clear documentation."
        ),
        (
            "I also developed and deployed a healthcare appointment platform in which reliable "
            "database operations, API integrations and validation rules were essential. "
            "Investigating inconsistent records and integration failures strengthened my habit of "
            "tracing issues methodically, checking assumptions and confirming outcomes through "
            "tests and technical evidence."
        ),
        (
            "My path combines software, databases, systems and support, giving me a broad view of "
            "how data moves through real applications and operations. I am now deliberately "
            "specialising in data engineering, building on a practical base in Python, SQL, "
            "integrations, data quality and "
            "troubleshooting. I am particularly motivated to deepen hands-on experience with "
            "Apache Flink, Apache Iceberg, AWS data services, orchestration and large-scale pipelines."
        ),
        (
            "I would welcome the opportunity to discuss how my technical foundation, curiosity and "
            "sense of responsibility could contribute to One Logic and its financial-services client."
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
        "Application - Data Engineer Junior",
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
