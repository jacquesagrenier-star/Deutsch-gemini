# -*- coding: utf-8 -*-
"""Lit et ecrit les dictionnaires d'interface de index.html.

    python tests/dico_interface.py --extraire uk sortie.json
    python tests/dico_interface.py --poser   uk lot.json
    python tests/dico_interface.py --etat    uk

POURQUOI PASSER PAR NODE. Les trois blocs `fr:`, `en:`, `tr:` sont du
JavaScript, pas du JSON : gabarits entre accents graves, apostrophes
echappees, concatenations, commentaires. Une expression reguliere qui pretend
les lire se trompe des la premiere chaine contenant une accolade. On les fait
donc evaluer par le seul moteur qui les comprend.

CE QUE --extraire PRODUIT : les cles ENCORE ABSENTES de la langue visee, avec
leur francais et leur anglais cote a cote. C'est la liste de travail, et elle
retrecit a chaque lot pose -- on ne retraduit jamais deux fois la meme cle.

CE QUE --poser REFUSE :
  - une cle inconnue des trois dictionnaires (faute de frappe : elle
    s'afficherait comme cle brute, jamais comme texte) ;
  - une valeur identique au francais ou a l'anglais (copie non traduite) ;
  - une valeur vide.
Le repli uk -> en -> fr rend ces trois defauts INVISIBLES a l'usage : la page
affiche quelque chose de lisible, simplement pas de l'ukrainien.
"""
import io
import json
import os
import re
import subprocess
import sys
import tempfile

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(RACINE, "index.html")


def bloc(html, nom):
    """Les bornes du dictionnaire `nom:` -- en comptant les accolades, car une
    expression reguliere ne sait pas ou une chaine se termine."""
    m = re.search(r"\n    " + nom + r": \{", html)
    if not m:
        return None
    i = m.end() - 1
    prof, j, dans_texte, delim, echap = 0, i, False, "", False
    while j < len(html):
        c = html[j]
        if dans_texte:
            if echap:
                echap = False
            elif c == "\\":
                echap = True
            elif c == delim:
                dans_texte = False
        else:
            if c in "\"'`":
                dans_texte, delim = True, c
            elif c == "{":
                prof += 1
            elif c == "}":
                prof -= 1
                if prof == 0:
                    return i, j + 1
        j += 1
    return None


def lire(codes):
    html = io.open(SRC, encoding="utf-8").read()
    script = "const out = {};\n"
    for c in codes:
        b = bloc(html, c)
        if not b:
            script += "out['%s'] = {};\n" % c
        else:
            script += "out['%s'] = %s;\n" % (c, html[b[0]:b[1]])
    script += "console.log(JSON.stringify(out));\n"
    f = tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8")
    f.write(script)
    f.close()
    res = subprocess.run(["node", f.name], capture_output=True, text=True,
                         encoding="utf-8")
    os.unlink(f.name)
    if res.returncode != 0:
        raise SystemExit("node a refuse les blocs :\n" + res.stderr[:2000])
    return json.loads(res.stdout)


def echapper(v):
    """Une chaine JS entre guillemets doubles, sur une seule ligne."""
    return (v.replace("\\", "\\\\").replace('"', '\\"')
             .replace("\n", "\\n").replace("\r", ""))


def poser(code, lot):
    html = io.open(SRC, encoding="utf-8").read()
    b = bloc(html, code)
    if not b:
        raise SystemExit("le bloc %s: n'existe pas encore dans index.html" % code)
    dicos = lire(["fr", "en", code])
    connues, deja = set(dicos["fr"]), dicos[code]

    lignes, refus = [], 0
    for cle, v in sorted(lot.items()):
        if cle not in connues:
            print("  ! %s : cle inconnue du dictionnaire francais" % cle); refus += 1; continue
        if not str(v).strip():
            print("  ! %s : valeur vide" % cle); refus += 1; continue
        if str(v).strip() == str(dicos["fr"].get(cle, "")).strip():
            print("  ! %s : identique au francais" % cle); refus += 1; continue
        if str(v).strip() == str(dicos["en"].get(cle, "")).strip():
            print("  ! %s : identique a l'anglais" % cle); refus += 1; continue
        if cle in deja:
            print("  ! %s : deja posee" % cle); refus += 1; continue
        lignes.append('        %s: "%s",' % (cle, echapper(v)))

    if lignes:
        # On insere juste avant l'accolade fermante du bloc. La derniere entree
        # existante peut ne pas avoir de virgule : on en ajoute une si besoin.
        interieur = html[b[0]:b[1]]
        avant = interieur[:-1].rstrip()
        if not avant.endswith(",") and not avant.endswith("{"):
            avant += ","
        neuf = avant + "\n" + "\n".join(lignes) + "\n    }"
        html = html[:b[0]] + neuf + html[b[1]:]
        io.open(SRC, "w", encoding="utf-8").write(html)

    print("  %d posees, %d refusees" % (len(lignes), refus))
    return refus


def etat(code):
    d = lire(["fr", "en", code])
    total, faites = len(d["fr"]), len(d[code])
    print("  %s : %d cles sur %d (%.1f %%), %d restantes"
          % (code, faites, total, 100.0 * faites / total, total - faites))
    return d


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return 1
    if a[0] == "--etat":
        etat(a[1]); return 0
    if a[0] == "--extraire":
        code, dest = a[1], a[2]
        d = lire(["fr", "en", code])
        restant = {k: {"fr": d["fr"][k], "en": d["en"].get(k, "")}
                   for k in d["fr"] if k not in d[code]}
        io.open(dest, "w", encoding="utf-8").write(
            json.dumps(restant, ensure_ascii=False, indent=1))
        print("  %d cles restantes ecrites dans %s" % (len(restant), dest))
        return 0
    if a[0] == "--poser":
        lot = json.load(io.open(a[2], encoding="utf-8"))
        r = poser(a[1], lot)
        etat(a[1])
        return 1 if r else 0
    print(__doc__); return 1


if __name__ == "__main__":
    sys.exit(main())
