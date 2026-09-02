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


OUTPUT = Path("output/pdf/Carta_Apresentacao_Empatias_Administrativo_Sistema_Primavera_Miguel_Magalhaes.pdf")


def build() -> None:
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Candidatura a Administrativo/a Sistema Primavera - Empatias")
    c.setAuthor("Miguel Magalhães")
    c.setSubject("Candidatura à função de Administrativo/a Sistema Primavera no Porto")

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
    draw_text_top(c, "Administrativo | Sistema Primavera - Porto", LEFT, 120.10, "Verdana", 10.1, MUTED)

    # Bloco do destinatário.
    box_top = 160.38
    box_bottom = 202.38
    c.setFillColor(BOX_FILL)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.rect(LEFT, PAGE_H - box_bottom, CONTENT_W, box_bottom - box_top, stroke=1, fill=1)
    draw_text_top(c, "Exma. Senhora Isabel Santos", LEFT + 9.0, 169.26, "Verdana", 9.1, BODY)
    draw_text_top(c, "Empatias", LEFT + 9.0, 183.26, "Verdana", 9.1, BODY)

    draw_text_top(
        c,
        "Assunto: Candidatura - Administrativo/a sistema Primavera",
        LEFT,
        218.68,
        "Verdana-Bold",
        10.3,
        NAVY,
    )
    draw_text_top(c, "Exma. Senhora Isabel Santos,", LEFT, 243.81, "Verdana", 9.3, BODY)

    paragraphs = [
        (
            "Apresento a minha candidatura à função de Administrativo/a sistema Primavera, no Porto, "
            "referente ao anúncio com a referência 15814860. A oportunidade interessa-me por combinar "
            "organização administrativa, tratamento rigoroso de informação e utilização de ferramentas "
            "informáticas de gestão."
        ),
        (
            "Durante o meu estágio na Aquário Eletrónica, trabalhei com Microsoft SQL Server e apoiei "
            "a sua integração com o ERP Primavera. Esta experiência permitiu-me compreender a relação "
            "entre os dados do sistema, os processos empresariais e a necessidade de manter informação "
            "coerente, atualizada e corretamente documentada."
        ),
        (
            "Na NewCoffee, para além do suporte aos utilizadores e aplicações internas, geri e atualizei "
            "informação relativa a equipamentos, utilizadores e ativos tecnológicos. Registei pedidos, "
            "acompanhei ocorrências, mantive documentação e colaborei com diferentes departamentos e "
            "fornecedores, desenvolvendo método, atenção ao detalhe e capacidade de organização."
        ),
        (
            "A minha experiência em ambientes de suporte ensinou-me também a confirmar dados antes de "
            "efetuar alterações, identificar inconsistências e explicar procedimentos de forma simples. "
            "Estou habituado a trabalhar com Microsoft 365, bases de dados, aplicações empresariais e "
            "sistemas Windows, adaptando-me rapidamente a novos processos e ferramentas."
        ),
        (
            "O meu contacto com o Primavera ocorreu sobretudo num contexto técnico e de integração com "
            "SQL Server. Pretendo agora aprofundar a utilização funcional do ERP nas áreas de faturação, "
            "gestão de stocks e apoio administrativo, aplicando a base que já possuo e aprendendo os "
            "procedimentos específicos utilizados pela empresa."
        ),
        (
            "Tenho disponibilidade imediata e teria muito gosto em conversar sobre a forma como o meu "
            "perfil técnico, organização e sentido de responsabilidade podem contribuir para a função."
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
        "Candidatura - Administrativo | Primavera",
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
