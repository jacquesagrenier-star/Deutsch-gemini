# -*- coding: utf-8 -*-
"""L'ALLEMAND dans les donnees de l'espagnol (espanol/datos/).

    python espanol/de/poser.py etat
    python espanol/de/poser.py reste <fichier> [n] [--depuis k]
    python espanol/de/poser.py pose <lot.txt> [<lot2.txt> ...]
    python espanol/de/poser.py pose --essai <lot.txt>   # controles seuls, rien n'est ecrit
    python espanol/de/poser.py controle          # vraisemblance des champs poses

NE LE 1er NOV. 2026, copie de espanol/ar/poser.py (l'arabe, 15 oct.) pour
ouvrir l'espagnol aux germanophones (interface « de », decision de Jacques).
Un parcours DETERMINISTE de chaque fichier sert de numerotation, chaque
entree se pose par son numero, et trois garde-fous encadrent l'ecriture :

  1. la deuxieme colonne du lot est le mot espagnol (ou le debut de la question)
     de l'entree a ce numero ; s'il differe, RIEN n'est ecrit ;
  2. avant d'ecrire, le fichier doit se reproduire a l'octet pres une fois relu
     et reserialise (json.dumps indent=1, ensure_ascii=False) ;
  3. apres l'ecriture, on relit le fichier et on compare chaque champ pose.

Les champs allemands suivent la convention des autres langues : traduction_de /
exemple_de dans le corpus ; translation_de, hint_de, explanation_de,
question_de, correctDe, optionsDe dans les exercices ; exemple_<temps>_de pour
la phrase de chaque temps du verbe. Les lecteurs d'index.html (SUFFIXE_LANGUE,
SUFFIXE_CHAMEAU, RANGS_CARTE) les trouvent par le code « de ».

⚠️ « de » DESIGNAIT DEJA LA LANGUE APPRISE dans une partie du code (la voix,
l'ecoute, l'index de recherche). Les champs *_de, eux, n'existaient nulle part :
aucune donnee allemande n'en porte, et ce script n'ecrit que dans espanol/.

L'allemand s'ecrit en lettres latines : on ne peut pas, comme pour l'arabe,
exiger son alphabet. Le controle est donc different -- une traduction ne doit
pas recopier le francais ni l'anglais, et une phrase de quatre mots ou plus
doit porter au moins un mot-outil allemand (der, ist, und, nicht...).

FORME D'UN LOT (texte, UTF-8, une entree par ligne, colonnes separees par « | »)

    #fichier temas
    12|casa|das Haus|Unser Haus hat einen kleinen Garten.

    #fichier tiempos
    12|hablar|<preterito>|<imperfecto>|<perfecto>|<futuro>|<condicional>|<subjuntivo>
      la phrase allemande de chaque temps (verbos.json, exemple_<temps>_de) ; une
      colonne vide est permise SEULEMENT si le verbe n'a pas ce temps.

    #fichier ejercicios
    serEstarExercises|0|Mi hermana ___|Meine Schwester ist Krankenpflegerin.|=|Beruf: was sie IST -> ser.
      colonnes : jeu | indice | debut de la question | translation_de | hint_de |
      explanation_de | [question_de]
      « = » recopie le francais (un indice comme « (vivir) », identique dans
      toutes les langues). question_de n'est due que si question_en existe et
      differe du francais ; sinon la colonne est ignoree.
    Les options et la bonne reponse (optionsDe, correctDe) sont recopiees
    automatiquement quand elles sont identiques en francais et en anglais
    (des mots espagnols, donc neutres).

Une ligne vide ou commencant par « # » (hors #fichier) est ignoree.
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATOS = os.environ.get("ESSAI_DATOS") or os.path.join(RACINE, "espanol", "datos")
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
CORPUS = ["temas", "verbos", "adjetivos", "adverbios", "expresiones", "funcionales"]
TEMPS = ["preterito", "imperfecto", "perfecto", "futuro", "condicional", "subjuntivo"]
ESSAI = False   # pose --essai : tous les controles, aucune ecriture

# Les mots-outils qui signent une phrase allemande. Une phrase francaise,
# anglaise ou espagnole de quatre mots n'en porte presque jamais aucun (« die »
# et « was » sont anglais, mais rares ensemble avec le reste ; « in » et « an »
# sont trop ambigus et ne sont pas dans la liste).
OUTILS = set("""der die das den dem des ein eine einen einem einer eines kein keine keinen keinem
ist sind bin bist war waren hat habe hast haben hatte wird werden wurde würde würden kann
können konnte muss müssen musste soll sollte will wollen möchte möchtest
und oder aber nicht auch noch schon sehr nur gern gerne immer nie heute morgen gestern hier dort
ich du er sie es wir ihr mich dich sich uns euch mir dir ihm ihnen mein meine meinen dein deine
sein seine ihre unser unsere euer eure
mit von zu zum zur für auf bei nach aus über unter vor hinter neben zwischen ohne gegen um bis seit
wenn weil dass ob als wie was wer wo wohin woher warum wann man jetzt viel viele mehr
gibt geht kommt macht ja nein bitte danke etwas nichts alles""".split())
MOT = re.compile(u"[A-Za-zÀ-ÿß]+")


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
        if not (e.get("translation_de") and e.get("hint_de") and e.get("explanation_de")):
            return False
        if e.get("question_en") and e["question_en"] != e["question"] and not e.get("question_de"):
            return False
        return True
    if nom == "tiempos":
        return all(e.get("exemple_%s_de" % t) for t in TEMPS if e.get("exemple_" + t))
    return bool(e.get("traduction_de") and e.get("exemple_de"))


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
    suite = len(es)
    for num, (ctx, e) in enumerate(es):
        if len(sortie) >= n:
            suite = num
            break
        if num < depuis or fait(nom, e):
            continue
        if nom == "ejercicios":
            ligne = [ctx, e["question"], e.get("question_en", ""), e["translation"],
                     e["hint"], e["explanation"]]
        elif nom == "tiempos":
            ligne = [str(num), e["mot"]] + [e.get("exemple_" + t, "") for t in TEMPS]
        else:
            ligne = [str(num), e["mot"], e["traduction"], e.get("traduction_en", ""),
                     e["exemple"], e["exemple_fr"]]
            if nom == "temas":
                ligne.insert(2, (e.get("genre") or "") + " " + ctx)
        sortie.append("|".join(col(x) for x in ligne))
    print("\n".join(sortie))
    print("# %d lignes ; lot suivant : --depuis %d (sur %d)" % (len(sortie), suite, len(es)), file=sys.stderr)


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


def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def doute_allemand(texte, fr="", en="", es=""):
    """Pourquoi ce texte n'a pas l'air allemand (None s'il l'a)."""
    if not texte or not texte.strip():
        return "vide"
    t = norm(texte)
    mots = [m.lower() for m in MOT.findall(texte)]
    if len(mots) >= 4:
        if t in (norm(fr), norm(en)):
            return "identique au francais ou a l'anglais"
        if not OUTILS.intersection(mots) and t != norm(es):
            return "aucun mot-outil allemand"
    elif fr and t == norm(fr) and t != norm(es) and t != norm(en):
        return "identique au francais"
    return None


def exiger_allemand(nom, num, texte, fr="", en="", es=""):
    d = doute_allemand(texte, fr, en, es)
    if d:
        raise SystemExit("%s : %s au numero %s : %s" % (nom, d, num, texte))


def poser_corpus(nom, lignes):
    d, brut, chemin = charger(nom)
    if serialiser(d, brut) != brut:
        raise SystemExit(nom + " : le fichier ne se reproduit pas a l'identique, rien n'est ecrit")
    es = entrees(nom, d)
    voulus = {}
    for cols in lignes:
        if len(cols) != 4:
            raise SystemExit("%s : 4 colonnes attendues (num|mot|traduction_de|exemple_de) : %s" % (nom, cols))
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
        exiger_allemand(nom, num, trad, e.get("traduction"), e.get("traduction_en"), e.get("mot"))
        exiger_allemand(nom, num, ex, e.get("exemple_fr"), e.get("exemple_en"), e.get("exemple"))
        voulus[num] = (trad, ex)
    for num, (trad, ex) in voulus.items():
        es[num][1]["traduction_de"] = trad
        es[num][1]["exemple_de"] = ex
    if ESSAI:
        print("  %-12s %d entrees verifiees (essai, rien n'est ecrit)" % (nom, len(voulus)))
        return
    io.open(chemin, "w", encoding="utf-8", newline="").write(serialiser(d, brut))
    d2, _, _ = charger(nom)
    es2 = entrees(nom, d2)
    for num, (trad, ex) in voulus.items():
        e = es2[num][1]
        if e["traduction_de"] != trad or e["exemple_de"] != ex:
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
                exiger_allemand("tiempos " + t, num, phrase, e.get("exemple_%s_fr" % t),
                                e.get("exemple_%s_en" % t), e.get("exemple_" + t))
                champs["exemple_%s_de" % t] = phrase
            elif phrase:
                raise SystemExit("tiempos : %s n'a pas de temps %s, la colonne doit rester vide (numero %d)"
                                 % (e["mot"], t, num))
        voulus[num] = champs
    for num, champs in voulus.items():
        es[num][1].update(champs)
    if ESSAI:
        print("  %-12s %d entrees verifiees (essai, rien n'est ecrit)" % (nom, len(voulus)))
        return
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
        for champ, valeur, base in (("translation_de", trad, "translation"), ("explanation_de", expl, "explanation")):
            if valeur != e[base]:
                exiger_allemand("ejercicios %s[%d] %s" % (jeu, idx, champ), idx, valeur,
                                e.get(base), e.get(base + "_en"), e.get("question"))
        due_q = bool(e.get("question_en")) and e["question_en"] != e["question"]
        if due_q and not question:
            raise SystemExit("ejercicios : %s[%d] demande question_de (la question est traduite)" % (jeu, idx))
        if question == "=":
            question = e["question"]
        voulus.append((e, trad, hint, expl, question if due_q else None))
    for e, trad, hint, expl, question in voulus:
        e["translation_de"] = trad
        e["hint_de"] = hint
        e["explanation_de"] = expl
        if question is not None:
            e["question_de"] = question
        if "options" in e and "optionsEn" in e and e["options"] == e["optionsEn"]:
            e["optionsDe"] = list(e["options"])
        if "correct" in e and "correctEn" in e and e["correct"] == e["correctEn"]:
            e["correctDe"] = e["correct"]
    if ESSAI:
        print("  %-12s %d entrees verifiees (essai, rien n'est ecrit)" % (nom, len(voulus)))
        return
    io.open(chemin, "w", encoding="utf-8", newline="").write(serialiser(d, brut))
    d2, _, _ = charger(nom)
    es2 = {ctx: x for ctx, x in entrees(nom, d2)}
    es1 = {ctx: x for ctx, x in entrees(nom, d)}
    for ctx, x in es1.items():
        y = es2[ctx]
        for k in ("translation_de", "hint_de", "explanation_de", "question_de", "optionsDe", "correctDe"):
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


def controle():
    """Un allemand qui n'en est pas : champ identique au francais ou a
    l'anglais, ou phrase sans aucun mot-outil allemand ; et un indice recopie du
    francais alors que l'anglais l'avait traduit."""
    suspects = 0
    for nom in CORPUS + ["ejercicios"]:
        d, _, _ = charger(nom)
        for ctx, e in entrees(nom, d):
            if nom == "ejercicios":
                champs = (("translation_de", "translation", "question"), ("explanation_de", "explanation", ""),
                          ("hint_de", "hint", ""), ("question_de", "question", "question"))
            else:
                champs = [("traduction_de", "traduction", "mot"), ("exemple_de", "exemple_fr", "exemple")]
                if nom == "verbos":
                    for t in TEMPS:
                        champs.append(("exemple_%s_de" % t, "exemple_%s_fr" % t, "exemple_" + t))
            for cde, cfr, ces in champs:
                v = e.get(cde)
                if not v:
                    continue
                if cde == "hint_de" and v == e.get("hint"):
                    if e.get("hint_en") and e["hint_en"] != e["hint"]:
                        print("  %s %s : hint_de recopie du francais : %s" % (nom, ctx, v[:70]))
                        suspects += 1
                    continue
                if cde == "question_de":
                    continue
                cen = cfr + "_en" if not cfr.endswith("_fr") else cfr[:-3] + "_en"
                if cfr == "traduction":
                    cen = "traduction_en"
                doute = doute_allemand(v, e.get(cfr), e.get(cen), e.get(ces) if ces else "")
                if doute:
                    print("  %s %s : %s %s : %s" % (nom, ctx, cde, doute, v[:70]))
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
        global ESSAI
        ESSAI = "--essai" in a
        pose([x for x in a[1:] if x != "--essai"])
    elif a[0] == "controle":
        sys.exit(1 if controle() else 0)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
