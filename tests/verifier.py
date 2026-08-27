# -*- coding: utf-8 -*-
"""
Verificateur de DeutschAI / Wortando.

Lancer avant chaque push :

    python tests/verifier.py

Sort en code 0 si tout va bien, 1 sinon. Aucune dependance : ni npm, ni
navigateur. Le fichier index.html est analyse comme du texte, ce qui suffit a
detecter la grande majorite des regressions rencontrees en pratique -- un
ecran cible qui n'existe pas, une fonction appelee mais jamais definie, une
cle de traduction en double ou absente d'une des deux langues.

Ce que ce verificateur NE fait PAS : juger la qualite d'une traduction, d'une
phrase d'exemple ou d'une mise en page. Il verifie que rien n'est casse, pas
que c'est bien.
"""
import io
import json
import os
import re
import sys
import collections

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Un chemin peut etre passe en argument pour verifier une variante du fichier
# (utile pour prouver que le filet attrape bien une regression donnee).
INDEX = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RACINE, "index.html")

NIVEAUX = ["A1", "A2", "B1", "B2"]
PERSONNES = ["ich", "du", "er_sie_es", "wir", "ihr", "sie_Sie"]
GENRES = {"der", "die", "das", "der/die", "der/das", "die (Pl.)"}
REKTIONS = {"", "Nominativ", "Akkusativ", "Dativ", "Akkusativ+Dativ", "Genitiv"}

CATS_ADVERBES = {"Zeit", "Ort/Richtung", "Häufigkeit", "Art und Weise",
                 "Grad/Menge", "Grund/Folge", "Verbindung/Logik", "Frageadverbien"}
CATS_EXPRESSIONS = {"Begrüßung/Small Talk", "Meinung/Zustimmung", "Gefühle/Reaktionen",
                    "Alltag/Organisation", "Diskussion/Nuance", "Feste Verbindungen"}

# Fonctions fournies par le navigateur ou par Firebase, appelees depuis le HTML
# mais definies ailleurs que dans index.html.
FONCTIONS_EXTERNES = {"print", "alert", "confirm", "history", "location", "window"}


class Rapport:
    def __init__(self):
        self.erreurs = []
        self.avertissements = []
        self.controles = 0

    def echec(self, categorie, message):
        self.erreurs.append((categorie, message))

    def alerte(self, categorie, message):
        self.avertissements.append((categorie, message))

    def controle(self, n=1):
        self.controles += n


# --------------------------------------------------------------------------
#  1. DONNEES
# --------------------------------------------------------------------------

def charger(nom):
    chemin = os.path.join(RACINE, nom)
    if not os.path.exists(chemin):
        return None
    return json.load(io.open(chemin, encoding="utf-8"))


def verifier_verbes(r):
    d = charger("verbe.json")
    if d is None:
        return r.echec("verbe.json", "fichier introuvable")
    requis = ["infinitif", "traduction", "traduction_en", "praesens", "exemple",
              "exemple_fr", "exemple_en", "perfekt", "perfekt_fr", "perfekt_en",
              "praeteritum", "praeteritum_fr", "praeteritum_en",
              "konjunktiv2", "konjunktiv2_fr", "konjunktiv2_en"]
    vus = {}
    for niveau in NIVEAUX:
        for v in d.get(niveau, []):
            r.controle()
            inf = v.get("infinitif", "?")
            for champ in requis:
                if not v.get(champ):
                    r.echec("verbe.json", "%s (%s) : champ vide -> %s" % (inf, niveau, champ))
            pr = v.get("praesens") or {}
            manquants = [p for p in PERSONNES if not pr.get(p)]
            if manquants:
                r.echec("verbe.json", "%s (%s) : praesens incomplet %s" % (inf, niveau, manquants))
            if "rektion" in v and v["rektion"] not in REKTIONS:
                r.echec("verbe.json", "%s : rektion inconnue %r" % (inf, v["rektion"]))
            if inf in vus:
                r.echec("verbe.json", "%s : doublon (%s et %s)" % (inf, vus[inf], niveau))
            vus[inf] = niveau
    print("   verbe.json      : %d verbes" % len(vus))


def verifier_liste(r, fichier, cats, nom_champ="mot"):
    d = charger(fichier)
    if d is None:
        return r.echec(fichier, "fichier introuvable")
    requis = [nom_champ, "traduction", "traduction_en", "kategorie",
              "exemple", "exemple_fr", "exemple_en"]
    vus = {}
    total = 0
    for niveau in NIVEAUX:
        for e in d.get(niveau, []):
            r.controle()
            total += 1
            mot = e.get(nom_champ, "?")
            for champ in requis:
                if not e.get(champ):
                    r.echec(fichier, "%s (%s) : champ vide -> %s" % (mot, niveau, champ))
            if e.get("kategorie") not in cats:
                r.echec(fichier, "%s : categorie inconnue %r" % (mot, e.get("kategorie")))
            if mot in vus:
                r.echec(fichier, "%s : doublon (%s et %s)" % (mot, vus[mot], niveau))
            vus[mot] = niveau
    print("   %-15s : %d entrees" % (fichier, total))


# Modules anglais : phrasal verbs, verbes irreguliers, pieges, expressions.
# Forme voisine des fichiers allemands, mais le mot vedette est anglais et la
# phrase d'exemple l'est aussi -- il n'y a donc pas de champ "exemple_en".
FICHIERS_ANGLAIS = [
    ("english_themes.json", None),
    ("phrasal_verbs.json", None),
    ("english_verbs.json", "formes"),
    ("english_britam.json", None),
    ("english_pitfalls.json", None),
    ("english_expressions.json", None),
]


def verifier_anglais(r):
    for fichier, champ_extra in FICHIERS_ANGLAIS:
        d = charger(fichier)
        if d is None:
            r.echec(fichier, "fichier introuvable")
            continue
        requis = ["mot", "traduction", "traduction_en", "kategorie",
                  "exemple", "exemple_fr"]
        vus = {}
        total = 0
        cats = set()
        for niveau in NIVEAUX:
            for e in d.get(niveau, []):
                r.controle()
                total += 1
                mot = e.get("mot", "?")
                for champ in requis:
                    if not e.get(champ):
                        r.echec(fichier, "%s (%s) : champ vide -> %s" % (mot, niveau, champ))
                if champ_extra and not e.get(champ_extra):
                    r.echec(fichier, "%s (%s) : champ vide -> %s" % (mot, niveau, champ_extra))
                # Un faux ami sans ligne "piege" perd tout son interet : c'est
                # justement elle qui nomme le mot francais trompeur.
                if e.get("kategorie") == "Faux amis" and not e.get("piege"):
                    r.echec(fichier, "%s : faux ami sans champ 'piege'" % mot)
                if mot in vus:
                    r.echec(fichier, "%s : doublon (%s et %s)" % (mot, vus[mot], niveau))
                vus[mot] = niveau
                cats.add(e.get("kategorie"))
        print("   %-24s : %d entrees, %d familles" % (fichier, total, len(cats)))


def verifier_themes(r):
    d = charger("themes.json")
    if d is None:
        return r.echec("themes.json", "fichier introuvable")
    themes = d.get("themes", [])
    ids = collections.Counter(t.get("id") for t in themes)
    for identifiant, n in ids.items():
        if n > 1:
            r.echec("themes.json", "id de theme en double : %s" % identifiant)
    noms, verbes, adjectifs = 0, 0, 0
    for t in themes:
        r.controle()
        niveau = t.get("niveau")
        if niveau not in NIVEAUX:
            r.echec("themes.json", "%s : niveau inconnu %r" % (t.get("id"), niveau))
        for m in t.get("mots", []):
            noms += 1
            for champ in ("mot", "genre", "traduction", "exemple", "exemple_fr"):
                if not m.get(champ):
                    r.echec("themes.json", "%s / %s : champ vide -> %s"
                            % (t.get("id"), m.get("mot", "?"), champ))
            if m.get("genre") not in GENRES:
                r.echec("themes.json", "%s : genre invalide %r" % (m.get("mot"), m.get("genre")))
        # Les verbes des chapitres VHS suivent le meme contrat que verbe.json
        for v in t.get("verben", []):
            verbes += 1
            pr = v.get("praesens") or {}
            if not pr:
                r.alerte("themes.json", "%s / %s : verbe sans conjugaison"
                         % (t.get("id"), v.get("infinitif")))
            elif [p for p in PERSONNES if not pr.get(p)]:
                r.echec("themes.json", "%s : praesens incomplet" % v.get("infinitif"))
        adjectifs += len(t.get("adjektive", []))
    print("   themes.json     : %d themes, %d noms, %d verbes, %d adjectifs"
          % (len(themes), noms, verbes, adjectifs))


def verifier_adjectifs(r):
    d = charger("adjectif.json")
    if d is None:
        return r.echec("adjectif.json", "fichier introuvable")
    total, vus = 0, {}
    for niveau in NIVEAUX:
        for a in d.get(niveau, []):
            r.controle()
            total += 1
            mot = a.get("mot", "?")
            for champ in ("mot", "traduction", "exemple"):
                if not a.get(champ):
                    r.echec("adjectif.json", "%s (%s) : champ vide -> %s" % (mot, niveau, champ))
            if mot in vus:
                r.echec("adjectif.json", "%s : doublon (%s et %s)" % (mot, vus[mot], niveau))
            vus[mot] = niveau
    print("   adjectif.json   : %d adjectifs" % total)


# --------------------------------------------------------------------------
#  2. CODE ET INTERFACE
# --------------------------------------------------------------------------

def blocs_i18n(source):
    """Renvoie {langue: {cle: ligne}} pour les deux dictionnaires de traduction."""
    debut = source.index("const I18N = {")
    fin = source.index("\n};", debut)
    bloc = source[debut:fin]
    coupe = bloc.index("\n    en: {")
    resultat = {}
    for langue, segment in (("fr", bloc[:coupe]), ("en", bloc[coupe:])):
        cles = collections.Counter(
            m[1] for m in re.findall(r"(^\s{8}|,\s*)([A-Za-z0-9_]+):\s*[\"'`]", segment, re.M))
        resultat[langue] = cles
    return resultat


def verifier_traductions(r, source):
    dicos = blocs_i18n(source)
    for langue, cles in dicos.items():
        doublons = [k for k, n in cles.items() if n > 1]
        for k in doublons:
            r.echec("i18n", "%s : cle en double -> %s (la derniere ecrase la premiere)" % (langue, k))
        r.controle(len(cles))
    fr, en = set(dicos["fr"]), set(dicos["en"])
    for k in sorted(fr - en):
        r.echec("i18n", "cle absente du dictionnaire anglais : %s" % k)
    for k in sorted(en - fr):
        r.echec("i18n", "cle absente du dictionnaire francais : %s" % k)
    print("   traductions     : %d cles fr, %d cles en" % (len(fr), len(en)))
    return fr


def verifier_cles_utilisees(r, source, cles):
    """Toute cle citee dans le HTML ou via t()/tf() doit exister."""
    citees = set()
    for attribut in ("data-i18n", "data-i18n-html", "data-i18n-placeholder"):
        citees |= set(re.findall(attribut + r'="([A-Za-z0-9_]+)"', source))
    citees |= set(re.findall(r"\bt\(\s*'([A-Za-z0-9_]+)'\s*\)", source))
    citees |= set(re.findall(r'\bt\(\s*"([A-Za-z0-9_]+)"\s*\)', source))
    citees |= set(re.findall(r"\btf\(\s*'([A-Za-z0-9_]+)'", source))
    citees |= set(re.findall(r'\btf\(\s*"([A-Za-z0-9_]+)"', source))
    for k in sorted(citees - cles):
        r.echec("i18n", "cle utilisee mais jamais definie : %s" % k)
    r.controle(len(citees))
    print("   cles utilisees  : %d" % len(citees))


def fonctions_definies(source):
    noms = set(re.findall(r"\bfunction\s+([A-Za-z0-9_]+)\s*\(", source))
    noms |= set(re.findall(r"\b(?:const|let|var)\s+([A-Za-z0-9_]+)\s*=\s*(?:async\s*)?\(?[A-Za-z0-9_,\s]*\)?\s*=>", source))
    noms |= set(re.findall(r"window\.([A-Za-z0-9_]+)\s*=", source))
    return noms


def verifier_appels(r, source, fonctions):
    """Chaque onclick du HTML doit viser une fonction reellement definie."""
    appels = set(re.findall(r'onclick="([A-Za-z0-9_]+)\s*\(', source))
    appels |= set(re.findall(r"onclick=\\?\"?([A-Za-z0-9_]+)\s*\(", source))
    inconnues = sorted(a for a in appels if a not in fonctions and a not in FONCTIONS_EXTERNES)
    for a in inconnues:
        r.echec("interface", "onclick appelle une fonction inexistante : %s()" % a)
    r.controle(len(appels))
    print("   appels onclick  : %d" % len(appels))


def verifier_ecrans(r, source, fonctions):
    """showScreen("x") doit viser une <section id="x"> existante."""
    sections = set(re.findall(r'<section id="([A-Za-z0-9_]+)"', source))
    cibles = set(re.findall(r'showScreen\(\s*["\']([A-Za-z0-9_]+)["\']', source))
    for c in sorted(cibles - sections):
        r.echec("interface", "showScreen vise un ecran inexistant : %s" % c)
    r.controle(len(cibles))
    # Les actions des panneaux sont appelees par window[action]()
    actions = set(re.findall(r'action:\s*"([A-Za-z0-9_]+)"', source))
    for a in sorted(actions):
        if a not in fonctions and not a.startswith("comingSoonPanel"):
            r.echec("interface", "action de panneau sans fonction : %s()" % a)
    r.controle(len(actions))
    print("   ecrans          : %d sections, %d cibles, %d actions de panneau"
          % (len(sections), len(cibles), len(actions)))


def verifier_retours_flashcards(r, source):
    """Chaque mode de flashcard doit avoir un ecran de retour explicite.

    C'est la regression exacte rencontree en v198 : les modes 'adverbien' et
    'konjunktionen' n'etaient pas dans la table, et leur bouton Retour tombait
    dans le cas par defaut -- l'ecran des noms.
    """
    modes = set(re.findall(r"flashcardMode\s*=\s*'([a-z]+)'", source))
    debut = source.find("const FLASHCARD_RETURN_SCREENS = {")
    if debut == -1:
        return r.echec("interface", "table FLASHCARD_RETURN_SCREENS introuvable")
    table = source[debut:source.index("};", debut)]
    traites = set(re.findall(r"^\s{4}([a-z]+):", table, re.M))
    # Les modes lies aux noms passent par nomenReturnScreen
    par_defaut = {"nomen", "vhskapitelverben", "vhskapiteladjektive"}
    oublies = sorted(modes - traites - par_defaut)
    for m in oublies:
        r.echec("interface",
                "mode de flashcard sans ecran de retour : '%s' (le bouton Retour ira vers Noms)" % m)
    r.controle(len(modes))
    print("   modes de cartes : %d, dont %d dans la table de retour" % (len(modes), len(traites)))


# --------------------------------------------------------------------------

def verifier_version(r, source):
    """Le numero de version vit a trois endroits : l'etiquette affichee, la
    constante APP_VERSION et version.json, que l'app distante consulte pour
    savoir si un appareil est reste en arriere. Les trois doivent concorder --
    sinon soit l'etiquette ment, soit personne n'est prevenu de la mise a jour.
    """
    badge = re.search(r'class="subtitle-version">v(\d+)<', source)
    const = re.search(r"const APP_VERSION = (\d+);", source)
    fichier = charger("version.json")
    if not badge:
        return r.echec("version", "etiquette de version introuvable dans index.html")
    if not const:
        return r.echec("version", "const APP_VERSION introuvable dans index.html")
    if fichier is None:
        return r.echec("version", "version.json introuvable")
    n_badge, n_const = int(badge.group(1)), int(const.group(1))
    n_fichier = int(fichier.get("version", 0))
    r.controle(3)
    if not (n_badge == n_const == n_fichier):
        r.echec("version", "numeros discordants -- etiquette v%d, APP_VERSION %d, version.json %d"
                % (n_badge, n_const, n_fichier))
    print("   version         : v%d (etiquette, APP_VERSION et version.json concordent)" % n_badge)


def main():
    if not os.path.exists(INDEX):
        print("index.html introuvable dans %s" % RACINE)
        return 1
    source = io.open(INDEX, encoding="utf-8").read()
    r = Rapport()

    print("\nDONNEES")
    verifier_verbes(r)
    verifier_adjectifs(r)
    verifier_liste(r, "adverbe.json", CATS_ADVERBES)
    verifier_liste(r, "redewendung.json", CATS_EXPRESSIONS)
    verifier_themes(r)

    print("\nMODULES ANGLAIS")
    verifier_anglais(r)

    print("\nCODE ET INTERFACE")
    cles = verifier_traductions(r, source)
    verifier_cles_utilisees(r, source, cles)
    fonctions = fonctions_definies(source)
    verifier_appels(r, source, fonctions)
    verifier_ecrans(r, source, fonctions)
    verifier_retours_flashcards(r, source)
    verifier_version(r, source)

    print("\n" + "-" * 62)
    if r.avertissements:
        print("%d avertissement(s) :" % len(r.avertissements))
        for cat, msg in r.avertissements[:15]:
            print("   [%s] %s" % (cat, msg))
        if len(r.avertissements) > 15:
            print("   ... et %d autres" % (len(r.avertissements) - 15))
    if r.erreurs:
        print("\nECHEC : %d probleme(s) sur %d controles\n" % (len(r.erreurs), r.controles))
        for cat, msg in r.erreurs[:40]:
            print("   [%s] %s" % (cat, msg))
        if len(r.erreurs) > 40:
            print("   ... et %d autres" % (len(r.erreurs) - 40))
        return 1
    print("\nOK : %d controles passes, aucun probleme.\n" % r.controles)
    return 0


if __name__ == "__main__":
    sys.exit(main())
