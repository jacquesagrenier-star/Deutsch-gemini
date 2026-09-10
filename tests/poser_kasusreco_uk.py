# -*- coding: utf-8 -*-
"""kasusReconnaissanceExercises (50) : reconnaitre le cas d'un groupe.

CINQ MOULES POUR LES EXPLICATIONS, UN POUR L'INDICE, UN POUR LA QUESTION. Ce
qui varie dans les moules est presque toujours de l'ALLEMAND -- le groupe
nominal cite, le verbe -- et ne se traduit donc pas.

LA SEULE VRAIE TRADUCTION EST AILLEURS : les 50 phrases d'exemple, et les
douze gloses de possession du Genitiv.

⚠️ CE QUE LE FRANCAIS APPUIE, L'UKRAINIEN N'A PAS A APPUYER. La glose du
Genitiv met la preposition en capitales -- « la couleur DE la voiture » --
parce que c'est elle qui porte la possession en francais. L'ukrainien la porte
dans la TERMINAISON du nom : il n'y a pas de mot a mettre en capitales. On
appuie donc sur le nom au genitif -- « колір МАШИНИ » -- ce qui montre
exactement ce que la glose francaise montre, a l'endroit ou la langue le fait.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

QSUF_FR = re.compile(r"^(.*?) Quel cas est (« .+? ») \?$")
HINT_FR = "(essaie les quatre questions : qui ? — qui/quoi ? — à qui ? — de qui ?)"
HINT_UK = "(спробуй чотири питання: хто? — кого/що? — кому? — чий?)"

# Les douze gloses de possession, traduites une par une.
POSSESSION = {
 "la couleur DE la voiture": "колір МАШИНИ",
 "la voiture DE mon frère": "машина МОГО БРАТА",
 "la couleur DU ciel": "колір НЕБА",
 "le titre DU livre": "назва КНИЖКИ",
 "la porte DE la maison": "двері БУДИНКУ",
 "le nom DE la ville": "назва МІСТА",
 "le coin DE la pièce": "куток КІМНАТИ",
 "le goût DU gâteau": "смак ТОРТА",
 "la voix DE la chanteuse": "голос СПІВАЧКИ",
 "le prix DE la voiture": "ціна МАШИНИ",
 "les feuilles DES arbres": "листя ДЕРЕВ",
 "l'opinion DU patron": "думка ШЕФА",
}

# Les 50 phrases, traduites depuis l'allemand.
T = {
"Der Lehrer erklärt den Schülern die Aufgabe.": "Учитель пояснює учням завдання.",
"Ich sehe den Hund im Garten.": "Я бачу собаку в саду.",
"Die Farbe des Autos gefällt mir.": "Колір машини мені подобається.",
"Der Hund läuft schnell.": "Собака біжить швидко.",
"Die Sonne scheint hell.": "Сонце світить яскраво.",
"Meine Schwester kocht das Abendessen.": "Моя сестра готує вечерю.",
"Das Kind spielt im Garten.": "Дитина грається в саду.",
"Die Katze schläft auf dem Sofa.": "Кішка спить на дивані.",
"Der Zug kommt pünktlich an.": "Потяг прибуває вчасно.",
"Die Studenten lernen fleißig.": "Студенти вчаться старанно.",
"Mein Vater arbeitet im Büro.": "Мій батько працює в офісі.",
"Die Blumen blühen im Frühling.": "Квіти квітнуть навесні.",
"Der Arzt untersucht den Patienten.": "Лікар оглядає пацієнта.",
"Die Kinder singen ein Lied.": "Діти співають пісню.",
"Die Bäckerin backt frisches Brot.": "Пекарка випікає свіжий хліб.",
"Ich kaufe einen Apfel.": "Я купую яблуко.",
"Er liest das Buch.": "Він читає книжку.",
"Wir besuchen unsere Großeltern.": "Ми відвідуємо наших бабусю й дідуся.",
"Sie trinkt den Kaffee.": "Вона п'є каву.",
"Ich sehe den Vogel im Baum.": "Я бачу птаха на дереві.",
"Der Koch bereitet die Suppe vor.": "Кухар готує суп.",
"Wir putzen das Fenster.": "Ми миємо вікно.",
"Sie schreibt einen Brief.": "Вона пише листа.",
"Ich rufe meinen Freund an.": "Я телефоную своєму другові.",
"Er trägt die Kiste.": "Він несе ящик.",
"Sie kauft ein neues Kleid.": "Вона купує нову сукню.",
"Ich gebe dem Kind ein Geschenk.": "Я даю дитині подарунок.",
"Er hilft seiner Mutter.": "Він допомагає своїй матері.",
"Wir danken dem Lehrer.": "Ми дякуємо вчителеві.",
"Sie schreibt ihrer Freundin eine Nachricht.": "Вона пише своїй подрузі повідомлення.",
"Ich zeige dem Touristen den Weg.": "Я показую туристові дорогу.",
"Er schenkt seinem Bruder ein Buch.": "Він дарує своєму братові книжку.",
"Wir folgen dem Guide.": "Ми йдемо за гідом.",
"Das Kleid gefällt der Frau.": "Сукня подобається жінці.",
"Ich vertraue meinem Kollegen.": "Я довіряю своєму колезі.",
"Sie erklärt den Schülern die Regel.": "Вона пояснює учням правило.",
"Wir schicken den Gästen eine Einladung.": "Ми надсилаємо гостям запрошення.",
"Er antwortet dem Chef sofort.": "Він відповідає шефові одразу.",
"Das Auto meines Bruders ist neu.": "Машина мого брата нова.",
"Die Farbe des Himmels ist blau.": "Колір неба блакитний.",
"Der Titel des Buches ist interessant.": "Назва книжки цікава.",
"Die Tür des Hauses ist offen.": "Двері будинку відчинені.",
"Der Name der Stadt ist bekannt.": "Назва міста відома.",
"Die Ecke des Zimmers ist dunkel.": "Куток кімнати темний.",
"Der Geschmack des Kuchens ist süß.": "Смак торта солодкий.",
"Die Stimme der Sängerin ist schön.": "Голос співачки гарний.",
"Der Preis des Autos ist hoch.": "Ціна машини висока.",
"Die Blätter der Bäume fallen im Herbst.": "Листя дерев опадає восени.",
"Die Meinung des Chefs zählt.": "Думка шефа важлива.",
"Der Wind weht stark.": "Вітер віє сильно.",
}


def traduire_explication(x):
    m = re.match(r"^(« .+? ») est le sujet de la phrase — Nominativ\.$", x)
    if m:
        return "%s — підмет речення — Nominativ." % m.group(1)
    m = re.match(r"^(« .+? ») est l'objet direct de (« .+? ») — Akkusativ\.$", x)
    if m:
        return "%s — прямий додаток до %s — Akkusativ." % m.groups()
    m = re.match(r"^(« .+? ») répond à « à qui \? » — c'est l'objet indirect, "
                 r"donc le Dativ\.$", x)
    if m:
        return ("%s відповідає на питання « кому? » — це непрямий додаток, "
                "отже Dativ." % m.group(1))
    m = re.match(r"^(« .+? ») répond à « à qui \? » — Dativ\.$", x)
    if m:
        return "%s відповідає на питання « кому? » — Dativ." % m.group(1)
    m = re.match(r"^(« .+? ») demande toujours le Dativ — (« .+? ») est l'objet "
                 r"du verbe\.$", x)
    if m:
        return "%s завжди вимагає Dativ — %s є додатком дієслова." % m.groups()
    m = re.match(r"^(« .+? ») marque la possession \((.+?)\) — Genitiv\.$", x)
    if m and m.group(2) in POSSESSION:
        return ("%s позначає належність (%s) — Genitiv."
                % (m.group(1), POSSESSION[m.group(2)]))
    return None


def main():
    d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
    entrees, rates = [], []
    for e in d["jeux"]["kasusReconnaissanceExercises"]:
        q, h, x = e["question"], e.get("hint", ""), e["explanation"]
        mq = QSUF_FR.match(q)
        if not mq:
            rates.append("QUESTION : " + q)
            continue
        phrase, groupe = mq.groups()
        if phrase not in T:
            rates.append("TRAD : " + phrase)
            continue
        if h != HINT_FR:
            rates.append("INDICE : " + h)
            continue
        uk_x = traduire_explication(x)
        if not uk_x:
            rates.append("EXPL : " + x)
            continue
        entrees.append({"question": q,
                        "question_uk": "%s У якому відмінку %s?" % (phrase, groupe),
                        "translation_uk": T[phrase], "hint_uk": HINT_UK,
                        "explanation_uk": uk_x})
    if rates:
        print("REFUS : %d" % len(rates))
        for r in rates[:12]:
            print("   " + r)
        sys.exit(1)
    io.open(os.path.join(R, "corrections_uk", "exos_kasusReconnaissance.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": "kasusReconnaissanceExercises", "entrees": entrees},
                   ensure_ascii=False, indent=1) + "\n")
    print("exos_kasusReconnaissance.json : %d entrees" % len(entrees))


if __name__ == "__main__":
    main()
