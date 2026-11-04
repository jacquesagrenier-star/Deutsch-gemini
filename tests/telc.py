"""Controle des donnees du telc Deutsch A2·B1 (visuel/prototype/telc/donnees/).

Usage : python tests/telc.py

Le format vient de preparation-examens/FORMAT-TELC.md (le Uebungstest gratuit du telc, format seulement) :
  Sprachbausteine : une lettre ou un courriel complet (formule d'appel, formule de fin), 10 trous, 3 choix par
  trou, une seule bonne reponse.
Le controle verifie aussi que la feuille n'est pas devinable : aucune lettre (a, b, c) ne porte plus de la moitie
des bonnes reponses d'une serie, comme tests/dtz.py pour le DTZ.
"""
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONNEES = os.path.join(RACINE, "visuel", "prototype", "telc", "donnees")
APPELS = ("Sehr geehrte", "Liebe ", "Lieber ", "Hallo ")
FINS = ("Mit freundlichen Grüßen", "Viele Grüße", "Liebe Grüße", "Herzliche Grüße", "Bis bald")

fautes = []


def faute(ou, quoi):
    fautes.append(ou + " : " + quoi)


def sprachbausteine():
    d = json.load(open(os.path.join(DONNEES, "sprachbausteine.json"), encoding="utf-8"))
    series = d.get("series") or []
    if not series:
        faute("sprachbausteine.json", "aucune serie")
    ids = [s.get("id") for s in series]
    if len(set(ids)) != len(ids):
        faute("sprachbausteine.json", "deux series ont le meme id")
    for s in series:
        ou = "Sprachbausteine serie %s" % s.get("id")
        for cle in ("registre", "situation_fr", "von", "an", "betreff", "absaetze", "luecken"):
            if not s.get(cle):
                faute(ou, "champ « %s » vide ou absent" % cle)
        if s.get("registre") not in ("formel", "informel"):
            faute(ou, "registre inconnu : %r" % s.get("registre"))
        absaetze = s.get("absaetze") or []
        texte = "\n".join(absaetze)
        if absaetze and not absaetze[0].startswith(APPELS):
            faute(ou, "la lettre ne commence pas par une formule d'appel : %r" % absaetze[0][:40])
        if not any(a.startswith(FINS) or "{" in a and any(f.split()[0] in a for f in FINS) for a in absaetze[-3:]):
            faute(ou, "pas de formule de fin dans les trois dernieres lignes")
        trous = [int(n) for n in re.findall(r"\{(\d+)\}", texte)]
        luecken = s.get("luecken") or []
        if len(luecken) != 10:
            faute(ou, "%d trous au lieu de 10" % len(luecken))
        if sorted(trous) != list(range(1, len(luecken) + 1)):
            faute(ou, "les trous du texte %s ne vont pas de 1 a %d, chacun une fois" % (trous, len(luecken)))
        if trous != sorted(trous):
            faute(ou, "les trous ne sont pas dans l'ordre du texte")
        lettres = {0: 0, 1: 0, 2: 0}
        for k, l in enumerate(luecken):
            o2 = ou + ", trou %s" % l.get("n")
            if l.get("n") != k + 1:
                faute(o2, "numero %r au rang %d" % (l.get("n"), k + 1))
            o = l.get("o") or []
            if len(o) != 3 or any(not str(x).strip() for x in o):
                faute(o2, "il faut 3 choix non vides : %r" % o)
            if len(set(o)) != len(o):
                faute(o2, "deux choix identiques : %r" % o)
            b = l.get("bon")
            if b not in (0, 1, 2):
                faute(o2, "« bon » doit valoir 0, 1 ou 2 : %r" % b)
            else:
                lettres[b] += 1
            if not (l.get("erkl_fr") or "").strip():
                faute(o2, "pas d'explication (erkl_fr)")
            elif b in (0, 1, 2) and len(o) == 3 and o[b] not in l["erkl_fr"]:
                faute(o2, "l'explication ne cite pas la bonne reponse « %s »" % o[b])
        if luecken and max(lettres.values()) > len(luecken) // 2:
            faute(ou, "feuille devinable : %s" % {"abc"[k]: v for k, v in lettres.items()})
    return len(series), sum(len(s.get("luecken") or []) for s in series)


n, t = sprachbausteine()
print("Sprachbausteine : %d series, %d trous" % (n, t))
if fautes:
    print("\n%d faute(s) :" % len(fautes))
    for f in fautes:
        print("   " + f)
    sys.exit(1)
print("OK : le format du telc est respecte.")
