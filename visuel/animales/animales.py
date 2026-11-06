# -*- coding: utf-8 -*-
"""Les animaux, theme illustre de la vague 2 (3 nov. 2026, decisions/DECISIONS.md : « Plutot 5 autres themes »).
LA SEULE SOURCE du theme : les animaux, ou ils vivent, ce qu'ils mangent, leur couleur et leur taille, toutes les
phrases (es, de) et leurs traductions (fr, en, pt ; de pour qui apprend l'espagnol), et les prompts des images.

    python visuel/animales/animales.py --json         # animales.json seul, gratuit
    python visuel/animales/animales.py --montrer      # les prompts, gratuit
    python visuel/animales/animales.py --provisoires  # des images dessinees pour essayer la page, gratuit
    python visuel/animales/animales.py --chat         # Moritz, recadre d'une image du chat deja payee, gratuit
    python visuel/animales/animales.py --webp         # les webp de la page, depuis les originaux
    python visuel/animales/animales.py --planche      # une planche de controle des originaux, gratuit
    python visuel/animales/animales.py --payer kuh fuchs ...   # FACTURE : 0,15 $ l'image (fal, nano-banana-pro)
    python visuel/animales/animales.py --payer --refaire kuh   # l'ancienne passe en <nom>-rate<k>.png

LA REGLE 2 DES THEMES (pas de theme qui refait une scene) : la ferme a deja sa scene (bauernhof), ou l'on nomme les
animaux en les touchant. Ici, un autre angle : le genre et le pluriel (der / die / das compte), ou ils vivent (la
ferme, la foret, la mer, la maison), ce qu'ils mangent, leur couleur et leur taille. Les animaux de la ferme SONT
ceux de la scene (la ferme de l'oncle d'Anna, dans le Brandebourg, un matin d'automne) : les images en sont des
retouches, la scene en reference, pour que tout reste coherent (decision du 3 nov., « la continuite des lieux ») ;
le chat est Moritz, chez Ben et Mia (le theme « Ou est le chat ? »), recadre d'une image deja payee.
UNE IMAGE NE DIT QUE CE QU'ELLE MONTRE : la couleur et le nombre d'animaux se relevent sur l'image avant publication ;
un leurre n'est jamais qu'une valeur clairement fausse (un chien mange aussi a la maison, un chat vit aussi a la
ferme : AUSSI, jamais proposes en leurre).
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/animales/img/.
"""
import hashlib, io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype", "animales")
sys.path.insert(0, os.path.join(RACINE, "video"))

TEXTE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15
PLAFOND = 2.50              # tout le theme, reprises comprises (le solde fal est partage entre six chantiers)
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "animales", "img")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FERME = PRINCIPAL + "/visuel/scenes/bauernhof.png"                         # la scene, la reference des retouches
SALON = PRINCIPAL + "/.claude/worktrees/themes-prepositions-b7f26b/visuel/gato/img"   # le salon de Jan et Katrin

# ---------------------------------------------------------------------------------------------------------------
# LES LIEUX : la forme de la phrase (« auf dem Bauernhof », « en la granja ») et le mot du corpus
HABITATS = {
    "bauernhof": {"de": "auf dem Bauernhof", "es": "en la granja", "motDe": ["Bauernhof", "der"], "motEs": ["granja", "la"],
                  "fr": "à la ferme", "en": "on the farm", "pt": "na fazenda"},
    "wald":      {"de": "im Wald", "es": "en el bosque", "motDe": ["Wald", "der"], "motEs": ["bosque", "el"],
                  "fr": "dans la forêt", "en": "in the forest", "pt": "na floresta"},
    "meer":      {"de": "im Meer", "es": "en el mar", "motDe": ["Meer", "das"], "motEs": ["mar", "el"],
                  "fr": "dans la mer", "en": "in the sea", "pt": "no mar"},
    "haus":      {"de": "im Haus", "es": "en casa", "motDe": ["Haus", "das"], "motEs": ["casa", "la"],
                  "fr": "à la maison", "en": "at home", "pt": "em casa"},
}
# CE QU'ILS MANGENT : « Die Kuh frisst Gras. » (fressen, pas essen : un animal), « La vaca come hierba. » ; le poisson
# qu'on mange est el pescado (el pez est vivant), en allemand c'est le meme mot, der Fisch.
ALIMENTS = {
    "gras":    {"de": "Gras", "es": "hierba", "motDe": ["Gras", "das"], "motEs": ["hierba", "la"],
                "fr": "de l'herbe", "en": "grass", "pt": "capim"},
    "fleisch": {"de": "Fleisch", "es": "carne", "motDe": ["Fleisch", "das"], "motEs": ["carne", "la"],
                "fr": "de la viande", "en": "meat", "pt": "carne"},
    "fisch":   {"de": "Fisch", "es": "pescado", "motDe": ["Fisch", "der"], "motEs": ["pescado", "el"],
                "fr": "du poisson", "en": "fish", "pt": "peixe"},
    "nuss":    {"de": "Nüsse", "es": "nueces", "motDe": ["Nuss", "die"], "motEs": ["nuez", "la"],
                "fr": "des noix", "en": "nuts", "pt": "nozes"},
}
# LES COULEURS : de (apres sein), deAttr (devant le nom, avec terminaison ; None quand elle ne se decline pas bien :
# orange, rosa), es [masculin, feminin], fr [m, f], en, pt [m, f]
COULEURS = {
    "noir-blanc": {"de": "schwarz und weiß", "deAttr": "schwarz-weiß", "es": ["blanco y negro", "blanca y negra"],
                   "fr": ["noir et blanc", "noire et blanche"], "en": "black and white", "pt": ["preto e branco", "preta e branca"]},
    "brun":       {"de": "braun", "deAttr": "braun", "es": ["marrón", "marrón"], "fr": ["marron", "marron"], "en": "brown", "pt": ["marrom", "marrom"]},
    "rose":       {"de": "rosa", "deAttr": None, "es": ["rosa", "rosa"], "fr": ["rose", "rose"], "en": "pink", "pt": ["rosa", "rosa"]},
    "blanc":      {"de": "weiß", "deAttr": "weiß", "es": ["blanco", "blanca"], "fr": ["blanc", "blanche"], "en": "white", "pt": ["branco", "branca"]},
    "gris":       {"de": "grau", "deAttr": "grau", "es": ["gris", "gris"], "fr": ["gris", "grise"], "en": "gray", "pt": ["cinza", "cinza"]},
    "orange":     {"de": "orange", "deAttr": None, "es": ["naranja", "naranja"], "fr": ["orange", "orange"], "en": "orange", "pt": ["laranja", "laranja"]},
    "bleu-jaune": {"de": "blau und gelb", "deAttr": None, "es": ["azul y amarillo", "azul y amarilla"], "fr": ["bleu et jaune", "bleue et jaune"],
                   "en": "blue and yellow", "pt": ["azul e amarelo", "azul e amarela"]},
}
# les mots du corpus de chaque couleur (pour le mot choisi traduit) : de, es (masculin)
COULEURS_MOTS = {"noir-blanc": (["schwarz", "weiß"], ["negro", "blanco"]), "brun": (["braun"], ["marrón"]), "rose": (["rosa"], ["rosa"]),
                 "blanc": (["weiß"], ["blanco"]), "gris": (["grau"], ["gris"]), "orange": (["orange"], ["naranja"]),
                 "bleu-jaune": (["blau", "gelb"], ["azul", "amarillo"])}

# ---------------------------------------------------------------------------------------------------------------
# LES ANIMAUX. de / es : [article, nom, pluriel] a la forme du corpus (themes.json, espanol/datos/temas.json) ;
# fr / en / pt : [le nom defini, le pluriel defini, le nom indefini, genre (m / f)] pour les traductions ;
# ou : ou il vit (None : nulle part d'unique -- un oiseau, une souris vivent partout -- et pas de question « ou ») ;
# aussi : les lieux ou il vit AUSSI, jamais en leurre ; mange : ce qu'il mange (vrai) ; non : ce qu'il ne mange
# clairement pas, les seuls leurres ; taille : 1 (un oiseau) a 5 (un cheval), on ne compare qu'a deux crans d'ecart ;
# couleur : relevee sur l'image ; aussiCouleur : ce qui peut aussi se dire (un renard roux est rot en allemand) ;
# nombre : combien on en voit sur l'image (3, ou « viele » pour un banc de poissons) ; plFaux : trois pluriels
# faux, des fautes d'apprenant (jamais une autre forme juste : pas « Kühen », datif pluriel).
ANIMAUX = {
    "kuh":     {"de": ["die", "Kuh", "Kühe"], "es": ["la", "vaca", "vacas"],
                "fr": ["la vache", "les vaches", "une vache", "f"], "en": ["the cow", "the cows", "a cow", "cows"], "pt": ["a vaca", "as vacas", "uma vaca", "f"],
                "ou": "bauernhof", "aussi": [], "mange": ["gras"], "non": ["fleisch", "fisch", "nuss"], "taille": 5, "couleur": "noir-blanc", "nombre": 1,
                "plFaux": {"de": ["Kuhe", "Kuhs", "Küher"], "es": ["vacaes", "vaca", "vacás"]}},
    "pferd":   {"de": ["das", "Pferd", "Pferde"], "es": ["el", "caballo", "caballos"],
                "fr": ["le cheval", "les chevaux", "un cheval", "m"], "en": ["the horse", "the horses", "a horse", "horses"], "pt": ["o cavalo", "os cavalos", "um cavalo", "m"],
                "ou": "bauernhof", "aussi": [], "mange": ["gras"], "non": ["fleisch", "fisch"], "taille": 5, "couleur": "brun", "nombre": 1,
                "plFaux": {"de": ["Pferder", "Pferds", "Pfärde"], "es": ["caballoes", "caballo", "caballós"]}},
    "schwein": {"de": ["das", "Schwein", "Schweine"], "es": ["el", "cerdo", "cerdos"],
                "fr": ["le cochon", "les cochons", "un cochon", "m"], "en": ["the pig", "the pigs", "a pig", "pigs"], "pt": ["o porco", "os porcos", "um porco", "m"],
                "ou": "bauernhof", "aussi": [], "mange": [], "non": [], "taille": 4, "couleur": "rose", "nombre": 1,
                "plFaux": {"de": ["Schweiner", "Schwein", "Schweins"], "es": ["cerdoes", "cerdo", "cerdós"]}},
    "schaf":   {"de": ["das", "Schaf", "Schafe"], "es": ["la", "oveja", "ovejas"],
                "fr": ["le mouton", "les moutons", "un mouton", "m"], "en": ["the sheep", "the sheep", "a sheep", "sheep"], "pt": ["a ovelha", "as ovelhas", "uma ovelha", "f"],
                "ou": "bauernhof", "aussi": [], "mange": ["gras"], "non": ["fleisch", "fisch", "nuss"], "taille": 4, "couleur": "blanc", "nombre": 3,
                "plFaux": {"de": ["Schäfe", "Schafer", "Schafs"], "es": ["ovejaes", "oveja", "ovejás"]}},
    "huhn":    {"de": ["das", "Huhn", "Hühner"], "es": ["la", "gallina", "gallinas"],
                "fr": ["la poule", "les poules", "une poule", "f"], "en": ["the hen", "the hens", "a hen", "hens"], "pt": ["a galinha", "as galinhas", "uma galinha", "f"],
                "ou": "bauernhof", "aussi": [], "mange": [], "non": [], "taille": 2, "couleur": "brun", "nombre": 3,
                "plFaux": {"de": ["Huhne", "Hühne", "Huhns"], "es": ["gallinaes", "gallina", "gallinás"]}},
    "hund":    {"de": ["der", "Hund", "Hunde"], "es": ["el", "perro", "perros"],
                "fr": ["le chien", "les chiens", "un chien", "m"], "en": ["the dog", "the dogs", "a dog", "dogs"], "pt": ["o cachorro", "os cachorros", "um cachorro", "m"],
                "ou": "bauernhof", "aussi": ["haus"], "mange": ["fleisch"], "non": ["gras", "nuss"], "taille": 3, "couleur": "noir-blanc", "nombre": 1,
                "plFaux": {"de": ["Hünde", "Hunder", "Hunds"], "es": ["perroes", "perro", "perrós"]}},
    "katze":   {"de": ["die", "Katze", "Katzen"], "es": ["el", "gato", "gatos"],
                "fr": ["le chat", "les chats", "un chat", "m"], "en": ["the cat", "the cats", "a cat", "cats"], "pt": ["o gato", "os gatos", "um gato", "m"],
                "ou": "haus", "aussi": ["bauernhof"], "mange": ["fleisch", "fisch"], "non": ["gras", "nuss"], "taille": 2, "couleur": "noir-blanc", "nombre": 1,
                "plFaux": {"de": ["Katzes", "Kätze", "Katze"], "es": ["gatoes", "gato", "gatós"]}},
    "goldfisch": {"de": ["der", "Goldfisch", "Goldfische"], "es": ["el", "pez de colores", "peces de colores"],
                "fr": ["le poisson rouge", "les poissons rouges", "un poisson rouge", "m"], "en": ["the goldfish", "the goldfish", "a goldfish", "goldfish"],
                "pt": ["o peixinho dourado", "os peixinhos dourados", "um peixinho dourado", "m"],
                "ou": "haus", "aussi": [], "mange": [], "non": [], "taille": 1, "couleur": "orange", "nombre": 1,
                "plFaux": {"de": ["Goldfischen", "Goldfischs", "Goldfischer"], "es": ["pezes de colores", "pez de colores", "peces de color"]}},
    "baer":    {"de": ["der", "Bär", "Bären"], "es": ["el", "oso", "osos"],
                "fr": ["l'ours", "les ours", "un ours", "m"], "en": ["the bear", "the bears", "a bear", "bears"], "pt": ["o urso", "os ursos", "um urso", "m"],
                "ou": "wald", "aussi": [], "mange": ["fisch"], "non": [], "taille": 5, "couleur": "brun", "nombre": 1,
                "plFaux": {"de": ["Bäre", "Bärs", "Bärer"], "es": ["osoes", "oso", "osós"]}},
    "fuchs":   {"de": ["der", "Fuchs", "Füchse"], "es": ["el", "zorro", "zorros"],
                "fr": ["le renard", "les renards", "un renard", "m"], "en": ["the fox", "the foxes", "a fox", "foxes"], "pt": ["a raposa", "as raposas", "uma raposa", "f"],
                "ou": "wald", "aussi": [], "mange": ["fleisch"], "non": ["gras"], "taille": 3, "couleur": "orange", "aussiCouleur": ["brun"], "nombre": 1,
                "frCouleur": "roux", "plFaux": {"de": ["Fuchse", "Fuchsen", "Füchser"], "es": ["zorroes", "zorro", "zorrós"]}},
    "eichhoernchen": {"de": ["das", "Eichhörnchen", "Eichhörnchen"], "es": ["la", "ardilla", "ardillas"],
                "fr": ["l'écureuil", "les écureuils", "un écureuil", "m"], "en": ["the squirrel", "the squirrels", "a squirrel", "squirrels"], "pt": ["o esquilo", "os esquilos", "um esquilo", "m"],
                "ou": "wald", "aussi": [], "mange": ["nuss"], "non": ["fleisch", "fisch", "gras"], "taille": 1, "couleur": "brun", "aussiCouleur": ["orange"], "nombre": 1,
                "plFaux": {"de": ["Eichhörnchens", "Eichhörnchenen", "Eichhörncher"], "es": ["ardillaes", "ardilla", "ardillás"]}},
    "vogel":   {"de": ["der", "Vogel", "Vögel"], "es": ["el", "pájaro", "pájaros"],
                "fr": ["l'oiseau", "les oiseaux", "un oiseau", "m"], "en": ["the bird", "the birds", "a bird", "birds"], "pt": ["o pássaro", "os pássaros", "um pássaro", "m"],
                "ou": None, "aussi": [], "mange": [], "non": [], "taille": 1, "couleur": "bleu-jaune", "nombre": 1,
                "plFaux": {"de": ["Vogels", "Vogeln", "Vögels"], "es": ["pájaroes", "pájaro", "pajaros"]}},
    "fisch":   {"de": ["der", "Fisch", "Fische"], "es": ["el", "pez", "peces"],
                "fr": ["le poisson", "les poissons", "un poisson", "m"], "en": ["the fish", "the fish", "a fish", "fish"], "pt": ["o peixe", "os peixes", "um peixe", "m"],
                "ou": "meer", "aussi": [], "mange": [], "non": [], "taille": 1, "couleur": None, "nombre": "viele",
                "plFaux": {"de": ["Fischs", "Fischen", "Füsche"], "es": ["pezes", "pezs", "pez"]}},
    "delfin":  {"de": ["der", "Delfin", "Delfine"], "es": ["el", "delfín", "delfines"],
                "fr": ["le dauphin", "les dauphins", "un dauphin", "m"], "en": ["the dolphin", "the dolphins", "a dolphin", "dolphins"], "pt": ["o golfinho", "os golfinhos", "um golfinho", "m"],
                "ou": "meer", "aussi": [], "mange": ["fisch"], "non": ["gras", "nuss"], "taille": 5, "couleur": "gris", "nombre": 1,
                "plFaux": {"de": ["Delfinen", "Delfins", "Delfiner"], "es": ["delfíns", "delfínes", "delfín"]}},
    "maus":    {"de": ["die", "Maus", "Mäuse"], "es": ["el", "ratón", "ratones"],
                "fr": ["la souris", "les souris", "une souris", "f"], "en": ["the mouse", "the mice", "a mouse", "mice"], "pt": ["o rato", "os ratos", "um rato", "m"],
                "ou": None, "aussi": [], "mange": [], "non": [], "taille": 1, "couleur": "gris", "nombre": 1,
                "plFaux": {"de": ["Mause", "Mäuser", "Mausen"], "es": ["ratóns", "ratónes", "ratón"]}},
}
# L'ordre de la decouverte : par lieu, la souris avec la ferme (sa grange) et l'oiseau avec la foret (sa branche)
GROUPES = [("bauernhof", ["kuh", "pferd", "schwein", "schaf", "huhn", "hund", "maus"]),
           ("haus", ["katze", "goldfisch"]),
           ("wald", ["baer", "fuchs", "eichhoernchen", "vogel"]),
           ("meer", ["fisch", "delfin"])]

# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES (4:3, 2K). source : FERME (la scene, retouchee), SALON (la piece du chat, retouchee), "chat" (Moritz,
# recadre gratuitement) ou rien (texte -> image). Chaque prompt dit la couleur et le nombre que la donnee annonce.
PHOTO = (" A photorealistic photograph, natural light, natural colours, sharp, no text, no logos, no watermark, "
         "landscape format. The whole animal is in the picture, from head to tail, and fills a good part of the frame. ")
MEME_FERME = ("The same farm as in the reference picture (the uncle's farm in Brandenburg, the same autumn morning light, the same "
              "red-brick farmhouse and barn, the same wooden fences). Now a closer photograph of ONE part of the farm, with no people: ")
IMAGES = {
    "kuh":     {"source": "ferme", "prompt": "the same black-and-white Holstein cow, alone in the frame, grazing on the green meadow behind the wooden fence, its head down eating grass, seen from the side."},
    "pferd":   {"source": "ferme", "prompt": "the same chestnut-brown horse with a white blaze on its forehead, standing in the paddock behind the wooden fence and eating grass, seen from the side."},
    "schwein": {"source": "ferme", "prompt": "the same pink pig with a few brown spots, standing in its muddy pen, looking at the camera."},
    "schaf":   {"source": "ferme", "prompt": "exactly THREE white sheep, no more, grazing together on the green hill meadow, all three entirely visible and clearly separate."},
    "huhn":    {"source": "ferme", "prompt": "exactly THREE brown hens, no more, pecking grain on the sandy farmyard, all three entirely visible and clearly separate."},
    "hund":    {"source": "ferme", "prompt": "the same black-and-white border collie, lying on the sandy farmyard in the sun, head up, looking at the camera."},
    "maus":    {"source": None, "prompt": "A small grey house mouse sitting on the old wooden floor of a farm barn, next to a little heap of straw, seen from the side, close-up at the mouse's height."},
    "katze":   {"source": "chat", "prompt": "(gratuit) Moritz, le chat noir et blanc de Ben et Mia, couche sur le canape gris (gato/sofa-auf), recadre."},
    "goldfisch": {"source": "salon", "prompt": "Exactly the same living room as in the reference picture, seen closer: on the light wooden dining table stands a round glass goldfish bowl with clear water, a little gravel and ONE orange goldfish swimming in it. The table and the bowl fill the lower half of the picture; behind, softly out of focus, the same white walls and light grey sofa. No people, no cat."},
    "baer":    {"source": None, "prompt": "A large brown bear walking on the moss among tall pine and beech trees in a green European forest, seen from the side."},
    "fuchs":   {"source": None, "prompt": "A red fox with bright orange fur, a white chest and a long bushy tail, standing among ferns and fallen leaves in a European forest, looking at the camera."},
    "eichhoernchen": {"source": None, "prompt": "A red-brown European squirrel with tufted ears sitting on a mossy tree trunk in the forest, holding a hazelnut in its front paws and eating it. Close-up, the whole squirrel and its tail in the picture."},
    "vogel":   {"source": None, "prompt": "A small blue tit (blue cap, blue wings, bright yellow belly) perched on a thin branch in a green forest, seen from the side, close-up, the background softly out of focus."},
    "fisch":   {"source": None, "prompt": "Underwater photograph in clear blue sea water: a shoal of many small silver fish swimming together, sunlight from the surface above. Many fish, no other animal."},
    "delfin":  {"source": None, "prompt": "A grey dolphin leaping out of the blue sea, its whole body in the air above the water, splashes, blue sky. The whole dolphin is in the picture."},
}
# LA PLANCHE D'ESSAI (6 images, 0,90 $, a faire approuver par Jacques avant tout) : ce qui risque le plus
ESSAI = ["kuh", "schaf", "goldfisch", "fuchs", "eichhoernchen", "delfin"]

LANGUES = {"es": ["fr", "en", "pt", "ar", "de"], "de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]}


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------------------------------------------
# LES PHRASES : chaque phrase de la page, dans la langue apprise, avec sa cle (« hab|kuh|bauernhof|sg »).
DEF_DE = {"der": "der", "die": "die", "das": "das"}
EIN = {"der": "ein", "die": "eine", "das": "ein"}
PRON_DE = {"der": "Er", "die": "Sie", "das": "Es"}
ENDUNG = {"der": "er", "die": "e", "das": "es"}
ZAHL = {3: "drei"}
NUM_ES = {3: "tres"}
NUM_FR = {3: "trois"}
NUM_EN = {3: "three"}
NUM_PT = {3: ("três", "três")}


def maj(s):
    return s[0].upper() + s[1:]


def de_sg(a, maj_=False):
    art, nom, _ = ANIMAUX[a]["de"]
    return (maj(art) if maj_ else art) + " " + nom


def de_pl(a, maj_=False):
    return ("Die " if maj_ else "die ") + ANIMAUX[a]["de"][2]


def es_sg(a, maj_=False):
    art, nom, _ = ANIMAUX[a]["es"]
    return (maj(art) if maj_ else art) + " " + nom


def es_pl(a, maj_=False):
    art, _, pl = ANIMAUX[a]["es"]
    p = "los" if art == "el" else "las"
    return (maj(p) if maj_ else p) + " " + pl


def es_f(a):
    return ANIMAUX[a]["es"][0] == "la"


def fr_f(a):
    return ANIMAUX[a]["fr"][3] == "f"


def pt_f(a):
    return ANIMAUX[a]["pt"][3] == "f"


def que_fr(a):
    n = ANIMAUX[a]["fr"][0]
    return "qu'" + n if n[0] in "aeiouyé" else "que " + n


def phrases():
    """{cle: {de, es, fr, en, pt}} : toutes les phrases, vraies et fausses (les fausses servent au « vrai ou faux »,
    et seule la vraie s'affiche apres la reponse)."""
    P = {}
    for a, x in ANIMAUX.items():
        fr, en, pt = x["fr"], x["en"], x["pt"]
        # « Das ist ein Fuchs. »
        P["ident|" + a] = {"de": "Das ist %s %s." % (EIN[x["de"][0]], x["de"][1]),
                           "es": "Es %s %s." % ("una" if es_f(a) else "un", x["es"][1]),
                           "fr": "C'est %s." % fr[2], "en": "It's %s." % en[2], "pt": "É %s." % pt[2]}
        # « der Fuchs, die Füchse » (l'article et le pluriel)
        P["art|" + a] = {"de": "%s, %s" % (de_sg(a), de_pl(a)), "es": "%s, %s" % (es_sg(a), es_pl(a)),
                         "fr": "%s, %s" % (fr[0], fr[1]), "en": en[0], "pt": "%s, %s" % (pt[0], pt[1])}
        # « ein Fuchs, zwei Füchse »
        un = {"fr": ("une " if fr_f(a) else "un ") + fr[2].split(" ", 1)[1], "pt": pt[2]}
        P["plur|" + a] = {"de": "%s %s, zwei %s" % (EIN[x["de"][0]], x["de"][1], x["de"][2]),
                          "es": "%s %s, dos %s" % ("una" if es_f(a) else "un", x["es"][1], x["es"][2]),
                          "fr": "%s, deux %s" % (un["fr"], fr[1].split(" ", 1)[1]),
                          "en": "one %s, two %s" % (en[0].split(" ", 1)[1], en[3]),
                          "pt": "%s, %s %s" % (un["pt"], "duas" if pt_f(a) else "dois", pt[1].split(" ", 1)[1])}
        # combien sur l'image : « Auf dem Bild sind drei Schafe. »
        n = x["nombre"]
        if n != 1:
            if n == "viele":
                P["nombre|" + a] = {"de": "Auf dem Bild sind viele %s." % x["de"][2], "es": "En la foto hay %s %s." % ("muchas" if es_f(a) else "muchos", x["es"][2]),
                                    "fr": "Sur la photo, il y a beaucoup de %s." % fr[1].split(" ", 1)[1], "en": "There are a lot of %s in the picture." % en[3],
                                    "pt": "Na foto há %s %s." % ("muitas" if pt_f(a) else "muitos", pt[1].split(" ", 1)[1])}
            else:
                P["nombre|" + a] = {"de": "Auf dem Bild sind %s %s." % (ZAHL[n], x["de"][2]), "es": "En la foto hay %s %s." % (NUM_ES[n], x["es"][2]),
                                    "fr": "Sur la photo, il y a %s %s." % (NUM_FR[n], fr[1].split(" ", 1)[1]), "en": "There are %s %s in the picture." % (NUM_EN[n], en[3]),
                                    "pt": "Na foto há %s %s." % (NUM_PT[n][1 if pt_f(a) else 0], pt[1].split(" ", 1)[1])}
        # ou il vit : vrai et faux, au singulier et au pluriel
        for h, hx in HABITATS.items():
            P["hab|%s|%s|sg" % (a, h)] = {"de": "%s lebt %s." % (de_sg(a, True), hx["de"]), "es": "%s vive %s." % (es_sg(a, True), hx["es"]),
                                          "fr": "%s vit %s." % (maj(fr[0]), hx["fr"]), "en": "%s lives %s." % (maj(en[0]), hx["en"]),
                                          "pt": "%s vive %s." % (maj(pt[0]), hx["pt"])}
            P["hab|%s|%s|pl" % (a, h)] = {"de": "%s leben %s." % (de_pl(a, True), hx["de"]), "es": "%s viven %s." % (es_pl(a, True), hx["es"]),
                                          "fr": "%s vivent %s." % (maj(fr[1]), hx["fr"]), "en": "%s live %s." % (maj(en[1]), hx["en"]),
                                          "pt": "%s vivem %s." % (maj(pt[1]), hx["pt"])}
        # ce qu'il mange : vrai et faux
        for f, fx in ALIMENTS.items():
            P["mange|%s|%s|sg" % (a, f)] = {"de": "%s frisst %s." % (de_sg(a, True), fx["de"]), "es": "%s come %s." % (es_sg(a, True), fx["es"]),
                                            "fr": "%s mange %s." % (maj(fr[0]), fx["fr"]), "en": "%s eats %s." % (maj(en[0]), fx["en"]),
                                            "pt": "%s come %s." % (maj(pt[0]), fx["pt"])}
            P["mange|%s|%s|pl" % (a, f)] = {"de": "%s fressen %s." % (de_pl(a, True), fx["de"]), "es": "%s comen %s." % (es_pl(a, True), fx["es"]),
                                            "fr": "%s mangent %s." % (maj(fr[1]), fx["fr"]), "en": "%s eat %s." % (maj(en[1]), fx["en"]),
                                            "pt": "%s comem %s." % (maj(pt[1]), fx["pt"])}
        # la couleur : vraie et fausses ; « Das ist ein brauner Bär. » devant le nom
        for c, cx in COULEURS.items():
            frc = x.get("frCouleur") if c == x["couleur"] and x.get("frCouleur") else cx["fr"][1 if fr_f(a) else 0]
            P["col|%s|%s" % (a, c)] = {"de": "%s ist %s." % (de_sg(a, True), cx["de"]), "es": "%s es %s." % (es_sg(a, True), cx["es"][1 if es_f(a) else 0]),
                                       "fr": "%s est %s." % (maj(fr[0]), frc), "en": "%s is %s." % (maj(en[0]), cx["en"]),
                                       "pt": "%s é %s." % (maj(pt[0]), cx["pt"][1 if pt_f(a) else 0])}
            if cx["deAttr"]:
                g = x["de"][0]
                art_fr = ("une " if fr_f(a) else "un ")
                nom_fr = fr[2].split(" ", 1)[1]
                P["attr|%s|%s" % (a, c)] = {"de": "Das ist %s %s%s %s." % (EIN[g], cx["deAttr"], ENDUNG[g], x["de"][1]),
                                            "fr": "C'est %s%s %s." % (art_fr, nom_fr, frc), "en": "It's %s %s %s." % ("an" if cx["en"][0] in "aeiou" else "a", cx["en"], en[2].split(" ", 1)[1]),
                                            "pt": "É %s %s." % (pt[2], cx["pt"][1 if pt_f(a) else 0])}
    # la taille : seulement a deux crans d'ecart au moins (« Das Pferd ist größer als der Hund. »)
    for a, x in ANIMAUX.items():
        for b, y in ANIMAUX.items():
            if x["taille"] - y["taille"] < 2:
                continue
            P["plus|%s|%s" % (a, b)] = {"de": "%s ist größer als %s." % (de_sg(a, True), de_sg(b)),
                                        "es": "%s es más grande que %s." % (es_sg(a, True), es_sg(b)),
                                        "fr": "%s est plus %s %s." % (maj(x["fr"][0]), "grande" if fr_f(a) else "grand", que_fr(b)),
                                        "en": "%s is bigger than %s." % (maj(x["en"][0]), y["en"][0]),
                                        "pt": "%s é maior que %s." % (maj(x["pt"][0]), y["pt"][0])}
            P["moins|%s|%s" % (b, a)] = {"de": "%s ist kleiner als %s." % (de_sg(b, True), de_sg(a)),
                                         "es": "%s es más %s que %s." % (es_sg(b, True), "pequeña" if es_f(b) else "pequeño", es_sg(a)),
                                         "fr": "%s est plus %s %s." % (maj(y["fr"][0]), "petite" if fr_f(b) else "petit", que_fr(a)),
                                         "en": "%s is smaller than %s." % (maj(y["en"][0]), x["en"][0]),
                                         "pt": "%s é menor que %s." % (maj(y["pt"][0]), x["pt"][0])}
    return P


def dit(a):
    """La phrase de la decouverte : ou il vit (sinon sa couleur), puis ce qu'il mange. {de, es, fr, en, pt}"""
    x = ANIMAUX[a]
    if x["ou"]:
        base = PH["hab|%s|%s|sg" % (a, x["ou"])]
    else:
        base = PH["col|%s|%s" % (a, x["couleur"])]
    out = dict(base)
    if x["mange"]:
        f = ALIMENTS[x["mange"][0]]
        pfr = "Elle" if fr_f(a) else "Il"
        ppt = "Ela" if pt_f(a) else "Ele"
        out = {"de": base["de"] + " %s frisst %s." % (PRON_DE[x["de"][0]], f["de"]), "es": base["es"] + " Come %s." % f["es"],
               "fr": base["fr"] + " %s mange %s." % (pfr, f["fr"]), "en": base["en"] + " It eats %s." % f["en"],
               "pt": base["pt"] + " %s come %s." % (ppt, f["pt"])}
    return out


PH = phrases()


def vraies():
    """Les cles des phrases qui peuvent s'afficher JUSTES (les seules a traduire)."""
    out = set()
    for a, x in ANIMAUX.items():
        out |= {"ident|" + a, "art|" + a, "plur|" + a}
        if x["nombre"] != 1:
            out.add("nombre|" + a)
        for h in ([x["ou"]] if x["ou"] else []) + x["aussi"]:
            out |= {"hab|%s|%s|sg" % (a, h), "hab|%s|%s|pl" % (a, h)}
        for f in x["mange"]:
            out |= {"mange|%s|%s|sg" % (a, f), "mange|%s|%s|pl" % (a, f)}
        if x["couleur"]:
            out.add("col|%s|%s" % (a, x["couleur"]))
            if COULEURS[x["couleur"]]["deAttr"]:
                out.add("attr|%s|%s" % (a, x["couleur"]))
    out |= {k for k in PH if k.startswith(("plus|", "moins|"))}
    return out


# ---------------------------------------------------------------------------------------------------------------
def gloses():
    """La traduction de chaque mot du theme dans les langues d'interface, prise au corpus (traduction,
    traduction_<langue>) : les noms (themes.json, temas.json) et les couleurs (adjectif.json, adjetivos.json)."""
    out = {"es": {}, "de": {}}
    for langue, fichier, adj in (("de", "themes.json", "adjectif.json"), ("es", "espanol/datos/temas.json", "espanol/datos/adjetivos.json")):
        corpus = {}
        for t in json.load(io.open(os.path.join(RACINE, fichier), encoding="utf-8"))["themes"]:
            for m in t["mots"]:
                corpus.setdefault(m["mot"], m)
        for liste in json.load(io.open(os.path.join(RACINE, adj), encoding="utf-8")).values():
            for m in liste:
                corpus.setdefault(m["mot"], m)
        mots = [x[langue][1] for x in ANIMAUX.values()]
        mots += [h["motDe" if langue == "de" else "motEs"][0] for h in HABITATS.values()]
        mots += [f["motDe" if langue == "de" else "motEs"][0] for f in ALIMENTS.values()]
        mots += [m for c in COULEURS_MOTS.values() for m in c[0 if langue == "de" else 1]]
        for mot in dict.fromkeys(mots):
            e = corpus.get(mot)
            if not e:
                sys.exit("  %s absent du corpus %s (espanol/ajouts/animales.json applique ?)" % (mot, langue))
            g = {l: e.get("traduction" if l == "fr" else "traduction_" + l) for l in LANGUES[langue]}
            manque = [l for l, v in g.items() if not v]
            if manque:
                sys.exit("  %s (%s) : pas de traduction en %s" % (mot, langue, ", ".join(manque)))
            out[langue][mot] = g
    return out


def ecrire_json():
    a_traduire = sorted(vraies())          # trie : un ensemble change d'ordre d'un lancement a l'autre
    phr = {"de": {k: v["de"] for k, v in PH.items() if "de" in v}, "es": {k: v["es"] for k, v in PH.items() if "es" in v}}
    trad = {"es": {}, "de": {}}
    for k in a_traduire:
        v = PH[k]
        if "es" in v:
            # en allemand, pour qui apprend l'espagnol : la phrase allemande du meme sens ; « Das ist ein brauner Bär. »
            # n'a pas de pendant espagnol (attr), « der Fuchs, die Füchse » se dit tel quel
            trad["es"][v["es"]] = {"fr": v["fr"], "en": v["en"], "pt": v["pt"], "de": v["de"]}
        trad["de"][v["de"]] = {"fr": v["fr"], "en": v["en"], "pt": v["pt"]}
    dits = {a: dit(a) for a in ANIMAUX}
    for a, d in dits.items():
        trad["es"][d["es"]] = {"fr": d["fr"], "en": d["en"], "pt": d["pt"], "de": d["de"]}
        trad["de"][d["de"]] = {"fr": d["fr"], "en": d["en"], "pt": d["pt"]}
    # les controles : chaque animal a sa couleur dans COULEURS, ses lieux dans HABITATS, une image prevue
    for a, x in ANIMAUX.items():
        if x["ou"] and x["ou"] not in HABITATS or any(h not in HABITATS for h in x["aussi"]):
            sys.exit("  %s : lieu inconnu" % a)
        if any(f not in ALIMENTS for f in x["mange"] + x["non"]) or set(x["mange"]) & set(x["non"]):
            sys.exit("  %s : aliment inconnu, ou vrai et faux a la fois" % a)
        if a not in IMAGES:
            sys.exit("  %s : pas d'image prevue" % a)
        if any(p in (x["de"][2], x["es"][2]) for p in x["plFaux"]["de"] + x["plFaux"]["es"]):
            sys.exit("  %s : un pluriel faux est le vrai" % a)
    if sorted(a for _, l in GROUPES for a in l) != sorted(ANIMAUX):
        sys.exit("  GROUPES : il manque un animal ou il y en a deux")
    d = {"animaux": {a: {k: v for k, v in x.items() if k not in ("fr", "en", "pt", "frCouleur")} for a, x in ANIMAUX.items()},
         "habitats": {h: {k: v for k, v in hx.items() if k in ("de", "es", "motDe", "motEs")} for h, hx in HABITATS.items()},
         "aliments": {f: {k: v for k, v in fx.items() if k in ("de", "es", "motDe", "motEs")} for f, fx in ALIMENTS.items()},
         "couleurs": {c: {"de": cx["de"], "deAttr": cx["deAttr"], "es": cx["es"], "motsDe": COULEURS_MOTS[c][0], "motsEs": COULEURS_MOTS[c][1]} for c, cx in COULEURS.items()},
         "groupes": GROUPES,
         "phrases": phr,
         "dit": {"de": {a: v["de"] for a, v in dits.items()}, "es": {a: v["es"] for a, v in dits.items()}},
         "trad": trad,
         # le mot choisi, quand il est faux : un lieu (« im Meer » -> dans la mer), une couleur (« grau » -> gris)
         "tradLieux": {l: {HABITATS[h][l]: {t: HABITATS[h][t] for t in ("fr", "en", "pt", "de") if t != l} for h in HABITATS} for l in ("de", "es")},
         "tradCouleurs": {"de": {cx["de"]: {"fr": cx["fr"][0], "en": cx["en"], "pt": cx["pt"][0]} for cx in COULEURS.values()},
                          # « gris » ne change pas en espagnol, mais se traduit gris ou grise : la cle porte le genre de l'animal
                          "es": {f + "|" + str(g): {"fr": cx["fr"][g], "en": cx["en"], "pt": cx["pt"][g], "de": cx["de"]} for cx in COULEURS.values() for g, f in enumerate(cx["es"])}},
         "gloses": gloses()}
    # ce que la page peut dire dans la decouverte : les fiches et les noms (les phrases apres les reponses se
    # relevent en jouant, visuel/voix_themes.py)
    a_dire = {"es": [v["es"] for v in dits.values()] + [es_sg(a) for a in ANIMAUX],
              "de": [v["de"] for v in dits.values()] + [de_sg(a) for a in ANIMAUX]}
    d["sons"] = {l: {t: identifiant(t) for t in dict.fromkeys(v)} for l, v in a_dire.items()}
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    os.makedirs(PROTO, exist_ok=True)
    io.open(os.path.join(PROTO, "animales.json"), "w", encoding="utf-8", newline="\n").write(texte)
    print("  animales.json : %d animaux, %d phrases (es %d, de %d), %d traduites" % (len(ANIMAUX), len(PH), len(phr["es"]), len(phr["de"]), len(trad["es"]) + len(trad["de"])))
    return d


def textes_a_dire(langue):
    """Pour les inventaires des voix (audio/manifest.py, manifest_es.py) : les fiches et les noms."""
    d = json.load(io.open(os.path.join(PROTO, "animales.json"), encoding="utf-8"))
    return list(d["sons"]["de" if langue == "de" else "es"])


# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES
def prompt(a):
    im = IMAGES[a]
    if im["source"] == "ferme":
        return MEME_FERME + im["prompt"] + PHOTO
    return im["prompt"] + PHOTO


def depense():
    chemin = os.path.join(DOSSIER, "depenses.log")
    if not os.path.exists(chemin):
        return 0.0
    # le montant est le dernier champ : sans rstrip(), « 0.15\n » n'etait jamais compte et la garde du plafond ne
    # voyait aucune depense passee (vecu le 3 nov. 2026, sans depassement : 2,10 $ pour 2,50 $)
    champs = [l.rstrip("\r\n").split("\t") for l in io.open(chemin, encoding="utf-8")]
    return sum(float(c[3]) for c in champs if len(c) >= 4 and c[3].replace(".", "", 1).isdigit())


def payer(noms, refaire):
    import omnihuman as O                                    # noqa: E402
    os.makedirs(DOSSIER, exist_ok=True)
    if refaire:
        for n in noms:
            png = os.path.join(DOSSIER, n + ".png")
            if os.path.exists(png):
                k = 1
                while os.path.exists(os.path.join(DOSSIER, "%s-rate%d.png" % (n, k))):
                    k += 1
                os.replace(png, os.path.join(DOSSIER, "%s-rate%d.png" % (n, k)))
    a_faire = [n for n in noms if IMAGES[n]["source"] != "chat" and not os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    deja = depense()
    print("  %d image(s) a faire, %.2f $ ; deja depense %.2f $ ; plafond %.2f $" % (len(a_faire), len(a_faire) * PRIX, deja, PLAFOND))
    if deja + len(a_faire) * PRIX > PLAFOND + 1e-9:
        sys.exit("  AU-DELA DU PLAFOND : rien n'est lance")
    if not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    for nom in a_faire:
        src = IMAGES[nom]["source"]
        corps = {"prompt": prompt(nom), "aspect_ratio": "4:3", "resolution": "2K", "output_format": "png", "num_images": 1}
        modele = TEXTE
        if src in ("ferme", "salon"):
            ref = FERME if src == "ferme" else os.path.join(SALON, "piece.png")
            corps["image_urls"] = [O.deposer(ref, "image/png", cle)[0]]
            modele = EDIT
        print("\n  %s (%s)\n  %s" % (nom, modele, corps["prompt"]))
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
            "prompt": corps["prompt"], "source": src, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


def chat():
    """Moritz (gato/sofa-auf, deja paye) : recadre autour du chat, en 4:3 -- gratuit."""
    from PIL import Image
    im = Image.open(os.path.join(SALON, "sofa-auf.png")).convert("RGB")
    W, H = im.size
    cx, cy, w = 0.44 * W, 0.575 * H, 600          # le chat fait un tiers de la largeur (20 % a 760 px : trop petit sur l accueil)
    h = w * 3 // 4
    x, y = int(cx - w / 2), int(cy - h / 2)
    os.makedirs(DOSSIER, exist_ok=True)
    im.crop((x, y, x + w, y + h)).save(os.path.join(DOSSIER, "katze.png"))
    print("  -> katze.png (recadre de gato/sofa-auf)")


def webp():
    from PIL import Image
    os.makedirs(PROTO, exist_ok=True)
    for a in ANIMAUX:
        png = os.path.join(DOSSIER, a + ".png")
        if not os.path.exists(png):
            print("  manque", a)
            continue
        im = Image.open(png).convert("RGB")
        W, H = im.size
        # 4:3 exactement (le modele rend parfois 1,33 a un pixel pres), 1200 x 900
        if abs(W / H - 4 / 3) > 0.01:
            if W / H > 4 / 3:
                nw = int(H * 4 / 3); im = im.crop(((W - nw) // 2, 0, (W - nw) // 2 + nw, H))
            else:
                nh = int(W * 3 / 4); im = im.crop((0, (H - nh) // 2, W, (H - nh) // 2 + nh))
        im.resize((1200, 900), Image.LANCZOS).save(os.path.join(PROTO, a + ".webp"), quality=80, method=6)
        print("  ->", a + ".webp")


def provisoires():
    """Des images dessinees (un aplat par lieu, le nom) pour essayer la page sans rien payer. A REMPLACER."""
    from PIL import Image, ImageDraw, ImageFont
    fonds = {"bauernhof": (176, 204, 120), "haus": (226, 214, 196), "wald": (92, 130, 84), "meer": (88, 150, 200)}
    try:
        police = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 96)
    except Exception:
        police = ImageFont.load_default()
    os.makedirs(PROTO, exist_ok=True)
    for h, liste in GROUPES:
        for a in liste:
            im = Image.new("RGB", (1200, 900), fonds[h])
            d = ImageDraw.Draw(im)
            d.ellipse((420, 260, 780, 620), fill=(250, 250, 250))
            d.text((600, 760), ANIMAUX[a]["de"][1], fill=(28, 36, 48), font=police, anchor="mm")
            im.save(os.path.join(PROTO, a + ".webp"), quality=70)
    print("  images provisoires ecrites dans", PROTO)


def planche():
    from PIL import Image, ImageDraw
    ids = [a for a in ANIMAUX if os.path.exists(os.path.join(DOSSIER, a + ".png"))]
    if not ids:
        return print("  aucune image")
    pl = Image.new("RGB", (3 * 600, ((len(ids) + 2) // 3) * 480), "white")
    for n, a in enumerate(ids):
        t = Image.open(os.path.join(DOSSIER, a + ".png")).convert("RGB").resize((600, 450))
        pl.paste(t, ((n % 3) * 600, (n // 3) * 480))
        ImageDraw.Draw(pl).text(((n % 3) * 600 + 8, (n // 3) * 480 + 452), a, fill="black")
    chemin = os.path.join(DOSSIER, "planche.jpg")
    pl.save(chemin, quality=85)
    print("  ->", chemin)


def main():
    ecrire_json()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--montrer" in sys.argv:
        for a in (args or list(IMAGES)):
            print("\n  %s (%s)\n  %s" % (a, IMAGES[a]["source"] or "texte", prompt(a)))
        print("\n  essai : %s (%.2f $) ; tout : %d images payantes (%.2f $), plafond %.2f $"
              % (", ".join(ESSAI), len(ESSAI) * PRIX, sum(1 for i in IMAGES.values() if i["source"] != "chat"),
                 sum(1 for i in IMAGES.values() if i["source"] != "chat") * PRIX, PLAFOND))
    if "--provisoires" in sys.argv:
        provisoires()
    if "--chat" in sys.argv:
        chat()
    if "--payer" in sys.argv:
        inconnus = [n for n in args if n not in IMAGES]
        if inconnus or not args:
            sys.exit("  --payer demande des noms d'images connus : " + ", ".join(inconnus))
        payer(args, "--refaire" in sys.argv)
    if "--webp" in sys.argv:
        webp()
    if "--planche" in sys.argv:
        planche()


if __name__ == "__main__":
    main()
