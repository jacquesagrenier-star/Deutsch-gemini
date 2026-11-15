"""Les traductions de l'examen telc Pflege : ce qui manque dans les 9 langues d'interface, et le repli d'un lot traduit.

    python visuel/prototype/telc-pflege/outils/a_traduire.py                       # le compte, langue par langue
    python visuel/prototype/telc-pflege/outils/a_traduire.py --sortie f.json --langue tr
        # ce qui manque en turc : {"interface": {cle: {fr, en}}, "<epreuve>": {"<cle>.<champ>": {fr, en}}}
    python visuel/prototype/telc-pflege/outils/a_traduire.py --appliquer t.json --langue tr
        # replie un lot traduit {"interface": {cle: texte}, "<epreuve>": {"<cle>.<champ>": texte}} dans les donnees

Les langues vivent dans les donnees memes (contrat pflege/FORMAT-DONNEES.md) : un champ traduit « X » d'un objet porteur
d'une « cle » s'ecrit X_fr, X_en, X_tr, X_uk, X_fa, X_pt, X_ar, X_pl, X_ru ; l'interface est dans donnees/interface.json
({fr: {…}, en: {…}, tr: {…}…}). On traduit depuis le francais ; l'allemand de l'examen ne se traduit jamais ; les {x}
restent tels quels. Un texte francais qui change rend sa traduction perimee : la refaire dans les 7 langues.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONNEES = os.path.join(ICI, "donnees")
EPREUVES = ["hoeren", "lesen", "sprachbausteine", "schreiben", "sprechen"]
LANGUES = ["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]
AUTRES = LANGUES[2:]


def lire(chemin):
    return json.load(io.open(chemin, encoding="utf-8"))


def ecrire(chemin, d):
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def objets(x):
    """(objet, champ) pour chaque champ traduit X d'un objet porteur d'une cle."""
    if isinstance(x, dict):
        if "cle" in x:
            for k in list(x):
                if k.endswith("_fr") and isinstance(x[k], str):
                    yield x, k[:-3]
        for v in x.values():
            yield from objets(v)
    elif isinstance(x, list):
        for v in x:
            yield from objets(v)


def manques(l):
    ui = lire(os.path.join(DONNEES, "interface.json"))
    out = {"interface": {k: {"fr": v, "en": ui["en"].get(k, "")} for k, v in ui["fr"].items() if not (ui.get(l, {}).get(k) or "").strip()}}
    for e in EPREUVES:
        d = lire(os.path.join(DONNEES, e + ".json"))
        out[e] = {o["cle"] + "." + c: {"fr": o[c + "_fr"], "en": o.get(c + "_en", "")} for o, c in objets(d)
                  if not (o.get(c + "_" + l) or "").strip()}
    return out


def appliquer(fichier, l):
    lot = lire(fichier)
    ui = lire(os.path.join(DONNEES, "interface.json"))
    ui.setdefault(l, {}).update({k: v for k, v in lot.get("interface", {}).items() if k in ui["fr"]})
    ui[l] = {k: ui[l][k] for k in ui["fr"] if k in ui[l]}
    ecrire(os.path.join(DONNEES, "interface.json"), ui)
    n = 0
    for e in EPREUVES:
        if not lot.get(e):
            continue
        chemin = os.path.join(DONNEES, e + ".json")
        d = lire(chemin)
        for o, c in objets(d):
            v = lot[e].get(o["cle"] + "." + c)
            if v:
                o[c + "_" + l] = v
                n += 1
            # l'ordre des champs : celui du contrat
            vals = {lg: o.pop(c + "_" + lg) for lg in LANGUES if c + "_" + lg in o}
            for lg in LANGUES:
                if lg in vals:
                    o[c + "_" + lg] = vals[lg]
        ecrire(chemin, d)
    print("%d texte(s) d'interface et %d aide(s) repliee(s) en %s" % (len(lot.get("interface", {})), n, l))


def main():
    langue = sys.argv[sys.argv.index("--langue") + 1] if "--langue" in sys.argv else None
    if "--appliquer" in sys.argv:
        return appliquer(sys.argv[sys.argv.index("--appliquer") + 1], langue)
    if "--sortie" in sys.argv:
        out = manques(langue)
        io.open(sys.argv[sys.argv.index("--sortie") + 1], "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=1))
        print("%d textes a traduire" % sum(len(v) for v in out.values()))
        return
    for l in AUTRES:
        m = manques(l)
        print("%s : %d texte(s) manquant(s)" % (l, sum(len(v) for v in m.values())))


if __name__ == "__main__":
    main()
