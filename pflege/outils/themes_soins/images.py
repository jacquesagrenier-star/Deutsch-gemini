# -*- coding: utf-8 -*-
"""Les images des themes illustres des Soins : les prompts, la commande de generation, les webp de la page.

    python pflege/outils/themes_soins/images.py schmerz              # ecrit les prompts, montre les commandes (rien de paye)
    python pflege/outils/themes_soins/images.py schmerz --webp       # les originaux -> visuel/prototype/soins-theme-<cle>/*.webp

Une image se paie par pflege/outils/generer_scene.py (fal, nano-banana-pro, 0,15 $ l'image), APRES que le lot a ete
presente a Jacques avec son cout exact (decision du 16 nov. 2026). Les originaux restent hors du depot
(~/.wortando/pflege/scenes/theme-<cle>-<nom>.png), le prompt et le recu fal reviennent dans pflege/scenes/.

LES PERSONNES : celles de la Pflege, avec leur image de reference (~/.wortando/pflege/personnages/) ; jamais Anna, sa
famille ni Mark. LES LIEUX : ceux des scenes, donnes en reference de style et de lieu (la chambre de l'hopital, la
salle commune de la maison de retraite, l'appartement de Frau Kowalski) -- la continuite des lieux.
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
PERSONNAGES = os.path.expanduser("~/.wortando/pflege/personnages")
ORIGINAUX = os.path.expanduser("~/.wortando/pflege/scenes")

PATIENTS = {
    "brandt":   {"ref": "herr-brandt.png", "lieu": "soins-zimmer", "qui": "elderly man of eighty-two, a hospital patient",
                 "il": "he", "son": "his", "habits": "He wears a plain pale-blue pyjama top with a collar and pale-blue pyjama trousers.",
                 "lieu_txt": "in his room on a hospital ward: the same pale-grey hospital bed, white walls and pale grey floor as in the second reference picture"},
    "lehmann":  {"ref": "frau-lehmann.png", "lieu": "soins-aufnahme", "qui": "woman of seventy-four, a hospital patient",
                 "il": "she", "son": "her", "habits": "Her clothes stay exactly as in the first reference picture.",
                 "lieu_txt": "in her room on a hospital ward, as in the second reference picture"},
    "weber":    {"ref": "frau-weber.png", "lieu": "soins-altenheim", "qui": "woman of eighty-one, a resident of a care home",
                 "il": "she", "son": "her", "habits": "Her clothes stay exactly as in the first reference picture.",
                 "lieu_txt": "in the bright common room of a care home, as in the second reference picture"},
    "schulze":  {"ref": "herr-schulze.png", "lieu": "soins-altenheim", "qui": "man of eighty-seven, a resident of a care home",
                 "il": "he", "son": "his", "habits": "His clothes stay exactly as in the first reference picture.",
                 "lieu_txt": "in the bright common room of a care home, as in the second reference picture"},
    "kowalski": {"ref": "frau-kowalski.png", "lieu": "soins-ambulant", "qui": "woman of seventy-nine at home",
                 "il": "she", "son": "her", "habits": "She wears the same light-blue quilted dressing gown as in the first reference picture.",
                 "lieu_txt": "in her living room at home, in the same dark-red armchair, as in the second reference picture"},
}

# la pose dit l'endroit sans erreur possible a 375 px ; l'expression : une douleur nette, pas une grimace
POSES = {
    "schmerz": {
        ("brandt", "huefte"): "sits on the edge of the bed, upright, one hand pressed flat on the side of his hip, on the bone at the top of the thigh, the other hand on the mattress beside him.",
        ("brandt", "ruecken"): "stands beside the bed, leaning slightly forward, one hand pressed on the small of his back, the other hand resting on the bed rail.",
        ("brandt", "knie"): "sits alone on a chair beside the bed, leaning forward, his right leg stretched a little forward, both hands clasped tightly around his right knee, the kneecap between his hands. No other person and no part of another person is anywhere in the picture.",
        ("lehmann", "fuss"): "sits in an armchair; one foot, wrapped in a clean white bandage, rests on a low footstool in front of her, and she points at that foot with one hand.",
        ("lehmann", "kopf"): "sits in an armchair, one hand laid on her forehead, her eyes half closed.",
        ("weber", "hand"): "sits at a table, holding one hand at the wrist with her other hand, close to her chest, looking down at it.",
        ("weber", "schulter"): "sits on a chair, one hand laid on her opposite shoulder, her head tilted a little away from it.",
        ("schulze", "bauch"): "sits on a chair, slightly hunched forward, both hands laid flat on his stomach.",
        ("schulze", "hals"): "sits on a chair, one hand laid at the front of his throat, as if swallowing hurt.",
        ("kowalski", "bein"): "sits in her armchair, leaning forward, both hands holding her lower leg just below the knee.",
        ("kowalski", "arm"): "sits upright in her armchair, seen from the front, the whole armchair in the picture. The arm nearer the bed lies stretched along the armrest of the armchair, its sleeve pushed up to the elbow, the bare forearm in full view; her other hand reaches across and grips that bare forearm halfway between the wrist and the elbow, and she looks down at it for a moment before looking up. Her lap lies free under the smooth dressing gown. To the right of the armchair stand the small wooden side table with its coffee cup and the open kitchen doorway; to the left, the care bed with its flowered cover; in front of the armchair, the bare wooden floorboards.",
    },
}
EXPRESSION = ("The face shows clear, real pain, the way a patient looks when telling the nurse where it hurts: the eyebrows "
              "drawn together, the eyes narrowed, the lips pressed together. The look goes towards someone just beside the camera.")


def prompt(cle, p, k):
    d = PATIENTS[p]
    return (
        "A real photograph, taken with a good phone camera and looking exactly like a phone photograph, of one " + d["qui"] + " "
        + d["lieu_txt"] + ", in a wide picture, the person seen from the knees up and filling most of the picture, everything in "
        "sharp focus. Natural colours, soft daylight. The textures of real cotton, skin and hair, with the true depth and the "
        "slight lens perspective of a photograph.\n\n"
        "The first reference picture shows this person: " + d["son"] + " face, hair and build stay exactly as in it. "
        + d["habits"] + " The second reference picture is a real phone photograph of the place: use it for the room, the light "
        "and the photographic look, nothing drawn or painted. Its other people do not appear here.\n\n"
        "The picture carries no writing, numbers, print, symbol or logo anywhere.\n\n"
        "THE PERSON " + POSES[cle][(p, k)] + " " + EXPRESSION + "\n")


def main():
    cle = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "schmerz"
    noms = []
    for (p, k) in POSES[cle]:
        nom = "theme-%s-%s-%s" % (cle, p, k)
        io.open(os.path.join(RACINE, "pflege", "scenes", nom + ".prompt.txt"), "w", encoding="utf-8", newline="\n").write(prompt(cle, p, k))
        noms.append((nom, p, k))
    if "--webp" in sys.argv:
        from PIL import Image
        dossier = os.path.join(RACINE, "visuel", "prototype", "soins-theme-" + cle)
        for nom, p, k in noms:
            src = os.path.join(ORIGINAUX, nom + ".png")
            if not os.path.exists(src):
                print("  manque : " + nom); continue
            im = Image.open(src).convert("RGB")
            w, h = im.size
            if w / h > 4 / 3:                       # recadrer en 4:3 au centre
                nw = int(h * 4 / 3); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
            else:
                nh = int(w * 3 / 4); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
            im.resize((1200, 900), Image.LANCZOS).save(os.path.join(dossier, "%s-%s.webp" % (p, k)), quality=82, method=6)
            print("  webp : %s-%s" % (p, k))
        return
    print("%d prompts ecrits (pflege/scenes/theme-%s-*.prompt.txt). Pour payer, une image a la fois :" % (len(noms), cle))
    for nom, p, k in noms:
        print('  python pflege/outils/generer_scene.py %s --ref %s %s --format 4:3 --payer'
              % (nom, os.path.join(PERSONNAGES, PATIENTS[p]["ref"]), PATIENTS[p]["lieu"]))


if __name__ == "__main__":
    main()
