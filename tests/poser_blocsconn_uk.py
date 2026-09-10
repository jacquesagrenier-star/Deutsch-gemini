# -*- coding: utf-8 -*-
"""blocsConnecteursExercises (120) : le jeu que mes notes annoncaient comme le plus dur.

ET ELLES AVAIENT RAISON SUR LE DIAGNOSTIC, PAS SUR LA METHODE. Il n'y a pas
« un moule » ici : chaque explication est une SUITE DE BLOCS recombines --
« la subordonnee occupe la premiere place... » + « dans la principale au
Perfekt... » + « l'autre ordre est egalement correct... ». Cinquante-quatre
explications distinctes, faites d'une vingtaine de blocs.

On ne traduit donc pas des explications : on traduit des blocs, et on les
recombine dans le meme ordre. Le script CONSOMME la phrase francaise bloc par
bloc depuis le debut ; s'il reste un morceau qu'aucun bloc ne couvre, il
REFUSE et l'affiche. Un bloc oublie ne peut pas se glisser en anglais ou en
francais dans la sortie -- c'est le seul point ou ce jeu pouvait echouer en
silence.

LES 54 PHRASES DEJA TRADUITES NE LE SONT PAS UNE SECONDE FOIS. Elles sont
communes avec ordreInverseExercises, et on va les CHERCHER dans exercices.json
au lieu de les recopier : deux copies d'une meme phrase finissent toujours par
diverger, et personne ne saurait laquelle est la bonne.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

G = r"(« [^»]+ »)"          # un morceau allemand cite, garde tel quel

# ⚠️ L'ORDRE COMPTE : un bloc qui en prefixe un autre doit venir APRES lui.
BLOCS = [
 # --- les ouvertures ---
 (r"Ce connecteur occupe lui-même la première place de la seconde proposition : "
  r"le verbe conjugué le suit aussitôt, et le sujet passe derrière\.",
  "Цей сполучник сам займає перше місце другої частини: відмінюване дієслово "
  "йде одразу за ним, а підмет — після дієслова."),
 (r"La subordonnée occupe la première place : le verbe conjugué de la principale "
  r"la suit immédiatement, et le sujet vient après lui\.",
  "Підрядне речення займає перше місце: відмінюване дієслово головного йде "
  "одразу за ним, а підмет — після дієслова."),
 (r"La subordonnée occupe la première place : le verbe de la principale la suit "
  r"immédiatement, et le sujet vient après lui\.",
  "Підрядне речення займає перше місце: дієслово головного йде одразу за ним, "
  "а підмет — після дієслова."),
 (r"La principale d'abord, la subordonnée après la virgule : dans la subordonnée, "
  r"le verbe conjugué part tout à la fin\.",
  "Спершу головне речення, підрядне — після коми: у підрядному відмінюване "
  "дієслово стає в самий кінець."),
 (G + r", " + G + r" et " + G + r" ne prennent aucune place dans la phrase : "
  r"après la virgule, on repart normalement — sujet, puis verbe\.",
  "%s, %s і %s не займають місця в реченні: після коми все починається як "
  "звичайно — підмет, потім присудок."),
 (G + r" et " + G + r" ne prennent aucune place non plus, et ne demandent pas de "
  r"virgule : la seconde moitié repart sujet, puis verbe\. Quand le sujet est le "
  r"même, on peut même ne pas le répéter — le verbe conjugué suit alors directement\.",
  "%s і %s теж не займають місця і не вимагають коми: друга половина "
  "починається з підмета, потім присудок. Коли підмет той самий, його можна "
  "навіть не повторювати — тоді відмінюване дієслово йде відразу."),
 (G + r" et " + G + r" ne prennent aucune place dans la phrase : après la virgule, "
  r"on repart normalement — sujet, puis verbe\.",
  "%s і %s не займають місця в реченні: після коми все починається як "
  "звичайно — підмет, потім присудок."),
 (G + r" ne prend aucune place : la seconde moitié garde exactement la forme de "
  r"la première\. Ici ce sont deux questions, donc le verbe est en tête des deux côtés\.",
  "%s не займає місця: друга половина зберігає точно таку саму форму, як перша. "
  "Тут це два питання, тож дієслово стоїть на початку з обох боків."),
 # --- les ajouts ---
 (r"Dans la principale au Perfekt, l'auxiliaire tient la deuxième place et le "
  r"participe part à la fin\.",
  "У головному реченні в Perfekt допоміжне дієслово стоїть на другому місці, "
  "а дієприкметник іде в кінець."),
 (r"Dans la subordonnée au passé, l'auxiliaire \(haben/sein\) ferme la marche, "
  r"juste après le participe\.",
  "У підрядному реченні в минулому часі допоміжне дієслово (haben/sein) "
  "замикає ряд, одразу після дієприкметника."),
 (r"Au Futur, " + G + r" tient la place du verbe conjugué et l'infinitif part à la fin\.",
  "У Futur %s посідає місце відмінюваного дієслова, а інфінітив іде в кінець."),
 (r"Et la particule séparable se détache pour aller en fin de proposition\.",
  "А відокремлюваний префікс відділяється й іде в кінець частини."),
 (G + r" ne fait que reprendre cette première place déjà occupée par la "
  r"subordonnée : le verbe reste juste après, il ne bouge pas une seconde fois\.",
  "%s лише підхоплює це перше місце, яке вже зайняте підрядним: дієслово "
  "лишається одразу за ним і вдруге не рухається."),
 (r"L'autre ordre est également correct : la subordonnée passe derrière, et "
  r"l'inversion disparaît — sujet, puis verbe\. → " + G,
  "Інший порядок теж правильний: підрядне переходить назад, і інверсія зникає "
  "— підмет, потім присудок. → %s"),
 (r"L'autre ordre est également correct : la subordonnée passe devant, et le "
  r"verbe de la principale saute alors avant son sujet\. → " + G,
  "Інший порядок теж правильний: підрядне переходить наперед, і тоді дієслово "
  "головного стрибає перед своїм підметом. → %s"),
 # --- les blocs qui ne servent qu'une fois ---
 (r"Dans la subordonnée, le verbe part à la fin \(regnet\)\. Dans la principale, "
  r"il vient juste après la virgule\.",
  "У підрядному дієслово йде в кінець (regnet). У головному воно стоїть "
  "одразу після коми."),
 (r"Verbe à particule : " + G + r" prend sa place après la virgule, " + G +
  r" reste à la fin\.",
  "Дієслово з відокремлюваним префіксом: %s стає після коми, %s лишається в кінці."),
 (r"Même schéma avec " + G + r" : ce n'est pas le sens qui décide de l'ordre, "
  r"c'est la position\.",
  "Та сама схема з %s: порядок визначає не зміст, а позиція."),
 (r"La même phrase retournée : la principale garde son ordre normal \(sujet, "
  r"verbe\), et le verbe de la subordonnée reste à la fin\.",
  "Те саме речення, перевернуте: головне зберігає звичайний порядок (підмет, "
  "присудок), а дієслово підрядного лишається в кінці."),
 (r"Rien ne précède la principale : sujet puis verbe, comme d'habitude\.",
  "Перед головним нічого немає: підмет, потім присудок, як звичайно."),
 (G + r" ouvre une subordonnée : son verbe \(kommt\) va tout à la fin\.",
  "%s відкриває підрядне: його дієслово (kommt) іде в самий кінець."),
 (r"Avec " + G + r", le verbe conjugué \(kann\) passe derrière l'infinitif : "
  r"c'est lui qui ferme la subordonnée\.",
  "З %s відмінюване дієслово (kann) стає позаду інфінітива: саме воно замикає підрядне."),
 (r"Au parfait, l'auxiliaire est le verbe conjugué : il ferme la subordonnée "
  r"\(haben\) et ouvre la principale \(sind\)\.",
  "У Perfekt допоміжне дієслово є відмінюваним: воно замикає підрядне (haben) "
  "і відкриває головне (sind)."),
 (r"Le participe \(gegangen\) reste à la fin de la principale, et le verbe de la "
  r"subordonnée \(war\) à la fin de la sienne\.",
  "Дієприкметник (gegangen) лишається в кінці головного, а дієслово підрядного "
  "(war) — у кінці свого."),
 (r"Deux parfaits : " + G + r" ferme la subordonnée, " + G + r" ouvre la "
  r"principale, et " + G + r" la termine\.",
  "Два Perfekt: %s замикає підрядне, %s відкриває головне, а %s його завершує."),
 (r"Dans la subordonnée au parfait, l'auxiliaire passe DERRIÈRE le participe : "
  r"geregnet hat\.",
  "У підрядному в Perfekt допоміжне дієслово стає ПОЗАДУ дієприкметника: geregnet hat."),
 (r"Même règle à la fin : aufgehört hat, et non hat aufgehört\.",
  "Те саме правило в кінці: aufgehört hat, а не hat aufgehört."),
 (G + r" demande un temps en arrière : plus-que-parfait dans la subordonnée, "
  r"parfait dans la principale\.",
  "%s вимагає кроку назад у часі: Plusquamperfekt у підрядному, Perfekt у головному."),
 (r"Au futur, " + G + r" est le verbe conjugué : il prend la place juste après "
  r"la virgule, l'infinitif reste à la fin\.",
  "У Futur %s є відмінюваним дієсловом: воно стає одразу після коми, а "
  "інфінітив лишається в кінці."),
 (r"La principale garde son ordre normal ; dans la subordonnée, l'auxiliaire "
  r"\(bin\) ferme la phrase\.",
  "Головне зберігає звичайний порядок; у підрядному допоміжне дієслово (bin) "
  "замикає речення."),
 (r"Subordonnée en tête : " + G + r" suit la virgule, et l'infinitif "
  r"\(aufstehen\) ferme la principale\.",
  "Підрядне на початку: %s іде після коми, а інфінітив (aufstehen) замикає головне."),
 (r"Dans la subordonnée au futur, " + G + r" passe derrière l'infinitif : regnen wird\.",
  "У підрядному в Futur %s стає позаду інфінітива: regnen wird."),
 (G + r" ouvre la phrase : verbe de la principale juste après la virgule\.",
  "%s відкриває речення: дієслово головного — одразу після коми."),
 (r"Deux propositions, deux règles : verbe à la fin dans la subordonnée, verbe "
  r"en tête dans la principale\.",
  "Дві частини, два правила: дієслово в кінці підрядного, дієслово на початку головного."),
 (r"La subordonnée est à la fin : la principale garde sujet puis verbe\.",
  "Підрядне стоїть у кінці: головне зберігає підмет, потім присудок."),
 (G + r" est ici une conjonction : elle ouvre une subordonnée, donc verbe à la "
  r"fin \(arbeite\)\.",
  "%s тут сполучник: він відкриває підрядне, тож дієслово йде в кінець (arbeite)."),
 (G + r" ouvre une question indirecte : c'est une subordonnée, le verbe va à la fin\.",
  "%s відкриває непряме питання: це підрядне, тож дієслово йде в кінець."),
 (r"Subordonnée en tête au prétérit, principale au parfait : l'auxiliaire "
  r"\(habe\) suit la virgule, le participe ferme la phrase\.",
  "Підрядне на початку в Präteritum, головне в Perfekt: допоміжне дієслово "
  "(habe) іде після коми, а дієприкметник замикає речення."),
]
BLOCS = [(re.compile(f), uk) for f, uk in BLOCS]

# Quatre indices sur six sont deja poses : ce sont des noms de temps allemands
# (« (Präsens) »), rien a traduire. Les deux autres portent une phrase, et
# c'est pour eux que trente-six exercices restaient a faire -- un jeu peut
# etre traduit a 100 % de ses explications et rester « a faire » sur un mot.
INDICES = {
 "(Perfekt — haben/sein et le participe sont deux blocs)":
     "(Perfekt — haben/sein і дієприкметник — два окремі блоки)",
 "(Futur — werden et l'infinitif sont deux blocs)":
     "(Futur — werden і інфінітив — два окремі блоки)",
}

# Les 66 phrases qui ne sont pas deja dans ordreInverseExercises.
T = {
"Je parle allemand tous les jours depuis que j'habite à Berlin.":
    "Я щодня розмовляю німецькою, відколи живу в Берліні.",
"Nous restons à la maison parce qu'il pleut aujourd'hui.":
    "Ми залишаємося вдома, бо сьогодні йде дощ.",
"J'attends ici jusqu'à ce que le train arrive.": "Я чекаю тут, доки не приїде потяг.",
"Elle apprend l'allemand pour pouvoir étudier à Vienne.":
    "Вона вчить німецьку, щоб могти навчатися у Відні.",
"Je suis allé me coucher tôt parce que j'étais fatigué.":
    "Я рано ліг спати, бо був утомлений.",
"Nous avons attendu jusqu'à ce que la pluie s'arrête.":
    "Ми чекали, доки дощ не припинився.",
"Je t'appellerai dès que je serai arrivé.": "Я зателефоную тобі, щойно приїду.",
"Nous resterons à la maison parce qu'il va pleuvoir.":
    "Ми залишимося вдома, бо буде дощ.",
"Il prend le bus bien qu'il ait une voiture.": "Він їздить автобусом, хоча має машину.",
"Je ne sais pas s'il vient aujourd'hui.": "Я не знаю, чи він сьогодні прийде.",
"Je ne sais pas s'il a reçu la lettre.": "Я не знаю, чи він отримав листа.",
"Il pleut, donc je reste à la maison.": "Іде дощ, тому я залишаюся вдома.",
"Il est fatigué, pourtant il continue à travailler.":
    "Він утомлений, проте працює далі.",
"Je n'ai pas le temps, donc je viens plus tard.":
    "У мене немає часу, тому я прийду пізніше.",
"Le temps est mauvais, pourtant nous allons à la mer.":
    "Погода погана, проте ми їдемо на море.",
"D'abord je range, ensuite je t'appelle.": "Спершу я прибираю, потім телефоную тобі.",
"J'apprends tous les jours, mais je fais encore beaucoup de fautes.":
    "Я вчуся щодня, але ще роблю багато помилок.",
"Nous n'y allons pas en voiture, mais nous prenons le train.":
    "Ми їдемо не машиною, а потягом.",
"Elle dit qu'elle n'a pas le temps demain.": "Вона каже, що завтра не має часу.",
"Il a plu très fort, de sorte que nous sommes restés à la maison.":
    "Ішов сильний дощ, так що ми залишилися вдома.",
"Il parle très bas, de sorte que je le comprends à peine.":
    "Він говорить дуже тихо, так що я його ледве розумію.",
"Le train était plein, de sorte que nous avons dû rester debout.":
    "Потяг був повний, так що нам довелося стояти.",
"Appelle-moi au cas où tu aurais besoin d'aide.":
    "Зателефонуй мені, якщо раптом тобі знадобиться допомога.",
"Je crois qu'il vient demain.": "Я думаю, що він завтра прийде.",
"Je suis content que tu sois venu.": "Я радий, що ти прийшов.",
"Elle a dit qu'elle venait plus tard.": "Вона сказала, що прийде пізніше.",
"Je fais la cuisine et tu mets la table.": "Я готую їжу, а ти накриваєш на стіл.",
"Nous sommes allés au cinéma et nous avons vu un film.":
    "Ми пішли в кіно і подивилися фільм.",
"Il se lève tôt et va courir.": "Він рано встає і йде бігати.",
"Tu viens avec nous ou tu restes ici ?": "Ти йдеш із нами чи залишаєшся тут?",
"Nous allons au cinéma ou nous restons à la maison.":
    "Ми йдемо в кіно або залишаємося вдома.",
"Veux-tu du thé ou préfères-tu du café ?": "Ти хочеш чаю чи волієш каву?",
"Je reste à la maison, car je suis malade.": "Я залишаюся вдома, бо я хворий.",
"Nous devons nous dépêcher, car le train part tout de suite.":
    "Нам треба поспішати, бо потяг зараз вирушає.",
"Elle a bien dormi, car elle était très fatiguée.":
    "Вона добре спала, бо була дуже втомлена.",
"J'ai peu de temps, mais je t'aide volontiers.":
    "У мене мало часу, але я охоче тобі допоможу.",
"La chambre est petite, mais elle est très claire.":
    "Кімната маленька, але дуже світла.",
"Je ne viens pas aujourd'hui, mais demain.": "Я прийду не сьогодні, а завтра.",
"Elle n'est pas fatiguée, mais malade.": "Вона не втомлена, а хвора.",
"Le bus était plein, c'est pourquoi j'y suis allé à pied.":
    "Автобус був повний, тому я пішов пішки.",
"J'ai trop dormi, c'est pourquoi j'arrive en retard.": "Я проспав, тому запізнююся.",
"Il fait froid, c'est pourquoi je m'habille chaudement.":
    "Холодно, тому я тепло вдягаюся.",
"Je n'ai pas faim, c'est pourquoi je ne mange rien.":
    "Я не голодний, тому нічого не їм.",
"L'exercice était difficile, néanmoins nous l'avons résolu.":
    "Завдання було важке, проте ми його розв'язали.",
"Il a peu étudié, néanmoins il a réussi.": "Він мало вчився, проте склав іспит.",
"L'appartement est bon marché, en plus il est central.":
    "Квартира недорога, до того ж розташована в центрі.",
"Je n'ai pas le temps, en plus je suis fatigué.":
    "У мене немає часу, до того ж я втомлений.",
"D'abord je prends le petit-déjeuner, ensuite je vais au travail.":
    "Спершу я снідаю, потім іду на роботу.",
"Quand tu as fini, alors je t'appelle.": "Коли ти закінчиш, тоді я тобі зателефоную.",
"Nous mangeons d'abord, ensuite nous regardons un film.":
    "Ми спершу їмо, потім дивимося фільм.",
"Le magasin est fermé, donc nous allons ailleurs.":
    "Крамниця зачинена, отже, ми йдемо в інше місце.",
"Il pleut, donc nous prenons le parapluie.": "Іде дощ, отже, ми беремо парасольку.",
"Nous mangeons à huit heures, avant cela nous faisons une promenade.":
    "Ми їмо о восьмій, перед тим гуляємо.",
"Je vais dormir, avant cela je me brosse les dents.":
    "Я йду спати, перед тим чищу зуби.",
"Le film commence à huit heures, avant cela nous nous retrouvons au café.":
    "Фільм починається о восьмій, перед тим ми зустрічаємося в кафе.",
"J'ai rangé, ensuite je me suis reposé.": "Я прибрав, потім відпочив.",
"Nous allons faire les courses, ensuite nous cuisinons ensemble.":
    "Ми йдемо по покупки, потім разом готуємо.",
"Avant de partir, éteins la lumière s'il te plaît.":
    "Перш ніж підеш, вимкни, будь ласка, світло.",
"Elle demande si nous avons le temps demain.":
    "Вона питає, чи маємо ми завтра час.",
"J'ai oublié ma clé, c'est pourquoi j'attends dehors.":
    "Я забув ключ, тому чекаю надворі.",
"Elle a de la fièvre, c'est pourquoi elle reste au lit.":
    "У неї температура, тому вона лишається в ліжку.",
"Le café était trop fort, c'est pourquoi je n'ai pas pu dormir.":
    "Кава була надто міцна, тому я не міг заснути.",
"J'avais peu de temps, pourtant j'ai tout réussi à faire.":
    "У мене було мало часу, проте я все встиг.",
"Le temps était mauvais, néanmoins nous avons fait de la randonnée.":
    "Погода була погана, проте ми ходили в похід.",
"Le cours est intéressant, en plus je fais la connaissance de beaucoup de gens.":
    "Курс цікавий, до того ж я знайомлюся з багатьма людьми.",
"J'ai tout compris, donc je n'ai pas besoin d'aide.":
    "Я все зрозумів, отже, мені не потрібна допомога.",
}


def traduire_explication(x):
    """Consomme la phrase francaise bloc par bloc. None des qu'un reste."""
    reste, sortie = x, []
    while reste:
        for motif, uk in BLOCS:
            m = motif.match(reste)
            # Un bloc doit finir la chaine ou etre suivi d'une espace : sans
            # cette verification, un bloc court validerait un bloc plus long
            # qui commence pareil, et la fin partirait en francais.
            if m and (m.end() == len(reste) or reste[m.end()] == " "):
                sortie.append(uk % m.groups() if m.groups() else uk)
                reste = reste[m.end():].lstrip(" ")
                break
        else:
            return None, reste
    return " ".join(sortie), ""


def main():
    d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
    # Les phrases communes avec ordreInverse, prises a la source.
    commun = {e["translation"]: e.get("translation_uk", "")
              for e in d["jeux"]["ordreInverseExercises"]}
    entrees, rates = [], []
    for e in d["jeux"]["blocsConnecteursExercises"]:
        q, x = e["question"], e["explanation"]
        uk_q = T.get(q) or commun.get(q)
        if not uk_q:
            rates.append("PHRASE : " + q)
            continue
        uk_x, reste = traduire_explication(x)
        if not uk_x:
            rates.append("BLOC INCONNU : " + reste[:110])
            continue
        entree = {"question": q, "question_uk": uk_q, "explanation_uk": uk_x}
        h = e.get("hint", "")
        if h in INDICES:
            entree["hint_uk"] = INDICES[h]
        entrees.append(entree)
    if rates:
        print("REFUS : %d" % len(rates))
        vus = set()
        for r in rates:
            if r[:60] not in vus:
                vus.add(r[:60])
                print("   " + r)
        sys.exit(1)
    io.open(os.path.join(R, "corrections_uk", "exos_blocsConnecteurs.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": "blocsConnecteursExercises", "entrees": entrees},
                   ensure_ascii=False, indent=1) + "\n")
    print("exos_blocsConnecteurs.json : %d entrees" % len(entrees))


if __name__ == "__main__":
    main()
