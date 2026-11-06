"""Les photos du DTZ (Lesen surtout) : celles des petites annonces, des brochures, et l'illustration de chaque Teil.
ET C'EST FACTURE : 0,15 $ l'image chez fal (nano-banana-pro).

    python visuel/prototype/dtz/outils/images.py --montrer          # les prompts et le cout, gratuit
    python visuel/prototype/dtz/outils/images.py                    # celles qui manquent
    python visuel/prototype/dtz/outils/images.py annonce-schreibtisch biblio-innen   # celles-la seulement
    python visuel/prototype/dtz/outils/images.py --web              # refait les webp de la page, gratuit

ACCORD DE JACQUES, 4 nov. 2026 (« Oui, les deux ») : environ 33 images, 5 $, plafond 7 $. Le lot se fait par
petits paquets, chaque image VERIFIEE contre sa description avant le paquet suivant (regle des themes illustres).

LES REGLES DE CES IMAGES
  - AUCUN TEXTE LISIBLE : les documents de Lesen sont mis en page en HTML ; une image ne porte que la photo (une
    IA ecrit mal l'allemand, et un texte dans une image ne se relit pas). Chaque prompt le redit.
  - Des photos ordinaires, comme celles qu'on poste avec une petite annonce : pas de studio, pas de marque.
  - Mark et Anna JAMAIS ensemble sur une image (decision du 3 nov.) ; Mark ne se regenere pas, son image sert de
    reference (retouche nano-banana-pro/edit) ; un lieu deja connu (sa cuisine, son salon) reprend ses meubles et
    ses couleurs (video/LIEUX.md, decision du 3 nov.).
Originaux en PNG dans outils/img/ (hors depot) ; la page lit les webp de images/ (largeur 720 px).
"""
import io
import json
import os
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
DTZ = os.path.dirname(ICI)
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(DTZ)))
PRINCIPAL = os.path.normpath(os.path.join(DEPOT, "..", "..", ".."))
if not os.path.exists(os.path.join(PRINCIPAL, "fal.secret")):
    PRINCIPAL = DEPOT
sys.path.insert(0, os.path.join(DEPOT, "video"))
import omnihuman as O                                        # noqa: E402

MODELE, PRIX = "fal-ai/nano-banana-pro", 0.15
ORIGINAUX = os.path.join(ICI, "img")
WEB = os.path.join(DTZ, "images")
SANS_TEXTE = (" Absolutely no text, no letters, no numbers, no signs, no labels and no logos anywhere in the picture;"
              " no brand names.")
ANNONCE = ("An ordinary photograph taken with a smartphone for a classified ad in Berlin, natural daylight, slightly "
           "imperfect framing, realistic, not a studio photo, no people.")

# nom : (format, description). Serie 1 d'abord ; les series suivantes s'ajoutent ici.
IMAGES = {
    "annonce-schreibtisch": ("4:3", "A used solid wooden desk, about 120 by 60 centimetres, standing empty in a bright "
                             "room of an old Berlin apartment with a worn wooden floor and a white wall."),
    "annonce-pasta": ("4:3", "In a cooking school kitchen, the hands of several adults roll out fresh pasta dough on a "
                      "floured wooden table, a bowl of tomatoes and basil beside them; faces are not visible."),
    "annonce-thai": ("4:3", "A wok of stir-fried vegetables with lemongrass, red chillies and lime halves on the steel "
                     "counter of a teaching kitchen, a gas flame under the wok."),
    "annonce-familienwohnung": ("4:3", "The bright, empty living room of an old Berlin apartment building (Altbau): "
                                "high white ceiling, wooden floor, two tall windows and an open glass door to a large "
                                "balcony with flower boxes, photographed for a rental listing."),
    "annonce-zweizimmer": ("4:3", "A small, bright, modern room of a rental flat: a glass door to a narrow balcony over "
                           "a green courtyard with trees, a simple fitted kitchen corner in the background, empty."),
    "annonce-herrenrad": ("4:3", "A used black men's city bicycle with 28-inch wheels, a front light and a rear rack, "
                          "leaning against a red brick wall in a Berlin backyard with cobblestones."),
    "brochure-bibliothek": ("16:9", "The bright interior of a modern public library in Berlin: rows of colourful "
                            "bookshelves, wooden reading tables, two readers seen from behind, large windows with "
                            "trees outside."),
}
PROMPT_EN_PLUS = {n: ANNONCE for n in IMAGES if n.startswith("annonce-")}


def prompt(nom):
    fmt, desc = IMAGES[nom]
    return (PROMPT_EN_PLUS.get(nom, "A realistic photograph, natural light.") + " " + desc + SANS_TEXTE)


def web():
    from PIL import Image
    os.makedirs(WEB, exist_ok=True)
    for nom in IMAGES:
        src = os.path.join(ORIGINAUX, nom + ".png")
        if not os.path.exists(src):
            continue
        im = Image.open(src).convert("RGB")
        if im.width > 720:
            im = im.resize((720, round(im.height * 720 / im.width)), Image.LANCZOS)
        im.save(os.path.join(WEB, nom + ".webp"), "WEBP", quality=80, method=6)
        print("  images/%s.webp" % nom)


def main():
    if "--web" in sys.argv:
        web()
        return
    montrer = "--montrer" in sys.argv
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or list(IMAGES)
    os.makedirs(ORIGINAUX, exist_ok=True)
    a_faire = [n for n in noms if not os.path.exists(os.path.join(ORIGINAUX, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if not montrer:
        os.environ.setdefault("FAL_KEY", io.open(os.path.join(PRINCIPAL, "fal.secret"), encoding="utf-8-sig").read().strip())
    cle = None if montrer else O.cle()
    for nom in a_faire:
        p = prompt(nom)
        print("\n  %s (%s)\n  %s" % (nom, IMAGES[nom][0], p))
        if montrer:
            continue
        corps = {"prompt": p, "aspect_ratio": IMAGES[nom][0], "resolution": "1K", "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + MODELE, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle)
        sortie = os.path.join(ORIGINAUX, nom + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(ORIGINAUX, nom + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": MODELE, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": p, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  -> outils/img/%s.png (%.2f $)" % (nom, PRIX))


if __name__ == "__main__":
    main()
