from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, PageBreak, PageTemplate,
    Paragraph, Preformatted, Spacer, Table, TableStyle,
)


OUT = Path("/Users/miguelmagalhaes/Documents/GitHub/Personal_Website/output/pdf/Guiao_Entrevista_Hexa_Miguel_Magalhaes.pdf")
OUT.parent.mkdir(parents=True, exist_ok=True)

PAGE_W, PAGE_H = A4
NAVY = colors.HexColor("#142B4A")
BLUE = colors.HexColor("#2775C9")
CYAN = colors.HexColor("#2BC4C9")
TEXT = colors.HexColor("#26323D")
MID = colors.HexColor("#64717D")
LIGHT = colors.HexColor("#F2F6F9")
PALE_BLUE = colors.HexColor("#EAF3FC")
PALE_GREEN = colors.HexColor("#EAF8F3")
PALE_YELLOW = colors.HexColor("#FFF5D6")
PALE_RED = colors.HexColor("#FCEBED")
LINE = colors.HexColor("#D4DEE7")

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", "/System/Library/Fonts/Supplemental/Arial Italic.ttf"))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", fontName="Arial-Bold", fontSize=24, leading=29, textColor=NAVY, spaceAfter=7*mm))
styles.add(ParagraphStyle(name="CoverSub", fontName="Arial", fontSize=12.5, leading=17, textColor=MID, spaceAfter=8*mm))
styles.add(ParagraphStyle(name="H1x", fontName="Arial-Bold", fontSize=17, leading=21, textColor=NAVY, spaceAfter=4.5*mm))
styles.add(ParagraphStyle(name="H2x", fontName="Arial-Bold", fontSize=11.5, leading=14, textColor=BLUE, spaceBefore=2.5*mm, spaceAfter=1.8*mm))
styles.add(ParagraphStyle(name="Bodyx", fontName="Arial", fontSize=9.25, leading=12.8, textColor=TEXT, spaceAfter=2.1*mm))
styles.add(ParagraphStyle(name="Smallx", fontName="Arial", fontSize=7.8, leading=10.2, textColor=MID, spaceAfter=1.4*mm))
styles.add(ParagraphStyle(name="Bulletx", fontName="Arial", fontSize=9.0, leading=12.3, textColor=TEXT, leftIndent=5*mm, firstLineIndent=-3.5*mm, spaceAfter=1.4*mm))
styles.add(ParagraphStyle(name="Qx", fontName="Arial-Bold", fontSize=9.5, leading=12.4, textColor=NAVY, spaceBefore=1.8*mm, spaceAfter=0.8*mm))
styles.add(ParagraphStyle(name="Answerx", fontName="Arial", fontSize=8.9, leading=12.1, textColor=TEXT, leftIndent=4*mm, borderColor=CYAN, borderWidth=1.4, borderPadding=(0,0,0,4*mm), spaceAfter=2.3*mm))
styles.add(ParagraphStyle(name="Quote", fontName="Arial-Italic", fontSize=9.1, leading=12.8, textColor=TEXT, leftIndent=5*mm, rightIndent=4*mm, spaceAfter=2.4*mm))
styles.add(ParagraphStyle(name="CodeX", fontName="Courier", fontSize=7.6, leading=9.8, textColor=TEXT, leftIndent=4*mm, rightIndent=4*mm, backColor=LIGHT, borderColor=LINE, borderWidth=0.5, borderPadding=4*mm, spaceAfter=3*mm))
styles.add(ParagraphStyle(name="Foot", fontName="Arial", fontSize=7.1, leading=8.8, textColor=MID))


def P(text, style="Bodyx"):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph("- " + text, styles["Bulletx"])


def callout(title, body, color=PALE_BLUE):
    t = Table([[P(title, "Qx"), P(body, "Bodyx")]], colWidths=[40*mm, 124*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color), ("BOX", (0,0), (-1,-1), 0.6, LINE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 4*mm), ("RIGHTPADDING", (0,0), (-1,-1), 4*mm),
        ("TOPPADDING", (0,0), (-1,-1), 3*mm), ("BOTTOMPADDING", (0,0), (-1,-1), 2.2*mm),
    ]))
    return t


def qa(question, answer):
    return KeepTogether([P(question, "Qx"), P(answer, "Answerx")])


def styled_table(rows, widths, header=True, font_size=None):
    t = Table(rows, colWidths=widths, repeatRows=1 if header else 0)
    rules = [
        ("BOX", (0,0), (-1,-1), 0.6, LINE), ("INNERGRID", (0,0), (-1,-1), 0.4, LINE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 3*mm), ("RIGHTPADDING", (0,0), (-1,-1), 3*mm),
        ("TOPPADDING", (0,0), (-1,-1), 2.2*mm), ("BOTTOMPADDING", (0,0), (-1,-1), 2.2*mm),
    ]
    if header:
        rules += [("BACKGROUND", (0,0), (-1,0), NAVY), ("TEXTCOLOR", (0,0), (-1,0), colors.white),
                  ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT])]
    else:
        rules += [("ROWBACKGROUNDS", (0,0), (-1,-1), [colors.white, LIGHT])]
    if font_size:
        rules += [("FONTSIZE", (0,0), (-1,-1), font_size)]
    t.setStyle(TableStyle(rules))
    return t


def on_page(canvas, doc):
    page = canvas.getPageNumber()
    canvas.saveState()
    if page == 1:
        canvas.setFillColor(CYAN)
        canvas.rect(0, PAGE_H-18*mm, PAGE_W, 18*mm, fill=1, stroke=0)
        canvas.setFillColor(NAVY)
        canvas.rect(0, PAGE_H-21*mm, PAGE_W, 3*mm, fill=1, stroke=0)
    else:
        canvas.setFillColor(NAVY)
        canvas.rect(0, PAGE_H-7*mm, PAGE_W, 7*mm, fill=1, stroke=0)
        canvas.setFillColor(CYAN)
        canvas.rect(0, PAGE_H-8.5*mm, PAGE_W, 1.5*mm, fill=1, stroke=0)
        canvas.setStrokeColor(LINE)
        canvas.line(18*mm, 15*mm, PAGE_W-18*mm, 15*mm)
        canvas.setFont("Arial", 7.4)
        canvas.setFillColor(MID)
        canvas.drawString(18*mm, 9.5*mm, "Miguel Magalhães | Preparação Hexa Consulting")
        canvas.drawRightString(PAGE_W-18*mm, 9.5*mm, str(page))
    canvas.restoreState()


doc = BaseDocTemplate(
    str(OUT), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
    topMargin=20*mm, bottomMargin=20*mm,
    title="Guião de Preparação para Entrevista Hexa Consulting",
    author="Miguel Magalhães",
    subject="Senior IT Support and Systems Administrator",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=on_page)])

story = []

# 1 - Cover
story += [
    Spacer(1, 20*mm), P("GUIÃO DE PREPARAÇÃO", "Smallx"),
    P("Entrevista Hexa Consulting<br/>Senior IT Support and Systems Administrator", "CoverTitle"),
    P("Miguel Magalhães | 8 de outubro de 2026 | 14h00 | Microsoft Teams", "CoverSub"),
]
facts = [
    [P("Entrevistadora", "Smallx"), P("Patrícia Soares - IT Recruiter", "Bodyx")],
    [P("Duração", "Smallx"), P("30 minutos. É provável que seja uma primeira conversa de recrutamento, com validação de experiência, motivação, disponibilidade e enquadramento no projeto.", "Bodyx")],
    [P("Modelo", "Smallx"), P("Híbrido: três dias por semana nas instalações da Trofa.", "Bodyx")],
    [P("Pontos centrais", "Smallx"), P("Suporte L2, Windows e Linux, servidores, Active Directory, redes, segurança, backups, monitorização e documentação.", "Bodyx")],
]
story += [styled_table(facts, [35*mm,129*mm], header=False), Spacer(1,6*mm), P("Objetivo realista", "H2x")]
story += [P("Demonstrar bases técnicas, experiência operacional e maturidade, sem te apresentares como administrador de sistemas sénior. O melhor resultado pode ser o avanço neste processo ou o enquadramento noutra oportunidade da Hexa mais próxima do teu nível.", "Bodyx")]
story += [P("As três mensagens que devem ficar", "H2x")]
story += [
    bullet("Tens experiência prática com suporte, utilizadores, equipamentos, acessos, redes, aplicações empresariais, SQL e documentação."),
    bullet("Trabalhas de forma estruturada: avalias impacto, recolhes evidências, isolas a causa, validas a solução e acompanhas o caso."),
    bullet("Reconheces as lacunas em administração avançada, mas tens formação, curiosidade técnica e vontade de evoluir com acompanhamento."),
    Spacer(1,4*mm), callout("Regra principal", "Não tentes corresponder artificialmente ao título sénior. A transparência, acompanhada de exemplos concretos, é a tua melhor estratégia.", PALE_YELLOW),
    PageBreak(),
]

# 2 - Role fit
story += [P("1. Leitura estratégica da vaga", "H1x")]
rows = [
    [P("O anúncio pede", "Smallx"), P("O teu ponto de partida", "Smallx"), P("Como responder", "Smallx")],
    [P("5 a 10 anos / nível sénior", "Bodyx"), P("Cerca de 2 anos combinados; mais de 1 ano diretamente em suporte.", "Bodyx"), P("Reconhecer a diferença e destacar escala, variedade e potencial.", "Bodyx")],
    [P("Suporte L2 autónomo", "Bodyx"), P("Experiência sobretudo L1, diagnóstico, resolução e escalonamento.", "Bodyx"), P("Explicar o método e mostrar prontidão para assumir casos mais complexos gradualmente.", "Bodyx")],
    [P("Windows/Linux e servidores", "Bodyx"), P("Windows forte; Linux e sistemas em contexto académico/prático limitado.", "Bodyx"), P("Separar claramente utilização, diagnóstico e administração avançada.", "Bodyx")],
    [P("AD, M365, redes e acessos", "Bodyx"), P("Experiência relevante e diretamente transferível.", "Bodyx"), P("Dar exemplos de contas, grupos, permissões, VPN, DHCP e conectividade.", "Bodyx")],
    [P("Backups, DR, AWS, patching", "Bodyx"), P("Conhecimento de base; não comprovado como responsabilidade autónoma.", "Bodyx"), P("Explicar conceitos e como trabalharias sob procedimentos e validação.", "Bodyx")],
]
story += [styled_table(rows, [43*mm,57*mm,64*mm]), Spacer(1,4*mm), P("Pontos fortes confirmados", "H2x")]
story += [
    bullet("Centenas de utilizadores distribuídos por cinco localizações e cerca de 20 a 40 pedidos diários na NewCoffee."),
    bullet("Windows, Active Directory, Microsoft 365, VPN, DHCP, ERP, SQL Server, hardware, periféricos e aplicações internas."),
    bullet("Registo, priorização, documentação, acompanhamento e escalonamento de incidentes."),
    bullet("Formação em Engenharia Informática e mestrado em Cibersegurança e Auditoria de Sistemas Informáticos."),
]
story += [P("Mensagem de enquadramento", "H2x"), P("Estou consciente de que o anúncio procura um perfil sénior. Candidatei-me porque várias responsabilidades estão alinhadas com a minha experiência e com o percurso que quero construir. Gostaria de perceber se existe margem para um perfil em evolução, com acompanhamento inicial, ou se a Hexa tem projetos semelhantes de nível júnior/intermédio.", "Quote"), PageBreak()]

# 3 - Pitch
story += [P("2. Apresentação inicial", "H1x"), P("Versão recomendada - cerca de 60 segundos", "H2x")]
story += [P("Sou o Miguel Magalhães, licenciado em Engenharia Informática e atualmente frequento o Mestrado em Cibersegurança e Auditoria de Sistemas Informáticos. A minha experiência principal foi na NewCoffee, onde prestei suporte de primeira linha a centenas de utilizadores em cinco localizações, tratando aproximadamente 20 a 40 pedidos por dia. Trabalhei com Windows, Active Directory, Microsoft 365, VPN, DHCP, equipamentos, aplicações empresariais e Microsoft SQL Server, e contribuí para uma plataforma interna de ITSM e gestão de ativos. Também tenho experiência anterior em suporte ao cliente, Python, ERP e redes. Procuro agora evoluir para suporte de segunda linha e administração de sistemas, consolidando conhecimentos de Windows e Linux, monitorização, segurança e continuidade. Sei que esta posição tem um nível sénior superior ao meu percurso atual, mas acredito que posso acrescentar valor nas áreas que já domino e crescer com rapidez num ambiente estruturado.", "Quote")]
story += [P("Versão curta - cerca de 30 segundos", "H2x")]
story += [P("Sou licenciado em Engenharia Informática e tenho experiência prática em suporte técnico, Windows, Active Directory, Microsoft 365, redes, aplicações empresariais e SQL Server. Na NewCoffee apoiei centenas de utilizadores em cinco localizações e tratei diariamente incidentes variados. Quero agora avançar para L2 e administração de sistemas, com maior contacto com infraestrutura, segurança e monitorização, mantendo uma abordagem transparente sobre o meu nível atual.", "Quote")]
story += [P("English introduction", "H2x")]
story += [P("My name is Miguel Magalhães. I have a degree in Computer Engineering and I am currently studying for a Master's degree in Cybersecurity and Computer Systems Auditing. At NewCoffee, I provided first-line support to hundreds of users across five locations and handled around twenty to forty requests per day. My experience includes Windows, Active Directory, Microsoft 365, VPN, networking, business applications and Microsoft SQL Server. I am now looking to progress into second-line support and systems administration. I understand that this is a senior position, so I would be transparent about my current level while showing the practical experience and learning ability I can bring to the team.", "Quote")]
story += [callout("Como terminar", "Liga sempre a tua apresentação ao próximo passo: mais L2, infraestrutura, segurança e responsabilidade operacional.", PALE_GREEN), PageBreak()]

# 4 - Recruiter questions
story += [P("3. Perguntas de recrutamento", "H1x")]
story += [
    qa("Porque tens interesse na Hexa Consulting?", "A Hexa trabalha com talento e tecnologia em projetos reais de transformação, infraestrutura e cibersegurança. Interessa-me a proximidade das equipas, a aprendizagem contínua e a possibilidade de evoluir num contexto de consultoria. Também me identifico com os valores apresentados pela empresa: responsabilidade, colaboração, honestidade, apoio mútuo e agilidade."),
    qa("Porque te candidataste a uma posição sénior?", "Candidatei-me porque várias responsabilidades correspondem ao meu percurso - suporte, Windows, Active Directory, redes, acessos, aplicações, documentação e cibersegurança - e porque representam a evolução que procuro. Reconheço que ainda não tenho os 5 a 10 anos pedidos. Gostaria de perceber se o projeto admite um perfil em desenvolvimento ou se existe outra oportunidade semelhante mais adequada ao meu nível."),
    qa("Que tipo de função procuras?", "Procuro suporte técnico L1/L2 ou suporte aplicacional com progressão para sistemas e infraestrutura. Quero continuar próximo dos utilizadores, mas assumir gradualmente incidentes mais complexos, análise de logs, monitorização, acessos, redes e automação."),
    qa("Quais são os teus principais pontos fortes?", "Diagnóstico estruturado, organização sob volume, comunicação clara com utilizadores, acompanhamento até ao encerramento e facilidade de aprendizagem. A minha formação em cibersegurança também me leva a considerar permissões, evidências, risco e boas práticas durante a resolução."),
    qa("Qual é a tua maior lacuna para esta função?", "Ainda não administrei de forma autónoma ambientes empresariais complexos com servidores físicos e virtuais, backups, disaster recovery e cloud. Tenho bases conceptuais e experiência transferível, mas procuro consolidar essas áreas com procedimentos, formação e contacto progressivo com ambientes reais."),
    PageBreak(),
]

# 5 - practical matters
story += [P("4. Questões difíceis e condições", "H1x"), Spacer(1,3*mm)]
story += [qa("Tens experiência de L2?", "A minha experiência foi principalmente de primeira linha, mas incluía diagnóstico, reprodução de problemas, recolha de evidências, resolução de incidentes de hardware, software, acessos e conectividade, e escalonamento estruturado quando necessário. Ainda não me apresentaria como L2 sénior, mas estou preparado para assumir gradualmente casos mais complexos.")]
story += [qa("Consegues trabalhar autonomamente?", "Sou autónomo nas áreas em que tenho experiência e sei quando devo escalar. Para alterações com impacto em servidores, segurança, backups ou produção, confirmaria o âmbito, seguiria o procedimento de mudança, prepararia reversão e pediria validação sempre que necessário. Autonomia também significa reconhecer limites e proteger a operação.")]
story += [qa("Disponibilidade para iniciar?", "Completar antes da entrevista: 'Tenho disponibilidade para iniciar a partir de __________. O anúncio refere 30 a 60 dias; consigo cumprir esse prazo e posso tentar ajustar caso o projeto tenha outra necessidade.'")]
story += [qa("Disponibilidade para três dias por semana na Trofa?", "Sim, tenho disponibilidade para o modelo híbrido indicado, incluindo três dias presenciais por semana na Trofa. Gostaria apenas de confirmar os dias habituais, o horário e se existem deslocações adicionais ou prevenção.")]
story += [qa("Qual é a tua expectativa salarial?", "Mantém consistência com qualquer valor já comunicado. Se ainda não deste um valor: 'Gostaria de compreender melhor o cliente, o nível efetivo de responsabilidade e o pacote global. Como o título é sénior mas o meu perfil é mais júnior/intermédio, estou aberto a uma proposta coerente com o enquadramento que a Hexa considerar adequado.' Se pedirem um número, usa apenas uma faixa que estejas realmente disposto a aceitar.")]
story += [qa("Aceitas prevenção ou intervenções fora de horas?", "Estou disponível para compreender o modelo. Antes de confirmar, gostaria de saber a frequência, os tempos de resposta, a rotação, a compensação e o tipo de incidentes. Valorizo previsibilidade e um processo de passagem de turno claro.")]
story += [callout("Atenção", "Não prometas disponibilidade, salário ou deslocações que depois não consigas cumprir. Preenche os espaços antes da entrevista.", PALE_YELLOW), PageBreak()]

# 6 - support method
story += [P("5. Método de diagnóstico e suporte L2", "H1x")]
steps = [
    [P("1", "Bodyx"), P("Avaliar", "Bodyx"), P("Impacto, urgência, utilizadores afetados, serviço e risco operacional.", "Bodyx")],
    [P("2", "Bodyx"), P("Recolher", "Bodyx"), P("Erro, hora, alterações recentes, logs, equipamento, conta, rede e passos de reprodução.", "Bodyx")],
    [P("3", "Bodyx"), P("Isolar", "Bodyx"), P("Conta, endpoint, aplicação, rede, servidor, integração ou dependência externa.", "Bodyx")],
    [P("4", "Bodyx"), P("Formar hipótese", "Bodyx"), P("Relacionar sintomas com evidências e testar primeiro opções seguras e reversíveis.", "Bodyx")],
    [P("5", "Bodyx"), P("Corrigir", "Bodyx"), P("Aplicar solução ou workaround, respeitando permissões, mudança e plano de reversão.", "Bodyx")],
    [P("6", "Bodyx"), P("Validar", "Bodyx"), P("Confirmar tecnicamente e com o utilizador; verificar efeitos secundários e monitorizar.", "Bodyx")],
    [P("7", "Bodyx"), P("Documentar", "Bodyx"), P("Causa, evidências, ações, resultado, riscos e conhecimento reutilizável.", "Bodyx")],
]
story += [styled_table([[P("Etapa", "Smallx"),P("Ação", "Smallx"),P("Aplicação", "Smallx")]]+steps, [15*mm,30*mm,119*mm]), Spacer(1,4*mm)]
story += [P("Exemplo de escalonamento completo", "H2x")]
story += [P("Incidente: VPN indisponível para vários utilizadores desde as 09h10. Impacto: acesso remoto bloqueado. Evidências: erro X, testes com duas contas e dois equipamentos, internet local funcional, autenticação válida, gateway VPN sem resposta. Ações: reinício do cliente sem efeito; verificação de DNS e conectividade concluída. Pedido: validar disponibilidade do serviço e logs do concentrador. Utilizadores informados; próxima atualização prevista às 10h00.", "Quote")]
story += [P("Frase útil", "H2x"), P("Antes de alterar qualquer componente, confirmo o impacto, as dependências, o procedimento aprovado e a possibilidade de reversão.", "Quote"), PageBreak()]

# 7 - technical foundations
story += [P("6. Revisão técnica essencial", "H1x")]
tech = [
    [P("Tema", "Smallx"), P("Pontos para rever", "Smallx")],
    [P("Active Directory", "Bodyx"), P("Utilizadores, grupos, UO, bloqueios, passwords, permissões, GPO e princípio do menor privilégio.", "Bodyx")],
    [P("DNS", "Bodyx"), P("Resolução de nomes, registos A/CNAME, cache, servidor configurado; distinguir nome de conectividade IP.", "Bodyx")],
    [P("DHCP", "Bodyx"), P("Lease, scope, reserva, gateway e DNS; endereço 169.254.x.x sugere falha na atribuição.", "Bodyx")],
    [P("TCP/IP e VPN", "Bodyx"), P("IP, máscara, gateway, portas, rotas, latência, perda, autenticação e acesso ao recurso remoto.", "Bodyx")],
    [P("Windows", "Bodyx"), P("Event Viewer, serviços, atualizações, drivers, disco, memória, permissões e testes com outro perfil.", "Bodyx")],
    [P("Linux", "Bodyx"), P("Logs, processos, CPU/memória/disco, serviços, permissões, rede e conectividade. Explicar o que sabes sem alegar administração avançada.", "Bodyx")],
    [P("Microsoft 365", "Bodyx"), P("Licenças, autenticação, Outlook, Teams, OneDrive, MFA e sincronização. Distinguir utilização/suporte de administração avançada.", "Bodyx")],
    [P("Patching", "Bodyx"), P("Inventário, criticidade, testes, janela, backup, plano de reversão, aplicação, validação e monitorização.", "Bodyx")],
    [P("Logs e desempenho", "Bodyx"), P("Definir período e sintoma, correlacionar eventos, medir CPU, memória, disco, rede e serviços dependentes.", "Bodyx")],
]
story += [styled_table(tech, [42*mm,122*mm]), Spacer(1,3*mm)]
story += [callout("Resposta segura", "Se não conheces uma ferramenta, explica o conceito, o método que seguirias e a experiência mais próxima. Nunca inventes utilização prática.", PALE_GREEN), PageBreak()]

# 8 - scenarios
story += [P("7. Cenários técnicos prováveis", "H1x")]
story += [
    qa("Um utilizador não consegue iniciar sessão. O que verificas?", "Confirmo o âmbito e a mensagem. Testo rede e domínio; verifico se a conta está bloqueada, desativada ou expirada, se a password necessita de alteração e se o equipamento comunica com o controlador de domínio. Comparo com outro utilizador ou dispositivo, consulto eventos e só redefino credenciais após validar identidade e política."),
    qa("Um computador obtém 169.254.x.x. O que significa?", "É um endereço automático e normalmente indica que o equipamento não recebeu configuração do DHCP. Verifico cabo ou Wi-Fi, adaptador, scope e disponibilidade do servidor, tento renovar a lease e comparo com outro equipamento na mesma rede."),
    qa("Um nome não resolve, mas o IP responde. Como investigas?", "O caminho IP está funcional e a suspeita passa para DNS. Confirmo o servidor DNS configurado, testo a resolução, verifico cache e registo, comparo com outro cliente e procuro alterações recentes. Evito criar entradas locais permanentes como solução definitiva."),
    qa("Um servidor está lento. Qual é a tua abordagem?", "Defino quando começou e quais os serviços afetados. Verifico CPU, memória, disco, I/O, rede, processos, serviços, eventos e alterações recentes. Comparo com a linha de base, identifico a dependência afetada e aplico apenas ações aprovadas, com validação e monitorização."),
    qa("Um backup falhou. O que fazes?", "Confirmo o job, alvo, erro, capacidade, conectividade, credenciais e última execução válida. Avalio a criticidade e o RPO, corrijo ou escalo, repito conforme procedimento e valido a recuperação, não apenas o estado verde do job. Registo a causa e o resultado."),
    qa("Detetas atividade suspeita numa conta. Como ages?", "Preservo evidências, confirmo o âmbito e sigo o procedimento de segurança. Posso bloquear ou conter a conta se estiver autorizado, revogar sessões e escalar à equipa de segurança. Evito apagar logs ou investigar fora do meu âmbito e documento todas as ações."),
    PageBreak(),
]

# 9 - gaps
story += [P("8. Como responder sobre tecnologias em falta", "H1x")]
gaps = [
    [P("Tecnologia", "Smallx"), P("Resposta recomendada", "Smallx")],
    [P("Windows Server", "Bodyx"), P("Tenho conhecimentos de Windows e Active Directory e contacto com serviços de rede. Ainda não fui responsável autónomo por um parque Windows Server; quero aprofundar administração, eventos, serviços, GPO e manutenção.", "Bodyx")],
    [P("Linux Server", "Bodyx"), P("Consigo trabalhar com linha de comandos e conceitos de logs, processos, permissões e rede. A minha experiência de produção é limitada e não a apresentaria como administração sénior.", "Bodyx")],
    [P("AWS", "Bodyx"), P("Tenho conhecimentos de base de cloud, mas ainda não administrei AWS em produção. Relacionaria a aprendizagem com identidade, redes, monitorização, segurança e responsabilidade partilhada.", "Bodyx")],
    [P("ServiceNow / Zendesk", "Bodyx"), P("Já trabalhei com processos de tickets e com uma plataforma interna de ITSM/ativos. Ainda que a ferramenta seja diferente, conheço categorização, prioridade, SLA, evidências, escalonamento e encerramento.", "Bodyx")],
    [P("Backups / DR", "Bodyx"), P("Conheço os objetivos de backup, restore, RPO e RTO, mas não fui responsável autónomo por uma solução empresarial. Seguiria runbooks, validaria restores e escalaria falhas críticas.", "Bodyx")],
    [P("Exchange", "Bodyx"), P("Tenho experiência de suporte em Microsoft 365 e correio. Não devo confundir isso com administração avançada de Exchange; estou disponível para formação.", "Bodyx")],
    [P("Virtualização", "Bodyx"), P("Conheço os conceitos, mas a administração de hosts, clusters e capacidade não está comprovada no meu percurso. Posso aprender a partir de procedimentos e ambientes controlados.", "Bodyx")],
    [P("macOS", "Bodyx"), P("A minha experiência principal é Windows. Posso diagnosticar com método e aprender os fluxos específicos de macOS, mas não alegaria experiência equivalente.", "Bodyx")],
]
story += [styled_table(gaps, [42*mm,122*mm])]
story += [Spacer(1,3*mm), callout("Fórmula", "Ainda não usei X em produção. Tenho experiência próxima em Y, compreendo os conceitos Z e aprenderia através de documentação, laboratório, acompanhamento e validação controlada.", PALE_BLUE), PageBreak()]

# 10 - STAR
story += [P("9. Exemplos comportamentais - método STAR", "H1x")]
story += [P("1. Gestão de volume na NewCoffee", "H2x")]
story += [bullet("Situação: centenas de utilizadores distribuídos por cinco localizações."), bullet("Tarefa: tratar cerca de 20 a 40 pedidos diários sem perder prioridade ou contexto."), bullet("Ação: avaliar impacto e urgência, recolher evidências, resolver na primeira linha e escalar com registo completo."), bullet("Resultado: acompanhamento mais organizado e comunicação clara com utilizadores e equipas técnicas.")]
story += [P("2. Incidente que exigia escalonamento", "H2x")]
story += [bullet("Situação: problema que não podia ser resolvido apenas na primeira linha."), bullet("Tarefa: evitar repetição de testes e manter o utilizador informado."), bullet("Ação: documentar sintomas, impacto, equipamento, testes e resultados; encaminhar para equipa interna ou fornecedor e acompanhar."), bullet("Resultado: transferência de contexto mais completa e continuidade até ao encerramento.")]
story += [P("3. Plataforma interna de ITSM e ativos", "H2x")]
story += [bullet("Situação: necessidade de centralizar utilizadores, equipamentos, pedidos, incidentes e avisos."), bullet("Tarefa: contribuir para a aplicação e para a qualidade da informação."), bullet("Ação: trabalhar com tecnologias web e Microsoft SQL Server, consultar e validar dados e corrigir problemas."), bullet("Resultado: informação de suporte e ativos mais acessível e organizada para a equipa.")]
story += [P("4. Diagnóstico de integração numa plataforma em produção", "H2x")]
story += [bullet("Situação: plataforma de marcações com API externa, API serverless e deployment."), bullet("Tarefa: validar disponibilidade, marcações e comunicação entre componentes."), bullet("Ação: reproduzir o comportamento, analisar logs e variáveis de ambiente e testar a integração."), bullet("Resultado: maior estabilidade e plataforma entregue em produção.")]
story += [callout("Personaliza", "Escolhe um incidente real e acrescenta: erro concreto, testes, solução e resultado. Não inventes percentagens nem responsabilidades de servidor.", PALE_YELLOW), PageBreak()]

# 11 - English and questions
story += [P("10. Inglês e perguntas à recrutadora", "H1x"), P("Perguntas prováveis em inglês", "H2x")]
story += [
    qa("Why are you interested in this opportunity?", "I am interested because the role combines user support, systems, networks and security. It is more senior than my current experience, but it matches the direction in which I want to grow. I would like to understand whether the project can accommodate a developing profile or whether Hexa has a similar junior or mid-level opportunity."),
    qa("How do you troubleshoot an incident?", "I assess the impact and urgency, collect evidence and recent changes, isolate the affected layer, test a safe hypothesis, apply an approved solution or workaround, validate it with the user and document the result."),
    qa("What is your experience with Windows and Linux?", "My strongest practical experience is with Windows, user support, Active Directory and Microsoft 365. I have basic Linux knowledge, including command-line work, logs, processes, permissions and networking, but I would not describe myself as a senior Linux administrator."),
]
story += [P("Perguntas inteligentes para fazer", "H2x")]
story += [
    bullet("A vaga é para contratação direta pela Hexa ou para um cliente? Em que setor?"),
    bullet("Qual é a divisão real entre suporte L2, administração de sistemas e projetos de melhoria?"),
    bullet("Que dimensão têm a equipa, o parque de utilizadores e o ambiente de servidores?"),
    bullet("Que ferramentas são usadas para ITSM, monitorização, backups, virtualização e gestão de endpoints?"),
    bullet("Existe prevenção, trabalho fora de horas ou deslocação entre instalações?"),
    bullet("O requisito sénior é rígido ou existe margem para um perfil júnior/intermédio com plano de evolução?"),
]
story += [callout("Escolha", "Faz três ou quatro perguntas. Prioriza o nível real da função, o cliente, as tecnologias, o modelo de trabalho e o apoio inicial.", PALE_GREEN), PageBreak()]

# 12 - checklist
story += [P("11. Checklist final", "H1x"), P("Na noite anterior", "H2x")]
story += [
    bullet("Treinar a apresentação de 60 segundos em português e inglês."),
    bullet("Escolher um incidente real e completar o exemplo STAR com detalhes verificáveis."),
    bullet("Definir disponibilidade real, expectativa salarial e viabilidade de três dias por semana na Trofa."),
    bullet("Rever AD, DNS, DHCP, TCP/IP, Windows, Linux, backups, patching, logs e segurança."),
    bullet("Ter CV, Dossier de Competências, anúncio e este guião acessíveis."),
]
story += [P("Dez minutos antes", "H2x")]
story += [bullet("Entrar no Teams com antecedência e testar câmara, microfone e internet."), bullet("Silenciar notificações, usar iluminação frontal e manter água e notas por perto."), bullet("Abrir apenas uma folha-resumo; não ler respostas completas.")]
story += [P("Durante a entrevista", "H2x")]
story += [bullet("Responder primeiro à pergunta e acrescentar contexto depois."), bullet("Usar exemplos concretos e respostas de 45 a 90 segundos."), bullet("Quando não souberes, admitir, explicar como investigarias e ligar ao que já sabes."), bullet("Não afirmar senioridade, L2 avançado, administração de servidores ou ferramentas que ainda não utilizaste.")]
summary_rows = [
    [P("Experiência", "Smallx"), P("Cerca de 2 anos combinados; mais de 1 ano diretamente em suporte.", "Bodyx")],
    [P("Maior prova", "Smallx"), P("Centenas de utilizadores, 5 localizações, cerca de 20 a 40 pedidos/dia.", "Bodyx")],
    [P("Forças", "Smallx"), P("Windows, AD, M365, VPN, DHCP, ERP, SQL Server, ITSM, documentação.", "Bodyx")],
    [P("Lacuna", "Smallx"), P("Sem experiência sénior autónoma em servidores, cloud, backups e DR.", "Bodyx")],
    [P("Objetivo", "Smallx"), P("Evoluir para L2/sistemas ou ser considerado para projeto adequado ao nível atual.", "Bodyx")],
]
story += [P("Resumo de bolso", "H2x"), styled_table(summary_rows, [38*mm,126*mm], header=False), Spacer(1,4*mm)]
story += [P("Fontes consultadas", "H2x"), P("- Dossier de Competências de Miguel Magalhães, versão fornecida em 7 de outubro de 2026.<br/>- Anúncio Senior IT Support and Systems Administrator, conteúdo fornecido pelo candidato.<br/>- Hexa Group, visão geral e posicionamento: https://www.hexa-group.pt/<br/>- Hexa Consulting: https://www.hexa-group.pt/hexa-consulting", "Foot")]

doc.build(story)
print(OUT)
