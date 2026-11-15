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

LE MANUEL (15 nov. 2026, pflege/examen/FORMAT-MANUEL.md) : les series d'entrainement (entrainement/<epreuve>.json, a
« cle » comme les examens) et les chapitres (manuel/<chapitre>.json, manuel/sommaire.json) entrent dans le meme lot.
Les blocs d'un chapitre n'ont pas de « cle » : ils sont reperes par leur chemin (« rubriques[0].blocs[2].texte ») ;
les listes pas_* (le pas a pas d'un exercice) s'echangent comme des listes. Les [[allemand]] restent tels quels.
L'espagnol (« es ») est la 10e langue prevue : --langue es fonctionne deja.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONNEES = os.path.join(ICI, "donnees")
EPREUVES = ["hoeren", "lesen", "sprachbausteine", "schreiben", "sprechen"]
LANGUES = ["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru", "es"]
AUTRES = LANGUES[2:]
CHAPITRES = ["sommaire", "examen", "hoeren", "lesen", "sprachbausteine", "schreiben", "sprechen", "kommunikation", "beruf", "grammatik"]


def fichiers():
    """(nom du lot, chemin, par chemin ?) : les examens et l'entrainement a « cle », le manuel par chemin."""
    for e in EPREUVES:
        yield e, os.path.join(DONNEES, e + ".json"), False
    for e in EPREUVES:
        yield "entrainement/" + e, os.path.join(DONNEES, "entrainement", e + ".json"), False
    for c in CHAPITRES:
        yield "manuel/" + c, os.path.join(DONNEES, "manuel", c + ".json"), True


def par_chemin(x, chemin=""):
    """(objet, champ, cle) pour chaque champ traduit X (X_fr texte, ou pas_fr liste) de tout objet, repere par son chemin."""
    if isinstance(x, dict):
        for k in list(x):
            if k.endswith("_fr") and isinstance(x[k], (str, list)) and not k.startswith("_"):
                yield x, k[:-3], (chemin + "." if chemin else "") + k[:-3]
        for k, v in x.items():
            if isinstance(v, (dict, list)):
                yield from par_chemin(v, (chemin + "." if chemin else "") + k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from par_chemin(v, "%s[%d]" % (chemin, i))


def champs(d, chemin_seul):
    if chemin_seul:
        return list(par_chemin(d))
    return [(o, c, o["cle"] + "." + c) for o, c in objets(d)]


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
    vide = lambda v: not v or (isinstance(v, str) and not v.strip())
    for nom, chemin, seul in fichiers():
        if not os.path.exists(chemin):
            continue
        d = lire(chemin)
        m = {k: {"fr": o[c + "_fr"], "en": o.get(c + "_en", "")} for o, c, k in champs(d, seul) if vide(o.get(c + "_" + l))}
        if m:
            out[nom] = m
    return out


def appliquer(fichier, l):
    lot = lire(fichier)
    ui = lire(os.path.join(DONNEES, "interface.json"))
    ui.setdefault(l, {}).update({k: v for k, v in lot.get("interface", {}).items() if k in ui["fr"]})
    ui[l] = {k: ui[l][k] for k in ui["fr"] if k in ui[l]}
    ecrire(os.path.join(DONNEES, "interface.json"), ui)
    n = 0
    for e, chemin, seul in fichiers():
        if not lot.get(e) or not os.path.exists(chemin):
            continue
        d = lire(chemin)
        for o, c, k in champs(d, seul):
            v = lot[e].get(k)
            if isinstance(o.get(c + "_fr"), list) and v is not None and (not isinstance(v, list) or len(v) != len(o[c + "_fr"])):
                print("  %s %s : %d etapes attendues, ignore" % (e, k, len(o[c + "_fr"])))
                v = None
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
