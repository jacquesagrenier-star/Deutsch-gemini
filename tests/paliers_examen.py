# -*- coding: utf-8 -*-
"""Range les mots d'examen encore absents par PALIER, et les prepare a l'ecriture.

    python tests/paliers_examen.py              # le compte par palier
    python tests/paliers_examen.py --palier 2   # ecrit le lot, avec WikDict

LES TROIS PALIERS, ET CE QU'ILS VALENT.

    3 listes  le noyau. Fait -- 159 cartes ecrites, 22 mots-outils ecartes.
    2 listes  deux examens sur trois le demandent. Le prochain lot.
    1 liste   un seul examen. A arbitrer : beaucoup sont propres au DTZ
              (vocabulaire administratif) ou des composes que le B1 liste
              parce qu'il liste tout.

POURQUOI LE PALIER EST LE BON TRI, ET PAS LA FREQUENCE. On n'a pas de corpus
de frequence sous la main, et on n'en a pas besoin : l'accord de trois jurys
independants sur un mot dit deja qu'il est central. Un mot que les trois
listes retiennent est utile ; un mot qu'une seule retient peut n'etre utile
qu'a cet examen-la.

CE QUE WIKDICT APPORTE, ET CE QU'IL NE FAUT PAS LUI DEMANDER. Il donne la
nature (nom, verbe, adjectif), le genre, le pluriel et une premiere traduction
francaise -- de quoi pre-remplir un lot au lieu de partir de la page blanche.
Il s'est trompe quatre fois sur les 82 noms du noyau (Doktores, Kontos,
Waegen, Herrn), soit une sur vingt. Chaque champ qu'il propose se relit.

Un mot qu'il ne connait pas n'est pas forcement du bruit : ce sont surtout des
composes (« Waschmaschine ») et des variantes autrichiennes. Ils sortent dans
un fichier a part plutot que d'etre jetes.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMENS = os.path.join(RACINE, "examens")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import langue as L                                          # noqa: E402
import listes_examen as X                                   # noqa: E402

NATURES = {"n": "noms", "v": "verbes", "adj": "adjectifs", "adv": "adverbes"}


def wikdict():
    """Les entetes du dictionnaire de-fr, indexees par mot allemand."""
    d = os.path.join(RACINE, "dict", "de-fr")
    tete = {}
    for f in sorted(os.listdir(d)):
        if not f.endswith(".json"):
            continue
        for e in json.load(io.open(os.path.join(d, f), encoding="utf-8")):
            if isinstance(e, dict) and e.get("m"):
                tete.setdefault(e["m"], e)
    return tete


def corpus():
    lg = L.Langue("tr")          # la langue cible est sans importance ici
    out = set()
    for cartes in lg.toutes_les_cartes().values():
        for c in cartes:
            mot = (c.get("cle") or "").strip()
            if mot:
                out.add(mot)
    return out


def ecartes():
    """Les mots-outils deja arbitres : ils ne reviennent pas a chaque palier."""
    chemin = os.path.join(RACINE, "ajouts", "noyau-00-ecartes.txt")
    if not os.path.isfile(chemin):
        return set()
    return {l.strip() for l in io.open(chemin, encoding="utf-8")
            if l.strip() and not l.startswith("#")}


def paliers():
    listes = X.charger()
    dedans = corpus()
    # La casse : « schade » et « Schade » sont le meme mot a apprendre.
    minuscules = {m.lower() for m in dedans}
    hors = ecartes()

    out = {3: [], 2: [], 1: []}
    union = set()
    for mots in listes.values():
        union |= mots
    for mot in sorted(union):
        if mot in dedans or mot.lower() in minuscules or mot in hors:
            continue
        n = sum(1 for mots in listes.values() if mot in mots)
        out[n].append(mot)
    return out


def ecrire_lot(n, tete):
    """Le niveau est LU, pas devine : un mot de la liste Goethe A2 est un mot
    A2, les autres sont B1. C'est la seule source de verite disponible, et
    elle vaut mieux qu'un jugement au cas par cas sur 600 mots."""
    mots = paliers()[n]
    a2 = X.charger().get("goethe_a2", set())
    par_nature = {v: [] for v in NATURES.values()}
    inconnus = []
    for mot in mots:
        e = tete.get(mot)
        nature = NATURES.get((e or {}).get("p"))
        if e is None or nature is None:
            inconnus.append(mot)
            continue
        par_nature[nature].append((mot, e, "A2" if mot in a2 else "B1"))

    os.makedirs(EXAMENS, exist_ok=True)
    chemin = os.path.join(EXAMENS, "palier%d.txt" % n)
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Palier %d : mots demandes par %d liste(s) sur 3, absents du cours\n"
                % (n, n))
        f.write("# %d mots classes, %d non reconnus par WikDict.\n" % (
            sum(len(v) for v in par_nature.values()), len(inconnus)))
        f.write("# Les champs proposes par WikDict sont a RELIRE : il s'est\n")
        f.write("# trompe une fois sur vingt sur les pluriels du noyau.\n")
        for nature in ("noms", "verbes", "adjectifs", "adverbes"):
            f.write("\n## %s (%d)\n" % (nature.upper(), len(par_nature[nature])))
            for mot, e, niveau in par_nature[nature]:
                f.write("%s | %s | %s | %s | %s\n" % (
                    niveau, e.get("g") or "", mot, e.get("pl") or "",
                    ", ".join(e.get("t", [])[:3])))
        f.write("\n## NON RECONNUS -- composes, variantes, bruit d'extraction (%d)\n"
                % len(inconnus))
        for mot in inconnus:
            f.write("%s\n" % mot)
    print("  ecrit : examens/palier%d.txt" % n)
    for nature in ("noms", "verbes", "adjectifs", "adverbes"):
        print("    %-11s %4d" % (nature, len(par_nature[nature])))
    print("    %-11s %4d" % ("inconnus", len(inconnus)))


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    p = paliers()
    for n in (3, 2, 1):
        print("  palier %d (%d liste(s))  %5d mot(s) encore absent(s)"
              % (n, n, len(p[n])))
    print()
    for i, a in enumerate(sys.argv):
        if a == "--palier" and i + 1 < len(sys.argv):
            ecrire_lot(int(sys.argv[i + 1]), wikdict())
    return 0


if __name__ == "__main__":
    sys.exit(main())
