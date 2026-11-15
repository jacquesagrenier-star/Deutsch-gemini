# -*- coding: utf-8 -*-
"""Controle des textes Soins : dialogues, grammaire, ecrit (pflege/sources/LISEZ-MOI.md). Gratuit, sans navigateur.

    python tests/pflege_dialogues.py            # tout, strict : les 9 langues doivent etre la
    python tests/pflege_dialogues.py --partiel  # les traductions manquantes ne sont que signalees
    python tests/pflege_dialogues.py --relire   # la liste de ce que l'infirmiere doit valider
    python tests/pflege_dialogues.py --chars    # les caracteres a dire (devis de la voix)

Ce qu'il verifie :
  - LES CLES : chaque source a ses champs ; niveaux A2 / B1 / B2 (ecrit : B1-B2) ; identifiants uniques ;
  - LES DIALOGUES : debut, « va » vers un noeud, noeuds tous atteints, une reponse juste par noeud, une faute a son
    aide et pas de « va », une repetition revient au meme noeud, chaque reponse juste mene a une fin sans boucle,
    longueur selon le niveau ; personnes et visages connus ; le registre (Sie : aucune reponse juste en du ; du+Sie :
    chaque noeud dit le sien) ; les questions d'ecoute (3 options, « juste » valide) ;
  - LA GRAMMAIRE : 10 questions par serie, la reponse parmi les options, la phrase complete qui la contient, le
    renvoi vers une <section> d'index.html, les dialogues cites existent ;
  - L'ECRIT : chaque point de la fiche est couvert par le modele, la grille a ses quatre criteres ;
  - LES 9 LANGUES : chaque unite (objet qui a « fr ») a ses 8 traductions, non perimees, avec les memes balises <b>
    et les memes noms ; chaque nom a sa forme dans chaque langue ;
  - LES NOMBRES : une phrase allemande prononcee a chiffres a son « dit », en lettres ;
  - LE DERIVE : pflege/datos/ est a jour (refait en memoire et compare).
"""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "pflege", "outils"))
import textes as T  # noqa: E402

ARGS = sys.argv[1:]
PARTIEL = "--partiel" in ARGS
erreurs, avis = [], []
E, A = erreurs.append, avis.append
NIVEAUX = {"A2", "B1", "B2"}
AIRS = {"sourire", "question", "attentive", "surprise", "perplexe", "amuse"}
# Echanges (reponses de l'apprenant) d'un chemin, selon le niveau : l'annexe C demande 12 a 20 repliques.
LONGUEUR = {"A2": (6, 10), "B1": (6, 12), "B2": (6, 12)}
TUTOIEMENT = re.compile(r"\b(du|dich|dir|dein\w*|deine\w*)\b")
CHIFFRE = re.compile(r"\d")
SECTIONS = set(re.findall(r'<section[^>]*id="([A-Za-z0-9_]+)"', io.open(os.path.join(RACINE, "index.html"), encoding="utf-8").read()))
table = T.noms()
sans_noms = lambda s: T.GABARIT.sub(" ", s or "")


def gabarits(s):
    return sorted(set(m.group(1) for m in T.GABARIT.finditer(s or "")))


# ------------------------------------------------------------------ nombres et noms (sur la source)

def controle_nombres(famille, ident, d, prononce=True):
    for chemin, u in T.unites(d):
        t = u.get("t")
        if not isinstance(t, str) or not prononce or u.get("prononce") is False:
            continue
        t_res = T.remplacer(t, "de", table, [])
        if CHIFFRE.search(t_res):
            if "dit" not in u:
                E("%s/%s %s : chiffre sans lecture (« dit ») : %s" % (famille, ident, chemin, t))
            elif CHIFFRE.search(T.remplacer(u["dit"], "de", table, [], forme_dit=True)):
                E("%s/%s %s : la lecture garde un chiffre : %s" % (famille, ident, chemin, u["dit"]))


def controle_gabarits(famille, ident, d):
    for chemin, u in T.unites(d):
        for cle in ["t", "dit"] + T.LANGUES:
            v = u.get(cle)
            if isinstance(v, str):
                m = []
                T.remplacer(v, "de" if cle in ("t", "dit") else cle, table, m, forme_dit=(cle == "dit"))
                for x in m:
                    E("%s/%s %s : %s" % (famille, ident, chemin, x))


# ------------------------------------------------------------------ dialogues

def controle_dialogue(ident, d, ids_grammaire):
    ou = "dialogues/" + ident
    for cle in ("id", "numero", "niveau", "registre", "role", "personnes", "titre", "intro", "but", "grammaire",
                "redemittel", "debut", "noeuds", "ecouter"):
        if cle not in d:
            E("%s : clé « %s » absente" % (ou, cle))
    if d.get("id") != ident:
        E("%s : id « %s » différent du nom du fichier" % (ou, d.get("id")))
    niv = d.get("niveau")
    if niv not in NIVEAUX:
        E("%s : niveau « %s » (A2, B1 ou B2)" % (ou, niv))
    pers = table["de"]
    for p in [d.get("role")] + d.get("personnes", []):
        if p not in pers:
            E("%s : personne « %s » absente de noms.json" % (ou, p))
    for g in d.get("grammaire", []):
        if ids_grammaire and g not in ids_grammaire:
            (E if ids_grammaire else A)("%s : point de grammaire « %s » inconnu" % (ou, g))
    if not 5 <= len(d.get("redemittel", [])) <= 10:
        E("%s : %d Redemittel (5 à 10)" % (ou, len(d.get("redemittel", []))))
    noeuds = d.get("noeuds", {})
    if d.get("debut") not in noeuds:
        E("%s : début « %s » absent" % (ou, d.get("debut")))
        return
    registre = d.get("registre")
    for n, noeud in noeuds.items():
        reg = noeud.get("registre", registre)
        if registre == "du+Sie" and reg not in ("du", "Sie"):
            E("%s %s : registre du nœud (du ou Sie) absent" % (ou, n))
        lignes = noeud.get("dit", [])
        for r in lignes:
            verifier_ligne(ou + " " + n, r, d)
        choix = noeud.get("choix", [])
        if not any(not c.get("faux") and not c.get("repete") for c in choix):
            E("%s %s : aucune réponse juste" % (ou, n))
        for i, c in enumerate(choix):
            w = "%s %s choix %d" % (ou, n, i)
            if "t" not in c or "fr" not in c:
                E("%s : « t » ou « fr » absent" % w)
            if c.get("faux"):
                if "aide" not in c:
                    E("%s : faute sans « aide »" % w)
                if "va" in c:
                    E("%s : une faute ne mène nulle part (pas de « va »)" % w)
            elif c.get("repete"):
                if c.get("va") != n:
                    E("%s : une répétition revient au même nœud" % w)
            else:
                if "va" not in c:
                    E("%s : réponse juste sans « va »" % w)
                elif c["va"] is not None and c["va"] not in noeuds:
                    E("%s : « va » vers « %s », absent" % (w, c["va"]))
                if reg == "Sie" and TUTOIEMENT.search(sans_noms(c.get("t", ""))):
                    E("%s : réponse juste en du dans un nœud au Sie : %s" % (w, c["t"]))
            for r in c.get("puis", []):
                if "recit" in r:
                    E("%s : un récit dans « puis » (format des conversations : la réaction est une réplique ; le récit va dans le « dit » du nœud suivant)" % w)
                    continue
                verifier_ligne(w, r, d)
        if not lignes and n == d.get("debut"):
            E("%s %s : le début doit dire quelque chose" % (ou, n))
    # Atteints, fins, longueur
    atteints, longueurs = set(), []

    def marcher(n, pile, k):
        if n is None:
            longueurs.append(k)
            return
        if n in pile:
            E("%s : boucle par le nœud « %s »" % (ou, n))
            return
        atteints.add(n)
        for c in noeuds[n].get("choix", []):
            if c.get("faux") or c.get("repete") or c.get("va", "?") == "?":
                continue
            if c["va"] is None or c["va"] in noeuds:
                marcher(c["va"], pile | {n}, k + 1)
    marcher(d["debut"], frozenset(), 0)
    for n in noeuds:
        if n not in atteints:
            E("%s : nœud « %s » jamais atteint" % (ou, n))
    if niv in LONGUEUR and longueurs:
        lo, hi = LONGUEUR[niv]
        if min(longueurs) < lo or max(longueurs) > hi:
            E("%s : %d à %d échanges (attendu %d à %d au %s)" % (ou, min(longueurs), max(longueurs), lo, hi, niv))
    for i, q in enumerate(d.get("ecouter", [])):
        if len(q.get("options", [])) != 3 or not isinstance(q.get("juste"), int) or not 0 <= q["juste"] < 3:
            E("%s ecouter %d : trois options et « juste » de 0 à 2" % (ou, i))
    if not 3 <= len(d.get("ecouter", [])) <= 5:
        E("%s : %d questions d'écoute (3 à 5)" % (ou, len(d.get("ecouter", []))))
    return longueurs


def verifier_ligne(ou, r, d):
    if "recit" in r:
        if "fr" not in r["recit"]:
            E("%s : récit sans « fr »" % ou)
        return
    if r.get("qui") not in [d.get("role")] + d.get("personnes", []):
        E("%s : « qui » = « %s », hors des personnes du dialogue" % (ou, r.get("qui")))
    if r.get("air", "sourire") not in AIRS:
        E("%s : visage « %s » inconnu" % (ou, r.get("air")))
    if "t" not in r or "fr" not in r:
        E("%s : réplique sans « t » ou « fr »" % ou)


# ------------------------------------------------------------------ grammaire

def controle_grammaire(ident, d, ids_dialogues):
    ou = "grammaire/" + ident
    for cle in ("id", "cle", "numero", "niveau", "titre", "resume", "regle", "exemples", "renvoi", "serie"):
        if cle not in d:
            E("%s : clé « %s » absente" % (ou, cle))
    if not ident.startswith(d.get("id", "?")):
        E("%s : id « %s » ne commence pas le nom du fichier" % (ou, d.get("id")))
    if d.get("niveau") not in NIVEAUX:
        E("%s : niveau « %s »" % (ou, d.get("niveau")))
    if d.get("renvoi") is not None and d.get("renvoi") not in SECTIONS:
        E("%s : renvoi « %s » : pas de <section> de ce nom dans index.html" % (ou, d.get("renvoi")))
    for x in d.get("dialogues", []):
        if x not in ids_dialogues:
            E("%s : dialogue « %s » inconnu" % (ou, x))
    if not 3 <= len(d.get("exemples", [])) <= 6:
        E("%s : %d exemples (3 à 6)" % (ou, len(d.get("exemples", []))))
    serie = d.get("serie", [])
    if len(serie) != 10:
        E("%s : %d questions (10 attendues)" % (ou, len(serie)))
    for i, q in enumerate(serie):
        w = "%s serie %d" % (ou, i)
        typ = q.get("type")
        if "explication" not in q:
            E("%s : pas d'explication" % w)
        if typ == "trou":
            if q.get("t", "").count("___") != 1:
                E("%s : un seul « ___ » dans la question" % w)
            if q.get("juste") not in q.get("options", []):
                E("%s : la réponse n'est pas parmi les options" % w)
            if len(set(q.get("options", []))) != len(q.get("options", [])) or not 2 <= len(q.get("options", [])) <= 4:
                E("%s : 2 à 4 options, distinctes" % w)
            ph = q.get("phrase", {}).get("t", "")
            if q.get("t") and ph != q["t"].replace("___", q.get("juste", "")):
                E("%s : la phrase complète ne correspond pas à la question remplie : %s" % (w, ph))
        elif typ == "choix":
            if not isinstance(q.get("juste"), int) or not 0 <= q["juste"] < len(q.get("options", [])):
                E("%s : « juste » hors des options" % w)
            if "consigne" not in q:
                E("%s : choix sans consigne" % w)
        elif typ == "ordre":
            if len(q.get("morceaux", [])) < 3:
                E("%s : au moins trois morceaux" % w)
            ph = q.get("phrase", {}).get("t", "")
            if re.sub(r"[ ,.?!]", "", " ".join(q.get("morceaux", []))) != re.sub(r"[ ,.?!]", "", ph):
                E("%s : les morceaux ne refont pas la phrase : %s" % (w, ph))
        else:
            E("%s : type « %s » inconnu (trou, choix, ordre)" % (w, typ))
        if typ in ("trou", "ordre") and "phrase" not in q:
            E("%s : phrase complète absente" % w)


# ------------------------------------------------------------------ ecrit

def controle_ecrit(ident, d):
    ou = "ecrit/" + ident
    if ident.startswith("grille"):
        crit = [c.get("id") for c in d.get("criteres", [])]
        if crit != ["contenu", "forme", "correction", "vocabulaire"]:
            E("%s : les quatre critères du barème, dans l'ordre (contenu, forme, correction, vocabulaire)" % ou)
        for c in d.get("criteres", []):
            if [n.get("points") for n in c.get("niveaux", [])] != [5, 4, 3, 2, 1, 0]:
                E("%s %s : les niveaux 5 à 0" % (ou, c.get("id")))
        return
    if ident.startswith("briques"):
        if not d.get("groupes") or not all(g.get("briques") for g in d["groupes"]):
            E("%s : une banque de briques a des « groupes », chacun avec ses « briques »" % ou)
        return
    if d.get("id") != ident:
        E("%s : id « %s » différent du nom du fichier" % (ou, d.get("id")))
    for cle in ("id", "genre", "niveau", "titre", "consigne", "fiche", "points", "modele") + (("briques",) if d.get("examen") else ()):
        if cle not in d:
            E("%s : clé « %s » absente" % (ou, cle))
    if d.get("prononce") is not False:
        E("%s : « prononce »: false attendu (l'écrit ne se dit pas)" % ou)
    ids = [p.get("id") for p in d.get("points", [])]
    if len(set(ids)) != len(ids):
        E("%s : identifiants de points en double" % ou)
    couvre = d.get("modele", {}).get("couvre", [])
    for p in ids:
        if p not in couvre:
            E("%s : le modèle ne couvre pas le point « %s »" % (ou, p))
    for p in couvre:
        if p not in ids:
            E("%s : le modèle couvre « %s », absent des points" % (ou, p))
    for ref in ("grille", "briques"):
        g = d.get(ref)
        if isinstance(g, str) and not os.path.exists(os.path.join(T.SOURCES, "ecrit", g + ".json")):
            E("%s : %s « %s » absente" % (ou, ref, g))
    if d.get("examen") and (d.get("grille") != "grille-telc-pflege" or "modele_b1" not in d):
        E("%s : une tâche d'examen a la grille telc et un modèle B1" % ou)
    if d.get("genre") not in ("aufnahmebericht", "biografiebericht", "pflegebericht", "sturzprotokoll", "nachricht"):
        E("%s : genre « %s » inconnu" % (ou, d.get("genre")))


# ------------------------------------------------------------------ langues

def controle_langues(res):
    nb = 0
    for famille, doc in res.items():
        cle = {"dialogues": "dialogues", "grammaire": "points", "ecrit": "taches"}[famille]
        for el in doc.get(cle, []):
            for chemin, u in T.unites(el):
                if chemin.startswith("chemin."):
                    continue
                nb += 1
                for l in T.AUTRES:
                    v = u.get(l)
                    if not v:
                        continue
                    if u["fr"].count("<b>") != v.count("<b>"):
                        E("%s/%s %s : %s : %d <b> contre %d en français" % (famille, el["id"], chemin, l, v.count("<b>"), u["fr"].count("<b>")))
                    if "{" in v or "}" in v:
                        E("%s/%s %s : %s : accolade restée (nom non remplacé ?)" % (famille, el["id"], chemin, l))
    return nb


def controle_gabarits_trad():
    """Chaque traduction garde les memes noms que le francais."""
    for famille in T.FAMILLES:
        for ident, _, d in T.sources(famille):
            fr = {c: u for c, u in T.unites(d)}
            for l in T.AUTRES:
                ch = T.chemin_traduction(l, famille, ident)
                if not os.path.exists(ch):
                    continue
                for c, e in T.lire(ch).get("cles", {}).items():
                    if c not in fr:
                        A("%s/%s : %s : clé orpheline « %s » (relancer extraire)" % (famille, ident, l, c))
                        continue
                    if e.get("fr") != fr[c]["fr"] or e.get("perime"):
                        continue  # périmée : signalée par la construction, jugée une fois refaite
                    if e.get(l) and gabarits(e[l]) != gabarits(fr[c]["fr"]):
                        E("%s/%s %s : %s : noms %s, en français %s" % (famille, ident, c, l, gabarits(e[l]), gabarits(fr[c]["fr"])))
                    if l == "tr" and e.get(l) and re.search(r"\}['’]", e[l]):
                        E("%s/%s %s : tr : suffixe collé après un nom (}') : prendre la forme fléchie de noms.json" % (famille, ident, c))
                    if e.get(l):
                        m = []
                        T.remplacer(e[l], l, table, m)
                        for x in m:
                            E("%s/%s %s : %s" % (famille, ident, c, x))


# ------------------------------------------------------------------ le contrat (pflege/FORMAT-DONNEES.md, § 2 à 4)

QUI_CONTRAT = {"elif", "jonas", "hoffmann", "sommer", "brandt", "lehmann", "lehmann_tochter", "schulze", "weber",
               "kowalski", "amira", "arun", "yusuf", "olena", "kraemer",
               "aksoy", "richter", "schulze_tochter"}   # les trois derniers : roles de l'examen repris par d19, d24, d26 (a ajouter au contrat, demande)


def controle_contrat(export):
    """Ce que l'app lira : ids « soins_ », traductions à 9 clés (en mode strict), « lecture » à côté d'un chiffre,
    les champs obligatoires de chaque famille."""
    def langues(obj, ou):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ("trad", "titre", "but", "intro", "regle", "resume", "piege", "note", "consigne", "corrige",
                         "corrige_b1", "rubrique", "texte", "question", "conseil", "seuils") and isinstance(v, dict) \
                        and all(len(x) == 2 for x in v):
                    manque = [l for l in T.LANGUES if not v.get(l)]
                    if manque and not PARTIEL:
                        E("%s.%s : traduction sans %s" % (ou, k, ",".join(manque)))
                else:
                    langues(v, ou + "." + k)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                langues(v, "%s.%d" % (ou, i))

    def parle(x, ou, cle="de"):
        if isinstance(x, dict) and CHIFFRE.search(x.get(cle, "")) and not x.get("lecture"):
            E("%s : chiffre sans « lecture » : %s" % (ou, x[cle]))

    for d in export["dialogues"]["dialogues"]:
        ou = d.get("id", "?")
        if not re.fullmatch(r"soins_dlg_\d\d_[a-z_]+", ou):
            E("dialogue : id hors contrat %r" % ou)
        for k in ("numero", "niveau", "titre_de", "titre", "lieu", "scene", "personnages", "apprenant", "but",
                  "repliques", "redemittel", "questions", "grammaire", "prepare", "relire"):
            if k not in d:
                E("%s : clé « %s » absente" % (ou, k))
        for i, r in enumerate(d["repliques"]):
            if r["qui"] not in QUI_CONTRAT:
                E("%s repliques.%d : qui %r hors contrat" % (ou, i, r["qui"]))
            parle(r, "%s repliques.%d" % (ou, i))
        if not 12 <= len(d["repliques"]) <= 30:
            A("%s : %d répliques sur le chemin modèle (le contrat dit 12 à 20)" % (ou, len(d["repliques"])))
        for i, r in enumerate(d["redemittel"]):
            parle(r, "%s redemittel.%d" % (ou, i))
        for g in d["grammaire"]:
            if not g.startswith("soins_gr_"):
                E("%s : grammaire %r" % (ou, g))
        langues(d, ou)
    for p in export["grammaire"]["points"]:
        ou = p.get("id", "?")
        if not re.fullmatch(r"soins_gr_\d\d_[a-z_]+", ou):
            E("grammaire : id hors contrat %r" % ou)
        for i, q in enumerate(p["serie"]):
            if q["type"] == "choix" and not 0 <= q.get("bon", -1) < len(q.get("choix", [])):
                E("%s serie.%d : « bon » hors des choix" % (ou, i))
            parle(q, "%s serie.%d" % (ou, i), "phrase")
        for i, e in enumerate(p["exemples"]):
            parle(e, "%s exemples.%d" % (ou, i))
        langues(p, ou)
    for s in export["ecrit"]["sujets"]:
        ou = s.get("id", "?")
        if not re.fullmatch(r"soins_ecrit_(aufnahme|biografie|pflegebericht|sturz|nachricht)_\d\d", ou):
            E("écrit : id hors contrat %r" % ou)
        for k in ("type", "niveau", "consigne", "fiche", "briques", "corrige_de", "points_cles", "relire"):
            if k not in s:
                E("%s : clé « %s » absente" % (ou, k))
        langues(s, ou)
    langues(export["ecrit"]["grilles"], "grilles")


# ------------------------------------------------------------------ main

def main():
    dialogues = T.sources("dialogues")
    grammaire = T.sources("grammaire")
    ecrit = T.sources("ecrit")
    ids_g = {d.get("id") for _, _, d in grammaire}
    ids_d = {d.get("id", "")[:3] for _, _, d in dialogues} | {d.get("id") for _, _, d in dialogues}
    for ident, _, d in dialogues:
        controle_dialogue(ident, d, ids_g)
        controle_nombres("dialogues", ident, d)
        controle_gabarits("dialogues", ident, d)
    for ident, _, d in grammaire:
        controle_grammaire(ident, d, ids_d)
        controle_nombres("grammaire", ident, d)
        controle_gabarits("grammaire", ident, d)
    for ident, _, d in ecrit:
        controle_ecrit(ident, d)
        controle_gabarits("ecrit", ident, d)
    numeros = [d.get("numero") for _, _, d in dialogues]
    if len(set(numeros)) != len(numeros):
        E("dialogues : numéros en double")
    controle_gabarits_trad()

    res, manques = T.construire_tout(ecrire_fichiers=False)
    nb = controle_langues(res)
    if PARTIEL:
        compte = {}
        for m in manques:
            compte[m.split(" : ")[0]] = compte.get(m.split(" : ")[0], 0) + 1
        for l, n in sorted(compte.items()):
            A("%s : %d textes ou noms à traduire" % (l, n))
    else:
        for m in manques:
            E(m)
    # Le derive est-il a jour, et au format du contrat (pflege/FORMAT-DONNEES.md) ?
    export = T.exporter(res)
    for famille, doc in export.items():
        ch = os.path.join(T.DATOS, famille + ".json")
        if not os.path.exists(ch):
            E("pflege/datos/%s.json absent : python pflege/outils/textes.py construire" % famille)
        elif T.lire(ch) != json.loads(json.dumps(doc, ensure_ascii=False)):
            E("pflege/datos/%s.json en retard sur les sources : python pflege/outils/textes.py construire" % famille)
    controle_contrat(export)

    if "--relire" in ARGS:
        print("À relire par l'infirmière :")
        for famille in T.FAMILLES:
            for ident, _, d in T.sources(famille):
                if d.get("relire_notes"):
                    print("  %s/%s (général) : %s" % (famille, ident, d["relire_notes"]["fr"]))
                for chemin, u in T.unites(d):
                    if u.get("relire"):
                        print("  %s/%s %s : %s\n      « %s »" % (famille, ident, chemin, u.get("relire_note", ""), u.get("t", u["fr"])))
    if "--chars" in ARGS:
        chars()
    nrel = sum(1 for f in T.FAMILLES for _, _, d in T.sources(f) for _, u in T.unites(d) if u.get("relire"))
    print("Textes Soins : %d dialogues, %d points de grammaire, %d fichiers d'écrit ; %d unités à traduire ; %d à relire par l'infirmière."
          % (len(dialogues), len(grammaire), len(ecrit), nb, nrel))
    for a in avis[:40]:
        print("  avis : " + a)
    if len(avis) > 40:
        print("  … et %d avis de plus" % (len(avis) - 40))
    for e in erreurs:
        print("  ERREUR : " + e)
    print("%d erreur(s), %d avis." % (len(erreurs), len(avis)))
    sys.exit(1 if erreurs else 0)


def chars():
    """Les caracteres allemands a dire (ElevenLabs facture au caractere) : dialogues (repliques, choix, Redemittel,
    questions d'ecoute), grammaire (exemples et phrases completes des series). Chaque texte une fois."""
    res, _ = T.construire_tout(ecrire_fichiers=False)
    vus = {}
    for el in res["dialogues"]["dialogues"]:
        for chemin, u in T.unites(el):
            if chemin.startswith("chemin.") or "t" not in u:
                continue
            if chemin.endswith("aide") or chemin in ("titre", "intro", "but"):
                continue
            s = u.get("dit", u["t"])
            vus[s] = ("dialogues", el["id"])
    for el in res["grammaire"]["points"]:
        for chemin, u in T.unites(el):
            if "t" in u and (chemin.startswith("exemples") or chemin.endswith("phrase") or chemin.startswith("tableau")):
                vus[u.get("dit", u["t"])] = ("grammaire", el["id"])
    par = {}
    for s, (f, i) in vus.items():
        par[f] = par.get(f, 0) + len(s)
    total = sum(par.values())
    print("Caractères à dire (textes distincts) : %s ; total %d." % (", ".join("%s %d" % kv for kv in par.items()), total))


if __name__ == "__main__":
    main()
