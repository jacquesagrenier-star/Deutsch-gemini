# -*- coding: utf-8 -*-
"""Le prochain lot a traduire, une ligne par carte. Ne peut pas ecrire.

    python tests/lot_compact.py --langue fa --fichier themes.json --niveau A1 --taille 80

Meme role que lot_langue.py, mais compact : l'allemand, le francais, l'anglais
et la phrase sur une seule ligne separee par « | ». lot_langue.py reste la
version lisible ; celle-ci sert quand le lot est long.
"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langue import Langue

CAT = {"themes.json": "noms", "verbe.json": "verbes", "adjectif.json": "adjectifs",
       "adverbe.json": "adverbes", "redewendung.json": "expressions"}

ap = argparse.ArgumentParser()
ap.add_argument("--langue", required=True)
ap.add_argument("--fichier", required=True)
ap.add_argument("--niveau", required=True)
ap.add_argument("--taille", type=int, default=80)
ap.add_argument("--depuis", type=int, default=0)
a = ap.parse_args()

L = Langue(a.langue)
cartes = L.toutes_les_cartes()[CAT[a.fichier]]
reste = [c for c in cartes if c["niveau"] == a.niveau and not (c.get("cible") or "").strip()]
print("# %s %s : %d a faire" % (a.fichier, a.niveau, len(reste)))
for c in reste[a.depuis:a.depuis + a.taille]:
    if "phrases" in c:
        bouts = " | ".join("%s>%s>%s" % (p["champ"], p["de"], p["fr"]) for p in c["phrases"])
        print("%s | %s | %s" % (c["cle"], c["sens_fr"], bouts))
    else:
        print("%s | %s | %s | %s" % (c["cle"], c["sens_fr"],
                                     c.get("phrase_de", ""), c.get("phrase_fr", "")))
