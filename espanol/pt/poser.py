# -*- coding: utf-8 -*-
"""Le portugais du Bresil dans les donnees de l'ESPAGNOL (espanol/datos/).

    python espanol/pt/poser.py etat
    python espanol/pt/poser.py reste <fichier> [n] [--depuis k]
    python espanol/pt/poser.py pose <lot.txt> [<lot2.txt> ...]
    python espanol/pt/poser.py controle          # vraisemblance des champs poses

NE LE 13 OCT. 2026 pour rendre l'espagnol complet aux lusophones (interface
« pt »). Meme principe que tests/corpus_langue.py pour l'allemand : un parcours
DETERMINISTE de chaque fichier sert de numerotation, chaque entree se pose par
son numero, et trois garde-fous encadrent l'ecriture :

  1. la deuxieme colonne du lot est le mot espagnol (ou le debut de la question)
     de l'entree a ce numero ; s'il differe, RIEN n'est ecrit ;
  2. avant d'ecrire, le fichier doit se reproduire a l'octet pres une fois relu
     et reserialise (json.dumps indent=1, ensure_ascii=False) ;
  3. apres l'ecriture, on relit le fichier et on compare chaque champ pose.

Les champs portugais suivent EXACTEMENT la convention de l'allemand (v765) :
traduction_pt / exemple_pt dans le corpus ; translation_pt, hint_pt,
explanation_pt, question_pt, correctPt, optionsPt dans les exercices. Ce sont
les memes lecteurs d'index.html (SUFFIXE_LANGUE, SUFFIXE_CHAMEAU, RANGS_CARTE)
qui les lisent : rien n'est cable a part.

FORME D'UN LOT (texte, UTF-8, une entree par ligne, colonnes separees par « | »)

    #fichier temas
    12|casa|a casa|Nossa casa tem um jardim pequeno.

    #fichier ejercicios
    serEstarExercises|0|Mi hermana ___|Minha irmã é enfermeira.|=|Uma profissão: o que ela É → ser.
      colonnes : jeu | indice | debut de la question | translation_pt | hint_pt |
      explanation_pt | [question_pt]
      « = » recopie le francais (un indice comme « (vivir) », identique dans
      toutes les langues). question_pt n'est due que si question_en existe et
      differe du francais ; sinon la colonne est ignoree.
    Les options et la bonne reponse (optionsPt, correctPt) sont recopiees
    automatiquement : elles sont identiques en francais et en anglais, donc
    neutres (des mots espagnols).

Une ligne vide ou commencant par « # » (hors #fichier) est ignoree.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATOS = os.path.join(RACINE, "espanol", "datos")
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
CORPUS = ["temas", "verbos", "adjetivos", "adverbios", "expresiones", "funcionales"]


def charger(nom):
    chemin = os.path.join(DATOS, nom + ".json")
    brut = io.open(chemin, encoding="utf-8", newline="").read()
    return json.loads(brut), brut, chemin


def serialiser(donnees, brut):
    t = json.dumps(donnees, ensure_ascii=False, indent=1)
    if brut.endswith("\n"):
        t += "\n"
    if "\r\n" in brut:
        t = t.replace("\n", "\r\n")
    return t


def entrees(nom, donnees):
    """Les entrees du fichier, dans un ordre fixe : (contexte, entree)."""
    out = []
    if nom == "temas":
        for t in donnees["themes"]:
            for m in t.get("mots", []):
                out.append((t.get("niveau", "") + " " + t.get("id", ""), m))
    elif nom == "ejercicios":
        for jeu, liste in donnees["jeux"].items():
            for i, x in enumerate(liste):
                out.append((jeu + "|" + str(i), x))
    else:
        for niv in NIVEAUX:
            for m in donnees.get(niv, []):
                out.append((niv, m))
    return out


def fait(nom, e):
    if nom == "ejercicios":
        if not (e.get("translation_pt") and e.get("hint_pt") and e.get("explanation_pt")):
            return False
        if e.get("question_en") and e["question_en"] != e["question"] and not e.get("question_pt"):
            return False
        return True
    return bool(e.get("traduction_pt") and e.get("exemple_pt"))


def etat():
    total_f, total_t = 0, 0
    for nom in CORPUS + ["ejercicios"]:
        d, _, _ = charger(nom)
        es = entrees(nom, d)
        f = sum(1 for _, e in es if fait(nom, e))
        total_f += f
        total_t += len(es)
        print("  %-12s %5d / %5d" % (nom, f, len(es)))
    print("  %-12s %5d / %5d" % ("TOTAL", total_f, total_t))


def col(s):
    return str(s if s is not None else "").replace("|", "¦").replace("\n", " ")


def reste(nom, n, depuis):
    d, _, _ = charger(nom)
    es = entrees(nom, d)
    sortie = []
    for num, (ctx, e) in enumerate(es):
        if num < depuis or fait(nom, e):
            continue
        if nom == "ejercicios":
            ligne = [ctx, e["question"], e.get("question_en", ""), e["translation"], e["translation_en"],
                     e["hint"], e["hint_en"], e["explanation"], e["explanation_en"]]
        else:
            ligne = [str(num), e["mot"], e["traduction"], e["traduction_en"],
                     e["exemple"], e["exemple_fr"], e["exemple_en"]]
            if nom == "temas":
                ligne.insert(2, (e.get("genre") or "") + " " + ctx)
        sortie.append("|".join(col(x) for x in ligne))
        if len(sortie) >= n:
            break
    print("\n".join(sortie))
    print("# %d lignes" % len(sortie), file=sys.stderr)


def lire_lot(chemin):
    """{fichier: [colonnes...]} -- un lot peut porter plusieurs fichiers."""
    lots = {}
    nom = None
    for brute in io.open(chemin, encoding="utf-8"):
        ligne = brute.rstrip("\r\n")
        if ligne.startswith("#fichier"):
            nom = ligne.split(None, 1)[1].strip()
            lots.setdefault(nom, [])
            continue
        if not ligne.strip() or ligne.startswith("#"):
            continue
        if nom is None:
            raise SystemExit("ligne avant tout #fichier : " + ligne)
        lots[nom].append([c.strip() for c in ligne.split("|")])
    return lots


def poser_corpus(nom, lignes):
    d, brut, chemin = charger(nom)
    if serialiser(d, brut) != brut:
        raise SystemExit(nom + " : le fichier ne se reproduit pas a l'identique, rien n'est ecrit")
    es = entrees(nom, d)
    voulus = {}
    for cols in lignes:
        if len(cols) != 4:
            raise SystemExit("%s : 4 colonnes attendues (num|mot|traduction_pt|exemple_pt) : %s" % (nom, cols))
        num, mot, trad, ex = cols
        num = int(num)
        if num >= len(es):
            raise SystemExit("%s : numero %d hors du fichier" % (nom, num))
        e = es[num][1]
        if e["mot"] != mot:
            raise SystemExit("%s : au numero %d le mot est « %s », pas « %s » -- rien n'est ecrit"
                             % (nom, num, e["mot"], mot))
        if not trad or not ex:
            raise SystemExit("%s : champ vide au numero %d" % (nom, num))
        if len(ex) < 8:
            raise SystemExit("%s : phrase trop courte au numero %d : %s" % (nom, num, ex))
        voulus[num] = (trad, ex)
    for num, (trad, ex) in voulus.items():
        es[num][1]["traduction_pt"] = trad
        es[num][1]["exemple_pt"] = ex
    io.open(chemin, "w", encoding="utf-8", newline="").write(serialiser(d, brut))
    d2, _, _ = charger(nom)
    es2 = entrees(nom, d2)
    for num, (trad, ex) in voulus.items():
        e = es2[num][1]
        if e["traduction_pt"] != trad or e["exemple_pt"] != ex:
            raise SystemExit("%s : relecture differente au numero %d" % (nom, num))
    print("  %-12s %d entrees posees" % (nom, len(voulus)))


def poser_exercices(lignes):
    nom = "ejercicios"
    d, brut, chemin = charger(nom)
    if serialiser(d, brut) != brut:
        raise SystemExit(nom + " : le fichier ne se reproduit pas a l'identique, rien n'est ecrit")
    voulus = []
    for cols in lignes:
        if len(cols) not in (6, 7):
            raise SystemExit("ejercicios : 6 ou 7 colonnes attendues : %s" % cols)
        jeu, idx, debut, trad, hint, expl = cols[:6]
        question = cols[6] if len(cols) == 7 else ""
        liste = d["jeux"].get(jeu)
        if liste is None:
            raise SystemExit("ejercicios : jeu inconnu " + jeu)
        idx = int(idx)
        if idx >= len(liste):
            raise SystemExit("ejercicios : %s[%d] hors de la liste" % (jeu, idx))
        e = liste[idx]
        if not e["question"].startswith(debut[:20]):
            raise SystemExit("ejercicios : %s[%d] commence par « %s », pas « %s » -- rien n'est ecrit"
                             % (jeu, idx, e["question"][:40], debut))
        if hint == "=":
            hint = e["hint"]
        if trad == "=":
            trad = e["translation"]
        if expl == "=":
            expl = e["explanation"]
        if not trad or not hint or not expl:
            raise SystemExit("ejercicios : champ vide pour %s[%d]" % (jeu, idx))
        due_q = bool(e.get("question_en")) and e["question_en"] != e["question"]
        if due_q and not question:
            raise SystemExit("ejercicios : %s[%d] demande question_pt (la question est traduite)" % (jeu, idx))
        if question == "=":
            question = e["question"]
        voulus.append((e, trad, hint, expl, question if due_q else None))
    for e, trad, hint, expl, question in voulus:
        e["translation_pt"] = trad
        e["hint_pt"] = hint
        e["explanation_pt"] = expl
        if question is not None:
            e["question_pt"] = question
        if "options" in e and "optionsEn" in e and e["options"] == e["optionsEn"]:
            e["optionsPt"] = list(e["options"])
        if "correct" in e and "correctEn" in e and e["correct"] == e["correctEn"]:
            e["correctPt"] = e["correct"]
    io.open(chemin, "w", encoding="utf-8", newline="").write(serialiser(d, brut))
    d2, _, _ = charger(nom)
    for (e, trad, hint, expl, question) in voulus:
        pass
    es2 = {ctx: x for ctx, x in entrees(nom, d2)}
    es1 = {ctx: x for ctx, x in entrees(nom, d)}
    for ctx, x in es1.items():
        y = es2[ctx]
        for k in ("translation_pt", "hint_pt", "explanation_pt", "question_pt", "optionsPt", "correctPt"):
            if x.get(k) != y.get(k):
                raise SystemExit("ejercicios : relecture differente pour " + ctx)
    print("  %-12s %d exercices poses" % (nom, len(voulus)))


def pose(chemins):
    for chemin in chemins:
        lots = lire_lot(chemin)
        for nom, lignes in lots.items():
            if nom == "ejercicios":
                poser_exercices(lignes)
            elif nom in CORPUS:
                poser_corpus(nom, lignes)
            else:
                raise SystemExit("fichier inconnu : " + nom)


FRANCAIS = {" le ", " la ", " les ", " des ", " une ", " est ", " et ", " dans ", " avec ", " pour ", " je ",
            " il ", " elle ", " nous ", " vous ", " ils ", " sont ", " ne ", " pas ", " que ", " qui ", " ce ",
            " cette ", " mon ", " ma ", " mes ", " ton ", " ta ", " tes ", " son ", " sa ", " ses ", " au ", " aux "}
ANGLAIS = {" the ", " and ", " is ", " are ", " with ", " you ", " he ", " she ", " they ", " we ", " this ",
           " that ", " my ", " your ", " his ", " her ", " their ", " of ", " to ", " in ", " on ", " at ", " it "}


def controle():
    """Un portugais qui ressemble a du francais ou a de l'anglais recopie."""
    suspects = 0
    for nom in CORPUS + ["ejercicios"]:
        d, _, _ = charger(nom)
        for ctx, e in entrees(nom, d):
            champs = (("traduction_pt", "traduction"), ("exemple_pt", "exemple_fr")) if nom != "ejercicios" \
                else (("translation_pt", "translation"), ("explanation_pt", "explanation"), ("hint_pt", "hint"), ("question_pt", "question"))
            for cpt, cfr in champs:
                v = e.get(cpt)
                if not v:
                    continue
                enc = " " + v.lower() + " "
                if v == e.get(cfr) and len(v) > 12 and any(m in enc for m in FRANCAIS):
                    print("  %s %s : %s identique au francais : %s" % (nom, ctx, cpt, v[:70]))
                    suspects += 1
                elif v == e.get(cfr + "_en", e.get(cfr.replace("_fr", "_en"))) and len(v) > 12 and any(m in enc for m in ANGLAIS):
                    print("  %s %s : %s identique a l'anglais : %s" % (nom, ctx, cpt, v[:70]))
                    suspects += 1
                elif sum(1 for m in FRANCAIS if m in enc) >= 2 and " não " not in enc and " você " not in enc:
                    print("  %s %s : %s sent le francais : %s" % (nom, ctx, cpt, v[:70]))
                    suspects += 1
                elif sum(1 for m in ANGLAIS if m in enc) >= 2:
                    print("  %s %s : %s sent l'anglais : %s" % (nom, ctx, cpt, v[:70]))
                    suspects += 1
    print("  %d suspect(s)" % suspects)
    return suspects


def main():
    a = sys.argv[1:]
    if not a or a[0] == "etat":
        etat()
    elif a[0] == "reste":
        nom = a[1]
        n = int(a[2]) if len(a) > 2 and a[2].isdigit() else 100
        depuis = int(a[a.index("--depuis") + 1]) if "--depuis" in a else 0
        reste(nom, n, depuis)
    elif a[0] == "pose":
        pose(a[1:])
    elif a[0] == "controle":
        sys.exit(1 if controle() else 0)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
