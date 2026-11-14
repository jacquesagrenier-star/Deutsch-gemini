# -*- coding: utf-8 -*-
"""Construit et controle les scenes des Soins (visuel/prototype/soins-*.points.json).

    python pflege/outils/construire_scenes.py soins-zimmer               # construire + controler
    python pflege/outils/construire_scenes.py soins-zimmer --detourer    # + SAM 2 (local, ~2 min par vue)
    python pflege/outils/construire_scenes.py --toutes                   # toutes les scenes soins-*
    python pflege/outils/construire_scenes.py --toutes --controle        # controler seulement

LA CHAINE HABITUELLE, SANS RIEN Y CHANGER
    detourer.py <nom> puis construire.py <nom>, comme toute scene. Depuis
    62ec6f4 (session architecture), construire.py lit pour une scene soins-
    les mots du corpus PUIS ceux de pflege/datos/themes.json, et ne fait
    aucune variante .es/.en/.pt. Une scene a plusieurs vues (« vues ») est
    construite vue par vue.

CE QUE CE SCRIPT AJOUTE : LE CONTROLE PROPRE AUX SOINS (pflege/FORMAT-DONNEES.md, § 5)
    - les couches A1 (le toucher des mots, titre seul), A2, B1, B2, C1 et SIT,
      dans cet ordre, comptees sur toutes les vues du groupe (la page des
      scenes les rassemble, chaque question gardant sa vue) ;
    - SIT : "type": "situation" sur chaque question, bonne reponse en c[0] ;
    - au moins 5 questions par couche A2-C1, 3 en SIT, 3 choix distincts,
      la phrase qui remplit le trou, sens, n et f presents ;
    - un masque pour chaque zone, et les 8 traductions (fr est dans le points.json).
"""
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype")

COUCHES_ATTENDUES = ["A1", "A2", "B1", "B2", "C1", "SIT"]
LANGUES = ["en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]          # + fr = les 9


def lire(nom):
    return json.load(io.open(os.path.join(PROTO, nom + ".points.json"), encoding="utf-8"))


def lire_js(chemin):
    t = io.open(chemin, encoding="utf-8").read()
    return json.loads(t[t.index("{"):t.rindex("}") + 1])


def controler(nom):
    pts = lire(nom)
    fautes = []
    vues = pts.get("vues") or [nom]
    couches = {}
    if nom == vues[0]:
        for v in vues:
            for niv, c in lire(v).get("couches", {}).items():
                couches.setdefault(niv, []).extend(c.get("qs", []))
        if list(couches) != COUCHES_ATTENDUES:
            fautes.append("couches %s, attendu %s (dans cet ordre)" % (list(couches), COUCHES_ATTENDUES))
    else:
        hors = [n for n in pts.get("couches", {}) if n not in COUCHES_ATTENDUES]
        if hors:
            fautes.append("couches inconnues : %s" % hors)
    for niv, qs in couches.items():
        if niv == "A1":
            continue
        if len(qs) < (3 if niv == "SIT" else 5):
            fautes.append("%s : %d question(s) seulement" % (niv, len(qs)))
        for q in qs:
            if niv == "SIT" and q.get("type") != "situation":
                fautes.append("SIT : « type »: « situation » manque -- %s" % q["q"])
            if len(set(q["c"])) != len(q["c"]) or len(q["c"]) < 3:
                fautes.append("%s : choix en double ou moins de 3 -- %s" % (niv, q["q"]))
            if "___" in q["q"] and not q["q"].replace("___", q["c"][0]).endswith(q["phrase"]):
                fautes.append("%s : la phrase ne remplit pas le trou -- %s" % (niv, q["q"]))
            for cle in ("phrase", "sens", "n", "f"):
                if not q.get(cle):
                    fautes.append("%s : « %s » manque -- %s" % (niv, cle, q["q"]))
    ids = [p["id"] for p in pts["points"]]
    if len(set(ids)) != len(ids):
        fautes.append("deux zones ont le meme id")
    m = os.path.join(PROTO, "masques-%s.js" % nom)
    if os.path.exists(m):
        sans = sorted(set(ids) - set(lire_js(m)["zones"]))
        if sans:
            fautes.append("zones sans masque (--detourer) : %s" % ", ".join(sans))
    else:
        fautes.append("pas de masques-%s.js (--detourer)" % nom)
    for l in LANGUES:
        t = os.path.join(PROTO, "traductions", "%s.%s.json" % (nom, l))
        if not os.path.exists(t):
            fautes.append("pas de traduction %s" % l)
    s = os.path.join(PROTO, "scene-%s.js" % nom)
    if os.path.exists(s):
        tr = lire_js(s).get("traductions", {})
        for l in LANGUES:
            vide = [g for g in ("champs", "couches", "questions", "sens") if not tr.get(l, {}).get(g) and
                    (g != "questions" or pts.get("couches"))]
            if l in tr and vide:
                fautes.append("%s : groupes vides ou perimes dans scene-%s.js : %s" % (l, nom, ", ".join(vide)))
    return fautes


def lancer(script, nom, extra=()):
    r = subprocess.run([sys.executable, "-X", "utf8", os.path.join(PROTO, script), nom] + list(extra))
    if r.returncode:
        sys.exit("  %s %s a echoue (%d)" % (script, nom, r.returncode))


def main():
    if "--toutes" in sys.argv:
        noms = sorted(f[:-len(".points.json")] for f in os.listdir(PROTO)
                      if f.startswith("soins-") and f.endswith(".points.json"))
    else:
        noms = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not noms:
        sys.exit(__doc__)
    ok = True
    for nom in noms:
        print("== %s" % nom)
        if "--controle" not in sys.argv:
            if "--detourer" in sys.argv:
                lancer("detourer.py", nom, [a for a in ("--voir", "--tout") if a in sys.argv])
            lancer("construire.py", nom, [a for a in ("--squelette",) if a in sys.argv])
        fautes = controler(nom)
        for f in fautes:
            print("  ⚠ %s" % f)
        print("  controle : %s" % ("rien a redire" if not fautes else "%d point(s)" % len(fautes)))
        ok = ok and not fautes
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
