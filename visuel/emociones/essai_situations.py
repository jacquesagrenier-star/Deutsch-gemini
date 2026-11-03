# -*- coding: utf-8 -*-
"""PLANCHE D'ESSAI (3 nov. 2026) : les emotions qu'un visage seul dit mal, montrees par une situation. Accord de
Jacques : « Oui, vas-y. Fabrique. Planche d'essai de 6 images » -- 0,90 $, plafond 1,20 $. ET C'EST FACTURE.
Chaque image essaie une facon de faire ; nos personnes, leur identite gardee par retouche (nano-banana-pro/edit,
l'image de la personne en reference). Rien n'est publie : Jacques choisit ensuite les facons qui marchent.

    python visuel/emociones/essai_situations.py            # celles qui manquent
    python visuel/emociones/essai_situations.py --planche  # la planche, gratuite

Originaux : C:/Users/jacqu/.wortando/emociones/essai/.
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import emociones as E                                        # noqa: E402  (SOURCES, omnihuman, la cle)
O = E.O
DOSSIER = os.path.join(os.path.dirname(E.DOSSIER), "essai")
SOURCES = dict(E.SOURCES, Mia=E.FAMILLE + "/Mia.png")
STYLE = (" A photorealistic photograph of a real everyday scene, natural light, natural colours, no text, no logos, no "
         "captions. The faces and gestures are easy to read.")
MEME = "exactly the same face, hair, age and clothes as in the reference picture"
# (nom, idee testee en francais, personnes en reference, scene) ; « depuis » : une image deja faite en reference
ESSAIS = [
    ("1-inquiet", "Inquiet, par la situation : Anna, la nuit, regarde son téléphone ; l'horloge marque 1 h", ["Anna"],
     "The woman from the reference picture (" + MEME + ") sits on the edge of her bed at night, in a dark bedroom lit only by "
     "the glow of her phone screen. She stares at the phone with a deeply worried face: furrowed brow, biting her lip. On the "
     "bedside table, a round analogue clock shows clearly that it is one o'clock (the hour hand on 1, the minute hand on 12)."),
    ("2-fier", "Fier, par la situation : Ben brandit sa médaille devant Gisela", ["Ben", "Gisela"],
     "In a cosy living room, the boy from the first reference picture (" + MEME + ") proudly holds up a gold medal on a ribbon, "
     "beaming, chin up, chest out, in front of the elderly woman from the second reference picture (" + MEME + "), who claps her "
     "hands and smiles at him, delighted."),
    ("3-gene", "Gêné, par la situation : Lucas renverse son café en pleine réunion", ["Lucas"],
     "During a work meeting at a long office table, the man from the reference picture (" + MEME + ", but he has taken off his "
     "sunglasses, which lie on the table, so that his eyes are visible) has just knocked over his cup of coffee: the coffee "
     "spills across the table and onto the papers. He blushes deeply, with an awkward, embarrassed smile and one hand on the "
     "back of his neck, while his colleagues around the table look at him."),
    ("4-decu-avant", "Déçu, avant / après (1) : Mia ouvre son cadeau en souriant", ["Mia"],
     "In a bright living room, the little girl from the reference picture (" + MEME + ") sits at a table and eagerly tears the "
     "colourful wrapping paper off a birthday present with a big ribbon, smiling excitedly, her eyes bright with expectation."),
    ("5-decu-apres", "Déçu, avant / après (2) : elle découvre des chaussettes", ["Mia"],
     "Exactly the same scene, the same room, the same table and the same little girl as in the second reference picture: she "
     "has now opened the present and holds up a pair of plain grey socks. She is disappointed: her smile has gone, the corners "
     "of her mouth turn down, her shoulders drop, the torn wrapping paper on the table.", "4-decu-avant"),
    ("6-jaloux", "Jaloux, par le contraste : Ben a une glace, Mia le regarde", ["Ben", "Mia"],
     "On a sunny park bench, the boy from the first reference picture (" + MEME + ") happily licks a big ice-cream cone. Next to "
     "him, the little girl from the second reference picture (" + MEME + ") has nothing: arms crossed, she stares at his ice "
     "cream with a jealous, sulky face, her lower lip pushed out."),
]


def planche():
    from PIL import Image, ImageDraw, ImageFont
    W, H, L = 600, 450, 110
    police = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 21)
    gras = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
    P = Image.new("RGB", (3 * W + 4 * 20, 2 * (H + L) + 3 * 20 + 60), (247, 248, 250))
    d = ImageDraw.Draw(P)
    d.text((20, 18), "Planche d'essai : les émotions par une situation (rien n'est publié)", font=gras, fill=(28, 36, 48))
    for k, (nom, idee, *_rest) in enumerate(ESSAIS):
        x, y = 20 + (k % 3) * (W + 20), 70 + (k // 3) * (H + L + 20)
        f = os.path.join(DOSSIER, nom + ".png")
        if os.path.exists(f):
            im = Image.open(f).convert("RGB")
            w, h = im.size
            c = min(w, h * W // H)
            im = im.crop(((w - c) // 2, 0, (w + c) // 2, c * H // W)).resize((W, H), Image.LANCZOS)
            P.paste(im, (x, y))
        else:
            d.rectangle((x, y, x + W, y + H), fill=(220, 224, 230))
            d.text((x + 20, y + H // 2), "refusée par le filtre de fal", font=police, fill=(200, 71, 58))
        d.text((x, y + H + 8), str(k + 1) + ".", font=gras, fill=(168, 106, 14))
        mots, ligne, yy = idee.split(" "), "", y + H + 8
        for m in mots:                                   # le texte se replie sur la largeur de l'image
            if d.textlength(ligne + " " + m, font=police) > W - 34:
                d.text((x + 30, yy), ligne.strip(), font=police, fill=(28, 36, 48)); yy += 27; ligne = ""
            ligne += " " + m
        d.text((x + 30, yy), ligne.strip(), font=police, fill=(28, 36, 48))
    sortie = os.path.join(DOSSIER, "planche-essai.jpg")
    P.save(sortie, quality=88)
    print("  ->", sortie)


def main():
    os.makedirs(DOSSIER, exist_ok=True)
    if "--planche" in sys.argv:
        return planche()
    if not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(E.PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    for essai in ESSAIS:
        nom, idee, gens, scene = essai[:4]
        depuis = essai[4] if len(essai) > 4 else None
        sortie = os.path.join(DOSSIER, nom + ".png")
        if os.path.exists(sortie):
            continue
        urls = [O.deposer(SOURCES[g], "image/png", cle)[0] for g in gens]
        if depuis:
            urls.append(O.deposer(os.path.join(DOSSIER, depuis + ".png"), "image/png", cle)[0])
        corps = {"prompt": scene + STYLE, "image_urls": urls, "aspect_ratio": "4:3", "resolution": "2K",
                 "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + E.EDIT, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            print("  ECHEC", nom, err)
            io.open(os.path.join(E.DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
                "%s\tessai-%s\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), err))
            continue
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(E.DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
            "%s\tessai-%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), E.PRIX))
        print("  ->", sortie, "(%.2f $)" % E.PRIX)
    planche()


if __name__ == "__main__":
    main()
