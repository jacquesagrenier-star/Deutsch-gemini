# -*- coding: utf-8 -*-
"""Classe les entrees anglaises par frequence d'usage, a partir de Leipzig.

    python anglais/outils/frequence.py            -- le rapport, sans rien ecrire
    python anglais/outils/frequence.py --ecrire   -- ecrit anglais/datos/frequence.json

Le pendant anglais de tests/frequence.py (l'allemand) : meme format de sortie,
memes principes. A relancer apres construire.py. FICHIER DERIVE, jamais a la main.

D'OU VIENNENT LES DONNEES (accord de Jacques, 28 oct. 2026 : « Oui, les deux »)
    Leipzig Corpora Collection, sous CC BY (verifie le 28 oct. sur
    wortschatz.uni-leipzig.de/en/usage : « The text corpora offered for download
    are made available under the Creative Commons licence CC BY »). Attribution
    dans la carte « Credits » (credits_freq de I18N_ANGLAIS).

        (c) Universitat Leipzig / Sachsische Akademie der Wissenschaften / InfAI

    Trois corpus, chacun ramene a une frequence PAR MILLION avant d'etre
    additionne (sinon le plus gros deciderait seul) :
        eng_news_2023_300K              la presse recente
        eng-com_web-public_2018_300K    le web americain (.com) -- l'anglais de base est americain
        eng-simple_wikipedia_2021_300K  Simple English Wikipedia -- un anglais
                                        ecrit pour des apprenants
    Leipzig n'a pas de sous-titres anglais : pas de corpus parle, contrairement
    a l'allemand (opensubtitles). C'est une limite connue.

    Les archives vivent HORS DU DEPOT et de OneDrive
    (C:/Users/jacqu/.wortando/frequence-en) ; seul le classement derive est versionne.

CE QUI EST MESURE
    - Un mot seul : la somme des formes qu'on possede (pluriel ; troisieme
      personne, preterit, participe, -ing ; jamais le comparatif), toutes
      casses confondues (« The » et « the »).
    - Deux mots (« parking lot », « get up ») : les cooccurrences de mots
      voisins de Leipzig (fichier -co_n), sommees sur les formes du verbe pour
      un phrasal verb. Ce fichier ne garde que les paires significatives : une
      paire absente compte zero, comme un mot absent.
    - Trois mots ou plus : le minimum des paires voisines -- une borne haute,
      pas une mesure exacte. Les expressions (« It depends. ») restent a zero
      sauf ce cas, comme en allemand.

    ⚠️ ON NE CLASSE QU'A L'INTERIEUR D'UNE CATEGORIE, jamais entre deux, et le
    niveau CECR reste l'organisateur principal : la frequence n'affine que
    l'ordre a l'interieur d'un niveau (voir CLAUDE.md, « frequence.json »).

LE BRITANNIQUE
    anglais/datos-gb a les memes mots dans le meme ordre. Une forme britannique
    differente (colour, flat) est classee juste apres l'americaine, avec la meme
    frequence : l'app lit un seul fichier pour les deux variantes.
"""
import argparse, io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SOURCE = "C:/Users/jacqu/.wortando/frequence-en"
CORPUS = ["eng_news_2023_300K", "eng-com_web-public_2018_300K", "eng-simple_wikipedia_2021_300K"]
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]


def charger():
    """(forme minuscule -> par million, (forme1, forme2) -> par million,
    forme exacte -> par million). La forme exacte sert aux mots a majuscule
    (May, Monday) : en minuscules, « May » prendrait la masse du modal « may »."""
    mots, paires, exacts = {}, {}, {}
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
                ids[p[0]] = p[1].lower()
                brut[p[1].lower()] = brut.get(p[1].lower(), 0) + int(p[2])
                exact = exacts.setdefault(nom, {})
                exact[p[1]] = exact.get(p[1], 0) + int(p[2])
                total += int(p[2])
        for m, n in brut.items():
            mots[m] = mots.get(m, 0.0) + n * 1e6 / total
        for m, n in exacts.pop(nom).items():
            if m[:1].isupper():
                exacts[m] = exacts.get(m, 0.0) + n * 1e6 / total
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
        print("  %-32s %7d formes, %9d occurrences, %7d paires" % (nom, len(brut), total, npaires))
    return mots, paires, exacts


def jetons(s):
    # Le trait d'union reste dans le mot : Leipzig compte « T-shirt » d'un bloc.
    return [x.strip("-") for x in re.findall(r"[a-z0-9'-]+", (s or "").lower()) if x.strip("-")]


def variantes(s):
    """« ehrlich/unehrlich » en allemand ; ici « was/were », « advisor / adviser »."""
    return [p.strip() for p in (s or "").split("/") if p.strip()]


def mesure(mots, paires, exacts, formes):
    """Frequence cumulee des formes (un mot, deux mots, ou plus)."""
    total, vues = 0.0, set()
    for brut in formes:
        for f in variantes(brut):
            f = re.sub(r"\s*\(.*?\)", "", f).strip()
            j = tuple(jetons(f))
            if not j or j in vues:
                continue
            vues.add(j)
            if len(j) == 1 and f[:1].isupper() and f in exacts:
                total += exacts[f]
            elif len(j) == 1:
                total += mots.get(j[0], 0.0)
            else:
                total += min(paires.get((a, b), 0.0) for a, b in zip(j, j[1:]))
    return total


def formes_verbe(e):
    inf = e.get("infinitif") or e.get("mot") or ""
    fo = e.get("formes") or {}
    base = [inf] + [fo.get(k, "") for k in ("troisieme", "preterit", "participe", "ing")]
    # Phrasal verb : les formes du verbe, suivies du reste (« got up », « getting up »).
    t = inf.split()
    if len(t) > 1:
        # Chaque variante d'abord (« was/were » donne deux formes), PUIS le reste :
        # coller le reste a « was/were » laissait « was » seul, et toute la masse
        # de « was » allait a « be entitled to ».
        reste = " ".join(t[1:])
        return [inf] + [v + " " + reste for x in base[1:] for v in variantes(x.split()[0] if x else "")]
    return [x for x in base if x]


# ⚠️ LES HOMOGRAPHES, ET LA REGLE QUI LES TRAITE (sur la FORME, jamais le sens).
# Le nom « can » (une boite) prenait la masse du modal, « will » (un testament)
# celle du futur : ils ouvraient le classement des noms. On ne demele pas le sens
# a partir d'une liste de formes ; on choisit donc une forme qui n'appartient
# qu'au nom, son PLURIEL (« cans », « wills »), quand le singulier est aussi le
# mot-vedette d'une autre categorie. Pour les adjectifs, adverbes et mots-outils
# qui partagent un mot-vedette (« even », « still »), il n'existe pas d'autre
# forme : la masse est partagee a parts egales entre les categories qui le
# portent. C'est une approximation annoncee, pas une mesure.
PARTAGEES = ("adjectifs", "adverbes", "mots-outils")


def corriger_homographes(us):
    # Les modaux et auxiliaires ne sont pas des mots-vedettes de nos listes
    # (on les apprend dans les fiches) : on les declare ici.
    vedettes = {m: {"modaux"} for m in ("can", "will", "may", "might", "must", "shall", "should", "would", "could", "do", "have", "be")}
    for cat, liste in us.items():
        for m, niv, formes in liste:
            vedettes.setdefault(m.lower(), set()).add(cat)
    diviseurs = {}
    for i, (m, niv, formes) in enumerate(us["noms"]):
        autres = vedettes.get(m.lower(), set()) - {"noms"}
        pl = formes[1] if len(formes) > 1 else ""
        if not autres or m[:1].isupper():
            continue        # pas d'homographe, ou un mot a majuscule (May) : mesure exacte
        if pl and pl not in ("—", "-") and pl.lower() != m.lower():
            us["noms"][i] = (m, niv, [pl])
        else:
            # Indenombrable (« work », « help ») : pas de pluriel, pas d'autre
            # forme. La masse est partagee entre le nom et ses homographes.
            diviseurs[i] = 1 + len(autres)
    parts = {m: len(c & set(PARTAGEES)) for m, c in vedettes.items()}
    return parts, diviseurs


def entrees(dossier):
    """categorie -> [(mot, niveau, formes)] dans l'ordre des fichiers."""
    def lire(n):
        return json.load(io.open(os.path.join(RACINE, dossier, n), encoding="utf-8"))
    out = {"noms": [], "verbes": [], "adjectifs": [], "adverbes": [], "mots-outils": [], "expressions": []}
    for t in lire("themes.json")["themes"]:
        for m in t["mots"]:
            out["noms"].append((m["mot"], t.get("niveau"), [m["mot"], m.get("pluriel", "")]))
    for niv, l in lire("verbes.json").items():
        for e in l:
            out["verbes"].append((e.get("infinitif") or e["mot"], niv, formes_verbe(e)))
    for nom, cle in (("adjectifs.json", "adjectifs"), ("adverbes.json", "adverbes"), ("expressions.json", "expressions")):
        for niv, l in lire(nom).items():
            for e in l:
                out[cle].append((e["mot"], niv, [e["mot"]]))
    for l in lire("fonctionnels.json").values():
        for e in l:
            out["mots-outils"].append((e["mot"], e.get("niveau"), [e["mot"]]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ecrire", action="store_true")
    a = ap.parse_args()
    mots, paires, exacts = charger()
    us, gb = entrees("anglais/datos"), entrees("anglais/datos-gb")
    parts, diviseurs = corriger_homographes(us)
    categories = {}
    for cat, liste in us.items():
        lignes = []
        for i, (m, niv, formes) in enumerate(liste):
            f = mesure(mots, paires, exacts, [x for x in formes if x not in ("—", "-")])
            if cat in PARTAGEES and parts.get(m.lower(), 1) > 1:
                f /= parts[m.lower()]
            if cat == "noms" and i in diviseurs:
                f /= diviseurs[i]
            lignes.append((i, m, niv, f))
        lignes.sort(key=lambda l: (-l[3], l[0]))
        sortie, vus = [], set()
        for i, m, niv, f in lignes:
            for mot in (m, gb[cat][i][0] if i < len(gb[cat]) else m):
                if mot not in vus:
                    vus.add(mot)
                    sortie.append({"m": mot, "n": niv, "f": round(f, 2)})
        categories[cat] = sortie
        zero = sum(1 for l in lignes if not l[3])
        print("  %-12s %5d entrees, %4d sans mesure (zero) ; en tete : %s" % (
            cat, len(lignes), zero, ", ".join(l[1] for l in lignes[:8])))
    if not a.ecrire:
        print("\n(rapport seulement ; --ecrire pour ecrire anglais/datos/frequence.json)")
        return
    d = {"_source": "Leipzig Corpora Collection (CC BY) -- (c) Universitat Leipzig / Sachsische Akademie der Wissenschaften / InfAI",
         "_corpus": CORPUS,
         "_note": "ORDRE = frequence, PAR CATEGORIE, jamais entre categories ; le niveau CECR reste l'organisateur principal. "
                  "f = frequence par million cumulee sur les formes connues (deux mots : cooccurrences voisines de Leipzig ; "
                  "trois et plus : minimum des paires). Les formes britanniques suivent l'americaine. "
                  "Fichier derive : python anglais/outils/frequence.py --ecrire",
         "categories": categories}
    with io.open(os.path.join(RACINE, "anglais/datos/frequence.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("\nEcrit : anglais/datos/frequence.json")


if __name__ == "__main__":
    main()
