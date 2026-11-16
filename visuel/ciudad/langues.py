# -*- coding: utf-8 -*-
"""En ville : s'orienter, dans les langues d'interface sans phrase traduite jusqu'ici (lot 14, 16 nov. 2026) : turc,
ukrainien, polonais, russe, persan et arabe pour qui apprend l'allemand, et l'arabe pour qui apprend l'espagnol.

Chaque phrase est refaite par la grammaire de sa langue, a partir de ce que ciudad.py sait (le lieu, la relation, le
chemin), jamais calquee sur le francais :
- le cas qu'exige chaque preposition : « bankanın yanında », « поруч із банком », « рядом с банком » (« со школой »),
  « obok banku », « między piekarnią a bankiem », « до аптеки », « к аптеке » ;
- le vouvoiement du Sie : « dönün », « поверніть », « поверните », « proszę skręcić », « بپیچید » ; l'arabe prend
  l'imperatif usuel des indications (« انعطف ») ;
- les noms des rues restent ceux du plan (« Bergstraße », « calle Mayor »), comme en francais : ce sont eux qu'on lit sur
  le dessin ; en turc ils prennent leur suffixe apres l'apostrophe (« Bergstraße'de », « Bergstraße'yi »).
Appele par ciudad.py ; les points douteux : retours/A-RELIRE-THEMES-<LG>.md.
"""

LANGUES = ("tr", "uk", "pl", "ru", "fa", "ar")

# --- LES LIEUX ----------------------------------------------------------------------------------------------------
# tr : (nominatif, genitif, datif)
TR = {"bahnhof": ("tren istasyonu", "tren istasyonunun", "tren istasyonuna"), "apotheke": ("eczane", "eczanenin", "eczaneye"),
      "rathaus": ("belediye binası", "belediye binasının", "belediye binasına"), "bank": ("banka", "bankanın", "bankaya"),
      "post": ("postane", "postanenin", "postaneye"), "haltestelle": ("otobüs durağı", "otobüs durağının", "otobüs durağına"),
      "krankenhaus": ("hastane", "hastanenin", "hastaneye"), "kirche": ("kilise", "kilisenin", "kiliseye"),
      "museum": ("müze", "müzenin", "müzeye"), "park": ("park", "parkın", "parka"),
      "supermarkt": ("süpermarket", "süpermarketin", "süpermarkete"), "bibliothek": ("kütüphane", "kütüphanenin", "kütüphaneye"),
      "kino": ("sinema", "sinemanın", "sinemaya"), "hotel": ("otel", "otelin", "otele"), "baeckerei": ("fırın", "fırının", "fırına"),
      "cafe": ("kafe", "kafenin", "kafeye"), "polizei": ("karakol", "karakolun", "karakola"), "schule": ("okul", "okulun", "okula")}
# uk : (nominatif, genitif, instrumental)
UK = {"bahnhof": ("вокзал", "вокзалу", "вокзалом"), "apotheke": ("аптека", "аптеки", "аптекою"), "rathaus": ("ратуша", "ратуші", "ратушею"),
      "bank": ("банк", "банку", "банком"), "post": ("пошта", "пошти", "поштою"), "haltestelle": ("зупинка", "зупинки", "зупинкою"),
      "krankenhaus": ("лікарня", "лікарні", "лікарнею"), "kirche": ("церква", "церкви", "церквою"), "museum": ("музей", "музею", "музеєм"),
      "park": ("парк", "парку", "парком"), "supermarkt": ("супермаркет", "супермаркету", "супермаркетом"),
      "bibliothek": ("бібліотека", "бібліотеки", "бібліотекою"), "kino": ("кінотеатр", "кінотеатру", "кінотеатром"),
      "hotel": ("готель", "готелю", "готелем"), "baeckerei": ("пекарня", "пекарні", "пекарнею"), "cafe": ("кафе", "кафе", "кафе"),
      "polizei": ("поліцейська дільниця", "поліцейської дільниці", "поліцейською дільницею"), "schule": ("школа", "школи", "школою")}
# ru : (nominatif, genitif, datif, instrumental)
RU = {"bahnhof": ("вокзал", "вокзала", "вокзалу", "вокзалом"), "apotheke": ("аптека", "аптеки", "аптеке", "аптекой"),
      "rathaus": ("ратуша", "ратуши", "ратуше", "ратушей"), "bank": ("банк", "банка", "банку", "банком"),
      "post": ("почта", "почты", "почте", "почтой"), "haltestelle": ("остановка", "остановки", "остановке", "остановкой"),
      "krankenhaus": ("больница", "больницы", "больнице", "больницей"), "kirche": ("церковь", "церкви", "церкви", "церковью"),
      "museum": ("музей", "музея", "музею", "музеем"), "park": ("парк", "парка", "парку", "парком"),
      "supermarkt": ("супермаркет", "супермаркета", "супермаркету", "супермаркетом"),
      "bibliothek": ("библиотека", "библиотеки", "библиотеке", "библиотекой"), "kino": ("кинотеатр", "кинотеатра", "кинотеатру", "кинотеатром"),
      "hotel": ("гостиница", "гостиницы", "гостинице", "гостиницей"), "baeckerei": ("пекарня", "пекарни", "пекарне", "пекарней"),
      "cafe": ("кафе", "кафе", "кафе", "кафе"),
      "polizei": ("полицейский участок", "полицейского участка", "полицейскому участку", "полицейским участком"),
      "schule": ("школа", "школы", "школе", "школой")}
# pl : (nominatif, genitif, instrumental)
PL = {"bahnhof": ("dworzec", "dworca", "dworcem"), "apotheke": ("apteka", "apteki", "apteką"), "rathaus": ("ratusz", "ratusza", "ratuszem"),
      "bank": ("bank", "banku", "bankiem"), "post": ("poczta", "poczty", "pocztą"), "haltestelle": ("przystanek", "przystanku", "przystankiem"),
      "krankenhaus": ("szpital", "szpitala", "szpitalem"), "kirche": ("kościół", "kościoła", "kościołem"), "museum": ("muzeum", "muzeum", "muzeum"),
      "park": ("park", "parku", "parkiem"), "supermarkt": ("supermarket", "supermarketu", "supermarketem"),
      "bibliothek": ("biblioteka", "biblioteki", "biblioteką"), "kino": ("kino", "kina", "kinem"), "hotel": ("hotel", "hotelu", "hotelem"),
      "baeckerei": ("piekarnia", "piekarni", "piekarnią"), "cafe": ("kawiarnia", "kawiarni", "kawiarnią"),
      "polizei": ("komisariat policji", "komisariatu policji", "komisariatem policji"), "schule": ("szkoła", "szkoły", "szkołą")}
FA = {"bahnhof": "ایستگاه قطار", "apotheke": "داروخانه", "rathaus": "شهرداری", "bank": "بانک", "post": "اداره پست",
      "haltestelle": "ایستگاه اتوبوس", "krankenhaus": "بیمارستان", "kirche": "کلیسا", "museum": "موزه", "park": "پارک",
      "supermarkt": "سوپرمارکت", "bibliothek": "کتابخانه", "kino": "سینما", "hotel": "هتل", "baeckerei": "نانوایی", "cafe": "کافه",
      "polizei": "کلانتری", "schule": "مدرسه"}
# ar : (indefini, defini, genre)
AR = {"bahnhof": ("محطة قطار", "محطة القطار", "f"), "apotheke": ("صيدلية", "الصيدلية", "f"), "rathaus": ("بلدية", "البلدية", "f"),
      "bank": ("بنك", "البنك", "m"), "post": ("مكتب بريد", "مكتب البريد", "m"), "haltestelle": ("موقف حافلات", "موقف الحافلات", "m"),
      "krankenhaus": ("مستشفى", "المستشفى", "m"), "kirche": ("كنيسة", "الكنيسة", "f"), "museum": ("متحف", "المتحف", "m"),
      "park": ("حديقة", "الحديقة", "f"), "supermarkt": ("سوبرماركت", "السوبرماركت", "m"), "bibliothek": ("مكتبة", "المكتبة", "f"),
      "kino": ("سينما", "السينما", "f"), "hotel": ("فندق", "الفندق", "m"), "baeckerei": ("مخبز", "المخبز", "m"),
      "cafe": ("مقهى", "المقهى", "m"), "polizei": ("مركز شرطة", "مركز الشرطة", "m"), "schule": ("مدرسة", "المدرسة", "f")}


def maj(s):
    """La majuscule de la phrase (en turc, i -> İ)."""
    return ("İ" if s[0] == "i" else s[0].upper()) + s[1:]


def _tr_rue(nom, suffixe):
    """« Bergstraße'de » : les rues du plan finissent toutes en -e (voyelle anterieure) ; une autre fin arrete."""
    if not nom.endswith("e"):
        raise ValueError("rue turque : " + nom)
    return nom + "'" + {"gen": "nin", "loc": "de", "acc": "yi"}[suffixe]


def _ru_s(instr):
    """« с банком », mais « со школой » (с devant s / sch + consonne)."""
    return ("со " if instr[:2] in ("шк", "ст", "сп", "зд") else "с ") + instr


def _ar_et(mot):
    """« والبنك » : le و arabe se colle au mot ; devant un nom latin (une rue), on garde l'espace."""
    return ("و " if mot[:1].isascii() else "و") + mot


# --- LES GROUPES : « neben der Bank », « an der Ecke Bergstraße und Lindenstraße » --------------------------------
def groupe(lg, rel, nomrue, app):
    t = rel[0]
    if lg == "tr":
        if t == "neben": return TR[rel[1]][1] + " yanında"
        if t == "gegenueber": return TR[rel[1]][1] + " karşısında"
        if t == "zwischen": return TR[rel[1]][0] + " ile " + TR[rel[2]][1] + " arasında"
        if t == "ecke": return nomrue(rel[1]) + " ile " + _tr_rue(nomrue(rel[2]), "gen") + " köşesinde"
        if t == "strasse": return _tr_rue(nomrue(rel[1]), "loc")
    if lg == "uk":
        if t == "neben": return "поруч із " + UK[rel[1]][2]
        if t == "gegenueber": return "навпроти " + UK[rel[1]][1]
        if t == "zwischen": return "між " + UK[rel[1]][2] + " та " + UK[rel[2]][2]
        if t == "ecke": return "на розі " + nomrue(rel[1]) + " та " + nomrue(rel[2])
        if t == "strasse": return "на вулиці " + nomrue(rel[1])
    if lg == "ru":
        if t == "neben": return "рядом " + _ru_s(RU[rel[1]][3])
        if t == "gegenueber": return "напротив " + RU[rel[1]][1]
        if t == "zwischen": return "между " + RU[rel[1]][3] + " и " + RU[rel[2]][3]
        if t == "ecke": return "на углу " + nomrue(rel[1]) + " и " + nomrue(rel[2])
        if t == "strasse": return "на улице " + nomrue(rel[1])
    if lg == "pl":
        if t == "neben": return "obok " + PL[rel[1]][1]
        if t == "gegenueber": return "naprzeciwko " + PL[rel[1]][1]
        if t == "zwischen": return "między " + PL[rel[1]][2] + " a " + PL[rel[2]][2]
        if t == "ecke": return "na rogu " + nomrue(rel[1]) + " i " + nomrue(rel[2])
        if t == "strasse": return "na ulicy " + nomrue(rel[1])
    if lg == "fa":
        if t == "neben": return "کنار " + FA[rel[1]]
        if t == "gegenueber": return "روبه‌روی " + FA[rel[1]]
        if t == "zwischen": return "بین " + FA[rel[1]] + " و " + FA[rel[2]]
        if t == "ecke": return "در نبش " + nomrue(rel[1]) + " و " + nomrue(rel[2])
        if t == "strasse": return "در خیابان " + nomrue(rel[1])
    if lg == "ar":
        if t == "neben": return "بجانب " + AR[rel[1]][1]
        if t == "gegenueber": return "مقابل " + AR[rel[1]][1]
        if t == "zwischen": return "بين " + AR[rel[1]][1] + " " + _ar_et(AR[rel[2]][1])
        if t == "ecke": return "عند زاوية " + nomrue(rel[1]) + " " + _ar_et(nomrue(rel[2]))
        # « في شارع Gartenstraße » ; une rue de Madrid porte deja « calle » : « في calle Mayor »
        if t == "strasse": return ("في شارع " if app == "de" else "في ") + nomrue(rel[1])
    raise KeyError((lg, rel))


def phrase_lieu(lg, lieu, rel, nomrue, app):
    """« Die Apotheke ist neben der Bank. »"""
    g = groupe(lg, rel, nomrue, app)
    if lg == "tr": return maj(TR[lieu][0]) + " " + g + "."
    if lg == "uk": return maj(UK[lieu][0]) + " " + g + "."
    if lg == "ru": return maj(RU[lieu][0]) + " " + g + "."
    if lg == "pl": return maj(PL[lieu][0]) + " jest " + g + "."
    if lg == "fa": return FA[lieu] + " " + g + " است."
    if lg == "ar": return AR[lieu][1] + " " + g + "."
    raise KeyError(lg)


# --- LES QUESTIONS ET LA PHOTO --------------------------------------------------------------------------------------
def question(lg, sorte, lieu, app):
    """gibt (« Entschuldigung, gibt es hier eine Apotheke? »), wie (« wie komme ich zur Apotheke? »), suche (« Ich suche
    den Weg zur Apotheke. » ; en espagnol « ¿Dónde está la farmacia? »), photo (« Das ist die Apotheke. »)."""
    if lg == "tr":
        n, gen, dat = TR[lieu]
        return {"gibt": "Affedersiniz, buralarda bir %s var mı?" % n, "wie": "Affedersiniz, %s nasıl giderim?" % dat,
                "suche": "%s giden yolu arıyorum." % maj(dat), "photo": "Burası %s." % n}[sorte]
    if lg == "uk":
        n, gen, _ = UK[lieu]
        return {"gibt": "Вибачте, тут поблизу є %s?" % n, "wie": "Вибачте, як мені дійти до %s?" % gen,
                "suche": "Я шукаю дорогу до %s." % gen, "photo": "Це %s." % n}[sorte]
    if lg == "ru":
        n, gen, dat, _ = RU[lieu]
        return {"gibt": "Извините, здесь поблизости есть %s?" % n, "wie": "Извините, как мне пройти к %s?" % dat,
                "suche": "Я ищу дорогу к %s." % dat, "photo": "Это %s." % n}[sorte]
    if lg == "pl":
        n, gen, _ = PL[lieu]
        return {"gibt": "Przepraszam, czy jest tu w pobliżu %s?" % n, "wie": "Przepraszam, jak dojść do %s?" % gen,
                "suche": "Szukam drogi do %s." % gen, "photo": "To jest %s." % n}[sorte]
    if lg == "fa":
        n = FA[lieu]
        return {"gibt": "ببخشید، این نزدیکی یک %s هست؟" % n, "wie": "ببخشید، چطور به %s بروم؟" % n,
                "suche": "دنبال راه %s می‌گردم." % n, "photo": "این %s است." % n}[sorte]
    if lg == "ar":
        ind, defi, g = AR[lieu]
        f = g == "f"
        return {"gibt": "عفوًا، هل %s %s %s من هنا؟" % ("توجد" if f else "يوجد", ind, "قريبة" if f else "قريب"),
                "wie": "عفوًا، كيف أصل إلى %s؟" % defi,
                "suche": ("أبحث عن الطريق إلى %s." % defi) if app == "de" else ("عفوًا، أين %s؟" % defi),
                "photo": "%s %s." % ("هذه هي" if f else "هذا هو", defi)}[sorte]
    raise KeyError(lg)


# --- LES ITINERAIRES ----------------------------------------------------------------------------------------------
ORD = {"tr": ["birinci", "ikinci", "üçüncü"],
       "uk": {"acc": ["першу", "другу", "третю"], "gen": ["першого", "другого", "третього"], "loc": ["першому", "другому", "третьому"]},
       "ru": {"acc": ["первую", "вторую", "третью"], "gen": ["первого", "второго", "третьего"], "loc": ["первом", "втором", "третьем"]},
       "pl": {"acc": ["pierwszą", "drugą", "trzecią"], "gen": ["pierwszego", "drugiego", "trzeciego"], "loc": ["pierwszym", "drugim", "trzecim"]},
       "fa": ["اول", "دوم", "سوم"], "ar": ["الأول", "الثاني", "الثالث"]}
COTE = {"tr": {"links": ("sola", "sol"), "rechts": ("sağa", "sağ")}, "uk": {"links": "ліворуч", "rechts": "праворуч"},
        "ru": {"links": "налево", "rechts": "направо"}, "pl": {"links": "w lewo", "rechts": "w prawo"},
        "fa": {"links": "چپ", "rechts": "راست"}, "ar": {"links": ("اليسار", "يسارًا"), "rechts": ("اليمين", "يمينًا")}}
# la fin : « Die Apotheke ist auf der linken Seite. » (lieu nomme) ou « Es ist auf der linken Seite. »
COTE_FIN = {"uk": {"links": "ліворуч", "rechts": "праворуч"}, "ru": {"links": "слева", "rechts": "справа"},
            "pl": {"links": "po lewej stronie", "rechts": "po prawej stronie"}}


def _rues(lg, ids, nomrue):
    if lg == "tr":
        return " ve ".join(_tr_rue(nomrue(i), "acc") for i in ids)
    et = {"uk": " та ", "ru": " и ", "pl": " i ", "fa": " و ", "ar": " و "}[lg]
    return et.join(nomrue(i) for i in ids)


def route(lg, e, forme, lieu, nomrue):
    """Les phrases d'un itineraire (une liste), comme phrases_route de ciudad.py."""
    out = []
    for i, v in enumerate(e["virages"]):
        c, r, k = v["cote"], v["rue"] - 1, v["carrefour"] - 1
        premier = i == 0
        if lg == "tr":
            s = COTE[lg][c][0]
            if forme == "A":
                out.append(("%s sokaktan %s dönün." % (maj(ORD[lg][r]), s)) if premier and r == 0 else
                           ("Düz gidin ve %s sokaktan %s dönün." % (ORD[lg][r], s)) if premier else
                           ("Sonra %s sokaktan %s dönün." % (ORD[lg][r], s)))
            else:
                kav = {0: "birinci kavşağa", 1: "ikinci kavşağa", 2: "üçüncü kavşağa"}[k]
                out.append(("%s kadar gidin ve orada %s dönün." % (maj(kav), s)) if premier else
                           ("Sonra %s kavşakta %s dönün." % (ORD[lg][k], s)))
        elif lg in ("uk", "ru"):
            s = COTE[lg][c]
            O = ORD[lg]
            if lg == "uk":
                if forme == "A":
                    out.append(("Поверніть %s на %s вулицю." % (s, O["acc"][r])) if premier and r == 0 else
                               ("Ідіть прямо й поверніть %s на %s вулицю." % (s, O["acc"][r])) if premier else
                               ("Потім поверніть %s на %s вулицю." % (s, O["acc"][r])))
                else:
                    out.append(("Дійдіть до %s перехрестя й там поверніть %s." % (O["gen"][k], s)) if premier else
                               ("Потім на %s перехресті поверніть %s." % (O["loc"][k], s)))
            else:
                if forme == "A":
                    out.append(("Поверните %s на %s улицу." % (s, O["acc"][r])) if premier and r == 0 else
                               ("Идите прямо и поверните %s на %s улицу." % (s, O["acc"][r])) if premier else
                               ("Потом поверните %s на %s улицу." % (s, O["acc"][r])))
                else:
                    out.append(("Дойдите до %s перекрёстка и там поверните %s." % (O["gen"][k], s)) if premier else
                               ("Потом на %s перекрёстке поверните %s." % (O["loc"][k], s)))
        elif lg == "pl":
            s = COTE[lg][c]
            O = ORD[lg]
            if forme == "A":
                out.append(("Proszę skręcić w %s ulicę %s." % (O["acc"][r], s)) if premier and r == 0 else
                           ("Proszę iść prosto i skręcić w %s ulicę %s." % (O["acc"][r], s)) if premier else
                           ("Potem proszę skręcić w %s ulicę %s." % (O["acc"][r], s)))
            else:
                out.append(("Proszę iść do %s skrzyżowania i tam skręcić %s." % (O["gen"][k], s)) if premier else
                           ("Potem na %s skrzyżowaniu proszę skręcić %s." % (O["loc"][k], s)))
        elif lg == "fa":
            s = COTE[lg][c]
            if forme == "A":
                out.append(("از خیابان %s به %s بپیچید." % (ORD[lg][r], s)) if premier and r == 0 else
                           ("مستقیم بروید و از خیابان %s به %s بپیچید." % (ORD[lg][r], s)) if premier else
                           ("سپس از خیابان %s به %s بپیچید." % (ORD[lg][r], s)))
            else:
                out.append(("تا چهارراه %s بروید و آنجا به %s بپیچید." % (ORD[lg][k], s)) if premier else
                           ("سپس سر چهارراه %s به %s بپیچید." % (ORD[lg][k], s)))
        elif lg == "ar":
            nom, adv = COTE[lg][c]
            if forme == "A":
                out.append(("خذ الشارع %s على %s." % (ORD[lg][r], nom)) if premier and r == 0 else
                           ("امشِ مستقيمًا ثم خذ الشارع %s على %s." % (ORD[lg][r], nom)) if premier else
                           ("ثم خذ الشارع %s على %s." % (ORD[lg][r], nom)))
            else:
                out.append(("امشِ حتى التقاطع %s وانعطف هناك %s." % (ORD[lg][k], adv)) if premier else
                           ("ثم انعطف %s عند التقاطع %s." % (adv, ORD[lg][k])))
    if e["traverses"]:
        r = _rues(lg, e["traverses"], nomrue)
        out.append({"tr": "Düz gidin ve %s geçin.", "uk": "Ідіть прямо й перейдіть %s.", "ru": "Идите прямо и перейдите %s.",
                    "pl": "Proszę iść prosto i przejść przez %s.", "fa": "مستقیم بروید و از %s رد شوید.",
                    "ar": "امشِ مستقيمًا واعبر %s."}[lg] % r)
    c = e["cote"]
    if lg == "tr":
        cote = COTE[lg][c][1] + " tarafta"
        out.append(maj(cote) + "." if lieu is None else "%s %s." % (maj(TR[lieu][0]), cote))
    elif lg in ("uk", "ru"):
        cote = COTE_FIN[lg][c]
        out.append(({"uk": "Це ", "ru": "Это "}[lg] + cote + ".") if lieu is None else "%s %s." % (maj({"uk": UK, "ru": RU}[lg][lieu][0]), cote))
    elif lg == "pl":
        cote = COTE_FIN[lg][c]
        out.append(("To jest " + cote + ".") if lieu is None else "%s jest %s." % (maj(PL[lieu][0]), cote))
    elif lg == "fa":
        cote = "سمت " + COTE[lg][c]
        out.append((cote + " است.") if lieu is None else "%s %s است." % (FA[lieu], cote))
    elif lg == "ar":
        cote = "على " + COTE[lg][c][0]
        out.append(("المكان " + cote + ".") if lieu is None else "%s %s." % (AR[lieu][1], cote))
    return out


GESTES = {"tr": {"links": "Burada sola dönün.", "rechts": "Burada sağa dönün.", "geradeaus": "Burada düz gidin."},
          "uk": {"links": "Тут поверніть ліворуч.", "rechts": "Тут поверніть праворуч.", "geradeaus": "Тут ідіть прямо."},
          "ru": {"links": "Здесь поверните налево.", "rechts": "Здесь поверните направо.", "geradeaus": "Здесь идите прямо."},
          "pl": {"links": "Tutaj proszę skręcić w lewo.", "rechts": "Tutaj proszę skręcić w prawo.", "geradeaus": "Tutaj proszę iść prosto."},
          "fa": {"links": "اینجا به چپ بپیچید.", "rechts": "اینجا به راست بپیچید.", "geradeaus": "اینجا مستقیم بروید."},
          "ar": {"links": "انعطف يسارًا هنا.", "rechts": "انعطف يمينًا هنا.", "geradeaus": "امشِ مستقيمًا هنا."}}
