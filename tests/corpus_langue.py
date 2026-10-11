# -*- coding: utf-8 -*-
"""Traduire le corpus dans une langue d'interface : sortir ce qui manque, poser un lot.

    python tests/corpus_langue.py --langue pt etat
    python tests/corpus_langue.py --langue pt reste themes.json A1 60
    python tests/corpus_langue.py --langue pt pose lot.json

NE EN v765 POUR LE PORTUGAIS DU BRESIL, sur le modele de l'outil ukrainien
(uk_outils.py, reste dans un scratchpad) : un parcours deterministe des six
fichiers sert de NUMEROTATION, et chaque carte se pose par son numero.

POURQUOI UN NUMERO ET PAS LE MOT. patch_langue.py pose par le mot allemand, et
corrige « toutes ses occurrences » : c'est juste pour reparer une perte, faux
pour un premier passage. « die Bank » est un banc dans un theme et une banque
dans un autre ; « der Leiter » un chef, « die Leiter » une echelle. Le numero
laisse chaque carte recevoir le sens de SON theme -- et `reste` affiche le
theme pour que la traduction le voie.

LES TROIS GARDE-FOUS, dans l'ordre :
  1. le premier element de chaque ligne du lot est le mot allemand du fichier
     a ce numero ; s'il differe, RIEN n'est ecrit (un decalage d'un rang colle
     des traductions sur les mauvais mots, en silence) ;
  2. avant d'ecrire, le fichier doit se reproduire a l'octet pres une fois
     relu et reserialise (sinon le diff part en reformatage et la vraie
     modification s'y perd) ;
  3. apres l'ecriture, on relit le fichier depuis le disque et on compare
     chaque champ pose a ce qui etait demande.

FORME D'UN LOT

    {"fichier": "themes.json",
     "e": {"12": ["Vater", "pai", "Meu pai trabalha muito."],
           "13": ["Mutter", "mãe", "Minha mãe ..."]}}

Les valeurs suivent l'ordre de `CHAMPS` pour le fichier : un verbe porte
traduction, exemple, perfekt, praeteritum, konjunktiv2 ; un mot-outil
traduction, exemple, kategorie. `reste` les montre dans ce meme ordre.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
FICHIERS = ["themes.json", "verbe.json", "adjectif.json", "adverbe.json",
            "redewendung.json", "funktionswort.json"]
TEMPS = ["perfekt", "praeteritum", "konjunktiv2"]


def charger(nom):
    chemin = os.path.join(RACINE, nom)
    brut = io.open(chemin, encoding="utf-8", newline="").read()
    return json.loads(brut), brut


def serialiser(donnees, saut_final, crlf=False):
    # themes.json est en fins de ligne Windows (ajouter_mots.py les garde) ;
    # les cinq autres en fins Unix. On reprend la convention du fichier.
    t = json.dumps(donnees, ensure_ascii=False, indent=2)
    t = t + "\n" if saut_final else t
    return t.replace("\n", "\r\n") if crlf else t


def cases(nom, donnees):
    """Toutes les entrees du fichier, dans un ordre fixe : (niveau, contexte, entree)."""
    out = []
    if nom == "themes.json":
        for t in donnees["themes"]:
            for liste in ("mots", "adjektive", "verben"):
                for m in t.get(liste, []):
                    out.append((t.get("niveau"), t.get("nom_theme") or t.get("id"), m))
    elif nom == "funktionswort.json":
        for cat, entrees in donnees.items():
            if isinstance(entrees, list):
                for m in entrees:
                    out.append((m.get("niveau"), cat, m))
    else:
        for niv in NIVEAUX:
            for m in donnees.get(niv, []):
                out.append((niv, "", m))
    return out


def cle(m):
    return m.get("mot") or m.get("infinitif") or ""


def champs(m):
    """Les champs a traduire de CETTE entree, dans l'ordre du lot."""
    c = ["traduction", "exemple"]
    if "infinitif" in m:
        c += [x for x in TEMPS if (m.get(x) or "").strip()]
    if (m.get("kategorie") or "").strip() and "kategorie_en" in m:
        c.append("kategorie")
    return c


def manque(m, lang):
    return [c for c in champs(m) if not (m.get("%s_%s" % (c, lang)) or "").strip()
            and (c != "exemple" or (m.get("exemple") or "").strip())]


def etat(lang):
    total = faits = 0
    for nom in FICHIERS:
        d, _ = charger(nom)
        par = {}
        for niv, _, m in cases(nom, d):
            a = par.setdefault(niv, [0, 0])
            a[0] += 1
            if not manque(m, lang):
                a[1] += 1
        for niv in sorted(par):
            n, f = par[niv]
            total += n
            faits += f
            print("  %-18s %-3s %5d / %5d" % (nom, niv, f, n))
    print("  ---\n  %s : %d / %d cartes completes (%.1f %%)" % (lang, faits, total, 100.0 * faits / max(total, 1)))


def reste(lang, nom, niveau, n):
    d, _ = charger(nom)
    vus = 0
    for i, (niv, ctx, m) in enumerate(cases(nom, d)):
        if niveau != "*" and niv != niveau:
            continue
        if not manque(m, lang):
            continue
        g = (m.get("genre") or "")
        ligne = "#%d %s%s [%s%s] fr=%s | en=%s" % (
            i, (g + " ") if g else "", cle(m), niv, (" " + ctx) if ctx else "",
            m.get("traduction", ""), m.get("traduction_en", ""))
        for c in champs(m)[1:]:
            if c == "kategorie":
                ligne += "\n    kat: %s" % m.get("kategorie", "")
            else:
                ligne += "\n    %s: %s" % (c[:4], m.get(c, ""))
        print(ligne)
        vus += 1
        if vus >= n:
            break
    print("(%d affichees)" % vus)


def pose(lang, chemin_lot):
    lot = json.load(io.open(chemin_lot, encoding="utf-8"))
    nom = lot["fichier"]
    d, brut = charger(nom)
    saut = brut.endswith("\n")
    crlf = "\r\n" in brut
    if serialiser(d, saut, crlf) != brut:
        sys.exit("  ARRET : %s ne se reproduit pas a l'octet pres -- rien n'est ecrit." % nom)
    toutes = cases(nom, d)
    erreurs, poses = [], []
    for num, vals in lot["e"].items():
        i = int(num)
        if i >= len(toutes):
            erreurs.append("#%s hors du fichier" % num)
            continue
        m = toutes[i][2]
        if vals[0] != cle(m):
            erreurs.append("#%s : le lot dit %r, le fichier %r" % (num, vals[0], cle(m)))
            continue
        cs = champs(m)
        if len(vals) - 1 != len(cs):
            erreurs.append("#%s %s : %d valeurs pour %s" % (num, vals[0], len(vals) - 1, cs))
            continue
        for c, v in zip(cs, vals[1:]):
            v = (v or "").strip()
            if not v:
                if c == "exemple" and not (m.get("exemple") or "").strip():
                    continue
                erreurs.append("#%s %s : %s vide" % (num, vals[0], c))
            elif c in ("exemple",) + tuple(TEMPS) and len(v) < 6:
                erreurs.append("#%s %s : %s trop court (%r)" % (num, vals[0], c, v))
            poses.append((i, "%s_%s" % (c, lang), v))
    if erreurs:
        sys.exit("  ARRET, rien n'est ecrit :\n    " + "\n    ".join(erreurs))
    for i, champ, v in poses:
        toutes[i][2][champ] = v
    io.open(os.path.join(RACINE, nom), "w", encoding="utf-8", newline="").write(serialiser(d, saut, crlf))
    relu, _ = charger(nom)
    rcases = cases(nom, relu)
    ecarts = [(i, c) for i, c, v in poses if rcases[i][2].get(c) != v]
    if ecarts:
        sys.exit("  RELECTURE : %d champs ne correspondent pas : %s" % (len(ecarts), ecarts[:5]))
    print("  %s : %d champs poses sur %d cartes, relus." % (nom, len(poses), len(lot["e"])))


def main():
    a = sys.argv[1:]
    lang = "pt"
    if "--langue" in a:
        k = a.index("--langue")
        lang = a[k + 1]
        del a[k:k + 2]
    if not a or a[0] == "etat":
        etat(lang)
    elif a[0] == "reste":
        reste(lang, a[1], a[2], int(a[3]) if len(a) > 3 else 40)
    elif a[0] == "pose":
        pose(lang, a[1])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
