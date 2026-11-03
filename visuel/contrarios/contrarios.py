# -*- coding: utf-8 -*-
"""Les contraires, quatrieme « theme illustre » (3 nov. 2026) : des CHOSES et des lieux, pas des personnes. La fin
de la liste « Adjetivos comunes » du cours d'espagnol de Jacques (accord du 3 nov. : « go ») : ancho / estrecho,
abierto / cerrado, bueno / malo, raro, extrano, precioso, asqueroso, bonito / feo ; et grande / pequeno, nuevo /
viejo, lleno / vacio. ET C'EST FACTURE : 0,15 $ l'image, chez fal ; 18 images, 3 $ au plus avec les reprises.

    python visuel/contrarios/contrarios.py --json            # contrarios.json seul, gratuit
    python visuel/contrarios/contrarios.py --montrer         # les prompts seuls, gratuit
    python visuel/contrarios/contrarios.py                   # celles qui manquent (0,15 $ chacune)
    python visuel/contrarios/contrarios.py vaso-lleno        # celles-la seulement
    python visuel/contrarios/contrarios.py --refaire vaso-lleno   # l'ancienne passe en <nom>-rate<k>.png

UNE IMAGE PAR MOT, qu'on reconnait d'un coup d'oeil, et les paires se ressemblent (la meme porte ouverte puis
fermee, le meme verre plein puis vide : la seconde est une RETOUCHE de la premiere). Feo ne va JAMAIS sous le visage
d'une vraie personne (decision du 3 nov.) : un vase. Mark et Anna donnent l'echelle (la ruelle, les valises, la
porte), toujours par retouche de leur image de reference, jamais d'une description seule.
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/contrarios/img/ ; puis web.py (les webp).
"""
import hashlib, io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))

TEXTE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "contrarios", "img")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
PERSONNES = {"Mark": PRINCIPAL + "/personnages/Mark.png",
             "Anna": "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img/Anna-quotidien.png"}

# ---------------------------------------------------------------------------------------------------------------
# LES MOTS, la seule source (la page lit contrarios.json). es = [masculin, feminin], a la forme du corpus
# (espanol/datos/adjetivos.json) ; de = la forme du corpus (adjectif.json). contraire : la paire d'images de
# « lo contrario » / « das Gegenteil ». voisins : ce qui peut AUSSI se dire de la meme chose -- jamais un leurre
# l'un pour l'autre (une pomme pourrie est mala ET asquerosa ; raro et extrano sont presque synonymes).
MOTS = {
    "ancho":     {"es": ["ancho", "ancha"],         "de": "breit",       "contraire": "estrecho"},
    "estrecho":  {"es": ["estrecho", "estrecha"],   "de": "schmal",      "contraire": "ancho"},
    "abierto":   {"es": ["abierto", "abierta"],     "de": "offen",       "contraire": "cerrado"},
    "cerrado":   {"es": ["cerrado", "cerrada"],     "de": "geschlossen", "contraire": "abierto"},
    "grande":    {"es": ["grande", "grande"],       "de": "groß",        "contraire": "pequeno"},
    "pequeno":   {"es": ["pequeño", "pequeña"],     "de": "klein",       "contraire": "grande"},
    "nuevo":     {"es": ["nuevo", "nueva"],         "de": "neu",         "contraire": "viejo"},
    "viejo":     {"es": ["viejo", "vieja"],         "de": "alt",         "contraire": "nuevo"},
    "lleno":     {"es": ["lleno", "llena"],         "de": "voll",        "contraire": "vacio"},
    "vacio":     {"es": ["vacío", "vacía"],         "de": "leer",        "contraire": "lleno"},
    "bonito":    {"es": ["bonito", "bonita"],       "de": "schön",       "contraire": "feo", "voisins": ["precioso"]},
    "feo":       {"es": ["feo", "fea"],             "de": "hässlich",    "contraire": "bonito", "voisins": ["raro", "extrano"]},
    "bueno":     {"es": ["bueno", "buena"],         "de": "gut",         "contraire": "malo"},
    "malo":      {"es": ["malo", "mala"],           "de": "schlecht",    "contraire": "bueno", "voisins": ["asqueroso"]},
    "raro":      {"es": ["raro", "rara"],           "de": "komisch",     "voisins": ["extrano", "feo"]},
    "extrano":   {"es": ["extraño", "extraña"],     "de": "seltsam",     "voisins": ["raro", "feo"]},
    "precioso":  {"es": ["precioso", "preciosa"],   "de": "wunderschön", "voisins": ["bonito"]},
    "asqueroso": {"es": ["asqueroso", "asquerosa"], "de": "eklig",       "voisins": ["malo", "feo"]},
}
# ser ou estar : seulement les mots ou l'un des deux est seul juste. La taille et la largeur sont des qualites (es) ;
# ouvert, ferme, plein, vide sont des etats (esta). Pas bonito, viejo, precioso (« esta preciosa » se dit aussi), ni
# la nourriture (« el pastel es bueno » et « esta bueno » sont justes tous deux).
SER = ["ancho", "estrecho", "grande", "pequeno"]
ESTAR = ["abierto", "cerrado", "lleno", "vacio"]

# LES IMAGES : une par mot. objet : le nom espagnol et allemand, avec l'article ; verbe : celui de la phrase de la
# question en espagnol (es / esta) ; faux : les mots CLAIREMENT faux pour cette image, les seuls leurres permis et
# les seuls faux d'un « vrai ou faux » (une vieille bicyclette n'est pas forcement laide, une valise pas forcement
# neuve : ce qu'on ne voit pas sur l'image n'est jamais propose). source : une personne (retouche de son image) ou une image deja faite (la paire).
IMAGES = {
    "calle-ancha":      {"mot": "ancho", "es": ("la", "calle"), "de": ("die", "Straße"), "verbe": "es", "faux": ["estrecho", "pequeno", "feo", "raro", "extrano", "asqueroso"],
        "prompt": "A very wide, sunny city boulevard in an old European city: four lanes, wide pavements on both sides, a few people walking far away, trees in a row. Seen from the middle of the pavement at eye level, so its great width is obvious."},
    "calle-estrecha":   {"mot": "estrecho", "es": ("la", "calle"), "de": ("die", "Straße"), "verbe": "es", "faux": ["ancho", "grande", "nuevo", "raro", "extrano", "asqueroso"], "source": "Mark",
        # 3 nov. : la premiere prise, Mark en pied au fond de la ruelle, avait perdu ses boucles : on le rapproche
        "prompt": "He stands close to the camera in a very narrow old cobbled lane between tall stone houses in an old European town, seen from the knees up, his face large and clearly visible, with exactly his curly dark brown hair and his short beard from the reference: the lane is so narrow that he touches both walls with his outstretched hands, smiling."},
    "puerta-abierta":   {"mot": "abierto", "es": ("la", "puerta"), "de": ("die", "Tür"), "verbe": "está", "faux": ["cerrado", "raro", "extrano", "feo", "asqueroso"], "source": "Anna",
        "prompt": "She stands at the entrance of a house and holds a green wooden front door WIDE OPEN with one hand, welcoming, smiling; through the open door we clearly see the bright hallway inside. The whole door and the doorway are in the picture."},
    "puerta-cerrada":   {"mot": "cerrado", "es": ("la", "puerta"), "de": ("die", "Tür"), "verbe": "está", "faux": ["abierto", "raro", "extrano", "feo", "asqueroso"], "source": "puerta-abierta",
        "prompt": "Exactly the same house entrance and the same green wooden front door, the same light, the same framing, but now the door is completely CLOSED and nobody is there: no person in the picture. Nothing else changes."},
    "jarron-bonito":    {"mot": "bonito", "es": ("el", "jarrón"), "de": ("die", "Vase"), "verbe": "es", "faux": ["feo", "raro", "extrano", "asqueroso"],
        "prompt": "An elegant, beautiful porcelain vase with a slender, harmonious shape and a delicate blue floral pattern, holding a few fresh white tulips, on a light wooden table against a plain light grey wall. Soft daylight."},
    "jarron-feo":       {"mot": "feo", "es": ("el", "jarrón"), "de": ("die", "Vase"), "verbe": "es", "faux": ["bonito", "precioso"], "source": "jarron-bonito",
        "prompt": "The same light wooden table, the same plain light grey wall and the same light, but the vase is replaced by a really ugly vase: lopsided and lumpy, clumsy, in clashing garish colours (muddy brown, lime green and orange stripes), badly glued, with three wilted dry flowers. It must look ugly at first sight, but still clearly a vase."},
    "pastel-bueno":     {"mot": "bueno", "es": ("el", "pastel"), "de": ("der", "Kuchen"), "verbe": "está", "faux": ["malo", "asqueroso", "feo", "raro", "extrano"],
        "prompt": "A delicious-looking slice of homemade chocolate cake with fresh raspberries on a white plate, a fork beside it, one bite already taken, on a cafe table. Appetising, warm light, close-up."},
    "comida-asquerosa": {"mot": "asqueroso", "es": ("la", "comida"), "de": ("das", "Essen"), "verbe": "está", "faux": ["bueno", "bonito", "precioso"],
        "prompt": "A failed, disgusting meal on a white plate on a kitchen table: a grey, lumpy, burnt casserole, black at the edges, with an oily greenish sauce, smoke rising from it, a burnt pan behind. Clearly inedible and unappetising, but nothing rotten or gory."},
    "manzana-mala":     {"mot": "malo", "es": ("la", "manzana"), "de": ("der", "Apfel"), "verbe": "está", "faux": ["bueno", "bonito", "precioso", "nuevo"],
        "prompt": "One rotten apple on a light kitchen counter: wrinkled skin, large soft brown spots, a little white mould on one side. Close-up, plain light background, natural light. Clearly gone bad, not edible."},
    "tetera-rara":      {"mot": "raro", "es": ("la", "tetera"), "de": ("die", "Teekanne"), "verbe": "es", "faux": ["asqueroso", "precioso"],
        "prompt": "A very strange, odd teapot on a light wooden table: it has three spouts pointing in different directions and two handles, one of them on top. Plain white porcelain. Light grey wall behind, soft daylight. Funny and odd, not ugly."},
    "silla-extrana":    {"mot": "extrano", "es": ("la", "silla"), "de": ("der", "Stuhl"), "verbe": "es", "faux": ["asqueroso", "precioso"],
        "prompt": "A strange wooden chair standing in an empty, light room: its four legs all have very different lengths, so it stands crooked, and its backrest is twisted like a spiral. Plain light grey wall, wooden floor, soft daylight."},
    "vista-preciosa":   {"mot": "precioso", "es": ("la", "vista"), "de": ("die", "Aussicht"), "verbe": "es", "faux": ["feo", "asqueroso", "pequeno", "estrecho", "raro", "extrano", "malo"],
        "prompt": "A magnificent view from a hill over the red-tiled roofs and church towers of an old European town at sunset, a river shining in the warm golden light, the sky pink and orange. Breathtaking, wide, photographed from a terrace with a stone balustrade in the foreground."},
    "maleta-grande":    {"mot": "grande", "es": ("la", "maleta"), "de": ("der", "Koffer"), "verbe": "es", "faux": ["pequeno", "raro", "extrano", "asqueroso"], "source": "Mark",
        "prompt": "In a bright railway station hall, he pulls a HUGE suitcase on wheels, nearly as tall as his chest, with a funny, slightly exhausted look. Seen from head to feet."},
    "maleta-pequena":   {"mot": "pequeno", "es": ("la", "maleta"), "de": ("der", "Koffer"), "verbe": "es", "faux": ["grande", "ancho", "asqueroso"], "source": "Anna",
        "prompt": "In a bright railway station hall, she holds up a TINY suitcase, no bigger than a shoebox, by its little handle in one hand, smiling, amused. Seen from head to feet."},
    "bici-nueva":       {"mot": "nuevo", "es": ("la", "bicicleta"), "de": ("das", "Fahrrad"), "verbe": "es", "faux": ["viejo", "feo", "asqueroso", "malo", "raro", "extrano"],
        "prompt": "A brand-new, shiny blue city bicycle in a bright bicycle shop, a price tag still hanging from the handlebar (no readable text), the tyres clean, the chrome gleaming. Seen from the side, the whole bicycle in the picture."},
    "bici-vieja":       {"mot": "viejo", "es": ("la", "bicicleta"), "de": ("das", "Fahrrad"), "verbe": "es", "faux": ["nuevo", "bonito", "precioso", "raro", "extrano"],
        "prompt": "A very old, rusty bicycle leaning against a weathered brick wall in a courtyard: faded paint, rust on the frame, a torn saddle, a crooked basket, flat tyres. Seen from the side, the whole bicycle in the picture."},
    "vaso-lleno":       {"mot": "lleno", "es": ("el", "vaso"), "de": ("das", "Glas"), "verbe": "está", "faux": ["vacio", "raro", "extrano", "asqueroso", "feo"],
        "prompt": "A simple clear drinking glass filled to the brim with orange juice, on a light wooden table against a plain light grey wall. Centred, close-up, soft daylight."},
    "vaso-vacio":       {"mot": "vacio", "es": ("el", "vaso"), "de": ("das", "Glas"), "verbe": "está", "faux": ["lleno", "raro", "extrano", "asqueroso", "feo"], "source": "vaso-lleno",
        "prompt": "Exactly the same glass, the same table, the same wall and the same light, but the glass is now completely EMPTY and clean: not a drop inside. Nothing else changes."},
}
# Les mots de chaque nom en allemand, pour les terminaisons (« ein großer Koffer », « eine breite Straße »).
MEME = ("The same person as in the reference picture: exactly the same face, the same age, the same hair, the same skin, "
        "the same body and the same clothes. ")
PHOTO = (" A photorealistic photograph, natural light, natural colours, no text, no logos, no captions, no watermark. "
         "Landscape format. ")

# PLUS DE PHRASES QUE D'IMAGES : d'autres choses, sans image, pour ser / estar et l'accord (es), pour la terminaison
# (de). Toutes ecrites pour etre justes d'une seule facon. (mot, phrase avec ___, genre du nom)
PHRASES_ES = [
    ("ancho", "El pasillo {v} ___.", "m"), ("ancho", "Este río {v} muy ___.", "m"),
    ("estrecho", "La carretera {v} muy ___.", "f"), ("estrecho", "El puente {v} ___.", "m"),
    ("abierto", "La tienda {v} ___.", "f"), ("abierto", "La ventana {v} ___.", "f"), ("abierto", "El banco {v} ___.", "m"),
    ("cerrado", "El museo {v} ___.", "m"), ("cerrado", "La farmacia {v} ___.", "f"),
    ("grande", "La plaza {v} muy ___.", "f"), ("grande", "El parque {v} ___.", "m"),
    # des mots communs a l'Espagne et a l'Amerique latine : pas « el piso » (le plancher la-bas), ni « la nevera »
    ("pequeno", "El baño {v} ___.", "m"), ("pequeno", "La cocina {v} ___.", "f"),
    ("lleno", "El autobús {v} ___.", "m"), ("lleno", "La caja {v} ___.", "f"),
    ("vacio", "La botella {v} ___.", "f"), ("vacio", "El tren {v} ___.", "m"),
    # l'accord seulement (le verbe est donne)
    ("bonito", "La plaza es muy ___.", "f"), ("feo", "El edificio es bastante ___.", "m"),
    ("nuevo", "La casa es ___.", "f"), ("nuevo", "El sofá es ___.", "m"),
    ("viejo", "El puente es muy ___.", "m"), ("viejo", "La iglesia es muy ___.", "f"),
    ("precioso", "La playa es ___.", "f"), ("precioso", "El jardín es ___.", "m"),
    ("raro", "Este libro es muy ___.", "m"), ("extrano", "La situación es ___.", "f"),
    ("bueno", "La sopa está muy ___.", "f"), ("malo", "La leche está ___.", "f"),
    ("asqueroso", "El café de la máquina está ___.", "m"),
]
PHRASES_DE = [   # « Das ist ein / eine ___ X. » : (mot, article indefini, nom, genre)
    ("breit", "ein", "Fluss", "m"), ("schmal", "ein", "Weg", "m"), ("schmal", "eine", "Brücke", "f"),
    ("offen", "ein", "Fenster", "n"), ("geschlossen", "ein", "Fenster", "n"), ("schön", "ein", "Garten", "m"),
    ("hässlich", "ein", "Hemd", "n"), ("gut", "ein", "Restaurant", "n"), ("schlecht", "ein", "Film", "m"),
    ("eklig", "ein", "Geruch", "m"), ("komisch", "ein", "Geräusch", "n"), ("seltsam", "eine", "Frage", "f"),
    ("wunderschön", "ein", "Abend", "m"), ("groß", "ein", "Haus", "n"), ("klein", "eine", "Wohnung", "f"),
    ("neu", "ein", "Handy", "n"), ("alt", "eine", "Kirche", "f"), ("voll", "ein", "Bus", "m"), ("leer", "eine", "Flasche", "f"),
]

# LA DECOUVERTE : ce que dit chaque image, en toutes lettres. Les exemples du corpus quand l'image le permet (ils ont
# deja leur voix : « La calle es muy estrecha. », « Die Tür ist offen. »), sinon la phrase de la question.
DIT = {
    "es": {"calle-estrecha": "La calle es muy estrecha.", "puerta-abierta": "La puerta está abierta.", "vaso-lleno": "El vaso está lleno."},
    "de": {"calle-ancha": "Die Straße ist sehr breit.", "calle-estrecha": "Die Gasse ist eng und schmal.", "puerta-abierta": "Die Tür ist offen.",
           "pastel-bueno": "Der Kuchen schmeckt sehr gut."},
}
# L'ordre de la planche : les paires de contraires cote a cote, puis raro / extrano (presque synonymes), puis
# precioso et asqueroso.
PLANCHE = [["calle-ancha", "calle-estrecha"], ["puerta-abierta", "puerta-cerrada"], ["maleta-grande", "maleta-pequena"],
           ["bici-nueva", "bici-vieja"], ["vaso-lleno", "vaso-vacio"], ["jarron-bonito", "jarron-feo"],
           ["pastel-bueno", "manzana-mala"], ["tetera-rara", "silla-extrana"], ["vista-preciosa", "comida-asquerosa"]]

# LA TRADUCTION DES PHRASES (Jacques, 3 nov. : « Il n'y a pas la traduction française. Qui serait importante » ; le
# modele, visuel/THEMES-ILLUSTRES.md) : en francais, anglais, portugais, et en allemand pour qui apprend l'espagnol,
# la phrase entiere, sous la phrase juste apres la reponse et sous la phrase de la decouverte ; dans les autres
# langues, le mot et sa traduction du corpus. Chaque phrase de la page a la sienne, ecrite a la main.
# L'image et son mot : (fr, en, pt, de) -- « Der Kuchen ist gut. » comme « El pastel está bueno. »
TRAD_IMG = {
    "calle-ancha":      ("La rue est large.", "The street is wide.", "A rua é larga.", "Die Straße ist breit."),
    "calle-estrecha":   ("La rue est étroite.", "The street is narrow.", "A rua é estreita.", "Die Straße ist schmal."),
    "puerta-abierta":   ("La porte est ouverte.", "The door is open.", "A porta está aberta.", "Die Tür ist offen."),
    "puerta-cerrada":   ("La porte est fermée.", "The door is closed.", "A porta está fechada.", "Die Tür ist geschlossen."),
    "jarron-bonito":    ("Le vase est joli.", "The vase is pretty.", "O vaso é bonito.", "Die Vase ist schön."),
    "jarron-feo":       ("Le vase est laid.", "The vase is ugly.", "O vaso é feio.", "Die Vase ist hässlich."),
    "pastel-bueno":     ("Le gâteau est bon.", "The cake is good.", "O bolo está bom.", "Der Kuchen ist gut."),
    "comida-asquerosa": ("La nourriture est dégoûtante.", "The food is disgusting.", "A comida está nojenta.", "Das Essen ist eklig."),
    "manzana-mala":     ("La pomme est gâtée.", "The apple has gone bad.", "A maçã está estragada.", "Der Apfel ist schlecht."),
    "tetera-rara":      ("La théière est bizarre.", "The teapot is odd.", "O bule é estranho.", "Die Teekanne ist komisch."),
    "silla-extrana":    ("La chaise est étrange.", "The chair is strange.", "A cadeira é estranha.", "Der Stuhl ist seltsam."),
    "vista-preciosa":   ("La vue est magnifique.", "The view is beautiful.", "A vista é linda.", "Die Aussicht ist wunderschön."),
    "maleta-grande":    ("La valise est grande.", "The suitcase is big.", "A mala é grande.", "Der Koffer ist groß."),
    "maleta-pequena":   ("La valise est petite.", "The suitcase is small.", "A mala é pequena.", "Der Koffer ist klein."),
    "bici-nueva":       ("Le vélo est neuf.", "The bike is new.", "A bicicleta é nova.", "Das Fahrrad ist neu."),
    "bici-vieja":       ("Le vélo est vieux.", "The bike is old.", "A bicicleta é velha.", "Das Fahrrad ist alt."),
    "vaso-lleno":       ("Le verre est plein.", "The glass is full.", "O copo está cheio.", "Das Glas ist voll."),
    "vaso-vacio":       ("Le verre est vide.", "The glass is empty.", "O copo está vazio.", "Das Glas ist leer."),
}
# « Das ist ein großer Koffer. » (la terminaison, en allemand) : (fr, en, pt)
TRAD_ATTR = {
    "calle-ancha": ("C'est une rue large.", "It's a wide street.", "É uma rua larga."),
    "calle-estrecha": ("C'est une rue étroite.", "It's a narrow street.", "É uma rua estreita."),
    "puerta-abierta": ("C'est une porte ouverte.", "It's an open door.", "É uma porta aberta."),
    "puerta-cerrada": ("C'est une porte fermée.", "It's a closed door.", "É uma porta fechada."),
    "jarron-bonito": ("C'est un joli vase.", "It's a pretty vase.", "É um vaso bonito."),
    "jarron-feo": ("C'est un vase laid.", "It's an ugly vase.", "É um vaso feio."),
    "pastel-bueno": ("C'est un bon gâteau.", "It's a good cake.", "É um bolo bom."),
    "comida-asquerosa": ("C'est un plat dégoûtant.", "It's disgusting food.", "É uma comida nojenta."),
    "manzana-mala": ("C'est une pomme gâtée.", "It's a bad apple.", "É uma maçã estragada."),
    "tetera-rara": ("C'est une théière bizarre.", "It's an odd teapot.", "É um bule estranho."),
    "silla-extrana": ("C'est une chaise étrange.", "It's a strange chair.", "É uma cadeira estranha."),
    "vista-preciosa": ("C'est une vue magnifique.", "It's a beautiful view.", "É uma vista linda."),
    "maleta-grande": ("C'est une grande valise.", "It's a big suitcase.", "É uma mala grande."),
    "maleta-pequena": ("C'est une petite valise.", "It's a small suitcase.", "É uma mala pequena."),
    "bici-nueva": ("C'est un vélo neuf.", "It's a new bike.", "É uma bicicleta nova."),
    "bici-vieja": ("C'est un vieux vélo.", "It's an old bike.", "É uma bicicleta velha."),
    "vaso-lleno": ("C'est un verre plein.", "It's a full glass.", "É um copo cheio."),
    "vaso-vacio": ("C'est un verre vide.", "It's an empty glass.", "É um copo vazio."),
}
# Les phrases sans image, telles qu'elles s'affichent une fois completees : (fr, en, pt, de) et (fr, en, pt)
TRAD_PHRASES_ES = {
    "El pasillo es ancho.": ("Le couloir est large.", "The hallway is wide.", "O corredor é largo.", "Der Flur ist breit."),
    "Este río es muy ancho.": ("Ce fleuve est très large.", "This river is very wide.", "Este rio é muito largo.", "Dieser Fluss ist sehr breit."),
    "La carretera es muy estrecha.": ("La route est très étroite.", "The road is very narrow.", "A estrada é muito estreita.", "Die Landstraße ist sehr schmal."),
    "El puente es estrecho.": ("Le pont est étroit.", "The bridge is narrow.", "A ponte é estreita.", "Die Brücke ist schmal."),
    "La tienda está abierta.": ("Le magasin est ouvert.", "The shop is open.", "A loja está aberta.", "Das Geschäft ist geöffnet."),
    "La ventana está abierta.": ("La fenêtre est ouverte.", "The window is open.", "A janela está aberta.", "Das Fenster ist offen."),
    "El banco está abierto.": ("La banque est ouverte.", "The bank is open.", "O banco está aberto.", "Die Bank ist geöffnet."),
    "El museo está cerrado.": ("Le musée est fermé.", "The museum is closed.", "O museu está fechado.", "Das Museum ist geschlossen."),
    "La farmacia está cerrada.": ("La pharmacie est fermée.", "The pharmacy is closed.", "A farmácia está fechada.", "Die Apotheke ist geschlossen."),
    "La plaza es muy grande.": ("La place est très grande.", "The square is very big.", "A praça é muito grande.", "Der Platz ist sehr groß."),
    "El parque es grande.": ("Le parc est grand.", "The park is big.", "O parque é grande.", "Der Park ist groß."),
    "El baño es pequeño.": ("La salle de bain est petite.", "The bathroom is small.", "O banheiro é pequeno.", "Das Bad ist klein."),
    "La cocina es pequeña.": ("La cuisine est petite.", "The kitchen is small.", "A cozinha é pequena.", "Die Küche ist klein."),
    "El autobús está lleno.": ("Le bus est plein.", "The bus is full.", "O ônibus está cheio.", "Der Bus ist voll."),
    "La caja está llena.": ("La boîte est pleine.", "The box is full.", "A caixa está cheia.", "Die Kiste ist voll."),
    "La botella está vacía.": ("La bouteille est vide.", "The bottle is empty.", "A garrafa está vazia.", "Die Flasche ist leer."),
    "El tren está vacío.": ("Le train est vide.", "The train is empty.", "O trem está vazio.", "Der Zug ist leer."),
    "La plaza es muy bonita.": ("La place est très jolie.", "The square is very pretty.", "A praça é muito bonita.", "Der Platz ist sehr schön."),
    "El edificio es bastante feo.": ("Le bâtiment est assez laid.", "The building is rather ugly.", "O prédio é bem feio.", "Das Gebäude ist ziemlich hässlich."),
    "La casa es nueva.": ("La maison est neuve.", "The house is new.", "A casa é nova.", "Das Haus ist neu."),
    "El sofá es nuevo.": ("Le canapé est neuf.", "The sofa is new.", "O sofá é novo.", "Das Sofa ist neu."),
    "El puente es muy viejo.": ("Le pont est très vieux.", "The bridge is very old.", "A ponte é muito velha.", "Die Brücke ist sehr alt."),
    "La iglesia es muy vieja.": ("L'église est très vieille.", "The church is very old.", "A igreja é muito velha.", "Die Kirche ist sehr alt."),
    "La playa es preciosa.": ("La plage est magnifique.", "The beach is beautiful.", "A praia é linda.", "Der Strand ist wunderschön."),
    "El jardín es precioso.": ("Le jardin est magnifique.", "The garden is beautiful.", "O jardim é lindo.", "Der Garten ist wunderschön."),
    "Este libro es muy raro.": ("Ce livre est très bizarre.", "This book is very odd.", "Este livro é muito estranho.", "Dieses Buch ist sehr komisch."),
    "La situación es extraña.": ("La situation est étrange.", "The situation is strange.", "A situação é estranha.", "Die Situation ist seltsam."),
    "La sopa está muy buena.": ("La soupe est très bonne.", "The soup is very good.", "A sopa está muito boa.", "Die Suppe ist sehr gut."),
    "La leche está mala.": ("Le lait a tourné.", "The milk has gone off.", "O leite está estragado.", "Die Milch ist schlecht."),
    "El café de la máquina está asqueroso.": ("Le café de la machine est dégoûtant.", "The coffee from the machine is disgusting.", "O café da máquina está nojento.", "Der Kaffee aus dem Automaten ist eklig."),
}
TRAD_PHRASES_DE = {
    "Das ist ein breiter Fluss.": ("C'est un fleuve large.", "It's a wide river.", "É um rio largo."),
    "Das ist ein schmaler Weg.": ("C'est un chemin étroit.", "It's a narrow path.", "É um caminho estreito."),
    "Das ist eine schmale Brücke.": ("C'est un pont étroit.", "It's a narrow bridge.", "É uma ponte estreita."),
    "Das ist ein offenes Fenster.": ("C'est une fenêtre ouverte.", "It's an open window.", "É uma janela aberta."),
    "Das ist ein geschlossenes Fenster.": ("C'est une fenêtre fermée.", "It's a closed window.", "É uma janela fechada."),
    "Das ist ein schöner Garten.": ("C'est un beau jardin.", "It's a beautiful garden.", "É um jardim bonito."),
    "Das ist ein hässliches Hemd.": ("C'est une chemise laide.", "It's an ugly shirt.", "É uma camisa feia."),
    "Das ist ein gutes Restaurant.": ("C'est un bon restaurant.", "It's a good restaurant.", "É um bom restaurante."),
    "Das ist ein schlechter Film.": ("C'est un mauvais film.", "It's a bad film.", "É um filme ruim."),
    "Das ist ein ekliger Geruch.": ("C'est une odeur dégoûtante.", "It's a disgusting smell.", "É um cheiro nojento."),
    "Das ist ein komisches Geräusch.": ("C'est un bruit bizarre.", "It's a strange noise.", "É um barulho estranho."),
    "Das ist eine seltsame Frage.": ("C'est une question étrange.", "It's a strange question.", "É uma pergunta estranha."),
    "Das ist ein wunderschöner Abend.": ("C'est une soirée magnifique.", "It's a wonderful evening.", "É uma noite maravilhosa."),
    "Das ist ein großes Haus.": ("C'est une grande maison.", "It's a big house.", "É uma casa grande."),
    "Das ist eine kleine Wohnung.": ("C'est un petit appartement.", "It's a small flat.", "É um apartamento pequeno."),
    "Das ist ein neues Handy.": ("C'est un téléphone neuf.", "It's a new phone.", "É um celular novo."),
    "Das ist eine alte Kirche.": ("C'est une vieille église.", "It's an old church.", "É uma igreja antiga."),
    "Das ist ein voller Bus.": ("C'est un bus plein.", "It's a full bus.", "É um ônibus cheio."),
    "Das ist eine leere Flasche.": ("C'est une bouteille vide.", "It's an empty bottle.", "É uma garrafa vazia."),
}
# les phrases de la decouverte prises au corpus, qui ne sont pas celles des questions
TRAD_DIT = {
    "es": {"La calle es muy estrecha.": ("La rue est très étroite.", "The street is very narrow.", "A rua é muito estreita.", "Die Straße ist sehr schmal.")},
    "de": {"Die Straße ist sehr breit.": ("La rue est très large.", "The street is very wide.", "A rua é muito larga."),
           "Die Gasse ist eng und schmal.": ("La ruelle est étroite et resserrée.", "The alley is tight and narrow.", "A viela é apertada e estreita."),
           "Der Kuchen schmeckt sehr gut.": ("Le gâteau est très bon.", "The cake tastes very good.", "O bolo está muito gostoso.")},
}

# Les trois mots qui n'etaient pas au corpus (asqueroso en espagnol, eklig et geschlossen en allemand) : leur
# traduction, en attendant qu'ils y entrent (espanol/ajouts/contrarios.json, adjectif.json).
AJOUTS_TRAD = {
    "es": {"asqueroso": {"fr": "dégoûtant", "en": "disgusting", "pt": "nojento", "ar": "مقزز", "de": "eklig, widerlich"}},
    "de": {"eklig": {"fr": "dégoûtant", "en": "disgusting", "tr": "iğrenç", "uk": "огидний", "fa": "چندش‌آور", "ar": "مقزز",
                     "pt": "nojento", "pl": "obrzydliwy", "ru": "отвратительный"},
           "geschlossen": {"fr": "fermé", "en": "closed", "tr": "kapalı", "uk": "зачинений", "fa": "بسته", "ar": "مغلق",
                           "pt": "fechado", "pl": "zamknięty", "ru": "закрытый"}},
}
LANGUES = {"es": ["fr", "en", "pt", "ar", "de"], "de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]}


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def traductions():
    """La traduction de chaque mot dans les langues d'interface, prise au corpus (traduction, traduction_<langue>)."""
    out = {"es": {}, "de": {}}
    for langue, fichier, cle in (("es", "espanol/datos/adjetivos.json", lambda m: m["es"][0]), ("de", "adjectif.json", lambda m: m["de"])):
        corpus = {}
        for liste in json.load(io.open(os.path.join(RACINE, fichier), encoding="utf-8")).values():
            for e in liste:
                corpus.setdefault(e["mot"], e)
        for k, m in MOTS.items():
            mot = cle(m)
            e = corpus.get(mot)
            if e:
                out[langue][k] = {l: e.get("traduction" if l == "fr" else "traduction_" + l) for l in LANGUES[langue]}
            elif mot in AJOUTS_TRAD[langue]:
                out[langue][k] = AJOUTS_TRAD[langue][mot]
            else:
                sys.exit("  %s absent du corpus %s et des ajouts" % (mot, langue))
            manque = [l for l, v in out[langue][k].items() if not v]
            if manque:
                sys.exit("  %s (%s) : pas de traduction en %s" % (mot, langue, ", ".join(manque)))
    return out


def forme_es(mot, genre):
    return MOTS[mot]["es"][1 if genre in ("f", "la") else 0]


def phrase_es(i):
    im = IMAGES[i]
    art, nom = im["es"]
    return "%s %s %s %s." % (art.capitalize(), nom, im["verbe"], forme_es(im["mot"], art))


def phrase_de(i):
    im = IMAGES[i]
    art, nom = im["de"]
    return "%s %s ist %s." % (art.capitalize(), nom, MOTS[im["mot"]]["de"])


ENDUNG = {"der": "er", "die": "e", "das": "es", "m": "er", "f": "e", "n": "es"}
ARTDE = {"der": "ein", "die": "eine", "das": "ein"}


def phrases_traduites(dit):
    """{es: {phrase: {fr, en, pt, de}}, de: {phrase: {fr, en, pt}}} : chaque phrase que la page peut montrer juste,
    a la lettre pres comme elle l'affiche ; une phrase sans traduction arrete le script."""
    es, de = {}, {}
    for i, t in TRAD_IMG.items():
        es[phrase_es(i)] = dict(zip(("fr", "en", "pt", "de"), t))
        de[phrase_de(i)] = dict(zip(("fr", "en", "pt"), t[:3]))
        art, nom = IMAGES[i]["de"]
        de["Das ist %s %s%s %s." % (ARTDE[art], MOTS[IMAGES[i]["mot"]]["de"], ENDUNG[art], nom)] = dict(zip(("fr", "en", "pt"), TRAD_ATTR[i]))
    for k, s, g in PHRASES_ES:
        v = "está" if k in ESTAR or k in ("bueno", "malo", "asqueroso") else "es"
        p = s.replace("{v}", v).replace("___", forme_es(k, g))
        if p not in TRAD_PHRASES_ES:
            sys.exit("  sans traduction : " + p)
        es[p] = dict(zip(("fr", "en", "pt", "de"), TRAD_PHRASES_ES[p]))
    for m, art, nom, g in PHRASES_DE:
        p = "Das ist %s %s%s %s." % (art, m, ENDUNG[g], nom)
        if p not in TRAD_PHRASES_DE:
            sys.exit("  sans traduction : " + p)
        de[p] = dict(zip(("fr", "en", "pt"), TRAD_PHRASES_DE[p]))
    for l, cible in (("es", es), ("de", de)):
        for p, t in TRAD_DIT[l].items():
            cible[p] = dict(zip(("fr", "en", "pt", "de"), t))
        manque = [p for p in dit[l].values() if p not in cible]
        if manque:
            sys.exit("  decouverte sans traduction : " + ", ".join(manque))
    return {"es": es, "de": de}


def ecrire_json():
    dit = {"es": {}, "de": {}}
    for i in IMAGES:
        dit["es"][i] = DIT["es"].get(i) or phrase_es(i)
        dit["de"][i] = DIT["de"].get(i) or phrase_de(i)
    for k, m in MOTS.items():
        if m.get("contraire") and MOTS[m["contraire"]].get("contraire") != k:
            sys.exit("  contraire boiteux : " + k)
    if sorted(im["mot"] for im in IMAGES.values()) != sorted(MOTS):
        sys.exit("  une image par mot : il en manque ou il y en a deux")
    d = {"mots": MOTS, "ser": SER, "estar": ESTAR,
         "images": {i: {k: v for k, v in im.items() if k not in ("prompt", "source")} for i, im in IMAGES.items()},
         "phrasesEs": PHRASES_ES, "phrasesDe": PHRASES_DE, "planche": PLANCHE, "dit": dit, "trad": traductions()}
    # ce que la page peut dire, et l'identifiant de son fichier (sha1 du texte, comme audio/manifest.py) : les phrases
    # de la decouverte et les mots cles a leurs deux formes ; sans fichier, la voix du telephone
    a_dire = {"es": list(dit["es"].values()) + [f for m in MOTS.values() for f in m["es"]],
              "de": list(dit["de"].values()) + [m["de"] for m in MOTS.values()]}
    d["sons"] = {l: {t: identifiant(t) for t in dict.fromkeys(v)} for l, v in a_dire.items()}
    d["phrasesTrad"] = phrases_traduites(dit)
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    for chemin in (os.path.join(ICI, "contrarios.json"), os.path.join(RACINE, "visuel", "prototype", "contrarios", "contrarios.json")):
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(texte)
    return d


def textes_a_dire(langue):
    """Pour les inventaires des voix (audio/manifest.py, manifest_es.py) : les phrases de la decouverte (es, de ;
    l'espagnol d'Amerique latine dit les memes) et les mots cles a leurs deux formes."""
    d = json.load(io.open(os.path.join(ICI, "contrarios.json"), encoding="utf-8"))
    l = "de" if langue == "de" else "es"
    mots = [m["de"] for m in d["mots"].values()] if l == "de" else [f for m in d["mots"].values() for f in m["es"]]
    return list(dict.fromkeys(list(d["dit"][l].values()) + mots))


def images():
    out = {}
    for i, im in IMAGES.items():
        src = im.get("source")
        prompt = (MEME if src in PERSONNES else "") + PHOTO + im["prompt"]
        out[i] = (src, prompt)
    return out


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    ecrire_json()
    if "--json" in sys.argv:
        return
    import omnihuman as O                                    # noqa: E402
    tout = images()
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or list(tout)
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
    # une image qui en retouche une autre passe apres elle (la porte fermee apres l'ouverte)
    a_faire.sort(key=lambda n: tout[n][0] in IMAGES)
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if not montrer and not os.environ.get("FAL_KEY") and not os.path.exists(os.path.join(RACINE, "fal.secret")):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = None if montrer else O.cle()
    for nom in a_faire:
        source, prompt = tout[nom]
        print("\n  %s%s\n  %s" % (nom, " (retouche de %s)" % source if source else "", prompt))
        if montrer:
            continue
        corps = {"prompt": prompt, "aspect_ratio": "4:3", "resolution": "2K", "output_format": "png", "num_images": 1}
        modele = TEXTE
        if source:
            chemin = PERSONNES.get(source) or os.path.join(DOSSIER, source + ".png")
            if not os.path.exists(chemin):
                print("  ATTENTE", nom, ": il faut d'abord", source)
                continue
            corps["image_urls"] = [O.deposer(chemin, "image/png", cle)[0]]
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
            "prompt": prompt, "source": source, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
