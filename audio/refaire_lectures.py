# -*- coding: utf-8 -*-
"""Refait les sons dont le texte a une lecture (audio/lectures/<langue>.json).

    python audio/refaire_lectures.py --langue de --a-blanc
    python audio/refaire_lectures.py --langue de
    python audio/refaire_lectures.py --langue es          # les deux voix
    puis : python audio/controler_sons.py (--dossiers de), audio/deposer.py,
           et AUDIO_REVISION + 1 dans index.html.

POURQUOI (28 oct. 2026) : voir audio/lectures.py -- les nombres sortaient
haches parce qu'on envoyait « 3,90 € » a la voix au lieu de « drei Euro
neunzig ».

CE QUE FAIT LE SCRIPT, pour chaque texte qui a une lecture :
  1. sauvegarde le son en ligne ET son original non normalise dans
     audio/mp3_avant_lecture/ (une fois : on garde le premier etat) ;
  2. demande la LECTURE a la meme voix, mêmes reglages, meme graine ;
     un texte sans espace passe par la porteuse et la recoupe, comme
     refaire_mots.py (un mot seul se lit mal) ;
  3. ecrit le brut dans audio/mp3_original/ -- sinon une normalisation future
     repartirait de l'ancien original et ferait revenir l'ancien son -- puis
     normalise vers audio/mp3/.
Le nom du fichier ne change pas : sha1(texte ECRIT)[:16].

REPRENABLE : audio/lectures/faits.json retient, par dossier, la lecture deja
produite pour chaque identifiant. Une lecture corrigee plus tard est refaite ;
une lecture inchangee ne coute plus rien.
"""
import argparse
import hashlib
import io
import json
import os
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                                   # noqa: E402
import lectures                                  # noqa: E402
import normaliser as N                           # noqa: E402
from recouper import recouper, Refus             # noqa: E402

MP3 = os.path.join(RACINE, "audio", "mp3")
AVANT = os.path.join(RACINE, "audio", "mp3_avant_lecture")
FAITS = os.path.join(RACINE, "audio", "lectures", "faits.json")
PORTEUSES = {"de": "Wort: %s.", "es": "Palabra: %s."}
VITESSE_PORTEUSE = 0.80

# langue -> [(dossier sous audio/mp3, identifiant de voix)]
VOIX = {
    "de": [("", generer.VOIX)],
    "es": [("es-es", "3EsCRTMlRTbsPyDyDm45"),     # Lolita (Espagne)
           ("es-419", "yR4AeVlfzs6IiKxIH9gQ")],   # Monica (Amerique latine)
}


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def appeler(voix, texte, reglages, cle):
    """Comme generer.synthetiser, mais pour n'importe quelle voix."""
    sauve = generer.VOIX
    generer.VOIX = voix
    try:
        if "speed" in reglages:
            return generer.synthetiser(texte, generer.MODELES["v2"][0], cle, reglages=reglages)
        return generer.synthetiser(texte, generer.MODELES["v2"][0], cle)
    finally:
        generer.VOIX = sauve


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--langue", required=True, choices=sorted(VOIX))
    p.add_argument("--a-blanc", action="store_true")
    p.add_argument("--plafond", type=int, default=30000)
    a = p.parse_args()

    table = lectures.table(a.langue)
    faits = json.load(io.open(FAITS, encoding="utf-8")) if os.path.exists(FAITS) else {}
    N.FF = N.ffmpeg()
    cle = None
    depense = 0
    for dossier, voix in VOIX[a.langue]:
        cle_dossier = dossier or "de"
        deja = faits.setdefault(cle_dossier, {})
        final_dir = os.path.join(MP3, dossier)
        orig_dir = os.path.join(N.SOURCE, dossier)
        a_faire = []
        for ecrit, dit in sorted(table.items()):
            i = identifiant(ecrit)
            if not os.path.exists(os.path.join(final_dir, i + ".mp3")):
                continue          # pas (encore) de son pour ce texte dans cette voix
            if deja.get(i) == dit:
                continue
            a_faire.append((i, ecrit, dit))
        cout = sum(len(PORTEUSES[a.langue] % d) if " " not in e else len(d) for _, e, d in a_faire)
        print("%s : %d sons a refaire, environ %d credits" % (cle_dossier, len(a_faire), cout))
        if a.a_blanc or not a_faire:
            continue
        cle = cle or generer.cle_api()
        for d in (os.path.join(AVANT, dossier), os.path.join(AVANT, "original", dossier), orig_dir):
            os.makedirs(d, exist_ok=True)
        for i, ecrit, dit in a_faire:
            mot_seul = " " not in ecrit.strip()
            texte = (PORTEUSES[a.langue] % dit) if mot_seul else dit
            if depense + len(texte) > a.plafond:
                print("  plafond atteint ; relancer reprend la suite.")
                break
            final = os.path.join(final_dir, i + ".mp3")
            orig = os.path.join(orig_dir, i + ".mp3")
            # 1. sauvegarde du premier etat
            for src, dst in ((final, os.path.join(AVANT, dossier, i + ".mp3")),
                             (orig, os.path.join(AVANT, "original", dossier, i + ".mp3"))):
                if os.path.exists(src) and not os.path.exists(dst):
                    shutil.copy2(src, dst)
            # 2. la voix
            reglages = dict(generer.REGLAGES, speed=VITESSE_PORTEUSE) if mot_seul else generer.REGLAGES
            try:
                octets = appeler(voix, texte, reglages, cle)
            except generer.TexteBloque:
                print("  ! refuse par ElevenLabs :", ecrit[:60])
                continue
            depense += len(texte)
            brut = orig + ".brut.mp3"
            open(brut, "wb").write(octets)
            if mot_seul:
                ref = os.path.join(AVANT, "original", dossier, i + ".mp3")
                try:
                    # Les bornes de duree se calculent sur ce qui est DIT : « Ce-O-zwei-Ausstoss »
                    # dure plus que les 11 signes de « CO2-Ausstoss » (refuse le 28 oct.). Et pas de
                    # reference : l'ancien son, mal lu, n'a pas la duree de la bonne lecture.
                    recouper(brut, brut + ".coupe", texte=dit)
                except Refus as err:
                    print("  ! decoupe refusee (%s) : %s" % (err, ecrit[:60]))
                    os.remove(brut)
                    continue
                os.replace(brut + ".coupe", brut)
            # 3. l'original devient le brut neuf, puis la normalisation vers le dossier en ligne
            os.replace(brut, orig)
            if not N.normaliser(orig, final + ".norm.mp3"):
                print("  ! normalisation echouee :", ecrit[:60])
                continue
            os.replace(final + ".norm.mp3", final)
            deja[i] = dit
            json.dump(faits, io.open(FAITS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print("  ok %s  %s" % (i, dit.replace("\n", " / ")[:70]))
    print("\n%d credits depenses environ." % depense)


if __name__ == "__main__":
    main()
