# -*- coding: utf-8 -*-
"""L'A1 voyage de l'anglais, a Boston : 12 escales, 2 etapes « installe », la
suite en 8 etapes. Meme format que espanol/datos/a1-voyage.json (le moteur :
chargerA1Voyage, preparerA1Voyage). SOURCE : on corrige ici, puis
python anglais/outils/construire.py.

- « mots » NOMME des mots du corpus A1 anglais (nom, infinitif, expression) :
  construire.py ecarte et signale ceux qui n'y sont pas.
- « blocs » : « phrase avec … | sens avec … | 3 mots anglais | leurs 3 sens » ;
  l'exemple prend le 3e mot.
- « dialogue » : « eux|moi | replique | sens ».
- Scenes : seulement les 37 gardees pour l'anglais (pas de kreuzung, ubahn, zug,
  stadtplatz, weihnachtsmarkt, post).
"""

ESCALES = [
{"id": "arriver", "pour": "tous", "icone": "🛬", "s": "Arriver à Boston et s'installer à l'hôtel",
 "scenes": ["flughafen", "hotel"],
 "mots": "airport, plane, flight, suitcase, luggage, passport, ticket, passenger, hotel, room, key, elevator, reservation, name, last name, country, nationality, taxi, bed, towel, shower, pillow, night, arrive, book, stay, Welcome!, Hello!, Good evening!",
 "tableau": {"t": "Arriver : to arrive",
  "l": "I arrive in Boston | j'arrive à Boston\nyou arrive late | tu arrives en retard\nhe · she arrives today | il · elle arrive aujourd'hui\nwe arrive at the airport | nous arrivons à l'aéroport\nthey arrive by plane | ils arrivent en avion\nmy flight arrives at six | mon vol arrive à six heures",
  "a": "Arrive in pour une ville ou un pays (arrive in Boston), arrive at pour un lieu précis (arrive at the hotel). Le -s de la 3ᵉ personne : she arrives."},
 "blocs": """I have a reservation under the name … . | J'ai une réservation au nom de … . | Smith / Garcia / Tremblay | Smith / Garcia / Tremblay
I'd like a room for … . | Je voudrais une chambre pour … . | one night / two nights / a week | une nuit / deux nuits / une semaine
Where is the … , please? | Où est … , s'il vous plaît ? | elevator / taxi stand / exit | l'ascenseur / la station de taxis / la sortie
Can I have … , please? | Est-ce que je peux avoir … , s'il vous plaît ? | a towel / another pillow / the Wi-Fi password | une serviette / un autre oreiller / le mot de passe du wifi
I'm here for … . | Je suis ici pour … . | work / a vacation / a week | le travail / des vacances / une semaine""",
 "dialogue": {"t": "À la réception de l'hôtel", "l": """eux | Good evening, welcome! Do you have a reservation? | Bonsoir, bienvenue ! Vous avez une réservation ?
moi | Yes, I have a reservation under the name Tremblay. | Oui, j'ai une réservation au nom de Tremblay.
eux | Perfect. Can I see your passport, please? | Parfait. Je peux voir votre passeport, s'il vous plaît ?
moi | Here you go. What time is breakfast? | Voilà. À quelle heure est le petit-déjeuner ?
eux | From seven to ten. Here is your key, room 412. | De sept à dix heures. Voici votre clé, chambre 412.
moi | Thank you very much! | Merci beaucoup !"""}},

{"id": "manger", "pour": "tous", "icone": "🍽️", "s": "Manger : le café, le restaurant",
 "scenes": ["fruehstueck", "restaurant"],
 "mots": "breakfast, lunch, dinner, coffee, tea, water, juice, milk, bread, egg, sandwich, soup, salad, pizza, cake, dessert, menu, check, tip, waiter, waitress, table, glass, cup, plate, order, eat, drink, The check, please., I'd like…, Enjoy your meal!",
 "tableau": {"t": "Vouloir poliment : I'd like",
  "l": "I'd like a coffee | je voudrais un café\nwould you like some water? | voulez-vous de l'eau ?\nhe'd like the soup | il voudrait la soupe\nwe'd like a table for two | nous voudrions une table pour deux\nthey'd like the check | ils voudraient l'addition\nI don't want dessert | je ne veux pas de dessert",
  "a": "I'd like est la forme polie (I would like). I want est direct : on le garde pour les amis. Pour commander : I'll have the soup (je vais prendre la soupe)."},
 "blocs": """I'd like … , please. | Je voudrais … , s'il vous plaît. | a coffee / an orange juice / a glass of water | un café / un jus d'orange / un verre d'eau
A table for … , please. | Une table pour … , s'il vous plaît. | two / four / one | deux / quatre / une personne
I'll have the … . | Je vais prendre … . | soup / salad / chicken | la soupe / la salade / le poulet
Can I have … ? | Je peux avoir … ? | the menu / the check / some bread | la carte / l'addition / du pain
Is the … included? | Le … est compris ? | tip / service / dessert | pourboire / service / dessert""",
 "dialogue": {"t": "Au restaurant", "l": """eux | Hi! Are you ready to order? | Bonjour ! Vous êtes prêts à commander ?
moi | Yes. I'll have the soup and a salad, please. | Oui. Je vais prendre la soupe et une salade, s'il vous plaît.
eux | Great. Anything to drink? | Très bien. Quelque chose à boire ?
moi | A glass of water, please. | Un verre d'eau, s'il vous plaît.
eux | Here you go. Enjoy your meal! | Voilà. Bon appétit !
moi | Thanks! Can I have the check, please? | Merci ! Je peux avoir l'addition, s'il vous plaît ?"""}},

{"id": "marche", "pour": "tous", "icone": "🍎", "s": "Le marché et la boulangerie",
 "scenes": ["markt-obst-heimisch", "baeckerei"],
 "mots": "market, fruit, apple, banana, orange, lemon, strawberry, grape, pear, vegetable, potato, tomato, carrot, onion, bread, cake, cookie, bakery, bag, price, dollar, cash, cheap, expensive, fresh, buy, pay, How much is it?",
 "tableau": {"t": "Acheter : to buy, to pay",
  "l": "I buy apples | j'achète des pommes\nyou pay in cash | tu paies en espèces\nshe buys bread every day | elle achète du pain tous les jours\nwe pay by card | nous payons par carte\nhow much is it? | combien ça coûte ?\nhow much are they? | combien coûtent-ils ?",
  "a": "How much is it? pour une chose, How much are they? pour plusieurs. Le prix : $3.50 se dit three fifty."},
 "blocs": """I'd like … , please. | Je voudrais … , s'il vous plaît. | a pound of apples / six eggs / a loaf of bread | une livre de pommes / six œufs / une miche de pain
How much are the … ? | Combien coûtent les … ? | strawberries / tomatoes / bananas | fraises / tomates / bananes
Are they … ? | Elles sont … ? | fresh / ripe / local | fraîches / mûres / d'ici
Can I pay … ? | Je peux payer … ? | by card / in cash / with my phone | par carte / en espèces / avec mon téléphone
That's all, … . | C'est tout, … . | thanks / thank you / thanks a lot | merci / merci / merci beaucoup""",
 "dialogue": {"t": "Au marché", "l": """eux | Good morning! What can I get you? | Bonjour ! Qu'est-ce que je vous sers ?
moi | Hi! How much are the strawberries? | Bonjour ! Combien coûtent les fraises ?
eux | Four dollars a box. They're very fresh. | Quatre dollars la barquette. Elles sont très fraîches.
moi | Great, I'll take two boxes. | Super, j'en prends deux barquettes.
eux | That's eight dollars. Anything else? | Ça fait huit dollars. Autre chose ?
moi | No, that's all, thanks. | Non, c'est tout, merci."""}},

{"id": "ville", "pour": "tous", "icone": "🗺️", "s": "En ville : trouver son chemin",
 "scenes": ["park", "museum"],
 "mots": "city, street, road, square, corner, bridge, building, park, museum, library, bank, church, map, way, traffic light, sidewalk, near, far, here, there, turn, walk, find, look for, Where is…?, Excuse me.",
 "tableau": {"t": "Où est… ? Il y a…",
  "l": "where is the museum? | où est le musée ?\nis there a bank near here? | y a-t-il une banque près d'ici ?\nthere is a park on the left | il y a un parc à gauche\nthere are two cafés | il y a deux cafés\nturn right at the corner | tournez à droite au coin\ngo straight ahead | allez tout droit",
  "a": "There is devant un singulier, there are devant un pluriel. Pour un lieu précis : Where is…? ; pour savoir s'il y en a un : Is there… near here?"},
 "blocs": """Excuse me, where is … ? | Excusez-moi, où est … ? | the museum / the subway station / Boston Common | le musée / la station de métro / Boston Common
Is there … near here? | Y a-t-il … près d'ici ? | a bank / a pharmacy / a restroom | une banque / une pharmacie / des toilettes
Is it … ? | C'est … ? | far / near / on the left | loin / près / à gauche
I'm looking for … . | Je cherche … . | Newbury Street / the library / my hotel | Newbury Street / la bibliothèque / mon hôtel
Can you show me on … ? | Pouvez-vous me montrer sur … ? | the map / my phone / this map | le plan / mon téléphone / ce plan""",
 "dialogue": {"t": "Demander son chemin", "l": """moi | Excuse me, where is the museum? | Excusez-moi, où est le musée ?
eux | Go straight ahead and turn left at the park. | Allez tout droit et tournez à gauche au parc.
moi | Is it far? | C'est loin ?
eux | No, it's about ten minutes on foot. | Non, c'est à environ dix minutes à pied.
moi | Thank you very much! | Merci beaucoup !
eux | You're welcome. Have a nice day! | De rien. Bonne journée !"""}},

{"id": "transports", "pour": "tous", "icone": "🚇", "s": "Se déplacer : le T, le bus, le vélo",
 "scenes": ["fahrradwerkstatt", "park"],
 "mots": "bus, subway, train, taxi, bike, car, bus stop, train station, platform, ticket, trip, driver, traffic, delay, map, go, take, leave, arrive, wait, ride, drive, today, tomorrow, late, early",
 "tableau": {"t": "Aller et prendre : to go, to take",
  "l": "I go downtown | je vais au centre-ville\nyou take the subway | tu prends le métro\nshe goes to work by bus | elle va au travail en bus\nwe take a taxi | nous prenons un taxi\nthe train leaves at ten | le train part à dix heures\nwhen does the bus come? | quand vient le bus ?",
  "a": "On prend un moyen de transport avec take (take the bus) ; « en bus » se dit by bus, mais « à pied » on foot. Le métro de Boston s'appelle « the T »."},
 "blocs": """A ticket to … , please. | Un billet pour … , s'il vous plaît. | Harvard / the airport / Cambridge | Harvard / l'aéroport / Cambridge
Does this bus go to … ? | Ce bus va à … ? | downtown / the airport / Harvard Square | au centre-ville / à l'aéroport / à Harvard Square
When does the next … leave? | Quand part le prochain … ? | train / bus / boat | train / bus / bateau
Where can I rent … ? | Où puis-je louer … ? | a bike / a car / a locker | un vélo / une voiture / un casier
Is this the stop for … ? | C'est l'arrêt pour … ? | the museum / the park / Fenway | le musée / le parc / Fenway""",
 "dialogue": {"t": "À l'arrêt de bus", "l": """moi | Excuse me, does this bus go downtown? | Excusez-moi, ce bus va au centre-ville ?
eux | Yes, take the 39. It comes every ten minutes. | Oui, prenez le 39. Il passe toutes les dix minutes.
moi | How much is a ticket? | Combien coûte un billet ?
eux | It's two dollars and forty cents. | Deux dollars quarante.
moi | Can I pay by card? | Je peux payer par carte ?
eux | Yes, you can tap your card on the bus. | Oui, vous pouvez passer votre carte dans le bus."""}},

{"id": "achats", "pour": "tous", "icone": "🛍️", "s": "Les achats : vêtements, tailles, prix",
 "scenes": ["kleidergeschaeft", "supermarkt"],
 "mots": "store, supermarket, shopping, clothes, shirt, T-shirt, sweater, pants, jeans, dress, shoe, jacket, size, color, fitting room, checkout, receipt, sale, cart, price, cheap, expensive, big, small, try, sell, How much is it?",
 "tableau": {"t": "Ce, ces : this, these",
  "l": "this shirt is nice | cette chemise est jolie\nthese shoes are too small | ces chaussures sont trop petites\nthat jacket over there | cette veste là-bas\nthose jeans are on sale | ces jeans-là sont en solde\nI'll take this one | je prends celui-ci\ndo you have it in blue? | vous l'avez en bleu ?",
  "a": "This / these pour ce qui est près de moi, that / those pour ce qui est plus loin. Les tailles américaines : small, medium, large (S, M, L)."},
 "blocs": """Do you have this in … ? | Vous avez ceci en … ? | medium / blue / a bigger size | taille M / bleu / une taille au-dessus
Can I try on … ? | Je peux essayer … ? | this sweater / these jeans / this dress | ce pull / ce jean / cette robe
It's too … . | C'est trop … . | big / small / expensive | grand / petit / cher
I'll take … . | Je prends … . | this one / these shoes / the blue one | celui-ci / ces chaussures / le bleu
Where is … ? | Où est … ? | the fitting room / the checkout / the shoe department | la cabine d'essayage / la caisse / le rayon des chaussures""",
 "dialogue": {"t": "Dans un magasin de vêtements", "l": """eux | Hi there! Can I help you? | Bonjour ! Je peux vous aider ?
moi | Yes, do you have this sweater in medium? | Oui, vous avez ce pull en taille M ?
eux | Sure, here you go. The fitting room is over there. | Bien sûr, voilà. La cabine d'essayage est là-bas.
moi | Thanks. How much is it? | Merci. Combien coûte-t-il ?
eux | It's forty dollars, but it's on sale today: thirty. | Quarante dollars, mais il est en solde aujourd'hui : trente.
moi | Great, I'll take it. | Super, je le prends."""}},

{"id": "sante", "pour": "tous", "icone": "💊", "s": "La santé : pharmacie, médecin",
 "scenes": ["apotheke", "arztpraxis"],
 "mots": "pharmacy, doctor, nurse, hospital, medicine, pill, prescription, appointment, pain, headache, fever, cold, cough, flu, head, stomach, back, throat, health, sick, tired, hurt, feel, help, need",
 "tableau": {"t": "Avoir mal : to hurt, to have",
  "l": "my head hurts | j'ai mal à la tête\nI have a headache | j'ai mal à la tête\nshe has a fever | elle a de la fièvre\nI have a cold | j'ai un rhume\nI feel sick | je me sens malade\ndo you have something for a cough? | avez-vous quelque chose contre la toux ?",
  "a": "Deux façons de dire « j'ai mal » : My back hurts (le dos fait mal) ou I have a backache. En cas d'urgence aux États-Unis : 911."},
 "blocs": """I have … . | J'ai … . | a headache / a fever / a sore throat | mal à la tête / de la fièvre / mal à la gorge
My … hurts. | J'ai mal … . | back / stomach / foot | au dos / au ventre / au pied
Do you have something for … ? | Avez-vous quelque chose contre … ? | a cold / a cough / the flu | le rhume / la toux / la grippe
I need … . | J'ai besoin … . | a doctor / an appointment / a pharmacy | d'un médecin / d'un rendez-vous / d'une pharmacie
I'm allergic to … . | Je suis allergique … . | penicillin / nuts / cats | à la pénicilline / aux noix / aux chats""",
 "dialogue": {"t": "À la pharmacie", "l": """eux | Hi, how can I help you? | Bonjour, que puis-je faire pour vous ?
moi | I have a bad cold and a sore throat. | J'ai un gros rhume et mal à la gorge.
eux | Do you have a fever? | Vous avez de la fièvre ?
moi | No, but I feel very tired. | Non, mais je me sens très fatigué.
eux | Take this, twice a day, after meals. | Prenez ceci, deux fois par jour, après les repas.
moi | Thank you. How much is it? | Merci. Combien ça coûte ?"""}},

{"id": "imprevus", "pour": "tous", "icone": "🧳", "s": "Les imprévus : perdre, attendre, réparer",
 "scenes": ["hotel", "flughafen"],
 "mots": "problem, key, passport, phone, wallet, bag, luggage, delay, mistake, help, lose, find, wait, call, fix, open, close, change, Excuse me., I'm sorry., No problem., I don't understand.",
 "tableau": {"t": "Hier : le prétérit (was, lost, found)",
  "l": "I lost my key | j'ai perdu ma clé\nmy flight was late | mon vol était en retard\nthe room was cold | la chambre était froide\nI found my phone | j'ai retrouvé mon téléphone\nwe waited an hour | nous avons attendu une heure\nsomeone called me | quelqu'un m'a appelé",
  "a": "Le prétérit raconte ce qui est arrivé : lose → lost, find → found, be → was / were. Les réguliers prennent -ed : waited, called."},
 "blocs": """I lost … . | J'ai perdu … . | my key / my passport / my phone | ma clé / mon passeport / mon téléphone
The … doesn't work. | Le … ne marche pas. | shower / Wi-Fi / heating | la douche / le wifi / le chauffage
My … was canceled. | Mon … a été annulé. | flight / train / reservation | vol / train / ma réservation
Can you … , please? | Pouvez-vous … , s'il vous plaît ? | help me / call a taxi / repeat that | m'aider / appeler un taxi / répéter
I'm sorry, I … . | Désolé, je … . | don't understand / am late / forgot | ne comprends pas / suis en retard / ai oublié""",
 "dialogue": {"t": "Un problème à l'hôtel", "l": """moi | Excuse me, I lost my room key. | Excusez-moi, j'ai perdu la clé de ma chambre.
eux | No problem. What's your room number? | Pas de problème. Quel est votre numéro de chambre ?
moi | Room 412. And the shower doesn't work. | La 412. Et la douche ne marche pas.
eux | I'm sorry. I'll send someone right away. | Désolé. J'envoie quelqu'un tout de suite.
moi | Thank you so much. | Merci beaucoup.
eux | Here is a new key. | Voici une nouvelle clé."""}},

{"id": "services", "pour": "tous", "icone": "🧺", "s": "Les services : laverie, coiffeur, banque",
 "scenes": ["waschsalon", "friseur"],
 "mots": "washing machine, money, coin, cash, credit card, bank, hairdresser, hair, towel, clothes, appointment, minute, hour, wash, cut, pay, open, close, wait, change",
 "tableau": {"t": "Pouvoir : can, can't",
  "l": "can I use this machine? | je peux utiliser cette machine ?\nyou can pay by card | vous pouvez payer par carte\nshe can't come today | elle ne peut pas venir aujourd'hui\ncan you cut my hair? | pouvez-vous me couper les cheveux ?\nwe can wait | nous pouvons attendre\nthey can't change money | ils ne peuvent pas changer d'argent",
  "a": "Can ne change jamais (she can) et le verbe qui suit reste nu. Pour une demande polie : Could you…? (pourriez-vous…?)."},
 "blocs": """Can I … here? | Je peux … ici ? | pay by card / wait / leave my bag | payer par carte / attendre / laisser mon sac
I need … . | J'ai besoin … . | change / quarters / a receipt | de monnaie / de pièces de 25 cents / d'un reçu
How long does … take? | Combien de temps dure … ? | the wash / the dryer / a haircut | le lavage / le séchage / une coupe
I'd like … . | Je voudrais … . | a haircut / an appointment / a shorter cut | une coupe / un rendez-vous / une coupe plus courte
What time do you … ? | À quelle heure … ? | open / close / start | ouvrez-vous / fermez-vous / commencez-vous""",
 "dialogue": {"t": "Chez le coiffeur", "l": """moi | Hi! Can I have a haircut today? | Bonjour ! Est-ce que je peux avoir une coupe aujourd'hui ?
eux | Sure, in about twenty minutes. Can you wait? | Bien sûr, dans une vingtaine de minutes. Vous pouvez attendre ?
moi | Yes, no problem. | Oui, pas de problème.
eux | How would you like it? | Comment la voulez-vous ?
moi | A little shorter, please. | Un peu plus courte, s'il vous plaît.
eux | Perfect. Have a seat. | Parfait. Asseyez-vous."""}},

{"id": "rencontrer", "pour": "tous", "icone": "🤝", "s": "Rencontrer des gens, être invité",
 "scenes": ["geburtstag", "familie"],
 "mots": "friend, family, guest, party, birthday, gift, name, age, country, language, job, Hello!, Nice to meet you., What's your name?, Where are you from?, How old are you?, Happy birthday!, Cheers!, like, love, meet, invite, celebrate, speak",
 "tableau": {"t": "Parler de soi : I'm, I'm from, I like",
  "l": "I'm Marie, I'm French | je suis Marie, je suis française\nI'm from Montreal | je viens de Montréal\nI'm thirty | j'ai trente ans\nI work in a bank | je travaille dans une banque\nI like music | j'aime la musique\nI speak a little English | je parle un peu anglais",
  "a": "Pour l'âge, on EST : I'm thirty. Pour le métier, un article : I'm a nurse. Les nationalités prennent une majuscule : French, Canadian."},
 "blocs": """Nice to meet you, I'm … . | Enchanté, je suis … . | Marie / Paul / Anna | Marie / Paul / Anna
I'm from … . | Je viens … . | France / Quebec / Belgium | de France / du Québec / de Belgique
I work as … . | Je travaille comme … . | a nurse / a teacher / an engineer | infirmière / professeur / ingénieur
I really like … . | J'aime beaucoup … . | Boston / this song / your house | Boston / cette chanson / ta maison
Thank you for … . | Merci pour … . | the invitation / the gift / dinner | l'invitation / le cadeau / le dîner""",
 "dialogue": {"t": "À une fête d'anniversaire", "l": """eux | Hi! I'm Jake. Are you a friend of Emma's? | Salut ! Je suis Jake. Tu es une amie d'Emma ?
moi | Yes! Nice to meet you, I'm Marie. | Oui ! Enchantée, je suis Marie.
eux | Where are you from, Marie? | Tu viens d'où, Marie ?
moi | I'm from Montreal. I'm here for a month. | Je viens de Montréal. Je suis ici pour un mois.
eux | Cool! Do you like Boston? | Génial ! Tu aimes Boston ?
moi | I love it. Cheers! | J'adore. Santé !"""}},

{"id": "plage", "pour": "voyage", "icone": "🏖️", "s": "La plage et le temps qu'il fait",
 "scenes": ["strand", "park", "winter"],
 "mots": "beach, sea, sun, sky, cloud, rain, snow, wind, weather, temperature, island, boat, hat, sunglasses, umbrella, towel, hot, cold, warm, sunny, rainy, windy, cloudy, swim, play",
 "tableau": {"t": "Le temps qu'il fait : it's…",
  "l": "it's sunny | il fait beau, il y a du soleil\nit's raining | il pleut\nit's snowing | il neige\nit's cold today | il fait froid aujourd'hui\nit's 75 degrees | il fait 24 °C (75 °F)\nwhat's the weather like? | quel temps fait-il ?",
  "a": "Le temps passe toujours par it : it's hot, it's raining. Aux États-Unis, la température est en Fahrenheit : 32 °F = 0 °C, 75 °F ≈ 24 °C."},
 "blocs": """It's … today. | Il fait … aujourd'hui. | sunny / cold / windy | beau / froid / du vent
Let's go to … . | Allons … . | the beach / the park / the island | à la plage / au parc / sur l'île
Don't forget … ! | N'oublie pas … ! | your hat / your sunglasses / the umbrella | ton chapeau / tes lunettes de soleil / le parapluie
Is the water … ? | L'eau est … ? | cold / warm / clean | froide / chaude / propre
Can we rent … ? | Peut-on louer … ? | a boat / an umbrella / two chairs | un bateau / un parasol / deux chaises""",
 "dialogue": {"t": "Une journée à la plage", "l": """eux | What's the weather like tomorrow? | Quel temps fait-il demain ?
moi | It's sunny and warm, about eighty degrees. | Il fait beau et chaud, environ vingt-sept degrés.
eux | Perfect! Let's go to the beach. | Parfait ! Allons à la plage.
moi | Great idea. Is the water cold? | Bonne idée. L'eau est froide ?
eux | A little. But you can swim. | Un peu. Mais on peut se baigner.
moi | Don't forget the sunglasses! | N'oublie pas les lunettes de soleil !"""}},

{"id": "visiter", "pour": "voyage", "icone": "🏛️", "s": "Visiter : musées, bibliothèques, horaires",
 "scenes": ["museum", "bibliothek"],
 "mots": "museum, library, ticket, painting, picture, art, photo, tourist, hour, morning, afternoon, Monday, Saturday, Sunday, open, close, visit, see, look, free, closed, What time is it?",
 "tableau": {"t": "Les horaires : at, on, from… to",
  "l": "it opens at ten | ça ouvre à dix heures\nit closes at five | ça ferme à dix-sept heures\nit's closed on Mondays | c'est fermé le lundi\nit's open from nine to six | c'est ouvert de neuf à dix-huit heures\nis it free on Sundays? | c'est gratuit le dimanche ?\nwhat time does it open? | à quelle heure ça ouvre ?",
  "a": "At + heure (at ten), on + jour (on Monday), from… to… pour une durée. Les Américains comptent sur 12 heures : 5 p.m. = 17 h."},
 "blocs": """What time does the … open? | À quelle heure ouvre … ? | museum / library / store | le musée / la bibliothèque / le magasin
Two tickets for … , please. | Deux billets pour … , s'il vous plaît. | adults / students / the exhibition | adultes / étudiants / l'exposition
Can I take … ? | Est-ce que je peux prendre … ? | photos / a map / a guide | des photos / un plan / un guide
Is it free on … ? | C'est gratuit le … ? | Sundays / Wednesdays / weekends | dimanche / mercredi / week-end
Where is … ? | Où est … ? | the gift shop / the café / the exit | la boutique / le café / la sortie""",
 "dialogue": {"t": "À l'entrée du musée", "l": """moi | Hi! Two tickets, please. | Bonjour ! Deux billets, s'il vous plaît.
eux | Are you students? | Vous êtes étudiants ?
moi | No. How much is it? | Non. Combien ça coûte ?
eux | Twenty-five dollars each. | Vingt-cinq dollars chacun.
moi | Can I take photos inside? | On peut prendre des photos à l'intérieur ?
eux | Yes, but no flash, please. | Oui, mais sans flash, s'il vous plaît."""}},
]

INSTALLE = [
{"id": "logement", "pour": "installe", "icone": "🏠", "s": "Le logement : chercher, louer, les voisins",
 "scenes": ["umzug", "wohnzimmer"],
 "mots": "house, apartment, room, bedroom, kitchen, bathroom, living room, door, window, wall, floor, stairs, balcony, garden, table, chair, sofa, closet, lamp, rug, mirror, fridge, stove, rent, furniture, neighbor, live, rent, move",
 "tableau": {"t": "Habiter : to live",
  "l": "I live in an apartment | j'habite dans un appartement\nyou live near downtown | tu habites près du centre-ville\nshe lives on the third floor | elle habite au troisième étage\nwe live with a roommate | nous habitons avec un colocataire\nthey live in Cambridge | ils habitent à Cambridge\nwhere do you live? | où habites-tu ?",
  "a": "Live in + ville ou quartier, live on + rue ou étage. Attention : le premier étage américain est le rez-de-chaussée (first floor = ground floor en Grande-Bretagne)."},
 "blocs": """I'm looking for … . | Je cherche … . | an apartment / a room / a roommate | un appartement / une chambre / un colocataire
How much is … ? | Combien coûte … ? | the rent / the deposit / heating | le loyer / la caution / le chauffage
Is … included? | Est-ce que … est compris ? | heating / Wi-Fi / electricity | le chauffage / le wifi / l'électricité
The … is broken. | Le … est cassé. | fridge / stove / lamp | frigo / la cuisinière / la lampe
Hi, I'm your new … . | Bonjour, je suis votre nouveau … . | neighbor / tenant / roommate | voisin / locataire / colocataire""",
 "dialogue": {"t": "Visiter un appartement", "l": """eux | Hi! Come in. This is the living room. | Bonjour ! Entrez. Voici le salon.
moi | It's very bright. How many bedrooms are there? | Il est très lumineux. Combien y a-t-il de chambres ?
eux | Two bedrooms and one bathroom. | Deux chambres et une salle de bain.
moi | How much is the rent? | Combien est le loyer ?
eux | Two thousand dollars a month, heating included. | Deux mille dollars par mois, chauffage compris.
moi | Can I move in next month? | Je peux emménager le mois prochain ?"""}},
{"id": "demarches", "pour": "installe", "icone": "🏛️", "s": "Les démarches : City Hall, formulaires",
 "scenes": ["buergeramt", "buero"],
 "mots": "address, name, first name, last name, age, nationality, country, passport, contract, office, desk, paper, pen, appointment, question, answer, help, need, write, spell, explain, understand, repeat, How do you spell that?, Can you repeat that, please?",
 "tableau": {"t": "Remplir un formulaire",
  "l": "first name · last name | prénom · nom de famille\ndate of birth | date de naissance\naddress · zip code | adresse · code postal\nphone number | numéro de téléphone\nsign here, please | signez ici, s'il vous plaît\nhow do you spell that? | comment ça s'écrit ?",
  "a": "Les dates américaines mettent le mois d'abord : 07/04/1995 = le 4 juillet 1995. Pour épeler son nom, l'alphabet est dans les repères."},
 "blocs": """I need … . | J'ai besoin … . | a form / an appointment / a copy | d'un formulaire / d'un rendez-vous / d'une copie
My … is … . | Mon … est … . | address / last name / phone number | adresse / nom de famille / numéro de téléphone
Can you help me with … ? | Pouvez-vous m'aider avec … ? | this form / my application / this letter | ce formulaire / ma demande / cette lettre
Do I need … ? | Ai-je besoin … ? | my passport / a photo / my contract | de mon passeport / d'une photo / de mon contrat
Sorry, can you … ? | Désolé, pouvez-vous … ? | repeat that / speak slowly / spell it | répéter / parler lentement / l'épeler""",
 "dialogue": {"t": "Au guichet de City Hall", "l": """eux | Good morning. How can I help you? | Bonjour. Que puis-je faire pour vous ?
moi | Hi, I need a form for a parking permit. | Bonjour, j'ai besoin d'un formulaire pour un permis de stationnement.
eux | Sure. What's your address? | Bien sûr. Quelle est votre adresse ?
moi | 25 Beacon Street, apartment 3. | 25 Beacon Street, appartement 3.
eux | And your last name? How do you spell it? | Et votre nom de famille ? Comment ça s'écrit ?
moi | T-R-E-M-B-L-A-Y. | T-R-E-M-B-L-A-Y."""}},
]

# La suite : une etape par groupe de themes ; elle prend tout l'A1 qui reste.
SUITE = [
 {"id": "famille", "icone": "👨‍👩‍👧", "s": "La famille et les proches", "scene": "familie", "themes": ["family_a1", "people_a1"],
  "tableau": {"t": "Avoir : to have, has",
   "l": "I have a brother | j'ai un frère\nyou have two kids | tu as deux enfants\nshe has a big family | elle a une grande famille\nwe have a dog | nous avons un chien\nthey have three cousins | ils ont trois cousins\ndo you have brothers or sisters? | as-tu des frères et sœurs ?",
   "a": "Have devient has avec he, she, it. Question et négation avec do / does : Does she have a car? I don't have a car."}},
 {"id": "maison", "icone": "🛏️", "s": "La maison et la chambre", "scene": "schlafzimmer", "themes": ["home_a1"],
  "tableau": {"t": "Où sont les choses : in, on, under",
   "l": "the keys are on the table | les clés sont sur la table\nthe cat is under the bed | le chat est sous le lit\nmy clothes are in the closet | mes vêtements sont dans le placard\nthe lamp is next to the sofa | la lampe est à côté du canapé\nthe garden is behind the house | le jardin est derrière la maison\nthere's a picture on the wall | il y a un tableau au mur",
   "a": "On pour une surface (on the table, on the wall), in pour l'intérieur (in the closet), under pour dessous."}},
 {"id": "cuisine", "icone": "🍳", "s": "Manger et cuisiner", "scene": "kueche", "themes": ["food_a1", "eatingout_a1"],
  "tableau": {"t": "Du, de la : some, any",
   "l": "I'd like some bread | je voudrais du pain\nis there any milk? | y a-t-il du lait ?\nthere isn't any sugar | il n'y a pas de sucre\nwe need some eggs | il nous faut des œufs\nI don't eat meat | je ne mange pas de viande\nhow much water? how many eggs? | combien d'eau ? combien d'œufs ?",
   "a": "Some dans les phrases affirmatives, any dans les questions et les négations. How much pour ce qui ne se compte pas (water), how many pour ce qui se compte (eggs)."}},
 {"id": "travail", "icone": "💼", "s": "Le travail et le bureau", "scene": "buero", "themes": ["work_a1"],
  "tableau": {"t": "Le présent simple : I work, she works",
   "l": "I work in an office | je travaille dans un bureau\nshe works from home | elle travaille de chez elle\nwe start at nine | nous commençons à neuf heures\nhe doesn't work on Fridays | il ne travaille pas le vendredi\nwhat do you do? | que fais-tu dans la vie ?\nI'm a nurse | je suis infirmière",
   "a": "Le présent simple dit l'habitude ; -s à la 3ᵉ personne. « Que fais-tu dans la vie ? » : What do you do?"}},
 {"id": "ecole", "icone": "📚", "s": "L'école et les études", "scene": "klassenzimmer", "themes": ["school_a1"],
  "tableau": {"t": "Les questions : what, when, where",
   "l": "what do you study? | qu'est-ce que tu étudies ?\nwhen is the exam? | quand est l'examen ?\nwhere is the classroom? | où est la salle de classe ?\nwho is your teacher? | qui est ton professeur ?\nwhy are you late? | pourquoi es-tu en retard ?\nhow do you spell it? | comment ça s'écrit ?",
   "a": "Le mot interrogatif d'abord, puis do / does pour les verbes ordinaires ; avec be, on inverse simplement : Where is it?"}},
 {"id": "loisirs", "icone": "⚽", "s": "Les loisirs et le sport", "scene": "sportplatz", "themes": ["freetime_a1", "animals_a1"],
  "tableau": {"t": "Aimer faire : I like + -ing",
   "l": "I like swimming | j'aime nager\nshe loves dancing | elle adore danser\nwe don't like running | nous n'aimons pas courir\ndo you like playing soccer? | aimes-tu jouer au foot ?\nI play the guitar | je joue de la guitare\nhe plays tennis | il joue au tennis",
   "a": "Après like, love, hate : le verbe en -ing (I like reading). Play the + instrument, play + sport, sans article."}},
 {"id": "corps", "icone": "🩺", "s": "Le corps et la santé", "scene": "untersuchung", "themes": ["body_a1", "clothes_a1"],
  "tableau": {"t": "En ce moment : I'm -ing",
   "l": "I'm wearing a sweater | je porte un pull\nshe's taking a pill | elle prend un comprimé\nwe're waiting for the doctor | nous attendons le médecin\nthey're sleeping | ils dorment\nwhat are you doing? | que fais-tu ?\nmy leg is hurting | ma jambe me fait mal",
   "a": "Be + -ing pour ce qui se passe maintenant. Le présent simple (I wear) dit l'habitude, le présent en -ing (I'm wearing) le moment présent."}},
 {"id": "societe", "icone": "📱", "s": "La ville, la technologie, les sentiments", "scene": "musik", "themes": ["city_a1", "tech_a1", "feelings_a1", "everyday_a1", "time_a1", "weather_a1", "shopping_a1", "travel_a1"],
  "tableau": {"t": "Comparer : bigger, more expensive",
   "l": "Boston is smaller than New York | Boston est plus petite que New York\nmy phone is newer | mon téléphone est plus récent\nthis app is more useful | cette application est plus utile\nit's the best café in town | c'est le meilleur café de la ville\nwinter is colder here | l'hiver est plus froid ici\nI'm happier now | je suis plus heureux maintenant",
   "a": "Adjectif court : -er et the -est (bigger, the biggest). Adjectif long : more et the most. « Que » se dit than."}},
]
