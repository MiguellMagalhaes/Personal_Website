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


OUTPUT = Path("output/pdf/Carta_Apresentacao_Sysmatch_Junior_Service_Desk_Miguel_Magalhaes.pdf")


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Candidatura a Junior Service Desk - Sysmatch")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Candidatura a Junior Service Desk no Porto")

    # Faixa superior e segmentos de destaque.
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 39.69, PAGE_W, 39.69, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.rect(0, PAGE_H - 39.69, 130.39, 8.51, stroke=0, fill=1)
    c.setFillColor(BLUE)
    c.rect(130.39, PAGE_H - 39.69, 62.37, 8.51, stroke=0, fill=1)

    # Cabeçalho do candidato.
    draw_text_top(c, "CANDIDATURA", LEFT, 75.73, "Verdana-Bold", 8.2, TEAL)
    draw_text_top(c, "3 de setembro de 2026", RIGHT, 75.73, "Verdana", 8.7, MUTED, True)
    draw_text_top(c, "Miguel Magalhães", LEFT, 92.58, "Verdana-Bold", 22.0, NAVY)
    draw_text_top(c, "Junior Service Desk - Porto", LEFT, 120.10, "Verdana", 10.1, MUTED)

    # Bloco do destinatário.
    box_top = 160.38
    box_bottom = 202.38
    c.setFillColor(BOX_FILL)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.rect(LEFT, PAGE_H - box_bottom, CONTENT_W, box_bottom - box_top, stroke=1, fill=1)
    draw_text_top(c, "Equipa de Recrutamento", LEFT + 9.0, 169.26, "Verdana", 9.1, BODY)
    draw_text_top(c, "Sysmatch", LEFT + 9.0, 183.26, "Verdana", 9.1, BODY)

    draw_text_top(
        c,
        "Assunto: Candidatura à posição de Junior Service Desk - Porto",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Exmos. Senhores,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "Apresento a minha candidatura à posição de Junior Service Desk no Porto. A função está "
            "diretamente alinhada com a minha experiência em suporte a utilizadores, sistemas Microsoft, "
            "Active Directory, equipamentos informáticos e resolução estruturada de incidentes."
        ),
        (
            "Na NewCoffee, prestei suporte técnico de primeira linha a utilizadores de diferentes "
            "departamentos e localizações. Diagnostiquei e resolvi incidentes de hardware, software, "
            "contas, acessos, impressão, conectividade e aplicações empresariais, mantendo os pedidos "
            "registados e acompanhados até à respetiva resolução ou escalamento."
        ),
        (
            "Preparei e mantive computadores Windows, portáteis, impressoras, dispositivos móveis e "
            "periféricos. Criei e geri utilizadores, grupos, passwords e permissões em Active Directory, "
            "apoiei serviços Microsoft 365 e tratei problemas de VPN, DHCP, DNS, TCP/IP e acesso remoto. "
            "Quando necessário, articulei a resolução com fornecedores externos, partilhando informação "
            "de diagnóstico clara e relevante."
        ),
        (
            "A minha experiência anterior de suporte na Staples reforçou a comunicação com utilizadores "
            "e a capacidade de explicar procedimentos técnicos de forma simples. Trabalho com organização, "
            "defino prioridades de acordo com o impacto e a urgência e mantenho uma postura calma, responsável "
            "e orientada para a solução. Possuo nível B2 de inglês e estou preparado para apoiar utilizadores "
            "internacionais e consultar documentação técnica."
        ),
        (
            "Desenvolvi também uma plataforma interna de ITSM para gestão de tickets, ativos, utilizadores, "
            "departamentos e indicadores operacionais. Este projeto aprofundou a minha compreensão da "
            "categorização e priorização de incidentes, cumprimento de processos, qualidade dos registos, "
            "gestão de inventário e manutenção de conhecimento técnico reutilizável."
        ),
        (
            "Sou licenciado em Engenharia Informática, possuo formação técnica superior em Redes e Sistemas "
            "Informáticos e frequento atualmente um mestrado em Cibersegurança e Auditoria de Sistemas. "
            "Esta formação complementa a experiência prática com conhecimentos de segurança, MFA, boas "
            "práticas de autenticação, redes e proteção dos sistemas de informação."
        ),
        (
            "Gostaria de contribuir desde o primeiro dia com a minha experiência em suporte e, simultaneamente, "
            "continuar a evoluir em Microsoft 365, gestão de dispositivos e processos de Service Desk num projeto "
            "internacional da Sysmatch. Terei muito gosto em aprofundar esta candidatura numa entrevista."
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
        "Candidatura - Junior Service Desk",
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
