# -*- coding: utf-8 -*-
"""L'arabe dans les donnees de l'ESPAGNOL (espanol/datos/).

    python espanol/ar/poser.py etat
    python espanol/ar/poser.py reste <fichier> [n] [--depuis k]
    python espanol/ar/poser.py pose <lot.txt> [<lot2.txt> ...]
    python espanol/ar/poser.py controle          # vraisemblance des champs poses

NE LE 13 OCT. 2026, copie de espanol/pt/poser.py (le portugais du Bresil,
v784) pour rendre l'espagnol complet aux arabophones (interface « ar »).
Meme principe que tests/corpus_langue.py pour l'allemand : un parcours
DETERMINISTE de chaque fichier sert de numerotation, chaque entree se pose par
son numero, et trois garde-fous encadrent l'ecriture :

  1. la deuxieme colonne du lot est le mot espagnol (ou le debut de la question)
     de l'entree a ce numero ; s'il differe, RIEN n'est ecrit ;
  2. avant d'ecrire, le fichier doit se reproduire a l'octet pres une fois relu
     et reserialise (json.dumps indent=1, ensure_ascii=False) ;
  3. apres l'ecriture, on relit le fichier et on compare chaque champ pose.

Les champs arabes suivent EXACTEMENT la convention de l'allemand :
traduction_ar / exemple_ar dans le corpus ; translation_ar, hint_ar,
explanation_ar, question_ar, correctAr, optionsAr dans les exercices ;
exemple_<temps>_ar pour la phrase de chaque temps du verbe (v785). Ce sont
les memes lecteurs d'index.html (SUFFIXE_LANGUE, SUFFIXE_CHAMEAU, RANGS_CARTE)
qui les lisent : rien n'est cable a part.

FORME D'UN LOT (texte, UTF-8, une entree par ligne, colonnes separees par « | »)

    #fichier temas
    12|casa|بيت|بيتنا له حديقة صغيرة.

    #fichier tiempos
    12|hablar|<preterito>|<imperfecto>|<perfecto>|<futuro>|<condicional>|<subjuntivo>
      la phrase arabe de chaque temps (verbos.json, exemple_<temps>_ar) ; une
      colonne vide est permise SEULEMENT si le verbe n'a pas ce temps.

    #fichier ejercicios
    serEstarExercises|0|Mi hermana ___|أختي ممرضة.|=|مهنة: ما هي عليه → ser.
      colonnes : jeu | indice | debut de la question | translation_ar | hint_ar |
      explanation_ar | [question_ar]
      « = » recopie le francais (un indice comme « (vivir) », identique dans
      toutes les langues). question_ar n'est due que si question_en existe et
      differe du francais ; sinon la colonne est ignoree.
    Les options et la bonne reponse (optionsAr, correctAr) sont recopiees
    automatiquement : elles sont identiques en francais et en anglais, donc
    neutres (des mots espagnols).

Une ligne vide ou commencant par « # » (hors #fichier) est ignoree.
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATOS = os.path.join(RACINE, "espanol", "datos")
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
CORPUS = ["temas", "verbos", "adjetivos", "adverbios", "expresiones", "funcionales"]
TEMPS = ["preterito", "imperfecto", "perfecto", "futuro", "condicional", "subjuntivo"]
ARABE = re.compile(u"[؀-ۿ]")


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
        if not (e.get("translation_ar") and e.get("hint_ar") and e.get("explanation_ar")):
            return False
        if e.get("question_en") and e["question_en"] != e["question"] and not e.get("question_ar"):
            return False
        return True
    if nom == "tiempos":
        return all(e.get("exemple_%s_ar" % t) for t in TEMPS if e.get("exemple_" + t))
    return bool(e.get("traduction_ar") and e.get("exemple_ar"))


def etat():
    total_f, total_t = 0, 0
    for nom in CORPUS + ["tiempos", "ejercicios"]:
        d, _, _ = charger("verbos" if nom == "tiempos" else nom)
        es = entrees("verbos" if nom == "tiempos" else nom, d)
        f = sum(1 for _, e in es if fait(nom, e))
        total_f += f
        total_t += len(es)
        print("  %-12s %5d / %5d" % (nom, f, len(es)))
    print("  %-12s %5d / %5d" % ("TOTAL", total_f, total_t))


def col(s):
    return str(s if s is not None else "").replace("|", "¦").replace("\n", " ")


def reste(nom, n, depuis):
    d, _, _ = charger("verbos" if nom == "tiempos" else nom)
    es = entrees("verbos" if nom == "tiempos" else nom, d)
    sortie = []
    for num, (ctx, e) in enumerate(es):
        if num < depuis or fait(nom, e):
            continue
        if nom == "ejercicios":
            ligne = [ctx, e["question"], e.get("question_en", ""), e["translation"],
                     e["hint"], e["explanation"]]
        elif nom == "tiempos":
            ligne = [str(num), e["mot"]] + [e.get("exemple_" + t, "") for t in TEMPS]
        else:
            ligne = [str(num), e["mot"], e["traduction"], e["exemple"], e["exemple_fr"]]
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


def exiger_arabe(nom, num, texte):
    if not ARABE.search(texte):
        raise SystemExit("%s : pas d'arabe au numero %s : %s" % (nom, num, texte))


def poser_corpus(nom, lignes):
    d, brut, chemin = charger(nom)
    if serialiser(d, brut) != brut:
        raise SystemExit(nom + " : le fichier ne se reproduit pas a l'identique, rien n'est ecrit")
    es = entrees(nom, d)
    voulus = {}
    for cols in lignes:
        if len(cols) != 4:
            raise SystemExit("%s : 4 colonnes attendues (num|mot|traduction_ar|exemple_ar) : %s" % (nom, cols))
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
        if len(ex) < 6:
            raise SystemExit("%s : phrase trop courte au numero %d : %s" % (nom, num, ex))
        exiger_arabe(nom, num, trad)
        exiger_arabe(nom, num, ex)
        voulus[num] = (trad, ex)
    for num, (trad, ex) in voulus.items():
        es[num][1]["traduction_ar"] = trad
        es[num][1]["exemple_ar"] = ex
    io.open(chemin, "w", encoding="utf-8", newline="").write(serialiser(d, brut))
    d2, _, _ = charger(nom)
    es2 = entrees(nom, d2)
    for num, (trad, ex) in voulus.items():
        e = es2[num][1]
        if e["traduction_ar"] != trad or e["exemple_ar"] != ex:
            raise SystemExit("%s : relecture differente au numero %d" % (nom, num))
    print("  %-12s %d entrees posees" % (nom, len(voulus)))


def poser_tiempos(lignes):
    nom = "verbos"
    d, brut, chemin = charger(nom)
    if serialiser(d, brut) != brut:
        raise SystemExit(nom + " : le fichier ne se reproduit pas a l'identique, rien n'est ecrit")
    es = entrees(nom, d)
    voulus = {}
    for cols in lignes:
        if len(cols) != 2 + len(TEMPS):
            raise SystemExit("tiempos : %d colonnes attendues (num|verbe|%s) : %s"
                             % (2 + len(TEMPS), "|".join(TEMPS), cols))
        num = int(cols[0])
        if num >= len(es):
            raise SystemExit("tiempos : numero %d hors du fichier" % num)
        e = es[num][1]
        if e["mot"] != cols[1]:
            raise SystemExit("tiempos : au numero %d le verbe est « %s », pas « %s » -- rien n'est ecrit"
                             % (num, e["mot"], cols[1]))
        champs = {}
        for t, phrase in zip(TEMPS, cols[2:]):
            if e.get("exemple_" + t):
                if not phrase:
                    raise SystemExit("tiempos : %s n'a pas sa phrase %s au numero %d" % (e["mot"], t, num))
                exiger_arabe("tiempos " + t, num, phrase)
                champs["exemple_%s_ar" % t] = phrase
            elif phrase:
                raise SystemExit("tiempos : %s n'a pas de temps %s, la colonne doit rester vide (numero %d)"
                                 % (e["mot"], t, num))
        voulus[num] = champs
    for num, champs in voulus.items():
        es[num][1].update(champs)
    io.open(chemin, "w", encoding="utf-8", newline="").write(serialiser(d, brut))
    d2, _, _ = charger(nom)
    es2 = entrees(nom, d2)
    for num, champs in voulus.items():
        for k, v in champs.items():
            if es2[num][1].get(k) != v:
                raise SystemExit("tiempos : relecture differente au numero %d (%s)" % (num, k))
    print("  %-12s %d verbes poses" % ("tiempos", len(voulus)))


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
        for champ, valeur in (("translation_ar", trad), ("explanation_ar", expl)):
            exiger_arabe("ejercicios %s[%d] %s" % (jeu, idx, champ), idx, valeur)
        due_q = bool(e.get("question_en")) and e["question_en"] != e["question"]
        if due_q and not question:
            raise SystemExit("ejercicios : %s[%d] demande question_ar (la question est traduite)" % (jeu, idx))
        if question == "=":
            question = e["question"]
        voulus.append((e, trad, hint, expl, question if due_q else None))
    for e, trad, hint, expl, question in voulus:
        e["translation_ar"] = trad
        e["hint_ar"] = hint
        e["explanation_ar"] = expl
        if question is not None:
            e["question_ar"] = question
        if "options" in e and "optionsEn" in e and e["options"] == e["optionsEn"]:
            e["optionsAr"] = list(e["options"])
        if "correct" in e and "correctEn" in e and e["correct"] == e["correctEn"]:
            e["correctAr"] = e["correct"]
    io.open(chemin, "w", encoding="utf-8", newline="").write(serialiser(d, brut))
    d2, _, _ = charger(nom)
    es2 = {ctx: x for ctx, x in entrees(nom, d2)}
    es1 = {ctx: x for ctx, x in entrees(nom, d)}
    for ctx, x in es1.items():
        y = es2[ctx]
        for k in ("translation_ar", "hint_ar", "explanation_ar", "question_ar", "optionsAr", "correctAr"):
            if x.get(k) != y.get(k):
                raise SystemExit("ejercicios : relecture differente pour " + ctx)
    print("  %-12s %d exercices poses" % (nom, len(voulus)))


def pose(chemins):
    for chemin in chemins:
        lots = lire_lot(chemin)
        for nom, lignes in lots.items():
            if nom == "ejercicios":
                poser_exercices(lignes)
            elif nom == "tiempos":
                poser_tiempos(lignes)
            elif nom in CORPUS:
                poser_corpus(nom, lignes)
            else:
                raise SystemExit("fichier inconnu : " + nom)


LATIN = re.compile(u"[A-Za-zÀ-ÿ]{4,}")


def controle():
    """Un arabe qui n'en est pas : champ identique au francais ou a l'anglais,
    sans lettre arabe, ou portant un mot latin de 4 lettres ou plus qui n'est
    pas dans la phrase espagnole (un mot espagnol cite est legitime)."""
    suspects = 0
    for nom in CORPUS + ["ejercicios"]:
        d, _, _ = charger(nom)
        for ctx, e in entrees(nom, d):
            if nom == "ejercicios":
                champs = (("translation_ar", "translation"), ("explanation_ar", "explanation"),
                          ("hint_ar", "hint"), ("question_ar", "question"))
                source = e.get("question", "") + " " + " ".join(e.get("options", []) or []) \
                    + " " + " ".join(e.get("answers", []) or [])
            else:
                champs = [("traduction_ar", "traduction"), ("exemple_ar", "exemple_fr")]
                source = e.get("exemple", "") + " " + e.get("mot", "")
                if nom == "verbos":
                    for t in TEMPS:
                        champs.append(("exemple_%s_ar" % t, "exemple_%s_fr" % t))
                        source += " " + e.get("exemple_" + t, "")
            source = source.lower()
            for car, cfr in champs:
                v = e.get(car)
                if not v:
                    continue
                if car == "hint_ar" and v == e.get("hint"):
                    continue        # un indice neutre « (vivir) » recopie
                if not ARABE.search(v):
                    print("  %s %s : %s sans arabe : %s" % (nom, ctx, car, v[:70]))
                    suspects += 1
                    continue
                if v == e.get(cfr):
                    print("  %s %s : %s identique au francais : %s" % (nom, ctx, car, v[:70]))
                    suspects += 1
                    continue
                for m in LATIN.findall(v):
                    if m.lower() not in source and m.lower() not in ("ser", "estar", "hay", "usted", "ustedes", "vosotros"):
                        print("  %s %s : %s mot latin « %s » : %s" % (nom, ctx, car, m, v[:70]))
                        suspects += 1
                        break
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
