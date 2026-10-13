from pathlib import Path
from html import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
import subprocess
import pdfplumber

ROOT = Path('/Users/miguelmagalhaes/Documents/GitHub/Personal_Website')
OUT = ROOT / 'output/pdf/Guiao_Entrevista_MysticInvest_Miguel_Magalhaes.pdf'
TMP = ROOT / 'tmp/pdfs/mysticinvest'
OUT.parent.mkdir(parents=True, exist_ok=True)
TMP.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('Guide', '/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('GuideBold', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
N=colors.HexColor('#17354A'); T=colors.HexColor('#087F87'); INK=colors.HexColor('#263847'); GRAY=colors.HexColor('#617584'); PALE=colors.HexColor('#EEF5F7')
styles={
 'title':ParagraphStyle('title',fontName='GuideBold',fontSize=26,leading=31,textColor=N,spaceAfter=12),
 'sub':ParagraphStyle('sub',fontName='Guide',fontSize=12,leading=17,textColor=T,spaceAfter=12),
 'h':ParagraphStyle('h',fontName='GuideBold',fontSize=17,leading=21,textColor=N,spaceAfter=12),
 'h2':ParagraphStyle('h2',fontName='GuideBold',fontSize=10.7,leading=14,textColor=T,spaceBefore=8,spaceAfter=5),
 'p':ParagraphStyle('p',fontName='Guide',fontSize=9.6,leading=13.7,textColor=INK,spaceAfter=7),
 'small':ParagraphStyle('small',fontName='Guide',fontSize=8,leading=11,textColor=GRAY,spaceAfter=6),
 'quote':ParagraphStyle('quote',fontName='Guide',fontSize=9.6,leading=14,textColor=N,spaceAfter=0),
 'cell':ParagraphStyle('cell',fontName='Guide',fontSize=9,leading=12.4,textColor=INK),
}
story=[]
def p(s,style='p'): return Paragraph(s,styles[style])
def add(s,style='p'): story.append(p(s,style))
def h(s): add(s,'h2')
def bullet(s): add('• '+s)
def quote(s):
 tb=Table([[p(s,'quote')]],colWidths=[170*mm]); tb.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),.5,colors.HexColor('#CCDDE2')),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]));story.append(tb);story.append(Spacer(1,7))
def table(rows,widths=None):
 tb=Table([[p(escape(c),'cell') for c in row] for row in rows],colWidths=widths or [49*mm,121*mm],hAlign='LEFT'); tb.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),PALE),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#CCDDE2')),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]));story.append(tb);story.append(Spacer(1,7))
def page(num,title):
 if story:story.append(PageBreak())
 add('GUIÃO DE PREPARAÇÃO  /  '+str(num).zfill(2),'small');add(title,'h')

page(1,'A tua entrevista, preparada com intenção')
add('Miguel Magalhães','title')
add('MysticInvest | IT Service Desk &amp; Support<br/>Field Support Services','sub')
table([['Quando','Quarta-feira, 14 de outubro de 2026 | 10h00-11h00 (hora de Portugal)'],['Onde','Rua de Miragaia, 103, 4050-387 Porto. Entrevista presencial.'],['À chegada','Dirigir-te à receção e pedir pela Luísa Henriques.'],['Contacto do convite','223 402 591'],['Preparação','Guião elaborado em 12 de outubro de 2026.']])
h('A mensagem que deves deixar')
quote('Tenho experiência prática a apoiar utilizadores em várias localizações. Investigo os problemas com método, comunico com clareza e acompanho os pedidos. Quero aplicar estas bases ao suporte das operações do grupo e aprofundar as tecnologias em que tenho menos experiência.')
h('Como usar este guião')
bullet('<b>Primeira leitura:</b> páginas 2-5 para posicionamento, apresentação e exemplos reais.')
bullet('<b>Treino técnico:</b> páginas 6-11 para rever conceitos e responder a cenários em voz alta.')
bullet('<b>Antes de sair:</b> páginas 12-14 para inglês, condições, simulação e revisão final.')
add('As respostas são sugestões de treino, não relatos de incidentes teus. Substitui os espaços pelos teus casos reais. Confirma datas, ferramentas, responsabilidades e resultados no teu CV. Não declares experiência profissional que apenas tens em contexto académico.','small')

page(2,'O que esta função pede - e o que tu trazes')
h('Compreender o negócio')
add('A MysticInvest opera no setor dos cruzeiros, com marcas como DouroAzul, Nicko Cruises e Mystic Cruises. Nesta vaga, o suporte pode chegar a escritórios, unidades do grupo, navios e serviços dirigidos a clientes. A estabilidade da tecnologia ajuda a manter o trabalho das equipas e a experiência dos passageiros. [1]')
add('Na entrevista, não precisas de decorar o tamanho da frota. Mostra que percebes a ligação entre uma falha técnica, o impacto operacional e a necessidade de coordenação com quem está no terreno.')
table([['Área da vaga','Como relacionar com o teu percurso'],['Suporte distribuído','NewCoffee: apoio a utilizadores de departamentos e localizações diferentes.'],['Equipamentos e aplicações','Preparação e configuração de postos Windows, periféricos, software e apoio a aplicações empresariais.'],['Acessos e Microsoft','Experiência com Active Directory e suporte em Microsoft 365. Explica as operações exatas que executaste.'],['Rede e diagnóstico','Conectividade, VPN e fundamentos de DNS/DHCP. Diferencia diagnóstico de administração avançada de rede.'],['Registo e conhecimento','Acompanhamento de incidentes, inventário e participação numa plataforma interna de ITSM/ativos.'],['Segurança','Mestrado em Cibersegurança e interesse em acessos, rastreabilidade e boas práticas.']])
h('Áreas a desenvolver: nomear, sem dramatizar')
add('Windows Server em produção, administração de Entra ID/Intune, configuração de firewalls e switching/routing, IPTV, satélite, VoIP e CCTV: indica para cada uma se tens experiência profissional, laboratório ou apenas bases teóricas. Não assumes domínio por conheceres um conceito relacionado.')
quote('O meu ponto mais forte é o suporte e o diagnóstico. Em algumas das plataformas especializadas ainda preciso de acompanhamento inicial. Tenho bases para compreender as dependências, seguir os procedimentos e aprender com a equipa.')

page(3,'Apresentação e motivação: o início da conversa')
h('“Fala-me um pouco de ti” | cerca de 75 segundos')
quote('Sou o Miguel Magalhães, licenciado em Engenharia Informática e atualmente a frequentar um mestrado em Cibersegurança. Na NewCoffee, prestei suporte informático a utilizadores de diferentes departamentos e cinco localizações, trabalhando com equipamentos Windows, Active Directory, Microsoft 365, aplicações empresariais e conectividade. Fazia o diagnóstico, acompanhava os pedidos e articulava com fornecedores quando era necessário escalar. Também participei no desenvolvimento de uma plataforma interna de ITSM e gestão de ativos. Esta oportunidade interessa-me por combinar apoio aos utilizadores, trabalho no terreno e infraestrutura. Quero contribuir com a experiência que já tenho e aprofundar as tecnologias utilizadas pelo grupo.')
h('“Porque queres trabalhar connosco?”')
quote('Interessa-me uma função em que o suporte tenha impacto direto nas operações. A variedade de unidades e o contexto dos navios tornam este desafio especialmente interessante. Identifico-me com a componente prática, com o acompanhamento dos incidentes e com a possibilidade de trabalhar em equipa para manter os serviços disponíveis.')
h('“Porque devemos escolher-te?”')
quote('Trago experiência de contacto direto com utilizadores, capacidade de diagnóstico e preocupação em acompanhar os pedidos até à validação. Sei comunicar com pessoas de áreas diferentes, documentar o que fiz e reconhecer quando devo envolver outra equipa. A formação em informática e o mestrado ajudam-me também a olhar para os problemas com atenção à segurança.')
h('“Onde queres evoluir?”')
add('Liga a resposta à vaga: ganhar autonomia em suporte L2, redes, sistemas e plataformas Microsoft; melhorar procedimentos; assumir responsabilidade progressiva. Podes referir o interesse em segurança, mantendo claro o compromisso com esta função de suporte e operações.')
h('“Porque terminou a experiência anterior?”')
add('Prepara a razão verdadeira em duas ou três frases. Explica o contexto e o que procuras agora. Não inventes fim de contrato, reorganização ou motivos pessoais. Evita críticas a antigos colegas e empregadores.')

page(4,'Cinco histórias reais que te distinguem')
add('Prepara cada exemplo em 60-120 segundos. Usa STAR: situação, tarefa, ação e resultado. O maior detalhe deve estar nas tuas ações. Se não tens métricas, descreve um resultado observável e verdadeiro.')
table([['História','O que tens de conseguir contar'],['1. Rede ou VPN','Quem ficou afetado? Que testes fizeste? Como distinguiste equipamento, rede e aplicação? Quem validou?'],['2. Conta ou acesso','Qual era o pedido? Como validaste identidade/autorização? O que alteraste e como testaste?'],['3. Equipamento/software','Como recolheste requisitos, preparaste/configuraste, verificaste funcionamento e atualizaste registos?'],['4. Escalonamento','Que evidências enviaste? Como acompanhaste o fornecedor e mantiveste o utilizador informado?'],['5. Melhoria','Que problema repetitivo existia? O que mudaste em documentação, inventário ou plataforma? Qual o efeito?']])
h('Ficha de preparação: preenche para cada caso')
bullet('<b>Situação:</b> onde ocorreu, quem era afetado e qual o impacto.')
bullet('<b>A minha responsabilidade:</b> o que estava dentro do meu âmbito.')
bullet('<b>As minhas ações:</b> informação recolhida, testes e decisões, pela ordem em que aconteceram.')
bullet('<b>Colaboração:</b> quem envolvi, porquê e com que informação.')
bullet('<b>Resultado:</b> como confirmei a recuperação ou a entrega.')
bullet('<b>Aprendizagem:</b> o que ficou documentado ou o que faria melhor.')
h('Se te pedirem um erro ou uma dificuldade')
quote('Numa situação em que [caso real], percebi que [dificuldade/erro]. Comuniquei o impacto, corrigi com [ações reais] e passei a [melhoria]. Aprendi a [lição concreta].')
add('Não uses os cenários das próximas páginas como histórias pessoais. São exercícios para demonstrar raciocínio. Se não resolveste um problema sozinho, a coordenação e a qualidade do escalonamento continuam a ser contributos relevantes.','small')

page(5,'O teu método de diagnóstico e comunicação')
h('Uma sequência que podes aplicar a quase qualquer cenário')
table([['Etapa','O que dizer/fazer'],['1. Impacto e âmbito','Quem está afetado? Um utilizador, uma área ou um navio? Existe alternativa? Qual a urgência operacional?'],['2. Informação','Mensagem exata, hora, última vez que funcionou, alterações recentes, dispositivo, localização e serviço.'],['3. Hipóteses','Separar equipamento, identidade, rede e aplicação; consultar alertas e incidentes semelhantes.'],['4. Testes','Começar por verificações pouco intrusivas e comparar com um caso que funciona. Registar resultados.'],['5. Intervenção','Atuar dentro das permissões, procedimentos e prioridades. Avaliar impacto e recuperação antes de alterar.'],['6. Escalonamento','Enviar contexto, impacto, evidências, testes realizados e próximo passo necessário.'],['7. Validação','Confirmar com o utilizador que a tarefa original funciona e atualizar ticket/documentação.']])
h('Modelo de atualização ao utilizador')
quote('Já confirmei que o problema afeta [âmbito]. Estou a verificar [componente]. Neste momento [existe/não existe] uma alternativa validada. Volto a atualizar às [hora acordada], mesmo que a análise ainda esteja em curso.')
h('Como demonstrar autonomia')
add('Autonomia é avançar com método dentro do teu âmbito, comunicar riscos e pedir apoio atempadamente. Evita prometer uma hora de resolução sem evidência. Combina uma hora para a próxima atualização.')
h('Passagem de caso à equipa/fornecedor')
add('<b>Incluir:</b> serviço e ativos, impacto/prioridade, hora de início e fuso, sintomas, erros, alterações recentes, logs relevantes, testes e resultados, ações executadas, alternativa e contacto local. Partilha dados e credenciais apenas pelos canais autorizados.')

page(6,'Redes: conceitos e verificações essenciais')
table([['Conceito','Explicação curta para a entrevista'],['IP / máscara / gateway','IP identifica a interface; máscara define a rede; gateway permite chegar a outras redes.'],['DNS','Resolve nomes em endereços e outros registos. A aplicação pode falhar por DNS mesmo havendo conectividade IP.'],['DHCP','Atribui configuração de rede automaticamente, incluindo endereço, gateway e servidores DNS.'],['VLAN','Separa redes lógicas. A comunicação entre VLANs exige encaminhamento e políticas adequadas.'],['Switch / router / firewall','Switch liga dispositivos na rede; router encaminha entre redes; firewall controla tráfego por políticas.'],['VPN','Cria ligação protegida entre redes ou utilizador e rede, conforme a solução e configuração.'],['Wi-Fi / PoE','Wi-Fi dá acesso sem fios; PoE pode alimentar APs, telefones e câmaras pelo cabo de rede.']])
h('Comandos: o que testam [2][3][4]')
bullet('<b>ipconfig /all:</b> observar endereço, gateway, DNS, DHCP e adaptadores. Um IPv4 169.254.x.x pode indicar ausência de atribuição DHCP, mas exige contexto.')
bullet('<b>ping &lt;destino&gt;:</b> testar resposta ICMP. Ausência de resposta pode resultar de filtragem, não apenas de falha do destino.')
bullet('<b>nslookup &lt;nome&gt;:</b> consultar DNS. Comparar resultado com o esperado, sem alterar configurações às cegas.')
bullet('<b>tracert &lt;destino&gt;:</b> observar saltos que respondem. Asteriscos não demonstram, isoladamente, uma falha naquele equipamento.')
bullet('<b>Test-NetConnection &lt;servidor&gt; -Port 443:</b> testar ligação TCP à porta indicada. Sucesso não confirma a saúde completa da aplicação.')
h('“Não consigo aceder à aplicação”')
add('Determinar se afeta um ou vários utilizadores; testar ligação física/Wi-Fi e configuração; verificar nome DNS, caminho e porta do serviço; confirmar VPN, se aplicável; comparar com um dispositivo funcional; verificar alertas e autenticação. Se afeta todo um navio, coordenar com o contacto local e equipa de rede antes de alterações.')
add('Pratica apenas em equipamentos próprios ou autorizados. Renovar IP, reiniciar interfaces ou alterar DNS pode interromper uma sessão remota; não são passos automáticos.','small')

page(7,'Windows, Active Directory e Microsoft 365')
h('Windows: diagnóstico sem saltar para a reinstalação')
add('Num posto lento, confirma desde quando, se é geral ou só numa aplicação e o que mudou. Consulta CPU, memória, disco, espaço livre, eventos e atualizações. Verifica conectividade se a aplicação depende de um servidor. Aplica a correção autorizada e valida a tarefa do utilizador.')
h('Active Directory: saber explicar')
add('<b>AD DS:</b> serviço de diretório para identidades e recursos de domínio. <b>Grupo:</b> facilita atribuição de acessos. <b>OU:</b> organiza objetos e permite delegação/aplicação de políticas. <b>GPO:</b> aplica configurações a utilizadores e computadores, segundo o âmbito definido.')
quote('Antes de desbloquear uma conta ou repor uma palavra-passe, valido a identidade e sigo o procedimento. Verifico se há bloqueio, expiração, estado da conta e sinais de tentativas repetidas. Se o bloqueio volta a ocorrer, investigo a origem ou escalo com evidências, em vez de apenas repetir o desbloqueio.')
h('Onboarding e offboarding')
add('Seguir pedido autorizado, perfil de função e grupos aprovados; atribuir só os acessos necessários; preparar equipamento, aplicações e MFA; testar e registar. Na saída, cumprir o momento definido para bloquear acessos, revogar sessões e recolher ativos. Retenção de dados e correio seguem as políticas internas.')
h('Microsoft 365: suporte versus administração')
add('Outlook é um cliente; Exchange Online fornece serviços de correio. Teams suporta colaboração; OneDrive sincroniza ficheiros do utilizador; SharePoint suporta conteúdos e colaboração da organização. Explica as tarefas que já fizeste e não confundas uso destas aplicações com administração do tenant.')
h('“O Outlook não recebe emails”')
add('Confirmar se o problema é individual ou geral, envio/receção, erro e hora. Comparar com acesso web aprovado; verificar autenticação, conectividade, quota/licença e regras, dentro do teu âmbito. Consultar estado do serviço e envolver administração para rastreio de mensagens, se necessário. Não apagar o perfil antes de avaliar dados locais.')
h('Entra ID e Intune [5][6]')
add('<b>Entra ID:</b> gestão de identidades e acessos na cloud; não é apenas um AD local alojado online. <b>Intune:</b> gestão de dispositivos e aplicações, políticas e conformidade. Acesso Condicional pode utilizar sinais de identidade e dispositivo. Não declares administração prática destas plataformas se apenas conheces os conceitos.')

page(8,'Suporte no terreno, navios e serviços associados')
h('Um telefone VoIP não funciona')
add('Confirmar se é um telefone ou vários, alimentação/PoE, cabo e porta, endereço IP e VLAN, acesso à plataforma de telefonia e estado de registo. Separar ausência de chamada de áudio unilateral. Firewall, NAT e QoS podem estar envolvidos, mas alterações são feitas pela equipa autorizada.')
h('Uma câmara CCTV ficou indisponível')
add('Verificar impacto e âmbito, alimentação/PoE, cablagem, ligação de rede, IP, acesso do gravador ou plataforma e alertas. Distinguir imagem ao vivo de gravação. Controlar acesso às imagens e coordenar com segurança/fornecedor; não reiniciar um sistema de vigilância sem avaliar o impacto.')
h('IPTV: televisão por rede IP')
add('Pode envolver recetores, switches, VLANs, servidores e distribuição multicast. Se uma televisão falha, comparar com outra; se toda a unidade falha, procurar uma dependência comum. Conhecer IGMP e multicast como conceitos é útil, sem fingir experiência de configuração.')
h('Satélite e ligação dos navios')
add('A conectividade pode variar com cobertura, capacidade, latência e condições operacionais. A arquitetura concreta do grupo não está indicada. Pergunta como é feita a ligação e quais os fornecedores. Recolhe estado, métricas e impacto; coordena com a equipa de comunicações e o contacto a bordo.')
h('Instalação e trabalho a bordo')
bullet('Confirmar requisitos, localização, autorizações e janela de intervenção.')
bullet('Preparar materiais, configurações, identificação e testes antes da deslocação.')
bullet('Respeitar procedimentos locais, segurança física e coordenação com a operação.')
bullet('Testar a entrega, atualizar inventário, portas/cabos e documentação.')
h('Quando não tens experiência na tecnologia')
quote('Ainda não trabalhei diretamente com esse sistema. Percebo a sua finalidade e começaria por verificar alimentação, ligação, âmbito e dependências. Seguiria a documentação e envolveria a equipa ou fornecedor responsável antes de alterações fora do meu âmbito.')

page(9,'Segurança, ITSM e qualidade de serviço')
table([['Termo','Explicação prática'],['Incidente','Interrupção não planeada ou degradação de um serviço; procurar restaurá-lo.'],['Pedido de serviço','Solicitação habitual, como acesso ou equipamento, segundo o catálogo/processo.'],['Problema','Causa, ou potencial causa, de incidentes; pode exigir análise posterior à recuperação.'],['Alteração','Modificação que pode afetar serviços e precisa de avaliação e controlo adequados.'],['SLA','Acordo com objetivos de serviço, como resposta/resolução, âmbito e regras de medição.'],['Prioridade','Normalmente combina impacto e urgência segundo a matriz da organização.']])
h('Suspeita de phishing ou comprometimento')
add('Pedir que não interaja mais com a mensagem; recolher hora, utilizador, dispositivo e ações realizadas. Reportar pelo canal de segurança. Se houver suspeita de dispositivo comprometido, seguir o procedimento de contenção autorizado, preservando evidências. Não apagar logs nem divulgar a mensagem a terceiros. Reposição de credenciais ou revogação de sessões deve ser coordenada.')
h('Base de conhecimento e inventário')
add('<b>Artigo:</b> título pesquisável, sintomas, âmbito, pré-requisitos, passos, riscos, validação, escalonamento e data/responsável. <b>Inventário:</b> identificador, número de série, modelo, utilizador/localização, estado, garantia e alterações relevantes. A documentação deve ser útil para outra pessoa repetir o trabalho.')
h('Monitorização e prevenção de falhas')
add('Confirmar se o alerta é atual, correlacionar com sintomas e métricas, avaliar impacto e tendência, agir pelo procedimento e registar. Não silenciar alertas para esconder uma falha; propostas de ajuste devem ser justificadas e validadas.')
h('Exemplo de ticket completo')
quote('Título: [local/unidade] - [serviço] indisponível.<br/>Impacto: [utilizadores/tarefa afetados]. Início: [data, hora, fuso].<br/>Sintoma/erro: [descrição exata]. Testes: [ação + resultado].<br/>Ações e autorização: [o que foi feito]. Estado: [equipa responsável].<br/>Próxima atualização: [hora]. Validação/encerramento: [teste e confirmação].')

page(10,'Cenários práticos: treina o raciocínio')
h('1. “Todo um navio perdeu acesso a serviços corporativos”')
add('<b>Resposta:</b> confirmo impacto, serviços e conectividade local versus ligação externa. Verifico alertas e alterações, contacto a bordo e alternativas aprovadas. Recolho configuração e resultados de testes; coordeno com redes/fornecedor. Comunico o estado e acompanho até validação. Não assumo logo que é satélite nem reinicio o equipamento central sem autorização.')
h('2. “Dois pedidos urgentes chegam ao mesmo tempo”')
add('<b>Resposta:</b> comparo impacto, urgência, serviço crítico, pessoas afetadas e alternativas. Aplico a matriz de prioridade e peço coordenação se existir conflito. Distribuo ou escalo o segundo pedido e informo ambos os contactos. A prioridade não depende só de quem insiste mais.')
h('3. “Uma conta bloqueia repetidamente”')
add('<b>Resposta:</b> valido identidade e estado; verifico origem e horários das tentativas, dispositivos ou serviços com credenciais antigas, dentro das minhas permissões. Se houver sinais suspeitos, envolvo segurança. Desbloqueio apenas pelo procedimento e monitorizo/valido a solução.')
h('4. “Uma atualização provocou uma falha”')
add('<b>Resposta:</b> confirmo relação temporal e impacto, recolho erros e notifico o responsável. Avalio recuperação ou rollback previsto, com autorização e dependências. Depois valido o serviço e documento para análise e prevenção. Não removo atualizações indiscriminadamente.')
h('5. “O utilizador está irritado e exige uma solução imediata”')
quote('Compreendo que esta falha esteja a impedir o seu trabalho. Vou confirmar consigo o impacto e as informações necessárias para avançar. Estou a tratar o pedido com a prioridade adequada e darei uma nova atualização às [hora]. Se existir uma alternativa segura, explico-lhe como utilizá-la.')
h('6. “Uma impressora de rede não imprime”')
add('<b>Resposta:</b> verifico se afeta uma pessoa ou todos; estado físico, papel, erro e conectividade; IP, fila, servidor de impressão e driver. Testo pelo caminho adequado e valido com o utilizador. Reiniciar o spooler de um servidor pode afetar outras filas: avalio primeiro.')
add('Treino: responde sem ler em até 90 segundos. O entrevistador quer perceber a sequência das decisões, não uma lista interminável de ferramentas.','small')

page(11,'Perguntas difíceis e respostas credíveis')
h('“Qual é o teu nível de administração de sistemas?”')
quote('A minha experiência mais consolidada é em suporte a utilizadores, equipamentos Windows, contas e acessos e diagnóstico de conectividade e aplicações. Em administração de servidores e plataformas especializadas, o meu nível varia conforme a tecnologia. Posso explicar as tarefas que já executei e aquelas em que ainda preciso de acompanhamento.')
h('“Tens experiência com ServiceNow, EasyVista ou osTicket?”')
add('Indica apenas as ferramentas que utilizaste. Se não usaste a indicada: “Ainda não trabalhei com essa ferramenta, mas tenho experiência em registo e acompanhamento de pedidos e numa plataforma interna de ITSM. Conheço a importância de prioridade, histórico, escalonamento e documentação.”')
h('“Não sabes resolver. O que fazes?”')
quote('Confirmo o impacto, organizo os testes e consulto a documentação. Se atingir o limite do meu âmbito ou houver risco para o serviço, escalo com evidências e uma hipótese fundamentada. Continuo a acompanhar a comunicação e a validação, de acordo com a responsabilidade atribuída.')
h('“Como lidas com pressão?”')
add('Conta um caso real. Explica como priorizaste, reduziste incerteza, comunicavas e envolveste apoio. Evita “nunca fico nervoso”; mostra que manténs um método mesmo com pressão.')
h('“A cibersegurança é o teu objetivo. Vais querer sair do suporte?”')
quote('O interesse em segurança complementa o meu trabalho em suporte e sistemas. Quero consolidar experiência operacional, perceber o ambiente e contribuir com continuidade. Vejo valor em crescer nesta função e aplicar boas práticas de segurança no trabalho diário.')
h('“Estás disponível para prevenção e deslocações?”')
quote('Tenho interesse e disponibilidade para estas componentes, como indiquei na candidatura. Gostaria de perceber a organização da escala, os tempos de resposta, a frequência e duração das deslocações e o acompanhamento inicial, para confirmar a compatibilidade com os meus compromissos académicos.')
h('Evitar')
add('Prometer domínio de todas as ferramentas; atribuir a ti trabalho de outra equipa; expor dados confidenciais; inventar métricas; prometer disponibilidade ilimitada; dizer que reinicias tudo; usar jargão sem conseguir explicar o significado.')

page(12,'Treino em inglês: simples, claro e praticável')
h('Tell me about yourself')
quote('My name is Miguel Magalhães. I have a degree in Computer Engineering and I am currently studying for a master’s degree in Cybersecurity. At NewCoffee, I provided first-line IT support to users across different departments and locations. My work included Windows devices, user accounts, business applications and connectivity issues. I also documented incidents and worked with external suppliers when escalation was needed. I am interested in this role because it combines user support, practical troubleshooting and infrastructure.')
h('Why are you interested in this position?')
quote('I enjoy understanding technical problems and helping people get back to work. Supporting different offices and vessels would give me the opportunity to contribute in a practical environment and develop my skills. I would bring a structured approach, clear communication and a willingness to learn the systems used by the team.')
h('How do you troubleshoot an issue?')
quote('First, I check the impact and whether the issue affects one user or several users. I ask when it started and whether anything changed. Then I test the most likely causes, record the results and follow the support procedures. If I need to escalate, I provide the technical details and keep the user informed. Finally, I confirm that the service is working again.')
h('Frases úteis durante a conversa')
table([['Situação','Frase'],['Pedir clarificação','Could you clarify which system or situation you mean?'],['Pedir repetição','Could you please repeat the question a little more slowly?'],['Admitir uma lacuna','I have not administered that platform in production yet.'],['Dar atualização','I am still investigating. I will update you at the agreed time.'],['Explicar colaboração','I collected the evidence and escalated the case to the responsible team.'],['Descrever o nível','I consider my English to be at B2 level, and I keep improving it.']])
h('Exercício de 15 minutos')
add('Grava a apresentação, a motivação e um incidente real em inglês. Ouve uma vez, simplifica frases longas e repete. Foca-te em seres compreensível e consistente. Não memorizes um texto com vocabulário que não consigas usar espontaneamente.')

page(13,'Condições e perguntas que vale a pena esclarecer')
h('Prioridade: prevenção e deslocações')
bullet('Que dias e horas cobre a semana de prevenção? Qual o tempo de resposta e a frequência típica de chamadas?')
bullet('Quando é necessário ir ao local? Como funcionam transporte, despesas, compensação e descanso após intervenções?')
bullet('Existe acompanhamento antes de entrar na escala? Quem dá apoio técnico em casos complexos?')
bullet('As deslocações são locais ou também internacionais? Podem envolver vários dias a bordo ou fora de casa?')
h('Equipa, aprendizagem e expectativas')
bullet('Como se distribuem os pedidos entre L1, L2, sistemas, redes e fornecedores?')
bullet('Quais são as tecnologias e incidentes mais frequentes? Que ferramenta ITSM utilizam?')
bullet('O que esperam que eu consiga fazer autonomamente nos primeiros três meses?')
bullet('Como funciona a formação e a documentação das unidades e dos navios?')
h('Salário: um ponto de partida teu, não uma estimativa de mercado')
quote('A minha expectativa situa-se nos 1.500 euros brutos mensais de remuneração base, acrescidos do subsídio de alimentação. Gostaria também de conhecer o enquadramento da prevenção, intervenções fora do horário e deslocações, para avaliar o pacote completo.')
add('Este valor corresponde à expectativa que já referiste neste chat. Revê-o antes da entrevista. Se apresentarem um total, pede a discriminação entre base, alimentação e outras componentes, e a indicação da remuneração anual. Não confundas bruto com líquido.')
h('Disponibilidade e compromissos')
add('Leva uma data de início realista e confirma o teu horário académico e do CCP. Se houver conflitos com turnos ou prevenção, explica-os de forma concreta antes de assumir um compromisso. Não precisas de divulgar detalhes pessoais irrelevantes.')
h('Fecho da entrevista')
quote('Obrigado pela conversa. Fiquei particularmente interessado em [aspeto discutido]. Acredito que posso contribuir com a minha experiência em suporte, organização e acompanhamento de incidentes. Há algum ponto do meu percurso que gostassem que esclarecesse? Quais serão os próximos passos?')

page(14,'Plano final, simulação e folha de bolso')
h('12 de outubro | cerca de 90 minutos')
add('20 min: apresentação e motivação. 40 min: preparar cinco exemplos reais. 20 min: rever AD, DNS/DHCP e método de diagnóstico. 10 min: identificar lacunas e perguntas.')
h('13 de outubro | dois blocos de 45 minutos')
add('Bloco 1: Microsoft 365/Entra/Intune, redes e serviços dos navios. Bloco 2: simulação sem consultar respostas, incluindo 10 minutos em inglês. Confirmar percurso, roupa, CV e disponibilidade. Evitar estudar até tarde.')
h('Simulação de 30 minutos')
add('3 min: apresentação. 5 min: percurso e motivação. 10 min: três cenários técnicos. 5 min: exemplo real e inglês. 5 min: condições e perguntas. 2 min: fecho. Avalia clareza, honestidade, sequência de diagnóstico, atenção ao impacto e comunicação; repete só as respostas que ficaram confusas.')
h('Antes de sair de casa')
bullet('Entrevista presencial: 14/10/2026, 10h00; Rua de Miragaia, 103, Porto. Pedir por Luísa Henriques.')
bullet('Planear chegada 10-15 minutos antes. Levar CV, bloco, caneta e contacto 223 402 591.')
bullet('Rever apresentação, dois exemplos fortes, expectativa e quatro perguntas prioritárias.')
h('Cinco lembretes para levar contigo')
quote('1. Confirmar impacto e âmbito antes de agir.<br/>2. Explicar testes e resultados, não apenas ferramentas.<br/>3. Distinguir experiência profissional, laboratório e teoria.<br/>4. Comunicar, escalar bem e validar a recuperação.<br/>5. Mostrar interesse e esclarecer prevenção, deslocações e aprendizagem.')
h('Fontes e limites do guião')
add('Base: anúncio, convite e informação do teu percurso partilhados nesta conversa. Os cenários são exercícios; a arquitetura, condições contratuais e perguntas efetivas da entrevista não são conhecidas. Fontes públicas consultadas em 12/10/2026:','small')
for label,url in [('[1] MysticInvest - Brands','https://mysticinvest.com/brands/'),('[2] Microsoft Learn - ipconfig','https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig'),('[3] Microsoft Learn - nslookup','https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup'),('[4] Microsoft Learn - Test-NetConnection','https://learn.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection'),('[5] Microsoft Learn - Intune','https://learn.microsoft.com/intune/fundamentals/what-is-intune'),('[6] Microsoft Learn - Entra ID','https://learn.microsoft.com/en-us/entra/fundamentals/whatis')]:
 add(f'<link href="{url}" color="#087F87">{escape(label)}</link>','small')

def deco(c,d):
 w,ht=A4;c.saveState();c.setFillColor(N);c.rect(0,ht-8*mm,w,8*mm,fill=1,stroke=0);c.setFillColor(T);c.rect(0,ht-9*mm,w,1*mm,fill=1,stroke=0)
 c.setFont('Guide',8);c.setFillColor(GRAY);c.drawString(20*mm,12*mm,'Miguel Magalhães | MysticInvest | Preparação pessoal');c.drawRightString(w-20*mm,12*mm,str(d.page));c.restoreState()
doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=20*mm,leftMargin=20*mm,topMargin=17*mm,bottomMargin=22*mm,title='Guião de Entrevista - MysticInvest - Miguel Magalhães',author='Miguel Magalhães')
doc.build(story,onFirstPage=deco,onLaterPages=deco)
with pdfplumber.open(OUT) as pdf:
 print('Pages:',len(pdf.pages))
 for i,pg in enumerate(pdf.pages):
  text=pg.extract_text() or '';print(i+1,len(text),text.splitlines()[:2])
subprocess.run(['/Users/miguelmagalhaes/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm','-png','-r','90',str(OUT),str(TMP/'page')],check=True)
from PIL import Image, ImageOps, ImageDraw
thumbs=[]
for i,path in enumerate(sorted(TMP.glob('page-*.png'))):
 im=Image.open(path).convert('RGB');im.thumbnail((300,425));tile=Image.new('RGB',(320,455),'#dce4e8');tile.paste(im,((320-im.width)//2,10));ImageDraw.Draw(tile).text((10,438),f'Página {i+1}',fill='black');thumbs.append(tile)
for batch in range((len(thumbs)+5)//6):
 items=thumbs[batch*6:(batch+1)*6];sheet=Image.new('RGB',(960,910),'white')
 for j,im in enumerate(items):sheet.paste(im,((j%3)*320,(j//3)*455))
 sheet.save(TMP/f'contact-{batch+1}.png')
print(OUT)
