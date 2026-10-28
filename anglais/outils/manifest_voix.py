# -*- coding: utf-8 -*-
"""Inventorie tout l'ANGLAIS que l'app prononcerait, et le chiffre, pour une
voix americaine (anglais/datos) puis une voix britannique (anglais/datos-gb).

    python anglais/outils/manifest_voix.py          # rapport seul : n'ecrit rien, ne depense rien

POURQUOI (28 oct. 2026). Jacques : « la voix pour apprendre l'anglais est
epouvantable ». La voix du telephone a ete mieux choisie (index.html,
scoreVoixAnglaise), mais l'allemand et l'espagnol ont de VRAIES voix
enregistrees (ElevenLabs, multilingual v2). Ce script dit ce que couterait la
meme chose en anglais, avant toute decision -- il ne genere rien.

MEME PRINCIPE QUE audio/manifest_es.py : les textes que l'app dit a voix haute
en anglais, dedoublonnes (un texte n'est compte qu'une fois, au niveau le plus
bas ou on l'entend), comptes en caracteres. Les traductions francaises ne sont
pas comptees : elles restent a la voix du telephone.

LA PORTEUSE. Un mot seul (sans espace) part dans « Word: <mot>. », a vitesse
0,80, comme « Palabra: %s. » pour l'espagnol : sur un mot isole, le modele
devine mal la langue. On paie donc la porteuse : elle est comptee.

CE QUI DIFFERE DE L'ESPAGNOL
  - Pas d'article : un nom se dit seul (« family »), son pluriel aussi.
  - La carte de verbe lit quatre lignes (carteVerbeAnglais) : « I work · he
    works », le preterit, « I have worked », « I am working » ; la carte
    d'adjectif deux (comparatif, superlatif).
  - Les exercices sont ranges au niveau de leur fiche quand anglais/outils le
    dit (grammaire_a1.py, temps_b1.py...) ; les autres a part (« EX »).
  - Les scenes : le mot seul (motDit), « Anna. waitress » pour une personne,
    et la phrase de chaque question ; en britannique, le mot « gb » du point.
"""
import glob, hashlib, io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import manifest as manifest_de       # noqa : reperes, conjugaison, A1 voyage (memes formes)

PORTEUSE = "Word: %s."
NIVEAUX = ("A1", "A2", "B1", "B2", "C1")
ORDRE = {"A1": 0, "A2": 1, "B1": 2, "B2": 3, "C1": 4, "EX": 5, "SC": 6}


def identifiant(texte):
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


def niveaux_des_series():
    """serie -> niveau, d'apres le fichier d'anglais/outils qui l'ecrit."""
    out = {}
    for f in glob.glob(os.path.join(ICI, "*.py")):
        m = re.search(r"_(a1|a2|b1|b2|c1)\.py$", f)
        if not m:
            continue
        for s in re.findall(r'"serie":\s*"([A-Za-z0-9_]+)"', io.open(f, encoding="utf-8").read()):
            out.setdefault(s, m.group(1).upper())
    return out


def recolter(variante):
    # Les exercices et les fiches n'existent qu'en americain : en britannique,
    # l'app les lit dans anglais/datos (LANGUE_ANGLAIS.fichiers). Meme repli ici.
    dossier = os.path.join(RACINE, "anglais", "datos-gb" if variante == "gb" else "datos")
    us = os.path.join(RACINE, "anglais", "datos")
    charger = lambda nom: json.load(io.open(os.path.join(dossier if os.path.exists(os.path.join(dossier, nom)) else us, nom),
                                            encoding="utf-8"))
    out = []

    def prendre(t, source, niveau):
        if t and str(t).strip():
            out.append((str(t).strip(), source, (niveau or "A1").upper()))

    for th in charger("themes.json")["themes"]:
        for m in th["mots"]:
            prendre(m.get("mot"), "noms", th["niveau"])
            if m.get("pluriel") and m["pluriel"] not in ("—", "-"):
                prendre(m["pluriel"], "noms.pluriel", th["niveau"])
            prendre(m.get("exemple"), "noms", th["niveau"])
    for niv, liste in charger("verbes.json").items():
        for v in liste:
            base, f = v.get("infinitif") or v.get("mot"), v.get("formes") or {}
            etre = base == "be"
            prendre(base, "verbes", niv)
            prendre("I am · you are · he is" if etre else "I %s · he %s" % (base, f.get("troisieme") or base), "verbes.formes", niv)
            prendre(f.get("preterit"), "verbes.formes", niv)
            if f.get("participe"):
                prendre("I have been" if etre else "I have " + f["participe"], "verbes.formes", niv)
            if f.get("ing"):
                prendre("I am being" if etre else "I am " + f["ing"], "verbes.formes", niv)
            prendre(v.get("exemple"), "verbes", niv)
    for niv, liste in charger("adjectifs.json").items():
        for a in liste:
            prendre(a.get("mot"), "adjectifs", niv)
            for k in ("comparatif", "superlatif"):
                prendre((a.get("formes") or {}).get(k), "adjectifs.formes", niv)
            prendre(a.get("exemple"), "adjectifs", niv)
    for fichier in ("adverbes.json", "expressions.json"):
        for niv, liste in charger(fichier).items():
            for x in liste:
                prendre(x.get("mot"), fichier, niv)
                prendre(x.get("exemple"), fichier, niv)
    for cle, liste in charger("fonctionnels.json").items():
        for x in liste if isinstance(liste, list) else []:
            prendre(x.get("mot"), "fonctionnels", x.get("niveau"))
            prendre(x.get("exemple"), "fonctionnels", x.get("niveau"))
    series = niveaux_des_series()
    for nom, jeu in charger("exercices.json").get("jeux", {}).items():
        for e in jeu:
            q, bon = e.get("question") or "", e.get("correct") or ""
            if "___" in q and bon:
                if q.startswith("___") and re.search(r"[.?!]", q):
                    bon = bon[:1].upper() + bon[1:]
                prendre(q.replace("___", bon, 1), "exercices", series.get(nom, "EX"))
    for f in charger("grammaire.json").get("fiches", []):
        for e in f.get("exemples", []):
            prendre(e[0] if isinstance(e[0], str) else e[0].get("fr"), "fiches", "A1")
    for g in charger("prononciation.json").get("groupes", []):
        for r in g.get("regles", []):
            for e in r.get("exemples", []):
                prendre(e.get("mot"), "prononciation", "A1")
    for etape in charger("premiers-pas.json")["etapes"]:
        for l in etape["tableau"]["l"]:
            prendre(l[0], "premiers_pas", "A1")
        for c in etape["cartes"]:
            prendre(c[0], "premiers_pas", "A1")
            if len(c) > 2 and isinstance(c[2], str):
                prendre(c[2], "premiers_pas", "A1")
        for p in etape["phrases"]:
            prendre(p["p"], "premiers_pas", "A1")
    for t in manifest_de.a1_voyage_textes(charger("a1-voyage.json")):
        prendre(t, "a1_voyage", "A1")
    # Les mots des tuiles (« Construire la phrase ») : chaque mot touche se dit.
    # « I » garde sa capitale ; le reste en minuscules, comme l'espagnol.
    for t, source, _ in list(out):
        if source in ("premiers_pas", "a1_voyage") and " " in t:
            for m in t.split():
                m = re.sub(r'[.,;:!?»")]+$', "", re.sub(r'^[«"(]+', "", m))
                m = m if m == "I" or m.startswith("I'") else m.lower()
                if re.search(r"\w", m):
                    prendre(m, "tuiles", "A1")
    for niveau, t in manifest_de.conjugaison_textes(charger("conjugaison.json")):
        prendre(t, "conjugaison", niveau)
    for t in manifest_de.reperes_textes(charger("reperes.json")):
        prendre(t, "reperes", "A1")
    for chemin in sorted(glob.glob(os.path.join(RACINE, "visuel", "prototype", "scene-*.en.js"))):
        txt = io.open(chemin, encoding="utf-8").read()
        sc = json.loads(txt[txt.index("{"):txt.rindex("}") + 1])
        ici = lambda m: dict(m, **m["gb"]) if variante == "gb" and isinstance(m.get("gb"), dict) else m
        for p in sc["points"]:
            for m in [p] + p.get("aussi", []):
                prendre(ici(m).get("mot"), "scenes", "SC")
            if p.get("personne"):
                prendre(p["personne"] + ". " + ici(p)["mot"], "scenes", "SC")
        for c in sc.get("couches", {}).values():
            for q in c.get("qs", []):
                prendre(ici(q).get("phrase"), "scenes", "SC")
    return out


def entrees(variante):
    vus = {}
    for t, s, n in recolter(variante):
        if t not in vus or ORDRE.get(n, 9) < ORDRE.get(vus[t]["niveau"], 9):
            vus[t] = {"id": identifiant(t), "texte": t, "source": s, "niveau": n}
    return list(vus.values())


def dit(e):
    """Ce qu'on enverrait a la voix : la porteuse pour un mot seul."""
    return PORTEUSE % e["texte"] if " " not in e["texte"] else e["texte"]


def main():
    for variante, nom in (("us", "Americain (anglais/datos)"), ("gb", "Britannique (anglais/datos-gb)")):
        es = entrees(variante)
        par = {}
        for e in es:
            p = par.setdefault(e["niveau"], [0, 0, 0, 0])
            p[0] += 1
            p[1] += len(dit(e))
            p[2] += " " not in e["texte"]
            p[3] += bool(re.search(r"\d", e["texte"]))
        print("\n== %s" % nom)
        print("    niveau   textes  mots seuls  caracteres dits (porteuse comprise)  avec chiffres")
        for n in NIVEAUX + ("EX", "SC"):
            if n in par:
                print("    %-6s %8d  %10d  %10d %33d" % (n, par[n][0], par[n][2], par[n][1], par[n][3]))
        cumul = lambda ns: [sum(par.get(n, [0, 0])[i] for n in ns) for i in (0, 1)]
        for libelle, ns in (("A1 seul", ("A1",)), ("A1-A2", ("A1", "A2")), ("A1-C1", NIVEAUX),
                            ("A1-C1 + exercices sans niveau + scenes", NIVEAUX + ("EX", "SC"))):
            t, c = cumul(ns)
            print("    %-40s %6d textes  %9d caracteres" % (libelle, t, c))


if __name__ == "__main__":
    main()
