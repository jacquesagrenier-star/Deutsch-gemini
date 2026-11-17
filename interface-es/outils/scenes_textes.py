# -*- coding: utf-8 -*-
"""Les textes des scenes allemandes en espagnol : extraire, controler, poser.

    python interface-es/outils/scenes_textes.py extraire [taille]   -> interface-es/sources/scenes-NN.json
    python interface-es/outils/scenes_textes.py controle <lot.es.json> [...]
    python interface-es/outils/scenes_textes.py pose <lot.es.json> [...]

Les scenes traduisent leur francais dans visuel/prototype/traductions/<scene>.<langue>.json
(groupes champs, couches, questions, sens : {cle: {fr, trad}}), lu par
visuel/prototype/construire.py, qui ne garde une traduction que si son « fr » est
encore celui de la scene. Ce module reprend `sources()` du constructeur pour savoir
quoi traduire, et ecrit <scene>.es.json dans la meme forme que les autres langues.
Une scene est « allemande » si elle a sa traduction russe (la derniere langue posee).

Cle d'un texte dans les lots : « <scene>¦<groupe>¦<cle> ».
Apres la pose : ajouter « es » a LANGUES / CHAMPS_MOT de construire.py, puis
reconstruire les scenes (python visuel/prototype/construire.py <scene>).
"""
import glob, io, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.path.dirname(ICI)
PROTO = os.path.join(RACINE, "visuel", "prototype")
TRAD = os.path.join(PROTO, "traductions")
sys.path.insert(0, PROTO)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import construire as C  # noqa: E402
import textes  # noqa: E402
SEP = "¦"


def scenes():
    for ch in sorted(glob.glob(os.path.join(TRAD, "*.ru.json"))):
        nom = os.path.basename(ch)[:-len(".ru.json")]
        pts = os.path.join(PROTO, nom + ".points.json")
        if os.path.exists(pts):
            yield nom, json.load(io.open(pts, encoding="utf-8"))


def lire(nom, lang):
    ch = os.path.join(TRAD, "%s.%s.json" % (nom, lang))
    return json.load(io.open(ch, encoding="utf-8")) if os.path.exists(ch) else {}


def extraire(taille=300):
    entrees = []
    for nom, pts in scenes():
        en = lire(nom, "en")
        es = lire(nom, "es")
        for groupe, textes_ in C.sources(pts).items():
            for cle, fr in textes_.items():
                deja = es.get(groupe, {}).get(cle)
                if deja and deja.get("trad") and deja.get("fr") == fr:
                    continue
                e = en.get(groupe, {}).get(cle) or {}
                entrees.append({"cle": SEP.join((nom, groupe, cle)), "fr": fr,
                                "en": e.get("trad", "") if e.get("fr") == fr else ""})
    k = 0
    for k, deb in enumerate(range(0, len(entrees), taille), 1):
        ch = os.path.join(ICI, "sources", "scenes-%02d.json" % k)
        io.open(ch, "w", encoding="utf-8").write(json.dumps(entrees[deb:deb + taille], ensure_ascii=False, indent=1) + "\n")
    print("%d textes de scenes a traduire, en %d sources" % (len(entrees), k))


def source_de(lot):
    base = os.path.basename(lot).replace(".es.json", ".json")
    return os.path.join(ICI, "sources", base)


def controle(lot):
    f, _ = textes.controle(source_de(lot), lot)
    return f


def pose(lot):
    if textes.controle(source_de(lot), lot, silencieux=True)[0]:
        sys.exit("ARRET : %s a des fautes" % lot)
    src = {x["cle"]: x for x in json.load(io.open(source_de(lot), encoding="utf-8"))}
    trad = json.load(io.open(lot, encoding="utf-8"))
    par_scene = {}
    for cle, v in trad.items():
        nom, groupe, k = cle.split(SEP, 2)
        par_scene.setdefault(nom, []).append((groupe, k, src[cle]["fr"], v))
    for nom, lignes in par_scene.items():
        fic = lire(nom, "es") or {"_lisez_moi": "L'espagnol d'Amerique latine, langue d'interface de l'allemand "
                                                 "(15 nov. 2026, interface-es/outils/scenes_textes.py).",
                                  "langue": "es", "scene": nom,
                                  "champs": {}, "couches": {}, "questions": {}, "sens": {}}
        for groupe, k, fr, v in lignes:
            fic.setdefault(groupe, {})[k] = {"fr": fr, "trad": v}
        io.open(os.path.join(TRAD, "%s.es.json" % nom), "w", encoding="utf-8").write(
            json.dumps(fic, ensure_ascii=False, indent=1) + "\n")
    print("%s : %d textes poses dans %d scenes" % (os.path.basename(lot), len(trad), len(par_scene)))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "extraire":
        extraire(int(a[1]) if len(a) > 1 else 300)
    elif a[0] == "controle":
        sys.exit(1 if sum(len(controle(x)) for x in a[1:]) else 0)
    elif a[0] == "pose":
        for x in a[1:]:
            pose(x)
    else:
        sys.exit(__doc__)
