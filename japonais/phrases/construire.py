#!/usr/bin/env python3
"""Phrases d'exemple Tatoeba pour les mots JLPT N5, N4 et N3.

Télécharge les listes de vocabulaire JLPT de Jonathan Waller (tanos.co.uk,
CC BY) et les exports de Tatoeba (CC BY 2.0 FR), puis choisit pour chaque mot
jusqu'à 3 phrases japonaises déjà traduites par des humains. Rien n'est
traduit ni inventé : un mot sans bonne phrase reste sans phrase, et il est
compté dans le rapport.

Usage :
    python construire.py               # télécharge ce qui manque, produit tout
    python construire.py --hors-ligne  # n'utilise que ce qui est déjà dans brut/
    python construire.py --brut DOSSIER

Produit, à côté de ce script : phrases.json et RAPPORT.md.
Les exports bruts vont dans brut/ (exclu du dépôt par .gitignore).

Bibliothèque standard uniquement.
"""

import argparse
import bz2
import csv
import datetime
import html
import io
import json
import os
import random
import re
import sys
import tarfile
import urllib.request
from collections import defaultdict

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_DEPOT = os.path.abspath(os.path.join(ICI, "..", ".."))

NIVEAUX = ["N5", "N4", "N3"]
# Plus le nombre est grand, plus le mot est facile (N5 = le plus facile).
RANG = {"N5": 5, "N4": 4, "N3": 3, "hors liste": 0}

TANOS = "https://www.tanos.co.uk/jlpt/jlpt{n}/vocab/"
TATOEBA = "https://downloads.tatoeba.org/exports/"
EXPORTS = {
    # nom local : (URL, fichier dans l'archive ou None si .bz2 simple)
    "jpn_sentences_detailed.tsv": (TATOEBA + "per_language/jpn/jpn_sentences_detailed.tsv.bz2", None),
    "fra_sentences_detailed.tsv": (TATOEBA + "per_language/fra/fra_sentences_detailed.tsv.bz2", None),
    "eng_sentences_detailed.tsv": (TATOEBA + "per_language/eng/eng_sentences_detailed.tsv.bz2", None),
    "links.csv": (TATOEBA + "links.tar.bz2", "links.csv"),
    "jpn_indices.csv": (TATOEBA + "jpn_indices.tar.bz2", "jpn_indices.csv"),
    "tags.csv": (TATOEBA + "tags.tar.bz2", "tags.csv"),
    "user_sentences.csv": (TATOEBA + "user_sentences.tar.bz2", "user_sentences.csv"),
}
# Ces deux-là affinent le tri ; leur absence n'empêche pas de construire.
FACULTATIFS = {"tags.csv", "user_sentences.csv"}
# Repli si un fichier par langue n'existe pas : l'export complet.
SENTENCES_COMPLET = (TATOEBA + "sentences_detailed.tar.bz2", "sentences_detailed.csv")

LONGUEUR_MIN, LONGUEUR_MAX = 6, 20
MAX_CANDIDATES = 3

# Étiquettes Tatoeba qui signalent une phrase douteuse.
TAGS_DOUTEUX = {
    "@needs native check", "@change", "@check", "@delete", "@neg",
    "@translation check", "@fixme", "@duplicate", "@check translation",
}

# Filtre lexical grossier : violence, sexe, vulgarité, politique, religion.
# Il ne voit que des mots, pas le sens : le rapport le rappelle.
ECARTER_JA = [
    "殺", "死ね", "自殺", "銃", "爆弾", "爆発", "戦争", "殴", "暴力", "血まみれ",
    "犯罪", "強盗", "強姦", "刑務所", "麻薬", "テロ", "拷問", "虐待", "誘拐",
    "セックス", "性交", "売春", "裸", "エッチ", "おっぱい", "ポルノ", "妊娠",
    "くそ", "クソ", "糞", "ちくしょう", "畜生", "ぶっ", "てめえ", "ばかやろう", "馬鹿野郎",
    "政治", "政府", "政党", "首相", "大統領", "選挙", "天皇", "共産", "独裁",
    "ナチ", "ヒトラー", "宗教", "神様", "イスラム", "キリスト", "ユダヤ",
]
# Note : des milliers de phrases récentes de Tatoeba sont des traductions de
# l'anglais autour de « Tom » et « Mary ». Elles ne sont pas fautives mais
# sonnent étrangement comme exemples d'un mot : on les classe après les autres
# plutôt que de les écarter (voir PENALITE_JA).
PENALITE_JA = ["トム", "メアリー", "メアリ", "ジョン"]

ECARTER_TRAD = re.compile(
    r"\b(fuck\w*|shit\w*|bitch\w*|cunt|dick|sex\w*|porn\w*|rape\w*|kill\w*|murder\w*|"
    r"suicid\w*|gun|guns|bomb\w*|nazi\w*|hitler|baise\w*|putain|merde\w*|salope|connard\w*|"
    r"bordel|tuer|tué\w*|meurtr\w*|viol|violée?s?|sexe\w*|pute\w*|bite|couilles?)\b",
    re.IGNORECASE,
)

# Mots grammaticaux du corpus (particules, auxiliaires, copule) : ils ne
# comptent pas dans « le mot le plus difficile de la phrase ».
GRAMMATICAUX = set(
    "は が を に で と も の へ や か ね よ な わ ぞ さ "
    "から まで より だけ しか ばかり ほど くらい ぐらい など って とか けど けれど けれども "
    "のに ので し たり ながら ても でも ば たら なら て で た だ です ます ない ず ぬ "
    "う よう そう らしい れる られる せる させる たい たがる まい ん んだ のだ のです "
    "する いる ある なる くる 来る 居る 有る 為る 成る".split()
)

KANA = re.compile(r"^[぀-ヿー～〜・ー]+$")
JA_CARACTERE = re.compile(r"[぀-ヿ㐀-鿿豈-﫿々ー]")


# --------------------------------------------------------------------------
# Téléchargement
# --------------------------------------------------------------------------

def telecharger(url, dest):
    print(f"  téléchargement {url}", flush=True)
    tmp = dest + ".part"
    req = urllib.request.Request(url, headers={"User-Agent": "wortando-japonais/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(tmp, "wb") as f:
        while True:
            bloc = r.read(1 << 20)
            if not bloc:
                break
            f.write(bloc)
    os.replace(tmp, dest)


def obtenir_export(brut, nom, hors_ligne):
    """Renvoie le chemin du fichier décompressé, ou None s'il est introuvable."""
    chemin = os.path.join(brut, nom)
    if os.path.exists(chemin):
        return chemin
    if hors_ligne:
        return None
    url, membre = EXPORTS[nom]
    archive = os.path.join(brut, os.path.basename(url))
    try:
        if not os.path.exists(archive):
            telecharger(url, archive)
        decompresser(archive, membre, chemin)
        return chemin
    except Exception as e:  # noqa: BLE001 - on rapporte et on continue
        print(f"  ! {nom} : {e}", file=sys.stderr)
        return None


def decompresser(archive, membre, dest):
    tmp = dest + ".part"
    if membre is None:
        with bz2.open(archive, "rb") as src, open(tmp, "wb") as out:
            while True:
                bloc = src.read(1 << 20)
                if not bloc:
                    break
                out.write(bloc)
    else:
        with tarfile.open(archive, "r:bz2") as tar:
            info = next((m for m in tar.getmembers() if os.path.basename(m.name) == membre), None)
            if info is None:
                raise RuntimeError(f"{membre} absent de {archive}")
            with tar.extractfile(info) as src, open(tmp, "wb") as out:
                while True:
                    bloc = src.read(1 << 20)
                    if not bloc:
                        break
                    out.write(bloc)
    os.replace(tmp, dest)


def obtenir_phrases(brut, hors_ligne):
    """Les trois fichiers de phrases ; repli sur l'export complet si besoin."""
    chemins = {lang: obtenir_export(brut, f"{lang}_sentences_detailed.tsv", hors_ligne)
               for lang in ("jpn", "fra", "eng")}
    if all(chemins.values()):
        return chemins
    complet = os.path.join(brut, "sentences_detailed.csv")
    if not os.path.exists(complet) and not hors_ligne:
        url, membre = SENTENCES_COMPLET
        archive = os.path.join(brut, os.path.basename(url))
        if not os.path.exists(archive):
            telecharger(url, archive)
        decompresser(archive, membre, complet)
    if not os.path.exists(complet):
        manque = [l for l, c in chemins.items() if not c]
        raise SystemExit(f"Phrases Tatoeba introuvables ({', '.join(manque)}) et pas d'export complet.")
    return {lang: complet for lang in ("jpn", "fra", "eng")}


# --------------------------------------------------------------------------
# Listes JLPT
# --------------------------------------------------------------------------

def nettoyer_cellule(c):
    c = re.sub(r"<br\s*/?>", ",", c, flags=re.I)
    c = re.sub(r"<[^>]+>", "", c)
    return html.unescape(c).strip()


def lire_tanos(brut, niveau, hors_ligne):
    n = niveau[1]
    chemin = os.path.join(brut, f"tanos_jlpt{n}_vocab.html")
    if not os.path.exists(chemin):
        if hors_ligne:
            raise SystemExit(f"{chemin} absent (mode hors ligne).")
        telecharger(TANOS.format(n=n), chemin)
    with open(chemin, "rb") as f:
        brut_html = f.read()
    texte = None
    for enc in ("utf-8", "shift_jis", "euc_jp"):
        try:
            texte = brut_html.decode(enc)
            break
        except UnicodeDecodeError:
            pass
    if texte is None:
        texte = brut_html.decode("utf-8", "replace")

    mots = []
    for ligne in re.findall(r"<tr[^>]*>(.*?)</tr>", texte, flags=re.S | re.I):
        cellules = [nettoyer_cellule(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", ligne, flags=re.S | re.I)]
        if len(cellules) < 3:
            continue
        kanji, kana, anglais = cellules[0], cellules[1], cellules[2]
        if not kana or not KANA.match(kana.replace(" ", "").replace(",", "").replace("、", "")):
            continue  # en-tête ou ligne parasite
        mots.append({"niveau": niveau, "mot": kanji or kana, "kanji": kanji,
                     "lecture": kana, "anglais": anglais, "source_liste": "tanos"})
    if not mots:
        raise SystemExit(f"Aucun mot lu dans {chemin} : la page de tanos a changé de format ?")
    return mots


def lire_mots_donnees():
    """japonais/mots.json de la branche japonais-donnees, s'il existe (lecture seule)."""
    import subprocess
    try:
        sortie = subprocess.run(
            ["git", "-C", RACINE_DEPOT, "show", "origin/japonais-donnees:japonais/mots.json"],
            capture_output=True, check=True,
        ).stdout
        return json.loads(sortie.decode("utf-8"))
    except Exception:  # noqa: BLE001
        return None


def charger_listes(brut, hors_ligne):
    mots = []
    for niveau in NIVEAUX:
        mots.extend(lire_tanos(brut, niveau, hors_ligne))
    # Un mot listé à deux niveaux garde le plus facile (même mot + même lecture).
    vus = {}
    for m in mots:
        cle = (m["kanji"], m["lecture"])
        if cle not in vus or RANG[m["niveau"]] > RANG[vus[cle]["niveau"]]:
            vus[cle] = m
    return [m for m in mots if vus[(m["kanji"], m["lecture"])] is m]


def variantes(champ):
    """« 会う, 逢う » ou « ～円 » → ['会う', '逢う'] / ['円']."""
    out = []
    for v in re.split(r"[,、;／/]", champ or ""):
        v = re.sub(r"\(.*?\)|（.*?）", "", v).strip().strip("～〜~").strip()
        if v:
            out.append(v)
    return out


def index_niveaux(mots):
    """forme (kanji ou kana) → rang le plus facile où elle apparaît."""
    idx = {}
    for m in mots:
        r = RANG[m["niveau"]]
        for f in variantes(m["kanji"]) + variantes(m["lecture"]):
            if r > idx.get(f, -1):
                idx[f] = r
    return idx


# --------------------------------------------------------------------------
# Tatoeba
# --------------------------------------------------------------------------

def lire_tsv(chemin):
    with open(chemin, encoding="utf-8", newline="") as f:
        for ligne in f:
            yield ligne.rstrip("\n").split("\t")


def charger_phrases(chemins):
    phrases = {"jpn": {}, "fra": {}, "eng": {}}
    deja = set()
    for lang, chemin in chemins.items():
        if chemin in deja:
            continue
        deja.add(chemin)
        for c in lire_tsv(chemin):
            if len(c) < 3 or c[1] not in phrases:
                continue
            auteur = c[3] if len(c) > 3 and c[3] not in ("", "\\N") else None
            phrases[c[1]][int(c[0])] = (c[2], auteur)
    return phrases


def charger_liens(chemin, phrases):
    jpn, fra, eng = phrases["jpn"], phrases["fra"], phrases["eng"]
    j_fr, j_en, en_fr = defaultdict(set), defaultdict(set), defaultdict(set)
    for c in lire_tsv(chemin):
        if len(c) < 2:
            continue
        a, b = int(c[0]), int(c[1])
        if a in jpn:
            if b in fra:
                j_fr[a].add(b)
            elif b in eng:
                j_en[a].add(b)
        elif a in eng and b in fra:
            en_fr[a].add(b)
    return j_fr, j_en, en_fr


def charger_tags(chemin):
    douteux = defaultdict(set)
    if not chemin:
        return douteux
    for c in lire_tsv(chemin):
        if len(c) >= 2 and c[1].strip().lower() in TAGS_DOUTEUX:
            douteux[int(c[0])].add(c[1].strip())
    return douteux


def charger_notes(chemin):
    """Phrases qu'au moins un contributeur a marquées « pas correcte » (-1)."""
    mauvaises = set()
    if not chemin:
        return mauvaises
    for c in lire_tsv(chemin):
        # Format documenté : utilisateur, id de phrase, note (-1/0/1), dates.
        try:
            sid, note = int(c[1]), int(c[2])
        except (IndexError, ValueError):
            continue
        if note < 0:
            mauvaises.add(sid)
    return mauvaises


# Une unité de ligne B : mot(lecture)[sens]{forme}~
UNITE = re.compile(
    r"^(?P<mot>[^(\[{~|]+)"
    r"(?:\((?P<lecture>[^)]*)\))?"
    r"(?:\[(?P<sens>\d+)\])?"
    r"(?:\{(?P<forme>[^}]*)\})?"
    r"(?P<verifie>~)?$"
)


def analyser_ligne_b(texte):
    unites = []
    for brut in texte.split():
        brut = brut.replace("|", "")  # « |1 » : numéro d'ordre parfois ajouté
        m = UNITE.match(brut)
        if not m:
            unites.append({"mot": brut, "lecture": None, "forme": None, "verifie": False})
            continue
        unites.append({"mot": m["mot"], "lecture": m["lecture"], "forme": m["forme"],
                       "verifie": bool(m["verifie"])})
    return unites


def charger_indices(chemin):
    """jpn_indices : id de phrase japonaise → unités de la ligne B.

    Format (doc Tatoeba) : id de phrase, id de « sens » (la phrase anglaise du
    corpus Tanaka, -1 si inconnue), puis la ligne B.
    """
    indices = {}
    for c in lire_tsv(chemin):
        if len(c) < 3:
            continue
        try:
            indices[int(c[0])] = analyser_ligne_b(c[2])
        except ValueError:
            continue
    return indices


# --------------------------------------------------------------------------
# Choix des phrases
# --------------------------------------------------------------------------

def longueur(texte):
    return len(JA_CARACTERE.findall(texte))


def niveau_unite(u, idx):
    """Rang JLPT d'une unité de ligne B, ou None si elle est grammaticale."""
    if u["mot"] in GRAMMATICAUX or re.fullmatch(r"[\d０-９.,]+", u["mot"]):
        return None
    for f in (u["mot"], u["lecture"]):
        if f and f in idx:
            return idx[f]
    if KANA.match(u["mot"]) and len(u["mot"]) <= 2:
        return None  # petit mot en kana hors liste : presque toujours grammatical
    return 0


def nom_rang(r):
    if r < 0:
        return "inconnu (phrase non indexée)"
    return {v: k for k, v in RANG.items()}[r]


def correspond(u, formes_mot, lectures):
    if u["mot"] not in formes_mot:
        return False
    # Si la ligne B précise une lecture (方(かた) / 方(ほう)), elle doit concorder.
    if u["lecture"] and lectures and u["lecture"] not in lectures:
        return False
    return True


def construire(args):
    brut = os.path.abspath(args.brut)
    os.makedirs(brut, exist_ok=True)

    print("Listes JLPT…", flush=True)
    mots = charger_listes(brut, args.hors_ligne)
    idx = index_niveaux(mots)
    compte = {n: sum(m["niveau"] == n for m in mots) for n in NIVEAUX}
    print(f"  {len(mots)} mots (" + ", ".join(f"{n} : {c}" for n, c in compte.items()) + ")")
    donnees = lire_mots_donnees()
    if donnees is not None:
        print("  (japonais/mots.json de japonais-donnees trouvé : non utilisé pour la liste, "
              "les listes de tanos font foi ici)")

    print("Exports Tatoeba…", flush=True)
    chemins_phrases = obtenir_phrases(brut, args.hors_ligne)
    chemins = {n: obtenir_export(brut, n, args.hors_ligne) for n in EXPORTS if "sentences" not in n}
    for n, c in chemins.items():
        if not c and n not in FACULTATIFS:
            raise SystemExit(f"Export obligatoire introuvable : {n}")

    phrases = charger_phrases(chemins_phrases)
    print(f"  phrases : {', '.join(f'{k} {len(v)}' for k, v in phrases.items())}")
    j_fr, j_en, en_fr = charger_liens(chemins["links.csv"], phrases)
    indices = charger_indices(chemins["jpn_indices.csv"])
    douteux = charger_tags(chemins.get("tags.csv"))
    mal_notees = charger_notes(chemins.get("user_sentences.csv"))
    print(f"  indices {len(indices)}, tags douteux {len(douteux)}, notées -1 {len(mal_notees)}")

    # Index inverse : forme de dictionnaire → phrases qui la contiennent.
    par_mot, par_lecture = defaultdict(list), defaultdict(list)
    for sid, unites in indices.items():
        if sid not in phrases["jpn"]:
            continue
        for u in unites:
            par_mot[u["mot"]].append((sid, u))
            # Un mot que la liste donne en kana (りんご) est souvent indexé
            # sous sa forme kanji avec sa lecture : 林檎(りんご){りんご}.
            if u["lecture"]:
                par_lecture[u["lecture"]].append((sid, u))

    stats_filtre = defaultdict(int)
    cache_eval = {}

    def evaluer(sid, mot_cible):
        """Caractéristiques d'une phrase, ou None si elle est écartée."""
        cle = (sid, mot_cible["kanji"], mot_cible["lecture"])
        if cle in cache_eval:
            return cache_eval[cle]
        ja, auteur_ja = phrases["jpn"][sid]
        res = None
        formes_cible = set(variantes(mot_cible["kanji"]) + variantes(mot_cible["lecture"]))
        if sid in douteux:
            stats_filtre["étiquette douteuse"] += 1
        elif sid in mal_notees:
            stats_filtre["notée incorrecte"] += 1
        elif any(m in ja and not any(m in f for f in formes_cible) for m in ECARTER_JA):
            stats_filtre["vocabulaire écarté (japonais)"] += 1
        else:
            fr_direct = sorted(j_fr.get(sid, ()))
            en = sorted(j_en.get(sid, ()))
            fr_indirect = sorted({f for e in en for f in en_fr.get(e, ())} - set(fr_direct))
            fr_ids = fr_direct or fr_indirect
            textes = [phrases["fra"][i][0] for i in fr_ids] + [phrases["eng"][i][0] for i in en]
            if not fr_ids:
                stats_filtre["sans français"] += 1
            elif any(ECARTER_TRAD.search(t) for t in textes):
                stats_filtre["vocabulaire écarté (traduction)"] += 1
            else:
                # On préfère une traduction non douteuse elle-même.
                fr_ids = sorted(fr_ids, key=lambda i: (i in douteux or i in mal_notees, i))
                en = sorted(en, key=lambda i: (i in douteux or i in mal_notees, i))
                rangs = [r for r in (niveau_unite(u, idx) for u in indices.get(sid, [])
                                     if u["mot"] not in formes_cible and u["lecture"] not in formes_cible)
                         if r is not None]
                res = {
                    "ja": ja, "auteur_ja": auteur_ja, "id_ja": sid,
                    "fr_ids": fr_ids, "fr_direct": bool(fr_direct),
                    "en_ids": en, "longueur": longueur(ja),
                    # Phrase absente de jpn_indices : niveau inconnu (-1), jamais « facile » par défaut.
                    "rang_max": (min(rangs) if rangs else 5) if sid in indices else -1,
                    "hors_liste": sum(1 for r in rangs if r == 0),
                    "penalite": any(p in ja for p in PENALITE_JA),
                }
        cache_eval[cle] = res
        return res

    sortie = []
    for m in mots:
        formes = variantes(m["kanji"]) or variantes(m["lecture"])
        lectures = set(variantes(m["lecture"]))
        if not variantes(m["kanji"]):
            formes = list(lectures)
        trouvees = {}
        for f in formes:
            for sid, u in par_mot.get(f, ()):
                if correspond(u, set(formes), lectures) and sid not in trouvees:
                    trouvees[sid] = "jpn_indices" + (" (vérifié ~)" if u["verifie"] else "")
        if not variantes(m["kanji"]):
            for f in lectures:
                for sid, u in par_lecture.get(f, ()):
                    # La forme écrite dans la phrase doit rester en kana.
                    if sid not in trouvees and (u["forme"] or "").startswith(f[:1]):
                        trouvees[sid] = "jpn_indices (lecture)" + (" (vérifié ~)" if u["verifie"] else "")
        def retenir(sids_modes):
            out = []
            for sid, mode in sids_modes.items():
                e = evaluer(sid, m)
                if e is not None and e["en_ids"]:
                    out.append(dict(e, mode=mode))
            return out

        evaluees = retenir(trouvees)
        if not evaluees:
            # Dernier recours : la forme exacte dans le texte, notée comme telle.
            sous_chaine = {}
            for f in formes:
                if len(f) < 2:
                    continue  # une sous-chaîne d'un seul caractère ne prouve rien
                for sid, (ja, _) in phrases["jpn"].items():
                    if f in ja and sid not in trouvees and sid not in sous_chaine:
                        sous_chaine[sid] = "forme exacte (sous-chaîne, non vérifié)"
            evaluees = retenir(sous_chaine)
            trouvees.update(sous_chaine)

        rang_mot = RANG[m["niveau"]]

        def cle_tri(e):
            hors_plage = max(LONGUEUR_MIN - e["longueur"], e["longueur"] - LONGUEUR_MAX, 0)
            return (
                not e["fr_direct"],
                e["rang_max"] < rang_mot,  # un mot plus difficile que le mot cible
                e["mode"].startswith("forme exacte"),
                hors_plage > 0,
                e["penalite"],
                "vérifié" not in e["mode"],
                hors_plage,
                abs(e["longueur"] - 12),
                e["id_ja"],
            )

        evaluees.sort(key=cle_tri)
        candidates = []
        for e in evaluees[:MAX_CANDIDATES]:
            candidates.append({
                "japonais": e["ja"],
                "francais": phrases["fra"][e["fr_ids"][0]][0],
                "anglais": phrases["eng"][e["en_ids"][0]][0],
                "francais_direct": e["fr_direct"],
                "ids_tatoeba": {"jpn": e["id_ja"], "fra": e["fr_ids"][0], "eng": e["en_ids"][0]},
                "auteurs": {
                    "jpn": e["auteur_ja"],
                    "fra": phrases["fra"][e["fr_ids"][0]][1],
                    "eng": phrases["eng"][e["en_ids"][0]][1],
                },
                "longueur": e["longueur"],
                "niveau_mot_le_plus_difficile": nom_rang(e["rang_max"]),
                "mots_hors_liste": e["hors_liste"],
                "niveau_respecte": e["rang_max"] >= rang_mot,
                "longueur_dans_la_cible": LONGUEUR_MIN <= e["longueur"] <= LONGUEUR_MAX,
                "appariement": e["mode"],
            })
        sortie.append({
            "niveau": m["niveau"], "mot": m["mot"], "lecture": m["lecture"],
            "anglais_liste": m["anglais"], "phrases_trouvees": len(trouvees),
            "phrases_retenables": len(evaluees), "candidates": candidates,
        })

    meta = {
        "genere_le": datetime.date.today().isoformat(),
        "sources": {
            "vocabulaire": "Listes JLPT de Jonathan Waller, https://www.tanos.co.uk/jlpt/ (CC BY)",
            "phrases": "Tatoeba, https://tatoeba.org (CC BY 2.0 FR) — exports " + TATOEBA,
        },
        "criteres": {
            "longueur_cible": [LONGUEUR_MIN, LONGUEUR_MAX],
            "max_candidates": MAX_CANDIDATES,
            "filtres": dict(stats_filtre),
        },
    }
    with open(os.path.join(ICI, "phrases.json"), "w", encoding="utf-8") as f:
        json.dump({"meta": meta, "mots": sortie}, f, ensure_ascii=False, indent=1)
    ecrire_rapport(sortie, meta, args.graine)
    print("phrases.json et RAPPORT.md écrits.")


# --------------------------------------------------------------------------
# Rapport
# --------------------------------------------------------------------------

def categorie(entree):
    if any(c["francais_direct"] for c in entree["candidates"]):
        return "direct"
    if entree["candidates"]:
        return "indirect"
    return "aucune"


def pct(a, b):
    return f"{100 * a / b:.0f} %" if b else "—"


def ecrire_rapport(sortie, meta, graine):
    L = ["# Phrases d'exemple Tatoeba pour le vocabulaire JLPT N5–N3", "",
         f"Généré le {meta['genere_le']} par `construire.py`. Aucune phrase n'est traduite ni inventée : "
         "seules des traductions humaines de Tatoeba sont retenues.", "",
         "## Couverture par niveau", "",
         "| Niveau | Mots | Français direct | Français indirect seulement | Aucune phrase | "
         "Direct + niveau respecté + 6–20 car. |",
         "|---|---:|---:|---:|---:|---:|"]
    for n in NIVEAUX + ["Total"]:
        es = [e for e in sortie if n == "Total" or e["niveau"] == n]
        t = len(es)
        d = sum(categorie(e) == "direct" for e in es)
        i = sum(categorie(e) == "indirect" for e in es)
        a = sum(categorie(e) == "aucune" for e in es)
        ideal = sum(any(c["francais_direct"] and c["niveau_respecte"] and c["longueur_dans_la_cible"]
                        for c in e["candidates"]) for e in es)
        L.append(f"| {n} | {t} | {d} ({pct(d, t)}) | {i} ({pct(i, t)}) | {a} ({pct(a, t)}) | "
                 f"{ideal} ({pct(ideal, t)}) |")
    L += ["",
          "- **Français direct** : au moins une candidate dont la phrase française est liée directement "
          "à la phrase japonaise dans Tatoeba.",
          "- **Français indirect seulement** : le français n'est relié qu'en passant par la phrase anglaise "
          "(japonais → anglais → français) ; le sens peut avoir dérivé à chaque étape.",
          "- **Dernière colonne** : la candidate idéale pour un apprenant (français direct, aucun autre mot "
          "plus difficile que le niveau du mot, longueur 6 à 20 caractères japonais).",
          "", "## Phrases écartées par les filtres", ""]
    for k, v in sorted(meta["criteres"]["filtres"].items(), key=lambda kv: -kv[1]):
        L.append(f"- {k} : {v}")
    sans = sum(1 for e in sortie if e["phrases_trouvees"] == 0)
    sous = sum(1 for e in sortie if any(c["appariement"].startswith("forme exacte") for c in e["candidates"]))
    L += ["", f"Mots absents de `jpn_indices` et de toute phrase : {sans}. "
          f"Mots dont une candidate n'a été trouvée que par sous-chaîne (à vérifier) : {sous}.", "",
          "## Vingt exemples tirés au hasard", "",
          f"Tirage reproductible (graine {graine}) parmi les mots qui ont au moins une candidate.", ""]
    rnd = random.Random(graine)
    avec = [e for e in sortie if e["candidates"]]
    for e in rnd.sample(avec, min(20, len(avec))):
        c = e["candidates"][0]
        L += [f"**{e['mot']}** ({e['lecture']}, {e['niveau']}) — #{c['ids_tatoeba']['jpn']}",
              f"- {c['japonais']}",
              f"- {c['francais']}" + ("" if c["francais_direct"] else " *(français indirect)*"),
              f"- {c['anglais']}",
              f"- {c['longueur']} car., mot le plus difficile : {c['niveau_mot_le_plus_difficile']}, "
              f"appariement : {c['appariement']}", ""]
    L += ["## Limites", "",
          "- Le filtre de contenu est lexical : il écarte des mots (violence, sexe, politique, religion, "
          "vulgarité), il ne juge pas le sens. Une phrase étrange mais polie passe.",
          "- Le niveau des autres mots vient des listes N5–N3 ; un mot hors de ces listes compte comme "
          "« hors liste » (plus difficile que N3). Les particules et auxiliaires sont ignorés.",
          "- `jpn_indices` ne couvre qu'une partie des phrases japonaises (surtout l'ancien corpus Tanaka). "
          "Les phrases récentes n'y sont pas indexées.",
          "- Les phrases autour de « Tom » et « Mary » sont gardées mais classées après les autres.", ""]
    with open(os.path.join(ICI, "RAPPORT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--brut", default=os.path.join(ICI, "brut"), help="dossier des exports bruts")
    p.add_argument("--hors-ligne", action="store_true", help="ne rien télécharger")
    p.add_argument("--graine", type=int, default=2026, help="graine du tirage des 20 exemples")
    construire(p.parse_args())


if __name__ == "__main__":
    main()
