# -*- coding: utf-8 -*-
"""Extrait les cles d'interface d'index.html pour preparer une nouvelle langue.

Reprend les bornes de bloc de verifier.py -- `const I18N = {` puis `  <code>: {`
-- pour compter exactement comme lui. Sans ca on croit avoir fini avec dix cles
de moins que le controle qui juge.

    python tests/cles_langue.py --langue fa            ce qui manque
    python tests/cles_langue.py --langue fa --tout     toutes les cles
    python tests/cles_langue.py --langue fa --lot 1 --taille 150
"""
import argparse, io, json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(RACINE, "index.html")

def blocs():
    """{code: {cle: texte}} pour chaque langue du bloc I18N."""
    s = io.open(INDEX, encoding="utf-8").read()
    d = s.index("const I18N = {")
    # La fermeture du bloc : la premiere ligne "};" en debut de ligne apres d.
    f = s.index("\n};", d)
    corps = s[d:f]
    out, courant = {}, None
    for ligne in corps.split("\n"):
        m = re.match(r"^    ([a-z]{2}): \{\s*$", ligne)
        if m:
            courant = m.group(1); out[courant] = {}
            continue
        if courant is None: continue
        m = re.match(r'^\s{8}([A-Za-z0-9_]+):\s*(.*?),?\s*$', ligne)
        if m and (m.group(2)[:1] in '"\'`'):
            out[courant][m.group(1)] = m.group(2)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langue", required=True)
    ap.add_argument("--tout", action="store_true")
    ap.add_argument("--lot", type=int)
    ap.add_argument("--taille", type=int, default=150)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    b = blocs()
    if "fr" not in b: sys.exit("bloc fr introuvable")
    cible = b.get(a.langue, {})
    cles = [k for k in b["fr"] if a.tout or k not in cible]

    if a.lot:
        deb = (a.lot - 1) * a.taille
        cles = cles[deb:deb + a.taille]

    if a.json:
        io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False).write(
            json.dumps([{"cle": k, "fr": b["fr"][k], "en": b.get("en", {}).get(k, "")}
                        for k in cles], ensure_ascii=False, indent=1))
        return

    print("langues : " + ", ".join("%s=%d" % (c, len(v)) for c, v in b.items()))
    print("%s : %d cles sur %d ; il en manque %d\n"
          % (a.langue, len(cible), len(b["fr"]), len(b["fr"]) - len(cible)))
    for k in cles:
        print("%-38s %s" % (k, b["fr"][k][:110]))

if __name__ == "__main__":
    main()
