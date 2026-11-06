# -*- coding: utf-8 -*-
"""« Le logement » -- le theme illustre des PIECES, des MEUBLES et de la RECHERCHE D'UN APPARTEMENT, en allemand et
en espagnol (4 nov. 2026, vague 3 des themes, priorite au DTZ). LA SEULE SOURCE du theme : les logements, les pieces,
ce que chaque photo montre, les plans, les annonces, les definitions, les phrases et leurs traductions, les prompts.

    python visuel/logement/logement.py              # visuel/prototype/logement/logement.json + les photos reprises (gratuit)
    python visuel/logement/logement.py --montrer    # les prompts des images neuves, gratuit
    python visuel/logement/logement.py --payer [ids]   # les images fal qui manquent, 0,15 $ chacune -- ACCORD DE JACQUES
    python visuel/logement/logement.py --webp       # les originaux (hors depot) -> webp

L'ANGLE (regle 2 : pas de theme qui refait une scene). Les scenes du salon, de la cuisine et de la chambre font
« trouve l'objet » dans UNE piece. Ici, on compare des PIECES et des LOGEMENTS : quelle piece est-ce, ou est chacun,
ou est quel meuble ; puis on CHERCHE un appartement (l'annonce, le loyer, les charges, la caution, la visite), ce que
le DTZ demande (Lesen : les annonces ; Sprechen : le logement).

LES LIEUX (regle des lieux, video/LIEUX.md) : trois logements connus, et chaque piece qui existe deja en photo est
REPRISE telle quelle, jamais refaite : la colocation de Mark (le salon et la cuisine des scenes, sa chambre et sa
salle de bains de « La journee »), l'appartement d'Anna (le salon du demenagement, sa chambre, sa cuisine et sa douche
de « La journee »), l'appartement de Jan et Katrin (le salon de « Ou est le chat ? », la chambre des enfants, la
cuisine, la salle de bains et l'entree de « La journee »). Ce qui manque se genere, en partant de ces photos :
le balcon d'Anna, l'entree de Mark, et la VISITE d'un appartement a louer (Lena, la petite soeur d'Anna, avec la
proprietaire, Frau Becker). La chambre d'Anna de la scene « Anna packt ihren Koffer » n'est PAS reprise : elle ne
ressemble pas a celle de « La journee » (signale au chef le 4 nov.).

UNE IMAGE NE DIT QUE CE QU'ELLE MONTRE : chaque photo porte la liste des objets qu'on y voit, releves a l'oeil
(4 nov.), et le verbe juste pour CETTE photo (le miroir du demenagement est pose contre le mur : il « steht »). Un
leurre ou une phrase fausse ne vient jamais d'un objet qui pourrait etre la : seulement d'un objet propre a une autre
sorte de piece (pas de lit dans une cuisine).
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype")
SORTIE = os.path.join(PROTO, "logement")
IMG = os.path.join(os.path.expanduser("~"), ".wortando", "logement", "img")     # originaux fal, hors depot et hors OneDrive
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
EDIT, PRIX = "fal-ai/nano-banana-pro/edit", 0.15

# ---------------------------------------------------------------------------------------------------------------
# LES PIECES. de (genre, mot), datif (« im Bad »), es (genre, mot du corpus, forme affichee), fr, en, pt (nom, lieu).
PIECES = {
    "wohnzimmer":   {"de": ("das", "Wohnzimmer"), "dat": "im Wohnzimmer", "es": ("el", "salón"),
                     "fr": ("le salon", "dans le salon"), "en": ("the living room", "in the living room"), "pt": ("a sala", "na sala")},
    "schlafzimmer": {"de": ("das", "Schlafzimmer"), "dat": "im Schlafzimmer", "es": ("el", "dormitorio"),
                     "fr": ("la chambre", "dans la chambre"), "en": ("the bedroom", "in the bedroom"), "pt": ("o quarto", "no quarto")},
    "kinderzimmer": {"de": ("das", "Kinderzimmer"), "dat": "im Kinderzimmer", "es": ("la", "habitación", "habitación de los niños"),
                     "fr": ("la chambre des enfants", "dans la chambre des enfants"), "en": ("the children's room", "in the children's room"),
                     "pt": ("o quarto das crianças", "no quarto das crianças")},
    "kueche":       {"de": ("die", "Küche"), "dat": "in der Küche", "es": ("la", "cocina"),
                     "fr": ("la cuisine", "dans la cuisine"), "en": ("the kitchen", "in the kitchen"), "pt": ("a cozinha", "na cozinha")},
    "bad":          {"de": ("das", "Bad"), "dat": "im Bad", "es": ("el", "baño"),
                     "fr": ("la salle de bains", "dans la salle de bains"), "en": ("the bathroom", "in the bathroom"), "pt": ("o banheiro", "no banheiro")},
    "flur":         {"de": ("der", "Flur"), "dat": "im Flur", "es": ("el", "pasillo"),
                     "fr": ("le couloir", "dans le couloir"), "en": ("the hallway", "in the hallway"), "pt": ("o corredor", "no corredor")},
    "balkon":       {"de": ("der", "Balkon"), "dat": "auf dem Balkon", "es": ("el", "balcón"),
                     "fr": ("le balcon", "sur le balcon"), "en": ("the balcony", "on the balcony"), "pt": ("a varanda", "na varanda")},
}
# « Marks Zimmer » : une piece a son nom, sans article (le genitif saxon) ; en espagnol « la habitación de Mark »
MARKS_ZIMMER = {"de": ("", "Marks Zimmer"), "dat": "in Marks Zimmer", "es": ("la", "habitación", "habitación de Mark"),
                "fr": ("la chambre de Mark", "dans la chambre de Mark"), "en": ("Mark's room", "in Mark's room"), "pt": ("o quarto do Mark", "no quarto do Mark")}
# ce qui compte comme « Zimmer » dans une annonce allemande (le salon compte, pas la cuisine ni le bain), et comme
# « habitación » dans une annonce espagnole (les chambres seulement : le salon ne compte pas)
ZIMMER_DE = {"wohnzimmer", "schlafzimmer", "kinderzimmer", "zimmer"}
HAB_ES = {"schlafzimmer", "kinderzimmer", "zimmer"}
# les pieces qui se ressemblent : les premiers leurres de « quelle piece est-ce ? »
VOISINES = {"wohnzimmer": ["schlafzimmer", "kueche", "kinderzimmer"], "schlafzimmer": ["kinderzimmer", "wohnzimmer", "bad"],
            "kinderzimmer": ["schlafzimmer", "wohnzimmer", "bad"], "kueche": ["wohnzimmer", "bad", "flur"],
            "bad": ["kueche", "flur", "schlafzimmer"], "flur": ["bad", "wohnzimmer", "kueche"], "balkon": ["wohnzimmer", "flur", "kueche"],
            "zimmer": ["kueche", "bad", "wohnzimmer"]}

# ---------------------------------------------------------------------------------------------------------------
# LES OBJETS. de (genre, mot), es (genre, mot ; « sens » quand le corpus a deux entrees), fr / en / pt (l'article
# defini, le nom ; un dict par langue apprise quand la traduction suit le mot : der Herd = la cuisiniere, el horno
# = le four), et la piece a laquelle l'objet appartient EN PROPRE (un leurre sur ; None : il peut etre partout).
OBJETS = {
    "sofa":     {"de": ("das", "Sofa"), "es": ("el", "sofá"), "fr": ("le", "canapé", "un"), "en": "sofa", "pt": ("o", "sofá", "um"), "piece": ["wohnzimmer"]},
    "bett":     {"de": ("das", "Bett"), "es": ("la", "cama"), "fr": ("le", "lit", "un"), "en": "bed", "pt": ("a", "cama", "uma"), "piece": ["schlafzimmer", "kinderzimmer", "zimmer"]},
    "schrank":  {"de": ("der", "Schrank"), "es": ("el", "armario"), "fr": ("l'", "armoire", "une"), "en": "cupboard", "pt": ("o", "armário", "um"), "piece": None},
    "tisch":    {"de": ("der", "Tisch"), "es": ("la", "mesa"), "fr": ("la", "table", "une"), "en": "table", "pt": ("a", "mesa", "uma"), "piece": None},
    "stuhl":    {"de": ("der", "Stuhl"), "es": ("la", "silla"), "fr": ("la", "chaise", "une"), "en": "chair", "pt": ("a", "cadeira", "uma"), "piece": None},
    "lampe":    {"de": ("die", "Lampe"), "es": ("la", "lámpara"), "fr": ("la", "lampe", "une"), "en": "lamp", "pt": ("a", "luminária", "uma"), "piece": None},
    "regal":    {"de": ("das", "Regal"), "es": ("la", "estantería"), "fr": ("l'", "étagère", "une"), "en": "shelf", "pt": ("a", "estante", "uma"), "piece": None},
    "spiegel":  {"de": ("der", "Spiegel"), "es": ("el", "espejo"), "fr": ("le", "miroir", "un"), "en": "mirror", "pt": ("o", "espelho", "um"), "piece": None},
    "teppich":  {"de": ("der", "Teppich"), "es": ("la", "alfombra"), "fr": ("le", "tapis", "un"), "en": "rug", "pt": ("o", "tapete", "um"), "piece": None},
    "bild":     {"de": ("das", "Bild"), "es": ("el", "cuadro"), "fr": ("le", "tableau", "un"), "en": "picture", "pt": ("o", "quadro", "um"), "piece": None},
    "vorhang":  {"de": ("der", "Vorhang"), "es": ("la", "cortina"), "fr": ("le", "rideau", "un"), "en": "curtain", "pt": ("a", "cortina", "uma"), "piece": None},
    "kissen":   {"de": ("das", "Kissen"), "es": ("el", "cojín"), "fr": ("le", "coussin", "un"), "en": "cushion", "pt": ("a", "almofada", "uma"), "piece": None},
    "kopfkissen": {"de": ("das", "Kissen"), "es": ("la", "almohada"), "fr": ("l'", "oreiller", "un"), "en": "pillow", "pt": ("o", "travesseiro", "um"), "piece": None},
    "pflanze":  {"de": ("die", "Pflanze"), "es": ("la", "planta", None, "la plante"), "fr": ("la", "plante", "une"), "en": "plant", "pt": ("a", "planta", "uma"), "piece": None},
    "kuehlschrank": {"de": ("der", "Kühlschrank"), "es": ("la", "nevera"), "fr": ("le", "réfrigérateur", "un"), "en": "fridge", "pt": ("a", "geladeira", "uma"), "piece": ["kueche"]},
    "herd":     {"de": ("der", "Herd"), "es": ("el", "horno"), "fr": {"de": ("la", "cuisinière", "une"), "es": ("le", "four", "un")},
                 "en": {"de": "stove", "es": "oven"}, "pt": {"de": ("o", "fogão", "um"), "es": ("o", "forno", "um")}, "piece": ["kueche"]},
    "spuele":   {"de": ("die", "Spüle"), "es": ("el", "fregadero"), "fr": ("l'", "évier", "un"), "en": "sink", "pt": ("a", "pia", "uma"), "piece": ["kueche"]},
    "dusche":   {"de": ("die", "Dusche"), "es": ("la", "ducha"), "fr": ("la", "douche", "une"), "en": "shower", "pt": ("o", "chuveiro", "um"), "piece": ["bad"]},
    "badewanne": {"de": ("die", "Badewanne"), "es": ("la", "bañera"), "fr": ("la", "baignoire", "une"), "en": "bathtub", "pt": ("a", "banheira", "uma"), "piece": ["bad"]},
    "heizung":  {"de": ("die", "Heizung"), "es": ("el", "radiador"), "fr": {"de": ("le", "chauffage", "un"), "es": ("le", "radiateur", "un")},
                 "en": "radiator", "pt": ("o", "aquecedor", "um"), "piece": None},
    "fernseher": {"de": ("der", "Fernseher"), "es": ("la", "televisión"), "fr": ("la", "télévision", "une"), "en": "TV", "pt": ("a", "televisão", "uma"), "piece": None},
    "fahrrad":  {"de": ("das", "Fahrrad"), "es": ("la", "bicicleta"), "fr": ("le", "vélo", "un"), "en": "bike", "pt": ("a", "bicicleta", "uma"), "piece": None},
    "handtuch": {"de": ("das", "Handtuch"), "es": ("la", "toalla"), "fr": ("la", "serviette", "une"), "en": "towel", "pt": ("a", "toalha", "uma"), "piece": None},
    "karton":   {"de": ("der", "Karton"), "es": ("la", "caja de cartón"), "fr": ("le", "carton", "un"), "en": "box", "pt": ("a", "caixa", "uma"), "piece": None},
    "uhr":      {"de": ("die", "Uhr"), "es": ("el", "reloj"), "fr": ("l'", "horloge", "une"), "en": "clock", "pt": ("o", "relógio", "um"), "piece": None},
    "korb":     {"de": ("der", "Korb"), "es": ("la", "cesta"), "fr": ("le", "panier", "un"), "en": "basket", "pt": ("a", "cesta", "uma"), "piece": None},
}
# LES PLACES PRECISES, verifiees sur chaque photo (sinon l'objet est « im Wohnzimmer », la piece de la photo)
ORTS = {
    "wand":          ("an der Wand", "en la pared", "au mur", "on the wall", "na parede"),
    "boden":         ("auf dem Boden", "en el suelo", "par terre", "on the floor", "no chão"),
    "ueber-tisch":   ("über dem Tisch", "encima de la mesa", "au-dessus de la table", "above the table", "acima da mesa"),
    "auf-bett":      ("auf dem Bett", "en la cama", "sur le lit", "on the bed", "na cama"),
    "auf-sofa":      ("auf dem Sofa", "en el sofá", "sur le canapé", "on the sofa", "no sofá"),
    "vor-fenster":   ("vor dem Fenster", "delante de la ventana", "devant la fenêtre", "in front of the window", "na frente da janela"),
    "unter-fenster": ("unter dem Fenster", "debajo de la ventana", "sous la fenêtre", "under the window", "embaixo da janela"),
    "neben-bett":    ("neben dem Bett", "al lado de la cama", "à côté du lit", "next to the bed", "ao lado da cama"),
    "ueber-spiegel": ("über dem Spiegel", "encima del espejo", "au-dessus du miroir", "above the mirror", "acima do espelho"),
    "vor-sofa":      ("vor dem Sofa", "delante del sofá", "devant le canapé", "in front of the sofa", "na frente do sofá"),
}

# ---------------------------------------------------------------------------------------------------------------
# LES LOGEMENTS : leur nom dans les phrases, et le PLAN (dessine par la page, en unites ; x, y, largeur, hauteur)
LOGEMENTS = {
    "mark": {"de": "in Marks WG", "es": "del piso de Mark", "fr": "de la colocation de Mark", "en": "in Mark's shared apartment", "pt": "do apartamento do Mark",
             "titre": {"de": "Marks WG", "es": "El piso de Mark", "fr": "La colocation de Mark", "en": "Mark's shared apartment", "pt": "O apartamento do Mark"},
             "plan": [("zimmer-mark", "zimmer", 0, 0, 3.4, 3.2), ("bad", "bad", 3.4, 0, 2.4, 3.2), ("kueche", "kueche", 5.8, 0, 4.2, 3.2),
                      ("flur", "flur", 0, 3.2, 10, 1.4), ("wohnzimmer", "wohnzimmer", 0, 4.6, 6, 3.6), ("zimmer-2", "zimmer", 6, 4.6, 4, 3.6)]},
    "anna": {"de": "in Annas Wohnung", "es": "del piso de Anna", "fr": "de l'appartement d'Anna", "en": "in Anna's apartment", "pt": "do apartamento da Anna",
             "titre": {"de": "Annas Wohnung", "es": "El piso de Anna", "fr": "L'appartement d'Anna", "en": "Anna's apartment", "pt": "O apartamento da Anna"},
             "plan": [("kueche", "kueche", 0, 0, 3.8, 3.2), ("bad", "bad", 3.8, 0, 2.2, 3.2), ("schlafzimmer", "schlafzimmer", 6, 0, 4, 3.2),
                      ("flur", "flur", 0, 3.2, 10, 1.4), ("wohnzimmer", "wohnzimmer", 0, 4.6, 7, 3.6), ("balkon", "balkon", 7, 5.2, 3, 2.4)]},
    "jk":   {"de": "in der Wohnung von Jan und Katrin", "es": "del piso de Jan y Katrin", "fr": "de l'appartement de Jan et Katrin",
             "en": "in Jan and Katrin's apartment", "pt": "do apartamento do Jan e da Katrin",
             "titre": {"de": "Die Wohnung von Jan und Katrin", "es": "El piso de Jan y Katrin", "fr": "L'appartement de Jan et Katrin",
                       "en": "Jan and Katrin's apartment", "pt": "O apartamento do Jan e da Katrin"},
             "plan": [("kueche", "kueche", 0, 0, 4, 3.4), ("bad", "bad", 4, 0, 2.4, 3.4), ("kinderzimmer", "kinderzimmer", 6.4, 0, 3.6, 3.4),
                      ("flur", "flur", 0, 3.4, 10, 1.3), ("wohnzimmer", "wohnzimmer", 0, 4.7, 5.8, 3.5), ("schlafzimmer", "schlafzimmer", 5.8, 4.7, 4.2, 3.5)]},
    "lena": {"de": "in der neuen Wohnung", "es": "del piso nuevo", "fr": "du nouvel appartement", "en": "in the new apartment", "pt": "do apartamento novo",
             "titre": {"de": "Die Wohnung für Lena", "es": "El piso para Lena", "fr": "L'appartement pour Lena", "en": "The apartment for Lena", "pt": "O apartamento para a Lena"},
             "plan": [("schlafzimmer", "schlafzimmer", 0, 0, 4, 3.2), ("bad", "bad", 4, 0, 2.2, 3.2), ("kueche", "kueche", 6.2, 0, 3.8, 3.2),
                      ("flur", "flur", 0, 3.2, 10, 1.4), ("wohnzimmer", "wohnzimmer", 0, 4.6, 10, 2.8), ("balkon", "balkon", 2, 7.4, 6, 1.2)]},
}

# ---------------------------------------------------------------------------------------------------------------
# LES PERSONNES : leur nom dans chaque langue, l'article portugais, le pluriel
PERS = {"Mark": "o", "Anna": "a", "Jan": "o", "Katrin": "a", "Ben": "o", "Mia": "a", "Lena": "a"}
def groupe_pers(noms):
    """« Ben und Mia » / « Ben y Mia » / « Ben et Mia » / « o Ben e a Mia » ; la famille entiere : « die Familie »."""
    if set(noms) == {"Jan", "Katrin", "Ben", "Mia"}:
        return {"de": ("Die Familie", "die Familie", False), "es": ("La familia", "la familia", False), "fr": ("La famille", False),
                "en": ("The family", False), "pt": ("A família", False)}
    pl = len(noms) > 1
    def lie(et, xs): return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " " + et + " " + xs[-1]
    pt = lie("e", [PERS[n] + " " + n for n in noms])
    return {"de": (lie("und", noms), lie("und", noms), pl), "es": (lie("y", noms), lie("y", noms), pl), "fr": (lie("et", noms), pl),
            "en": (lie("and", noms), pl), "pt": (pt[0].upper() + pt[1:], pl)}

# ---------------------------------------------------------------------------------------------------------------
# LES PHOTOS. src : une photo deja publiee (reprise, recadree en 4:3 pour les scenes, qui sont en hauteur), ou None
# (une image neuve, a generer : elle n'entre dans le jeu que quand son webp existe). piece : la piece montree ;
# reconnaissable : la piece se voit sans qu'on la nomme ; personnes : {nom: piece} ; objets : {objet: (verbe, place)}.
# Verbe : steht / liegt / hängt (le verbe juste pour CETTE photo), ou « ist » pour ce qui n'en prend aucun (la douche).
PHOTOS = {
    # LA COLOCATION DE MARK -- le salon (scene « Nach der Party »), la cuisine (scene « Mark kocht »), la Journee
    "mark-salon":   {"src": ("wohnzimmer.webp", 1150), "logement": "mark", "piece": "wohnzimmer", "personnes": {},
                     "objets": {"sofa": ("steht", None), "fahrrad": ("steht", None), "pflanze": ("steht", None), "regal": ("steht", None),
                                "tisch": ("steht", "vor-sofa"), "fernseher": ("steht", None), "schrank": ("steht", None)}},
    "mark-salon-2": {"src": ("journee/mark-6.webp", 0), "logement": "mark", "piece": "wohnzimmer", "personnes": {"Mark": "wohnzimmer"},
                     "objets": {"sofa": ("steht", None), "bild": ("hängt", "wand"), "pflanze": ("steht", None), "regal": ("steht", None),
                                "fahrrad": ("steht", None), "tisch": ("steht", None), "stuhl": ("steht", None)}},
    "mark-kueche":  {"src": ("kueche.webp", 900), "logement": "mark", "piece": "kueche", "personnes": {"Mark": "kueche"},
                     "objets": {"kuehlschrank": ("steht", None), "herd": ("steht", None), "spuele": ("ist", None), "tisch": ("steht", None),
                                "pflanze": ("steht", None)}},
    "mark-kueche-2": {"src": ("journee/mark-7.webp", 0), "logement": "mark", "piece": "kueche", "personnes": {"Mark": "kueche"},
                     "objets": {"kuehlschrank": ("steht", None), "herd": ("steht", None), "tisch": ("steht", None), "stuhl": ("steht", None),
                                "lampe": ("hängt", None), "regal": ("hängt", "wand")}},
    "mark-zimmer":  {"src": ("journee/mark-1.webp", 0), "logement": "mark", "piece": "zimmer", "personnes": {"Mark": "zimmer"},
                     "objets": {"bett": ("steht", None), "vorhang": ("hängt", "vor-fenster"), "stuhl": ("steht", None), "kopfkissen": ("liegt", "auf-bett")}},
    "mark-zimmer-2": {"src": ("journee/mark-8.webp", 0), "logement": "mark", "piece": "zimmer", "personnes": {"Mark": "zimmer"},
                     "objets": {"bett": ("steht", None)}},
    "mark-bad":     {"src": ("journee/mark-4.webp", 0), "logement": "mark", "piece": "bad", "personnes": {"Mark": "bad"},
                     "objets": {"spiegel": ("hängt", "wand"), "dusche": ("ist", None), "lampe": ("hängt", "ueber-spiegel")}},
    "mark-bad-2":   {"src": ("journee/mark-3.webp", 0), "logement": "mark", "piece": "bad", "personnes": {"Mark": "bad"},
                     "objets": {"dusche": ("ist", None)}},
    "mark-flur":    {"src": None, "logement": "mark", "piece": "flur", "personnes": {"Mark": "flur"},
                     "objets": {"spiegel": ("hängt", "wand"), "lampe": ("hängt", None), "teppich": ("liegt", "boden")}},
    # L'APPARTEMENT D'ANNA -- le salon du jour du demenagement (scene « Umzug »), la Journee
    "anna-salon":   {"src": ("umzug.webp", 1000), "logement": "anna", "piece": "wohnzimmer", "personnes": {"Anna": "wohnzimmer"},
                     "objets": {"sofa": ("steht", None), "kissen": ("liegt", "auf-sofa"), "spiegel": ("steht", None), "lampe": ("steht", None),
                                "bild": ("hängt", "wand"), "uhr": ("steht", "boden"), "regal": ("steht", None), "karton": ("steht", "boden"),
                                "tisch": ("steht", None), "heizung": ("ist", "unter-fenster")}},
    "anna-chambre": {"src": ("journee/anna-1.webp", 0), "logement": "anna", "piece": "schlafzimmer", "personnes": {"Anna": "schlafzimmer"},
                     "objets": {"bett": ("steht", None), "lampe": ("steht", "neben-bett"), "kopfkissen": ("liegt", "auf-bett")}},
    "anna-chambre-2": {"src": ("journee/anna-4.webp", 0), "logement": "anna", "piece": "schlafzimmer", "personnes": {"Anna": "schlafzimmer"},
                     "objets": {"bett": ("steht", None), "lampe": ("steht", "neben-bett"), "schrank": ("steht", None), "kopfkissen": ("liegt", "auf-bett")}},
    "anna-chambre-3": {"src": ("journee/anna-10.webp", 0), "logement": "anna", "piece": "schlafzimmer", "personnes": {"Anna": "schlafzimmer"},
                     "objets": {"bett": ("steht", None), "lampe": ("steht", "neben-bett")}},
    "anna-cuisine": {"src": ("journee/anna-5.webp", 0), "logement": "anna", "piece": "kueche", "personnes": {"Anna": "kueche"},
                     "objets": {"tisch": ("steht", None), "stuhl": ("steht", None), "lampe": ("hängt", "ueber-tisch"), "regal": ("hängt", "wand"),
                                "schrank": ("steht", None), "heizung": ("ist", "unter-fenster")}},
    "anna-cuisine-2": {"src": ("journee/anna-9.webp", 0), "logement": "anna", "piece": "kueche", "personnes": {"Anna": "kueche"},
                     "objets": {"tisch": ("steht", None), "stuhl": ("steht", None), "lampe": ("hängt", "ueber-tisch"), "regal": ("hängt", "wand"),
                                "schrank": ("steht", None), "heizung": ("ist", "unter-fenster")}},
    "anna-bad":     {"src": ("journee/anna-3.webp", 0), "logement": "anna", "piece": "bad", "personnes": {"Anna": "bad"},
                     "objets": {"dusche": ("ist", None)}},
    "anna-balkon":  {"src": None, "logement": "anna", "piece": "balkon", "personnes": {"Anna": "balkon"},
                     "objets": {"pflanze": ("steht", None), "tisch": ("steht", None), "stuhl": ("steht", None)}},
    # L'APPARTEMENT DE JAN ET KATRIN -- le salon de « Ou est le chat ? », la Journee
    "jk-salon":     {"src": ("gato/piece.webp", 0), "logement": "jk", "piece": "wohnzimmer", "personnes": {},
                     "objets": {"schrank": ("steht", None), "bild": ("hängt", "wand"), "sofa": ("steht", None), "kissen": ("liegt", "auf-sofa"),
                                "korb": ("steht", None), "pflanze": ("steht", None), "regal": ("steht", None), "tisch": ("steht", None),
                                "stuhl": ("steht", None), "karton": ("steht", "boden"), "vorhang": ("hängt", None)}},
    "jk-enfants":   {"src": ("journee/familia-1.webp", 0), "logement": "jk", "piece": "kinderzimmer", "personnes": {"Katrin": "kinderzimmer", "Mia": "kinderzimmer"},
                     "objets": {"bett": ("steht", None), "lampe": ("steht", None), "teppich": ("liegt", "boden"), "regal": ("steht", None), "vorhang": ("hängt", None)}},
    "jk-enfants-2": {"src": ("journee/familia-7.webp", 0), "logement": "jk", "piece": "kinderzimmer", "personnes": {"Ben": "kinderzimmer", "Mia": "kinderzimmer"},
                     "objets": {"bett": ("steht", None), "lampe": ("steht", None), "teppich": ("liegt", "boden"), "regal": ("steht", None),
                                "stuhl": ("steht", None), "heizung": ("ist", "unter-fenster"), "vorhang": ("hängt", None)}},
    "jk-enfants-3": {"src": ("journee/familia-8.webp", 0), "logement": "jk", "piece": "kinderzimmer", "personnes": {"Jan": "kinderzimmer", "Ben": "kinderzimmer", "Mia": "kinderzimmer"},
                     "objets": {"bett": ("steht", None), "lampe": ("steht", None), "teppich": ("liegt", "boden")}},
    "jk-cuisine":   {"src": ("journee/familia-2.webp", 0), "logement": "jk", "piece": "kueche", "personnes": {"Jan": "kueche", "Katrin": "kueche", "Ben": "kueche", "Mia": "kueche"},
                     "objets": {"tisch": ("steht", None), "lampe": ("hängt", "ueber-tisch"), "stuhl": ("steht", None), "heizung": ("ist", None)}},
    "jk-cuisine-2": {"src": ("journee/familia-6.webp", 0), "logement": "jk", "piece": "kueche", "personnes": {"Jan": "kueche", "Katrin": "kueche", "Ben": "kueche", "Mia": "kueche"},
                     "objets": {"tisch": ("steht", None), "lampe": ("hängt", "ueber-tisch")}},
    "jk-bad":       {"src": ("journee/familia-3.webp", 0), "logement": "jk", "piece": "bad", "personnes": {"Ben": "bad", "Mia": "bad"},
                     "objets": {"spiegel": ("hängt", "wand"), "badewanne": ("steht", None), "handtuch": ("hängt", None)}},
    "jk-flur":      {"src": ("journee/familia-4.webp", 0), "logement": "jk", "piece": "flur", "personnes": {"Katrin": "flur", "Mia": "flur"},
                     "objets": {"lampe": ("hängt", None), "bild": ("hängt", "wand"), "heizung": ("ist", None)}},
    # LA VISITE (die Besichtigung) : un appartement a louer, vide ; Lena et la proprietaire, Frau Becker
    "visite-cuisine": {"src": None, "logement": "lena", "piece": "kueche", "personnes": {"Lena": "kueche"}, "becker": True,
                     "objets": {"herd": ("steht", None), "kuehlschrank": ("steht", None), "spuele": ("ist", None), "schrank": ("hängt", "wand")}},
    "visite-bad":   {"src": None, "logement": "lena", "piece": "bad", "personnes": {"Lena": "bad"}, "becker": True,
                     "objets": {"badewanne": ("steht", None), "spiegel": ("hängt", "wand")}},
    "visite-balkon": {"src": None, "logement": "lena", "piece": "balkon", "reconnaissable": False, "personnes": {"Lena": "balkon"}, "becker": True,
                     "objets": {}},
    "visite-vertrag": {"src": None, "logement": "lena", "piece": "kueche", "reconnaissable": False, "personnes": {"Lena": "kueche"}, "becker": True,
                     "objets": {}},
}
# ce que montre la visite : Frau Becker montre une piece, Lena signe, Lena recoit les cles
VISITE = {
    "visite-cuisine": {"de": ("Was zeigt Frau Becker Lena?", "die Küche", "Frau Becker zeigt Lena die Küche.", ["das Bad", "den Balkon"], "kueche"),
                       "es": ("¿Qué le enseña la señora Becker a Lena?", "la cocina", "La señora Becker le enseña la cocina a Lena.", ["el baño", "el balcón"], "kueche"),
                       "fr": "Frau Becker montre la cuisine à Lena.", "en": "Mrs Becker shows Lena the kitchen.", "pt": "A senhora Becker mostra a cozinha para a Lena."},
    "visite-bad":     {"de": ("Was zeigt Frau Becker Lena?", "das Bad", "Frau Becker zeigt Lena das Bad.", ["die Küche", "den Balkon"], "bad"),
                       "es": ("¿Qué le enseña la señora Becker a Lena?", "el baño", "La señora Becker le enseña el baño a Lena.", ["la cocina", "el balcón"], "bad"),
                       "fr": "Frau Becker montre la salle de bains à Lena.", "en": "Mrs Becker shows Lena the bathroom.", "pt": "A senhora Becker mostra o banheiro para a Lena."},
    "visite-balkon":  {"de": ("Was zeigt Frau Becker Lena?", "den Balkon", "Frau Becker zeigt Lena den Balkon.", ["die Küche", "das Bad"], "balkon"),
                       "es": ("¿Qué le enseña la señora Becker a Lena?", "el balcón", "La señora Becker le enseña el balcón a Lena.", ["la cocina", "el baño"], "balkon"),
                       "fr": "Frau Becker montre le balcon à Lena.", "en": "Mrs Becker shows Lena the balcony.", "pt": "A senhora Becker mostra a varanda para a Lena."},
    "visite-vertrag": {"de": ("Was unterschreibt Lena?", "den Mietvertrag", "Lena unterschreibt den Mietvertrag.", ["die Miete", "den Schlüssel"], "mietvertrag"),
                       "es": ("¿Qué firma Lena?", "el contrato", "Lena firma el contrato.", ["la llave", "el alquiler"], "contrato"),
                       "fr": "Lena signe le contrat de location.", "en": "Lena signs the rental contract.", "pt": "A Lena assina o contrato de aluguel."},
}

# ---------------------------------------------------------------------------------------------------------------
# LES ANNONCES (DTZ, Lesen) : les donnees, et le texte qu'on en tire. Berlin en allemand, Madrid en espagnol.
# z : Zimmer (le salon compte) ; qm ; et : etage (0 : rez-de-chaussee) ; km : Kaltmiete ; nk : Nebenkosten ;
# kt : Kaution en Monatsmieten (Kaltmiete) ; blk, aufz, ebk ; frei : « sofort » ou une date (jour, mois).
ANNONCES_DE = [
    {"id": "pankow", "ort": "Pankow", "z": 2, "qm": 62, "et": 2, "km": 720, "nk": 180, "kt": 3, "blk": 1, "aufz": 1, "ebk": 1, "frei": (1, 12)},
    {"id": "neukoelln", "ort": "Neukölln", "z": 2, "qm": 55, "et": 4, "km": 640, "nk": 150, "kt": 3, "blk": 0, "aufz": 0, "ebk": 1, "frei": "sofort"},
    {"id": "wedding", "ort": "Wedding", "z": 1, "qm": 38, "et": 0, "km": 450, "nk": 110, "kt": 2, "blk": 0, "aufz": 0, "ebk": 0, "frei": (1, 1)},
    {"id": "friedrichshain", "ort": "Friedrichshain", "z": 3, "qm": 78, "et": 3, "km": 980, "nk": 230, "kt": 3, "blk": 1, "aufz": 1, "ebk": 1, "frei": (1, 2)},
    {"id": "moabit", "ort": "Moabit", "z": 2, "qm": 58, "et": 1, "km": 690, "nk": 170, "kt": 2, "blk": 1, "aufz": 0, "ebk": 0, "frei": "sofort"},
    {"id": "schoeneberg", "ort": "Schöneberg", "z": 1, "qm": 42, "et": 5, "km": 560, "nk": 130, "kt": 3, "blk": 1, "aufz": 1, "ebk": 1, "frei": (15, 12)},
    {"id": "kreuzberg", "ort": "Kreuzberg", "z": 3, "qm": 85, "et": 2, "km": 1050, "nk": 250, "kt": 3, "blk": 0, "aufz": 0, "ebk": 1, "frei": (1, 1)},
    {"id": "lichtenberg", "ort": "Lichtenberg", "z": 2, "qm": 60, "et": 0, "km": 600, "nk": 160, "kt": 2, "blk": 0, "aufz": 0, "ebk": 1, "frei": "sofort"},
    {"id": "spandau", "ort": "Spandau", "z": 3, "qm": 72, "et": 1, "km": 820, "nk": 210, "kt": 3, "blk": 1, "aufz": 0, "ebk": 0, "frei": (1, 12)},
    {"id": "prenzlauerberg", "ort": "Prenzlauer Berg", "z": 2, "qm": 64, "et": 4, "km": 890, "nk": 190, "kt": 3, "blk": 1, "aufz": 1, "ebk": 0, "frei": (1, 2)},
    # les chambres en colocation : un loyer « warm » (tout compris), la taille de la WG (3er-WG : trois personnes)
    {"id": "wg-kreuzberg", "ort": "Kreuzberg", "wg": 3, "qm": 16, "et": 2, "warm": 480, "kt": 2, "frei": (1, 12)},
    {"id": "wg-neukoelln", "ort": "Neukölln", "wg": 2, "qm": 12, "et": 3, "warm": 420, "kt": 2, "frei": "sofort"},
    {"id": "wg-friedrichshain", "ort": "Friedrichshain", "wg": 4, "qm": 15, "et": 1, "warm": 560, "kt": 2, "frei": (1, 1)},
]
# hab : habitaciones (les chambres) ; pl : planta (0 : bajo) ; alq : alquiler ; gas : gastos ; fz : fianza en meses ;
# asc, balc, amu ; libre : « ya » ou une date ; comp : habitacion en piso compartido (le nombre de personnes)
ANNONCES_ES = [
    {"id": "chamberi", "ort": "Chamberí", "hab": 2, "qm": 70, "pl": 3, "alq": 1180, "gas": 60, "fz": 1, "asc": 1, "balc": 1, "amu": 1, "libre": (1, 12)},
    {"id": "lavapies", "ort": "Lavapiés", "hab": 1, "qm": 45, "pl": 2, "alq": 950, "gas": 40, "fz": 2, "asc": 0, "balc": 0, "amu": 1, "libre": "ya"},
    {"id": "usera", "ort": "Usera", "hab": 2, "qm": 65, "pl": 0, "alq": 900, "gas": 50, "fz": 1, "asc": 0, "balc": 0, "amu": 0, "libre": (1, 1)},
    {"id": "tetuan", "ort": "Tetuán", "hab": 3, "qm": 85, "pl": 4, "alq": 1300, "gas": 80, "fz": 2, "asc": 1, "balc": 1, "amu": 0, "libre": (1, 2)},
    {"id": "carabanchel", "ort": "Carabanchel", "hab": 2, "qm": 68, "pl": 1, "alq": 1000, "gas": 45, "fz": 1, "asc": 0, "balc": 1, "amu": 1, "libre": "ya"},
    {"id": "retiro", "ort": "Retiro", "hab": 1, "qm": 50, "pl": 5, "alq": 1150, "gas": 70, "fz": 2, "asc": 1, "balc": 1, "amu": 1, "libre": (15, 12)},
    {"id": "malasana", "ort": "Malasaña", "hab": 2, "qm": 60, "pl": 4, "alq": 1200, "gas": 50, "fz": 2, "asc": 0, "balc": 0, "amu": 1, "libre": (1, 1)},
    {"id": "vallecas", "ort": "Vallecas", "hab": 2, "qm": 72, "pl": 2, "alq": 950, "gas": 55, "fz": 1, "asc": 1, "balc": 0, "amu": 0, "libre": "ya"},
    {"id": "arganzuela", "ort": "Arganzuela", "hab": 3, "qm": 90, "pl": 3, "alq": 1450, "gas": 90, "fz": 2, "asc": 1, "balc": 1, "amu": 1, "libre": (1, 12)},
    {"id": "latina", "ort": "La Latina", "hab": 1, "qm": 40, "pl": 1, "alq": 800, "gas": 35, "fz": 1, "asc": 0, "balc": 1, "amu": 0, "libre": "ya"},
    {"id": "hortaleza", "ort": "Hortaleza", "hab": 2, "qm": 66, "pl": 2, "alq": 980, "gas": 40, "fz": 2, "asc": 1, "balc": 1, "amu": 0, "libre": "ya"},
    {"id": "comp-lavapies", "ort": "Lavapiés", "comp": 3, "qm": 12, "pl": 2, "alq": 450, "fz": 1, "libre": "ya"},
    {"id": "comp-moncloa", "ort": "Moncloa", "comp": 4, "qm": 14, "pl": 3, "alq": 520, "fz": 1, "libre": (1, 12)},
    {"id": "comp-usera", "ort": "Usera", "comp": 2, "qm": 10, "pl": 1, "alq": 380, "fz": 1, "libre": "ya"},
]
MOIS_DE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
MOIS_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
MOIS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
MOIS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MOIS_PT = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
ORD_DE = ["", "ersten", "zweiten", "dritten", "vierten", "fünften"]
ORD_ES = ["", "primera", "segunda", "tercera", "cuarta", "quinta"]
ORD_FR = ["", "premier", "deuxième", "troisième", "quatrième", "cinquième"]
ORD_EN = ["", "first", "second", "third", "fourth", "fifth"]
ORD_PT = ["", "primeiro", "segundo", "terceiro", "quarto", "quinto"]
NOMBRE_DE = ["null", "ein", "zwei", "drei", "vier", "fünf"]
NOMBRE_ES = ["cero", "una", "dos", "tres", "cuatro", "cinco"]
NOMBRE_FR = ["zéro", "une", "deux", "trois", "quatre", "cinq"]
NOMBRE_EN = ["zero", "one", "two", "three", "four", "five"]
NOMBRE_PT = ["zero", "um", "dois", "três", "quatro", "cinco"]

# LES PERSONNES QUI CHERCHENT (« Welche Anzeige passt? », DTZ Lesen) : leur visage vient de la famille (allemand)
# et de « Decrire » (espagnol) ; ce qu'elles cherchent est une donnee, la phrase en est tiree.
SUCHENDE_DE = [
    {"nom": "Lena", "visage": "familia/Lena-visage.webp", "il": "Sie", "z": 2, "blk": 1, "max": 950},
    {"nom": "Felix", "visage": "familia/Felix-visage.webp", "il": "Er", "z": 1, "ebk": 1, "sofort": 1, "max": 800},
    {"nom": "Sophie", "visage": "familia/Sophie-visage.webp", "il": "Sie", "wg": 1, "max": 500},
]
SUCHENDE_ES = [
    {"nom": "Elena", "il": "Elle", "visage": "descripcion/Elena-visage.webp", "hab": 2, "balc": 1, "max": 1100},
    {"nom": "Diego", "il": "Il", "visage": "descripcion/Diego-visage.webp", "amu": 1, "asc": 1, "max": 1250},
    {"nom": "Inés", "il": "Elle", "visage": "descripcion/Ines-visage.webp", "comp": 1, "max": 500},
]

# LES ABREVIATIONS DES ANNONCES ALLEMANDES (le mot du corpus qu'elles cachent)
ABK = [("Zi.", "Zimmer", "das"), ("Whg.", "Wohnung", "die"), ("KM", "Kaltmiete", "die"), ("NK", "Nebenkosten", "die"),
       ("EBK", "Einbauküche", "die"), ("OG", "Obergeschoss", "das"), ("EG", "Erdgeschoss", "das"), ("MM", "Monatsmiete", "die"),
       ("WG", "Wohngemeinschaft", "die"), ("m²", "Quadratmeter", "der")]

# LES DEFINITIONS (« Welches Wort passt? » et l'inverse) : le mot du corpus, la definition dans la langue apprise,
# et sa traduction (fr, en, pt ; de pour l'espagnol). A faire relire par un germanophone, comme toutes les phrases.
DEFS_DE = [
    ("Miete", "die", "Das Geld, das man jeden Monat für die Wohnung bezahlt.",
     "L'argent qu'on paie chaque mois pour le logement.", "The money you pay every month for the apartment.", "O dinheiro que se paga todo mês pelo apartamento."),
    ("Nebenkosten", "die", "Wasser, Heizung und Müll: Das bezahlt man zusätzlich zur Kaltmiete.",
     "L'eau, le chauffage et les ordures : on le paie en plus du loyer hors charges.", "Water, heating and rubbish: you pay this on top of the basic rent.", "Água, aquecimento e lixo: paga-se isso além do aluguel."),
    ("Kaution", "die", "Das Geld, das man am Anfang bezahlt und am Ende zurückbekommt.",
     "L'argent qu'on paie au début et qu'on récupère à la fin.", "The money you pay at the start and get back at the end.", "O dinheiro que se paga no início e se recebe de volta no fim."),
    ("Vermieterin", "die", "Ihr gehört die Wohnung, und sie vermietet sie.",
     "L'appartement est à elle, et elle le loue.", "She owns the apartment and rents it out.", "O apartamento é dela, e ela o aluga."),
    ("Mieter", "der", "Er wohnt in der Wohnung und bezahlt die Miete.",
     "Il habite l'appartement et paie le loyer.", "He lives in the apartment and pays the rent.", "Ele mora no apartamento e paga o aluguel."),
    ("Mietvertrag", "der", "Das Papier, das Mieter und Vermieter unterschreiben.",
     "Le papier que le locataire et le propriétaire signent.", "The paper that the tenant and the landlord sign.", "O papel que o inquilino e o proprietário assinam."),
    ("Erdgeschoss", "das", "Die Etage ganz unten, auf der Höhe der Straße.",
     "L'étage tout en bas, au niveau de la rue.", "The floor at the very bottom, at street level.", "O andar mais baixo, no nível da rua."),
    ("Etage", "die", "Ein Stockwerk im Haus: über dem Erdgeschoss die erste, dann die zweite und so weiter.",
     "Un niveau de l'immeuble : au-dessus du rez-de-chaussée le premier, puis le deuxième, et ainsi de suite.",
     "A level of the building: above the ground floor the first, then the second, and so on.",
     "Um andar do prédio: acima do térreo o primeiro, depois o segundo, e assim por diante."),
    ("Aufzug", "der", "Damit fährt man nach oben, ohne die Treppe zu nehmen.",
     "Avec lui, on monte sans prendre l'escalier.", "With it you go up without taking the stairs.", "Com ele se sobe sem usar a escada."),
    ("Keller", "der", "Der Raum ganz unten im Haus, unter dem Erdgeschoss.",
     "La pièce tout en bas de la maison, sous le rez-de-chaussée.", "The room at the very bottom of the house, below the ground floor.", "O cômodo mais embaixo da casa, abaixo do térreo."),
    ("Nachbar", "der", "Er wohnt im selben Haus, in der Wohnung nebenan.",
     "Il habite le même immeuble, dans l'appartement d'à côté.", "He lives in the same building, in the apartment next door.", "Ele mora no mesmo prédio, no apartamento ao lado."),
    ("Schlüssel", "der", "Damit öffnet man die Tür.",
     "Avec elle, on ouvre la porte.", "You open the door with it.", "Com ela se abre a porta."),
    ("Briefkasten", "der", "Hier kommen die Briefe an.",
     "C'est là qu'arrivent les lettres.", "This is where the letters arrive.", "É aqui que chegam as cartas."),
    ("Umzug", "der", "Man wechselt die Wohnung und bringt seine Sachen in die neue Wohnung.",
     "On change de logement et on emporte ses affaires dans le nouveau.", "You change apartments and take your things to the new one.", "Muda-se de apartamento e levam-se as coisas para o novo."),
    ("Mitbewohner", "der", "Er wohnt mit dir in der WG.",
     "Il habite avec toi dans la colocation.", "He lives with you in the shared apartment.", "Ele mora com você no apartamento compartilhado."),
    ("Balkon", "der", "Hier ist man draußen, aber noch in der Wohnung.",
     "Là, on est dehors, mais encore dans l'appartement.", "Here you are outside, but still in the apartment.", "Aqui se está do lado de fora, mas ainda no apartamento."),
]
DEFS_ES = [
    ("alquiler", "el", "El dinero que se paga cada mes por el piso.",
     "L'argent qu'on paie chaque mois pour l'appartement.", "The money you pay every month for the apartment.", "O dinheiro que se paga todo mês pelo apartamento.", "Das Geld, das man jeden Monat für die Wohnung bezahlt."),
    ("fianza", "la", "El dinero que se paga al principio y se recupera al final.",
     "L'argent qu'on paie au début et qu'on récupère à la fin.", "The money you pay at the start and get back at the end.", "O dinheiro que se paga no início e se recebe de volta no fim.", "Das Geld, das man am Anfang bezahlt und am Ende zurückbekommt."),
    ("propietario", "el", "Es el dueño del piso y lo alquila.",
     "C'est le propriétaire de l'appartement, et il le loue.", "He owns the apartment and rents it out.", "Ele é o dono do apartamento e o aluga.", "Ihm gehört die Wohnung, und er vermietet sie."),
    ("inquilino", "el", "Vive en el piso y paga el alquiler.",
     "Il habite l'appartement et paie le loyer.", "He lives in the apartment and pays the rent.", "Ele mora no apartamento e paga o aluguel.", "Er wohnt in der Wohnung und bezahlt die Miete."),
    ("contrato", "el", "El papel que firman el inquilino y el propietario.",
     "Le papier que le locataire et le propriétaire signent.", "The paper that the tenant and the landlord sign.", "O papel que o inquilino e o proprietário assinam.", "Das Papier, das Mieter und Vermieter unterschreiben."),
    ("ascensor", "el", "Sirve para subir sin usar la escalera.",
     "Il sert à monter sans prendre l'escalier.", "It takes you up without using the stairs.", "Serve para subir sem usar a escada.", "Damit fährt man nach oben, ohne die Treppe zu nehmen."),
    ("sótano", "el", "La parte del edificio que está debajo de la planta baja.",
     "La partie de l'immeuble qui est sous le rez-de-chaussée.", "The part of the building below the ground floor.", "A parte do prédio que fica abaixo do térreo.", "Der Teil des Hauses unter dem Erdgeschoss."),
    ("vecino", "el", "Vive en el mismo edificio, en el piso de al lado.",
     "Il habite le même immeuble, dans l'appartement d'à côté.", "He lives in the same building, in the apartment next door.", "Ele mora no mesmo prédio, no apartamento ao lado.", "Er wohnt im selben Haus, in der Wohnung nebenan."),
    ("llave", "la", "Sirve para abrir la puerta.",
     "Elle sert à ouvrir la porte.", "You use it to open the door.", "Serve para abrir a porta.", "Damit öffnet man die Tür."),
    ("buzón", "el", "Aquí llegan las cartas.",
     "C'est là qu'arrivent les lettres.", "This is where the letters arrive.", "É aqui que chegam as cartas.", "Hier kommen die Briefe an."),
    ("mudanza", "la", "Cuando cambias de casa y llevas tus cosas al piso nuevo.",
     "Quand on change de logement et qu'on emporte ses affaires dans le nouveau.", "When you move house and take your things to the new apartment.", "Quando se muda de casa e se levam as coisas para o apartamento novo.", "Man wechselt die Wohnung und bringt seine Sachen in die neue Wohnung."),
    ("trastero", "el", "Un cuarto pequeño para guardar las cosas que no usas.",
     "Une petite pièce pour ranger les affaires qu'on n'utilise pas.", "A small room to keep the things you don't use.", "Um cômodo pequeno para guardar as coisas que não se usam.", "Ein kleiner Raum für die Sachen, die man nicht benutzt."),
    ("balcón", "el", "Aquí estás fuera, pero todavía en el piso.",
     "Là, on est dehors, mais encore dans l'appartement.", "Here you are outside, but still in the apartment.", "Aqui se está do lado de fora, mas ainda no apartamento.", "Hier ist man draußen, aber noch in der Wohnung."),
]

# LES MOTS ABSENTS DU CORPUS (4 nov.) : prepares dans ajouts/ et espanol/ajouts/logement.json, pas appliques. Le
# tirage les tient « hors jeu » tant qu'ils n'y sont pas ; leurs gloses sont ecrites ici.
HORS_CORPUS = {
    "de": {"Kinderzimmer": {"fr": "chambre d'enfant", "en": "children's room", "pt": "quarto das crianças"},
           "Kaltmiete": {"fr": "loyer hors charges", "en": "basic rent (without bills)", "pt": "aluguel sem despesas"},
           "Monatsmiete": {"fr": "un mois de loyer", "en": "a month's rent", "pt": "um mês de aluguel"},
           "Quadratmeter": {"fr": "mètre carré", "en": "square metre", "pt": "metro quadrado"}},
    "es": {"bañera": {"fr": "la baignoire", "en": "bathtub", "pt": "a banheira", "de": "die Badewanne"},
           "fianza": {"fr": "la caution", "en": "deposit", "pt": "o depósito, a caução", "de": "die Kaution"}},
}


# ---------------------------------------------------------------------------------------------------------------
def charger_corpus():
    th = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))["themes"]
    te = json.load(io.open(os.path.join(RACINE, "espanol", "datos", "temas.json"), encoding="utf-8"))["themes"]
    def index(themes):
        out = {}
        for t in themes:
            for w in t.get("mots", []):
                out.setdefault((w.get("genre"), w["mot"]), []).append(w)
        return out
    def verbes(fichier):
        out = {}
        def parcourir(o):
            if isinstance(o, dict):
                if "infinitif" in o: out.setdefault(o["infinitif"], o)
                for v in o.values(): parcourir(v)
            elif isinstance(o, list):
                for v in o: parcourir(v)
        parcourir(json.load(io.open(os.path.join(RACINE, fichier), encoding="utf-8")))
        return out
    def adjectifs(fichier):
        out = {}
        d = json.load(io.open(os.path.join(RACINE, fichier), encoding="utf-8"))
        for l in d.values():
            if isinstance(l, list):
                for w in l:
                    if w.get("mot"): out.setdefault(w["mot"], w)
        return out
    return {"de": index(th), "es": index(te), "vde": verbes("verbe.json"), "ves": verbes(os.path.join("espanol", "datos", "verbos.json")),
            "ade": adjectifs("adjectif.json"), "aes": adjectifs(os.path.join("espanol", "datos", "adjetivos.json"))}


LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru", "de"]
champ = lambda w, l: w.get("traduction" if l == "fr" else "traduction_" + l)


def choisir(entrees, sens):
    """L'entree du corpus voulue : celle dont la traduction est « sens », sinon la premiere."""
    if sens:
        for w in entrees:
            if w.get("traduction") == sens: return w
    return entrees[0]


def maj(s):
    return s[0].upper() + s[1:]


def construire():
    C = charger_corpus()
    d = {"_lisez_moi": "FABRIQUE par visuel/logement/logement.py -- ne pas modifier a la main.",
         "pieces": {}, "objets": {}, "logements": {}, "photos": {}, "items": {"de": {}, "es": {}}, "mots": {"de": [], "es": []},
         "gloses": {"de": {}, "es": {}}, "choix": {"de": {}, "es": {}}, "annonces": {"de": {}, "es": {}}}
    # ---- les mots du theme, a la forme du corpus, et leurs gloses ----
    mots = {"de": {}, "es": {}}
    def mot(app, genre, m, cat=None, sens=None):
        k = (cat or "n") + ":" + m + (("|" + sens) if sens else "")
        if k in mots[app]: return k
        e = {"k": k, "mot": m}
        if genre: e["genre"] = genre
        if cat: e["cat"] = cat
        if sens: e["sens"] = sens
        mots[app][k] = e
        # la glose : le corpus relu ; sinon, les mots hors corpus (ecrits ici)
        if cat == "verbe":
            w = C["v" + app].get(m)
        elif cat == "adjectif":
            w = C["a" + app].get(m)
        else:
            w = (lambda l: choisir(l, sens) if l else None)(C[app].get((genre, m)))
        if w:
            d["gloses"][app][m if not sens else m + "|" + sens] = {l: champ(w, l) for l in LANGUES if champ(w, l)}
        elif m in HORS_CORPUS[app]:
            d["gloses"][app][m] = HORS_CORPUS[app][m]
        else:
            raise SystemExit("mot absent du corpus et sans glose : %s %s (%s)" % (genre, m, app))
        return k
    def glose_de(app, k):
        e = mots[app][k]
        return e["mot"] + ("|" + e["sens"] if e.get("sens") else "")

    # ---- les pieces ----
    for pid, p in list(PIECES.items()) + [("zimmer", MARKS_ZIMMER)]:
        d["pieces"][pid] = {"de": (p["de"][0] + " " + p["de"][1]).strip(), "deDat": p["dat"],
                            "es": p["es"][0] + " " + (p["es"][2] if len(p["es"]) > 2 else p["es"][1]),
                            "fr": p["fr"][0], "en": p["en"][0], "pt": p["pt"][0],
                            "kDe": mot("de", "das", "Zimmer") if pid == "zimmer" else mot("de", p["de"][0], p["de"][1]),
                            "kEs": mot("es", p["es"][0], p["es"][1])}
    def piece_txt(app, pid, forme):
        p = PIECES.get(pid) or MARKS_ZIMMER
        if app == "de": return {"nom": (p["de"][0] + " " + p["de"][1]).strip(), "dat": p["dat"]}[forme]
        es = p["es"][0] + " " + (p["es"][2] if len(p["es"]) > 2 else p["es"][1])
        return {"nom": es, "dat": ("en el balcón" if pid == "balkon" else "en " + es)}[forme]
    def piece_tr(l, pid, forme):
        p = PIECES.get(pid) or MARKS_ZIMMER
        return p[l][0 if forme == "nom" else 1]

    # ---- les objets ----
    def obj_tr(oid, l, app):
        o = OBJETS[oid][l]
        if isinstance(o, dict): o = o[app]
        return o
    def obj_fr(oid, app, defini=True):
        a, m, u = obj_tr(oid, "fr", app)
        return (a + m if a.endswith("'") else a + " " + m) if defini else u + " " + m
    def obj_en(oid, app): return "the " + obj_tr(oid, "en", app)
    def obj_pt(oid, app, defini=True):
        a, m, u = obj_tr(oid, "pt", app)
        return (a if defini else u) + " " + m
    for oid, o in OBJETS.items():
        es = o["es"]
        d["objets"][oid] = {"kDe": mot("de", o["de"][0], o["de"][1]), "kEs": mot("es", es[0], es[1], sens=es[3] if len(es) > 3 else None),
                            "de": o["de"][0] + " " + o["de"][1], "es": es[0] + " " + es[1], "piece": o["piece"]}

    # ---- les verbes ----
    INF = {"steht": "stehen", "liegt": "liegen", "hängt": "hängen"}
    for v in INF.values(): mot("de", None, v, "verbe")
    mot("es", None, "estar", "verbe")

    # ---- les photos : celles qui existent en webp entrent dans le jeu ----
    for iid, ph in PHOTOS.items():
        pret = os.path.exists(os.path.join(SORTIE, iid + ".webp"))
        d["photos"][iid] = {"logement": ph["logement"], "piece": ph["piece"], "pret": pret,
                            "reconnaissable": ph.get("reconnaissable", True), "personnes": ph["personnes"], "objets": list(ph["objets"])}
    for lid, lo in LOGEMENTS.items():
        d["logements"][lid] = {"titre": lo["titre"], "plan": [{"id": r[0], "piece": r[1], "x": r[2], "y": r[3], "w": r[4], "h": r[5]} for r in lo["plan"]]}

    I = d["items"]
    def ajouter(app, sorte, it):
        I[app].setdefault(sorte, []).append(it)
    def tr(fr, en, pt, de=None):
        t = {"fr": fr, "en": en, "pt": pt}
        if de: t["de"] = de
        return t

    for iid, ph in PHOTOS.items():
        if not d["photos"][iid]["pret"]: continue
        lo, pid = LOGEMENTS[ph["logement"]], ph["piece"]
        rec = ph.get("reconnaissable", True)
        pdat = d["pieces"][pid]
        # 1. « Welches Zimmer ist das? » -- la piece, au nominatif, et ses voisines pour leurres
        if rec:
            for app in ("de", "es"):
                nom = piece_txt(app, pid, "nom")
                if pid == "zimmer":
                    phrase = {"de": "Das ist Marks Zimmer.", "es": "Es la habitación de Mark."}[app]
                    t = tr("C'est la chambre de Mark.", "This is Mark's room.", "Este é o quarto do Mark.", "Das ist Marks Zimmer." if app == "es" else None)
                else:
                    phrase = ("Das ist " + nom + " " + lo["de"] + ".") if app == "de" else ("Es " + nom + " " + lo["es"] + ".")
                    t = tr("C'est " + piece_tr("fr", pid, "nom") + " " + lo["fr"] + ".", "This is " + piece_tr("en", pid, "nom") + " " + lo["en"] + ".",
                           maj(("Esta é " if piece_tr("pt", pid, "nom").startswith("a ") else "Este é ") + piece_tr("pt", pid, "nom") + " " + lo["pt"] + "."),
                           ("Das ist " + piece_txt("de", pid, "nom") + " " + lo["de"] + ".") if app == "es" and pid != "zimmer" else None)
                leurres = [piece_txt(app, v, "nom") for v in VOISINES[pid] if v != "zimmer"]
                k = pdat["kDe"] if app == "de" else pdat["kEs"]
                q = {"de": "Welches Zimmer ist das?", "es": "¿Qué parte de la casa es?"}[app]
                ajouter(app, "zimmer", {"img": iid, "q": q, "rep": nom, "leurres": leurres, "phrase": phrase, "trad": t, "mots": [k], "mot": k})
                # l'ecoute : la phrase dite, trois photos de pieces DIFFERENTES (le choix se fait a la page)
                ajouter(app, "entendre", {"img": iid, "piece": pid, "phrase": phrase, "trad": t, "mots": [k], "mot": k})
        # 2. « Wo ist Mark? » -- la personne et sa piece, au datif
        par_piece = {}
        for n, p in ph["personnes"].items(): par_piece.setdefault(p, []).append(n)
        if ph.get("becker"): pass
        for p, noms in par_piece.items():
            g = groupe_pers(noms)
            for app in ("de", "es"):
                lieu = piece_txt(app, p, "dat")
                pl = g[app][2]
                if app == "de":
                    q = "Wo " + ("sind " if pl else "ist ") + g["de"][1] + "?"
                    phrase = g["de"][0] + (" sind " if pl else " ist ") + lieu + "."
                    leurres = [piece_txt("de", v, "dat") for v in VOISINES[p] if v != "zimmer"]
                else:
                    q = "¿Dónde " + ("están " if pl else "está ") + g["es"][1] + "?"
                    phrase = g["es"][0] + (" están " if pl else " está ") + lieu + "."
                    leurres = [piece_txt("es", v, "dat") for v in VOISINES[p] if v != "zimmer"]
                plfr, plen, plpt = g["fr"][1], g["en"][1], g["pt"][1]
                t = tr(g["fr"][0] + (" sont " if plfr else " est ") + piece_tr("fr", p, "dat") + ".",
                       g["en"][0] + (" are " if plen else " is ") + piece_tr("en", p, "dat") + ".",
                       g["pt"][0] + (" estão " if plpt else " está ") + piece_tr("pt", p, "dat") + ".",
                       (g["de"][0] + (" sind " if g["de"][2] else " ist ") + piece_txt("de", p, "dat") + ".") if app == "es" else None)
                k = d["pieces"][p]["kDe" if app == "de" else "kEs"]
                rep = maj(lieu) + "." if app == "de" else maj(lieu) + "."
                ajouter(app, "wo", {"img": iid, "q": q, "rep": rep, "leurres": [maj(x) + "." for x in leurres], "phrase": phrase, "trad": t,
                                    "mots": [k] + (["verbe:estar"] if app == "es" else []), "mot": k})
                # en allemand, le datif de la piece : « Mark ist ___ Bad. » im / in der / ins ; auf dem Balkon
                if app == "de" and p != "zimmer":
                    art = lieu.rsplit(" ", 1)[0]
                    opts = {"im": ["im", "in der", "ins"], "in der": ["in der", "im", "in die"], "auf dem": ["auf dem", "im", "auf den"]}[art]
                    ajouter("de", "im", {"img": iid, "trou": g["de"][0] + (" sind " if pl else " ist ") + "___ " + PIECES[p]["de"][1] + ".",
                                         "rep": art, "opts": opts, "phrase": phrase, "trad": t, "mots": [k], "mot": k})
        # 3. les objets : le verbe (de), l'article, hay / esta (es), le datif de la piece (de), vrai ou faux
        for oid, (verbe, ort) in ph["objets"].items():
            o = OBJETS[oid]
            kde, kes = d["objets"][oid]["kDe"], d["objets"][oid]["kEs"]
            if ort:
                lde, les, lfr, len_, lpt = ORTS[ort]
            else:
                lde, les = piece_txt("de", pid, "dat"), piece_txt("es", pid, "dat")
                lfr, len_, lpt = piece_tr("fr", pid, "dat"), piece_tr("en", pid, "dat"), piece_tr("pt", pid, "dat")
            de_nom = maj(o["de"][0]) + " " + o["de"][1]
            es_nom = maj(o["es"][0]) + " " + o["es"][1]
            phrase_de = de_nom + " " + verbe + " " + lde + "."
            phrase_es = es_nom + " está " + les + "."
            t_obj = lambda app: tr(maj(obj_fr(oid, app)) + " est " + lfr + ".", maj(obj_en(oid, app)) + " is " + len_ + ".",
                                   maj(obj_pt(oid, app)) + " está " + lpt + ".", phrase_de if app == "es" else None)
            # l'article : « ___ Sofa steht im Wohnzimmer. » der / die / das ; « ___ sofá está en el salón. » El / La
            ajouter("de", "artikel", {"img": iid, "trou": "___ " + o["de"][1] + " " + verbe + " " + lde + ".", "rep": maj(o["de"][0]),
                                      "opts": ["Der", "Die", "Das"], "phrase": phrase_de, "trad": t_obj("de"), "mots": [kde], "mot": kde})
            ajouter("es", "artikel", {"img": iid, "trou": "___ " + o["es"][1] + " está " + les + ".", "rep": maj(o["es"][0]),
                                      "opts": ["El", "La"], "phrase": phrase_es, "trad": t_obj("es"), "mots": [kes], "mot": kes})
            # le verbe de position (de) : steht / liegt / haengt ; « ist » n'est pas demande
            if verbe in INF:
                kv = "verbe:" + INF[verbe]
                ajouter("de", "verbe", {"img": iid, "trou": de_nom + " ___ " + lde + ".", "rep": verbe, "opts": ["steht", "liegt", "hängt"],
                                        "phrase": phrase_de, "trad": t_obj("de"), "mots": [kv, kde], "mot": kv})
                faux_v = {"steht": "liegt", "liegt": "steht", "hängt": "steht"}[verbe]
                ajouter("de", "vraifaux", {"img": iid, "phrase": phrase_de, "vrai": True, "juste": phrase_de, "trad": t_obj("de"), "mots": [kv], "mot": kv})
                ajouter("de", "vraifaux", {"img": iid, "phrase": de_nom + " " + faux_v + " " + lde + ".", "vrai": False, "juste": phrase_de, "trad": t_obj("de"),
                                           "mots": [kv], "mot": kv, "choix": faux_v})
            # le datif de la piece (de), quand la place est la piece : « Das Bett steht ___ Kinderzimmer. »
            if not ort and pid != "zimmer":
                art = lde.rsplit(" ", 1)[0]
                opts = {"im": ["im", "in der", "ins"], "in der": ["in der", "im", "in die"], "auf dem": ["auf dem", "im", "auf den"]}[art]
                kp = d["pieces"][pid]["kDe"]
                ajouter("de", "im", {"img": iid, "trou": de_nom + " " + verbe + " ___ " + PIECES[pid]["de"][1] + ".", "rep": art, "opts": opts,
                                     "phrase": phrase_de, "trad": t_obj("de"), "mots": [kp, kde], "mot": kp})
            # hay ou esta (es) : « En la cocina hay una nevera. » / « La nevera está en la cocina. »
            un = {"el": "un", "la": "una"}[o["es"][0]]
            lieu_es = piece_txt("es", pid, "dat")
            hay = maj(lieu_es) + " hay " + un + " " + o["es"][1] + "."
            t_hay = tr(maj(piece_tr("fr", pid, "dat")) + ", il y a " + obj_fr(oid, "es", False) + ".",
                       "There is " + ("an " if obj_tr(oid, "en", "es")[0] in "aeiou" else "a ") + obj_tr(oid, "en", "es") + " " + piece_tr("en", pid, "dat") + ".",
                       maj(piece_tr("pt", pid, "dat")) + " há " + obj_pt(oid, "es", False) + ".",
                       maj(piece_txt("de", pid, "dat")) + " gibt es " + {"der": "einen", "die": "eine", "das": "ein"}[o["de"][0]] + " " + o["de"][1] + ".")
            ajouter("es", "hayEsta", {"img": iid, "trou": maj(lieu_es) + " ___ " + un + " " + o["es"][1] + ".", "rep": "hay", "opts": ["hay", "está"],
                                      "phrase": hay, "trad": t_hay, "mots": ["verbe:estar", kes], "mot": kes})
            if not ort:
                ajouter("es", "hayEsta", {"img": iid, "trou": es_nom + " ___ " + les + ".", "rep": "está", "opts": ["está", "hay"],
                                          "phrase": phrase_es, "trad": t_obj("es"), "mots": ["verbe:estar", kes], "mot": "verbe:estar"})
            # vrai : « Hier steht ein Bett. » / « Aquí hay una cama. »
            ein = {"der": "ein", "die": "eine", "das": "ein"}[o["de"][0]]
            vde = verbe if verbe in INF else "ist"
            for app in ("de", "es"):
                if app == "de":
                    ph_v = "Hier " + vde + " " + ein + " " + o["de"][1] + "."
                    k = kde
                else:
                    ph_v = "Aquí hay " + un + " " + o["es"][1] + "."
                    k = kes
                t = tr("Ici, il y a " + obj_fr(oid, app, False) + ".", "There is " + ("an " if obj_tr(oid, "en", app)[0] in "aeiou" else "a ") + obj_tr(oid, "en", app) + " here.",
                       "Aqui há " + obj_pt(oid, app, False) + ".", ("Hier gibt es " + {"der": "einen", "die": "eine", "das": "ein"}[o["de"][0]] + " " + o["de"][1] + ".") if app == "es" else None)
                ajouter(app, "vraifaux", {"img": iid, "phrase": ph_v, "vrai": True, "juste": ph_v, "trad": t, "mots": [k], "mot": k})
        # faux : un objet PROPRE a une autre sorte de piece (« Hier steht ein Herd. » dans une chambre)
        types = {pid} | ({"schlafzimmer"} if pid == "zimmer" else set())
        for oid, o in OBJETS.items():
            if not o["piece"] or set(o["piece"]) & types or oid in ph["objets"]: continue
            if pid == "balkon" or not rec: continue
            for app in ("de", "es"):
                if app == "de":
                    vrb = {"bett": "steht", "sofa": "steht", "kuehlschrank": "steht", "herd": "steht", "badewanne": "steht"}.get(oid, "ist")
                    ph_f = "Hier " + vrb + " " + {"der": "ein", "die": "eine", "das": "ein"}[o["de"][0]] + " " + o["de"][1] + "."
                    k = d["objets"][oid]["kDe"]
                    juste = "Das ist " + piece_txt("de", pid, "nom") + "." if pid != "zimmer" else "Das ist Marks Zimmer."
                else:
                    ph_f = "Aquí hay " + {"el": "un", "la": "una"}[o["es"][0]] + " " + o["es"][1] + "."
                    k = d["objets"][oid]["kEs"]
                    juste = "Es " + piece_txt("es", pid, "nom") + "."
                t = tr("C'est " + piece_tr("fr", pid, "nom") + ".", "This is " + piece_tr("en", pid, "nom") + ".",
                       maj(("Esta é " if piece_tr("pt", pid, "nom").startswith("a ") else "Este é ") + piece_tr("pt", pid, "nom") + "."),
                       ("Das ist " + piece_txt("de", pid, "nom") + ".") if app == "es" and pid != "zimmer" else ("Das ist Marks Zimmer." if app == "es" else None))
                ajouter(app, "vraifaux", {"img": iid, "phrase": ph_f, "vrai": False, "juste": juste, "trad": t, "mots": [k], "mot": k})
        # faux : une autre piece (« Das ist das Bad. » sur une cuisine) ; vrai : la bonne
        if rec:
            for app in ("de", "es"):
                k = d["pieces"][pid]["kDe" if app == "de" else "kEs"]
                juste = ("Das ist " + piece_txt("de", pid, "nom") + ".") if app == "de" else ("Es " + piece_txt("es", pid, "nom") + ".")
                if pid == "zimmer": juste = {"de": "Das ist Marks Zimmer.", "es": "Es la habitación de Mark."}[app]
                t = tr("C'est " + piece_tr("fr", pid, "nom") + ".", "This is " + piece_tr("en", pid, "nom") + ".",
                       maj(("Esta é " if piece_tr("pt", pid, "nom").startswith("a ") else "Este é ") + piece_tr("pt", pid, "nom") + "."),
                       ("Das ist " + piece_txt("de", pid, "nom") + ".") if app == "es" and pid != "zimmer" else ("Das ist Marks Zimmer." if app == "es" else None))
                ajouter(app, "vraifaux", {"img": iid, "phrase": juste, "vrai": True, "juste": juste, "trad": t, "mots": [k], "mot": k})
                for v in VOISINES[pid][:2]:
                    if v == "zimmer": continue
                    faux = ("Das ist " + piece_txt("de", v, "nom") + ".") if app == "de" else ("Es " + piece_txt("es", v, "nom") + ".")
                    kv = d["pieces"][v]["kDe" if app == "de" else "kEs"]
                    ajouter(app, "vraifaux", {"img": iid, "phrase": faux, "vrai": False, "juste": juste, "trad": t, "mots": [kv, k], "mot": k})
        # la visite : ce que Frau Becker montre (l'accusatif : den Balkon), ce que Lena signe
        if iid in VISITE:
            v = VISITE[iid]
            for app in ("de", "es"):
                q, rep, phrase, leurres, cle = v[app]
                if cle in PIECES: k = d["pieces"][cle]["kDe" if app == "de" else "kEs"]
                elif app == "de": k = mot("de", "der", "Mietvertrag")
                else: k = mot("es", "el", "contrato")
                t = tr(v["fr"], v["en"], v["pt"], v["de"][2] if app == "es" else None)
                ajouter(app, "visite", {"img": iid, "q": q, "rep": rep, "leurres": leurres, "phrase": phrase, "trad": t, "mots": [k], "mot": k})

    # ---- « Wo steht der Herd? » : touche la photo ; les leurres sont des pieces ou l'objet n'est sûrement pas ----
    for oid, o in OBJETS.items():
        if not o["piece"]: continue
        bons = [i for i, ph in PHOTOS.items() if d["photos"][i]["pret"] and oid in ph["objets"] and PHOTOS[i].get("reconnaissable", True)]
        faux = [i for i, ph in PHOTOS.items() if d["photos"][i]["pret"] and PHOTOS[i].get("reconnaissable", True)
                and ph["piece"] not in o["piece"] and not (ph["piece"] == "zimmer" and "schlafzimmer" in o["piece"]) and oid not in ph["objets"]]
        for i in bons:
            ph = PHOTOS[i]; verbe = ph["objets"][oid][0]
            vq = verbe if verbe in INF else "ist"
            pid = ph["piece"]
            lo = LOGEMENTS[ph["logement"]]
            phrase_de = maj(o["de"][0]) + " " + o["de"][1] + " " + vq + " " + piece_txt("de", pid, "dat") + "."
            phrase_es = maj(o["es"][0]) + " " + o["es"][1] + " está " + piece_txt("es", pid, "dat") + "."
            for app in ("de", "es"):
                k = d["objets"][oid]["kDe" if app == "de" else "kEs"]
                q = ("Wo " + vq + " " + o["de"][0] + " " + o["de"][1] + "?") if app == "de" else ("¿Dónde está " + o["es"][0] + " " + o["es"][1] + "?")
                t = tr(maj(obj_fr(oid, app)) + " est " + piece_tr("fr", pid, "dat") + ".", maj(obj_en(oid, app)) + " is " + piece_tr("en", pid, "dat") + ".",
                       maj(obj_pt(oid, app)) + " está " + piece_tr("pt", pid, "dat") + ".", phrase_de if app == "es" else None)
                ajouter(app, "ding", {"img": i, "q": q, "faux": faux, "phrase": phrase_de if app == "de" else phrase_es, "trad": t, "mots": [k], "mot": k})

    # ---- les plans : « Was ist neben dem Bad? », « zwischen », « Welches Zimmer ist das? » (le plan), compter ----
    for lid, lo in LOGEMENTS.items():
        pl = lo["plan"]
        nommer = lambda app, r, forme: ("Marks Zimmer" if forme == "nom" else "Marks Zimmer") if (r[0] == "zimmer-mark" and app == "de") else (
            ("la habitación de Mark") if r[0] == "zimmer-mark" else piece_txt(app, r[1], forme))
        dat_de = lambda r: "Marks Zimmer" if r[0] == "zimmer-mark" else {"der": "dem", "die": "der", "das": "dem"}[PIECES[r[1]]["de"][0]] + " " + PIECES[r[1]]["de"][1]
        fr_n = lambda r: "la chambre de Mark" if r[0] == "zimmer-mark" else piece_tr("fr", r[1], "nom")
        en_n = lambda r: "Mark's room" if r[0] == "zimmer-mark" else piece_tr("en", r[1], "nom")
        pt_n = lambda r: "o quarto do Mark" if r[0] == "zimmer-mark" else piece_tr("pt", r[1], "nom")
        fr_a = lambda r: (lambda s: "du" + s[2:] if s.startswith("le ") else "de " + s)(fr_n(r))
        pt_a = lambda r: (lambda s: "do" + s[1:] if s.startswith("o ") else "da" + s[1:])(pt_n(r))
        es_a = lambda r: (lambda s: "del" + s[2:] if s.startswith("el ") else "de " + s)(nommer("es", r, "nom"))
        utiles = [r for r in pl if r[1] not in ("flur",) and r[0] != "zimmer-2"]
        def voisins_lat(r):
            g = [s for s in utiles if s is not r and abs(s[3] - r[3]) < .01 and (abs(s[2] - (r[2] + r[4])) < .01 or abs(r[2] - (s[2] + s[4])) < .01)]
            return sorted(g, key=lambda s: s[2])
        for r in utiles:
            vs = voisins_lat(r)
            if not vs: continue
            kde = d["pieces"][r[1]]["kDe"]; kes = d["pieces"][r[1]]["kEs"]
            non = [s for s in utiles if s is not r and s not in vs]
            for v in vs:
                kvde, kves = d["pieces"][v[1]]["kDe"], d["pieces"][v[1]]["kEs"]
                # « Was ist neben dem Bad? » -> die Küche (un seul voisin parmi les choix)
                ajouter("de", "plan", {"plan": lid, "marque": [r[0]], "q": "Was ist neben " + dat_de(r) + "?", "rep": nommer("de", v, "nom"),
                                       "leurres": [nommer("de", s, "nom") for s in non], "phrase": maj(nommer("de", v, "nom")) + " ist neben " + dat_de(r) + ".",
                                       "trad": tr(maj(fr_n(v)) + " est à côté " + fr_a(r) + ".", maj(en_n(v)) + " is next to " + en_n(r) + ".",
                                                  maj(pt_n(v)) + " fica ao lado " + pt_a(r) + "."), "mots": [kvde, kde], "mot": kvde})
                ajouter("es", "plan", {"plan": lid, "marque": [r[0]], "q": "¿Qué hay al lado " + es_a(r) + "?", "rep": nommer("es", v, "nom"),
                                       "leurres": [nommer("es", s, "nom") for s in non], "phrase": maj(nommer("es", v, "nom")) + " está al lado " + es_a(r) + ".",
                                       "trad": tr(maj(fr_n(v)) + " est à côté " + fr_a(r) + ".", maj(en_n(v)) + " is next to " + en_n(r) + ".",
                                                  maj(pt_n(v)) + " fica ao lado " + pt_a(r) + ".", maj(nommer("de", v, "nom")) + " ist neben " + dat_de(r) + "."),
                                       "mots": [kves, kes], "mot": kves})
            if len(vs) == 2:
                a, b = vs
                ajouter("de", "plan", {"plan": lid, "marque": [a[0], b[0]], "q": "Was ist zwischen " + dat_de(a) + " und " + dat_de(b) + "?", "rep": nommer("de", r, "nom"),
                                       "leurres": [nommer("de", s, "nom") for s in non], "phrase": maj(nommer("de", r, "nom")) + " ist zwischen " + dat_de(a) + " und " + dat_de(b) + ".",
                                       "trad": tr(maj(fr_n(r)) + " est entre " + fr_n(a) + " et " + fr_n(b) + ".", maj(en_n(r)) + " is between " + en_n(a) + " and " + en_n(b) + ".",
                                                  maj(pt_n(r)) + " fica entre " + pt_n(a) + " e " + pt_n(b) + "."), "mots": [kde], "mot": kde})
                ajouter("es", "plan", {"plan": lid, "marque": [a[0], b[0]], "q": "¿Qué hay entre " + nommer("es", a, "nom") + " y " + nommer("es", b, "nom") + "?",
                                       "rep": nommer("es", r, "nom"), "leurres": [nommer("es", s, "nom") for s in non],
                                       "phrase": maj(nommer("es", r, "nom")) + " está entre " + nommer("es", a, "nom") + " y " + nommer("es", b, "nom") + ".",
                                       "trad": tr(maj(fr_n(r)) + " est entre " + fr_n(a) + " et " + fr_n(b) + ".", maj(en_n(r)) + " is between " + en_n(a) + " and " + en_n(b) + ".",
                                                  maj(pt_n(r)) + " fica entre " + pt_n(a) + " e " + pt_n(b) + ".", maj(nommer("de", r, "nom")) + " ist zwischen " + dat_de(a) + " und " + dat_de(b) + "."),
                                       "mots": [kes], "mot": kes})
        # la piece marquee, sans son nom (le plan montre ses meubles dessines)
        for r in pl:
            if r[0] in ("zimmer-2", "zimmer-mark"): continue
            for app in ("de", "es"):
                k = d["pieces"][r[1]]["kDe" if app == "de" else "kEs"]
                nom = nommer(app, r, "nom")
                ajouter(app, "planZimmer", {"plan": lid, "marque": [r[0]], "anonyme": True, "q": {"de": "Welches Zimmer ist markiert?", "es": "¿Qué parte de la casa está marcada?"}[app],
                                            "rep": nom, "leurres": [piece_txt(app, v, "nom") for v in VOISINES[r[1]] if v != "zimmer"],
                                            "phrase": ("Das ist " + nom + ".") if app == "de" else ("Es " + nom + "."),
                                            "trad": tr("C'est " + fr_n(r) + ".", "This is " + en_n(r) + ".", maj(("Esta é " if pt_n(r).startswith("a ") else "Este é ") + pt_n(r) + "."),
                                                       ("Das ist " + nommer("de", r, "nom") + ".") if app == "es" else None), "mots": [k], "mot": k})
        # compter : « Wie viele Zimmer hat Annas Wohnung? » -- le salon compte en allemand, pas en espagnol
        nde = sum(1 for r in pl if r[1] in ZIMMER_DE)
        nes = sum(1 for r in pl if r[1] in HAB_ES)
        tit = lo["titre"]
        ajouter("de", "zaehlen", {"plan": lid, "q": "Wie viele Zimmer hat die Wohnung?", "titre": tit["de"], "rep": NOMBRE_DE[nde].replace("ein", "Ein").capitalize() + (" Zimmer" if nde != 1 else " Zimmer"),
                                  "opts": [maj(NOMBRE_DE[n]) + " Zimmer" for n in sorted({nde, nde + 1, nde + 2, max(1, nde - 1)})][:3] if nde > 1 else ["Ein Zimmer", "Zwei Zimmer", "Drei Zimmer"],
                                  "phrase": tit["de"] + " hat " + NOMBRE_DE[nde] + " Zimmer.",
                                  "trad": tr(tit["fr"] + " a " + NOMBRE_FR[nde] + " pièces.", tit["en"] + " has " + NOMBRE_EN[nde] + " rooms.", tit["pt"] + " tem " + NOMBRE_PT[nde] + " cômodos."),
                                  "mots": [mot("de", "das", "Zimmer")], "mot": mot("de", "das", "Zimmer"), "note": "zaehlenDe"})
        ajouter("es", "zaehlen", {"plan": lid, "q": "¿Cuántas habitaciones tiene el piso?", "titre": tit["es"], "rep": maj(NOMBRE_ES[nes]) + (" habitación" if nes == 1 else " habitaciones"),
                                  "opts": [maj(NOMBRE_ES[n]) + (" habitación" if n == 1 else " habitaciones") for n in range(1, 5)],
                                  "phrase": tit["es"] + " tiene " + NOMBRE_ES[nes] + (" habitación." if nes == 1 else " habitaciones."),
                                  "trad": tr(tit["fr"] + " a " + NOMBRE_FR[nes] + (" chambre." if nes == 1 else " chambres."), tit["en"] + " has " + NOMBRE_EN[nes] + (" bedroom." if nes == 1 else " bedrooms."),
                                             tit["pt"] + " tem " + NOMBRE_PT[nes] + (" quarto." if nes == 1 else " quartos."), tit["de"] + " hat " + NOMBRE_DE[nes] + (" Schlafzimmer." if nes != 1 else " Schlafzimmer.")),
                                  "mots": [mot("es", "la", "habitación")], "mot": mot("es", "la", "habitación"), "note": "zaehlenEs"})
    # les choix de « zaehlen » : la bonne et deux voisines, toujours trois
    for app in ("de", "es"):
        for it in I[app]["zaehlen"]:
            n = [x for x in it["opts"] if x != it["rep"]][:2]
            it["opts"] = [it["rep"]] + n

    annonces_de(d, mot, I, tr)
    annonces_es(d, mot, I, tr)
    # ---- les definitions (dans les deux sens) ----
    for (m, g, defi, fr, en, pt) in DEFS_DE:
        k = mot("de", g, m)
        autres = [x for x in DEFS_DE if x[0] != m]
        ajouter("de", "wort", {"q": defi, "rep": g + " " + m, "leurres": [x[1] + " " + x[0] for x in autres], "phrase": defi, "trad": tr(fr, en, pt), "mots": [k], "mot": k})
        ajouter("de", "sens", {"q": "Was ist " + ("ein " if g != "die" else "eine ") + m + "?" if m not in ("Miete", "Nebenkosten", "Kaution") else "Was ist " + g + " " + m + "?",
                               "rep": defi, "leurres": [x[2] for x in autres], "phrase": defi, "trad": tr(fr, en, pt), "mots": [k], "mot": k, "long": True})
    for (m, g, defi, fr, en, pt, de) in DEFS_ES:
        k = mot("es", g, m)
        autres = [x for x in DEFS_ES if x[0] != m]
        ajouter("es", "wort", {"q": defi, "rep": g + " " + m, "leurres": [x[1] + " " + x[0] for x in autres], "phrase": defi, "trad": tr(fr, en, pt, de), "mots": [k], "mot": k})
        ajouter("es", "sens", {"q": "¿Qué es " + g + " " + m + "?", "rep": defi, "leurres": [x[2] for x in autres], "phrase": defi, "trad": tr(fr, en, pt, de), "mots": [k], "mot": k, "long": True})
    # ---- les abreviations (de) ----
    for (a, m, g) in ABK:
        k = mot("de", g, m)
        autres = [x for x in ABK if x[0] != a]
        gl = d["gloses"]["de"][m]
        ajouter("de", "abk", {"q": "Was bedeutet „" + a + "“?", "rep": m, "leurres": [x[1] for x in autres], "phrase": a + " heißt " + m + ".",
                              "trad": tr(a + " veut dire « " + m + " » : " + gl.get("fr", "") + ".", a + " means “" + m + "”: " + gl.get("en", gl.get("fr", "")) + ".",
                                         a + " quer dizer “" + m + "”: " + gl.get("pt", gl.get("fr", "")) + "."), "mots": [k], "mot": k})
        ajouter("de", "abkRev", {"q": "Wie steht „" + m + "“ in einer Anzeige?", "rep": a, "leurres": [x[0] for x in autres], "phrase": a + " heißt " + m + ".",
                                 "trad": tr(a + " veut dire « " + m + " » : " + gl.get("fr", "") + ".", a + " means “" + m + "”: " + gl.get("en", gl.get("fr", "")) + ".",
                                            a + " quer dizer “" + m + "”: " + gl.get("pt", gl.get("fr", "")) + "."), "mots": [k], "mot": k})

    # ---- le mot choisi, traduit (quand il est faux) : une piece, un groupe au datif, un verbe, un objet ----
    for app in ("de", "es"):
        ch = d["choix"][app]
        for pid in list(PIECES) + ["zimmer"]:
            g = d["gloses"][app]
            ch[piece_txt(app, pid, "nom")] = {"fr": piece_tr("fr", pid, "nom"), "en": piece_tr("en", pid, "nom"), "pt": piece_tr("pt", pid, "nom")}
            ch[maj(piece_txt(app, pid, "dat")) + "."] = {"fr": piece_tr("fr", pid, "dat"), "en": piece_tr("en", pid, "dat"), "pt": piece_tr("pt", pid, "dat")}
            if app == "es": ch[piece_txt(app, pid, "nom")]["de"] = piece_txt("de", pid, "nom")
        if app == "de":
            for v, inf in INF.items():
                ch[v] = {l: x for l, x in d["gloses"]["de"].get(inf, {}).items()}
        for (m, g, *_r) in (DEFS_DE if app == "de" else DEFS_ES):
            ch[g + " " + m] = dict(d["gloses"][app].get(m, {}))
        if app == "de":
            for (a, m, g) in ABK: ch[m] = dict(d["gloses"]["de"].get(m, {}))
    d["mots"] = {app: list(mots[app].values()) for app in ("de", "es")}
    return d


def date_de(f):
    return "ab sofort" if f == "sofort" else "ab dem %d. %s" % (f[0], MOIS_DE[f[1] - 1])
def date_court_de(f):
    return "ab sofort frei" if f == "sofort" else "frei ab %d.%d." % f


def annonces_de(d, mot, I, tr):
    """Le texte de chaque annonce (abrege, comme dans le DTZ) et ses questions."""
    A = d["annonces"]["de"]
    km_k, nk_k, kt_k = mot("de", "die", "Kaltmiete"), mot("de", "die", "Nebenkosten"), mot("de", "die", "Kaution")
    mi_k, zi_k, wo_k = mot("de", "die", "Miete"), mot("de", "das", "Zimmer"), mot("de", "die", "Wohnung")
    bl_k, au_k, et_k, eg_k = mot("de", "der", "Balkon"), mot("de", "der", "Aufzug"), mot("de", "die", "Etage"), mot("de", "das", "Erdgeschoss")
    wg_k, eb_k = mot("de", "die", "WG"), mot("de", "die", "Einbauküche")
    for a in ANNONCES_DE:
        et = "EG" if a["et"] == 0 else "%d. OG" % a["et"]
        if a.get("wg"):
            texte = "%s: WG-Zimmer in %der-WG, %d m², %s. Warmmiete %d €, Kaution 2 MM. %s" % (a["ort"], a["wg"], a["qm"], et, a["warm"], maj(date_court_de(a["frei"])).rstrip(".") + ".")
            warm, kt = a["warm"], a["warm"] * a["kt"]
        else:
            feats = ["Balkon" if a["blk"] else "ohne Balkon", "Aufzug" if a["aufz"] else "kein Aufzug", "EBK" if a["ebk"] else "ohne EBK"]
            texte = "%s: %d-Zi.-Whg., %d m², %s, %s. KM %d €, NK %d €, Kaution %d MM. %s" % (a["ort"], a["z"], a["qm"], et, ", ".join(feats), a["km"], a["nk"], a["kt"], maj(date_court_de(a["frei"])).rstrip(".") + ".")
            warm, kt = a["km"] + a["nk"], a["km"] * a["kt"]
        A[a["id"]] = {"texte": texte, "ort": a["ort"], "warm": warm}
        Q = []
        euros = lambda n: "%d €" % n
        if not a.get("wg"):
            Q.append(("Wie hoch ist die Kaltmiete?", euros(a["km"]), [euros(warm), euros(a["nk"])], "Die Kaltmiete ist %d Euro." % a["km"],
                      ("Le loyer hors charges est de %d euros." % a["km"], "The basic rent is %d euros." % a["km"], "O aluguel sem despesas é de %d euros." % a["km"]), [km_k, mi_k]))
            Q.append(("Wie hoch sind die Nebenkosten?", euros(a["nk"]), [euros(a["km"]), euros(warm)], "Die Nebenkosten sind %d Euro." % a["nk"],
                      ("Les charges sont de %d euros." % a["nk"], "The bills are %d euros." % a["nk"], "As despesas são de %d euros." % a["nk"]), [nk_k]))
            Q.append(("Wie hoch ist die Warmmiete?", euros(warm), [euros(a["km"]), euros(warm + a["nk"])], "Die Warmmiete ist %d Euro: %d plus %d." % (warm, a["km"], a["nk"]),
                      ("Le loyer charges comprises est de %d euros : %d plus %d." % (warm, a["km"], a["nk"]), "The total rent is %d euros: %d plus %d." % (warm, a["km"], a["nk"]),
                       "O aluguel com despesas é de %d euros: %d mais %d." % (warm, a["km"], a["nk"])), [mi_k, nk_k]))
            Q.append(("Wie viele Zimmer hat die Wohnung?", "%d" % a["z"], [str(x) for x in (a["z"] + 1, a["z"] + 2)], "Die Wohnung hat %s Zimmer." % NOMBRE_DE[a["z"]],
                      ("L'appartement a %s pièce%s." % (NOMBRE_FR[a["z"]], "s" if a["z"] > 1 else ""), "The apartment has %s room%s." % (NOMBRE_EN[a["z"]], "s" if a["z"] > 1 else ""),
                       "O apartamento tem %s cômodo%s." % (NOMBRE_PT[a["z"]], "s" if a["z"] > 1 else "")), [zi_k, wo_k]))
            ja = "Ja, die Wohnung hat einen Balkon." if a["blk"] else "Nein, die Wohnung hat keinen Balkon."
            Q.append(("Hat die Wohnung einen Balkon?", "Ja" if a["blk"] else "Nein", ["Nein" if a["blk"] else "Ja"], ja,
                      ("Oui, l'appartement a un balcon." if a["blk"] else "Non, l'appartement n'a pas de balcon.", "Yes, the apartment has a balcony." if a["blk"] else "No, the apartment has no balcony.",
                       "Sim, o apartamento tem varanda." if a["blk"] else "Não, o apartamento não tem varanda."), [bl_k]))
            ja = "Ja, das Haus hat einen Aufzug." if a["aufz"] else "Nein, das Haus hat keinen Aufzug."
            Q.append(("Gibt es einen Aufzug?", "Ja" if a["aufz"] else "Nein", ["Nein" if a["aufz"] else "Ja"], ja,
                      ("Oui, l'immeuble a un ascenseur." if a["aufz"] else "Non, l'immeuble n'a pas d'ascenseur.", "Yes, the building has a lift." if a["aufz"] else "No, the building has no lift.",
                       "Sim, o prédio tem elevador." if a["aufz"] else "Não, o prédio não tem elevador."), [au_k]))
            ja = "Ja, die Wohnung hat eine Einbauküche." if a["ebk"] else "Nein, die Wohnung hat keine Einbauküche."
            Q.append(("Gibt es eine Einbauküche?", "Ja" if a["ebk"] else "Nein", ["Nein" if a["ebk"] else "Ja"], ja,
                      ("Oui, la cuisine est équipée." if a["ebk"] else "Non, la cuisine n'est pas équipée.", "Yes, it has a fitted kitchen." if a["ebk"] else "No, it has no fitted kitchen.",
                       "Sim, a cozinha é equipada." if a["ebk"] else "Não, a cozinha não é equipada."), [eb_k]))
        else:
            Q.append(("Wie hoch ist die Miete?", euros(warm), [euros(warm - 60), euros(warm + 80)], "Die Miete ist %d Euro warm." % warm,
                      ("Le loyer est de %d euros, charges comprises." % warm, "The rent is %d euros, bills included." % warm, "O aluguel é de %d euros, com despesas." % warm), [mi_k]))
            Q.append(("Wie viele Personen wohnen in der WG?", str(a["wg"]), [str(a["wg"] + 1), str(a["wg"] - 1 if a["wg"] > 2 else a["wg"] + 2)],
                      "In der WG wohnen %s Personen." % NOMBRE_DE[a["wg"]].replace("ein", "eine"),
                      ("%s personnes habitent dans la colocation." % maj(NOMBRE_FR[a["wg"]]), "%s people live in the shared apartment." % maj(NOMBRE_EN[a["wg"]]),
                       "%s pessoas moram no apartamento compartilhado." % maj(NOMBRE_PT[a["wg"]].replace("dois", "duas"))), [wg_k]))
        # la caution, l'etage, la date : pour toutes
        Q.append(("Wie hoch ist die Kaution?", euros(kt), [euros(a.get("km", warm)), euros(kt + a.get("km", warm))], "Die Kaution ist %d Euro." % kt,
                  ("La caution est de %d euros." % kt, "The deposit is %d euros." % kt, "A caução é de %d euros." % kt), [kt_k]))
        if a["et"] == 0:
            Q.append(("In welcher Etage ist die Wohnung?", "im Erdgeschoss", ["in der ersten Etage", "in der zweiten Etage"], "Die Wohnung ist im Erdgeschoss.",
                      ("L'appartement est au rez-de-chaussée.", "The apartment is on the ground floor.", "O apartamento fica no térreo."), [eg_k, et_k]))
        else:
            n = a["et"]
            autres = ["im Erdgeschoss"] + ["in der %s Etage" % ORD_DE[x] for x in (n - 1, n + 1) if 0 < x <= 5]
            Q.append(("In welcher Etage ist die Wohnung?" if not a.get("wg") else "In welcher Etage ist die WG?", "in der %s Etage" % ORD_DE[n], autres[:2],
                      ("Die Wohnung" if not a.get("wg") else "Die WG") + " ist in der %s Etage." % ORD_DE[n],
                      ("C'est au %s étage." % ORD_FR[n], "It is on the %s floor." % ORD_EN[n], "Fica no %s andar." % ORD_PT[n]), [et_k]))
        f = a["frei"]
        autres = [x for x in ["ab sofort", "ab dem 1. Dezember", "ab dem 1. Januar", "ab dem 1. Februar", "ab dem 15. Dezember"] if x != date_de(f)]
        Q.append(("Ab wann ist " + ("die Wohnung" if not a.get("wg") else "das Zimmer") + " frei?", date_de(f), autres[:2],
                  ("Die Wohnung" if not a.get("wg") else "Das Zimmer") + " ist " + date_de(f) + " frei.",
                  ("C'est libre tout de suite." if f == "sofort" else "C'est libre à partir du %s %s." % ("1er" if f[0] == 1 else f[0], MOIS_FR[f[1] - 1]),
                   "It is free right away." if f == "sofort" else "It is free from %s %d." % (MOIS_EN[f[1] - 1], f[0]),
                   "Está livre agora mesmo." if f == "sofort" else "Está livre a partir de %d de %s." % (f[0], MOIS_PT[f[1] - 1])), [wo_k]))
        for (q, rep, leurres, phrase, (fr, en, pt), ks) in Q:
            I["de"].setdefault("annonce", []).append({"annonce": a["id"], "q": q, "rep": rep, "leurres": leurres, "phrase": phrase, "trad": tr(fr, en, pt), "mots": ks, "mot": ks[0]})
    # « Welche Anzeige passt? » : une seule annonce sur trois remplit TOUT ce que la personne cherche
    for s in SUCHENDE_DE:
        def passe(a):
            w = a["warm"] if a.get("wg") else a["km"] + a["nk"]
            if s.get("wg"): return bool(a.get("wg")) and w <= s["max"]
            if a.get("wg"): return False
            return a["z"] >= s.get("z", 1) and w <= s["max"] and (not s.get("blk") or a["blk"]) and (not s.get("ebk") or a["ebk"]) and (not s.get("sofort") or a["frei"] == "sofort")
        bons = [a["id"] for a in ANNONCES_DE if passe(a)]
        faux = [a["id"] for a in ANNONCES_DE if not passe(a)]
        if not bons or len(faux) < 2: raise SystemExit("passt : %s n'a pas d'annonce juste" % s["nom"])
        if s.get("wg"):
            besoin = "%s sucht ein WG-Zimmer. %s kann höchstens %d € warm bezahlen." % (s["nom"], s["il"], s["max"])
            fr = "%s cherche une chambre en colocation. Elle peut payer au plus %d € charges comprises." % (s["nom"], s["max"])
            ks = [wg_k, mi_k, wo_k]
        else:
            crit = ["mindestens %s Zimmern" % NOMBRE_DE[s["z"]].replace("ein", "einem") if s.get("z", 1) > 1 else None,
                    "einem Balkon" if s.get("blk") else None, "einer Einbauküche" if s.get("ebk") else None]
            crit = [c for c in crit if c]
            besoin = "%s sucht eine Wohnung mit %s%s. %s kann höchstens %d € warm bezahlen." % (s["nom"], " und ".join(crit), ", ab sofort" if s.get("sofort") else "", s["il"], s["max"])
            fr_c = [("au moins %s pièces" % NOMBRE_FR[s["z"]]) if s.get("z", 1) > 1 else None, "un balcon" if s.get("blk") else None, "une cuisine équipée" if s.get("ebk") else None]
            fr = "%s cherche un appartement avec %s%s. %s peut payer au plus %d € charges comprises." % (s["nom"], " et ".join(c for c in fr_c if c), ", libre tout de suite" if s.get("sofort") else "",
                                                                                                        "Elle" if s["il"] == "Sie" else "Il", s["max"])
            ks = ([zi_k] if s.get("z", 1) > 1 else []) + ([bl_k] if s.get("blk") else []) + ([eb_k] if s.get("ebk") else []) + [mi_k, wo_k]
        for b in bons:
            ort = A[b]["ort"]
            I["de"].setdefault("passt", []).append({"visage": s["visage"], "q": besoin, "rep": b, "faux": faux,
                                                    "phrase": "Die Anzeige aus %s passt zu %s." % (ort, s["nom"]),
                                                    "trad": tr("L'annonce de %s convient à %s. (%s)" % (ort, s["nom"], fr), "The ad from %s suits %s." % (ort, s["nom"]),
                                                               "O anúncio de %s serve para %s." % (ort, s["nom"])), "mots": ks, "mot": ks[0]})


def date_es(f):
    return "ya" if f == "ya" else "a partir del %d de %s" % (f[0], MOIS_ES[f[1] - 1])


def annonces_es(d, mot, I, tr):
    A = d["annonces"]["es"]
    al_k, fz_k, hb_k, pi_k = mot("es", "el", "alquiler"), mot("es", "la", "fianza"), mot("es", "la", "habitación"), mot("es", "el", "piso")
    as_k, bc_k = mot("es", "el", "ascensor"), mot("es", "el", "balcón")
    am_k = mot("es", None, "amueblado", "adjectif")
    for a in ANNONCES_ES:
        planta = "planta baja" if a["pl"] == 0 else "%d.ª planta" % a["pl"]
        libre = "Libre ya" if a["libre"] == "ya" else "Libre a partir del %d de %s" % (a["libre"][0], MOIS_ES[a["libre"][1] - 1])
        if a.get("comp"):
            texte = "%s: habitación en piso compartido (%d personas), %d m², %s. %d €/mes, gastos incluidos. Fianza: %d mes. %s." % (
                a["ort"], a["comp"], a["qm"], planta, a["alq"], a["fz"], libre)
            total = a["alq"]
        else:
            feats = ["con ascensor" if a["asc"] else "sin ascensor", "con balcón" if a["balc"] else "sin balcón", "amueblado" if a["amu"] else "sin amueblar"]
            texte = "%s: piso de %d hab., %d m², %s, %s. %d €/mes + %d € de gastos. Fianza: %d %s. %s." % (
                a["ort"], a["hab"], a["qm"], planta, ", ".join(feats), a["alq"], a["gas"], a["fz"], "mes" if a["fz"] == 1 else "meses", libre)
            total = a["alq"] + a["gas"]
        fz = a["alq"] * a["fz"]
        A[a["id"]] = {"texte": texte, "ort": a["ort"], "total": total}
        euros = lambda n: "%d €" % n
        Q = []
        if not a.get("comp"):
            Q.append(("¿Cuánto es el alquiler?", euros(a["alq"]), [euros(total), euros(a["gas"])], "El alquiler es de %d euros al mes." % a["alq"],
                      ("Le loyer est de %d euros par mois." % a["alq"], "The rent is %d euros a month." % a["alq"], "O aluguel é de %d euros por mês." % a["alq"],
                       "Die Miete ist %d Euro im Monat." % a["alq"]), [al_k]))
            Q.append(("¿Cuánto se paga al mes en total?", euros(total), [euros(a["alq"]), euros(total + a["gas"])], "En total se pagan %d euros al mes: %d más %d." % (total, a["alq"], a["gas"]),
                      ("Au total, on paie %d euros par mois : %d plus %d." % (total, a["alq"], a["gas"]), "In total you pay %d euros a month: %d plus %d." % (total, a["alq"], a["gas"]),
                       "No total, pagam-se %d euros por mês: %d mais %d." % (total, a["alq"], a["gas"]), "Insgesamt zahlt man %d Euro im Monat: %d plus %d." % (total, a["alq"], a["gas"])), [al_k]))
            Q.append(("¿Cuántas habitaciones tiene el piso?", str(a["hab"]), [str(a["hab"] + 1), str(a["hab"] + 2)],
                      "El piso tiene %s habitaci%s." % (NOMBRE_ES[a["hab"]], "ón" if a["hab"] == 1 else "ones"),
                      ("L'appartement a %s chambre%s." % (NOMBRE_FR[a["hab"]], "s" if a["hab"] > 1 else ""), "The apartment has %s bedroom%s." % (NOMBRE_EN[a["hab"]], "s" if a["hab"] > 1 else ""),
                       "O apartamento tem %s quarto%s." % (NOMBRE_PT[a["hab"]], "s" if a["hab"] > 1 else ""), "Die Wohnung hat %s Schlafzimmer." % NOMBRE_DE[a["hab"]]), [hb_k, pi_k]))
            for (q, c, k, oui, non) in (("¿Tiene ascensor el edificio?", a["asc"], as_k, ("Sí, el edificio tiene ascensor.", "Oui, l'immeuble a un ascenseur.", "Yes, the building has a lift.", "Sim, o prédio tem elevador.", "Ja, das Haus hat einen Aufzug."),
                                         ("No, el edificio no tiene ascensor.", "Non, l'immeuble n'a pas d'ascenseur.", "No, the building has no lift.", "Não, o prédio não tem elevador.", "Nein, das Haus hat keinen Aufzug.")),
                                        ("¿Tiene balcón el piso?", a["balc"], bc_k, ("Sí, el piso tiene balcón.", "Oui, l'appartement a un balcon.", "Yes, the apartment has a balcony.", "Sim, o apartamento tem varanda.", "Ja, die Wohnung hat einen Balkon."),
                                         ("No, el piso no tiene balcón.", "Non, l'appartement n'a pas de balcon.", "No, the apartment has no balcony.", "Não, o apartamento não tem varanda.", "Nein, die Wohnung hat keinen Balkon.")),
                                        ("¿Está amueblado el piso?", a["amu"], am_k, ("Sí, el piso está amueblado.", "Oui, l'appartement est meublé.", "Yes, the apartment is furnished.", "Sim, o apartamento é mobiliado.", "Ja, die Wohnung ist möbliert."),
                                         ("No, el piso no está amueblado.", "Non, l'appartement n'est pas meublé.", "No, the apartment is not furnished.", "Não, o apartamento não é mobiliado.", "Nein, die Wohnung ist nicht möbliert."))):
                x = oui if c else non
                Q.append((q, "Sí" if c else "No", ["No" if c else "Sí"], x[0], x[1:], [k]))
        else:
            Q.append(("¿Cuánto es el alquiler?", euros(a["alq"]), [euros(a["alq"] - 50), euros(a["alq"] + 70)], "El alquiler es de %d euros al mes, con los gastos incluidos." % a["alq"],
                      ("Le loyer est de %d euros par mois, charges comprises." % a["alq"], "The rent is %d euros a month, bills included." % a["alq"],
                       "O aluguel é de %d euros por mês, com despesas incluídas." % a["alq"], "Die Miete ist %d Euro im Monat, mit Nebenkosten." % a["alq"]), [al_k]))
            Q.append(("¿Cuántas personas viven en el piso?", str(a["comp"]), [str(a["comp"] + 1), str(a["comp"] - 1 if a["comp"] > 2 else a["comp"] + 2)],
                      "En el piso viven %s personas." % NOMBRE_ES[a["comp"]].replace("una", "una"),
                      ("%s personnes habitent dans l'appartement." % maj(NOMBRE_FR[a["comp"]]), "%s people live in the apartment." % maj(NOMBRE_EN[a["comp"]]),
                       "%s pessoas moram no apartamento." % maj(NOMBRE_PT[a["comp"]].replace("dois", "duas")), "In der Wohnung wohnen %s Personen." % NOMBRE_DE[a["comp"]]), [pi_k]))
        Q.append(("¿Cuánto es la fianza?", euros(fz), [euros(fz + a["alq"]) if a["fz"] == 1 else euros(a["alq"]), euros(fz + 2 * a["alq"])], "La fianza es de %d euros." % fz,
                  ("La caution est de %d euros." % fz, "The deposit is %d euros." % fz, "A caução é de %d euros." % fz, "Die Kaution ist %d Euro." % fz), [fz_k]))
        n = a["pl"]
        rep = "en la planta baja" if n == 0 else "en la %s planta" % ORD_ES[n]
        autres = [x for x in (["en la planta baja"] + ["en la %s planta" % ORD_ES[m] for m in range(1, 6)]) if x != rep]
        autres = sorted(autres, key=lambda x: abs((["en la planta baja"] + ["en la %s planta" % ORD_ES[m] for m in range(1, 6)]).index(x) - n))[:2]
        Q.append(("¿En qué planta está?", rep, autres, ("El piso está " if not a.get("comp") else "La habitación está ") + rep + ".",
                  (("C'est au rez-de-chaussée." if n == 0 else "C'est au %s étage." % ORD_FR[n]), ("It is on the ground floor." if n == 0 else "It is on the %s floor." % ORD_EN[n]),
                   ("Fica no térreo." if n == 0 else "Fica no %s andar." % ORD_PT[n]), ("Sie ist im Erdgeschoss." if n == 0 else "Sie ist in der %s Etage." % ORD_DE[n])), [pi_k]))
        f = a["libre"]
        autres = [x for x in ["ya", "a partir del 1 de diciembre", "a partir del 1 de enero", "a partir del 1 de febrero", "a partir del 15 de diciembre"] if x != date_es(f)]
        Q.append(("¿Desde cuándo está libre?", date_es(f), autres[:2], ("Ya está libre." if f == "ya" else "Está libre " + date_es(f) + "."),
                  ("C'est libre tout de suite." if f == "ya" else "C'est libre à partir du %s %s." % ("1er" if f[0] == 1 else f[0], MOIS_FR[f[1] - 1]),
                   "It is free right away." if f == "ya" else "It is free from %s %d." % (MOIS_EN[f[1] - 1], f[0]),
                   "Está livre agora mesmo." if f == "ya" else "Está livre a partir de %d de %s." % (f[0], MOIS_PT[f[1] - 1]),
                   "Sie ist ab sofort frei." if f == "ya" else "Sie ist ab dem %d. %s frei." % (f[0], MOIS_DE[f[1] - 1])), [pi_k]))
        for (q, rep, leurres, phrase, (fr, en, pt, de), ks) in Q:
            I["es"].setdefault("annonce", []).append({"annonce": a["id"], "q": q, "rep": rep, "leurres": leurres, "phrase": phrase, "trad": tr(fr, en, pt, de), "mots": ks, "mot": ks[0]})
    for s in SUCHENDE_ES:
        def passe(a):
            if s.get("comp"): return bool(a.get("comp")) and a["alq"] <= s["max"]
            if a.get("comp"): return False
            return a["hab"] >= s.get("hab", 1) and a["alq"] + a["gas"] <= s["max"] and (not s.get("balc") or a["balc"]) and (not s.get("amu") or a["amu"]) and (not s.get("asc") or a["asc"])
        bons = [a["id"] for a in ANNONCES_ES if passe(a)]
        faux = [a["id"] for a in ANNONCES_ES if not passe(a)]
        if not bons or len(faux) < 2: raise SystemExit("passt : %s n'a pas d'annonce juste" % s["nom"])
        if s.get("comp"):
            besoin = "%s busca una habitación en un piso compartido. Puede pagar como máximo %d € al mes." % (s["nom"], s["max"])
            fr = "%s cherche une chambre en colocation. Elle peut payer au plus %d € par mois." % (s["nom"], s["max"])
            de = "%s sucht ein WG-Zimmer. Sie kann höchstens %d € im Monat bezahlen." % (s["nom"], s["max"])
            ks = [hb_k, al_k, pi_k]
        else:
            crit = [("al menos %s habitaciones" % NOMBRE_ES[s["hab"]]) if s.get("hab", 1) > 1 else None, "balcón" if s.get("balc") else None, "ascensor" if s.get("asc") else None]
            crit = [c for c in crit if c]
            besoin = "%s busca un piso%s%s%s. Puede pagar como máximo %d € al mes en total." % (s["nom"], " amueblado" if s.get("amu") else "", " con " if crit else "", " y ".join(crit), s["max"])
            fr = "%s cherche un appartement%s%s. %s peut payer au plus %d € par mois au total." % (s["nom"], " meublé" if s.get("amu") else "",
                  (" avec " + " et ".join(x for x in [("au moins %s chambres" % NOMBRE_FR[s["hab"]]) if s.get("hab", 1) > 1 else None, "un balcon" if s.get("balc") else None, "un ascenseur" if s.get("asc") else None] if x)) if crit else "", s["il"], s["max"])
            de = None
            ks = ([hb_k] if s.get("hab", 1) > 1 else []) + ([bc_k] if s.get("balc") else []) + ([as_k] if s.get("asc") else []) + ([am_k] if s.get("amu") else []) + [al_k, pi_k]
        for b in bons:
            ort = A[b]["ort"]
            I["es"].setdefault("passt", []).append({"visage": s["visage"], "q": besoin, "rep": b, "faux": faux,
                                                    "phrase": "El anuncio de %s es para %s." % (ort, s["nom"]),
                                                    "trad": tr("L'annonce de %s convient à %s. (%s)" % (ort, s["nom"], fr), "The ad from %s suits %s." % (ort, s["nom"]),
                                                               "O anúncio de %s serve para %s." % (ort, s["nom"]), "Die Anzeige aus %s passt zu %s." % (ort, s["nom"])), "mots": ks, "mot": ks[0]})


# ---------------------------------------------------------------------------------------------------------------
# LES PHOTOS REPRISES : recadrees en 4:3 (une scene est en hauteur : la bande de 4:3 qui montre la piece), 960 px
def reprendre():
    from PIL import Image
    os.makedirs(SORTIE, exist_ok=True)
    n = 0
    for iid, ph in PHOTOS.items():
        if not ph["src"]: continue
        src, y0 = ph["src"]
        im = Image.open(os.path.join(PROTO, src)).convert("RGB")
        if im.height > im.width:
            h = round(im.width * .75)
            im = im.crop((0, y0, im.width, y0 + h))
        im = im.resize((960, 720), Image.LANCZOS)
        im.save(os.path.join(SORTIE, iid + ".webp"), quality=78, method=6)
        n += 1
    print("  %d photos reprises dans visuel/prototype/logement/" % n)


# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES NEUVES (planche d'essai, 6 images, 0,90 $ : ACCORD DE JACQUES avant tout --payer)
GARDE = ("A real photograph, taken with a good phone camera and looking exactly like a phone photograph, in a 4:3 landscape picture, "
         "everything in sharp focus, natural colours, the textures of real wood, plaster, paint, fabric, tiles, plants and skin. "
         "Nothing in the picture carries any readable writing, numbers, logos or brands. ")
BECKER = ("FRAU BECKER, the landlady: a friendly woman in her early sixties, short grey hair, rimless glasses, a beige cardigan over a "
          "light-blue blouse, dark trousers, holding a plain dark-blue folder; ")
VIDE = ("an EMPTY flat for rent in an old Berlin building (Altbau): freshly painted white walls, light oak floorboards, high ceilings with "
        "a simple white stucco border, tall white wooden double windows, white radiators under the windows, no furniture at all, no boxes, "
        "no curtains; ")
NEUVES = {
    "anna-balkon": (["Anna", "anna-cuisine"], "The small balcony of Anna's flat in an old Berlin building, in the late afternoon sun. The second "
                    "reference picture shows her kitchen in the same flat: the same old building, the same tall white wooden windows. A narrow "
                    "balcony with a black wrought-iron railing, a small round metal bistro table and two folding metal chairs, several green "
                    "plants and red geraniums in terracotta pots on the floor and on the railing; behind the railing, the green trees of a Berlin "
                    "inner courtyard and the facade of the building opposite. Anna, exactly as in the first reference picture (same face, same "
                    "dark-blonde hair, same height), in a light-grey sweater and jeans, waters the plants with a small green watering can, smiling. "
                    "Seen from the open balcony door, the white door frame visible on the left edge."),
    "mark-flur":   (["Mark", "mark-salon"], "The hallway of Mark's shared flat, in the same old Berlin building as the living room of the second "
                    "reference picture: the same light wooden floorboards, the same white walls and white panelled doors. A long, narrow hallway "
                    "seen from one end; two white panelled doors on the side, a row of coat hooks with jackets and a backpack, a tall mirror in a "
                    "simple wooden frame hanging on the wall, a ceiling lamp with a round white paper shade switched on, a long striped runner rug "
                    "on the floor, two pairs of sneakers under the hooks. Mark, exactly as in the first reference picture (same face, same dark "
                    "curly hair), just home in a dark jacket, hangs his scarf on a hook, a bunch of keys in his other hand."),
    "visite-cuisine": (["Lena"], VIDE + "THE KITCHEN of this flat: a fitted kitchen along one wall with white cupboards, a light wooden worktop, a "
                    "stainless-steel sink and tap, a white electric stove with an oven, a tall white fridge, white wall cupboards above; the rest "
                    "of the kitchen is empty. " + BECKER + "she opens a wall cupboard and shows it with her other hand. LENA, exactly as in the "
                    "reference picture (same face, hair, height, clothes), visits the flat: she looks at the kitchen with interest, a small "
                    "notebook in her hand. Both are seen whole from head to shoes; their shoes stand on the floorboards with their shadows under them."),
    "visite-bad":  (["Lena", "visite-cuisine"], "The same empty flat for rent as in the second reference picture (same building, same white walls "
                    "and light oak floorboards in the hallway). THE BATHROOM: white tiles up to shoulder height, a white bathtub along the back "
                    "wall, a white washbasin with a chrome tap and a rectangular mirror hanging above it, a small frosted window, a white towel "
                    "radiator; no towels, no bottles, empty and clean. Frau Becker, exactly as in the second reference picture, stands in the "
                    "bathroom and points at the bathtub; Lena, exactly as in the first reference picture, looks in from the open door."),
    "visite-balkon": (["Lena", "visite-cuisine"], "The same empty flat for rent as in the second reference picture. THE LIVING ROOM: a large, "
                    "bright, completely empty room with light oak floorboards, white walls and an open glass balcony door at the back. Lena, "
                    "exactly as in the first reference picture, stands OUTSIDE on the balcony, behind a black iron railing, looking out at the "
                    "green trees, delighted; Frau Becker, exactly as in the second reference picture, waits inside in the empty room, holding "
                    "her folder."),
    "visite-vertrag": (["Lena", "visite-cuisine"], "The same empty kitchen as in the second reference picture (same white fitted kitchen, same "
                    "light wooden worktop). Lena, exactly as in the first reference picture, signs a document of two plain white pages with a pen "
                    "on the kitchen worktop (the pages show only grey lines, nothing readable); Frau Becker, exactly as in the second reference "
                    "picture, smiles and holds out a bunch of two keys to her."),
}
def references(iid):
    refs, qui = [], NEUVES[iid][0]
    for r in qui:
        if r == "Mark": refs.append(PRINCIPAL + "/personnages/Mark.png")
        elif r == "Anna": refs.append(FAMILLE + "/Anna-quotidien.png")
        elif r == "Lena": refs.append(FAMILLE + "/Lena.png")
        elif r in NEUVES: refs.append(os.path.join(IMG, r + ".png"))
        else: refs.append(os.path.join(SORTIE, r + ".webp"))
    return refs


def payer(ids):
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    os.makedirs(IMG, exist_ok=True)
    a_faire = [i for i in (ids or list(NEUVES)) if i in NEUVES and not os.path.exists(os.path.join(IMG, i + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    cle = O.cle()
    for iid in a_faire:
        refs = references(iid)
        manque = [r for r in refs if not os.path.exists(r)]
        if manque:
            print("  %s : reference absente %s -- sautee" % (iid, manque)); continue
        prompt = GARDE + NEUVES[iid][1]
        urls = []
        for r in refs:
            typ = "image/webp" if r.endswith(".webp") else "image/png"
            urls.append(O.deposer(r, typ, cle)[0])
        corps = {"prompt": prompt, "aspect_ratio": "4:3", "resolution": "2K", "output_format": "png", "num_images": 1, "image_urls": urls}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle)
        sortie = os.path.join(IMG, iid + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(IMG, iid + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": EDIT, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "references": [os.path.basename(r) for r in refs], "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


def webp():
    from PIL import Image
    for iid in NEUVES:
        src = os.path.join(IMG, iid + ".png")
        if not os.path.exists(src): continue
        im = Image.open(src).convert("RGB").resize((960, 720), Image.LANCZOS)
        im.save(os.path.join(SORTIE, iid + ".webp"), quality=78, method=6)
        print("  ", iid)


def ecrire_voix(d):
    """LES VOIX A ENREGISTRER (accord de Jacques, ElevenLabs v2) : chaque phrase dite apres une reponse. Les phrases
    a chiffres (les annonces) restent a la voix du telephone, comme les prix de « Manger »."""
    v = {"_lisez_moi": "FABRIQUE par visuel/logement/logement.py : les textes a enregistrer (ElevenLabs v2, accord de Jacques). Sans chiffres.", "de": [], "es": []}
    for app in ("de", "es"):
        s = set()
        for sorte, items in d["items"][app].items():
            for it in items:
                for t in (it.get("phrase"), it.get("juste")):
                    if t and not any(c.isdigit() for c in t): s.add(t)
        v[app] = sorted(s)
    v["credits"] = {"de (Aurora)": sum(len(t) for t in v["de"]), "es (Lolita + Monica)": 2 * sum(len(t) for t in v["es"])}
    io.open(os.path.join(ICI, "voix.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(v, ensure_ascii=False, indent=1) + "\n")
    return v["credits"]


def ecrire_json():
    os.makedirs(SORTIE, exist_ok=True)
    d = construire()
    print("  voix a enregistrer (credits) :", ecrire_voix(d))
    io.open(os.path.join(SORTIE, "logement.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "\n")
    for app in ("de", "es"):
        print("  %s : %s" % (app, ", ".join("%s %d" % (k, len(v)) for k, v in d["items"][app].items())))
    print("  photos pretes : %d / %d" % (sum(1 for p in d["photos"].values() if p["pret"]), len(d["photos"])))


def main():
    a = sys.argv[1:]
    if "--montrer" in a:
        for iid in NEUVES:
            print("\n  %s  (%s)\n  %s" % (iid, ", ".join(os.path.basename(r) for r in references(iid)), GARDE + NEUVES[iid][1]))
        print("\n  %d images, %.2f $" % (len(NEUVES), len(NEUVES) * PRIX))
        return
    if "--payer" in a:
        payer([x for x in a if not x.startswith("--")])
    if "--webp" in a:
        webp()
    reprendre()
    ecrire_json()


if __name__ == "__main__":
    main()
