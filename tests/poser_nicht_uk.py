# -*- coding: utf-8 -*-
"""wortstellungNichtExercises (50) : quatre moules et une variante par element."""
import io, json, os, re, sys

R = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"

H = {
 "(négation générale, en fin de phrase)": "(загальне заперечення, у кінці речення)",
 "(négation d'un élément précis)": "(заперечення певного елемента)",
 "(négation d'un élément précis, placée juste avant lui)":
   "(заперечення певного елемента, безпосередньо перед ним)",
}

T = {
"Je ne comprends pas ça.":"Я цього не розумію.",
"Tu ne comprends pas ça.":"Ти цього не розумієш.",
"Il ne comprend pas ça.":"Він цього не розуміє.",
"Elle ne comprend pas ça.":"Вона цього не розуміє.",
"Nous ne comprenons pas ça.":"Ми цього не розуміємо.",
"Vous ne comprenez pas ça.":"Ви цього не розумієте.",
"Ils ne comprennent pas ça.":"Вони цього не розуміють.",
"Je n'aime pas Berlin.":"Мені не подобається Берлін.",
"Tu n'aimes pas Berlin.":"Тобі не подобається Берлін.",
"Il n'aime pas Berlin.":"Йому не подобається Берлін.",
"Elle n'aime pas Berlin.":"Їй не подобається Берлін.",
"Nous n'aimons pas Berlin.":"Нам не подобається Берлін.",
"Vous n'aimez pas Berlin.":"Вам не подобається Берлін.",
"Ils n'aiment pas Berlin.":"Їм не подобається Берлін.",
"Je ne le connais pas.":"Я його не знаю.",
"Tu ne le connais pas.":"Ти його не знаєш.",
"Il ne le connaît pas.":"Він його не знає.",
"Elle ne le connaît pas.":"Вона його не знає.",
"Nous ne le connaissons pas.":"Ми його не знаємо.",
"Vous ne le connaissez pas.":"Ви його не знаєте.",
"Ils ne le connaissent pas.":"Вони його не знають.",
"Je n'ai pas besoin de ça.":"Мені це не потрібно.",
"Tu n'as pas besoin de ça.":"Тобі це не потрібно.",
"Il n'a pas besoin de ça.":"Йому це не потрібно.",
"Elle n'a pas besoin de ça.":"Їй це не потрібно.",
"Nous n'avons pas besoin de ça.":"Нам це не потрібно.",
"Vous n'avez pas besoin de ça.":"Вам це не потрібно.",
"Ils n'ont pas besoin de ça.":"Їм це не потрібно.",
"Je n'entends pas Anna.":"Я не чую Анну.",
"Tu n'entends pas Anna.":"Ти не чуєш Анну.",
"Il n'entend pas Anna.":"Він не чує Анну.",
"Elle n'entend pas Anna.":"Вона не чує Анну.",
"Nous n'entendons pas Anna.":"Ми не чуємо Анну.",
"Vous n'entendez pas Anna.":"Ви не чуєте Анну.",
"Ils n'entendent pas Anna.":"Вони не чують Анну.",
"Je ne viens pas aujourd'hui, mais demain.":"Я прийду не сьогодні, а завтра.",
"Il n'habite pas à Berlin, mais à Munich.":"Він живе не в Берліні, а в Мюнхені.",
"Nous n'y allons pas en voiture, mais en train.":"Ми їдемо не автомобілем, а потягом.",
"Elle n'achète pas la robe rouge, mais la bleue.":"Вона купує не червону сукню, а синю.",
"Nous ne mangeons pas à la maison, mais au restaurant.":"Ми їмо не вдома, а в ресторані.",
"Il ne travaille pas le lundi, mais le mardi.":"Він працює не в понеділок, а у вівторок.",
"Je n'apprends pas le français, mais l'allemand.":"Я вчу не французьку, а німецьку.",
"Elle ne chante pas fort, mais doucement.":"Вона співає не голосно, а тихо.",
"On ne se retrouve pas à deux heures, mais à trois heures.":"Ми зустрічаємося не о другій, а о третій.",
"Je ne bois pas de thé, mais du café.":"Я п'ю не чай, а каву.",
"Il ne lit pas le journal, mais un livre.":"Він читає не газету, а книжку.",
"Vous n'y allez pas à pied, mais en bus.":"Ви йдете не пішки, а їдете автобусом.",
"Ils ne viennent pas seuls, mais à deux.":"Вони приходять не самі, а вдвох.",
"Nous n'habitons pas en ville, mais à la campagne.":"Ми живемо не в місті, а на селі.",
"Tu ne rends pas visite à ta tante, mais à ton oncle.":"Ти йдеш у гості не до тітки, а до дядька.",
}

d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
entrees, rates = [], []
for e in d["jeux"]["wortstellungNichtExercises"]:
    fr, x, h = e["translation"], e["explanation"], e.get("hint", "")
    if fr not in T: rates.append("PHRASE : " + fr); continue
    if h not in H: rates.append("INDICE : " + h); continue

    if x == "Négation générale de toute l'action → « nicht » en fin de phrase.":
        expl = "Загальне заперечення всієї дії → « nicht » у кінці речення."
    elif x == ("Quand la négation porte sur toute l'action, « nicht » se place "
               "généralement à la fin de la phrase."):
        expl = ("Коли заперечення стосується всієї дії, « nicht » зазвичай "
                "стає в кінці речення.")
    elif re.match(r"^« (.+?) » est un nom propre \(défini\) : la négation générale se fait "
                  r"avec « nicht », pas « kein »\.$", x):
        mot = re.match(r"^« (.+?) »", x).group(1)
        expl = ("« %s » — власна назва (означена): загальне заперечення робиться "
                "через « nicht », а не « kein »." % mot)
    elif re.match(r"^« (.+?) » est un nom propre \(défini\) : négation avec « nicht » "
                  r"en fin de phrase\.$", x):
        mot = re.match(r"^« (.+?) »", x).group(1)
        expl = ("« %s » — власна назва (означена): заперечення через « nicht » "
                "у кінці речення." % mot)
    elif re.match(r"^« (.+?) » est un pronom défini : négation avec « nicht » "
                  r"en fin de phrase\.$", x):
        mot = re.match(r"^« (.+?) »", x).group(1)
        expl = ("« %s » — означений займенник: заперечення через « nicht » "
                "у кінці речення." % mot)
    elif re.match(r"^« (.+?) » est démonstratif \(défini\) : négation avec « nicht » "
                  r"en fin de phrase\.$", x):
        mot = re.match(r"^« (.+?) »", x).group(1)
        expl = ("« %s » — вказівне слово (означене): заперечення через « nicht » "
                "у кінці речення." % mot)
    elif x.startswith("Quand « nicht » ne porte que sur un élément précis"):
        m = re.match(r"^Quand « nicht » ne porte que sur un élément précis \(ici « (.+?) », "
                     r"contrasté avec « (.+?) »\), il se place juste avant cet élément, "
                     r"pas en fin de phrase\.$", x)
        if not m: rates.append("EXPL : " + x); continue
        expl = ("Коли « nicht » стосується лише певного елемента (тут « %s », "
                "протиставленого « %s »), воно стає безпосередньо перед ним, "
                "а не в кінці речення." % m.groups())
    else:
        m = re.match(r"^« nicht » précède directement l'élément contrasté « (.+?) »\.$", x)
        if not m: rates.append("EXPL : " + x); continue
        expl = ("« nicht » стоїть безпосередньо перед протиставленим елементом "
                "« %s »." % m.group(1))

    entrees.append({"question": e["question"], "translation_uk": T[fr],
                    "hint_uk": H[h], "explanation_uk": expl})

if rates:
    print("REFUS : %d" % len(rates))
    for r in rates[:8]: print("   " + r)
    sys.exit(1)
io.open(os.path.join(R, "corrections_uk", "exos_wortstellungNicht.json"), "w",
        encoding="utf-8", newline="\n").write(
    json.dumps({"jeu": "wortstellungNichtExercises", "entrees": entrees},
               ensure_ascii=False, indent=1) + "\n")
print("exos_wortstellungNicht.json : %d entrees" % len(entrees))
