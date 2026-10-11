# -*- coding: utf-8 -*-
"""Les paquets a faire relire par d'autres IA (ChatGPT, Gemini) : l'espagnol.

    python fusion-espagnol/paquets_relecture.py      # ecrit relecture-espagnol/

Demande de Jacques (10 oct. 2026) : « partager toutes les phrases qu'on a
ecrites, les faire verifier par d'autres intelligences artificielles », et
« tout le contenu du programme, pour voir s'il manque des choses ».

Chaque fichier commence par la consigne a coller, puis les elements NUMEROTES
(FI = fiche, SE = ser/estar, PP = por/para, FA = faux amis, GU = gustar,
AC = accents, SC = scenes, MN = mots nouveaux, PR / IN / AD = exercices
generes). Un retour « SE-12 : ... » se rattache ainsi a sa ligne sans
ambiguite. Un lot depasse rarement 18 000 caracteres : il tient dans une
fenetre de discussion.

Methode (memoire « relecture croisee ») : contraste mecanique d'abord, autre
modele ensuite, et n'appliquer que les faits verifiables.
"""
import glob, io, json, os

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(RACINE, "espanol", "datos")
SORTIE = os.path.join(RACINE, "relecture-espagnol")
MAX = 18000

CONSIGNE = """CONSIGNE (à coller telle quelle)

Tu es professeur d'espagnol, de langue maternelle espagnole, et tu connais l'espagnol d'Espagne comme celui d'Amérique latine. Tu relis le contenu d'une application qui enseigne l'espagnol à des francophones (et à des anglophones). Pour chaque élément numéroté ci-dessous, vérifie :
1. L'espagnol est-il correct et naturel ? (grammaire, accords, accents écrits, ponctuation ¿ ¡)
2. Dans un exercice à choix, la bonne réponse (marquée ✔) est-elle la SEULE possible ? Une autre option serait-elle aussi acceptable ?
3. La traduction française et la traduction anglaise sont-elles fidèles ?
4. L'explication est-elle exacte ?
5. Un mot ou une tournure diffère-t-il entre l'Espagne et l'Amérique latine sans que ce soit signalé ?

Ne réécris pas ce qui est correct, et ne donne pas d'avis de style. Réponds UNIQUEMENT par un tableau :
n° | problème | correction proposée | certitude (sûr / probable / à discuter)
Si tout un lot est correct, réponds seulement « Rien à signaler ».

"""

CONSIGNE_PROGRAMME = """CONSIGNE (à coller telle quelle)

Tu es concepteur de programmes d'espagnol langue étrangère, et tu connais le Plan curricular del Instituto Cervantes et le Cadre européen (CECR). Voici le contenu complet d'une application qui enseigne l'espagnol à des francophones, du A1 au B2 (vocabulaire avec voix, fiches de grammaire, exercices, scènes illustrées). Dis-moi CE QUI MANQUE, par niveau :
1. les points de grammaire importants absents (ou trop peu travaillés) ;
2. les fonctions de communication absentes (se présenter, commander, demander son chemin, exprimer une opinion…) ;
3. les champs lexicaux ou des mots très fréquents absents ;
4. tout ce qui, dans ce qui existe, te semble mal placé dans les niveaux.
Classe tes réponses de la plus urgente à la moins urgente pour un débutant francophone. Sois concret : donne des exemples de ce qu'il faudrait ajouter. Ne répète pas ce qui existe déjà.

"""


LISEZ_MOI = """# Relecture de l'espagnol par d'autres IA

1. Ouvre un fichier (double-clic : il s'ouvre dans le Bloc-notes), Ctrl+A puis Ctrl+C.
2. Colle-le dans ChatGPT, puis dans Gemini (une nouvelle conversation par fichier).
3. Copie leur réponse (le tableau) et colle-la à Claude, en disant de quel fichier elle vient.
   Claude vérifie chaque remarque et n'applique que ce qui est vérifiable.

Par où commencer :
- 01-programme.md : ce qui MANQUE (grammaire, situations, mots). Le plus important avant l'annonce.
- 02-fiches : les 10 fiches de grammaire.
- 03 à 07 : toutes les phrases écrites (exercices, scènes, mots nouveaux). Chaque élément est numéroté (SE-12, SC-40…).

Pas encore à faire relire : les jeux « passé simple », « imparfait » et « subjonctif ». Ils avaient été
fabriqués mécaniquement et contiennent des phrases fausses : Claude les réécrit d'abord.
"""


def lire(nom):
    return json.load(io.open(os.path.join(DATOS, nom), encoding="utf-8"))


def fr_en(v):
    if isinstance(v, dict):
        return v.get("fr", ""), v.get("en", "")
    return v, v


def ecrire_lots(base, titre, consigne, blocs, maxi=MAX):
    """Coupe la liste de blocs en lots de `maxi` caracteres au plus."""
    lots, courant = [], []
    for b in blocs:
        if courant and sum(len(x) for x in courant) + len(b) > maxi:
            lots.append(courant)
            courant = []
        courant.append(b)
    if courant:
        lots.append(courant)
    noms = []
    for i, lot in enumerate(lots, 1):
        suffixe = "" if len(lots) == 1 else "-lot%d" % i
        nom = "%s%s.md" % (base, suffixe)
        entete = "# %s%s\n\n" % (titre, "" if len(lots) == 1 else " — lot %d sur %d" % (i, len(lots)))
        io.open(os.path.join(SORTIE, nom), "w", encoding="utf-8").write(entete + consigne + "\n".join(lot) + "\n")
        noms.append((nom, sum(len(x) for x in lot)))
    return noms


def exo(prefixe, i, e):
    q = e.get("question", "")
    rep = e.get("correct", "")
    opts = e.get("options") or []
    ch = " / ".join(("✔ " + o) if o == rep else o for o in opts) if opts else "réponse : ✔ " + rep
    return ("**%s-%d** %s\n- choix : %s\n- FR : %s\n- EN : %s\n- explication FR : %s\n- explication EN : %s\n"
            % (prefixe, i, q, ch, e.get("translation", ""), e.get("translation_en", ""),
               e.get("explanation", ""), e.get("explanation_en", "")))


def main():
    os.makedirs(SORTIE, exist_ok=True)
    for f in glob.glob(os.path.join(SORTIE, "*.md")):
        os.remove(f)
    faits = []

    # ---- 01. Le programme -------------------------------------------------
    temas = lire("temas.json")["themes"]
    gram = lire("grammaire.json")["fiches"]
    jeux = lire("ejercicios.json")["jeux"]
    lignes = ["## Structure\n",
              "- Niveaux : A1, A2, B1, B2 (vocabulaire) ; scènes de A1 à C1.",
              "- Chaque mot : article, pluriel, traduction FR et EN, phrase d'exemple ES/FR/EN, voix (Espagne ou Amérique latine au choix).",
              "- Séance du jour avec répétition espacée ; dictées ; dictionnaire espagnol-français (WikDict).",
              "- Variante Amérique latine : %d noms changent (piso → departamento…)." % len(lire("variantes.json")["noms"]), ""]
    for fichier, cle, nom in (("verbos.json", "infinitif", "Verbes (conjugués : présent, passé simple, imparfait, subjonctif)"),
                              ("adjetivos.json", "mot", "Adjectifs"), ("adverbios.json", "mot", "Adverbes"),
                              ("expresiones.json", "mot", "Expressions"), ("funcionales.json", "mot", "Mots-outils")):
        d = lire(fichier)
        lignes.append("- %s : %s" % (nom, ", ".join("%s %d" % (n, len(v)) for n, v in d.items())))
    lignes.append("\n## Fiches de grammaire (%d)\n" % len(gram))
    for g in gram:
        lignes.append("- **%s** — %s" % (fr_en(g["titre"])[0], fr_en(g["resume"])[0]))
    lignes.append("\n## Jeux d'exercices (%d)\n" % len(jeux))
    for n, j in jeux.items():
        lignes.append("- %s : %d questions (sujet : %s)" % (n, len(j), j[0].get("topic", "")))
    lignes.append("\n## Scènes illustrées\n\n- La classe, l'examen médical (de face, de dos), le marché (4 étals), le cabinet médical (blessure au genou). A1 : toucher et nommer ; A2-C1 : questions sur l'image (estar et prépositions ; pronoms, ser/estar, impératif d'usted, quantités ; relatives, passif ; futur de probabilité, deber de, si + subjonctif).")
    lignes.append("\n## Thèmes de vocabulaire (%d), avec leurs mots\n" % len(temas))
    for th in temas:
        lignes.append("- **%s (%s, %d mots)** : %s" % (th.get("nom_theme_es") or th["id"], th.get("niveau"), len(th["mots"]),
                                                       ", ".join(m["mot"] for m in th["mots"])))
    for fichier, cle, nom in (("verbos.json", "infinitif", "Verbes"), ("adjetivos.json", "mot", "Adjectifs"),
                              ("adverbios.json", "mot", "Adverbes"), ("expresiones.json", "mot", "Expressions"),
                              ("funcionales.json", "mot", "Mots-outils")):
        lignes.append("\n## %s, par niveau\n" % nom)
        for niv, v in lire(fichier).items():
            lignes.append("- **%s** : %s" % (niv, ", ".join(x.get(cle, "") for x in v)))
    # Le programme se juge d'un seul tenant : un lot sans les autres dirait
    # « il manque » ce qui est simplement dans le lot suivant.
    faits += ecrire_lots("01-programme", "Le programme d'espagnol de Wortando", CONSIGNE_PROGRAMME,
                         [l + "\n" for l in lignes], maxi=10 ** 6)

    # ---- 02. Les fiches ---------------------------------------------------
    blocs = []
    for i, g in enumerate(gram, 1):
        t = ["**FI-%d — %s** (%s)\n" % (i, fr_en(g["titre"])[0], fr_en(g["titre"])[1])]
        t.append("- règle FR : %s\n- règle EN : %s" % fr_en(g["regle"]))
        for k, l in enumerate(g.get("tableau", []), 1):
            d = fr_en(l[1])
            t.append("- tableau %d : %s | FR : %s | EN : %s%s" % (k, l[0], d[0], d[1], (" | exemple : " + " / ".join(dict.fromkeys(fr_en(l[2])))) if len(l) > 2 else ""))
        for k, e in enumerate(g.get("exemples", []), 1):
            d = fr_en(e[1])
            t.append("- exemple %d : %s | FR : %s | EN : %s" % (k, e[0], d[0], d[1]))
        t.append("- attention FR : %s\n- attention EN : %s\n" % fr_en(g.get("attention", "")))
        blocs.append("\n".join(t) + "\n")
    faits += ecrire_lots("02-fiches", "Les fiches de grammaire", CONSIGNE, blocs)

    # ---- 03-05. Les exercices ecrits a la main ---------------------------
    for base, titre, sets in (("03-exercices-ser-estar-por-para", "Exercices ser / estar et por / para",
                               (("SE", "serEstarExercises"), ("PP", "porParaExercises"))),
                              ("04-exercices-pieges", "Exercices faux amis, gustar, accents",
                               (("FA", "falsosAmigosExercises"), ("GU", "gustarExercises"), ("AC", "acentosExercises"))),
                              ("05-exercices-generes", "Exercices présent, infinitif, adverbes",
                               (("PR", "exercises"), ("IN", "infinitivExercises"), ("AD", "adverbienNuanceExercises")))):
        blocs = [exo(p, i, e) for p, n in sets for i, e in enumerate(jeux.get(n, []), 1)]
        faits += ecrire_lots(base, titre, CONSIGNE, blocs)

    # ---- 06. Les scenes ---------------------------------------------------
    blocs, k = [], 0
    for f in sorted(glob.glob(os.path.join(RACINE, "visuel", "prototype", "espanol", "*.json"))):
        if f.endswith("mots.json"):
            continue
        d = json.load(io.open(f, encoding="utf-8"))
        nom = os.path.basename(f)[:-5]
        for niv, c in d.get("couches", {}).items():
            for q in c.get("qs", []):
                k += 1
                ch = " / ".join(("✔ " + o) if j == 0 else o for j, o in enumerate(q["c"]))
                t = ("**SC-%d** (%s, %s) %s\n- choix : %s\n- phrase complète : %s\n- explication FR : %s\n- explication EN : %s\n"
                     % (k, nom, niv, q["q"], ch, q["phrase"], q["n"], q.get("n_en", "")))
                if q.get("latam"):
                    t += "- version Amérique latine : %s\n" % json.dumps(q["latam"], ensure_ascii=False)
                blocs.append(t)
    faits += ecrire_lots("06-scenes", "Les questions des scènes (les faits viennent de l'image)", CONSIGNE, blocs)

    # ---- 07. Les mots nouveaux -------------------------------------------
    aj = json.load(io.open(os.path.join(RACINE, "espanol", "ajouts", "mots-scenes.json"), encoding="utf-8"))
    blocs, k = [], 0
    for theme, ls in aj["ajouts"].items():
        for mot, art, pl, fr, en, ex, ex_fr, ex_en in ls:
            k += 1
            blocs.append("**MN-%d** %s %s (pluriel : %s) — FR : %s — EN : %s\n- exemple : %s | FR : %s | EN : %s\n"
                         % (k, art, mot, pl or "—", fr, en, ex, ex_fr, ex_en))
    for mot, v in aj["variantes"].items():
        k += 1
        blocs.append("**MN-%d** variante Amérique latine (Mexique) de « %s » : %s %s (pluriel : %s) — exemple : %s\n"
                     % (k, mot, v["genre"], v["mot"], v.get("pluriel"), v.get("exemple")))
    faits += ecrire_lots("07-mots-nouveaux", "Les mots ajoutés pour les scènes", CONSIGNE, blocs)

    io.open(os.path.join(SORTIE, "00-LISEZ-MOI.md"), "w", encoding="utf-8").write(LISEZ_MOI)
    for nom, n in faits:
        print("  %-48s %6d caracteres" % (nom, n))


if __name__ == "__main__":
    main()
