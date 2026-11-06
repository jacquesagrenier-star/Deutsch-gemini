"""Controle des donnees de l'ecoute du telc Deutsch A2·B1 (visuel/prototype/telc/donnees/hoeren.json).

Usage : python tests/telc_hoeren.py

Le format vient de preparation-examens/FORMAT-TELC.md (le Uebungstest gratuit du telc, format seulement) :
  Hoeren Teil 1 (32-36) : 5 associations, solutions a-i ; Teil 2 (37-41) et Teil 3 (42-46) : 5 richtig / falsch ;
  Teil 4 (47-51) : 5 associations, solutions a-f (une de trop) ; Hoeren und Schreiben (52-56) : 5 notes.
Le controle verifie aussi :
  - qu'aucune solution n'est prise deux fois (Teil 1 et 4) et que la feuille n'est pas devinable (pas plus de 4 « richtig »
    ou de 4 « falsch » sur les 5 d'un Teil) ;
  - que chaque replique qui contient un chiffre a sa lecture en lettres (« dit »), et que cette lecture n'a plus de
    chiffre (regle du depot : les nombres se disent en lettres) ;
  - que chaque voix nommee existe, et que chaque explication et traduction existe en francais ET en anglais ;
  - que la solution d'une note s'entend bien dans le message (dans « dit » ou « text »).
Separe de tests/telc.py (les Sprachbausteine), que d'autres sessions modifient en meme temps.
"""
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHIER = os.path.join(RACINE, "visuel", "prototype", "telc", "donnees", "hoeren.json")
fautes = []


def faute(ou, quoi):
    fautes.append(ou + " : " + quoi)


def langues(ou, o, champ):
    for l in ("fr", "en"):
        if not (o.get(champ + "_" + l) or "").strip():
            faute(ou, "« %s_%s » vide ou absent" % (champ, l))


def repliques(ou, lignes, voix):
    if not lignes:
        faute(ou, "aucune replique")
    for k, l in enumerate(lignes or []):
        o2 = "%s, replique %d" % (ou, k + 1)
        if l.get("wer") not in voix:
            faute(o2, "voix inconnue : %r" % l.get("wer"))
        t = l.get("text") or ""
        if not t.strip():
            faute(o2, "texte vide")
        if re.search(r"\d", t) and not l.get("dit"):
            faute(o2, "un chiffre sans lecture en lettres (« dit ») : %r" % t[:60])
        if l.get("dit") and re.search(r"\d", l["dit"]):
            faute(o2, "la lecture contient encore un chiffre : %r" % l["dit"][:60])


def associations(ou, bloc, items_cle, lettres_attendues, voix):
    sol = bloc.get("loesungen") or bloc.get("saetze") or []
    lettres = [x.get("b") for x in sol]
    if lettres != list(lettres_attendues):
        faute(ou, "solutions %s au lieu de %s" % ("".join(map(str, lettres)), lettres_attendues))
    for x in sol:
        if not all((x.get(c) or "").strip() for c in ("de", "fr", "en")):
            faute(ou, "solution %s sans de / fr / en" % x.get("b"))
    items = bloc.get(items_cle) or []
    bons = [it.get("bon") for it in items]
    if len(set(bons)) != len(bons):
        faute(ou, "une solution est prise deux fois : %s" % bons)
    for it in items:
        if it.get("bon") not in lettres:
            faute(ou, "item %s : solution %r inconnue" % (it.get("nr"), it.get("bon")))
        langues(ou + ", item %s" % it.get("nr"), it, "erkl")
    return items


def numeros(ou, items, debut):
    nrs = [it.get("nr") for it in items]
    if nrs != list(range(debut, debut + 5)):
        faute(ou, "numeros %s au lieu de %d a %d" % (nrs, debut, debut + 4))


def vrai_faux(ou, items):
    for it in items:
        o2 = ou + ", item %s" % it.get("nr")
        if not isinstance(it.get("bon"), bool):
            faute(o2, "« bon » doit valoir true ou false")
        if not (it.get("aussage") or "").strip():
            faute(o2, "pas d'Aussage")
        langues(o2, it, "aussage")
        langues(o2, it, "erkl")
    r = sum(1 for it in items if it.get("bon") is True)
    if r == 0 or r == len(items):
        faute(ou, "feuille devinable : %d richtig sur %d" % (r, len(items)))


def main():
    d = json.load(open(FICHIER, encoding="utf-8"))
    voix = d.get("voix") or {}
    for t in ("T1", "T2", "T3", "T4", "HS", "ende"):
        c = (d.get("consignes") or {}).get(t) or {}
        if not all((c.get(k) or "").strip() for k in ("de", "fr", "en")) or c.get("wer") not in voix:
            faute("consigne " + t, "de / fr / en ou voix manquant")
        if re.search(r"\d", c.get("dit") or c.get("de") or ""):
            faute("consigne " + t, "un chiffre dans la consigne dite")
    for t in ("T1", "T2", "T3", "T4", "HS"):
        c = (d.get("conseils") or {}).get(t) or {}
        if not ((c.get("fr") or "").strip() and (c.get("en") or "").strip()):
            faute("conseil " + t, "fr / en manquant")
    nH = 0
    for s in d.get("hoeren") or []:
        ou = "Hoeren serie %s" % s.get("id")
        t1 = s.get("T1") or {}
        repliques(ou + " T1", t1.get("audio"), voix)
        items = associations(ou + " T1", t1, "items", "abcdefghi", voix)
        numeros(ou + " T1", items, 32)
        langues(ou + " T1", t1, "situation")
        langues(ou + " T1", t1, "frage")
        t2 = s.get("T2") or {}
        repliques(ou + " T2", t2.get("audio"), voix)
        numeros(ou + " T2", t2.get("items") or [], 37)
        vrai_faux(ou + " T2", t2.get("items") or [])
        langues(ou + " T2", t2, "situation")
        t3 = s.get("T3") or []
        numeros(ou + " T3", t3, 42)
        vrai_faux(ou + " T3", t3)
        for a in t3:
            repliques(ou + " T3 %s" % a.get("nr"), a.get("audio"), voix)
        t4 = s.get("T4") or {}
        repliques(ou + " T4 intro", t4.get("intro"), voix)
        pers = associations(ou + " T4", t4, "personen", "abcdef", voix)
        numeros(ou + " T4", pers, 47)
        if len(pers) != 5:
            faute(ou + " T4", "%d personnes au lieu de 5" % len(pers))
        for p in pers:
            repliques(ou + " T4 %s" % p.get("nr"), p.get("audio"), voix)
        langues(ou + " T4", t4, "thema")
        nH += 1
    nHS = 0
    for s in d.get("notizen") or []:
        ou = "Hoeren und Schreiben serie %s" % s.get("id")
        ms = s.get("nachrichten") or []
        numeros(ou, ms, 52)
        for m in ms:
            o2 = ou + ", message %s" % m.get("nr")
            repliques(o2, m.get("audio"), voix)
            z = (m.get("notiz") or {}).get("zeilen") or []
            if sum(x.count("{}") for x in z) != 1:
                faute(o2, "la note doit avoir exactement une case {}")
            if m.get("typ") not in ("uhrzeit", "zahl", "telefon", "wort"):
                faute(o2, "type inconnu : %r" % m.get("typ"))
            if not (m.get("loesung") or "").strip():
                faute(o2, "pas de solution")
            langues(o2, m, "erkl")
            entendu = " ".join((l.get("text") or "") + " " + (l.get("dit") or "") for l in m.get("audio") or [])
            sol = m.get("loesung") or ""
            if m.get("typ") in ("zahl", "telefon"):
                if re.sub(r"\D", "", sol) not in re.sub(r"\D", "", entendu):
                    faute(o2, "la solution %r ne s'entend pas dans le message" % sol)
            elif m.get("typ") == "wort" and sol.lower() not in entendu.lower():
                faute(o2, "la solution %r ne s'entend pas dans le message" % sol)
        nHS += 1
    print("Hoeren : %d serie(s), %d items ; Hoeren und Schreiben : %d serie(s), %d notes" % (nH, nH * 20, nHS, nHS * 5))
    if fautes:
        print("\n%d faute(s) :" % len(fautes))
        for f in fautes:
            print("   " + f)
        sys.exit(1)
    print("OK : le format du telc est respecte.")


main()
