# -*- coding: utf-8 -*-
"""Verifie que les phrases des exercices d'articles repondent en ligne.

    python audio/controler_articles.py            # controle les 152
    python audio/controler_articles.py --local    # controle le disque, pas le reseau

POURQUOI CE CONTROLE EXISTE
    Le 9 septembre 2026, Jacques signale : « quand on ecoute la phrase, c'est
    pas ta voix Aurora, c'est ta voix du iPhone ». La cause n'etait pas une
    panne : ces 120 exercices sont FABRIQUES PAR LE CODE, ils n'etaient donc
    pas dans le manifeste, aucun mp3 n'existait, et l'application retombait sur
    la synthese du telephone -- ce qu'elle doit faire quand un fichier manque.

    Le defaut ne se voyait donc nulle part : pas d'erreur, pas de trace, juste
    une voix qui n'est pas la bonne. Ce script pose la question a la place de
    l'oreille -- chaque phrase a-t-elle son fichier, oui ou non.

CE QU'IL NE JUGE PAS
    La qualite de la prononciation. Un fichier peut repondre et dire n'importe
    quoi ; seule une ecoute le dira.
"""
import argparse
import io
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MP3 = os.path.join(RACINE, "audio", "mp3")


def base_audio():
    """L'adresse que l'application utilise, lue dans index.html.

    Elle n'est pas recopiee ici : une adresse recopiee finit par pointer
    ailleurs que l'application, et le controle dirait alors le contraire de la
    verite.
    """
    src = io.open(os.path.join(RACINE, "index.html"), encoding="utf-8").read()
    for ligne in src.splitlines():
        if "AUDIO_BASE" in ligne and "http" in ligne:
            d = ligne.index("\"") + 1
            f = ligne.index("\"", d)
            return ligne[d:f]
    sys.exit("  AUDIO_BASE introuvable dans index.html.")


def phrases():
    r = subprocess.run(["node", os.path.join(RACINE, "tests", "phrases_articles.js")],
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        sys.exit("  tests/phrases_articles.js a echoue :\n" + (r.stderr or ""))
    return [l for l in (r.stdout or "").split("\n") if l.strip()]


def identifiants(textes):
    m = json.load(io.open(os.path.join(RACINE, "audio", "manifest.json"),
                          encoding="utf-8"))
    par_texte = {e["texte"]: e["id"] for e in m}
    manquants = [t for t in textes if t not in par_texte]
    if manquants:
        print("  %d phrase(s) absente(s) du manifeste -- relancer"
              " `python audio/manifest.py --ecrire` :" % len(manquants))
        for t in manquants[:5]:
            print("     " + t)
        sys.exit(1)
    return [(t, par_texte[t]) for t in textes]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--local", action="store_true",
                   help="regarde le disque au lieu du reseau")
    a = p.parse_args()

    paires = identifiants(phrases())
    print("  %d phrases d'exercices d'articles" % len(paires))

    absents = []
    if a.local:
        for texte, ident in paires:
            if not os.path.exists(os.path.join(MP3, ident + ".mp3")):
                absents.append((texte, ident))
        ou = "sur le disque"
    else:
        base = base_audio()
        print("  base : " + base)
        for i, (texte, ident) in enumerate(paires, 1):
            url = base + ident + ".mp3"
            try:
                req = urllib.request.Request(url, method="HEAD")
                with urllib.request.urlopen(req, timeout=20) as r:
                    if r.status != 200:
                        absents.append((texte, ident))
            except urllib.error.HTTPError:
                absents.append((texte, ident))
            except Exception as e:
                print("  reseau : %s" % e)
                absents.append((texte, ident))
            if i % 40 == 0:
                print("     %d / %d" % (i, len(paires)))
        ou = "en ligne"

    print()
    if absents:
        print("  MANQUANTS %s : %d sur %d" % (ou, len(absents), len(paires)))
        for texte, ident in absents[:10]:
            print("     %s  %s" % (ident, texte))
        if len(absents) > 10:
            print("     ... et %d autres" % (len(absents) - 10))
        return 1
    print("  Les %d phrases repondent %s." % (len(paires), ou))
    print("  (ce controle dit qu'un fichier existe, pas qu'il sonne juste)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
