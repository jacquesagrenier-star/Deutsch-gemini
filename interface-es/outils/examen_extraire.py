# -*- coding: utf-8 -*-
"""pruefung.json (les epreuves d'examen) : les textes a traduire en espagnol.

    python interface-es/outils/examen_extraire.py

Ecrit interface-es/sources/examen-<section>.json : [{cle, de, fr, en}], la cle
etant celle de russe/outils/poser_examen.py (« lesen/3/1|frage »), qui pose
ensuite : python interface-es/outils/poser_examen_es.py pruefung.json es <lot> [...] --ecrire
(copie du russe, ou l'espagnol a droit aux guillemets « »). `de` donne
l'allemand de l'epreuve (la question, le texte lu ou les morceaux a ordonner).
"""
import io, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.path.dirname(ICI)
d = json.load(io.open(os.path.join(RACINE, "pruefung.json"), encoding="utf-8"))


def allemand(o, parent=None):
    morceaux = []
    for k in ("frage", "aufgabe", "text", "transkript", "satz"):
        if isinstance(o.get(k), str):
            morceaux.append(o[k])
    if isinstance(o.get("chunks"), list):
        morceaux.append(" ".join(x for x in o["chunks"] if isinstance(x, str)))
    if not morceaux and parent:
        return allemand(parent)
    return " || ".join(morceaux)[:900]


def relever(path, o, out, parent=None):
    for k in o:
        if not k.endswith("_fr"):
            continue
        base = k[:-3]
        if (base + "_es") in o:
            continue
        out.append({"cle": path + "|" + base, "de": allemand(o, parent), "fr": o[k], "en": o.get(base + "_en", "")})


total = 0
for sec in ["sprechen", "schreiben", "lesen", "hoeren"]:
    out = []
    for i, o in enumerate(d[sec]):
        p = sec + "/" + str(i)
        relever(p, o, out)
        if sec == "lesen":
            for j, q in enumerate(o.get("fragen", [])):
                relever(p + "/" + str(j), q, out, parent=o)
    io.open(os.path.join(ICI, "sources", "examen-%s.json" % sec), "w", encoding="utf-8").write(
        json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print("%s : %d textes" % (sec, len(out)))
    total += len(out)
print("total %d" % total)
