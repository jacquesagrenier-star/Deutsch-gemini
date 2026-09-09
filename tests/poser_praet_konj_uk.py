# -*- coding: utf-8 -*-
"""praeteritumExercises (70) et konjunktiv2Exercises (70), par moules.

Les 140 explications sont toutes differentes A LA LECTURE, et pourtant elles
ne portent que quelques MOULES : un debut francais (« Preterit fort de »,
« Konjunktiv II de »...), un milieu francais (« a la 2e personne du pluriel »)
et, entre les deux, des formes ALLEMANDES qui ne se traduisent pas.

On traduit donc les fragments francais, une fois chacun, et le script
reassemble. C'est ce qui garantit que « a la 2e personne du pluriel » se dit
avec les memes mots dans les 140 explications.

⚠️ REFUS D'ECRIRE si un fragment francais n'est pas couvert, ou s'il reste du
francais dans le resultat. Un moule silencieusement rate poserait une regle
a moitie traduite, et aucun controle ensuite ne verrait la difference.

    python tests/poser_praet_konj_uk.py        ecrit les deux fichiers
"""
import io, json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORR = os.path.join(RACINE, "corrections_uk")

# ---------- fragments francais -> ukrainien ----------
# Ordre important : les plus longs d'abord, sinon un fragment court mange
# le debut d'un plus long.
FRAGMENTS = [
 # ⚠️ CE SUFFIXE EN PREMIER. Il contient « + infinitif », que le fragment
 # court plus bas remplacerait d'abord -- le suffixe ne se reconnaitrait plus
 # ensuite et repartirait a moitie en francais. Signale par le garde-fou.
 (" — c'est aussi l'auxiliaire de toutes les constructions « würde + infinitif ».",
  " — це також допоміжне дієслово всіх конструкцій « würde + інфінітив »."),
 ("Pour la plupart des verbes, le Konjunktiv II moderne se forme avec ",
  "У більшості дієслів сучасний Konjunktiv II утворюється з "),
 (" à la 2e personne (un -e- s'intercale car le radical finit en -ß) ",
  " у 2-й особі (вставляється -e-, бо основа закінчується на -ß) "),
 (" + infinitif à la fin de la phrase ", " + інфінітив у кінці речення "),
 (" + infinitif à la 1re personne du pluriel ", " + інфінітив у 1-й особі множини "),
 (" + infinitif à la 2e personne du pluriel ", " + інфінітив у 2-й особі множини "),
 (" + infinitif à la 2e personne ", " + інфінітив у 2-й особі "),
 (" + infinitif à la 3e personne ", " + інфінітив у 3-й особі "),
 (" + infinitif ", " + інфінітив "),
 (" à la 1re personne du pluriel ", " у 1-й особі множини "),
 (" à la 2e personne du pluriel ", " у 2-й особі множини "),
 (" à la 2e personne ", " у 2-й особі "),
 (" à la 3e personne ", " у 3-й особі "),
 (" (radical ", " (основа "),
 ("Prétérit irrégulier de ", "Неправильний претерит "),
 ("Prétérit fort de ", "Сильний претерит "),
 ("Konjunktiv II de ", "Konjunktiv II дієслова "),
 ("Construction ", "Конструкція "),
 # Trois suffixes que le releve initial avait manques : ils ne tiennent qu'a
 # quatre exercices sur 70, et c'est le garde-fou qui les a signales, pas la
 # lecture. Sans lui, quatre explications seraient parties a moitie en francais.
 (" — la forme polie pour « vouloir » dans une demande.",
  " — ввічлива форма для « хотіти » у проханні."),
 (" — forme polie pour demander une permission.",
  " — ввічлива форма, щоб попросити дозволу."),
 (" — forme polie pour une demande.",
  " — ввічлива форма для прохання."),
]
INDICES = [
 (" — verbe irrégulier)", " — неправильне дієслово)"),
 (" — verbe fort)", " — сильне дієслово)"),
 (" — würde + infinitif)", " — würde + інфінітив)"),
 (" — Konjunktiv II)", " — Konjunktiv II)"),
]
# Tout mot francais qui survivrait a la traduction : le script s'arrete.
# ⚠️ UNIQUEMENT DES MOTS DISTINCTIFS. Le premier jet listait « du », « le »,
# « est », « fort »... et prenait le « du warst » allemand pour du francais :
# le garde-fou refusait les 140 explications, toutes correctes. Un filet qui
# attrape tout n'attrape rien -- on le rend PRECIS plutot que large.
RESTE_FR = re.compile(
 r"\b(personne|pluriel|radical|verbe|irrégulier|Prétérit|Construction|infinitif"
 r"|auxiliaire|constructions|toutes|aussi|car|finit|intercale|plupart|moderne"
 r"|phrase|forme)\b", re.I)

def traduire(texte, table):
    for fr, uk in table:
        texte = texte.replace(fr, uk)
    return texte

T_PRAET = {
"J'étais à Berlin l'année dernière.":"Торік я був у Берліні.",
"Je n'avais pas le temps hier.":"Учора я не мав часу.",
"Je suis devenu professeur à vingt-cinq ans.":"У двадцять п'ять я став учителем.",
"Je suis allé au cinéma hier soir.":"Учора ввечері я ходив у кіно.",
"Je suis arrivé en retard au travail.":"Я запізнився на роботу.",
"Je l'ai vu la semaine dernière au parc.":"Минулого тижня я бачив його в парку.",
"J'ai mangé un petit pain ce matin.":"Сьогодні вранці я з'їв булочку.",
"J'ai bu trop de café hier.":"Учора я випив забагато кави.",
"Je lui ai donné mon numéro de téléphone.":"Я дав йому свій номер телефону.",
"J'ai pris le bus au lieu du train.":"Я поїхав автобусом замість потяга.",
"Je suis allé en Italie l'année dernière.":"Торік я їздив до Італії.",
"J'ai lu tout le livre en une journée.":"Я прочитав усю книжку за день.",
"Je lui ai écrit une longue lettre.":"Я написав йому довгого листа.",
"J'ai parlé avec mon patron hier.":"Учора я говорив зі своїм начальником.",
"Étais-tu à la maison hier ?":"Ти був учора вдома?",
"Avais-tu un animal de compagnie enfant ?":"Чи мав ти в дитинстві домашню тварину?",
"Quand es-tu devenu père ?":"Коли ти став батьком?",
"Es-tu allé nager l'été dernier ?":"Ти ходив плавати минулого літа?",
"Quand es-tu rentré à la maison hier ?":"Коли ти вчора повернувся додому?",
"As-tu vu le film la semaine dernière ?":"Ти бачив той фільм минулого тижня?",
"Qu'as-tu mangé au petit-déjeuner ?":"Що ти їв на сніданок?",
"As-tu bu mon café par erreur ?":"Ти випив мою каву помилково?",
"Lui as-tu donné le cadeau ?":"Ти дав йому подарунок?",
"As-tu pris mon parapluie ?":"Ти взяв мою парасольку?",
"Es-tu allé seul à Munich ?":"Ти їздив до Мюнхена сам?",
"As-tu lu le journal ce matin ?":"Ти читав газету сьогодні вранці?",
"As-tu passé l'examen la semaine dernière ?":"Ти складав іспит минулого тижня?",
"Parlais-tu allemand quand tu étais petit ?":"Ти говорив німецькою, коли був малим?",
"Il était très malade l'année dernière.":"Торік він був дуже хворий.",
"Elle n'avait aucune idée de l'affaire.":"Вона гадки не мала про цю справу.",
"Il est soudainement devenu très pâle.":"Він раптом дуже зблід.",
"Elle allait courir tous les matins.":"Вона щоранку ходила бігати.",
"Il est venu sans prévenir.":"Він прийшов без попередження.",
"Elle l'a vu pour la dernière fois en mai.":"Востаннє вона бачила його в травні.",
"Il n'a rien mangé de toute la journée.":"Він цілий день нічого не їв.",
"Elle buvait un verre de vin chaque soir.":"Вона щовечора випивала келих вина.",
"Il a donné de l'argent au mendiant.":"Він дав грошей жебракові.",
"Elle a assumé la responsabilité de l'erreur.":"Вона взяла на себе відповідальність за помилку.",
"Il roulait trop vite sur l'autoroute.":"Він їхав автобаном надто швидко.",
"Elle a lu le verdict à voix haute.":"Вона прочитала вирок уголос.",
"Il a écrit le scénario du film.":"Він написав сценарій фільму.",
"Elle parlait trois langues couramment.":"Вона вільно говорила трьома мовами.",
"Nous étions au théâtre hier.":"Учора ми були в театрі.",
"Nous avons eu beaucoup de chance l'été dernier.":"Минулого літа нам дуже пощастило.",
"Nous devenions peu à peu impatients.":"Ми поволі ставали нетерплячими.",
"Nous sommes allés nous promener ensemble.":"Ми разом пішли гуляти.",
"Nous sommes arrivés juste à temps.":"Ми прийшли якраз вчасно.",
"Nous avons vu un magnifique feu d'artifice.":"Ми бачили чудовий феєрверк.",
"Nous avons dîné ensemble.":"Ми повечеряли разом.",
"Nous avons bu à sa santé.":"Ми випили за його здоров'я.",
"Nous leur avons donné toutes les informations.":"Ми дали їм усю інформацію.",
"Nous avons pris le premier train du matin.":"Ми поїхали першим ранковим потягом.",
"Nous avons traversé toute la ville.":"Ми проїхали через усе місто.",
"Nous avons lu le livre pour le cours d'allemand.":"Ми прочитали книжку для уроку німецької.",
"Nous avons écrit une carte ensemble.":"Ми разом написали листівку.",
"Nous avons longtemps parlé de l'avenir.":"Ми довго говорили про майбутнє.",
"Étiez-vous en Espagne l'année dernière ?":"Ви були торік в Іспанії?",
"Aviez-vous assez de temps pour l'examen ?":"Чи мали ви досить часу на іспит?",
"Comment êtes-vous devenus de si bons amis ?":"Як ви стали такими добрими друзями?",
"Êtes-vous allés randonner le week-end ?":"Ви ходили в похід на вихідних?",
"Êtes-vous arrivés à l'heure à la fête ?":"Ви прийшли на свято вчасно?",
"Avez-vous vu l'arc-en-ciel hier ?":"Ви бачили вчора веселку?",
"Qu'avez-vous mangé à la fête ?":"Що ви їли на святі?",
"Avez-vous bu assez d'eau pendant la randonnée ?":"Чи пили ви досить води під час походу?",
"Lui avez-vous donné une seconde chance ?":"Ви дали йому другий шанс?",
"Avez-vous pris le raccourci à travers la forêt ?":"Ви пішли навпростець через ліс?",
"Êtes-vous allés en voiture ou en train ?":"Ви їхали автомобілем чи потягом?",
"Avez-vous lu la notice avant le montage ?":"Ви читали інструкцію перед складанням?",
"Avez-vous écrit une excuse au professeur ?":"Ви написали вчителеві пояснення?",
"Avez-vous parlé assez fort pour tout le monde ?":"Чи говорили ви досить гучно, щоб усі чули?",
}

T_KONJ = {
"Si j'étais riche, je ne travaillerais plus.":"Якби я був багатий, я б більше не працював.",
"Si j'avais plus de temps, je voyagerais plus souvent.":"Якби я мав більше часу, я б частіше подорожував.",
"À ta place, je serais plus prudent.":"На твоєму місці я був би обережніший.",
"Je pourrais t'aider si j'avais le temps.":"Я міг би тобі допомогти, якби мав час.",
"En fait, je devrais me lever plus tôt.":"Власне, я мав би вставати раніше.",
"Pourrais-je utiliser votre téléphone un instant ?":"Чи міг би я на хвилинку скористатися вашим телефоном?",
"Je devrais en fait manger moins de bonbons.":"Власне, мені слід було б їсти менше солодощів.",
"Je voudrais bien un verre d'eau.":"Я хотів би склянку води.",
"J'aimerais bien savoir ce qu'il pense vraiment.":"Я хотів би знати, що він насправді думає.",
"S'il ne pleuvait pas, j'irais me promener.":"Якби не йшов дощ, я б пішов гуляти.",
"Si je pouvais, je viendrais tout de suite.":"Якби я міг, я б прийшов одразу.",
"Avec plus d'argent, j'achèterais une nouvelle voiture.":"Маючи більше грошей, я б купив нове авто.",
"Sans la blessure, je jouerais au football aujourd'hui.":"Якби не травма, я б сьогодні грав у футбол.",
"Un dimanche, je ne travaillerais jamais.":"У неділю я б ніколи не працював.",
"Si tu étais à ma place, que ferais-tu ?":"Якби ти був на моєму місці, що б ти зробив?",
"Si tu avais plus de patience, tout serait plus simple.":"Якби ти мав більше терпіння, усе було б простіше.",
"Ferais-tu la même chose à ma place ?":"Чи зробив би ти те саме на моєму місці?",
"Pourrais-tu me passer le sel, s'il te plaît ?":"Чи міг би ти подати мені сіль, будь ласка?",
"En fait, tu devrais faire plus d'efforts.":"Власне, тобі слід було б більше старатися.",
"Aurais-tu vraiment le droit de faire ça à ma place ?":"Чи справді ти мав би право робити це на моєму місці?",
"Tu devrais vraiment t'excuser.":"Тобі справді слід було б вибачитися.",
"Voudrais-tu boire quelque chose aussi ?":"Чи хотів би ти теж щось випити?",
"Aimerais-tu savoir comment se termine l'histoire ?":"Чи хотів би ти знати, чим закінчується історія?",
"Si tu étais libre, irais-tu randonner avec moi ?":"Якби ти був вільний, чи пішов би ти зі мною в похід?",
"Viendrais-tu plus tôt demain si j'avais besoin de toi ?":"Чи прийшов би ти завтра раніше, якби я тебе потребував?",
"Achèterais-tu la robe si elle était moins chère ?":"Чи купив би ти цю сукню, якби вона була дешевша?",
"Préférerais-tu jouer au tennis ou nager ?":"Ти б радше грав у теніс чи плавав?",
"Travaillerais-tu aussi à l'étranger ?":"Чи працював би ти також за кордоном?",
"S'il était honnête, il l'admettrait.":"Якби він був чесний, він би це визнав.",
"Si elle avait plus d'expérience, elle obtiendrait le poste.":"Якби вона мала більше досвіду, вона б отримала цю посаду.",
"Il a dit qu'il le ferait tout de suite.":"Він сказав, що зробив би це одразу.",
"Elle pourrait réussir l'examen si elle étudiait davantage.":"Вона могла б скласти іспит, якби більше вчилася.",
"En fait, il devrait s'excuser.":"Власне, йому слід було б вибачитися.",
"Aurait-elle le droit d'emprunter la voiture si elle demandait ?":"Чи мала б вона право позичити авто, якби попросила?",
"Il devrait faire plus attention à sa santé.":"Йому слід було б більше дбати про своє здоров'я.",
"Elle aimerait bien voyager au Japon.":"Вона хотіла б поїхати до Японії.",
"Il aimerait bien savoir si elle lui en veut encore.":"Він хотів би знати, чи вона ще сердиться на нього.",
"S'il faisait soleil, elle irait nager.":"Якби світило сонце, вона б пішла плавати.",
"Il a dit qu'il viendrait plus tard.":"Він сказав, що прийшов би пізніше.",
"Avec plus de budget, elle achèterait une plus grande maison.":"Маючи більший бюджет, вона б купила більший будинок.",
"Sans pluie, il jouerait au golf aujourd'hui.":"Якби не дощ, він би сьогодні грав у гольф.",
"Elle préférerait travailler de chez elle.":"Вона радше працювала б з дому.",
"Si nous étions plus riches, nous voyagerions davantage.":"Якби ми були багатші, ми б більше подорожували.",
"Si nous avions plus de courage, nous essaierions.":"Якби ми мали більше сміливості, ми б спробували.",
"Ferions-nous la même chose à ta place ?":"Чи зробили б ми те саме на твоєму місці?",
"Nous pourrions partir plus tôt si nous le voulions.":"Ми могли б піти раніше, якби захотіли.",
"En fait, nous devrions économiser davantage.":"Власне, нам слід було б більше заощаджувати.",
"Aurions-nous le droit de fumer ici si personne n'était là ?":"Чи мали б ми право тут курити, якби нікого не було?",
"Nous devrions parler plus souvent ensemble.":"Нам слід було б частіше розмовляти.",
"Nous aimerions bien avoir un peu plus de temps.":"Ми хотіли б мати трохи більше часу.",
"Nous aimerions bien savoir quand arrive le résultat.":"Ми хотіли б знати, коли буде результат.",
"S'il faisait plus froid, nous n'irions pas nager.":"Якби було холодніше, ми б не пішли плавати.",
"Nous viendrions bien plus tôt, mais le train est annulé.":"Ми б залюбки прийшли раніше, але потяг скасовано.",
"Avec un plus grand budget, nous achèterions un bateau.":"Маючи більший бюджет, ми б купили човен.",
"S'il faisait beau, nous jouerions dehors.":"Якби була гарна погода, ми б грали надворі.",
"Sans cette commande, nous ne travaillerions pas le week-end.":"Якби не це замовлення, ми б не працювали у вихідні.",
"Si vous étiez à notre place, que feriez-vous ?":"Якби ви були на нашому місці, що б ви зробили?",
"Si vous aviez plus de pratique, l'examen serait plus facile.":"Якби ви мали більше практики, іспит був би легший.",
"Feriez-vous la même chose ?":"Чи зробили б ви те саме?",
"Pourriez-vous nous aider demain ?":"Чи могли б ви нам завтра допомогти?",
"En fait, vous devriez partir plus tôt.":"Власне, вам слід було б вийти раніше.",
"Auriez-vous le droit d'entrer dans la pièce si vous demandiez ?":"Чи мали б ви право зайти до кімнати, якби попросили?",
"Vous devriez vraiment vous reposer davantage.":"Вам справді слід було б більше відпочивати.",
"Voudriez-vous manger quelque chose aussi ?":"Чи хотіли б ви теж щось з'їсти?",
"Aimeriez-vous savoir ce qui se passe ensuite ?":"Чи хотіли б ви знати, що буде далі?",
"Si vous aviez le temps, iriez-vous randonner avec nous ?":"Якби ви мали час, чи пішли б ви з нами в похід?",
"Viendriez-vous plus tôt si nous avions besoin de vous ?":"Чи прийшли б ви раніше, якби ми вас потребували?",
"Achèteriez-vous la maison si vous aviez l'argent ?":"Чи купили б ви будинок, якби мали гроші?",
"Préféreriez-vous jouer aux cartes ou regarder la télé ?":"Ви б радше грали в карти чи дивилися телевізор?",
"Travailleriez-vous aussi le week-end ?":"Чи працювали б ви також у вихідні?",
}


def faire(jeu, table, sortie):
    d = json.load(io.open(os.path.join(RACINE, "exercices.json"), encoding="utf-8"))
    entrees, rates = [], []
    for e in d["jeux"][jeu]:
        fr = e["translation"]
        tran = table.get(fr)
        if not tran:
            rates.append("PHRASE SANS TRADUCTION : " + fr); continue
        expl = traduire(e["explanation"], FRAGMENTS)
        hint = traduire(e.get("hint", ""), INDICES)
        if RESTE_FR.search(expl):
            rates.append("FRANCAIS RESTANT dans l'explication : " + expl[:80]); continue
        if RESTE_FR.search(hint):
            rates.append("FRANCAIS RESTANT dans l'indice : " + hint); continue
        entrees.append({"question": e["question"], "cle_translation": fr,
                        "translation_uk": tran, "hint_uk": hint, "explanation_uk": expl})
    if rates:
        print("REFUS D'ECRIRE (%s) : %d cas." % (jeu, len(rates)))
        for r in rates[:10]: print("   " + r)
        return 1
    io.open(os.path.join(CORR, sortie), "w", encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": jeu, "entrees": entrees}, ensure_ascii=False, indent=1) + "\n")
    print("%-34s %3d entrees" % (sortie, len(entrees)))
    return 0


sys.exit(faire("praeteritumExercises", T_PRAET, "exos_praeteritum.json")
         or faire("konjunktiv2Exercises", T_KONJ, "exos_konjunktiv2.json"))
