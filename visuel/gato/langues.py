# -*- coding: utf-8 -*-
"""« Où est le chat ? » dans les langues d'interface sans phrase traduite jusqu'ici : turc, ukrainien, polonais,
russe (lot 1 de l'alignement des themes, 14 nov. 2026 ; le persan et l'arabe suivront ici meme).

LE CHEMIN NATIF (decision du chef du 14 nov.) : on ne traduit pas des phrases une a une, on traduit les MORCEAUX que
gato.py assemble -- le nom, la preposition, le verbe de position, le verbe du mouvement -- et chaque langue a sa
petite grammaire. Ces quatre langues font ce que fait l'allemand, et que le francais ne fait pas : elles separent
« ou il est » (Wo? + datif) de « ou il va » (Wohin? + accusatif). Le russe dit на столе / на стол, под столом / под
стол ; le polonais w koszu / do kosza ; le turc masanin ustunde / ustune. Le groupe allemand porte deja son cas
(« auf dem Tisch », « auf den Tisch ») : chaque cas recoit SA traduction, et le mauvais choix traduit dit enfin
la difference que l'eleve a manquee.

Moritz est un chat : кот (ru), кіт (uk), kot (pl), kedi (tr), comme dans les textes de la page (« Це Моріц, кіт
Бена й Мії »).

Points douteux : retours/A-RELIRE-THEMES-<LG>.md (a relire par un natif).
"""

LANGUES = ("tr", "uk", "pl", "ru")

# ---------------------------------------------------------------------------------------------------------------
# LES NOMS
# ru, uk, pl : (nominatif, genitif, datif, accusatif, instrumental, locatif) ; pluriel a part (« pl »)
RU = {
    "tisch":   ("стол", "стола", "столу", "стол", "столом", "столе"),
    "kissen":  ("подушка", "подушки", "подушке", "подушку", "подушкой", "подушке"),
    "stuhl":   ("стул", "стула", "стулу", "стул", "стулом", "стуле"),
    "sofa":    ("диван", "дивана", "дивану", "диван", "диваном", "диване"),
    "schrank": ("шкаф", "шкафа", "шкафу", "шкаф", "шкафом", "шкафу"),          # на шкафу, в шкафу
    "regal":   ("стеллаж", "стеллажа", "стеллажу", "стеллаж", "стеллажом", "стеллаже"),
    "korb":    ("корзина", "корзины", "корзине", "корзину", "корзиной", "корзине"),
    "karton":  ("коробка", "коробки", "коробке", "коробку", "коробкой", "коробке"),
    "fenster": ("окно", "окна", "окну", "окно", "окном", "окне"),
    "tuer":    ("дверь", "двери", "двери", "дверь", "дверью", "двери"),
    "pflanze": ("растение", "растения", "растению", "растение", "растением", "растении"),
    "vorhang": ("штора", "шторы", "шторе", "штору", "шторой", "шторе"),
    "tasche":  ("сумка", "сумки", "сумке", "сумку", "сумкой", "сумке"),
    "lampe":   ("лампа", "лампы", "лампе", "лампу", "лампой", "лампе"),
    "bild":    ("картина", "картины", "картине", "картину", "картиной", "картине"),
    "wand":    ("стена", "стены", "стене", "стену", "стеной", "стене"),
}
RU_PL = {
    "kissen": ("подушки", "подушек", "подушкам", "подушки", "подушками", "подушках"),
    "stuhl":  ("стулья", "стульев", "стульям", "стулья", "стульями", "стульях"),
}
UK = {
    "tisch":   ("стіл", "столу", "столу", "стіл", "столом", "столі"),
    "kissen":  ("подушка", "подушки", "подушці", "подушку", "подушкою", "подушці"),
    "stuhl":   ("стілець", "стільця", "стільцю", "стілець", "стільцем", "стільці"),
    "sofa":    ("диван", "дивана", "дивану", "диван", "диваном", "дивані"),
    "schrank": ("шафа", "шафи", "шафі", "шафу", "шафою", "шафі"),
    "regal":   ("стелаж", "стелажа", "стелажу", "стелаж", "стелажем", "стелажі"),
    "korb":    ("кошик", "кошика", "кошику", "кошик", "кошиком", "кошику"),
    "karton":  ("коробка", "коробки", "коробці", "коробку", "коробкою", "коробці"),
    "fenster": ("вікно", "вікна", "вікну", "вікно", "вікном", "вікні"),
    "tuer":    ("двері", "дверей", "дверям", "двері", "дверима", "дверях"),       # toujours au pluriel
    "pflanze": ("рослина", "рослини", "рослині", "рослину", "рослиною", "рослині"),
    "vorhang": ("штора", "штори", "шторі", "штору", "шторою", "шторі"),
    "tasche":  ("сумка", "сумки", "сумці", "сумку", "сумкою", "сумці"),
    "lampe":   ("лампа", "лампи", "лампі", "лампу", "лампою", "лампі"),
    "bild":    ("картина", "картини", "картині", "картину", "картиною", "картині"),
    "wand":    ("стіна", "стіни", "стіні", "стіну", "стіною", "стіні"),
}
UK_PL = {
    "kissen": ("подушки", "подушок", "подушкам", "подушки", "подушками", "подушках"),
    "stuhl":  ("стільці", "стільців", "стільцям", "стільці", "стільцями", "стільцях"),
}
PL = {
    "tisch":   ("stół", "stołu", "stołowi", "stół", "stołem", "stole"),
    "kissen":  ("poduszka", "poduszki", "poduszce", "poduszkę", "poduszką", "poduszce"),
    "stuhl":   ("krzesło", "krzesła", "krzesłu", "krzesło", "krzesłem", "krześle"),
    "sofa":    ("kanapa", "kanapy", "kanapie", "kanapę", "kanapą", "kanapie"),
    "schrank": ("szafa", "szafy", "szafie", "szafę", "szafą", "szafie"),
    "regal":   ("regał", "regału", "regałowi", "regał", "regałem", "regale"),
    "korb":    ("kosz", "kosza", "koszowi", "kosz", "koszem", "koszu"),
    "karton":  ("karton", "kartonu", "kartonowi", "karton", "kartonem", "kartonie"),
    "fenster": ("okno", "okna", "oknu", "okno", "oknem", "oknie"),
    "tuer":    ("drzwi", "drzwi", "drzwiom", "drzwi", "drzwiami", "drzwiach"),     # toujours au pluriel
    "pflanze": ("roślina", "rośliny", "roślinie", "roślinę", "rośliną", "roślinie"),
    "vorhang": ("zasłona", "zasłony", "zasłonie", "zasłonę", "zasłoną", "zasłonie"),
    "tasche":  ("torba", "torby", "torbie", "torbę", "torbą", "torbie"),
    "lampe":   ("lampa", "lampy", "lampie", "lampę", "lampą", "lampie"),
    "bild":    ("obraz", "obrazu", "obrazowi", "obraz", "obrazem", "obrazie"),
    "wand":    ("ściana", "ściany", "ścianie", "ścianę", "ścianą", "ścianie"),
}
PL_PL = {
    "kissen": ("poduszki", "poduszek", "poduszkom", "poduszki", "poduszkami", "poduszkach"),
    "stuhl":  ("krzesła", "krzeseł", "krzesłom", "krzesła", "krzesłami", "krzesłach"),
}
N, G, D, A, I, L = range(6)

# tr : (nom, genitif, locatif, datif) ; les postpositions se construisent sur le genitif (masanın üstünde)
TR = {
    "tisch":   ("masa", "masanın", "masada", "masaya"),
    "kissen":  ("kırlent", "kırlentin", "kırlentte", "kırlente"),
    "stuhl":   ("sandalye", "sandalyenin", "sandalyede", "sandalyeye"),
    "sofa":    ("kanepe", "kanepenin", "kanepede", "kanepeye"),
    "schrank": ("dolap", "dolabın", "dolapta", "dolaba"),
    "regal":   ("kitaplık", "kitaplığın", "kitaplıkta", "kitaplığa"),
    "korb":    ("sepet", "sepetin", "sepette", "sepete"),
    "karton":  ("kutu", "kutunun", "kutuda", "kutuya"),
    "fenster": ("pencere", "pencerenin", "pencerede", "pencereye"),
    "tuer":    ("kapı", "kapının", "kapıda", "kapıya"),
    "pflanze": ("bitki", "bitkinin", "bitkide", "bitkiye"),
    "vorhang": ("perde", "perdenin", "perdede", "perdeye"),
    "tasche":  ("çanta", "çantanın", "çantada", "çantaya"),
    "lampe":   ("lamba", "lambanın", "lambada", "lambaya"),
    "bild":    ("tablo", "tablonun", "tabloda", "tabloya"),
    "wand":    ("duvar", "duvarın", "duvarda", "duvara"),
}
TR_PL = {
    "kissen": ("kırlentler", "kırlentlerin", "kırlentlerde", "kırlentlere"),
    "stuhl":  ("sandalyeler", "sandalyelerin", "sandalyelerde", "sandalyelere"),
}
# la postposition : (ou il est, ou il va), sur le genitif
TR_POST = {"auf": ("üstünde", "üstüne"), "unter": ("altında", "altına"), "in": ("içinde", "içine"), "vor": ("önünde", "önüne"),
           "hinter": ("arkasında", "arkasına"), "neben": ("yanında", "yanına"), "zwischen": ("arasında", "arasına")}


def _forme(table, pl_table, nom, pl, cas):
    return (pl_table[nom] if pl else table[nom])[cas]


def _so(nom):
    """« со » devant с, з, ш, ж + consonne (со столом, со шкафом, со шторой)."""
    return "со" if (nom[0] in "сзшж" and nom[1] not in "аеёиоуыэюя") else "с"


def _zi(nom):
    """« зі » devant с, з, ш, щ + consonne (зі столом, зі стільцем), « із » ailleurs apres « поруч »."""
    return "зі" if (nom[0] in "сзшщ" and nom[1] not in "аеєиіїоуюя") else "із"


def lieu(lg, prep, nom, cas, pl=False):
    """Le groupe allemand (prep + nom, au datif « dat » ou a l'accusatif « akk ») dans la langue lg."""
    wo = cas == "dat"
    if lg == "ru":
        f = lambda c: _forme(RU, RU_PL, nom, pl, c)
        if prep == "in" and nom == "regal":                    # dans l'etagere : sur l'etagere du meuble
            return "на полке стеллажа" if wo else "на полку стеллажа"
        if prep == "auf":    return "на " + (f(L) if wo else f(A))
        if prep == "unter":  return "под " + (f(I) if wo else f(A))
        if prep == "in":     return "в " + (f(L) if wo else f(A))
        if prep == "vor":    return "перед " + f(I)
        if prep == "hinter": return "за " + (f(I) if wo else f(A))
        if prep == "neben":  return "рядом " + _so(f(I)) + " " + f(I)
        if prep == "zwischen": return "между " + f(I)
        if prep == "über":   return ("над " + f(I)) if wo else ("через " + f(A))
        if prep == "an":
            if nom == "wand": return "на " + (f(L) if wo else f(A))
            return ("у " + f(G)) if wo else ("к " + f(D))
    if lg == "uk":
        f = lambda c: _forme(UK, UK_PL, nom, pl, c)
        if prep == "in" and nom == "regal":
            return "на полиці стелажа" if wo else "на полицю стелажа"
        if prep == "auf":    return "на " + (f(L) if wo else f(A))
        if prep == "unter":  return "під " + (f(I) if wo else f(A))
        if prep == "in":     return "у " + (f(L) if wo else f(A))
        if prep == "vor":    return "перед " + f(I)
        if prep == "hinter": return "за " + (f(I) if wo else f(A))
        if prep == "neben":  return "поруч " + _zi(f(I)) + " " + f(I)
        if prep == "zwischen": return "між " + f(I)
        if prep == "über":   return ("над " + f(I)) if wo else ("через " + f(A))
        if prep == "an":
            if nom == "wand": return "на " + (f(L) if wo else f(A))
            return ("біля " + f(G)) if wo else ("до " + f(G))
    if lg == "pl":
        f = lambda c: _forme(PL, PL_PL, nom, pl, c)
        if prep == "in" and nom == "regal":
            return "na półce regału" if wo else "na półkę regału"
        if prep == "auf":    return "na " + (f(L) if wo else f(A))
        if prep == "unter":  return "pod " + (f(I) if wo else f(A))
        if prep == "in":     return ("w " + f(L)) if wo else ("do " + f(G))
        if prep == "vor":    return "przed " + f(I)
        if prep == "hinter": return "za " + (f(I) if wo else f(A))
        if prep == "neben":  return "obok " + f(G)
        if prep == "zwischen": return "między " + f(I)
        if prep == "über":   return ("nad " + f(I)) if wo else ("przez " + f(A))
        if prep == "an":
            if nom == "wand": return "na " + (f(L) if wo else f(A))
            return ("przy " + f(L)) if wo else ("do " + f(G))
    if lg == "tr":
        t = TR_PL[nom] if pl else TR[nom]
        if prep == "in" and nom == "regal":
            return "kitaplığın rafında" if wo else "kitaplığın rafına"
        if prep in TR_POST:  return t[1] + " " + TR_POST[prep][0 if wo else 1]
        # au-dessus, sans contact : « üzerinde asılı » (yukarısında se comprend, un natif ne le dit pas ; relecture du 14 nov.)
        if prep == "über":   return t[1] + (" üzerinde" if wo else " üzerinden")
        if prep == "an":     return t[2] if wo else t[3]          # masada / masaya, pencerede / pencereye, duvarda / duvara
    raise SystemExit("langues.py : pas de groupe pour %s %s %s (%s)" % (prep, nom, cas, lg))


# ---------------------------------------------------------------------------------------------------------------
# LES PHRASES DES PLACES : « Die Katze sitzt auf dem Tisch. » / « Die Katze springt auf den Tisch. »
SUJET = {"ru": "Кот", "uk": "Кіт", "pl": "Kot", "tr": "Kedi"}
POSTURE = {"sitzt": {"ru": "сидит", "uk": "сидить", "pl": "siedzi", "tr": "oturuyor"},
           "liegt": {"ru": "лежит", "uk": "лежить", "pl": "leży", "tr": "yatıyor"}}
# le verbe du mouvement de chaque place (les verbes allemands suivent la place : springt, legt sich, kriecht, setzt
# sich, läuft, klettert) ; le groupe est celui de l'accusatif, sauf la ou la langue garde le meme cas (перед
# диваном, рядом с корзиной, między poduszkami) -- lieu() le sait deja
MOUVEMENT = {
    "legt sich": {"ru": "ложится", "uk": "лягає", "pl": "kładzie się", "tr": "yatıyor"},
    "springt":   {"ru": "прыгает", "uk": "стрибає", "pl": "wskakuje", "tr": "atlıyor"},
    "kriecht":   {"ru": "залезает", "uk": "залазить", "pl": "wchodzi", "tr": "giriyor"},
    "setzt sich": {"ru": "садится", "uk": "сідає", "pl": "siada", "tr": "oturuyor"},
    "läuft":     {"ru": "заходит", "uk": "заходить", "pl": "wchodzi", "tr": "geçiyor"},
    "klettert":  {"ru": "забирается", "uk": "залазить", "pl": "wspina się", "tr": "tırmanıyor"},
}
# « setzt sich ans Fenster » : on s'assoit A la fenetre, on ne s'assoit pas VERS elle (у окна, біля вікна, przy
# oknie, pencereye) ; « springt auf … » en polonais : wskakuje NA (stół, kanapę), mais DO (kartonu)
MOUVEMENT_LIEU = {("fenster-an", "ru"): "у окна", ("fenster-an", "uk"): "біля вікна", ("fenster-an", "pl"): "przy oknie"}


def _uk_v(avant, groupe):
    """L'alternance ukrainienne у / в : « в » apres une voyelle (лягає в кошик), « у » apres une consonne (лежить у
    кошику) ; seul, le groupe garde « у »."""
    if groupe.startswith("у ") and avant[-1] in "аеєиіїоуюя":
        return "в " + groupe[2:]
    return groupe


def phrase(lg, verbe, groupe, mouvement=False):
    """Le chat (sujet), son verbe, le groupe : dans l'ordre de la langue."""
    v = (MOUVEMENT if mouvement else POSTURE)[verbe][lg]
    if lg == "tr":
        return SUJET[lg] + " " + groupe + " " + v + "."
    if lg == "uk":
        groupe = _uk_v(v, groupe)
    return SUJET[lg] + " " + v + " " + groupe + "."


def place(lg, id, prep, nom, vWo, vWohin, pl):
    """(la phrase de position, la phrase du mouvement) d'une place du chat."""
    pos = phrase(lg, vWo, lieu(lg, prep, nom, "dat", pl))
    mv = MOUVEMENT_LIEU.get((id, lg)) or lieu(lg, prep, nom, "akk", pl)
    return pos, phrase(lg, vWohin, mv, mouvement=True)


# ---------------------------------------------------------------------------------------------------------------
# LES PHRASES A PART : les personnes, leurs gestes, les objets de la piece, le saut par-dessus le carton
PHRASES = {
    "Die Katze sitzt zwischen Ben und Mia.": {"ru": "Кот сидит между Беном и Мией.", "uk": "Кіт сидить між Беном і Мією.",
                                            "pl": "Kot siedzi między Benem a Mią.", "tr": "Kedi Ben ile Mia'nın arasında oturuyor."},
    "Die Katze liegt neben Mia.": {"ru": "Кот лежит рядом с Мией.", "uk": "Кіт лежить поруч із Мією.", "pl": "Kot leży obok Mii.",
                                   "tr": "Kedi Mia'nın yanında yatıyor."},
    "Anna legt die Katze in den Korb.": {"ru": "Анна кладёт кота в корзину.", "uk": "Анна кладе кота в кошик.",
                                         "pl": "Anna wkłada kota do kosza.", "tr": "Anna kediyi sepete koyuyor."},
    "Ben setzt die Katze auf den Tisch.": {"ru": "Бен сажает кота на стол.", "uk": "Бен садить кота на стіл.",
                                           "pl": "Ben sadza kota na stole.", "tr": "Ben kediyi masanın üstüne koyuyor."},
    "Die Lampe hängt über dem Tisch.": {"ru": "Лампа висит над столом.", "uk": "Лампа висить над столом.", "pl": "Lampa wisi nad stołem.",
                                        "tr": "Lamba masanın üzerinde asılı."},
    "Das Bild hängt über dem Sofa.": {"ru": "Картина висит над диваном.", "uk": "Картина висить над диваном.",
                                      "pl": "Obraz wisi nad kanapą.", "tr": "Tablo kanepenin üzerinde asılı."},
    "Das Bild hängt an der Wand.": {"ru": "Картина висит на стене.", "uk": "Картина висить на стіні.", "pl": "Obraz wisi na ścianie.",
                                    "tr": "Tablo duvarda asılı."},
    "Die Katze springt über den Karton.": {"ru": "Кот прыгает через коробку.", "uk": "Кіт стрибає через коробку.",
                                           "pl": "Kot skacze przez karton.", "tr": "Kedi kutunun üzerinden atlıyor."},
}
GROUPES = {
    "zwischen Ben und Mia": {"ru": "между Беном и Мией", "uk": "між Беном і Мією", "pl": "między Benem a Mią", "tr": "Ben ile Mia'nın arasında"},
    "neben Mia": {"ru": "рядом с Мией", "uk": "поруч із Мією", "pl": "obok Mii", "tr": "Mia'nın yanında"},
}
