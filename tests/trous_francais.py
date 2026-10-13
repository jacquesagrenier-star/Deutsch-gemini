# -*- coding: utf-8 -*-
"""Du FRANCAIS recopie dans une langue cible, la ou une traduction est due.

    python tests/trous_francais.py                 # sort 0 si rien, 1 sinon
    python tests/trous_francais.py --detail        # chaque trou, un par ligne
    python tests/trous_francais.py --racine <dossier du depot>
    python tests/trous_francais.py --langues en,tr,uk,fa,pt,ar,pl,ru

CE QUE LES AUTRES CONTROLES NE VOIENT PAS. trous_langue.py et lot_exos.py
verifient qu'un champ traduit EXISTE et n'est pas vide. Ils ne lisent pas ce
qu'il contient. Le 12 octobre 2026, 130 exercices avaient dans TOUTES les
langues la question, les options et la bonne reponse recopiees du francais
(« Quel type de conjonction est « dass » ? » servi a un lecteur arabe), et
aucun controle ne le disait.

CE QU'IL CHERCHE, dans les dix fichiers de donnees et dans index.html :
  - identique_fr   le texte cible est exactement le francais, et ce francais
                   est reconnaissable comme du francais ;
  - partiel        une PHRASE du texte cible est une phrase francaise du
                   texte source (consigne francaise laissee derriere une
                   phrase allemande traduite a moitie) ;
  - identique_en   le texte cible (ni fr ni en) est exactement l'ANGLAIS --
                   meme defaut, autre langue recopiee ;
  - francais_libre une phrase francaise dans un champ cible, qui n'est pas
                   dans la source (francais arrive par un autre chemin).

CE QU'IL EXCLUT, et pourquoi -- les faux positifs ont ete regardes un par un :
  - un texte identique partout SANS marqueur francais : une phrase allemande
    (« Ich ___ nach Berlin. »), un nom propre, un nombre, un terme grammatical
    allemand (Akkusativ), un mot identique par nature (Taxi) ;
  - le score de francais exige au moins un MOT-OUTIL francais ou une elision
    (l', d', qu'...) : un simple accent ne suffit pas, l'allemand ecrit
    « Café » et le portugais « você » ;
  - les mots-outils ambigus sont ecartes de la liste : « des » (genitif
    allemand), « du » (tu, en allemand), « mais » (plus, en portugais),
    « ton » (Nuance/Ton), « son » et « ses » (turc : dernier, voix), « ne »
    (turc : quoi), « de », « a », « que », « la », « en » (portugais et
    espagnol), « par » (portugais : pair), « place », « position »,
    « question », « phrase », « article », « texte » (anglais ou allemand).

LA SOURCE EST LE FRANCAIS. Un champ n'est du que si sa version francaise
existe et n'est pas vide -- la meme regle que trous_langue.py.

DEUX CONVENTIONS DE SUFFIXE COEXISTENT (voir trous_langue.py) : « question_tr »
et « optionsTr ». Le francais est tantot le champ nu (« traduction »,
« question »), tantot suffixe (« exemple_fr », quand le champ nu est
l'allemand). Les textes d'interface d'index.html sont dans des blocs par
langue (I18N, I18N_ESPAGNOL, grammaire.json), les petites tables de libelles
sont des objets { fr: ..., en: ... }, les exercices d'articles sont des
tableaux POSITIONNELS dont le rang de chaque langue est lu dans le code qui
les consomme (construireExercicesArticles).

Aucune dependance. Le module est aussi importe par balayer.py et poser.py
(dossier trous-traduction) : ses fonctions d'enumeration portent la POSITION
de chaque texte, ce qui permet de reecrire un fichier sans toucher au reste.
"""
import argparse
import io
import json
import os
import re
import sys

LANGUES_CIBLES = ["en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]
LANGUES_CONNUES = ["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]
FICHIERS_JSON = ["exercices.json", "pruefung.json", "grammaire.json",
                 "themes.json", "verbe.json", "adjectif.json", "adverbe.json",
                 "redewendung.json", "funktionswort.json", "prononciation.json"]

# ---------------------------------------------------------------------------
# Reconnaitre du francais
# ---------------------------------------------------------------------------

# Mots-outils que SEUL le francais emploie, parmi les langues qui se croisent
# ici (allemand, anglais, turc, portugais, espagnol des exemples). Chaque mot
# ambigu retire de cette liste l'a ete apres un faux positif, voir l'en-tete.
MOTS_FR = """
le les une est sont pour avec dans qui quel quelle quels quelles où pas ce
cette ces sur tout toute tous toutes sans bien déjà encore ici vous nous je
il elle ils elles mon mes tes leur leurs au aux et comme après avant quand
pourquoi comment lequel laquelle lesquels chaque plusieurs aucun aucune
ordre mots mot verbe verbes réponse sujet cas nom temps forme lettre exemple
toujours jamais très aussi être avoir faire dire peut peux doit faut voir
regarde cherche trouve choisis mets remets complète conjugue écris lis écoute
oui merci bonjour parce donc alors puis entre vers chez
rien juste bouge connecteur conjonction famille dernier dernière première
seul seule autre autres celui celle ceux nouveau nouvelle petit petite bon
bonne mauvais mauvaise vrai faux fausse quelque quelques parmi selon sous
depuis pendant contre malgré ainsi soit voici voilà pourtant cependant
surtout souvent parfois beaucoup peu trop assez moins
""".split()
RE_MOTS_FR = re.compile(r"(?<![\w'’-])(%s)(?![\w'’-])" % "|".join(
    re.escape(m) for m in MOTS_FR), re.I)

# Elisions et tournures que ni l'allemand, ni l'anglais, ni le turc, ni le
# portugais ne produisent : deux points chacune.
RE_FORT_FR = re.compile(
    r"(?<![\w])[ldjncmst]['’](?=[a-zàâäéèêëîïôöùûüœ])"   # l'homme, d'abord, qu'il
    r"|(?<![\w])qu['’]"
    r"|\bc['’]est\b|\best-ce\b|\bn['’]est\b|\bil y a\b|\bde la\b|\bà la\b|\bà l['’]",
    re.I)
RE_ACCENTS_FR = re.compile(r"[èêàùœîâûëï]")
RE_BALISES = re.compile(r"<[^>]+>")

# L'anglais, pour reconnaitre un texte anglais recopie dans une autre langue.
MOTS_EN = """
the is are of to and in with this that after at end goes verb word words
which what where you your it its not does do here there sentence clause
""".split()
RE_MOTS_EN = re.compile(r"(?<![\w'’-])(%s)(?![\w'’-])" % "|".join(MOTS_EN), re.I)


def texte_nu(t):
    """Sans balises HTML ni espaces superflus."""
    return " ".join(RE_BALISES.sub(" ", t).split())


def score_francais(t):
    """0 = rien de francais. >= 2 = du francais reconnaissable."""
    t = texte_nu(t)
    if not t:
        return 0
    faibles = set(m.lower() for m in RE_MOTS_FR.findall(t))
    forts = len(RE_FORT_FR.findall(t))
    accents = 1 if RE_ACCENTS_FR.search(t) else 0
    if not faibles and not forts:
        return 0
    return len(faibles) + 2 * forts + accents


def est_francais(t):
    return score_francais(t) >= 2


def est_anglais(t):
    t = texte_nu(t)
    return len(set(m.lower() for m in RE_MOTS_EN.findall(t))) >= 2


RE_PHRASES = re.compile(r"(?<=[.!?…])\s+|<br\s*/?>|\n")


def phrases(t):
    return [p.strip() for p in RE_PHRASES.split(t) if p and p.strip()]


# ---------------------------------------------------------------------------
# JSON avec positions
# ---------------------------------------------------------------------------

class Noeud(object):
    """Une valeur JSON et sa place dans le texte : [debut, fin)."""
    __slots__ = ("valeur", "debut", "fin", "enfants", "cles")

    def __init__(self, valeur, debut, fin, enfants=None, cles=None):
        self.valeur = valeur      # python : str, int, float, bool, None, list, dict
        self.debut = debut
        self.fin = fin
        self.enfants = enfants    # list de Noeud (tableau) ou dict cle -> Noeud
        self.cles = cles          # dict cle -> (debut, fin) de la cle ecrite

    def __getitem__(self, k):
        return self.enfants[k]


RE_NOMBRE = re.compile(r"-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?")
RE_ESPACES = re.compile(r"[ \t\r\n]*")


def _chaine_json(s, i):
    """Lit une chaine JSON a partir du guillemet ouvrant. (valeur, fin)."""
    j = i + 1
    morceaux = []
    while True:
        c = s[j]
        if c == '"':
            return "".join(morceaux), j + 1
        if c == "\\":
            e = s[j + 1]
            if e == "u":
                code = int(s[j + 2:j + 6], 16)
                j += 6
                if 0xD800 <= code < 0xDC00 and s[j:j + 2] == "\\u":
                    bas = int(s[j + 2:j + 6], 16)
                    code = 0x10000 + ((code - 0xD800) << 10) + (bas - 0xDC00)
                    j += 6
                morceaux.append(chr(code))
            else:
                morceaux.append({"n": "\n", "t": "\t", "r": "\r", "b": "\b",
                                 "f": "\f", "/": "/", "\\": "\\", '"': '"'}[e])
                j += 2
        else:
            morceaux.append(c)
            j += 1


def lire_json_positions(s):
    """Analyse un texte JSON complet et renvoie l'arbre de Noeud."""
    def valeur(i):
        i = RE_ESPACES.match(s, i).end()
        c = s[i]
        if c == '"':
            v, fin = _chaine_json(s, i)
            return Noeud(v, i, fin)
        if c == "{":
            enfants, cles, pos = {}, {}, {}
            j = RE_ESPACES.match(s, i + 1).end()
            if s[j] == "}":
                return Noeud({}, i, j + 1, enfants, cles)
            while True:
                j = RE_ESPACES.match(s, j).end()
                k, fk = _chaine_json(s, j)
                cles[k] = (j, fk)
                j = RE_ESPACES.match(s, fk).end()
                assert s[j] == ":", "':' attendu a %d" % j
                n = valeur(j + 1)
                enfants[k] = n
                j = RE_ESPACES.match(s, n.fin).end()
                if s[j] == ",":
                    j += 1
                    continue
                assert s[j] == "}", "'}' attendu a %d" % j
                return Noeud({k: n.valeur for k, n in enfants.items()}, i, j + 1, enfants, cles)
        if c == "[":
            enfants = []
            j = RE_ESPACES.match(s, i + 1).end()
            if s[j] == "]":
                return Noeud([], i, j + 1, enfants)
            while True:
                n = valeur(j)
                enfants.append(n)
                j = RE_ESPACES.match(s, n.fin).end()
                if s[j] == ",":
                    j += 1
                    continue
                assert s[j] == "]", "']' attendu a %d" % j
                return Noeud([n.valeur for n in enfants], i, j + 1, enfants)
        for mot, v in (("true", True), ("false", False), ("null", None)):
            if s.startswith(mot, i):
                return Noeud(v, i, i + len(mot))
        m = RE_NOMBRE.match(s, i)
        assert m, "valeur JSON inattendue a %d : %r" % (i, s[i:i + 20])
        txt = m.group(0)
        return Noeud(float(txt) if ("." in txt or "e" in txt or "E" in txt) else int(txt), i, m.end())
    return valeur(0)


# ---------------------------------------------------------------------------
# Litteraux JavaScript avec positions (index.html)
# ---------------------------------------------------------------------------

RE_ESPACES_JS = re.compile(r"(?:\s|//[^\n]*|/\*.*?\*/)*", re.S)
RE_IDENT = re.compile(r"[A-Za-z_$][A-Za-z0-9_$]*")


def _chaine_js(s, i):
    """Lit une chaine JS ("", '' ou ``) a partir du delimiteur. (valeur, fin)."""
    q = s[i]
    j = i + 1
    morceaux = []
    while True:
        c = s[j]
        if c == q:
            return "".join(morceaux), j + 1
        if c == "\\":
            e = s[j + 1]
            if e == "u":
                if s[j + 2] == "{":
                    k = s.index("}", j + 3)
                    morceaux.append(chr(int(s[j + 3:k], 16)))
                    j = k + 1
                else:
                    morceaux.append(chr(int(s[j + 2:j + 6], 16)))
                    j += 6
            elif e == "x":
                morceaux.append(chr(int(s[j + 2:j + 4], 16)))
                j += 4
            elif e == "\n":
                j += 2
            else:
                morceaux.append({"n": "\n", "t": "\t", "r": "\r", "b": "\b",
                                 "f": "\f", "v": "\v", "0": "\0"}.get(e, e))
                j += 2
        else:
            morceaux.append(c)
            j += 1


def lire_js_positions(s, i):
    """Lit un litteral JS (objet, tableau, chaine, autre) a partir de s[i].

    Les valeurs qui ne sont ni objet, ni tableau, ni chaine (un appel, une
    expression ternaire, un identifiant) sont gardees en texte brut, jusqu'a
    la virgule ou la fermeture du conteneur, parentheses et chaines comprises.
    """
    def valeur(i):
        i = RE_ESPACES_JS.match(s, i).end()
        c = s[i]
        if c in "\"'`":
            v, fin = _chaine_js(s, i)
            return Noeud(v, i, fin)
        if c == "{":
            enfants, cles = {}, {}
            j = RE_ESPACES_JS.match(s, i + 1).end()
            if s[j] == "}":
                return Noeud({}, i, j + 1, enfants, cles)
            while True:
                j = RE_ESPACES_JS.match(s, j).end()
                if s[j] in "\"'":
                    k, fk = _chaine_js(s, j)
                else:
                    m = RE_IDENT.match(s, j)
                    assert m, "cle JS attendue a %d : %r" % (j, s[j:j + 30])
                    k, fk = m.group(0), m.end()
                cles[k] = (j, fk)
                j = RE_ESPACES_JS.match(s, fk).end()
                assert s[j] == ":", "':' attendu a %d : %r" % (j, s[j:j + 30])
                n = valeur(j + 1)
                enfants[k] = n
                j = RE_ESPACES_JS.match(s, n.fin).end()
                if s[j] == ",":
                    j += 1
                    j2 = RE_ESPACES_JS.match(s, j).end()
                    if s[j2] == "}":
                        j = j2
                    else:
                        continue
                assert s[j] == "}", "'}' attendu a %d : %r" % (j, s[j:j + 30])
                return Noeud({k: n.valeur for k, n in enfants.items()}, i, j + 1, enfants, cles)
        if c == "[":
            enfants = []
            j = RE_ESPACES_JS.match(s, i + 1).end()
            if s[j] == "]":
                return Noeud([], i, j + 1, enfants)
            while True:
                n = valeur(j)
                enfants.append(n)
                j = RE_ESPACES_JS.match(s, n.fin).end()
                if s[j] == ",":
                    j += 1
                    j2 = RE_ESPACES_JS.match(s, j).end()
                    if s[j2] == "]":
                        j = j2
                    else:
                        continue
                assert s[j] == "]", "']' attendu a %d : %r" % (j, s[j:j + 30])
                return Noeud([n.valeur for n in enfants], i, j + 1, enfants)
        # Expression quelconque : jusqu'a la virgule ou la fermeture, en
        # respectant parentheses, crochets, accolades et chaines.
        j, prof = i, 0
        while True:
            c = s[j]
            if c in "\"'`":
                _, j = _chaine_js(s, j)
                continue
            if c in "([{":
                prof += 1
            elif c in ")]}":
                if prof == 0:
                    break
                prof -= 1
            elif c in ",;" and prof == 0:
                break
            elif c == "\n" and prof == 0 and s[i:j].strip():
                # Fin de ligne sans virgule : fin d'une declaration `const`.
                break
            j += 1
        brut = s[i:j].rstrip()
        return Noeud(brut, i, i + len(brut))
    return valeur(i)


def chaine_js(texte):
    """Ecrit un litteral JS entre guillemets doubles, UTF-8 brut."""
    return '"' + texte.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r") + '"'


def chaine_json(texte):
    return json.dumps(texte, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Enumerer les champs traduits
# ---------------------------------------------------------------------------

class Champ(object):
    """Un texte cible et sa source francaise.

    fichier      nom du fichier
    identifiant  chemin lisible de l'objet (« jeux/konnektorenExercises/12 »)
    champ        nom de base (« question », « options[1] », « textes »)
    langue       langue cible
    texte        texte cible tel qu'ecrit
    fr           texte francais source
    en           texte anglais, s'il existe (pour identique_en)
    repere       l'allemand ou le francais qui identifie l'objet a l'oeil
    noeud        Noeud du texte cible (position), None si la cle manque
    conteneur    Noeud du dict qui porte le champ
    cle          cle du texte cible dans ce dict (« question_ar », « ar »)
    index        rang dans une liste d'options, sinon None
    """
    def __init__(self, **kw):
        self.__dict__.update(kw)


def suffixe_camel(lg):
    return lg[0].upper() + lg[1:]


def cle_cible(d, base, lg):
    """La cle ou vit (ou vivra) la langue lg pour cette base, selon la
    convention en vigueur DANS CE DICT : « base_lg » si une soeur a un suffixe
    souligne, « baseLg » si une soeur est en casse chameau."""
    souligne = base + "_" + lg
    chameau = base + suffixe_camel(lg)
    if souligne in d:
        return souligne
    if chameau in d:
        return chameau
    for autre in LANGUES_CONNUES:
        if autre != "fr" and (base + "_" + autre) in d:
            return souligne
    for autre in LANGUES_CONNUES:
        if autre != "fr" and (base + suffixe_camel(autre)) in d:
            return chameau
    return souligne


def _bases_du_dict(d):
    """[(base, cle_fr)] : les champs francais d'un dict, chaque base une fois."""
    out, vus = [], set()
    for k in d:
        if k.endswith("_fr") and isinstance(d[k], (str, list)):
            base = k[:-3]
            if base not in vus:
                vus.add(base)
                out.append((base, k))
    for k in d:
        if k in vus or k.endswith("_fr") or not isinstance(d[k], (str, list)):
            continue
        if k + "_fr" in d:
            continue
        soeurs = any((k + "_" + lg) in d or (k + suffixe_camel(lg)) in d
                     for lg in LANGUES_CONNUES if lg != "fr")
        if soeurs:
            vus.add(k)
            out.append((k, k))
    return out


def _est_dict_langues(d):
    return "fr" in d and isinstance(d["fr"], str) and any(
        lg in d and isinstance(d[lg], str) for lg in LANGUES_CONNUES if lg != "fr")


def _repere(d):
    for k in ("mot", "infinitif", "question", "frage", "id", "text", "audio", "typ", "teil"):
        v = d.get(k)
        if isinstance(v, str) and v:
            return v[:70]
    return ""


def enumerer_json(nom, racine_noeud, langues):
    """Chaque texte cible du fichier, avec sa source francaise."""
    def chemin_str(ch):
        return "/".join(str(x) for x in ch)

    def visiter(n, ch):
        if isinstance(n.valeur, dict):
            d = n.valeur
            if _est_dict_langues(d):
                for lg in langues:
                    if lg == "fr":
                        continue
                    cible = n.enfants.get(lg)
                    if cible is None or not isinstance(cible.valeur, str) or not cible.valeur:
                        continue
                    yield Champ(fichier=nom, identifiant=chemin_str(ch), champ="(langues)",
                                langue=lg, texte=cible.valeur, fr=d["fr"], en=d.get("en"),
                                repere="", noeud=cible, conteneur=n, cle=lg, index=None)
            else:
                for base, kfr in _bases_du_dict(d):
                    fr = d[kfr]
                    if not fr:
                        continue
                    en = d.get(cle_cible(d, base, "en"))
                    for lg in langues:
                        if lg == "fr":
                            continue
                        k = cle_cible(d, base, lg)
                        cible = n.enfants.get(k)
                        if cible is None or not cible.valeur:
                            continue
                        if isinstance(fr, list) and isinstance(cible.valeur, list):
                            for i, el in enumerate(cible.enfants):
                                if i >= len(fr) or not isinstance(el.valeur, str) or not isinstance(fr[i], str):
                                    continue
                                yield Champ(fichier=nom, identifiant=chemin_str(ch), champ="%s[%d]" % (base, i),
                                            langue=lg, texte=el.valeur, fr=fr[i],
                                            en=(en[i] if isinstance(en, list) and i < len(en) else None),
                                            repere=_repere(d), noeud=el, conteneur=n, cle=k, index=i)
                        elif isinstance(fr, str) and isinstance(cible.valeur, str):
                            yield Champ(fichier=nom, identifiant=chemin_str(ch), champ=base,
                                        langue=lg, texte=cible.valeur, fr=fr,
                                        en=(en if isinstance(en, str) else None),
                                        repere=_repere(d), noeud=cible, conteneur=n, cle=k, index=None)
            for k, enfant in n.enfants.items():
                for c in visiter(enfant, ch + [k]):
                    yield c
        elif isinstance(n.valeur, list):
            for i, enfant in enumerate(n.enfants):
                for c in visiter(enfant, ch + [i]):
                    yield c

    # grammaire.json : textes[langue][cle] -- un bloc par langue, comme I18N.
    if nom == "grammaire.json":
        textes = racine_noeud.enfants["textes"]
        fr = textes.enfants["fr"]
        for lg in langues:
            if lg == "fr" or lg not in textes.enfants:
                continue
            bloc = textes.enfants[lg]
            for k, cible in bloc.enfants.items():
                if k in fr.enfants and isinstance(cible.valeur, str) and cible.valeur and fr.enfants[k].valeur:
                    en = textes.enfants.get("en")
                    yield Champ(fichier=nom, identifiant=k, champ="textes", langue=lg,
                                texte=cible.valeur, fr=fr.enfants[k].valeur,
                                en=(en.enfants[k].valeur if en and k in en.enfants else None),
                                repere="", noeud=cible, conteneur=bloc, cle=k, index=None)
        return
    for c in visiter(racine_noeud, []):
        yield c


# --- index.html -------------------------------------------------------------

# Les tableaux positionnels d'index.html et le rang de chaque langue, lus dans
# construireExercicesArticles() et construireExercicesArticlesMix().
POSITIONNELS = {
    "ARTICLE_EXPLICATIONS": {"fr": 0, "en": 1, "tr": 2, "fa": 3, "pt": 4, "uk": 5, "ar": 6, "pl": 7},
    "ARTICLE_DECLENCHEURS": {"fr": 0, "en": 1, "tr": 2, "fa": 3, "pt": 4, "uk": 5, "ar": 6, "pl": 7},
}
RANGS_ARTICLES = {"fr": 2, "en": 3, "tr": 5, "fa": 6, "pt": 7, "uk": 8, "ar": 9, "pl": 10}
RANGS_ARTICLES_MIX = {"fr": 5, "en": 6, "tr": 8, "fa": 9, "pt": 10, "uk": 11, "ar": 12, "pl": 13}
RE_CONST = re.compile(r"^const ([A-Za-z_][A-Za-z0-9_]*) = ", re.M)
RE_FR_OBJET = re.compile(r"\bfr\s*:\s*[\"'`]")


def _blocs_langues(nom_const, s, langues, nom_fichier):
    m = re.search(r"^const %s = " % re.escape(nom_const), s, re.M)
    if not m:
        return
    racine = lire_js_positions(s, m.end())
    fr = racine.enfants.get("fr")
    if fr is None:
        return
    for lg in langues:
        if lg == "fr" or lg not in racine.enfants:
            continue
        bloc = racine.enfants[lg]
        en = racine.enfants.get("en")
        for k, cible in bloc.enfants.items():
            src = fr.enfants.get(k)
            if src is None or not isinstance(cible.valeur, str) or not isinstance(src.valeur, str):
                continue
            if not cible.valeur or not src.valeur:
                continue
            yield Champ(fichier=nom_fichier, identifiant="%s/%s" % (nom_const, k), champ="texte",
                        langue=lg, texte=cible.valeur, fr=src.valeur,
                        en=(en.enfants[k].valeur if en and k in en.enfants and isinstance(en.enfants[k].valeur, str) else None),
                        repere="", noeud=cible, conteneur=bloc, cle=k, index=None)


def enumerer_html(s, langues, nom_fichier="index.html"):
    """Les textes d'interface traduits d'index.html, avec leur position."""
    for c in _blocs_langues("I18N", s, langues, nom_fichier):
        yield c
    for c in _blocs_langues("I18N_ESPAGNOL", s, langues, nom_fichier):
        yield c

    # Les deux grands dictionnaires sont exclus du balayage des petites tables.
    exclure = []
    for nom_const in ("I18N", "I18N_ESPAGNOL"):
        m = re.search(r"^const %s = " % nom_const, s, re.M)
        if m:
            n = lire_js_positions(s, m.end())
            exclure.append((n.debut, n.fin))

    def dans_exclu(i):
        return any(a <= i < b for a, b in exclure)

    # Les petites tables { fr: "...", en: "...", tr: "..." } : l'accolade la
    # plus proche AVANT « fr: » sur la meme ligne ouvre l'objet.
    vus = set()
    for m in RE_FR_OBJET.finditer(s):
        if dans_exclu(m.start()):
            continue
        debut_ligne = s.rfind("\n", 0, m.start()) + 1
        acc = s.rfind("{", debut_ligne, m.start())
        if acc < 0 or acc in vus:
            continue
        try:
            n = lire_js_positions(s, acc)
        except (AssertionError, IndexError, ValueError):
            continue
        if not isinstance(n.valeur, dict) or not _est_dict_langues(n.valeur):
            continue
        vus.add(acc)
        ligne = s.count("\n", 0, acc) + 1
        for lg in langues:
            if lg == "fr" or lg not in n.enfants:
                continue
            cible = n.enfants[lg]
            if not isinstance(cible.valeur, str) or not cible.valeur:
                continue
            yield Champ(fichier=nom_fichier, identifiant="objet@%d" % ligne, champ="(langues)",
                        langue=lg, texte=cible.valeur, fr=n.valeur["fr"], en=n.valeur.get("en"),
                        repere=n.valeur["fr"][:60], noeud=cible, conteneur=n, cle=lg, index=None)

    # Les tableaux positionnels des exercices d'articles.
    for m in RE_CONST.finditer(s):
        nom_const = m.group(1)
        rangs = None
        if nom_const in POSITIONNELS:
            rangs = POSITIONNELS[nom_const]
        elif nom_const == "ARTICLES_MIX":
            rangs = RANGS_ARTICLES_MIX
        elif nom_const.startswith("ARTICLES_"):
            rangs = RANGS_ARTICLES
        if rangs is None:
            continue
        racine = lire_js_positions(s, m.end())
        if racine.enfants is None:
            continue
        lignes = racine.enfants.items() if isinstance(racine.valeur, dict) else enumerate(racine.enfants)
        for k, rangee in lignes:
            if not isinstance(rangee.valeur, list) or len(rangee.enfants) <= rangs["fr"]:
                continue
            fr = rangee.enfants[rangs["fr"]].valeur
            if not isinstance(fr, str) or not fr:
                continue
            en_n = rangee.enfants[rangs["en"]] if len(rangee.enfants) > rangs["en"] else None
            for lg in langues:
                if lg == "fr" or lg not in rangs or len(rangee.enfants) <= rangs[lg]:
                    continue
                cible = rangee.enfants[rangs[lg]]
                if not isinstance(cible.valeur, str) or not cible.valeur:
                    continue
                yield Champ(fichier=nom_fichier, identifiant="%s/%s" % (nom_const, k), champ="rang",
                            langue=lg, texte=cible.valeur, fr=fr,
                            en=(en_n.valeur if en_n is not None and isinstance(en_n.valeur, str) else None),
                            repere=rangee.enfants[0].valeur if isinstance(rangee.enfants[0].valeur, str) else "",
                            noeud=cible, conteneur=rangee, cle=rangs[lg], index=rangs[lg])

    # Les constantes paralleles : NOM, NOM_EN, NOM_TR... (listes d'options).
    consts = {m.group(1): m.end() for m in RE_CONST.finditer(s)}
    for nom_const, pos in consts.items():
        for lg in langues:
            if lg == "fr":
                continue
            suffixe = "_" + lg.upper()
            if not nom_const.endswith(suffixe):
                continue
            base = nom_const[:-len(suffixe)]
            if base not in consts:
                continue
            src = lire_js_positions(s, consts[base])
            cible = lire_js_positions(s, pos)
            en_n = lire_js_positions(s, consts[base + "_EN"]) if (base + "_EN") in consts else None
            if isinstance(src.valeur, str) and isinstance(cible.valeur, str):
                yield Champ(fichier=nom_fichier, identifiant="const/%s" % base, champ="valeur",
                            langue=lg, texte=cible.valeur, fr=src.valeur,
                            en=(en_n.valeur if en_n is not None and isinstance(en_n.valeur, str) else None),
                            repere=base, noeud=cible, conteneur=None, cle=nom_const, index=None)
            elif isinstance(src.valeur, list) and isinstance(cible.valeur, list):
                for i, el in enumerate(cible.enfants):
                    if i >= len(src.enfants) or not isinstance(el.valeur, str) or not isinstance(src.enfants[i].valeur, str):
                        continue
                    yield Champ(fichier=nom_fichier, identifiant="const/%s" % base, champ="valeur[%d]" % i,
                                langue=lg, texte=el.valeur, fr=src.enfants[i].valeur,
                                en=(en_n.enfants[i].valeur if en_n is not None and isinstance(en_n.valeur, list) and i < len(en_n.enfants) else None),
                                repere=base, noeud=el, conteneur=cible, cle=nom_const, index=i)


# ---------------------------------------------------------------------------
# Juger
# ---------------------------------------------------------------------------

def normaliser(t):
    return " ".join(t.split()).strip().lower()


def juger(c):
    """(type, detail) si le champ est un trou, sinon (None, raison_exclusion)."""
    cible, fr = c.texte, c.fr
    if normaliser(cible) == normaliser(fr):
        if est_francais(fr):
            return "identique_fr", fr
        return None, "identique sans marqueur francais"
    if c.langue != "en" and c.en and normaliser(cible) == normaliser(c.en) \
            and normaliser(c.en) != normaliser(fr) and est_anglais(c.en):
        return "identique_en", c.en
    # Une phrase francaise du texte source laissee dans la cible.
    phr_fr = set(normaliser(p) for p in phrases(fr) if len(p) >= 12)
    for p in phrases(cible):
        pn = normaliser(p)
        if len(p) >= 12 and pn in phr_fr and est_francais(p):
            return "partiel", p
    # Une phrase francaise qui n'est pas dans la source.
    for p in phrases(cible):
        if len(p) >= 15 and score_francais(p) >= 4 and normaliser(p) not in phr_fr:
            return "francais_libre", p
    return None, ""


def balayer(racine, langues=None, fichiers=None):
    """[(Champ, type, detail)] pour tout le depot, et le compte des exclus."""
    langues = langues or LANGUES_CIBLES
    fichiers = fichiers or FICHIERS_JSON + ["index.html"]
    trous, exclus = [], {}
    for nom in fichiers:
        chemin = os.path.join(racine, nom)
        if not os.path.exists(chemin):
            continue
        with io.open(chemin, encoding="utf-8", newline="") as f:
            s = f.read()
        if nom.endswith(".json"):
            champs = enumerer_json(nom, lire_json_positions(s), langues)
        else:
            champs = enumerer_html(s, langues, nom)
        for c in champs:
            genre, detail = juger(c)
            if genre:
                trous.append((c, genre, detail))
            elif detail:
                exclus[(nom, detail)] = exclus.get((nom, detail), 0) + 1
    return trous, exclus


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser()
    p.add_argument("--racine", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    p.add_argument("--langues", default=",".join(LANGUES_CIBLES))
    p.add_argument("--detail", action="store_true")
    a = p.parse_args()
    langues = [l.strip() for l in a.langues.split(",") if l.strip()]
    trous, exclus = balayer(a.racine, langues)
    if not trous:
        print("  aucun texte francais recopie dans une langue cible (%s)" % ", ".join(langues))
        return 0
    par_fichier = {}
    for c, genre, detail in trous:
        par_fichier.setdefault(c.fichier, {}).setdefault(c.langue, 0)
        par_fichier[c.fichier][c.langue] += 1
    print("  %d texte(s) francais (ou anglais) recopie(s) dans une langue cible\n" % len(trous))
    for f in sorted(par_fichier):
        print("  %-20s %s" % (f, "  ".join("%s:%d" % (lg, n) for lg, n in sorted(par_fichier[f].items()))))
    if a.detail:
        print()
        for c, genre, detail in trous:
            print("  %-16s %-14s %-40s %-12s %s  %s" % (c.fichier, genre, c.identifiant[:40], c.champ + "/" + c.langue, (c.repere or "")[:30], detail[:70]))
    return 1


if __name__ == "__main__":
    sys.exit(main())
