# -*- coding: utf-8 -*-
"""Controle des reperes (v879) : reperes.json et espanol/datos/reperes.json.

- les cinq blocs, dans l'ordre (n0-20, n20-100, n100-1000, jours, mois) ;
- chaque titre, astuce et sens de jour ou de mois dans les 9 langues ;
- le sens d'un nombre = des chiffres, croissants dans le tableau, de 0 a 1000 ;
- chaque suite a dire (p) faite de mots du tableau, dans l'ordre ;
- le fichier est bien celui que construit tests/reperes_construire.py.

    python tests/reperes.py
"""
import io, json, os, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "tests"))
import reperes_construire as rc

ORDRE = {"de": ["n0-20", "n20-100", "n100-1000", "jours", "mois", "alphabet", "genre-die", "genre-der", "genre-das", "pluriel"],
         "es": ["n0-20", "n20-100", "n100-1000", "jours", "mois", "alphabet", "genre-m", "genre-f", "pluriel"]}
erreurs = []

def verifier(chemin, langue):
    d = json.load(io.open(os.path.join(RACINE, chemin), encoding="utf-8"))
    if d != json.loads(json.dumps(rc.construire(langue), ensure_ascii=False)):
        erreurs.append("%s : differe de ce que construit tests/reperes_construire.py (relancer le constructeur)" % chemin)
    R = d.get("reperes", [])
    if [r.get("id") for r in R] != ORDRE[langue]:
        erreurs.append("%s : blocs %r au lieu de %r" % (chemin, [r.get("id") for r in R], ORDRE[langue]))
    for r in R:
        ou = "%s [%s]" % (chemin, r.get("id"))
        for champ in ("t", "a"):
            manque = [lg for lg in rc.LANGUES if not (r.get(champ) or {}).get(lg)]
            if manque:
                erreurs.append("%s : %s sans %s" % (ou, champ, ",".join(manque)))
        if r["type"] == "nombre":
            valeurs = []
            for l in r["l"] + r.get("x", []):
                if not (isinstance(l[1], str) and l[1].isdigit()):
                    erreurs.append("%s : %r n'a pas de sens en chiffres" % (ou, l))
                elif not 0 <= int(l[1]) <= 1000:
                    erreurs.append("%s : %r hors de 0-1000" % (ou, l))
            valeurs = [int(l[1]) for l in r["l"] if l[1].isdigit()]
            if valeurs != sorted(valeurs):
                erreurs.append("%s : le tableau n'est pas dans l'ordre croissant" % ou)
        elif r["type"] == "lettre":
            lettres = [l[1] for l in r["l"]]
            for l in r["l"]:
                if len(l) < 3 or len(l[2]) < 2 or any(c not in lettres or c == l[1] for c in l[2]):
                    erreurs.append("%s : %r -- il faut deux autres lettres de l'alphabet qui se confondent" % (ou, l))
            for s in r.get("p", []):
                if not s[1] or len(s[0].split(", ")) != len(s[1]):
                    erreurs.append("%s : l'epellation %r ne compte pas une lettre par lettre de %r" % (ou, s[0], s[1]))
        elif r["type"] == "genre":
            arts = ("der", "die", "das") if langue == "de" else ("el", "la")
            for l in r["l"] + r.get("x", []):
                if l[0].split(" ")[0] not in arts or "→" not in l[1]:
                    erreurs.append("%s : %r -- article ou regle illisible" % (ou, l))
        elif r["type"] == "pluriel":
            for x in r.get("x", []):
                if len(x) != 5 or len(set(x[1:2] + x[3:5])) != 3:
                    erreurs.append("%s : %r -- il faut le pluriel et deux leurres differents" % (ou, x))
        else:
            for l in r["l"]:
                manque = [lg for lg in rc.LANGUES if not (l[1] or {}).get(lg)]
                if manque:
                    erreurs.append("%s : %s sans %s" % (ou, l[0], ",".join(manque)))
            mots = [l[0] for l in r["l"]]
            for s in r.get("p", []):
                parts = s[0].split(", ")
                if any(m not in mots for m in parts):
                    erreurs.append("%s : la suite %r a un mot hors du tableau" % (ou, s[0]))
                elif [mots.index(m) for m in parts] != list(range(mots.index(parts[0]), mots.index(parts[0]) + len(parts))):
                    erreurs.append("%s : la suite %r n'est pas dans l'ordre" % (ou, s[0]))
    return R

de = verifier("reperes.json", "de")
es = verifier(os.path.join("espanol", "datos", "reperes.json"), "es")
if erreurs:
    print("\n".join(erreurs))
    sys.exit(1)
print("OK : reperes allemands (%d blocs) et espagnols (%d blocs)." % (len(de), len(es)))
