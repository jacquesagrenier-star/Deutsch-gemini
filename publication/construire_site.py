"""
LE SITE PUBLIC : SEULEMENT L'APP (11 nov. 2026, audit de lancement, point 2).

Cloudflare Pages publiait le DEPOT ENTIER sur wortando.com : le journal des
retours (prenoms de testeurs), les decisions, CLAUDE.md, .claude/, tests/...
repondaient 200. Rendre le depot GitHub prive n'y changeait rien.

Ce script copie dans `_site/` la seule liste blanche ci-dessous ; Cloudflare
publie `_site/` et rien d'autre. Une page ou un fichier NOUVEAU que l'app doit
charger doit donc entrer dans la liste, sinon il repond 404 en ligne :

    python publication/construire_site.py --sortie "$TEMP/_site" --verifier

dit ce qui sort (tout ce qui est publie, par dossier) et ce qui manque
(fichiers cites par le site mais laisses dehors). Sur le PC, toujours avec
--sortie hors de OneDrive. Mode d'emploi : publication/LISEZ-MOI.md.

Reglage Cloudflare (une fois, par Jacques) :
    Commande de construction : python3 publication/construire_site.py
    Dossier de sortie        : _site

Il ecrit aussi _site/_redirects (les fichiers internes vers l'accueil, en 301) :
voir la section 3 et publication/LISEZ-MOI.md.

Aucune dependance : bibliotheque standard de Python 3, comme sur la machine de
construction de Cloudflare.
"""
import os
import re
import shutil
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# --sortie <dossier> : construire ailleurs. Sur le PC, TOUJOURS hors de
# OneDrive (le site pese plus de 250 Mo, et OneDrive le synchroniserait).
SORTIE = (sys.argv[sys.argv.index("--sortie") + 1] if "--sortie" in sys.argv
          else os.path.join(RACINE, "_site"))

IMAGES = {"webp", "png", "jpg", "jpeg", "gif", "svg", "ico"}
SONS = {"mp3", "m4a", "ogg", "wav"}
VIDEOS = {"mp4", "webm"}
PAGES = {"html", "js", "mjs", "css", "json"}

# ---- 1. Les fichiers de la racine, un par un ----
FICHIERS_RACINE = [
    # L'app, son service worker, son manifeste et sa version.
    "index.html", "firebase-messaging-sw.js", "manifest.json", "version.json",
    # Les pages que les magasins et la politique citent par leur adresse.
    "confidentialite.html", "conditions.html", "supprimer-compte.html",
    # Les donnees allemandes, lues depuis la racine.
    "a1-voyage.json", "adjectif.json", "adverbe.json", "conjugaison.json",
    "etapes.json", "exercices.json", "frequence.json", "funktionswort.json",
    "grammaire.json", "je-sais.json", "premiers-pas.json", "prononciation.json",
    "pruefung.json", "redewendung.json", "reperes.json", "synonymes.json",
    "themes.json", "verbe.json",
    # L'ancien module anglais (masque depuis la v727, mais encore lu).
    "english_britam.json", "english_expressions.json", "english_pitfalls.json",
    "english_themes.json", "english_verbs.json", "phrasal_verbs.json",
]

# ---- 2. Les dossiers : prefixe -> extensions permises (a toute profondeur) ----
# Les sources (.py), les notes (.md, .txt), les lots de relecture, les outils
# restent dehors meme dans un dossier publie.
DOSSIERS = {
    # Les liens d'application Android (Google Play).
    ".well-known/": {"json"},
    # Icones, logo, mosaique allemande, regles du genre.
    "branding/": IMAGES | {"json"},
    # Le dictionnaire allemand (WikDict, CC BY-SA) et sa licence.
    "dict/": {"json"},
    # Le ciel des etoiles.
    "etoiles/ciel.json": None,
    # La visite guidee, en voix.
    "voix-visite/": SONS | {"json"},
    # Les videos de l'app (ouverture, demarrage) et le schema de preparation.
    "video/": VIDEOS | {"jpg", "png"},
    # Les scenes, les themes illustres, l'essai du DTZ, les fonds.
    "visuel/prototype/": PAGES | IMAGES | SONS | VIDEOS,
    "visuel/fond/": IMAGES,
    # L'espagnol : donnees, dictionnaire, mosaique, et l'ancienne adresse
    # espanol/ (redirection + service worker qui se desinscrit).
    "espanol/index.html": None,
    "espanol/sw.js": None,
    "espanol/manifest.json": None,
    "espanol/version.json": None,
    "espanol/marca/wortando-icono.png": None,
    "espanol/marca/wortando-apple-touch-icon.png": None,
    "espanol/datos/": {"json"},
    "espanol/dicc/": {"json"},
    "espanol/mosaique/": IMAGES | {"json", "html"},
    # Le japonais (essai admin).
    "japonais/datos/": {"json"},
    "japonais/kana/traits/": IMAGES,
    "japonais/kanji/traits/": IMAGES,
    "japonais/mosaique/app/": IMAGES | {"json"},
    # L'anglais (essai admin) : americain, britannique, mosaique.
    "anglais/datos/": {"json"},
    "anglais/datos-gb/": {"json"},
    "anglais/mosaique/app/": IMAGES | {"json"},
    # Le portugais (essai admin) : Portugal, Bresil, mosaique.
    "portugais/datos/": {"json"},
    "portugais/datos-br/": {"json"},
    "portugais/dicc/": {"json"},
    "portugais/mosaique/app/": IMAGES | {"json"},
}

# Jamais publies, meme sous un prefixe permis.
EXCLUS = re.compile(r"(^|/)(__pycache__|outils|lots|sources|_essai[^/]*|\.git[^/]*)(/|$)")

# La page des adresses inconnues (sinon Cloudflare sert l'app, en 200, pour
# n'importe quelle adresse, et un fichier retire ne repond jamais 404).
PAGE_404 = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Wortando</title>
<style>body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
font:17px/1.5 system-ui,sans-serif;background:#F6F1E7;color:#1C2430;text-align:center;padding:16px}
a{color:#1C2430;font-weight:700}</style></head>
<body><main><p>Cette page n'existe pas.</p><p><a href="/">Ouvrir Wortando</a></p></main></body></html>
"""


# ---- 3. Les redirections des fichiers internes (12 nov. 2026) ----
# Le « cache de preservation » de Cloudflare Pages (workers-sdk,
# pages-shared/asset-server/handler.ts, assetPreservationCacheV2) garde 7 jours,
# par URL exacte et par centre de donnees, chaque fichier qu'il a servi ; quand
# le deploiement actuel n'a plus le fichier, il le RESSERT au lieu de la 404.
# Apres le passage a _site/, wortando.com servait encore CLAUDE.md,
# decisions/DECISIONS.md, firestore.rules... et « Purge Everything » ne l'a pas
# vide. Pages lit _redirects AVANT de chercher un fichier : une redirection vers
# l'accueil passe devant ce cache, partout et des le deploiement.
#
# La liste est DERIVEE de ce qui n'est pas publie (rien a tenir a la main) :
#  - un joker « /dossier/* » pour chaque dossier sans AUCUN fichier publie
#    dessous (le plus haut possible), jamais pour un dossier de l'app (ci-dessous) ;
#  - une ligne par fichier interne restant (racine, notes et sources rangees a
#    cote de fichiers publies).
# Un dossier qui gagne un fichier publie perd son joker a la construction
# suivante. La construction s'arrete si une regle couvrait un fichier publie.
JAMAIS_DE_JOKER = {"visuel", "espanol", "anglais", "portugais", "japonais", "audio"}
MAX_STATIQUES = 2000   # limites de Cloudflare Pages (constants.ts)
MAX_JOKERS = 100
# Un chemin d'URL tel que le navigateur l'envoie : accents et espaces encodes ;
# « * » et « : » encodes aussi (ils feraient d'une ligne une regle dynamique).
SURS_DANS_URL = "/!$&'()+,;=@~-._"


def _url(chemin):
    from urllib.parse import quote
    return "/" + quote(chemin, safe=SURS_DANS_URL)


def redirections(retenus):
    """(jokers, statiques, laisses) : dossiers et fichiers internes renvoyes vers /."""
    publies = set(retenus)
    dehors = [c for c in fichiers_du_depot() if c not in publies]
    # Tout dossier qui contient (a toute profondeur) un fichier publie.
    habites = set()
    for c in retenus:
        parties = c.split("/")[:-1]
        for i in range(1, len(parties) + 1):
            habites.add("/".join(parties[:i]))

    def dossier_joker(c):
        """Le plus haut dossier de c sans fichier publie (hors dossiers de l'app au 1er niveau)."""
        parties = c.split("/")[:-1]
        for i in range(1, len(parties) + 1):
            d = "/".join(parties[:i])
            if d in habites:
                continue
            if i == 1 and d in JAMAIS_DE_JOKER:
                continue
            return d
        return None

    par_dossier = {}
    isoles = []
    for c in dehors:
        d = dossier_joker(c)
        if d:
            par_dossier.setdefault(d, []).append(c)
        elif c + ".html" not in publies and c + "/index.html" not in publies:
            # (« /conditions » est l'adresse courte de conditions.html : pas de ligne)
            isoles.append(c)
    # Les plus gros dossiers en joker ; au-dela de 100, leurs fichiers en lignes.
    tries = sorted(par_dossier, key=lambda d: (-len(par_dossier[d]), d))
    jokers = sorted(tries[:MAX_JOKERS])
    for d in tries[MAX_JOKERS:]:
        isoles.extend(par_dossier[d])
    # Les lignes : la racine d'abord, puis les notes, puis le reste.
    def rang(c):
        ext = c.rsplit(".", 1)[-1].lower() if "." in c.rsplit("/", 1)[-1] else ""
        return (0 if "/" not in c else 1 if ext in ("md", "txt", "rules", "csv", "tsv") else 2, c)
    isoles.sort(key=rang)
    statiques, laisses = isoles[:MAX_STATIQUES], isoles[MAX_STATIQUES:]
    # Garde-fou : aucune regle ne doit toucher un fichier publie.
    for d in jokers:
        if d in habites or any(p.startswith(d + "/") for p in publies):
            raise SystemExit("ERREUR _redirects : le joker /%s/* couvrirait un fichier publie" % d)
    for c in statiques:
        if c in publies:
            raise SystemExit("ERREUR _redirects : %s est publie" % c)
    return jokers, statiques, laisses


def ecrire_redirections(retenus):
    jokers, statiques, laisses = redirections(retenus)
    lignes = ["# Fichiers internes du depot -> l'accueil (publication/construire_site.py, ne pas modifier a la main)."]
    lignes += ["%s %s" % (_url(c), "/ 301") for c in statiques]
    lignes += ["%s/* / 301" % _url(d) for d in jokers]
    for l in lignes:
        if len(l) > 2000:
            raise SystemExit("ERREUR _redirects : ligne trop longue : %s..." % l[:80])
    with open(os.path.join(SORTIE, "_redirects"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lignes) + "\n")
    return jokers, statiques, laisses


def fichiers_du_depot():
    """Les fichiers suivis par git si possible (pas ce qui traine sur le disque)."""
    try:
        import subprocess
        sortie = subprocess.run(["git", "ls-files", "-z"], cwd=RACINE, capture_output=True, check=True).stdout
        return [p.decode("utf-8") for p in sortie.split(b"\0") if p]
    except Exception:
        liste = []
        for d, sous, fs in os.walk(RACINE):
            sous[:] = [s for s in sous if s not in (".git", "_site", "node_modules")]
            for f in fs:
                liste.append(os.path.relpath(os.path.join(d, f), RACINE).replace(os.sep, "/"))
        return liste


def publie(chemin):
    if chemin in FICHIERS_RACINE:
        return True
    if EXCLUS.search(chemin):
        return False
    ext = chemin.rsplit(".", 1)[-1].lower() if "." in chemin.rsplit("/", 1)[-1] else ""
    for prefixe, exts in DOSSIERS.items():
        if exts is None:
            if chemin == prefixe:
                return True
        elif chemin.startswith(prefixe) and ext in exts:
            return True
    return False


def construire():
    if os.path.isdir(SORTIE):
        shutil.rmtree(SORTIE)
    os.makedirs(SORTIE)
    retenus = [c for c in fichiers_du_depot() if publie(c) and os.path.isfile(os.path.join(RACINE, c))]
    for c in retenus:
        dest = os.path.join(SORTIE, c)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(os.path.join(RACINE, c), dest)
    with open(os.path.join(SORTIE, "404.html"), "w", encoding="utf-8") as f:
        f.write(PAGE_404)
    manquants = [c for c in FICHIERS_RACINE if not os.path.isfile(os.path.join(RACINE, c))]
    return retenus, manquants


# ---- --verifier : ce que le site cite mais n'a pas ----
REF = re.compile(r"""["'`(]([A-Za-z0-9_./${}-]+\.(?:json|js|html|webp|png|jpe?g|gif|svg|mp3|m4a|mp4|webm|css))[?"'`)#]""", re.I)


def verifier(retenus):
    """Un fichier du depot laisse DEHORS dont le nom paraît dans un fichier
    publie est suspect : le site le cite, il repondra 404. Pas une preuve (un
    commentaire cite des fichiers qui ne se chargent pas), un signal a lire."""
    publies = set(retenus)
    noms_publies = {c.rsplit("/", 1)[-1] for c in retenus}
    dehors = [c for c in fichiers_du_depot() if c not in publies]
    par_nom = {}
    for c in dehors:
        # Un nom dont une copie EST publiee (themes.json, index.html, les
        # scenes...) se resout presque toujours vers elle : seul le bruit.
        if c.rsplit("/", 1)[-1] in noms_publies:
            continue
        if re.search(r"\.(json|js|html|webp|png|jpe?g|gif|svg|mp3|m4a|mp4|webm|css)$", c, re.I):
            par_nom.setdefault(c.rsplit("/", 1)[-1], []).append(c)
    cites = {}
    for c in retenus:
        if not re.search(r"\.(html|js|css|json)$", c):
            continue
        try:
            texte = open(os.path.join(RACINE, c), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for m in REF.finditer(texte):
            nom = m.group(1).rsplit("/", 1)[-1]
            if nom in par_nom:
                cites.setdefault(nom, set()).add(c)
    return {nom: (par_nom[nom], sorted(qui)[:3]) for nom, qui in cites.items()}


def main():
    retenus, manquants = construire()
    taille = sum(os.path.getsize(os.path.join(SORTIE, c)) for c in retenus)
    print("_site : %d fichiers, %.1f Mo (+ 404.html, _redirects)" % (len(retenus), taille / 1e6))
    jokers, statiques, laisses = ecrire_redirections(retenus)
    print("_redirects : %d dossiers internes en joker (max %d), %d fichiers internes en lignes (max %d)%s"
          % (len(jokers), MAX_JOKERS, len(statiques), MAX_STATIQUES,
             (" ; %d laisses en 404 seulement (au-dela de la limite)" % len(laisses)) if laisses else ""))
    if manquants:
        print("ABSENTS du depot (liste a corriger) : " + ", ".join(manquants))
    if "--verifier" in sys.argv:
        par_dossier = {}
        for c in retenus:
            d = c.split("/")[0] if "/" in c else "(racine)"
            par_dossier[d] = par_dossier.get(d, 0) + 1
        print("\nPublie, par dossier :")
        for d in sorted(par_dossier):
            print("  %-14s %5d" % (d, par_dossier[d]))
        suspects = verifier(retenus)
        print("\nCites par le site mais laisses dehors (%d noms) :" % len(suspects))
        for nom in sorted(suspects):
            ou, qui = suspects[nom]
            print("  %-40s %s  <- %s" % (nom, ", ".join(ou[:2]) + (" ..." if len(ou) > 2 else ""), ", ".join(qui)))
    sys.exit(1 if manquants else 0)


if __name__ == "__main__":
    main()
