# -*- coding: utf-8 -*-
"""Les noms du B1 portugais, par theme. SOURCE : c'est ici qu'on corrige, puis
python portugais/outils/construire.py (qui appelle niveaux.py apres l'A1).

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (29 oct. 2026),
converti au portugais d'Europe (variante_niveaux.py), puis relu. Meme format
que noms_a1.py (session socle). BROUILLON : a faire relire par un lusophone du Portugal.

Drapeaux en plus de ceux de l'A1 : « g? » genre devine (a verifier) ; « ex? »
la phrase ne contient pas le mot (a revoir) ; « ex=? » aucune phrase (a ecrire).
"""

NIVEAU = 'B1'

# (id du theme, nom portugais, theme source dont on reprend l'icone)
THEMES = [
    ('familia_b1_pt', 'Família e relações', 'familie_b1'),
    ('trabalho_b1_pt', 'Trabalho e profissões 1', 'arbeit_buero_b1'),
    ('trabalho_b1_pt_2', 'Trabalho e profissões 2', 'arbeit_buero_b1'),
    ('trabalho_b1_pt_3', 'Trabalho e profissões 3', 'arbeit_buero_b1'),
    ('comida_b1_pt', 'Comida e cozinha 1', 'essen_trinken_b1'),
    ('comida_b1_pt_2', 'Comida e cozinha 2', 'essen_trinken_b1'),
    ('casa_b1_pt', 'A casa', 'wohnen_b1'),
    ('saude_b1_pt', 'O corpo e a saúde 1', 'gesundheit_b1'),
    ('saude_b1_pt_2', 'O corpo e a saúde 2', 'gesundheit_b1'),
    ('roupa_b1_pt', 'Roupa e aparência', 'kleidung_b1'),
    ('natureza_b1_pt', 'Natureza e ambiente 1', 'nom_paisaje'),
    ('natureza_b1_pt_2', 'Natureza e ambiente 2', 'nom_paisaje'),
    ('natureza_b1_pt_3', 'Natureza e ambiente 3', 'nom_paisaje'),
    ('viagens_b1_pt', 'Viagens e transportes 1', 'verkehr_b1'),
    ('viagens_b1_pt_2', 'Viagens e transportes 2', 'verkehr_b1'),
    ('cidade_b1_pt', 'A cidade', 'stadt_gebaeude_b1'),
    ('escola_b1_pt', 'Escola e estudos 1', 'schule_b1'),
    ('escola_b1_pt_2', 'Escola e estudos 2', 'schule_b1'),
    ('cultura_b1_pt', 'Tempos livres e cultura 1', 'musik_kunst_b1'),
    ('cultura_b1_pt_2', 'Tempos livres e cultura 2', 'musik_kunst_b1'),
    ('desporto_b1_pt', 'Desporto', 'sport_b1'),
    ('media_b1_pt', 'Media e comunicação 1', 'medien_technologie_b1'),
    ('media_b1_pt_2', 'Media e comunicação 2', 'medien_technologie_b1'),
    ('dinheiro_b1_pt', 'Dinheiro e economia 1', 'einkaufen_geld_b1'),
    ('dinheiro_b1_pt_2', 'Dinheiro e economia 2', 'einkaufen_geld_b1'),
    ('sentimentos_b1_pt', 'Sentimentos e caráter', 'gefuehle_charakter_b1'),
    ('sociedade_b1_pt', 'Sociedade e política 1', 'politik_gesellschaft_b1'),
    ('sociedade_b1_pt_2', 'Sociedade e política 2', 'politik_gesellschaft_b1'),
    ('sociedade_b1_pt_3', 'Sociedade e política 3', 'politik_gesellschaft_b1'),
    ('lei_b1_pt', 'Lei e segurança', 'la_justicia'),
    ('ideias_b1_pt', 'Ideias e debate', 'la_argumentacion'),
    ('tempo_b1_pt', 'O tempo', 'zeit_kalender_b1'),
    ('quotidiano_b1_pt', 'Palavras do dia a dia', 'grundwortschatz_b1'),
]

NOMS = {
"familia_b1_pt": """
o adulto | l'adulte | O curso é só para adultos. | Le cours est réservé aux adultes.
o auxílio parental | l'allocation parentale | Durante a licença recebe-se o auxílio parental. | Pendant le congé parental, on reçoit une allocation parentale. | pl=auxílios parentais
o berçário | la crèche (pour bébés) | O nosso bebé vai ao berçário desde janeiro. | Notre bébé va à la crèche depuis janvier.
o carrinho de bebé | la poussette, landau | O carrinho de bebé não cabe no elevador. | La poussette ne rentre pas dans l'ascenseur. | pl=carrinhos de bebé
a companheira | la compagne (de vie) | A companheira dele é da Itália. | Sa compagne vient d'Italie. | g?
o companheiro | le compagnon (de vie) | O companheiro dela trabalha como arquiteto. | Son compagnon travaille comme architecte.
o compromisso | l'engagement | É um compromisso de longo prazo. | C'est un engagement à long terme.
a convivência | la vie commune | A convivência no apartamento funciona bem. | La vie commune dans l'appartement fonctionne bien.
a creche | la crèche, garderie | O nosso filho vai à creche há um ano. | Notre fils va à la crèche depuis un an.
o cuidado das crianças | la garde d'enfants | Um bom cuidado infantil é importante para pais que trabalham. | Une bonne garde d'enfants est importante pour les parents qui travaillent. | g? | pl=cuidados das crianças | ex?
a cumplicidade | la complicité | Há muita cumplicidade entre eles. | Il y a beaucoup de complicité entre eux.
o familiar | le proche, membre de la famille | Só familiares podem entrar no quarto. | Seuls les proches peuvent entrer dans la chambre. | g?
a fidelidade | la fidélité | Ele valoriza muito a fidelidade. | Il valorise beaucoup la fidélité.
a guarda | la garde d'enfant (droit) | O tribunal decidiu sobre a guarda. | Le tribunal a statué sur la garde des enfants. | g?
o idoso | le senior, personne âgée | Idosos pagam a metade. | Les seniors paient moitié prix.
a inveja | l'envie, la jalousie | Ele sente inveja do irmão. | Il envie son frère.
a licença parental | le congé parental | Ele vai tirar seis meses de licença parental. | Il prend six mois de congé parental. | g? | pl=licenças parentais
a licença-maternidade | le congé de maternité (protection) | Ela está em proteção à maternidade desde o início da gravidez. | Elle est en congé de maternité depuis le début de sa grossesse. | pl=licenças-maternidades | ex?
o mamãe | la maman |  |  | g? | ex=?
a nova geração | relève, jeunes talents | O clube está a procurar jovens talentos no desporto. | Le club recherche de jeunes talents sportifs. | g? | pl=novas gerações | ex?
o papai | le papa | O papai vem nos buscar às cinco. | Papa vient nous chercher à cinq heures.
a prima | la cousine | A minha prima estuda medicina. | Ma cousine étudie la médecine.
o rancor | la rancune | Ele não guarda rancor dela. | Il ne lui garde pas rancune.
a reconciliação | la réconciliation | A reconciliação veio meses depois. | La réconciliation est venue des mois après. | pl=reconciliações
o respeito | le respect | Eles tratam-se com respeito. | Ils se traitent avec respect.
o rompimento | la rupture | O rompimento foi tranquilo. | La rupture s'est passée calmement.
a separação | la séparation | A separação foi muito dolorosa para os dois. | La séparation a été très douloureuse pour les deux. | g? | pl=separações
a sobrinha | la nièce | A minha sobrinha estuda em Lisboa. | Ma nièce fait ses études à Lisbonne.
a tutela | la tutelle | Depois do divórcio ela assumiu a tutela. | Après le divorce, elle a obtenu la tutelle. | g?
a viúva | la veuve | Ela é viúva há dez anos. | Elle est veuve depuis dix ans. | g?
a vovó | la mamie, grand-mère | No domingo vamos visitar a vovó. | Dimanche, nous allons voir mamie. | g?
o vovô | le papi, grand-père | O vovô gosta de contar histórias antigas. | Papi aime raconter de vieilles histoires.
o órfão | l'orphelin, l'orpheline | Ele ficou órfão aos dez anos. | Il est devenu orphelin à dix ans. | pl=órfãos
""",
"trabalho_b1_pt": """
o acompanhamento | le suivi | Fazemos um acompanhamento todo mês. | Nous faisons un suivi chaque mois.
o acordo coletivo | la convention collective | O acordo coletivo fixa o salário mínimo. | La convention fixe le salaire minimum. | pl=acordos coletivos
a advogada | l'avocate | A advogada defende os meus interesses no tribunal. | L'avocate représente mes intérêts devant le tribunal. | g?
a agricultora | l'agricultrice | A agricultora cuida das vacas. | L'agricultrice s'occupe des vaches. | g?
a agência de publicidade | l'agence de publicité | Ela trabalhou numa grande agência de publicidade. | Elle a travaillé dans une grande agence de publicité. | g? | pl=agências de publicidade
o andamento | le déroulement, procédure | O andamento da prova foi explicado em detalhes. | Le déroulement de l'examen nous a été expliqué en détail.
o anexo | la pièce jointe ; installation | Em anexo segue o meu currículo. | Vous trouverez mon CV en pièce jointe.
a aprendizagem | l'apprentissage (formation) | Um ambiente de aprendizagem tranquilo faz mais efeito do que qualquer método. | Un environnement d'apprentissage calme agit plus que toute méthode.
a apresentação | la présentation | A apresentação dura quinze minutos. | La présentation dure quinze minutes. | pl=apresentações
a arquiteta | l'architecte | A arquiteta projeta um novo prédio comercial. | L'architecte conçoit un nouvel immeuble de bureaux. | g?
a artista | l'artiste (femme) | A artista pinta sobretudo paisagens. | L'artiste peint surtout des paysages. | g?
o assistente de consultório | l'assistant médical | O assistente mede a pressão primeiro. | L'assistant médical mesure d'abord la tension. | pl=assistentes de consultório | ex?
o assistente social | le travailleur social | O assistente social ajuda a família com os requerimentos. | Le travailleur social aide la famille pour les démarches. | pl=assistentes sociais
o atendente | l'employé de service |  |  | ex=?
a atividade | l'activité | Há muitas atividades para crianças. | Il y a beaucoup d'activités pour les enfants.
a atriz | l'actrice | A atriz foi premiada pelo papel. | L'actrice a été récompensée pour son rôle. | g?
o balanço | le bilan | O balanço do ano foi positivo. | Le bilan de l'année a été positif.
a caixa postal | la boîte postale | Escreva para a nossa caixa postal. | Écrivez à notre boîte postale. | pl=caixas postais
a capacidade | la capacité, compétence | Ele tem a capacidade de resolver problemas complexos rápido. | Il a la capacité de résoudre rapidement des problèmes complexes. | g?
o carimbo | le tampon, cachet | Sem carimbo o formulário não vale. | Sans cachet, le formulaire n'est pas valable.
a carta comercial | la lettre commerciale |  |  | pl=cartas comerciais | ex=?
a carta de apresentação | la lettre de motivation | A carta de apresentação não deve ter mais de uma página. | La lettre de motivation ne devrait pas dépasser une page. | g? | pl=cartas de apresentação
a carta de referência | certificat de travail | O meu antigo empregador escreveu-me uma boa carta de referência. | Mon ancien employeur m'a rédigé un bon certificat de travail. | g? | pl=cartas de referência
a carta registrada | la lettre recommandée | Mande o pedido de demissão por carta registrada. | Envoyez la résiliation en recommandé. | g? | pl=cartas registradas
o carteiro | le facteur | O carteiro vem toda manhã às dez. | Le facteur passe chaque matin à dix heures.
o cartão de visita | la carte de visite | Aqui está o meu cartão de visita. | Voici ma carte de visite. | pl=cartões de visita
a colaboração | la collaboration, participation | A colaboração dos voluntários foi decisiva para o projeto. | La collaboration des bénévoles a été décisive pour le projet. | g? | pl=colaborações
o comissário de bordo | le steward | O comissário nos mostra os lugares. | Le steward nous montre nos places. | pl=comissários de bordo | ex?
a competência | la responsabilité | Isso não é da minha área de competência. | Cela ne relève pas de mon domaine de compétence. | g?
o concorrente | le concurrent | O concorrente baixou os preços. | Le concurrent a baissé les prix.
a condições de trabalho | les conditions de travail | As condições de trabalho na empresa são muito boas. | Les conditions de travail dans l'entreprise sont très bonnes. | pl=condições de trabalho
a conferência | la conférence, réunion | A conferência começa às nove. | La conférence commence à neuf heures. | g?
a confirmação | la confirmation, attestation | O senhor vai receber uma confirmação por e-mail. | Vous recevrez une confirmation par courriel. | pl=confirmações
os conhecimentos | les connaissances (savoir) | Para esta vaga é preciso de ter bons conhecimentos de alemão. | Pour ce poste, il faut de bonnes connaissances en allemand. | g?
o consultor | le consultant | O consultor nos dá dicas valiosas. | Le consultant nous donne de précieux conseils.
o contador | le comptable | O contador confere o balanço anual. | Le comptable vérifie le bilan annuel.
a copiadora | la photocopieuse | A copiadora do escritório quebrou de novo. | La photocopieuse du bureau est encore en panne. | g?
o corretor de imóveis | l'agent immobilier | O corretor de imóveis nos mostra o apartamento. | L'agent immobilier nous fait visiter l'appartement. | pl=corretores de imóveis
a cozinheira | la cuisinière | A cozinheira experimentou uma receita nova. | La cuisinière a essayé une nouvelle recette. | g?
o cuidador | le soignant, aide-soignant | O cuidador vem toda manhã. | L'aide-soignant vient chaque matin.
""",
"trabalho_b1_pt_2": """
o cuidador de idosos | soignant pour personnes âgées | O meu tio trabalha como cuidador de idosos. | Mon oncle travaille comme soignant pour personnes âgées. | pl=cuidadores de idosos
a cuidadora de crianças | l'assistante maternelle | A cuidadora toma conta de quatro crianças. | L'assistante maternelle garde quatre enfants. | g? | pl=cuidadoras de crianças | ex?
a cuidadora de idosos | la soignante pour personnes âgées | A cuidadora cuida de dez moradores. | La soignante s'occupe de dix résidents. | g? | pl=cuidadoras de idosos | ex?
o curso de integração | le cours d'intégration | O curso de integração dura seis meses. | Le cours d'intégration dure six mois. | pl=cursos de integração
a demissão | licenciement | É possível entrar na justiça contra a demissão. | On peut contester le licenciement en justice. | g? | pl=demissões
o desafio | le défi | O emprego novo é um grande desafio para mim. | Le nouveau travail est un grand défi pour moi. | g?
a direção | la direction, la visite guidée | Ela assume a direção do novo projeto. | Elle prend la direction du nouveau projet. | pl=direções
a dona de casa | la femme au foyer | Depois do parto ela foi dona de casa por dois anos. | Après la naissance, elle a été femme au foyer pendant deux ans. | g? | pl=donas de casa
o dono | l'aubergiste, le patron | O dono do bar nos traz mais uma cerveja. | Le patron nous apporte encore une bière.
o eletricista | l'électricien | O eletricista conserta a fiação quebrada. | L'électricien répare le câble défectueux.
o empregado | le salarié | O empregado de mesa traz a comida. | Le serveur apporte le repas.
o empregador | l'employeur | O meu empregador paga uma parte do seguro. | Mon employeur paie une partie de l'assurance.
a empregadora | l'employeuse | A empregadora oferece horários flexíveis. | L'employeuse propose des horaires flexibles. | g?
os empresários | les gens d'affaires |  |  | g? | ex=?
a escolha da profissão | le choix professionnel | Muitos jovens têm dificuldade na escolha da profissão. | Le choix professionnel est difficile pour beaucoup de jeunes. | pl=escolhas da profissão
a especialista | l'expert | A especialista explicou as causas da mudança climática. | L'experte a expliqué les causes du changement climatique. | g?
a estagiária | la stagiaire (femme) | A estagiária trabalha na redação há um mês. | La stagiaire travaille à la rédaction depuis un mois. | g?
o estagiário | le stagiaire | O estagiário aprende rápido. | Le stagiaire apprend vite.
a estratégia | la stratégie | A estratégia mudou em janeiro. | La stratégie a changé en janvier.
a filial | la filiale | Abriram uma filial em Lisboa. | Ils ont ouvert une filiale à Lisbonne.
o fim do expediente | la fin de la journée de travail | Às cinco horas termina o meu expediente. | À cinq heures, j'ai fini ma journée. | g? | pl=fins do expediente | ex?
o fisioterapeuta | physiothérapeute | O fisioterapeuta a ajuda a andar. | Le physiothérapeute l'aide à marcher.
a forma de tratamento | la formule d'appel | Numa carta a forma de tratamento é importante. | Dans une lettre, la formule d'appel est importante. | g? | pl=formas de tratamento
a formação continuada | la formation continue | A empresa oferece capacitação regularmente. | L'entreprise propose une formation continue régulière. | pl=formações continuadas | ex?
a formação profissional | la formation professionnelle | Ele encontrou uma vaga de formação profissional. | Il a trouvé une place de formation. | pl=formações profissionais
o fornecedor | le fournisseur | Eles trocaram de fornecedor em janeiro. | Ils ont changé de fournisseur en janvier.
a fusão | la fusion | A fusão foi concluída em março. | La fusion s'est conclue en mars. | pl=fusões
a gerência | la direction | A diretoria anunciou a mudança ontem. | La direction a annoncé le changement hier. | ex?
a greve | la grève | A greve durou dois dias. | La grève a duré deux jours.
a guia turística | la guide touristique (femme) | A guia conta muitas histórias interessantes. | La guide touristique raconte beaucoup d'histoires intéressantes. | g? | pl=guias turísticas | ex?
o guia turístico | la guide touristique (personne ou livre) | O guia nos mostra os principais pontos turísticos. | Le guide touristique nous montre les principaux sites. | pl=guias turísticos | ex?
a iniciativa | l'initiative | Foi uma iniciativa da equipa. | Ce fut une initiative de l'équipe.
o instrutor do curso | l'animateur de cours, formateur | Pergunte ao instrutor do curso, por favor. | Adressez-vous au formateur, s'il vous plaît. | pl=instrutores do curso
a jornada de trabalho | la journée de travail | Ele tem jornada de sete horas. | Il a une journée de sept heures. | pl=jornadas de trabalho | ex?
a jornalista | la journaliste | A jornalista investiga esse assunto há semanas. | La journaliste enquête sur ce sujet depuis des semaines. | g?
a mensalidade | la cotisation, la part | A mensalidade é de trinta euros. | La cotisation mensuelle est de trente euros.
o mestre | le maître, le champion | Ele é mestre no seu ofício. | Il est maître dans son métier. | g?
a monitora | l'encadrante, animatrice | A monitora cuida de dez adolescentes. | L'animatrice s'occupe de dix adolescents. | g?
o mundo do trabalho | le monde du travail | O mundo do trabalho mudou muito nos últimos anos. | Le monde du travail a beaucoup changé ces dernières années. | pl=mundos do trabalho
o mérito | le mérite | A promoção foi por mérito próprio. | La promotion s'est faite au mérite.
""",
"trabalho_b1_pt_3": """
a negociação | la négociation | A negociação foi longa. | La négociation a été longue. | pl=negociações
o nutricionista | le conseiller en nutrition | A nutricionista recomenda mais legumes. | La conseillère en nutrition recommande plus de légumes.
a oportunidade de carreira | l'opportunité de carrière | Este emprego oferece boas oportunidades de carreira. | Cet emploi offre de bonnes opportunités de carrière. | pl=oportunidades de carreira
a orientação | la conseil, consultation | A orientação no banco foi gratuita. | La consultation à la banque était gratuite. | g? | pl=orientações
a parteira | la sage-femme | A parteira chegou às três da madrugada. | La sage-femme est arrivée à trois heures du matin. | g?
a permissão de trabalho | le permis de travail | Sem permissão de trabalho ele não pode trabalhar. | Sans permis de travail, il n'a pas le droit de travailler. | g? | pl=permissões de trabalho
o personal trainer | l'entraîneur sportif | O personal trainer faz um novo plano de treino para ela. | L'entraîneur sportif lui prépare un nouveau programme d'entraînement. | pl=personais traineres
o período de experiência | la période d'essai | O período de experiência aqui dura seis meses. | La période d'essai dure six mois chez nous. | pl=períodos de experiência
o pessoal | le personnel | Pintar significa para ela uma verdadeira realização pessoal. | Peindre représente pour elle un véritable épanouissement personnel. | g?
o planeamento | la planification | O planeamento demora mais que o trabalho. | La planification prend plus de temps que le travail.
a prioridade | la priorité | A segurança é a prioridade. | La sécurité est la priorité.
o profissional | l'artisan | O profissional está a instalar a cozinha nova. | L'artisan installe la nouvelle cuisine.
o profissional qualificado | la travailleur qualifié | Neste setor faltam profissionais qualificados. | Ce secteur manque de main-d'œuvre qualifiée. | g? | pl=profissionais qualificados
a proposta | la proposition | Enviei a proposta ontem. | J'ai envoyé la proposition hier.
o pré-requisito | la condition préalable | Um bom alemão é pré-requisito para esta vaga. | De bonnes connaissances en allemand sont une condition pour ce poste. | pl=prés-requisitos
o quadro de funcionários | l'effectif | O quadro de funcionários cresceu dez por cento. | L'effectif a augmenté de dix pour cent. | pl=quadros de funcionários
o refeitório | la cantine | No almoço eu como no refeitório. | À midi, je mange à la cantine.
o representante | le représentant | O representante da empresa chega às dez. | Le représentant de l'entreprise vient à dix heures.
o repórter | journaliste, reporter | Um repórter entrevista o vencedor depois do jogo. | Un journaliste interviewe le vainqueur après le match.
a responsabilidade | la responsabilité | Ele assumiu a responsabilidade pelo erro. | Il a assumé la responsabilité de l'erreur.
o sindicato | le syndicat | O sindicato convocou uma reunião. | Le syndicat a convoqué une réunion.
o soldado | le soldat | O avô dele foi soldado. | Son grand-père était soldat.
o substituto | le remplacement, représentation | Precisamos de um substituto para a colega doente. | Nous avons besoin d'un remplaçant pour la collègue malade.
o sócio | l'associé | O sócio dele mora no Chile. | Son associé vit au Chili.
o talhante | le boucher | Compro a carne no talho. | J'achète la viande chez le boucher. | g? | ex?
o teletrabalho | le télétravail | O home office economiza duas horas por dia para ele. | Le télétravail lui économise deux heures par jour. | ex?
o trabalho por turnos | le travail posté, service par équipes | Como enfermeira eu trabalho por turnos. | En tant qu'infirmière, je travaille en horaires postés. | pl=trabalhos pores turnos
o trabalho temporário | le travail intérimaire | Ele começou com trabalho temporário. | Il a commencé par de l'intérim. | pl=trabalhos temporários
o tradutor | le traducteur | O tradutor está a trabalhar num texto difícil. | Le traducteur travaille sur un texte difficile.
a tradutora | la traductrice | A tradutora domina quatro línguas. | La traductrice maîtrise quatre langues. | g?
a vaga de aprendiz | la place d'apprentissage | Ele está a procurar uma vaga de aprendiz de cozinheiro. | Il cherche une place d'apprentissage comme cuisinier. | pl=vagas de aprendiz
a vaga de formação profissional | la place de formation | Ele encontrou uma vaga de formação profissional. | Il a trouvé une place de formation. | pl=vagas de formação profissional
a vocação | la vocation | Ensinar é a vocação dela. | Enseigner est sa vocation. | pl=vocações
o zelador | le concierge, gardien | O zelador tem a chave. | Le concierge a la clé.
a área | le domaine, secteur | Ela trabalha na área de marketing. | Elle travaille dans le domaine du marketing.
""",
"comida_b1_pt": """
o aditivo | l'additif | O produto não contém aditivos. | Le produit ne contient pas d'additifs.
a alimentação | l'alimentation | Ele cuida muito da alimentação. | Il fait très attention à son alimentation. | pl=alimentações
o alimento | la denrée alimentaire | Compramos os nossos alimentos na feira semanal. | Nous achetons nos denrées alimentaires au marché hebdomadaire.
o aperitivo | l'apéritif | Tomamos um aperitivo antes do almoço. | Nous prenons un apéritif avant le repas.
o apetite | l'appétit | Depois da doença ele tem pouco apetite. | Après la maladie, il a peu d'appétit. | g?
o aroma | l'arôme | O aroma do pão enche a casa. | L'arôme du pain remplit la maison.
o aspargo | l'asperge | Na primavera há aspargos brancos no mercado. | Au printemps, il y a des asperges blanches au marché.
o assado | le rôti | Aos domingos lá em casa tem assado. | Le dimanche, chez nous, il y a un rôti.
a beterraba | la betterave | A beterraba tinge tudo de vermelho. | La betterave teint tout en rouge.
o bife | le steak | Eu queria o bife, por favor. | Je prendrai le steak, s'il vous plaît.
o bife à milanesa | l'escalope panée | Vou querer um bife à milanesa com batata frita. | Je prends une escalope avec des frites. | pl=bifes às milanesas
o bolachas | la petits gâteaux, pâtisserie | Com o café tem bolachas. | Avec le café, il y a des petits gâteaux. | g? | pl=bolachas
o bolinho | la boulette (de pomme de terre) | Com o assado tem bolinhos. | Avec le rôti, il y a des boulettes.
o bufê | le buffet | Na festa havia um bufê grande. | Il y avait un grand buffet pendant la fête.
o caldo | le bouillon | O caldo leva frango e legumes. | Le bouillon contient du poulet et des légumes.
a caloria | la calorie | Ele conta as calorias de cada refeição. | Il compte les calories de chaque repas.
a canela | la cannelle | Polvilha um pouco de canela na maçã. | Saupoudre un peu de cannelle sur la pomme. | g?
o carne moída | la viande hachée | Para o molho eu preciso de carne moída. | Pour la sauce, il me faut de la viande hachée. | g? | pl=carnes moídas
a cervejaria ao ar livre | la brasserie en plein air |  |  | pl=cervejarias aos ares livres | ex=?
o chantili | la crème fouettée (autrichien) | O café é servido com chantili. | Le café est servi avec de la crème fouettée. | g?
o chip | la puce (électronique) | O cartão de crédito tem um chip pequeno. | La carte de crédit a une petite puce.
o chocolate quente | le cacao, chocolat chaud | De manhã as crianças tomam chocolate quente. | Le matin, les enfants boivent du chocolat chaud. | g? | pl=chocolates quentes
a churrasqueira | le barbecue, gril | A churrasqueira fica no fundo do jardim. | Le barbecue est au fond du jardin. | g?
a comida pronta | le plat préparé | Comida pronta costuma ter muito sal. | Les plats préparés contiennent souvent beaucoup de sel. | g? | pl=comidas prontas
o comportamento alimentar | le comportement alimentaire | O comportamento alimentar dela mudou depois do diagnóstico. | Son comportement alimentaire a changé après le diagnostic. | pl=comportamentos alimentares
a conserva | la conserve | Guardamos conservas para o inverno. | Nous gardons des conserves pour l'hiver.
a conversa depois da refeição | le moment après le repas | A conversa de sobremesa durou duas horas. | Le moment après le repas a duré deux heures. | pl=conversas depois da refeição | ex?
a couve-de-bruxelas | le chou de Bruxelles | Poucas crianças gostam de couve-de-bruxelas. | Peu d'enfants aiment les choux de Bruxelles. | pl=couves-des-bruxelas
o doce | sucrerie, bonbon | As crianças adoram doces. | Les enfants adorent les sucreries. | g?
o ensopado | le ragoût | O ensopado cozinha em fogo baixo. | Le ragoût cuit à feu doux.
a especialidade | la spécialité | A especialidade da casa é o cordeiro. | La spécialité de la maison est l'agneau.
a fibra | la fibre | O pão integral fornece fibras. | Le pain complet apporte des fibres.
o fogão | la cuisinière | O fogão tem quatro bocas. | La cuisinière a quatre plaques de cuisson. | pl=fogões
os frutas | les fruits | Coma frutas e legumes todo dia. | Mange des fruits et des légumes tous les jours. | g?
o fósforo | l'allumette | Ele acende a vela com um fósforo. | Il allume la bougie avec une allumette.
a fôrma | le moule à gâteau | A fôrma está untada com manteiga. | Le moule à gâteau est beurré. | g?
a gastronomia | la gastronomie | A gastronomia do norte é substanciosa. | La gastronomie du nord est copieuse.
a gordura | la graisse, matière grasse | Gordura demais na comida faz mal. | Trop de graisse dans la nourriture n'est pas sain.
o género alimentício | la denrée alimentaire | Os géneros alimentícios ficaram mais caros. | Les denrées alimentaires ont augmenté. | pl=géneros alimentícios
o hambúrguer | le hamburger | As crianças querem hambúrguer de novo. | Les enfants veulent encore un hamburger. | g?
""",
"comida_b1_pt_2": """
o hábito alimentar | l'habitude alimentaire | Os meus hábitos alimentares mudaram desde a mudança. | Mes habitudes alimentaires ont changé depuis le déménagement. | pl=hábitos alimentares
o ketchup | le ketchup | Ele sempre come a batata frita com ketchup. | Il mange toujours ses frites avec du ketchup. | g?
o lanche | le casse-croûte, goûter | O lanche das crianças é às cinco. | Le goûter des enfants est à cinq heures.
o lanche da tarde | le goûter | O lanche das crianças é às cinco. | Le goûter des enfants est à cinq heures. | pl=lanches da tarde | ex?
o lanchinho | la collation, en-cas | Entre as refeições eu gosto de comer um lanchinho. | Entre les repas, j'aime bien prendre une collation.
o líquido | liquide | Este líquido não pode ser bebido. | On ne doit pas boire ce liquide.
a maionese | la mayonnaise | Ela sempre faz a maionese em casa. | Elle fait toujours sa mayonnaise elle-même. | g?
a margarina | la margarine | Eu uso margarina em vez de manteiga. | Je prends de la margarine au lieu du beurre. | g?
o molho | la sauce | O molho está salgado demais. | La sauce est trop salée.
o muesli | le muesli | No pequeno-almoço eu como muesli. | Au petit-déjeuner, je mange du muesli. | g?
a nutrição | la nutrition | Ela estuda nutrição na universidade. | Il étudie la nutrition à l'université. | pl=nutrições
a panqueca | la crêpe, beignet | Hoje no pequeno-almoço tem panqueca. | Aujourd'hui, il y a des crêpes au petit-déjeuner. | g?
a pastilha elástica | le chewing-gum | Mascar pastilha elástica não é permitido na sala de aula. | Mâcher du chewing-gum n'est pas autorisé en classe. | g? | pl=pastilhas elásticas
o prato preferido | le plat préféré | Pizza é o meu prato preferido. | La pizza est mon plat préféré. | pl=pratos preferidos
o prato principal | le plat principal | O prato principal chega em poucos minutos. | Le plat principal arrive dans quelques minutes. | pl=pratos principais
o prazer | le plaisir (savourer) | O pequeno-almoço é um verdadeiro prazer para ela. | Le café du matin est un vrai plaisir pour elle. | g?
o preparo | la préparation (cuisine) | O preparo leva só vinte minutos. | La préparation ne prend que vingt minutes.
a proteína | la protéine | As lentilhas têm muita proteína. | Les lentilles ont beaucoup de protéines.
o rabanete | le radis | Os rabanetes são vermelhos e um pouco picantes. | Les radis sont rouges et un peu piquants.
a refeição | le repas | Três refeições por dia são mais que suficientes para mim. | Trois repas par jour me suffisent amplement. | pl=refeições
o requeijão fresco | le fromage blanc | No pequeno-almoço eu como quark com frutas. | Au petit-déjeuner, je mange du fromage blanc avec des fruits. | pl=requeijões frescos | ex?
o ruibarbo | la rhubarbe | Com o ruibarbo faz-se compota. | Avec la rhubarbe, on fait de la confiture.
a textura | la texture | Gosto da textura do arroz. | J'aime la texture du riz.
a vitamina | la vitamine | A laranja tem vitamina C. | L'orange contient de la vitamine C.
a água mineral | l'eau minérale | Uma água mineral, por favor. | Une eau minérale, s'il vous plaît. | pl=águas minerais
""",
"casa_b1_pt": """
a agulha | l'aiguille | Preciso de uma agulha mais fina. | Il me faut une aiguille plus fine.
a alavanca | le levier | Puxe a alavanca para baixo. | Tire le levier vers le bas.
a alça | la poignée | A alça da bolsa quebrou. | La poignée du sac est cassée. | g?
o andar de cima | l'étage supérieur | O consultório fica no primeiro andar. | Le cabinet est au premier étage. | pl=andares de cima | ex?
a antena | l'antenne | A antena entortou com o vento. | L'antenne s'est tordue avec le vent.
o apito | le sifflet | A escalação foi mudada uma hora antes do apito inicial. | La composition a été modifiée une heure avant le coup d'envoi.
o ar-condicionado | la climatisation | O quarto tem ar-condicionado. | La chambre a la climatisation. | pl=ares-condicionados
a armadilha | le piège | O rato caiu na armadilha. | La souris est tombée dans le piège.
o armazenamento | le rangement | O armazenamento dos dados é limitado a dois anos. | Le stockage des données est limité à deux ans.
o arranjo | la réparation | O arranjo custa mais que o aparelho. | La réparation coûte plus cher que l'appareil.
o atacador | le lacet | O teu atacador desamarrou. | Un de tes lacets s'est défait.
a auxílio-moradia | l'allocation logement | Para o auxílio-moradia é preciso de fazer um requerimento. | Pour l'allocation logement, il faut faire une demande. | g? | pl=auxílios-moradias
o banheira | la baignoire |  |  | ex=?
a cabana | la cabane, refuge |  |  | ex=?
o cachimbo | la pipe, le sifflet | O meu pai fumava cachimbo. | Mon père fumait la pipe.
a cómoda | la commode | A cómoda fica ao lado da cama. | La commode se trouve à côté du lit. | g?
a decoração | l'aménagement, mobilier | A decoração do apartamento é muito moderna. | L'aménagement de l'appartement est très moderne. | g? | pl=decorações
o eletrodoméstico | l'appareil ménager | Este eletrodoméstico economiza muita energia. | Cet appareil ménager économise beaucoup d'énergie.
o engradado | la caisse, le casier | Ele leva um engradado de água lá para cima. | Il monte une caisse d'eau.
a escadaria | la cage d'escalier | Na escadaria tem cheiro de tinta fresca. | Ça sent la peinture fraîche dans la cage d'escalier.
o ferro de passar | le fer à repasser | O ferro de passar ainda está quente. | Le fer à repasser est encore chaud. | pl=ferros de passar
o fogo | le feu | O fogo apagou sozinho. | Le feu s'est éteint tout seul.
a gráfica | l'imprimerie | Levaram o cartaz à gráfica. | Ils ont porté l'affiche à l'imprimerie.
o incómodo | dérangement, perturbation | Desculpe o incómodo, só tenho uma pergunta rápida. | Excusez le dérangement, j'ai juste une petite question.
a lanterna | la lampe de poche | Pegue a lanterna, está escuro. | Prends la lampe de poche, il fait sombre.
o lar | le foyer, résidence | O lar de idosos fica na periferia. | La résidence pour personnes âgées se trouve en périphérie.
a lata de lixo | la poubelle | A lata de lixo fica bem em frente da casa. | La poubelle se trouve juste devant la maison. | g? | pl=latas de lixo
a lenha | le bois de chauffage | Guardamos a lenha embaixo da varanda. | Nous rangeons le bois sous le porche.
a limpeza | le nettoyage | A limpeza da escada é tarefa de todos os inquilinos. | Le nettoyage de la cage d'escalier est la tâche de tous les locataires. | g?
o local de residência | le lieu de résidence | Preencha o seu local de residência, por favor. | Indiquez votre lieu de résidence, s'il vous plaît. | pl=locais de residência
a loja de ferragens | la quincaillerie | Compre os parafusos na loja de ferragens. | Achète les vis à la quincaillerie. | pl=lojas de ferragens
a lâmina | la lame | Troque a lâmina, já não corta. | Change la lame, elle ne coupe plus.
o machado | la hache | Com o machado ele racha lenha. | Il coupe du bois avec la hache.
o morador | l'habitant, résident | Os moradores do prédio conhecem-se todos. | Les habitants de l'immeuble se connaissent tous.
o pano | le chiffon | Passe um pano na mesa. | Passe un chiffon sur la table.
o pavio | la mèche | O pavio da vela é muito curto. | La mèche de la bougie est très courte.
o pincel | le pinceau | Limpe o pincel com água morna. | Nettoie le pinceau à l'eau tiède. | pl=pincéis
o plugue | la fiche, prise (mâle) | Tira o plugue da tomada. | Débranche la fiche de la prise murale.
o pregador | la pince | Faltam pregadores para estender a roupa. | Il manque des pinces pour étendre le linge.
o produto de limpeza | le produit de nettoyage | O produto de limpeza tem cheiro de limão. | Le produit de nettoyage sent le citron. | pl=produtos de limpeza
o quitinete | le studio, petit appartement | Alugamos um apartamento pequeno por uma semana. | Nous louons un studio pour une semaine. | g? | ex?
o regulamento do prédio | le règlement intérieur | Pelo regulamento do prédio é proibido fazer churrasco na sacada. | Selon le règlement intérieur, griller sur le balcon est interdit. | pl=regulamentos do prédio
a república | la colocation | Ele mora numa república com três amigos. | Il vit en colocation avec trois amis.
o sabão em pó | la lessive, détergent | Este sabão em pó é ecológico. | Cette lessive est respectueuse de l'environnement. | pl=sabões ens pós
o saco | le sac (grand) | Põe o saco no canto. | Mets le sac dans le coin.
o subsolo | le sous-sol | A lavanderia fica no subsolo. | La buanderie est au sous-sol.
a sujeira | la saleté | A sujeira na escada vem das botas da obra. | La saleté dans l'escalier vient des chaussures de chantier. | g?
o tubo | le tube, le tuyau | O cano do ralo está entupido. | Le tuyau d'évacuation est bouché. | ex?
o valor do renda | le prix du loyer | Os rendas na cidade subiram muito. | Les prix des loyers en ville ont fortement augmenté. | pl=valores do renda | ex?
a viga | la poutre | As vigas do teto são de carvalho. | Les poutres du plafond sont en chêne.
a área útil | la surface habitable | A área útil é de setenta e cinco metros quadrados. | La surface habitable est de soixante-quinze mètres carrés. | g? | pl=áreas úteis
""",
"saude_b1_pt": """
a acessibilidade | l'accessibilité | A acessibilidade do metro melhorou. | L'accessibilité du métro s'est améliorée.
a alta | la sortie (d'hôpital) | Ele recebeu alta na terça. | On lui a donné sa sortie mardi.
o analgésico | l'antidouleur | Tome um analgésico, se for preciso. | Prenez un antidouleur si nécessaire.
a anestesia | l'anesthésie | A cirurgia é feita com anestesia geral. | L'opération se déroule sous anesthésie générale. | g?
a articulação | l'articulation | As articulações dele doem no inverno. | Ses articulations lui font mal en hiver. | pl=articulações
a asa | l'aile | O pássaro quebrou a asa. | L'oiseau s'est cassé l'aile. | g?
a autonomia | l'autonomie | Ele recuperou a autonomia em um ano. | Il a retrouvé son autonomie en un an.
a barreira | la barrière | As barreiras arquitetónicas continuam. | Les barrières architecturales demeurent.
o batimento | le battement de cœur | Ouve-se o batimento com o aparelho. | On entend le battement avec l'appareil.
a cadeira de rodas | le fauteuil roulant | Ele anda de cadeira de rodas desde o acidente. | Il est en fauteuil roulant depuis l'accident. | pl=cadeiras de rodas
a carteira de vacinação | carnet de vaccination | Não esquece a carteira de vacinação na consulta. | N'oublie pas ton carnet de vaccination pour la visite chez le médecin. | g? | pl=carteiras de vacinação
o cartão do seguro-saúde | la carte d'assurance maladie | Traga o seu cartão do seguro-saúde, por favor. | Apportez votre carte d'assurance maladie, s'il vous plaît. | pl=cartões do seguro-saúde
o centro cirúrgico | le bloc opératoire | Ele entrou no centro cirúrgico às sete. | Il est entré au bloc à sept heures. | pl=centros cirúrgicos
a chamada de emergência | l'appel d'urgence | Num acidente é preciso de ligar logo para a emergência. | En cas d'accident, il faut immédiatement composer le numéro d'urgence. | g? | pl=chamadas de emergência | ex?
o cigarro | la cigarette | Ele parou de fumar cigarro há cinco anos. | Il a arrêté de fumer des cigarettes il y a cinq ans.
a cirurgia | la chirurgie | A cirurgia durou quatro horas. | La chirurgie a duré quatre heures.
o cirurgião | le chirurgien | O cirurgião explicou a operação. | Le chirurgien a expliqué l'opération. | pl=cirurgiões
a clínica | la clinique | Ele está internado na clínica desde segunda. | Il est à la clinique depuis lundi.
o consultório médico | le cabinet médical | O consultório fica aberto até as dezoito horas. | Le cabinet médical est ouvert jusqu'à dix-huit heures. | pl=consultórios médicos | ex?
o contágio | la contagion | O contágio ocorre pelo ar. | La contagion se produit par l'air.
a coriza | le rhume | Estou com uma coriza leve. | J'ai un petit rhume.
o creme dental | le dentifrice | O creme dental está quase acabando. | Le dentifrice est presque fini. | pl=cremes dentais
o cuidado | la prise en charge, garde | Cuidado, o degrau está escorregadio! | Prudence, la marche est glissante !
os cuidado de idosos | les soins aux personnes âgées | Ela especializou-se em cuidado de idosos. | Elle s'est spécialisée dans les soins aux personnes âgées.
o cérebro | le cerveau | O cérebro consome muita energia. | Le cerveau consomme beaucoup d'énergie.
a deficiência | le handicap | A deficiência não o impede de trabalhar. | Le handicap ne l'empêche pas de travailler.
o diagnóstico | le diagnostic | O diagnóstico chegou em uma semana. | Le diagnostic est arrivé en une semaine.
a doação | le don | A doação de sangue é rápida. | Le don de sang est rapide. | pl=doações
o doente | le malade (personne) | O doente precisa de muito repouso. | Le malade a besoin de beaucoup de repos.
a dose | la dose | A dose é de dois comprimidos. | La dose est de deux comprimés.
a droga | la drogue | Aqui as drogas são estritamente proibidas. | Les drogues sont strictement interdites ici.
o efeito | l'effet | O efeito aparece em três dias. | L'effet se remarque au bout de trois jours.
a enfermagem | les soins infirmiers | Ela fez uma formação em enfermagem. | Elle a suivi une formation en soins infirmiers.
a epidemia | l'épidémie | A epidemia durou um inverno. | L'épidémie a duré un hiver.
a escova de dentes | la brosse à dents | Esqueci a minha escova de dentes. | J'ai oublié ma brosse à dents. | pl=escovas de dentes
o estetoscópio | le stéthoscope | A médica ausculta os meus pulmões com o estetoscópio. | La médecin m'écoute les poumons avec le stéthoscope.
a ferida | la blessure | A ferida precisa de ser enfaixada regularmente. | La blessure doit être pansée régulièrement. | g?
a força | la force | Depois da doença ainda lhe falta força. | Après la maladie, il lui manque encore de la force. | g?
o fumante | le fumeur | Para fumantes tem um lugar lá fora. | Il y a un espace dehors pour les fumeurs. | g?
o fármaco | le médicament | O medicamento chega às farmácias em maio. | Le médicament arrive en pharmacie en mai. | ex?
""",
"saude_b1_pt_2": """
o fígado | le foie | O álcool afeta o fígado. | L'alcool affecte le foie.
o fôlego | le souffle, respiration | Depois da corrida eu fiquei sem fôlego. | Après la course, j'étais hors d'haleine.
o gesso | le plâtre | Ele está com o braço engessado há duas semanas. | Il porte un plâtre au bras depuis deux semaines. | ex?
a gravidez | la grossesse | Durante a gravidez ela não fuma. | Pendant la grossesse, elle ne fume pas. | g?
o histórico médico | le dossier médical | O prontuário está no computador. | Le dossier est dans l'ordinateur. | pl=históricos médicos | ex?
o horário de atendimento | les heures de consultation | O horário de atendimento é das oito ao meio-dia. | La consultation a lieu de huit heures à midi. | pl=horários de atendimento
a infecção | l'infection | O médico constatou uma infecção. | Le médecin a constaté une infection. | pl=infecções
a inflamação | l'inflammation | A ferida virou uma inflamação. | La blessure s'est transformée en inflammation. | pl=inflamações
o ingestão | la prise (de médicaments) | Os comprimidos devem ser tomados duas vezes por dia. | La prise des comprimés se fait deux fois par jour. | pl=ingestões | ex?
a injeção | la piqûre, seringue | A enfermeira dá-lhe uma injeção. | L'infirmière lui fait une piqûre. | pl=injeções
o lar de idosos | la maison de retraite | A minha avó mora num lar de idosos. | Ma grand-mère habite dans une maison de retraite. | pl=lares de idosos
o lente de contacto | la lentille de contact | Ela usa lente de contacto desde o ano passado. | Elle porte des lentilles de contact depuis l'année dernière. | g? | pl=lentes de contacto
a maternidade | la maternité (service) | O bebé nasceu na maternidade. | Le bébé est né au service de maternité.
o medicamento para dormir | le somnifère | O médico receitou-lhe um medicamento para dormir. | Le médecin lui a prescrit un somnifère. | pl=medicamentos paras dormires
a medicina | la médecine, médicament | Ela estuda medicina na universidade. | Elle étudie la médecine à l'université. | g?
a melhora | le rétablissement, amélioration | Melhoras! | Bon rétablissement ! | g?
o médico especialista | le spécialiste médical | O especialista recomendou-me uma segunda opinião. | Le spécialiste m'a recommandé un second avis. | pl=médicos especialistas | ex?
o músculo | le muscle | Ele machucou um músculo. | Il s'est fait mal à un muscle.
o nervo | le nerf | O nervo do braço está inflamado. | Le nerf du bras est enflammé.
o não fumante | le non-fumeur | Eu queria um lugar para não fumantes. | J'aimerais une place non-fumeur. | pl=nões fumantes | ex?
o olhar | le regard ; vue | Ele lançou-me um olhar de reprovação. | Il m'a lancé un regard de reproche. | g?
o osso | l'os | Ele quebrou um osso do pé. | Il s'est cassé un os du pied.
a panturrilha | le mollet | Depois de correr, as minhas panturrilhas doem. | Après la course, j'ai mal aux mollets.
a pasta de dentes | le dentifrice |  |  | g? | pl=pastas de dentes | ex=?
a pomada | la pommade | A pomada ajuda contra a dor. | La pommade soulage la douleur. | g?
a prevenção | la prévention | A prevenção custa menos que o tratamento. | La prévention coûte moins cher que le traitement. | pl=prevenções
o pulmão | le poumon | A fumaça prejudica os pulmões. | La fumée abîme les poumons. | pl=pulmões
a pílula | la pilule, comprimé | Toma a pílula depois de comer. | Prends le comprimé après le repas. | g?
a rampa | la rampe | A rampa fica à esquerda. | La rampe est à gauche.
a reabilitação | rééducation | Depois do acidente ele está a fazer uma reabilitação longa. | Après l'accident, il fait une longue rééducation. | pl=reabilitações
o rim | le rein | Beba água para cuidar dos rins. | Bois de l'eau pour ménager les reins.
o risco de morte | le danger de mort | Atenção, risco de morte! | Attention, danger de mort ! | pl=riscos de morte
a saúde pública | la santé publique | A saúde pública funciona bem aqui. | La santé publique fonctionne bien ici. | pl=saúdes públicas
a silhueta | la silhouette ; personnage | Na neblina só se viam silhuetas. | Dans le brouillard on ne voyait que des contours. | g?
a substância que vicia | la substance addictive | O álcool também é uma substância que vicia. | L'alcool est aussi une substance addictive. | pl=substâncias ques vicias
o tabaco | le tabac | O tabaco ficou caro aqui. | Le tabac est devenu cher ici.
a terapia | la thérapie | A terapia o ajudou muito. | La thérapie l'a beaucoup aidé.
o transplante | la greffe | O transplante correu bem. | La greffe s'est bien passée.
as urgências | les urgences (service) |  |  | ex=?
a vacinação | la vaccination | A vacina protege contra a doença. | La vaccination protège contre la maladie. | pl=vacinações | ex?
a veia | la veine | A enfermeira procura uma veia. | L'infirmière cherche une veine.
o álcool | l'alcool | Ele não bebe álcool durante a semana. | Il ne boit pas d'alcool en semaine.
o órgão | l'organe | O coração é um órgão vital. | Le cœur est un organe vital. | pl=órgãos
""",
"roupa_b1_pt": """
a calça de moletom | le pantalon de jogging | Para correr ela usa uma calça de moletom confortável. | Pour courir, elle porte un pantalon de jogging confortable. | pl=calças de moletom
os joias | les bijoux | Ela raramente usa joias. | Elle porte rarement des bijoux. | g?
a regata | le débardeur, haut | No verão ela usa muito regata. | En été, elle porte souvent un débardeur. | g?
o uniforme | l'uniforme | O motorista usa um uniforme azul. | Le chauffeur porte un uniforme bleu.
""",
"natureza_b1_pt": """
o adubo | l'engrais | Eles usam adubo natural. | Ils utilisent de l'engrais naturel.
a agricultura | l'agriculture | A agricultura emprega mil pessoas. | L'agriculture emploie mille personnes.
a altitude | l'altitude | O vilarejo fica a mil metros de altitude. | Le village est à mille mètres d'altitude.
a altura | la hauteur, altitude | Em criança, eu media a altura de todas as árvores. | Enfant, je mesurais la hauteur de tous les arbres.
o ambiente | l'ambiance | Precisamos de proteger o meio ambiente. | Nous devons protéger l'environnement.
o apagão | la coupure de courant | Houve um apagão de três horas. | Il y a eu une coupure de trois heures. | pl=apagões
os arredores | les environs, alentours | Nos arredores há muitas trilhas. | Dans les environs, il y a beaucoup de sentiers. | g?
a astronomia | l'astronomie | A astronomia o apaixona desde criança. | L'astronomie le passionne depuis l'enfance.
o atalho | le raccourci | Conheço um atalho pela floresta. | Je connais un raccourci par la forêt.
a autoestrada | l'autoroute | A autoestrada está interditada. | L'autoroute est coupée.
a biodiversidade | la biodiversité | A biodiversidade do rio recupera-se. | La biodiversité du fleuve se rétablit.
o boi | le bovin, bœuf | O meu avô arava com dois bois. | Mon grand-père labourait avec deux bœufs. | g?
o brinquedo | le jouet | Recolha os brinquedos antes do jantar. | Ramasse les jouets avant le dîner.
a brisa | la brise | Sopra uma brisa agradável. | Il y a une brise agréable.
o cais | le quai | Os barcos descarregam no cais. | Les bateaux déchargent sur le quai. | pl=cais
o carvão | le charbon | Fecharam a última mina de carvão. | Ils ont fermé la dernière mine de charbon. | pl=carvões
a casca | l'écorce | A casca destas árvores é bem lisa. | L'écorce de ces arbres est toute lisse. | g?
a catástrofe | la catastrophe | A enchente foi uma catástrofe. | L'inondation a été une catastrophe.
o cervo | le cerf | Havia um cervo na beira da floresta. | Un cerf se tenait à la lisière de la forêt.
o chifre | la corne | O touro perdeu um chifre. | Le taureau a perdu une corne.
a cobra | le serpent | A cobra move-se sem barulho pela grama. | Le serpent se déplace silencieusement dans l'herbe. | g?
a coleta de lixo | le ramassage des ordures | A coleta de lixo passa na terça. | Le ramassage des ordures a lieu le mardi. | g? | pl=coletas de lixo
o colete | le gilet | Ele sempre usa um colete refletivo. | Il porte toujours un gilet réfléchissant.
a colheita | la récolte | A colheita foi boa este ano. | La récolte a été bonne cette année.
o combustível | le carburant | O combustível subiu outra vez. | Le carburant a encore augmenté. | pl=combustíveis
o cometa | la comète | O cometa é visto a cada setenta anos. | La comète se voit tous les soixante-dix ans.
a consciência ambiental | la conscience environnementale | A consciência ambiental da população cresce sem parar. | La conscience environnementale de la population augmente constamment. | g? | pl=consciências ambientais
o continente | le continent | A África é o segundo maior continente. | L'Afrique est le deuxième continent le plus grand.
o cultivo | la culture | O cultivo da oliveira exige paciência. | La culture de l'olivier exige de la patience.
o desmatamento | la déforestation | O desmatamento avança a cada ano. | La déforestation avance chaque année.
o desperdício | le gaspillage | O desperdício de comida é enorme. | Le gaspillage alimentaire est énorme.
o eclipse | l'éclipse | O eclipse foi visto em todo o país. | L'éclipse s'est vue dans tout le pays.
o ecossistema | l'écosystème | O ecossistema da floresta é frágil. | L'écosystème de la forêt est fragile.
a eletricidade | l'électricité | A eletricidade subiu vinte por cento. | L'électricité a augmenté de vingt pour cent.
a emissão | l'émission | As emissões caíram cinco por cento. | Les émissions ont baissé de cinq pour cent. | pl=emissões
a escassez | la pénurie | Houve escassez de água em agosto. | Il y a eu une pénurie d'eau en août.
a espécie animal | l'espèce animale | Esta espécie animal está ameaçada de extinção. | Cette espèce animale est menacée d'extinction. | pl=espécies animais
o farol | le phare | O farol é visto do porto. | Le phare se voit depuis le port.
a fila | la file, le rang | Há fila de carros desde a saída dez. | Il y a une file depuis la sortie dix.
o frasco | le flacon | Guarde os temperos em frascos. | Garde les épices dans des bocaux.
""",
"natureza_b1_pt_2": """
o gabinete | le bureau |  |  | ex=?
o gado | le bétail | O gado passa o verão na montanha. | Le bétail passe l'été dans la montagne.
a gaiola | la cage | O pássaro saiu da gaiola. | L'oiseau est sorti de la cage.
a galáxia | la galaxie | A nossa galáxia tem milhões de estrelas. | Notre galaxie a des millions d'étoiles.
a geada | le gel | Com geada a água do balde fica congelada. | Par temps de gel, l'eau reste gelée dans le seau. | g?
a gravidade | la gravité | A gravidade da Lua é menor. | La gravité de la Lune est plus faible.
o gás de escapamento | le gaz d'échappement | Os gases de escapamento são prejudiciais ao meio ambiente. | Les gaz d'échappement sont nocifs pour l'environnement. | g? | pl=gases de escapamento
o hipopótamo | l'hippopotame | O hipopótamo está deitado na água. | L'hippopotame est couché dans l'eau.
a horta | le potager | Ele tem tomates na horta. | Il a des tomates dans son potager.
a humidade | l'humidité | A humidade do ar está alta hoje. | L'humidité de l'air est élevée aujourd'hui.
o inseto | l'insecte | No verão há muitos insetos no jardim. | En été, il y a beaucoup d'insectes dans le jardin.
a inundação | l'inondation | A cidade sofreu uma grande inundação. | La ville a subi une grande inondation. | pl=inundações
a irrigação | l'irrigation | A irrigação por gotejamento economiza água. | L'irrigation goutte à goutte économise l'eau. | pl=irrigações
a laje | la dalle | Levantaram uma lajota do chão. | Ils ont soulevé une dalle du sol. | ex?
a lavoura | le champ | O agricultor trabalha na lavoura. | Le fermier travaille dans le champ.
o lixo volumoso | les encombrants |  |  | pl=lixos volumosos | ex=?
o Mar do Norte | la mer du Nord | A zona de baixa pressão está a passar pelo Mar do Norte. | La dépression passe au-dessus de la mer du Nord. | pl=Mares do Norte
a maré | la marée | A maré sobe muito rápido aqui. | La marée monte très vite ici.
a maré alta | la marée haute, l'inondation | A maré alta chega por volta das seis. | La marée haute arrive vers six heures. | g? | pl=marés altas
a membrana | la membrane | A membrana protege o interior. | La membrane protège l'intérieur.
o moinho | le moulin | Resta um moinho de vento na colina. | Il reste un moulin à vent sur la colline.
o mosquito | le moustique | O mosquito picou-me na perna. | Le moustique m'a piqué à la jambe.
o nó | le nœud | Dê um nó duplo. | Fais un double nœud.
o oceano | l'océan | O oceano separa os dois países. | L'océan sépare les deux pays.
o painel | le panneau | Instalaram painéis no telhado. | Ils ont installé des panneaux sur le toit. | pl=painéis
o parque zoológico | le parc animalier | No domingo vamos ao parque zoológico com as crianças. | Dimanche, nous visitons le parc animalier avec les enfants. | pl=parques zoológicos
o pastor | le berger | O pastor conhece cada ovelha. | Le berger connaît chaque mouton.
a pecuária | l'élevage | A pecuária é a atividade principal. | L'élevage est l'activité principale.
a pegada | l'empreinte | Reduzimos a pegada de carbono. | Nous réduisons l'empreinte carbone.
o penhasco | la falaise | A trilha margeia o penhasco. | Le sentier longe la falaise.
a península | la péninsule | A península tem três climas. | La péninsule a trois climats.
o petróleo | le pétrole | O preço do petróleo muda todo dia. | Le prix du pétrole change chaque jour.
o pinguim | le manchot, pingouin | No zoológico há seis pinguins. | Au zoo, il y a six manchots. | g?
a pista | la piste | A pista está molhada. | La piste est mouillée.
o planalto | le plateau | O planalto é seco e frio no inverno. | Le plateau est sec et froid en hiver.
a planície | la plaine | A planície estende-se até o horizonte. | La plaine s'étend jusqu'à l'horizon.
a poluição ambiental | la pollution de l'environnement | A poluição na cidade está a aumentar. | La pollution environnementale augmente en ville. | g? | pl=poluições ambientais | ex?
a potência | la puissance | A potência do motor é alta. | La puissance du moteur est élevée.
a poça | la flaque | As crianças pulam nas poças. | Les enfants sautent dans les flaques.
o poço | le puits | O poço está seco desde julho. | Le puits est à sec depuis juillet.
""",
"natureza_b1_pt_3": """
a praga | le fléau, l'infestation | Uma praga arruinou a colheita. | Une infestation a ruiné la récolte.
o predador | le prédateur | O leão é um predador perigoso. | Le lion est un prédateur dangereux.
a pressão atmosférica | la pression atmosphérique | A pressão atmosférica cai antes de uma tempestade. | La pression atmosphérique baisse avant une tempête. | g? | pl=pressões atmosféricas
a previsão | la prévision | A previsão para amanhã está boa. | La prévision pour demain semble bonne. | g? | pl=previsões
a proteção ambiental | la protection de l'environnement | A proteção ambiental é um tema importante para os jovens. | La protection de l'environnement est un sujet important pour les jeunes. | g? | pl=proteções ambientais
a proteção do clima | la protection du climat | A proteção do clima está na agenda política. | La protection du climat figure à l'agenda politique. | g? | pl=proteções do clima
o pulso | le poignet, la poupée | O meu pulso dói de tanto escrever. | J'ai mal au poignet à force d'écrire.
o pátio | la cour, ferme | As crianças brincam no pátio. | Les enfants jouent dans la cour.
a quinta | la ferme | O porco vive na quinta. | Le cochon vit à la ferme.
o raiz | la racine | Vamos atacar o problema pela raiz. | Nous attaquerons le problème à la racine. | g?
o reaproveitamento | recyclage | O reaproveitamento do plástico ajuda o meio ambiente. | Le recyclage du plastique aide l'environnement.
o rebanho | le troupeau | A manada segue em frente em busca de comida. | Le troupeau continue sa route à la recherche de nourriture. | ex?
o recurso | la ressource | A água é um recurso limitado. | L'eau est une ressource limitée.
a região | la région, coin | A região é muito tranquila. | Le coin est très calme. | g? | pl=regiões
a reserva natural | la réserve naturelle | Esta reserva natural abriga aves raras. | Cette réserve naturelle abrite des oiseaux rares. | pl=reservas naturais
o satélite | le satellite | O satélite envia dados a cada hora. | Le satellite envoie des données chaque heure.
a selva | la forêt tropicale | A selva cobre grande parte do país. | La forêt couvre une grande partie du pays.
a serra | le massif montagneux | Na serra ainda tem neve. | Il y a encore de la neige en montagne.
o sino | la cloche | O sino toca a cada hora. | La cloche sonne chaque heure.
a sombra | l'ombre | Vamos sentar na sombra. | Asseyons-nous à l'ombre.
a sustentabilidade | la durabilité | A sustentabilidade custa mais no início. | La durabilité coûte plus cher au début.
o telescópio | le télescope | O telescópio fica na montanha. | Le télescope est dans la montagne.
o terremoto | le tremblement de terre | O terremoto durou trinta segundos. | Le tremblement de terre a duré trente secondes.
a toupeira | la taupe | Uma toupeira revirou o jardim. | Une taupe a retourné le jardin.
o trator | le tracteur | O trator está no campo. | Le tracteur est dans le champ.
a turbina | la turbine | A turbina gira com o vento. | La turbine tourne avec le vent.
o túnel | le tunnel | O túnel tem três quilómetros. | Le tunnel fait trois kilomètres. | pl=túneis
a usina | la centrale | A usina produz energia para a região. | La centrale produit l'énergie de la région.
o vaga-lume | la luciole | Em junho dá para ver vaga-lumes aqui. | En juin, on voit des lucioles ici. | g? | pl=vagas-lumes | ex?
o vagão | le wagon | O nosso vagão é o número quatro. | Notre wagon est le numéro quatre. | pl=vagões
a vegetação | la végétation | A vegetação muda com a altitude. | La végétation change avec l'altitude. | g? | pl=vegetações
o veneno | le poison | Algumas plantas têm um veneno forte. | Certaines plantes contiennent un poison puissant.
o vinhedo | le vignoble | Os vinhedos cobrem toda a encosta. | Les vignobles couvrent tout le coteau.
a volta | le tour, la monnaie | Vamos dar uma volta. | Allons faire un tour.
a órbita | l'orbite | O satélite está em órbita desde 2019. | Le satellite est en orbite depuis 2019.
""",
"viagens_b1_pt": """
o abrigo de Autocarro | l'abribus | Esperamos o Autocarro sob o abrigo. | Nous attendons le bus sous l'abribus. | pl=abrigos de Autocarro | ex?
o acampamento | le camp | Em julho as crianças vão para o acampamento. | Les enfants partent en camp en juillet.
o acidente de trânsito | l'accident de la route | O acidente de trânsito causou um grande estrago. | L'accident de la route a causé de gros dégâts. | pl=acidentes de trânsito
o albergue | l'auberge | Dormimos em um albergue do caminho. | Nous dormons dans une auberge du chemin.
o albergue da juventude | l'auberge de jeunesse | No albergue a noite custa vinte euros. | À l'auberge de jeunesse, la nuit coûte vingt euros. | pl=albergues da juventude | ex?
a autoescola | l'auto-école | A autoescola custa dois mil euros. | L'auto-école coûte deux mille euros. | g?
a aventura | l'aventure | A viagem foi uma aventura. | Le voyage a été une aventure.
o aviso | l'annonce (haut-parleur) | O aviso estava difícil de entender. | L'annonce était difficile à comprendre.
a baldeação | la correspondance | É preciso de fazer baldeação em Sol. | Il faut faire une correspondance à Sol. | pl=baldeações
a balsa | le ferry, bac | A balsa sai de hora em hora. | Le ferry part toutes les heures. | g?
a bicicleta elétrica | le vélo électrique | Com a bicicleta elétrica eu subo até a montanha. | Avec le vélo électrique, j'arrive même à monter la côte. | g? | pl=bicicletas elétricas
o bicicletário | le support à vélos | Deixo a bicicleta no bicicletário. | Je laisse mon vélo au support à vélos.
o bilhete diário | le billet journalier | Para o torneio também há bilhetes de um dia. | Il y a aussi des billets journaliers pour le tournoi. | g? | pl=bilhetes diários | ex?
a bomba de ar | la pompe à vélo |  |  | pl=bombas de ar | ex=?
o carro compartilhado | l'autopartage | O carro compartilhado é muito popular na cidade. | L'autopartage est très populaire en ville. | pl=carros compartilhados
o carro de passeio | la voiture particulière | De carro leva duas horas. | En voiture, il faut deux heures. | pl=carros de passeio | ex?
o choque cultural | le choc culturel | O choque cultural foi bem forte no começo. | Le choc culturel était assez fort au début. | pl=choques culturais
a ciclista | le cycliste | Ciclistas, por favor, usem o caminho da direita. | Les cyclistes empruntent la piste de droite. | g?
o comboio metropolitano | le train de banlieue | De comboio metropolitano eu chego em vinte minutos. | Avec le train de banlieue, j'y suis en vingt minutes. | pl=comboios metropolitanos
o cume | le sommet | Chegamos ao cume ao meio-dia. | Nous arrivons au sommet à midi.
a curva | le virage, courbe | Vai devagar, a curva é fechada. | Roule doucement, le virage est serré. | g?
o diesel | le gazole, diesel | O diesel é mais barato que a gasolina. | Le gazole est moins cher que l'essence. | pl=dieséis
a estação central | la gare centrale |  |  | pl=estações centrais | ex=?
a faixa | la voie | Fique na faixa da direita, por favor. | Reste sur la voie de droite, s'il te plaît.
a ferrovia | le chemin de fer | O meu avô trabalhou na ferrovia. | Mon grand-père a travaillé aux chemins de fer.
a fila de carros | la file de voitures | Há fila de carros desde a saída dez. | Il y a une file depuis la sortie dix. | pl=filas de carros
o furgão | la camionnette de livraison | O furgão entra na rua lateral. | La camionnette tourne dans la rue latérale. | pl=furgões
o guia de viagem | la guide de voyage | O guia conhece muito bem a cidade. | Le guide de voyage connaît très bien la ville. | pl=guias de viagem | ex?
o guidão | le guidon | Ele segura firme o guidão da bicicleta. | Il se tient fermement au guidon du vélo. | pl=guidões
a infração | l'infraction | Ele cometeu uma infração leve. | Il a commis une infraction légère. | pl=infrações
o limite de velocidade | la limitation de vitesse | Aqui o limite de velocidade é 30. | Ici, la vitesse est limitée à 30. | pl=limites de velocidade
o luz traseira | le feu arrière |  |  | g? | pl=luzes traseiras | ex=?
a meia pensão | la demi-pension | Reservamos o hotel com meia pensão. | Nous réservons l'hôtel en demi-pension. | g? | pl=meias pensões
o meio de transporte | le moyen de transport | Eu só ando de transporte público. | Je ne me déplace qu'en transports en commun. | pl=meios de transporte | ex?
o mirante | le belvédère | Do mirante vê-se todo o vale. | Du belvédère on voit toute la vallée.
a mobilidade | la mobilité | A mobilidade urbana melhorou com o elétrico. | La mobilité urbaine s'est améliorée avec le tramway.
o morador local | l'habitant local, autochtone | Os moradores locais conhecem as praias mais bonitas. | Les habitants locaux connaissent les plus belles plages. | pl=moradores locais
a operadora de turismo | voyagiste | A operadora oferece pacotes de viagem baratos. | Le voyagiste propose des voyages organisés à prix abordable. | g? | pl=operadoras de turismo | ex?
o parquímetro | le parcmètre | Pago no parquímetro. | Je paie au parcmètre.
o passe anual | l'abonnement annuel | Com o passe anual eu economizo muito. | Avec l'abonnement annuel, j'économise beaucoup. | pl=passes anuais
""",
"viagens_b1_pt_2": """
o passeio turístico | le circuit, tour | O passeio dura duas horas. | Le circuit dure deux heures. | pl=passeios turísticos | ex?
a peça de reposição | la pièce de rechange | Para esta bicicleta velha quase não se acham peças de reposição. | On trouve difficilement des pièces de rechange pour ce vieux vélo. | g? | pl=peças de reposição
a placa de trânsito | le panneau de signalisation | Não conheço esta placa de trânsito. | Je ne connais pas ce panneau. | pl=placas de trânsito
o ponto turístico | le site touristique | Este ponto turístico não pode ficar de fora. | Il ne faut pas manquer ce site touristique. | pl=pontos turísticos
o porta-malas | le coffre (de voiture) | As malas estão no porta-malas. | Les valises sont dans le coffre. | g? | pl=portas-malas
a portagem | le péage |  |  | ex=?
a pousada | la pension (hébergement) ; retraite | Hospedei-me numa pousada muito limpa. | J'ai logé dans une auberge très propre.
o pouso | l'atterrissage | O pouso foi bem tranquilo. | L'atterrissage a été très doux.
o refúgio | le refuge | Passamos a noite no refúgio. | Nous passons la nuit au refuge.
a rua de mão única | la rue à sens unique | Cuidado, esta rua é de mão única! | Attention, c'est une rue à sens unique ! | pl=ruas de mão única | ex?
a ruína | la ruine | Visitamos umas ruínas romanas. | Nous visitons des ruines romaines.
a saída | la sortie (d'autoroute) | Pegue a próxima saída. | Prenez la prochaine sortie. | g?
a sobretaxa | le supplément | Por causa da doença preexistente houve uma sobretaxa de risco. | En raison de l'antécédent, il y a eu une surprime.
a tarifa | le tarif | A tarifa reduzida é para estudantes. | Le tarif réduit est pour les étudiants.
a temporada | la saison | Na alta temporada tudo custa o dobro. | En haute saison tout coûte le double.
o trajeto | le trajet | O trajeto dura quarenta minutos. | Le trajet dure quarante minutes.
o transporte | le transport | O transporte dos móveis leva dois dias. | Le transport des meubles dure deux jours.
o travão | le frein | O travão da bicicleta não funciona. | Le frein du vélo ne fonctionne pas. | pl=travões
o trecho | le trajet, parcours | Lê o segundo trecho, por favor. | Lis le deuxième passage, s'il te plaît.
a trilha | le sentier | A trilha sobe durante duas horas. | Le sentier monte pendant deux heures.
o turismo | le tourisme | O turismo dá trabalho a meia ilha. | Le tourisme fait vivre la moitié de l'île.
o vagão-restaurante | le wagon-restaurant | O vagão-restaurante é o quarto vagão. | Le wagon-restaurant est en quatrième voiture. | g? | pl=vagões-restaurantes
a velocidade | la vitesse | A velocidade estava alta demais. | La vitesse était beaucoup trop élevée. | g?
o veículo | le véhicule | Este veículo gasta pouca gasolina. | Ce véhicule consomme peu d'essence.
o veículo automotor | le véhicule à moteur | Para um veículo automotor é preciso de ter seguro. | Il faut une assurance pour le véhicule à moteur. | pl=veículos automotores
a viagem de volta | le trajet de retour | A viagem de volta demora mais. | Le trajet de retour dure plus longtemps. | g? | pl=viagens de volta
a vivência | l'expérience vécue | A viagem foi uma experiência bonita. | Le voyage a été une belle expérience. | g? | ex?
a âncora | l'ancre | O navio lança âncora no porto. | Le navire jette l'ancre dans le port. | g?
""",
"cidade_b1_pt": """
a abóbada | la voûte | A abóbada da igreja é gótica. | La voûte de l'église est gothique.
o achados e perdidos | le bureau des objets trouvés | Pergunta pela tua chave nos achados e perdidos. | Demande ta clé au bureau des objets trouvés. | g? | pl=achados e perdidos
o andaime | l'échafaudage | O andaime cobre toda a fachada. | L'échafaudage couvre toute la façade.
o arquiteto | l'architecte | O arquiteto apresentou o projeto. | L'architecte a présenté le projet.
a arquitetura | l'architecture | A arquitetura do bairro é do século dezenove. | L'architecture du quartier date du dix-neuvième siècle.
o centro da cidade | le centre-ville | A igreja fica no centro da cidade. | L'église est au centre-ville. | pl=centros da cidade
a cidade grande | grande ville | Lisboa é uma cidade grande muito animada. | Lisbonne est une grande ville très animée. | pl=cidades grandes
a cidade portuária | la ville portuaire | Porto é a maior cidade portuária do país. | Porto est la plus grande ville portuaire du pays. | pl=cidades portuárias
a coluna | la colonne | A coluna é de pedra branca. | La colonne est en pierre blanche.
o concreto | le béton | O concreto leva um mês para secar. | Le béton met un mois à sécher.
o conjunto residencial | le lotissement | Neste conjunto residencial moram muitas famílias jovens. | De nombreuses jeunes familles vivent dans ce lotissement. | pl=conjuntos residenciais
a construção | la construction, chantier | A construção da escola leva dois anos. | La construction de l'école dure deux ans. | g? | pl=construções
os corpo de bombeiros | les pompiers | Os bombeiros chegaram em cinco minutos. | Les pompiers sont arrivés en cinq minutes. | ex?
o crescimento | la croissance | O crescimento da cidade foi rápido. | La croissance de la ville a été rapide.
a densidade | la densité | A densidade populacional é alta. | La densité de population est élevée.
a drogaria | la droguerie, parapharmacie | Pasta de dentes eu compro na drogaria. | J'achète le dentifrice à la droguerie.
o espaço | l'espace | Faltam espaços verdes no centro. | Il manque des espaces verts au centre.
a estrutura | la structure | A estrutura é de concreto. | La structure est en béton.
a fachada | la façade | A fachada foi restaurada em 2020. | La façade a été restaurée en 2020.
o guarda-volumes | le vestiaire | Os casacos ficam na chapelaria. | Les manteaux restent au vestiaire. | g? | pl=guardas-volumes | ex?
a infraestrutura | l'infrastructure | A infraestrutura do porto é antiga. | L'infrastructure du port est ancienne.
a livraria | la librairie | Na livraria também há cartões. | À la librairie, il y a aussi des cartes.
a mesquita | la mosquée | A nova mesquita foi inaugurada no ano passado. | La nouvelle mosquée a été inaugurée l'année dernière.
a metrópole | la métropole | Tóquio é uma das maiores metrópoles do mundo. | Tokyo est l'une des plus grandes métropoles du monde. | g?
a metrópole mundial | la métropole mondiale | Paris é considerada uma verdadeira metrópole mundial. | Paris est considérée comme une véritable métropole mondiale. | g? | pl=metrópoles mundiais
o município | la commune, municipalité | O município organiza uma festa de verão todo ano. | La commune organise une fête d'été chaque année.
o objeto achado | l'objet trouvé | Os objetos achados estão no escritório ao lado. | Les objets trouvés sont dans le bureau d'à côté. | pl=objetos achados
o parquinho | l'aire de jeux | O parquinho fica logo ali na esquina. | L'aire de jeux est juste au coin.
a periferia | la périphérie | Ele mora na periferia de Aveiro. | Il habite la périphérie de Aveiro.
o ponto central | le centre, point central | A praça do mercado é o ponto central do centro histórico. | La place du marché est le centre de la vieille ville. | pl=pontos centrais
a proximidade | la proximité |  |  | ex=?
o prédio industrial | le bâtiment industriel | O antigo prédio industrial foi transformado em apartamentos. | L'ancien bâtiment industriel a été transformé en appartements. | g? | pl=prédios industriais
a restauração | la restauration | A restauração durou três anos. | La restauration a duré trois ans. | pl=restaurações
a rua lateral | la rue latérale | O correio fica numa rua lateral. | La poste est dans une rue latérale. | pl=ruas laterais
a rua transversal | la rue transversale | Pegue a segunda transversal à direita. | Prenez la deuxième rue transversale à droite. | g? | pl=ruas transversais | ex?
o salão | la salle (grande) | A conferência acontece no salão grande. | La conférence a lieu dans la grande salle. | pl=salões
a saída de emergência | la sortie de secours | A saída de emergência fica no fundo, à esquerda. | La sortie de secours est au fond à gauche. | g? | pl=saídas de emergência
a secretaria de obras | le service de l'urbanisme | A secretaria de obras aprova o novo projeto de construção. | Le service de l'urbanisme approuve le nouveau plan de construction. | g? | pl=secretarias de obras
o subúrbio | la banlieue | Ele cresceu em um subúrbio de Lisboa. | Il a grandi dans une banlieue de Lisboa.
o terreno | le terrain à bâtir | Eles compraram um terreno nos arredores. | Ils ont acheté un terrain en périphérie.
o urbanismo | l'urbanisme | O urbanismo dos anos sessenta é visível. | L'urbanisme des années soixante se voit.
a zona | la zone | É uma zona de peões desde março. | C'est une zone piétonne depuis mars.
a zona industrial | la zone industrielle | A fábrica fica na zona industrial, na periferia. | L'usine se trouve dans la zone industrielle en périphérie. | pl=zonas industriais
""",
"escola_b1_pt": """
o alfabeto | l'alphabet | O alfabeto alemão tem 26 letras. | L'alphabet allemand a 26 lettres.
a amostra | l'échantillon | Analisam a amostra no laboratório. | Ils analysent l'échantillon au laboratoire.
o aprendiz | l'apprenant | A empresa está a procurar dois aprendizes. | L'entreprise cherche deux apprentis. | g?
a biologia | la biologie | Biologia era a minha matéria preferida. | La biologie était ma matière préférée. | g?
o boletim | bulletin | O boletim dele foi muito bom este ano. | Son bulletin était très bon cette année.
o caderno escolar | le cahier d'école | Ele esqueceu o caderno em casa. | Il a oublié son cahier d'école à la maison. | pl=cadernos escolares | ex?
a caneta esferográfica | le stylo à bille | Preencha o formulário com caneta esferográfica. | Remplissez le formulaire au stylo à bille. | g? | pl=canetas esferográficas
o certificado | le diplôme, certificat | No fim, cada participante recebe um certificado. | Chaque participant reçoit un certificat à la fin.
o cientista | le scientifique | O cientista publicou o seu estudo. | Le scientifique a publié son étude.
a ciência | la science | A ciência avança devagar, mas avança. | La science avance lentement mais avance.
o colega de turma | camarade de classe | O meu colega de turma ajuda-me com a lição de casa. | Mon camarade de classe m'aide avec mes devoirs. | pl=colegas de turma
os conhecimentos de línguas | les connaissances linguistiques | Para esta vaga são exigidos bons conhecimentos de línguas. | De bonnes connaissances linguistiques sont requises pour ce poste. | g?
o conselho de pais | le conseil des parents d'élèves | Ela faz parte do conselho de pais da escola. | Elle est au conseil des parents de l'école. | pl=conselhos de pais
o curso intensivo | le cours intensif | No verão vou fazer um curso intensivo. | Cet été, je suis un cours intensif. | pl=cursos intensivos
a célula | la cellule | A célula divide-se todos os dias. | La cellule se divise chaque jour.
a definição | définition | A definição deste termo não é bem clara. | La définition de ce terme n'est pas tout à fait claire. | g? | pl=definições
a descoberta | la découverte | Foi a descoberta do século. | Ce fut la découverte du siècle.
a descrição | la description | Sem uma descrição precisa eu não acho a casa. | Sans description précise, je ne trouve pas la maison. | pl=descrições
o dialeto | le dialecte | Nesta região muita gente fala um dialeto forte. | Dans cette région, beaucoup de gens parlent un dialecte prononcé.
o diploma de língua | le diplôme de langue | Para a vaga é preciso um diploma de língua. | Pour ce poste, il faut un diplôme de langue. | pl=diplomas de língua
o diálogo | le dialogue | Leiam o diálogo em dupla. | Lisez le dialogue à deux.
a educação | l'éducation | A educação pública é gratuita. | L'éducation publique est gratuite. | pl=educações
a enciclopédia | l'encyclopédie, lexique | Antigamente havia uma enciclopédia em toda casa. | Autrefois, il y avait une encyclopédie dans chaque maison.
a escola integrada | l'école polyvalente | O meu filho estuda numa escola integrada. | Mon fils va dans une école polyvalente. | pl=escolas integradas
a escola primária | l'école primaire | A minha filha está na escola primária desde agosto. | Ma fille va à l'école primaire depuis août. | pl=escolas primárias
a escola secundária | l'école secondaire | Depois da escola primária vem a secundária. | Après l'école primaire vient l'école secondaire. | pl=escolas secundárias | ex?
a escolaridade | scolarité, instruction | Ele teve uma escolaridade muito boa. | Il a bénéficié d'une très bonne scolarité.
a espécie | l'espèce | É uma espécie protegida. | C'est une espèce protégée.
o estudo | l'étude | O estudo durou cinco anos. | L'étude a duré cinq ans.
o exercício | l'exercice | Façam o exercício da página doze, por favor. | Faites l'exercice de la page douze.
a exigência | l'exigence | A exigência do curso é alta. | L'exigence du cours est élevée.
o experimento | l'expérience | O experimento deu errado três vezes. | L'expérience a raté trois fois.
o filme plástico | le film plastique, feuille | Cobre a salada com filme plástico. | Couvre la salade avec du film plastique. | g? | pl=filmes plásticos
a filosofia | la philosophie | Ele estuda filosofia e história. | Il étudie la philosophie et l'histoire. | g?
o foco | le point fort, priorité | O foco do curso está na gramática. | Le cours met l'accent sur la grammaire.
a folha de respostas | la feuille de réponses | Escreva tudo na folha de respostas. | Écrivez tout sur la feuille de réponses. | pl=folhas de respostas
o folheto informativo | la fiche d'information | No folheto informativo estão todas as regras importantes. | La fiche d'information contient toutes les règles importantes. | pl=folhetos informativos
a formação | la formation | Ele recebeu formação na empresa. | Il a reçu une formation dans l'entreprise. | pl=formações
o fracasso | l'échec | O fracasso escolar preocupa os professores. | L'échec scolaire inquiète les professeurs.
a física | la physique | Em física eu sempre tirava nota boa. | En physique, j'avais toujours un bon résultat. | g?
""",
"escola_b1_pt_2": """
a geografia | la géographie |  |  | g? | ex=?
o Gymnasium | le lycée | Depois da escola primária ela vai para o Gymnasium. | Après le primaire, elle va au lycée.
a habilidade | l'aptitude | Ele tem habilidade para idiomas. | Il a des aptitudes pour les langues.
a Hauptschule | l'école secondaire (filière générale) | Ele terminou a Hauptschule com boas notas. | Il a terminé l'école secondaire avec de bonnes notes. | g?
a hipótese | l'hypothèse | A hipótese não se confirmou. | L'hypothèse ne s'est pas confirmée.
o instituto | l'institut | Ela faz pesquisa num instituto em Porto. | Elle fait de la recherche dans un institut à Porto.
a inteligência | l'intelligence | Só inteligência não basta. | L'intelligence seule ne suffit pas. | g?
a introdução | l'introduction | No primeiro dia tem uma breve introdução. | Le premier jour, il y a une courte introduction. | g? | pl=introduções
o laboratório | le laboratoire | Ele trabalha em um laboratório de Aveiro. | Il travaille dans un laboratoire de Aveiro.
a língua estrangeira | la langue étrangère | O alemão é a minha segunda língua estrangeira. | L'allemand est ma deuxième langue étrangère. | g? | pl=línguas estrangeiras
a língua materna | la langue maternelle | A minha língua materna é o turco. | Ma langue maternelle est le turc. | pl=línguas maternas
a matemática | les maths | Em matemática eu nunca fui bom. | En maths, je n'ai jamais été bon. | g?
o material de apoio | l'outil, moyen auxiliaire | Na prova não é permitido nenhum material de apoio. | Aucun outil n'est autorisé à l'examen. | g? | pl=materiais de apoio
o método | la méthode | Eles usam um método muito prático. | Ils utilisent une méthode très pratique.
o módulo | le module | O primeiro módulo dura quatro semanas. | Le premier module dure quatre semaines.
o nível | le niveau | O nível de espanhol dele é intermediário. | Son niveau d'espagnol est intermédiaire. | pl=níveis
o orientador | l'encadrant | O meu orientador dá-me um retorno valioso. | Mon encadrant me donne des retours précieux.
o participante | le participant | O curso tem doze participantes. | Le cours compte douze participants. | g?
a participação | la participation | A participação no curso é gratuita. | La participation au cours est gratuite. | g? | pl=participações
o prefácio | la préface, avant-propos | O prefácio explica por que o livro foi escrito. | La préface explique pourquoi le livre a été écrit.
a preparação | la préparation | A preparação para a prova leva meses. | La préparation à l'examen dure des mois. | g? | pl=preparações
o programa de intercâmbio | le programme d'échange | Ela participa de um programa de intercâmbio na França. | Elle participe à un programme d'échange en France. | pl=programas de intercâmbio
a pronúncia | la prononciation | A tua pronúncia já está muito boa. | Ta prononciation est déjà très bonne.
a prova escrita | l'examen écrit | A prova escrita é semana que vem. | L'examen écrit aura lieu la semaine prochaine. | g? | pl=provas escritas
a química | la chimie | Na escola eu não gostava de química. | À l'école, je n'aimais pas la chimie. | g?
a recompensa | la récompense | Como recompensa o cão ganha um bolacha. | En récompense, le chien reçoit un biscuit. | g?
o reforço de língua | le soutien linguistique | A escola oferece reforço de língua extra. | L'école propose un soutien linguistique supplémentaire. | pl=reforços de língua
o repetir de ano | redoublement | Repetir de ano é uma grande preocupação para muitos alunos. | Le redoublement est une grande source d'inquiétude pour de nombreux élèves. | g? | pl=repetires de ano
o retorno | le retour, réponse | Ainda estou a esperar um retorno da repartição. | J'attends encore une réponse de l'administration.
a revisão | la révision, répétition | A revisão por pares levou um ano. | La relecture par les pairs a pris un an. | g? | pl=revisões
a segunda língua | la langue seconde |  |  | pl=segundas línguas | ex=?
o sistema | le système | O sistema educacional mudou em 2020. | Le système éducatif a changé en 2020.
o snack-bar | la cafétéria | Na estação tem uma snack-bar boa. | Il y a un bon snack à la gare. | g? | pl=snacks-bares
o sucesso | le succès | O projeto foi um sucesso. | Le projet a été un succès.
a tabela | le tableau, tableur | Os números estão na tabela abaixo. | Les chiffres figurent dans le tableau ci-dessous.
o termo genérico | le terme générique | «Móveis» é um termo genérico para mesa, cadeira e armário. | «Meuble» est un terme générique pour table, chaise et armoire. | pl=termos genéricos
o teste | le test | O teste dura uma hora. | Le test dure une heure.
o turco | le turc (la langue) | O meu colega é turco. | Mon collègue est turc.
a tutoria | le suivi, le tutorat | A tutoria é às terças. | Le tutorat est le mardi.
o ucraniano | l'ukrainien (la langue) | Ela fala ucraniano e russo. | Elle parle ukrainien et russe.
o universo | l'univers | O universo está em expansão. | L'univers est en expansion.
a Volkshochschule | l'université populaire | Eu aprendo alemão na Volkshochschule. | J'apprends l'allemand à l'université populaire.
""",
"cultura_b1_pt": """
a abertura da exposição | vernissage | A abertura da exposição teve muito público. | Le vernissage a attiré beaucoup de monde. | g? | pl=aberturas da exposição
a atividade de lazer | l'activité de loisir | Pintar é a minha atividade de lazer favorita. | La peinture est mon activité de loisir préférée. | pl=atividades de lazer
o balé | le ballet | A minha filha dança balé há cinco anos. | Ma fille fait du ballet depuis cinq ans. | g?
o banquete | le repas de fête | No Natal lá em casa tem uma grande ceia. | À Noël, nous avons un grand repas de fête. | g? | ex?
a biografia | la biographie | A biografia tem seiscentas páginas. | La biographie fait six cents pages.
a boneca | la poupée | A minha filha dorme com a boneca. | Ma fille dort avec sa poupée. | g?
o calendário de feriados | le calendrier des fêtes | O calendário de feriados está pendurado na cozinha. | Le calendrier des fêtes est accroché dans la cuisine. | pl=calendários de feriados
o capítulo | le chapitre | O capítulo três é o melhor. | Le chapitre trois est le meilleur.
a cerimónia de casamento | la cérémonie de mariage | A cerimónia é às onze horas. | La cérémonie de mariage est à onze heures. | g? | pl=cerimónias de casamento | ex?
a civilização | la civilisation | Ele estuda as civilizações antigas. | Il étudie les civilisations anciennes. | pl=civilizações
o compasso | la mesure (musique) | Toca os primeiros oito compassos de novo. | Rejoue les huit premières mesures.
o compositor | le compositeur | Beethoven é um compositor famoso. | Beethoven est un compositeur célèbre.
a compositora | la compositrice | A compositora está a escrever a trilha do filme novo. | La compositrice écrit la musique du nouveau film. | g?
o conto | le conte | Ela lia-nos um conto toda noite. | Elle nous lisait un conte chaque soir.
o conto de fadas | le conte | À noite eu leio um conto de fadas para as crianças. | Le soir, je lis un conte aux enfants. | pl=contos de fadas
a crença | la croyance | Ele respeita as crenças dos outros. | Il respecte les croyances des autres.
a cruz | la croix | No alto da montanha há uma cruz. | Il y a une croix sur la montagne.
a crítica | la critique | A crítica foi muito dura. | La critique a été très dure.
a cultura | la culture | A cultura do país fascina-me. | La culture du pays me fascine.
o descanso | la détente, récupération | Depois da competição o corredor precisa de descanso. | Après la compétition, le coureur a besoin de récupération.
o diabo | le diable | Na história aparece um diabo. | Dans l'histoire, il y a un diable.
a discoteca | la discothèque |  |  | g? | ex=?
a diversidade | la diversité | A diversidade enriquece a cidade. | La diversité enrichit la ville.
a diversão | le plaisir, amusement | O parque de diversões abriu novas montanhas-russas. | Le parc d'attractions a inauguré de nouvelles montagnes russes. | g? | pl=diversões
o enredo | l'intrigue, l'action | O enredo do filme é simples. | L'intrigue du film est simple.
o ensaio | l'essai | Ele publicou um ensaio sobre o clima. | Il a publié un essai sur le climat.
o entretenimento | le divertissement | É puro entretenimento. | C'est du pur divertissement.
a escola de música | l'école de musique | Ele dá aula de violão na escola de música. | Il enseigne la guitare à l'école de musique. | pl=escolas de música
o espetáculo | le spectacle | O espetáculo começa às nove. | Le spectacle commence à neuf heures.
o espírito | l'esprit, le fantôme | O filme capta com precisão o espírito da época. | Le film saisit exactement l'esprit du temps.
a fantasma | le fantôme | As crianças brincam de fantasma. | Les enfants jouent au fantôme. | g?
a felicitação | la félicitation | Os meus parabéns pelo emprego novo! | Mes félicitations pour le nouveau travail ! | pl=felicitações | ex?
o feriado nacional | la fête nationale | No feriado nacional as lojas ficam fechadas. | Le jour de la fête nationale, les magasins sont fermés. | pl=feriados nacionais
a flauta | la flûte | A minha irmã toca flauta. | Ma sœur joue de la flûte. | g?
o folclore | le folklore | O folclore do norte é muito vivo. | Le folklore du nord est très vivant.
a fotografia | la photographie | Fotografia é o maior hobby dele. | La photographie est son plus grand loisir. | g?
o herói | le héros | O herói do filme morre no final. | Le héros du film meurt à la fin.
a identidade | l'identité | A identidade constrói-se aos poucos. | L'identité se construit peu à peu.
o isqueiro | le briquet |  |  | ex=?
o jazz | le jazz | Na sexta uma banda vai tocar jazz. | Vendredi, un groupe joue du jazz. | g?
""",
"cultura_b1_pt_2": """
o leitor | le lecteur | O leitor descobre o final tarde. | Le lecteur découvre la fin tardivement.
a literatura | la littérature | Ele estuda literatura espanhola. | Il étudie la littérature espagnole.
a melodia | la mélodie | Conheço esta melodia desde criança. | Je connais cette mélodie depuis mon enfance.
o mito | le mythe | É um mito muito difundido. | C'est un mythe très répandu.
o ofício | l'artisanat/loisir manuel | No tempo livre ele está a aprender um novo ofício. | Il apprend un nouvel artisanat pendant son temps libre.
o original | l'original | Traga o original, por favor. | Apportez l'original, s'il vous plaît.
o palco | la scène | Ele subiu ao palco sem medo. | Il est monté sur scène sans peur.
os parabéns | les félicitations | Parabéns pela prova! | Toutes mes félicitations pour l'examen ! | g?
o parque de diversões | le parc d'attractions | O parque de diversões abriu novas montanhas-russas. | Le parc d'attractions a inauguré de nouvelles montagnes russes. | pl=parques de diversões
o parvo | le fou (du carnaval) | Foi um erro parvo. | Ce fut une erreur bête.
o passatempo | le passe-temps | O passatempo favorito dele é a pesca. | Son passe-temps préféré est la pêche.
o passatempo favorito | l'occupation préférée | Ler é o meu passatempo favorito no fim de semana. | La lecture est mon occupation préférée le week-end. | pl=passatempos favoritos
o património | le patrimoine | O centro histórico é património protegido. | La vieille ville est un patrimoine protégé.
o Pentecostes | la Pentecôte | No Pentecostes temos quatro dias de folga. | À la Pentecôte, nous avons quatre jours de congé. | pl=Pentecostes
a peça de colecionador | la pièce de collection | Este selo é uma peça de colecionador valiosa. | Ce timbre est une pièce de collection précieuse. | pl=peças de colecionador
a piada | la blague | Ele gosta de contar piadas nas festas. | Il aime raconter des blagues dans les fêtes. | g?
o piquenique | le pique-nique |  |  | ex=?
a poesia | la poésie | Poesia não se lê depressa. | La poésie ne se lit pas vite.
o ponto de encontro | le point de rencontre | O ponto de encontro é em frente ao cinema. | Le point de rencontre est devant le cinéma. | pl=pontos de encontro
o som | la sonorité, le son | O som deste violino é quente. | La sonorité de ce violon est chaude.
o símbolo | le symbole | A pomba é um símbolo de paz. | La colombe est un symbole de paix.
a trama | l'intrigue | A trama complica-se no meio. | L'intrigue se complique au milieu.
o trompete | la trompette | Ele está a aprender trompete há dois anos. | Il apprend la trompette depuis deux ans. | g?
a turnê | la tournée | A turnê passa por dez cidades. | La tournée passe par dix villes.
o álbum de fotos | l'album photo | A minha avó gosta de mostrar o seu álbum de fotos antigo. | Ma grand-mère aime montrer son vieil album photo. | pl=álbuns de fotos
a ópera | l'opéra | No sábado vamos à ópera. | Samedi, nous allons à l'opéra.
""",
"desporto_b1_pt": """
o adepto | le supporter | Os adeptos lotaram o estádio. | Les supporters ont rempli le stade.
o arco | l'arc | Ele atira com arco e flecha. | Il tire à l'arc.
o atleta | le sportif, athlète | Os atletas treinam todo dia. | Les sportifs s'entraînent tous les jours.
o atleta profissional | le sportif professionnel | Um atleta profissional treina todo dia. | Un sportif professionnel s'entraîne tous les jours. | pl=atletas profissionais
o atletismo | l'athlétisme | O atletismo é um dos desportos mais antigos. | L'athlétisme est l'un des plus anciens sports.
o automobilismo | le sport automobile | Ele interessa-se muito por automobilismo. | Il s'intéresse beaucoup au sport automobile.
a bolsa de academia | le sac de sport | Esqueci a minha bolsa de academia no carro. | J'ai oublié mon sac de sport dans la voiture. | pl=bolsas de academia
a cabine | la cabine, vestiaire | O senhor pode experimentar a calça na cabine. | Vous pouvez essayer le pantalon en cabine.
o campeão mundial | le champion du monde | Ele foi campeão mundial duas vezes. | Il est devenu deux fois champion du monde. | pl=campeões mundiais
a classificação | le classement | Eles sobem duas posições na classificação. | Ils montent de deux places au classement. | pl=classificações
o condicionamento físico | la forme physique | Pelo condicionamento eu corro três vezes por semana. | Pour la forme, je cours trois fois par semaine. | pl=condicionamentos físicos | ex?
a Copa do Mundo | le championnat du monde | O campeonato mundial é na Ásia este ano. | Le championnat du monde a lieu en Asie cette année. | g? | pl=Copas do Mundo | ex?
a corredora | la coureuse | A corredora treina duas horas por dia. | La coureuse s'entraîne deux heures par jour. | g?
a corrida | la course | A corrida começa às nove horas. | La course commence à neuf heures. | g?
a defesa | le défenseur | O defesa joga com muita segurança. | Le défenseur joue très sûrement. | g?
a derrota | la défaite | Depois da derrota todos ficaram decepcionados. | Après la défaite, tout le monde était déçu.
o desempenho | la performance | O desempenho dele caiu depois da lesão. | Sa performance a baissé après la blessure.
a disciplina | la discipline | Eu criaria o cão com mais disciplina. | Moi, j'élèverais le chien avec plus de discipline.
a equipa de futebol | l'équipe de football |  |  | g? | pl=equipas de futebol | ex=?
a equipa do coração | le club préféré |  |  | g? | pl=equipas do coração | ex=?
o espectador | le spectateur | Havia vinte mil espectadores no estádio. | Il y avait vingt mille spectateurs au stade.
o esqui | le ski |  |  | g? | ex=?
o estádio | le stade | O estádio tem sessenta mil lugares. | Le stade a soixante mille places.
a ginástica | la gymnastique | De manhã eu faço dez minutos de ginástica. | Le matin, je fais dix minutes de gymnastique. | g?
a goleira | la gardienne de but | A goleira joga na seleção há cinco anos. | La gardienne de but joue dans l'équipe nationale depuis cinq ans. | g?
o golfe | le golf | No fim de semana ele joga golfe. | Le week-end, il joue au golf. | g?
o golpe | le coup | Com um golpe o jogo acabou. | En un coup, la partie était finie.
o guarda-redes | le gardien de but | O guarda-redes defende a última bola. | Le gardien de but arrête le dernier ballon. | g? | pl=guardas-redes
o júri | le jury | O júri avalia a apresentação de cada participante. | Le jury évalue la performance de chaque participant.
a lesão | la blessure | A lesão o deixou fora por um mês. | La blessure l'a écarté un mois. | pl=lesões
a modalidade desportiva | le type de sport | Natação é a minha modalidade preferida. | La natation est mon sport préféré. | pl=modalidades desportivas | ex?
o mountain bike | le vélo tout-terrain | De mountain bike dá para andar também na floresta. | Avec un VTT, on roule aussi en forêt. | g? | pl=mountains bikes
o organizador | l'organisateur | O organizador do torneio espera mil espectadores. | L'organisateur du tournoi attend mille spectateurs.
a organizadora | l'organisatrice | A organizadora cuida de todos os detalhes. | L'organisatrice s'occupe de tous les détails. | g?
o perdedor | le perdant | O perdedor também ganha uma medalha. | Le perdant reçoit aussi une médaille.
a piscina coberta | la piscine couverte |  |  | pl=piscinas cobertas | ex=?
a raquete de ténis | la raquette de tennis | A raquete de ténis dela já é bem velha. | Sa raquette de tennis est déjà très vieille. | g? | pl=raquetes de ténis
o recorde | le record | Ele bateu o recorde do clube. | Il a battu le record du club.
a resistência | l'endurance | Falta resistência a ele no segundo tempo. | Il manque d'endurance en deuxième mi-temps.
o vencedor | le vainqueur | O vencedor ganha uma taça grande. | Le vainqueur reçoit une grande coupe.
a vencedora | la gagnante | A vencedora está feliz com a medalha. | La gagnante est ravie de sa médaille. | g?
a vitória | la victoire | A vitória foi muito comemorada. | La victoire a été célébrée abondamment. | g?
""",
"media_b1_pt": """
o alcance | la portée | O alcance do vídeo surpreendeu a todos. | La portée de la vidéo a surpris tout le monde.
o algoritmo | l'algorithme | Este algoritmo ordena os dados em segundos. | Cet algorithme trie les données en quelques secondes.
a amostragem | l'échantillonnage | A amostragem foi feita em dez cidades. | L'échantillonnage s'est fait dans dix villes.
o aparelho de cd | le lecteur de CD | No carro ainda tenho um aparelho de CD. | Dans la voiture, j'ai encore un lecteur de CD. | pl=aparelhos de cd
a atualização | la mise à jour | A atualização leva dez minutos. | La mise à jour prend dix minutes. | pl=atualizações
a audiência | l'audience | A audiência do programa cresceu. | L'audience de l'émission a augmenté.
o avanço | l'avancée | É um avanço importante na medicina. | C'est une avancée importante en médecine.
o backup | la sauvegarde, le soutien | O backup é salvo toda noite. | La sauvegarde se fait chaque nuit.
o blog | le blogue | Ela escreve um blog sobre culinária. | Elle tient un blogue sur la cuisine.
o buscador | le moteur de recherche | Digito a pergunta no buscador. | J'écris la question dans le moteur de recherche.
a caixa postal do telemóvel | la messagerie mobile | A caixa postal está cheia. | La messagerie est pleine. | g? | pl=caixas postais do telemóvel | ex?
o CD-ROM | le cédérom | O livro vem com um CD-ROM. | Le livre est accompagné d'un cédérom. | g? | pl=CDs-ROMs
o chat | le clavardage, discussion en ligne | No chat todo mundo escreve bem curto. | Dans le clavardage, tout le monde écrit très court.
o clique | le clic | Com um clique está tudo salvo. | En un clic, tout est enregistré.
o comentário | le commentaire | Ele apagou o comentário na hora. | Il a effacé le commentaire aussitôt.
o comercial | le spot publicitaire | O comercial dura só vinte segundos. | Le spot ne dure que vingt secondes.
a comunicação | la communication | A comunicação na equipa funciona bem. | La communication dans l'équipe fonctionne bien. | g? | pl=comunicações
o concerto de calouros | le télécrochet | No sábado passa um reality de talentos. | Samedi, il y a un télécrochet. | pl=concertos de calouros | ex?
o conexão à internet | la connexion internet | Sem conexão à internet não consigo pagar on-line. | Sans connexion internet, je ne peux pas payer en ligne. | pl=conexões às internets
o conhecimentos de informática | les connaissances en informatique | Para esta vaga são necessários bons conhecimentos de informática. | De bonnes connaissances en informatique sont nécessaires pour ce poste. | g? | pl=conhecimentos de informática
o conteúdo | le contenu | Ele publica conteúdo todos os dias. | Il publie du contenu tous les jours.
a continuação | la suite (continuation) | A continuação do filme sai no ano que vem. | La suite du film sort l'année prochaine. | g? | pl=continuações
o código de área | l'indicatif téléphonique | O código de área de Lisboa é 030. | L'indicatif de Lisbonne est le 030. | pl=códigos de área
a cópia | la copie, la sauvegarde | Por favor, traga uma cópia do seu passaporte. | Apportez une copie de votre passeport, s'il vous plaît.
o disco rígido | le disque dur | O HD está cheio. | Le disque dur est plein. | pl=discos rígidos | ex?
o dispositivo | l'appareil | Tenho três dispositivos conectados. | J'ai trois appareils connectés.
o DVD | le DVD | O filme só existe em DVD. | Le film n'existe plus qu'en DVD. | g?
o editor | l'éditeur (responsable) | O editor aparece na primeira página. | L'éditeur figure sur la première page.
a editora | la maison d'édition | O livro foi publicado por uma editora pequena. | Le livre a été publié par une petite maison d'édition.
a estatística | la statistique | A estatística não diz toda a verdade. | La statistique ne dit pas toute la vérité.
o estúdio | le studio | O programa é ao vivo, direto do estúdio. | L'émission est diffusée en direct du studio.
a expressão | l'expression | Esta expressão é muito coloquial. | Cette expression est très familière. | pl=expressões
o fax | le fax, télécopie | Mande-me o formulário por fax. | Envoyez-moi le formulaire par fax. | g? | pl=fax
a fita cassete | la cassette | No porão ainda há fitas cassete antigas. | Il reste de vieilles cassettes à la cave. | g? | pl=fitas cassetes | ex?
o fórum | le forum | A resposta está num fórum na internet. | La réponse se trouve dans un forum sur Internet.
o gráfico | le graphique | O gráfico mostra a tendência. | Le graphique montre la tendance.
a ilustração | l'illustration, image | A figura mostra exatamente como funciona o jogo. | L'illustration montre le déroulement précis du match. | pl=ilustrações | ex?
a imagem | l'image | Eles cuidam muito da imagem. | Ils soignent beaucoup leur image.
a influência | l'influence | Ele tem muita influência entre os jovens. | Il a beaucoup d'influence chez les jeunes.
a inovação | l'innovation | A inovação muda o setor a cada ano. | L'innovation change le secteur chaque année. | pl=inovações
""",
"media_b1_pt_2": """
a instruções de uso | la notice d'utilisation | As instruções de uso estão em alemão. | La notice est en allemand. | pl=instruções de uso
a invenção | l'invention | A imprensa foi uma invenção decisiva. | L'imprimerie fut une invention décisive. | pl=invenções
o logotipo | le logo | Eles mudaram o logotipo em janeiro. | Ils ont changé le logo en janvier.
o manual de instruções | le mode d'emploi | Lê primeiro o manual de instruções. | Lis d'abord le mode d'emploi. | pl=manuais de instruções
o monitor | l'écran, moniteur | O monitor é pequeno demais para trabalhar. | L'écran est trop petit pour travailler.
a média | la moyenne | A média de idade é de trinta anos. | La moyenne d'âge est de trente ans.
a notícia falsa | la fausse nouvelle | A notícia falsa correu mais rápido do que a correção. | La fausse nouvelle a été plus rapide que le démenti. | pl=notícias falsas
a novidade | la nouvelle | Eu fico a saber das novidades tarde. | J'apprends les nouvelles tard.
o número de telefone | le numéro de téléphone | Por favor, informe o seu número de telefone. | Veuillez indiquer votre numéro de téléphone. | pl=números de telefone
o ouvinte | l'auditeur | O palestrante tinha muitos ouvintes atentos. | L'orateur avait beaucoup d'auditeurs attentifs. | g?
o patrocínio | le parrainage | O patrocínio paga o estádio. | Le parrainage paie le stade.
o perfil | le profil | O perfil dela tem mil seguidores. | Son profil a mille abonnés. | pl=perfis
a porcentagem | le pourcentage | A porcentagem subiu três pontos. | Le pourcentage a monté de trois points.
a privacidade | la vie privée | A privacidade preocupa os utilizadores. | La vie privée inquiète les utilisateurs.
o programa de computador | le logiciel | Para o trabalho ele precisa de um programa especial. | Il a besoin d'un logiciel spécial pour son travail. | pl=programas de computador | ex?
a propaganda | la publicité | Depois da propaganda o filme continua. | Après la publicité, le film reprend.
a proporção | la proportion | A proporção de mulheres é maior. | La proportion de femmes est plus élevée. | pl=proporções
a publicação | la publication | A publicação teve muitas reações. | La publication a eu beaucoup de réactions. | pl=publicações
a radiodifusão | la radiodiffusion | Ela trabalha na rádio e televisão. | Elle travaille à la radio. | g? | pl=radiodifusões | ex?
a reação | la réaction | A reação dele foi imediata. | Sa réaction a été immédiate. | pl=reações
o remetente | l'expéditeur | Na carta não tem remetente. | Il n'y a pas d'expéditeur sur la lettre. | g?
a secretária eletrónica | le répondeur | Deixa um recado na secretária eletrónica, por favor. | Laisse-moi un message sur le répondeur. | pl=secretárias eletrónicas
o seguidor | l'abonné | Ele ganhou cem seguidores em um dia. | Il a gagné cent abonnés en un jour.
o servidor | le serveur | O servidor está fora do ar. | Le serveur est en panne.
o slogan | le slogan | O slogan é fácil de lembrar. | Le slogan se retient très bien.
o smartphone | le téléphone intelligent | Sem smartphone eu não acho o caminho. | Sans téléphone intelligent, je ne trouve pas mon chemin. | g?
o software | le logiciel | Este software é muito fácil de usar. | Ce logiciel est très simple à utiliser.
a série | la série | Esta série já tem oito temporadas. | Cette série compte déjà huit saisons.
a tecla | la touche | Aperte a tecla verde. | Appuyez sur la touche verte. | g?
o telefone fixo | la ligne fixe | Prefiro que o senhor ligue-me no fixo. | Appelez-moi plutôt sur la ligne fixe. | g? | pl=telefones fixos | ex?
o telefone telemóvel | le téléphone portable | Por favor, desligue o seu telemóvel. | Veuillez éteindre votre téléphone portable. | g? | pl=telefones telemóveis | ex?
o telefonema | l'appel téléphonique | Acabei de ter um telefonema importante com o meu chefe. | Je viens d'avoir un appel téléphonique important avec mon patron.
o tráfego de dados | le trafic de données | O tráfego de dados aumenta muito todo ano. | Le trafic de données augmente fortement chaque année. | pl=tráfegos de dados
a técnica | la technique, technologie | No peixe, a técnica de corte decide tudo. | Pour le poisson, la manière de couper décide de tout. | g?
a unidade de disco | le lecteur (informatique) | O computador não há mais drive. | L'ordinateur n'a plus de lecteur. | pl=unidades de disco | ex?
o vício | l'addiction | Fumar é um vício. | Fumer est une dépendance.
o vírus | le virus | Um vírus travou o computador. | Un virus a bloqué l'ordinateur. | pl=vírus
o índice | l'indice | O índice de preços subiu. | L'indice des prix a augmenté.
""",
"dinheiro_b1_pt": """
a abertura | l'ouverture (d'un compte) | A abertura de uma conta leva só dez minutos. | L'ouverture d'un compte ne prend que dix minutes. | g?
o armazém | l'entrepôt | O armazém está cheio. | L'entrepôt est plein.
o atendimento ao cliente | le service client | O atendimento ao cliente funciona vinte e quatro horas. | Le service client est joignable vingt-quatre heures sur vingt-quatre. | pl=atendimentos aos clientes
o aumento | l'augmentation, hausse | O aumento de casos assim é motivo de preocupação. | La multiplication de tels cas donne matière à inquiétude.
o aval | la caution | O banco pede um fiador. | La banque demande une caution. | ex?
o aviso de cobrança | rappel (de paiement) | Já recebi o segundo aviso de cobrança da empresa. | J'ai déjà reçu le deuxième rappel de paiement de l'entreprise. | g? | pl=avisos de cobrança
a ação | l'action | A ação subiu três por cento. | L'action a monté de trois pour cent. | pl=ações
a cadeia | la chaîne | No fim da cadeia alimentar tudo se acumula. | Au bout de la chaîne alimentaire, tout s'accumule.
o cartão de crédito | la carte de crédit | Geralmente pago com cartão de crédito. | Je paie la plupart du temps par carte de crédit. | pl=cartões de crédito
o cartão de débito | la carte de débit | Posso pagar no débito? | Puis-je payer par carte de débit ? | pl=cartões de débito | ex?
o cartão do banco | la carte bancaire | Pago com o cartão do banco. | Je paie avec la carte bancaire. | pl=cartões do banco
o catálogo | le catalogue |  |  | ex=?
o comprador | l'acheteur | Apareceu um comprador para o carro. | Un acheteur s'est présenté pour la voiture.
o comércio | le commerce | O comércio entre os dois países cresceu. | Le commerce entre les deux pays a crû.
a concorrência | la concurrence | Há muita concorrência no setor. | Il y a beaucoup de concurrence dans le secteur.
o consumidor | le consommateur | O consumidor compara preços. | Le consommateur compare les prix.
a consumidora | la consommatrice | A consumidora reclamou do preço. | La consommatrice s'est plainte du prix. | g?
o consumo | la consommation | O consumo de água caiu em agosto. | La consommation d'eau a baissé en août.
a contribuição | la cotisation, contribution | A alíquota de contribuição sobe na virada do ano. | Le taux de cotisation augmente au changement d'année. | pl=contribuições
o corte | la coupe budgétaire | Anunciaram um corte na saúde. | Ils ont annoncé une coupe dans la santé.
a crise | la crise | A crise durou três anos. | La crise a duré trois ans.
o código do banco | le code banque | O código do banco está no cartão. | Le code banque figure sur la carte. | pl=códigos do banco
a data de validade | la date de péremption | Confere a data de validade na embalagem. | Vérifie la date de péremption sur l'emballage. | g? | pl=datas de validade
o desemprego | le chômage | O desemprego caiu dois pontos. | Le chômage a baissé de deux points.
a devolução | le retour | A devolução é gratuita. | Le retour est gratuit. | pl=devoluções
o dinheiro em espécie | l'argent liquide | Prefiro pagar em dinheiro do que com cartão. | Je préfère payer en liquide plutôt qu'avec une carte. | pl=dinheiros ens espécies | ex?
a divisa | la devise | Ele trocou moeda no aeroporto. | Il a changé des devises à l'aéroport. | ex?
o débito automático | virement automatique |  |  | pl=débitos automáticos | ex=?
a economia | l'économie | A economia cresce devagar. | L'économie croît lentement.
a embalagem | l'emballage | A embalagem é de papelão reciclado. | L'emballage est en carton recyclé.
o emprego | l'emploi | O emprego melhorou este ano. | L'emploi s'est amélioré cette année.
a entrega | la livraison | A entrega é feita de manhã. | La livraison se fait le matin.
a etiqueta | l'étiquette | Eu colaria a etiqueta na tampa. | Moi, je collerais l'étiquette sur le couvercle.
o fabricante | le fabricant | O fabricante dá dois anos de garantia. | Le fabricant donne deux ans de garantie.
o fundo | le fonds | O fundo investe em energia limpa. | Le fonds investit dans l'énergie propre.
a garantia | la garantie | A garantia dura dois anos. | La garantie dure deux ans.
o IBAN | l'IBAN | Para a transferência preciso do teu IBAN. | Pour le virement, j'ai besoin de ton IBAN.
a importação | l'importation | A importação da Ásia aumentou. | L'importation depuis l'Asie a augmenté. | g? | pl=importações
a indústria | l'industrie | A indústria têxtil caiu muito. | L'industrie textile a beaucoup baissé.
a inflação | l'inflation | A inflação encarece a comida. | L'inflation renchérit la nourriture. | pl=inflações
""",
"dinheiro_b1_pt_2": """
o investimento | l'investissement | O investimento criou cem empregos. | L'investissement a créé cent emplois.
o juros | l'intérêt (bancaire) | Pelo empréstimo pagam-se juros. | Pour le crédit, on paie des intérêts. | g? | pl=juros
o lucro | le bénéfice ; gain | A empresa está a ter lucro este ano. | L'entreprise fait des bénéfices cette année.
o maquinário | les machines | O maquinário é dos anos noventa. | Les machines datent des années quatre-vingt-dix.
a mercadoria | la marchandise | A mercadoria será entregue amanhã. | La marchandise sera livrée demain. | g?
a mesada | l'argent de poche | A minha filha recebe mesada toda semana. | Ma fille reçoit de l'argent de poche chaque semaine. | g?
a montagem | l'assemblage | A montagem leva duas horas. | L'assemblage prend deux heures.
a necessidade | le besoin, demande | Em caso de necessidade, ligue para nós, por favor. | En cas de besoin, appelez-nous.
o número de cliente | le numéro de client | Por favor, informe o seu número de cliente. | Veuillez indiquer votre numéro de client. | pl=números de cliente
o operário | l'ouvrier | O operário trabalha no turno da noite. | L'ouvrier travaille de nuit.
o pacotinho | le petit paquet | Um pacotinho custa menos que um pacote. | Un petit paquet coûte moins cher qu'un colis.
o pagamento | le paiement | O pagamento foi recebido. | Le paiement nous est bien parvenu.
o pagamento parcelado | le paiement échelonné |  |  | pl=pagamentos parcelados | ex=?
o prejuízo | la perte | A empresa teve prejuízo no ano passado. | L'entreprise a subi une perte l'année dernière.
a procura | la demande (marché) | A procura por apartamentos é grande. | La demande de logements est forte. | g?
a produção | la production | A produção cresceu cinco por cento. | La production a crû de cinq pour cent. | pl=produções
a rentabilidade | la rentabilité | A rentabilidade está baixa este ano. | La rentabilité est faible cette année.
o saldo | le solde | O saldo da conta é zero. | Le solde du compte est nul.
o salão de cabeleireiro | salon de coiffure | Ela tem horário no salão às quatro horas. | Elle a un rendez-vous au salon de coiffure à seize heures. | pl=salões de cabeleireiro | ex?
o setor | le secteur | Ele trabalha há dez anos no setor de gastronomia. | Il travaille dans la restauration depuis dix ans.
o talho | la boucherie | Sempre compro carne no talho da esquina. | J'achète toujours la viande à la boucherie du coin.
a transferência | virement | A transferência normalmente leva um dia. | Le virement prend normalement un jour. | g?
o título | l'obligation, le bon | Ele comprou um título do governo. | Il a acheté une obligation d'État.
""",
"sentimentos_b1_pt": """
a alma | l'âme | A música faz bem para a alma. | La musique fait du bien à l'âme. | g?
a autoconfiança | la confiance en soi | A autoconfiança dela cresceu ultimamente. | Sa confiance en soi a grandi ces derniers temps. | g?
a autoestima | l'estime de soi | A autoestima constrói-se devagar. | L'estime de soi se construit lentement.
o azar | la malchance | Isso foi pura imprudência, não azar. | C'était de la pure imprudence, pas de la malchance. | g?
a beleza | la beauté | A beleza da paisagem impressionou-me. | La beauté du paysage m'a impressionné. | g?
a briga | la dispute | Depois da briga eles fizeram as pazes. | Après la dispute, ils se sont réconciliés.
o ciúme | la jalousie | O ciúme dele torna o relacionamento difícil. | Sa jalousie complique la relation.
o compaixão | la compassion | Ela mostrou muita compaixão pelas pessoas afetadas. | Elle a montré une grande compassion pour les personnes touchées. | pl=compaixões
o comportamento | le comportement | O comportamento dele mudou de repente. | Son comportement a changé d'un coup.
a compreensão | la compréhension | Obrigado pela sua compreensão. | Merci de votre compréhension. | pl=compreensões
a consideração | les égards, considération | Tenha consideração pelos outros inquilinos, por favor. | S'il te plaît, aie des égards pour les autres locataires. | pl=considerações
a decepção | la déception | A decepção estava estampada no rosto dela. | La déception se lisait sur son visage. | g? | pl=decepções
o desejo | le souhait | O maior desejo dela é um emprego fixo. | Son plus grand souhait est un poste fixe. | g?
a desgraça | le malheur, accident | Uma ligação evitou a desgraça. | Un appel évita le malheur. | g?
o dor de amor | le chagrin d'amour | Depois da separação ele sofreu muito tempo de dor de amor. | Après la séparation, il a eu un chagrin d'amour pendant longtemps. | pl=dores de amor
a emoção | l'émotion | Ele não soube esconder a emoção. | Il n'a pas su cacher l'émotion. | pl=emoções
a esperança | l'espoir | Ainda não perdi a esperança. | Je n'ai pas encore perdu espoir. | g?
a fraqueza | la faiblesse | Ceder aqui não é fraqueza, mas estratégia. | Céder n'est pas ici une faiblesse, mais une stratégie.
a honra | l'honneur | É uma honra conhecer o senhor. | C'est un honneur de faire votre connaissance.
a imaginação | l'imagination | As crianças têm muita imaginação. | Les enfants ont beaucoup d'imagination. | pl=imaginações
a impressão | l'impression | Ela causou uma boa impressão na nutricionista. | Elle a fait bonne impression sur la conseillère en nutrition. | g? | pl=impressões
a intenção | l'intention | Ele deu a entender a sua intenção. | Il laissait entendre son intention. | pl=intenções
a memória | la mémoire | A memória dela é excelente. | Sa mémoire est excellente.
a mente | l'esprit | Ele tem uma mente muito desperta. | Il a un esprit très éveillé.
a motivação | la motivation | Falta motivação a ele este ano. | Il manque de motivation cette année. | pl=motivações
o pensamento | la pensée | Um pensamento veio-lhe de repente. | Une pensée lui est venue soudain.
a percepção | la perception | A percepção de risco dele é baixa. | Sa perception du risque est faible. | pl=percepções
a pressão | la pression | No trabalho tenho muita pressão. | Au travail, je subis beaucoup de pression. | g? | pl=pressões
o pânico | panique | Com o alarme de incêndio, houve pânico. | La panique a éclaté à l'alarme incendie.
a saudade de casa | le mal du pays | No começo eu sentia muita saudade de casa. | Au début, j'avais un grand mal du pays. | pl=saudades de casa
o segredo | le secret | Mantenha a sua palavra-passe em segredo. | Gardez votre mot de passe secret.
o sentimento | le sentiment | Ela tem dificuldade de mostrar os sentimentos. | Elle a du mal à montrer ses sentiments.
a serenidade | le calme/sérénité | Ele sempre reage ao estresse com serenidade. | Il réagit toujours au stress avec sérénité.
o susto | la frayeur | Que susto! | Quelle frayeur !
o talento | le talent | Ela tem muito talento para línguas. | Elle a un grand talent pour les langues.
o temor | la crainte, la peur | Ele falou sem temor. | Il a parlé sans crainte.
""",
"sociedade_b1_pt": """
o abandono | l'abandon | A evasão escolar caiu este ano. | L'abandon scolaire a baissé cette année. | ex?
o abismo | le fossé | A exclusão digital afeta os idosos. | Le fossé numérique touche les personnes âgées. | ex?
o acesso | l'accès | O acesso à moradia é difícil. | L'accès au logement est difficile.
o acolhimento | l'accueil | O acolhimento no vilarejo foi bom. | L'accueil au village a été bon.
o acontecimento | l'événement | Foi o acontecimento do ano. | Ce fut l'événement de l'année.
o acordo | l'accord | Eles chegaram a um acordo na sexta. | Ils sont arrivés à un accord vendredi.
a administração | l'administration | A administração da cidade introduziu muitas regras novas. | L'administration de la ville a introduit beaucoup de nouvelles règles. | g? | pl=administrações
a arrecadação | la collecte | Fazemos uma arrecadação de roupas. | Nous faisons une collecte de vêtements. | pl=arrecadações
o arrombador | cambrioleur | O ladrão foi pego pela polícia. | Le cambrioleur a été arrêté par la police. | ex?
o arrombamento | le cambriolage | Depois do arrombamento ela instalou uma fechadura nova. | Après le cambriolage, elle a fait installer une nouvelle serrure.
o asilo | l'asile | Ele pediu asilo na fronteira. | Il a demandé l'asile à la frontière.
o assassino | le tueur | No policial o assassino é preso no final. | Dans le polar, le tueur est arrêté à la fin.
a assistência social | l'aide sociale | A família recebe assistência social. | La famille reçoit une aide sociale. | g? | pl=assistências sociais
a associação | l'association | A associação organiza a festa do bairro. | L'association organise la fête du quartier. | pl=associações
o atestado | l'attestation, certificat | A repartição emite um atestado para o senhor. | L'administration vous délivre une attestation.
o ato | l'acte, action | O terceiro ato é o melhor. | Le troisième acte est le meilleur.
a atualidade | l'actualité | Ele acompanha a atualidade toda manhã. | Il suit l'actualité chaque matin.
a autorização | l'autorisation | Sem autorização não se pode estacionar aqui. | Sans autorisation, on n'a pas le droit de se garer ici. | pl=autorizações
o beneficiário | le bénéficiaire | Há trezentos beneficiários. | Il y a trois cents bénéficiaires.
a burocracia | la bureaucratie | A burocracia de algumas repartições é muito complicada. | La bureaucratie dans certains bureaux est très compliquée. | g?
a campanha | la campagne | A campanha dura três semanas. | La campagne dure trois semaines.
a candidata | la candidate (femme) | A candidata apresenta hoje o seu programa. | La candidate présente son programme aujourd'hui. | g?
a certidão de nascimento | l'acte de naissance | Para o requerimento o senhor precisa da certidão de nascimento. | Pour la demande, vous avez besoin de votre acte de naissance. | g? | pl=certidões de nascimento
o certificado de naturalização | certificat de naturalisation | Ontem ela recebeu o certificado de naturalização. | Elle a reçu hier son certificat de naturalisation. | pl=certificados de naturalização
a cidadania | la citoyenneté | Ele obteve a cidadania em 2023. | Il a obtenu la citoyenneté en 2023.
a cidadã | la citoyenne | A cidadã faz trabalho voluntário há anos. | La citoyenne s'engage bénévolement depuis des années. | g?
a cidadã da ue | la citoyenne de l'UE | A cidadã da UE não precisa de visto para a viagem. | La citoyenne de l'UE n'a pas besoin de visa pour le voyage. | g? | pl=cidadãs da ue
o cidadão da ue | le citoyen de l'UE | Como cidadão da UE ele pode trabalhar em qualquer país-membro. | En tant que citoyen de l'UE, il peut travailler dans chaque pays membre. | pl=cidadãos da ue
a coalizão | la coalition | A coalizão chega a um acordo. | La coalition s'accorde sur un compromis. | g? | pl=coalizões
o conselho tutelar | le service de la jeunesse | O órgão de proteção à juventude ajuda a família. | Le service de la jeunesse aide la famille. | pl=conselhos tutelares | ex?
o consentimento | l'accord, consentement | Sem o consentimento dela nada pode ser feito. | Rien ne peut être entrepris sans son accord.
a conservatória de registo civil | le bureau de l'état civil |  |  | g? | pl=conservatórias de registo civil | ex=?
a constituição | la constitution | A constituição garante a liberdade de expressão. | La constitution garantit la liberté d'expression. | g? | pl=constituições
o consulado | le consulat | O visto o senhor consegue no consulado. | Vous obtiendrez le visa au consulat.
o controle | le contrôle | Onde está o controle da TV? | Où est la télécommande de la télé ? | g?
a cooperação | la coopération | A cooperação entre vilarejos funciona. | La coopération entre villages fonctionne. | pl=cooperações
a coroa | la couronne | A coroa está no museu. | La couronne se trouve au musée. | g?
a corrupção | la corruption | A corrupção indigna os cidadãos. | La corruption indigne les citoyens. | pl=corrupções
a criminalidade | la délinquance | A criminalidade caiu dez por cento. | La délinquance a baissé de dix pour cent.
o criminoso | le criminel | O criminoso foi preso rapidamente. | Le criminel a été arrêté rapidement.
""",
"sociedade_b1_pt_2": """
os dados pessoais | les état civil, identité | A polícia anota os dados pessoais. | La police relève l'identité.
o dano | le dommage, dégât | Os danos materiais foram menores. | Les dégâts matériels ont été mineurs.
a declaração | la déclaration | Ele fez uma declaração à tarde. | Il a fait une déclaration l'après-midi. | pl=declarações
o deputado | le député | O deputado vota contra a lei nova. | Le député vote contre la nouvelle loi.
a desconfiança | la méfiance | Há desconfiança em relação às instituições. | Il y a de la méfiance envers les institutions.
o desenvolvimento | le développement, évolution | O desenvolvimento do país foi rápido. | Le développement du pays a été rapide.
a desigualdade | l'inégalité | A desigualdade entre o campo e a cidade cresce. | L'inégalité entre la campagne et la ville augmente.
o dever | le devoir, obligation | Todo mundo tem direitos e deveres. | Chacun a des droits et des devoirs. | g?
a diferença salarial | l'écart de salaire | A diferença salarial diminuiu um ponto. | L'écart de salaire s'est réduit d'un point. | pl=diferenças salariais
o direito | le droit | Ele tem direito a um advogado. | Il a droit à un avocat.
o direito de voto | le droit de vote |  |  | pl=direitos de voto | ex=?
a discriminação | la discrimination | A lei pune a discriminação. | La loi punit la discrimination. | pl=discriminações
o discurso | le discours | O discurso durou vinte minutos. | Le discours a duré vingt minutes.
o donativo | le don | Ele deixou uma doação na caixa. | Il a laissé un don dans la boîte. | ex?
a embaixada | l'ambassade ; message | O visto o senhor consegue na embaixada. | Vous obtiendrez le visa à l'ambassade.
a emigração | l'émigration | A emigração para a América era muito comum no século XIX. | L'émigration vers l'Amérique était très fréquente au 19e siècle. | g? | pl=emigrações
o engajamento | l'engagement | A dedicação dela à comunidade é muito valorizada. | Son engagement pour la communauté est très apprécié. | ex?
a estrangeira | l'étrangère | A estrangeira mora na Alemanha há cinco anos. | L'étrangère vit en Allemagne depuis cinq ans. | g?
a exclusão | l'exclusion | A exclusão começa na escola. | L'exclusion commence à l'école. | pl=exclusões
a exportação | l'exportation | A exportação de máquinas é muito importante para o país. | L'exportation de machines est très importante pour le pays. | g? | pl=exportações
o formulário de requerimento | le formulaire de demande | Por favor, preencha o formulário completo. | Veuillez remplir entièrement le formulaire de demande. | pl=formulários de requerimento | ex?
a fuga | la fuite, exil | A fuga durou três semanas. | La fuite a duré trois semaines. | g?
o habitante | l'habitant | A cidade tem duzentos mil habitantes. | La ville compte deux cent mille habitants. | g?
a igualdade | l'égalité | Eles lutam pela igualdade salarial. | Ils luttent pour l'égalité des salaires.
a igualdade de direitos | l'égalité des droits | A igualdade entre homens e mulheres é importante para ela. | L'égalité des droits entre hommes et femmes est importante pour elle. | g? | pl=igualdades de direitos | ex?
o imigrante | l'immigré | O imigrante chegou há dez anos. | L'immigré est arrivé il y a dix ans.
a imigração | l'immigration | A imigração mudou o bairro. | L'immigration a changé le quartier. | pl=imigrações
o impacto | l'impact | A medida teve pouco impacto. | La mesure a eu peu d'impact.
o incentivo | la aide, subvention | A escola recebe um financiamento do estado. | L'école reçoit une subvention du Land. | ex?
a integração | l'intégration | A integração leva tempo. | L'intégration prend du temps. | pl=integrações
a intimação | l'injonction, mise en demeure | Recebi uma intimação da repartição. | J'ai reçu une mise en demeure de l'administration. | pl=intimações
a liberdade | la liberté | A liberdade de imprensa está protegida. | La liberté de la presse est protégée.
a luta | le combat, la lutte | A luta contra a pobreza continua. | La lutte contre la pauvreté continue. | g?
a manifestação | la manifestation | Houve uma manifestação na praça. | Il y a eu une manifestation sur la place. | pl=manifestações
o maus-tratos | la maltraitance | Denunciaram um caso de maus-tratos. | Ils ont dénoncé un cas de maltraitance. | pl=maus-tratos
a medida | la mesure (décision) | A cidade decidiu novas medidas. | La ville a décidé de nouvelles mesures. | g?
o membro | le membre | A comunidade religiosa aqui há quarenta membros. | La communauté religieuse compte ici quarante membres.
o migrante | le migrant | Muitos migrantes buscam uma vida melhor na Europa. | Beaucoup de migrants cherchent une vie meilleure en Europe. | g?
a migração | la migration | Migração é um tema em toda a Europa. | La migration est un sujet dans toute l'Europe. | pl=migrações
a minoria | la minorité | Os direitos das minorias precisam de ser protegidos. | Les droits des minorités doivent être protégés.
""",
"sociedade_b1_pt_3": """
o morto | le mort, victime | Ainda bem que não houve mortos no acidente. | Heureusement, l'accident n'a pas fait de morts.
a nação | la nation | Muitas nações trabalham juntas na proteção do clima. | De nombreuses nations collaborent pour la protection du climat. | pl=nações
a norma | la règle, la norme | A norma aplica-se a todos. | La règle s'applique à tous.
a oportunidade | l'occasion, la chance | Todos merecem a mesma oportunidade. | Tous méritent la même chance.
a oposição | l'opposition | A oposição criticou a medida. | L'opposition a critiqué la mesure. | pl=oposições
a ordem social | l'ordre social | Esta ordem social mudou muito. | Cet ordre social a beaucoup changé. | pl=ordens sociais
a organização | l'organisation | A organização atua em vinte países. | L'organisation travaille dans vingt pays. | pl=organizações
a origem | l'origine | A família dele é de origem galega. | Sa famille est d'origine galicienne.
a origem imigrante | l'origine migratoire | Muitas crianças da turma têm origem imigrante. | Beaucoup d'enfants de la classe ont une origine migratoire. | pl=origens imigrantes
o país de origem | le pays d'origine | Preencha o seu país de origem, por favor. | Indiquez votre pays d'origine, s'il vous plaît. | pl=paises de origem
a pobreza | la pauvreté | A pobreza afeta uma criança em cada cinco. | La pauvreté touche un enfant sur cinq.
o poder | le pouvoir | Ela tem muito poder na empresa. | Elle a beaucoup de pouvoir dans l'entreprise. | g?
a polícia civil | la police criminelle | A polícia de investigação está a apurar o caso desde a semana passada. | La police criminelle enquête sur l'affaire depuis la semaine dernière. | g? | pl=polícias civis | ex?
a política | la politique | Não falamos de política à mesa. | Nous ne parlons pas politique à table.
o político | l'homme politique | Os políticos discutem os impostos. | Les hommes politiques débattent des impôts.
a população | la population | A população do vilarejo diminui a cada ano. | La population du village baisse chaque année. | pl=populações
o preconceito | le préjugé | Há muitos preconceitos contra os jovens. | Il y a beaucoup de préjugés sur les jeunes.
o presidente da câmara | le maire | O presidente da câmara inaugura hoje a nova câmara municipal. | Le maire inaugure aujourd'hui la nouvelle mairie. | g? | pl=presidentes da câmara
o presidente federal | le président fédéral | O presidente federal faz um discurso. | Le président fédéral prononce un discours. | pl=presidentes federais
o privilégio | le privilège | É um privilégio poder estudar. | C'est un privilège de pouvoir étudier.
o processo | le processus, procès | O processo de integração leva tempo. | Le processus d'intégration prend du temps.
a proibição | l'interdiction | A proibição vale a partir de janeiro. | L'interdiction s'applique à partir de janvier. | g? | pl=proibições
o protesto | la protestation | Houve protestos fortes contra os planos. | Les projets ont suscité de vives protestations.
a proteção | la protection | O seguro oferece proteção contra roubo. | L'assurance offre une protection contre le vol. | pl=proteções
o refugiado | le réfugié | O refugiado espera uma resposta. | Le réfugié attend une réponse.
a reivindicação | la revendication, exigence | As reivindicações dos trabalhadores são claras. | Les revendications des ouvriers sont claires. | pl=reivindicações
a repartição pública | l'administration, bureau officiel | Esse requerimento o senhor faz na repartição. | Cette demande se fait auprès de l'administration. | pl=repartições públicas | ex?
a representação | la représentation | Falta representação dos jovens. | Il manque une représentation des jeunes. | pl=representações
o requerimento | la demande (formulaire) | Ela fez o requerimento do auxílio parental. | Elle a déposé une demande d'allocation parentale.
a residência | la résidence | Ele tem residência permanente. | Il a la résidence permanente.
a secretaria de assistência social | le service social | O requerimento o senhor faz na assistência social. | Vous déposez la demande au service social. | g? | pl=secretarias de assistência social | ex?
o sexo | le sexe, le genre | O formulário pergunta o sexo. | Le formulaire demande le sexe.
a sociedade | la société | A sociedade mudou muito em trinta anos. | La société a beaucoup changé en trente ans.
a solidariedade | la solidarité | A solidariedade do bairro surpreendeu a todos. | La solidarité du quartier a surpris tout le monde.
a solidão | la solitude | A solidão afeta muito os idosos. | La solitude touche beaucoup les personnes âgées. | pl=solidões
a tendência | la tendance | É uma tendência dos últimos anos. | C'est une tendance des dernières années.
a Turquia | la Turquie | No verão vamos para a Turquia. | Cet été, nous allons en Turquie. | g?
a Ucrânia | l'Ukraine | A família dele é da Ucrânia. | Sa famille vient d'Ukraine.
o valor | la valeur | A honestidade é um valor importante. | L'honnêteté est une valeur importante.
a violência | la violence | A violência no estádio preocupa. | La violence au stade inquiète.
o voluntariado | le bénévolat | O voluntariado mudou a vida dele. | Le bénévolat lui a changé la vie.
o voluntário | le bénévole | Os voluntários distribuem comida. | Les bénévoles distribuent des repas.
o voto | le vote | O voto dele decidiu o resultado. | Son vote a décidé du résultat.
""",
"lei_b1_pt": """
o advogado | l'avocat | O advogado dele falou com a família. | Son avocat a parlé avec la famille.
o delito | le délit | É um delito leve. | C'est un délit mineur.
o juiz | le juge | O juiz pediu mais provas. | Le juge a demandé plus de preuves.
o julgamento | le procès | O julgamento começa em setembro. | Le procès commence en septembre.
a justiça | la justice | A justiça demora demais. | La justice met trop de temps.
a pena | la peine | A pena foi de seis meses. | La peine a été de six mois.
a prisão | la prison | Ele passou dois anos na prisão. | Il a passé deux ans en prison. | pl=prisões
a sentença | le jugement | A sentença foi divulgada ontem. | Le jugement a été connu hier.
a vítima | la victime | A vítima depôs no julgamento. | La victime a témoigné au procès.
""",
"ideias_b1_pt": """
a abordagem | l'approche | A abordagem dele é muito prática. | Son approche est très pratique.
o argumento | l'argument | O argumento dele não me convence. | Son argument ne me convainc pas.
a batalha | la bataille | A batalha durou um único dia. | La bataille a duré un seul jour.
a catedral | la cathédrale | A catedral abre às dez. | La cathédrale ouvre à dix heures.
a causa | la cause | A causa do atraso foi a neve. | La cause du retard fut la neige.
a certeza | la certitude | Não tenho nenhuma certeza. | Je n'ai aucune certitude.
a conclusão | la conclusion | A conclusão chega na última página. | La conclusion arrive à la dernière page. | pl=conclusões
a consequência | la conséquence | A consequência apareceu um ano depois. | La conséquence s'est vue un an après.
a ditadura | la dictature | A ditadura terminou em 1975. | La dictature s'est terminée en 1975.
a fé | la foi | Ele fala da sua fé com naturalidade. | Il parle de sa foi avec naturel.
o império | l'empire | O império estendia-se por três continentes. | L'empire s'étendait sur trois continents.
o inconveniente | l'inconvénient | O único inconveniente é a distância. | Le seul inconvénient est la distance.
a independência | l'indépendance | Eles celebram a independência em setembro. | Ils célèbrent l'indépendance en septembre.
a laicidade | la laïcité | A laicidade separa Estado e igreja. | La laïcité sépare l'État et l'église.
o monumento | le monument | O monumento é do século dezoito. | Le monument est du dix-huitième siècle.
a oração | la prière | A oração dura alguns minutos. | La prière dure quelques minutes. | pl=orações
a paz | la paix | Assinaram a paz em 1939. | Ils ont signé la paix en 1939.
o peregrino | le pèlerin | O peregrino caminha trinta quilómetros por dia. | Le pèlerin marche trente kilomètres par jour.
a razão | la raison | Ele tem razão em uma coisa. | Il a raison sur un point. | pl=razões
a religião | la religion | No país convivem várias religiões. | Plusieurs religions cohabitent dans le pays. | pl=religiões
a revolução | la révolution | A revolução mudou o país. | La révolution a changé le pays. | pl=revoluções
o rito | le rite | O rito repete-se a cada primavera. | Le rite se répète chaque printemps.
o templo | le temple | O templo é do século doze. | Le temple est du douzième siècle.
o tratado | le traité | O tratado foi assinado em Lisboa. | Le traité a été signé à Lisboa.
a vantagem | l'avantage | A vantagem é o preço. | L'avantage est le prix.
a época | l'époque | Foi uma época difícil. | Ce fut une époque difficile.
""",
"tempo_b1_pt": """
o começo | le début | No começo tudo era novo para mim. | Au début, tout était nouveau pour moi.
o dia a dia | le quotidien, vie de tous les jours | No dia a dia eu falo alemão quase sempre. | Au quotidien, je parle surtout allemand. | pl=dias as dias
a dia útil | le jour de la semaine | Nos dias úteis eu acordo às seis. | En semaine, je me lève à six heures. | g? | pl=dias úteis
a duração | la durée | A duração do curso é de dez semanas. | La durée du cours est de dix semaines. | g? | pl=durações
a estação do ano | la saison | O verão é a minha estação preferida. | L'été est ma saison préférée. | pl=estações do ano | ex?
o feriado | le jour férié | Amanhã é feriado nacional. | Demain est un jour férié.
o instante | l'instant, moment | Um instante, por favor! | Un instant, s'il vous plaît !
o início | le début | No início do curso éramos doze. | Au début du cours, nous étions douze.
o milénio | le millénaire | A cidade tem mais de mil anos. | La ville a plus de mille ans. | ex?
o período | la période | Nesse período o tempo variou muito. | Pendant cette période, le temps a été très variable.
a pressa | l'hâte, urgence | Hoje de manhã barbeei-me com pressa. | Ce matin, je me suis rasé à la hâte. | g?
a retrospectiva | le bilan/rétrospective | Olhando para trás, o ano foi bem bem-sucedido. | En rétrospective, l'année a été assez réussie. | g? | ex?
a rotina diária | le déroulement de la journée | Descreva a sua rotina diária, por favor. | Décrivez le déroulement de votre journée, s'il vous plaît. | pl=rotinas diárias
o trimestre | le trimestre | Os números do primeiro trimestre saíram. | Les chiffres du premier trimestre sont arrivés.
""",
"quotidiano_b1_pt": """
o acaso | le hasard, coïncidence | Nós encontramo-nos por acaso. | Nous nous sommes rencontrés par hasard.
a alternativa | l'alternative | Andar de bicicleta é uma boa alternativa ao carro. | Faire du vélo est une bonne alternative à la voiture. | g?
a base | la base | A confiança é a base de toda amizade. | La confiance est la base de toute amitié. | g?
o buraco | le trou | Há um buraco fundo na rua. | Il y a un trou profond dans la rue.
o cancelamento | la résiliation, licenciement | Mandei o cancelamento do meu contrato pelo correio. | J'ai envoyé la résiliation de mon contrat par courrier.
a capacitação | la formation continue | Ele está a fazer uma capacitação na área de TI. | Il suit une formation continue en informatique. | pl=capacitações
as coisas | les affaires, trucs | Tira as tuas coisas da mesa! | Enlève tes affaires de la table !
a comparação | la comparaison | Em comparação com antes, está mais barato. | Par comparaison avec avant, c'est moins cher. | pl=comparações
o contraste | contraste, opposé | O contraste entre as cores é muito forte. | Le contraste entre les couleurs est très marqué. | g?
o contrário | le contraire | O contrário de grande é pequeno. | Le contraire de grand est petit.
o CÓDIGO POSTAL | le code postal | O código postal vem antes do nome da cidade. | Le code postal se place avant le nom de la ville. | pl=CÓDIGOs POSTALs
o detalhe | le détail | Conta-me cada detalhe. | Raconte-moi chaque détail. | g?
a dificuldade | la difficulté | Ele tem dificuldade com a gramática. | Il a des difficultés avec la grammaire.
a década | la décennie | Nas últimas duas décadas muita coisa mudou. | Beaucoup de choses ont changé au cours des deux dernières décennies. | g?
a emergência | l'urgence | Em caso de emergência, chame o médico na hora. | Appelez immédiatement le médecin en cas d'urgence. | g?
a exceção | l'exception | Neste caso vamos abrir uma exceção. | Dans ce cas, nous faisons une exception. | pl=exceções
o facto | le fait | É um facto, não uma opinião. | C'est un fait, pas une opinion.
a falta | le manque, pénurie | Há falta de profissionais qualificados. | Il y a une pénurie de personnel qualifié. | g?
o fator | le facteur (élément) | O preço é um fator importante. | Le prix est un facteur important.
a finalidade | le but, objectif | Os recursos foram desviados da sua finalidade. | Les fonds ont été détournés de leur objet.
a localização | la situation, l'emplacement | A localização é mais uma desvantagem. | L'emplacement est plutôt un inconvénient. | pl=localizações
a maioria | la majorité | A maioria dos participantes ficou satisfeita. | La majorité des participants était satisfaite. | g?
o material | le matériau | O material da jaqueta é muito resistente. | Le matériau de la veste est très robuste.
o miligrama | milligramme | O comprimido contém quinhentos miligramas de princípio ativo. | Le comprimé contient cinq cents milligrammes de substance active. | g?
a moldura | cadre | O quadro está numa moldura dourada. | Le tableau est accroché dans un cadre doré.
o múltiplo | le multiple | Os múltiplos de quatro são fáceis de calcular. | Le multiple de quatre est facile à calculer.
o nome de solteira | le nom de jeune fille | Escreva também o seu nome de solteira. | Indiquez aussi votre nom de jeune fille. | pl=nomes de solteira
o objeto | l'objet | Não deixe objetos no carro. | Ne laissez aucun objet dans la voiture.
a obra de arte | l'œuvre d'art | Esta obra de arte está no museu há cem anos. | Cette œuvre d'art est exposée au musée depuis cent ans. | pl=obras de arte
o ofício artesanal | l'artisanat, métier manuel | Ela aprendeu um ofício tradicional. | Elle a appris un artisanat traditionnel. | pl=ofícios artesanais | ex?
o padrão | le motif | Com isso a empresa estabelece novos padrões. | L'entreprise établit ainsi de nouveaux critères de référence. | pl=padrões
o perdão | le pardon | Com licença, este lugar está livre? | Pardon, cette place est-elle libre ? | pl=perdões | ex?
a peça | la pièce détachée | O armário é composto de muitas peças. | L'armoire est composée de nombreuses pièces détachées. | g?
a peça avulsa | la pièce détachée | Também dá para comprar as peças avulsas. | On peut aussi acheter les pièces séparément. | g? | pl=peças avulsas
o pormenor | le détail |  |  | ex=?
a possibilidade | la possibilité | Ainda há outra possibilidade. | Il y a encore une autre possibilité.
o quilograma | le kilogramme | A mala pesa vinte quilos. | La valise pèse vingt kilogrammes. | g? | ex?
a realidade | la réalité | Infelizmente a realidade é diferente do planeado. | La réalité est malheureusement différente de ce qui était prévu. | g?
a recomendação | la recommandation | O gerente do banco deu-me uma boa recomendação. | Le conseiller bancaire m'a donné une bonne recommandation. | g? | pl=recomendações
o relacionamento | la relation | Eles têm um bom relacionamento. | Ils ont une bonne relation.
o sentido | le sens | Isso não faz sentido para mim. | Ça n'a aucun sens pour moi.
o significado | la signification | Não sei o significado desta palavra. | Je ne connais pas la signification de ce mot.
a simetria | la symétrie | A simetria deste prédio é impressionante. | La symétrie de ce bâtiment est impressionnante. | g?
o sinal | le signe, symbole | O sinal de vitória é conhecido no mundo inteiro. | Le signe de la victoire est connu dans le monde entier.
a sugestão | la proposition, suggestion | Tenho uma sugestão melhor. | J'ai une meilleure proposition. | g? | pl=sugestões
o tipo | la sorte, type | É um tipo de problema completamente novo. | C'est un tout nouveau genre de problème.
o trabalho voluntário | la fonction bénévole | Ela faz trabalho voluntário nos bombeiros com prazer. | Elle exerce sa fonction bénévole aux pompiers avec plaisir. | pl=trabalhos voluntários
a verdade | la vérité | Diz-me a verdade, por favor. | Dis-moi la vérité, s'il te plaît. | g?
o ângulo | l'angle | Mede o ângulo com o esquadro. | Mesure l'angle avec le rapporteur.
""",
}
