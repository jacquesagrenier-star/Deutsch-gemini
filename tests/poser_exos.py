# -*- coding: utf-8 -*-
"""Ajoute des exercices a un jeu de exercices.json, sans toucher aux autres.

    python poser_lot_exos.py lot_derein.json          # essai a blanc
    python poser_lot_exos.py lot_derein.json --ecrire

⚠️ LE FICHIER DOIT SE REPRODUIRE A L'OCTET PRES avant modification, meme
garde-fou que tests/lot_exos.py : exercices.json pese 1,6 Mo, et une
indentation differente ferait un diff ou personne ne verrait la vraie
modification.

LES CINQ LANGUES D'UN COUP. Un lot porte fr / en / tr / uk / fa pour les
TROIS champs qui se traduisent vraiment -- la traduction de la phrase,
l'indice et l'explication. Les autres champs sont de l'ALLEMAND : la question
a trous, la bonne reponse et les options sont les memes dans toutes les
langues, le script les recopie.

⚠️ CE QUE CA NE REMPLACE PAS : une relecture. Les traductions turque,
ukrainienne et persane sont ecrites ici sans qu'aucun controle du depot ne les
juge. C'est une decision de Jacques, prise en connaissance de cause le
15 septembre 2026 : livrer cinq langues d'un coup plutot que d'attendre une
campagne de relecture par jeu. La relecture reste a faire, et le format le
permet -- tests/lot_exos.py sait extraire une langue d'un jeu pour la
soumettre.
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


# Les trois champs qui se traduisent, et leur nom dans exercices.json.
CHAMPS = {"t": "translation", "h": "hint", "x": "explanation"}
# Les suffixes, par langue. Le francais n'en a pas : c'est le champ nu.
SUFFIXE = {"fr": "", "en": "_en", "tr": "_tr", "uk": "_uk", "fa": "_fa"}
# Les champs ALLEMANDS, recopies tels quels dans chaque langue.
CASSE_CHAMEAU = {"en": "En", "tr": "Tr", "uk": "Uk", "fa": "Fa"}


def entree(e, topic):
    """Une ligne du lot -> une entree au format de exercices.json."""
    out = {
        "topic": topic,
        "question": e["q"],
        "answers": [e["c"]],
        "correct": e["c"],
        "options": e["o"],
    }
    for langue, suf in SUFFIXE.items():
        # La question a trous, la reponse et les options sont de l'allemand :
        # elles ne se traduisent pas, elles se recopient.
        if langue != "fr":
            out["question" + suf] = e["q"]
            out["correct" + CASSE_CHAMEAU[langue]] = e["c"]
            out["options" + CASSE_CHAMEAU[langue]] = e["o"]
        for court, long in CHAMPS.items():
            val = e.get(court + "_" + langue)
            if val:
                out[long + suf] = val
    return out


def completer(lot, data):
    """Ajoute des langues a des entrees DEJA presentes, sans en creer.

    Sert a rattraper un jeu pose en francais et en anglais seulement. La
    question allemande est la cle : elle est deja unique dans un jeu, et elle
    rend le fichier de rattrapage lisible sans compter les rangs.
    """
    jeu = lot["jeu"]
    par_question = {}
    for x in data["jeux"][jeu]:
        par_question[x.get("question", "").strip()] = x
    touchees, absentes, champs = 0, [], 0
    for e in lot["entrees"]:
        cible = par_question.get(e["q"].strip())
        if cible is None:
            absentes.append(e["q"])
            continue
        touchees += 1
        for langue, suf in SUFFIXE.items():
            if langue != "fr":
                cible.setdefault("question" + suf, cible["question"])
                cible.setdefault("correct" + CASSE_CHAMEAU[langue], cible["correct"])
                cible.setdefault("options" + CASSE_CHAMEAU[langue], cible["options"])
            for court, long in CHAMPS.items():
                val = e.get(court + "_" + langue)
                if val:
                    cible[long + suf] = val
                    champs += 1
    print("  entrees completees : %d" % touchees)
    print("  introuvables       : %d %s" % (len(absentes), absentes[:3] or ""))
    print("  champs poses       : %d" % champs)
    return not absentes


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

    if "--completer" in sys.argv:
        print("  jeu          : %s  (rattrapage de langues)" % jeu)
        if not completer(lot, data):
            sys.exit("  -> RIEN N'EST ECRIT : des questions sont introuvables")
        if "--ecrire" not in sys.argv:
            print("\n  (essai a blanc -- relancer avec --ecrire)")
            return
        io.open(CIBLE, "w", encoding="utf-8", newline="").write(rendre(data))
        print("\n  ecrit : exercices.json")
        return

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
