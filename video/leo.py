# -*- coding: utf-8 -*-
"""Leo, le heros des scenes de Lisbonne (1er nov. 2026). ET C'EST FACTURE : 0,15 $ l'image, chez fal.

    python video/leo.py face           # Leo de face -> personnages/Leo.png (0,15 $)
    python video/leo.py vues           # depuis personnages/Leo.png : gauche, droite, dos (0,45 $)
    python video/leo.py ... --montrer  # le prompt seul, gratuit

Jacques, 1er nov. 2026 : « Fais les cinq au complet. » -- les cinq propositions de
portugais/lisbonne/HISTOIRE-LISBONNE.md, dont Leo et sa depense. Leo Tavares, 24 ans, de Montreal
(le Petit Portugal), petit-fils d'une Acorienne, debutant en portugais, passe un an a Lisbonne.

Meme planche que Camille (video/camille.py) : en pied, fond studio gris clair uni, lumiere douce,
9:16. Les vues se font TOUJOURS depuis l'image de face, jamais en chaine ; le prompt des vues ne
redecrit ni le visage ni la tenue : c'est l'image qui les porte.
"""
import io
import json
import os
import sys
import time
sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

TEXTE = "fal-ai/nano-banana-pro"
EDIT = "fal-ai/nano-banana-pro/edit"
PRIX = 0.15
DOSSIER = os.path.join(RACINE, "personnages")
# Ses objets a lui (HISTOIRE-LISBONNE.md, section 1) : le coton ouate bleu des Canadiens -- sans
# logo, une marque dessinee se deforme et ne s'efface pas -- et le foulard brode de sa grand-mere.
FACE = ("A photorealistic young man of twenty-four from Montreal, whose grandmother came from the Azores, "
        "with an ordinary, approachable face, the kind of person you would ask for directions. Full body, "
        "standing, facing the camera, on a plain light grey studio background with even soft light. Average "
        "height, lean build. A friendly, slightly shy half-smile that reaches his eyes. HAIR: dark brown, thick "
        "and a little wavy, short on the sides and longer on top, slightly untidy. EYES: dark brown, warm and "
        "curious. Light olive skin, a short dark stubble, thick dark eyebrows. CLOTHES: a plain royal-blue "
        "hooded sweatshirt with a red band across the chest, open over a plain white t-shirt, straight "
        "dark-blue jeans, white canvas sneakers; a soft cream cotton scarf with small blue embroidered flowers "
        "loosely knotted around his neck. POSTURE: upright and relaxed, arms hanging naturally at his sides, "
        "weight settled evenly.")
VUE_BASE = ("The same young man as in the reference image, same face, same hair, same build, same clothes, "
            "same scarf. Full body, standing, on a plain light grey studio background with even soft light. "
            "Photorealistic. POSTURE: upright and relaxed, arms hanging naturally at his sides, weight settled "
            "evenly. ")
VUES = {
    # Dire ce qu'on VOIT (la premiere « gauche » de Camille regardait a droite, 31 oct.).
    "gauche": "VIEW: seen from the side, in full profile. He has turned so that his nose points toward the LEFT "
              "edge of the picture: we see his left cheek, his left shoulder and his left arm, and the back of his "
              "head is on the right side of the picture.",
    "droite": "VIEW: seen from the side, in full profile. He has turned so that his nose points toward the RIGHT "
              "edge of the picture: we see his right cheek, his right shoulder and his right arm, and the back of "
              "his head is on the left side of the picture.",
    "dos": "VIEW: seen from directly behind, back to camera, head facing away.",
}


def generer(modele, prompt, sortie, refs=()):
    """Comme video/camille.py (31 oct. 2026), recopie pour que ce fichier se suffise."""
    cle = O.cle()
    corps = {"prompt": prompt, "aspect_ratio": "9:16", "resolution": "2K", "output_format": "png", "num_images": 1}
    if refs:
        corps["image_urls"] = [O.deposer(r, "image/png", cle)[0] for r in refs]
    soum = O._json("https://queue.fal.run/" + modele, cle, corps)
    res = O.attendre(soum["status_url"], soum["response_url"], cle)
    O.telecharger(res["images"][0]["url"], sortie)
    io.open(os.path.splitext(sortie)[0] + "-fal.json", "w", encoding="utf-8").write(json.dumps({
        "modele": modele, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "prompt": prompt, "references": [os.path.relpath(r, RACINE) for r in refs], "prix": PRIX},
        ensure_ascii=False, indent=1))
    print("  ->", os.path.relpath(sortie, RACINE), "(%.2f $)" % PRIX)


def main():
    montrer = "--montrer" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--montrer"]
    face = os.path.join(DOSSIER, "Leo.png")
    if args == ["face"]:
        travaux = [(TEXTE, FACE, face, ())]
    elif args == ["vues"]:
        if not os.path.exists(face):
            sys.exit("  pas de " + face)
        travaux = [(EDIT, VUE_BASE + v, os.path.join(DOSSIER, "Leo-%s.png" % n), (face,)) for n, v in VUES.items()]
    else:
        sys.exit(__doc__)
    print("  %d image(s), %.2f $" % (len(travaux), len(travaux) * PRIX))
    for modele, prompt, sortie, refs in travaux:
        print("\n  %s  %s\n  %s" % (modele, os.path.basename(sortie), prompt))
        if montrer:
            continue
        if os.path.exists(sortie):
            sys.exit("  %s existe deja : rien de paye." % sortie)
        generer(modele, prompt, sortie, refs)


if __name__ == "__main__":
    main()
