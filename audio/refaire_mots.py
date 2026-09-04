# -*- coding: utf-8 -*-
"""Refait les mots isoles avec une porteuse allemande, puis les recoupe.

    python audio/refaire_mots.py --blanc
    python audio/refaire_mots.py --niveaux A1,A2 --plafond 40000
    python audio/refaire_mots.py --porteuse "Wort: %s."

LE DEFAUT QU'ON REPARE. `eleven_multilingual_v2` deduit la langue du texte
qu'on lui envoie. Sur un mot court et isole il n'a presque rien pour la
deduire : « neu » sort a la francaise, « jung » avec un j qui n'est pas
allemand. Constate a l'oreille le 3 septembre 2026 par une germanophone, sur
des fichiers deja en ligne.

CE QUI A ETE ESSAYE ET ECARTE, pour ne pas y revenir :
  - regenerer avec une autre graine : le defaut se repete. Ce n'est pas le
    tirage.
  - monter la stabilite a 0,95 : sans effet. Ce n'est pas la distribution.
  - `language_code: "de"` : l'API le VALIDE (un code invente est refuse avec
    « Model 'eleven_multilingual_v2' does not support language_code 'zz' »)
    mais la lecture ne change pas a l'oreille. Accepte, sans effet.
  - le mot dans une phrase allemande : JUSTE. C'est la seule chose qui marche,
    et c'est ce que fait ce script.

CE QUI NE BOUGE PAS. Le fichier produit garde le nom `sha1(mot)[:16].mp3` :
l'app cherche exactement la meme empreinte et ne saura jamais que le son a ete
fabrique autrement. En revanche `AUDIO_REVISION` DOIT etre incremente dans
index.html apres le depot, sinon les appareils garderont l'ancien son douze
mois -- Hosting sert ces fichiers en `immutable, un an`.

L'ANCIEN FICHIER EST SAUVEGARDE AVANT D'ETRE REMPLACE, dans
mp3_original_avant_porteuse/. Un mot mal prononce reste un mot audible ; une
recoupe ratee peut ne rien dire du tout. On doit pouvoir revenir en arriere
sans regenerer ni repayer.
"""
import argparse
import io
import json
import os
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generer import VOIX, FORMAT, REGLAGES, SEED, MODELES, cle_api  # noqa: E402
from essai_prononciation import appeler                            # noqa: E402
from recouper import recouper, Refus                               # noqa: E402

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGINAUX = os.path.join(RACINE, "audio", "mp3_original")
SAUVEGARDE = os.path.join(RACINE, "audio", "mp3_original_avant_porteuse")
BRUTS = os.path.join(RACINE, "audio", "mp3_porteuse_brut")
MANIFESTE = os.path.join(RACINE, "audio", "manifest.json")
REGISTRE = os.path.join(RACINE, "audio", "refaits_porteuse.json")
# Le modele n'est plus en dur : il se choisit en ligne de commande et doit
# TOUJOURS etre celui du reste du corpus. La table vient de generer.py, pour
# qu'il n'y ait qu'un seul endroit ou les identifiants de modeles existent.
MODELE_DEFAUT = "flash"

PORTEUSE_DEFAUT = "Wort: %s."

# LA VITESSE N'EST PAS UN CONFORT, ELLE REPARE UN EFFET DE BORD.
# Dans la porteuse, le mot est dit au debit de la conversation ; genere
# seul il etait dit en forme de citation, plus posee. « Besprechung »
# passait de 0,71 s a 0,55 s -- 23 % plus vite, et ca s'entend sur un mot
# de quatre syllabes. A 0,80 il retrouve exactement 0,71 s. Choisi a
# l'oreille le 3 septembre 2026, sur des mots courts ET longs.
VITESSE_DEFAUT = 0.80


def registre_lu():
    if os.path.exists(REGISTRE):
        with io.open(REGISTRE, encoding="utf-8") as f:
            return json.load(f)
    return {"faits": [], "refuses": {}}


def registre_ecrit(r):
    with io.open(REGISTRE, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1)
        f.write(u"\n")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--niveaux", default="A1,A2")
    p.add_argument("--porteuse", default=PORTEUSE_DEFAUT,
                   help="gabarit, %%s a la place du mot")
    p.add_argument("--vitesse", type=float, default=VITESSE_DEFAUT,
                   help="0.80 rend au mot son debit de citation")
    p.add_argument("--plafond", type=int, default=50000,
                   help="credits maximum pour cette execution")
    p.add_argument("--modele", default=MODELE_DEFAUT, choices=sorted(MODELES),
                   help="doit etre le meme que celui du corpus")
    p.add_argument("--max", type=int, default=0, help="limiter le nombre de mots")
    p.add_argument("--blanc", action="store_true")
    a = p.parse_args()

    if "%s" not in a.porteuse:
        print("La porteuse doit contenir %s a la place du mot."); return 1

    modele_id = MODELES[a.modele][0]
    niveaux = [n.strip() for n in a.niveaux.split(",")]
    with io.open(MANIFESTE, encoding="utf-8") as f:
        manifeste = json.load(f)

    reg = registre_lu()
    faits = set(reg["faits"])
    # LE GENRE « mot » DU MANIFESTE N'EST PAS UN MOT ISOLE. Les expressions de
    # redewendung.json y sont rangees comme « mot » : « Bis morgen », « Danke,
    # gut », « Das freut mich ». Sur A1, 235 des 340 refus etaient de celles-la.
    #
    # Les emballer dans « Wort: ... » est inutile ET DANGEREUX. Inutile parce
    # qu'une expression porte deja son contexte : elle n'a jamais eu le probleme
    # de detection de langue que la porteuse corrige. Dangereux parce que le
    # decoupage garde tout ce qui suit la plus grande pause -- sur « Wort: Bis
    # morgen. », il peut ne garder que « morgen » et perdre « Bis ». Le garde-fou
    # sur la duree en attrape une partie, mais ce n'est pas sa raison d'etre.
    #
    # On filtre donc sur l'ESPACE, pas sur le genre declare.
    mots = [e for e in manifeste
            if e["niveau"] in niveaux and e["genre"] == "mot"
            and " " not in e["texte"].strip()
            and e["id"] not in faits]
    if a.max:
        mots = mots[:a.max]

    cout = sum(len(a.porteuse % e["texte"]) for e in mots)
    surcout = len(a.porteuse % "")
    print("  porteuse : %-16s (%d caracteres de contexte par mot)"
          % (a.porteuse, surcout))
    print("  vitesse  : %.2f" % a.vitesse)
    print("  %d mot(s) a refaire, %d deja faits" % (len(mots), len(faits)))
    print("  cout : %d credits  (plafond de cette execution : %d)"
          % (cout, a.plafond))
    if reg["refuses"]:
        print("  %d refus a reprendre a la main (voir refaits_porteuse.json)"
              % len(reg["refuses"]))

    if a.blanc:
        print("\n  (a blanc -- rien n'a ete appele)")
        for e in mots[:8]:
            print("     %-20s %s" % (e["texte"], a.porteuse % e["texte"]))
        return 0
    if not mots:
        print("\n  rien a faire.")
        return 0

    for d in (SAUVEGARDE, BRUTS):
        os.makedirs(d, exist_ok=True)
    cle = cle_api()

    reglages = dict(REGLAGES, speed=a.vitesse)
    depense = poses = refuses = 0
    debut = time.time()
    try:
        for e in mots:
            texte = a.porteuse % e["texte"]
            prix = len(texte)
            if depense + prix > a.plafond:
                print("\n  plafond atteint. Relance : la reprise est automatique.")
                break

            brut = os.path.join(BRUTS, "%s__v%s.mp3"
                                % (e["id"], ("%.2f" % a.vitesse).replace(".", "")))
            if not os.path.exists(brut):
                with open(brut, "wb") as f:
                    f.write(appeler(texte, reglages, SEED, cle, modele_id))
                depense += prix

            cible = os.path.join(ORIGINAUX, e["id"] + ".mp3")
            ancien = cible if os.path.exists(cible) else None
            try:
                # La duree de l'ancien fichier sert de garde-fou : il etait mal
                # prononce, pas mal decoupe, donc sa duree est une reference
                # propre a CE mot.
                n = recouper(brut, brut + ".coupe", reference=ancien,
                             texte=e["texte"])
            except Refus as err:
                reg["refuses"][e["id"]] = {"mot": e["texte"], "raison": str(err)}
                refuses += 1
                print("  ! %-18s %s" % (e["texte"], err))
                continue

            if ancien and not os.path.exists(os.path.join(SAUVEGARDE, e["id"] + ".mp3")):
                shutil.copy2(ancien, os.path.join(SAUVEGARDE, e["id"] + ".mp3"))
            shutil.move(brut + ".coupe", cible)
            reg["faits"].append(e["id"])
            poses += 1

            if poses % 25 == 0:
                ecoule = time.time() - debut
                reste = (len(mots) - poses) * ecoule / max(poses, 1)
                print("  %5d/%d  %6d credits  reste ~%d min"
                      % (poses, len(mots), depense, int(reste / 60)))
                registre_ecrit(reg)
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("\n  interrompu -- ce qui est fait est conserve.")
    finally:
        registre_ecrit(reg)

    print("\n  %d pose(s), %d refus, %d credits depenses"
          % (poses, refuses, depense))
    print("\n  ENSUITE, DANS CET ORDRE :")
    print("    python audio/normaliser.py --niveaux %s" % a.niveaux)
    print("    python audio/deposer.py")
    print("    incrementer AUDIO_REVISION dans index.html  <-- sans quoi rien")
    print("    ne change sur les appareils pendant douze mois.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
