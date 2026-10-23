# -*- coding: utf-8 -*-
"""Refait quelques fichiers ESPAGNOLS mal dits, sous leur nom d'origine.

    python audio/refaire_es.py              # a blanc : ce qui serait fait, et le cout
    python audio/refaire_es.py --payer      # genere, recoupe, normalise (deux voix)

POURQUOI UN SCRIPT A PART. generer_es.py ne refait que ce qui MANQUE : un
fichier present est un fichier fait. Ici le fichier existe, il est servi, et
il est faux. Le nom ne change pas (c'est l'empreinte du texte AFFICHE, que
l'app recalcule) : seul ce qu'on fait DIRE a la voix change.

LES DEUX DEFAUTS QUI L'ONT FAIT NAITRE (Jacques, 23 oct. 2026) :
  - « ¿Hay…? » : la voix tenait le « y » une seconde, « hayyyyy ». Les points
    de suspension faisaient trainer la synthese -- Monica le disait en 0,97 s
    de parole, contre 0,72 s pour « ¿Puedo…? » qui a deux syllabes. On fait
    dire « ¿Hay? » ; le fichier garde le nom de « ¿Hay…? ».
  - « a pie » : lu comme l'anglais « a pie » (une tarte). generer_es.py
    n'emploie la porteuse que pour les textes SANS espace -- « la casa » porte
    son contexte, mais « a pie » est fait de deux mots anglais. On le fait donc
    dire dans la porteuse espagnole, comme un mot seul.

LA PORTEUSE est celle des refus du 22 oct. (« Palabra. ... gracias ») : un
point puis des points de suspension imposent une vraie pause, que recouper.py
sait trouver. Pas d'ancien fichier en reference : l'ancien est justement trop
long, c'est le defaut qu'on corrige.

L'ANCIEN FICHIER est mis de cote dans ~/.wortando/audio-es-avant-23-oct/ avant
d'etre remplace. Apres : python audio/deposer.py, puis incrementer
AUDIO_REVISION dans index.html -- sans quoi les telephones gardent l'ancien
son douze mois.
"""
import argparse, os, shutil, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                       # noqa : cle, reglages, modeles
import manifest_es                   # noqa : identifiant()
import normaliser as N               # noqa
from generer_es import VOIX, VITESSE_PORTEUSE, appeler   # noqa
from recouper import recouper, Refus  # noqa

PORTEUSE = "Palabra. ... %s"
# (texte affiche, donc nom du fichier ; texte dit dans la porteuse)
REFAITS = [
    ("¿Hay…?", "¿Hay?"),
    ("a pie", "a pie"),
]
ARCHIVE = os.path.join(os.path.expanduser("~"), ".wortando", "audio-es-avant-23-oct")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--payer", action="store_true", help="appelle ElevenLabs (sinon a blanc)")
    a = p.parse_args()

    modele, taux = generer.MODELES["v2"]
    cout = int(sum(len(PORTEUSE % dit) for _, dit in REFAITS) * taux) * len(VOIX)
    print("%d textes x %d voix, porteuse %r, modele %s : environ %d credits"
          % (len(REFAITS), len(VOIX), PORTEUSE, modele, cout))
    for affiche, dit in REFAITS:
        print("  %s  %-8s <- %r" % (manifest_es.identifiant(affiche), affiche, PORTEUSE % dit))
    if not a.payer:
        return

    N.FF = N.ffmpeg()
    cle = generer.cle_api()
    rates = 0
    for variante, (voix, dossier) in sorted(VOIX.items()):
        bruts = os.path.join(RACINE, "audio", "bruts_es", dossier, "refaits-23-oct")
        os.makedirs(bruts, exist_ok=True)
        os.makedirs(os.path.join(ARCHIVE, dossier), exist_ok=True)
        for affiche, dit in REFAITS:
            ident = manifest_es.identifiant(affiche)
            brut = os.path.join(bruts, ident + ".mp3")
            if not os.path.exists(brut):
                son = appeler(voix, PORTEUSE % dit, dict(generer.REGLAGES, speed=VITESSE_PORTEUSE), modele, cle)
                open(brut, "wb").write(son)
            cible = os.path.join(RACINE, "audio", "mp3", dossier, ident + ".mp3")
            original = os.path.join(N.SOURCE, dossier, ident + ".mp3")
            coupe = brut + ".coupe.mp3"
            try:
                recouper(brut, coupe, texte=dit)
            except Refus as err:
                print("  REFUS %s %s : %s" % (dossier, affiche, err))
                rates += 1
                continue
            for ancien, nom in ((cible, "mp3"), (original, "original")):
                garde = os.path.join(ARCHIVE, dossier, "%s.%s.mp3" % (ident, nom))
                if os.path.exists(ancien) and not os.path.exists(garde):
                    shutil.copy2(ancien, garde)
            os.makedirs(os.path.dirname(original), exist_ok=True)
            shutil.copy2(coupe, original)
            tmp = cible + ".norm.mp3"
            if not N.normaliser(original, tmp, intermediaire=tmp + ".t1.mp3"):
                print("  NORMALISATION RATEE %s %s" % (dossier, affiche))
                rates += 1
                continue
            os.replace(tmp, cible)
            os.remove(coupe)
            print("  %s %-8s %.2f s" % (dossier, affiche, N.duree(cible)))
    print("fait, %d rate(s)" % rates)


if __name__ == "__main__":
    main()
