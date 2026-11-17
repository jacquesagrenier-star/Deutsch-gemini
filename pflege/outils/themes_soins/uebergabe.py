# -*- coding: utf-8 -*-
"""Theme illustre des Soins, chapitre 8 : la releve (soins-theme-uebergabe). Decision de Jacques du 16 nov. 2026.

    python pflege/outils/themes_soins/uebergabe.py    # ecrit visuel/prototype/soins-theme-uebergabe/donnees.json

L'ANGLE (regle 2 : pas de scene refaite). La scene de la releve (soins-uebergabe) se passe au lit de Frau Lehmann ;
ici, la FEUILLE DE RELEVE et ce qu'on en dit a voix haute :
  - la feuille d'un patient, DESSINEE par la page (la regle des papiers : aucun texte dans une image generee), avec
    ses abreviations (Z.n., VW, BZ, NRS, li., re.) : on y lit le motif, les valeurs, ce qui reste a faire ;
  - les abreviations de la documentation (pflege/datos/themes.json), dans les deux sens, et leur lecture (« Be-Zett ») ;
  - le passif et le Perfekt des transmissions (« Der Verband wurde gewechselt », « Er ist operiert worden ») ;
  - objectif, sans jugement (« Mobilisation abgelehnt, wegen Angst vor einem Sturz », pas « Er ist faul ») ;
  - l'ordre de la releve : d'abord qui et pourquoi, a la fin ce qui reste a faire.
Les patients et leurs faits sont ceux des dialogues (d06 la releve, d08 la chute, d09 le repas, d10 les medicaments,
d12 la nuit) ; ce qui n'y est pas est marque ⚕️ a relire. Les valeurs s'ecrivent en chiffres sur la feuille (un papier
se lit) et se DISENT en lettres (regle 4). Aucune image a payer : les visages des patients existent.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import Theme  # noqa: E402

T = Theme("uebergabe")

# ---------- les patients et leur feuille ----------
# lieu, zimmer (ecrit, dit), age (dit), grund (feuille, dit), werte [(abk ecrite, heure ecrite, heure dite, valeur
# ecrite, valeur dite, mot du corpus)], verlauf [(feuille, phrase dite, fr)], offen [(feuille, dit, fr)]
P = {
    "lehmann": {
        "de": "Frau Lehmann", "fr": "Mme Lehmann", "lieu": "Station 4B", "zimmer": ("14", "vierzehn"), "alter": ("74", "vierundsiebzig"),
        "grund": ("Wunde re. Fuß bei Diabetes", "eine Wunde am rechten Fuß bei Diabetes", "une plaie au pied droit sur un diabète"),
        "werte": [("BZ", "7:00", "sieben Uhr", "180", "hundertachtzig", "der Blutzucker"),
                  ("BZ", "12:00", "zwölf Uhr", "140", "hundertvierzig", "der Blutzucker")],
        "verlauf": [("Nacht ruhig", "Die Nacht war ruhig.", "La nuit a été calme."),
                    ("VW heute früh: Wunde reizlos", "Der Verband wurde heute früh gewechselt, die Wunde ist reizlos.",
                     "Le pansement a été changé ce matin, la plaie est calme.")],
        "offen": [("BZ um 14:00", "Um vierzehn Uhr muss der Blutzucker gemessen werden.", "À 14 h, il faut mesurer la glycémie."),
                  ("Tochter: Gespräch mit Dr. Sommer morgen 10:00", "Die Tochter möchte morgen um zehn mit Dr. Sommer sprechen.",
                   "La fille voudrait parler avec la docteure Sommer demain à 10 h.")],
    },
    "brandt": {
        "de": "Herr Brandt", "fr": "M. Brandt", "lieu": "Station 4B", "zimmer": ("12", "zwölf"), "alter": ("82", "zweiundachtzig"),
        "grund": ("Z.n. Hüft-TEP re. nach Sturz", "eine neue Hüfte rechts nach einem Sturz", "une prothèse de hanche droite après une chute"),
        "werte": [("NRS", "10:00", "zehn Uhr", "7", "sieben", "NRS (= numerische Ratingskala)"),
                  ("NRS", "10:30", "halb elf", "3", "drei", "NRS (= numerische Ratingskala)")],
        "verlauf": [("Schmerzmittel n.B. um 10:00", "Er hat um zehn Uhr sein Schmerzmittel bei Bedarf bekommen.",
                     "Il a eu son antalgique si besoin à 10 h."),
                    ("Mobilisation abgelehnt (Angst vor Sturz)", "Die Mobilisation hat er abgelehnt, wegen Angst vor einem Sturz.",
                     "Il a refusé la mobilisation, par peur de tomber.")],
        "offen": [("Mobilisation am Nachmittag erneut anbieten", "Am Nachmittag soll die Mobilisation noch einmal angeboten werden.",
                   "Cet après-midi, il faut lui reproposer la mobilisation.")],
    },
    "weber": {
        "de": "Frau Weber", "fr": "Mme Weber", "lieu": "Haus Lindenhof", "zimmer": ("7", "sieben"), "alter": ("81", "einundachtzig"),
        "grund": ("Sturz heute Nacht, li. Handgelenk schmerzhaft", "ein Sturz heute Nacht, das linke Handgelenk tut weh",
                  "une chute cette nuit, le poignet gauche douloureux"),
        "werte": [("NRS", "6:00", "sechs Uhr", "5", "fünf", "NRS (= numerische Ratingskala)")],
        "verlauf": [("kein Kopfanprall", "Sie ist nicht mit dem Kopf aufgeschlagen.", "Elle ne s'est pas cogné la tête."),
                    ("Hausärztin informiert, Sturzprotokoll geschrieben", "Die Hausärztin wurde informiert, das Sturzprotokoll ist geschrieben.",
                     "La médecin traitante a été informée, le rapport de chute est écrit.")],
        "offen": [("Röntgen li. Handgelenk um 11:00", "Um elf Uhr wird das linke Handgelenk geröntgt.", "À 11 h, on fait une radio du poignet gauche.")],
    },
    "schulze": {
        "de": "Herr Schulze", "fr": "M. Schulze", "lieu": "Haus Lindenhof", "zimmer": ("3", "drei"), "alter": ("87", "siebenundachtzig"),
        "grund": ("Demenz, nachts unruhig", "eine Demenz, nachts ist er unruhig", "une démence, il est agité la nuit"),
        "werte": [("Temp.", "7:00", "sieben Uhr", "36,8", "sechsunddreißig Komma acht", "Temp. (= Temperatur)")],
        "verlauf": [("3:00 im Flur, wollte zur Arbeit, ließ sich beruhigen",
                     "Um drei Uhr war er im Flur, er wollte zur Arbeit; er hat sich beruhigen lassen.",
                     "À 3 h, il était dans le couloir, il voulait aller au travail ; il s'est laissé calmer."),
                    ("Mittagessen: verschluckt, gut abgehustet", "Beim Mittagessen hat er sich verschluckt und gut abgehustet.",
                     "Au déjeuner, il a avalé de travers et a bien toussé.")],
        "offen": [("beim Essen aufrecht sitzen lassen", "Beim Essen soll er aufrecht sitzen.", "Pendant le repas, il doit être assis droit.")],
    },
    "kowalski": {
        "de": "Frau Kowalski", "fr": "Mme Kowalski", "lieu": "Ambulanter Dienst", "zimmer": None, "alter": ("79", "neunundsiebzig"),
        "grund": ("Diabetes, Bluthochdruck", "Diabetes und Bluthochdruck", "un diabète et une hypertension"),
        "werte": [("BZ", "8:00", "acht Uhr", "210", "zweihundertzehn", "der Blutzucker")],
        "verlauf": [("Insulin nach Schema", "Sie hat ihr Insulin nach Schema bekommen.", "Elle a eu son insuline selon le schéma."),
                    ("neu: Ramipril 1x tgl. morgens", "Sie nimmt neu Ramipril, einmal täglich am Morgen.",
                     "Elle prend depuis peu du ramipril, une fois par jour le matin.")],
        "offen": [("Apotheke: Ramipril teilen?", "Die Apotheke soll gefragt werden, ob man Ramipril teilen darf.",
                   "Il faut demander à la pharmacie si l'on peut couper le ramipril.")],
    },
}
VISAGE = {p: "visage-" + p for p in P}
for p in P:
    T.image(VISAGE[p], "Le visage de " + P[p]["fr"] + ".", personne=p)


def feuille(p):
    """La feuille de releve d'un patient, en HTML (allemand, lue a 375 px)."""
    d = P[p]
    lignes = [("Zimmer" if d["zimmer"] else "Klientin", (d["zimmer"][0] + " – " if d["zimmer"] else "") + d["de"] + ", " + d["alter"][0] + " J.")]
    lignes.append(("Grund", d["grund"][0]))
    for abk, h, _, v, _, _ in d["werte"]:
        lignes.append((abk + " " + h, v))
    for f, _, _ in d["verlauf"]:
        lignes.append(("Verlauf", f))
    for f, _, _ in d["offen"]:
        lignes.append(("Offen", f))
    return ('<div class="titrePapier">Übergabe · ' + d["lieu"] + '</div><table>'
            + "".join("<tr><th>" + a + "</th><td>" + b + "</td></tr>" for a, b in lignes) + "</table>")


def qui(p):
    """La premiere phrase d'une releve : qui (et la chambre), l'age."""
    d = P[p]
    if d["zimmer"]:
        de = "Zimmer " + d["zimmer"][1] + ": " + d["de"] + ", " + d["alter"][1] + " Jahre."
        fr = "Chambre " + d["zimmer"][0] + " : " + d["fr"] + ", " + d["alter"][0] + " ans."
    else:
        de = "Bei " + d["de"] + ", " + d["alter"][1] + " Jahre."
        fr = "Chez " + d["fr"] + ", " + d["alter"][0] + " ans."
    return T.phrase(de, fr)


def grund(p):
    d = P[p]
    return T.phrase(d["de"] + " hat " + d["grund"][1] + "." if not d["grund"][1].startswith("ein Sturz") and not d["grund"][1].startswith("eine neue")
                    else ({"weber": d["de"] + " ist heute Nacht gestürzt, das linke Handgelenk tut weh.",
                           "brandt": d["de"] + " hat nach einem Sturz eine neue Hüfte rechts bekommen."}[p]),
                    d["fr"] + " a " + d["grund"][2] + "." if p not in ("weber", "brandt") else
                    {"weber": "Mme Weber est tombée cette nuit, le poignet gauche lui fait mal.",
                     "brandt": "M. Brandt a eu une nouvelle hanche droite après une chute."}[p])


T.texte("titre", "La relève")
T.texte("intro", "Touche un patient : tu vois sa feuille de relève et tu entends comment on la transmet. Les abréviations se lisent à voix haute.")
T.texte("regle", "Une relève a un ordre : d'abord qui et pourquoi, puis ce qui s'est passé, à la fin ce qui reste à faire. On dit des faits, avec l'heure et la valeur, sans jugement. Ce qui a été fait se dit au passif : « Der Verband wurde gewechselt ».")
T.texte("liste", "Lis la feuille de relève et réponds.")
T.texte("vraifaux", "Lis la feuille de relève : vrai ou faux ?")
T.texte("zuerst", "Tu fais la relève de ce patient : que dis-tu en premier ?")
T.texte("zuletzt", "Tu fais la relève de ce patient : que dis-tu à la fin ?")
T.texte("objektiv", "Quelle phrase a sa place dans la relève ?")
T.texte("passiv", "Choisis la bonne forme.")
T.texte("abk", "Que veut dire cette abréviation ?")
T.texte("abk2", "Comment l'écrit-on en abrégé ?")

uebergabe = T.mot("die Übergabe")
bericht = T.mot("der Pflegebericht")
massnahme = T.mot("die Maßnahme")
objektiv = T.mot("objektiv und wertfrei formulieren")
for p in P:
    T.glose(qui(p), P[p]["fr"])

# ---------- la feuille : motif, valeurs, ce qui reste a faire ----------
toutes_offen = [(q, o) for q in P for o in P[q]["offen"]]
tous_verlauf = [(q, v) for q in P for v in P[q]["verlauf"]]
for p, d in P.items():
    vis = [{"img": VISAGE[p]}, {"doc": feuille(p)}]
    autres = [q for q in P if q != p]
    # pourquoi est-il la ?
    g = grund(p)
    for n in range(2):
        leurres = [P[q]["grund"][1] for q in autres[n * 2: n * 2 + 3]]
        T.question("liste", uebergabe, "liste", d["grund"][1], g, choix=[d["grund"][1]] + leurres, visuel=vis,
                   enonce="Warum ist " + d["de"] + " bei uns?")
        for x in [d["grund"][1]] + leurres:
            T.glose(x, next(P[q]["grund"][2] for q in P if P[q]["grund"][1] == x))
    # les valeurs, dites en lettres
    for abk, h, hdit, v, vdit, mot in d["werte"]:
        w = T.mot(mot)
        nom = {"BZ": "der Blutzucker", "NRS": "der Schmerz auf der Skala", "Temp.": "die Temperatur"}[abk]
        ph = T.phrase({"BZ": "Der Blutzucker lag um " + hdit + " bei " + vdit + ".",
                       "NRS": "Um " + hdit + " lag der Schmerz bei " + vdit + " von zehn.",
                       "Temp.": "Um " + hdit + " lag die Temperatur bei " + vdit + " Grad."}[abk],
                      {"BZ": "À %s, la glycémie était à %s." % (h.replace(":00", " h").replace(":30", " h 30"), v),
                       "NRS": "À %s, la douleur était à %s sur 10." % (h.replace(":00", " h").replace(":30", " h 30"), v),
                       "Temp.": "À %s, la température était de %s °C." % (h.replace(":00", " h"), v)}[abk])
        confus = {"hundertachtzig": ["hundertacht", "achtzehn", "hundertvierzig"], "hundertvierzig": ["hundertvier", "vierzehn", "hundertachtzig"],
                  "zweihundertzehn": ["zweihundertzwölf", "hundertzehn", "zwanzig"], "sieben": ["siebzehn", "drei", "acht"],
                  "drei": ["dreizehn", "sieben", "acht"], "fünf": ["fünfzehn", "vier", "sechs"],
                  "sechsunddreißig Komma acht": ["achtunddreißig Komma sechs", "sechsunddreißig Komma drei", "siebenunddreißig Komma acht"]}[vdit]
        frage = {"BZ": "Wie hoch war der Blutzucker um " + hdit + "?", "NRS": "Wie stark war der Schmerz um " + hdit + "?",
                 "Temp.": "Wie hoch war die Temperatur um " + hdit + "?"}[abk]
        T.question("liste", w, "liste", vdit, ph, choix=[vdit] + confus, visuel=vis, enonce=frage)
    # ce qui reste a faire
    for f, dit, fr in d["offen"]:
        ph = T.phrase(dit, fr)
        leurres = [o[1] for q, o in toutes_offen if q != p][:3]
        for x, frx in [(dit, fr)] + [(o[1], o[2]) for q, o in toutes_offen if q != p]:
            T.glose(x, frx)
        T.question("liste", massnahme, "liste", dit, ph, choix=[dit] + leurres, visuel=vis, enonce="Was ist bei " + d["de"] + " noch offen?")
    # ce qui s'est passe
    for f, dit, fr in d["verlauf"]:
        ph = T.phrase(dit, fr)
        leurres = [v[1] for q, v in tous_verlauf if q != p]
        leurres = leurres[len(f) % 3:][:3]
        for x, frx in [(dit, fr)] + [(v[1], v[2]) for q, v in tous_verlauf if q != p]:
            T.glose(x, frx)
        T.question("liste", bericht, "liste", dit, ph, choix=[dit] + leurres, visuel=vis, enonce="Was steht im Verlauf bei " + d["de"] + "?")
        # vrai ou faux : un fait de la feuille, ou un fait d'un autre patient
        T.question("vraifaux", bericht, "vraifaux", "Richtig", ph, choix=["Richtig", "Falsch"], visuel=vis, enonce=dit,
                   centre=True, ordre_fixe=True)
    for q, v in tous_verlauf:
        if q != p and len(v[1]) % 2 == len(p) % 2:
            T.question("vraifaux", bericht, "vraifaux", "Falsch", T.phrase(d["verlauf"][0][1], d["verlauf"][0][2]),
                       choix=["Richtig", "Falsch"], visuel=vis, enonce=v[1].replace(P[q]["de"], d["de"]) if P[q]["de"] in v[1] else v[1],
                       centre=True, ordre_fixe=True)
    # l'ordre : d'abord qui, a la fin ce qui reste a faire
    debut = qui(p)
    fin_ = d["offen"][0][1]
    milieu = [d["verlauf"][0][1], d["verlauf"][-1][1]]
    T.question("zuerst", uebergabe, "zuerst", debut, debut, choix=[debut, fin_] + milieu[:2], visuel=vis, enonce=d["de"] + ": Was sagen Sie zuerst?")
    T.question("zuletzt", uebergabe, "zuletzt", fin_, T.phrase(fin_, d["offen"][0][2]), choix=[fin_, debut] + milieu[:2], visuel=vis,
               enonce=d["de"] + ": Was sagen Sie am Ende?")

# ---------- objectif, sans jugement ----------
OBJ = [
    ("brandt", "Mobilisation abgelehnt, wegen Angst vor einem Sturz.", "Mobilisation refusée, par peur d'une chute.",
     ["Er ist faul und will nicht laufen.", "Er ist ein schwieriger Patient."]),
    ("lehmann", "Die Wunde ist reizlos.", "La plaie est calme.",
     ["Die Wunde sieht eklig aus.", "Die Wunde ist ganz okay, glaube ich."]),
    ("weber", "Gestürzt auf dem Weg zur Toilette, kein Kopfanprall.", "Chute en allant aux toilettes, sans choc à la tête.",
     ["Sie ist mal wieder hingefallen, typisch.", "Sie passt einfach nicht auf."]),
    ("schulze", "Nachts um drei Uhr im Flur, hat sich beruhigen lassen.", "La nuit, à 3 h, dans le couloir, il s'est laissé calmer.",
     ["Er hat die ganze Nacht genervt.", "Er war wieder total durcheinander, wie immer."]),
    ("kowalski", "Blutzucker am Morgen zweihundertzehn, Insulin nach Schema gegeben.", "Glycémie du matin à 210, insuline donnée selon le schéma.",
     ["Der Zucker war viel zu hoch, wie immer.", "Sie isst bestimmt heimlich Süßes."]),
]
T.texte("gehoert", "Cette phrase a-t-elle sa place dans la relève ?")
for p, bon, fr, mauvais in OBJ:
    ph = T.phrase(bon, fr)
    T.question("gehoert", objektiv, "gehoert", "Ja", ph, choix=["Ja", "Nein"], visuel={"img": VISAGE[p]}, enonce=bon,
               centre=True, ordre_fixe=True)
    for m in mauvais:
        T.question("gehoert", objektiv, "gehoert", "Nein", ph, choix=["Ja", "Nein"], visuel={"img": VISAGE[p]}, enonce=m,
                   centre=True, ordre_fixe=True)
    autres_mauvais = [m for q, b, f, ms in OBJ if q != p for m in ms]
    for n in range(3):
        T.question("objektiv", objektiv, "objektiv", bon, ph, choix=[bon] + mauvais + [autres_mauvais[(n * 3 + len(p)) % len(autres_mauvais)]],
                   visuel={"img": VISAGE[p]}, enonce="Übergabe: " + P[p]["de"])

# ---------- le passif et le Perfekt des transmissions ----------
# (phrase avec ___, bonne, leurres, francais, mot du corpus vise)
PASSIV = [
    ("Der Verband ___ heute früh gewechselt.", "wurde", ["hat", "ist"], "Le pansement a été changé ce matin.", "die Übergabe"),
    ("Herr Brandt ist am Dienstag operiert ___.", "worden", ["geworden", "wurde"], "M. Brandt a été opéré mardi.", "die Übergabe"),
    ("Die Hausärztin ___ informiert.", "wurde", ["hat", "wird worden"], "La médecin traitante a été informée.", "die Übergabe"),
    ("Frau Weber ___ heute Nacht gestürzt.", "ist", ["hat", "wurde"], "Mme Weber est tombée cette nuit.", "die Übergabe"),
    ("Frau Lehmann ___ Insulin nach Schema bekommen.", "hat", ["ist", "wurde"], "Mme Lehmann a eu de l'insuline selon le schéma.", "die Übergabe"),
    ("Herr Schulze hat sich beim Essen ___.", "verschluckt", ["verschlucken", "verschluckte"], "M. Schulze a avalé de travers pendant le repas.", "die Übergabe"),
    ("Die Mobilisation ___ abgelehnt.", "wurde", ["hat", "ist worden"], "La mobilisation a été refusée.", "die Übergabe"),
    ("Das Sturzprotokoll ist ___.", "geschrieben", ["schreibt", "geschreibt"], "Le rapport de chute est écrit.", "der Pflegebericht"),
    ("Am Nachmittag soll die Mobilisation noch einmal angeboten ___.", "werden", ["worden", "wird"], "Cet après-midi, il faut lui reproposer la mobilisation.", "die Maßnahme"),
    ("Um vierzehn Uhr muss der Blutzucker gemessen ___.", "werden", ["worden", "sein"], "À 14 h, il faut mesurer la glycémie.", "der Blutzucker"),
    ("Das Schmerzmittel ___ um zehn Uhr gegeben.", "wurde", ["hat", "ist worden"], "L'antalgique a été donné à 10 h.", "die Übergabe"),
    ("Die Ärztin ist ___ worden.", "informiert", ["informieren", "informierte"], "La médecin a été informée.", "die Übergabe"),
]
for phrase, bon, leurres, fr, mot in PASSIV:
    ph = T.phrase(phrase.replace("___", bon), fr)
    T.question("passiv", T.mot(mot), "passiv", bon, ph, choix=[bon] + leurres, enonce=phrase, centre=True)

# ---------- les abreviations : le sens, puis l'abreviation ----------
corp = T.corpus
ABK = ["RR (= Blutdruck)", "HF (= Herzfrequenz)", "AF (= Atemfrequenz)", "Temp. (= Temperatur)", "BZ (= Blutzucker)",
       "i.v. (= intravenös)", "s.c. (= subkutan)", "i.m. (= intramuskulär)", "p.o. (= per os)", "Tbl. (= Tablette)",
       "Trpf. (= Tropfen)", "bds. (= beidseits)", "tgl. (= täglich)", "V.a. (= Verdacht auf)", "Z.n. (= Zustand nach)",
       "OK (= Oberkörper)", "Amp. (= Ampulle)", "PVK (= peripherer Venenkatheter)", "DK (= Dauerkatheter)", "HA (= Hausarzt)",
       "KH (= Krankenhaus)", "Rö (= Röntgen)", "NRS (= numerische Ratingskala)", "VW (= Verbandswechsel)", "BE (= Blutentnahme)",
       "ggf. (= gegebenenfalls)", "b.B. / n.B. (= bei Bedarf / nach Bedarf)", "li. / re. (= links / rechts)"]
sens = {}
for a in ABK:
    court, long_ = a.split(" (= ", 1)
    sens[a] = (court, long_.rstrip(")"))
for i, a in enumerate(ABK):
    court, long_ = sens[a]
    m = corp[a]
    w = T.mot(a, dit=m.get("lecture_mot"))
    lect = (m.get("lecture_mot") or court).split(",")[0].strip()
    ph = T.phrase(court + " heißt: " + long_ + ".", court + " veut dire : " + m["traduction"] + ".")
    T.glose(long_, m["traduction"])
    T.glose(court, m["traduction"])
    autres = [x for x in ABK if x != a]
    for n in range(2):
        leurres = [sens[x][1] for x in autres[(i * 2 + n * 5) % len(autres):][:3]]
        if len(leurres) < 3:
            leurres += [sens[x][1] for x in autres[:3 - len(leurres)]]
        T.question("abk", w, "abk", long_, ph, choix=[long_] + leurres, enonce=court, centre=True,
                   dit=lect + " heißt: " + long_ + ".")
        leurres2 = [sens[x][0] for x in autres[(i * 3 + n * 7) % len(autres):][:3]]
        if len(leurres2) < 3:
            leurres2 += [sens[x][0] for x in autres[:3 - len(leurres2)]]
        T.question("abk2", w, "abk2", court, ph, choix=[court] + leurres2, enonce=long_, centre=True,
                   dit=lect + " heißt: " + long_ + ".")

# ---------- la decouverte : chaque patient, sa feuille, sa premiere phrase ----------
for p in P:
    T.decouverte.append({"visuel": [{"img": VISAGE[p]}, {"doc": feuille(p)}], "vignette": {"img": VISAGE[p]},
                         "texte": qui(p), "court": P[p]["de"], "dit": grund(p)})

T.ecrire()
