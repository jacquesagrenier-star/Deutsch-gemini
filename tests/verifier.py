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
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Un chemin peut etre passe en argument pour verifier une variante du fichier
# (utile pour prouver que le filet attrape bien une regression donnee).
INDEX = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RACINE, "index.html")

# C1 ouvert le 30 aout 2026. Les fichiers de verbes, adjectifs et adverbes
# n'ont pas encore de cle "C1" : les boucles ci-dessous acceptent une cle
# absente, donc les y laisser ne coute rien et evite de l'oublier plus tard.
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
PERSONNES = ["ich", "du", "er_sie_es", "wir", "ihr", "sie_Sie"]
GENRES = {"der", "die", "das", "der/die", "der/das", "die (Pl.)"}
REKTIONS = {"", "Nominativ", "Akkusativ", "Dativ", "Akkusativ+Dativ", "Genitiv"}

CATS_ADVERBES = {"Zeit", "Ort/Richtung", "Häufigkeit", "Art und Weise",
                 "Grad/Menge", "Grund/Folge", "Verbindung/Logik", "Frageadverbien",
                 # Marqueurs d'attitude, regroupes avec les particules dans
                 # la porte "Expressions & tournures" (v265).
                 "Nuance/Ton"}
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
    """Renvoie {langue: Counter(cle)} pour TOUS les dictionnaires de traduction.

    Le decoupage etait code en dur pour deux langues : il coupait a "en: {" et
    attribuait tout le reste a l'anglais. Un troisieme bloc voyait donc ses
    cles comptees comme des doublons anglais. On repere maintenant chaque
    entete "    xx: {" et on borne chaque langue par la suivante.
    """
    debut = source.index("const I18N = {")
    fin = source.index("\n};", debut)
    bloc = source[debut:fin]
    entetes = [(m.start(), m.group(1)) for m in re.finditer(r"\n    ([a-z]{2}): \{", bloc)]
    resultat = {}
    for i, (pos, langue) in enumerate(entetes):
        borne = entetes[i + 1][0] if i + 1 < len(entetes) else len(bloc)
        resultat[langue] = collections.Counter(
            m[1] for m in re.findall(r"(^\s{8}|,\s*)([A-Za-z0-9_]+):\s*[\"'`]",
                                     bloc[pos:borne], re.M))
    return resultat


def cles_du_cours():
    """Les clefs de grammaire.json, par langue.

    Elles faisaient partie du bloc I18N jusqu'a la v393. Elles sont maintenant
    versees dans I18N au chargement par chargerCours() -- donc, du point de vue
    de l'app, elles existent. Le verificateur doit voir la meme chose que le
    navigateur, sinon il proteste contre un fichier qui marche.
    """
    chemin = os.path.join(RACINE, "grammaire.json")
    if not os.path.exists(chemin):
        return {}
    with io.open(chemin, encoding="utf-8") as f:
        return json.load(f).get("textes", {})


def verifier_traductions(r, source):
    dicos = blocs_i18n(source)
    cours = cles_du_cours()
    for langue, textes in cours.items():
        if langue not in dicos:
            r.echec("i18n", "grammaire.json parle %s, absent du dictionnaire" % langue)
            continue
        for k in textes:
            # Definie aux deux endroits : la version de grammaire.json ecrase
            # celle d'index.html au chargement, sans rien dire. Une des deux
            # est morte, et on ne sait pas laquelle on lit.
            if k in dicos[langue]:
                r.echec("i18n", "%s : %s est defini DANS index.html ET dans "
                                "grammaire.json (le second ecrase le premier)"
                        % (langue, k))
            dicos[langue][k] = 1
        r.controle(len(textes))
    for langue, cles in dicos.items():
        doublons = [k for k, n in cles.items() if n > 1]
        for k in doublons:
            r.echec("i18n", "%s : cle en double -> %s (la derniere ecrase la premiere)" % (langue, k))
        r.controle(len(cles))
    # Le francais fait reference : c'est la langue d'origine du contenu.
    fr = set(dicos["fr"])
    encours = []
    for langue in sorted(dicos):
        if langue == "fr":
            continue
        autres = set(dicos[langue])
        manquantes = sorted(fr - autres)
        # UNE LANGUE QU'ON REMPLIT N'EST PAS UNE LANGUE CASSEE. L'ukrainien est
        # arrive vide (v388) et se remplit par lots : exiger la parite des le
        # premier jour ferait echouer le verificateur a chaque push pendant des
        # semaines, et on prendrait l'habitude de le lancer en fermant les yeux
        # -- ce qui vaut moins que pas de verificateur du tout.
        #
        # Le repli uk -> en -> fr rend l'absence sans danger : la cle s'affiche
        # en anglais. On COMPTE donc au lieu d'echouer, tant que la langue n'est
        # pas complete. Le jour ou elle l'est, toute cle perdue redevient une
        # erreur -- la regle se referme d'elle-meme, sans rien a desactiver.
        if manquantes and len(autres) < len(fr):
            encours.append((langue, len(autres), len(manquantes)))
        else:
            for k in manquantes:
                r.echec("i18n", "cle absente du dictionnaire %s : %s" % (langue, k))
        for k in sorted(autres - fr):
            r.echec("i18n", "cle absente du dictionnaire francais : %s (vue en %s)" % (k, langue))
    print("   traductions     : " +
          " | ".join("%d cles %s" % (len(dicos[l]), l) for l in sorted(dicos)))
    if cours:
        print("   dont le cours   : %s (grammaire.json)"
              % " | ".join("%d %s" % (len(cours[l]), l) for l in sorted(cours)))
    for langue, faites, reste in encours:
        print("   langue en cours : %s a %d cles sur %d (%.0f %%), %d a ecrire"
              % (langue, faites, len(fr), 100.0 * faites / len(fr), reste))
    return fr


def verifier_langue_enseignee(r, source):
    """La langue enseignee ne peut pas valoir "en".

    prefixeLangue() rangerait alors la progression sous "en__", exactement le
    prefixe que la DIRECTION utilise deja pour le module anglais. Les deux se
    melangeraient sans aucun signe -- le genre de collision qu'on ne voit
    qu'apres avoir perdu des donnees. Le jour ou quelqu'un ecrira code: "en"
    dans LANGUE_ENSEIGNEE, il faut que ca s'arrete ici.
    """
    m = re.search(r'const LANGUE_ENSEIGNEE = \{.*?code:\s*"([a-z]{2})"',
                  source, re.S)
    if not m:
        r.echec("langue", "LANGUE_ENSEIGNEE.code introuvable")
        return
    code = m.group(1)
    if code == "en":
        r.echec("langue", 'LANGUE_ENSEIGNEE.code = "en" : son prefixe de '
                          'progression entrerait en collision avec le "en__" '
                          'du module anglais')
    r.controle(1)
    print("   langue enseignee: %s (prefixe de progression : %s)"
          % (code, "aucun" if code == "de" else code + "__"))


def verifier_jeux_exercices(r, source):
    """Tout jeu demande par son nom doit exister dans exercices.json.

    Depuis la v392 le code ne tient plus les exercices : il les demande par
    leur nom. Le lien entre les deux n'etait verifie nulle part -- un nom mal
    orthographie ne se voyait qu'a l'ouverture de l'exercice, sur un message
    d'erreur. Les cinq JSON de vocabulaire avaient ce controle ; celui-ci
    l'avait perdu en naissant.
    """
    chemin = os.path.join(RACINE, "exercices.json")
    if not os.path.exists(chemin):
        r.echec("exercices", "exercices.json est absent : tous les exercices "
                             "sont hors service")
        return
    try:
        with io.open(chemin, encoding="utf-8") as f:
            jeux = json.load(f).get("jeux", {})
    except ValueError as e:
        r.echec("exercices", "exercices.json illisible : %s" % e)
        return

    demandes = set(re.findall(r'startExerciseSet(?:Melange)?\(\s*"([A-Za-z0-9_]+)"',
                              source))
    for nom in sorted(demandes - set(jeux)):
        r.echec("exercices", "jeu demande par le code mais absent d'exercices.json"
                             " : %s" % nom)
    # L'inverse n'est pas une erreur -- un jeu peut etre prepare avant d'etre
    # branche -- mais il vaut d'etre dit : personne ne le joue.
    orphelins = sorted(set(jeux) - demandes)

    total = 0
    for nom, liste in sorted(jeux.items()):
        if not isinstance(liste, list) or not liste:
            r.echec("exercices", "%s : liste vide ou mal formee" % nom)
            continue
        total += len(liste)
        for k, ex in enumerate(liste):
            if not isinstance(ex, dict):
                r.echec("exercices", "%s[%d] n'est pas un objet" % (nom, k))
                break
            # Le rendu lit question/correct ou chunks : sans l'un des deux,
            # la carte s'affiche vide sans rien signaler.
            if not ex.get("question") and not ex.get("chunks"):
                r.echec("exercices", "%s[%d] n'a ni question ni chunks" % (nom, k))
            if not ex.get("correct") and not ex.get("answers") and not ex.get("chunks"):
                r.echec("exercices", "%s[%d] n'a pas de reponse" % (nom, k))
        r.controle(len(liste))

    print("   exercices.json  : %d jeux, %d exercices, %d demandes par le code"
          % (len(jeux), total, len(demandes)))
    if orphelins:
        print("   jeux non joues  : %s" % ", ".join(orphelins))


# Series ou l'indice est l'ENONCE du drill, pas une fuite : la question donne
# le cas et le genre, l'eleve doit produire le pronom. Sans l'indice, il n'y a
# tout simplement plus d'exercice.
INDICES_QUI_SONT_L_ENONCE = {
    "relativReconNomAkk", "relativReconDativ", "relativReconMixed",
    "relativGenitivReconnaissanceExercises",
}


def verifier_indices_revelateurs(r):
    """Un indice partage ne doit pas annoncer la reponse.

    Le defaut, signale par Jacques sur weil/obwohl : la serie portait DEUX
    indices, un par reponse. Les 14 « weil » avaient le leur, les 14
    « obwohl » l'autre. Reconnaitre l'indice suffisait -- la phrase allemande
    devenait decorative, et l'exercice ne mesurait plus rien.

    Rien ne le signalait : chaque exercice, pris seul, avait un indice juste.
    La fuite n'existe qu'a l'echelle de la serie, et c'est exactement ce
    qu'un controle voit mieux qu'une relecture.

    Ce qui declenche : un choix ferme (2 a 4 reponses possibles) ou un meme
    indice, partage par au moins trois exercices, ne va JAMAIS qu'avec une
    seule reponse.
    """
    chemin = os.path.join(RACINE, "exercices.json")
    if not os.path.exists(chemin):
        return
    try:
        jeux = json.load(io.open(chemin, encoding="utf-8")).get("jeux", {})
    except ValueError:
        return

    for nom, liste in sorted(jeux.items()):
        if nom in INDICES_QUI_SONT_L_ENONCE:
            continue
        if not isinstance(liste, list):
            continue
        reponses = set(ex.get("correct") for ex in liste if isinstance(ex, dict))
        if not (2 <= len(reponses) <= 4):
            continue          # pas un choix ferme : l'indice ne peut rien trahir
        par_indice = {}
        for ex in liste:
            if not isinstance(ex, dict):
                continue
            h = ex.get("hint")
            if h:
                par_indice.setdefault(h, []).append(ex.get("correct"))
        for h, rs in sorted(par_indice.items()):
            r.controle()
            if len(rs) >= 3 and len(set(rs)) == 1:
                r.echec("exercices",
                        "%s : l'indice %s revient %d fois et ne va qu'avec "
                        "« %s » -- il donne la reponse"
                        % (nom, h[:48], len(rs), rs[0]))


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


def verifier_octets_de_controle(r, chemin):
    """Le fichier contient-il un octet qu'aucun navigateur n'attend ?

    ⚠️ LA FAUTE DU 12 SEPTEMBRE 2026. Les scripts de construction passent par
    un heredoc, et ce shell y REDUIT les doubles antislashs meme entre quotes
    simples. `content:"\\00a0\\2022"` est arrive dans index.html sous la forme
    `content:"<NUL>a0<0x82>2"` : un octet NUL au milieu du HTML, et le
    `<script>` entier a cesse de s'analyser -- ni accueil, ni mosaique.

    Le reste du verificateur n'a rien vu : il cherche des cles et des appels,
    et un NUL ne l'en empeche pas. Ce controle-ci ne demande rien a personne,
    il regarde les octets.

    Aucun octet de controle n'a de raison d'etre dans ce fichier, a part la
    tabulation et le saut de ligne.
    """
    octets = io.open(chemin, "rb").read()
    permis = {0x09, 0x0a, 0x0d}
    fautifs = {}
    for i, o in enumerate(octets):
        if o < 0x20 and o not in permis:
            fautifs.setdefault(o, []).append(i)
    for o in sorted(fautifs):
        pos = fautifs[o][0]
        extrait = octets[max(0, pos - 40):pos + 20].decode("utf-8", "replace")
        r.echec("interface",
                "octet de controle 0x%02X dans %s (%d fois, le premier en %d) : %s"
                % (o, os.path.basename(chemin), len(fautifs[o]), pos,
                   extrait.replace("\n", " ")))
    r.controle(len(octets) // 1000 or 1)
    print("   octets        : %d Ko, %d octet(s) de controle interdit"
          % (len(octets) // 1024, sum(len(v) for v in fautifs.values())))


def verifier_zone_morte(r, source):
    """Une constante du sommet en utilise-t-elle une declaree plus bas ?

    ⚠️ LA FAUTE, DEUX FOIS. Un `const` n'est pas remonte comme une fonction : le
    lire avant sa ligne leve une ReferenceError -- sa « zone morte temporelle ».
    Dans un fichier de 26 000 lignes ou tout est au meme niveau, rien ne signale
    qu'une constante en attend une autre sept mille lignes plus bas.

    v555 : REGLES_GENRE_URL valait MOSAIQUE_BASE.replace(...), et MOSAIQUE_BASE
    etait declare 7 650 lignes plus loin. A l'evaluation, TOUT CE QUI SUIT a
    cesse de s'executer -- ni mosaique, ni bandeau de seance, ni la moitie de
    l'accueil. Le fichier portait deja l'avertissement, pose apres un accident
    identique sur des `let`.

    On ne verifie que le cas net : `const X = NOM...` ou NOM est une autre
    constante de premier niveau. Ni les appels de fonction (celles-la sont
    remontees), ni l'interieur des fonctions.
    """
    decls = {}
    for m in re.finditer(r"^const\s+([A-Za-z_$][\w$]*)\s*=", source, re.M):
        decls.setdefault(m.group(1), m.start())
    fautes = 0
    for m in re.finditer(r"^const\s+([A-Za-z_$][\w$]*)\s*=\s*([A-Za-z_$][\w$]*)", source, re.M):
        nom, source_nom = m.group(1), m.group(2)
        if source_nom not in decls:
            continue
        if decls[source_nom] > m.start():
            fautes += 1
            r.echec("interface",
                    "zone morte temporelle : const %s lit %s, declare plus bas"
                    % (nom, source_nom))
        r.controle()
    print("   constantes    : %d au premier niveau, %d en zone morte" % (len(decls), fautes))


def verifier_appels_internes(r, source, fonctions):
    """Un appel en position d'instruction vise-t-il une fonction qui existe ?

    ⚠️ LE TROU QUE CE CONTROLE FERME. La v553 a fait appeler passerAuSuivant()
    par le balayage ; la v553b a supprime cette fonction en defaisant le bouton
    « Suivant » -- et l'appel est reste. Le balayage levait une erreur, la carte
    ne bougeait plus, et l'ecran restait bloque. Personne ne l'a vu avant que
    Jacques ne s'y retrouve coince.

    verifier_appels() ne voyait pas le probleme : il verifie les `onclick` du
    HTML, pas les appels a l'interieur du JavaScript.

    ⚠️ LE MOTIF EST VOLONTAIREMENT ETROIT : une ligne qui ne contient QUE
    `  nomDeFonction();`. Un motif large -- tout `nom(` -- ramenerait les
    fonctions locales, les parametres, les methodes et les globales du
    navigateur, et un controle qui accuse a tort est pire que pas de controle
    (v537). Etroit, il n'attrape pas tout, mais il n'accuse jamais a tort -- et
    il attrape exactement la faute commise.
    """
    appels = set(re.findall(r"^\s{4,}([a-zA-Z_$][\w$]*)\(\);\s*$", source, re.M))
    inconnues = sorted(a for a in appels if a not in fonctions
                       and a not in FONCTIONS_EXTERNES)
    for a in inconnues:
        r.echec("interface", "appel a une fonction qui n'existe pas : %s()" % a)
    r.controle(len(appels))
    print("   appels internes : %d en position d'instruction, %d orphelins"
          % (len(appels), len(inconnues)))


def verifier_tuiles_non_vides(r, source):
    """Une tuile doit garder au moins DEUX entrees une fois le filtre applique.

    C'est le defaut de la v536, trouve a l'usage et non ici : retirer les
    actions de vocabulaire des panneaux a vide la tuile « Noms », qui n'avait
    ni lecon ni exercice propre pour amortir le retrait. Il restait UNE dictee
    sous un titre qui en promet beaucoup plus.

    La regle que ce controle inscrit dans le code : toute modification de
    ACTIONS_VOCABULAIRE se juge sur l'ETAT FINAL DE CHAQUE TUILE, jamais sur la
    constante seule. La constante est lisible d'un coup d'oeil ; ce qu'elle
    laisse dans chaque panneau ne l'est pas.

    Le seuil est deux : une tuile a une seule entree n'est pas un menu, c'est un
    bouton qui s'est deguise en menu -- un ecran de plus pour rien.

    ⚠️ IL DIT AUSSI QUI A VIDE LA TUILE. Une tuile qui n'avait qu'une entree
    AVANT le filtre n'est pas le probleme du filtre : c'est un choix ancien, et
    l'accuser ici ferait porter a la v536 des defauts qu'elle n'a pas commis.
    Un controle qui accuse a tort est pire que pas de controle (v537).
    """
    debut = source.find("function orbPanelData(id){")
    if debut == -1:
        return r.echec("interface", "orbPanelData() introuvable")
    corps = source[debut:source.index("\n}\n", debut)]

    filtre_actif = re.search(r"const VOCAB_DANS_TUILES\s*=\s*(true|false)", source)
    masquees = set()
    if filtre_actif and filtre_actif.group(1) == "false":
        bloc = source[source.index("const ACTIONS_VOCABULAIRE = ["):]
        masquees = set(re.findall(r'"([A-Za-z0-9_]+)"', bloc[:bloc.index("];")]))

    # Un bloc par panneau : if(id === "xxx"){ ... } jusqu'au panneau suivant.
    # Un « open... » ouvre un ecran de choix, un « start... » pose une carte.
    # Masquer un sommaire ferme une consultation, pas une revision generique --
    # c'est ce qui avait vide « Noms » et « Expressions ».
    for a in sorted(masquees):
        if not a.startswith("start"):
            r.echec("interface",
                    "ACTIONS_VOCABULAIRE contient un sommaire : %s() ouvre un "
                    "ecran de choix, il n'a pas a etre masque" % a)
    r.controle(len(masquees))

    bornes = [(m.group(1), m.start()) for m in
              re.finditer(r'if\(id === "([a-z0-9]+)"\)\{', corps)]
    vides = 0
    for i, (nom, pos) in enumerate(bornes):
        fin = bornes[i + 1][1] if i + 1 < len(bornes) else len(corps)
        actions = re.findall(r'action:\s*"([A-Za-z0-9_]+)"', corps[pos:fin])
        restantes = [a for a in actions if a not in masquees]
        if len(restantes) < 2:
            vides += 1
            if len(actions) < 2:
                # Pas le filtre : cette tuile n'a jamais eu qu'une entree.
                r.alerte("interface",
                          "la tuile « %s » n'a qu'une entree, filtre ou pas : un menu "
                          "d'un seul element est un bouton deguise" % nom)
            else:
                r.echec("interface",
                        "le filtre du vocabulaire vide la tuile « %s » : %d entree(s) "
                        "sur %d, il reste %s"
                        % (nom, len(restantes), len(actions), ", ".join(restantes) or "rien"))
        r.controle(1)
    print("   tuiles          : %d panneaux, %d actions masquees, %d a une seule entree"
          % (len(bornes), len(masquees), vides))


# --------------------------------------------------------------------------

def verifier_taille_des_champs(r, source):
    """Aucun champ de saisie ne doit descendre sous 16px.

    En dessous, Safari iOS zoome sur le champ des qu'on le touche ET NE
    DEZOOME PAS : l'app reste plus large que l'ecran, et il faut pincer a deux
    doigts pour revenir. Signale trois fois par le meme testeur avant qu'on
    trouve d'ou ca venait (v503 puis v506).

    Deux failles distinctes, et ce controle ferme les deux :
      - une taille ECRITE sous 16px (le cas de .filters-bar, #retourTexte et
        .admin-code-note, corriges en v503) ;
      - une taille ABSENTE, donc heritee du navigateur -- le cas du selecteur
        de voix, mesure a 13,33px. C'est celui qu'aucune recherche de texte
        n'attrape : il n'y a rien a chercher. D'ou la regle de base
        `input, textarea, select` dans le CSS, dont l'absence est un echec
        ici : sans elle, le prochain champ cree sans style repart a 13px.
    """
    # a) La regle de base doit exister, sinon le filet a un trou.
    if not re.search(r"input,\s*textarea,\s*select\s*\{[^}]*font-size:\s*16px", source):
        r.echec("interface",
                "la regle de base `input, textarea, select { font-size:16px }` a disparu -- "
                "tout champ cree sans style repartira a 13px et fera zoomer Safari iOS")
    r.controle()

    # b) Aucune taille explicite sous 16px sur un champ, inline ou en CSS.
    fautes = []
    for m in re.finditer(r"<(input|textarea|select)\b[^>]*style=\"([^\"]*)\"", source):
        px = re.search(r"font-size:\s*(\d+(?:\.\d+)?)px", m.group(2))
        if px and float(px.group(1)) < 16:
            fautes.append("<%s style=\"...font-size:%spx...\">" % (m.group(1), px.group(1)))
    # Les blocs CSS dont le selecteur nomme un champ.
    for m in re.finditer(r"([^{}]*(?:input|textarea|select)[^{}]*)\{([^}]*)\}", source):
        sel = m.group(1).strip().splitlines()[-1].strip()
        if sel.startswith("/*") or "::placeholder" in sel:
            continue
        px = re.search(r"font-size:\s*(\d+(?:\.\d+)?)px", m.group(2))
        if px and float(px.group(1)) < 16:
            fautes.append("%s { font-size:%spx }" % (sel, px.group(1)))
    for f in fautes:
        r.echec("interface",
                "champ de saisie sous 16px -- Safari iOS zoomera dessus sans dezoomer : %s" % f)
    r.controle(max(1, len(fautes)))
    print("   champs de saisie: plancher de 16px respecte (%d faute%s)"
          % (len(fautes), "s" if len(fautes) > 1 else ""))


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



def verifier_chemins(r):
    """Chaque ecran, panneau et jeu est-il ATTEIGNABLE depuis l'accueil ?

    Le reste de ce fichier repond a « la cible existe-t-elle ? ». Cette
    question-la est differente, et la difference a deja coute une version : en
    v409, un ecran, 45 exercices et 18 cartes existaient depuis des mois, tous
    valides ici -- et aucune tuile ne les portait. C'est un usager qui l'a
    trouve. Le parcours du graphe vit dans tests/chemins.py, qui s'execute
    aussi seul et sait montrer le chemin complet de chaque cible.
    """
    try:
        import chemins
    except ImportError as e:
        r.alerte("chemins", "tests/chemins.py introuvable : %s" % e)
        return
    source = chemins.lire()
    _, liens = chemins.graphe(source)
    joignables = chemins.parcourir(liens, chemins.DEPART)
    cibles = ([("ecran:" + x) for x in chemins.ecrans(source)]
              + [("panneau:" + x) for x in chemins.panneaux(source)])
    try:
        with io.open(os.path.join(RACINE, "exercices.json"), encoding="utf-8") as f:
            cibles += ["jeu:" + x for x in json.load(f).get("jeux", {})]
    except (IOError, ValueError):
        pass
    perdus = [c for c in sorted(cibles)
              if c not in joignables and c not in chemins.HORS_CLIC]
    for c in perdus:
        r.echec("chemins", "aucun chemin depuis l'accueil vers %s" % c)
    r.controle(len(cibles))
    print("   chemins d'acces : %d cibles, %d sans chemin" % (len(cibles), len(perdus)))


def verifier_export_csv(r):
    """Les CSV de export/ sont-ils encore le reflet des JSON ?

    Ce sont des fichiers derives : rien ne les regenere tout seul, et ils
    avaient pris quatre versions de retard sans que rien ne le signale. Un
    avertissement, pas une erreur : une donnee modifiee sans avoir encore
    relance l'export n'est pas une regression, seulement un export a refaire.
    """
    try:
        import exporter
    except Exception:
        return                      # exporter.py absent : rien a verifier
    dossier = os.path.join(RACINE, "export")
    if not os.path.isdir(dossier):
        return
    try:
        attendus = exporter.produire()
    except Exception as e:
        return r.alerte("export", "exporter.py n'a pas pu produire les CSV (%s)" % e)
    retard = []
    for nom, contenu in sorted(attendus.items()):
        r.controle()
        chemin = os.path.join(dossier, nom)
        if not os.path.exists(chemin):
            retard.append(nom)
            continue
        actuel = io.open(chemin, encoding="utf-8-sig", newline="").read()
        if actuel and not actuel.startswith(exporter.BOM):
            actuel = exporter.BOM + actuel
        if actuel != contenu:
            retard.append(nom)
    if retard:
        r.alerte("export", "%d CSV en retard sur les JSON (%s) -- relancer : "
                           "python tests/exporter.py" % (len(retard), ", ".join(retard[:3])
                                                         + ("..." if len(retard) > 3 else "")))
    print("   export/         : %d CSV, %s" % (len(attendus),
          "a jour" if not retard else "%d en retard" % len(retard)))


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
    verifier_jeux_exercices(r, source)
    verifier_indices_revelateurs(r)
    verifier_langue_enseignee(r, source)
    verifier_cles_utilisees(r, source, cles)
    fonctions = fonctions_definies(source)
    verifier_appels(r, source, fonctions)
    verifier_ecrans(r, source, fonctions)
    verifier_retours_flashcards(r, source)
    verifier_octets_de_controle(r, INDEX)
    verifier_zone_morte(r, source)
    verifier_appels_internes(r, source, fonctions)
    verifier_tuiles_non_vides(r, source)
    verifier_taille_des_champs(r, source)
    verifier_version(r, source)
    verifier_chemins(r)
    verifier_export_csv(r)

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
