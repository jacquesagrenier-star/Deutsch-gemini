# -*- coding: utf-8 -*-
"""Classe les entrees espagnoles par frequence d'usage, a partir de Leipzig.

    python espanol/frequence.py            -- le rapport, sans rien ecrire
    python espanol/frequence.py --ecrire   -- ecrit espanol/datos/frequence.json

Le pendant espagnol de tests/frequence.py (l'allemand) et d'anglais/outils/
frequence.py : meme format de sortie, memes principes. FICHIER DERIVE, jamais a
la main ; a relancer apres un ajout au corpus (ajouter_mots.py).

POURQUOI (6 nov. 2026, decision 34d02c3, recommandation 4 de la maquette du test
de niveau) : le test de niveau tire ses mots dans les rangs moyens de chaque
niveau, ni les tout premiers ni les plus rares. L'espagnol n'avait pas de
classement. ⚠️ LA SEANCE DU JOUR ESPAGNOLE NE LE LIT PAS (chargerFrequence()
rend un classement vide en espagnol, comme avant) : l'ordre des mots neufs de
l'espagnol ne change pas tant que Jacques ne l'a pas decide.

D'OU VIENNENT LES DONNEES, ET CE QUE LA LICENCE OBLIGE
    Leipzig Corpora Collection, sous CC BY : usage commercial permis,
    attribution obligatoire (carte « Credits », cle credits_freq, la meme que
    pour l'allemand).

        (c) Universitat Leipzig / Sachsische Akademie der Wissenschaften / InfAI

    Trois corpus, comme l'allemand, chacun ramene a une frequence PAR MILLION
    avant d'etre additionne (sinon le plus gros deciderait seul) :
        spa_news_2023_300K        la presse recente (Espagne et Amerique latine)
        spa_web_2016_300K         le web : un registre plus courant que la presse
        spa_opensubtitles_2018    les sous-titres OPUS OpenSubtitles 2018 (Lison &
                                  Tiedemann 2016), de la langue PARLEE -- sans eux
                                  la presse hisserait « gobierno » au-dessus de
                                  « agua », comme « Regierung » devant « Wasser »
    Leipzig n'a pas de sous-titres espagnols : la liste d'OPUS
    (object.pouta.csc.fi/OPUS-OpenSubtitles/v2018/freq/es.freq.gz, repliee en
    minuscules) est remise au format de Leipzig, les 400 000 premieres formes.
    SUBTLEX-ESP reste ecarte pour la meme raison que SUBTLEX-DE : licence non
    commerciale.

    Les archives vivent HORS DU DEPOT et de OneDrive
    (C:/Users/jacqu/.wortando/frequence-es) ; seul le classement derive est versionne.

CE QUI EST MESURE
    - Un mot seul : la somme des formes qu'on possede, en minuscules (l'espagnol
      n'a pas la majuscule des noms allemands) : le pluriel d'un nom ; le
      feminin et les pluriels d'un adjectif ; pour un verbe, l'infinitif et
      toutes les formes conjuguees de verbos.json (present, pretérito,
      imperfecto, futur, conditionnel, subjonctif, imperatif, participe), sans
      le pronom (« me levanto » compte « levanto »).
    - Deux mots (« tarjeta sanitaria », « tener que ») : les cooccurrences de
      mots voisins de Leipzig (fichier -co_n) ; trois mots ou plus : le
      minimum des paires voisines, une borne haute.

⚠️ LES HOMOGRAPHES : « trabajo » est un nom ET « je travaille », « cuenta » un
    nom ET « il compte ». Le singulier prendrait la masse du verbe. Pour un nom
    dont le singulier est aussi une forme d'un de nos verbes ou le mot-vedette
    d'une autre categorie, on mesure son PLURIEL seul (« trabajos », une forme
    qui n'appartient qu'au nom), multiplie par le rapport median
    (singulier + pluriel) / pluriel des noms sans homographe. C'est une
    estimation annoncee, pas une mesure. Un nom sans pluriel distinct
    (« la crisis ») garde sa masse, partagee avec ses homographes.
    Adjectifs, adverbes et mots-outils qui partagent un mot-vedette (« bajo »,
    « claro ») se partagent la masse a parts egales, comme en anglais.

⚠️ ON NE CLASSE QU'A L'INTERIEUR D'UNE CATEGORIE, jamais entre deux, et le
niveau CECR reste l'organisateur principal (voir CLAUDE.md, « frequence.json »).
Pas de « palier » de liste officielle, contrairement a l'allemand : le PCIC de
l'Instituto Cervantes n'est pas redistribuable ici.
"""
import argparse, io, json, os, re, statistics, sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")
SOURCE = "C:/Users/jacqu/.wortando/frequence-es"
CORPUS = ["spa_news_2023_300K", "spa_web_2016_300K", "spa_opensubtitles_2018"]
PRONOMS = {"me", "te", "se", "nos", "os"}
AUXILIAIRES = {"he", "has", "ha", "hemos", "habéis", "han"}


def charger():
    """(forme minuscule -> par million, (forme1, forme2) -> par million)."""
    mots, paires = {}, {}
    for nom in CORPUS:
        base = os.path.join(SOURCE, nom, nom)
        if not os.path.exists(base + "-words.txt"):
            sys.exit("  Corpus absent : %s-words.txt (voir le haut du script)" % base)
        ids, brut, total = {}, {}, 0
        with io.open(base + "-words.txt", encoding="utf-8") as f:
            for ligne in f:
                p = ligne.rstrip("\n").split("\t")
                if len(p) < 3 or not p[2].isdigit():
                    continue
                m = p[1].lower()
                ids[p[0]] = m
                brut[m] = brut.get(m, 0) + int(p[2])
                total += int(p[2])
        for m, n in brut.items():
            mots[m] = mots.get(m, 0.0) + n * 1e6 / total
        npaires = 0
        if os.path.exists(base + "-co_n.txt"):
            with io.open(base + "-co_n.txt", encoding="utf-8") as f:
                for ligne in f:
                    p = ligne.split("\t")
                    if len(p) < 3 or p[0] not in ids or p[1] not in ids:
                        continue
                    k = (ids[p[0]], ids[p[1]])
                    paires[k] = paires.get(k, 0.0) + int(p[2]) * 1e6 / total
                    npaires += 1
        print("  %-26s %7d formes, %10d occurrences, %8d paires" % (nom, len(brut), total, npaires))
    return mots, paires


def jetons(s):
    return [x for x in re.findall(r"[a-záéíóúüñ0-9]+", (s or "").lower()) if x]


def variantes(s):
    """« el/la periodista », « pelirrojo / pelirroja » : chaque morceau compte."""
    return [p.strip() for p in re.split(r"\s*/\s*", s or "") if p.strip()]


def mesure(mots, paires, formes):
    total, vues = 0.0, set()
    for brut in formes:
        for f in variantes(brut):
            f = re.sub(r"\s*\(.*?\)", "", f).strip()
            j = tuple(jetons(f))
            if not j or j in vues:
                continue
            vues.add(j)
            if len(j) == 1:
                total += mots.get(j[0], 0.0)
            else:
                total += min(paires.get((a, b), 0.0) for a, b in zip(j, j[1:]))
    return total


def sans_pronom(forme):
    """« me levanto » -> « levanto » ; « he vivido » -> « vivido » ;
    « me doy cuenta » -> « doy cuenta »."""
    t = forme.split()
    while len(t) > 1 and (t[0] in PRONOMS or t[0] in AUXILIAIRES):
        t = t[1:]
    return " ".join(t)


def formes_verbe(e):
    inf = e.get("infinitif") or e.get("mot") or ""
    out = [inf]
    for cle in ("praesens", "preterito", "imperfecto", "futuro", "condicional", "subjuntivo", "imperativo", "perfecto"):
        v = e.get(cle)
        vals = v.values() if isinstance(v, dict) else (v or [])
        for x in vals:
            if isinstance(x, str) and x.strip() and x.strip() not in ("—", "-"):
                out.append(sans_pronom(x.strip().lower()))
    return out


def formes_adjectif(e):
    m = (e.get("mot") or "").lower()
    fem = (e.get("feminin") or m).lower()
    out = [m, fem]
    for x in {m, fem}:
        if " " in x:
            continue
        out.append(x + ("es" if re.search(r"[^aeiouáéíóú]$", x) else "s"))
    return out


def entrees():
    def lire(n):
        return json.load(io.open(os.path.join(DATOS, n), encoding="utf-8"))
    out = {"noms": [], "verbes": [], "adjectifs": [], "adverbes": [], "mots-outils": [], "expressions": []}
    for t in lire("temas.json")["themes"]:
        for m in t["mots"]:
            out["noms"].append((m["mot"], t.get("niveau"), [m["mot"].lower(), (m.get("pluriel") or "").lower()]))
            ARTICLES[(m["mot"], t.get("niveau"))] = (m.get("genre") or "").lower()
    for niv, l in lire("verbos.json").items():
        if niv.startswith("_"):
            continue
        for e in l:
            out["verbes"].append((e.get("infinitif") or e["mot"], niv, formes_verbe(e)))
    for nom, cle in (("adjetivos.json", "adjectifs"), ("adverbios.json", "adverbes"),
                     ("expresiones.json", "expressions"), ("funcionales.json", "mots-outils")):
        for niv, l in lire(nom).items():
            if niv.startswith("_"):
                continue
            for e in l:
                formes = formes_adjectif(e) if cle == "adjectifs" else [e["mot"].lower()]
                out[cle].append((e["mot"], niv, formes))
    return out


PARTAGEES = ("adjectifs", "adverbes", "mots-outils")
ARTICLES = {}   # (mot, niveau) -> « el » / « la » : la paire article + nom des homographes sans pluriel
# Des mots-outils tres frequents qui ne sont pas des mots-vedettes de
# funcionales.json (on n'y a que « esta », pas « este ») : sans eux, le nom
# « el este » (l'est) ouvrait le classement des noms A2.
HORS_LISTE = {"este", "esto", "estos"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ecrire", action="store_true")
    a = ap.parse_args()
    mots, paires = charger()
    es = entrees()
    # ⚠️ LES FORMES VERBALES QUI SONT AUSSI DES MOTS D'UNE AUTRE CATEGORIE : « una »
    # (unir), « para » (parar), « como » (comer), « sobre » (sobrar) prenaient
    # la masse de l'article, de la preposition, de la conjonction -- « unir »
    # et « parar » finissaient deuxieme et troisieme des verbes. Une forme
    # conjuguee qui est le mot-vedette d'une autre categorie (ou un mot-outil
    # quelconque) ne compte pas pour le verbe ; l'infinitif compte toujours.
    formes_verbales = {f for _, _, fo in es["verbes"] for f in fo[1:] if " " not in f}
    autres = {m.lower() for cat, l in es.items() if cat != "verbes" for m, _, _ in l} | HORS_LISTE
    autres |= {f for cat in ("mots-outils", "adverbes") for _, _, fo in es[cat] for f in fo}
    es["verbes"] = [(m, niv, [fo[0]] + [f for f in fo[1:] if f not in autres]) for m, niv, fo in es["verbes"]]

    # Les homographes des noms : formes de nos verbes (AVANT le filtre ci-dessus),
    # mots-vedettes des autres categories, et les mots-outils hors liste.
    formes_verbales |= HORS_LISTE
    vedettes = {}
    for cat, liste in es.items():
        for m, niv, fo in liste:
            vedettes.setdefault(m.lower(), set()).add(cat)
    rapports = []
    for m, niv, fo in es["noms"]:
        sg, pl = fo[0], fo[1] if len(fo) > 1 else ""
        if " " in sg or not pl or pl == sg or sg in formes_verbales or (vedettes.get(sg, set()) - {"noms"}):
            continue
        fpl = mots.get(pl, 0.0)
        if fpl > 0:
            rapports.append((mots.get(sg, 0.0) + fpl) / fpl)
    rapport = statistics.median(rapports) if rapports else 1.0
    # Et pour un homographe SANS pluriel distinct (« el este », l'est) : la paire
    # article + nom de Leipzig, multipliee par le rapport median masse / paire
    # des noms sans homographe. Une forme qui n'appartient qu'au nom.
    rapports_art = []
    for m, niv, fo in es["noms"]:
        sg, art = fo[0], ARTICLES.get((m, niv), "")
        if " " in sg or art not in ("el", "la") or sg in formes_verbales or (vedettes.get(sg, set()) - {"noms"}):
            continue
        fp = paires.get((art, sg), 0.0)
        if fp > 0:
            rapports_art.append(mesure(mots, paires, fo) / fp)
    rapport_art = statistics.median(rapports_art) if rapports_art else 1.0
    print("  rapport median masse / (article + nom) : %.2f (sur %d noms)" % (rapport_art, len(rapports_art)))
    print("  rapport median (singulier + pluriel) / pluriel des noms : %.2f (sur %d noms)" % (rapport, len(rapports)))
    parts = {m: len(c & set(PARTAGEES)) for m, c in vedettes.items()}

    categories, homographes = {}, 0
    for cat, liste in es.items():
        lignes = []
        for i, (m, niv, formes) in enumerate(liste):
            formes = [x for x in formes if x and x not in ("—", "-")]
            if cat == "noms":
                sg = formes[0] if formes else ""
                pl = formes[1] if len(formes) > 1 else ""
                homo = " " not in sg and (sg in formes_verbales or (vedettes.get(sg, set()) - {"noms"}))
                if homo and pl and pl != sg:
                    f = mesure(mots, paires, [pl]) * rapport
                    homographes += 1
                elif homo:
                    art = ARTICLES.get((m, niv), "")
                    f = paires.get((art, sg), 0.0) * rapport_art if art in ("el", "la") else                         mesure(mots, paires, formes) / (1 + len(vedettes.get(sg, set()) - {"noms"}) + (sg in formes_verbales))
                    homographes += 1
                else:
                    f = mesure(mots, paires, formes)
            else:
                f = mesure(mots, paires, formes)
                if cat in PARTAGEES and parts.get(m.lower(), 1) > 1:
                    f /= parts[m.lower()]
            lignes.append((i, m, niv, f))
        lignes.sort(key=lambda l: (-l[3], l[0]))
        sortie, vus = [], set()
        for i, m, niv, f in lignes:
            if (m, niv) in vus:
                continue
            vus.add((m, niv))
            sortie.append({"m": m, "n": niv, "f": round(f, 2)})
        categories[cat] = sortie
        zero = sum(1 for l in lignes if not l[3])
        print("  %-12s %5d entrees, %4d sans mesure (zero) ; en tete : %s" % (
            cat, len(lignes), zero, ", ".join(l[1] for l in lignes[:10])))
    print("  noms homographes mesures par le pluriel : %d" % homographes)
    for niv in ("A1", "A2", "B1", "B2"):
        tete = [e["m"] for e in categories["noms"] if e["n"] == niv][:12]
        print("  noms %s en tete : %s" % (niv, ", ".join(tete)))
    if not a.ecrire:
        print("\n(rapport seulement ; --ecrire pour ecrire espanol/datos/frequence.json)")
        return
    d = {"_source": "Leipzig Corpora Collection (CC BY) -- (c) Universitat Leipzig / Sachsische Akademie der Wissenschaften / InfAI ; "
                    "OPUS OpenSubtitles 2018 (Lison & Tiedemann 2016), d'apres opensubtitles.org",
         "_corpus": CORPUS,
         "_note": "ORDRE = frequence, PAR CATEGORIE, jamais entre categories ; le niveau CECR reste l'organisateur principal. "
                  "f = frequence par million cumulee sur les formes connues (deux mots : cooccurrences voisines de Leipzig ; "
                  "trois et plus : minimum des paires) ; f = 0 veut dire ABSENT des listes, pas rare. "
                  "Noms homographes d'une forme verbale : pluriel x rapport median. "
                  "Lu par le test de niveau ; PAS par la seance espagnole (chargerFrequence). "
                  "Fichier derive : python espanol/frequence.py --ecrire",
         "categories": categories}
    with io.open(os.path.join(DATOS, "frequence.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("\nEcrit : espanol/datos/frequence.json")


if __name__ == "__main__":
    main()
