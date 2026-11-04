# -*- coding: utf-8 -*-
"""Retouche UNE personne de « Descripcion fisica » sans la refaire. ET C'EST FACTURE : 0,15 $ la retouche, chez fal.

    python visuel/descripcion/retoucher.py Elena            # la retouche de RETOUCHES["Elena"]
    python visuel/descripcion/retoucher.py Elena --montrer  # le prompt seul, gratuit

L'original est garde a cote (img/<Nom>-avant<k>.png) ; ensuite, le detourage a refaire (supprimer
img/<Nom>-detoure.png puis detourer.py), web.py, decouverte.py et yeux_personnes.py, qui en derivent.

Elena (3 nov. 2026) : ses donnees disent « pendientes », mais ses cheveux cachaient les boucles d'oreilles.
Jacques : « Retoucher les images » plutot que retirer le mot.
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

MODELE, PRIX = "fal-ai/nano-banana-pro/edit", 0.15
RETOUCHES = {
    # 1re retouche ratee (img/Elena-rate1.png) : les cheveux etaient partis derriere les epaules, elle n'avait
    # plus l'air d'avoir les cheveux longs (« largo » dans ses donnees). Seul le haut des cheveux bouge.
    "Elena": ("Edit this photograph, change only the hair right at her ears: tuck the hair just behind both ears at "
              "the top, so that both earlobes are clearly visible, and she wears small round gold hoop earrings "
              "that are clearly visible on both earlobes. Below the ears, the hair stays EXACTLY as it is now: very "
              "long, straight, blond, falling IN FRONT of both shoulders and down over the chest to the middle of "
              "the t-shirt, as in the original. Keep everything else exactly the same: the same woman, the same face, the same blue eyes, "
              "the same smile, the same pink t-shirt, black trousers and white sneakers, the same pose, the same "
              "framing from head to feet, the same plain light grey studio background and light. Photorealistic, "
              "no text."),
}
DOSSIER = os.path.join(ICI, "img")


def main():
    montrer = "--montrer" in sys.argv
    noms = [a for a in sys.argv[1:] if not a.startswith("--")]
    for nom in noms:
        prompt = RETOUCHES[nom]
        png = os.path.join(DOSSIER, nom + ".png")
        print("\n  %s (%.2f $)\n  %s" % (nom, PRIX, prompt))
        if montrer:
            continue
        cle = O.cle()
        url = O.deposer(png, "image/png", cle)[0]
        corps = {"prompt": prompt, "image_urls": [url], "aspect_ratio": "9:16", "resolution": "2K",
                 "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + MODELE, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        k = 1
        while os.path.exists(os.path.join(DOSSIER, "%s-avant%d.png" % (nom, k))):
            k += 1
        os.replace(png, os.path.join(DOSSIER, "%s-avant%d.png" % (nom, k)))
        O.telecharger(res["images"][0]["url"], png)
        io.open(os.path.join(DOSSIER, nom + "-retouche-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": MODELE, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "source": "%s-avant%d.png" % (nom, k), "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", os.path.relpath(png, RACINE), "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
