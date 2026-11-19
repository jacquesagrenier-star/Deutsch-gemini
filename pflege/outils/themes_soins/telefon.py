# -*- coding: utf-8 -*-
"""Theme illustre des Soins, chapitre 10 : le telephone (soins-theme-telefon). Decision de Jacques du 16 nov. 2026.

    python pflege/outils/themes_soins/telefon.py      # ecrit visuel/prototype/soins-theme-telefon/donnees.json

L'ANGLE (regle 2 : pas de scene refaite). La scene du telephone (soins-telefon) fait nommer les objets du poste, la
nuit ; ici, l'APPEL lui-meme :
  - QUI APPELLE : la premiere phrase de celui qui appelle (le laboratoire, la pharmacie, le medecin de garde, une
    fille de patiente, la cadre), dite et ecrite ;
  - QUE REPONDRE : les repliques des dialogues d19 (le laboratoire, la pharmacie) et d23 (la famille au telephone,
    le secret professionnel), mot pour mot, avec leurs traductions (pflege/sources/traductions/), comme la couche
    « Situation » des scenes : une replique, la bonne reponse, la faute du dialogue et son explication ;
  - LA NOTE D'APPEL, dessinee (la regle des papiers) : qui, quand, quel patient, quelle valeur, a qui transmis ; les
    nombres se DISENT en lettres (« sechs Komma zwei ») ;
  - EPELER (buchstabieren) : l'alphabet telephonique allemand traditionnel (DIN 5009, Anton, Berta, Casar...), les noms
    du service.
Les personnes : Frau Aksoy (le laboratoire), Herr Richter (la pharmacie), Dr. Kramer (le medecin de garde) -- trois
des cinq visages manquants, a faire a l'etape 2 --, Frau Kruger et Frau Hoffmann, qui existent.
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
sys.path.insert(0, os.path.dirname(ICI))
from commun import Theme, RACINE, LANGUES  # noqa: E402
import situations_scenes as S  # noqa: E402  (les dialogues, leurs traductions, les noms)

T = Theme("telefon")
SRC = S.Sources()
NOMS = {}
for _l in LANGUES + ["de"]:
    if _l == "fr" or _l == "de" or os.path.exists(os.path.join(RACINE, "pflege", "sources", "traductions", _l, "noms.json")):
        NOMS[_l] = SRC.noms(_l)          # l'espagnol n'a pas encore de dialogues traduits : ses phrases vont aux traducteurs


def de(t):
    return S.remplacer(t, NOMS["de"], [])


def traductions(d, cle, fr):
    """Les traductions d'un texte de dialogue (cle « noeuds.<n>.choix.<k> » ou « ...dit.<k> »), noms remplaces."""
    out = {}
    for l in LANGUES[1:]:
        if l not in NOMS:
            continue
        try:
            t = SRC.trad(d, l).get(cle, {}).get(l)
        except SystemExit:
            t = None
        if t:
            out[l] = S.remplacer(t, NOMS[l], [])
    return out


# ---------- les personnes qui appellent ----------
APPELS = [
    # (id image, qui appelle -- le mot vise, sa premiere phrase (dialogue, noeud, cle), francais)
    ("aksoy", "das Labor", ("d19-telefon", "melden", "noeuds.melden.choix.0.puis.0")),
    ("richter", "die Apotheke", ("d19-telefon", "apotheke", "noeuds.apotheke.dit.0")),
    ("kraemer", "der Arzt", ("d07-sbar", "melden", "noeuds.melden.dit.1")),
    ("krueger", "der Angehörige", ("d23-schweigepflicht", "anruf", "noeuds.anruf.dit.0")),
    ("hoffmann", "die Stationsleitung", ("d11-dienst-tauschen", "anruf", "noeuds.anruf.dit.1")),
]
WER = {"das Labor": ("Das Labor ruft an.", "C'est le laboratoire qui appelle."),
       "die Apotheke": ("Die Apotheke ruft an.", "C'est la pharmacie qui appelle."),
       "der Arzt": ("Der Arzt vom Dienst ruft an.", "C'est le médecin de garde qui appelle."),
       "der Angehörige": ("Eine Angehörige ruft an.", "C'est une proche qui appelle."),
       "die Stationsleitung": ("Die Stationsleitung ruft an.", "C'est la cadre du service qui appelle.")}
IMAGES = {"aksoy": "Frau Aksoy, du laboratoire central de l'hôpital, en blouse blanche, au téléphone.",
          "richter": "Herr Richter, de la pharmacie de l'hôpital, au téléphone, devant des étagères de boîtes.",
          "kraemer": "Dr. Krämer, le médecin de garde, la nuit, au téléphone.",
          "krueger": "Frau Krüger, la fille de Frau Lehmann.",
          "hoffmann": "Frau Hoffmann, la cadre du service."}
for i, alt in IMAGES.items():
    T.image("visage-" + i, alt, personne=i)

T.texte("titre", "Le téléphone")
T.texte("intro", "Touche une personne : tu entends comment elle se présente au téléphone. Puis les réponses justes, la note d'appel et l'alphabet pour épeler.")
T.texte("regle", "Au téléphone, on se présente toujours : le service, son nom, le bonjour. On note tout de suite (qui, quand, quel patient, quelle valeur), on répète la valeur pour la vérifier, et on ne donne aucune information sur un patient à quelqu'un qu'on ne peut pas identifier. Pour épeler un nom : « K wie Kaufmann ».")
T.texte("wer", "Écoute la personne : qui appelle ?")
T.texte("antwort", "Que réponds-tu ?")
T.texte("notiz", "Lis la note d'appel et réponds.")
T.texte("vraifaux", "Lis la note d'appel : vrai ou faux ?")
T.texte("buchst", "Le nom est épelé au téléphone : lequel est-ce ?")
T.texte("lettre", "Quel mot de l'alphabet téléphonique manque ?")

for img, mot, (d, noeud, cle) in APPELS:
    w = T.mot(mot)
    dlg = SRC.dialogue(d)
    nd = dlg["noeuds"][noeud]
    if ".puis." in cle:
        k = int(cle.split(".choix.")[1].split(".")[0])
        ligne = nd["choix"][k]["puis"][0]
    else:
        # la premiere ligne « dit » qui est une replique (pas un recit) ; sa vraie cle de traduction
        j = next(j for j, l in enumerate(nd["dit"]) if l.get("qui"))
        ligne, cle = nd["dit"][j], "noeuds.%s.dit.%d" % (noeud, j)
    parle = de(ligne.get("dit") or ligne["t"])
    fr_ligne = S.remplacer(ligne.get("fr", ""), NOMS["fr"], [])
    T.phrase(parle, fr_ligne, trad=traductions(d, cle, fr_ligne))
    juste_de, juste_fr = WER[mot]
    ph = T.phrase(juste_de, juste_fr)
    autres = [m for _, m, _ in APPELS if m != mot]
    # avec le visage, puis a l'oreille seulement
    T.question("wer", w, "wer", juste_de, ph, choix=[juste_de] + [WER[m][0] for m in autres][:3], visuel={"cite": parle, "visage": "visage-" + img},
               dit=parle + " " + juste_de)
    T.question("wer", w, "wer", juste_de, ph, choix=[juste_de] + [WER[m][0] for m in autres][1:4], ecoute=parle)
    T.glose(juste_de, juste_fr)
    T.decouverte.append({"visuel": {"cite": parle, "visage": "visage-" + img}, "vignette": {"img": "visage-" + img},
                         "texte": parle, "court": juste_de.split(" ruft")[0].replace("Der Arzt vom Dienst", "Arzt").replace("Eine ", "")})

# ---------- que repondre : les repliques de d19 et d23, telles quelles ----------
# le mot que chaque noeud fait travailler
NOEUDS = [("d19-telefon", {"melden": "das Telefon", "patient": "das Telefon", "wert": "das Telefon", "apotheke": "die Apotheke",
                           "insulin": "die Apotheke", "moerser": "die Apotheke"}),
          ("d23-schweigepflicht", {"anruf": "die Schweigepflicht", "befinden": "die Auskunft", "werte": "die Auskunft",
                                   "sorge": "die Auskunft", "nachbar": "die Schweigepflicht", "ende": "das Telefon"})]
for d, noeuds in NOEUDS:
    dlg = SRC.dialogue(d)
    for noeud, mot in noeuds.items():
        w = T.mot(mot)
        nd = dlg["noeuds"][noeud]
        faux = [(k, c) for k, c in enumerate(nd["choix"]) if c.get("faux")]
        bons = [(k, c) for k, c in enumerate(nd["choix"]) if not c.get("faux")]
        if not faux or not bons:
            continue
        kf, cf = faux[0]
        try:
            ligne = S.replique(dlg, noeud)
        except SystemExit:
            # le telephone sonne : personne n'a encore parle (« melden »), la question part de la sonnerie
            ligne = {"qui": "", "t": "(Das Telefon klingelt.)", "fr": "(Le téléphone sonne.)"}
        qui = ligne["qui"]
        nom = (NOMS["de"].get(qui) or {}).get("") or qui
        parle = de(ligne.get("dit") or ligne["t"])
        aide_fr = S.remplacer(cf["aide"]["fr"], NOMS["fr"], []) if cf.get("aide") else ""
        T.texte("aide-" + d[:3] + "-" + noeud, aide_fr)
        # les fautes d'ailleurs dans le meme dialogue, pour la troisieme proposition
        ailleurs = [de(c.get("dit") or c["t"]) for n2, nd2 in dlg["noeuds"].items() if n2 != noeud
                    for c in nd2.get("choix", []) if c.get("faux")]
        for i, (kb, cb) in enumerate(bons):
            bonne = de(cb.get("dit") or cb["t"])
            fr_b = S.remplacer(cb["fr"], NOMS["fr"], [])
            ph = T.phrase(bonne, fr_b, trad=traductions(d, "noeuds.%s.choix.%d" % (noeud, kb), fr_b))
            mauvaise = de(cf.get("dit") or cf["t"])
            autre = ailleurs[(i + len(noeud)) % len(ailleurs)] if ailleurs else None
            choix = [bonne, mauvaise] + ([autre] if autre and autre not in (bonne, mauvaise) else [])
            if len(choix) < 3:
                continue
            T.question("antwort", w, "antwort", bonne, ph, choix=choix, visuel={"cite": parle, "visage": "visage-" + {"aksoy": "aksoy", "richter": "richter", "lehmann_tochter": "krueger"}.get(qui, "krueger")},
                       enonce=None, aide=("aide-" + d[:3] + "-" + noeud) if aide_fr else None)
            T.glose(mauvaise, S.remplacer(cf["fr"], NOMS["fr"], []))

# ---------- l'article des mots de l'appel ----------
T.texte("artikel", "Choisis le bon article.")
ARTIKEL = [("das Labor", "___ Labor ruft an.", "Das Labor ruft an.", "C'est le laboratoire qui appelle."),
           ("die Apotheke", "___ Apotheke ruft an.", "Die Apotheke ruft an.", "C'est la pharmacie qui appelle."),
           ("der Arzt", "___ Arzt vom Dienst ruft an.", "Der Arzt vom Dienst ruft an.", "C'est le médecin de garde qui appelle."),
           ("der Angehörige", "___ Angehörige möchte eine Auskunft.", "Der Angehörige möchte eine Auskunft.", "Le proche voudrait une information."),
           ("die Stationsleitung", "___ Stationsleitung ruft an.", "Die Stationsleitung ruft an.", "C'est la cadre du service qui appelle."),
           ("das Telefon", "___ Telefon klingelt.", "Das Telefon klingelt.", "Le téléphone sonne."),
           ("die Schweigepflicht", "___ Schweigepflicht gilt auch am Telefon.", "Die Schweigepflicht gilt auch am Telefon.", "Le secret professionnel s'applique aussi au téléphone."),
           ("die Auskunft", "Am Telefon gebe ich ___ Auskunft nur mit Kennwort.", "Am Telefon gebe ich die Auskunft nur mit Kennwort.",
            "Au téléphone, je ne donne l'information qu'avec le mot de passe.")]
for mot, enonce, juste, fr in ARTIKEL:
    w = T.mot(mot)
    bonne = juste.split(" ")[0] if enonce.startswith("___") else "die"
    T.question("artikel", w, "artikel", bonne, T.phrase(juste, fr), choix=(["Der", "Die", "Das"] if enonce.startswith("___") else ["der", "die", "das"]),
               enonce=enonce, centre=True, ordre_fixe=True)

# ---------- la note d'appel ----------
NOTES = [
    {"qui": "Frau Aksoy, Zentrallabor", "quand": ("15:40", "fünfzehn Uhr vierzig", "15 h 40"), "patient": "Lehmann, Gisela (geb. 21.08.1952)",
     "anliegen": ("Kalium 6,2 mmol/l – kritisch", "Kalium sechs Komma zwei Millimol pro Liter", "un potassium à 6,2 mmol/l"),
     "an": ("Dr. Sommer, 15:45", "an Dr. Sommer", "à la docteure Sommer"), "durchwahl": ("412", "vier eins zwei", "412"),
     "mot": "die Laborwerte"},
    {"qui": "Herr Richter, Apotheke", "quand": ("10:05", "zehn Uhr fünf", "10 h 05"), "patient": "–",
     "anliegen": ("5 Insulinpens lispro, Lieferung vor 14:00", "fünf Insulinpens, Lieferung vor vierzehn Uhr", "cinq stylos d'insuline, livrés avant 14 h"),
     "an": ("Stationsleitung", "an die Stationsleitung", "à la cadre"), "durchwahl": ("287", "zwei acht sieben", "287"),
     "mot": "das Insulin"},
    {"qui": "Frau Krüger (Tochter von Frau Lehmann)", "quand": ("19:20", "neunzehn Uhr zwanzig", "19 h 20"), "patient": "Lehmann, Gisela",
     "anliegen": ("Kennwort richtig; fragt nach Blutwerten → Gespräch mit Dr. Sommer morgen 10:00", "das Gespräch mit Dr. Sommer morgen um zehn", "l'entretien avec la docteure Sommer demain à 10 h"),
     "an": ("Frau Lehmann (Grüße)", "an Frau Lehmann", "à Mme Lehmann"), "durchwahl": ("–", "", ""),
     "mot": "die Auskunft"},
]


def note(n):
    lignes = [("Anrufer", n["qui"]), ("Uhrzeit", n["quand"][0]), ("Patient", n["patient"]), ("Anliegen", n["anliegen"][0]),
              ("Weitergegeben an", n["an"][0]), ("Rückruf", "Durchwahl " + n["durchwahl"][0] if n["durchwahl"][0] != "–" else "–")]
    return '<div class="titrePapier">Telefonnotiz</div><table>' + "".join("<tr><th>" + a + "</th><td>" + b + "</td></tr>" for a, b in lignes) + "</table>"


durchwahl = T.mot("die Durchwahl")
uhrzeit = T.mot("die Uhrzeit")
for i, n in enumerate(NOTES):
    w = T.mot(n["mot"])
    vis = {"doc": note(n)}
    autres = [x for x in NOTES if x is not n]
    # quand
    ph_q = T.phrase("Der Anruf kam um " + n["quand"][1] + ".", "L'appel est arrivé à " + n["quand"][2] + ".")
    T.question("notiz", uhrzeit, "notiz", n["quand"][1], ph_q, choix=[n["quand"][1]] + [x["quand"][1] for x in autres] + ["fünf Uhr fünfzehn"],
               visuel=vis, enonce="Wann kam der Anruf?")
    # l'objet de l'appel
    ph_a = T.phrase("Es ging um " + n["anliegen"][1] + ".", "Il s'agissait de " + n["anliegen"][2] + ".")
    T.question("notiz", w, "notiz", n["anliegen"][1], ph_a, choix=[n["anliegen"][1]] + [x["anliegen"][1] for x in autres], visuel=vis,
               enonce="Worum ging es?")
    T.glose(n["anliegen"][1], n["anliegen"][2])
    # a qui transmis
    ph_t = T.phrase("Die Nachricht wurde " + n["an"][1] + " weitergegeben.", "Le message a été transmis " + n["an"][2] + ".")
    T.question("notiz", w, "notiz", n["an"][1], ph_t, choix=[n["an"][1]] + [x["an"][1] for x in autres], visuel=vis, enonce="An wen wurde die Nachricht weitergegeben?")
    T.glose(n["an"][1], n["an"][2])
    # le numero, chiffre par chiffre
    if n["durchwahl"][1]:
        ph_d = T.phrase("Die Durchwahl ist " + n["durchwahl"][1] + ".", "Le numéro direct est le " + n["durchwahl"][2] + ".")
        confus = {"vier eins zwei": ["vier zwei eins", "vierhundertzwölf", "eins vier zwei"],
                  "zwei acht sieben": ["zwei sieben acht", "acht zwei sieben", "zweihundertachtundsiebzig"]}[n["durchwahl"][1]]
        T.question("notiz", durchwahl, "notiz", n["durchwahl"][1], ph_d, choix=[n["durchwahl"][1]] + confus, visuel=vis,
                   enonce="Unter welcher Durchwahl ruft man zurück?")
        T.question("vraifaux", durchwahl, "vraifaux", "Falsch", ph_d, choix=["Richtig", "Falsch"], visuel=vis,
                   enonce="Die Durchwahl ist " + confus[0] + ".", centre=True, ordre_fixe=True)
    for ph in (ph_q, ph_a, ph_t):
        T.question("vraifaux", w, "vraifaux", "Richtig", ph, choix=["Richtig", "Falsch"], visuel=vis, enonce=ph, centre=True, ordre_fixe=True)
    for x in autres:
        T.question("vraifaux", w, "vraifaux", "Falsch", ph_a, choix=["Richtig", "Falsch"], visuel=vis,
                   enonce="Es ging um " + x["anliegen"][1] + ".", centre=True, ordre_fixe=True)
        T.question("vraifaux", uhrzeit, "vraifaux", "Falsch", ph_q, choix=["Richtig", "Falsch"], visuel=vis,
                   enonce="Der Anruf kam um " + x["quand"][1] + ".", centre=True, ordre_fixe=True)

# ---------- epeler : l'alphabet telephonique (DIN 5009, la forme traditionnelle) ----------
ALPHA = [("A", "Anton"), ("Ä", "Ärger"), ("B", "Berta"), ("C", "Cäsar"), ("D", "Dora"), ("E", "Emil"), ("F", "Friedrich"), ("G", "Gustav"),
         ("H", "Heinrich"), ("I", "Ida"), ("J", "Julius"), ("K", "Kaufmann"), ("L", "Ludwig"), ("M", "Martha"), ("N", "Nordpol"), ("O", "Otto"),
         ("Ö", "Ökonom"), ("P", "Paula"), ("Q", "Quelle"), ("R", "Richard"), ("S", "Samuel"), ("Sch", "Schule"), ("T", "Theodor"), ("U", "Ulrich"),
         ("Ü", "Übermut"), ("V", "Viktor"), ("W", "Wilhelm"), ("X", "Xanthippe"), ("Y", "Ypsilon"), ("Z", "Zacharias")]
CODE = dict(ALPHA)
buchst = T.mot("verbe:buchstabieren")
NAMEN = {"Krämer": ["Kremer", "Krähmer", "Krämmer"], "Aksoy": ["Aksoi", "Axoy", "Akzoy"], "Richter": ["Richtner", "Rihter", "Richtter"],
         "Lehmann": ["Leman", "Lehman", "Lemann"], "Brandt": ["Brand", "Brant", "Bandt"], "Weber": ["Webber", "Wäber", "Veber"],
         "Schulze": ["Schultze", "Schulz", "Schulse"], "Kowalski": ["Kovalski", "Kowalsky", "Kowalzki"], "Hoffmann": ["Hofmann", "Hoffman", "Hofman"],
         "Haddad": ["Hadad", "Haddat", "Hadat"], "Sommer": ["Somer", "Zommer", "Sommers"], "Krüger": ["Krieger", "Kruger", "Krügger"]}


def epeler(nom):
    out, i = [], 0
    while i < len(nom):
        if nom[i:i + 3].lower() == "sch":
            out.append("Sch wie Schule"); i += 3; continue
        c = nom[i].upper()
        out.append(c + " wie " + CODE[c]); i += 1
    return ", ".join(out)


for nom, faux in NAMEN.items():
    sp = epeler(nom)
    ph = T.phrase(nom + ": " + sp + ".", "« " + nom + " », épelé avec l'alphabet téléphonique allemand.")
    T.question("buchst", buchst, "buchst", nom, ph, choix=[nom] + faux, enonce=sp + ".", ecoute=sp)
    T.question("buchst", buchst, "buchst", nom, ph, choix=[nom] + faux, ecoute=sp)
for i, (lettre, mot) in enumerate(ALPHA):
    if i == 0 or i == len(ALPHA) - 1:
        continue
    av, ap = ALPHA[i - 1], ALPHA[i + 1]
    ph = T.phrase(lettre + " wie " + mot + ".", "« " + lettre + " » se dit « " + mot + " » dans l'alphabet téléphonique.")
    leurres = [m for _, m in ALPHA if m not in (mot, av[1], ap[1])]
    leurres = leurres[(i * 3) % len(leurres):][:3] + leurres[:max(0, 3 - len(leurres[(i * 3) % len(leurres):][:3]))]
    T.question("lettre", buchst, "lettre", mot, ph, choix=[mot] + leurres,
               enonce=av[0] + " wie " + av[1] + ", " + lettre + " wie ___, " + ap[0] + " wie " + ap[1], centre=True)

T.ecrire()
