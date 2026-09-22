# -*- coding: utf-8 -*-
"""Ce qu'il reste sur le compte fal, en dollars.

    python video/solde_fal.py

POURQUOI CET OUTIL EXISTE
    Le 22 septembre 2026, une retouche s'est arretee sur un HTTP 403 --
    << User is locked. Reason: Exhausted balance >> -- au moment de
    televerser. Le message arrive de l'API de stockage, pas de celle qui
    facture : rien dans la sortie ne disait COMBIEN il manquait, ni si un
    rechargement etait deja passe. La reponse tient en un appel gratuit.

    Le solde peut etre NEGATIF : fal laisse passer la derniere requete puis
    verrouille le compte. -1,94 $ ce jour-la, donc un rechargement qui
    ramene a zero ne suffit pas a debloquer.

CE QU'IL NE DIT PAS
    Le delai. Un paiement accepte chez fal met parfois quelques minutes a
    lever le verrou : un solde redevenu positif ici et un 403 a l'appel
    suivant ne se contredisent pas, ils se suivent.
"""
import io
import os
import sys
import urllib.error
import urllib.request

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")

URL = "https://rest.alpha.fal.ai/billing/user_balance"


def main():
    req = urllib.request.Request(URL, headers={"Authorization": "Key " + O.cle()})
    try:
        brut = urllib.request.urlopen(req, timeout=20).read().decode().strip()
    except urllib.error.HTTPError as e:
        sys.exit("  HTTP %s : %s" % (e.code, e.read().decode()[:200]))
    try:
        solde = float(brut)
    except ValueError:
        sys.exit("  reponse inattendue : %s" % brut[:200])

    print("  solde fal : %.2f $" % solde)
    if solde <= 0:
        print("  COMPTE VERROUILLE. Recharger sur fal.ai/dashboard/billing --")
        print("  et il faut depasser zero, pas l'atteindre : le solde est")
        print("  negatif de %.2f $." % -solde)
        return 1
    # Les deux depenses courantes, pour savoir ce qu'on peut encore lancer.
    print("  soit environ %d image(s) a 0,15 $" % int(solde / 0.15))
    print("       ou environ %.0f s de clip Seedance a 0,2419 $/s" % (solde / 0.2419))
    print("       ou environ %.0f s d'avatar OmniHuman a 0,16 $/s" % (solde / 0.16))
    return 0


if __name__ == "__main__":
    sys.exit(main())
