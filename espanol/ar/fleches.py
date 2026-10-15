# -*- coding: utf-8 -*-
"""Le sens des fleches dans l'arabe de l'espagnol (15 oct. 2026).

    python espanol/ar/fleches.py            # compte ce qui changerait
    python espanol/ar/fleches.py --ecrire   # corrige lots/*.ar.json et les champs _ar de espanol/datos

Le francais ecrit « A → B ». En arabe, de droite a gauche, on ecrit « A ← B » :
la fleche suit le sens de lecture. MAIS l'algorithme bidirectionnel du
navigateur (regle N1) donne a un signe neutre la direction de ses deux voisins
forts quand ils sont pareils : entre deux mots latins, la fleche entre dans le
segment latin, qui s'affiche de gauche a droite -- « la pelota ← la » se lit
alors a l'envers. D'ou la regle, appliquee a chaque fleche :

  - ses deux voisins forts (lettres, balises HTML sautees) sont latins -> « → »
  - sinon (un cote arabe, ou le bord du paragraphe, qui est arabe) -> « ← »
"""
import glob
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
FLECHES = "←→"
BALISE = re.compile(r"<[^>]*>")


def nature(c):
    if "؀" <= c <= "ۿ" or "ݐ" <= c <= "ݿ" or "ﭐ" <= c <= "﷿" or "ﹰ" <= c <= "﻿":
        return "R"
    if c.isalpha():
        return "L"
    return None


def corriger(texte):
    if not isinstance(texte, str) or not any(f in texte for f in FLECHES):
        return texte
    # on remplace les balises par des espaces de meme longueur pour garder les positions
    nu = BALISE.sub(lambda m: " " * len(m.group(0)), texte)
    out = list(texte)
    for i, c in enumerate(nu):
        if c not in FLECHES:
            continue
        avant = next((nature(x) for x in reversed(nu[:i]) if nature(x)), "R")
        apres = next((nature(x) for x in nu[i + 1:] if nature(x)), "R")
        out[i] = "→" if avant == "L" and apres == "L" else "←"
    return "".join(out)


def corriger_objet(o, compte):
    if isinstance(o, dict):
        return {k: corriger_objet(v, compte) for k, v in o.items()}
    if isinstance(o, list):
        return [corriger_objet(v, compte) for v in o]
    n = corriger(o)
    if n != o:
        compte.append((o, n))
    return n


def champs_ar(o, compte):
    """Ne touche que les champs arabes : *_ar, *Ar, et la cle « ar »."""
    if isinstance(o, dict):
        out = {}
        for k, v in o.items():
            if k == "ar" or k.endswith("_ar") or k.endswith("Ar"):
                out[k] = corriger_objet(v, compte)
            else:
                out[k] = champs_ar(v, compte)
        return out
    if isinstance(o, list):
        return [champs_ar(v, compte) for v in o]
    return o


def main():
    ecrire = "--ecrire" in sys.argv
    total = 0
    for chemin in sorted(glob.glob(os.path.join(ICI, "lots", "*.ar.json"))):
        d = json.load(io.open(chemin, encoding="utf-8"))
        compte = []
        d2 = corriger_objet(d, compte)
        total += len(compte)
        print("  %-28s %d" % (os.path.basename(chemin), len(compte)))
        if ecrire and compte:
            io.open(chemin, "w", encoding="utf-8").write(json.dumps(d2, ensure_ascii=False, indent=1) + "\n")
    for chemin in sorted(glob.glob(os.path.join(RACINE, "espanol", "datos", "*.json"))):
        brut = io.open(chemin, encoding="utf-8", newline="").read()
        d = json.loads(brut)
        t = json.dumps(d, ensure_ascii=False, indent=1) + ("\n" if brut.endswith("\n") else "")
        if "\r\n" in brut:
            t = t.replace("\n", "\r\n")
        compte = []
        d2 = champs_ar(d, compte)
        if not compte:
            continue
        if t != brut:
            raise SystemExit(chemin + " ne se reproduit pas a l'identique : rien n'est ecrit")
        total += len(compte)
        print("  %-28s %d" % (os.path.basename(chemin), len(compte)))
        for a, b in compte[:2]:
            print("      ", a[:90], "\n    ->", b[:90])
        if ecrire:
            t2 = json.dumps(d2, ensure_ascii=False, indent=1) + ("\n" if brut.endswith("\n") else "")
            if "\r\n" in brut:
                t2 = t2.replace("\n", "\r\n")
            io.open(chemin, "w", encoding="utf-8", newline="").write(t2)
    print("  %d texte(s) %s" % (total, "corrige(s)" if ecrire else "a corriger"))


if __name__ == "__main__":
    main()
