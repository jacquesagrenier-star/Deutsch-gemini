# -*- coding: utf-8 -*-
"""Espagnol : present et preterit compares a la forme reguliere.

Toute difference est listee ; on retire ensuite ce que la grammaire explique
(diphtongue, e->i, -zco, -go, y entre voyelles, c->qu...). Ce qui reste est a
regarder a la main.
"""
import json
import re
import sys

from commun import charger
from verbes_es import sans_accent, nu, base

FINS = {"ar": (["o", "as", "a", "amos", "áis", "an"], ["é", "aste", "ó", "amos", "asteis", "aron"]),
        "er": (["o", "es", "e", "emos", "éis", "en"], ["í", "iste", "ió", "imos", "isteis", "ieron"]),
        "ir": (["o", "es", "e", "imos", "ís", "en"], ["í", "iste", "ió", "imos", "isteis", "ieron"])}


def reguliers(inf):
    t = sans_accent(inf[-2:])
    r = inf[:-2]
    pr, pt = FINS[t]
    return [r + e for e in pr], [r + e for e in pt]


def explique_present(inf, i, a, att):
    # diphtongue / e->i sur 1,2,3,6 ; -zco/-go/-oy/-igo au yo ; -uir -> uy ; accent sur u/i (reúno, envío)
    if i in (0, 1, 2, 5):
        for x, y in (("e", "ie"), ("o", "ue"), ("e", "i"), ("u", "ue"), ("i", "ie"), ("i", "í"), ("u", "ú")):
            if sans_accent(a) == sans_accent(att) or att.replace(x, y) == a or \
                    att[::-1].replace(x[::-1], y[::-1], 1)[::-1] == a:
                return True
        if inf.endswith("uir") and a.replace("uy", "u") == att:
            return True
    if i == 0 and re.search(r"(zco|go|oy|igo|jo|zo|ío|úo|yo)$", a):
        return True
    if sans_accent(a) == sans_accent(att):
        return True
    return False


def explique_preterit(inf, i, a, att):
    if i == 0 and re.search(r"(qué|gué|cé|güé)$", a):
        return True
    if i in (2, 5) and (re.search(r"yó$|yeron$", a) or "i" in a and att.replace("e", "i", 1) == a
                        or att.replace("o", "u", 1) == a):
        return True
    if sans_accent(a) == sans_accent(att):
        return True
    if inf.endswith(("eer", "aer", "oír", "uir")) and a.replace("í", "i") == att.replace("í", "i"):
        return True
    return False


def main():
    VE = charger("espanol/datos/verbos.json")
    out = []
    for niv, lst in VE.items():
        for k, v in enumerate(lst):
            if " " in v["mot"].strip() and not v["mot"].endswith("se"):
                continue
            inf = base(v["infinitif"])
            if sans_accent(inf[-2:]) not in FINS:
                continue
            pres = [nu(x) for x in (v.get("praesens") or {}).values()]
            pret = [nu(x) for x in (v.get("preterito") or [])]
            rp, rt = reguliers(inf)
            dp = [(i, a, b) for i, (a, b) in enumerate(zip(pres, rp)) if a != b and not explique_present(inf, i, a, b)]
            dt = [(i, a, b) for i, (a, b) in enumerate(zip(pret, rt)) if a != b and not explique_preterit(inf, i, a, b)]
            if dp or dt:
                out.append({"ou": "verbos.%s[%d]" % (niv, k), "mot": v["mot"], "present": dp, "preterit": dt,
                            "pres": pres, "pret": pret})
    for o in out:
        print(o["mot"], "| P:", " ".join(o["pres"]), "| T:", " ".join(o["pret"]))
    print(len(out))
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
