# -*- coding: utf-8 -*-
"""Construit pflege/datos/chapitres.json, les 14 chapitres de « Ma journée au service », à partir de
pflege/sources/chapitres.py et des données des Soins (décision de Jacques du 16 nov. 2026 ; plan :
pflege/PLAN-CHAPITRES.md).

    python pflege/outils/chapitres.py              # écrit la sortie et affiche la carte
    python pflege/outils/chapitres.py --verifier   # contrôle seulement (tests/pflege.py) : 1 si la sortie est
                                                   # périmée ou si un renvoi est faux

Ce qu'il refuse :
  - un renvoi vers une scène, un dialogue, un écrit ou un thème illustré qui n'existe pas ;
  - un dialogue ou un écrit rangé dans deux chapitres, ou dans aucun ;
  - un champ « chapitre » (mot, carte-phrase) qui ne nomme pas un chapitre ;
  - un titre ou un sous-titre absent dans l'une des 9 langues.

La sortie, par chapitre : ses scènes, son thème illustré, ses dialogues (ids de dialogues.json), ses écrits, sa
grammaire (déduite des dialogues), ses mots, paires et abréviations (« <themeId>:<rang> », la clé de la progression
de l'app : themeId = l'id du thème AVEC son niveau, rang = la place du mot dans ce thème), ses cartes-phrases (ids),
leurs comptes, « complet » et « manque ». Les mots et cartes-phrases encore sans chapitre sont listés à part
(« a_ranger »).
"""
import importlib.util
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
DATOS = os.path.join(RACINE, "pflege", "datos")
SORTIE = os.path.join(DATOS, "chapitres.json")
PROTO = os.path.join(RACINE, "visuel", "prototype")


def charger_source():
    spec = importlib.util.spec_from_file_location("chapitres_source", os.path.join(RACINE, "pflege", "sources", "chapitres.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def lire(nom):
    with open(os.path.join(DATOS, nom), encoding="utf-8") as f:
        return json.load(f)


def construire():
    S = charger_source()
    erreurs = []
    ids = [c["id"] for c in S.CHAPITRES]
    if len(set(ids)) != len(ids):
        erreurs.append("deux chapitres ont le meme id")
    connus = set(ids)

    dialogues = lire("dialogues.json")["dialogues"]
    par_source = {d["source"]: d for d in dialogues}
    sujets = {e["id"]: e for e in lire("ecrit.json")["sujets"]}
    ecrits = set(sujets)
    themes = lire("themes.json")
    themes = themes if isinstance(themes, list) else themes["themes"]
    redemittel = lire("redemittel.json")

    # dialogues et écrits : un chapitre chacun
    place_dlg, place_ecr = {}, {}
    for c in S.CHAPITRES:
        for l in S.LANGUES:
            for champ in ("titre", "sous_titre"):
                if not str(c.get(champ, {}).get(l, "")).strip():
                    erreurs.append("%s : %s manque en %s" % (c["id"], champ, l))
        for s in c.get("scenes", []):
            if not os.path.exists(os.path.join(PROTO, s + ".points.json")):
                erreurs.append("%s : scene inconnue %s" % (c["id"], s))
        if c.get("theme_illustre") and not os.path.exists(os.path.join(PROTO, c["theme_illustre"])):
            erreurs.append("%s : theme illustre introuvable %s" % (c["id"], c["theme_illustre"]))
        for d in c.get("dialogues", []):
            if d not in par_source:
                erreurs.append("%s : dialogue inconnu %s" % (c["id"], d))
            elif d in place_dlg:
                erreurs.append("dialogue %s dans %s et %s" % (d, place_dlg[d], c["id"]))
            place_dlg[d] = c["id"]
        for e in c.get("ecrits", []):
            if e not in ecrits:
                erreurs.append("%s : ecrit inconnu %s" % (c["id"], e))
            elif e in place_ecr:
                erreurs.append("ecrit %s dans %s et %s" % (e, place_ecr[e], c["id"]))
            place_ecr[e] = c["id"]
        for d in c.get("voir_aussi", {}).get("dialogues", []):
            if d not in par_source:
                erreurs.append("%s : voir_aussi, dialogue inconnu %s" % (c["id"], d))
        for e in c.get("voir_aussi", {}).get("ecrits", []):
            if e not in ecrits:
                erreurs.append("%s : voir_aussi, ecrit inconnu %s" % (c["id"], e))
    for d in par_source:
        if d not in place_dlg:
            erreurs.append("dialogue %s dans aucun chapitre" % d)
    for e in ecrits:
        if e not in place_ecr:
            erreurs.append("ecrit %s dans aucun chapitre" % e)

    # mots, paires, abréviations
    mots = {i: [] for i in ids}
    paires = {i: [] for i in ids}
    abrev = {i: [] for i in ids}
    a_ranger = {"mots": 0, "paires": 0, "cartes": 0}
    for th in themes:
        base = th["id"].rsplit("_", 1)[0]
        for rang, w in enumerate(th.get("mots", [])):
            cle = "%s:%d" % (th["id"], rang)
            est_abrev = "(=" in w.get("mot", "")
            ch = w.get("chapitre")
            if ch and ch not in connus:
                erreurs.append("mot %s (%s) : chapitre inconnu %s" % (cle, w.get("mot"), ch))
                ch = None
            if not ch:
                ch = S.ABREVIATIONS_DEFAUT if est_abrev else S.THEME_DEFAUT.get(base)
            if not ch:
                a_ranger["paires" if w.get("sorte") == "paire" else "mots"] += 1
                continue
            (paires if w.get("sorte") == "paire" else abrev if est_abrev else mots)[ch].append(cle)

    # cartes-phrases : celles d'un dialogue suivent leur dialogue
    cartes = {i: [] for i in ids}
    dlg_id_vers_source = {d["id"]: d["source"] for d in dialogues}
    for k in redemittel.get("cartes", []):
        if k.get("retire"):
            continue
        ch = k.get("chapitre")
        if ch and ch not in connus:
            erreurs.append("carte %s : chapitre inconnu %s" % (k.get("id"), ch))
            ch = None
        if not ch and k.get("dialogue"):
            ch = place_dlg.get(dlg_id_vers_source.get(k["dialogue"], k["dialogue"]))
        if not ch:
            ch = S.GROUPE_DEFAUT.get(k.get("groupe"))
        if not ch:
            a_ranger["cartes"] += 1
            continue
        cartes[ch].append(k["id"])

    # la personne en face dans un dialogue (pour la vignette de l'ecran du chapitre) : son id, son nom allemand
    # (pflege/sources/noms.json), son visage s'il existe (visuel/prototype/conversation/soins/<id>.webp)
    noms = json.load(open(os.path.join(RACINE, "pflege", "sources", "noms.json"), encoding="utf-8"))["personnes"]

    def en_face(d):
        autres = [p for p in d.get("personnages", []) if p != d.get("apprenant")]
        if not autres:
            return {}
        q = autres[0]
        nom = (noms.get(q, {}).get("de", {}) or {}).get("") or q
        visage = os.path.exists(os.path.join(PROTO, "conversation", "soins", q + ".webp"))
        return {"avec": q, "avec_nom": nom, "visage": ("conversation/soins/%s.webp" % q) if visage else None}

    sortie_ch = []
    for numero, c in enumerate(S.CHAPITRES, 1):
        dlg = [par_source[d]["id"] for d in c.get("dialogues", []) if d in par_source]
        grammaire = []
        for d in c.get("dialogues", []):
            for g in par_source.get(d, {}).get("grammaire", []) or []:
                if g not in grammaire:
                    grammaire.append(g)
        scenes_vraies = [] if c.get("scene_provisoire") else c.get("scenes", [])
        compte = {"scenes": len(scenes_vraies), "theme_illustre": 1 if c.get("theme_illustre") else 0,
                  "dialogues": len(dlg), "ecrits": len(c.get("ecrits", [])), "mots": len(mots[c["id"]])}
        manque = [k for k, minimum in S.COMPLET.items() if compte[k] < minimum]
        sortie_ch.append({
            "id": c["id"], "numero": numero, "cle": c["cle"], "de": c["de"],
            "titre": c["titre"], "sous_titre": c["sous_titre"],
            "scenes": c.get("scenes", []), "scene_provisoire": bool(c.get("scene_provisoire")),
            "theme_illustre": c.get("theme_illustre"),
            "dialogues": dlg,
            # ce que l'accueil et l'ecran du chapitre affichent, sans charger dialogues.json ni ecrit.json
            "dialogues_info": [dict({"id": par_source[d]["id"], "niveau": par_source[d].get("niveau"),
                                     "de": par_source[d].get("titre_de", ""),
                                     "titre": {l: par_source[d]["titre"].get(l, "") for l in S.LANGUES if par_source[d]["titre"].get(l)}},
                                    **en_face(par_source[d]))
                               for d in c.get("dialogues", []) if d in par_source],
            "ecrits": c.get("ecrits", []),
            "ecrits_info": [{"id": e, "niveau": sujets[e].get("niveau"),
                             "titre": ({l: v for l, v in sujets[e]["titre"].items() if l in S.LANGUES and v}
                                       if isinstance(sujets[e].get("titre"), dict) else {"fr": str(sujets[e].get("titre", ""))})}
                            for e in c.get("ecrits", []) if e in sujets],
            "voir_aussi": {"dialogues": [par_source[d]["id"] for d in c.get("voir_aussi", {}).get("dialogues", []) if d in par_source],
                           "ecrits": c.get("voir_aussi", {}).get("ecrits", [])},
            "grammaire": grammaire,
            "mots": mots[c["id"]], "paires": paires[c["id"]], "abreviations": abrev[c["id"]],
            "cartes": cartes[c["id"]],
            "comptes": dict(compte, paires=len(paires[c["id"]]), abreviations=len(abrev[c["id"]]),
                            cartes=len(cartes[c["id"]])),
            "complet": not manque,
            "manque": manque,
        })
    doc = {
        "_note": "DERIVE de pflege/sources/chapitres.py par pflege/outils/chapitres.py : ne pas corriger a la main "
                 "(plan : pflege/PLAN-CHAPITRES.md). Les cles des mots sont « <themeId avec niveau>:<rang> », celles "
                 "de la progression de l'app (soinsDuNiveau).",
        "langues": S.LANGUES,
        "complet_si": S.COMPLET,
        "chapitres": sortie_ch,
        "a_ranger": a_ranger,
    }
    return doc, erreurs


def texte(doc):
    return json.dumps(doc, ensure_ascii=False, indent=1) + "\n"


def main():
    doc, erreurs = construire()
    verifier = "--verifier" in sys.argv
    if erreurs:
        print("chapitres.py : %d erreur(s)" % len(erreurs))
        for e in erreurs:
            print("  " + e)
        return 1
    neuf = texte(doc)
    if verifier:
        ancien = open(SORTIE, encoding="utf-8").read() if os.path.exists(SORTIE) else ""
        if ancien != neuf:
            print("pflege/datos/chapitres.json n'est pas a jour : python pflege/outils/chapitres.py")
            return 1
        return 0
    with open(SORTIE, "w", encoding="utf-8", newline="\n") as f:
        f.write(neuf)
    print("%-22s %-3s %-3s %-3s %-3s %-4s %-3s %-3s %-4s  %s" % ("chapitre", "sc", "ti", "dlg", "ecr", "mots", "pai", "abr", "cart", "manque"))
    for c in doc["chapitres"]:
        k = c["comptes"]
        print("%-22s %-3d %-3d %-3d %-3d %-4d %-3d %-3d %-4d  %s" % (c["id"], k["scenes"], k["theme_illustre"], k["dialogues"],
              k["ecrits"], k["mots"], k["paires"], k["abreviations"], k["cartes"], ", ".join(c["manque"]) or "complet"))
    print("a ranger :", doc["a_ranger"])
    print("ecrit :", os.path.relpath(SORTIE, RACINE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
