# -*- coding: utf-8 -*-
"""L'apostrophe ukrainienne : ʼ (U+02BC), jamais l'apostrophe droite ' (lot 89, 13 nov. 2026).

En ukrainien l'apostrophe fait partie du mot (м'ясо, п'ять, сім'я, з'явиться). La forme typographique
recommandee est ʼ (U+02BC, « lettre apostrophe ») : c'est une LETTRE, donc le mot reste entier au
double-clic, a la coupure de ligne et dans la recherche. Decision du chef d'orchestre du 13 nov. 2026.

La recherche de l'app tient ', ’ et ʼ pour equivalents (normalizeSearch, normaliserSaisie) : un clavier
ukrainien sous Windows tape la droite, et elle doit trouver le mot ecrit avec ʼ.

    python tests/apostrophe_uk.py              controle : les fichiers SERVIS (liste blanche de
                                               publication/construire_site.py) ; code 1 s'il en reste
    python tests/apostrophe_uk.py --liste      les mots touches, pour verifier qu'ils sont ukrainiens
    python tests/apostrophe_uk.py --ecrire     remplace ' -> ʼ entre deux lettres cyrilliques dans les
                                               fichiers servis ET leurs sources (scripts poser_*_uk.py,
                                               ajouts/, corrections_uk/, etapes/traductions/...), pour
                                               qu'une reconstruction ne ramene pas la droite.

Hors champ : les archives de travail (retours/, relecture_uk/, .claude/, video/, scenes/ -- la serie
video --, les .md). Le controle est appele par tests/verifier.py.
"""
import io
import os
import re
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "publication"))

CYR = "а-яА-ЯіїєґІЇЄҐёЁ"
DROITE = re.compile("(?<=[" + CYR + "])'(?=[" + CYR + "])")
MOT = re.compile("[" + CYR + "]+'[" + CYR + "'ʼ]*")
APOSTROPHE_UK = "ʼ"
TEXTES = (".json", ".js", ".html", ".py")
HORS_CHAMP = ("retours/", "relecture_uk/", ".claude/", "video/", "scenes/", "audio/", "export/")


def fichiers_suivis():
    sortie = subprocess.run(["git", "ls-files", "-z"], cwd=RACINE, capture_output=True).stdout
    return [f for f in sortie.decode("utf-8").split("\0") if f]


def fichiers_servis():
    import construire_site
    return [f for f in fichiers_suivis()
            if f.endswith((".json", ".js", ".html")) and construire_site.publie(f)]


def fichiers_a_corriger():
    return [f for f in fichiers_suivis()
            if f.endswith(TEXTES) and not f.startswith(HORS_CHAMP)]


def lire(f):
    try:
        return io.open(os.path.join(RACINE, f), encoding="utf-8", newline="").read()
    except (UnicodeDecodeError, OSError):
        return None


def candidats():
    """Les fichiers suivis qui contiennent le motif, par git grep (2 s au lieu de 12 sous OneDrive)."""
    sortie = subprocess.run(["git", "grep", "-l", "-z", "-P", "(*UTF)[" + CYR + "]'[" + CYR + "]"],
                            cwd=RACINE, capture_output=True)
    if sortie.returncode not in (0, 1):
        return None
    return [f for f in sortie.stdout.decode("utf-8").split("\0") if f]


def controler(fichiers=None):
    """[(fichier, nombre)] des apostrophes droites entre deux lettres cyrilliques, fichiers servis."""
    if fichiers is None:
        trouves = candidats()
        if trouves is None:
            fichiers = fichiers_servis()
        else:
            import construire_site
            fichiers = [f for f in trouves if f.endswith((".json", ".js", ".html")) and construire_site.publie(f)]
    restes = []
    for f in fichiers:
        texte = lire(f)
        if texte and "'" in texte:
            n = len(DROITE.findall(texte))
            if n:
                restes.append((f, n))
    return restes


def main():
    if "--liste" in sys.argv:
        mots = {}
        for f in fichiers_a_corriger():
            texte = lire(f)
            if texte and "'" in texte:
                for m in MOT.findall(texte):
                    mots[m] = mots.get(m, 0) + 1
        for m, n in sorted(mots.items(), key=lambda x: -x[1]):
            print("%5d  %s" % (n, m))
        print("%d mots distincts" % len(mots))
        return 0
    if "--ecrire" in sys.argv:
        total, touches = 0, 0
        for f in fichiers_a_corriger():
            texte = lire(f)
            if not texte or "'" not in texte:
                continue
            neuf, n = DROITE.subn(APOSTROPHE_UK, texte)
            if n:
                io.open(os.path.join(RACINE, f), "w", encoding="utf-8", newline="").write(neuf)
                total += n
                touches += 1
        print("%d apostrophes remplacees dans %d fichiers" % (total, touches))
        return 0
    restes = controler()
    for f, n in restes:
        print("   %s : %d apostrophe(s) droite(s) en ukrainien" % (f, n))
    print("%d fichier(s) servi(s) avec une apostrophe droite en ukrainien" % len(restes))
    return 1 if restes else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
