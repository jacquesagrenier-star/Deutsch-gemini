# -*- coding: utf-8 -*-
"""Controle du vocabulaire des Soins (Wortando Pflege) : pflege/datos/themes.json.

    python tests/pflege_vocabulaire.py          # code 0 si tout va bien, 1 sinon
    python tests/pflege_vocabulaire.py --detail # et la liste des entrees a relire

Aucune dependance. Ce qu'il verifie :
  1. pflege/datos/ est a jour sur ses sources (pflege/sources/vocabulaire/) ;
  2. chaque entree a ses cles, son niveau (A2, B1, B2), un genre et un pluriel si c'est
     un nom, ses traductions et sa phrase d'exemple dans les 9 langues d'interface ;
  3. aucun doublon entre deux entrees des Soins ;
  4. aucun doublon avec le corpus general (themes.json, verbe.json, adjectif.json,
     adverbe.json, redewendung.json, funktionswort.json) hors des REPRISES voulues
     (meme carte, une phrase de soins en plus) ; un homographe dans un autre sens doit
     le dire (sens_distinct) ;
  5. chaque reprise trouve sa fiche au corpus ;
  6. aucun {Personnage} non remplace ;
  7. les nombres en lettres : tout texte allemand PRONONCE (le mot, la phrase d'exemple)
     qui contient un chiffre a sa lecture dans pflege/datos/lectures-de.json ou
     audio/lectures/de.json, et une lecture ne contient plus de chiffre ;
  8. l'ecriture de chaque langue : cyrillique en uk et ru (sans les lettres de l'autre),
     arabe en ar et persan en fa (lettres persanes en fa, pas en ar), apostrophe
     ukrainienne ʼ, point d'interrogation ؟ en ar et fa, espace avant « ? » en francais.
"""
import io
import json
import os
import re
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "pflege", "outils"))
import corpus  # noqa: E402

FICHIER = os.path.join(RACINE, "pflege", "datos", "themes.json")
LECTURES = os.path.join(RACINE, "pflege", "datos", "lectures-de.json")
LECTURES_APP = os.path.join(RACINE, "audio", "lectures", "de.json")
LANGUES = ["en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]  # + fr sans suffixe
NIVEAUX = {"A2", "B1", "B2"}
LISTES = {"mots": "nom", "verben": "verbe", "adjektive": "adjectif", "ausdruecke": "expression", "reprises": "reprise"}
# deux types du corpus qu'on tient pour la meme carte
CLASSE = {"nom": "nom", "verbe": "verbe", "adjectif": "adj", "adverbe": "adj", "expression": "expr", "mot-outil": "outil"}

CYR = re.compile(r"[Ѐ-ӿ]")
ARABE = re.compile(r"[؀-ۿ]")
SEUL_RU = re.compile(r"[ыэъёЫЭЪЁ]")
SEUL_UK = re.compile(r"[іїєґІЇЄҐ]")
PERSAN = re.compile(r"[پچژگیک]")
ARABE_SEUL = re.compile(r"[يك]")  # ya et kaf arabes : en persan on ecrit ی et ک


class R:
    def __init__(self):
        self.echecs, self.avert = [], []

    def echec(self, m):
        self.echecs.append(m)

    def averti(self, m):
        self.avert.append(m)


def tete(d):
    return d.get("mot") or d.get("infinitif") or "?"


def verifier_entree(r, th, liste, d):
    ou = "%s/%s/%s" % (th["id"], liste, tete(d))
    if d.get("domaine") != "pflege":
        r.echec("%s : domaine absent" % ou)
    typ = LISTES[liste]
    if typ == "nom":
        for k in ("mot", "genre", "pluriel"):
            if not d.get(k):
                r.echec("%s : %s absent" % (ou, k))
        if d.get("genre") not in ("der", "die", "das", "die (Pl.)"):
            r.echec("%s : genre %r" % (ou, d.get("genre")))
        if "article_fr" not in d:
            r.echec("%s : article_fr absent" % ou)
    if typ == "verbe":
        if not d.get("infinitif"):
            r.echec("%s : infinitif absent" % ou)
        if d.get("auxiliaire") not in (None, "haben", "sein") or ("partizip2" in d) != ("auxiliaire" in d):
            r.echec("%s : auxiliaire / partizip2 incoherents" % ou)
    if typ == "reprise":
        src = d.get("source") or {}
        if not src.get("fichier") or not src.get("theme"):
            r.echec("%s : reprise sans source" % ou)
        elif not [h for h in corpus.chercher(d["mot"]) if h["fichier"] == src["fichier"] and h["ou"] == src["theme"]]:
            r.echec("%s : la fiche reprise n'existe plus au corpus (%s %s)" % (ou, src["fichier"], src["theme"]))
        if "precision" in d:
            for l in LANGUES:
                if not d.get("precision_" + l):
                    r.echec("%s : precision_%s absente" % (ou, l))
    else:
        if not d.get("traduction"):
            r.echec("%s : traduction (fr) absente" % ou)
        for l in LANGUES:
            if not d.get("traduction_" + l):
                r.echec("%s : traduction_%s absente" % (ou, l))
    if not d.get("exemple") or not d.get("exemple_fr"):
        r.echec("%s : exemple ou exemple_fr absent" % ou)
    for l in LANGUES:
        if not d.get("exemple_" + l):
            r.echec("%s : exemple_%s absent" % (ou, l))
    # ecritures
    for champ, val in d.items():
        if not isinstance(val, str):
            continue
        if "{" in val or "}" in val:
            r.echec("%s : %s garde un personnage non remplace : %s" % (ou, champ, val))
        lang = champ.rsplit("_", 1)[-1] if "_" in champ else None
        if lang == "uk":
            if not CYR.search(val):
                r.echec("%s : %s n'est pas en cyrillique" % (ou, champ))
            if SEUL_RU.search(val):
                r.echec("%s : %s a une lettre russe : %s" % (ou, champ, val))
            if "'" in val or "’" in val:
                r.echec("%s : %s : apostrophe ukrainienne attendue (ʼ) : %s" % (ou, champ, val))
        if lang == "ru":
            if not CYR.search(val):
                r.echec("%s : %s n'est pas en cyrillique" % (ou, champ))
            if SEUL_UK.search(val):
                r.echec("%s : %s a une lettre ukrainienne : %s" % (ou, champ, val))
        if lang in ("fa", "ar"):
            if not ARABE.search(val):
                r.echec("%s : %s n'est pas en ecriture arabe" % (ou, champ))
            if "?" in val:
                r.echec("%s : %s : point d'interrogation ؟ attendu : %s" % (ou, champ, val))
        if lang == "fa" and ARABE_SEUL.search(val):
            r.echec("%s : %s : ي ou ك arabes en persan (ی, ک) : %s" % (ou, champ, val))
        if lang == "ar" and PERSAN.search(val):
            r.echec("%s : %s : lettre persane en arabe : %s" % (ou, champ, val))
        if champ in ("exemple_fr", "traduction") and re.search(r"\S[?!]", val):
            r.echec("%s : %s : espace attendue avant ? ou ! en francais : %s" % (ou, champ, val))


def classe_pflege(liste, d):
    return {"mots": "nom", "verben": "verbe", "adjektive": "adj", "ausdruecke": "expr"}[liste]


def main():
    r = R()
    detail = "--detail" in sys.argv

    p = subprocess.run([sys.executable, os.path.join(RACINE, "pflege", "outils", "construire_vocabulaire.py"), "--verifier"],
                       capture_output=True, text=True, encoding="utf-8")
    if p.returncode != 0:
        r.echec("pflege/datos/ : " + (p.stdout + p.stderr).strip().splitlines()[-1])

    if not os.path.exists(FICHIER):
        print("ECHEC : %s absent" % FICHIER)
        return 1
    doc = json.load(io.open(FICHIER, encoding="utf-8"))
    themes = doc.get("themes", [])

    vus = {}
    comptes = {}
    a_relire = []
    textes_dits = set()
    ids = set()
    for th in themes:
        for k in ("id", "nom_theme", "niveau", "domaine", "sujet", "numero", "titre"):
            if k not in th:
                r.echec("%s : %s absent" % (th.get("id"), k))
        if th.get("id") in ids:
            r.echec("theme en double : %s" % th.get("id"))
        ids.add(th.get("id"))
        if not str(th.get("id", "")).startswith("pflege_"):
            r.echec("%s : l'id doit commencer par pflege_" % th.get("id"))
        if th.get("niveau") not in NIVEAUX:
            r.echec("%s : niveau %r" % (th.get("id"), th.get("niveau")))
        if sorted((th.get("titre") or {}).keys()) != sorted(["fr"] + LANGUES):
            r.echec("%s : titre sans ses 9 langues" % th.get("id"))
        for liste in LISTES:
            for d in th.get(liste, []):
                verifier_entree(r, th, liste, d)
                c = comptes.setdefault(th.get("numero"), {}).setdefault(th["niveau"], [0, 0])
                c[0] += 1
                if liste == "reprises":
                    c[1] += 1
                if d.get("relire"):
                    a_relire.append("%s · %s" % (th["id"], tete(d)))
                textes_dits.add(d.get("exemple", ""))
                if liste != "reprises":
                    textes_dits.add(tete(d))
                # doublons entre entrees des Soins
                cl = (corpus.cle(tete(d), garder_sich=True),
                      "reprise:" + str(d.get("type")) if liste == "reprises" else classe_pflege(liste, d))
                if cl in vus:
                    r.echec("doublon dans les Soins : %s (%s et %s)" % (tete(d), vus[cl], th["id"]))
                vus[cl] = th["id"]
                # doublons avec le corpus general
                if liste != "reprises":
                    hits = [h for h in corpus.chercher(tete(d)) if CLASSE.get(h["type"]) == classe_pflege(liste, d)]
                    if hits and not d.get("sens_distinct"):
                        r.echec("%s/%s : deja au corpus (%s %s, « %s ») : en faire une REPRISE, ou dire sens_distinct"
                                % (th["id"], tete(d), hits[0]["fichier"], hits[0]["ou"], hits[0]["traduction"]))
                    if d.get("sens_distinct") and not hits:
                        r.echec("%s/%s : sens_distinct, mais le mot n'est pas au corpus" % (th["id"], tete(d)))
    # une reprise et une carte neuve du meme mot dans les Soins
    for (cl, k), ou in vus.items():
        if k.startswith("reprise") and any(not k2.startswith("reprise") and c2 == cl for (c2, k2) in vus):
            r.averti("%s : repris du corpus ET carte neuve (verifier que c'est voulu)" % cl)

    # nombres en lettres
    table = {}
    for chemin in (LECTURES_APP, LECTURES):
        if os.path.exists(chemin):
            table.update(json.load(io.open(chemin, encoding="utf-8")))
    propres = json.load(io.open(LECTURES, encoding="utf-8")) if os.path.exists(LECTURES) else {}
    for t in sorted(textes_dits):
        if re.search(r"\d", t) and t not in table:
            r.echec("texte a chiffres sans lecture (pflege/sources : LECTURES) : %s" % t)
    for k, v in propres.items():
        if re.search(r"\d", v):
            r.echec("lecture encore chiffree : %s" % v)
        if k not in textes_dits:
            r.averti("lecture sans texte : %s" % k)

    # bilan
    total = sum(c[0] for n in comptes.values() for c in n.values())
    reprises = sum(c[1] for n in comptes.values() for c in n.values())
    print("Vocabulaire des Soins : %d entrees (%d reprises du corpus), %d themes-niveaux, %d a relire" % (total, reprises, len(themes), len(a_relire)))
    for num in sorted(comptes, key=lambda x: (x is None, x)):
        ligne = "  theme %-2s" % num
        for niv in ("A2", "B1", "B2"):
            c = comptes[num].get(niv, [0, 0])
            ligne += "  %s %3d (%d repr.)" % (niv, c[0], c[1])
        print(ligne)
    par_niv = {n: sum(comptes[x].get(n, [0, 0])[0] for x in comptes) for n in ("A2", "B1", "B2")}
    print("  total       A2 %d · B1 %d · B2 %d" % (par_niv["A2"], par_niv["B1"], par_niv["B2"]))
    if detail:
        print("A relire (%d) :" % len(a_relire))
        for x in a_relire:
            print("   " + x)
    for a in r.avert:
        print("  avertissement : " + a)
    if r.echecs:
        for e in r.echecs[:200]:
            print("ECHEC : " + e)
        if len(r.echecs) > 200:
            print("... et %d de plus" % (len(r.echecs) - 200))
        print("%d echec(s)" % len(r.echecs))
        return 1
    print("aucun probleme")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
