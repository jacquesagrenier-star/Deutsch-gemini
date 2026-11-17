# -*- coding: utf-8 -*-
"""Les textes rangés en objets par langue ({"fr": …, "en": …, …, "ru": …}) : relever, poser « es ».

    python interface-es/outils/dicts_langue.py extraire <fichier.json>       -> interface-es/sources/dicts-<nom>.json
    python interface-es/outils/dicts_langue.py controle <fichier.json>       lit interface-es/lots/dicts-<nom>.es.json
    python interface-es/outils/dicts_langue.py pose <fichier.json>           ecrit « es » dans chaque objet

Pour premiers-pas.json, a1-voyage.json, conjugaison.json et tout fichier de la
meme forme. Un objet est « a traduire » quand il porte « fr » ET « ru » (la
derniere langue ajoutee) et pas encore « es ». Sa cle est son chemin dans le
JSON (« /etapes/0/s ») : la pose retrouve l'objet par ce chemin et verifie que
son francais n'a pas change depuis l'extraction.

Garde-fous : le fichier doit se reproduire a l'octet pres avec la forme
detectee (indentation, fins de ligne) avant toute ecriture ; apres l'ecriture,
on relit et on compare chaque texte pose. Le controle du texte lui-meme
(balises, marques, vosotros) est celui de textes.py.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import textes  # noqa: E402


def forme(brut, d):
    crlf = "\r\n" in brut
    for ind in (1, 2, None, 4):
        for sep in (None, (",", ":")):
            for fin in ("\n", ""):
                t = json.dumps(d, ensure_ascii=False, indent=ind, separators=sep) + fin
                if crlf:
                    t = t.replace("\n", "\r\n")
                if t == brut:
                    return (ind, sep, fin, crlf)
    return None


def serialiser(d, f):
    ind, sep, fin, crlf = f
    t = json.dumps(d, ensure_ascii=False, indent=ind, separators=sep) + fin
    return t.replace("\n", "\r\n") if crlf else t


def charger(nom):
    chemin = os.path.join(RACINE, nom)
    brut = io.open(chemin, encoding="utf-8", newline="").read()
    d = json.loads(brut)
    f = forme(brut, d)
    if not f:
        sys.exit("%s ne se reproduit dans aucune forme connue : rien ne sera ecrit" % nom)
    return chemin, d, f


def objets(d):
    """(chemin, objet) de chaque objet par langue a traduire, dans l'ordre du fichier."""
    out = []
    def v(o, ch):
        if isinstance(o, dict):
            if isinstance(o.get("fr"), str) and "ru" in o:
                out.append((ch, o))
            for k, x in o.items():
                v(x, ch + "/" + k)
        elif isinstance(o, list):
            for i, x in enumerate(o):
                v(x, ch + "/" + str(i))
    v(d, "")
    return out


def allemand_voisin(d, chemin):
    """L'allemand que le texte traduit : l'element qui le precede dans sa liste
    (["die erste Straße", {"fr": …}]), ou les chaines soeurs de son objet
    ({"p": "Hin und zurück?", "s": {"fr": …}})."""
    morceaux = chemin.strip("/").split("/")
    parent = d
    for m in morceaux[:-1]:
        parent = parent[int(m)] if isinstance(parent, list) else parent[m]
    dernier = morceaux[-1]
    if isinstance(parent, list):
        i = int(dernier)
        avant = [x for x in parent[:i] if isinstance(x, str)]
        return avant[-1] if avant else ""
    soeurs = [v for k, v in parent.items() if k != dernier and isinstance(v, str)]
    return " · ".join(soeurs)


def noms(nom):
    base = os.path.splitext(os.path.basename(nom))[0]
    return (os.path.join(ICI, "sources", "dicts-%s.json" % base),
            os.path.join(ICI, "lots", "dicts-%s.es.json" % base))


def extraire(nom):
    _, d, _ = charger(nom)
    src, _ = noms(nom)
    out = [{"cle": ch, "de": allemand_voisin(d, ch), "fr": o["fr"], "en": o.get("en", "")}
           for ch, o in objets(d) if not o.get("es")]
    os.makedirs(os.path.dirname(src), exist_ok=True)
    io.open(src, "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print("%s : %d textes a traduire -> %s" % (nom, len(out), os.path.relpath(src, RACINE)))


def controle(nom):
    src, lot = noms(nom)
    fautes, _ = textes.controle(src, lot)
    return fautes


def pose(nom):
    src, lot = noms(nom)
    fautes, _ = textes.controle(src, lot, silencieux=True)
    if fautes:
        sys.exit("ARRET : %d fautes au controle, rien n'est ecrit" % len(fautes))
    chemin, d, f = charger(nom)
    source = {x["cle"]: x for x in json.load(io.open(src, encoding="utf-8"))}
    trad = json.load(io.open(lot, encoding="utf-8"))
    par_chemin = dict(objets(d))
    erreurs = []
    for k, v in trad.items():
        o = par_chemin.get(k)
        if o is None:
            erreurs.append("chemin introuvable : " + k)
        elif o["fr"] != source[k]["fr"]:
            erreurs.append("le francais a change depuis l'extraction : " + k)
    if erreurs:
        sys.exit("ARRET, rien n'est ecrit :\n  " + "\n  ".join(erreurs[:10]))
    for k, v in trad.items():
        par_chemin[k]["es"] = v
    io.open(chemin, "w", encoding="utf-8", newline="").write(serialiser(d, f))
    _, relu, _ = charger(nom)
    r = dict(objets(relu))
    ecarts = [k for k, v in trad.items() if r[k].get("es") != v]
    if ecarts:
        sys.exit("RELECTURE : %d textes differents : %s" % (len(ecarts), ecarts[:5]))
    print("%s : %d textes poses, relus." % (nom, len(trad)))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    act, nom = sys.argv[1], sys.argv[2]
    if act == "extraire":
        extraire(nom)
    elif act == "controle":
        sys.exit(1 if controle(nom) else 0)
    elif act == "pose":
        pose(nom)
    else:
        sys.exit(__doc__)
