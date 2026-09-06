# -*- coding: utf-8 -*-
"""Releve des CHEMINS D'ACCES : par ou passe-t-on pour atteindre chaque chose ?

    python tests/chemins.py             # le releve
    python tests/chemins.py --orphelins # seulement ce qui n'est atteignable

POURQUOI CE SCRIPT EXISTE
    Le verificateur repond a « la cible existe-t-elle ? ». Il ne repond pas a
    « peut-on y arriver ? ». La difference a deja coute une version : en v409,
    un ecran d'explication, 45 exercices et 18 cartes existaient depuis des
    mois, tous valides par le verificateur -- et AUCUNE TUILE NE LES PORTAIT.
    On n'y arrivait qu'en appuyant sur « Retour » depuis un ecran de passage.
    Aucun test ne voyait ca ; c'est un usager qui l'a trouve.

    41 ecrans, 40 jeux d'exercices, 17 formats de cartes : la surface est trop
    grande pour qu'une relecture suffise. Ce script parcourt le graphe pour de
    bon, depuis l'accueil, et dit ce qui n'est pas atteignable.

CE QU'IL SUIT
    accueil --(onclick)--> fonction --(showScreen)--> ecran
                                    --(openOrbPanel)--> panneau
    panneau --(action:)--> fonction --(jeu('nom'))--> jeu d'exercices

CE QU'IL NE VOIT PAS, et il faut le savoir
    Un bouton construit en JavaScript par concatenation de chaines (les barres
    de niveau, par exemple) : son onclick n'existe pas dans le HTML. Ils sont
    reperes a part, par `onclick=\\"` dans les litteraux, et rattaches a la
    fonction qui les fabrique. Un chemin qui depend d'une condition
    (`if(estAdmin)`) est compte comme ouvert : ce releve dit ce qui est
    JOIGNABLE, pas ce qui est visible a tout le monde.
"""
import io
import os
import re
import sys
from collections import deque

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(RACINE, "index.html")
DEPART = "ecran:home"

# ENTREES QUI NE SONT PAS DES CLICS. L'application en a, et les compter comme
# orphelines noierait les vrais defauts sous du bruit. Chacune doit porter la
# raison pour laquelle elle n'est atteinte par aucun bouton -- sans quoi cette
# liste deviendrait l'endroit ou l'on fait taire ce script.
HORS_CLIC = {
    "ecran:setup": "premier lancement : ouvert par le rappel d'authentification "
                   "Firebase quand isSetupDone() est faux, jamais par un clic",
    "ecran:auth": "ecran de depart quand personne n'est connecte",
}


def lire():
    with io.open(SOURCE, encoding="utf-8") as f:
        return f.read()


def corps_des_fonctions(s):
    """Le corps de chaque fonction de premier niveau.

    La fermeture est reconnue a une accolade seule en colonne 0 : c'est le
    style du fichier, verifie sur 575 fonctions. Une fonction imbriquee ne peut
    donc pas fermer sa parente par accident."""
    lignes = s.split("\n")
    debuts = {}
    for i, l in enumerate(lignes):
        m = re.match(r"^(?:async\s+)?function\s+([A-Za-z_$][\w$]*)\s*\(", l)
        if m:
            debuts[i] = m.group(1)
    out = {}
    for i, nom in debuts.items():
        j = i + 1
        while j < len(lignes) and lignes[j] != "}":
            j += 1
        out[nom] = "\n".join(lignes[i:j])
    return out


def ecrans(s):
    return set(re.findall(r'<section\s+id="([^"]+)"\s+class="screen', s))


def onclicks_par_ecran(s):
    """Les fonctions appelees depuis le HTML de chaque ecran."""
    bornes = [(m.group(1), m.start())
              for m in re.finditer(r'<section\s+id="([^"]+)"\s+class="screen', s)]
    bornes.append((None, len(s)))
    out = {}
    for k in range(len(bornes) - 1):
        nom, debut = bornes[k]
        fin = bornes[k + 1][1]
        bloc = s[debut:fin]
        # TOUS les appels de l'attribut, pas seulement le premier. Un bouton
        # ecrit `onclick="event.stopPropagation(); ouvrirAideExamen();"` --
        # s'arreter au premier appel ne verrait que stopPropagation, et
        # l'ecran ouvert par le second passerait pour orphelin.
        #
        # L'ARGUMENT compte autant que le nom : une tuile d'accueil porte
        # `onclick="openOrbPanel('kasus')"`, et retenir « openOrbPanel » sans
        # « kasus » perd tout le graphe, puisque la fonction ouvre alors un
        # panneau nomme par une variable, que rien ne resout statiquement.
        appels = set()
        for attr in re.findall(r'onclick="([^"]*)"', bloc):
            for f, arg in re.findall(
                    r"""([A-Za-z_$][\w$]*)\s*\(\s*(?:['"]([^'"]*)['"])?""", attr):
                appels.add((f, arg))
        out[nom] = appels
    return out


def panneaux(s):
    """Chaque panneau et les fonctions que ses options declenchent."""
    debut = s.index("function orbPanelData(")
    fin = s.index("\nlet openOrbId", debut)
    bloc = s[debut:fin]
    morceaux = re.split(r'if\s*\(\s*id\s*===\s*["\']([^"\']+)["\']\s*\)', bloc)
    out = {}
    for k in range(1, len(morceaux), 2):
        nom = morceaux[k]
        actions = re.findall(r'action:\s*[`"\']([A-Za-z_$][\w$]*)', morceaux[k + 1])
        out[nom] = set(actions)
    return out


def graphe(s):
    fonctions = corps_des_fonctions(s)
    liens = {}

    def relier(a, b):
        liens.setdefault(a, set()).add(b)

    def relier_appel(src, f, arg):
        relier(src, "fn:" + f)
        if not arg:
            return
        if f == "openOrbPanel":
            relier(src, "panneau:" + arg)
        elif f == "showScreen":
            relier(src, "ecran:" + arg)
        elif f == "orbAction":
            relier(src, "fn:" + arg)

    for ecran, appels in onclicks_par_ecran(s).items():
        for f, arg in appels:
            relier_appel("ecran:" + ecran, f, arg)
    for pan, actions in panneaux(s).items():
        for f in actions:
            relier("panneau:" + pan, "fn:" + f)

    for nom, corps in fonctions.items():
        src = "fn:" + nom
        for cible in re.findall(r'showScreen\(\s*["\']([^"\']+)["\']', corps):
            relier(src, "ecran:" + cible)
        for cible in re.findall(r'openOrbPanel\(\s*["\']([^"\']+)["\']', corps):
            relier(src, "panneau:" + cible)
        for cible in re.findall(r'\bjeu\(\s*["\']([^"\']+)["\']', corps):
            relier(src, "jeu:" + cible)
        # Un jeu se lance presque toujours par son NOM passe en chaine a
        # startExerciseSet / startExerciseSetMelange, jamais par jeu() en
        # direct. Sans cette ligne, les 40 jeux paraissent tous orphelins.
        for cible in re.findall(
                r'startExerciseSet\w*\(\s*["\']([^"\']+)["\']', corps):
            relier(src, "jeu:" + cible)
        # Les boutons fabriques en JavaScript : leur onclick est dans une chaine.
        for cible in re.findall(r'onclick=\?["\']\s*([A-Za-z_$][\w$]*)\s*\(', corps):
            if cible in fonctions:
                relier(src, "fn:" + cible)
        # Un appel direct d'une fonction connue compte comme un chemin : c'est
        # ainsi que openNomen() mene a l'ecran des themes.
        for cible in set(re.findall(r'\b([A-Za-z_$][\w$]*)\s*\(', corps)):
            if cible != nom and cible in fonctions:
                relier(src, "fn:" + cible)
    return fonctions, liens


def parcourir(liens, depart):
    """Le plus court chemin depuis l'accueil vers chaque noeud."""
    chemins = {depart: [depart]}
    file = deque([depart])
    while file:
        n = file.popleft()
        for suiv in sorted(liens.get(n, ())):
            if suiv not in chemins:
                chemins[suiv] = chemins[n] + [suiv]
                file.append(suiv)
    return chemins


def joli(n):
    return n.split(":", 1)[1] if ":" in n else n


def main():
    s = lire()
    fonctions, liens = graphe(s)
    chemins = parcourir(liens, DEPART)

    import json
    jeux = json.load(io.open(os.path.join(RACINE, "exercices.json"),
                             encoding="utf-8"))["jeux"]
    tous_ecrans = ecrans(s)
    tous_panneaux = set(panneaux(s))

    seul_orphelins = "--orphelins" in sys.argv
    familles = [
        ("ECRANS", ["ecran:" + x for x in sorted(tous_ecrans)]),
        ("PANNEAUX", ["panneau:" + x for x in sorted(tous_panneaux)]),
        ("JEUX D'EXERCICES", ["jeu:" + x for x in sorted(jeux)]),
    ]

    total_orphelins = 0
    for titre, noeuds in familles:
        orphelins = [n for n in noeuds if n not in chemins and n not in HORS_CLIC]
        total_orphelins += len(orphelins)
        print("\n%s  (%d, dont %d SANS CHEMIN)" % (titre, len(noeuds), len(orphelins)))
        print("-" * 62)
        for n in noeuds:
            c = chemins.get(n)
            if n in HORS_CLIC:
                if not seul_orphelins:
                    print("  %-34s hors clic  (%s)" % (joli(n), HORS_CLIC[n]))
            elif c is None:
                print("  ⚠️  %-34s AUCUN CHEMIN DEPUIS L'ACCUEIL" % joli(n))
            elif not seul_orphelins:
                print("  %-34s %d etapes  %s" %
                      (joli(n), len(c) - 1,
                       " > ".join(joli(x) for x in c[1:]) or "(l'accueil)"))

    print("\n" + "=" * 62)
    if total_orphelins:
        print("⚠️  %d cible(s) sans aucun chemin depuis l'accueil." % total_orphelins)
        print("    C'est exactement le defaut de la v409 : la chose existe,")
        print("    le verificateur la valide, et personne ne peut y arriver.")
        return 1
    print("OK : tout est joignable depuis l'accueil.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
