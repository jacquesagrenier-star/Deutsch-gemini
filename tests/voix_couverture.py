# -*- coding: utf-8 -*-
"""Tout ce que l'app dit en allemand a-t-il sa voix enregistree ?

    python tests/voix_couverture.py           # bilan, 15 textes au plus par groupe
    python tests/voix_couverture.py --tout    # chaque texte manquant

Sort en code 0 si tout est couvert, 1 si un texte demande par l'app est ABSENT
DU MANIFESTE (un defaut de code, a reparer dans audio/manifest.py), 2 si tout
est inventorie mais des mp3 restent A GENERER (attente de generation, pas un
defaut). Aucune dependance : la bibliotheque standard, et node pour les deux
listes que l'app fabrique par le code (comme audio/manifest.py).

POURQUOI CE CONTROLE EXISTE. L'app nomme un mp3 par l'empreinte du texte
qu'elle envoie a direAllemand() ; audio/manifest.py inventorie les textes a
generer. Quand les deux ne disent pas la meme chaine -- un prefixe ajoute a la
volee, une cle de themes.json que le manifeste ne lit pas, une donnee en dur
dans index.html -- il n'y a AUCUNE erreur nulle part : le fichier manque et
l'app retombe sur la voix du telephone. Le 12 octobre 2026, un audit a trouve
1 087 textes dans ce cas, ajoutes a l'app en quatre fois depuis la v407 sans
que le manifeste soit mis au courant. Ce script rejoue les formules DE L'APP
(chaque bloc cite sa ligne d'index.html ou de visuel/prototype/index.html) et
les compare au manifeste : un ajout qui parle sans etre inventorie se voit
ici, avant qu'un usager ne l'entende avec la voix du telephone.

⚠️ CE SCRIPT NE DOIT PAS LIRE LE MANIFESTE POUR SAVOIR QUOI DEMANDER. Sa
valeur tient a ce qu'il reecrit les formules depuis le code JS, pas depuis
manifest.py : deux copies de la meme formule se trompent ensemble. Et il ne
retire pas les espaces de bord sauf la ou le JS le fait (`.trim()`), parce que
l'app non plus : une donnee avec un espace de trop donne une autre empreinte.

TROIS ETATS, bien separes :
  - absent du manifeste      : manifest.py ne le produit pas -> defaut de code ;
  - manifest.json en retard  : manifest.py le produit, mais le fichier ecrit
                               ne l'a pas encore -> `python audio/manifest.py --ecrire` ;
  - mp3 pas encore genere    : inventorie, mais sans fichier dans audio/mp3/
                               -> generer.py, normaliser.py, deposer.py.
Les deux derniers ne se voient que si audio/manifest.json et audio/mp3/
existent (ils sont hors depot) ; ailleurs le script le dit et s'en tient au
premier etat.
"""
import collections
import hashlib
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import manifest  # noqa: E402  -- audio/manifest.py : recolter() ne fait que lire

TOUT = "--tout" in sys.argv
MAX_PAR_GROUPE = None if TOUT else 15

# TEXTES INVENTORIES MAIS SANS MP3, CONNUS ET ACCEPTES. Le filtre de contenu
# d'ElevenLabs refuse ces deux imperatifs (journal_refaire.txt, et le
# commentaire au-dessus de direAllemand) ; ils sortent a la voix du telephone
# et c'est assume. Un texte ajoute ici doit dire pourquoi.
EXCEPTIONS = {
    "Töte! Tötet! Töten Sie!": "refuse par le filtre de contenu ElevenLabs",
    "Ernähre dich! Ernährt euch! Ernähren Sie sich!": "refuse par le filtre de contenu ElevenLabs",
}
# ET CE QUI N'EST PAS DENOMBRABLE : « Mon vocabulaire » (mode monvocab) fait
# dire n'importe quel mot du dictionnaire WikDict, jusqu'a 5 000 par usager.
# Aurora ne parle que si le mot est aussi dans le cours ; le reste sort a la
# voix du telephone par construction. Rien a controler ici.


def charger(nom):
    with io.open(os.path.join(RACINE, nom), encoding="utf-8") as f:
        return json.load(f)


def empreinte(texte):
    # empreinteAudio() dans index.html, empreinte() dans le prototype des
    # scenes : sha1 du texte tel quel, 16 premiers hexadecimaux.
    return hashlib.sha1(texte.encode("utf-8")).hexdigest()[:16]


DEMANDES = collections.OrderedDict()   # groupe -> OrderedDict(texte -> None)


def demander(groupe, texte):
    """Un texte que l'app envoie a direAllemand() / dire(), tel quel."""
    if texte is None:
        return
    texte = str(texte)
    if not texte.strip():
        return
    DEMANDES.setdefault(groupe, collections.OrderedDict())[texte] = None


def js(valeur):
    """Ce qu'un gabarit JS `${x}` ecrit pour une valeur absente : « undefined ».
    On le reproduit expres, pour qu'une forme manquante se voie ici."""
    return "undefined" if valeur is None else str(valeur)


def textes_du_code(nom_script):
    """Une liste que l'app fabrique par le code, lue par node (tests/*.js)."""
    r = subprocess.run(["node", os.path.join(RACINE, "tests", nom_script)],
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        sys.exit("  tests/%s a echoue :\n%s" % (nom_script, r.stderr or ""))
    return [l for l in (r.stdout or "").split("\n") if l.strip()]


# ---------------------------------------------------------------- les demandes

# 1. LES NOMS (themes.json -> mots). La carte dit « der Mann » (texteCarteAPrononcer :
#    article + mot), la dictee dit « Mann » seul (speakDictationText), le second
#    haut-parleur dit « die » + pluriel (plurielDit = articlePluriel() + forme,
#    articlePluriel() rendant toujours "die " pour l'allemand), la chaine du verso
#    finit sur l'exemple (texteAudioExemple = card[5]).
themes = charger("themes.json")["themes"]
for th in themes:
    for m in th.get("mots") or []:
        mot = m.get("mot") or ""
        genre = m.get("genre") or ""
        demander("nomen.mot", mot)
        if genre:
            demander("nomen.article", genre + " " + mot)
        pluriel = (m.get("pluriel") or "").strip()
        if pluriel and pluriel not in ("—", "-"):
            demander("nomen.pluriel", "die " + pluriel)
        demander("nomen.exemple", m.get("exemple"))
    # 2. LES CHAPITRES VHS (themes.json -> verben / adjektive). Passes tels quels
    #    aux cartes Verbes (mode vhskapitelverben) et Adjectifs (vhskapiteladjektive) :
    #    memes boutons que verbe.json, l'adjectif en tableau [mot, fr, "", exemple, ...].
    for v in th.get("verben") or []:
        demander("kapitel.verben.infinitif", v.get("infinitif"))
        for cle in ("exemple", "perfekt", "praeteritum", "konjunktiv2"):
            demander("kapitel.verben." + cle, v.get(cle))
        imp = v.get("imperativ")
        if imp:
            demander("kapitel.verben.imperativ",
                     "%s %s %s" % (js(imp.get("du")), js(imp.get("ihr")), js(imp.get("sie_Sie"))))
    for a in th.get("adjektive") or []:
        demander("kapitel.adjektive.mot", a.get("mot"))
        demander("kapitel.adjektive.exemple", a.get("exemple"))

# 3. LES VERBES (verbe.json). Les quatre temps ont chacun leur bouton ; l'imperatif
#    est un gabarit JS : sentenceSpeakBtnHtml(`${imp.du} ${imp.ihr} ${imp.sie_Sie}`).
for niv, liste in charger("verbe.json").items():
    for v in liste:
        demander("verben.infinitif", v.get("infinitif"))
        for cle in ("exemple", "perfekt", "praeteritum", "konjunktiv2"):
            demander("verben." + cle, v.get(cle))
        imp = v.get("imperativ")
        if imp:
            demander("verben.imperativ",
                     "%s %s %s" % (js(imp.get("du")), js(imp.get("ihr")), js(imp.get("sie_Sie"))))

# 4. ADJECTIFS, ADVERBES, EXPRESSIONS : le mot et l'exemple. Et, pour l'adjectif,
#    LES DEGRES (v677) : reglerAudioPluriel(germanWord + ", " + card[15] + ", " + card[16]),
#    seulement quand comparatif ET superlatif existent.
for fichier, groupe in (("adjectif.json", "adjektive"), ("adverbe.json", "adverbien"),
                        ("redewendung.json", "redewendungen")):
    for niv, liste in charger(fichier).items():
        for x in liste:
            demander(groupe + ".mot", x.get("mot"))
            demander(groupe + ".exemple", x.get("exemple"))
            if groupe == "adjektive" and x.get("comparatif") and x.get("superlatif"):
                demander("adjektive.degres",
                         x.get("mot") + ", " + x["comparatif"] + ", " + x["superlatif"])

# 5. LES MOTS DE FONCTION (funktionswort.json) : mot et exemple, toutes sections.
for section, liste in charger("funktionswort.json").items():
    for x in liste:
        demander("funktionswort." + section + ".mot", x.get("mot"))
        demander("funktionswort." + section + ".exemple", x.get("exemple"))

# 6. L'EXAMEN (pruefung.json). Hoeren : dictationText = o.audio (sans trim).
#    Sprechen / Schreiben / Lesen construisent un audioDe que
#    phraseAllemandeDeLExercice() rend apres .trim().
pruefung = charger("pruefung.json")
for o in pruefung.get("hoeren") or []:
    demander("pruefung.hoeren", o.get("audio"))
for o in pruefung.get("sprechen") or []:
    if o.get("chunks"):
        demander("pruefung.sprechen", (js(o.get("frage")) + " " + " ".join(o["chunks"])).strip())
for o in pruefung.get("schreiben") or []:
    if o.get("chunks"):
        demander("pruefung.schreiben", " ".join(o["chunks"]).strip())
for o in pruefung.get("lesen") or []:
    if o.get("text"):
        demander("pruefung.lesen", str(o["text"]).strip())

# 7. LES EXERCICES DE GRAMMAIRE (exercices.json), formule de phraseAllemandeDeLExercice() :
#    audioDe d'abord, sinon les blocs joints, sinon l'enonce avec la bonne forme a la
#    place du blanc -- capitalisee si le blanc ouvre la phrase ET que l'enonce
#    contient . ? ! (enonceEstUnePhrase). Puis .trim().
for nom, liste in charger("exercices.json")["jeux"].items():
    for x in liste:
        if x.get("audioDe"):
            demander("exercices." + nom, str(x["audioDe"]).strip())
            continue
        if x.get("chunks"):
            demander("exercices." + nom, " ".join(x["chunks"]).strip())
            continue
        enonce = x.get("question") or ""
        if "___" not in enonce:
            continue
        bon = x.get("correct") or (x.get("answers") or [""])[0]
        if not bon:
            continue
        bon = str(bon)
        if enonce.index("___") == 0 and any(c in enonce for c in ".?!"):
            bon = bon[0].upper() + bon[1:]
        demander("exercices." + nom, enonce.replace("___", bon, 1).strip())

# 8. CE QUE L'APP FABRIQUE PAR LE CODE, lu dans index.html par node : les exercices
#    d'articles (audioDe de chaque exercice) et les verbes de position
#    (positionsverbenTheme : infinitif, exemple, perfekt, praeteritum).
for t in textes_du_code("phrases_articles.js"):
    demander("exercices.articles", t)
for t in textes_du_code("phrases_positionsverben.js"):
    demander("positionsverben", t)

# 9. LES SCENES (visuel/prototype/scene-*.js, le fichier que l'app charge ; pas la
#    variante .es.js). dire(p.genre + " " + p.mot) pour tout point touche ; en A1
#    « decouvrir », le prenom devant : dire((p.personne ? p.personne + ". " : "") +
#    p.genre + " " + p.mot) ; et dire(q.phrase) pour chaque question A2-C1.
proto = os.path.join(RACINE, "visuel", "prototype")
for f in sorted(os.listdir(proto)):
    if not (f.startswith("scene-") and f.endswith(".js")) or f.endswith(".es.js"):
        continue
    with io.open(os.path.join(proto, f), encoding="utf-8") as fh:
        src = fh.read()
    scene = json.loads(src[src.index("{"):].rstrip().rstrip(";"))
    for p in scene.get("points") or []:
        base = js(p.get("genre")) + " " + js(p.get("mot"))
        demander("scene.mot", base)
        if p.get("personne"):
            demander("scene.personne", p["personne"] + ". " + base)
    for niv, couche in (scene.get("couches") or {}).items():
        for q in couche.get("qs") or []:
            demander("scene.phrase", q.get("phrase"))

# 10. LA PRONONCIATION (prononciation.json) : direMotPron() dit e.mot de chaque exemple.
for g in charger("prononciation.json").get("groupes") or []:
    for regle in g.get("regles") or []:
        for e in regle.get("exemples") or []:
            demander("prononciation", e.get("mot"))
        for var in (regle.get("variantes") or {}).values():
            if isinstance(var, dict):
                for e in var.get("exemples") or []:
                    demander("prononciation", e.get("mot"))

# 11. LES FEUILLES DE CONJUGAISON (conjugaison.json, v867) : construireTableau()
# dit texteFormeTableau(l[0]) -- la forme, crochets retires (replace(/[\[\]]/g, "")).
for feuilles in (charger("conjugaison.json").get("niveaux") or {}).values():
    for f in feuilles:
        for l in f.get("l") or []:
            demander("conjugaison", str(l[0]).replace("[", "").replace("]", ""))

# ---------------------------------------------------------------- le manifeste

# Ce que manifest.py produit AUJOURD'HUI : la reference de l'etat « absent du
# manifeste ». S'arrete de lui-meme si node ou un script tests/*.js manque.
INVENTAIRE = {e["texte"] for e in manifest.dedoublonner(manifest.recolter())}

chemin_json = os.path.join(RACINE, "audio", "manifest.json")
ECRIT = None
if os.path.exists(chemin_json):
    ECRIT = {e["texte"] for e in charger("audio/manifest.json")}

dossier_mp3 = os.path.join(RACINE, "audio", "mp3")
MP3 = None
if os.path.isdir(dossier_mp3):
    MP3 = {f[:-4] for f in os.listdir(dossier_mp3) if f.endswith(".mp3")}

# ---------------------------------------------------------------- le bilan

absents = collections.OrderedDict()    # groupe -> [textes] : defaut de code
en_retard = collections.OrderedDict()  # groupe -> [textes] : --ecrire a relancer
a_generer = collections.OrderedDict()  # groupe -> [textes] : mp3 pas encore la
acceptes = []
deja_vus = set()
n_demandes = 0
for groupe, textes in DEMANDES.items():
    for t in textes:
        if t in deja_vus:
            continue
        deja_vus.add(t)
        n_demandes += 1
        if t not in INVENTAIRE:
            absents.setdefault(groupe, []).append(t)
        elif ECRIT is not None and t not in ECRIT:
            en_retard.setdefault(groupe, []).append(t)
        elif MP3 is not None and empreinte(t) not in MP3:
            if t in EXCEPTIONS:
                acceptes.append(t)
            else:
                a_generer.setdefault(groupe, []).append(t)


def montrer(titre, par_groupe):
    n = sum(len(v) for v in par_groupe.values())
    car = sum(len(t) for v in par_groupe.values() for t in v)
    print("%s : %d texte(s), %d caracteres" % (titre, n, car))
    for groupe, textes in par_groupe.items():
        print("  %-28s %5d" % (groupe, len(textes)))
        for t in textes[:MAX_PAR_GROUPE]:
            print("      " + t)
        if MAX_PAR_GROUPE is not None and len(textes) > MAX_PAR_GROUPE:
            print("      ... (%d de plus, --tout pour les voir)" % (len(textes) - MAX_PAR_GROUPE))
    return n, car


print("textes allemands demandes par l'app : %d uniques, dans %d groupes"
      % (n_demandes, len(DEMANDES)))
print("textes du manifeste (manifest.py)    : %d" % len(INVENTAIRE))
print()

code = 0
if absents:
    montrer("ABSENTS DU MANIFESTE (defaut de code : audio/manifest.py ne les voit pas)", absents)
    code = 1
else:
    print("absents du manifeste : aucun -- tout ce que l'app dit est inventorie.")
print()

if ECRIT is None:
    print("audio/manifest.json absent (hors depot) : le retard du fichier ecrit n'est pas verifiable ici.")
elif en_retard:
    montrer("MANIFEST.JSON EN RETARD (relancer : python audio/manifest.py --ecrire)", en_retard)
    code = code or 2
else:
    print("audio/manifest.json : a jour de manifest.py.")
print()

if MP3 is None:
    print("audio/mp3/ absent (hors depot) : les mp3 a generer ne sont pas verifiables ici.")
else:
    if a_generer:
        n, car = montrer("MP3 PAS ENCORE GENERES (inventories, attente de generation)", a_generer)
        # Meme bareme que manifest.py : un credit par caractere en Multilingual
        # v2, un demi en Flash.
        print("  a generer : %d textes, %d caracteres -> %d credits Flash, %d credits Multilingual v2"
              % (n, car, int(car * 0.5), car))
        code = code or 2
    else:
        print("mp3 : chaque texte inventorie a son fichier dans audio/mp3/.")
    if acceptes:
        print("  sans mp3 mais acceptes (%d) :" % len(acceptes))
        for t in acceptes:
            print("      %s  -- %s" % (t, EXCEPTIONS[t]))
    perdus = [t for t in EXCEPTIONS if t not in deja_vus]
    if perdus:
        print("  ⚠️ exceptions que l'app ne demande plus (a retirer de la liste) : %s" % perdus)
print()

if code == 0:
    print("tout est couvert.")
elif code == 1:
    print("DEFAUT : des textes demandes par l'app ne sont pas dans le manifeste.")
else:
    print("inventaire complet ; il reste des fichiers a produire.")
sys.exit(code)
