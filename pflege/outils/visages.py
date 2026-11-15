# -*- coding: utf-8 -*-
"""Les visages des dialogues des Soins, découpés dans les portraits maîtres (aucune image nouvelle, aucune dépense).

    python pflege/outils/visages.py            # écrit visuel/prototype/conversation/soins/<id>.webp
    python pflege/outils/visages.py --planche  # et une planche de contrôle dans ~/.wortando/pflege/

Les portraits maîtres (en pied, fond de studio) vivent hors du dépôt, dans ~/.wortando/pflege/personnages/
(validés par Jacques le 14 nov. 2026, pflege/scenes/portraits.py). Le lecteur des conversations
(visuel/prototype/conversation.html) montre un carré arrondi de 108 px et une vignette de 36 px : un carré de
480 px, centré sur le visage, comme les visages des conversations de Premiers pas.

Un seul visage par personne (« sourire ») : le lecteur retombe sur lui pour toutes les expressions (REPLI).
Dr. Krämer et Frau Kowalski n'ont pas de portrait maître : le lecteur montre leur initiale.
"""
import json
import os
import sys
from urllib.parse import quote

from PIL import Image

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SOURCE = os.path.expanduser("~/.wortando/pflege/personnages")
SORTIE = os.path.join(RACINE, "visuel", "prototype", "conversation", "soins")
COTE = 480

# id du personnage (pflege/sources/noms.json) -> portrait maitre et cadrage de la tete, en pixels du portrait :
# (centre horizontal, haut du crane, hauteur de la tete du crane au menton). Lus a l'oeil sur la planche des
# soignants (planche-soignants.jpg, 1/4 de l'original) et sur une grille des patients : les patients sont
# decoupes dans des scenes, pas sur un fond de studio, et un detecteur ne se fie pas a ces images.
PORTRAITS = {
    "elif":            ("elif.png",         852, 232, 248),
    "yusuf":           ("yusuf.png",        900, 132, 308),
    "jonas":           ("jonas.png",        884, 140, 292),
    "hoffmann":        ("hoffmann.png",     884, 168, 280),
    "sommer":          ("sommer.png",       912, 168, 280),
    "arun":            ("arun.png",         876, 200, 272),
    "olena":           ("olena.png",        868, 192, 320),
    "amira":           ("amira.png",        892, 200, 320),
    "brandt":          ("herr-brandt.png",  263,  40, 193),
    "lehmann":         ("frau-lehmann.png", 172,  30, 210),
    "lehmann_tochter": ("frau-krueger.png", 330,  22, 247),
    "weber":           ("frau-weber.png",   397,  18, 187),
    "schulze":         ("herr-schulze.png", 199,  24, 211),
}


def visage(chemin, cx, haut, tete):
    """Un carre ou la tete fait la moitie de la hauteur, le crane a un dixieme du bord haut (le cadrage des visages
    des conversations de Premiers pas) ; serre contre le bord de l'image quand la tete en est trop pres."""
    im = Image.open(chemin).convert("RGB")
    w, h = im.size
    cote = min(tete * 2.0, w, h)
    g = min(max(0, cx - cote / 2), w - cote)
    t = min(max(0, haut - cote * 0.10), h - cote)
    return im.crop((int(g), int(t), int(g + cote), int(t + cote))).resize((COTE, COTE), Image.LANCZOS)


NOMS = os.path.join(RACINE, "pflege", "sources", "noms.json")
PERSONNES = os.path.join(SORTIE, "personnes.json")


def initiale(nom):
    """Un visage de repli, l'initiale du nom de famille sur un fond doux (personne sans portrait maitre)."""
    lettre = nom.replace("Dr. ", "").replace("Herr ", "").replace("Frau ", "")[:1].upper()
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120"><rect width="120" height="120" fill="#DCE3EA"/>'
           '<text x="60" y="78" font-family="Georgia,serif" font-size="56" text-anchor="middle" fill="#1C2430">%s</text></svg>'
           % lettre)
    return "data:image/svg+xml," + quote(svg)


def ecrire_personnes():
    """conversation/soins/personnes.json : le format des personnes des conversations (nom, voix, visages). Le nom
    affiche est la forme allemande (« Herr Brandt », « Dr. Kraemer ») dans toutes les langues : on apprend l'allemand
    du service, et c'est ainsi que la soignante les appelle."""
    noms = json.load(open(NOMS, encoding="utf-8"))["personnes"]
    sortie = {"_lisez_moi": "DERIVE de pflege/sources/noms.json et des portraits maitres par pflege/outils/visages.py : "
                            "ne pas corriger a la main. Les personnes des dialogues des Soins, au format de "
                            "conversation/personnes.json ; un seul visage (sourire), ou l'initiale sans portrait maitre."}
    for qui, v in noms.items():
        if qui.startswith("_") or v.get("genre") not in ("f", "m"):
            continue
        nom = v.get("de", {}).get("") or v.get("fr", {}).get("") or qui
        image = os.path.join(SORTIE, qui + ".webp")
        visage_ = ("conversation/soins/%s.webp" % qui) if os.path.exists(image) else initiale(nom)
        sortie[qui] = {"nom": {"fr": nom}, "voix": v["genre"], "visages": {"sourire": visage_}}
    with open(PERSONNES, "w", encoding="utf-8", newline="\n") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("  personnes :", len(sortie) - 1)


def main():
    os.makedirs(SORTIE, exist_ok=True)
    faits = {}
    for qui, (f, cx, haut, tete) in PORTRAITS.items():
        src = os.path.join(SOURCE, f)
        if not os.path.exists(src):
            print("  absent :", src)
            continue
        v = visage(src, cx, haut, tete)
        dest = os.path.join(SORTIE, qui + ".webp")
        v.save(dest, "WEBP", quality=82, method=6)
        faits[qui] = v
        print("  %-16s %6d octets" % (qui, os.path.getsize(dest)))
    ecrire_personnes()
    if "--planche" in sys.argv:
        n = len(faits)
        pl = Image.new("RGB", (240 * min(n, 7), 240 * ((n + 6) // 7)), "white")
        for i, v in enumerate(faits.values()):
            pl.paste(v.resize((240, 240)), (240 * (i % 7), 240 * (i // 7)))
        p = os.path.expanduser("~/.wortando/pflege/planche-visages.jpg")
        pl.save(p, quality=85)
        print("  planche :", p)


if __name__ == "__main__":
    main()
