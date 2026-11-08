# -*- coding: utf-8 -*-
"""« Les métiers » -- le theme illustre des PROFESSIONS, en espagnol et en allemand (3 nov. 2026).
LA SEULE SOURCE du theme : les metiers (masculin et feminin), ou chacun travaille, ce qu'il fait, les personnes et
leurs images, les phrases et leurs traductions. La page (visuel/prototype/metiers.html) n'ecrit aucune phrase.

    python visuel/metiers/metiers.py --json          # visuel/prototype/metiers/metiers.json seul, gratuit
    python visuel/metiers/metiers.py --scenes        # les personnes des scenes, recadrees (gratuit)
    python visuel/metiers/metiers.py --provisoires   # les portraits en attente, faits des images de Decrire (gratuit, PAS a committer)
    python visuel/metiers/metiers.py --montrer       # les prompts seuls, gratuit
    python visuel/metiers/metiers.py --payer [noms]  # les portraits fal qui manquent, 0,15 $ chacun -- ACCORD DE JACQUES
    python visuel/metiers/metiers.py --webp          # les originaux -> visuel/prototype/metiers/*.webp

CE QU'ON DOIT POUVOIR DIRE (le chef, 3 nov.) : qui fait quoi, ou chacun travaille, « Je suis medecin » SANS ARTICLE
(Ich bin Arztin, Soy medica), et le masculin et le feminin (medico / medica, Arzt / Arztin).

L'ANGLE (regle 2 des themes : pas de theme qui refait une scene). Les scenes explorent un LIEU et ses objets ; ici,
ce sont les PERSONNES : leur metier, son feminin, leur lieu de travail, leur geste. Neuf professionnels des scenes
(la medecin du cabinet, la pharmacienne, la boulangere, le coiffeur, le professeur du cours d'espagnol, la serveuse,
le mecanicien de l'atelier de velos, la vendeuse, le receptionniste de l'hotel) sont RECADRES dans leur scene : ils
sont gratuits et ils montrent ou ils travaillent. Dix portraits de plus donnent l'AUTRE genre (ou un metier sans
scene) : les personnes de « Decrire une personne », en tenue de travail, sur le fond de studio des themes. Pas Mark
ni Anna (Anna est employee au guichet de l'aeroport, son histoire ne se refait pas ici), pas la famille d'Anna.

LES IMAGES : chaque portrait est une RETOUCHE de l'image de la personne dans Decrire (visuel/descripcion/img, hors
depot), pour qu'elle reste elle-meme (nano-banana-pro/edit, 0,15 $). Chaque image se verifie contre sa description.
Originaux : visuel/metiers/img/ (hors depot) ; webp : visuel/prototype/metiers/.

LA CONTINUITE DES LIEUX (regle de Jacques du 3 nov., verifiee avant toute generation) : aucun lieu neuf. Les lieux de
travail montres sont les images MEMES des scenes (recadrees, pas regenerees) ; les portraits sont sur le fond de
studio des themes, sans decor. Rien a ajouter a video/LIEUX.md.
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.dirname(ICI))
import personnes as PERS                                     # noqa: E402 -- la fiche commune (6 nov. 2026)
PROTO = os.path.join(RACINE, "visuel", "prototype", "metiers")
SCENES = os.path.join(RACINE, "visuel", "prototype")
IMG = os.path.join(ICI, "img")
# les originaux de Decrire une personne (hors depot) : dans le dossier principal, un worktree ne les a pas
DECRIRE = os.environ.get("DECRIRE_IMG", "C:/Users/jacqu/OneDrive/Desktop/Mes Projets/DeutschAI/visuel/descripcion/img")
MODELE, EDIT, PRIX = "fal-ai/nano-banana-pro", "fal-ai/nano-banana-pro/edit", 0.15

# ---------------------------------------------------------------------------------------------------------------
# LES METIERS. de / es : (masculin, feminin), chacun (article, mot) ; fr, en, pt (bresilien, la langue d'interface) :
# (masculin, feminin) sans article. Les douze sont au corpus des deux langues, au masculin et au feminin (les
# manquants : ajouts/theme-metiers.json et espanol/ajouts/metiers.json).
M = {}
def metier(id, de, es, fr, en, pt, lieux, act, faux, pas_faux=(), confus=()):
    M[id] = {"de": de, "es": es, "fr": fr, "en": en, "pt": pt, "lieux": list(lieux), "act": act,
             "faux": faux, "pasFaux": list(pas_faux), "confus": list(confus)}

# act : ce que fait la personne -- par langue (verbe a la 3e personne, infinitif, complement) ; fr, en, pt : le
# groupe verbal entier. faux : les verbes CLAIREMENT faux avec ce complement (« backt Brot » : jamais « schneidet »,
# on coupe du pain ; jamais « verkauft », on en vend), les seuls que la page propose en leurre.
metier("arzt", (("der", "Arzt"), ("die", "Ärztin")), (("el", "médico"), ("la", "médica")),
       ("médecin", "médecin"), ("doctor", "doctor"), ("médico", "médica"), ["praxis", "krankenhaus"],
       {"de": ("untersucht", "untersuchen", "die Patienten"), "es": ("examina", "examinar", "a los pacientes"),
        "fr": "examine les patients", "en": "examines the patients", "pt": "examina os pacientes"},
       {"de": ["backt", "schneidet", "repariert", "verkauft", "regelt"], "es": ["hace", "corta", "repara", "vende", "cocina"]},
       confus=["pfleger"])
metier("apotheker", (("der", "Apotheker"), ("die", "Apothekerin")), (("el", "farmacéutico"), ("la", "farmacéutica")),
       ("pharmacien", "pharmacienne"), ("pharmacist", "pharmacist"), ("farmacêutico", "farmacêutica"), ["apotheke"],
       {"de": ("verkauft", "verkaufen", "Medikamente"), "es": ("vende", "vender", "medicamentos"),
        "fr": "vend des médicaments", "en": "sells medicine", "pt": "vende remédios"},
       {"de": ["backt", "schneidet", "repariert", "regelt", "unterrichtet"], "es": ["corta", "cocina", "repara", "enseña", "controla"]},
       pas_faux=["krankenhaus"])
metier("baecker", (("der", "Bäcker"), ("die", "Bäckerin")), (("el", "panadero"), ("la", "panadera")),
       ("boulanger", "boulangère"), ("baker", "baker"), ("padeiro", "padeira"), ["baeckerei"],
       {"de": ("backt", "backen", "Brot"), "es": ("hace", "hacer", "pan"),
        "fr": "fait du pain", "en": "bakes bread", "pt": "faz pão"},
       {"de": ["repariert", "regelt", "unterrichtet", "untersucht", "pflegt"], "es": ["repara", "examina", "enseña", "controla", "cuida"]})
metier("friseur", (("der", "Friseur"), ("die", "Friseurin")), (("el", "peluquero"), ("la", "peluquera")),
       ("coiffeur", "coiffeuse"), ("hairdresser", "hairdresser"), ("cabeleireiro", "cabeleireira"), ["salon"],
       {"de": ("schneidet", "schneiden", "Haare"), "es": ("corta", "cortar", "el pelo"),
        "fr": "coupe les cheveux", "en": "cuts hair", "pt": "corta cabelo"},
       {"de": ["backt", "repariert", "regelt", "kocht", "unterrichtet"], "es": ["cocina", "repara", "enseña", "controla", "sirve"]})
metier("lehrer", (("der", "Lehrer"), ("die", "Lehrerin")), (("el", "profesor"), ("la", "profesora")),
       ("professeur", "professeure"), ("teacher", "teacher"), ("professor", "professora"), ["schule"],
       {"de": ("unterrichtet", "unterrichten", "die Kinder"), "es": ("enseña", "enseñar", "a los niños"),
        "fr": "enseigne aux enfants", "en": "teaches the children", "pt": "ensina as crianças"},
       {"de": ["backt", "repariert", "schneidet", "verkauft", "regelt"], "es": ["corta", "repara", "vende", "cocina", "controla"]})
metier("kellner", (("der", "Kellner"), ("die", "Kellnerin")), (("el", "camarero"), ("la", "camarera")),
       ("serveur", "serveuse"), ("waiter", "waitress"), ("garçom", "garçonete"), ["restaurant"],
       {"de": ("bringt", "bringen", "das Essen"), "es": ("sirve", "servir", "la comida"),
        "fr": "apporte les plats", "en": "brings the food", "pt": "serve a comida"},
       {"de": ["repariert", "schneidet", "regelt", "unterrichtet", "untersucht"], "es": ["repara", "corta", "enseña", "examina", "controla"]},
       pas_faux=["kueche", "hotel"], confus=["koch"])
metier("koch", (("der", "Koch"), ("die", "Köchin")), (("el", "cocinero"), ("la", "cocinera")),
       ("cuisinier", "cuisinière"), ("cook", "cook"), ("cozinheiro", "cozinheira"), ["kueche", "restaurant"],
       {"de": ("kocht", "kochen", "für die Gäste"), "es": ("cocina", "cocinar", "para los clientes"),
        "fr": "cuisine pour les clients", "en": "cooks for the guests", "pt": "cozinha para os clientes"},
       {"de": ["repariert", "regelt", "untersucht", "unterrichtet"], "es": ["repara", "examina", "enseña", "controla"]},
       pas_faux=["hotel", "krankenhaus", "schule"], confus=["kellner"])
metier("mechaniker", (("der", "Mechaniker"), ("die", "Mechanikerin")), (("el", "mecánico"), ("la", "mecánica")),
       ("mécanicien", "mécanicienne"), ("mechanic", "mechanic"), ("mecânico", "mecânica"), ["werkstatt"],
       {"de": ("repariert", "reparieren", "Fahrräder"), "es": ("repara", "reparar", "bicicletas"),
        "fr": "répare des vélos", "en": "repairs bikes", "pt": "conserta bicicletas"},
       {"de": ["backt", "kocht", "unterrichtet", "pflegt", "regelt"], "es": ["cocina", "corta", "enseña", "cuida", "sirve"]})
metier("verkaeufer", (("der", "Verkäufer"), ("die", "Verkäuferin")), (("el", "dependiente"), ("la", "dependienta")),
       ("vendeur", "vendeuse"), ("salesperson", "salesperson"), ("vendedor", "vendedora"), ["geschaeft"],
       {"de": ("verkauft", "verkaufen", "Kleidung"), "es": ("vende", "vender", "ropa"),
        "fr": "vend des vêtements", "en": "sells clothes", "pt": "vende roupas"},
       {"de": ["backt", "kocht", "untersucht", "regelt", "unterrichtet"], "es": ["cocina", "examina", "enseña", "controla", "sirve"]},
       pas_faux=["baeckerei", "apotheke"])
metier("polizist", (("der", "Polizist"), ("die", "Polizistin")), (("el", "policía"), ("la", "policía")),
       ("policier", "policière"), ("police officer", "police officer"), ("policial", "policial"), ["polizei"],
       {"de": ("regelt", "regeln", "den Verkehr"), "es": ("controla", "controlar", "el tráfico"),
        "fr": "règle la circulation", "en": "directs the traffic", "pt": "controla o trânsito"},
       {"de": ["backt", "schneidet", "kocht", "verkauft", "pflegt", "unterrichtet"], "es": ["hace", "corta", "cocina", "vende", "sirve", "enseña"]})
metier("pfleger", (("der", "Krankenpfleger"), ("die", "Krankenschwester")), (("el", "enfermero"), ("la", "enfermera")),
       ("infirmier", "infirmière"), ("nurse", "nurse"), ("enfermeiro", "enfermeira"), ["krankenhaus"],
       {"de": ("pflegt", "pflegen", "die Kranken"), "es": ("cuida", "cuidar", "a los enfermos"),
        "fr": "soigne les malades", "en": "looks after the sick", "pt": "cuida dos doentes"},
       {"de": ["backt", "schneidet", "repariert", "verkauft", "regelt"], "es": ["hace", "corta", "repara", "vende", "cocina"]},
       pas_faux=["praxis"], confus=["arzt"])
metier("rezeptionist", (("der", "Rezeptionist"), ("die", "Rezeptionistin")), (("el", "recepcionista"), ("la", "recepcionista")),
       ("réceptionniste", "réceptionniste"), ("receptionist", "receptionist"), ("recepcionista", "recepcionista"), ["hotel"],
       {"de": ("gibt", "geben", "den Gästen den Schlüssel"), "es": ("da", "dar", "la llave a los huéspedes"),
        "fr": "donne la clé aux clients", "en": "gives the guests the key", "pt": "entrega a chave aos hóspedes"},
       {"de": ["backt", "schneidet", "repariert", "untersucht", "unterrichtet"], "es": ["corta", "cocina", "repara", "examina", "enseña"]},
       pas_faux=["krankenhaus", "praxis"])

# LES LIEUX : la phrase (« in einer Praxis », la preposition et le datif), le nom au corpus (le mot que la question
# teste), et fr, en, pt. « an einer Schule » : un professeur travaille A une ecole ; « bei der Polizei ».
L = {
    "praxis":      {"de": "in einer Praxis", "es": "en una consulta", "nde": ("die", "Praxis"), "nes": ("la", "consulta"),
                    "fr": "dans un cabinet médical", "en": "in a doctor's office", "pt": "em um consultório"},
    "krankenhaus": {"de": "im Krankenhaus", "es": "en el hospital", "nde": ("das", "Krankenhaus"), "nes": ("el", "hospital"),
                    "fr": "à l'hôpital", "en": "in a hospital", "pt": "no hospital"},
    "apotheke":    {"de": "in einer Apotheke", "es": "en una farmacia", "nde": ("die", "Apotheke"), "nes": ("la", "farmacia"),
                    "fr": "dans une pharmacie", "en": "at a pharmacy", "pt": "em uma farmácia"},
    "baeckerei":   {"de": "in einer Bäckerei", "es": "en una panadería", "nde": ("die", "Bäckerei"), "nes": ("la", "panadería"),
                    "fr": "dans une boulangerie", "en": "at a bakery", "pt": "em uma padaria"},
    "salon":       {"de": "in einem Friseursalon", "es": "en una peluquería", "nde": ("der", "Friseursalon"), "nes": ("la", "peluquería"),
                    "fr": "dans un salon de coiffure", "en": "at a hair salon", "pt": "em um salão de beleza"},
    "schule":      {"de": "an einer Schule", "es": "en un colegio", "nde": ("die", "Schule"), "nes": ("el", "colegio"),
                    "fr": "dans une école", "en": "at a school", "pt": "em uma escola"},
    "restaurant":  {"de": "in einem Restaurant", "es": "en un restaurante", "nde": ("das", "Restaurant"), "nes": ("el", "restaurante"),
                    "fr": "dans un restaurant", "en": "in a restaurant", "pt": "em um restaurante"},
    "kueche":      {"de": "in der Küche", "es": "en la cocina", "nde": ("die", "Küche"), "nes": ("la", "cocina"),
                    "fr": "en cuisine", "en": "in the kitchen", "pt": "na cozinha"},
    "werkstatt":   {"de": "in einer Werkstatt", "es": "en un taller", "nde": ("die", "Werkstatt"), "nes": ("el", "taller"),
                    "fr": "dans un atelier", "en": "in a workshop", "pt": "em uma oficina"},
    "geschaeft":   {"de": "in einem Geschäft", "es": "en una tienda", "nde": ("das", "Geschäft"), "nes": ("la", "tienda"),
                    "fr": "dans un magasin", "en": "in a store", "pt": "em uma loja"},
    "polizei":     {"de": "bei der Polizei", "es": "en la comisaría", "nde": ("die", "Polizei"), "nes": ("la", "comisaría"),
                    "fr": "dans la police", "en": "for the police", "pt": "na polícia"},
    "hotel":       {"de": "in einem Hotel", "es": "en un hotel", "nde": ("das", "Hotel"), "nes": ("el", "hotel"),
                    "fr": "dans un hôtel", "en": "in a hotel", "pt": "em um hotel"},
}

# ---------------------------------------------------------------------------------------------------------------
# LES PERSONNES. Les scenes : (scene, metier, sexe, centre x %, centre y %, largeur %) -- un cadre 3:4 autour du
# professionnel, pris dans l'image de la scene (gratuit). Les portraits : (metier, sexe, tenue et geste) ; la personne
# est celle de Decrire (meme visage, meme silhouette), en tenue de travail.
SCENE_P = {
    "s-aerztin":      ("arztpraxis", "arzt", "f", 78, 54, 46),
    "s-apothekerin":  ("apotheke", "apotheker", "f", 22, 46, 46),
    "s-baeckerin":    ("baeckerei", "baecker", "f", 22, 46, 46),
    "s-friseur":      ("friseur", "friseur", "m", 62, 44, 52),
    "s-lehrer":       ("klassenzimmer", "lehrer", "m", 18, 45, 42),
    "s-kellnerin":    ("restaurant", "kellner", "f", 52, 46, 42),
    "s-mechaniker":   ("fahrradwerkstatt", "mechaniker", "m", 66, 58, 52),
    "s-verkaeuferin": ("kleidergeschaeft", "verkaeufer", "f", 81, 56, 38),
    "s-rezeptionist": ("hotel", "rezeptionist", "m", 19, 46, 44),
}
# le professeur de la scene est celui du cours d'espagnol de la Volkshochschule (« Im Spanischkurs ») : il enseigne
# l'espagnol, pas « aux enfants »
ACT_SCENE = {"s-lehrer": {"de": ("unterrichtet", "unterrichten", "Spanisch"), "es": ("enseña", "enseñar", "español"),
                          "fr": "enseigne l'espagnol", "en": "teaches Spanish", "pt": "ensina espanhol"}}
UNIFORME = ("the current German police uniform: dark blue trousers, a light blue shirt and a dark blue police jacket with "
            "the word POLIZEI on the chest, a dark blue police cap")
PORTRAITS = {   # nom : (metier, sexe, metier en anglais, tenue, geste)
    "Diego":  ("arzt", "m", "a doctor", "a white knee-length doctor's coat over a light blue shirt and dark trousers, a stethoscope around his neck, his usual glasses",
               "He holds a clipboard against his chest."),
    "Pablo":  ("baecker", "m", "a baker", "a white baker's jacket, a long white apron lightly dusted with flour and a white baker's cap; his usual beard",
               "He holds a large wooden tray of fresh crusty bread loaves and pretzels in both hands."),
    "Ines":   ("friseur", "f", "a hairdresser", "a black hairdresser's tunic over black trousers and a small black tool belt with combs and brushes at the waist; her short red hair and her tattoo as before",
               "She holds a pair of hairdressing scissors in one hand and a comb in the other."),
    "Marta":  ("lehrer", "f", "a schoolteacher", "a smart cardigan over a blouse, her usual glasses",
               "She stands next to a small green chalkboard on an easel with a simple chalk drawing of a sun, a house and a tree (no writing at all), a piece of chalk in one hand and a few exercise books in the other."),
    "Javier": ("koch", "m", "a chef", "a white double-breasted chef's jacket, a tall white chef's hat and a black apron; his usual moustache",
               "He holds a frying pan with colourful vegetables."),
    "Elena":  ("polizist", "f", "a German police officer", UNIFORME + "; her long blond hair tied back",
               "She stands upright, friendly and confident."),
    "Tomas":  ("polizist", "m", "a German police officer", UNIFORME + "; his usual goatee",
               "He stands upright, friendly and confident."),
    "Rosa":   ("mechaniker", "f", "a bicycle mechanic", "dark blue work overalls with the sleeves rolled up, a little grease on her hands; her long black hair tied back",
               "She holds a bicycle wheel in one hand and a spanner in the other."),
    "Carmen": ("koch", "f", "a cook", "a white chef's jacket, a black apron and a white chef's cap over her curly red hair, her usual glasses",
               "She holds a wooden spoon over a steaming pot."),
    "Lucas":  ("pfleger", "m", "a hospital nurse", "light blue hospital scrubs (tunic and trousers) with a small watch pinned to the chest, no sunglasses; his usual beard",
               "He holds a small tray with a glass of water and a few pills."),
}
ESSAI = ["Diego", "Pablo", "Ines", "Marta", "Javier", "Elena"]     # la planche d'essai (6 images, 0,90 $)


def prompt_de(nom):
    met, sexe, qui, tenue, geste = PORTRAITS[nom]
    texte = " except the word POLIZEI on the uniform" if met == "polizist" else ""
    return ("Exactly the same person as in the reference picture: the same face, the same skin, the same hair colour, "
            "the same body shape and build, the same height and the same age. Keep the identity exactly. "
            "Now photographed at work as %s, wearing %s. %s Three-quarter shot from the knees up, facing the camera, "
            "a warm natural smile. Plain seamless light grey studio background, soft even studio light, photorealistic "
            "photograph, natural colours. No other people, no text, no letters, no logos%s."
            % (qui, tenue, geste, texte))


# ---------------------------------------------------------------------------------------------------------------
# LES PHRASES. Tout se fabrique ici, par langue apprise, avec leurs traductions (fr, en, pt ; et de pour qui
# apprend l'espagnol), et la page les prend telles quelles.
G = {"m": 0, "f": 1}
VOY = "aeéèêiîoôuh"
def fr_art(met, s, defini=True):
    mot = M[met]["fr"][G[s]]
    if defini:
        return ("l'" if mot[0] in VOY else ("le " if s == "m" else "la ")) + mot
    return ("un " if s == "m" else "une ") + mot
def en_nom(met, s): return M[met]["en"][G[s]]
def en_a(mot): return ("an " if mot[0] in "aeiou" else "a ") + mot
def pt_art(met, s): return ("o " if s == "m" else "a ") + M[met]["pt"][G[s]]
def forme(app, met, s): return M[met][app][G[s]]                  # (article, mot)
def aff(app, met, s): a, m = forme(app, met, s); return a + " " + m
def maj(t): return t[0].upper() + t[1:]


def personnes():
    """Les dix-neuf personnes : id -> {img, sexe, metier, nom, scene}."""
    P = {}
    for id, (sc, met, s, *_r) in SCENE_P.items():
        P[id] = {"img": id, "sexe": s, "metier": met, "nom": None, "scene": sc}
    for nom, (met, s, *_r) in PORTRAITS.items():
        # le metier et le prenom ecrit viennent de la fiche commune (visuel/personnes.json) : « Inés », pas « Ines »
        if PERS.metier(nom) != met or PERS.sexe(nom) != s:
            raise SystemExit("%s : %s ici, %s dans visuel/personnes.json" % (nom, met, PERS.metier(nom)))
        P[nom] = {"img": nom, "sexe": s, "metier": met, "nom": PERS.nom(nom), "scene": None}
    return P


def act_de(pid, P):
    return ACT_SCENE.get(pid, M[P[pid]["metier"]]["act"])


def construire():
    P = personnes()
    d = {"_lisez_moi": "FABRIQUE par visuel/metiers/metiers.py : ne pas corriger a la main.",
         "metiers": {}, "lieux": {}, "personnes": P, "phrases": {"de": {}, "es": {}}, "paires": {"de": [], "es": []},
         "sansImage": {"de": [], "es": []}, "trad": {"de": {}, "es": {}}, "gloses": {"de": {}, "es": {}}}
    for id, m in M.items():
        d["metiers"][id] = {"de": {s: {"genre": forme("de", id, s)[0], "mot": forme("de", id, s)[1]} for s in "mf"},
                            "es": {s: {"genre": forme("es", id, s)[0], "mot": forme("es", id, s)[1]} for s in "mf"},
                            "lieux": m["lieux"], "pasFaux": m["pasFaux"], "confus": m["confus"],
                            "verbes": {"de": m["act"]["de"][0], "es": m["act"]["es"][0]},
                            "inf": {"de": m["act"]["de"][1], "es": m["act"]["es"][1]}, "faux": m["faux"],
                            "trad": {"fr": [fr_art(id, "m"), fr_art(id, "f")], "en": [en_nom(id, "m"), en_nom(id, "f")],
                                     "pt": [pt_art(id, "m"), pt_art(id, "f")], "de": [aff("de", id, "m"), aff("de", id, "f")]}}
    for id, l in L.items():
        # fr, en, pt (et de pour qui apprend l'espagnol) : le lieu CHOISI traduit, apres une erreur
        d["lieux"][id] = {"de": l["de"], "es": l["es"], "nom": {"de": {"genre": l["nde"][0], "mot": l["nde"][1]},
                                                                "es": {"genre": l["nes"][0], "mot": l["nes"][1]}},
                          "trad": {"fr": l["fr"], "en": l["en"], "pt": l["pt"], "de": l["de"]}}
    T = d["trad"]
    def tr(app, phrase, fr, en, pt, de=None):
        T[app][phrase] = {"fr": fr, "en": en, "pt": pt}
        if app == "es" and de: T[app][phrase]["de"] = de

    for pid, p in P.items():
        met, s, nom = p["metier"], p["sexe"], p["nom"]
        a = act_de(pid, P)
        pron_de, pron_fr, pron_en, pron_pt = ("Er", "Il", "He", "Ele") if s == "m" else ("Sie", "Elle", "She", "Ela")
        de_art, de_mot = forme("de", met, s); es_art, es_mot = forme("es", met, s)
        fr_m, en_m, pt_m = M[met]["fr"][G[s]], en_nom(met, s), M[met]["pt"][G[s]]
        # le sujet d'une phrase : le prenom, ou pour une personne des scenes « die Arztin » / « la medica »
        suj = {"de": nom or maj(aff("de", met, s)), "es": nom or maj(aff("es", met, s)),
               "fr": nom or maj(fr_art(met, s)), "en": nom or "The " + en_m, "pt": nom or maj(pt_art(met, s))}
        # le sujet d'une phrase sur le metier : le prenom, sinon le pronom (« Sie ist Arztin. », « Es medica. »)
        sm = {"de": nom or pron_de, "fr": nom or pron_fr, "en": nom or pron_en, "pt": nom or pron_pt}
        for app in ("de", "es"):
            q = {}
            mot = de_mot if app == "de" else es_mot
            # le metier : « Diego ist Arzt. » / « Diego es medico. » (pas d'article : la regle du theme)
            if app == "de":
                q["beruf"] = {"q": "Was ist %s von Beruf?" % (nom or pron_de.lower()), "rep": de_mot,
                              "phrase": "%s ist %s." % (sm["de"], de_mot)}
            else:
                q["beruf"] = {"q": "¿A qué se dedica %s?" % nom if nom else "¿A qué se dedica?", "rep": es_mot,
                              "phrase": ("%s es %s." % (nom, es_mot)) if nom else "Es %s." % es_mot}
            ph = q["beruf"]["phrase"]
            tr(app, ph, "%s est %s." % (sm["fr"], fr_m), "%s is %s." % (sm["en"], en_a(en_m)), "%s é %s." % (sm["pt"], pt_m),
               "%s ist %s." % (sm["de"], de_mot))
            # « Je suis medecin » : la reponse a « Was sind Sie von Beruf? » / « ¿A que te dedicas? », et le meme sans
            # le prenom ; l'article en trop est le piege
            if app == "de":
                un = "ein" if s == "m" else "eine"
                q["ich"] = {"q": "Was sind Sie von Beruf?", "juste": "Ich bin %s." % de_mot, "faux": "Ich bin %s %s." % (un, de_mot)}
                q["ist"] = {"juste": "%s ist %s." % (sm["de"], de_mot), "faux": "%s ist %s %s." % (sm["de"], un, de_mot)}
                # avec un adjectif, l'article revient : « Diego ist ein guter Arzt. »
                adj = "guter" if s == "m" else "gute"
                q["adj"] = {"trou": "%s ist ___ %s %s." % (sm["de"], adj, de_mot), "rep": un,
                            "opts": ["ein", "der", "einen"] if s == "m" else ["eine", "die", "einer"],
                            "phrase": "%s ist %s %s %s." % (sm["de"], un, adj, de_mot)}
                bon_fr = ("un bon " if s == "m" else "une bonne ") + fr_m
                sfr = nom + " est" if nom else "C'est"
                tr(app, q["adj"]["phrase"], "%s %s." % (sfr, bon_fr), "%s is a good %s." % (sm["en"], en_m),
                   "%s é %s %s." % (sm["pt"], "um bom" if s == "m" else "uma boa", pt_m))
            else:
                un = "un" if s == "m" else "una"
                q["ich"] = {"q": "¿A qué te dedicas?", "juste": "Soy %s." % es_mot, "faux": "Soy %s %s." % (un, es_mot)}
                q["ist"] = {"juste": ph, "faux": ("%s es %s %s." % (nom, un, es_mot)) if nom else "Es %s %s." % (un, es_mot)}
            tr(app, q["ich"]["juste"], "Je suis %s." % fr_m, "I'm %s." % en_a(en_m), "Sou %s." % pt_m, "Ich bin %s." % de_mot)
            # ou il travaille : une phrase par lieu juste
            q["ou"] = {"q": ("Wo arbeitet %s?" % (nom or pron_de.lower())) if app == "de" else ("¿Dónde trabaja %s?" % nom if nom else "¿Dónde trabaja?"),
                       "lieux": {}}
            for lid in M[met]["lieux"]:
                l = L[lid]
                phl = ("%s arbeitet %s." % (sm["de"], l["de"])) if app == "de" else (("%s trabaja %s." % (nom, l["es"])) if nom else "Trabaja %s." % l["es"])
                q["ou"]["lieux"][lid] = phl
                tr(app, phl, "%s travaille %s." % (sm["fr"], l["fr"]), "%s works %s." % (sm["en"], l["en"]),
                   "%s trabalha %s." % (sm["pt"], l["pt"]), "%s arbeitet %s." % (sm["de"], l["de"]))
            # ce qu'il fait : « Wer backt Brot? » -> « Pablo backt Brot. » ; et le verbe a trouver
            v, inf, o = a[app]
            phf = "%s %s %s." % (suj[app], v, o)
            q["fait"] = {"q": ("Wer %s %s?" % (v, o)) if app == "de" else "¿Quién %s %s?" % (v, o),
                         "phrase": phf, "trou": "%s ___ %s." % (suj[app], o), "v": v, "inf": inf}
            tr(app, phf, "%s %s." % (suj["fr"], a["fr"]), "%s %s." % (suj["en"], a["en"]), "%s %s." % (suj["pt"], a["pt"]),
               "%s %s %s." % (suj["de"], a["de"][0], a["de"][2]))
            # als / de : « Pablo arbeitet als Backer. » (jamais « wie ») ; « Pablo trabaja de panadero. »
            if app == "de":
                q["als"] = {"trou": "%s arbeitet ___ %s." % (sm["de"], de_mot), "rep": "als", "opts": ["als", "wie", "bei"],
                            "phrase": "%s arbeitet als %s." % (sm["de"], de_mot)}
            else:
                se = nom + " trabaja" if nom else "Trabaja"
                q["als"] = {"trou": "%s ___ %s." % (se, es_mot), "rep": "de", "opts": ["de", "en", "para"],
                            "phrase": "%s de %s." % (se, es_mot)}
            tr(app, q["als"]["phrase"], "%s travaille comme %s." % (sm["fr"], fr_m), "%s works as %s." % (sm["en"], en_a(en_m)),
               "%s trabalha como %s." % (sm["pt"], pt_m), "%s arbeitet als %s." % (sm["de"], de_mot))
            # la phrase a lire ou a entendre, sans prenom (les images n'en portent pas)
            q["cual"] = ("%s ist %s." % (pron_de, de_mot)) if app == "de" else "Es %s." % es_mot
            tr(app, q["cual"], "%s est %s." % (pron_fr, fr_m), "%s is %s." % (pron_en, en_a(en_m)), "%s é %s." % (pron_pt, pt_m),
               "%s ist %s." % (pron_de, de_mot))
            d["phrases"][app][pid] = q

    # les formes sans image (der Apotheker, die Krankenschwester...) : « als » seul, en texte, avec le pronom
    avec = {(p["metier"], p["sexe"]) for p in P.values()}
    for met in M:
        for s in "mf":
            if (met, s) in avec: continue
            pron = ("Er", "Il", "He", "Ele") if s == "m" else ("Sie", "Elle", "She", "Ela")
            de_mot, es_mot = forme("de", met, s)[1], forme("es", met, s)[1]
            fr_m, en_m, pt_m = M[met]["fr"][G[s]], en_nom(met, s), M[met]["pt"][G[s]]
            dph = "%s arbeitet als %s." % (pron[0], de_mot)
            d["sansImage"]["de"].append({"metier": met, "sexe": s, "trou": "%s arbeitet ___ %s." % (pron[0], de_mot), "phrase": dph})
            tr("de", dph, "%s travaille comme %s." % (pron[1], fr_m), "%s works as %s." % (pron[2], en_a(en_m)), "%s trabalha como %s." % (pron[3], pt_m))
            # en espagnol, le pronom dit le genre quand le mot ne le dit pas (el / la policia)
            eph = "%s trabaja de %s." % ("Él" if s == "m" else "Ella", es_mot)
            d["sansImage"]["es"].append({"metier": met, "sexe": s, "trou": "%s trabaja ___ %s." % ("Él" if s == "m" else "Ella", es_mot), "phrase": eph})
            tr("es", eph, "%s travaille comme %s." % (pron[1], fr_m), "%s works as %s." % (pron[2], en_a(en_m)), "%s trabalha como %s." % (pron[3], pt_m), dph)
    # le masculin et le feminin : « der Arzt → die Arztin » ; les deux sens
    for met in M:
        for app in ("de", "es"):
            m_, f_ = aff(app, met, "m"), aff(app, met, "f")
            d["paires"][app].append({"metier": met, "m": m_, "f": f_})
            tr(app, m_ + " → " + f_, fr_art(met, "m") + " → " + fr_art(met, "f"),
               ("the " + en_nom(met, "m") + " → the " + en_nom(met, "f")) if en_nom(met, "m") != en_nom(met, "f") else "the " + en_nom(met, "m") + " (a man → a woman)",
               pt_art(met, "m") + " → " + pt_art(met, "f"), aff("de", met, "m") + " → " + aff("de", met, "f"))
            tr(app, f_ + " → " + m_, fr_art(met, "f") + " → " + fr_art(met, "m"),
               ("the " + en_nom(met, "f") + " → the " + en_nom(met, "m")) if en_nom(met, "m") != en_nom(met, "f") else "the " + en_nom(met, "f") + " (a woman → a man)",
               pt_art(met, "f") + " → " + pt_art(met, "m"), aff("de", met, "f") + " → " + aff("de", met, "m"))
    gloses(d)
    return d


# ---------------------------------------------------------------------------------------------------------------
# LES GLOSES : la traduction de chaque mot teste, prise au CORPUS RELU (et, pour un mot pas encore pose, au fichier
# d'ajouts qui l'y posera), pour les langues ou la phrase n'est pas traduite (ar, tr, uk, fa, pl, ru) et pour le
# mot montre sous la reponse.
LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru", "de"]
def gloses(d):
    champ = lambda w, l: w.get("traduction" if l == "fr" else "traduction_" + l)
    def pose(app, w):
        d["gloses"][app].setdefault(w.get("mot") or w.get("infinitif"), {l: champ(w, l) for l in LANGUES if champ(w, l)})
    noms_de = {forme("de", m, s) for m in M for s in "mf"} | {L[l]["nde"] for l in L}
    noms_es = {forme("es", m, s) for m in M for s in "mf"} | {L[l]["nes"] for l in L}
    th = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))["themes"]
    aj = json.load(io.open(os.path.join(RACINE, "ajouts", "theme-metiers.json"), encoding="utf-8"))["noms"]
    for w in [w for t in th for w in t.get("mots", [])] + aj:
        if (w.get("genre"), w.get("mot")) in noms_de: pose("de", w)
    te = json.load(io.open(os.path.join(RACINE, "espanol", "datos", "temas.json"), encoding="utf-8"))["themes"]
    aje = json.load(io.open(os.path.join(RACINE, "espanol", "ajouts", "metiers.json"), encoding="utf-8"))["ajouts"]
    for w in [w for t in te for w in t.get("mots", [])]:
        # el / la policia, el / la recepcionista : le meme mot, deux entrees ; la glose de l'une sert a l'autre
        if (w.get("genre"), w.get("mot")) in noms_es: pose("es", w)
    for lignes in aje.values():
        for li in lignes:
            w = {"mot": li[0], "genre": li[1], "traduction": li[3], "traduction_en": li[4]}
            w.update({k: v for k, v in li[8].items() if k.startswith("traduction")})
            pose("es", w)
    def parcourir(o, fn):
        if isinstance(o, dict):
            if "infinitif" in o: fn(o)
            for v in o.values(): parcourir(v, fn)
        elif isinstance(o, list):
            for v in o: parcourir(v, fn)
    verbes_de = {m["act"]["de"][1] for m in M.values()} | {a["de"][1] for a in ACT_SCENE.values()}
    verbes_es = {m["act"]["es"][1] for m in M.values()} | {a["es"][1] for a in ACT_SCENE.values()}
    parcourir(json.load(io.open(os.path.join(RACINE, "verbe.json"), encoding="utf-8")), lambda w: w["infinitif"] in verbes_de and pose("de", w))
    parcourir(json.load(io.open(os.path.join(RACINE, "espanol", "datos", "verbos.json"), encoding="utf-8")), lambda w: w["infinitif"] in verbes_es and pose("es", w))
    manque = [("de", m) for _, m in noms_de if m not in d["gloses"]["de"]] + [("de", v) for v in verbes_de if v not in d["gloses"]["de"]]
    manque += [("es", m) for _, m in noms_es if m not in d["gloses"]["es"]] + [("es", v) for v in verbes_es if v not in d["gloses"]["es"]]
    if manque:
        raise SystemExit("gloses absentes du corpus et des ajouts : %s" % manque)


def ecrire_voix(d):
    """LES VOIX A ENREGISTRER (strategie des voix, 3 nov. : rien avant le renouvellement du 4 nov., le telephone d'ici
    la) : chaque phrase juste que la page peut dire, par langue, et les credits ElevenLabs. L'espagnol se dit deux
    fois (Lolita pour l'Espagne, Monica pour l'Amerique latine)."""
    v = {"_lisez_moi": "FABRIQUE par visuel/metiers/metiers.py : les textes a enregistrer (ElevenLabs v2, accord de Jacques).",
         "de": sorted(d["trad"]["de"]), "es": sorted(d["trad"]["es"])}
    # l'anglais (et ce que d'autres outils y posent) vient de visuel/voix_themes.py, qui joue la page : on le garde
    chemin = os.path.join(ICI, "voix.json")
    if os.path.exists(chemin):
        for k, x in json.load(io.open(chemin, encoding="utf-8")).items():
            if k not in v and k != "credits":
                v[k] = x
    v["credits"] = {"de (Aurora)": sum(len(t) for t in v["de"]), "es (Lolita + Monica)": 2 * sum(len(t) for t in v["es"])}
    io.open(os.path.join(ICI, "voix.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(v, ensure_ascii=False, indent=1) + "\n")
    return v["credits"]


def ecrire_json():
    os.makedirs(PROTO, exist_ok=True)
    d = construire()
    print("  voix a enregistrer (credits) :", ecrire_voix(d))
    io.open(os.path.join(PROTO, "metiers.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print("  visuel/prototype/metiers/metiers.json : %d metiers, %d personnes, %d phrases traduites (de), %d (es)"
          % (len(d["metiers"]), len(d["personnes"]), len(d["trad"]["de"]), len(d["trad"]["es"])))


# ---------------------------------------------------------------------------------------------------------------
W_WEB, H_WEB = 600, 800       # les images de la page : 3:4

def scenes():
    """Les neuf professionnels des scenes, recadres en 3:4 autour d'eux, dans l'image de la scene (gratuit)."""
    from PIL import Image
    os.makedirs(PROTO, exist_ok=True)
    for id, (sc, met, s, cx, cy, larg) in SCENE_P.items():
        im = Image.open(os.path.join(SCENES, sc + ".webp")).convert("RGB")
        w = im.width * larg / 100; h = w * 4 / 3
        x0 = min(max(0, im.width * cx / 100 - w / 2), im.width - w)
        y0 = min(max(0, im.height * cy / 100 - h / 2), im.height - h)
        c = im.crop((round(x0), round(y0), round(x0 + w), round(y0 + h))).resize((W_WEB, H_WEB), Image.LANCZOS)
        c.save(os.path.join(PROTO, id + ".webp"), quality=80, method=6)
        print("  %-15s %s, %d x %d px de la scene" % (id, sc, w, h))


def provisoires():
    """En attendant les portraits : la personne de Decrire, telle quelle, sur le fond gris, marquee PROVISOIRE. Elles
    s'ecrivent dans visuel/prototype/metiers/ et NE SE COMMITTENT PAS."""
    from PIL import Image, ImageDraw, ImageFont
    f = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 30)
    for nom, (met, s, *_r) in PORTRAITS.items():
        if os.path.exists(os.path.join(IMG, nom + ".png")): continue
        fond = Image.new("RGB", (W_WEB, H_WEB), (222, 224, 228))
        p = Image.open(os.path.join(RACINE, "visuel", "prototype", "descripcion", nom + ".webp")).convert("RGBA")
        p = p.resize((round(p.width * 1500 / p.height), 1500))
        fond.paste(p, ((W_WEB - p.width) // 2, 40), p)
        d = ImageDraw.Draw(fond)
        d.rectangle((0, H_WEB - 90, W_WEB, H_WEB), fill=(160, 40, 40))
        d.text((W_WEB / 2, H_WEB - 45), "PROVISOIRE · " + forme("de", met, s)[1], fill="white", font=f, anchor="mm")
        fond.save(os.path.join(PROTO, nom + ".webp"), quality=80)
    print("  portraits provisoires dans visuel/prototype/metiers/ (a ne pas committer)")


def payer(noms):
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import omnihuman as O                                    # noqa: E402
    os.makedirs(IMG, exist_ok=True)
    a_faire = [n for n in (noms or PORTRAITS) if not os.path.exists(os.path.join(IMG, n + ".png"))]
    print("  %d image(s) a faire, %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    cle = O.cle()
    for nom in a_faire:
        ref = os.path.join(DECRIRE, nom + ".png")
        if not os.path.exists(ref):
            print("  %s : reference absente %s -- sautee" % (nom, ref)); continue
        corps = {"prompt": prompt_de(nom), "aspect_ratio": "3:4", "resolution": "2K", "output_format": "png", "num_images": 1,
                 "image_urls": [O.deposer(ref, "image/png", cle)[0]]}
        soum = O._json("https://queue.fal.run/" + EDIT, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle)
        sortie = os.path.join(IMG, nom + ".png")
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(IMG, nom + "-fal.json"), "w", encoding="utf-8").write(json.dumps({
            "modele": EDIT, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": corps["prompt"], "references": [os.path.basename(ref)], "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", os.path.relpath(sortie, RACINE), "(%.2f $)" % PRIX)


def webp():
    """Les portraits (visuel/metiers/img/*.png) -> visuel/prototype/metiers/<Nom>.webp, 600 x 800."""
    from PIL import Image
    for nom in PORTRAITS:
        src = os.path.join(IMG, nom + ".png")
        if not os.path.exists(src): continue
        im = Image.open(src).convert("RGB")
        r = W_WEB / H_WEB
        if im.width / im.height > r:
            w = round(im.height * r); im = im.crop(((im.width - w) // 2, 0, (im.width - w) // 2 + w, im.height))
        else:
            h = round(im.width / r); im = im.crop((0, 0, im.width, h))
        im.resize((W_WEB, H_WEB), Image.LANCZOS).save(os.path.join(PROTO, nom + ".webp"), quality=80, method=6)
        print("  ", nom)


def main():
    a = sys.argv[1:]
    if "--montrer" in a:
        for nom in PORTRAITS:
            print("\n  %s%s\n  %s" % (nom, "  (planche d'essai)" if nom in ESSAI else "", prompt_de(nom)))
        print("\n  %d portraits, %.2f $ ; la planche d'essai : %d, %.2f $" % (len(PORTRAITS), len(PORTRAITS) * PRIX, len(ESSAI), len(ESSAI) * PRIX))
        return
    if "--scenes" in a:
        scenes()
    if "--provisoires" in a:
        provisoires()
    if "--payer" in a:
        payer([x for x in a if not x.startswith("--")])
    if "--webp" in a:
        webp()
    ecrire_json()


if __name__ == "__main__":
    main()
