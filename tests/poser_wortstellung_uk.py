# -*- coding: utf-8 -*-
"""wortstellungSub (50) et wortstellungTekamolo (30), par moules."""
import io, json, os, re, sys

RACINE = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
CORR = os.path.join(RACINE, "corrections_uk")
d = json.load(io.open(os.path.join(RACINE, "exercices.json"), encoding="utf-8"))

def ecrire(nom, jeu, entrees):
    io.open(os.path.join(CORR, nom), "w", encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": jeu, "entrees": entrees}, ensure_ascii=False, indent=1) + "\n")
    print("%-34s %3d entrees" % (nom, len(entrees)))

# ================= wortstellungSub =================
T1 = {
"Je vais me coucher tôt parce que je suis fatigué(e).":"Я рано лягаю спати, бо я втомлений.",
"Tu souris beaucoup parce que tu es heureux/heureuse.":"Ти багато усміхаєшся, бо ти щасливий.",
"Il reste au lit parce qu'il est malade.":"Він лишається в ліжку, бо він хворий.",
"Elle mange maintenant parce qu'elle a faim.":"Вона зараз їсть, бо вона голодна.",
"Nous n'avons pas de temps parce que nous sommes occupés.":"Ми не маємо часу, бо ми зайняті.",
"Vous parlez peu parce que vous êtes tristes.":"Ви мало говорите, бо ви сумні.",
"Ils tremblent parce qu'ils sont nerveux.":"Вони тремтять, бо вони нервові.",
"Je ris souvent parce que je suis satisfait(e).":"Я часто сміюся, бо я задоволений.",
"Tu bâilles parce que tu es fatigué(e).":"Ти позіхаєш, бо ти втомлений.",
"Nous avons froid parce qu'il fait froid.":"Нам холодно, бо надворі холодно.",
"Ma mère dit que je suis fatigué(e).":"Моя мама каже, що я втомлений.",
"Je vois que tu es heureux/heureuse.":"Я бачу, що ти щасливий.",
"Elle sait qu'il est malade.":"Вона знає, що він хворий.",
"Je crois qu'elle a faim.":"Я думаю, що вона голодна.",
"Il comprend que nous sommes occupés.":"Він розуміє, що ми зайняті.",
"Je remarque que vous êtes tristes.":"Я помічаю, що ви сумні.",
"Le professeur voit qu'ils sont nerveux.":"Учитель бачить, що вони нервові.",
"Tu sais que je suis satisfait(e).":"Ти знаєш, що я задоволений.",
"Je crois que tu es fatigué(e).":"Я думаю, що ти втомлений.",
"Je pense qu'il fait froid.":"Я думаю, що надворі холодно.",
"Je bois du café quand je suis fatigué(e).":"Я п'ю каву, коли я втомлений.",
"Tu chantes quand tu es heureux/heureuse.":"Ти співаєш, коли ти щасливий.",
"Il reste à la maison quand il est malade.":"Він лишається вдома, коли він хворий.",
"Elle cuisine quand elle a faim.":"Вона готує, коли вона голодна.",
"Nous ne répondons pas quand nous sommes occupés.":"Ми не відповідаємо, коли ми зайняті.",
"Vous pleurez quand vous êtes tristes.":"Ви плачете, коли ви сумні.",
"Ils se taisent quand ils sont nerveux.":"Вони мовчать, коли вони нервові.",
"Je souris quand je suis satisfait(e).":"Я усміхаюся, коли я задоволений.",
"Tu vas dormir quand tu es fatigué(e).":"Ти йдеш спати, коли ти втомлений.",
"Nous restons à l'intérieur quand il fait froid.":"Ми лишаємося всередині, коли надворі холодно.",
"Je continue à travailler bien que je sois fatigué(e).":"Я працюю далі, хоча я втомлений.",
"Tu te plains bien que tu sois heureux/heureuse.":"Ти скаржишся, хоча ти щасливий.",
"Il va au travail bien qu'il soit malade.":"Він іде на роботу, хоча він хворий.",
"Elle ne mange rien bien qu'elle ait faim.":"Вона нічого не їсть, хоча вона голодна.",
"Nous t'aidons bien que nous soyons occupés.":"Ми тобі допомагаємо, хоча ми зайняті.",
"Vous riez bien que vous soyez tristes.":"Ви смієтеся, хоча ви сумні.",
"Ils continuent à jouer bien qu'ils soient nerveux.":"Вони грають далі, хоча вони нервові.",
"Je cherche un nouvel emploi bien que je sois satisfait(e).":"Я шукаю нову роботу, хоча я задоволений.",
"Tu danses bien que tu sois fatigué(e).":"Ти танцюєш, хоча ти втомлений.",
"Nous nageons bien qu'il fasse froid.":"Ми плаваємо, хоча надворі холодно.",
"Je fais une pause puisque je suis fatigué(e).":"Я роблю перерву, оскільки я втомлений.",
"Tout le monde est content puisque tu es heureux/heureuse.":"Усі раді, оскільки ти щасливий.",
"Il ne travaille pas puisqu'il est malade.":"Він не працює, оскільки він хворий.",
"Nous mangeons maintenant puisqu'elle a faim.":"Ми зараз їмо, оскільки вона голодна.",
"Personne ne nous dérange puisque nous sommes occupés.":"Ніхто нас не турбує, оскільки ми зайняті.",
"Nous restons avec vous puisque vous êtes tristes.":"Ми лишаємося з вами, оскільки ви сумні.",
"Nous parlons calmement puisqu'ils sont nerveux.":"Ми говоримо спокійно, оскільки вони нервові.",
"Je n'ai besoin de rien puisque je suis satisfait(e).":"Мені нічого не треба, оскільки я задоволений.",
"Nous arrêtons puisque tu es fatigué(e).":"Ми зупиняємося, оскільки ти втомлений.",
"Nous faisons un feu puisqu'il fait froid.":"Ми розпалюємо вогонь, оскільки надворі холодно.",
}

entrees, rates = [], []
for e in d["jeux"]["wortstellungSubExercises"]:
    fr, x, h = e["translation"], e["explanation"], e.get("hint", "")
    if fr not in T1: rates.append("PHRASE : " + fr); continue
    m = re.match(r"^Après « (\w+) », le verbe conjugué \((\w+)\) va à la fin\.$", x)
    if m:
        expl = "Після « %s » дієвідмінюване дієслово (%s) іде в кінець." % m.groups()
    elif re.match(r"^Après « (\w+) », le verbe conjugué va (?:aussi )?à la toute fin de la proposition\.$", x):
        c = re.match(r"^Après « (\w+) »", x).group(1)
        aussi = "так само " if "aussi" in x else ""
        expl = "Після « %s » дієвідмінюване дієслово %sіде в самий кінець підрядного речення." % (c, aussi)
    elif x.startswith("« da » (puisque) suit la même règle"):
        expl = ("« da » (оскільки) підпорядковується тому самому правилу: дієвідмінюване "
                "дієслово іде в самий кінець підрядного речення.")
    else:
        rates.append("EXPL : " + x); continue
    mh = re.match(r"^\(après « (\w+) »\)$", h)
    if not mh: rates.append("INDICE : " + h); continue
    entrees.append({"question": e["question"], "translation_uk": T1[fr],
                    "hint_uk": "(після « %s »)" % mh.group(1), "explanation_uk": expl})
if rates:
    print("REFUS wortstellungSub : %d" % len(rates))
    for r in rates[:8]: print("   " + r)
    sys.exit(1)
ecrire("exos_wortstellungSub.json", "wortstellungSubExercises", entrees)

# ================= wortstellungTekamolo =================
TYPE = {"temporel": "темпоральне", "causal": "каузальне",
        "modal": "модальне", "local": "локальне"}
GLOSE = {"quand": "коли", "pourquoi": "чому", "lieu": "місце",
         "comment": "як", "où": "де"}
T2 = {
"Je pars demain à cause des vacances à Berlin.":"Я їду завтра через канікули до Берліна.",
"Nous voyageons en été à cause du mariage en Italie.":"Ми їдемо влітку через весілля до Італії.",
"Il reste aujourd'hui à cause du temps à la maison.":"Він лишається сьогодні через погоду вдома.",
"Elle vient lundi à cause de l'examen à l'université.":"Вона приходить у понеділок через іспит до університету.",
"Je vais chaque jour par habitude à la salle de sport.":"Я ходжу щодня за звичкою до спортзалу.",
"Je pars demain en train à Berlin.":"Я їду завтра потягом до Берліна.",
"Nous allons aujourd'hui à pied en ville.":"Ми йдемо сьогодні пішки до міста.",
"Il arrive à huit heures en voiture.":"Він приїжджає о восьмій годині автомобілем.",
"Elle voyage la semaine prochaine avec des amis en Espagne.":"Вона їде наступного тижня з друзями до Іспанії.",
"Je cours chaque matin rapidement au travail.":"Я біжу щоранку швидко на роботу.",
"Je pars demain à Berlin.":"Я їду завтра до Берліна.",
"Nous allons aujourd'hui au cinéma.":"Ми йдемо сьогодні в кіно.",
"Il vient lundi à l'école.":"Він приходить у понеділок до школи.",
"Elle voyage en été en Italie.":"Вона їде влітку до Італії.",
"Je vais chaque jour au travail.":"Я ходжу щодня на роботу.",
"Je pars à cause des vacances en train.":"Я їду через канікули потягом.",
"Il voyage pour le travail en avion.":"Він їде через роботу літаком.",
"Nous marchons par curiosité lentement à travers la ville.":"Ми йдемо з цікавості повільно через місто.",
"Elle vient à cause du temps à pied.":"Вона приходить через погоду пішки.",
"J'aide par amour volontiers.":"Я допомагаю з любові охоче.",
"Je pars à cause des vacances à Berlin.":"Я їду через канікули до Берліна.",
"Il voyage pour le travail à Munich.":"Він їде через роботу до Мюнхена.",
"Nous allons par curiosité au musée.":"Ми йдемо з цікавості до музею.",
"Elle vient à cause de l'examen à l'université.":"Вона приходить через іспит до університету.",
"Je m'envole à cause du mariage en Italie.":"Я лечу через весілля до Італії.",
"Je pars en train à Berlin.":"Я їду потягом до Берліна.",
"Nous allons à pied au cinéma.":"Ми йдемо пішки в кіно.",
"Il vient en voiture au travail.":"Він приїжджає автомобілем на роботу.",
"Elle voyage avec des amis en Espagne.":"Вона їде з друзями до Іспанії.",
"Je cours rapidement à la maison.":"Я біжу швидко додому.",
}

entrees, rates = [], []
for e in d["jeux"]["wortstellungTekamoloExercises"]:
    fr, x = e["translation"], e["explanation"]
    m = re.match(r"^(.*?) — Qu'est-ce qui vient en premier : « (.+?) » \((\w+)\) ou « (.+?) » \((\w+)\) \?$", fr)
    if not m: rates.append("PHRASE HORS MOULE : " + fr[:60]); continue
    phrase, a, ta, b, tb = m.groups()
    if phrase not in T2: rates.append("PHRASE : " + phrase); continue
    if ta not in TYPE or tb not in TYPE: rates.append("TYPE : " + ta + "/" + tb); continue
    tran = "%s — Що йде першим: « %s » (%s) чи « %s » (%s)?" % (
        T2[phrase], a, TYPE[ta], b, TYPE[tb])

    m2 = re.match(r"^Le (\w+) vient toujours avant le (\w+) dans l'ordre TeKaMoLo\.$", x)
    m3 = re.match(r"^Le (\w+) vient toujours avant le (\w+) \((\w+)\) dans l'ordre TeKaMoLo\.$", x)
    m4 = re.match(r"^Le (\w+) \((\w+)\) vient toujours avant le (\w+) \((\w+)\) dans l'ordre TeKaMoLo\.$", x)
    m5 = re.match(r"^Selon l'ordre TeKaMoLo, le (\w+) \((\w+)\) vient toujours avant le (\w+) \((\w+)\)\.$", x)
    if m2:
        expl = "У порядку TeKaMoLo %s завжди йде перед %s." % (TYPE[m2.group(1)], TYPE[m2.group(2)])
    elif m3:
        expl = "У порядку TeKaMoLo %s завжди йде перед %s (%s)." % (
            TYPE[m3.group(1)], TYPE[m3.group(2)], GLOSE[m3.group(3)])
    elif m4:
        expl = "У порядку TeKaMoLo %s (%s) завжди йде перед %s (%s)." % (
            TYPE[m4.group(1)], GLOSE[m4.group(2)], TYPE[m4.group(3)], GLOSE[m4.group(4)])
    elif m5:
        expl = "За порядком TeKaMoLo %s (%s) завжди йде перед %s (%s)." % (
            TYPE[m5.group(1)], GLOSE[m5.group(2)], TYPE[m5.group(3)], GLOSE[m5.group(4)])
    else:
        rates.append("EXPL : " + x); continue
    entrees.append({"question": e["question"], "translation_uk": tran,
                    "hint_uk": "(TeKaMoLo: Temporal > Kausal > Modal > Lokal)",
                    "explanation_uk": expl})
if rates:
    print("REFUS Tekamolo : %d" % len(rates))
    for r in rates[:8]: print("   " + r)
    sys.exit(1)
ecrire("exos_tekamolo.json", "wortstellungTekamoloExercises", entrees)
