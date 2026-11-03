# -*- coding: utf-8 -*-
"""La meteo et les saisons, theme illustre de la vague 2 (3 nov. 2026, Jacques : « Plutot 5 autres themes »).
Quel temps il fait (hace calor, llueve, esta nublado ; es ist warm, es regnet, es ist bewoelkt), les degres, les
saisons et ce qu'on y fait, les mois rattaches a leur saison. ET C'EST FACTURE : 0,15 $ l'image, chez fal ;
14 images, 2,50 $ au plus pour le theme (le solde fal est partage entre cinq themes et la video du DTZ).

    python visuel/meteo/meteo.py --json            # meteo.json seul, gratuit
    python visuel/meteo/meteo.py --montrer         # les prompts seuls, gratuit
    python visuel/meteo/meteo.py --essai           # la planche d'essai : 6 images (0,90 $), accord de Jacques
    python visuel/meteo/meteo.py                   # celles qui manquent (0,15 $ chacune)
    python visuel/meteo/meteo.py regen             # celles-la seulement
    python visuel/meteo/meteo.py --refaire regen   # l'ancienne passe en <nom>-rate<k>.png

CE QUI EXISTAIT DEJA ET QU'ON NE DOUBLE PAS : la scene de l'hiver (Anna et son bonhomme de neige, « mir ist kalt »
en B1) et le theme Vetements (s'habiller selon la meteo) ; ici, aucune question sur un vetement, pas de bonhomme de
neige. Les Reperes (jours, mois, nombres) : les mois ne sont demandes que rattaches a leur saison.

LES IMAGES : UNE place de Berlin (Prenzlauer Berg), puis des RETOUCHES de la premiere -- meme cadrage, memes
maisons, meme tilleul, seul le temps change (la methode de « Ou est le chat ? ») ; et six moments de saison avec
nos personnes (Anna, Ben, Mia), par retouche de leurs images de reference. Pas d'enfant triste (le filtre de fal),
pas d'enfant en maillot : c'est Anna qui nage.
Le thermometre, les mois et les pictogrammes sont DESSINES par la page : gratuits.
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/meteo/img/ ; puis web.py (les webp).
Toute phrase de la page vient d'ici (-> visuel/prototype/meteo/meteo.json) : aucune n'est ecrite dans la page.
"""
import hashlib, io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))

TEXTE, EDIT, PRIX, PLAFOND = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15, 2.50
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "meteo", "img")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
PERSONNES = {"Anna": FAMILLE + "/Anna-quotidien.png", "Ben": FAMILLE + "/Ben.png", "Mia": FAMILLE + "/Mia.png"}

# ---------------------------------------------------------------------------------------------------------------
# LES FAITS : ce qu'une image peut montrer du temps. Chaque fait a ses phrases dans chaque langue, et chaque phrase
# le mot du corpus qu'elle fait travailler (la cle de MOTS). En allemand comme en espagnol, la phrase la plus
# courante, jamais un calque du francais : hace sol / esta soleado, die Sonne scheint / es ist sonnig.
FAITS = {
    "sol":      {"es": [("Hace sol.", "sol"), ("Está soleado.", "soleado")], "de": [("Die Sonne scheint.", "Sonne"), ("Es ist sonnig.", "sonnig")]},
    "calor":    {"es": [("Hace calor.", "calor")], "de": [("Es ist heiß.", "heiß")]},
    "frio":     {"es": [("Hace frío.", "frío")], "de": [("Es ist kalt.", "kalt")]},
    "fresco":   {"es": [("Hace fresco.", "fresco")], "de": [("Es ist kühl.", "kühl")]},
    "lluvia":   {"es": [("Llueve.", "llover")], "de": [("Es regnet.", "regnen")]},
    "nieve":    {"es": [("Nieva.", "nevar")], "de": [("Es schneit.", "schneien")]},
    "nublado":  {"es": [("Está nublado.", "nublado")], "de": [("Es ist bewölkt.", "bewölkt")]},
    "viento":   {"es": [("Hace viento.", "viento")], "de": [("Es ist windig.", "windig")]},
    "niebla":   {"es": [("Hay niebla.", "niebla")], "de": [("Es ist neblig.", "neblig")]},
    "tormenta": {"es": [("Hay tormenta.", "tormenta")], "de": [("Es gibt ein Gewitter.", "Gewitter")]},
    "buen":     {"es": [("Hace buen tiempo.", "tiempo")], "de": [("Das Wetter ist schön.", "Wetter")]},
    "malo":     {"es": [("Hace mal tiempo.", "tiempo")], "de": [("Das Wetter ist schlecht.", "Wetter")]},
}
# leur traduction : (fr, en, pt, de pour qui apprend l'espagnol) ; l'allemand prend (fr, en, pt)
TRAD_FAITS = {
    "Hace sol.": ("Il y a du soleil.", "It's sunny.", "Está fazendo sol.", "Die Sonne scheint."),
    "Está soleado.": ("C'est ensoleillé.", "It's sunny.", "Está ensolarado.", "Es ist sonnig."),
    "Hace calor.": ("Il fait chaud.", "It's hot.", "Está calor.", "Es ist heiß."),
    "Hace frío.": ("Il fait froid.", "It's cold.", "Está frio.", "Es ist kalt."),
    "Hace fresco.": ("Il fait frais.", "It's cool.", "Está fresco.", "Es ist kühl."),
    "Llueve.": ("Il pleut.", "It's raining.", "Está chovendo.", "Es regnet."),
    "Nieva.": ("Il neige.", "It's snowing.", "Está nevando.", "Es schneit."),
    "Está nublado.": ("Le ciel est couvert.", "It's cloudy.", "Está nublado.", "Es ist bewölkt."),
    "Hace viento.": ("Il y a du vent.", "It's windy.", "Está ventando.", "Es ist windig."),
    "Hay niebla.": ("Il y a du brouillard.", "It's foggy.", "Tem neblina.", "Es ist neblig."),
    "Hay tormenta.": ("Il y a de l'orage.", "There's a thunderstorm.", "Tem tempestade.", "Es gibt ein Gewitter."),
    "Hace buen tiempo.": ("Il fait beau.", "The weather is nice.", "O tempo está bom.", "Das Wetter ist schön."),
    "Hace mal tiempo.": ("Il fait mauvais.", "The weather is bad.", "O tempo está ruim.", "Das Wetter ist schlecht."),
    "Die Sonne scheint.": ("Le soleil brille.", "The sun is shining.", "O sol está brilhando."),
    "Es ist sonnig.": ("C'est ensoleillé.", "It's sunny.", "Está ensolarado."),
    "Es ist heiß.": ("Il fait très chaud.", "It's hot.", "Está muito quente."),
    "Es ist kalt.": ("Il fait froid.", "It's cold.", "Está frio."),
    "Es ist kühl.": ("Il fait frais.", "It's cool.", "Está fresco."),
    "Es regnet.": ("Il pleut.", "It's raining.", "Está chovendo."),
    "Es schneit.": ("Il neige.", "It's snowing.", "Está nevando."),
    "Es ist bewölkt.": ("Le ciel est couvert.", "It's cloudy.", "Está nublado."),
    "Es ist windig.": ("Il y a du vent.", "It's windy.", "Está ventando."),
    "Es ist neblig.": ("Il y a du brouillard.", "It's foggy.", "Tem neblina."),
    "Es gibt ein Gewitter.": ("Il y a un orage.", "There's a thunderstorm.", "Tem uma tempestade."),
    "Das Wetter ist schön.": ("Il fait beau.", "The weather is nice.", "O tempo está bom."),
    "Das Wetter ist schlecht.": ("Il fait mauvais.", "The weather is bad.", "O tempo está ruim."),
}

# LES MOTS DU THEME, a la forme du corpus (themes.json, adjectif.json, verbe.json ; espanol/datos/temas.json,
# adjetivos.json, verbos.json) : le script s'arrete si l'un d'eux manque. genre pour un nom, cat sinon.
MOTS = {
    "es": {"tiempo": "el", "sol": "el", "calor": "el", "viento": "el", "niebla": "la", "tormenta": "la", "lluvia": "la",
           "nieve": "la", "nube": "la", "grado": "el", "primavera": "la", "verano": "el", "otoño": "el", "invierno": "el",
           "enero": "el", "febrero": "el", "abril": "el", "mayo": "el", "julio": "el", "agosto": "el", "octubre": "el",
           "noviembre": "el", "parque": "el", "lago": "el", "helado": "el", "hoja": "la",
           "frío": "adjectif", "fresco": "adjectif", "nublado": "adjectif", "soleado": "adjectif",
           "llover": "verbe", "nevar": "verbe", "nadar": "verbe", "pasear": "verbe", "comer": "verbe", "recoger": "verbe",
           "jugar": "verbe", "leer": "verbe"},
    "de": {"Wetter": "das", "Sonne": "die", "Regen": "der", "Schnee": "der", "Wind": "der", "Wolke": "die", "Nebel": "der",
           "Gewitter": "das", "Grad": "der", "Frühling": "der", "Sommer": "der", "Herbst": "der", "Winter": "der",
           "Januar": "der", "Februar": "der", "April": "der", "Mai": "der", "Juli": "der", "August": "der", "Oktober": "der",
           "November": "der", "Park": "der", "See": "der", "Eis": "das", "Blatt": "das",
           "heiß": "adjectif", "warm": "adjectif", "kühl": "adjectif", "kalt": "adjectif", "sonnig": "adjectif",
           "bewölkt": "adjectif", "windig": "adjectif", "neblig": "adjectif",
           "regnen": "verbe", "schneien": "verbe", "schwimmen": "verbe", "essen": "verbe", "sammeln": "verbe",
           "spielen": "verbe", "lesen": "verbe", "spazieren": "verbe"},
}

# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES. vrais : les faits que l'image montre sans discussion ; douteux : ceux qu'elle ne tranche pas (un jour
# de pluie est-il frais ? la neige est-elle du mauvais temps ?) -- jamais demandes, jamais pris pour leurre. Tout
# autre fait est clairement FAUX pour elle, et seul un fait faux sert de leurre ou de faux d'un « vrai ou faux ».
# temp : les degres du thermometre dessine a cote (decouverte) ; saison : None quand l'image ne la dit pas.
GARDE = ("Exactly the same square as in the reference picture: the same old buildings with the same pastel colours, "
         "the same balconies and windows, the same big linden tree with the round wooden bench around its trunk, the "
         "same little cafe on the right, the same green street lamp and bicycle rack on the left, the same camera "
         "position, the same lens and the same framing. Only the season, the weather and the light change, as "
         "described: ")
PHOTO = (" A photorealistic photograph, natural colours, no text, no letters, no logos, no signs with writing, no "
         "watermark. Landscape format 4:3.")
MEME = ("The people are exactly the same persons as in the reference pictures: the same faces, the same ages, the "
        "same hair, the same skin. ")
PLACE = ("A small, quiet cobbled square in an old residential neighbourhood of Berlin (Prenzlauer Berg): five-storey "
         "old apartment buildings in pastel colours (pale yellow, light green, soft pink) with balconies and tall "
         "windows all around; in the middle a big old linden tree with a round wooden bench around its trunk; on the "
         "right a small cafe with three round outdoor tables, chairs and two large white parasols; on the left an old "
         "dark green cast-iron street lamp and a bicycle rack with two bicycles. Wide view from a pedestrian's eye "
         "level, the sky fills the upper third of the picture. ")
IMAGES = {
    # la place, sept fois : la premiere est la base, les autres en sont des retouches
    "sommer":    {"saison": "verano", "temp": 31, "vrais": ["calor", "sol", "buen"], "douteux": [],
        "prompt": PLACE + "HIGH SUMMER, a very hot afternoon: a deep blue sky without a single cloud, blazing sunshine, "
                  "hard short shadows on the cobblestones, the linden tree dark green and full of leaves; a few people sit "
                  "at the cafe under the open parasols with cold drinks and fan themselves; a man walks by in the heat."},
    "fruehling": {"saison": "primavera", "temp": 16, "vrais": ["buen", "sol"], "douteux": ["fresco", "viento"], "source": "sommer",
        "prompt": "SPRING, a mild sunny morning: a bright blue sky with a few small white clouds, soft sunshine; the linden "
                  "tree has fresh, light-green young leaves; window boxes on the balconies and two big pots by the cafe are "
                  "full of red and yellow tulips; a small tree in pink blossom next to the cafe; the parasols are closed; "
                  "two people drink coffee outside, a woman walks by. It is clearly spring."},
    "herbst":    {"saison": "otono", "temp": 11, "vrais": ["viento", "fresco"], "douteux": ["sol", "nublado", "buen", "malo", "frio"], "source": "sommer",
        "prompt": "AUTUMN, a cool and VERY WINDY day: the linden tree has yellow and orange leaves, and many leaves fly "
                  "through the air across the square and lie on the cobblestones; fast-moving white and grey clouds with "
                  "patches of blue; the branches bend in the wind; a woman holds on to her hat, a man leans into the wind; "
                  "the parasols are folded and the cafe chairs are stacked. The wind must be obvious at first sight."},
    "winter":    {"saison": "invierno", "temp": -2, "vrais": ["nieve", "frio"], "douteux": ["nublado", "malo", "viento", "fresco"], "source": "sommer",
        "prompt": "WINTER, IT IS SNOWING: big snowflakes are falling everywhere, the sky is white-grey, a thick layer of "
                  "fresh snow covers the cobblestones, the bench, the bicycles and the roofs; the linden tree is bare, its "
                  "branches white with snow; the cafe terrace is empty, the tables covered with snow, the parasols gone; "
                  "the street lamp is lit; two people walk carefully through the snow. No snowman, no sledge."},
    "regen":     {"saison": None, "temp": 12, "vrais": ["lluvia", "nublado", "malo"], "douteux": ["fresco", "viento", "frio"], "source": "sommer",
        "prompt": "A RAINY day: heavy rain is falling, clearly visible streaks of rain, a dark grey sky, the cobblestones "
                  "wet and shiny with big puddles in which the houses are reflected; three people walk under umbrellas; the "
                  "cafe terrace is empty, the chairs wet, the parasols closed; the linden tree is green."},
    "bewoelkt":  {"saison": None, "temp": 14, "vrais": ["nublado"], "douteux": ["fresco", "malo", "frio", "viento", "buen"], "source": "sommer",
        "prompt": "An OVERCAST day: the whole sky is covered by thick, flat grey clouds, no sun at all, no shadows, dull "
                  "flat light; it is NOT raining and the ground is completely dry; no puddles, no umbrellas; the linden "
                  "tree is green; a few people walk by; the parasols are closed."},
    "nebel":     {"saison": None, "temp": 5, "vrais": ["niebla"], "douteux": ["frio", "fresco", "malo", "nublado"], "source": "sommer",
        "prompt": "A very FOGGY morning: thick white fog fills the square, the buildings at the back are only pale grey "
                  "shapes, barely visible; only the linden tree, the bench and the street lamp in the foreground are "
                  "clear; the street lamp is lit; soft white light; nobody at the cafe; one person walks into the fog."},
    "gewitter":  {"saison": None, "temp": 22, "vrais": ["tormenta", "lluvia", "malo", "nublado"], "douteux": ["viento", "calor", "fresco"], "source": "sommer",
        "prompt": "A summer THUNDERSTORM in the late afternoon: a very dark, blue-black sky full of heavy storm clouds, ONE "
                  "bright bolt of lightning over the roofs, pouring rain, the linden tree green and shaking; the parasols "
                  "are closed; two people run for shelter under a balcony; the lit windows glow yellow."},
    # les moments de saison, avec nos personnes ; act : la phrase de ACTIVITES qu'ils illustrent
    "park":      {"saison": "primavera", "temp": 17, "act": "park", "vrais": ["sol", "buen"], "douteux": ["fresco", "viento", "calor"], "source": ["Anna", "Ben", "Mia"],
        "prompt": "In a Berlin park in SPRING: trees in pink and white blossom, fresh green grass with daisies, tulips, a "
                  "mild sunny day, a blue sky with a few small white clouds. The woman of the first picture walks on a "
                  "path, smiling, holding the hand of the girl of the third picture; the boy of the second picture walks "
                  "happily beside them. They wear light spring jackets. Seen from the front, the three faces clearly visible."},
    "see":       {"saison": "verano", "temp": 30, "act": "see", "vrais": ["sol", "calor", "buen"], "douteux": [], "source": ["Anna"],
        "prompt": "On a very hot, sunny summer day at a lake near Berlin, with green trees around and a cloudless blue "
                  "sky: the woman of the reference picture SWIMS in the clear lake, only her head and shoulders above the "
                  "water, smiling, her hair wet; a wooden jetty and people lying on the grassy shore in the background. "
                  "Her face is close enough to be recognised."},
    "eis":       {"saison": "verano", "temp": 32, "act": "eis", "vrais": ["sol", "calor", "buen"], "douteux": [], "source": ["Ben", "Mia"],
        "prompt": "On a very hot, sunny summer day in a Berlin street, in front of a small ice-cream parlour with a striped "
                  "awning (no writing anywhere): the boy of the first picture and the girl of the second picture each eat "
                  "an ice-cream cone, smiling and happy; strong sunshine, a blue sky, short shadows. Seen from the front."},
    "blaetter":  {"saison": "otono", "temp": 12, "act": "blaetter", "vrais": [], "douteux": ["sol", "fresco", "buen", "nublado", "viento", "frio"], "source": ["Ben", "Mia"],
        "prompt": "In a forest near Berlin in AUTUMN: the trees are yellow, orange and red, the ground is covered with "
                  "fallen leaves; the boy of the first picture and the girl of the second picture collect colourful "
                  "leaves, hold them up and laugh; soft autumn sunlight between the trees. Seen from the front."},
    "schnee":    {"saison": "invierno", "temp": -3, "act": "schnee", "vrais": ["frio"], "douteux": ["sol", "buen", "nieve", "fresco"], "source": ["Ben", "Mia"],
        "prompt": "In a Berlin park in WINTER, a cold sunny day after a heavy snowfall, everything covered in white snow, a "
                  "blue sky: the boy of the first picture and the girl of the second picture play in the snow, throw snow "
                  "in the air and laugh, in warm winter clothes. No snowman, no sledge. Seen from the front."},
    "lesen":     {"saison": None, "temp": 13, "act": "lesen", "vrais": ["lluvia", "malo"], "douteux": ["nublado", "fresco", "frio", "viento"], "source": ["Anna", "Mia"],
        "prompt": "Inside a cosy living room on a RAINY day: heavy rain runs down the big window behind them, the sky "
                  "outside is dark grey; the woman of the first picture sits on a sofa and reads a picture book to the "
                  "girl of the second picture, who sits next to her and smiles; a warm lamp is lit. Seen from the front."},
}
ESSAI = ["sommer", "regen", "winter", "herbst", "see", "lesen"]        # la planche d'essai (0,90 $)
SAISONS = {"primavera": ("primavera", "Frühling"), "verano": ("verano", "Sommer"), "otono": ("otoño", "Herbst"), "invierno": ("invierno", "Winter")}
# « Es verano. » / « Es ist Sommer. » (la saison d'une image) et ses traductions (fr, en, pt, de)
SAISON_PHRASE = {"primavera": ("Es primavera.", "Es ist Frühling.", "C'est le printemps.", "It's spring.", "É primavera."),
                 "verano": ("Es verano.", "Es ist Sommer.", "C'est l'été.", "It's summer.", "É verão."),
                 "otono": ("Es otoño.", "Es ist Herbst.", "C'est l'automne.", "It's autumn.", "É outono."),
                 "invierno": ("Es invierno.", "Es ist Winter.", "C'est l'hiver.", "It's winter.", "É inverno.")}
# les enonces dans la langue apprise ({q} : la personne ; ___ : le trou)
ENONCES = {"es": {"temps": "¿Qué tiempo hace?", "degres": "¿Cuántos grados hace?", "saison": "¿Qué estación es?",
                  "act": "¿Qué pasa en la foto?", "dit": "{q} dice: «___»", "vrai": "Verdadero", "faux": "Falso", "bravo": "¡Muy bien!"},
           "de": {"temps": "Wie ist das Wetter?", "degres": "Wie warm ist es?", "saison": "Welche Jahreszeit ist das?",
                  "act": "Was passiert auf dem Bild?", "dit": "{q} sagt: „___“", "vrai": "Richtig", "faux": "Falsch", "bravo": "Sehr gut!"}}
TRAD_SAISON = {"primavera": ("le printemps", "spring", "primavera", "Frühling"), "verano": ("l'été", "summer", "verão", "Sommer"),
               "otono": ("l'automne", "autumn", "outono", "Herbst"), "invierno": ("l'hiver", "winter", "inverno", "Winter")}

# LES MOMENTS DE SAISON : la phrase, le trou du verbe et ses leurres (la personne, le radical : jugan pour juegan,
# lest pour liest), et les mots qu'elle fait travailler (le premier : celui du trou).
ACTIVITES = {
    "park":     {"es": {"phrase": "En primavera, Anna pasea por el parque con Ben y Mia.", "verbe": "pasea", "leurres": ["pasean", "paseo"], "mots": ["pasear", "parque", "primavera"]},
                 "de": {"phrase": "Im Frühling geht Anna mit Ben und Mia im Park spazieren.", "verbe": "geht", "leurres": ["gehen", "gehst"], "mots": ["spazieren", "Park", "Frühling"],
                        "v2": "Im Frühling Anna geht mit Ben und Mia im Park spazieren."},
                 "trad": ("Au printemps, Anna se promène dans le parc avec Ben et Mia.", "In spring, Anna goes for a walk in the park with Ben and Mia.",
                          "Na primavera, a Anna passeia no parque com o Ben e a Mia.", "Im Frühling geht Anna mit Ben und Mia im Park spazieren.")},
    "see":      {"es": {"phrase": "En verano, Anna nada en el lago.", "verbe": "nada", "leurres": ["nadan", "nado"], "mots": ["nadar", "lago", "verano"]},
                 "de": {"phrase": "Im Sommer schwimmt Anna im See.", "verbe": "schwimmt", "leurres": ["schwimmen", "schwimme"], "mots": ["schwimmen", "See", "Sommer"],
                        "v2": "Im Sommer Anna schwimmt im See."},
                 "trad": ("En été, Anna nage dans le lac.", "In summer, Anna swims in the lake.", "No verão, a Anna nada no lago.", "Im Sommer schwimmt Anna im See.")},
    "eis":      {"es": {"phrase": "En verano, Ben y Mia comen helado.", "verbe": "comen", "leurres": ["come", "comemos"], "mots": ["comer", "helado", "verano"]},
                 "de": {"phrase": "Im Sommer essen Ben und Mia Eis.", "verbe": "essen", "leurres": ["isst", "esst"], "mots": ["essen", "Eis", "Sommer"],
                        "v2": "Im Sommer Ben und Mia essen Eis."},
                 "trad": ("En été, Ben et Mia mangent une glace.", "In summer, Ben and Mia eat ice cream.", "No verão, o Ben e a Mia tomam sorvete.", "Im Sommer essen Ben und Mia Eis.")},
    "blaetter": {"es": {"phrase": "En otoño, Ben y Mia recogen hojas en el bosque.", "verbe": "recogen", "leurres": ["recoge", "recojen"], "mots": ["recoger", "hoja", "otoño"]},
                 "de": {"phrase": "Im Herbst sammeln Ben und Mia Blätter im Wald.", "verbe": "sammeln", "leurres": ["sammelt", "sammle"], "mots": ["sammeln", "Blatt", "Herbst"],
                        "v2": "Im Herbst Ben und Mia sammeln Blätter im Wald."},
                 "trad": ("En automne, Ben et Mia ramassent des feuilles dans la forêt.", "In autumn, Ben and Mia collect leaves in the forest.",
                          "No outono, o Ben e a Mia apanham folhas na floresta.", "Im Herbst sammeln Ben und Mia Blätter im Wald.")},
    "schnee":   {"es": {"phrase": "En invierno, Ben y Mia juegan en la nieve.", "verbe": "juegan", "leurres": ["jugan", "juega"], "mots": ["jugar", "nieve", "invierno"]},
                 "de": {"phrase": "Im Winter spielen Ben und Mia im Schnee.", "verbe": "spielen", "leurres": ["spielt", "spiele"], "mots": ["spielen", "Schnee", "Winter"],
                        "v2": "Im Winter Ben und Mia spielen im Schnee."},
                 "trad": ("En hiver, Ben et Mia jouent dans la neige.", "In winter, Ben and Mia play in the snow.", "No inverno, o Ben e a Mia brincam na neve.", "Im Winter spielen Ben und Mia im Schnee.")},
    "lesen":    {"es": {"phrase": "Cuando llueve, Anna lee un libro con Mia.", "verbe": "lee", "leurres": ["leen", "lea"], "mots": ["leer", "llover"]},
                 "de": {"phrase": "Wenn es regnet, liest Anna mit Mia ein Buch.", "verbe": "liest", "leurres": ["lest", "lesen"], "mots": ["lesen", "regnen"],
                        "v2": "Wenn es regnet, Anna liest mit Mia ein Buch."},
                 "trad": ("Quand il pleut, Anna lit un livre avec Mia.", "When it rains, Anna reads a book with Mia.", "Quando chove, a Anna lê um livro com a Mia.", "Wenn es regnet, liest Anna mit Mia ein Buch.")},
}

# LA FAMILLE DU MOT : le nom, le verbe, l'adjectif (der Regen, es regnet ; la lluvia, llueve) -- la confusion la plus
# frequente d'un debutant. (phrase a trou, la bonne forme, les autres formes, le mot travaille, l'image ou c'est vrai)
FAMILLES = {
    "es": [("Hoy ___ mucho.", "llueve", ["lluvia", "llover"], "llover", "regen"),
           ("La ___ no para.", "lluvia", ["llueve", "llover"], "lluvia", "regen"),
           ("Hoy ___.", "nieva", ["nieve", "nevar"], "nevar", "winter"),
           ("Hay mucha ___ en la plaza.", "nieve", ["nieva", "nevar"], "nieve", "winter"),
           ("Hace mucho ___.", "sol", ["soleado"], "sol", "sommer"),
           ("Es un día ___.", "soleado", ["sol"], "soleado", "sommer"),
           ("El cielo está ___.", "nublado", ["nube", "nubes"], "nublado", "bewoelkt"),
           ("Hay muchas ___ en el cielo.", "nubes", ["nublado", "nube"], "nube", "bewoelkt"),
           ("Hace mucho ___.", "viento", ["ventoso"], "viento", "herbst")],
    "de": [("Es ___.", "regnet", ["Regen", "regnen"], "regnen", "regen"),
           ("Heute gibt es viel ___.", "Regen", ["regnet", "regnerisch"], "Regen", "regen"),
           ("Es ___.", "schneit", ["Schnee", "schneien"], "schneien", "winter"),
           ("Auf dem Platz liegt viel ___.", "Schnee", ["schneit", "schneien"], "Schnee", "winter"),
           ("Es ist ___.", "sonnig", ["Sonne", "scheint"], "sonnig", "sommer"),
           ("Die ___ scheint.", "Sonne", ["sonnig", "scheint"], "Sonne", "sommer"),
           ("Es ist ___.", "bewölkt", ["Wolke", "Wolken"], "bewölkt", "bewoelkt"),
           ("Am Himmel sind viele ___.", "Wolken", ["bewölkt", "Wolke"], "Wolke", "bewoelkt"),
           ("Es ist ___.", "windig", ["Wind"], "windig", "herbst"),
           ("Der ___ ist sehr stark.", "Wind", ["windig"], "Wind", "herbst"),
           ("Es ist ___.", "neblig", ["Nebel"], "neblig", "nebel"),
           ("Heute gibt es viel ___.", "Nebel", ["neblig"], "Nebel", "nebel")],
}
# le fait que dit chaque phrase de la famille, d'apres son image : elle est aussi un « vrai ou faux » sur une autre photo
FAIT_FAMILLE = {"regen": "lluvia", "winter": "nieve", "sommer": "sol", "bewoelkt": "nublado", "herbst": "viento", "nebel": "niebla"}
TRAD_FAMILLES = {
    "Hoy llueve mucho.": ("Aujourd'hui, il pleut beaucoup.", "It's raining a lot today.", "Hoje está chovendo muito.", "Heute regnet es viel."),
    "La lluvia no para.": ("La pluie ne s'arrête pas.", "The rain isn't stopping.", "A chuva não para.", "Der Regen hört nicht auf."),
    "Hoy nieva.": ("Aujourd'hui, il neige.", "It's snowing today.", "Hoje está nevando.", "Heute schneit es."),
    "Hay mucha nieve en la plaza.": ("Il y a beaucoup de neige sur la place.", "There's a lot of snow on the square.", "Tem muita neve na praça.", "Auf dem Platz liegt viel Schnee."),
    "Hace mucho sol.": ("Il y a beaucoup de soleil.", "It's very sunny.", "Está fazendo muito sol.", "Die Sonne scheint stark."),
    "Es un día soleado.": ("C'est une journée ensoleillée.", "It's a sunny day.", "É um dia ensolarado.", "Es ist ein sonniger Tag."),
    "El cielo está nublado.": ("Le ciel est couvert.", "The sky is cloudy.", "O céu está nublado.", "Der Himmel ist bewölkt."),
    "Hay muchas nubes en el cielo.": ("Il y a beaucoup de nuages dans le ciel.", "There are a lot of clouds in the sky.", "Tem muitas nuvens no céu.", "Am Himmel sind viele Wolken."),
    "Hace mucho viento.": ("Il y a beaucoup de vent.", "It's very windy.", "Está ventando muito.", "Es ist sehr windig."),
    "Es regnet.": None, "Es schneit.": None, "Es ist sonnig.": None, "Es ist bewölkt.": None, "Es ist windig.": None, "Es ist neblig.": None,
    "Heute gibt es viel Regen.": ("Aujourd'hui, il y a beaucoup de pluie.", "There's a lot of rain today.", "Hoje tem muita chuva."),
    "Auf dem Platz liegt viel Schnee.": ("Il y a beaucoup de neige sur la place.", "There's a lot of snow on the square.", "Tem muita neve na praça."),
    "Die Sonne scheint.": None,
    "Am Himmel sind viele Wolken.": ("Il y a beaucoup de nuages dans le ciel.", "There are a lot of clouds in the sky.", "Tem muitas nuvens no céu."),
    "Der Wind ist sehr stark.": ("Le vent est très fort.", "The wind is very strong.", "O vento está muito forte."),
    "Heute gibt es viel Nebel.": ("Aujourd'hui, il y a beaucoup de brouillard.", "There's a lot of fog today.", "Hoje tem muita neblina."),
}

# HACE, ESTA OU HAY (espagnol) ; IST, GIBT OU « MACHT » (allemand : « es macht kalt » est le calque du francais).
# (le fait, la phrase a trou, la bonne reponse, les options) -- pas de « hay » pour sol et viento : « hay sol », « hay
# viento » se disent aussi, surtout en Amerique latine.
VERBE_TEMPS = {
    "es": [("calor", "___ calor.", "Hace", ["Hace", "Está", "Hay"]), ("frio", "___ frío.", "Hace", ["Hace", "Está", "Hay"]),
           ("fresco", "___ fresco.", "Hace", ["Hace", "Hay"]), ("sol", "___ sol.", "Hace", ["Hace", "Está"]),
           ("sol", "___ soleado.", "Está", ["Está", "Hace", "Hay"]), ("viento", "___ viento.", "Hace", ["Hace", "Está"]),
           ("nublado", "___ nublado.", "Está", ["Está", "Hace", "Hay"]), ("niebla", "___ niebla.", "Hay", ["Hay", "Hace", "Está"]),
           ("tormenta", "___ tormenta.", "Hay", ["Hay", "Hace", "Está"]), ("buen", "___ buen tiempo.", "Hace", ["Hace", "Está", "Hay"]),
           ("malo", "___ mal tiempo.", "Hace", ["Hace", "Está", "Hay"])],
    "de": [("calor", "Es ___ heiß.", "ist", ["ist", "macht", "gibt"]), ("frio", "Es ___ kalt.", "ist", ["ist", "macht", "gibt"]),
           ("fresco", "Es ___ kühl.", "ist", ["ist", "macht", "gibt"]), ("sol", "Es ___ sonnig.", "ist", ["ist", "macht", "gibt"]),
           ("viento", "Es ___ windig.", "ist", ["ist", "macht", "gibt"]), ("nublado", "Es ___ bewölkt.", "ist", ["ist", "macht", "gibt"]),
           ("niebla", "Es ___ neblig.", "ist", ["ist", "gibt", "macht"]), ("tormenta", "Es ___ ein Gewitter.", "gibt", ["gibt", "ist", "macht"]),
           ("buen", "Das Wetter ___ schön.", "ist", ["ist", "macht", "gibt"])],
}

# DEHORS OU MOI : hace frio / tengo frio ; es ist kalt / mir ist kalt. Le piege du francais (« j'ai froid ») et deux
# formes qui veulent dire autre chose (soy fria : je suis une personne froide ; ich bin kalt). Jamais « estoy
# caliente » ni « ich bin heiss » sur un bouton : la decouverte en parle, sans le faire choisir.
# (qui, l'image, ce qu'on demande : moi | dehors, la bonne reponse, les autres, le mot)
RESSENTI = {
    "es": [("Anna", "winter", "moi", "Tengo frío.", ["Hace frío.", "Soy fría."], "frío"),
           ("Anna", "winter", "dehors", "Hace frío.", ["Tengo frío.", "Soy fría."], "frío"),
           ("Mark", "nebel", "moi", "Tengo frío.", ["Hace frío.", "Soy frío."], "frío"),
           ("Mark", "nebel", "dehors", "Hace frío.", ["Tengo frío.", "Soy frío."], "frío"),
           ("Anna", "sommer", "moi", "Tengo calor.", ["Hace calor."], "calor"),
           ("Anna", "sommer", "dehors", "Hace calor.", ["Tengo calor."], "calor"),
           ("Mark", "sommer", "moi", "Tengo calor.", ["Hace calor."], "calor"),
           ("Mark", "sommer", "dehors", "Hace calor.", ["Tengo calor."], "calor")],
    "de": [("Anna", "winter", "moi", "Mir ist kalt.", ["Es ist kalt.", "Ich bin kalt.", "Ich habe kalt."], "kalt"),
           ("Anna", "winter", "dehors", "Es ist kalt.", ["Mir ist kalt.", "Es macht kalt."], "kalt"),
           ("Mark", "nebel", "moi", "Mir ist kalt.", ["Es ist kalt.", "Ich habe kalt."], "kalt"),
           ("Mark", "nebel", "dehors", "Es ist kalt.", ["Mir ist kalt.", "Es macht kalt."], "kalt"),
           ("Anna", "sommer", "moi", "Mir ist heiß.", ["Es ist heiß.", "Ich habe heiß."], "heiß"),
           ("Anna", "sommer", "dehors", "Es ist heiß.", ["Mir ist heiß.", "Es macht heiß."], "heiß"),
           ("Mark", "sommer", "moi", "Mir ist heiß.", ["Es ist heiß.", "Ich habe heiß."], "heiß"),
           ("Mark", "sommer", "dehors", "Es ist heiß.", ["Mir ist heiß.", "Es macht heiß."], "heiß")],
}
TRAD_RESSENTI = {
    "Tengo frío.": ("J'ai froid.", "I'm cold.", "Estou com frio.", "Mir ist kalt."), "Tengo calor.": ("J'ai chaud.", "I'm hot.", "Estou com calor.", "Mir ist heiß."),
    "Mir ist kalt.": ("J'ai froid.", "I'm cold.", "Estou com frio."), "Mir ist heiß.": ("J'ai chaud.", "I'm hot.", "Estou com calor."),
}
# ce que veut dire le mauvais choix (« Tu as choisi : Soy fría — je suis une personne froide ») ; « Ich habe kalt »,
# « Es macht kalt » n'existent pas : on le dit
CHOIX_RESSENTI = {
    "Soy fría.": ("je suis une personne froide (le caractère)", "I'm a cold person (character)", "sou uma pessoa fria (o caráter)", "ich bin ein kalter Mensch (der Charakter)"),
    "Soy frío.": ("je suis une personne froide (le caractère)", "I'm a cold person (character)", "sou uma pessoa fria (o caráter)", "ich bin ein kalter Mensch (der Charakter)"),
    "Ich bin kalt.": ("je suis froid au toucher, ou une personne froide", "I'm cold to the touch, or a cold person", "estou frio ao toque, ou sou uma pessoa fria"),
    "Ich habe kalt.": ("ne se dit pas : c'est le français mot à mot", "not German: a word-for-word copy of French", "não se diz: é o francês palavra por palavra"),
    "Ich habe heiß.": ("ne se dit pas : c'est le français mot à mot", "not German: a word-for-word copy of French", "não se diz: é o francês palavra por palavra"),
    "Es macht kalt.": ("ne se dit pas : c'est le français mot à mot", "not German: a word-for-word copy of French", "não se diz: é o francês palavra por palavra"),
    "Es macht heiß.": ("ne se dit pas : c'est le français mot à mot", "not German: a word-for-word copy of French", "não se diz: é o francês palavra por palavra"),
}

# L'ORDRE DES MOTS (allemand) : le verbe en DEUXIEME position, meme apres « heute » ou « im Winter » -- l'erreur que fait
# tout francophone. (la phrase juste, la phrase fautive, le mot, l'image)
V2_TEMPS = [("Heute regnet es.", "Heute es regnet.", "regnen", "regen"), ("Heute schneit es.", "Heute es schneit.", "schneien", "winter"),
            ("Heute ist es kalt.", "Heute es ist kalt.", "kalt", "winter"), ("Heute ist es heiß.", "Heute es ist heiß.", "heiß", "sommer"),
            ("Heute ist es windig.", "Heute es ist windig.", "windig", "herbst"), ("Heute ist es neblig.", "Heute es ist neblig.", "neblig", "nebel"),
            ("Heute gibt es ein Gewitter.", "Heute es gibt ein Gewitter.", "Gewitter", "gewitter"),
            ("Im Winter ist es kalt.", "Im Winter es ist kalt.", "Winter", "winter"), ("Im Sommer ist es heiß.", "Im Sommer es ist heiß.", "Sommer", "sommer")]
TRAD_V2 = {"Heute regnet es.": ("Aujourd'hui, il pleut.", "It's raining today.", "Hoje está chovendo."),
           "Heute schneit es.": ("Aujourd'hui, il neige.", "It's snowing today.", "Hoje está nevando."),
           "Heute ist es kalt.": ("Aujourd'hui, il fait froid.", "It's cold today.", "Hoje está frio."),
           "Heute ist es heiß.": ("Aujourd'hui, il fait très chaud.", "It's hot today.", "Hoje está muito quente."),
           "Heute ist es windig.": ("Aujourd'hui, il y a du vent.", "It's windy today.", "Hoje está ventando."),
           "Heute ist es neblig.": ("Aujourd'hui, il y a du brouillard.", "It's foggy today.", "Hoje tem neblina."),
           "Heute gibt es ein Gewitter.": ("Aujourd'hui, il y a un orage.", "There's a thunderstorm today.", "Hoje tem uma tempestade."),
           "Im Winter ist es kalt.": ("En hiver, il fait froid.", "It's cold in winter.", "No inverno, faz frio."),
           "Im Sommer ist es heiß.": ("En été, il fait très chaud.", "It's hot in summer.", "No verão, faz muito calor.")}

# ---------------------------------------------------------------------------------------------------------------
# LES DEGRES, en lettres (la voix les dit comme ils s'ecrivent ; rien a mettre dans audio/lectures). Le thermometre
# montre le chiffre. veintiun et treinta y un devant grados (l'apocope) ; un seul degre : jamais demande.
UNITES_ES = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece",
             "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiún", "veintidós",
             "veintitrés", "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
DIZ_ES = {3: "treinta", 4: "cuarenta", 5: "cincuenta"}
UNITES_DE = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf", "dreizehn",
             "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]
DIZ_DE = {2: "zwanzig", 3: "dreißig", 4: "vierzig", 5: "fünfzig"}


def nombre_es(n):
    if n < 30:
        return UNITES_ES[n]
    d, u = divmod(n, 10)
    return DIZ_ES[d] + ("" if not u else " y " + ("un" if u == 1 else UNITES_ES[u]))


def nombre_de(n):
    if n < 20:
        return UNITES_DE[n]
    d, u = divmod(n, 10)
    return ("" if not u else ("ein" if u == 1 else UNITES_DE[u]) + "und") + DIZ_DE[d]


def degres_es(t):
    return "Hace %s grados%s." % (nombre_es(abs(t)), " bajo cero" if t < 0 else "")


def degres_de(t):
    return "Es sind %s%s Grad." % ("minus " if t < 0 else "", nombre_de(abs(t)))


def trad_degres(t):
    a = abs(t)
    return ("Il fait %s%d degrés." % ("moins " if t < 0 else "", a), "It's %s%d degrees." % ("minus " if t < 0 else "", a),
            "Faz %d graus%s." % (a, " abaixo de zero" if t < 0 else ""), "Es sind %s%d Grad." % ("minus " if t < 0 else "", a))


# les temperatures demandees (jamais 1 ni -1, le singulier), et les nombres possibles pour un leurre
TEMPERATURES = [-10, -8, -6, -5, -4, -3, -2, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
LEURRES_NOMBRES = sorted(set(range(-12, 51)) - {1, -1})
# LE RESSENTI selon les degres : des bandes SEPAREES, pour qu'un seul mot soit juste (19 degres n'est ni chaud ni frais)
BANDES = {"es": [("calor", 28, 99), ("fresco", 10, 16), ("frio", -99, 5)],
          "de": [("calor", 30, 99), ("warm", 20, 26), ("fresco", 9, 15), ("frio", -99, 4)]}
BANDE_PHRASE = {"es": {"calor": ("Hace calor.", "calor"), "fresco": ("Hace fresco.", "fresco"), "frio": ("Hace frío.", "frío")},
                "de": {"calor": ("Es ist heiß.", "heiß"), "warm": ("Es ist warm.", "warm"), "fresco": ("Es ist kühl.", "kühl"), "frio": ("Es ist kalt.", "kalt")}}
TRAD_WARM = ("Il fait bon.", "It's warm.", "Está agradável.")

# LES MOIS, chacun dans UNE saison sans discussion (pas mars, juin, septembre ni decembre, qui changent de saison en
# cours de mois). En Espagne et en Allemagne : l'hemisphere nord -- la decouverte dit que c'est l'inverse en
# Argentine ou au Chili.
MOIS = [("enero", "Januar", "invierno", "janvier", "January", "janeiro"), ("febrero", "Februar", "invierno", "février", "February", "fevereiro"),
        ("abril", "April", "primavera", "avril", "April", "abril"), ("mayo", "Mai", "primavera", "mai", "May", "maio"),
        ("julio", "Juli", "verano", "juillet", "July", "julho"), ("agosto", "August", "verano", "août", "August", "agosto"),
        ("octubre", "Oktober", "otono", "octobre", "October", "outubro"), ("noviembre", "November", "otono", "novembre", "November", "novembro")]
SAISON_FR = {"primavera": ("le printemps", "de printemps"), "verano": ("l'été", "d'été"), "otono": ("l'automne", "d'automne"), "invierno": ("l'hiver", "d'hiver")}
SAISON_DE_MONAT = {"primavera": "Frühlingsmonat", "verano": "Sommermonat", "otono": "Herbstmonat", "invierno": "Wintermonat"}


def phrases_mois():
    """{es: {mes: {...}}, de: {...}} : la phrase de la saison et la phrase du mois, et leurs traductions."""
    es, de, trad_es, trad_de = {}, {}, {}, {}
    for m_es, m_de, s, fr, en, pt in MOIS:
        s_es, s_de = SAISONS[s]
        f_s, f_de_s = SAISON_FR[s]
        en_s, pt_s = TRAD_SAISON[s][1], TRAD_SAISON[s][2]
        p1 = "En España, en %s es %s." % (m_es, s_es)
        p2 = "En España, %s es un mes de %s." % (m_es, s_es)
        es[m_es] = {"saison": s, "phrase": p1, "trouSaison": "En España, en %s es ___." % m_es,
                    "phraseMois": p2, "trouMois": "En España, ___ es un mes de %s." % s_es}
        trad_es[p1] = ("En Espagne, en %s, c'est %s." % (fr, f_s), "In Spain, it's %s in %s." % (en_s, en),
                       "Na Espanha, em %s é %s." % (pt, pt_s), "In Spanien ist im %s %s." % (m_de, s_de))
        trad_es[p2] = ("En Espagne, %s est un mois %s." % (fr, f_de_s), "In Spain, %s is a %s month." % (en, en_s),
                       "Na Espanha, %s é um mês de %s." % (pt, pt_s), "In Spanien ist der %s ein %s." % (m_de, SAISON_DE_MONAT[s]))
        q = "Im %s ist in Deutschland %s." % (m_de, s_de)
        de[m_de] = {"saison": s, "phrase": q, "trouSaison": "Im %s ist in Deutschland ___." % m_de,
                    "trouMois": "___ ist in Deutschland %s." % s_de, "repMois": "Im " + m_de}
        trad_de[q] = ("En %s, en Allemagne, c'est %s." % (fr, f_s), "In Germany, it's %s in %s." % (en_s, en),
                      "Em %s, na Alemanha, é %s." % (pt, pt_s))
    return es, de, trad_es, trad_de


# ---------------------------------------------------------------------------------------------------------------
LANGUES = {"es": ["fr", "en", "pt", "ar", "de"], "de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]}


def corpus():
    """{es: {cle: entree}, de: {...}} -- les noms des themes, les adjectifs, les verbes ; une cle absente arrete."""
    def charger(chemin):
        return json.load(io.open(os.path.join(RACINE, chemin), encoding="utf-8"))
    out = {}
    for l, (themes, adj, verb) in {"es": ("espanol/datos/temas.json", "espanol/datos/adjetivos.json", "espanol/datos/verbos.json"),
                                   "de": ("themes.json", "adjectif.json", "verbe.json")}.items():
        noms, adjs, verbes = {}, {}, {}
        for t in charger(themes)["themes"]:
            for m in t["mots"]:
                noms.setdefault((m["mot"], m.get("genre")), m)
        for liste in charger(adj).values():
            for e in liste:
                adjs.setdefault(e["mot"], e)
        for liste in charger(verb).values():
            for e in liste:
                verbes.setdefault(e["infinitif"], e)
        res = {}
        for cle, g in MOTS[l].items():
            e = adjs.get(cle) if g == "adjectif" else verbes.get(cle) if g == "verbe" else noms.get((cle, g))
            if not e:
                sys.exit("  %s (%s, %s) absent du corpus" % (cle, l, g))
            gl = {x: e.get("traduction" if x == "fr" else "traduction_" + x) for x in LANGUES[l]}
            manque = [x for x, v in gl.items() if not v]
            if manque:
                sys.exit("  %s (%s) : pas de traduction en %s" % (cle, l, ", ".join(manque)))
            res[cle] = gl
        out[l] = res
    return out


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def verifier():
    """Les controles qu'aucune page ne ferait : chaque mot vise par au moins une question, chaque phrase traduite."""
    for i, im in IMAGES.items():
        if set(im["vrais"]) & set(im["douteux"]):
            sys.exit("  %s : un fait vrai ET douteux" % i)
        for f in im["vrais"] + im["douteux"]:
            if f not in FAITS:
                sys.exit("  %s : fait inconnu %s" % (i, f))
        if im.get("act") and im["act"] not in ACTIVITES:
            sys.exit("  %s : activite inconnue" % i)
    for l in ("es", "de"):
        vises = set()
        for k, f in FAITS.items():
            if any(k in im["vrais"] for im in IMAGES.values()):
                vises |= {w for _, w in f[l]}
        vises |= {x[3] for x in FAMILLES[l]} | {x[5] for x in RESSENTI[l]}
        vises |= {w for a in ACTIVITES.values() for w in a[l]["mots"]}
        vises |= {"grado" if l == "es" else "Grad"} | {w for _, w in BANDE_PHRASE[l].values()}
        vises |= {m[0] if l == "es" else m[1] for m in MOIS} | {s[0] if l == "es" else s[1] for s in SAISONS.values()}
        if l == "de":
            vises |= {x[2] for x in V2_TEMPS}
        for k, f, rep, opts in VERBE_TEMPS[l]:
            vises |= {w for _, w in FAITS[k][l]}
        orphelins = set(MOTS[l]) - vises
        if orphelins:
            sys.exit("  %s : mots qu'aucune question ne vise : %s" % (l, ", ".join(sorted(orphelins))))
        inconnus = vises - set(MOTS[l])
        if inconnus:
            sys.exit("  %s : mots vises absents de MOTS : %s" % (l, ", ".join(sorted(inconnus))))


def ecrire_json():
    verifier()
    gloses = corpus()
    mois_es, mois_de, trad_mois_es, trad_mois_de = phrases_mois()
    trad = {"es": {}, "de": {}}
    for p, t in TRAD_FAITS.items():
        trad["es" if len(t) == 4 else "de"][p] = dict(zip(("fr", "en", "pt", "de"), t))
    for a in ACTIVITES.values():
        trad["es"][a["es"]["phrase"]] = dict(zip(("fr", "en", "pt", "de"), a["trad"]))
        trad["de"][a["de"]["phrase"]] = dict(zip(("fr", "en", "pt"), a["trad"][:3]))
    for p, t in list(TRAD_FAMILLES.items()) + list(TRAD_RESSENTI.items()) + list(TRAD_V2.items()):
        if t:
            trad["es" if len(t) == 4 else "de"][p] = dict(zip(("fr", "en", "pt", "de"), t))
    trad["de"]["Es ist warm."] = dict(zip(("fr", "en", "pt"), TRAD_WARM))
    for p, t in trad_mois_es.items():
        trad["es"][p] = dict(zip(("fr", "en", "pt", "de"), t))
    for p, t in trad_mois_de.items():
        trad["de"][p] = dict(zip(("fr", "en", "pt"), t))
    degres = {"es": {}, "de": {}}
    for t in LEURRES_NOMBRES:
        degres["es"][t], degres["de"][t] = degres_es(t), degres_de(t)
        tr = trad_degres(t)
        trad["es"][degres_es(t)] = dict(zip(("fr", "en", "pt", "de"), tr))
        trad["de"][degres_de(t)] = dict(zip(("fr", "en", "pt"), tr[:3]))
    # chaque phrase juste que la page peut montrer doit avoir sa traduction (les phrases completees des familles, de
    # « hace / ist » et de l'ordre des mots sont des faits ou des phrases deja traduites)
    for l in ("es", "de"):
        manque = [x[0].replace("___", x[1]) for x in FAMILLES[l] if x[0].replace("___", x[1]) not in trad[l]]
        manque += [x[1].replace("___", x[2]) for x in VERBE_TEMPS[l] if x[1].replace("___", x[2]) not in trad[l]]
        manque += [x[3] for x in RESSENTI[l] if x[3] not in trad[l]]
        manque += [x[0] for x in V2_TEMPS if x[0] not in trad["de"]] if l == "de" else []
        if manque:
            sys.exit("  %s : sans traduction : %s" % (l, " | ".join(manque)))
    images = {i: {k: v for k, v in im.items() if k not in ("prompt", "source")} for i, im in IMAGES.items()}
    d = {"faits": FAITS, "mots": MOTS, "images": images, "saisons": SAISONS, "activites": {k: {l: a[l] for l in ("es", "de")} for k, a in ACTIVITES.items()},
         "familles": {l: [list(x) + [FAIT_FAMILLE[x[4]]] for x in FAMILLES[l]] for l in FAMILLES}, "verbeTemps": VERBE_TEMPS, "ressenti": RESSENTI, "choixRessenti": {p: dict(zip(("fr", "en", "pt", "de"), t)) for p, t in CHOIX_RESSENTI.items()},
         "v2": V2_TEMPS, "temperatures": TEMPERATURES, "leurresNombres": LEURRES_NOMBRES, "degres": degres, "bandes": BANDES,
         "bandePhrase": BANDE_PHRASE, "mois": {"es": mois_es, "de": mois_de}, "trad": trad, "gloses": gloses,
         "tradSaison": {s: dict(zip(("fr", "en", "pt", "de"), t)) for s, t in TRAD_SAISON.items()},
         "saisonPhrase": {s: {"es": t[0], "de": t[1]} for s, t in SAISON_PHRASE.items()}, "enonces": ENONCES}
    for s, t in SAISON_PHRASE.items():
        trad["es"][t[0]] = dict(zip(("fr", "en", "pt", "de"), t[2:] + (t[1],)))
        trad["de"][t[1]] = dict(zip(("fr", "en", "pt"), t[2:]))
    # ce que la decouverte dit (et l'identifiant de son fichier, sha1 du texte) ; sans fichier, la voix du telephone
    a_dire = {"es": [], "de": []}
    for l in ("es", "de"):
        for f in FAITS.values():
            a_dire[l] += [p for p, _ in f[l]]
        a_dire[l] += [a[l]["phrase"] for a in ACTIVITES.values()]
        a_dire[l] += [degres[l][t] for t in TEMPERATURES]
        a_dire[l] += [m["phrase"] for m in (mois_es if l == "es" else mois_de).values()]
    d["sons"] = {l: {t: identifiant(t) for t in dict.fromkeys(v)} for l, v in a_dire.items()}
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    for chemin in (os.path.join(RACINE, "visuel", "prototype", "meteo", "meteo.json"),):
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(texte)
    # les voix a enregistrer (visuel/meteo/voix.json) : c'est visuel/voix_themes.py qui les releve, dans la page et
    # en jouant des parties (les phrases dites apres une reponse)
    print("  -> visuel/prototype/meteo/meteo.json (%d images, %d mots es, %d mots de)" % (len(IMAGES), len(MOTS["es"]), len(MOTS["de"])))
    return d


def prompts():
    out = {}
    for i, im in IMAGES.items():
        src = im.get("source")
        if isinstance(src, list):
            refs = ", ".join("the %s picture: %s" % (("first", "second", "third")[n], q) for n, q in enumerate(src))
            out[i] = (src, MEME + "(" + refs + ") " + im["prompt"] + PHOTO)
        elif src:
            out[i] = (src, GARDE + im["prompt"] + PHOTO)
        else:
            out[i] = (None, im["prompt"] + PHOTO)
    return out


def depense():
    chemin = os.path.join(DOSSIER, "depenses.log")
    if not os.path.exists(chemin):
        return 0.0
    total = 0.0
    for ligne in io.open(chemin, encoding="utf-8"):
        c = ligne.rstrip("\n").split("\t")
        try:
            total += float(c[3])
        except (IndexError, ValueError):
            pass
    return total


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    ecrire_json()
    if "--json" in sys.argv:
        return
    tout = prompts()
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or (ESSAI if "--essai" in sys.argv else list(tout))
    inconnus = [n for n in noms if n not in tout]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    os.makedirs(DOSSIER, exist_ok=True)
    if refaire and not montrer:
        for n in noms:
            png = os.path.join(DOSSIER, n + ".png")
            if os.path.exists(png):
                k = 1
                while os.path.exists(os.path.join(DOSSIER, "%s-rate%d.png" % (n, k))):
                    k += 1
                os.replace(png, os.path.join(DOSSIER, "%s-rate%d.png" % (n, k)))
    a_faire = [n for n in noms if not os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    a_faire.sort(key=lambda n: isinstance(tout[n][0], str))     # la base avant ses retouches
    deja = depense()
    print("  %d image(s) a faire, %.2f $ ; deja depense %.2f $, plafond %.2f $" % (len(a_faire), len(a_faire) * PRIX, deja, PLAFOND))
    if not montrer and deja + len(a_faire) * PRIX > PLAFOND + 1e-9:
        sys.exit("  PLAFOND : %.2f + %.2f > %.2f $ -- demander a Jacques" % (deja, len(a_faire) * PRIX, PLAFOND))
    if montrer:
        for nom in a_faire:
            print("\n  %s%s\n  %s" % (nom, " (retouche de %s)" % (tout[nom][0],) if tout[nom][0] else "", tout[nom][1]))
        return
    import omnihuman as O                                    # noqa: E402
    if not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    for nom in a_faire:
        source, prompt = tout[nom]
        print("\n  %s%s\n  %s" % (nom, " (retouche de %s)" % (source,) if source else "", prompt))
        corps = {"prompt": prompt, "aspect_ratio": "4:3", "resolution": "2K", "output_format": "png", "num_images": 1}
        modele = TEXTE
        if source:
            chemins = [PERSONNES[s] for s in source] if isinstance(source, list) else [os.path.join(DOSSIER, source + ".png")]
            if not all(os.path.exists(c) for c in chemins):
                print("  ATTENTE", nom, ": il faut d'abord", source)
                continue
            corps["image_urls"] = [O.deposer(c, "image/png", cle)[0] for c in chemins]
            modele = EDIT
        soum = O._json("https://queue.fal.run/" + modele, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            print("  ECHEC", nom, err)
            io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
                "%s\t%s\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), str(err).replace("\n", " ")))
            continue
        sortie = os.path.join(DOSSIER, nom + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
            "%s\t%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), PRIX))
        io.open(os.path.join(DOSSIER, nom + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": modele, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
