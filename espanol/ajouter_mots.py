# -*- coding: utf-8 -*-
"""Verse un fichier d'ajouts dans le corpus espagnol (temas.json, variantes.json).

    python espanol/ajouter_mots.py espanol/ajouts/mots-scenes.json

Le pendant espagnol de tests/ajouter_mots.py. IDEMPOTENT : un mot deja
present dans son theme n'est pas rajoute, un theme deja cree n'est pas
recree, une variante deja posee n'est pas ecrasee. Relancer ne change rien.

Format du fichier d'ajouts : voir son « _lisez_moi ». Chaque entree est une
ligne [mot, article, pluriel, traduction fr, traduction en, exemple,
exemple fr, exemple en] -- l'ordre des champs du corpus, sans rien a nommer.

Un mot sans pluriel (las gafas, los calzoncillos) porte null : l'app ne le
dit qu'une fois.
"""
import io, json, os, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")


def lire(chemin):
    return json.load(io.open(chemin, encoding="utf-8"))


def ecrire(chemin, d):
    # Le style du fichier tel qu'il est (indent 1, fins de ligne d'origine) :
    # un diff ne doit montrer que les mots ajoutes.
    fin = "\r\n" if "\r\n" in io.open(chemin, encoding="utf-8", newline="").read() else "\n"
    io.open(chemin, "w", encoding="utf-8", newline="").write(
        (json.dumps(d, ensure_ascii=False, indent=1) + "\n").replace("\n", fin))


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    aj = lire(sys.argv[1])
    temas_chemin = os.path.join(DATOS, "temas.json")
    temas = lire(temas_chemin)
    par_id = {t["id"]: t for t in temas["themes"]}
    allemand = {t["id"]: t for t in lire(os.path.join(RACINE, "themes.json"))["themes"]}

    crees = 0
    for nt in aj.get("themes_nouveaux", []):
        if nt["id"] in par_id:
            continue
        svg = allemand[nt["svg_de"]].get("svg", "")
        t = {"id": nt["id"], "nom_theme": nt["nom_theme"], "nom_theme_es": nt["nom_theme_es"],
             "niveau": nt["niveau"], "svg": svg, "mots": []}
        # Le theme neuf se range apres le dernier theme de son niveau : les
        # listes de l'app suivent l'ordre du fichier.
        rang = max((i for i, x in enumerate(temas["themes"]) if x.get("niveau") == nt["niveau"]),
                   default=len(temas["themes"]) - 1)
        temas["themes"].insert(rang + 1, t)
        par_id[t["id"]] = t
        crees += 1

    ajoutes = 0
    # DEJA PRESENT = n'importe ou dans le corpus, avec le meme sens : un mot
    # deplace ensuite vers un autre theme (vocabulaire_b2.py) ne doit pas
    # revenir dans son theme d'origine a la relance. Le sens departage les
    # homographes voulus (planta : l'etage, et la plante).
    partout = {(m["mot"], m.get("traduction")) for t in temas["themes"] for m in t["mots"]}
    for theme, lignes in aj.get("ajouts", {}).items():
        if theme not in par_id:
            sys.exit("theme inconnu : %s" % theme)
        t = par_id[theme]
        deja = {m["mot"] for m in t["mots"]}
        for mot, art, pl, fr, en, ex, ex_fr, ex_en in lignes:
            if mot in deja or (mot, fr) in partout:
                continue
            e = {"traduction": fr, "traduction_en": en, "exemple": ex, "exemple_fr": ex_fr,
                 "exemple_en": ex_en, "theme_source": theme, "mot": mot, "genre": art}
            if pl:
                e["pluriel"] = pl
            t["mots"].append(e)
            deja.add(mot)
            ajoutes += 1

    var_chemin = os.path.join(DATOS, "variantes.json")
    var = lire(var_chemin)
    poses = 0
    for mot, v in aj.get("variantes", {}).items():
        if mot not in var["noms"]:
            var["noms"][mot] = v
            poses += 1

    # LES EXPRESSIONS ET LES MOTS-OUTILS (10 oct. 2026) : rangees par niveau,
    # avec leur categorie (kategorie). Ligne : [mot, categorie, traduction fr,
    # traduction en, exemple, exemple fr, exemple en]. Un mot deja present a
    # n'importe quel niveau n'est pas rajoute : deplacer un mot de niveau
    # n'est pas le role de ce script.
    autres = 0
    for fichier, source in (("expresiones", "palabras_utiles"), ("funcionales", "gramatica")):
        if fichier not in aj:
            continue
        chemin = os.path.join(DATOS, fichier + ".json")
        d = lire(chemin)
        deja = {x["mot"] for v in d.values() for x in v}
        for niv, lignes in aj[fichier].items():
            for mot, cat, fr, en, ex, ex_fr, ex_en in lignes:
                if mot in deja:
                    continue
                d.setdefault(niv, []).append({"traduction": fr, "traduction_en": en, "exemple": ex,
                                              "exemple_fr": ex_fr, "exemple_en": ex_en,
                                              "theme_source": source, "mot": mot, "kategorie": cat})
                deja.add(mot)
                autres += 1
        ecrire(chemin, d)

    ecrire(temas_chemin, temas)
    ecrire(var_chemin, var)
    print("themes crees : %d   mots ajoutes : %d   variantes posees : %d   expressions et mots-outils : %d"
          % (crees, ajoutes, poses, autres))


if __name__ == "__main__":
    main()
