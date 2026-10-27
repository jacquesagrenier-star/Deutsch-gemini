# -*- coding: utf-8 -*-
"""« Premiers pas » en anglais : le parcours des vrais debutants, par situations
de voyage, a Boston (decide par Jacques le 27 oct. 2026). Meme format que
espanol/datos/premiers-pas.json. SOURCE : on corrige ici, puis
python anglais/outils/construire.py.

Une etape : titre, scene (une des 37 scenes gardees pour l'anglais, ou None),
tableau (titre, lignes « forme | sens », astuce), cartes (« expression | sens |
exemple | sens de l'exemple »), phrases (« phrase | sens | leurre | leurre »,
les leurres etant deux sens proches mais faux).
Les phrases n'emploient que des mots deja vus dans l'etape ou avant.
"""

ETAPES = [
{"s": "L'arrivée : saluer et se présenter", "scene": "flughafen",
 "tableau": {"t": "Être : to be", "a": "À l'oral, on contracte presque toujours : I'm, you're, he's. « Avoir 20 ans » se dit avec be : I'm twenty.",
  "l": """I am · I'm | je suis
you are · you're | tu es, vous êtes
he is · he's | il est
she is · she's | elle est
we are · we're | nous sommes
they are · they're | ils, elles sont"""},
 "cartes": """hello | bonjour | Hello, I'm Marie. | Bonjour, je suis Marie.
hi | salut | Hi! How are you? | Salut ! Comment ça va ?
good morning | bonjour (le matin) | Good morning, Mr. Smith. | Bonjour, monsieur Smith.
good evening | bonsoir | |
goodbye | au revoir | Goodbye, see you tomorrow! | Au revoir, à demain !
my name is… | je m'appelle… | My name is Paul. | Je m'appelle Paul.
What's your name? | Comment tu t'appelles ? | |
Nice to meet you. | Enchanté. | Nice to meet you, Anna. | Enchanté, Anna.
How are you? | Comment allez-vous ? | |
I'm fine, thanks. | Je vais bien, merci. | I'm fine, thanks. And you? | Je vais bien, merci. Et toi ?
I'm from… | je viens de… | I'm from France. | Je viens de France.
Where are you from? | D'où venez-vous ? | |
French | français, française | I'm French. | Je suis français.
Canadian | canadien, canadienne | She's Canadian. | Elle est canadienne.
a tourist | un, une touriste | I'm a tourist. | Je suis touriste.
a student | un étudiant | |
yes | oui | |
no | non | |
please | s'il vous plaît | |
thank you | merci | Thank you very much! | Merci beaucoup !
excuse me | excusez-moi | Excuse me, are you Tom? | Excusez-moi, vous êtes Tom ?
sorry | pardon, désolé | |
my passport | mon passeport | Here is my passport. | Voici mon passeport.
Welcome to Boston! | Bienvenue à Boston ! | | """,
 "phrases": """Hello, my name is Marie. | Bonjour, je m'appelle Marie. | Au revoir, je m'appelle Marie. | Bonjour, tu t'appelles Marie ?
I'm from France. | Je viens de France. | Je vais en France. | Tu viens de France.
She's Canadian. | Elle est canadienne. | Il est canadien. | Elle est française.
Nice to meet you. | Enchanté. | Merci beaucoup. | Comment ça va ?
I'm a tourist. | Je suis touriste. | Tu es touriste. | Je suis étudiant.
Where are you from? | D'où viens-tu ? | Où es-tu ? | Comment t'appelles-tu ?
Excuse me, are you Tom? | Excusez-moi, vous êtes Tom ? | Pardon, je suis Tom. | Bonjour, voici Tom.
Here is my passport. | Voici mon passeport. | Voici ton passeport. | Où est mon passeport ?"""},

{"s": "Au café : commander et payer", "scene": "fruehstueck",
 "tableau": {"t": "Demander poliment : I'd like, can I have", "a": "I'd like… (je voudrais) et Can I have…? (est-ce que je peux avoir) sont polis. I want… est plus direct : on l'évite avec un serveur.",
  "l": """I'd like… | je voudrais…
Can I have…? | est-ce que je peux avoir… ?
a · an | un, une (an devant une voyelle)
some | un peu de, du
the | le, la, les
How much is it? | combien ça coûte ?"""},
 "cartes": """a coffee | un café | A coffee, please. | Un café, s'il vous plaît.
a tea | un thé | I'd like a tea. | Je voudrais un thé.
water | de l'eau | Can I have some water? | Est-ce que je peux avoir de l'eau ?
an orange juice | un jus d'orange | An orange juice, please. | Un jus d'orange, s'il vous plaît.
milk | du lait | Coffee with milk, please. | Un café au lait, s'il vous plaît.
sugar | du sucre | No sugar, thanks. | Pas de sucre, merci.
a muffin | un muffin | I'd like a blueberry muffin. | Je voudrais un muffin aux myrtilles.
a sandwich | un sandwich | |
a bagel | un bagel | |
breakfast | le petit-déjeuner | |
the menu | la carte | Can I have the menu? | Est-ce que je peux avoir la carte ?
the check | l'addition | The check, please. | L'addition, s'il vous plaît.
to go | à emporter | A coffee to go, please. | Un café à emporter, s'il vous plaît.
for here | sur place | For here or to go? | Sur place ou à emporter ?
small | petit | |
large | grand | A large coffee, please. | Un grand café, s'il vous plaît.
hot | chaud | |
cold | froid | |
a dollar | un dollar | It's three dollars. | Ça fait trois dollars.
a tip | un pourboire | |
by card | par carte | Can I pay by card? | Est-ce que je peux payer par carte ?
cash | en espèces | |
delicious | délicieux | It's delicious! | C'est délicieux !
Here you go. | Voilà, tenez. | | """,
 "phrases": """I'd like a coffee, please. | Je voudrais un café, s'il vous plaît. | Je voudrais un thé, s'il vous plaît. | Tu veux un café ?
Can I have some water? | Est-ce que je peux avoir de l'eau ? | Est-ce que je peux avoir du lait ? | Vous avez de l'eau ?
A large coffee to go, please. | Un grand café à emporter, s'il vous plaît. | Un petit café sur place, s'il vous plaît. | Un grand thé à emporter, s'il vous plaît.
The check, please. | L'addition, s'il vous plaît. | La carte, s'il vous plaît. | Merci beaucoup.
How much is it? | Combien ça coûte ? | C'est délicieux ? | Où est-ce ?
Can I pay by card? | Est-ce que je peux payer par carte ? | Est-ce que je peux payer en espèces ? | Vous voulez la carte ?
It's delicious! | C'est délicieux ! | C'est chaud ! | C'est trois dollars !
I'm from France. | Je viens de France. | Je suis en France. | Elle vient de France.
Nice to meet you. | Enchanté. | Merci beaucoup. | Au revoir."""},

{"s": "En ville : trouver son chemin", "scene": "park",
 "tableau": {"t": "Où est… ? Il y a…", "a": "Where is…? pour un lieu précis ; Is there… near here? pour savoir s'il y en a un. Pour répondre : It's on the left, on the right, straight ahead.",
  "l": """Where is…? | où est… ?
Is there… near here? | est-ce qu'il y a… près d'ici ?
There is… | il y a…
on the left | à gauche
on the right | à droite
straight ahead | tout droit"""},
 "cartes": """the street | la rue | It's on Main Street. | C'est sur Main Street.
the station | la station, la gare | Where is the station? | Où est la station ?
the park | le parc | The park is on the right. | Le parc est à droite.
the museum | le musée | Is there a museum near here? | Est-ce qu'il y a un musée près d'ici ?
the bank | la banque | |
a restaurant | un restaurant | |
the bathroom | les toilettes | Excuse me, where is the bathroom? | Excusez-moi, où sont les toilettes ?
a map | un plan | Do you have a map? | Vous avez un plan ?
near | près | Is it near? | C'est près ?
far | loin | It's not far. | Ce n'est pas loin.
here | ici | |
there | là-bas | It's over there. | C'est là-bas.
next to | à côté de | The bank is next to the café. | La banque est à côté du café.
in front of | devant | |
the corner | le coin | It's on the corner. | C'est au coin.
turn left | tournez à gauche | Turn left at the bank. | Tournez à gauche à la banque.
turn right | tournez à droite | |
go straight | allez tout droit | Go straight for two minutes. | Allez tout droit pendant deux minutes.
I'm lost. | Je suis perdu. | Excuse me, I'm lost. | Excusez-moi, je suis perdu.
on foot | à pied | Ten minutes on foot. | Dix minutes à pied.""",
 "phrases": """Where is the museum? | Où est le musée ? | Où est la banque ? | Le musée est loin ?
Is there a bank near here? | Est-ce qu'il y a une banque près d'ici ? | Est-ce qu'il y a un parc près d'ici ? | La banque est-elle loin ?
It's on the left. | C'est à gauche. | C'est à droite. | C'est tout droit.
Turn right at the corner. | Tournez à droite au coin. | Tournez à gauche au coin. | Allez tout droit au coin.
The park is not far. | Le parc n'est pas loin. | Le parc est loin. | La gare n'est pas loin.
Excuse me, I'm lost. | Excusez-moi, je suis perdu. | Pardon, je suis touriste. | Excusez-moi, où est-ce ?
Ten minutes on foot. | Dix minutes à pied. | Deux minutes à pied. | Dix minutes en bus.
A coffee to go, please. | Un café à emporter, s'il vous plaît. | Un café sur place, s'il vous plaît. | Un thé à emporter, s'il vous plaît.
I'm from Canada. | Je viens du Canada. | Je suis au Canada. | Il vient du Canada."""},

{"s": "Les transports : bus, métro, billets", "scene": None,
 "tableau": {"t": "Aller et prendre : go, take", "a": "On prend un transport avec take : take the bus, take the subway. « En bus » : by bus. Le métro de Boston s'appelle « the T ».",
  "l": """I go to… | je vais à…
I take the bus | je prends le bus
by bus · by train | en bus, en train
a ticket to… | un billet pour…
When does it leave? | quand part-il ?
the next train | le prochain train"""},
 "cartes": """the bus | le bus | I take the bus. | Je prends le bus.
the subway | le métro | The subway is fast. | Le métro est rapide.
the train | le train | |
a taxi | un taxi | |
the airport | l'aéroport | I go to the airport. | Je vais à l'aéroport.
a ticket | un billet | One ticket, please. | Un billet, s'il vous plaît.
a round trip | un aller-retour | |
one way | un aller simple | |
the bus stop | l'arrêt de bus | Where is the bus stop? | Où est l'arrêt de bus ?
the platform | le quai | |
the next stop | le prochain arrêt | The next stop is Park Street. | Le prochain arrêt est Park Street.
to leave | partir | The train leaves at ten. | Le train part à dix heures.
to arrive | arriver | |
late | en retard | The bus is late. | Le bus est en retard.
on time | à l'heure | |
today | aujourd'hui | |
tomorrow | demain | |
the morning | le matin | in the morning | le matin
at five | à cinq heures | |
a bike | un vélo | | """,
 "phrases": """I take the subway. | Je prends le métro. | Je prends le bus. | Je vais au métro.
A ticket to the airport, please. | Un billet pour l'aéroport, s'il vous plaît. | Un taxi pour l'aéroport, s'il vous plaît. | Un billet pour la gare, s'il vous plaît.
When does the next train leave? | Quand part le prochain train ? | Quand arrive le prochain train ? | Où est le prochain train ?
The bus is late. | Le bus est en retard. | Le bus est à l'heure. | Le train est en retard.
Where is the bus stop? | Où est l'arrêt de bus ? | Où est la gare ? | L'arrêt de bus est loin ?
The train leaves at five. | Le train part à cinq heures. | Le train arrive à cinq heures. | Le bus part à cinq heures.
I go to the airport tomorrow. | Je vais à l'aéroport demain. | Je vais à l'aéroport aujourd'hui. | Tu vas à l'aéroport demain.
It's on the right. | C'est à droite. | C'est à gauche. | C'est tout droit.
Can I pay by card? | Est-ce que je peux payer par carte ? | Est-ce que je peux payer en espèces ? | Je peux avoir la carte ?"""},

{"s": "L'hôtel : la réservation, la chambre", "scene": "hotel",
 "tableau": {"t": "Avoir : to have", "a": "He, she, it : has. Pour la question et la négation : Do you have…? I don't have… « J'ai une réservation » : I have a reservation.",
  "l": """I have | j'ai
you have | tu as, vous avez
he · she has | il · elle a
we have | nous avons
they have | ils ont
Do you have…? | avez-vous… ?"""},
 "cartes": """a room | une chambre | I'd like a room. | Je voudrais une chambre.
a reservation | une réservation | I have a reservation. | J'ai une réservation.
a night | une nuit | For two nights. | Pour deux nuits.
the key | la clé | Here is your key. | Voici votre clé.
the floor | l'étage | Your room is on the third floor. | Votre chambre est au troisième étage.
the elevator | l'ascenseur | The elevator is on the left. | L'ascenseur est à gauche.
the bed | le lit | |
the shower | la douche | |
a towel | une serviette | Can I have a towel? | Est-ce que je peux avoir une serviette ?
the Wi-Fi | le wifi | Do you have Wi-Fi? | Vous avez le wifi ?
the password | le mot de passe | |
breakfast | le petit-déjeuner | Is breakfast included? | Le petit-déjeuner est compris ?
included | compris | |
a single room | une chambre simple | |
a double room | une chambre double | |
it doesn't work | ça ne marche pas | The shower doesn't work. | La douche ne marche pas.
noisy | bruyant | The room is noisy. | La chambre est bruyante.
clean | propre | |
quiet | calme | |
to check out | quitter la chambre | | """,
 "phrases": """I have a reservation. | J'ai une réservation. | Vous avez une réservation ? | J'ai une chambre.
Do you have Wi-Fi? | Vous avez le wifi ? | Où est le wifi ? | J'ai le wifi.
Is breakfast included? | Le petit-déjeuner est compris ? | Le petit-déjeuner est délicieux ? | Où est le petit-déjeuner ?
The shower doesn't work. | La douche ne marche pas. | La douche est propre. | La clé ne marche pas.
I'd like a quiet room. | Je voudrais une chambre calme. | Je voudrais une chambre double. | La chambre est bruyante.
Your room is on the third floor. | Votre chambre est au troisième étage. | Votre chambre est à gauche. | La chambre est au deuxième étage.
For two nights, please. | Pour deux nuits, s'il vous plaît. | Pour trois nuits, s'il vous plaît. | Une chambre, s'il vous plaît.
The bus is late. | Le bus est en retard. | Le train est en retard. | Le bus est à l'heure.
Where is the station? | Où est la station ? | Où est le parc ? | La station est loin ?"""},

{"s": "Les achats : magasins, tailles, prix", "scene": "kleidergeschaeft",
 "tableau": {"t": "Les nombres et les prix", "a": "On dit le prix en dollars et en cents : $4.50 = four fifty. Le point sépare les cents, pas la virgule.",
  "l": """one, two, three | un, deux, trois
ten, twenty | dix, vingt
fifty, a hundred | cinquante, cent
How much is it? | combien ça coûte ?
It's ten dollars. | ça fait dix dollars
four fifty | 4,50 $"""},
 "cartes": """the store | le magasin | The store opens at nine. | Le magasin ouvre à neuf heures.
the supermarket | le supermarché | |
a shirt | une chemise | I'd like this shirt. | Je voudrais cette chemise.
a T-shirt | un t-shirt | |
pants | un pantalon | |
shoes | des chaussures | |
the size | la taille | What size? | Quelle taille ?
small · medium · large | petit, moyen, grand | Do you have a medium? | Vous avez un M ?
too big | trop grand | It's too big. | C'est trop grand.
too small | trop petit | |
cheap | pas cher | It's cheap. | Ce n'est pas cher.
expensive | cher | It's too expensive. | C'est trop cher.
this one | celui-ci, celle-ci | I'll take this one. | Je prends celui-ci.
Can I try it on? | Je peux l'essayer ? | |
the fitting room | la cabine d'essayage | |
a bag | un sac | Do you need a bag? | Vous avez besoin d'un sac ?
the receipt | le ticket de caisse | |
on sale | en solde | These shoes are on sale. | Ces chaussures sont en solde.
Just looking. | Je regarde seulement. | I'm just looking, thanks. | Je regarde seulement, merci.
red · blue · black | rouge, bleu, noir | | """,
 "phrases": """How much is this shirt? | Combien coûte cette chemise ? | Où est cette chemise ? | Combien coûte ce t-shirt ?
It's twenty dollars. | Ça fait vingt dollars. | Ça fait dix dollars. | Ça fait cinquante dollars.
It's too expensive. | C'est trop cher. | C'est trop grand. | Ce n'est pas cher.
Can I try it on? | Je peux l'essayer ? | Je peux payer par carte ? | Je peux avoir un sac ?
Do you have a medium? | Vous avez un M ? | Vous avez un L ? | Vous avez la taille ?
I'll take this one. | Je prends celui-ci. | Je voudrais celui-ci. | J'ai celui-ci.
I'm just looking, thanks. | Je regarde seulement, merci. | Je suis perdu, merci. | Je prends celui-ci, merci.
I have a reservation. | J'ai une réservation. | Vous avez une réservation ? | J'ai une chambre.
I take the bus. | Je prends le bus. | Je prends le métro. | Je vais au bus."""},

{"s": "La santé : pharmacie, médecin", "scene": "apotheke",
 "tableau": {"t": "Pouvoir : can, can't", "a": "Can ne change jamais (she can) et le verbe suit sans to : I can't sleep. « J'ai mal à la tête » : I have a headache, ou My head hurts.",
  "l": """I can | je peux, je sais
I can't | je ne peux pas
Can you help me? | pouvez-vous m'aider ?
I have a headache | j'ai mal à la tête
My… hurts | j'ai mal au…
I need… | j'ai besoin de…"""},
 "cartes": """the pharmacy | la pharmacie | Is there a pharmacy near here? | Est-ce qu'il y a une pharmacie près d'ici ?
a doctor | un médecin | I need a doctor. | J'ai besoin d'un médecin.
the hospital | l'hôpital | |
sick | malade | I'm sick. | Je suis malade.
a cold | un rhume | I have a cold. | J'ai un rhume.
a fever | de la fièvre | |
a headache | un mal de tête | |
a stomachache | un mal de ventre | |
my back | mon dos | My back hurts. | J'ai mal au dos.
my throat | ma gorge | |
medicine | un médicament | Do you have medicine for a cold? | Vous avez un médicament contre le rhume ?
a pill | un comprimé | One pill, twice a day. | Un comprimé, deux fois par jour.
a prescription | une ordonnance | |
an appointment | un rendez-vous | I'd like an appointment. | Je voudrais un rendez-vous.
Help! | Au secours ! | |
Call 911! | Appelez le 911 ! | |
an ambulance | une ambulance | |
tired | fatigué | |
better | mieux | I feel better. | Je me sens mieux.
allergic to | allergique à | I'm allergic to nuts. | Je suis allergique aux noix.""",
 "phrases": """I need a doctor. | J'ai besoin d'un médecin. | J'ai besoin d'une pharmacie. | Je suis médecin.
I have a headache. | J'ai mal à la tête. | J'ai mal au dos. | J'ai un rhume.
My back hurts. | J'ai mal au dos. | J'ai mal à la tête. | Mon dos va mieux.
Can you help me? | Pouvez-vous m'aider ? | Je peux vous aider ? | Pouvez-vous appeler ?
I can't sleep. | Je ne peux pas dormir. | Je peux dormir. | Je ne peux pas manger.
I'm allergic to nuts. | Je suis allergique aux noix. | J'ai besoin de noix. | Je suis malade.
I feel better today. | Je me sens mieux aujourd'hui. | Je suis fatigué aujourd'hui. | Je me sens mieux demain.
It's too expensive. | C'est trop cher. | Ce n'est pas cher. | C'est trop petit.
Is breakfast included? | Le petit-déjeuner est compris ? | La chambre est comprise ? | Où est le petit-déjeuner ?"""},

{"s": "Se débrouiller et bavarder : faire répéter, l'heure, la météo", "scene": "winter",
 "tableau": {"t": "Les questions : what, where, when, how", "a": "Le mot interrogatif d'abord, puis do / does pour la plupart des verbes : What do you do? Avec be, on inverse : Where is it? What time is it?",
  "l": """What? | quoi ? que ?
Where? | où ?
When? | quand ?
How? | comment ?
What time is it? | quelle heure est-il ?
How's the weather? | quel temps fait-il ?"""},
 "cartes": """I don't understand. | Je ne comprends pas. | Sorry, I don't understand. | Désolé, je ne comprends pas.
Can you repeat that? | Pouvez-vous répéter ? | |
slowly | lentement | Can you speak slowly, please? | Pouvez-vous parler lentement, s'il vous plaît ?
What does … mean? | Que veut dire… ? | What does "subway" mean? | Que veut dire « subway » ?
I speak a little English. | Je parle un peu anglais. | |
It's three o'clock. | Il est trois heures. | |
half past | et demie | It's half past six. | Il est six heures et demie.
the weather | le temps | |
It's sunny. | Il fait beau. | |
It's raining. | Il pleut. | Take an umbrella, it's raining. | Prends un parapluie, il pleut.
It's snowing. | Il neige. | |
It's cold. | Il fait froid. | It's very cold in Boston in January. | Il fait très froid à Boston en janvier.
It's hot. | Il fait chaud. | |
today | aujourd'hui | |
the weekend | le week-end | What do you do on the weekend? | Que fais-tu le week-end ?
I like… | j'aime… | I like Boston. | J'aime Boston.
Me too. | Moi aussi. | |
Really? | Vraiment ? | |
Of course. | Bien sûr. | |
See you later! | À plus tard ! | | """,
 "phrases": """Sorry, I don't understand. | Désolé, je ne comprends pas. | Désolé, je ne sais pas. | Désolé, je suis en retard.
Can you speak slowly, please? | Pouvez-vous parler lentement, s'il vous plaît ? | Pouvez-vous répéter, s'il vous plaît ? | Pouvez-vous m'aider, s'il vous plaît ?
What time is it? | Quelle heure est-il ? | Quel temps fait-il ? | Quand est-ce ?
It's half past six. | Il est six heures et demie. | Il est six heures. | Il est sept heures et demie.
It's very cold today. | Il fait très froid aujourd'hui. | Il fait très chaud aujourd'hui. | Il fait froid demain.
It's raining. | Il pleut. | Il neige. | Il fait beau.
I like Boston. | J'aime Boston. | Tu aimes Boston ? | Je vais à Boston.
I need a doctor. | J'ai besoin d'un médecin. | J'ai besoin d'une pharmacie. | Je suis médecin.
How much is it? | Combien ça coûte ? | C'est trop cher. | Où est-ce ?"""},
]
