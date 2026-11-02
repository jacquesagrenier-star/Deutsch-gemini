# -*- coding: utf-8 -*-
"""L'ESPAGNOL des textes de l'anglais hors corpus (2 nov. 2026) : fiches, tuiles,
series par temps, exercices, Premiers pas, A1 voyage, reperes, prononciation,
feuilles de conjugaison. Le pendant de espagnol.py (les cartes).

Une seule regle d'identite, pour extraire (anglais/es/extraire.py) comme pour
poser (ici) : chaque texte francais a traduire a une CLE, et la memoire
anglais/es/traductions/textes.json dit {cle: {"fr": temoin, "es": texte}}.
Un francais change depuis la traduction (le temoin differe) n'est pas pose :
extraire.py le ressort.

  objets {"fr": ...}      premiers-pas, a1-voyage, reperes, prononciation, conjugaison
                          cle « <fichier>|<francais> » -> on ajoute "es" a cote de "fr"
  mots de prononciation   « prononciation-mot|<mot>|<traduction> » -> traduction_es
  grammaire.json          textes.fr -> textes.es ; fiches : titre, resume, regle,
                          attention, tableau[i][1], exemples[i][1] deviennent {fr, es} ;
                          tuiles (titre, desc) et temps (titre, texte) aussi
  exercices.json          memoire exercices.json {« <jeu>|<question> » : {...}}
                          -> translation_es, explanation_es

NIVEAUX : le palier en cours ; une entree d'un autre niveau n'est ni extraite ni
posee (anglais/es/AVANCEMENT.md, « l'A1 d'abord »). Les objets sans niveau
(Premiers pas, reperes, prononciation, A1 voyage, tuiles) sont de l'A1.
"""
import io
import json
import os

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
MEMOIRE = os.path.join(RACINE, "anglais", "es", "traductions")
OBJETS = ["premiers-pas", "a1-voyage", "reperes", "prononciation", "conjugaison"]
NIVEAUX = ["A1"]
CHAMPS_FICHE = ["titre", "resume", "regle", "attention"]


def memoire(nom):
    p = os.path.join(MEMOIRE, nom + ".json")
    return json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else {}


def texte_fr(v):
    """Le francais d'un champ deja pose ({fr, es}) ou encore nu."""
    return v.get("fr", "") if isinstance(v, dict) else (v or "")


# ------------------------------------------------------------------ les entrees
# Chacune : (cle, francais, contexte, poser(es)) -- le meme parcours sert aux deux.

def entrees_objets(nom, d):
    out = []

    def marcher(o, niveau):
        if isinstance(o, dict):
            for k in ("A1", "A2", "B1", "B2", "C1"):
                if k in o and isinstance(o[k], (list, dict)):
                    marcher(o[k], k)
            for k, v in o.items():
                if k in ("A1", "A2", "B1", "B2", "C1"):
                    continue
                if k == "fr" and isinstance(v, str):
                    if niveau in NIVEAUX:
                        out.append(("%s|%s" % (nom, v), v, nom, lambda es, o=o: o.__setitem__("es", es)))
                elif k == "exemples" and nom == "prononciation" and isinstance(v, list):
                    for e in v:
                        if isinstance(e, dict) and e.get("mot") and e.get("traduction") and niveau in NIVEAUX:
                            out.append(("prononciation-mot|%s|%s" % (e["mot"], e["traduction"]), e["traduction"],
                                        "prononciation : le sens du mot « %s »" % e["mot"],
                                        lambda es, e=e: e.__setitem__("traduction_es", es)))
                else:
                    marcher(v, niveau)
        elif isinstance(o, list):
            for v in o:
                marcher(v, niveau)
    marcher(d, "A1")
    return out


def _champ(o, k):
    """Pose {fr, es} a la place d'un champ francais nu."""
    def poser(es):
        o[k] = {"fr": texte_fr(o[k]), "es": es}
    return poser


def entrees_grammaire(g):
    out = []
    for k, v in (g.get("textes", {}).get("fr", {}) or {}).items():
        out.append(("grammaire-textes|" + k, v, "titre ou texte d'ecran de grammaire",
                    lambda es, k=k: g.setdefault("textes", {}).setdefault("es", {}).__setitem__(k, es)))
    for f in g.get("fiches", []):
        if (f.get("niveau") or "A1") not in NIVEAUX:
            continue
        for k in CHAMPS_FICHE:
            if f.get(k):
                out.append(("grammaire|%s|%s" % (f["id"], k), texte_fr(f[k]), "fiche « %s »" % texte_fr(f.get("titre")), _champ(f, k)))
        for i, ligne in enumerate(f.get("tableau") or []):
            if len(ligne) > 1 and ligne[1]:
                out.append(("grammaire|%s|tableau|%d" % (f["id"], i), texte_fr(ligne[1]),
                            "fiche « %s », tableau : sens de « %s »" % (texte_fr(f.get("titre")), texte_fr(ligne[0])), _champ(ligne, 1)))
        for i, e in enumerate(f.get("exemples") or []):
            if len(e) > 1 and e[1]:
                out.append(("grammaire|%s|exemples|%d" % (f["id"], i), texte_fr(e[1]),
                            "fiche, traduction de : %s" % texte_fr(e[0]), _champ(e, 1)))
    for tid, tu in (g.get("tuiles") or {}).items():
        for o in tu.get("options", []):
            for k in ("titre", "desc"):
                if o.get(k):
                    out.append(("tuiles|%s|%s|%s" % (tid, o.get("id"), k), texte_fr(o[k]), "tuile %s" % tid, _champ(o, k)))
    for x in g.get("temps") or []:
        if x.get("niveau") not in NIVEAUX:
            continue
        for k in ("titre", "texte"):
            if x.get(k):
                out.append(("temps|%s|%s" % (x["id"], k), texte_fr(x[k]), "serie par temps %s" % x["id"], _champ(x, k)))
    return out


def series_du_palier(g):
    """Les series d'exercices du palier : celles de ses fiches, de ses temps, et
    des options de tuiles marquees de son niveau (« · A1 »)."""
    s = set()
    for f in g.get("fiches", []):
        if (f.get("niveau") or "A1") in NIVEAUX:
            if f.get("serie"):
                s.add(f["serie"])
            for e in f.get("exercices") or []:
                s.add(e[0] if isinstance(e, list) else e)
    for x in g.get("temps") or []:
        if x.get("niveau") in NIVEAUX:
            s.add(x["serie"])
    for tu in (g.get("tuiles") or {}).values():
        for o in tu.get("options", []):
            if o.get("type") == "serie" and any(("· " + n) in texte_fr(o.get("desc")) for n in NIVEAUX):
                s.add(o.get("cible"))
    return s


def cle_exercice(jeu, q):
    return "%s|%s" % (jeu, q.get("question", ""))


# ------------------------------------------------------------------ la pose

def poser(us, gb):
    """Pose la memoire dans us / gb ({"grammaire.json": ..., ...}). Renvoie des comptes."""
    mem, mex = memoire("textes"), memoire("exercices")
    stats = {}
    for jeu in (us, gb):
        for nom in OBJETS:
            if nom + ".json" in jeu:
                n = t = 0
                for cle, fr, _, mettre in entrees_objets(nom, jeu[nom + ".json"]):
                    n += 1
                    e = mem.get(cle)
                    if e and e.get("fr") == fr and e.get("es"):
                        mettre(e["es"])
                        t += 1
                stats[nom] = (n, t)
    g = us.get("grammaire.json")
    if g:
        n = t = 0
        for cle, fr, _, mettre in entrees_grammaire(g):
            n += 1
            e = mem.get(cle)
            if e and e.get("fr") == fr and e.get("es"):
                mettre(e["es"])
                t += 1
        stats["grammaire"] = (n, t)
        ex = us.get("exercices.json", {}).get("jeux", {})
        n = t = 0
        for jeu in sorted(series_du_palier(g)):
            for q in ex.get(jeu, []):
                n += 1
                e = mex.get(cle_exercice(jeu, q))
                if e and e.get("tr_fr") == q.get("translation") and e.get("ex_fr") == q.get("explanation"):
                    q["translation_es"], q["explanation_es"] = e["tr"], e["ex"]
                    t += 1
        stats["exercices"] = (n, t)
    return stats
