# -*- coding: utf-8 -*-
"""Classe nos entrees par frequence d'usage, a partir des listes de Leipzig.

    python tests/frequence.py            -- le rapport, sans rien ecrire
    python tests/frequence.py --ecrire   -- ecrit frequence.json

D'OU VIENNENT LES DONNEES, ET CE QUE LA LICENCE OBLIGE
    Leipzig Corpora Collection (Universitat Leipzig), sous CC BY : usage
    commercial permis, PAS de partage a l'identique -- moins contraignant que
    le CC BY-SA de WikDict, que le depot porte deja. L'attribution est
    obligatoire et va au meme endroit que celle de WikDict.

        (c) Universitat Leipzig / Sachsische Akademie der Wissenschaften / InfAI

    Deux corpus, volontairement :
        deu_mixed-typical_2011  le melange equilibre -- registre proche de
                                celui qu'un apprenant rencontre
        deu_news_2023           la presse recente -- vocabulaire d'aujourd'hui
    Chacun est ramene a une frequence PAR MILLION avant d'etre additionne,
    sinon le plus gros corpus deciderait seul.

    Les archives vivent HORS DU DEPOT (C:/Users/jacqu/.wortando/frequence) :
    100 Mo de donnees brutes n'ont rien a faire dans un depot public, et seul
    le classement derive est versionne.

⚠️ LE PIEGE QUE CE SCRIPT CONTOURNE
    Ces listes comptent des FORMES, pas des lemmes. La frequence de « gehen »
    est portee par « geht », « ging », « gegangen » -- l'infinitif lui-meme est
    rare. Un appariement naif ferait donc descendre tous les verbes et tous les
    adjectifs, et monter tous les noms.

    Deux protections, et la seconde suffirait a elle seule :

    1. On additionne les formes qu'on POSSEDE DEJA : les six personnes du
       present pour un verbe, le pluriel pour un nom, les cinq desinences
       regulieres pour un adjectif. Aucun lemmatiseur, aucune dependance.
    2. ON NE CLASSE QU'A L'INTERIEUR D'UNE CATEGORIE. Un bloc melange les types
       selon une composition fixe (tant de noms, tant de verbes), donc on n'a
       jamais besoin de comparer un verbe a un nom. Le biais restant est
       constant dans une categorie : il s'annule au classement.

⚠️ CE QUI N'EST PAS CLASSABLE
    Les expressions (« Wie geht's ? ») sont des suites de mots : aucune liste
    de frequence ne les contient. Elles sortent du classement et le rapport le
    dit, plutot que de leur donner un rang invente.
"""
import argparse
import io
import json
import os
import re
import sys
import tarfile

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = "C:/Users/jacqu/.wortando/frequence"
CORPUS = ["deu_mixed-typical_2011_300K", "deu_news_2023_300K"]
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
# Les desinences de la declinaison faible et forte. « gut » -> gute, guten,
# gutes, guter, gutem. On ne genere pas le comparatif : « besser » n'est pas
# une forme de « gut » au sens ou une liste de frequence l'entendrait.
DESINENCES = ["e", "en", "es", "er", "em"]


def charger_frequences():
    """forme -> frequence par million, additionnee sur les deux corpus."""
    freq = {}
    for nom in CORPUS:
        chemin = os.path.join(SOURCE, nom, nom + "-words.txt")
        if not os.path.exists(chemin):
            arch = os.path.join(SOURCE, nom + ".tar.gz")
            if not os.path.exists(arch):
                sys.exit("  Corpus absent : %s\n  Le telecharger depuis "
                         "https://downloads.wortschatz-leipzig.de/corpora/%s.tar.gz"
                         % (arch, nom))
            with tarfile.open(arch) as t:
                t.extract("%s/%s-words.txt" % (nom, nom), SOURCE)
        brut, total = {}, 0
        with io.open(chemin, encoding="utf-8") as f:
            for ligne in f:
                p = ligne.rstrip("\n").split("\t")
                if len(p) < 3:
                    continue
                try:
                    n = int(p[2])
                except ValueError:
                    continue
                brut[p[1]] = brut.get(p[1], 0) + n
                total += n
        if not total:
            sys.exit("  Corpus vide : " + chemin)
        for mot, n in brut.items():
            freq[mot] = freq.get(mot, 0.0) + n * 1e6 / total
        print("  %-28s %7d formes, %9d occurrences" % (nom, len(brut), total))
    return freq


def eclater(f):
    """Les variantes d'une entree telle que nos fichiers l'ecrivent.

    Plusieurs entrees portent une PAIRE separee par une barre oblique --
    « ehrlich/unehrlich », « fern/nah », « bloß / nur ». Cherchees telles
    quelles, elles etaient muettes alors que leurs deux membres sont courants.
    Une barre oblique n'apparait jamais dans une forme allemande : la couper
    est sans risque.
    """
    f = (f or "").strip()
    if not f:
        return []
    if "/" in f:
        return [p.strip() for p in f.split("/") if p.strip()]
    return [f]


def somme(freq, formes):
    """La frequence cumulee des formes trouvees, et combien ont ete trouvees."""
    total, vues, trouvees = 0.0, set(), 0
    for brut in formes:
        for f in eclater(brut):
            if f in vues:
                continue
            vues.add(f)
            v = freq.get(f)
            if v:
                total += v
                trouvees += 1
    return total, trouvees


def note_nom(freq, o):
    s, n = somme(freq, [o.get("mot"), o.get("pluriel")])
    return s, n, False


PRONOMS = {"mich", "dich", "sich", "uns", "euch"}


def formes_verbales(o):
    """Toutes les formes d'un verbe qui tiennent en UN SEUL mot.

    ⚠️ Deux familles cassaient l'appariement, et pour deux raisons opposees.

    LES PRONOMINAUX. « sich erinnern » s'ecrit en deux mots -- infinitif comme
    present (« erinnere mich »). Aucune forme ne pouvait donc etre trouvee. Le
    verbe lui-meme, « erinnern », est parfaitement courant : il suffit de
    retirer le pronom.

    LES SEPARABLES. « anrufen » se dit « rufe an » : deux mots la aussi, mais
    ici on ne PEUT pas retirer la particule -- « rufe » donnerait la frequence
    de « rufen », un autre verbe. La forme d'un seul mot qui existe vraiment
    est le PARTICIPE, « angerufen », qu'on va chercher dans la phrase d'exemple
    du parfait. Sans ca, le rang median des separables etait 1017 contre 436
    pour les autres, et « anrufen » -- verbe d'A1 -- tombait au rang 806.
    """
    brutes = [o.get("infinitif")]
    p = o.get("praesens")
    if isinstance(p, dict):
        brutes.extend(p.values())

    out, separable = [], False
    for f in brutes:
        mots = (f or "").strip().split()
        if len(mots) > 1 and mots[0] == "sich":
            mots = mots[1:]
        if len(mots) > 1 and mots[-1] in PRONOMS:
            mots = mots[:-1]
        if len(mots) == 1:
            out.append(mots[0])
        elif len(mots) == 2:
            separable = True

    if separable:
        # La particule est le dernier mot du present, le participe le seul
        # mot de la phrase du parfait qui commence par elle ET porte un « ge ».
        p1 = ((p or {}).get("ich") or "").split()
        part = p1[-1] if len(p1) > 1 and p1[-1] not in PRONOMS else ""
        if part:
            for mot in re.findall(r"\w+", o.get("perfekt") or "", re.UNICODE):
                b = mot.lower()
                if b.startswith(part) and "ge" in b[len(part):]:
                    out.append(mot)
    return out


def est_separable(o):
    m = ((o.get("praesens") or {}).get("ich") or "").split()
    return len(m) > 1 and m[-1] not in PRONOMS


def note_verbe(freq, o):
    # L'infinitif ET les six personnes du present. C'est ce qui remet les
    # verbes a leur place : « sein » comme forme est rare, « ist » ne l'est pas.
    s, n = somme(freq, formes_verbales(o))
    return s, n, False


def mediane(v):
    v = sorted(v)
    return v[len(v) // 2] if v else 0


def corriger_familles(lignes):
    """Fond deux sous-groupes mesures a des echelles differentes.

    Le participe ne rattrape qu'une partie du retard des verbes separables :
    il couvre le parfait, alors que l'usage courant est au present, ou le
    verbe est coupe en deux (« rufe ... an ») et donc introuvable dans une
    liste de formes. Apres correction le rang median restait 873 pour les
    separables contre 554 pour les autres -- « anrufen », verbe d'A1, au rang
    629.

    ⚠️ C'est exactement le probleme des categories, un cran plus bas : deux
    populations dont la MESURE, non la langue, differe d'un facteur a peu pres
    constant. Et la solution est la meme -- ne comparer que ce qui est
    comparable. On classe chaque famille contre elle-meme, puis on fond les
    deux listes par PERCENTILE. Le 10e percentile des separables se retrouve
    au niveau du 10e percentile des autres, ce qui est vrai par construction
    et n'invente aucune frequence.

    ⚠️ UNE PREMIERE VERSION FONDAIT LES DEUX LISTES PAR PERCENTILE, ET C'ETAIT
    FAUX. Les rangs medians devenaient parfaits (657 contre 656) mais la tete
    du classement devenait absurde : « annehmen » et « anbieten » passaient
    devant « haben » et « koennen ». Fondre par percentile suppose deux
    distributions de MEME FORME ; or le sommet de la frequence allemande est
    tenu par des auxiliaires et des modaux, et aucun verbe separable n'en
    approche. Le percentile corrigeait le milieu en cassant les extremes.

    D'ou un simple FACTEUR MULTIPLICATIF, qui est le modele qu'on vient de
    decrire : ce qui manque a un separable, c'est la masse du present, une
    proportion a peu pres constante de son usage. On l'estime par le rapport
    des medianes, on multiplie, et on classe tout ensemble. La forme de la
    distribution est preservee -- le sommet reste le sommet.

    Renvoie (avant, apres, facteur) pour que le rapport montre le resultat au
    lieu de l'affirmer.
    """
    if not lignes:
        return None
    rang = {id(l): i for i, l in enumerate(sorted(lignes, key=lambda l: -l[2]))}
    avant = (mediane([rang[id(l)] for l in lignes if l[5] == "sep"]),
             mediane([rang[id(l)] for l in lignes if l[5] != "sep"]))
    m_sep = mediane([l[2] for l in lignes if l[5] == "sep" and l[3]])
    m_autre = mediane([l[2] for l in lignes if l[5] != "sep" and l[3]])
    if not m_sep or not m_autre:
        return None
    facteur = m_autre / m_sep
    for l in lignes:
        l[6] = l[2] * facteur if l[5] == "sep" else l[2]
    rang = {id(l): i for i, l in enumerate(sorted(lignes, key=lambda l: -l[6]))}
    apres = (mediane([rang[id(l)] for l in lignes if l[5] == "sep"]),
             mediane([rang[id(l)] for l in lignes if l[5] != "sep"]))
    return (avant, apres, facteur)


def note_simple(freq, o):
    s, n = somme(freq, [(o.get("mot") or "").strip()])
    return s, n, False


# ⚠️ L'ADJECTIF EST LE CAS DIFFICILE, ET IL A FALLU MESURER POUR TRANCHER.
#
#   Compter la forme NUE hisse « zu » au premier rang des adjectifs -- la
#   frequence est celle de la preposition et de la particule, pas celle de
#   « zu » au sens de « ferme ». Meme chose pour « rund » et « weiter ».
#
#   Ne compter que les formes DECLINEES corrige ca (le classement devient neu,
#   gross, weit, deutsch, gut, klein...) mais rend muets 70 adjectifs de plus :
#   les invariables (lila, beige, chic, gratis, fit, extra) n'ont aucune forme
#   declinee, et « hoch » se decline en « hohe », pas en « hoche ».
#
#   D'ou la regle retenue : LES DECLINEES D'ABORD, la forme nue seulement si
#   aucune declinee n'est connue -- et dans ce cas l'entree est SIGNALEE, parce
#   que c'est exactement la ou le classement est fragile.
def note_adjectif(freq, o):
    # eclater() AVANT de decliner : « ehrlich/unehrlich » + « e » donnerait
    # « ehrlich/unehrliche », dont la coupure produirait la forme nue du
    # premier membre -- exactement ce que le repli est cense eviter.
    bases = eclater(o.get("mot"))
    if not bases:
        return 0.0, 0, False
    s, n = somme(freq, [b + d for b in bases for d in DESINENCES])
    if n:
        return s, n, False
    s, n = somme(freq, bases)
    return s, n, bool(n)


def entrees():
    """(categorie, niveau, cle, noteur, objet) pour tout le corpus."""
    out = []
    th = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))
    for t in th["themes"]:
        for m in t.get("mots", []):
            if m.get("mot"):
                out.append(("noms", t.get("niveau"), m["mot"], note_nom, m))
    for fichier, cat, cle, noteur in [
            ("verbe.json", "verbes", "infinitif", note_verbe),
            ("adjectif.json", "adjectifs", "mot", note_adjectif),
            ("adverbe.json", "adverbes", "mot", note_simple),
            ("redewendung.json", "expressions", "mot", note_simple)]:
        chemin = os.path.join(RACINE, fichier)
        if not os.path.exists(chemin):
            continue
        d = json.load(io.open(chemin, encoding="utf-8"))
        for niv in NIVEAUX:
            for o in (d.get(niv) or []) if isinstance(d, dict) else []:
                if o.get(cle):
                    out.append((cat, niv, o[cle], noteur, o))
    # ⚠️ funktionswort.json est range par FAMILLE GRAMMATICALE (konjunktionen,
    # partikeln, praepositionen, zahlen, pronomen, artikelwoerter) et non par
    # niveau CECR. Le parcourir comme les autres le rendait invisible : il
    # n'apparaissait tout simplement pas dans le rapport, sans erreur.
    chemin = os.path.join(RACINE, "funktionswort.json")
    if os.path.exists(chemin):
        d = json.load(io.open(chemin, encoding="utf-8"))
        for famille, liste in (d.items() if isinstance(d, dict) else []):
            if not isinstance(liste, list):
                continue
            for o in liste:
                if o.get("mot"):
                    out.append(("mots-outils", famille, o["mot"], note_simple, o))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ecrire", action="store_true",
                    help="ecrit frequence.json (sinon : rapport seulement)")
    a = ap.parse_args()

    print("\nLES CORPUS")
    freq = charger_frequences()
    print("  %-28s %7d formes distinctes au total\n" % ("reunis", len(freq)))

    par_cat = {}
    for cat, niv, cle, noteur, o in entrees():
        # La FAMILLE : un sous-groupe dont on sait que la mesure le penalise
        # d'un facteur a peu pres constant. Voir corriger_familles().
        fam = "sep" if (cat == "verbes" and est_separable(o)) else ""
        s, n, r = noteur(freq, o)
        # (mot, niveau, frequence, formes trouvees, repli, famille, cle de tri)
        par_cat.setdefault(cat, []).append([cle, niv, s, n, r, fam, s])
    ecart = corriger_familles(par_cat.get("verbes") or [])

    print("LA COUVERTURE -- combien de nos mots la liste connait")
    print("  %-13s %6s %9s %9s %8s %s"
          % ("", "total", "trouves", "muets", "%", "replis"))
    print("  " + "-" * 60)
    resultat, muets_par_cat, replis_par_cat = {}, {}, {}
    for cat in ["noms", "verbes", "adjectifs", "adverbes", "mots-outils",
                "expressions"]:
        lignes = par_cat.get(cat)
        if not lignes:
            continue
        muets = [l[0] for l in lignes if l[3] == 0]
        replis = sorted([(l[2], l[0]) for l in lignes if l[4]], reverse=True)
        pct = 100.0 * (len(lignes) - len(muets)) / len(lignes)
        print("  %-13s %6d %9d %9d %7.1f%% %6d"
              % (cat, len(lignes), len(lignes) - len(muets), len(muets), pct,
                 len(replis)))
        muets_par_cat[cat] = muets
        replis_par_cat[cat] = replis
        # Le classement : la plus frequente d'abord. Les muettes finissent en
        # queue, dans l'ordre alphabetique -- un ordre arbitraire ASSUME vaut
        # mieux qu'un ordre arbitraire qui se prend pour un classement.
        # Tri sur la CLE l[6] : la frequence pour la plupart des categories,
        # le percentile de famille pour les verbes (voir corriger_familles).
        connues = sorted([l for l in lignes if l[3]], key=lambda l: -l[6])
        inconnues = sorted([l for l in lignes if not l[3]], key=lambda l: l[0])
        rangs = []
        for l in connues:
            e = {"m": l[0], "n": l[1], "f": round(l[2], 2)}
            if l[4]:
                e["approx"] = 1   # note obtenue sur la forme nue : fragile
            rangs.append(e)
        resultat[cat] = rangs + [{"m": l[0], "n": l[1], "f": 0}
                                 for l in inconnues]

    print()
    for cat in ["noms", "verbes", "adjectifs", "adverbes", "mots-outils"]:
        if cat in resultat:
            print("  %-12s tete : %s" % (
                cat, ", ".join(x["m"] for x in resultat[cat][:12])))
    if ecart:
        print("\n  LES VERBES SEPARABLES -- rang median, separables / autres")
        print("     avant correction : %4d / %4d" % ecart[0])
        print("     apres correction : %4d / %4d   (facteur x%.2f)"
              % (ecart[1] + (ecart[2],)))

    print("\n  LES MUETS -- absents de la liste, ranges en queue")
    for cat, muets in muets_par_cat.items():
        if muets:
            print("  %-13s %4d, dont : %s"
                  % (cat, len(muets), ", ".join(sorted(muets)[:7])))
    replis_adj = replis_par_cat.get("adjectifs") or []
    if replis_adj:
        print("\n  LES REPLIS -- notes sur la forme nue faute de declinaison "
              "connue,\n  donc les plus exposes a l'homographie. Les plus hauts "
              "d'abord :")
        print("  " + ", ".join("%s (%.0f)" % (c, s) for s, c in replis_adj[:12]))

    if not a.ecrire:
        print("\n  (rapport seulement -- relancer avec --ecrire pour produire "
              "frequence.json)")
        return

    dest = os.path.join(RACINE, "frequence.json")
    val = {
        "_source": "Leipzig Corpora Collection (CC BY) -- "
                   "(c) Universitat Leipzig / Sachsische Akademie der "
                   "Wissenschaften / InfAI",
        "_corpus": CORPUS,
        "_note": "Classement PAR CATEGORIE, jamais entre categories : les "
                 "listes comptent des formes et non des lemmes, ce qui "
                 "penalise verbes et adjectifs face aux noms. f = frequence "
                 "par million, cumulee sur les formes connues ; f = 0 veut "
                 "dire ABSENT de la liste, pas rare.",
        "categories": resultat
    }
    # COMPACT, et une ligne par categorie. Indente, le meme contenu pesait
    # 490 ko contre 250 : l'app charge ses donnees depuis GitHub a chaque
    # ouverture, et ce fichier est derive -- la source lisible, c'est ce
    # script. Une ligne par categorie garde tout de meme le diff lisible
    # quand un mot change de rang.
    parts = []
    for cle, v in val.items():
        if cle != "categories":
            parts.append(" %s: %s" % (json.dumps(cle), json.dumps(v, ensure_ascii=False)))
    cats = [" %s: %s" % (json.dumps(k), json.dumps(v, ensure_ascii=False,
                                                   separators=(",", ":")))
            for k, v in val["categories"].items()]
    io.open(dest, "w", encoding="utf-8", newline="").write(
        "{\n" + ",\n".join(parts) + ',\n "categories": {\n'
        + ",\n".join(cats) + "\n }\n}\n")
    print("\n  ecrit : frequence.json  (%d ko, %d entrees)"
          % (os.path.getsize(dest) // 1024,
             sum(len(v) for v in val["categories"].values())))


if __name__ == "__main__":
    main()
