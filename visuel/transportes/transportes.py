# -*- coding: utf-8 -*-
"""« Les transports » -- le theme illustre des DEPLACEMENTS, en espagnol et en allemand (3 nov. 2026, vague 2).
LA SEULE SOURCE du theme : les moyens de transport, les images, le tableau des departs, le plan du metro, les
billets, toutes les phrases, leurs traductions, les lectures en lettres des nombres et les prompts des images.

    python visuel/transportes/transportes.py --json          # visuel/prototype/transportes/transportes.json, gratuit
    python visuel/transportes/transportes.py --provisoires   # des images DESSINEES, gratuites, pour essayer la page
    python visuel/transportes/transportes.py --montrer       # les prompts seuls, gratuit
    python visuel/transportes/transportes.py --payer [ids]   # les images fal qui manquent, 0,15 $ chacune -- ACCORD DE JACQUES
    python visuel/transportes/transportes.py --webp          # les originaux -> webp

L'ANGLE (regle 2 des themes : pas de theme qui refait une scene). Les scenes U-Bahn, Zug, Kreuzung et Flughafen
font nommer leurs OBJETS (der Bahnsteig, die Ampel, die Gepaeckablage) et le « Wo? » de ces objets. Ici, ce sont
des PERSONNES qui se deplacent, et les gestes du voyage :
  - COMMENT ON Y VA : « mit dem Bus » (mit + DATIF, le point cle : der Bus -> mit dem Bus, die U-Bahn -> mit der
    U-Bahn), « zu Fuss » ; en espagnol « en autobus » SANS article, mais « a pie » ;
  - MONTER, DESCENDRE, CHANGER : einsteigen in + accusatif (in den Bus), aussteigen aus + datif (aus dem Bus), le
    verbe separable (Mark steigt ... ein) ; umsteigen sur un plan de metro ; subir al / bajar del (al, del) et
    « cambiar de linea » ;
  - L'HEURE DU DEPART : un tableau des departs (Wann? Von welchem Gleis? Verspaetung), l'heure dite en mots (halb
    neun = 8 h 30, le piege des francophones ; las nueve menos cuarto) ;
  - ACHETER UN BILLET : einfach oder hin und zurueck ? de ida o de ida y vuelta ? et le prix en toutes lettres
    (neunundzwanzig : l'unite avant la dizaine).
Le tableau, le plan et les billets sont DESSINES par la page depuis ces donnees (lisibles a 375 px, aucun texte a
faire ecrire par un modele d'image). Les photos : des personnes de l'histoire (Mark, de Montreal ; Anna et sa soeur
Lena, son cousin Felix, de la famille d'Anna) dans les transports de Berlin, retouches de leurs images de reference.
Originaux : visuel/transportes/img/ (hors depot) ; webp : visuel/prototype/transportes/.
"""
import io, json, os, random, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype", "transportes")
IMG = os.path.join(ICI, "img")
# les images de reference des personnes (hors depot, dossier de la session des themes)
REF = {"Mark": "C:/Users/jacqu/.wortando/wt-themes/visuel/descripcion/img/Mark-detoure.png",
       "Anna": "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img/Anna-quotidien.png",
       "Lena": "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img/Lena.png",
       "Felix": "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img/Felix.png"}
MODELE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15
PLAFOND = 2.50              # le plafond du theme (le solde fal est partage entre cinq themes et le DTZ)

# ---------------------------------------------------------------------------------------------------------------
# LES PERSONNES : le pronom dans chaque langue
PERS = {"Mark": "m", "Anna": "f", "Lena": "f", "Felix": "m"}
PRON = {"de": {"m": "er", "f": "sie"}, "fr": {"m": "il", "f": "elle"}, "en": {"m": "he", "f": "she"}, "pt": {"m": "ele", "f": "ela"}}

# LES MOYENS DE TRANSPORT : (genre, mot) allemand, (genre, mot) espagnol, et « en bus » en francais, anglais, portugais
MOYENS = {
    "bus":      (("der", "Bus"),         ("el", "autobús"),   "en bus",     "by bus",    "de ônibus"),
    "ubahn":    (("die", "U-Bahn"),      ("el", "metro"),     "en métro",   "by subway", "de metrô"),
    "tram":     (("die", "Straßenbahn"), ("el", "tranvía"),   "en tram",    "by tram",   "de bonde"),
    "zug":      (("der", "Zug"),         ("el", "tren"),      "en train",   "by train",  "de trem"),
    "auto":     (("das", "Auto"),        ("el", "coche"),     "en voiture", "by car",    "de carro"),
    "taxi":     (("das", "Taxi"),        ("el", "taxi"),      "en taxi",    "by taxi",   "de táxi"),
    "fahrrad":  (("das", "Fahrrad"),     ("la", "bicicleta"), "à vélo",     "by bike",   "de bicicleta"),
    "flugzeug": (("das", "Flugzeug"),    ("el", "avión"),     "en avion",   "by plane",  "de avião"),
    "fuss":     (("der", "Fuß"),         ("el", "pie"),       "à pied",     "on foot",   "a pé"),
}
DAT = {"der": "dem", "die": "der", "das": "dem"}
AKK = {"der": "den", "die": "die", "das": "das"}


def mit_de(m):
    """« mit dem Bus », « zu Fuß »"""
    if m == "fuss": return "zu Fuß"
    g, mot = MOYENS[m][0]
    return "mit " + DAT[g] + " " + mot


def en_es(m):
    """« en autobús », « a pie » (sans article)"""
    return "a pie" if m == "fuss" else "en " + MOYENS[m][1][1]


def verbe_de(m):
    return {"fuss": "gehen", "flugzeug": "fliegen"}.get(m, "fahren")


CONJ_DE = {"fahren": {"ich": "fahre", "du": "fährst", "er": "fährt", "ihr": "fahrt"}, "gehen": {"ich": "gehe", "du": "gehst", "er": "geht"},
           "fliegen": {"ich": "fliege", "du": "fliegst", "er": "fliegt"}}
CONJ_ES = {"yo": "voy", "tu": "vas", "el": "va"}

# OU L'ON VA : (allemand, espagnol, francais, anglais, portugais). L'avion a ses villes.
DEST = [("zur Arbeit", "al trabajo", "au travail", "to work", "para o trabalho"),
        ("zum Bahnhof", "a la estación", "à la gare", "to the station", "para a estação"),
        ("in die Stadt", "al centro", "en ville", "into town", "para o centro"),
        ("nach Hause", "a casa", "à la maison", "home", "para casa"),
        ("zum Supermarkt", "al supermercado", "au supermarché", "to the supermarket", "para o supermercado")]
DEST_AVION = {"de": [("nach München", "à Munich", "to Munich", "para Munique"), ("nach Wien", "à Vienne", "to Vienna", "para Viena"),
                     ("nach Paris", "à Paris", "to Paris", "para Paris")],
              "es": [("a Barcelona", "à Barcelone", "to Barcelona", "para Barcelona", "nach Barcelona"), ("a Roma", "à Rome", "to Rome", "para Roma", "nach Rom"),
                     ("a París", "à Paris", "to Paris", "para Paris", "nach Paris")]}

# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES : qui, quel moyen, quel geste (ein : il monte, aus : il descend), le LIEU et le prompt.
# LA CONTINUITE DES LIEUX (decision de Jacques du 3 nov. : « Que ça soit consistant lorsqu'on va faire des vidéos »,
# video/LIEUX.md) : une photo prise dans un lieu que les scenes montrent deja reprend CE lieu, son image donnee en
# reference « pour le lieu » -- l'arret de bus, le tram, le taxi et la piste cyclable de la scene Kreuzung (le bus y est
# BLANC, le tram JAUNE, le taxi CREME, la piste ROUGE) ; le quai et la rame jaune de la scene U-Bahn (carrelage vert pale,
# sol de granit gris). Les lieux neufs (le quai de la grande gare, la rue de Felix, l'avion) sont decrits dans
# video/LIEUX.md. La personne vient de son image de reference (Mark : le meme que dans la scene U-Bahn).
LIEUX = {"kreuzung": os.path.join(RACINE, "visuel", "prototype", "kreuzung.webp"),
         "ubahn": os.path.join(RACINE, "visuel", "prototype", "ubahn.webp")}
STYLE = ("A natural, photorealistic photograph, eye level, 4:3, the light of an overcast autumn day in Berlin. NO logos, "
         "NO readable text, NO brand names anywhere. The person looks exactly like in the PERSON reference picture: same "
         "face, hair, body and clothes. One person in focus; other people, if any, are few and blurred in the background. ")
LIEU_TXT = {"kreuzung": "The PLACE is the street corner of the PLACE reference picture, now seen at eye level from the sidewalk: the same "
                        "cream and beige old buildings, the same wet grey cobblestones, the same glass bus shelter with its yellow round "
                        "stop sign, the same tram rails, the same red bike lane. ",
            "ubahn": "The PLACE is the underground station of the PLACE reference picture: the same pale green tiled wall, the same grey "
                     "granite floor with its dark tactile strip, the same yellow train, the same hanging clock. "}
IMAGES = {
    # --- gratuite : recadree dans la scene U-Bahn (Mark monte dans la rame), 4:3 ---
    "ubahn-ein": {"qui": "Mark", "moyen": "ubahn", "geste": "ein", "recadrage": ("ubahn", (160, 800, 1536, 1832))},
    # --- la planche d'essai (6) ---
    "bus-ein":  {"qui": "Mark", "moyen": "bus", "geste": "ein", "essai": True, "lieu": "kreuzung",
                 "prompt": "Mark is GETTING ON the WHITE city bus of the place at its bus stop: one foot on the step of the open front "
                           "door, his hand on the door rail, his body turned towards the inside of the bus. Seen from the sidewalk, slightly from the side."},
    "ubahn":    {"qui": "Anna", "moyen": "ubahn", "essai": True, "lieu": "ubahn",
                 "prompt": "Anna is SITTING INSIDE the yellow underground train of the place, by the window, the dark tunnel outside; "
                           "rows of seats and yellow grab poles around her. She looks relaxed, a bag on her lap."},
    "fahrrad":  {"qui": "Mark", "moyen": "fahrrad", "essai": True, "lieu": "kreuzung",
                 "prompt": "Mark is RIDING a city bicycle on the RED bike lane of the place, wearing a helmet, both hands on the "
                           "handlebars, seen from the side, clearly moving."},
    "fuss":     {"qui": "Anna", "moyen": "fuss", "essai": True, "lieu": "kreuzung",
                 "prompt": "Anna is WALKING on the cobblestone sidewalk of the place, mid-stride, seen from the side, a bag on her "
                           "shoulder. No vehicle near her: she clearly goes on foot."},
    "zug-aus":  {"qui": "Anna", "moyen": "zug", "geste": "aus", "essai": True,
                 "prompt": "In a large Berlin main station with a glass roof (the platform of a long-distance train, a NEW place: grey "
                           "concrete platform, white line along the edge, steel pillars), Anna is GETTING OFF a white long-distance train "
                           "with a red stripe (the train of the scene Zug: through its windows, the same dark blue seats and light grey interior): she steps down from the open train door with a small dark-red suitcase, one foot already on "
                           "the platform, her body facing away from the train."},
    "automat":  {"qui": "Mark", "action": "kaufen", "essai": True, "lieu": "ubahn",
                 "prompt": "Mark is BUYING a ticket at a ticket machine standing against the green tiled wall of the platform of the "
                           "place: he touches the machine's screen with one finger, a bank card in his other hand. The screen shows only "
                           "blurred colored buttons, no readable text."},
    # --- la suite (6), apres la planche ---
    "bus-aus":  {"qui": "Mark", "moyen": "bus", "geste": "aus", "base": "bus-ein",
                 "prompt": "The same bus, the same bus stop, the same Mark: now he is GETTING OFF the bus. He steps down from the "
                           "open door onto the sidewalk, facing AWAY from the bus, the bus behind him."},
    "zug-ein":  {"qui": "Anna", "moyen": "zug", "geste": "ein", "base": "zug-aus",
                 "prompt": "The same train, the same platform, the same Anna and suitcase: now she is GETTING ON the train. "
                           "She lifts her suitcase and steps up into the open train door, facing the train, her back half to the camera."},
    "tram-ein": {"qui": "Lena", "moyen": "tram", "geste": "ein", "lieu": "kreuzung",
                 "prompt": "Lena is GETTING ON the YELLOW tram of the place at the tram stop: one foot on the step of the open tram door, "
                           "facing the tram, the tram rails in the street."},
    "taxi-aus": {"qui": "Mark", "moyen": "taxi", "geste": "aus", "lieu": "kreuzung",
                 "prompt": "Mark is GETTING OUT of the CREAM-colored taxi of the place, parked along the sidewalk: the rear door is "
                           "open, one foot on the sidewalk, he is standing up out of the car. The taxi roof sign has no text."},
    "auto":     {"qui": "Felix", "moyen": "auto",
                 "prompt": "In a quiet residential Berlin street with trees (a NEW place), Felix is DRIVING a small grey car, seen "
                           "through the open driver's window from the side: both hands on the steering wheel, seat belt on, looking ahead."},
    "flugzeug": {"qui": "Felix", "moyen": "flugzeug",
                 "prompt": "Felix is sitting by the window inside a passenger airplane in flight (a NEW place): the airplane wing and "
                           "clouds are visible through the oval window, seat belt on, a small table folded in front of him.",
                 # la prise payee met sa chaussure au premier plan, contre la paroi : on recadre (gratuit) au-dessus
                 "cadre": (291, 34, 2121, 1406)},
}
ORDRE = list(IMAGES)
PAYANTES = [i for i in ORDRE if not IMAGES[i].get("recadrage")]

# ---------------------------------------------------------------------------------------------------------------
# LES NOMBRES EN LETTRES (la voix ; et la sorte « prix », qui fait choisir le prix ecrit en mots)
UN_DE = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf", "dreizehn",
         "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]
DIX_DE = {2: "zwanzig", 3: "dreißig", 4: "vierzig", 5: "fünfzig", 6: "sechzig", 7: "siebzig", 8: "achtzig", 9: "neunzig"}
UN_ES = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce",
         "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro",
         "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
DIX_ES = {3: "treinta", 4: "cuarenta", 5: "cincuenta", 6: "sesenta", 7: "setenta", 8: "ochenta", 9: "noventa"}


def nombre_de(n):
    if n < 20: return UN_DE[n]
    d, u = divmod(n, 10)
    return DIX_DE[d] if not u else ("ein" if u == 1 else UN_DE[u]) + "und" + DIX_DE[d]


def nombre_es(n):
    if n < 30: return UN_ES[n]
    d, u = divmod(n, 10)
    return DIX_ES[d] + ("" if not u else " y " + UN_ES[u])


def heure_ecrite(h, m):
    return "%d:%02d" % (h, m)


def heure_dite_de(h, m):
    """« acht Uhr fünfzehn » (la lecture de « 8:15 Uhr »)"""
    return nombre_de(h) .replace("eins", "ein") + " Uhr" + ("" if not m else " " + nombre_de(m))


def heure_dite_es(h, m):
    """« las ocho y cuarto », « las dieciséis cuarenta » (la lecture de « las 8:15 »)"""
    hh = nombre_es(h)
    if m == 0: return hh + " en punto"
    if h <= 12 and m == 15: return hh + " y cuarto"
    if h <= 12 and m == 30: return hh + " y media"
    return hh + " " + nombre_es(m)


def douze(h):
    return h % 12 or 12


# l'heure DITE comme on la dit (la sorte « uhrzeit » / « hora ») : 8:15 -> Viertel nach acht, las ocho y cuarto
def heure_mots_de(h, m):
    a, b = douze(h), douze(h + 1)
    w = lambda x: "eins" if x == 1 else nombre_de(x)
    return {15: "Viertel nach " + w(a), 30: "halb " + w(b), 45: "Viertel vor " + w(b)}[m]


def heure_mots_es(h, m):
    a, b = douze(h), douze(h + 1)
    return {15: "las %s y cuarto" % nombre_es(a), 30: "las %s y media" % nombre_es(a), 45: "las %s menos cuarto" % nombre_es(b)}[m]


def heure_mots_fr(h, m):
    a, b = douze(h), douze(h + 1)
    fr = ["", "une", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze"]
    hr = lambda x: fr[x] + (" heure" if x == 1 else " heures")
    return {15: hr(a) + " et quart", 30: hr(a) + " et demie", 45: hr(b) + " moins le quart"}[m]


def heure_mots_en(h, m):
    a, b = douze(h), douze(h + 1)
    en = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
    return {15: "a quarter past " + en[a], 30: "half past " + en[a], 45: "a quarter to " + en[b]}[m]


def heure_mots_pt(h, m):
    a, b = douze(h), douze(h + 1)
    pt = ["", "uma", "duas", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze"]
    return {15: pt[a] + " e quinze", 30: pt[a] + " e meia", 45: "quinze para as " + pt[b]}[m]


# les LEURRES de l'heure en mots : toujours FAUX pour cette heure (jamais « drei Viertel neun », regional mais juste)
def leurres_heure(h, m, app):
    f = heure_mots_de if app == "de" else heure_mots_es
    if m == 15: c = [(h - 1, 45), (h + 1, 15), (h, 30)]          # Viertel vor acht (7:45), Viertel nach neun, halb neun
    elif m == 30: c = [(h - 1, 30), (h, 15), (h + 1, 30)]        # halb acht (7:30) : LE piege ; Viertel nach acht
    else: c = [(h - 1, 45), (h + 1, 15), (h, 15)]                # Viertel vor acht (7:45), Viertel nach neun
    return [f(a, b) for a, b in c]


def prix_ecrit_de(e, c):
    return "%d,%02d €" % (e, c)


def prix_mots_de(e, c):
    return nombre_de(e) + " Euro" + ("" if not c else " " + nombre_de(c))


def prix_mots_es(e, c):
    """« veintiún euros », « sesenta y un euros » : uno devient un devant le nom (masculin)"""
    eu = nombre_es(e)
    eu = eu[:-3] + "ún" if eu == "veintiuno" else (eu[:-1] if eu.endswith("uno") else eu)
    return eu + " euros" + ("" if not c else " con " + nombre_es(c))


def leurres_prix(e, c, app):
    """des prix FAUX qui ressemblent : l'unite et la dizaine inversees (29 / 92, le piege de l'allemand), la dizaine
    et le « -zehn » (19 / 90, dieciséis / sesenta), dix euros de plus, les centimes changes"""
    f = prix_mots_de if app == "de" else prix_mots_es
    c_ = []
    d, u = divmod(e, 10)
    if d and u and d != u: c_.append((u * 10 + d, c))
    if 13 <= e <= 19: c_.append(((e - 10) * 10, c))
    if e % 10 == 0 and 30 <= e <= 90: c_.append((10 + e // 10, c))
    if app == "es" and e // 10 in (6, 7): c_.append((e + (10 if e // 10 == 6 else -10), c))     # sesenta / setenta
    c_ += [(e + 10, c), (e, (c + 10) % 100 if c else 50)]
    vus, out = set(), []
    for a, b in c_:
        if (a, b) != (e, c) and 2 <= a <= 99 and (a, b) not in vus:
            vus.add((a, b)); out.append(f(a, b))
    return out[:3]


# ---------------------------------------------------------------------------------------------------------------
# LE TABLEAU DES DEPARTS : des trains, l'heure, la destination, la voie (le quai), le retard. Fixe (tire une fois, graine
# fixe) : les phrases et leurs traductions se fabriquent ici, la page ne fait que choisir.
VILLES = {"de": [("Hamburg", "Hambourg", "Hamburg", "Hamburgo"), ("München", "Munich", "Munich", "Munique"), ("Köln", "Cologne", "Cologne", "Colônia"),
                 ("Leipzig", "Leipzig", "Leipzig", "Leipzig"), ("Dresden", "Dresde", "Dresden", "Dresden"), ("Frankfurt", "Francfort", "Frankfurt", "Frankfurt"),
                 ("Hannover", "Hanovre", "Hanover", "Hanôver"), ("Stuttgart", "Stuttgart", "Stuttgart", "Stuttgart"), ("Rostock", "Rostock", "Rostock", "Rostock"),
                 ("Nürnberg", "Nuremberg", "Nuremberg", "Nuremberg"), ("Bremen", "Brême", "Bremen", "Bremen"), ("Düsseldorf", "Düsseldorf", "Düsseldorf", "Düsseldorf")],
          "es": [("Sevilla", "Séville", "Seville", "Sevilha", "Sevilla"), ("Valencia", "Valence", "Valencia", "Valência", "Valencia"),
                 ("Barcelona", "Barcelone", "Barcelona", "Barcelona", "Barcelona"), ("Bilbao", "Bilbao", "Bilbao", "Bilbao", "Bilbao"),
                 ("Málaga", "Malaga", "Malaga", "Málaga", "Málaga"), ("Zaragoza", "Saragosse", "Zaragoza", "Saragoça", "Saragossa"),
                 ("Granada", "Grenade", "Granada", "Granada", "Granada"), ("Salamanca", "Salamanque", "Salamanca", "Salamanca", "Salamanca"),
                 ("Toledo", "Tolède", "Toledo", "Toledo", "Toledo"), ("Córdoba", "Cordoue", "Cordoba", "Córdoba", "Córdoba"),
                 ("Alicante", "Alicante", "Alicante", "Alicante", "Alicante"), ("Valladolid", "Valladolid", "Valladolid", "Valladolid", "Valladolid")]}
HEURES_PERMISES = [6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21]      # ni 12 ni 13 : « halb eins », « la una »


def tableaux(app):
    r = random.Random("tableaux-" + app)
    villes = list(range(len(VILLES[app])))
    out = []
    for t in range(4):                                   # quatre tableaux de cinq trains
        r.shuffle(villes)
        h0 = r.choice([6, 9, 15, 18])
        lignes, vues = [], set()
        h, m = h0, r.choice([0, 15, 30])
        for k in range(5):
            m += r.choice([15, 15, 15, 20, 30])
            while m >= 60: h += 1; m -= 60
            while h not in HEURES_PERMISES: h += 1
            v = villes[k]
            gl = r.randint(1, 14)
            while gl in vues: gl = r.randint(1, 14)
            vues.add(gl)
            retard = r.choice([0, 0, 0, 5, 10, 15, 20])
            lignes.append({"h": h, "m": m, "ville": v, "voie": gl, "retard": retard})
        # au moins une heure en quart et une demie par tableau (la sorte « uhrzeit » / « hora »)
        if not any(l["m"] in (15, 30, 45) for l in lignes):
            lignes[1]["m"] = 30
        out.append(lignes)
    return out


# ---------------------------------------------------------------------------------------------------------------
# LE PLAN DU METRO : trois lignes qui se croisent deux a deux une seule fois ; un trajet d'une station d'une ligne a
# une station d'une autre (jamais une station de correspondance) ne change qu'a un endroit. Les noms sont inventes
# (aucun vrai plan de Berlin ni de Madrid ne doit sembler faux a qui y vit).
# station : (nom allemand, genre allemand, nom espagnol), x, y dans un plan de 100 x 100
STATIONS = {
    "zoo":      (("Zoo", "der", "Zoológico"), 8, 46),
    "goethe":   (("Goetheplatz", "der", "Cervantes"), 28, 46),
    "markt":    (("Marktplatz", "der", "Plaza Mayor"), 48, 46),
    "rathaus":  (("Rathaus", "das", "Ayuntamiento"), 68, 46),
    "ost":      (("Ostbahnhof", "der", "Estación Este"), 92, 46),
    "uni":      (("Universität", "die", "Universidad"), 48, 6),
    "linden":   (("Lindenallee", "die", "Alameda"), 48, 26),
    "schiller": (("Schillerstraße", "die", "Calle Real"), 48, 66),
    "stadion":  (("Stadion", "das", "Estadio"), 48, 92),
    "flughafen": (("Flughafen", "der", "Aeropuerto"), 88, 26),
    "museum":   (("Museum", "das", "Museo"), 28, 86),
    "hafen":    (("Hafen", "der", "Puerto"), 12, 100),
}
# la ligne : (nom allemand, nom espagnol, couleur, stations dans l'ordre)
LIGNES = {"1": ("U1", "línea 1", "#D6453A", ["zoo", "goethe", "markt", "rathaus", "ost"]),
          "2": ("U2", "línea 2", "#2F6FB5", ["uni", "linden", "markt", "schiller", "stadion"]),
          "3": ("U3", "línea 3", "#2E9A5B", ["flughafen", "rathaus", "schiller", "museum", "hafen"])}


def correspondance(a, b):
    commun = [s for s in LIGNES[a][3] if s in LIGNES[b][3]]
    assert len(commun) == 1, (a, b, commun)
    return commun[0]


def an_de(s):
    nom, g, _ = STATIONS[s][0]
    return ("an der " if g == "die" else "am ") + nom


def von_de(s):
    nom, g, _ = STATIONS[s][0]
    return ("von der " if g == "die" else "vom ") + nom


def zu_de(s):
    nom, g, _ = STATIONS[s][0]
    return ("zur " if g == "die" else "zum ") + nom


def trajets():
    out = []
    for a in LIGNES:
        for b in LIGNES:
            if a == b: continue
            x = correspondance(a, b)
            inter = {correspondance(p, q) for p in LIGNES for q in LIGNES if p < q}
            for s in LIGNES[a][3]:
                for t in LIGNES[b][3]:
                    if s in inter or t in inter or s in LIGNES[b][3] or t in LIGNES[a][3]: continue
                    out.append({"de": s, "vers": t, "l1": a, "l2": b, "change": x})
    return out


# ---------------------------------------------------------------------------------------------------------------
# LES BILLETS : einfach oder hin und zurueck ? Et le prix. (ville, prix aller simple, prix aller-retour) par langue
PRIX_BILLETS = {"de": {"Hamburg": ((29, 90), (59, 80)), "München": ((49, 90), (89, 0)), "Köln": ((39, 90), (72, 0)), "Leipzig": ((19, 90), (37, 80)),
                       "Dresden": ((24, 90), (42, 0)), "Frankfurt": ((47, 0), (86, 0)), "Hannover": ((34, 90), (68, 0)), "Rostock": ((17, 90), (35, 80))},
                "es": {"Sevilla": ((67, 50), (98, 0)), "Valencia": ((36, 40), (64, 0)), "Barcelona": ((76, 0), (99, 0)), "Bilbao": ((45, 60), (84, 0)),
                       "Málaga": ((58, 20), (96, 0)), "Zaragoza": ((16, 90), (32, 0)), "Toledo": ((13, 90), (27, 80)), "Salamanca": ((26, 70), (49, 0))}}
RETOUR = {"de": [("am Sonntag", "dimanche", "on Sunday", "no domingo"), ("am Montag", "lundi", "on Monday", "na segunda-feira"),
                 ("am Freitag", "vendredi", "on Friday", "na sexta-feira"), ("morgen", "demain", "tomorrow", "amanhã"),
                 ("heute Abend", "ce soir", "tonight", "hoje à noite")],
          "es": [("el domingo", "dimanche", "on Sunday", "no domingo", "am Sonntag"), ("el lunes", "lundi", "on Monday", "na segunda-feira", "am Montag"),
                 ("el viernes", "vendredi", "on Friday", "na sexta-feira", "am Freitag"), ("mañana", "demain", "tomorrow", "amanhã", "morgen"),
                 ("esta noche", "ce soir", "tonight", "hoje à noite", "heute Abend")]}


# ---------------------------------------------------------------------------------------------------------------
# LA DONNEE DE LA PAGE : toutes les phrases (questions, reponses justes) et leurs traductions
def construire():
    d = {"_lisez_moi": "FABRIQUE par visuel/transportes/transportes.py -- ne pas modifier a la main.",
         "moyens": {}, "images": {}, "trad": {"de": {}, "es": {}}, "choix": {"de": {}, "es": {}}, "lectures": {"de": {}, "es": {}},
         "gloses": {"de": {}, "es": {}}, "stations": {}, "lignes": {}, "trajets": [], "tableaux": {}, "billets": {"de": [], "es": []}}
    tr = d["trad"]

    def trad(app, phrase, fr, en, pt, de=None):
        if phrase in tr[app] and tr[app][phrase]["fr"] != fr:
            raise SystemExit("deux traductions pour « %s » : %s / %s" % (phrase, tr[app][phrase]["fr"], fr))
        tr[app][phrase] = {"fr": fr, "en": en, "pt": pt}
        if de: tr[app][phrase]["de"] = de

    def choix(app, texte, fr, en, pt, de=None):
        c = {"fr": fr, "en": en, "pt": pt}
        if de: c["de"] = de
        d["choix"][app][texte] = c

    def lecture(app, ecrit, dit):
        if any(ch.isdigit() for ch in ecrit): d["lectures"][app][ecrit] = dit

    # --- les moyens de transport ---
    for m, (de_, es_, fr, en, pt) in MOYENS.items():
        d["moyens"][m] = {"de": {"genre": de_[0], "mot": de_[1], "mit": mit_de(m), "verbe": verbe_de(m)},
                          "es": {"genre": es_[0], "mot": es_[1], "en": en_es(m)}, "fr": fr, "en": en, "pt": pt}
        maj = lambda s: s[0].upper() + s[1:] + "."
        choix("de", maj(mit_de(m)), maj(fr), maj(en), maj(pt))
        choix("es", maj(en_es(m)), maj(fr), maj(en), maj(pt), maj(mit_de(m)))

    # --- les phrases d'une personne et d'un moyen : « Mark fährt mit dem Bus zur Arbeit. » ---
    phrases = {"de": [], "es": []}
    for m in MOYENS:
        de_, es_, fr, en, pt = MOYENS[m]
        v = verbe_de(m)
        for qui, sexe in PERS.items():
            dests_de = DEST_AVION["de"] if m == "flugzeug" else [(x[0], x[2], x[3], x[4]) for x in DEST]
            dests_es = DEST_AVION["es"] if m == "flugzeug" else [(x[1], x[2], x[3], x[4], x[0]) for x in DEST]
            for (dd, dfr, den, dpt) in dests_de:
                p = "%s %s %s %s." % (qui, CONJ_DE[v]["er"], mit_de(m), dd)
                ich = "%s sagt: „Ich %s %s %s.“" % (qui, CONJ_DE[v]["ich"], mit_de(m), dd)
                q = "Wie kommt %s %s?" % (qui, dd)
                frp = "%s va %s %s." % (qui, dfr, fr)
                trad("de", p, frp, "%s goes %s %s." % (qui, den, en), "%s vai %s %s." % (qui, dpt, pt))
                trad("de", ich, "%s dit : « Je vais %s %s. »" % (qui, dfr, fr), "%s says: “I go %s %s.”" % (qui, den, en),
                     "%s diz: “Eu vou %s %s.”" % (qui, dpt, pt))
                phrases["de"].append({"qui": qui, "moyen": m, "dest": dd, "phrase": p, "ich": ich, "q": q,
                                      "trou": "%s ___ %s %s." % (qui, mit_de(m), dd), "trouIch": "%s sagt: „Ich ___ %s %s.“" % (qui, mit_de(m), dd),
                                      "trouMit": "%s geht ___ Fuß %s." % (qui, dd) if m == "fuss" else "%s %s mit ___ %s %s." % (qui, CONJ_DE[v]["er"], de_[1], dd),
                                      "verbe": v})
            for (dd, dfr, den, dpt, dde) in dests_es:
                p = "%s va %s %s." % (qui, dd, en_es(m))
                yo = "%s dice: «Voy %s %s.»" % (qui, dd, en_es(m))
                q = "¿Cómo va %s %s?" % (qui, dd)
                gde = "%s %s %s %s." % (qui, CONJ_DE[v]["er"], mit_de(m), dde)
                trad("es", p, "%s va %s %s." % (qui, dfr, fr), "%s goes %s %s." % (qui, den, en), "%s vai %s %s." % (qui, dpt, pt), gde)
                trad("es", yo, "%s dit : « Je vais %s %s. »" % (qui, dfr, fr), "%s says: “I go %s %s.”" % (qui, den, en),
                     "%s diz: “Eu vou %s %s.”" % (qui, dpt, pt), "%s sagt: „Ich %s %s %s.“" % (qui, CONJ_DE[v]["ich"], mit_de(m), dde))
                phrases["es"].append({"qui": qui, "moyen": m, "dest": dd, "phrase": p, "ich": yo, "q": q,
                                      "trou": "%s ___ %s %s." % (qui, dd, en_es(m)), "trouIch": "%s dice: «___ %s %s.»" % (qui, dd, en_es(m)),
                                      "trouMit": "%s va %s ___ %s." % (qui, dd, "pie" if m == "fuss" else es_[1]), "verbe": "ir"})
    d["phrases"] = phrases

    # --- les images, et la phrase de chaque image ---
    GESTE_FR = {"ein": ("monte dans", "gets on", "entra n"), "aus": ("descend d", "gets off", "desce d")}
    for id, im in IMAGES.items():
        e = {"qui": im["qui"], "moyen": im.get("moyen"), "geste": im.get("geste"), "action": im.get("action"), "essai": bool(im.get("essai"))}
        qui, m, g = im["qui"], im.get("moyen"), im.get("geste")
        if g:
            gd, mot = MOYENS[m][0]
            ges, motes = MOYENS[m][1]
            fr_nom = {"bus": ("le", "bus"), "zug": ("le", "train"), "tram": ("le", "tram"), "taxi": ("le", "taxi"), "ubahn": ("le", "métro")}[m]
            en_nom = {"bus": "bus", "zug": "train", "tram": "tram", "taxi": "taxi", "ubahn": "subway"}[m]
            pt_nom = {"bus": ("o", "ônibus"), "zug": ("o", "trem"), "tram": ("o", "bonde"), "taxi": ("o", "táxi"), "ubahn": ("o", "metrô")}[m]
            if g == "ein":
                de = {"phrase": "%s steigt in %s %s ein." % (qui, AKK[gd], mot), "art": AKK[gd], "prep": "in"}
                es = {"phrase": "%s sube al %s." % (qui, motes), "verbe": "subir", "contr": "al"}
                fr = "%s monte dans %s %s." % (qui, fr_nom[0], fr_nom[1])
                en = ("%s gets into the %s." if m == "taxi" else "%s gets on the %s.") % (qui, en_nom)
                pt = "%s entra no %s." % (qui, pt_nom[1])
            else:
                de = {"phrase": "%s steigt aus %s %s aus." % (qui, DAT[gd], mot), "art": DAT[gd], "prep": "aus"}
                es = {"phrase": "%s baja del %s." % (qui, motes), "verbe": "bajar", "contr": "del"}
                fr = "%s descend du %s." % (qui, fr_nom[1])
                en = ("%s gets out of the %s." if m == "taxi" else "%s gets off the %s.") % (qui, en_nom)
                pt = ("%s sai do %s." if m == "taxi" else "%s desce do %s.") % (qui, pt_nom[1])
            trad("de", de["phrase"], fr, en, pt)
            trad("es", es["phrase"], fr, en, pt, de["phrase"])
            e["de"], e["es"] = de, es
        elif im.get("action") == "kaufen":
            e["de"] = {"phrase": "Mark kauft eine Fahrkarte am Automaten."}
            e["es"] = {"phrase": "Mark compra un billete en la máquina."}
            trad("de", e["de"]["phrase"], "Mark achète un billet au distributeur.", "Mark buys a ticket from the machine.", "Mark compra uma passagem na máquina.")
            trad("es", e["es"]["phrase"], "Mark achète un billet au distributeur.", "Mark buys a ticket from the machine.", "Mark compra uma passagem na máquina.",
                 e["de"]["phrase"])
        if m and not g:
            # la phrase de l'image seule, sans destination : « Anna fährt mit der U-Bahn. », « Anna va en metro. »
            v = verbe_de(m)
            de_p = "%s %s %s." % (qui, CONJ_DE[v]["er"], mit_de(m))
            es_p = "%s va %s." % (qui, en_es(m))
            fr, en, pt = MOYENS[m][2:]
            trad("de", de_p, "%s y va %s." % (qui, fr) if m != "flugzeug" else "%s voyage en avion." % qui,
                 "%s goes %s." % (qui, en) if m != "flugzeug" else "%s is travelling by plane." % qui,
                 "%s vai %s." % (qui, pt) if m != "flugzeug" else "%s viaja de avião." % qui)
            trad("es", es_p, "%s y va %s." % (qui, fr) if m != "flugzeug" else "%s voyage en avion." % qui,
                 "%s goes %s." % (qui, en) if m != "flugzeug" else "%s is travelling by plane." % qui,
                 "%s vai %s." % (qui, pt) if m != "flugzeug" else "%s viaja de avião." % qui, de_p)
            e["de"], e["es"] = {"phrase": de_p}, {"phrase": es_p}
        d["images"][id] = e
    # les phrases « fausses » du vrai ou faux, sur une image d'un geste : le geste contraire (aussteigen pour einsteigen)
    for id, e in d["images"].items():
        if e["geste"]:
            autre = next((k for k, x in d["images"].items() if x["moyen"] == e["moyen"] and x["geste"] and x["geste"] != e["geste"]), None)
            e["contraire"] = autre
            # le geste contraire, meme si son image n'existe pas (le tram, le taxi) : la phrase fausse du vrai ou faux
            qui, m = e["qui"], e["moyen"]
            gd, mot = MOYENS[m][0]; motes = MOYENS[m][1][1]
            if e["geste"] == "ein":
                e["de"]["faux"] = "%s steigt aus %s %s aus." % (qui, DAT[gd], mot); e["es"]["faux"] = "%s baja del %s." % (qui, motes)
            else:
                e["de"]["faux"] = "%s steigt in %s %s ein." % (qui, AKK[gd], mot); e["es"]["faux"] = "%s sube al %s." % (qui, motes)

    # les groupes que les choix proposent (« in den … ein ») et leur traduction quand l'eleve les choisit a tort
    choix("de", "in … ein", "monter dans", "get on", "entrar em")
    choix("de", "aus … aus", "descendre de", "get off", "descer de")
    choix("es", "sube al", "monte dans le", "gets on the", "sobe no", "steigt in … ein")
    choix("es", "baja del", "descend du", "gets off the", "desce do", "steigt aus … aus")

    # --- le plan du metro ---
    for s, ((nde, g, nes), x, y) in STATIONS.items():
        d["stations"][s] = {"de": nde, "genre": g, "es": nes, "x": x, "y": y, "an": an_de(s)}
    for k, (nde, nes, coul, st) in LIGNES.items():
        d["lignes"][k] = {"de": nde, "es": nes, "couleur": coul, "stations": st}
    for t in trajets():
        for qui, sexe in PERS.items():
            s, v, x = STATIONS[t["de"]][0], STATIONS[t["vers"]][0], STATIONS[t["change"]][0]
            l2de, l2es = LIGNES[t["l2"]][0], LIGNES[t["l2"]][1]
            er, ilfr, heen = PRON["de"][sexe], PRON["fr"][sexe], PRON["en"][sexe]
            # allemand
            debut = "%s fährt %s %s." % (qui, von_de(t["de"]), zu_de(t["vers"]))
            ph = debut + " %s steigt %s um." % (er.capitalize(), an_de(t["change"]))
            phl = debut + " %s steigt %s in die %s um." % (er.capitalize(), an_de(t["change"]), l2de)
            frd = "%s va de %s à %s." % (qui, s[0], v[0])
            trad("de", ph, frd + " %s change à %s." % (ilfr.capitalize(), x[0]), "%s goes from %s to %s. %s changes at %s." % (qui, s[0], v[0], heen.capitalize(), x[0]),
                 "%s vai de %s para %s. %s faz baldeação em %s." % (qui, s[0], v[0], PRON["pt"][sexe].capitalize(), x[0]))
            trad("de", phl, frd + " À %s, %s prend la %s." % (x[0], ilfr, l2de), "%s goes from %s to %s. At %s %s changes to the %s." % (qui, s[0], v[0], x[0], heen, l2de),
                 "%s vai de %s para %s. Em %s, %s muda para a %s." % (qui, s[0], v[0], x[0], PRON["pt"][sexe], l2de))
            # espagnol
            debes = "%s va de %s a %s." % (qui, s[2], v[2])
            phe = debes + " Cambia de línea en %s." % x[2]
            phel = debes + " En %s cambia a la %s." % (x[2], l2es)
            fres = "%s va de %s à %s." % (qui, s[2], v[2])
            trad("es", phe, fres + " %s change de ligne à %s." % (ilfr.capitalize(), x[2]), "%s goes from %s to %s. %s changes lines at %s." % (qui, s[2], v[2], heen.capitalize(), x[2]),
                 "%s vai de %s para %s. %s troca de linha em %s." % (qui, s[2], v[2], PRON["pt"][sexe].capitalize(), x[2]),
                 "%s fährt von %s nach %s. %s steigt in %s um." % (qui, s[2], v[2], er.capitalize(), x[2]))
            trad("es", phel, fres + " À %s, %s prend la ligne %s." % (x[2], ilfr, t["l2"]), "%s goes from %s to %s. At %s %s changes to line %s." % (qui, s[2], v[2], x[2], heen, t["l2"]),
                 "%s vai de %s para %s. Em %s, %s muda para a linha %s." % (qui, s[2], v[2], x[2], PRON["pt"][sexe], t["l2"]),
                 "%s fährt von %s nach %s. In %s steigt %s in die Linie %s um." % (qui, s[2], v[2], x[2], er, t["l2"]))
            d["trajets"].append(dict(t, qui=qui, de_={"debut": debut, "q": debut + " Wo steigt %s um?" % er, "phrase": ph,
                                                      "qL": debut + " In welche Linie steigt %s %s um?" % (er, an_de(t["change"])), "phraseL": phl},
                                     es={"debut": debes, "q": debes + " ¿Dónde cambia de línea?", "phrase": phe,
                                         "qL": debes + " En %s, ¿a qué línea cambia?" % x[2], "phraseL": phel}))
    # le nom de la ligne lu en lettres (U2 -> U zwei ; la linea 2 -> la línea dos)
    for t in d["trajets"]:
        for app, cle in (("de", "de_"), ("es", "es")):
            for k in ("phraseL", "qL"):
                txt = t[cle][k]
                if app == "de":
                    lecture("de", txt, txt.replace("U1", "U eins").replace("U2", "U zwei").replace("U3", "U drei"))
                else:
                    lecture("es", txt, txt.replace("línea 1", "línea uno").replace("línea 2", "línea dos").replace("línea 3", "línea tres"))
    for k, (nde, nes, coul, st) in LIGNES.items():
        choix("de", "In die %s." % nde, "La %s." % nde, "The %s." % nde, "A %s." % nde)
        choix("es", "A la %s." % nes, "La ligne %s." % k, "Line %s." % k, "A linha %s." % k, "In die Linie %s." % k)
        lecture("de", "In die %s." % nde, "In die U " + nombre_de(int(k)) + ".")
        lecture("es", "A la %s." % nes, "A la línea " + nombre_es(int(k)) + ".")

    # --- les tableaux des departs ---
    for app in ("de", "es"):
        tabs = tableaux(app)
        d["tableaux"][app] = []
        for lignes in tabs:
            out = []
            for l in lignes:
                v = VILLES[app][l["ville"]]
                h, m = l["h"], l["m"]
                he = heure_ecrite(h, m)
                if app == "de":
                    vil = v[0]
                    a = "Der Zug nach %s fährt um %s Uhr ab." % (vil, he)
                    b = "Der Zug nach %s fährt von Gleis %d ab." % (vil, l["voie"])
                    c = "Der Zug nach %s hat %d Minuten Verspätung." % (vil, l["retard"]) if l["retard"] else None
                    fra, frb = "Le train pour %s part à %d h %02d." % (v[1], h, m), "Le train pour %s part de la voie %d." % (v[1], l["voie"])
                    ena, enb = "The train to %s leaves at %s." % (v[2], he), "The train to %s leaves from platform %d." % (v[2], l["voie"])
                    pta, ptb = "O trem para %s sai às %dh%02d." % (v[3], h, m), "O trem para %s sai da plataforma %d." % (v[3], l["voie"])
                    trad("de", a, fra, ena, pta); trad("de", b, frb, enb, ptb)
                    lecture("de", a, a.replace(he + " Uhr", heure_dite_de(h, m)))
                    lecture("de", b, b.replace("Gleis %d" % l["voie"], "Gleis " + nombre_de(l["voie"])))
                    r = {"heure": he, "ville": vil, "voie": l["voie"], "retard": l["retard"], "h": h, "m": m,
                         "phraseHeure": a, "phraseVoie": b, "qHeure": "Wann fährt der Zug nach %s ab?" % vil,
                         "qVoie": "Von welchem Gleis fährt der Zug nach %s ab?" % vil, "qVille": "Wohin fährt der Zug um %s Uhr?" % he,
                         "repHeure": "Um %s Uhr." % he, "repVoie": "Von Gleis %d." % l["voie"], "repVille": "Nach %s." % vil}
                    lecture("de", r["qVille"], r["qVille"].replace(he + " Uhr", heure_dite_de(h, m)))
                    lecture("de", r["repHeure"], "Um %s." % heure_dite_de(h, m))
                    lecture("de", r["repVoie"], "Von Gleis %s." % nombre_de(l["voie"]))
                    choix("de", r["repVille"], "Pour %s." % v[1], "To %s." % v[2], "Para %s." % v[3])
                    if c:
                        trad("de", c, "Le train pour %s a %d minutes de retard." % (v[1], l["retard"]), "The train to %s is %d minutes late." % (v[2], l["retard"]),
                             "O trem para %s está %d minutos atrasado." % (v[3], l["retard"]))
                        lecture("de", c, c.replace("%d Minuten" % l["retard"], nombre_de(l["retard"]) + " Minuten"))
                        r.update(phraseRetard=c, qRetard="Wie viel Verspätung hat der Zug nach %s?" % vil, repRetard="%d Minuten." % l["retard"])
                        lecture("de", r["repRetard"], nombre_de(l["retard"]).capitalize() + " Minuten.")
                    if m in (15, 30, 45):
                        mots = heure_mots_de(h, m)
                        p = "Der Zug nach %s fährt um %s ab." % (vil, mots)
                        trad("de", p, "Le train pour %s part à %s." % (v[1], heure_mots_fr(h, m)), "The train to %s leaves at %s." % (v[2], heure_mots_en(h, m)),
                             "O trem para %s sai às %s." % (v[3], heure_mots_pt(h, m)))
                        r.update(mots=mots, phraseMots=p, leurresMots=leurres_heure(h, m, "de"),
                                 trouMots="Der Zug nach %s fährt um %s Uhr ab. Man sagt auch: um ___." % (vil, he))
                        lecture("de", r["trouMots"], r["trouMots"].replace(he + " Uhr", heure_dite_de(h, m)))
                else:
                    vil = v[0]
                    a = "El tren para %s sale a las %s." % (vil, he)
                    b = "El tren para %s sale del andén %d." % (vil, l["voie"])
                    c = "El tren para %s tiene %d minutos de retraso." % (vil, l["retard"]) if l["retard"] else None
                    trad("es", a, "Le train pour %s part à %d h %02d." % (v[1], h, m), "The train to %s leaves at %s." % (v[2], he),
                         "O trem para %s sai às %dh%02d." % (v[3], h, m), "Der Zug nach %s fährt um %s Uhr ab." % (v[4], he))
                    trad("es", b, "Le train pour %s part du quai %d." % (v[1], l["voie"]), "The train to %s leaves from platform %d." % (v[2], l["voie"]),
                         "O trem para %s sai da plataforma %d." % (v[3], l["voie"]), "Der Zug nach %s fährt von Gleis %d ab." % (v[4], l["voie"]))
                    lecture("es", a, a.replace("las " + he, "las " + heure_dite_es(h, m)))
                    lecture("es", b, b.replace("andén %d" % l["voie"], "andén " + nombre_es(l["voie"])))
                    r = {"heure": he, "ville": vil, "voie": l["voie"], "retard": l["retard"], "h": h, "m": m,
                         "phraseHeure": a, "phraseVoie": b, "qHeure": "¿A qué hora sale el tren para %s?" % vil,
                         "qVoie": "¿De qué andén sale el tren para %s?" % vil, "qVille": "¿Adónde va el tren de las %s?" % he,
                         "repHeure": "A las %s." % he, "repVoie": "Del andén %d." % l["voie"], "repVille": "A %s." % vil}
                    lecture("es", r["qVille"], r["qVille"].replace("las " + he, "las " + heure_dite_es(h, m)))
                    lecture("es", r["repHeure"], "A las %s." % heure_dite_es(h, m))
                    lecture("es", r["repVoie"], "Del andén %s." % nombre_es(l["voie"]))
                    choix("es", r["repVille"], "Pour %s." % v[1], "To %s." % v[2], "Para %s." % v[3], "Nach %s." % v[4])
                    if c:
                        trad("es", c, "Le train pour %s a %d minutes de retard." % (v[1], l["retard"]), "The train to %s is %d minutes late." % (v[2], l["retard"]),
                             "O trem para %s está %d minutos atrasado." % (v[3], l["retard"]), "Der Zug nach %s hat %d Minuten Verspätung." % (v[4], l["retard"]))
                        lecture("es", c, c.replace("%d minutos" % l["retard"], nombre_es(l["retard"]) + " minutos"))
                        r.update(phraseRetard=c, qRetard="¿Cuánto retraso tiene el tren para %s?" % vil, repRetard="%d minutos." % l["retard"])
                        lecture("es", r["repRetard"], nombre_es(l["retard"]).capitalize() + " minutos.")
                    if m in (15, 30, 45):
                        mots = heure_mots_es(h, m)
                        p = "El tren para %s sale a %s." % (vil, mots)
                        trad("es", p, "Le train pour %s part à %s." % (v[1], heure_mots_fr(h, m)), "The train to %s leaves at %s." % (v[2], heure_mots_en(h, m)),
                             "O trem para %s sai às %s." % (v[3], heure_mots_pt(h, m)), "Der Zug nach %s fährt um %s ab." % (v[4], heure_mots_de(h, m)))
                        r.update(mots=mots, phraseMots=p, leurresMots=leurres_heure(h, m, "es"),
                                 trouMots="El tren para %s sale a las %s. Es decir, a ___." % (vil, he))
                        lecture("es", r["trouMots"], r["trouMots"].replace("las " + he, "las " + heure_dite_es(h, m)))
                out.append(r)
            d["tableaux"][app].append(out)

    # --- les billets : einfach oder hin und zurueck ? et le prix ---
    for app in ("de", "es"):
        for i, (vil, (pa, pr)) in enumerate(PRIX_BILLETS[app].items()):
            v = next(x for x in VILLES[app] if x[0] == vil)
            for qui, sexe in PERS.items():
                for j, ret in enumerate(RETOUR[app] + [None]):
                    if app == "de":
                        if ret:
                            sit = "%s fährt nach %s und kommt %s zurück." % (qui, vil, ret[0])
                            fr = "%s va à %s et revient %s." % (qui, v[1], ret[1]); en = "%s is going to %s and coming back %s." % (qui, v[2], ret[2])
                            pt = "%s vai para %s e volta %s." % (qui, v[3], ret[3])
                        else:
                            sit = "%s fährt nach %s und bleibt dort." % (qui, vil)
                            fr = "%s va à %s et y reste." % (qui, v[1]); en = "%s is going to %s and staying there." % (qui, v[2]); pt = "%s vai para %s e fica lá." % (qui, v[3])
                        trad("de", sit, fr, en, pt)
                        rep = "Hin und zurück, bitte." if ret else "Einfach, bitte."
                    else:
                        if ret:
                            sit = "%s va a %s y vuelve %s." % (qui, vil, ret[0])
                            fr = "%s va à %s et revient %s." % (qui, v[1], ret[1]); en = "%s is going to %s and coming back %s." % (qui, v[2], ret[2])
                            pt = "%s vai para %s e volta %s." % (qui, v[3], ret[3]); de = "%s fährt nach %s und kommt %s zurück." % (qui, v[4], ret[4])
                        else:
                            sit = "%s va a %s y se queda allí." % (qui, vil)
                            fr = "%s va à %s et y reste." % (qui, v[1]); en = "%s is going to %s and staying there." % (qui, v[2])
                            pt = "%s vai para %s e fica lá." % (qui, v[3]); de = "%s fährt nach %s und bleibt dort." % (qui, v[4])
                        trad("es", sit, fr, en, pt, de)
                        rep = "De ida y vuelta, por favor." if ret else "Solo de ida, por favor."
                    d["billets"][app].append({"ville": vil, "qui": qui, "situation": sit, "retour": bool(ret), "rep": rep})
            # le prix : l'aller simple et l'aller-retour
            for (e, c), ar in ((pa, False), (pr, True)):
                if app == "de":
                    ecrit = prix_ecrit_de(e, c)
                    ph = "Die Fahrkarte nach %s kostet %s." % (vil, ecrit) if not ar else "Hin und zurück nach %s kostet %s." % (vil, ecrit)
                    q = "Was kostet die Fahrkarte nach %s?" % vil if not ar else "Was kostet die Fahrkarte nach %s hin und zurück?" % vil
                    mots, leurres = prix_mots_de(e, c), leurres_prix(e, c, "de")
                    frp = ("Le billet pour %s coûte %s." if not ar else "L'aller-retour pour %s coûte %s.") % (v[1], ecrit.replace(",", ","))
                    enp = ("The ticket to %s costs €%s." if not ar else "A return ticket to %s costs €%s.") % (v[2], ecrit.replace(" €", "").replace(",", "."))
                    ptp = ("A passagem para %s custa %s." if not ar else "Ida e volta para %s custa %s.") % (v[3], ecrit)
                    trad("de", ph, frp, enp, ptp)
                    lecture("de", ph, ph.replace(ecrit, mots))
                else:
                    ecrit = prix_ecrit_de(e, c)
                    ph = "El billete para %s cuesta %s." % (vil, ecrit) if not ar else "El billete de ida y vuelta para %s cuesta %s." % (vil, ecrit)
                    q = "¿Cuánto cuesta el billete para %s?" % vil if not ar else "¿Cuánto cuesta el billete de ida y vuelta para %s?" % vil
                    mots, leurres = prix_mots_es(e, c), leurres_prix(e, c, "es")
                    trad("es", ph, ("Le billet pour %s coûte %s." if not ar else "L'aller-retour pour %s coûte %s.") % (v[1], ecrit),
                         ("The ticket to %s costs €%s." if not ar else "A return ticket to %s costs €%s.") % (v[2], ecrit.replace(" €", "").replace(",", ".")),
                         ("A passagem para %s custa %s." if not ar else "Ida e volta para %s custa %s.") % (v[3], ecrit),
                         ("Die Fahrkarte nach %s kostet %s." if not ar else "Hin und zurück nach %s kostet %s.") % (v[4], ecrit))
                    lecture("es", ph, ph.replace(ecrit, mots))
                d.setdefault("prix", {"de": [], "es": []})[app].append({"ville": vil, "ar": ar, "ecrit": ecrit, "phrase": ph, "q": q, "mots": mots, "leurres": leurres})
    choix("de", "Einfach, bitte.", "Un aller simple, s'il vous plaît.", "One way, please.", "Só ida, por favor.")
    choix("de", "Hin und zurück, bitte.", "Un aller-retour, s'il vous plaît.", "Return, please.", "Ida e volta, por favor.")
    choix("es", "Solo de ida, por favor.", "Un aller simple, s'il vous plaît.", "One way, please.", "Só ida, por favor.", "Einfach, bitte.")
    choix("es", "De ida y vuelta, por favor.", "Un aller-retour, s'il vous plaît.", "Return, please.", "Ida e volta, por favor.", "Hin und zurück, bitte.")
    gloses(d)
    return d


# LES GLOSES : la traduction de chaque mot teste, prise au CORPUS RELU (pour les langues ou la phrase n'est pas
# traduite : turc, ukrainien, persan, arabe, polonais, russe -- « der Bus — автобус »)
MOTS_DE = {"noms": [MOYENS[m][0] for m in MOYENS] + [("die", "Fahrkarte"), ("das", "Gleis"), ("die", "Verspätung")],
           "verbes": ["fahren", "gehen", "fliegen", "einsteigen", "aussteigen", "umsteigen", "abfahren", "kosten", "kaufen"]}
MOTS_ES = {"noms": [MOYENS[m][1] for m in MOYENS] + [("el", "billete"), ("el", "andén"), ("el", "retraso")],
           "verbes": ["ir", "subir", "bajar", "cambiar", "salir", "costar", "comprar"]}


def gloses(d):
    LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru", "de"]
    champ = lambda w, l: w.get("traduction" if l == "fr" else "traduction_" + l)

    def pose(app, cle, w):
        if cle not in d["gloses"][app]:
            d["gloses"][app][cle] = {l: champ(w, l) for l in LANGUES if champ(w, l)}

    def parcourir(o, fn):
        if isinstance(o, dict):
            if "infinitif" in o: fn(o)
            for v in o.values(): parcourir(v, fn)
        elif isinstance(o, list):
            for v in o: parcourir(v, fn)
    th = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))["themes"]
    for t in th:
        for w in t.get("mots", []):
            if (w.get("genre"), w.get("mot")) in MOTS_DE["noms"]: pose("de", w["mot"], w)
    parcourir(json.load(io.open(os.path.join(RACINE, "verbe.json"), encoding="utf-8")), lambda w: w["infinitif"] in MOTS_DE["verbes"] and pose("de", w["infinitif"], w))
    te = json.load(io.open(os.path.join(RACINE, "espanol", "datos", "temas.json"), encoding="utf-8"))["themes"]
    for t in te:
        for w in t.get("mots", []):
            if (w.get("genre"), w.get("mot")) in MOTS_ES["noms"]: pose("es", w["mot"], w)
    parcourir(json.load(io.open(os.path.join(RACINE, "espanol", "datos", "verbos.json"), encoding="utf-8")), lambda w: w["infinitif"] in MOTS_ES["verbes"] and pose("es", w["infinitif"], w))
    manque = [m for g, m in MOTS_DE["noms"] if m not in d["gloses"]["de"]] + [v for v in MOTS_DE["verbes"] if v not in d["gloses"]["de"]]
    manque += [m for g, m in MOTS_ES["noms"] if m not in d["gloses"]["es"]] + [v for v in MOTS_ES["verbes"] if v not in d["gloses"]["es"]]
    if manque:
        raise SystemExit("mots absents du corpus : %s" % manque)
    d["mots"] = {"de": {"noms": MOTS_DE["noms"], "verbes": MOTS_DE["verbes"]}, "es": {"noms": MOTS_ES["noms"], "verbes": MOTS_ES["verbes"]}}


def ecrire_voix(d):
    """TOUTES LES PHRASES que la page peut dire (visuel/transportes/toutes-les-phrases.json), par langue, et le nombre
    de caracteres DITS (les nombres en lettres) : le plafond de ce qu'il faudrait enregistrer. Ce qui s'enregistre
    vraiment (strategie des voix du 3 nov. : le telephone d'ici la, rien sans l'accord de Jacques) est l'inventaire de
    visuel/voix_themes.py, qui joue des parties -> visuel/transportes/voix.json."""
    def textes(app):
        t = set(d["trad"][app])
        for lignes in d["tableaux"][app]:
            for r in lignes:
                t.update(x for x in (r.get("phraseHeure"), r.get("phraseVoie"), r.get("phraseRetard"), r.get("phraseMots")) if x)
        t.update(p["phrase"] for p in d["prix"][app])
        return sorted(t)
    v = {"_lisez_moi": "FABRIQUE par visuel/transportes/transportes.py : les textes a enregistrer (ElevenLabs v2, accord de Jacques). "
                       "Un texte a chiffres se dit par sa lecture (cle « lectures » de transportes.json, a recopier dans audio/lectures/<langue>.json).",
         "de": textes("de"), "es": textes("es")}
    dit = lambda app, t: d["lectures"][app].get(t, t)
    v["credits"] = {"de (Aurora)": sum(len(dit("de", t)) for t in v["de"]), "es (Lolita + Monica)": 2 * sum(len(dit("es", t)) for t in v["es"])}
    io.open(os.path.join(ICI, "toutes-les-phrases.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(v, ensure_ascii=False, indent=1) + "\n")
    return v["credits"]


def ecrire_json():
    os.makedirs(PROTO, exist_ok=True)
    d = construire()
    print("  toutes les phrases (credits, au plus) :", ecrire_voix(d))
    io.open(os.path.join(PROTO, "transportes.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("  visuel/prototype/transportes/transportes.json : %d images, %d trajets, %d billets, %d phrases traduites (de), %d (es), %d lectures (de), %d (es)"
          % (len(d["images"]), len(d["trajets"]), len(d["billets"]["de"]), len(d["trad"]["de"]), len(d["trad"]["es"]),
             len(d["lectures"]["de"]), len(d["lectures"]["es"])))


# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES
def prompt(id):
    im = IMAGES[id]
    ordre = "The first picture is the PERSON." if not im.get("base") else "The first picture is the previous shot; the second is the PERSON."
    if im.get("lieu"): ordre += " The last picture is the PLACE."
    lieu = LIEU_TXT.get(im.get("lieu"), "")
    if im.get("base"):
        return STYLE + ordre + " " + im["prompt"] + " Keep everything else exactly as in the previous shot: same place, same light, same framing."
    return STYLE + ordre + " " + lieu + im["prompt"]


def references(id):
    im = IMAGES[id]
    refs = []
    if im.get("base"): refs.append(os.path.join(IMG, im["base"] + ".png"))
    refs.append(REF[im["qui"]])
    if im.get("lieu"): refs.append(LIEUX[im["lieu"]])
    return refs


def recadrer():
    """Les images GRATUITES, recadrees dans une scene (la meme personne au meme endroit) : 4:3, 1200 px."""
    from PIL import Image
    for id, im in IMAGES.items():
        if not im.get("recadrage"): continue
        scene, boite = im["recadrage"]
        src = Image.open(LIEUX[scene]).convert("RGB").crop(boite)
        src.resize((1200, 900), Image.LANCZOS).save(os.path.join(PROTO, id + ".webp"), quality=80, method=6)
        print("  recadree :", id)


def provisoires():
    """Des images DESSINEES (aplats), gratuites, pour essayer la page avant les photos. Elles portent « PROVISOIRE »
    et NE SE COMMITTENT PAS."""
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1200, 900
    f = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 46)
    p = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 30)
    COUL = {"bus": (240, 196, 40), "ubahn": (240, 196, 40), "tram": (240, 210, 60), "zug": (220, 220, 225), "auto": (150, 155, 165),
            "taxi": (236, 224, 190), "fahrrad": (60, 120, 200), "flugzeug": (200, 220, 240), "fuss": (190, 210, 190), None: (200, 200, 200)}
    os.makedirs(PROTO, exist_ok=True)
    for id, im in IMAGES.items():
        if im.get("recadrage"): continue
        m = im.get("moyen")
        img = Image.new("RGB", (W, H), (226, 232, 238))
        dr = ImageDraw.Draw(img)
        dr.rectangle((0, int(H * .7), W, H), fill=(170, 170, 170))
        dr.rounded_rectangle((120, 260, 1080, 640), 40, fill=COUL[m], outline=(60, 60, 60), width=4)
        g = im.get("geste")
        dr.ellipse((560 if g != "aus" else 820, 300, 680 if g != "aus" else 940, 420), fill=(60, 60, 70))
        dr.text((W / 2, 150), "%s · %s" % (im["qui"], m or im.get("action")), fill=(30, 30, 30), font=f, anchor="mm")
        if g: dr.text((W / 2, 700), {"ein": "→ steigt ein / sube", "aus": "← steigt aus / baja"}[g], fill=(30, 30, 30), font=p, anchor="mm")
        dr.text((W / 2, 60), "PROVISOIRE -- image fal en attente", fill=(160, 40, 40), font=p, anchor="mm")
        img.save(os.path.join(PROTO, id + ".webp"), quality=75)
    print("  %d images provisoires dans visuel/prototype/transportes/ (a ne pas committer)" % len(IMAGES))


def payer(ids):
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    os.makedirs(IMG, exist_ok=True)
    a_faire = [i for i in (ids or PAYANTES) if i in PAYANTES and not os.path.exists(os.path.join(IMG, i + ".png"))]
    deja = sum(json.load(io.open(os.path.join(IMG, f), encoding="utf-8")).get("prix", PRIX) for f in os.listdir(IMG) if f.endswith("-fal.json"))
    print("  %d image(s) a faire, %.2f $ (deja depense : %.2f $, plafond %.2f $)" % (len(a_faire), len(a_faire) * PRIX, deja, PLAFOND))
    if deja + len(a_faire) * PRIX > PLAFOND + 1e-9:
        raise SystemExit("  PLAFOND DEPASSE : rien n'est lance.")
    cle = O.cle()
    for id in a_faire:
        refs = references(id)
        manque = [r for r in refs if not os.path.exists(r)]
        if manque:
            print("  %s : reference absente %s -- sautee" % (id, manque)); continue
        corps = {"prompt": prompt(id), "aspect_ratio": "4:3", "resolution": "2K", "output_format": "png", "num_images": 1,
                 "image_urls": [O.deposer(r, "image/webp" if r.endswith(".webp") else "image/png", cle)[0] for r in refs]}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle)
        sortie = os.path.join(IMG, id + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(IMG, id + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": EDIT, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": corps["prompt"], "references": [os.path.basename(r) for r in refs], "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", os.path.relpath(sortie, RACINE), "(%.2f $)" % PRIX)


def webp():
    from PIL import Image
    for id in PAYANTES:
        src = os.path.join(IMG, id + ".png")
        if not os.path.exists(src): continue
        im = Image.open(src).convert("RGB")
        if IMAGES[id].get("cadre"): im = im.crop(IMAGES[id]["cadre"])
        im = im.resize((1200, round(1200 * im.height / im.width)), Image.LANCZOS)
        im.save(os.path.join(PROTO, id + ".webp"), quality=78, method=6)
        print("  ", id)


def main():
    a = sys.argv[1:]
    if "--montrer" in a:
        for id in PAYANTES:
            print("\n  %s%s  (%s)\n  %s" % (id, "  [planche d'essai]" if IMAGES[id].get("essai") else "",
                                           ", ".join(os.path.basename(r) for r in references(id)), prompt(id)))
        print("\n  %d images, %.2f $ (planche d'essai : %d, %.2f $)" % (len(PAYANTES), len(PAYANTES) * PRIX,
              sum(1 for i in IMAGES.values() if i.get("essai")), sum(PRIX for i in IMAGES.values() if i.get("essai"))))
        return
    if "--provisoires" in a:
        provisoires()
    if "--payer" in a:
        payer([x for x in a if not x.startswith("--")])
    if "--webp" in a:
        webp()
    recadrer()
    ecrire_json()


if __name__ == "__main__":
    main()
