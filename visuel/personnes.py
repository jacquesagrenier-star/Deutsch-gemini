# -*- coding: utf-8 -*-
"""La fiche commune des personnes recurrentes des themes illustres (decision de Jacques du 6 nov. 2026).

    import sys, os ; sys.path.insert(0, <dossier visuel>) ; import personnes as PERS

Lit visuel/personnes.json, complete par visuel/familia/familia.json (ages, liens) et scenes/personnages.json (Mark,
Anna). Les generateurs y prennent le metier, le prenom ecrit et les faits au lieu de les ecrire chacun de leur cote ;
tests/themes_illustres.py y prend la liste noire et les ages. Rien ne s'ecrit ici : on corrige personnes.json.
"""
import io, json, os

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)


def _lire(*p):
    return json.load(io.open(os.path.join(RACINE, *p), encoding="utf-8"))


FICHE = _lire("visuel", "personnes.json")
RECURRENTS = FICHE["recurrents"]
RESERVES = FICHE["reserves"]
TRAITS_INTERDITS = set(FICHE["traits_interdits"])
MOTS_INTERDITS = {l: set(v) for l, v in FICHE["mots_interdits"].items()}

for _n, _f in _lire("visuel", "familia", "familia.json").items():
    if _n in RECURRENTS:
        RECURRENTS[_n].setdefault("age", _f.get("age"))
        RECURRENTS[_n].setdefault("parents", _f.get("parents"))
        RECURRENTS[_n].setdefault("conjoint", _f.get("conjoint"))
_histoire = _lire("scenes", "personnages.json")
for _n in ("Mark", "Anna"):
    RECURRENTS[_n].setdefault("age", _histoire[_n.lower()].get("age"))


def nom(cle):
    """Le prenom ecrit : « Inés » pour l'image « Ines »."""
    f = RECURRENTS.get(cle) or RESERVES.get(cle) or {}
    return f.get("nom", cle)


def noms():
    """{cle d'image: prenom ecrit}, seulement ceux qui different (Ines -> Inés, Tomas -> Tomás)."""
    return {k: f["nom"] for k, f in RECURRENTS.items() if f.get("nom") and f["nom"] != k}


def sexe(cle):
    return (RECURRENTS.get(cle) or RESERVES[cle])["sexe"]


def metier(cle):
    """Le metier de la fiche (id de visuel/metiers/metiers.py), ou None."""
    return (RECURRENTS.get(cle) or RESERVES.get(cle) or {}).get("metier")


def age(cle):
    return (RECURRENTS.get(cle) or {}).get("age")


def recurrent(cle):
    """Mark, Anna, la famille d'Anna et les 12 de Descripcion : ceux qui ne portent aucun trait interdit."""
    return cle in RECURRENTS


def reserve(cle):
    return cle in RESERVES


def visage(cle):
    """L'image d'une personne : la sienne, ou pour un prenom reserve celle du visage qu'il reprend."""
    return RESERVES[cle]["visage"] if cle in RESERVES else cle


def qui_fait(met, s=None):
    """Les recurrents qui ont ce metier (et ce sexe) : le medecin du Corps est Diego."""
    return [k for k, f in RECURRENTS.items() if f.get("metier") == met and (s is None or f["sexe"] == s)]


def jamais(cle):
    """Les faits « jamais » d'une personne : [{moyen, dest}] (Anna ne va jamais au travail en voiture)."""
    return (RECURRENTS.get(cle) or {}).get("jamais", [])


def lieu_enfant(cle):
    """« kita » avant 6 ans, « schule » apres (Ben 7 ans, Mia 4 ans) ; None pour un adulte."""
    a = age(cle)
    if a is None or a >= 18:
        return None
    return "kita" if a < 6 else "schule"


def verifier():
    """Les fautes de la fiche elle-meme (un prenom reserve qui reprend un visage inconnu, un enfant sans lieu juste)."""
    fautes = []
    for k, f in RESERVES.items():
        if k in RECURRENTS:
            fautes.append("%s : prenom reserve ET recurrent" % k)
        v = f["visage"]
        if v not in RECURRENTS and not v.startswith("s-"):
            fautes.append("%s : visage inconnu %s" % (k, v))
        elif v in RECURRENTS and RECURRENTS[v]["sexe"] != f["sexe"]:
            fautes.append("%s : pas le sexe de son visage %s" % (k, v))
    vus = {}
    for k, f in RESERVES.items():
        if f["visage"] in vus:
            fautes.append("%s et %s : le meme visage" % (vus[f["visage"]], k))
        vus[f["visage"]] = k
    for k, f in RECURRENTS.items():
        if f.get("lieu") and f["lieu"] != lieu_enfant(k):
            fautes.append("%s : lieu %s pour %s ans" % (k, f["lieu"], age(k)))
    return fautes


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k in RECURRENTS:
        print("  %-7s %-6s %-12s age %-4s %s" % (k, nom(k), metier(k) or "-", age(k), RECURRENTS[k].get("faits", "")))
    print("  reserves :", ", ".join("%s (visage de %s)" % (k, visage(k)) for k in RESERVES))
    f = verifier()
    print("  fiche : " + ("; ".join(f) if f else "aucune faute"))
