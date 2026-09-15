# -*- coding: utf-8 -*-
"""Ajoute des exercices a un jeu de exercices.json, sans toucher aux autres.

    python poser_lot_exos.py lot_derein.json          # essai a blanc
    python poser_lot_exos.py lot_derein.json --ecrire

⚠️ LE FICHIER DOIT SE REPRODUIRE A L'OCTET PRES avant modification, meme
garde-fou que tests/lot_exos.py : exercices.json pese 1,6 Mo, et une
indentation differente ferait un diff ou personne ne verrait la vraie
modification.

⚠️ LES LANGUES tr / uk / fa NE SONT PAS REMPLIES ICI, et c'est voulu. Les
poser au jugé dans trois langues qu'aucun controle de ce depot ne relit, ce
serait exactement ce que la methode de relecture croisee interdit. Le repli de
texteTraduit() affiche le francais en attendant, et tests/lot_exos.py sait
poser une langue jeu par jeu -- c'est le chemin par lequel les 1 682 autres
exercices ont recu les leurs.
"""
import io
import json
import os
import sys

RACINE = r"C:\Users\jacqu\OneDrive\Desktop\Mes Projets\DeutschAI"
CIBLE = os.path.join(RACINE, "exercices.json")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def charger_brut():
    brut = io.open(CIBLE, encoding="utf-8").read()
    data = json.loads(brut)
    return brut, data


def rendre(data):
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


def entree(e, topic):
    """Une ligne du lot -> une entree au format de exercices.json."""
    return {
        "topic": topic,
        "question": e["q"],
        "question_en": e["q"],          # la question EST en allemand
        "translation": e["fr"],
        "translation_en": e["en"],
        "hint": e["h"],
        "hint_en": e["he"],
        "answers": [e["c"]],
        "correct": e["c"],
        "correctEn": e["c"],
        "explanation": e["x"],
        "explanation_en": e["xe"],
        "options": e["o"],
        "optionsEn": e["o"],
    }


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    lot = json.load(io.open(sys.argv[1], encoding="utf-8"))
    brut, data = charger_brut()

    if rendre(data) != brut:
        sys.exit("  -> exercices.json ne se reproduit pas a l'octet pres : "
                 "on n'ecrit rien (voir le garde-fou de tests/lot_exos.py)")

    jeu = lot["jeu"]
    if jeu not in data["jeux"]:
        sys.exit("  -> jeu inconnu : " + jeu)
    avant = len(data["jeux"][jeu])
    connues = {x.get("question", "").strip() for x in data["jeux"][jeu]}

    neuves, doublons = [], []
    for e in lot["entrees"]:
        if e["q"].strip() in connues:
            doublons.append(e["q"])
            continue
        if e["c"] not in e["o"]:
            sys.exit("  -> la bonne reponse n'est pas dans les options : " + e["q"])
        connues.add(e["q"].strip())
        neuves.append(entree(e, lot["topic"]))

    print("  jeu          : %s" % jeu)
    print("  avant        : %d exercices" % avant)
    print("  a ajouter    : %d" % len(neuves))
    print("  doublons     : %d %s" % (len(doublons), doublons[:3] or ""))
    print("  apres        : %d" % (avant + len(neuves)))

    if "--ecrire" not in sys.argv:
        print("\n  (essai a blanc -- relancer avec --ecrire)")
        return
    data["jeux"][jeu].extend(neuves)
    io.open(CIBLE, "w", encoding="utf-8", newline="").write(rendre(data))
    print("\n  ecrit : exercices.json")


main()
