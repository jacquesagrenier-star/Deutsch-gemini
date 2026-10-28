# -*- coding: utf-8 -*-
"""Verse dans les listes A2-C1 les mots allemands encore absents de l'anglais.

    python anglais/outils/ajouter_manques.py B1 ecartes.txt [--ecrire]

OUTIL DE TRAVAIL (28 oct. 2026, consigne de Jacques « tous les mots »). Il part
de manques_allemand.py (cumule), propose pour chaque mot absent une ligne au
format de noms_<niv>.py / mots_<niv>.py (tete anglaise, traduction francaise du
mot allemand, theme anglais), et l'ajoute a la fin du bon bloc avec --ecrire.
Sans --ecrire, il affiche seulement les lignes : c'est la relecture.

ecartes.txt : une tete anglaise par ligne, « tete # raison » ; ces mots ne sont
pas ajoutes (la raison va dans la liste justifiee de PLAN-A2-C1.md). Une ligne
« tete => remplacement » corrige la tete (« drinks menu => drink menu »).
La phrase d'exemple est choisie a la construction (construire.py), et c'est
d'abord celle du mot allemand lui-meme.
"""
import io, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import couverture as C
import manques_allemand as M
import extraire_niveaux as X

CLASSE = {"noms": "nom", "verbes": "verbe", "adjectifs": "adj", "adverbes": "adv", "expressions": "expr"}
BLOC = {"verbes": "VERBES", "adjectifs": "ADJECTIFS", "adverbes": "ADVERBES", "expressions": "EXPRESSIONS"}
CAT_ADV = dict(X.CAT_ADV)
CAT_EXPR = dict(X.CAT_EXPR)


def lire_ecartes(p):
    ecartes, remplace = {}, {}
    for l in io.open(p, encoding="utf-8").read().splitlines():
        l = l.strip()
        if not l or l.startswith("//"):
            continue
        if "=>" in l:
            a, b = l.split("=>", 1)
            remplace[a.strip().lower()] = b.strip()
        else:
            a, _, raison = l.partition("#")
            ecartes[a.strip().lower()] = raison.strip()
    return ecartes, remplace


def themes_du_niveau(niv):
    import importlib
    src = importlib.import_module("noms_" + niv.lower())
    return [t[0] for t in src.THEMES]


def theme_pour(niv, e, themes):
    """Le theme allemand de l'entree -> notre theme anglais du niveau."""
    for t in C.lire("themes.json")["themes"]:
        if t["niveau"].upper() == niv and any(m is e or (m.get("mot") == e.get("mot") and m.get("traduction") == e.get("traduction")) for m in t["mots"]):
            cle = X.theme_anglais(t["id"])
            cands = [x for x in themes if x == "%s_%s" % (cle, niv.lower()) or x.startswith("%s_%s_" % (cle, niv.lower()))]
            if cands:
                return cands[-1]
    cands = [x for x in themes if x.startswith("everyday_")]
    return cands[-1] if cands else themes[-1]


def lignes(niv, ecartes, remplace):
    res = M.manques()
    out = {}
    vus = set()
    themes = themes_du_niveau(niv)
    for cat in M.CATS:
        for e in res[(niv, cat)][1]:
            tete = C.tetes(e.get("traduction_en"))[0]
            if tete in ecartes or tete in vus:
                continue
            vus.add(tete)
            mot = remplace.get(tete, tete)
            if cat == "noms":
                us, gb = X.vers_americain(mot)
                d = {"mot": us, "gb": gb}
                drap = X.drapeaux_nom(d)
                ligne = " | ".join([us, M.francais(e)] + drap)
                out.setdefault(theme_pour(niv, e, themes), []).append(ligne)
            elif cat == "verbes":
                out.setdefault("VERBES", []).append("%s | %s" % (mot, M.francais(e)))
            elif cat == "adjectifs":
                us, gb = X.vers_americain(mot)
                out.setdefault("ADJECTIFS", []).append("%s | %s%s" % (us, M.francais(e), (" | gb=" + gb) if gb else ""))
            elif cat == "adverbes":
                out.setdefault("ADVERBES", []).append("%s | %s | %s" % (mot, M.francais(e), CAT_ADV.get(e.get("kategorie"), "Manière")))
            else:
                en, fr = (e.get("exemple_en") or "").strip(), (e.get("exemple_fr") or "").strip()
                if not (en and fr):
                    continue
                out.setdefault("EXPRESSIONS", []).append("%s | %s | %s | %s | %s" % (
                    mot, M.francais(e), CAT_EXPR.get(e.get("kategorie"), "Tournures"), en.replace("|", "/"), fr.replace("|", "/")))
    return out


def ecrire(niv, out):
    for fichier, blocs in (("noms_%s.py" % niv.lower(), [b for b in out if b not in BLOC.values()]),
                           ("mots_%s.py" % niv.lower(), [b for b in out if b in BLOC.values()])):
        p = os.path.join(ICI, fichier)
        texte = io.open(p, encoding="utf-8").read()
        for b in blocs:
            m = re.search(r'(?:"%s": """|%s = """)\n(.*?)\n"""' % (re.escape(b), re.escape(b)), texte, re.S)
            if not m:
                raise SystemExit("bloc introuvable : %s dans %s" % (b, fichier))
            texte = texte[:m.end(1)] + "\n" + "\n".join(out[b]) + texte[m.end(1):]
        io.open(p, "w", encoding="utf-8", newline="\n").write(texte)


def main():
    niv, p = sys.argv[1].upper(), sys.argv[2]
    ecartes, remplace = lire_ecartes(p)
    out = lignes(niv, ecartes, remplace)
    n = sum(len(v) for v in out.values())
    if "--ecrire" in sys.argv:
        ecrire(niv, out)
        print("%s : %d lignes ajoutees." % (niv, n))
    else:
        for b, ls in out.items():
            print("## " + b)
            for l in ls:
                print("   " + l)
        print("%d lignes" % n)


if __name__ == "__main__":
    main()
