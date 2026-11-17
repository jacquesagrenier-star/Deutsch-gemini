# -*- coding: utf-8 -*-
"""« Les métiers » dans les langues d'interface sans phrase traduite jusqu'ici (lot 11 de l'alignement des themes,
16 nov. 2026) : turc, ukrainien, polonais, russe, persan et arabe pour qui apprend l'allemand, et l'arabe pour qui
apprend l'espagnol.

LE CHEMIN NATIF : metiers.py fabrique chaque phrase par sorte (le metier, « je suis », ou, ce qu'il fait, « als », la
paire masculin -> feminin) et la decrit a rendre() ; ici, la grammaire de chaque langue la refait :
  - le metier SANS article, comme en allemand : « Diego doktor. », « Дієго — лікар. », « Diego jest lekarzem. »
    (l'instrumental polonais), « دیه‌گو پزشک است. », « دييغو طبيب. » ; avec un adjectif, l'article indefini revient
    la ou la langue en a un (« iyi bir doktor ») ;
  - « als » : l'instrumental slave (« працює лікарем », « работает врачом »), « jako » + nominatif en polonais,
    « olarak » en turc, « به‌عنوان » en persan, l'accusatif d'etat en arabe (« يعمل طبيبًا ») ;
  - l'arabe accorde le verbe au sexe de la personne (VSO, comme les lots precedents) ; le russe accorde l'adjectif au
    genre du NOM (« хороший врач » pour une femme medecin, « хорошая учительница ») ;
  - les noms des metiers suivent les gloses du corpus (themes.json), que la page montre a cote ; quand une langue n'a
    qu'un mot pour les deux sexes (turc, persan, le russe « врач »), la paire le dit (« erkek doktor → kadın doktor »).
Les prenoms sont translitteres en ukrainien, russe, persan et arabe, comme dans les lots 6 a 10.

Points douteux : retours/A-RELIRE-THEMES-<LG>.md (a relire par un natif).
"""

LANGUES = ("tr", "uk", "pl", "ru", "fa", "ar")

NOMS = {
    "uk": {"Diego": "Дієго", "Pablo": "Пабло", "Ines": "Інес", "Marta": "Марта", "Javier": "Хавʼєр", "Elena": "Елена",
           "Tomas": "Томас", "Rosa": "Роза", "Carmen": "Кармен", "Lucas": "Лукас"},
    "ru": {"Diego": "Диего", "Pablo": "Пабло", "Ines": "Инес", "Marta": "Марта", "Javier": "Хавьер", "Elena": "Елена",
           "Tomas": "Томас", "Rosa": "Роза", "Carmen": "Кармен", "Lucas": "Лукас"},
    "fa": {"Diego": "دیه‌گو", "Pablo": "پابلو", "Ines": "اینس", "Marta": "مارتا", "Javier": "خاویر", "Elena": "النا",
           "Tomas": "توماس", "Rosa": "روزا", "Carmen": "کارمن", "Lucas": "لوکاس"},
    "ar": {"Diego": "دييغو", "Pablo": "بابلو", "Ines": "إينيس", "Marta": "مارتا", "Javier": "خافيير", "Elena": "إيلينا",
           "Tomas": "توماس", "Rosa": "روزا", "Carmen": "كارمن", "Lucas": "لوكاس"},
}

# LES METIERS. Par langue : (masculin, feminin).
#   tr : le mot (un seul pour les deux sexes) et sa forme « je suis » (« doktorum ») -- (mot, ben)
#   uk, ru : (nominatif, instrumental) ; ru porte aussi le genre du NOM feminin (« f » ou « m » : врач reste masculin)
#   pl : (nominatif, instrumental)
#   fa : le mot (un seul)
#   ar : (indefini, defini, accusatif d'etat)
MET = {
    "arzt": {
        "tr": ("doktor", "doktorum"),
        "uk": (("лікар", "лікарем"), ("лікарка", "лікаркою")),
        "ru": (("врач", "врачом"), ("врач", "врачом", "m")),
        "pl": (("lekarz", "lekarzem"), ("lekarka", "lekarką")),
        "fa": "پزشک",
        "ar": (("طبيب", "الطبيب", "طبيبًا"), ("طبيبة", "الطبيبة", "طبيبةً"))},
    "apotheker": {
        "tr": ("eczacı", "eczacıyım"),
        "uk": (("фармацевт", "фармацевтом"), ("фармацевтка", "фармацевткою")),
        "ru": (("фармацевт", "фармацевтом"), ("фармацевт", "фармацевтом", "m")),
        "pl": (("farmaceuta", "farmaceutą"), ("farmaceutka", "farmaceutką")),
        "fa": "داروساز",
        "ar": (("صيدلي", "الصيدلي", "صيدليًّا"), ("صيدلانية", "الصيدلانية", "صيدلانيةً"))},
    "baecker": {
        "tr": ("fırıncı", "fırıncıyım"),
        "uk": (("пекар", "пекарем"), ("пекарка", "пекаркою")),
        "ru": (("пекарь", "пекарем"), ("пекарь", "пекарем", "m")),
        "pl": (("piekarz", "piekarzem"), ("piekarka", "piekarką")),
        "fa": "نانوا",
        "ar": (("خبّاز", "الخبّاز", "خبّازًا"), ("خبّازة", "الخبّازة", "خبّازةً"))},
    "friseur": {
        "tr": ("kuaför", "kuaförüm"),
        "uk": (("перукар", "перукарем"), ("перукарка", "перукаркою")),
        "ru": (("парикмахер", "парикмахером"), ("парикмахер", "парикмахером", "m")),
        "pl": (("fryzjer", "fryzjerem"), ("fryzjerka", "fryzjerką")),
        "fa": "آرایشگر",
        "ar": (("حلّاق", "الحلّاق", "حلّاقًا"), ("مصفّفة شعر", "مصفّفة الشعر", "مصفّفةَ شعر"))},
    "lehrer": {
        "tr": ("öğretmen", "öğretmenim"),
        "uk": (("учитель", "учителем"), ("учителька", "учителькою")),
        "ru": (("учитель", "учителем"), ("учительница", "учительницей", "f")),
        "pl": (("nauczyciel", "nauczycielem"), ("nauczycielka", "nauczycielką")),
        "fa": "معلم",
        "ar": (("معلّم", "المعلّم", "معلّمًا"), ("معلّمة", "المعلّمة", "معلّمةً"))},
    "kellner": {
        "tr": ("garson", "garsonum"),
        "uk": (("офіціант", "офіціантом"), ("офіціантка", "офіціанткою")),
        "ru": (("официант", "официантом"), ("официантка", "официанткой", "f")),
        "pl": (("kelner", "kelnerem"), ("kelnerka", "kelnerką")),
        "fa": "پیشخدمت",
        "ar": (("نادل", "النادل", "نادلًا"), ("نادلة", "النادلة", "نادلةً"))},
    "koch": {
        "tr": ("aşçı", "aşçıyım"),
        "uk": (("кухар", "кухарем"), ("кухарка", "кухаркою")),
        "ru": (("повар", "поваром"), ("повар", "поваром", "m")),
        "pl": (("kucharz", "kucharzem"), ("kucharka", "kucharką")),
        "fa": "آشپز",
        "ar": (("طبّاخ", "الطبّاخ", "طبّاخًا"), ("طبّاخة", "الطبّاخة", "طبّاخةً"))},
    "mechaniker": {
        "tr": ("tamirci", "tamirciyim"),
        "uk": (("механік", "механіком"), ("механікиня", "механікинею")),
        "ru": (("механик", "механиком"), ("механик", "механиком", "m")),
        "pl": (("mechanik", "mechanikiem"), ("mechaniczka", "mechaniczką")),
        "fa": "مکانیک",
        "ar": (("ميكانيكي", "الميكانيكي", "ميكانيكيًّا"), ("ميكانيكية", "الميكانيكية", "ميكانيكيةً"))},
    "verkaeufer": {
        "tr": ("satıcı", "satıcıyım"),
        "uk": (("продавець", "продавцем"), ("продавчиня", "продавчинею")),
        "ru": (("продавец", "продавцом"), ("продавщица", "продавщицей", "f")),
        "pl": (("sprzedawca", "sprzedawcą"), ("sprzedawczyni", "sprzedawczynią")),
        "fa": "فروشنده",
        "ar": (("بائع", "البائع", "بائعًا"), ("بائعة", "البائعة", "بائعةً"))},
    "polizist": {
        "tr": ("polis memuru", "polis memuruyum"),
        "uk": (("поліцейський", "поліцейським"), ("поліцейська", "поліцейською")),
        "ru": (("полицейский", "полицейским"), ("сотрудница полиции", "сотрудницей полиции", "f")),
        "pl": (("policjant", "policjantem"), ("policjantka", "policjantką")),
        "fa": "پلیس",
        "ar": (("شرطي", "الشرطي", "شرطيًّا"), ("شرطية", "الشرطية", "شرطيةً"))},
    "pfleger": {
        "tr": ("hemşire", "hemşireyim"),
        "uk": (("медбрат", "медбратом"), ("медсестра", "медсестрою")),
        "ru": (("медбрат", "медбратом"), ("медсестра", "медсестрой", "f")),
        "pl": (("pielęgniarz", "pielęgniarzem"), ("pielęgniarka", "pielęgniarką")),
        "fa": "پرستار",
        "ar": (("ممرّض", "الممرّض", "ممرّضًا"), ("ممرّضة", "الممرّضة", "ممرّضةً"))},
    "rezeptionist": {
        "tr": ("resepsiyonist", "resepsiyonistim"),
        "uk": (("адміністратор", "адміністратором"), ("адміністраторка", "адміністраторкою")),
        "ru": (("администратор", "администратором"), ("администратор", "администратором", "m")),
        "pl": (("recepcjonista", "recepcjonistą"), ("recepcjonistka", "recepcjonistką")),
        "fa": "مسئول پذیرش",
        "ar": (("موظّف استقبال", "موظّف الاستقبال", "موظّفَ استقبال"), ("موظّفة استقبال", "موظّفة الاستقبال", "موظّفةَ استقبال"))},
}

# LES LIEUX : « ... travaille dans une pharmacie » (le complement de lieu tel qu'il suit le verbe)
LIEUX = {
    "praxis":      {"tr": "muayenehanede", "uk": "у лікарському кабінеті", "pl": "w gabinecie lekarskim", "ru": "во врачебном кабинете", "fa": "در مطب", "ar": "في عيادة"},
    "krankenhaus": {"tr": "hastanede", "uk": "у лікарні", "pl": "w szpitalu", "ru": "в больнице", "fa": "در بیمارستان", "ar": "في المستشفى"},
    "apotheke":    {"tr": "eczanede", "uk": "в аптеці", "pl": "w aptece", "ru": "в аптеке", "fa": "در داروخانه", "ar": "في صيدلية"},
    "baeckerei":   {"tr": "fırında", "uk": "у пекарні", "pl": "w piekarni", "ru": "в пекарне", "fa": "در نانوایی", "ar": "في مخبز"},
    "salon":       {"tr": "kuaför salonunda", "uk": "у перукарні", "pl": "w salonie fryzjerskim", "ru": "в парикмахерской", "fa": "در آرایشگاه", "ar": "في صالون تصفيف الشعر"},
    "schule":      {"tr": "okulda", "uk": "у школі", "pl": "w szkole", "ru": "в школе", "fa": "در مدرسه", "ar": "في مدرسة"},
    "restaurant":  {"tr": "restoranda", "uk": "у ресторані", "pl": "w restauracji", "ru": "в ресторане", "fa": "در رستوران", "ar": "في مطعم"},
    "kueche":      {"tr": "mutfakta", "uk": "на кухні", "pl": "w kuchni", "ru": "на кухне", "fa": "در آشپزخانه", "ar": "في المطبخ"},
    "werkstatt":   {"tr": "tamirhanede", "uk": "у майстерні", "pl": "w warsztacie", "ru": "в мастерской", "fa": "در تعمیرگاه", "ar": "في ورشة تصليح"},
    "geschaeft":   {"tr": "dükkânda", "uk": "у магазині", "pl": "w sklepie", "ru": "в магазине", "fa": "در مغازه", "ar": "في متجر"},
    "polizei":     {"tr": "emniyette", "uk": "у поліції", "pl": "w policji", "ru": "в полиции", "fa": "در پلیس", "ar": "في الشرطة"},
    "hotel":       {"tr": "otelde", "uk": "у готелі", "pl": "w hotelu", "ru": "в гостинице", "fa": "در هتل", "ar": "في فندق"},
}
# « en la comisaría » (qui apprend l'espagnol) : le poste, pas la police
LIEUX_ES_AR = {"polizei": "في مركز الشرطة"}

# CE QU'IL FAIT : le groupe verbal a la 3e personne ; ar : (verbe au masculin, reste) -- le feminin prend « ت »
ACT = {
    "arzt":         {"tr": "hastaları muayene ediyor", "uk": "оглядає пацієнтів", "pl": "bada pacjentów", "ru": "осматривает пациентов", "fa": "بیماران را معاینه می‌کند", "ar": ("يفحص", "المرضى")},
    "apotheker":    {"tr": "ilaç satıyor", "uk": "продає ліки", "pl": "sprzedaje leki", "ru": "продаёт лекарства", "fa": "دارو می‌فروشد", "ar": ("يبيع", "الأدوية")},
    "baecker":      {"tr": "ekmek pişiriyor", "uk": "пече хліб", "pl": "piecze chleb", "ru": "печёт хлеб", "fa": "نان می‌پزد", "ar": ("يخبز", "الخبز")},
    "friseur":      {"tr": "saç kesiyor", "uk": "стриже волосся", "pl": "strzyże włosy", "ru": "стрижёт волосы", "fa": "مو کوتاه می‌کند", "ar": ("يقصّ", "الشعر")},
    "lehrer":       {"tr": "çocuklara ders veriyor", "uk": "навчає дітей", "pl": "uczy dzieci", "ru": "учит детей", "fa": "به بچه‌ها درس می‌دهد", "ar": ("يعلّم", "الأطفال")},
    "s-lehrer":     {"tr": "İspanyolca öğretiyor", "uk": "викладає іспанську", "pl": "uczy hiszpańskiego", "ru": "преподаёт испанский", "fa": "اسپانیایی درس می‌دهد", "ar": ("يعلّم", "الإسبانية")},
    "kellner":      {"tr": "yemeği getiriyor", "uk": "приносить їжу", "pl": "przynosi jedzenie", "ru": "приносит еду", "fa": "غذا را می‌آورد", "ar": ("يقدّم", "الطعام")},
    "koch":         {"tr": "misafirler için yemek pişiriyor", "uk": "готує для гостей", "pl": "gotuje dla gości", "ru": "готовит для гостей", "fa": "برای مهمان‌ها غذا می‌پزد", "ar": ("يطبخ", "للضيوف")},
    "mechaniker":   {"tr": "bisiklet tamir ediyor", "uk": "ремонтує велосипеди", "pl": "naprawia rowery", "ru": "ремонтирует велосипеды", "fa": "دوچرخه تعمیر می‌کند", "ar": ("يصلح", "الدراجات")},
    "verkaeufer":   {"tr": "kıyafet satıyor", "uk": "продає одяг", "pl": "sprzedaje ubrania", "ru": "продаёт одежду", "fa": "لباس می‌فروشد", "ar": ("يبيع", "الملابس")},
    "polizist":     {"tr": "trafiği yönetiyor", "uk": "регулює рух", "pl": "kieruje ruchem", "ru": "регулирует движение", "fa": "ترافیک را هدایت می‌کند", "ar": ("ينظّم", "حركة المرور")},
    "pfleger":      {"tr": "hastalara bakıyor", "uk": "доглядає за хворими", "pl": "opiekuje się chorymi", "ru": "ухаживает за больными", "fa": "از بیماران مراقبت می‌کند", "ar": ("يعتني", "بالمرضى")},
    "rezeptionist": {"tr": "misafirlere anahtarı veriyor", "uk": "дає гостям ключ", "pl": "daje gościom klucz", "ru": "даёт гостям ключ", "fa": "کلید را به مهمان‌ها می‌دهد", "ar": ("يعطي", "الضيوف المفتاح")},
}
# l'espagnol dit « cocina para los clientes » : les clients, pas les invites
ACT_ES_AR = {"koch": ("يطبخ", "للزبائن")}

PRON = {"tr": ("O", "O"), "uk": ("Він", "Вона"), "ru": ("Он", "Она"), "pl": ("On", "Ona"), "fa": ("او", "او"), "ar": ("هو", "هي")}
BON = {"uk": ("хороший", "хороша"), "ru": ("хороший", "хорошая"), "pl": ("dobrym", "dobrą"), "ar": ("جيد", "جيدة")}


def _maj(t):
    return t[0].upper() + t[1:]


def _ezafe_fa(mot):
    """Le nom persan devant son adjectif : « نانوا » prend « ی » (نانوای خوب), les autres l'ezafe muette."""
    return mot + "ی" if mot.endswith(("ا", "و")) else mot


def _verbe_ar(v, s):
    return ("ت" + v[1:]) if s == "f" else v


def _sujet(lg, n, pron_ok=True):
    """Le sujet d'une phrase sur le metier : le prenom, sinon le pronom."""
    if n.get("pid") in NOMS.get(lg, {}):
        return NOMS[lg][n["pid"]], True
    if n.get("nom"):
        return n["nom"], True
    return PRON[lg][0 if n["s"] == "m" else 1], False


def _mot(lg, met, s, cas=0):
    """Le metier : cas 0 = nominatif (indefini en arabe), 1 = instrumental / defini, 2 = accusatif d'etat (arabe)."""
    m = MET[met][lg]
    if lg in ("tr",):
        return m[0]
    if lg == "fa":
        return m
    return m[0 if s == "m" else 1][cas]


def _ru_genre(met, s):
    return "m" if s == "m" else MET[met]["ru"][1][2]


def rendre(lg, app, n):
    """La phrase n (une sorte et ses parties, voir metiers.py) dans la langue lg."""
    k, met, s = n["k"], n.get("met"), n.get("s")
    G = 0 if s == "m" else 1
    if k == "est":                                       # « Diego ist Arzt. » / « Sie ist Ärztin. »
        S, nomme = _sujet(lg, n)
        if lg == "tr": return "%s %s." % (S, _mot(lg, met, s))
        if lg in ("uk", "ru"): return ("%s — %s." if nomme else "%s %s.") % (S, _mot(lg, met, s))
        if lg == "pl": return "%s jest %s." % (S, _mot(lg, met, s, 1))
        if lg == "fa": return "%s %s است." % (S, _mot(lg, met, s))
        if lg == "ar": return "%s %s." % (S, _mot(lg, met, s))
    if k == "bon":                                       # « Diego ist ein guter Arzt. »
        S, nomme = _sujet(lg, n)
        if lg == "tr": return "%s iyi bir %s." % (S, _mot(lg, met, s))
        if lg == "uk": return ("%s — %s %s." if nomme else "%s %s %s.") % (S, BON["uk"][G], _mot(lg, met, s))
        if lg == "ru":
            b = BON["ru"][0 if _ru_genre(met, s) == "m" else 1]
            return ("%s — %s %s." if nomme else "%s %s %s.") % (S, b, _mot(lg, met, s))
        if lg == "pl": return "%s jest %s %s." % (S, BON["pl"][G], _mot(lg, met, s, 1))
        if lg == "fa": return "%s %s خوبی است." % (S, _ezafe_fa(_mot(lg, met, s)))
        if lg == "ar": return "%s %s %s." % (S, _mot(lg, met, s), BON["ar"][G])
    if k == "je":                                        # « Ich bin Ärztin. »
        if lg == "tr": return "Ben %s." % MET[met]["tr"][1]
        if lg in ("uk", "ru"): return "Я %s." % _mot(lg, met, s)
        if lg == "pl": return "Jestem %s." % _mot(lg, met, s, 1)
        if lg == "fa": return "من %s هستم." % _mot(lg, met, s)
        if lg == "ar": return "أنا %s." % _mot(lg, met, s)
    if k == "ou":                                        # « Sie arbeitet in einer Praxis. »
        S, nomme = _sujet(lg, n)
        loc = (LIEUX_ES_AR.get(n["lieu"]) if (app == "es" and lg == "ar") else None) or LIEUX[n["lieu"]][lg]
        if lg == "tr": return "%s %s çalışıyor." % (S, loc)
        if lg == "uk": return "%s працює %s." % (S, loc)
        if lg == "ru": return "%s работает %s." % (S, loc)
        if lg == "pl": return "%s pracuje %s." % (S, loc)
        if lg == "fa": return "%s %s کار می‌کند." % (S, loc)
        if lg == "ar":
            v = _verbe_ar("يعمل", s)
            return ("%s %s %s." % (v, S, loc)) if nomme else "%s %s." % (v, loc)
    if k == "fait":                                      # « Pablo backt Brot. » / « Die Ärztin untersucht die Patienten. »
        a = n["act"]
        if lg == "ar" and app == "es" and a in ACT_ES_AR:
            act = ACT_ES_AR[a]
        else:
            act = ACT[a][lg]
        if n.get("pid") in NOMS.get(lg, {}) or n.get("nom"):
            S = _sujet(lg, n)[0]
        else:                                            # une personne des scenes : « la medecin »
            S = _mot(lg, met, s, 1) if lg == "ar" else _maj(_mot(lg, met, s))
        if lg == "ar":
            return "%s %s %s." % (_verbe_ar(act[0], s), S, act[1])
        return "%s %s." % (S, act)
    if k == "comme":                                     # « Pablo arbeitet als Bäcker. »
        S, nomme = _sujet(lg, n)
        if lg == "tr": return "%s %s olarak çalışıyor." % (S, _mot(lg, met, s))
        if lg == "uk": return "%s працює %s." % (S, _mot(lg, met, s, 1))
        if lg == "ru": return "%s работает %s." % (S, _mot(lg, met, s, 1))
        if lg == "pl": return "%s pracuje jako %s." % (S, _mot(lg, met, s))
        if lg == "fa": return "%s به‌عنوان %s کار می‌کند." % (S, _mot(lg, met, s))
        if lg == "ar":
            v = _verbe_ar("يعمل", s)
            return ("%s %s %s." % (v, S, _mot(lg, met, s, 2))) if nomme else "%s %s." % (v, _mot(lg, met, s, 2))
    if k == "paire":                                     # « der Arzt → die Ärztin » (et l'inverse)
        a, b = n["de"], n["vers"]
        return seul(lg, met, a) + " → " + seul(lg, met, b)
    raise ValueError("sorte inconnue : %r" % (n,))


def seul(lg, met, s):
    """Le metier seul, pour la paire et pour le choix traduit : le sexe dit quand la langue n'a qu'un mot."""
    if lg == "tr":
        return ("erkek " if s == "m" else "kadın ") + MET[met]["tr"][0]
    if lg == "fa":
        return _ezafe_fa(MET[met]["fa"]) + (" مرد" if s == "m" else " زن")
    if lg == "ru":
        m, f = MET[met]["ru"][0][0], MET[met]["ru"][1][0]
        if m == f:
            return m + (" (мужчина)" if s == "m" else " (женщина)")
    return _mot(lg, met, s)
