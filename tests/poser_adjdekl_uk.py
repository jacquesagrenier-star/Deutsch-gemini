# -*- coding: utf-8 -*-
"""adjektiveDeklinationExercises (50) : les terminaisons de l'adjectif.

TROIS PIECES, TROIS TRAITEMENTS
  - la parenthese de la question et l'indice sont des LISTES DE MOTS-CLES
    (« article défini, Nominativ, masculin ») : on traduit les mots-cles une
    fois et on recompose. Trente et un indices et quarante-sept parentheses
    tiennent dans une vingtaine de mots.
  - l'explication suit un moule par case du tableau -- trente-huit -- et
    chacune finit par un exemple ALLEMAND qui ne se traduit pas.
  - les cinquante phrases se traduisent une par une.

⚠️ DES TRADUCTIONS IDENTIQUES, ET C'EST NORMAL. « Der alte Baum steht im
Garten » et « Ein alter Baum steht im Garten » donnent la MEME phrase
ukrainienne : l'ukrainien n'a pas d'articles. Ce n'est pas un doublon a
corriger -- c'est ce que la langue fait, et l'exercice porte sur l'allemand de
la question, qui, lui, distingue. La cle est donc la question allemande.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Les mots-cles, pour la parenthese de la question ET pour l'indice.
MOTS = {
 "article défini": "означений артикль",
 "article indéfini": "неозначений артикль",
 "article négatif": "заперечний артикль",
 "article possessif": "присвійний займенник",
 "sans article": "без артикля",
 "après un article défini": "після означеного артикля",
 "après un article indéfini": "після неозначеного артикля",
 "après « kein »": "після « kein »",
 "après « meine »": "після « meine »",
 "après « meinen »": "після « meinen »",
 "après « meiner »": "після « meiner »",
 "comme un article indéfini": "як після неозначеного артикля",
 "comme un article indéfini au pluriel": "як після неозначеного артикля в множині",
 "masculin": "чоловічий рід",
 "féminin": "жіночий рід",
 "neutre": "середній рід",
 "pluriel": "множина",
 "Nominativ": "Nominativ",
 "Akkusativ": "Akkusativ",
 "Dativ": "Dativ",
 "Genitiv": "Genitiv",
 "Nominativ/Akkusativ": "Nominativ/Akkusativ",
 "Dativ pluriel": "Dativ множини",
 "Genitiv pluriel": "Genitiv множини",
}

CORPS = {
"Après un article défini au Nominativ masculin, l'adjectif prend -e":
 "Після означеного артикля в Nominativ чоловічого роду прикметник бере -e",
"Après un article défini au masculin Nominativ, l'adjectif prend -e":
 "Після означеного артикля в Nominativ чоловічого роду прикметник бере -e",
"Après un article défini au féminin Nominativ, l'adjectif prend -e":
 "Після означеного артикля в Nominativ жіночого роду прикметник бере -e",
"Après un article défini au féminin Akkusativ, l'adjectif prend -e":
 "Після означеного артикля в Akkusativ жіночого роду прикметник бере -e",
"Après un article défini au neutre Nominativ, l'adjectif prend -e":
 "Після означеного артикля в Nominativ середнього роду прикметник бере -e",
"Après un article défini au neutre Akkusativ, l'adjectif prend -e":
 "Після означеного артикля в Akkusativ середнього роду прикметник бере -e",
"Après un article défini au pluriel, l'adjectif prend toujours -en":
 "Після означеного артикля в множині прикметник завжди бере -en",
"Après un article défini, le Dativ prend toujours -en":
 "Після означеного артикля Dativ завжди бере -en",
"Après un article défini, le Genitiv prend toujours -en":
 "Після означеного артикля Genitiv завжди бере -en",
"Après un article défini, toutes les terminaisons masculines à l'Akkusativ sont -en":
 "Після означеного артикля всі чоловічі закінчення в Akkusativ — -en",
"Après un article indéfini au Nominativ masculin, l'adjectif porte lui-même la marque -er":
 "Після неозначеного артикля в Nominativ чоловічого роду прикметник сам несе позначку -er",
"Après un article indéfini au masculin Nominativ, l'adjectif porte -er":
 "Після неозначеного артикля в Nominativ чоловічого роду прикметник несе -er",
"Après un article indéfini au masculin Akkusativ, l'adjectif prend -en":
 "Після неозначеного артикля в Akkusativ чоловічого роду прикметник бере -en",
"Après un article indéfini au féminin Nominativ, l'adjectif prend -e":
 "Після неозначеного артикля в Nominativ жіночого роду прикметник бере -e",
"Après un article indéfini au féminin Akkusativ, l'adjectif prend -e":
 "Після неозначеного артикля в Akkusativ жіночого роду прикметник бере -e",
"Après un article indéfini au neutre (Nom./Akk.), l'adjectif prend -es":
 "Після неозначеного артикля в середньому роді (Nom./Akk.) прикметник бере -es",
"Après un article indéfini, le Dativ prend toujours -en":
 "Після неозначеного артикля Dativ завжди бере -en",
"Après un article indéfini, le Genitiv prend toujours -en":
 "Після неозначеного артикля Genitiv завжди бере -en",
"Après un article possessif au pluriel (déclinaison mixte), l'adjectif prend -en":
 "Після присвійного займенника в множині (мішана відміна) прикметник бере -en",
"Après un article possessif au pluriel, l'adjectif prend -en":
 "Після присвійного займенника в множині прикметник бере -en",
"Au Dativ pluriel, l'adjectif prend toujours -en":
 "У Dativ множини прикметник завжди бере -en",
"Au Genitiv pluriel, l'adjectif prend toujours -en":
 "У Genitiv множини прикметник завжди бере -en",
"Sans article au Dativ (masc./neutre), l'adjectif prend -em":
 "Без артикля в Dativ (чол./сер.) прикметник бере -em",
"Sans article au masculin Nominativ, l'adjectif prend -er":
 "Без артикля в Nominativ чоловічого роду прикметник бере -er",
"Sans article au masculin Akkusativ, l'adjectif prend -en":
 "Без артикля в Akkusativ чоловічого роду прикметник бере -en",
"Sans article au masculin Genitiv, l'adjectif prend -en":
 "Без артикля в Genitiv чоловічого роду прикметник бере -en",
"Sans article au féminin Nominativ, l'adjectif prend -e":
 "Без артикля в Nominativ жіночого роду прикметник бере -e",
"Sans article au féminin Akkusativ, l'adjectif prend -e":
 "Без артикля в Akkusativ жіночого роду прикметник бере -e",
"Sans article au féminin Dativ, l'adjectif prend -er":
 "Без артикля в Dativ жіночого роду прикметник бере -er",
"Sans article au féminin Genitiv, l'adjectif prend -er":
 "Без артикля в Genitiv жіночого роду прикметник бере -er",
"Sans article au neutre Nominativ, l'adjectif prend -es":
 "Без артикля в Nominativ середнього роду прикметник бере -es",
"Sans article au neutre Akkusativ, l'adjectif prend -es":
 "Без артикля в Akkusativ середнього роду прикметник бере -es",
"Sans article au neutre Genitiv, l'adjectif prend -en":
 "Без артикля в Genitiv середнього роду прикметник бере -en",
"Sans article au pluriel Nominativ, l'adjectif prend -e":
 "Без артикля в Nominativ множини прикметник бере -e",
"Sans article au pluriel Akkusativ, l'adjectif prend -e":
 "Без артикля в Akkusativ множини прикметник бере -e",
"Sans article au pluriel Dativ, l'adjectif prend -en":
 "Без артикля в Dativ множини прикметник бере -en",
"Sans article au pluriel Genitiv, l'adjectif prend -er":
 "Без артикля в Genitiv множини прикметник бере -er",
"« kein » se décline comme « ein » : au neutre Akkusativ, l'adjectif prend -es":
 "« kein » відмінюється як « ein »: в Akkusativ середнього роду прикметник бере -es",
}

T = {
"Der klein___ Hund schläft.": "Маленький пес спить.",
"Ich sehe den klein___ Hund.": "Я бачу маленького пса.",
"Ein groß___ Mann steht da.": "Там стоїть високий чоловік.",
"Ich habe ein neu___ Auto.": "У мене нова машина.",
"Kalt___ Wasser ist gesund.": "Холодна вода корисна.",
"Mit heiß___ Tee wird es besser.": "З гарячим чаєм стане краще.",
"Die klein___ Frau lächelt.": "Маленька жінка усміхається.",
"Ich sehe die klein___ Frau.": "Я бачу маленьку жінку.",
"Ich helfe der klein___ Frau.": "Я допомагаю маленькій жінці.",
"Das ist die Tasche der klein___ Frau.": "Це сумка маленької жінки.",
"Das klein___ Kind schläft.": "Маленька дитина спить.",
"Ich sehe das klein___ Kind.": "Я бачу маленьку дитину.",
"Ich helfe dem klein___ Kind.": "Я допомагаю маленькій дитині.",
"Das ist das Spielzeug des klein___ Kindes.": "Це іграшка маленької дитини.",
"Ich helfe dem klein___ Hund.": "Я допомагаю маленькому псові.",
"Das ist der Schwanz des klein___ Hundes.": "Це хвіст маленького пса.",
"Die klein___ Hunde schlafen.": "Маленькі пси сплять.",
"Ich sehe die klein___ Hunde.": "Я бачу маленьких псів.",
"Ich helfe den klein___ Hunden.": "Я допомагаю маленьким псам.",
"Das sind die Namen der klein___ Hunde.": "Це імена маленьких псів.",
"Der alt___ Baum steht im Garten.": "Старе дерево стоїть у саду.",
"Ich sehe einen groß___ Mann.": "Я бачу високого чоловіка.",
"Ich helfe einem groß___ Mann.": "Я допомагаю високому чоловікові.",
"Das ist der Hut eines groß___ Mannes.": "Це капелюх високого чоловіка.",
"Ein alt___ Baum steht im Garten.": "Старе дерево стоїть у саду.",
"Eine klein___ Frau steht da.": "Там стоїть маленька жінка.",
"Ich sehe eine klein___ Frau.": "Я бачу маленьку жінку.",
"Ich helfe einer klein___ Frau.": "Я допомагаю маленькій жінці.",
"Das ist die Tasche einer klein___ Frau.": "Це сумка маленької жінки.",
"Ich helfe einem klein___ Kind.": "Я допомагаю маленькій дитині.",
"Das ist das Spielzeug eines klein___ Kindes.": "Це іграшка маленької дитини.",
"Meine klein___ Kinder spielen.": "Мої маленькі діти граються.",
"Ich sehe meine klein___ Kinder.": "Я бачу своїх маленьких дітей.",
"Ich helfe meinen klein___ Kindern.": "Я допомагаю своїм маленьким дітям.",
"Das sind die Namen meiner klein___ Kinder.": "Це імена моїх маленьких дітей.",
"Ich habe kein neu___ Auto.": "У мене немає нової машини.",
"Kalt___ Kaffee ist nicht lecker.": "Холодна кава несмачна.",
"Ich trinke kalt___ Kaffee.": "Я п'ю холодну каву.",
"Das ist der Geschmack kalt___ Kaffees.": "Це смак холодної кави.",
"Frisch___ Milch ist im Kühlschrank.": "Свіже молоко в холодильнику.",
"Ich trinke frisch___ Milch.": "Я п'ю свіже молоко.",
"Der Kuchen schmeckt mit frisch___ Milch besser.": "Пиріг смачніший зі свіжим молоком.",
"Das ist der Geschmack frisch___ Milch.": "Це смак свіжого молока.",
"Ich trinke kalt___ Wasser.": "Я п'ю холодну воду.",
"Das ist der Geschmack kalt___ Wassers.": "Це смак холодної води.",
"Klein___ Kinder lachen viel.": "Маленькі діти багато сміються.",
"Ich sehe klein___ Kinder.": "Я бачу маленьких дітей.",
"Er spielt gern mit klein___ Kindern.": "Він любить гратися з маленькими дітьми.",
"Das sind die Stimmen klein___ Kinder.": "Це голоси маленьких дітей.",
"Nach lang___ Zeit sehen wir uns wieder.": "Після довгого часу ми знову бачимося.",
}

QUESTION = re.compile(r"^(.+?) \(([^()]+)\)$")


def liste_mots(texte):
    """« article défini, Nominativ, masculin » -> la meme liste en ukrainien."""
    bouts = []
    for mot in texte.split(", "):
        if mot not in MOTS:
            return None
        bouts.append(MOTS[mot])
    return ", ".join(bouts)


def main():
    d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
    entrees, rates = [], []
    for e in d["jeux"]["adjektiveDeklinationExercises"]:
        q, h, x = e["question"], e.get("hint", ""), e["explanation"]
        mq = QUESTION.match(q)
        if not mq:
            rates.append("QUESTION : " + q)
            continue
        phrase, dedans = mq.groups()
        if phrase not in T:
            rates.append("TRAD : " + phrase)
            continue
        mots = liste_mots(dedans)
        if not mots:
            rates.append("PARENTHESE : " + dedans)
            continue
        if not (h.startswith("(") and h.endswith(")")):
            rates.append("INDICE : " + h)
            continue
        uk_h = liste_mots(h[1:-1])
        if not uk_h:
            rates.append("INDICE : " + h)
            continue
        # L'explication finit toujours par un exemple allemand ; on coupe au
        # DERNIER « : », parce que le moule de « kein » en porte deja un.
        i = x.rfind(" : ")
        corps, exemple = (x[:i], x[i + 3:]) if i > 0 else (None, None)
        if corps not in CORPS:
            rates.append("EXPL : " + str(corps))
            continue
        entrees.append({"question": q,
                        "question_uk": "%s (%s)" % (phrase, mots),
                        "translation_uk": T[phrase],
                        "hint_uk": "(%s)" % uk_h,
                        "explanation_uk": "%s: %s" % (CORPS[corps], exemple)})
    if rates:
        print("REFUS : %d" % len(rates))
        for r in rates[:12]:
            print("   " + r)
        sys.exit(1)
    io.open(os.path.join(R, "corrections_uk", "exos_adjektiveDeklination.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": "adjektiveDeklinationExercises", "entrees": entrees},
                   ensure_ascii=False, indent=1) + "\n")
    print("exos_adjektiveDeklination.json : %d entrees" % len(entrees))


if __name__ == "__main__":
    main()
