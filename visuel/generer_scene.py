# -*- coding: utf-8 -*-
"""L'image d'une scene illustree, chez fal. ET C'EST FACTURE.

    python visuel/generer_scene.py klassenzimmer            # montre, ne paie rien
    python visuel/generer_scene.py klassenzimmer --payer    # 0,15 $

CE QUE C'EST
    Le fond d'une scene interactive : une piece dessinee ou l'on touche les
    objets. Les MOTS NE SONT JAMAIS DANS L'IMAGE -- l'app les pose par-dessus,
    pour qu'une meme image serve l'allemand, le japonais et l'espagnol, et
    qu'on puisse cacher les etiquettes pour s'exercer.

LE PROMPT VIT DANS scenes/<nom>.prompt.txt, PAS ICI
    Meme regle que image_plan.py : une source unique, sinon elle diverge.

PAR DEFAUT IL NE PAIE PAS
    Contrairement a image_plan.py, il faut --payer. Lire le prompt et le
    controle d'abord est gratuit, et c'est la seule occasion de voir qu'on
    s'apprete a envoyer autre chose que ce qu'on croit.

LE CONTROLE EST CELUI DES VIDEOS
    video/verifier_prompt.py, jeu POUR_IMAGE : ce que les images de la serie
    ont deja coute (garde negative, icone nommee par son nom...). Une scene
    n'a pas de lecon a elle tant qu'aucune prise n'a ete refusee.

UNE PRISE PAYEE NE S'ECRASE PAS
    La precedente est rangee en -v1, -v2... avec son recu, et seulement
    APRES que la nouvelle est arrivee (voir image_plan.py, 22 sept. 2026).
"""
import argparse
import io
import json
import os
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402
import verifier_prompt as VP                                # noqa: E402

TEXTE = "fal-ai/nano-banana-pro"
EDIT = "fal-ai/nano-banana-pro/edit"     # 1 a 4 references, meme prix
PRIX = 0.15                      # $ l'image en 2K, comme image_plan.py


def ranger(chemin):
    base, ext = os.path.splitext(chemin)
    i = 1
    while os.path.exists("%s-v%d%s" % (base, i, ext)):
        i += 1
    for vieux, neuf in [(chemin, "%s-v%d%s" % (base, i, ext)),
                        (base + "-fal.json", "%s-v%d-fal.json" % (base, i))]:
        if os.path.exists(vieux):
            os.replace(vieux, neuf)
            print("  prise precedente rangee : %s" % os.path.basename(neuf))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("nom")
    p.add_argument("--format", default="3:4", dest="ratio")
    p.add_argument("--ref", nargs="*", default=[],
                   help="1 a 4 images de reference, dans l'ordre ou le prompt "
                        "les nomme (« the first reference picture »...)")
    p.add_argument("--payer", action="store_true",
                   help="appeler fal ; sans lui, rien n'est envoye")
    a = p.parse_args()

    source = os.path.join(ICI, "scenes", a.nom + ".prompt.txt")
    if not os.path.exists(source):
        sys.exit("  introuvable : %s" % source)
    prompt = io.open(source, encoding="utf-8").read().strip()
    sortie = os.path.join(ICI, "scenes", a.nom + ".png")

    if len(a.ref) > 4:
        sys.exit("  au plus 4 references ; %d donnees." % len(a.ref))
    refs = [r if os.path.isabs(r) else os.path.join(RACINE, r) for r in a.ref]
    for r in refs:
        if not os.path.exists(r):
            sys.exit("  reference introuvable : %s" % r)
    modele = EDIT if refs else TEXTE

    print("scene %s -> %s" % (a.nom, os.path.relpath(sortie, RACINE)))
    print("  modele  %s, %s, 2K" % (modele, a.ratio))
    print("  refs    %s" % (", ".join(os.path.relpath(r, RACINE) for r in refs)
                            or "aucune"))
    print("  cout    %.2f $" % PRIX)
    print("  prompt  %d mots" % len(prompt.split()))
    fautes = VP.dire(a.nom, VP.controler(prompt, image=True), bavard=False)

    if not a.payer:
        print("\n" + "-" * 70 + "\n" + prompt + "\n" + "-" * 70)
        print("\n  RIEN N'A ETE APPELE. --payer pour generer.")
        return
    if fautes and not os.environ.get("WORTANDO_FORCER"):
        sys.exit("\n  %d faute(s) connue(s) : rien n'a ete facture." % fautes)

    cle = O.cle()
    corps = {"prompt": prompt, "aspect_ratio": a.ratio, "resolution": "2K",
             "output_format": "png", "num_images": 1}
    if refs:
        urls = []
        for r in refs:
            u, o = O.deposer(r, "image/png" if r.lower().endswith(".png")
                             else "image/jpeg", cle)
            print("    depose %s (%.1f Mo)" % (os.path.basename(r), o / 1e6))
            urls.append(u)
        corps["image_urls"] = urls
    soum = O._json("https://queue.fal.run/" + modele, cle, corps)
    print("    requete %s" % soum.get("request_id", "?"))
    res = O.attendre(soum["status_url"], soum["response_url"], cle)

    neuve = sortie + ".neuve"
    octets = O.telecharger(res["images"][0]["url"], neuve)
    if os.path.exists(sortie):
        ranger(sortie)
    os.replace(neuve, sortie)
    print("    -> %s  (%.1f Mo, %.2f $)" % (os.path.basename(sortie),
                                            octets / 1e6, PRIX))
    io.open(os.path.splitext(sortie)[0] + "-fal.json", "w",
            encoding="utf-8").write(json.dumps({
                "modele": modele, "request_id": soum.get("request_id"),
                "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "references": [os.path.relpath(r, RACINE) for r in refs],
                "format": a.ratio, "cout_usd": PRIX, "prompt": prompt,
                "description": res.get("description", ""),
            }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
