# -*- coding: utf-8 -*-
"""« La journee » dans les langues d'interface sans phrase traduite jusqu'ici : turc, ukrainien, polonais, russe
(lot 1 de l'alignement des themes, 14 nov. 2026 ; le persan et l'arabe suivront ici meme).

LE CHEMIN NATIF (decision du chef du 14 nov.) : comme le francais, l'anglais et le portugais de journee.py, chaque
verbe a sa phrase traduite aux cinq personnes (je, tu, il/elle, nous, ils), {S} le sujet, {H} l'heure, que la page
assemble avec les memes choix que la question. Rien n'est ecrit phrase par phrase.

L'ORDRE DES MOTS : le russe, l'ukrainien et le polonais mettent l'heure a la fin (« Анна прокидається о 6:30 ») ; le
turc la met avant le verbe et laisse tomber le pronom (« Anna saat 6.30'da uyanıyor », « Saat 7'de kalkıyorum »).
Quand la phrase finit deja sur un complement de lieu (« в детский сад »), l'heure passe apres le sujet. La page
resserre les espaces quand l'heure est absente (le verbe seul, pour le choix faux traduit).

Le temps : le present (le turc : le present en -iyor, celui d'une journee qu'on raconte ; les faits de frequence au
present general, -ir / -ar : « Anna kahvaltısını her zaman evde yapar »).

Points douteux : retours/A-RELIRE-THEMES-<LG>.md (a relire par un natif).
"""

LANGUES = ("tr", "uk", "pl", "ru")

SUJETS = {
    "Anna":    {"ru": "Анна", "uk": "Анна", "pl": "Anna", "tr": "Anna"},
    "Mark":    {"ru": "Марк", "uk": "Марк", "pl": "Mark", "tr": "Mark"},
    "Katrin":  {"ru": "Катрин", "uk": "Катрін", "pl": "Katrin", "tr": "Katrin"},
    "Jan":     {"ru": "Ян", "uk": "Ян", "pl": "Jan", "tr": "Jan"},
    "BenMia":  {"ru": "Бен и Мия", "uk": "Бен і Мія", "pl": "Ben i Mia", "tr": "Ben ile Mia"},
    "familia": {"ru": "Семья", "uk": "Родина", "pl": "Rodzina", "tr": "Aile"},
}
PERSONNES = {"ru": ["Я", "Ты", None, "Мы", None], "uk": ["Я", "Ти", None, "Ми", None],
             "pl": ["Ja", "Ty", None, "My", None], "tr": ["Ben", "Sen", None, "Biz", None]}


def _slave(sujets, formes, suite="", heure_avant=False):
    """Les cinq personnes d'une langue slave : « я просыпаюсь {H} », « {S} просыпается {H} »..."""
    out = []
    for k in range(5):
        s = sujets[k] if k in (0, 1, 3) else "{S}"
        v = formes[k] + (" " + suite if suite else "")
        out.append((s + " {H} " + v) if heure_avant else (s + " " + v + " {H}"))
    return out


def _tr(formes, suite="", suites=None):
    """Les cinq personnes du turc : sans pronom, l'heure avant le complement et le verbe (« {S} {H} eve dönüyor »)."""
    out = []
    for k in range(5):
        c = (suites[k] if suites else suite)
        v = ((c + " ") if c else "") + formes[k]
        out.append(("{S} {H} " if k in (2, 4) else "{H} ") + v)
    return out


# le polonais laisse tomber le pronom, comme le turc (« Budzę się o 6:30 ») ; le russe et l'ukrainien le gardent
RU_P, UK_P, PL_P = ["я", "ты", None, "мы", None], ["я", "ти", None, "ми", None], ["", "", None, "", None]
ru = lambda formes, suite="", avant=False: _slave(RU_P, formes, suite, avant)
uk = lambda formes, suite="", avant=False: _slave(UK_P, formes, suite, avant)
pl = lambda formes, suite="", avant=False: _slave(PL_P, formes, suite, avant)
IYOR = lambda r: [r + "yor" + x for x in ("um", "sun", "", "uz", "lar")]       # uyanıyorum ... uyanıyorlar

VERBES = {
    "despertarse": {
        "ru": ru(["просыпаюсь", "просыпаешься", "просыпается", "просыпаемся", "просыпаются"]),
        "uk": uk(["прокидаюся", "прокидаєшся", "прокидається", "прокидаємося", "прокидаються"]),
        "pl": pl(["budzę się", "budzisz się", "budzi się", "budzimy się", "budzą się"]),
        "tr": _tr(IYOR("uyanı"))},
    "levantarse": {
        "ru": ru(["встаю", "встаёшь", "встаёт", "встаём", "встают"]),
        "uk": uk(["встаю", "встаєш", "встає", "встаємо", "встають"]),
        "pl": pl(["wstaję", "wstajesz", "wstaje", "wstajemy", "wstają"]),
        "tr": _tr(IYOR("kalkı"))},
    "ducharse": {
        "ru": ru(["принимаю", "принимаешь", "принимает", "принимаем", "принимают"], "душ"),
        "uk": uk(["приймаю", "приймаєш", "приймає", "приймаємо", "приймають"], "душ"),
        "pl": pl(["biorę", "bierzesz", "bierze", "bierzemy", "biorą"], "prysznic"),
        "tr": _tr(IYOR("alı"), "duş")},
    "vestirse": {
        "ru": ru(["одеваюсь", "одеваешься", "одевается", "одеваемся", "одеваются"]),
        "uk": uk(["одягаюся", "одягаєшся", "одягається", "одягаємося", "одягаються"]),
        "pl": pl(["ubieram się", "ubierasz się", "ubiera się", "ubieramy się", "ubierają się"]),
        "tr": _tr(IYOR("giyini"))},
    "desayunar": {
        "ru": ru(["завтракаю", "завтракаешь", "завтракает", "завтракаем", "завтракают"]),
        "uk": uk(["снідаю", "снідаєш", "снідає", "снідаємо", "снідають"]),
        "pl": pl(["jem", "jesz", "je", "jemy", "jedzą"], "śniadanie"),
        "tr": _tr(IYOR("yapı"), "kahvaltı")},
    "ir-trabajo": {
        "ru": ru(["еду", "едешь", "едет", "едем", "едут"], "на работу на метро"),
        "uk": uk(["їду", "їдеш", "їде", "їдемо", "їдуть"], "на роботу метро"),
        "pl": pl(["jadę", "jedziesz", "jedzie", "jedziemy", "jadą"], "do pracy metrem"),
        "tr": _tr(IYOR("gidi"), "metroyla işe")},
    "trabajar-aeropuerto": {
        "ru": ru(["работаю", "работаешь", "работает", "работаем", "работают"], "в аэропорту"),
        "uk": uk(["працюю", "працюєш", "працює", "працюємо", "працюють"], "в аеропорту"),
        "pl": pl(["pracuję", "pracujesz", "pracuje", "pracujemy", "pracują"], "na lotnisku"),
        "tr": _tr(IYOR("çalışı"), "havalimanında")},
    "volver": {
        "ru": ru(["возвращаюсь", "возвращаешься", "возвращается", "возвращаемся", "возвращаются"], "домой"),
        "uk": uk(["повертаюся", "повертаєшся", "повертається", "повертаємося", "повертаються"], "додому"),
        "pl": pl(["wracam", "wracasz", "wraca", "wracamy", "wracają"], "do domu"),
        "tr": _tr(IYOR("dönü"), "eve")},
    "cenar": {
        "ru": ru(["ужинаю", "ужинаешь", "ужинает", "ужинаем", "ужинают"]),
        "uk": uk(["вечеряю", "вечеряєш", "вечеряє", "вечеряємо", "вечеряють"]),
        "pl": pl(["jem", "jesz", "je", "jemy", "jedzą"], "kolację"),
        "tr": _tr(IYOR("yi"), "akşam yemeği")},
    "acostarse": {
        "ru": ru(["ложусь", "ложишься", "ложится", "ложимся", "ложатся"], "спать"),
        "uk": uk(["лягаю", "лягаєш", "лягає", "лягаємо", "лягають"], "спати"),
        "pl": pl(["kładę się", "kładziesz się", "kładzie się", "kładziemy się", "kładą się"], "spać"),
        "tr": _tr(IYOR("yatı"))},
    "correr": {
        "ru": ru(["иду", "идёшь", "идёт", "идём", "идут"], "на пробежку"),
        "uk": uk(["йду", "йдеш", "йде", "йдемо", "йдуть"], "на пробіжку"),
        "pl": pl(["idę", "idziesz", "idzie", "idziemy", "idą"], "pobiegać"),
        "tr": _tr(IYOR("çıkı"), "koşuya")},
    "afeitarse": {
        "ru": ru(["бреюсь", "бреешься", "бреется", "бреемся", "бреются"]),
        "uk": uk(["голюся", "голишся", "голиться", "голимося", "голяться"]),
        "pl": pl(["golę się", "golisz się", "goli się", "golimy się", "golą się"]),
        "tr": _tr(IYOR("olu"), "tıraş")},
    "trabajar-portatil": {
        "ru": ru(["работаю", "работаешь", "работает", "работаем", "работают"], "за ноутбуком"),
        "uk": uk(["працюю", "працюєш", "працює", "працюємо", "працюють"], "за ноутбуком"),
        "pl": pl(["pracuję", "pracujesz", "pracuje", "pracujemy", "pracują"], "na laptopie"),
        "tr": _tr(IYOR("çalışı"), suites=["dizüstü bilgisayarımda", "dizüstü bilgisayarında", "dizüstü bilgisayarında",
                                           "dizüstü bilgisayarımızda", "dizüstü bilgisayarlarında"])},
    "cocinar": {
        "ru": ru(["готовлю", "готовишь", "готовит", "готовим", "готовят"]),
        "uk": uk(["готую", "готуєш", "готує", "готуємо", "готують"]),
        "pl": pl(["gotuję", "gotujesz", "gotuje", "gotujemy", "gotują"]),
        "tr": _tr(IYOR("yapı"), "yemek")},
    "despertar": {
        "ru": ru(["бужу", "будишь", "будит", "будим", "будят"], "Мию"),
        "uk": uk(["буджу", "будиш", "будить", "будимо", "будять"], "Мію"),
        "pl": pl(["budzę", "budzisz", "budzi", "budzimy", "budzą"], "Mię"),
        "tr": _tr(IYOR("uyandırı"), "Mia'yı")},
    "lavarse-dientes": {
        "ru": ru(["чищу", "чистишь", "чистит", "чистим", "чистят"], "зубы"),
        "uk": uk(["чищу", "чистиш", "чистить", "чистимо", "чистять"], "зуби"),
        "pl": pl(["myję", "myjesz", "myje", "myjemy", "myją"], "zęby"),
        "tr": _tr(IYOR("fırçalı"), suites=["dişlerimi", "dişlerini", "dişlerini", "dişlerimizi", "dişlerini"])},
    "peinar": {
        "ru": ru(["причёсываю", "причёсываешь", "причёсывает", "причёсываем", "причёсывают"], "Мию"),
        "uk": uk(["зачісую", "зачісуєш", "зачісує", "зачісуємо", "зачісують"], "Мію"),
        "pl": pl(["czeszę", "czeszesz", "czesze", "czeszemy", "czeszą"], "Mię"),
        "tr": _tr(IYOR("tarı"), "Mia'nın saçını")},
    # l'heure apres le sujet : la phrase finit sur « в детский сад », « до садочка », « do przedszkola »
    "llevar-colegio": {
        "ru": ru(["отвожу", "отводишь", "отводит", "отводим", "отводят"], "Бена в школу, а Мию — в детский сад", True),
        "uk": uk(["відводжу", "відводиш", "відводить", "відводимо", "відводять"], "Бена до школи, а Мію — до садочка", True),
        "pl": pl(["odprowadzam", "odprowadzasz", "odprowadza", "odprowadzamy", "odprowadzają"], "Bena do szkoły, a Mię do przedszkola", True),
        "tr": _tr(IYOR("götürü"), "Ben'i okula, Mia'yı kreşe")},
    "ponerse-pijama": {
        # au pluriel, chacun la sienne : пижамы, піжами, piżamy (relecture a l'aveugle du 14 nov.)
        "ru": ru(["надеваю пижаму", "надеваешь пижаму", "надевает пижаму", "надеваем пижамы", "надевают пижамы"]),
        "uk": uk(["одягаю піжаму", "одягаєш піжаму", "одягає піжаму", "одягаємо піжами", "одягають піжами"]),
        "pl": pl(["zakładam piżamę", "zakładasz piżamę", "zakłada piżamę", "zakładamy piżamy", "zakładają piżamy"]),
        "tr": _tr(IYOR("giyi"), suites=["pijamamı", "pijamanı", "pijamasını", "pijamalarımızı", "pijamalarını"])},
}

# les faits de frequence, dans l'ordre de FREQUENCES (journee.py) ; la cle allemande sert de garde
FREQUENCES = {
    "Anna frühstückt immer zu Hause.": {
        "ru": "Анна всегда завтракает дома.", "uk": "Анна завжди снідає вдома.",
        "pl": "Anna zawsze je śniadanie w domu.", "tr": "Anna kahvaltısını her zaman evde yapar."},
    "Anna fährt nie mit dem Auto zur Arbeit.": {
        "ru": "Анна никогда не ездит на работу на машине.", "uk": "Анна ніколи не їздить на роботу машиною.",
        "pl": "Anna nigdy nie jeździ do pracy samochodem.", "tr": "Anna işe asla arabayla gitmez."},
    "Anna isst manchmal mit ihrer Familie zu Abend.": {
        "ru": "Анна иногда ужинает с семьёй.", "uk": "Анна іноді вечеряє з родиною.",
        "pl": "Anna czasami je kolację z rodziną.", "tr": "Anna bazen ailesiyle akşam yemeği yer."},
    "Mark geht immer joggen.": {
        "ru": "Марк всегда ходит на пробежку.", "uk": "Марк завжди ходить на пробіжку.",
        "pl": "Mark zawsze chodzi biegać.", "tr": "Mark her zaman koşuya çıkar."},
    "Mark rasiert sich manchmal.": {
        "ru": "Марк иногда бреется.", "uk": "Марк іноді голиться.", "pl": "Mark czasami się goli.", "tr": "Mark bazen tıraş olur."},
    "Mark kocht manchmal.": {
        "ru": "Марк иногда готовит.", "uk": "Марк іноді готує.", "pl": "Mark czasami gotuje.", "tr": "Mark bazen yemek yapar."},
    "Mark geht nie früh ins Bett.": {
        "ru": "Марк никогда не ложится спать рано.", "uk": "Марк ніколи не лягає спати рано.",
        "pl": "Mark nigdy nie kładzie się spać wcześnie.", "tr": "Mark asla erken yatmaz."},
    "Ben und Mia putzen sich immer die Zähne.": {
        "ru": "Бен и Мия всегда чистят зубы.", "uk": "Бен і Мія завжди чистять зуби.",
        "pl": "Ben i Mia zawsze myją zęby.", "tr": "Ben ile Mia dişlerini her zaman fırçalar."},
    "Mia kämmt sich nie allein.": {
        "ru": "Мия никогда не причёсывается сама.", "uk": "Мія ніколи не зачісується сама.",
        "pl": "Mia nigdy nie czesze się sama.", "tr": "Mia saçını asla kendi kendine taramaz."},
    "Jan bringt Ben manchmal zur Schule und Mia in die Kita.": {
        "ru": "Ян иногда отводит Бена в школу, а Мию — в детский сад.", "uk": "Ян іноді відводить Бена до школи, а Мію — до садочка.",
        "pl": "Jan czasami odprowadza Bena do szkoły, a Mię do przedszkola.", "tr": "Jan bazen Ben'i okula, Mia'yı kreşe götürür."},
    "Katrin weckt Mia immer.": {
        "ru": "Катрин всегда будит Мию.", "uk": "Катрін завжди будить Мію.", "pl": "Katrin zawsze budzi Mię.",
        "tr": "Katrin Mia'yı her zaman uyandırır."},
    "Ben und Mia gehen nie spät ins Bett.": {
        "ru": "Бен и Мия никогда не ложатся спать поздно.", "uk": "Бен і Мія ніколи не лягають спати пізно.",
        "pl": "Ben i Mia nigdy nie kładą się spać późno.", "tr": "Ben ile Mia asla geç yatmaz."},
}


def appliquer(sujets, personnes, verbes, frequences):
    """Pose les quatre langues dans les tables de journee.py ; une traduction absente arrete le script."""
    for s, t in SUJETS.items():
        sujets[s].update(t)
    personnes.update(PERSONNES)
    for vb, v in verbes.items():
        if vb not in VERBES:
            raise SystemExit("journee, langues natives : le verbe %s n'a pas de traduction" % vb)
        for lg in LANGUES:
            if len(VERBES[vb][lg]) != 5:
                raise SystemExit("journee, langues natives : %s / %s n'a pas cinq personnes" % (vb, lg))
            v[lg] = VERBES[vb][lg]
    for f in frequences:
        if f["dei"] not in FREQUENCES:
            raise SystemExit("journee, langues natives : pas de traduction pour « %s »" % f["dei"])
        f.update(FREQUENCES[f["dei"]])
