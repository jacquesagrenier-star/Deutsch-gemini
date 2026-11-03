# -*- coding: utf-8 -*-
"""Manger et gouter, theme illustre (3 nov. 2026). ET C'EST FACTURE : 0,15 $ l'image, chez fal -- RIEN NE SE LANCE
SANS L'ACCORD DE JACQUES, donne dans la session du theme (proposition : 32 images, 4,80 $, 6 $ au plus).

    python visuel/manger/manger.py --json        # manger.json et gloses.json seuls, gratuit
    python visuel/manger/manger.py --montrer     # les prompts seuls, gratuit
    python visuel/manger/manger.py               # les images qui manquent (0,15 $ chacune)
    python visuel/manger/manger.py gout-Carmen   # celle-la seulement
    python visuel/manger/manger.py --refaire gout-Carmen   # l'ancienne passe en <nom>-rate<n>.png

L'ANGLE (regle 2 des themes : pas de scene refaite) : ni la cuisine, ni le supermarche, ni le marche, ni la
boulangerie, ni le restaurant comme lieu. Ici, des PERSONNES qui goutent, aiment ou n'aiment pas, et commandent :
les gouts (me gusta / gustan, ich mag, das schmeckt mir), les saveurs (dulce, salado, picante, amargo, acido / suss,
salzig, scharf, bitter, sauer), les quantites (un kilo de, una botella de, un poco de / ein Kilo, eine Flasche, ein
bisschen) et la commande au cafe (Quisiera..., La cuenta, por favor / Ich haette gern..., Die Rechnung, bitte).
Le lien avec « Les contraires » : rico / asqueroso, lecker / eklig ; avec « Emotions » : les visages qui aiment.

Trois sortes d'images :
  - 16 DEGUSTATIONS, tete et epaules (1:1), par RETOUCHE de nos personnes (nano-banana-pro/edit) : le meme visage.
    Ben et Mia ne font qu'aimer (le filtre de fal refuse un enfant en detresse, vu le 3 nov.) ;
  - 10 QUANTITES, natures mortes sans personne (4:3, texte -> image), sans aucun texte dans l'image ;
  - 6 MOMENTS AU CAFE (4:3), le meme cafe : chaque moment part du precedent (continuite du decor).
La carte et ses prix, la liste de courses : dessinees dans la page (fal ecrit mal).
Toutes les phrases de la page sont FABRIQUEES depuis manger.json : une image ne dit que ce qu'elle montre.
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/manger/img/.
"""
import hashlib, io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SORTIE = os.path.join(RACINE, "visuel", "prototype", "manger")

EDIT, T2I, PRIX = "fal-ai/nano-banana-pro/edit", "fal-ai/nano-banana-pro", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "manger", "img")
# les sources des personnes, en pied : les memes qu'emociones.py
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
SOURCES = {"Mark": PRINCIPAL + "/personnages/Mark.png", "Anna": FAMILLE + "/Anna-quotidien.png"}
for n in ("Gisela", "Ben", "Mia", "Heinz", "Peter", "Monika", "Sabine", "Frank", "Jan", "Katrin", "Lena", "Felix", "Sophie"):
    SOURCES[n] = FAMILLE + "/" + n + ".png"
for n in ("Carmen", "Diego", "Marta", "Javier", "Rosa", "Lucas", "Tomas", "Elena", "Ines", "Pablo"):
    SOURCES[n] = PRINCIPAL + "/visuel/descripcion/img/" + n + ".png"
SEXE = {"Anna": "f", "Carmen": "f", "Gisela": "f", "Mark": "m", "Diego": "m", "Ben": "m", "Mia": "f", "Marta": "f",
        "Javier": "m", "Rosa": "f", "Lucas": "m", "Tomas": "m", "Elena": "f", "Ines": "f", "Pablo": "m", "Heinz": "m",
        "Peter": "m", "Felix": "m"}
NOMS = {"Ines": "Inés", "Tomas": "Tomás"}
ENFANTS = {"Ben", "Mia"}

# ---------- LES MOTS ----------
# Les saveurs : es [m, f, m pl, f pl], de (attribut, invariable), et la forme nominale allemande (« etwas Saures »).
SAVEURS = {
    "dulce":   {"es": ["dulce", "dulce", "dulces", "dulces"], "de": "süß", "etwas": "Süßes"},
    "salado":  {"es": ["salado", "salada", "salados", "saladas"], "de": "salzig", "etwas": "Salziges"},
    "picante": {"es": ["picante", "picante", "picantes", "picantes"], "de": "scharf", "etwas": "Scharfes"},
    "amargo":  {"es": ["amargo", "amarga", "amargos", "amargas"], "de": "bitter", "etwas": "Bitteres"},
    "acido":   {"es": ["ácido", "ácida", "ácidos", "ácidas"], "de": "sauer", "etwas": "Saures"},
}
# Les aliments goutes. es : le mot du corpus (singulier), son genre, pl = montre au pluriel (las fresas) ;
# « vu » = ce que dit la phrase (la comida picante). de : idem ; « nom » = sujet au nominatif (die Erdbeeren),
# « gen » = le mot general apres mag (Erdbeeren, scharfes Essen), « kein » = la negation qui va avec (keine, kein,
# keinen : accusatif). saveur : la sienne, ou rien si l'image ne la montre pas (pas de question de saveur).
# estar : la soupe EST TROP salee maintenant (está salada), le citron est acide (es acido).
ALIMENTS = {
    "tarta":     {"es": {"mot": "tarta", "genre": "la", "vu": "la tarta"},
                  "de": {"mot": "Kuchen", "genre": "der", "nom": "der Kuchen", "gen": "Kuchen", "kein": "keinen"}, "saveur": "dulce"},
    "chocolate": {"es": {"mot": "chocolate", "genre": "el", "vu": "el chocolate"},
                  "de": {"mot": "Schokolade", "genre": "die", "nom": "die Schokolade", "gen": "Schokolade", "kein": "keine"}, "saveur": "dulce"},
    "limon":     {"es": {"mot": "limón", "genre": "el", "vu": "el limón"},
                  "de": {"mot": "Zitrone", "genre": "die", "nom": "die Zitrone", "gen": "Zitronen", "kein": "keine"}, "saveur": "acido"},
    "picante":   {"es": {"mot": "comida", "genre": "la", "vu": "la comida picante", "court": "la comida"},
                  "de": {"mot": "Essen", "genre": "das", "nom": "das scharfe Essen", "gen": "scharfes Essen", "kein": "kein", "court": "das Essen"}, "saveur": "picante"},
    "cafe":      {"es": {"mot": "café", "genre": "el", "vu": "el café"},
                  "de": {"mot": "Kaffee", "genre": "der", "nom": "der Kaffee", "gen": "schwarzen Kaffee", "kein": "keinen"}, "saveur": "amargo"},
    "sopa":      {"es": {"mot": "sopa", "genre": "la", "vu": "la sopa"},
                  "de": {"mot": "Suppe", "genre": "die", "nom": "die Suppe", "gen": None, "kein": None}, "saveur": "salado", "estar": True},
    "pretzel":   {"es": {"mot": "pretzel", "genre": "el", "vu": "el pretzel"},
                  "de": {"mot": "Brezel", "genre": "die", "nom": "die Brezel", "gen": "Brezeln", "kein": "keine"}, "saveur": "salado"},
    "fresa":     {"es": {"mot": "fresa", "genre": "la", "vu": "las fresas", "pl": True},
                  "de": {"mot": "Erdbeere", "genre": "die", "nom": "die Erdbeeren", "gen": "Erdbeeren", "kein": "keine", "pl": True}, "saveur": "dulce"},
    "pescado":   {"es": {"mot": "pescado", "genre": "el", "vu": "el pescado"},
                  "de": {"mot": "Fisch", "genre": "der", "nom": "der Fisch", "gen": "Fisch", "kein": "keinen"}, "saveur": None},
    "galleta":   {"es": {"mot": "galleta", "genre": "la", "vu": "las galletas", "pl": True},
                  "de": {"mot": "Keks", "genre": "der", "nom": "die Kekse", "gen": "Kekse", "kein": "keine", "pl": True}, "saveur": "dulce"},
    "pizza":     {"es": {"mot": "pizza", "genre": "la", "vu": "la pizza"},
                  "de": {"mot": "Pizza", "genre": "die", "nom": "die Pizza", "gen": "Pizza", "kein": "keine"}, "saveur": None},
    "queso":     {"es": {"mot": "queso", "genre": "el", "vu": "el queso"},
                  "de": {"mot": "Käse", "genre": "der", "nom": "der Käse", "gen": "Käse", "kein": "keinen"}, "saveur": None},
    "tomate":    {"es": {"mot": "tomate", "genre": "el", "vu": "los tomates", "pl": True},
                  "de": {"mot": "Tomate", "genre": "die", "nom": "die Tomaten", "gen": "Tomaten", "kein": "keine", "pl": True}, "saveur": None},
}
# La traduction des aliments (fr en pt) : apres « aimer » (fr : le citron), sans article en anglais, apres « gostar de »
# en portugais du Bresil (de limao, da sopa) ; sujet d'une phrase de saveur (fr : Le citron est...).
TRAD_ALIMENTS = {
    "tarta":     {"fr": ["le gâteau", "Le gâteau", "est sucré"], "en": ["cake", "Cake", "is sweet"], "pt": ["de bolo", "O bolo", "é doce"]},
    "chocolate": {"fr": ["le chocolat", "Le chocolat", "est sucré"], "en": ["chocolate", "Chocolate", "is sweet"], "pt": ["de chocolate", "O chocolate", "é doce"]},
    "limon":     {"fr": ["le citron", "Le citron", "est acide"], "en": ["lemon", "Lemon", "is sour"], "pt": ["de limão", "O limão", "é azedo"]},
    "picante":   {"fr": ["les plats épicés", "Le plat", "est épicé"], "en": ["spicy food", "The food", "is spicy"], "pt": ["de comida apimentada", "A comida", "é apimentada"]},
    "cafe":      {"fr": ["le café noir", "Le café noir", "est amer"], "en": ["black coffee", "Black coffee", "is bitter"], "pt": ["de café puro", "O café puro", "é amargo"]},
    "sopa":      {"fr": ["la soupe", "La soupe", "est salée"], "en": ["the soup", "The soup", "is salty"], "pt": ["da sopa", "A sopa", "está salgada"]},
    "pretzel":   {"fr": ["les bretzels", "Le bretzel", "est salé"], "en": ["pretzels", "The pretzel", "is salty"], "pt": ["de pretzel", "O pretzel", "é salgado"]},
    "fresa":     {"fr": ["les fraises", "Les fraises", "sont sucrées"], "en": ["strawberries", "Strawberries", "are sweet"], "pt": ["de morango", "Os morangos", "são doces"]},
    "pescado":   {"fr": ["le poisson", "Le poisson", ""], "en": ["fish", "Fish", ""], "pt": ["de peixe", "O peixe", ""]},
    "galleta":   {"fr": ["les biscuits", "Les biscuits", "sont sucrés"], "en": ["cookies", "Cookies", "are sweet"], "pt": ["de biscoito", "Os biscoitos", "são doces"]},
    "pizza":     {"fr": ["la pizza", "La pizza", ""], "en": ["pizza", "Pizza", ""], "pt": ["de pizza", "A pizza", ""]},
    "queso":     {"fr": ["le fromage", "Le fromage", ""], "en": ["cheese", "Cheese", ""], "pt": ["de queijo", "O queijo", ""]},
    "tomate":    {"fr": ["les tomates", "Les tomates", ""], "en": ["tomatoes", "Tomatoes", ""], "pt": ["de tomate", "Os tomates", ""]},
}

# Les 16 degustations : qui, quoi, la reaction (encanta, gusta, no, nada), et ce que le visage montre.
# Une personne une fois ; les paires du meme aliment (le citron, les plats epices, le cafe noir) opposent un « oui »
# et un « non » : la seule question « a qui ne plait pas... ? » qui ne suppose rien de ce qu'on ne voit pas.
REACTIONS = {
    "encanta": "absolutely delighted: eyes closed with pleasure or shining, a big happy smile, clearly loving the taste.",
    "gusta":   "enjoying it: a warm, satisfied smile while tasting, relaxed and pleased.",
    "no":      "does not like it: a clear grimace of displeasure, the nose wrinkled, the mouth pulled to one side, pulling slightly back from the food.",
    "nada":    "disgusted: a strong grimace of disgust, the tongue slightly out, pushing the plate away with one hand, leaning back.",
}
DEGUSTATIONS = [
    ("Ben",    "tarta",     "encanta", "eating a slice of chocolate cake with a small fork, a little chocolate on the corner of the mouth."),
    ("Mia",    "chocolate", "encanta", "holding a square of milk chocolate from a bar in her hand and biting into it."),
    ("Carmen", "limon",     "no",      "has just bitten into a slice of fresh lemon held in her fingers; the sourness makes her squint and pucker her lips."),
    ("Tomas",  "limon",     "gusta",   "sucking happily on a slice of fresh lemon held in his fingers, enjoying the sour taste."),
    ("Diego",  "picante",   "gusta",   "eating a bowl of very spicy red chili stew with fresh red chili peppers on top, a spoon in hand; his cheeks are a bit red and a drop of sweat is on his forehead, but he loves it."),
    ("Elena",  "picante",   "no",      "has just tasted a spoonful of very spicy red chili stew with fresh red chili peppers on top; her face is red, her eyes watery, she fans her open mouth with her hand."),
    ("Mark",   "cafe",      "gusta",   "drinking a small cup of black espresso coffee, no milk, savouring it."),
    ("Marta",  "cafe",      "no",      "has just tasted a small cup of black espresso coffee, no milk; the bitterness makes her grimace, the tongue slightly out."),
    ("Javier", "sopa",      "no",      "has just tasted a spoonful of vegetable soup from a bowl; it is far too salty: he grimaces and holds the salt shaker away in his other hand."),
    ("Rosa",   "pretzel",   "gusta",   "biting into a big soft pretzel covered with coarse salt crystals."),
    ("Anna",   "fresa",     "gusta",   "eating fresh red strawberries from a small bowl, holding one strawberry near her mouth."),
    ("Lucas",  "pescado",   "nada",    "in front of a plate with a whole grilled fish."),
    ("Felix",  "galleta",   "gusta",   "eating round butter cookies from a small plate, holding one cookie."),
    ("Pablo",  "pizza",     "encanta", "biting into a slice of pizza with melted cheese and tomato."),
    ("Heinz",  "queso",     "gusta",   "tasting a piece of cheese from a small wooden board with several cheeses, nodding with approval."),
    ("Peter",  "tomate",    "no",      "in front of a small plate of sliced fresh tomatoes, pushing it slightly away with one finger."),
]
# Ce que la personne dit en goutant : « ¡Qué rico! » / « Lecker! » quand elle aime ; « ¡Está asqueroso! » /
# « Igitt, das ist eklig! » pour le degout ; sinon la saveur de trop (« ¡Está demasiado ácido! » / « Das ist zu
# sauer! ») ; sans saveur, ce qu'elle n'aime pas (« No me gustan los tomates. »).

# Les QUANTITES (10 natures mortes) : le contenant (mot du corpus) et ce qu'il contient.
CONTENANTS = {
    "kilo":    {"es": {"mot": "kilo", "genre": "el", "art": "un kilo de"},        "de": {"mot": "Kilo", "genre": "das", "art": "ein Kilo"}},
    "botella": {"es": {"mot": "botella", "genre": "la", "art": "una botella de"}, "de": {"mot": "Flasche", "genre": "die", "art": "eine Flasche"}},
    "vaso":    {"es": {"mot": "vaso", "genre": "el", "art": "un vaso de"},        "de": {"mot": "Glas", "genre": "das", "art": "ein Glas"}},
    "taza":    {"es": {"mot": "taza", "genre": "la", "art": "una taza de"},       "de": {"mot": "Tasse", "genre": "die", "art": "eine Tasse"}},
    "trozo":   {"es": {"mot": "trozo", "genre": "el", "art": "un trozo de"},      "de": {"mot": "Stück", "genre": "das", "art": "ein Stück"}},
    "lata":    {"es": {"mot": "lata", "genre": "la", "art": "una lata de"},       "de": {"mot": "Dose", "genre": "die", "art": "eine Dose"}},
    "docena":  {"es": {"mot": "docena", "genre": "la", "art": "una docena de"},   "de": {"mot": "Dutzend", "genre": "das", "art": "ein Dutzend"}},
    "loncha":  {"es": {"mot": "loncha", "genre": "la", "art": "una loncha de"},   "de": {"mot": "Scheibe", "genre": "die", "art": "eine Scheibe"}},
    "litro":   {"es": {"mot": "litro", "genre": "el", "art": "un litro de"},      "de": {"mot": "Liter", "genre": "der", "art": "ein Liter"}},
    "poco":    {"es": {"mot": None, "art": "un poco de"},                          "de": {"mot": None, "art": "ein bisschen"}},
}
# Les contenants qu'une meme image pourrait aussi montrer : une bouteille d'eau peut faire un litre.
VOISINS_CONTENANTS = {"botella": ["litro"], "litro": ["botella"]}
CONTENUS = {
    "naranja": {"es": {"mot": "naranja", "genre": "la", "dit": "naranjas"}, "de": {"mot": "Orange", "genre": "die", "dit": "Orangen"},
                "tr": {"fr": "oranges", "en": "oranges", "pt": "laranjas", "de": "Orangen"}},
    "agua":    {"es": {"mot": "agua", "genre": "el", "dit": "agua"}, "de": {"mot": "Wasser", "genre": "das", "dit": "Wasser"},
                "tr": {"fr": "eau", "en": "water", "pt": "água", "de": "Wasser"}},
    "leche":   {"es": {"mot": "leche", "genre": "la", "dit": "leche"}, "de": {"mot": "Milch", "genre": "die", "dit": "Milch"},
                "tr": {"fr": "lait", "en": "milk", "pt": "leite", "de": "Milch"}},
    "te":      {"es": {"mot": "té", "genre": "el", "dit": "té"}, "de": {"mot": "Tee", "genre": "der", "dit": "Tee"},
                "tr": {"fr": "thé", "en": "tea", "pt": "chá", "de": "Tee"}},
    "tarta":   {"es": {"mot": "tarta", "genre": "la", "dit": "tarta"}, "de": {"mot": "Kuchen", "genre": "der", "dit": "Kuchen"},
                "tr": {"fr": "gâteau", "en": "cake", "pt": "bolo", "de": "Kuchen"}},
    "tomate":  {"es": {"mot": "tomate", "genre": "el", "dit": "tomates"}, "de": {"mot": "Tomate", "genre": "die", "dit": "Tomaten"},
                "tr": {"fr": "tomates", "en": "tomatoes", "pt": "tomates", "de": "Tomaten"}},
    "huevo":   {"es": {"mot": "huevo", "genre": "el", "dit": "huevos"}, "de": {"mot": "Ei", "genre": "das", "dit": "Eier"},
                "tr": {"fr": "œufs", "en": "eggs", "pt": "ovos", "de": "Eier"}},
    "queso":   {"es": {"mot": "queso", "genre": "el", "dit": "queso"}, "de": {"mot": "Käse", "genre": "der", "dit": "Käse"},
                "tr": {"fr": "fromage", "en": "cheese", "pt": "queijo", "de": "Käse"}},
    "azucar":  {"es": {"mot": "azúcar", "genre": "el", "dit": "azúcar"}, "de": {"mot": "Zucker", "genre": "der", "dit": "Zucker"},
                "tr": {"fr": "sucre", "en": "sugar", "pt": "açúcar", "de": "Zucker"}},
}
# fr / en / pt du contenant (« une bouteille d' », « a bottle of », « uma garrafa de »)
TRAD_CONTENANTS = {
    "kilo":    {"fr": "un kilo de ", "en": "a kilo of ", "pt": "um quilo de "},
    "botella": {"fr": "une bouteille de ", "en": "a bottle of ", "pt": "uma garrafa de "},
    "vaso":    {"fr": "un verre de ", "en": "a glass of ", "pt": "um copo de "},
    "taza":    {"fr": "une tasse de ", "en": "a cup of ", "pt": "uma xícara de "},
    "trozo":   {"fr": "un morceau de ", "en": "a piece of ", "pt": "um pedaço de "},
    "lata":    {"fr": "une boîte de ", "en": "a can of ", "pt": "uma lata de "},
    "docena":  {"fr": "une douzaine d'", "en": "a dozen ", "pt": "uma dúzia de "},
    "loncha":  {"fr": "une tranche de ", "en": "a slice of ", "pt": "uma fatia de "},
    "litro":   {"fr": "un litre de ", "en": "a litre of ", "pt": "um litro de "},
    "poco":    {"fr": "un peu de ", "en": "a little ", "pt": "um pouco de "},
}
# fr : l'elision devant une voyelle (« une bouteille d'eau »)
QUANTITES = [
    ("kilo",    "naranja", "About one kilo of fresh oranges (seven or eight oranges) in the bowl of a simple kitchen scale."),
    ("botella", "agua",    "One single clear plastic bottle of still water, closed, standing upright."),
    ("vaso",    "leche",   "One single clear drinking glass full of milk."),
    ("taza",    "te",      "One single white ceramic cup of hot tea on its saucer, a tea bag string hanging over the rim, light steam."),
    ("trozo",   "tarta",   "One single slice of cake on a small white plate, with a small fork."),
    ("lata",    "tomate",  "One single closed tin can of peeled tomatoes, with a plain red label showing a picture of tomatoes, no words."),
    ("docena",  "huevo",   "Twelve brown eggs in an open cardboard egg box with two rows of six."),
    ("loncha",  "queso",   "One single thin slice of yellow cheese lying flat on a small wooden board."),
    ("litro",   "leche",   "One single closed one-litre carton of milk, white and blue, with a plain picture of a glass of milk and no words."),
    ("poco",    "azucar",  "A teaspoon with a small amount of white sugar, next to a small white sugar bowl."),
]

# LES MOMENTS AU CAFE : Mark et Tomas, clients ; Javier, le serveur ; Ines, la serveuse. Le meme cafe tout du long.
# Pas Anna : le cafe a deux avec Mark est un moment de l'histoire a ne pas depenser (scenes/personnages.json, _arc).
# Chaque moment : la personne qui parle, ce qu'elle dit (es, de), la phrase qui decrit le moment, le mot qu'il porte.
CAFE = [
    {"id": "carta", "qui": "Mark", "gens": ["Mark", "Tomas", "Javier"],
     "scene": "Mark and Tomas have just sat down at a small round table by the window; there is nothing on the table yet. Mark raises his hand with a friendly smile to call the waiter Javier, who is walking towards them with two menus under his arm.",
     "es": {"dit": "La carta, por favor.", "fait": "Mark pide la carta.", "mot": {"mot": "carta", "genre": "la"}},
     "de": {"dit": "Die Speisekarte, bitte.", "fait": "Mark möchte die Speisekarte.", "mot": {"mot": "Speisekarte", "genre": "die"}},
     "tr": {"fr": ["La carte, s'il vous plaît.", "Mark demande la carte."], "en": ["The menu, please.", "Mark asks for the menu."],
            "pt": ["O cardápio, por favor.", "Mark pede o cardápio."], "de": ["Die Speisekarte, bitte.", "Mark möchte die Speisekarte."]}},
    {"id": "pedir", "qui": "Mark", "gens": ["Mark", "Tomas", "Javier"],
     "scene": "Mark and Tomas sit at the same table, each holding an open menu. The waiter Javier stands beside the table writing the order on a small notepad; Mark speaks to him, pointing at a line on his menu.",
     "es": {"dit": "Quisiera un café, por favor.", "fait": "Mark pide un café.", "mot": {"mot": "pedir", "cat": "verbe"}},
     "de": {"dit": "Ich hätte gern einen Kaffee, bitte.", "fait": "Mark bestellt einen Kaffee.", "mot": {"mot": "bestellen", "cat": "verbe"}},
     "tr": {"fr": ["Je voudrais un café, s'il vous plaît.", "Mark commande un café."], "en": ["I'd like a coffee, please.", "Mark orders a coffee."],
            "pt": ["Eu queria um café, por favor.", "Mark pede um café."], "de": ["Ich hätte gern einen Kaffee, bitte.", "Mark bestellt einen Kaffee."]}},
    {"id": "camarera", "qui": "Ines", "gens": ["Ines", "Mark", "Tomas"],
     "scene": "At the same table, the waitress Ines arrives with a tray and puts down a cup of coffee, a glass of orange juice and a slice of cake in front of Mark and Tomas, smiling.",
     "es": {"dit": "Aquí tienen.", "fait": "La camarera trae el café.", "mot": {"mot": "camarera", "genre": "la"}},
     "de": {"dit": "Bitte schön.", "fait": "Die Kellnerin bringt den Kaffee.", "mot": {"mot": "Kellnerin", "genre": "die"}},
     "tr": {"fr": ["Voilà.", "La serveuse apporte le café."], "en": ["Here you are.", "The waitress brings the coffee."],
            "pt": ["Aqui está.", "A garçonete traz o café."], "de": ["Bitte schön.", "Die Kellnerin bringt den Kaffee."]}},
    {"id": "cuenta", "qui": "Tomas", "gens": ["Tomas", "Mark", "Javier"],
     "scene": "Later, at the same table, the cups are empty. Tomas raises his hand towards the waiter Javier, who is at the counter in the background, making the small writing gesture in the air that means 'the bill, please'.",
     "es": {"dit": "La cuenta, por favor.", "fait": "Tomás pide la cuenta.", "mot": {"mot": "cuenta", "genre": "la"}},
     "de": {"dit": "Die Rechnung, bitte.", "fait": "Tomás möchte die Rechnung.", "mot": {"mot": "Rechnung", "genre": "die"}},
     "tr": {"fr": ["L'addition, s'il vous plaît.", "Tomás demande l'addition."], "en": ["The bill, please.", "Tomás asks for the bill."],
            "pt": ["A conta, por favor.", "Tomás pede a conta."], "de": ["Die Rechnung, bitte.", "Tomás möchte die Rechnung."]}},
    {"id": "pagar", "qui": "Mark", "gens": ["Mark", "Ines", "Tomas"],
     "scene": "At the same table, the waitress Ines holds out a card payment terminal and Mark pays by holding his bank card against it, smiling; the empty cups are still on the table.",
     "es": {"dit": "¿Puedo pagar con tarjeta?", "fait": "Mark paga con tarjeta.", "mot": {"mot": "pagar", "cat": "verbe"}},
     "de": {"dit": "Kann ich mit Karte bezahlen?", "fait": "Mark bezahlt mit Karte.", "mot": {"mot": "bezahlen", "cat": "verbe"}},
     "tr": {"fr": ["Je peux payer par carte ?", "Mark paie par carte."], "en": ["Can I pay by card?", "Mark pays by card."],
            "pt": ["Posso pagar com cartão?", "Mark paga com cartão."], "de": ["Kann ich mit Karte bezahlen?", "Mark bezahlt mit Karte."]}},
    {"id": "propina", "qui": "Tomas", "gens": ["Tomas", "Javier", "Mark"],
     "scene": "Standing up to leave the same table, Tomas puts a few coins on the small saucer and gives them to the waiter Javier with a friendly nod; Javier smiles and thanks him; Mark puts on his jacket.",
     "es": {"dit": "Esto es para usted.", "fait": "Tomás deja una propina.", "mot": {"mot": "propina", "genre": "la"}},
     "de": {"dit": "Stimmt so.", "fait": "Tomás gibt Trinkgeld.", "mot": {"mot": "Trinkgeld", "genre": "das"}},
     "tr": {"fr": ["C'est pour vous.", "Tomás laisse un pourboire."], "en": ["This is for you.", "Tomás leaves a tip."],
            "pt": ["Isto é para o senhor.", "Tomás deixa uma gorjeta."], "de": ["Das ist für Sie.", "Tomás gibt Trinkgeld."]}},
]
# Qui est qui au cafe (la question « Javier es... ») : le mot du corpus pour chacun.
# Les reponses possibles a « Javier es ___. », au genre de la personne (jamais « Tomas es la camarera ») : le cuisinier
# (el cocinero, au corpus) sert de troisieme choix.
ROLES_CHOIX = {"es": {"m": ["el camarero", "el cliente", "el cocinero"], "f": ["la camarera", "la cliente", "la cocinera"]},
               "de": {"m": ["der Kellner", "der Gast", "der Koch"], "f": ["die Kellnerin", "der Gast", "die Köchin"]}}
ROLES = {"Javier": {"es": {"mot": "camarero", "genre": "el"}, "de": {"mot": "Kellner", "genre": "der"}},
         "Ines":   {"es": {"mot": "camarera", "genre": "la"}, "de": {"mot": "Kellnerin", "genre": "die"}},
         "Mark":   {"es": {"mot": "cliente", "genre": "el"}, "de": None},
         "Tomas":  {"es": {"mot": "cliente", "genre": "el"}, "de": None}}

# LA CARTE DU CAFE, dessinee dans la page (prix en euros, comme un cafe de Madrid et un cafe de Berlin). Les articles
# a l'accusatif allemand (einen Kaffee) ; es « un trozo de tarta » ; [un, deux] en fr/en/pt/de.
CARTE = {
    "es": [
        {"cle": "cafe", "mot": "café", "genre": "el", "carte": "Café", "un": "un café", "deux": "dos cafés", "prix": 150},
        {"cle": "te", "mot": "té", "genre": "el", "carte": "Té", "un": "un té", "deux": "dos tés", "prix": 160},
        {"cle": "zumo", "mot": "zumo", "genre": "el", "carte": "Zumo de naranja", "un": "un zumo", "deux": "dos zumos", "prix": 250},
        {"cle": "agua", "mot": "agua", "genre": "el", "carte": "Agua", "un": "un agua", "deux": "dos aguas", "prix": 120},
        {"cle": "cerveza", "mot": "cerveza", "genre": "la", "carte": "Cerveza", "un": "una cerveza", "deux": "dos cervezas", "prix": 280},
        {"cle": "tarta", "mot": "tarta", "genre": "la", "carte": "Tarta (trozo)", "un": "un trozo de tarta", "deux": "dos trozos de tarta", "prix": 350},
        {"cle": "bocadillo", "mot": "bocadillo", "genre": "el", "carte": "Bocadillo", "un": "un bocadillo", "deux": "dos bocadillos", "prix": 420},
        {"cle": "helado", "mot": "helado", "genre": "el", "carte": "Helado", "un": "un helado", "deux": "dos helados", "prix": 290},
    ],
    "de": [
        {"cle": "cafe", "mot": "Kaffee", "genre": "der", "carte": "Kaffee", "nom": "ein Kaffee", "un": "einen Kaffee", "deux": "zwei Kaffee", "prix": 280},
        {"cle": "te", "mot": "Tee", "genre": "der", "carte": "Tee", "nom": "ein Tee", "un": "einen Tee", "deux": "zwei Tee", "prix": 250},
        {"cle": "zumo", "mot": "Saft", "genre": "der", "carte": "Orangensaft", "nom": "ein Orangensaft", "un": "einen Orangensaft", "deux": "zwei Orangensäfte", "prix": 320},
        {"cle": "agua", "mot": "Wasser", "genre": "das", "carte": "Wasser", "nom": "ein Wasser", "un": "ein Wasser", "deux": "zwei Wasser", "prix": 220},
        {"cle": "cerveza", "mot": "Bier", "genre": "das", "carte": "Bier", "nom": "ein Bier", "un": "ein Bier", "deux": "zwei Bier", "prix": 360},
        {"cle": "tarta", "mot": "Kuchen", "genre": "der", "carte": "Kuchen (Stück)", "nom": "ein Stück Kuchen", "un": "ein Stück Kuchen", "deux": "zwei Stück Kuchen", "prix": 390},
        {"cle": "bocadillo", "mot": "Brezel", "genre": "die", "carte": "Brezel", "nom": "eine Brezel", "un": "eine Brezel", "deux": "zwei Brezeln", "prix": 190},
        {"cle": "helado", "mot": "Eis", "genre": "das", "carte": "Eis", "nom": "ein Eis", "un": "ein Eis", "deux": "zwei Eis", "prix": 310},
    ],
}
# fr / en / pt / de des articles de la carte (de : pour qui apprend l'espagnol), [un, deux]
TRAD_CARTE = {
    "cafe":      {"fr": ["un café", "deux cafés"], "en": ["a coffee", "two coffees"], "pt": ["um café", "dois cafés"], "de": ["einen Kaffee", "zwei Kaffee"]},
    "te":        {"fr": ["un thé", "deux thés"], "en": ["a tea", "two teas"], "pt": ["um chá", "dois chás"], "de": ["einen Tee", "zwei Tee"]},
    "zumo":      {"fr": ["un jus d'orange", "deux jus d'orange"], "en": ["an orange juice", "two orange juices"], "pt": ["um suco de laranja", "dois sucos de laranja"], "de": ["einen Orangensaft", "zwei Orangensäfte"]},
    "agua":      {"fr": ["une eau", "deux eaux"], "en": ["a water", "two waters"], "pt": ["uma água", "duas águas"], "de": ["ein Wasser", "zwei Wasser"]},
    "cerveza":   {"fr": ["une bière", "deux bières"], "en": ["a beer", "two beers"], "pt": ["uma cerveja", "duas cervejas"], "de": ["ein Bier", "zwei Bier"]},
    "tarta":     {"fr": ["une part de gâteau", "deux parts de gâteau"], "en": ["a piece of cake", "two pieces of cake"], "pt": ["um pedaço de bolo", "dois pedaços de bolo"], "de": ["ein Stück Kuchen", "zwei Stück Kuchen"]},
    "bocadillo": {"fr": ["un sandwich", "deux sandwichs"], "en": ["a sandwich", "two sandwiches"], "pt": ["um sanduíche", "dois sanduíches"], "de": ["ein belegtes Brötchen", "zwei belegte Brötchen"]},
    "helado":    {"fr": ["une glace", "deux glaces"], "en": ["an ice cream", "two ice creams"], "pt": ["um sorvete", "dois sorvetes"], "de": ["ein Eis", "zwei Eis"]},
}
# Allemand appris : la Brezel remplace le bocadillo (meme cle, d'autres mots) ; sa traduction :
TRAD_CARTE_DE = {"bocadillo": {"fr": ["un bretzel", "deux bretzels"], "en": ["a pretzel", "two pretzels"], "pt": ["um pretzel", "dois pretzels"]}}

# LA LISTE DE COURSES, dessinee dans la page : ce qui est ecrit (chiffres, unites abregees) et ce qui se dit.
# [ecrit, dit, unite (mot du corpus), produit, [trois fausses lectures]]. Les nombres se disent en lettres (regle du
# 28 oct.). Les fausses lectures, ecrites a la main, sont bien formees et toutes fausses pour la ligne ecrite : une
# autre unite, un autre nombre.
LISTE = {
    "es": [
        ["1 kg tomates", "un kilo de tomates", "kilo", "tomates", ["un litro de tomates", "dos kilos de tomates", "cien gramos de tomates"]],
        ["2 kg patatas", "dos kilos de patatas", "kilo", "patatas", ["doce kilos de patatas", "dos litros de patatas", "doscientos gramos de patatas"]],
        ["½ kg queso", "medio kilo de queso", "kilo", "queso", ["un kilo de queso", "medio litro de queso", "cinco kilos de queso"]],
        ["1 kg naranjas", "un kilo de naranjas", "kilo", "naranjas", ["once kilos de naranjas", "un litro de naranjas", "cien gramos de naranjas"]],
        ["100 g jamón", "cien gramos de jamón", "gramo", "jamon", ["cien kilos de jamón", "diez gramos de jamón", "mil gramos de jamón"]],
        ["200 g queso", "doscientos gramos de queso", "gramo", "queso", ["doce gramos de queso", "doscientos kilos de queso", "dos kilos de queso"]],
        ["250 g jamón", "doscientos cincuenta gramos de jamón", "gramo", "jamon", ["veinticinco gramos de jamón", "doscientos cincuenta kilos de jamón", "dos kilos y medio de jamón"]],
        ["500 g arroz", "quinientos gramos de arroz", "gramo", "arroz", ["cincuenta gramos de arroz", "quinientos kilos de arroz", "cinco kilos de arroz"]],
        ["1 l leche", "un litro de leche", "litro", "leche", ["un kilo de leche", "once litros de leche", "medio litro de leche"]],
        ["2 l agua", "dos litros de agua", "litro", "agua", ["doce litros de agua", "dos kilos de agua", "medio litro de agua"]],
        ["3 l leche", "tres litros de leche", "litro", "leche", ["trece litros de leche", "tres kilos de leche", "treinta litros de leche"]],
        ["½ l aceite", "medio litro de aceite", "litro", "aceite", ["un litro de aceite", "medio kilo de aceite", "cinco litros de aceite"]],
        ["150 g queso", "ciento cincuenta gramos de queso", "gramo", "queso", ["quince gramos de queso", "ciento cincuenta kilos de queso", "un kilo y medio de queso"]],
        ["300 g jamón", "trescientos gramos de jamón", "gramo", "jamon", ["treinta gramos de jamón", "trescientos kilos de jamón", "tres kilos de jamón"]],
        ["2 kg manzanas", "dos kilos de manzanas", "kilo", "manzanas", ["doce kilos de manzanas", "dos litros de manzanas", "doscientos gramos de manzanas"]],
    ],
    "de": [
        ["1 kg Tomaten", "ein Kilo Tomaten", "Kilo", "tomates", ["ein Liter Tomaten", "zwei Kilo Tomaten", "hundert Gramm Tomaten"]],
        ["2 kg Kartoffeln", "zwei Kilo Kartoffeln", "Kilo", "patatas", ["zwölf Kilo Kartoffeln", "zwei Liter Kartoffeln", "zweihundert Gramm Kartoffeln"]],
        ["½ kg Käse", "ein halbes Kilo Käse", "Kilo", "queso", ["ein Kilo Käse", "ein halber Liter Käse", "fünf Kilo Käse"]],
        ["1 kg Orangen", "ein Kilo Orangen", "Kilo", "naranjas", ["elf Kilo Orangen", "ein Liter Orangen", "hundert Gramm Orangen"]],
        ["100 g Schinken", "hundert Gramm Schinken", "Gramm", "jamon", ["hundert Kilo Schinken", "zehn Gramm Schinken", "tausend Gramm Schinken"]],
        ["200 g Käse", "zweihundert Gramm Käse", "Gramm", "queso", ["zwölf Gramm Käse", "zweihundert Kilo Käse", "zwei Kilo Käse"]],
        ["250 g Schinken", "zweihundertfünfzig Gramm Schinken", "Gramm", "jamon", ["fünfundzwanzig Gramm Schinken", "zweihundertfünfzig Kilo Schinken", "zweieinhalb Kilo Schinken"]],
        ["500 g Reis", "fünfhundert Gramm Reis", "Gramm", "arroz", ["fünfzig Gramm Reis", "fünfhundert Kilo Reis", "fünf Kilo Reis"]],
        ["1 l Milch", "ein Liter Milch", "Liter", "leche", ["ein Kilo Milch", "elf Liter Milch", "ein halber Liter Milch"]],
        ["2 l Wasser", "zwei Liter Wasser", "Liter", "agua", ["zwölf Liter Wasser", "zwei Kilo Wasser", "ein halber Liter Wasser"]],
        ["3 l Milch", "drei Liter Milch", "Liter", "leche", ["dreizehn Liter Milch", "drei Kilo Milch", "dreißig Liter Milch"]],
        ["1 Pfund Tomaten", "ein Pfund Tomaten", "Pfund", "tomates", ["ein Kilo Tomaten", "eine Packung Tomaten", "ein Liter Tomaten"]],
        ["1 Packung Nudeln", "eine Packung Nudeln", "Packung", "nudeln", ["ein Liter Nudeln", "eine Flasche Nudeln", "eine Dose Nudeln"]],
        ["1 Packung Reis", "eine Packung Reis", "Packung", "arroz", ["ein Liter Reis", "eine Flasche Reis", "eine Tasse Reis"]],
        ["1 Packung Kaffee", "eine Packung Kaffee", "Packung", "cafe", ["ein Liter Kaffee", "eine Flasche Kaffee", "zehn Packungen Kaffee"]],
        ["2 Packungen Kekse", "zwei Packungen Kekse", "Packung", "galletas", ["zwölf Packungen Kekse", "zwei Liter Kekse", "eine Packung Kekse"]],
        ["1 Pfund Kartoffeln", "ein Pfund Kartoffeln", "Pfund", "patatas", ["ein Kilo Kartoffeln", "eine Packung Kartoffeln", "ein Liter Kartoffeln"]],
        ["2 Pfund Äpfel", "zwei Pfund Äpfel", "Pfund", "manzanas", ["zwölf Pfund Äpfel", "zwei Kilo Äpfel", "zwei Liter Äpfel"]],
        ["150 g Käse", "hundertfünfzig Gramm Käse", "Gramm", "queso", ["fünfzehn Gramm Käse", "hundertfünfzig Kilo Käse", "eineinhalb Kilo Käse"]],
    ],
}
# la traduction de l'unite ecrite (fr / en / pt) quand elle n'est pas un symbole (kg, g, l)
UNITES = {"Pfund": {"fr": "livre de", "en": "pound of", "pt": "libra de"}, "Packung": {"fr": "paquet de", "en": "packet of", "pt": "pacote de"}}
PRODUITS = {"tomates": {"fr": "tomates", "en": "tomatoes", "pt": "tomates", "de": "Tomaten"},
            "patatas": {"fr": "pommes de terre", "en": "potatoes", "pt": "batatas", "de": "Kartoffeln"},
            "queso": {"fr": "fromage", "en": "cheese", "pt": "queijo", "de": "Käse"},
            "naranjas": {"fr": "oranges", "en": "oranges", "pt": "laranjas", "de": "Orangen"},
            "jamon": {"fr": "jambon", "en": "ham", "pt": "presunto", "de": "Schinken"},
            "arroz": {"fr": "riz", "en": "rice", "pt": "arroz", "de": "Reis"},
            "leche": {"fr": "lait", "en": "milk", "pt": "leite", "de": "Milch"},
            "agua": {"fr": "eau", "en": "water", "pt": "água", "de": "Wasser"},
            "aceite": {"fr": "huile", "en": "oil", "pt": "óleo", "de": "Öl"},
            "nudeln": {"fr": "pâtes", "en": "pasta", "pt": "macarrão", "de": "Nudeln"},
            "manzanas": {"fr": "pommes", "en": "apples", "pt": "maçãs", "de": "Äpfel"},
            "cafe": {"fr": "café", "en": "coffee", "pt": "café", "de": "Kaffee"},
            "galletas": {"fr": "biscuits", "en": "cookies", "pt": "biscoitos", "de": "Kekse"}}

# Les mots que l'Amerique latine dit autrement (espanol/datos/variantes.json) : affiches, jamais envoyes (la carte du
# corpus reste zumo, camarero, bocadillo, patata).
LATAM = {"zumo": "jugo", "zumos": "jugos", "Zumo": "Jugo", "camarero": "mesero", "camarera": "mesera", "bocadillo": "sándwich",
         "bocadillos": "sándwiches", "patatas": "papas", "Bocadillo": "Sándwich"}

# Les sens (visuel/THEMES-ILLUSTRES.md, « Un mot a deux sens ») : rico est « delicieux » ici, pas « riche ».
SENS = {"es": {"rico": "délicieux"}, "de": {}}


# ---------- les phrases de la langue apprise (la page applique les memes regles) ----------
def nom(p):
    return NOMS.get(p, p)


def es_gusta(p, cle, r):
    """« A Carmen no le gusta el limón. » / « A Anna le gustan las fresas. » / « A Lucas no le gusta nada el pescado. »"""
    a = ALIMENTS[cle]["es"]
    n = "n" if a.get("pl") else ""
    verbe = {"encanta": "le encanta" + n, "gusta": "le gusta" + n, "no": "no le gusta" + n, "nada": "no le gusta" + n + " nada"}[r]
    return "A %s %s %s." % (nom(p), verbe, a["vu"])


def de_mag(p, cle, r):
    """« Carmen mag keine Zitronen. » / « Ben liebt Kuchen. » ; None si mögen ne dit pas l'image (la soupe trop salee)."""
    a = ALIMENTS[cle]["de"]
    if not a["gen"]:
        return None
    if r == "encanta":
        return "%s liebt %s." % (nom(p), a["gen"])
    if r == "gusta":
        return "%s mag %s." % (nom(p), a["gen"])
    return "%s mag %s%s %s." % (nom(p), "überhaupt " if r == "nada" else "", a["kein"], a["gen"])


def de_schmeckt(p, cle, r):
    """« Die Erdbeeren schmecken Anna. » / « Die Suppe schmeckt Javier nicht. »"""
    a = ALIMENTS[cle]["de"]
    v = "schmecken" if a.get("pl") else "schmeckt"
    neg = {"encanta": "", "gusta": "", "no": " nicht", "nada": " überhaupt nicht"}[r]
    s = a["nom"]
    return "%s %s %s%s." % (s[0].upper() + s[1:], v, nom(p), neg)


def es_saveur(cle):
    """« El limón es ácido. » / « Las fresas son dulces. » / « La sopa está salada. »"""
    a, al = ALIMENTS[cle]["es"], ALIMENTS[cle]
    if not al["saveur"]:
        return None
    f = SAVEURS[al["saveur"]]["es"][(2 if a.get("pl") else 0) + (1 if a["genre"] == "la" else 0)]
    verbe = ("están" if a.get("pl") else "está") if al.get("estar") else ("son" if a.get("pl") else "es")
    s = a.get("court", a["vu"])          # « La comida es picante. », jamais « la comida picante es picante »
    return "%s %s %s." % (s[0].upper() + s[1:], verbe, f)


def de_saveur(cle):
    a, al = ALIMENTS[cle]["de"], ALIMENTS[cle]
    if not al["saveur"]:
        return None
    s = a.get("court", a["nom"]) if cle != "picante" else "das Essen"
    return "%s %s %s." % (s[0].upper() + s[1:], "sind" if a.get("pl") else "ist", SAVEURS[al["saveur"]]["de"])


def es_dit(cle, r):
    a, al = ALIMENTS[cle]["es"], ALIMENTS[cle]
    if r in ("encanta", "gusta"):
        return "¡Qué rico!"
    if r == "nada":
        return "¡Está asqueroso!"
    if al["saveur"]:
        f = SAVEURS[al["saveur"]]["es"][(2 if a.get("pl") else 0) + (1 if a["genre"] == "la" else 0)]
        return "¡%s demasiado %s!" % ("Están" if a.get("pl") else "Está", f)
    return "No me gusta%s %s." % ("n" if a.get("pl") else "", a["vu"])


def de_dit(cle, r):
    a, al = ALIMENTS[cle]["de"], ALIMENTS[cle]
    if r in ("encanta", "gusta"):
        return "Lecker!"
    if r == "nada":
        return "Igitt, das ist eklig!"
    if al["saveur"]:
        return "Das ist zu %s!" % SAVEURS[al["saveur"]]["de"]
    return "Ich mag %s %s." % (a["kein"], a["gen"])


def quantite(langue, cont, contenu):
    c = CONTENANTS[cont][langue]["art"]
    d = CONTENUS[contenu][langue]["dit"]
    return c + " " + d


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def images():
    """{nom: (sources, prompt, format, depart)} -- depart : l'image deja faite qui sert de decor (le cafe)."""
    MEME = ("The same person as in the reference picture: exactly the same face, the same age, the same hair, the same skin, "
            "the same glasses or beard if any, and the same clothes. ")
    PORTRAIT = (" A photorealistic head-and-shoulders portrait, from the top of the head to the middle of the chest, facing the "
                "camera, centred, the food clearly visible in the picture. Plain light grey studio background with even soft "
                "light, nothing else, no text, no logos. Natural skin texture, no retouching. What the person does: ")
    NATURE = ("A photorealistic still-life photograph on a light wooden table, plain light grey studio background, soft even "
              "light, seen slightly from above, the object centred and entirely visible, nothing else on the table. "
              "Absolutely no text, no letters, no numbers, no logos anywhere. ")
    CAFE_ = ("A photorealistic photograph in a small, bright, simple neighbourhood cafe with wooden tables, white walls, a counter "
             "in the background and a big window with daylight; natural colours, no text, no logos, no captions, no writing on "
             "the menus or the walls. The people are the ones in the reference pictures, with exactly the same faces, hair and "
             "clothes; everybody's face and gesture are easy to read. ")
    out = {}
    for p, cle, r, quoi in DEGUSTATIONS:
        out["gout-" + p] = ([p], MEME + PORTRAIT + quoi + " The expression: " + REACTIONS[r], "1:1", None)
    for cont, contenu, quoi in QUANTITES:
        out["qte-%s-%s" % (cont, contenu)] = ([], NATURE + quoi, "4:3", None)
    avant = None
    for m in CAFE:
        roles = " Javier is the waiter: a white shirt and a black apron." if "Javier" in m["gens"] else ""
        roles += " Ines is the waitress: a white shirt and a black apron." if "Ines" in m["gens"] else ""
        decor = " The same cafe, the same table, the same light as in the last reference picture." if avant else ""
        out["cafe-" + m["id"]] = (m["gens"], CAFE_ + roles + decor + " " + m["scene"], "4:3", avant)
        avant = "cafe-" + m["id"]
    return out


def ecrire_json():
    """manger.json : la donnee de la page (questions et decouverte), et les phrases de la decouverte avec l'identifiant
    de leur son (sha1 du texte, comme audio/manifest.py), pour les inventaires des voix."""
    gouts = [{"id": "gout-" + p, "p": p, "a": cle, "r": r} for p, cle, r, _ in DEGUSTATIONS]
    qtes = [{"id": "qte-%s-%s" % (c, d), "c": c, "d": d} for c, d, _ in QUANTITES]
    dec = {}
    for langue in ("es", "latam", "de"):
        L = "de" if langue == "de" else "es"
        dec[langue] = {}
        for g in gouts:
            t = (de_mag(g["p"], g["a"], g["r"]) or de_schmeckt(g["p"], g["a"], g["r"])) if L == "de" else es_gusta(g["p"], g["a"], g["r"])
            dec[langue][g["id"]] = {"texte": t, "son": identifiant(t)}
        for q in qtes:
            t = quantite(L, q["c"], q["d"])
            t = t[0].upper() + t[1:] + "."
            dec[langue][q["id"]] = {"texte": t, "son": identifiant(t)}
        for m in CAFE:
            t = m[L]["dit"]
            if langue == "latam":
                t = " ".join(LATAM.get(w, w) for w in t.split(" "))
            dec[langue]["cafe-" + m["id"]] = {"texte": t, "son": identifiant(t)}
    d = {"sexe": SEXE, "noms": NOMS, "enfants": sorted(ENFANTS),
         "aliments": ALIMENTS, "tradAliments": TRAD_ALIMENTS, "saveurs": SAVEURS, "gouts": gouts,
         "contenants": CONTENANTS, "voisinsContenants": VOISINS_CONTENANTS, "contenus": CONTENUS,
         "tradContenants": TRAD_CONTENANTS, "quantites": qtes,
         "cafe": [{k: v for k, v in m.items() if k != "scene"} for m in CAFE], "roles": ROLES, "rolesChoix": ROLES_CHOIX,
         "carte": CARTE, "tradCarte": TRAD_CARTE, "tradCarteDe": TRAD_CARTE_DE,
         "liste": LISTE, "unites": UNITES, "produits": PRODUITS, "latam": LATAM, "sens": SENS,
         "decouverte": dec}
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    os.makedirs(SORTIE, exist_ok=True)
    io.open(os.path.join(SORTIE, "manger.json"), "w", encoding="utf-8", newline="\n").write(texte)


def mots_du_theme():
    """Les mots que la page enseigne, a la forme du corpus, par langue : (mot, genre ou cat). La page les recalcule de
    la meme facon (motsDuTheme) ; ici, pour les gloses et le controle du corpus."""
    out = {"es": [], "de": []}
    for L in ("es", "de"):
        for cle, a in ALIMENTS.items():
            out[L].append((a[L]["mot"], a[L]["genre"]))
        for s in SAVEURS.values():
            out[L].append((s["es"][0] if L == "es" else s["de"], "adjectif"))
        out[L] += [("rico", "adjectif"), ("asqueroso", "adjectif"), ("gustar", "verbe"), ("encantar", "verbe")] if L == "es" else \
                  [("lecker", "adjectif"), ("eklig", "adjectif"), ("mögen", "verbe"), ("schmecken", "verbe"), ("lieben", "verbe")]
        out[L] += [("probar", "verbe")] if L == "es" else [("probieren", "verbe")]
        for c in CONTENANTS.values():
            if c[L]["mot"]:
                out[L].append((c[L]["mot"], c[L]["genre"]))
        for c in CONTENUS.values():
            out[L].append((c[L]["mot"], c[L]["genre"]))
        for m in CAFE:
            w = m[L]["mot"]
            out[L].append((w["mot"], w.get("genre") or w.get("cat")))
        for r in ROLES.values():
            if r[L]:
                out[L].append((r[L]["mot"], r[L]["genre"]))
        for it in CARTE[L]:
            out[L].append((it["mot"], it["genre"]))
        out[L] += [(u, "el" if L == "es" else ("das" if u in ("Kilo", "Gramm", "Pfund") else ("der" if u == "Liter" else "die")))
                   for u in (["kilo", "gramo", "litro"] if L == "es" else ["Kilo", "Gramm", "Liter", "Pfund", "Packung"])]
        out[L] = list(dict.fromkeys(out[L]))
    return out


def ecrire_gloses():
    """La traduction des mots du theme tiree du CORPUS (relu), pour les langues d'interface ou la page ne traduit pas la
    phrase entiere (ar, tr, uk, fa, pl, ru) : « el limón — ليمون ». Meme forme que emociones/gloses.json. Les mots
    absents du corpus sont listes (ils attendent d'y entrer) ; DERIVE : le refaire."""
    def lire(p):
        return json.load(io.open(os.path.join(RACINE, p), encoding="utf-8"))
    LDE = {"fr": "traduction", "en": "traduction_en", "tr": "traduction_tr", "uk": "traduction_uk", "fa": "traduction_fa",
           "ar": "traduction_ar", "pt": "traduction_pt", "pl": "traduction_pl", "ru": "traduction_ru"}
    LES = {"fr": "traduction", "en": "traduction_en", "pt": "traduction_pt", "ar": "traduction_ar", "de": "traduction_de"}
    plats = lambda p: [e for v in lire(p).values() if isinstance(v, list) for e in v if isinstance(e, dict)]
    noms = lambda p: [m for t in lire(p)["themes"] for m in t["mots"]]
    sources = {"de": (plats("adjectif.json"), plats("verbe.json"), noms("themes.json"), LDE),
               "es": (plats("espanol/datos/adjetivos.json"), plats("espanol/datos/verbos.json"), noms("espanol/datos/temas.json"), LES)}
    out, manque = {"de": {}, "es": {}}, {"de": [], "es": []}
    voulus = mots_du_theme()
    for L, (adjs, verbes, ns, champs) in sources.items():
        for mot, g in voulus[L]:
            sens = SENS[L].get(mot)
            if g == "adjectif":
                cand = [e for e in adjs if e.get("mot") == mot]
                cle = mot
            elif g == "verbe":
                cand = [e for e in verbes if (e.get("infinitif") or e.get("mot")) == mot]
                cle = mot
            else:
                cand = [m for m in ns if m.get("mot") == mot and m.get("genre") == g]
                cle = g + " " + mot
            if sens:
                cand = [e for e in cand if e.get("traduction") == sens] or cand
            if not cand:
                manque[L].append(cle)
                continue
            out[L][cle] = {l: cand[0][c] for l, c in champs.items() if cand[0].get(c)}
    io.open(os.path.join(SORTIE, "gloses.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return manque


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    tout = images()
    noms_ = [a for a in sys.argv[1:] if not a.startswith("--")] or list(tout)
    inconnus = [n for n in noms_ if n not in tout]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    for p, cle, r, _ in DEGUSTATIONS:
        if p in ENFANTS and r in ("no", "nada"):
            sys.exit("  %s : un enfant ne fait qu'aimer (filtre de fal)" % p)
    ecrire_json()
    manque = ecrire_gloses()
    for L in manque:
        if manque[L]:
            print("  absents du corpus (%s) : %s" % (L, ", ".join(manque[L])))
    if "--json" in sys.argv:
        return
    if refaire and not montrer:
        for n in noms_:
            png = os.path.join(DOSSIER, n + ".png")
            if os.path.exists(png):
                k = 1
                while os.path.exists(os.path.join(DOSSIER, "%s-rate%d.png" % (n, k))):
                    k += 1
                os.replace(png, os.path.join(DOSSIER, "%s-rate%d.png" % (n, k)))
    a_faire = [n for n in noms_ if not os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if montrer:
        for n in a_faire:
            print("\n  %s %s\n  %s" % (n, tout[n][0], tout[n][1]))
        return
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    if not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    os.makedirs(DOSSIER, exist_ok=True)
    depots = {}

    def deposer(chemin):
        if chemin not in depots:
            depots[chemin] = O.deposer(chemin, "image/png", cle)[0]
        return depots[chemin]
    for nom_ in a_faire:
        gens, prompt, fmt, depart = tout[nom_]
        print("\n  %s\n  %s" % (nom_, prompt))
        refs = [deposer(SOURCES[g]) for g in gens]
        if depart:
            png = os.path.join(DOSSIER, depart + ".png")
            if not os.path.exists(png):
                print("  ATTENTE", nom_, ": le decor", depart, "n'est pas encore fait")
                continue
            refs.append(deposer(png))
        modele = EDIT if refs else T2I
        corps = {"prompt": prompt, "aspect_ratio": fmt, "resolution": "2K", "output_format": "png", "num_images": 1}
        if refs:
            corps["image_urls"] = refs
        soum = O._json("https://queue.fal.run/" + modele, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            print("  ECHEC", nom_, err)
            io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
                "%s\t%s\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom_, soum.get("request_id"), str(err).replace("\n", " ")))
            continue
        sortie = os.path.join(DOSSIER, nom_ + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
            "%s\t%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom_, soum.get("request_id"), PRIX))
        io.open(os.path.join(DOSSIER, nom_ + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": modele, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "sources": [SOURCES[g] for g in gens] + ([depart] if depart else []), "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
