# -*- coding: utf-8 -*-
"""Les fetes et les invitations, theme illustre de la vague 4 (decision de Jacques du 5 nov. 2026, « go » sur la liste
des quatre : le travail, l'ecole, les fetes, les vacances). En allemand ET en espagnol ; en portugais depuis le lot P4
(12 nov. 2026, Lisbonne, Portugal et Bresil : FETES_PT et la suite, plus bas).

    python visuel/fetes/fetes.py --json             # fetes.json seul, gratuit
    python visuel/fetes/fetes.py --montrer          # les prompts seuls, gratuit
    python visuel/fetes/fetes.py --essai            # la planche d'essai (6 images, 0,90 $) -- ACCORD DE JACQUES
    python visuel/fetes/fetes.py ostern silvester   # celles-la seulement (0,15 $ chacune)
    python visuel/fetes/fetes.py --refaire ostern   # l'ancienne passe en <nom>-rate<k>.png

L'ANGLE (regle 2 des themes : pas de scene refaite). La scene « Marks Geburtstag » enseigne les OBJETS de la fete (la
Torte, die Kerze, der Luftballon, das Geschenk) ; celle du Weihnachtsmarkt, les objets du marche. Le theme enseigne ce
qu'on FAIT autour d'une fete : reconnaitre la fete et sa date, souhaiter (Frohe Weihnachten ; ¡Feliz Navidad!), lire
une invitation, accepter ou refuser poliment selon son agenda (Ich komme gern / Leider kann ich nicht ; con mucho gusto
/ lo siento, no puedo), proposer un jour, se mettre d'accord, dire qui apporte quoi. C'est la troisieme partie de l'oral
du DTZ, « gemeinsam etwas planen » : proposer, reagir, se mettre d'accord (le FORMAT seulement, visuel/prototype/
dtz-oral.html ; aucun contenu d'examen n'est repris).

LES DEUX MONDES. Les images sont les memes, sans texte ; les invitations, les agendas et la liste « qui apporte quoi »
sont dessines en HTML par la page, avec les personnes de chaque langue :
  - en allemand, Mark (de Montreal, Gartenstrasse 12 a Pankow, ne le 14 mars 2001) et la famille d'Anna (Anna sans
    compagnon ni enfant ; Jan et Katrin, parents de Ben, 7 ans, et de Mia ; Lena ; Felix et Sophie, les cousins ;
    Heinz et Gisela, les grands-parents). Anna habite le Kiez de Mark depuis son emmenagement (la scene umzug) : d'ou
    son Einweihungsparty ;
  - en espagnol, Mark a Madrid (calle de la Luna 12, comme « Les demarches ») et les personnes de « Decrire une
    personne » (Ines, Javier, Carmen, Tomas, Elena, Diego, Marta).
Une image qui montre une personne nommee n'est jamais dans une question qui la nomme autrement.

LES PHRASES SONT FABRIQUEES par la page (fetes.html) a partir de ces tables, jamais ecrites une a une. Un leurre n'est
jamais une reponse possible : chaque fete dit quelles autres fetes son image montre aussi (« aussi »), chaque date se
compare jour par jour (« jours ») et deux periodes qui se touchent ne sont jamais proposees l'une pour l'autre ; un
agenda ne propose jamais un motif qui n'y est pas ; un rendez-vous chez le medecin ne tombe jamais un dimanche.

Images : fal, nano-banana-pro, 0,15 $ l'image. Mark, Anna, Lena, Felix, Ben, Mia, Carmen, Javier et Ines ne se
regenerent jamais : retouches de leurs images. Le salon de Jan et Katrin reprend le maitre du « chat » (video/LIEUX.md).
Pas d'enfant triste, pas d'alcool. Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/fetes/img/.
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))

TEXTE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "fetes", "img")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
DESCR = "C:/Users/jacqu/.wortando/wt-themes/visuel/descripcion/img"
REFERENCES = {"Mark": PRINCIPAL + "/personnages/Mark.png", "Anna": FAMILLE + "/Anna-quotidien.png",
              "Lena": FAMILLE + "/Lena.png", "Felix": FAMILLE + "/Felix.png", "Ben": FAMILLE + "/Ben.png", "Mia": FAMILLE + "/Mia.png",
              "Carmen": DESCR + "/Carmen.png", "Javier": DESCR + "/Javier.png", "Ines": DESCR + "/Ines.png",
              # les lieux deja photographies (video/LIEUX.md) : le salon de Jan et Katrin (le chat), la cuisine de Mark
              "salon-jan-katrin": os.path.join(os.path.expanduser("~"), ".wortando", "meteo", "ref", "salon-jan-katrin.png"),
              "cuisine-mark": RACINE + "/visuel/prototype/kueche.webp"}

LANGUES = {"es": ["fr", "en", "pt", "ar", "de"], "de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]}
# les langues des phrases traduites en entier (les autres : le mot et sa glose du corpus)
TL = {"de": ["fr", "en", "pt"], "es": ["fr", "en", "pt", "de"]}

# ---------------------------------------------------------------------------------------------------------------
# LES FETES. mot / genre : la forme du corpus (le mot que la question fait avancer) ; nom : comment la fete s'ecrit
# dans une phrase et sur un bouton (« Weihnachten », « la Navidad ») ; quand : la date dite ; jours : les jours qu'elle
# couvre (MM-JJ, « 12 » = tout le mois) pour juger un leurre ; wunsch : le souhait ; aussi : les fetes qu'une meme
# image ou un meme souhait peut aussi dire (jamais en leurre) ; img : les images qui la montrent ; t : {langue: [le
# nom, la date]} ; latam : seulement avec variante=latam ; zu (de) : la contraction de « Glueckwunsch zum / zur ».
FETES = {
    "de": {
        "geburtstag": {"mot": "Geburtstag", "genre": "der", "nom": "Geburtstag", "wunsch": "Herzlichen Glückwunsch zum Geburtstag!", "zu": "zum",
                       "img": ["geburtstag", "kindergeburtstag"],
                       "t": {"fr": ["un anniversaire", None, "Joyeux anniversaire !"], "en": ["a birthday", None, "Happy birthday!"], "pt": ["um aniversário", None, "Feliz aniversário!"]}},
        "weihnachten": {"mot": "Weihnachten", "genre": "das", "nom": "Weihnachten", "quand": "im Dezember", "jours": ["12"], "wunsch": "Frohe Weihnachten!",
                        "img": ["weihnachten", "weihnachtsmarkt"],
                        "t": {"fr": ["Noël", "en décembre", "Joyeux Noël !"], "en": ["Christmas", "in December", "Merry Christmas!"], "pt": ["o Natal", "em dezembro", "Feliz Natal!"]}},
        "silvester":   {"mot": "Silvester", "genre": "das", "nom": "Silvester", "quand": "am 31. Dezember", "jours": ["12-31"], "wunsch": "Guten Rutsch ins neue Jahr!",
                        "aussi": ["neujahr"], "img": ["silvester"],
                        "t": {"fr": ["la Saint-Sylvestre", "le 31 décembre", "Bonne fin d'année !"], "en": ["New Year's Eve", "on December 31", "Have a good start to the new year!"],
                              "pt": ["o Réveillon", "em 31 de dezembro", "Boas entradas!"]}},
        "neujahr":     {"mot": "Neujahr", "genre": "das", "nom": "Neujahr", "quand": "am 1. Januar", "jours": ["01-01"], "wunsch": "Frohes neues Jahr!",
                        "aussi": ["silvester"], "img": [],
                        "t": {"fr": ["le jour de l'An", "le 1er janvier", "Bonne année !"], "en": ["New Year's Day", "on January 1", "Happy New Year!"], "pt": ["o Ano-Novo", "em 1º de janeiro", "Feliz Ano-Novo!"]}},
        "ostern":      {"mot": "Ostern", "genre": "das", "nom": "Ostern", "quand": "im März oder April", "jours": ["03", "04"], "wunsch": "Frohe Ostern!",
                        "img": ["ostern"],
                        "t": {"fr": ["Pâques", "en mars ou en avril", "Joyeuses Pâques !"], "en": ["Easter", "in March or April", "Happy Easter!"], "pt": ["a Páscoa", "em março ou abril", "Feliz Páscoa!"]}},
        "karneval":    {"mot": "Karneval", "genre": "der", "nom": "Karneval", "img": ["karneval"],
                        "t": {"fr": ["le carnaval", None, None], "en": ["carnival", None, None], "pt": ["o Carnaval", None, None]}},
        "hochzeit":    {"mot": "Hochzeit", "genre": "die", "nom": "Hochzeit", "wunsch": "Herzlichen Glückwunsch zur Hochzeit!", "zu": "zur", "img": ["hochzeit"],
                        "t": {"fr": ["un mariage", None, "Félicitations pour votre mariage !"], "en": ["a wedding", None, "Congratulations on your wedding!"], "pt": ["um casamento", None, "Parabéns pelo casamento!"]}},
        "muttertag":   {"mot": "Muttertag", "genre": "der", "nom": "Muttertag", "quand": "im Mai", "jours": ["05"], "wunsch": "Alles Gute zum Muttertag!", "zu": "zum", "img": [],
                        "t": {"fr": ["la fête des Mères", "en mai", "Bonne fête, maman !"], "en": ["Mother's Day", "in May", "Happy Mother's Day!"], "pt": ["o Dia das Mães", "em maio", "Feliz Dia das Mães!"]}},
    },
    "es": {
        "cumpleanos":  {"mot": "cumpleaños", "genre": "el", "nom": "el cumpleaños", "wunsch": "¡Feliz cumpleaños!", "img": ["geburtstag", "kindergeburtstag"],
                        "t": {"fr": ["un anniversaire", None, "Joyeux anniversaire !"], "en": ["a birthday", None, "Happy birthday!"], "pt": ["um aniversário", None, "Feliz aniversário!"],
                              "de": ["ein Geburtstag", None, "Herzlichen Glückwunsch zum Geburtstag!"]}},
        "navidad":     {"mot": "Navidad", "genre": "la", "nom": "la Navidad", "quand": "el 25 de diciembre", "jours": ["12-25"], "wunsch": "¡Feliz Navidad!",
                        "img": ["weihnachten", "weihnachtsmarkt"],
                        "t": {"fr": ["Noël", "le 25 décembre", "Joyeux Noël !"], "en": ["Christmas", "on December 25", "Merry Christmas!"], "pt": ["o Natal", "em 25 de dezembro", "Feliz Natal!"],
                              "de": ["Weihnachten", "am 25. Dezember", "Frohe Weihnachten!"]}},
        "nochevieja":  {"mot": "Nochevieja", "genre": "la", "nom": "la Nochevieja", "quand": "el 31 de diciembre", "jours": ["12-31"], "wunsch": "¡Feliz Año Nuevo!",
                        "aussi": ["anonuevo"], "img": ["silvester", "uvas"],
                        "t": {"fr": ["la Saint-Sylvestre", "le 31 décembre", "Bonne année !"], "en": ["New Year's Eve", "on December 31", "Happy New Year!"],
                              "pt": ["o Réveillon", "em 31 de dezembro", "Feliz Ano-Novo!"], "de": ["Silvester", "am 31. Dezember", "Frohes neues Jahr!"]}},
        "anonuevo":    {"mot": "Año Nuevo", "genre": "el", "nom": "el Año Nuevo", "quand": "el 1 de enero", "jours": ["01-01"], "wunsch": "¡Feliz Año Nuevo!",
                        "aussi": ["nochevieja"], "img": [],
                        "t": {"fr": ["le jour de l'An", "le 1er janvier", "Bonne année !"], "en": ["New Year's Day", "on January 1", "Happy New Year!"],
                              "pt": ["o Ano-Novo", "em 1º de janeiro", "Feliz Ano-Novo!"], "de": ["Neujahr", "am 1. Januar", "Frohes neues Jahr!"]}},
        "reyes":       {"mot": "Día de Reyes", "genre": "el", "nom": "el Día de Reyes", "quand": "el 6 de enero", "jours": ["01-06"], "wunsch": "¡Feliz Día de Reyes!", "img": ["reyes"],
                        "t": {"fr": ["l'Épiphanie (les Rois mages)", "le 6 janvier", "Bonne fête des Rois !"], "en": ["Three Kings' Day", "on January 6", "Happy Three Kings' Day!"],
                              "pt": ["o Dia de Reis", "em 6 de janeiro", "Feliz Dia de Reis!"], "de": ["der Dreikönigstag", "am 6. Januar", "Einen schönen Dreikönigstag!"]}},
        "semanasanta": {"mot": "Semana Santa", "genre": "la", "nom": "la Semana Santa", "quand": "en marzo o abril", "jours": ["03", "04"], "img": ["semanasanta"],
                        "t": {"fr": ["la Semaine sainte", "en mars ou en avril", None], "en": ["Holy Week", "in March or April", None],
                              "pt": ["a Semana Santa", "em março ou abril", None], "de": ["die Karwoche", "im März oder April", None]}},
        "carnaval":    {"mot": "carnaval", "genre": "el", "nom": "el carnaval", "img": ["karneval"],
                        "t": {"fr": ["le carnaval", None, None], "en": ["carnival", None, None], "pt": ["o Carnaval", None, None], "de": ["der Karneval", None, None]}},
        "boda":        {"mot": "boda", "genre": "la", "nom": "la boda", "wunsch": "¡Felicidades a los novios!", "img": ["hochzeit"],
                        "t": {"fr": ["un mariage", None, "Félicitations aux mariés !"], "en": ["a wedding", None, "Congratulations to the happy couple!"],
                              "pt": ["um casamento", None, "Parabéns aos noivos!"], "de": ["eine Hochzeit", None, "Herzlichen Glückwunsch dem Brautpaar!"]}},
        "muertos":     {"mot": "Día de Muertos", "genre": "el", "nom": "el Día de Muertos", "quand": "el 1 y el 2 de noviembre", "jours": ["11-01", "11-02"], "img": ["muertos"], "latam": True,
                        "t": {"fr": ["le jour des Morts (au Mexique)", "le 1er et le 2 novembre", None], "en": ["the Day of the Dead", "on November 1 and 2", None],
                              "pt": ["o Dia dos Mortos", "em 1º e 2 de novembro", None], "de": ["der Tag der Toten", "am 1. und 2. November", None]}},
    },
}
# les images que la page montre et ce qu'elles montrent, par langue (une image d'une seule langue : absente de l'autre)
IMG_LANGUES = {"ostern": ["de"], "uvas": ["es"], "reyes": ["es"], "semanasanta": ["es"], "muertos": ["es"]}
# dans : « Zu Ostern sagt man ... » / « En Navidad se dice ... » ; c : une fete qu'on compte (« Das ist EIN Geburtstag. »,
# « Es UNA boda. ») ; situation : la phrase qui pose le souhait (« Heute ist Ostern. ») -- {P} une personne, ihr / ihm
for _l, _d in {"de": {"geburtstag": ("Zum Geburtstag", True, "{P} hat heute Geburtstag."), "weihnachten": ("Zu Weihnachten", False, "Heute ist Weihnachten."),
                      "silvester": ("An Silvester", False, "Heute ist Silvester."), "neujahr": ("An Neujahr", False, "Heute ist Neujahr."),
                      "ostern": ("Zu Ostern", False, "Heute ist Ostern."), "karneval": (None, False, None),
                      "hochzeit": ("Zur Hochzeit", True, "Deine Kollegin heiratet heute."), "muttertag": ("Zum Muttertag", False, "Heute ist Muttertag.")},
               "es": {"cumpleanos": ("En un cumpleaños", True, "Hoy es el cumpleaños de {P}."), "navidad": ("En Navidad", False, "Hoy es Navidad."),
                      "nochevieja": ("En Nochevieja", False, "Hoy es Nochevieja."), "anonuevo": ("En Año Nuevo", False, "Hoy es Año Nuevo."),
                      "reyes": ("El Día de Reyes", False, "Hoy es el Día de Reyes."), "semanasanta": (None, False, None), "carnaval": (None, False, None),
                      "boda": ("En una boda", True, "Tu compañera de trabajo se casa hoy."), "muertos": (None, False, None)}}.items():
    for _k, (_dans, _c, _sit) in _d.items():
        FETES[_l][_k].update({"dans": _dans, "c": _c, "situation": _sit})
# les traductions de la situation : {P} la personne
SITUATIONS_T = {"de": {"geburtstag": {"fr": "C'est l'anniversaire de {P} aujourd'hui.", "en": "It's {P}'s birthday today.", "pt": "Hoje é o aniversário de {P}."},
                       "hochzeit": {"fr": "Ta collègue se marie aujourd'hui.", "en": "Your colleague is getting married today.", "pt": "Sua colega se casa hoje."}},
                "es": {"cumpleanos": {"fr": "C'est l'anniversaire de {P} aujourd'hui.", "en": "It's {P}'s birthday today.", "pt": "Hoje é o aniversário de {P}.", "de": "{P} hat heute Geburtstag."},
                       "boda": {"fr": "Ta collègue se marie aujourd'hui.", "en": "Your colleague is getting married today.", "pt": "Sua colega de trabalho se casa hoje.", "de": "Deine Kollegin heiratet heute."}}}
# le sexe des personnes qui n'apparaissent que comme hotes (« Gisela und Heinz »)
SEXE = {"Gisela": "f", "Heinz": "m", "Ben": "m"}

# ---------------------------------------------------------------------------------------------------------------
# LES PERSONNES de chaque monde (s : le sexe, pour lieber / liebe, querido / querida, obrigado / obrigada).
PERSONNES = {
    "de": {"Mark": "m", "Anna": "f", "Lena": "f", "Felix": "m", "Sophie": "f", "Jan": "m", "Katrin": "f"},
    "es": {"Mark": "m", "Inés": "f", "Javier": "m", "Carmen": "f", "Tomás": "m", "Elena": "f", "Diego": "m", "Marta": "f"},
}

# CE QU'ON APPORTE (la liste « qui apporte quoi » et l'invitation). def : apres « Wer bringt ... mit? » / « ¿Quién trae
# ...? » ; indef : « Bring gern ... mit » / « Trae ... » ; t : {langue: [defini, indefini]} (de : a l'accusatif).
APPORTS = {
    "de": {
        "kuchen":   {"mot": "Kuchen", "genre": "der", "def": "den Kuchen", "indef": "einen Kuchen",
                     "t": {"fr": ["le gâteau", "un gâteau"], "en": ["the cake", "a cake"], "pt": ["o bolo", "um bolo"]}},
        "salat":    {"mot": "Salat", "genre": "der", "def": "den Salat", "indef": "einen Salat",
                     "t": {"fr": ["la salade", "une salade"], "en": ["the salad", "a salad"], "pt": ["a salada", "uma salada"]}},
        "brot":     {"mot": "Brot", "genre": "das", "def": "das Brot", "indef": "ein Brot",
                     "t": {"fr": ["le pain", "du pain"], "en": ["the bread", "some bread"], "pt": ["o pão", "pão"]}},
        "getraenk": {"mot": "Getränk", "genre": "das", "def": "die Getränke", "indef": "Getränke",
                     "t": {"fr": ["les boissons", "des boissons"], "en": ["the drinks", "some drinks"], "pt": ["as bebidas", "bebidas"]}},
        "nachtisch": {"mot": "Nachtisch", "genre": "der", "def": "den Nachtisch", "indef": "einen Nachtisch",
                     "t": {"fr": ["le dessert", "un dessert"], "en": ["the dessert", "a dessert"], "pt": ["a sobremesa", "uma sobremesa"]}},
        "saft":     {"mot": "Saft", "genre": "der", "def": "den Saft", "indef": "Saft",
                     "t": {"fr": ["le jus", "du jus"], "en": ["the juice", "some juice"], "pt": ["o suco", "suco"]}},
        "luftballon": {"mot": "Luftballon", "genre": "der", "def": "die Luftballons", "indef": "Luftballons",
                     "t": {"fr": ["les ballons", "des ballons"], "en": ["the balloons", "some balloons"], "pt": ["os balões", "balões"]}},
        "kerze":    {"mot": "Kerze", "genre": "die", "def": "die Kerzen", "indef": "Kerzen",
                     "t": {"fr": ["les bougies", "des bougies"], "en": ["the candles", "some candles"], "pt": ["as velas", "velas"]}},
    },
    "es": {
        "ensalada": {"mot": "ensalada", "genre": "la", "def": "la ensalada", "indef": "una ensalada",
                     "t": {"fr": ["la salade", "une salade"], "en": ["the salad", "a salad"], "pt": ["a salada", "uma salada"], "de": ["den Salat", "einen Salat"]}},
        "pan":      {"mot": "pan", "genre": "el", "def": "el pan", "indef": "pan",
                     "t": {"fr": ["le pain", "du pain"], "en": ["the bread", "some bread"], "pt": ["o pão", "pão"], "de": ["das Brot", "Brot"]}},
        "postre":   {"mot": "postre", "genre": "el", "def": "el postre", "indef": "un postre",
                     "t": {"fr": ["le dessert", "un dessert"], "en": ["the dessert", "a dessert"], "pt": ["a sobremesa", "uma sobremesa"], "de": ["den Nachtisch", "einen Nachtisch"]}},
        "bebida":   {"mot": "bebida", "genre": "la", "def": "las bebidas", "indef": "bebidas",
                     "t": {"fr": ["les boissons", "des boissons"], "en": ["the drinks", "some drinks"], "pt": ["as bebidas", "bebidas"], "de": ["die Getränke", "Getränke"]}},
        "fruta":    {"mot": "fruta", "genre": "la", "def": "la fruta", "indef": "fruta",
                     "t": {"fr": ["les fruits", "des fruits"], "en": ["the fruit", "some fruit"], "pt": ["as frutas", "frutas"], "de": ["das Obst", "Obst"]}},
        "globo":    {"mot": "globo", "genre": "el", "def": "los globos", "indef": "globos",
                     "t": {"fr": ["les ballons", "des ballons"], "en": ["the balloons", "some balloons"], "pt": ["os balões", "balões"], "de": ["die Luftballons", "Luftballons"]}},
        "uva":      {"mot": "uva", "genre": "la", "def": "las uvas", "indef": "las uvas",
                     "t": {"fr": ["les raisins", "les raisins"], "en": ["the grapes", "the grapes"], "pt": ["as uvas", "as uvas"], "de": ["die Trauben", "die Trauben"]}},
    },
}

# ---------------------------------------------------------------------------------------------------------------
# LES INVITATIONS (la carte dessinee par la page). de : qui invite (hote, s : m / f / pl), qui est invite (parmi
# « pour »), la fete (« fete » : une cle de FETES, ou None), le texte de la carte (« texte » : {invite} = « dich »),
# la date ISO (le jour de la semaine se calcule), l'heure, le lieu, ce qu'on peut apporter (« apports » : la carte en
# tire un), la date de reponse. nom : l'evenement dans une phrase (« Die Party ist am Samstag. ») ; t : traductions
# [l'evenement, ce que fete l'hote]. feiert : la phrase « Mark feiert Geburtstag. ».
INVITATIONS = {
    "de": [
        {"id": "mark", "hote": "Mark", "s": "m", "pour": ["Anna", "Lena", "Felix", "Sophie"], "fete": "geburtstag",
         "titre": "Ich werde 26!", "texte": "Ich lade dich herzlich zu meiner Geburtstagsparty ein.",
         "date": "2027-03-13", "heure": 19, "lieu": "bei mir, Gartenstraße 12", "apports": ["salat", "brot", "getraenk", "nachtisch"], "repondre": "2027-03-10",
         "nom": "die Party", "feiert": "Mark feiert Geburtstag.",
         "t": {"fr": ["la fête", "Mark fête son anniversaire."], "en": ["the party", "Mark is celebrating his birthday."], "pt": ["a festa", "O Mark comemora o aniversário."]}},
        {"id": "ben", "hote": "Jan und Katrin", "s": "pl", "pour": ["Anna", "Lena", "Felix", "Sophie"], "fete": "geburtstag",
         "titre": "Ben wird acht!", "texte": "Wir laden dich herzlich zu Bens Geburtstag ein.",
         "date": "2027-04-24", "heure": 15, "lieu": "bei uns zu Hause", "apports": ["kuchen", "saft", "luftballon"], "repondre": "2027-04-20",
         "nom": "die Feier", "feiert": "Ben feiert Geburtstag.",
         "t": {"fr": ["la fête", "Ben fête son anniversaire."], "en": ["the party", "Ben is celebrating his birthday."], "pt": ["a festa", "O Ben comemora o aniversário."]}},
        {"id": "felix", "hote": "Felix", "s": "m", "pour": ["Anna", "Lena", "Mark", "Sophie"], "fete": "silvester",
         "titre": "Silvesterparty!", "texte": "Ich lade dich herzlich zu meiner Silvesterparty ein.",
         "date": "2026-12-31", "heure": 20, "lieu": "bei mir, Florastraße 7", "apports": ["salat", "brot", "nachtisch", "getraenk"], "repondre": "2026-12-27",
         "nom": "die Party", "feiert": "Felix feiert Silvester.",
         "t": {"fr": ["la fête", "Felix fête la Saint-Sylvestre."], "en": ["the party", "Felix is celebrating New Year's Eve."], "pt": ["a festa", "O Felix comemora o Réveillon."]}},
        {"id": "anna", "hote": "Anna", "s": "f", "pour": ["Mark", "Lena", "Felix", "Sophie"], "fete": None,
         "titre": "Meine neue Wohnung!", "texte": "Ich lade dich herzlich zu meiner Einweihungsparty ein.",
         "date": "2026-11-28", "heure": 18, "lieu": "bei mir, Kastanienallee 21", "apports": ["salat", "brot", "kuchen", "kerze", "getraenk"], "repondre": "2026-11-25",
         "nom": "die Party", "feiert": None,
         "t": {"fr": ["la fête", None], "en": ["the party", None], "pt": ["a festa", None]}},
        {"id": "grosseltern", "hote": "Gisela und Heinz", "s": "pl", "pour": ["Anna", "Lena", "Felix", "Sophie", "Jan"], "fete": "weihnachten",
         "titre": "Frohe Weihnachten!", "texte": "Wir laden dich herzlich zum Weihnachtsessen ein.",
         "date": "2026-12-25", "heure": 13, "lieu": "bei uns", "apports": ["nachtisch", "brot", "salat"], "repondre": "2026-12-15",
         "nom": "das Essen", "feiert": "Gisela und Heinz feiern Weihnachten.",
         "t": {"fr": ["le repas", "Gisela et Heinz fêtent Noël."], "en": ["the meal", "Gisela and Heinz are celebrating Christmas."], "pt": ["o almoço", "A Gisela e o Heinz comemoram o Natal."]}},
        {"id": "lena", "hote": "Lena", "s": "f", "pour": ["Anna", "Mark", "Felix", "Sophie"], "fete": "ostern",
         "titre": "Frohe Ostern!", "texte": "Ich lade dich herzlich zum Osterfrühstück ein.",
         "date": "2027-03-28", "heure": 10, "lieu": "bei mir, Breite Straße 3", "apports": ["brot", "kuchen", "saft"], "repondre": "2027-03-24",
         "nom": "das Frühstück", "feiert": "Lena feiert Ostern.",
         "t": {"fr": ["le petit-déjeuner", "Lena fête Pâques."], "en": ["the breakfast", "Lena is celebrating Easter."], "pt": ["o café da manhã", "A Lena comemora a Páscoa."]}},
    ],
    "es": [
        {"id": "mark", "hote": "Mark", "s": "m", "pour": ["Inés", "Javier", "Carmen", "Tomás", "Elena", "Diego"], "fete": "cumpleanos",
         "titre": "¡Cumplo 26 años!", "texte": "Te invito a mi fiesta de cumpleaños.",
         "date": "2027-03-13", "heure": 21, "lieu": "en mi casa, calle de la Luna 12", "apports": ["ensalada", "pan", "postre", "bebida"], "repondre": "2027-03-10",
         "nom": "la fiesta", "feiert": "Mark celebra su cumpleaños.",
         "t": {"fr": ["la fête", "Mark fête son anniversaire."], "en": ["the party", "Mark is celebrating his birthday."], "pt": ["a festa", "O Mark comemora o aniversário."],
               "de": ["die Party", "Mark feiert Geburtstag."]}},
        {"id": "ines", "hote": "Inés", "s": "f", "pour": ["Mark", "Javier", "Carmen", "Tomás", "Elena"], "fete": "nochevieja",
         "titre": "¡Nochevieja en casa!", "texte": "Te invito a la cena de Nochevieja.",
         "date": "2026-12-31", "heure": 21, "lieu": "en mi casa, calle del Pez 8", "apports": ["uva", "postre", "pan"], "repondre": "2026-12-27",
         "nom": "la cena", "feiert": "Inés celebra la Nochevieja.",
         "t": {"fr": ["le dîner", "Inés fête la Saint-Sylvestre."], "en": ["the dinner", "Inés is celebrating New Year's Eve."], "pt": ["o jantar", "A Inés comemora o Réveillon."],
               "de": ["das Essen", "Inés feiert Silvester."]}},
        {"id": "boda", "hote": "Javier y Marta", "s": "pl", "pour": ["Mark", "Inés", "Carmen", "Tomás", "Elena", "Diego"], "fete": "boda",
         "titre": "¡Nos casamos!", "texte": "Te invitamos a nuestra boda.",
         "date": "2027-06-05", "heure": 12, "lieu": "en la finca El Encinar", "apports": [], "repondre": "2027-04-30",
         "nom": "la boda", "feiert": "Javier y Marta celebran su boda.",
         "t": {"fr": ["le mariage", "Javier et Marta fêtent leur mariage."], "en": ["the wedding", "Javier and Marta are celebrating their wedding."],
               "pt": ["o casamento", "O Javier e a Marta comemoram o casamento."], "de": ["die Hochzeit", "Javier und Marta feiern ihre Hochzeit."]}},
        {"id": "carmen", "hote": "Carmen", "s": "f", "pour": ["Mark", "Inés", "Javier", "Tomás", "Elena", "Diego"], "fete": "reyes",
         "titre": "¡Día de Reyes!", "texte": "Te invito a merendar el Día de Reyes.",
         "date": "2027-01-06", "heure": 17, "lieu": "en mi casa, plaza de Olavide 3", "apports": ["fruta", "bebida", "globo"], "repondre": "2027-01-03",
         "nom": "la fiesta", "feiert": "Carmen celebra el Día de Reyes.",
         "t": {"fr": ["la fête", "Carmen fête l'Épiphanie."], "en": ["the party", "Carmen is celebrating Three Kings' Day."], "pt": ["a festa", "A Carmen comemora o Dia de Reis."],
               "de": ["die Feier", "Carmen feiert den Dreikönigstag."]}},
        {"id": "tomas", "hote": "Tomás", "s": "m", "pour": ["Mark", "Inés", "Javier", "Carmen", "Elena", "Diego"], "fete": None,
         "titre": "¡Fiesta en la terraza!", "texte": "Te invito a una fiesta en mi terraza.",
         "date": "2027-06-19", "heure": 20, "lieu": "en mi casa, calle Mayor 5", "apports": ["ensalada", "pan", "fruta", "bebida"], "repondre": "2027-06-16",
         "nom": "la fiesta", "feiert": None,
         "t": {"fr": ["la fête", None], "en": ["the party", None], "pt": ["a festa", None], "de": ["die Party", None]}},
    ],
}

# LES MOTIFS D'UN AGENDA (accepter ou refuser selon l'agenda, proposer un autre jour). court : ce que l'agenda montre ;
# satz : ce qu'on dit apres « Am Samstag » / « El sabado » ; semaine : seulement du lundi au vendredi (le medecin) ;
# t : la meme proposition, traduite apres le jour.
MOTIFS = {
    "de": {
        "arbeiten": {"court": "arbeiten", "satz": "muss ich arbeiten",
                     "t": {"fr": "je dois travailler", "en": "I have to work", "pt": "tenho que trabalhar"}},
        "eltern":   {"court": "Eltern besuchen", "satz": "besuche ich meine Eltern",
                     "t": {"fr": "je rends visite à mes parents", "en": "I'm visiting my parents", "pt": "vou visitar meus pais"}},
        "arzt":     {"court": "Termin beim Arzt", "satz": "habe ich einen Termin beim Arzt", "semaine": True,
                     "t": {"fr": "j'ai rendez-vous chez le médecin", "en": "I have a doctor's appointment", "pt": "tenho consulta médica"}},
        "training": {"court": "Training", "satz": "habe ich Training",
                     "t": {"fr": "j'ai entraînement", "en": "I have training", "pt": "tenho treino"}},
        "kino":     {"court": "Kino mit Freunden", "satz": "gehe ich mit Freunden ins Kino",
                     "t": {"fr": "je vais au cinéma avec des amis", "en": "I'm going to the cinema with friends", "pt": "vou ao cinema com amigos"}},
    },
    "es": {
        "trabajo":  {"court": "trabajo", "satz": "trabajo",
                     "t": {"fr": "je travaille", "en": "I'm working", "pt": "trabalho", "de": "arbeite ich"}},
        "padres":   {"court": "visitar a mis padres", "satz": "visito a mis padres",
                     "t": {"fr": "je rends visite à mes parents", "en": "I'm visiting my parents", "pt": "vou visitar meus pais", "de": "besuche ich meine Eltern"}},
        "medico":   {"court": "cita con el médico", "satz": "tengo cita con el médico", "semaine": True,
                     "t": {"fr": "j'ai rendez-vous chez le médecin", "en": "I have a doctor's appointment", "pt": "tenho consulta médica", "de": "habe ich einen Termin beim Arzt"}},
        "clase":    {"court": "clase de alemán", "satz": "tengo clase de alemán",
                     "t": {"fr": "j'ai cours d'allemand", "en": "I have German class", "pt": "tenho aula de alemão", "de": "habe ich Deutschkurs"}},
        "cine":     {"court": "cine con amigos", "satz": "voy al cine con unos amigos",
                     "t": {"fr": "je vais au cinéma avec des amis", "en": "I'm going to the cinema with friends", "pt": "vou ao cinema com uns amigos", "de": "gehe ich mit Freunden ins Kino"}},
    },
}
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

# ---------------------------------------------------------------------------------------------------------------
# LES MOMENTS : une image d'action (Mark), la phrase qu'elle dit, le verbe du corpus qu'elle fait avancer.
# phrase : {langue: la phrase} ; t : {langue de traduction: la phrase}.
MOMENTS = [
    {"id": "einladen", "img": "einladen", "v": {"de": "einladen", "es": "invitar"},
     "phrase": {"de": "Mark lädt seine Freunde ein.", "es": "Mark invita a sus amigos."},
     "t": {"fr": "Mark invite ses amis.", "en": "Mark is inviting his friends.", "pt": "O Mark convida os amigos.", "de": "Mark lädt seine Freunde ein."}},
    {"id": "karte", "img": "karte", "v": {"de": "gratulieren", "es": "felicitar"},
     "phrase": {"de": "Mark gratuliert seiner Freundin zum Geburtstag.", "es": "Mark felicita a su amiga por su cumpleaños."},
     "t": {"fr": "Mark souhaite un joyeux anniversaire à son amie.", "en": "Mark is wishing his friend a happy birthday.",
           "pt": "O Mark dá os parabéns à amiga pelo aniversário.", "de": "Mark gratuliert seiner Freundin zum Geburtstag."}},
    {"id": "mitbringen", "img": "mitbringen", "v": {"de": "mitbringen", "es": "traer"},
     "phrase": {"de": "Mark bringt einen Salat mit.", "es": "Mark trae una ensalada."},
     "t": {"fr": "Mark apporte une salade.", "en": "Mark is bringing a salad.", "pt": "O Mark leva uma salada.", "de": "Mark bringt einen Salat mit."}},
    {"id": "absagen", "img": "absagen", "v": {"de": "absagen", "es": "poder"},
     "phrase": {"de": "Mark sagt am Telefon ab.", "es": "Mark dice por teléfono que no puede ir."},
     "t": {"fr": "Mark se décommande au téléphone.", "en": "Mark is cancelling on the phone.", "pt": "O Mark avisa por telefone que não pode ir.", "de": "Mark sagt am Telefon ab."}},
    {"id": "planen", "img": "planen", "v": {"de": "planen", "es": "planear"},
     "phrase": {"de": "Mark und Anna planen eine Party.", "es": "Mark planea una fiesta con una amiga."},
     "t": {"fr": "Mark et Anna préparent une fête.", "en": "Mark and Anna are planning a party.", "pt": "O Mark e a Anna planejam uma festa.", "de": "Mark plant mit einer Freundin eine Party."},
     "t_es": {"fr": "Mark prépare une fête avec une amie.", "en": "Mark is planning a party with a friend.", "pt": "O Mark planeja uma festa com uma amiga."}},
    {"id": "feiern", "img": "geburtstag", "v": {"de": "feiern", "es": "celebrar"},
     "phrase": {"de": "Mark feiert seinen Geburtstag.", "es": "Mark celebra su cumpleaños."},
     "t": {"fr": "Mark fête son anniversaire.", "en": "Mark is celebrating his birthday.", "pt": "O Mark comemora o aniversário.", "de": "Mark feiert seinen Geburtstag."}},
]

# LA CONJUGAISON (espagnol) : la phrase a trou, le verbe et la personne (cle de praesens) ; les leurres : les autres
# personnes du meme verbe. {A} = un apport (« Yo ___ el pan. »).
CONJ_ES = [
    {"v": "poder", "p": "du", "phrase": "¿___ venir a mi fiesta?", "t": {"fr": "Tu peux venir à ma fête ?", "en": "Can you come to my party?", "pt": "Você pode vir à minha festa?", "de": "Kannst du zu meiner Party kommen?"}},
    {"v": "poder", "p": "ich", "phrase": "Lo siento, no ___ ir.", "t": {"fr": "Désolé, je ne peux pas venir.", "en": "Sorry, I can't go.", "pt": "Sinto muito, não posso ir.", "de": "Tut mir leid, ich kann nicht kommen."}},
    {"v": "traer", "p": "ich", "phrase": "Yo ___ {A}.", "t": {"fr": "J'apporte {A}.", "en": "I'll bring {A}.", "pt": "Eu levo {A}.", "de": "Ich bringe {A} mit."}},
    {"v": "traer", "p": "er_sie_es", "phrase": "{P} ___ {A}.", "t": {"fr": "{P} apporte {A}.", "en": "{P} is bringing {A}.", "pt": "{P} leva {A}.", "de": "{P} bringt {A} mit."}},
    {"v": "traer", "p": "du", "phrase": "¿Qué ___ tú?", "t": {"fr": "Qu'est-ce que tu apportes ?", "en": "What are you bringing?", "pt": "O que você leva?", "de": "Was bringst du mit?"}},
    {"v": "invitar", "p": "ich", "phrase": "Te ___ a mi cumpleaños.", "t": {"fr": "Je t'invite à mon anniversaire.", "en": "I'm inviting you to my birthday.", "pt": "Te convido para o meu aniversário.", "de": "Ich lade dich zu meinem Geburtstag ein."}},
    {"v": "invitar", "p": "sie_Sie", "phrase": "Javier y Marta te ___ a su boda.", "t": {"fr": "Javier et Marta t'invitent à leur mariage.", "en": "Javier and Marta are inviting you to their wedding.", "pt": "O Javier e a Marta te convidam para o casamento.", "de": "Javier und Marta laden dich zu ihrer Hochzeit ein."}},
    {"v": "celebrar", "p": "wir", "phrase": "El sábado ___ el cumpleaños de Mark.", "t": {"fr": "Samedi, nous fêtons l'anniversaire de Mark.", "en": "On Saturday we're celebrating Mark's birthday.", "pt": "No sábado comemoramos o aniversário do Mark.", "de": "Am Samstag feiern wir Marks Geburtstag."}},
    {"v": "venir", "p": "du", "phrase": "¿___ a la cena de Nochevieja?", "t": {"fr": "Tu viens au dîner de la Saint-Sylvestre ?", "en": "Are you coming to the New Year's Eve dinner?", "pt": "Você vem ao jantar de Réveillon?", "de": "Kommst du zum Silvesteressen?"}},
    {"v": "ir", "p": "ich", "phrase": "¡Gracias! Claro que ___ a tu fiesta.", "t": {"fr": "Merci ! Bien sûr que je viens à ta fête.", "en": "Thanks! Of course I'll come to your party.", "pt": "Obrigado! Claro que vou à sua festa.", "de": "Danke! Natürlich komme ich zu deiner Party."}},
    {"v": "ir", "p": "wir", "phrase": "El sábado ___ a la boda de Javier y Marta.", "t": {"fr": "Samedi, nous allons au mariage de Javier et Marta.", "en": "On Saturday we're going to Javier and Marta's wedding.", "pt": "No sábado vamos ao casamento do Javier e da Marta.", "de": "Am Samstag gehen wir zur Hochzeit von Javier und Marta."}},
]
# « Te invito al cumpleanos » / « a la boda » (a + el = al) : l'evenement, son article, et qui le donne
AL_ES = [
    {"mot": "cumpleaños", "genre": "el", "apres": "cumpleaños de {H}", "hotes": ["Mark", "Tomás", "Inés", "Elena"], "t": {"fr": "à l'anniversaire de {H}", "en": "to {H}'s birthday", "pt": "para o aniversário de {H}", "de": "zu {H}s Geburtstag"}},
    {"mot": "boda", "genre": "la", "apres": "boda de {H}", "hotes": ["Javier y Marta"], "t": {"fr": "au mariage de {H}", "en": "to {H}'s wedding", "pt": "para o casamento de {H}", "de": "zur Hochzeit von {H}"}},
    {"mot": "cena", "genre": "la", "apres": "cena de Nochevieja", "hotes": [None], "t": {"fr": "au dîner de la Saint-Sylvestre", "en": "to the New Year's Eve dinner", "pt": "para o jantar de Réveillon", "de": "zum Silvesteressen"}},
    {"mot": "fiesta", "genre": "la", "apres": "fiesta de {H}", "hotes": ["Carmen", "Tomás", "Diego", "Inés"], "t": {"fr": "à la fête de {H}", "en": "to {H}'s party", "pt": "para a festa de {H}", "de": "zu {H}s Party"}},
]
# « Ich lade dich zu meiner Party ein » / « Herzlichen Glueckwunsch zum Geburtstag » (allemand) : le nom, son genre, le
# datif du possessif (meinem / meiner)
ZU_DE = [
    {"mot": "Party", "genre": "die", "t": {"fr": "à ma fête", "en": "to my party", "pt": "para a minha festa"}},
    {"mot": "Geburtstag", "genre": "der", "t": {"fr": "à mon anniversaire", "en": "to my birthday", "pt": "para o meu aniversário"}},
    {"mot": "Fest", "genre": "das", "t": {"fr": "à ma fête", "en": "to my celebration", "pt": "para a minha festa"}},
    {"mot": "Feier", "genre": "die", "t": {"fr": "à ma fête", "en": "to my celebration", "pt": "para a minha comemoração"}},
    {"mot": "Einweihungsparty", "genre": "die", "t": {"fr": "à ma crémaillère", "en": "to my housewarming party", "pt": "para a minha festa de casa nova"}},
]

# ---------------------------------------------------------------------------------------------------------------
# LES MOTS ABSENTS DU CORPUS (espagnol), a proposer a Jacques ; en attendant, l'app les tient « hors jeu ».
AJOUTS_TRAD = {
    "de": {},
    "es": {"Año Nuevo": {"fr": "jour de l'An", "en": "New Year's Day", "pt": "Ano-Novo", "ar": "رأس السنة", "de": "Neujahr"},
           "Día de Reyes": {"fr": "Épiphanie (fête des Rois)", "en": "Three Kings' Day", "pt": "Dia de Reis", "ar": "عيد الملوك الثلاثة", "de": "Dreikönigstag"},
           "Semana Santa": {"fr": "Semaine sainte", "en": "Holy Week", "pt": "Semana Santa", "ar": "أسبوع الآلام", "de": "Karwoche"},
           "carnaval": {"fr": "carnaval", "en": "carnival", "pt": "Carnaval", "ar": "الكرنفال", "de": "Karneval"},
           "Día de Muertos": {"fr": "jour des Morts", "en": "Day of the Dead", "pt": "Dia dos Mortos", "ar": "يوم الموتى", "de": "Tag der Toten"}},
}

# ---------------------------------------------------------------------------------------------------------------
# LE PORTUGAIS APPRIS (lot P4, 12 nov. 2026). Lisbonne, le Portugal d'abord ; « br_ » seulement la ou le Bresil differe
# (la page prend pt_, ou br_ s'il existe, avec &variante=br, et les pose sous « pt » au chargement). Pas « pt » : cette
# cle est deja la TRADUCTION en portugais du Bresil pour qui apprend es ou de. Le monde de l'espagnol transpose a
# Lisbonne : Mark (Rua da Rosa 12) et les personnes de « Decrire une personne » (Inês a l'orthographe portugaise).
# Au Portugal l'article devant le prenom (o Mark, a Inês), le pronom apres le verbe (convido-te, diz-se), « tu » entre
# amis ; au Bresil le prenom seul, le pronom avant (te convido, se diz), « você ». L'axe : ir a + l'article (vou ao
# aniversário, à festa), poder, levar (on apporte A la fete), convidar, celebrar ; la troisieme partie du DTZ comme ailleurs.
#
# LES IMAGES (aucune image nouvelle, decision de Jacques) : ouvertes au portugais celles dont la coutume existe au Portugal
# et au Bresil -- l'anniversaire, le Natal (le sapin et les cadeaux), la passagem de ano (feu d'artifice et cierges
# magiques, une rue generique), le Dia de Reis (le roscon de l'image est tres proche du bolo-rei portugais), la Semana
# Santa (les processions existent au Portugal, Braga, et au Bresil), le mariage. ECARTEES : karneval (une petite ville
# allemande a colombages, en manteaux d'hiver), weihnachtsmarkt (bretzels, eglise de brique : un marche allemand),
# ostern (la chasse aux oeufs peints, coutume allemande ; l'espagnol l'ecarte aussi), uvas (les raisins frais devant
# l'horloge de la Puerta del Sol a la tele : la coutume de Madrid ; au Portugal ce sont 12 passas), muertos (le Mexique).
# Le Carnaval et la Páscoa restent, sans image (la date, le souhait).
IMG_EXCLUES_PT = ["karneval", "weihnachtsmarkt", "ostern", "uvas", "muertos"]
PERSONNES_PT = {"Mark": "m", "Inês": "f", "Javier": "m", "Carmen": "f", "Tomás": "m", "Elena": "f", "Diego": "m", "Marta": "f"}


def _br(pt, br):
    """La donnee du Bresil : celle du Portugal, ou chaque cle de br remplace la sienne (cle par cle, entree par entree)."""
    import copy
    out = copy.deepcopy(pt)
    for k, v in br.items():
        if isinstance(out, dict) and isinstance(out.get(k), dict) and isinstance(v, dict):
            out[k].update(copy.deepcopy(v))
        else:
            out[k] = copy.deepcopy(v)
    return out


# LES FETES (memes champs que FETES ; {P} : la personne, avec l'article au Portugal). Le Dia de Reis et le Natal sont
# « aussi » l'un de l'autre : le bolo-rei se mange de Noel aux Rois et l'image des Rois montre des cadeaux.
FETES_PT = {
    "aniversario": {"mot": "aniversário", "genre": "o", "nom": "o aniversário", "wunsch": "Parabéns! Feliz aniversário!", "img": ["geburtstag", "kindergeburtstag"],
                    "dans": "Num aniversário", "c": True, "situation": "{P} faz anos hoje.",
                    "t": {"fr": ["un anniversaire", None, "Joyeux anniversaire !"], "en": ["a birthday", None, "Happy birthday!"]}},
    "natal":       {"mot": "Natal", "genre": "o", "nom": "o Natal", "quand": "a 25 de dezembro", "jours": ["12-25"], "wunsch": "Feliz Natal!", "aussi": ["reis"],
                    "img": ["weihnachten"], "dans": "No Natal", "c": False, "situation": "Hoje é dia de Natal.",
                    "t": {"fr": ["Noël", "le 25 décembre", "Joyeux Noël !"], "en": ["Christmas", "on December 25", "Merry Christmas!"]}},
    "passagem":    {"mot": "passagem de ano", "genre": "a", "nom": "a passagem de ano", "quand": "a 31 de dezembro", "jours": ["12-31"], "wunsch": "Feliz Ano Novo!",
                    "aussi": ["anonovo"], "img": ["silvester"], "dans": "Na passagem de ano", "c": False, "situation": "Hoje é a passagem de ano.",
                    "t": {"fr": ["la Saint-Sylvestre", "le 31 décembre", "Bonne année !"], "en": ["New Year's Eve", "on December 31", "Happy New Year!"]}},
    "anonovo":     {"mot": "Ano Novo", "genre": "o", "nom": "o Ano Novo", "quand": "a 1 de janeiro", "jours": ["01-01"], "wunsch": "Feliz Ano Novo!",
                    "aussi": ["passagem"], "img": [], "dans": "No Ano Novo", "c": False, "situation": "Hoje é dia de Ano Novo.",
                    "t": {"fr": ["le jour de l'An", "le 1er janvier", "Bonne année !"], "en": ["New Year's Day", "on January 1", "Happy New Year!"]}},
    "reis":        {"mot": "Dia de Reis", "genre": "o", "nom": "o Dia de Reis", "quand": "a 6 de janeiro", "jours": ["01-06"], "aussi": ["natal"], "img": ["reyes"],
                    "dans": None, "c": False, "situation": None,
                    "t": {"fr": ["l'Épiphanie (les Rois mages)", "le 6 janvier", None], "en": ["Three Kings' Day", "on January 6", None]}},
    "pascoa":      {"mot": "Páscoa", "genre": "a", "nom": "a Páscoa", "quand": "em março ou abril", "jours": ["03", "04"], "wunsch": "Boa Páscoa!", "aussi": ["semanasanta"],
                    "img": [], "dans": "Na Páscoa", "c": False, "situation": "Hoje é domingo de Páscoa.",
                    "t": {"fr": ["Pâques", "en mars ou en avril", "Joyeuses Pâques !"], "en": ["Easter", "in March or April", "Happy Easter!"]}},
    "semanasanta": {"mot": "Semana Santa", "genre": "a", "nom": "a Semana Santa", "quand": "em março ou abril", "jours": ["03", "04"], "aussi": ["pascoa"],
                    "img": ["semanasanta"], "dans": None, "c": False, "situation": None,
                    "t": {"fr": ["la Semaine sainte", "en mars ou en avril", None], "en": ["Holy Week", "in March or April", None]}},
    # le mardi gras tombe entre le 3 fevrier et le 9 mars
    "carnaval":    {"mot": "carnaval", "genre": "o", "nom": "o Carnaval", "quand": "em fevereiro ou março", "jours": ["02", "03"], "img": [],
                    "dans": None, "c": False, "situation": None,
                    "t": {"fr": ["le carnaval", "en février ou en mars", None], "en": ["carnival", "in February or March", None]}},
    "casamento":   {"mot": "casamento", "genre": "o", "nom": "o casamento", "wunsch": "Muitos parabéns aos noivos!", "img": ["hochzeit"],
                    "dans": "Num casamento", "c": True, "situation": "A tua colega casa-se hoje.",
                    "t": {"fr": ["un mariage", None, "Félicitations aux mariés !"], "en": ["a wedding", None, "Congratulations to the happy couple!"]}},
    # le premier dimanche de mai au Portugal, le deuxieme au Bresil
    "mae":         {"mot": "Dia da Mãe", "genre": "o", "nom": "o Dia da Mãe", "quand": "no primeiro domingo de maio", "jours": ["05"], "wunsch": "Feliz Dia da Mãe!",
                    "img": [], "dans": "No Dia da Mãe", "c": False, "situation": "Hoje é o Dia da Mãe.",
                    "t": {"fr": ["la fête des Mères", "le premier dimanche de mai", "Bonne fête, maman !"], "en": ["Mother's Day", "on the first Sunday in May", "Happy Mother's Day!"]}},
}
FETES_BR = _br(FETES_PT, {
    "aniversario": {"dans": "Em um aniversário", "situation": "{P} faz aniversário hoje."},
    "natal": {"quand": "em 25 de dezembro"},
    "passagem": {"mot": "réveillon", "genre": "o", "nom": "o Réveillon", "quand": "em 31 de dezembro", "dans": "No Réveillon", "situation": "Hoje é noite de Réveillon."},
    "anonovo": {"quand": "em 1º de janeiro"},
    "reis": {"quand": "em 6 de janeiro"},
    "pascoa": {"wunsch": "Feliz Páscoa!"},
    "casamento": {"wunsch": "Parabéns aos noivos!", "dans": "Em um casamento", "situation": "Sua colega de trabalho se casa hoje."},
    "mae": {"mot": "Dia das Mães", "nom": "o Dia das Mães", "quand": "no segundo domingo de maio", "wunsch": "Feliz Dia das Mães!", "dans": "No Dia das Mães",
            "situation": "Hoje é Dia das Mães.",
            "t": {"fr": ["la fête des Mères", "le deuxième dimanche de mai", "Bonne fête, maman !"], "en": ["Mother's Day", "on the second Sunday in May", "Happy Mother's Day!"]}},
})
SITUATIONS_T_PT = {"aniversario": {"fr": "C'est l'anniversaire de {P} aujourd'hui.", "en": "It's {P}'s birthday today."},
                   "casamento": {"fr": "Ta collègue se marie aujourd'hui.", "en": "Your colleague is getting married today."}}

APPORTS_PT = {
    "bolo":      {"mot": "bolo", "genre": "o", "def": "o bolo", "indef": "um bolo", "t": {"fr": ["le gâteau", "un gâteau"], "en": ["the cake", "a cake"]}},
    "salada":    {"mot": "salada", "genre": "a", "def": "a salada", "indef": "uma salada", "t": {"fr": ["la salade", "une salade"], "en": ["the salad", "a salad"]}},
    "pao":       {"mot": "pão", "genre": "o", "def": "o pão", "indef": "pão", "t": {"fr": ["le pain", "du pain"], "en": ["the bread", "some bread"]}},
    "bebida":    {"mot": "bebida", "genre": "a", "def": "as bebidas", "indef": "bebidas", "t": {"fr": ["les boissons", "des boissons"], "en": ["the drinks", "some drinks"]}},
    "sobremesa": {"mot": "sobremesa", "genre": "a", "def": "a sobremesa", "indef": "uma sobremesa", "t": {"fr": ["le dessert", "un dessert"], "en": ["the dessert", "a dessert"]}},
    "fruta":     {"mot": "fruta", "genre": "a", "def": "a fruta", "indef": "fruta", "t": {"fr": ["les fruits", "des fruits"], "en": ["the fruit", "some fruit"]}},
    "balao":     {"mot": "balão", "genre": "o", "def": "os balões", "indef": "balões", "t": {"fr": ["les ballons", "des ballons"], "en": ["the balloons", "some balloons"]}},
    "sumo":      {"mot": "sumo", "genre": "o", "def": "o sumo", "indef": "sumo", "t": {"fr": ["le jus", "du jus"], "en": ["the juice", "some juice"]}},
}
APPORTS_BR = _br(APPORTS_PT, {"sumo": {"mot": "suco", "def": "o suco", "indef": "suco"}})

# LES INVITATIONS (memes champs ; nomMot : le mot du corpus que dit « nom », vise par les questions sur la carte)
INVITATIONS_PT = [
    {"id": "mark", "hote": "Mark", "s": "m", "pour": ["Inês", "Javier", "Carmen", "Tomás", "Elena", "Diego"], "fete": "aniversario",
     "titre": "Faço 26 anos!", "texte": "Convido-te para a minha festa de anos.",
     "date": "2027-03-13", "heure": 20, "lieu": "na minha casa, Rua da Rosa 12", "apports": ["salada", "pao", "sobremesa", "bebida"], "repondre": "2027-03-10",
     "nom": "a festa", "nomMot": ["festa", "a"], "feiert": "O Mark celebra o aniversário.",
     "t": {"fr": ["la fête", "Mark fête son anniversaire."], "en": ["the party", "Mark is celebrating his birthday."]}},
    {"id": "ines", "hote": "Inês", "s": "f", "pour": ["Mark", "Javier", "Carmen", "Tomás", "Elena"], "fete": "passagem",
     "titre": "Passagem de ano cá em casa!", "texte": "Convido-te para o jantar da passagem de ano.",
     "date": "2026-12-31", "heure": 21, "lieu": "na minha casa, Rua do Norte 8", "apports": ["sobremesa", "pao", "bebida"], "repondre": "2026-12-27",
     "nom": "o jantar", "nomMot": ["jantar", "o"], "feiert": "A Inês celebra a passagem de ano.",
     "t": {"fr": ["le dîner", "Inês fête la Saint-Sylvestre."], "en": ["the dinner", "Inês is celebrating New Year's Eve."]}},
    {"id": "casamento", "hote": "Javier e Marta", "s": "pl", "pour": ["Mark", "Inês", "Carmen", "Tomás", "Elena", "Diego"], "fete": "casamento",
     "titre": "Vamos casar!", "texte": "Convidamos-te para o nosso casamento.",
     "date": "2027-06-05", "heure": 12, "lieu": "na Quinta do Sobreiro", "apports": [], "repondre": "2027-04-30",
     "nom": "o casamento", "nomMot": ["casamento", "o"], "feiert": "O Javier e a Marta celebram o casamento.",
     "t": {"fr": ["le mariage", "Javier et Marta fêtent leur mariage."], "en": ["the wedding", "Javier and Marta are celebrating their wedding."]}},
    {"id": "carmen", "hote": "Carmen", "s": "f", "pour": ["Mark", "Inês", "Javier", "Tomás", "Elena", "Diego"], "fete": "reis",
     "titre": "Dia de Reis!", "texte": "Convido-te para um lanche com bolo-rei no Dia de Reis.",
     "date": "2027-01-06", "heure": 17, "lieu": "na minha casa, Rua de São Bento 30", "apports": ["fruta", "sumo", "balao"], "repondre": "2027-01-03",
     "nom": "o lanche", "nomMot": ["lanche", "o"], "feiert": "A Carmen celebra o Dia de Reis.",
     "t": {"fr": ["le goûter", "Carmen fête l'Épiphanie."], "en": ["the afternoon snack", "Carmen is celebrating Three Kings' Day."]}},
    {"id": "tomas", "hote": "Tomás", "s": "m", "pour": ["Mark", "Inês", "Javier", "Carmen", "Elena", "Diego"], "fete": None,
     "titre": "Festa no terraço!", "texte": "Convido-te para uma festa no meu terraço.",
     "date": "2027-06-19", "heure": 20, "lieu": "na minha casa, Rua da Graça 5", "apports": ["salada", "pao", "fruta", "bebida"], "repondre": "2027-06-16",
     "nom": "a festa", "nomMot": ["festa", "a"], "feiert": None,
     "t": {"fr": ["la fête", None], "en": ["the party", None]}},
]
_INV_BR = {"mark": {"texte": "Quero te convidar para a minha festa de aniversário.", "feiert": "Mark celebra o aniversário."},
           "ines": {"titre": "Réveillon aqui em casa!", "texte": "Quero te convidar para o jantar de Réveillon.", "feiert": "Inês celebra o Réveillon."},
           "casamento": {"titre": "Vamos nos casar!", "texte": "Convidamos você para o nosso casamento.", "feiert": "Javier e Marta celebram o casamento."},
           "carmen": {"texte": "Quero te convidar para um lanche com bolo-rei no Dia de Reis.", "feiert": "Carmen celebra o Dia de Reis."},
           "tomas": {"texte": "Quero te convidar para uma festa no meu terraço."}}
INVITATIONS_BR = [_br(i, _INV_BR[i["id"]]) for i in INVITATIONS_PT]

MOTIFS_PT = {
    "trabalho": {"court": "trabalho", "satz": "tenho de trabalhar", "t": {"fr": "je dois travailler", "en": "I have to work"}},
    "pais":     {"court": "visitar os pais", "satz": "vou visitar os meus pais", "t": {"fr": "je rends visite à mes parents", "en": "I'm visiting my parents"}},
    "medico":   {"court": "consulta no médico", "satz": "tenho consulta no médico", "semaine": True, "t": {"fr": "j'ai rendez-vous chez le médecin", "en": "I have a doctor's appointment"}},
    "aula":     {"court": "aula de alemão", "satz": "tenho aula de alemão", "t": {"fr": "j'ai cours d'allemand", "en": "I have German class"}},
    "cinema":   {"court": "cinema com amigos", "satz": "vou ao cinema com uns amigos", "t": {"fr": "je vais au cinéma avec des amis", "en": "I'm going to the cinema with friends"}},
}
MOTIFS_BR = _br(MOTIFS_PT, {"trabalho": {"satz": "tenho que trabalhar"}, "pais": {"satz": "vou visitar meus pais"},
                            "medico": {"court": "consulta médica", "satz": "tenho consulta médica"}})

# LES MOMENTS DE MARK (les memes images ; w : le mot vise -- « os parabéns » pour la carte, plus naturel que felicitar)
MOMENTS_PT = [
    {"id": "einladen", "img": "einladen", "w": ["convidar", None, "verbe"], "phrase": "O Mark convida os amigos.",
     "t": {"fr": "Mark invite ses amis.", "en": "Mark is inviting his friends."}},
    {"id": "karte", "img": "karte", "w": ["parabéns", "os", None], "phrase": "O Mark escreve um cartão de parabéns à amiga.",
     "t": {"fr": "Mark écrit une carte d'anniversaire à son amie.", "en": "Mark is writing a birthday card to his friend."}},
    {"id": "mitbringen", "img": "mitbringen", "w": ["levar", None, "verbe"], "phrase": "O Mark leva uma salada.",
     "t": {"fr": "Mark apporte une salade.", "en": "Mark is bringing a salad."}},
    {"id": "absagen", "img": "absagen", "w": ["poder", None, "verbe"], "phrase": "O Mark diz ao telefone que não pode ir.",
     "t": {"fr": "Mark dit au téléphone qu'il ne peut pas venir.", "en": "Mark is saying on the phone that he can't come."}},
    {"id": "planen", "img": "planen", "w": ["planear", None, "verbe"], "phrase": "O Mark planeia uma festa com uma amiga.",
     "t": {"fr": "Mark prépare une fête avec une amie.", "en": "Mark is planning a party with a friend."}},
    {"id": "feiern", "img": "geburtstag", "w": ["celebrar", None, "verbe"], "phrase": "O Mark celebra o aniversário.",
     "t": {"fr": "Mark fête son anniversaire.", "en": "Mark is celebrating his birthday."}},
]
_MOM_BR = {"einladen": {"phrase": "Mark convida os amigos."}, "karte": {"phrase": "Mark escreve um cartão de parabéns para a amiga."},
           "mitbringen": {"phrase": "Mark leva uma salada."}, "absagen": {"phrase": "Mark diz no telefone que não pode ir."},
           "planen": {"w": ["planejar", None, "verbe"], "phrase": "Mark planeja uma festa com uma amiga."}, "feiern": {"phrase": "Mark celebra o aniversário."}}
MOMENTS_BR = [_br(m, _MOM_BR[m["id"]]) for m in MOMENTS_PT]

# LA CONJUGAISON : le sujet toujours dit (sinon une autre personne serait juste aussi : « não pode ir » = il ne peut pas) ;
# au Bresil « você » prend la 3e personne (er_sie_es)
CONJ_PT = [
    {"v": "poder", "p": "du", "phrase": "Tu ___ vir à minha festa?", "t": {"fr": "Tu peux venir à ma fête ?", "en": "Can you come to my party?"}},
    {"v": "poder", "p": "ich", "phrase": "Desculpa, eu não ___ ir.", "t": {"fr": "Désolé, je ne peux pas venir.", "en": "Sorry, I can't go."}},
    {"v": "levar", "p": "ich", "phrase": "Eu ___ {A}.", "t": {"fr": "J'apporte {A}.", "en": "I'll bring {A}."}},
    {"v": "levar", "p": "er_sie_es", "phrase": "{P} ___ {A}.", "t": {"fr": "{P} apporte {A}.", "en": "{P} is bringing {A}."}},
    {"v": "levar", "p": "du", "phrase": "E tu, o que ___?", "t": {"fr": "Et toi, qu'est-ce que tu apportes ?", "en": "And you, what are you bringing?"}},
    {"v": "convidar", "p": "ich", "phrase": "Eu ___ a Marta para o meu aniversário.", "t": {"fr": "J'invite Marta à mon anniversaire.", "en": "I'm inviting Marta to my birthday."}},
    {"v": "convidar", "p": "sie_Sie", "phrase": "O Javier e a Marta ___-te para o casamento.", "t": {"fr": "Javier et Marta t'invitent à leur mariage.", "en": "Javier and Marta are inviting you to their wedding."}},
    {"v": "celebrar", "p": "wir", "phrase": "No sábado nós ___ o aniversário do Mark.", "t": {"fr": "Samedi, nous fêtons l'anniversaire de Mark.", "en": "On Saturday we're celebrating Mark's birthday."}},
    {"v": "vir", "p": "du", "phrase": "Tu ___ ao jantar da passagem de ano?", "t": {"fr": "Tu viens au dîner de la Saint-Sylvestre ?", "en": "Are you coming to the New Year's Eve dinner?"}},
    {"v": "ir", "p": "ich", "phrase": "Obrigado! Claro que eu ___ à tua festa.", "t": {"fr": "Merci ! Bien sûr que je viens à ta fête.", "en": "Thanks! Of course I'll come to your party."}},
    {"v": "ir", "p": "wir", "phrase": "No sábado nós ___ ao casamento do Javier e da Marta.", "t": {"fr": "Samedi, nous allons au mariage de Javier et Marta.", "en": "On Saturday we're going to Javier and Marta's wedding."}},
]
_CONJ_BR = [{"p": "er_sie_es", "phrase": "Você ___ vir à minha festa?"}, {"phrase": "Desculpe, eu não ___ ir."}, {}, {},
            {"p": "er_sie_es", "phrase": "E você, o que ___?", "t": {"fr": "Et toi, qu'est-ce que tu apportes ?", "en": "And you, what are you bringing?"}},
            {"phrase": "Eu ___ Marta para o meu aniversário."}, {"phrase": "Javier e Marta te ___ para o casamento."},
            {"phrase": "No sábado nós ___ o aniversário de Mark."}, {"p": "er_sie_es", "phrase": "Você ___ ao jantar de Réveillon?"},
            {"phrase": "Obrigado! Claro que eu ___ à sua festa."}, {"phrase": "No sábado nós ___ ao casamento de Javier e Marta."}]
CONJ_BR = [_br(c, b) for c, b in zip(CONJ_PT, _CONJ_BR)]

# « Vou ao aniversário do Mark » / « à festa da Carmen » (a + o = ao, a + a = à) ; {deH} : do Mark, da Inês (Bresil :
# de Mark). Les leurres sont les quatre contractions : une seule s'accorde (jamais « para o », juste aussi, ni « no »).
AL_PT = [
    {"mot": "aniversário", "genre": "o", "apres": "aniversário {deH}", "hotes": ["Mark", "Tomás", "Inês", "Elena"], "t": {"fr": "à l'anniversaire de {H}", "en": "to {H}'s birthday"}},
    {"mot": "casamento", "genre": "o", "apres": "casamento {deH}", "hotes": ["Javier e Marta"], "t": {"fr": "au mariage de {H}", "en": "to {H}'s wedding"}},
    {"mot": "jantar", "genre": "o", "apres": "jantar da passagem de ano", "hotes": [None], "t": {"fr": "au dîner de la Saint-Sylvestre", "en": "to the New Year's Eve dinner"}},
    {"mot": "festa", "genre": "a", "apres": "festa {deH}", "hotes": ["Carmen", "Tomás", "Diego", "Inês"], "t": {"fr": "à la fête de {H}", "en": "to {H}'s party"}},
]
AL_BR = _br(AL_PT, {})
AL_BR[2]["apres"] = "jantar de Réveillon"

# LES MOTS ABSENTS DU CORPUS PORTUGAIS (a ajouter : portugais/outils) : leur traduction, en attendant (« hors jeu »)
PT_AJOUTS = {"Natal": "Noël", "passagem de ano": "la Saint-Sylvestre (le passage à la nouvelle année)", "Ano Novo": "le jour de l'An",
             "Dia de Reis": "l'Épiphanie (la fête des Rois)", "Páscoa": "Pâques", "Semana Santa": "la Semaine sainte", "Dia da Mãe": "la fête des Mères"}
# le corpus portugais n'a que le francais : l'anglais des mots du theme, ici
PT_EN = {"aniversário": "birthday", "Natal": "Christmas", "passagem de ano": "New Year's Eve", "réveillon": "New Year's Eve (party)", "Ano Novo": "New Year's Day",
         "Dia de Reis": "Three Kings' Day", "Páscoa": "Easter", "Semana Santa": "Holy Week", "carnaval": "carnival", "casamento": "wedding",
         "Dia da Mãe": "Mother's Day", "Dia das Mães": "Mother's Day", "bolo": "cake", "salada": "salad", "pão": "bread", "bebida": "drink",
         "sobremesa": "dessert", "fruta": "fruit", "balão": "balloon", "sumo": "juice", "suco": "juice", "convidar": "to invite",
         "parabéns": "congratulations, happy birthday", "levar": "to take, to bring (along)", "poder": "can, to be able to", "planear": "to plan",
         "planejar": "to plan", "celebrar": "to celebrate", "ir": "to go", "vir": "to come", "combinar": "to arrange, to agree on",
         "convite": "invitation", "festa": "party", "jantar": "dinner", "lanche": "afternoon snack",
         "segunda-feira": "Monday", "terça-feira": "Tuesday", "quarta-feira": "Wednesday", "quinta-feira": "Thursday", "sexta-feira": "Friday",
         "sábado": "Saturday", "domingo": "Sunday"}


def corpus_pt(br):
    """(noms {(mot, genre): entree}, verbes {infinitif: entree}) du corpus portugais (Portugal ou Bresil)."""
    dos = os.path.join(RACINE, "portugais", "datos-br" if br else "datos")
    noms = {}
    for t in json.load(io.open(os.path.join(dos, "themes.json"), encoding="utf-8"))["themes"]:
        for m in t["mots"]:
            noms.setdefault((m["mot"], m.get("genre")), m)
    verbes = {e.get("infinitif"): e for l in json.load(io.open(os.path.join(dos, "verbes.json"), encoding="utf-8")).values() if isinstance(l, list) for e in l}
    return noms, verbes


def mots_du_theme_pt(br):
    """Comme mots_du_theme : la forme du corpus (Portugal ou Bresil), le francais du corpus et l'anglais de PT_EN ; un mot
    absent garde PT_AJOUTS et va dans la liste des absents."""
    noms, verbes = corpus_pt(br)
    mots, absents = [], []

    def ajouter(mot, genre=None, cat=None):
        if any(m["mot"] == mot and m.get("genre") == genre and m.get("cat") == cat for m in mots):
            return
        e = verbes.get(mot) if cat == "verbe" else noms.get((mot, genre))
        if e:
            fr = e.get("traduction")
        elif mot in PT_AJOUTS:
            fr = PT_AJOUTS[mot]; absents.append(mot)
        else:
            sys.exit("  %s (%s) absent du corpus portugais%s et des ajouts" % (mot, genre or cat, " (Bresil)" if br else ""))
        if mot not in PT_EN:
            sys.exit("  %s : pas d'anglais dans PT_EN" % mot)
        w = {"mot": mot, "g": {"fr": fr, "en": PT_EN[mot]}}
        if genre:
            w["genre"] = genre
        if cat:
            w["cat"] = cat
        mots.append(w)
    for f in (FETES_BR if br else FETES_PT).values():
        ajouter(f["mot"], f["genre"])
    for a in (APPORTS_BR if br else APPORTS_PT).values():
        ajouter(a["mot"], a["genre"])
    for m in (MOMENTS_BR if br else MOMENTS_PT):
        ajouter(*m["w"])
    for n, j in enumerate(JOURS["pt"]):
        ajouter(j, "o" if n >= 5 else "a")
    ajouter("convite", "o")
    for i in INVITATIONS_PT:
        ajouter(*i["nomMot"])
    for v in ("ir", "vir", "combinar", "poder", "convidar", "levar", "celebrar"):
        ajouter(v, cat="verbe")
    return mots, sorted(set(absents))


def conjugaisons_pt(br):
    _, verbes = corpus_pt(br)
    vs = set(c["v"] for c in CONJ_PT) | set(m["w"][0] for m in (MOMENTS_BR if br else MOMENTS_PT) if m["w"][2] == "verbe") | {"combinar"}
    out = {}
    for v in sorted(vs):
        if v not in verbes:
            sys.exit("  verbe portugais absent : %s" % v)
        out[v] = verbes[v]["praesens"]
    return out


def verifier_pt():
    for br in (False, True):
        F, A, I, M = (FETES_BR, APPORTS_BR, INVITATIONS_BR, MOTIFS_BR) if br else (FETES_PT, APPORTS_PT, INVITATIONS_PT, MOTIFS_PT)
        for f, x in F.items():
            for a in x.get("aussi", []):
                if a not in F:
                    sys.exit("  pt %s : aussi inconnu %s" % (f, a))
            for i in x["img"]:
                if i in IMG_EXCLUES_PT or (i not in IMAGES and i not in REPRISES):
                    sys.exit("  pt %s : image exclue ou inconnue %s" % (f, i))
            for l in ("fr", "en"):
                if x.get("quand") and not x["t"][l][1]:
                    sys.exit("  pt %s : date %s absente" % (f, l))
                if x.get("wunsch") and not x["t"][l][2]:
                    sys.exit("  pt %s : souhait %s absent" % (f, l))
            if x.get("wunsch") and not (x.get("dans") and x.get("situation")):
                sys.exit("  pt %s : souhait sans « dans » ni situation" % f)
        # un souhait n'est jamais celui d'une autre fete, sauf « aussi » (Ano Novo / passagem)
        for f, x in F.items():
            for g, y in F.items():
                if f < g and x.get("wunsch") and x.get("wunsch") == y.get("wunsch") and g not in x.get("aussi", []):
                    sys.exit("  pt %s / %s : le meme souhait" % (f, g))
        for inv in I:
            if inv["fete"] and inv["fete"] not in F:
                sys.exit("  pt invitation %s : fete inconnue" % inv["id"])
            for a in inv["apports"]:
                if a not in A:
                    sys.exit("  pt invitation %s : apport inconnu %s" % (inv["id"], a))
            for p in inv["pour"] + inv["hote"].split(" e "):
                if p not in PERSONNES_PT:
                    sys.exit("  pt invitation %s : personne inconnue %s" % (inv["id"], p))
        for k, m in M.items():
            if any(l not in m["t"] for l in ("fr", "en")):
                sys.exit("  pt motif %s : traduction" % k)
        for m in (MOMENTS_BR if br else MOMENTS_PT):
            if m["img"] in IMG_EXCLUES_PT or m["img"] not in IMAGES and m["img"] not in REPRISES:
                sys.exit("  pt moment %s : image" % m["id"])
        # le sujet de la phrase a trou est toujours dit : « ___ » n'ouvre jamais la phrase
        for c in (CONJ_BR if br else CONJ_PT):
            if c["phrase"].startswith("___"):
                sys.exit("  pt conj %s : sujet absent" % c["phrase"])


def portugais(d):
    """Pose pt_ / br_ dans la donnee construite (ecrire_json), a cote de de et es."""
    def poser(o, pt, br=None):
        o["pt_"] = pt
        if br is not None and br != pt:
            o["br_"] = br
    poser(d["fetes"], FETES_PT, FETES_BR)
    poser(d["personnes"], PERSONNES_PT)
    poser(d["situationsT"], SITUATIONS_T_PT)
    poser(d["apports"], APPORTS_PT, APPORTS_BR)
    poser(d["invitations"], INVITATIONS_PT, INVITATIONS_BR)
    poser(d["motifs"], MOTIFS_PT, MOTIFS_BR)
    d["momentsPt"] = {}; poser(d["momentsPt"], MOMENTS_PT, MOMENTS_BR)
    d["conjPt"] = {}; poser(d["conjPt"], CONJ_PT, CONJ_BR)
    d["alPt"] = {}; poser(d["alPt"], AL_PT, AL_BR)
    d["imgExcluesPt"] = IMG_EXCLUES_PT
    for cle, br in (("pt_", False), ("br_", True)):
        d["mots"][cle], d["absents"][cle] = mots_du_theme_pt(br)
        d["conj"][cle] = conjugaisons_pt(br)


# ---------------------------------------------------------------------------------------------------------------
# LES IMAGES (4:3, aucun texte lisible). source : des references (personnes, lieux), jamais une description seule de
# nos personnes. reprise : une image deja faite, recadree en 4:3 par web.py (gratuit).
REPRISES = {"geburtstag": {"src": RACINE + "/visuel/prototype/geburtstag.webp", "haut": 0.36},
            "weihnachtsmarkt": {"src": RACINE + "/visuel/prototype/weihnachtsmarkt.webp", "haut": 0.15}}
PHOTO = (" A photorealistic photograph, natural light, natural colours, 4:3 landscape format. ABSOLUTELY NO readable text, "
         "no letters, no numbers, no logos, no signs, no captions, no watermark anywhere in the picture: every paper, screen, "
         "card and banner is blank or blurred. No alcohol: no wine, beer or champagne bottles or glasses anywhere. "
         "Hands: five fingers each, natural. Everybody is cheerful.")
GENS = "The people are exactly the people of the reference pictures, in this order: {qui}. Same faces, same hair, same age, same build. "
IMAGES = {
    # LES FETES
    "weihnachten": {"source": ["Anna", "Ben", "Mia", "salon-jan-katrin"],
                    "prompt": "Christmas Eve in the living room of the last reference picture (same furniture, same colours, same window), now decorated: a real fir Christmas tree with warm white fairy lights and red and golden baubles next to the sofa, wrapped presents with ribbons under it. Anna, the aunt, sits on the floor by the tree with the two children; the boy happily unwraps a present, the little girl laughs and holds a small teddy bear. Evening, warm cosy light."},
    "silvester":   {"source": ["Anna", "Lena", "Felix"],
                    "prompt": "New Year's Eve at midnight on a Berlin street of old five-storey apartment buildings: the three friends stand side by side seen from the front, wearing winter coats and scarves, each holding a burning sparkler, laughing and looking up; colourful fireworks burst in the night sky above the rooftops. Cold winter night, the light of the sparklers on their faces."},
    "ostern":      {"source": ["Ben", "Mia"],
                    "prompt": "Easter morning in a green spring garden with a lawn, a blossoming apple tree and yellow daffodils: the two children (the boy and the little girl of the references), in light spring jackets, joyfully hunt for brightly painted Easter eggs; the boy holds a small basket with coloured eggs, the little girl has just found a blue egg in the grass and smiles. Sunny morning."},
    "karneval":    {"prompt": "A carnival parade in a street of an old German town: a crowd of cheerful people in colourful costumes (clowns, pirates, a ladybird, a cowboy) with painted faces, colourful confetti and streamers in the air, a decorated parade float in the background. Daytime, February, people in costumes over warm clothes."},
    "hochzeit":    {"prompt": "A wedding: a happy young bride in a simple white dress and a groom in a dark suit come out of the door of an old town hall hand in hand, smiling, while friends and family on the steps throw rose petals and clap. Sunny day in June."},
    "kindergeburtstag": {"source": ["Ben", "Mia", "salon-jan-katrin"],
                    "prompt": "A child's birthday party in the living room of the last reference picture (same furniture, same colours, same window), decorated with colourful balloons and a paper garland: the boy wears a colourful paper party hat and blows out the eight candles on a chocolate birthday cake on the table, cheeks puffed, delighted; his little sister and three other happy children in party hats clap around the table. Afternoon light."},
    "uvas":        {"source": ["Carmen", "Javier", "Ines"],
                    "prompt": "New Year's Eve in Spain, a few seconds before midnight, in a bright Madrid living room: the three friends stand in front of a television (the screen shows only a blurred clock tower at night, nothing readable), each holding a small glass bowl with exactly twelve green grapes, laughing as they eat the first grapes one by one. Paper streamers and a few gold balloons. Night, warm indoor light."},
    "reyes":       {"prompt": "The morning of the sixth of January in a Spanish family dining room: on the table a large ring-shaped roscon de Reyes cake decorated with candied fruit and almond slices, a golden paper crown next to it, cups of hot chocolate; a smiling grandmother and a happy boy wearing a golden paper crown, opened presents and wrapping paper on the chairs. Morning light."},
    "semanasanta": {"prompt": "A Holy Week procession in a narrow street of an old Andalusian town with white houses and iron balconies, seen from a distance: a richly decorated float covered with white flowers and tall lit candles is carried slowly through the crowd, a brass band follows; the spectators on the pavements watch quietly. Spring evening, golden light."},
    "muertos":     {"prompt": "A Mexican Day of the Dead home altar (ofrenda) on several steps covered with a white cloth: bright orange marigold flowers, lit candles, colourful sugar skulls, a round pan de muerto bread, oranges, a cup of hot chocolate, and colourful cut paper banners (papel picado) above, with only geometric patterns and flowers cut in them, no letters. A few framed photographs whose faces are blurred. Warm candle light, no people."},
    # LES MOMENTS DE MARK
    "einladen":    {"source": ["Mark", "cuisine-mark"],
                    "prompt": "The man of the first reference sits at the wooden table of the kitchen of the second reference picture (same sage green wall, same round clock) and types a message on his smartphone with a happy smile, a paper calendar and a cup of coffee in front of him. The phone screen is blank and bright. Seen at three quarters, from the waist up."},
    "karte":       {"source": ["Mark", "cuisine-mark"],
                    "prompt": "The man of the first reference sits at the wooden table of the kitchen of the second reference picture and writes in a greeting card with a pen, smiling; the card has a simple drawn yellow balloon on its front, no letters; a small wrapped present with a ribbon lies next to it. Seen at three quarters, from the waist up."},
    "mitbringen":  {"source": ["Mark"],
                    "prompt": "The man of the reference stands at the open front door of a Berlin apartment, in a winter jacket, holding a large glass bowl of colourful salad in both hands, smiling; a friendly woman in her thirties (not in the references, brown hair in a bun) opens the door and welcomes him with a wide smile. Warm light from inside the flat, the dark staircase behind him. Seen from the side, both from the waist up."},
    "absagen":     {"source": ["Mark"],
                    "prompt": "The man of the reference stands by the window of a bright office and talks on his mobile phone with a sorry, apologetic expression, one hand raised a little as if to say sorry; a laptop and papers on the desk behind him. Seen at three quarters, from the waist up."},
    "planen":      {"source": ["Mark", "Anna", "cuisine-mark"],
                    "prompt": "The man and the woman of the first two references sit side by side at the wooden table of the kitchen of the third reference picture and plan a party together: she points at a paper wall calendar lying open on the table, he writes a list in a notebook with a pen, both smiling and talking. The calendar and the notebook cannot be read. Seen from the front, from the waist up."},
}
ESSAI = ["weihnachten", "silvester", "ostern", "uvas", "planen", "mitbringen"]


def charge(f):
    return json.load(io.open(os.path.join(RACINE, f), encoding="utf-8"))


def corpus_noms(langue):
    out = {}
    for t in charge("themes.json" if langue == "de" else "espanol/datos/temas.json")["themes"]:
        for m in t["mots"]:
            out.setdefault((m["mot"], m.get("genre")), m)
    return out


def corpus_liste(fichier, cle):
    out = {}
    for niv, l in charge(fichier).items():
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
    adverbes = corpus_liste("adverbe.json" if langue == "de" else "espanol/datos/adverbios.json", "mot")
    mots, absents = [], []

    def ajouter(mot, genre=None, cat=None):
        if (mot, genre, cat) in [(m["mot"], m.get("genre"), m.get("cat")) for m in mots]:
            return
        e = verbes.get(mot) if cat == "verbe" else adverbes.get(mot) if cat == "adverbe" else noms.get((mot, genre))
        if e:
            g = {l: glose(e, l) for l in LANGUES[langue]}
        elif mot in AJOUTS_TRAD[langue]:
            g = AJOUTS_TRAD[langue][mot]; absents.append(mot)
        else:
            sys.exit("  %s (%s) absent du corpus %s et des ajouts" % (mot, genre or cat, langue))
        manque = [l for l, v in g.items() if not v]
        if manque:
            sys.exit("  %s (%s) : pas de traduction en %s" % (mot, langue, ", ".join(manque)))
        w = {"mot": mot, "g": g}
        if genre:
            w["genre"] = genre
        if cat:
            w["cat"] = cat
        mots.append(w)
    for f in FETES[langue].values():
        ajouter(f["mot"], f["genre"])
    for a in APPORTS[langue].values():
        ajouter(a["mot"], a["genre"])
    for m in MOMENTS:
        ajouter(m["v"][langue], cat="verbe")
    for j in JOURS[langue]:
        ajouter(j, "der" if langue == "de" else "el")
    if langue == "de":
        ajouter("Einladung", "die"); ajouter("Zeit", "die")
        ajouter("Party", "die"); ajouter("Fest", "das"); ajouter("Feier", "die"); ajouter("Einweihungsparty", "die")
        ajouter("gern", cat="adverbe"); ajouter("leider", cat="adverbe")
    else:
        ajouter("invitación", "la"); ajouter("fiesta", "la"); ajouter("cena", "la")
        for v in ("venir", "ir", "quedar", "poder", "invitar", "traer", "celebrar"):
            ajouter(v, cat="verbe")
    return mots, sorted(set(absents))


def conjugaisons(langue):
    verbes = corpus_liste("verbe.json" if langue == "de" else "espanol/datos/verbos.json", "infinitif")
    vs = set(m["v"][langue] for m in MOMENTS) | ({"kommen", "können", "haben", "einladen", "mitbringen"} if langue == "de" else {"poder", "traer", "invitar", "celebrar", "venir", "quedar", "ir"})
    return {v: verbes[v]["praesens"] for v in sorted(vs)}


def verifier():
    for langue in ("de", "es"):
        P = PERSONNES[langue]
        for f, x in FETES[langue].items():
            for a in x.get("aussi", []):
                if a not in FETES[langue]:
                    sys.exit("  %s %s : aussi inconnu %s" % (langue, f, a))
            for i in x["img"]:
                if i not in IMAGES and i not in REPRISES:
                    sys.exit("  %s %s : image inconnue %s" % (langue, f, i))
            for l in TL[langue]:
                if l not in x["t"]:
                    sys.exit("  %s %s : traduction %s absente" % (langue, f, l))
                if x.get("quand") and not x["t"][l][1]:
                    sys.exit("  %s %s : date %s absente" % (langue, f, l))
                if x.get("wunsch") and not x["t"][l][2]:
                    sys.exit("  %s %s : souhait %s absent" % (langue, f, l))
        for inv in INVITATIONS[langue]:
            if inv["fete"] and inv["fete"] not in FETES[langue]:
                sys.exit("  invitation %s : fete inconnue" % inv["id"])
            for a in inv["apports"]:
                if a not in APPORTS[langue]:
                    sys.exit("  invitation %s : apport inconnu %s" % (inv["id"], a))
            for p in inv["pour"]:
                if p not in P:
                    sys.exit("  invitation %s : personne inconnue %s" % (inv["id"], p))
            for l in TL[langue]:
                if l not in inv["t"]:
                    sys.exit("  invitation %s : traduction %s" % (inv["id"], l))
        for k, a in APPORTS[langue].items():
            for l in TL[langue]:
                if l not in a["t"]:
                    sys.exit("  apport %s : traduction %s" % (k, l))
        for k, m in MOTIFS[langue].items():
            for l in TL[langue]:
                if l not in m["t"]:
                    sys.exit("  motif %s : traduction %s" % (k, l))
    for m in MOMENTS:
        if m["img"] not in IMAGES and m["img"] not in REPRISES:
            sys.exit("  moment %s : image inconnue" % m["id"])


def ecrire_json():
    verifier()
    d = {"fetes": FETES, "imgLangues": IMG_LANGUES, "personnes": PERSONNES, "sexe": SEXE, "situationsT": SITUATIONS_T, "apports": APPORTS, "invitations": INVITATIONS, "motifs": MOTIFS,
         "jours": JOURS, "mois": MOIS, "moments": MOMENTS, "conjEs": CONJ_ES, "alEs": AL_ES, "zuDe": ZU_DE, "mots": {}, "absents": {}, "conj": {}}
    for langue in ("de", "es"):
        d["mots"][langue], d["absents"][langue] = mots_du_theme(langue)
        d["conj"][langue] = conjugaisons(langue)
    noms = list(IMAGES) + list(REPRISES)
    d["images"] = {i: os.path.exists(os.path.join(RACINE, "visuel", "prototype", "fetes", i + ".webp")) for i in noms}
    verifier_pt()
    portugais(d)
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    chemin = os.path.join(RACINE, "visuel", "prototype", "fetes", "fetes.json")
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(texte)
    for langue in ("de", "es", "pt_", "br_"):
        print("  %s : %d mots, dont %d absents du corpus (%s)" % (langue, len(d["mots"][langue]), len(d["absents"][langue]), ", ".join(d["absents"][langue])))
    print("  images : %d / %d faites" % (sum(d["images"].values()), len(noms)))
    return d


def reference(nom):
    """Le chemin d'une reference en png (fal n'accepte pas toujours le webp) : un webp se convertit une fois."""
    src = REFERENCES[nom]
    if not src.endswith(".webp"):
        return src
    from PIL import Image
    png = os.path.join(DOSSIER, "ref-" + nom + ".png")
    if not os.path.exists(png):
        Image.open(src).convert("RGB").save(png)
    return png


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    ecrire_json()
    if "--json" in sys.argv:
        return
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or (ESSAI if "--essai" in sys.argv else list(IMAGES))
    inconnus = [n for n in noms if n not in IMAGES]
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

    def prompt_de(nom):
        im = IMAGES[nom]
        gens = [s for s in im.get("source", []) if s in ("Mark", "Anna", "Lena", "Felix", "Ben", "Mia", "Carmen", "Javier", "Ines")]
        return (GENS.format(qui=", ".join(gens)) if gens else "") + im["prompt"] + PHOTO
    if montrer:
        for nom in a_faire:
            print("\n  %s%s\n  %s" % (nom, " (retouche de %s)" % "+".join(IMAGES[nom]["source"]) if IMAGES[nom].get("source") else "", prompt_de(nom)))
        return
    import omnihuman as O                                    # noqa: E402
    if not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    for nom in a_faire:
        source, prompt = IMAGES[nom].get("source"), prompt_de(nom)
        print("\n  %s\n  %s" % (nom, prompt))
        corps = {"prompt": prompt, "aspect_ratio": "4:3", "resolution": "2K", "output_format": "png", "num_images": 1}
        modele = TEXTE
        if source:
            corps["image_urls"] = [O.deposer(reference(s), "image/png", cle)[0] for s in source]
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
