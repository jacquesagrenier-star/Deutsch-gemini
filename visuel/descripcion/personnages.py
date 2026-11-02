# -*- coding: utf-8 -*-
"""Les douze personnages de « Descripcion fisica » (2 nov. 2026). ET C'EST FACTURE : 0,15 $ l'image, chez fal.

    python visuel/descripcion/personnages.py              # ceux qui manquent (0,15 $ chacun)
    python visuel/descripcion/personnages.py Elena Pablo  # ceux-la seulement
    python visuel/descripcion/personnages.py --montrer    # les prompts seuls, gratuit

Jacques : « entre des vraies personnes et des personnages de bande dessinee », puis la 3D (« 3 »), puis
PHOTOREALISTE, comme Mark et Anna (voir STYLE). Chaque personnage est UNE combinaison precise
(PERSONNAGES, la meme que celle des exercices) : une image ne sert que si elle la respecte, et se refait
sinon. Cadrage identique pour tous (en pied, de la tete aux pieds, petite marge) : l'app les remet a
l'echelle de leur taille (alto, mediano, bajo) devant la toise. Images : visuel/descripcion/img/<Nom>.png.
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

MODELE, PRIX = "fal-ai/nano-banana-pro", 0.15
# 2 nov. : Lucas (pas assez gros) et Tomas (pas assez fort) refaits, les premiers en img/*-rate.png.
# Jacques, apres l'essai en 3D : « on a toujours ete avec des vrais personnages, ca peut etre un peu bizarre » --
# PHOTOREALISTE, la meme planche que Mark et Anna (personnages/Mark.png) : en pied, fond studio gris clair uni,
# lumiere douce, 9:16. Des personnages qu'on pourra reutiliser ailleurs.
STYLE = "A photorealistic photograph of a real person, natural skin texture, no retouching, no studio glamour. "
CADRE = (" Full body from head to feet, standing straight, facing the camera, arms hanging naturally at the sides, "
         "a friendly natural smile. The whole body fills the height of the picture with a small even margin above "
         "the head and below the shoes. Plain light grey studio background with even soft light, nothing else in "
         "the picture, no text.")
# Mark et Anna existent deja (personnages/) : ils ne se regenerent pas. Leur description suit leur fiche
# (scenes/personnages.json) et leur image, pas l'inverse.
EXISTANTS = {"Mark": "personnages/Mark.png", "Anna": "personnages/anna-20260908-0439.png"}
PERSONNAGES = {
    "Mark":   ("m", "alto", "delgado", "corto", "ondulado", "castano", "castanos", [], ""),
    "Anna":   ("f", "mediano", "delgado", "largo", "liso", "castano_claro", None, [], ""),
    "Diego":  ("m", "alto", "delgado", "corto", "rizado", "negro", "castanos", ["gafas"],
               "A tall, thin man of about twenty-five. HAIR: short, tightly curly, black. EYES: brown. Rectangular black-framed glasses. A plain light blue t-shirt, dark blue jeans, white sneakers."),
    "Elena":  ("f", "bajo", "delgado", "largo", "liso", "rubio", "azules", ["pendientes"],
               "A short, slim woman of about twenty-two, petite. HAIR: long, straight, blond, falling well below the shoulders. EYES: clearly blue. Small round gold earrings. A pink t-shirt, black trousers, white sneakers."),
    "Pablo":  ("m", "mediano", "fuerte", "calvo", "liso", "castano", "verdes", ["barba"],
               "A man of about thirty-five, of average height, strong and muscular with broad shoulders. A completely bald, shaved head. EYES: green. A full, thick dark brown beard. A green t-shirt, beige chinos, brown leather shoes."),
    "Marta":  ("f", "alto", "gordo", "largo", "ondulado", "castano", "verdes", ["gafas"],
               "A tall, plump woman of about forty, clearly overweight with a full round figure. HAIR: long, wavy, chestnut brown. EYES: green. Round black-framed glasses. A loose mustard-yellow top, dark green trousers, black flat shoes."),
    "Javier": ("m", "bajo", "gordo", "corto", "liso", "negro", "negros", ["bigote"],
               "A short, plump man of about fifty, clearly overweight with a round belly. HAIR: short, straight, black, combed to the side. EYES: very dark brown, almost black. A thick black moustache, no beard. A red polo shirt, blue jeans, black shoes."),
    "Ines":   ("f", "mediano", "delgado", "corto", "liso", "rojo", "grises", ["tatuaje"],
               "A slim woman of about twenty-eight, of average height. HAIR: short, straight, natural copper-red (a redhead), in a chin-length bob. EYES: grey. Light freckles. A small visible star tattoo on her right forearm. A purple t-shirt, black jeans, white sneakers."),
    "Tomas":  ("m", "alto", "fuerte", "corto", "liso", "rubio", "azules", ["perilla", "pendiente"],
               "A tall, very muscular man of about thirty, like a weightlifter: very broad shoulders, a big chest and thick, muscular arms that fill the sleeves of his t-shirt. HAIR: short, straight, blond. EYES: blue. A small blond goatee on the chin only, no moustache, and one small silver earring in his left ear. A teal t-shirt, light beige trousers, grey sneakers."),
    "Carmen": ("f", "bajo", "gordo", "largo", "rizado", "rojo", "azules", ["gafas"],
               "A short, plump woman of about forty-five, clearly overweight with a round figure. HAIR: long, curly, natural red (a redhead). EYES: blue. Thin red-framed glasses. A navy blue blouse, black trousers, black shoes."),
    "Lucas":  ("m", "alto", "gordo", "corto", "ondulado", "castano_claro", None, ["gafas_sol", "barba"],
               "A tall, obese man of about forty, with a very large round belly that pushes his t-shirt out, wide hips, a double chin and thick arms: clearly fat, not average. HAIR: short, wavy, light brown. Dark sunglasses that hide his eyes, and a short light-brown beard. An orange t-shirt, blue jeans, brown boots."),
    "Rosa":   ("f", "bajo", "fuerte", "largo", "liso", "negro", "castanos", ["tatuaje"],
               "A short, strong athletic woman of about thirty-five with muscular arms. HAIR: long, straight, black, worn loose. EYES: brown. A visible flower tattoo on her left upper arm. A coral sleeveless top, dark grey trousers, white sneakers."),
}
# La taille de chacun, en metres, pour la rangee devant la toise. Mark : « a peu pres 6 pieds » (Jacques, 2 nov.).
METRES = {"Mark": 1.83, "Anna": 1.70, "Diego": 1.90, "Elena": 1.55, "Pablo": 1.74, "Marta": 1.85, "Javier": 1.60,
          "Ines": 1.69, "Tomas": 1.92, "Carmen": 1.53, "Lucas": 1.88, "Rosa": 1.57}
DOSSIER = os.path.join(ICI, "img")


def ecrire_json():
    sortie = {nom: dict(zip(("sexe", "altura", "tam", "largo", "tipo", "color", "ojos", "lleva"), v[:8]), metres=METRES[nom]) for nom, v in PERSONNAGES.items()}
    io.open(os.path.join(ICI, "personnages.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n")


def main():
    montrer = "--montrer" in sys.argv
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or list(PERSONNAGES)
    os.makedirs(DOSSIER, exist_ok=True)
    ecrire_json()
    a_faire = [n for n in noms if n not in EXISTANTS and not os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    cle = None if montrer else O.cle()
    for nom in a_faire:
        prompt = STYLE + PERSONNAGES[nom][8] + CADRE
        print("\n  %s\n  %s" % (nom, prompt))
        if montrer:
            continue
        corps = {"prompt": prompt, "aspect_ratio": "9:16", "resolution": "2K", "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + MODELE, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle)
        sortie = os.path.join(DOSSIER, nom + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(DOSSIER, nom + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": MODELE, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", os.path.relpath(sortie, RACINE), "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
