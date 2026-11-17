# -*- coding: utf-8 -*-
"""Les animaux dans les langues d'interface sans phrase traduite jusqu'ici (lot 13, 16 nov. 2026) : turc, ukrainien,
polonais, russe, persan et arabe pour qui apprend l'allemand, et l'arabe pour qui apprend l'espagnol.

Chaque phrase est refaite par la grammaire de sa langue, a partir de la cle de animales.py (« hab|kuh|bauernhof|sg »),
jamais calquee sur le francais :
- turc : pas d'article, le singulier apres un nombre (« iki inek »), l'ablatif de la comparaison (« ayıdan küçüktür ») ;
- ukrainien, russe, polonais : le genre de l'animal accorde la couleur et le comparatif (« Білка менша за ведмедя »,
  « Wiewiórka jest mniejsza od niedźwiedzia », « Белка меньше медведя »), la forme apres deux (« дві корови »,
  « два медведя »), le pronom de la seconde phrase de la decouverte ; une vache, un chien, un chat n'ont pas le meme
  genre d'une langue a l'autre (собака est masculin en ukrainien, feminin en russe) ;
- persan : le singulier apres un nombre, l'ezafe de « گربهٔ » ;
- arabe : le verbe d'abord, accorde (« تعيش البقرة »), le pluriel non humain au feminin singulier (« تعيش الأبقار »),
  le duel (« بقرتان »), « هذا / هذه ».
Appele par animales.py (ecrire_json) ; les points douteux : retours/A-RELIRE-THEMES-<LG>.md.
"""

LANGUES = ("tr", "uk", "pl", "ru", "fa", "ar")

# --- LES ANIMAUX -------------------------------------------------------------------------------------------------
# tr : (singulier, pluriel, ablatif)
TR = {"kuh": ("inek", "inekler", "inekten"), "pferd": ("at", "atlar", "attan"), "schwein": ("domuz", "domuzlar", "domuzdan"),
      "schaf": ("koyun", "koyunlar", "koyundan"), "huhn": ("tavuk", "tavuklar", "tavuktan"), "hund": ("köpek", "köpekler", "köpekten"),
      "katze": ("kedi", "kediler", "kediden"), "goldfisch": ("japon balığı", "japon balıkları", "japon balığından"),
      "baer": ("ayı", "ayılar", "ayıdan"), "fuchs": ("tilki", "tilkiler", "tilkiden"), "eichhoernchen": ("sincap", "sincaplar", "sincaptan"),
      "vogel": ("kuş", "kuşlar", "kuştan"), "fisch": ("balık", "balıklar", "balıktan"), "delfin": ("yunus", "yunuslar", "yunustan"),
      "maus": ("fare", "fareler", "fareden")}
# uk : (singulier, pluriel, apres deux, accusatif, genre)
UK = {"kuh": ("корова", "корови", "корови", "корову", "f"), "pferd": ("кінь", "коні", "коні", "коня", "m"),
      "schwein": ("свиня", "свині", "свині", "свиню", "f"), "schaf": ("вівця", "вівці", "вівці", "вівцю", "f"),
      "huhn": ("курка", "кури", "курки", "курку", "f"), "hund": ("собака", "собаки", "собаки", "собаку", "m"),
      "katze": ("кіт", "коти", "коти", "кота", "m"), "goldfisch": ("золота рибка", "золоті рибки", "золоті рибки", "золоту рибку", "f"),
      "baer": ("ведмідь", "ведмеді", "ведмеді", "ведмедя", "m"), "fuchs": ("лисиця", "лисиці", "лисиці", "лисицю", "f"),
      "eichhoernchen": ("білка", "білки", "білки", "білку", "f"), "vogel": ("птах", "птахи", "птахи", "птаха", "m"),
      "fisch": ("риба", "риби", "риби", "рибу", "f"), "delfin": ("дельфін", "дельфіни", "дельфіни", "дельфіна", "m"),
      "maus": ("миша", "миші", "миші", "мишу", "f")}
# ru : (singulier, pluriel, apres deux, genitif, genre)
RU = {"kuh": ("корова", "коровы", "коровы", "коровы", "f"), "pferd": ("лошадь", "лошади", "лошади", "лошади", "f"),
      "schwein": ("свинья", "свиньи", "свиньи", "свиньи", "f"), "schaf": ("овца", "овцы", "овцы", "овцы", "f"),
      "huhn": ("курица", "куры", "курицы", "курицы", "f"), "hund": ("собака", "собаки", "собаки", "собаки", "f"),
      "katze": ("кошка", "кошки", "кошки", "кошки", "f"), "goldfisch": ("золотая рыбка", "золотые рыбки", "золотые рыбки", "золотой рыбки", "f"),
      "baer": ("медведь", "медведи", "медведя", "медведя", "m"), "fuchs": ("лиса", "лисы", "лисы", "лисы", "f"),
      "eichhoernchen": ("белка", "белки", "белки", "белки", "f"), "vogel": ("птица", "птицы", "птицы", "птицы", "f"),
      "fisch": ("рыба", "рыбы", "рыбы", "рыбы", "f"), "delfin": ("дельфин", "дельфины", "дельфина", "дельфина", "m"),
      "maus": ("мышь", "мыши", "мыши", "мыши", "f")}
# pl : (singulier, pluriel, apres deux, genitif, genre)
PL = {"kuh": ("krowa", "krowy", "krowy", "krowy", "f"), "pferd": ("koń", "konie", "konie", "konia", "m"),
      "schwein": ("świnia", "świnie", "świnie", "świni", "f"), "schaf": ("owca", "owce", "owce", "owcy", "f"),
      "huhn": ("kura", "kury", "kury", "kury", "f"), "hund": ("pies", "psy", "psy", "psa", "m"),
      "katze": ("kot", "koty", "koty", "kota", "m"), "goldfisch": ("złota rybka", "złote rybki", "złote rybki", "złotej rybki", "f"),
      "baer": ("niedźwiedź", "niedźwiedzie", "niedźwiedzie", "niedźwiedzia", "m"), "fuchs": ("lis", "lisy", "lisy", "lisa", "m"),
      "eichhoernchen": ("wiewiórka", "wiewiórki", "wiewiórki", "wiewiórki", "f"), "vogel": ("ptak", "ptaki", "ptaki", "ptaka", "m"),
      "fisch": ("ryba", "ryby", "ryby", "ryby", "f"), "delfin": ("delfin", "delfiny", "delfiny", "delfina", "m"),
      "maus": ("mysz", "myszy", "myszy", "myszy", "f")}
# fa : (singulier, pluriel, devant un adjectif)
FA = {"kuh": ("گاو", "گاوها", "گاو"), "pferd": ("اسب", "اسب‌ها", "اسب"), "schwein": ("خوک", "خوک‌ها", "خوک"),
      "schaf": ("گوسفند", "گوسفندها", "گوسفند"), "huhn": ("مرغ", "مرغ‌ها", "مرغ"), "hund": ("سگ", "سگ‌ها", "سگ"),
      "katze": ("گربه", "گربه‌ها", "گربهٔ"), "goldfisch": ("ماهی قرمز", "ماهی‌های قرمز", "ماهی قرمز"),
      "baer": ("خرس", "خرس‌ها", "خرس"), "fuchs": ("روباه", "روباه‌ها", "روباه"), "eichhoernchen": ("سنجاب", "سنجاب‌ها", "سنجاب"),
      "vogel": ("پرنده", "پرنده‌ها", "پرندهٔ"), "fisch": ("ماهی", "ماهی‌ها", "ماهی"), "delfin": ("دلفین", "دلفین‌ها", "دلفین"),
      "maus": ("موش", "موش‌ها", "موش")}
# ar : (indefini, defini, pluriel defini, duel, genre) ; la poule au pluriel « الدجاجات », pas le collectif « الدجاج » (masculin)
AR = {"kuh": ("بقرة", "البقرة", "الأبقار", "بقرتان", "f"), "pferd": ("حصان", "الحصان", "الخيول", "حصانان", "m"),
      "schwein": ("خنزير", "الخنزير", "الخنازير", "خنزيران", "m"), "schaf": ("خروف", "الخروف", "الخراف", "خروفان", "m"),
      "huhn": ("دجاجة", "الدجاجة", "الدجاجات", "دجاجتان", "f"), "hund": ("كلب", "الكلب", "الكلاب", "كلبان", "m"),
      "katze": ("قطّ", "القطّ", "القطط", "قطّان", "m"),
      "goldfisch": ("سمكة ذهبية", "السمكة الذهبية", "الأسماك الذهبية", "سمكتان ذهبيتان", "f"),
      "baer": ("دبّ", "الدبّ", "الدببة", "دبّان", "m"), "fuchs": ("ثعلب", "الثعلب", "الثعالب", "ثعلبان", "m"),
      "eichhoernchen": ("سنجاب", "السنجاب", "السناجب", "سنجابان", "m"), "vogel": ("طائر", "الطائر", "الطيور", "طائران", "m"),
      "fisch": ("سمكة", "السمكة", "الأسماك", "سمكتان", "f"), "delfin": ("دلفين", "الدلفين", "الدلافين", "دلفينان", "m"),
      "maus": ("فأر", "الفأر", "الفئران", "فأران", "m")}
# combien sur l'image (animales.py, « nombre ») : beaucoup de poissons, trois poules, trois moutons
NOMBRE = {
    "fisch": {"tr": "Fotoğrafta çok balık var.", "uk": "На фото багато риб.", "pl": "Na zdjęciu jest dużo ryb.",
              "ru": "На фото много рыб.", "fa": "در عکس ماهی‌های زیادی هست.", "ar": "في الصورة أسماك كثيرة."},
    "huhn": {"tr": "Fotoğrafta üç tavuk var.", "uk": "На фото три курки.", "pl": "Na zdjęciu są trzy kury.",
             "ru": "На фото три курицы.", "fa": "در عکس سه مرغ هست.", "ar": "في الصورة ثلاث دجاجات."},
    "schaf": {"tr": "Fotoğrafta üç koyun var.", "uk": "На фото три вівці.", "pl": "Na zdjęciu są trzy owce.",
              "ru": "На фото три овцы.", "fa": "در عکس سه گوسفند هست.", "ar": "في الصورة ثلاثة خراف."},
}

# --- LES LIEUX, CE QU'ILS MANGENT, LES COULEURS ------------------------------------------------------------------
LIEUX = {"tr": {"bauernhof": "çiftlikte", "wald": "ormanda", "meer": "denizde", "haus": "evde"},
         "uk": {"bauernhof": "на фермі", "wald": "у лісі", "meer": "у морі", "haus": "удома"},
         "pl": {"bauernhof": "na farmie", "wald": "w lesie", "meer": "w morzu", "haus": "w domu"},
         "ru": {"bauernhof": "на ферме", "wald": "в лесу", "meer": "в море", "haus": "дома"},
         "fa": {"bauernhof": "در مزرعه", "wald": "در جنگل", "meer": "در دریا", "haus": "در خانه"},
         "ar": {"bauernhof": "في المزرعة", "wald": "في الغابة", "meer": "في البحر", "haus": "في البيت"}}
ALIMENTS = {"tr": {"gras": "ot", "fleisch": "et", "fisch": "balık", "nuss": "ceviz"},
            "uk": {"gras": "траву", "fleisch": "мʼясо", "fisch": "рибу", "nuss": "горіхи"},
            "pl": {"gras": "trawę", "fleisch": "mięso", "fisch": "ryby", "nuss": "orzechy"},
            "ru": {"gras": "траву", "fleisch": "мясо", "fisch": "рыбу", "nuss": "орехи"},
            "fa": {"gras": "علف", "fleisch": "گوشت", "fisch": "ماهی", "nuss": "گردو"},
            "ar": {"gras": "العشب", "fleisch": "اللحم", "fisch": "السمك", "nuss": "الجوز"}}
# uk, ru, pl : (masculin, feminin, neutre) ; ar : (masculin, feminin) ; tr, fa : invariables
COULEURS = {
    "tr": {"noir-blanc": "siyah beyaz", "brun": "kahverengi", "rose": "pembe", "blanc": "beyaz", "gris": "gri", "orange": "turuncu",
           "bleu-jaune": "mavi ve sarı"},
    "fa": {"noir-blanc": "سیاه و سفید", "brun": "قهوه‌ای", "rose": "صورتی", "blanc": "سفید", "gris": "خاکستری", "orange": "نارنجی",
           "bleu-jaune": "آبی و زرد"},
    "uk": {"noir-blanc": ("чорно-білий", "чорно-біла", "чорно-біле"), "brun": ("коричневий", "коричнева", "коричневе"),
           "rose": ("рожевий", "рожева", "рожеве"), "blanc": ("білий", "біла", "біле"), "gris": ("сірий", "сіра", "сіре"),
           "orange": ("помаранчевий", "помаранчева", "помаранчеве"), "bleu-jaune": ("синьо-жовтий", "синьо-жовта", "синьо-жовте")},
    "ru": {"noir-blanc": ("чёрно-белый", "чёрно-белая", "чёрно-белое"), "brun": ("коричневый", "коричневая", "коричневое"),
           "rose": ("розовый", "розовая", "розовое"), "blanc": ("белый", "белая", "белое"), "gris": ("серый", "серая", "серое"),
           "orange": ("оранжевый", "оранжевая", "оранжевое"), "bleu-jaune": ("сине-жёлтый", "сине-жёлтая", "сине-жёлтое")},
    "pl": {"noir-blanc": ("czarno-biały", "czarno-biała", "czarno-białe"), "brun": ("brązowy", "brązowa", "brązowe"),
           "rose": ("różowy", "różowa", "różowe"), "blanc": ("biały", "biała", "białe"), "gris": ("szary", "szara", "szare"),
           "orange": ("pomarańczowy", "pomarańczowa", "pomarańczowe"), "bleu-jaune": ("niebiesko-żółty", "niebiesko-żółta", "niebiesko-żółte")},
    "ar": {"noir-blanc": ("أسود وأبيض", "سوداء وبيضاء"), "brun": ("بنّي", "بنّية"), "rose": ("وردي", "وردية"), "blanc": ("أبيض", "بيضاء"),
           "gris": ("رمادي", "رمادية"), "orange": ("برتقالي", "برتقالية"), "bleu-jaune": ("أزرق وأصفر", "زرقاء وصفراء")},
}
# un renard roux (le francais dit « roux », comme animales.py : frCouleur) : la couleur qu'on lui donne vraiment
COULEUR_RENARD = {"uk": "руда", "ru": "рыжая", "pl": "rudy"}
G3 = {"m": 0, "f": 1, "n": 2}


def maj(s):
    """La majuscule de la phrase (en turc, i -> İ)."""
    return ("İ" if s[0] == "i" else s[0].upper()) + s[1:]


def couleur(lg, c, g="m"):
    """La couleur au genre demande (g : m, f ou n), pour tradCouleurs et les phrases."""
    v = COULEURS[lg][c]
    if isinstance(v, str):
        return v
    return v[min(G3[g], len(v) - 1)]


def lieu(lg, h):
    return LIEUX[lg][h]


def _g(lg, a):
    return {"uk": UK, "ru": RU, "pl": PL, "ar": AR}[lg][a][4]


def _couleur_de(lg, a, c, ou_attr=False):
    if a == "fuchs" and c == "orange" and lg in COULEUR_RENARD:
        return COULEUR_RENARD[lg]
    return couleur(lg, c, _g(lg, a) if lg in ("uk", "ru", "pl", "ar") else "m")


def _uk_prep(precedent, groupe):
    """« у лісі » / « в лісі » : в après une voyelle (l'alternance у / в de l'ukrainien)."""
    if groupe.startswith("у ") and precedent[-1:] in "аеєиіїоуюя":
        return "в " + groupe[2:]
    return groupe


def rendre(lg, cle):
    """La phrase de la cle de animales.py (ident, art, plur, nombre, hab, mange, col, attr, plus, moins)."""
    k = cle.split("|")
    sorte, a = k[0], k[1]
    if sorte == "nombre":
        return NOMBRE[a][lg]
    if lg == "tr":
        sg, pl, abl = TR[a]
        if sorte == "ident": return "Bu bir %s." % sg
        if sorte == "art": return "%s, %s" % (sg, pl)
        if sorte == "plur": return "bir %s, iki %s" % (sg, sg)
        if sorte == "hab": return "%s %s yaşar." % (maj(sg if k[3] == "sg" else pl), LIEUX[lg][k[2]])
        if sorte == "mange": return "%s %s yer." % (maj(sg if k[3] == "sg" else pl), ALIMENTS[lg][k[2]])
        if sorte == "col": return "%s %s." % (maj(sg), _couleur_de(lg, a, k[2]))
        if sorte == "attr": return "Bu %s bir %s." % (_couleur_de(lg, a, k[2]), sg)
        if sorte in ("plus", "moins"): return "%s %s %s." % (maj(sg), TR[k[2]][2], "büyüktür" if sorte == "plus" else "küçüktür")
    if lg in ("uk", "ru", "pl"):
        T = {"uk": UK, "ru": RU, "pl": PL}[lg]
        sg, pl, deux, obl, g = T[a]
        if sorte == "ident": return {"uk": "Це %s.", "ru": "Это %s.", "pl": "To jest %s."}[lg] % sg
        if sorte == "art": return "%s, %s" % (sg, pl)
        if sorte == "plur":
            un = {"uk": ("один", "одна"), "ru": ("один", "одна"), "pl": ("jeden", "jedna")}[lg][g == "f"]
            dv = {"uk": ("два", "дві"), "ru": ("два", "две"), "pl": ("dwa", "dwie")}[lg][g == "f"]
            return "%s %s, %s %s" % (un, sg, dv, deux)
        if sorte == "hab":
            v = {"uk": ("живе", "живуть"), "ru": ("живёт", "живут"), "pl": ("żyje", "żyją")}[lg][k[3] == "pl"]
            l = LIEUX[lg][k[2]]
            return "%s %s %s." % (maj(sg if k[3] == "sg" else pl), v, _uk_prep(v, l) if lg == "uk" else l)
        if sorte == "mange":
            v = {"uk": ("їсть", "їдять"), "ru": ("ест", "едят"), "pl": ("je", "jedzą")}[lg][k[3] == "pl"]
            return "%s %s %s." % (maj(sg if k[3] == "sg" else pl), v, ALIMENTS[lg][k[2]])
        if sorte == "col":
            return ("%s jest %s." if lg == "pl" else "%s %s.") % (maj(sg), _couleur_de(lg, a, k[2]))
        if sorte == "attr":
            return {"uk": "Це %s %s.", "ru": "Это %s %s.", "pl": "To jest %s %s."}[lg] % (_couleur_de(lg, a, k[2]), sg)
        if sorte in ("plus", "moins"):
            b = T[k[2]]
            if lg == "ru":
                return "%s %s %s." % (maj(sg), "больше" if sorte == "plus" else "меньше", b[3])
            if lg == "uk":
                adj = {"plus": ("більший", "більша", "більше"), "moins": ("менший", "менша", "менше")}[sorte][G3[g]]
                return "%s %s за %s." % (maj(sg), adj, b[3])
            adj = {"plus": ("większy", "większa", "większe"), "moins": ("mniejszy", "mniejsza", "mniejsze")}[sorte][G3[g]]
            return "%s jest %s od %s." % (maj(sg), adj, b[3])
    if lg == "fa":
        sg, pl, ez = FA[a]
        if sorte == "ident": return "این یک %s است." % sg
        if sorte == "art": return "%s، %s" % (sg, pl)
        if sorte == "plur": return "یک %s، دو %s" % (sg, sg)
        if sorte == "hab": return "%s %s زندگی %s." % (sg if k[3] == "sg" else pl, LIEUX[lg][k[2]], "می‌کند" if k[3] == "sg" else "می‌کنند")
        if sorte == "mange": return "%s %s %s." % (sg if k[3] == "sg" else pl, ALIMENTS[lg][k[2]], "می‌خورد" if k[3] == "sg" else "می‌خورند")
        if sorte == "col": return "%s %s است." % (sg, _couleur_de(lg, a, k[2]))
        if sorte == "attr": return "این یک %s %s است." % (ez, _couleur_de(lg, a, k[2]))
        if sorte in ("plus", "moins"): return "%s از %s %s است." % (sg, FA[k[2]][0], "بزرگ‌تر" if sorte == "plus" else "کوچک‌تر")
    if lg == "ar":
        ind, defi, pl, duel, g = AR[a]
        f = g == "f"
        if sorte == "ident": return "%s %s." % ("هذه" if f else "هذا", ind)
        if sorte == "art": return "%s، %s" % (defi, pl)
        if sorte == "plur":     # « بقرة واحدة، بقرتان » (le duel), « سمكة ذهبية واحدة، سمكتان ذهبيتان »
            return "%s %s، %s" % (ind, "واحدة" if f else "واحد", duel)
        # le pluriel d'un animal (non humain) s'accorde au feminin singulier : « تعيش الأبقار »
        if sorte == "hab":
            v = "تعيش" if (f or k[3] == "pl") else "يعيش"
            return "%s %s %s." % (v, defi if k[3] == "sg" else pl, LIEUX[lg][k[2]])
        if sorte == "mange":
            v = "تأكل" if (f or k[3] == "pl") else "يأكل"
            return "%s %s %s." % (v, defi if k[3] == "sg" else pl, ALIMENTS[lg][k[2]])
        if sorte == "col": return "%s %s." % (defi, _couleur_de(lg, a, k[2]))
        if sorte == "attr": return "%s %s %s." % ("هذه" if f else "هذا", ind, _couleur_de(lg, a, k[2]))
        if sorte in ("plus", "moins"): return "%s %s من %s." % (defi, "أكبر" if sorte == "plus" else "أصغر", AR[k[2]][1])
    raise KeyError("%s %s" % (lg, cle))


def suite_mange(lg, a, f):
    """La seconde phrase de la decouverte : « Er frisst Gras. » (le pronom, ou rien la ou la langue l'omet)."""
    al = ALIMENTS[lg][f]
    if lg == "tr":
        return "%s yer." % maj(al)
    if lg == "fa":
        return "%s می‌خورد." % al
    if lg == "pl":              # le polonais omet le pronom sujet : « Je mięso. »
        return "Je %s." % al
    if lg == "ar":
        return "%s %s." % ("تأكل" if AR[a][4] == "f" else "يأكل", al)
    g = {"uk": UK, "ru": RU, "pl": PL}[lg][a][4]
    pron = {"uk": {"m": "Він", "f": "Вона"}, "ru": {"m": "Он", "f": "Она"}, "pl": {"m": "On", "f": "Ona"}}[lg][g]
    v = {"uk": "їсть", "ru": "ест", "pl": "je"}[lg]
    return "%s %s %s." % (pron, v, al)
