from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, Frame, PageBreak, PageTemplate, Spacer, Table, TableStyle

from build_konica_interview_guide import (
    BLUE,
    CONTENT_W,
    GuideDocTemplate,
    H1,
    H2,
    H3,
    INK,
    LEFT,
    MUTED,
    NAVY,
    PALE,
    PALE_BLUE,
    PALE_GOLD,
    PALE_GREEN,
    PALE_RED,
    P,
    RIGHT,
    RULE,
    TEAL,
    WHITE,
    bilingual,
    box,
    bullet,
    num,
    register_fonts,
    section_title,
    table,
)


OUTPUT = Path(
    "output/pdf/Guia_Sintese_Entrevista_Rumos_IT_Helpdesk_Technician_Miguel_Magalhaes.pdf"
)
PAGE_W, PAGE_H = A4
TOP = 22 * mm
BOTTOM = 17 * mm


def page_header_footer(c, doc):
    page = c.getPageNumber()
    c.saveState()
    if page == 1:
        c.setFillColor(NAVY)
        c.rect(0, PAGE_H - 16 * mm, PAGE_W, 16 * mm, stroke=0, fill=1)
        c.setFillColor(TEAL)
        c.rect(0, PAGE_H - 16 * mm, 46 * mm, 3.5 * mm, stroke=0, fill=1)
        c.setFillColor(BLUE)
        c.rect(46 * mm, PAGE_H - 16 * mm, 22 * mm, 3.5 * mm, stroke=0, fill=1)
        c.restoreState()
        return

    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 13 * mm, PAGE_W, 13 * mm, stroke=0, fill=1)
    c.setFont("Verdana-Bold", 7.1)
    c.setFillColor(WHITE)
    c.drawString(LEFT, PAGE_H - 8.4 * mm, "RUMOS | IT HELPDESK TECHNICIAN")
    c.setFont("Verdana", 7.1)
    c.drawRightString(PAGE_W - RIGHT, PAGE_H - 8.4 * mm, "GUIÃO-SÍNTESE DE ENTREVISTA")

    c.setStrokeColor(RULE)
    c.setLineWidth(0.55)
    c.line(LEFT, 12.2 * mm, PAGE_W - RIGHT, 12.2 * mm)
    c.setFont("Verdana", 6.8)
    c.setFillColor(MUTED)
    c.drawString(LEFT, 8.2 * mm, "Miguel Magalhães • Preparação de entrevista")
    c.drawRightString(PAGE_W - RIGHT, 8.2 * mm, f"p. {page}")
    c.restoreState()


class RumosGuideDoc(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=LEFT,
            rightMargin=RIGHT,
            topMargin=TOP,
            bottomMargin=BOTTOM,
            title="Guia-síntese de entrevista - Rumos IT Helpdesk Technician",
            author="Miguel Magalhães",
            subject="Preparação personalizada para entrevista de IT Helpdesk Technician",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
            id="main",
        )
        self.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=page_header_footer)])


def make_story():
    s = []

    # Cover
    s += [
        Spacer(1, 27 * mm),
        P("GUIÃO-SÍNTESE • PREPARAÇÃO DE ENTREVISTA", "CoverKicker"),
        Spacer(1, 4 * mm),
        P("IT Helpdesk Technician", "CoverTitle"),
        P("Rumos • Matosinhos / Porto • Presencial", "CoverSub"),
        Spacer(1, 18 * mm),
        box(
            "OBJETIVO",
            "Demonstrar experiência prática em suporte, Windows, Active Directory, redes, equipamentos, impressoras e atendimento ao utilizador. A tua vantagem não é saber tudo: é investigar com método, comunicar bem, documentar e aprender rapidamente sem comprometer a segurança.",
            PALE_BLUE,
            BLUE,
        ),
        Spacer(1, 8 * mm),
        Table(
            [
                [P("PRIORIDADE 1", "GuideSmall"), P("PRIORIDADE 2", "GuideSmall"), P("PRIORIDADE 3", "GuideSmall")],
                [P("Redes Windows", "GuideBody"), P("Active Directory", "GuideBody"), P("Troubleshooting", "GuideBody")],
            ],
            colWidths=[CONTENT_W / 3] * 3,
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                    ("BACKGROUND", (0, 1), (-1, 1), PALE),
                    ("BOX", (0, 0), (-1, -1), 0.5, RULE),
                    ("INNERGRID", (0, 0), (-1, -1), 0.4, RULE),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ]
            ),
        ),
        Spacer(1, 24 * mm),
        P("Miguel Magalhães", "CoverName"),
        P("Engenharia Informática • Redes e Sistemas • Suporte Técnico", "CoverSub"),
        Spacer(1, 8 * mm),
        P("Memoriza estruturas e exemplos reais. Não tentes decorar todas as frases palavra por palavra.", "GuideSmall"),
        PageBreak(),
    ]

    # Positioning and intro
    section_title(s, "01", "Posicionamento e apresentação", "A mensagem que o entrevistador deve recordar.")
    s += [
        box(
            "A TUA MENSAGEM CENTRAL",
            "Tenho formação em Engenharia Informática e Redes e Sistemas, juntamente com experiência prática em suporte a utilizadores, equipamentos Windows, Active Directory, VPN, conectividade, impressão e aplicações empresariais. Trabalho de forma estruturada, comunico claramente, documento as intervenções e sei quando resolver autonomamente ou escalar com evidências.",
            PALE_GREEN,
            TEAL,
        ),
        H2("Sobre o requisito dos dois anos"),
        box(
            "RESPOSTA HONESTA",
            "Embora ainda não tenha dois anos contínuos com o título formal de Helpdesk Technician, acumulei experiência diretamente relacionada na NewCoffee, Staples e no estágio, executando tarefas muito próximas das responsabilidades desta função.",
            PALE_GOLD,
            colors.HexColor("#996B00"),
        ),
    ]
    s += bilingual(
        "Fala-me um pouco sobre ti / Tell me about yourself",
        "Sou licenciado em Engenharia Informática e tenho também um CTeSP em Redes e Sistemas Informáticos. Atualmente frequento um mestrado em Cibersegurança e Auditoria de Sistemas, em regime pós-laboral. Na NewCoffee prestei suporte a diferentes departamentos e localizações, trabalhando com equipamentos Windows, Active Directory, contas, permissões, impressão, VPN, DHCP, conectividade e aplicações empresariais. Também preparava equipamentos e articulava incidentes mais complexos com fornecedores externos. Desenvolvi ainda uma plataforma interna de ITSM para tickets, ativos, utilizadores e indicadores. Procuro agora consolidar a minha carreira em Helpdesk e contribuir para um serviço organizado e orientado para o utilizador.",
        "I hold a Bachelor's degree in Computer Engineering and a higher technical qualification in Computer Networks and Systems. I am currently pursuing a Master's degree in Cybersecurity and Computer Systems Auditing through an evening programme. At NewCoffee, I supported users across different departments and locations, working with Windows devices, Active Directory, accounts, permissions, printing, VPN, DHCP, connectivity and business applications. I also prepared equipment and coordinated more complex incidents with external providers. I am now looking to consolidate my career in IT Helpdesk and contribute to a structured, user-focused service.",
    )
    s += [
        H2("Porque devem contratar-te?"),
        P("Porque tenho experiência prática nas principais áreas da função: suporte a utilizadores, Windows, Active Directory, equipamentos, impressoras, redes e gestão de pedidos. Sei comunicar com utilizadores não técnicos, documentar e acompanhar um problema até à resolução. A plataforma de ITSM que desenvolvi demonstra iniciativa e compreensão de tickets, ativos, prioridades e indicadores. Ainda tenho áreas para aprofundar, mas possuo boas bases, aprendo rapidamente e não comprometo a segurança para resolver mais depressa."),
        PageBreak(),
    ]

    # Universal method + AD
    section_title(s, "02", "Método universal e Active Directory", "Usa este raciocínio em praticamente todos os cenários.")
    s += [
        table(
            [
                ["Passo", "Ação"],
                ["1", "Confirmar utilizador, equipamento e contacto."],
                ["2", "Perceber impacto e âmbito: um utilizador, vários ou serviço global?"],
                ["3", "Perguntar quando começou e se houve alterações recentes."],
                ["4", "Recolher mensagem de erro e tentar reproduzir."],
                ["5", "Investigar por camadas: físico -> sistema -> rede -> identidade -> aplicação."],
                ["6", "Fazer uma alteração controlada de cada vez."],
                ["7", "Validar com o utilizador, documentar e escalar com evidências se necessário."],
            ],
            [24 * mm, CONTENT_W - 24 * mm],
        ),
        H2("Resposta universal"),
        box(
            "",
            "Começaria por determinar o âmbito e impacto do incidente. Recolheria a mensagem de erro, alterações recentes e configuração relevante. Depois investigaria por camadas, começando pelo equipamento, sistema operativo, rede, identidade e aplicação. Faria uma alteração controlada de cada vez, validaria o resultado e documentaria os testes e a resolução.",
            PALE_BLUE,
            BLUE,
        ),
        H2("Utilizador não consegue iniciar sessão"),
        P("Confirmar se é conta local ou de domínio; verificar Caps Lock, nome do domínio, ligação à rede e mensagem exata. No Active Directory, confirmar se a conta está bloqueada, desativada ou expirada. Fazer reset apenas depois de verificar a identidade e seguir o procedimento."),
        H2("Novo utilizador"),
        num(1, "Pedido e aprovação do responsável."),
        num(2, "Criar utilizador segundo a convenção e colocar na OU correta."),
        num(3, "Adicionar apenas aos grupos autorizados."),
        num(4, "Preparar email, licenças, aplicações e computador."),
        num(5, "Testar autenticação e acessos; registar equipamento e intervenção."),
        H2("Conceitos rápidos"),
        table(
            [
                ["Conceito", "Explicação"],
                ["OU", "Organiza objetos e permite aplicar políticas."],
                ["Grupo", "Atribui acessos e permissões centralmente."],
                ["Conta local", "Existe apenas naquele computador."],
                ["Conta de domínio", "É gerida centralmente pelo Active Directory."],
                ["Menor privilégio", "Conceder apenas os acessos necessários e aprovados."],
            ],
            [40 * mm, CONTENT_W - 40 * mm],
        ),
        PageBreak(),
    ]

    # Onboarding and networks
    section_title(s, "03", "Preparação de PCs e redes Windows", "A área técnica com maior probabilidade de perguntas práticas.")
    s += [
        H2("Checklist de onboarding"),
        table(
            [
                ["Fase", "Verificações"],
                ["Equipamento", "Estado físico, número de série, carregador, periféricos e inventário."],
                ["Sistema", "Windows, drivers, atualizações, nome do computador e join ao domínio."],
                ["Aplicações", "Microsoft 365, software corporativo, Outlook, VPN e impressoras."],
                ["Segurança", "Políticas aplicadas, acessos aprovados e sem privilégios administrativos desnecessários."],
                ["Validação", "Rede, autenticação, aplicações, áudio, câmara, impressão e registo de entrega."],
            ],
            [38 * mm, CONTENT_W - 38 * mm],
        ),
        H2("Ordem de diagnóstico de rede"),
        box(
            "",
            "Camada física -> configuração IP -> conectividade local -> gateway -> Internet -> DNS",
            PALE_GREEN,
            TEAL,
        ),
        H2("Comandos essenciais"),
        table(
            [
                ["Comando", "Serve para"],
                ["ipconfig /all", "Ver IP, máscara, gateway, DNS e servidor DHCP."],
                ["ipconfig /release", "Libertar a configuração recebida por DHCP."],
                ["ipconfig /renew", "Solicitar uma nova configuração ao DHCP."],
                ["ipconfig /flushdns", "Limpar a cache DNS local."],
                ["ping", "Testar alcance e latência básica."],
                ["tracert", "Ver o caminho até ao destino."],
                ["nslookup", "Testar resolução DNS."],
                ["arp -a", "Ver associações IP/MAC locais."],
                ["netstat -ano", "Ver ligações, portas e PID dos processos."],
            ],
            [42 * mm, CONTENT_W - 42 * mm],
        ),
        PageBreak(),
    ]

    # Network scenarios
    section_title(s, "04", "Cenários de rede", "Responde por ordem e explica o que cada teste permite concluir.")
    s += [
        H2("O computador não tem Internet"),
        box(
            "RESPOSTA MODELO",
            "Primeiro verificaria se afeta apenas aquele utilizador ou vários. Confirmaria cabo ou Wi-Fi e o estado do adaptador. Depois usaria ipconfig /all para verificar IP, máscara, gateway e DNS. Testaria o gateway, depois um IP externo e finalmente um nome de domínio. Assim conseguiria distinguir um problema local, de acesso externo ou de DNS.",
            PALE_GREEN,
            TEAL,
        ),
        H2("Perguntas-relâmpago"),
        table(
            [
                ["Pergunta", "Resposta"],
                ["O PC recebeu 169.254.x.x", "É APIPA: normalmente não conseguiu obter configuração válida por DHCP."],
                ["Ping a 8.8.8.8 funciona, mas google.com não", "A conectividade IP existe; suspeitar de DNS."],
                ["Não consegue fazer ping ao gateway", "Investigar ligação física/Wi-Fi, adaptador, configuração IP, VLAN, porta ou rede local."],
                ["Só um utilizador está afetado", "Comparar configuração e equipamento com um utilizador funcional."],
                ["Vários utilizadores estão afetados", "Tratar como potencial incidente de infraestrutura e correlacionar tickets."],
            ],
            [69 * mm, CONTENT_W - 69 * mm],
        ),
        H2("TCP/IP, DNS e DHCP numa frase"),
        bullet("<b>TCP/IP:</b> conjunto de protocolos que permite comunicação em rede."),
        bullet("<b>DHCP:</b> atribui IP, máscara, gateway e DNS automaticamente."),
        bullet("<b>DNS:</b> converte nomes como empresa.pt em endereços IP."),
        bullet("<b>Gateway:</b> encaminha tráfego da rede local para outras redes."),
        H2("Wi-Fi versus Ethernet"),
        P("Ethernet tende a oferecer maior estabilidade e menor interferência; Wi-Fi depende de sinal, canal, interferência, densidade e roaming. Antes de culpar a Internet, distingue ligação ao ponto de acesso da conectividade externa."),
        box(
            "ERRO A EVITAR",
            "Não enumeres comandos sem explicar a hipótese que estás a testar. Um ping bem-sucedido não prova que a aplicação ou o serviço estejam operacionais.",
            PALE_RED,
            colors.HexColor("#A02B33"),
        ),
        PageBreak(),
    ]

    # Printer hardware backup
    section_title(s, "05", "Impressoras, hardware e backups", "Diagnosticar significa isolar o componente com evidência.")
    s += [
        H2("Impressora de rede não imprime"),
        P("Confirmar se afeta um utilizador ou todos; verificar alimentação, papel, consumíveis, erros e estado online; confirmar IP e conectividade; analisar fila, impressora predefinida, trabalhos bloqueados, Print Spooler e driver; imprimir página de teste; escalar avaria física com evidências."),
        H2("Hardware - diagnóstico básico"),
        table(
            [
                ["Sintoma", "Abordagem"],
                ["PC não liga", "Alimentação, carregador, bateria, cabos, indicadores, periféricos e POST."],
                ["Lentidão", "CPU, RAM, disco, processos, atualizações, espaço livre e Event Viewer."],
                ["Monitor sem imagem", "Energia, entrada, cabo, porta, deteção no Windows, driver e teste direto."],
                ["Docking station", "Alimentação, firmware, drivers, cabo e teste com componentes conhecidos."],
                ["Erro de dispositivo", "Device Manager, código de erro, driver, firmware e hardware alternativo."],
            ],
            [48 * mm, CONTENT_W - 48 * mm],
        ),
        H2("Backups"),
        table(
            [
                ["Tipo/conceito", "Definição"],
                ["Full", "Copia todos os dados selecionados."],
                ["Incremental", "Copia alterações desde o último backup realizado."],
                ["Diferencial", "Copia alterações desde o último backup completo."],
                ["Regra 3-2-1", "Três cópias, dois suportes diferentes e uma cópia fora do local."],
                ["Restore", "Deve ser testado; backup não validado pode não ser recuperável."],
                ["Redundância", "Melhora disponibilidade, mas não substitui backup."],
            ],
            [45 * mm, CONTENT_W - 45 * mm],
        ),
        box(
            "FRASE FORTE",
            "Um backup só é realmente útil quando existe um processo de restauro testado e documentado.",
            PALE_BLUE,
            BLUE,
        ),
        PageBreak(),
    ]

    # M365 and VPN
    section_title(s, "06", "Microsoft 365 e VPN", "Distingue sempre conta, cliente local, rede e serviço cloud.")
    s += [
        H2("Outlook não sincroniza"),
        num(1, "Confirmar conectividade, âmbito e mensagem de erro."),
        num(2, "Testar Outlook Web para distinguir cliente local de conta/serviço."),
        num(3, "Verificar modo offline, credenciais, MFA, quota e suplementos."),
        num(4, "Consultar saúde do serviço, se houver acesso."),
        num(5, "Só recriar perfil depois de excluir causas simples e proteger dados locais."),
        H2("Teams e OneDrive"),
        table(
            [
                ["Serviço", "Verificações"],
                ["Teams", "Áudio selecionado, permissões, mute físico, test call, web vs aplicação, drivers e rede."],
                ["OneDrive", "Pausa, conta/tenant, espaço, nomes/caminhos inválidos, estado do cliente e versão web."],
            ],
            [35 * mm, CONTENT_W - 35 * mm],
        ),
        H2("Utilizador não liga à VPN"),
        table(
            [
                ["Ordem", "Verificação"],
                ["1", "Existe acesso à Internet?"],
                ["2", "Qual é a mensagem de erro?"],
                ["3", "Credenciais, MFA e estado da conta estão corretos?"],
                ["4", "Cliente VPN, configuração, certificado e data/hora estão corretos?"],
                ["5", "DNS, rotas e logs revelam a causa? Outros utilizadores estão afetados?"],
            ],
            [24 * mm, CONTENT_W - 24 * mm],
        ),
        box(
            "IMPORTANTE",
            "Se utilizares um exemplo de Fortinet, descreve apenas as operações que executaste realmente. Não transformes contacto com a ferramenta em administração avançada.",
            PALE_GOLD,
            colors.HexColor("#996B00"),
        ),
        PageBreak(),
    ]

    # Security and behavioral
    section_title(s, "07", "Segurança e atendimento", "Helpdesk é uma linha de defesa e também a face do serviço de IT.")
    s += [
        H2("Password num Post-it"),
        box(
            "RESPOSTA MODELO",
            "Não utilizaria, copiaria nem fotografaria as credenciais. Alertaria o colaborador de forma discreta para o risco, pediria a remoção do Post-it e, conforme a política interna, a alteração da password. Se existisse um procedimento de reporte, seguiria esse procedimento.",
            PALE_GREEN,
            TEAL,
        ),
        H2("Possível phishing"),
        P("Pedir para não clicar, responder ou abrir anexos; preservar a mensagem; recolher informação e reportar à equipa de segurança. Se houve introdução de credenciais, escalar imediatamente para contenção, possível reset, revogação de sessões e análise do equipamento."),
        H2("Utilizador irritado"),
        P("Escutar sem interromper, reconhecer o impacto, recolher factos, explicar o que será verificado e evitar prometer prazos não garantidos. Manter o utilizador informado até à resolução ou escalamento."),
        H2("Vários tickets simultâneos"),
        P("Priorizar por impacto, urgência, risco, número de utilizadores e SLA. Um incidente generalizado ou de segurança tem prioridade sobre um pedido de conveniência individual."),
        H2("Quando não sabes resolver"),
        P("Recolher evidências, consultar documentação e base de conhecimento, executar testes seguros dentro do nível de acesso e escalar com contexto. Nunca transferir um ticket vazio."),
        H2("Princípios"),
        bullet("Verificar identidade antes de resets ou alterações de acesso."),
        bullet("Aplicar menor privilégio e exigir aprovação adequada."),
        bullet("Nunca desativar MFA ou controlos de segurança apenas para resolver depressa."),
        bullet("Preservar evidências e documentar todas as ações relevantes."),
        PageBreak(),
    ]

    # STAR
    section_title(s, "08", "Histórias STAR do teu percurso", "Preenche com factos e resultados que consigas sustentar.")
    s += [
        table(
            [
                ["História", "O que preparar"],
                ["Conectividade/VPN", "Quem foi afetado; testes; causa; resolução ou escalamento; validação."],
                ["Preparação de equipamento", "Windows, conta, software, acessos, inventário e testes antes da entrega."],
                ["Plataforma ITSM", "Necessidade, fluxos, tickets/ativos/utilizadores e melhoria concreta."],
                ["Escalamento a fornecedor", "Evidências recolhidas, handoff, acompanhamento e validação final."],
            ],
            [48 * mm, CONTENT_W - 48 * mm],
        ),
        H2("Estrutura STAR"),
        box("S - SITUAÇÃO", "Contexto, utilizadores afetados e impacto: ______________________________________________", WHITE, NAVY),
        Spacer(1, 3),
        box("T - TAREFA", "A tua responsabilidade e limite de acesso: ______________________________________________", WHITE, NAVY),
        Spacer(1, 3),
        box("A - AÇÕES", "Perguntas, testes, ferramentas, comunicação e decisões: __________________________________", WHITE, NAVY),
        Spacer(1, 3),
        box("R - RESULTADO", "Resultado verdadeiro, validação e aprendizagem: __________________________________________", WHITE, NAVY),
        H2("O que valoriza a resposta"),
        bullet("Dizer exatamente o que fizeste, não apenas o que a equipa fez."),
        bullet("Explicar a lógica por trás dos testes."),
        bullet("Demonstrar comunicação, documentação e validação."),
        bullet("Não inventar métricas, fabricantes ou tempos de resolução."),
        PageBreak(),
    ]

    # Salary + questions
    section_title(s, "09", "Negociação e perguntas ao entrevistador", "Não aceites por impulso nem transformes o final num interrogatório.")
    s += [
        H2("Se voltarem aos €1.100 brutos"),
        box(
            "RESPOSTA",
            "Tenho muito interesse no projeto e acredito que existe um bom alinhamento técnico. No entanto, tendo em conta a componente presencial e o conjunto de responsabilidades, gostaria de perceber se existe flexibilidade no salário-base. Caso o orçamento inicial esteja fechado, seria possível acordarmos uma revisão salarial ao fim de seis meses, associada a objetivos concretos?",
            PALE_GREEN,
            TEAL,
        ),
        H2("Confirmar sempre"),
        bullet("Salário-base bruto x 14 e subsídio de alimentação."),
        bullet("Seguro de saúde e restantes benefícios."),
        bullet("Horário, turnos, deslocações e eventual prevenção."),
        bullet("Formação, certificações e plano de progressão."),
        bullet("Data, critérios e valor potencial de revisão salarial."),
        H2("Perguntas para colocares"),
        num(1, "Qual é a dimensão da equipa e quantos utilizadores/localizações são suportados?"),
        num(2, "Quais são os incidentes mais frequentes e a ferramenta de ticketing?"),
        num(3, "Como é feita a divisão entre L1, L2 e fornecedores externos?"),
        num(4, "Que autonomia esperam nos primeiros três meses? Existe onboarding?"),
        num(5, "Que tecnologias utilizam para VPN, backups e gestão de equipamentos?"),
        num(6, "Quais são os SLAs principais e como é avaliado o desempenho?"),
        num(7, "Existe uma revisão salarial formal depois do período inicial?"),
        PageBreak(),
    ]

    # Final checklist
    section_title(s, "10", "Revisão final e fecho", "O essencial para chegares calmo e preparado.")
    s += [
        H2("Não dizer"),
        table(
            [
                ["Evitar", "Substituir por"],
                ["Domino Active Directory", "Tenho experiência com operações de contas, grupos, permissões e acessos."],
                ["Tenho dois anos de Helpdesk", "Tenho experiência acumulada diretamente alinhada com a função."],
                ["Reinicio e vejo se resolve", "Explicar âmbito, hipótese, teste, validação e documentação."],
                ["Desativo antivírus/MFA", "Seguir procedimento e nunca contornar segurança sem autorização."],
                ["Escalo logo", "Investigar dentro do acesso e escalar com evidências."],
                ["Aceito qualquer salário", "Demonstrar interesse e negociar o pacote com serenidade."],
            ],
            [52 * mm, CONTENT_W - 52 * mm],
        ),
        H2("Plano de 60 minutos"),
        table(
            [
                ["Tempo", "Revisão"],
                ["20 min", "IP, máscara, gateway, DNS, DHCP, APIPA e comandos."],
                ["15 min", "Active Directory, autenticação e onboarding."],
                ["10 min", "Impressoras, hardware e backups."],
                ["10 min", "Outlook, VPN, segurança e utilizadores difíceis."],
                ["5 min", "Apresentação inicial e perguntas finais."],
            ],
            [35 * mm, CONTENT_W - 35 * mm],
        ),
        H2("Antes da entrevista"),
        bullet("CV e anúncio abertos; três histórias STAR e cinco perguntas preparadas."),
        bullet("Câmara, microfone e ligação testados; papel, caneta e água."),
        bullet("Entrar 8-10 minutos antes e responder com calma."),
        H2("Frase final"),
        box(
            "",
            "Obrigado por explicarem melhor a função e o projeto. A conversa reforçou o meu interesse porque as responsabilidades estão alinhadas com a experiência que já adquiri em suporte, sistemas e redes. Acredito que consigo contribuir desde o início e evoluir rapidamente com os processos e tecnologias da equipa.",
            PALE_GREEN,
            TEAL,
        ),
        H2("Mensagem para ti"),
        box(
            "",
            "Não precisas de parecer sénior. Precisas de demonstrar método, honestidade, segurança, comunicação e capacidade de aprendizagem. Responde primeiro à pergunta; depois dá um exemplo real.",
            PALE_BLUE,
            BLUE,
        ),
    ]
    return s


def build():
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = RumosGuideDoc(str(OUTPUT))
    doc.build(make_story())
    print(OUTPUT.resolve())


if __name__ == "__main__":
    build()
