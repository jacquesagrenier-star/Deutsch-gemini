# -*- coding: utf-8 -*-
"""Les bonnes reponses traduites absentes de « answers » (3 nov. 2026).

L'ecran d'exercices affiche options<Langue> (valeurTraduite) mais juge le
choix contre ex.answers seul : quand answers ne porte que fr / en / tr, la
bonne option affichee en uk, fa, pt, ar, pl, ru (ou de, pour l'espagnol) est
comptee fausse. On ajoute a answers chaque correct<Langue> qui y manque,
partout ou options<Langue> existe. Comparaison sans casse, comme l'app.

    python retours/qualite-es-de/reponses_traduites.py             # compte
    python retours/qualite-es-de/reponses_traduites.py --ecrire    # corrige
    python retours/qualite-es-de/reponses_traduites.py --controle  # chaque option juste affichee est acceptee
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
FICHIERS = ["exercices.json", "espanol/datos/ejercicios.json",
            "anglais/datos/exercices.json", "portugais/datos/exercices.json"]


def format_de(raw, d):
    for ind in (None, 1, 2, 4):
        for sep in ((",", ": "), (", ", ": "), (",", ":")):
            s = json.dumps(d, ensure_ascii=False, indent=ind, separators=sep)
            for fin in ("", "\n"):
                if s + fin == raw:
                    return ind, sep, fin
    raise SystemExit("format inconnu")


def langues(e):
    """(suffixe, options, correct) de chaque langue traduite de l'exercice."""
    for k, v in e.items():
        if k.startswith("options") and k != "options" and isinstance(v, list):
            L = k[len("options"):]
            yield L, v, e.get("correct" + L)


def main():
    ecrire, controle = "--ecrire" in sys.argv, "--controle" in sys.argv
    total_err = 0
    for rel in FICHIERS:
        chemin = os.path.join(RACINE, rel)
        if not os.path.exists(chemin):
            continue
        raw = io.open(chemin, encoding="utf-8", newline="").read().replace("\r\n", "\n")
        d = json.loads(raw)
        fmt = format_de(raw, d) if ecrire else None   # avant toute modification
        jeux = d.get("jeux", d)
        ajouts, exos, erreurs = 0, set(), []
        for fam, liste in jeux.items():
            if not isinstance(liste, list):
                continue
            for i, e in enumerate(liste):
                if not isinstance(e, dict) or not isinstance(e.get("answers"), list):
                    continue
                vus = {str(a).lower() for a in e["answers"]}
                for L, opts, c in langues(e):
                    if not c:
                        continue
                    if controle:
                        # l'option que l'ecran montre comme juste doit etre acceptee
                        if c not in opts:
                            erreurs.append("%s %s[%d] %s : correct%s absent de options%s" % (rel, fam, i, c, L, L))
                        if str(c).lower() not in vus:
                            erreurs.append("%s %s[%d] : correct%s « %s » refuse" % (rel, fam, i, L, c))
                    elif str(c).lower() not in vus:
                        e["answers"].append(c)
                        vus.add(str(c).lower())
                        ajouts += 1
                        exos.add((fam, i))
        if controle:
            print("%-34s %d defaut(s)" % (rel, len(erreurs)))
            for x in erreurs[:10]:
                print("   ", x)
            total_err += len(erreurs)
            continue
        print("%-34s %d reponse(s) ajoutee(s) dans %d exercice(s) : %s"
              % (rel, ajouts, len(exos), ", ".join(sorted({f for f, _ in exos}))))
        if ecrire and ajouts:
            ind, sep, fin = fmt
            io.open(chemin, "w", encoding="utf-8", newline="\n").write(
                json.dumps(d, ensure_ascii=False, indent=ind, separators=sep) + fin)
    if controle:
        sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
