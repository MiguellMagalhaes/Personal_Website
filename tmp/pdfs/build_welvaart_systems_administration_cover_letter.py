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


OUTPUT = Path("output/pdf/Carta_Apresentacao_Welvaart_Administracao_Sistemas_Miguel_Magalhaes.pdf")


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Candidatura a Administracao de Sistemas - Welvaart")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Candidatura a Administracao de Sistemas no Porto")

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
    draw_text_top(c, "Administração de Sistemas - Porto", LEFT, 120.10, "Verdana", 10.1, MUTED)

    # Bloco do destinatário.
    box_top = 160.38
    box_bottom = 202.38
    c.setFillColor(BOX_FILL)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.rect(LEFT, PAGE_H - box_bottom, CONTENT_W, box_bottom - box_top, stroke=1, fill=1)
    draw_text_top(c, "Equipa de Recrutamento", LEFT + 9.0, 169.26, "Verdana", 9.1, BODY)
    draw_text_top(c, "Welvaart", LEFT + 9.0, 183.26, "Verdana", 9.1, BODY)

    draw_text_top(
        c,
        "Assunto: Candidatura à posição de Administração de Sistemas - Porto",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Exmos. Senhores,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "Apresento a minha candidatura à posição de Administração de Sistemas no Porto. "
            "A oportunidade interessa-me pela combinação entre sistemas Microsoft, gestão de "
            "identidades, redes e segurança, áreas diretamente relacionadas com a minha formação "
            "e com a experiência prática que desenvolvi em suporte e infraestrutura informática."
        ),
        (
            "Na NewCoffee, prestei suporte técnico de primeira linha a utilizadores de diferentes "
            "departamentos e localizações. Administrei contas, grupos, acessos e permissões em "
            "Active Directory, preparei e mantive computadores Windows, portáteis, impressoras e "
            "dispositivos móveis e acompanhei incidentes de software, conectividade e aplicações "
            "empresariais até à sua resolução ou escalamento."
        ),
        (
            "Trabalhei também com Microsoft 365, VPN, DHCP, acesso remoto e inventário de ativos, "
            "colaborando com fornecedores externos em ocorrências que exigiam intervenção especializada. "
            "Este contacto diário com utilizadores e sistemas reforçou a minha capacidade de diagnóstico, "
            "documentação, priorização e comunicação em situações com impacto operacional."
        ),
        (
            "Desenvolvi ainda uma plataforma interna de ITSM para gestão de tickets, ativos, utilizadores "
            "e indicadores de suporte. O projeto aprofundou a minha compreensão da rastreabilidade das "
            "intervenções, controlo de acessos, consistência da informação técnica e melhoria contínua "
            "dos processos de suporte e administração."
        ),
        (
            "Sou licenciado em Engenharia Informática, possuo um Curso Técnico Superior Profissional em "
            "Redes e Sistemas Informáticos e frequento atualmente um mestrado em Cibersegurança e Auditoria "
            "de Sistemas Informáticos. Embora o meu percurso profissional ainda não totalize os cinco anos "
            "indicados, ofereço experiência diretamente aplicável em Windows, Active Directory, Microsoft 365 "
            "e redes, bem como bases sólidas de segurança, backups e recuperação."
        ),
        (
            "Pretendo aprofundar, em contexto empresarial, a administração de Windows Server e a utilização "
            "de Veeam, Symantec Endpoint Protection e FortiGate. Aprendo novas ferramentas com rapidez, trabalho "
            "de forma responsável e metódica e identifico-me com os valores de profissionalismo, honestidade e "
            "rigor que a Welvaart apresenta."
        ),
        (
            "Teria muito gosto em conversar sobre a forma como a minha experiência, formação técnica e vontade "
            "de evoluir podem contribuir para a Welvaart e para os projetos dos seus clientes."
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
        "Candidatura - Administração de Sistemas",
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
