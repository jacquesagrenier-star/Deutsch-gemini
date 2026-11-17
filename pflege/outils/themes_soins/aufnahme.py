# -*- coding: utf-8 -*-
"""Theme illustre des Soins, chapitre 1 : l'admission (soins-theme-aufnahme). Decision de Jacques du 16 nov. 2026.

    python pflege/outils/themes_soins/aufnahme.py            # ecrit visuel/prototype/soins-theme-aufnahme/donnees.json
    python pflege/outils/themes_soins/aufnahme.py --images   # et recadre les objets dans les images des scenes (gratuit)

L'ANGLE (regle 2 : pas de scene refaite). La scene de l'admission (soins-aufnahme) fait nommer les objets de la
chambre ; ici, l'ENTRETIEN et la FICHE :
  - la fiche d'admission de quatre patients, DESSINEE par la page (la regle des papiers), avec les faits des ecrits
    e01-e04 (pflege/sources/ecrit/) : la date de naissance, dite en lettres (« am dritten Mai neunzehnhundert-
    vierundvierzig » : les ordinaux et les annees), les allergies, les aides techniques, la personne a prevenir ;
  - la bonne question pour chaque rubrique (« Wen dürfen wir im Notfall anrufen? ») ;
  - la question indirecte, polie, de l'anamnese (« Darf ich fragen, ob Sie Allergien haben? ») : le mot qui
    l'ouvre (ob, wann, welche…) et le verbe a la fin ;
  - les objets qu'on note a l'admission (lunettes, appareil auditif, boite a dentier, canne, carte d'allergie,
    objets de valeur), RECADRES dans les images des scenes : aucune image a payer.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import Theme, RACINE  # noqa: E402

T = Theme("aufnahme")

MOIS = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
MOIS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
ORD = {1: "ersten", 2: "zweiten", 3: "dritten", 4: "vierten", 5: "fünften", 6: "sechsten", 7: "siebten", 8: "achten", 9: "neunten",
       10: "zehnten", 11: "elften", 12: "zwölften", 13: "dreizehnten", 14: "vierzehnten", 15: "fünfzehnten", 16: "sechzehnten",
       17: "siebzehnten", 18: "achtzehnten", 19: "neunzehnten", 20: "zwanzigsten", 21: "einundzwanzigsten", 22: "zweiundzwanzigsten",
       23: "dreiundzwanzigsten", 24: "vierundzwanzigsten", 25: "fünfundzwanzigsten", 26: "sechsundzwanzigsten",
       27: "siebenundzwanzigsten", 28: "achtundzwanzigsten", 29: "neunundzwanzigsten", 30: "dreißigsten", 31: "einunddreißigsten"}
UNITE = ["", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
DIZ = {2: "zwanzig", 3: "dreißig", 4: "vierzig", 5: "fünfzig", 6: "sechzig", 7: "siebzig", 8: "achtzig", 9: "neunzig"}


def annee(a):
    """1944 -> neunzehnhundertvierundvierzig"""
    r = a - 1900
    return "neunzehnhundert" + (UNITE[r % 10] + "und" if r % 10 else "") + DIZ[r // 10]


def date_dite(j, m, a):
    return "am " + ORD[j] + " " + MOIS[m - 1] + " " + annee(a)


# ---------- les patients et leur fiche (les ecrits e01-e04, pflege/sources/ecrit/) ----------
P = {
    "brandt": {"de": "Herr Brandt", "fr": "M. Brandt", "fiche": "Brandt, Heinrich", "geb": (3, 5, 1944),
               "grund": "Sturz, Schenkelhalsfraktur re.", "allergie": ("gegen Penicillin", "Penicillin (Hautausschlag)", "à la pénicilline"),
               "medik": "Ramipril morgens", "hilfe": ("ein Hörgerät und eine Lesebrille", "Hörgerät li., Lesebrille", "d'un appareil auditif et de lunettes de lecture"),
               "kontakt": ("sein Bruder", "Bruder (wohnt in der Nähe)", "son frère"), "titre": "Pflegeanamnese – Aufnahme"},
    "lehmann": {"de": "Frau Lehmann", "fr": "Mme Lehmann", "fiche": "Lehmann, Gisela", "geb": (21, 8, 1952),
                "grund": "Ulkus re. Vorfuß bei Diabetes", "allergie": ("keine bekannt", "keine bekannt", "aucune connue"),
                "medik": "Insulin nach Schema", "hilfe": ("eine Brille und einen Gehstock", "Brille, Gehstock", "de lunettes et d'une canne"),
                "kontakt": ("ihre Tochter, Frau Krüger", "Tochter (Frau Krüger)", "sa fille, Mme Krüger"), "titre": "Pflegeanamnese – Aufnahme"},
    "weber": {"de": "Frau Weber", "fr": "Mme Weber", "fiche": "Weber, Hildegard", "geb": (17, 2, 1945),
              "grund": "lebte allein, zwei Stürze", "allergie": ("keine bekannt", "keine bekannt", "aucune connue"),
              "medik": "gegen Bluthochdruck", "hilfe": ("eine Brille und einen Rollator", "Brille, Rollator", "de lunettes et d'un déambulateur"),
              "kontakt": ("ihr Sohn Thomas", "Sohn Thomas (Bremen)", "son fils Thomas"), "titre": "Aufnahmebogen – Altenpflege"},
    "kowalski": {"de": "Frau Kowalski", "fr": "Mme Kowalski", "fiche": "Kowalski, Maria", "geb": (28, 6, 1947),
                 "grund": "Diabetes (Insulin), Hypertonie", "allergie": ("keine bekannt", "keine bekannt", "aucune connue"),
                 "medik": "Insulin morgens und abends", "hilfe": ("eine Brille und draußen einen Gehstock", "Brille; draußen Gehstock", "de lunettes et, dehors, d'une canne"),
                 "kontakt": ("ihre Nichte", "Nichte (Nummer in der Mappe)", "sa nièce"), "titre": "Erstbesuch – Ambulanter Dienst"},
}
VISAGE = {p: "visage-" + p for p in P}
for p in P:
    T.image(VISAGE[p], "Le visage de " + P[p]["fr"] + ".", personne=p)


def fiche(p):
    d = P[p]
    j, m, a = d["geb"]
    lignes = [("Name, Vorname", d["fiche"]), ("Geburtsdatum", "%02d.%02d.%d" % (j, m, a)), ("Grund", d["grund"]),
              ("Allergien", d["allergie"][1]), ("Medikamente", d["medik"]), ("Hilfsmittel", d["hilfe"][1]),
              ("Angehörige", d["kontakt"][1])]
    return ('<div class="titrePapier">' + d["titre"] + '</div><table>'
            + "".join("<tr><th>" + x + "</th><td>" + y + "</td></tr>" for x, y in lignes) + "</table>")


T.texte("titre", "L'admission")
T.texte("intro", "Touche une fiche ou un objet : l'entretien d'admission, les questions qu'on pose, et ce qu'on note.")
T.texte("regle", "La question polie de l'entretien est souvent indirecte : « Darf ich fragen, ob Sie Allergien haben? ». Le mot qui l'ouvre (ob, wann, welche, wen) envoie le verbe à la fin. Une date se dit avec un nombre ordinal : « am dritten Mai ».")
T.texte("fiche", "Lis la fiche d'admission et réponds.")
T.texte("vraifaux", "Lis la fiche d'admission : vrai ou faux ?")
T.texte("datum", "Lis la date de naissance : comment la dit-on ?")
T.texte("frage", "Tu veux remplir cette rubrique : quelle question poses-tu ?")
T.texte("konj", "Choisis le mot qui ouvre la question indirecte.")
T.texte("stellung", "Quelle phrase est juste ?")
T.texte("objet", "Regarde l'objet entouré : qu'est-ce que c'est ?")
T.texte("artikel", "Choisis le bon article.")

w_geb = T.mot("das Geburtsdatum")
w_all = T.mot("die Allergie")
w_ang = T.mot("der Angehörige")
w_bog = T.mot("der Aufnahmebogen")
w_med = T.mot("das Medikament")

# ---------- la fiche : la date dite, l'allergie, les aides, la personne a prevenir ----------
for p, d in P.items():
    vis = [{"img": VISAGE[p]}, {"doc": fiche(p)}]
    j, m, a = d["geb"]
    dit = date_dite(j, m, a)
    ph = T.phrase(d["de"] + " ist " + dit + " geboren.", "%s est né%s le %d %s %d." % (d["fr"], "" if p == "brandt" else "e", j, MOIS_FR[m - 1], a))
    faux = [date_dite(j, m % 12 + 1, a), date_dite(min(28, j + 10) if j < 18 else j - 10, m, a), date_dite(j, m, a + 10 if a < 1950 else a - 10)]
    T.question("datum", w_geb, "datum", dit, ph, choix=[dit] + faux, visuel=vis, enonce="Wann ist " + d["de"] + " geboren?")
    autres = [q for q in P if q != p]
    # l'allergie
    ph_a = T.phrase(d["de"] + " hat " + ("keine bekannte Allergie." if d["allergie"][0] == "keine bekannt" else "eine Allergie " + d["allergie"][0] + "."),
                    d["fr"] + (" n'a aucune allergie connue." if d["allergie"][0] == "keine bekannt" else " est allergique " + d["allergie"][2] + "."))
    T.question("fiche", w_all, "fiche", d["allergie"][0], ph_a, choix=["gegen Penicillin", "keine bekannt", "gegen Pflaster", "gegen Jod"],
               visuel=vis, enonce="Welche Allergie hat " + d["de"] + "?")
    # les aides techniques
    ph_h = T.phrase(d["de"] + " braucht " + d["hilfe"][0] + ".", d["fr"] + " a besoin " + d["hilfe"][2] + ".")
    T.question("fiche", w_bog, "fiche", d["hilfe"][0], ph_h, choix=[d["hilfe"][0]] + [P[q]["hilfe"][0] for q in autres],
               visuel=vis, enonce="Welche Hilfsmittel braucht " + d["de"] + "?")
    # la personne a prevenir
    ph_k = T.phrase("Im Notfall ruft man " + {"sein Bruder": "seinen Bruder", "ihre Tochter, Frau Krüger": "ihre Tochter, Frau Krüger",
                                              "ihr Sohn Thomas": "ihren Sohn Thomas", "ihre Nichte": "ihre Nichte"}[d["kontakt"][0]] + " an.",
                    "En cas d'urgence, on appelle " + d["kontakt"][2] + ".")
    T.question("fiche", w_ang, "fiche", d["kontakt"][0], ph_k, choix=[d["kontakt"][0]] + [P[q]["kontakt"][0] for q in autres],
               visuel=vis, enonce="Wen ruft man bei " + d["de"] + " im Notfall an?")
    for x in [d["hilfe"][0], d["kontakt"][0]]:
        pass
    T.glose(d["hilfe"][0], d["hilfe"][2].replace("d'un ", "un ").replace("d'une ", "une ").replace("de lunettes", "des lunettes"))
    T.glose(d["kontakt"][0], d["kontakt"][2])
    T.glose(dit, "%d %s %d" % (j, MOIS_FR[m - 1], a))
    for f in faux:
        pass
    # vrai ou faux : ses faits, ou ceux d'un autre patient
    vrais = [(ph_a, ph_a), (ph_h, ph_h), (ph_k, ph_k)]
    for enonce, juste in vrais:
        T.question("vraifaux", w_bog, "vraifaux", "Richtig", juste, choix=["Richtig", "Falsch"], visuel=vis, enonce=enonce, centre=True, ordre_fixe=True)
    for q in autres:
        e = d["de"] + " braucht " + P[q]["hilfe"][0] + "."
        if P[q]["hilfe"][0] != d["hilfe"][0]:
            T.question("vraifaux", w_bog, "vraifaux", "Falsch", ph_h, choix=["Richtig", "Falsch"], visuel=vis, enonce=e, centre=True, ordre_fixe=True)
    T.question("fiche", w_med, "fiche", d["medik"], T.phrase(d["de"] + " nimmt " + {"Ramipril morgens": "morgens Ramipril",
               "Insulin nach Schema": "Insulin nach Schema", "gegen Bluthochdruck": "ein Mittel gegen Bluthochdruck",
               "Insulin morgens und abends": "morgens und abends Insulin"}[d["medik"]] + ".",
               d["fr"] + " prend " + {"Ramipril morgens": "du ramipril le matin", "Insulin nach Schema": "de l'insuline selon le schéma",
                                      "gegen Bluthochdruck": "un médicament contre l'hypertension",
                                      "Insulin morgens und abends": "de l'insuline matin et soir"}[d["medik"]] + "."),
               choix=[d["medik"]] + [P[q]["medik"] for q in autres], visuel=vis, enonce="Welche Medikamente nimmt " + d["de"] + "?")
for g, fr in (("gegen Penicillin", "à la pénicilline"), ("keine bekannt", "aucune connue"), ("gegen Pflaster", "aux pansements adhésifs"),
              ("gegen Jod", "à l'iode"), ("Ramipril morgens", "du ramipril le matin"), ("Insulin nach Schema", "de l'insuline selon le schéma"),
              ("gegen Bluthochdruck", "contre l'hypertension"), ("Insulin morgens und abends", "de l'insuline matin et soir")):
    T.glose(g, fr)

# ---------- la bonne question pour chaque rubrique, puis la question indirecte ----------
# (rubrique, mot du corpus, question directe, francais, ouvreur indirect, debut de la subordonnee, verbe final, francais indirect)
RUB = [
    ("Geburtsdatum", "das Geburtsdatum", "Wann sind Sie geboren?", "Quand êtes-vous né(e) ?", "wann", "Sie", "geboren sind", "quand vous êtes né(e)"),
    ("Allergien", "die Allergie", "Haben Sie Allergien?", "Avez-vous des allergies ?", "ob", "Sie", "Allergien haben", "si vous avez des allergies"),
    ("Medikamente", "das Medikament", "Welche Medikamente nehmen Sie?", "Quels médicaments prenez-vous ?", "welche", "Medikamente Sie", "nehmen", "quels médicaments vous prenez"),
    ("Hilfsmittel", "das Hörgerät", "Brauchen Sie eine Brille oder ein Hörgerät?", "Avez-vous besoin de lunettes ou d'un appareil auditif ?", "ob", "Sie", "eine Brille oder ein Hörgerät brauchen", "si vous avez besoin de lunettes ou d'un appareil auditif"),
    ("Angehörige", "der Angehörige", "Wen dürfen wir im Notfall anrufen?", "Qui pouvons-nous appeler en cas d'urgence ?", "wen", "wir", "im Notfall anrufen dürfen", "qui nous pouvons appeler en cas d'urgence"),
    ("Vorerkrankungen", "die Vorerkrankung", "Welche Krankheiten haben Sie schon?", "Quelles maladies avez-vous déjà ?", "welche", "Krankheiten Sie", "schon haben", "quelles maladies vous avez déjà"),
    ("Wertsachen", "die Wertsachen", "Haben Sie Wertsachen dabei?", "Avez-vous des objets de valeur sur vous ?", "ob", "Sie", "Wertsachen dabeihaben", "si vous avez des objets de valeur sur vous"),
    ("Patientenverfügung", "die Patientenverfügung", "Haben Sie eine Patientenverfügung?", "Avez-vous des directives anticipées ?", "ob", "Sie", "eine Patientenverfügung haben", "si vous avez des directives anticipées"),
    ("Gewicht", "das Gewicht", "Wie viel wiegen Sie?", "Combien pesez-vous ?", "wie viel", "Sie", "wiegen", "combien vous pesez"),
]
for i, (rub, mot, q, qfr, ouv, sujet, verbe, ifr) in enumerate(RUB):
    w = T.mot(mot)
    ph = T.phrase(q, qfr)
    T.glose(q, qfr)
    autres = [r for r in RUB if r[0] != rub]
    for n in range(2):
        leurres = [r[2] for r in autres[(i + n * 3) % len(autres):][:3]]
        if len(leurres) < 3:
            leurres += [r[2] for r in autres[:3 - len(leurres)]]
        T.question("frage", w, "frage", q, ph, choix=[q] + leurres, visuel={"doc": '<table><tr><th>' + rub + '</th><td>……………</td></tr></table>'},
                   enonce="Rubrik: " + rub)
    # l'indirecte : « Darf ich fragen, ob Sie Allergien haben? » / « Ich möchte wissen, … »
    for debut, dfr in (("Darf ich fragen, ", "Puis-je vous demander "), ("Ich möchte gern wissen, ", "J'aimerais savoir ")):
        ind = debut + ouv + " " + sujet + " " + verbe + ("?" if debut.startswith("Darf") else ".")
        phi = T.phrase(ind, dfr + ifr + (" ?" if debut.startswith("Darf") else "."))
        ouvreurs = ["ob", "wann", "welche", "wen", "wie viel", "dass"]
        T.question("konj", w, "konj", ouv, phi, choix=[ouv] + [o for o in ouvreurs if o != ouv][:3],
                   enonce=ind.replace(debut + ouv + " ", debut + "___ ", 1))
        # le verbe a la fin, ou pas
        mots_v = verbe.split(" ")
        faux1 = debut + ouv + " " + mots_v[-1] + " " + sujet + (" " + " ".join(mots_v[:-1]) if len(mots_v) > 1 else "") + ("?" if debut.startswith("Darf") else ".")
        faux2 = debut + q[0].lower() + q[1:] if not q.startswith("Wen") else debut + "wen dürfen wir im Notfall anrufen?"
        if faux1 != ind and faux2 != ind and faux1 != faux2:
            T.question("stellung", w, "stellung", ind, phi, choix=[ind, faux1, faux2], enonce=None)

# ---------- les objets, recadres dans les scenes ----------
# (nom, scene, zone, mot du corpus, francais indefini, francais defini)
OBJETS = [
    ("brille", "soins-zimmer-nachttisch", "brille", "die Brille", "des lunettes", "Les lunettes sont"),
    ("hoergeraet", "soins-zimmer-nachttisch", "hoergeraet", "das Hörgerät", "un appareil auditif", "L'appareil auditif est"),
    ("prothesendose", "soins-zimmer-nachttisch", "prothesendose", "die Prothesendose", "une boîte à dentier", "La boîte à dentier est"),
    ("gehstock", "soins-aufnahme", "gehstock", "der Gehstock", "une canne", "La canne est"),
    ("rollator", "soins-zimmer", "rollator", "der Rollator", "un déambulateur", "Le déambulateur est"),
    ("rollstuhl", "soins-zimmer", "rollstuhl", "der Rollstuhl", "un fauteuil roulant", "Le fauteuil roulant est"),
    ("allergiepass", "soins-aufnahme", "allergiepass", "der Allergiepass", "une carte d'allergie", "La carte d'allergie est"),
    ("wertsachenbeutel", "soins-aufnahme", "wertsachenbeutel", "der Wertsachenbeutel", "une pochette pour objets de valeur", "La pochette pour objets de valeur est"),
    ("portemonnaie", "soins-aufnahme", "portemonnaie", "das Portemonnaie", "un porte-monnaie", "Le porte-monnaie est"),
    ("koffer", "soins-aufnahme", "koffer", "der Koffer", "une valise", "La valise est"),
    ("einweisung", "soins-aufnahme", "einweisung", "der Einweisungsschein", "un bon d'hospitalisation", "Le bon d'hospitalisation est"),
    ("aufnahmebogen", "soins-aufnahme", "aufnahmebogen", "der Aufnahmebogen", "une fiche d'admission", "La fiche d'admission est"),
    ("waage", "soins-aufnahme", "waage", "die Waage", "une balance", "La balance est"),
]
ART = {"der": "Der", "die": "Die", "das": "Das"}
for nom, scene, zone, mot, _, _ in OBJETS:
    T.image("objet-" + nom, "Recadré dans la scène " + scene + " : " + mot + ", entouré.", scene=scene, zone=zone)
for i, (nom, scene, zone, mot, fr_un, fr_le) in enumerate(OBJETS):
    w = T.mot(mot)
    art, n = mot.split(" ", 1)
    ein = {"der": "ein", "die": "eine", "das": "ein"}[art]
    ph = T.phrase("Das ist " + ein + " " + n + ".", ("Ce sont " if fr_un.startswith("des ") else "C'est ") + fr_un + ".")
    autres = [o[3] for o in OBJETS if o[3] != mot]
    for k in range(2):
        leurres = autres[(i * 2 + k * 5) % len(autres):][:3]
        if len(leurres) < 3:
            leurres += autres[:3 - len(leurres)]
        T.question("objet", w, "objet", mot, ph, choix=[mot] + leurres, visuel={"img": "objet-" + nom})
    T.question("artikel", w, "artikel", ART[art], T.phrase(ART[art] + " " + n + " ist hier.", fr_le + " ici."),
               choix=["Der", "Die", "Das"], visuel={"img": "objet-" + nom}, enonce="___ " + n + " ist hier.", centre=True, ordre_fixe=True)
    T.glose(mot, T.mots[w]["glose"]["fr"])

# ---------- la decouverte ----------
for p in P:
    j, m, a = P[p]["geb"]
    T.decouverte.append({"visuel": [{"img": VISAGE[p]}, {"doc": fiche(p)}], "vignette": {"img": VISAGE[p]},
                         "texte": T.phrase(P[p]["de"] + " ist " + date_dite(j, m, a) + " geboren.", "%s est né%s le %d %s %d." % (P[p]["fr"], "" if p == "brandt" else "e", j, MOIS_FR[m - 1], a)),
                         "court": P[p]["de"]})
for nom, scene, zone, mot, _, _ in OBJETS[:8]:
    w = T.rang[mot]
    T.decouverte.append({"visuel": {"img": "objet-" + nom}, "texte": mot, "trad": T.mots[w]["glose"], "court": mot.split(" ", 1)[1]})


def recadrer():
    """Les objets, recadres en 4:3 dans les originaux des scenes, l'objet entoure d'un trait ambre (gratuit)."""
    import json
    from PIL import Image, ImageDraw
    dossier = os.path.join(RACINE, "visuel", "prototype", "soins-theme-aufnahme")
    for nom, scene, zone, mot, _, _ in OBJETS:
        pts = json.load(open(os.path.join(RACINE, "visuel", "prototype", scene + ".points.json"), encoding="utf-8"))
        x, y, w, h = next(p["boite"] for p in pts["points"] if p["id"] == zone)
        src = os.path.expanduser("~/.wortando/pflege/scenes/" + scene + ".png")
        im = Image.open(src).convert("RGB")
        W, H = im.size
        bx0, by0, bx1, by1 = x * W / 100, y * H / 100, (x + w) * W / 100, (y + h) * H / 100
        cx, cy = (bx0 + bx1) / 2, (by0 + by1) / 2
        ch = max((by1 - by0) * 1.35, (bx1 - bx0) * 1.35 * 3 / 4, 240)
        cw = ch * 4 / 3
        x0, y0 = max(0, min(W - cw, cx - cw / 2)), max(0, min(H - ch, cy - ch / 2))
        c = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((800, 600), Image.LANCZOS)
        d = ImageDraw.Draw(c)
        k = 800 / cw
        m = 10
        d.rounded_rectangle([(bx0 - x0) * k - m, (by0 - y0) * k - m, (bx1 - x0) * k + m, (by1 - y0) * k + m], radius=14, outline=(232, 162, 58), width=5)
        c.save(os.path.join(dossier, "objet-" + nom + ".webp"), quality=84, method=6)
        print("  objet-" + nom)


T.ecrire()
if "--images" in sys.argv:
    recadrer()
