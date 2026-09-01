# -*- coding: utf-8 -*-
"""Combien de credits restent, et est-ce que ca suffit pour finir.

    python audio/solde.py
    python audio/solde.py --niveaux A1,A2

Un seul appel, en lecture seule, a /v1/user/subscription. La cle est lue par
generer.py, elle ne transite ni par la ligne de commande ni par l'affichage.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generer                                          # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")


def solde():
    """Le solde, ou None si la cle n'a pas le droit de le lire.

    Une cle limitee au seul Text to Speech se voit refuser cet appel avec un
    401 -- alors qu'elle genere parfaitement. Confondre les deux ferait croire
    a une cle morte et enverrait en recreer une pour rien.
    """
    req = urllib.request.Request(
        "https://api.elevenlabs.io/v1/user/subscription",
        headers={"xi-api-key": generer.cle_api()})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            return None
        raise
    return (d["character_count"], d["character_limit"],
            d.get("next_character_count_reset_unix"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--niveaux", default="A1,A2")
    a = p.parse_args()

    infos = solde()
    reste = None
    if infos is None:
        print("\n  Le solde n'est pas lisible : cette cle n'a que le droit de")
        print("  generer (Text to Speech). Ce n'est PAS une panne — la")
        print("  generation, elle, fonctionne. Le solde se lit sur")
        print("  elevenlabs.io, en haut du menu de profil.")
    else:
        utilise, limite, remise = infos
        reste = limite - utilise
        print("\n  credits : %d utilises sur %d — il reste %d"
              % (utilise, limite, reste))
        if remise:
            import datetime
            d = datetime.datetime.fromtimestamp(remise)
            print("  remise a zero le %s" % d.strftime("%d %B %Y"))

    _, entrees = generer.a_produire(a.niveaux.split(","))
    taux = generer.MODELES["v2"][1]
    cout = int(sum(len(e["texte"]) for e in entrees) * taux)
    print("\n  niveaux %s : %d fichiers a produire, environ %d credits"
          % (a.niveaux, len(entrees), cout))
    if not entrees:
        print("  -> rien a faire, ces niveaux sont complets.")
    elif reste is None:
        # Sans le solde, on ne peut pas dire s'il suffit -- mais on peut donner
        # la commande avec le bon plafond, qui est la seule chose qui manque.
        print("  -> lance, avec un plafond au moins egal a ce cout :")
        print("     python audio/generer.py --niveaux %s --plafond %d"
              % (a.niveaux, cout + 1000))
    elif cout <= reste:
        print("  -> le solde suffit. Lance :")
        print("     python audio/generer.py --niveaux %s --plafond %d"
              % (a.niveaux, reste))
    else:
        print("  -> il manque %d credits. Le script s'arretera en route ;"
              % (cout - reste))
        print("     la reprise plus tard repartira exactement d'ou il s'arrete.")


if __name__ == "__main__":
    main()
