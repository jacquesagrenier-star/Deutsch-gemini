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
    ("pequeno", "El piso {v} ___.", "m"), ("pequeno", "La cocina {v} ___.", "f"),
    ("lleno", "El autobús {v} ___.", "m"), ("lleno", "La nevera {v} ___.", "f"),
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
