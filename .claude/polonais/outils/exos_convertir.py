# -*- coding: utf-8 -*-
"""Brouillon compact -> fichier de correction de tests/lot_exos.py.

    python exos_convertir.py <brouillon.txt> <dossier du releve> <dossier de sortie> [langue=pl]

Ecrit pour pt (brouillon JSON aligne par debut de question), generalise pour
pl avec un brouillon TEXTE, plus sur a ecrire a la main qu'un JSON :

    jeu: perfektExercises
    moule: <regex>\t<remplacement>          (applique dans l'ordre)
    texte: <texte exact>\t<remplacement>    (idem, sans regex : une phrase recurrente)
    <rang>\t<traduction>\t<explication ou *>[\t{"hint": "...", ...}]

<rang> est le numero de la ligne dans le releve <jeu>.txt de exos_dump.py :
chaque rang doit figurer une fois, dans l'ordre, sinon refus (un decalage
d'une ligne collerait chaque traduction sur l'exercice voisin, en silence).
"-" pour une traduction que le releve ne demande pas.
extras : {"hint": ..., "question": ..., "correct": ..., "options": [...]}

Une valeur "*" (explication ou extra) est fabriquee a partir du FRANCAIS par
les moules du brouillon, appliques dans l'ordre. Un indice ou une question
que le releve demande et que l'entree ne donne pas vaut "*". Garde-fou :
refus s'il reste un mot francais distinctif, des chevrons, de l'alphabet
cyrillique ou arabe, dans un texte fabrique comme dans un texte ecrit.
"""
import io, json, os, re, sys

FRANCAIS = ["«", "»", " le ", " la ", " les ", " verbe", "personne", "avec ",
            "Avec ", " est ", " car ", " une ", " un ", " et ", " pas ",
            " se termine", " qui ", " dans ", " sur ",
            "masculin", "féminin", "neutre", "pluriel", "phrase", "Prétérit", "prétérit", " ici", "toujours", " donc ",
            " ou ", " en ", "être", "avoir", "é", "è", "à ", "ç"]
ETRANGER = re.compile("[Ѐ-ӿ؀-ۿ]")


def controle(v, ou, fr=""):
    for s in (v if isinstance(v, list) else [v]):
        if not isinstance(s, str) or not s.strip() or any(ord(c) < 32 for c in s):
            sys.exit("TEXTE VIDE OU CONTROLE dans %s : %r" % (ou, s))
        if ETRANGER.search(s):
            sys.exit("ALPHABET ETRANGER dans %s : %r" % (ou, s))
        for m in FRANCAIS:
            if m in s:
                sys.exit("FRANCAIS RESTANT %r dans %s :\n   fr : %s\n   pl : %s" % (m, ou, fr, s))
    return v


def fabriquer(fr, moules, ou):
    v = fr
    for motif, rempl in moules:
        v = re.sub(motif, rempl, v)
    return controle(v, ou, fr)


def lire_brouillon(chemin):
    jeu, moules, e = None, [], []
    for n, l in enumerate(io.open(chemin, encoding="utf-8"), 1):
        l = l.rstrip("\n")
        if not l.strip() or l.startswith("#"):
            continue
        if l.startswith("jeu:"):
            jeu = l[4:].strip()
        elif l.startswith("texte:"):
            m = (l[7:] if l[6:7] == " " else l[6:]).split("\t")   # remplacement litteral
            if len(m) != 2:
                sys.exit("TEXTE ligne %d : il faut <texte>TAB<remplacement>" % n)
            moules.append((re.escape(m[0]), m[1].replace("\\", "\\\\")))
        elif l.startswith("moule:"):
            m = (l[7:] if l[6:7] == " " else l[6:]).split("\t")   # un seul espace apres "moule:"
            if len(m) != 2:
                sys.exit("MOULE ligne %d : il faut <regex>TAB<remplacement>" % n)
            re.compile(m[0])
            moules.append((m[0], m[1]))
        else:
            c = l.split("\t")
            if len(c) not in (3, 4):
                sys.exit("LIGNE %d : %d colonnes" % (n, len(c)))
            extras = json.loads(c[3]) if len(c) == 4 else {}
            e.append((int(c[0]), c[1].strip(), c[2].strip(), extras))
    return jeu, moules, e


src, RELEVE, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
L = sys.argv[4] if len(sys.argv) > 4 else "pl"
CH = L[0].upper() + L[1:]
jeu, moules, brouillon = lire_brouillon(src)
releve = [json.loads(l) for l in io.open(os.path.join(RELEVE, jeu + ".txt"), encoding="utf-8") if l.strip()]
rangs = [b[0] for b in brouillon]
if rangs != list(range(len(releve))):
    manque = sorted(set(range(len(releve))) - set(rangs))
    sys.exit("RANGS : %d lignes pour %d au releve ; manquent %s ; ordre respecte : %s"
             % (len(rangs), len(releve), manque[:10], rangs == sorted(rangs)))
entrees = []
for r, (rang, trad, expl, extras) in zip(releve, brouillon):
    ou = "%s #%d (%s)" % (jeu, rang, r["_q"][:40])
    ent = {"question": r["_q"]}
    if "_cle" in r:
        ent["cle_translation"] = r["_cle"]
    if "translation" in r:
        ent["translation_" + L] = controle(trad, ou, r["translation"])
    elif trad != "-":
        sys.exit("TRADUCTION NON DEMANDEE %s" % ou)
    if "explanation" in r:
        ent["explanation_" + L] = (fabriquer(r["explanation"], moules, ou) if expl == "*"
                                   else controle(expl, ou, r["explanation"]))
    extras = dict(extras)
    for k in ("hint", "question"):
        if k in r and k not in extras:
            extras[k] = "*"
    for k, v in extras.items():
        if k not in r:
            sys.exit("EXTRA NON DEMANDE %s : %s" % (k, ou))
        if v == "*":
            v = fabriquer(r[k], moules, ou)
        else:
            controle(v, ou, json.dumps(r[k], ensure_ascii=False))
        if k in ("correct", "options"):
            if k == "options" and len(v) != len(r[k]["fr"]):
                sys.exit("OPTIONS %s : %d au lieu de %d" % (ou, len(v), len(r[k]["fr"])))
            ent[k + CH] = v
        else:
            ent[k + "_" + L] = v
    manque = [k for k in r if not k.startswith("_") and
              (k + "_" + L not in ent and k + CH not in ent)]
    if manque:
        sys.exit("CHAMP OUBLIE %s pour %s" % (manque, ou))
    entrees.append(ent)
sortie = os.path.join(SORTIE, "corr_" + jeu + ".json")
io.open(sortie, "w", encoding="utf-8").write(
    json.dumps({"jeu": jeu, "entrees": entrees}, ensure_ascii=False, indent=1) + "\n")
print("%s : %d entrees -> %s" % (jeu, len(entrees), sortie))
