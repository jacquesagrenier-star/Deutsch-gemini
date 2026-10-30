# -*- coding: utf-8 -*-
"""Les noms du C1 portugais, par theme. SOURCE : c'est ici qu'on corrige, puis
python portugais/outils/construire.py (qui appelle niveaux.py apres l'A1).

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (29 oct. 2026),
converti au portugais d'Europe (variante_niveaux.py), puis relu. Meme format
que noms_a1.py (session socle). BROUILLON : a faire relire par un lusophone du Portugal.

Drapeaux en plus de ceux de l'A1 : « g? » genre devine (a verifier) ; « ex? »
la phrase ne contient pas le mot (a revoir) ; « ex=? » aucune phrase (a ecrire).
"""

NIVEAU = 'C1'

# (id du theme, nom portugais, theme source dont on reprend l'icone)
THEMES = [
    ('familia_c1_pt', 'Família e relações', 'erziehung_kindheit_c1'),
    ('trabalho_c1_pt', 'Trabalho e profissões', 'arbeit_buero_c1'),
    ('comida_c1_pt', 'Comida e cozinha', 'kueche_kochen_c1'),
    ('casa_c1_pt', 'A casa', 'garten_pflanzen_c1'),
    ('saude_c1_pt', 'O corpo e a saúde', 'gesundheit_c1'),
    ('roupa_c1_pt', 'Roupa e aparência', 'kleidung_c1'),
    ('natureza_c1_pt', 'Natureza e ambiente 1', 'umwelt_c1'),
    ('natureza_c1_pt_2', 'Natureza e ambiente 2', 'umwelt_c1'),
    ('viagens_c1_pt', 'Viagens e transportes', 'verkehr_c1'),
    ('cidade_c1_pt', 'A cidade', 'stadt_gebaeude_c1'),
    ('escola_c1_pt', 'Escola e estudos', 'universitaet_c1'),
    ('cultura_c1_pt', 'Tempos livres e cultura 1', 'technik_kunst_c1'),
    ('cultura_c1_pt_2', 'Tempos livres e cultura 2', 'technik_kunst_c1'),
    ('desporto_c1_pt', 'Desporto', 'sport_c1'),
    ('media_c1_pt', 'Media e comunicação', 'bildung_medien_c1'),
    ('dinheiro_c1_pt', 'Dinheiro e economia 1', 'wirtschaft_verwaltung_c1'),
    ('dinheiro_c1_pt_2', 'Dinheiro e economia 2', 'wirtschaft_verwaltung_c1'),
    ('sentimentos_c1_pt', 'Sentimentos e caráter', 'denken_wahrnehmung_c1'),
    ('sociedade_c1_pt', 'Sociedade e política', 'gesellschaft_wandel_c1'),
    ('lei_c1_pt', 'Lei e segurança', 'sicherheit_krisen_c1'),
    ('ideias_c1_pt', 'Ideias e debate 1', 'ursache_wirkung_c1'),
    ('ideias_c1_pt_2', 'Ideias e debate 2', 'ursache_wirkung_c1'),
]

NOMS = {
"familia_c1_pt": """
o aconchego | le sentiment de sécurité affective | As crianças precisam mais de aconchego do que de brinquedos. | Les enfants ont besoin de sécurité affective plus que de jouets.
a afeição | l'affection | O carinho dela era verdadeiro, mas discreto. | Son affection était sincère, mais discrète. | pl=afeições | ex?
o ambiente de aprendizagem | l'environnement d'apprentissage | Um ambiente de aprendizagem tranquilo faz mais efeito do que qualquer método. | Un environnement d'apprentissage calme agit plus que toute méthode. | pl=ambientes de aprendizagem
a casa de repouso | la EHPAD, maison de soins | A vaga na casa de repouso custa mais do que a reforma. | La place en maison de soins coûte plus que la retraite. | pl=casas de repouso
a cerimónia fúnebre | la cérémonie funéraire | A cerimónia fúnebre foi só para os mais próximos. | La cérémonie funéraire a eu lieu dans l'intimité. | g? | pl=cerimónias fúnebres
os condolências | les condoléances | Ele deu os pêsames à família. | Il a présenté ses condoléances à la famille. | g? | ex?
o dever de vigilância | l'obligation de surveillance | O dever de vigilância termina no portão da escola. | L'obligation de surveillance s'arrête au portail de l'école. | pl=deveres de vigilância
o direito à reforma | le droit à la retraite | O direito à reforma surge depois de cinco anos de contribuição. | Le droit à la retraite naît après cinq ans de cotisation. | pl=direitos às reformas
o diretivas antecipadas de vontade | les directives anticipées | Sem diretivas antecipadas, outros decidem. | Sans directives anticipées, d'autres décident. | g? | pl=diretivas antecipadas de vontade | ex?
a discrição | la discrétion | Dava para confiar na discrição dela. | On pouvait compter sur sa discrétion. | pl=discrições
o distanciamento | l'éloignement, aliénation | O distanciamento aconteceu devagar e sem ninguém perceber. | L'éloignement s'est produit lentement et sans qu'on le remarque.
a escolaridade obrigatória | l'obligation scolaire | A escolaridade obrigatória termina aos dezesseis anos. | L'obligation scolaire prend fin au seizième anniversaire. | g? | pl=escolaridades obrigatórias
o estilo de criação | le style éducatif | Os dois têm estilos de criação muito diferentes. | Les deux ont un style éducatif très différent. | pl=estilos de criação
a etapa do desenvolvimento | l'étape de développement | Cada etapa do desenvolvimento chega no seu próprio tempo. | Chaque étape de développement vient à son propre rythme. | g? | pl=etapas do desenvolvimento
a fase da birra | la période d'opposition | A fase da birra passa, prometo. | La période d'opposition passe, promis. | g? | pl=fases da birra
a fragilidade | la fragilité (grand âge) | A fragilidade chegou mais rápido do que o esperado. | La fragilité est venue plus vite que prévu. | g?
a imposição de limites | la pose de limites | Impor limites não é o contrário de dar carinho. | Poser des limites n'est pas le contraire de l'attention. | pl=imposições de limites | ex?
a intimidade | la familiarité, intimité | Depois de vinte anos surge uma intimidade própria. | Après vingt ans naît une familiarité particulière.
o inventário | le règlement de la succession | O inventário arrastou-se por dois anos. | Le règlement de la succession s'est étiré sur deux ans.
o isolamento | l'isolement, solitude subie | Nós refizemos o isolamento do telhado. | Nous avons refait l'isolation du toit.
a lealdade | la loyauté | Lealdade é diferente de obediência. | La loyauté est autre chose que l'obéissance.
a necessidade de apoio pedagógico | le besoin de soutien scolaire | Foi constatada nele uma necessidade especial de apoio pedagógico. | Un besoin de soutien particulier a été constaté chez lui. | pl=necessidades de apoio pedagógico | ex?
o obituário | la nécrologie, hommage | O obituário saiu no jornal na manhã seguinte. | La nécrologie était dans le journal le lendemain matin.
o papel de exemplo | la fonction d'exemple | Os professores servem de exemplo, queiram ou não. | Les enseignants ont une fonction d'exemple, qu'ils le veuillent ou non. | g? | pl=papéis de exemplo | ex?
a pessoa de referência | la figure de référence | Uma criança precisa de poucas pessoas de referência, mas confiáveis. | Un enfant a besoin de peu de figures de référence, mais fiables. | g? | pl=pessoas de referência
a reaproximação | le rapprochement |  |  | pl=reaproximações | ex=?
a reunião de pais | la réunion de parents | Na reunião de pais só meia dúzia de pessoas falou. | À la réunion de parents, seule une poignée de gens a parlé. | g? | pl=reuniões de pais
a troca de gerações | le changement de génération | Na empresa vai haver uma troca de gerações. | L'entreprise est à la veille d'un changement de génération. | pl=trocas de gerações
o vínculo | le lien, attachement | O vínculo entre os dois durou décadas. | Le lien entre les deux a tenu des décennies.
o zelo | la attention bienveillante | O zelo dele às vezes sufocava. | Sa sollicitude paraissait parfois étouffante.
""",
"trabalho_c1_pt": """
o abuso | l'exigence excessive, affront | Este prazo é um verdadeiro abuso. | Ce délai est une exigence proprement inacceptable. | g?
a adaptação | l'adaptation, ajustement | Sem adaptação ao novo clima não dá. | Sans adaptation au nouveau climat, rien n'est possible. | pl=adaptações
o agendamento | la prise de rendez-vous | Sem agendamento ninguém é atendido. | Sans rendez-vous, personne n'est reçu.
o aviso prévio | le délai de préavis | O aviso prévio é de três meses até o fim do trimestre. | Le délai de préavis est de trois mois à la fin du trimestre. | pl=avisos prévios
a boa vontade comercial | le geste commercial | Por cortesia o aparelho foi trocado mesmo assim. | Par geste commercial, l'appareil a été échangé malgré tout. | g? | pl=boas vontades comerciais | ex?
a carga | la charge, contrainte | A carga estava mal presa. | La cargaison était mal arrimée. | g?
o centro de distribuição | la plateforme de transbordement | O porto é o principal entreposto da região. | Le port est la principale plateforme de transbordement de la région. | pl=centros de distribuição | ex?
o ciclo | le cycle, circuit | O material fica no ciclo e nunca vira lixo. | Le matériau reste dans le cycle et ne devient jamais un déchet.
o clima de trabalho | l'ambiance de travail | O clima de trabalho melhorou desde a troca. | L'ambiance de travail s'est améliorée depuis le changement. | pl=climas de trabalho
a consultoria especializada | le conseil spécialisé | A consultoria especializada não custa nada e muitas vezes economiza centenas. | Le conseil spécialisé ne coûte rien et fait souvent économiser des centaines. | g? | pl=consultorias especializadas
o controle de estoque | la gestion des stocks | Sem um bom controle de estoque, vive-se procurando. | Sans gestion des stocks propre, on cherche sans arrêt. | g? | pl=controles de estoque
o custo do frete | les frais de transport | O custo do frete é maior do que o valor da mercadoria. | Les frais de transport dépassent la valeur de la marchandise. | pl=custos do frete
o dano no transporte | l'avarie de transport | Um dano no transporte precisa de ser comunicado em sete dias. | Une avarie de transport doit être signalée sous sept jours. | pl=danos nos transportes
o depósito intermediário | l'entrepôt intermédiaire | A mercadoria fica quatro semanas no depósito intermediário. | La marchandise reste quatre semaines à l'entrepôt intermédiaire. | pl=depósitos intermediários
o desembaraço aduaneiro | le dédouanement | O desembaraço aduaneiro demora mais do que a viagem. | Le dédouanement dure plus longtemps que le trajet. | pl=desembaraços aduaneiros
a disponibilidade | la joignabilité, accessibilité | O atendimento por telefone vai até as dezesseis horas. | La joignabilité téléphonique s'arrête à seize heures. | ex?
a falta de fornecimento | la rupture d'approvisionnement | A falta de um único chip parou a fábrica. | Une rupture sur une puce a arrêté l'usine. | g? | pl=faltas de fornecimento | ex?
a finitude | la caractère fini, finitude | Durante muito tempo ninguém falava da finitude dos recursos. | La finitude des réserves n'a longtemps préoccupé personne.
a franquia | la franchise (assurance) | Nesta apólice a franquia é de trezentos euros. | Sur cette police, la franchise est de trois cents euros. | g?
o gestor | le cadre dirigeant | De um gestor espera-se mais do que conhecimento técnico. | D'un cadre on attend plus que des compétences techniques.
a gestão de reclamações | la gestion des réclamations | Uma boa gestão de reclamações segura mais clientes do que qualquer propaganda. | Une bonne gestion des réclamations retient plus de clients que la publicité. | g? | pl=gestões de reclamações
o palete | la palette | Num palete cabem quarenta caixas. | Quarante cartons tiennent sur une palette.
o período de integração | la période de formation initiale | O treinamento inicial dura uns três meses. | La formation initiale dure environ trois mois. | pl=períodos de integração | ex?
o plantão | l'astreinte, disponibilité | Ele está de plantão neste fim de semana. | Il est d'astreinte ce week-end. | pl=plantões
a pressão por desempenho | la pression de la performance | Hoje a pressão por desempenho já começa na escola. | La pression de la performance commence aujourd'hui dès l'école. | g? | pl=pressões pores desempenhos
o processamento | le traitement, exécution (d'un dossier) | Normalmente o processamento leva duas semanas. | En règle générale, le traitement prend deux semaines.
o rastreamento | le suivi de colis | O rastreamento não mostra nada de novo há três dias. | Le suivi de colis n'affiche rien de neuf depuis trois jours.
o reconhecimento | la reconnaissance, estime | Reconhecimento não custa nada e mantém as pessoas mais tempo na empresa. | La reconnaissance ne coûte rien et retient les gens plus longtemps.
a renovação | le renouvellement, rénovation | A renovação da rede vai levar anos. | Le renouvellement du réseau prend des années. | g? | pl=renovações
a reposição | le réapprovisionnement | A reposição chega na sexta, no mínimo. | Le réapprovisionnement arrive vendredi au plus tôt. | g? | pl=reposições
a rotatividade | la rotation du personnel | A alta rotatividade custa mais do que qualquer aumento. | La forte rotation du personnel coûte plus cher que toute augmentation.
a separação de pedidos | la préparation de commandes | Depois da reforma, a separação de pedidos é semiautomática. | La préparation de commandes est semi-automatique depuis les travaux. | g? | pl=separações de pedidos
o serviço adicional | la prestation supplémentaire | Cada serviço adicional é cobrado à parte. | Chaque prestation supplémentaire est facturée à part. | pl=serviços adicionais
o serviço prestado | la prestation de service | Quais serviços estão incluídos no preço está nas letras miúdas. | Quelles prestations sont comprises dans le prix est écrit en petit. | pl=serviços prestados | ex?
a taxa de ocupação | le taux de charge, occupation | A oficina está com noventa por cento da capacidade ocupada. | Le taux de charge de l'atelier est de quatre-vingt-dix pour cent. | g? | pl=taxas de ocupação | ex?
o tempo de espera | le temps d'attente | O tempo de espera hoje é de seis semanas. | Le temps d'attente est actuellement de six semaines. | pl=tempos de espera
a trajetória | le parcours, itinéraire | A trajetória dele é tudo menos linear. | Son parcours est tout sauf linéaire. | g?
a unidade de embalagem | l'unité de conditionnement | A embalagem tem doze unidades. | L'unité de conditionnement comprend douze pièces. | pl=unidades de embalagem | ex?
a vigência do contrato | la durée du contrat | A vigência do contrato é renovada automaticamente. | La durée du contrat se prolonge automatiquement. | g? | pl=vigências do contrato
o volume de pedidos | le carnet de commandes | O volume de pedidos está melhor do que no ano passado. | Le carnet de commandes est meilleur que l'an dernier. | pl=volumes de pedidos
""",
"comida_c1_pt": """
o aroma de tostado | l'arôme de torréfaction | O aroma de tostado só aparece acima de cento e sessenta graus. | L'arôme de torréfaction n'apparaît qu'au-dessus de cent soixante degrés. | pl=aromas de tostado
o artigo de prazer | le produit de plaisir (café, alcool…) | O café é considerado um prazer, não um alimento. | Le café passe pour un produit de plaisir, pas pour un aliment. | pl=artigos de prazer | ex?
a conservação | la conservation (procédé) | O sal foi a forma mais antiga de conservação. | Le sel était la plus ancienne forme de conservation. | pl=conservações
a consistência | la consistance, texture | A consistência deve ser cremosa, não líquida. | La consistance doit être crémeuse, pas liquide. | g?
a douração | le coloration, brunissement | A douração traz o sabor, não só o calor. | C'est le brunissement qui apporte le goût, pas la chaleur seule. | g? | pl=dourações
o estilo de vida | la conduite de vie | Uma vida tranquila era mais importante para ele do que dinheiro. | Une conduite de vie tranquille lui importait plus que l'argent. | pl=estilos de vida | ex?
o exercício de atenção plena | l'exercice de pleine conscience | Dez minutos de atenção plena bastam para começar. | Dix minutes d'exercice de pleine conscience suffisent pour commencer. | pl=exercícios de atenção plena | ex?
o fase de recuperação | la phase de récupération | Sem fase de recuperação o treino não adianta nada. | Sans phase de récupération, l'entraînement ne donne rien. | g? | pl=fases de recuperação
o fazer conservas | la mise en conserve, stérilisation | Fazer conserva só compensa a partir de uma quantidade maior. | La mise en conserve ne vaut la peine qu'à partir d'une certaine quantité. | g? | pl=fazeres conservas | ex?
a fermentação | la fermentation | No frio a fermentação leva o dobro do tempo. | La fermentation dure deux fois plus longtemps au froid. | g? | pl=fermentações
a fermentação da massa | la conduite de la pâte | Uma fermentação longa deixa o pão mais leve. | Une longue conduite de la pâte rend le pain plus digeste. | pl=fermentações da massa | ex?
a infusão | l'infusion | A segunda infusão é mais suave. | La seconde infusion a un goût plus doux. | g? | pl=infusões
a intolerância | l'intolérance | A intolerância só se manifestou tarde. | L'intolérance ne s'est manifestée que tard. | g?
a marinada | la marinade | A marinada precisa de pelo menos quatro horas. | La marinade demande au moins quatre heures. | g?
a maturação | l'affinage, maturation | A maturação no porão leva dezoito meses. | L'affinage en cave dure dix-huit mois. | g? | pl=maturações
a pausa digital | la pause numérique | No domingo a família faz uma pausa digital. | Le dimanche, la famille fait une pause numérique. | pl=pausas digitais
a renúncia ao consumo | le renoncement à consommer | Deixar de consumir é mais fácil do que consumir com consciência. | Renoncer à consommer est plus simple qu'une consommation consciente. | g? | pl=renúncias aos consumos | ex?
o sedentarismo | le manque d'activité physique | O sedentarismo age mais devagar do que o cigarro, mas com certeza. | Le manque d'activité agit plus lentement que le tabac, mais sûrement.
a sequência dos pratos | l'ordre des plats | A sequência dos pratos estava num cartão em cada lugar. | L'ordre des plats figurait sur une carte à chaque place. | g? | pl=sequências dos pratos
o tamanho da porção | la taille des portions | O tamanho das porções aumentou desde os anos noventa. | La taille des portions a grandi depuis les années quatre-vingt-dix. | pl=tamanhos da porção | ex?
o tempo de cozimento | le temps de cuisson |  |  | pl=tempos de cozimento | ex=?
a técnica de corte | la manière de couper | No peixe, a técnica de corte decide tudo. | Pour le poisson, la manière de couper décide de tout. | g? | pl=técnicas de corte
o valor nutricional | la valeur nutritive | O valor nutricional está na parte de trás. | La valeur nutritive figure au dos. | pl=valores nutricionais
""",
"casa_c1_pt": """
o acabamento | la façonnage, finition | Pelo acabamento reconhece-se o preço. | À la finition, on reconnaît le prix.
o acabamento final | la finition, dernière main | Ao texto só falta o retoque final. | Il ne manque au texte que la dernière main. | pl=acabamentos finais | ex?
o acabamento posterior | la reprise, retouche | Sem acabamento a borda continua afiada. | Sans retouche, l'arête reste coupante. | pl=acabamentos posteriores | ex?
o adensamento | la densification | O adensamento economiza espaço e gera brigas. | La densification économise de l'espace et crée des conflits.
a bucha | la cheville | Sem bucha o parafuso não aguenta uma semana. | Sans cheville, la vis ne tient pas une semaine. | g?
o canteiro | la plate-bande, carré | Um canteiro elevado poupa as costas e aquece mais cedo. | Un carré surélevé ménage le dos et se réchauffe plus tôt.
o canteiro elevado | le carré surélevé | Um canteiro elevado poupa as costas e aquece mais cedo. | Un carré surélevé ménage le dos et se réchauffe plus tôt. | pl=canteiros elevados
a cobertura morta | le paillis | A cobertura morta mantém a humidade do solo. | Le paillis retient l'humidité dans le sol. | g? | pl=coberturas mortas
o composto | le compost | O composto precisa de ar, não só de tempo. | Le compost a besoin d'air, pas seulement de temps.
a estaca | la bouture | De uma estaca nasce um arbusto em dois anos. | D'une bouture naît un arbuste en deux ans.
a estrutura do imóvel | la structure du bâti | A estrutura do imóvel é melhor do que a primeira impressão. | La structure du bâti est meilleure que la première impression. | g? | pl=estruturas do imóvel
o excesso de colheita | la surproduction de récolte | Em agosto há o excesso de abobrinha de sempre. | En août règne l'habituelle surabondance de courgettes. | pl=excessos de colheita | ex?
a fabricação | la fabrication | A produção funciona em dois turnos. | La fabrication tourne en deux équipes. | pl=fabricações | ex?
a falta de moradia | la crise du logement | Na cidade há falta de moradia há anos. | La ville connaît une crise du logement depuis des années. | g? | pl=faltas de moradia
a frequência de rega | le rythme d'arrosage | Mais importante do que a quantidade é a frequência da rega. | Plus important que la quantité est le rythme d'arrosage. | g? | pl=frequências de rega | ex?
o grampo sargento | le serre-joint | Dois grampos substituem uma terceira mão. | Deux serre-joints remplacent une troisième main. | pl=grampos sargentos | ex?
o imóveis vazios | la vacance (de logements) | A taxa de imóveis vazios é de oito por cento. | Le taux de vacance est de huit pour cent. | g? | pl=imóveis vazios
a infestação de pragas | l'infestation | A infestação passou semanas sem ser notada. | L'infestation est passée inaperçue des semaines. | g? | pl=infestações de pragas | ex?
o instruções | le mode d'emploi | As instruções são bem complicadas. | Le mode d'emploi est plutôt compliqué. | g? | pl=instruções
o isolamento térmico | l'isolation |  |  | pl=isolamentos térmicos | ex=?
a liga | l'alliage | O canal liga dois rios. | Le canal relie deux rivières. | g?
a lixa | le papier de verre | No final, mais uma passada com lixa fina. | Pour finir, encore un passage au papier de verre fin. | g?
o local | l'emplacement, exposition | Ela é sócia de um clube local. | Elle est membre d'une association locale. | g?
a lâmina de serra | la lame de scie | Uma lâmina cega lasca a madeira. | Une lame émoussée arrache le bois. | pl=lâminas de serra | ex?
o manual de montagem | la notice de montage | O manual de montagem é só de desenhos, sem palavras. | La notice de montage est faite d'images sans mots. | pl=manuais de montagem
a massa corrida | l'enduit de rebouchage | A massa corrida precisa de secar totalmente. | L'enduit doit sécher complètement. | g? | pl=massas corridas
a meia-sombra | la mi-ombre | A samambaia quer meia-sombra e solo húmido. | La fougère veut la mi-ombre et un sol humide. | g? | pl=meias-sombras
o metro dobrável | le mètre pliant |  |  | pl=metros dobráveis | ex=?
a modernização | la modernisation |  |  | pl=modernizações | ex=?
a muda | le plant, jeune pousse | O horário muda semana que vem. | L'emploi du temps change la semaine prochaine.
a peça bruta | l'ébauche, pièce brute | Da peça bruta sai um cabo em três horas. | De l'ébauche naît une poignée en trois heures. | pl=peças brutas
o plano de zoneamento | le plan local d'urbanisme | O plano de zoneamento aqui só permite três andares. | Le plan d'urbanisme n'autorise ici que trois étages. | pl=planos de zoneamento
a poda | la taille (des végétaux) | A poda é feita no fim do inverno. | La taille se fait à la fin de l'hiver. | g?
a precisão de encaixe | la précision d'ajustement | A precisão de encaixe fica abaixo de um décimo de milímetro. | La précision d'ajustement est sous le dixième de millimètre. | g? | pl=precisões de encaixe
a raízes | le système racinaire | As raízes vão mais longe do que a copa. | Le système racinaire s'étend plus loin que la couronne. | pl=raízes
o rejunte | le joint | Os rejuntes ficaram pretos. | Les joints ont noirci.
a resistência ao frio | la rusticité | A resistência ao frio vem em letra pequena na etiqueta. | La rusticité est indiquée en petit sur l'étiquette. | g? | pl=resistências aos frios
o revestimento | le revêtement | O revestimento dura dez anos; a chapa, trinta. | Le revêtement tient dix ans, la tôle trente.
a rosca | le filetage | A rosca espanou. | Le filetage est arraché. | g?
a semeadura | le semis | A semeadura começa depois das geadas de maio. | Le semis commence après les saints de glace. | g?
o silicone | le silicone | O silicone encolhe ao secar. | Le silicone se rétracte en séchant.
a sublocação | la sous-location | Ele mora de sublocação na casa de uma colega. | Il est en sous-location chez une collègue. | pl=sublocações
o suporte | la fixation, support | O suporte aguenta vinte quilos. | La fixation supporte vingt kilos.
o tombamento | la protection du patrimoine | A casa é tombada. | La maison est classée au patrimoine. | ex?
o trabalho sob medida | le travail sur mesure | Aquilo foi trabalho sob medida, não produção em série. | C'était du sur-mesure, pas de la série. | pl=trabalhos sobs medidas
a urbanização | la viabilisation (d'un terrain) | Urbanizar o terreno custa mais do que construir. | La viabilisation du terrain coûte plus cher que la construction. | pl=urbanizações | ex?
o uso temporário | l'occupation temporaire | Até a demolição, o espaço é usado temporariamente como ateliê. | Jusqu'à la démolition, une occupation temporaire comme atelier est prévue. | pl=usos temporários | ex?
a época de floração | la période de floraison | A floração dura menos de três semanas. | La floraison dure à peine trois semaines. | g? | pl=épocas de floração | ex?
""",
"saude_c1_pt": """
o acompanhamento dos familiares | l'accompagnement des proches | Acompanhar os familiares faz parte da profissão, mas não está em plano nenhum. | L'accompagnement des proches fait partie du métier, mais ne figure dans aucun plan. | pl=acompanhamentos dos familiares | ex?
o acompanhamento pós-tratamento | le suivi post-thérapeutique | O acompanhamento depois do tratamento é tão importante quanto o tratamento. | Le suivi est aussi important que le traitement. | pl=acompanhamentos poses-tratamentos | ex?
a administração de medicamentos | l'administration des médicaments | A administração de medicamentos é registrada toda vez. | L'administration des médicaments est documentée chaque fois. | g? | pl=administrações de medicamentos
o alongamento | l'étirement | O alongamento é no final, não no começo. | L'étirement va à la fin, pas au début.
a ausência de sintomas | l'absence de symptômes | Ausência de sintomas não significa cura. | L'absence de symptômes ne signifie pas la guérison. | g? | pl=ausências de sintomas
a bula | la notice (de médicament) | Na bula está tudo e nada. | La notice dit tout et rien.
a capacidade de autocura | les capacités d'auto-guérison | Não se deve subestimar a capacidade de autocura do corpo. | Il ne faut pas sous-estimer les capacités d'auto-guérison. | g? | pl=capacidades de autocura
a capacidade de reação | la capacité de réaction | O cansaço diminui os reflexos mais do que uma cerveja. | La fatigue diminue la capacité de réaction plus qu'une bière. | pl=capacidades de reação | ex?
a casa de cuidados paliativos | l'unité de soins palliatifs | Na casa de cuidados paliativos trabalham mais voluntários do que funcionários. | Dans l'unité de soins palliatifs, il y a plus de bénévoles que de salariés. | pl=casas de cuidados paliativos
a centro-dia | l'accueil de jour | Três vezes por semana ela vai ao centro-dia. | Trois fois par semaine, elle va à l'accueil de jour. | g? | pl=centros-dias
a chance de cura | la chance de guérison | Detectado cedo, as chances de cura são muito boas. | Détectées tôt, les chances de guérison sont très bonnes. | pl=chances de cura
o comportamento compulsivo | la conduite addictive | O comportamento compulsivo raramente começa pela própria substância. | La conduite addictive commence rarement par la substance elle-même. | pl=comportamentos compulsivos
o contrato de cuidados | le contrat de prise en charge | O contrato de cuidados vale por doze meses. | Le contrat de prise en charge court sur douze mois. | pl=contratos de cuidados
a coordenação motora fina | la motricité fine |  |  | g? | pl=coordenações motoras finas | ex=?
os cuidados paliativos | les soins palliatifs | Os cuidados paliativos começam mais cedo do que a maioria pensa. | Les soins palliatifs commencent plus tôt qu'on ne croit.
a dependência | la dépendance | A dependência desenvolveu-se ao longo de anos. | La dépendance s'est développée sur des années. | g?
o desempenho máximo | la performance maximale |  |  | pl=desempenhos máximos | ex=?
o distúrbio do sono | le trouble du sommeil | Os distúrbios do sono muitas vezes são o primeiro sinal. | Les troubles du sommeil sont souvent le premier signe. | pl=distúrbios do sono
a doença preexistente | l'antécédent médical | Com doenças preexistentes é preciso cuidado especial. | En cas d'antécédents médicaux, une prudence particulière s'impose. | g? | pl=doenças preexistentes
a dor muscular | les courbatures | A dor muscular só veio dois dias depois. | Les courbatures ne sont venues que le surlendemain. | g? | pl=dores musculares
o esgotamento | l'épuisement | O esgotamento só veio depois das férias. | L'épuisement n'est venu qu'après les vacances.
a evolução da doença | l'évolution de la maladie | A evolução da doença foi mais leve do que se temia. | L'évolution de la maladie a été plus douce que redouté. | g? | pl=evoluções da doença
a flexibilidade | la souplesse, mobilité | Com a idade, a primeira coisa a ir embora é a flexibilidade. | Avec l'âge, c'est la souplesse qui part en premier. | g?
o grau de dependência | le niveau de dépendance | O grau de dependência define cada benefício. | Le niveau de dépendance décide de chaque prestation. | pl=graus de dependência
a internação temporária | l'hébergement temporaire | Depois do hospital vieram quatro semanas de internação temporária. | Après l'hôpital, quatre semaines d'hébergement temporaire ont suivi. | pl=internações temporárias
o limiar de dor | le seuil de douleur | Cada um tem um limiar de dor diferente. | Chacun a un seuil de douleur différent. | pl=limiares de dor
o má postura | la mauvaise posture | Anos de má postura não se corrigem em uma semana. | Des années de mauvaise posture ne se corrigent pas en une semaine. | g? | pl=más posturas
a obrigação de registo | l'obligation de traçabilité | A obrigação de registrar tudo come um terço do tempo de trabalho. | L'obligation de traçabilité mange un tiers du temps de travail. | g? | pl=obrigações de registo | ex?
o perfil de efeitos colaterais | le profil d'effets secondaires | O perfil de efeitos colaterais é desfavorável para idosos. | Le profil d'effets secondaires est défavorable aux personnes âgées. | pl=perfis de efeitos colaterais
o plano de treino | le plan d'entraînement |  |  | g? | pl=planos de treino | ex=?
a pressão da competição | la pression de la compétition | Sob a pressão da competição tudo muda. | Sous la pression de la compétition, tout change. | g? | pl=pressões da competição
o processo de recuperação | le processus de guérison | O processo de recuperação correu sem contratempos. | Le processus de guérison s'est déroulé sans rechute. | pl=processos de recuperação
a proteção vacinal | la protection vaccinale | A proteção da vacina diminui depois de alguns anos. | La protection vaccinale diminue après quelques années. | g? | pl=proteções vacinais | ex?
o quadro clínico | le tableau clinique | O quadro clínico não corresponde a nenhum diagnóstico conhecido. | Le tableau clinique ne correspond à aucun diagnostic connu. | pl=quadros clínicos
o repouso | le repos au lit | O médico receitou três dias de repouso. | Le médecin a prescrit trois jours de repos au lit.
a ruptura de ligamento | la rupture ligamentaire | A ruptura de ligamento aconteceu na aterrissagem. | La rupture ligamentaire s'est produite à la réception. | g? | pl=rupturas de ligamento
a ruptura de tendão | la rupture de tendon | Uma ruptura de tendão significa seis meses parado. | Une rupture de tendon signifie six mois d'arrêt. | pl=rupturas de tendão
o senso de equilíbrio | le sens de l'équilibre | O equilíbrio pode ser treinado como um músculo. | Le sens de l'équilibre s'entraîne comme un muscle. | pl=sensos de equilíbrio | ex?
o serviço de apoio | l'offre de répit | O serviço de apoio quase não é usado porque quase ninguém o conhece. | L'offre de répit est peu utilisée parce qu'elle est peu connue. | pl=serviços de apoio
a sobrecarga | la surmenage, surcharge | A lesão foi uma típica sobrecarga. | La blessure était une surcharge classique. | g?
a tensão muscular | la contracture, tension musculaire | Com tensão muscular eu faria uma massagem nas costas. | En cas de tensions, je me ferais masser le dos. | g? | pl=tensões musculares
o tratamento da dor | le traitement de la douleur | Um bom tratamento da dor muda tudo. | Un bon traitement de la douleur change tout. | g? | pl=tratamentos da dor
a técnica de respiração | la technique respiratoire | A técnica de respiração certa economiza uma força surpreendente. | La bonne technique respiratoire économise étonnamment de la force. | g? | pl=técnicas de respiração
o tónus | le gainage, tonus corporel | Sem estabilidade do corpo a melhor técnica não adianta. | Sans gainage, la meilleure technique ne sert à rien. | g? | pl=tónus | ex?
a visita domiciliar | la visite à domicile | A visita domiciliar dura menos de uma hora. | La visite à domicile dure une petite heure. | g? | pl=visitas domiciliares
""",
"roupa_c1_pt": """
o amassado | le faux pli | Linho sempre amassa, faz parte. | Le lin fait toujours des faux plis, cela en fait partie. | ex?
a barra | l'ourlet | Ainda dá para soltar a barra dois centímetros. | L'ourlet peut encore être rallongé de deux centimètres. | g?
o caimento | la coupe, tombé | O caimento está certo, a cor não. | La coupe est bonne, la couleur non.
o conforto | le confort de port | Em conforto o algodão ganha de tudo. | Pour le confort, le coton bat tout.
a costura | la couture (ligne) | A costura abriu no ombro. | La couture a lâché à l'épaule. | g?
o código de vestimenta | le code vestimentaire | Aqui não existe mais código de vestimenta formal. | Il n'y a plus ici de code vestimentaire formel. | pl=códigos de vestimenta
o forro | la doublure | O forro estraga-se mais rápido do que o tecido. | La doublure s'abîme plus vite que le tissu.
o modismo | le phénomène de mode | Aquilo foi um modismo, não uma evolução. | C'était un phénomène de mode, pas une évolution.
o molde | le patron (couture) | O molde é dos anos cinquenta. | Le patron date des années cinquante.
a peça sob medida | le confection sur mesure | Uma peça sob medida custa três vezes mais e dura dez vezes mais. | Un sur-mesure coûte trois fois plus et dure dix fois plus. | pl=peças sobs medidas
o punho | le bord-côte, poignet | Os punhos estão lasseados. | Les bords-côtes sont détendus.
a qualidade do acabamento | la qualité de fabrication | A qualidade do acabamento vê-se do lado de dentro. | La qualité de fabrication se voit à l'intérieur. | g? | pl=qualidades do acabamento
a resistência da cor | la solidité des couleurs | A resistência da cor foi testada depois da terceira lavagem. | La solidité des couleurs a été vérifiée après trois lavages. | g? | pl=resistências da cor
""",
"natureza_c1_pt": """
o abafamento | la lourdeur, air moite | O mormaço geralmente termina em chuva à noite. | La lourdeur se décharge le plus souvent le soir. | ex?
o abastecimento de água potável | l'approvisionnement en eau potable | No verão o abastecimento de água potável fica no limite. | L'approvisionnement en eau potable est tendu en été. | pl=abastecimentos de água potável
a abertura de sol | l'éclaircie | À tarde há breves aberturas de sol. | L'après-midi apporte de brèves éclaircies. | pl=aberturas de sol
o adestramento | le dressage | O adestramento baseia-se na repetição, não na severidade. | Le dressage repose sur la répétition, pas sur la sévérité.
a alerta de temporal | l'alerte météo | Há alerta de temporal para o sul. | Une alerte météo est en vigueur pour le sud. | g? | pl=alertas de temporal
a amurada | le bastingage | Ele passou a travessia inteira na amurada. | Il est resté au bastingage toute la traversée.
o animal da mesma espécie | le congénère | Sem outros da mesma espécie o animal definha. | Sans congénères, l'animal dépérit. | pl=animais da mesma espécie | ex?
o aquecimento global | le réchauffement de la planète | O aquecimento global não pode mais ser detido, só freado. | Le réchauffement de la planète ne peut plus être arrêté, seulement freiné. | pl=aquecimentos globais
a arrebentação | le ressac, brisants | A arrebentação fazia mais barulho do que o vento. | Le ressac était plus bruyant que le vent. | g? | pl=arrebentações
o atracadouro | l'embarcadère | O atracadouro foi reformado depois da tempestade. | L'embarcadère a été refait après la tempête.
a bacia do porto | le bassin portuaire | Na antiga bacia do porto hoje ficam casas flutuantes. | Dans l'ancien bassin portuaire mouillent aujourd'hui des péniches d'habitation. | g? | pl=bacias do porto
o baixio | le haut-fond | Os baixios não aparecem em nenhum mapa antigo. | Les hauts-fonds ne figurent sur aucune vieille carte.
o banco de neblina | le banc de brouillard | No vale persiste um banco de neblina denso. | Un banc de brouillard dense persiste dans la vallée. | pl=bancos de neblina
o bem-estar animal | le bien-être animal | Bem-estar animal custa dinheiro, e alguém tem de pagar. | Le bien-être animal coûte de l'argent, et quelqu'un doit le payer. | g? | pl=bens-estares animais
a cadeia alimentar | la chaîne alimentaire | No fim da cadeia alimentar tudo se acumula. | Au bout de la chaîne alimentaire, tout s'accumule. | pl=cadeias alimentares
o cardume | le banc, essaim, nuée | O cardume muda de direção como um único animal. | Le banc change de direction comme un seul animal.
o cascalho | l'éboulis | O caminho passa por cascalho solto. | Le chemin passe sur des éboulis instables.
a charneca | la lande | Em agosto a charneca floresce em roxo. | En août, la lande fleurit en violet. | g?
a chuva de granizo | l'averse de grêle | Uma rápida chuva de granizo destruiu metade da colheita. | Une brève averse de grêle a détruit la moitié de la récolte. | g? | pl=chuvas de granizo
a clareira | la clairière | Na clareira de repente ficou tudo em silêncio. | Dans la clairière, le silence s'est fait d'un coup.
o comportamento migratório | le comportement migratoire | O comportamento migratório das cegonhas mudou. | Le comportement migratoire des cigognes a changé. | pl=comportamentos migratórios
o comportamento territorial | le comportement territorial |  |  | pl=comportamentos territoriais | ex=?
a correnteza | le courant | A correnteza aqui é mais forte do que parece. | Le courant est ici plus fort qu'il n'en a l'air. | g?
a criação de animais | la élevage, détention d'animaux | A criação de animais está sujeita a regras. | La détention d'animaux est soumise à des conditions. | g? | pl=criações de animais
o degelo | la fonte des neiges | Depois do degelo o riacho transborda. | Après la fonte des neiges, le ruisseau est en crue.
o descarte | l'élimination (des déchets) | O descarte de tintas velhas é cobrado à parte. | L'élimination des vieilles peintures coûte un supplément.
a direção do vento | la direction du vent | Com a direção do vento muda também o cheiro. | Avec la direction du vent tourne aussi l'odeur. | g? | pl=direções do vento
a distância de fuga | la distance de fuite | Na cidade a distância de fuga dos pássaros diminui. | En ville, la distance de fuite des oiseaux diminue. | g? | pl=distâncias de fuga
a enchente | l'inondation | Depois da enchente o porão ficou húmido por semanas. | Après l'inondation, la cave est restée humide des semaines.
a encosta íngreme | la pente raide | Na encosta íngreme ainda crescem videiras antigas. | Sur la pente raide pousse encore de la vigne ancienne. | pl=encostas íngremes
a erosão do solo | l'érosion des sols | Sem sebes a erosão do solo aumenta rápido. | Sans haies, l'érosion des sols augmente rapidement. | g? | pl=erosões do solo
a escassez de matérias-primas | la pénurie de matières premières | A escassez de matérias-primas faz os preços subirem há meses. | La pénurie de matières premières fait monter les prix depuis des mois. | g? | pl=escassezes de matérias-primas
a exigência ambiental | la contrainte environnementale | A construção nova teve de cumprir exigências ambientais rigorosas. | La construction a dû remplir de strictes contraintes environnementales. | g? | pl=exigências ambientais
a extinção de espécies | l'extinction des espèces | A extinção de espécies avança mais rápido do que nunca. | L'extinction des espèces se déroule plus vite que jamais. | g? | pl=extinções de espécies
a fertilidade do solo | la fertilité du sol |  |  | g? | pl=fertilidades do solo | ex=?
o fertilizante | l'engrais | Os fertilizantes estão duas vezes mais caros desde a guerra. | Les engrais coûtent deux fois plus cher depuis la guerre.
a força da natureza | la force de la nature | Contra forças da natureza assim nenhum muro adianta. | Contre de telles forces de la nature, aucun mur ne sert. | g? | pl=forças da natureza
a força do vento | la force du vent | Com vento força oito a balsa fica no porto. | À force huit, le ferry reste au port. | g? | pl=forças do vento | ex?
a foz | l'embouchure, confluent | Na foz o rio de repente fica largo. | À l'embouchure, la rivière devient soudain large.
a frente de tempestade | le front orageux | A frente de tempestade chega aqui perto da meia-noite. | Le front orageux nous atteint vers minuit. | g? | pl=frentes de tempestade
""",
"natureza_c1_pt_2": """
o gás de efeito estufa | le gaz à effet de serre | O metano é um gás de efeito estufa muito mais potente do que o CO2. | Le méthane est un gaz à effet de serre bien plus puissant que le CO2. | pl=gases de efeito estufa
a hibernação | l'hibernation | A hibernação começa mais tarde do que antigamente. | L'hibernation commence plus tard qu'autrefois. | g? | pl=hibernações
a humidade do ar | l'humidité de l'air | Com esta humidade nada seca. | Avec cette humidité, rien ne sèche. | pl=humidades do ar | ex?
o impacto ambiental | la compatibilité environnementale | O impacto ambiental é avaliado antes da obra. | La compatibilité environnementale est examinée avant les travaux. | pl=impactos ambientais
o limite da vegetação arbórea | la limite des arbres | Acima do limite das árvores só cresce capim. | Au-dessus de la limite des arbres ne pousse plus que de l'herbe. | pl=limites da vegetação arbórea | ex?
o limite de congelamento | la limite de gel | O limite de congelamento desce para oitocentos metros. | La limite de gel descend à huit cents mètres. | pl=limites de congelamento
a linha costeira | le littoral, trait de côte | A linha costeira mudou desde 1900. | Le trait de côte s'est déplacé depuis 1900. | g? | pl=linhas costeiras
o mar agitado | la état de la mer, houle | Com este mar agitado nenhum barco sai. | Par cette houle, aucun bateau ne sort. | pl=mares agitados
o mar de wadden | la mer des Wadden, estran | O mar de Wadden seca duas vezes por dia. | L'estran découvre deux fois par jour. | pl=mares de wadden
a maré baixa | la marée basse | Na maré baixa dá para ir a pé até a ilha. | À marée basse, on peut marcher jusqu'à l'île. | pl=marés baixas
as marés | les marées | Aqui as marés determinam o dia inteiro. | Les marées règlent ici toute la journée.
o material particulado fino | les particules fines | Neste cruzamento o material particulado fica sempre acima do limite. | À ce carrefour, les particules fines dépassent durablement la limite. | pl=materiais particulados finos | ex?
a matilha | la meute, harde | A matilha percorre mais de cem quilómetros por mês. | La meute parcourt plus de cent kilomètres par mois. | g?
o navio cargueiro | le cargo | O cargueiro espera há três dias para entrar no porto. | Le cargo attend depuis trois jours pour entrer. | pl=navios cargueiros | ex?
a nebulosidade | la nébulosité | A nebulosidade aumenta no fim da tarde. | La nébulosité augmente vers le soir. | g?
a ninhada | la portée (petits) | A ninhada teve seis filhotes. | La portée comptait six petits. | g?
o nível do mar | le niveau de la mer | O nível do mar sobe devagar, mas sem parar. | Le niveau de la mer monte lentement mais sûrement. | pl=níveis do mar
a orla da floresta | la lisière de forêt | Na orla da floresta ficam as árvores mais antigas. | À la lisière de la forêt se dressent les arbres les plus vieux. | pl=orlas da floresta
a pecuária extensiva | l'économie pastorale | O pastoreio mantém a paisagem aberta. | L'économie pastorale maintient le paysage ouvert. | g? | pl=pecuárias extensivas | ex?
o perigo no mar | la détresse en mer | O barco entrou em perigo no mar. | Le bateau s'est trouvé en détresse en mer. | pl=perigos nos mares
a pesca | la pêche (activité) | Da pesca ainda vivem quatro famílias. | Quatre familles vivent encore de la pêche.
o poluente | le polluant | Os poluentes acumulam-se no solo. | Les polluants se déposent dans le sol.
a poluição sonora | la nuisance sonore | A poluição sonora do aeroporto nunca foi medida. | La nuisance sonore de l'aéroport n'a jamais été mesurée. | g? | pl=poluições sonoras
a população de animais selvagens | la population de gibier | A população de animais selvagens é contada toda primavera. | La population de gibier est comptée chaque printemps. | g? | pl=populações de animais selvagens
a presa | la proie | A presa fareja o caçador muito antes. | La proie flaire le chasseur bien avant. | g?
o preço da terra | le prix du foncier | O preço da terra triplicou em dez anos. | Les prix du foncier ont triplé en dix ans. | pl=preços da terra
a produção de leite | la production laitière | A produção de leite por vaca dobrou. | La production laitière par vache a doublé. | g? | pl=produções de leite
a rajada de vento | la rafale | Algumas rajadas chegam a cem quilómetros por hora. | Certaines rafales atteignent cent kilomètres à l'heure. | g? | pl=rajadas de vento | ex?
o recurso mineral | la ressource du sous-sol | O país vive dos seus recursos minerais. | Le pays vit de ses ressources du sous-sol. | pl=recursos minerais
o reflorestamento | le reboisement | O reflorestamento leva décadas; o desmatamento, uma tarde. | Le reboisement demande des décennies, le déboisement un après-midi.
a renaturalização | la renaturation | A renaturalização do rio leva dez anos. | La renaturation de la rivière prendra dix ans. | g? | pl=renaturalizações
o rendimento da colheita | le rendement de la récolte | A colheita rendeu um terço abaixo da média. | Le rendement était d'un tiers sous la moyenne. | pl=rendimentos da colheita | ex?
a rotação de culturas | la rotation des cultures | Sem rotação de culturas o solo esgota-se. | Sans rotation des cultures, le sol s'épuise. | pl=rotações de culturas
as sementes | les semences | As sementes vêm de três grandes grupos. | Les semences proviennent de trois groupes.
a sobrepesca | la surpêche | A sobrepesca é mais antiga do que qualquer cota. | La surpêche est plus ancienne que tout quota. | g?
a sucessão na quinta | la reprise de la ferme | A sucessão na quinta não está resolvida. | La reprise de la ferme n'est pas réglée. | g? | pl=sucessões nas quintas
o tamanho da população | l'effectif (population animale) |  |  | pl=tamanhos da população | ex=?
o tipo de solo | la nature du sol | O tipo de solo decide a variedade. | La nature du sol décide du cépage. | pl=tipos de solo
o trabalhador temporário da colheita | le saisonnier agricole | Sem trabalhadores da colheita a lavoura fica parada. | Sans saisonniers, le champ reste sur pied. | pl=trabalhadores temporários da colheita | ex?
a turfeira | la tourbière, marais | A turfeira armazena mais carbono do que a floresta. | La tourbière stocke plus de carbone que la forêt. | g?
o uso responsável dos recursos | la préservation des ressources | O uso responsável dos recursos começa nas compras. | La préservation des ressources commence à l'achat. | pl=usos responsáveis dos recursos
a variação de temperatura | la variation de température | As variações de temperatura prejudicam as videiras. | Les variations de température éprouvent les vignes. | pl=variações de temperatura
a venda direta | la vente directe | A venda direta rende mais do que o atacado. | La vente directe rapporte plus que le commerce de gros. | g? | pl=vendas diretas
a zona de alta pressão | l'anticyclone | Uma zona de alta pressão traz duas semanas tranquilas. | Un anticyclone apporte deux semaines calmes. | pl=zonas de alta pressão
a zona de baixa pressão | la dépression | A zona de baixa pressão está a passar pelo Mar do Norte. | La dépression passe au-dessus de la mer du Nord. | g? | pl=zonas de baixa pressão
a área cultivada | la surface cultivée | A área cultivada de trigo encolheu. | La surface cultivée en blé a diminué. | g? | pl=áreas cultivadas
a área livre | l'espace de sortie, parcours | As galinhas ficam soltas todos os dias. | Les poules ont un parcours extérieur chaque jour. | g? | pl=áreas livres | ex?
a época de reprodução | la période de nidification | Na época de reprodução o caminho fica fechado. | Pendant la nidification, le chemin reste fermé. | pl=épocas de reprodução
""",
"viagens_c1_pt": """
o cancelamento da viagem | l'annulation de voyage | O seguro só cobre o cancelamento da viagem em caso de doença. | L'assurance ne couvre l'annulation qu'en cas de maladie. | pl=cancelamentos da viagem
o circuito | le circuit | O circuito passa por quatro países. | Le circuit traverse quatre pays.
o despacho de bagagem | l'enregistrement des bagages | O despacho de bagagem fecha quarenta minutos antes do voo. | L'enregistrement des bagages ferme quarante minutes avant le départ. | pl=despachos de bagagem
o desvio | la déviation | O desvio passa por três vilarejos. | La déviation passe par trois villages.
o estreitamento | le goulet, passage étroit | No estreitamento engarrafa todas as manhãs. | Au goulet, ça bouchonne chaque matin.
a etapa de expansão | la phase d'aménagement | A segunda etapa de expansão ainda não tem financiamento. | La deuxième phase d'aménagement n'est pas encore financée. | g? | pl=etapas de expansão
a frequência | le cadencement | Uma frequência maior ajudaria mais do que comboios novos. | Un cadencement plus serré apporterait plus que de nouveaux trains.
a infraestrutura de recarga | l'infrastructure de recharge | Sem infraestrutura de recarga o melhor carro não serve para nada. | Sans infrastructure de recharge, la meilleure voiture ne sert à rien. | pl=infraestruturas de recarga
o ir e voltar | le fait de faire la navette | O deslocamento diário custa a ele duas horas. | La navette quotidienne lui coûte deux heures. | g? | pl=ires e voltares | ex?
a malha | le réseau de lignes | A malha é mais velha do que os comboios. | Le réseau de lignes est plus vieux que les véhicules. | g?
o número de passageiros | le nombre de voyageurs | O número de passageiros volta a subir aos poucos. | Le nombre de voyageurs remonte lentement. | pl=números de passageiros
o pacote de viagem | le voyage à forfait | Num pacote de viagem a operadora responde por tudo. | Dans un voyage à forfait, l'organisateur répond de tout. | pl=pacotes de viagem
a preferência | la priorité | Quem vem da direita tem a preferência, mesmo sem placa. | La priorité vient de droite, même sans panneau. | g?
a proibição de circular | l'interdiction de circuler | Para carros a diesel antigos vale uma proibição de circular. | Une interdiction de circuler s'applique aux vieux diesels. | pl=proibições de circular
a regra de entrada | la condition d'entrée | As regras de entrada mudam quase todos os meses. | Les conditions d'entrée changent presque tous les mois. | pl=regras de entrada
a remarcação | le changement de réservation | Uma remarcação custa mais do que o voo. | Un changement de réservation coûte plus cher que le vol. | pl=remarcações
a rota alternativa | l'itinéraire de contournement | A rota alternativa é mais longa, mas mais confiável. | L'itinéraire de contournement est plus long, mais plus fiable. | g? | pl=rotas alternativas
a segurança no trânsito | la sécurité routière | A segurança no trânsito melhorou muito desde os anos oitenta. | La sécurité routière s'est fortement améliorée depuis les années quatre-vingt. | g? | pl=seguranças nos trânsitos
o seguro-saúde para viagem internacional | l'assurance maladie à l'étranger |  |  | g? | pl=seguros-saúdes paras viagens internacionais | ex=?
o tempo de permanência | la durée de séjour | O tempo de permanência permitido é de noventa dias. | La durée de séjour autorisée est de quatre-vingt-dix jours. | pl=tempos de permanência
a transição da mobilidade | la transition des mobilités | A transição da mobilidade raramente fracassa por falta de dinheiro. | La transition des mobilités échoue rarement faute d'argent. | g? | pl=transições da mobilidade
o transporte de longa distância | le transport longue distance | No transporte de longa distância valem outras tarifas. | Le transport longue distance applique d'autres tarifs. | pl=transportes de longa distância
o transporte local | le transport de proximité | O transporte local é pago pelas prefeituras. | Le transport de proximité est payé par les villes. | pl=transportes locais
a travessia da fronteira | le passage de frontière | A travessia da fronteira foi sem controle. | Le passage de la frontière s'est fait sans contrôle. | g? | pl=travessias da fronteira
o volume de tráfego | le trafic, volume de circulation | O volume de tráfego quase não se recuperou desde 2019. | Le volume de circulation ne s'est guère rétabli depuis 2019. | pl=volumes de tráfego
""",
"cidade_c1_pt": """
o bairro periférico | le quartier périphérique | Nos bairros periféricos os rendas ainda são acessíveis. | Dans les quartiers périphériques, les loyers restent abordables. | pl=bairros periféricos
o conjunto de ruas | l'enfilade de rues, îlot | O quarteirão inteiro é da mesma época. | Toute l'enfilade de rues date de la même époque. | pl=conjuntos de ruas | ex?
a construções | le urbanisation, bâti | As construções chegam até o rio. | Le bâti s'avance jusqu'à la rivière. | pl=construções
o eixo visual | la perspective visuelle | O prédio novo destrói a antiga vista para a catedral. | La construction neuve détruit l'ancienne perspective vers la cathédrale. | pl=eixos visuais | ex?
o espaço livre | l'espace libre | No centro, espaço livre é o bem mais caro. | L'espace libre est le bien le plus cher du centre-ville. | g? | pl=espaços livres
a moderação do tráfego | l'apaisement de la circulation | A moderação do tráfego reduziu o barulho pela metade. | L'apaisement de la circulation a réduit le bruit de moitié. | g? | pl=moderações do tráfego
os moradores | les riverains | Os moradores foram consultados tarde demais. | Les riverains ont été consultés trop tard.
a qualidade do espaço público | la qualité de séjour (espace public) | Sem bancos, ninguém quer ficar no lugar. | Sans bancs, il n'y a pas de qualité de séjour. | pl=qualidades do espaço público | ex?
a valorização | la revalorisation, gentrification | A valorização do bairro expulsa justamente quem o construiu. | La revalorisation du quartier chasse justement ceux qui l'ont façonné. | g? | pl=valorizações
a área verde | l'espace vert | Sobram quatro metros quadrados de área verde por habitante. | Il reste quatre mètres carrés d'espace vert par habitant. | g? | pl=áreas verdes
""",
"escola_c1_pt": """
o achado incidental | la découverte fortuite (examen) | O tumor foi um achado puramente incidental. | La tumeur était une pure découverte fortuite. | pl=achados incidentais | ex?
o agente patogénico | l'agent pathogène | O agente patogénico só foi identificado semanas depois. | L'agent pathogène n'a été identifié que des semaines plus tard. | pl=agentes patogénicos
a aproximação | l'approximation | O resultado é só uma aproximação grosseira. | Le résultat n'est qu'une approximation grossière. | pl=aproximações
o avanço decisivo | la percée | O avanço decisivo veio de um grupo de trabalho bem pequeno. | La percée est venue d'une toute petite équipe. | pl=avanços decisivos
a comparabilidade | la comparabilité | Sem critérios iguais não há comparabilidade nenhuma. | Sans critères identiques, toute comparabilité disparaît.
o conselho de classe | le conseil de classe |  |  | pl=conselhos de classe | ex=?
a dependência de cuidados | la dépendance (besoin de soins) |  |  | g? | pl=dependências de cuidados | ex=?
o erro médico | l'erreur médicale | Não foi possível comprovar um erro médico. | Aucune erreur médicale n'a pu être prouvée. | pl=erros médicos
o esclarecimento | l'information, éclaircissement | Antes da intervenção é obrigatório um esclarecimento detalhado. | Avant l'intervention, une information détaillée est obligatoire.
a expectativa de vida | l'espérance de vie | A expectativa de vida sobe lentamente há décadas. | L'espérance de vie augmente lentement depuis des décennies. | g? | pl=expectativas de vida
o ganho de conhecimento | le gain de connaissance | O ganho de conhecimento mal justifica o esforço. | Le gain de connaissance justifie à peine l'effort. | pl=ganhos de conhecimento
a justificativa de falta | le justificatif d'absence | Sem justificativa por escrito, a falta não é abonada. | Sans justificatif écrit, l'absence est considérée comme injustifiée. | g? | pl=justificativas de falta | ex?
o levantamento | l'enquête, collecte de données | O levantamento abrangeu dois mil domicílios. | L'enquête portait sur deux mille ménages.
o meio especializado | le milieu spécialisé, les spécialistes | O estudo teve uma receção controversa entre os especialistas. | L'étude a été reçue de façon controversée par les spécialistes. | pl=meios especializados | ex?
a mudança de escola | le changement d'école | A mudança de escola foi mais difícil para ela do que o esperado. | Le changement d'école lui a été plus difficile que prévu. | g? | pl=mudanças de escola
a nota do boletim | la note du bulletin | A nota do boletim é a média de quatro provas. | La note du bulletin se compose de quatre devoirs. | g? | pl=notas do boletim
a pesquisa básica | la recherche fondamentale | A pesquisa básica só dá retorno depois de décadas. | La recherche fondamentale ne rapporte qu'après des décennies. | g? | pl=pesquisas básicas
a precisão da medição | la précision de mesure | A precisão da medição é de meio milímetro. | La précision de mesure est d'un demi-millimètre. | g? | pl=precisões da medição
o processo de inscrição | la procédure d'inscription | O processo de inscrição vai de janeiro a março. | La procédure d'inscription court de janvier à mars. | pl=processos de inscrição
o progresso | le progrès | O progresso no aprendizado é difícil de traduzir em notas. | Le progrès d'apprentissage se laisse difficilement traduire en notes.
a recaída | la rechute | Depois de dois anos houve uma recaída. | Au bout de deux ans, il y a eu une rechute.
o regimento escolar | le règlement intérieur | O regimento da escola fica pendurado ao lado da entrada. | Le règlement intérieur est affiché près de l'entrée. | pl=regimentos escolares | ex?
a reprodutibilidade | la reproductibilité | A reprodutibilidade do experimento nunca foi verificada. | La reproductibilité de l'expérience n'a jamais été vérifiée. | g?
a verificação | la vérification, contrôle | O resultado indicava uma segunda verificação. | Le résultat suggérait un second contrôle. | pl=verificações
a vigilância do recreio | la surveillance de récréation | A vigilância do recreio muda todas as semanas. | La surveillance de récréation change chaque semaine. | g? | pl=vigilâncias do recreio
""",
"cultura_c1_pt": """
a anacruse | l'anacrouse ; coup d'envoi | A anacruse já dá o andamento inteiro. | L'anacrouse donne déjà tout le tempo. | g?
a arcada | la conduite d'archet | Pela arcada reconhece-se a escola. | À la conduite d'archet, on reconnaît l'école.
a assembleia geral anual | l'assemblée générale annuelle | Dezoito sócios foram à assembleia geral. | Dix-huit membres sont venus à l'assemblée générale. | pl=assembleias gerais anuais | ex?
a campanha de doações | l'appel aux dons | A campanha de doações juntou o suficiente em três dias. | L'appel aux dons a rassemblé assez en trois jours. | g? | pl=campanhas de doações
a capacidade de processamento | la puissance de calcul | A capacidade de processamento não basta para esta tarefa. | La puissance de calcul ne suffit pas pour cette tâche. | g? | pl=capacidades de processamento
o caso de uso | le cas d'usage | Para este caso de uso a ferramenta é pesada demais. | Pour ce cas d'usage, l'outil est trop lourd. | pl=casos de uso
o cenário | le décor de scène | O cenário era composto por duas cadeiras. | Le décor se composait de deux chaises.
o conexão em rede | la mise en réseau | A interligação dos aparelhos traz riscos novos. | La mise en réseau des appareils apporte de nouveaux risques. | pl=conexões ens redes | ex?
o conjunto | la formation, ensemble | Planeamos o projeto em conjunto. | Nous avons planifié le projet ensemble.
a construção dos personagens | la caractérisation des personnages | A construção dos personagens é mais precisa do que a trama. | La caractérisation des personnages est plus fine que l'intrigue. | g? | pl=construções dos personagens
a contraluz | le contre-jour | Na contraluz o rosto perde todos os detalhes. | À contre-jour, le visage perd tout détail.
a criptografia | le chiffrement | Sem criptografia fica tudo exposto. | Sans chiffrement, tout est à découvert. | g?
o dedilhado | le doigté | O dedilhado está em letra pequena em cima das notas. | Le doigté est écrit en petit au-dessus des notes.
o desdobramento | les suite, conséquences | A noite teve desdobramentos judiciais. | La soirée a eu des suites judiciaires.
o direitos de encenação | le droit de représentation | Os direitos de encenação são da editora. | Le droit de représentation appartient à l'éditeur. | pl=direitos de encenação
o direitos de imagem | les droits d'image | Os direitos de imagem são do fotógrafo, não de quem encomendou. | Les droits d'image appartiennent au photographe, pas au commanditaire. | pl=direitos de imagem
a distância focal | la focale | A distância focal muda a perspectiva, não só o recorte. | La focale change la perspective, pas seulement le cadrage. | g? | pl=distâncias focais
o dominante de cor | la dominante colorée | A foto está puxada para o verde. | L'image a une dominante verte. | g? | pl=dominantes de cor | ex?
a edição de imagem | la retouche d'image | Sem edição nenhuma foto fica assim. | Sans retouche, aucune photo ne ressemble à cela. | pl=edições de imagem | ex?
a encenação | la mise en scène | A montagem foi mais polémica do que a peça. | La mise en scène a fait plus débat que la pièce. | pl=encenações | ex?
o enquadramento | le cadrage | Outro enquadramento conta outra história. | Un autre cadrage raconte une autre histoire.
o equilíbrio de volume | l'équilibre des volumes | O equilíbrio de volume entre coro e orquestra não estava certo. | L'équilibre entre le chœur et l'orchestre n'était pas bon. | pl=equilíbrios de volume
o espírito da época | l'esprit du temps | O filme capta com precisão o espírito da época. | Le film saisit exactement l'esprit du temps. | pl=espíritos da época
o estatuto | les statuts | O estatuto prevê eleições a cada dois anos. | Les statuts prévoient une élection tous les deux ans.
a estreia mundial | la création (première mondiale) | A estreia mundial foi num pátio dos fundos. | La création a eu lieu dans une arrière-cour. | g? | pl=estreias mundiais
o feitio | la facture, manière dont c'est fait | Pelo feitio reconhece-se na hora a idade do móvel. | À la facture, on reconnaît tout de suite l'âge du meuble.
a figura de linguagem | l'image, figure de style | A metáfora manca, mas fica na memória. | L'image cloche, mais elle marque. | pl=figuras de linguagem | ex?
a folha de partitura | la feuille de musique | A partitura caiu da estante no meio do concerto. | La feuille de musique est tombée du pupitre en plein concert. | g? | pl=folhas de partitura | ex?
a foto de arquivo | la photo d'archive | Trata-se de uma foto de arquivo de 2019. | Il s'agit d'une photo d'archive de 2019. | g? | pl=fotos de arquivo
o funcionamento | le mode d'action, fonctionnement | O funcionamento do processo é surpreendentemente simples. | Le mode d'action du procédé est étonnamment simple.
a imitação | l'imitation | A imitação é mais bem-feita do que o original. | L'imitation est mieux réalisée que l'original. | g? | pl=imitações
a improvisação | l'improvisation | A melhor improvisação é bem preparada. | La meilleure improvisation est bien préparée. | pl=improvisações
a interface | l'interface | A interface entre os dois sistemas é propensa a falhas. | L'interface entre les deux systèmes est sujette aux erreurs. | g?
a leitura | la lecture, interprétation | Há pelo menos duas leituras deste final. | Il y a au moins deux lectures de cette fin.
a linha melódica | la conduite mélodique | A linha melódica fica na mão esquerda. | La conduite mélodique est à la main gauche. | g? | pl=linhas melódicas
a linha narrativa | le fil narratif | A segunda trama fica sem resolução. | Le second fil narratif reste sans résolution. | g? | pl=linhas narrativas | ex?
a manutenção | la maintenance, entretien | A manutenção está prevista para a noite de domingo. | La maintenance est prévue pour dimanche nuit. | g? | pl=manutenções
o monitoramento | la surveillance | O monitoramento da rede funciona 24 horas por dia. | La surveillance du réseau fonctionne jour et nuit.
a métrica | le mètre (poésie) | A métrica quebra exatamente neste ponto. | Le mètre se rompt précisément à cet endroit. | g?
a obra-prima | le chef-d'œuvre | Hoje o livro é considerado uma obra-prima. | Le livre est aujourd'hui tenu pour un chef-d'œuvre. | g? | pl=obras-primas
""",
"cultura_c1_pt_2": """
a partitura | la partition (d'orchestre) | Na partitura há mais do que na folha de música. | La partition dit plus que la feuille de notes.
a perda de sócios | la perte d'adhérents | A perda de sócios atinge quase todos os clubes. | La perte d'adhérents touche presque tous les clubs. | g? | pl=perdas de sócios
o ponto de vista narrativo | le point de vue narratif | O ponto de vista narrativo muda no meio do capítulo. | Le point de vue narratif change au milieu du chapitre. | pl=pontos de vista narrativo
a profundidade de campo | la profondeur de champ | Com o diafragma aberto, a profundidade de campo vira centímetros. | À pleine ouverture, la profondeur de champ tombe à quelques centimètres. | g? | pl=profundidades de campo
a propensão a falhas | la vulnérabilité aux pannes | A propensão a falhas caiu pela metade desde a atualização. | La vulnérabilité aux pannes a été divisée par deux depuis la mise à jour. | g? | pl=propensões as falhas
a quebra de estilo | la rupture de style | O anexo é uma quebra total de estilo. | L'extension est une franche rupture de style. | pl=quebras de estilo | ex?
a reação do público | la réaction du public | A reação do público foi dividida. | La réaction du public était partagée. | g? | pl=reações do público
o refrão | le refrain | Depois de duas vezes todo mundo canta o refrão junto. | Après deux passages, tout le monde chante le refrain. | pl=refrões
o registo de associações | le registre des associations | A associação está no registo desde 1954. | L'association figure au registre depuis 1954. | pl=registos de associações | ex?
a regência | la direction (d'orchestre) | A regência foi contida e precisa. | La direction était sobre et précise. | g?
o relatório financeiro | le rapport financier | O relatório financeiro foi melhor do que o esperado. | Le rapport financier a été meilleur que prévu. | pl=relatórios financeiros
a reprodução | la restitution, reproduction | A reprodução das cores é surpreendentemente fiel. | La restitution des couleurs est étonnamment fidèle. | g? | pl=reproduções
a resenha | la critique (compte rendu) | Ele resenha dois romances por mês. | Il chronique deux romans par mois. | g?
a reunião da diretoria | la réunion du comité | A reunião da diretoria foi até a meia-noite. | La réunion du comité a duré jusqu'à minuit. | g? | pl=reuniões da diretoria
a reverberação | la réverbération | A reverberação da igreja não perdoa bilhetes rápidas. | La réverbération de l'église ne pardonne pas les passages rapides. | g? | pl=reverberações
a rubrica | la didascalie | As rubricas são mais longas do que os diálogos. | Les didascalies sont plus longues que les dialogues.
a sede do clube | le local du club | A sede do clube é mantida por voluntários. | Le local du club est tenu par des bénévoles. | g? | pl=sedes do clube
o timbre | le timbre | O timbre do instrumento muda tudo. | Le timbre de l'instrument change tout.
a tonalidade | la tonalité | A peça está num tom sombrio. | Le morceau est dans une tonalité sombre. | ex?
o trabalho de base | la formation des jeunes |  |  | pl=trabalhos de base | ex=?
a usabilidade | la facilité d'utilisation | É na usabilidade que a maioria das boas ideias fracassa. | C'est sur la facilité d'utilisation qu'échouent la plupart des bonnes idées.
a utilidade pública | l'utilité publique | Sem o status de utilidade pública não haveria benefícios fiscais. | Sans reconnaissance d'utilité publique, pas d'avantage fiscal. | pl=utilidades públicas
""",
"desporto_c1_pt": """
o acréscimos | le temps additionnel | O empate saiu acréscimo-nos. | L'égalisation est tombée dans le temps additionnel. | g? | pl=acréscimos | ex?
o andamento do jogo | le déroulement du match | O andamento do jogo diz mais do que o marcador. | Le déroulement du match en dit plus que le score. | pl=andamentos do jogo
o armador | le meneur de jeu |  |  | ex=?
o chance de golo | l'occasion de but | De quinze chances de golo saiu um único golo. | De quinze occasions est né un seul but. | g? | pl=chances de golo
a decisão da arbitragem | la décision arbitrale | Ainda se vai falar da decisão do juiz por anos. | On parlera encore des années de la décision arbitrale. | pl=decisões da arbitragem | ex?
a escalação | la composition d'équipe | A escalação foi mudada uma hora antes do apito inicial. | La composition a été modifiée une heure avant le coup d'envoi. | g? | pl=escalações
a jogada | l'action de jeu, combinaison | A jogada foi ensaiada, não espontânea. | L'action était répétée, pas spontanée. | g?
o jogo limpo | le fair-play | Não foi um jogo limpo. | Ce n'était pas un jeu correct. | pl=jogos limpos
a linha de defesa | la ligne défensive | A linha de defesa estava adiantada demais. | La ligne défensive était trop haute. | g? | pl=linhas de defesa
a posição na tabela | la place au classement |  |  | g? | pl=posições nas tabelas | ex=?
a pré-temporada | le stage de préparation | A pré-temporada é em janeiro, na Espanha. | Le stage a lieu en janvier en Espagne. | g? | pl=prés-temporadas
o rebaixamento | la relégation | O rebaixamento já estava definido em março. | La relégation était acquise dès mars.
a substituição | le remplacement | A substituição veio vinte minutos atrasada. | Le remplacement est venu vingt minutes trop tard. | g? | pl=substituições
""",
"media_c1_pt": """
a alusão | l'allusion (souvent moqueuse) | A indireta ao antecessor dele foi impossível de não notar. | L'allusion à son prédécesseur était impossible à manquer. | g? | pl=alusões | ex?
a apuração | l'enquête journalistique | A apuração levou mais tempo do que a publicação permitia. | L'enquête a duré plus longtemps que la publication ne le permettait. | g? | pl=apurações
o arquivo de log | le fichier journal | No arquivo de log está quem mudou o quê e quando. | Le fichier journal indique qui a changé quoi et quand. | pl=arquivos de log
a aula particular | le cours particuliers, soutien scolaire | Sem aula de reforço ele não teria passado de ano. | Sans soutien scolaire, il n'aurait pas réussi son année. | g? | pl=aulas particulares | ex?
a capacidade de compreensão | la faculté de compréhension | Elogiaram sobretudo a rapidez com que ela entende as coisas. | On a surtout loué sa rapidité de compréhension. | pl=capacidades de compreensão | ex?
a capacidade de memorização | la capacité de mémorisation | A falta de sono reduz bastante a memória. | Le manque de sommeil abaisse nettement la capacité de mémorisation. | pl=capacidades de memorização | ex?
o chavão | le slogan, mot-clé | A palavra virou um chavão vazio. | Le mot est devenu un slogan vide. | pl=chavões
a cobertura | la couverture médiatique | A cobertura foi parcial e sensacionalista. | La couverture médiatique a été partiale et bruyante. | g?
a compatibilidade | la compatibilité | Tudo esbarra na compatibilidade com o sistema antigo. | Tout échoue sur la compatibilité avec l'ancien système.
o conhecimento superficial | le demi-savoir, connaissances superficielles | Saber pela metade é mais perigoso do que admitir que não sabe. | Le demi-savoir est plus dangereux que l'ignorance avouée. | pl=conhecimentos superficiais | ex?
o conhecimento técnico | la compétence technique | Para esta vaga é necessário um conhecimento técnico aprofundado. | Ce poste exige des compétences techniques approfondies. | pl=conhecimentos técnicos
a conta de utilizador | le compte utilisateur | A conta foi bloqueada depois de três tentativas erradas. | Le compte utilisateur a été bloqué après trois tentatives. | g? | pl=contas de utilizador | ex?
a correção | le rectificatif, démenti | A correção é gratuita. | La reprise est gratuite. | pl=correções
a credibilidade | la crédibilité | Um único erro custou a ele a credibilidade. | Une seule erreur lui a coûté sa crédibilité. | g?
a cultura geral | la culture générale | Cultura geral é mais do que saber responder a quiz. | La culture générale est plus qu'un savoir de quiz. | pl=culturas gerais
o direito de acesso | le droit d'accès | Os direitos de acesso nunca foram revistos. | Les droits d'accès n'ont jamais été vérifiés. | pl=direitos de acesso
o erro de raciocínio | l'erreur de raisonnement | O erro de raciocínio já está na primeira frase. | L'erreur de raisonnement est déjà dans la première phrase. | pl=erros de raciocínio
a escolha das palavras | le choix des mots | Neste assunto a escolha das palavras é fundamental. | Sur ce sujet, tout dépend du choix des mots. | g? | pl=escolhas das palavras
o exagero | l'exagération | Sem exagero: foi a melhor noite do ano. | Sans exagération : c'était la meilleure soirée de l'année.
a expressão idiomática | l'expression idiomatique | Esta expressão idiomática não pode ser traduzida ao pé da letra. | Cette expression ne se traduit pas mot à mot. | pl=expressões idiomáticas
o formato de arquivo | le format de fichier | Só dois programas leem este formato de arquivo. | Seuls deux logiciels lisent ce format de fichier. | pl=formatos de arquivo
a formulação | la formulation | Eu atenuaria um pouco a formulação. | J'atténuerais un peu la formulation. | pl=formulações
o frase feita | la formule creuse | O discurso dele era quase só frase feita. | Son discours n'était presque que formules creuses. | g? | pl=frases feitas
a função de filtro | la fonction de filtrage | Sem função de filtro a lista é inútil. | Sans fonction de filtrage, la liste est inutilisable. | pl=funções de filtro
a generalização | la généralisation | É bom evitar generalizações desse tipo. | Il faut se garder de telles généralisations. | pl=generalizações
a gestão de permissões | la gestion des droits | A gestão de permissões fica com o departamento de TI. | La gestion des droits relève du service informatique. | g? | pl=gestões de permissões
a indignação | l'indignation | A indignação durou exatamente três dias. | L'indignation a duré exactement trois jours. | g? | pl=indignações
a interface do utilizador | l'interface utilisateur | A interface não é mexida há oito anos. | L'interface n'a pas été touchée depuis huit ans. | g? | pl=interfaces do utilizador | ex?
a interpretação | l'interprétation (d'un texte) | Esta frase permite várias interpretações. | Cette phrase se prête à plusieurs interprétations. | pl=interpretações
a lacuna de conhecimento | la lacune | A prova revelou lacunas consideráveis. | L'examen a mis au jour des lacunes considérables. | g? | pl=lacunas de conhecimento | ex?
a liberdade de imprensa | la liberté de la presse | A liberdade de imprensa está na Constituição. | La liberté de la presse figure dans la constitution. | g? | pl=liberdades de imprensa
o login | la connexion, inscription | O login só funciona com o segundo fator. | La connexion ne fonctionne qu'avec un second facteur.
a mensagem de erro | le message d'erreur | A mensagem de erro não diz nada de útil. | Le message d'erreur ne dit rien d'utile. | g? | pl=mensagens de erro
a naturalidade | la désinvolture, ton anodin | Ele mencionou a demissão com uma naturalidade fingida. | Il a mentionné le licenciement avec une désinvolture feinte.
o opinião pública | l'opinion publique, sphère publique | O relatório nunca foi apresentado ao público. | Le rapport n'a jamais été présenté au public. | pl=opiniões públicas | ex?
o progresso no aprendizado | le progrès d'apprentissage | O progresso no aprendizado é difícil de traduzir em notas. | Le progrès d'apprentissage se laisse difficilement traduire en notes. | pl=progressos nos aprendizados
o regulamento de provas | le règlement des examens | O regulamento só permite refazer a prova duas vezes. | Le règlement des examens ne prévoit que deux redoublements. | pl=regulamentos de provas | ex?
o relatório de análise | le rapport d'analyse | O relatório de análise chega todas as segundas. | Le rapport d'analyse arrive chaque lundi. | pl=relatórios de análise
a tagarelice | la loquacité | A tagarelice dele cansou todo mundo na mesa. | Sa loquacité a fatigué toute la tablée. | g?
a taxa de transferência | le débit de transmission | A taxa de transferência despenca à noite. | Le débit s'effondre le soir. | g? | pl=taxas de transferência
o termo técnico | le terme technique | O texto está cheio de termos técnicos que ninguém explica. | Le texte est plein de termes techniques que personne n'explique. | pl=termos técnicos
o texto literal | la teneur exacte, texte littéral | No texto literal não há nada sobre isso. | Rien de tel ne figure dans le texte exact. | pl=textos literais
o tom de voz | le ton, intonation | Não foi o conteúdo que me incomodou, mas o tom. | Ce n'est pas le contenu qui m'a gêné, mais le ton. | pl=tons de voz | ex?
a trajetória escolar | le parcours scolaire | A origem social marca a trajetória escolar mais do que o talento. | L'origine sociale marque le parcours scolaire plus que le talent. | g? | pl=trajetórias escolares
a área de estudo | la spécialité, filière | Depois de dois semestres ela mudou de curso. | Elle a changé de filière après deux semestres. | g? | pl=áreas de estudo | ex?
a área de transferência | le presse-papiers | O texto ainda está na área de transferência. | Le texte est encore dans le presse-papiers. | pl=áreas de transferência
""",
"dinheiro_c1_pt": """
a adjudicação | l'attribution (d'un marché) | A adjudicação do contrato está a ser analisada. | L'attribution du marché est actuellement examinée. | g? | pl=adjudicações
a alíquota de contribuição | le taux de cotisation | A alíquota de contribuição sobe na virada do ano. | Le taux de cotisation augmente au changement d'année. | g? | pl=alíquotas de contribuição
a amortização | le amortissement (d'une dette) | A amortização só começa no segundo ano. | L'amortissement ne commence qu'à la deuxième année. | g? | pl=amortizações
o apego às marcas | la conscience de marque | O apego às marcas começa no jardim de infância. | La conscience de marque commence à la maternelle. | pl=apegos àss marcas
a aquisição | le rachat, reprise | A compra do concorrente foi aprovada. | Le rachat du concurrent a été autorisé. | pl=aquisições | ex?
o atraso no pagamento | le retard de paiement | Em caso de atraso no pagamento, há taxas de cobrança. | En cas de retard de paiement, des frais de rappel s'appliquent. | pl=atrasos nos pagamentos
o aviso de sinistro | la déclaration de sinistre | O aviso de sinistro precisa de chegar em uma semana. | La déclaration de sinistre doit parvenir sous une semaine. | pl=avisos de sinistro
a capacidade de crédito | la solvabilité | O banco verifica primeiro a capacidade de crédito. | La banque vérifie d'abord la solvabilité. | g? | pl=capacidades de crédito
a característica | la caractéristique, trait distinctif | A principal característica deste tipo de construção é a leveza. | La caractéristique principale de cette construction est sa légèreté. | g?
o cheque especial | le découvert | Entrar no cheque especial sai caro. | Le découvert du compte coûte cher. | pl=cheques especiais
a cobertura do seguro | la couverture d'assurance | A cobertura do seguro só começa no dia seguinte. | La couverture d'assurance ne commence que le lendemain. | g? | pl=coberturas do seguro
o componente | la composante, élément constitutif | Um único componente trava toda a produção. | Une seule pièce bloque toute la fabrication. | g?
o comportamento de compra | le comportement d'achat | O comportamento de compra mudou desde a crise. | Le comportement d'achat a changé depuis la crise. | pl=comportamentos de compra
a conjuntura económica | la conjoncture | Recentemente a economia esfriou de forma perceptível. | La conjoncture s'est nettement refroidie ces derniers temps. | pl=conjunturas económicas | ex?
a defesa do consumidor | la protection du consommateur | A defesa do consumidor só entra em ação depois da compra. | La protection du consommateur n'intervient qu'après l'achat. | g? | pl=defesas do consumidor
a depreciação | l'amortissement | A máquina é depreciada ao longo de dez anos. | La machine s'amortit sur dix ans. | pl=depreciações | ex?
o depósito retornável | la consigne ; gage | Cada garrafa tem um depósito de 25 centavos. | Chaque bouteille porte une consigne de 25 centimes. | pl=depósitos retornáveis | ex?
a desvalorização | la perte de valeur | A desvalorização é maior no primeiro ano. | La perte de valeur est la plus forte la première année. | g? | pl=desvalorizações
o direito de rescisão | le droit de résiliation | Depois de um aumento do prémio há direito de rescisão. | Après une hausse de cotisation, il existe un droit de résiliation. | pl=direitos de rescisão
a disputa entre peritos | le litige d'expertise | No final houve uma disputa entre peritos no tribunal. | Au bout du compte, un litige d'expertise est passé devant le tribunal. | pl=disputas entres peritos
a diversificação | la diversification, dispersion | Uma diversificação ampla reduz o risco. | Une large diversification abaisse le risque. | pl=diversificações
a durabilidade | la durée de conservation | O produto não estraga necessariamente quando passa a data. | La conservation ne s'arrête pas à la date. | ex?
o débito devolvido | le rejet de prélèvement | Cada débito devolvido gera tarifas extras. | Chaque rejet de prélèvement entraîne des frais supplémentaires. | pl=débitos devolvidos
o efeito da publicidade | l'impact publicitaire | O efeito da publicidade é difícil de medir. | L'impact publicitaire se mesure difficilement. | pl=efeitos da publicidade
o encargo | le prélèvement, taxe | Sobre o salário ainda incidem os encargos. | Au salaire s'ajoutent encore les prélèvements.
o endividamento | l'endettement | O endividamento dos municípios cresce há anos. | L'endettement des communes croît depuis des années.
a faixa de isenção | l'abattement fiscal | Até o limite de isenção tudo fica livre de imposto. | Jusqu'à l'abattement, tout reste exonéré. | g? | pl=faixas de isenção | ex?
a fiança | la caution, garantie | Sem a fiança dos pais ela não conseguiu o apartamento. | Sans la caution de ses parents, elle n'a pas obtenu l'appartement. | g?
a fidelização de clientes | la fidélisation de la clientèle | Fidelizar clientes custa menos do que conquistar novos. | Fidéliser coûte moins cher que conquérir. | pl=fidelizações de clientes | ex?
a formação de reservas | la constitution de réserves | Sem formar reservas nenhum clube sobrevive a uma fase ruim. | Sans constitution de réserves, aucune association ne survit à un creux. | pl=formações de reservas | ex?
a garantia legal | la garantie légale | A garantia legal vale dois anos. | La garantie légale vaut deux ans. | g? | pl=garantias legais
o gargalo | le goulot d'étranglement, pénurie | Há um verdadeiro gargalo de mão de obra qualificada. | Il y a une véritable pénurie de main-d'œuvre qualifiée. | g?
a geração de valor | la création de valeur | Grande parte do valor gerado fica na região. | Une grande partie de la création de valeur reste dans la région. | pl=gerações de valor | ex?
a implementação | la mise en œuvre | Entre a decisão e a implementação passaram-se dois anos. | Deux ans se sont écoulés entre la décision et la mise en œuvre. | g? | pl=implementações
a indicação de origem | l'indication d'origine | A indicação de origem está em letras miúdas atrás. | L'indication d'origine est écrite petit au dos. | g? | pl=indicações de origem
a invalidez profissional | l'invalidité professionnelle | Quase ninguém se protege a tempo contra a invalidez profissional. | Presque personne ne s'assure à temps contre l'invalidité professionnelle. | g? | pl=invalidezes profissionais
a licitação | l'appel d'offres | A licitação não teve transparência. | L'attribution était opaque. | pl=licitações
os lixo de embalagens | les déchets d'emballage | O lixo das embalagens pesa mais do que o conteúdo. | Les déchets d'emballage pèsent plus que le contenu. | ex?
a notificação | la décision administrative, notification | A notificação chegou pelo correio, três semanas depois. | La décision est arrivée par la poste, trois semaines plus tard. | g? | pl=notificações
a origem regional | la caractère régional | A origem regional virou argumento de venda. | Le caractère régional est devenu un argument de vente. | g? | pl=origens regionais
""",
"dinheiro_c1_pt_2": """
o pagamento do prémio | le paiement des cotisations | Sem o pagamento do prémio a cobertura fica suspensa. | En cas de défaut de paiement, la couverture est suspendue. | pl=pagamentos do prémio
o poder de compra | le pouvoir d'achat | O poder de compra caiu apesar dos salários maiores. | Le pouvoir d'achat a baissé malgré des salaires plus élevés. | pl=poderes de compra
a política de preços | la politique de prix | A política de preços é quase incompreensível para os clientes. | La politique de prix est difficilement compréhensible pour les clients. | g? | pl=políticas de preços
a previdência | la prévoyance vieillesse | Como autónomo, ele mesmo paga a previdência. | Comme profession libérale, il cotise lui-même. | g?
o procedimento | la manière de procéder | Todos concordaram com o procedimento. | Tous étaient d'accord sur la manière de procéder.
o produto de massa | le produit de masse | Entre o produto de massa e o artesanal está o preço. | Entre produit de masse et artisanat, il y a le prix. | pl=produtos de massa
o produto descartável | le produit jetable | Uma ferramenta virou produto descartável. | D'un outil on a fait un produit jetable. | pl=produtos descartáveis
a realização | la exécution, réalisation | A realização do estudo levou seis meses. | La réalisation de l'étude a duré six mois. | g? | pl=realizações
a regulação | le règlement (d'un sinistre) | A regulação do sinistro levou oito meses. | Le règlement du sinistre a traîné huit mois. | g? | pl=regulações
o rendimento | le rendement | O cansaço diminuiu o rendimento dele. | La fatigue a diminué son rendement.
o segurado | le preneur d'assurance | O segurado responde por informações falsas. | Le preneur d'assurance répond des fausses déclarations.
o seguro contra acidentes | l'assurance accidents | O seguro contra acidentes também vale no trajeto para o trabalho. | L'assurance accidents vaut aussi sur le trajet du travail. | pl=seguros contras acidentes
o seguro de proteção jurídica | la protection juridique | O seguro jurídico só vale depois de três meses. | La protection juridique ne joue qu'après trois mois. | pl=seguros de proteção jurídica | ex?
o seguro de responsabilidade civil | la responsabilité civile |  |  | pl=seguros de responsabilidade civil | ex=?
o selo de qualidade | le label de qualité | O selo de qualidade diz menos do que se pensa. | Le label de qualité dit moins qu'on ne croit. | pl=selos de qualidade
o sinistro coberto | le cas de prise en charge | Em caso de sinistro, a seguradora paga em trinta dias. | En cas de prise en charge, la caisse paie sous trente jours. | pl=sinistros cobertos | ex?
a sobretaxa de risco | la surprime | Por causa da doença preexistente houve uma sobretaxa de risco. | En raison de l'antécédent, il y a eu une surprime. | pl=sobretaxas de risco
o subsídio | la subvention, aide financière | Houve um subsídio do governo para a reforma. | Une subvention publique a été accordée pour les travaux.
a taxa de juros | le taux d'intérêt | A taxa de juros está atrelada à taxa básica. | Le taux d'intérêt est indexé sur le taux directeur. | pl=taxas de juros
o valor de cobertura | le plafond de garantie | O valor de cobertura é de cinco milhões. | Le plafond de garantie est de cinq millions. | pl=valores de cobertura
a área de competência | le domaine de compétence | Isso não é da minha área de competência. | Cela ne relève pas de mon domaine de compétence. | pl=áreas de competência
""",
"sentimentos_c1_pt": """
o adiamento | le sursis, report | O assunto não admite adiamento. | L'affaire ne souffre aucun report.
a análise | l'examen, considération | A análise dos dados levou mais tempo do que o levantamento. | L'analyse des données a pris plus de temps que la collecte. | g?
o ar pensativo | la gravité pensive | O filme deixou um silencioso ar de reflexão. | Le film a laissé une discrète gravité pensive. | g? | pl=ares pensativos | ex?
a atenção plena | la attention, pleine conscience | Dez minutos de atenção plena bastam para começar. | Dix minutes d'exercice de pleine conscience suffisent pour commencer. | g? | pl=atenções plenas
o autocontrole | la maîtrise de soi | Custou a ele um bom autocontrole ficar calmo. | Il lui a fallu une certaine maîtrise de soi pour rester calme. | g?
a avaliação | l'appréciation, estimation | Na minha avaliação, isso ainda vai levar meses. | D'après mon appréciation, cela prendra encore des mois. | pl=avaliações
a cegueira | l'aveuglement | Só mais tarde ele percebeu a própria cegueira. | Ce n'est que plus tard qu'il a reconnu son propre aveuglement.
a constância | la constance, durabilité | Constância é mais rara do que talento. | La constance est plus rare que le don. | g?
o design | la conception, mise en forme | O design da capa decidiu as vendas. | La conception de la couverture a décidé des ventes.
a distração | la distraction, étourderie | A distração dele é famosa entre os colegas. | Sa distraction est proverbiale chez ses collègues. | g? | pl=distrações
o estímulo à reflexão | l'élément de réflexion | A palestra dela deu-me vários pontos para refletir. | Sa conférence m'a donné plusieurs éléments de réflexion. | pl=estímulos às reflexões | ex?
o excesso de confiança | la témérité, exubérance | Na euforia, ele recusou a oferta. | Par excès de confiance, il a refusé l'offre. | pl=excessos de confiança | ex?
a expectativa | l'attitude d'attente | A expectativa do público era enorme. | L'attente du public était énorme. | g?
a expressividade | la force expressive | O texto ganha expressividade quando é cortado. | Le texte gagne en force expressive quand on le raccourcit.
a força de vontade | la force de volonté | Para isso é preciso mais força de vontade do que talento. | Cela demande plus de volonté que de talent. | g? | pl=forças de vontade
a ilusão | le vœu pieux, pensée illusoire | Esta previsão é pura ilusão. | Cette prévision est un pur vœu pieux. | g? | pl=ilusões
a imprudência | l'légèreté, imprudence | Isso foi pura imprudência, não azar. | C'était de la pure imprudence, pas de la malchance. | g?
a indulgência | l'indulgence | Ele pediu compreensão pela ligação tardia. | Il a demandé de l'indulgence pour son appel tardif. | g? | ex?
a linha de raciocínio | le cheminement de pensée | Não consegui acompanhar totalmente o raciocínio dele. | Je n'ai pas tout à fait pu suivre son cheminement de pensée. | g? | pl=linhas de raciocínio | ex?
o modo de pensar | le mode de pensée | O modo de pensar dela é bem diferente do meu. | Son mode de pensée diffère beaucoup du mien. | pl=modos de pensar
a parcialidade | le parti pris |  |  | g? | ex=?
a persistência | la persévérance, ténacité | Com persistência ela finalmente alcançou o seu objetivo. | À force de persévérance, elle a fini par atteindre son but. | g?
a presunção | la présomption, arrogance | Seria presunção julgar isso. | Ce serait de la présomption que d'en juger. | pl=presunções
o recalque | le refoulement | Negar o problema só ajuda por pouco tempo. | Le refoulement n'aide que peu de temps. | g? | ex?
a sequência | la succession, enchaînement | A sequência dos acontecimentos continua obscura até hoje. | L'enchaînement des événements reste flou à ce jour. | g?
a simultaneidade | la simultanéité | A simultaneidade das duas crises dificultou tudo. | La simultanéité des deux crises a tout compliqué. | g?
a sinceridade | la sincérité | A sinceridade dela era incómoda, mas valiosa. | Sa sincérité était gênante, mais précieuse. | g?
a teimosia | l'entêtement, caractère buté | A teimosia dele muitas vezes o salvou e muitas vezes o prejudicou. | Son entêtement l'a souvent sauvé et souvent desservi. | g?
a transitoriedade | le caractère éphémère | O quadro fala da transitoriedade de todas as coisas. | Le tableau parle du caractère éphémère de toute chose.
o traço de caráter | le trait de caractère | A generosidade era o traço mais marcante dele. | La générosité était son trait de caractère le plus frappant. | pl=traços de caráter | ex?
a vigilância | la vigilance | A profissão exige vigilância constante. | Le métier exige une vigilance constante. | g?
""",
"sociedade_c1_pt": """
a alternância de poder | l'alternance | A alternância de poder foi surpreendentemente tranquila. | L'alternance s'est déroulée étonnamment calmement. | g? | pl=alternâncias de poder
a camada | la couche sociale | Hoje há uma camada densa de poluição sobre a cidade. | Un épais smog recouvre la ville aujourd'hui. | g?
o comparecimento às urnas | le taux de participation | O comparecimento ficou abaixo de cinquenta por cento. | Le taux de participation était sous les cinquante pour cent. | pl=comparecimentos àss urnas | ex?
a correlação de forças | le rapport de majorité | A correlação de forças mudou em duas cadeiras. | Le rapport de majorité s'est déplacé de deux sièges. | g? | pl=correlações de forças
a cédula de votação | le bulletin de vote | Na cédula havia onze nomes. | Onze noms figuraient sur le bulletin de vote. | pl=cédulas de votação | ex?
o debate do orçamento | le débat budgétaire | O debate do orçamento arrastou-se por três dias. | Le débat budgétaire s'est étiré sur trois jours. | pl=debates do orçamento
o envelhecimento | le vieillissement (de la population) | O envelhecimento da população pesa sobre a previdência. | Le vieillissement pèse sur les caisses de retraite.
a grupo marginalizado | le groupe marginalisé |  |  | g? | pl=grupos marginalizados | ex=?
o lobby | le lobbying | O lobby é permitido, mas raramente visível. | Le lobbying est permis, mais rarement visible.
a oportunidade de ascensão | la chance de promotion sociale | Sem diploma as chances de ascensão são pequenas. | Sans diplôme, les chances de promotion sont faibles. | pl=oportunidades de ascensão | ex?
o pertencimento | l'appartenance | O sentimento de pertencimento surge aos poucos. | Le sentiment d'appartenance naît lentement.
a pretensão ao poder | la prétention au pouvoir | A pretensão dele ao poder nunca foi escondida. | Sa prétention au pouvoir n'a jamais été dissimulée. | g? | pl=pretensões aos poderes | ex?
o princípio norteador | le modèle directeur, idéal affiché | O ideal da escola está em todas as paredes, mas raramente é vivido. | L'idéal affiché de l'école est sur chaque mur, rarement vécu. | pl=princípios norteadores | ex?
o projeto de lei | le projet de loi | O projeto de lei foi debatido em primeira leitura. | Le projet de loi a été débattu en première lecture. | pl=projetos de lei
a prosperidade | la prospérité | A prosperidade é distribuída de forma muito desigual. | La prospérité est très inégalement répartie. | g?
a renúncia | la démission | A renúncia veio na mesma noite. | La démission est arrivée le soir même. | g?
a ruptura | le bouleversement | A ruptura de ligamento aconteceu na aterrissagem. | La rupture ligamentaire s'est produite à la réception.
o tabu | le tabou | Aqui falar de salário ainda é tabu. | Parler des salaires reste ici un tabou. | g?
a transformação | la mutation, transformation | O mundo do trabalho está a passar por uma transformação profunda. | Le monde du travail connaît une mutation profonde. | pl=transformações
a tutela excessiva | la mise sous tutelle, paternalisme | Muita gente sentiu a norma como puro paternalismo. | Beaucoup ont ressenti cette règle comme du pur paternalisme. | g? | pl=tutelas excessivas | ex?
o voto de confiança | la question de confiance | Ele pediu um voto de confiança e perdeu. | Il a posé la question de confiance et l'a perdue. | pl=votos de confiança
o êxodo | l'exode, départ (d'une région) | O êxodo dos jovens esvazia vilarejos inteiros. | L'exode des jeunes vide des villages entiers.
""",
"lei_c1_pt": """
o agente de liberdade condicional | l'agent de probation | O agente de liberdade condicional faz contacto todos os meses. | L'agent de probation prend contact chaque mois. | pl=agentes de liberdade condicional
a ajuda para a reconstrução | l'aide à la reconstruction | A ajuda para a reconstrução chegou tarde e em parcelas. | L'aide à la reconstruction est venue tard et par tranches. | g? | pl=ajudas paras as reconstruções
a ameaça | la menace | A ameaça foi subestimada por muito tempo. | La menace a longtemps été sous-estimée. | g?
a apelação | l'appel (recours) | Foi interposta apelação contra a sentença. | Un appel a été interjeté contre le jugement. | pl=apelações
a apreensão | la saisie | Depois da apreensão o computador ficou três meses fora. | Après la saisie, l'ordinateur est resté absent trois mois. | pl=apreensões
a busca | la perquisition | A busca durou seis horas. | La perquisition a duré six heures. | g?
o cessar-fogo | le cessez-le-feu | O cessar-fogo não durou nem três dias. | Le cessez-le-feu n'a pas tenu trois jours. | pl=cessares-fogos
o comando da operação | le commandement des opérations | O comando da operação decidiu esperar. | Le commandement a décidé d'attendre. | pl=comandos da operação
a defesa civil | la protection civile | A defesa civil foi reorganizada depois da enchente. | La protection civile a été réorganisée après l'inondation. | g? | pl=defesas civis
o depoimento de testemunha | le témoignage | O depoimento da testemunha contradizia os autos. | Le témoignage contredisait le dossier. | pl=depoimentos de testemunha | ex?
o desarmamento | le désarmement | Fala-se de desarmamento desde que existem armas. | On parle de désarmement depuis qu'il existe des armes.
a detenção | l'arrestation | A prisão foi feita de madrugada. | L'arrestation a eu lieu au petit matin. | pl=detenções | ex?
a dissuasão | la dissuasion | A dissuasão só funciona enquanto se acredita nela. | La dissuasion ne fonctionne que tant qu'on y croit. | g? | pl=dissuasões
a equipas de resgate | les forces d'intervention | As equipas de resgate chegaram em doze minutos. | Les forces d'intervention étaient sur place en douze minutes. | pl=equipas de resgate
o espólio | la succession, héritage | O espólio foi dividido entre três herdeiros. | La succession a été partagée entre trois héritiers.
o estado de alerta | l'état d'alerte | Os bombeiros ficaram em alerta a noite toda. | Les pompiers sont restés en état d'alerte toute la nuit. | pl=estados de alerta | ex?
a evacuação | l'évacuation | A evacuação do prédio levou quarenta minutos. | L'évacuation du bâtiment a duré quarante minutes. | g? | pl=evacuações
a falha de segurança | la faille de sécurité | A falha de segurança era conhecida havia dois anos. | La faille de sécurité était connue depuis deux ans. | g? | pl=falhas de segurança
o foco de crise | le foyer de crise | A região é considerada um foco de crise há anos. | La région passe depuis des années pour un foyer de crise. | pl=focos de crise
a identificação | le contrôle d'identité | Ficou só numa identificação. | Cela s'est arrêté à un contrôle d'identité. | pl=identificações
a indenização | l'indemnisation, dédommagement | Os afetados receberam uma indenização financeira. | Les personnes concernées ont reçu une indemnisation financière. | pl=indenizações
a infração administrativa | la contravention | Estacionar em local proibido é infração administrativa, não crime. | Le stationnement interdit est une contravention, pas un délit. | pl=infrações administrativas
o interrogatório | l'audition, interrogatoire | O interrogatório foi gravado. | L'audition a été enregistrée.
a investigação | l'enquête (judiciaire) | As investigações ainda estão em andamento. | L'enquête est toujours en cours. | pl=investigações
a jurisprudência | la jurisprudence | Aqui a jurisprudência mudou bastante. | La jurisprudence a nettement évolué sur ce point. | g?
o laudo | l'expertise, rapport d'expert | O tribunal pediu um laudo independente. | Le tribunal a fait établir une expertise indépendante.
a liberdade condicional | le sursis (avec mise à l'épreuve) | A pena foi suspensa condicionalmente. | La peine a été assortie du sursis. | pl=liberdades condicionais | ex?
o local do crime | le lieu du crime | O local do crime ficou isolado por horas. | Le lieu du crime a été bouclé des heures. | pl=locais do crime
a medida preventiva | la mesure de précaution | As medidas preventivas custaram menos do que um único prejuízo. | Les mesures de précaution ont coûté moins qu'un seul sinistre. | pl=medidas preventivas
a obrigatoriedade de consentimento | l'obligation d'accord préalable | Para este passo é obrigatório o consentimento da comissão de funcionários. | Cette démarche exige l'accord préalable du comité d'entreprise. | pl=obrigatoriedades de consentimento | ex?
a obrigação | l'obligation, engagement | Do contrato resultam obrigações claras. | Le contrat entraîne des obligations claires. | pl=obrigações
a parte do conflito | la partie au conflit | As duas partes do conflito reivindicam o mesmo vale. | Les deux parties au conflit revendiquent la même vallée. | g? | pl=partes do conflito
a perícia | la police scientifique, relevé d'indices | A perícia trabalhou até de madrugada. | La police scientifique a travaillé jusque tard dans la nuit. | g?
a população civil | la population civile | A população civil carrega o maior peso. | La population civile porte le fardeau principal. | g? | pl=populações civis
a prescrição | la prescription | A prescrição ocorre depois de três anos. | La prescription intervient après trois ans. | g? | pl=prescrições
a procuração | la procuration | Sem procuração por escrito ela não pode assinar nada. | Sans procuration écrite, elle n'a pas le droit de signer. | pl=procurações
a proteção a testemunhas | la protection des témoins | Sem proteção a testemunhas ninguém teria deposto. | Sans protection des témoins, personne n'aurait témoigné. | pl=proteções as testemunhas
o queixa-crime | la plainte pénale | Ela registrou boletim de ocorrência contra desconhecidos. | Elle a déposé une plainte contre X. | g? | pl=queixas-crimes | ex?
o rearmamento | le réarmement | O rearmamento começou anos antes do conflito. | Le réarmement a commencé des années avant le conflit.
o regulamento | le règlement, arrêté | O novo regulamento entra em vigor em janeiro. | Le nouveau règlement entre en vigueur en janvier.
a rescisão | la dissolution, résiliation | A rescisão do contrato foi feita de comum acordo. | La résiliation du contrat s'est faite d'un commun accord. | g? | pl=rescisões
a revogação | la rétractation, révocation | A desistência precisa de ser feita por escrito. | La rétractation doit se faire par écrit. | pl=revogações | ex?
o tratado de paz | le traité de paix | Nunca se assinou um tratado de paz. | Aucun traité de paix n'a jamais été signé. | pl=tratados de paz
a viatura | la voiture de patrouille | Uma viatura ficou a noite toda em frente da casa. | Une voiture de patrouille est restée toute la nuit devant la maison.
o ónus da prova | la charge de la preuve | O ónus da prova cabe ao autor da ação. | La charge de la preuve incombe au demandeur. | g? | pl=ónus da prova
""",
"ideias_c1_pt": """
a aceleração | l'accélération | Acelerar o processo era urgente. | L'accélération de la procédure était urgente. | pl=acelerações | ex?
a acusação | le reproche, accusation | Ele rejeitou a acusação com firmeza. | Il a rejeté l'accusation avec fermeté. | g? | pl=acusações
a afirmação | l'affirmation | A afirmação dele não pôde ser confirmada por nenhuma fonte. | Son affirmation n'a pu être étayée par aucune source. | g? | pl=afirmações
o agravamento | l'exacerbation | O agravamento da situação era previsível. | L'exacerbation de la situation était prévisible.
o altruísmo | le désintéressement | A abnegação dela chegava ao esgotamento. | Son désintéressement allait jusqu'à l'épuisement. | ex?
o amor ao próximo | l'amour du prochain | O amor ao próximo é mais incómodo do que parece. | L'amour du prochain est plus inconfortable qu'il n'y paraît. | pl=amores aos próximos
a aprovação | l'approbation, accord | O pedido teve ampla aprovação na comissão. | La demande a reçu une large approbation en commission. | pl=aprovações
a arbitrariedade | l'arbitraire | Sem regras fixas reina a arbitrariedade. | Sans règles fermes règne l'arbitraire. | g?
o arrependimento | le remords, repentir | Na carta dele não havia sinal de arrependimento. | Sa lettre ne laissait lire aucun remords.
a assistência espiritual | l'accompagnement spirituel | No hospital há assistência espiritual 24 horas. | À l'hôpital, l'accompagnement spirituel est assuré jour et nuit. | g? | pl=assistências espirituais
o atrito | la friction, frottement | Entre os departamentos há atritos constantes. | Il y a des frictions constantes entre les services.
a ausência de reservas | l'absence de réserve | Ele ajudou com uma entrega total que surpreendeu a todos. | Il a aidé avec une absence de réserve qui a surpris tout le monde. | g? | pl=ausências de reservas | ex?
a busca de sentido | la quête de sens | A busca de sentido muitas vezes começa depois de uma perda. | La quête de sens commence souvent après une perte. | g? | pl=buscas de sentido
a bênção | la bénédiction | No final houve a bênção para todos. | À la fin, il y a eu la bénédiction pour tous. | g? | pl=bênçãos
o ceder | le fait de céder | Ceder aqui não é fraqueza, mas estratégia. | Céder n'est pas ici une faiblesse, mais une stratégie. | g?
a circunstância | la donnée, circonstance | Uma infeliz série de circunstâncias causou o acidente. | Un malheureux enchaînement de circonstances a mené à l'accident. | g?
o clero | le clergé | O clero ficou fora do debate. | Le clergé s'est tenu à l'écart du débat.
o complexo do mosteiro | l'ensemble monastique | O mosteiro está vazio desde 1803. | L'ensemble monastique est vide depuis 1803. | pl=complexos do mosteiro | ex?
o comprovante | la pièce justificative, preuve | Eu guardo os comprovantes. | Je conserve les reçus. | g?
a comunidade religiosa | la communauté religieuse | A comunidade religiosa aqui há quarenta membros. | La communauté religieuse compte ici quarante membres. | g? | pl=comunidades religiosas
a conciliação | la conciliation, arbitrage | A disputa terminou numa conciliação. | Le litige s'est terminé par une conciliation. | pl=conciliações
a conjugação | l'interaction, jeu combiné | O sucesso deve-se à conjugação de muitos fatores. | Le succès repose sur l'interaction de nombreux facteurs. | pl=conjugações
a constatação | le constat, connaissance acquise | Esta constatação chegou tarde demais para muitos. | Ce constat est arrivé trop tard pour beaucoup. | pl=constatações
a convicção | la conviction | Ela defende a sua convicção com calma e sem levantar a voz. | Elle défend sa conviction calmement et sans hausser le ton. | pl=convicções
o costume dos feriados | la coutume de fête | Cada região tem os seus próprios costumes de feriado. | Chaque région a ses propres coutumes de fête. | g? | pl=costumes dos feriados | ex?
a crónica | la chronique | A crónica do vilarejo remonta a 1400. | La chronique du village remonte à 1400. | g?
o desequilíbrio de poder | le rapport de force inégal | Entre contratante e fornecedor há um claro desequilíbrio de poder. | Entre donneur d'ordre et fournisseur, le rapport de force est inégal. | g? | pl=desequilíbrios de poder
o desnível | l'écart, dénivelé | Há uma disparidade clara entre a cidade e o campo. | Il existe un écart marqué entre la ville et la campagne. | g? | pl=desníveis | ex?
a devoção | la piété | A devoção dela era silenciosa e sem alarde. | Sa piété était discrète et sans ostentation. | g? | pl=devoções
a dignidade humana | la dignité humaine | A dignidade humana está no primeiro artigo. | La dignité humaine figure au premier article. | g? | pl=dignidades humanas
a dimensão | l'ampleur | A dimensão do estrago só ficou clara semanas depois. | L'ampleur des dégâts n'est apparue que des semaines plus tard. | g? | pl=dimensões
a distensão | la détente, apaisement | Depois do encontro houve um alívio perceptível da tensão. | Après la rencontre, une détente sensible s'est installée. | g? | pl=distensões | ex?
o efeito associado | le phénomène concomitant | O barulho é um efeito inevitável da obra. | Le bruit est un phénomène concomitant inévitable du chantier. | pl=efeitos associados | ex?
o efeito colateral | l'effet secondaire | O medicamento quase não tem efeitos colaterais. | Le médicament n'a presque pas d'effets secondaires. | pl=efeitos colaterais
o encadeamento | l'enchaînement | Uma infeliz série de circunstâncias causou o acidente. | Un malheureux enchaînement de circonstances a mené à l'accident. | ex?
o endurecimento | l'aggravation, durcissement | O endurecimento das regras surpreendeu muita gente. | Le durcissement des règles en a surpris beaucoup.
o enfraquecimento | l'atténuation | Já se desenha uma desaceleração do crescimento. | Un ralentissement de la croissance se dessine. | ex?
a era | l'ère, âge | Vivemos na era da distração. | Nous vivons à l'ère de la distraction.
a escalada | l'escalade | Os dois lados queriam evitar uma nova escalada. | Les deux camps voulaient éviter une nouvelle escalade.
a estagnação | la stagnation | Ao crescimento seguiu-se uma longa estagnação. | L'essor a été suivi d'une longue stagnation. | g? | pl=estagnações
""",
"ideias_c1_pt_2": """
o estopim | le déclencheur | O verdadeiro estopim da briga foi uma parvoíce. | Le véritable déclencheur de la dispute était un détail. | g?
a expulsão | l'expulsion, déplacement forcé | A expulsão atingiu milhões de pessoas. | L'expulsion a touché des millions de personnes. | g? | pl=expulsões
o factos | l'état de fait, situation | Os dois factos ocorreram simultaneamente. | Les deux événements se sont produits simultanément. | g? | pl=factos
o fonte de erro | la source d'erreur | A maior fonte de erro era a digitação manual. | La principale source d'erreur était la saisie manuelle. | g? | pl=fontes de erro
a força motriz | la force motrice | A curiosidade era a verdadeira força motriz do trabalho dele. | La curiosité était la véritable force motrice de son travail. | g? | pl=forças motrizes
a herança pesada | le fardeau hérité | As dívidas são uma herança pesada dos anos noventa. | Les dettes sont un fardeau hérité des années quatre-vingt-dix. | pl=heranças pesadas
a hipocrisia | l'hypocrisie | A indignação era pura hipocrisia. | L'indignation n'était que pure hypocrisie. | g?
a igualdade de tratamento | l'égalité de traitement | A lei exige igualdade de tratamento, não igualdade. | La loi exige l'égalité de traitement, pas l'égalité. | pl=igualdades de tratamento
a insinuação | l'insinuation, procès d'intention | Isso é uma insinuação sem nenhuma prova. | C'est une insinuation pour laquelle il n'existe aucune preuve. | pl=insinuações
a insistência | l'obstination, refus de céder | A insistência dele na data dificultou tudo. | Son obstination sur la date a tout compliqué. | g?
o instrumento de pressão | le moyen de pression | A greve era o único instrumento de pressão deles. | La grève était leur seul moyen de pression. | g? | pl=instrumentos de pressão
a interação | l'interaction réciproque | Entre os dois fatores há uma interação estreita. | Il existe une étroite interaction entre les deux facteurs. | pl=interações
a irregularidade | le dysfonctionnement, abus | O relatório revelou irregularidades graves. | Le rapport a mis au jour de graves dysfonctionnements.
a justificativa | la justification | A recusa veio sem justificativa nenhuma. | Le refus est arrivé sans la moindre justification. | g?
o marco | la césure, rupture | O ano de 1989 foi um marco. | L'année 1989 fut une césure.
o meio-termo | le compromis | No fim saiu um meio-termo que não agradou totalmente a ninguém. | Au bout du compte, un compromis dont personne n'était tout à fait satisfait. | pl=meios-termos
o memorial | le mémorial (d'avertissement) | O memorial fica no meio da cidade. | Le mémorial se dresse au centre de la ville.
a misericórdia | la miséricorde | Misericórdia é mais do que pena. | La miséricorde est plus que la pitié. | g?
o momento de oração | l'office, recueillement | O culto dura só vinte minutos. | L'office ne dure que vingt minutes. | pl=momentos de oração | ex?
a ocupação | l'occupation (militaire) | A ocupação terminou oficialmente em 1955. | L'occupation s'est officiellement terminée en 1955. | g? | pl=ocupações
o outro lado da moeda | le revers, envers | O outro lado do sucesso é uma grande pressão por resultados. | Le revers du succès est une forte pression des attentes. | pl=outros lados da moeda | ex?
a peregrinação | le pèlerinage | A romaria percorre oitenta quilómetros. | Le pèlerinage court sur quatre-vingts kilomètres. | pl=peregrinações | ex?
a ponderação | la pesée du pour et du contre | Depois de uma ponderação cuidadosa, decidimos que não. | Après avoir soigneusement pesé le pour et le contre, nous avons renoncé. | pl=ponderações
o ponto de discórdia | le point de désaccord | O verdadeiro ponto de discórdia era o dinheiro, não o tempo. | Le véritable point de désaccord était l'argent, pas le temps. | g? | pl=pontos de discórdia
o ponto de virada | le tournant | Olhando para trás, aquele foi o ponto de virada. | Rétrospectivement, c'était le tournant. | pl=pontos de virada
o posicionamento | la prise de position | O ministério divulgou um posicionamento breve. | Le ministère a publié une brève prise de position.
o pretexto | le prétexte | O atraso era só um pretexto. | Le retard n'était qu'un prétexte.
a provocação | la provocation | O comentário foi uma provocação deliberada. | La remarque était une provocation délibérée. | pl=provocações
a pós-guerra | l'après-guerre | No pós-guerra faltava tudo, menos trabalho. | Dans l'après-guerre, tout manquait sauf le travail. | g? | pl=poses-guerras
a razoabilidade | le caractère raisonnablement exigible | No fim, quem decide o que é razoável exigir é um tribunal. | C'est un tribunal qui tranche en fin de compte ce qui est exigible. | ex?
a reconstrução | la reconstruction | A reconstrução durou mais do que a guerra. | La reconstruction a duré plus longtemps que la guerre. | g? | pl=reconstruções
a rejeição | le refus, rejet | A rejeição da proposta foi unânime. | Le rejet de la proposition a été unanime. | g? | pl=rejeições
a relativização | la relativisation | As ressalvas constantes dele enfraqueceram o argumento. | Ses relativisations constantes affaiblissaient l'argument. | pl=relativizações | ex?
a ressalva | la réserve | Ele aprovou o plano só com ressalvas. | Il n'a approuvé le plan que sous réserve. | g?
o retidão | la probité | A integridade dele era indiscutível. | Sa probité était incontestée. | pl=retidões | ex?
a retirada | le retrait, repli | Esta declaração foi retirada depois. | Ces propos ont été retirés par la suite. | g?
a retroalimentação | la rétroaction | Entre preços e salários surge um círculo vicioso perigoso. | Une rétroaction dangereuse s'installe entre les prix et les salaires. | pl=retroalimentações | ex?
a reunificação | la réunification | A reunificação transformou os dois lados. | La réunification a changé les deux camps. | g? | pl=reunificações
a reviravolta | le revirement | Depois do discurso houve uma reviravolta repentina no clima. | Après le discours, un revirement soudain s'est produit dans l'ambiance.
o senso de dever | le sens du devoir | Por puro senso de dever ele ficou até o fim. | Par pur sens du devoir, il est resté jusqu'au bout. | pl=sensos de dever
o senso de justiça | le sens de la justice | As crianças têm um senso de justiça surpreendentemente aguçado. | Les enfants ont un sens de la justice étonnamment aiguisé. | pl=sensos de justiça
o senso de responsabilidade | le sens des responsabilités | Esperam dela mais senso de responsabilidade. | On attend d'elle un plus grand sens des responsabilités. | pl=sensos de responsabilidade
o sentimento de culpa | le sentiment de culpabilité | O sentimento de culpa ficou, embora ninguém o acusasse de nada. | Le sentiment de culpabilité est resté, bien que personne ne lui reprochât rien. | pl=sentimentos de culpa
o sermão | le sermon, prêche | O sermão foi mais curto do que de costume. | Le sermon a été plus court que d'habitude. | pl=sermões
a superstição | la superstition | A superstição resiste mais do que o conhecimento. | La superstition tient plus obstinément que le savoir. | g? | pl=superstições
a testemunha da época | le témoin de l'époque | As últimas testemunhas da época têm mais de noventa anos. | Les derniers témoins de l'époque ont plus de quatre-vingt-dix ans. | g? | pl=testemunhas da época
a tolerância | la tolérance | Com atrasos ele não tem tolerância. | Sur les retards, il est sans indulgence. | g?
o trabalho forçado | le travail forcé |  |  | pl=trabalhos forçados | ex=?
o ultimato | l'ultimatum | Ela deu um ultimato: até sexta ou nada. | Elle a posé un ultimatum : vendredi ou jamais.
a viabilidade | la viabilité, solidité | A viabilidade do conceito nunca foi verificada. | La viabilité du concept n'a jamais été vérifiée. | g?
a visão de mundo | la conception du monde |  |  | g? | pl=visões de mundo | ex=?
""",
}
