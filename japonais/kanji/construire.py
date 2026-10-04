#!/usr/bin/env python3
"""Pilote des mnémotechniques kanji N5 : refait les champs dérivés des données.

    python japonais/kanji/construire.py                 # construit et vérifie
    python japonais/kanji/construire.py --donnees F.json  # écrit seulement les
                                                          # données dérivées (pour écrire les textes)
    python japonais/kanji/construire.py --kanjivg DOSSIER # copie locale de KanjiVG

Entrées (rien n'est tiré de la mémoire de qui que ce soit) :
  ../kanji.json                  KANJIDIC2 + niveaux Tanos (branche japonais-donnees)
  ../mots.json                   listes de vocabulaire JLPT de Waller
  KanjiVG (git clone)            groupes kvg:element de chaque SVG
  textes/textes_n5.json         les textes écrits à la main (sens retenus, mnémotechniques, confiance)
  textes/noms_composants.json   le nom français / anglais de chaque composant
  textes/a_relire.json          les 20 kanji de la page de relecture

Sorties : mnemoniques_n5.json, composants.json, a-relire.html.
Bibliothèque standard seulement. Code de sortie 1 si une vérification échoue.
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter, OrderedDict

ICI = os.path.dirname(os.path.abspath(__file__))
JAPONAIS = os.path.dirname(ICI)
SOURCES = os.path.join(ICI, "textes")
KVG_DEPOT = "https://github.com/KanjiVG/kanjivg.git"
NS = "{http://kanjivg.tagaini.net}"
NIVEAU = "N5"


# ---------------------------------------------------------------- kana, romaji

def hira(s):
    """Katakana → hiragana (le reste inchangé)."""
    return "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)


ROMAJI = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "を": "o", "ん": "n",
}
YOON = {"ゃ": "a", "ゅ": "u", "ょ": "o"}


def romaji(kana):
    """Hepburn modifié : voyelles longues ō / ū, っ double la consonne."""
    k = hira(kana)
    syl = []
    i = 0
    while i < len(k):
        c = k[i]
        if i + 1 < len(k) and k[i + 1] in YOON and c in ROMAJI:
            base = ROMAJI[c]
            if base in ("shi", "chi", "ji"):
                syl.append(base[:-1] + YOON[k[i + 1]])
            else:
                syl.append(base[:-1] + "y" + YOON[k[i + 1]])
            i += 2
            continue
        if c == "っ":
            syl.append("っ")
        elif c in ROMAJI:
            syl.append(ROMAJI[c])
        else:
            raise ValueError("kana inconnu pour le romaji : %r dans %r" % (c, kana))
        i += 1
    out = ""
    for j, s in enumerate(syl):
        if s == "っ":
            nxt = syl[j + 1] if j + 1 < len(syl) else ""
            out += "t" if nxt.startswith("ch") else nxt[:1]
        elif s == "n" and j + 1 < len(syl) and syl[j + 1][:1] in "aiueoy":
            out += "n'"
        else:
            out += s
    for long_, court in (("ou", "ō"), ("oo", "ō"), ("uu", "ū")):
        out = out.replace(long_, court)
    return out


# ---------------------------------------------------- lectures et alignement

DAKUTEN = dict(zip("かきくけこさしすせそたちつてとはひふへほ", "がぎぐげござじずぜぞだぢづでどばびぶべぼ"))
HANDAKUTEN = dict(zip("はひふへほ", "ぱぴぷぺぽ"))
DAKUTEN["ち"] = "じ"
DAKUTEN["つ"] = "ず"


def lectures_de(entree):
    """Lectures KANJIDIC d'un kanji : liste de (type, forme KANJIDIC, radical en hiragana, clé).

    La clé regroupe ce qu'on retient : on → la lecture on ; kun → le radical
    sans okurigana, et みっ (みっ.つ) se range sous み quand み existe aussi.
    """
    out = []
    for r in entree.get("lectures_on", []):
        out.append(("on", r, hira(r), ("on", r)))
    radicaux = {r.replace("-", "").split(".")[0] for r in entree.get("lectures_kun", [])}
    for r in entree.get("lectures_kun", []):
        radical = r.replace("-", "").split(".")[0]
        if not radical:
            continue
        cle = radical[:-1] if radical.endswith("っ") and radical[:-1] in radicaux else radical
        out.append(("kun", r, radical, ("kun", cle)))
    return out


def surfaces(radical):
    """Formes que prend une lecture dans un mot, avec leur coût (0 = telle quelle)."""
    yield radical, 0, ""
    if radical[0] in DAKUTEN:
        yield DAKUTEN[radical[0]] + radical[1:], 1, "rendaku"
    if radical[0] in HANDAKUTEN:
        yield HANDAKUTEN[radical[0]] + radical[1:], 1, "handakuten"
    if len(radical) > 1 and radical[-1] in "つちくき":
        yield radical[:-1] + "っ", 1, "gémination"
        if radical[0] in DAKUTEN:
            yield DAKUTEN[radical[0]] + radical[1:-1] + "っ", 2, "rendaku+gémination"
        if radical[0] in HANDAKUTEN:
            yield HANDAKUTEN[radical[0]] + radical[1:-1] + "っ", 2, "handakuten+gémination"


def est_kana(c):
    return "ぁ" <= c <= "ゖ" or "ァ" <= c <= "ヺ" or c == "ー"


def aligner(graphie, kana, index_kanji):
    """Toutes les découpes de `kana` sur `graphie`, au coût minimal.

    Chaque kanji doit prendre une de ses lectures KANJIDIC (ou une variante
    régulière : rendaku, gémination). Renvoie (coût, [découpes]) ; une découpe
    est une liste de (kanji, clé de lecture, forme KANJIDIC, surface, variante).
    Aucune découpe : lecture spéciale (jukujikun, ateji) ou kanji inconnu.
    """
    kana = hira(kana)
    resultats = []

    def rec(i, j, cout, chemin, precedent):
        if i == len(graphie):
            if j == len(kana):
                resultats.append((cout, list(chemin)))
            return
        c = graphie[i]
        if est_kana(c):
            if j < len(kana) and hira(c) == kana[j]:
                rec(i + 1, j + 1, cout, chemin, None)
            return
        cible = precedent if c == "々" else c
        entree = index_kanji.get(cible)
        if entree is None:
            return
        for type_, forme, radical, cle in lectures_de(entree):
            for surf, cout_v, variante in surfaces(radical):
                if kana.startswith(surf, j):
                    chemin.append((c, cle, forme, surf, variante))
                    rec(i + 1, j + len(surf), cout + cout_v, chemin, cible)
                    chemin.pop()

    rec(0, 0, 0, [], None)
    if not resultats:
        return None, []
    meilleur = min(c for c, _ in resultats)
    vues, uniques = set(), []
    for c, d in resultats:
        if c == meilleur and tuple(d) not in vues:
            vues.add(tuple(d))
            uniques.append(d)
    return meilleur, uniques


def changements_de_type(decoupe):
    """Nombre de passages on ↔ kun dans un mot : 天気 se lit plutôt tout on."""
    types = [d[1][0] for d in decoupe]
    return sum(1 for a, b in zip(types, types[1:]) if a != b)


# ------------------------------------------------------------------ KanjiVG

def kanjivg_dossier(chemin):
    if chemin:
        return chemin
    chemin = os.environ.get("KANJIVG") or os.path.join(os.path.expanduser("~"), ".cache", "kanjivg")
    if not os.path.isdir(os.path.join(chemin, "kanji")):
        print("Clonage de KanjiVG dans", chemin)
        subprocess.run(["git", "clone", "--depth", "1", KVG_DEPOT, chemin], check=True)
    return chemin


def kanjivg_version(dossier):
    try:
        return subprocess.run(["git", "-C", dossier, "log", "-1", "--format=%H %cs"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "inconnue"


def composants_kanjivg(dossier, kanji):
    """Décomposition KanjiVG d'un kanji.

    composants : les premiers groupes portant kvg:element sous la racine (les
      morceaux kvg:part d'un même élément sont réunis) ;
    sous_composants : tous les éléments plus profonds ;
    traits_libres : traits que KanjiVG ne range dans aucun élément nommé.
    """
    fichier = os.path.join(dossier, "kanji", "%05x.svg" % ord(kanji))
    if not os.path.exists(fichier):
        return None
    arbre = ET.parse(fichier)
    racine = next(g for g in arbre.iter() if g.get("id") == "kvg:%05x" % ord(kanji))
    total = sum(1 for e in racine.iter() if e.tag.endswith("path"))

    premiers, profonds = [], []
    couverts = [0]

    def descendre(g, niveau_trouve):
        for enfant in g:
            if not enfant.tag.endswith("g"):
                continue
            el = enfant.get(NS + "element")
            if el and not niveau_trouve:
                info = OrderedDict(element=el)
                if enfant.get(NS + "original"):
                    info["forme_de"] = enfant.get(NS + "original")
                if not any(p["element"] == el for p in premiers):
                    premiers.append(info)
                couverts[0] += sum(1 for e in enfant.iter() if e.tag.endswith("path"))
                descendre(enfant, True)
            else:
                if el and el not in profonds:
                    profonds.append(el)
                descendre(enfant, niveau_trouve)

    descendre(racine, False)
    return OrderedDict(
        composants=premiers,
        sous_composants=[e for e in profonds if not any(p["element"] == e for p in premiers)],
        traits=total,
        traits_libres=total - couverts[0] if premiers else 0,
    )


# ------------------------------------------------------------- dérivation

def charger(nom):
    with open(nom, encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=OrderedDict)


def deriver(dossier_kvg):
    kanji_json = charger(os.path.join(JAPONAIS, "kanji.json"))
    mots_json = charger(os.path.join(JAPONAIS, "mots.json"))
    index_kanji = {}
    for niveau, liste in kanji_json["niveaux"].items():
        for e in liste:
            index_kanji[e["kanji"]] = e
    tous_mots = [m for liste in mots_json["niveaux"].values() for m in liste]
    mots_n5 = mots_json["niveaux"][NIVEAU]

    # Alignement de chaque mot (une fois).
    alignements = {}
    for m in tous_mots:
        if m["kanji"]:
            alignements[(m["kanji"], m["kana"])] = aligner(m["kanji"], m["kana"], index_kanji)

    def lecture_dans(mot, kanji):
        """Lectures prises par `kanji` dans `mot` (une par occurrence), ou un échec.

        Entre découpes de même coût, on préfère celle qui change le moins de
        type de lecture (元気 : ゲン on + キ on plutôt que キ kun, KANJIDIC
        donnant き dans les deux listes). Si un doute subsiste, le mot est écarté.
        """
        cout, decoupes = alignements[(mot["kanji"], mot["kana"])]
        if not decoupes:
            return "spéciale", None
        moins = min(changements_de_type(d) for d in decoupes)
        decoupes = [d for d in decoupes if changements_de_type(d) == moins]
        lectures = set()
        for d in decoupes:
            lectures.add(tuple((cle, surf, variante) for (c, cle, forme, surf, variante) in d if c == kanji))
        if len({tuple(x[0] for x in l) for l in lectures}) != 1:
            return "ambiguë", sorted({x[0] for l in lectures for x in l})
        return "ok", sorted(lectures)[0]

    sortie = OrderedDict()
    for e in kanji_json["niveaux"][NIVEAU]:
        k = e["kanji"]
        n5 = [m for m in mots_n5 if m["kanji"] and k in m["kanji"]]
        comptes, mots_par_lecture, ecartes = Counter(), {}, []
        for m in n5:
            statut, val = lecture_dans(m, k)
            if statut == "ok":
                for cle, surf, variante in dict(((x[0], x) for x in val)).values():
                    comptes[cle] += 1
                    mots_par_lecture.setdefault(cle, []).append(
                        OrderedDict(mot=m["kanji"], kana=m["kana"], sens_en=m["tanos"]["champs"]["waller_definition"],
                                    surface=surf, variante=variante or None))
            else:
                ecartes.append(OrderedDict(mot=m["kanji"], kana=m["kana"], sens_en=m["tanos"]["champs"]["waller_definition"],
                                           raison=statut, lectures_possibles=[list(x) for x in val] if val else None))
        # Départage, et repli quand aucun mot N5 ne s'aligne : tous les niveaux.
        tous = Counter()
        for m in tous_mots:
            if m["kanji"] and k in m["kanji"]:
                statut, val = lecture_dans(m, k)
                if statut == "ok":
                    for cle in {x[0] for x in val}:
                        tous[cle] += 1
        base = comptes if comptes else tous
        classement = sorted(base, key=lambda c: (-comptes[c], -tous[c], c))
        retenue = classement[0] if classement else None
        egalite = len(classement) > 1 and base[classement[0]] == base[classement[1]]
        kvg = composants_kanjivg(dossier_kvg, k)
        sortie[k] = OrderedDict(
            kanji=k,
            sens_fr_candidats=e["sens_fr"],
            sens_en_candidats=e["sens_en"],
            lectures_on=e["lectures_on"],
            lectures_kun=e["lectures_kun"],
            traits=e["traits"][0] if e["traits"] else None,
            mots_n5=len(n5),
            comptes_lecture=[OrderedDict(type=c[0], lecture=c[1], romaji=romaji(c[1]), mots_n5=comptes[c],
                                         tous_niveaux=tous[c]) for c in classement],
            lecture_derivee=None if retenue is None else OrderedDict(
                type=retenue[0], kana=retenue[1], romaji=romaji(retenue[1]), mots_n5=comptes[retenue],
                egalite=egalite, comptee_sur="N5" if comptes else "tous niveaux (aucun mot N5 aligné)"),
            mots_par_lecture={"%s:%s" % c: v for c, v in mots_par_lecture.items()},
            mots_non_alignes=ecartes,
            kanjivg=kvg,
        )
    return sortie, kanji_json["meta"], mots_json["meta"]


# --------------------------------------------------------------- construction

def gras(texte):
    """**x** → <strong>x</strong>, le reste échappé."""
    morceaux = re.split(r"\*\*(.+?)\*\*", texte)
    return "".join(html.escape(m) if i % 2 == 0 else "<strong>%s</strong>" % html.escape(m)
                   for i, m in enumerate(morceaux))


def contient_mot(texte, mot):
    t = texte.replace("**", "").lower()
    return re.search(r"(?<![\w-])" + re.escape(mot.lower()) + r"(?![\w-])", t) is not None


def construire(dossier_kvg):
    derive, meta_k, meta_m = deriver(dossier_kvg)
    textes = charger(os.path.join(SOURCES, "textes_n5.json"))
    noms = charger(os.path.join(SOURCES, "noms_composants.json"))
    selection = charger(os.path.join(SOURCES, "a_relire.json"))
    erreurs, avis = [], []

    entrees = []
    utilises = OrderedDict()
    peu = []
    for k, d in derive.items():
        t = textes.get(k)
        if t is None:
            erreurs.append("%s : aucun texte dans textes/textes_n5.json" % k)
            continue
        # Lecture : celle des données, sauf dérogation écrite et justifiée.
        lect = d["lecture_derivee"]
        if t.get("lecture_derogation"):
            der = t["lecture_derogation"]
            trouve = [c for c in d["comptes_lecture"] if c["lecture"] == der["kana"] and c["type"] == der["type"]]
            if not trouve:
                erreurs.append("%s : dérogation vers %s absente des comptes" % (k, der["kana"]))
                continue
            c = trouve[0]
            lect = OrderedDict(type=c["type"], kana=c["lecture"], romaji=c["romaji"], mots_n5=c["mots_n5"],
                               egalite=False, derogation=der["raison"])
        if lect is None:
            erreurs.append("%s : aucune lecture alignée dans les mots N5" % k)
            continue
        cle = "%s:%s" % (lect["type"], lect["kana"])
        mots_lect = d["mots_par_lecture"].get(cle, [])

        # Sens retenus : un des candidats KANJIDIC, mot pour mot.
        if t["sens_fr"] not in d["sens_fr_candidats"]:
            erreurs.append("%s : sens_fr « %s » absent de KANJIDIC %s" % (k, t["sens_fr"], d["sens_fr_candidats"]))
        if t["sens_en"] not in d["sens_en_candidats"]:
            erreurs.append("%s : sens_en « %s » absent de KANJIDIC %s" % (k, t["sens_en"], d["sens_en_candidats"]))

        # Les mnémotechniques citent le sens et le romaji, et ont un morceau en gras.
        for langue in ("fr", "en"):
            txt = t["mnemo_" + langue]
            if not contient_mot(txt, t["sens_" + langue]):
                erreurs.append("%s : mnemo_%s ne cite pas le sens « %s »" % (k, langue, t["sens_" + langue]))
            if "(%s)" % lect["romaji"] not in txt:
                erreurs.append("%s : mnemo_%s ne cite pas la lecture « (%s) »" % (k, langue, lect["romaji"]))
            if "**" not in txt:
                erreurs.append("%s : mnemo_%s sans morceau en gras" % (k, langue))

        # Composants : ceux de KanjiVG, sous leur nom du lexique.
        kvg = d["kanjivg"]
        if kvg is None:
            erreurs.append("%s : absent de KanjiVG" % k)
            continue
        permis = [c["element"] for c in kvg["composants"]] + kvg["sous_composants"]
        if not kvg["composants"]:
            permis.append(k)
        noms_cites = []
        for el in t["composants_cites"]:
            if el not in permis:
                erreurs.append("%s : composant %s absent de sa décomposition KanjiVG %s" % (k, el, permis))
                continue
            if el not in noms:
                erreurs.append("%s : composant %s sans nom dans noms_composants.json" % (k, el))
                continue
            for langue in ("fr", "en"):
                if not contient_mot(t["mnemo_" + langue], noms[el][langue]):
                    erreurs.append("%s : mnemo_%s ne nomme pas %s « %s »" % (k, langue, el, noms[el][langue]))
            noms_cites.append(OrderedDict(element=el, fr=noms[el]["fr"], en=noms[el]["en"]))
            utilises.setdefault(el, []).append(k)
        if t["confiance"] not in ("haute", "moyenne", "basse"):
            erreurs.append("%s : confiance « %s »" % (k, t["confiance"]))

        # Exemples : deux mots N5 qui ont la lecture retenue ; à défaut, des
        # mots N5 qui contiennent le kanji sous une lecture spéciale (signalés).
        if t.get("exemples"):
            exemples = [m for m in mots_lect if m["mot"] in t["exemples"]]
            if len(exemples) != len(t["exemples"]):
                erreurs.append("%s : exemples %s pas tous dans les mots N5 en %s" % (k, t["exemples"], cle))
        else:
            exemples, vus = [], set()
            for m in sorted(mots_lect, key=lambda m: (m["variante"] is not None, len(m["mot"]))):
                if m["mot"] not in vus:
                    vus.add(m["mot"])
                    exemples.append(m)
            exemples = exemples[:2]
        exemples = [OrderedDict(mot=m["mot"], kana=m["kana"], romaji=romaji(m["kana"]), sens_en=m["sens_en"])
                    for m in exemples]
        if len(exemples) < 2:
            # Pas assez de mots N5 sous la lecture retenue : on complète avec
            # d'autres mots N5 du kanji, en disant sous quelle lecture.
            vus = {m["mot"] for m in exemples}
            autres = [(c, m) for c, ms in d["mots_par_lecture"].items() if c != cle for m in ms]
            autres.sort(key=lambda x: (x[1]["variante"] is not None, len(x[1]["mot"])))
            for c, m in autres:
                if len(exemples) < 2 and m["mot"] not in vus:
                    vus.add(m["mot"])
                    exemples.append(OrderedDict(mot=m["mot"], kana=m["kana"], romaji=romaji(m["kana"]),
                                                sens_en=m["sens_en"], autre_lecture=c.split(":")[1]))
            for m in d["mots_non_alignes"]:
                if len(exemples) < 2 and m["mot"] not in vus:
                    vus.add(m["mot"])
                    exemples.append(OrderedDict(mot=m["mot"], kana=m["kana"], romaji=romaji(m["kana"]),
                                                sens_en=m["sens_en"], lecture_speciale=True))
            peu.append(k)

        fragile = []
        if lect.get("egalite"):
            fragile.append("égalité entre lectures dans les mots N5, départagée par les autres niveaux")
        if lect.get("comptee_sur", "N5") != "N5":
            fragile.append("aucun mot N5 ne s'aligne : lecture comptée sur tous les niveaux")
        elif lect["mots_n5"] <= 1:
            fragile.append("un seul mot N5 porte cette lecture")
        if lect["type"] == "kun" and len(lect["kana"]) == 1:
            fragile.append("lecture kun d'une seule syllabe, souvent un fragment (okurigana, suffixe)")

        entrees.append(OrderedDict(
            kanji=k,
            statut="brouillon à relire",
            traits=d["traits"],
            sens_fr=t["sens_fr"],
            sens_en=t["sens_en"],
            sens_fr_candidats=d["sens_fr_candidats"],
            sens_en_candidats=d["sens_en_candidats"],
            lecture=lect,
            lecture_fragile=fragile,
            comptes_lecture=d["comptes_lecture"],
            mots_n5_contenant=d["mots_n5"],
            mots_n5_non_alignes=d["mots_non_alignes"],
            composants=[OrderedDict(element=c["element"], **({"forme_de": c["forme_de"]} if "forme_de" in c else {}),
                                    fr=noms.get(c["element"], {}).get("fr"), en=noms.get(c["element"], {}).get("en"))
                        for c in kvg["composants"]],
            sous_composants=kvg["sous_composants"],
            traits_libres=kvg["traits_libres"],
            composants_cites=noms_cites,
            mnemo_fr=t["mnemo_fr"],
            mnemo_en=t["mnemo_en"],
            confiance=t["confiance"],
            confiance_pourquoi=t["confiance_pourquoi"],
            exemples=exemples,
        ))

    if peu:
        avis.append("%d kanji ont moins de deux mots N5 sous la lecture retenue ; exemples complétés "
                    "par une autre lecture (marquée) : %s" % (len(peu), " ".join(peu)))
    for k in textes:
        if k not in derive and not k.startswith("_"):
            erreurs.append("%s : texte pour un kanji hors de la liste N5" % k)

    # Lexique des composants : tous ceux de KanjiVG, nommés ou non.
    lexique = OrderedDict()
    for k, d in derive.items():
        kvg = d["kanjivg"] or {"composants": [], "sous_composants": []}
        for el in [c["element"] for c in kvg["composants"]] + kvg["sous_composants"] + ([k] if not kvg["composants"] else []):
            lexique.setdefault(el, OrderedDict(element=el, fr=noms.get(el, {}).get("fr"), en=noms.get(el, {}).get("en"),
                                               dans=[], cite_dans=utilises.get(el, [])))
            if k not in lexique[el]["dans"] and el != k:
                lexique[el]["dans"].append(k)
    for el in noms:
        if not el.startswith("_") and el not in lexique:
            avis.append("composant %s nommé mais absent des décompositions N5" % el)
    for el, info in lexique.items():
        if info["fr"] is None and info["cite_dans"]:
            erreurs.append("composant %s cité mais sans nom" % el)
    # Un même nom pour deux composants casserait le système cumulatif.
    vus = {}
    for el, n in noms.items():
        if el.startswith("_"):
            continue
        for langue in ("fr", "en"):
            if (langue, n[langue]) in vus:
                erreurs.append("nom %s « %s » donné à %s et %s" % (langue, n[langue], vus[(langue, n[langue])], el))
            vus[(langue, n[langue])] = el

    meta = OrderedDict(
        description="Pilote : mnémotechniques des kanji JLPT N5 pour francophones (et anglophones).",
        statut="brouillon à relire",
        construit_par="python japonais/kanji/construire.py",
        sources=OrderedDict(
            kanji="japonais/kanji.json (KANJIDIC2 %s, niveaux Tanos)" % meta_k["sources"]["kanjidic2_version"]["database_version"],
            mots="japonais/mots.json (listes JLPT de Jonathan Waller)",
            kanjivg="%s @ %s" % (KVG_DEPOT, kanjivg_version(dossier_kvg)),
        ),
        licence="Données dérivées de KANJIDIC2 (CC BY-SA 4.0) et KanjiVG (CC BY-SA 3.0) ; voir LICENCES.md.",
        kanji_n5_dans_kanji_json=len(derive),
    )
    return entrees, lexique, meta, erreurs, avis, selection


def ecrire_json(nom, obj):
    with open(os.path.join(ICI, nom), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def page_relecture(entrees, selection):
    par_kanji = {e["kanji"]: e for e in entrees}
    cartes = []
    for k in selection["kanji"]:
        e = par_kanji[k]
        l = e["lecture"]
        ex = " · ".join("%s <span class=k>%s</span>%s" % (
            html.escape(m["mot"]), html.escape(m["kana"]),
            " <small>(autre lecture)</small>" if m.get("autre_lecture") else
            " <small>(lecture spéciale)</small>" if m.get("lecture_speciale") else "")
            for m in e["exemples"])
        comp = ", ".join("%s %s" % (c["element"], html.escape(c["fr"])) for c in e["composants_cites"]) or "—"
        cartes.append("""<article>
  <div class=kanji lang=ja>{k}</div>
  <div class=corps>
    <p class=tete><b>{sens}</b> · <span lang=ja>{kana}</span> <i>{romaji}</i> <small>(lecture {type}, {n} mot{s} N5)</small></p>
    <p class=comp>Composants : {comp}</p>
    <p class=mnemo>{mnemo}</p>
    <p class=ex lang=ja>{ex}</p>
    <p class=cases><label><span class=case></span> ça marche</label><label><span class=case></span> ça ne marche pas</label></p>
    <p class=note>Remarque :</p>
  </div>
</article>""".format(k=k, sens=html.escape(e["sens_fr"]), kana=html.escape(l["kana"]), romaji=html.escape(l["romaji"]),
                     type=l["type"], n=l["mots_n5"], s="s" if l["mots_n5"] > 1 else "", comp=comp, mnemo=gras(e["mnemo_fr"]), ex=ex))
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kanji N5 à relire</title>
<!-- Généré par construire.py : ne pas modifier à la main. -->
<style>
:root{{--encre:#1C2430;--papier:#FBF8F2;--ambre:#E8A23A;--trait:#d9d2c3;--doux:#5b6470}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--encre:#ECE7DD;--papier:#171C24;--trait:#3a4250;--doux:#a7afba}}}}
:root[data-theme="dark"]{{--encre:#ECE7DD;--papier:#171C24;--trait:#3a4250;--doux:#a7afba}}
*{{box-sizing:border-box}}
body{{margin:0;padding:24px 16px;background:var(--papier);color:var(--encre);font:16px/1.5 Georgia,"Times New Roman",serif}}
main{{max-width:820px;margin:0 auto}}
h1{{font-size:1.5rem;margin:0 0 .25rem}}
.intro{{color:var(--doux);margin:0 0 1.5rem}}
article{{display:flex;gap:20px;border-top:1px solid var(--trait);padding:18px 0;break-inside:avoid;page-break-inside:avoid}}
.kanji{{font-size:88px;line-height:1;min-width:110px;text-align:center;font-family:"Noto Serif JP","Hiragino Mincho ProN","Yu Mincho",serif}}
.corps{{flex:1;min-width:0}}
.corps p{{margin:.2rem 0}}
.tete{{font-size:1.1rem}}
.tete i{{color:var(--doux)}}
.comp,.ex,small{{color:var(--doux);font-size:.9rem}}
.mnemo{{font-size:1.05rem;margin:.5rem 0!important}}
.mnemo strong{{background:linear-gradient(transparent 60%,color-mix(in srgb,var(--ambre) 45%,transparent) 60%)}}
.k{{opacity:.8}}
.cases{{display:flex;gap:28px;margin-top:.6rem!important;flex-wrap:wrap}}
.case{{display:inline-block;width:16px;height:16px;border:1.5px solid var(--encre);vertical-align:-2px;margin-right:6px}}
.note{{color:var(--doux);border-bottom:1px dotted var(--trait);padding-bottom:1.2rem}}
@media (max-width:520px){{article{{flex-direction:column;gap:6px}}.kanji{{text-align:left;font-size:72px}}}}
@media print{{body{{background:#fff;color:#000}}}}
</style>
</head>
<body>
<main>
<h1>Kanji N5 : 20 mnémotechniques à juger</h1>
<p class="intro">Brouillon à relire. Pour chaque kanji : est-ce que la phrase française fait <em>entendre</em> la lecture (le morceau souligné) et <em>voir</em> le sens ? Cochez, annotez, imprimez. Rien n'est envoyé. {n} kanji choisis pour varier : simples, composés, lectures on et kun, et trois de confiance basse.</p>
{cartes}
</main>
</body>
</html>
""".format(cartes="\n".join(cartes), n=len(selection["kanji"]))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--kanjivg", help="copie locale du dépôt KanjiVG (sinon ~/.cache/kanjivg, cloné au besoin)")
    p.add_argument("--donnees", help="écrire seulement les données dérivées dans ce fichier")
    a = p.parse_args()
    dossier = kanjivg_dossier(a.kanjivg)

    if a.donnees:
        derive, _, _ = deriver(dossier)
        with open(a.donnees, "w", encoding="utf-8") as f:
            json.dump(derive, f, ensure_ascii=False, indent=1)
        print("Données dérivées de %d kanji écrites dans %s" % (len(derive), a.donnees))
        return 0

    entrees, lexique, meta, erreurs, avis, selection = construire(dossier)
    for k in selection["kanji"]:
        if k not in {e["kanji"] for e in entrees}:
            erreurs.append("a_relire.json : %s sans entrée" % k)
    if len(selection["kanji"]) != 20:
        erreurs.append("a_relire.json : %d kanji au lieu de 20" % len(selection["kanji"]))
    basses = [k for k in selection["kanji"] if any(e["kanji"] == k and e["confiance"] == "basse" for e in entrees)]
    if len(basses) != 3:
        erreurs.append("a_relire.json : %d kanji de confiance basse au lieu de 3" % len(basses))

    ecrire_json("mnemoniques_n5.json", OrderedDict(meta=meta, kanji=entrees))
    nommes = [v for v in lexique.values() if v["fr"]]
    ecrire_json("composants.json", OrderedDict(
        meta=OrderedDict(description="Lexique des composants KanjiVG des kanji N5, un nom stable par composant.",
                         source=meta["sources"]["kanjivg"], statut="brouillon à relire",
                         composants=len(lexique), nommes=len(nommes)),
        composants=list(lexique.values())))
    if not erreurs:
        with open(os.path.join(ICI, "a-relire.html"), "w", encoding="utf-8") as f:
            f.write(page_relecture(entrees, selection))

    conf = Counter(e["confiance"] for e in entrees)
    typ = Counter(e["lecture"]["type"] for e in entrees)
    print("Kanji N5 dans kanji.json : %d ; entrées écrites : %d" % (meta["kanji_n5_dans_kanji_json"], len(entrees)))
    print("Confiance : haute %d, moyenne %d, basse %d" % (conf["haute"], conf["moyenne"], conf["basse"]))
    print("Lectures retenues : on %d, kun %d" % (typ["on"], typ["kun"]))
    print("Composants KanjiVG : %d, dont %d nommés, %d cités dans un mnémotechnique"
          % (len(lexique), len(nommes), sum(1 for v in lexique.values() if v["cite_dans"])))
    for x in avis:
        print("  avis :", x)
    for x in erreurs:
        print("  ERREUR :", x)
    print("Aucune erreur." if not erreurs else "%d erreur(s)." % len(erreurs))
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
