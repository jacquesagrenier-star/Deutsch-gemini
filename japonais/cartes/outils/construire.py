#!/usr/bin/env python3
"""Cartes de vocabulaire japonais N5-N3 : fabrique les fiches à partir des sources
et des décisions écrites à la main, puis vérifie tout.

    python japonais/cartes/outils/construire.py            # construit + vérifie
    python japonais/cartes/outils/construire.py --lots     # écrit aussi les lots à juger (lots/)
    python japonais/cartes/outils/construire.py --kanji F  # kanji.json local (sinon git show)

Entrées :
  sources/mots-n5-n3.json      Tanos + JMdict + phrases Tatoeba candidates (extrait sur le PC)
  kanji.json                   KANJIDIC2 (git show origin/japonais-donnees:japonais/kanji.json)
  decisions/<niv>-<nnn>.json   LES SEULS FICHIERS ÉCRITS À LA MAIN : glose choisie, phrase
                               retenue, verdict sur ce que JMdict proposait.

Sorties : mots-n5.json, mots-n4.json, mots-n3.json, phrases-n5.json…, a-relire.html,
          doublons.json (les entrées écartées parce que leur id existe déjà).

Bibliothèque standard seulement. Code de sortie 1 si une vérification échoue.
"""
import argparse
import json
import os
import subprocess
import sys
from collections import Counter, OrderedDict

ICI = os.path.dirname(os.path.abspath(__file__))
CARTES = os.path.dirname(ICI)
DEPOT = os.path.dirname(os.path.dirname(CARTES))
NIVEAUX = ["N5", "N4", "N3"]
TAILLE_LOT = 50
VERDICTS = ["BON", "A_AMELIORER", "A_REMPLACER", "FAUX"]

SOURCES = OrderedDict([
    ("tanos", {"nom": "Listes JLPT de Jonathan Waller (tanos.co.uk), copie stephenmk/yomitan-jlpt-vocab",
               "licence": "CC BY", "fichier": "japonais/cartes/sources/mots-n5-n3.json"}),
    ("jmdict", {"nom": "JMdict (EDRDG), jmdict-simplified 3.6.2+20260928191014",
                "licence": "CC BY-SA 4.0", "fichier": "japonais/cartes/sources/mots-n5-n3.json"}),
    ("kanjidic2", {"nom": "KANJIDIC2 (EDRDG) 2025-310", "licence": "CC BY-SA 4.0",
                   "fichier": "japonais/kanji.json @ japonais-donnees"}),
    ("tatoeba", {"nom": "Tatoeba (corpus Tanaka pour l'essentiel du japonais)",
                 "licence": "CC BY 2.0 FR", "fichier": "japonais/cartes/sources/mots-n5-n3.json"}),
    ("wortando", {"nom": "Texte original Wortando (brouillon machine)", "licence": "à choisir par le propriétaire",
                  "fichier": "japonais/cartes/decisions/"}),
    ("calcul", {"nom": "Calculé par un script à partir des champs voisins", "licence": "-",
                "fichier": "japonais/cartes/outils/construire.py"}),
])


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
    "わ": "wa", "ゐ": "i", "ゑ": "e", "を": "o", "ん": "n", "ゔ": "vu",
}
YOON = {"ゃ": "a", "ゅ": "u", "ょ": "o"}
PETITES = {"ぁ": "a", "ぃ": "i", "ぅ": "u", "ぇ": "e", "ぉ": "o"}
MACRON = {"a": "ā", "i": "ī", "u": "ū", "e": "ē", "o": "ō"}


def _syllabes(kana):
    """Découpe en syllabes romanisées ; 'っ' et 'ー' restent des marqueurs."""
    k = hira(kana)
    syl = []
    i = 0
    while i < len(k):
        c = k[i]
        nxt = k[i + 1] if i + 1 < len(k) else ""
        if nxt in YOON and c in ROMAJI:
            base = ROMAJI[c]
            syl.append(base[:-1] + YOON[nxt] if base in ("shi", "chi", "ji") else base[:-1] + "y" + YOON[nxt])
            i += 2
            continue
        if nxt in PETITES and c in ROMAJI:
            # Sons des emprunts : ファ fa, ティ ti, ウィ wi, チェ che, トゥ tu, ヴァ va
            base, v = ROMAJI[c], PETITES[nxt]
            if base in ("shi", "chi", "ji") and v == "e":
                syl.append(base[:-1] + "e")
            elif base in ("te", "de") and v in "iu":
                syl.append(base[0] + v)
            elif base in ("to", "do") and v == "u":
                syl.append(base[0] + "u")
            elif base == "fu":
                syl.append("f" + v)
            elif base == "tsu":
                syl.append("ts" + v)
            elif base == "vu":
                syl.append("v" + v)
            elif base == "u":
                syl.append("w" + v)
            elif base in ("ku", "gu"):
                syl.append(base[0] + "w" + v)
            else:
                syl.append(base[:-1] + v)
            i += 2
            continue
        if c in ("っ", "ー"):
            syl.append(c)
        elif c in ROMAJI:
            syl.append(ROMAJI[c])
        else:
            raise ValueError("kana inconnu pour le romaji : %r dans %r" % (c, kana))
        i += 1
    return syl


def _romaji_bloc(kana, voyelles_longues=True):
    syl = _syllabes(kana)
    out = ""
    for j, s in enumerate(syl):
        if s == "っ":
            nxt = syl[j + 1] if j + 1 < len(syl) else ""
            out += "t" if nxt.startswith("ch") else nxt[:1]
        elif s == "ー":
            if out and out[-1] in MACRON:
                out = out[:-1] + MACRON[out[-1]]
        elif s == "n" and j + 1 < len(syl) and syl[j + 1][:1] in "aiueoy":
            out += "n'"
        else:
            out += s
    if voyelles_longues:
        for long_, court in (("ou", "ō"), ("oo", "ō"), ("uu", "ū"), ("aa", "ā"), ("ee", "ē")):
            out = out.replace(long_, court)
    return out


# Mots en kana où deux voyelles se touchent sans faire une voyelle longue.
ROMAJI_EXCEPTIONS = {"そのうち": "sonouchi"}


def romaji(kana, blocs=None, classe=None):
    """Hepburn modifié (comme japonais/kana/kana.json) : voyelles longues avec macron.

    Les voyelles ne fusionnent qu'à l'intérieur d'un bloc de furigana : 思う reste
    « omou » (おも + う), 学校 donne « gakkō » (こう dans un seul bloc). Sans blocs (mot en
    kana), le う final d'un verbe en -u (v5u) ne fusionne pas : もらう, おう.
    """
    if not blocs and kana in ROMAJI_EXCEPTIONS:
        return ROMAJI_EXCEPTIONS[kana]
    if blocs:
        morceaux = [lec if lec is not None else txt for txt, lec in blocs]
    elif classe and classe.startswith("v5u") and len(kana) > 1 and hira(kana).endswith("う"):
        morceaux = [kana[:-1], kana[-1]]
    else:
        morceaux = [kana]
    # On romanise tout d'un coup (っ et ん regardent la syllabe suivante), puis on
    # fusionne les voyelles bloc par bloc.
    tout = _romaji_bloc("".join(morceaux), voyelles_longues=False)
    if len(morceaux) == 1:
        return _romaji_bloc(morceaux[0])
    # Recoupe : romanise chaque préfixe sans fusion pour retrouver les frontières.
    res, prec = "", ""
    acc = ""
    for m in morceaux:
        acc += m
        cur = _romaji_bloc(acc, voyelles_longues=False)
        part = cur[len(prec):] if cur.startswith(prec) else None
        if part is None:  # っ en fin de bloc : la frontière bouge, on refait sans découpe
            return _romaji_bloc("".join(morceaux))
        for long_, court in (("ou", "ō"), ("oo", "ō"), ("uu", "ū"), ("aa", "ā"), ("ee", "ē")):
            part = part.replace(long_, court)
        res += part
        prec = cur
    assert prec == tout
    return res


# ---------------------------------------------------- lectures et alignement
# Repris de japonais/kanji/construire.py (branche japonais-kanji-mnemo).

DAKUTEN = dict(zip("かきくけこさしすせそたちつてとはひふへほ", "がぎぐげござじずぜぞだぢづでどばびぶべぼ"))
HANDAKUTEN = dict(zip("はひふへほ", "ぱぴぷぺぽ"))
DAKUTEN["ち"] = "じ"
DAKUTEN["つ"] = "ず"


def lectures_de(entree):
    out = []
    for r in entree.get("lectures_on", []):
        out.append(("on", hira(r)))
    for r in entree.get("lectures_kun", []):
        radical = r.replace("-", "").split(".")[0]
        if radical:
            out.append(("kun", radical))
            # Forme en -i d'un verbe (入.る → いり dans 入口, 切.る → きり → きっ dans 切手)
            if "." in r:
                oku = r.replace("-", "").split(".")[1]
                if oku and oku[-1] in RENYOU:
                    out.append(("kun", radical + oku[:-1] + RENYOU[oku[-1]]))
                if len(oku) >= 2 and oku[-1] == "る":  # verbe en -eru/-iru : 受.ける → うけ
                    out.append(("kun", radical + oku[:-1]))
    return out


RENYOU = dict(zip("うくぐすつぬぶむる", "いきぎしちにびみり"))


def surfaces(radical):
    yield radical, 0
    if radical[0] in DAKUTEN:
        yield DAKUTEN[radical[0]] + radical[1:], 1
    if radical[0] in HANDAKUTEN:
        yield HANDAKUTEN[radical[0]] + radical[1:], 1
    if radical[0] in "ちつ":  # rendaku ぢ / づ (小包 こづつみ), à côté de じ / ず
        yield {"ち": "ぢ", "つ": "づ"}[radical[0]] + radical[1:], 1
    if len(radical) > 1 and radical[-1] in "つちくきり":
        yield radical[:-1] + "っ", 1
        if radical[0] in DAKUTEN:
            yield DAKUTEN[radical[0]] + radical[1:-1] + "っ", 2
        if radical[0] in HANDAKUTEN:
            yield HANDAKUTEN[radical[0]] + radical[1:-1] + "っ", 2


def est_kana(c):
    return "ぁ" <= c <= "ゖ" or "ァ" <= c <= "ヺ" or c == "ー"


def aligner(graphie, kana, index_kanji):
    """Découpes de `kana` sur `graphie` au coût minimal : (coût, [[(kanji, surface, type)…]…])."""
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
        for type_, radical in lectures_de(entree):
            for surf, cout_v in surfaces(radical):
                if kana.startswith(surf, j):
                    chemin.append((c, surf, type_))
                    rec(i + 1, j + len(surf), cout + cout_v, chemin, cible)
                    chemin.pop()

    rec(0, 0, 0, [], None)
    if not resultats:
        return None, []
    meilleur = min(c for c, _ in resultats)
    return meilleur, [d for c, d in resultats if c == meilleur]


def furigana(graphie, kana, index_kanji):
    """Rend (blocs, statut, note). blocs = [[texte, lecture|None], …]."""
    if not graphie:
        return [[kana, None]], "brouillon", None
    cout, decoupes = aligner(graphie, kana, index_kanji)
    if decoupes:
        # Les découpes qui ne diffèrent que par le type (on/kun de même son) donnent les
        # mêmes furigana ; on ne garde que les surfaces différentes.
        par_surface = OrderedDict()
        for d in decoupes:
            par_surface.setdefault(tuple(s for _, s, _ in d), d)
        if len(par_surface) == 1:
            d = next(iter(par_surface.values()))
            return _blocs(graphie, kana, [s for _, s, _ in d]), "brouillon", None
        # Plusieurs coupes : on préfère celle qui ne change pas de type de lecture.
        def changements(d):
            t = [x[2] for x in d]
            return sum(1 for a, b in zip(t, t[1:]) if a != b)
        notes = sorted(par_surface.values(), key=changements)
        if changements(notes[0]) < changements(notes[1]):
            return _blocs(graphie, kana, [s for _, s, _ in notes[0]]), "brouillon", None
        bloc = _bloc_unique(graphie, kana)
        return bloc, "manquant", "découpe ambiguë (%s) : un seul bloc en attendant" % " / ".join(
            "+".join(k) for k in par_surface)
    bloc = _bloc_unique(graphie, kana)
    inconnus = [c for c in graphie if not est_kana(c) and c != "々" and c not in index_kanji]
    if inconnus:
        return bloc, "manquant", "kanji absent de kanji.json (%s) : lecture non vérifiée, un seul bloc" % "".join(inconnus)
    return bloc, "brouillon", "lecture spéciale (hors lectures KANJIDIC) : un seul bloc pour le mot"


def _blocs(graphie, kana, surfaces_kanji):
    """Reconstitue les blocs : un par kanji, kana contigus réunis (lecture None)."""
    out, it = [], iter(surfaces_kanji)
    for c in graphie:
        if est_kana(c):
            if out and out[-1][1] is None:
                out[-1][0] += c
            else:
                out.append([c, None])
        else:
            out.append([c, next(it)])
    # 々 : le bloc garde sa propre lecture
    return out


def _bloc_unique(graphie, kana):
    """Un bloc pour le cœur en kanji ; les kana identiques au début et à la fin restent à part."""
    h = hira(kana)
    debut = 0
    while debut < len(graphie) and est_kana(graphie[debut]) and debut < len(h) and hira(graphie[debut]) == h[debut]:
        debut += 1
    fin = 0
    while (fin < len(graphie) - debut and est_kana(graphie[-1 - fin]) and fin < len(h) - debut
           and hira(graphie[-1 - fin]) == h[-1 - fin]):
        fin += 1
    out = []
    if debut:
        out.append([graphie[:debut], None])
    out.append([graphie[debut:len(graphie) - fin], kana[debut:len(kana) - fin]])
    if fin:
        out.append([graphie[len(graphie) - fin:], None])
    return out


# ------------------------------------------------------------------ chargement

def charger_kanji(chemin):
    if chemin:
        texte = open(chemin, encoding="utf-8").read()
    else:
        texte = subprocess.run(["git", "-C", DEPOT, "show", "origin/japonais-donnees:japonais/kanji.json"],
                               capture_output=True, text=True, check=True, encoding="utf-8").stdout
    data = json.loads(texte)
    index = {e["kanji"]: e for niv in data["niveaux"].values() for e in niv}
    complement = os.path.join(CARTES, "sources", "kanji-complement.json")
    if os.path.exists(complement):  # kanji hors listes JLPT (分, 丈…) : outils/complement_kanji.py
        for c, e in json.load(open(complement, encoding="utf-8"))["kanji"].items():
            index.setdefault(c, e)
    return index


def sans_rare(f):
    return f[:-7] if f.endswith(" (rare)") else f


def misc_premier_sens(e):
    return e["sens_en"][0].get("misc", []) if e["sens_en"] else []


def forme_kanji(e):
    """(forme affichée, note) : null si « usually kana » au premier sens ; sinon la forme
    Tanos si JMdict la dit courante, sinon la première forme courante de JMdict."""
    formes = e["jmdict_formes_kanji"]
    courantes = [f for f in formes if not f.endswith(" (rare)")]
    if "uk" in misc_premier_sens(e):
        if e["kanji"]:
            return None, "s'écrit d'habitude en kana (JMdict « uk ») ; forme kanji : %s" % e["kanji"]
        return None, None
    if e["kanji"] and e["kanji"] in courantes:
        return e["kanji"], None
    if courantes:
        if e["kanji"]:
            return courantes[0], "Tanos écrit %s (graphie peu courante) ; forme courante JMdict" % e["kanji"]
        return courantes[0], "Tanos l'écrit en kana ; JMdict donne %s comme forme courante" % courantes[0]
    return e["kanji"], None


def gloses_fr_plates(e):
    vues, out = set(), []
    for groupe in e["gloses_fr_en_vrac"]:
        for g in groupe:
            if g not in vues:
                vues.add(g)
                out.append(g)
    return out


def phrases_eligibles(e):
    return [p for p in e["phrases_candidates"] if "sous-chaîne" not in p["appariement"]]


def charger_entrees():
    src = json.load(open(os.path.join(CARTES, "sources", "mots-n5-n3.json"), encoding="utf-8"))
    par_niveau = OrderedDict((n, []) for n in NIVEAUX)
    for e in src["entrees"]:
        par_niveau[e["niveau"]].append(e)
    gardees, ecartees, vus = OrderedDict(), [], {}
    for niv in NIVEAUX:
        groupes = OrderedDict()
        for e in par_niveau[niv]:
            groupes.setdefault(e["jmdict_id"], []).append(e)
        gardees[niv] = []
        for jid, l in groupes.items():
            def rang(e):
                kanas = e["jmdict_formes_kana"]
                rk = kanas.index(e["kana"]) if e["kana"] in kanas else 99
                fk = [sans_rare(f) for f in e["jmdict_formes_kanji"]]
                rf = fk.index(e["kanji"]) if e["kanji"] in fk else 99
                return (rk, rf)
            choisie = min(l, key=rang)
            for autre in l:
                if autre is not choisie:
                    ecartees.append({"id": "jmdict:" + jid, "niveau": niv, "kanji": autre["kanji"], "kana": autre["kana"],
                                     "waller_en": autre["waller_en"], "garde": "%s %s %s" % (niv, choisie["kanji"] or "", choisie["kana"]),
                                     "raison": "même id dans le même niveau"})
            if jid in vus:
                prem = vus[jid]
                ecartees.append({"id": "jmdict:" + jid, "niveau": niv, "kanji": choisie["kanji"], "kana": choisie["kana"],
                                 "waller_en": choisie["waller_en"], "garde": "%s %s %s" % (prem["niveau"], prem["kanji"] or "", prem["kana"]),
                                 "raison": "id déjà présent à un niveau plus facile"})
                continue
            vus[jid] = choisie
            gardees[niv].append(choisie)
    return gardees, ecartees


# ---------------------------------------------------------------------- lots

def resume_lot(e, idx_kanji):
    k, _ = forme_kanji(e)
    sens = []
    for i, s in enumerate(e["sens_en"][:6]):
        t = "%d. [%s] %s" % (i + 1, ",".join(s["pos"]), "; ".join(s["en"][:6]))
        extra = s.get("misc", []) + s.get("field", [])
        if extra:
            t += " {" + ",".join(extra) + "}"
        if s.get("info"):
            t += " (" + "; ".join(s["info"])[:120] + ")"
        sens.append(t)
    if len(e["sens_en"]) > 6:
        sens.append("… %d autres sens" % (len(e["sens_en"]) - 6))
    ph = []
    for p in phrases_eligibles(e):
        drap = []
        drap.append("niveau ok" if p["niveau_respecte"] else "niveau dépassé (" + str(p["niveau_mot_le_plus_difficile"]) + ")")
        drap.append("longueur ok" if p["longueur_dans_la_cible"] else "longueur hors cible")
        drap.append("fr direct" if p["francais_direct"] else "fr via l'anglais")
        ph.append(OrderedDict([("jpn", p["ids_tatoeba"]["jpn"]), ("ja", p["japonais"]), ("fr", p["francais"]),
                               ("en", p["anglais"]), ("drapeaux", ", ".join(drap))]))
    rejet = len(e["phrases_candidates"]) - len(ph)
    d = OrderedDict([("id", "jmdict:" + e["jmdict_id"]), ("mot", k or e["kana"]), ("kana", e["kana"]),
                     ("waller", e["waller_en"]), ("sens_en", sens), ("fr_jmdict", gloses_fr_plates(e)),
                     ("phrases", ph)])
    if rejet:
        d["phrases_rejetees_sous_chaine"] = rejet
    return d


def decouper(gardees):
    """Lots de 50 mots ; un reste de moins de 10 rejoint le lot précédent."""
    out = OrderedDict()
    for niv, l in gardees.items():
        bornes = list(range(0, len(l), TAILLE_LOT))
        if len(bornes) > 1 and len(l) - bornes[-1] < 10:
            bornes.pop()
        for i, n in enumerate(bornes):
            fin = bornes[i + 1] if i + 1 < len(bornes) else len(l)
            out["%s-%03d" % (niv.lower(), i + 1)] = l[n:fin]
    return out


def ecrire_lots(gardees, idx_kanji):
    dossier = os.path.join(CARTES, "lots")
    os.makedirs(dossier, exist_ok=True)
    for nom, l in decouper(gardees).items():
        with open(os.path.join(dossier, nom + ".json"), "w", encoding="utf-8") as f:
            json.dump([resume_lot(e, idx_kanji) for e in l], f, ensure_ascii=False, indent=1)


def lots_de(gardees):
    return OrderedDict((nom, ["jmdict:" + e["jmdict_id"] for e in l]) for nom, l in decouper(gardees).items())


# ----------------------------------------------------------------- décisions

def charger_decisions(erreurs):
    dossier = os.path.join(CARTES, "decisions")
    dec = {}
    if not os.path.isdir(dossier):
        return dec
    for nom in sorted(os.listdir(dossier)):
        if not nom.endswith(".json"):
            continue
        try:
            l = json.load(open(os.path.join(dossier, nom), encoding="utf-8"))
        except ValueError as ex:
            erreurs.append("%s : JSON illisible (%s)" % (nom, ex))
            continue
        for d in l:
            if d.get("id") in dec:
                erreurs.append("%s : décision en double pour %s" % (nom, d.get("id")))
            d["_fichier"] = nom
            dec[d["id"]] = d
    return dec


def feuille(v, src, statut="brouillon", note=None):
    f = OrderedDict([("v", v), ("src", src), ("statut", statut)])
    if note:
        f["note"] = note
    return f


def classe_de(e):
    pos = e["sens_en"][0]["pos"] if e["sens_en"] else []
    return pos[0] if pos else None


def flexion_de(classe):
    if classe and (classe.startswith("v") and classe not in ("vs-c",) or classe in ("adj-i", "adj-ix")):
        return OrderedDict([("moteur", "conjugaison"), ("classe_cle", "classe")])
    return None


def construire_fiche(e, niv, idx_kanji, d, erreurs, phrases_sortie):
    jid = "jmdict:" + e["jmdict_id"]
    k, note_k = forme_kanji(e)
    classe = classe_de(e)
    blocs, st_furi, note_furi = furigana(k, e["kana"], idx_kanji)
    rom = romaji(e["kana"], blocs if k else None, classe)
    fr_plates = gloses_fr_plates(e)
    en_plates = [g for s in e["sens_en"] for g in s["en"]]

    fiche = OrderedDict()
    fiche["id"] = jid
    fiche["type"] = "mot"
    fiche["niveau"] = niv
    ecr = OrderedDict()
    if k:
        ecr["kanji"] = feuille(k, "tanos" if k == e["kanji"] else "jmdict", note=note_k)
    else:
        ecr["kanji"] = feuille(None, None, note=note_k) if note_k else feuille(None, None)
    ecr["kana"] = feuille(e["kana"], "tanos")
    ecr["romaji"] = feuille(rom, "calcul")
    fiche["ecritures"] = ecr
    fiche["furigana"] = feuille(blocs, "calcul", st_furi, note_furi)
    fiche["classe"] = feuille(classe, "jmdict") if classe else feuille(None, None, "manquant", "aucun sens JMdict")
    fiche["flexion"] = flexion_de(classe)

    if d is None:
        fr = OrderedDict([("affichee", feuille(None, None, "manquant", "pas encore jugé")), ("autres", [])])
        en = OrderedDict([("affichee", feuille(e["waller_en"], "tanos")), ("autres", [])])
        fiche["gloses"] = OrderedDict([("fr", fr), ("en", en)])
        verdict, raison, ph = None, None, []
    else:
        lieu = "%s / %s" % (d["_fichier"], jid)
        aff = (d.get("fr") or "").strip()
        if not aff:
            erreurs.append(lieu + " : glose française affichée vide")
        src_fr = d.get("fr_src")
        if src_fr not in ("jmdict", "wortando"):
            erreurs.append(lieu + " : fr_src doit valoir jmdict ou wortando")
        if src_fr == "jmdict":
            manquantes = [p for p in aff.split(" ; ") if p not in fr_plates]
            if manquantes:
                erreurs.append(lieu + " : fr_src=jmdict mais « %s » n'est pas une glose JMdict" % " ; ".join(manquantes))
        if aff.count(";") > 1:
            erreurs.append(lieu + " : plus de deux sens dans la glose affichée")
        fr = OrderedDict()
        fr["affichee"] = feuille(aff, src_fr, note=d.get("note"))
        fr["autres"] = [feuille(a, "jmdict" if a in fr_plates else "wortando") for a in d.get("fr_autres", []) if a and a != aff]
        aff_en = (d.get("en") or "").strip()
        if not aff_en:
            erreurs.append(lieu + " : glose anglaise affichée vide")
        src_en = "jmdict" if all(p in en_plates for p in aff_en.split("; ")) else (
            "tanos" if aff_en == e["waller_en"] else "wortando")
        en = OrderedDict()
        en["affichee"] = feuille(aff_en, src_en)
        en["autres"] = [feuille(a, "jmdict" if a in en_plates else "wortando") for a in d.get("en_autres", []) if a and a != aff_en]
        fiche["gloses"] = OrderedDict([("fr", fr), ("en", en)])
        verdict, raison = d.get("verdict"), d.get("raison")
        if verdict not in VERDICTS:
            erreurs.append(lieu + " : verdict %r inconnu" % verdict)
        if not raison:
            erreurs.append(lieu + " : raison absente")
        ph = []
        candidates = {p["ids_tatoeba"]["jpn"]: p for p in phrases_eligibles(e)}
        toutes = {p["ids_tatoeba"]["jpn"]: p for p in e["phrases_candidates"]}
        if len(d.get("phrases", [])) > 2:
            erreurs.append(lieu + " : plus de deux phrases")
        for pid in d.get("phrases", []):
            if pid not in candidates:
                erreurs.append(lieu + " : phrase %s %s" % (pid, "rejetée (sous-chaîne)" if pid in toutes else "absente des candidates"))
                continue
            p = candidates[pid]
            fid = "phrase:tatoeba:%d" % pid
            ph.append(fid)
            fp = phrases_sortie.get(fid)
            if fp is None:
                fp = OrderedDict()
                fp["id"] = fid
                fp["type"] = "phrase"
                fp["niveau"] = niv
                fp["texte"] = OrderedDict([
                    ("ja", feuille(p["japonais"], "tatoeba", "brouillon", "japonais à relire par un natif")),
                    ("fr", feuille(p["francais"], "tatoeba", "brouillon",
                                   None if p["francais_direct"] else "traduction française rattachée via l'anglais")),
                    ("en", feuille(p["anglais"], "tatoeba", "brouillon")),
                ])
                fp["tatoeba"] = OrderedDict([("ids", p["ids_tatoeba"]), ("auteurs", p["auteurs"])])
                fp["mots"] = []
                fp["provenance"] = OrderedDict([("appariement", p["appariement"]),
                                                ("niveau_mot_le_plus_difficile", p["niveau_mot_le_plus_difficile"]),
                                                ("longueur", p["longueur"])])
                phrases_sortie[fid] = fp
            fp["mots"].append(jid)
        if not ph and not d.get("note_phrase"):
            erreurs.append(lieu + " : aucune phrase retenue et pas de note_phrase")
    fiche["kanji"] = list(OrderedDict.fromkeys(c for c in (k or "") if not est_kana(c) and c != "々"))
    fiche["phrases"] = ph
    if d is not None and d.get("note_phrase"):
        fiche["note_phrases"] = d["note_phrase"]
    fiche["image"] = None
    fiche["verdict_machine"] = verdict
    fiche["raison"] = raison
    prov = OrderedDict([("tanos", OrderedDict([("kanji", e["kanji"]), ("kana", e["kana"]), ("waller_en", e["waller_en"])])),
                        ("jmdict_id", e["jmdict_id"])])
    if d is not None:
        prov["decision"] = "japonais/cartes/decisions/" + d["_fichier"]
    fiche["provenance"] = prov
    # Données utiles à la page de relecture, retirées avant écriture.
    fiche["_fr_jmdict"] = fr_plates
    fiche["_en_jmdict"] = ["; ".join(s["en"][:4]) for s in e["sens_en"][:3]]
    return fiche


# --------------------------------------------------------------- vérifications

STATUTS = {"manquant", "brouillon", "source", "relu", "relu_natif", "valide"}


def verifier_feuille(f, lieu, erreurs):
    if not isinstance(f, dict) or "v" not in f or f.get("statut") not in STATUTS:
        erreurs.append(lieu + " : feuille mal formée")
    elif f.get("src") is not None and f["src"] not in SOURCES:
        erreurs.append(lieu + " : source inconnue %r" % f["src"])


def verifier(fichiers, erreurs):
    import re
    motif = re.compile(r"^(jmdict|ja|kanji|kana|phrase|de):.+")
    ids = Counter()
    for nom, data in fichiers.items():
        if set(data) != {"sources", "entrees"}:
            erreurs.append(nom + " : clés racine attendues sources + entrees")
        for f in data["entrees"]:
            lieu = "%s / %s" % (nom, f.get("id"))
            ids[f["id"]] += 1
            if not motif.match(f["id"]) or f.get("type") not in ("mot", "phrase") or f.get("niveau") not in NIVEAUX:
                erreurs.append(lieu + " : id, type ou niveau invalide")
            if f["type"] == "mot":
                for c in ("kanji", "kana", "romaji"):
                    verifier_feuille(f["ecritures"][c], lieu + " ecritures." + c, erreurs)
                for c in ("furigana", "classe"):
                    verifier_feuille(f[c], lieu + " " + c, erreurs)
                for lg in ("fr", "en"):
                    verifier_feuille(f["gloses"][lg]["affichee"], lieu + " glose " + lg, erreurs)
                    for a in f["gloses"][lg]["autres"]:
                        verifier_feuille(a, lieu + " autres " + lg, erreurs)
                blocs = f["furigana"]["v"]
                graphie = f["ecritures"]["kanji"]["v"]
                if "".join(b[0] for b in blocs) != (graphie or f["ecritures"]["kana"]["v"]):
                    erreurs.append(lieu + " : les furigana ne recomposent pas l'écriture")
                if hira("".join(b[1] if b[1] is not None else b[0] for b in blocs)) != hira(f["ecritures"]["kana"]["v"]):
                    erreurs.append(lieu + " : les furigana ne recomposent pas la lecture")
                attendu = romaji(f["ecritures"]["kana"]["v"], blocs if graphie else None, f["classe"]["v"])
                if attendu != f["ecritures"]["romaji"]["v"]:
                    erreurs.append(lieu + " : romaji %r, recalculé %r" % (f["ecritures"]["romaji"]["v"], attendu))
                if not isinstance(f["kanji"], list) or not isinstance(f["phrases"], list):
                    erreurs.append(lieu + " : kanji / phrases doivent être des listes")
            else:
                for c in ("ja", "fr", "en"):
                    verifier_feuille(f["texte"][c], lieu + " texte." + c, erreurs)
    for i, n in ids.items():
        if n > 1:
            erreurs.append("id en double : %s (%d fois)" % (i, n))


def tests_romaji(erreurs):
    cas = [("みず", None, None, "mizu"), ("がっこう", [["学", "がっ"], ["校", "こう"]], None, "gakkō"),
           ("おもう", [["思", "おも"], ["う", None]], None, "omou"), ("コーヒー", None, None, "kōhī"),
           ("おかあさん", [["お", None], ["母", "かあ"], ["さん", None]], None, "okāsan"),
           ("しんぶん", None, None, "shinbun"), ("きんえん", None, None, "kin'en"), ("ちょっと", None, None, "chotto"),
           ("パーティー", None, None, "pātī"), ("もらう", None, "v5u", "morau"), ("ありがとう", None, None, "arigatō"),
           ("きって", None, None, "kitte"), ("まっちゃ", None, None, "matcha"), ("フォーク", None, None, "fōku")]
    for kana, blocs, classe, attendu in cas:
        r = romaji(kana, blocs, classe)
        if r != attendu:
            erreurs.append("test romaji : %s → %s, attendu %s" % (kana, r, attendu))


# ----------------------------------------------------------------------- main

def principal():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kanji")
    ap.add_argument("--lots", action="store_true")
    ap.add_argument("--sec", action="store_true", help="vérifie sans rien écrire (pour juger en parallèle)")
    args = ap.parse_args()
    erreurs = []
    tests_romaji(erreurs)
    idx_kanji = charger_kanji(args.kanji)
    gardees, ecartees = charger_entrees()
    if args.lots:
        ecrire_lots(gardees, idx_kanji)
    decisions = charger_decisions(erreurs)
    connus = {"jmdict:" + e["jmdict_id"] for l in gardees.values() for e in l}
    for i, d in decisions.items():
        if i not in connus:
            erreurs.append("%s : décision pour un id inconnu %s" % (d["_fichier"], i))

    fichiers, pour_page = OrderedDict(), OrderedDict()
    for niv in NIVEAUX:
        phrases = OrderedDict()
        fiches = [construire_fiche(e, niv, idx_kanji, decisions.get("jmdict:" + e["jmdict_id"]), erreurs, phrases)
                  for e in gardees[niv]]
        pour_page[niv] = (fiches, phrases)
        propres = [OrderedDict((k, v) for k, v in f.items() if not k.startswith("_")) for f in fiches]
        fichiers["mots-%s.json" % niv.lower()] = OrderedDict([("sources", SOURCES), ("entrees", propres)])
        fichiers["phrases-%s.json" % niv.lower()] = OrderedDict([("sources", SOURCES), ("entrees", list(phrases.values()))])
    verifier(fichiers, erreurs)

    # Les lots incomplets sont signalés, pas bloquants : on avance niveau par niveau.
    etat = OrderedDict()
    for lot, ids in lots_de(gardees).items():
        faits = sum(1 for i in ids if i in decisions)
        etat[lot] = (faits, len(ids))

    for nom, data in ([] if args.sec else fichiers.items()):
        with open(os.path.join(CARTES, nom), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
            f.write("\n")
    if not args.sec:
        with open(os.path.join(CARTES, "doublons.json"), "w", encoding="utf-8") as f:
            json.dump(ecartees, f, ensure_ascii=False, indent=1)
            f.write("\n")
        import page
        page.ecrire(os.path.join(CARTES, "a-relire.html"), pour_page)

    stats = Counter()
    for niv, (fiches, _) in pour_page.items():
        for f in fiches:
            stats[(niv, f["verdict_machine"] or "non jugé")] += 1
    for niv in NIVEAUX:
        print(niv, ", ".join("%s %d" % (v, stats[(niv, v)]) for v in VERDICTS + ["non jugé"] if stats[(niv, v)]))
    incomplets = [l for l, (a, b) in etat.items() if a < b]
    print("Lots incomplets :", ", ".join("%s (%d/%d)" % (l, *etat[l]) for l in incomplets) or "aucun")
    print("Doublons écartés :", len(ecartees))
    if erreurs:
        print("\n%d ERREUR(S) :" % len(erreurs))
        for e in erreurs[:200]:
            print(" -", e)
        sys.exit(1)
    print("Vérifications : tout passe.")


if __name__ == "__main__":
    sys.path.insert(0, ICI)
    principal()
