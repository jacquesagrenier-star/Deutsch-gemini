# -*- coding: utf-8 -*-
"""infinitivExercises (70) : cinq moules pour 70 explications."""
import io, json, os, re, sys

RACINE = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
QSUF_FR = " Quel est l'infinitif du verbe conjugué ?"
QSUF_UK = " Який інфінітив дієвідмінюваного дієслова?"

T = {
"Que fais-tu en ce moment ?":"Що ти зараз робиш?",
"Les enfants jouent dans le jardin.":"Діти граються в саду.",
"Elle achète un nouveau vélo.":"Вона купує новий велосипед.",
"Nous habitons ici depuis cinq ans.":"Ми живемо тут п'ять років.",
"Il travaille dans une banque.":"Він працює в банку.",
"J'attends déjà depuis une heure.":"Я чекаю вже годину.",
"Je trouve ça très intéressant.":"Мені це видається дуже цікавим.",
"Comment t'appelles-tu ?":"Як тебе звати?",
"Ils voyagent chaque année en Espagne.":"Вони щороку їздять до Іспанії.",
"Il collectionne les vieux timbres.":"Він збирає старі марки.",
"Nous randonnons tous les dimanches.":"Ми ходимо в походи щонеділі.",
"Le bébé dort déjà.":"Немовля вже спить.",
"Il court cinq kilomètres tous les matins.":"Він щоранку пробігає п'ять кілометрів.",
"Nous partons en avion au Canada la semaine prochaine.":"Наступного тижня ми летимо до Канади.",
"Elle chante très bien.":"Вона дуже гарно співає.",
"Les couples dansent sur la musique.":"Пари танцюють під музику.",
"Mon père cuisine tous les soirs.":"Мій батько готує щовечора.",
"Ma grand-mère fait cuire un gâteau.":"Моя бабуся пече торт.",
"Je lave ma voiture le samedi.":"Я мию своє авто в суботу.",
"Il aide son frère avec ses devoirs.":"Він допомагає братові з домашнім завданням.",
"Nous nous retrouvons à huit heures.":"Ми зустрічаємося о восьмій годині.",
"Peux-tu m'apporter le livre ?":"Чи можеш ти принести мені книжку?",
"Je pense souvent à toi.":"Я часто думаю про тебе.",
"Je ne comprends pas la question.":"Я не розумію запитання.",
"Le film commence à neuf heures.":"Фільм починається о дев'ятій годині.",
"Nous restons à la maison aujourd'hui.":"Сьогодні ми лишаємося вдома.",
"Le verre tombe de la table.":"Склянка падає зі столу.",
"Le bus s'arrête à chaque coin de rue.":"Автобус зупиняється на кожному розі.",
"Elle porte un manteau rouge.":"Вона носить червоне пальто.",
"Il tire le chariot le long de la rue.":"Він тягне візок уздовж вулиці.",
"Le magasin ferme à dix-huit heures.":"Магазин зачиняється о вісімнадцятій годині.",
"Elle ouvre la fenêtre.":"Вона відчиняє вікно.",
"Notre équipe gagne le match.":"Наша команда виграє матч.",
"Il perd toujours ses clés.":"Він завжди губить свої ключі.",
"J'oublie souvent son nom.":"Я часто забуваю його ім'я.",
"Les enfants rient fort.":"Діти голосно сміються.",
"Le bébé pleure toute la nuit.":"Немовля плаче цілу ніч.",
"Je me sens mieux aujourd'hui.":"Сьогодні я почуваюся краще.",
"Entends-tu la musique ?":"Ти чуєш музику?",
"Le repas sent très bon.":"Їжа дуже смачно пахне.",
"La soupe a un goût délicieux.":"Суп надзвичайно смачний.",
"Je connais bien cette ville.":"Я добре знаю це місто.",
"Nous avons besoin de plus de temps.":"Нам потрібно більше часу.",
"La robe me plaît beaucoup.":"Сукня мені дуже подобається.",
"Le livre m'appartient.":"Книжка належить мені.",
"La voiture est garée devant la maison.":"Авто стоїть перед будинком.",
"Le chat est allongé sur le canapé.":"Кіт лежить на дивані.",
"Il est assis près de la fenêtre.":"Він сидить біля вікна.",
"Elle pose le livre sur la table.":"Вона кладе книжку на стіл.",
"Je mets le vase sur l'étagère.":"Я ставлю вазу на полицю.",
"Il s'assoit sur la chaise.":"Він сідає на стілець.",
"Elle nettoie la maison tous les samedis.":"Вона прибирає в домі щосуботи.",
"Je me douche tous les matins.":"Я приймаю душ щоранку.",
"Il essaie encore une fois.":"Він пробує ще раз.",
"Nous planifions un grand voyage.":"Ми плануємо велику подорож.",
"Elle choisit la robe bleue.":"Вона обирає синю сукню.",
"Les citoyens élisent un nouveau président.":"Громадяни обирають нового президента.",
"Je paie la facture tout de suite.":"Я одразу оплачую рахунок.",
"Il vend sa vieille voiture.":"Він продає своє старе авто.",
"Nous louons un appartement au bord de la mer.":"Ми винаймаємо квартиру біля моря.",
"Puis-je vous demander quelque chose ?":"Чи можу я вас щось запитати?",
"Il ne répond jamais à mes messages.":"Він ніколи не відповідає на мої повідомлення.",
"Ma grand-mère aime raconter des histoires.":"Моя бабуся любить розповідати історії.",
"Le professeur explique la règle encore une fois.":"Учитель ще раз пояснює правило.",
"Peux-tu me montrer le chemin ?":"Чи можеш ти показати мені дорогу?",
"Le chien suit son maître partout.":"Пес усюди йде за своїм господарем.",
"L'école commence à huit heures.":"Школа починається о восьмій годині.",
"La pluie s'arrête enfin.":"Дощ нарешті вщухає.",
"Je me lève tous les jours à sept heures.":"Я щодня встаю о сьомій годині.",
"Elle se réveille toujours tôt.":"Вона завжди прокидається рано.",
}

d = json.load(io.open(os.path.join(RACINE, "exercices.json"), encoding="utf-8"))
entrees, rates = [], []
for e in d["jeux"]["infinitivExercises"]:
    fr, q, x, h = e["translation"], e["question"], e["explanation"], e.get("hint", "")
    if fr not in T: rates.append("PHRASE : " + fr); continue
    if not q.endswith(QSUF_FR): rates.append("QUESTION : " + q); continue

    m = re.match(r"^« (.+?) » est la forme « (.+?) » de l'infinitif « (.+?) »\.$", x)
    m2 = re.match(r"^« (.+?) » est ici déjà la forme du pluriel, identique à l'infinitif\.$", x)
    m3 = re.match(r"^« (.+?) » est la forme « (.+?) » de l'infinitif « (.+?) » \(voyelle qui change : (.+?)\)\.$", x)
    m4 = re.match(r"^Après un verbe modal comme « (.+?) », le second verbe reste à l'infinitif : (.+?)\.$", x)
    m5 = re.match(r"^« (.+?) » est la forme éclatée du verbe à particule séparable « (.+?) »(.*)$", x)
    if m3:
        expl = "« %s » — це форма « %s » інфінітива « %s » (голосний змінюється: %s)." % m3.groups()
    elif m:
        expl = "« %s » — це форма « %s » інфінітива « %s »." % m.groups()
    elif m2:
        expl = "« %s » тут уже форма множини, тотожна інфінітиву." % m2.group(1)
    elif m4:
        expl = ("Після модального дієслова на кшталт « %s » друге дієслово лишається "
                "в інфінітиві: %s." % m4.groups())
    elif m5:
        forme, inf, suite = m5.groups()
        expl = ("« %s » — це розділена форма дієслова з відокремлюваним префіксом « %s »"
                % (forme, inf))
        if suite.strip() == ".":
            expl += "."
        elif suite.startswith(" : la particule « ") and suite.endswith(" part à la fin de la phrase."):
            part = re.search(r"« (.+?) » part", suite).group(1)
            expl += " : префікс « %s » іде в кінець речення." % part
        else:
            rates.append("SUITE HORS MOULE : " + suite); continue
    else:
        rates.append("EXPL : " + x); continue

    # Trois formes d'indice, trouvees par le garde-fou : sept exercices sur 70
    # portent les deux dernieres, et une relecture les aurait manquees.
    mh = re.match(r"^\(le verbe conjugué est « (.+?) »\)$", h)
    mh2 = re.match(r"^\(le verbe conjugué est déjà à l'infinitif : « (.+?) », après le verbe modal « (.+?) »\)$", h)
    mh3 = re.match(r"^\(verbe à particule séparable : « (.+?) »\)$", h)
    if mh:
        hint = "(дієвідмінюване дієслово — « %s »)" % mh.group(1)
    elif mh2:
        hint = ("(дієслово вже в інфінітиві: « %s », після модального « %s »)" % mh2.groups())
    elif mh3:
        hint = "(дієслово з відокремлюваним префіксом: « %s »)" % mh3.group(1)
    else:
        rates.append("INDICE : " + h); continue
    entrees.append({"question": q, "translation_uk": T[fr],
                    "question_uk": q[:-len(QSUF_FR)] + QSUF_UK,
                    "hint_uk": hint, "explanation_uk": expl})
if rates:
    print("REFUS : %d" % len(rates))
    for r in rates[:8]: print("   " + r)
    sys.exit(1)
io.open(os.path.join(RACINE, "corrections_uk", "exos_infinitiv.json"), "w",
        encoding="utf-8", newline="\n").write(
    json.dumps({"jeu": "infinitivExercises", "entrees": entrees}, ensure_ascii=False, indent=1) + "\n")
print("exos_infinitiv.json : %d entrees" % len(entrees))
