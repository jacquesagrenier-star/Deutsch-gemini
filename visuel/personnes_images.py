# -*- coding: utf-8 -*-
"""Les visages de la fiche commune (visuel/personnes.json) : les prenoms reserves et les figurants. ET C'EST FACTURE :
0,15 $ l'image, chez fal. Accord de Jacques (7 nov. 2026) : « Oui, fais-les » (la coherence des personnages, environ
5,40 $ avec les situations des emotions et le cafe de « Manger et gouter »).

    python visuel/personnes_images.py               # ceux qui manquent (0,15 $ chacun)
    python visuel/personnes_images.py Hugo Nuria    # ceux-la seulement
    python visuel/personnes_images.py --montrer     # les prompts seuls, gratuit
    python visuel/personnes_images.py --refaire Hugo   # l'ancienne passe en <nom>-rate<N>.png

Pourquoi : un prenom reserve portait le visage d'une des douze de Descripcion (Hugo avait celui de Diego), si bien
qu'un meme visage avait deux prenoms dans le theme des emotions. Chacun a maintenant le sien, decrit dans la fiche.
Meme planche que Descripcion (descripcion/personnages.py) : photorealiste, en pied, fond studio gris clair, 9:16. Ce
sont les SOURCES des retouches (nano-banana-pro/edit) des themes : emociones.py, manger.py.
Originaux hors du depot et de OneDrive : ~/.wortando/personnes/img/ (personnes.VISAGES).
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402
sys.path.insert(0, ICI)
import personnes as PERS                                     # noqa: E402

MODELE, PRIX = "fal-ai/nano-banana-pro", 0.15
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
STYLE = "A photorealistic photograph of a real person, natural skin texture, no retouching, no studio glamour. "
CADRE = (" Full body from head to feet, standing straight, facing the camera, arms hanging naturally at the sides, "
         "a calm, neutral, natural expression. The whole body fills the height of the picture with a small even margin above "
         "the head and below the shoes. Plain light grey studio background with even soft light, nothing else in "
         "the picture, no text.")


def a_faire_liste():
    """{cle: description} : les prenoms reserves qui ont leur visage, et les figurants."""
    out = {}
    for k in list(PERS.RESERVES) + list(PERS.FIGURANTS):
        if PERS.image_propre(k):
            out[k] = (PERS.RESERVES.get(k) or PERS.FIGURANTS[k])["description"]
    return out


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    tout = a_faire_liste()
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or list(tout)
    inconnus = [n for n in noms if n not in tout]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    os.makedirs(PERS.VISAGES, exist_ok=True)
    if refaire and not montrer:
        for n in noms:
            png = os.path.join(PERS.VISAGES, n + ".png")
            if os.path.exists(png):
                k = 1
                while os.path.exists(os.path.join(PERS.VISAGES, "%s-rate%d.png" % (n, k))):
                    k += 1
                os.replace(png, os.path.join(PERS.VISAGES, "%s-rate%d.png" % (n, k)))
    a_faire = [n for n in noms if not os.path.exists(os.path.join(PERS.VISAGES, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if not montrer and not os.environ.get("FAL_KEY") and not os.path.exists(os.path.join(RACINE, "fal.secret")):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = None if montrer else O.cle()
    for nom in a_faire:
        prompt = STYLE + tout[nom] + CADRE
        print("\n  %s\n  %s" % (nom, prompt))
        if montrer:
            continue
        corps = {"prompt": prompt, "aspect_ratio": "9:16", "resolution": "2K", "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + MODELE, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        sortie = os.path.join(PERS.VISAGES, nom + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(PERS.VISAGES, "depenses.log"), "a", encoding="utf-8").write(
            "%s\t%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), PRIX))
        io.open(os.path.join(PERS.VISAGES, nom + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": MODELE, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
