# -*- coding: utf-8 -*-
"""exercises (50) : le present des verbes reguliers.

NEUF MOULES D'EXPLICATION, quatre d'indice. Tout ce qui varie -- le pronom, le
verbe, la terminaison, l'exemple final -- est ALLEMAND et reste tel quel.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MOULES = [
 (re.compile(r"^Avec (« .+? »), le verbe régulier (« .+? ») prend la terminaison (-\w+)$"),
  "З %s правильне дієслово %s бере закінчення %s"),
 (re.compile(r"^Avec (« .+? »), le verbe régulier reprend la forme infinitive$"),
  "З %s правильне дієслово повертається до форми інфінітива"),
 (re.compile(r"^Avec un sujet pluriel \((« .+? ») = sie\), le verbe reprend "
             r"la forme infinitive$"),
  "З підметом у множині (%s = sie) дієслово повертається до форми інфінітива"),
 (re.compile(r"^Le radical de (« .+? ») se termine déjà en (-\w+), donc "
             r"(« .+? ») prend simplement (-\w+)$"),
  "Основа %s вже закінчується на %s, тому %s бере просто %s"),
 (re.compile(r"^Le radical de (« .+? ») se termine en (-\w+), donc on ajoute "
             r"un -e avant (-\w+)$"),
  "Основа %s закінчується на %s, тому перед %s додається -e"),
 (re.compile(r"^Le radical de (« .+? ») se termine en (-\w+), donc (« .+? ») "
             r"prend seulement (-\w+) \(pas (-\w+)\)$"),
  "Основа %s закінчується на %s, тому %s бере лише %s (не %s)"),
 (re.compile(r"^Le radical de (« .+? ») se termine en (-\w+), donc (« .+? ») "
             r"prend simplement (-\w+)$"),
  "Основа %s закінчується на %s, тому %s бере просто %s"),
 (re.compile(r"^Pour les verbes en (-\w+), la forme (« .+? ») perd le -e final "
             r"de la terminaison$"),
  "У дієсловах на %s форма %s втрачає кінцеве -e закінчення"),
 (re.compile(r"^Pour les verbes en (-\w+), la forme (« .+? ») garde le -e et "
             r"devient (-\w+)$"),
  "У дієсловах на %s форма %s зберігає -e і стає %s"),
]

# Le membre de droite d'un indice, quand il y en a un. Le gauche est le verbe
# allemand et ne bouge pas.
DROITE = {
 "le radical se termine en -t": "основа закінчується на -t",
 "le radical se termine en -d": "основа закінчується на -d",
 "le radical se termine en -ß": "основа закінчується на -ß",
 "le radical se termine en -s": "основа закінчується на -s",
 "verbe en -eln": "дієслово на -eln",
 "verbe en -ern": "дієслово на -ern",
}

T = {
"Ich ___ jeden Tag Deutsch.": "Я щодня вчу німецьку.",
"Ich ___ Fußball.": "Я граю у футбол.",
"Du ___ gern Klavier.": "Ти любиш грати на піаніно.",
"Er ___ jeden Samstag Tennis.": "Він грає в теніс щосуботи.",
"Wir ___ zusammen Karten.": "Ми разом граємо в карти.",
"Ihr ___ im Park Fußball.": "Ви граєте у футбол у парку.",
"Die Kinder ___ im Garten.": "Діти граються в саду.",
"Ich ___ meine Hausaufgaben.": "Я роблю домашнє завдання.",
"Du ___ das sehr gut.": "Ти робиш це дуже добре.",
"Sie ___ das Abendessen.": "Вона готує вечерю.",
"Wir ___ eine Pause.": "Ми робимо перерву.",
"Ihr ___ zu viel Lärm.": "Ви робите забагато шуму.",
"Meine Eltern ___ eine Reise.": "Мої батьки вирушають у подорож.",
"Ich ___ frisches Brot.": "Я купую свіжий хліб.",
"Du ___ ein neues Auto.": "Ти купуєш нову машину.",
"Er ___ Blumen für seine Frau.": "Він купує квіти для своєї дружини.",
"Wir ___ Obst auf dem Markt.": "Ми купуємо фрукти на ринку.",
"Ihr ___ zu viele Süßigkeiten.": "Ви купуєте забагато солодощів.",
"Die Touristen ___ Souvenirs.": "Туристи купують сувеніри.",
"Ich ___ in Berlin.": "Я живу в Берліні.",
"Du ___ in einer kleinen Wohnung.": "Ти живеш у маленькій квартирі.",
"Sie ___ auf dem Land.": "Вона живе на селі.",
"Wir ___ seit zwei Jahren hier.": "Ми живемо тут уже два роки.",
"Ihr ___ ziemlich weit weg.": "Ви живете доволі далеко.",
"Meine Großeltern ___ am Meer.": "Мої бабуся й дідусь живуть біля моря.",
"Ich ___ in einem Büro.": "Я працюю в офісі.",
"Du ___ sehr fleißig.": "Ти працюєш дуже старанно.",
"Er ___ als Lehrer.": "Він працює вчителем.",
"Wir ___ heute lange.": "Ми сьогодні працюємо довго.",
"Ihr ___ zu viel.": "Ви працюєте забагато.",
"Meine Kollegen ___ im Homeoffice.": "Мої колеги працюють дистанційно.",
"Du ___ schon lange.": "Ти чекаєш уже давно.",
"Er ___ auf den Bus.": "Він чекає на автобус.",
"Wir ___ auf dich.": "Ми чекаємо на тебе.",
"Ihr ___ vor der Tür.": "Ви чекаєте перед дверима.",
"Du ___ die Aufgabe leicht.": "Ти вважаєш це завдання легким.",
"Sie ___ den Film langweilig.": "Вона вважає фільм нудним.",
"Wir ___ das eine gute Idee.": "Ми вважаємо це доброю ідеєю.",
"Ihr ___ den Weg bestimmt.": "Ви напевно знайдете дорогу.",
"Du ___ Anna, oder?": "Тебе звати Анна, чи не так?",
"Er ___ Thomas.": "Його звати Томас.",
"Wir ___ Müller.": "Наше прізвище Мюллер.",
"Du ___ oft nach Frankreich.": "Ти часто їздиш до Франції.",
"Sie ___ gern allein.": "Вона любить подорожувати сама.",
"Ich ___ Briefmarken.": "Я збираю марки.",
"Wir ___ Geld für einen guten Zweck.": "Ми збираємо гроші на добру справу.",
"Die Schüler ___ Ideen für das Projekt.": "Учні збирають ідеї для проєкту.",
"Ich ___ gern in den Bergen.": "Я люблю ходити в гори.",
"Wir ___ jedes Wochenende.": "Ми ходимо в походи щовихідних.",
"Meine Freunde ___ durch den Wald.": "Мої друзі мандрують лісом.",
}


def traduire_corps(c):
    for motif, gabarit in MOULES:
        m = motif.match(c)
        if m:
            return gabarit % m.groups()
    return None


def traduire_indice(h):
    if not (h.startswith("(") and h.endswith(")")):
        return None
    dedans = h[1:-1]
    if " — " not in dedans:
        return h            # juste l'infinitif allemand : rien a traduire
    g, dr = dedans.split(" — ", 1)
    if dr not in DROITE:
        return None
    return "(%s — %s)" % (g, DROITE[dr])


def main():
    d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
    entrees, rates = [], []
    for e in d["jeux"]["exercises"]:
        q, h, x = e["question"], e.get("hint", ""), e["explanation"]
        if q not in T:
            rates.append("TRAD : " + q)
            continue
        uk_h = traduire_indice(h) if h else None
        if h and not uk_h:
            rates.append("INDICE : " + h)
            continue
        i = x.rfind(" : ")
        corps, exemple = (x[:i], x[i + 3:]) if i > 0 else (None, None)
        uk_c = traduire_corps(corps) if corps else None
        if not uk_c:
            rates.append("EXPL : " + str(corps))
            continue
        entree = {"question": q, "cle_translation": e["translation"],
                  "translation_uk": T[q],
                  "explanation_uk": "%s: %s" % (uk_c, exemple)}
        if uk_h:
            entree["hint_uk"] = uk_h
        entrees.append(entree)
    if rates:
        print("REFUS : %d" % len(rates))
        for r in rates[:12]:
            print("   " + r)
        sys.exit(1)
    io.open(os.path.join(R, "corrections_uk", "exos_exercises.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": "exercises", "entrees": entrees},
                   ensure_ascii=False, indent=1) + "\n")
    print("exos_exercises.json : %d entrees" % len(entrees))


if __name__ == "__main__":
    main()
