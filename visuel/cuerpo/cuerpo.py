# -*- coding: utf-8 -*-
"""Le corps et la sante, theme illustre de la vague 1 (3 nov. 2026). L'ANGLE : DIRE OU ON A MAL ET COMMENT ON SE
SENT -- des personnes qui ont mal, pas les objets des scenes arztpraxis, apotheke et untersuchung. ET LES IMAGES
SONT FACTUREES : 0,15 $ l'image, chez fal. Aucune image ne se fait sans l'accord de Jacques lui-meme.

    python visuel/cuerpo/cuerpo.py --json        # cuerpo.json et gloses.json seuls, gratuit
    python visuel/cuerpo/cuerpo.py --montrer     # les prompts, gratuit
    python visuel/cuerpo/cuerpo.py               # les images qui manquent (0,15 $ chacune)
    python visuel/cuerpo/cuerpo.py dolor-cabeza-Anna   # celles-la seulement
    python visuel/cuerpo/cuerpo.py --refaire dolor-cabeza-Anna   # l'ancienne passe en <nom>-rate<n>.png

LES PERSONNES SONT LES NOTRES, par RETOUCHE de leur image existante (nano-banana-pro/edit), jamais une description
seule : les douze de « Decrire une personne », la famille d'Anna. Une douleur MODEREE (une grimace, la main sur
l'endroit), jamais forte ; l'enfant (Ben) n'a qu'un genou ecorche (le filtre de fal refuse un enfant en detresse,
3 nov.). Reutilises sans frais : les visages « malade » et « fatigue » d'Emotions (le lien estar enfermo / tener
fiebre), les silhouettes en pied et les visages de Decrire pour toucher le corps.
LA SEULE SOURCE DES MOTS : la page lit cuerpo.json (questions et decouverte) et en fabrique toutes ses phrases.
Originaux hors du depot et de OneDrive : C:/Users/jacqu/.wortando/cuerpo/img/.
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))

EDIT, PRIX = "fal-ai/nano-banana-pro/edit", 0.15
DOSSIER = os.path.join(os.path.expanduser("~"), ".wortando", "cuerpo", "img")
PRINCIPAL = "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI"
FAMILLE = "C:/Users/jacqu/.wortando/wt-themes/visuel/familia/img"
SOURCES = {"Mark": PRINCIPAL + "/personnages/Mark.png", "Anna": FAMILLE + "/Anna-quotidien.png"}
for n in ("Gisela", "Ben", "Heinz", "Peter", "Monika", "Sabine", "Frank", "Jan", "Katrin", "Lena", "Felix", "Sophie"):
    SOURCES[n] = FAMILLE + "/" + n + ".png"
for n in ("Carmen", "Diego", "Marta", "Javier", "Rosa", "Lucas", "Tomas", "Elena", "Ines", "Pablo"):
    SOURCES[n] = PRINCIPAL + "/visuel/descripcion/img/" + n + ".png"
SEXE = {"Anna": "f", "Carmen": "f", "Gisela": "f", "Mark": "m", "Diego": "m", "Ben": "m", "Marta": "f", "Javier": "m",
        "Rosa": "f", "Lucas": "m", "Tomas": "m", "Elena": "f", "Ines": "f", "Pablo": "m",
        "Heinz": "m", "Peter": "m", "Monika": "f", "Sabine": "f", "Frank": "m", "Jan": "m", "Katrin": "f", "Lena": "f",
        "Felix": "m", "Sophie": "f"}
NOMS = {"Ines": "Inés", "Tomas": "Tomás"}

# LES PARTIES DU CORPS. es / de : [article, mot] tels qu'on les dit ici (« me duelen los pies », « mir tun die Fuesse
# weh ») ; ces / cde : le mot du CORPUS, cle de la progression commune aux cartes (pie, el ; Fuss, der) ;
# dolor : l'endroit a des images « j'ai mal » ; toucher : on le touche sur la
# silhouette (corps) ou sur le visage (cara). Le cou et la gorge sont deux mots en espagnol (el cuello, la garganta),
# un seul en allemand (der Hals) : un meme mot allemand, une seule cle.
PARTES = {
    "cabeza":   {"es": ["la", "cabeza"], "de": ["der", "Kopf"], "dolor": True, "toucher": "corps"},
    "garganta": {"es": ["la", "garganta"], "de": ["der", "Hals"], "dolor": True},
    "oido":     {"es": ["el", "oído"], "de": ["das", "Ohr"], "dolor": True},
    "muela":    {"es": ["la", "muela"], "de": ["der", "Zahn"], "dolor": True},
    "espalda":  {"es": ["la", "espalda"], "de": ["der", "Rücken"], "dolor": True},
    "estomago": {"es": ["el", "estómago"], "de": ["der", "Bauch"], "dolor": True, "toucher": "corps"},
    "brazo":    {"es": ["el", "brazo"], "de": ["der", "Arm"], "dolor": True, "toucher": "corps"},
    "mano":     {"es": ["la", "mano"], "de": ["die", "Hand"], "dolor": True, "toucher": "corps"},
    "rodilla":  {"es": ["la", "rodilla"], "de": ["das", "Knie"], "dolor": True, "toucher": "corps"},
    "piernas":  {"es": ["las", "piernas"], "de": ["die", "Beine"], "dolor": True, "toucher": "corps",
                 "ces": ["pierna", "la"], "cde": ["Bein", "das"], "un": {"es": ["la", "pierna"], "de": ["das", "Bein"]}},
    "pies":     {"es": ["los", "pies"], "de": ["die", "Füße"], "dolor": True, "toucher": "corps",
                 "ces": ["pie", "el"], "cde": ["Fuß", "der"], "un": {"es": ["el", "pie"], "de": ["der", "Fuß"]}},
    "ojos":     {"es": ["los", "ojos"], "de": ["die", "Augen"], "dolor": True, "toucher": "cara",
                 "ces": ["ojo", "el"], "cde": ["Auge", "das"], "un": {"es": ["el", "ojo"], "de": ["das", "Auge"]}},
    "cuello":   {"es": ["el", "cuello"], "de": ["der", "Hals"], "toucher": "corps"},
    "hombro":   {"es": ["el", "hombro"], "de": ["die", "Schulter"], "toucher": "corps"},
    "pecho":    {"es": ["el", "pecho"], "de": ["die", "Brust"], "toucher": "corps"},
    "nariz":    {"es": ["la", "nariz"], "de": ["die", "Nase"], "toucher": "cara"},
    "boca":     {"es": ["la", "boca"], "de": ["der", "Mund"], "toucher": "cara"},
    "oreja":    {"es": ["la", "oreja"], "de": ["das", "Ohr"], "toucher": "cara"},
}
# Ce que montre chaque image « j'ai mal » : la main sur l'endroit, une douleur moderee.
GESTES = {
    "cabeza":   "has a headache: both hands pressed to the temples, the eyes half shut, a pained frown.",
    "garganta": "has a sore throat: one hand gently holding the front of the throat, swallowing with a pained grimace.",
    "oido":     "has an earache: one hand cupped over one ear, the head tilted toward that side, a pained face.",
    "muela":    "has a toothache: one hand pressed against the cheek over the jaw, the cheek slightly swollen, a pained grimace.",
    "espalda":  "has back pain: standing slightly bent forward, seen in three-quarter view so that both hands pressed on the lower back are clearly visible, a pained grimace.",
    "estomago": "has a stomach ache: both arms wrapped around the belly, slightly bent forward, a pained face.",
    "brazo":    "has a sore arm: holding the upper arm with the other hand, wincing.",
    "mano":     "has a sore hand: holding one hand by the wrist with the other hand and looking at it, wincing. No blood, no wound.",
    "rodilla":  "has a sore knee: sitting on a chair, both hands holding one knee, wincing.",
    "piernas":  "has sore, tired legs after a long walk: sitting on a bench, rubbing both thighs with both hands, a tired, pained face.",
    "pies":     "has sore feet after walking all day: sitting on a stool, the shoes off on the floor beside them, massaging one bare foot with both hands, a tired grimace.",
    "ojos":     "has sore, tired eyes: the eyes red and watery, rubbing both closed eyes with the fingertips.",
}
# Un geste propre a une personne (l'enfant : un genou ecorche, rien de plus).
GESTE_A_PART = {
    ("rodilla", "Ben"): "has a small scraped knee after falling while playing: wearing shorts, sitting on a bench, pointing at a small plaster on his knee, a little pout. He is not crying and not in distress.",
}
# 12 endroits x 3 personnes : au moins un homme et une femme par endroit, jamais deux fois la meme personne pour un
# endroit, deux endroits au plus par personne. Les jambes et les pieds sont vus en entier (assis).
DOLORES = {
    "cabeza":   ["Anna", "Diego", "Marta"],
    "garganta": ["Mark", "Elena", "Peter"],
    "oido":     ["Carmen", "Tomas", "Lena"],
    "muela":    ["Javier", "Rosa", "Felix"],
    "espalda":  ["Heinz", "Pablo", "Monika"],
    "estomago": ["Ines", "Lucas", "Sophie"],
    "brazo":    ["Jan", "Katrin", "Diego"],
    "mano":     ["Frank", "Elena", "Tomas"],
    "rodilla":  ["Ben", "Gisela", "Lucas"],
    "piernas":  ["Sabine", "Pablo", "Rosa"],
    "pies":     ["Mark", "Carmen", "Katrin"],
    "ojos":     ["Anna", "Javier", "Ines"],
}
EN_PIED = {"rodilla", "piernas", "pies"}
# Les maux : tener / haben + le nom. es / de : ce qui suit « tiene » / « hat » (sans article : fiebre, tos, gripe,
# Fieber, Husten ; avec : un resfriado, eine Grippe) ; ces / cde : le mot du corpus. emo : les images viennent
# d'Emotions (le visage « malade » est un rhume : mouchoir, nez rouge, echarpe).
SINTOMAS = {
    "fiebre":    {"es": "fiebre", "de": "Fieber", "ces": ["fiebre", "la"], "cde": ["Fieber", "das"],
                  "gens": ["Mark", "Rosa", "Heinz"],
                  "geste": "has a fever: flushed red cheeks, a sweaty forehead, glassy tired eyes, a digital thermometer in the mouth, one hand on the forehead, a blanket around the shoulders."},
    "tos":       {"es": "tos", "de": "Husten", "ces": ["tos", "la"], "cde": ["Husten", "der"],
                  "gens": ["Elena", "Javier", "Sabine"],
                  "geste": "has a bad cough: coughing hard into the bend of the elbow, the eyes squeezed shut, the other hand on the chest. A cough, not a sneeze."},
    "gripe":     {"es": "gripe", "de": "eine Grippe", "ces": ["gripe", "la"], "cde": ["Grippe", "die"],
                  "gens": ["Tomas", "Monika", "Lucas"],
                  "geste": "has the flu: lying in bed under a thick duvet, propped up on pillows, pale and exhausted, a box of tissues and a cup of tea on the bedside table."},
    "alergia":   {"es": "alergia", "de": "eine Allergie", "ces": ["alergia", "la"], "cde": ["Allergie", "die"],
                  "gens": ["Carmen", "Diego", "Lena"],
                  "geste": "has hay fever: sneezing into a tissue right next to a big vase of flowers, red itchy watery eyes."},
    "resfriado": {"es": "un resfriado", "de": "eine Erkältung", "ces": ["resfriado", "el"], "cde": ["Erkältung", "die"],
                  "gens": ["Mark", "Gisela", "Ben", "Pablo", "Marta"], "emo": "enfermo"},
}
# Estar / sein + l'adjectif : le lien avec Emotions, et leurs images.
ESTADOS = {
    "enfermo": {"es": ["enfermo", "enferma"], "de": "krank", "gens": ["Mark", "Gisela", "Ben", "Pablo", "Marta"]},
    "cansado": {"es": ["cansado", "cansada"], "de": "müde", "gens": ["Anna", "Mark", "Ben", "Rosa", "Pablo"]},
}
# Les maux qu'une image ne sait pas distinguer : jamais l'un comme leurre de l'autre.
VOISINS = {"rodilla": ["piernas"], "piernas": ["rodilla", "pies"], "pies": ["piernas"], "brazo": ["mano"], "mano": ["brazo"],
           "cabeza": ["oido", "ojos", "fiebre", "gripe"], "oido": ["cabeza", "muela"], "muela": ["oido"], "ojos": ["cabeza", "alergia", "cansado"],
           "garganta": ["tos", "gripe", "resfriado"], "fiebre": ["gripe", "resfriado", "enfermo", "cansado", "cabeza"],
           "gripe": ["fiebre", "resfriado", "tos", "enfermo", "cansado", "cabeza", "garganta"], "resfriado": ["gripe", "alergia", "enfermo", "fiebre", "tos", "garganta"],
           "tos": ["gripe", "resfriado", "garganta"], "alergia": ["resfriado", "ojos"], "enfermo": ["resfriado", "gripe", "fiebre", "cansado"],
           "cansado": ["enfermo", "gripe", "fiebre", "ojos", "piernas", "pies"], "estomago": [], "espalda": []}
# LES CONSEILS : « tienes que … » / « du musst … ». va : les maux pour lesquels il convient. Un conseil GENERAL
# (se reposer, aller chez le medecin, une pastille, de l'eau, rester au lit) convient a trop de maux pour servir de
# leurre : il n'est jamais qu'une bonne reponse. Les leurres sont des conseils PRECIS qui ne conviennent pas au mal
# montre ; dans le doute, un conseil « va » (de la glace sur une tete qui fait mal, un the pour le ventre) : une
# question n'a qu'une bonne reponse.
CONSEJOS = {
    "descansar": {"es": "descansar", "de": "dich ausruhen", "general": True,
                  "va": ["fiebre", "gripe", "resfriado", "cansado", "enfermo", "espalda", "cabeza", "piernas", "pies", "rodilla"]},
    "medico":    {"es": "ir al médico", "de": "zum Arzt gehen", "general": True,
                  "va": ["fiebre", "gripe", "tos", "alergia", "oido", "ojos", "estomago", "espalda", "rodilla", "brazo", "mano", "garganta", "enfermo"]},
    "pastilla":  {"es": "tomar una pastilla", "de": "eine Tablette nehmen", "general": True,
                  "va": ["cabeza", "fiebre", "gripe", "alergia", "muela", "espalda", "oido"]},
    "agua":      {"es": "beber mucha agua", "de": "viel Wasser trinken", "general": True,
                  "va": ["fiebre", "gripe", "resfriado", "cabeza", "enfermo"]},
    "cama":      {"es": "quedarte en la cama", "de": "im Bett bleiben", "general": True,
                  "va": ["fiebre", "gripe", "enfermo", "resfriado", "cansado", "espalda"]},
    "te":        {"es": "beber té con miel", "de": "Tee mit Honig trinken", "va": ["garganta", "tos", "resfriado", "gripe", "enfermo", "fiebre", "estomago", "cansado", "cabeza"]},
    "jarabe":    {"es": "tomar un jarabe", "de": "Hustensaft nehmen", "va": ["tos", "garganta", "resfriado", "gripe"]},
    "dentista":  {"es": "ir al dentista", "de": "zum Zahnarzt gehen", "va": ["muela"]},
    "tirita":    {"es": "ponerte una tirita", "de": "ein Pflaster draufkleben", "va": [], "images": ["dolor-rodilla-Ben"]},
    "sentarte":  {"es": "sentarte un rato", "de": "dich kurz hinsetzen", "va": ["pies", "piernas", "cansado", "rodilla", "espalda"]},
    "pantalla":  {"es": "mirar menos la pantalla", "de": "weniger auf den Bildschirm schauen", "va": ["ojos", "cabeza", "cansado"]},
    "hielo":     {"es": "ponerte hielo", "de": "Eis drauflegen", "va": ["brazo", "mano", "rodilla", "pies", "piernas", "espalda", "cabeza", "muela"]},
    "ligero":    {"es": "comer algo ligero", "de": "etwas Leichtes essen", "va": ["estomago", "gripe", "enfermo", "fiebre", "muela", "garganta"]},
}
# Le conseil de la decouverte, pour chaque mal (sa phrase a une voix).
CONSEJO_DECOUVERTE = {"fiebre": "cama", "tos": "jarabe", "gripe": "descansar", "alergia": "pastilla", "resfriado": "te",
                      "cansado": "sentarte", "muela": "dentista", "estomago": "ligero"}
# Les deux medecins du dialogue : la medica / die Aerztin, el medico / der Arzt (le genre se voit).
MEDICOS = {"f": "Ines", "m": "Pablo"}
GESTE_MEDECIN = ("is a doctor: wearing a white doctor's coat over the same clothes, a stethoscope around the neck, "
                 "sitting at a desk in a bright, simple consulting room, facing the camera with a kind, attentive smile; a computer and a few papers on the desk.")
# LE TOUCHER : les zones a la main (pour-cent de l'image), sur les silhouettes en pied de Decrire et sur deux visages
# ou les oreilles se voient (Mark, Tomas). Une partie peut avoir deux zones (gauche, droite, haut et bas du bras).
TOUCHER = {
    "corps": {
        "Mark":   {"cabeza": [[50, 4]], "cuello": [[50, 17]], "hombro": [[22, 21], [80, 21]], "brazo": [[14, 32], [88, 32], [12, 47], [90, 47]],
                   "mano": [[17, 59], [87, 59]], "pecho": [[50, 30]], "estomago": [[50, 46]], "piernas": [[32, 67], [68, 67], [28, 88], [72, 88]],
                   "rodilla": [[30, 79], [68, 79]], "pies": [[30, 96], [80, 96]]},
        "Carmen": {"cabeza": [[52, 5]], "cuello": [[52, 19]], "hombro": [[25, 22], [80, 22]], "brazo": [[14, 34], [90, 34], [8, 48], [94, 48]],
                   "mano": [[12, 58], [92, 58]], "pecho": [[52, 32]], "estomago": [[52, 48]], "piernas": [[40, 65], [64, 65], [40, 88], [63, 88]],
                   "rodilla": [[40, 78], [64, 78]], "pies": [[35, 97], [70, 97]]},
        "Tomas":  {"cabeza": [[48, 4.5]], "cuello": [[48, 18]], "hombro": [[20, 23], [78, 23]], "brazo": [[8, 33], [90, 33], [5, 45], [92, 45]],
                   "mano": [[8, 57], [88, 57]], "pecho": [[48, 32]], "estomago": [[48, 45]], "piernas": [[33, 65], [65, 65], [33, 88], [70, 88]],
                   "rodilla": [[33, 78], [65, 78]], "pies": [[30, 96], [75, 96]]},
        "Rosa":   {"cabeza": [[48, 5]], "cuello": [[48, 18]], "hombro": [[22, 21], [78, 21]], "brazo": [[10, 32], [88, 32], [5, 46], [93, 46]],
                   "mano": [[5, 57], [90, 57]], "pecho": [[48, 30]], "estomago": [[48, 45]], "piernas": [[35, 63], [62, 63], [33, 88], [62, 88]],
                   "rodilla": [[35, 77], [62, 77]], "pies": [[30, 97], [68, 97]]},
    },
    "cara": {
        "Mark":  {"ojos": [[41, 62], [59, 62]], "nariz": [[51, 71]], "boca": [[51, 84]], "oreja": [[29, 66], [73, 64]]},
        "Tomas": {"ojos": [[43, 42], [62, 42]], "nariz": [[53, 53]], "boca": [[54, 66]], "oreja": [[33, 52], [72, 54]]},
    },
}
# La decouverte « j'ai mal » : la personne de chaque fiche (sa phrase a une voix).
DECOUVERTE = {"cabeza": "Anna", "garganta": "Mark", "oido": "Carmen", "muela": "Javier", "espalda": "Heinz", "estomago": "Ines",
              "brazo": "Jan", "mano": "Frank", "rodilla": "Gisela", "piernas": "Sabine", "pies": "Carmen", "ojos": "Javier",
              "fiebre": "Mark", "tos": "Elena", "gripe": "Tomas", "alergia": "Lena", "resfriado": "Gisela", "cansado": "Rosa"}

MEME = ("The same person as in the reference picture: exactly the same face, the same age, the same hair, the same skin, "
        "the same glasses or beard if any, the same body and the same clothes. ")
BUSTE = (" A photorealistic half-length portrait, from the top of the head to the hips, facing the camera, centred. Plain "
         "light grey studio background with even soft light, nothing else in the picture, no text, no logos. Natural skin "
         "texture, no retouching. A moderate, everyday pain, not dramatic, no blood. The person: ")
PIED = (" A photorealistic full-body photograph, from the top of the head to the feet, the person sitting and centred. Plain "
        "light grey studio background with even soft light, only the seat, nothing else, no text, no logos. Natural skin "
        "texture, no retouching. A moderate, everyday pain, not dramatic, no blood. The person: ")
SITUATION = (" A photorealistic photograph, natural light, natural colours, no text, no logos. The person is clearly visible, "
             "in the centre, the face easy to read. The person: ")


def images():
    out = {}
    for part, gens in DOLORES.items():
        for p in gens:
            geste = GESTE_A_PART.get((part, p), GESTES[part])
            out["dolor-" + part + "-" + p] = (p, MEME + (PIED if part in EN_PIED else BUSTE) + geste, "3:4")
    for s, d in SINTOMAS.items():
        if d.get("emo"):
            continue
        for p in d["gens"]:
            out["sintoma-" + s + "-" + p] = (p, MEME + (SITUATION if s == "gripe" else BUSTE) + d["geste"], "3:4")
    for sexe, p in MEDICOS.items():
        out["medico-" + p] = (p, MEME + SITUATION + GESTE_MEDECIN, "4:3")
    return out


def verifier_regles():
    fautes = []
    par = {}
    for part, gens in DOLORES.items():
        if len(set(gens)) != len(gens):
            fautes.append("%s : deux fois la meme personne" % part)
        if len({SEXE[p] for p in gens}) < 2:
            fautes.append("%s : un seul sexe" % part)
        for p in gens:
            par[p] = par.get(p, 0) + 1
    fautes += ["%s : %d endroits (2 au plus)" % (p, n) for p, n in par.items() if n > 2]
    for (part, p) in GESTE_A_PART:
        if p not in DOLORES[part]:
            fautes.append("geste a part de %s pour %s, absent de DOLORES" % (p, part))
    if "Ben" in [p for part, g in DOLORES.items() for p in g if part != "rodilla"]:
        fautes.append("Ben (l'enfant) n'a qu'un genou ecorche")
    if "Ben" in [p for s, d in SINTOMAS.items() if not d.get("emo") for p in d["gens"]]:
        fautes.append("Ben (l'enfant) n'a qu'un rhume, deja fait dans Emotions")
    tous = set(PARTES) | set(SINTOMAS) | set(ESTADOS)
    for k, v in VOISINS.items():
        fautes += ["voisin inconnu %s -> %s" % (k, x) for x in v if x not in tous]
    for c, d in CONSEJOS.items():
        fautes += ["conseil %s : mal inconnu %s" % (c, x) for x in d["va"] if x not in tous]
    return fautes


def ecrire_json():
    gens = sorted({p for g in DOLORES.values() for p in g} | {p for d in SINTOMAS.values() for p in d["gens"]}
                  | {p for d in ESTADOS.values() for p in d["gens"]} | set(MEDICOS.values()) | set(TOUCHER["corps"]) | set(TOUCHER["cara"]))
    partes = {}
    for k, v in PARTES.items():
        d = {"es": v["es"], "de": v["de"],
             "ces": v.get("ces") or [v["es"][1], v["es"][0]], "cde": v.get("cde") or [v["de"][1], v["de"][0]]}
        for c in ("dolor", "toucher", "un"):
            if v.get(c):
                d[c] = v[c]
        partes[k] = d
    d = {"sexe": {p: SEXE[p] for p in gens}, "noms": NOMS, "partes": partes, "dolores": DOLORES,
         "sintomas": {k: {c: v[c] for c in ("es", "de", "ces", "cde", "gens", "emo") if c in v} for k, v in SINTOMAS.items()},
         "estados": ESTADOS, "voisins": VOISINS, "consejos": CONSEJOS, "consejoDecouverte": CONSEJO_DECOUVERTE,
         "medicos": MEDICOS, "toucher": TOUCHER, "decouverte": DECOUVERTE}
    texte = json.dumps(d, ensure_ascii=False, indent=1) + "\n"
    chemin = os.path.join(RACINE, "visuel", "prototype", "cuerpo", "cuerpo.json")
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(texte)


# Les mots du dialogue chez le medecin, au corpus (les questions de « En la consulta » les visent).
# S'y ajoutent les leurres du dialogue, pour traduire un mauvais choix (« Tu as choisi : la tirita — le pansement »).
CONSULTA = {"es": [["médico", "el"], ["médica", "la"], ["receta", "la"], ["cita", "la"], ["tirita", "la"], ["pastilla", "la"], ["paciente", "el"]],
            "de": [["Arzt", "der"], ["Ärztin", "die"], ["Rezept", "das"], ["Termin", "der"], ["Besserung", "die"], ["Pflaster", "das"], ["Patient", "der"]]}
# Les mots ajoutes au corpus pour ce theme (3 nov., accord de Jacques : « go » ; espanol/ajouts/cuerpo-salud.json,
# ajouts/cuerpo-schmerzen.json). Une copie du depot d'avant leur ajout les dirait « hors jeu » : le tirage les laisse.
A_AJOUTER = {"es": ["garganta", "oído", "muela"],
             "de": ["Kopfschmerzen", "Halsschmerzen", "Bauchschmerzen", "Zahnschmerzen", "Rückenschmerzen"]}


def ecrire_gloses():
    """Le mot de la question et sa traduction du corpus, pour les langues ou l'on ne fabrique pas la phrase entiere
    (ar, tr, uk, fa, pl, ru) : sous la phrase juste, « la rodilla — коліно ». Meme forme que familia/gloses.json.
    Fichier DERIVE : le refaire."""
    def lire(p):
        return json.load(io.open(os.path.join(RACINE, p), encoding="utf-8"))
    LDE = {"fr": "traduction", "en": "traduction_en", "tr": "traduction_tr", "uk": "traduction_uk", "fa": "traduction_fa",
           "ar": "traduction_ar", "pt": "traduction_pt", "pl": "traduction_pl", "ru": "traduction_ru"}
    LES = {"fr": "traduction", "en": "traduction_en", "pt": "traduction_pt", "ar": "traduction_ar", "de": "traduction_de"}
    adj = lambda p: [e for v in lire(p).values() for e in v if isinstance(e, dict)]
    # le sens de la sante d'abord : « das Rezept » est l'ordonnance (gesundheit_a1), pas la recette (essen_trinken_b1)
    sante = lambda t: any(x in t["id"] for x in ("gesundheit", "koerper", "cuerpo", "salud", "medicina"))
    noms = lambda p: [m for t in sorted(lire(p)["themes"], key=lambda t: not sante(t)) for m in t["mots"]]
    voulus = {"es": {}, "de": {}}
    for v in PARTES.values():
        ces = v.get("ces") or [v["es"][1], v["es"][0]]
        cde = v.get("cde") or [v["de"][1], v["de"][0]]
        voulus["es"][ces[0]] = ces[1]
        voulus["de"][cde[0]] = cde[1]
    for v in SINTOMAS.values():
        voulus["es"][v["ces"][0]] = v["ces"][1]
        voulus["de"][v["cde"][0]] = v["cde"][1]
    for l in ("es", "de"):
        for m, g in CONSULTA[l]:
            voulus[l][m] = g
    for m in A_AJOUTER["de"]:
        voulus["de"][m] = "die"                      # les composes en -schmerzen, au pluriel seulement
    adjs = {"es": [e["es"][0] for e in ESTADOS.values()], "de": [e["de"] for e in ESTADOS.values()] + ["gesund"]}
    out = {"de": {}, "es": {}}
    for langue, a, ns, champs in (("de", adj("adjectif.json"), noms("themes.json"), LDE),
                                  ("es", adj("espanol/datos/adjetivos.json"), noms("espanol/datos/temas.json"), LES)):
        for e in a:
            if e["mot"] in adjs[langue] and e["mot"] not in out[langue]:
                out[langue][e["mot"]] = {l: e[c] for l, c in champs.items() if e.get(c)}
        for m in ns:
            if voulus[langue].get(m["mot"]) == m.get("genre"):
                out[langue].setdefault(m["genre"] + " " + m["mot"], {l: m[c] for l, c in champs.items() if m.get(c)})
    manque = [g + " " + m for l in voulus for m, g in voulus[l].items() if (g + " " + m) not in out[l] and m not in A_AJOUTER[l]]
    manque += [m for l in adjs for m in adjs[l] if m not in out[l]]
    assert not manque, "absents du corpus : %s" % manque
    io.open(os.path.join(RACINE, "visuel", "prototype", "cuerpo", "gloses.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n")


def main():
    montrer, refaire = "--montrer" in sys.argv, "--refaire" in sys.argv
    tout = images()
    noms = [a for a in sys.argv[1:] if not a.startswith("--")] or list(tout)
    inconnus = [n for n in noms if n not in tout]
    if inconnus:
        sys.exit("  inconnu : " + ", ".join(inconnus))
    fautes = verifier_regles()
    if fautes:
        sys.exit("  distribution fautive :\n  " + "\n  ".join(fautes))
    ecrire_json()
    ecrire_gloses()
    if "--json" in sys.argv:
        print("  cuerpo.json et gloses.json ecrits ; %d images au plan (%.2f $)" % (len(tout), len(tout) * PRIX))
        return
    os.makedirs(DOSSIER, exist_ok=True)
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
    if montrer:
        for n in a_faire:
            print("\n  %s (%s, %s)\n  %s" % (n, tout[n][0], tout[n][2], tout[n][1]))
        return
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    if not os.environ.get("FAL_KEY"):
        os.environ["FAL_KEY"] = io.open(PRINCIPAL + "/fal.secret", encoding="utf-8-sig").read().strip()
    cle = O.cle()
    depots = {}
    for nom in a_faire:
        source, prompt, fmt = tout[nom]
        print("\n  %s\n  %s" % (nom, prompt))
        if source not in depots:
            depots[source] = O.deposer(SOURCES[source], "image/png", cle)[0]
        corps = {"prompt": prompt, "image_urls": [depots[source]], "aspect_ratio": fmt, "resolution": "2K",
                 "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
        try:
            res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        except O.ResultatIndisponible as err:
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
