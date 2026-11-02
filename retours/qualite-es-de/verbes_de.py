# -*- coding: utf-8 -*-
"""Allemand : chaque phrase d'un verbe (present, Perfekt, Praeteritum,
Konjunktiv II) contient-elle une forme de CE verbe ?

On compare le squelette du radical (consonnes du debut et de la fin), parce que
l'ablaut change les voyelles : nehmen -> nahm, genommen, naehme.

    python retours/qualite-es-de/verbes_de.py [sortie.json]
"""
import json
import re
import sys

from commun import charger

PREFIXES = sorted("ab an auf aus bei ein mit nach vor weg zu zurück fest los her hin um durch über unter wieder weiter fort heraus herein hinaus voran zusammen statt teil kennen spazieren dar empor entgegen gegenüber nieder vorbei vorüber ge be ver zer er ent emp miss".split(), key=len, reverse=True)
SUPPLETIFS = {"sein": ("bin", "bist", "ist", "sind", "seid", "war", "wär", "gewesen", "sei"),
              "werden": ("wird", "wirst", "wurd", "würd", "word", "werd"),
              "gehen": ("geh", "ging", "gang"), "stehen": ("steh", "stand", "stünd", "stün"),
              "tun": ("tu", "tat", "tät", "getan"), "haben": ("hab", "hat", "hätt", "hast")}


def racine(inf):
    inf = inf.replace("sich ", "").split()[-1]
    r = inf[:-2] if inf.endswith("en") else inf[:-1] if inf.endswith("n") else inf
    pref = ""
    for p in PREFIXES:
        if r.startswith(p) and len(r) - len(p) >= 2:
            pref, r = p, r[len(p):]
            break
    return pref, r


def debut(r):
    m = re.match(r"^[^aeiouäöüy]*", r)
    return m.group(0) or r[:1]


def fin(r):
    m = re.search(r"[^aeiouäöüyh]+$", r)
    return m.group(0) if m else ""


EQUIV = {"g": "(g|ch)", "k": "(k|ch|ck)", "ck": "(ck|k|ch)", "tz": "(tz|ß|ss|s)", "ss": "(ss|ß)",
         "ß": "(ß|ss)", "nk": "(nk|ch)", "ng": "(ng|ch)", "nd": "(nd|n|t)", "dd": "d"}


def motif(inf):
    pref, r = racine(inf)
    d, f = debut(r), fin(r)
    if not d:
        d = r[:1]
    fpat = EQUIV.get(f, re.escape(f)) if f and f != d else ""
    return pref, re.compile(re.escape(d) + r"\w*" + fpat, re.I) if fpat else re.compile(re.escape(d), re.I)


def contient(inf, phrase):
    base = inf.replace("sich ", "").split()[-1]
    if base in SUPPLETIFS:
        return any(f in phrase.lower() for f in SUPPLETIFS[base])
    pref, pat = motif(inf)
    for tok in re.findall(r"\w+", phrase):
        t = tok.lower()
        for cand in (t, t[2:] if t.startswith("ge") else t,
                     t[len(pref):] if pref and t.startswith(pref) else t,
                     t[len(pref) + 2:] if pref and t.startswith(pref + "ge") else t,
                     t[len(pref) + 2:] if pref and t.startswith(pref + "zu") else t):
            if pat.match(cand):
                return True
    return False


def main():
    out = []
    VB = charger("verbe.json")
    n = 0
    for niv, lst in VB.items():
        for i, v in enumerate(lst):
            for champ in ("exemple", "perfekt", "praeteritum", "konjunktiv2"):
                ph = v.get(champ)
                if not ph:
                    continue
                n += 1
                if not contient(v["infinitif"], ph):
                    out.append({"ou": "verbe.%s[%d].%s" % (niv, i, champ), "mot": v["infinitif"],
                                "phrase": ph, "fr": v.get(champ + "_fr"), "code": "phrase_sans_verbe"})
            # le present : ich/wir/sie et l'infinitif
            pr = v.get("praesens") or {}
            inf = v["infinitif"].replace("sich ", "")
            if pr and " " not in inf and inf not in ("sein", "tun"):
                if pr.get("wir") and pr["wir"].split()[0] != inf and not pr["wir"].startswith(inf) \
                        and not inf.endswith(pr["wir"].split()[0]):
                    out.append({"ou": "verbe.%s[%d].praesens" % (niv, i), "mot": v["infinitif"],
                                "phrase": json.dumps(pr, ensure_ascii=False), "code": "wir_different"})
                if pr.get("wir") != pr.get("sie_Sie"):
                    out.append({"ou": "verbe.%s[%d].praesens" % (niv, i), "mot": v["infinitif"],
                                "phrase": json.dumps(pr, ensure_ascii=False), "code": "wir_sie_differents"})
    print("phrases :", n, "signalements :", len(out))
    for o in out:
        print(o["code"], o["ou"], o["mot"], "|", o["phrase"][:100])
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
