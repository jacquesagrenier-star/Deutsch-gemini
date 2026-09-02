# -*- coding: utf-8 -*-
"""Prepare la relecture croisee du TURC, puis la depouille.

    python tests/relecture_tr.py --suspects               # 1a. les champs perdus
    python tests/relecture_tr.py --collisions             # 1b. les collisions
    python tests/relecture_tr.py --niveaux A1,A2          # 2. les lots a distribuer
    python tests/relecture_tr.py --rapport                # 3. le depouillement

MEME METHODE QUE POUR L'ALLEMAND, MEME ORDRE.

C'est `tests/relecture.py` transpose au turc, et l'ordre des trois etapes
compte plus que les outils :

  1. LE CONTRASTE MECANIQUE D'ABORD. Cote allemand c'etait WikDict, sur le
     genre et le pluriel. Il n'existe pas d'equivalent turc utilisable ici --
     mais il reste un controle qu'une machine tranche seule, et c'est
     justement le defaut le plus grave de ce corpus : DEUX MOTS ALLEMANDS
     DISTINCTS QUI RECOIVENT LA MEME REPONSE TURQUE. La carte devient alors
     indecidable : quoi que l'apprenant reponde, il ne peut pas avoir raison.
     L'allemand aligne quatre verbes pour nier et cinq pour echouer ; le turc
     les a tous, mais seulement si on refuse le mot facile. `--collisions` les
     sort toutes, sans avis, sans IA.

  2. LA RELECTURE PAR UN AUTRE MODELE ENSUITE, et seulement pour ce qu'aucune
     table ne juge : le sens, le naturel, le registre, l'accord entre la
     phrase allemande et sa version turque.

  3. N'APPLIQUER QUE LES FAITS. Le depouillement ne corrige RIEN. Il produit
     une liste a examiner. L'application est EN SERVICE : un avis n'y suffit
     pas.

UNE LIMITE A REDIRE A CHAQUE FOIS. Le relecteur est un autre modele, pas un
autre esprit : il partage une partie de nos donnees d'entrainement, donc une
partie de nos angles morts -- et c'est le plus vrai sur le regional. Son
accord n'est pas une preuve. Pour trancher ce qui reste, il faut un autre
fournisseur, ou une locutrice native.

LE FRANCAIS EST DONNE, MAIS IL N'EST PAS LA SOURCE. Chaque carte porte sa
traduction francaise pour fixer le SENS VOULU, sans quoi le relecteur juge
une ambiguite allemande au lieu de la traduction. La consigne le dit
explicitement : l'allemand est l'original, le turc est ce qu'on juge.

Taille des lots : 100 cartes. Lecon de la relecture espagnole -- a 330 le
relecteur cale, a 100 ca passe. Les verbes portent cinq fragments turcs par
carte (le verbe et quatre temps) : ils descendent a 40.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORTIE = os.path.join(RACINE, "relecture_tr")
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]

# Combien de cartes par lot, selon le poids reel d'une carte. Une carte de
# verbe porte cinq fragments turcs, une carte de nom en porte deux : les
# compter pareil donnerait des lots cinq fois plus lourds sans que ca se voie.
TAILLE = {"verbes": 40}
TAILLE_DEFAUT = 100


# ---------------------------------------------------------------- chargement
#
# Chaque categorie rend une liste de cartes deja mises a plat, portant
# toujours : cle (le mot allemand, identifiant du signalement), niveau, et les
# champs a soumettre. La forme des fichiers JSON differe d'une categorie a
# l'autre -- c'est ici, et seulement ici, que ca se voit.

def _charger(nom):
    return json.load(io.open(os.path.join(RACINE, nom), encoding="utf-8"))


def cartes_noms():
    d = _charger("themes.json")
    themes = d.get("themes", d)
    out = []
    for t in themes:
        for m in t.get("mots", []):
            out.append({
                "cle": m.get("mot"),
                "niveau": t.get("niveau"),
                "theme": t.get("nom_theme"),
                "allemand": ((m.get("genre") or "") + " " + (m.get("mot") or "")).strip(),
                "sens_fr": m.get("traduction"),
                "turc": m.get("traduction_tr"),
                "phrase_de": m.get("exemple"),
                "phrase_fr": m.get("exemple_fr"),
                "phrase_tr": m.get("exemple_tr"),
            })
    return out


def cartes_simples(fichier, champ_mot="mot"):
    """adjectif.json, adverbe.json, redewendung.json : meme forme."""
    d = _charger(fichier)
    out = []
    for niveau in NIVEAUX:
        for m in d.get(niveau, []):
            out.append({
                "cle": m.get(champ_mot),
                "niveau": niveau,
                "allemand": m.get(champ_mot),
                "sens_fr": m.get("traduction"),
                "turc": m.get("traduction_tr"),
                "phrase_de": m.get("exemple"),
                "phrase_fr": m.get("exemple_fr"),
                "phrase_tr": m.get("exemple_tr"),
            })
    return out


def cartes_verbes():
    """Un verbe porte quatre temps, chacun avec sa phrase et sa version turque.

    On soumet les quatre : c'est la ou se cachent les erreurs de temps et
    d'aspect, que le turc rend differemment de l'allemand.
    """
    d = _charger("verbe.json")
    temps = [("exemple", "Präsens"), ("perfekt", "Perfekt"),
             ("praeteritum", "Präteritum"), ("konjunktiv2", "Konjunktiv II")]
    out = []
    for niveau in NIVEAUX:
        for v in d.get(niveau, []):
            phrases = []
            for champ, libelle in temps:
                de = v.get(champ)
                if not de:
                    continue
                phrases.append({
                    "temps": libelle,
                    "champ": champ,
                    "de": de,
                    "fr": v.get(champ + "_fr"),
                    "tr": v.get(champ + "_tr"),
                })
            out.append({
                "cle": v.get("infinitif"),
                "niveau": niveau,
                "allemand": v.get("infinitif"),
                "sens_fr": v.get("traduction"),
                "turc": v.get("traduction_tr"),
                "phrases": phrases,
            })
    return out


CATEGORIES = {
    "noms": cartes_noms,
    "verbes": cartes_verbes,
    "adjectifs": lambda: cartes_simples("adjectif.json"),
    "adverbes": lambda: cartes_simples("adverbe.json"),
    "expressions": lambda: cartes_simples("redewendung.json"),
}


def toutes_les_cartes():
    tout = {}
    for nom, fn in CATEGORIES.items():
        tout[nom] = fn()
    return tout


# ------------------------------------------------------- 1. controle mecanique

def _suspects(cartes):
    """Champs turcs qui ne peuvent PAS etre une traduction.

    Trouve le 2 septembre 2026, et c'est la raison d'etre de l'etape
    mecanique : 673 entrees portaient UN SEUL CARACTERE en guise de
    traduction -- « bereits » traduit par « c », « es geht um » par « s ».
    Le champ existe et n'est pas vide, donc `reste_turc.py` le comptait
    comme fait et l'application l'affichait tel quel.

    Ce n'est pas un jugement de qualite : une traduction d'un caractere ou
    une phrase de trois caracteres ne sont pas des traductions faibles, ce
    sont des donnees perdues. Aucune relecture n'a a en juger, et leur
    envoyer un lot de « c » gaspille un relecteur.

    Le seuil des mots est bas exprès : « az », « su », « ne » sont de vrais
    mots turcs. On ne signale donc qu'un caractere unique. Une phrase, elle,
    ne fait jamais moins de huit caracteres.
    """
    out = []
    for c in cartes:
        mot = (c.get("turc") or "").strip()
        if len(mot) <= 1:
            out.append((c, "traduction_tr", mot))
        phrases = c.get("phrases")
        if phrases:
            for p in phrases:
                tr = (p.get("tr") or "").strip()
                if len(tr) < 8:
                    out.append((c, p["champ"] + "_tr", tr))
        else:
            ph = (c.get("phrase_tr") or "").strip()
            if len(ph) < 8:
                out.append((c, "exemple_tr", ph))
    return out


def suspects():
    tout = toutes_les_cartes()
    if not os.path.isdir(SORTIE):
        os.makedirs(SORTIE)
    total = 0
    lignes = []
    for nom in sorted(tout):
        trouves = _suspects(tout[nom])
        if not trouves:
            continue
        total += len(trouves)
        par_niveau = {}
        for c, champ, val in trouves:
            par_niveau.setdefault(c.get("niveau"), []).append((c, champ, val))
        lignes.append("\n## %s (%d champs)\n" % (nom, len(trouves)))
        for niv in NIVEAUX:
            if niv not in par_niveau:
                continue
            lignes.append("### %s — %d\n" % (niv, len(par_niveau[niv])))
            for c, champ, val in par_niveau[niv]:
                lignes.append("- **%s** — `%s` vaut %s (attendu : %s)"
                              % (c.get("allemand"), champ, repr(val),
                                 c.get("sens_fr") or "?"))
            lignes.append("")
        print("  %-12s %4d champ(s) perdu(s)" % (nom, len(trouves)))

    chemin = os.path.join(SORTIE, "suspects.md")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Champs turcs perdus — le controle mecanique\n\n")
        f.write("Produit par `python tests/relecture_tr.py --suspects`. ")
        f.write("**Aucune correction appliquee.**\n\n")
        f.write("Ce ne sont pas des traductions faibles, ce sont des donnees ")
        f.write("perdues : un caractere unique en guise de mot, une phrase de ")
        f.write("moins de huit caracteres. Le champ existe et n'est pas vide, ")
        f.write("donc `reste_turc.py` les comptait comme faits et ")
        f.write("l'application les affiche tels quels.\n\n")
        f.write("Ils sont exclus des lots de relecture : envoyer un lot de ")
        f.write("« c » a un relecteur gaspille le relecteur.\n")
        f.write("\n".join(lignes))
        f.write("\n")
    print()
    print("  ecrit : relecture_tr/suspects.md  (%d champs)" % total)
    return 0


# LES PAIRES DE GENRE NE SONT PAS DES COLLISIONS, ET LES SIGNALER SANS FIN
# EST PIRE QU'INUTILE.
#
# « der Experte » et « die Expertin » recoivent tous deux « uzman », et c'est
# JUSTE : le turc n'a pas de genre grammatical et ne feminise pas le nom de
# metier. Inventer « kadin uzman » pour departager les deux cartes
# enseignerait une regle qui n'existe pas dans la langue.
#
# Elles sortent donc du decompte et vont dans une section a part, une fois,
# pour qu'on sache qu'elles ont ete vues et non oubliees. Sans ca, chaque
# relance du controle les remet dans la pile et on finit par ne plus lire le
# rapport du tout.
#
# La detection est mecanique : on plie les tremas, on retire l'eventuel « in »
# final, le « e » final, et on ramene -mann/-frau au radical. Si les deux mots
# se rejoignent, c'est la meme entree au feminin.
#
#     Experte / Expertin        -> expert
#     Koch / Koechin            -> koch
#     Tormann / Torfrau         -> tor
#     Cousin / Cousine          -> cousin
def _radical(mot):
    m = (mot or "").lower().strip()
    for article in ("der ", "die ", "das "):
        if m.startswith(article):
            m = m[len(article):]
    for a, b in (("ä", "a"), ("ö", "o"), ("ü", "u"), ("ß", "ss")):
        m = m.replace(a, b)
    if m.endswith("frau"):
        m = m[:-4]
    elif m.endswith("mann"):
        m = m[:-4]
    # LE « E » SE RETIRE AVANT LE « IN », ET L'ORDRE COMPTE. Dans l'autre
    # sens, Cousin perdait son « in » et devenait « cous » tandis que Cousine
    # ne perdait que son « e » et restait « cousin » : la paire la plus
    # evidente du corpus etait la seule a ne pas etre reconnue.
    if m.endswith("e"):
        m = m[:-1]
    if m.endswith("in"):
        m = m[:-2]
    return m


def paire_de_genre(cartes):
    radicaux = {_radical(c.get("allemand")) for c in cartes}
    return len(radicaux) == 1


def collisions():
    """Deux mots allemands distincts, une seule reponse turque.

    Le defaut le plus grave du corpus, et le seul qu'aucune relecture par lots
    ne peut voir : le relecteur ne recoit qu'une centaine de cartes, la
    collision se joue entre deux lots. Une machine, elle, voit tout le corpus
    d'un coup.

    On ne compare qu'A L'INTERIEUR d'une categorie. « laut » (adjectif, fort)
    et « der Laut » (nom, le son) ne sont pas en concurrence sur une carte :
    les paquets sont separes. Les fondre produirait du bruit, exactement comme
    fondre `das Alter` et `der Alter` cote allemand avait produit 25 faux
    positifs.
    """
    tout = toutes_les_cartes()
    total = 0
    lignes = []
    genres = []
    for nom in sorted(tout):
        par_turc = {}
        for c in tout[nom]:
            tr = (c.get("turc") or "").strip().lower()
            de = (c.get("allemand") or "").strip()
            if not tr or not de:
                continue
            par_turc.setdefault(tr, [])
            # Le meme mot allemand peut figurer dans deux themes : ce n'est
            # pas une collision, c'est un doublon de corpus.
            if de not in [x["allemand"] for x in par_turc[tr]]:
                par_turc[tr].append(c)
        tous = [(tr, v) for tr, v in par_turc.items() if len(v) > 1]
        groupes = [g for g in tous if not paire_de_genre(g[1])]
        genres.extend((nom, tr, v) for tr, v in tous if paire_de_genre(v))
        groupes.sort(key=lambda g: (-len(g[1]), g[0]))
        if not groupes:
            continue
        total += sum(len(v) for _, v in groupes)
        lignes.append("\n## %s (%d reponses turques pour %d mots allemands)\n"
                      % (nom, len(groupes), sum(len(v) for _, v in groupes)))
        for tr, v in groupes:
            mots = ", ".join("%s (%s)" % (x["allemand"], x["niveau"]) for x in v)
            lignes.append("- **%s** ← %s" % (tr, mots))
            for x in v:
                if x.get("sens_fr"):
                    lignes.append("    - %s : %s" % (x["allemand"], x["sens_fr"]))
        lignes.append("")

    if not os.path.isdir(SORTIE):
        os.makedirs(SORTIE)
    chemin = os.path.join(SORTIE, "collisions.md")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Collisions turques — le controle mecanique\n\n")
        f.write("Produit par `python tests/relecture_tr.py --collisions`. ")
        f.write("**Aucune correction appliquee.**\n\n")
        f.write("Chaque ligne est un mot turc qui repond a PLUSIEURS mots ")
        f.write("allemands distincts de la meme categorie. La carte devient ")
        f.write("indecidable : quoi que l'apprenant reponde, il ne peut pas ")
        f.write("avoir raison.\n\n")
        f.write("Toutes ne sont pas des erreurs — deux quasi-synonymes ")
        f.write("allemands peuvent legitimement partager un mot turc si la ")
        f.write("langue n'en a pas deux. Mais chacune doit etre REGARDEE, et ")
        f.write("aucune relecture par lots ne peut les voir : le relecteur ne ")
        f.write("recoit qu'une centaine de cartes a la fois.\n")
        f.write("\n".join(lignes))
        if genres:
            f.write("\n\n---\n\n# Paires de genre — vues, et acceptees\n\n")
            f.write("Ces %d groupes ne sont PAS des collisions a corriger. "
                    % len(genres))
            f.write("Le turc n'a pas de genre grammatical et ne feminise pas ")
            f.write("le nom de metier : « uzman » est la bonne reponse pour ")
            f.write("`der Experte` comme pour `die Expertin`. Inventer une ")
            f.write("forme feminine pour departager les deux cartes ")
            f.write("enseignerait une regle qui n'existe pas dans la langue.\n\n")
            f.write("Ils sont reconnus mecaniquement (voir `paire_de_genre`) ")
            f.write("et sortis du decompte, pour qu'une relance du controle ne ")
            f.write("les remette pas dans la pile a chaque fois.\n\n")
            for nom, tr, v in sorted(genres):
                mots = ", ".join(x["allemand"] for x in v)
                f.write("- *%s* — **%s** ← %s\n" % (nom, tr, mots))
        f.write("\n")
    print("  ecrit : relecture_tr/collisions.md  (%d cartes a regarder, "
          "%d paires de genre acceptees)" % (total, len(genres)))
    return 0


# ------------------------------------------------------------------ 2. les lots

CONSIGNE = u"""# Consigne de relecture — traduction turque de Wortando

Tu relis la traduction TURQUE d'un cours d'allemand. Le fichier joint contient
une centaine de cartes.

## Ce qui est la source, et ce qui ne l'est pas

- **L'allemand est l'original.** C'est lui que la traduction turque doit rendre.
- **Le francais est donne uniquement pour fixer le sens voulu**, quand le mot
  allemand est ambigu hors contexte. Ne juge pas la qualite du francais, et ne
  reproche pas au turc de s'ecarter du francais s'il rend bien l'allemand.
- **Le turc est ce que tu juges.**

## Ce qu'on te demande de signaler

1. `contresens` — la traduction turque ne veut pas dire ce que dit l'allemand.
2. `phrase_infidele` — la phrase turque ne dit pas ce que dit la phrase
   allemande (sens, temps, aspect, personne, negation).
3. `turc_peu_naturel` — c'est comprehensible mais aucun locuteur ne le dirait
   ainsi ; donne la formulation naturelle.
4. `registre` — le turc est trop familier ou trop soutenu pour le niveau
   annonce (A1 a C1), ou pour la situation de la phrase.
5. `incoherence` — deux champs de la MEME carte se contredisent (le mot est
   traduit d'une facon, la phrase d'une autre).

## Ce qu'on ne te demande PAS

- Ne juge pas le genre ni le pluriel allemands : ils ont deja ete verifies.
- Ne signale pas qu'un mot turc pourrait avoir un synonyme. On ne cherche pas
  la meilleure variante possible, on cherche ce qui est FAUX ou INUTILISABLE.
- Ne signale pas les collisions entre deux cartes : elles sont detectees
  mecaniquement sur le corpus entier, tu n'en vois qu'un fragment.
- Si tu hesites, ne signale pas. Une liste courte et sure vaut mieux qu'une
  liste longue a trier.

## Le format de ta reponse

Un tableau JSON, et rien d'autre. Un objet par signalement :

```json
[
  {
    "mot": "Vater",
    "champ": "traduction_tr",
    "verdict": "contresens",
    "suggestion": "baba — « ata » veut dire ancetre, pas pere"
  }
]
```

- `mot` : la valeur du champ `cle` de la carte, recopiee telle quelle.
- `champ` : `traduction_tr`, `exemple_tr`, ou pour un verbe `perfekt_tr`,
  `praeteritum_tr`, `konjunktiv2_tr`.
- `verdict` : un des cinq mots ci-dessus.
- `suggestion` : la correction, et en une phrase pourquoi.

Si tu ne trouves rien, reponds `[]`.

Enregistre ta reponse sous `verdict_<nom du lot>.json` dans le dossier
`relecture_tr/`.
"""


def faire_lots(categories, niveaux, taille_forcee):
    if not os.path.isdir(SORTIE):
        os.makedirs(SORTIE)

    with io.open(os.path.join(SORTIE, "CONSIGNE.md"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write(CONSIGNE)

    total_lots = total_cartes = 0
    for nom in categories:
        cartes = [c for c in CATEGORIES[nom]()
                  if c.get("niveau") in niveaux and c.get("turc")]
        # Les champs perdus (voir --suspects) sortent des lots : ils ne se
        # relisent pas, ils se refont. Les laisser dedans ferait juger a un
        # relecteur des donnees qui n'ont jamais ete une traduction.
        perdues = {id(c) for c, _, _ in _suspects(cartes)}
        exclues = len([c for c in cartes if id(c) in perdues])
        cartes = [c for c in cartes if id(c) not in perdues]
        if not cartes:
            if exclues:
                print("  %-12s  0 lot — %d cartes toutes perdues" % (nom, exclues))
            continue
        taille = taille_forcee or TAILLE.get(nom, TAILLE_DEFAUT)
        # UN LOT NE MELANGE PAS LES NIVEAUX. Le relecteur doit juger le
        # registre CONTRE le niveau annonce : un lot ou A1 et C1 se suivent
        # l'en empeche. Et ca permet de commencer par ce qui sert vraiment
        # aujourd'hui -- A1 et A2 -- sans attendre le reste.
        #
        # A l'interieur d'un niveau, l'ordre du corpus est conserve : les
        # cartes d'un meme theme restent ensemble, ce qui donne le contexte
        # qui fait voir une incoherence entre deux fiches voisines.
        n_lots = 0
        for niv in niveaux:
            du_niveau = [c for c in cartes if c.get("niveau") == niv]
            if not du_niveau:
                continue
            lots = [du_niveau[i:i + taille]
                    for i in range(0, len(du_niveau), taille)]
            for i, lot in enumerate(lots, 1):
                base = "%s_%s_lot_%02d" % (nom, niv, i)
                donnees = {
                    "lot": base,
                    "categorie": nom,
                    "niveau": niv,
                    "cartes": lot,
                }
                chemin = os.path.join(SORTIE, base + ".json")
                with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
                    json.dump(donnees, f, ensure_ascii=False, indent=1)
                    f.write("\n")
            n_lots += len(lots)
        print("  %-12s %2d lot(s) de %3d  — %4d cartes%s"
              % (nom, n_lots, taille, len(cartes),
                 ("  (%d ecartees, perdues)" % exclues) if exclues else ""))
        total_lots += n_lots
        total_cartes += len(cartes)

    print()
    print("  %d lots, %d cartes, niveaux %s" %
          (total_lots, total_cartes, ",".join(niveaux)))
    print("  consigne a joindre : relecture_tr/CONSIGNE.md")
    return 0


# ---------------------------------------------------------- 3. depouillement

def rapport():
    tout = toutes_les_cartes()
    connus = {c["cle"] for v in tout.values() for c in v if c.get("cle")}

    trouvailles, lus = [], 0
    noms = sorted(os.listdir(SORTIE)) if os.path.isdir(SORTIE) else []
    for nom in noms:
        if not nom.startswith("verdict_") or not nom.endswith(".json"):
            continue
        try:
            d = json.load(io.open(os.path.join(SORTIE, nom), encoding="utf-8"))
        except ValueError as e:
            print("  ! %s illisible : %s" % (nom, e))
            continue
        lus += 1
        for h in d if isinstance(d, list) else d.get("signalements", []):
            h["_source"] = nom
            trouvailles.append(h)

    if not lus:
        print("Aucun verdict_*.json dans %s." % SORTIE)
        return 1

    # Un signalement qui porte sur un mot absent du corpus est un mot invente
    # ou recopie de travers : il ne se corrige pas, il s'ecarte.
    fantomes = [h for h in trouvailles if h.get("mot") not in connus]
    reels = [h for h in trouvailles if h.get("mot") in connus]
    par_type = {}
    for h in reels:
        par_type.setdefault(h.get("verdict", "?"), []).append(h)

    print()
    print("RELECTURE CROISEE — TURC")
    print("  %d fichier(s), %d signalement(s)" % (lus, len(trouvailles)))
    if fantomes:
        print("  %d portent sur un mot absent du corpus (ignores)" % len(fantomes))
    print()
    for t in sorted(par_type, key=lambda k: -len(par_type[k])):
        print("  %-24s %3d" % (t, len(par_type[t])))

    chemin = os.path.join(SORTIE, "divergences_tr.md")
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Divergences de la relecture croisee (turc)\n\n")
        f.write("Produit par `python tests/relecture_tr.py --rapport`. ")
        f.write("**Aucune correction appliquee.** L'application est en ")
        f.write("service : ce qui remonte ici s'examine, ne s'applique pas ")
        f.write("en bloc.\n\n")
        f.write("Les collisions ne figurent pas : elles sont tranchees ")
        f.write("mecaniquement par `--collisions`, sur le corpus entier.\n")
        for t in sorted(par_type, key=lambda k: -len(par_type[k])):
            f.write("\n## %s (%d)\n\n" % (t, len(par_type[t])))
            for h in sorted(par_type[t], key=lambda x: str(x.get("mot", ""))):
                f.write("- **%s** — champ `%s`" % (h.get("mot", "?"),
                                                   h.get("champ", "?")))
                if h.get("suggestion"):
                    f.write("\n  - suggestion : %s" % h["suggestion"])
                f.write("\n")
    print()
    print("  ecrit : relecture_tr/divergences_tr.md")
    return 0


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    args = sys.argv[1:]
    if "--suspects" in args:
        return suspects()
    if "--collisions" in args:
        return collisions()
    if "--rapport" in args:
        return rapport()

    categories = list(CATEGORIES)
    niveaux = list(NIVEAUX)
    taille = None
    for i, a in enumerate(args):
        if a == "--categories" and i + 1 < len(args):
            categories = [c.strip() for c in args[i + 1].split(",")]
        elif a == "--niveaux" and i + 1 < len(args):
            niveaux = [n.strip().upper() for n in args[i + 1].split(",")]
        elif a == "--cartes" and i + 1 < len(args):
            taille = int(args[i + 1])
    inconnues = [c for c in categories if c not in CATEGORIES]
    if inconnues:
        print("Categorie inconnue : %s" % ", ".join(inconnues))
        print("Disponibles : %s" % ", ".join(sorted(CATEGORIES)))
        return 1
    return faire_lots(categories, niveaux, taille)


if __name__ == "__main__":
    sys.exit(main())
