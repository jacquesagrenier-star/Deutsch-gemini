# -*- coding: utf-8 -*-
"""« EN VILLE : S'ORIENTER » (theme illustre, vague 3, 4 nov. 2026) : les lieux de la ville, demander et donner son
chemin, situer un lieu sur un petit plan. Allemand (Berlin, le quartier de Mark : il habite Gartenstrasse 12) et
espagnol (Madrid, la ville de la serie espagnole).

LA SEULE SOURCE du theme. Elle fabrique visuel/prototype/ciudad/ciudad.json :
  - le PLAN du quartier (deux longues rues, trois rues transversales, 24 maisons dont 18 lieux) : la page le dessine,
    aucune image a payer pour lui ;
  - les FAITS de chaque lieu, mesures sur le plan (neben / al lado de, gegenueber / enfrente de, zwischen / entre,
    an der Ecke / en la esquina, in der ...strasse / en la calle ...) ;
  - les ITINERAIRES : depuis chacun des quatre « Sie sind hier » / « Usted esta aqui », le chemin le plus simple
    (deux virages au plus) vers chaque lieu, et ses phrases, en deux tournures (« die zweite Strasse links » et « bis
    zur zweiten Kreuzung ... links ab »), avec les fausses descriptions de la serie « beschreibung » ;
  - les phrases traduites (fr, en, pt, et de pour qui apprend l'espagnol) et les gloses du corpus (les autres langues).
Aucune phrase n'est ecrite dans la page : tout vient d'ici.

    python visuel/ciudad/ciudad.py              -> ciudad.json
    python visuel/ciudad/ciudad.py --recadrer   -> les photos gratuites, prises dans les scenes Kreuzung et Stadtplatz
    python visuel/ciudad/ciudad.py --montrer    -> les prompts des photos a payer et leur cout (gratuit)
    python visuel/ciudad/ciudad.py --payer [ids]-> fal nano-banana-pro, 0,15 $ l'image (ACCORD DE JACQUES d'abord)
    python visuel/ciudad/ciudad.py --webp       -> les originaux (visuel/ciudad/img/, hors depot) en webp
"""
import io, json, os, sys, time

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype", "ciudad")
IMG = os.path.join(ICI, "img")
MODELE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15
# les originaux des personnes (hors depot) : Mark detoure, la reference de toutes ses images
PERSONNES = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI/visuel/descripcion/img"

# ---------------------------------------------------------------------------------------------------------------
# LES LIEUX. de : (genre, mot) ; es : (genre, mot, etiquette du plan) ; fr : (article, nom) ; en ; pt : (article, nom)
# Tous au corpus (themes.json, espanol/datos/temas.json), sauf « el ayuntamiento » (espanol/ajouts/ciudad.json,
# prepare, pas applique : sans lui, le mot reste « hors jeu » dans le tirage et la page marche quand meme).
LIEUX = {
    "bahnhof":     {"de": ("der", "Bahnhof"),     "es": ("la", "estación", "Estación"),        "fr": ("la", "gare"),          "en": "station",        "pt": ("a", "estação")},
    "apotheke":    {"de": ("die", "Apotheke"),    "es": ("la", "farmacia", "Farmacia"),        "fr": ("la", "pharmacie"),     "en": "pharmacy",       "pt": ("a", "farmácia")},
    "rathaus":     {"de": ("das", "Rathaus"),     "es": ("el", "ayuntamiento", "Ayuntamiento"), "fr": ("la", "mairie"),       "en": "town hall",      "pt": ("a", "prefeitura")},
    "bank":        {"de": ("die", "Bank"),        "es": ("el", "banco", "Banco"),              "fr": ("la", "banque"),        "en": "bank",           "pt": ("o", "banco")},
    "post":        {"de": ("die", "Post"),        "es": ("la", "oficina de correos", "Correos"), "fr": ("la", "poste"),       "en": "post office",    "pt": ("o", "correio")},
    "haltestelle": {"de": ("die", "Haltestelle"), "es": ("la", "parada", "Parada"),            "fr": ("l'", "arrêt de bus", "le"), "en": "bus stop",   "pt": ("o", "ponto de ônibus")},
    "krankenhaus": {"de": ("das", "Krankenhaus"), "es": ("el", "hospital", "Hospital"),        "fr": ("l'", "hôpital", "le"), "en": "hospital",       "pt": ("o", "hospital")},
    "kirche":      {"de": ("die", "Kirche"),      "es": ("la", "iglesia", "Iglesia"),          "fr": ("l'", "église", "la"),  "en": "church",         "pt": ("a", "igreja")},
    "museum":      {"de": ("das", "Museum"),      "es": ("el", "museo", "Museo"),              "fr": ("le", "musée"),         "en": "museum",         "pt": ("o", "museu")},
    "park":        {"de": ("der", "Park"),        "es": ("el", "parque", "Parque"),            "fr": ("le", "parc"),          "en": "park",           "pt": ("o", "parque")},
    "supermarkt":  {"de": ("der", "Supermarkt"),  "es": ("el", "supermercado", "Supermercado"), "fr": ("le", "supermarché"),  "en": "supermarket",    "pt": ("o", "supermercado")},
    "bibliothek":  {"de": ("die", "Bibliothek"),  "es": ("la", "biblioteca", "Biblioteca"),    "fr": ("la", "bibliothèque"),  "en": "library",        "pt": ("a", "biblioteca")},
    "kino":        {"de": ("das", "Kino"),        "es": ("el", "cine", "Cine"),                "fr": ("le", "cinéma"),        "en": "cinema",         "pt": ("o", "cinema")},
    "hotel":       {"de": ("das", "Hotel"),       "es": ("el", "hotel", "Hotel"),              "fr": ("l'", "hôtel", "le"),   "en": "hotel",          "pt": ("o", "hotel")},
    "baeckerei":   {"de": ("die", "Bäckerei"),    "es": ("la", "panadería", "Panadería"),      "fr": ("la", "boulangerie"),   "en": "bakery",         "pt": ("a", "padaria")},
    "cafe":        {"de": ("das", "Café"),        "es": ("la", "cafetería", "Cafetería"),      "fr": ("le", "café"),          "en": "café",           "pt": ("o", "café")},
    "polizei":     {"de": ("die", "Polizei"),     "es": ("la", "comisaría", "Comisaría"),      "fr": ("le", "commissariat"),  "en": "police station", "pt": ("a", "delegacia")},
    "schule":      {"de": ("die", "Schule"),      "es": ("la", "escuela", "Escuela"),          "fr": ("l'", "école", "la"),   "en": "school",         "pt": ("a", "escola")},
}
# « Gibt es hier ...? » / « ¿Hay ... por aquí? » ne se demande pas d'un lieu qu'une ville n'a qu'une fois
SANS_GIBT_ES = {"rathaus", "polizei"}

# ---------------------------------------------------------------------------------------------------------------
# LE PLAN (viewBox 360 x 480, en portrait comme le telephone). Deux longues rues nord-sud (L0, L1), trois rues
# transversales est-ouest (Q0 au sud, Q1, Q2 au nord) ; toutes continuent jusqu'au bord (on y entre et on en sort).
# Les maisons bordent les longues rues : quatre colonnes (W0 a l'ouest de L0, E0 a l'est, W1 et E1 de part et
# d'autre de L1), deux troncons par rue (0 au sud, 1 au nord), trois maisons par troncon (0 au sud, 2 au nord).
RUES = {   # id : (de, es) -- la Gartenstrasse est la rue de Mark (decision de Jacques du 3 nov. : Gartenstrasse 12)
    "L0": ("Gartenstraße", "calle Mayor"),
    "L1": ("Bergstraße", "calle del Sol"),
    "Q0": ("Lindenstraße", "calle de la Luna"),
    "Q1": ("Schulstraße", "calle de la Paz"),
    "Q2": ("Parkstraße", "calle del Prado"),
}
LX = [100, 260]               # x des longues rues
QY = [420, 250, 80]           # y des rues transversales (Q0 au sud)
DEMI = 11                     # demi-largeur d'une rue
COLONNES = {"W0": (6, 87), "E0": (113, 178), "W1": (182, 247), "E1": (273, 354)}
COTE = {"W0": ("L0", "W"), "E0": ("L0", "E"), "W1": ("L1", "W"), "E1": ("L1", "E")}
TRONCONS = {0: (263, 407), 1: (93, 237)}   # y (haut, bas) de chaque troncon, entre deux rues transversales
# les maisons, troncon par troncon, du sud au nord ; None : une maison d'habitation, sans nom
MAISONS = {
    ("W0", 1): ["museum", "kirche", "kino"],
    ("E0", 1): ["bibliothek", "cafe", "hotel"],
    ("W1", 1): ["park", "park", "park"],
    ("E1", 1): ["schule", None, "krankenhaus"],
    ("W0", 0): ["supermarkt", None, "polizei"],
    ("E0", 0): ["baeckerei", "apotheke", "bank"],
    ("W1", 0): ["post", "haltestelle", "rathaus"],
    ("E1", 0): ["bahnhof", None, None],
}
# les quatre points de depart, au bord du plan : (rue, extremite, cap)
DEPARTS = {"sud": ("L0", "s", "N"), "nord": ("L1", "n", "S"), "ouest": ("Q1", "w", "E"), "est": ("Q0", "e", "W")}


def lots():
    """Les 24 maisons : id, colonne, troncon, rang, lieu, rectangle."""
    out = []
    for (col, tr), liste in MAISONS.items():
        x0, x1 = COLONNES[col]
        haut, bas = TRONCONS[tr]
        h = (bas - haut - 6) / 3
        for rang, lieu in enumerate(liste):
            y1 = bas - rang * (h + 3)
            out.append({"id": "%s-%d-%d" % (col, tr, rang), "col": col, "tr": tr, "rang": rang, "lieu": lieu,
                        "rect": [x0, round(y1 - h, 1), x1 - x0, round(h, 1)]})
    return out


LOTS = lots()
LOT = {l["id"]: l for l in LOTS}
def lots_du(lieu): return [l for l in LOTS if l["lieu"] == lieu]
def lot_en(col, tr, rang): return LOT.get("%s-%d-%d" % (col, tr, rang))
FACE = {"W0": "E0", "E0": "W0", "W1": "E1", "E1": "W1"}

# ---------------------------------------------------------------------------------------------------------------
# LES FAITS, mesures sur le plan. Une relation porte sur une MAISON (pour savoir, dans « touche la bonne maison »,
# qu'aucune autre maison proposee ne la verifie) : neben (meme troncon, rang voisin), gegenueber (meme rang, en face,
# de l'autre cote de la longue rue), zwischen (le rang du milieu, entre deux lieux nommes), Ecke (rang 0 ou 2 : le
# coin de la longue rue et de la rue transversale), Strasse (la longue rue).
def coin(l):
    if l["rang"] == 1: return None
    q = "Q%d" % (l["tr"] + (1 if l["rang"] == 2 else 0))
    return (COTE[l["col"]][0], q)


def relations_du_lot(l):
    rel = set()
    col, tr, rang = l["col"], l["tr"], l["rang"]
    for d in (-1, 1):
        v = lot_en(col, tr, rang + d)
        if v and v["lieu"] and v["lieu"] != l["lieu"]: rel.add(("neben", v["lieu"]))
    f = lot_en(FACE[col], tr, rang)
    if f and f["lieu"] and f["lieu"] != l["lieu"]: rel.add(("gegenueber", f["lieu"]))
    a, b = lot_en(col, tr, rang - 1), lot_en(col, tr, rang + 1)
    if rang == 1 and a and b and a["lieu"] and b["lieu"] and a["lieu"] != l["lieu"] and b["lieu"] != l["lieu"] and a["lieu"] != b["lieu"]:
        rel.add(("zwischen", a["lieu"], b["lieu"]))
    c = coin(l)
    if c: rel.add(("ecke",) + c)
    rel.add(("strasse", COTE[col][0]))
    return rel


def relations_du_lieu(lieu):
    s = set()
    for l in lots_du(lieu): s |= relations_du_lot(l)
    return s


def vrai_pour_lot(rel, l):
    """La relation est-elle vraie de cette maison ? (zwischen : dans un sens ou dans l'autre)"""
    r = relations_du_lot(l)
    if rel[0] == "zwischen": return rel in r or ("zwischen", rel[2], rel[1]) in r
    return rel in r


# ---------------------------------------------------------------------------------------------------------------
# LES MOTS DES PHRASES
DAT = {"der": "dem", "die": "der", "das": "dem"}
ZU = {"der": "zum", "die": "zur", "das": "zum"}
EIN = {"der": "einen", "die": "eine", "das": "ein"}
ORD_DE = ["erste", "zweite", "dritte"]; ORD_DE_DAT = ["ersten", "zweiten", "dritten"]
ORD_ES_F = ["primera", "segunda", "tercera"]; ORD_ES_M = ["primer", "segundo", "tercer"]
ORD_FR_F = ["première", "deuxième", "troisième"]; ORD_FR_M = ["premier", "deuxième", "troisième"]
ORD_EN = ["first", "second", "third"]
ORD_PT_F = ["primeira", "segunda", "terceira"]; ORD_PT_M = ["primeiro", "segundo", "terceiro"]
CAP = lambda s: s[0].upper() + s[1:]
def rue(id, app): return RUES[id][0] if app == "de" else RUES[id][1]
def rue_de_es(id): return CAP(RUES[id][1])      # une rue de Madrid dans une phrase allemande : « die Calle Mayor »


def de_nom(lieu): g, m = LIEUX[lieu]["de"]; return g + " " + m
def de_dat(lieu): g, m = LIEUX[lieu]["de"]; return DAT[g] + " " + m
def es_nom(lieu): g, m = LIEUX[lieu]["es"][:2]; return g + " " + m
def es_de(lieu):   # de + el = del
    g, m = LIEUX[lieu]["es"][:2]; return ("del " if g == "el" else "de la ") + m
def es_a(lieu):
    g, m = LIEUX[lieu]["es"][:2]; return ("al " if g == "el" else "a la ") + m
def es_un(lieu): g, m = LIEUX[lieu]["es"][:2]; return ("un " if g == "el" else "una ") + m
def fr_nom(lieu):
    x = LIEUX[lieu]["fr"]; return x[0] + ("" if x[0].endswith("'") else " ") + x[1]
def fr_de(lieu):
    x = LIEUX[lieu]["fr"]
    return {"le": "du ", "la": "de la ", "l'": "de l'"}[x[0]] + x[1]
def fr_a(lieu):
    x = LIEUX[lieu]["fr"]
    return {"le": "au ", "la": "à la ", "l'": "à l'"}[x[0]] + x[1]
def fr_un(lieu):
    x = LIEUX[lieu]["fr"]; g = x[2] if len(x) > 2 else x[0]
    return ("un " if g == "le" else "une ") + x[1]
def en_nom(lieu): return "the " + LIEUX[lieu]["en"]
def en_un(lieu): n = LIEUX[lieu]["en"]; return ("an " if n[0] in "aeiou" else "a ") + n
def pt_nom(lieu): a, n = LIEUX[lieu]["pt"]; return a + " " + n
def pt_de(lieu): a, n = LIEUX[lieu]["pt"]; return ("do " if a == "o" else "da ") + n
def pt_a(lieu): a, n = LIEUX[lieu]["pt"]; return ("ao " if a == "o" else "à ") + n
def pt_un(lieu): a, n = LIEUX[lieu]["pt"]; return ("um " if a == "o" else "uma ") + n


# le groupe de lieu d'une relation, dans chaque langue. app : la langue apprise (les noms des rues en dependent)
def groupe(rel, app, langue):
    t = rel[0]
    nomrue = (lambda i: rue(i, app)) if langue != "de" or app == "de" else rue_de_es
    if langue == "de":
        if t == "neben": return "neben " + de_dat(rel[1])
        if t == "gegenueber": return "gegenüber " + de_dat(rel[1])
        if t == "zwischen": return "zwischen " + de_dat(rel[1]) + " und " + de_dat(rel[2])
        if t == "ecke": return "an der Ecke " + nomrue(rel[1]) + " und " + nomrue(rel[2])
        if t == "strasse": return "in der " + nomrue(rel[1])
    if langue == "es":
        if t == "neben": return "al lado " + es_de(rel[1])
        if t == "gegenueber": return "enfrente " + es_de(rel[1])
        if t == "zwischen": return "entre " + es_nom(rel[1]) + " y " + es_nom(rel[2])
        if t == "ecke": return "en la esquina de la " + nomrue(rel[1]) + " con la " + nomrue(rel[2])
        if t == "strasse": return "en la " + nomrue(rel[1])
    if langue == "fr":
        if t == "neben": return "à côté " + fr_de(rel[1])
        if t == "gegenueber": return "en face " + fr_de(rel[1])
        if t == "zwischen": return "entre " + fr_nom(rel[1]) + " et " + fr_nom(rel[2])
        if t == "ecke": return "au coin de la " + nomrue(rel[1]) + " et de la " + nomrue(rel[2])
        if t == "strasse": return "dans la " + nomrue(rel[1])
    if langue == "en":
        if t == "neben": return "next to " + en_nom(rel[1])
        if t == "gegenueber": return "opposite " + en_nom(rel[1])
        if t == "zwischen": return "between " + en_nom(rel[1]) + " and " + en_nom(rel[2])
        if t == "ecke": return "on the corner of " + nomrue(rel[1]) + " and " + nomrue(rel[2])
        if t == "strasse": return "on " + nomrue(rel[1])
    if langue == "pt":
        if t == "neben": return "ao lado " + pt_de(rel[1])
        if t == "gegenueber": return "em frente " + pt_a(rel[1])
        if t == "zwischen": return "entre " + pt_nom(rel[1]) + " e " + pt_nom(rel[2])
        if t == "ecke": return "na esquina da " + nomrue(rel[1]) + " com a " + nomrue(rel[2])
        if t == "strasse": return "na " + nomrue(rel[1])
    raise KeyError((rel, langue))


def phrase_lieu(lieu, rel, app, langue):
    """« Die Apotheke ist neben der Bank. » et ses traductions"""
    g = groupe(rel, app, langue)
    if langue == "de": return CAP(de_nom(lieu)) + " ist " + g + "."
    if langue == "es": return CAP(es_nom(lieu)) + " está " + g + "."
    if langue == "fr": return CAP(fr_nom(lieu)) + " est " + g + "."
    if langue == "en": return CAP(en_nom(lieu)) + " is " + g + "."
    if langue == "pt": return CAP(pt_nom(lieu)) + " fica " + g + "."


# ---------------------------------------------------------------------------------------------------------------
# LES ITINERAIRES. Le graphe des rues : les carrefours I(k, j) et les bouts de rue au bord du plan.
def pos(n):
    if n[0] == "I": return (LX[n[1]], QY[n[2]])
    if n[0] == "L": return (LX[n[1]], 0 if n[2] == "n" else 480)
    if n[0] == "Q": return (0 if n[2] == "w" else 360, QY[n[1]])


RANG_L = lambda k: [("L", k, "n"), ("I", k, 2), ("I", k, 1), ("I", k, 0), ("L", k, "s")]
RANG_Q = lambda j: [("Q", j, "w"), ("I", 0, j), ("I", 1, j), ("Q", j, "e")]
VOISINS = {}
for lignes in [RANG_L(0), RANG_L(1), RANG_Q(0), RANG_Q(1), RANG_Q(2)]:
    for a, b in zip(lignes, lignes[1:]):
        VOISINS.setdefault(a, []).append(b); VOISINS.setdefault(b, []).append(a)


def cap(a, b):
    (xa, ya), (xb, yb) = pos(a), pos(b)
    if xa == xb: return "N" if yb < ya else "S"
    return "E" if xb > xa else "W"


GAUCHE = {"N": "W", "W": "S", "S": "E", "E": "N"}
DROITE = {v: k for k, v in GAUCHE.items()}
OPPOSE = {"N": "S", "S": "N", "E": "W", "W": "E"}
def rue_entre(a, b):
    """La rue qui porte le segment a-b"""
    return "L%d" % a[1] if (a[0] in "IL" and b[0] in "IL" and pos(a)[0] == pos(b)[0] and a[0] != "Q") else (
        "Q%d" % (a[2] if a[0] == "I" else a[1]))


def rue_transversale(n, c):
    """Au carrefour n, la rue que croise celui qui va dans la direction c"""
    return ("Q%d" % n[2]) if c in "NS" else ("L%d" % n[1])


def itineraire(depart, lieu):
    """Le chemin le plus simple (le moins de virages, puis le plus court) jusqu'a la maison du lieu (le parc : celle du
    milieu). Rend la liste des carrefours et la maison."""
    import heapq
    l = [x for x in lots_du(lieu)]; l = l[len(l) // 2]
    k = int(COTE[l["col"]][0][1]); tr = l["tr"]
    bord = {("I", k, tr), ("I", k, tr + 1)}
    rue_, bout, c0 = DEPARTS[depart]
    n0 = ("L", int(rue_[1]), bout) if rue_[0] == "L" else ("Q", int(rue_[1]), bout)
    tas = [(0, 0, [n0], c0)]
    vus = {}
    while tas:
        virages, dist, chemin, c = heapq.heappop(tas)
        n = chemin[-1]
        if vus.get((n, c), (9, 9e9)) <= (virages, dist): continue
        vus[(n, c)] = (virages, dist)
        for m in VOISINS.get(n, []):
            d = cap(n, m)
            if d == OPPOSE[c]: continue
            v = virages + (0 if (d == c or n[0] != "I") else 1)
            if v > 2: continue
            ch = chemin + [m]
            (xa, ya), (xb, yb) = pos(n), pos(m)
            if n in bord and m in bord:
                return ch, l
            heapq.heappush(tas, (v, dist + abs(xa - xb) + abs(ya - yb), ch, d))
    raise ValueError((depart, lieu))


def etapes(depart, lieu):
    """Le chemin en ETAPES : les virages (cote, rang de la rue de ce cote, rang du carrefour), les rues traversees a
    la fin, et le cote de la maison a l'arrivee."""
    ch, l = itineraire(depart, lieu)
    caps = [cap(a, b) for a, b in zip(ch, ch[1:])]
    virages, carrefours, rues_cote, traverses = [], 0, {"links": 0, "rechts": 0}, []
    gestes = []    # a chaque carrefour : (carrefour, cap en arrivant, ce qu'on y fait) -- la serie « richtung »
    for i in range(1, len(ch) - 1):
        n, c_in, c_out = ch[i], caps[i - 1], caps[i]
        carrefours += 1
        for cote, f in (("links", GAUCHE), ("rechts", DROITE)):
            if any(cap(n, m) == f[c_in] for m in VOISINS[n]): rues_cote[cote] += 1
        if c_out == c_in:
            traverses.append(rue_transversale(n, c_in)); gestes.append((n, c_in, "geradeaus"))
        else:
            cote = "links" if c_out == GAUCHE[c_in] else "rechts"
            virages.append({"cote": cote, "rue": rues_cote[cote], "carrefour": carrefours})
            gestes.append((n, c_in, cote))
            carrefours, rues_cote, traverses = 0, {"links": 0, "rechts": 0}, []
    c_fin = caps[-1]
    cote_lot = COTE[l["col"]][1]           # W ou E
    gauche = GAUCHE[c_fin] == cote_lot
    # le dernier carrefour franchi ne compte pas : on s'arrete sur le troncon qui suit
    trav = traverses
    # le point d'arrivee sur la rue, devant la maison
    xl = LX[int(COTE[l["col"]][0][1])]
    yl = l["rect"][1] + l["rect"][3] / 2
    points = [list(pos(n)) for n in ch[:-1]] + [[xl, round(yl, 1)]]
    return {"virages": virages, "traverses": trav, "cote": "links" if gauche else "rechts", "points": points,
            "gestes": [{"pt": list(pos(n)), "cap": c, "fait": f, "i": ch.index(n)} for n, c, f in gestes], "lot": l["id"]}


# Les phrases d'un itineraire. forme « A » : die zweite Strasse links ; forme « B » : bis zur zweiten Kreuzung, links
# abbiegen. fin : « Die Apotheke ist auf der linken Seite. » ; neutre : « Es ist auf der linken Seite. »
COTES = {"de": {"links": "links", "rechts": "rechts"}, "es": {"links": "izquierda", "rechts": "derecha"},
         "fr": {"links": "gauche", "rechts": "droite"}, "en": {"links": "left", "rechts": "right"},
         "pt": {"links": "esquerda", "rechts": "direita"}}


def liste_rues(ids, app, langue):
    nom = (lambda i: rue(i, app)) if (langue != "de" or app == "de") else rue_de_es
    art = {"de": "die ", "es": "la ", "fr": "la ", "en": "", "pt": "a "}[langue]
    et = {"de": " und ", "es": " y ", "fr": " et ", "en": " and ", "pt": " e "}[langue]
    return et.join(art + nom(i) for i in ids)


def phrases_route(e, app, langue, forme, lieu=None):
    """Les phrases (une liste) : les virages, la traversee finale, la fin (lieu nomme, ou neutre si lieu est None)."""
    out = []
    S = COTES[langue]
    for i, v in enumerate(e["virages"]):
        s, r, k = S[v["cote"]], v["rue"] - 1, v["carrefour"] - 1
        premier = i == 0
        if langue == "de":
            if forme == "A":
                out.append(("Nehmen Sie die %s Straße %s." % (ORD_DE[r], s)) if premier and r == 0 else
                           ("Gehen Sie geradeaus und nehmen Sie die %s Straße %s." % (ORD_DE[r], s)) if premier else
                           ("Nehmen Sie dann die %s Straße %s." % (ORD_DE[r], s)))
            else:
                out.append(("Gehen Sie bis zur %s Kreuzung und biegen Sie dort %s ab." % (ORD_DE_DAT[k], s)) if premier else
                           ("Biegen Sie dann an der %s Kreuzung %s ab." % (ORD_DE_DAT[k], s)))
        elif langue == "es":
            if forme == "A":
                out.append(("Tome la %s calle a la %s." % (ORD_ES_F[r], s)) if premier and r == 0 else
                           ("Siga todo recto y tome la %s calle a la %s." % (ORD_ES_F[r], s)) if premier else
                           ("Luego tome la %s calle a la %s." % (ORD_ES_F[r], s)))
            else:
                out.append(("Siga hasta el %s cruce y gire a la %s." % (ORD_ES_M[k], s)) if premier else
                           ("Luego, en el %s cruce, gire a la %s." % (ORD_ES_M[k], s)))
        elif langue == "fr":
            if forme == "A":
                out.append(("Prenez la %s rue à %s." % (ORD_FR_F[r], s)) if premier and r == 0 else
                           ("Allez tout droit et prenez la %s rue à %s." % (ORD_FR_F[r], s)) if premier else
                           ("Prenez ensuite la %s rue à %s." % (ORD_FR_F[r], s)))
            else:
                out.append(("Allez jusqu'au %s carrefour et tournez à %s." % (ORD_FR_M[k], s)) if premier else
                           ("Ensuite, au %s carrefour, tournez à %s." % (ORD_FR_M[k], s)))
        elif langue == "en":
            if forme == "A":
                out.append(("Take the %s street on the %s." % (ORD_EN[r], s)) if premier and r == 0 else
                           ("Go straight ahead and take the %s street on the %s." % (ORD_EN[r], s)) if premier else
                           ("Then take the %s street on the %s." % (ORD_EN[r], s)))
            else:
                out.append(("Go to the %s intersection and turn %s." % (ORD_EN[k], s)) if premier else
                           ("Then turn %s at the %s intersection." % (s, ORD_EN[k])))
        elif langue == "pt":
            if forme == "A":
                out.append(("Pegue a %s rua à %s." % (ORD_PT_F[r], s)) if premier and r == 0 else
                           ("Siga em frente e pegue a %s rua à %s." % (ORD_PT_F[r], s)) if premier else
                           ("Depois pegue a %s rua à %s." % (ORD_PT_F[r], s)))
            else:
                out.append(("Vá até o %s cruzamento e vire à %s." % (ORD_PT_M[k], s)) if premier else
                           ("Depois, no %s cruzamento, vire à %s." % (ORD_PT_M[k], s)))
    if e["traverses"]:
        r = liste_rues(e["traverses"], app, langue)
        out.append({"de": "Gehen Sie geradeaus und überqueren Sie %s.", "es": "Siga todo recto y cruce %s.",
                    "fr": "Allez tout droit et traversez %s.", "en": "Go straight ahead and cross %s.",
                    "pt": "Siga em frente e atravesse %s."}[langue] % r)
    s = S[e["cote"]]
    if lieu is None:
        out.append({"de": "Es ist auf der %s Seite." % {"links": "linken", "rechts": "rechten"}[e["cote"]],
                    "es": "Está a la %s." % s, "fr": "C'est sur la %s." % s, "en": "It's on the %s." % s,
                    "pt": "Fica à %s." % s}[langue])
    elif lieu == "___":
        out.append({"de": "___ ist auf der %s Seite." % {"links": "linken", "rechts": "rechten"}[e["cote"]],
                    "es": "___ está a la %s." % s}[langue])
    else:
        out.append({"de": CAP(de_nom(lieu)) + " ist auf der %s Seite." % {"links": "linken", "rechts": "rechten"}[e["cote"]],
                    "es": CAP(es_nom(lieu)) + " está a la %s." % s,
                    "fr": CAP(fr_nom(lieu)) + " est sur la %s." % s,
                    "en": CAP(en_nom(lieu)) + " is on the %s." % s,
                    "pt": CAP(pt_nom(lieu)) + " fica à %s." % s}[langue])
    return out


def fausses(e):
    """Les fausses descriptions d'un chemin dessine (serie « beschreibung ») : le premier virage de l'autre cote, la
    maison de l'autre cote, une rue de plus ou de moins. Jamais l'autre forme du meme chemin (elle est juste aussi)."""
    out = []
    inv = {"links": "rechts", "rechts": "links"}
    if e["virages"]:
        f = json.loads(json.dumps(e)); f["virages"][0]["cote"] = inv[f["virages"][0]["cote"]]; out.append(f)
        f = json.loads(json.dumps(e)); v = f["virages"][0]
        if v["rue"] < 3 and v["carrefour"] < 3: v["rue"] += 1; v["carrefour"] += 1; out.append(f)
        elif v["rue"] > 1: v["rue"] -= 1; v["carrefour"] -= 1; out.append(f)
    f = json.loads(json.dumps(e)); f["cote"] = inv[f["cote"]]; out.append(f)
    return out


# ---------------------------------------------------------------------------------------------------------------
# LA DONNEE DE LA PAGE
TRADS = ["fr", "en", "pt"]


def construire():
    d = {"plan": {"rues": {}, "lots": [dict(l, rels=sorted([list(r) for r in relations_du_lot(l)])) for l in LOTS], "departs": {}, "lx": LX, "qy": QY, "demi": DEMI},
         "lieux": {}, "faits": {}, "routes": {"de": [], "es": []}, "trad": {"de": {}, "es": {}},
         "gloses": {"de": {}, "es": {}}, "photos": []}
    for k, (de, es) in RUES.items(): d["plan"]["rues"][k] = {"de": de, "es": es}
    for k, (r, b, c) in DEPARTS.items():
        n = ("L", int(r[1]), b) if r[0] == "L" else ("Q", int(r[1]), b)
        x, y = pos(n); x = min(352, max(8, x)); y = min(472, max(8, y))
        d["plan"]["departs"][k] = {"pt": [x, y], "cap": c}

    def trad(app, phrase, par_langue):
        d["trad"][app][phrase] = {l: v for l, v in par_langue.items() if l != app}

    for lieu, x in LIEUX.items():
        d["lieux"][lieu] = {"de": {"genre": x["de"][0], "mot": x["de"][1]},
                            "es": {"genre": x["es"][0], "mot": x["es"][1], "etiquette": x["es"][2]},
                            "gibt": lieu not in SANS_GIBT_ES}
        for app in ("de", "es"):
            L = ["de", "es", "fr", "en", "pt"]
            # Gibt es hier eine Apotheke ? / ¿Hay una farmacia por aquí? / ¿Dónde está la farmacia?
            if lieu not in SANS_GIBT_ES:
                q = {"de": "Entschuldigung, gibt es hier " + EIN[x["de"][0]] + " " + x["de"][1] + "?",
                     "es": "Perdone, ¿hay " + es_un(lieu) + " por aquí?",
                     "fr": "Excusez-moi, est-ce qu'il y a " + fr_un(lieu) + " près d'ici ?",
                     "en": "Excuse me, is there " + en_un(lieu) + " around here?",
                     "pt": "Com licença, tem " + pt_un(lieu) + " por aqui?"}
                trad(app, q[app], q)
            q = {"de": "Entschuldigung, wie komme ich " + ZU[x["de"][0]] + " " + x["de"][1] + "?",
                 "es": "Perdone, ¿cómo llego " + es_a(lieu) + "?",
                 "fr": "Excusez-moi, comment est-ce que je vais " + fr_a(lieu) + " ?",
                 "en": "Excuse me, how do I get to " + en_nom(lieu) + "?",
                 "pt": "Com licença, como eu chego " + pt_a(lieu) + "?"}
            trad(app, q[app], q)
            q = {"de": "Ich suche den Weg " + ZU[x["de"][0]] + " " + x["de"][1] + ".",
                 "es": "Perdone, ¿dónde está " + es_nom(lieu) + "?",
                 "fr": "Je cherche le chemin pour aller " + fr_a(lieu) + ".",
                 "en": "I'm looking for the way to " + en_nom(lieu) + ".",
                 "pt": "Estou procurando o caminho " + ("para o " if x["pt"][0] == "o" else "para a ") + x["pt"][1] + "."}
            if app == "es":
                q.update({"fr": "Excusez-moi, où est " + fr_nom(lieu) + " ?", "en": "Excuse me, where is " + en_nom(lieu) + "?",
                          "pt": "Com licença, onde fica " + pt_nom(lieu) + "?", "de": "Entschuldigung, wo ist " + de_nom(lieu) + "?"})
            trad(app, q[app], q)
            # « Das ist die Apotheke. » / « Es la farmacia. » (la photo)
            q = {"de": "Das ist " + de_nom(lieu) + ".", "es": "Es " + es_nom(lieu) + ".", "fr": "C'est " + fr_nom(lieu) + ".",
                 "en": "This is " + en_nom(lieu) + ".", "pt": "É " + pt_nom(lieu) + "."}
            trad(app, q[app], q)
        # les faits
        rels = sorted(relations_du_lieu(lieu))
        for app in ("de", "es"):
            liste = []
            for rel in rels:
                ph = {l: phrase_lieu(lieu, rel, app, l) for l in ["de", "es", "fr", "en", "pt"]}
                gr = {l: groupe(rel, app, l) for l in ["de", "es", "fr", "en", "pt"]}
                trad(app, ph[app], ph)
                d["trad"][app][gr[app]] = {l: v for l, v in gr.items() if l != app}
                liste.append({"rel": list(rel), "groupe": gr[app], "phrase": ph[app]})
            d["faits"].setdefault(app, {})[lieu] = liste
    # tous les groupes possibles (vrais pour un lieu, faux pour d'autres : les leurres), pour qu'un leurre se
    # traduise aussi (le mauvais choix traduit)
    toutes = set()
    for lieu in LIEUX: toutes |= relations_du_lieu(lieu)
    d["relations"] = sorted([list(r) for r in toutes])
    for app in ("de", "es"):
        d["groupes"] = d.get("groupes", {})
        d["groupes"][app] = {}
        for r in toutes:
            gr = {l: groupe(r, app, l) for l in ["de", "es", "fr", "en", "pt"]}
            d["groupes"][app][gr[app]] = r
            d["trad"][app][gr[app]] = {l: v for l, v in gr.items() if l != app}
    # les itineraires
    for dep in DEPARTS:
        for lieu in LIEUX:
            e = etapes(dep, lieu)
            for app in ("de", "es"):
                L = ["de", "es", "fr", "en", "pt"]
                r = {"depart": dep, "lieu": lieu, "points": e["points"], "gestes": e["gestes"], "cote": e["cote"],
                     "lot": e["lot"], "virages": e["virages"], "traverses": e["traverses"], "formes": {}}
                for forme in ("A", "B"):
                    if forme == "B" and not e["virages"]: continue
                    pars = {l: phrases_route(e, app, l, forme, lieu) for l in L}
                    neutre = {l: phrases_route(e, app, l, forme, None) for l in L}
                    trou = phrases_route(e, app, app, forme, "___")
                    for i in range(len(pars[app])):
                        trad(app, pars[app][i], {l: pars[l][i] for l in L})
                        trad(app, neutre[app][i], {l: neutre[l][i] for l in L})
                    faux = []
                    for f in fausses(e):
                        fp = {l: phrases_route(f, app, l, forme, lieu) for l in L}
                        for i in range(len(fp[app])): trad(app, fp[app][i], {l: fp[l][i] for l in L})
                        faux.append(" ".join(fp[app]))
                    r["formes"][forme] = {"phrases": pars[app], "neutre": neutre[app], "trou": trou,
                                          "faux": [x for x in faux if x != " ".join(pars[app])]}
                    for liste in (pars, neutre):
                        trad(app, " ".join(liste[app]), {l: " ".join(liste[l]) for l in L})
                    for x in faux:
                        pass
                d["routes"][app].append(r)
    # les gestes a un carrefour (serie « richtung ») : « Biegen Sie hier links ab. »
    G = {"links": {"de": "Biegen Sie hier links ab.", "es": "Aquí gire a la izquierda.", "fr": "Ici, tournez à gauche.",
                   "en": "Turn left here.", "pt": "Aqui, vire à esquerda."},
         "rechts": {"de": "Biegen Sie hier rechts ab.", "es": "Aquí gire a la derecha.", "fr": "Ici, tournez à droite.",
                    "en": "Turn right here.", "pt": "Aqui, vire à direita."},
         "geradeaus": {"de": "Gehen Sie hier geradeaus.", "es": "Aquí siga todo recto.", "fr": "Ici, allez tout droit.",
                       "en": "Go straight on here.", "pt": "Aqui, siga em frente."}}
    d["gestes"] = {}
    for app in ("de", "es"):
        d["gestes"][app] = {k: v[app] for k, v in G.items()}
        for k, v in G.items(): trad(app, v[app], v)
    # les photos qui existent deja (recadrees ou payees)
    if os.path.isdir(PROTO):
        d["photos"] = sorted(f[:-5] for f in os.listdir(PROTO) if f.endswith(".webp") and f[:-5] in LIEUX)
    d["personnes"] = sorted(f[:-5] for f in os.listdir(PROTO) if f.endswith(".webp") and f[:-5] in PERSONNES_IMG) if os.path.isdir(PROTO) else []
    gloses(d)
    return d


def gloses(d):
    """La traduction de chaque mot teste, prise au CORPUS RELU (les langues ou la phrase n'est pas traduite)."""
    LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru", "de"]
    champ = lambda w, l: w.get("traduction" if l == "fr" else "traduction_" + l)
    def pose(app, cle, w):
        if cle not in d["gloses"][app]:
            d["gloses"][app][cle] = {l: champ(w, l) for l in LANGUES if champ(w, l)}
    def parcourir(o, fn):
        if isinstance(o, dict):
            fn(o)
            for v in o.values(): parcourir(v, fn)
        elif isinstance(o, list):
            for v in o: parcourir(v, fn)
    lire = lambda *c: json.load(io.open(os.path.join(RACINE, *c), encoding="utf-8"))
    noms_de = {x["de"][1]: x["de"][0] for x in LIEUX.values()}
    noms_de.update({m: "die" for m in MOTS_DE["noms"]})
    for t in lire("themes.json")["themes"]:
        for w in t.get("mots", []):
            if noms_de.get(w.get("mot")) == w.get("genre"): pose("de", w["mot"], w)
    for w in lire("funktionswort.json")["praepositionen"]:
        if w["mot"] in MOTS_DE["praep"]: pose("de", w["mot"], w)
    parcourir(lire("adverbe.json"), lambda w: w.get("mot") in MOTS_DE["adverbes"] and "traduction" in w and pose("de", w["mot"], w))
    parcourir(lire("verbe.json"), lambda w: w.get("infinitif") in MOTS_DE["verbes"] and pose("de", w["infinitif"], w))
    noms_es = {x["es"][1]: x["es"][0] for x in LIEUX.values()}
    noms_es.update(MOTS_ES["noms"])
    for t in lire("espanol", "datos", "temas.json")["themes"]:
        for w in t.get("mots", []):
            if noms_es.get(w.get("mot")) == w.get("genre"): pose("es", w["mot"], w)
    parcourir(lire("espanol", "datos", "funcionales.json"), lambda w: w.get("mot") in MOTS_ES["praep"] and "traduction" in w and pose("es", w["mot"], w))
    parcourir(lire("espanol", "datos", "verbos.json"), lambda w: w.get("infinitif") in MOTS_ES["verbes"] and pose("es", w["infinitif"], w))
    parcourir(lire("espanol", "datos", "adverbios.json"), lambda w: w.get("mot") in MOTS_ES["adverbes"] and "traduction" in w and pose("es", w["mot"], w))
    # absents du corpus a ce jour (ajout prepare : espanol/ajouts/ciudad.json) ; « al lado de » vient des cartes de
    # prepositions (index.html, praepTheme), comme dans « Ou est le chat ? »
    MAIN = {"ayuntamiento": {"fr": "la mairie", "en": "the town hall", "pt": "a prefeitura", "ar": "البلدية", "de": "das Rathaus"},
            "todo recto": {"fr": "tout droit", "en": "straight ahead", "pt": "em frente", "ar": "على طول، مباشرة", "de": "geradeaus"},
            "al lado de": {"fr": "à côté de", "en": "next to", "pt": "ao lado de", "ar": "بجانب", "de": "neben"}}
    for k, v in MAIN.items(): d["gloses"]["es"].setdefault(k, v)
    manque = [m for m in list(noms_de) + MOTS_DE["praep"] + MOTS_DE["adverbes"] + MOTS_DE["verbes"] if m not in d["gloses"]["de"]]
    manque += [m for m in list(noms_es) + MOTS_ES["praep"] + MOTS_ES["adverbes"] + MOTS_ES["verbes"] if m not in d["gloses"]["es"]]
    if manque: raise SystemExit("gloses absentes du corpus : %s" % manque)


# LES MOTS DU THEME qui ne sont pas des lieux (la page les lit dans ciudad.json : « mots »)
MOTS_DE = {"noms": ["Straße", "Ecke", "Kreuzung"], "praep": ["neben", "gegenüber", "zwischen", "an", "zu"],
           "adverbes": ["geradeaus", "links", "rechts"], "verbes": ["gehen", "nehmen", "abbiegen", "überqueren"]}
MOTS_ES = {"noms": {"calle": "la", "esquina": "la", "cruce": "el", "derecha": "la", "izquierda": "la"},
           "praep": ["al lado de", "enfrente de", "entre"], "adverbes": ["todo recto"],
           "verbes": ["tomar", "girar", "doblar", "cruzar", "seguir", "llegar", "estar"]}


def ecrire_json():
    d = construire()
    d["mots"] = {"de": MOTS_DE, "es": MOTS_ES}
    os.makedirs(PROTO, exist_ok=True)
    io.open(os.path.join(PROTO, "ciudad.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "\n")
    n = sum(len(v) for v in d["trad"]["de"].values())
    print("  ciudad.json : %d lieux, %d routes de, %d phrases de traduites, %d es, photos : %s" % (
        len(d["lieux"]), len(d["routes"]["de"]), len(d["trad"]["de"]), len(d["trad"]["es"]), ", ".join(d["photos"]) or "aucune"))


# ---------------------------------------------------------------------------------------------------------------
# LES PHOTOS. Gratuites : recadrees dans les scenes de l'app (le meme Berlin, la meme rue que Kreuzung) ; les
# autres, a payer, dans le meme style que la scene Kreuzung (facades claires du vieux Berlin, rien d'ecrit nulle part :
# un lieu se reconnait a ce qu'il montre, jamais a son enseigne -- une enseigne donnerait la reponse en allemand).
RECADRAGES = {   # lieu : (scene, (x0, y0, x1, y1) en fraction de l'image)
    "baeckerei":   ("kreuzung", (0.0, 0.165, 0.31, 0.295)),
    "apotheke":    ("kreuzung", (0.29, 0.145, 0.53, 0.28)),
    "post":        ("kreuzung", (0.42, 0.15, 0.64, 0.275)),
    "cafe":        ("kreuzung", (0.60, 0.13, 0.95, 0.285)),
    "haltestelle": ("kreuzung", (0.0, 0.33, 0.32, 0.505)),
    "kirche":      ("stadtplatz", (0.0, 0.145, 0.60, 0.395)),
}
RUE_BERLIN = ("A photorealistic photograph, taken with a good phone camera from the opposite pavement, of the ground floor "
              "and first floor of an old cream or pale-ochre Berlin building on an ordinary street of the same district as "
              "the first picture (only its streets and buildings: no person of it), on a bright, slightly overcast late morning, in a 4:3 landscape picture. Natural "
              "colours, soft daylight, wet-looking cobbled pavement in front. Nothing in the picture carries any writing, "
              "letters, numbers or logos: no sign, no name, no poster, no number plate; every sign is a plain shape or a "
              "pictogram. ")
FACADES = {   # lieu : ce qui le fait reconnaitre SANS rien d'ecrit
    "bahnhof": "The building is a large old red-brick railway station hall with tall arched windows and a big round station "
               "clock with plain hands and no numbers above the wide entrance; through the open entrance, platforms and a "
               "red regional train are visible; travellers with suitcases walk in.",
    "rathaus": "The building is a grand old town hall of red and sandstone with a clock tower, a wide stone staircase up to "
               "a heavy double wooden door, and three flags on poles above the entrance: plain flags in black, red and gold "
               "stripes, without any emblem.",
    "bank": "The building is a modern bank branch on the ground floor of the old building: a glass front with an ATM built "
            "into the wall beside the door, a person withdrawing cash at the ATM, and through the glass a counter and a "
            "small round sign showing only a plain euro symbol €.",
    "krankenhaus": "The building is a modern hospital with a wide glass entrance and an ambulance (white with red stripes, no "
                   "lettering) parked in front; above the entrance, a plain white square sign with a red cross.",
    "museum": "The building is a classical museum with tall stone columns, broad stone steps, and a banner showing only a "
              "painting of a portrait, no letters; a few visitors walk up the steps.",
    "bibliothek": "The building is a public library: through big windows, tall shelves full of books and people reading at "
                  "long tables; a returns slot beside the door; a bicycle against the wall.",
    "kino": "The building is an old cinema with a curved canopy over the entrance lined with warm light bulbs, glass doors, "
            "and framed film posters showing only pictures of actors, without any letters; a couple holding popcorn.",
    "supermarkt": "The building is a supermarket: wide automatic glass doors, a row of shopping trolleys in front, crates of "
                  "fruit and vegetables on display outside, and a person coming out with a full shopping bag.",
    "hotel": "The building is a small hotel: a revolving glass door under a dark-blue canopy, a doorman in a dark uniform, "
             "a traveller arriving with a suitcase, and a plain dark-blue flag without any emblem.",
    "park": "Instead of a building: the entrance of a city park, a wrought-iron gate open onto a gravel path between tall "
            "green trees, benches, a lawn and a few people walking a dog.",
    "polizei": "The building is a police station: a grey stone building with a blue lamp above the door and two police cars "
               "in blue and silver, with plain bodywork and no lettering, parked in front.",
    "schule": "The building is a primary school: a big old red-brick school building with tall windows full of children's "
              "drawings, a schoolyard behind a low fence and children with school bags going in.",
}
# Mark demande son chemin (la decouverte, l'onglet « Demander son chemin ») : il est la, dans la Gartenstrasse
PERSONNES_IMG = {
    "mark-demande": "Mark, the young man of the second picture (the same face, hair, build and clothes), stands on the pavement "
                    "of the same old Berlin street, holding his phone in one hand, and politely asks a woman of about sixty "
                    "with grey hair and a shopping bag for the way; he looks at her, friendly and a little lost.",
    "mark-gauche": "Mark, the young man of the second picture (the same face, hair, build and clothes), on the same Berlin pavement, listens to the woman of about "
                   "sixty with grey hair and a shopping bag, who stretches out her arm and points along the street to HER "
                   "left, seen from the front; Mark looks in that direction and nods.",
}
PLANCHE = ["bahnhof", "rathaus", "bank", "krankenhaus", "kino", "mark-demande"]   # l'essai : 6 images, 0,90 $


def prompt_de(id):
    if id in FACADES: return RUE_BERLIN + FACADES[id]
    if id in PERSONNES_IMG:
        return ("A photorealistic photograph, taken with a good phone camera, of a street scene in an old Berlin district "
                "like the street of the first picture, bright overcast late morning, 4:3 landscape. " + PERSONNES_IMG[id] +
                " Nothing carries any writing, letters, numbers or logos.")
    raise KeyError(id)


def references(id):
    """Pour le lieu : la scene Kreuzung (la meme rue de Berlin) ; pour Mark : sa photo detouree."""
    refs = [os.path.join(RACINE, "visuel", "prototype", "kreuzung.webp")]
    if id in PERSONNES_IMG: refs.append(os.path.join(PERSONNES, "Mark-detoure.png"))
    return refs


A_PAYER = list(FACADES) + list(PERSONNES_IMG)


def recadrer():
    from PIL import Image
    os.makedirs(PROTO, exist_ok=True)
    for lieu, (scene, (a, b, c, e)) in RECADRAGES.items():
        im = Image.open(os.path.join(RACINE, "visuel", "prototype", scene + ".webp")).convert("RGB")
        W, H = im.size
        x0, y0, x1, y1 = a * W, b * H, c * W, e * H
        # 4:3 exactement, centre sur le cadre demande
        w, h = x1 - x0, y1 - y0
        if w / h > 4 / 3: nw, nh = h * 4 / 3, h
        else: nw, nh = w, w * 3 / 4
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        box = (round(max(0, cx - nw / 2)), round(max(0, cy - nh / 2)), round(min(W, cx + nw / 2)), round(min(H, cy + nh / 2)))
        r = im.crop(box)
        r = r.resize((800, 600), Image.LANCZOS)
        r.save(os.path.join(PROTO, lieu + ".webp"), quality=80, method=6)
        print("  %-12s <- %s %s" % (lieu, scene, box))


def payer(ids):
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    os.makedirs(IMG, exist_ok=True)
    a_faire = [i for i in (ids or PLANCHE) if not os.path.exists(os.path.join(IMG, i + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    cle = O.cle()
    for id in a_faire:
        prompt, refs = prompt_de(id), references(id)
        manque = [r for r in refs if not os.path.exists(r)]
        if manque:
            print("  %s : reference absente %s -- sautee" % (id, manque)); continue
        corps = {"prompt": prompt, "aspect_ratio": "4:3", "resolution": "2K", "output_format": "png", "num_images": 1,
                 "image_urls": [O.deposer(r, "image/webp" if r.endswith(".webp") else "image/png", cle)[0] for r in refs]}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle)
        sortie = os.path.join(IMG, id + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(IMG, id + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": EDIT, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "references": [os.path.basename(r) for r in refs], "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", os.path.relpath(sortie, RACINE), "(%.2f $)" % PRIX)


def webp():
    from PIL import Image
    os.makedirs(PROTO, exist_ok=True)
    for id in A_PAYER:
        src = os.path.join(IMG, id + ".png")
        if not os.path.exists(src): continue
        im = Image.open(src).convert("RGB").resize((1000, 750), Image.LANCZOS)
        im.save(os.path.join(PROTO, id + ".webp"), quality=78, method=6)
        print("  ", id)


def main():
    a = sys.argv[1:]
    if "--montrer" in a:
        for id in A_PAYER:
            print("\n  %s%s  (%s)\n  %s" % (id, "  [PLANCHE]" if id in PLANCHE else "", ", ".join(os.path.basename(r) for r in references(id)), prompt_de(id)))
        print("\n  planche d'essai : %d images, %.2f $ ; tout : %d images, %.2f $" % (len(PLANCHE), len(PLANCHE) * PRIX, len(A_PAYER), len(A_PAYER) * PRIX))
        return
    if "--recadrer" in a: recadrer()
    if "--payer" in a: payer([x for x in a if not x.startswith("--")])
    if "--webp" in a: webp()
    ecrire_json()


if __name__ == "__main__":
    main()
