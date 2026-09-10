# -*- coding: utf-8 -*-
"""praepWoWohinExercises (50) : Wechselpraepositionen, position ou deplacement.

LE JEU EST FAIT DE PAIRES. Presque chaque phrase revient deux fois -- une fois
immobile (Wo ? Dativ), une fois en mouvement (Wohin ? Akkusativ) -- avec le
meme decor et le verbe qui change. L'explication suit : un prefixe pris dans
une vingtaine de formules, puis toujours « -> Wo ? -> Dativ : <groupe> ».
Le groupe est ALLEMAND et ne se traduit pas.

⚠️ UNE DISTINCTION QUE L'UKRAINIEN NE PORTE PAS TOUJOURS, ET QU'ON NE FORCE
PAS. « біля » regit le genitif quel que soit le mouvement : « біля дверей »
traduit aussi bien « neben der Tuer » que « neben die Tuer ». La traduction
ukrainienne ne montre donc pas le contraste dans ces cas-la -- et c'est juste :
elle traduit la phrase, elle n'enseigne pas la regle. La regle est dans
l'allemand de la question et dans l'explication, qui, elles, opposent bien
Dativ et Akkusativ.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------- les prefixes d'explication
# ⚠️ DU PLUS LONG AU PLUS COURT. « decrit le fait de poser quelque part »
# contient presque « decrit le fait de poser a plat quelque part » : teste dans
# le mauvais ordre, le plus court mange le plus long et la moitie du sens part.
PREFIXES = [
 ("« %s » à la forme intransitive décrit une position suspendue fixe",
  "« %s » у неперехідній формі описує нерухоме висіння"),
 ("« %s » à la forme transitive décrit le fait de suspendre quelque part",
  "« %s » у перехідній формі описує дію повісити щось кудись"),
 ("« %s » décrit le fait de mettre en position assise",
  "« %s » описує дію посадити когось"),
 ("« %s » décrit le fait de mettre debout quelque part",
  "« %s » описує дію поставити щось кудись"),
 ("« %s » décrit le fait de prendre place quelque part",
  "« %s » описує дію сісти десь"),
 ("« %s » décrit le fait de poser à plat quelque part",
  "« %s » описує дію покласти щось плазом кудись"),
 ("« %s » décrit le fait de poser quelque part",
  "« %s » описує дію покласти щось кудись"),
 ("« %s » décrit une position à plat, sans mouvement",
  "« %s » описує положення лежачи, без руху"),
 ("« %s » décrit une position fixe (debout)",
  "« %s » описує нерухоме положення (стоячи)"),
 ("« %s » décrit une position assise fixe",
  "« %s » описує нерухоме положення сидячи"),
 ("« %s » intransitif décrit une position fixe",
  "« %s » неперехідне описує нерухоме положення"),
 ("« %s » décrit une position fixe",
  "« %s » описує нерухоме положення"),
 ("« %s » transitif décrit un déplacement",
  "« %s » перехідне описує переміщення"),
 ("« %s » indique ici un déplacement vers un endroit",
  "« %s » вказує тут на переміщення в певне місце"),
 ("« %s » indique un déplacement vers un endroit",
  "« %s » вказує на переміщення в певне місце"),
 ("« %s » décrit un déplacement vers un endroit",
  "« %s » описує переміщення в певне місце"),
 ("« %s » indique un déplacement vers le jardin",
  "« %s » вказує на переміщення до саду"),
 ("« %s » décrit un déplacement",
  "« %s » описує переміщення"),
]
# Les trois prefixes qui ne citent aucun verbe : ils ne servent qu'une fois.
UNIQUES = {
 "Aucun mouvement : le chat est déjà sur le canapé":
     "Жодного руху: кішка вже на дивані",
 "Les enfants jouent sur place, sans changer d'endroit":
     "Діти граються на місці, не змінюючи місця",
 "Aucun déplacement décrit": "Жодного переміщення не описано",
}

# ------------------------------------------------------------------ les indices
# Le membre de droite est presque toujours un verbe ALLEMAND, garde tel quel.
# Deux exceptions portent un mot francais.
DROITE = {"position": "положення", "hängen transitif": "hängen перехідне"}
GAUCHE = {
 "action de déplacer un objet": "дія переміщення предмета",
 "déplacement en voiture": "переміщення автомобілем",
 "déplacement vers le jardin": "переміщення до саду",
 "déplacement": "переміщення",
 "elle change de place": "вона змінює місце",
 "elle déplace la chaise": "вона переставляє стілець",
 "elle déplace la clé": "вона перевішує ключ",
 "elle déplace la tasse": "вона переставляє чашку",
 "elle déplace le tableau": "вона перевішує картину",
 "elle déplace les chaussures": "вона переставляє взуття",
 "elle dépose la serviette": "вона кладе рушник",
 "elle installe l'enfant": "вона садовить дитину",
 "elle ne bouge pas": "вона не рухається",
 "elle range les vêtements": "вона складає одяг",
 "il déplace l'affiche": "він перевішує плакат",
 "il déplace la chaise": "він переставляє стілець",
 "il déplace la lampe": "він перевішує лампу",
 "il déplace la voiture": "він переставляє машину",
 "il déplace le vélo": "він переставляє велосипед",
 "il dépose le ballon": "він кладе м'яч",
 "il dépose le livre": "він кладе книжку",
 "il dépose les livres": "він кладе книжки",
 "il installe l'enfant": "він садовить дитину",
 "il ne bouge pas": "він не рухається",
 "ils jouent sur place": "вони граються на місці",
 "ils sont déjà dans le jardin": "вони вже в саду",
 "je déplace la veste": "я перевішую куртку",
 "l'affiche ne bouge pas": "плакат не рухається",
 "l'enfant ne bouge pas": "дитина не рухається",
 "la chaise ne bouge pas": "стілець не рухається",
 "la clé ne bouge pas": "ключ не рухається",
 "la lampe ne bouge pas": "лампа не рухається",
 "la tasse ne bouge pas": "чашка не рухається",
 "la veste ne bouge pas": "куртка не рухається",
 "la voiture ne bouge pas": "машина не рухається",
 "le chat ne bouge pas": "кішка не рухається",
 "le chien ne bouge pas": "собака не рухається",
 "le livre ne bouge pas": "книжка не рухається",
 "le tableau ne bouge pas": "картина не рухається",
 "le vin ne bouge pas": "вино не рухається",
 "le vélo ne bouge pas": "велосипед не рухається",
 "les chaussures ne bougent pas": "взуття не рухається",
 "les livres ne bougent pas": "книжки не рухаються",
 "les vêtements ne bougent pas": "одяг не рухається",
 "nous ne bougeons pas": "ми не рухаємося",
 "« laufen » décrit ici un déplacement vers cet endroit":
     "« laufen » описує тут переміщення в це місце",
}

# ------------------------------------------------------------- les 50 phrases
T = {
"Die Katze schläft auf ___ Sofa. (das Sofa)": "Кішка спить на дивані.",
"Ich stelle die Vase auf ___ Tisch. (der Tisch)": "Я ставлю вазу на стіл.",
"Die Kinder spielen in ___ Garten. (der Garten)": "Діти граються в саду.",
"Wir gehen in ___ Garten. (der Garten)": "Ми йдемо в сад.",
"Der Wein steht auf ___ Tisch. (der Tisch)": "Вино стоїть на столі.",
"Er stellt den Stuhl neben ___ Schrank. (der Schrank)": "Він ставить стілець біля шафи.",
"Der Schlüssel liegt auf ___ Kommode. (die Kommode)": "Ключ лежить на комоді.",
"Sie legt das Handtuch auf ___ Bett. (das Bett)": "Вона кладе рушник на ліжко.",
"Die Katze sitzt auf ___ Fensterbank. (die Fensterbank)": "Кішка сидить на підвіконні.",
"Er setzt das Kind auf ___ Stuhl. (der Stuhl)": "Він садовить дитину на стілець.",
"Die Jacke hängt an ___ Haken. (der Haken)": "Куртка висить на гачку.",
"Ich hänge die Jacke an ___ Haken. (der Haken)": "Я вішаю куртку на гачок.",
"Die Lampe hängt über ___ Tisch. (der Tisch)": "Лампа висить над столом.",
"Er hängt die Lampe über ___ Tisch. (der Tisch)": "Він вішає лампу над столом.",
"Das Bild hängt über ___ Sofa. (das Sofa)": "Картина висить над диваном.",
"Sie hängt das Bild über ___ Sofa. (das Sofa)": "Вона вішає картину над диваном.",
"Der Hund liegt unter ___ Tisch. (der Tisch)": "Собака лежить під столом.",
"Er legt den Ball unter ___ Tisch. (der Tisch)": "Він кладе м'яч під стіл.",
"Die Schuhe stehen unter ___ Bett. (das Bett)": "Взуття стоїть під ліжком.",
"Sie stellt die Schuhe unter ___ Bett. (das Bett)": "Вона ставить взуття під ліжко.",
"Das Auto steht vor ___ Haus. (das Haus)": "Машина стоїть перед будинком.",
"Er stellt das Auto vor ___ Haus. (das Haus)": "Він ставить машину перед будинком.",
"Die Kinder spielen vor ___ Schule. (die Schule)": "Діти граються перед школою.",
"Die Kinder laufen vor ___ Schule. (die Schule)": "Діти біжать перед школу.",
"Das Buch liegt zwischen ___ Zeitschriften. (die Zeitschriften)":
    "Книжка лежить між журналами.",
"Er legt das Buch zwischen ___ Zeitschriften. (die Zeitschriften)":
    "Він кладе книжку між журнали.",
"Der Stuhl steht zwischen ___ Tisch und ___ Schrank. (der Tisch, der Schrank)":
    "Стілець стоїть між столом і шафою.",
"Sie stellt den Stuhl zwischen ___ Tisch und ___ Schrank. (der Tisch, der Schrank)":
    "Вона ставить стілець між стіл і шафу.",
"Das Poster hängt an ___ Wand. (die Wand)": "Плакат висить на стіні.",
"Er hängt das Poster an ___ Wand. (die Wand)": "Він вішає плакат на стіну.",
"Er steht an ___ Ampel. (die Ampel)": "Він стоїть біля світлофора.",
"Er fährt an ___ Ampel. (die Ampel)": "Він їде до світлофора.",
"Die Tasse steht auf ___ Regal. (das Regal)": "Чашка стоїть на полиці.",
"Sie stellt die Tasse auf ___ Regal. (das Regal)": "Вона ставить чашку на полицю.",
"Das Kind sitzt auf ___ Boden. (der Boden)": "Дитина сидить на підлозі.",
"Die Mutter setzt das Kind auf ___ Boden. (der Boden)": "Мати садовить дитину на підлогу.",
"Die Kleider liegen in ___ Schrank. (der Schrank)": "Одяг лежить у шафі.",
"Sie legt die Kleider in ___ Schrank. (der Schrank)": "Вона кладе одяг у шафу.",
"Er sitzt in ___ Auto. (das Auto)": "Він сидить у машині.",
"Er steigt in ___ Auto. (das Auto)": "Він сідає в машину.",
"Das Fahrrad steht neben ___ Tür. (die Tür)": "Велосипед стоїть біля дверей.",
"Er stellt das Fahrrad neben ___ Tür. (die Tür)": "Він ставить велосипед біля дверей.",
"Sie sitzt neben ___ Freund. (ihr Freund)": "Вона сидить біля свого друга.",
"Sie setzt sich neben ___ Freund. (ihr Freund)": "Вона сідає біля свого друга.",
"Wir sind in ___ Kino. (das Kino)": "Ми в кіно.",
"Wir gehen in ___ Kino. (das Kino)": "Ми йдемо в кіно.",
"Die Bücher sind auf ___ Tisch. (der Tisch)": "Книжки на столі.",
"Er legt die Bücher auf ___ Tisch. (der Tisch)": "Він кладе книжки на стіл.",
"Der Schlüssel hängt an ___ Nagel. (der Nagel)": "Ключ висить на цвяху.",
"Sie hängt den Schlüssel an ___ Nagel. (der Nagel)": "Вона вішає ключ на цвях.",
}

QUEUE = re.compile(r"^(.*?) → (Wo|Wohin) \? → (Dativ|Akkusativ) : (.+)\.$")


def traduire_prefixe(p):
    if p in UNIQUES:
        return UNIQUES[p]
    m = re.match(r"^« (.+?) » (.+)$", p)
    if not m:
        return None
    verbe = m.group(1)
    for fr, uk in PREFIXES:
        if p == fr % verbe:
            return uk % verbe
    return None


def traduire_indice(h):
    if not (h.startswith("(") and h.endswith(")")):
        return None
    dedans = h[1:-1]
    if " — " in dedans:
        g, dr = dedans.split(" — ", 1)
        if g not in GAUCHE:
            return None
        return "(%s — %s)" % (GAUCHE[g], DROITE.get(dr, dr))
    if dedans not in GAUCHE:
        return None
    return "(%s)" % GAUCHE[dedans]


def main():
    d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
    entrees, rates = [], []
    for e in d["jeux"]["praepWoWohinExercises"]:
        q, h, x = e["question"], e.get("hint", ""), e["explanation"]
        if q not in T:
            rates.append("TRAD : " + q)
            continue
        uk_h = traduire_indice(h)
        if not uk_h:
            rates.append("INDICE : " + h)
            continue
        m = QUEUE.match(x)
        if not m:
            rates.append("EXPL (queue) : " + x)
            continue
        pre = traduire_prefixe(m.group(1))
        if not pre:
            rates.append("EXPL (prefixe) : " + m.group(1))
            continue
        entrees.append({"question": q, "translation_uk": T[q], "hint_uk": uk_h,
                        "explanation_uk": "%s → %s? → %s: %s."
                        % (pre, m.group(2), m.group(3), m.group(4))})
    if rates:
        print("REFUS : %d" % len(rates))
        for r in rates[:12]:
            print("   " + r)
        sys.exit(1)
    io.open(os.path.join(R, "corrections_uk", "exos_praepWoWohin.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": "praepWoWohinExercises", "entrees": entrees},
                   ensure_ascii=False, indent=1) + "\n")
    print("exos_praepWoWohin.json : %d entrees" % len(entrees))


if __name__ == "__main__":
    main()
