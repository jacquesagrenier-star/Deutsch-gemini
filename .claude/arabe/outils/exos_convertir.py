# -*- coding: utf-8 -*-
"""Brouillon compact -> fichier de correction de lot_exos.py.

Brouillon : {"jeu": "...", "moules": [[regex, remplacement], ...],
             "e": [ ["debut de la question", trad, expl, {extras}], ... ]}
Aligne PAR ORDRE sur le relevé <jeu>.txt de dump.py, et refuse si la question
du relevé ne commence pas par le debut donne : un decalage d'une ligne
collerait sinon chaque traduction sur l'exercice voisin, en silence.
extras : {"hint": ..., "question": ..., "correct": ..., "options": [...]}

Une valeur "*" (explication ou extra) est fabriquee a partir du FRANCAIS par
les moules du brouillon, appliques dans l'ordre. Garde-fou : refus s'il reste
un mot francais distinctif apres les moules.
"""
import io, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
FRANCAIS = [" le ", " la ", " les ", "verbe", "personne", "avec ",
            "Avec ", " est ", " car ", " une ", " un ", " et ", " pas ",
            " se termine", " qui ", " dans ", " sur ",
            "masculin ", "féminin", "neutre", "pluriel", "phrase", "Prétérit", "prétérit", " ici", "toujours", " donc "]


def fabriquer(fr, moules, ou):
    v = fr
    for motif, rempl in moules:
        v = re.sub(motif, rempl, v)
    if any(ord(c) < 32 for c in v):
        sys.exit("CARACTERE DE CONTROLE dans %s : %r" % (ou, v))
    for m in FRANCAIS:
        if m in v:
            sys.exit("FRANCAIS RESTANT %r dans %s :\n   fr : %s\n   ar : %s" % (m, ou, fr, v))
    return v


def melange(v, ou):
    # Un mot qui melange lettres latines et arabes : une faute de frappe
    # invisible dans une ligne RTL (meme garde-fou que lot.py).
    for t in (v if isinstance(v, list) else [v]):
        for mot in re.findall(r"[^\s\-—،,.;:!?()«»“”'/→←=+|]+", t):
            if re.search(r"[A-Za-zÄÖÜäöüß]", mot) and re.search(r"[\u0600-\u06ff]", mot):
                sys.exit("MOT MELANGE %r dans %s" % (mot, ou))


brouillon = json.load(io.open(sys.argv[1], encoding="utf-8"))
jeu = brouillon["jeu"]
moules = brouillon.get("moules", [])
releve = [json.loads(l) for l in io.open(os.path.join(ICI, jeu + ".txt"), encoding="utf-8") if l.strip()]
if len(releve) != len(brouillon["e"]):
    sys.exit("NOMBRE : releve %d, brouillon %d" % (len(releve), len(brouillon["e"])))
entrees = []
for r, b in zip(releve, brouillon["e"]):
    debut = b[0]
    if not r["_q"].startswith(debut):
        sys.exit("DECALAGE : releve %r / brouillon %r" % (r["_q"][:50], debut))
    ent = {"question": r["_q"]}
    if "_cle" in r:
        ent["cle_translation"] = r["_cle"]
    if "translation" in r:
        ent["translation_ar"] = b[1]
    if "explanation" in r:
        ent["explanation_ar"] = (fabriquer(r["explanation"], moules, r["_q"])
                                 if b[2] == "*" else b[2])
    extras = dict(b[3]) if len(b) > 3 else {}
    for k in ("hint", "question"):
        if k in r and k not in extras and moules:
            extras[k] = "*"
    for k, v in extras.items():
        if v == "*":
            v = fabriquer(r[k], moules, r["_q"])
        if k in ("correct", "options"):
            ent[k + "Ar"] = v
        else:
            ent[k + "_ar"] = v
    for k, v in ent.items():
        if k.endswith("_ar") or k.endswith("Ar"):
            melange(v, r["_q"])
    manque = [k for k in r if not k.startswith("_") and
              (k + "_ar" not in ent and k + "Ar" not in ent)]
    if manque:
        sys.exit("CHAMP OUBLIE %s pour %r" % (manque, r["_q"][:50]))
    entrees.append(ent)
sortie = os.path.join(ICI, "corr_" + jeu + ".json")
io.open(sortie, "w", encoding="utf-8").write(
    json.dumps({"jeu": jeu, "entrees": entrees}, ensure_ascii=False, indent=1))
print("%s : %d entrees -> %s" % (jeu, len(entrees), os.path.basename(sortie)))
