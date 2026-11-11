# -*- coding: utf-8 -*-
"""Controle d'etoiles/ciel.json : chaque figure, chaque etoile, chaque nom.

    python etoiles/outils/controle.py

ERREUR (code de sortie 1) : ce qui casserait l'app ou trahirait la regle des distances ; AVERTISSEMENT : ce qu'un
humain doit regarder. Les 15 premieres figures sont controlees comme les autres, mais ce qu'on n'exige que des
nouvelles (chaque etoile reliee a une etoile allumee avant elle, de 4 a 12 etoiles) n'y est qu'un avertissement."""
import json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
sys.path.insert(0, ICI)
from voyage import VOYAGE, ORDRE_EXISTANT
from construire import BOITE

LANGUES_FIGURE = ["fr", "de", "es", "en", "pt", "ja", "tr", "pl", "ru", "uk", "ar", "fa"]
LANGUES_INTERFACE = ["fr", "en", "es", "de", "pt", "tr", "pl", "ru", "uk", "ar", "fa"]
# Les seances de chaque niveau (decision du 11 nov. 2026) : le voyage doit aller jusqu'au bout du C1.
SEANCES = [("A1", 30), ("A2", 70), ("B1", 180), ("B2", 50), ("C1", 100)]
ARTICLES = r"^(le |la |les |l'|der |die |das |el |la |las |los |o |a |os |as |the )"

erreurs, avertis = [], []


def err(m): erreurs.append(m)
def avert(m): avertis.append(m)


def simplifier(t):
    t = re.sub(r"\s*\(.*\)$", "", t)
    t = re.sub(ARTICLES, "", t, flags=re.I)
    t = re.sub(r"^Gwiazdozbiór ", "", t)
    return t.strip().lower()


def main():
    d = json.load(open(os.path.join(RACINE, "ciel.json"), encoding="utf-8"))
    C, ordre = d["constellations"], d.get("ordre") or []
    S = json.load(open(os.path.join(RACINE, "sources-etoiles.json"), encoding="utf-8"))["constellations"]
    if set(S) != set(C) or any(len(S[k]) != len(C[k]["etoiles"]) for k in C):
        err("sources-etoiles.json ne suit pas ciel.json")
    for k in C:
        for e in C[k]["etoiles"]:
            if "source" in e:
                err("%s / %s : « source » encore dans ciel.json" % (k, e["nom"]))
    nouvelles = [f["cle"] for f in VOYAGE]
    if ordre != ORDRE_EXISTANT + nouvelles:
        err("ordre : %s" % ordre)
    if set(C) != set(ordre):
        err("constellations hors de l'ordre : %s" % (set(C) ^ set(ordre)))
    for g, c in d["groupes"].items():
        if c not in C:
            err("groupe %s -> %s inconnue" % (g, c))
    vues = {}
    for k in ordre:
        c, neuve = C[k], k in nouvelles
        E, T = c["etoiles"], c["traits"]
        n = len(E)
        if not 4 <= n <= 12:
            (err if neuve else avert)("%s : %d etoiles (4 a 12 voulues)" % (k, n))
        for lg in LANGUES_FIGURE:
            if not (c["noms"].get(lg) or "").strip():
                err("%s : pas de nom en %s" % (k, lg))
        paires = set()
        for t in T:
            if len(t) != 2 or not all(isinstance(i, int) and 0 <= i < n for i in t) or t[0] == t[1]:
                err("%s : trait invalide %s" % (k, t))
                continue
            p = tuple(sorted(t))
            if p in paires:
                err("%s : trait en double %s" % (k, t))
            paires.add(p)
        for i in range(1, n):
            if not any(i in p and min(p) < i and max(p) == i for p in paires):
                (err if neuve else avert)("%s : l'etoile %d (%s) n'est reliee a aucune etoile allumee avant elle"
                                          % (k, i + 1, E[i]["nom"]))
        for i, e in enumerate(E):
            q = "%s / %s" % (k, e["nom"])
            if not (0 <= e["x"] <= BOITE[0] and 0 <= e["y"] <= BOITE[1]):
                err(q + " : hors de la boite")
            s = S.get(k, [{}] * n)[i] if i < len(S.get(k, [])) else {}
            p, er = s.get("parallaxe_mas"), s.get("erreur_mas")
            if not p or p <= 0 or er is None:
                err(q + " : pas de parallaxe")
                continue
            if not s.get("reference") or not s.get("catalogue"):
                err(q + " : parallaxe sans reference")
            al = 3261.563777 / p
            if abs(al - e["al"]) > 0.1 + al * 1e-6:
                err(q + " : al %s ne suit pas la parallaxe (%.1f)" % (e["al"], al))
            rel = er / p
            if rel > 0.5:
                err(q + " : parallaxe trop incertaine (%d %%)" % round(rel * 100))
            doit_environ = rel > 0.10 or al >= 1000
            if neuve and s.get("hipparcos_2007_mas") and s.get("gaia_mas"):
                h, g = s["hipparcos_2007_mas"], s["gaia_mas"]
                doit_environ = doit_environ or abs(h - g) / max(h, g) > 0.10
            if doit_environ and not e["environ"]:
                err(q + " : distance incertaine (%d %%) affichee sans « environ »" % round(rel * 100))
            if not isinstance(e["affiche"], int) or e["affiche"] <= 0 or abs(e["affiche"] - al) > max(5, al * 0.06):
                err(q + " : affiche %s pour %.0f al" % (e["affiche"], al))
            if neuve:
                cle_s = s.get("simbad")
                if cle_s in vues:
                    err(q + " : deja dans %s" % vues[cle_s])
                vues[cle_s] = k
                if "noms" in e:
                    for lg in LANGUES_INTERFACE:
                        if not e["noms"].get(lg):
                            err(q + " : nom sans nom propre absent en " + lg)
                elif s.get("nom", "").startswith("UAI") is False:
                    err(q + " : nom propre sans source")
            if not re.fullmatch(r"#[0-9A-F]{6}", e["couleur"]) or not 0 < e["lum"] <= 1 or e["r"] <= 0:
                err(q + " : dessin invalide")
    # les noms, contre les titres des articles de Wikipedia (information, pas une regle)
    wiki = json.load(open(os.path.join(RACINE, "sources", "wikipedia_noms.json"), encoding="utf-8"))
    ecarts = []
    for f in VOYAGE:
        art = wiki[f["con"]]["articles"]
        for lg in LANGUES_FIGURE:
            # un titre en latin (« Ursa Minor (takımyıldız) ») ou au genitif polonais ne dit rien de l'usage : on le saute
            if lg not in art or lg == "en" or simplifier(art[lg]) in (simplifier(art.get("en", "")), simplifier(f["noms"]["en"]))                     or art[lg].startswith("Gwiazdozbiór"):
                continue
            if simplifier(f["noms"][lg]) != simplifier(art[lg]):
                ecarts.append("%s %s : « %s » / Wikipedia « %s »" % (f["cle"], lg, f["noms"][lg], art[lg]))
    # le voyage et les niveaux
    total = sum(len(C[k]["etoiles"]) for k in ordre)
    besoin = sum(n for _, n in SEANCES)
    if total < besoin * 0.97:
        err("le voyage s'arrete a %d etoiles, il en faut environ %d pour finir le C1" % (total, besoin))
    print("Voyage : %d constellations, %d etoiles (dont %d nouvelles dans %d figures)." % (
        len(ordre), total, sum(len(C[k]["etoiles"]) for k in nouvelles), len(nouvelles)))
    debut = 0
    for niv, n in SEANCES:
        a, b = debut + 1, debut + n
        cum, ou = 0, []
        for k in ordre:
            m = len(C[k]["etoiles"])
            if cum + m >= a and cum < b:
                ou.append(C[k]["noms"]["fr"])
            cum += m
        print("  %s, seances %d a %d : %s" % (niv, a, b, ", ".join(ou)))
        debut = b
    print("  au-dela du C1 : %d etoiles de marge" % (total - besoin))
    print("\nNoms differents du titre de l'article Wikipedia (%d, a regarder ; les titres latins sont sautes) :" % len(ecarts))
    for x in ecarts:
        print("  " + x)
    for m in avertis:
        print("AVERTISSEMENT " + m)
    for m in erreurs:
        print("ERREUR " + m)
    print("\n%d erreur(s), %d avertissement(s)." % (len(erreurs), len(avertis)))
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
