# -*- coding: utf-8 -*-
"""Les portraits neufs des personnes des conversations. ET C'EST FACTURE : 0,15 $ l'image, chez fal (nano-banana-pro).

    python visuel/conversation/portraits.py --montrer          # les prompts seuls, gratuit
    python visuel/conversation/portraits.py Rainer Aylin       # ceux-la (0,15 $ chacun)
    python visuel/conversation/portraits.py                    # tous ceux qui manquent
    python visuel/conversation/portraits.py --refaire Rainer   # l'ancien passe en <nom>-rateN.png
    python visuel/conversation/portraits.py --web              # les webp de la page (480 x 480), gratuit
    python visuel/conversation/portraits.py --planche          # la planche de controle, gratuit

Decision de Jacques du 16 nov. 2026 (« Les 27 portraits (4 $) », decisions/DECISIONS.md) : les 27 personnes des
conversations qui empruntaient un visage (« provisoire » dans personnes-<lot>.json) recoivent le leur. Elles n'ont
pas d'image source : c'est une generation TEXTE vers image, au cadre des portraits de la page (conversation/*-neutre,
tete et epaules, fond studio gris clair, photorealiste), avec une expression calme et aimable qui servira de base
aux expressions (visages.py, par retouche) apres la relecture native des lots.

Regles : uniquement des adultes ; un visage neuf qui ne ressemble a aucun recurrent (Mark, Anna, la famille d'Anna,
les douze de Descripcion) ni a une reserve ; un prenom de fichier neuf, ni recurrent ni reserve (visuel/personnes.json).
Aucun badge, logo ni texte demande : un badge nomme arrive avec de fausses lettres (video/verifier_prompt.py,
« affiche-qui-ecrit »).
Originaux hors du depot et de OneDrive : ~/.wortando/conversation/img/<Nom>-neutre.png.
"""
import io, json, os, subprocess, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

MODELE, PRIX = "fal-ai/nano-banana-pro", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "conversation", "img")
WEB = os.path.join(RACINE, "visuel", "prototype", "conversation")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"

STYLE = "A photorealistic photograph of a real person, natural skin texture, no retouching, no studio glamour. "
# Le cadre des portraits d'emotions (emociones.py, PORTRAIT), repris par visages.py : les visages vont ensemble.
CADRE = (" A head-and-shoulders portrait, from the top of the head to the middle of the chest, facing the camera, "
         "centred. Plain light grey studio background with even soft light, nothing else in the picture, no text, "
         "no logos. The expression is calm, pleasant and natural, the lips closed with a faint friendly hint of a "
         "smile, the eyes looking straight into the camera.")

# cle de personnes-<lot>.json : (Nom du fichier, lot, ce qu'on demande). Les ages et metiers sont ceux de la
# description du lot ; l'origine, le visage et la coiffure sont choisis pour qu'aucun ne ressemble a un autre.
PERSONNES = {
    "bahnangestellter": ("Rainer", "a1-1",
        "A German man of about fifty, slim, with short grey hair neatly parted, thin metal-framed glasses and a "
        "clean-shaven narrow face. He wears a plain light-blue uniform shirt with a dark red tie, the uniform of a "
        "railway ticket clerk, with no logo. Kind and composed."),
    "kassiererin": ("Aylin", "a1-1",
        "A Turkish-German woman of about forty-five, with dark brown hair pulled back into a low ponytail, dark "
        "eyes and a round face. She wears a plain navy-blue polo shirt, the uniform of a supermarket cashier, with "
        "no logo. Busy but kind."),
    "apothekerin": ("Claire", "a1-1",
        "A woman of about forty with a straight chin-length brown bob, rectangular dark-framed glasses and fair "
        "skin. She wears a white pharmacist's coat, open over a pale grey top. Calm and attentive."),
    "praxis_empfang": ("Selin", "a1-2",
        "A woman of about thirty of Middle Eastern descent, with long dark hair tied back in a neat bun, olive skin "
        "and dark eyes. She wears light blue medical scrubs, the uniform of a doctor's receptionist. Calm and kind."),
    "post_schalter": ("Nikos", "a1-2",
        "A Greek man of about fifty-five, sturdy, with short grey hair, a full grey moustache, bushy dark-grey "
        "eyebrows and olive skin, no glasses. He wears a plain dark-blue short-sleeved uniform shirt with an "
        "open collar, the uniform of a post office counter clerk, with no logo. Easy-going and unhurried."),
    "museum_kasse": ("Romy", "a1-2",
        "A young woman of about twenty-five, a student, with a short dark-blonde pixie cut, freckles and small "
        "silver ear studs. She wears a dark charcoal cardigan over a black T-shirt. Friendly and relaxed."),
    "buergeramt_schalter": ("Birgit", "a1-2",
        "A German woman of about forty with shoulder-length straight medium-brown hair, fair skin and light "
        "eyes. She wears a soft beige cardigan over a white blouse, the look of a town hall counter clerk. "
        "Polite and matter-of-fact."),
    "bibliothek_schalter": ("Keira", "a1-2",
        "An African-American woman of about thirty-five with voluminous shoulder-length curly hair, warm brown "
        "skin and dark eyes. She wears a bright mustard-yellow knitted sweater and a plain red lanyard around her "
        "neck, its card hidden behind the sweater. A cheerful public librarian."),
    "a22_apothekerin": ("Dagmar", "a2-2",
        "A woman of about fifty with short silver-blonde hair cut close at the sides, round tortoiseshell glasses "
        "and fair skin with fine lines. She wears a white pharmacist's coat over a navy top. Kind and precise."),
    "a22_sekretaerin": ("Renate", "a2-2",
        "A woman of about fifty-five with chin-length wavy grey hair, fair skin and light blue eyes. She wears a "
        "dusty-rose cardigan over a white blouse and a light telephone headset with a small microphone arm. The "
        "secretary of a primary school, friendly and efficient."),
    "a22_erzieherin": ("Zoe", "a2-2",
        "A young woman of about twenty-five of mixed Black and white heritage, with light brown skin and curly "
        "light-brown hair tied up in a high puff, a few loose curls at the temples. She wears a bright turquoise "
        "hooded sweatshirt. A nursery educator with a soft, gentle look."),
    "a22_trainer": ("Kwame", "a2-2",
        "A Black man of about forty of Ghanaian descent, athletic, with very short black hair, a neatly trimmed "
        "short beard and dark brown skin. He wears a dark green zip-up sports club tracksuit jacket with no logo "
        "and a silver whistle on a black cord around his neck. A friendly sports coach."),
    "a22_bibliothekar": ("Arjun", "a2-2",
        "A man of about thirty-five of Indian descent, slim, with short neat black hair, round black-framed "
        "glasses, light brown skin and a clean-shaven face. He wears a plain burgundy crew-neck sweater over a "
        "collared shirt. A quiet, helpful librarian."),
    "hotline_agentin": ("Mei", "a2-3",
        "A woman of about thirty of Chinese descent, with straight black hair in a shoulder-length cut with "
        "bangs, and a light headset with a small microphone arm over her hair. She wears a plain lavender office "
        "blouse. A smiling customer service agent."),
    "versicherung_beraterin": ("Claudia", "a2-3",
        "A woman of about forty-five with shoulder-length dark-blonde hair with soft waves, fair skin and small "
        "pearl earrings. She wears a navy blazer over a light blue blouse. An insurance adviser in a branch "
        "office, composed and professional."),
    "vermietung_agentin": ("Yasmin", "a2-3",
        "A young woman of about twenty-five of North African descent, with long dark wavy hair tied back in a "
        "ponytail, warm olive skin and dark eyes. She wears a plain red company polo shirt with no logo, the "
        "uniform of a car rental desk agent. Bright and helpful."),
    "gepaeck_agent": ("Omar", "a2-3",
        "A man of about fifty of Arab descent, with short black hair greying at the temples, a short salt-and-"
        "pepper beard and warm brown skin. He wears a white short-sleeved airport staff uniform shirt with dark "
        "blue shoulder epaulettes and a dark blue tie. Calm and obliging."),
    "rad_verkaeuferin": ("Freya", "a2-3",
        "A sporty woman of about thirty-five with reddish-blonde hair in a messy braid over one shoulder, light "
        "freckled skin and a slightly weathered outdoor complexion. She wears a dark grey canvas workshop apron "
        "over an olive-green T-shirt. A bicycle shop saleswoman and mechanic."),
    "b11_guichet": ("Daria", "b1-1",
        "A woman of about thirty of Eastern European descent, with straight light-brown hair in a sleek low "
        "ponytail, pale skin and grey-green eyes. She wears a plain white office blouse under a dark grey "
        "cardigan. A clerk at a public administration counter, polite and businesslike."),
    "b11_conseillere": ("Brigitte", "b1-1",
        "A woman of about fifty with a short layered auburn haircut, green-framed glasses, fair skin with a few "
        "freckles. She wears a teal knit top under a charcoal blazer. A job centre adviser, attentive and "
        "experienced."),
    "b11_service_client": ("Priya", "b1-1",
        "A woman of about thirty of South Asian descent, with long straight black hair worn loose over one "
        "shoulder, brown skin, and a light headset with a small microphone arm. She wears a plain coral-pink "
        "office top. A customer service adviser on the telephone."),
    "b11_camarade": ("Linh", "b1-1",
        "A young woman of about twenty-three of Vietnamese descent, with long straight black hair half tied up, "
        "and a casual cream knitted sweater. A friendly student from abroad in a language class."),
    "fitness_beraterin": ("Vanessa", "b1-2",
        "A fit woman of about thirty of Brazilian descent, with long dark-brown hair in a high ponytail, tanned "
        "golden-brown skin. She wears a plain black gym staff polo shirt with no logo. Smiling and salesy."),
    "umzugschef": ("Bogdan", "b1-2",
        "A burly Polish man of about fifty, broad-shouldered, with a thick neck, short greying brown hair cut "
        "very short, a ruddy complexion and stubble. He wears a dark orange work polo shirt with no logo, the "
        "uniform of a removal company foreman. Frank and practical."),
    "b13_fluggesellschaft": ("Noemi", "b1-3",
        "A woman of about thirty-five of Italian descent, with dark brown hair in a smooth tight bun, olive skin "
        "and dark eyes. She wears a navy airline uniform jacket over a white blouse with a small red silk scarf "
        "tied at the neck, no logo. Polite and a little hurried."),
    "b13_notruf": ("Stefan", "b1-3",
        "A man of about forty-five with a shaved head, a short dark-blond beard, fair skin and light blue eyes, "
        "with a light headset with a small microphone arm. He wears a plain dark navy polo shirt. An emergency "
        "call dispatcher, calm and reassuring."),
    "b13_kundenservice": ("Grace", "b1-3",
        "A Black woman of about thirty with short natural hair in a tidy rounded afro, dark brown skin, and a "
        "light headset with a small microphone arm. She wears a plain mint-green office blouse. A call centre "
        "agent, friendly and professional."),
}
NOMS = {v[0]: k for k, v in PERSONNES.items()}


def prompt(cle):
    return STYLE + PERSONNES[cle][2] + CADRE


def png(nom):
    return os.path.join(DOSSIER, nom + "-neutre.png")


# Un portrait sorti trop large se RECADRE (gratuit) : (gauche, haut, cote) en fractions de l'image.
# 16 nov. 2026 : Daria et Linh sont sorties assises a une table, dont le bord (et un carnet) fermait le bas.
RECADRAGE = {"Daria": (0.14, 0.08, 0.72), "Linh": (0.07, 0.02, 0.86)}
# Retouches gratuites deja faites sur l'original (l'image d'avant gardee a cote) :
#   Omar : un badge « AHMED » en lettres latines et arabes, que le prompt ne demandait pas (« affiche-qui-ecrit » :
#   un uniforme d'aeroport arrive avec son badge ecrit), efface par visuel/effacer_texte.py, boite
#   [470, 1760, 305, 145], « tout » ; l'original : Omar-neutre-avec-badge.png.


def web(nom):
    """Le webp de la page : carre 480 x 480 (le portrait est deja carre, tete et epaules)."""
    if not os.path.exists(png(nom)):
        return
    g, h, c = RECADRAGE.get(nom, (0, 0, 1))
    vf = "crop='min(iw,ih)*%g':'min(iw,ih)*%g':'iw*%g':'ih*%g',scale=480:480" % (c, c, g, h)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", png(nom), "-vf", vf, "-quality", "85",
                    os.path.join(WEB, nom + "-neutre.webp")], check=True)


def planche(sortie):
    """Les 27 webp en planche (6 de large), le prenom et la cle sous chacun : pour les verifier d'un coup d'oeil."""
    from PIL import Image, ImageDraw, ImageFont
    noms = [v[0] for v in PERSONNES.values()]
    t, l = 240, 6
    h = (len(noms) + l - 1) // l
    im = Image.new("RGB", (l * t, h * (t + 34)), "white")
    d = ImageDraw.Draw(im)
    try:
        f = ImageFont.truetype("arial.ttf", 15)
    except OSError:
        f = ImageFont.load_default()
    for i, n in enumerate(noms):
        x, y = (i % l) * t, (i // l) * (t + 34)
        p = os.path.join(WEB, n + "-neutre.webp")
        if os.path.exists(p):
            im.paste(Image.open(p).convert("RGB").resize((t, t)), (x, y))
        d.text((x + 6, y + t + 2), n, fill="black", font=f)
        d.text((x + 6, y + t + 17), NOMS[n], fill="#666", font=f)
    im.save(sortie, quality=88)
    print("  planche :", sortie)


EDIT = "fal-ai/nano-banana-pro/edit"
# Un portrait juste dont le FOND deborde (un bureau, une chaise) : on retouche le fond seul, le visage choisi reste
# (0,15 $). 16 nov. 2026 : Priya (un open space, un telephone) et Stefan (un dossier de chaise noire) -- le mot
# « headset » a fait venir le centre d'appels autour d'eux, malgre « nothing else in the picture ».
FOND = ("The same picture of the same person: exactly the same face, hair, skin, headset, clothes, pose, framing and "
        "expression. Change only what is behind the person: a plain light grey studio background with even soft "
        "light, an empty seamless wall, nothing else behind the person.")


def refaire_fond(nom, cle):
    source = png(nom)
    k = 1
    while os.path.exists(os.path.join(DOSSIER, "%s-neutre-rate%d.png" % (nom, k))):
        k += 1
    ancien = os.path.join(DOSSIER, "%s-neutre-rate%d.png" % (nom, k))
    os.replace(source, ancien)
    url = O.deposer(ancien, "image/png", cle)[0]
    corps = {"prompt": FOND, "image_urls": [url], "aspect_ratio": "1:1", "resolution": "2K",
             "output_format": "png", "num_images": 1}
    soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
    res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
    O.telecharger(res["images"][0]["url"], source)
    io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
        "%s\t%s-neutre-fond\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), PRIX))
    web(nom)
    print("  fond refait :", nom, "(%.2f $)" % PRIX)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--fond" in sys.argv:          # python portraits.py --fond Priya Stefan   (0,15 $ chacun)
        if not os.environ.get("FAL_KEY"):
            os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
        cle = O.cle()
        for n in args:
            refaire_fond(n, cle)
        return
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    os.makedirs(DOSSIER, exist_ok=True)
    if "--planche" in sys.argv:
        planche(args[0] if args and args[0].endswith(".jpg") else os.path.join(DOSSIER, "planche-portraits.jpg"))
        return
    noms = args or [v[0] for v in PERSONNES.values()]
    inconnus = [n for n in noms if n not in NOMS]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    if "--web" in sys.argv:
        for n in noms:
            web(n)
        print("  webp refaits")
        return
    if refaire and not montrer:
        for n in noms:
            if os.path.exists(png(n)):
                k = 1
                while os.path.exists(os.path.join(DOSSIER, "%s-neutre-rate%d.png" % (n, k))):
                    k += 1
                os.replace(png(n), os.path.join(DOSSIER, "%s-neutre-rate%d.png" % (n, k)))
    a_faire = [n for n in noms if not os.path.exists(png(n))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    if not montrer and not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = None if montrer else O.cle()
    for nom in a_faire:
        p = prompt(NOMS[nom])
        print("\n  %s (%s)\n  %s" % (nom, NOMS[nom], p))
        if montrer:
            continue
        corps = {"prompt": p, "aspect_ratio": "1:1", "resolution": "2K", "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + MODELE, cle, corps)
        journal = io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8")
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            print("  ECHEC", nom, err)
            journal.write("%s\t%s-neutre\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom,
                          soum.get("request_id"), str(err).replace("\n", " ")))
            journal.close()
            continue
        O.telecharger(res["images"][0]["url"], png(nom))
        journal.write("%s\t%s-neutre\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), PRIX))
        journal.close()
        io.open(os.path.join(DOSSIER, nom + "-neutre-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": MODELE, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": p, "prix": PRIX, "personne": NOMS[nom]}, ensure_ascii=False, indent=1))
        web(nom)
        print("  ->", png(nom), "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
