# -*- coding: utf-8 -*-
"""Les noms du B2 portugais, par theme. SOURCE : c'est ici qu'on corrige, puis
python portugais/outils/construire.py (qui appelle niveaux.py apres l'A1).

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (29 oct. 2026),
converti au portugais d'Europe (variante_niveaux.py), puis relu. Meme format
que noms_a1.py (session socle). BROUILLON : a faire relire par un lusophone du Portugal.

Drapeaux en plus de ceux de l'A1 : « g? » genre devine (a verifier) ; « ex? »
la phrase ne contient pas le mot (a revoir) ; « ex=? » aucune phrase (a ecrire).
"""

NIVEAU = 'B2'

# (id du theme, nom portugais, theme source dont on reprend l'icone)
THEMES = [
    ('familia_b2_pt', 'Família e relações', 'familie_b2'),
    ('trabalho_b2_pt', 'Trabalho e profissões', 'arbeit_buero_b2'),
    ('comida_b2_pt', 'Comida e cozinha', 'frutas_verduras_b2'),
    ('casa_b2_pt', 'A casa', 'wohnen_b2'),
    ('saude_b2_pt', 'O corpo e a saúde', 'gesundheit_b2'),
    ('roupa_b2_pt', 'Roupa e aparência', 'kleidung_b2'),
    ('natureza_b2_pt', 'Natureza e ambiente', 'tiere_b2'),
    ('viagens_b2_pt', 'Viagens e transportes', 'verkehr_b2'),
    ('cidade_b2_pt', 'A cidade', 'stadt_gebaeude_b2'),
    ('escola_b2_pt', 'Escola e estudos', 'schule_b2'),
    ('cultura_b2_pt', 'Tempos livres e cultura', 'feste_feiertage_b2'),
    ('desporto_b2_pt', 'Desporto', 'sport_b2'),
    ('media_b2_pt', 'Media e comunicação', 'la_ia'),
    ('dinheiro_b2_pt', 'Dinheiro e economia', 'einkaufen_geld_b2'),
    ('sentimentos_b2_pt', 'Sentimentos e caráter', 'nom_interior'),
    ('sociedade_b2_pt', 'Sociedade e política', 'politik_gesellschaft_b2'),
    ('ideias_b2_pt', 'Ideias e debate 1', 'pensamiento_critico'),
    ('ideias_b2_pt_2', 'Ideias e debate 2', 'pensamiento_critico'),
    ('tempo_b2_pt', 'O tempo', 'zeit_kalender_b2'),
    ('quotidiano_b2_pt', 'Palavras do dia a dia', 'zahlen_mengen_b2'),
]

NOMS = {
"familia_b2_pt": """
a adoção | l'adoption | A adoção levou quase três anos. | L'adoption a pris près de trois ans. | g? | pl=adoções
a criança acolhida | l'enfant placé | Eles acolheram uma criança. | Ils ont accueilli un enfant placé. | pl=crianças acolhidas | ex?
a cunhada | la belle-sœur | A minha cunhada assumiu a empresa. | Ma belle-sœur a repris l'entreprise.
o descendente | le descendant | Ele não tem descendentes diretos. | Il n'a pas de descendants directs. | g?
a família recomposta | la famille recomposée | Eles vivem felizes numa família recomposta. | Ils vivent heureux dans une famille recomposée. | pl=famílias recompostas
a madrasta | la belle-mère (remariage) | A madrasta o trata como se fosse filho dela. | Sa belle-mère le traite comme son propre enfant. | g?
o meia-irmã | la demi-sœur | A minha meia-irmã raramente vem nos visitar. | Ma demi-sœur nous rend rarement visite. | g? | pl=meias-irmãs
o meio-irmão | le demi-frère | O meu meio-irmão mora com o pai dele. | Mon demi-frère vit chez son père. | pl=meios-irmãos
o padrasto | le beau-père (remariage) | O padrasto cuida dela com carinho. | Son beau-père s'occupe d'elle avec affection.
o parentes | la parenté | Todos os parentes dele vieram para a festa. | Toute sa parenté est venue à la fête. | pl=parentes
a pensão alimentícia | la pension alimentaire | O pai paga pensão para dois filhos. | Le père verse une pension pour deux enfants. | g? | pl=pensões alimentícias | ex?
o responsável legal | le titulaire de l'autorité parentale | Os responsáveis legais precisam de assinar. | Les titulaires de l'autorité parentale doivent signer. | pl=responsáveis legais
os sogros | les beaux-parents | Os sogros vêm passar a Páscoa. | Les beaux-parents viennent pour Pâques.
o tutor legal | le tuteur légal | Depois da morte dos pais foi nomeado um tutor. | Après la mort des parents, un tuteur légal a été désigné. | pl=tutores legais | ex?
a união familiar | cohésion familiale | A união familiar os ajudou nos tempos difíceis. | La cohésion familiale les a aidés dans les moments difficiles. | g? | pl=uniões familiares
a árvore genealógica | l'arbre généalogique | A árvore genealógica vai até 1750. | L'arbre généalogique remonte à 1750. | g? | pl=árvores genealógicas
""",
"trabalho_b2_pt": """
os acordo de metas | les objectifs convenus | Temos um acordo de metas claro para este trimestre. | Nous avons des objectifs clairement convenus pour ce trimestre.
o ajudante temporário | l'renfort, extra | Em dezembro contratamos dois temporários. | En décembre, nous embauchons deux extras. | g? | pl=ajudantes temporários | ex?
o arquivamento | le classement | Ninguém gosta de arquivar papéis. | Personne n'aime faire le classement. | ex?
a ata | le procès-verbal | Quem escreve a ata hoje? | Qui rédige le procès-verbal aujourd'hui ? | g?
a automação do emprego | l'automatisation de l'emploi | A automação do emprego avança devagar. | L'automatisation de l'emploi avance lentement. | pl=automações do emprego
a autoridade | l'autorité | Ele exerce a autoridade sem levantar a voz. | Il exerce l'autorité sans hausser la voix.
o carisma | le charisme | O carisma dele abre portas. | Son charisme ouvre des portes.
o chefe de departamento | le chef de service | O chefe de departamento decide sozinho. | Le chef de service décide seul. | pl=chefes de departamento
a comissão de funcionários | le comité d'entreprise | A comissão de funcionários precisa de aprovar. | Le comité d'entreprise doit donner son accord. | g? | pl=comissões de funcionários
o contrato de trabalho | le contrat de travail | O contrato de trabalho é por tempo indeterminado. | Le contrat de travail est à durée indéterminée. | pl=contratos de trabalho
o corpo docente | le équipe, corps enseignant | Os professores reúnem-se toda segunda. | L'équipe se réunit tous les lundis. | pl=corpos docentes | ex?
o cronograma | le calendrier de projet | O cronograma atrasou um mês. | Le calendrier a pris un mois de retard.
a cultura empresarial | la culture d'entreprise | A cultura da empresa incentiva a colaboração e a abertura. | La culture d'entreprise favorise la collaboration et l'ouverture. | g? | pl=culturas empresariais | ex?
a delegação | la délégation | O clube enviou uma delegação. | L'association dépêcha une délégation. | pl=delegações
o departamento de rh | les ressources humaines | O RH analisa todas as candidaturas recebidas. | Les ressources humaines examinent toutes les candidatures reçues. | pl=departamentos de rh | ex?
o desgaste | l'usure | O desgaste é maior no lado de dentro. | L'usure est la plus forte à l'intérieur.
o diretora-geral | la directrice générale | A diretora-geral toma todas as decisões importantes. | La directrice générale prend toutes les décisions importantes. | g? | pl=diretoras-gerais
a diretoria | la direction | A diretoria reúne-se amanhã numa reunião de crise. | La direction se réunit demain pour une réunion de crise. | g?
o empresário | l'entrepreneur | O empresário abriu a empresa há dez anos. | L'entrepreneur a fondé son entreprise il y a dix ans.
a experiência profissional | l'expérience professionnelle | A experiência profissional dela convenceu o RH na hora. | Son expérience professionnelle a immédiatement convaincu les ressources humaines. | g? | pl=experiências profissionais
a flexibilidade do trabalho | la flexibilité du travail | A flexibilidade do trabalho tem dois lados. | La flexibilité du travail a deux faces. | pl=flexibilidades do trabalho
o funcionário público | le fonctionnaire | Como funcionário público, ele tem estabilidade. | Comme fonctionnaire, il est inamovible. | pl=funcionários públicos
a gestão | la gestion | A gestão do tempo é o mais difícil. | La gestion du temps est le plus difficile. | pl=gestões
o horário flexível | les horaires flexibles | Nós trabalhamos com horário flexível. | Nous travaillons en horaires flexibles. | pl=horários flexíveis
o indicador | l'indicateur | O indicador melhorou dois pontos. | L'indicateur s'est amélioré de deux points.
o instrutor | le formateur, maître d'apprentissage | O instrutor acompanha quatro aprendizes. | Le formateur encadre quatre apprentis.
a liderança | le leadership | A liderança dele mudou a equipa. | Son leadership a changé l'équipe.
o mentor | le mentor | O mentor dele o acompanhou por cinco anos. | Son mentor l'a accompagné cinq ans.
a motivação da equipa | la motivation de l'équipe | A motivação da equipa caiu no outono. | La motivation de l'équipe a baissé en automne. | pl=motivações da equipa
a negociação salarial | la négociation salariale | A negociação salarial é na primavera. | La négociation salariale a lieu au printemps. | g? | pl=negociações salariais
o nómade digital | le nomade numérique | O nómade digital trabalha de Lisboa. | Le nomade numérique travaille depuis Lisbonne. | pl=nómades digitais
a obsolescência | l'obsolescence | A obsolescência da formação preocupa. | L'obsolescence de la formation inquiète.
a pauta | l'ordre du jour | O item três da pauta foi retirado. | Le point trois de l'ordre du jour est supprimé.
a prestação de contas | la reddition de comptes | A prestação de contas é anual. | La reddition de comptes est annuelle. | pl=prestações de contas
o profissional de ofício | l'artisan | Hoje em dia é difícil achar um bom profissional. | Un bon artisan est difficile à trouver aujourd'hui. | g? | pl=profissionais de ofício | ex?
o profissional liberal | le profession libérale | Como autónomo, ele mesmo paga a previdência. | Comme profession libérale, il cotise lui-même. | g? | pl=profissionais liberais | ex?
o quem muda de carreira | le reconverti professionnel | Mudando de área, ele teve de aprender muita coisa do zero. | En tant que reconverti professionnel, il a dû tout réapprendre. | g? | pl=quens mudas de carreira | ex?
a reconversão | la reconversion | A reconversão do setor levará anos. | La reconversion du secteur durera des années. | pl=reconversões
o recurso humano | les ressources humaines | O recurso humano é o mais valioso. | La ressource humaine est la plus précieuse. | pl=recursos humanos
a referência | le rapport, la référence | A gastronomia francesa é referência no mundo inteiro. | L'art culinaire français est considéré comme une référence mondiale. | g?
a reputação | la réputation | A empresa tem boa reputação. | L'entreprise a une bonne réputation. | pl=reputações
o risco operacional | le risque opérationnel | Avaliam o risco operacional todo mês. | Ils évaluent le risque opérationnel chaque mois. | pl=riscos operacionais
o superior | le supérieur hiérarchique | Ele fez um curso superior de três anos. | Il a fait des études de trois ans.
o trabalhador autónomo | l'travailleur indépendant | Os autónomos não têm renda fixa. | Les indépendants n'ont pas de revenu fixe. | pl=trabalhadores autónomos | ex?
o trabalhador de turno | le travailleur posté | Quem trabalha em turnos muitas vezes dorme mal. | Les travailleurs postés dorment souvent mal. | pl=trabalhadores de turno | ex?
a viagem a trabalho | le voyage professionnel | A viagem a trabalho dura três dias. | Le voyage professionnel dure trois jours. | g? | pl=viagens as trabalhos
a visão | la vision | Ele tem uma visão clara do futuro. | Il a une vision claire de l'avenir. | pl=visões
""",
"comida_b2_pt": """
a acelga | la blette | A minha avó cozinha acelga com batatas. | Ma grand-mère cuisine les blettes avec des pommes de terre.
o aipo | le céleri | Ponho aipo no caldo. | Je mets du céleri dans le bouillon.
a alcachofra | l'artichaut | As alcachofras comem-se folha por folha. | Les artichauts se mangent feuille par feuille.
a batata-doce | la patate douce | Assamos batatas-doces no forno. | On fait rôtir des patates douces au four. | pl=batatas-doces
a boca do fogão | la plaque de cuisson | A boca de trás do fogão está quebrada. | La plaque arrière est cassée. | g? | pl=bocas do fogão | ex?
a coifa | la hotte aspirante | A coifa faz barulho demais. | La hotte est trop bruyante. | g?
os congelados | les surgelés | Os congelados muitas vezes são mais frescos do que se pensa. | Les surgelés sont souvent plus frais qu'on ne croit.
o copo medidor | le verre doseur | Sem copo medidor a receita fica difícil. | Sans verre doseur, la recette devient difficile. | pl=copos medidores
o couve-rábano | le chou-rave | O couve-rábano pode ser comido cru. | Le chou-rave peut se manger cru. | pl=couves-rábanos
a culinária | l'art culinaire | Faço um curso de culinária. | Je suis un cours de cuisine. | g?
a degustação | dégustation | Na degustação vamos provar cinco vinhos diferentes. | Lors de la dégustation, nous goûtons cinq vins différents. | pl=degustações
a despensa | le garde-manger | A despensa está cheia de macarrão. | Le garde-manger est plein de pâtes. | g?
a digestibilidade | digestibilité | Este prato é apreciado por ser leve. | Ce plat est apprécié pour sa digestibilité. | ex?
o enlatado | la conserve | No porão ainda tem enlatados velhos. | Il reste de vieilles conserves à la cave.
o erva-doce | le fenouil | O funcho tem um gosto levemente adocicado. | Le fenouil a un goût légèrement sucré. | g? | pl=ervas-doces | ex?
o estoque | la réserve, provisions | O estoque dá para duas semanas. | La réserve suffit pour deux semaines.
o figo | la figue | Os figos frescos só se encontram no fim do verão. | Les figues fraîches ne se trouvent qu'à la fin de l'été.
o funcho | le fenouil | O funcho tem sabor de anis. | Le fenouil a un goût anisé.
a groselha | la groseille | As groselhas são pequenas e ácidas. | Les groseilles sont petites et acides.
a groselha-espinhosa | la groseille à maquereau | A groselha-espinhosa é verde e peluda. | La groseille à maquereau est verte et poilue. | pl=groselhas-espinhosas
o higiene na cozinha | l'hygiène en cuisine | Higiene na cozinha é muito importante na hora de cozinhar. | L'hygiène en cuisine est très importante lors de la cuisson. | g? | pl=higienes nas cozinhas
a liquidificadora | mixeur |  |  | ex=?
a mistura de temperos | le mélange d'épices | Esta mistura de temperos vem do Marrocos. | Ce mélange d'épices vient du Maroc. | pl=misturas de temperos
a papaia | la papaye |  |  | ex=?
o papaia papaia | la papaye |  |  | g? | pl=papaias papaias | ex=?
o porta-temperos | l'étagère à épices | No porta-temperos está a faltar a pimenta. | Il manque le poivre dans l'étagère à épices. | g? | pl=portas-temperos
o processador de alimentos | le robot de cuisine | O processador pica os legumes em segundos. | Le robot de cuisine hache les légumes en quelques secondes. | pl=processadores de alimentos | ex?
o produto orgânico | le produit bio | Aqui os produtos orgânicos custam quase o dobro. | Les produits bio coûtent presque le double ici. | pl=produtos orgânicos
o ralador | la râpe | O ralador é afiado, toma cuidado. | La râpe est tranchante, fais attention.
a romã | la grenade (fruit) | A romã tem muitas sementes vermelhas. | La grenade a beaucoup de graines rouges.
o suplemento alimentar | le complément alimentaire | Suplemento alimentar não substitui legumes. | Un complément ne remplace pas les légumes. | pl=suplementos alimentares
a travessa | le plat à gratin | O refratário não cabe no forno. | Le plat à gratin ne rentre pas dans le four. | g? | ex?
a tábua de cortar | la planche à découper | Corta a cebola na tábua. | Coupe l'oignon sur la planche à découper. | pl=tábuas de cortar | ex?
o vegano | le végétalien | Para veganos há dois pratos. | Il y a deux plats pour les végétaliens.
o vegetariano | le végétarien | Como vegetariano, ele come ovos e queijo. | Comme végétarien, il mange des œufs et du fromage.
""",
"casa_b2_pt": """
a administradora | la syndic, gérance | A administradora nunca responde aos e-mails. | La gérance ne répond jamais aux courriels. | g?
o aparador | le buffet/vaisselier | O aparador fica na sala de jantar. | Le buffet se trouve dans la salle à manger.
o apartamento próprio | l'appartement en copropriété | Ela comprou um apartamento no centro. | Elle a acheté un appartement en copropriété dans le centre. | pl=apartamentos próprios | ex?
o carpete | la moquette | O carpete tem de sair. | La moquette doit disparaître.
a caução | la caution | Eu reclamaria a caução do proprietário. | Moi, je réclamerais la caution au propriétaire. | pl=cauções
o colchão | le matelas | O colchão é mole demais para as costas. | Le matelas est trop mou pour le dos. | pl=colchões
o contrato de energia elétrica | le contrat d'électricité | O contrato de luz ainda vale por um ano. | Le contrat d'électricité court encore un an. | pl=contratos de energia elétrica | ex?
o contrato de renda | le contrat de location |  |  | pl=contratos de renda | ex=?
a cozinha planeada | la cuisine équipée | O apartamento tem cozinha planeada. | L'appartement a une cuisine équipée. | g? | pl=cozinhas planeadas
a cristaleira | la vitrine | Na cristaleira fica a louça boa. | La belle vaisselle est dans la vitrine.
o custo do aquecimento | les frais de chauffage | O custo do aquecimento dobrou. | Les frais de chauffage ont doublé. | pl=custos do aquecimento
as despesas extras | les charges locatives | As despesas extras sobem todo ano. | Les charges locatives continuent d'augmenter chaque année.
a eficiência energética | l'efficacité énergétique | A eficiência energética deste aparelho é excelente. | L'efficacité énergétique de cet appareil est excellente. | g? | pl=eficiências energéticas
o mercado imobiliário | le marché immobilier | O mercado imobiliário nesta cidade está muito apertado. | Le marché immobilier est très tendu dans cette ville. | pl=mercados imobiliários
a roupa de cama | le linge de lit | A roupa de cama é trocada a cada duas semanas. | Le linge de lit se change toutes les deux semaines. | g? | pl=roupas de cama
a secadora de roupa | sèche-linge | A secadora nos economiza muito tempo. | Le sèche-linge nous fait gagner beaucoup de temps. | g? | pl=secadoras de roupa | ex?
o sótão | le grenier | No sótão está o piano velho. | Au grenier se trouve le vieux piano. | pl=sótãos
""",
"saude_b2_pt": """
o atestado médico | l'arrêt de travail | A partir do terceiro dia é preciso de atestado médico. | À partir du troisième jour, il faut un arrêt de travail. | pl=atestados médicos
o cadáver | le cadavre | A polícia encontrou o cadáver na floresta. | La police a trouvé le cadavre dans la forêt.
a clavícula | la clavicule | A clavícula cicatriza em seis semanas. | La clavicule guérit en six semaines. | g?
o clínico geral | le médecin traitant | O clínico geral encaminha-me para o especialista. | Le médecin traitant m'adresse au spécialiste. | pl=clínicos gerais
a coluna vertebral | la colonne vertébrale | Sentar-se mal é ruim para a coluna vertebral. | Mal s'asseoir est mauvais pour la colonne vertébrale. | pl=colunas vertebrais
a costela | la côte | Caí e quebrei uma costela. | Je suis tombé et je me suis cassé une côte.
o exame preventivo | l'examen préventif | Ela faz check-up regularmente. | Elle va régulièrement à l'examen préventif. | g? | pl=exames preventivos | ex?
a fisioterapia | la kinésithérapie | Depois da fratura veio a fisioterapia. | Après la fracture, il y a eu de la kinésithérapie. | g?
o intestino | l'intestin | O intestino precisa de fibras. | L'intestin a besoin de fibres.
o metabolismo | le métabolisme | Um metabolismo lento dificulta o emagrecimento. | Un métabolisme lent complique la perte de poids.
as nádegas | les fesses | A injeção é aplicada nas nádegas. | La piqûre se fait dans les fesses.
a omoplata | l'omoplate | Dói entre as minhas omoplatas. | J'ai mal entre les omoplates.
a pressão arterial | la tension artérielle | A pressão está um pouco alta. | La tension est un peu trop élevée. | g? | pl=pressões arteriais | ex?
a recuperação | la guérison | A recuperação ainda vai levar algumas semanas. | La guérison durera encore quelques semaines. | g? | pl=recuperações
a rótula | la rotule | A patela saiu do lugar de novo. | La rotule est ressortie. | g? | ex?
a sala de espera | la salle d'attente | Na sala de espera havia doze pessoas. | Douze personnes attendaient dans la salle d'attente. | pl=salas de espera
o sistema de saúde | le système de santé | O sistema de saúde enfrenta grandes desafios. | Le système de santé fait face à de grands défis. | pl=sistemas de saúde
o sistema imunológico | le système immunitaire | O sistema imunológico nos protege das doenças. | Le système immunitaire nous protège des maladies. | pl=sistemas imunológicos
o sistema nervoso | le système nerveux | O sistema nervoso controla todos os movimentos do corpo. | Le système nerveux contrôle tous les mouvements du corps. | pl=sistemas nervosos
o tendão | le tendon | O tendão está inflamado, não rompido. | Le tendon est irrité, pas rompu. | pl=tendões
""",
"roupa_b2_pt": """
o blazer | le blazer | O blazer combina perfeitamente com o look dela. | Le blazer va parfaitement avec sa tenue.
a gola | le col | A gola está lasseada. | Le col est détendu. | g?
o linho | le lin | Linho amassa, faz parte. | Le lin froisse, cela en fait partie.
a meia-calça | le collant | No inverno a meia-calça é indispensável. | Le collant est indispensable en hiver. | g? | pl=meias-calças
o selo de sustentabilidade | label de durabilité | O selo de sustentabilidade garante uma produção justa. | Le label de durabilité garantit une production équitable. | pl=selos de sustentabilidade
a sola | la semelle | A sola está gasta. | La semelle est usée jusqu'au trou. | g?
o t-shirt de baixo | le maillot de corps | Ele usa uma t-shirt branca por baixo da camisa. | Il porte un maillot de corps blanc sous la chemise. | g? | pl=ts-shirts de baixo | ex?
a tendência da moda | la tendance mode | Esta tendência volta a cada década. | Cette tendance mode revient chaque décennie. | pl=tendências da moda | ex?
""",
"natureza_b2_pt": """
o anfíbio | l'amphibien | Os anfíbios precisam de água para desovar. | Les amphibiens ont besoin d'eau pour pondre.
o animal selvagem | l'animal sauvage | Este animal selvagem deve ser observado de longe. | Il faut observer cet animal sauvage de loin. | pl=animais selvagens
o balanço ecológico | le bilan écologique | O balanço ecológico deste produto é surpreendentemente bom. | Le bilan écologique de ce produit est étonnamment bon. | pl=balanços ecológicos
a catástrofe natural | la catastrophe naturelle | A catástrofe natural atingiu a região em cheio. | La catastrophe naturelle a durement touché la région. | g? | pl=catástrofes naturais
os chifres | les bois (de cerf) | O cervo perde os chifres todo ano. | Le cerf perd ses bois chaque année.
o chumbo | le plomb | O chumbo é tóxico para o corpo. | Le plomb est toxique pour le corps.
a compensação | la compensation | A compensação não basta por si só. | La compensation ne suffit pas à elle seule. | pl=compensações
a condições do tempo | la situation météorologique | As condições do tempo seguem estáveis próximo-nos dias. | La situation météorologique reste stable dans les prochains jours. | pl=condições do tempo
a corça | le chevreuil | O veado esconde-se entre as árvores. | Le chevreuil se cache entre les arbres. | g? | ex?
o dano ambiental | le dommage environnemental | O dano ambiental quase não pode ser revertido. | Le dommage environnemental peut difficilement être réparé. | pl=danos ambientais
o desenvolvimento sustentável | le développement durable | O desenvolvimento sustentável exige tempo. | Le développement durable exige du temps. | pl=desenvolvimentos sustentáveis
a economia circular | l'économie circulaire | A economia circular reduz o resíduo. | L'économie circulaire réduit le déchet. | pl=economias circulares
a erosão | l'érosion | A erosão está a destruir o litoral aos poucos. | L'érosion détruit lentement la côte. | g? | pl=erosões
o evento climático extremo | le phénomène météo extrême | Eventos climáticos extremos estão mais frequentes último-nos anos. | Les phénomènes météo extrêmes se multiplient ces dernières années. | pl=eventos climáticos extremos
a garra | la griffe | O gato recolheu as unhas. | Le chat a rentré ses griffes. | g? | ex?
o hidrogénio | l'hydrogène | O comboio anda a hidrogénio. | Le train roule à l'hydrogène.
o hábitat | l'habitat | Esta floresta é o hábitat de muitas espécies. | Cette forêt est l'habitat de nombreuses espèces animales.
o mamífero | le mammifère | A baleia é um mamífero, não um peixe. | La baleine est un mammifère, pas un poisson.
a migração das aves | la migration des oiseaux | A migração das aves começa em setembro. | La migration des oiseaux commence en septembre. | g? | pl=migrações das aves
o morcego | la chauve-souris | O morcego caça insetos à noite. | La chauve-souris chasse les insectes la nuit.
a mudança climática | le changement climatique | A mudança climática altera o tempo no mundo inteiro. | Le changement climatique modifie le temps dans le monde entier. | g? | pl=mudanças climáticas
a neutralidade | la neutralité | Buscam a neutralidade de carbono em 2040. | Ils visent la neutralité carbone en 2040.
a neutralidade climática | la neutralité climatique | A neutralidade climática é a meta declarada de muitos países. | La neutralité climatique est l'objectif déclaré de nombreux pays. | g? | pl=neutralidades climáticas
a nevada | la chute de neige | A primeira nevada veio no fim de novembro. | La première neige est tombée fin novembre.
a onda de calor | la canicule | A onda de calor durou onze dias. | La canicule a duré onze jours. | g? | pl=ondas de calor
a onda de frio repentina | le coup de froid | Uma onda de frio destruiu as flores. | Un coup de froid a détruit les fleurs. | pl=ondas de frio repentina | ex?
a pancada de chuva | l'averse | À tarde há pancadas de chuva isoladas. | L'après-midi apporte quelques averses. | g? | pl=pancadas de chuva
o pasto | le pâturage ; saule | As vacas ficam no pasto de maio a outubro. | Les vaches sont au pâturage de mai à octobre.
a pelagem | le pelage, fourrure | No inverno a pelagem fica mais densa. | En hiver, le pelage s'épaissit. | g?
a pista escorregadia | le verglas | Por causa da pista com gelo, dois Autocarro não circularam. | Deux bus ont été supprimés à cause du verglas. | pl=pistas escorregadias | ex?
o plástico descartável | le plastique à usage unique | O plástico descartável é proibido desde 2021. | Le plastique à usage unique est interdit depuis 2021. | pl=plásticos descartáveis
a poluição da água | la pollution de l'eau | A poluição da água vem da agricultura. | La pollution de l'eau vient de l'agriculture. | g? | pl=poluições da água
a política ambiental | la politique environnementale | A política ambiental está no centro do debate. | La politique environnementale est au cœur du débat. | g? | pl=políticas ambientais
a precipitação | la précipitation | A chuva foi muito escassa neste mês. | Les précipitations ont été très faibles ce mois-ci. | pl=precipitações | ex?
a proteção das espécies | la protection des espèces | A proteção das espécies salva muitos animais ameaçados. | La protection des espèces sauve de nombreux animaux menacés. | g? | pl=proteções das espécies
o pântano | le marais | O pântano foi drenado há cem anos. | Le marais a été asséché il y a cent ans.
a qualidade do ar | la qualité de l'air | A qualidade do ar melhorou desde 2015. | La qualité de l'air s'est améliorée depuis 2015. | g? | pl=qualidades do ar
a rachadura | la fissure | Há uma rachadura funda na parede. | Il y a une fissure profonde dans le mur.
a raposa | le renard | À noite a raposa aproxima-se das galinhas de mansinho. | Le renard s'approche des poules la nuit. | g?
a resiliência | la résilience | A resiliência do sistema é baixa. | La résilience du système est faible.
o riacho | le ruisseau | No verão o riacho tem pouca água. | Le ruisseau a peu d'eau en été.
o rochedo | le rocher | No rochedo há uma ruína. | Une ruine se dresse sur le rocher.
o roedor | le rongeur | Camundongos e ratos são roedores. | Souris et rats sont des rongeurs.
o ruminante | le ruminant | As vacas são ruminantes com quatro estômagos. | Les vaches sont des ruminants à quatre estomacs. | g?
o réptil | le reptile | Os répteis aquecem-se ao sol. | Les reptiles se réchauffent au soleil. | pl=répteis
o sistema de energia solar | l'installation solaire | O sistema solar cobre metade do consumo. | L'installation solaire couvre la moitié de la consommation. | pl=sistemas de energia solar | ex?
a transição | la transition | A transição energética custará muito. | La transition énergétique coûtera cher. | pl=transições
a transição energética | la transition énergétique | A transição energética está a demorar mais do que o previsto. | La transition énergétique dure plus longtemps que prévu. | g? | pl=transições energéticas
a águia | l'aigle | A águia voa em círculos bem alto sobre o vale. | L'aigle plane haut au-dessus de la vallée. | g?
""",
"viagens_b2_pt": """
o documento do veículo | la carte grise | O documento do carro está no porta-luvas. | La carte grise est dans la boîte à gants. | pl=documentos do veículo | ex?
a infraestrutura de transportes | l'infrastructure routière | A infraestrutura de transportes precisa de ser modernizada com urgência. | L'infrastructure routière doit être modernisée d'urgence. | g? | pl=infraestruturas de transportes
a linha de balsa | la liaison par ferry | No inverno não há balsa. | En hiver, il n'y a pas de liaison par ferry. | g? | pl=linhas de balsa | ex?
o pernoite | la nuitée | A diária custa oitenta euros. | La nuitée coûte quatre-vingts euros. | g? | ex?
o ponto de Autocarro | l'arrêt de bus | O ponto de Autocarro mudou de lugar. | L'arrêt de bus a été déplacé. | pl=pontos de Autocarro
o quadro de horários | l'horaire | O horário muda no fim de semana. | L'horaire change le week-end. | pl=quadros de horários | ex?
a regra de trânsito | la règle de circulation | Muitos motoristas não conhecem esta regra de trânsito. | Beaucoup d'automobilistes ne connaissent pas cette règle de circulation. | pl=regras de trânsito
a seguro-viagem | l'assurance voyage | Eu sempre faço seguro-viagem. | Je souscris toujours une assurance voyage. | pl=seguros-viagens
o turismo sustentável | le tourisme durable | O turismo sustentável ganha cada vez mais adeptos. | Le tourisme durable gagne de plus en plus d'adeptes. | pl=turismos sustentáveis
""",
"cidade_b2_pt": """
o desenvolvimento urbano | le développement urbain | O desenvolvimento urbano cria novos empregos. | Le développement urbain crée de nouveaux emplois. | pl=desenvolvimentos urbanos
o dique | la digue, le barrage | O dique segura a água. | La digue retient l'eau.
a gentrificação | gentrification | A gentrificação está a mudar muito este bairro. | La gentrification transforme fortement ce quartier. | g? | pl=gentrificações
a muralha da cidade | le rempart | Da muralha ainda restam três torres. | Il reste trois tours du rempart. | pl=muralhas da cidade | ex?
o planeamento urbano | l'urbanisme | Hoje o planeamento urbano prevê mais áreas verdes. | L'urbanisme prend aujourd'hui davantage en compte les espaces verts. | pl=planeamentos urbanos
a praça do mercado | la place du marché | Aos sábados tem feira na praça do mercado. | Le samedi, il y a marché sur la place. | pl=praças do mercado
o pátio dos fundos | l'arrière-cour | No pátio dos fundos ficam as bicicletas. | Les vélos sont dans l'arrière-cour. | pl=pátios dos fundos
o saguão de entrada | le hall d'entrée | No saguão de entrada há um mapa antigo pendurado. | Un vieux plan est accroché dans le hall d'entrée. | pl=saguões de entrada
o terraço na cobertura | la terrasse sur le toit | Do terraço dá para ver o rio. | Depuis la terrasse, on voit la rivière. | pl=terraços nas coberturas | ex?
a torre da igreja | le clocher | A torre da igreja dá para ver de longe. | Le clocher se voit de loin. | g? | pl=torres da igreja
a zona comercial e industrial | la zone d'activité | A zona industrial fica na periferia. | La zone d'activité est en bordure du village. | g? | pl=zonas comerciais e industriais | ex?
""",
"escola_b2_pt": """
a bolsa de pesquisa | la bourse de recherche | A bolsa de pesquisa financia o projeto dela por três anos. | La bourse de recherche finance son projet pendant trois ans. | g? | pl=bolsas de pesquisa
a candidatura | la candidature | A candidatura dela convenceu a comissão na hora. | Sa candidature a immédiatement convaincu la commission. | g?
a dissertação de mestrado | le mémoire de master | A dissertação de mestrado tem oitenta páginas. | Le mémoire fait quatre-vingts pages. | g? | pl=dissertações de mestrado
o doutorado | doctorat | Ele começa o doutorado no ano que vem. | Il commence son doctorat l'année prochaine.
a excursão da escola | le voyage scolaire | A excursão da turma vai para Porto. | Le voyage scolaire va à Porto. | g? | pl=excursões da escola | ex?
o financiamento | le financement | O financiamento vem de um fundo público. | Le financement vient d'un fonds public.
a igualdade de oportunidades | l'égalité des chances | A igualdade de oportunidades na educação continua a ser um objetivo importante. | L'égalité des chances dans l'éducation reste un objectif important. | g? | pl=igualdades de oportunidades
o lanche do recreio | le casse-croûte de la récréation | O lanche do recreio ainda está na mesa. | Le casse-croûte est encore sur la table. | pl=lanches do recreio
a livre-docência | l'habilitation | Depois da livre-docência ela virou professora titular. | Après son habilitation, elle est devenue professeure. | g? | pl=livres-docências
o medo de prova | la peur des examens | Quase todo mundo tem medo de prova. | Presque tout le monde a peur des examens. | pl=medos de prova
a metodologia | la méthodologie | A metodologia está descrita no anexo. | La méthodologie est décrite en annexe.
a moradia estudantil | la résidence universitaire | Na moradia estudantil moram trezentos estudantes. | Trois cents étudiants vivent en résidence. | pl=moradias estudantis
a média das notas | la moyenne générale | A média das notas decide a vaga na universidade. | La moyenne décide de la place à l'université. | g? | pl=médias das notas
o professor responsável pela turma | le professeur principal | O professor da turma liga para os pais. | Le professeur principal appelle les parents. | pl=professores responsáveis pelas turmas | ex?
a prova final | l'examen final | A prova final é em junho. | L'examen final a lieu en juin. | g? | pl=provas finais
a publicação científica | la publication scientifique | A publicação científica saiu em março. | La publication scientifique est parue en mars. | pl=publicações científicas
o pátio da escola | la cour de récréation | No pátio da escola há uma tília antiga. | Un vieux tilleul se dresse dans la cour. | pl=pátios da escola
a replicação | la réplication | A replicação do estudo falhou. | La réplication de l'étude a échoué. | pl=replicações
a secretaria de provas | le service des examens | A secretaria de provas fica aberta até meio-dia. | Le service des examens est ouvert jusqu'à midi. | g? | pl=secretarias de provas
o sistema educacional | le système éducatif | O sistema educacional está a ser muito debatido. | Le système éducatif fait actuellement l'objet de vifs débats. | pl=sistemas educacionais
a tese | la thèse | Ele defende a tese em junho. | Il soutient sa thèse en juin.
a tese de doutorado | la thèse | A tese dela foi elogiada pela faculdade. | Sa thèse a été saluée par la faculté. | g? | pl=teses de doutorado | ex?
a vaga na universidade | la place à l'université | Faltam milhares de vagas em medicina. | Il manque des milliers de places en médecine. | g? | pl=vagas nas universidades | ex?
a variável | la variable | Eles controlam cada variável do experimento. | Ils contrôlent chaque variable de l'expérience. | pl=variáveis
""",
"cultura_b2_pt": """
a ambivalência | l'ambivalence | Ele sente ambivalência diante da mudança. | Il ressent de l'ambivalence face au changement.
o anfitrião | l'hôte (qui reçoit) | O anfitrião quase não conseguiu comer. | L'hôte a à peine eu le temps de manger. | pl=anfitriões
os aplausos | les applaudissements | Os aplausos duraram cinco minutos. | Les applaudissements ont duré cinq minutes.
o batizado | le baptême | O batizado é em maio. | Le baptême a lieu en mai.
o cargo voluntário | la fonction bénévole | O trabalho voluntário no clube dá muita alegria a ele. | Sa fonction bénévole dans l'association lui apporte beaucoup de joie. | pl=cargos voluntários | ex?
a cerimónia | la cérémonie | A cerimónia durou cerca de uma hora. | La cérémonie a duré environ une heure. | g?
a classe social | la classe sociale | A classe social influencia a saúde. | La classe sociale influence la santé. | pl=classes sociais
a coesão | la cohésion | A coesão do grupo rompeu-se. | La cohésion du groupe s'est rompue. | pl=coesões
a coleção | la collection | A coleção dele tem trezentos discos. | Sa collection compte trois cents disques. | g? | pl=coleções
a composição | la composition | Esta composição dura mais de uma hora. | Cette composition dure plus d'une heure. | pl=composições
a comunidade | la communauté | Esta comunidade ajuda-se mutuamente. | Cette communauté se soutient mutuellement.
o costumes | le folklore/coutumes | Em algumas regiões os costumes antigos resistem. | Dans certaines régions, de vieilles coutumes persistent. | pl=costumes
a crítica literária | la critique littéraire | A crítica literária ignorou o livro. | La critique littéraire a ignoré le livre. | pl=críticas literárias
o desenraizamento | le déracinement | Ele fala do desenraizamento dos emigrantes. | Il parle du déracinement des émigrés.
o desfecho | le dénouement | O desfecho decepciona alguns. | Le dénouement déçoit certains.
o enterro | l'enterrement | Mais de cem pessoas foram ao enterro. | Plus de cent personnes sont venues à l'enterrement.
o estereótipo | le stéréotype | O estereótipo persiste na publicidade. | Le stéréotype persiste dans la publicité.
o estilo narrativo | le style narratif | O estilo narrativo dele é seco. | Son style narratif est sec. | pl=estilos narrativos
a estética | l'esthétique | A estética do prédio divide opiniões. | L'esthétique du bâtiment divise.
o evento | la manifestation, événement | Com chuva o evento é cancelado. | La manifestation est annulée en cas de pluie.
a festa de aniversário | la fête d'anniversaire | A festa de aniversário foi no jardim. | La fête d'anniversaire était dans le jardin. | g? | pl=festas de aniversário
a festividade | festivité | A festividade atraiu muitos convidados. | La festivité a attiré de nombreux invités. | g?
a geração perdida | la génération perdue | Chamam de geração perdida os que foram embora. | Ils appellent génération perdue ceux qui sont partis. | pl=gerações perdidas
o gosto | le goût | Gosto não se discute. | Des goûts on ne discute pas.
a harmonia | l'harmonie | Há harmonia entre cor e forma. | Il y a une harmonie entre couleur et forme.
a jardinagem | le jardinage | Mexer no jardim relaxa mais do que ver televisão. | Le jardinage détend plus que la télévision. | ex?
a melancolia | la mélancolie | Há melancolia na música dele. | Il y a de la mélancolie dans sa musique.
a mobilidade social | la mobilité sociale | A mobilidade social desacelerou. | La mobilité sociale s'est ralentie. | pl=mobilidades sociais
o movimento artístico | le courant artistique | Este movimento artístico influenciou muitos artistas depois. | Ce courant artistique a influencé de nombreux artistes ultérieurs. | pl=movimentos artísticos
o narrador | le narrateur | O narrador mente para o leitor. | Le narrateur ment au lecteur.
a norma social | la norme sociale | A norma social mudou em vinte anos. | La norme sociale a changé en vingt ans. | pl=normas sociais
a nostalgia | la nostalgie | Ele sente nostalgia daqueles verões. | Il a la nostalgie de ces étés-là.
a perplexidade | le désarroi | A notícia causou perplexidade. | La nouvelle a causé du désarroi.
o ponto de vista | le point de vue | O ponto de vista muda a cada capítulo. | Le point de vue change à chaque chapitre. | pl=pontos de vista
o rascunho | le projet, esquisse | A equipa descarta o primeiro rascunho. | L'équipe rejette le premier projet.
a realização pessoal | l'épanouissement personnel | Pintar significa para ela uma verdadeira realização pessoal. | Peindre représente pour elle un véritable épanouissement personnel. | g? | pl=realizações pessoais
o remorso | le remords | Resta a ele um pequeno remorso. | Il lui reste un petit remords.
a resignação | la résignation | Ele aceitou com resignação. | Il l'a accepté avec résignation. | pl=resignações
o simbolismo | le symbolisme | O simbolismo da água percorre o romance. | Le symbolisme de l'eau parcourt le roman.
a sociologia | la sociologie | A sociologia estuda essas mudanças. | La sociologie étudie ces changements.
a textura visual | la texture visuelle | A textura visual do muro atrai o olhar. | La texture visuelle du mur attire l'œil. | pl=texturas visuais
a torta | le gâteau (à étages) | Ainda sobrou um quarto da torta. | Un quart du gâteau reste encore. | g?
o ócio | le loisir, temps libre | Falta a ele tranquilidade para ler. | Il lui manque le loisir de lire. | ex?
""",
"desporto_b2_pt": """
o adversário | l'adversaire | O adversário simplesmente foi melhor. | L'adversaire était tout simplement meilleur.
o desporto de alto rendimento | le sport de haut niveau | O desporto de alto rendimento exige muita disciplina. | Le sport de haut niveau exige une discipline stricte. | pl=desportos de alto rendimento
o desporto de resistência | le sport d'endurance | Desporto de resistência melhora a saúde do coração. | Le sport d'endurance améliore la santé cardiaque. | pl=desportos de resistência
a modalidade | la discipline sportive | Esta modalidade exige muita concentração. | Cette discipline sportive demande beaucoup de concentration.
a sessão de treino | la séance d'entraînement | Três treinos por semana bastam. | Trois séances par semaine suffisent. | g? | pl=sessões de treino | ex?
""",
"media_b2_pt": """
a automação | l'automatisation | A automação eliminou tarefas repetitivas. | L'automatisation a supprimé des tâches répétitives. | pl=automações
a cibersegurança | la cybersécurité | A cibersegurança está cada vez mais importante para as empresas. | La cybersécurité devient de plus en plus importante pour les entreprises. | g?
a coletiva de imprensa | la conférence de presse | A coletiva de imprensa durou dez minutos. | La conférence de presse a duré dix minutes. | pl=coletivas de imprensa
a confiabilidade | la fiabilité | A confiabilidade do sistema é alta. | La fiabilité du système est élevée.
a cópia de segurança | la copie de sauvegarde | Eu automatizaria as cópias de segurança. | Moi, j'automatiserais les sauvegardes. | g? | pl=cópias de segurança
a desinformação | la désinformation | A desinformação espalha-se muito rápido. | La désinformation se répand très vite. | pl=desinformações
a digitalização | la numérisation | A digitalização muda o nosso dia a dia profundamente. | La numérisation transforme fondamentalement notre quotidien. | g? | pl=digitalizações
o furo | le scoop | Eles conseguiram o furo do ano. | Ils ont obtenu le scoop de l'année.
a inteligência artificial | l'intelligence artificielle | A inteligência artificial escreve o rascunho. | L'intelligence artificielle écrit le brouillon. | pl=inteligências artificiais
a ironia | l'ironie | Ele não captou a ironia do comentário. | Il n'a pas saisi l'ironie du commentaire.
o jornalismo | le journalisme | O jornalismo investigativo custa caro. | Le journalisme d'investigation coûte cher.
a metáfora | la métaphore | A metáfora do rio repete-se. | La métaphore du fleuve revient.
o navegador | le navigateur |  |  | ex=?
o noticiário | les informations, journal | O noticiário começa às oito. | Le journal est à huit heures.
a persuasão | la persuasion | Persuasão não é manipulação. | La persuasion n'est pas la manipulation. | pl=persuasões
a proteção de dados | la protection des données |  |  | g? | pl=proteções de dados | ex=?
a redação | la rédaction | A redação fecha às onze. | La rédaction ferme à onze heures. | pl=redações
a retórica | la rhétorique | A retórica dele convence sem argumentos. | Sa rhétorique convainc sans arguments.
a réplica | la réplique | A réplica dele foi imediata. | Sa réplique a été immédiate.
a supervisão | la supervision | É preciso supervisão humana. | Il faut une supervision humaine. | pl=supervisões
a transparência algorítmica | la transparence algorithmique | Exigem transparência algorítmica. | Ils exigent la transparence algorithmique. | pl=transparências algorítmicas
a veracidade | la véracité | Eles verificam a veracidade de cada dado. | Ils vérifient la véracité de chaque donnée.
o viés algorítmico | le biais algorithmique | O viés algorítmico foi detectado tarde. | Le biais algorithmique a été détecté tard. | pl=viéss algorítmicos
o viés editorial | le biais éditorial | O viés editorial aparece na manchete. | Le biais éditorial se voit dans le titre. | pl=viéss editoriais
a ênfase retórica | l'emphase rhétorique | A ênfase retórica cansa o ouvinte. | L'emphase rhétorique fatigue l'auditeur. | pl=ênfases retóricas
""",
"dinheiro_b2_pt": """
a caderneta de poupança | le livret d'épargne | A poupança quase não rende mais juros. | Le livret ne rapporte presque plus d'intérêts. | g? | pl=cadernetas de poupança | ex?
a comparação de preços | la comparaison de prix | Comparar preços quase sempre vale a pena. | Une comparaison de prix vaut presque toujours la peine. | pl=comparações de preços | ex?
o comportamento de consumo | le comportement de consommation | O comportamento de consumo dos jovens mudou muito. | Le comportement de consommation des jeunes a beaucoup changé. | pl=comportamentos de consumo
o déficit | le déficit | O déficit caiu pela metade. | Le déficit s'est réduit de moitié.
a dívida pública | la dette publique | A dívida pública ultrapassa cem por cento. | La dette publique dépasse cent pour cent. | pl=dívidas públicas
a economias | l'économie | As minhas economias dão para uma emergência. | Mes économies suffisent pour une urgence. | pl=economias
o estímulo | la relance | O estímulo chegou em abril. | La relance est arrivée en avril.
o extrato bancário | le relevé de compte | No extrato está a faltar um lançamento. | Il manque une écriture sur le relevé. | pl=extratos bancários | ex?
a macroeconomia | la macroéconomie | A macroeconomia explica pouco o cotidiano. | La macroéconomie explique peu le quotidien.
a pechincha | la bonne affaire | O casaco foi uma verdadeira pechincha. | Le manteau était une vraie bonne affaire. | g?
o poder aquisitivo | le pouvoir d'achat | O poder de compra caiu dois pontos. | Le pouvoir d'achat a baissé de deux points. | pl=poderes aquisitivos | ex?
a produtividade | la productivité | A produtividade não cresce desde 2008. | La productivité ne croît plus depuis 2008.
o produto interno bruto | le produit intérieur brut | O produto interno bruto cresceu um por cento. | Le produit intérieur brut a crû d'un pour cent. | pl=produtos internos brutos
a recessão | la récession | A recessão durou cinco trimestres. | La récession a duré cinq trimestres. | pl=recessões
o troco | la monnaie (rendue) | Ela deu-me troco a menos. | Elle m'a rendu trop peu de monnaie.
o vale-presente | le bon d'achat | O vale ainda vale até o fim de maio. | Le bon est valable jusqu'à fin mai. | g? | pl=vales-presentes | ex?
""",
"sentimentos_b2_pt": """
a ambição | l'ambition | A ambição dele o motiva todo dia. | Son ambition le pousse chaque jour. | pl=ambições
a angústia | l'angoisse | Ele sentiu uma angústia difícil de explicar. | Il a ressenti une angoisse difficile à expliquer.
a autorreflexão | l'introspection | A autorreflexão ajuda a aprender com os erros. | L'introspection aide à apprendre de ses erreurs. | g? | pl=autorreflexões
o carinho | l'affection | Ele diz isso com carinho. | Il le dit avec affection.
o consolo | la consolation | Foi um consolo saber a tempo. | Ce fut une consolation de le savoir à temps.
o desespero | le désespoir | Por desespero ela acabou ligando para ele. | Par désespoir, elle a fini par l'appeler.
o dom | le don | Ela tem o dom de saber ouvir. | Elle a le don de bien écouter.
a empatia | l'empathie | Empatia é uma qualidade importante para esta profissão. | L'empathie est une qualité importante pour ce métier. | g?
o empenho | l'acharnement | Ele conseguiu à força de empenho. | Il l'a obtenu à force d'acharnement.
o espanto | l'étonnement | Ele olhou-nos com espanto. | Il nous a regardés avec étonnement.
o falatório | le bavardage, les racontars | Não liga para o falatório das pessoas. | N'écoute pas les racontars des gens.
a impaciência | l'impatience | A impaciência dele era bem perceptível. | Son impatience était nettement perceptible. | g?
o impulso | l'impulsion | Ele comprou por impulso. | Il l'a acheté sur un coup de tête.
a incerteza | l'incertitude | A incerteza freia o investimento. | L'incertitude freine l'investissement.
o indício | l'indice | Há indícios de melhora. | Il y a des indices d'amélioration.
a inquietação | l'inquiétude | Há certa inquietação no bairro. | Il y a une certaine inquiétude dans le quartier. | pl=inquietações
o instinto | l'instinct | Ele confiou no instinto. | Il s'est fié à son instinct.
a mesa de cabeceira | la table de nuit | Deixo o livro na mesa de cabeceira antes de dormir. | Je pose le livre sur la table de nuit avant de dormir. | pl=mesas de cabeceira
a modéstia | la modestie | Apesar do sucesso, ela continua muito humilde. | Malgré son succès, elle reste pleine de modestie. | g? | ex?
a probabilidade | la probabilité |  |  | ex=?
a suposição | la supposition | É uma suposição, não um facto. | C'est une supposition, pas un fait. | pl=suposições
a suspeita | le soupçon | Tenho a suspeita de que ele já sabia. | J'ai le soupçon qu'il le savait déjà.
""",
"sociedade_b2_pt": """
a abstenção | l'abstention | A abstenção ultrapassou quarenta por cento. | L'abstention a dépassé quarante pour cent. | pl=abstenções
a aliança | l'alliance | A aliança foi assinada em 1949. | L'alliance a été signée en 1949.
a antropologia | l'anthropologie | A antropologia estuda essas práticas. | L'anthropologie étudie ces pratiques.
o ato administrativo | l'acte administratif | É possível entrar na justiça contra um ato administrativo. | On peut contester un acte administratif en justice. | pl=atos administrativos
a bancada | le groupe parlementaire | A bancada vota em bloco contra. | Le groupe vote unanimement contre. | g?
a cadeia de suprimentos | la chaîne d'approvisionnement | Uma única fábrica travou toda a cadeia de suprimentos. | Une seule usine a bloqué toute la chaîne d'approvisionnement. | pl=cadeias de suprimentos
a campanha eleitoral | la campagne électorale | A campanha eleitoral dura seis semanas. | La campagne électorale dure six semaines. | g? | pl=campanhas eleitorais
a censura | la censure | A censura desapareceu em 1978. | La censure a disparu en 1978.
o chanceler | le chancelier | O chanceler fala hoje à noite. | Le chancelier parle ce soir.
a competitividade | la compétitivité | A competitividade do setor caiu. | La compétitivité du secteur a baissé.
a condecoração | la décoration, l'ordre | Ele recebeu uma condecoração pela sua coragem. | Il a reçu une décoration pour son courage. | pl=condecorações
o consenso | le consensus | Eles buscam um consenso amplo. | Ils cherchent un large consensus.
a crítica social | la critique sociale | Esta crítica social provocou debates acalorados. | Cette critique sociale a déclenché de vifs débats. | pl=críticas sociais
a declaração universal | la déclaration universelle | A Declaração Universal é de 1948. | La Déclaration universelle date de 1948. | pl=declarações universais
o deslocado | la personne déplacée | Os deslocados vivem no sul. | Les personnes déplacées vivent dans le sud.
a deslocalização | la délocalisation | A deslocalização fechou a fábrica. | La délocalisation a fermé l'usine. | pl=deslocalizações
a dignidade | la dignité | A dignidade da pessoa é inviolável. | La dignité de la personne est inviolable.
a diplomacia | la diplomatie | A diplomacia evitou o conflito. | La diplomatie a évité le conflit.
o distrito eleitoral | la circonscription | Neste distrito eleitoral foi apertado. | Dans cette circonscription, cela s'est joué de peu. | pl=distritos eleitorais
a etnia | l'ethnie | Quatro etnias convivem na região. | Quatre ethnies cohabitent dans la région.
o federalismo | le fédéralisme | A Alemanha baseia-se no princípio do federalismo. | L'Allemagne repose sur le principe du fédéralisme.
a geopolítica | la géopolitique | A geopolítica da região é complexa. | La géopolitique de la région est complexe.
a globalização | la mondialisation | A globalização mudou o comércio. | La mondialisation a changé le commerce. | pl=globalizações
a impunidade | l'impunité | Denunciam a impunidade dos crimes. | Ils dénoncent l'impunité des délits.
a interdependência | l'interdépendance | A interdependência entre os países cresceu. | L'interdépendance entre pays a crû.
o legado | l'héritage culturel | O legado indígena continua vivo. | L'héritage indigène reste vivant.
a legislação | la législation | A legislação ficou mais rígida último-nos anos. | La législation a été durcie ces dernières années. | g? | pl=legislações
a Lei Fundamental | la Loi fondamentale | Isso está no primeiro artigo da Lei Fundamental. | C'est écrit au premier article de la Loi fondamentale. | pl=Leis Fundamentais
o mandato | le mandat | O mandato dura quatro anos. | Le mandat dure quatre ans.
a mediação | la médiation | A mediação durou seis meses. | La médiation a duré six mois. | pl=mediações
a mestiçagem | le métissage | A mestiçagem marcou a cozinha local. | Le métissage a marqué la cuisine locale.
o ministério | le ministère | O ministério está a analisar o pedido. | Le ministère examine la demande.
a multinacional | la multinationale | A multinacional opera em cem países. | La multinationale opère dans cent pays.
o ocupante de cargo público | le titulaire d'une charge publique | Quem ocupa cargo público está sujeito a regras especiais. | Les titulaires de charges publiques ont des règles à part. | g? | pl=ocupantes de cargo público | ex?
o parentesco simbólico | la parenté symbolique | O parentesco simbólico une os vizinhos. | La parenté symbolique unit les voisins. | pl=parentescos simbólicos
a participação cidadã | la participation citoyenne | A participação cidadã fortalece a confiança na política. | La participation citoyenne renforce la confiance envers la politique. | g? | pl=participações cidadãs
o plebiscito | le référendum | Houve um plebiscito sobre a questão. | La question a fait l'objet d'un référendum.
a proteção legal | la protection légale | Ele pediu amparo ao tribunal. | Il a demandé protection au tribunal. | pl=proteções legais | ex?
o referendo | le référendum | O referendo foi realizado em junho. | Le référendum a eu lieu en juin.
o ritual | le rituel | O ritual repete-se a cada colheita. | Le rituel se répète à chaque récolte.
a sanção | la sanction | As sanções duraram dois anos. | Les sanctions ont duré deux ans. | pl=sanções
a separação dos poderes | la séparation des pouvoirs | A separação dos poderes é um princípio básico. | La séparation des pouvoirs est un principe fondamental. | pl=separações dos poderes
a soberania | la souveraineté | Eles defendem a sua soberania sobre a água. | Ils défendent leur souveraineté sur l'eau.
a tarifa alfandegária | le droit de douane | A tarifa alfandegária encarece a importação. | Le droit de douane renchérit l'importation. | pl=tarifas alfandegárias
a tensão diplomática | la tension diplomatique | A tensão diplomática durou um mês. | La tension diplomatique a duré un mois. | pl=tensões diplomáticas
o União | la fédération, l'alliance | A União Europeia é formada por vinte e sete Estados. | L'Union européenne compte vingt-sept États. | pl=Uniões
o órgão público | l'administration, service public | A repartição responde depois de oito semanas. | L'administration répond au bout de huit semaines. | pl=órgãos públicos | ex?
""",
"ideias_b2_pt": """
a ambiguidade | l'ambiguïté | A ambiguidade do texto é intencional. | L'ambiguïté du texte est voulue.
a bioética | la bioéthique | A bioética acompanha cada avanço. | La bioéthique accompagne chaque avancée.
o ceticismo | le scepticisme | Ele recebeu a notícia com ceticismo. | Il l'a reçu avec scepticisme.
a cláusula | la clause | A sexta cláusula é a chave. | La sixième clause est la clé.
a coerência | la cohérence | Falta coerência entre os dados. | Il manque de la cohérence entre les données.
o compromisso mútuo | l'engagement mutuel | Eles assinaram um compromisso mútuo. | Ils ont signé un engagement mutuel. | pl=compromissos mútuos
o conceito | le concept | O conceito é difícil de traduzir. | Le concept est difficile à traduire.
a concessão | la concession | Ele fez uma concessão importante. | Il a fait une concession importante. | pl=concessões
a condição | la condition | Eles aceitam com uma condição. | Ils acceptent à une condition. | pl=condições
a consciência | la conscience | A consciência do problema chegou tarde. | La conscience du problème est venue tard.
o contra-argumento | le contre-argument | O contra-argumento dele foi sólido. | Son contre-argument était solide. | pl=contras-argumentos
a contradição | la contradiction | Há uma contradição no relatório. | Il y a une contradiction dans le rapport. | pl=contradições
a contrapartida | la contrepartie | Pediram uma contrapartida clara. | Ils ont demandé une contrepartie claire.
a cortesia | la politesse | A cortesia custa pouco. | La politesse ne coûte rien.
o critério | le critère | O critério de seleção é claro. | Le critère de sélection est clair.
o depoimento | le témoignage | O depoimento durou três horas. | Le témoignage a duré trois heures.
o dilema | le dilemme | É um dilema sem saída clara. | C'est un dilemme sans issue claire.
o ensaio clínico | l'essai clinique | O ensaio clínico inclui mil pessoas. | L'essai clinique inclut mille personnes. | pl=ensaios clínicos
o esquecimento | l'oubli | O esquecimento também é uma decisão. | L'oubli est aussi une décision.
o eufemismo | l'euphémisme | Ele usou um eufemismo para não magoar. | Il a usé d'un euphémisme pour ne pas blesser.
a evidência | la preuve | Não há evidência suficiente. | Il n'y a pas assez de preuves.
a existência | l'existence | Ele pergunta-se sobre o sentido da existência. | Il s'interroge sur le sens de l'existence.
a exumação | l'exhumation | A exumação foi feita em abril. | L'exhumation a eu lieu en avril. | pl=exumações
a falácia | le sophisme | É uma falácia muito comum. | C'est un sophisme très courant.
o gene | le gène | Identificaram o gene responsável. | Ils ont identifié le gène responsable.
a genética | la génétique | A genética explica parte do risco. | La génétique explique une partie du risque.
o impasse | l'impasse | As conversas chegaram a um impasse. | Les discussions sont arrivées à une impasse.
a integridade | l'intégrité | A integridade dele nunca esteve em dúvida. | Son intégrité n'a jamais été mise en doute.
o jargão | le jargon | O jargão técnico exclui o leitor. | Le jargon technique exclut le lecteur. | pl=jargões
o limite | la limite | O debate fixa um limite claro. | Le débat fixe une limite claire.
a memória histórica | la mémoire historique | A memória histórica é estudada na escola. | La mémoire historique s'étudie à l'école. | pl=memórias históricas
o moderador | le modérateur | O moderador cortou a intervenção. | Le modérateur a coupé l'intervention.
a moral | la morale | Ele não julga a moral de ninguém. | Il ne juge la morale de personne.
a nuance | la nuance | Há uma nuance importante nessa frase. | Il y a une nuance importante dans cette phrase.
a objetividade | l'objectivité | A objetividade total não existe. | L'objectivité totale n'existe pas.
a objeção | l'objection | Ninguém levantou nenhuma objeção. | Personne n'a soulevé d'objection. | pl=objeções
o paradoxo | le paradoxe | É um paradoxo conhecido. | C'est un paradoxe connu.
o pensador | le penseur | É o pensador mais citado do século. | C'est le penseur le plus cité du siècle.
a polémica | la polémique | A polémica durou uma semana. | La polémique a duré une semaine.
a precisão | la précision | Ele fala com muita precisão. | Il parle avec beaucoup de précision. | pl=precisões
""",
"ideias_b2_pt_2": """
a premissa | la prémisse | A premissa de partida é falsa. | La prémisse de départ est fausse.
o princípio | le principe | Ele age segundo os seus princípios. | Il agit selon ses principes.
a privacidade dos dados | la confidentialité des données | A privacidade dos dados é essencial. | La confidentialité des données est essentielle. | pl=privacidades dos dados
o raciocínio | le raisonnement | O raciocínio dele tem uma falha. | Son raisonnement a une faille.
o registo | le registre | O registo do e-mail é informal demais. | Le registre du courriel est trop informel.
a reparação | la réparation | A lei prevê uma reparação simbólica. | La loi prévoit une réparation symbolique. | pl=reparações
o sinónimo | le synonyme | Procuro um sinónimo mais suave. | Je cherche un synonyme plus doux.
a sutileza | la subtilité | A sutileza perde-se na tradução. | La subtilité se perd à la traduction.
o tato | le tact | Ele disse isso com muito tato. | Il l'a dit avec beaucoup de tact.
o tom | le ton | Não gostei do tom dele. | Je n'ai pas aimé son ton.
a transparência | la transparence | Exigem mais transparência nas contas. | Ils exigent plus de transparence dans les comptes.
a vala | la fosse | Localizaram a vala em 2019. | Ils ont localisé la fosse en 2019.
a vez de falar | le tour de parole | Ele respeita a vez de falar. | Il respecte le tour de parole. | pl=vezes de falar
o viés | le biais | O viés do estudo é evidente. | Le biais de l'étude est évident. | pl=viéss
a ética | l'éthique | A ética profissional é pouco ensinada. | L'éthique professionnelle s'enseigne peu.
a ênfase | l'emphase | Ele pôs ênfase na última palavra. | Il a mis l'emphase sur le dernier mot.
""",
"tempo_b2_pt": """
o ano bissexto | l'année bissextile | No ano bissexto fevereiro tem 29 dias. | En année bissextile, février a 29 jours. | pl=anos bissextos
a antecedência | le temps de préparation | Precisamos de duas semanas de antecedência. | Il nous faut deux semaines de préparation. | g?
o atraso acumulado | le retard accumulé | As pendências aumentam toda semana. | Le retard s'accumule chaque semaine. | pl=atrasos acumulados | ex?
a fase de transição | la phase de transition | A fase de transição foi muito exigente para todos. | La phase de transition a été très exigeante pour tous. | g? | pl=fases de transição
o fuso horário | le fuseau horaire | Há seis fusos horários entre nós. | Six fuseaux horaires nous séparent. | pl=fusos horários
o intervalo de tempo | le laps de temps | Nesse intervalo de tempo muita coisa mudou. | Dans ce laps de temps, beaucoup a changé. | pl=intervalos de tempo
""",
"quotidiano_b2_pt": """
o comprimento | la longueur | O comprimento da sala é de seis metros. | La longueur de la pièce est de six mètres.
o contorno | le contour | Dá para adivinhar os contornos na neblina. | On devine les contours dans le brouillard.
a cota | le quota/taux | A sobrepesca é mais antiga do que qualquer cota. | La surpêche est plus ancienne que tout quota. | g?
o cálculo | le calcul | O cálculo deu um resultado surpreendente. | Le calcul a donné un résultat surprenant.
o degradê | le dégradé de couleurs | O degradê vai do azul ao cinza. | Le dégradé va du bleu au gris.
a desvantagem | l'inconvénient | A única desvantagem é o preço. | Le seul inconvénient, c'est le prix.
a diferença | la différence, écart | A diferença é de exatamente doze euros. | L'écart est exactement de douze euros. | g?
o elemento | l'élément | A água é formada por dois elementos. | L'eau est composée de deux éléments.
a estimativa | l'estimation | Esta estimativa baseia-se em dados antigos. | Cette estimation repose sur des données anciennes.
a fração | la fraction ; fracture | Um terço é uma fração. | Un tiers est une fraction. | pl=frações
a largura | la largeur | Com esta largura o armário não cabe. | À cette largeur, l'armoire ne passe pas.
a perspectiva | la perspective | A perspectiva deste quadro é incomum. | La perspective de ce tableau est inhabituelle. | g?
a xadrez | le carreau | Uma saia xadrez vermelha. | Une jupe à carreaux rouges. | g?
""",
}
