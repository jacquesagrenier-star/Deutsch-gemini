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

# ---------------------------------------------------------------------------------------------------------------
# Lot 2 (20 nov. 2026, decision 1843330 : « go Les expressions des visages (environ 184 images, environ 28 $) ») :
# toutes les expressions que les 80 conversations demandent (champ « air ») et qu'aucun visage n'a encore, compte
# fait visage par visage (un visage peut tenir plusieurs roles). Les noms d'expression sont ceux de la page
# (personnes.json) ; « sourire » et « attentive » reprennent les textes « accueil » et « ecoute » du lot 1.
EXPRESSIONS["sourire"] = EXPRESSIONS["accueil"]
EXPRESSIONS["attentive"] = EXPRESSIONS["ecoute"]
EXPRESSIONS["amuse"] = ("amused, enjoying a light joke: a broad, genuine smile showing the teeth a little, the eyes "
                        "narrowed and crinkled with laughter, the head tilted back very slightly, the eyes looking "
                        "straight into the camera.")
# La base : 185 images (45 visages). Ce qui manque, ou n'a que l'image du sourire.
LOT2_BASE = {
    "Arjun": ["question", "attentive", "perplexe", "amuse"],
    "Aylin": ["question", "attentive", "perplexe", "amuse"],
    "Birgit": ["attentive", "surprise"],
    "Bogdan": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Brigitte": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Bruno": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Carlos": ["question"],
    "Carmen": ["question", "attentive"],
    "Claire": ["question", "attentive", "perplexe", "amuse"],
    "Claudia": ["question", "attentive", "perplexe", "amuse"],
    "Dagmar": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Daria": ["question", "attentive", "perplexe", "amuse"],
    "Diego": ["surprise", "amuse"],
    "Elena": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Freya": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Grace": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Hugo": ["question", "attentive", "perplexe", "amuse"],
    "Ines": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Irene": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Javier": ["question", "surprise", "amuse"],
    "Keira": ["question", "attentive", "surprise"],
    "Kellnerin": ["amuse"],
    "Kwame": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Linh": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Mario": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Marta": ["question", "attentive", "surprise"],
    "Mei": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Nikos": ["question", "attentive", "perplexe"],
    "Noemi": ["question", "attentive", "surprise", "perplexe"],
    "Nuria": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Omar": ["question", "attentive", "perplexe", "amuse"],
    "Pablo": ["question", "surprise", "perplexe"],
    "Paula": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Priya": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Rainer": ["question", "attentive", "perplexe", "amuse"],
    "Renate": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Romy": ["question", "attentive", "perplexe"],
    "Rosa": ["question", "attentive", "perplexe", "amuse"],
    "Selin": ["question", "attentive", "surprise", "perplexe"],
    "Sergio": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Silvia": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Stefan": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Vanessa": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Yasmin": ["question", "attentive", "surprise", "perplexe", "amuse"],
    "Zoe": ["question", "attentive", "surprise", "perplexe", "amuse"],
}
# Option B, 10 images : les expressions EMPRUNTEES au theme des emotions qui disent autre chose que le moment de la
# conversation -- Pablo « attentive » = Pablo qui baille (cansado), « amuse » = Pablo qui brandit une medaille
# (orgulloso) ; Javier « perplexe » = bras croises, fache (enfadado), « attentive » = la main sur le front
# (preocupado) ; Diego « perplexe » = il se ronge les ongles (nervioso), « question » et « attentive » = inquiet
# (preocupado) ; Carmen, Marta et Tomas « amuse » = un rire gene cache derriere la main (avergonzado).
LOT2_EMPRUNTS = {
    "Pablo": ["attentive", "amuse"], "Javier": ["attentive", "perplexe"],
    "Diego": ["question", "attentive", "perplexe"], "Carmen": ["amuse"], "Marta": ["amuse"], "Tomas": ["amuse"],
}
# Option C, 9 images : un vrai sourire pour les neuf reserves, dont le portrait « neutre » (recadre de leur image en
# pied) est serieux, parfois severe (Carlos, Silvia), alors qu'il sert de « sourire » a l'accueil de la personne.
LOT2_SOURIRES = {n: ["sourire"] for n in ("Bruno", "Carlos", "Hugo", "Irene", "Mario", "Nuria", "Paula", "Sergio",
                                          "Silvia")}
# Ce que Jacques a accorde (rempli APRES son mot dans la fenetre de la session, jamais avant) : les parties du lot
# et le plafond en dollars, reprises comprises. Tant que PLAFOND_LOT2 vaut 0, le script refuse de payer le lot 2.
LOT2_ACCORDE = ("base", "emprunts", "sourires")   # Jacques, 20 nov. 2026 : « Tout : 204, 33,60 $ max »
PLAFOND_LOT2 = 33.60
LOT2 = {"base": LOT2_BASE, "emprunts": LOT2_EMPRUNTS, "sourires": LOT2_SOURIRES}

# Les sources : le portrait carre des 27 (portraits.py), l'image en pied des reserves et des douze de Descripcion.
_PERS = os.path.join(os.path.expanduser("~"), ".wortando", "personnes", "img")
for _n in ("Bruno", "Carlos", "Hugo", "Irene", "Mario", "Nuria", "Paula", "Sergio", "Silvia"):
    SOURCES[_n] = os.path.join(_PERS, _n + ".png")
for _n in ("Carmen", "Diego", "Elena", "Ines", "Javier", "Marta", "Pablo", "Rosa"):
    SOURCES[_n] = PRINCIPAL + "/visuel/descripcion/img/%s.png" % _n
for _n in LOT2_BASE:
    if _n not in SOURCES:
        SOURCES[_n] = os.path.join(DOSSIER, _n + "-neutre.png")
# Daria et Linh sont sorties assises a une table : la source est leur portrait RECADRE (portraits.py), sinon la
# table reviendrait dans chaque expression.
SOURCE_RECADREE = {"Daria": (0.14, 0.08, 0.72), "Linh": (0.07, 0.02, 0.86)}
NOMS_LOT2 = {}
for _partie, _table in LOT2.items():
    for _n, _es in _table.items():
        for _e in _es:
            A_FAIRE["%s-%s" % (_n, _e)] = (_n, _e)
            NOMS_LOT2["%s-%s" % (_n, _e)] = _partie
# Les vetements et accessoires a garder, ecrits : un casque-micro ou des lunettes ne sont pas « des vetements ».
MEME = MEME.replace("the same glasses or beard if any", "the same glasses, headset, earrings or beard if any")


def prompt(nom):
    _, e = A_FAIRE[nom]
    return MEME + PORTRAIT + EXPRESSIONS[e]


def source(n):
    """Le fichier televerse : la source, recadree d'abord si elle l'exige (gratuit, ~/.wortando)."""
    if n not in SOURCE_RECADREE:
        return SOURCES[n]
    from PIL import Image
    sortie = os.path.join(DOSSIER, n + "-source.png")
    if not os.path.exists(sortie):
        g, h, c = SOURCE_RECADREE[n]
        im = Image.open(SOURCES[n])
        cote = min(im.size) * c
        im.crop((int(im.width * g), int(im.height * h), int(im.width * g + cote), int(im.height * h + cote))).save(sortie)
    return sortie


def depense_lot2():
    """Ce que le lot 2 a deja coute, lu dans depenses.log (les ECHEC ne sont pas factures)."""
    log = os.path.join(DOSSIER, "depenses.log")
    if not os.path.exists(log):
        return 0.0
    total = 0.0
    for l in io.open(log, encoding="utf-8"):
        c = l.rstrip("\n").split("\t")
        if len(c) >= 4 and c[1] in NOMS_LOT2 and c[3] != "ECHEC" and c[0] >= "2026-11-20":
            total += float(c[3])
    return total


def controle_fond(nom):
    """Instrument gratuit : l'ecart-type du bord de l'image (3 % de chaque cote). Un fond de studio uni reste bas ; un
    bureau, une chaise ou une table le font monter. Ne juge ni le visage ni l'expression : la planche le fait.
    ⚠️ Il ne voit PAS la brume du bas (20 nov. : Elena, Sergio, Irene, depuis une source en pied -- le corps se perd
    dans un fondu gris ou flottent les chaussures) : le bas est occupe par les vetements, on ne peut pas le mesurer
    comme un fond. Regarder le bas de chaque image sur la planche."""
    from PIL import Image, ImageStat
    im = Image.open(os.path.join(DOSSIER, nom + ".png")).convert("L").resize((400, 400))
    b = 12
    bandes = [im.crop((0, 0, 400, b)), im.crop((0, 0, b, 300)), im.crop((400 - b, 0, 400, 300))]
    return max(ImageStat.Stat(x).stddev[0] for x in bandes)


# Un portrait sorti trop large se RECADRE (gratuit) plutot que de se racheter : (gauche, haut, cote) en fractions.
# Kellnerin-accueil (11 nov.) : le modele a recule, la tete au tiers du cadre et un coin de table en bas.
RECADRAGE = {"Kellnerin-accueil": (0.2, 0.08, 0.6), "Kellnerin-question": (0.1, 0.02, 0.8),
             "Kellnerin-surprise": (0.1, 0.02, 0.8), "Kellnerin-perplexe": (0.1, 0.02, 0.8)}
# Lot 2 (20 nov.) : Elena, retouchee depuis son image EN PIED, est sortie a mi-corps, et en « attentive » et
# « surprise » le bas du corps se perd dans une brume ou flottent ses baskets. Le haut est juste : on recadre ces
# deux-la au-dessus de la brume (un recadrage commun aux cinq serrait trop les tetes deja grandes).
RECADRAGE["Elena-attentive"] = (0.12, 0.0, 0.76)
RECADRAGE["Elena-surprise"] = (0.14, 0.02, 0.72)
# Javier « perplexe » est sorti a mi-corps (son image source est en pied) : l'expression est juste, le cadre non.
RECADRAGE["Javier-perplexe"] = (0.2, 0.03, 0.56)
# Sergio (cinq expressions, pas le sourire) et Irene (le sourire) : la meme brume aux chaussures flottantes, des 77 %
# de la hauteur. Meme cause qu'Elena : une source EN PIED, que le modele termine en fondu plutot que de couper.
for _e in ("question", "attentive", "surprise", "perplexe", "amuse"):
    RECADRAGE["Sergio-" + _e] = (0.14, 0.03, 0.72)
RECADRAGE["Irene-sourire"] = (0.12, 0.02, 0.76)
# Et Diego (question), Mario (question, sourire), Nuria (amuse), Rosa (attentive, perplexe, amuse) : la meme brume,
# de 80 a 85 % de la hauteur. Onze images sur 204, toutes depuis une source EN PIED, aucune depuis un portrait carre.
RECADRAGE.update({"Diego-question": (0.08, 0.0, 0.84), "Mario-question": (0.1, 0.02, 0.8),
                  "Mario-sourire": (0.12, 0.02, 0.76), "Nuria-amuse": (0.1, 0.04, 0.8),
                  "Rosa-attentive": (0.12, 0.02, 0.76), "Rosa-perplexe": (0.1, 0.02, 0.8),
                  "Rosa-amuse": (0.12, 0.02, 0.76)})


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


def planche(visage, sortie):
    """La source et toutes les expressions d'un visage cote a cote, legendees : le controle a l'oeil (meme personne,
    bonne expression, cadre, fond, aucun texte)."""
    from PIL import Image, ImageDraw
    noms = [n for n, (v, _) in A_FAIRE.items() if v == visage and os.path.exists(os.path.join(DOSSIER, n + ".png"))]
    t = 300
    im = Image.new("RGB", ((len(noms) + 1) * t, t + 22), "white")
    d = ImageDraw.Draw(im)
    s = Image.open(source(visage)).convert("RGB")
    c = min(s.size)
    im.paste(s.crop(((s.width - c) // 2, 0, (s.width - c) // 2 + c, c)).resize((t, t)), (0, 0))
    d.text((6, t + 4), visage + " (source)", fill="black")
    for i, n in enumerate(noms, 1):
        im.paste(Image.open(os.path.join(DOSSIER, n + ".png")).convert("RGB").resize((t, t)), (i * t, 0))
        d.text((i * t + 6, t + 4), "%s  fond %.0f" % (n.split("-", 1)[1], controle_fond(n)), fill="black")
    im.save(sortie, quality=88)
    print("  planche :", sortie)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    os.makedirs(DOSSIER, exist_ok=True)
    if "--compte" in sys.argv:          # gratuit : le lot 2 par partie, au cent pres
        for partie, table in LOT2.items():
            n = sum(len(v) for v in table.values())
            print("  %-9s %3d images  %6.2f $  (%d visages)" % (partie, n, n * PRIX, len(table)))
        print("  deja depense sur le lot 2 : %.2f $ ; accorde : %s, plafond %.2f $" % (depense_lot2(), LOT2_ACCORDE or "rien",
                                                                                     PLAFOND_LOT2))
        return
    if "--planche" in sys.argv:         # python visages.py --planche Aylin [sortie.jpg]
        planche(args[0], args[1] if len(args) > 1 else os.path.join(DOSSIER, "planche-%s.jpg" % args[0]))
        return
    noms = args or [n for n in A_FAIRE if n not in NOMS_LOT2 or NOMS_LOT2[n] in LOT2_ACCORDE or montrer]
    inconnus = [n for n in noms if n not in A_FAIRE]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
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
        visage = A_FAIRE[nom][0]
        print("\n  %s\n  %s" % (nom, prompt(nom)))
        if montrer:
            continue
        # La garde du lot 2 : rien n'est paye hors des parties accordees par Jacques, ni au-dela de son plafond.
        if nom in NOMS_LOT2:
            if NOMS_LOT2[nom] not in LOT2_ACCORDE:
                sys.exit("  ARRET : %s est dans la partie « %s », que Jacques n'a pas accordee." % (nom, NOMS_LOT2[nom]))
            if depense_lot2() + PRIX > PLAFOND_LOT2 + 1e-9:
                sys.exit("  ARRET : le plafond du lot 2 (%.2f $) serait depasse (deja %.2f $). Demander a Jacques."
                         % (PLAFOND_LOT2, depense_lot2()))
        if visage not in depots:
            depots[visage] = O.deposer(source(visage), "image/png", cle)[0]
        corps = {"prompt": prompt(nom), "image_urls": [depots[visage]], "aspect_ratio": "1:1", "resolution": "2K",
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
            "prompt": prompt(nom), "source": source(visage), "prix": PRIX}, ensure_ascii=False, indent=1))
        web(nom)
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
