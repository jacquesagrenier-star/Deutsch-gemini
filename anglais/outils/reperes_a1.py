# -*- coding: utf-8 -*-
"""Les reperes de l'anglais (nombres, jours, mois, heure, couleurs, pluriel),
au format de espanol/datos/reperes.json. SOURCE : on corrige ici, puis
python anglais/outils/construire.py (anglais/datos et datos-gb).

Les nombres portent une prononciation figuree pour un francophone, comme
l'espagnol (« θÉ-ro ») : la syllabe forte en MAJUSCULES, θ pour le th de
« three », ð pour celui de « the ».
"""

def sens(fr):
    return {"fr": fr}

NOMBRES_0_20 = [
    ("zero", "0", "ZI-rô"), ("one", "1", "OUANN"), ("two", "2", "TOU"), ("three", "3", "θRI"),
    ("four", "4", "FOR"), ("five", "5", "FAÏV"), ("six", "6", "SIKS"), ("seven", "7", "SÈ-veun"),
    ("eight", "8", "ÉÏT"), ("nine", "9", "NAÏN"), ("ten", "10", "TÈN"), ("eleven", "11", "i-LÈ-veun"),
    ("twelve", "12", "TOUÈLV"), ("thirteen", "13", "θeur-TINN"), ("fourteen", "14", "for-TINN"),
    ("fifteen", "15", "fif-TINN"), ("sixteen", "16", "siks-TINN"), ("seventeen", "17", "sè-veun-TINN"),
    ("eighteen", "18", "éï-TINN"), ("nineteen", "19", "naïn-TINN"), ("twenty", "20", "TOUÈN-ti"),
]
NOMBRES_20_100 = [
    ("twenty", "20", "TOUÈN-ti"), ("twenty-one", "21", "touèn-ti-OUANN"), ("twenty-two", "22", "touèn-ti-TOU"),
    ("thirty", "30", "θEUR-di"), ("forty", "40", "FOR-di"), ("fifty", "50", "FIF-ti"),
    ("sixty", "60", "SIKS-ti"), ("seventy", "70", "SÈ-veun-di"), ("eighty", "80", "ÉÏ-di"),
    ("ninety", "90", "NAÏN-di"), ("one hundred", "100", "ouann HEUN-drid"),
]
X_20_100 = [("twenty-three", "23"), ("thirty-six", "36"), ("forty-five", "45"), ("fifty-eight", "58"),
            ("sixty-four", "64"), ("seventy-two", "72"), ("eighty-one", "81"), ("ninety-nine", "99")]
NOMBRES_100_1000 = [
    ("one hundred", "100", "ouann HEUN-drid"), ("two hundred", "200", "tou HEUN-drid"),
    ("three hundred", "300", "θri HEUN-drid"), ("five hundred", "500", "faïv HEUN-drid"),
    ("one thousand", "1000", "ouann θAOU-zeund"),
]
# L'americain dit « one hundred twenty », le britannique « one hundred AND
# twenty » : construire.py ajoute le « and » dans datos-gb.
X_100_1000 = [("one hundred one", "101"), ("one hundred twenty", "120"), ("two hundred fifty", "250"),
              ("three hundred forty", "340"), ("six hundred seventy-five", "675"), ("nine hundred ninety", "990")]

JOURS = [("Monday", "lundi"), ("Tuesday", "mardi"), ("Wednesday", "mercredi"), ("Thursday", "jeudi"),
         ("Friday", "vendredi"), ("Saturday", "samedi"), ("Sunday", "dimanche")]
MOIS = [("January", "janvier"), ("February", "février"), ("March", "mars"), ("April", "avril"),
        ("May", "mai"), ("June", "juin"), ("July", "juillet"), ("August", "août"),
        ("September", "septembre"), ("October", "octobre"), ("November", "novembre"), ("December", "décembre")]
HEURES = [("one o'clock", "1 h"), ("two o'clock", "2 h"), ("three o'clock", "3 h"), ("four o'clock", "4 h"),
          ("five o'clock", "5 h"), ("six o'clock", "6 h"), ("seven o'clock", "7 h"), ("eight o'clock", "8 h"),
          ("nine o'clock", "9 h"), ("ten o'clock", "10 h"), ("eleven o'clock", "11 h"), ("twelve o'clock", "12 h")]
COULEURS = [("red", "rouge", "#d93a32"), ("blue", "bleu", "#2f6fd6"), ("green", "vert", "#2e9d4f"),
            ("yellow", "jaune", "#f2c230"), ("black", "noir", "#1b1b1b"), ("white", "blanc", "#f7f7f2"),
            ("gray", "gris", "#8a8f96"), ("brown", "marron", "#7a4e2d"), ("orange", "orange", "#f08a24"),
            ("pink", "rose", "#f29bb8"), ("purple", "violet", "#7b4bb3")]
PLURIEL_L = [["books", "a book → +s"], ["buses", "a bus → +es"], ["cities", "a city → -ies"],
             ["knives", "a knife → -ves"], ["children", "a child → irrégulier"], ["men", "a man → irrégulier"],
             ["feet", "a foot → irrégulier"], ["people", "a person → irrégulier"]]
PLURIEL_X = [["a cat", "cats", "+s", "cates", "cat"], ["a box", "boxes", "+es", "boxs", "boxies"],
             ["a baby", "babies", "-y → -ies", "babys", "babyes"], ["a boy", "boys", "+s (voyelle + y)", "boies", "boyes"],
             ["a woman", "women", "irrégulier", "womans", "womens"], ["a tooth", "teeth", "irrégulier", "tooths", "teeths"],
             ["a leaf", "leaves", "-f → -ves", "leafs", "leafes"], ["a child", "children", "irrégulier", "childs", "childrens"],
             ["a glass", "glasses", "+es", "glasss", "glassies"], ["a mouse", "mice", "irrégulier", "mouses", "mices"]]

REPERES = [
    {"id": "n0-20", "type": "nombre", "t": sens("Les nombres de 0 à 20"),
     "a": sens("De 13 à 19, la fin -teen porte l'accent : thirTEEN, fourTEEN. C'est ce qui les distingue des dizaines, accentuées au début : THIRty, FORty. Zéro se dit aussi « oh » dans un numéro de téléphone."),
     "l": [[m, n, sens(p)] for m, n, p in NOMBRES_0_20], "x": []},
    {"id": "n20-100", "type": "nombre", "t": sens("Les dizaines, jusqu'à 100"),
     "a": sens("On relie la dizaine et l'unité par un trait d'union : twenty-one, forty-five. En américain, le t entre deux voyelles se dit presque comme un d : thirty « θEUR-di »."),
     "l": [[m, n, sens(p)] for m, n, p in NOMBRES_20_100], "x": [list(x) for x in X_20_100]},
    {"id": "n100-1000", "type": "nombre", "t": sens("Les centaines, jusqu'à 1000"),
     "a": sens("Hundred et thousand ne prennent jamais de s après un nombre : two hundred, five thousand. L'américain dit one hundred twenty ; le britannique ajoute and : one hundred and twenty."),
     "l": [[m, n, sens(p)] for m, n, p in NOMBRES_100_1000], "x": [list(x) for x in X_100_1000]},
    {"id": "jours", "type": "suite", "t": sens("Les jours de la semaine"),
     "a": sens("Toujours une majuscule : Monday. « Lundi » (quand ?) se dit on Monday ; « le lundi » (chaque lundi) : on Mondays."),
     "l": [[m, sens(f)] for m, f in JOURS],
     "p": [["Monday, Tuesday, Wednesday", sens("lundi, mardi, mercredi")],
           ["Thursday, Friday, Saturday, Sunday", sens("jeudi, vendredi, samedi, dimanche")]]},
    {"id": "mois", "type": "suite", "t": sens("Les mois de l'année"),
     "a": sens("Une majuscule aussi : January. « En janvier » se dit in January. Les dates américaines mettent le mois d'abord : 7/4 = le 4 juillet."),
     "l": [[m, sens(f)] for m, f in MOIS],
     "p": [["January, February, March, April", sens("janvier, février, mars, avril")],
           ["May, June, July, August", sens("mai, juin, juillet, août")],
           ["September, October, November, December", sens("septembre, octobre, novembre, décembre")]]},
    {"id": "heures", "type": "suite", "t": sens("L'heure"),
     "a": sens("« Il est 3 h » : It's three o'clock. Pour la demie : half past three ; pour le quart : a quarter past three (3 h 15), a quarter to four (3 h 45). On compte sur 12 heures : 3 p.m. = 15 h, 3 a.m. = 3 h du matin."),
     "l": [[m, sens(f)] for m, f in HEURES],
     "p": [["one o'clock, two o'clock, three o'clock", sens("1 h, 2 h, 3 h")],
           ["It's half past seven.", sens("Il est 7 h 30.")],
           ["It's a quarter past nine.", sens("Il est 9 h 15.")]]},
    {"id": "couleurs", "type": "couleur", "t": sens("Les couleurs"),
     "a": sens("Les couleurs ne s'accordent jamais : a red car, two red cars. Elles se placent avant le nom. Gray s'écrit grey en anglais britannique."),
     "l": [[m, sens(f), h] for m, f, h in COULEURS]},
    {"id": "pluriel", "type": "pluriel", "t": sens("Le pluriel"),
     "a": sens("Presque toujours -s. Après s, sh, ch, x : -es. Consonne + y : -ies. Une poignée d'irréguliers à connaître par cœur : men, women, children, feet, teeth, people, mice."),
     "l": PLURIEL_L, "x": PLURIEL_X},
]
