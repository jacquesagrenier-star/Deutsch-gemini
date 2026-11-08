"""Controle de Lire (Leseverstehen) du telc Deutsch A2·B1 : visuel/prototype/telc/donnees/lesen.json.

Usage : python tests/telc_lesen.py

Le format vient du Testformat de l'Uebungstest telc Deutsch A2·B1 (preparation-examens/FORMAT-TELC.md, format
seulement) :
  Teil 1 : items 1-5, petites annonces a associer (ici 8 annonces a-h, donc 3 sans situation) ;
  Teil 2 : items 6-9, un texte court : 6 en Richtig/Falsch, 7-9 en a/b/c ;
  Teil 3 : items 10-13, des courriels, le sens global (ici 6 phrases a-f, donc 2 sans courriel) ;
  Teil 4 : items 14-18, un texte plus long, a/b/c.
Le controle verifie aussi : une annonce ou une phrase ne sert qu'une fois ; chaque explication existe en francais
et en anglais, et cite le texte allemand entre guillemets ; la feuille n'est pas devinable (aucune lettre a, b, c
ne porte plus de la moitie des bonnes reponses a/b/c d'une serie, comme tests/dtz.py et tests/telc.py).
"""
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHIER = os.path.join(RACINE, "visuel", "prototype", "telc", "donnees", "lesen.json")
LANGUES = ("fr", "en")

fautes = []


def faute(ou, quoi):
    fautes.append(ou + " : " + quoi)


def textes(ou, o, *cles):
    for c in cles:
        for l in LANGUES:
            if not str(o.get(c + "_" + l) or "").strip():
                faute(ou, "« %s_%s » vide ou absent" % (c, l))


def explication(ou, o, texte_de):
    """L'explication cite le texte : au moins un passage entre guillemets qui se trouve dans le document."""
    textes(ou, o, "erkl")
    cites = re.findall(r"« ([^»]+) »", o.get("erkl_fr") or "") + re.findall(r"“([^”]+)”", o.get("erkl_en") or "")
    morceaux = [m for c in cites for m in re.split(r"\s*…\s*", c) if len(m) > 3]
    if texte_de and not any(m in texte_de for m in morceaux):
        faute(ou, "l'explication ne cite aucun passage du texte allemand")


def abc(ou, it, compte):
    o = it.get("optionen") or []
    if len(o) != 3 or len(set(o)) != 3 or any(not x.strip() for x in o):
        faute(ou, "il faut 3 choix differents et non vides : %r" % o)
    for l in LANGUES:
        if len(it.get("optionen_" + l) or []) != 3:
            faute(ou, "« optionen_%s » doit avoir 3 choix" % l)
    if it.get("bon") not in (0, 1, 2):
        faute(ou, "« bon » doit valoir 0, 1 ou 2 : %r" % it.get("bon"))
    else:
        compte[it["bon"]] += 1


def doc(t):
    return " ".join([t.get("kopf", ""), t.get("titel", "")] + list(t.get("absaetze") or []))


def serie(s):
    ou = "Lesen serie %s" % s.get("id")
    compte = {0: 0, 1: 0, 2: 0}
    # Teil 1
    t1 = s.get("T1") or {}
    anz = t1.get("anzeigen") or []
    lettres = [a.get("b") for a in anz]
    if lettres != list("abcdefgh"):
        faute(ou + ", Teil 1", "les annonces doivent etre a-h, dans l'ordre : %r" % lettres)
    for a in anz:
        if not (a.get("titel") or "").strip() or not (a.get("text") or "").strip():
            faute(ou + ", Teil 1, annonce %s" % a.get("b"), "titre ou texte vide")
    items = t1.get("items") or []
    if [i.get("nr") for i in items] != [1, 2, 3, 4, 5]:
        faute(ou + ", Teil 1", "les situations doivent etre 1-5 : %r" % [i.get("nr") for i in items])
    bons = [i.get("bon") for i in items]
    if len(set(bons)) != len(bons):
        faute(ou + ", Teil 1", "une annonce sert deux fois : %r" % bons)
    for it in items:
        o2 = ou + ", item %s" % it.get("nr")
        if it.get("bon") not in lettres:
            faute(o2, "« bon » n'est pas une annonce : %r" % it.get("bon"))
        if not (it.get("situation") or "").strip():
            faute(o2, "situation vide")
        textes(o2, it, "situation")
        annonce = next((a for a in anz if a.get("b") == it.get("bon")), {})
        explication(o2, it, doc({"titel": annonce.get("titel", ""), "absaetze": [annonce.get("text", "")]}) + " " +
                    " ".join(a.get("text", "") + " " + a.get("titel", "") for a in anz))
    # Teil 2 et Teil 4
    for teil, nrs in (("T2", [6, 7, 8, 9]), ("T4", [14, 15, 16, 17, 18])):
        t = s.get(teil) or {}
        tx = t.get("text") or {}
        if not tx.get("absaetze"):
            faute(ou + ", " + teil, "pas de texte")
        items = t.get("items") or []
        if [i.get("nr") for i in items] != nrs:
            faute(ou + ", " + teil, "les items doivent etre %r : %r" % (nrs, [i.get("nr") for i in items]))
        for k, it in enumerate(items):
            o2 = ou + ", item %s" % it.get("nr")
            if not (it.get("frage") or "").strip():
                faute(o2, "question vide")
            textes(o2, it, "frage")
            rf = bool(it.get("rf"))
            if teil == "T2" and rf != (k == 0):
                faute(o2, "au Teil 2, seul le premier item est en Richtig/Falsch")
            if teil == "T4" and rf:
                faute(o2, "le Teil 4 n'a que des choix a/b/c")
            if rf:
                if it.get("bon") not in (0, 1):
                    faute(o2, "Richtig/Falsch : « bon » doit valoir 0 ou 1")
            else:
                abc(o2, it, compte)
            explication(o2, it, doc(tx))
    # Teil 3
    t3 = s.get("T3") or {}
    saetze = t3.get("saetze") or []
    ls = [p.get("b") for p in saetze]
    if ls != list("abcdef"):
        faute(ou + ", Teil 3", "les phrases doivent etre a-f : %r" % ls)
    for p in saetze:
        for c in ("de",) + LANGUES:
            if not (p.get(c) or "").strip():
                faute(ou + ", Teil 3, phrase %s" % p.get("b"), "« %s » vide" % c)
    mails = t3.get("mails") or []
    if [m.get("nr") for m in mails] != [10, 11, 12, 13]:
        faute(ou + ", Teil 3", "les courriels doivent etre 10-13 : %r" % [m.get("nr") for m in mails])
    bons = [m.get("bon") for m in mails]
    if len(set(bons)) != len(bons):
        faute(ou + ", Teil 3", "une phrase sert deux fois : %r" % bons)
    for m in mails:
        o2 = ou + ", item %s" % m.get("nr")
        if m.get("bon") not in ls:
            faute(o2, "« bon » n'est pas une phrase : %r" % m.get("bon"))
        if not m.get("von") or not m.get("an") or len(m.get("absaetze") or []) < 3:
            faute(o2, "un courriel a un expediteur, un destinataire, une formule d'appel, un corps et une fin")
        explication(o2, m, " ".join(m.get("absaetze") or []))
    total = sum(compte.values())
    if total and max(compte.values()) > total // 2:
        faute(ou, "feuille devinable (a/b/c) : %s" % {"abc"[k]: v for k, v in compte.items()})


def main():
    d = json.load(open(FICHIER, encoding="utf-8"))
    for teil in ("T1", "T2", "T3", "T4"):
        c = (d.get("consignes") or {}).get(teil) or {}
        for l in ("de",) + LANGUES:
            if not (c.get(l) or "").strip():
                faute("consignes " + teil, "« %s » vide" % l)
    series = d.get("series") or []
    if not series:
        faute("lesen.json", "aucune serie")
    ids = [s.get("id") for s in series]
    if len(set(ids)) != len(ids):
        faute("lesen.json", "deux series ont le meme id")
    for s in series:
        serie(s)
    print("Lesen : %d series, %d questions" % (len(series), 18 * len(series)))
    if fautes:
        print("\n%d faute(s) :" % len(fautes))
        for f in fautes:
            print("   " + f)
        sys.exit(1)
    print("OK : le format de Lire du telc est respecte.")


main()
