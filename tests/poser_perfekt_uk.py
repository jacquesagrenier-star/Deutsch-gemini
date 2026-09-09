# -*- coding: utf-8 -*-
"""perfektExercises (145) : une grille de huit regles.

Les 145 exercices ne portent que HUIT formes d'explication, chacune avec deux
ou trois parties variables (le verbe, son participe, la forme fautive). On
traduit donc les huit MOULES, et le script remplit les trous en les lisant
dans l'explication francaise -- au lieu de recopier 145 fois une regle en
risquant qu'elle finisse dite de huit facons differentes.

Seules les 145 phrases d'exemple sont traduites a la main : elles n'ont rien
de commun, aucun moule ne les couvre.

⚠️ Le script REFUSE d'ecrire s'il rencontre une explication qui ne rentre dans
aucun moule, ou une phrase sans traduction. Un moule silencieusement rate
poserait une explication fausse, ce qu'aucun controle ne verrait ensuite.
"""
import io, json, os, re, sys

RACINE = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
SORTIE = os.path.join(RACINE, "corrections_uk", "exos_perfekt.json")

# ---------- les huit moules ----------
def m_faible(v, p):
    return "Слабке дієслово, правильне: ge- + основа + -t, основа не змінюється. %s → %s." % (v, p)
def m_faible_dt(v, p):
    return ("Слабке дієслово: ge- + основа + -t. Тут основа закінчується на -d або -t, звідси "
            "сполучне -e-, що робить слово вимовним: %s → %s." % (v, p))
def m_faible_mn(v, p):
    return ("Слабке дієслово: ge- + основа + -t. Тут основа закінчується на приголосний із -m або "
            "-n, звідси сполучне -e-, що робить слово вимовним: %s → %s." % (v, p))
def m_fort(v, p, faux):
    return ("Сильне дієслово: ge- + основа, часто зі зміною голосного, + -en. %s → %s. "
            "Це не %s." % (v, p, faux))
def m_ieren(v, p, faux):
    return "Дієслова на -ieren НІКОЛИ не беруть ge-: %s → %s, і аж ніяк не %s." % (v, p, faux)
def m_insep(v, p, faux):
    return ("Невідокремлюваний префікс (be-, emp-, ent-, er-, miss-, ver-, zer-): без ge-. "
            "%s → %s, а не %s." % (v, p, faux))
def m_sep(v, p, faux):
    return ("Дієслово з відокремлюваним префіксом: ge- прослизає МІЖ префіксом і основою. "
            "%s → %s, а не %s." % (v, p, faux))
def m_sein(v):
    return ("« %s » виражає переміщення або зміну стану: його Perfekt утворюється з sein, "
            "а не з haben." % v)
def m_haben(v):
    return ("« %s » не виражає ні переміщення, ні зміни стану: отже haben, як і для переважної "
            "більшості дієслів." % v)
def m_bleiben(v):
    return ("« %s » бере sein, не виражаючи ні переміщення, ні зміни стану: це виняток, який "
            "запам'ятовують як є, разом із bleiben, sein і werden." % v)

# ---------- les indices ----------
def h_type(v, t):
    return "(%s — %s)" % (v, t)
TYPES = {
 "verbe faible": "слабке дієслово",
 "verbe fort": "сильне дієслово",
 "en -ieren": "на -ieren",
 "préfixe inséparable": "невідокремлюваний префікс",
 "particule séparable": "відокремлюваний префікс",
}
H_HABEN_SEIN = "(haben чи sein?)"

# ---------- les 145 phrases ----------
T = {
"Le bébé a pleuré.":"Немовля плакало.",
"Je t'ai cru.":"Я тобі повірив.",
"J'ai écouté de la musique.":"Я слухав музику.",
"Je me suis garé ici.":"Я тут припаркувався.",
"J'ai dansé avec elle.":"Я танцював із нею.",
"Je me suis douché rapidement.":"Я швидко прийняв душ.",
"J'ai économisé beaucoup d'argent.":"Я заощадив багато грошей.",
"J'ai travaillé hier.":"Я вчора працював.",
"Je lui ai demandé directement.":"Я запитав його прямо.",
"J'ai eu besoin de plus de temps.":"Мені знадобилося більше часу.",
"L'enfant a peint un tableau.":"Дитина намалювала картину.",
"J'ai nettoyé ma chambre.":"Я прибрав свою кімнату.",
"Je t'ai montré le chemin.":"Я показав тобі дорогу.",
"J'ai senti la douleur.":"Я відчув біль.",
"J'ai beaucoup appris l'allemand.":"Я багато вчив німецьку.",
"Les enfants ont beaucoup ri.":"Діти багато сміялися.",
"J'ai attendu le bus.":"Я чекав на автобус.",
"J'ai ouvert la fenêtre.":"Я відчинив вікно.",
"Nous sommes allés en Italie.":"Ми подорожували до Італії.",
"J'ai acheté du pain frais.":"Я купив свіжого хліба.",
"Ils ont vécu longtemps ensemble.":"Вони довго жили разом.",
"Je t'ai répondu tout de suite.":"Я відповів тобі одразу.",
"Je t'ai dit la vérité.":"Я сказав тобі правду.",
"J'ai longtemps habité à Berlin.":"Я довго жив у Берліні.",
"J'ai cherché mes clés.":"Я шукав свої ключі.",
"Il est arrivé en retard.":"Він прийшов пізно.",
"Elle s'appelait Anna.":"Її звали Анна.",
"Elle est restée médecin.":"Вона лишилася лікаркою.",
"J'ai parlé allemand.":"Я говорив німецькою.",
"J'ai mangé une pizza.":"Я з'їв піцу.",
"J'ai mal dormi.":"Я погано спав.",
"J'ai fermé la porte.":"Я зачинив двері.",
"Je suis allé en voiture.":"Я поїхав автомобілем.",
"J'ai couru ce matin.":"Я бігав сьогодні вранці.",
"J'ai vu mes amis.":"Я бачив своїх друзів.",
"Nous sommes allés en Espagne en avion.":"Ми полетіли до Іспанії.",
"Je l'ai rencontrée au parc.":"Я зустрів її в парку.",
"Je me suis lavé les mains.":"Я вимив руки.",
"Elle a porté une veste rouge.":"Вона носила червону куртку.",
"La mère a appelé les enfants.":"Мати покликала дітей.",
"Nous avons nagé jusqu'à l'île.":"Ми пливли до острова.",
"La voiture était garée devant la maison.":"Автомобіль стояв перед будинком.",
"Je t'ai écrit un e-mail.":"Я написав тобі електронного листа.",
"J'ai bu du café ce matin.":"Я пив каву сьогодні вранці.",
"J'ai lu un livre hier soir.":"Учора ввечері я читав книжку.",
"Le soleil a brillé.":"Сонце світило.",
"Ça a sonné bizarre.":"Це звучало дивно.",
"J'ai chargé les caisses.":"Я завантажив ящики.",
"Il a grimpé la montagne.":"Він піднявся на гору.",
"Il s'est cassé le bras.":"Він зламав собі руку.",
"J'ai étudié la médecine.":"Я вивчав медицину.",
"Qu'est-ce qui s'est passé ?":"Що сталося?",
"Je l'ai félicité.":"Я його привітав.",
"Ça a fonctionné tout de suite.":"Це запрацювало одразу.",
"J'ai tout contrôlé.":"Я все перевірив.",
"J'ai marqué la date.":"Я позначив дату.",
"Nous avons tout organisé.":"Ми все організували.",
"J'ai téléphoné avec lui.":"Я говорив із ним по телефону.",
"Nous avons réduit le prix.":"Ми знизили ціну.",
"J'ai réservé la table.":"Я забронював столик.",
"Ça m'a beaucoup intéressé.":"Це мене дуже зацікавило.",
"J'ai formulé la réponse.":"Я сформулював відповідь.",
"J'ai installé la mise à jour.":"Я встановив оновлення.",
"J'ai réparé l'ordinateur.":"Я полагодив комп'ютер.",
"Nous avons discuté de politique.":"Ми обговорювали політику.",
"J'ai critiqué la décision.":"Я розкритикував рішення.",
"Cette règle a toujours existé.":"Це правило існувало завжди.",
"Je t'ai informé de la situation.":"Я повідомив тобі про ситуацію.",
"Nous avons investi de l'argent dans l'entreprise.":"Ми вклали гроші в підприємство.",
"J'ai réagi immédiatement au message.":"Я одразу відреагував на повідомлення.",
"Il a risqué beaucoup d'argent.":"Він ризикнув великими грошима.",
"Elle a délégué le travail.":"Вона делегувала роботу.",
"Il a ignoré l'avertissement.":"Він проігнорував попередження.",
"Il a spéculé avec des actions.":"Він спекулював акціями.",
"Ils ont importé beaucoup de fruits.":"Вони імпортували багато фруктів.",
"Elle a bien gagné sa vie.":"Вона добре заробляла.",
"J'ai commencé le travail.":"Я почав роботу.",
"J'ai payé la facture.":"Я оплатив рахунок.",
"J'ai reçu un cadeau.":"Я отримав подарунок.",
"Je leur ai rendu visite la semaine dernière.":"Я відвідав їх минулого тижня.",
"Il a vendu son vieux vélo.":"Він продав свій старий велосипед.",
"Je n'ai pas compris la question.":"Я не зрозумів запитання.",
"Je t'ai raconté une histoire.":"Я розповів тобі історію.",
"Elle a excusé son retard.":"Вона вибачилася за запізнення.",
"Le professeur nous a expliqué la grammaire.":"Учитель пояснив нам граматику.",
"J'ai oublié ma clé hier.":"Учора я забув ключа.",
"J'ai tout réglé.":"Я все залагодив.",
"Je le lui ai permis.":"Я йому це дозволив.",
"J'ai déplacé la chaise.":"Я пересунув стілець.",
"J'ai remplacé la pièce.":"Я замінив деталь.",
"Je ne l'ai pas remarqué.":"Я цього не помітив.",
"J'ai commandé le livre.":"Я замовив книжку.",
"Nous avons déterminé le lieu.":"Ми визначили місце.",
"Je l'ai déjà mentionné.":"Я вже про це згадував.",
"J'y ai renoncé.":"Я від цього відмовився.",
"J'ai atteint mon objectif.":"Я досяг своєї мети.",
"Je ne m'y attendais pas.":"Я цього не очікував.",
"J'ai supprimé le fichier.":"Я видалив файл.",
"Je viens de l'apprendre.":"Я щойно про це дізнався.",
"Nous avons augmenté le budget.":"Ми збільшили бюджет.",
"Je me suis levé tard.":"Я пізно встав.",
"J'ai fait les courses aujourd'hui.":"Сьогодні я зробив покупки.",
"J'ai regardé la télévision hier.":"Учора я дивився телевізор.",
"L'autobus est déjà parti.":"Автобус уже поїхав.",
"J'ai rangé ma chambre.":"Я прибрав у своїй кімнаті.",
"J'ai enlevé mes chaussures.":"Я зняв взуття.",
"J'ai arrêté le travail.":"Я припинив роботу.",
"Elle est partie sans un mot.":"Вона пішла без жодного слова.",
"Elle a ouvert la lettre tout de suite.":"Вона одразу відкрила листа.",
"Il a vite fermé la valise.":"Він швидко закрив валізу.",
"Je t'ai apporté un gâteau.":"Я приніс тобі тістечко.",
"Je l'ai signalé.":"Я про це повідомив.",
"Je suis monté dans le train.":"Я сів у потяг.",
"Nous avons fabriqué l'appareil.":"Ми виготовили пристрій.",
"Je suis descendu du bus.":"Я вийшов з автобуса.",
"Le conducteur s'est arrêté immédiatement.":"Водій одразу зупинився.",
"Je l'ai invitée à la fête.":"Я запросив її на свято.",
"Nous avons continué le projet.":"Ми продовжили проєкт.",
"Je l'ai finalement découvert.":"Зрештою я це з'ясував.",
"J'ai constaté une différence.":"Я помітив різницю.",
"Il a présenté le nouveau projet hier.":"Учора він представив новий проєкт.",
"Elle l'a seulement suggéré.":"Вона лише натякнула на це.",
"Le pont s'est effondré.":"Міст обвалився.",
"Ils ont mis en œuvre le plan.":"Вони втілили план.",
"J'ai suivi le conseil.":"Я послухався поради.",
"L'avion a atterri.":"Літак приземлився.",
"Un nouveau projet est né.":"Народився новий проєкт.",
"Le livre est paru la semaine dernière.":"Книжка вийшла минулого тижня.",
"Elle a sauté du plongeoir dans l'eau.":"Вона стрибнула з вишки у воду.",
"Sa grand-mère est morte l'an dernier.":"Його бабуся померла торік.",
"Les enfants ont joué au foot.":"Діти грали у футбол.",
"Le gâteau m'a plu.":"Тістечко мені смакувало.",
"J'ai compté l'argent deux fois.":"Я двічі перерахував гроші.",
"J'ai déjà eu deux cafés.":"Я вже випив дві кави.",
"Il a fumé pendant vingt ans.":"Він курив двадцять років.",
"J'ai cuisiné des pâtes hier soir.":"Учора ввечері я зварив макарони.",
"Nous avons fêté son anniversaire.":"Ми святкували його день народження.",
"J'ai déjà fait ma valise.":"Я вже спакував валізу.",
"Nous avons longtemps regardé la mer.":"Ми довго дивилися на море.",
"J'ai posé le livre sur la table.":"Я поклав книжку на стіл.",
}

# ---------- generation ----------
def main():
    d = json.load(io.open(os.path.join(RACINE, "exercices.json"), encoding="utf-8"))
    liste = d["jeux"]["perfektExercises"]
    entrees, rates = [], []
    for e in liste:
        fr, h, x = e["translation"], e.get("hint", ""), e["explanation"]
        tran = T.get(fr)
        if not tran:
            rates.append("PHRASE SANS TRADUCTION : " + fr); continue

        mh = re.match(r"^\((.+?) — (.+?)\)$", h or "")
        expl = None
        if "Verbe faible régulier" in x:
            v, p = re.search(r"pas\. (\S+) → (\S+)\.", x).groups(); expl = m_faible(v, p)
        elif "-d ou -t" in x:
            v, p = re.search(r": (\S+) → (\S+)\.", x).groups(); expl = m_faible_dt(v, p)
        elif "-m ou -n" in x:
            v, p = re.search(r": (\S+) → (\S+)\.", x).groups(); expl = m_faible_mn(v, p)
        elif "Verbe fort" in x:
            v, p = re.search(r"-en\. (\S+) → (\S+)\.", x).groups()
            f = re.search(r"pas (\S+)\.", x).group(1); expl = m_fort(v, p, f)
        elif "-ieren ne prennent" in x:
            v, p = re.search(r": (\S+) → (\S+),", x).groups()
            f = re.search(r"pas (\S+)\.", x).group(1); expl = m_ieren(v, p, f)
        elif "Préfixe inséparable" in x:
            v, p = re.search(r"ge-\. (\S+) → (\S+),", x).groups()
            f = re.search(r"pas (\S+)\.", x).group(1); expl = m_insep(v, p, f)
        elif "particule séparable" in x:
            v, p = re.search(r"radical\. (\S+) → (\S+),", x).groups()
            f = re.search(r"non (\S+)\.", x).group(1); expl = m_sep(v, p, f)
        elif "sein sans exprimer" in x:
            expl = m_bleiben(re.search(r"« (.+?) »", x).group(1))
        elif "exprime un déplacement" in x:
            expl = m_sein(re.search(r"« (.+?) »", x).group(1))
        elif "n'exprime ni déplacement" in x:
            expl = m_haben(re.search(r"« (.+?) »", x).group(1))
        if expl is None:
            rates.append("EXPLICATION HORS MOULE : " + x[:70]); continue

        if h == "(haben ou sein ?)":
            hint = H_HABEN_SEIN
        elif mh and mh.group(2) in TYPES:
            hint = h_type(mh.group(1), TYPES[mh.group(2)])
        else:
            rates.append("INDICE HORS MOULE : " + str(h)); continue

        ent = {"question": e["question"], "translation_uk": tran,
               "hint_uk": hint, "explanation_uk": expl}
        # La question se repete d'un exercice a l'autre dans ce jeu.
        ent["cle_translation"] = fr
        entrees.append(ent)

    if rates:
        print("REFUS D'ECRIRE : %d cas hors moule." % len(rates))
        for r in rates[:12]: print("   " + r)
        return 1
    io.open(SORTIE, "w", encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": "perfektExercises", "entrees": entrees}, ensure_ascii=False, indent=1) + "\n")
    print("exos_perfekt.json : %d entrees, les 8 moules ont couvert tout le jeu." % len(entrees))
    return 0

sys.exit(main())
