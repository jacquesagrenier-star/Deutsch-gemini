# -*- coding: utf-8 -*-
"""Les visages expressifs des conversations. ET C'EST FACTURE : 0,15 $ l'image, chez fal (nano-banana-pro/edit).

    python visuel/conversation/visages.py --montrer        # les prompts seuls, gratuit
    python visuel/conversation/visages.py                  # celles qui manquent
    python visuel/conversation/visages.py Kellnerin-question
    python visuel/conversation/visages.py --refaire Kellnerin-question   # l'ancienne passe en <nom>-rateN.png
    python visuel/conversation/visages.py --web            # refait les webp de la page, gratuit

Decision de Jacques du 11 nov. 2026 (option A, « des visages expressifs ») : dans une conversation, le portrait de la
personne qui parle change selon le moment (accueil, question, surprise, « Wie bitte? ») ; pas de bouche qui bouge.
Lot 1, le cafe : accord « Oui, fabrique » (0,75 $, plafond 1,05 $).

Toujours par RETOUCHE de l'image source de la personne (le meme visage, les memes vetements), au style des portraits
du theme des emotions (visuel/emociones/emociones.py : tete et epaules, fond studio gris clair), pour que tous les
visages des conversations aillent ensemble. Originaux hors du depot et de OneDrive : ~/.wortando/conversation/img/.
La page lit visuel/prototype/conversation/<nom>.webp (480 x 480).
"""
import io, json, os, subprocess, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

EDIT, PRIX = "fal-ai/nano-banana-pro/edit", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "conversation", "img")
WEB = os.path.join(RACINE, "visuel", "prototype", "conversation")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
SOURCES = {
    "Kellnerin": os.path.join(os.path.expanduser("~"), ".wortando", "personnes", "img", "Kellnerin.png"),
    "Tomas": PRINCIPAL + "/visuel/descripcion/img/Tomas.png",
}
# Le meme cadre que les emotions (emociones.py, MEME et PORTRAIT), mot pour mot.
MEME = ("The same person as in the reference picture: exactly the same face, the same age, the same hair, the same skin, "
        "the same glasses or beard if any, the same body and the same clothes. ")
PORTRAIT = (" A photorealistic head-and-shoulders portrait, from the top of the head to the middle of the chest, facing the "
            "camera, centred. Plain light grey studio background with even soft light, nothing else in the picture, no text, "
            "no logos. Natural skin texture, no retouching. The expression is: ")
EXPRESSIONS = {
    "accueil":  "friendly and welcoming, greeting a customer: a warm, open smile, the eyes looking straight into the camera.",
    "question": "asking a question with interest: the eyebrows slightly raised, the head tilted a little to one side, a light "
                "attentive smile, the eyes looking straight into the camera.",
    "surprise": "mildly surprised, taken aback: the eyebrows raised, the eyes wide open, the mouth slightly open, the eyes "
                "looking straight into the camera. Surprise, not fear.",
    "perplexe": "puzzled, not understanding what was just said: one eyebrow raised, a slight frown, the head turned a little to "
                "one side, the lips pressed into a small uncertain line, the eyes looking straight into the camera.",
    "ecoute":   "listening with curiosity: the head tilted slightly, a small friendly closed-mouth smile, the eyebrows a little "
                "raised, attentive eyes looking straight into the camera.",
}
# Lot 1 (le cafe, 11 nov. 2026) : la serveuse n'avait que deux recadrages ou elle regarde en bas ; le voisin (Tomas,
# visages du theme des emotions) n'avait pas d'ecoute.
A_FAIRE = {
    "Kellnerin-accueil": ("Kellnerin", "accueil"),
    "Kellnerin-question": ("Kellnerin", "question"),
    "Kellnerin-surprise": ("Kellnerin", "surprise"),
    "Kellnerin-perplexe": ("Kellnerin", "perplexe"),
    "Tomas-ecoute": ("Tomas", "ecoute"),
}


def prompt(nom):
    _, e = A_FAIRE[nom]
    return MEME + PORTRAIT + EXPRESSIONS[e]


# Un portrait sorti trop large se RECADRE (gratuit) plutot que de se racheter : (gauche, haut, cote) en fractions.
# Kellnerin-accueil (11 nov.) : le modele a recule, la tete au tiers du cadre et un coin de table en bas.
RECADRAGE = {"Kellnerin-accueil": (0.2, 0.08, 0.6), "Kellnerin-question": (0.1, 0.02, 0.8),
             "Kellnerin-surprise": (0.1, 0.02, 0.8), "Kellnerin-perplexe": (0.1, 0.02, 0.8)}


def web(nom):
    """Le webp de la page : carre 480 x 480, centre sur le visage (le portrait est deja tete et epaules)."""
    png = os.path.join(DOSSIER, nom + ".png")
    if not os.path.exists(png):
        return
    os.makedirs(WEB, exist_ok=True)
    g, h, c = RECADRAGE.get(nom, (0, 0, 1))
    vf = "crop='min(iw,ih)*%g':'min(iw,ih)*%g':'iw*%g':'ih*%g',scale=480:480" % (c, c, g, h)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", png, "-vf", vf,
                    "-quality", "85", os.path.join(WEB, nom + ".webp")], check=True)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    noms = args or list(A_FAIRE)
    inconnus = [n for n in noms if n not in A_FAIRE]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    os.makedirs(DOSSIER, exist_ok=True)
    if "--web" in sys.argv:
        for n in noms:
            web(n)
        print("  webp refaits")
        return
    if refaire and not montrer:
        for n in noms:
            png = os.path.join(DOSSIER, n + ".png")
            if os.path.exists(png):
                k = 1
                while os.path.exists(os.path.join(DOSSIER, "%s-rate%d.png" % (n, k))):
                    k += 1
                os.replace(png, os.path.join(DOSSIER, "%s-rate%d.png" % (n, k)))
    a_faire = [n for n in noms if not os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if not montrer and not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = None if montrer else O.cle()
    depots = {}
    for nom in a_faire:
        source = A_FAIRE[nom][0]
        print("\n  %s\n  %s" % (nom, prompt(nom)))
        if montrer:
            continue
        if source not in depots:
            depots[source] = O.deposer(SOURCES[source], "image/png", cle)[0]
        corps = {"prompt": prompt(nom), "image_urls": [depots[source]], "aspect_ratio": "1:1", "resolution": "2K",
                 "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            print("  ECHEC", nom, err)
            io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
                "%s\t%s\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), str(err).replace("\n", " ")))
            continue
        sortie = os.path.join(DOSSIER, nom + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
            "%s\t%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), PRIX))
        io.open(os.path.join(DOSSIER, nom + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": EDIT, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt(nom), "source": SOURCES[source], "prix": PRIX}, ensure_ascii=False, indent=1))
        web(nom)
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
