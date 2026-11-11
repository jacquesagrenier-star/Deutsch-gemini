# -*- coding: utf-8 -*-
"""Convertit les dictionnaires WikDict portugais (SQLite) en paquets JSON servables.

    python portugais/outils/dicc_construire.py            # les deux paires
    python portugais/outils/dicc_construire.py pt-fr

Le pendant portugais d'espanol/dicc_construire.py, dont il reprend le format a
l'identique (le moteur lit les deux de la meme facon). Sortie :
portugais/datos/dicc/pt-fr/ et fr-pt/, partages par le Portugal et le Bresil
(le Wiktionnaire ne separe pas les deux variantes ; « train » rend « trem |
comboio »). FICHIERS DERIVES, jamais a la main.

D'OU VIENNENT LES DONNEES (accord de Jacques, 11 nov. 2026, decisions/
DECISIONS.md : « Oui, telecharge »)
    WikDict (Wiktionnaire via DBnary), **CC BY-SA 4.0**, telecharge depuis
    https://download.wikdict.com/dictionaries/sqlite/2/ (pt-fr.sqlite3 et
    fr-pt.sqlite3, version du 23 juin 2026). Les SQLite restent HORS du depot
    et de OneDrive : C:/Users/jacqu/.wortando/wikdict-pt (ou WIKDICT_PT).

    NE PAS changer de source a la legere. FreeDict publie les memes paires et
    sort en premier quand on cherche, mais plusieurs de ses dictionnaires sont
    sous AGPLv3 -- une licence ecrite precisement pour atteindre les
    applications servies par reseau, soit l'inverse de ce qu'il faut a un
    produit payant. La ligne d'attribution affichee sous les resultats
    (dict_credit) et la carte « Credits » sont une obligation de la licence,
    pas une decoration. Les adaptations sont decrites dans
    portugais/datos/dicc/LICENSE.txt, comme l'exige le « partage dans les
    memes conditions ».

LE DECOUPAGE EST PAR TAILLE, pas par lettre initiale (paquets de 120 Ko au
plus) ; index.json liste le premier mot normalise de chaque paquet, et le
client y cherche par dichotomie.

CE QUI DIFFERE DE L'ESPAGNOL
    - L'ORDRE DES TRADUCTIONS suit l'ordre des sens du Wiktionnaire
      (sense_num) : « maison » rendait « habitacao · vivenda · casa · lar »
      (l'ordre des lignes de la base, sans garantie), il rend maintenant
      « casa · lar · habitacao · vivenda ». Pas de tri par frequence : en
      allemand, il cassait une entree sur quatre (voir DICT_REGIONAL dans
      index.html).
    - LE GENRE n'est pas dans le Wiktionnaire portugais de WikDict
      (« por/casa__Substantivo__1 », sans masculin ni feminin). Il est greffe
      depuis NOTRE corpus (portugais/datos et datos-br, themes.json), seulement
      quand les deux variantes s'accordent : « o » / « a » devant le mot
      portugais (pt-fr), liste `tg` alignee sur les traductions (fr-pt).
      Un nom absent du corpus reste sans article, plutot qu'un article devine.
    - Les affixes (« -cao », « anti- ») sont ecartes, comme en allemand
      (signale par une usagere le 5 sept. 2026 : ce ne sont pas des mots).
"""
import io, json, os, re, sqlite3, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SORTIE = os.path.join(RACINE, "portugais", "datos", "dicc")
SOURCE = os.environ.get("WIKDICT_PT") or "C:/Users/jacqu/.wortando/wikdict-pt"
TAILLE_PAQUET = 120 * 1024
MAX_TRAD = 8          # au-dela, la fiche devient illisible

# Classes : le Wiktionnaire portugais (pt-fr) puis le francais (fr-pt).
CLASSES = [("substantivo", "n"), ("verbo", "v"), ("adjetivo", "adj"),
           ("advérbio", "adv"), ("preposição", "prep"), ("pronome", "pron"),
           ("conjunção", "conj"), ("interjeição", "interj"),
           ("__nom__", "n"), ("__verb__", "v"), ("__adj__", "adj"), ("__adv__", "adv"),
           ("préposition", "prep"), ("pronom", "pron"), ("conjonction", "conj"),
           ("interjection", "interj")]


def normaliser(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]", "", s)


def genres_du_corpus():
    """mot portugais (minuscule) -> « o » / « a », la ou les deux variantes s'accordent."""
    vus = {}
    for dossier in ("datos", "datos-br"):
        chemin = os.path.join(RACINE, "portugais", dossier, "themes.json")
        for t in json.load(io.open(chemin, encoding="utf-8"))["themes"]:
            for m in t["mots"]:
                g = (m.get("genre") or "").lower()
                if g in ("o", "a"):
                    vus.setdefault(m["mot"].lower(), set()).add(g)
    return {m: next(iter(g)) for m, g in vus.items() if len(g) == 1}


def lire(paire):
    """Reunit tous les sens d'un meme mot en une seule fiche, dans l'ordre des sens."""
    db = sqlite3.connect(os.path.join(SOURCE, paire + ".sqlite3"))
    fiches = {}
    lignes = db.execute(
        "SELECT lexentry, written_rep, trans_list, importance FROM translation "
        "ORDER BY written_rep, lexentry, sense_num IS NULL, CAST(sense_num AS INTEGER), sense_num")
    for lexentry, ecrit, traductions, importance in lignes:
        if not ecrit or not traductions:
            continue
        ecrit = ecrit.strip()
        if not ecrit or len(ecrit) > 40 or ecrit.startswith("-") or ecrit.endswith("-"):
            continue
        f = fiches.setdefault(ecrit, {"m": ecrit, "t": [], "r": 0.0})
        for t in traductions.split(" | "):
            t = t.strip()
            if t and t not in f["t"] and not t.startswith("-") and not t.endswith("-"):
                f["t"].append(t)
        f["r"] = max(f["r"], round(importance or 0.0, 2))
        marque = (lexentry or "").lower()
        if "p" not in f:
            for long_, court in CLASSES:
                if long_ in marque:
                    f["p"] = court
                    break
    db.close()
    for f in fiches.values():
        f["t"] = f["t"][:MAX_TRAD]
    return sorted((f for f in fiches.values() if f["t"]),
                  key=lambda f: (normaliser(f["m"]), f["m"]))


def greffer_genre_pt(fiches, genres):
    """pt-fr : l'article devant le nom portugais, quand notre corpus le connait."""
    n = 0
    for f in fiches:
        g = genres.get(f["m"].lower())
        if g and f.get("p", "n") == "n":
            f["g"] = g
            n += 1
    print("        genre greffe sur %d fiches pt-fr" % n)
    return fiches


def greffer_genre_fr(fiches, genres):
    """fr-pt : `tg`, alignee sur `t`, chaine vide la ou le genre est inconnu."""
    n = 0
    for f in fiches:
        if f.get("p") not in (None, "n"):
            continue
        arts = [genres.get(t.lower(), "") for t in f["t"]]
        if any(arts):
            f["tg"] = arts
            n += 1
    print("        genre greffe sur %d fiches fr-pt" % n)
    return fiches


def ecrire(paire, fiches):
    destination = os.path.join(SORTIE, paire)
    if os.path.isdir(destination):
        for v in os.listdir(destination):
            os.remove(os.path.join(destination, v))
    else:
        os.makedirs(destination)

    paquets, courant, poids = [], [], 0
    for f in fiches:
        ligne = json.dumps(f, ensure_ascii=False, separators=(",", ":"))
        if courant and poids + len(ligne.encode("utf-8")) > TAILLE_PAQUET:
            paquets.append(courant); courant, poids = [], 0
        courant.append(f); poids += len(ligne.encode("utf-8")) + 1
    if courant:
        paquets.append(courant)

    bornes = []
    for i, p in enumerate(paquets):
        bornes.append(normaliser(p[0]["m"]))
        io.open(os.path.join(destination, "%03d.json" % i), "w",
                encoding="utf-8", newline="\n").write(
            json.dumps(p, ensure_ascii=False, separators=(",", ":")))
    io.open(os.path.join(destination, "index.json"), "w",
            encoding="utf-8", newline="\n").write(
        json.dumps(bornes, ensure_ascii=False, separators=(",", ":")))

    fichiers = os.listdir(destination)
    poids = sum(os.path.getsize(os.path.join(destination, v)) for v in fichiers)
    plus_gros = max(os.path.getsize(os.path.join(destination, v)) for v in fichiers)
    avec_genre = sum(1 for f in fiches if "g" in f or "tg" in f)
    print("%-7s %6d mots  %3d paquets  %5.1f Mo  plus gros %5.1f Ko  %d avec genre"
          % (paire, len(fiches), len(paquets), poids / 1048576, plus_gros / 1024, avec_genre))


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    voulu = set(sys.argv[1:]) or {"pt-fr", "fr-pt"}
    genres = genres_du_corpus()
    print("        %d noms du corpus au genre sur" % len(genres))
    if "pt-fr" in voulu:
        ecrire("pt-fr", greffer_genre_pt(lire("pt-fr"), genres))
    if "fr-pt" in voulu:
        ecrire("fr-pt", greffer_genre_fr(lire("fr-pt"), genres))
