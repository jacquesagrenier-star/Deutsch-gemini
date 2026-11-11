# -*- coding: utf-8 -*-
"""Classe les entrees portugaises par frequence d'usage, a partir de Leipzig.

    python portugais/outils/frequence.py            -- le rapport, sans rien ecrire
    python portugais/outils/frequence.py --ecrire   -- ecrit portugais/datos/frequence.json
                                                       ET portugais/datos-br/frequence.json

Le pendant portugais d'espanol/frequence.py (dont il reprend la methode, la
grammaire etant la meme : o / a, six personnes) et de tests/frequence.py
(l'allemand). FICHIERS DERIVES, jamais a la main ; a relancer apres
construire.py (comme l'anglais : python anglais/outils/frequence.py --ecrire).

D'OU VIENNENT LES DONNEES, ET CE QUE LA LICENCE OBLIGE
    Accord de Jacques le 11 nov. 2026 (decisions/DECISIONS.md, « Oui,
    telecharge ») : la liste de frequence Leipzig portugaise, comme pour
    l'anglais le 28 oct. Leipzig Corpora Collection, sous CC BY : usage
    commercial permis, attribution obligatoire (carte « Credits », cle
    credits_freq de I18N_PORTUGAIS).

        (c) Universitat Leipzig / Sachsische Akademie der Wissenschaften / InfAI

    Trois corpus PAR VARIANTE, chacun ramene a une frequence PAR MILLION avant
    d'etre additionne (sinon le plus gros deciderait seul) :

      Portugal (datos/)
        por-pt_newscrawl_2011_300K   la presse du Portugal
        por-pt_web_2015_300K         le web du Portugal (.pt) : un registre plus courant
        por_wikipedia_2021_300K      Wikipedia en portugais (neutre)
      Bresil (datos-br/)
        por-br_newscrawl_2011_300K   la presse du Bresil
        por_news_2023_300K           la presse recente, toutes variantes (surtout le Bresil)
        por_wikipedia_2021_300K      Wikipedia en portugais (neutre)

    Leipzig n'a pas de corpus web bresilien telechargeable (aucun « por-br_web »
    au 11 nov. 2026) ni de sous-titres : pas de corpus PARLE, contrairement a
    l'allemand et a l'espagnol (OPUS OpenSubtitles). La presse hisse donc
    « governo » au-dessus de « agua ». Limite connue ; les listes OPUS pt et
    pt_br existent, mais leur ajout n'est pas dans l'accord du 11 nov.

    Les archives vivent HORS DU DEPOT et de OneDrive
    (C:/Users/jacqu/.wortando/frequence-pt) ; seul le classement derive est versionne.

CE QUI EST MESURE
    - Un mot seul : la somme des formes qu'on possede, en minuscules : le
      pluriel d'un nom ; le feminin et les pluriels d'un adjectif ; pour un
      verbe, l'infinitif et les formes conjuguees de verbes.json (present,
      perfeito, imperfeito, futur, conditionnel, subjonctif, imperatif), sans
      le pronom : « chamo-me » (Portugal) et « me chamo » (Bresil) comptent
      « chamo » ; « chamamo-nos » compte « chamamos ». Les formes a mesoclise
      (« chamar-me-ei ») sont laissees de cote.
    - Deux mots (« casa de banho », « ter de ») : les cooccurrences de mots
      voisins de Leipzig (fichier -co_n) ; trois mots ou plus : le minimum des
      paires voisines, une borne haute.

⚠️ LES HOMOGRAPHES, comme en espagnol : « trabalho » est un nom ET « je
    travaille », « conta » un nom ET « il compte ». Pour un nom dont le
    singulier est aussi une forme d'un de nos verbes ou le mot-vedette d'une
    autre categorie, on mesure son PLURIEL seul (« trabalhos »), multiplie par
    le rapport median (singulier + pluriel) / pluriel des noms sans homographe.
    Sans pluriel distinct : la paire article + nom (« o este », l'est), au
    rapport median masse / paire. Estimations annoncees, pas des mesures.
    Adjectifs, adverbes et mots-outils qui partagent un mot-vedette
    (« baixo », « claro ») se partagent la masse a parts egales.

⚠️ ON NE CLASSE QU'A L'INTERIEUR D'UNE CATEGORIE, jamais entre deux, et le
niveau CECR reste l'organisateur principal (voir CLAUDE.md, « frequence.json ») :
les listes comptent des formes et non des lemmes, ce qui penalise verbes et
adjectifs face aux noms.

LE BRESIL A SON PROPRE FICHIER (datos-br/frequence.json), mesure sur ses
corpus : ses mots different (autocarro / onibus, comboio / trem) et l'app lit
le fichier de la variante choisie (renvoi « frequence.json » de LANGUE_PORTUGAIS).
"""
import argparse, io, json, os, re, statistics, sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SOURCE = "C:/Users/jacqu/.wortando/frequence-pt"
VARIANTES = {
    "pt": ("portugais/datos", ["por-pt_newscrawl_2011_300K", "por-pt_web_2015_300K", "por_wikipedia_2021_300K"]),
    "br": ("portugais/datos-br", ["por-br_newscrawl_2011_300K", "por_news_2023_300K", "por_wikipedia_2021_300K"]),
}
PRONOMS = {"me", "te", "se", "nos", "vos", "lhe", "lhes", "o", "a", "os", "as"}
# Les auxiliaires des temps composes (« tenho vivido ») : le participe seul compte.
AUXILIAIRES = {"tenho", "tens", "tem", "temos", "tendes", "têm", "tinha", "tinhas",
               "tínhamos", "tínheis", "tinham"}
LETTRES = "a-záàâãéêíóôõúüç"


def charger(corpus):
    """(forme minuscule -> par million, (forme1, forme2) -> par million)."""
    mots, paires = {}, {}
    for nom in corpus:
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
        print("  %-28s %7d formes, %10d occurrences, %8d paires" % (nom, len(brut), total, npaires))
    return mots, paires


def jetons(s):
    # Le trait d'union separe : Leipzig compte « chamo-me » en deux mots.
    return [x for x in re.findall(r"[" + LETTRES + r"0-9]+", (s or "").lower()) if x]


def variantes(s):
    """« o/a estudante », « bonito / bonita » : chaque morceau compte."""
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


def sans_pronom(forme, composee=False):
    """« chamo-me » -> « chamo » ; « chamamo-nos » -> « chamamos » ;
    « me chamo » -> « chamo » ; « tenho vivido » -> « vivido ». Une mesoclise
    (« chamar-me-ei ») rend une chaine vide : la forme est laissee de cote."""
    forme = forme.strip().lower()
    t = forme.split()
    # L'auxiliaire ne s'enleve que dans un temps compose : « tenho de » (ter de)
    # garde son « tenho ».
    while len(t) > 1 and (t[0] in PRONOMS or (composee and t[0] in AUXILIAIRES)):
        t = t[1:]
    if not t:
        return ""
    tete = t[0].split("-")
    if len(tete) >= 3:
        return ""                       # mesoclise : chamar-me-ei
    if len(tete) == 2 and tete[1] in PRONOMS:
        v = tete[0]
        if tete[1] == "nos" and v.endswith("mo"):
            v += "s"                    # chamamo-nos -> chamamos
        t[0] = v
    return " ".join(t)


def formes_verbe(e):
    inf = sans_pronom(e.get("infinitif") or e.get("mot") or "")
    out = [inf]
    for cle in ("praesens", "perfeito", "imperfeito", "futuro", "condicional", "conjuntivo",
                "imperativo", "conj_imperfeito", "conj_futuro", "mais_que_perfeito",
                "perfeito_composto", "participio", "gerundio"):
        v = e.get(cle)
        if isinstance(v, str):
            vals = [v]
        else:
            vals = v.values() if isinstance(v, dict) else (v or [])
        for x in vals:
            if isinstance(x, str) and x.strip() and x.strip() not in ("—", "-"):
                f = sans_pronom(x, cle in ("perfeito_composto", "mais_que_perfeito"))
                # Un verbe de plusieurs mots (« ser promovido ») n'a qu'un
                # participe ou un gerondif d'un mot (« sido », « sendo ») : ce
                # serait la masse de « ser », pas la sienne.
                if f and (" " in f or " " not in inf):
                    out.append(f)
    return out


def formes_adjectif(e):
    m = (e.get("mot") or "").lower()
    fo = e.get("formes") or {}
    out = [m]
    for k in ("feminin", "pluriel", "feminin_pluriel"):
        x = (fo.get(k) or "").lower()
        if x and x not in out:
            out.append(x)
    return out


ARTICLES = {}   # (mot, niveau) -> « o » / « a » : la paire article + nom des homographes sans pluriel
# Des mots-outils tres frequents qui ne sont pas des mots-vedettes de
# fonctionnels.json : sans eux, le nom « o este » (l'est) ouvrirait le
# classement des noms (meme piege qu'en espagnol).
#
# Les possessifs sont ranges avec leur article (« a tua », « o seu ») : « sua »
# donnait au verbe « suar » (suer) toute la masse de « sa / leur ».
HORS_LISTE = {"este", "esta", "isto", "estes", "estas", "esse", "essa", "isso",
              "um", "uma", "uns", "umas",
              "meu", "meus", "minha", "minhas", "teu", "teus", "tua", "tuas",
              "seu", "seus", "sua", "suas", "nosso", "nossos", "nossa", "nossas",
              "vosso", "vossos", "vossa", "vossas"}
ARTICLES_SEULS = {"o", "a", "os", "as", "um", "uma"}


def vedettes_de(m):
    """« o / a » -> o, a ; « o meu » -> o meu, meu ; « um / uma » -> um, uma."""
    out = set()
    for v in variantes(m.lower()):
        out.add(v)
        t = v.split()
        if len(t) == 2 and t[0] in ARTICLES_SEULS:
            out.add(t[1])
    return out


# ⚠️ LA PREMIERE PERSONNE QUI EST UN NOM : « governo » (je gouverne / le
# gouvernement), « jogo », « trabalho », « canto ». Le nom manque souvent a nos
# listes, et la forme donnait au verbe sa masse : « governar » passait devant
# « levar ». Une forme conjuguee (jamais l'infinitif) qui est un NOM du
# Wiktionnaire portugais (dictionnaire WikDict pt-fr, deja telecharge pour la
# recherche) ne compte pas pour le verbe. Approximation annoncee : « dado »
# (le de / donne) quitte aussi « dar », ce qui ne change rien a son rang.
WIKDICT = "C:/Users/jacqu/.wortando/wikdict-pt/pt-fr.sqlite3"
NOMS_WIKT = set()


def noms_du_wiktionnaire():
    if not os.path.exists(WIKDICT):
        sys.exit("  Dictionnaire absent : %s (voir portugais/outils/dicc_construire.py)" % WIKDICT)
    import sqlite3
    db = sqlite3.connect(WIKDICT)
    noms = {(w or "").strip().lower() for w, lx in db.execute(
        "SELECT written_rep, lexentry FROM translation") if lx and "__substantivo" in lx.lower()}
    db.close()
    return noms


def entrees(dossier):
    def lire(n):
        return json.load(io.open(os.path.join(RACINE, dossier, n), encoding="utf-8"))
    out = {"noms": [], "verbes": [], "adjectifs": [], "adverbes": [], "mots-outils": [], "expressions": []}
    for t in lire("themes.json")["themes"]:
        for m in t["mots"]:
            pl = (m.get("pluriel") or "").lower()
            out["noms"].append((m["mot"], t.get("niveau"), [m["mot"].lower(), "" if pl in ("—", "-") else pl]))
            ARTICLES[(m["mot"], t.get("niveau"))] = (m.get("genre") or "").lower()
    for niv, l in lire("verbes.json").items():
        if niv.startswith("_"):
            continue
        for e in l:
            out["verbes"].append((e.get("infinitif") or e["mot"], niv, formes_verbe(e)))
    for nom, cle in (("adjectifs.json", "adjectifs"), ("adverbes.json", "adverbes"),
                     ("expressions.json", "expressions")):
        for niv, l in lire(nom).items():
            if niv.startswith("_"):
                continue
            for e in l:
                formes = formes_adjectif(e) if cle == "adjectifs" else [e["mot"].lower()]
                out[cle].append((e["mot"], niv, formes))
    # fonctionnels.json est range par categorie grammaticale ; le niveau est dans l'entree.
    for l in lire("fonctionnels.json").values():
        for e in l:
            out["mots-outils"].append((e["mot"], e.get("niveau"), [e["mot"].lower()]))
    return out


PARTAGEES = ("adjectifs", "adverbes", "mots-outils")


def classer(variante, corpus, dossier):
    print("\n== %s (%s) ==" % (variante, dossier))
    if not NOMS_WIKT:
        NOMS_WIKT.update(noms_du_wiktionnaire())
    mots, paires = charger(corpus)
    ARTICLES.clear()
    pt = entrees(dossier)
    # ⚠️ LES FORMES VERBALES QUI SONT AUSSI DES MOTS D'UNE AUTRE CATEGORIE :
    # « para » (parar), « como » (comer), « sobre » (sobrar), « era » (ser et
    # le nom « a era ») prendraient la masse de la preposition ou de la
    # conjonction. Une forme conjuguee qui est le mot-vedette d'une autre
    # categorie (ou un mot-outil quelconque) ne compte pas pour le verbe ;
    # l'infinitif compte toujours.
    formes_verbales = {f for _, _, fo in pt["verbes"] for f in fo[1:] if " " not in f}
    autres = {v for cat, l in pt.items() if cat != "verbes" for m, _, _ in l for v in vedettes_de(m)} | HORS_LISTE
    autres |= {f for cat in ("mots-outils", "adverbes") for _, _, fo in pt[cat] for f in fo}
    autres |= NOMS_WIKT
    pt["verbes"] = [(m, niv, [fo[0]] + [f for f in fo[1:] if f not in autres]) for m, niv, fo in pt["verbes"]]

    formes_verbales |= HORS_LISTE
    vedettes = {}
    for cat, liste in pt.items():
        for m, niv, fo in liste:
            for v in ({m.lower()} | (vedettes_de(m) if cat != "noms" else set())):
                vedettes.setdefault(v, set()).add(cat)
    rapports = []
    for m, niv, fo in pt["noms"]:
        sg, pl = fo[0], fo[1] if len(fo) > 1 else ""
        if " " in sg or not pl or pl == sg or sg in formes_verbales or (vedettes.get(sg, set()) - {"noms"}):
            continue
        fpl = mots.get(pl, 0.0)
        if fpl > 0:
            rapports.append((mots.get(sg, 0.0) + fpl) / fpl)
    rapport = statistics.median(rapports) if rapports else 1.0
    rapports_art = []
    for m, niv, fo in pt["noms"]:
        sg, art = fo[0], ARTICLES.get((m, niv), "")
        if " " in sg or art not in ("o", "a") or sg in formes_verbales or (vedettes.get(sg, set()) - {"noms"}):
            continue
        fp = paires.get((art, sg), 0.0)
        if fp > 0:
            rapports_art.append(mesure(mots, paires, fo) / fp)
    rapport_art = statistics.median(rapports_art) if rapports_art else 1.0
    print("  rapport median masse / (article + nom) : %.2f (sur %d noms)" % (rapport_art, len(rapports_art)))
    print("  rapport median (singulier + pluriel) / pluriel des noms : %.2f (sur %d noms)" % (rapport, len(rapports)))
    parts = {m: len(c & set(PARTAGEES)) for m, c in vedettes.items()}

    categories, homographes = {}, 0
    for cat, liste in pt.items():
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
                    if art in ("o", "a"):
                        f = paires.get((art, sg), 0.0) * rapport_art
                    else:
                        f = mesure(mots, paires, formes) / (1 + len(vedettes.get(sg, set()) - {"noms"}) + (sg in formes_verbales))
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
    print("  noms homographes mesures par le pluriel ou l'article : %d" % homographes)
    for niv in ("A1", "A2", "B1", "B2", "C1"):
        tete = [e["m"] for e in categories["noms"] if e["n"] == niv][:12]
        print("  noms %s en tete : %s" % (niv, ", ".join(tete)))
    for niv in ("A1", "B1"):
        tete = [e["m"] for e in categories["verbes"] if e["n"] == niv][:12]
        print("  verbes %s en tete : %s" % (niv, ", ".join(tete)))
    return categories


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ecrire", action="store_true")
    ap.add_argument("--variante", choices=sorted(VARIANTES), help="une seule variante (defaut : les deux)")
    a = ap.parse_args()
    for v in ([a.variante] if a.variante else ["pt", "br"]):
        dossier, corpus = VARIANTES[v]
        categories = classer(v, corpus, dossier)
        if not a.ecrire:
            continue
        d = {"_source": "Leipzig Corpora Collection (CC BY) -- (c) Universitat Leipzig / Sachsische Akademie der Wissenschaften / InfAI",
             "_corpus": corpus,
             "_note": "ORDRE = frequence, PAR CATEGORIE, jamais entre categories ; le niveau CECR reste l'organisateur principal. "
                      "f = frequence par million cumulee sur les formes connues (deux mots : cooccurrences voisines de Leipzig ; "
                      "trois et plus : minimum des paires) ; f = 0 veut dire ABSENT des listes, pas rare. "
                      "Noms homographes d'une forme verbale : pluriel x rapport median. "
                      "Fichier derive : python portugais/outils/frequence.py --ecrire",
             "categories": categories}
        chemin = os.path.join(RACINE, dossier, "frequence.json")
        with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
            json.dump(d, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print("  Ecrit : %s/frequence.json" % dossier)
    if not a.ecrire:
        print("\n(rapport seulement ; --ecrire pour ecrire les deux frequence.json)")


if __name__ == "__main__":
    main()
