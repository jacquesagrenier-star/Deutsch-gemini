# -*- coding: utf-8 -*-
"""Contrôle du parcours « Premiers pas » (premiers-pas.json et
espanol/datos/premiers-pas.json). Aucune dépendance.

    python tests/premiers_pas.py            # les deux fichiers
    python tests/premiers_pas.py --detail   # affiche aussi les comptes par étape

Ce qu'il vérifie :
  - 8 étapes ; 20 à 24 cartes et 8 à 10 phrases par étape ; un tableau par étape ;
  - chaque phrase a exactement 2 leurres, aucun identique au bon sens ;
  - chaque objet de sens porte toutes les langues attendues, non vides
    (allemand : fr en tr uk fa ar pt pl ru ; espagnol : fr en pt ar) ;
  - chaque scène existe : visuel/prototype/scene-<nom>.js ET scene-<nom>.es.js ;
  - les variantes « la » (Amérique latine) ont la même forme que l'entrée ;
  - LE PLUS IMPORTANT : chaque phrase n'emploie que des mots déjà vus, c'est-à-dire
    présents dans les cartes (expression ET exemple) ou les lignes de tableau de son
    étape ou des étapes précédentes. Les variantes « la » comptent aussi.

Mots-outils permis sans avoir été vus (MOTS_OUTILS) : des mots grammaticaux qu'un
débutant lit sans les apprendre -- articles, contractions, conjonctions, « non »,
« très ». La liste est courte à dessein : tout mot de contenu doit être vu.
"""
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHIERS = {
    "de": {"chemin": "premiers-pas.json", "langues": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]},
    "es": {"chemin": os.path.join("espanol", "datos", "premiers-pas.json"), "langues": ["fr", "en", "pt", "ar"]},
}
MOTS_OUTILS = {
    "de": {"und", "oder", "in", "im", "ins", "am", "an", "auf", "aus", "mit", "für", "nach", "zu", "zum", "zur", "von",
           "der", "die", "das", "dem", "den", "ein", "eine", "einen", "einem", "nicht", "kein", "sehr", "mein", "es",
           "ich", "sie"},
    "es": {"y", "o", "a", "de", "en", "con", "sin", "el", "la", "los", "las", "un", "una", "al", "del", "mi", "no",
           "muy", "es", "que"},
}
NB_ETAPES = 8
CARTES_MIN, CARTES_MAX = 20, 24
PHRASES_MIN, PHRASES_MAX = 8, 10

PONCTUATION = re.compile(r"[¿?¡!.,;:—–\"“”„«»…·()/\[\]]")


def mots(texte):
    """Les mots d'un texte, en minuscules, sans ponctuation. Les « … » séparent."""
    t = PONCTUATION.sub(" ", texte.replace("…", " "))
    return [m for m in t.lower().split() if m]


def main():
    detail = "--detail" in sys.argv
    erreurs = []
    for code, info in FICHIERS.items():
        chemin = os.path.join(RACINE, info["chemin"])
        try:
            with open(chemin, encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            erreurs.append("%s : illisible (%s)" % (info["chemin"], e))
            continue
        erreurs += verifier(code, info, data, detail)
    if erreurs:
        print("\n".join(erreurs))
        print("\n%d problème(s)." % len(erreurs))
        sys.exit(1)
    print("Premiers pas : aucun problème.")


def verifier(code, info, data, detail):
    err = []
    nom = info["chemin"]
    langues = info["langues"]
    etapes = data.get("etapes")
    if not isinstance(etapes, list):
        return ["%s : pas de liste « etapes »" % nom]
    if len(etapes) != NB_ETAPES:
        err.append("%s : %d étapes au lieu de %d" % (nom, len(etapes), NB_ETAPES))
    if not isinstance(data.get("_lisez_moi"), list) or not data["_lisez_moi"]:
        err.append("%s : « _lisez_moi » absent ou vide" % nom)

    def sens(obj, ou):
        if not isinstance(obj, dict):
            err.append("%s : %s : sens attendu sous forme d'objet, reçu %r" % (nom, ou, obj))
            return
        for l in langues:
            if not isinstance(obj.get(l), str) or not obj[l].strip():
                err.append("%s : %s : langue « %s » absente ou vide" % (nom, ou, l))
        for l in obj:
            if l not in langues:
                err.append("%s : %s : langue inattendue « %s »" % (nom, ou, l))

    vus = set(MOTS_OUTILS[code])
    total_cartes = total_phrases = 0
    for i, e in enumerate(etapes, 1):
        ou = "étape %d" % i
        sens(e.get("s"), ou + " titre")
        # Scène
        scene = e.get("scene")
        if not isinstance(scene, str) or not scene:
            err.append("%s : %s : scène absente" % (nom, ou))
        else:
            for suffixe in (".js", ".es.js"):
                p = os.path.join(RACINE, "visuel", "prototype", "scene-" + scene + suffixe)
                if not os.path.isfile(p):
                    err.append("%s : %s : scène introuvable : visuel/prototype/scene-%s%s" % (nom, ou, scene, suffixe))
        # Tableau
        tab = e.get("tableau")
        if not isinstance(tab, dict):
            err.append("%s : %s : tableau absent" % (nom, ou))
            tab = {"l": []}
        else:
            sens(tab.get("t"), ou + " tableau titre")
            sens(tab.get("a"), ou + " tableau astuce")
            if not isinstance(tab.get("l"), list) or not tab["l"]:
                err.append("%s : %s : tableau sans lignes" % (nom, ou))
                tab["l"] = []
        nouveaux = set()
        for j, l in enumerate(tab["l"], 1):
            if not isinstance(l, list) or len(l) < 2 or not isinstance(l[0], str):
                err.append("%s : %s : ligne %d du tableau mal formée" % (nom, ou, j))
                continue
            sens(l[1], "%s tableau ligne %d" % (ou, j))
            nouveaux.update(mots(l[0]))
            if len(l) > 2:
                la = l[2]
                if not (isinstance(la, dict) and isinstance(la.get("la"), list) and len(la["la"]) == 1):
                    err.append("%s : %s : ligne %d du tableau : « la » attendu sous la forme {\"la\": [forme]}" % (nom, ou, j))
                else:
                    nouveaux.update(mots(la["la"][0]))
        # Cartes
        cartes = e.get("cartes")
        if not isinstance(cartes, list):
            err.append("%s : %s : cartes absentes" % (nom, ou))
            cartes = []
        if not CARTES_MIN <= len(cartes) <= CARTES_MAX:
            err.append("%s : %s : %d cartes (attendu %d à %d)" % (nom, ou, len(cartes), CARTES_MIN, CARTES_MAX))
        for j, c in enumerate(cartes, 1):
            ouc = "%s carte %d" % (ou, j)
            if not isinstance(c, list) or len(c) < 2 or not isinstance(c[0], str):
                err.append("%s : %s : mal formée" % (nom, ouc))
                continue
            sens(c[1], ouc + " sens")
            nouveaux.update(mots(c[0]))
            reste = c[2:]
            if reste and isinstance(reste[0], str):
                if len(reste) < 2:
                    err.append("%s : %s : exemple sans sens" % (nom, ouc))
                else:
                    sens(reste[1], ouc + " sens de l'exemple")
                nouveaux.update(mots(reste[0]))
                reste = reste[2:]
            for x in reste:
                if not (isinstance(x, dict) and isinstance(x.get("la"), list) and len(x["la"]) in (2, 4)):
                    err.append("%s : %s : élément inattendu %r (seul {\"la\": [...]} est admis)" % (nom, ouc, x))
                    continue
                positionnels = len([y for y in c if not (isinstance(y, dict) and "la" in y)])
                if len(x["la"]) != positionnels:
                    err.append("%s : %s : « la » n'a pas la forme de la carte" % (nom, ouc))
                for k, v in enumerate(x["la"]):
                    if v is None:
                        continue
                    if k in (1, 3):
                        err.append("%s : %s : « la » ne doit pas redéfinir un sens" % (nom, ouc))
                    elif isinstance(v, str):
                        nouveaux.update(mots(v))
                    else:
                        err.append("%s : %s : « la » : élément %d invalide" % (nom, ouc, k))
        vus |= nouveaux
        # Phrases
        phrases = e.get("phrases")
        if not isinstance(phrases, list):
            err.append("%s : %s : phrases absentes" % (nom, ou))
            phrases = []
        if not PHRASES_MIN <= len(phrases) <= PHRASES_MAX:
            err.append("%s : %s : %d phrases (attendu %d à %d)" % (nom, ou, len(phrases), PHRASES_MIN, PHRASES_MAX))
        for j, p in enumerate(phrases, 1):
            oup = "%s phrase %d" % (ou, j)
            if not isinstance(p, dict) or not isinstance(p.get("p"), str):
                err.append("%s : %s : mal formée" % (nom, oup))
                continue
            sens(p.get("s"), oup + " sens")
            leurres = p.get("l")
            if not isinstance(leurres, list) or len(leurres) != 2:
                err.append("%s : %s : %s leurres au lieu de 2" % (nom, oup, len(leurres) if isinstance(leurres, list) else "aucun"))
                leurres = []
            for k, l in enumerate(leurres, 1):
                sens(l, "%s leurre %d" % (oup, k))
                if isinstance(l, dict) and isinstance(p.get("s"), dict):
                    for lang in langues:
                        if l.get(lang) and l.get(lang) == p["s"].get(lang):
                            err.append("%s : %s : leurre %d identique au bon sens (%s)" % (nom, oup, k, lang))
            if len(leurres) == 2 and all(isinstance(x, dict) for x in leurres) and leurres[0] == leurres[1]:
                err.append("%s : %s : les deux leurres sont identiques" % (nom, oup))
            textes = [p["p"]]
            if "la" in p:
                if not (isinstance(p["la"], dict) and isinstance(p["la"].get("p"), str)):
                    err.append("%s : %s : « la » attendu sous la forme {\"p\": ...}" % (nom, oup))
                else:
                    textes.append(p["la"]["p"])
            for t in textes:
                inconnus = [m for m in mots(t) if m not in vus]
                if inconnus:
                    err.append("%s : %s : mots jamais vus : %s   (« %s »)" % (nom, oup, ", ".join(inconnus), t))
        total_cartes += len(cartes)
        total_phrases += len(phrases)
        if detail:
            print("%s  %s : %d cartes, %d phrases, %d lignes de tableau, scène %s" % (code, ou, len(cartes), len(phrases), len(tab["l"]), scene))
    if detail:
        print("%s  total : %d cartes, %d phrases, langues %s" % (code, total_cartes, total_phrases, " ".join(langues)))
    return err


if __name__ == "__main__":
    main()
