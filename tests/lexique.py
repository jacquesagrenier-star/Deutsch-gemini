# -*- coding: utf-8 -*-
"""Verifie qu'un episode n'enseigne aucun mot que l'app ignore.

    python tests/lexique.py                       # toutes les scenes
    python tests/lexique.py --scene 01-ankunft-berlin

POURQUOI CE CONTROLE EXISTE
    Un mot rencontre une seule fois dans une video ne s'apprend pas. Ce sont
    les cartes qui l'installent ; la video lui donne une situation ou il
    compte. Un mot du lexique d'un episode qui n'est nulle part dans le
    vocabulaire est donc du decor : joli, et sans effet.

    REGLE : on ne publie pas un episode sans avoir livre son lexique.

POURQUOI IL EST ECRIT PLUTOT QUE FAIT A LA MAIN
    Le 8 septembre 2026, la meme verification a ete faite trois fois de suite
    a la main, avec trois resultats differents -- 10/26, puis 22/26, puis
    26/26. Deux causes, et elles se reproduiront :

      1. LES ARTICLES. Le lexique dit << Koffern >>, l'app dit << der Koffer >>.
         Comparer sans reduire les deux formes rejette des mots bel et bien
         presents.
      2. LES FICHIERS OUBLIES. Le vocabulaire vit dans HUIT fichiers, pas
         trois. draussen n'etait pas absent : il etait dans adverbe.json, que
         personne n'avait pense a ouvrir.

    Une conclusion tiree de trois fichiers sur huit est une conclusion fausse
    qui a l'air d'une mesure.
"""
import argparse
import glob
import io
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Les huit fichiers ou vit le vocabulaire allemand. En ajouter un ici le jour
# ou un neuvième apparait -- c'est le seul endroit a tenir a jour.
FICHIERS = ("themes.json", "verbe.json", "adjectif.json", "adverbe.json",
            "funktionswort.json", "redewendung.json", "synonymes.json",
            "pruefung.json")

# Les cles sous lesquelles un mot-vedette peut se presenter selon le fichier.
CLES = ("mot", "infinitif", "ausdruck", "wort")


def nu(s):
    """Reduit une forme a sa base comparable : minuscules, sans article, sans
    ce qui suit une virgule ou une parenthese."""
    s = s.strip().lower()
    s = re.sub(r"^(der|die|das)\s+", "", s)
    return re.split(r"[,(/]", s)[0].strip()


def vedettes():
    mots = []

    def w(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in CLES and isinstance(v, str):
                    mots.append(v)
                else:
                    w(v)
        elif isinstance(x, list):
            for v in x:
                w(v)

    manquants = []
    for f in FICHIERS:
        p = os.path.join(RACINE, f)
        if not os.path.exists(p):
            manquants.append(f)
            continue
        w(json.load(io.open(p, encoding="utf-8")))
    if manquants:
        print("  ATTENTION, fichiers absents : %s" % ", ".join(manquants))
    return mots


def controle(scene, base):
    p = os.path.join(RACINE, "scenes", scene + ".json")
    d = json.load(io.open(p, encoding="utf-8"))
    lex = d.get("lexique") or {}
    if not lex:
        print("  %-24s pas de lexique" % scene)
        return 0
    absents = []
    for cle, v in lex.items():
        lemme = nu(v.get("lemme") or cle)
        # Le lexique cite parfois la forme flechie : Koffern, Automaten, dauert.
        formes = [lemme]
        if lemme.endswith("en"):
            formes.append(lemme[:-2])
        if lemme.endswith("n"):
            formes.append(lemme[:-1])
        if lemme.endswith("t"):
            formes.append(lemme[:-1] + "en")
        if not any(f in base for f in formes):
            absents.append((cle, v.get("fr", "")))
    n = len(lex)
    if absents:
        print("  %-24s %d/%d  -- %d A LIVRER :" % (scene, n - len(absents), n, len(absents)))
        for cle, fr in absents:
            print("       %-22s %s" % (cle, fr))
    else:
        print("  %-24s %d/%d  tout le lexique est dans l'app" % (scene, n, n))
    return len(absents)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene")
    a = ap.parse_args()
    mots = vedettes()
    base = {nu(m) for m in mots}
    print("  %d mots-vedettes dans %d fichiers, %d formes comparables\n"
          % (len(mots), len(FICHIERS), len(base)))

    scenes = ([a.scene] if a.scene else
              sorted(os.path.basename(f)[:-5]
                     for f in glob.glob(os.path.join(RACINE, "scenes", "*.json"))
                     if not os.path.basename(f).startswith("personnages")))
    if not scenes:
        sys.exit("  Aucune scene trouvee.")
    total = sum(controle(s, base) for s in scenes)
    print()
    if total:
        sys.exit("  %d mot(s) a ajouter au vocabulaire avant publication." % total)
    print("  OK.")


if __name__ == "__main__":
    main()
