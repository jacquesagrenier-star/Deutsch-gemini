# -*- coding: utf-8 -*-
"""Ecrit scenes/02-beim-buergeramt.json.

⚠️ LES CHAMPS DE DOCUMENTATION SONT COPIES DE L'EPISODE 1, PAS REECRITS.
   _format, _balises et la fiche des locuteurs recurrents disent des choses
   arretees pour toute la serie. Les reformuler, c'est creer deux versions
   d'une meme regle et se garantir qu'elles divergeront.
"""
import collections
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

un = json.load(io.open(os.path.join("scenes", "01-ankunft-berlin.json"), encoding="utf-8"),
               object_pairs_hook=collections.OrderedDict)

P = []


def decor(n, image, de, fr, en, tr, uk, fa, balise, duree=5):
    P.append(collections.OrderedDict([
        ("n", n), ("type", "decor"), ("locuteur", "erzaehler"), ("duree", duree),
        ("image", image), ("de", de), ("fr", fr), ("en", en), ("tr", tr),
        ("uk", uk), ("fa", fa), ("balise", balise)]))


def dit(n, qui, de, fr, en, tr, uk, fa, balise, duree=4):
    P.append(collections.OrderedDict([
        ("n", n), ("type", "replique"), ("locuteur", qui), ("duree", duree),
        ("de", de), ("fr", fr), ("en", en), ("tr", tr), ("uk", uk), ("fa", fa),
        ("balise", balise)]))


# ===================== ACTE 1 : IL ARRIVE =====================
decor(1, "buergeramt_aussen.jpg",
      "Ein Amt in Berlin. Montagmorgen, kurz vor neun.",
      "Un bureau administratif à Berlin. Lundi matin, juste avant neuf heures.",
      "A government office in Berlin. Monday morning, just before nine.",
      "Berlin'de bir resmî daire. Pazartesi sabahı, dokuza az kala.",
      "Установа в Берліні. Понеділок, ранок, майже дев'ята.",
      "یک اداره در برلین. صبح دوشنبه، کمی مانده به ساعت نه.",
      "[calm]")

decor(2, "buergeramt_wartezimmer.jpg",
      "Mark muss sich anmelden. In Deutschland ist das Pflicht.",
      "Mark doit déclarer son domicile. En Allemagne, c'est obligatoire.",
      "Mark has to register his address. In Germany, that is mandatory.",
      "Mark'ın adres kaydı yaptırması gerekiyor. Almanya'da bu zorunlu.",
      "Марк мусить зареєструвати місце проживання. У Німеччині це обов'язок.",
      "مارک باید نشانی‌اش را ثبت کند. در آلمان این کار الزامی است.",
      "[calm]")

dit(3, "mark",
    "Guten Tag. Ich möchte mich anmelden.",
    "Bonjour. Je voudrais déclarer mon domicile.",
    "Hello. I would like to register my address.",
    "İyi günler. Adres kaydı yaptırmak istiyorum.",
    "Доброго дня. Я хотів би зареєструвати місце проживання.",
    "روز بخیر. می‌خواهم نشانی‌ام را ثبت کنم.",
    "[politely]")

dit(4, "beamtin",
    "Guten Tag. Haben Sie einen Termin?",
    "Bonjour. Vous avez un rendez-vous ?",
    "Hello. Do you have an appointment?",
    "İyi günler. Randevunuz var mı?",
    "Доброго дня. У вас є запис?",
    "روز بخیر. وقت قبلی دارید؟",
    "[neutral]")

dit(5, "mark",
    "Nein. Kann ich heute einen bekommen?",
    "Non. Est-ce que je peux en avoir un aujourd'hui ?",
    "No. Can I get one today?",
    "Hayır. Bugün alabilir miyim?",
    "Ні. Чи можу я отримати його сьогодні?",
    "نه. می‌توانم امروز یکی بگیرم؟",
    "[hopeful]")

# ===================== ACTE 2 : LE CHIFFRE =====================
decor(6, "buergeramt_bildschirm.jpg",
      "Die Frau schaut auf den Bildschirm. Es dauert einen Moment.",
      "L'employée regarde l'écran. Ça prend un moment.",
      "The clerk looks at the screen. It takes a moment.",
      "Görevli ekrana bakıyor. Bir an sürüyor.",
      "Працівниця дивиться на екран. Це триває якусь мить.",
      "کارمند به صفحه نگاه می‌کند. کمی طول می‌کشد.",
      "[calm]")

dit(7, "beamtin",
    "Der erste freie Termin ist in sechs Wochen.",
    "Le premier rendez-vous libre est dans six semaines.",
    "The first available appointment is in six weeks.",
    "İlk boş randevu altı hafta sonra.",
    "Найближчий вільний запис — через шість тижнів.",
    "نخستین وقت خالی، شش هفتهٔ دیگر است.",
    "[matter-of-fact]")

dit(8, "mark",
    "Sechs Wochen? Ich wohne doch schon hier.",
    "Six semaines ? Mais j'habite déjà ici.",
    "Six weeks? But I already live here.",
    "Altı hafta mı? Ama ben zaten burada oturuyorum.",
    "Шість тижнів? Але ж я вже тут живу.",
    "شش هفته؟ ولی من همین حالا اینجا زندگی می‌کنم.",
    "[surprised]")

dit(9, "beamtin",
    "Sie haben vierzehn Tage Zeit für die Anmeldung.",
    "Vous avez quatorze jours pour faire la déclaration.",
    "You have fourteen days to register.",
    "Kayıt için on dört gününüz var.",
    "На реєстрацію у вас чотирнадцять днів.",
    "برای ثبت‌نام چهارده روز وقت دارید.",
    "[matter-of-fact]")

dit(10, "mark",
    "Vierzehn Tage. Und der Termin ist in sechs Wochen.",
    "Quatorze jours. Et le rendez-vous est dans six semaines.",
    "Fourteen days. And the appointment is in six weeks.",
    "On dört gün. Ve randevu altı hafta sonra.",
    "Чотирнадцять днів. А запис — через шість тижнів.",
    "چهارده روز. و وقت، شش هفتهٔ دیگر.",
    "[flat]")

# ⚠️ LE TRAIT D'HUMOUR, ET SA LIMITE. Il est de SITUATION, pas de mots : le
# spectateur voit deux nombres qui ne vont pas ensemble et un visage qui n'y
# peut rien. Celui qui n'a jamais mis les pieds dans un Buergeramt trouve ca
# etrange ; celui qui y est alle rit. LES DEUX COMPRENNENT LA PHRASE -- c'est
# la seule forme d'humour admissible a ce niveau (voir _incarnation).
dit(11, "beamtin",
    "Ja. Das ist bei uns so.",
    "Oui. C'est comme ça chez nous.",
    "Yes. That is how it works here.",
    "Evet. Bizde böyle.",
    "Так. У нас це так.",
    "بله. اینجا همین‌طور است.",
    "[dry, gone almost before it appears]")

# ===================== ACTE 3 : LE FORMULAIRE =====================
decor(12, "buergeramt_formular.jpg",
      "Sie nimmt ein Blatt aus der Schublade.",
      "Elle sort une feuille du tiroir.",
      "She takes a sheet out of the drawer.",
      "Çekmeceden bir kâğıt çıkarıyor.",
      "Вона дістає аркуш із шухляди.",
      "او برگه‌ای از کشو بیرون می‌آورد.",
      "[calm]")

dit(13, "beamtin",
    "Hier ist das Formular. Füllen Sie es zu Hause aus.",
    "Voici le formulaire. Remplissez-le à la maison.",
    "Here is the form. Fill it in at home.",
    "İşte form. Evde doldurun.",
    "Ось формуляр. Заповніть його вдома.",
    "این فرم است. آن را در خانه پر کنید.",
    "[helpful]")

dit(14, "mark",
    "Welche Papiere brauche ich?",
    "De quels papiers ai-je besoin ?",
    "Which documents do I need?",
    "Hangi belgelere ihtiyacım var?",
    "Які документи мені потрібні?",
    "به چه مدارکی نیاز دارم؟",
    "[politely]")

dit(15, "beamtin",
    "Ihren Pass und die Wohnungsgeberbestätigung.",
    "Votre passeport et l'attestation du bailleur.",
    "Your passport and the landlord's confirmation.",
    "Pasaportunuz ve ev sahibi onay belgesi.",
    "Ваш паспорт і підтвердження від власника житла.",
    "گذرنامه‌تان و تأییدیهٔ صاحبخانه.",
    "[matter-of-fact]")

# ⚠️ LE MOT DE VINGT-SEPT LETTRES, ET C'EST LE PLAN QUI VOYAGE.
# Personne n'a besoin de comprendre l'allemand pour comprendre ce plan : un mot
# trop long, un visage qui decroche, une demande de repetition. C'est le meme
# ressort que le chiffre -- visible sans les mots.
dit(16, "mark",
    "Die … was, bitte?",
    "La… quoi, pardon ?",
    "The… what, sorry?",
    "Ne… efendim?",
    "Під… що, перепрошую?",
    "چی… ببخشید؟",
    "[lost, then trying again]")

dit(17, "beamtin",
    "Ein Papier von Ihrem Vermieter. Das ist ganz normal.",
    "Un papier de votre propriétaire. C'est tout à fait normal.",
    "A paper from your landlord. That is completely normal.",
    "Ev sahibinizden bir belge. Bu gayet normal.",
    "Папір від вашого орендодавця. Це цілком звично.",
    "کاغذی از صاحبخانه‌تان. کاملاً عادی است.",
    "[warm, explains rather than instructs]")

# ===================== ACTE 4 : LA CHUTE =====================
decor(18, "buergeramt_ausgang.jpg",
      "Mark geht mit einem Blatt Papier nach draußen.",
      "Mark sort avec une feuille de papier.",
      "Mark walks out with one sheet of paper.",
      "Mark elinde bir kâğıtla dışarı çıkıyor.",
      "Марк виходить з аркушем паперу.",
      "مارک با یک برگه کاغذ بیرون می‌رود.",
      "[calm]")

# ⚠️ LA CHUTE REBOUCLE SUR LE CHIFFRE. C'est le moteur 03 : on ouvre sur un
# nombre, on ferme dessus. Entre les deux, l'episode n'a fait que l'expliquer.
decor(19, "buergeramt_strasse.jpg",
      "Vierzehn Tage für die Anmeldung. Sechs Wochen bis zum Termin.",
      "Quatorze jours pour la déclaration. Six semaines jusqu'au rendez-vous.",
      "Fourteen days to register. Six weeks until the appointment.",
      "Kayıt için on dört gün. Randevuya altı hafta.",
      "Чотирнадцять днів на реєстрацію. Шість тижнів до запису.",
      "چهارده روز برای ثبت‌نام. شش هفته تا وقت ملاقات.",
      "[calm]", duree=6)

# --------------------------------------------------------------------------
# LE LEXIQUE : uniquement des mots QUI SONT DEJA DES CARTES. Verifie contre les
# huit fichiers de vocabulaire -- pas trois, c'est l'erreur que le docstring de
# tests/lexique.py raconte, et que j'ai refaite ce matin.
LEX = collections.OrderedDict([
    ("Amt",         ("das Amt", "die Ämter", "l'administration", "government office", "daire", "установа", "اداره")),
    ("Bürgeramt",   ("das Bürgeramt", "die Bürgerämter", "le bureau des citoyens", "citizens' office", "vatandaş bürosu", "бюро для громадян", "ادارهٔ شهروندان")),
    ("Anmeldung",   ("die Anmeldung", "die Anmeldungen", "la déclaration de domicile", "registration", "kayıt", "реєстрація", "ثبت‌نام")),
    ("anmelden",    ("sich anmelden", "— (verbe)", "déclarer son domicile", "to register", "kayıt yaptırmak", "реєструватися", "ثبت‌نام کردن")),
    ("Termin",      ("der Termin", "die Termine", "le rendez-vous", "appointment", "randevu", "запис", "وقت ملاقات")),
    ("Formular",    ("das Formular", "die Formulare", "le formulaire", "form", "form", "формуляр", "فرم")),
    ("ausfüllen",   ("ausfüllen", "— (verbe)", "remplir", "to fill in", "doldurmak", "заповнювати", "پر کردن")),
    ("Papier",      ("das Papier", "die Papiere", "le papier, le document", "paper, document", "kâğıt, belge", "папір, документ", "کاغذ، مدرک")),
    ("Pass",        ("der Pass", "die Pässe", "le passeport", "passport", "pasaport", "паспорт", "گذرنامه")),
    ("Vermieter",   ("der Vermieter", "die Vermieter", "le propriétaire bailleur", "landlord", "ev sahibi", "орендодавець", "صاحبخانه")),
    ("Blatt",       ("das Blatt", "die Blätter", "la feuille", "sheet", "yaprak, kâğıt", "аркуш", "برگه")),
    ("Woche",       ("die Woche", "die Wochen", "la semaine", "week", "hafta", "тиждень", "هفته")),
    ("Pflicht",     ("die Pflicht", "die Pflichten", "l'obligation", "duty, obligation", "zorunluluk", "обов'язок", "وظیفه")),
    ("frei",        ("frei", "— (adjectif)", "libre", "free, available", "boş", "вільний", "آزاد")),
    ("brauchen",    ("brauchen", "— (verbe)", "avoir besoin de", "to need", "ihtiyaç duymak", "потребувати", "نیاز داشتن")),
    ("wohnen",      ("wohnen", "— (verbe)", "habiter", "to live, to reside", "oturmak", "мешкати", "زندگی کردن")),
])
lexique = collections.OrderedDict()
for cle, (lemme, pl, fr, en, tr, uk, fa) in LEX.items():
    lexique[cle] = collections.OrderedDict([
        ("lemme", lemme), ("pluriel", pl), ("fr", fr), ("en", en),
        ("tr", tr), ("uk", uk), ("fa", fa)])

loc = collections.OrderedDict()
loc["erzaehler"] = un["locuteurs"]["erzaehler"]
loc["mark"] = un["locuteurs"]["mark"]
# ⚠️ ETAGE 2 : la fonctionnaire ne va PAS dans personnages.json. Elle n'apparait
# qu'une fois, donc elle n'a besoin d'aucun ancrage, d'aucune image maitresse et
# d'aucune voix dediee. C'est aussi realiste : dans la vraie vie on ne tombe
# jamais deux fois sur le meme employe.
loc["beamtin"] = collections.OrderedDict([
    ("nom", "Die Beamtin"),
    ("avatar", None),
    ("voix", "aurora"),
    ("_etage", "2 -- figure d'un seul episode. Aucun ancrage, aucune fiche "
               "dans personnages.json. Elle vouvoie, et Mark la vouvoie : "
               "c'est l'allemand des demarches, celui que testent le DTZ, "
               "le A2 et le B1."),
])

scene = collections.OrderedDict([
    ("_format", un["_format"]),
    ("id", "beim_buergeramt"),
    ("episode", 2),
    ("serie", "Mark in Berlin"),
    ("situation", "Beim Bürgeramt"),
    ("titre", collections.OrderedDict([
        ("fr", "Au Bürgeramt"), ("en", "At the registration office"),
        ("tr", "Vatandaş bürosunda"), ("uk", "У бюро для громадян"),
        ("fa", "در ادارهٔ شهروندان")])),
    ("niveau", "A2"),
    ("theme", "stadt_gebaeude"),
    ("duree", 84),
    ("chronometrage", "absent"),
    ("vitrine", collections.OrderedDict([
        ("moteur", "03 -- le chiffre"),
        ("accroche", "« Sechs Wochen. » plein cadre a zero seconde, puis "
                     "l'episode entier explique le nombre."),
        ("plans", [7, 8, 9, 10, 11, 16, 17]),
        ("_note", "Le montage vitrine ouvre sur le plan 7 et se referme sur le "
                  "19, qui redit les deux nombres. Voir PROCEDURE-episode.md, "
                  "etape 8."),
    ])),
    ("demarche", collections.OrderedDict([
        ("delai_legal_jours", 14),
        ("premier_creneau_semaines", 6),
        ("papiers", ["Pass", "Wohnungsgeberbestätigung", "Formular"]),
    ])),
    ("locuteurs", loc),
    ("plans", P),
    ("lexique", lexique),
    ("_balises", un["_balises"]),
])

dst = os.path.join("scenes", "02-beim-buergeramt.json")
io.open(dst, "w", encoding="utf-8", newline="\n").write(
    json.dumps(scene, ensure_ascii=False, indent=1) + "\n")
print("  %s   %d plans (%d repliques, %d decors), %d mots au lexique"
      % (dst, len(P),
         sum(1 for p in P if p["type"] == "replique"),
         sum(1 for p in P if p["type"] == "decor"),
         len(lexique)))
