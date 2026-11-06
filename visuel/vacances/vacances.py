# -*- coding: utf-8 -*-
"""« Les vacances et le voyage », theme illustre (vague 4, 5 nov. 2026 : « les vacances et le voyage (Perfekt /
preterito) »). LA SEULE SOURCE du theme : les trois voyages, leurs etapes, les mots, les reservations, les deux
valises, les faits du temps qu'il fait et les prompts des images. La page (visuel/prototype/vacances.html) lit
vacances.json, fabrique ses phrases avec les memes regles et ne contient aucune phrase ecrite a la main.

    python visuel/vacances/vacances.py --json        # vacances.json et gloses.json seuls, gratuit
    python visuel/vacances/vacances.py --montrer     # les prompts des images, gratuit
    python visuel/vacances/vacances.py --provisoire  # des images provisoires (aplats + visages), gratuit, A NE PAS COMMITTER
    python visuel/vacances/vacances.py --web         # les webp (originaux fal + images des scenes recadrees)
    python visuel/vacances/vacances.py --planche     # les 6 images de la planche d'essai : FACTURE, 0,90 $
    python visuel/vacances/vacances.py anna-altstadt # celle-la seulement : FACTURE, 0,15 $
    python visuel/vacances/vacances.py               # toutes celles qui manquent : FACTURE (accord de Jacques)

LE POINT DE GRAMMAIRE CENTRAL : RACONTER AU PASSE.
  - en allemand le Perfekt, haben ou sein + le participe a la fin (Anna ist nach Malaga geflogen ; Anna hat ein Eis
    gegessen). L'auxiliaire et le participe ne sont pas ecrits ici : ils sont LUS dans la phrase « perfekt » du
    corpus (verbe.json), et l'auxiliaire se conjugue par personne (bin, bist, ist / habe, hast, hat). Le temps
    qu'il fait se dit au Praeteritum pour sein (es war warm), comme le font les Allemands ;
  - en espagnol le preterito indefinido, pris tel quel dans le corpus (verbos.json, cle « preterito ») : fui, viajo,
    hizo, comimos.
  Les traductions (fr, en, pt) se fabriquent de la meme facon : le passe compose francais (avoir ou etre, l'accord
  du participe avec etre), le preterit anglais, le preterito perfeito bresilien (les formes regulieres calculees,
  fazer et ir ecrits).

TROIS VOYAGES, on suit des personnes et l'ordre de ce qu'elles ont fait (une frise par voyage) :
  - Anna a Malaga, en octobre (elle part de l'aeroport de Berlin, la scene « flughafen » ; la plage, la scene
    « strand », ecrite pour Anna sur la cote espagnole) ;
  - Mark a Hambourg, un week-end de pluie (l'hotel, la scene « hotel », est un hotel de Hambourg) ;
  - la famille d'Anna (Jan, Katrin, Ben, Mia) a la mer Baltique, l'ete dernier, dans un appartement de vacances.
  Anna n'a ni compagnon ni enfant : elle voyage seule. La chambre d'Anna est celle de « La journee » (lit blanc,
  decision du 4 nov.), celle de Mark celle de « La journee » (lit en bois clair, une chaise couverte de vetements).
Les reservations et la reception se DESSINENT (une confirmation de reservation en HTML, la regle des documents) ;
le temps qu'il fait renvoie au theme de la meteo sans le refaire : il ne se dit ici qu'au passe.
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/vacances/img/.
"""
import hashlib, io, json, os, re, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype")
SORTIE = os.path.join(PROTO, "vacances")
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "vacances", "img")
EDIT, PRIX = "fal-ai/nano-banana-pro/edit", 0.15
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
JOURNEE = os.path.join(os.path.expanduser("~"), ".wortando", "journee", "img")
SOURCES = {"Mark": PRINCIPAL + "/personnages/Mark.png", "Anna": FAMILLE + "/Anna-quotidien.png",
           "Jan": FAMILLE + "/Jan.png", "Katrin": FAMILLE + "/Katrin.png", "Ben": FAMILLE + "/Ben.png", "Mia": FAMILLE + "/Mia.png",
           # les lieux et les tenues deja photographies (video/LIEUX.md)
           "chambre-anna": JOURNEE + "/anna-1.png",              # la chambre qui fait foi (lit blanc, decision du 4 nov.)
           "chambre-mark": JOURNEE + "/mark-1.png",              # sa chambre de la colocation
           "aeroport": PROTO + "/flughafen.webp",                # Anna, son manteau bleu marine, sa valise rouge fonce
           "plage": PROTO + "/strand.webp",                      # Anna a la plage, en Espagne
           "hotel": PROTO + "/hotel.webp"}                       # Mark a Hambourg, manteau de laine gris
SEXE = {"Anna": "f", "Mark": "m", "Jan": "m", "Katrin": "f", "Ben": "m", "Mia": "f"}

# ---------------------------------------------------------------------------------------------------------------
# LES SUJETS. n : l'indice des formes (2 : il, elle ; 4 : ils) ; g : le genre, pour l'accord francais et les
# possessifs (« seinen Koffer », « sa valise ») ; pron : le pronom allemand qui le remplace (« Sie ist ... geflogen »).
SUJETS = {
    "Anna":    {"de": "Anna", "es": "Anna", "fr": "Anna", "en": "Anna", "pt": "Anna", "pron": "sie", "n": 2, "g": "f", "qui": ["Anna"]},
    "Mark":    {"de": "Mark", "es": "Mark", "fr": "Mark", "en": "Mark", "pt": "Mark", "pron": "er", "n": 2, "g": "m", "qui": ["Mark"]},
    "familia": {"de": "Die Familie", "es": "La familia", "fr": "La famille", "en": "The family", "pt": "A família", "pron": "sie", "n": 2, "g": "f", "qui": ["Jan", "Katrin", "Ben", "Mia"]},
    "BenMia":  {"de": "Ben und Mia", "es": "Ben y Mia", "fr": "Ben et Mia", "en": "Ben and Mia", "pt": "Ben e Mia", "pron": "sie", "n": 4, "g": "pl", "qui": ["Ben", "Mia"]},
}
# les personnes des exercices de conjugaison, dans l'ordre des formes : je, tu, il/elle, nous, ils
PERSONNES = {"de": ["Ich", "Du", None, "Wir", None], "es": ["Yo", "Tú", None, "Nosotros", None],
             "fr": ["Je", "Tu", None, "Nous", None], "en": ["I", "You", None, "We", None], "pt": ["Eu", "Você", None, "Nós", None]}
HABEN = ["habe", "hast", "hat", "haben", "haben"]
SEIN = ["bin", "bist", "ist", "sind", "sind"]
# l'indice du corpus espagnol (six formes, vosotros compris) pour nos cinq personnes
ES_IDX = [0, 1, 2, 3, 5]

# ---------------------------------------------------------------------------------------------------------------
# LES TROIS VOYAGES : un titre, le moment (en tete de phrase en allemand : « Im Oktober ist Anna ... geflogen », le
# verbe en deuxieme position), et les etapes dans l'ordre.
VOYAGES = {
    "anna":    {"titre": {"de": "Annas Urlaub in Málaga", "es": "Las vacaciones de Anna en Málaga", "fr": "Les vacances d'Anna à Málaga", "en": "Anna's holiday in Málaga", "pt": "As férias da Anna em Málaga"},
                "quand": {"de": "Im Oktober", "es": "En octubre", "fr": "En octobre", "en": "In October", "pt": "Em outubro"}},
    "mark":    {"titre": {"de": "Marks Wochenende in Hamburg", "es": "El fin de semana de Mark en Hamburgo", "fr": "Le week-end de Mark à Hambourg", "en": "Mark's weekend in Hamburg", "pt": "O fim de semana do Mark em Hamburgo"},
                "quand": {"de": "Letztes Wochenende", "es": "El fin de semana pasado", "fr": "Le week-end dernier", "en": "Last weekend", "pt": "No fim de semana passado"}},
    "familia": {"titre": {"de": "Die Familie an der Ostsee", "es": "La familia en el mar Báltico", "fr": "La famille à la mer Baltique", "en": "The family at the Baltic Sea", "pt": "A família no mar Báltico"},
                "quand": {"de": "Letzten Sommer", "es": "El verano pasado", "fr": "L'été dernier", "en": "Last summer", "pt": "No verão passado"}},
}

# LES ETAPES. Une etape : sa cle (= son image), le voyage, le sujet, et pour chaque langue :
#   de : (infinitif du CORPUS, ce qui va entre l'auxiliaire et le participe) -- {P:m} un possessif a l'accusatif ;
#   es : (infinitif du CORPUS, ce qui suit le verbe) ; latam : ce qui change en Amerique latine ;
#   fr : (auxiliaire « avoir » / « etre », participe, ce qui suit, reflechi) ; en : (preterit, ce qui suit) ;
#   pt : (infinitif portugais, ce qui suit).
# groupe : deux etapes du meme groupe se ressemblent (manger, partir...) et ne sont jamais leurres l'une de l'autre.
# meteo : les faits du temps vrais sur l'image, et les douteux (ni vrais ni faux : jamais proposes).
# aux : False quand l'auxiliaire n'est pas tranche (schwimmen : « ist » au nord, « hat » au sud) -- pas de question
# sur haben / sein pour lui.
ETAPES = [
    {"cle": "anna-koffer", "voyage": "anna", "sujet": "Anna", "groupe": "valise",
     "de": ("packen", "{P:m} Koffer"), "es": ("hacer", "la maleta"),
     "fr": ("avoir", "fait", "{P:f} valise"), "en": ("packed", "{P} suitcase"), "pt": ("fazer", "a mala")},
    {"cle": "anna-flughafen", "voyage": "anna", "sujet": "Anna", "groupe": "depart",
     "de": ("fahren", "zum Flughafen"), "es": ("ir", "al aeropuerto"),
     "fr": ("etre", "allé", "à l'aéroport"), "en": ("went", "to the airport"), "pt": ("ir", "ao aeroporto")},
    {"cle": "anna-flug", "voyage": "anna", "sujet": "Anna", "groupe": "depart",
     "de": ("fliegen", "nach Málaga"), "es": ("volar", "a Málaga"),
     "fr": ("avoir", "pris", "l'avion pour Málaga"), "en": ("flew", "to Málaga"), "pt": ("voar", "para Málaga")},
    {"cle": "anna-meer", "voyage": "anna", "sujet": "Anna", "groupe": "eau", "aux": False,
     "de": ("schwimmen", "im Meer"), "es": ("nadar", "en el mar"),
     "fr": ("avoir", "nagé", "dans la mer"), "en": ("swam", "in the sea"), "pt": ("nadar", "no mar"),
     "meteo": {"vrais": ["sonne", "warm"], "douteux": []}},
    {"cle": "anna-eis", "voyage": "anna", "sujet": "Anna", "groupe": "manger",
     "de": ("essen", "am Strand ein Eis"), "es": ("comer", "un helado en la playa"),
     "fr": ("avoir", "mangé", "une glace sur la plage"), "en": ("ate", "an ice cream on the beach"), "pt": ("comer", "um sorvete na praia"),
     "meteo": {"vrais": ["sonne", "warm"], "douteux": []}},
    {"cle": "anna-altstadt", "voyage": "anna", "sujet": "Anna", "groupe": "visite",
     "de": ("besichtigen", "die Altstadt"), "es": ("visitar", "el casco antiguo"),
     "fr": ("avoir", "visité", "la vieille ville"), "en": ("visited", "the old town"), "pt": ("visitar", "o centro histórico"),
     "meteo": {"vrais": ["sonne", "warm"], "douteux": []}},
    {"cle": "anna-souvenirs", "voyage": "anna", "sujet": "Anna", "groupe": "achat",
     "de": ("kaufen", "Souvenirs"), "es": ("comprar", "recuerdos"),
     "fr": ("avoir", "acheté", "des souvenirs"), "en": ("bought", "souvenirs"), "pt": ("comprar", "lembranças"),
     "meteo": {"vrais": ["sonne"], "douteux": ["warm"]}},

    {"cle": "mark-rucksack", "voyage": "mark", "sujet": "Mark", "groupe": "valise",
     "de": ("packen", "{P:m} Rucksack"), "es": ("hacer", "la mochila"),
     "fr": ("avoir", "fait", "{P:m} sac à dos"), "en": ("packed", "{P} backpack"), "pt": ("arrumar", "a mochila")},
    {"cle": "mark-zug", "voyage": "mark", "sujet": "Mark", "groupe": "depart",
     "de": ("fahren", "mit dem Zug nach Hamburg"), "es": ("ir", "a Hamburgo en tren"),
     "fr": ("etre", "allé", "à Hambourg en train"), "en": ("took", "the train to Hamburg"), "pt": ("ir", "de trem para Hamburgo"),
     "meteo": {"vrais": ["regen"], "douteux": ["kalt"]}},
    {"cle": "mark-hotel", "voyage": "mark", "sujet": "Mark", "groupe": "arrivee",
     "de": ("ankommen", "im Hotel"), "es": ("llegar", "al hotel"),
     "fr": ("etre", "arrivé", "à l'hôtel"), "en": ("arrived", "at the hotel"), "pt": ("chegar", "ao hotel")},
    {"cle": "mark-hafen", "voyage": "mark", "sujet": "Mark", "groupe": "visite",
     "de": ("machen", "eine Rundfahrt durch den Hafen"), "es": ("hacer", "una excursión en barco por el puerto"),
     "fr": ("avoir", "fait", "un tour du port en bateau"), "en": ("took", "a boat tour of the harbor"), "pt": ("fazer", "um passeio de barco pelo porto"),
     "meteo": {"vrais": ["regen"], "douteux": ["kalt"]}},
    {"cle": "mark-fisch", "voyage": "mark", "sujet": "Mark", "groupe": "manger",
     "de": ("essen", "ein Fischbrötchen"), "es": ("comer", "un bocadillo de pescado"), "latam": {"es": "un sándwich de pescado"},
     "fr": ("avoir", "mangé", "un sandwich au poisson"), "en": ("ate", "a fish sandwich"), "pt": ("comer", "um sanduíche de peixe"),
     "meteo": {"vrais": ["regen"], "douteux": ["kalt"]}},
    {"cle": "mark-museum", "voyage": "mark", "sujet": "Mark", "groupe": "visite",
     "de": ("gehen", "ins Museum"), "es": ("ir", "al museo"),
     "fr": ("etre", "allé", "au musée"), "en": ("went", "to the museum"), "pt": ("ir", "ao museu")},
    {"cle": "mark-postkarte", "voyage": "mark", "sujet": "Mark", "groupe": "ecrire",
     "de": ("schreiben", "eine Postkarte"), "es": ("escribir", "una postal"),
     "fr": ("avoir", "écrit", "une carte postale"), "en": ("wrote", "a postcard"), "pt": ("escrever", "um cartão-postal")},

    {"cle": "familia-auto", "voyage": "familia", "sujet": "familia", "groupe": "depart",
     "de": ("fahren", "mit dem Auto an die Ostsee"), "es": ("ir", "al mar Báltico en coche"), "latam": {"es": "al mar Báltico en carro"},
     "fr": ("etre", "allé", "à la mer Baltique en voiture"), "en": ("drove", "to the Baltic Sea"), "pt": ("ir", "de carro para o mar Báltico")},
    {"cle": "familia-wohnung", "voyage": "familia", "sujet": "familia", "groupe": "arrivee",
     "de": ("mieten", "eine Ferienwohnung"), "es": ("alquilar", "un apartamento de vacaciones"),
     "fr": ("avoir", "loué", "un appartement de vacances"), "en": ("rented", "a vacation apartment"), "pt": ("alugar", "um apartamento de férias")},
    {"cle": "familia-sandburg", "voyage": "familia", "sujet": "BenMia", "groupe": "jeu",
     "de": ("bauen", "eine Sandburg"), "es": ("hacer", "un castillo de arena"),
     "fr": ("avoir", "fait", "un château de sable"), "en": ("built", "a sandcastle"), "pt": ("fazer", "um castelo de areia"),
     "meteo": {"vrais": ["sonne"], "douteux": ["warm"]}},
    {"cle": "familia-baden", "voyage": "familia", "sujet": "BenMia", "groupe": "eau",
     "de": ("baden", "im Meer"), "es": ("bañarse", "en el mar"),
     "fr": ("etre", "baigné", "dans la mer", True), "en": ("swam", "in the sea"), "pt": ("tomar", "banho de mar"),
     "meteo": {"vrais": ["sonne"], "douteux": ["warm"]}},
    {"cle": "familia-rad", "voyage": "familia", "sujet": "familia", "groupe": "sortie",
     "de": ("fahren", "am Strand entlang Fahrrad"), "es": ("montar", "en bicicleta a lo largo de la playa"),
     "fr": ("avoir", "fait", "du vélo le long de la plage"), "en": ("rode", "bikes along the beach"), "pt": ("andar", "de bicicleta pela praia"),
     "meteo": {"vrais": ["sonne"], "douteux": ["warm"]}},
    {"cle": "familia-karten", "voyage": "familia", "sujet": "familia", "groupe": "jeu",
     "de": ("spielen", "Karten"), "es": ("jugar", "a las cartas"),
     "fr": ("avoir", "joué", "aux cartes"), "en": ("played", "cards"), "pt": ("jogar", "cartas"),
     "meteo": {"vrais": ["regen"], "douteux": ["kalt"]}},
]

# LE TEMPS QU'IL FAISAIT (au passe seulement ; le theme de la meteo a le reste). Chaque fait : sa phrase et le mot
# du corpus qu'il fait avancer. Le faux d'une question n'est jamais un fait vrai ni douteux de l'image.
METEO = {
    "sonne": {"de": "Die Sonne hat geschienen.", "es": "Hizo sol.", "mot_de": {"mot": "scheinen", "cat": "verbe"}, "mot_es": {"mot": "sol", "genre": "el"},
              "fr": "Il y avait du soleil.", "en": "It was sunny.", "pt": "Fez sol."},
    "warm":  {"de": "Es war warm.", "es": "Hizo calor.", "mot_de": {"mot": "warm", "cat": "adjectif"}, "mot_es": {"mot": "calor", "genre": "el"},
              "fr": "Il faisait chaud.", "en": "It was warm.", "pt": "Fez calor."},
    "regen": {"de": "Es hat geregnet.", "es": "Llovió.", "mot_de": {"mot": "regnen", "cat": "verbe"}, "mot_es": {"mot": "llover", "cat": "verbe"},
              "fr": "Il a plu.", "en": "It rained.", "pt": "Choveu."},
    "kalt":  {"de": "Es war kalt.", "es": "Hizo frío.", "mot_de": {"mot": "kalt", "cat": "adjectif"}, "mot_es": {"mot": "frío", "cat": "adjectif"},
              "fr": "Il faisait froid.", "en": "It was cold.", "pt": "Fez frio."},
    "schnee": {"de": "Es hat geschneit.", "es": "Nevó.", "mot_de": {"mot": "schneien", "cat": "verbe"}, "mot_es": {"mot": "nevar", "cat": "verbe"},
               "fr": "Il a neigé.", "en": "It snowed.", "pt": "Nevou."},
}

# LES DEUX VALISES : ce qui est VISIBLE sur le lit (et seulement ca : une chose rangee dans la valise ne se voit pas,
# donc rien ne se demande au passe « qu'a-t-elle emporte »). de / es : (genre, mot du corpus, pluriel affiche) ;
# Tous au corpus depuis le 6 nov. 2026 (die Sonnencreme, die Sonnenbrille, la crema solar : decision fe14b7d).
OBJETS = {
    "pass":        {"de": ("der", "Pass"), "es": ("el", "pasaporte"), "fr": "le passeport", "en": "the passport", "pt": "o passaporte"},
    "badeanzug":   {"de": ("der", "Badeanzug"), "es": ("el", "bañador"), "fr": "le maillot de bain", "en": "the swimsuit", "pt": "o maiô"},
    "hut":         {"de": ("der", "Hut"), "es": ("el", "sombrero"), "fr": "le chapeau", "en": "the hat", "pt": "o chapéu"},
    "sandalen":    {"de": ("die", "Sandale", "Sandalen"), "es": ("la", "sandalia", "sandalias"), "fr": "les sandales", "en": "the sandals", "pt": "as sandálias"},
    "kamera":      {"de": ("die", "Kamera"), "es": ("la", "cámara"), "fr": "l'appareil photo", "en": "the camera", "pt": "a câmera"},
    "sonnenbrille": {"de": ("die", "Sonnenbrille"), "es": ("las", "gafas de sol"), "fr": "les lunettes de soleil", "en": "the sunglasses", "pt": "os óculos de sol"},
    "sonnencreme": {"de": ("die", "Sonnencreme"), "es": ("la", "crema solar"), "fr": "la crème solaire", "en": "the sunscreen", "pt": "o protetor solar"},
    "regenschirm": {"de": ("der", "Regenschirm"), "es": ("el", "paraguas"), "fr": "le parapluie", "en": "the umbrella", "pt": "o guarda-chuva"},
    "pullover":    {"de": ("der", "Pullover"), "es": ("el", "jersey"), "latam": "suéter", "fr": "le pull", "en": "the sweater", "pt": "o suéter"},
    "ladegeraet":  {"de": ("das", "Ladegerät"), "es": ("el", "cargador"), "fr": "le chargeur", "en": "the charger", "pt": "o carregador"},
    "stadtplan":   {"de": ("der", "Stadtplan"), "es": ("el", "mapa"), "fr": "le plan de la ville", "en": "the city map", "pt": "o mapa"},
}
VALISES = {
    "anna-koffer":   {"qui": "Anna", "vus": ["pass", "badeanzug", "hut", "sandalen", "kamera", "sonnenbrille", "sonnencreme"]},
    "mark-rucksack": {"qui": "Mark", "vus": ["regenschirm", "pullover", "ladegeraet", "stadtplan"]},
}

# LES RESERVATIONS (dessinees, jamais dans une image) : qui, l'hotel, la chambre, les nuits, le petit-dejeuner.
# Celles d'Anna et de Mark sont celles de leurs voyages ; les autres, des membres de la famille d'Anna et ses amis
# (visuel/familia, visuel/logement), pour qu'une question ne se devine pas au nom.
RESERVATIONS = [
    {"qui": "Mark",   "hotel": "Hotel am Hafen", "ville": {"de": "Hamburg", "es": "Hamburgo"}, "chambre": "einzel", "nuits": 2, "petitdej": True},
    {"qui": "Anna",   "hotel": "Hotel Mirador", "ville": {"de": "Málaga", "es": "Málaga"}, "chambre": "einzel", "nuits": 5, "petitdej": False},
    {"qui": "Lena",   "hotel": "Hotel Alpenblick", "ville": {"de": "München", "es": "Múnich"}, "chambre": "doppel", "nuits": 3, "petitdej": True},
    {"qui": "Felix",  "hotel": "Pension Sonne", "ville": {"de": "Wien", "es": "Viena"}, "chambre": "doppel", "nuits": 2, "petitdej": False},
    {"qui": "Katrin", "hotel": "Hotel Seeblick", "ville": {"de": "Rostock", "es": "Rostock"}, "chambre": "doppel", "nuits": 4, "petitdej": True},
    {"qui": "Jan",    "hotel": "Hotel Central", "ville": {"de": "Köln", "es": "Colonia"}, "chambre": "einzel", "nuits": 1, "petitdej": True},
    {"qui": "Sophie", "hotel": "Hotel Marina", "ville": {"de": "Barcelona", "es": "Barcelona"}, "chambre": "doppel", "nuits": 6, "petitdej": False},
    {"qui": "Peter",  "hotel": "Hotel Krone", "ville": {"de": "Dresden", "es": "Dresde"}, "chambre": "einzel", "nuits": 3, "petitdej": False},
]
NOMBRES = {"de": ["", "eine", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht"],
           "es": ["", "una", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho"]}
# les mots d'ordre (frise) : ceux du corpus
LIENS = {"de": ["zuerst", "dann", "danach", "schließlich"], "es": ["primero", "después", "luego", "al final"]}

# LES MOTS QUI MANQUAIENT AU CORPUS : les six ajoutes le 6 nov. 2026 (« Oui, les 6 », decision fe14b7d) par
# ajouts/vacances.json et espanol/ajouts/vacances.json ; il n'en manque plus.
AJOUTS = {"de": [], "es": []}

# ---------------------------------------------------------------------------------------------------------------
# LE CORPUS
def lire(p):
    return json.load(io.open(os.path.join(RACINE, p), encoding="utf-8"))


def index_verbes(fichier):
    acc = {}
    def walk(o):
        if isinstance(o, dict):
            if "infinitif" in o: acc.setdefault(o["infinitif"], o)
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(lire(fichier))
    return acc


def index_noms(fichier):
    acc = {}
    for t in lire(fichier)["themes"]:
        for m in t["mots"]:
            acc.setdefault((m.get("genre"), m["mot"]), m)
    return acc


def index_mots(fichier):
    acc = {}
    def walk(o):
        if isinstance(o, dict):
            if "mot" in o: acc.setdefault(o["mot"], o)
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(lire(fichier))
    return acc


AUX_FORMES = {"bin": "sein", "bist": "sein", "ist": "sein", "sind": "sein", "seid": "sein",
              "habe": "haben", "hast": "haben", "hat": "haben", "haben": "haben", "habt": "haben"}


def perfekt(entree):
    """(auxiliaire, participe) LUS dans la phrase « perfekt » du corpus : « Wir sind nach Spanien geflogen. » ->
    (sein, geflogen). Le participe est le dernier mot de la proposition principale (avant la premiere virgule)."""
    mots = re.sub(r"[.!?]", "", entree["perfekt"].split(",")[0]).split()
    aux = next(AUX_FORMES[m] for m in mots if m in AUX_FORMES)
    return aux, mots[-1]


PREFIXES_INSEP = ("be", "ver", "er", "ent", "zer", "emp", "miss")
PREFIXES_SEP = ("an", "ein", "auf", "aus", "mit", "zurück", "ab", "zu", "vor", "nach", "weg")


def faux_participes(inf, pp):
    """Les participes FAUX qu'un apprenant fabrique, calcules depuis l'infinitif et le vrai participe : le faible
    pour un fort (gefliegt, geesst), le fort pour un faible (gekaufen), le ge- de trop (gebesichtigt, gereserviert),
    le ge- mal place (geankommen), l'infinitif apres ge-. Jamais le vrai."""
    out = []
    sep = next((p for p in PREFIXES_SEP if inf.startswith(p) and pp.startswith(p + "ge")), None)
    racine = inf[len(sep):] if sep else inf
    radical = racine[:-2] if racine.endswith("en") else racine[:-1]
    fort = pp.endswith("en")
    insep = racine.startswith(PREFIXES_INSEP) and not pp[len(sep or ""):].startswith("ge")
    ieren = inf.endswith("ieren")
    pre = sep or ""
    if fort:
        out.append(pre + ("" if insep else "ge") + radical + "t")          # gefliegt, angekommt
        out.append(pre + ("" if insep else "ge") + racine)                 # geessen -> « geessen » (l'infinitif)
    else:
        out.append(pre + ("" if (insep or ieren) else "ge") + radical + "en")   # gekaufen, gebauen
    if insep or ieren:
        out.append("ge" + pp)                                               # gebesichtigt, gereserviert
    if sep:
        out.append("ge" + sep + pp[len(sep) + 2:])                           # geankommen
    out.append(inf)                                                         # « ist nach Malaga fliegen »
    return [f for f in dict.fromkeys(out) if f != pp]


# LE PRETERITO PERFEITO BRESILIEN (la traduction portugaise) : les formes regulieres calculees ; fazer et ir ecrits.
PT_IRREG = {"fazer": ["fiz", "fez", "fez", "fizemos", "fizeram"], "ir": ["fui", "foi", "foi", "fomos", "foram"]}


def pt_preterito(inf):
    if inf in PT_IRREG:
        return PT_IRREG[inf]
    r, t = inf[:-2], inf[-2:]
    if t == "ar":
        eu = r + "ei"
        if r.endswith("c"): eu = r[:-1] + "quei"
        if r.endswith("g"): eu = r + "uei"
        return [eu, r + "ou", r + "ou", r + "amos", r + "aram"]
    if t == "er":
        return [r + "i", r + "eu", r + "eu", r + "emos", r + "eram"]
    return [r + "i", r + "iu", r + "iu", r + "imos", r + "iram"]


def verifier():
    """Chaque verbe est au corpus, avec son Perfekt (allemand) ou son preterito (espagnol) ; chaque objet et chaque
    fait du temps a son mot ; chaque etape a son image."""
    vde, ves = index_verbes("verbe.json"), index_verbes("espanol/datos/verbos.json")
    nde, nes = index_noms("themes.json"), index_noms("espanol/datos/temas.json")
    ade, aes = index_mots("adjectif.json"), index_mots("espanol/datos/adjetivos.json")
    fautes, absents = [], []
    for e in ETAPES:
        if e["de"][0] not in vde or not vde[e["de"][0]].get("perfekt"): fautes.append("de %s : %s sans Perfekt au corpus" % (e["cle"], e["de"][0]))
        if e["es"][0] not in ves or not ves[e["es"][0]].get("preterito"): fautes.append("es %s : %s sans preterito au corpus" % (e["cle"], e["es"][0]))
        if e["cle"] not in IMAGES and e["cle"] not in REPRISES: fautes.append("image manquante : " + e["cle"])
    for k, o in OBJETS.items():
        if (o["de"][0], o["de"][1]) not in nde: absents.append("de " + o["de"][0] + " " + o["de"][1])
        if (o["es"][0], o["es"][1]) not in nes: absents.append("es " + o["es"][0] + " " + o["es"][1])
    for k, f in METEO.items():
        for app, m in (("de", f["mot_de"]), ("es", f["mot_es"])):
            ok = (m["mot"] in (vde if app == "de" else ves)) if m.get("cat") == "verbe" else \
                 (m["mot"] in (ade if app == "de" else aes)) if m.get("cat") == "adjectif" else ((m.get("genre"), m["mot"]) in (nde if app == "de" else nes))
            if not ok: absents.append(app + " " + m["mot"])
    for app, noms in (("de", [("das", "Doppelzimmer"), ("das", "Einzelzimmer"), ("die", "Nacht"), ("das", "Frühstück")]),
                      ("es", [("la", "habitación"), ("la", "habitación doble"), ("la", "habitación individual"), ("la", "noche"), ("el", "desayuno"), ("la", "reserva")])):
        for g, m in noms:
            if (g, m) not in (nde if app == "de" else nes): fautes.append("%s %s %s absent" % (app, g, m))
    return fautes, sorted(set(absents))


def construire():
    vde, ves = index_verbes("verbe.json"), index_verbes("espanol/datos/verbos.json")
    verbes = {"de": {}, "es": {}}
    for e in ETAPES:
        inf = e["de"][0]
        if inf not in verbes["de"]:
            aux, pp = perfekt(vde[inf])
            verbes["de"][inf] = {"aux": aux, "pp": pp, "faux": faux_participes(inf, pp), "praesens": vde[inf]["praesens"]["er_sie_es"]}
        inf = e["es"][0]
        if inf not in verbes["es"]:
            v = ves[inf]
            pret = [v["preterito"][i] for i in ES_IDX]
            pres = [v["praesens"][c] for c in ("ich", "du", "er_sie_es", "wir", "sie_Sie")]
            verbes["es"][inf] = {"pret": pret, "pres": pres}
    etapes = []
    for e in ETAPES:
        x = dict(e)
        x["pt"] = (e["pt"][0], e["pt"][1], pt_preterito(e["pt"][0]))
        etapes.append(x)
    return {"_lisez_moi": "FICHIER DERIVE de visuel/vacances/vacances.py (python visuel/vacances/vacances.py --json) : ne pas corriger ici.",
            "sujets": SUJETS, "personnes": PERSONNES, "haben": HABEN, "sein": SEIN, "voyages": VOYAGES, "etapes": etapes,
            "verbes": verbes, "meteo": METEO, "objets": OBJETS, "valises": VALISES, "reservations": RESERVATIONS,
            "nombres": NOMBRES, "liens": LIENS, "sexe": SEXE}


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def phrase_de(d, e, k=None, S=None):
    """« Anna ist nach Málaga geflogen. » ; k, S : une autre personne (« Ich bin nach Málaga geflogen. »)."""
    inf, c = e["de"]
    v = d["verbes"]["de"][inf]
    s = d["sujets"][e["sujet"]]
    k = s["n"] if k is None else k
    aux = (SEIN if v["aux"] == "sein" else HABEN)[k]
    return " ".join(w for w in [S or s["de"], aux, poss_de(c, k, s["g"]), v["pp"]] if w) + "."


def poss_de(c, k, g):
    def rempl(m):
        genre = m.group(1)
        base = ["mein", "dein", "sein" if g == "m" else "ihr", "unser", "ihr"][k]
        return base + {"m": "en", "f": "e", "n": "", "pl": "e"}[genre]
    return re.sub(r"\{P:(m|f|n|pl)\}", rempl, c)


def phrase_es(d, e, latam=False):
    inf, c = e["es"]
    if latam and e.get("latam", {}).get("es"):
        c = e["latam"]["es"]
    s = d["sujets"][e["sujet"]]
    return " ".join([s["es"], d["verbes"]["es"][inf]["pret"][s["n"]], c]) + "."


def ecrire_json():
    d = construire()
    dec = {"de": {}, "es": {}, "latam": {}}
    for e in ETAPES:
        for langue, t in (("de", phrase_de(d, e)), ("es", phrase_es(d, e)), ("latam", phrase_es(d, e, True))):
            dec[langue][e["cle"]] = {"texte": t, "son": identifiant(t)}
    d["decouverte"] = dec
    os.makedirs(SORTIE, exist_ok=True)
    io.open(os.path.join(SORTIE, "vacances.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    return d


def ecrire_gloses():
    """La traduction des mots du theme, tiree du CORPUS (relu), pour toutes les langues d'interface : la ligne sous la
    reponse dans les langues ou la page ne traduit pas la phrase entiere, et le mot CHOISI quand il est faux.
    Comme journee/gloses.json. Fichier DERIVE."""
    LDE = {"fr": "traduction", "en": "traduction_en", "tr": "traduction_tr", "uk": "traduction_uk", "fa": "traduction_fa",
           "ar": "traduction_ar", "pt": "traduction_pt", "pl": "traduction_pl", "ru": "traduction_ru"}
    LES = {"fr": "traduction", "en": "traduction_en", "pt": "traduction_pt", "ar": "traduction_ar", "de": "traduction_de"}
    out = {"de": {}, "es": {}}
    for app, champs in (("de", LDE), ("es", LES)):
        verbes = index_verbes("verbe.json" if app == "de" else "espanol/datos/verbos.json")
        noms = index_noms("themes.json" if app == "de" else "espanol/datos/temas.json")
        adj = index_mots("adjectif.json" if app == "de" else "espanol/datos/adjetivos.json")
        adv = index_mots("adverbe.json" if app == "de" else "espanol/datos/adverbios.json")
        def poser(cle, entree):
            if entree: out[app][cle] = {l: entree[c] for l, c in champs.items() if entree.get(c)}
        for e in ETAPES:
            poser(e[app][0], verbes.get(e[app][0]))
        for o in OBJETS.values():
            g, m = o[app][0], o[app][1]
            poser(g + " " + m, noms.get((g, m)))
        for f in METEO.values():
            m = f["mot_" + app]
            if m.get("cat") == "verbe": poser(m["mot"], verbes.get(m["mot"]))
            elif m.get("cat") == "adjectif": poser(m["mot"], adj.get(m["mot"]))
            else: poser(m["genre"] + " " + m["mot"], noms.get((m["genre"], m["mot"])))
        for g, m in ([("das", "Doppelzimmer"), ("das", "Einzelzimmer"), ("die", "Nacht"), ("das", "Frühstück"), ("das", "Hotel")] if app == "de"
                     else [("la", "habitación"), ("la", "habitación doble"), ("la", "habitación individual"), ("la", "noche"), ("el", "desayuno"), ("la", "reserva"), ("el", "hotel")]):
            poser(g + " " + m, noms.get((g, m)))
        for v in (["reservieren", "buchen"] if app == "de" else ["reservar"]):
            poser(v, verbes.get(v))
        for l in LIENS[app]:
            poser(l, adv.get(l))
    io.open(os.path.join(SORTIE, "gloses.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n")


def textes_a_dire(langue):
    """Pour les inventaires des voix : les phrases de la decouverte (de, es, latam)."""
    d = json.load(io.open(os.path.join(SORTIE, "vacances.json"), encoding="utf-8"))
    return [v["texte"] for v in d["decouverte"][langue].values()]


# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES. REPRISES : trois images des scenes, deja publiees, recadrees en 4:3 autour de la personne (gratuit) --
# (fichier, haut du cadre en pixels sur l'original 1536 x 2752). IMAGES : les autres, par RETOUCHE (les visages de
# reference, le lieu ou la tenue d'une image deja faite), jamais une description seule.
REPRISES = {"anna-flughafen": ("flughafen.webp", 1060), "anna-eis": ("strand.webp", 1180), "mark-hotel": ("hotel.webp", 820)}
PLANCHE = ["anna-koffer", "anna-altstadt", "mark-zug", "mark-hafen", "familia-wohnung", "familia-sandburg"]
STYLE = (" A photorealistic photograph of a real moment of a trip, natural colours, natural light, no text, no letters, "
         "no numbers, no signs, no logos, no captions anywhere. The people are clearly visible, their faces and gestures "
         "easy to read, and they look happy and relaxed. ")
MEME = ("The same people as in the reference pictures: exactly the same faces, ages, hair, skin and bodies. ")
# (personnes, references de lieu ou de tenue, la scene) -- les references de lieu passent APRES les visages
IMAGES = {
    # Anna, son voyage a Malaga en octobre. Sa valise : la petite valise a roulettes ROUGE FONCE de l'aeroport.
    "anna-koffer": (["Anna"], ["chambre-anna", "aeroport"],
        "The same bedroom as in the second reference picture (white bed with a light-grey duvet, wooden bedside table "
        "with its small lamp, wooden wardrobe), in daylight. Anna, in a light-grey sweater and jeans, packs her small "
        "dark-red suitcase on wheels (the suitcase of the third reference picture), which lies open on the bed. Next to "
        "it, laid out neatly on the duvet with space between them, each object clearly visible: a dark-red passport, a "
        "pair of sunglasses, a white tube of sun cream without any print, a light-blue one-piece swimsuit, a straw sun "
        "hat, a pair of brown leather sandals and a small black camera. She holds the swimsuit, about to put it in."),
    "anna-flug": (["Anna"], ["aeroport"],
        "Inside a passenger plane, a window seat: Anna, in the light-grey sweater of the reference picture (no coat), "
        "looks out of the oval window and smiles; through the window, far below, a sunny blue sea and a Spanish coast "
        "with white houses. Her seat belt is fastened. Only Anna is in the row."),
    "anna-meer": (["Anna"], ["plage"],
        "On the same Spanish beach as in the second reference picture, on a sunny day: Anna, in the light-blue "
        "one-piece swimsuit of that picture, swims in the calm turquoise sea, her head and shoulders above the water, "
        "her hair tied back and wet, laughing; the sandy beach and the rocks behind her."),
    "anna-altstadt": (["Anna"], ["plage"],
        "In the old town of Málaga on a sunny October day: Anna, in a light summer dress, sandals and a straw sun hat, "
        "a small bag on her shoulder, walks across a sunny square in front of the great cathedral of Málaga (pale stone, "
        "tall arched doors), looking up at it, impressed; orange trees and other tourists far behind her."),
    "anna-souvenirs": (["Anna"], ["plage"],
        "At a small souvenir stall in a sunny street of the old town of Málaga: Anna, in a light summer dress and a "
        "straw sun hat, holds up a painted ceramic plate with blue and yellow patterns and smiles; on the stall, more "
        "colourful painted ceramic plates, small bowls and fans, without any writing; the smiling stall keeper, an "
        "elderly man, stands behind it."),
    # Mark, un week-end de pluie a Hambourg : le manteau de laine gris de l'hotel, un pull bleu fonce, un jean.
    "mark-rucksack": (["Mark"], ["chambre-mark", "hotel"],
        "The same bedroom as in the second reference picture (light wooden bed, white walls, a chair covered with "
        "clothes), in daylight. Mark, in a T-shirt and jeans, packs his black backpack (the one of the third reference picture) that lies open on the bed. Next "
        "to it, laid out on the bed with space between them, each object clearly visible: a folded black umbrella, a "
        "folded grey knitted pullover, a white phone charger with its cable, and a folded paper city map showing only "
        "coloured streets and a blue river, without any letters. He puts the pullover into the backpack."),
    "mark-zug": (["Mark"], ["hotel"],
        "Inside a modern German long-distance train on a rainy day: Mark, in the grey wool coat and the dark-blue sweater "
        "of the second reference picture, sits at a window seat with his black backpack on the seat beside him; "
        "raindrops run down the window and green fields pass by outside. He looks out of the window, relaxed, a paper "
        "cup of coffee on the small table."),
    "mark-hafen": (["Mark"], ["hotel"],
        "On the open deck of a small harbour tour boat in the port of Hamburg on a rainy day: Mark, in the grey wool "
        "coat of the second reference picture, holds a black umbrella and smiles at the view; behind him, big container "
        "ships, tall red-brick warehouses and huge harbour cranes in the grey rain. A few other passengers far behind."),
    "mark-fisch": (["Mark"], ["hotel"],
        "Under the awning of a small fish snack stand at the harbour of Hamburg, on a rainy day: Mark, in the grey wool "
        "coat of the second reference picture, takes a big bite of a fish sandwich (a crusty bread roll with a piece of "
        "pickled herring, onions and lettuce), enjoying it; rain falls behind him, the harbour water in the background."),
    "mark-museum": (["Mark"], ["hotel"],
        "In a quiet hall of a maritime museum in Hamburg: Mark, in the dark-blue sweater of the second reference "
        "picture, his grey coat over his arm, looks with interest at a large wooden model of an old sailing ship in a "
        "glass case; old ship paintings on the walls, no labels, no signs, no text anywhere."),
    "mark-postkarte": (["Mark"], ["hotel"],
        "In a cosy café in Hamburg, rain on the big window: Mark, in the dark-blue sweater of the second reference "
        "picture, sits at a small wooden table and writes on a picture postcard with a pen; the postcard shows the "
        "harbour of Hamburg; a cup of coffee next to it. We do not see any handwriting, only the pen on the card."),
    # La famille d'Anna (Jan, Katrin, Ben 7 ans, Mia 4 ans) a la mer Baltique, l'ete dernier
    "familia-auto": (["Jan", "Katrin", "Ben", "Mia"], [],
        "On a small sunny car park behind the dunes of the Baltic Sea, in summer: the family has just arrived by car. "
        "Jan opens the boot of their grey family car, full of bags and a beach bag; Katrin helps Mia (4) out of the car; "
        "Ben (7) points excitedly at the sea, visible over the dunes and the beach grass. Everybody wears light summer "
        "clothes. No number plate is readable."),
    "familia-wohnung": (["Jan", "Katrin", "Ben", "Mia"], [],
        "In front of the door of a small holiday flat in a white seaside house at the Baltic Sea, in summer: Katrin "
        "unlocks the blue front door with a key, Jan carries two bags, Ben (7) and Mia (4) wait, excited, with their "
        "small backpacks; pink roses climb along the white wall. Light summer clothes, sunny afternoon."),
    "familia-sandburg": (["Ben", "Mia"], [],
        "On a wide sandy beach of the Baltic Sea on a sunny summer day, typical German wicker beach chairs (Strandkorb) "
        "in the background: Ben (7) and his little sister Mia (4), in T-shirts and shorts and sun hats, kneel in the "
        "sand and build a big sandcastle with towers, with a red bucket and a blue spade, proud and laughing."),
    "familia-baden": (["Ben", "Mia", "Jan"], [],
        "At the edge of the calm Baltic Sea on a sunny summer day: Ben (7) and Mia (4), in long-sleeved swim shirts and "
        "swim shorts, splash and play in the shallow water up to their knees, laughing; their father Jan stands in the "
        "water next to them, in swim trunks and a T-shirt, watching them. The wide sandy beach behind them."),
    "familia-rad": (["Jan", "Katrin", "Ben", "Mia"], [],
        "On a sunny summer day, the family rides bicycles on a flat path along the beach of the Baltic Sea, the dunes and "
        "the sea beside them: Jan in front, Ben (7) on his own small bike, Katrin behind with Mia (4) in a child seat on "
        "her bike; everybody wears a bicycle helmet and smiles."),
    "familia-karten": (["Jan", "Katrin", "Ben", "Mia"], ["familia-wohnung"],
        "Inside the cosy holiday flat (the white seaside house of the last reference picture), on a rainy afternoon: "
        "heavy rain runs down the window; the whole family sits around a wooden table and plays cards, Mia (4) on "
        "Katrin's lap, Ben (7) laughing as he puts down a card, Jan holding his cards. The cards have plain coloured "
        "backs and simple pictures, no letters and no numbers."),
}


def web():
    """Les webp de la page (960 x 720, 4:3) : les originaux fal, et les reprises recadrees depuis les scenes."""
    from PIL import Image
    manque = []
    for cle, (fichier, haut) in REPRISES.items():
        im = Image.open(os.path.join(PROTO, fichier)).convert("RGB")
        w, h = im.size
        ch = round(w * 3 / 4)
        haut = max(0, min(haut, h - ch))
        im.crop((0, haut, w, haut + ch)).resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, cle + ".webp"), "WEBP", quality=78, method=6)
    for cle in IMAGES:
        src = os.path.join(DOSSIER, cle + ".png")
        if not os.path.exists(src):
            manque.append(cle)
            continue
        im = Image.open(src).convert("RGB")
        w, h = im.size
        if abs(w * 3 - h * 4) > 8:
            ch = round(w * 3 / 4) if w * 3 < h * 4 else h
            cw = round(ch * 4 / 3)
            im = im.crop(((w - cw) // 2, (h - ch) // 2, (w + cw) // 2, (h + ch) // 2))
        im.resize((960, 720), Image.LANCZOS).save(os.path.join(SORTIE, cle + ".webp"), "WEBP", quality=78, method=6)
    print("  webp faits dans %s" % os.path.relpath(SORTIE, RACINE) + ("" if not manque else " ; MANQUENT : " + ", ".join(manque)))


def provisoire():
    """Des images PROVISOIRES pour construire la page sans depense : un aplat, les visages et le geste ecrit.
    Jamais committees : les vraies les remplacent."""
    from PIL import Image, ImageDraw, ImageFont
    visages = {p: os.path.join(PROTO, "familia" if p != "Mark" else "descripcion", p + "-visage.webp") for p in SEXE}
    try:
        police = ImageFont.truetype("arial.ttf", 46)
    except OSError:
        police = ImageFont.load_default()
    for cle, (qui, _, _) in IMAGES.items():
        if os.path.exists(os.path.join(DOSSIER, cle + ".png")):
            continue
        im = Image.new("RGB", (960, 720), (205, 222, 236))
        for k, p in enumerate(qui):
            try:
                im.paste(Image.open(visages[p]).convert("RGB").resize((200, 200)), (40 + k * 220, 120))
            except OSError:
                pass
        dr = ImageDraw.Draw(im)
        e = next(x for x in ETAPES if x["cle"] == cle)
        dr.text((40, 440), e["de"][0] + " / " + e["es"][0], fill=(232, 162, 58), font=police)
        dr.text((40, 510), "PROVISOIRE " + cle, fill=(200, 71, 58), font=police)
        im.save(os.path.join(SORTIE, cle + ".webp"), "WEBP", quality=70)
    print("  images provisoires dans %s (a ne pas committer)" % os.path.relpath(SORTIE, RACINE))


def references(cle):
    qui, lieux, _ = IMAGES[cle]
    refs = [SOURCES[p] for p in qui]
    for l in lieux:
        refs.append(os.path.join(DOSSIER, l + ".png") if l in IMAGES else SOURCES[l])
    return refs


def prompt(cle):
    qui, lieux, scene = IMAGES[cle]
    noms = ", ".join("%s (reference picture %d)" % (p, k + 1) for k, p in enumerate(qui))
    return MEME + "The people: " + noms + ". " + STYLE + "Scene: " + scene


def generer(noms, montrer):
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    os.makedirs(DOSSIER, exist_ok=True)
    a_faire = [n for n in noms if not os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if not montrer and not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = None if montrer else O.cle()
    depots = {}
    def deposer(chemin):
        if chemin not in depots:
            typ = "image/webp" if chemin.endswith(".webp") else "image/png"
            depots[chemin] = O.deposer(chemin, typ, cle)[0]
        return depots[chemin]
    for nom in a_faire:
        refs = references(nom)
        texte = prompt(nom)
        print("\n  %s  (%s)\n  %s" % (nom, ", ".join(os.path.basename(r) for r in refs), texte))
        if montrer:
            continue
        manquants = [r for r in refs if not os.path.exists(r)]
        if manquants:
            print("  ATTENTE : reference absente " + ", ".join(manquants))
            continue
        corps = {"prompt": texte, "image_urls": [deposer(r) for r in refs], "aspect_ratio": "4:3", "resolution": "2K",
                 "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
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
            "modele": EDIT, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": texte, "sources": refs, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


def main():
    fautes, absents = verifier()
    if fautes:
        sys.exit("  donnee fautive :\n  " + "\n  ".join(fautes))
    if absents:
        print("  absents du corpus (hors jeu dans l'app tant qu'ils n'y sont pas) : " + ", ".join(absents))
    d = ecrire_json()
    ecrire_gloses()
    if "--json" in sys.argv:
        for app in ("de",):
            for inf, v in d["verbes"]["de"].items():
                print("  %-12s %-5s %-14s faux : %s" % (inf, v["aux"], v["pp"], ", ".join(v["faux"])))
        return
    if "--provisoire" in sys.argv:
        return provisoire()
    if "--web" in sys.argv:
        return web()
    noms = PLANCHE if "--planche" in sys.argv else ([a for a in sys.argv[1:] if not a.startswith("--")] or list(IMAGES))
    inconnus = [n for n in noms if n not in IMAGES]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    generer(noms, "--montrer" in sys.argv)


if __name__ == "__main__":
    main()
