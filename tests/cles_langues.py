# -*- coding: utf-8 -*-
"""Chaque cle d'interface existe-t-elle dans LES CINQ langues ?

    python tests/cles_langues.py

⚠️ POURQUOI CE CONTROLE EXISTE A COTE DE verifier.py
    Le verificateur compare le francais et l'anglais. Les trois autres langues
    -- turc, ukrainien, persan -- ont ete ajoutees plus tard, et rien ne dit
    qu'une cle posee aujourd'hui en francais et en anglais y arrive aussi. Une
    cle manquante ne casse rien : t() renvoie la cle elle-meme, et l'ecran
    affiche « compte_rencontres » a un lecteur ukrainien. Un defaut muet, donc,
    et exactement le genre que ce depot cherche a rendre bruyant.
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGUES = ["fr", "en", "tr", "uk", "fa"]


def blocs(s):
    """Le texte de chaque dictionnaire de langue, du marqueur au suivant."""
    out, bornes = {}, []
    for lg in LANGUES:
        m = re.search(r"^    %s: \{$" % lg, s, re.M)
        if not m:
            sys.exit("  Bloc de langue introuvable : %s" % lg)
        bornes.append((m.start(), lg))
    bornes.sort()
    # ⚠️ LE DERNIER BLOC NE VA PAS JUSQU'A LA FIN DU FICHIER. Une premiere
    # version le laissait courir, et il ramassait les clefs du code qui suit --
    # `answers`, `correct`, `explanation`... -- ce qui faisait croire a 135
    # traductions manquantes dans les quatre autres langues. Le dictionnaire se
    # ferme sur `};` en debut de ligne.
    fin_dico = s.index("\n};", bornes[-1][0]) + 1
    for i, (d, lg) in enumerate(bornes):
        f = bornes[i + 1][0] if i + 1 < len(bornes) else fin_dico
        out[lg] = s[d:f]
    return out


def cles(bloc):
    # Les cles d'un niveau : « nom: » a huit espaces d'indentation. Les objets
    # imbriques sont plus indentes, donc ignores.
    #
    # ⚠️ ET PARFOIS DEUX CLES SUR UNE LIGNE : `op_verben_o4_t: "...",
    # op_verben_o4_d: "..."`. Ne lire que la premiere faisait apparaitre
    # quatre-vingt-dix traductions manquantes qui existaient toutes -- un
    # defaut de l'analyseur presente comme un defaut des donnees, ce qui est
    # pire que pas de controle du tout.
    return set(re.findall(r"(?:^        |, )([A-Za-z_][A-Za-z0-9_]*):",
                          bloc, re.M))


def main():
    s = io.open(os.path.join(RACINE, "index.html"), encoding="utf-8").read()
    b = blocs(s)
    par_langue = {lg: cles(b[lg]) for lg in LANGUES}
    toutes = set()
    for lg in LANGUES:
        toutes |= par_langue[lg]

    print("\n  %-6s %8s %10s" % ("langue", "cles", "manquantes"))
    print("  " + "-" * 30)
    manque = {}
    for lg in LANGUES:
        absent = sorted(toutes - par_langue[lg])
        manque[lg] = absent
        print("  %-6s %8d %10d" % (lg, len(par_langue[lg]), len(absent)))

    total = sum(len(v) for v in manque.values())
    if not total:
        print("\n  Les %d cles existent dans les cinq langues.\n" % len(toutes))
        return 0

    print("\n  CE QUI MANQUE\n")
    for lg in LANGUES:
        if not manque[lg]:
            continue
        print("  %s (%d) :" % (lg, len(manque[lg])))
        for c in manque[lg]:
            # La ou elle existe deja, pour savoir quoi traduire.
            ou = [x for x in LANGUES if c in par_langue[x]]
            print("      %-34s presente en : %s" % (c, ", ".join(ou)))
        print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
