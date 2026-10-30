# -*- coding: utf-8 -*-
"""Les reperes du portugais (nombres, jours, mois, heure, couleurs, alphabet,
genre, pluriel), au format de espanol/datos/reperes.json. SOURCE : on corrige
ici, puis python portugais/outils/construire.py.

Les nombres portent une prononciation figuree pour un francophone, celle de
Lisbonne : la syllabe forte en MAJUSCULES ; le e atone presque avale (« d' ») ;
le s final dit « ch » (« dois » : DOÏCH) ; les voyelles nasales notees « ñ ».
"""

def sens(fr):
    return {"fr": fr}

NOMBRES_0_20 = [
    ("zero", "0", "ZÈ-rou"), ("um", "1", "OUñ"), ("dois", "2", "DOÏCH"), ("três", "3", "TRÉCH"),
    ("quatro", "4", "KOUA-trou"), ("cinco", "5", "SIñ-kou"), ("seis", "6", "SÂÏCH"), ("sete", "7", "SÈT'"),
    ("oito", "8", "OÏ-tou"), ("nove", "9", "NOV'"), ("dez", "10", "DÈCH"), ("onze", "11", "Oñ-z'"),
    ("doze", "12", "DÔ-z'"), ("treze", "13", "TRÉ-z'"), ("catorze", "14", "ka-TÔR-z'"),
    ("quinze", "15", "KIñ-z'"), ("dezasseis", "16", "d'za-SÂÏCH"), ("dezassete", "17", "d'za-SÈT'"),
    ("dezoito", "18", "d'ZOÏ-tou"), ("dezanove", "19", "d'za-NOV'"), ("vinte", "20", "VIñ-t'"),
]
NOMBRES_20_100 = [
    ("vinte", "20", "VIñ-t'"), ("vinte e um", "21", "viñ-ti-OUñ"), ("vinte e dois", "22", "viñ-ti-DOÏCH"),
    ("trinta", "30", "TRIñ-ta"), ("quarenta", "40", "koua-RÉñ-ta"), ("cinquenta", "50", "siñ-KOUÉñ-ta"),
    ("sessenta", "60", "s'-SÉñ-ta"), ("setenta", "70", "s'-TÉñ-ta"), ("oitenta", "80", "oï-TÉñ-ta"),
    ("noventa", "90", "nou-VÉñ-ta"), ("cem", "100", "SÂÏñ"),
]
X_20_100 = [("vinte e três", "23"), ("trinta e seis", "36"), ("quarenta e cinco", "45"), ("cinquenta e oito", "58"),
            ("sessenta e quatro", "64"), ("setenta e dois", "72"), ("oitenta e um", "81"), ("noventa e nove", "99")]
NOMBRES_100_1000 = [
    ("cem", "100", "SÂÏñ"), ("cento e um", "101", "SÉñ-tou i OUñ"), ("duzentos", "200", "dou-ZÉñ-touch"),
    ("trezentos", "300", "tr'-ZÉñ-touch"), ("quinhentos", "500", "ki-GNÉñ-touch"), ("mil", "1000", "MIL"),
]
X_100_1000 = [("cento e vinte", "120"), ("duzentos e cinquenta", "250"), ("trezentos e quarenta", "340"),
              ("seiscentos e setenta e cinco", "675"), ("novecentos e noventa", "990"), ("mil e quinhentos", "1500")]

JOURS = [("segunda-feira", "lundi"), ("terça-feira", "mardi"), ("quarta-feira", "mercredi"),
         ("quinta-feira", "jeudi"), ("sexta-feira", "vendredi"), ("sábado", "samedi"), ("domingo", "dimanche")]
MOIS = [("janeiro", "janvier"), ("fevereiro", "février"), ("março", "mars"), ("abril", "avril"),
        ("maio", "mai"), ("junho", "juin"), ("julho", "juillet"), ("agosto", "août"),
        ("setembro", "septembre"), ("outubro", "octobre"), ("novembro", "novembre"), ("dezembro", "décembre")]
HEURES = [("uma hora", "1 h"), ("duas horas", "2 h"), ("três horas", "3 h"), ("quatro horas", "4 h"),
          ("cinco horas", "5 h"), ("seis horas", "6 h"), ("sete horas", "7 h"), ("oito horas", "8 h"),
          ("nove horas", "9 h"), ("dez horas", "10 h"), ("onze horas", "11 h"), ("meio-dia", "midi")]
COULEURS = [("vermelho", "rouge", "#d93a32"), ("azul", "bleu", "#2f6fd6"), ("verde", "vert", "#2e9d4f"),
            ("amarelo", "jaune", "#f2c230"), ("preto", "noir", "#1b1b1b"), ("branco", "blanc", "#f7f7f2"),
            ("cinzento", "gris", "#8a8f96"), ("castanho", "marron", "#7a4e2d"), ("cor de laranja", "orange", "#f08a24"),
            ("cor-de-rosa", "rose", "#f29bb8"), ("roxo", "violet", "#7b4bb3")]
ALPHABET = [
    ("á", "A", ["E", "O"]), ("bê", "B", ["V", "P"]), ("cê", "C", ["S", "Ç"]), ("dê", "D", ["T", "B"]),
    ("é", "E", ["I", "A"]), ("efe", "F", ["V", "S"]), ("guê", "G", ["J", "Q"]), ("agá", "H", ["A", "G"]),
    ("i", "I", ["E", "Y"]), ("jota", "J", ["G", "X"]), ("capa", "K", ["Q", "C"]), ("ele", "L", ["R", "E"]),
    ("eme", "M", ["N", "E"]), ("ene", "N", ["M", "H"]), ("ó", "O", ["U", "A"]), ("pê", "P", ["B", "T"]),
    ("quê", "Q", ["K", "C"]), ("erre", "R", ["L", "H"]), ("esse", "S", ["Z", "C"]), ("tê", "T", ["D", "P"]),
    ("u", "U", ["O", "V"]), ("vê", "V", ["B", "F"]), ("dâblio", "W", ["V", "U"]), ("xis", "X", ["S", "Z"]),
    ("ípsilon", "Y", ["I", "J"]), ("zê", "Z", ["S", "X"]),
]
EPELER = [["Lisboa", "L-I-S-B-O-A"], ["Porto", "P-O-R-T-O"], ["Silva", "S-I-L-V-A"], ["Sousa", "S-O-U-S-A"],
          ["Coimbra", "C-O-I-M-B-R-A"], ["Faro", "F-A-R-O"]]
GENRE_M_L = [["o livro", "-o → o"], ["o carro", "-o → o"], ["o jardim", "-im → o"], ["o hotel", "-l → o"],
             ["o dia", "⚠️ -a → o"], ["o mapa", "⚠️ -a → o"], ["o problema", "⚠️ -ma → o"], ["o sofá", "⚠️ -á → o"]]
GENRE_M_X = [["o prato", "-o → o"], ["o quarto", "-o → o"], ["o jornal", "-l → o"], ["o clima", "⚠️ -ma → o"],
             ["o pão", "-ão (concret) → o"], ["o avião", "-ão (concret) → o"], ["o café", "-é → o"], ["o leite", "-e → o"]]
GENRE_F_L = [["a casa", "-a → a"], ["a mesa", "-a → a"], ["a estação", "-ção → a"], ["a cidade", "-dade → a"],
             ["a viagem", "-agem → a"], ["a mão", "⚠️ -ão → a"], ["a foto", "⚠️ -o → a"], ["a moto", "⚠️ -o → a"]]
GENRE_F_X = [["a cama", "-a → a"], ["a lição", "-ção → a"], ["a universidade", "-dade → a"], ["a garagem", "-agem → a"],
             ["a paragem", "-agem → a"], ["a profissão", "-são → a"], ["a nuvem", "⚠️ -em → à apprendre (o homem)"], ["a ponte", "-e → a"]]
PLURIEL_L = [["as casas", "a casa → +s"], ["os homens", "o homem → -ns"], ["as flores", "a flor → +es"],
             ["os hotéis", "o hotel → -éis"], ["os jornais", "o jornal → -ais"], ["as estações", "a estação → -ões"],
             ["os pães", "o pão → -ães"], ["as mãos", "a mão → -ãos"]]
PLURIEL_X = [["a casa", "as casas", "+s", "as casaes", "os casas"], ["o homem", "os homens", "-m → -ns", "os homems", "os homenes"],
             ["a flor", "as flores", "+es", "as flors", "as floris"], ["o hotel", "os hotéis", "-el → -éis", "os hoteles", "os hotels"],
             ["o animal", "os animais", "-al → -ais", "os animals", "os animales"], ["a lição", "as lições", "-ão → -ões", "as lição", "as liçãos"],
             ["o pão", "os pães", "-ão → -ães", "os pãos", "os pões"], ["a mão", "as mãos", "-ão → -ãos", "as mães", "as mões"],
             ["o mês", "os meses", "-ês → -eses", "os mêss", "os mês"], ["o lápis", "os lápis", "invariable", "os lápises", "os lápiss"]]

REPERES = [
    {"id": "n0-20", "type": "nombre", "t": sens("Les nombres de 0 à 20"),
     "a": sens("Un et deux ont un féminin : um, uma ; dois, duas (duas horas, deux heures). Au Portugal, 16, 17 et 19 s'écrivent dezasseis, dezassete, dezanove (le Brésil dit dezesseis, dezessete, dezenove). Le s final se dit « ch » : dois, três, seis."),
     "l": [[m, n, sens(p)] for m, n, p in NOMBRES_0_20], "x": []},
    {"id": "n20-100", "type": "nombre", "t": sens("Les dizaines, jusqu'à 100"),
     "a": sens("On relie la dizaine et l'unité par e (et) : vinte e um, quarenta e cinco. Le e se dit « i », lié au mot d'avant : « viñ-ti-OUñ ». Cem, c'est cent tout rond ; devant un autre nombre, il devient cento : cento e um."),
     "l": [[m, n, sens(p)] for m, n, p in NOMBRES_20_100], "x": [list(x) for x in X_20_100]},
    {"id": "n100-1000", "type": "nombre", "t": sens("Les centaines, jusqu'à 1000"),
     "a": sens("Les centaines s'accordent avec le nom : duzentos euros, mais duzentas pessoas. Le e revient entre chaque partie : trezentos e quarenta. Mil ne prend jamais um devant : mil euros."),
     "l": [[m, n, sens(p)] for m, n, p in NOMBRES_100_1000], "x": [list(x) for x in X_100_1000]},
    {"id": "jours", "type": "suite", "t": sens("Les jours de la semaine"),
     "a": sens("Du lundi au vendredi, on compte : segunda-feira (deuxième), terça-feira (troisième)… à l'oral, on dit souvent segunda, terça, quarta. Pas de majuscule. « Lundi » (quand ?) : na segunda-feira ; « le lundi » (chaque lundi) : à segunda-feira, às segundas."),
     "l": [[m, sens(f)] for m, f in JOURS],
     "p": [["segunda-feira, terça-feira, quarta-feira", sens("lundi, mardi, mercredi")],
           ["quinta-feira, sexta-feira, sábado, domingo", sens("jeudi, vendredi, samedi, dimanche")]]},
    {"id": "mois", "type": "suite", "t": sens("Les mois de l'année"),
     "a": sens("Pas de majuscule non plus (depuis la réforme de 1990) : janeiro, fevereiro. « En janvier » : em janeiro. La date : dia 5 de maio, le 5 mai."),
     "l": [[m, sens(f)] for m, f in MOIS],
     "p": [["janeiro, fevereiro, março, abril", sens("janvier, février, mars, avril")],
           ["maio, junho, julho, agosto", sens("mai, juin, juillet, août")],
           ["setembro, outubro, novembro, dezembro", sens("septembre, octobre, novembre, décembre")]]},
    {"id": "heures", "type": "suite", "t": sens("L'heure"),
     "a": sens("« Il est une heure » : é uma hora ; à partir de deux, au pluriel : são duas horas, são três horas. La demie : e meia (três e meia) ; le quart : e um quarto ; « moins le quart » : um quarto para as quatro. « À huit heures » : às oito."),
     "l": [[m, sens(f)] for m, f in HEURES],
     "p": [["é uma hora, são duas horas, são três horas", sens("il est 1 h, 2 h, 3 h")],
           ["São sete e meia.", sens("Il est 7 h 30.")],
           ["São nove e um quarto.", sens("Il est 9 h 15.")]]},
    {"id": "couleurs", "type": "couleur", "t": sens("Les couleurs"),
     "a": sens("Les couleurs s'accordent comme les adjectifs : um carro vermelho, uma casa vermelha. Azul et verde ne changent qu'au pluriel (azuis, verdes). Cor-de-rosa et cor de laranja sont invariables. Gris se dit cinzento au Portugal (cinza au Brésil)."),
     "l": [[m, sens(f), h] for m, f, h in COULEURS]},
    {"id": "alphabet", "type": "lettre", "t": sens("L'alphabet, pour épeler"),
     "a": sens("Le h ne se prononce jamais (agá). Ç (cê cedilhado) se dit « s ». K, w et y ne servent que dans les mots étrangers. Pour épeler un nom au téléphone, on dit les lettres une à une : S de Sousa."),
     "l": [[a, b, c] for a, b, c in ALPHABET], "p": [[m, sens(e)] for m, e in EPELER]},
    {"id": "genre-m", "type": "genre", "t": sens("Le genre : les terminaisons masculines (o)"),
     "a": sens("-o, -l, -im, -r : presque toujours o. Méfie-toi de -ma : o problema, o clima, o sistema (mots savants), mais a cama. Les pièges à retenir : o dia, o mapa, o sofá."),
     "l": GENRE_M_L, "x": GENRE_M_X},
    {"id": "genre-f", "type": "genre", "t": sens("Le genre : les terminaisons féminines (a)"),
     "a": sens("-a, -ção, -são, -dade, -agem : a. Pièges fréquents : a mão, a foto, a tribo. Un mot en -e ne dit rien (o leite, a ponte, a noite) : apprends l'article avec le mot."),
     "l": GENRE_F_L, "x": GENRE_F_X},
    {"id": "pluriel", "type": "pluriel", "t": sens("Le pluriel"),
     "a": sens("Voyelle → +s. -m → -ns. -r, -z → +es. -l → -is (hotel → hotéis, animal → animais). Les -ão ont trois pluriels, à apprendre avec le mot : -ões (le plus courant), -ães, -ãos. Un mot en -s non accentué ne change pas (o lápis → os lápis)."),
     "l": PLURIEL_L, "x": PLURIEL_X},
]
