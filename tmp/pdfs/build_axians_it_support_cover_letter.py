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


OUTPUT = Path("output/pdf/Carta_Apresentacao_Axians_IT_Support_Miguel_Magalhaes.pdf")


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Candidatura a IT Support - Axians Portugal")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Candidatura à posição de IT Support no Porto")

    # Faixa superior e segmentos de destaque.
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 39.69, PAGE_W, 39.69, stroke=0, fill=1)
    c.setFillColor(TEAL)
    c.rect(0, PAGE_H - 39.69, 130.39, 8.51, stroke=0, fill=1)
    c.setFillColor(BLUE)
    c.rect(130.39, PAGE_H - 39.69, 62.37, 8.51, stroke=0, fill=1)

    # Cabeçalho do candidato.
    draw_text_top(c, "CANDIDATURA", LEFT, 75.73, "Verdana-Bold", 8.2, TEAL)
    draw_text_top(c, "2 de setembro de 2026", RIGHT, 75.73, "Verdana", 8.7, MUTED, True)
    draw_text_top(c, "Miguel Magalhães", LEFT, 92.58, "Verdana-Bold", 22.0, NAVY)
    draw_text_top(c, "IT Support - Porto", LEFT, 120.10, "Verdana", 10.1, MUTED)

    # Bloco do destinatário.
    box_top = 160.38
    box_bottom = 202.38
    c.setFillColor(BOX_FILL)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.rect(LEFT, PAGE_H - box_bottom, CONTENT_W, box_bottom - box_top, stroke=1, fill=1)
    draw_text_top(c, "Equipa de Recrutamento", LEFT + 9.0, 169.26, "Verdana", 9.1, BODY)
    draw_text_top(c, "Axians Portugal", LEFT + 9.0, 183.26, "Verdana", 9.1, BODY)

    draw_text_top(
        c,
        "Assunto: Candidatura à posição de IT Support - Porto",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Exmos. Senhores,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "Apresento a minha candidatura à posição de IT Support no Porto. A combinação entre "
            "suporte técnico, gestão de identidades e segurança digital corresponde diretamente à "
            "minha experiência e ao percurso que estou a desenvolver na área de sistemas e cibersegurança."
        ),
        (
            "Na NewCoffee, prestei suporte informático de primeira linha a utilizadores de diferentes "
            "departamentos e localizações. Diagnostiquei e resolvi incidentes de hardware, software, "
            "contas, permissões, impressão, conectividade e aplicações empresariais, registando, "
            "acompanhando e documentando os pedidos até à respetiva resolução ou encaminhamento."
        ),
        (
            "Preparei e mantive computadores Windows, portáteis, impressoras, dispositivos móveis e "
            "periféricos. Criei e geri contas, grupos e direitos de acesso em Active Directory, apoiei "
            "serviços de VPN, DHCP e acesso remoto e colaborei com fornecedores externos sempre que "
            "um incidente exigia escalamento ou intervenção especializada."
        ),
        (
            "Desenvolvi também uma plataforma interna de ITSM para gerir tickets, ativos, utilizadores, "
            "departamentos e indicadores operacionais. Este trabalho reforçou a minha compreensão da "
            "categorização e priorização de incidentes, do controlo de inventário, da rastreabilidade das "
            "intervenções e da importância de manter informação técnica rigorosa e atualizada."
        ),
        (
            "Sou licenciado em Engenharia Informática, possuo formação técnica em Redes e Sistemas "
            "Informáticos e frequento atualmente um mestrado em Cibersegurança e Auditoria de Sistemas. "
            "Quero agora aprofundar a administração de Azure AD, Intune, SCCM e GPO, bem como MFA, "
            "acesso condicional e reporting de conformidade, apoiado por bases sólidas em Windows, "
            "Active Directory, Microsoft 365, redes, controlo de acessos e resolução de incidentes."
        ),
        (
            "Teria muito gosto em conversar sobre a forma como a minha experiência prática, sentido de "
            "responsabilidade e comunicação orientada para o utilizador podem contribuir para a Axians e os seus clientes."
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
        "Candidatura - IT Support",
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
