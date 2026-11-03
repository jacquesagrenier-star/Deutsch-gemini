# -*- coding: utf-8 -*-
"""Les emotions et le caractere, troisieme « theme illustre » (3 nov. 2026). ET C'EST FACTURE : 0,15 $ l'image,
chez fal. Accord de Jacques (3 nov.) : « Oui, les trois » -- 48 images, 7,20 $, 9 $ au plus avec les reprises.

    python visuel/emociones/emociones.py                 # celles qui manquent (0,15 $ chacune)
    python visuel/emociones/emociones.py Anna-contento   # celles-la seulement
    python visuel/emociones/emociones.py --montrer       # les prompts seuls, gratuit
    python visuel/emociones/emociones.py --json          # emociones.json seul, gratuit
    python visuel/emociones/emociones.py --refaire Anna-triste   # l'ancienne passe en <nom>-rate.png

UNE EMOTION SE LIT SUR UN VISAGE : six personnes deja faites (Anna, Carmen et Gisela ; Mark, Diego et Ben), 36
portraits, chaque emotion sur trois visages dont au moins un homme et une femme (l'accord contento /
contenta s'y voit). Toujours par RETOUCHE de leur image existante (nano-banana-pro/edit) : le meme visage, jamais
une description seule. UN TRAIT DE CARACTERE DEMANDE UNE SITUATION : douze petites scenes, une par trait, chacune
avec une personne de « Decrire une personne », en paires de contraires.
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/emociones/img/.
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

EDIT, PRIX = "fal-ai/nano-banana-pro/edit", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "emociones", "img")
# Les sources, en pied, 1536 x 2752 : le depot principal (Descripcion, Mark) et la famille.
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
SOURCES = {"Mark": PRINCIPAL + "/personnages/Mark.png", "Anna": FAMILLE + "/Anna-quotidien.png",
           "Gisela": FAMILLE + "/Gisela.png", "Ben": FAMILLE + "/Ben.png"}
for n in ("Carmen", "Diego", "Marta", "Javier", "Rosa", "Lucas", "Tomas", "Elena", "Ines", "Pablo"):
    SOURCES[n] = PRINCIPAL + "/visuel/descripcion/img/" + n + ".png"
SEXE = {"Anna": "f", "Carmen": "f", "Gisela": "f", "Mark": "m", "Diego": "m", "Ben": "m", "Marta": "f", "Javier": "m",
        "Rosa": "f", "Lucas": "m", "Tomas": "m", "Elena": "f", "Ines": "f", "Pablo": "m"}

# Chaque emotion : ce que le visage doit montrer, sans equivoque (la peur n'est pas la surprise, l'inquietude n'est
# pas la nervosite : chacune a son geste).
EMOTIONS = {
    "contento":    "happy and cheerful: a broad, genuine smile showing the teeth, bright eyes, raised cheeks.",
    "triste":      "sad: the eyes look down, the inner eyebrows are raised, the corners of the mouth turn down, the eyes are moist, close to tears.",
    "enfadado":    "angry: a deep frown, the eyebrows pulled down and together, the lips pressed tightly, glaring at the camera, the arms crossed.",
    "miedo":       "frightened, afraid: the eyes wide open with fear, the eyebrows raised and drawn together, the mouth slightly open, both hands raised in front of the chest as if to protect themselves, leaning back.",
    "sorprendido": "pleasantly surprised, amazed: the eyebrows raised very high, the eyes wide open, the mouth open in a round O, one hand on the cheek. Surprise, not fear.",
    "cansado":     "very tired, sleepy: heavy, half-closed eyelids, dark circles under the eyes, yawning widely with one hand in front of the mouth.",
    "aburrido":    "bored: the head resting heavily on one hand, the cheek pushed up by the hand, the eyes rolled to the side, a flat, expressionless mouth, slumped.",
    "nervioso":    "nervous: biting the nails of one hand, the eyes glancing sideways, the shoulders tense and raised, a small drop of sweat on the forehead.",
    "preocupado":  "worried: a deeply furrowed brow, the eyebrows drawn up and together, one hand pressed against the forehead, the lips pressed, the gaze lost to the side.",
    "orgulloso":   "proud: the chin raised, the chest out, a satisfied closed-mouth smile, holding up a gold medal on a ribbon in one hand.",
    "avergonzado": "embarrassed, ashamed: blushing red cheeks, an awkward, shy smile, one hand covering part of the face, the eyes looking down and away.",
    "enfermo":     "sick with a cold: a pale face, a red nose, feverish, watery eyes, a thick scarf around the neck, holding a paper tissue to the nose.",
}
# Six expressions par personne ; chaque emotion sur trois visages, au moins un homme et une femme. Anna a les
# quatre de la vignette (contente, surprise, fachee, triste : la bande de photomaton).
# 3 nov. : Ben triste et Ben qui a peur, refuses deux fois par le filtre de fal (content_policy_violation : un enfant
# en detresse). On ne contourne pas le filtre : la tristesse passe a Diego, la peur a Mark ; Ben garde quatre visages.
PORTRAITS = {
    "Anna":   ["contento", "triste", "enfadado", "sorprendido", "cansado", "nervioso"],
    "Carmen": ["avergonzado", "orgulloso", "triste", "sorprendido", "miedo", "preocupado"],
    "Gisela": ["avergonzado", "orgulloso", "contento", "enfadado", "aburrido", "enfermo"],
    "Mark":   ["sorprendido", "avergonzado", "cansado", "nervioso", "preocupado", "enfermo", "miedo"],
    "Diego":  ["enfadado", "contento", "miedo", "aburrido", "nervioso", "preocupado", "triste"],
    "Ben":    ["orgulloso", "aburrido", "cansado", "enfermo"],
}
# Les traits, en paires de contraires ; la personne et la situation qui le montre sans un mot.
TRAITS = {
    "generoso":     ("Marta", "In a cafe, she happily pays the bill for the whole table of friends, handing her card to the waiter while the friends thank her, smiling."),
    "tacano":       ("Javier", "At a restaurant table with friends, the bill arrives: he hides his wallet behind his back and looks away, pretending not to see the bill, while the friends look at him annoyed."),
    "trabajador":   ("Rosa", "In an office in the evening, the window dark outside, she works hard and concentrated at her desk covered with folders, typing on a laptop, a cup of coffee beside her; the other desks are empty."),
    "perezoso":     ("Lucas", "In the middle of the day, he lies lazily on a sofa in a living room watching television, a bag of crisps on his belly, while a big pile of dirty dishes and an overflowing laundry basket wait next to him."),
    "extrovertido": ("Tomas", "At a lively party, he stands in the middle of a group of people, telling a story with big gestures and laughing loudly; everybody around him laughs too."),
    "timido":       ("Elena", "At a lively party, she stands alone in a corner, half hidden behind a plant, holding her glass in both hands close to her chest and looking at the floor, while other guests chat in the background."),
    "educado":      ("Mark", "At the entrance of a building, he holds the door open with a friendly smile for an elderly lady with a shopping bag who walks in and thanks him."),
    "grosero":      ("Ines", "In a queue at a bakery counter, she pushes rudely in front of the other customers with her elbow, talking loudly on her phone, while the people in the queue look at her shocked."),
    "ordenado":     ("Carmen", "She sits at a perfectly tidy desk in a bright study: pencils lined up, folders neatly stacked and labelled, shelves in perfect order behind her; she smiles, satisfied."),
    "desordenado":  ("Diego", "He stands in the middle of a very messy bedroom, scratching his head: clothes all over the floor and the unmade bed, open drawers, books and empty cups everywhere."),
    "simpatico":    ("Anna", "On a city street, she kindly helps a lost tourist couple, pointing the way on their paper map with a warm, friendly smile."),
    "antipatico":   ("Pablo", "On a city street, a young woman asks him a question politely; he turns his back on her with a cold, unfriendly face and his arms crossed."),
}
MEME = ("The same person as in the reference picture: exactly the same face, the same age, the same hair, the same skin, "
        "the same glasses or beard if any, the same body and the same clothes. ")
PORTRAIT = (" A photorealistic head-and-shoulders portrait, from the top of the head to the middle of the chest, facing the "
            "camera, centred. Plain light grey studio background with even soft light, nothing else in the picture, no text, "
            "no logos. Natural skin texture, no retouching. The expression is: ")
SITUATION = (" A photorealistic photograph of a real everyday scene, natural light, natural colours, no text, no logos, "
             "no captions. The person is clearly visible from head to at least the knees, in the centre, and their face "
             "and gesture are easy to read. Scene: ")


def images():
    """{nom de fichier: (source, prompt, format)} -- 36 portraits et 12 situations."""
    out = {}
    for p, emos in PORTRAITS.items():
        for e in emos:
            out[p + "-" + e] = (p, MEME + PORTRAIT + EMOTIONS[e], "1:1")
    for t, (p, scene) in TRAITS.items():
        out["trait-" + t] = (p, MEME + SITUATION + scene, "4:3")
    return out


# LES MOTS, la seule source : la page les lit dans emociones.json (questions et decouverte), les inventaires des voix
# (audio/manifest.py, manifest_es.py) y lisent les phrases de la decouverte. es = [masculin, feminin] ; latam ne
# porte que ce qui change en Amerique latine (enfadado -> enojado). « miedo » se dit avec tener / haben : c'est la
# lecon (tiene miedo, hat Angst), pas estar / sein.
MOTS_EMOTIONS = {
    "contento":    {"es": ["contento", "contenta"], "de": "glücklich"},
    "triste":      {"es": ["triste", "triste"], "de": "traurig"},
    "enfadado":    {"es": ["enfadado", "enfadada"], "latam": ["enojado", "enojada"], "de": "sauer"},
    "miedo":       {"es": ["miedo", "miedo"], "de": "Angst", "tener": True},
    "sorprendido": {"es": ["sorprendido", "sorprendida"], "de": "überrascht"},
    "cansado":     {"es": ["cansado", "cansada"], "de": "müde"},
    "aburrido":    {"es": ["aburrido", "aburrida"], "de": "gelangweilt"},
    "nervioso":    {"es": ["nervioso", "nerviosa"], "de": "nervös"},
    "preocupado":  {"es": ["preocupado", "preocupada"], "de": "besorgt"},
    "orgulloso":   {"es": ["orgulloso", "orgullosa"], "de": "stolz"},
    "avergonzado": {"es": ["avergonzado", "avergonzada"], "de": "verlegen"},
    "enfermo":     {"es": ["enfermo", "enferma"], "de": "krank"},
}
# En allemand, d'autres tournures avec haben, vraies pour la meme image (l'exercice « ist oder hat? ») :
HABEN = {"enfadado": "schlechte Laune", "enfermo": "eine Erkältung"}
# Les traits, et leur contraire (la paire d'images de l'exercice « lo contrario » / « das Gegenteil »).
MOTS_TRAITS = {
    "generoso":     {"es": ["generoso", "generosa"], "de": "großzügig", "contraire": "tacano"},
    "tacano":       {"es": ["tacaño", "tacaña"], "de": "geizig", "contraire": "generoso"},
    "trabajador":   {"es": ["trabajador", "trabajadora"], "de": "fleißig", "contraire": "perezoso"},
    "perezoso":     {"es": ["perezoso", "perezosa"], "de": "faul", "contraire": "trabajador"},
    "extrovertido": {"es": ["extrovertido", "extrovertida"], "de": "kontaktfreudig", "contraire": "timido"},
    "timido":       {"es": ["tímido", "tímida"], "de": "schüchtern", "contraire": "extrovertido"},
    "educado":      {"es": ["educado", "educada"], "de": "höflich", "contraire": "grosero"},
    "grosero":      {"es": ["grosero", "grosera"], "de": "unhöflich", "contraire": "educado"},
    "ordenado":     {"es": ["ordenado", "ordenada"], "de": "ordentlich", "contraire": "desordenado"},
    "desordenado":  {"es": ["desordenado", "desordenada"], "de": "unordentlich", "contraire": "ordenado"},
    "simpatico":    {"es": ["simpático", "simpática"], "de": "sympathisch", "contraire": "antipatico"},
    "antipatico":   {"es": ["antipático", "antipática"], "de": "unsympathisch", "contraire": "simpatico"},
}
# La decouverte : un visage par emotion, deux emotions par personne (des visages varies sur la planche).
DECOUVERTE = {"contento": "Anna", "nervioso": "Anna", "miedo": "Carmen", "orgulloso": "Carmen",
              "avergonzado": "Gisela", "enfermo": "Gisela", "sorprendido": "Mark", "preocupado": "Mark",
              "enfadado": "Diego", "triste": "Diego", "aburrido": "Ben", "cansado": "Ben"}
NOMS = {"Ines": "Inés", "Tomas": "Tomás"}


def phrase(langue, p, mot, emotion):
    """La phrase dite et ecrite : « Carmen está triste. », « Carmen tiene miedo. », « Marta es generosa. »,
    « Carmen ist traurig. », « Carmen hat Angst. ». La page fabrique ses phrases avec la meme regle."""
    n, f = NOMS.get(p, p), SEXE[p] == "f"
    if langue == "de":
        return "%s %s %s." % (n, "hat" if mot.get("tener") else "ist", mot["de"])
    forme = (mot.get("latam") if langue == "latam" else None) or mot["es"]
    verbe = "tiene" if mot.get("tener") else ("está" if emotion else "es")
    return "%s %s %s." % (n, verbe, forme[1 if f else 0])


def identifiant(texte):
    import hashlib
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def ecrire_json():
    """La donnee de la page : qui montre quelle emotion, quel trait est montre par qui, les mots, et les phrases de
    la decouverte avec l'identifiant de leur son (sha1 du texte, comme audio/manifest.py)."""
    dec = {}
    for langue in ("es", "latam", "de"):
        dec[langue] = {}
        for e, p in DECOUVERTE.items():
            t = phrase(langue, p, MOTS_EMOTIONS[e], True)
            dec[langue][e] = {"texte": t, "son": identifiant(t)}
        for t_id, (p, _) in TRAITS.items():
            t = phrase(langue, p, MOTS_TRAITS[t_id], False)
            dec[langue][t_id] = {"texte": t, "son": identifiant(t)}
    d = {"sexe": {p: SEXE[p] for p in list(PORTRAITS) + [v[0] for v in TRAITS.values()]},
         "noms": NOMS, "portraits": PORTRAITS, "traits": {t: v[0] for t, v in TRAITS.items()},
         "emotions": MOTS_EMOTIONS, "caracteres": MOTS_TRAITS, "haben": HABEN,
         "decouverte": {"visages": DECOUVERTE, "phrases": dec}}
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    for chemin in (os.path.join(ICI, "emociones.json"), os.path.join(RACINE, "visuel", "prototype", "emociones", "emociones.json")):
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        io.open(chemin, "w", encoding="utf-8", newline="\n").write(texte)


def textes_a_dire(langue):
    """Pour les inventaires des voix : les phrases de la decouverte, dans cette langue (es, latam, de)."""
    d = json.load(io.open(os.path.join(ICI, "emociones.json"), encoding="utf-8"))
    return [v["texte"] for v in d["decouverte"]["phrases"][langue].values()]


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    tout = images()
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or list(tout)
    inconnus = [n for n in noms if n not in tout]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    os.makedirs(DOSSIER, exist_ok=True)
    ecrire_json()
    if "--json" in sys.argv:
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
    if not montrer and not os.environ.get("FAL_KEY") and not os.path.exists(os.path.join(RACINE, "fal.secret")):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = None if montrer else O.cle()
    depots = {}
    for nom in a_faire:
        source, prompt, fmt = tout[nom]
        print("\n  %s\n  %s" % (nom, prompt))
        if montrer:
            continue
        if source not in depots:
            depots[source] = O.deposer(SOURCES[source], "image/png", cle)[0]
        corps = {"prompt": prompt, "image_urls": [depots[source]], "aspect_ratio": fmt, "resolution": "2K",
                 "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
            # 3 nov. : Ben triste refuse (HTTP 422) et tout le lot s'arretait. On note la raison et on continue.
            import urllib.request, urllib.error
            raison = str(err)
            try:
                urllib.request.urlopen(urllib.request.Request(soum["response_url"], headers={"Authorization": "Key " + cle}), timeout=60)
            except urllib.error.HTTPError as e:
                raison += " " + e.read().decode("utf-8", "replace")[:400]
            print("  ECHEC", nom, raison)
            io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
                "%s\t%s\t%s\tECHEC\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), raison.replace("\n", " ")))
            continue
        sortie = os.path.join(DOSSIER, nom + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(DOSSIER, "depenses.log"), "a", encoding="utf-8").write(
            "%s\t%s\t%s\t%.2f\n" % (time.strftime("%Y-%m-%dT%H:%M:%S"), nom, soum.get("request_id"), PRIX))
        io.open(os.path.join(DOSSIER, nom + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": EDIT, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "source": SOURCES[source], "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", sortie, "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
