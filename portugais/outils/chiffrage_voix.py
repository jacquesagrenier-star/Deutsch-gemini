# -*- coding: utf-8 -*-
"""Combien coûterait une voix enregistree (ElevenLabs) pour l'A1 portugais ?

    python portugais/outils/chiffrage_voix.py

NE GENERE RIEN ET NE DEPENSE RIEN : il lit portugais/datos et compte les
textes que l'app dirait a voix haute en portugais, dedoublonnes, avec la
porteuse des mots seuls (« Palavra: casa. », comptee dans le prix, comme
« Word: kitchen. » pour l'anglais). Modele multilingual v2 : 1 caractere =
1 credit. Les traductions francaises restent a la voix du telephone.
"""
import io, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.path.dirname(os.path.dirname(ICI)), "portugais", "datos")
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
PORTEUSE = "Palavra: %s."


def ch(f):
    return json.load(io.open(os.path.join(D, f), encoding="utf-8"))


def compter():
    mots, phrases = set(), set()

    def mot(t):
        if t and t.strip() and t != "—":
            mots.add(t.strip())

    def phrase(t):
        if t and t.strip():
            phrases.add(t.strip())

    for t in ch("themes.json")["themes"]:
        for m in t["mots"]:
            mot((m["genre"] + " " + m["mot"]).strip())
            if m["pluriel"] != "—" and m["genre"] in ("o", "a"):
                mot(("os " if m["genre"] == "o" else "as ") + m["pluriel"])
            phrase(m["exemple"])
    for v in ch("verbes.json")["A1"]:
        mot(v["infinitif"])
        phrase(v["exemple"])
        for f in v["praesens"].values():
            mot(f)
    for a in ch("adjectifs.json")["A1"]:
        mot(a["mot"])
        f = a["formes"]
        for k in ("feminin", "pluriel", "feminin_pluriel", "comparatif", "superlatif"):
            mot(f.get(k))
        phrase(a["exemple"])
    for fic in ("adverbes.json", "expressions.json"):
        for e in ch(fic)["A1"]:
            mot(e["mot"])
            phrase(e["exemple"])
    for liste in ch("fonctionnels.json").values():
        for e in liste:
            mot(e["mot"])
            phrase(e["exemple"])
    for e in ch("premiers-pas.json")["etapes"]:
        for c in e["cartes"]:
            mot(c[0])
            phrase(c[2])
        for p in e["phrases"]:
            phrase(p["p"])
        for l in e["tableau"]["l"]:
            phrase(l[0])
    av = ch("a1-voyage.json")
    for e in av["escales"] + av["installe"]:
        for b in e["blocs"]:
            phrase(b["ex"])
            for v in b["v"]:
                mot(v)
        for l in e["dialogue"]["l"]:
            phrase(l["p"])
        for l in e["tableau"]["l"]:
            phrase(l[0])
    for r in ch("reperes.json")["reperes"]:
        for l in r.get("l", []):
            if isinstance(l, list) and l and isinstance(l[0], str):
                mot(l[0])
    for g in ch("prononciation.json")["groupes"]:
        for r in g["regles"]:
            for x in r["exemples"]:
                mot(x["mot"])
    for jeu in ch("exercices.json")["jeux"].values():
        for q in jeu:
            phrase(q["question"].replace("___", q["correct"]))
    mots -= phrases
    n_mots = sum(len(PORTEUSE % m) for m in mots)
    n_phr = sum(len(p) for p in phrases)
    return len(mots), n_mots, len(phrases), n_phr


if __name__ == "__main__":
    nm, cm, np_, cp = compter()
    print("A1 portugais : %d mots seuls (%d caracteres avec la porteuse), %d phrases (%d caracteres)." % (nm, cm, np_, cp))
    print("Total : %d textes, %d credits (multilingual v2), hors reprises (compter 5 a 10 %%)." % (nm + np_, cm + cp))
