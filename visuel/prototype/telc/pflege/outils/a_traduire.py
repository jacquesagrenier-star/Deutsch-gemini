"""Ce qui reste a traduire dans les 7 autres langues d'interface de l'examen telc Pflege (tr, uk, fa, ar, pt, pl, ru).

    python visuel/prototype/telc/pflege/outils/a_traduire.py            # le compte, langue par langue
    python visuel/prototype/telc/pflege/outils/a_traduire.py --sortie f.json [--langue tr]
        # {"interface": {cle: {fr, en}}, "<epreuve>": {cle.champ: {fr, en}}} : ce qui manque (toutes les cles sans --langue)

Les traductions vont dans donnees/langues/interface.<l>.json et donnees/modell-1/langues/<epreuve>.<l>.json, des
dictionnaires plats {cle: texte}. On traduit depuis le francais (l'anglais aide a lever une ambiguite) ; l'allemand
de l'examen ne se traduit jamais. Les {x} restent tels quels.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DONNEES = os.path.join(ICI, "donnees")
EPREUVES = ["hoeren", "lesen", "sprachbausteine", "schreiben", "sprechen"]
AUTRES = ["tr", "uk", "fa", "ar", "pt", "pl", "ru"]


def lire(chemin, defaut=None):
    return json.load(io.open(chemin, encoding="utf-8")) if os.path.exists(chemin) else defaut


def objets(x):
    if isinstance(x, dict):
        champs = [k[:-3] for k in x if k.endswith("_fr") and isinstance(x[k], str)]
        if champs and "cle" in x:
            for c in champs:
                yield x["cle"] + "." + c, {"fr": x[c + "_fr"], "en": x.get(c + "_en", "")}
        for v in x.values():
            yield from objets(v)
    elif isinstance(x, list):
        for v in x:
            yield from objets(v)


def sources():
    ui = lire(os.path.join(DONNEES, "interface.json"))
    out = {"interface": {k: {"fr": v, "en": ui["en"].get(k, "")} for k, v in ui["fr"].items()}}
    for e in EPREUVES:
        d = lire(os.path.join(DONNEES, "modell-1", e + ".json"))
        if d:
            out[e] = dict(objets(d))
    return out


def fichier(groupe, l):
    if groupe == "interface":
        return os.path.join(DONNEES, "langues", "interface.%s.json" % l)
    return os.path.join(DONNEES, "modell-1", "langues", "%s.%s.json" % (groupe, l))


def main():
    S = sources()
    langue = sys.argv[sys.argv.index("--langue") + 1] if "--langue" in sys.argv else None
    if "--sortie" in sys.argv:
        out = {}
        for g, cles in S.items():
            deja = lire(fichier(g, langue), {}) if langue else {}
            out[g] = {k: v for k, v in cles.items() if not (deja.get(k) or "").strip()}
        io.open(sys.argv[sys.argv.index("--sortie") + 1], "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=1))
        print("%d textes a traduire" % sum(len(v) for v in out.values()))
        return
    for l in AUTRES:
        manque = sum(1 for g, cles in S.items() for k in cles if not (lire(fichier(g, l), {}).get(k) or "").strip())
        print("%s : %d texte(s) manquant(s) sur %d" % (l, manque, sum(len(v) for v in S.values())))


if __name__ == "__main__":
    main()
