"""Fabrique pflege/datos/ a partir de pflege/sources/ (Wortando Pflege, la section Soins).

    python pflege/outils/construire.py              ecrit pflege/datos/themes.json
    python pflege/outils/construire.py --verifier   ne touche a rien ; echec si le fichier n'est pas a jour

pflege/datos/ est DERIVE : on corrige les sources, jamais le JSON. Le format est celui de themes.json
(mot, genre, pluriel, traduction, traduction_<langue>, exemple, exemple_<langue>, article_fr), que l'app lit
avec la meme fonction que le corpus (rangsDuMotDeTheme). Les ids sont « soins_<theme>_<niveau> » (pas « pflege_ » : le corpus a deja pflege_betreuung_c1) : l'app
refuse tout autre prefixe (chargerThemesSoins).
"""
import importlib.util
import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]          # pflege/
SOURCES = RACINE / "sources"
SORTIE = RACINE / "datos" / "themes.json"

# Les themes, dans l'ordre ou l'ecran Soins les montre (annexe A du plan).
THEMES = ["vitalzeichen"]

LANGUES = ["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]
NIVEAUX = ["A2", "B1", "B2", "C1"]


def charger(nom):
    spec = importlib.util.spec_from_file_location("source_" + nom, SOURCES / (nom + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def entree_mot(ligne):
    niveau, genre, mot, pluriel, article_fr, trad, exemple_de, relire = ligne
    e = {"mot": mot, "genre": genre, "pluriel": pluriel,
         "traduction": trad["fr"][0], "exemple": exemple_de, "exemple_fr": trad["fr"][1],
         "article_fr": article_fr}
    for l in LANGUES[1:]:
        e["traduction_" + l] = trad[l][0]
        e["exemple_" + l] = trad[l][1]
    if relire:
        e["relire"] = relire
    return niveau, e


def construire():
    themes = []
    for nom in THEMES:
        src = charger(nom)
        par_niveau = {}
        for ligne in src.MOTS:
            niveau, e = entree_mot(ligne)
            par_niveau.setdefault(niveau, []).append(e)
        for niveau in NIVEAUX:
            if niveau not in par_niveau:
                continue
            themes.append({
                "id": src.THEME["base"] + "_" + niveau.lower(),
                "nom_theme": src.THEME["nom_theme"],
                "nom_theme_fr": src.THEME["nom_theme_fr"],
                "niveau": niveau,
                "svg": src.THEME["svg"],
                "mots": par_niveau[niveau],
            })
    return {
        "_note": "DERIVE de pflege/sources/ par pflege/outils/construire.py : ne pas corriger a la main. "
                 "Wortando Pflege, la section Soins (essai « soins »). Controle : python tests/pflege.py.",
        "themes": themes,
    }


def texte(donnees):
    return json.dumps(donnees, ensure_ascii=False, indent=1) + "\n"


def main():
    attendu = texte(construire())
    if "--verifier" in sys.argv:
        actuel = SORTIE.read_text(encoding="utf-8") if SORTIE.exists() else ""
        if actuel != attendu:
            print("pflege/datos/themes.json n'est pas a jour : python pflege/outils/construire.py")
            return 1
        print("pflege/datos/themes.json a jour")
        return 0
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(attendu, encoding="utf-8", newline="\n")
    n = sum(len(t["mots"]) for t in json.loads(attendu)["themes"])
    print("ecrit", SORTIE.relative_to(RACINE.parent), ":", n, "mots")
    return 0


if __name__ == "__main__":
    sys.exit(main())
