# -*- coding: utf-8 -*-
"""relativGenitivReconnaissanceExercises (51) : dessen / deren.

QUATRE MOULES, UN PAR GENRE. Le reste est de l'allemand cite.

LA GLOSE CHANGE DE LANGUE, PAS SEULEMENT DE MOTS. Le francais met « dont »
dans les quatre indices : il n'a qu'une forme. Le turc y a mis sa construction
possessive, le persan « که ...ِ او ». L'ukrainien, lui, ACCORDE -- чий, чия,
чиє, чиї -- exactement comme l'allemand accorde dessen/deren. On donne donc la
forme du genre concerne : c'est la meme information que « dont », dite dans
une langue qui fait la distinction que l'exercice enseigne.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GENRES = {"masculin": ("чоловічий рід", "чоловічого роду", "чий"),
          "féminin": ("жіночий рід", "жіночого роду", "чия"),
          "neutre": ("середній рід", "середнього роду", "чиє"),
          "pluriel": ("множина", "множини", "чиї")}

T = {
"Der Mann, ___ Auto kaputt ist, wartet auf den Abschleppwagen.":
    "Чоловік, чия машина зламана, чекає на евакуатор.",
"Der Lehrer, ___ Buch ich gelesen habe, ist bekannt.":
    "Учитель, чию книжку я прочитав, відомий.",
"Der Nachbar, ___ Hund ständig bellt, stört uns.":
    "Сусід, чий пес постійно гавкає, заважає нам.",
"Der Sänger, ___ Stimme wunderschön ist, füllt jedes Konzert.":
    "Співак, чий голос чудовий, збирає повні зали.",
"Der Schauspieler, ___ Filme sehr beliebt sind, lebt in Los Angeles.":
    "Актор, чиї фільми дуже популярні, живе в Лос-Анджелесі.",
"Der Freund, ___ Schwester Ärztin ist, kommt heute zu Besuch.":
    "Друг, чия сестра лікарка, приходить сьогодні в гості.",
"Der Chef, ___ Meinung allen wichtig ist, ist selten hier.":
    "Шеф, чия думка важлива для всіх, буває тут рідко.",
"Der Politiker, ___ Rede sehr lang war, wurde stark kritisiert.":
    "Політик, чия промова була дуже довгою, зазнав сильної критики.",
"Der Student, ___ Projekt sehr originell ist, bekommt ein Stipendium.":
    "Студент, чий проєкт дуже оригінальний, отримує стипендію.",
"Der Künstler, ___ Bilder im Museum hängen, ist schon gestorben.":
    "Митець, чиї картини висять у музеї, уже помер.",
"Der Fahrer, ___ Auto zu schnell fuhr, bekam eine Strafe.":
    "Водій, чия машина їхала надто швидко, отримав штраф.",
"Der Onkel, ___ Garten riesig ist, wohnt auf dem Land.":
    "Дядько, чий сад величезний, живе на селі.",
"Die Frau, ___ Sohn Lehrer ist, wohnt hier.":
    "Жінка, чий син учитель, живе тут.",
"Die Ärztin, ___ Praxis hier ist, ist sehr nett.":
    "Лікарка, чий кабінет тут, дуже приємна.",
"Die Sängerin, ___ Lied ich mag, gibt bald ein Konzert.":
    "Співачка, чия пісня мені подобається, скоро дає концерт.",
"Die Kollegin, ___ Idee sehr gut war, wurde befördert.":
    "Колега, чия ідея була дуже вдалою, отримала підвищення.",
"Die Nachbarin, ___ Katze immer weg ist, sucht sie überall.":
    "Сусідка, чия кішка постійно тікає, шукає її всюди.",
"Die Schriftstellerin, ___ Bücher sehr erfolgreich sind, lebt in Paris.":
    "Письменниця, чиї книжки дуже успішні, живе в Парижі.",
"Die Firma, ___ Produkte sehr beliebt sind, wächst schnell.":
    "Фірма, чиї товари дуже популярні, швидко зростає.",
"Die Studentin, ___ Noten immer gut sind, bekommt ein Stipendium.":
    "Студентка, чиї оцінки завжди добрі, отримує стипендію.",
"Die Schwester, ___ Mann Arzt ist, wohnt in München.":
    "Сестра, чий чоловік лікар, живе в Мюнхені.",
"Die Direktorin, ___ Entscheidungen immer klug sind, wird sehr respektiert.":
    "Директорка, чиї рішення завжди мудрі, має велику повагу.",
"Das Kind, ___ Eltern Lehrer sind, lernt gern.":
    "Дитина, чиї батьки вчителі, любить учитися.",
"Das Haus, ___ Dach kaputt ist, wird repariert.":
    "Будинок, чий дах зламаний, будуть ремонтувати.",
"Das Mädchen, ___ Mutter Ärztin ist, will auch Ärztin werden.":
    "Дівчина, чия мати лікарка, теж хоче стати лікаркою.",
"Das Restaurant, ___ Küche exzellent ist, ist immer voll.":
    "Ресторан, чия кухня чудова, завжди повний.",
"Das Team, ___ Trainer sehr streng ist, gewinnt fast immer.":
    "Команда, чий тренер дуже суворий, майже завжди перемагає.",
"Das Unternehmen, ___ Chef sehr bekannt ist, wächst schnell.":
    "Підприємство, чий керівник дуже відомий, швидко зростає.",
"Das Auto, ___ Motor sehr laut ist, gehört meinem Bruder.":
    "Машина, чий двигун дуже гучний, належить моєму братові.",
"Das Buch, ___ Ende überraschend ist, wurde ein Bestseller.":
    "Книжка, чий кінець несподіваний, стала бестселером.",
"Das Dorf, ___ Kirche sehr alt ist, liegt in den Bergen.":
    "Село, чия церква дуже давня, лежить у горах.",
"Das Mädchen, ___ Zeichnungen sehr schön sind, will Künstlerin werden.":
    "Дівчина, чиї малюнки дуже гарні, хоче стати художницею.",
"Die Leute, ___ Auto alt ist, kaufen sich ein neues.":
    "Люди, чия машина стара, купують собі нову.",
"Die Studenten, ___ Noten gut sind, freuen sich.":
    "Студенти, чиї оцінки добрі, радіють.",
"Die Kinder, ___ Eltern streng sind, gehen früh ins Bett.":
    "Діти, чиї батьки суворі, лягають спати рано.",
"Die Nachbarn, ___ Garten sehr gepflegt ist, gewinnen jedes Jahr einen Preis.":
    "Сусіди, чий сад дуже доглянутий, щороку отримують нагороду.",
"Die Firmen, ___ Produkte umweltfreundlich sind, werden immer beliebter.":
    "Фірми, чиї товари екологічні, стають дедалі популярнішими.",
"Die Sportler, ___ Trainer sehr erfahren ist, gewinnen oft.":
    "Спортсмени, чий тренер дуже досвідчений, часто перемагають.",
"Die Musiker, ___ Konzert ausverkauft war, sind sehr glücklich.":
    "Музиканти, чий концерт був аншлаговим, дуже щасливі.",
"Die Schüler, ___ Lehrerin sehr geduldig ist, lernen gern.":
    "Учні, чия вчителька дуже терпляча, люблять учитися.",
"Die Eltern, ___ Kinder im Ausland leben, reisen oft.":
    "Батьки, чиї діти живуть за кордоном, часто подорожують.",
"Der Arzt, ___ Wartezimmer immer voll ist, ist sehr beliebt.":
    "Лікар, чия приймальня завжди повна, дуже популярний.",
"Die Bäckerei, ___ Brot sehr lecker ist, ist immer voll.":
    "Пекарня, чий хліб дуже смачний, завжди повна.",
"Der Bauer, ___ Felder riesig sind, arbeitet den ganzen Tag.":
    "Фермер, чиї поля величезні, працює цілий день.",
"Das Café, ___ Kaffee sehr gut ist, liegt gleich um die Ecke.":
    "Кафе, чия кава дуже добра, розташоване відразу за рогом.",
"Der Regisseur, ___ Filme sehr originell sind, gewinnt oft Preise.":
    "Режисер, чиї фільми дуже оригінальні, часто отримує нагороди.",
"Die Universität, ___ Programme sehr anspruchsvoll sind, ist weltbekannt.":
    "Університет, чиї програми дуже вимогливі, відомий у всьому світі.",
"Der Ingenieur, ___ Erfindung genial ist, wird oft interviewt.":
    "Інженер, чий винахід геніальний, часто дає інтерв'ю.",
"Das Krankenhaus, ___ Personal sehr freundlich ist, ist bei allen beliebt.":
    "Лікарня, чий персонал дуже привітний, подобається всім.",
"Die Wissenschaftler, ___ Forschung wichtig ist, bekommen viel Geld.":
    "Науковці, чиє дослідження важливе, отримують багато грошей.",
"Die Band, ___ Musik sehr modern ist, hat viele junge Fans.":
    "Гурт, чия музика дуже сучасна, має багато молодих фанів.",
}

HINT = re.compile(r"^\(Genitiv, (\w+) -- « dont »\)$")
EXPL = re.compile(r"^(« .+? ») est (\w+) -- Genitiv \w+ = (« .+? »)\.$")


def main():
    d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
    entrees, rates = [], []
    for e in d["jeux"]["relativGenitivReconnaissanceExercises"]:
        q, h, x = e["question"], e.get("hint", ""), e["explanation"]
        mh, mx = HINT.match(h), EXPL.match(x)
        if q not in T:
            rates.append("TRAD : " + q)
            continue
        if not mh or mh.group(1) not in GENRES:
            rates.append("INDICE : " + h)
            continue
        if not mx or mx.group(2) not in GENRES:
            rates.append("EXPL : " + x)
            continue
        # L'indice et l'explication doivent parler du MEME genre. Rien ne
        # l'attraperait a la relecture : les deux phrases sont justes seules.
        if mh.group(1) != mx.group(2):
            rates.append("GENRES DIFFERENTS : " + q)
            continue
        court, longg, glose = GENRES[mh.group(1)]
        entrees.append({"question": q, "translation_uk": T[q],
                        "hint_uk": "(Genitiv, %s — « %s »)" % (court, glose),
                        "explanation_uk": "%s — %s — Genitiv %s = %s."
                        % (mx.group(1), court, longg, mx.group(3))})
    if rates:
        print("REFUS : %d" % len(rates))
        for r in rates[:12]:
            print("   " + r)
        sys.exit(1)
    io.open(os.path.join(R, "corrections_uk", "exos_relativGenitiv.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": "relativGenitivReconnaissanceExercises",
                    "entrees": entrees}, ensure_ascii=False, indent=1) + "\n")
    print("exos_relativGenitiv.json : %d entrees" % len(entrees))


if __name__ == "__main__":
    main()
