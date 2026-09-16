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


OUTPUT = Path(
    "output/pdf/Carta_Apresentacao_IT_User_Support_Workplace_Infrastructure_Miguel_Magalhaes.pdf"
)


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Candidatura - IT User Support / Workplace Infrastructure")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Candidatura a uma posição de IT User Support no Porto")

    # Faixa superior e destaques.
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 39.69, PAGE_W, 39.69, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.rect(0, PAGE_H - 39.69, 130.39, 8.51, stroke=0, fill=1)
    c.setFillColor(BLUE)
    c.rect(130.39, PAGE_H - 39.69, 62.37, 8.51, stroke=0, fill=1)

    # Cabeçalho do candidato.
    draw_text_top(c, "CANDIDATURA", LEFT, 75.73, "Verdana-Bold", 8.2, TEAL)
    draw_text_top(c, "16 de setembro de 2026", RIGHT, 75.73, "Verdana", 8.7, MUTED, True)
    draw_text_top(c, "Miguel Magalhães", LEFT, 92.58, "Verdana-Bold", 22.0, NAVY)
    draw_text_top(c, "IT User Support / Workplace Infrastructure - Porto", LEFT, 120.10, "Verdana", 10.1, MUTED)

    # Destinatário genérico, uma vez que o anúncio não identifica a empresa.
    box_top = 160.38
    box_bottom = 202.38
    c.setFillColor(BOX_FILL)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.rect(LEFT, PAGE_H - box_bottom, CONTENT_W, box_bottom - box_top, stroke=1, fill=1)
    draw_text_top(c, "Equipa de Recrutamento", LEFT + 9.0, 169.26, "Verdana", 9.1, BODY)
    draw_text_top(c, "Porto", LEFT + 9.0, 183.26, "Verdana", 9.1, BODY)

    draw_text_top(
        c,
        "Assunto: Candidatura - IT User Support / Workplace Infrastructure",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Exmos. Senhores,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "Apresento a minha candidatura à oportunidade de IT User Support / Workplace Infrastructure "
            "no Porto. O suporte técnico L1/L2, a gestão de equipamentos e a colaboração com equipas de "
            "Infrastructure, Security e SysAdmin correspondem ao percurso que tenho vindo a construir em "
            "suporte, sistemas, redes e cibersegurança."
        ),
        (
            "Na NewCoffee, prestei suporte de primeira linha a utilizadores de diferentes departamentos e "
            "localizações, diagnosticando incidentes relacionados com equipamentos Windows, hardware, "
            "software, contas, permissões, impressão, VPN, DHCP, conectividade e aplicações empresariais. "
            "Trabalhei também com Active Directory, inventário e preparação de postos, acompanhando os pedidos "
            "até à resolução ou ao escalamento para fornecedores externos."
        ),
        (
            "Na Staples, reforcei a comunicação com utilizadores e o suporte a hardware, software, periféricos "
            "e sistemas de ponto de venda. Desenvolvi ainda uma plataforma interna de ITSM para centralizar "
            "tickets, ativos, utilizadores e indicadores, aprofundando a minha compreensão de prioridades, "
            "SLAs, documentação e rastreabilidade."
        ),
        (
            "Sou licenciado em Engenharia Informática, possuo um CTeSP em Redes e Sistemas Informáticos e "
            "frequento atualmente um mestrado em Cibersegurança e Auditoria de Sistemas, em regime pós-laboral. "
            "Tenho bases em Windows, Active Directory, Microsoft 365, hardware, TCP/IP, DNS, DHCP e VPN, além "
            "de automação com Python. Quero aprofundar PowerShell, macOS, SCCM, MDM e o suporte a Cisco e "
            "Microsoft Teams Rooms num ambiente empresarial estruturado."
        ),
        (
            "Embora a minha experiência seja mais recente do que os quatro anos indicados, as responsabilidades "
            "que já assumi estão alinhadas com a função. Investigo problemas por camadas, documento com rigor, "
            "comunico com utilizadores e equipas técnicas e aprendo rapidamente sem comprometer a segurança."
        ),
        (
            "Teria muito gosto em conversar sobre a forma como a minha experiência prática, responsabilidade e "
            "orientação para o utilizador poderão contribuir para a equipa e para os serviços de IT."
        ),
    ]

    top = 267.01
    for paragraph in paragraphs:
        top = draw_paragraph(c, paragraph, top)

    draw_text_top(c, "Com os melhores cumprimentos,", LEFT, top + 3.0, "Verdana", 9.3, BODY)
    draw_text_top(c, "Miguel Magalhães", LEFT, top + 31.3, "Verdana-Bold", 10.2, NAVY)

    # Rodapé.
    footer_y = PAGE_H - 790.87
    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    c.line(62.36, footer_y, 532.91, footer_y)
    draw_text_top(c, "Miguel Magalhães", 62.36, 802.25, "Verdana", 7.8, MUTED)
    draw_text_top(
        c,
        "Candidatura - IT User Support",
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
