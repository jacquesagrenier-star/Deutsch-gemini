# -*- coding: utf-8 -*-
"""partikelnNuanceExercises (50) : ce que la particule ajoute au ton.

LE JEU LE MOINS MOULABLE DES DIX. Les explications decrivent un TON, et un ton
ne se decline pas en gabarit : elles sont traduites une par une. Ce qui se
compose, ce sont les treize etiquettes de reponse (options), l'indice et le
suffixe de question.

⚠️ CE JEU DEMANDE AUSSI correctUk ET optionsUk. Les autres jeux repondent par
un mot allemand ; celui-ci repond par une ETIQUETTE EN LANGUE DE L'UTILISATEUR
-- « Insistance amicale », « Resignation »... Sans optionsUk, l'ukrainophone
choisirait entre treize etiquettes francaises. C'est le genre de trou qu'aucun
compteur d'entrees ne voit : le champ options existe, il est simplement dans
la mauvaise langue.

⚠️ ET « pas « mais » » DEVIENT « pas « але » ». La mise en garde de l'indice
cite le mot de la langue de l'utilisateur, pas le francais : elle sert a
ecarter la traduction courante de « aber », et cette traduction courante n'est
pas la meme en ukrainien.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

QSUF = re.compile(r"^(.+?) Quelle nuance apporte (« .+? ») ici \?$")

OPTIONS = {
 "Insistance amicale (encouragement)": "Дружнє наполягання (заохочення)",
 "Adoucit la demande (plus léger)": "Пом'якшує прохання (легший тон)",
 "Curiosité informelle": "Невимушена цікавість",
 "Résignation (« c'est comme ça »)": "Змирення (« так уже є »)",
 "Supposition probable": "Імовірне припущення",
 "Évidence partagée": "Спільна очевидність",
 "Rassurance": "Заспокоєння",
 "Surprise, emphase admirative": "Здивування, захоплений наголос",
 "Curiosité, changement de sujet": "Цікавість, зміна теми",
 "Urgence, mise en garde": "Терміновість, застереження",
 "Permission rassurante": "Заспокійливий дозвіл",
 "Simplicité, désinvolture": "Простота, невимушеність",
 "Exaspération, emphase forte": "Роздратування, сильний наголос",
}

HINTS = {
 "(ton du locuteur)": "(тон мовця)",
 "(ton du locuteur — pas une simple affirmation)": "(тон мовця — не просте твердження)",
 "(ton du locuteur — pas « mais »)": "(тон мовця — не « але »)",
 "(ton du locuteur — pas « peut-être »)": "(тон мовця — не « можливо »)",
}

# cle : la phrase allemande. valeur : (traduction, explication).
E = {
"Mach das doch!": ("Ну ж бо, зроби це!",
 "« doch » м'яко спонукає когось до дії — дружнє наполягання."),
"Komm mal her!": ("Ходи-но сюди.",
 "« mal » робить прохання легшим і невимушеним, менш прямим, ніж сухий наказ."),
"Was machst du denn?": ("Що ж ти робиш?",
 "« denn » у питанні виражає дружній і невимушений інтерес, а не нейтральне запитання."),
"Das ist eben so.": ("Так уже є, та й годі.",
 "« eben » (або « halt ») виражає, що ситуацію приймають, не маючи змоги її змінити."),
"Das wird wohl stimmen.": ("Це, мабуть, правда.",
 "« wohl » показує, що мовець вважає це правдою, але без цілковитої певності."),
"Das schaffst du schon!": ("Не хвилюйся, ти впораєшся.",
 "« schon » тут заспокоює й підбадьорює впевнено — це не просте часове твердження."),
"Das ist aber schön!": ("Ото ж бо, як гарно!",
 "« aber » тут виражає захоплене здивування, а не протиставлення (« але »)."),
"Was machst du eigentlich?": ("До речі, що ти робиш?",
 "« eigentlich » вводить питання ніби мимохідь, часто щоб змінити тему."),
"Geh bloß nicht dahin!": ("Тільки не ходи туди!",
 "« bloß » (або « nur ») підсилює застереження, надаючи йому терміновості."),
"Du kannst ruhig fragen.": ("Ти можеш спокійно запитати.",
 "« ruhig » тут запевняє, що дія цілком прийнятна."),
"Sag es einfach!": ("Просто скажи це.",
 "« einfach » применшує складність дії, цілком невимушено."),
"Das ist vielleicht ein Chaos!": ("Ото ж бо безлад!",
 "Тут « vielleicht » виражає не можливість, а роздратований наголос — на кшталт « ото ж бо! »."),
"Sei doch nicht so ernst!": ("Ну ж бо, не будь таким серйозним!",
 "« doch » м'яко заохочує змінити ставлення — дружнє наполягання."),
"Frag doch mal nach!": ("То запитай-но!",
 "« doch » м'яко спонукає до дії — дружнє наполягання."),
"Komm doch mit uns!": ("Ходімо ж із нами!",
 "« doch » тепло заохочує співрозмовника приєднатися — дружнє наполягання."),
"Zeig mir mal deine Fotos.": ("Покажи-но мені свої світлини.",
 "« mal » робить прохання легшим і невимушенішим."),
"Warte mal kurz.": ("Зачекай-но трохи.",
 "« mal » пом'якшує прохання, роблячи його менш прямим."),
"Erzähl mal, wie war's?": ("Розкажи-но, як воно було?",
 "« mal » надає проханню легкого і дружнього тону."),
"Wo warst du denn?": ("Де ж ти був?",
 "« denn » виражає тут дружній і невимушений інтерес."),
"Wer ist das denn?": ("Хто ж це?",
 "« denn » пом'якшує питання і виражає невимушену цікавість."),
"Wie geht's dir denn?": ("Як же ти маєшся?",
 "« denn » надає питанню дружнього і невимушеного тону."),
"So ist das Leben eben.": ("Таке життя, так уже є.",
 "« eben » виражає прийняття незмінної ситуації."),
"Das kostet halt viel Geld.": ("Це дорого, так уже є.",
 "« halt » (варіант « eben ») виражає змирення перед фактом."),
"Er ist eben so.": ("Він такий, та й годі.",
 "« eben » виражає змирене прийняття риси характеру."),
"Er ist wohl krank.": ("Він, мабуть, хворий.",
 "« wohl » вказує на ймовірне припущення, без певності."),
"Das war wohl ein Fehler.": ("Це, мабуть, була помилка.",
 "« wohl » виражає ймовірне припущення мовця."),
"Sie kommt wohl später.": ("Вона, мабуть, прийде пізніше.",
 "« wohl » позначає радше ймовірне припущення, ніж певність."),
"Das weißt du ja.": ("Ти ж це знаєш.",
 "« ja » підкреслює, що цей факт уже відомий обом співрозмовникам."),
"Es ist ja Wochenende.": ("Це ж вихідні, ти знаєш.",
 "« ja » нагадує про очевидність, спільну для обох співрозмовників."),
"Du kennst ihn ja schon.": ("Ти ж його вже знаєш.",
 "« ja » сигналізує, що цей факт має бути відомий співрозмовникові."),
"Das ist ja klar.": ("Це ж очевидно.",
 "« ja » підкреслює очевидність, яку обидва співрозмовники вже поділяють."),
"Es wird schon gut gehen.": ("Усе буде добре, не хвилюйся.",
 "« schon » тут упевнено заспокоює, без жодного зв'язку з часом."),
"Mach dir keine Sorgen, das klappt schon.": ("Не хвилюйся, усе вийде.",
 "« schon » заспокоює й упевнено підбадьорює."),
"Du findest den Weg schon.": ("Ти ж знайдеш дорогу.",
 "« schon » тут виражає впевнене заспокоєння."),
"Du bist aber groß geworden!": ("Ото ж бо, як ти виріс!",
 "« aber » тут виражає захоплене здивування, а не протиставлення."),
"Das ist aber teuer!": ("Ото ж бо, як дорого!",
 "« aber » позначає тут здивування, без ідеї протиставлення."),
"Sie kann aber gut singen!": ("Ото ж бо, як гарно вона співає!",
 "« aber » виражає тут захоплений наголос перед талантом."),
"Wie spät ist es eigentlich?": ("До речі, котра година?",
 "« eigentlich » вводить питання ніби мимохідь."),
"Wo wohnst du eigentlich?": ("До речі, де ти живеш?",
 "« eigentlich » виражає цікавість, що злегка змінює тему."),
"Was studierst du eigentlich?": ("До речі, що ти вивчаєш?",
 "« eigentlich » вводить питання, поставлене ніби мимохідь."),
"Sag das bloß nicht!": ("Тільки не кажи цього!",
 "« bloß » підсилює застереження, надаючи йому терміновості."),
"Mach das nur nicht!": ("Тільки не роби цього!",
 "« nur » (варіант « bloß ») підсилює застереження, надаючи йому терміновості."),
"Fass das bloß nicht an!": ("Тільки не чіпай цього!",
 "« bloß » позначає терміновість застереження."),
"Du darfst ruhig Platz nehmen.": ("Ти можеш спокійно сісти.",
 "« ruhig » запевняє, що запропонована дія цілком прийнятна."),
"Iss ruhig noch etwas.": ("Візьми спокійно ще трохи.",
 "« ruhig » дає співрозмовникові заспокійливий дозвіл."),
"Frag ruhig, wenn du etwas nicht verstehst.": ("Питай спокійно, якщо чогось не розумієш.",
 "« ruhig » запевняє, що ставити питання — доречно."),
"Komm einfach vorbei.": ("Просто заходь.",
 "« einfach » применшує складність дії, цілком невимушено."),
"Ruf mich einfach an.": ("Просто зателефонуй мені.",
 "« einfach » робить запропоновану дію невимушеною і без ускладнень."),
"Mach es einfach so, wie du willst.": ("Просто зроби так, як хочеш.",
 "« einfach » виражає невимушеність, без зайвих ускладнень."),
"Du bist vielleicht ein Glückspilz!": ("Ото ж бо, який ти щасливчик!",
 "Тут « vielleicht » виражає не можливість, а сильний наголос — захоплений або "
 "роздратований, залежно від тону."),
}


def main():
    d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
    entrees, rates = [], []
    for e in d["jeux"]["partikelnNuanceExercises"]:
        q, h = e["question"], e.get("hint", "")
        mq = QSUF.match(q)
        if not mq:
            rates.append("QUESTION : " + q)
            continue
        phrase, particule = mq.groups()
        if phrase not in E:
            rates.append("PHRASE : " + phrase)
            continue
        if h not in HINTS:
            rates.append("INDICE : " + h)
            continue
        opts = e.get("options") or []
        if any(o not in OPTIONS for o in opts) or e["correct"] not in OPTIONS:
            rates.append("OPTIONS : " + q)
            continue
        trad, expl = E[phrase]
        # L'explication doit citer la particule de SA question. Une ligne
        # recopiee d'une autre entree passerait tous les controles.
        if particule not in expl and not expl.startswith("Тут"):
            rates.append("PARTICULE ABSENTE DE L'EXPLICATION : " + q)
            continue
        entrees.append({"question": q,
                        "question_uk": "%s Який відтінок додає %s тут?"
                                       % (phrase, particule),
                        "translation_uk": trad, "hint_uk": HINTS[h],
                        "explanation_uk": expl,
                        "correctUk": OPTIONS[e["correct"]],
                        "optionsUk": [OPTIONS[o] for o in opts]})
    if rates:
        print("REFUS : %d" % len(rates))
        for r in rates[:12]:
            print("   " + r)
        sys.exit(1)
    io.open(os.path.join(R, "corrections_uk", "exos_partikelnNuance.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": "partikelnNuanceExercises", "entrees": entrees},
                   ensure_ascii=False, indent=1) + "\n")
    print("exos_partikelnNuance.json : %d entrees" % len(entrees))


if __name__ == "__main__":
    main()
