# -*- coding: utf-8 -*-
"""Genere anglais/datos/synonymes.json -- les voisins de sens DEJA DANS LE COURS.

    python anglais/outils/voisins.py            -- le rapport, sans rien ecrire
    python anglais/outils/voisins.py --ecrire   -- ecrit le fichier

Le pendant anglais de tests/synonymes.py. A relancer apres construire.py.
FICHIER DERIVE, jamais a la main.

LA REGLE, comme en allemand : DEUX SOURCES DOIVENT CONCORDER.
L'allemand rapproche deux mots qui partagent une traduction en francais ET en
anglais. L'anglais n'a qu'une langue de traduction ; la seconde source est
Open English WordNet : deux mots anglais sont voisins s'ils sont dans un meme
ensemble de synonymes de WordNet ET partagent une traduction francaise dans
nos listes. WordNet seul rapproche « car » et « machine » (un vieux sens) ;
le francais seul rapproche « fly » et « steal » (« voler »). Ensemble, non.

Les deux mots doivent etre dans le cours, dans la meme categorie.

D'OU VIENT WORDNET (accord de Jacques, 28 oct. 2026 : « Oui, les deux »)
    Open English WordNet, edition 2025 (github.com/globalwordnet/english-wordnet),
    sous CC BY 4.0, derive de Princeton WordNet (licence WordNet) : l'attribution
    nomme les deux (carte « Credits », credits_freq de I18N_ANGLAIS).
    L'archive vit HORS DU DEPOT : C:/Users/jacqu/.wortando/wordnet-en.

ECARTE AUTOMATIQUEMENT (sur la forme, jamais sur le sens) :
  1. la variante britannique d'un meme mot (color / colour)
  2. le pluriel ou une meme forme a la casse ou au trait d'union pres
"""
import argparse, glob, io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
WORDNET = "C:/Users/jacqu/.wortando/wordnet-en/json"
POS = {"noms": ("n",), "verbes": ("v",), "adjectifs": ("a", "s"), "adverbes": ("r",)}
ARTICLES = re.compile(r"^(le |la |les |l'|un |une |des |du |de la |se |s'|être )")


# Paires ecartees A LA MAIN, apres lecture d'un echantillon (28 oct. 2026).
# Chacune passait les deux sources et disait pourtant quelque chose de faux a un
# apprenant. La raison est ecrite, sinon la ligne se fait supprimer.
A_ECARTER = {
    ("say", "tell"):     "tell prend toujours une personne (tell me) ; say non -- on ne les echange pas",
    ("chance", "luck"):  "faux ami enseigne dans le cours : chance = occasion, luck = la chance",
    ("get up", "raise"): "raise = lever quelque chose ; get up = se lever",
    ("fit", "go"):       "« ca va avec » n'est qu'un sens rare de go",
}


def paires_confondues():
    """Les « mots confondus » des fiches Pieges (lend / borrow, say / tell...) :
    le cours les OPPOSE, ils ne peuvent pas etre presentes comme voisins."""
    out = set()
    d = json.load(io.open(os.path.join(ICI, "ancien", "english_pitfalls.json"), encoding="utf-8"))
    for l in d.values():
        for e in l:
            if e.get("kategorie") == "Mots confondus":
                mots = [norme(re.sub(r"^to ", "", x.strip())) for x in e["mot"].split("/")]
                out |= {tuple(sorted((a, b))) for a in mots for b in mots if a != b}
    return out


def lire(dossier, nom):
    return json.load(io.open(os.path.join(RACINE, dossier, nom), encoding="utf-8"))


def entrees(dossier):
    """categorie -> [(mot, traduction)] dans l'ordre des fichiers."""
    out = {"noms": [], "verbes": [], "adjectifs": [], "adverbes": []}
    for t in lire(dossier, "themes.json")["themes"]:
        for m in t["mots"]:
            out["noms"].append((m["mot"], m.get("traduction", "")))
    for niv, l in lire(dossier, "verbes.json").items():
        for e in l:
            out["verbes"].append((e.get("infinitif") or e["mot"], e.get("traduction", "")))
    for nom, cle in (("adjectifs.json", "adjectifs"), ("adverbes.json", "adverbes")):
        for niv, l in lire(dossier, nom).items():
            for e in l:
                out[cle].append((e["mot"], e.get("traduction", "")))
    return out


def sens_fr(t):
    """Les traductions francaises, sans article ni parenthese."""
    t = re.sub(r"\(.*?\)", "", (t or "").lower())
    out = set()
    for p in re.split(r"[,;/]", t):
        p = ARTICLES.sub("", p.strip()).strip(" .!?")
        if p:
            out.add(p)
    return out


def norme(m):
    return re.sub(r"[-\s]+", " ", m.lower()).strip()


def charger_wordnet():
    lemmes = {}
    for f in sorted(glob.glob(os.path.join(WORDNET, "entries-*.json"))):
        for lemme, par_pos in json.load(io.open(f, encoding="utf-8")).items():
            for pos, d in par_pos.items():
                for s in d.get("sense", []):
                    lemmes.setdefault((norme(lemme), pos[0]), set()).add(s["synset"])
    membres = {}
    for f in sorted(glob.glob(os.path.join(WORDNET, "*.*.json"))):
        if os.path.basename(f).startswith("entries-"):
            continue
        for sid, s in json.load(io.open(f, encoding="utf-8")).items():
            if isinstance(s, dict) and "members" in s:
                membres[sid] = [norme(x) for x in s["members"]]
    if not lemmes or not membres:
        sys.exit("  WordNet absent ou vide : " + WORDNET)
    return lemmes, membres


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ecrire", action="store_true")
    a = ap.parse_args()
    lemmes, membres = charger_wordnet()
    us, gb = entrees("anglais/datos"), entrees("anglais/datos-gb")
    exclues = paires_confondues() | {tuple(sorted(p)) for p in A_ECARTER}
    voisins, bilan = {}, []
    for cat, liste in us.items():
        index = {}
        for i, (m, tr) in enumerate(liste):
            index.setdefault(norme(m), []).append(i)
        gb_de = {i: gb[cat][i][0] for i in range(min(len(liste), len(gb[cat])))}
        n_wn = n_garde = 0
        for i, (m, tr) in enumerate(liste):
            synsets = set()
            for p in POS[cat]:
                synsets |= lemmes.get((norme(m), p), set())
            fr = sens_fr(tr)
            # Trie : l'ordre d'un set de chaines change d'un passage a l'autre
            # (graine de hachage), et avec lui l'ordre des voisins ecrits.
            for sid in sorted(synsets):
                for autre in membres.get(sid, []):
                    for j in index.get(autre, []):
                        m2, tr2 = liste[j]
                        if j == i or norme(m2) == norme(m):
                            continue
                        # Variante britannique d'un meme mot, ou pluriel : une forme, pas un voisin.
                        if norme(gb_de.get(i, "")) == norme(m2) or norme(gb_de.get(j, "")) == norme(m):
                            continue
                        if norme(m2) in (norme(m) + "s", norme(m) + "es"):
                            continue
                        n_wn += 1
                        if not (fr & sens_fr(tr2)):
                            continue
                        if tuple(sorted((norme(m), norme(m2)))) in exclues:
                            continue
                        n_garde += 1
                        for a_, b_, ia, ib in ((m, m2, i, j), (gb_de.get(i, m), gb_de.get(j, m2), i, j)):
                            l = voisins.setdefault(a_, [])
                            if b_ not in l and b_ != a_:
                                l.append(b_)
        bilan.append("  %-10s %5d paires WordNet dans le cours, %4d gardees (traduction francaise commune)" % (cat, n_wn, n_garde))
    for l in bilan:
        print(l)
    print("  %d mots ont au moins un voisin" % len(voisins))
    ex = [(k, v) for k, v in sorted(voisins.items())][:0]
    for k in ("car", "begin", "big", "quickly", "job", "buy", "happy", "often", "angry", "street"):
        if k in voisins:
            print("    %-10s -> %s" % (k, ", ".join(voisins[k])))
    if not a.ecrire:
        print("\n(rapport seulement ; --ecrire pour ecrire anglais/datos/synonymes.json)")
        return
    d = {"_note": "Voisins de sens deja presents dans le cours. Une paire n'y figure que si deux sources concordent : "
                  "un meme ensemble de synonymes d'Open English WordNet (CC BY 4.0, d'apres Princeton WordNet) ET une "
                  "traduction francaise commune dans nos listes. Variantes britanniques et pluriels ecartes. "
                  "Fichier derive : python anglais/outils/voisins.py --ecrire",
         "voisins": dict(sorted(voisins.items()))}
    with io.open(os.path.join(RACINE, "anglais/datos/synonymes.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("\nEcrit : anglais/datos/synonymes.json")


if __name__ == "__main__":
    main()
