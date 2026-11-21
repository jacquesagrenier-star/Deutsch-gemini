# -*- coding: utf-8 -*-
"""Ce que les etoiles racontent dans Ton ciel (ligne 160, livraison B, decision de Jacques du 20 nov. 2026).

    python etoiles/outils/infos.py

Ecrit etoiles/infos/<langue>.json, un fichier par langue d'interface (DERIVE : jamais a la main), charge par Ton ciel seulement, a partir de :
  - etoiles/outils/origines.txt : l'origine du nom de chaque etoile nommee, a nos mots, d'apres le catalogue de l'UAI
    tenu par le WGSN (etoiles/sources/wgsn_origines.tsv) ; une etoile sans origine sure n'a pas de ligne ;
  - etoiles/sources/simbad_types.tsv et simbad_diametres.tsv (SIMBAD, releve de etoiles/outils/simbad_portrait.py) :
    le type spectral de chaque etoile (sa couleur, sa classe : supergeante, geante, sous-geante, etoile) et, quand il a
    ete mesure, son diametre rapporte a celui du Soleil ;
  - etoiles/outils/histoires.txt : la petite histoire de chaque constellation, a nos mots, d'apres Ian Ridpath, Star
    Tales (sources par figure dans etoiles/sources/histoires_sources.tsv).
Les phrases du portrait sont des gabarits (TEXTES ci-dessous), composees par l'app : le nombre est ecrit par elle, a la
mode de la langue. Traductions hors fr et en : a relire par des natifs (retours/A-RELIRE-ETOILES.md, section 5).
"""
import csv
import json
import os
import re
import statistics

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
LANGUES = ["fr", "en", "de", "es", "pt", "tr", "uk", "ru", "pl", "ar", "fa"]
R_SOLEIL_KM = 695700.0

# --- l'origine : le prefixe par langue d'origine, puis le sens entre guillemets (q) ou une description (d)
PREFIXES = {
    "fr": {"ar": "De l'arabe", "grc": "Du grec ancien", "la": "Du latin", "fa": "Du persan", "sux": "Du sumérien", "sa": "Du sanskrit",
           "wrr": "Du wardaman (Australie)", "yua": "Du maya yucatèque", "zh": "Du chinois", "haw": "De l'hawaïen",
           "naq": "Du khoekhoe (Afrique australe)", "non": "Du vieux norrois", "pmt": "Du tuamotu (Polynésie)", "en": "De l'anglais",
           "tr": "Du turc", "mod": "Un nom moderne"},
    "en": {"ar": "From Arabic", "grc": "From Ancient Greek", "la": "From Latin", "fa": "From Persian", "sux": "From Sumerian", "sa": "From Sanskrit",
           "wrr": "From Wardaman (Australia)", "yua": "From Yucatec Maya", "zh": "From Chinese", "haw": "From Hawaiian",
           "naq": "From Khoekhoe (southern Africa)", "non": "From Old Norse", "pmt": "From Tuamotuan (Polynesia)", "en": "From English",
           "tr": "From Turkish", "mod": "A modern name"},
    "de": {"ar": "Aus dem Arabischen", "grc": "Aus dem Altgriechischen", "la": "Aus dem Lateinischen", "fa": "Aus dem Persischen",
           "sux": "Aus dem Sumerischen", "sa": "Aus dem Sanskrit", "wrr": "Aus dem Wardaman (Australien)", "yua": "Aus dem yukatekischen Maya",
           "zh": "Aus dem Chinesischen", "haw": "Aus dem Hawaiischen", "naq": "Aus dem Khoekhoe (südliches Afrika)", "non": "Aus dem Altnordischen",
           "pmt": "Aus dem Tuamotu (Polynesien)", "en": "Aus dem Englischen", "tr": "Aus dem Türkischen", "mod": "Ein moderner Name"},
    "es": {"ar": "Del árabe", "grc": "Del griego antiguo", "la": "Del latín", "fa": "Del persa", "sux": "Del sumerio", "sa": "Del sánscrito",
           "wrr": "Del wardaman (Australia)", "yua": "Del maya yucateco", "zh": "Del chino", "haw": "Del hawaiano",
           "naq": "Del joijói (sur de África)", "non": "Del nórdico antiguo", "pmt": "Del tuamotu (Polinesia)", "en": "Del inglés",
           "tr": "Del turco", "mod": "Un nombre moderno"},
    "pt": {"ar": "Do árabe", "grc": "Do grego antigo", "la": "Do latim", "fa": "Do persa", "sux": "Do sumério", "sa": "Do sânscrito",
           "wrr": "Do wardaman (Austrália)", "yua": "Do maia iucateque", "zh": "Do chinês", "haw": "Do havaiano",
           "naq": "Do khoekhoe (sul da África)", "non": "Do nórdico antigo", "pmt": "Do tuamotu (Polinésia)", "en": "Do inglês",
           "tr": "Do turco", "mod": "Um nome moderno"},
    "tr": {"ar": "Arapçadan", "grc": "Eski Yunancadan", "la": "Latinceden", "fa": "Farsçadan", "sux": "Sümerceden", "sa": "Sanskritçeden",
           "wrr": "Wardaman dilinden (Avustralya)", "yua": "Yukatek Mayacasından", "zh": "Çinceden", "haw": "Hawaii dilinden",
           "naq": "Khoekhoe dilinden (Güney Afrika)", "non": "Eski İskandinavcadan", "pmt": "Tuamotu dilinden (Polinezya)", "en": "İngilizceden",
           "tr": "Türkçeden", "mod": "Modern bir ad"},
    "uk": {"ar": "З арабської", "grc": "З давньогрецької", "la": "З латини", "fa": "З перської", "sux": "З шумерської", "sa": "Із санскриту",
           "wrr": "З мови вардаман (Австралія)", "yua": "З юкатекської мови мая", "zh": "З китайської", "haw": "З гавайської",
           "naq": "З мови кхойкхой (Південна Африка)", "non": "З давньоскандинавської", "pmt": "З мови туамоту (Полінезія)",
           "en": "З англійської", "tr": "З турецької", "mod": "Сучасна назва"},
    "ru": {"ar": "С арабского", "grc": "С древнегреческого", "la": "С латыни", "fa": "С персидского", "sux": "С шумерского", "sa": "С санскрита",
           "wrr": "С языка вардаман (Австралия)", "yua": "С юкатекского языка майя", "zh": "С китайского", "haw": "С гавайского",
           "naq": "С языка кхойкхой (Южная Африка)", "non": "С древнескандинавского", "pmt": "С языка туамоту (Полинезия)",
           "en": "С английского", "tr": "С турецкого", "mod": "Современное название"},
    "pl": {"ar": "Z arabskiego", "grc": "Ze starogreckiego", "la": "Z łaciny", "fa": "Z perskiego", "sux": "Z sumeryjskiego", "sa": "Z sanskrytu",
           "wrr": "Z języka wardaman (Australia)", "yua": "Z języka maja jukatańskiego", "zh": "Z chińskiego", "haw": "Z hawajskiego",
           "naq": "Z języka khoekhoe (Afryka Południowa)", "non": "Ze staronordyckiego", "pmt": "Z języka tuamotu (Polinezja)",
           "en": "Z angielskiego", "tr": "Z tureckiego", "mod": "Nazwa współczesna"},
    "ar": {"ar": "من العربية", "grc": "من اليونانية القديمة", "la": "من اللاتينية", "fa": "من الفارسية", "sux": "من السومرية", "sa": "من السنسكريتية",
           "wrr": "من لغة الوردمان (أستراليا)", "yua": "من لغة المايا اليوكاتيكية", "zh": "من الصينية", "haw": "من لغة هاواي",
           "naq": "من لغة الخويخوي (جنوب أفريقيا)", "non": "من الإسكندنافية القديمة", "pmt": "من لغة تواموتو (بولينيزيا)",
           "en": "من الإنجليزية", "tr": "من التركية", "mod": "اسم حديث"},
    "fa": {"ar": "از عربی", "grc": "از یونانی باستان", "la": "از لاتین", "fa": "از فارسی", "sux": "از سومری", "sa": "از سانسکریت",
           "wrr": "از زبان واردامان (استرالیا)", "yua": "از مایای یوکاتکی", "zh": "از چینی", "haw": "از هاوایی",
           "naq": "از زبان خویخوی (جنوب آفریقا)", "non": "از نورس باستان", "pmt": "از زبان تواموتو (پولینزی)", "en": "از انگلیسی",
           "tr": "از ترکی", "mod": "نامی جدید"},
}
PATRONS = {
    "fr": ("{o} : « {s} ».", "{o} : {s}."), "en": ("{o}: “{s}”.", "{o}: {s}."), "de": ("{o}: „{s}“.", "{o}: {s}."),
    "es": ("{o}: «{s}».", "{o}: {s}."), "pt": ("{o}: “{s}”.", "{o}: {s}."), "tr": ("{o}: “{s}”.", "{o}: {s}."),
    "uk": ("{o}: «{s}».", "{o}: {s}."), "ru": ("{o}: «{s}».", "{o}: {s}."), "pl": ("{o}: „{s}”.", "{o}: {s}."),
    "ar": ("{o}: «{s}».", "{o}: {s}."), "fa": ("{o}: «{s}».", "{o}: {s}."),
}

# --- le portrait : la classe (sg supergeante, g geante, sous sous-geante, e etoile), la couleur, la chaleur, la taille
TEXTES = {
    "fr": {"sg": "une supergéante {c}", "g": "une géante {c}", "sous": "une sous-géante {c}", "e": "une étoile {c}", "genre": "ffff",
           "f": ["bleue", "blanche", "jaune pâle", "jaune", "orange", "rouge"], "m": ["bleu", "blanc", "jaune pâle", "jaune", "orange", "rouge"],
           "temp": ["Sa surface est bien plus chaude que celle du Soleil.", "Sa surface est plus chaude que celle du Soleil.",
                    "Sa surface est un peu plus chaude que celle du Soleil.", "Sa surface est à peu près aussi chaude que celle du Soleil.",
                    "Sa surface est un peu moins chaude que celle du Soleil.", "Sa surface est bien moins chaude que celle du Soleil."],
           "taille": "Environ {n} fois le diamètre du Soleil.", "pareil": "À peu près la taille du Soleil."},
    "en": {"sg": "a {c} supergiant", "g": "a {c} giant", "sous": "a {c} subgiant", "e": "a {c} star", "genre": "mmmm",
           "m": ["blue", "white", "yellow-white", "yellow", "orange", "red"], "f": ["blue", "white", "yellow-white", "yellow", "orange", "red"],
           "temp": ["Its surface is much hotter than the Sun's.", "Its surface is hotter than the Sun's.", "Its surface is a little hotter than the Sun's.",
                    "Its surface is about as hot as the Sun's.", "Its surface is a little cooler than the Sun's.", "Its surface is much cooler than the Sun's."],
           "taille": "About {n} times the Sun's diameter.", "pareil": "About the size of the Sun."},
    "de": {"sg": "ein {c} Überriese", "g": "ein {c} Riese", "sous": "ein {c} Unterriese", "e": "ein {c} Stern", "genre": "mmmm",
           "m": ["blauer", "weißer", "gelblich-weißer", "gelber", "orangefarbener", "roter"], "f": ["blaue", "weiße", "gelblich-weiße", "gelbe", "orangefarbene", "rote"],
           "temp": ["Seine Oberfläche ist viel heißer als die der Sonne.", "Seine Oberfläche ist heißer als die der Sonne.",
                    "Seine Oberfläche ist etwas heißer als die der Sonne.", "Seine Oberfläche ist etwa so heiß wie die der Sonne.",
                    "Seine Oberfläche ist etwas kühler als die der Sonne.", "Seine Oberfläche ist viel kühler als die der Sonne."],
           "taille": "Etwa {n}-mal so groß wie die Sonne.", "pareil": "Etwa so groß wie die Sonne."},
    "es": {"sg": "una supergigante {c}", "g": "una gigante {c}", "sous": "una subgigante {c}", "e": "una estrella {c}", "genre": "ffff",
           "f": ["azul", "blanca", "blanca amarillenta", "amarilla", "naranja", "roja"], "m": ["azul", "blanco", "blanco amarillento", "amarillo", "naranja", "rojo"],
           "temp": ["Su superficie es mucho más caliente que la del Sol.", "Su superficie es más caliente que la del Sol.",
                    "Su superficie es un poco más caliente que la del Sol.", "Su superficie es casi tan caliente como la del Sol.",
                    "Su superficie es un poco menos caliente que la del Sol.", "Su superficie es mucho menos caliente que la del Sol."],
           "taille": "Unas {n} veces el diámetro del Sol.", "pareil": "Más o menos del tamaño del Sol."},
    "pt": {"sg": "uma supergigante {c}", "g": "uma gigante {c}", "sous": "uma subgigante {c}", "e": "uma estrela {c}", "genre": "ffff",
           "f": ["azul", "branca", "branco-amarelada", "amarela", "laranja", "vermelha"], "m": ["azul", "branco", "branco-amarelado", "amarelo", "laranja", "vermelho"],
           "temp": ["Sua superfície é muito mais quente que a do Sol.", "Sua superfície é mais quente que a do Sol.",
                    "Sua superfície é um pouco mais quente que a do Sol.", "Sua superfície é quase tão quente quanto a do Sol.",
                    "Sua superfície é um pouco menos quente que a do Sol.", "Sua superfície é muito menos quente que a do Sol."],
           "taille": "Cerca de {n} vezes o diâmetro do Sol.", "pareil": "Mais ou menos do tamanho do Sol."},
    "tr": {"sg": "{c} bir süperdev", "g": "{c} bir dev", "sous": "{c} bir altdev", "e": "{c} bir yıldız", "genre": "mmmm",
           "m": ["mavi", "beyaz", "sarımsı beyaz", "sarı", "turuncu", "kırmızı"], "f": ["mavi", "beyaz", "sarımsı beyaz", "sarı", "turuncu", "kırmızı"],
           "temp": ["Yüzeyi Güneş'inkinden çok daha sıcak.", "Yüzeyi Güneş'inkinden daha sıcak.", "Yüzeyi Güneş'inkinden biraz daha sıcak.",
                    "Yüzeyi aşağı yukarı Güneş'inki kadar sıcak.", "Yüzeyi Güneş'inkinden biraz daha soğuk.", "Yüzeyi Güneş'inkinden çok daha soğuk."],
           "taille": "Çapı Güneş'inkinin yaklaşık {n} katı.", "pareil": "Aşağı yukarı Güneş büyüklüğünde."},
    "uk": {"sg": "{c} надгігант", "g": "{c} гігант", "sous": "{c} субгігант", "e": "{c} зоря", "genre": "mmmf",
           "m": ["блакитний", "білий", "жовтувато-білий", "жовтий", "помаранчевий", "червоний"], "f": ["блакитна", "біла", "жовтувато-біла", "жовта", "помаранчева", "червона"],
           "temp": ["Поверхня набагато гарячіша, ніж у Сонця.", "Поверхня гарячіша, ніж у Сонця.", "Поверхня трохи гарячіша, ніж у Сонця.",
                    "Поверхня приблизно така ж гаряча, як у Сонця.", "Поверхня трохи холодніша, ніж у Сонця.", "Поверхня набагато холодніша, ніж у Сонця."],
           "taille": "Діаметр: як у Сонця × {n}.", "pareil": "Приблизно розміром із Сонце."},
    "ru": {"sg": "{c} сверхгигант", "g": "{c} гигант", "sous": "{c} субгигант", "e": "{c} звезда", "genre": "mmmf",
           "m": ["голубой", "белый", "желтовато-белый", "жёлтый", "оранжевый", "красный"], "f": ["голубая", "белая", "желтовато-белая", "жёлтая", "оранжевая", "красная"],
           "temp": ["Поверхность намного горячее, чем у Солнца.", "Поверхность горячее, чем у Солнца.", "Поверхность чуть горячее, чем у Солнца.",
                    "Поверхность примерно такая же горячая, как у Солнца.", "Поверхность чуть холоднее, чем у Солнца.", "Поверхность намного холоднее, чем у Солнца."],
           "taille": "Диаметр: как у Солнца × {n}.", "pareil": "Примерно размером с Солнце."},
    "pl": {"sg": "{c} nadolbrzym", "g": "{c} olbrzym", "sous": "{c} podolbrzym", "e": "{c} gwiazda", "genre": "mmmf",
           "m": ["niebieski", "biały", "żółtawobiały", "żółty", "pomarańczowy", "czerwony"], "f": ["niebieska", "biała", "żółtawobiała", "żółta", "pomarańczowa", "czerwona"],
           "temp": ["Powierzchnia jest znacznie gorętsza niż u Słońca.", "Powierzchnia jest gorętsza niż u Słońca.", "Powierzchnia jest nieco gorętsza niż u Słońca.",
                    "Powierzchnia jest mniej więcej tak gorąca jak u Słońca.", "Powierzchnia jest nieco chłodniejsza niż u Słońca.", "Powierzchnia jest znacznie chłodniejsza niż u Słońca."],
           "taille": "Średnica: jak u Słońca × {n}.", "pareil": "Mniej więcej wielkości Słońca."},
    "ar": {"sg": "عملاق فائق {c}", "g": "عملاق {c}", "sous": "نجم شبه عملاق {c}", "e": "نجم {c}", "genre": "mmmm",
           "m": ["أزرق", "أبيض", "أبيض مصفرّ", "أصفر", "برتقالي", "أحمر"], "f": ["زرقاء", "بيضاء", "بيضاء مصفرّة", "صفراء", "برتقالية", "حمراء"],
           "temp": ["سطحه أشدّ حرارة من سطح الشمس بكثير.", "سطحه أشدّ حرارة من سطح الشمس.", "سطحه أشدّ حرارة قليلًا من سطح الشمس.",
                    "سطحه بحرارة سطح الشمس تقريبًا.", "سطحه أبرد قليلًا من سطح الشمس.", "سطحه أبرد بكثير من سطح الشمس."],
           "taille": "قطره يعادل قطر الشمس × {n} تقريبًا.", "pareil": "بحجم الشمس تقريبًا."},
    "fa": {"sg": "ابرغولی {c}", "g": "غولی {c}", "sous": "زیرغولی {c}", "e": "ستاره‌ای {c}", "genre": "mmmm",
           "m": ["آبی", "سفید", "سفیدِ مایل به زرد", "زرد", "نارنجی", "سرخ"], "f": ["آبی", "سفید", "سفیدِ مایل به زرد", "زرد", "نارنجی", "سرخ"],
           "temp": ["سطحش بسیار داغ‌تر از سطح خورشید است.", "سطحش داغ‌تر از سطح خورشید است.", "سطحش کمی داغ‌تر از سطح خورشید است.",
                    "سطحش تقریباً به داغی سطح خورشید است.", "سطحش کمی خنک‌تر از سطح خورشید است.", "سطحش بسیار خنک‌تر از سطح خورشید است."],
           "taille": "قطرش حدود {n} برابر قطر خورشید است.", "pareil": "تقریباً هم‌اندازهٔ خورشید."},
}
CLASSES = ["sg", "g", "sous", "e"]
COULEUR = {"O": 0, "B": 0, "A": 1, "F": 2, "G": 3, "K": 4, "M": 5}
CHALEUR = {"O": 0, "B": 0, "A": 1, "F": 2, "G": 3, "K": 4, "M": 5}


def lire_tsv(chemin):
    with open(chemin, encoding="utf-8") as f:
        return list(csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t"))


def classe_spectrale(s):
    """« K1III », « B8Ia », « A1V+A2Vm », « kA5hF0VmF3 » -> (lettre, classe) ; None si illisible."""
    s = (s or "").strip()
    m = re.match(r"k?([OBAFGKM])[\d.]*\s*(?:h[OBAFGKM][\d.]*)?(?:m[OBAFGKM][\d.]*)?\s*(0|Iab|Ia|Ib|III|II|IV|VI|V|I)?", s)
    if not m:
        return None
    lettre, lum = m.group(1), m.group(2) or ""
    if lum in ("0", "Ia", "Iab", "Ib", "I"):
        cl = "sg"
    elif lum in ("II", "III"):
        cl = "g"
    elif lum == "IV":
        cl = "sous"
    else:
        cl = "e"
    return lettre, cl


def main():
    ciel = json.load(open(os.path.join(RACINE, "ciel.json"), encoding="utf-8"))
    src = json.load(open(os.path.join(RACINE, "sources-etoiles.json"), encoding="utf-8"))["constellations"]
    types = {" ".join(r["designation"].split()): r for r in lire_tsv(os.path.join(RACINE, "sources", "simbad_types.tsv"))}
    diam = {}
    for r in lire_tsv(os.path.join(RACINE, "sources", "simbad_diametres.tsv")):
        diam.setdefault(" ".join(r["designation"].split()), []).append(r)
    # l'origine
    wgsn = {r["nom"]: r for r in lire_tsv(os.path.join(RACINE, "sources", "wgsn_origines.tsv"))}
    origines, sans = {}, []
    for l in open(os.path.join(ICI, "origines.txt"), encoding="utf-8"):
        if not l.strip() or l.startswith("#"):
            continue
        ch = l.rstrip("\n").split("|")
        assert len(ch) == 14, ch[0]
        nom, code, sorte, textes = ch[0], ch[1], ch[2], dict(zip(LANGUES, ch[3:]))
        w = wgsn.get(nom)
        assert w and w["langue"] not in ("absent", "unknown", ""), "origine sans source sure : " + nom
        origines[nom] = {lg: PATRONS[lg][0 if sorte == "q" else 1].format(o=PREFIXES[lg][code], s=textes[lg]) for lg in LANGUES}
    noms = [e["nom"] for c in ciel["constellations"].values() for e in c["etoiles"] if not e.get("noms")]
    sans = [n for n in noms if n not in origines]
    inconnus = [n for n in origines if n not in noms]
    assert not inconnus, inconnus
    # le portrait : « lettre,classe,rapport » par etoile, dans l'ordre des etoiles de chaque figure
    portraits, mesures, illisibles = {}, 0, []
    for cle, c in ciel["constellations"].items():
        lst = []
        for i, e in enumerate(c["etoiles"]):
            d = " ".join(src[cle][i]["simbad"].split())
            t = types.get(d)
            cs = classe_spectrale(t["sp_type"]) if t else None
            if not cs:
                illisibles.append((cle, e["nom"], t and t["sp_type"]))
                lst.append("")
                continue
            # la taille : les diametres en km (physiques) d'abord ; sinon en mas, avec la distance
            rap = None
            vals = [float(x["diameter"]) / 2 / R_SOLEIL_KM for x in diam.get(d, []) if x["unit"].strip() == "km"]
            if not vals:
                vals = [float(x["diameter"]) * (e["al"] / 3.26156) * 0.10751 for x in diam.get(d, []) if x["unit"].strip() == "mas"]
            if vals:
                v = statistics.median(vals)
                if 0.3 < v < 3000:
                    rap = round(v, 1) if v < 10 else int(round(v, -1) if v >= 100 else round(v))
                    mesures += 1
            lst.append("%s,%s,%s" % (cs[0], cs[1], "" if rap is None else rap))
        portraits[cle] = lst
    # l'histoire de chaque figure (quand elle est ecrite)
    histoires = {}
    chemin = os.path.join(ICI, "histoires.txt")
    if os.path.exists(chemin):
        for l in open(chemin, encoding="utf-8"):
            if not l.strip() or l.startswith("#"):
                continue
            ch = l.rstrip("\n").split("|")
            assert len(ch) == 12, ch[0]
            assert ch[0] in ciel["constellations"], ch[0]
            histoires[ch[0]] = dict(zip(LANGUES, ch[1:]))
    textes = {lg: {k: TEXTES[lg][k] for k in ("sg", "g", "sous", "e", "genre", "m", "f", "temp", "taille", "pareil")} for lg in LANGUES}
    sortie = {
        "_lisez_moi": [
            "Ce que les etoiles racontent dans Ton ciel (ligne 160). Fichier DERIVE : python etoiles/outils/infos.py. Ne pas corriger a la main.",
            "origines : l'origine du nom d'une etoile nommee, par langue d'interface (catalogue de l'UAI, WGSN ; Kunitzsch & Smart 2006).",
            "portraits : par figure, dans l'ordre de ses etoiles, « lettre,classe,rapport » : la lettre spectrale (OBAFGKM), la classe "
            "(sg supergeante, g geante, sous sous-geante, e etoile), le diametre rapporte au Soleil s'il est mesure (SIMBAD). Vide : type illisible.",
            "textes : les gabarits du portrait par langue ; m / f : les six couleurs (bleu, blanc, jaune pale, jaune, orange, rouge) au genre de la classe (genre : sg g sous e).",
            "histoires : la petite histoire de chaque figure, montree quand elle est complete (d'apres Ian Ridpath, Star Tales).",
        ],
        "origines": origines,
        "portraits": portraits,
        "textes": textes,
        "histoires": histoires,
    }
    # Un fichier par langue d'interface (environ 30 ko chacun, au lieu de 310 ko pour tout) : Ton ciel ne charge que le sien.
    dossier = os.path.join(RACINE, "infos")
    os.makedirs(dossier, exist_ok=True)
    for lg in LANGUES:
        un = {"_lisez_moi": sortie["_lisez_moi"], "langue": lg,
              "origines": {n: v[lg] for n, v in origines.items()}, "portraits": portraits, "textes": textes[lg],
              "histoires": {k: v[lg] for k, v in histoires.items()}}
        with open(os.path.join(dossier, lg + ".json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(un, f, ensure_ascii=False, separators=(",", ":"))
            f.write("\n")
    print("origines %d (sans ligne : %d, %s) ; portraits %d etoiles, %d tailles mesurees, illisibles %s ; histoires %d / %d" % (
        len(origines), len(sans), sans, sum(len(v) for v in portraits.values()), mesures, illisibles, len(histoires), len(ciel["constellations"])))


if __name__ == "__main__":
    main()
