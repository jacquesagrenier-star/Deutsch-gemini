# -*- coding: utf-8 -*-
"""Verbes, adjectifs, adverbes et expressions du B1 portugais. SOURCE : c'est ici qu'on corrige, puis
python portugais/outils/construire.py (qui appelle niveaux.py apres l'A1).

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (29 oct. 2026),
converti au portugais d'Europe (variante_niveaux.py), puis relu. Meme format
que mots_a1.py et phrases_a1.py (session socle). BROUILLON : a faire relire par un lusophone du Portugal.

Drapeaux en plus de ceux de l'A1 : « g? » genre devine (a verifier) ; « ex? »
la phrase ne contient pas le mot (a revoir) ; « ex=? » aucune phrase (a ecrire).
"""

NIVEAU = 'B1'

# « infinitif | traduction | phrase | sa traduction | drapeaux » (formes : irreguliers.py).
VERBES = """
abandonar | abandonner | Ele abandonou o projeto no meio do caminho. | Il a abandonné le projet à mi-chemin.
abastecer | approvisionner | Eles abastecem vinte vilarejos. | Ils approvisionnent vingt villages.
abençoar | bénir | O padre abençoou a casa nova. | Le curé a béni la nouvelle maison.
abraçar | embrasser, serrer | Ela abraçou a mãe por muito tempo. | Elle a longuement pris sa mère dans ses bras.
acalmar | calmer | A música acalma as crianças. | La musique calme les enfants.
acenar | faire signe de la main | As crianças acenam da janela. | Les enfants font signe depuis la fenêtre.
acolher | accueillir | O vilarejo acolhe vinte famílias. | Le village accueille vingt familles.
acompanhar | accompagner | O filho acompanha a mãe ao médico. | Le fils accompagne sa mère chez le médecin.
acumular | accumuler | Ele acumula papéis há anos. | Il accumule des papiers depuis des années.
adaptar | adapter | Vamos adaptar o horário aos novos turnos. | Nous adapterons l'horaire aux nouveaux roulements.
adaptar-se | s'adapter | Ele adaptou-se ao clima em um ano. | Il s'est adapté au climat en un an. | pron
adivinhar | deviner | Adivinhe quem ligou. | Devine qui a appelé.
administrar | gérer | Ele administra o orçamento. | Il gère le budget.
admitir | admettre | Ele admite que se enganou. | Il admet qu'il s'est trompé.
adquirir | acquérir | Eu adquiro novos conhecimentos. | J'acquiers de nouvelles connaissances.
afirmar | affirmer | Ele afirma que não sabia de nada. | Il affirme qu'il ne savait rien.
afogar | noyer, étouffer | Sem colete salva-vidas eu afogar-me-ia em dois minutos. | Sans gilet de sauvetage, je me noierais en deux minutes.
afogar-se | se noyer | Ele quase se afoga no lago. | Il se noie presque dans le lac. | pron
agarrar | attraper | Agarre a corda com força. | Attrape la corde fermement.
agitar | agiter | Agite a embalagem antes de usar. | Agite le flacon avant usage.
agravar | aggraver | A crise agravou o problema. | La crise a aggravé le problème.
alimentar-se | s'alimenter | Ele alimenta-se muito bem desde janeiro. | Il s'alimente très bien depuis janvier. | pron
aliviar | soulager | O comprimido alivia a dor. | Le comprimé soulage la douleur.
alterar | altérer | O barulho alterou o sono do hotel todo. | Le bruit a perturbé le sommeil de tout l'hôtel.
amarrar | attacher | Amarre bem os atacadores. | Attache bien tes lacets.
ameaçar | menacer | Ele ameaçou renunciar. | Il a menacé de démissionner.
ampliar | élargir, agrandir | Eles ampliam a fábrica este ano. | Ils agrandissent l'usine cette année.
analisar | analyser | Analisamos os resultados na segunda. | Nous analysons les résultats lundi.
aplicar | appliquer | Aplique o creme duas vezes por dia. | Applique la crème deux fois par jour.
apontar | signaler | O relatório aponta três riscos. | Le rapport signale trois risques.
apostar | parier | Eles apostaram no vencedor. | Ils ont parié sur le vainqueur.
apresentar-se | se présenter, se comporter | Ontem ele apresentou-me à família dele. | Hier, il m'a présenté à sa famille. | pron
apropriar-se de | s'approprier, acquérir | Com mais cursos as pessoas integrar-se-iam melhor. | Avec plus de cours, on intégrerait mieux les gens.
aprovar | adopter (une loi, une décision) | O parlamento aprova a lei. | Le parlement adopte la loi.
aproximar-se de | s'approcher de ; se fermer | Ele aproximou-se da janela para ver a rua. | Il s'est approché de la fenêtre pour voir la rue.
arar | labourer | Eles aram a terra antes de semear. | Ils labourent la terre avant de semer.
arder | brûler | Sem água o campo arderia em minutos. | Sans eau, le champ brûlerait en quelques minutes.
argumentar | argumenter | Ele argumenta muito bem a sua posição. | Il argumente très bien sa position.
armazenar | stocker | Eles armazenam a fruta refrigerada. | Ils stockent les fruits au froid.
arrancar | arracher, démarrer | O comboio vai arrancar em dois minutos. | Le train démarrera dans deux minutes.
arrastar | traîner | Ele arrastou a mala até a plataforma. | Il a traîné la valise jusqu'au quai.
arrecadar | collecter (des fonds) | Eles arrecadaram mil euros em um dia. | Ils ont collecté mille euros en un jour.
arredondar | arrondir | O vendedor sempre arredondava a seu favor. | Le commerçant arrondissait toujours en sa faveur.
arrendar | affermer, louer (des biens) | Ele arrenda as suas terras. | Il afferme son terrain.
arriscar | risquer | Ele arriscou o cargo para defendê-lo. | Il a risqué son poste pour le défendre.
arrombar | cambrioler, pénétrer par effraction | Alguém arrombou a loja. | Quelqu'un s'est introduit dans le magasin.
assegurar | assurer | Ele assegurou que chegaria a tempo. | Il a assuré qu'il arriverait à temps.
assistir | regarder, assister à | As crianças assistem aos jogadores. | Les enfants regardent les joueurs.
assistir a | assister | Ele assistiu à palestra inteira. | Il a assisté à toute la conférence.
associar | classer, associer | Eu associaria esta cor ao outono. | J'associerais cette couleur à l'automne.
atacar | attaquer | O cão ataca o carteiro. | Le chien attaque le facteur.
atender | s'occuper de | Já estão a atender o senhor? | On s'occupe de vous ?
ater-se a | s'en tenir à, respecter | Com esse guarda-redes eles classificar-se-iam com certeza. | Avec ce gardien, ils se qualifieraient à coup sûr.
atrair | attirer | A feira atrai milhares de visitantes. | La foire attire des milliers de visiteurs.
atrapalhar | gêner, entraver | O carro atrapalha o trânsito. | La voiture gêne la circulation.
atrasar | retarder | Atrasaram o relógio uma hora. | Ils ont retardé l'horloge d'une heure.
atropelar | écraser ; brûler (un feu) | Cuidado para não furar o sinal vermelho. | Fais attention à ne pas brûler le feu rouge. | ex?
atualizar | mettre à jour | Atualizo o telemóvel à noite. | Je mets à jour le portable la nuit.
automatizar | automatiser | Eles automatizam o processo de entrega. | Ils automatisent le processus de livraison.
barbear | raser | Ele barbeia-se todas as manhãs. | Il se rase chaque matin.
bater papo | bavarder | Batemos papo um pouco no terraço. | Nous avons bavardé un moment en terrasse.
bloquear | bloquer | O sistema bloqueia as mensagens estranhas. | Le système bloque les messages étranges.
buzinar | klaxonner | Na cidade é proibido buzinar à noite. | En ville, on ne peut pas klaxonner la nuit.
captar | saisir, comprendre | Eu capto a situação rápido. | Je saisis vite la situation.
castigar | punir | Ele ficou de castigo sem sair. | Ils l'ont puni de sortie.
causar | causer | A tempestade causou danos graves. | L'orage a causé des dégâts graves.
censurar | reprocher | Ela nunca me censurou por nada. | Elle ne m'a jamais rien reproché.
cessar | cesser | A chuva não cessou a noite inteira. | La pluie n'a pas cessé de la nuit.
chamar a atenção | frapper, se remarquer | Isso chamaria a atenção de qualquer um. | Cela frapperait n'importe qui.
checar | vérifier | Vou dar uma checada rápida nos meus e-mails. | Je vérifie vite mes courriels.
chover granizo | grêler | Em junho às vezes chove granizo. | En juin, il grêle parfois.
chutar | tirer (arme, ballon) | Ele chuta a bola para o golo. | Il tire le ballon dans le but.
circular | circuler | Não se pode circular pelo centro. | On ne peut pas circuler dans le centre.
citar | citer | Ele cita três autores na primeira página. | Il cite trois auteurs dès la première page.
classificar | classer | Eles classificam os resíduos por cor. | Ils classent les déchets par couleur.
classificar-se | se qualifier | Eles classificaram-se para a final. | Ils se sont qualifiés pour la finale. | pron
clicar | cliquer | Clique no campo verde. | Cliquez sur la case verte.
clicar em | cliquer sur | Clique no campo verde. | Cliquez sur la case verte.
coincidir | coïncider | A festa vai coincidir com o meu aniversário. | La fête coïncidera avec mon anniversaire.
colaborar | collaborer | Colaboramos com outra empresa. | Nous collaborons avec une autre entreprise.
colecionar | collectionner, collecter | Eu coleciono selos. | Je collectionne les timbres.
colher | récolter | Eles colhem a uva em setembro. | Ils récoltent le raisin en septembre.
comercializar | commercialiser | A empresa comercializa o novo produto. | L'entreprise commercialise le nouveau produit.
comparecer | se rendre, venir | Cem pessoas comparecem todos os domingos. | Cent personnes viennent chaque dimanche.
compor-se | se composer (de qch), s'asseoir ensemble | A equipa é composta de dez pessoas. | L'équipe se compose de dix personnes. | pron
compreender | comprendre | Compreendi o problema ao ler o relatório. | J'ai compris le problème en lisant le rapport.
comprometer-se | s'engager | Ele comprometeu-se a nos ajudar. | Il s'est engagé à nous aider. | pron
comprovar | démontrer, prouver | O estudo nos comprova o efeito. | L'étude nous démontre l'effet.
concluir | conclure | Eles concluem que é preciso mais tempo. | Ils concluent qu'il faut plus de temps.
concordar | être d'accord, approuver | Eu concordo com a tua proposta. | J'approuve ta proposition.
condenar | condamner | Ele foi condenado a uma multa. | Il a été condamné à une amende.
confessar | avouer | Ele confessou que tinha quebrado o vaso. | Il a avoué qu'il avait cassé le vase.
confirmar | confirmer | Confirme a tua presença antes de sexta. | Confirme ta présence avant vendredi.
confundir | confondre | Eu sempre confundo os dois irmãos. | Je confonds toujours les deux frères.
conhecer bem | s'y connaître (en qch) | O guia conhece muito bem o centro histórico. | Le guide touristique connaît parfaitement la vieille ville.
conquistar | conquérir | Eles conquistaram a região em dois anos. | Ils ont conquis la région en deux ans.
conservar | conserver | Eles conservam a floresta desde 1990. | Ils conservent la forêt depuis 1990.
considerar | considérer | Considero que é cedo demais. | Je considère que c'est trop tôt.
consistir | consister | O trabalho consiste em revisar textos. | Le travail consiste à relire des textes.
consolar | consoler | Eu consolo o meu amigo. | Je console mon ami.
consultar | consulter | Consulte o horário antes de sair. | Consulte l'horaire avant de partir.
contagiar | contaminer | Não quero contagiar ninguém. | Je ne veux contaminer personne.
contar com | compter sur (auf) | Nós contamos com ele. | Nous avons compté sur lui.
contemplar | contempler | Contemplamos o pôr do sol da praia. | Nous contemplons le coucher de soleil.
contestar | contester, réclamer | Eu contesto a conta. | Je conteste la facture.
continuar juntos | rester ensemble | Os dois amigos continuam juntos desde a escola. | Les deux amis restent ensemble depuis l'école.
contrair | contracter (un crédit) | Ela faz um empréstimo para a faculdade. | Elle contracte un crédit pour ses études. | ex?
contribuir para | contribuer à (zu) | Cada um contribui para o sucesso. | Chacun contribue au succès.
controlar | contrôler | Eles controlam a temperatura a cada hora. | Ils contrôlent la température chaque heure.
convencer | convaincre | Essa explicação não me convence. | Cette explication ne me convainc pas.
conversar on-line | clavarder, discuter en ligne | À noite eu converso on-line com a minha família. | Le soir, je clavarde avec ma famille.
converter | convertir | A chuva convertia o caminho num lamaçal. | La pluie transformait le chemin en bourbier.
convocar | convoquer | Convocaram uma reunião urgente. | Ils ont convoqué une réunion urgente.
coordenar | coordonner | Ele coordena três equipas ao mesmo tempo. | Il coordonne trois équipes à la fois.
copiar | copier | Copie o arquivo para a pasta nova. | Copie le fichier dans le nouveau dossier.
cultivar | cultiver | Eles cultivam tomates o ano todo. | Ils cultivent des tomates toute l'année.
cumprir | accomplir, respecter | Ele cumpre a lei ao pé da letra. | Il respecte la loi à la lettre.
danificar | abîmer | A humidade danificou os livros. | L'humidité a abîmé les livres.
dar aula | enseigner | Ela dá aula de alemão numa escola para adultos. | Elle enseigne l'allemand à l'université populaire.
dar comida | nourrir (un animal) | Ele dá comida para o gato todas as manhãs às sete. | Il nourrit le chat tous les matins à sept heures.
dar conta de | surmonter, gérer (une tâche) | Ele deu conta da tarefa sozinho. | Il gérait la tâche seul.
dar notícias | donner de ses nouvelles, se manifester | Ele não dá notícias há semanas. | Il n'a pas donné de nouvelles depuis des semaines.
dar-se bem | bien s'entendre avec | Eu dou-me bem com os meus colegas. | Je m'entends bien avec mes collègues.
debruçar-se sobre | se confronter à, examiner (mit) | Eu debruço-me sobre o tema. | Je me penche sur le sujet.
decepcionar | décevoir | O resultado decepciona-me. | Le résultat me déçoit.
declarar | déclarer, témoigner | Vão declarar estado de emergência amanhã. | Ils déclareront l'état d'urgence demain.
decorar | décorer | Decoraram a sala com flores. | Ils ont décoré la salle de fleurs.
decorrer | se dérouler ; s'égarer | A noite transcorre bem tranquila. | La soirée se déroule très calmement. | ex?
dedicar | consacrer | Ele dedica duas horas por dia ao piano. | Il consacre deux heures par jour au piano.
dedicar-se | se consacrer | Eu dedico-me ao meu trabalho. | Je me consacre à mon travail. | pron
defender | défendre | Ela defendeu a tese com calma. | Il a défendu sa thèse avec calme.
defender-se | se défendre | Eu defendo-me das críticas. | Je me défends contre la critique. | pron
definir | définir | Defina bem o objetivo do projeto. | Définis bien l'objectif du projet.
degustar | déguster | Degustamos três queijos diferentes. | Nous dégustons trois fromages différents.
delegar | déléguer | Ele delega as tarefas mais simples. | Il délègue les tâches les plus simples.
demolir | démolir | Demoliram o prédio antigo. | Ils ont démoli l'ancien immeuble.
demonstrar | démontrer | O estudo demonstra o contrário. | L'étude démontre le contraire.
depender | dépendre | Tudo depende do tempo que fizer. | Tout dépend du temps qu'il fera.
depender de | arriver (sur qch), dépendre de | Ele sempre dependeu do irmão mais velho. | Il a toujours dépendu de son frère aîné.
derreter | faire fondre | O sol derreteu o gelo do caminho. | Le soleil a fait fondre la glace du chemin.
desabar | s'effondrer | O prédio antigo está a desabar. | Le vieux bâtiment s'effondre.
desaparecer | disparaître | Eles documentam a língua antes que desapareça. | Ils documentent la langue avant qu'elle disparaisse.
descartar | éliminer, jeter (des déchets) | Ele descarta as pilhas velhas no supermercado. | Il jette les vieilles piles au supermarché.
desconfiar | se méfier | Desconfio de preços muito baixos. | Je me méfie des prix très bas.
descrever | décrire | Ele descreve o vilarejo com muitos detalhes. | Il décrit le village avec beaucoup de détail.
descuidar | négliger | Ele descuidou do jardim o inverno inteiro. | Il a négligé le jardin tout l'hiver.
desencadear | déclencher | O incidente desencadeou um debate. | L'incident déclenchait un débat.
desenvolver-se | se développer | Com mais dinheiro o projeto desenvolver-se-ia mais rápido. | Avec plus d'argent, le projet se développerait plus vite. | pron
desfazer | défaire | Desfaça a mala antes de jantar. | Défais la valise avant de dîner.
desistir de | abandonner, renoncer | Não vamos desistir até encontrar o cão. | Nous n'abandonnerons pas avant d'avoir retrouvé le chien.
deslocar-se | se déplacer | Ele desloca-se de bicicleta o ano todo. | Il se déplace à vélo toute l'année. | pron
despejar | déverser | Eles despejaram resíduos no rio. | Ils ont déversé des déchets dans le fleuve.
desrespeitar | ignorer, ne pas respecter | Ele desrespeita as normas. | Il ne respecte pas les règlements.
destruir | détruire | O fogo destruiu meio hectare. | Le feu a détruit un demi-hectare.
deter | interpeller, arrêter | A polícia detém dois homens. | La police interpelle deux hommes.
difundir | diffuser, répandre | O rádio difundiu a notícia em minutos. | La radio a diffusé la nouvelle en quelques minutes.
digerir | digérer | Digiro mal comida gordurosa. | Je digère mal la nourriture grasse.
digitar | taper (au clavier) | Ela digita muito rápido. | Elle tape très vite.
diminuir | diminuer | O consumo diminuiu este ano. | La consommation a diminué cette année.
discriminar | discriminer | A lei proíbe discriminar por idade. | La loi interdit de discriminer par l'âge.
disparar | tirer | Ele disparou a câmara sem pensar. | Il a déclenché l'appareil sans réfléchir.
dispor de | disposer de (über) | Eu disponho de experiência suficiente. | Je dispose de suffisamment d'expérience.
dissolver | dissoudre ; résoudre | Dissolve-se o comprimido na água. | On dissout le comprimé dans l'eau.
distinguir | distinguer | Não distingo os gémeos. | Je ne distingue pas les jumeaux.
distribuir | distribuer | Eles distribuem em toda a península. | Ils distribuent dans toute la péninsule.
divertir | amuser | O espetáculo divertiu as crianças. | Le spectacle a amusé les enfants.
divertir-se | s'amuser | As crianças divertem-se com o palhaço. | Les enfants s'amusent du clown. | pron
divorciar-se | divorcer (lassen), séparer | Eles vão divorciar-se depois de dez anos. | Ils divorcent après dix ans. | pron
doar | donner | Ele doa sangue três vezes por ano. | Il donne son sang trois fois par an.
documentar | documenter | Eu documento cada passo. | Je documente chaque étape.
dominar | maîtriser | Eu domino três línguas. | Je maîtrise trois langues.
duvidar | douter | Duvido desse número. | Je doute de ce chiffre.
duvidar de | douter de | Eu duvido das palavras dele. | Je doute de ses paroles.
edificar | bâtir | Não queremos que edifiquem sobre a floresta. | Nous ne voulons pas qu'ils bâtissent sur la forêt.
editar | éditer | Ele editou o vídeo em uma noite. | Il a monté la vidéo en une nuit.
educar | éduquer | Eles educaram os filhos em duas línguas. | Ils ont élevé leurs enfants en deux langues.
elaborar | établir, créer (un document) | O grupo está a elaborar uma proposta. | Le groupe élabore une proposition.
eliminar | éliminer | O filtro eliminava quase todo o barulho. | Le filtre éliminait presque tout le bruit.
elogiar | louer, féliciter | O professor elogia os alunos. | Le professeur félicite les élèves.
emagrecer | maigrir | Ele emagreceu cinco quilos. | Il a maigri de cinq kilos.
embalar | emballer | Nós embalamos a mercadoria com cuidado. | Nous emballons la marchandise avec soin.
emigrar | émigrer | Ele emigrou para a Alemanha nos anos setenta. | Il a émigré en Allemagne dans les années soixante-dix.
emocionar | émouvoir | A cena final emociona a todos. | La scène finale émeut tout le monde.
empregar | employer | A empresa emprega cem pessoas. | L'entreprise emploie cent personnes.
encenar | représenter, jouer (une pièce) | O teatro está a encenar uma peça nova. | Le théâtre joue une nouvelle pièce.
encomendar | commander | Encomendamos o sofá em outubro. | Nous commandons le canapé en octobre.
endividar-se | s'endetter | Ele endividou-se para abrir o negócio. | Il s'est endetté pour ouvrir le commerce. | pron
enfatizar | souligner | O relatório enfatiza a necessidade de investir. | Le rapport met l'accent sur la nécessité d'investir.
enfraquecer | affaiblir | A seca enfraqueceu as plantações. | La sécheresse a affaibli les cultures.
engajar-se | s'engager | Eu engajo-me na proteção do meio ambiente. | Je m'engage pour la protection de l'environnement. | pron
enganar | tromper | As aparências enganam. | Les apparences sont trompeuses.
enganar-se | se tromper | Desta vez ele enganou-se. | Il s'est trompé cette fois. | pron
engordar | grossir | Ele engorda no inverno. | Il grossit en hiver.
enrolar | enrouler, emballer | Ele enrolou o cachecol no pescoço. | Il a enroulé l'écharpe autour de son cou.
entender mal | mal comprendre | Por favor, não me entenda mal. | Ne me comprenez pas de travers, s'il vous plaît.
entrar em acordo | se mettre d'accord | Nós chegamos a um acordo sobre o preço. | Nous nous mettons d'accord sur un prix.
enviar por fax | faxer, envoyer par télécopie | Eu mandei o formulário por fax para ele. | Je lui faxais le formulaire.
erguer | lever | Ele ergueu a voz para ser ouvido. | Il a élevé la voix pour se faire entendre.
esclarecer | éclaircir | Esclareça o terceiro ponto, por favor. | Éclaircis le troisième point, s'il te plaît.
esconder | cacher | Escondi as chaves embaixo do vaso. | J'ai caché les clés sous le pot.
escrever num blog | bloguer | Ela escreve um blog sobre viagens. | Elle blogue sur les voyages.
esforçar-se | s'efforcer | Ele esforça-se para melhorar a cada dia. | Il s'efforce de progresser chaque jour. | pron
esfriar | refroidir | Deixa a sopa esfriar um pouco. | Laisse la soupe refroidir un peu.
esgotar | épuiser | Esgotamos os recursos do solo. | Nous épuisons les ressources du sol.
espalhar | diffuser, répandre | Ele espalha a notícia rápido. | Il répand la nouvelle rapidement.
especular | spéculer | Eles especulam com o preço dos terrenos. | Ils spéculent sur le prix du terrain.
estabelecer-se | s'établir | Eles estabeleceram-se no litoral. | Ils se sont établis sur la côte. | pron
estagnar | stagner | A economia estagnou por dois trimestres. | L'économie a stagné deux trimestres.
estar definido | être établi, être certain | A data ainda não está definida. | La date n'est pas encore fixée.
estender-se | s'étendre | O deserto estende-se para o sul. | Le désert s'étend vers le sud. | pron
estimar | estimer | Eles estimam o número em um milhão. | Ils estiment le chiffre à un million.
exagerar | exagérer | Ele exagerava em todas as histórias. | Il exagérait dans chaque histoire.
excluir | exclure | O sistema exclui muitas pessoas. | Le système exclut beaucoup de gens.
experimentar | expérimenter | Eles experimentam materiais novos. | Ils expérimentent de nouveaux matériaux.
explodir | exploser | O pneu explode de repente. | Le pneu explose soudainement.
explorar | explorer | Exploramos o centro histórico a pé. | Nous explorons la vieille ville à pied.
exportar | exporter | Eles exportam azeite para trinta países. | Ils exportent de l'huile vers trente pays.
expressar | exprimer | Ele tem dificuldade em expressar o que sente. | Il a du mal à exprimer ce qu'il ressent.
facilitar | faciliter | O elevador facilita o acesso. | L'ascenseur facilite l'accès.
falir | faire faillite | A empresa faliu em 2019. | L'entreprise a fait faillite en 2019.
fazer as contas | facturer, faire les comptes | A empresa faz as contas dos custos no fim do mês. | L'entreprise règle les comptes à la fin du mois.
fazer bico | faire un petit boulot | Nas férias eu faço bico num café. | Pendant les vacances, je fais un petit boulot au café.
fazer esforço | faire des efforts | Eu esforço-me para a prova. | Je fais des efforts pour l'examen.
fazer greve | faire grève | Os motoristas de Autocarro estão em greve desde segunda. | Les chauffeurs de bus font grève depuis lundi.
fazer o check-out | quitter l'hôtel (check-out) | Fizemos o check-out às onze horas. | Nous avons quitté la chambre à onze heures.
fazer raio-x | radiographier, faire une radio | O médico faz um raio-X do braço quebrado. | Le médecin radiographie le bras cassé.
fazer seguro | assurer | Nós fazemos o seguro do carro com esta empresa. | Nous assurons la voiture auprès de cette compagnie.
feder | puer, sentir mauvais | O lixo fede com o calor. | Les ordures puent à la chaleur.
ficar entre si | rester entre soi | Neste bairro os moradores gostam de ficar entre si. | Dans ce quartier, les habitants aiment rester entre eux.
ficar à toa | paresser, ne rien faire | Nas férias o que eu mais gosto é ficar à toa. | En vacances, j'aime surtout ne rien faire.
financiar | financer | O banco financia a obra. | La banque finance les travaux.
fingir | faire semblant | Ele fingiu não ter ouvido nada. | Il a fait semblant de ne rien avoir entendu.
florescer | fleurir | Na primavera as árvores florescem. | Au printemps, les arbres fleurissent.
formar | former | A universidade forma mil alunos por ano. | L'université forme mille étudiants par an.
fornecer | apporter | Os legumes fornecem vitaminas. | Les légumes apportent des vitamines.
fortalecer | renforcer | O exercício fortalece as costas. | L'exercice renforce le dos.
fracassar | échouer | O plano fracassou por falta de dinheiro. | Le plan a échoué faute d'argent.
frustrar | frustrer | A longa espera frustra muitos clientes. | La longue attente frustre beaucoup de clients.
fundar | fonder | Eles fundaram a cidade em 1250. | Ils ont fondé la ville en 1250.
fundir | fusionner | Eles fundiram as duas filiais. | Ils ont fusionné les deux filiales.
garantir | garantir | A lei garante o acesso. | La loi garantit l'accès.
gerar | produire | Os painéis geram energia para a casa. | Les panneaux produisent l'électricité de la maison.
gerir | gérer | Ela geriu a crise com muita calma. | Elle a géré la crise avec beaucoup de calme.
governar | gouverner | Eles governam há quatro anos. | Ils gouvernent depuis quatre ans.
guardar | conserver, garder | Eu guardo os comprovantes. | Je conserve les reçus.
guiar | guider | Ele guiou-nos pelo centro histórico. | Il nous a guidés dans la vieille ville.
hesitar | hésiter | Eu hesito diante desta decisão. | J'hésite face à cette décision.
identificar | identifier | Identifico a música em dois segundos. | J'identifie la chanson en deux secondes.
ignorar | ignorer | Ele ignorou os meus conselhos e errou. | Il a ignoré mes conseils et il s'est trompé.
impedir | empêcher | A chuva impediu o jogo. | La pluie a empêché le match.
implicar | impliquer | A mudança implica mais trabalho. | Le changement implique plus de travail.
impor | imposer | Impuseram um horário novo. | Ils ont imposé un nouvel horaire.
importar | importer | Importamos quase todo o gás. | Nous importons presque tout le gaz.
improvisar | improviser | Ele improvisou um discurso de três minutos. | Il a improvisé un discours de trois minutes.
impulsionar | impulser | A lei impulsionou a reciclagem. | La loi a impulsé le recyclage.
indicar | indiquer | A placa indica a saída. | Le panneau indique la sortie.
informar-se | se renseigner | Eu informo-me sobre o preço. | Je me renseigne sur le prix. | pron
infringir | enfreindre (gegen) | Ele infringe as regras. | Il enfreint les règles.
iniciar | démarrer, lancer | O programa inicia automaticamente. | Le programme démarre automatiquement.
insinuar | suggérer, laisser entendre | Eu só insinuaria isso. | Je ne ferais que le suggérer.
insistir | insister | Ele insiste em pagar. | Il insiste pour payer lui-même.
inspirar | inspirer | A viagem inspirou o romance dele. | Le voyage lui a inspiré le roman.
insultar | insulter | Ele não xinga ninguém. | Il n'insulte personne. | ex?
integrar | intégrer | O curso integra os novos moradores na cidade. | Le cours intègre les nouveaux habitants à la ville.
integrar-se | s'intégrer | Ele integrou-se muito rápido no bairro. | Il s'est intégré très vite dans le quartier. | pron
interromper | interrompre | O meu irmão interrompia todas as conversas. | Mon frère interrompait toutes les conversations.
intervir | intervenir, opérer | O ministro vai intervir no congresso amanhã. | Le ministre interviendra au congrès demain.
introduzir | introduire | Introduzi o cartão e digitei o código. | J'ai introduit la carte et j'ai tapé le code.
investigar | déterminer, enquêter | A polícia investiga a causa. | La police détermine la cause.
isolar | isoler | Nós isolamos o telhado contra o frio. | Nous isolons le toit contre le froid.
jogar os dados | jouer aux dés | Nós jogamos os dados para ver a ordem. | Nous jouons aux dés pour l'ordre.
julgar | juger | Ele será julgado na semana que vem. | On le juge la semaine prochaine.
jurar | jurer | Juro que não sabia. | Je te jure que je ne le savais pas.
justificar | justifier | Ele justifica o gasto com dois números. | Il justifie la dépense avec deux chiffres.
lamentar | regretter, être désolé | Eu lamentaria muito ter de recusar. | Un refus me peinerait beaucoup.
lavar a louça | laver la vaisselle | Depois de comer ele lava a louça. | Après le repas, il fait la vaisselle.
legislar | légiférer | O governo vai legislar sobre inteligência artificial. | Le gouvernement légiférera sur l'intelligence artificielle.
lesionar-se | se blesser | Ele lesionou-se aos vinte minutos. | Il s'est blessé à la vingtième minute. | pron
levar | apporter, amener | Ele leva as crianças para a creche todas as manhãs. | Il amène les enfants à la crèche tous les matins.
levar a | mener à, conduire (zu) | O caminho leva à estação. | Le chemin mène à la gare.
levar a sério | prendre à cœur | Eu levo o teu conselho a sério. | Je prends ton conseil à cœur.
libertar | libérer | Libertaram os reféns ao amanhecer. | Ils ont libéré les otages à l'aube.
limitar | limiter | Limitaram a lotação a cem pessoas. | Ils ont limité la jauge à cent personnes.
limitar-se | se limiter (à qch) | A visita limita-se ao centro histórico. | La visite se limite au centre historique. | pron
lutar | lutter | Eles lutam contra a exclusão desde 2010. | Ils luttent contre l'exclusion depuis 2010.
mandar por e-mail | envoyer par courriel | Eu mando-te o endereço por e-mail. | Je t'envoie l'adresse par courriel.
manejar | manier | O meu avô manejava o trator como ninguém. | Mon grand-père maniait le tracteur comme personne.
manifestar-se | s'exprimer | Ele manifestou-se de forma crítica sobre a proposta. | Il s'est exprimé de façon critique sur la proposition. | pron
maquiar | maquiller | Ela maquia-se todas as manhãs. | Elle se maquille chaque matin.
marginalizar | marginaliser | O sistema marginaliza os mais pobres. | Le système marginalise les plus pauvres.
massagear | masser | O fisioterapeuta massageia as costas dela. | Le physiothérapeute lui masse le dos.
matar | tuer | A geada matou as plantas. | Le gel a tué les plantes.
merecer | mériter | Ele merece um prémio pelo seu esforço. | Il mérite un prix pour son effort.
mergulhar | plonger | Ele gosta de mergulhar na água clara do lago. | Il aime plonger dans l'eau claire du lac.
mergulhar em | s'approfondir, se plonger dans | Eu mergulho no livro. | Je me plonge dans le livre.
mobiliar | aménager, meubler | Nós estamos a mobiliar o apartamento de novo. | Nous réaménageons l'appartement.
montar | assembler | Eles montam o motor em uma hora. | Ils assemblent le moteur en une heure.
morrer de fome | mourir de faim | Ainda bem que ninguém morreu de fome. | Heureusement, personne n'est mort de faim.
motivar | motiver | O professor motiva muito a turma. | Le professeur motive beaucoup la classe.
mudar-se para | emménager | No mês passado mudamo-nos para o apartamento novo. | Nous avons emménagé dans le nouvel appartement le mois dernier.
multar | verbaliser | Ele foi multado por excesso de velocidade. | Il a été verbalisé pour excès de vitesse.
narrar | raconter | Ele narra a história em primeira pessoa. | Il raconte l'histoire à la première personne.
naturalizar | naturaliser | O Estado naturaliza milhares de pessoas por ano. | L'État naturalise des milliers de personnes chaque année.
negar | nier | Ele nega qualquer relação com o caso. | Il nie tout lien avec l'affaire.
negligenciar | négliger | Ela negligenciava o trabalho. | Elle négligeait son travail.
negociar | négocier | Eles negociam o acordo esta semana. | Ils négocient l'accord cette semaine.
notar | remarquer | Notei que ele estava nervoso. | J'ai remarqué qu'il était nerveux.
obedecer | obéir | O cão obedece à minha irmã. | Le chien obéit à ma sœur.
obrigar | forcer, obliger | Ninguém te obriga a isso. | Personne ne t'y oblige.
obter | obtenir | Ela obteve a bolsa no ano passado. | Il a obtenu la bourse l'an dernier.
ocorrer | se produire | O acidente ocorreu de madrugada. | L'accident s'est produit à l'aube.
ocultar | cacher | Ele ocultou a verdade durante meses. | Il a caché la vérité pendant des mois.
ocupar-se de | s'occuper de (mit) | Eu ocupo-me do tema. | Je m'occupe du sujet.
ofender | offenser, insulter | Isso o ofenderia. | Ça l'offenserait.
oferecer | offrir, proposer | A cidade oferece muito para as famílias. | La ville offre beaucoup pour les familles.
operar | opérer | Ele foi operado do joelho. | On l'a opéré du genou.
opor | opposer | Ele opõe-se a qualquer mudança. | Il s'oppose à tout changement.
opor-se | s'opposer, résister | Eu oponho-me a esta regra. | Je m'oppose à cette règle. | pron
orbitar | orbiter | O satélite orbita a cada noventa minutos. | Le satellite orbite toutes les quatre-vingt-dix minutes.
ordenar | ordonner, disposer | O general ordena o ataque aos soldados. | Le général ordonne l'attaque aux soldats.
orientar-se | s'orienter | Eu oriento-me pelo mapa. | Je m'oriente avec la carte. | pron
ousar | oser | Eu não ousaria isso. | Je n'oserais pas ça.
pagar de volta | rembourser | Eu pago-te o dinheiro de volta. | Je te rembourse l'argent.
participar | participer | Participei do concurso no ano passado. | J'ai participé au concours l'an dernier.
patrocinar | parrainer | Um banco patrocina a equipa. | Une banque parraine l'équipe.
percorrer | parcourir | Percorremos o norte de comboio. | Nous avons parcouru le nord en train.
perdoar | pardonner | Ela perdoou tudo a ele. | Elle lui a tout pardonné.
peregrinar | faire un pèlerinage | Eles peregrinam a Santiago no verão. | Ils font le pèlerinage de Saint-Jacques l'été.
perguntar de novo | se renseigner, redemander | Eu pergunto pelo resultado. | Je demande le résultat.
pernoitar | passer la nuit, loger | Nós dormimos na casa de amigos. | Nous logeons chez des amis. | ex?
perseguir | poursuivre | A polícia perseguiu o ladrão. | La police a poursuivi le voleur.
persuadir | persuader | O anúncio persuade sem mentir. | La publicité persuade sans mentir.
pesar | peser | A mala pesa vinte quilos. | La valise pèse vingt kilos.
pesquisar no google | chercher sur Internet | Vou pesquisar a palavra rapidinho no Google. | Je cherche vite ce mot sur Internet.
picar | piquer | Os mosquitos picam mais à noite. | Les moustiques piquent surtout le soir.
pisar | marcher sur, donner un coup de pied | Não pisa nas flores, por favor. | Ne marche pas sur les fleurs, s'il te plaît.
postar | publier sur les réseaux | O político posta todos os dias. | L'homme politique publie chaque jour.
poupar | ménager, préserver | Ele poupava a bateria sempre que podia. | Il ménageait la batterie autant qu'il le pouvait.
praticar desporto | faire du sport | Ela pratica desporto regularmente no clube. | Elle fait régulièrement du sport dans un club.
prender | arrêter (police) | A polícia prende o criminoso. | La police arrête le coupable.
presenciar | assister à | Presenciamos um concerto inesquecível. | Nous avons assisté à un concert inoubliable.
pretender | avoir l'intention de | Ele pretende terminar a tese este ano. | Il a l'intention de finir sa thèse cette année.
prevenir | prévenir | O desporto previne muitas doenças. | Le sport prévient beaucoup de maladies.
prever | prévoir | Preveem chuva para o fim de semana. | Ils prévoient de la pluie pour le week-end.
produzir | produire | Eles produziram menos do que o planeado. | Ils produisaient moins que prévu.
programar | programmer | Eu programaria a irrigação para a noite. | Moi, je programmerais l'arrosage la nuit.
projetar | concevoir | Ele projetou o museu em 1998. | Il a conçu le musée en 1998.
prometer | promettre | Ele prometeu ligar ao chegar. | Il a promis d'appeler en arrivant.
promover | promouvoir | Vamos promover o produto na televisão. | Nous ferons la promotion du produit à la télévision.
pronunciar | prononcer | Como se pronuncia esta palavra? | Comment prononce-t-on ce mot ?
propor | proposer | Proponho começar pelo mais difícil. | Je propose de commencer par le difficile.
protestar | protester | Eles protestam contra o corte. | Ils protestent contre la coupe budgétaire.
provocar | provoquer | A tempestade provocou cortes de energia. | L'orage a provoqué des coupures de courant.
punir | punir | O professor pune os atrasos. | Le professeur punit le manque de ponctualité.
pôr em prática | mettre en œuvre | Nós pomos a ideia em prática. | Nous mettons l'idée en œuvre.
pôr em risco | mettre en danger | Fumar põe a saúde em risco. | Fumer met en danger la santé.
pôr prazo | limiter dans le temps | Eu poria o livro em outro lugar. | Je poserais le livre ailleurs.
questionar | remettre en question | Eu questiono a decisão. | Je remets en question la décision.
rasgar | déchirer, arracher | Um papel mais fino rasgaria na hora. | Un papier plus fin se déchirerait tout de suite.
realizar | réaliser, mettre en œuvre | Nós realizamos o projeto em dois anos. | Nous réalisions le projet en deux ans.
rebelar-se | se révolter | O povo rebelou-se contra o imposto. | Le peuple s'est révolté contre l'impôt. | pron
recompensar | récompenser | Eu recompenso o bom desempenho. | Je récompense les bonnes performances.
recuperar-se | se rétablir | Ele recuperou-se em três semanas. | Il s'est rétabli en trois semaines. | pron
recusar | refuser | Eu recuso a oferta. | Je refuse l'offre.
reembolsar | rembourser (des frais) | O seguro nos reembolsa os custos do arranjo. | L'assurance nous rembourse les frais de réparation.
refletir | réfléchir | Ele reflete antes de responder. | Il réfléchit avant de répondre.
refutar | réfuter | Eu refuto este argumento. | Je réfute cet argument.
registrar | enregistrer, remarquer | Ele registrou o incidente. | Il a enregistré l'incident.
regular | régler ; embaucher | Uma lei regula o horário de funcionamento. | Une loi régit les heures d'ouverture.
reivindicar | réclamer | Eles reivindicam um aumento de dez por cento. | Ils réclament une augmentation de dix pour cent.
relacionar | relier | Relacione cada palavra com a sua definição. | Relie chaque mot à sa définition.
relampejar | faire des éclairs | Lá fora já está a relampejar. | Dehors, il y a déjà des éclairs.
relatar | rapporter, raconter | O relato foi muito floreado. | Le récit a été largement enjolivé.
remoer | ruminer, se creuser la tête | Eu quebro a cabeça com a resposta. | Je me creuse la tête sur la réponse. | ex?
render-se | abandonner | Com um palhaço as crianças divertir-se-iam mais. | Avec un clown, les enfants s'amuseraient plus. | pron
renovar | rénover | A câmara municipal renovava uma rua por ano. | La mairie rénovait une rue chaque année.
renunciar | démissionner | Ele renunciou depois do escândalo. | Il a démissionné après le scandale.
repreender | réprimander | O chefe repreende os atrasos. | Le patron réprimande les retards.
representar | représenter | O quadro representa uma festa. | Le tableau représente une fête.
resfriar-se | attraper un rhume | No inverno eu resfrio-me com frequência. | J'attrape souvent un rhume en hiver. | pron
resistir | résister | A estrutura resistiu ao temporal. | La structure a résisté à la tempête.
respeitar | respecter | Respeitamos as opiniões dos outros. | Nous respectons les opinions des autres.
restaurar | restaurer | Eles restauram a fachada neste verão. | Ils restaurent la façade cet été.
resultar | s'avérer | O erro resultou da falta de tempo. | L'erreur résultait de la pression du temps.
reunir | réunir | Ele reuniu toda a equipa na segunda. | Il a réuni toute l'équipe lundi.
reunir-se | se réunir | Os voluntários reuniram-se todas as segundas. | Les bénévoles se sont réunis chaque lundi. | pron
revelar | révéler ; trahir | Eu nunca revelaria um segredo. | Je ne révélerais jamais un secret.
rezar | prier | Ele reza todas as noites antes de dormir. | Il prie chaque soir avant de dormir.
rodear | entourer | As montanhas rodeiam o vilarejo. | Les montagnes entourent le village.
rogar | prier, supplier | Roguei a ele que esperasse um minuto. | Je l'ai supplié d'attendre une minute.
romper | rompre | Eu romperia esse contrato agora mesmo. | Moi, je romprais ce contrat tout de suite.
sacar | retirer (de l'argent) | Saco cem euros no multibanco. | Je retire cent euros au distributeur.
sacudir | secouer | Agite bem antes de usar. | Bien agiter avant emploi. | ex?
sair-se | se classer, s'en sortir (résultat) | Ele sai-se bem na prova. | Il s'en sort bien à l'examen. | pron
sangrar | saigner | A minha mão está a sangrar. | Ma main saigne.
sarar | guérir | O ferimento sara em uma semana. | La blessure guérit en une semaine.
selecionar | sélectionner | Eles selecionaram dez candidatos. | Ils ont sélectionné dix candidats.
semear | semer | Eles semeiam o trigo em outubro. | Ils sèment le blé en octobre.
sentir falta de | manquer à quelqu'un | Eu sinto muita falta da minha família. | Ma famille me manque beaucoup.
sentir frio | avoir froid | No inverno eu sinto frio com frequência. | J'ai souvent froid en hiver.
ser cancelado | être annulé, ne pas avoir lieu | A aula de hoje foi cancelada. | Le cours a été annulé aujourd'hui.
ser promovido | être promu | Ela foi promovida a chefe de equipa. | Elle a été promue cheffe d'équipe.
silenciar | mettre en sourdine | Silenciei a conversa do grupo. | J'ai mis la conversation du groupe en sourdine.
simplificar | simplifier | Simplifique o texto para o folheto. | Simplifie le texte pour la brochure.
situar | situer | Situaram a fábrica ao lado do rio. | Ils ont situé l'usine près de la rivière.
situar-se | se situer | O mercado situava-se ao lado da igreja. | Le marché se situait à côté de l'église. | pron
socorrer | secourir | Socorreram os feridos na hora. | Ils ont secouru les blessés sur-le-champ.
sofrer | souffrir, subir | Eles sofrem com a falta de moradia. | Ils subissent le manque de logement.
soltar-se | partir ; se détacher | Soltei o barbante e o balão foi embora. | J'ai lâché la ficelle et le ballon s'est envolé. | pron
somar | additionner | Some as três quantias. | Additionne les trois montants.
soprar | souffler | A criança sopra as velas. | L'enfant souffle les bougies.
sortear | tirer au sort (officiellement) | A federação sorteia os confrontos. | La fédération tire au sort les rencontres.
suar | transpirer | Eu suo com esse calor. | Je transpire à cause de la chaleur.
sufocar | étouffer | Eu sufocaria naquela sala. | J'étoufferais dans cette pièce.
sugerir | suggérer | Sugiro que conversemos sobre isso amanhã. | Je suggère qu'on en parle demain.
superar | surmonter, dépasser | Ele superou a própria marca. | Il a dépassé sa propre marque.
supervisionar | superviser | Ele supervisionou as obras. | Il a supervisé les travaux.
supor | supposer | Suponho que ele vai chegar atrasado. | Je suppose qu'il arrivera en retard.
suprimir | supprimer | O editor suprimia as frases longas demais. | L'éditeur supprimait les phrases trop longues.
temperar | assaisonner | Tempero a salada com azeite e sal. | J'assaisonne la salade d'huile et de sel.
ter a ver | avoir affaire (à qch/qn) | A profissão dele tem muito a ver com turismo. | Son métier a beaucoup à voir avec le tourisme.
ter coragem | oser | Eu não tenho coragem de perguntar isso. | Je n'ose pas demander ça.
ter efeito sobre | avoir un effet sur (auf) | Isso tem um efeito negativo sobre o meio ambiente. | Ça a un effet négatif sur l'environnement.
ter medo | avoir peur, s'angoisser | Eu tenho medo da prova. | J'ai peur de l'examen.
ter razão | avoir raison | Se eu tivesse tempo, iria ao cinema. | Si j'avais le temps, j'irais au cinéma.
tirar a sorte | tirer au sort | Nós tiramos a sorte para ver quem começa. | On tire au sort qui commence.
tirar folga | prendre congé, se libérer | Ela tira uma tarde de folga para a visita guiada. | Elle se libère un après-midi pour la visite guidée.
transformar | transformer | Eles transformam o leite em queijo. | Ils transforment le lait en fromage.
transportar | transporter | O camião transporta os móveis. | Le camion transporte les meubles.
travar | freiner | O medo o travava na hora de falar. | La peur l'inhibait quand il parlait.
trovejar | tonner | Está a trovejar há uma hora. | Il tonne depuis une heure.
unir | unir | Uniram as duas mesas para o jantar. | Ils ont réuni les deux tables pour le dîner.
vacinar | vacciner | O médico vacina as crianças no outono. | Le médecin vaccine les enfants à l'automne.
valer | valoir | Este quadro vale uma fortuna. | Ce tableau vaut une fortune.
valorizar | apprécier, évaluer | Eles valorizam muito a pontualidade. | Ils apprécient beaucoup la ponctualité.
vencer | vaincre, expirer | O prazo vence na sexta. | Le délai expire vendredi.
vigiar | surveiller | Vigie a panela enquanto eu saio. | Surveille la casserole pendant que je sors.
vir de | provenir, être originaire de | A minha família vem da Anatólia. | Ma famille est originaire d'Anatolie.
vir à cabeça | venir à l'esprit | Ele viria junto com prazer, se pudesse. | Il viendrait volontiers, s'il le pouvait.
virar-se | se débrouiller, s'en sortir | Com um manual eu virar-me-ia melhor. | Avec une notice, je m'en sortirais mieux. | pron
votar | voter | Sempre voto nas eleições municipais. | Je vote toujours aux municipales.
zombar | se moquer | Não zombe do sotaque dele. | Ne te moque pas de son accent.
zombar de | se moquer de | As crianças não zombam dele. | Les enfants ne se moquent pas de lui.
"""

# « masculin | feminin | traduction | phrase | sa traduction | drapeaux ».
ADJECTIFS = """
absoluto | absoluta | absolu | Ele exige silêncio absoluto. | Il exige un silence absolu.
abundante | abundante | abondant | A colheita foi abundante. | La récolte a été abondante.
acessível | acessível | accessible | O museu é acessível para cadeira de rodas. | Le musée est accessible en fauteuil roulant.
acima da média | acima da média | au-dessus de la moyenne | Ela ganha um salário acima da média. | Elle gagne un salaire au-dessus de la moyenne.
aclamado | aclamada | acclamé | É um espetáculo muito aclamado. | C'est un spectacle très acclamé.
adaptado | adaptada | adapté | É um apartamento adaptado. | C'est un appartement adapté.
adaptável | adaptável | adaptable | Ela adapta-se muito bem a situações novas. | Elle s'adapte très bien aux nouvelles situations. | ex?
adequado | adequada | adéquat | Não é o momento adequado. | Ce n'est pas le moment adéquat.
adicional | adicional | supplémentaire | Há taxas adicionais para este serviço. | Il y a des frais supplémentaires pour ce service.
agrícola | agrícola | agricole | É uma zona agrícola. | C'est une zone agricole.
agudo | aguda | aigu | Ele sentiu uma dor aguda no joelho. | Il a senti une douleur aiguë au genou.
alheio | alheia | d'autrui | Não mexa no que é alheio. | Ne touche pas à ce qui est à autrui.
alongado | alongada | allongé | Ele tem o rosto alongado. | Il a le visage allongé.
alternativo | alternativa | alternatif, autre | Existe um caminho alternativo? | Y a-t-il un autre chemin ?
altruísta | altruísta | altruiste | Foi um gesto altruísta. | Ce fut un geste altruiste.
alérgico | alérgica | allergique (à qch) | Ele é alérgico a castanhas. | Il est allergique aux noix.
ambicioso | ambiciosa | ambitieux | Ele é um rapaz ambicioso. | C'est un jeune homme ambitieux.
ameno | amena | doux (climat, goût) | O inverno foi ameno este ano. | L'hiver a été doux cette année.
ansioso | ansiosa | impatient, curieux | Eu estava ansioso pelas férias. | Je me réjouissais des vacances.
antigo | antiga | ancien | É um prédio muito antigo. | C'est un bâtiment très ancien.
anual | anual | annuel | Os custos anuais da conta são baixos. | Les frais annuels du compte sont faibles.
anónimo | anónima | anonyme | Ele recebeu uma mensagem anónima. | Il a reçu un message anonyme.
ao mesmo tempo | ao mesmo tempo | simultané | Ele é professor e músico ao mesmo tempo. | Il est enseignant et musicien à la fois.
ao norte | ao norte | au nord, septentrional | O vilarejo fica ao norte da cidade. | Le village se trouve au nord de la ville.
ao sul | ao sul | au sud, méridional | Ao sul dos Alpes é mais quente. | Au sud des Alpes, il fait plus chaud.
ao vivo | ao vivo | en direct | O jogo vai ser transmitido ao vivo. | Le match est retransmis en direct.
aos poucos | aos poucos | progressivement, peu à peu | Aos poucos ela acostuma-se com o novo país. | Elle s'habitue peu à peu au nouveau pays.
apropriado | apropriada | approprié | Procure um tom mais apropriado. | Cherche un ton plus approprié.
aproximado | aproximada | approximatif | É um número aproximado. | C'est un chiffre approximatif.
arriscado | arriscada | risqué | É um investimento arriscado. | C'est un investissement risqué.
arrogante | arrogante | arrogant | O tom dele foi bem arrogante. | Son ton était plutôt arrogant.
atento | atenta | attentif | Os alunos estavam muito atentos. | Les élèves étaient très attentifs.
ativo | ativa | actif | Ele continua ativo aos oitenta anos. | Il reste actif à quatre-vingts ans.
ausente | ausente | absent | Três alunos estão ausentes hoje. | Trois élèves sont absents aujourd'hui.
autorizado | autorizada | autorisé, fondé | Só os moradores têm autorização para estacionar. | Seuls les riverains sont autorisés à stationner. | ex?
autêntico | autêntica | authentique | É couro autêntico. | C'est du cuir authentique.
avançado | avançada | avancé | É uma técnica muito avançada. | C'est une technique très avancée.
bem | bem | assez, plutôt (ennuyeux) | A palestra foi bem chata. | La conférence était plutôt ennuyeuse.
bem cozido | bem cozido | cuit à point ; (gar nicht) pas du tout | Não gosto disso nem um pouco. | Cela ne me plaît pas du tout. | ex?
bem-humorado | bem-humorada | plein d'humour/sans humour | O colega novo tem muito senso de humor. | Le nouveau collègue a beaucoup d'humour. | ex?
bem-sucedido | bem-sucedida | réussi | Foi um lançamento bem-sucedido. | Ce fut un lancement réussi.
benéfico | benéfica | bénéfique | A mudança foi benéfica para todos. | Le changement a été bénéfique pour tous.
bilíngue | bilíngue | bilingue | Os filhos dele são bilíngues. | Ses enfants sont bilingues.
brilhante | brilhante | brillant | Ele teve uma ideia brilhante. | Il a eu une idée brillante.
bruto | bruta | brut | O salário bruto não é o líquido. | Le salaire brut n'est pas le net.
básico | básica | basique | A medida violou um direito básico. | La mesure a porté atteinte à un droit fondamental.
bêbado | bêbada | ivre, saoul |  |  | ex=?
caloroso | calorosa | chaleureux | Deram-nos uma receção calorosa. | Ils nous ont réservé un accueil chaleureux.
caseiro | caseira | fait maison | A sobremesa é caseira. | Le dessert est fait maison.
categórico | categórica | catégorique | Foi um não categórico. | Ce fut un non catégorique.
católico | católica | catholique | Ele foi criado na fé católica. | Il a été élevé dans la religion catholique.
caótico | caótica | chaotique | A mesa dele parece uma confusão. | Son bureau a l'air chaotique. | ex?
cego | cega | aveugle | Ele é cego de nascença. | Il est aveugle de naissance.
chamativo | chamativa | voyant, accrocheur | É um cartaz muito chamativo. | C'est une affiche très accrocheuse.
cheio de tato | cheio de tato | plein de tact | Ela resolveu a situação com muito tato. | Elle a résolu la situation avec beaucoup de tact. | ex?
científico | científica | scientifique | É um artigo científico. | C'est un article scientifique.
civil | civil | civil | Eles casaram-se no civil. | Ils se sont mariés civilement.
coletivo | coletiva | collectif | Foi uma decisão coletiva. | Ce fut une décision collective.
com deficiência | com deficiência | handicapé | A associação ajuda pessoas com deficiência. | L'association aide les personnes handicapées.
com direitos iguais | com direitos iguais | égal en droits | No desporto homens e mulheres nem sempre têm direitos iguais. | Les hommes et les femmes ne sont pas toujours égaux dans le sport. | ex?
compartilhado | compartilhada | partagé | Eles trabalham em um espaço compartilhado. | Ils travaillent dans un espace partagé.
compassivo | compassiva | compatissant | Ele reagiu à notícia com muita compaixão. | Il a réagi avec beaucoup de compassion à la nouvelle. | ex?
competente | competente | compétent | Ele tem uma equipa muito competente. | Il a une équipe très compétente.
competitivo | competitiva | compétitif | É um campeonato muito competitivo. | C'est un championnat très compétitif.
completamente | completamente | complètement, totalement | É uma situação completamente nova para ele. | C'est une situation complètement nouvelle pour lui.
completo | completa | complet | Por favor, preencha o formulário por completo. | Veuillez remplir le formulaire entièrement.
complexo | complexa | complexe | É um problema complexo. | C'est un problème complexe.
compreensível | compreensível | compréhensible | A decisão dele é bem compreensível. | Sa décision est facile à comprendre.
concentrado | concentrada | concentré | Ela trabalha muito concentrada. | Elle travaille de façon très concentrée.
concreto | concreta | concret | Dê-me um exemplo concreto. | Donne-moi un exemple concret.
confiável | confiável | fiable | O meu colega é muito confiável. | Mon collègue est très fiable.
confuso | confusa | confus | A mensagem era confusa. | Le message était confus.
congestionado | congestionada | encombré | O centro fica congestionado às oito. | Le centre est encombré à huit heures.
consciente | consciente | conscient | Ele está consciente do problema. | Il est conscient du problème.
conservador | conservadora | conservateur | As opiniões dele são bem conservadoras. | Ses opinions sont plutôt conservatrices.
constante | constante | constant | Há um barulho constante na rua. | Il y a un bruit constant dans la rue.
constrangedor | constrangedora | embarrassant, gênant | Fiquei morrendo de vergonha. | J'étais vraiment gêné. | ex?
contagioso | contagiosa | contagieux | A gripe é muito contagiosa. | La grippe est très contagieuse.
contemporâneo | contemporânea | contemporain | É um prédio contemporâneo. | C'est un bâtiment contemporain.
contrário | contrária | contraire | Ele foi para o lado contrário. | Il est allé du côté contraire.
contínuo | contínua | continu | Ele precisa de atenção contínua. | Il a besoin d'une attention continue.
convencido | convencida | convaincu | Estou convencido de que ele tem razão. | Je suis convaincu qu'il a raison.
convincente | convincente | convaincant | A resposta dele foi convincente. | Sa réponse a été convaincante.
correto | correta | correct | A resposta correta é a segunda. | La bonne réponse est la deuxième.
cosmético | cosmética | cosmétique | É só uma mudança superficial. | Ce n'est qu'un changement cosmétique. | ex?
cotidiano | cotidiana | quotidien | São gestos cotidianos, sem importância. | Ce sont des gestes quotidiens, sans importance.
criativo | criativa | créatif | Ele tem uma equipa criativa. | Il a une équipe créative.
crítico | crítica | critique | Chegamos a um ponto crítico. | Nous arrivons à un point critique.
crónico | crónica | chronique | É uma dor crónica. | C'est une douleur chronique.
culpado | culpada | coupable | Ele declarou-se culpado. | Il s'est déclaré coupable.
cultural | cultural | culturel | Há uma diferença cultural clara. | Il y a une différence culturelle nette.
custoso | custosa | coûteux | O arranjo foi caro. | La réparation a été coûteuse. | ex?
da mesma idade | da mesma idade | du même âge | Ela gosta de brincar com crianças da mesma idade. | Elle aime jouer avec des enfants du même âge.
de língua inglesa | de língua inglesa | anglophone/germanophone | Ele está a procurar um jornal em inglês. | Il cherche un journal anglophone. | ex?
de peões | de peões | piétonnier | A rua de peões está cheia. | La rue piétonne est pleine.
de vários anos | de vários anos | pluriannuel, de plusieurs années | Ela tem vários anos de experiência na área. | Elle a une expérience de plusieurs années dans ce domaine. | ex?
decepcionado | decepcionada | déçu | Ele ficou decepcionado com o resultado. | Il était déçu du résultat.
decepcionante | decepcionante | décevant | O resultado foi bem decepcionante. | Le résultat était assez décevant.
decisivo | decisiva | décisif | Foi um momento decisivo. | Ce fut un moment décisif.
delicado | delicada | délicat | É um assunto delicado. | C'est une affaire délicate.
democrático | democrática | démocratique | A decisão foi democrática. | La décision a été démocratique.
desajeitado | desajeitada | maladroit | Sou desajeitado com as mãos. | Je suis maladroit de mes mains.
desatento | desatenta | inattentif | Ele estava desatento na aula. | Il n'était pas attentif en cours.
desconfiado | desconfiada | méfiant | Ela desconfiava de estranhos. | Elle était méfiante envers les inconnus. | ex?
desconhecido | desconhecida | inconnu | A causa continua desconhecida. | La cause reste inconnue.
descontraído | descontraída | détendu, relâché | A relação entre eles é bem descontraída. | La relation entre eux est plutôt décontractée.
desejável | desejável | souhaitable | Seria desejável avisar antes. | Il serait souhaitable de prévenir avant.
desesperado | desesperada | désespéré | Ela procurava a chave desesperadamente. | Elle cherchait désespérément sa clé. | ex?
desigual | desigual | inégal | A distribuição é desigual. | La répartition est inégale.
desinteressado | desinteressada | désintéressé | Foi uma ajuda desinteressada. | Ce fut une aide désintéressée.
desnecessário | desnecessária | inutile | Esse gasto era desnecessário. | Cette dépense était inutile.
desobediente | desobediente | désobéissant | A criança foi desobediente hoje. | L'enfant a été désobéissant aujourd'hui.
destemido | destemida | sans peur | O bombeiro agiu sem medo. | Le pompier a agi sans peur. | ex?
devido | devida | dû, à échéance |  |  | ex=?
digno | digna | digne | Ele manteve uma atitude digna. | Il a gardé une attitude digne.
diplomático | diplomática | diplomate | O chefe reagiu às críticas com diplomacia. | Le chef a réagi avec diplomatie face à la critique. | ex?
disciplinado | disciplinada | discipliné | A atleta treina com muita disciplina. | L'athlète s'entraîne de façon très disciplinée. | ex?
disposto a ceder | disposto a ceder | prêt au compromis | Os dois lados estavam dispostos a ceder. | Les deux parties étaient prêtes au compromis. | ex?
distraído | distraída | distrait | Ele estava distraído com o barulho. | Il était distrait par le bruit.
diverso | diversa | divers | O bairro é muito diverso. | Le quartier est très divers.
duradouro | duradoura | durable | Procuro algo duradouro. | Je cherche quelque chose de durable.
duvidoso | duvidosa | douteux | O dado parece-me duvidoso. | La donnée me semble douteuse.
educativo | educativa | éducatif | É um programa educativo. | C'est un programme éducatif.
eletrónico | eletrónica | électronique | A inscrição só pode ser feita on-line. | L'inscription se fait uniquement par voie électronique. | ex?
elevado | elevada | élevé | O custo é elevado. | Le coût est élevé.
elétrico | elétrica | électrique | Ele comprou um carro elétrico. | Il a acheté une voiture électrique.
em forma | em forma | en forme | Por favor, faça um currículo em forma de tabela. | Veuillez rédiger un CV sous forme de tableau.
em princípio | em princípio | fondamental, en principe | Em princípio eu concordo. | En principe, je suis d'accord.
emocional | emocional | émotionnel | Foi uma reação emocional. | Ce fut une réaction émotionnelle.
engajado | engajada | engagé, impliqué | Ele é um funcionário muito dedicado. | C'est un employé très engagé. | ex?
enganoso | enganosa | trompeur | É um anúncio enganoso. | C'est une publicité trompeuse.
entediado | entediada | qui s'ennuie | Os alunos pareciam entediados. | Les élèves avaient l'air de s'ennuyer.
entusiasmado | entusiasmada | enthousiaste | Os fãs ficaram encantados com o concerto. | Les fans étaient enthousiasmés par le concert. | ex?
equilibrado | equilibrada | équilibré | Ele segue uma dieta equilibrada. | Il suit un régime équilibré.
equitativo | equitativa | équitable | Eles buscam uma divisão equitativa. | Ils cherchent un partage équitable.
escondido | escondida | caché | A chave está escondida debaixo do tapete. | La clé est cachée sous le paillasson.
espacial | espacial | spatial | É uma missão espacial. | C'est une mission spatiale.
especial | especial | spécial | Prepararam um menu especial. | Ils ont préparé un menu spécial.
específico | específica | spécifique | Precisamos de uma ferramenta específica. | Il nous faut un outil spécifique.
esperançoso | esperançosa | plein d'espoir | Ele olha para o futuro com esperança. | Il envisage l'avenir avec espoir. | ex?
espontâneo | espontânea | spontané | Foi uma reação espontânea. | Ce fut une réaction spontanée.
essencial | essencial | essentiel | A água é essencial para a vida. | L'eau est essentielle à la vie.
estatístico | estatística | statistique | A estatística mostra uma tendência clara. | La statistique montre une tendance claire.
estilístico | estilística | stylistique | O texto tem erros de estilo. | Le texte a des fautes de style. | ex?
estrangeiro | estrangeira | étranger | Temos muitos hóspedes estrangeiros. | Nous avons beaucoup d'hôtes étrangers.
estressado | estressada | stressé | Antes da prova ele estava muito estressado. | Avant l'examen, il était très stressé.
estrito | estrita | strict | Eles seguem um horário rigoroso. | Ils suivent un horaire strict. | ex?
estável | estável | stable | Ele procura um emprego estável. | Il cherche un emploi stable.
eterno | eterna | éternel | A espera pareceu-me eterna. | L'attente m'a paru éternelle.
evangélico | evangélica | protestant, évangélique | A família dele é protestante. | Sa famille est protestante. | ex?
eventual | eventual | éventuel, éventuellement | Talvez eu chegue mais tarde. | Éventuellement, je viendrai plus tard. | ex?
exato | exata | exact | Não sei o número exato. | Je ne connais pas le chiffre exact.
exausto | exausta | épuisé | Depois da maratona ela estava completamente exausta. | Après le marathon, elle était complètement épuisée.
excelente | excelente | excellent | A comida estava excelente. | Le repas était excellent.
experiente | experiente | expérimenté | Ele é um piloto experiente. | C'est un pilote expérimenté.
explícito | explícita | explicite | Precisamos de uma permissão explícita. | Il nous faut une autorisation explicite.
externo | externa | externe | Contrataram um auditor externo. | Ils ont engagé un auditeur externe.
extremo | extrema | extrême | O tempo foi extremo este ano. | Le temps a été extrême cette année.
exótico | exótica | exotique | A cidade tem um charme exótico. | La ville a un charme exotique.
falso | falsa | faux | A nota era falsa. | Le billet s'est avéré faux.
fantástico | fantástica | fantastique | Passamos um fim de semana fantástico. | Nous avons passé un week-end fantastique.
fascinante | fascinante | fascinant | A história da região é fascinante. | L'histoire de la région est fascinante.
favorável | favorável | favorable | O relatório é favorável ao projeto. | Le rapport est favorable au projet.
feminino | feminina | féminin, de sexe féminin | A equipa tem três mulheres. | L'équipe compte trois membres féminins. | ex?
financeiro | financeira | financier | É um problema financeiro grave. | C'est un problème financier grave.
fixo | fixa | fixe, ferme | Agora ela há um emprego fixo. | Elle a maintenant un poste fixe.
fluente | fluente | courant (langue) | Ela fala alemão fluentemente. | Elle parle couramment l'allemand. | ex?
formado | formada | formé, qualifié | Ela é enfermeira formada. | Elle est infirmière diplômée.
formal | formal | formel | É uma carta formal. | C'est une lettre formelle.
frequente | frequente | fréquent | O Autocarro é frequente na hora do rush. | Le bus est fréquent aux heures de pointe.
fundamental | fundamental | fondamental | É um direito fundamental. | C'est un droit fondamental.
futuro | futura | futur | Pense nas gerações futuras. | Pense aux générations futures.
fértil | fértil | fertile | O vale é muito fértil. | La vallée est très fertile.
físico | física | physique | Exige um esforço físico considerável. | Cela demande un effort physique important.
genial | genial | génial | Foi uma ideia genial. | C'était une idée géniale.
geral | geral | général | A impressão geral é boa. | L'impression générale est bonne.
grato | grata | reconnaissant | Sou muito grato pela tua ajuda. | Je te suis très reconnaissant pour ton aide.
gótico | gótica | gothique | É uma catedral gótica. | C'est une cathédrale gothique.
habitual | habitual | habituel | Ele chegou na hora habitual. | Il est arrivé à l'heure habituelle.
histórico | histórica | historique | Foi um momento histórico. | Ce fut un moment historique.
horizontal | horizontal | horizontal | Coloque a tábua na horizontal. | Posez la planche à l'horizontale.
humano | humana | humain | É um erro totalmente humano. | C'est une erreur tout à fait humaine.
ideal | ideal | idéal | É o lugar ideal para ler. | C'est l'endroit idéal pour lire.
idealista | idealista | idéaliste | Ele tem uma visão idealista do trabalho. | Il a une vision idéaliste du travail.
idêntico | idêntica | identique | Os dois textos são idênticos. | Les deux textes sont identiques.
ilegal | ilegal | illégal | Estacionar ali é ilegal. | Se garer là est illégal.
ilógico | ilógica | illogique | O argumento parece ilógico. | L'argument semble illogique.
imediato | imediata | immédiat | A resposta foi imediata. | La réponse a été immédiate.
impaciente | impaciente | impatient | Ele fica impaciente rápido. | Il devient vite impatient.
impressionante | impressionante | impressionnant | A vista lá de cima é impressionante. | La vue d'en haut est impressionnante.
imprevisível | imprevisível | imprévisible | O tempo é imprevisível aqui. | Le temps est imprévisible ici.
inclusivo | inclusiva | inclusif | É uma escola inclusiva. | C'est une école inclusive.
incompetente | incompetente | incompétent | O funcionário parecia totalmente incompetente. | L'employé paraissait totalement incompétent.
incrível | incrível | incroyable | Ele contou uma história incrível. | Il a raconté une histoire incroyable.
incómodo | incómoda | gênant | Os incómodos sumiram depois de uma semana. | Les troubles ont disparu au bout d'une semaine.
indeciso | indecisa | indécis ; match nul | O jogo terminou empatado. | Le match s'est terminé par un nul. | ex?
independente | independente | indépendant | Ele vive de forma independente. | Il vit de façon indépendante.
indiferente | indiferente | indifférent | O resultado é totalmente indiferente para ele. | Le résultat lui est complètement indifférent.
indireto | indireta | indirect | Ele recebeu uma resposta indireta. | Il a reçu une réponse indirecte.
indisciplinado | indisciplinada | indiscipliné | A turma estava bem indisciplinada hoje. | La classe était plutôt indisciplinée aujourd'hui.
individual | individual | individuel | Cada um tem um armário individual. | Chacun a un casier individuel.
industrial | industrial | industriel | É um polo industrial. | C'est une zone industrielle.
inesperado | inesperada | inattendu | Foi uma visita inesperada. | Ce fut une visite inattendue.
inesquecível | inesquecível | inoubliable | Foi uma noite inesquecível. | Ce fut une nuit inoubliable.
inexperiente | inexperiente | inexpérimenté | Como estagiário ele ainda é inexperiente. | En tant que stagiaire, il est encore inexpérimenté.
inferior | inferior | inférieur | A qualidade é inferior à esperada. | La qualité est inférieure à celle attendue.
infiel | infiel | infidèle | Ele foi infiel à companheira. | Il a été infidèle à sa partenaire.
infinito | infinita | infini | O universo parece infinito. | L'univers semble infini.
informal | informal | informel | Foi uma reunião informal. | Ce fut une réunion informelle.
injusto | injusta | injuste | Foi uma decisão injusta. | Ce fut une décision injuste.
inocente | inocente | innocent | O tribunal o declarou inocente. | Le tribunal l'a déclaré innocent.
insatisfeito | insatisfeita | insatisfait | Muitos funcionários estão insatisfeitos com o salário. | Beaucoup d'employés sont insatisfaits de leur salaire.
insensato | insensata | déraisonnable | Seria insensato desistir agora. | Ce serait déraisonnable d'abandonner maintenant.
insuficiente | insuficiente | insuffisant | As provas são insuficientes. | Les preuves sont insuffisantes.
integral | integral | complet | Prefiro arroz integral. | Je préfère le riz complet.
inteiro | inteira | entier | Ele comeu o pão inteiro. | Il a mangé le pain entier.
intensivo | intensiva | intensif, intense | Estamos a fazer um curso intensivo de línguas. | Nous suivons un cours de langue intensif.
intercultural | intercultural | interculturel | A escola oferece projetos interculturais. | L'école propose des projets interculturels.
interior | interior | intérieur | Os meus avós viviam no interior. | Mes grands-parents vivaient à la campagne.
intermediário | intermediária | intermédiaire | Estou em um nível intermediário. | Je suis à un niveau intermédiaire.
internacional | internacional | international | Ele trabalha em uma empresa internacional. | Il travaille dans une entreprise internationale.
intolerante | intolerante | intolérant | Ela não tolera críticas. | Elle est intolérante face à la critique. | ex?
invejoso | invejosa | envieux | Ela tem inveja da irmã. | Elle est envieuse de sa sœur. | ex?
invicto | invicta | invaincu |  |  | ex=?
irritante | irritante | agaçant, contrarié | O barulho do vizinho é realmente irritante. | Le bruit du voisin est vraiment agaçant.
junto | junta | ensemble | Guardamos as fotos juntas. | Nous rangeons les photos ensemble.
jurídico | jurídica | juridique, légal | Do ponto de vista jurídico isso não é problema. | Sur le plan juridique, ce n'est pas un problème.
laico | laica | laïque | É um Estado laico. | C'est un État laïque.
liberal | liberal | libéral | Ele defende valores liberais. | Il défend des valeurs libérales.
limitado | limitada | limité | As vagas são limitadas. | Les places sont limitées.
literário | literária | littéraire | É um prémio literário importante. | C'est un prix littéraire important.
local | local | local | Compramos produtos locais. | Nous achetons du produit local.
loucamente | loucamente | fou, énorme (intensif) | Isso gasta uma quantidade enorme de energia. | Cela coûte énormément d'énergie. | ex?
luxuoso | luxuosa | luxueux | Eles hospedaram-se em um hotel luxuoso. | Ils ont logé dans un hôtel luxueux.
líder | líder | leader | É a empresa líder do setor. | C'est l'entreprise leader du secteur.
lógico | lógica | logique | É a conclusão lógica. | C'est la conclusion logique.
maduro | madura | mûr | O abacate já está maduro. | L'avocat est déjà mûr.
magnífico | magnífica | magnifique | Ele fez um trabalho magnífico. | Il a fait un travail magnifique.
majestoso | majestosa | majestueux | O aqueduto é majestoso. | L'aqueduc est majestueux.
manual | manual | manuel | É um trabalho manual. | C'est un travail manuel.
medieval | medieval | médiéval | A ponte é medieval. | Le pont est médiéval.
medroso | medrosa | craintif, anxieux | A criança é muito medrosa. | L'enfant est très craintif.
meio | meia | demi | Já estou a esperar há meia hora. | J'attends déjà depuis une demi-heure.
mensal | mensal | mensuel | Recebemos um boletim mensal. | Nous recevons un bulletin mensuel.
mental | mental | mental | Ele fez um cálculo mental rápido. | Il a fait un calcul mental rapide.
mesquinho | mesquinha | mesquin, tatillon | O chefe dele às vezes é bem implicante. | Son patron est parfois plutôt mesquin. | ex?
misterioso | misteriosa | mystérieux | Ele recebeu uma carta misteriosa. | Il a reçu une lettre mystérieuse.
modesto | modesta | modeste | Apesar do sucesso, ele continua humilde. | Malgré son succès, il reste modeste. | ex?
montanhoso | montanhosa | montagneux | É uma região montanhosa. | C'est une région montagneuse.
morno | morna | tiède | O café já está morno. | Le café est déjà tiède.
mortal | mortal | mortel | Foi um erro fatal para o projeto. | Ce fut une erreur mortelle pour le projet. | ex?
motivado | motivada | motivé | A nova estagiária está muito motivada. | La nouvelle stagiaire est très motivée.
multilíngue | multilíngue | plurilingue/unilingue | A escola oferece um ensino multilíngue. | L'école propose un enseignement plurilingue.
mundial | mundial | mondial | Ele bateu o recorde mundial. | Il a battu le record mondial.
municipal | municipal | municipal, urbain | É uma piscina municipal. | C'est une piscine municipale.
muscular | muscular | musculaire | Ele tem uma lesão muscular. | Il a une lésion musculaire.
médico | médica | médical | Ele precisa de um laudo médico. | Il a besoin d'un rapport médical.
móvel | móvel | mobile | Eles compraram móveis novos. | Ils ont acheté de nouveaux meubles.
mútuo | mútua | mutuel | Eles chegaram a um acordo mútuo. | Ils sont parvenus à un accord mutuel.
nacional | nacional | national | É um feriado nacional. | C'est une fête nationale.
nada | nada | du tout (pas bon du tout) | Isso não está nada saboroso. | Ça n'a pas bon goût du tout.
negativo | negativa | négatif | O balanço foi negativo. | Le bilan a été négatif.
noturno | noturna | nocturne | Há um Autocarro noturno aos sábados. | Il y a un bus de nuit le samedi.
notável | notável | notable | Houve uma melhora notável. | Il y a eu une amélioration notable.
nu | nua | nu | No inverno as árvores ficam nuas. | Les arbres sont nus en hiver.
nuclear | nuclear | nucléaire | A usina nuclear fecha em 2035. | La centrale nucléaire ferme en 2035.
nítido | nítida | net | A imagem é nítida mesmo à noite. | L'image est nette même de nuit.
obediente | obediente | obéissant | O cão é muito obediente. | Le chien est très obéissant.
obrigado | obrigada | tenu, obligé | Todo mundo é obrigado a fazer o registo. | Chacun est tenu de s'inscrire.
obrigatório | obrigatória | obligatoire | A presença é obrigatória. | La présence est obligatoire.
oficial | oficial | officiel | Ainda não há resposta oficial. | Il n'y a pas encore de réponse officielle.
oral | oral | oral | A prova tem uma parte oral. | L'examen comporte une partie orale.
orgânico | orgânica | biologique | Ela só compra legumes orgânicos. | Elle n'achète que des légumes biologiques.
original | original | initial, à l'origine | Guarde o documento original. | Garde le document original.
otimista | otimista | optimiste | Ele continua otimista apesar de tudo. | Il reste optimiste malgré tout.
outro | outra | autre, supplémentaire | O senhor tem outras perguntas? | Avez-vous d'autres questions ?
oval | oval | ovale |  |  | ex=?
pacífico | pacífica | pacifique | Foi um protesto pacífico. | Ce fut une manifestation pacifique.
paralelo | paralela | parallèle | As duas ruas são paralelas. | Les deux rues sont parallèles.
parecido | parecida | semblable, similaire | As duas palavras soam parecidas. | Les deux mots se ressemblent.
parente | parente | apparenté, de la famille | Somos parentes distantes. | Nous sommes parents éloignés.
parvo | parva | bête | Foi um erro parvo. | Ce fut une erreur bête.
passivo | passiva | passif | Na aula ele é meio passivo. | En cours, il est plutôt passif.
perfeito | perfeita | parfait | O horário é perfeito para mim. | L'horaire est parfait pour moi.
pessimista | pessimista | pessimiste | Não seja tão pessimista. | Ne sois pas si pessimiste.
pessoal | pessoal | personnel, en personne | É uma decisão pessoal. | C'est une décision personnelle.
pitoresco | pitoresca | pittoresque | É um vilarejo pitoresco. | C'est un village pittoresque.
poderoso | poderosa | puissant | É um argumento poderoso. | C'est un argument puissant.
poluente | poluente | polluant | É a indústria mais poluente. | C'est l'industrie la plus polluante.
político | política | politique | É uma decisão política, não técnica. | C'est une décision politique, pas technique.
popular | popular | populaire | É uma festa muito popular. | C'est une fête très populaire.
por escrito | por escrito | écrit/oral | Por favor, confirme isso por escrito. | Veuillez le confirmer par écrit.
positivo | positiva | positif | O resultado foi positivo. | Le résultat a été positif.
pouco confiável | pouco confiável | peu fiable | Infelizmente ele não é muito confiável. | Il est malheureusement plutôt peu fiable. | ex?
pouco saudável | pouco saudável | malsain/sain | Comida pronta muitas vezes não é saudável. | Les plats préparés sont souvent malsains. | ex?
preferível | preferível | préférable | É preferível avisar antes. | Il est préférable de prévenir avant.
prejudicial | prejudicial | nocif | O excesso de sal é prejudicial. | L'excès de sel est nocif.
preocupado | preocupada | inquiet | Ele está preocupado com a prova. | Il est inquiet pour l'examen.
presente | presente | présent, sur place | Todos os inquilinos estavam presentes na reunião. | Tous les locataires étaient présents à la réunion.
prestativo | prestativa | serviable | A minha vizinha é sempre prestativa. | Ma voisine est toujours serviable.
preventivo | preventiva | préventif | É uma medida preventiva. | C'est une mesure préventive.
previsto | prevista | prévu, probablement | Acabou sendo mais fácil do que o previsto. | Ça s'est avéré plus facile que prévu.
prezado | prezada | honoré (formule d'appel) | Prezados senhores e senhoras, | Madame, Monsieur,
profissional | profissional | professionnel | Ele mantém um tom profissional. | Il garde un ton professionnel.
progressista | progressista | progressiste | A empresa tem uma política progressista. | L'entreprise a une politique progressiste.
punível | punível | punissable, répréhensible | Isso é crime e sai caro. | C'est répréhensible et cela coûte cher. | ex?
puro | pura | pur | É lã pura. | C'est de la laine pure.
pálido | pálida | pâle |  |  | ex=?
pão-duro | pão-dura | avare | O homem pão-duro nunca dá gorjeta. | L'homme avare ne donne jamais de pourboire.
péssimo | péssima | exécrable | O serviço foi péssimo. | Le service a été exécrable.
público | pública | public | O transporte público é barato aqui. | Les transports publics sont bon marché ici.
quadrado | quadrada | carré | Temos uma mesa quadrada na cozinha. | Nous avons une table carrée dans la cuisine.
qualificado | qualificada | qualifié | Falta pessoal qualificado. | Il manque du personnel qualifié.
que se conserva | que se conserva | qui se conserve | O leite ainda dura uma semana. | Le lait se conserve encore une semaine. | ex?
quieto | quieta | immobile | Fique quieto um momento, por favor. | Tais-toi un instant, s'il te plaît.
racional | racional | rationnel | Ele busca uma explicação racional. | Il cherche une explication rationnelle.
razoável | razoável | raisonnable | O preço parece-me razoável. | Le prix me paraît raisonnable.
realista | realista | réaliste | É um romance realista. | C'est un roman réaliste.
realmente | realmente | vraiment (bon) | Foi um filme realmente bom. | C'était vraiment un bon film.
rebelde | rebelde | rebelle | Na adolescência ela era muito rebelde. | Adolescente, elle était très rebelle.
recente | recente | récent | É uma notícia recente. | C'est une nouvelle récente.
reformado | reformada | à la retraite | O meu pai está reformado há um ano. | Mon père est à la retraite depuis un an.
relativo | relativa | relatif, relativement | Tudo é relativo, ele sempre diz. | Tout est relatif, dit-il toujours.
relaxado | relaxada | détendu | Depois das férias ela sente-se relaxada. | Après les vacances, elle se sent détendue.
relevante | relevante | pertinent | Inclua só dados relevantes. | N'inclus que des données pertinentes.
remoto | remota | reculé | Ele mora em um vale remoto. | Il vit dans une vallée reculée.
resfriado | resfriada | enrhumé | Estou resfriado desde ontem. | Je suis enrhumé depuis hier.
responsável | responsável | responsable | Ele é responsável por três equipas. | Il est responsable de trois équipes.
restante | restante | restant, qui reste | Não sobrou nada do bolo. | Il ne reste rien du gâteau. | ex?
rico | rica | riche | O país é rico em água. | Le pays est riche en eau.
rural | rural | rural | A zona rural perde habitantes. | La zone rurale perd des habitants.
sagrado | sagrada | sacré | É um lugar sagrado. | C'est un lieu sacré.
satisfatório | satisfatória | satisfaisant | O resultado é satisfatório, mas não é bom. | Le résultat est satisfaisant, mais pas bon.
sazonal | sazonal | saisonnier | É um trabalho sazonal. | C'est un travail saisonnier.
secreto | secreta | secret | Eles fizeram uma reunião secreta. | Ils ont tenu une réunion secrète.
seguinte | seguinte | suivant | Responda às seguintes perguntas. | Répondez aux questions suivantes.
seguro de si | seguro de si | sûr de soi | Ela mostra-se muito segura de si. | Elle se présente avec beaucoup d'assurance. | ex?
sem esperança | sem esperança | sans espoir | A situação parecia sem saída. | La situation semblait désespérée. | ex?
sem sal | sem sal | fade | A sopa está sem sal. | La soupe est fade.
sem sentido | sem sentido | insensé/sensé | Seria inútil protestar agora. | Il serait insensé de protester maintenant. | ex?
sem sucesso | sem sucesso | sans succès, raté | Tentei abrir a porta sem sucesso. | J'ai essayé d'ouvrir la porte sans succès.
sem tato | sem tato | sans tact | O comentário dele foi bem indelicado. | Sa remarque était plutôt sans tact. | ex?
sem valor | sem valor | sans valeur | Sem assinatura o contrato não vale nada. | Sans signature, le contrat est sans valeur. | ex?
sensato | sensata | sensé | Ele deu um conselho sensato. | Il a donné un conseil sensé.
sensível | sensível | sensible (émotif) | Ele é muito sensível ao barulho. | Il est très sensible au bruit.
severo | severa | sévère | O professor é severo, mas justo. | Le professeur est sévère mais juste.
significativo | significativa | significatif | É uma diferença significativa. | C'est une différence significative.
similar | similar | similaire | Temos gostos parecidos. | Nous avons des goûts similaires. | ex?
social | social | social | É um problema social complexo. | C'est un problème social complexe.
solar | solar | solaire | A energia solar é a mais barata. | L'énergie solaire est la moins chère.
solidário | solidária | solidaire | É um bairro muito solidário. | C'est un quartier très solidaire.
solvente | solvente | solvable | É um cliente com boa situação financeira. | C'est un client solvable. | ex?
superemocionante | superemocionante | super, génial | O filme foi superemocionante. | Le film était super captivant.
superficial | superficial | superficiel | Ele fez uma análise superficial. | Il a fait une analyse superficielle.
superior | superior | supérieur | Ele mora no andar superior. | Il vit à l'étage supérieur.
surdo | surda | sourd | Desde o acidente ele é surdo de um ouvido. | Depuis l'accident, il est sourd d'une oreille.
surpreendente | surpreendente | surprenant | O resultado foi surpreendente. | Le résultat a été surprenant.
surpreso | surpresa | surpris | Fiquei surpreso com a notícia. | J'ai été surpris par la nouvelle.
suspeito | suspeita | suspect | A mala parece suspeita. | La valise a l'air suspecte.
sustentável | sustentável | durable | É um modelo sustentável. | C'est un modèle durable.
sábio | sábia | sage | Foi uma decisão sábia. | Ce fut une décision sage.
só | só | seulement, rien que | Isso custa só dez euros. | Ça ne coûte que dix euros.
sólido | sólida | solide | O argumento é sólido. | L'argument est solide.
talentoso | talentosa | doué | Ele é um pintor talentoso. | C'est un peintre talentueux.
temporário | temporária | temporaire | É um contrato temporário. | C'est un contrat temporaire.
tenso | tensa | tendu | O clima estava tenso. | L'ambiance était tendue.
ter culpa | ter culpa | être responsable, être en faute | Quem tem culpa por este mal-entendido? | Qui est en faute dans ce malentendu ? | ex?
todos | todos | tous, l'ensemble de | Todos os documentos foram verificados. | Tous les documents ont été vérifiés.
tolerante | tolerante | tolérant | É uma cidade tolerante. | C'est une ville tolérante.
total | total | total | Foi um fracasso total. | Ce fut un échec total.
totalmente | totalmente | tout à fait, complètement | Depois do trabalho estou totalmente cansado. | Après le travail, je suis totalement épuisé.
trabalhista | trabalhista | du travail | O mercado de trabalho está a mudar. | Le marché du travail change. | ex?
tradicional | tradicional | traditionnel | É um prato tradicional do sul. | C'est un plat traditionnel du sud.
transparente | transparente | transparent | Use um recipiente transparente. | Utilise un récipient transparent.
tudo bem | tudo bem | d'accord, correct | Tudo bem se eu chegar mais tarde? | C'est d'accord si j'arrive plus tard ?
técnico | técnica | technique | Ele tem bons conhecimentos técnicos. | Il a de bonnes connaissances techniques.
uniforme | uniforme | uniforme, homogène | Todos os formulários têm um formato padronizado. | Tous les formulaires ont un format uniforme. | ex?
urbano | urbana | urbain | O transporte urbano funciona bem. | Le transport urbain fonctionne bien.
valioso | valiosa | précieux | Ele deu-nos um conselho valioso. | Il nous a donné un conseil précieux.
vedado | vedada | dense, étanche | A janela não está mais bem vedada. | La fenêtre n'est plus vraiment étanche.
vegetariano | vegetariana | végétarien | Ele foi vegetariano durante anos. | Il s'est nourri végétarien pendant des années.
veloz | veloz | rapide | É um corredor veloz. | C'est un coureur rapide.
venenoso | venenosa | toxique, vénéneux | Esta planta é venenosa. | Cette plante est vénéneuse.
vertical | vertical | vertical | Guarde as tábuas na vertical. | Range les planches en position verticale.
viciado | viciada | dépendant, accro | Muitos jovens são viciados no telemóvel. | Beaucoup de jeunes sont accros à leur téléphone.
viciante | viciante | addictif |  |  | ex=?
violento | violenta | violent |  |  | ex=?
viral | viral | viral | O vídeo viralizou. | La vidéo est devenue virale. | ex?
virtual | virtual | virtuel | Fizemos uma visita virtual. | Nous avons fait une visite virtuelle.
visível | visível | visible | A rachadura é visível da rua. | La fissure est visible depuis la rue.
vital | vital | vital | É um órgão vital. | C'est un organe vital.
viúvo | viúva | veuf, veuve | Ela é viúva há três anos. | Elle est veuve depuis trois ans.
voluntário | voluntária | bénévole | Ela trabalha como voluntária num asilo. | Elle travaille bénévolement à la maison de retraite.
vulnerável | vulnerável | vulnérable | Eles protegem as famílias vulneráveis. | Ils protègent les familles vulnérables.
válido | válida | valable | A passagem é válida por um mês. | Le billet est valable un mois.
à parte | à parte | en plus, spécialement | O pequeno-almoço é cobrado à parte. | Le petit-déjeuner est en supplément.
árido | árida | aride | É uma zona árida e ventosa. | C'est une zone aride et venteuse.
íngreme | íngreme | raide, escarpé | O caminho até lá em cima é bem íngreme. | Le chemin qui monte est assez raide.
óbvio | óbvia | évident, bien entendu | A explicação mais óbvia costuma ser a certa. | L'explication la plus évidente est le plus souvent la bonne.
único | única | unique | É a única opção que resta. | C'est la seule option qui reste.
"""

# « adverbe | traduction | categorie | phrase | sa traduction ».
ADVERBES = """
a caminho | en route | Lieu | Já estou a caminho da estação. | Je suis déjà en route pour la gare.
a esta altura | entre-temps, désormais | Temps | Hoje em dia ela fala alemão fluentemente. | Désormais, elle parle couramment allemand. | ex?
a fundo | à fond | Manière | O caso foi analisado a fundo. | Le dossier a été examiné de manière approfondie.
a propósito | au fait | Liaison |  |  | ex=?
a qualquer momento | à tout moment | Temps | Pode ligar-me a qualquer momento. | Vous pouvez m'appeler à tout moment.
a sós | seul à seul | Manière |  |  | ex=?
a tempo | à temps | Temps | Chegamos bem a tempo. | Nous sommes arrivés juste à temps.
abertamente | ouvertement | Manière | Ele falou abertamente do problema. | Il a parlé ouvertement du problème.
absolutamente | absolument | Quantité | Ele não sabia absolutamente nada. | Il ne savait absolument rien.
agora há pouco | tout à l'heure (passé) | Temps |  |  | ex=?
ainda não | pas encore | Temps | Ele ainda não respondeu. | Il n'a pas encore répondu.
algum dia | un jour ou l'autre | Temps | Um dia eu vou ao Japão. | Un jour ou l'autre, j'irai au Japon. | ex?
alguma vez | jamais (un jour) | Temps |  |  | ex=?
aliás | au fait, d'ailleurs | Nuance | Aliás, o teu pacote chegou. | Au fait, ton colis est arrivé.
altamente | hautement | Quantité | É um produto altamente inflamável. | C'est un produit hautement inflammable.
amplamente | largement | Manière | O método é amplamente aceito. | La méthode est largement acceptée.
antecipadamente | à l'avance, devant | Temps | Desde já, muito obrigado! | Merci d'avance ! | ex?
anteontem à noite | avant-hier soir | Temps | Anteontem à noite houve tempestade. | Avant-hier soir il y a eu de l'orage.
ao meio-dia | à midi | Temps | Ao meio-dia a loja fecha por uma hora. | À midi, le magasin ferme une heure.
ao todo | au total | Quantité | Ao todo éramos doze pessoas. | Au total, nous étions douze personnes.
atentamente | attentivement | Manière | Ela ouviu atentamente a pergunta. | Elle a écouté attentivement la question.
atravessado | en travers | Lieu | O carro está atravessado na rua. | La voiture est en travers de la rue.
automaticamente | automatiquement | Manière | A porta fecha automaticamente. | La porte se ferme automatiquement.
bom | bof, enfin bon | Nuance | Bom, não foi tão ruim assim. | Bof, ce n'était pas si terrible.
brevemente | brièvement | Manière | Explique brevemente. | Explique-le brièvement.
cabalmente | pleinement | Manière | Ele cumpriu cabalmente a palavra. | Il a pleinement tenu parole.
cada vez | chaque fois | Fréquence | A batata-doce está cada vez mais popular. | La patate douce devient de plus en plus populaire.
caso contrário | faute de quoi | Cause et conséquence | Por favor, pague até sexta; caso contrário, será enviado um aviso de cobrança. | Veuillez payer avant vendredi, faute de quoi un rappel sera envoyé.
cerca de | environ | Quantité | A viagem dura cerca de duas horas. | Le trajet dure environ deux heures.
com atenção | attentivement | Manière | Ela ouviu com atenção. | Elle a écouté attentivement.
com dificuldade | péniblement | Manière | Ele abaixava-se com dificuldade por causa das costas. | Il se baissait difficilement à cause de son dos.
com isso | par ce biais | Cause et conséquence | Com isso economizamos muita energia todos os anos. | Par ce biais, nous économisons beaucoup d'énergie chaque année.
com paciência | patiemment | Manière | O professor explica tudo com paciência. | Le professeur explique tout patiemment.
com quê | avec quoi | Question | Em que posso ajudar o senhor? | En quoi puis-je vous aider ? | ex?
completamente | complètement | Quantité | O livro é completamente diferente. | Le livre est complètement différent.
comumente | communément | Fréquence | É comumente conhecida como gripe. | On l'appelle communément la grippe.
consequentemente | en conséquence | Liaison | Consequentemente, a entrega atrasou. | En conséquence, la livraison a été retardée.
consideravelmente | considérablement | Quantité | Os preços subiram consideravelmente. | Les prix ont considérablement augmenté.
cuidadosamente | soigneusement | Manière | Ele revisou cuidadosamente cada página. | Il a examiné soigneusement chaque page.
de acordo | en conséquence | Cause et conséquence | A lei é clara e a decisão foi tomada de acordo com ela. | La loi est claire, la décision a été prise en conformité.
de facto | en effet | Affirmation | De facto, o prazo já venceu. | En effet, le délai est déjà échu.
de forma autónoma | de façon autonome | Manière | Os alunos trabalham sozinhos no projeto. | Les élèves travaillent de façon autonome sur le projet. | ex?
de forma direcionada | de manière ciblée | Manière | Ela candidata-se especificamente em empresas pequenas. | Elle postule de manière ciblée dans de petites entreprises. | ex?
de jeito nenhum | pas du tout | Affirmation | Não me incomoda nem um pouco. | Ça ne me dérange pas du tout. | ex?
de manhã | le matin | Temps | De manhã eu sempre tomo um café. | Le matin, je bois toujours un café.
de novo | de nouveau | Temps | Tente de novo amanhã. | Réessaie demain.
de propósito | exprès | Manière | Ele não fez de propósito. | Il ne l'a pas fait exprès.
de ré | en marche arrière | Lieu | Ele saiu de ré da garagem. | Il est sorti du garage en marche arrière.
de sobra | largement, en abondance | Quantité | Há tempo de sobra para a inscrição. | Il y a largement le temps pour l'inscription.
de uma vez | d'un coup | Temps | Ele entendeu tudo de uma vez. | Il a tout compris d'un coup.
de verdade | vraiment | Affirmation | Foi muito gentil da tua parte, de verdade. | C'était vraiment gentil de ta part.
desarrumado | en désordre, pêle-mêle | Manière | Na mesa está tudo desarrumado. | Sur le bureau, tout est en désordre.
desde então | depuis lors | Temps | Ela pediu demissão e desde então trabalha como autónoma. | Elle a démissionné et travaille depuis en indépendante.
desta vez | cette fois-ci | Temps | Desta vez vou fazer vista grossa. | Cette fois, je ferme les yeux.
detalhadamente | en détail | Manière | Ele explicou detalhadamente. | Il l'a expliqué en détail.
devidamente | dûment | Manière | O documento está devidamente assinado. | Le document est dûment signé.
dificilmente | difficilement | Manière | Dificilmente chegaremos a tempo. | Nous arriverons difficilement à l'heure.
diretamente | directement | Manière | Vá diretamente ao escritório. | Va directement au bureau.
duramente | durement | Manière | Criticaram duramente a decisão. | Ils ont durement critiqué la décision.
durante anos | pendant des années | Temps | A fábrica poluiu o rio durante anos. | L'usine a pollué la rivière pendant des années.
durante semanas | pendant des semaines | Temps | Ele esperou uma resposta durante semanas. | Il a attendu une réponse pendant des semaines.
efetivamente | effectivement | Affirmation | De facto, o comboio saiu com atraso. | Effectivement, le train est parti en retard. | ex?
em consequência disso | en conséquence de quoi | Cause et conséquence | Houve um acidente, em consequência disso a rua foi fechada. | Il y a eu un accident, en conséquence la rue était fermée.
em grande parte | en grande partie | Quantité | As obras estão em grande parte concluídas. | Les travaux sont en grande partie terminés.
em lugar nenhum | nulle part | Lieu | Não acho a minha identidade em lugar nenhum. | Je ne trouve ma carte d'identité nulle part.
em parte | en partie | Quantité | Os custos são reembolsados em parte. | Les frais sont remboursés en partie.
enormemente | énormément | Quantité | O projeto cresceu enormemente. | Le projet a énormément grandi.
escassamente | à peine | Quantité | Durou mal dez minutos. | Ça a duré à peine dix minutes. | ex?
escondido | en cachette | Manière | As crianças comeram bolachas escondido. | Les enfants ont mangé des biscuits en cachette.
espontaneamente | spontanément | Manière | Decidimos viajar de improviso. | Nous avons décidé spontanément de partir. | ex?
estritamente | strictement | Manière | É estritamente confidencial. | C'est strictement confidentiel.
evidentemente | évidemment | Affirmation | Evidentemente, não era a intenção dele. | Évidemment, ce n'était pas son intention.
excessivamente | excessivement | Quantité | O texto é excessivamente longo. | Le texte est excessivement long.
exclusivamente | exclusivement | Manière | Ele dedica-se exclusivamente à pesquisa. | Il se consacre exclusivement à la recherche.
expressamente | expressément | Manière | O chefe proibiu isso expressamente. | Le patron l'a expressément interdit.
extremamente | extrêmement | Quantité | O inverno foi extremamente seco. | L'hiver a été extrêmement sec.
facilmente | facilement | Manière | Resolve-se facilmente. | Ça se résout facilement.
fora isso | à part ça, sinon | Cause et conséquence | O motor faz barulho, fora isso o carro anda bem. | Le moteur fait du bruit, à part ça la voiture roule bien.
formalmente | formellement | Manière | Ele foi formalmente convidado. | Il a été formellement invité.
fortemente | fortement | Manière | Eu desaconselharia isso fortemente. | Je le déconseillerais vivement.
gravemente | gravement | Manière | Ele ficou gravemente ferido. | Il a été gravement blessé.
igual | pareil | Manière | Fizemos igual ao ano passado. | On l'a fait pareil que l'an dernier.
igualmente | de même | Liaison | O segundo curso foi igualmente interessante. | Le deuxième cours était tout aussi intéressant.
incluído | y compris, inclus | Quantité | O preço inclui o pequeno-almoço. | Le prix est petit-déjeuner inclus. | ex?
indubitavelmente | indubitablement | Affirmation | É indubitavelmente o melhor do grupo. | C'est indubitablement le meilleur du groupe.
injustamente | injustement | Liaison | Ele foi injustamente acusado. | Il a été injustement accusé.
inteiramente | entièrement | Quantité | A culpa é inteiramente minha. | La faute est entièrement mienne.
intensamente | intensément | Manière | Ele trabalhou intensamente o mês inteiro. | Il a travaillé intensément tout le mois.
legalmente | légalement | Liaison | Ele não é legalmente obrigado. | Il n'est pas légalement obligé.
lentamente | lentement | Manière | O comboio avançava lentamente. | Le train avançait lentement.
levemente | légèrement | Quantité | O paciente melhorou levemente. | Le patient s'est légèrement amélioré.
ligeiramente | légèrement | Quantité | Os preços subiram ligeiramente. | Les prix ont légèrement augmenté.
livremente | librement | Manière |  |  | ex=?
localmente | localement | Lieu | O produto é fabricado localmente. | Le produit est fabriqué localement.
longamente | longuement | Temps | Eles discutiram isso longamente. | Ils en ont longuement discuté.
lá dentro | dedans | Lieu | Vamos para dentro, está frio. | Rentrons, il fait froid. | ex?
líquido | net (salaire) | Quantité | Sobram para mim dois mil euros líquidos. | Net, il me reste deux mille euros. | ex?
mais uma vez | encore une fois | Fréquence | Mais uma vez, muito obrigado por tudo! | Encore une fois, merci pour tout !
mais vezes | plus souvent | Fréquence |  |  | ex=?
majoritariamente | principalement | Quantité | Votaram majoritariamente a favor. | Ils ont voté majoritairement pour.
meio período | à mi-temps | Temps | Ela só trabalha meio período. | Elle ne travaille qu'à mi-temps.
menos | moins (température, calcul) | Quantité | Eu correria de manhã, faz menos calor. | Moi, je courrais le matin, il fait moins chaud.
meramente | simplement | Quantité | É meramente uma formalidade. | C'est simplement une formalité.
naturalmente | naturellement | Manière | Naturalmente, todos estavam convidados. | Naturellement, tout le monde était invité.
nem sequer | même pas | Affirmation | Ele nem me cumprimentou. | Il ne m'a même pas salué. | ex?
no começo | au début | Temps | No começo tudo era muito difícil. | Au début, tout était très difficile.
no fim | à la fin | Temps | No fim eles ficaram em casa. | À la fin ils sont restés à la maison.
no futuro | à l'avenir | Temps | Daqui em diante os pedidos serão feitos on-line. | À l'avenir, les demandes se feront en ligne. | ex?
no início | au début | Temps | No início não gostei. | Au début ça ne m'a pas plu.
no meio | au milieu | Lieu | Ele acordou no meio da noite. | Il s'est réveillé au milieu de la nuit.
notavelmente | notablement | Quantité | O trânsito diminuiu notavelmente. | Le trafic a notablement baissé.
obviamente | évidemment | Affirmation | Obviamente é preciso de avisar antes. | Évidemment il faut prévenir avant.
oficialmente | officiellement | Liaison | Ainda não foi anunciado oficialmente. | Ce n'a pas encore été annoncé officiellement.
para dentro | à l'intérieur (mouvement) | Lieu | Vamos para dentro, está frio. | Rentrons, il fait froid.
para fora | dehors (vers moi) | Lieu | Leve o lixo para fora, por favor. | Sors la poubelle, s'il te plaît.
para lá | là-bas (direction) | Lieu | Esqueci o pão. – Deixa para lá. | J'ai oublié le pain. – Ce n'est pas grave.
para quê | pour quoi, à quoi | Question |  |  | ex=?
paralelamente | en passant, à côté | Manière | Paralelamente ele ainda faz faculdade. | À côté de cela, il fait encore des études.
parcialmente | partiellement | Quantité | O túnel está parcialmente aberto. | Le tunnel est partiellement ouvert.
pelo visto | apparemment | Liaison | Pelo visto ela não recebeu o e-mail. | Elle n'a apparemment pas reçu le courriel.
perfeitamente | parfaitement | Manière | Isso é perfeitamente possível. | C'est tout à fait possible.
plenamente | pleinement | Quantité | Concordo plenamente. | Je suis pleinement d'accord.
por dentro | à l'intérieur | Lieu | Por dentro o apartamento parece bem maior. | À l'intérieur, l'appartement paraît bien plus grand.
por exemplo | par exemple | Liaison | Dá para ir de bicicleta, por exemplo. | On peut par exemple y aller à vélo.
por fora | à l'extérieur | Lieu | Por fora a casa é pintada de cinza. | À l'extérieur, la maison est peinte en gris.
por mim | pour moi, si tu veux | Nuance |  |  | ex=?
por outro lado | en revanche | Liaison | No norte está a chover; no sul, por outro lado, faz sol. | Au nord il pleut, en revanche au sud le soleil brille.
por pouco | tout juste | Quantité | Apanhámos o comboio por pouco. | Nous avons attrapé le train de justesse.
por que motivo | pour quelle raison | Question | Por que motivo o compromisso foi adiado? | Pour quelle raison le rendez-vous a-t-il été reporté ?
por sua vez | à son tour, de nouveau | Liaison | Isso, pela sua vez, leva a custos mais altos. | Cela entraîne à son tour des coûts plus élevés. | ex?
por último | en dernier, finalement | Temps | Embarcamos por último. | Nous avons embarqué les derniers.
portanto | par conséquent | Liaison | Chovia; portanto, cancelamos. | Il pleuvait ; par conséquent, nous avons annulé.
porém | toutefois, cela dit | Nuance | O plano era bom, porém faltava dinheiro. | Le plan était bon, cependant l'argent manquait.
possivelmente | peut-être | Doute | Possivelmente mudem a data. | Ils changeront peut-être la date.
pouco a pouco | petit à petit | Manière | Pouco a pouco todos os convidados foram chegando. | Petit à petit, tous les invités sont arrivés.
praticamente | pratiquement | Quantité | Está praticamente terminado. | C'est pratiquement terminé.
profundamente | profondément | Manière | A notícia o afetou profundamente. | La nouvelle l'a profondément affecté.
provavelmente | probablement | Doute | Provavelmente vai chover amanhã. | Il pleuvra probablement demain.
puramente | purement | Manière | Foi uma coincidência puramente casual. | Ce fut une coïncidence purement fortuite.
quarto | quatrièmement | Liaison | E em quarto lugar, é longe demais. | Et quatrièmement, c'est beaucoup trop loin.
radicalmente | radicalement | Manière | O bairro mudou radicalmente. | Le quartier a radicalement changé.
rapidamente | rapidement | Manière | A notícia espalhou-se rapidamente. | La nouvelle s'est répandue rapidement.
razoavelmente | raisonnablement | Manière | O preço é razoavelmente baixo. | Le prix est raisonnablement bas.
recém | récemment | Temps | É pão recém-feito. | C'est du pain fraîchement fait.
rigorosamente | rigoureusement | Manière | Os dados foram verificados rigorosamente. | Les données ont été rigoureusement vérifiées.
se necessário | au besoin | Cause et conséquence | Eu ergueria a voz fosse-se necessário. | Moi, j'élèverais la voix si nécessaire.
segundo | deuxièmement | Liaison | Em segundo lugar, não tenho tempo para isso. | Deuxièmement, je n'ai pas le temps pour cela.
sem contratempos | sans accroc | Manière | A mudança correu sem nenhum contratempo. | Le déménagement s'est déroulé sans accroc. | ex?
sem dúvida | sans doute | Affirmation | É sem dúvida a melhor opção. | C'est sans doute la meilleure option.
sem parar | sans arrêt | Fréquence | O telefone toca sem parar. | Le téléphone sonne sans arrêt.
sem problemas | sans problème | Manière | A transferência funcionou sem problemas. | Le virement a fonctionné sans problème.
sem querer | par mégarde | Manière | Apaguei o arquivo sem querer. | J'ai supprimé le fichier par mégarde.
separado | séparément, l'un de l'autre | Lieu | As duas casas ficam bem longe uma da outra. | Les deux maisons sont très éloignées l'une de l'autre. | ex?
simplesmente | tout simplement | Manière | Simplesmente, não é verdade. | Tout simplement, ce n'est pas vrai.
sobre o quê | de quoi, sur quoi | Question |  |  | ex=?
suficientemente | suffisamment | Quantité | Não está suficientemente claro. | Ce n'est pas suffisamment clair.
sumamente | extrêmement | Quantité | É um caso extremamente delicado. | C'est un cas extrêmement délicat. | ex?
supostamente | prétendument | Doute | Supostamente o pagamento já foi feito. | Le paiement aurait prétendument été fait.
surpreendentemente | de façon surprenante | Manière | A prova foi surpreendentemente fácil. | L'examen était étonnamment facile.
só | seulement, pas avant | Temps | O comboio só chega às oito. | Le train n'arrive qu'à huit heures.
terceiro | troisièmement | Liaison | E em terceiro lugar, o tempo estava ruim. | Et troisièmement, le temps était mauvais.
tranquilamente | tranquillement | Manière | Fale com calma, não há pressa. | Parle tranquillement, rien ne presse. | ex?
unicamente | uniquement | Quantité | Paga-se unicamente em dinheiro. | On paie uniquement en espèces.
urgentemente | d'urgence | Temps | Precisamos urgentemente de uma resposta. | Il nous faut d'urgence une réponse.
vamos | allons-y ; qui se passe | Nuance | Amanhã vamos para Lisboa. | Demain, nous allons à Lisbonne.
verdadeiramente | véritablement | Affirmation | Foi verdadeiramente emocionante. | Ce fut véritablement émouvant.
visivelmente | visiblement | Affirmation | Ele estava visivelmente cansado. | Il était visiblement fatigué.
várias vezes | sans cesse, à répétition | Fréquence | Eu liguei várias vezes. | J'ai appelé à plusieurs reprises.
à toa | pour rien, en vain ; gratuitement | Nuance | Nas férias eu só fiquei à toa. | En vacances, je n'ai fait que paresser.
é que | à savoir, en effet | Liaison | Não posso ir, é que estou doente. | Je ne peux pas venir, je suis en effet malade.
é verdade que | certes | Nuance | É verdade que ele chegou atrasado. | Il est vrai qu'il est arrivé en retard.
"""

# « expression | traduction | categorie | phrase | sa traduction ».
EXPRESSIONS = """
a caminho | en chemin | Au quotidien | Já estou a caminho da tua casa. | Je suis déjà en chemin vers chez toi.
a longo prazo | à long terme | Au quotidien | A longo prazo, sai mais barato. | À long terme, ça revient moins cher.
a não ser que | à moins que | Discuter | Vamos amanhã, a não ser que neve. | Nous partons demain, à moins qu'il neige.
a rigor | à proprement parler | Discuter | A rigor isso não é permitido. | À proprement parler, ce n'est pas autorisé.
abrir uma exceção | faire une exception | Tournures | Hoje vamos abrir uma exceção. | Aujourd'hui, nous faisons une exception.
acompanhar o ritmo de | suivre le rythme de | Tournures | As empresas pequenas mal conseguem acompanhar o ritmo. | Les petites entreprises peinent à suivre le rythme.
agradecer por | remercier pour | Tournures | Eu gostaria de agradecer pela sua paciência. | Je voudrais vous remercier pour votre patience.
ao longo do ano letivo | tout au long de l'année | Au quotidien | Ao longo do ano letivo fazemos três provas. | Tout au long de l'année nous faisons trois examens.
aos poucos | peu à peu | Discuter | Aos poucos estou a entender mais. | Peu à peu, je comprends davantage.
aproveitar uma oportunidade | saisir une occasion | Au quotidien | Ele aproveitou a oportunidade na hora. | Il a saisi l'occasion immédiatement.
arranjar uma desculpa | trouver une excuse | Au quotidien | Ele sempre arranja uma desculpa. | Il trouve toujours une excuse.
assumir a responsabilidade | assumer la responsabilité | Tournures | Ela assumiu a responsabilidade pelo projeto. | Elle a assumé la responsabilité du projet.
avisar que está doente | se déclarer malade | Au quotidien | Hoje vou ter de avisar que estou doente. | Je dois me déclarer malade aujourd'hui.
chegar a um meio-termo | trouver un compromis | Tournures | No fim chegamos a um meio-termo. | Finalement, nous avons trouvé un compromis.
claro que sim | je vous en prie, bien sûr (Espagne) | Politesse | Posso sentar-me aqui? — Claro que sim! | Je peux m'asseoir ici ? — Je vous en prie !
combinar de | convenir de | Tournures | Combinamos de nos ver na terça. | Nous avons convenu de nous voir mardi.
começar a | se mettre à | Tournures | Começou a chover de repente. | Il s'est mis à pleuvoir d'un coup.
concordar em parte | être d'accord en partie | Réagir | Concordo em parte com o relatório. | Je suis d'accord en partie avec le rapport.
considero isso | je considère cela comme | Donner son avis | Considero isso um erro. | Je considère cela comme une erreur.
contar com | compter sur | Tournures | Dá para contar com ele. | On peut compter sur lui.
cumprir a palavra | tenir parole | Tournures | Ele sempre cumpre a palavra. | Il tient toujours parole.
cumprir um prazo | respecter un délai | Au quotidien | Temos de cumprir o prazo de qualquer jeito. | Nous devons absolument respecter le délai.
dar meia-volta | faire demi-tour | Tournures | Demos meia-volta ao chegar ao rio. | Nous avons fait demi-tour en arrivant à la rivière.
de facto | en effet | Discuter | Isso de facto é um problema. | C'est en effet un problème.
de modo geral | dans l'ensemble | Discuter | De modo geral estou satisfeito. | Dans l'ensemble, je suis satisfait.
de primeira | du premier coup | Discuter | Ela resolveu a tarefa de primeira. | Elle a résolu l'exercice du premier coup.
definir prioridades | définir des priorités | Au quotidien | É preciso de definir prioridades claras. | Il faut définir des priorités claires.
demorar a chegar | se faire attendre | Tournures | A resposta demorou muito a chegar. | La réponse s'est fait longtemps attendre.
depender de | dépendre de | Tournures | Isso depende do tempo. | Cela dépend du temps.
desistir de | renoncer à | Tournures | Desistimos do plano. | Nous avons renoncé à ce plan.
dito de outra forma | autrement dit | Discuter | Dito de outra forma: precisamos de economizar. | Autrement dit : nous devons économiser.
do meu ponto de vista | de mon point de vue | Réagir | Do meu ponto de vista, falta informação. | De mon point de vue, il manque des informations.
duvido que | je doute que | Donner son avis | Duvido que ele chegue no horário. | Je doute qu'il arrive à l'heure.
dá notícias | donne de tes nouvelles | Bavarder | Cuida-se e dá notícias! | Porte-toi bien et donne de tes nouvelles !
em comparação com | par rapport à | Discuter | Em comparação com ontem, está frio. | Par rapport à hier, il fait froid.
em outras palavras | autrement dit | Discuter | Em outras palavras: vamos começar do zero. | Autrement dit : nous recommençons depuis le début.
entrar em contacto | prendre contact | Au quotidien | Por favor, entre em contacto com a central. | Veuillez prendre contact avec le siège.
entre outras coisas | entre autres | Discuter | Falamos, entre outras coisas, dos custos. | Nous avons parlé entre autres des coûts.
estar de mau humor | être de mauvais poil | Tournures | Hoje ele está de mau humor, não pergunte nada. | Aujourd'hui il est de mauvais poil, ne lui demande rien.
estar de saco cheio | en avoir assez | Réagir | Estou de saco cheio deste barulho. | J'en ai assez de ce bruit.
estar em jogo | être en jeu | Tournures | Há muita coisa em jogo desta vez. | Il y a beaucoup en jeu cette fois.
estar nas nuvens | être au septième ciel | Réagir | Desde o casamento ela está nas nuvens. | Depuis le mariage, elle est au septième ciel.
estar à disposição | être à disposition | Tournures | Para qualquer dúvida, estou à sua disposição. | Je reste à votre disposition pour toute question.
estou convencido | je suis convaincu | Donner son avis | Estou convencido de que vai dar certo. | Je suis convaincu que ça va marcher.
eu te dou notícias | je te fais signe | Bavarder | Dou-te notícias assim que souber mais. | Je te fais signe dès que j'en sais plus.
fazer hora extra | faire des heures supplémentaires | Au quotidien | Esta semana estou a fazer muita hora extra. | Cette semaine, je fais beaucoup d'heures supplémentaires.
fazer um requerimento | déposer une demande | Tournures | O senhor precisa de fazer um requerimento na repartição. | Vous devez déposer une demande auprès de l'administration.
ficar de pé | se lever | Tournures | Todos ficaram de pé no final. | Tout le monde s'est levé à la fin.
ganhar experiência | acquérir de l'expérience | Tournures | No estágio ganha-se uma experiência valiosa. | En stage, on acquiert une expérience précieuse.
há bons motivos para isso | il y a de bonnes raisons | Donner son avis | Há bons motivos para agir agora. | Il y a de bonnes raisons d'agir maintenant.
isso está fora de dúvida | cela ne fait aucun doute | Donner son avis | A competência dele está fora de dúvida. | Sa compétence ne fait aucun doute.
isso faz sentido para mim | ça me paraît logique | Donner son avis | A tua explicação faz sentido para mim. | Ton explication me paraît logique.
isso é discutível | c'est discutable | Donner son avis | É-se mais bonito, isso é discutível. | Que ce soit plus beau, c'est discutable.
lembrar-se de | se souvenir de | Tournures | Eu lembro-me bem daquele dia. | Je me souviens bien de ce jour.
levar até o fim | mener à terme | Au quotidien | Eu gostaria de levar o projeto até o fim. | Je voudrais mener le projet à terme.
manter-se atualizado | se tenir au courant | Au quotidien | Eu mantenho-me atualizado pelo noticiário. | Je me tiens au courant par les informations.
no que diz respeito a | en ce qui concerne | Discuter | No que diz respeito a dinheiro, sou cuidadoso. | En ce qui concerne l'argent, je suis prudent.
não acho | je ne suis pas d'accord | Réagir | Não acho que seja uma boa ideia. | Je ne trouve pas que ce soit une bonne idée.
não acredito | je n'en reviens pas | Réagir | Ele ganhou? Não acredito! | Il a gagné ? Je n'en reviens pas !
não correr riscos | jouer la sécurité | Au quotidien | Prefiro não arriscar e reservo cedo. | Je préfère jouer la sécurité et réserver tôt.
não estar a fim | ne pas avoir envie | Réagir | Hoje não estou a fim de cozinhar. | Aujourd'hui, je n'ai pas envie de cuisiner.
não estou convencido de que | je ne suis pas convaincu que… (+ subjonctif) | Réagir | Não estou convencido de que seja a melhor solução. | Je ne suis pas convaincu que ce soit la meilleure solution.
não faz sentido | ça n'a pas de sens | Réagir | Este parágrafo não faz sentido. | Ce paragraphe n'a pas de sens.
não fazer diferença | ne pas importer | Discuter | Aqui o preço não faz diferença. | Le prix n'importe pas ici.
não ter pressa | prendre son temps | Au quotidien | Vai com calma, não tem pressa. | Prends ton temps, rien ne presse.
os prós e os contras | le pour et le contre | Discuter | Pesamos os prós e os contras. | Nous avons pesé le pour et le contre.
ou seja | c'est-à-dire | Discuter | Ele reformou-se cedo, ou seja, não trabalha mais. | Il est préretraité, c'est-à-dire qu'il ne travaille plus.
pagar uma conta | régler une facture | Tournures | Ainda preciso de pagar a conta. | Je dois encore régler la facture.
para ser sincero | à vrai dire | Discuter | Para ser sincero, eu esqueci. | À vrai dire, je l'ai oublié.
participar de | participer à | Tournures | Muita gente participou da discussão. | Beaucoup ont participé à la discussion.
pedir desculpas por | s'excuser de | Tournures | Ele pediu desculpas pelo atraso. | Il s'est excusé de son retard.
pelo contrário | au contraire | Discuter | Não foi chato, pelo contrário! | Ce n'était pas ennuyeux, au contraire !
perder a cabeça | perdre la tête | Réagir | Mesmo sob estresse ela nunca perde a cabeça. | Même sous le stress, elle ne perd jamais la tête.
perder a compostura | perdre son sang-froid | Réagir | Apesar das acusações, ele não perdeu a compostura. | Malgré les reproches, il n'a pas perdu son sang-froid.
por conta própria | à ses propres frais | Au quotidien | Ela viajou por conta própria. | Elle a voyagé à ses propres frais.
preencher um requerimento | remplir un formulaire | Au quotidien | Por favor, preencha o requerimento por completo. | Veuillez remplir entièrement le formulaire.
preocupar-se com | se faire du souci pour | Réagir | Não se preocupa com a prova. | Ne te fais pas de souci pour l'examen.
pôr a mão na massa | mettre la main à la pâte | Au quotidien | Todo mundo pôs a mão na massa. | Tout le monde a mis la main à la pâte.
pôr à prova | mettre à l'épreuve | Tournures | A mudança pôs a nossa paciência à prova. | Le déménagement a mis notre patience à l'épreuve.
que bom te ver | content de te voir | Bavarder | Que bom ver-te, senta aí! | Content de te voir, assieds-toi donc !
recorrer a | faire appel à, mobiliser | Tournures | Ela recorreu a uma assessoria jurídica. | Elle a fait appel à un conseil juridique.
Se cuida | Porte-toi bien | Bavarder | Tenho de ir. Cuida-se! | Je dois y aller. Porte-toi bien !
Seja bem-vindo | Bienvenue | Bavarder | Sejam muito bem-vindos ao nosso clube! | Bienvenue dans notre association !
Seja como for | Quoi qu'il en soit | Discuter | Seja como for, temos de continuar. | Quoi qu'il en soit, nous devons continuer.
sem querer | par inadvertance | Au quotidien | Apertei a tecla errada sem querer. | J'ai appuyé par inadvertance sur la mauvaise touche.
sofrer com | souffrir de | Tournures | Muita gente sofre com o barulho. | Beaucoup souffrent du bruit.
sou contra | je suis contre | Donner son avis | Sou contra, é arriscado demais. | Je suis contre, c'est trop risqué.
subir pelas paredes | sortir de ses gonds | Réagir | Quando ouviu isso, ele subiu pelas paredes. | Quand il a entendu ça, il est sorti de ses gonds.
tanto faz | ça m'est égal | Réagir | Cinema ou teatro, tanto faz. | Cinéma ou théâtre, ça m'est égal.
tirar férias | prendre des congés | Au quotidien | Em agosto vou tirar duas semanas de férias. | En août, je prends deux semaines de congés.
tirar o melhor proveito | en tirer le meilleur parti | Réagir | O tempo está ruim, vamos tirar o melhor proveito disso. | Le temps est mauvais, tirons-en le meilleur parti.
tomar conhecimento de | prendre acte de | Tournures | Tomamos conhecimento da sua reclamação. | Nous avons pris acte de votre réclamation.
vale a pena tentar | ça vaut la peine d'essayer | Réagir | Vale a pena tentar mais uma vez. | Ça vaut la peine d'essayer encore une fois.
voltar atrás | se rétracter | Tournures | Ele voltou atrás no último momento. | Il s'est rétracté au dernier moment.
à primeira vista | à première vue | Discuter | À primeira vista o apartamento parece pequeno. | À première vue, l'appartement paraît petit.
"""
