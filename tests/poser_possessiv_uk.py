# -*- coding: utf-8 -*-
"""possessivExercises (70) : les possessifs allemands, tous cas, toutes personnes.

LE JEU EST UNE GRILLE, PAS UNE LISTE. Dix phrases-cadres x sept personnes.
On traduit les dix cadres et les sept personnes une fois, et on remplit --
c'est la methode des moules, comme pour le Perfekt et relativOrder.

DEUX CHOSES QUE L'UKRAINIEN FAIT AUTREMENT, ET QUI SONT ASSUMEES

  1. « son frere (a lui) » / « (a elle) ». Le francais doit gloser parce que
     « son » est ambigu ; l'ukrainien ne l'est pas -- його / її portent la
     distinction dans le mot. La glose disparait donc, et rien n'est perdu :
     l'ukrainophone lit exactement l'information que le francophone lit.

  2. « das Kind » est NEUTRE en allemand ; « дитина » est FEMININ en
     ukrainien. L'accord suit la langue qu'on ecrit, pas celle qu'on enseigne
     -- « моя дитина », jamais « моє дитина ». L'indice, lui, garde le genre
     ALLEMAND (сер.) : c'est lui que l'exercice demande.
"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- les cadres
# Chaque cadre : (determinant francais par personne, phrase francaise,
# phrase ukrainienne, forme ukrainienne du possessif a employer).
PERSONNES = ["1sg", "2sg", "3m", "3f", "1pl", "2pl", "3pl"]

# Les sept possessifs ukrainiens, dans les huit formes dont les cadres ont
# besoin. його et її sont invariables -- c'est la langue, pas un raccourci.
UK = {
 #            nom_m     nom_f    nom_pl   acc_m     acc_f    dat_m       dat_f     instr_f    gen_m
 "1sg":  ["мій",   "моя",   "мої",   "мого",    "мою",   "моєму",   "моїй",   "моєю",   "мого"],
 "2sg":  ["твій",  "твоя",  "твої",  "твого",   "твою",  "твоєму",  "твоїй",  "твоєю",  "твого"],
 "3m":   ["його",  "його",  "його",  "його",    "його",  "його",    "його",   "його",   "його"],
 "3f":   ["її",    "її",    "її",    "її",      "її",    "її",      "її",     "її",     "її"],
 "1pl":  ["наш",   "наша",  "наші",  "нашого",  "нашу",  "нашому",  "нашій",  "нашою",  "нашого"],
 "2pl":  ["ваш",   "ваша",  "ваші",  "вашого",  "вашу",  "вашому",  "вашій",  "вашою",  "вашого"],
 "3pl":  ["їхній", "їхня",  "їхні",  "їхнього", "їхню",  "їхньому", "їхній",  "їхньою", "їхнього"],
}
NOM_M, NOM_F, NOM_PL, ACC_M, ACC_F, DAT_M, DAT_F, INSTR_F, GEN_M = range(9)

# (determinants francais par personne, gabarit francais, gabarit ukrainien,
#  index de la forme ukrainienne, faut-il une majuscule au possessif)
CADRES = [
 (["Mon", "Ton", "Son frère (à lui)", "Son frère (à elle)", "Notre", "Votre", "Leur"],
  "%s frère est sympa.", "%s брат приємний.", NOM_M, True),
 (["Ma", "Ta", "Sa sœur (à elle)", "Sa sœur (à lui)", "Notre", "Votre", "Leur"],
  "%s sœur est intelligente.", "%s сестра розумна.", NOM_F, True),
 (["Mon", "Ton", "Son enfant (à lui)", "Son enfant (à elle)", "Notre", "Votre", "Leur"],
  "%s enfant joue dehors.", "%s дитина грається надворі.", NOM_F, True),
 (["Mes", "Tes", "Ses parents (à lui)", "Ses parents (à elle)", "Nos", "Vos", "Leurs"],
  "%s parents habitent à Berlin.", "%s батьки живуть у Берліні.", NOM_PL, True),
 (["mon", "ton", "son frère (à lui)", "son frère (à elle)", "notre", "votre", "leur"],
  "Peter voit %s frère.", "Петер бачить %s брата.", ACC_M, False),
 (["ma", "ta", "sa sœur (à elle)", "sa sœur (à lui)", "notre", "votre", "leur"],
  "Peter connaît %s sœur.", "Петер знає %s сестру.", ACC_F, False),
 (["mon", "ton", "son frère (à lui)", "son frère (à elle)", "notre", "votre", "leur"],
  "Peter aide %s frère.", "Петер допомагає %s братові.", DAT_M, False),
 (["ma", "ta", "sa sœur (à elle)", "sa sœur (à lui)", "notre", "votre", "leur"],
  "Peter remercie %s sœur.", "Петер дякує %s сестрі.", DAT_F, False),
 (["mon", "ton", "son enfant (à lui)", "son enfant (à elle)", "notre", "votre", "leur"],
  "Peter joue avec %s enfant.", "Петер грається з %s дитиною.", INSTR_F, False),
 (["mon", "ton", "son frère (à lui)", "son frère (à elle)", "notre", "votre", "leur"],
  "C'est la voiture de %s frère.", "Це машина %s брата.", GEN_M, False),
]


def table_traductions():
    """Les 70 phrases francaises et leur ukrainien, construites une fois."""
    t = {}
    for dets, gabfr, gabuk, forme, majuscule in CADRES:
        for det, pers in zip(dets, PERSONNES):
            # Le francais glose « son frere (a lui) » DANS le groupe nominal :
            # le determinant porte alors deja le nom, et %s le remplace en
            # entier. Sinon on colle simplement le determinant.
            fr = gabfr % det if " " not in det else gabfr.replace("%s frère", det) \
                                                         .replace("%s sœur", det) \
                                                         .replace("%s enfant", det) \
                                                         .replace("%s parents", det)
            uk = UK[pers][forme]
            t[fr] = gabuk % (uk[0].upper() + uk[1:] if majuscule else uk)
    return t


# ---------------------------------------------------------------- les indices
GENRES = {"masc.": "чол.", "fém.": "жін.", "neutre": "сер.", "pluriel": "мн."}
GLOSES = {"« à lui »": "« його »", "« à elle »": "« її »", "« à eux »": "« їхній »"}


def traduire_indice(h):
    m = re.match(r"^\((\w+ \w+), (\w+), ([^,)—]+?)"
                 r"(?:, (« à (?:lui|elle|eux) »))?"
                 r"(?: — attention au piège)?\)$", h)
    if not m:
        return None
    nom, cas, genre, glose = m.group(1), m.group(2), m.group(3).strip(), m.group(4)
    if genre not in GENRES:
        return None
    bouts = [nom, cas, GENRES[genre]]
    if glose:
        bouts.append(GLOSES[glose])
    piege = " — увага, пастка" if "attention au piège" in h else ""
    return "(" + ", ".join(bouts) + piege + ")"


# ----------------------------------------------------------- les explications
CAS = {"Nominatif": "Nominativ", "Accusatif": "Akkusativ",
       "Datif": "Dativ", "Génitif": "Genitiv"}
GENRE_LONG = {"masculin": "чоловічий рід", "féminin": "жіночий рід",
              "neutre": "середній рід", "pluriel": "множина"}

# ⚠️ L'ORDRE COMPTE, ET C'EST UN PIEGE DEJA RENCONTRE. Le 9 septembre, sur les
# suffixes du Konjunktiv II, « + infinitif » a ete remplace avant le suffixe
# plus long qui le contenait, et l'interieur repartait a moitie en francais.
# On va donc du plus long au plus court, toujours.
CORPS = [
 ("le possessif ne prend pas de terminaison",
  "присвійний займенник не бере закінчення"),
 ("comme le masculin, terminaison -em", "як чоловічий, закінчення -em"),
 ("comme le masculin, pas de terminaison", "як чоловічий, без закінчення"),
 ("comme le nominatif, terminaison -e", "як Nominativ, закінчення -e"),
 ("terminaison -en", "закінчення -en"),
 ("terminaison -em", "закінчення -em"),
 ("terminaison -er", "закінчення -er"),
 ("terminaison -es", "закінчення -es"),
 ("terminaison -e", "закінчення -e"),
]
EUER = (", et « euer » perd son 2e e", ", а « euer » втрачає друге e")
PAS = {" (pas « euere »).": " (не « euere »).", " (pas « eueren »).": " (не « eueren »)."}

# Les deux phrases de « euer » qui ne suivent aucun moule : elles ne servent
# qu'une fois chacune, et les recopier vaut mieux que de tordre un gabarit.
UNIQUES = {
 "Nominatif masculin, pas de terminaison : la forme reste « euer » "
 "(rien à perdre ici, pas de terminaison ajoutée).":
 "Nominativ, чоловічий рід, без закінчення: форма лишається « euer » "
 "(тут нічого втрачати — закінчення не додається).",
 "Nominatif neutre, comme le masculin, pas de terminaison : euer.":
 "Nominativ, середній рід, як чоловічий, без закінчення: euer.",
}


def traduire_explication(x):
    if x in UNIQUES:
        return UNIQUES[x]
    m = re.match(r"^(\w+) (\w+) : (.+?) → (\S+?)(\.| \(pas « \w+ »\)\.)$", x)
    if not m:
        return None
    cas, genre, corps, forme, fin = m.groups()
    if cas not in CAS or genre not in GENRE_LONG:
        return None
    euer = EUER[0] in corps
    if euer:
        corps = corps.replace(EUER[0], "")
    for fr, uk in CORPS:
        if corps == fr:
            corps = uk
            break
    else:
        return None
    if euer:
        corps += EUER[1]
    fin = PAS.get(fin, ".") if fin != "." else "."
    return "%s, %s: %s → %s%s" % (CAS[cas], GENRE_LONG[genre], corps, forme, fin)


# ------------------------------------------------------------------- le travail
def main():
    T = table_traductions()
    d = json.load(io.open(os.path.join(R, "exercices.json"), encoding="utf-8"))
    entrees, rates = [], []
    for e in d["jeux"]["possessivExercises"]:
        fr, h, x = e["translation"], e.get("hint", ""), e["explanation"]
        uk_t, uk_h, uk_x = T.get(fr), traduire_indice(h), traduire_explication(x)
        if not uk_t:
            rates.append("TRAD : " + fr)
            continue
        if not uk_h:
            rates.append("INDICE : " + h)
            continue
        if not uk_x:
            rates.append("EXPL : " + x)
            continue
        # « ___ Bruder ist nett. » sert a sept exercices : la question ne
        # suffit pas a designer une ligne, la traduction francaise si.
        entrees.append({"question": e["question"], "cle_translation": fr,
                        "translation_uk": uk_t, "hint_uk": uk_h,
                        "explanation_uk": uk_x})
    if rates:
        print("REFUS : %d" % len(rates))
        for r in rates[:12]:
            print("   " + r)
        sys.exit(1)
    dossier = os.path.join(R, "corrections_uk")
    os.makedirs(dossier, exist_ok=True)
    io.open(os.path.join(dossier, "exos_possessiv.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps({"jeu": "possessivExercises", "entrees": entrees},
                   ensure_ascii=False, indent=1) + "\n")
    print("exos_possessiv.json : %d entrees" % len(entrees))


if __name__ == "__main__":
    main()
