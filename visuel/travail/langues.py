# -*- coding: utf-8 -*-
"""Le travail et l'emploi : les phrases traduites en turc, ukrainien, polonais, russe, persan et arabe
(lot 15, 16 nov. 2026), et en arabe pour l'espagnol appris.

La traduction suit le français de la page (le champ « t » de travail.py), pas le mot à mot de la phrase
apprise : l'entretien porte la question ET la réponse, le CV « rubrique = traduction », comme en français.
Les familles de phrases (annonces, qualités, entretien, lettre, CV) sont refaites par la grammaire de chaque
langue à partir de la phrase apprise ; le reste est une table. Une phrase sans traduction arrête travail.py.

Noms : Марк, مارك, مارک comme dans les autres thèmes ; les noms d'entreprise (Sonnenweg Reisen, Viajes Solano)
restent en lettres latines, comme les rues du plan de la ville ; en persan et en arabe la phrase ne commence
jamais par eux (le sens de lecture de la ligne se règle sur la première lettre).
Chiffres occidentaux en persan et en arabe, comme les degrés de la météo.
"""
import re

LANGUES = ("tr", "uk", "pl", "ru", "fa", "ar")


def pour(app):
    """les langues que ce module traduit pour une langue apprise"""
    return list(LANGUES) if app == "de" else ["ar"] if app == "es" else []


# ---------- petits outils ----------
def _pl(n, un, quelques, beaucoup):
    """uk, ru : 1 / 2-4 / 5+ (11-14 : 5+)"""
    if n % 10 == 1 and n % 100 != 11:
        return un
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return quelques
    return beaucoup


def _pol(n, un, quelques, beaucoup):
    """polonais : 1 / 2-4 (sauf 12-14) / le reste"""
    if n == 1:
        return un
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return quelques
    return beaucoup


def _g(s, g):
    """{masculin|féminin} -> la forme du genre"""
    return re.sub(r"\{([^{}|]*)\|([^{}|]*)\}", lambda m: m.group(1) if g == "m" else m.group(2), s)


def _cap(s):
    """majuscule en début de chaque phrase (« пані Шнайдер … » -> « Пані Шнайдер … »)"""
    return re.sub(r"(^|[.!?] )(\w)", lambda m: m.group(1) + m.group(2).upper(), s)


GUILLEMETS = {"tr": ("“", "”"), "uk": ("«", "»"), "ru": ("«", "»"), "pl": ("„", "”"), "fa": ("«", "»"), "ar": ("«", "»")}


def _dialogue(lg, q, r):
    o, f = GUILLEMETS[lg]
    return o + q + f + " — " + o + r + f


def _montant(lg, s):
    """« 3.000 » / « 14,50 » -> l'écriture de la langue ; l'euro en lettres en persan et en arabe"""
    if lg == "tr":
        n = s
    else:
        n = s.replace(".", "")
    return n + (" یورو" if lg == "fa" else " يورو" if lg == "ar" else " €")


MOIS = {"Dezember": "dic", "Januar": "jan", "diciembre": "dic", "enero": "jan"}
MOIS_T = {"dic": {"tr": "Aralık", "uk": "грудня", "ru": "декабря", "pl": "grudnia", "fa": "دسامبر", "ar": "ديسمبر"},
          "jan": {"tr": "Ocak", "uk": "січня", "ru": "января", "pl": "stycznia", "fa": "ژانویه", "ar": "يناير"}}


def _date(lg, j, mois):
    m = MOIS_T[MOIS[mois]][lg]
    if lg == "tr":
        return "%s %s'ta" % (j, m)          # Aralık'ta, Ocak'ta
    return "%s %s" % (j, m)


def _heures(lg, n):
    n = int(n)
    return {"tr": "%d saat" % n, "uk": "%d %s" % (n, _pl(n, "година", "години", "годин")),
            "ru": "%d %s" % (n, _pl(n, "час", "часа", "часов")), "pl": "%d %s" % (n, _pol(n, "godzina", "godziny", "godzin")),
            "fa": "%d ساعت" % n, "ar": "%d %s" % (n, "ساعات" if 3 <= n <= 10 else "ساعة")}[lg]


# ---------- les personnes ----------
# nom : genre, puis la forme de chaque langue (le nominatif ; les autres cas sont écrits dans les phrases fixes)
GENS = {
    "Mark": ("m", {"tr": "Mark", "uk": "Марк", "pl": "Mark", "ru": "Марк", "fa": "مارک", "ar": "مارك"}),
    "Jonas": ("m", {"tr": "Jonas", "uk": "Йонас", "pl": "Jonas", "ru": "Йонас", "fa": "یوناس", "ar": "يوناس"}),
    "Lisa": ("f", {"tr": "Lisa", "uk": "Ліза", "pl": "Lisa", "ru": "Лиза", "fa": "لیزا", "ar": "ليزا"}),
    "Frau Schneider": ("f", {"tr": "Schneider Hanım", "uk": "пані Шнайдер", "pl": "pani Schneider", "ru": "госпожа Шнайдер",
                             "fa": "خانم اشنایدر", "ar": "السيدة شنايدر"}),
    # l'espagnol appris (l'arabe seul)
    "Jorge": ("m", {"ar": "خورخي"}),
    "Lucía": ("f", {"ar": "لوسيا"}),
    "La señora Navarro": ("f", {"ar": "السيدة نافارو"}),
}
# les destinataires des candidatures : (titre, nom) -> langue -> « à … »
DEST = {
    "de": {"Schneider": ("f", "Schneider", "Шнайдер", "Шнайдер", "اشنایدر", "شنايدر"),
           "Lange": ("m", "Lange", "Ланге", "Ланге", "لانگه", "لانغه"),
           "Krause": ("f", "Krause", "Краузе", "Краузе", "کراوزه", "كراوزه"),
           "Wolf": ("m", "Wolf", "Вольф", "Вольф", "ولف", "فولف"),
           "Sommer": ("f", "Sommer", "Зоммер", "Зоммер", "زومر", "زومر"),
           "Brandt": ("m", "Brandt", "Брандт", "Брандт", "برانت", "برانت")},
    "es": {"Navarro": ("f", "نافارو"), "Gil": ("m", "خيل"), "López": ("f", "لوبيز"), "Ruiz": ("m", "رويز"),
           "Vega": ("f", "فيغا"), "Sanz": ("m", "سانز")},
}
# génitif polonais et datif ukrainien / russe des messieurs (les dames ne se déclinent pas)
PL_GEN = {"Lange": "Langego", "Wolf": "Wolfa", "Brandt": "Brandta"}
UK_DAT = {"Ланге": "Ланге", "Вольф": "Вольфу", "Брандт": "Брандту"}
UK_VOC = {"Ланге": "Ланге", "Вольф": "Вольфе", "Брандт": "Брандте"}   # « Шановний пане Вольфе, »


def _a_qui(lg, nom):
    g, tr, uk, ru, fa, ar = DEST["de"][nom]
    if lg == "tr":
        return "%s %s" % (tr, "Hanım'a" if g == "f" else "Bey'e")
    if lg == "uk":
        return "пані %s" % uk if g == "f" else "пану %s" % UK_DAT[uk]
    if lg == "ru":
        return "госпоже %s" % ru if g == "f" else "господину %s" % UK_DAT[ru]
    if lg == "pl":
        return "do pani %s" % nom if g == "f" else "do pana %s" % PL_GEN[nom]
    if lg == "fa":
        return "%s %s" % ("خانم" if g == "f" else "آقای", fa)
    return "%s %s" % ("السيدة" if g == "f" else "السيد", ar)


def _salut(lg, nom, app="de"):
    """« Sehr geehrte Frau Schneider, » -> l'en-tête de lettre de la langue"""
    if app == "es":
        g, ar = DEST["es"][nom]
        return "السيدة %s المحترمة،" % ar if g == "f" else "السيد %s المحترم،" % ar
    g, tr, uk, ru, fa, ar = DEST["de"][nom]
    f = g == "f"
    return {"tr": "Sayın %s %s," % (tr, "Hanım" if f else "Bey"),
            "uk": ("Шановна пані %s," % uk) if f else ("Шановний пане %s," % UK_VOC[uk]),
            "ru": ("Уважаемая госпожа %s," if f else "Уважаемый господин %s,") % ru,
            "pl": "Szanowna Pani," if f else "Szanowny Panie,",
            "fa": ("خانم %s گرامی،" if f else "آقای %s گرامی،") % fa,
            "ar": ("السيدة %s المحترمة،" if f else "السيد %s المحترم،") % ar}[lg]


# ---------- les métiers des annonces ----------
# rôle appris -> langue -> (nominatif « le nouveau … », génitif / complément « le poste de … »)
ROLES = {
    "Mitarbeiter": {"tr": ("çalışan", "müşteri hizmetleri çalışanı"), "uk": ("працівник", "працівника служби підтримки клієнтів"),
                    "ru": ("сотрудник", "сотрудника службы поддержки клиентов"), "pl": ("pracownik", "pracownika obsługi klienta"),
                    "fa": ("کارمند", "کارمند خدمات مشتریان"), "ar": ("الموظف", "موظف خدمة العملاء")},
    "Rezeptionist": {"tr": ("resepsiyonist", "resepsiyonist"), "uk": ("адміністратор", "адміністратора"), "ru": ("администратор", "администратора"),
                     "pl": ("recepcjonista", "recepcjonisty"), "fa": ("متصدی پذیرش", "متصدی پذیرش"), "ar": ("موظف الاستقبال", "موظف استقبال")},
    "Kellner": {"tr": ("garson", "garson"), "uk": ("офіціант", "офіціанта"), "ru": ("официант", "официанта"), "pl": ("kelner", "kelnera"),
                "fa": ("گارسون", "گارسون"), "ar": ("النادل", "نادل")},
    "Koch": {"tr": ("aşçı", "aşçı"), "uk": ("кухар", "кухаря"), "ru": ("повар", "повара"), "pl": ("kucharz", "kucharza"),
             "fa": ("آشپز", "آشپز"), "ar": ("الطباخ", "طباخ")},
    "Verkäufer": {"tr": ("satış elemanı", "satış elemanı"), "uk": ("продавець", "продавця"), "ru": ("продавец", "продавца"),
                  "pl": ("sprzedawca", "sprzedawcy"), "fa": ("فروشنده", "فروشنده"), "ar": ("البائع", "بائع")},
    "Fahrer": {"tr": ("şoför", "şoför"), "uk": ("водій", "водія"), "ru": ("водитель", "водителя"), "pl": ("kierowca", "kierowcy"),
               "fa": ("راننده", "راننده"), "ar": ("السائق", "سائق")},
}
ROLES_ES = {"agente de atención al cliente": "Mitarbeiter", "recepcionista": "Rezeptionist", "camarero": "Kellner",
            "cocinero": "Koch", "dependiente": "Verkäufer", "conductor": "Fahrer"}
# lieu appris -> langue -> « travaille dans … »
LIEUX = {
    "Reisebüro": {"tr": "bir seyahat acentesinde çalışıyor", "uk": "працює в туристичній агенції", "ru": "работает в турагентстве",
                  "pl": "pracuje w biurze podróży", "fa": "در یک آژانس مسافرتی کار می‌کند", "ar": "في وكالة سفر"},
    "Hotel": {"tr": "bir otelde çalışıyor", "uk": "працює в готелі", "ru": "работает в гостинице", "pl": "pracuje w hotelu",
              "fa": "در یک هتل کار می‌کند", "ar": "في فندق"},
    "Café": {"tr": "bir kafede çalışıyor", "uk": "працює в кафе", "ru": "работает в кафе", "pl": "pracuje w kawiarni",
             "fa": "در یک کافه کار می‌کند", "ar": "في مقهى"},
    "Restaurant": {"tr": "bir restoranda çalışıyor", "uk": "працює в ресторані", "ru": "работает в ресторане", "pl": "pracuje w restauracji",
                   "fa": "در یک رستوران کار می‌کند", "ar": "في مطعم"},
    "Bäckerei": {"tr": "bir fırında çalışıyor", "uk": "працює в пекарні", "ru": "работает в пекарне", "pl": "pracuje w piekarni",
                 "fa": "در یک نانوایی کار می‌کند", "ar": "في مخبز"},
    "Apotheke": {"tr": "bir eczane için çalışıyor", "uk": "працює на аптеку", "ru": "работает на аптеку", "pl": "pracuje dla apteki",
                 "fa": "برای یک داروخانه کار می‌کند", "ar": "لدى صيدلية"},
}
LIEUX_ES = {"agencia": "Reisebüro", "hotel": "Hotel", "cafetería": "Café", "restaurante": "Restaurant", "panadería": "Bäckerei",
            "farmacia": "Apotheke"}
# persan : le nom suivi d'un adjectif prend l'ezafe écrit (ـهٔ) quand il finit par un h muet
EZAFE_FA = {"فروشنده": "فروشندهٔ", "راننده": "رانندهٔ"}


def _nouveau(lg, role, lieu):
    r = ROLES[role][lg][0]
    l = LIEUX[lieu][lg]
    if lg == "tr":
        return "Yeni %s %s." % (r, l)
    if lg == "uk":
        return "Новий %s %s." % (r, l)
    if lg == "ru":
        return "Новый %s %s." % (r, l)
    if lg == "pl":
        return "Nowy %s %s." % (r, l)
    if lg == "fa":
        return "%s جدید %s." % (EZAFE_FA.get(r, r), l)
    return "يعمل %s الجديد %s." % (r, l)


# ---------- les qualités ----------
# adjectif appris -> langue -> (la phrase qui le montre, avec {P} ; l'adjectif attribut ; « il faut être … » ; l'adjectif seul, au masculin)
Q_DE = {
    "pünktlich": {
        "tr": ("{P} asla geç kalmaz.", "{P} dakiktir.", "Dakik olmak gerekiyor.", "dakik"),
        "uk": ("{P} ніколи не запізнюється.", "{P} пунктуальн{ий|а}.", "Потрібно бути пунктуальним.", "пунктуальний"),
        "ru": ("{P} никогда не опаздывает.", "{P} пунктуальн{ый|ая}.", "Нужно быть пунктуальным.", "пунктуальный"),
        "pl": ("{P} nigdy się nie spóźnia.", "{P} jest punktualn{y|a}.", "Trzeba być punktualnym.", "punktualny"),
        "fa": ("{P} هیچ‌وقت دیر نمی‌آید.", "{P} وقت‌شناس است.", "باید وقت‌شناس بود.", "وقت‌شناس"),
        "ar": ("{P} لا {ي|ت}تأخر أبدًا.", "{P} دقيق{|ة} في المواعيد.", "يجب أن يكون الموظف دقيقًا في المواعيد.", "دقيق في المواعيد")},
    "zuverlässig": {
        "tr": ("{P} her zaman söz verdiğini yapar.", "{P} güvenilirdir.", "Güvenilir olmak gerekiyor.", "güvenilir"),
        "uk": ("{P} завжди робить те, що обіцяє.", "{P} надійн{ий|а}.", "Потрібно бути надійним.", "надійний"),
        "ru": ("{P} всегда делает то, что обещает.", "{P} надёжн{ый|ая}.", "Нужно быть надёжным.", "надёжный"),
        "pl": ("{P} zawsze robi to, co obiecuje.", "{P} jest rzeteln{y|a}.", "Trzeba być rzetelnym.", "rzetelny"),
        "fa": ("{P} همیشه به قولش عمل می‌کند.", "{P} قابل اعتماد است.", "باید قابل اعتماد بود.", "قابل اعتماد"),
        "ar": ("{P} {ي|ت}في دائمًا بما {ي|ت}عد به.", "{P} جدير{|ة} بالثقة.", "يجب أن يكون الموظف جديرًا بالثقة.", "جدير بالثقة")},
    "freundlich": {
        "tr": ("{P} her zaman gülümser ve müşterileri selamlar.", "{P} cana yakındır.", "Cana yakın olmak gerekiyor.", "cana yakın"),
        "uk": ("{P} завжди усміхається й вітається з клієнтами.", "{P} привітн{ий|а}.", "Потрібно бути привітним.", "привітний"),
        "ru": ("{P} всегда улыбается и здоровается с клиентами.", "{P} приветлив{ый|ая}.", "Нужно быть приветливым.", "приветливый"),
        "pl": ("{P} zawsze się uśmiecha i wita klientów.", "{P} jest uprzejm{y|a}.", "Trzeba być uprzejmym.", "uprzejmy"),
        "fa": ("{P} همیشه لبخند می‌زند و به مشتری‌ها سلام می‌کند.", "{P} خوش‌برخورد است.", "باید خوش‌برخورد بود.", "خوش‌برخورد"),
        "ar": ("{P} {ي|ت}بتسم دائمًا و{ي|ت}حيّي الزبائن.", "{P} ودود{|ة}.", "يجب أن يكون الموظف ودودًا.", "ودود")},
    "flexibel": {
        "tr": ("{P} hafta sonu da çalışabilir.", "{P} esnektir.", "Esnek olmak gerekiyor.", "esnek"),
        "uk": ("{P} може працювати й у вихідні.", "{P} гнучк{ий|а}.", "Потрібно бути гнучким.", "гнучкий"),
        "ru": ("{P} может работать и по выходным.", "{P} гибк{ий|ая}.", "Нужно быть гибким.", "гибкий"),
        "pl": ("{P} może pracować także w weekendy.", "{P} jest elastyczn{y|a}.", "Trzeba być elastycznym.", "elastyczny"),
        "fa": ("{P} آخر هفته‌ها هم می‌تواند کار کند.", "{P} انعطاف‌پذیر است.", "باید انعطاف‌پذیر بود.", "انعطاف‌پذیر"),
        "ar": ("{P} {ي|ت}ستطيع العمل في عطلة نهاية الأسبوع أيضًا.", "{P} مرن{|ة}.", "يجب أن يكون الموظف مرنًا.", "مرن")},
    "fleißig": {
        "tr": ("{P} çok çalışır ve sadece kısa molalar verir.", "{P} çalışkandır.", "Çalışkan olmak gerekiyor.", "çalışkan"),
        "uk": ("{P} багато працює й робить лише короткі перерви.", "{P} старанн{ий|а}.", "Потрібно бути старанним.", "старанний"),
        "ru": ("{P} много работает и делает только короткие перерывы.", "{P} трудолюбив{ый|ая}.", "Нужно быть трудолюбивым.", "трудолюбивый"),
        "pl": ("{P} dużo pracuje i robi tylko krótkie przerwy.", "{P} jest pracowit{y|a}.", "Trzeba być pracowitym.", "pracowity"),
        "fa": ("{P} زیاد کار می‌کند و فقط استراحت‌های کوتاه دارد.", "{P} کوشا است.", "باید کوشا بود.", "کوشا"),
        "ar": ("{P} {ي|ت}عمل كثيرًا ولا {ي|ت}أخذ إلا استراحات قصيرة.", "{P} مجتهد{|ة}.", "يجب أن يكون الموظف مجتهدًا.", "مجتهد")},
    "selbstständig": {
        "tr": ("{P} tek başına, yardım almadan iyi çalışır.", "{P} bağımsızdır.", "Bağımsız çalışabilmek gerekiyor.", "bağımsız"),
        "uk": ("{P} добре працює сам{|а}, без допомоги.", "{P} самостійн{ий|а}.", "Потрібно бути самостійним.", "самостійний"),
        "ru": ("{P} хорошо работает сам{|а}, без помощи.", "{P} самостоятельн{ый|ая}.", "Нужно быть самостоятельным.", "самостоятельный"),
        "pl": ("{P} dobrze pracuje sam{|a}, bez pomocy.", "{P} jest samodzieln{y|a}.", "Trzeba być samodzielnym.", "samodzielny"),
        "fa": ("{P} به‌تنهایی و بدون کمک خوب کار می‌کند.", "{P} مستقل است.", "باید مستقل بود.", "مستقل"),
        "ar": ("{P} {ي|ت}عمل جيدًا وحد{ه|ها}، دون مساعدة.", "{P} مستقل{|ة}.", "يجب أن يكون الموظف مستقلًا.", "مستقل")},
    "ordentlich": {
        "tr": ("{P} her akşam masasını toplar.", "{P} derli topludur.", "Derli toplu olmak gerekiyor.", "derli toplu"),
        "uk": ("{P} щовечора прибирає свій стіл.", "{P} охайн{ий|а}.", "Потрібно бути охайним.", "охайний"),
        "ru": ("{P} каждый вечер убирает свой стол.", "{P} аккуратн{ый|ая}.", "Нужно быть аккуратным.", "аккуратный"),
        "pl": ("{P} co wieczór sprząta swoje biurko.", "{P} jest schludn{y|a}.", "Trzeba być schludnym.", "schludny"),
        "fa": ("{P} هر شب میزش را مرتب می‌کند.", "{P} مرتب است.", "باید مرتب بود.", "مرتب"),
        "ar": ("{P} {ي|ت}رتّب مكتب{ه|ها} كل مساء.", "{P} منظّم{|ة}.", "يجب أن يكون الموظف منظّمًا.", "منظّم")},
    "teamfähig": {
        "tr": ("{P} iş arkadaşlarıyla çalışmayı sever.", "{P} takım çalışmasına yatkındır.", "Takım çalışmasına yatkın olmak gerekiyor.", None),
        "uk": ("{P} любить працювати з колегами.", "{P} уміє працювати в команді.", "Потрібно вміти працювати в команді.", None),
        "ru": ("{P} любит работать с коллегами.", "{P} умеет работать в команде.", "Нужно уметь работать в команде.", None),
        "pl": ("{P} lubi pracować z kolegami.", "{P} potrafi pracować w zespole.", "Trzeba umieć pracować w zespole.", None),
        "fa": ("{P} دوست دارد با همکارانش کار کند.", "{P} اهل کار گروهی است.", "باید اهل کار گروهی بود.", None),
        "ar": ("{P} {ي|ت}حب العمل مع زملائ{ه|ها}.", "{P} قادر{|ة} على العمل ضمن فريق.", "يجب أن يكون الموظف قادرًا على العمل ضمن فريق.", None)},
}
# l'espagnol appris : les qualités de la page espagnole (l'arabe seul)
Q_ES = {
    "puntual": Q_DE["pünktlich"]["ar"],
    "responsable": ("{P} {ي|ت}في دائمًا بوعود{ه|ها}.", "{P} مسؤول{|ة}.", "يجب أن يكون الموظف مسؤولًا.", "مسؤول"),
    "amable": ("{P} {ي|ت}بتسم دائمًا و{ي|ت}حيّي الزبائن.", "{P} لطيف{|ة}.", "يجب أن يكون الموظف لطيفًا.", "لطيف"),
    "flexible": Q_DE["flexibel"]["ar"],
    "trabajador": ("{P} {ي|ت}عمل كثيرًا و{ي|ت}أخذ استراحات قليلة.", "{P} مجتهد{|ة}.", "يجب أن يكون الموظف مجتهدًا.", "مجتهد"),
    "ordenado": Q_DE["ordentlich"]["ar"],
    "independiente": Q_DE["selbstständig"]["ar"],
}
ES_FEM = {"trabajadora": "trabajador", "ordenada": "ordenado"}
# ser / estar : l'état du moment, avec l'arabe
ESTAR_ES = {"enfermo": "مريض{|ة} اليوم", "nervioso": "متوتر{|ة} قبل المقابلة", "contento": "سعيد{|ة} بعمل{ه|ها} الجديد",
            "cansado": "متعب{|ة} بعد ثماني ساعات من العمل"}
ESTAR_FEM = {"enferma": "enfermo", "nerviosa": "nervioso", "contenta": "contento", "cansada": "cansado"}


def _attribut_ar(adj_es, g):
    """« Mark es puntual. » -> l'adjectif arabe accordé (le second membre de Q_ES)"""
    a = Q_ES[ES_FEM.get(adj_es, adj_es)][1]
    return _g(a.replace("{P} ", "").rstrip("."), g)


def _personne(lg, nom, app):
    g, formes = GENS[nom]
    return g, formes[lg]


def _qualite(lg, nom, adj, app):
    g, p = _personne(lg, nom, app)
    if app == "de":
        ctx, attr = Q_DE[adj][lg][0], Q_DE[adj][lg][1]
    else:
        ctx, attr = Q_ES[ES_FEM.get(adj, adj)][0], Q_ES[ES_FEM.get(adj, adj)][1]
    s = _cap((_g(ctx, g) + " " + _g(attr, g)).replace("{P}", p))
    if lg == "uk":   # « у » entre consonnes, « в » après une voyelle : Марк уміє, Ліза вміє
        s = re.sub(r"([аеєиіїоуюя]) уміє", r"\1 вміє", s)
    return s


# ---------- l'entretien (la question puis la réponse, comme en français) ----------
QUESTIONS = {
    "moi": {"tr": "Bize biraz kendinizden bahseder misiniz?", "uk": "Розкажіть, будь ласка, трохи про себе.",
            "ru": "Расскажите, пожалуйста, немного о себе.", "pl": "Proszę powiedzieć coś o sobie.",
            "fa": "لطفاً کمی از خودتان بگویید.", "ar": "حدِّثنا قليلًا عن نفسك."},
    "langues": {"tr": "Hangi dilleri konuşuyorsunuz?", "uk": "Якими мовами ви розмовляєте?", "ru": "На каких языках вы говорите?",
                "pl": "Jakimi językami pan mówi?", "fa": "به چه زبان‌هایی صحبت می‌کنید؟", "ar": "ما اللغات التي تتحدثها؟"},
    "experience": {"tr": "İş deneyiminiz var mı?", "uk": "У вас уже є досвід роботи?", "ru": "У вас уже есть опыт работы?",
                   "pl": "Czy ma pan już doświadczenie zawodowe?", "fa": "سابقهٔ کار دارید؟", "ar": "هل لديك خبرة مهنية؟"},
    "forts": {"tr": "Güçlü yönleriniz nelerdir?", "uk": "Які ваші сильні сторони?", "ru": "Какие у вас сильные стороны?",
              "pl": "Jakie są pana mocne strony?", "fa": "نقاط قوت شما چیست؟", "ar": "ما نقاط قوتك؟"},
    "quand": {"tr": "Ne zaman başlayabilirsiniz?", "uk": "Коли ви можете почати?", "ru": "Когда вы можете начать?",
              "pl": "Kiedy może pan zacząć?", "fa": "از کی می‌توانید شروع کنید؟", "ar": "متى يمكنك أن تبدأ؟"},
    "temps": {"tr": "Tam zamanlı mı yoksa yarı zamanlı mı çalışmak istersiniz?",
              "uk": "Ви хочете працювати повний чи неповний робочий день?",
              "ru": "Вы хотите работать полный или неполный рабочий день?",
              "pl": "Chce pan pracować na pełen etat czy na część etatu?",
              "fa": "می‌خواهید تمام‌وقت کار کنید یا پاره‌وقت؟", "ar": "هل تريد العمل بدوام كامل أم بدوام جزئي؟"},
    "questions": {"tr": "Başka sorunuz var mı?", "uk": "У вас ще є запитання?", "ru": "У вас есть ещё вопросы?",
                  "pl": "Czy ma pan jeszcze jakieś pytania?", "fa": "سؤال دیگری دارید؟", "ar": "هل لديك أسئلة أخرى؟"},
    "pourquoi": {"tr": "Neden bizde çalışmak istiyorsunuz?", "uk": "Чому ви хочете працювати в нас?", "ru": "Почему вы хотите работать у нас?",
                 "pl": "Dlaczego chce pan pracować u nas?", "fa": "چرا می‌خواهید پیش ما کار کنید؟", "ar": "لماذا تريد العمل لدينا؟"},
}
# l'espagnol : deux questions dites autrement par la page française
QUESTIONS_ES = {"experience": "هل لديك خبرة؟", "temps": "هل تفضّل العمل بدوام كامل أم بدوام جزئي؟", "questions": "هل لديك سؤال؟"}


def _forts(lg, a, b, app):
    if app == "de":
        x, y = Q_DE[a][lg][3], Q_DE[b][lg][3]
    else:
        x, y = Q_ES[a][3], Q_ES[b][3]
    r = {"tr": "%s ve %s biriyim." % (x[0].upper() + x[1:], y), "uk": "Я %s і %s." % (x, y), "ru": "Я %s и %s." % (x, y),
         "pl": "Jestem %s i %s." % (x, y), "fa": "من %s و %s هستم." % (x, y), "ar": "أنا %s و%s." % (x, y)}[lg]
    return _dialogue(lg, QUESTIONS["forts"][lg], r)


def _commencer(lg, j, mois, app):
    d = _date(lg, j, mois)
    r = {"tr": "%s başlayabilirim." % d, "uk": "Я можу почати %s." % d, "ru": "Я могу начать %s." % d,
         "pl": "Mogę zacząć %s." % d, "fa": "می‌توانم از %s شروع کنم." % d, "ar": "يمكنني أن أبدأ في %s." % d}[lg]
    return _dialogue(lg, QUESTIONS["quand"][lg], r)


def _temps(lg, plein, app):
    if app == "es":
        return _dialogue(lg, QUESTIONS_ES["temps"], "أفضّل الدوام الكامل." if plein else "أفضّل الدوام الجزئي.")
    r = {"tr": "Tam zamanlı çalışmak isterim." if plein else "Yarı zamanlı çalışmak isterim.",
         "uk": "Я хотів би працювати %s робочий день." % ("повний" if plein else "неповний"),
         "ru": "Я хотел бы работать %s рабочий день." % ("полный" if plein else "неполный"),
         "pl": "Chciałbym pracować %s." % ("na pełen etat" if plein else "na część etatu"),
         "fa": "دوست دارم %s کار کنم." % ("تمام‌وقت" if plein else "پاره‌وقت"),
         "ar": "أودّ العمل بدوام %s." % ("كامل" if plein else "جزئي")}[lg]
    return _dialogue(lg, QUESTIONS["temps"][lg], r)


# ---------- le CV : « rubrique = traduction », comme en français ----------
RUBRIQUES = {
    "Persönliche Daten": {"tr": "Kişisel bilgiler", "uk": "Особисті дані", "ru": "Личные данные", "pl": "Dane osobowe",
                          "fa": "اطلاعات شخصی", "ar": "البيانات الشخصية"},
    "Berufserfahrung": {"tr": "İş deneyimi", "uk": "Досвід роботи", "ru": "Опыт работы", "pl": "Doświadczenie zawodowe",
                        "fa": "سابقهٔ کار", "ar": "الخبرة المهنية"},
    "Ausbildung": {"tr": "Eğitim", "uk": "Освіта", "ru": "Образование", "pl": "Wykształcenie", "fa": "تحصیلات", "ar": "التعليم"},
    "Sprachkenntnisse": {"tr": "Yabancı diller", "uk": "Знання мов", "ru": "Знание языков", "pl": "Znajomość języków",
                         "fa": "مهارت‌های زبانی", "ar": "المهارات اللغوية"},
    "Hobbys": {"tr": "Hobiler", "uk": "Хобі", "ru": "Хобби", "pl": "Zainteresowania", "fa": "سرگرمی‌ها", "ar": "الهوايات"},
}
RUBRIQUES_ES = {"Datos personales": "Persönliche Daten", "Experiencia laboral": "Berufserfahrung", "Formación": "Ausbildung",
                "Idiomas": "Sprachkenntnisse", "Aficiones": "Hobbys"}

# ---------- les phrases fixes, par langue apprise ----------
L = LANGUES


def _t(*v):
    return dict(zip(L, v))


FIXE_DE = {
    # la taille du poste
    "Die Stelle ist in Vollzeit.": _t("Pozisyon tam zamanlı.", "Це робота на повний робочий день.", "To praca na pełen etat.",
                                      "Это работа на полный рабочий день.", "این کار تمام‌وقت است.", "الوظيفة بدوام كامل."),
    "Die Stelle ist in Teilzeit.": _t("Pozisyon yarı zamanlı.", "Це робота на неповний робочий день.", "To praca na część etatu.",
                                      "Это работа на неполный рабочий день.", "این کار پاره‌وقت است.", "الوظيفة بدوام جزئي."),
    "Die Stelle ist ein Minijob.": _t("Bu bir mini iş, haftada birkaç saat.", "Це мініджоб, кілька годин на тиждень.",
                                      "To minijob, kilka godzin tygodniowo.", "Это миниджоб, несколько часов в неделю.",
                                      "این یک مینی‌جاب است، چند ساعت در هفته.", "هذا عمل صغير، بضع ساعات في الأسبوع."),
    "Man fängt sofort an.": _t("İşe hemen başlanıyor.", "Починають одразу.", "Zaczyna się od razu.", "Начинают сразу.",
                               "کار فوراً شروع می‌شود.", "يبدأ العمل فورًا."),
    # l'entretien
    "Ich heiße Mark Garnier, ich bin 25 Jahre alt und komme aus Kanada.": ("moi", _t(
        "Adım Mark Garnier, 25 yaşındayım ve Kanada'dan geliyorum.", "Мене звати Марк Гарньє, мені 25 років, і я з Канади.",
        "Nazywam się Mark Garnier, mam 25 lat i pochodzę z Kanady.", "Меня зовут Марк Гарнье, мне 25 лет, я из Канады.",
        "اسم من مارک گارنیه است، 25 سال دارم و اهل کانادا هستم.","اسمي مارك غارنييه، عمري 25 سنة، وأنا من كندا.")),
    "Ich spreche Französisch, Deutsch und Englisch.": ("langues", _t(
        "Fransızca, Almanca ve İngilizce konuşuyorum.", "Я розмовляю французькою, німецькою та англійською.",
        "Mówię po francusku, po niemiecku i po angielsku.", "Я говорю по-французски, по-немецки и по-английски.",
        "فرانسوی، آلمانی و انگلیسی صحبت می‌کنم.", "أتحدث الفرنسية والألمانية والإنجليزية.")),
    "Ja, ich habe zwei Jahre im Kundenservice gearbeitet.": ("experience", _t(
        "Evet, iki yıl müşteri hizmetlerinde çalıştım.", "Так, я два роки працював у службі підтримки клієнтів.",
        "Tak, przez dwa lata pracowałem w obsłudze klienta.", "Да, я два года работал в службе поддержки клиентов.",
        "بله، دو سال در بخش خدمات مشتریان کار کرده‌ام.", "نعم، عملت سنتين في خدمة العملاء.")),
    "Ja: Wie viele Tage Urlaub habe ich im Jahr?": ("questions", _t(
        "Evet: Yılda kaç gün iznim var?", "Так: скільки днів відпустки в мене на рік?", "Tak: ile dni urlopu mam w roku?",
        "Да: сколько дней отпуска у меня в году?", "بله: سالی چند روز مرخصی دارم؟", "نعم: كم يومًا من الإجازة لي في السنة؟")),
    "Ich arbeite gern mit Menschen, und ich spreche drei Sprachen.": ("pourquoi", _t(
        "İnsanlarla çalışmayı seviyorum ve üç dil konuşuyorum.", "Я люблю працювати з людьми, і я розмовляю трьома мовами.",
        "Lubię pracować z ludźmi i mówię trzema językami.", "Я люблю работать с людьми, и я говорю на трёх языках.",
        "کار کردن با مردم را دوست دارم و به سه زبان صحبت می‌کنم.", "أحب العمل مع الناس، وأتحدث ثلاث لغات.")),
    # la lettre
    "Mit freundlichen Grüßen": _t("Saygılarımla", "З повагою", "Z poważaniem", "С уважением", "با احترام", "مع خالص التحية"),
    # ce que dit le CV
    "Mark spricht Französisch als Muttersprache.": _t(
        "Mark'ın ana dili Fransızca.", "Французька — рідна мова Марка.", "Francuski jest językiem ojczystym Marka.",
        "Французский — родной язык Марка.", "زبان مادری مارک فرانسوی است.", "الفرنسية هي اللغة الأم لمارك."),
    "Mark spricht ein bisschen Deutsch und lernt es.": _t(
        "Mark biraz Almanca biliyor ve öğreniyor.", "Марк трохи розмовляє німецькою і вчить її.",
        "Mark trochę mówi po niemiecku i uczy się go.", "Марк немного говорит по-немецки и учит его.",
        "مارک کمی آلمانی صحبت می‌کند و دارد آن را یاد می‌گیرد.", "يتحدث مارك قليلًا من الألمانية ويتعلّمها."),
    "Mark spricht sehr gut Englisch.": _t(
        "Mark çok iyi İngilizce konuşuyor.", "Марк дуже добре розмовляє англійською.", "Mark bardzo dobrze mówi po angielsku.",
        "Марк очень хорошо говорит по-английски.", "مارک خیلی خوب انگلیسی صحبت می‌کند.", "يتحدث مارك الإنجليزية جيدًا جدًا."),
    # le contrat (la ligne du contrat et la phrase disent la même chose en français)
    "Mark fängt am 1. Dezember an.": _t(
        "Mark 1 Aralık'ta başlıyor.", "Марк починає 1 грудня.", "Mark zaczyna 1 grudnia.", "Марк начинает 1 декабря.",
        "مارک از 1 دسامبر شروع می‌کند.", "يبدأ مارك العمل في 1 ديسمبر."),
    "Die Probezeit dauert 6 Monate.": _t(
        "Deneme süresi 6 ay sürüyor.", "Випробувальний термін триває 6 місяців.", "Okres próbny trwa 6 miesięcy.",
        "Испытательный срок длится 6 месяцев.", "دورهٔ آزمایشی 6 ماه طول می‌کشد.", "تستمر فترة التجربة 6 أشهر."),
    "Mark arbeitet 40 Stunden pro Woche.": _t(
        "Mark haftada 40 saat çalışıyor.", "Марк працює 40 годин на тиждень.", "Mark pracuje 40 godzin tygodniowo.",
        "Марк работает 40 часов в неделю.", "مارک هفته‌ای 40 ساعت کار می‌کند.", "يعمل مارك 40 ساعة في الأسبوع."),
    "Mark verdient 3.000 € brutto im Monat.": _t(
        "Mark ayda brüt 3.000 € kazanıyor.", "Марк заробляє 3000 € брутто на місяць.", "Mark zarabia 3000 € brutto miesięcznie.",
        "Марк зарабатывает 3000 € брутто в месяц.", "مارک ماهانه 3000 یورو ناخالص درآمد دارد.", "راتب مارك الإجمالي 3000 يورو في الشهر."),
    "Mark hat 28 Tage Urlaub im Jahr.": _t(
        "Mark'ın yılda 28 gün izni var.", "У Марка 28 днів відпустки на рік.", "Mark ma 28 dni urlopu w roku.",
        "У Марка 28 дней отпуска в год.", "مارک سالی 28 روز مرخصی دارد.", "لدى مارك 28 يومًا إجازة في السنة."),
    # ce qui se passe sur les images
    "Mark sucht eine Stelle.": _t("Mark iş arıyor.", "Марк шукає роботу.", "Mark szuka pracy.", "Марк ищет работу.",
                                  "مارک دنبال کار می‌گردد.", "يبحث مارك عن عمل."),
    "Mark schreibt seine Bewerbung.": _t("Mark başvurusunu yazıyor.", "Марк пише заявку на роботу.", "Mark pisze podanie o pracę.",
                                         "Марк пишет заявку на работу.", "مارک درخواست کارش را می‌نویسد.", "يكتب مارك طلب التوظيف."),
    "Mark schickt seinen Lebenslauf.": _t("Mark özgeçmişini gönderiyor.", "Марк надсилає своє резюме.", "Mark wysyła swoje CV.",
                                          "Марк отправляет своё резюме.", "مارک رزومه‌اش را می‌فرستد.", "يرسل مارك سيرته الذاتية."),
    "Mark bewirbt sich um die Stelle.": _t("Mark bu pozisyona başvuruyor.", "Марк подає заявку на цю посаду.", "Mark ubiega się o to stanowisko.",
                                           "Марк подаёт заявку на эту должность.", "مارک برای این شغل درخواست می‌دهد.", "يتقدّم مارك لهذه الوظيفة."),
    "Mark stellt sich bei Frau Schneider vor.": _t(
        "Mark, Schneider Hanım'la iş görüşmesi yapıyor.", "Марк проходить співбесіду в пані Шнайдер.",
        "Mark ma rozmowę kwalifikacyjną u pani Schneider.", "Марк проходит собеседование у госпожи Шнайдер.",
        "مارک با خانم اشنایدر مصاحبهٔ کاری دارد.", "يُجري مارك مقابلة عمل مع السيدة شنايدر."),
    "Mark unterschreibt den Arbeitsvertrag.": _t("Mark iş sözleşmesini imzalıyor.", "Марк підписує трудовий договір.",
                                                 "Mark podpisuje umowę o pracę.", "Марк подписывает трудовой договор.",
                                                 "مارک قرارداد کار را امضا می‌کند.", "يوقّع مارك عقد العمل."),
    "Mark fängt am Montag an.": _t("Mark pazartesi başlıyor.", "Марк починає в понеділок.", "Mark zaczyna w poniedziałek.",
                                   "Марк начинает в понедельник.", "مارک دوشنبه شروع می‌کند.", "يبدأ مارك يوم الاثنين."),
    "Frau Schneider begrüßt Mark.": _t("Schneider Hanım Mark'ı karşılıyor.", "Пані Шнайдер вітає Марка.", "Pani Schneider wita Marka.",
                                       "Госпожа Шнайдер встречает Марка.", "خانم اشنایدر به مارک خوشامد می‌گوید.", "تستقبل السيدة شنايدر مارك."),
    "Frau Schneider stellt Mark die Kollegen vor.": _t(
        "Schneider Hanım, Mark'ı iş arkadaşlarıyla tanıştırıyor.", "Пані Шнайдер знайомить Марка з колегами.",
        "Pani Schneider przedstawia Markowi kolegów.", "Госпожа Шнайдер знакомит Марка с коллегами.",
        "خانم اشنایدر همکاران را به مارک معرفی می‌کند.", "تُعرّف السيدة شنايدر مارك على زملائه."),
    "Mark lernt seine Kollegen kennen.": _t("Mark iş arkadaşlarıyla tanışıyor.", "Марк знайомиться зі своїми колегами.",
                                            "Mark poznaje swoich kolegów.", "Марк знакомится со своими коллегами.",
                                            "مارک با همکارانش آشنا می‌شود.", "يتعرّف مارك على زملائه."),
    "Lisa zeigt Mark seinen Schreibtisch.": _t("Lisa, Mark'a çalışma masasını gösteriyor.", "Ліза показує Маркові його стіл.",
                                               "Lisa pokazuje Markowi jego biurko.", "Лиза показывает Марку его стол.",
                                               "لیزا میز مارک را به او نشان می‌دهد.", "تُري ليزا مارك مكتبه."),
    "Mark arbeitet im Kundenservice.": _t("Mark müşteri hizmetlerinde çalışıyor.", "Марк працює в службі підтримки клієнтів.",
                                          "Mark pracuje w obsłudze klienta.", "Марк работает в службе поддержки клиентов.",
                                          "مارک در بخش خدمات مشتریان کار می‌کند.", "يعمل مارك في خدمة العملاء."),
    "Mark isst mit den Kollegen in der Kantine.": _t(
        "Mark iş arkadaşlarıyla kantinde yemek yiyor.", "Марк обідає з колегами в їдальні.", "Mark je z kolegami w stołówce.",
        "Марк обедает с коллегами в столовой.", "مارک با همکارانش در سلف غذا می‌خورد.", "يأكل مارك مع زملائه في المقصف."),
    "Mark meldet sich heute krank.": _t("Mark bugün hasta olduğunu bildiriyor.", "Марк сьогодні повідомляє, що захворів.",
                                        "Mark zgłasza dziś, że jest chory.", "Марк сегодня сообщает, что заболел.",
                                        "مارک امروز اطلاع می‌دهد که بیمار است.", "يُبلغ مارك اليوم أنه مريض."),
    "Mark ruft seine Chefin an.": _t("Mark müdürünü arıyor.", "Марк телефонує своїй начальниці.", "Mark dzwoni do swojej szefowej.",
                                     "Марк звонит своей начальнице.", "مارک به رئیسش زنگ می‌زند.", "يتصل مارك بمديرته."),
    "Mark verdient 3.000 Euro im Monat.": _t("Mark ayda 3.000 avro kazanıyor.", "Марк заробляє 3000 євро на місяць.",
                                             "Mark zarabia 3000 euro miesięcznie.", "Марк зарабатывает 3000 евро в месяц.",
                                             "مارک ماهی 3000 یورو درآمد دارد.", "يكسب مارك 3000 يورو في الشهر."),
    # du ou Sie (Frau Schneider dit Sie à Mark, les collègues du) ; l'arabe marque le Sie par « حضرتك »
    "Können Sie am Montag anfangen?": _t("Pazartesi başlayabilir misiniz?", "Ви можете почати в понеділок?", "Może pan zacząć w poniedziałek?",
                                         "Вы можете начать в понедельник?", "می‌توانید از دوشنبه شروع کنید؟", "هل يمكن لحضرتك أن تبدأ يوم الاثنين؟"),
    "Kannst du mir kurz helfen?": _t("Bana biraz yardım edebilir misin?", "Можеш мені трохи допомогти?", "Możesz mi chwilę pomóc?",
                                     "Можешь мне немного помочь?", "می‌توانی یک لحظه کمکم کنی؟", "هل يمكنك مساعدتي قليلًا؟"),
    "Haben Sie Erfahrung im Kundenservice?": _t("Müşteri hizmetlerinde deneyiminiz var mı?", "У вас є досвід роботи в службі підтримки клієнтів?",
                                                "Ma pan doświadczenie w obsłudze klienta?", "У вас есть опыт работы в службе поддержки клиентов?",
                                                "در خدمات مشتریان تجربه دارید؟", "هل لدى حضرتك خبرة في خدمة العملاء؟"),
    "Hast du heute Mittag Zeit?": _t("Bugün öğlen vaktin var mı?", "У тебе є час сьогодні в обід?", "Masz dziś czas w południe?",
                                     "У тебя есть время сегодня в обед?", "امروز ظهر وقت داری؟", "هل لديك وقت اليوم عند الظهر؟"),
    "Sprechen Sie auch Englisch?": _t("İngilizce de konuşuyor musunuz?", "Ви також розмовляєте англійською?", "Czy mówi pan także po angielsku?",
                                      "Вы также говорите по-английски?", "انگلیسی هم صحبت می‌کنید؟", "هل تتحدث حضرتك الإنجليزية أيضًا؟"),
    "Sprichst du auch Französisch?": _t("Fransızca da konuşuyor musun?", "Ти також розмовляєш французькою?", "Mówisz też po francusku?",
                                        "Ты тоже говоришь по-французски?", "فرانسوی هم صحبت می‌کنی؟", "هل تتحدث الفرنسية أيضًا؟"),
    "Woher kommen Sie?": _t("Nerelisiniz?", "Звідки ви?", "Skąd pan pochodzi?", "Откуда вы?", "اهل کجا هستید؟", "من أين حضرتك؟"),
    "Woher kommst du?": _t("Nerelisin?", "Звідки ти?", "Skąd jesteś?", "Откуда ты?", "اهل کجایی؟", "من أين أنت؟"),
    "Arbeiten Sie gern im Team?": _t("Takım hâlinde çalışmayı sever misiniz?", "Ви любите працювати в команді?", "Lubi pan pracować w zespole?",
                                     "Вы любите работать в команде?", "کار تیمی را دوست دارید؟", "هل تحب حضرتك العمل ضمن فريق؟"),
    "Seit wann arbeitest du hier?": _t("Ne zamandan beri burada çalışıyorsun?", "Відколи ти тут працюєш?", "Od kiedy tu pracujesz?",
                                       "С каких пор ты здесь работаешь?", "از کی اینجا کار می‌کنی؟", "منذ متى تعمل هنا؟"),
    "Trinken Sie einen Kaffee?": _t("Bir kahve alır mısınız?", "Випʼєте кави?", "Napije się pan kawy?", "Выпьете кофе?",
                                    "قهوه میل دارید؟", "هل تشرب حضرتك قهوة؟"),
    "Trinkst du auch einen Kaffee?": _t("Sen de bir kahve içer misin?", "Ти теж випʼєш кави?", "Ty też napijesz się kawy?",
                                        "Ты тоже выпьешь кофе?", "تو هم قهوه می‌خوری؟", "هل تشرب قهوة أنت أيضًا؟"),
    "Sind Sie Herr Garnier?": _t("Garnier Bey siz misiniz?", "Ви пан Гарньє?", "Czy to pan Garnier?", "Вы господин Гарнье?",
                                 "شما آقای گارنیه هستید؟", "هل حضرتك السيد غارنييه؟"),
    "Bist du der Neue?": _t("Yeni gelen sen misin?", "Ти новенький?", "To ty jesteś ten nowy?", "Ты новенький?",
                            "تو تازه‌واردی؟", "هل أنت الموظف الجديد؟"),
    "Isst du heute mit uns in der Kantine?": _t("Bugün bizimle kantinde yemek yer misin?", "Ти сьогодні обідатимеш з нами в їдальні?",
                                                "Zjesz dziś z nami w stołówce?", "Ты сегодня пообедаешь с нами в столовой?",
                                                "امروز با ما در سلف غذا می‌خوری؟", "هل تأكل معنا في المقصف اليوم؟"),
    # le téléphone : Mark se déclare malade (Mark parle, puis Frau Schneider)
    "Es tut mir leid, ich bin krank.": _t("Üzgünüm, hastayım.", "Вибачте, я захворів.", "Przepraszam, jestem chory.",
                                          "Извините, я заболел.", "متأسفم، بیمارم.", "آسف، أنا مريض."),
    "Ich kann heute nicht zur Arbeit kommen.": _t("Bugün işe gelemiyorum.", "Я не можу сьогодні прийти на роботу.", "Nie mogę dziś przyjść do pracy.",
                                                  "Я не могу сегодня прийти на работу.", "امروز نمی‌توانم سر کار بیایم.", "لا أستطيع المجيء إلى العمل اليوم."),
    "Oh, das tut mir leid. Gehen Sie bitte zum Arzt.": _t(
        "Ah, çok üzüldüm. Lütfen doktora gidin.", "Ой, мені шкода. Будь ласка, підіть до лікаря.", "Och, przykro mi. Proszę iść do lekarza.",
        "Ой, мне жаль. Пожалуйста, сходите к врачу.", "آه، متأسفم. لطفاً پیش دکتر بروید.", "آه، يؤسفني ذلك. اذهب إلى الطبيب من فضلك."),
    "Und schicken Sie mir bitte die Krankmeldung.": _t(
        "Ve lütfen bana hastalık raporunu gönderin.", "І, будь ласка, надішліть мені лікарняний.", "I proszę przesłać mi zwolnienie lekarskie.",
        "И, пожалуйста, пришлите мне больничный.", "و لطفاً گواهی استعلاجی را برایم بفرستید.", "وأرسل لي الإجازة المرضية من فضلك."),
    "Gute Besserung, Herr Garnier!": _t("Geçmiş olsun, Garnier Bey!", "Одужуйте, пане Гарньє!", "Szybkiego powrotu do zdrowia, panie Garnier!",
                                        "Выздоравливайте, господин Гарнье!", "آقای گارنیه، زودتر خوب شوید!", "أتمنى لك الشفاء العاجل يا سيد غارنييه!"),
    # qui est qui (la page française ne traduit que la conclusion)
    "CHEFIN": _t("Schneider Hanım, Mark'ın müdürü.", "Пані Шнайдер — начальниця Марка.", "Pani Schneider jest szefową Marka.",
                 "Госпожа Шнайдер — начальница Марка.", "خانم اشنایدر رئیس مارک است.", "السيدة شنايدر هي مديرة مارك."),
    "KOLLEGE": _t("Jonas, Mark'ın iş arkadaşı.", "Йонас — колега Марка.", "Jonas jest kolegą Marka z pracy.",
                  "Йонас — коллега Марка.", "یوناس همکار مارک است.", "يوناس زميل مارك."),
    "KOLLEGIN": _t("Lisa, Mark'ın iş arkadaşı.", "Ліза — колега Марка.", "Lisa jest koleżanką Marka z pracy.",
                   "Лиза — коллега Марка.", "لیزا همکار مارک است.", "ليزا زميلة مارك."),
    "NEU": _t("Mark yeni bir çalışan.", "Марк — новий працівник.", "Mark jest nowym pracownikiem.", "Марк — новый сотрудник.",
              "مارک کارمند جدید است.", "مارك موظف جديد."),
    "ARBEITGEBER": _t("Sonnenweg Reisen, Mark'ın işvereni.", "Sonnenweg Reisen — роботодавець Марка.", "Sonnenweg Reisen jest pracodawcą Marka.",
                      "Sonnenweg Reisen — работодатель Марка.", "کارفرمای مارک Sonnenweg Reisen است.", "جهة عمل مارك هي Sonnenweg Reisen."),
    "KUNDE": _t("Adam bir müşteri.", "Чоловік — клієнт.", "Mężczyzna jest klientem.", "Мужчина — клиент.", "آن مرد مشتری است.", "الرجل زبون."),
    "KUNDIN": _t("Kadın bir müşteri.", "Жінка — клієнтка.", "Kobieta jest klientką.", "Женщина — клиентка.", "آن زن مشتری است.", "المرأة زبونة."),
    # les papiers
    "Das ist die Stellenanzeige.": _t("Bu iş ilanı.", "Це оголошення про вакансію.", "To jest ogłoszenie o pracę.", "Это объявление о вакансии.",
                                      "این آگهی استخدام است.", "هذا هو إعلان الوظيفة."),
    "Das ist der Lebenslauf.": _t("Bu özgeçmiş.", "Це резюме.", "To jest CV.", "Это резюме.", "این رزومه است.", "هذه هي السيرة الذاتية."),
    "Das ist das Anschreiben.": _t("Bu ön yazı.", "Це супровідний лист.", "To jest list motywacyjny.", "Это сопроводительное письмо.",
                                   "این نامهٔ انگیزشی است.", "هذه هي رسالة التحفيز."),
    "Das ist der Arbeitsvertrag.": _t("Bu iş sözleşmesi.", "Це трудовий договір.", "To jest umowa o pracę.", "Это трудовой договор.",
                                      "این قرارداد کار است.", "هذا هو عقد العمل."),
}
# les lignes du contrat : la page française les traduit par la phrase
FIXE_DE["Beginn: 1. Dezember 2026"] = FIXE_DE["Mark fängt am 1. Dezember an."]
FIXE_DE["Probezeit: 6 Monate"] = FIXE_DE["Die Probezeit dauert 6 Monate."]
FIXE_DE["Arbeitszeit: 40 Stunden pro Woche"] = FIXE_DE["Mark arbeitet 40 Stunden pro Woche."]
FIXE_DE["Gehalt: 3.000 € brutto im Monat"] = FIXE_DE["Mark verdient 3.000 € brutto im Monat."]
FIXE_DE["Urlaub: 28 Tage im Jahr"] = FIXE_DE["Mark hat 28 Tage Urlaub im Jahr."]
# qui est qui : la phrase apprise -> la conclusion
QUI_DE = {"Sie ist Marks Chefin.": "CHEFIN", "Sie ist die Chefin.": "CHEFIN", "Er ist Marks Kollege.": "KOLLEGE",
          "Jonas ist ein Kollege von Mark.": "KOLLEGE", "Sie ist Marks Kollegin.": "KOLLEGIN", "Lisa ist eine Kollegin von Mark.": "KOLLEGIN",
          "Er ist ein neuer Mitarbeiter.": "NEU", "Die Firma hat einen neuen Mitarbeiter: Mark.": "NEU",
          "Die Firma ist Marks Arbeitgeber.": "ARBEITGEBER", "Das ist sein Arbeitgeber.": "ARBEITGEBER",
          "Der Mann ist ein Kunde.": "KUNDE", "Sie ist eine Kundin.": "KUNDIN"}

FIXE_ES = {
    "Es un puesto de jornada completa.": "هذه وظيفة بدوام كامل.",
    "Es un puesto de media jornada.": "هذه وظيفة بدوام جزئي.",
    "Es un trabajo por horas.": "هذا عمل بأجر بالساعة، بضع ساعات في الأسبوع.",
    "Se empieza a trabajar de inmediato.": "يبدأ العمل فورًا.",
    "Me llamo Mark Garnier, tengo 25 años y soy de México.": ("moi", "اسمي مارك غارنييه، عمري 25 سنة، وأنا من المكسيك."),
    "Hablo español, inglés y francés.": ("langues", "أتحدث الإسبانية والإنجليزية والفرنسية."),
    "Sí, he trabajado dos años en atención al cliente.": ("experience", "نعم، عملت سنتين في خدمة العملاء."),
    "Sí: ¿cuántos días de vacaciones tengo al año?": ("questions", "نعم: كم يومًا من الإجازة لي في السنة؟"),
    "Me gusta trabajar con la gente y hablo tres idiomas.": ("pourquoi", "أحب العمل مع الناس، وأتحدث ثلاث لغات."),
    "Un cordial saludo,": "مع خالص التحية،",
    "La lengua materna de Mark es el español.": "اللغة الأم لمارك هي الإسبانية.",
    "Mark habla muy bien inglés.": "يتحدث مارك الإنجليزية جيدًا جدًا.",
    "Mark tiene un nivel intermedio de francés.": "مستوى مارك في الفرنسية متوسط.",
    "Mark empieza el 1 de diciembre.": "يبدأ مارك العمل في 1 ديسمبر.",
    "El período de prueba dura 2 meses.": "تستمر فترة التجربة شهرين.",
    "Mark trabaja 40 horas a la semana.": "يعمل مارك 40 ساعة في الأسبوع.",
    "Mark gana 1.700 € brutos al mes.": "راتب مارك الإجمالي 1700 يورو في الشهر.",
    "Mark tiene 30 días de vacaciones al año.": "لدى مارك 30 يومًا إجازة في السنة.",
    "Mark busca trabajo.": "يبحث مارك عن عمل.",
    "Mark escribe su carta de presentación.": "يكتب مارك رسالة التقديم.",
    "Mark envía su currículum.": "يرسل مارك سيرته الذاتية.",
    "Mark solicita el puesto.": "يتقدّم مارك لهذه الوظيفة.",
    "Mark tiene una entrevista con la señora Navarro.": "لدى مارك مقابلة عمل مع السيدة نافارو.",
    "Mark firma el contrato.": "يوقّع مارك العقد.",
    "La señora Navarro saluda a Mark.": "تستقبل السيدة نافارو مارك.",
    "La señora Navarro presenta a Mark a sus compañeros.": "تُعرّف السيدة نافارو مارك على الزملاء.",
    "Mark conoce a sus compañeros.": "يتعرّف مارك على زملائه.",
    "Lucía le enseña su escritorio a Mark.": "تُري لوسيا مارك مكتبه.",
    "Mark trabaja en atención al cliente.": "يعمل مارك في خدمة العملاء.",
    "Mark come con sus compañeros en el comedor.": "يأكل مارك مع زملائه في المقصف.",
    "Mark llama a su jefa.": "يتصل مارك بمديرته.",
    "Mark gana 1.700 euros al mes.": "يكسب مارك 1700 يورو في الشهر.",
    "Mark empieza el lunes.": "يبدأ مارك يوم الاثنين.",
    "¿Puede usted empezar el lunes?": "هل يمكن لحضرتك أن تبدأ يوم الاثنين؟",
    "¿Me puedes ayudar un momento?": "هل يمكنك مساعدتي لحظة؟",
    "¿Tiene usted experiencia en atención al cliente?": "هل لدى حضرتك خبرة في خدمة العملاء؟",
    "¿Tienes tiempo para comer hoy?": "هل لديك وقت للغداء اليوم؟",
    "¿Habla usted inglés?": "هل تتحدث حضرتك الإنجليزية؟",
    "¿Hablas francés también?": "هل تتحدث الفرنسية أيضًا؟",
    "¿De dónde es usted?": "من أين حضرتك؟",
    "¿De dónde eres?": "من أين أنت؟",
    "¿Trabaja usted bien en equipo?": "هل تعمل حضرتك جيدًا ضمن فريق؟",
    "¿Desde cuándo trabajas aquí?": "منذ متى تعمل هنا؟",
    "¿Quiere usted un café?": "هل تريد حضرتك قهوة؟",
    "¿Quieres un café?": "هل تريد قهوة؟",
    "¿Comes con nosotros hoy?": "هل تأكل معنا اليوم؟",
    "Lo siento, estoy enfermo.": "آسف، أنا مريض.",
    "Hoy no puedo ir a trabajar.": "لا أستطيع الذهاب إلى العمل اليوم.",
    "Vaya al médico, por favor.": "آه، يؤسفني ذلك. اذهب إلى الطبيب من فضلك.",
    "Y mándeme la baja médica, por favor.": "وأرسل لي الإجازة المرضية من فضلك.",
    "La señora Navarro dirige el equipo de atención al cliente. Es la jefa de Mark.": "السيدة نافارو هي مديرة مارك.",
    "La señora Navarro es la jefa de Mark, Jorge y Lucía.": "السيدة نافارو هي مديرة مارك.",
    "Jorge trabaja con Mark en el mismo equipo. Es su compañero.": "خورخي زميل مارك.",
    "Jorge y Mark trabajan juntos. Jorge es un compañero de Mark.": "خورخي زميل مارك.",
    "Lucía trabaja con Mark en el mismo equipo. Es su compañera.": "لوسيا زميلة مارك.",
    "Lucía y Mark trabajan juntos. Lucía es una compañera de Mark.": "لوسيا زميلة مارك.",
    "Mark trabaja para Viajes Solano. Viajes Solano es su empresa.": "شركة مارك هي Viajes Solano.",
    "Viajes Solano paga el sueldo de Mark: es su empresa.": "شركة مارك هي Viajes Solano.",
    "Mark ayuda por teléfono a un señor que quiere reservar un viaje. El señor es un cliente.": "الرجل زبون.",
    "Mark habla por teléfono con un señor que busca un viaje. Es un cliente de Viajes Solano.": "الرجل زبون.",
    "La oficina de Viajes Solano está en Madrid.": "مكتب Viajes Solano في مدريد.",
    "La mesa de Mark está al lado de la ventana.": "مكتب مارك بجانب النافذة.",
    "Viajes Solano es una empresa de viajes.": "إن Viajes Solano شركة سفريات.",
    "La señora Navarro es la jefa de Mark.": "السيدة نافارو هي مديرة مارك.",
    "Jorge es el compañero de Mark.": "خورخي هو زميل مارك.",
    "Es la oferta de empleo.": "هذا هو إعلان الوظيفة.",
    "Es el currículum.": "هذه هي السيرة الذاتية.",
    "Es la carta de presentación.": "هذه هي رسالة التقديم.",
    "Es el contrato.": "هذا هو عقد العمل.",
}
FIXE_ES["Fecha de inicio: 1 de diciembre de 2026"] = FIXE_ES["Mark empieza el 1 de diciembre."]
FIXE_ES["Período de prueba: 2 meses"] = FIXE_ES["El período de prueba dura 2 meses."]
FIXE_ES["Jornada: completa, 40 horas semanales"] = FIXE_ES["Mark trabaja 40 horas a la semana."]
FIXE_ES["Sueldo: 1.700 € brutos al mes"] = FIXE_ES["Mark gana 1.700 € brutos al mes."]
FIXE_ES["Vacaciones: 30 días al año"] = FIXE_ES["Mark tiene 30 días de vacaciones al año."]


# ---------- la traduction d'une phrase apprise ----------
def _de(ph, lg):
    f = FIXE_DE.get(ph)
    if f is not None:
        if isinstance(f, tuple):
            return _dialogue(lg, QUESTIONS[f[0]][lg], f[1][lg])
        return f[lg]
    for fin, cle in QUI_DE.items():
        if ph.endswith(fin):
            return FIXE_DE[cle][lg]
    m = re.fullmatch(r"Man arbeitet (\d+) Stunden pro Woche\.", ph)
    if m:
        h = _heures(lg, m.group(1))
        return {"tr": "Haftada %s çalışılıyor." % h, "uk": "Працюють %s на тиждень." % h, "ru": "Работают %s в неделю." % h,
                "pl": "Pracuje się %s tygodniowo." % h, "fa": "هفته‌ای %s کار می‌کنند." % h, "ar": "مدة العمل %s في الأسبوع." % h}[lg]
    m = re.fullmatch(r"Man verdient ([\d.,]+) € (im Monat|pro Stunde)\.", ph)
    if m:
        x, mois = _montant(lg, m.group(1)), m.group(2) == "im Monat"
        if mois:
            return {"tr": "Ayda %s kazanılıyor." % x, "uk": "Заробляють %s на місяць." % x, "ru": "Зарабатывают %s в месяц." % x,
                    "pl": "Zarabia się %s miesięcznie." % x, "fa": "درآمد ماهانه %s است." % x, "ar": "الراتب %s في الشهر." % x}[lg]
        return {"tr": "Saat başına %s kazanılıyor." % x, "uk": "Заробляють %s на годину." % x, "ru": "Зарабатывают %s в час." % x,
                "pl": "Zarabia się %s za godzinę." % x, "fa": "درآمد ساعتی %s است." % x, "ar": "الأجر %s في الساعة." % x}[lg]
    m = re.fullmatch(r"Man fängt am (\d+)\. (\w+) an\.", ph)
    if m:
        d = _date(lg, m.group(1), m.group(2))
        return {"tr": "İşe %s başlanıyor." % d, "uk": "Починають %s." % d, "ru": "Начинают %s." % d, "pl": "Zaczyna się %s." % d,
                "fa": "کار از %s شروع می‌شود." % d, "ar": "يبدأ العمل في %s." % d}[lg]
    m = re.fullmatch(r"Man schickt die Bewerbung an (?:Frau|Herrn) (\w+)\.", ph)
    if m:
        a = _a_qui(lg, m.group(1))
        return {"tr": "Başvuru %s gönderiliyor." % a, "uk": "Заявку надсилають %s." % a, "ru": "Заявку отправляют %s." % a,
                "pl": "Aplikację wysyła się %s." % a, "fa": "درخواست را برای %s می‌فرستند." % a, "ar": "تُرسَل طلبات التوظيف إلى %s." % a}[lg]
    m = re.fullmatch(r"Man soll (\w+) sein\.", ph)
    if m:
        return Q_DE[m.group(1)][lg][2]
    m = re.fullmatch(r"Der neue (\w+) arbeitet (?:in einem|in einer|für eine) (\w+)\.", ph)
    if m:
        return _nouveau(lg, m.group(1), m.group(2))
    m = re.fullmatch(r"(Mark|Jonas|Lisa|Frau Schneider) .+\. \1 ist (\w+)\.", ph)
    if m:
        return _qualite(lg, m.group(1), m.group(2), "de")
    m = re.fullmatch(r"Ich bin (\w+) und (\w+)\.", ph)
    if m:
        return _forts(lg, m.group(1), m.group(2), "de")
    m = re.fullmatch(r"Ich kann am (\d+)\. (\w+) anfangen\.", ph)
    if m:
        return _commencer(lg, m.group(1), m.group(2), "de")
    m = re.fullmatch(r"Ich möchte gern in (Vollzeit|Teilzeit) arbeiten\.", ph)
    if m:
        return _temps(lg, m.group(1) == "Vollzeit", "de")
    m = re.fullmatch(r"Sehr geehrte(?:r)? (?:Frau|Herr) (\w+),", ph)
    if m:
        return _salut(lg, m.group(1))
    m = re.fullmatch(r"ich habe Ihre Anzeige gelesen und bewerbe mich um die Stelle als (\w+)(?: im Kundenservice)?\.", ph)
    if m:
        r = ROLES[m.group(1)][lg][1]
        return {"tr": "%s pozisyonu için başvuruyorum." % (r[0].upper() + r[1:]),
                "uk": "Я подаю заявку на посаду %s." % r, "ru": "Я подаю заявку на должность %s." % r,
                "pl": "Ubiegam się o stanowisko %s." % r, "fa": "برای سمت %s درخواست می‌دهم." % r, "ar": "أتقدّم بطلب لوظيفة %s." % r}[lg]
    m = re.match(r"(Persönliche Daten|Berufserfahrung|Ausbildung|Sprachkenntnisse|Hobbys): ", ph)
    if m:
        return m.group(1) + " = " + RUBRIQUES[m.group(1)][lg]
    return None


def _es(ph, lg):
    f = FIXE_ES.get(ph)
    if f is not None:
        if isinstance(f, tuple):
            return _dialogue(lg, QUESTIONS_ES.get(f[0]) or QUESTIONS[f[0]][lg], f[1])
        return f
    m = re.fullmatch(r"Se trabajan (\d+) horas a la semana\.", ph)
    if m:
        return "مدة العمل %s في الأسبوع." % _heures(lg, m.group(1))
    m = re.fullmatch(r"Se gana ([\d.,]+) € (al mes|la hora)\.", ph)
    if m:
        x = _montant(lg, m.group(1))
        return ("الراتب %s في الشهر." if m.group(2) == "al mes" else "الأجر %s في الساعة.") % x
    m = re.fullmatch(r"Se empieza a trabajar el (\d+) de (\w+)\.", ph)
    if m:
        return "يبدأ العمل في %s." % _date(lg, m.group(1), m.group(2))
    m = re.fullmatch(r"Se envía el currículum (?:a la señora|al señor) (\w+)\.", ph)
    if m:
        g, ar = DEST["es"][m.group(1)]
        return "تُرسَل السيرة الذاتية إلى %s %s." % ("السيدة" if g == "f" else "السيد", ar)
    m = re.fullmatch(r"Hay que ser (\w+)\.", ph)
    if m:
        return Q_ES[m.group(1)][2]
    m = re.fullmatch(r"El nuevo (.+?) trabaja (?:en una|en un|para una) (\w+)(?: de viajes)?\.", ph)
    if m:
        if m.group(1).startswith("agente"):   # « le nouvel agent du service client », pas « le nouvel employé »
            return "يعمل موظف خدمة العملاء الجديد %s." % LIEUX[LIEUX_ES[m.group(2)]][lg]
        return _nouveau(lg, ROLES_ES[m.group(1)], LIEUX_ES[m.group(2)])
    m = re.fullmatch(r"(Mark|Jorge|Lucía|La señora Navarro) .+\. \1 es (\w+)\.", ph)
    if m:
        return _qualite(lg, m.group(1), m.group(2), "es")
    m = re.fullmatch(r"(Mark|Jorge|Lucía) es (\w+)\.", ph)
    if m:
        g, p = _personne(lg, m.group(1), "es")
        return "%s %s." % (p, _attribut_ar(m.group(2), g))
    m = re.fullmatch(r"(Mark|Jorge|Lucía) está (\w+) .+\.", ph)
    if m:
        g, p = _personne(lg, m.group(1), "es")
        return "%s %s." % (p, _g(ESTAR_ES[ESTAR_FEM.get(m.group(2), m.group(2))], g))
    m = re.fullmatch(r"Soy (\w+) y (\w+)\.", ph)
    if m:
        return _forts(lg, m.group(1), m.group(2), "es")
    m = re.fullmatch(r"Puedo empezar el (\d+) de (\w+)\.", ph)
    if m:
        return _commencer(lg, m.group(1), m.group(2), "es")
    m = re.fullmatch(r"Prefiero la (jornada completa|media jornada)\.", ph)
    if m:
        return _temps(lg, m.group(1) == "jornada completa", "es")
    m = re.fullmatch(r"Estimad[oa] señor[a]? (\w+):", ph)
    if m:
        return _salut(lg, m.group(1), "es")
    m = re.fullmatch(r"He leído su oferta y me gustaría solicitar el puesto de (.+)\.", ph)
    if m:
        return "أتقدّم بطلب لوظيفة %s." % ROLES[ROLES_ES[m.group(1)]][lg][1]
    m = re.match(r"(Datos personales|Experiencia laboral|Formación|Idiomas|Aficiones): ", ph)
    if m:
        return m.group(1) + " = " + RUBRIQUES[RUBRIQUES_ES[m.group(1)]][lg]
    return None


def traduire(app, ph, lg):
    """la phrase apprise -> sa traduction dans la langue lg, ou None"""
    return _de(ph, lg) if app == "de" else _es(ph, lg)


def poser(app, questions, actions, docs):
    """ajoute les langues de ce module au champ « t » des questions et des actions ; renvoie (les phrases sans traduction,
    {papier: {langue: « C'est … » en entier}}) -- la page en a besoin pour les fiches des papiers, « C'est » ne se colle
    pas devant un nom dans ces langues. DOCS n'est pas touché (travail.py le dépaquette en trois).
    travail.py s'arrête si la première liste n'est pas vide."""
    manque, papiers = [], {}
    for x in list(questions) + list(actions):
        if not x.get("t"):
            continue
        for lg in pour(app):
            v = traduire(app, x["ph"], lg)
            if not v:
                manque.append((lg, x["ph"]))
            else:
                x["t"][lg] = v
    # un même dict « t » peut servir à deux phrases (travail.py le partage) : chaque phrase doit garder SA traduction
    for x in list(questions) + list(actions):
        if x.get("t"):
            for lg in pour(app):
                if x["t"].get(lg) != traduire(app, x["ph"], lg):
                    manque.append((lg, "deux traductions pour un même champ t : " + x["ph"]))
    debut = {"de": "Das ist ", "es": "Es "}[app]
    for cle, d in docs.items():
        ph = debut + d[1] + " " + d[0] + "."
        full = {}
        for lg in pour(app):
            v = traduire(app, ph, lg)
            if not v:
                manque.append((lg, ph))
            else:
                full[lg] = v
        papiers[cle] = full
    return manque, papiers
