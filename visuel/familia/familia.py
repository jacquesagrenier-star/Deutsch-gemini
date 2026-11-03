# -*- coding: utf-8 -*-
"""La famille d'Anna, premier « theme illustre » apres « Decrire une personne » (2 nov. 2026). ET C'EST FACTURE :
0,15 $ l'image, chez fal.

    python visuel/familia/familia.py              # celles qui manquent (0,15 $ chacune)
    python visuel/familia/familia.py Heinz Mia    # celles-la seulement
    python visuel/familia/familia.py --montrer    # les prompts seuls, gratuit
    python visuel/familia/familia.py --json       # familia.json seul, gratuit

POURQUOI LA FAMILLE D'ANNA ET PAS CELLE DE MARK. La regle de coherence des scenes (15 oct. 2026) : « famille en
Allemagne = celle d'Anna » ; celle de Mark est a Montreal (pere franco-canadien, mere allemande, scenes/
personnages.json). Anna n'a pas de compagnon : elle est la tante de Ben et Mia, jamais une mere ou une epouse.
Et en espagnol l'histoire tient aussi : Anna suit le cours d'espagnol de la VHS (episode 05), elle y presente sa
famille.

Meme planche que « Decrire une personne » (visuel/descripcion/personnages.py) : photorealiste, en pied, fond de
studio gris clair, 9:16 ; detourees (detourer.py) puis rangees a l'echelle de leur taille. Anna n'est pas
regeneree : son image de guichet (personnages/anna-20260908-0439.png) donne, par retouche, son image de tous les
jours (Anna-quotidien) -- la regle 3 de la fiche, jamais du texte seul. Images : visuel/familia/img/ (hors depot).
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

MODELE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15
STYLE = "A photorealistic photograph of a real person, natural skin texture, no retouching, no studio glamour. "
CADRE = (" Full body from head to feet, standing straight, facing the camera, arms hanging naturally at the sides, "
         "a friendly natural smile. The whole body fills the height of the picture with a small even margin above "
         "the head and below the shoes. Plain light grey studio background with even soft light, nothing else in "
         "the picture, no text, no logos.")
ANNA_SOURCE = "personnages/anna-20260908-0439.png"
ANNA_RETOUCHE = ("The same woman as in the reference picture: exactly the same face, the same hair, the same build "
                 "and height. Only her clothes change, and she holds nothing: she is off duty, in everyday clothes, "
                 "a simple soft blue-grey knit sweater, dark blue jeans and white sneakers; no lanyard, no badge, no "
                 "uniform, nothing in her hands." + CADRE)

# L'ARBRE. Chaque personne : sexe, taille en metres, parents (le couple), conjoint, et sa description.
# Heinz et Gisela -> Peter (marie a Monika) et Sabine (mariee a Frank).
# Peter et Monika -> Jan (marie a Katrin), Anna, Lena.  Sabine et Frank -> Felix, Sophie.  Jan et Katrin -> Ben, Mia.
# Les traits de famille : les Becker (Heinz, Peter, Sabine, Jan, Anna, Lena) ont les yeux clairs et des cheveux
# blond fonce a chatain clair, comme Anna.
FAMILLE = {
    "Heinz":  ("m", 1.76, None, "Gisela", 82,
               "An elderly man of about eighty-two, of Northern European appearance, slim, standing upright. Short white hair, thinning on top. Light blue eyes. Clean-shaven. Thin metal-framed glasses. A beige knitted cardigan over a light blue checked shirt, grey trousers, brown leather shoes."),
    "Gisela": ("f", 1.60, None, "Heinz", 79,
               "An elderly woman of about seventy-nine, of Northern European appearance, short and slightly plump. Short, softly curled silver-white hair. Light grey-blue eyes. A lilac blouse under an open dark grey knitted cardigan, a dark grey skirt to below the knee, comfortable black shoes."),
    "Peter":  ("m", 1.82, "Heinz", "Monika", 61,
               "A tall, slim man of about sixty, of Northern European appearance. Short grey hair that was once dark blond, and a neatly trimmed short grey beard. Light blue eyes. A navy blue crew-neck sweater over a white collared shirt, beige chinos, brown shoes."),
    "Monika": ("f", 1.66, None, "Peter", 58,
               "A slim woman of about fifty-eight, of Northern European appearance, of average height. Straight light brown hair to the chin, with a few grey strands. Green eyes. Small pearl earrings. A sage-green blouse, dark blue jeans, brown ballet flats."),
    "Sabine": ("f", 1.68, "Heinz", "Frank", 56,
               "A woman of about fifty-six, of Northern European appearance, of average height and build. Short ash-blond hair in a neat bob. Light blue eyes. Red-framed reading glasses. A burgundy sweater, black trousers, black shoes."),
    "Frank":  ("m", 1.86, None, "Sabine", 59,
               "A tall, broad and sturdy man of about fifty-nine with a small belly. Short dark brown hair going grey at the temples, clean-shaven. Brown eyes. A dark green zip-up fleece jacket over a grey t-shirt, blue jeans, brown hiking shoes."),
    "Jan":    ("m", 1.85, "Peter", "Katrin", 34,
               "A tall, athletic man of about thirty-four, of Northern European appearance. Short dark-blond hair and a short, well-kept dark-blond beard. Light blue eyes. A plain charcoal grey hooded sweatshirt, blue jeans, white sneakers."),
    "Katrin": ("f", 1.68, None, "Jan", 33,
               "A slim woman of about thirty-three, of average height. Long dark brown hair in a ponytail. Brown eyes. A mustard-yellow cardigan over a white t-shirt, black jeans, white sneakers."),
    "Anna":   ("f", 1.70, "Peter", None, 30, None),
    "Lena":   ("f", 1.65, "Peter", None, 25,
               "A slim young woman of about twenty-five, of Northern European appearance. Long, straight blond hair, lighter than her sister's, worn loose. Light blue eyes and a few light freckles. A turquoise sweater, light grey trousers, white sneakers."),
    "Felix":  ("m", 1.80, "Sabine", None, 28,
               "A slim young man of about twenty-eight, of average to tall height. Short dark brown hair, slightly messy. Brown eyes. Round tortoiseshell glasses. A rust-orange corduroy shirt over a white t-shirt, dark grey trousers, brown leather sneakers."),
    "Sophie": ("f", 1.63, "Sabine", None, 22,
               "A young woman of about twenty-two, slim, rather short. Shoulder-length wavy dark brown hair. Brown eyes. A bright yellow sweater, light blue jeans, white sneakers."),
    "Ben":    ("m", 1.22, "Jan", None, 7,
               "A boy of about seven, of Northern European appearance. Short, slightly tousled dark-blond hair. Light blue eyes. A plain red t-shirt, blue jeans, blue and white sneakers."),
    "Mia":    ("f", 1.03, "Jan", None, 4,
               "A little girl of about four, of Northern European appearance. Light brown hair in two small pigtails. Brown eyes. A light blue cotton dress, white tights and red shoes."),
}
# « parents » ne nomme qu'un des deux parents de sang ; l'autre est son conjoint.
DOSSIER = os.path.join(ICI, "img")


def ecrire_json():
    sortie = {}
    for nom, (sexe, metres, parent, conjoint, age, _) in FAMILLE.items():
        parents = [parent, FAMILLE[parent][3]] if parent else []
        sortie[nom] = {"sexe": sexe, "metres": metres, "age": age, "parents": [p for p in parents if p], "conjoint": conjoint}
    io.open(os.path.join(ICI, "familia.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n")


def main():
    montrer = "--montrer" in sys.argv
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or list(FAMILLE)
    os.makedirs(DOSSIER, exist_ok=True)
    ecrire_json()
    if "--json" in sys.argv:
        return
    nom_fichier = lambda n: "Anna-quotidien" if n == "Anna" else n
    a_faire = [n for n in noms if not os.path.exists(os.path.join(DOSSIER, nom_fichier(n) + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    cle = None if montrer else O.cle()
    for nom in a_faire:
        prompt = ANNA_RETOUCHE if nom == "Anna" else STYLE + FAMILLE[nom][5] + CADRE
        print("\n  %s\n  %s" % (nom, prompt))
        if montrer:
            continue
        corps = {"prompt": prompt, "aspect_ratio": "9:16", "resolution": "2K", "output_format": "png", "num_images": 1}
        modele = MODELE
        if nom == "Anna":
            modele = EDIT
            corps["image_urls"] = [O.deposer(os.path.join(RACINE, ANNA_SOURCE), "image/png", cle)[0]]
        soum = O._json("https://queue.fal.run/" + modele, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle)
        sortie = os.path.join(DOSSIER, nom_fichier(nom) + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(DOSSIER, nom_fichier(nom) + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": modele, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", os.path.relpath(sortie, RACINE), "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
