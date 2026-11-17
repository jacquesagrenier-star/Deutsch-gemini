# -*- coding: utf-8 -*-
"""La meteo dans les langues d'interface sans phrase traduite jusqu'ici (lot 12, 16 nov. 2026) : turc, ukrainien,
polonais, russe, persan et arabe pour qui apprend l'allemand, et l'arabe pour qui apprend l'espagnol.

Ecrites pour chaque langue, pas calquees sur le francais : « Мені холодно » / « Jest mi zimno » / « سردم است » pour
« Mir ist kalt », le temps qu'il fait sans sujet en ukrainien et en russe (« Холодно. »), « hava » en turc. Les degres
s'accordent au nombre (1 градус, 2 градуси, 5 градусів ; 2 stopnie, 5 stopni). En persan, « ماه مه » et jamais « مه »
seul : c'est aussi le brouillard. Appele par meteo.py (ecrire_json) ; les points douteux : retours/A-RELIRE-THEMES-<LG>.md.
"""

LANGUES = ("tr", "uk", "pl", "ru", "fa", "ar")

# la phrase allemande -> (tr, uk, pl, ru, fa, ar)
DE = {
    "Die Sonne scheint.": ("Güneş parlıyor.", "Світить сонце.", "Świeci słońce.", "Светит солнце.", "خورشید می‌درخشد.", "الشمس مشرقة."),
    "Es ist sonnig.": ("Hava güneşli.", "Сонячно.", "Jest słonecznie.", "Солнечно.", "هوا آفتابی است.", "الجو مشمس."),
    "Es ist heiß.": ("Hava çok sıcak.", "Спекотно.", "Jest gorąco.", "Жарко.", "هوا خیلی گرم است.", "الجو حارّ جدًا."),
    "Es ist kalt.": ("Hava soğuk.", "Холодно.", "Jest zimno.", "Холодно.", "هوا سرد است.", "الجو بارد."),
    "Es ist kühl.": ("Hava serin.", "Прохолодно.", "Jest chłodno.", "Прохладно.", "هوا خنک است.", "الجو منعش."),
    "Es regnet.": ("Yağmur yağıyor.", "Іде дощ.", "Pada deszcz.", "Идёт дождь.", "باران می‌بارد.", "السماء تمطر."),
    "Es schneit.": ("Kar yağıyor.", "Іде сніг.", "Pada śnieg.", "Идёт снег.", "برف می‌بارد.", "الثلج يتساقط."),
    "Es ist bewölkt.": ("Hava bulutlu.", "Хмарно.", "Jest pochmurno.", "Облачно.", "هوا ابری است.", "الجو غائم."),
    "Es ist windig.": ("Hava rüzgârlı.", "Вітряно.", "Jest wietrznie.", "Ветрено.", "باد می‌وزد.", "الرياح تهبّ."),
    "Es ist neblig.": ("Hava sisli.", "Туманно.", "Jest mglisto.", "Туманно.", "هوا مه‌آلود است.", "هناك ضباب."),
    "Es gibt ein Gewitter.": ("Gök gürültülü fırtına var.", "Іде гроза.", "Jest burza.", "Идёт гроза.", "رعد و برق می‌زند.", "هناك عاصفة رعدية."),
    "Das Wetter ist schön.": ("Hava güzel.", "Гарна погода.", "Pogoda jest ładna.", "Хорошая погода.", "هوا خوب است.", "الطقس جميل."),
    "Das Wetter ist schlecht.": ("Hava kötü.", "Погана погода.", "Pogoda jest brzydka.", "Плохая погода.", "هوا بد است.", "الطقس سيئ."),
    "Im Frühling geht Anna mit Ben und Mia im Park spazieren.": (
        "İlkbaharda Anna, Ben ve Mia ile parkta yürüyüş yapıyor.", "Навесні Анна гуляє з Беном і Мією в парку.",
        "Wiosną Anna spaceruje z Benem i Mią po parku.", "Весной Анна гуляет с Беном и Мией в парке.",
        "در بهار، آنا با بن و میا در پارک قدم می‌زند.", "في الربيع، تتنزّه آنا في الحديقة مع بن وميا."),
    "Im Sommer schwimmt Anna im See.": ("Yazın Anna gölde yüzüyor.", "Улітку Анна плаває в озері.", "Latem Anna pływa w jeziorze.",
                                        "Летом Анна плавает в озере.", "در تابستان، آنا در دریاچه شنا می‌کند.", "في الصيف، تسبح آنا في البحيرة."),
    "Im Sommer essen Ben und Mia Eis.": ("Yazın Ben ve Mia dondurma yiyorlar.", "Улітку Бен і Мія їдять морозиво.", "Latem Ben i Mia jedzą lody.",
                                         "Летом Бен и Мия едят мороженое.", "در تابستان، بن و میا بستنی می‌خورند.", "في الصيف، يأكل بن وميا المثلّجات."),
    "Im Herbst sammeln Ben und Mia Blätter im Wald.": (
        "Sonbaharda Ben ve Mia ormanda yaprak topluyorlar.", "Восени Бен і Мія збирають листя в лісі.",
        "Jesienią Ben i Mia zbierają liście w lesie.", "Осенью Бен и Мия собирают листья в лесу.",
        "در پاییز، بن و میا در جنگل برگ جمع می‌کنند.", "في الخريف، يجمع بن وميا أوراق الشجر في الغابة."),
    "Im Winter spielen Ben und Mia im Schnee.": ("Kışın Ben ve Mia karda oynuyorlar.", "Узимку Бен і Мія граються в снігу.",
                                                 "Zimą Ben i Mia bawią się na śniegu.", "Зимой Бен и Мия играют в снегу.",
                                                 "در زمستان، بن و میا در برف بازی می‌کنند.", "في الشتاء، يلعب بن وميا في الثلج."),
    "Wenn es regnet, liest Anna mit Mia ein Buch.": (
        "Yağmur yağınca Anna, Mia ile kitap okuyor.", "Коли йде дощ, Анна читає з Мією книжку.",
        "Kiedy pada deszcz, Anna czyta z Mią książkę.", "Когда идёт дождь, Анна читает с Мией книгу.",
        "وقتی باران می‌بارد، آنا با میا کتاب می‌خواند.", "عندما تمطر، تقرأ آنا كتابًا مع ميا."),
    "Heute gibt es viel Regen.": ("Bugün çok yağmur var.", "Сьогодні сильний дощ.", "Dziś dużo pada.", "Сегодня сильный дождь.",
                                  "امروز باران زیادی می‌بارد.", "اليوم مطر غزير."),
    "Auf dem Platz liegt viel Schnee.": ("Meydanda çok kar var.", "На площі багато снігу.", "Na placu leży dużo śniegu.", "На площади много снега.",
                                         "در میدان برف زیادی هست.", "في الساحة ثلج كثير."),
    "Am Himmel sind viele Wolken.": ("Gökyüzünde çok bulut var.", "На небі багато хмар.", "Na niebie jest dużo chmur.", "На небе много облаков.",
                                     "در آسمان ابرهای زیادی هست.", "في السماء غيوم كثيرة."),
    "Der Wind ist sehr stark.": ("Rüzgâr çok kuvvetli.", "Вітер дуже сильний.", "Wiatr jest bardzo silny.", "Ветер очень сильный.",
                                 "باد خیلی شدید است.", "الريح قوية جدًا."),
    "Heute gibt es viel Nebel.": ("Bugün çok sis var.", "Сьогодні густий туман.", "Dziś jest gęsta mgła.", "Сегодня густой туман.",
                                  "امروز هوا خیلی مه‌آلود است.", "اليوم ضباب كثيف."),
    "Mir ist kalt.": ("Üşüyorum.", "Мені холодно.", "Jest mi zimno.", "Мне холодно.", "سردم است.", "أشعر بالبرد."),
    "Mir ist heiß.": ("Sıcakladım.", "Мені жарко.", "Jest mi gorąco.", "Мне жарко.", "گرمم است.", "أشعر بالحرّ."),
    "Heute regnet es.": ("Bugün yağmur yağıyor.", "Сьогодні йде дощ.", "Dziś pada deszcz.", "Сегодня идёт дождь.", "امروز باران می‌بارد.", "اليوم تمطر."),
    "Heute schneit es.": ("Bugün kar yağıyor.", "Сьогодні йде сніг.", "Dziś pada śnieg.", "Сегодня идёт снег.", "امروز برف می‌بارد.", "اليوم يتساقط الثلج."),
    "Heute ist es kalt.": ("Bugün hava soğuk.", "Сьогодні холодно.", "Dziś jest zimno.", "Сегодня холодно.", "امروز هوا سرد است.", "الجو بارد اليوم."),
    "Heute ist es heiß.": ("Bugün hava çok sıcak.", "Сьогодні спекотно.", "Dziś jest gorąco.", "Сегодня жарко.", "امروز هوا خیلی گرم است.", "الجو حارّ جدًا اليوم."),
    "Heute ist es windig.": ("Bugün hava rüzgârlı.", "Сьогодні вітряно.", "Dziś jest wietrznie.", "Сегодня ветрено.", "امروز باد می‌وزد.", "الرياح تهبّ اليوم."),
    "Heute ist es neblig.": ("Bugün hava sisli.", "Сьогодні туманно.", "Dziś jest mglisto.", "Сегодня туманно.", "امروز هوا مه‌آلود است.", "هناك ضباب اليوم."),
    "Heute gibt es ein Gewitter.": ("Bugün gök gürültülü fırtına var.", "Сьогодні гроза.", "Dziś jest burza.", "Сегодня гроза.",
                                    "امروز رعد و برق می‌زند.", "هناك عاصفة رعدية اليوم."),
    "Im Winter ist es kalt.": ("Kışın hava soğuk.", "Узимку холодно.", "Zimą jest zimno.", "Зимой холодно.", "در زمستان هوا سرد است.",
                               "في الشتاء يكون الجو باردًا."),
    "Im Sommer ist es heiß.": ("Yazın hava çok sıcak.", "Улітку спекотно.", "Latem jest gorąco.", "Летом жарко.", "در تابستان هوا خیلی گرم است.",
                               "في الصيف يكون الجو حارًّا جدًا."),
    "Es ist warm.": ("Hava ılık.", "Тепло.", "Jest ciepło.", "Тепло.", "هوا گرم است.", "الجو دافئ."),
    "Es ist Frühling.": ("Mevsim ilkbahar.", "Зараз весна.", "Jest wiosna.", "Сейчас весна.", "بهار است.", "نحن في الربيع."),
    "Es ist Sommer.": ("Mevsim yaz.", "Зараз літо.", "Jest lato.", "Сейчас лето.", "تابستان است.", "نحن في الصيف."),
    "Es ist Herbst.": ("Mevsim sonbahar.", "Зараз осінь.", "Jest jesień.", "Сейчас осень.", "پاییز است.", "نحن في الخريف."),
    "Es ist Winter.": ("Mevsim kış.", "Зараз зима.", "Jest zima.", "Сейчас зима.", "زمستان است.", "نحن في الشتاء."),
}

# la phrase espagnole -> l'arabe (pour qui apprend l'espagnol) ; « Hace sol » et « Hace calor » ne disent pas la meme
# chose que « Die Sonne scheint » et « Es ist heiß » (le francais : « il y a du soleil », « il fait chaud »)
ES_AR = {
    "Hace sol.": "هناك شمس.", "Está soleado.": "الجو مشمس.", "Hace calor.": "الجو حارّ.", "Hace frío.": "الجو بارد.",
    "Hace fresco.": "الجو منعش.", "Llueve.": "السماء تمطر.", "Nieva.": "الثلج يتساقط.", "Está nublado.": "الجو غائم.",
    "Hace viento.": "الرياح تهبّ.", "Hay niebla.": "هناك ضباب.", "Hay tormenta.": "هناك عاصفة.",
    "Hace buen tiempo.": "الطقس جميل.", "Hace mal tiempo.": "الطقس سيئ.",
    "En primavera, Anna pasea por el parque con Ben y Mia.": "في الربيع، تتنزّه آنا في الحديقة مع بن وميا.",
    "En verano, Anna nada en el lago.": "في الصيف، تسبح آنا في البحيرة.",
    "En verano, Ben y Mia comen helado.": "في الصيف، يأكل بن وميا المثلّجات.",
    "En otoño, Ben y Mia recogen hojas en el bosque.": "في الخريف، يجمع بن وميا أوراق الشجر في الغابة.",
    "En invierno, Ben y Mia juegan en la nieve.": "في الشتاء، يلعب بن وميا في الثلج.",
    "Cuando llueve, Anna lee un libro con Mia.": "عندما تمطر، تقرأ آنا كتابًا مع ميا.",
    "Hoy llueve mucho.": "اليوم تمطر كثيرًا.", "La lluvia no para.": "المطر لا يتوقف.", "Hoy nieva.": "اليوم يتساقط الثلج.",
    "Hay mucha nieve en la plaza.": "في الساحة ثلج كثير.", "Hace mucho sol.": "الشمس ساطعة جدًا.",
    "Es un día soleado.": "إنه يوم مشمس.", "El cielo está nublado.": "السماء غائمة.",
    "Hay muchas nubes en el cielo.": "في السماء غيوم كثيرة.", "Hace mucho viento.": "هناك رياح قوية.",
    "Tengo frío.": "أشعر بالبرد.", "Tengo calor.": "أشعر بالحرّ.",
    "Es primavera.": "نحن في الربيع.", "Es verano.": "نحن في الصيف.", "Es otoño.": "نحن في الخريف.", "Es invierno.": "نحن في الشتاء.",
}

# LES MOIS (le mois allemand -> sa forme dans chaque langue) et LES SAISONS (cle de meteo.py)
MOIS = {
    "tr": {"Januar": "Ocak", "Februar": "Şubat", "April": "Nisan", "Mai": "Mayıs", "Juli": "Temmuz", "August": "Ağustos",
           "Oktober": "Ekim", "November": "Kasım"},
    # le locatif : « у січні », « в январе », « w styczniu »
    "uk": {"Januar": "У січні", "Februar": "У лютому", "April": "У квітні", "Mai": "У травні", "Juli": "У липні", "August": "У серпні",
           "Oktober": "У жовтні", "November": "У листопаді"},
    "pl": {"Januar": "W styczniu", "Februar": "W lutym", "April": "W kwietniu", "Mai": "W maju", "Juli": "W lipcu", "August": "W sierpniu",
           "Oktober": "W październiku", "November": "W listopadzie"},
    "ru": {"Januar": "В январе", "Februar": "В феврале", "April": "В апреле", "Mai": "В мае", "Juli": "В июле", "August": "В августе",
           "Oktober": "В октябре", "November": "В ноябре"},
    "fa": {"Januar": "ژانویه", "Februar": "فوریه", "April": "آوریل", "Mai": "مه", "Juli": "ژوئیه", "August": "اوت",
           "Oktober": "اکتبر", "November": "نوامبر"},
    "ar": {"Januar": "يناير", "Februar": "فبراير", "April": "أبريل", "Mai": "مايو", "Juli": "يوليو", "August": "أغسطس",
           "Oktober": "أكتوبر", "November": "نوفمبر"},
}
SAISONS = {
    "tr": {"primavera": "ilkbahar", "verano": "yaz", "otono": "sonbahar", "invierno": "kış"},
    "uk": {"primavera": "весна", "verano": "літо", "otono": "осінь", "invierno": "зима"},
    "pl": {"primavera": "wiosna", "verano": "lato", "otono": "jesień", "invierno": "zima"},
    "ru": {"primavera": "весна", "verano": "лето", "otono": "осень", "invierno": "зима"},
    "fa": {"primavera": "بهار", "verano": "تابستان", "otono": "پاییز", "invierno": "زمستان"},
    "ar": {"primavera": "الربيع", "verano": "الصيف", "otono": "الخريف", "invierno": "الشتاء"},
}


def mois_de(lg, m_de, s):
    """« Im Januar ist in Deutschland Winter. »"""
    m, sa = MOIS[lg][m_de], SAISONS[lg][s]
    return {"tr": "%s ayında Almanya'da %s olur." % (m, sa),
            "uk": "%s в Німеччині %s." % (m, sa),
            "pl": "%s w Niemczech jest %s." % (m, sa),
            "ru": "%s в Германии %s." % (m, sa),
            "fa": "در ماه %s، در آلمان %s است." % (m, sa),
            "ar": "في شهر %s، يكون %s في ألمانيا." % (m, sa)}[lg]


def mois_es_ar(m_de, s):
    """« En España, en enero es invierno. » et « En España, enero es un mes de invierno. », en arabe."""
    m, sa = MOIS["ar"][m_de], SAISONS["ar"][s]
    return ("في إسبانيا، يكون %s في شهر %s." % (sa, m), "في إسبانيا، %s شهر من أشهر %s." % (m, sa))


def _uk_ru(n, un, deux, cinq):
    n = abs(n)
    if n % 10 == 1 and n % 100 != 11:
        return un
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return deux
    return cinq


def degres(lg, t):
    """« Es sind minus zwölf Grad. » : le chiffre, comme la phrase francaise (« Il fait moins 12 degrés. »)."""
    a, moins = abs(t), t < 0
    if lg == "tr":
        return "Hava %s%d derece." % ("eksi " if moins else "", a)
    if lg == "uk":
        return "Зараз %s%d %s." % ("мінус " if moins else "", a, _uk_ru(a, "градус", "градуси", "градусів"))
    if lg == "ru":
        return "Сейчас %s%d %s." % ("минус " if moins else "", a, _uk_ru(a, "градус", "градуса", "градусов"))
    if lg == "pl":
        mot = "stopień" if a == 1 else ("stopnie" if 2 <= a % 10 <= 4 and not 12 <= a % 100 <= 14 else "stopni")
        return "Jest %s%d %s." % ("minus " if moins else "", a, mot)
    if lg == "fa":
        return "دما %s%d درجه است." % ("منفی " if moins else "", a)
    if lg == "ar":
        return "درجة الحرارة %d%s." % (a, " تحت الصفر" if moins else "")
    raise KeyError(lg)


# ce que veut dire le mauvais choix du ressenti (meteo.py, CHOIX_RESSENTI)
_PAS_ALLEMAND = {"tr": "Almancada böyle söylenmez: Fransızcadan kelimesi kelimesine çeviri",
                 "uk": "так німецькою не кажуть: це дослівний переклад із французької",
                 "pl": "tak się nie mówi po niemiecku: to dosłowne tłumaczenie z francuskiego",
                 "ru": "так по-немецки не говорят: это дословный перевод с французского",
                 "fa": "در آلمانی این‌طور نمی‌گویند: ترجمهٔ کلمه‌به‌کلمه از فرانسوی است",
                 "ar": "لا يُقال هكذا بالألمانية: إنها ترجمة حرفية من الفرنسية"}
CHOIX = {
    "Ich bin kalt.": {"tr": "dokununca soğuğum, ya da soğuk biriyim",
                      "uk": "моє тіло холодне на дотик, або я холодна людина",
                      "pl": "moje ciało jest zimne w dotyku albo jestem zimną osobą",
                      "ru": "моё тело холодное на ощупь, или я холодный человек",
                      "fa": "بدنم سرد است، یا آدم سردی هستم",
                      "ar": "جسمي بارد عند اللمس، أو أنا شخص بارد"},
    "Ich habe kalt.": _PAS_ALLEMAND, "Ich habe heiß.": _PAS_ALLEMAND, "Es macht kalt.": _PAS_ALLEMAND, "Es macht heiß.": _PAS_ALLEMAND,
    "Soy fría.": {"ar": "أنا شخص بارد (الطبع)"},
    "Soy frío.": {"ar": "أنا شخص بارد (الطبع)"},
}
