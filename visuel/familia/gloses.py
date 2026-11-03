# -*- coding: utf-8 -*-
"""Les traductions des mots des themes illustres, tirees du CORPUS (relu), pour les langues d'interface ou la page ne
traduit pas la phrase entiere (ar, tr, uk, fa, pl, ru) : sous la phrase juste, « la abuela — бабуся ».

    python visuel/familia/gloses.py      -> visuel/prototype/familia/gloses.json, visuel/prototype/descripcion/gloses.json

Jacques, 3 nov. 2026 : « Il n'y a pas la traduction française. Qui serait importante ». La phrase entiere se traduit
en francais, anglais, portugais (et en allemand pour qui apprend l'espagnol) ; dans les autres langues, une phrase
fabriquee avec des prenoms etrangers aux cas du russe, de l'ukrainien, du polonais ou du turc serait fausse une fois
sur deux et personne ne la relirait : on donne le mot, que le corpus traduit deja.
Fichiers DERIVES du corpus : les refaire, pas les corriger.
"""
import io, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
LANGUES_DE = {"fr": "traduction", "en": "traduction_en", "tr": "traduction_tr", "uk": "traduction_uk", "fa": "traduction_fa",
              "ar": "traduction_ar", "pt": "traduction_pt", "pl": "traduction_pl", "ru": "traduction_ru"}
LANGUES_ES = {"fr": "traduction", "en": "traduction_en", "pt": "traduction_pt", "ar": "traduction_ar", "de": "traduction_de"}


def lire(p):
    return json.load(io.open(os.path.join(RACINE, p), encoding="utf-8"))


def noms(p):
    d = lire(p)
    return [m for t in d["themes"] for m in t["mots"]]


def adjectifs(p):
    d = lire(p)
    return [e for v in d.values() for e in v if isinstance(e, dict)]


def table(entrees, langues, voulus):
    out = {}
    for e in entrees:
        cle = ((e.get("genre") or "") + " " + e["mot"]).strip()
        if e["mot"] in voulus and cle not in out:
            out[cle] = {l: e[c] for l, c in langues.items() if e.get(c)}
    return out


FAMILLE_DE = ["Vater", "Mutter", "Sohn", "Tochter", "Mann", "Frau", "Bruder", "Schwester", "Großvater", "Großmutter", "Enkel", "Enkelin",
              "Onkel", "Tante", "Neffe", "Nichte", "Cousin", "Cousine", "Schwiegervater", "Schwiegermutter", "Schwiegersohn",
              "Schwiegertochter", "Schwager", "Schwägerin", "Eltern", "Geschwister", "Großeltern"]
FAMILLE_ES = ["padre", "madre", "hijo", "hija", "marido", "mujer", "hermano", "hermana", "abuelo", "abuela", "nieto", "nieta", "tío", "tía",
              "sobrino", "sobrina", "primo", "prima", "suegro", "suegra", "yerno", "nuera", "cuñado", "cuñada"]
DESC_DE_N = ["Brille", "Bart"]
DESC_DE_A = ["schwarz", "braun", "blond", "rot", "glatt", "kurz", "lang", "grün", "blau", "dunkel", "grau", "schlank", "mollig", "kräftig", "groß", "klein"]
DESC_ES_N = ["gafas", "gafas de sol", "barba", "bigote", "tatuaje"]
DESC_ES_A = ["negro", "castaño", "rubio", "rojo", "liso", "rizado", "corto", "largo", "verde", "azul", "gris", "delgado", "gordito", "fuerte", "alto", "bajo", "pelirrojo", "calvo"]

# Le sens de la TAILLE d'une personne, la ou le corpus donne le sens general (3 nov. 2026, relecture qualite :
# « büyük » et « великий » disent « gros, grand en volume », pas « de grande taille »). Le corpus garde son sens.
SENS_TAILLE = {"groß": {"tr": "uzun boylu", "uk": "високий"}, "klein": {"tr": "kısa boylu", "uk": "невисокий"}}


def main():
    fam = {"de": table(noms("themes.json"), LANGUES_DE, FAMILLE_DE), "es": table(noms("espanol/datos/temas.json"), LANGUES_ES, FAMILLE_ES)}
    desc = {"de": dict(table(noms("themes.json"), LANGUES_DE, DESC_DE_N), **table(adjectifs("adjectif.json"), LANGUES_DE, DESC_DE_A)),
            "es": dict(table(noms("espanol/datos/temas.json"), LANGUES_ES, DESC_ES_N), **table(adjectifs("espanol/datos/adjetivos.json"), LANGUES_ES, DESC_ES_A))}
    for m, t in SENS_TAILLE.items():
        desc["de"].setdefault(m, {}).update(t)
    for nom, d, voulus in (("familia", fam, {"de": FAMILLE_DE, "es": FAMILLE_ES}), ("descripcion", desc, {"de": DESC_DE_N + DESC_DE_A, "es": DESC_ES_N + DESC_ES_A})):
        for l in d:
            trouves = {k.split(" ", 1)[-1] for k in d[l]}
            manque = [m for m in voulus[l] if m not in trouves]
            if manque: print("  %s %s : sans traduction au corpus : %s" % (nom, l, manque))
        chemin = os.path.join(RACINE, "visuel", "prototype", nom, "gloses.json")
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
        print("  -> %s (%d + %d mots)" % (os.path.relpath(chemin, RACINE), len(d["de"]), len(d["es"])))


if __name__ == "__main__":
    main()
