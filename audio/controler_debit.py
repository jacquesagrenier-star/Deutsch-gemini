# -*- coding: utf-8 -*-
"""Cherche les prises ou ElevenLabs a dit AUTRE CHOSE que le texte.

    python audio/controler_debit.py --scene 02-beim-buergeramt

POURQUOI CET OUTIL EXISTE, ET CE QU'IL AURAIT EVITE
    Le 14 septembre, trois prises sur dix-neuf etaient fausses et LES TROIS ONT
    ETE TROUVEES PAR L'OREILLE DE JACQUES, pas par la mesure :

      plan 14   « Welche Papiere brauche ich? » en 10,22 s -- phrase repetee
      plan 16   « Die ... was, bitte? » en 7,80 s -- phrase repetee
      plan 08   un « ahhhh » invente, absent du script

    Le 08 est le cas qui justifie ce fichier. Je l'avais MESURE a 1,9
    syllabe/seconde contre 6 a 7 ailleurs -- l'anomalie etait sous mes yeux,
    chiffree -- et je l'ai attribuee a une pause dramatique. Une mesure qu'on
    regarde sans seuil n'arbitre rien.

    LA CAUSE ETAIT LA MEME POUR LES TROIS : generees sans previous_text /
    next_text, et le modele remplit quand il est seul devant une phrase courte.
    Le remede est dans generer.py ; ce controle est le filet.

DEUX MESURES, ET POURQUOI PAS UNE
    mots/s        lisible, mais l'allemand compose fausse tout : le plan 15 dit
                  « Wohnungsgeberbestaetigung », vingt-six lettres comptees
                  pour UN mot -- il sort a 66 % de la mediane sans rien avoir.
    signes/s      immunise contre les composes. C'est celle qui decide.

⚠️ LE SEUIL EST RELATIF AU LOCUTEUR, pas absolu. Aurora narre plus lentement
   que Mark ne parle, et le fonctionnaire a ete choisi pour son debit lent --
   5,51 syllabes/s contre 7,03, c'est ce qui le distingue de Mark a l'oreille.
   Une cible unique les declarerait tous anormaux.

⚠️ ET CE CONTROLE NE REMPLACE PAS L'ECOUTE. Il attrape le remplissage, qui
   change la DUREE. Une prise a la bonne duree mais mal jouee passera -- et
   c'est l'oreille de Jacques qui tranche, comme depuis le 3 septembre.

RIEN N'EST APPELE, RIEN N'EST FACTURE.
"""
import argparse
import io
import json
import os
import statistics
import sys

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                          # noqa: E402

# Releves sur l'episode 2 refait avec contexte, ou les dix-neuf sont saines.
# Un remplissage divise le debit par trois ou plus : 0,60 laisse passer les
# variations de jeu et attrape ce qu'on cherche.
PLANCHER = 0.60
PLAFOND = 1.70


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--scene", required=True)
    a = p.parse_args()

    d = json.loads(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                           encoding="utf-8").read())
    dossier = os.path.join(RACINE, "audio", "scenes", a.scene)
    ff = M.ffmpeg()

    par = {}
    for plan in d["plans"]:
        f = os.path.join(dossier, "%02d-%s.mp3" % (plan["n"], plan["locuteur"]))
        if not os.path.exists(f):
            sys.exit("  voix absente : %s" % f)
        debut, fin, _ = M.parole(ff, f)
        voix = fin - debut
        if voix <= 0:
            sys.exit("  plan %d : aucune voix detectee." % plan["n"])
        signes = len(plan["de"].replace(" ", ""))
        par.setdefault(plan["locuteur"], []).append(
            (plan["n"], signes / voix, len(plan["de"].split()) / voix,
             voix, plan["de"]))

    suspects = []
    for loc in sorted(par):
        v = par[loc]
        med = statistics.median(x[1] for x in v)
        print("  %-10s mediane %.1f signes/s, sur %d plans" % (loc, med, len(v)))
        for n, sps, mps, voix, texte in sorted(v):
            r = sps / med
            mauvais = r < PLANCHER or r > PLAFOND
            print("    plan %-3d %5.1f signes/s  %3.0f%%  %5.2fs  %s%s"
                  % (n, sps, r * 100, voix, texte[:34],
                     "  <-- SUSPECT" if mauvais else ""))
            if mauvais:
                suspects.append((n, r, texte))
        print()

    if not suspects:
        print("  Aucune prise suspecte. (L'oreille reste juge du JEU.)")
        return
    print("  %d prise(s) suspecte(s) -- ECOUTER avant de monter :" % len(suspects))
    for n, r, texte in suspects:
        print("    plan %-3d %3.0f%% du debit habituel  « %s »" % (n, r * 100, texte))
    print("\n  Si une prise repete ou invente, la refaire :")
    print("    python audio/refaire_plan.py --scene %s --plan N --pour-de-vrai"
          % a.scene)
    sys.exit(1)


if __name__ == "__main__":
    main()
