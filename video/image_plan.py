# -*- coding: utf-8 -*-
"""L'image fixe d'un plan, chez fal. ET C'EST FACTURE.

    python video/image_plan.py --scene 02-beim-buergeramt --plan 1 --montrer
    python video/image_plan.py --scene 02-beim-buergeramt --plan 1 \\
        --ref personnages/Mark-dos.png personnages/Mark.png

CE QUE CA REMPLACE
    Artlist / Framing, dont les credits sont epuises. Le meme geste : un
    prompt, des images de reference, une image verticale en retour.

DEUX MODELES, ET LE CHOIX N'EST PAS QUE FINANCIER
    sans --ref   fal-ai/nano-banana-pro          texte -> image
    avec --ref   fal-ai/nano-banana-pro/edit     1 a 4 references
    0,15 $ l'image dans les deux cas (le 4K double ; on reste en 2K).

    ⚠️ TOUT PLAN QUI CONTIENT UN PERSONNAGE PASSE PAR --ref, meme s'il est
       petit et de dos. La coherence de personnage est LE defaut recurrent du
       projet : les deux Annas du 8 septembre, le plan de dos de l'aeroport
       le 12. Un plan sans ancrage ne rate pas a moitie, il rate entierement,
       et il se voit au montage, pas au retour.

LE PROMPT SE LIT DANS A-TOURNER.txt, IL NE SE RECOPIE PAS
    Bloc « PROMPT D'IMAGE (Framing) », jusqu'au premier ⚠️, « Reference » ou
    « PROMPT DE MOUVEMENT ». Le fichier reste la source unique : un prompt
    recopie ici divergerait le jour ou l'on corrige la-bas.

    ⚠️ TOUJOURS LIRE --montrer AVANT DE PAYER. C'est gratuit, ca affiche le
       prompt exact et les references, et c'est la seule occasion de voir
       qu'on s'apprete a envoyer autre chose que ce qu'on croit.

LA CLE N'EST PAS DANS LE CODE
    fal.secret a la racine (ignore par git) ou FAL_KEY.
"""
import argparse
import io
import json
import os
import re
import sys
import time
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

TEXTE = "fal-ai/nano-banana-pro"
EDIT = "fal-ai/nano-banana-pro/edit"
PRIX = 0.15                      # $ l'image, releve sur la fiche du modele
MIMES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
         ".webp": "image/webp"}


def bloc_plan(txt, n):
    """Le bloc d'un plan dans A-TOURNER.txt, de son titre au suivant."""
    m = re.search(r"^PLAN %02d\b.*?(?=^PLAN \d\d\b|\Z)" % n, txt, re.S | re.M)
    if not m:
        sys.exit("  A-TOURNER.txt n'a pas de « PLAN %02d »." % n)
    return m.group(0)


def prompt_image(bloc, n):
    """Le prompt de Framing : de son titre jusqu'a ce qui n'est plus lui.

    ⚠️ On s'arrete au premier ⚠️, « Reference » ou « PROMPT DE MOUVEMENT ».
    Ces lignes-la sont des consignes A NOUS, pas au modele -- les envoyer
    ferait payer une image ou le generateur essaie d'obeir a du francais."""
    m = re.search(r"PROMPT D'IMAGE \(Framing\)\s*\n(.*?)"
                  r"(?=\n\s*(?:⚠|REFERENCE|Reference|PROMPT DE MOUVEMENT)|\Z)",
                  bloc, re.S)
    if not m or not m.group(1).strip():
        sys.exit("  plan %02d : pas de bloc « PROMPT D'IMAGE (Framing) »." % n)
    return "\n".join(l.rstrip() for l in m.group(1).strip().splitlines())


def nom_image(bloc, n):
    m = re.search(r"Image a nommer\s*:\s*(\S+)", bloc)
    return m.group(1) if m else "plan%02d.png" % n


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--scene", default="02-beim-buergeramt")
    p.add_argument("--plan", type=int, required=True)
    p.add_argument("--ref", nargs="*", default=[],
                   help="1 a 4 images de reference, chemins depuis la racine")
    p.add_argument("--format", default="9:16", dest="ratio")
    p.add_argument("--resolution", default="2K", choices=["1K", "2K", "4K"])
    p.add_argument("--montrer", action="store_true",
                   help="afficher le prompt et les references, ne rien appeler")
    p.add_argument("--refaire", action="store_true")
    a = p.parse_args()

    ep = os.path.join(RACINE, "video", "episode-%s" % a.scene)
    feuille = os.path.join(ep, "A-TOURNER.txt")
    if not os.path.exists(feuille):
        sys.exit("  introuvable : %s" % feuille)
    bloc = bloc_plan(io.open(feuille, encoding="utf-8").read(), a.plan)
    prompt = prompt_image(bloc, a.plan)
    nom = nom_image(bloc, a.plan)
    sortie = os.path.join(ep, "01-images", nom)

    if len(a.ref) > 4:
        sys.exit("  au plus 4 references ; %d donnees." % len(a.ref))
    refs = []
    for r in a.ref:
        c = r if os.path.isabs(r) else os.path.join(RACINE, r)
        if not os.path.exists(c):
            sys.exit("  reference introuvable : %s" % c)
        refs.append(c)

    modele = EDIT if refs else TEXTE
    cout = PRIX * (2 if a.resolution == "4K" else 1)
    print("plan %02d -> %s" % (a.plan, os.path.relpath(sortie, RACINE)))
    print("  modele     %s" % modele)
    print("  format     %s, %s" % (a.ratio, a.resolution))
    print("  references %s" % (", ".join(os.path.basename(r) for r in refs)
                               or "aucune (texte seul)"))
    print("  cout       %.2f $" % cout)
    print("  prompt     %d mots, %d caracteres" % (len(prompt.split()), len(prompt)))

    if a.montrer:
        print("\n" + "-" * 70)
        print(prompt)
        print("-" * 70)
        print("\n  RIEN N'A ETE APPELE. Relance sans --montrer pour generer.")
        return

    if os.path.exists(sortie) and not a.refaire:
        sys.exit("  %s existe deja. --refaire pour la remplacer." % nom)

    cle = O.cle()
    corps = {"prompt": prompt, "aspect_ratio": a.ratio,
             "resolution": a.resolution, "output_format": "png",
             "num_images": 1}
    if refs:
        urls = []
        for c in refs:
            mime = MIMES.get(os.path.splitext(c)[1].lower(), "image/png")
            u, o = O.deposer(c, mime, cle)
            print("    depose %s (%.1f Mo)" % (os.path.basename(c), o / 1e6))
            urls.append(u)
        corps["image_urls"] = urls

    soum = O._json("https://queue.fal.run/" + modele, cle, corps)
    print("    requete %s" % soum.get("request_id", "?"))
    res = O.attendre(soum["status_url"], soum["response_url"], cle)

    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    octets = O.telecharger(res["images"][0]["url"], sortie)
    print("    -> %s  (%.1f Mo, %.2f $)" % (nom, octets / 1e6, cout))

    recu = os.path.splitext(sortie)[0] + "-fal.json"
    io.open(recu, "w", encoding="utf-8").write(json.dumps({
        "modele": modele, "request_id": soum.get("request_id"),
        "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "references": [os.path.relpath(r, RACINE) for r in refs],
        "format": a.ratio, "resolution": a.resolution,
        "cout_usd": cout, "prompt": prompt,
        "description": res.get("description", ""),
    }, ensure_ascii=False, indent=1))
    if res.get("description"):
        print("    le modele decrit : %s" % res["description"][:200])


if __name__ == "__main__":
    main()
