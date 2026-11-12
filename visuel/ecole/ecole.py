# -*- coding: utf-8 -*-
"""L'ecole et la garderie des enfants, theme illustre de la vague 4 (5 nov. 2026, « go » de Jacques sur la liste du
chef : le travail, l'ecole et la garderie, les fetes, les vacances). Sujet frequent du DTZ : inscrire un enfant, le mot
d'absence a l'enseignante, la reunion de parents, l'horaire, les vacances scolaires, les fournitures, aller chercher
l'enfant.

    python visuel/ecole/ecole.py --json             # ecole.json seul, gratuit
    python visuel/ecole/ecole.py --montrer          # les prompts seuls, gratuit
    python visuel/ecole/ecole.py --essai            # la planche d'essai (6 images, 0,90 $) -- ACCORD DE JACQUES
    python visuel/ecole/ecole.py klasse krank       # celles-la seulement (0,15 $ chacune)
    python visuel/ecole/ecole.py --refaire krank    # l'ancienne passe en <nom>-rate<k>.png

LES PERSONNES (scenes/personnages.json, visuel/familia/familia.json) : les enfants du theme sont Ben (7 ans, en 2e annee
de la Grundschule) et Mia (4 ans, a la Kita), les enfants de Jan et Katrin -- jamais Anna, qui n'a pas d'enfant. Anna,
leur tante, et Mark, ami de la famille, peuvent aller chercher Mia. Mark est canadien (Montreal), il n'est PAS allemand.
Personnes neuves, sans nom de famille : Frau Weber, l'enseignante de Ben ; Frau Krueger, l'educatrice de Mia. La famille
n'a pas de nom de famille dans l'histoire : Katrin signe « Katrin (Bens Mutter) ».

L'ANGLE (regle 2 : pas de scene refaite). La scene « Klassenzimmer » est une salle de cours d'adultes (la VHS) ; ici,
ce sont les PARENTS face a l'ecole : amener et aller chercher, inscrire, ecrire a l'enseignante, lire l'horaire, la liste
des fournitures, le calendrier des vacances, l'invitation a la reunion de parents. Les papiers sont DESSINES en HTML par
la page (aucun texte dans les images), comme dans « Les demarches ».

LA GRAMMAIRE : en allemand Wohin? + accusatif / Wo? + datif (in die Kita, in der Schule, von der Kita), les verbes
separables (Mark holt Mia ab, Katrin meldet Mia an, Katrin ruft in der Schule an), les pluriels de la liste (vier Hefte) ;
en espagnol ir a / estar en, la contraction al, la « a » personnelle (Mark recoge a Mia), les pluriels ; en portugais
(lot P4, 12 nov. 2026, Lisbonne, Portugal et Bresil : PT_... plus bas) ir a / estar em et leurs contractions (à escola, ao
jardim de infância, na escola, no jardim de infância), ir buscar / buscar, l'accord um / uma, dois / duas.

LES PHRASES SONT FABRIQUEES par la page (ecole.html) a partir de ces tables, jamais ecrites une a une. Un leurre n'est
jamais une reponse possible : chaque action dit les verbes qui iraient aussi (aussi_v), chaque objet les objets qu'on
pourrait confondre sur son image (proches), chaque enfant ou il peut aller.

Images : fal, nano-banana-pro (retouche /edit avec les personnes en reference), 0,15 $ l'image. Originaux hors du depot :
C:/Users/jacqu/.wortando/ecole/img/. Les enfants restent neutres ou joyeux (fal refuse un enfant triste ou apeure).
"""
import hashlib, io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))

TEXTE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "ecole", "img")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
JOURNEE = os.path.join(os.path.expanduser("~"), ".wortando", "journee", "img")
SOURCES = {"Mark": PRINCIPAL + "/personnages/Mark.png", "Anna": FAMILLE + "/Anna-quotidien.png",
           "Jan": FAMILLE + "/Jan.png", "Katrin": FAMILLE + "/Katrin.png", "Ben": FAMILLE + "/Ben.png", "Mia": FAMILLE + "/Mia.png",
           # les lieux deja photographies (video/LIEUX.md) : la chambre des enfants, la cuisine de Jan et Katrin, l'ecole de Ben
           "chambre": JOURNEE + "/familia-1.png", "cuisine": JOURNEE + "/familia-2.png", "ecole": JOURNEE + "/familia-5.png"}
LANGUES = {"es": ["fr", "en", "pt", "ar", "de"], "de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]}

# ---------------------------------------------------------------------------------------------------------------
# LES LIEUX DES ENFANTS. akk : Wohin? (in die Kita) ; dat : Wo? (in der Kita) ; von : d'ou l'on vient chercher
# l'enfant (von der Kita) ; faux_akk / faux_dat : les formes fausses proposees en leurre (le mauvais cas, le mauvais
# article) ; trad : {langue: [le nom avec l'article, « a » + le lieu, « de » + le lieu]}.
LIEUX = {
    "de": {
        "kita":         {"mot": "Kita", "genre": "die", "nom": "die Kita", "akk": "in die Kita", "dat": "in der Kita", "von": "von der Kita",
                         "faux_akk": ["in der Kita", "in den Kita"], "faux_dat": ["in die Kita", "im Kita"],
                         "trad": {"fr": ["la garderie", "à la garderie", "de la garderie"], "en": ["the day-care centre", "to day care", "from day care"], "pt": ["a creche", "à creche", "da creche"]}},
        "kindergarten": {"mot": "Kindergarten", "genre": "der", "nom": "der Kindergarten", "akk": "in den Kindergarten", "dat": "im Kindergarten", "von": "vom Kindergarten",
                         "faux_akk": ["im Kindergarten", "in die Kindergarten"], "faux_dat": ["in den Kindergarten", "in die Kindergarten"],
                         "trad": {"fr": ["le jardin d'enfants", "au jardin d'enfants", "du jardin d'enfants"], "en": ["the kindergarten", "to kindergarten", "from kindergarten"], "pt": ["o jardim de infância", "ao jardim de infância", "do jardim de infância"]}},
        "grundschule":  {"mot": "Grundschule", "genre": "die", "nom": "die Grundschule", "akk": "in die Grundschule", "dat": "in der Grundschule", "von": "von der Grundschule",
                         "faux_akk": ["in der Grundschule", "in den Grundschule"], "faux_dat": ["in die Grundschule", "im Grundschule"],
                         "trad": {"fr": ["l'école primaire", "à l'école primaire", "de l'école primaire"], "en": ["the primary school", "to primary school", "from primary school"], "pt": ["a escola primária", "à escola primária", "da escola primária"]}},
        "schule":       {"mot": "Schule", "genre": "die", "nom": "die Schule", "akk": "in die Schule", "dat": "in der Schule", "von": "von der Schule",
                         "faux_akk": ["in der Schule", "ins Schule"], "faux_dat": ["in die Schule", "im Schule"],
                         "trad": {"fr": ["l'école", "à l'école", "de l'école"], "en": ["the school", "to school", "from school"], "pt": ["a escola", "à escola", "da escola"]}},
    },
    "es": {
        "guarderia":    {"mot": "guardería", "genre": "la", "nom": "la guardería", "akk": "a la guardería", "dat": "en la guardería", "von": "en la guardería",
                         "faux_akk": ["al guardería", "en la guardería"], "faux_dat": ["a la guardería", "al guardería"],
                         "trad": {"fr": ["la garderie", "à la garderie", "à la garderie"], "en": ["the day-care centre", "to day care", "from day care"], "pt": ["a creche", "à creche", "na creche"], "de": ["die Kita", "in die Kita", "von der Kita"]}},
        "colegio":      {"mot": "colegio", "genre": "el", "nom": "el colegio", "akk": "al colegio", "dat": "en el colegio", "von": "en el colegio",
                         "faux_akk": ["a el colegio", "en el colegio"], "faux_dat": ["al colegio", "a el colegio"],
                         "trad": {"fr": ["l'école", "à l'école", "à l'école"], "en": ["the school", "to school", "from school"], "pt": ["a escola", "à escola", "na escola"], "de": ["die Schule", "in die Schule", "von der Schule"]}},
        "escuela":      {"mot": "escuela", "genre": "la", "nom": "la escuela", "akk": "a la escuela", "dat": "en la escuela", "von": "en la escuela",
                         "faux_akk": ["al escuela", "en la escuela"], "faux_dat": ["a la escuela", "al escuela"],
                         "trad": {"fr": ["l'école", "à l'école", "à l'école"], "en": ["the school", "to school", "from school"], "pt": ["a escola", "à escola", "na escola"], "de": ["die Schule", "in die Schule", "von der Schule"]}},
    },
}
# les enfants : leur age et les lieux ou ils vont (les deux noms d'un meme lieu sont justes ; ceux de l'autre enfant,
# jamais : Ben, 7 ans, ne va plus a la Kita ; Mia, 4 ans, ne va pas encore a l'ecole)
ENFANTS = {"Ben": {"age": 7, "de": ["grundschule", "schule"], "es": ["colegio", "escuela"], "pron": {"de": "er", "es": ""}},
           "Mia": {"age": 4, "de": ["kita", "kindergarten"], "es": ["guarderia"], "pron": {"de": "sie", "es": ""}}}
AGES = {"de": {7: "sieben", 4: "vier"}, "es": {7: "siete", 4: "cuatro"}}

# ---------------------------------------------------------------------------------------------------------------
# CE QUE FONT LES PERSONNES. v : l'infinitif du corpus (la page prend sa conjugaison) ; s : le sujet (pl : deux
# personnes, la 3e personne du pluriel) ; c : le complement (en allemand, la particule separable va apres lui) ;
# img : l'image d'action (une image peut porter deux actions : jamais l'une pour leurre de l'autre) ; noms : les mots
# du corpus que l'action fait AUSSI travailler (le nom de l'image) ; adj : un adjectif (Ben ist krank) ;
# aussi_v : les verbes qui iraient aussi avec ce complement (jamais un leurre) ; pa : la « a » personnelle (es) ;
# t : la traduction de la phrase.
ACTIONS = {
    "de": [
        {"id": "bringen_kita", "v": "bringen", "s": "Katrin", "c": "Mia in die Kita", "img": "kita-bringen", "noms": [["Kita", "die"]], "faux_v": ["packen", "malen", "schreiben", "anrufen"], "aussi_v": [],
         "t": {"fr": "Katrin amène Mia à la garderie.", "en": "Katrin takes Mia to day care.", "pt": "Katrin leva a Mia à creche."}},
        {"id": "bringen_schule", "v": "bringen", "s": "Jan", "c": "Ben in die Schule", "img": "schulweg", "noms": [["Schule", "die"]], "faux_v": ["packen", "malen", "anrufen", "spielen"], "aussi_v": [],
         "t": {"fr": "Jan amène Ben à l'école.", "en": "Jan takes Ben to school.", "pt": "Jan leva o Ben à escola."}},
        {"id": "abholen_kita", "v": "abholen", "s": "Mark", "c": "Mia von der Kita", "img": "kita-abholen", "noms": [["Kita", "die"]], "faux_v": ["packen", "malen", "schreiben", "anmelden"], "aussi_v": [],
         "t": {"fr": "Mark va chercher Mia à la garderie.", "en": "Mark picks Mia up from day care.", "pt": "Mark busca a Mia na creche."}},
        {"id": "abholen_schule", "v": "abholen", "s": "Jan", "c": "Ben von der Schule", "img": "schule-abholen", "noms": [["Schule", "die"]], "faux_v": ["packen", "malen", "schreiben", "spielen"], "aussi_v": [],
         "t": {"fr": "Jan va chercher Ben à l'école.", "en": "Jan picks Ben up from school.", "pt": "Jan busca o Ben na escola."}},
        {"id": "anmelden", "v": "anmelden", "s": "Katrin", "c": "Mia in der Kita", "img": "anmelden", "noms": [["Kita", "die"]], "faux_v": ["packen", "schreiben", "anrufen"], "aussi_v": [],
         "t": {"fr": "Katrin inscrit Mia à la garderie.", "en": "Katrin registers Mia at the day-care centre.", "pt": "Katrin matricula a Mia na creche."}},
        {"id": "sprechen", "v": "sprechen", "s": "Katrin", "c": "mit der Lehrerin", "img": "lehrerin", "noms": [["Lehrerin", "die"]], "faux_v": ["packen", "anrufen"], "aussi_v": [],
         "t": {"fr": "Katrin parle avec l'enseignante.", "en": "Katrin talks to the teacher.", "pt": "Katrin fala com a professora."}},
        {"id": "anrufen", "v": "anrufen", "s": "Katrin", "c": "in der Schule", "img": "krank", "noms": [["Schule", "die"]], "aussi_v": [],
         "t": {"fr": "Katrin appelle l'école.", "en": "Katrin calls the school.", "pt": "Katrin liga para a escola."}},
        {"id": "krank", "v": "sein", "s": "Ben", "c": "krank", "img": "krank", "adj": "krank", "noms": [], "aussi_v": [], "etat": True,
         "t": {"fr": "Ben est malade.", "en": "Ben is ill.", "pt": "O Ben está doente."}},
        {"id": "packen", "v": "packen", "s": "Ben", "c": "seine Schultasche", "img": "packen", "noms": [["Schultasche", "die"]], "faux_v": ["anrufen", "sprechen", "spielen", "gehen"], "aussi_v": [],
         "t": {"fr": "Ben prépare son cartable.", "en": "Ben packs his school bag.", "pt": "O Ben arruma a mochila da escola."}},
        {"id": "hausaufgaben", "v": "machen", "s": "Ben", "c": "seine Hausaufgaben", "img": "hausaufgaben", "noms": [["Hausaufgabe", "die"]], "faux_v": ["spielen", "sprechen", "anrufen", "gehen"], "aussi_v": [],
         "t": {"fr": "Ben fait ses devoirs.", "en": "Ben does his homework.", "pt": "O Ben faz a lição de casa."}},
        {"id": "schreiben", "v": "schreiben", "s": "Ben", "c": "in sein Heft", "img": "klasse", "noms": [["Heft", "das"]], "faux_v": ["anrufen", "gehen", "sprechen", "spielen"], "aussi_v": ["malen"],
         "t": {"fr": "Ben écrit dans son cahier.", "en": "Ben writes in his exercise book.", "pt": "O Ben escreve no caderno."}},
        {"id": "malen", "v": "malen", "s": "Mia", "c": "ein Bild", "img": "malen", "noms": [], "faux_v": ["anrufen", "gehen", "sprechen", "spielen"], "aussi_v": [],
         "t": {"fr": "Mia peint un tableau.", "en": "Mia paints a picture.", "pt": "A Mia pinta um quadro."}},
        {"id": "spielen", "v": "spielen", "s": "Ben", "c": "in der Pause", "img": "pause", "noms": [["Pause", "die"]], "aussi_v": [],
         "t": {"fr": "Ben joue pendant la récréation.", "en": "Ben plays at break time.", "pt": "O Ben brinca no recreio."}},
        {"id": "elternabend", "v": "gehen", "s": "Jan und Katrin", "pl": True, "c": "zum Elternabend", "img": "elternabend", "noms": [["Elternabend", "der"]], "aussi_v": [],
         "t": {"fr": "Jan et Katrin vont à la réunion de parents.", "en": "Jan and Katrin go to the parents' evening.", "pt": "Jan e Katrin vão à reunião de pais."}},
    ],
    "es": [
        {"id": "bringen_kita", "v": "llevar", "s": "Katrin", "pa": "Mia", "c": "a la guardería", "img": "kita-bringen", "noms": [["guardería", "la"]], "faux_v": ["preparar", "escribir", "pintar", "hablar", "llamar"], "aussi_v": [],
         "t": {"fr": "Katrin amène Mia à la garderie.", "en": "Katrin takes Mia to day care.", "pt": "Katrin leva a Mia à creche.", "de": "Katrin bringt Mia in die Kita."}},
        {"id": "bringen_schule", "v": "llevar", "s": "Jan", "pa": "Ben", "c": "al colegio", "img": "schulweg", "noms": [["colegio", "el"]], "faux_v": ["preparar", "escribir", "pintar", "hablar"], "aussi_v": [],
         "t": {"fr": "Jan amène Ben à l'école.", "en": "Jan takes Ben to school.", "pt": "Jan leva o Ben à escola.", "de": "Jan bringt Ben in die Schule."}},
        {"id": "abholen_kita", "v": "recoger", "s": "Mark", "pa": "Mia", "c": "en la guardería", "img": "kita-abholen", "noms": [["guardería", "la"]], "faux_v": ["preparar", "escribir", "hablar", "llamar"], "aussi_v": [],
         "t": {"fr": "Mark va chercher Mia à la garderie.", "en": "Mark picks Mia up from day care.", "pt": "Mark busca a Mia na creche.", "de": "Mark holt Mia von der Kita ab."}},
        {"id": "abholen_schule", "v": "recoger", "s": "Jan", "pa": "Ben", "c": "en el colegio", "img": "schule-abholen", "noms": [["colegio", "el"]], "faux_v": ["preparar", "escribir", "hablar", "llamar"], "aussi_v": [],
         "t": {"fr": "Jan va chercher Ben à l'école.", "en": "Jan picks Ben up from school.", "pt": "Jan busca o Ben na escola.", "de": "Jan holt Ben von der Schule ab."}},
        {"id": "anmelden", "v": "matricular", "s": "Katrin", "pa": "Mia", "c": "en la guardería", "img": "anmelden", "noms": [["guardería", "la"]], "faux_v": ["preparar", "escribir", "hablar", "llamar"], "aussi_v": [],
         "t": {"fr": "Katrin inscrit Mia à la garderie.", "en": "Katrin registers Mia at the day-care centre.", "pt": "Katrin matricula a Mia na creche.", "de": "Katrin meldet Mia in der Kita an."}},
        {"id": "sprechen", "v": "hablar", "s": "Katrin", "c": "con la profesora", "img": "lehrerin", "noms": [["profesora", "la"]], "faux_v": ["preparar", "matricular", "recoger"], "aussi_v": [],
         "t": {"fr": "Katrin parle avec l'enseignante.", "en": "Katrin talks to the teacher.", "pt": "Katrin fala com a professora.", "de": "Katrin spricht mit der Lehrerin."}},
        {"id": "anrufen", "v": "llamar", "s": "Katrin", "c": "al colegio", "img": "krank", "noms": [["colegio", "el"]], "aussi_v": [],
         "t": {"fr": "Katrin appelle l'école.", "en": "Katrin calls the school.", "pt": "Katrin liga para a escola.", "de": "Katrin ruft in der Schule an."}},
        {"id": "krank", "v": "estar", "s": "Ben", "c": "enfermo", "img": "krank", "adj": "enfermo", "noms": [], "aussi_v": [], "etat": True,
         "t": {"fr": "Ben est malade.", "en": "Ben is ill.", "pt": "O Ben está doente.", "de": "Ben ist krank."}},
        {"id": "packen", "v": "preparar", "s": "Ben", "c": "su mochila", "img": "packen", "noms": [["mochila", "la"]], "faux_v": ["hablar", "llamar", "jugar", "ir"], "aussi_v": [],
         "t": {"fr": "Ben prépare son cartable.", "en": "Ben packs his school bag.", "pt": "O Ben arruma a mochila.", "de": "Ben packt seine Schultasche."}},
        {"id": "hausaufgaben", "v": "hacer", "s": "Ben", "c": "los deberes", "img": "hausaufgaben", "noms": [["deberes", "los"]], "faux_v": ["hablar", "llamar", "jugar", "ir"], "aussi_v": ["preparar"],
         "t": {"fr": "Ben fait ses devoirs.", "en": "Ben does his homework.", "pt": "O Ben faz a lição de casa.", "de": "Ben macht seine Hausaufgaben."}},
        {"id": "schreiben", "v": "escribir", "s": "Ben", "c": "en su cuaderno", "img": "klasse", "noms": [["cuaderno", "el"]], "faux_v": ["llamar", "ir", "hablar", "recoger"], "aussi_v": ["pintar", "dibujar"],
         "t": {"fr": "Ben écrit dans son cahier.", "en": "Ben writes in his exercise book.", "pt": "O Ben escreve no caderno.", "de": "Ben schreibt in sein Heft."}},
        {"id": "malen", "v": "pintar", "s": "Mia", "c": "en la guardería", "img": "malen", "noms": [["guardería", "la"]], "aussi_v": ["jugar", "dibujar", "escribir"],
         "t": {"fr": "Mia peint à la garderie.", "en": "Mia paints at day care.", "pt": "A Mia pinta na creche.", "de": "Mia malt in der Kita."}},
        {"id": "spielen", "v": "jugar", "s": "Ben", "c": "en el recreo", "img": "pause", "noms": [["recreo", "el"]], "aussi_v": [],
         "t": {"fr": "Ben joue pendant la récréation.", "en": "Ben plays at break time.", "pt": "O Ben brinca no recreio.", "de": "Ben spielt in der Pause."}},
        {"id": "elternabend", "v": "ir", "s": "Jan y Katrin", "pl": True, "c": "a la reunión de padres", "img": "elternabend", "noms": [["reunión", "la"]], "aussi_v": [],
         "t": {"fr": "Jan et Katrin vont à la réunion de parents.", "en": "Jan and Katrin go to the parents' meeting.", "pt": "Jan e Katrin vão à reunião de pais.", "de": "Jan und Katrin gehen zum Elternabend."}},
    ],
}

# ---------------------------------------------------------------------------------------------------------------
# LES FOURNITURES. Une image par objet (decoupee dans une seule photo « material », ou seule). pl : le pluriel du
# corpus ; proches : les objets qu'on pourrait confondre sur l'image (jamais un leurre l'un de l'autre) ;
# liste : False pour un objet qui n'entre pas dans la liste des fournitures. trad : [le nom avec l'article, le pluriel].
OBJETS = {
    "de": {
        "schultasche":   {"mot": "Schultasche", "genre": "die", "pl": "Schultaschen", "img": "ranzen", "proches": [], "liste": False,
                          "trad": {"fr": ["le cartable", "cartables"], "en": ["the school bag", "school bags"], "pt": ["a mochila da escola", "mochilas"]}},
        "federmaeppchen": {"mot": "Federmäppchen", "genre": "das", "pl": "Federmäppchen", "img": "maeppchen", "proches": [],
                          "trad": {"fr": ["la trousse", "trousses"], "en": ["the pencil case", "pencil cases"], "pt": ["o estojo", "estojos"]}},
        "heft":          {"mot": "Heft", "genre": "das", "pl": "Hefte", "img": "heft", "proches": ["buch"],
                          "trad": {"fr": ["le cahier", "cahiers"], "en": ["the exercise book", "exercise books"], "pt": ["o caderno", "cadernos"]}},
        "bleistift":     {"mot": "Bleistift", "genre": "der", "pl": "Bleistifte", "img": "bleistift", "proches": [],
                          "trad": {"fr": ["le crayon à papier", "crayons à papier"], "en": ["the pencil", "pencils"], "pt": ["o lápis", "lápis"]}},
        "lineal":        {"mot": "Lineal", "genre": "das", "pl": "Lineale", "img": "lineal", "proches": [],
                          "trad": {"fr": ["la règle", "règles"], "en": ["the ruler", "rulers"], "pt": ["a régua", "réguas"]}},
        "radiergummi":   {"mot": "Radiergummi", "genre": "der", "pl": "Radiergummis", "img": "radiergummi", "proches": [],
                          "trad": {"fr": ["la gomme", "gommes"], "en": ["the eraser", "erasers"], "pt": ["a borracha", "borrachas"]}},
        "buch":          {"mot": "Buch", "genre": "das", "pl": "Bücher", "img": "buch", "proches": ["heft"],
                          "trad": {"fr": ["le livre", "livres"], "en": ["the book", "books"], "pt": ["o livro", "livros"]}},
        "schere":        {"mot": "Schere", "genre": "die", "pl": "Scheren", "img": "schere", "proches": [],
                          "trad": {"fr": ["les ciseaux", "paires de ciseaux"], "en": ["the scissors", "pairs of scissors"], "pt": ["a tesoura", "tesouras"]}},
    },
    "es": {
        "mochila":       {"mot": "mochila", "genre": "la", "pl": "mochilas", "img": "ranzen", "proches": [], "liste": False,
                          "trad": {"fr": ["le cartable", "cartables"], "en": ["the school bag", "school bags"], "pt": ["a mochila", "mochilas"], "de": ["die Schultasche", "Schultaschen"]}},
        "estuche":       {"mot": "estuche", "genre": "el", "pl": "estuches", "img": "maeppchen", "proches": [],
                          "trad": {"fr": ["la trousse", "trousses"], "en": ["the pencil case", "pencil cases"], "pt": ["o estojo", "estojos"], "de": ["das Federmäppchen", "Federmäppchen"]}},
        "cuaderno":      {"mot": "cuaderno", "genre": "el", "pl": "cuadernos", "img": "heft", "proches": ["libro"],
                          "trad": {"fr": ["le cahier", "cahiers"], "en": ["the exercise book", "exercise books"], "pt": ["o caderno", "cadernos"], "de": ["das Heft", "Hefte"]}},
        "lapiz":         {"mot": "lápiz", "genre": "el", "pl": "lápices", "img": "bleistift", "proches": [],
                          "trad": {"fr": ["le crayon", "crayons"], "en": ["the pencil", "pencils"], "pt": ["o lápis", "lápis"], "de": ["der Bleistift", "Bleistifte"]}},
        "regla":         {"mot": "regla", "genre": "la", "pl": "reglas", "img": "lineal", "proches": [],
                          "trad": {"fr": ["la règle", "règles"], "en": ["the ruler", "rulers"], "pt": ["a régua", "réguas"], "de": ["das Lineal", "Lineale"]}},
        "goma":          {"mot": "goma", "genre": "la", "pl": "gomas", "img": "radiergummi", "proches": [],
                          "trad": {"fr": ["la gomme", "gommes"], "en": ["the eraser", "erasers"], "pt": ["a borracha", "borrachas"], "de": ["der Radiergummi", "Radiergummis"]}},
        "libro":         {"mot": "libro", "genre": "el", "pl": "libros", "img": "buch", "proches": ["cuaderno"],
                          "trad": {"fr": ["le livre", "livres"], "en": ["the book", "books"], "pt": ["o livro", "livros"], "de": ["das Buch", "Bücher"]}},
        "tijeras":       {"mot": "tijeras", "genre": "las", "pl": "tijeras", "img": "schere", "proches": [], "liste": False,
                          "trad": {"fr": ["les ciseaux", "paires de ciseaux"], "en": ["the scissors", "pairs of scissors"], "pt": ["a tesoura", "tesouras"], "de": ["die Schere", "Scheren"]}},
    },
}
NOMBRES = {"de": ["", "ein", "zwei", "drei", "vier", "fünf"], "es": ["", "un", "dos", "tres", "cuatro", "cinco"],
           "fr": ["", "un", "deux", "trois", "quatre", "cinq"], "en": ["", "one", "two", "three", "four", "five"], "pt": ["", "um", "dois", "três", "quatro", "cinco"]}

# ---------------------------------------------------------------------------------------------------------------
# L'HORAIRE DE BEN (classe 2b / 2.º B) : les heures et les matieres, jour par jour (1 = lundi). La matiere porte le mot
# du corpus qu'elle fait travailler (None : pas au corpus, jamais visee).
HEURES = [["8:00", "8:45"], ["8:50", "9:35"], ["9:55", "10:40"], ["10:45", "11:30"], ["11:35", "12:20"], ["12:25", "13:10"]]
PAUSE = ["9:35", "9:55"]
MATIERES = {
    "de": {"deutsch": {"aff": "Deutsch", "mot": None}, "mathe": {"aff": "Mathe", "mot": ["Mathe", "die"]}, "sport": {"aff": "Sport", "mot": ["Sport", "der"]},
           "kunst": {"aff": "Kunst", "mot": ["Kunst", "die"]}, "musik": {"aff": "Musik", "mot": ["Musik", "die"]},
           "sachunterricht": {"aff": "Sachunterricht", "mot": None}, "englisch": {"aff": "Englisch", "mot": None}},
    "es": {"deutsch": {"aff": "Lengua", "mot": None}, "mathe": {"aff": "Matemáticas", "mot": None}, "sport": {"aff": "Educación Física", "mot": None},
           "kunst": {"aff": "Plástica", "mot": None}, "musik": {"aff": "Música", "mot": ["música", "la"]},
           "sachunterricht": {"aff": "Ciencias", "mot": None}, "englisch": {"aff": "Inglés", "mot": None}},
}
MATIERES_TRAD = {"deutsch": {"fr": "allemand", "en": "German", "pt": "alemão", "de": "Deutsch"}, "mathe": {"fr": "maths", "en": "maths", "pt": "matemática", "de": "Mathe"},
                 "sport": {"fr": "sport", "en": "PE", "pt": "educação física", "de": "Sport"}, "kunst": {"fr": "arts plastiques", "en": "art", "pt": "artes", "de": "Kunst"},
                 "musik": {"fr": "musique", "en": "music", "pt": "música", "de": "Musik"}, "sachunterricht": {"fr": "sciences", "en": "science", "pt": "ciências", "de": "Sachunterricht"},
                 "englisch": {"fr": "anglais", "en": "English", "pt": "inglês", "de": "Englisch"}}
HORAIRE = {1: ["deutsch", "deutsch", "mathe", "sachunterricht", "sport"],
           2: ["mathe", "deutsch", "englisch", "kunst", "kunst"],
           3: ["deutsch", "mathe", "musik", "sport", "sachunterricht"],
           4: ["mathe", "deutsch", "sachunterricht", "englisch", "musik", "sport"],
           5: ["deutsch", "mathe", "deutsch", "sport"]}
JOURS = {"de": ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
         "es": ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"],
         "fr": ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"],
         "en": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
         "pt": ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]}
MOIS = {"de": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
        "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
        "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
        "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "pt": ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]}
ORDINAUX = {"de": ["", "ersten", "zweiten", "dritten", "vierten", "fünften", "sechsten"], "es": ["", "primera", "segunda", "tercera", "cuarta", "quinta", "sexta"],
            "fr": ["", "première", "deuxième", "troisième", "quatrième", "cinquième", "sixième"], "en": ["", "first", "second", "third", "fourth", "fifth", "sixth"],
            "pt": ["", "primeira", "segunda", "terceira", "quarta", "quinta", "sexta"]}

# ---------------------------------------------------------------------------------------------------------------
# LES VACANCES SCOLAIRES 2026-2027 (inventees, vraisemblables pour Berlin) : [cle, debut, fin] en (jour, mois, annee)
FERIEN = [["herbst", [19, 10, 2026], [31, 10, 2026]], ["weihnachten", [21, 12, 2026], [2, 1, 2027]], ["winter", [1, 2, 2027], [6, 2, 2027]],
          ["ostern", [22, 3, 2027], [2, 4, 2027]], ["sommer", [8, 7, 2027], [20, 8, 2027]]]
# L'ESPAGNOL A LES VRAIES VACANCES DE MADRID, 2026-2027 (decision de Jacques, 8 nov. 2026). Source officielle : ORDEN 2034/2026,
# BOCM n. 131 du 4 juin 2026 : premier jour de classe en primaire le 7 sept., dernier le 18 juin ; Navidad du 23 dec. au 6 janv.
# et 7-8 janv. non lectifs ; Semana Santa du 20 au 28 mars et 19 et 29 mars non lectifs ; l'Orden donne a ces jours « los mismos
# efectos » que les vacances, d'ou les periodes affichees. L'ete n'a pas de date de fin : elle depend du curso 2027/2028, pas encore fixe.
FERIEN_ES = [["weihnachten", [23, 12, 2026], [8, 1, 2027]], ["ostern", [19, 3, 2027], [29, 3, 2027]], ["sommer", [19, 6, 2027], None]]
RENTREE_ES = [7, 9, 2026]
# jours sans classe absents du calendrier affiche : jamais tires pour « tiene colegio ». Festivites et non lectifs de l'Orden ; 9.11 = la
# Almudena, a Madrid ville ; 3.5.2027 par prudence : le 2 mai tombe un dimanche et son report eventuel n'est pas fixe par l'Orden.
SANS_ECOLE_ES = ["12.10.2026", "2.11.2026", "9.11.2026", "7.12.2026", "8.12.2026", "12.2.2027", "15.2.2027", "3.5.2027"]
FERIEN_NOMS = {"de": {"herbst": "Herbstferien", "weihnachten": "Weihnachtsferien", "winter": "Winterferien", "ostern": "Osterferien", "sommer": "Sommerferien"},
               "es": {"herbst": "vacaciones de otoño", "weihnachten": "vacaciones de Navidad", "winter": "vacaciones de invierno", "ostern": "vacaciones de Semana Santa", "sommer": "vacaciones de verano"},
               "fr": {"herbst": "vacances d'automne", "weihnachten": "vacances de Noël", "winter": "vacances d'hiver", "ostern": "vacances de Pâques", "sommer": "vacances d'été"},
               "en": {"herbst": "autumn holidays", "weihnachten": "Christmas holidays", "winter": "winter holidays", "ostern": "Easter holidays", "sommer": "summer holidays"},
               "pt": {"herbst": "férias de outono", "weihnachten": "férias de Natal", "winter": "férias de inverno", "ostern": "férias da Páscoa", "sommer": "férias de verão"}}

# ---------------------------------------------------------------------------------------------------------------
# LES PAPIERS. Le mot d'absence : les raisons (la phrase et les mots du corpus qu'elle fait travailler) ;
# l'invitation a la reunion de parents : les jours, heures, salles et sujets possibles ; qui va chercher Mia.
RAISONS = {
    "de": {"krank": {"p": "Er ist krank.", "mots": [["krank", "adjectif"]], "t": {"fr": "Il est malade.", "en": "He is ill.", "pt": "Ele está doente."}},
           "fieber": {"p": "Er hat Fieber.", "mots": [["Fieber", "das"]], "t": {"fr": "Il a de la fièvre.", "en": "He has a temperature.", "pt": "Ele está com febre."}},
           "arzt": {"p": "Er hat einen Termin beim Arzt.", "mots": [["Termin", "der"], ["Arzt", "der"]], "t": {"fr": "Il a rendez-vous chez le médecin.", "en": "He has a doctor's appointment.", "pt": "Ele tem consulta no médico."}}},
    "es": {"krank": {"p": "Está enfermo.", "mots": [["enfermo", "adjectif"]], "t": {"fr": "Il est malade.", "en": "He is ill.", "pt": "Ele está doente.", "de": "Er ist krank."}},
           "fieber": {"p": "Tiene fiebre.", "mots": [["fiebre", "la"]], "t": {"fr": "Il a de la fièvre.", "en": "He has a temperature.", "pt": "Ele está com febre.", "de": "Er hat Fieber."}},
           "arzt": {"p": "Tiene cita con el médico.", "mots": [["cita", "la"], ["médico", "el"]], "t": {"fr": "Il a rendez-vous chez le médecin.", "en": "He has a doctor's appointment.", "pt": "Ele tem consulta no médico.", "de": "Er hat einen Termin beim Arzt."}}},
}
ELTERNABEND = {"heures": [[18, 0], [18, 30], [19, 0], [19, 30]], "salles": {"de": ["Raum 12", "Raum 8", "Raum 21"], "es": ["aula 12", "aula 8", "aula 21"]},
               "sujets": {"de": ["der Ausflug in den Zoo", "die Weihnachtsfeier", "die Hausaufgaben", "das Schwimmen im Sportunterricht", "die Klassenfahrt"],
                          "es": ["la excursión al zoo", "la fiesta de Navidad", "los deberes", "la natación en Educación Física", "el viaje de fin de curso"]},
               "sujets_t": {"fr": ["la sortie au zoo", "la fête de Noël", "les devoirs", "la natation en sport", "le voyage de classe"],
                            "en": ["the trip to the zoo", "the Christmas party", "the homework", "swimming in PE", "the class trip"],
                            "pt": ["o passeio ao zoológico", "a festa de Natal", "a lição de casa", "a natação na educação física", "a viagem da turma"],
                            "de": ["der Ausflug in den Zoo", "die Weihnachtsfeier", "die Hausaufgaben", "das Schwimmen im Sportunterricht", "die Klassenfahrt"]}}
# qui peut aller chercher Mia (la Kita a leurs noms) : les parents, la tante Anna, l'ami Mark
ABHOLER = {"Katrin": {"de": "ihre Mutter", "es": "su madre", "t": {"fr": "sa mère", "en": "her mother", "pt": "a mãe dela", "de": "ihre Mutter"}},
           "Jan": {"de": "ihr Vater", "es": "su padre", "t": {"fr": "son père", "en": "her father", "pt": "o pai dela", "de": "ihr Vater"}},
           "Anna": {"de": "ihre Tante", "es": "su tía", "t": {"fr": "sa tante", "en": "her aunt", "pt": "a tia dela", "de": "ihre Tante"}},
           "Mark": {"de": "ein Freund der Familie", "es": "un amigo de la familia", "t": {"fr": "un ami de la famille", "en": "a friend of the family", "pt": "um amigo da família", "de": "ein Freund der Familie"}}}
ABHOL_HEURES = [[13, 0], [14, 30], [15, 0], [15, 30], [16, 0], [16, 30]]
# les papiers eux-memes, comme des mots : « Was ist das? » -> der Stundenplan (le mot du corpus et sa traduction)
PAPIERS = {
    "de": {"stundenplan": {"mot": "Stundenplan", "genre": "der", "aff": "ein Stundenplan", "t": {"fr": "un emploi du temps", "en": "a timetable", "pt": "um horário escolar"}},
           "entschuldigung": {"mot": "Entschuldigung", "genre": "die", "aff": "eine Entschuldigung", "t": {"fr": "un mot d'absence", "en": "a note excusing an absence", "pt": "uma justificativa de falta"}},
           "elternabend": {"mot": "Elternabend", "genre": "der", "aff": "eine Einladung zum Elternabend", "t": {"fr": "une invitation à la réunion de parents", "en": "an invitation to the parents' evening", "pt": "um convite para a reunião de pais"}},
           "ferien": {"mot": "Ferien", "genre": "die", "aff": "ein Ferienkalender", "t": {"fr": "un calendrier des vacances", "en": "a holiday calendar", "pt": "um calendário de férias"}},
           "liste": {"mot": None, "genre": None, "aff": "eine Materialliste", "t": {"fr": "une liste de fournitures", "en": "a list of school supplies", "pt": "uma lista de material escolar"}}},
    "es": {"stundenplan": {"mot": "horario", "genre": "el", "aff": "un horario", "t": {"fr": "un emploi du temps", "en": "a timetable", "pt": "um horário escolar", "de": "ein Stundenplan"}},
           "entschuldigung": {"mot": "justificante", "genre": "el", "aff": "un justificante", "t": {"fr": "un mot d'absence", "en": "a note excusing an absence", "pt": "uma justificativa de falta", "de": "eine Entschuldigung"}},
           "elternabend": {"mot": "reunión", "genre": "la", "aff": "una invitación a la reunión de padres", "t": {"fr": "une invitation à la réunion de parents", "en": "an invitation to the parents' meeting", "pt": "um convite para a reunião de pais", "de": "eine Einladung zum Elternabend"}},
           "ferien": {"mot": "vacaciones", "genre": "las", "aff": "un calendario de vacaciones", "t": {"fr": "un calendrier des vacances", "en": "a holiday calendar", "pt": "um calendário de férias", "de": "ein Ferienkalender"}},
           "liste": {"mot": None, "genre": None, "aff": "una lista de material", "t": {"fr": "une liste de fournitures", "en": "a list of school supplies", "pt": "uma lista de material escolar", "de": "eine Materialliste"}}},
}
NOMS_ECOLE = {"de": {"kita": "Kita Pusteblume", "schule": "Grundschule am Kiez", "lehrerin": "Frau Weber", "erzieherin": "Frau Krüger", "klasse": "2b"},
              "es": {"kita": "Guardería Pusteblume", "schule": "Colegio Am Kiez", "lehrerin": "la señora Ortega", "erzieherin": "la señora Krüger", "klasse": "2.º B"}}

# ---------------------------------------------------------------------------------------------------------------
# LES MOTS ABSENTS DU CORPUS, a ajouter PAR PAIRES (accord de Jacques), prepares dans ajouts/ecole.json et
# espanol/ajouts/ecole.json : en attendant, l'app les tient « hors jeu ». Leur traduction ici (la ligne sous le mot).
AJOUTS_TRAD = {
    "de": {"Schultasche": {"fr": "cartable", "en": "school bag", "tr": "okul çantası", "uk": "шкільний ранець", "fa": "کیف مدرسه", "ar": "حقيبة المدرسة",
                           "pt": "mochila escolar", "pl": "tornister", "ru": "школьный ранец"}},
    "es": {"guardería": {"fr": "garderie, crèche", "en": "day-care centre", "pt": "creche", "ar": "حضانة الأطفال", "de": "Kita"},
           "justificante": {"fr": "justificatif, mot d'absence", "en": "note excusing an absence", "pt": "justificativa", "ar": "مبرر الغياب", "de": "Entschuldigung"},
           "deberes": {"fr": "devoirs", "en": "homework", "pt": "lição de casa", "ar": "الواجبات المدرسية", "de": "Hausaufgaben"},
           "recreo": {"fr": "récréation", "en": "break time", "pt": "recreio", "ar": "الاستراحة", "de": "Pause"},
           "estuche": {"fr": "trousse", "en": "pencil case", "pt": "estojo", "ar": "مقلمة", "de": "Federmäppchen"},
           "matricular": {"fr": "inscrire", "en": "to register, to enrol", "pt": "matricular", "ar": "يسجّل", "de": "anmelden"}},
}


# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES (4:3, aucun texte lisible). source : les personnes en reference (jamais une description seule d'une
# personne connue) et le lieu (« pour le lieu ») ; les objets sont decoupes dans une seule photo (« material »).
# ESSAI : la planche d'essai (6 images, 0,90 $), a montrer a Jacques avant le reste.
PHOTO = (" A photorealistic photograph, natural light, natural colours, 4:3 landscape format. ABSOLUTELY NO readable text, "
         "no letters, no numbers, no logos, no signs, no captions, no watermark anywhere in the picture: every paper, book cover, "
         "board and screen is blank or blurred. Hands: five fingers each, natural. The children are calm or smiling, relaxed and happy.")
QUI = {"Ben": "Ben is the 7-year-old boy of reference picture {n} (exactly the same face, hair and age)",
       "Mia": "Mia is the 4-year-old girl of reference picture {n} (exactly the same face, hair and age)",
       "Katrin": "Katrin is the woman of reference picture {n} (exactly the same face, hair and age)",
       "Jan": "Jan is the man of reference picture {n} (exactly the same face, beard, hair and age)",
       "Mark": "Mark is the young man of reference picture {n} (exactly the same face, curly dark brown hair, age and build)"}
KITA = ("The place is a bright, friendly Berlin day-care centre (Kita): pale wooden floor, white walls, low wooden benches and a row of small "
        "coat hooks with children's jackets and little backpacks, colourful children's drawings without any writing on the walls, big windows. ")
ERZIEHERIN = "the day-care teacher, a friendly woman in her forties with short red-blond hair, a green cardigan and jeans"
LEHRERIN = "Ben's class teacher, a friendly woman in her forties with shoulder-length brown hair, glasses, a dark blue jumper"
CLASSE = ("The place is a primary school classroom in Berlin for 7-year-olds: small light wooden desks and light wooden chairs in rows, a big "
          "green blackboard that is completely clean and empty, children's paintings without writing on a corkboard on the right, a window on the left. ")
IMAGES = {
    # les fournitures : une seule photo, decoupee ensuite (decouper.py)
    "material":      {"qui": [], "prompt": "Flat lay seen from directly above on a light wooden school desk: seven school supplies laid out in a neat grid, "
                      "well apart from each other, none touching or overlapping, each one whole and fully inside the picture: a plain blue exercise book "
                      "(thin, soft cover, closed), a thick hardback children's book with a plain green cover, a zipped red pencil case, one yellow pencil "
                      "with a pink end, a transparent 30 cm plastic ruler without numbers, a white and blue eraser, a pair of children's scissors with "
                      "orange handles. Even soft daylight, no shadows hiding anything. No people, no hands."},
    "ranzen":        {"qui": [], "prompt": "A German children's school satchel (Schulranzen), bright blue with reflective strips, standing alone on a light "
                      "wooden floor against a white wall, seen from the front, the whole satchel in the picture, closed. No people, no hands."},
    # amener, aller chercher, inscrire
    "kita-bringen":  {"qui": ["Katrin", "Mia"], "prompt": KITA + "Morning. Katrin, in her coat, kneels in the cloakroom and helps Mia take off her "
                      "jacket at Mia's coat hook; " + ERZIEHERIN + " stands next to them and greets Mia with a warm smile. Seen from the side, the whole scene."},
    "kita-abholen":  {"qui": ["Mark", "Mia"], "lieu": "kita-bringen", "prompt": "The same day-care cloakroom as in the last reference picture, in the "
                      "afternoon. Mia, with her jacket already on and her little backpack, runs happily towards Mark, who has just come in, smiling, "
                      "and crouches to catch her; " + ERZIEHERIN + " watches them, smiling. Seen from the side, the whole scene."},
    "schulweg":      {"existe": "journee/familia-5"},
    "schule-abholen": {"qui": ["Jan", "Ben"], "lieu": "ecole", "prompt": "The same primary school entrance on the same Berlin street as in the last "
                      "reference picture, but in the early afternoon in daylight. Ben, with his school satchel on his back, comes out of the glass "
                      "door and runs to his father Jan, who waits on the pavement and opens his arms, both smiling. Other children leave the school."},
    "anmelden":      {"qui": ["Katrin", "Jan", "Mia"], "lieu": "kita-bringen", "prompt": "A small office in the same day-care centre as in the last "
                      "reference picture. Katrin and Jan sit at a desk opposite the day-care director (a woman in her fifties with grey hair in a bun "
                      "and a red scarf) and Katrin fills in a blank paper registration form with a pen; Mia sits on Jan's lap and plays with a wooden "
                      "toy. Seen at three quarters, from the waist up."},
    # a l'ecole
    "klasse":        {"qui": ["Ben"], "prompt": CLASSE + "Ben sits at his desk among his classmates and writes carefully in his exercise book with a "
                      "pencil; " + LEHRERIN + " walks between the desks behind him. Seen from the front at the height of the children, Ben in the middle."},
    "lehrerin":      {"qui": ["Katrin", "Ben"], "lieu": "klasse", "prompt": "At the open door of the same classroom as in the last reference picture, "
                      "after school: Katrin talks with " + LEHRERIN + " (the woman of the last reference picture), both friendly and attentive; Ben "
                      "stands next to his mother with his satchel. Seen from the side, the three of them from the waist up."},
    "elternabend":   {"qui": ["Jan", "Katrin"], "lieu": "klasse", "prompt": "The same classroom as in the last reference picture, in the evening, "
                      "the ceiling lights on, dark outside. A parents' evening with ONLY ADULTS, no children at all in the room: Jan, Katrin and four other parents sit on the small "
                      "children's chairs, their knees up high, a little amused; " + LEHRERIN + " (the woman of the last reference picture) stands in front of the clean "
                      "blackboard and talks to them. Seen from the side of the room, a funny, warm moment."},
    "pause":         {"qui": ["Ben"], "lieu": "ecole", "prompt": "The schoolyard of the same Berlin primary school as in the last reference picture, "
                      "during the morning break, daylight: Ben laughs and runs after a red ball with three classmates, a big chestnut tree and a "
                      "climbing frame behind them. Seen from a little distance, the whole schoolyard."},
    # a la maison
    "krank":         {"qui": ["Ben", "Katrin"], "lieu": "chambre", "prompt": "The same children's bedroom as in the last reference picture, in the "
                      "morning. Ben lies in his bed under the duvet, in pyjamas, a thermometer in his mouth, calm and cosy, a cup of tea on the bedside "
                      "table; Katrin sits on the edge of the bed, one hand on his forehead, and phones the school with her mobile phone. Calm, caring mood."},
    "hausaufgaben":  {"qui": ["Ben", "Jan"], "lieu": "cuisine", "prompt": "The same family kitchen as in the last reference picture, in the "
                      "afternoon. Ben sits at the wooden table and does his homework in an exercise book, concentrating; Jan sits beside him and points "
                      "at the page to help, a glass of milk on the table. The pages show no readable writing."},
    "packen":        {"qui": ["Ben"], "lieu": "chambre", "prompt": "The same children's bedroom as in the last reference picture, in the evening. "
                      "Ben kneels on the rug and packs his open blue school satchel: he puts an exercise book and his red pencil case into it, a few "
                      "books beside him. Seen from the side, the whole child in the picture."},
    "malen":         {"qui": ["Mia"], "lieu": "kita-bringen", "prompt": "The play room of the same day-care centre as in the last reference picture. "
                      "Mia, in a little painting apron, paints a colourful picture of a house and a sun with a brush at a low table, two other small "
                      "children paint beside her, pots of paint on the table. Seen at the height of the children."},
}
ESSAI = ["material", "kita-bringen", "kita-abholen", "klasse", "krank", "elternabend"]
# les decoupes de « material » (x0, y0, x1, y1 en fractions de l'image), a relever sur l'image une fois faite
DECOUPES = {"heft": (110, 90, 570, 660), "buch": (585, 85, 1005, 660), "maeppchen": (995, 80, 1310, 660), "bleistift": (125, 690, 605, 785),
            "lineal": (125, 805, 655, 935), "radiergummi": (685, 805, 895, 915), "schere": (915, 765, 1290, 945)}
DECOUPES = {k: (x0 / 1400, y0 / 1045, x1 / 1400, y1 / 1045) for k, (x0, y0, x1, y1) in DECOUPES.items()}   # relevees sur la vue 1400 x 1045


# ---------------------------------------------------------------------------------------------------------------
# LE PORTUGAIS APPRIS (lot P4, 12 nov. 2026). Lisbonne, le Portugal d'abord ; « br_ » seulement la ou le Bresil differe
# (la page prend pt_, ou br_ s'il existe, avec &variante=br, et les pose sous « pt » au chargement). Pas « pt » : cette
# cle est deja la TRADUCTION en portugais du Bresil pour qui apprend es ou de. La meme famille que l'espagnol a Madrid :
# Jan et Katrin, Ben (7 ans, a escola, 2.º ano) et Mia (4 ans, o jardim de infância -- jamais a creche, qui est pour les
# moins de trois ans, au Portugal comme au Bresil). L'axe : ir a + l'article (à escola, ao jardim de infância), estar em
# (na escola, no jardim de infância), « ir buscar » au Portugal / « buscar » au Bresil, porque. Au Portugal l'article
# devant le prenom (o Ben, a Mia, a Katrin), au Bresil le prenom seul. Les leurres de « Vai ___ » ne proposent jamais
# « na » / « no » (le Bresil les dit pour le mouvement) ni « para a » (juste).
PT_LIEUX = {
    "escola": {"mot": "escola", "genre": "a", "nom": "a escola", "akk": "à escola", "dat": "na escola", "von": "da escola",
               "faux_akk": ["ao escola", "a a escola"], "faux_dat": ["no escola", "em a escola"],
               "trad": {"fr": ["l'école", "à l'école", "à l'école"], "en": ["the school", "to school", "from school"]}},
    "jardim": {"mot": "jardim de infância", "genre": "o", "nom": "o jardim de infância", "akk": "ao jardim de infância", "dat": "no jardim de infância",
               "von": "do jardim de infância", "faux_akk": ["à jardim de infância", "a o jardim de infância"], "faux_dat": ["na jardim de infância", "em o jardim de infância"],
               "trad": {"fr": ["le jardin d'enfants", "au jardin d'enfants", "au jardin d'enfants"], "en": ["the kindergarten", "to kindergarten", "from kindergarten"]}},
}
PT_ENFANTS = {"Ben": ["escola"], "Mia": ["jardim"]}
PT_AGES = {7: "sete", 4: "quatro"}


def _pt_action(id_, v, s, c, img, noms, faux, t_fr, t_en, **extra):
    """Une action portugaise : s et c portent deja les articles (o Ben, a Mia) ; « Portugal » et « Bresil » en paires."""
    a = {"id": id_, "v": v, "s": s, "c": c, "img": img, "noms": noms, "aussi_v": [], "t": {"fr": t_fr, "en": t_en}}
    if faux:
        a["faux_v"] = faux
    a.update(extra)
    return a


# (Portugal, Bresil) : le sujet, le complement et, pour « aller chercher », l'infinitif affiche (ir buscar / buscar)
_PT_ACT = [
    ("bringen_kita", "levar", ("A Katrin", "Katrin"), ("a Mia ao jardim de infância", "Mia ao jardim de infância"), "kita-bringen", [["jardim de infância", "o"]],
     ["escrever", "pintar", "brincar", "fazer"], "Katrin amène Mia au jardin d'enfants.", "Katrin takes Mia to kindergarten.", {}),
    ("bringen_schule", "levar", ("O Jan", "Jan"), ("o Ben à escola", "Ben à escola"), "schulweg", [["escola", "a"]],
     ["escrever", "pintar", "brincar", "fazer"], "Jan amène Ben à l'école.", "Jan takes Ben to school.", {}),
    ("abholen_kita", "buscar", ("O Mark", "Mark"), ("a Mia ao jardim de infância", "Mia no jardim de infância"), "kita-abholen", [["jardim de infância", "o"]],
     ["escrever", "pintar", "brincar", "fazer"], "Mark va chercher Mia au jardin d'enfants.", "Mark picks Mia up from kindergarten.", {"inf": ("ir buscar", "buscar")}),
    ("abholen_schule", "buscar", ("O Jan", "Jan"), ("o Ben à escola", "Ben na escola"), "schule-abholen", [["escola", "a"]],
     ["escrever", "pintar", "brincar", "fazer"], "Jan va chercher Ben à l'école.", "Jan picks Ben up from school.", {"inf": ("ir buscar", "buscar")}),
    ("anmelden", "inscrever", ("A Katrin", "Katrin"), ("a Mia no jardim de infância", "Mia no jardim de infância"), "anmelden", [["jardim de infância", "o"]],
     ["escrever", "pintar", "brincar"], "Katrin inscrit Mia au jardin d'enfants.", "Katrin registers Mia at the kindergarten.", {}),
    # « com a professora » : seuls des verbes qui ont besoin d'un complement direct (inscrever, buscar, arrumar), jamais
    # pintar, brincar, escrever, ir, qui iraient avec « com »
    ("sprechen", "falar", ("A Katrin", "Katrin"), ("com a professora", "com a professora"), "lehrerin", [["professora", "a"]],
     ["inscrever", "buscar", "arrumar"], "Katrin parle avec l'enseignante.", "Katrin talks to the teacher.", {}),
    ("anrufen", "ligar", ("A Katrin", "Katrin"), ("para a escola", "para a escola"), "krank", [["escola", "a"]],
     None, "Katrin appelle l'école.", "Katrin calls the school.", {}),
    ("krank", "estar", ("O Ben", "Ben"), ("doente", "doente"), "krank", [],
     None, "Ben est malade.", "Ben is ill.", {"adj": "doente", "etat": True}),
    ("packen", "arrumar", ("O Ben", "Ben"), ("a mochila", "a mochila"), "packen", [["mochila", "a"]],
     ["falar", "brincar", "ir", "escrever"], "Ben prépare son cartable.", "Ben packs his school bag.", {}),
    ("hausaufgaben", "fazer", ("O Ben", "Ben"), ("os trabalhos de casa", "o dever de casa"), "hausaufgaben", ([["trabalhos de casa", "os"]], [["dever de casa", "o"]]),
     ["falar", "ligar", "brincar", "ir"], "Ben fait ses devoirs.", "Ben does his homework.", {}),
    # « no caderno » : jamais buscar (au Bresil, chercher dans le cahier), inscrever (inscrire dedans), desenhar, pintar
    ("schreiben", "escrever", ("O Ben", "Ben"), ("no caderno", "no caderno"), "klasse", [["caderno", "o"]],
     ["ligar", "ir", "falar", "levar"], "Ben écrit dans son cahier.", "Ben writes in his exercise book.", {"aussi_v": ["desenhar", "pintar"]}),
    ("malen", "pintar", ("A Mia", "Mia"), ("no jardim de infância", "no jardim de infância"), "malen", [["jardim de infância", "o"]],
     None, "Mia peint au jardin d'enfants.", "Mia paints at kindergarten.", {"aussi_v": ["brincar", "desenhar", "escrever"]}),
    ("spielen", "brincar", ("O Ben", "Ben"), ("no recreio", "no recreio"), "pause", [["recreio", "o"]],
     None, "Ben joue pendant la récréation.", "Ben plays at break time.", {}),
    ("elternabend", "ir", ("O Jan e a Katrin", "Jan e Katrin"), ("à reunião de pais", "à reunião de pais"), "elternabend", [["reunião", "a"]],
     None, "Jan et Katrin vont à la réunion de parents.", "Jan and Katrin go to the parents' meeting.", {"pl": True}),
]


def pt_actions(br):
    out = []
    for id_, v, s, c, img, noms, faux, tf, te, extra in _PT_ACT:
        i = 1 if br else 0
        ex = {k: (x[i] if isinstance(x, tuple) else x) for k, x in extra.items()}
        out.append(_pt_action(id_, v, s[i], c[i], img, noms[i] if isinstance(noms, tuple) else noms, faux, tf, te, **ex))
    return out


PT_OBJETS = {
    "mochila": {"mot": "mochila", "genre": "a", "pl": "mochilas", "img": "ranzen", "proches": [], "liste": False,
                "trad": {"fr": ["le cartable", "cartables"], "en": ["the school bag", "school bags"]}},
    "estojo":  {"mot": "estojo", "genre": "o", "pl": "estojos", "img": "maeppchen", "proches": [],
                "trad": {"fr": ["la trousse", "trousses"], "en": ["the pencil case", "pencil cases"]}},
    "caderno": {"mot": "caderno", "genre": "o", "pl": "cadernos", "img": "heft", "proches": ["livro"],
                "trad": {"fr": ["le cahier", "cahiers"], "en": ["the exercise book", "exercise books"]}},
    "lapis":   {"mot": "lápis", "genre": "o", "pl": "lápis", "img": "bleistift", "proches": [],
                "trad": {"fr": ["le crayon", "crayons"], "en": ["the pencil", "pencils"]}},
    "regua":   {"mot": "régua", "genre": "a", "pl": "réguas", "img": "lineal", "proches": [],
                "trad": {"fr": ["la règle", "règles"], "en": ["the ruler", "rulers"]}},
    "borracha": {"mot": "borracha", "genre": "a", "pl": "borrachas", "img": "radiergummi", "proches": [],
                 "trad": {"fr": ["la gomme", "gommes"], "en": ["the eraser", "erasers"]}},
    "livro":   {"mot": "livro", "genre": "o", "pl": "livros", "img": "buch", "proches": ["caderno"],
                "trad": {"fr": ["le livre", "livres"], "en": ["the book", "books"]}},
    # une seule tesoura dans la liste (« uma tesoura »), comme die Schere
    "tesoura": {"mot": "tesoura", "genre": "a", "pl": "tesouras", "img": "schere", "proches": [],
                "trad": {"fr": ["les ciseaux", "paires de ciseaux"], "en": ["the scissors", "pairs of scissors"]}},
}
PT_NOMBRES = ["", "um", "dois", "três", "quatro", "cinco"]          # « duas » devant un nom feminin : la page
# l'horaire : au Portugal les disciplines du 1.º ciclo, au Bresil les materias des anos iniciais
PT_MATIERES = (
    {"deutsch": {"aff": "Português", "mot": None}, "mathe": {"aff": "Matemática", "mot": ["matemática", "a"]}, "sport": {"aff": "Educação Física", "mot": None},
     "kunst": {"aff": "Artes Visuais", "mot": None}, "musik": {"aff": "Música", "mot": ["música", "a"]},
     "sachunterricht": {"aff": "Estudo do Meio", "mot": None}, "englisch": {"aff": "Inglês", "mot": None}},
    {"deutsch": {"aff": "Português", "mot": None}, "mathe": {"aff": "Matemática", "mot": ["matemática", "a"]}, "sport": {"aff": "Educação Física", "mot": None},
     "kunst": {"aff": "Arte", "mot": None}, "musik": {"aff": "Música", "mot": ["música", "a"]},
     "sachunterricht": {"aff": "Ciências", "mot": None}, "englisch": {"aff": "Inglês", "mot": None}})
# LES VACANCES DE LISBONNE, 2026-2027 : PLAUSIBLES, PAS OFFICIELLES (le despacho du calendrier scolaire 2026/2027 n'a pas
# ete lu) -- d'apres le modele des annees precedentes : rentree la semaine du 14 sept. ; Natal du lundi 21 dec. au 1er janv.
# (reprise le lundi 4) ; Carnaval du lundi 8 au mercredi 10 fevr. (mardi gras le 9, Paques le 28 mars 2027) ; Pascoa du 22
# mars au 2 avril ; fin des cours du 1.º ciclo le 30 juin. A remplacer par les dates du despacho quand on l'aura.
FERIEN_PT = [["weihnachten", [21, 12, 2026], [1, 1, 2027]], ["carnaval", [8, 2, 2027], [10, 2, 2027]], ["ostern", [22, 3, 2027], [2, 4, 2027]], ["sommer", [1, 7, 2027], None]]
RENTREE_PT = [14, 9, 2026]
# les jours feries nationaux sans ecole, hors vacances : 5 out., 1 e 8 dez., Corpo de Deus (27 maio 2027), 10 junho ;
# 1 nov. 2026 et 13 junho 2027 (Santo António, Lisbonne) tombent un dimanche, 25 abril un dimanche, 1 maio un samedi
SANS_ECOLE_PT = ["5.10.2026", "1.12.2026", "8.12.2026", "27.5.2027", "10.6.2027"]
PT_FERIEN_NOMS = ({"weihnachten": "férias do Natal", "carnaval": "férias do Carnaval", "ostern": "férias da Páscoa", "sommer": "férias de verão"},
                  {"weihnachten": "férias de Natal", "carnaval": "recesso de Carnaval", "ostern": "recesso de Páscoa", "sommer": "férias de verão"})
PT_RAISONS = (
    {"krank": {"p": "Está doente.", "mots": [["doente", "adjectif"]], "t": {"fr": "Il est malade.", "en": "He is ill."}},
     "fieber": {"p": "Tem febre.", "mots": [["febre", "a"]], "t": {"fr": "Il a de la fièvre.", "en": "He has a temperature."}},
     "arzt": {"p": "Tem uma consulta no médico.", "mots": [["consulta", "a"], ["médico", "o"]], "t": {"fr": "Il a rendez-vous chez le médecin.", "en": "He has a doctor's appointment."}}},
    {"krank": {"p": "Está doente.", "mots": [["doente", "adjectif"]], "t": {"fr": "Il est malade.", "en": "He is ill."}},
     "fieber": {"p": "Está com febre.", "mots": [["febre", "a"]], "t": {"fr": "Il a de la fièvre.", "en": "He has a temperature."}},
     "arzt": {"p": "Tem consulta com o médico.", "mots": [["consulta", "a"], ["médico", "o"]], "t": {"fr": "Il a rendez-vous chez le médecin.", "en": "He has a doctor's appointment."}}})
PT_SALLES = ["sala 12", "sala 8", "sala 21"]
PT_SUJETS = (["a visita de estudo ao jardim zoológico", "a festa de Natal", "os trabalhos de casa", "as aulas de natação", "o passeio de fim de ano"],
             ["o passeio ao zoológico", "a festa de Natal", "o dever de casa", "as aulas de natação", "o passeio de fim de ano"])
PT_PAPIERS = (
    {"stundenplan": {"mot": "horário", "genre": "o", "aff": "um horário", "t": {"fr": "un emploi du temps", "en": "a timetable"}},
     "entschuldigung": {"mot": "justificação de faltas", "genre": "a", "aff": "uma justificação de faltas", "t": {"fr": "un mot d'absence", "en": "a note excusing an absence"}},
     "elternabend": {"mot": "reunião", "genre": "a", "aff": "um convite para a reunião de pais", "t": {"fr": "une invitation à la réunion de parents", "en": "an invitation to the parents' meeting"}},
     "ferien": {"mot": "férias", "genre": "as", "aff": "um calendário das férias", "t": {"fr": "un calendrier des vacances", "en": "a holiday calendar"}},
     "liste": {"mot": None, "genre": None, "aff": "uma lista de material", "t": {"fr": "une liste de fournitures", "en": "a list of school supplies"}}},
    {"stundenplan": {"mot": "horário", "genre": "o", "aff": "um horário", "t": {"fr": "un emploi du temps", "en": "a timetable"}},
     "entschuldigung": {"mot": "justificativa de falta", "genre": "a", "aff": "uma justificativa de falta", "t": {"fr": "un mot d'absence", "en": "a note excusing an absence"}},
     "elternabend": {"mot": "reunião", "genre": "a", "aff": "um convite para a reunião de pais", "t": {"fr": "une invitation à la réunion de parents", "en": "an invitation to the parents' meeting"}},
     "ferien": {"mot": "férias", "genre": "as", "aff": "um calendário de férias", "t": {"fr": "un calendrier des vacances", "en": "a holiday calendar"}},
     "liste": {"mot": None, "genre": None, "aff": "uma lista de material", "t": {"fr": "une liste de fournitures", "en": "a list of school supplies"}}})
# des noms inventes (pas une vraie ecole de Lisbonne) : Dente-de-Leão = Pusteblume, « do Bairro » = am Kiez
PT_NOMS = ({"kita": "Jardim de Infância Dente-de-Leão", "schule": "Escola Básica do Bairro", "lehrerin": "a professora Teresa", "erzieherin": "a educadora Rita",
            "klasse": "2.º B", "turma": "Turma 2.º B", "daTurma": "da turma 2.º B", "grupo": "Sala das Joaninhas"},
           {"kita": "Jardim de Infância Dente-de-Leão", "schule": "Escola Básica do Bairro", "lehrerin": "a professora Teresa", "erzieherin": "a professora Rita",
            "klasse": "2º ano B", "turma": "2º ano B", "daTurma": "do 2º ano B", "grupo": "Turma Joaninha"})
# le corpus portugais n'a que le francais : l'anglais des mots du theme, ici
PT_EN = {"escola": "school", "jardim de infância": "kindergarten", "levar": "to take, to bring", "buscar": "to pick up, to fetch",
         "inscrever": "to register, to enrol", "falar": "to speak, to talk", "professora": "teacher (woman)", "ligar": "to call (on the phone)",
         "doente": "ill, sick", "arrumar": "to tidy, to pack", "mochila": "backpack, school bag", "fazer": "to do, to make",
         "trabalhos de casa": "homework", "dever de casa": "homework", "escrever": "to write", "caderno": "exercise book",
         "pintar": "to paint", "brincar": "to play (children)", "recreio": "break time", "ir": "to go", "reunião": "meeting",
         "estojo": "pencil case", "lápis": "pencil", "régua": "ruler", "borracha": "eraser", "livro": "book", "tesoura": "scissors",
         "matemática": "maths", "música": "music", "febre": "fever, temperature", "consulta": "appointment (doctor)", "médico": "doctor",
         "horário": "timetable", "justificação de faltas": "note excusing an absence", "justificativa de falta": "note excusing an absence",
         "férias": "holidays", "faltar": "to be absent, to miss", "aula": "lesson, class"}
# LES MOTS ABSENTS DU CORPUS PORTUGAIS (a ajouter : portugais/outils) : leur traduction francaise, en attendant
PT_AJOUTS_FR = {"buscar": "aller chercher (au Portugal : ir buscar)", "ligar": "appeler (au téléphone)", "trabalhos de casa": "devoirs",
                "dever de casa": "devoirs", "recreio": "récréation", "justificação de faltas": "mot d'absence", "férias": "vacances"}
# les verbes absents du corpus : leur present (au Portugal « ir buscar », au Bresil « buscar »)
PT_CONJ_AJOUTS = ({"buscar": {"er": "vai buscar", "ich": "vou buscar", "du": "vais buscar", "pl": "vão buscar"},
                   "ligar": {"er": "liga", "ich": "ligo", "du": "ligas", "pl": "ligam"}},
                  {"buscar": {"er": "busca", "ich": "busco", "du": "buscas", "pl": "buscam"},
                   "ligar": {"er": "liga", "ich": "ligo", "du": "ligas", "pl": "ligam"}})


def corpus_pt(br):
    """(noms {(mot, genre): entree}, verbes {infinitif: entree}, adjectifs {mot: entree}) du corpus portugais."""
    dos = os.path.join(RACINE, "portugais", "datos-br" if br else "datos")
    noms = {}
    for t in json.load(io.open(os.path.join(dos, "themes.json"), encoding="utf-8"))["themes"]:
        for m in t["mots"]:
            noms.setdefault((m["mot"], m.get("genre")), m)
    lis = lambda f, cle: {e.get(cle) or e.get("mot"): e for l in json.load(io.open(os.path.join(dos, f), encoding="utf-8")).values() if isinstance(l, list) for e in l}
    return noms, lis("verbes.json", "infinitif"), lis("adjectifs.json", "mot")


def mots_du_theme_pt(br):
    """Comme mots_du_theme, pour le portugais appris : la forme du corpus (Portugal ou Bresil), le francais du corpus et
    l'anglais de PT_EN ; un mot absent garde PT_AJOUTS_FR et va dans la liste des absents."""
    i = 1 if br else 0
    noms, verbes, adjs = corpus_pt(br)
    mots, absents = [], []

    def ajouter(mot, genre=None, cat=None):
        if any(m["mot"] == mot and m.get("genre") == genre and m.get("cat") == cat for m in mots):
            return
        e = verbes.get(mot) if cat == "verbe" else adjs.get(mot) if cat == "adjectif" else noms.get((mot, genre))
        if e:
            fr = e.get("traduction")
        elif mot in PT_AJOUTS_FR:
            fr = PT_AJOUTS_FR[mot]; absents.append(mot)
        else:
            sys.exit("  %s (%s) absent du corpus portugais%s et des ajouts" % (mot, genre or cat, " (Bresil)" if br else ""))
        if mot not in PT_EN:
            sys.exit("  %s : pas d'anglais dans PT_EN" % mot)
        w = {"mot": mot, "g": {"fr": fr, "en": PT_EN[mot]}}
        if genre: w["genre"] = genre
        if cat: w["cat"] = cat
        mots.append(w)
    for l in PT_LIEUX.values():
        ajouter(l["mot"], l["genre"])
    for a in pt_actions(br):
        if a["v"] != "estar":
            ajouter(a["v"], cat="verbe")
        for n, g in a["noms"]:
            ajouter(n, g)
        if a.get("adj"):
            ajouter(a["adj"], cat="adjectif")
    for o in PT_OBJETS.values():
        ajouter(o["mot"], o["genre"])
    for m in PT_MATIERES[i].values():
        if m["mot"]:
            ajouter(*m["mot"])
    for r in PT_RAISONS[i].values():
        for n, g in r["mots"]:
            ajouter(n, None, "adjectif") if g == "adjectif" else ajouter(n, g)
    for p in PT_PAPIERS[i].values():
        if p["mot"]:
            ajouter(p["mot"], p["genre"])
    ajouter("faltar", cat="verbe")
    ajouter("professora", "a")
    ajouter("recreio", "o")
    ajouter("aula", "a")              # « o Ben tem aulas » : le calendrier des vacances
    return mots, sorted(set(absents))


def conjugaisons_pt(br):
    _, verbes, _ = corpus_pt(br)
    out = {}
    for a in pt_actions(br):
        if a["v"] in PT_CONJ_AJOUTS[1 if br else 0]:
            out[a["v"]] = PT_CONJ_AJOUTS[1 if br else 0][a["v"]]
            continue
        e = verbes.get(a["v"])
        if not e:
            sys.exit("  verbe portugais absent : %s" % a["v"])
        p = e["praesens"]
        out[a["v"]] = {"er": p["er_sie_es"], "ich": p["ich"], "du": p["du"], "pl": p["sie_Sie"]}
    return out


def verifier_pt():
    for br in (False, True):
        acts = pt_actions(br)
        if [a["id"] for a in acts] != [a["id"] for a in ACTIONS["de"]]:
            sys.exit("  les actions pt ne sont pas dans l'ordre de l'allemand")
        for a in acts:
            if a["img"] not in IMAGES:
                sys.exit("  image inconnue : %s" % a["img"])
            if any(l not in a["t"] for l in ("fr", "en")):
                sys.exit("  pt %s : traduction absente" % a["id"])
            # un leurre de verbe n'est jamais le verbe juste ni un verbe qui irait aussi
            if set(a.get("faux_v", [])) & ({a["v"]} | set(a["aussi_v"])):
                sys.exit("  pt %s : un leurre est une reponse possible" % a["id"])
        for e, ks in PT_ENFANTS.items():
            for k in ks:
                if k not in PT_LIEUX:
                    sys.exit("  lieu portugais inconnu : %s" % k)
        for k, l in PT_LIEUX.items():
            # « Vai ___ » : jamais « na » / « no » (le Bresil les dit pour le mouvement) ni « para a » (juste)
            if any(f.split(" ")[0] in ("na", "no", "para") for f in l["faux_akk"]):
                sys.exit("  %s : un leurre de « vai ___ » serait dit au Bresil" % k)


def portugais(d):
    """Pose pt_ / br_ dans la donnee construite (ecrire_json), a cote de de et es."""
    def poser(o, pt, br=None):
        o["pt_"] = pt
        if br is not None and br != pt:
            o["br_"] = br
    poser(d["lieux"], PT_LIEUX)
    for e, ks in PT_ENFANTS.items():
        poser(d["enfants"][e], ks)
    poser(d["ages"], PT_AGES)
    poser(d["actions"], pt_actions(False), pt_actions(True))
    poser(d["objets"], PT_OBJETS)
    poser(d["nombres"], PT_NOMBRES)
    poser(d["matieres"], *PT_MATIERES)
    poser(d["jours"], JOURS["pt"]); poser(d["mois"], MOIS["pt"]); poser(d["ordinaux"], ORDINAUX["pt"])
    d["ferienPt"], d["rentreePt"], d["sansEcolePt"] = FERIEN_PT, RENTREE_PT, SANS_ECOLE_PT
    # la traduction de « Português » (la matiere « deutsch » de l'horaire) : le portugais, pas l'allemand
    d["matieresTradPt"] = {"deutsch": {"fr": "portugais", "en": "Portuguese"}}
    poser(d["ferienNoms"], *PT_FERIEN_NOMS)
    poser(d["raisons"], *PT_RAISONS)
    poser(d["elternabend"]["salles"], PT_SALLES)
    poser(d["elternabend"]["sujets"], *PT_SUJETS)
    poser(d["papiers"], *PT_PAPIERS)
    poser(d["noms"], *PT_NOMS)
    for cle, br in (("pt_", False), ("br_", True)):
        d["mots"][cle], d["absents"][cle] = mots_du_theme_pt(br)
        d["conj"][cle] = conjugaisons_pt(br)


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def corpus_noms(langue):
    f = "themes.json" if langue == "de" else "espanol/datos/temas.json"
    out = {}
    for t in json.load(io.open(os.path.join(RACINE, f), encoding="utf-8"))["themes"]:
        for m in t["mots"]:
            out.setdefault((m["mot"], m.get("genre")), m)
    return out


def corpus_liste(fichier, cle):
    out = {}
    for niv, l in json.load(io.open(os.path.join(RACINE, fichier), encoding="utf-8")).items():
        if isinstance(l, list):
            for e in l:
                out.setdefault(e.get(cle) or e.get("mot"), e)
    return out


def glose(e, l):
    return e.get("traduction" if l == "fr" else "traduction_" + l)


def mots_du_theme(langue):
    """Les mots que le theme fait travailler, a la forme du corpus, et leur traduction (le corpus, sinon AJOUTS_TRAD)."""
    noms = corpus_noms(langue)
    verbes = corpus_liste("verbe.json" if langue == "de" else "espanol/datos/verbos.json", "infinitif")
    adjs = corpus_liste("adjectif.json" if langue == "de" else "espanol/datos/adjetivos.json", "mot")
    mots, absents = [], []

    def ajouter(mot, genre=None, cat=None):
        if any(m["mot"] == mot and m.get("genre") == genre and m.get("cat") == cat for m in mots):
            return
        e = verbes.get(mot) if cat == "verbe" else adjs.get(mot) if cat == "adjectif" else noms.get((mot, genre))
        if e:
            g = {l: glose(e, l) for l in LANGUES[langue]}
        elif mot in AJOUTS_TRAD[langue]:
            g = AJOUTS_TRAD[langue][mot]; absents.append(mot)
        else:
            sys.exit("  %s (%s) absent du corpus %s et des ajouts" % (mot, genre or cat, langue))
        manque = [l for l in LANGUES[langue] if not g.get(l)]
        if manque:
            sys.exit("  %s (%s) : pas de traduction en %s" % (mot, langue, ", ".join(manque)))
        w = {"mot": mot, "g": g}
        if genre: w["genre"] = genre
        if cat: w["cat"] = cat
        mots.append(w)
    for l in LIEUX[langue].values():
        ajouter(l["mot"], l["genre"])
    for a in ACTIONS[langue]:
        if a["v"] not in ("sein", "estar"):
            ajouter(a["v"], cat="verbe")
        for n, g in a["noms"]:
            ajouter(n, g)
        if a.get("adj"):
            ajouter(a["adj"], cat="adjectif")
    for o in OBJETS[langue].values():
        ajouter(o["mot"], o["genre"])
    for m in MATIERES[langue].values():
        if m["mot"]:
            ajouter(*m["mot"])
    for r in RAISONS[langue].values():
        for n, g in r["mots"]:
            ajouter(n, None, "adjectif") if g == "adjectif" else ajouter(n, g)
    for p in PAPIERS[langue].values():
        if p["mot"]:
            ajouter(p["mot"], p["genre"])
    ajouter("fehlen" if langue == "de" else "faltar", cat="verbe")          # le mot d'absence : « Ben fehlt am Montag »
    ajouter("Lehrerin" if langue == "de" else "profesora", "die" if langue == "de" else "la")
    ajouter("Pause" if langue == "de" else "recreo", "die" if langue == "de" else "el")
    return mots, sorted(set(absents))


def conjugaisons(langue):
    """Le present de chaque verbe (corpus) : 3e du singulier et du pluriel, et le reste pour les leurres."""
    verbes = corpus_liste("verbe.json" if langue == "de" else "espanol/datos/verbos.json", "infinitif")
    out = {}
    for a in ACTIONS[langue]:
        e = verbes.get(a["v"])
        if not e:
            if a["v"] == "matricular":            # absent du corpus (ajout propose) : regulier en -ar
                p = {"ich": "matriculo", "du": "matriculas", "er_sie_es": "matricula", "wir": "matriculamos", "ihr": "matriculáis", "sie_Sie": "matriculan"}
            else:
                sys.exit("  verbe absent : %s" % a["v"])
        else:
            p = e["praesens"]
        out[a["v"]] = {"er": p["er_sie_es"], "ich": p["ich"], "du": p["du"], "pl": p["sie_Sie"]}
    return out


def verifier():
    for langue in ("de", "es"):
        need = ["fr", "en", "pt"] + (["de"] if langue == "es" else [])
        ids = [a["id"] for a in ACTIONS[langue]]
        if ids != [a["id"] for a in ACTIONS["de"]]:
            sys.exit("  les actions de et es ne sont pas dans le meme ordre")
        for a in ACTIONS[langue]:
            if a["img"] not in IMAGES:
                sys.exit("  image inconnue : %s" % a["img"])
            manque = [l for l in need if l not in a["t"]]
            if manque:
                sys.exit("  %s %s : traduction absente (%s)" % (langue, a["id"], manque))
        for o in OBJETS[langue].values():
            if o["img"] not in IMAGES and o["img"] not in ("maeppchen", "heft", "bleistift", "lineal", "radiergummi", "buch", "schere"):
                sys.exit("  image d'objet inconnue : %s" % o["img"])
        for e in ENFANTS.values():
            for k in e[langue]:
                if k not in LIEUX[langue]:
                    sys.exit("  lieu inconnu : %s" % k)


def ecrire_json():
    verifier()
    d = {"lieux": LIEUX, "enfants": ENFANTS, "ages": AGES, "actions": ACTIONS, "objets": OBJETS, "nombres": NOMBRES,
         "heures": HEURES, "pause": PAUSE, "matieres": MATIERES, "matieresTrad": MATIERES_TRAD, "horaire": HORAIRE,
         "jours": JOURS, "mois": MOIS, "ordinaux": ORDINAUX, "ferien": FERIEN, "ferienEs": FERIEN_ES, "rentreeEs": RENTREE_ES, "sansEcoleEs": SANS_ECOLE_ES, "ferienNoms": FERIEN_NOMS, "raisons": RAISONS,
         "elternabend": ELTERNABEND, "abholer": ABHOLER, "abholHeures": ABHOL_HEURES, "papiers": PAPIERS, "noms": NOMS_ECOLE,
         "mots": {}, "absents": {}, "conj": {}}
    for langue in ("de", "es"):
        d["mots"][langue], d["absents"][langue] = mots_du_theme(langue)
        d["conj"][langue] = conjugaisons(langue)
    verifier_pt()
    portugais(d)
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    chemin = os.path.join(RACINE, "visuel", "prototype", "ecole", "ecole.json")
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(texte)
    for langue in ("de", "es", "pt_", "br_"):
        print("  %s : %d mots, dont %d absents du corpus (%s)" % (langue, len(d["mots"][langue]), len(d["absents"][langue]), ", ".join(d["absents"][langue])))
    return d


def images():
    out = {}
    for i, im in IMAGES.items():
        if im.get("existe"):
            continue
        refs = [SOURCES[p] for p in im["qui"]]
        if im.get("lieu"):
            refs.append(SOURCES[im["lieu"]] if im["lieu"] in SOURCES else os.path.join(DOSSIER, im["lieu"] + ".png"))
        qui = "".join("%s. " % QUI[p].replace("{n}", str(i + 1)) for i, p in enumerate(im["qui"]))
        if im.get("lieu"):
            qui += "Reference picture %d is only for the place (the room, its furniture and colours, the light). " % (len(im["qui"]) + 1)
        photo = PHOTO if im["qui"] else PHOTO.replace("Hands: five fingers each, natural. The children are calm or smiling, relaxed and happy.", "No people and no hands in the picture: the objects alone.")
        out[i] = (refs, ("In this picture: " + qui if qui else "") + im["prompt"] + photo)
    return out


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    ecrire_json()
    if "--json" in sys.argv:
        return
    tout = images()
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
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if montrer:
        for nom in a_faire:
            print("\n  %s (%d reference(s))\n  %s" % (nom, len(tout[nom][0]), tout[nom][1]))
        return
    import omnihuman as O                                    # noqa: E402
    if not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    for nom in a_faire:
        refs, prompt = images()[nom]                         # refait : un lieu genere plus tot dans la meme passe existe maintenant
        manque = [r for r in refs if not os.path.exists(r)]
        if manque:
            print("  %s : reference absente (%s), passe" % (nom, ", ".join(manque)))
            continue
        print("\n  %s (%d reference(s))\n  %s" % (nom, len(refs), prompt))
        corps = {"prompt": prompt, "aspect_ratio": "4:3", "resolution": "2K", "output_format": "png", "num_images": 1}
        modele = TEXTE
        if refs:
            corps["image_urls"] = [O.deposer(r, "image/png", cle)[0] for r in refs]
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
            "prompt": prompt, "refs": refs, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
