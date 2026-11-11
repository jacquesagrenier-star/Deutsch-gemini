# -*- coding: utf-8 -*-
"""Fait des 35 scenes japonaises de Camille (« Une annee a Tokyo ») des scenes JOUABLES.

    python japonais/scenes/construire_scenes.py

Entree : visuel/prototype/<nom>.points.json (zones, lexique : lecture et
         traduction francaise de chaque mot, prototypes du 12 oct. 2026),
         japonais/datos/themes.json (le mot tel que les cartes le portent :
         son theme, son niveau, ses traductions francaise et anglaise).
Sortie : visuel/prototype/scene-<nom>.ja.js -- le meme format que les scenes
         espagnoles (scene-<nom>.es.js), lu par la meme page
         (visuel/prototype/index.html?apprendre=ja). FICHIER DERIVE.

Ce que le japonais change : pas de genre ni de pluriel ; chaque mot porte
`lecture` (kana) et `romaji`, que la page ecrit sous le mot et que la voix
lit. Une seule couche, A1 (« touche, ecoute ») : les questions A2-C1 des
autres scenes enseignent l'allemand ou l'espagnol, elles ne se traduisent
pas ; celles du japonais restent a ecrire.

Le niveau : N5 -> A1, N4 -> A2, N3 -> B1, comme les cartes. Un mot hors du
corpus garde sa traduction du lexique (ecrite a la main le 12 oct.).

LES 35 SCENES (11 nov. 2026, lot J3) : l'ordre de l'annee de Camille
(japonais/scenes/HISTOIRE-CAMILLE.md). Les trois prototypes du 12 oct.
(eki, konbini, genkan) gardent leur place, 2 a 4. L'anglais de chaque
scene vient de traductions_en.py. Le script ecrit aussi
japonais/scenes/scenes-ja-index.js : la table SCENES_JA a recopier dans
index.html (titres ja, fr, en, dans l'ordre).
Brouillon : a faire relire par un natif.
"""
import importlib.util
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
JAPONAIS = os.path.normpath(os.path.join(ICI, ".."))
RACINE = os.path.normpath(os.path.join(JAPONAIS, ".."))
PROTO = os.path.join(RACINE, "visuel", "prototype")
SCENES = ("kuukou eki konbini genkan heya kuyakusho hanami suupaa raamen sentou tsuyu kyoushitsu "
          "yuubinkyoku mensetsu kissaten shinkansen sofu-no-ie daidokoro obon natsumatsuri hanabi "
          "kamakura fushimi ryokan momiji izakaya kusuriya depaato furusato kotatsu chichi-tochaku "
          "oomisoka hatsumoude kenrokuen ichinengo").split()
NIVEAUX = {"N5": "A1", "N4": "A2", "N3": "B1", "N2": "B2", "N1": "C1"}

import sys
sys.path.insert(0, ICI)
from traductions_en import SCENES_EN   # noqa: E402

spec = importlib.util.spec_from_file_location(
    "cartes_construire", os.path.join(JAPONAIS, "cartes", "outils", "construire.py"))
_m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_m)


def romaji(kana):
    return _m.romaji("".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in kana))


# Ce que la page dit en anglais (le reste vient du corpus).
TRADUCTIONS_EN = {
    "konbini": {"alt": "Inside a Japanese convenience store in the evening: bread and snacks on the left, drinks fridges on the right, a case of onigiri and bento in the middle, and at the back the till where a customer is paying.",
                "consigne": "It's late and you're hungry. Tap something in the store."},
    "eki": {"alt": "A small Japanese station seen from the hall: three automatic ticket gates, a ticket machine on the left, the staffed ticket window on the right, and behind them the platform with its yellow line, a bench, a drinks vending machine, passengers and a silver train with an orange stripe, doors open.",
            "consigne": "Your train is here. Tap something in the station."},
    "genkan": {"alt": "The entryway of a Japanese home: shoes lined up on the tiles, a young man sitting on the step untying his shoe, slippers ready on the wooden floor, an umbrella stand, a shoe cupboard with a vase and keys, a coat and a hat on the hook; at the back, through the open sliding door, the tatami room with the kotatsu, a woman serving tea and a cat asleep on a cushion.",
               "consigne": "You're arriving at your hosts' home. Tap something in the house."},
}


def corpus():
    d = json.load(io.open(os.path.join(JAPONAIS, "datos", "themes.json"), encoding="utf-8"))
    idx = {}
    for t in d["themes"]:
        for m in t.get("mots", []):
            idx.setdefault(m["mot"], dict(m, theme=t["id"], niveau=t.get("niveau")))
    return idx


def mot_de(mot, lex, cor):
    c = cor.get(mot)
    l = lex.get(mot, {})
    lecture = (c or {}).get("lecture") or l.get("kana") or mot
    niveau = (c or {}).get("niveau") or NIVEAUX.get(l.get("niveau"), "B2")
    return {
        "mot": mot, "genre": None, "pluriel": None, "niveau": niveau,
        "theme": (c or {}).get("theme"),
        "fr": (c or {}).get("traduction") or l.get("fr", ""),
        "en": (c or {}).get("traduction_en", ""),
        "lecture": lecture, "romaji": romaji(lecture),
    }


def construire(nom, cor):
    src = json.load(io.open(os.path.join(PROTO, nom + ".points.json"), encoding="utf-8"))
    lex = src.get("lexique", {})
    points, sans_carte = [], set()
    for p in src["points"]:
        m = mot_de(p["mot"], lex, cor)
        if not m["theme"]:
            sans_carte.add(p["mot"])
        aussi = []
        for a in p.get("aussi", []):
            ma = mot_de(a if isinstance(a, str) else a.get("mot"), lex, cor)
            aussi.append({k: ma[k] for k in ("mot", "genre", "niveau", "theme", "fr", "en", "lecture", "romaji")})
        points.append(dict({"id": p["id"]}, **m, personne=None, aussi=aussi,
                           sur=p.get("sur"), devant=p.get("devant", 0),
                           boites=p.get("boites") or [p["boite"]], latam=None))
    scene = {
        "image": src["image"],
        "points": points,
        "grosPlans": src.get("grosPlans", []),
        "titre": src["titre"],
        "titre_fr": src.get("titre_fr", ""),
        "alt": src["alt"],
        "consigne": src["consigne"],
        "exclus": src.get("exclus", []),
        "couches": {"A1": {"titre": "Les mots de la scène"}},
        "traductions": {"en": {"champs": champs_en(nom), "couches": {"A1": "Words in the scene"}}},
    }
    chemin = os.path.join(PROTO, "scene-%s.ja.js" % nom)
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write("// GENERE par japonais/scenes/construire_scenes.py (%s.points.json) -- ne pas modifier a la main.\n" % nom)
        f.write("window.SCENE = ")
        f.write(json.dumps(scene, ensure_ascii=False))
        f.write(";\n")
    a1 = sorted({p["mot"] for p in points if p["niveau"] == "A1" and p["theme"]})
    print("%s : %d zones, %d mots A1 avec carte, sans carte : %s"
          % (nom, len(points), len(a1), " ".join(sorted(sans_carte)) or "aucun"))


def champs_en(nom):
    if nom in TRADUCTIONS_EN:
        return TRADUCTIONS_EN[nom]
    _, alt, consigne = SCENES_EN[nom]
    return {"alt": alt, "consigne": consigne}


TITRES_EN_PROTOTYPES = {"konbini": "At the konbini", "eki": "At the station", "genkan": "In the entryway"}
# Le ruban de l'accueil veut des titres courts (le titre complet reste dans la scene).
TITRES_COURTS_FR = {"genkan": "À l'entrée", "kuyakusho": "À la mairie", "furusato": "La ville du père",
                    "hatsumoude": "Le premier sanctuaire", "raamen": "Au ramen"}


def table_index():
    """La table SCENES_JA d'index.html, dans l'ordre de l'annee."""
    lignes = []
    for nom in SCENES:
        src = json.load(io.open(os.path.join(PROTO, nom + ".points.json"), encoding="utf-8"))
        en = TITRES_EN_PROTOTYPES.get(nom) or SCENES_EN[nom][0]
        lignes.append("    { nom: %s, ja: %s, fr: %s, en: %s }" % tuple(
            json.dumps(x, ensure_ascii=False) for x in (nom, src["titre"], TITRES_COURTS_FR.get(nom) or src.get("titre_fr", ""), en)))
    sortie = os.path.join(ICI, "scenes-ja-index.js")
    with io.open(sortie, "w", encoding="utf-8", newline="\n") as f:
        f.write("// GENERE par japonais/scenes/construire_scenes.py : a recopier dans index.html (SCENES_JA).\n")
        f.write("const SCENES_JA = [\n" + ",\n".join(lignes) + "\n];\n")
    print("-> %s (%d scenes)" % (os.path.relpath(sortie, RACINE), len(lignes)))


def main():
    cor = corpus()
    for nom in SCENES:
        construire(nom, cor)
    table_index()


if __name__ == "__main__":
    main()
