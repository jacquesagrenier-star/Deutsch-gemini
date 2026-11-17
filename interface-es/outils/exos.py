# -*- coding: utf-8 -*-
"""exercices.json en espagnol : recopier l'allemand, extraire le reste, controler, poser.

    python interface-es/outils/exos.py etat
    python interface-es/outils/exos.py extraire [taille]        -> interface-es/sources/exos-NN.json
    python interface-es/outils/exos.py controle <lot.es.json> [...]
    python interface-es/outils/exos.py pose <lot.es.json> [...]

Un exercice porte question / translation / hint / explanation (souligne :
`translation_ru`) et correct / options (chameau : `correctRu`). On prend le
RUSSE, derniere langue complete, comme temoin de ce qui se traduit :
  - un champ russe IDENTIQUE au champ de base est de l'allemand recopie
    (« Ich ___ jeden Tag Deutsch. », « (lernen) », les tuiles « lerne ») :
    on le recopie en espagnol, personne n'a a le retaper ;
  - un champ russe different est une traduction : il va aux traducteurs.
Le francais de base : `translation`, `hint`, `explanation` sont en francais,
`question` / `correct` / `options` en allemand (sauf exceptions, que la regle
ci-dessus traite d'elle-meme).

L'identifiant d'un exercice est « jeu#rang » ; la pose verifie que la question
allemande du fichier est celle de la source. Aller-retour a l'octet pres avant
d'ecrire (exercices.json est en JSON compact), relecture apres.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.path.dirname(ICI)
CHEMIN = os.path.join(RACINE, "exercices.json")
SOURCES = os.path.join(ICI, "sources")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import textes  # noqa: E402

SOULIGNE = ["question", "translation", "hint", "explanation"]
CHAMEAU = ["correct", "options"]


def cle(base, lg):
    return base + ("_" + lg if base in SOULIGNE else lg.capitalize())


def charger():
    brut = io.open(CHEMIN, encoding="utf-8", newline="").read()
    d = json.loads(brut)
    if json.dumps(d, ensure_ascii=False, separators=(",", ":")) != brut:
        sys.exit("exercices.json ne se reproduit plus a l'octet pres : rien ne sera ecrit")
    return d


def ecrire(d):
    io.open(CHEMIN, "w", encoding="utf-8", newline="").write(json.dumps(d, ensure_ascii=False, separators=(",", ":")))


def champs_a_traduire(e):
    """[(base, cle_es)] des champs que le russe traduit vraiment et que l'espagnol n'a pas."""
    out = []
    for base in SOULIGNE + CHAMEAU:
        ru = e.get(cle(base, "ru"))
        if ru in (None, "", []):
            continue
        if e.get(cle(base, "es")) not in (None, "", []):
            continue
        if ru == e.get(base):
            continue
        out.append(base)
    return out


def recopier(d):
    """Les champs que le russe recopie de l'allemand : recopies en espagnol."""
    n = 0
    for liste in d["jeux"].values():
        for e in liste:
            for base in SOULIGNE + CHAMEAU:
                ru = e.get(cle(base, "ru"))
                k = cle(base, "es")
                if ru in (None, "", []) or e.get(k) not in (None, "", []):
                    continue
                if ru == e.get(base):
                    e[k] = list(ru) if isinstance(ru, list) else ru
                    n += 1
    return n


def etat():
    d = charger()
    tot = reste = 0
    for nom, liste in sorted(d["jeux"].items()):
        n = sum(1 for e in liste if champs_a_traduire(e))
        tot += len(liste)
        reste += n
        if n:
            print("   %-40s %4d a traduire sur %4d" % (nom, n, len(liste)))
    copies = sum(1 for l in d["jeux"].values() for e in l for b in SOULIGNE + CHAMEAU
                 if e.get(cle(b, "ru")) not in (None, "", []) and e.get(cle(b, "ru")) == e.get(b)
                 and e.get(cle(b, "es")) in (None, "", []))
    print("   ---\n   %d exercices a traduire sur %d ; %d champs allemands a recopier" % (reste, tot, copies))


def extraire(taille=120):
    d = charger()
    n = recopier(d)
    if n:
        ecrire(d)
        print("%d champs allemands recopies en espagnol" % n)
    entrees = []
    for nom, liste in d["jeux"].items():
        for i, e in enumerate(liste):
            cs = champs_a_traduire(e)
            if not cs:
                continue
            # « _question » : la question telle qu'elle est dans le fichier, a recopier
            # dans le lot (elle sert de cle de controle) ; « question » peut ensuite
            # devenir un champ a traduire (une consigne francaise).
            x = {"id": "%s#%d" % (nom, i), "_question": e.get("question", ""), "topic": e.get("topic", ""),
                 "reponse": e.get("correct", ""), "champs": cs}
            for b in cs:
                x[b] = {"fr": e.get(b), "en": e.get(cle(b, "en"))}
            entrees.append(x)
    os.makedirs(SOURCES, exist_ok=True)
    k = 0
    for k, deb in enumerate(range(0, len(entrees), taille), 1):
        ch = os.path.join(SOURCES, "exos-%02d.json" % k)
        io.open(ch, "w", encoding="utf-8").write(json.dumps(entrees[deb:deb + taille], ensure_ascii=False, indent=1) + "\n")
    print("%d exercices a traduire, en %d sources (exos-01 a exos-%02d)" % (len(entrees), k, k))


def controle(chemin, silencieux=False):
    d = charger()
    lot = json.load(io.open(chemin, encoding="utf-8"))
    fautes, avis = [], []
    for ident, vals in lot.items():
        nom, _, i = ident.partition("#")
        liste = d["jeux"].get(nom)
        if liste is None or not i.isdigit() or int(i) >= len(liste):
            fautes.append("exercice introuvable : " + ident)
            continue
        e = liste[int(i)]
        if vals.get("_question") != e.get("question"):
            fautes.append("%s : la question allemande ne correspond pas" % ident)
        cs = champs_a_traduire(e)
        for b in cs:
            v = vals.get(b)
            if v in (None, "", []):
                fautes.append("%s : %s manquant" % (ident, b))
                continue
            ref = e.get(b)
            if isinstance(ref, list) != isinstance(v, list) or (isinstance(ref, list) and len(ref) != len(v)):
                fautes.append("%s : %s n'a pas la forme de la source" % (ident, b))
                continue
            for t in (v if isinstance(v, list) else [v]):
                vo = textes.VOSOTROS.search(textes.sans_balises(t))
                if vo and vo.group(0).lower() not in ("dieciséis", "veintiséis"):
                    fautes.append("%s : %s -- vosotros ? %r" % (ident, b, vo.group(0)))
                if textes.LETTRES_FR.search(t):
                    avis.append("%s : %s -- du francais ? %r" % (ident, b, t[:60]))
            if isinstance(v, str) and sorted(textes.BALISE.findall(v)) != sorted(textes.BALISE.findall(ref or "")):
                fautes.append("%s : %s -- balises differentes" % (ident, b))
        for b in vals:
            if b != "_question" and b not in cs:
                fautes.append("%s : %s en trop" % (ident, b))
    if not silencieux:
        print("%s : %d exercices, %d fautes, %d avis" % (os.path.relpath(chemin, RACINE), len(lot), len(fautes), len(avis)))
        for f in fautes:
            print("  FAUTE " + f)
        for a in avis[:40]:
            print("  avis  " + a)
    return fautes


def pose(chemin):
    if controle(chemin, silencieux=True):
        sys.exit("ARRET : %s a des fautes (lancer « controle »)" % chemin)
    d = charger()
    lot = json.load(io.open(chemin, encoding="utf-8"))
    poses = []
    for ident, vals in lot.items():
        nom, _, i = ident.partition("#")
        e = d["jeux"][nom][int(i)]
        for b, v in vals.items():
            if b == "_question":
                continue
            e[cle(b, "es")] = v
            poses.append((nom, int(i), cle(b, "es"), v))
    ecrire(d)
    relu = charger()
    ecarts = [p for p in poses if relu["jeux"][p[0]][p[1]].get(p[2]) != p[3]]
    if ecarts:
        sys.exit("RELECTURE : %d champs differents" % len(ecarts))
    print("%s : %d champs poses sur %d exercices, relus." % (os.path.basename(chemin), len(poses), len(lot)))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "etat":
        etat()
    elif a[0] == "extraire":
        extraire(int(a[1]) if len(a) > 1 else 120)
    elif a[0] == "controle":
        sys.exit(1 if sum(len(controle(c)) for c in a[1:]) else 0)
    elif a[0] == "pose":
        for c in a[1:]:
            pose(c)
    else:
        sys.exit(__doc__)
