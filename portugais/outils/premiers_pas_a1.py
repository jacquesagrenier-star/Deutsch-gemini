# -*- coding: utf-8 -*-
"""« Premiers pas » en portugais : le parcours des vrais debutants, par
situations de voyage, a Lisbonne (propose le 29 oct. 2026, a confirmer par
Jacques). Meme format que espanol/datos/premiers-pas.json. SOURCE : on corrige
ici, puis python portugais/outils/construire.py.

Une etape : titre, scene (une scene dont scene-<nom>.pt.js existe, ou None),
tableau (titre, lignes « forme | sens », astuce), cartes (« expression | sens |
exemple | sens de l'exemple »), phrases (« phrase | sens | leurre | leurre »,
les leurres etant deux sens proches mais faux).
Les phrases n'emploient que des mots deja vus dans l'etape ou avant.
"""

ETAPES = [
{"s": "L'arrivée : saluer et se présenter", "scene": "flughafen",
 "tableau": {"t": "Être : ser", "a": "Ser dit ce qu'on est : son nom, son pays, son métier. La terminaison suffit, on omet souvent eu : Sou o Pierre. Une femme dit obrigada, un homme obrigado.",
  "l": """eu sou | je suis
tu és | tu es
ele · ela é | il · elle est
o senhor · a senhora é | vous êtes (poli)
nós somos | nous sommes
eles · elas são | ils · elles sont"""},
 "cartes": """olá | bonjour, salut | Olá, sou a Marie. | Bonjour, je suis Marie.
bom dia | bonjour (le matin) | Bom dia, senhor Silva. | Bonjour, monsieur Silva.
boa tarde | bonjour (l'après-midi) | |
boa noite | bonsoir, bonne nuit | |
adeus | au revoir | Adeus, até amanhã! | Au revoir, à demain !
chamo-me… | je m'appelle… | Chamo-me Paul. | Je m'appelle Paul.
Como se chama? | Comment vous appelez-vous ? | |
muito prazer | enchanté | Muito prazer, Ana. | Enchanté, Ana.
Como está? | Comment allez-vous ? | |
estou bem, obrigado | je vais bien, merci | Estou bem, obrigada. E o senhor? | Je vais bien, merci. Et vous ?
sou de… | je suis de… | Sou de França. | Je suis de France.
De onde é? | D'où êtes-vous ? | |
francês · francesa | français, française | Sou francês. | Je suis français.
canadiano · canadiana | canadien, canadienne | Ela é canadiana. | Elle est canadienne.
turista | touriste | Sou turista. | Je suis touriste.
estudante | étudiant, étudiante | |
sim | oui | |
não | non | |
por favor | s'il vous plaît | |
obrigado · obrigada | merci | Muito obrigado! | Merci beaucoup !
desculpe | excusez-moi | Desculpe, é o Rui? | Excusez-moi, vous êtes Rui ?
o passaporte | le passeport | Aqui está o meu passaporte. | Voici mon passeport.
Bem-vindo a Lisboa! | Bienvenue à Lisbonne ! | | """,
 "phrases": """Olá, chamo-me Marie. | Bonjour, je m'appelle Marie. | Au revoir, je m'appelle Marie. | Bonjour, tu t'appelles Marie ?
Sou de França. | Je suis de France. | Je vais en France. | Tu es de France.
Ela é canadiana. | Elle est canadienne. | Il est canadien. | Elle est française.
Muito prazer. | Enchanté. | Merci beaucoup. | Comment ça va ?
Sou turista. | Je suis touriste. | Tu es touriste. | Je suis étudiant.
De onde é? | D'où êtes-vous ? | Où êtes-vous ? | Comment vous appelez-vous ?
Desculpe, é o Rui? | Excusez-moi, vous êtes Rui ? | Pardon, je suis Rui. | Bonjour, voici Rui.
Aqui está o meu passaporte. | Voici mon passeport. | Voici ton passeport. | Où est mon passeport ?"""},

{"s": "À la pastelaria : commander et payer", "scene": "fruehstueck",
 "tableau": {"t": "Demander poliment : queria", "a": "Queria (je voudrais) est la forme polie qu'on entend partout. Quero (je veux) est direct. Au Portugal, on ajoute volontiers se faz favor (s'il vous plaît).",
  "l": """queria… | je voudrais…
pode trazer…? | pouvez-vous apporter… ?
um · uma | un, une
o · a | le, la
se faz favor | s'il vous plaît
Quanto é? | c'est combien ?"""},
 "cartes": """uma bica | un expresso (à Lisbonne) | Uma bica, se faz favor. | Un expresso, s'il vous plaît.
um galão | un grand café au lait | Queria um galão. | Je voudrais un grand café au lait.
um chá | un thé | |
água | de l'eau | Pode trazer água? | Pouvez-vous apporter de l'eau ?
um sumo de laranja | un jus d'orange | Um sumo de laranja, por favor. | Un jus d'orange, s'il vous plaît.
leite | du lait | Um café com leite. | Un café au lait.
açúcar | du sucre | Sem açúcar, obrigado. | Sans sucre, merci.
um pastel de nata | un flan pâtissier | Queria dois pastéis de nata. | Je voudrais deux flans pâtissiers.
uma torrada | une tartine grillée | |
uma tosta mista | un croque-monsieur | |
o pequeno-almoço | le petit-déjeuner | |
a ementa | la carte | Pode trazer a ementa? | Pouvez-vous apporter la carte ?
a conta | l'addition | A conta, se faz favor. | L'addition, s'il vous plaît.
Quanto é? | C'est combien ? | Quanto é, por favor? | C'est combien, s'il vous plaît ?
um euro | un euro | São dois euros. | Ça fait deux euros.
o cartão | la carte (bancaire) | Posso pagar com cartão? | Je peux payer par carte ?
em dinheiro | en espèces | |
para levar | à emporter | Um café para levar. | Un café à emporter.
aqui | ici, sur place | |
uma mesa | une table | Uma mesa para dois, por favor. | Une table pour deux, s'il vous plaît. """,
 "phrases": """Uma bica, se faz favor. | Un expresso, s'il vous plaît. | Une bière, s'il vous plaît. | L'addition, s'il vous plaît.
Queria um galão. | Je voudrais un grand café au lait. | Je voudrais un thé. | Je veux un café noir.
Sem açúcar, obrigado. | Sans sucre, merci. | Avec du sucre, merci. | Sans lait, merci.
Queria dois pastéis de nata. | Je voudrais deux flans pâtissiers. | Je voudrais un flan pâtissier. | Je voudrais deux croissants.
A conta, se faz favor. | L'addition, s'il vous plaît. | La carte, s'il vous plaît. | L'eau, s'il vous plaît.
Posso pagar com cartão? | Je peux payer par carte ? | Je peux payer en espèces ? | Vous payez par carte ?
Um café para levar. | Un café à emporter. | Un café sur place. | Deux cafés à emporter.
Uma mesa para dois, por favor. | Une table pour deux, s'il vous plaît. | Une table pour quatre, s'il vous plaît. | Deux cafés, s'il vous plaît."""},

{"s": "En ville : trouver son chemin", "scene": "stadtplatz",
 "tableau": {"t": "Où est… ? Il y a… : fica, há", "a": "Pour un lieu fixe, le Portugal dit fica : Onde fica o museu? Pour savoir s'il y en a un : Há uma farmácia aqui perto? Há ne change jamais.",
  "l": """Onde fica…? | où se trouve… ?
Onde é…? | où est… ?
Há… aqui perto? | y a-t-il… près d'ici ?
há um · há uma | il y a un, une
à direita · à esquerda | à droite · à gauche
sempre em frente | tout droit"""},
 "cartes": """Onde fica…? | Où se trouve… ? | Onde fica o castelo? | Où se trouve le château ?
a rua | la rue | |
a praça | la place | A praça é muito bonita. | La place est très jolie.
o castelo | le château | |
o museu | le musée | |
a igreja | l'église | |
o rio | le fleuve | O Tejo é um rio. | Le Tage est un fleuve.
o miradouro | le belvédère | Há um miradouro aqui perto? | Il y a un belvédère près d'ici ?
a farmácia | la pharmacie | |
a casa de banho | les toilettes | Onde é a casa de banho? | Où sont les toilettes ?
à direita | à droite | Vire à direita. | Tournez à droite.
à esquerda | à gauche | |
sempre em frente | tout droit | Siga sempre em frente. | Continuez tout droit.
perto | près | É perto? | C'est près ?
longe | loin | Não é longe. | Ce n'est pas loin.
aqui | ici | |
ali | là-bas | O museu é ali. | Le musée est là-bas.
o mapa | le plan | Pode mostrar no mapa? | Pouvez-vous montrer sur le plan ?
a pé | à pied | São cinco minutos a pé. | C'est à cinq minutes à pied.
Estou perdido. | Je suis perdu. | Desculpe, estou perdida. | Excusez-moi, je suis perdue. """,
 "phrases": """Onde fica o castelo? | Où se trouve le château ? | Où est le musée ? | Le château est loin ?
Há uma farmácia aqui perto? | Il y a une pharmacie près d'ici ? | La pharmacie est loin ? | Il y a une banque près d'ici ?
Vire à direita. | Tournez à droite. | Tournez à gauche. | Allez tout droit.
Siga sempre em frente. | Continuez tout droit. | Tournez à droite. | Arrêtez-vous ici.
Não é longe. | Ce n'est pas loin. | C'est très loin. | Ce n'est pas près.
O museu é ali. | Le musée est là-bas. | Le musée est ici. | L'église est là-bas.
São cinco minutos a pé. | C'est à cinq minutes à pied. | C'est à cinq minutes en bus. | C'est à dix minutes à pied.
Desculpe, estou perdida. | Excusez-moi, je suis perdue. | Excusez-moi, je suis en retard. | Merci, je suis arrivée."""},

{"s": "Les transports : le métro, le tram, le comboio", "scene": "kreuzung",
 "tableau": {"t": "Aller, prendre : ir, apanhar", "a": "Au Portugal, on « attrape » le bus : apanhar o autocarro (le Brésil dit pegar o ônibus). Le train se dit o comboio, le tram o elétrico. Ir de : ir de metro, en métro.",
  "l": """vou de metro | je vais en métro
apanho o autocarro | je prends le bus
o elétrico 28 | le tram 28
o comboio para Sintra | le train pour Sintra
um bilhete | un billet, un ticket
a próxima paragem | le prochain arrêt"""},
 "cartes": """o metro | le métro | Vou de metro. | J'y vais en métro.
o autocarro | le bus | Apanho o autocarro. | Je prends le bus.
o elétrico | le tram | O elétrico 28 vai para o castelo. | Le tram 28 va au château.
o comboio | le train | O comboio para Sintra parte às dez. | Le train pour Sintra part à dix heures.
o táxi | le taxi | |
o barco | le bateau | |
a estação | la gare, la station | Onde fica a estação? | Où est la gare ?
a paragem | l'arrêt | A paragem é ali. | L'arrêt est là-bas.
o bilhete | le billet | Um bilhete para Cascais, por favor. | Un billet pour Cascais, s'il vous plaît.
ida e volta | aller-retour | |
o cartão Viva | la carte de transport de Lisbonne | Queria carregar o cartão. | Je voudrais recharger la carte.
apanhar | prendre (un transport) | |
sair | descendre, sortir | Saio na próxima. | Je descends au prochain.
a próxima paragem | le prochain arrêt | |
a linha | la ligne, la voie | A linha azul vai para o centro. | La ligne bleue va au centre.
Este autocarro vai para…? | Ce bus va à… ? | Este autocarro vai para Belém? | Ce bus va à Belém ?
A que horas parte? | À quelle heure part-il ? | |
o atraso | le retard | |
o aeroporto | l'aéroport | |
a mala | la valise | | """,
 "phrases": """Vou de metro. | J'y vais en métro. | J'y vais en bus. | J'y vais à pied.
O comboio para Sintra parte às dez. | Le train pour Sintra part à dix heures. | Le train pour Sintra arrive à dix heures. | Le bus pour Sintra part à dix heures.
Um bilhete para Cascais, por favor. | Un billet pour Cascais, s'il vous plaît. | Deux billets pour Cascais, s'il vous plaît. | Un aller-retour pour Cascais.
Este autocarro vai para Belém? | Ce bus va à Belém ? | Ce train va à Belém ? | Ce bus vient de Belém ?
Saio na próxima. | Je descends au prochain. | Je monte au prochain. | Je descends ici.
A paragem é ali. | L'arrêt est là-bas. | La gare est là-bas. | L'arrêt est ici.
A linha azul vai para o centro. | La ligne bleue va au centre. | La ligne verte va au centre. | La ligne bleue va à l'aéroport.
Queria carregar o cartão. | Je voudrais recharger la carte. | Je voudrais acheter la carte. | Je voudrais payer par carte."""},

{"s": "L'hôtel : la réservation, la chambre", "scene": "hotel",
 "tableau": {"t": "Avoir : ter", "a": "Ter est irrégulier : tenho, tens, tem. Avoir une réservation : ter uma reserva. Au Portugal, le rez-de-chaussée est o rés-do-chão, et le premier étage o primeiro andar.",
  "l": """eu tenho | j'ai
tu tens | tu as
ele · o senhor tem | il a · vous avez
nós temos | nous avons
eles têm | ils ont
Tem…? | avez-vous… ?"""},
 "cartes": """o hotel | l'hôtel | |
a reserva | la réservation | Tenho uma reserva. | J'ai une réservation.
em nome de… | au nom de… | Tenho uma reserva em nome de Tremblay. | J'ai une réservation au nom de Tremblay.
o quarto | la chambre | Queria um quarto para duas noites. | Je voudrais une chambre pour deux nuits.
uma noite | une nuit | |
a chave | la clé | Aqui está a chave. | Voici la clé.
o andar | l'étage | O quarto fica no terceiro andar. | La chambre est au troisième étage.
o elevador | l'ascenseur | Onde é o elevador? | Où est l'ascenseur ?
o pequeno-almoço | le petit-déjeuner | O pequeno-almoço está incluído? | Le petit-déjeuner est compris ?
a casa de banho | la salle de bain | |
o duche | la douche | O duche não funciona. | La douche ne marche pas.
a toalha | la serviette | Pode dar-me outra toalha? | Pouvez-vous me donner une autre serviette ?
a palavra-passe | le mot de passe | Qual é a palavra-passe do wi-fi? | Quel est le mot de passe du wifi ?
a receção | la réception | |
Tem…? | Avez-vous… ? | Tem um quarto livre? | Avez-vous une chambre libre ?
livre | libre | |
incluído | compris | |
a cama | le lit | |
a janela | la fenêtre | |
o barulho | le bruit | Há muito barulho. | Il y a beaucoup de bruit. """,
 "phrases": """Tenho uma reserva em nome de Tremblay. | J'ai une réservation au nom de Tremblay. | J'ai une chambre au nom de Tremblay. | Vous avez une réservation au nom de Tremblay ?
Queria um quarto para duas noites. | Je voudrais une chambre pour deux nuits. | Je voudrais une chambre pour une nuit. | Je voudrais deux chambres pour une nuit.
O pequeno-almoço está incluído? | Le petit-déjeuner est compris ? | Le petit-déjeuner est à quelle heure ? | Le dîner est compris ?
O quarto fica no terceiro andar. | La chambre est au troisième étage. | La chambre est au deuxième étage. | L'ascenseur est au troisième étage.
Tem um quarto livre? | Avez-vous une chambre libre ? | La chambre est libre ? | Avez-vous une table libre ?
Pode dar-me outra toalha? | Pouvez-vous me donner une autre serviette ? | Pouvez-vous me donner la clé ? | Pouvez-vous me donner un autre oreiller ?
O duche não funciona. | La douche ne marche pas. | La télé ne marche pas. | La douche est froide.
Qual é a palavra-passe do wi-fi? | Quel est le mot de passe du wifi ? | Où est le wifi ? | Le wifi ne marche pas ?"""},

{"s": "Les achats : magasins, tailles, prix", "scene": "kleidergeschaeft",
 "tableau": {"t": "Ce, cette : este, esta", "a": "Este, esta pour ce qui est près de moi ; esse, essa pour ce qui est près de toi. Ils s'accordent : este casaco, esta camisa, estes sapatos. Quanto custa? pour une chose, Quanto custam? pour plusieurs.",
  "l": """este casaco | ce manteau-ci
esta camisa | cette chemise-ci
esse · essa | ce, cette (près de toi)
Quanto custa? | combien coûte-t-il ?
Quanto custam? | combien coûtent-ils ?
Posso experimentar? | je peux essayer ?"""},
 "cartes": """a loja | le magasin | A loja abre às dez. | Le magasin ouvre à dix heures.
Quanto custa? | Combien ça coûte ? | Quanto custa esta camisa? | Combien coûte cette chemise ?
caro · barato | cher · bon marché | É muito caro. | C'est très cher.
o tamanho | la taille | Que tamanho veste? | Quelle taille faites-vous ?
o número | la pointure | Calço o número 40. | Je chausse du 40.
Posso experimentar? | Je peux essayer ? | |
o provador | la cabine d'essayage | |
a camisa | la chemise | |
a camisola | le pull | |
as calças | le pantalon | |
o casaco | la veste, le manteau | |
os sapatos | les chaussures | |
grande · pequeno | grand · petit | É pequeno demais. | C'est trop petit.
outra cor | une autre couleur | Tem noutra cor? | Vous l'avez dans une autre couleur ?
levo | je le prends | Levo este. | Je prends celui-ci.
os saldos | les soldes | |
o saco | le sac | Quer um saco? | Voulez-vous un sac ?
o talão | le ticket de caisse | |
Só estou a ver. | Je regarde seulement. | Obrigado, só estou a ver. | Merci, je regarde seulement. """,
 "phrases": """Quanto custa esta camisa? | Combien coûte cette chemise ? | Combien coûtent ces chemises ? | Vous avez cette chemise ?
É muito caro. | C'est très cher. | C'est très bon marché. | C'est trop grand.
Posso experimentar? | Je peux essayer ? | Je peux payer ? | Je peux regarder ?
É pequeno demais. | C'est trop petit. | C'est trop grand. | C'est trop cher.
Tem noutra cor? | Vous l'avez dans une autre couleur ? | Vous l'avez dans une autre taille ? | C'est quelle couleur ?
Levo este. | Je prends celui-ci. | Je regarde celui-ci. | J'essaie celui-ci.
Calço o número 40. | Je chausse du 40. | Je fais du 40. | Je voudrais le 40.
Obrigado, só estou a ver. | Merci, je regarde seulement. | Merci, je le prends. | Merci, c'est tout."""},

{"s": "La santé : pharmacie, médecin", "scene": "apotheke",
 "tableau": {"t": "Avoir mal : dói-me", "a": "« J'ai mal à la tête » se dit Dói-me a cabeça (la tête me fait mal) ; au pluriel, Doem-me os pés. Au Portugal, « je suis enrhumé » : estou constipado (un faux ami !).",
  "l": """dói-me a cabeça | j'ai mal à la tête
dói-me a barriga | j'ai mal au ventre
doem-me as costas | j'ai mal au dos
estou doente | je suis malade
estou constipado | je suis enrhumé
tenho febre | j'ai de la fièvre"""},
 "cartes": """a farmácia | la pharmacie | Onde há uma farmácia? | Où y a-t-il une pharmacie ?
o médico · a médica | le médecin | Preciso de um médico. | J'ai besoin d'un médecin.
o hospital | l'hôpital | |
o centro de saúde | le centre de santé | |
dói-me… | j'ai mal à… | Dói-me a cabeça. | J'ai mal à la tête.
a cabeça | la tête | |
a barriga | le ventre | |
as costas | le dos | |
a garganta | la gorge | Dói-me a garganta. | J'ai mal à la gorge.
a febre | la fièvre | Tenho febre. | J'ai de la fièvre.
constipado | enrhumé | Estou constipada. | Je suis enrhumée.
a tosse | la toux | |
doente | malade | |
o medicamento | le médicament | |
o comprimido | le comprimé | Um comprimido três vezes por dia. | Un comprimé trois fois par jour.
a receita | l'ordonnance | Precisa de receita? | Il faut une ordonnance ?
a alergia | l'allergie | Tenho alergia a… | Je suis allergique à…
Socorro! | Au secours ! | |
o 112 | le 112 (urgences) | Ligue para o 112! | Appelez le 112 ! """,
 "phrases": """Dói-me a cabeça. | J'ai mal à la tête. | J'ai mal au ventre. | Tu as mal à la tête ?
Preciso de um médico. | J'ai besoin d'un médecin. | Je suis médecin. | J'ai besoin d'une pharmacie.
Tenho febre. | J'ai de la fièvre. | J'ai froid. | J'ai de la toux.
Estou constipada. | Je suis enrhumée. | Je suis constipée. | Je suis fatiguée.
Dói-me a garganta. | J'ai mal à la gorge. | J'ai mal au dos. | J'ai mal à la tête.
Precisa de receita? | Il faut une ordonnance ? | Vous avez une ordonnance ? | C'est un médicament ?
Um comprimido três vezes por dia. | Un comprimé trois fois par jour. | Deux comprimés par jour. | Un comprimé le soir.
Ligue para o 112! | Appelez le 112 ! | Appelez un taxi ! | Appelez l'hôtel !"""},

{"s": "Se débrouiller et bavarder : faire répéter, l'heure, la météo", "scene": "strand",
 "tableau": {"t": "Il fait… : está", "a": "Le temps qu'il fait passe par estar : está calor, está frio, está sol. La pluie en cours : está a chover. « Je ne comprends pas » se dit, au Portugal, não percebo.",
  "l": """está calor | il fait chaud
está frio | il fait froid
está sol | il fait soleil
está a chover | il pleut
Que horas são? | quelle heure est-il ?
são três horas | il est trois heures"""},
 "cartes": """Não percebo. | Je ne comprends pas. | Desculpe, não percebo. | Excusez-moi, je ne comprends pas.
Pode repetir? | Pouvez-vous répéter ? | |
mais devagar | plus lentement | Fale mais devagar, por favor. | Parlez plus lentement, s'il vous plaît.
Fala francês? | Vous parlez français ? | |
um pouco | un peu | Falo um pouco de português. | Je parle un peu portugais.
Como se diz…? | Comment dit-on… ? | |
Que horas são? | Quelle heure est-il ? | |
são duas horas | il est deux heures | São duas e meia. | Il est deux heures et demie.
hoje | aujourd'hui | |
amanhã | demain | |
o tempo | le temps (qu'il fait) | Como está o tempo? | Quel temps fait-il ?
está calor | il fait chaud | Hoje está muito calor. | Aujourd'hui, il fait très chaud.
está frio | il fait froid | |
está sol | il fait soleil | |
está a chover | il pleut | |
a praia | la plage | Vamos à praia? | On va à la plage ?
o mar | la mer | |
bonito | beau, joli | Lisboa é muito bonita! | Lisbonne est très jolie !
Gosto muito. | J'aime beaucoup. | Gosto muito de Lisboa. | J'aime beaucoup Lisbonne.
até logo | à plus tard | |
Boa viagem! | Bon voyage ! | | """,
 "phrases": """Desculpe, não percebo. | Excusez-moi, je ne comprends pas. | Excusez-moi, je ne sais pas. | Pardon, je n'entends pas.
Fale mais devagar, por favor. | Parlez plus lentement, s'il vous plaît. | Parlez plus fort, s'il vous plaît. | Répétez, s'il vous plaît.
Falo um pouco de português. | Je parle un peu portugais. | Je parle bien portugais. | Je comprends un peu le portugais.
São duas e meia. | Il est deux heures et demie. | Il est deux heures et quart. | Il est une heure et demie.
Hoje está muito calor. | Aujourd'hui, il fait très chaud. | Aujourd'hui, il fait très froid. | Demain, il fera chaud.
Vamos à praia? | On va à la plage ? | On va à la mer ? | On va au parc ?
Gosto muito de Lisboa. | J'aime beaucoup Lisbonne. | Je connais bien Lisbonne. | J'habite à Lisbonne.
Lisboa é muito bonita! | Lisbonne est très jolie ! | Lisbonne est très grande ! | Lisbonne est très chaude !"""},
]
