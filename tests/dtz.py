"""Controle des donnees du DTZ (Hoeren et Lesen) : dtz/donnees/hoeren.json et lesen.json.

    python tests/dtz.py            -> les defauts, et le bilan par serie
    python tests/dtz.py --mots     -> en plus, la liste des mots cles absents du corpus

Ce que le JSON ne dit pas a la relecture, et que ce script compte :
  - le FORMAT DU DTZ (Pruefungshandbuch 2009) : 20 items en Hoeren (4 + 5 + 8 + 3), 25 en Lesen
    (5 + 5 + 6 + 3 + 6), numerotes sans trou ni doublon, chaque Teil avec son exemple la ou l'examen en a un ;
  - une bonne reponse qui existe (bon dans les options, une lettre de T2 qui existe, x une seule fois par
    serie, chaque annonce de T2 au plus une fois, deux phrases de T4 sans personne) ;
  - LA FEUILLE DE REPONSES NE DOIT PAS SE DEVINER : dans une serie, aucune lettre ne porte plus de la moitie
    des bonnes reponses a 3 choix ;
  - les mots cles (repetition espacee) qui existent dans le corpus allemand, a la forme que lit
    carteDeScene() d'index.html : un nom (mot + genre) dans themes.json, un verbe par son infinitif dans
    verbe.json, un adjectif dans adjectif.json. Un mot absent ne casse rien (l'app l'ignore) : il est signale.
"""
import json
import os
import sys
from collections import Counter

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONNEES = os.path.join(RACINE, "dtz", "donnees")

ATTENDU_H = {"T1": 4, "T2": 5, "T3": 8, "T4": 3}
ATTENDU_L = {"T1": 5, "T2": 5, "T3": 6, "T4": 3, "T5": 6}


def charger(nom):
    with open(os.path.join(DONNEES, nom), encoding="utf-8") as f:
        return json.load(f)


def corpus():
    noms, verbes, adjs = set(), set(), set()
    with open(os.path.join(RACINE, "themes.json"), encoding="utf-8") as f:
        for th in json.load(f)["themes"]:
            for m in th.get("mots", []):
                noms.add((m.get("mot"), m.get("genre")))
    with open(os.path.join(RACINE, "verbe.json"), encoding="utf-8") as f:
        for niv in json.load(f).values():
            for v in niv:
                verbes.add(v.get("infinitif"))
    with open(os.path.join(RACINE, "adjectif.json"), encoding="utf-8") as f:
        for niv in json.load(f).values():
            for a in niv:
                adjs.add(a.get("mot"))
    return noms, verbes, adjs


def main():
    voir_mots = "--mots" in sys.argv
    defauts, absents = [], []
    noms, verbes, adjs = corpus()

    def mots(ou, liste):
        for m in liste or []:
            cat = m.get("cat")
            if cat == "verbe":
                ok = m["mot"] in verbes
            elif cat == "adjectif":
                ok = m["mot"] in adjs
            elif cat is None:
                ok = (m["mot"], m.get("genre")) in noms
            else:
                ok = False
                defauts.append("%s : cat « %s » inconnue de carteDeScene (nom, verbe ou adjectif seulement)" % (ou, cat))
            if not ok:
                absents.append("%s : %s %s" % (ou, m.get("genre") or cat or "", m["mot"]))

    def choix(ou, it, n=3):
        opts = it.get("optionen") or []
        if len(opts) != n:
            defauts.append("%s : %d options au lieu de %d" % (ou, len(opts), n))
        if not isinstance(it.get("bon"), int) or not 0 <= it["bon"] < len(opts):
            defauts.append("%s : bon hors des options" % ou)
        if "optionen_fr" in it and len(it["optionen_fr"]) != len(opts):
            defauts.append("%s : optionen_fr n'a pas la longueur de optionen" % ou)
        for cle in ("frage", "frage_fr", "erkl_fr"):
            if not it.get(cle):
                defauts.append("%s : %s manque" % (ou, cle))

    H = charger("hoeren.json")
    L = charger("lesen.json")
    voix = H.get("voix", {})

    for s in H["series"]:
        sid = s["id"]
        nrs, lettres = [], Counter()
        for teil in ("T1", "T2", "T3"):
            items = s[teil]
            vrais = [i for i in items if not i.get("beispiel")]
            if len(vrais) != ATTENDU_H[teil]:
                defauts.append("Hören %s %s : %d items au lieu de %d" % (sid, teil, len(vrais), ATTENDU_H[teil]))
            if teil in ("T1", "T3") and not any(i.get("beispiel") for i in items):
                defauts.append("Hören %s %s : pas d'exemple" % (sid, teil))
            audios = {i["nr"]: i for i in items if i.get("audio")}
            for it in items:
                ou = "Hören %s %s nr %s" % (sid, teil, it["nr"])
                if not it.get("beispiel"):
                    nrs.append(it["nr"])
                n = 2 if it.get("rf") else 3
                choix(ou, it, n)
                if n == 3 and not it.get("beispiel"):
                    lettres["abc"[it["bon"]]] += 1
                if not it.get("audio") and it.get("gleiches_audio") not in audios:
                    defauts.append("%s : ni audio ni gleiches_audio valable" % ou)
                for r in it.get("audio") or []:
                    if r.get("wer") not in voix:
                        defauts.append("%s : voix « %s » inconnue" % (ou, r.get("wer")))
                mots(ou, it.get("mots"))
        # T3 : par conversation, un vrai/faux puis un choix a 3
        convs = {}
        for it in s["T3"]:
            if it.get("gespraech"):
                convs.setdefault(it["gespraech"], []).append(it)
        for g, its in convs.items():
            if [bool(i.get("rf")) for i in its] != [True, False]:
                defauts.append("Hören %s T3 Gespräch %s : il faut un vrai/faux puis un choix a 3" % (sid, g))
        t4 = s["T4"]
        lettres_t4 = [x["b"] for x in t4["saetze"]]
        if lettres_t4 != list("abcdef"):
            defauts.append("Hören %s T4 : les phrases doivent etre a-f" % sid)
        prises = []
        for a in t4["aussagen"]:
            ou = "Hören %s T4 nr %s" % (sid, a["nr"])
            if a["bon"] not in lettres_t4:
                defauts.append("%s : bon « %s » n'est pas une phrase" % (ou, a["bon"]))
            prises.append(a["bon"])
            if not a.get("beispiel"):
                nrs.append(a["nr"])
            for r in a.get("audio") or []:
                if r.get("wer") not in voix:
                    defauts.append("%s : voix « %s » inconnue" % (ou, r.get("wer")))
            mots(ou, a.get("mots"))
        if len(set(prises)) != len(prises):
            defauts.append("Hören %s T4 : une phrase sert deux fois" % sid)
        if len(set(lettres_t4) - set(prises)) != 2:
            defauts.append("Hören %s T4 : il faut exactement deux phrases de trop" % sid)
        if len([a for a in t4["aussagen"] if not a.get("beispiel")]) != ATTENDU_H["T4"]:
            defauts.append("Hören %s T4 : %d avis au lieu de 3" % (sid, len(t4["aussagen"]) - 1))
        if sorted(nrs) != list(range(1, 21)):
            defauts.append("Hören %s : numeros %s, attendu 1-20" % (sid, sorted(nrs)))
        tot = sum(lettres.values())
        if tot and max(lettres.values()) > tot / 2:
            defauts.append("Hören %s : la lettre %s porte %d bonnes reponses sur %d" % (sid, lettres.most_common(1)[0][0], lettres.most_common(1)[0][1], tot))
        print("Hören %s : %d items, bonnes reponses a/b/c = %s" % (sid, len(nrs), dict(sorted(lettres.items()))))

    for s in L["series"]:
        sid = s["id"]
        nrs, lettres = [], Counter()

        def compte(ou, it, n=3):
            choix(ou, it, n)
            if not it.get("beispiel"):
                nrs.append(it["nr"])
                if n == 3:
                    lettres["abc"[it["bon"]]] += 1
            mots(ou, it.get("mots"))

        t1 = s["T1"]
        if not 5 <= len(t1["dokument"]["zeilen"]) <= 9:
            defauts.append("Lesen %s T1 : %d rubriques (5-7 dans le manuel)" % (sid, len(t1["dokument"]["zeilen"])))
        for it in t1["items"]:
            compte("Lesen %s T1 nr %s" % (sid, it["nr"]), it)
            if not it["optionen"][2].startswith("andere"):
                defauts.append("Lesen %s T1 nr %s : la 3e option doit etre l'option negative" % (sid, it["nr"]))
        if len([i for i in t1["items"] if not i.get("beispiel")]) != 5:
            defauts.append("Lesen %s T1 : il faut 5 items" % sid)

        t2 = s["T2"]
        ann = [a["b"] for a in t2["anzeigen"]]
        if ann != list("abcdefgh"):
            defauts.append("Lesen %s T2 : il faut huit annonces a-h" % sid)
        prises = []
        for it in t2["items"]:
            ou = "Lesen %s T2 nr %s" % (sid, it["nr"])
            if it["bon"] != "x" and it["bon"] not in ann:
                defauts.append("%s : bon « %s » n'est pas une annonce" % (ou, it["bon"]))
            prises.append(it["bon"])
            if not it.get("beispiel"):
                nrs.append(it["nr"])
            for cle in ("situation", "situation_fr", "erkl_fr"):
                if not it.get(cle):
                    defauts.append("%s : %s manque" % (ou, cle))
            mots(ou, it.get("mots"))
        if prises.count("x") != 1:
            defauts.append("Lesen %s T2 : il faut exactement une situation sans annonce (x)" % sid)
        sans_x = [p for p in prises if p != "x"]
        if len(set(sans_x)) != len(sans_x):
            defauts.append("Lesen %s T2 : une annonce sert deux fois" % sid)

        t3 = s["T3"]
        if len(t3["texte"]) != 3:
            defauts.append("Lesen %s T3 : %d textes au lieu de 3" % (sid, len(t3["texte"])))
        for tx in t3["texte"]:
            if [bool(i.get("rf")) for i in tx["items"]] != [True, False]:
                defauts.append("Lesen %s T3 « %s » : il faut un vrai/faux puis un choix a 3" % (sid, tx["titel"]))
            for it in tx["items"]:
                compte("Lesen %s T3 nr %s" % (sid, it["nr"]), it, 2 if it.get("rf") else 3)

        for it in s["T4"]["items"]:
            compte("Lesen %s T4 nr %s" % (sid, it["nr"]), it, 2)
            if not it.get("rf"):
                defauts.append("Lesen %s T4 nr %s : T4 est en vrai/faux" % (sid, it["nr"]))

        t5 = s["T5"]
        texte = t5["brief"]["betreff"] + " " + " ".join(t5["brief"]["text"])
        for lu in t5["luecken"]:
            ou = "Lesen %s T5 nr %s" % (sid, lu["nr"])
            if "{%d}" % lu["nr"] not in texte:
                defauts.append("%s : le trou {%d} n'est pas dans la lettre" % (ou, lu["nr"]))
            if len(lu["optionen"]) != 3 or not 0 <= lu["bon"] < 3:
                defauts.append("%s : il faut 3 options et un bon valable" % ou)
            if not lu.get("erkl_fr"):
                defauts.append("%s : erkl_fr manque" % ou)
            if not lu.get("beispiel"):
                nrs.append(lu["nr"])
                lettres["abc"[lu["bon"]]] += 1
            mots(ou, lu.get("mots"))
        if not any(lu.get("beispiel") for lu in t5["luecken"]):
            defauts.append("Lesen %s T5 : pas d'exemple" % sid)

        if sorted(nrs) != list(range(1, 26)):
            defauts.append("Lesen %s : numeros %s, attendu 1-25" % (sid, sorted(nrs)))
        tot = sum(lettres.values())
        if tot and max(lettres.values()) > tot / 2:
            defauts.append("Lesen %s : la lettre %s porte trop de bonnes reponses" % (sid, lettres.most_common(1)[0][0]))
        print("Lesen %s : %d items, bonnes reponses a/b/c (choix a 3) = %s" % (sid, len(nrs), dict(sorted(lettres.items()))))

    print()
    print("Series : %d en Hören, %d en Lesen (au moins 6 voulues, dont 3 pour l'examen blanc)" % (len(H["series"]), len(L["series"])))
    print("Mots cles absents du corpus : %d%s" % (len(absents), "" if voir_mots else " (--mots pour la liste)"))
    if voir_mots:
        for a in absents:
            print("  " + a)
    if defauts:
        print("\n%d DEFAUT(S) :" % len(defauts))
        for d in defauts:
            print("  - " + d)
        sys.exit(1)
    print("Aucun defaut.")


if __name__ == "__main__":
    main()
