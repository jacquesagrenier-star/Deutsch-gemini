# -*- coding: utf-8 -*-
"""Theme illustre des Soins, chapitre 7 : la douleur (soins-theme-schmerz). Decision de Jacques du 16 nov. 2026.

    python pflege/outils/themes_soins/schmerz.py      # ecrit visuel/prototype/soins-theme-schmerz/donnees.json

L'ANGLE (regle 2 des themes : pas de scene refaite). La scene de la chambre (soins-zimmer) fait nommer les objets
du lit ; ici, la douleur elle-meme, comme on la recueille au lit du patient :
  - OU : les patients connus (Herr Brandt, Frau Lehmann, Frau Weber, Herr Schulze, Frau Kowalski) montrent ou ils
    ont mal ; « Herr Brandt hat Schmerzen in der Hüfte », « Mir tut die Hüfte weh » (wehtun + nominatif, l'article) ;
  - COMBIEN : l'echelle numerique de 0 a 10, DESSINEE par la page (aucun chiffre dans une image generee) ; le nombre
    se dit en lettres (« eine Sieben »), et ce qu'il veut dire (leicht 1-3, mittelstark 4-6, stark 7-10) ⚕️ ;
  - COMMENT : ce que dit le patient (« Es sticht wie ein Messer. ») -> le caractere (stechend, brennend, dumpf,
    ziehend, druckend), et la terminaison de l'adjectif (ein stechender Schmerz, stechende Schmerzen) ;
  - LES DEUX LANGUES : ce que dit le patient et ce qu'ecrit le service (« das Bauchweh » -> die Abdominalschmerzen),
    les paires du corpus (pflege/datos/themes.json, sorte « paire »), dans les deux sens.
Les images : une par patient et par endroit (IMAGES ci-dessous), faites a l'etape 2 (fal, 0,15 $ l'image, lot annonce
a Jacques). Les personnes sont celles de la Pflege (pflege/PERSONNAGES.md), jamais Anna, sa famille ni Mark.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import Theme  # noqa: E402

T = Theme("schmerz")

# ---------- les personnes (pflege/sources/noms.json) ----------
P = {
    "brandt":   {"de": "Herr Brandt",   "fr": "M. Brandt",     "er": "er"},
    "lehmann":  {"de": "Frau Lehmann",  "fr": "Mme Lehmann",   "er": "sie"},
    "weber":    {"de": "Frau Weber",    "fr": "Mme Weber",     "er": "sie"},
    "schulze":  {"de": "Herr Schulze",  "fr": "M. Schulze",    "er": "er"},
    "kowalski": {"de": "Frau Kowalski", "fr": "Mme Kowalski",  "er": "sie"},
}

# ---------- les parties du corps : le mot du corpus, « in » + datif, le francais « a mal a » ----------
# compose : la forme ou l'on dit d'abord le mot compose (Kopfschmerzen), et le mot du corpus qu'elle fait travailler
K = {
    "huefte":   {"mot": "die Hüfte",   "in": "in der Hüfte",   "fr": "à la hanche",  "nom_fr": "La hanche"},
    "ruecken":  {"mot": "der Rücken",  "in": "im Rücken",      "fr": "au dos",       "nom_fr": "Le dos"},
    "knie":     {"mot": "das Knie",    "in": "im Knie",        "fr": "au genou",     "nom_fr": "Le genou"},
    "fuss":     {"mot": "der Fuß",     "in": "im Fuß",         "fr": "au pied",      "nom_fr": "Le pied"},
    "kopf":     {"mot": "der Kopf",    "in": "im Kopf",        "fr": "à la tête",    "nom_fr": "La tête",   "compose": "Kopfschmerzen"},
    "hand":     {"mot": "die Hand",    "in": "in der Hand",    "fr": "à la main",    "nom_fr": "La main"},
    "schulter": {"mot": "die Schulter","in": "in der Schulter","fr": "à l'épaule",   "nom_fr": "L'épaule"},
    "bauch":    {"mot": "der Bauch",   "in": "im Bauch",       "fr": "au ventre",    "nom_fr": "Le ventre", "compose": "Bauchschmerzen"},
    "hals":     {"mot": "der Hals",    "in": "im Hals",        "fr": "à la gorge",   "nom_fr": "La gorge",  "compose": "Halsschmerzen"},
    "bein":     {"mot": "das Bein",    "in": "im Bein",        "fr": "à la jambe",   "nom_fr": "La jambe"},
    "arm":      {"mot": "der Arm",     "in": "im Arm",         "fr": "au bras",      "nom_fr": "Le bras"},
}

# ---------- les images : une personne, un endroit (decrites ici, faites a l'etape 2) ----------
IMAGES = [
    ("brandt", "huefte",   "Herr Brandt, assis au bord de son lit, la main sur la hanche droite, le visage crispé de douleur."),
    ("brandt", "ruecken",  "Herr Brandt, debout près du lit, la main au creux des reins, légèrement penché."),
    ("brandt", "knie",     "Herr Brandt, assis sur une chaise près du lit, les deux mains autour du genou droit."),
    ("lehmann", "fuss",    "Frau Lehmann, assise, le pied droit pansé posé sur un tabouret, elle montre son pied du doigt."),
    ("lehmann", "kopf",    "Frau Lehmann, dans un fauteuil, la main sur le front et les yeux mi-clos."),
    ("weber", "hand",      "Frau Weber, assise à table, tient sa main gauche dans sa main droite, la grimace aux lèvres."),
    ("weber", "schulter",  "Frau Weber, assise, la main droite posée sur l'épaule gauche."),
    ("schulze", "bauch",   "Herr Schulze, assis sur une chaise, les deux mains sur le ventre, un peu courbé."),
    ("schulze", "hals",    "Herr Schulze, assis, la main sur la gorge, l'air de mal avaler."),
    ("kowalski", "bein",   "Frau Kowalski, dans son fauteuil, chez elle, la main sur le bas de la jambe."),
    ("kowalski", "arm",    "Frau Kowalski, assise, tient son bras droit plié contre elle."),
]
for p, k, alt in IMAGES:
    T.image(p + "-" + k, alt, personne=p, endroit=k)
NOMS_IMG = [p + "-" + k for p, k, _ in IMAGES]
VISAGE = {p: next(p + "-" + k for q, k, _ in IMAGES if q == p) for p in P}

ART = {"der": "Der", "die": "Die", "das": "Das"}
FR_ART = {"der": "le", "die": "la", "das": "le"}


def lieu(p, k, phrase=True):
    """« Herr Brandt hat Schmerzen in der Hüfte. » / « Frau Lehmann hat Kopfschmerzen. » -- phrase=False : un enonce
    faux du « vrai ou faux », jamais montre traduit, donc sans traduction a faire."""
    c = K[k].get("compose")
    de = P[p]["de"] + " hat " + (c if c else "Schmerzen " + K[k]["in"]) + "."
    return T.phrase(de, P[p]["fr"] + " a mal " + K[k]["fr"] + ".") if phrase else de


def mir(k):
    """« Mir tut die Hüfte weh. » -- wehtun : la partie du corps est le sujet, au nominatif."""
    de = "Mir tut " + K[k]["mot"] + " weh."
    return T.phrase(de, "J'ai mal " + K[k]["fr"] + ".")


def tut(k):
    """« Die Hüfte tut weh. »"""
    art, nom = K[k]["mot"].split(" ", 1)
    return T.phrase(ART[art] + " " + nom + " tut weh.", K[k]["nom_fr"] + " fait mal.")


# ---------- les mots et les consignes ----------
for k in K:
    T.mot(K[k]["mot"])
T.texte("titre", "La douleur")
T.texte("intro", "Touche une image : le patient te dit où il a mal. Puis l'échelle de la douleur, et les mots pour dire comment ça fait mal.")
T.texte("regle", "« Mir tut der Rücken weh » : avec wehtun, la partie du corps est le sujet (nominatif), la personne est au datif (mir, ihm, ihr). Au pluriel : « Mir tun die Füße weh ».")
T.texte("wo", "Regarde l'image : où le patient a-t-il mal ?")
T.texte("sagt", "Regarde l'image : que dit le patient ?")
T.texte("vraifaux", "Regarde l'image : vrai ou faux ?")
T.texte("ecoute", "Écoute le patient et touche la bonne image.")
T.texte("artikel", "Choisis le bon article.")

for p, k, _ in IMAGES:
    w = T.rang[K[k]["mot"]]
    img = p + "-" + k
    juste = lieu(p, k)
    # OU : « Wo hat Herr Brandt Schmerzen? » -- in + datif
    autres = [x for x in K if x != k]
    for n in range(4):
        leurres = [K[x]["in"] for x in autres[n * 2: n * 2 + 3]] if n < 3 else [K[x]["in"] for x in autres[-3:]]
        T.question("wo", w, "wo", K[k]["in"], juste, choix=[K[k]["in"]] + leurres, visuel={"img": img},
                   enonce="Wo hat " + P[p]["de"] + " Schmerzen?", centre=True)
    # QUE DIT-IL : « Mir tut die Hüfte weh. »
    for n in range(3):
        leurres = [mir(x) for x in autres[n * 3: n * 3 + 3]]
        T.question("sagt", w, "sagt", mir(k), mir(k), choix=[mir(k)] + leurres, visuel={"img": img},
                   enonce="Was sagt " + P[p]["de"] + "?")
    # VRAI OU FAUX : la phrase juste, ou la meme avec un autre endroit (toujours faux pour l'image)
    T.question("vraifaux", w, "vraifaux", "Richtig", juste, choix=["Richtig", "Falsch"], visuel={"img": img},
               enonce=juste, centre=True, ordre_fixe=True)
    for x in autres[:4]:
        T.question("vraifaux", w, "vraifaux", "Falsch", juste, choix=["Richtig", "Falsch"], visuel={"img": img},
                   enonce=lieu(p, x, False), centre=True, ordre_fixe=True)
    # L'ECOUTE : « Mir tut die Hüfte weh. » -> l'image, parmi deux autres endroits
    for n in range(3):
        autres_img = [i for i in NOMS_IMG if T.images[i]["endroit"] != k]
        T.question("ecoute", w, "ecoute", img, juste, images=[img] + autres_img[n * 3: n * 3 + 2], ecoute=mir(k))
    # L'ARTICLE : « ___ Hüfte tut weh. »
    art, nom = K[k]["mot"].split(" ", 1)
    T.question("artikel", w, "artikel", ART[art], tut(k), choix=["Der", "Die", "Das"], visuel={"img": img},
               enonce="___ " + nom + " tut weh.", centre=True, ordre_fixe=True)
    T.glose(K[k]["in"], K[k]["fr"])

# ---------- l'echelle de la douleur (NRS), dessinee ----------
ZAHL = ["Null", "Eins", "Zwei", "Drei", "Vier", "Fünf", "Sechs", "Sieben", "Acht", "Neun", "Zehn"]
STUFE = [("keine Schmerzen", "pas de douleur")] + [("leichte Schmerzen", "des douleurs légères")] * 3 \
    + [("mittelstarke Schmerzen", "des douleurs modérées")] * 3 + [("starke Schmerzen", "des douleurs fortes")] * 4
skala = T.mot("die Schmerzskala")
T.texte("echelle", "Regarde l'échelle : quel chiffre le patient montre-t-il ?")
T.texte("stufe", "Regarde l'échelle : ce sont des douleurs de quelle force ?")
for n in range(11):
    eine = "eine " + ZAHL[n]
    T.glose(eine, str(n), partout=True)
    stufe_de, stufe_fr = STUFE[n]
    ph_stufe = T.phrase(("Eine " + ZAHL[n] + " heißt: " if n == 0 else "Eine " + ZAHL[n] + ": Das sind ") + stufe_de + ".",
                        ("Zéro veut dire : " if n == 0 else "%d : ce sont " % n) + stufe_fr + ".")
    for p in P:
        ph = T.phrase(P[p]["de"] + " zeigt auf der Schmerzskala " + eine + ".",
                      P[p]["fr"] + " montre %d sur l'échelle de la douleur." % n)
        voisins = [x for x in (n - 1, n + 1, (n + 5) % 11) if 0 <= x <= 10 and x != n]
        T.question("echelle", skala, "echelle", eine, ph, choix=[eine] + ["eine " + ZAHL[x] for x in voisins],
                   visuel=[{"img": VISAGE[p]}, {"echelle": n}], enonce="Welche Zahl zeigt " + P[p]["de"] + "?", centre=True)
    T.question("stufe", skala, "stufe", stufe_de, ph_stufe,
               choix=["keine Schmerzen", "leichte Schmerzen", "mittelstarke Schmerzen", "starke Schmerzen"],
               visuel={"echelle": n}, enonce="Eine " + ZAHL[n] + " auf der Schmerzskala: Was bedeutet das?", ordre_fixe=True)
for de, fr in set(STUFE):
    T.glose(de, fr)

# ---------- le caractere de la douleur : ce que dit le patient -> l'adjectif ----------
# Les citations sont celles du corpus quand il en a (« Es sticht wie ein Messer. », paire « stechende Schmerzen »).
CAR = {
    "stechend": {"fr": "lancinante", "fr_pl": "lancinantes", "dit": ["Es sticht wie ein Messer.", "Es sticht, wenn ich mich bewege."]},
    "brennend": {"fr": "brûlante", "fr_pl": "brûlantes", "dit": ["Es brennt wie Feuer.", "Es brennt die ganze Zeit."]},
    "dumpf":    {"fr": "sourde", "fr_pl": "sourdes", "dit": ["Es tut tief drin weh, nicht spitz.", "Es ist kein spitzer Schmerz, eher tief und schwer."]},
    "ziehend":  {"fr": "qui tire", "fr_pl": "qui tirent", "dit": ["Es zieht, wenn ich den Arm hebe.", "Es zieht und spannt."]},
    "drückend": {"fr": "oppressante", "fr_pl": "oppressantes", "dit": ["Es drückt wie ein schwerer Stein.", "Es drückt die ganze Zeit."]},
}
CIT_FR = {"Es sticht wie ein Messer.": "Ça pique comme un couteau.", "Es sticht, wenn ich mich bewege.": "Ça pique quand je bouge.",
          "Es brennt wie Feuer.": "Ça brûle comme du feu.", "Es brennt die ganze Zeit.": "Ça brûle tout le temps.",
          "Es tut tief drin weh, nicht spitz.": "Ça fait mal tout au fond, pas en pointe.",
          "Es ist kein spitzer Schmerz, eher tief und schwer.": "Ce n'est pas une douleur aiguë, plutôt profonde et lourde.",
          "Es zieht, wenn ich den Arm hebe.": "Ça tire quand je lève le bras.", "Es zieht und spannt.": "Ça tire et ça tend.",
          "Es drückt wie ein schwerer Stein.": "Ça appuie comme une lourde pierre.", "Es drückt die ganze Zeit.": "Ça appuie tout le temps."}
T.texte("art", "Lis ce que dit le patient : quelle douleur est-ce ?")
T.texte("endung", "Choisis la bonne terminaison de l'adjectif.")
ADJ = list(CAR)
for a in ADJ:
    w = T.mot(a)
    T.glose(a, CAR[a]["fr"])
    ein = T.phrase("Das ist ein " + a + "er Schmerz.", "C'est une douleur " + CAR[a]["fr"] + ".")
    for i, cit in enumerate(CAR[a]["dit"]):
        T.phrase(cit, CIT_FR[cit])
        for j, p in enumerate(P):
            leurres = [x for x in ADJ if x != a]
            leurres = leurres[(i + j) % 4:] + leurres[:(i + j) % 4]
            T.question("art", w, "art", a, ein, choix=[a] + leurres[:3], visuel={"cite": cit, "visage": VISAGE[p]},
                       enonce=P[p]["de"] + " sagt: „" + cit + "“ Welcher Schmerz ist das?", dit=cit + " " + ein)
    # la terminaison : ein stechender Schmerz / stechende Schmerzen / der Schmerz ist stechend
    T.question("endung", w, "endung", a + "er", ein, choix=[a + "er", a + "e", a + "es"],
               enonce="Das ist ein ___ Schmerz.", centre=True)
    T.question("endung", w, "endung", a, T.phrase("Der Schmerz ist " + a + ".", "La douleur est " + CAR[a]["fr"] + "."),
               choix=[a, a + "er", a + "e"], enonce="Der Schmerz ist ___.", centre=True)
    for p in P:
        ph = T.phrase(P[p]["de"] + " hat " + a + "e Schmerzen.", P[p]["fr"] + " a des douleurs " + CAR[a]["fr_pl"] + ".")
        T.question("endung", w, "endung", a + "e", ph, choix=[a + "e", a + "er", a], visuel={"img": VISAGE[p]},
                   enonce=P[p]["de"] + " hat ___ Schmerzen.", centre=True)

# ---------- ce que dit le patient, ce qu'ecrit le service (les paires du corpus) ----------
PAIRES = ["die Abdominalschmerzen", "stechende Schmerzen", "ausstrahlende Schmerzen", "die thorakalen Schmerzen",
          "die Lumbalgie", "die Parästhesien", "die Dysurie", "der Juckreiz", "das Analgetikum", "die Übelkeit",
          "der Schwindel", "die Atemnot", "die Beinödeme"]
T.texte("service", "Le patient le dit avec ses mots : qu'écris-tu dans le rapport de soins ?")
T.texte("patient", "C'est écrit dans le rapport : comment le patient le dit-il ?")
corp = T.corpus
for i, s in enumerate(PAIRES):
    m = corp["paire:" + s]
    w = T.mot("paire:" + s)
    pat = m["patient"]
    T.glose(s, m["traduction"])
    T.glose(pat, m["traduction_patient"])
    ph = T.phrase("Der Patient sagt: „" + pat + "“ – im Bericht steht: " + s + ".",
                  "Le patient dit : « " + m["traduction_patient"] + " » – dans le rapport : " + m["traduction"] + ".")
    autres = [x for x in PAIRES if x != s]
    for n in range(2):
        leurres = autres[(i + n * 3) % len(autres):][:3]
        if len(leurres) < 3:
            leurres += autres[:3 - len(leurres)]
        T.question("service", w, "service", s, ph, choix=[s] + leurres, visuel={"cite": pat},
                   enonce="Was schreiben Sie in den Pflegebericht?")
        T.question("patient", w, "patient", pat, ph, choix=[pat] + [corp["paire:" + x]["patient"] for x in leurres],
                   enonce="Im Bericht steht: " + s + ". Wie hat es der Patient gesagt?")

# ---------- la decouverte ----------
for p, k, _ in IMAGES:
    T.decouverte.append({"visuel": {"img": p + "-" + k}, "texte": mir(k), "court": K[k]["mot"].split(" ", 1)[1],
                         "dit": lieu(p, k)})
T.decouverte.append({"visuel": {"echelle": 7}, "texte": T.phrase("Die Schmerzskala geht von null bis zehn.",
                     "L'échelle de la douleur va de zéro à dix."), "court": "0 – 10",
                     "dit": T.phrase("Null heißt: keine Schmerzen. Zehn heißt: die stärksten Schmerzen.",
                                     "Zéro veut dire : pas de douleur. Dix veut dire : la pire douleur imaginable.")})
for a in ADJ:
    T.decouverte.append({"visuel": {"cite": CAR[a]["dit"][0]}, "texte": "Das ist ein " + a + "er Schmerz.", "court": a,
                         "dit": CAR[a]["dit"][0]})
T.ecrire({"bravo": "Sehr gut!"})
