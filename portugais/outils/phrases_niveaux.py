# -*- coding: utf-8 -*-
"""Les phrases ecrites a la main pour les cartes A2-C1 que l'extraction avait
laissees sans phrase, ou avec une phrase qui ne contenait pas le mot (30 oct.
2026). SOURCE : niveaux.py les prend a la place de celle de la liste.

Une ligne : « classe | mot | phrase portugaise | traduction francaise ».
Classe : nom (le mot sans article), verbe, adj, adv, expr.
« — » a la place de la phrase ECARTE le mot : bresilien sans equivalent simple
au Portugal (atendente, quitinete, Copa do Mundo...), glose qui n'est pas un mot
(« que trabalha »), genre ou forme fautifs dans la liste, doublon d'un mot de
l'A1. Il reste liste dans rapport_niveaux.txt (ECARTE).
BROUILLON : a faire relire par un lusophone du Portugal.
"""

PHRASES = """
# ------------------------------------------------------------------ A2
nom | ementa de bebidas | Pode trazer-me a ementa de bebidas, por favor? | Vous pouvez m'apporter la carte des boissons, s'il vous plaît ?
nom | feijão | Hoje há sopa de feijão ao almoço. | Aujourd'hui, il y a une soupe de haricots au déjeuner.
nom | peneira | Passa a farinha pela peneira. | Passe la farine au tamis.
nom | pãozinho | — |
nom | refrigerante | Prefiro água a um refrigerante. | Je préfère l'eau à un soda.
nom | caixote do lixo | Deita o papel no caixote do lixo. | Jette le papier dans la poubelle.
nom | caçarola | A carne coze devagar na caçarola. | La viande cuit doucement dans la cocotte.
nom | hall de entrada | Deixa os sapatos no hall de entrada. | Laisse tes chaussures dans le hall d'entrée.
nom | lenço | Tens um lenço? Estou constipado. | Tu as un mouchoir ? Je suis enrhumé.
nom | plano de saúde | — |
nom | fato de banho | Não te esqueças do fato de banho! | N'oublie pas ton maillot de bain !
nom | roupão | Depois do banho, visto o roupão. | Après la douche, je mets mon peignoir.
nom | anão | A Branca de Neve vive com sete anões. | Blanche-Neige vit avec sept nains.
nom | burro | O burro carrega a lenha até à aldeia. | L'âne porte le bois jusqu'au village.
nom | bomba de gasolina | Paramos na próxima bomba de gasolina. | Nous nous arrêtons à la prochaine station-service.
nom | hospedeira de bordo | A hospedeira de bordo serve o café. | L'hôtesse de l'air sert le café.
nom | itinerário | O itinerário passa por Évora e por Beja. | L'itinéraire passe par Évora et par Beja.
nom | anfiteatro | A aula é no anfiteatro dois. | Le cours a lieu dans l'amphithéâtre deux.
nom | restaurante universitário | — |
nom | anjo | No topo da árvore de Natal há um anjo. | En haut du sapin de Noël, il y a un ange.
nom | filme ou livro policial | — |
nom | jogo de tabuleiro | Ao domingo jogamos um jogo de tabuleiro. | Le dimanche, nous jouons à un jeu de société.
nom | véspera de ano-novo | — |
nom | voleibol | No verão jogamos voleibol na praia. | En été, nous jouons au volley-ball sur la plage.
nom | conta poupança | Abri uma conta poupança para as férias. | J'ai ouvert un compte épargne pour les vacances.
nom | cupom fiscal | — |
nom | feira de antiguidades | Comprei este candeeiro na feira de antiguidades. | J'ai acheté cette lampe au marché aux puces.
nom | caráter | Ela tem um caráter forte. | Elle a un caractère fort.
nom | cartão de cidadão | Mostre-me o cartão de cidadão, por favor. | Montrez-moi votre carte d'identité, s'il vous plaît.
nom | oval | — |
nom | resto | Guardo o resto do bolo para amanhã. | Je garde le reste du gâteau pour demain.
verbe | possuir | A família possui uma quinta no Douro. | La famille possède une propriété dans le Douro.
adj | apressado | Hoje estou muito apressado. | Aujourd'hui, je suis très pressé.
adj | bem organizado | O horário está bem organizado. | L'emploi du temps est bien organisé.
adj | bem-vindo | Bem-vindo a Lisboa! | Bienvenue à Lisbonne !
adj | burro | Não sejas burro, pensa um bocado! | Ne sois pas bête, réfléchis un peu !
adj | chinês | Jantámos num restaurante chinês. | Nous avons dîné dans un restaurant chinois.
adj | espesso | O molho está espesso demais. | La sauce est trop épaisse.
adj | festivo | O ambiente na rua é muito festivo. | L'ambiance dans la rue est très festive.
adj | hábil | Ele é muito hábil com as mãos. | Il est très habile de ses mains.
adj | incomum | Este calor é incomum em outubro. | Cette chaleur est inhabituelle en octobre.
adj | louco | Isso é uma ideia louca! | C'est une idée folle !
adj | morto | Encontrei um pássaro morto no jardim. | J'ai trouvé un oiseau mort dans le jardin.
adj | nascido | Sou nascido e criado no Porto. | Je suis né et j'ai grandi à Porto.
adj | orgulhoso | Os pais estão orgulhosos da filha. | Les parents sont fiers de leur fille.
adj | pouco claro | A explicação ainda está pouco clara. | L'explication n'est pas encore claire.
adj | pouco nítido | A fotografia está pouco nítida. | La photo n'est pas très nette.
adj | que trabalha | — |
adj | repousante | Foi um fim de semana muito repousante. | Ce fut un week-end très reposant.
adj | solitário | O farol fica num sítio solitário. | Le phare se trouve dans un endroit solitaire.
adv | com que frequência | Com que frequência vais ao ginásio? | Combien de fois vas-tu à la salle de sport ?
adv | de volta | Estou de volta às seis. | Je suis de retour à six heures.
adv | onde quer que | Onde quer que vás, liga-me. | Où que tu ailles, appelle-moi.
adv | para onde | Para onde vais nas férias? | Où vas-tu en vacances ?
adv | quanto tempo | Quanto tempo demora a viagem? | Combien de temps dure le voyage ?
expr | quanto tempo | Olá! Há quanto tempo! | Salut ! Ça fait longtemps !

# ------------------------------------------------------------------ B1
nom | licença-maternidade | Ela está de licença-maternidade até março. | Elle est en congé de maternité jusqu'en mars.
nom | mamãe | — |
nom | nova geração | A nova geração de músicos é muito talentosa. | La nouvelle génération de musiciens est très talentueuse.
nom | atendente | — |
nom | carta comercial | Aprendemos a escrever uma carta comercial. | Nous apprenons à écrire une lettre commerciale.
nom | empresários | Os empresários reuniram-se com o ministro. | Les chefs d'entreprise se sont réunis avec le ministre.
nom | fim do expediente | No fim do expediente vamos beber um café. | À la fin de la journée de travail, nous allons boire un café.
nom | formação continuada | — |
nom | gerência | A gerência pede desculpa pelo incómodo. | La direction vous prie d'excuser la gêne.
nom | talhante | O talhante corta a carne à minha frente. | Le boucher coupe la viande devant moi.
nom | teletrabalho | Às sextas faço teletrabalho. | Le vendredi, je fais du télétravail.
nom | cervejaria ao ar livre | — |
nom | requeijão fresco | — |
nom | banheira | — |
nom | cabana | Passámos a noite numa cabana na serra. | Nous avons passé la nuit dans une cabane à la montagne.
nom | quitinete | — |
nom | tubo | O tubo da máquina de lavar está entupido. | Le tuyau de la machine à laver est bouché.
nom | valor do renda | — |
nom | chamada de emergência | Para uma chamada de emergência, ligue 112. | Pour un appel d'urgence, composez le 112.
nom | fármaco | Este fármaco só se vende com receita. | Ce médicament ne se vend que sur ordonnance.
nom | gesso | Ele tem o braço engessado: vai ficar com o gesso um mês. | Il a le bras dans le plâtre : il gardera le plâtre un mois.
nom | histórico médico | O médico consultou o meu histórico médico. | Le médecin a consulté mon dossier médical.
nom | ingestão | — |
nom | médico especialista | O médico de família mandou-me a um médico especialista. | Le médecin de famille m'a envoyé chez un spécialiste.
nom | pasta de dentes | Acabou a pasta de dentes. | Il n'y a plus de dentifrice.
nom | urgências | Fomos às urgências às duas da manhã. | Nous sommes allés aux urgences à deux heures du matin.
nom | vacinação | A vacinação contra a gripe começa em outubro. | La vaccination contre la grippe commence en octobre.
nom | uniforme | Os alunos daquele colégio usam uniforme. | Les élèves de ce collège portent un uniforme.
nom | gabinete | O diretor está no gabinete. | Le directeur est dans son bureau.
nom | laje | A laje da varanda precisa de arranjo. | La dalle du balcon a besoin d'être réparée.
nom | lixo volumoso | A câmara recolhe o lixo volumoso às quintas. | La mairie ramasse les encombrants le jeudi.
nom | rebanho | O pastor leva o rebanho para a serra. | Le berger mène le troupeau à la montagne.
nom | vaga-lume | No verão há vaga-lumes no jardim. | En été, il y a des lucioles dans le jardin.
nom | bomba de ar | Tens uma bomba de ar? O pneu está vazio. | Tu as une pompe ? Le pneu est à plat.
nom | estação central | O comboio para o Porto parte da estação central. | Le train pour Porto part de la gare centrale.
nom | luz traseira | — |
nom | meio de transporte | O elétrico é o meu meio de transporte preferido. | Le tram est mon moyen de transport préféré.
nom | portagem | Nesta autoestrada paga-se portagem. | Sur cette autoroute, on paie un péage.
nom | vivência | Viver no estrangeiro foi uma grande vivência. | Vivre à l'étranger a été une grande expérience.
nom | corpo de bombeiros | — |
nom | guarda-volumes | — |
nom | proximidade | A proximidade do mar torna a cidade agradável. | La proximité de la mer rend la ville agréable.
nom | rua transversal | A farmácia fica numa rua transversal. | La pharmacie se trouve dans une rue transversale.
nom | geografia | A geografia de Portugal é muito variada. | La géographie du Portugal est très variée.
nom | segunda língua | O inglês é a minha segunda língua. | L'anglais est ma langue seconde.
nom | banquete | Depois do casamento houve um grande banquete. | Après le mariage, il y a eu un grand banquet.
nom | discoteca | Ao sábado vamos à discoteca. | Le samedi, nous allons en discothèque.
nom | felicitação | Recebi muitas felicitações pelo meu aniversário. | J'ai reçu beaucoup de félicitations pour mon anniversaire.
nom | isqueiro | Tens um isqueiro para acender a vela? | Tu as un briquet pour allumer la bougie ?
nom | piquenique | Fizemos um piquenique no parque. | Nous avons fait un pique-nique dans le parc.
nom | Copa do Mundo | — |
nom | equipa de futebol | O meu irmão joga numa equipa de futebol. | Mon frère joue dans une équipe de football.
nom | equipa do coração | O Benfica é a minha equipa do coração. | Benfica est mon club de cœur.
nom | esqui | Nunca fiz esqui na Serra da Estrela. | Je n'ai jamais fait de ski dans la Serra da Estrela.
nom | piscina coberta | No inverno nado na piscina coberta. | En hiver, je nage à la piscine couverte.
nom | concerto de calouros | — |
nom | disco rígido | Guardei as fotografias no disco rígido. | J'ai enregistré les photos sur le disque dur.
nom | ilustração | O livro tem ilustrações muito bonitas. | Le livre a de très belles illustrations.
nom | radiodifusão | A radiodifusão começou em Portugal nos anos vinte. | La radiodiffusion a commencé au Portugal dans les années vingt.
nom | telefone fixo | Já quase ninguém tem telefone fixo. | Presque plus personne n'a de ligne fixe.
nom | telefone telemóvel | — |
nom | unidade de disco | — |
nom | aval | O banco pediu um aval para o empréstimo. | La banque a demandé une caution pour le prêt.
nom | cartão de débito | Pago tudo com o cartão de débito. | Je paie tout avec ma carte de débit.
nom | catálogo | Escolhi o sofá no catálogo. | J'ai choisi le canapé dans le catalogue.
nom | divisa | O euro é uma divisa forte. | L'euro est une devise forte.
nom | débito automático | Pago a luz por débito automático. | Je paie l'électricité par prélèvement automatique.
nom | pagamento parcelado | — |
nom | abandono | O abandono de animais é crime. | L'abandon d'animaux est un délit.
nom | abismo | Há um abismo entre ricos e pobres. | Il y a un fossé entre riches et pauvres.
nom | arrombador | — |
nom | conselho tutelar | — |
nom | direito de voto | Em Portugal, o direito de voto começa aos dezoito anos. | Au Portugal, le droit de vote commence à dix-huit ans.
nom | donativo | Fizemos um donativo ao banco alimentar. | Nous avons fait un don à la banque alimentaire.
nom | engajamento | — |
nom | incentivo | O governo dá um incentivo a quem compra um carro elétrico. | Le gouvernement accorde une aide à qui achète une voiture électrique.
nom | morto | O acidente fez dois mortos. | L'accident a fait deux morts.
nom | milénio | O mosteiro tem quase um milénio. | Le monastère a presque mille ans.
nom | retrospectiva | — |
nom | perdão | Peço-te perdão pelo que disse. | Je te demande pardon pour ce que j'ai dit.
nom | pormenor | Conta-me tudo, com todos os pormenores! | Raconte-moi tout, avec tous les détails !
nom | quilograma | Um litro de água pesa um quilograma. | Un litre d'eau pèse un kilogramme.
verbe | atropelar | Um carro quase atropelou o cão. | Une voiture a failli écraser le chien.
verbe | contrair | Contraíram um empréstimo para comprar a casa. | Ils ont contracté un prêt pour acheter la maison.
verbe | decorrer | A reunião decorreu sem problemas. | La réunion s'est déroulée sans problème.
verbe | insultar | Não se deve insultar ninguém. | On ne doit insulter personne.
verbe | pernoitar | Vamos pernoitar em Coimbra. | Nous allons passer la nuit à Coimbra.
verbe | remoer | Não vale a pena remoer o passado. | Ça ne sert à rien de ruminer le passé.
verbe | sacudir | Sacode a toalha na varanda. | Secoue la nappe sur le balcon.
adj | adaptável | É um sofá adaptável a qualquer sala. | C'est un canapé adaptable à n'importe quel salon.
adj | autorizado | Só o pessoal autorizado pode entrar. | Seul le personnel autorisé peut entrer.
adj | bem cozido | Gosto do bife bem cozido. | J'aime le steak bien cuit.
adj | bem-humorado | O meu avô está sempre bem-humorado. | Mon grand-père est toujours de bonne humeur.
adj | bêbado | Ele chegou a casa bêbado. | Il est rentré ivre.
adj | caótico | O trânsito em Lisboa é caótico. | La circulation à Lisbonne est chaotique.
adj | cheio de tato | Ela é sempre cheia de tato. | Elle est toujours pleine de tact.
adj | com direitos iguais | Homens e mulheres são cidadãos com direitos iguais. | Hommes et femmes sont des citoyens égaux en droits.
adj | compassivo | A enfermeira foi muito compassiva. | L'infirmière a été très compatissante.
adj | constrangedor | Foi um momento muito constrangedor. | Ce fut un moment très gênant.
adj | cosmético | É uma mudança apenas cosmética. | C'est un changement seulement cosmétique.
adj | custoso | Acordar cedo é custoso. | Se lever tôt est pénible.
adj | de língua inglesa | Ele cresceu num país de língua inglesa. | Il a grandi dans un pays anglophone.
adj | de vários anos | É um projeto de vários anos. | C'est un projet de plusieurs années.
adj | desconfiado | O gato é desconfiado com estranhos. | Le chat est méfiant avec les inconnus.
adj | desesperado | Estava desesperado à procura das chaves. | Il cherchait ses clés, désespéré.
adj | destemido | O bombeiro destemido entrou no prédio. | Le pompier intrépide est entré dans l'immeuble.
adj | devido | O pagamento devido vence amanhã. | Le paiement dû arrive à échéance demain.
adj | diplomático | Foi uma resposta muito diplomática. | Ce fut une réponse très diplomatique.
adj | disciplinado | É um aluno muito disciplinado. | C'est un élève très discipliné.
adj | eletrónico | Recebi o bilhete eletrónico por e-mail. | J'ai reçu le billet électronique par courriel.
adj | engajado | — |
adj | entusiasmado | As crianças estão entusiasmadas com a viagem. | Les enfants sont enthousiastes à l'idée du voyage.
adj | esperançoso | Estamos esperançosos quanto ao resultado. | Nous avons bon espoir quant au résultat.
adj | estilístico | O texto tem alguns erros estilísticos. | Le texte a quelques fautes de style.
adj | estrito | O regulamento é muito estrito. | Le règlement est très strict.
adj | evangélico | A igreja evangélica fica ao fundo da rua. | L'église évangélique est au bout de la rue.
adj | eventual | Em caso de eventual atraso, avise-nos. | En cas d'éventuel retard, prévenez-nous.
adj | feminino | A equipa feminina ganhou o campeonato. | L'équipe féminine a gagné le championnat.
adj | fluente | Ela fala um português fluente. | Elle parle un portugais courant.
adj | indeciso | Ainda estou indeciso entre os dois cursos. | J'hésite encore entre les deux cursus.
adj | intolerante | Sou intolerante à lactose. | Je suis intolérant au lactose.
adj | invejoso | Não sejas invejoso do teu irmão. | Ne sois pas jaloux de ton frère.
adj | invicto | O clube continua invicto esta época. | Le club reste invaincu cette saison.
adj | loucamente | — |
adj | mesquinho | Foi um comentário mesquinho. | C'était un commentaire mesquin.
adj | modesto | Vivem numa casa modesta. | Ils vivent dans une maison modeste.
adj | mortal | O veneno desta cobra é mortal. | Le venin de ce serpent est mortel.
adj | oval | A mesa da sala é oval. | La table du salon est ovale.
adj | pouco confiável | Esta aplicação é pouco confiável. | Cette application est peu fiable.
adj | pouco saudável | Comer fritos todos os dias é pouco saudável. | Manger des fritures tous les jours est malsain.
adj | punível | Conduzir sem carta é punível por lei. | Conduire sans permis est puni par la loi.
adj | pálido | Estás tão pálido! Sentes-te bem? | Tu es si pâle ! Tu te sens bien ?
adj | que se conserva | — |
adj | restante | O restante dinheiro fica para as férias. | L'argent restant est pour les vacances.
adj | seguro de si | Ela é muito segura de si. | Elle est très sûre d'elle.
adj | sem esperança | O doente não está sem esperança. | Le malade n'est pas sans espoir.
adj | sem sentido | É uma discussão sem sentido. | C'est une discussion insensée.
adj | sem tato | Foi uma pergunta sem tato. | C'était une question sans tact.
adj | sem valor | É um anel sem valor. | C'est une bague sans valeur.
adj | similar | Temos um problema similar no escritório. | Nous avons un problème similaire au bureau.
adj | solvente | A empresa ainda é solvente. | L'entreprise est encore solvable.
adj | ter culpa | — |
adj | trabalhista | É um advogado de direito trabalhista. | C'est un avocat en droit du travail.
adj | uniforme | A cor da parede não está uniforme. | La couleur du mur n'est pas uniforme.
adj | viciante | Este jogo é muito viciante. | Ce jeu est très addictif.
adj | violento | Houve uma tempestade violenta ontem. | Il y a eu une violente tempête hier.
adj | viral | O vídeo tornou-se viral num dia. | La vidéo est devenue virale en un jour.
adv | a propósito | A propósito, viste o Rui? | Au fait, tu as vu Rui ?
adv | a sós | Preciso de falar contigo a sós. | J'ai besoin de te parler seul à seul.
adv | agora há pouco | Agora há pouco esteve aqui a tua mãe. | Ta mère était là tout à l'heure.
adv | alguma vez | Já alguma vez estiveste nos Açores? | Es-tu déjà allé aux Açores ?
adv | livremente | Aqui podes falar livremente. | Ici, tu peux parler librement.
adv | mais vezes | Devias vir cá mais vezes. | Tu devrais venir ici plus souvent.
adv | para quê | Para quê tanta pressa? | Pourquoi tant de hâte ?
adv | por mim | Por mim, podemos ir já. | Pour moi, nous pouvons y aller tout de suite.
adv | sobre o quê | Sobre o quê é o livro? | De quoi parle le livre ?
nom | conservatória de registo civil | Casámos na conservatória de registo civil. | Nous nous sommes mariés à l'état civil.
nom | secretaria de assistência social | O pedido faz-se na secretaria de assistência social. | La demande se fait au service d'aide sociale.

# ------------------------------------------------------------------ B2
nom | ajudante temporário | Em dezembro contratamos dois ajudantes temporários. | En décembre, nous embauchons deux intérimaires.
nom | arquivamento | O arquivamento dos documentos leva horas. | L'archivage des documents prend des heures.
nom | corpo docente | O corpo docente reúne-se todas as segundas. | Le corps enseignant se réunit tous les lundis.
nom | departamento de rh | — |
nom | profissional liberal | Como profissional liberal, ele paga a sua própria segurança social. | En tant que travailleur indépendant, il paie sa propre sécurité sociale.
nom | quem muda de carreira | — |
nom | trabalhador autónomo | O trabalhador autónomo não tem um salário fixo. | Le travailleur indépendant n'a pas de salaire fixe.
nom | trabalhador de turno | O trabalhador de turno muitas vezes dorme mal. | Le travailleur posté dort souvent mal.
nom | digestibilidade | A digestibilidade deste prato é ótima. | Ce plat est très digeste.
nom | erva-doce | Ponho sementes de erva-doce no pão. | Je mets des graines d'anis dans le pain.
nom | liquidificadora | Faço a sopa com a liquidificadora. | Je fais la soupe au mixeur.
nom | papaia | A papaia é uma fruta tropical. | La papaye est un fruit tropical.
nom | papaia papaia | — |
nom | travessa | Põe a travessa no forno. | Mets le plat dans le four.
nom | contrato de renda | Assinámos o contrato de renda por dois anos. | Nous avons signé le bail pour deux ans.
nom | exame preventivo | Ela faz um exame preventivo todos os anos. | Elle fait un bilan de santé chaque année.
nom | rótula | Ele partiu a rótula a jogar futebol. | Il s'est cassé la rotule en jouant au football.
nom | corça | A corça esconde-se entre as árvores. | La biche se cache entre les arbres.
nom | garra | A águia agarra o peixe com as garras. | L'aigle attrape le poisson avec ses serres.
nom | precipitação | A precipitação foi muito escassa este mês. | Les précipitations ont été très faibles ce mois-ci.
nom | linha de balsa | — |
nom | pernoite | O preço do pernoite inclui o pequeno-almoço. | Le prix de la nuitée comprend le petit-déjeuner.
nom | quadro de horários | O quadro de horários está afixado na estação. | Le tableau des horaires est affiché à la gare.
nom | cargo voluntário | Tem um cargo voluntário no clube do bairro. | Il a une fonction bénévole au club du quartier.
nom | jardinagem | A jardinagem relaxa-me mais do que a televisão. | Le jardinage me détend plus que la télévision.
nom | ócio | Também precisamos de momentos de ócio. | Nous avons aussi besoin de moments de loisir.
nom | sessão de treino | Faço três sessões de treino por semana. | Je fais trois séances d'entraînement par semaine.
nom | navegador | Abre o site noutro navegador. | Ouvre le site dans un autre navigateur.
nom | proteção de dados | A lei de proteção de dados é muito exigente. | La loi sur la protection des données est très exigeante.
nom | caderneta de poupança | — |
nom | comparação de preços | Uma comparação de preços vale quase sempre a pena. | Une comparaison des prix vaut presque toujours la peine.
nom | vale-presente | — |
nom | modéstia | Apesar do sucesso, fala com muita modéstia. | Malgré son succès, elle parle avec beaucoup de modestie.
nom | probabilidade | A probabilidade de chuva é de oitenta por cento. | La probabilité de pluie est de quatre-vingts pour cent.
nom | ocupante de cargo público | — |
nom | proteção legal | A lei garante proteção legal aos inquilinos. | La loi garantit une protection juridique aux locataires.
nom | órgão público | O pedido foi enviado ao órgão público competente. | La demande a été envoyée à l'organisme public compétent.
nom | atraso acumulado | O atraso acumulado aumenta todas as semanas. | Le retard accumulé augmente chaque semaine.
verbe | ancorar | O direito à saúde está ancorado na Constituição. | Le droit à la santé est ancré dans la Constitution.
verbe | constituir | Doze artigos constituem a lei. | Douze articles constituent la loi.
adj | abrangente | Ele deu uma visão abrangente do problema. | Il a donné une vue d'ensemble du problème.
adj | autóctone | O sobreiro é uma espécie autóctone. | Le chêne-liège est une espèce autochtone.
adj | de duplo sentido | Foi um comentário de duplo sentido. | Ce fut un commentaire à double sens.
adj | de grandes consequências | Foi uma decisão de grandes consequências. | Ce fut une décision lourde de conséquences.
adj | dependente | Ainda é dependente dos pais. | Il dépend encore de ses parents.
adj | inclinado | O quadro está inclinado para a esquerda. | Le tableau penche vers la gauche.
adj | inconsciente | Estava inconsciente quando a ambulância chegou. | Il était inconscient quand l'ambulance est arrivée.
adj | inequívoco | A resposta foi inequívoca. | La réponse a été sans équivoque.
adj | insignificante | É uma diferença insignificante. | C'est une différence insignifiante.
adj | matizado | Ela tem uma opinião matizada sobre isso. | Elle a une opinion nuancée là-dessus.
adj | minucioso | Fez um trabalho muito minucioso. | Il a fait un travail très minutieux.
adj | não intencional | Foi um erro não intencional. | Ce fut une erreur involontaire.
adj | potente | Este aspirador é muito potente. | Cet aspirateur est très puissant.
adj | supérfluo | Esta informação é supérflua. | Cette information est superflue.
adj | vinculativo | O contrato é vinculativo para as duas partes. | Le contrat engage les deux parties.
adv | de certo modo | De certo modo, tens razão. | D'une certaine manière, tu as raison.
adv | o quê | — |

# ------------------------------------------------------------------ C1
nom | afeição | Tinha uma grande afeição pelos avós. | Il avait une grande affection pour ses grands-parents.
nom | condolências | Apresento-lhe as minhas sinceras condolências. | Je vous présente mes sincères condoléances.
nom | imposição de limites | A imposição de limites também é uma forma de carinho. | Poser des limites est aussi une forme d'affection.
nom | papel de exemplo | — |
nom | reaproximação | Houve uma reaproximação entre os dois países. | Il y a eu un rapprochement entre les deux pays.
nom | boa vontade comercial | — |
nom | centro de distribuição | A empresa abriu um centro de distribuição perto de Leiria. | L'entreprise a ouvert un centre de distribution près de Leiria.
nom | disponibilidade | Agradecemos a sua disponibilidade. | Nous vous remercions de votre disponibilité.
nom | período de integração | O período de integração dura três meses. | La période d'intégration dure trois mois.
nom | taxa de ocupação | A taxa de ocupação dos hotéis chegou aos noventa por cento. | Le taux d'occupation des hôtels a atteint quatre-vingt-dix pour cent.
nom | artigo de prazer | — |
nom | estilo de vida | Mudou de estilo de vida depois de se reformar. | Il a changé de mode de vie après sa retraite.
nom | exercício de atenção plena | Faço um exercício de atenção plena todas as manhãs. | Je fais un exercice de pleine conscience chaque matin.
nom | renúncia ao consumo | A renúncia ao consumo é uma escolha difícil. | Renoncer à la consommation est un choix difficile.
nom | tempo de cozimento | — |
nom | acabamento final | Ao texto só falta o acabamento final. | Il ne manque au texte que la touche finale.
nom | fabricação | A fabricação dos azulejos ainda é artesanal. | La fabrication des azulejos est encore artisanale.
nom | isolamento térmico | A casa antiga não tem isolamento térmico. | La vieille maison n'a pas d'isolation thermique.
nom | metro dobrável | Mede a parede com o metro dobrável. | Mesure le mur avec le mètre pliant.
nom | modernização | A modernização da linha de comboio vai demorar anos. | La modernisation de la ligne de train prendra des années.
nom | tombamento | — |
nom | urbanização | A urbanização do terreno custa mais do que a construção. | L'aménagement du terrain coûte plus cher que la construction.
nom | uso temporário | O edifício está cedido para uso temporário. | Le bâtiment est prêté pour un usage temporaire.
nom | época de floração | A época de floração das amendoeiras é em fevereiro. | La floraison des amandiers a lieu en février.
nom | acompanhamento dos familiares | — |
nom | capacidade de reação | O cansaço diminui a capacidade de reação. | La fatigue diminue la capacité de réaction.
nom | coordenação motora fina | Os puzzles treinam a coordenação motora fina. | Les puzzles entraînent la motricité fine.
nom | desempenho máximo | O atleta atingiu o desempenho máximo em agosto. | L'athlète a atteint sa meilleure performance en août.
nom | plano de treino | O treinador fez-me um plano de treino. | L'entraîneur m'a fait un plan d'entraînement.
nom | senso de equilíbrio | — |
nom | tónus | — |
nom | amassado | — |
nom | abafamento | — |
nom | comportamento territorial | O comportamento territorial dos lobos é muito forte. | Le comportement territorial des loups est très marqué.
nom | fertilidade do solo | A fertilidade do solo no Ribatejo é famosa. | La fertilité du sol du Ribatejo est célèbre.
nom | navio cargueiro | O navio cargueiro espera há três dias para entrar no porto. | Le cargo attend depuis trois jours pour entrer au port.
nom | pecuária extensiva | No Alentejo pratica-se a pecuária extensiva. | Dans l'Alentejo, on pratique l'élevage extensif.
nom | rendimento da colheita | O rendimento da colheita foi fraco este ano. | Le rendement de la récolte a été faible cette année.
nom | tamanho da população | O tamanho da população de linces está a crescer. | La taille de la population de lynx augmente.
nom | área livre | — |
nom | ir e voltar | — |
nom | seguro-saúde para viagem internacional | — |
nom | conjunto de ruas | — |
nom | eixo visual | — |
nom | qualidade do espaço público | — |
nom | conselho de classe | — |
nom | dependência de cuidados | — |
nom | meio especializado | — |
nom | conexão em rede | — |
nom | dominante de cor | — |
nom | encenação | A encenação foi mais polémica do que a peça. | La mise en scène a été plus controversée que la pièce.
nom | figura de linguagem | A metáfora é uma figura de linguagem. | La métaphore est une figure de style.
nom | folha de partitura | — |
nom | linha narrativa | A segunda linha narrativa fica sem resolução. | La deuxième intrigue reste sans dénouement.
nom | tonalidade | A peça está numa tonalidade sombria. | Le morceau est dans une tonalité sombre.
nom | trabalho de base | Antes da obra, há muito trabalho de base. | Avant le chantier, il y a beaucoup de travail préparatoire.
nom | acréscimos | — |
nom | armador | — |
nom | posição na tabela | A equipa subiu duas posições na tabela. | L'équipe a gagné deux places au classement.
nom | alusão | Fez uma alusão ao antecessor. | Il a fait une allusion à son prédécesseur.
nom | capacidade de compreensão | Elogiaram a sua capacidade de compreensão. | On a salué sa capacité de compréhension.
nom | capacidade de memorização | A falta de sono reduz a capacidade de memorização. | Le manque de sommeil réduit la capacité de mémorisation.
nom | conhecimento superficial | Um conhecimento superficial é mais perigoso do que a ignorância. | Une connaissance superficielle est plus dangereuse que l'ignorance.
nom | opinião pública | A opinião pública mudou depois do escândalo. | L'opinion publique a changé après le scandale.
nom | área de estudo | Depois de dois semestres, mudou de área de estudo. | Après deux semestres, elle a changé de domaine d'études.
nom | aquisição | A aquisição do concorrente foi aprovada. | Le rachat du concurrent a été approuvé.
nom | conjuntura económica | A conjuntura económica arrefeceu nos últimos meses. | La conjoncture économique s'est refroidie ces derniers mois.
nom | depreciação | A depreciação da máquina faz-se em dez anos. | L'amortissement de la machine se fait sur dix ans.
nom | durabilidade | A durabilidade deste tecido é impressionante. | La durabilité de ce tissu est impressionnante.
nom | faixa de isenção | — |
nom | fidelização de clientes | A fidelização de clientes custa menos do que a conquista de novos. | Fidéliser les clients coûte moins cher qu'en conquérir de nouveaux.
nom | formação de reservas | Sem formação de reservas, nenhuma empresa aguenta uma crise. | Sans constitution de réserves, aucune entreprise ne résiste à une crise.
nom | geração de valor | A geração de valor fica, em grande parte, na região. | La création de valeur reste en grande partie dans la région.
nom | seguro de responsabilidade civil | O seguro de responsabilidade civil cobriu os danos. | L'assurance responsabilité civile a couvert les dégâts.
nom | estímulo à reflexão | — |
nom | excesso de confiança | O excesso de confiança fez-lhe perder o jogo. | L'excès de confiance lui a fait perdre la partie.
nom | indulgência | Peço a sua indulgência pelo atraso. | Je vous prie d'excuser mon retard.
nom | linha de raciocínio | Não consegui acompanhar a linha de raciocínio dele. | Je n'ai pas réussi à suivre son raisonnement.
nom | parcialidade | O árbitro foi acusado de parcialidade. | L'arbitre a été accusé de partialité.
nom | recalque | — |
nom | grupo marginalizado | O projeto apoia um grupo marginalizado da cidade. | Le projet soutient un groupe marginalisé de la ville.
nom | oportunidade de ascensão | Sem diploma, as oportunidades de ascensão são poucas. | Sans diplôme, les possibilités de promotion sont rares.
nom | princípio norteador | A igualdade é o princípio norteador da escola. | L'égalité est le principe directeur de l'école.
nom | tutela excessiva | — |
nom | detenção | A detenção foi feita de madrugada. | L'arrestation a eu lieu à l'aube.
nom | estado de alerta | Os bombeiros estiveram em estado de alerta a noite toda. | Les pompiers ont été en état d'alerte toute la nuit.
nom | liberdade condicional | Saiu da prisão em liberdade condicional. | Il est sorti de prison en liberté conditionnelle.
nom | obrigatoriedade de consentimento | — |
nom | queixa-crime | Ela apresentou uma queixa-crime contra desconhecidos. | Elle a porté plainte contre X.
nom | revogação | A revogação da lei foi aprovada ontem. | L'abrogation de la loi a été approuvée hier.
nom | aceleração | A aceleração do processo era urgente. | L'accélération du processus était urgente.
nom | altruísmo | O altruísmo dela impressionou toda a gente. | Son altruisme a impressionné tout le monde.
nom | ausência de reservas | Aceitou a proposta com ausência de reservas. | Il a accepté la proposition sans réserve.
nom | complexo do mosteiro | — |
nom | desnível | Há um grande desnível entre o norte e o sul. | Il y a un grand écart entre le nord et le sud.
nom | distensão | Depois do encontro, houve uma distensão entre os dois governos. | Après la rencontre, il y a eu une détente entre les deux gouvernements.
nom | encadeamento | Foi um encadeamento infeliz de circunstâncias. | Ce fut un enchaînement malheureux de circonstances.
nom | enfraquecimento | Nota-se um enfraquecimento da economia. | On constate un affaiblissement de l'économie.
nom | momento de oração | — |
nom | peregrinação | A peregrinação a Fátima atrai milhares de pessoas. | Le pèlerinage à Fátima attire des milliers de personnes.
nom | razoabilidade | Duvido da razoabilidade desta decisão. | Je doute du bien-fondé de cette décision.
nom | relativização | A relativização do problema não ajuda ninguém. | Relativiser le problème n'aide personne.
nom | retidão | A retidão dele era indiscutível. | Sa droiture était indiscutable.
nom | retroalimentação | — |
nom | trabalho forçado | O trabalho forçado é proibido em todo o mundo. | Le travail forcé est interdit dans le monde entier.
nom | visão de mundo | Cada geração tem a sua visão de mundo. | Chaque génération a sa vision du monde.
verbe | conjecturar | Só podemos conjecturar sobre as razões. | Nous ne pouvons que faire des conjectures sur les raisons.
verbe | desarmar | Uma frase bastou para desarmar a discussão. | Une phrase a suffi pour désamorcer la dispute.
verbe | desbotar | A camisola desbotou na máquina. | Le pull a déteint dans la machine.
verbe | desescalar | Um tom calmo ajuda a desescalar o conflito. | Un ton calme aide à désamorcer le conflit.
verbe | encaixar | Ele encaixa bem as críticas. | Il encaisse bien les critiques.
verbe | esquadrinhar | A polícia esquadrinhou o bairro inteiro. | La police a passé tout le quartier au peigne fin.
verbe | expirar | O prazo expira no fim do mês. | Le délai expire à la fin du mois.
verbe | intitular | Como vamos intitular o capítulo? | Quel titre allons-nous donner au chapitre ?
verbe | reorganizar | Temos de reorganizar os dois capítulos. | Nous devons réorganiser les deux chapitres.
verbe | replicar | Ela replicou com um argumento muito forte. | Elle a répliqué avec un argument très fort.
verbe | requerer | Ela requereu a prorrogação do prazo. | Elle a demandé la prolongation du délai.
adj | abrupto | A estrada termina num declive abrupto. | La route se termine par une pente abrupte.
adj | adaptado ao cargo | — |
adj | admissível | Este atraso não é admissível. | Ce retard n'est pas admissible.
adj | bem pensado | O projeto está bem pensado. | Le projet est bien pensé.
adj | caduco | Com a nova lei, a regra ficou caduca. | Avec la nouvelle loi, la règle est devenue caduque.
adj | característico | O cheiro a sardinha assada é característico de junho. | L'odeur de sardine grillée est caractéristique de juin.
adj | com erros | — |
adj | comunicativo | Depois do segundo café, fica mais comunicativo. | Après le deuxième café, il devient plus communicatif.
adj | condicional | A oferta é condicional à aprovação do banco. | L'offre est conditionnelle à l'accord de la banque.
adj | de pouca manutenção | — |
adj | decidido | Ela apresentou-se muito decidida. | Elle s'est présentée très décidée.
adj | defensável | É uma posição defensável. | C'est une position défendable.
adj | divisivo | É um tema divisivo na sociedade. | C'est un sujet qui divise la société.
adj | do mesmo nível | — |
adj | esbanjador | É muito esbanjador com o dinheiro. | Il est très dépensier.
adj | feito por profissional | — |
adj | grosseiro | Foi um erro grosseiro. | Ce fut une erreur grossière.
adj | imaculado | A toalha estava imaculada. | La nappe était immaculée.
adj | imperturbável | Ficou imperturbável perante as críticas. | Il est resté imperturbable face aux critiques.
adj | incansável | É uma defensora incansável dos animais. | C'est une défenseure infatigable des animaux.
adj | incoerente | As duas versões são incoerentes. | Les deux versions sont incohérentes.
adj | incontestado | É o líder incontestado do grupo. | C'est le chef incontesté du groupe.
adj | indulgente | O examinador foi indulgente. | L'examinateur a été indulgent.
adj | insistente | Foi muito insistente ao telefone. | Il a été très insistant au téléphone.
adj | intransigente | Neste ponto, ele é intransigente. | Sur ce point, il est intransigeant.
adj | irrestrito | Tem o meu apoio irrestrito. | Il a mon soutien sans réserve.
adj | lacunar | A documentação é lacunar. | La documentation est lacunaire.
adj | meticuloso | Ela é meticulosa no trabalho. | Elle est méticuleuse dans son travail.
adj | negligente | O condutor foi negligente. | Le conducteur a été négligent.
adj | nitidamente delimitado | — |
adj | não provado | A acusação continua não provada. | L'accusation reste non prouvée.
adj | obscuro | A origem do dinheiro é obscura. | L'origine de l'argent est obscure.
adj | periférico | É uma questão periférica. | C'est une question secondaire.
adj | perseverante | É uma aluna perseverante. | C'est une élève persévérante.
adj | pomposo | O discurso foi pomposo e vazio. | Le discours a été pompeux et creux.
adj | pouco prático | O formulário é pouco prático. | Le formulaire est peu pratique.
adj | pouco usado | Esta expressão hoje é pouco usada. | Cette expression est peu employée aujourd'hui.
adj | prioritário | Esta tarefa é prioritária. | Cette tâche est prioritaire.
adj | pronto para publicação | — |
adj | propenso a falhas | O sistema antigo é propenso a falhas. | L'ancien système est sujet aux pannes.
adj | pé no chão | — |
adj | quantificável | O benefício é difícil de quantificar, mas não deixa de ser quantificável. | Le bénéfice est difficile à chiffrer, mais il reste quantifiable.
adj | que separa | — |
adj | redigido por extenso | — |
adj | repetível | A experiência tem de ser repetível. | L'expérience doit être reproductible.
adj | sem contradições | O texto é surpreendentemente sem contradições. | Le texte est étonnamment exempt de contradictions.
adj | sem transparência | Foi um concurso sem transparência. | Ce fut un appel d'offres opaque.
adj | sob medida | Fizemos um móvel sob medida. | Nous avons fait faire un meuble sur mesure.
adj | subordinado | Esta questão é subordinada à principal. | Cette question est subordonnée à la principale.
adj | transferível | O bilhete não é transferível. | Le billet n'est pas transférable.
adj | vergonhoso | Foi um comportamento vergonhoso. | Ce fut un comportement honteux.
adv | vice-versa | Ela ajuda-me e vice-versa. | Elle m'aide et vice versa.
"""
