# -*- coding: utf-8 -*-
"""Construit les donnees anglaises de l'app : anglais/datos (americain) et
anglais/datos-gb (britannique), a partir des listes de ce dossier.

    python anglais/outils/construire.py

LES FICHIERS PRODUITS SONT DERIVES : on corrige noms_a1.py, mots_a1.py,
phrases_a1.py ou variante.py, puis on relance. Le rapport (rapport.txt) dit
d'ou vient chaque phrase d'exemple et ce qui reste a regarder.

D'ou viennent les phrases d'exemple des mots. Nos corpus allemand et espagnol
donnent, pour chaque mot, une phrase traduite en anglais ET en francais
(exemple_en, exemple_fr) : 11 500 paires, alignees puisque traductions d'une
meme phrase. On prend pour chaque mot anglais la paire qui le contient, de
preference celle ecrite pour ce mot-la (meme tete anglaise), a un niveau bas,
courte, et pas deja prise par un autre mot. Les phrases ecrites a la main
(drapeau ex=) passent avant.

Les deux cours ont les MEMES mots dans le MEME ordre : la progression d'un
eleve (theme + rang) le suit quand il change de variante.
"""
import json, os, random, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import noms_a1, mots_a1, phrases_a1, variante, exemples_imposes, grammaire_a1, parcours_debutant

NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
RAPPORT = []


def charger(chemin):
    with open(os.path.join(RACINE, chemin), encoding="utf-8") as f:
        return json.load(f)


def ecrire(chemin, donnees):
    p = os.path.join(RACINE, chemin)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=1)
        f.write("\n")


def lignes(bloc):
    for l in bloc.strip().splitlines():
        l = l.strip()
        if l and not l.startswith("#"):
            yield [c.strip() for c in l.split("|")]


def drapeaux(cols):
    d = {}
    for c in cols:
        if "=" in c:
            k, v = c.split("=", 1)
            d[k.strip()] = v.strip()
        elif c:
            d[c] = True
    return d


# ---------------------------------------------------------------- l'orthographe
def remplacer_mots(texte, paires, conserver_casse=True):
    """Remplace des mots entiers (ou groupes de mots), casse respectee."""
    for a, b in paires:
        motif = re.compile(r"(?<![\w'])" + re.escape(a) + r"(?![\w'])", re.I)

        def rep(m, b=b):
            s = m.group(0)
            if s.isupper() and len(s) > 1:
                return b.upper()
            if s[0].isupper():
                return b[0].upper() + b[1:]
            return b
        texte = motif.sub(rep, texte)
    return texte


VOYELLE_MUETTE = ("hour", "honest", "honor", "honour", "heir")
CONSONNE_SONORE = ("uni", "use", "usu", "euro", "one", "once", "uk", "us ")


def article_indefini(mot):
    m = mot.lower()
    if m.startswith(VOYELLE_MUETTE):
        return "an"
    if m.startswith(CONSONNE_SONORE):
        return "a"
    return "an" if m[:1] in "aeiou" else "a"


def corriger_a_an(texte):
    def rep(m):
        art, mot = m.group(1), m.group(2)
        bon = article_indefini(mot)
        if art[0].isupper():
            bon = bon.capitalize()
        return bon + " " + mot
    return re.sub(r"\b([Aa]n?) ([A-Za-z][\w'-]*)", rep, texte)


def vers_gb(texte):
    """Une phrase americaine -> la phrase britannique."""
    if not texte:
        return texte
    # Le vocabulaire AVANT l'orthographe : sinon « movie theater » devient
    # « movie theatre », que la table du vocabulaire ne reconnait plus.
    t = remplacer_mots(texte, variante.VOCABULAIRE_PHRASES)
    t = remplacer_mots(t, variante.ORTHOGRAPHE)
    t = re.sub(r"\b" + variante.DETERMINANTS_STORE + r" store(s?)\b",
               lambda m: m.group(1) + " shop" + m.group(2), t, flags=re.I)
    return corriger_a_an(t)


GB_VERS_US = [(b, a) for a, b in variante.ORTHOGRAPHE]


def vers_us(texte):
    return remplacer_mots(texte, GB_VERS_US)


# ---------------------------------------------------------------- les formes
def pluriel(mot):
    if " " in mot:
        tete, dernier = mot.rsplit(" ", 1)
        return tete + " " + pluriel(dernier)
    m = mot
    if re.search(r"[^aeiou]y$", m):
        return m[:-1] + "ies"
    if re.search(r"(s|sh|ch|x|z)$", m):
        return m + "es"
    if re.search(r"[^aeiou]o$", m) and m not in ("photo", "piano", "radio", "video", "zoo", "kilo"):
        return m + "es"
    return m + "s"


def est_irr(base):
    return base in mots_a1.IRREGULIERS


def ing(base, gb=False):
    if base == "be":
        return "being"
    if base.endswith("ie"):
        return base[:-2] + "ying"
    if base in mots_a1.DOUBLENT or (gb and base in mots_a1.DOUBLENT_GB):
        return base + base[-1] + "ing"
    if base.endswith("e") and not base.endswith(("ee", "ye", "oe")):
        return base[:-1] + "ing"
    return base + "ing"


def passe_regulier(base, gb=False):
    if base.endswith("e"):
        return base + "d"
    if re.search(r"[^aeiou]y$", base):
        return base[:-1] + "ied"
    if base in mots_a1.DOUBLENT or (gb and base in mots_a1.DOUBLENT_GB):
        return base + base[-1] + "ed"
    return base + "ed"


def troisieme(base):
    if base == "be":
        return "is"
    if base == "have":
        return "has"
    if re.search(r"[^aeiou]y$", base):
        return base[:-1] + "ies"
    if re.search(r"(s|sh|ch|x|z|o)$", base):
        return base + "es"
    return base + "s"


def formes_verbe(verbe, gb=False):
    """{troisieme, preterit, participe, ing}, et la particule recollee pour
    get up, put on, look for..."""
    base, _, particule = verbe.partition(" ")
    suite = (" " + particule) if particule else ""
    if est_irr(base):
        irr = mots_a1.IRREGULIERS[base]
        pret, part = (irr[2] if (gb and len(irr) > 2) else irr[:2])
    else:
        pret = part = passe_regulier(base, gb)
    return {
        "troisieme": troisieme(base) + suite,
        "preterit": pret + suite if "/" not in pret else pret,
        "participe": part + suite if "/" not in part else part,
        "ing": ing(base, gb) + suite,
    }


def praesens(verbe):
    base, _, particule = verbe.partition(" ")
    suite = (" " + particule) if particule else ""
    if base == "be":
        f = ["am", "are", "is", "are", "are", "are"]
    else:
        f = [base, base, troisieme(base), base, base, base]
    return dict(zip(["ich", "du", "er_sie_es", "wir", "ihr", "sie_Sie"], [x + suite for x in f]))


def syllabes(mot):
    s = re.sub(r"e$", "", mot)
    return max(1, len(re.findall(r"[aeiouy]+", s)))


def comparatif(adj):
    if adj in mots_a1.COMPARATIFS_IRREGULIERS:
        return mots_a1.COMPARATIFS_IRREGULIERS[adj]
    if adj in mots_a1.COURTS:
        return mots_a1.COURTS[adj]
    if syllabes(adj) == 1:
        if re.search(r"[^aeiou][aeiou][^aeiouwy]$", adj):
            return adj + adj[-1] + "er", "the " + adj + adj[-1] + "est"
        if adj.endswith("e"):
            return adj + "r", "the " + adj + "st"
        return adj + "er", "the " + adj + "est"
    if syllabes(adj) == 2 and adj.endswith("y"):
        return adj[:-1] + "ier", "the " + adj[:-1] + "iest"
    return "more " + adj, "the most " + adj


# ---------------------------------------------------------------- la banque
def banque_de_phrases():
    """Toutes les paires (anglais, francais) de nos corpus, avec la tete
    anglaise du mot pour lequel elles ont ete ecrites et son niveau."""
    paires = []

    def tete(en):
        en = re.sub(r"\(.*?\)", "", en or "")
        p = re.split(r"[,;/]", en)[0].strip()
        return re.sub(r"^(the|a|an|to)\s+", "", p, flags=re.I).strip().lower()

    def ajouter(e, niveau, classe):
        if not isinstance(e, dict):
            return
        en, fr = e.get("exemple_en"), e.get("exemple_fr")
        if en and fr:
            paires.append({"en": en.strip(), "fr": fr.strip(), "tete": tete(e.get("traduction_en")),
                           "niveau": niveau, "classe": classe})

    for f in ("themes.json", "espanol/datos/temas.json"):
        for t in charger(f)["themes"]:
            for m in t.get("mots", []):
                ajouter(m, (t.get("niveau") or "C1").upper(), "nom")
    classes = {"verbe": "verbe", "verbos": "verbe", "adjectif": "adj", "adjetivos": "adj",
               "adverbe": "adv", "adverbios": "adv", "redewendung": "expr", "expresiones": "expr"}
    for f in ("verbe.json", "adjectif.json", "adverbe.json", "redewendung.json",
              "espanol/datos/verbos.json", "espanol/datos/adjetivos.json",
              "espanol/datos/adverbios.json", "espanol/datos/expresiones.json"):
        d = charger(f)
        classe = classes[os.path.basename(f)[:-5]]
        for n, liste in d.items():
            if isinstance(liste, list):
                for e in liste:
                    ajouter(e, n.upper() if n.upper() in NIVEAUX else "C1", classe)
    # Les phrases du cours americain : orthographe americaine, et aucune
    # phrase qui trahit l'anglais britannique (flat, lift, holiday...).
    marques = re.compile(r"(?<![\w'])(" + "|".join(re.escape(m) for m in variante.MARQUES_BRITANNIQUES)
                         + r")(?![\w'])", re.I)
    propres, vus = [], set()
    for p in paires:
        p["en"] = vers_us(p["en"])
        if marques.search(p["en"]) or p["en"] in vus:
            continue
        # Les phrases trop liees a l'Europe : euros, kilometres... on les
        # garde, mais en dernier recours.
        p["europe"] = bool(re.search(r"\b(euros?|Madrid|Berlin|Spain|Spanish|German|Germany|Barcelona|Munich|Hamburg|Seville|Mexico)\b", p["en"]))
        vus.add(p["en"])
        propres.append(p)
    return propres


class Choisisseur:
    def __init__(self, banque):
        self.banque = banque
        self.prises = set()

    def choisir(self, mot, formes, classe, tetes=None):
        tetes = {t.lower() for t in (tetes or [mot])}
        motifs = [re.compile(r"(?<![\w'-])" + re.escape(f) + r"(?![\w'-])", re.I)
                  for f in sorted(set(formes), key=len, reverse=True) if f]
        meilleur, score_max = None, None
        for p in self.banque:
            if p["en"] in self.prises:
                continue
            if not any(m.search(p["en"]) for m in motifs):
                continue
            n_mots = len(p["en"].split())
            if n_mots < 3:
                continue
            # La phrase ecrite pour CE mot, dans la MEME classe : « to fly »
            # (voler), pas « the fly » (la mouche).
            score = 0
            if p["tete"] in tetes and p["classe"] == classe:
                score += 20
            elif p["tete"] in tetes:
                score += 4
            if p["classe"] == classe:
                score += 3
            score += {"A1": 6, "A2": 4, "B1": 2}.get(p["niveau"], 0)
            score -= abs(n_mots - 7) * 0.6
            if p["europe"]:
                score -= 8
            if "?" in p["en"] and "?" not in p["fr"]:
                score -= 5
            if score_max is None or score > score_max:
                meilleur, score_max = p, score
        if meilleur:
            self.prises.add(meilleur["en"])
            origine = ("MEME MOT" if meilleur["classe"] == classe else "MEME MOT, AUTRE CLASSE") if meilleur["tete"] in tetes else "autre mot (" + meilleur["tete"] + ")"
            RAPPORT.append("  %-22s %-28s %s" % (mot, origine, meilleur["en"]))
            return meilleur["en"], meilleur["fr"]
        RAPPORT.append("  %-22s AUCUNE PHRASE" % mot)
        return "", ""


def exemple_impose(d, classe=None, mot=None):
    """(anglais, francais, anglais britannique ou None), ou None."""
    if "ex" in d:
        en, _, fr = d["ex"].partition("#")
        return en.strip(), fr.strip(), None
    x = exemples_imposes.IMPOSES.get((classe, mot))
    if x:
        RAPPORT.append("  %-22s %-28s %s" % (mot, "IMPOSEE", x[0]))
        return x[0], x[1], (x[2] if len(x) > 2 else None)
    return None


def avec_gb(ex):
    """(en, fr) de la banque -> (en, fr, None) ; la phrase britannique est
    alors calculee par vers_gb."""
    return ex if len(ex) == 3 else (ex[0], ex[1], None)


def phrase_gb(ex):
    return ex[2] if ex[2] else vers_gb(ex[0])


# ---------------------------------------------------------------- construction
def construire():
    banque = banque_de_phrases()
    ch = Choisisseur(banque)
    print("Banque : %d paires anglais-francais." % len(banque))

    # Les icones des themes, reprises des themes espagnols et allemands.
    icones = {}
    for f in ("espanol/datos/temas.json", "themes.json"):
        for t in charger(f)["themes"]:
            icones.setdefault(t["id"], t.get("svg", ""))

    us, gb = {}, {}

    # --- Les noms
    RAPPORT.append("== NOMS")
    th_us, th_gb = [], []
    for tid, nom, source in noms_a1.THEMES:
        mots_us, mots_gb = [], []
        for cols in lignes(noms_a1.NOMS[tid]):
            mot, fr, d = cols[0], cols[1], drapeaux(cols[2:])
            sans_pluriel = d.get("u") or d.get("plt")
            pl = "—" if sans_pluriel else d.get("pl", pluriel(mot))
            formes = [mot] + ([] if sans_pluriel else [pl])
            ex = avec_gb(exemple_impose(d, "nom", mot) or ch.choisir(mot, formes, "nom"))
            e = {"mot": mot, "genre": "", "pluriel": pl, "traduction": fr,
                 "exemple": ex[0], "exemple_fr": ex[1]}
            g = dict(e, exemple=phrase_gb(ex))
            if "gb" in d:
                mg = d["gb"]
                g["mot"] = mg
                g["pluriel"] = "—" if sans_pluriel else (d.get("plgb") or pluriel(mg))
                e["registre"], e["vergleich"] = "variante_gb", mg
                g["registre"], g["vergleich"] = "variante_us", mot
            else:
                g["mot"] = vers_gb(mot)
            mots_us.append(e)
            mots_gb.append(g)
        base = {"id": tid, "niveau": "A1", "svg": icones.get(source, "")}
        th_us.append(dict(base, nom_theme=nom, mots=mots_us))
        th_gb.append(dict(base, nom_theme=vers_gb(nom), mots=mots_gb))
    us["themes.json"] = {"themes": th_us}
    gb["themes.json"] = {"themes": th_gb}

    # --- Les verbes
    RAPPORT.append("== VERBES")
    v_us, v_gb = [], []
    for cols in lignes(mots_a1.VERBES):
        verbe, fr, d = cols[0], cols[1], drapeaux(cols[2:])
        f = formes_verbe(verbe)
        toutes = [verbe, f["troisieme"], f["ing"]] + f["preterit"].split("/") + f["participe"].split("/")
        if verbe == "be":
            toutes += ["am", "are", "is"]
        ex = avec_gb(exemple_impose(d, "verbe", verbe) or ch.choisir(verbe, [x.strip() for x in toutes], "verbe"))
        e = {"mot": verbe, "infinitif": verbe, "traduction": fr,
             "exemple": ex[0], "exemple_fr": ex[1],
             "praesens": praesens(verbe), "formes": f,
             "irregulier": est_irr(verbe.partition(" ")[0])}
        v_us.append(e)
        v_gb.append(dict(e, exemple=phrase_gb(ex), formes=formes_verbe(verbe, gb=True)))
    us["verbes.json"] = {"A1": v_us}
    gb["verbes.json"] = {"A1": v_gb}

    # --- Les adjectifs
    RAPPORT.append("== ADJECTIFS")
    a_us, a_gb = [], []
    for cols in lignes(mots_a1.ADJECTIFS):
        adj, fr, d = cols[0], cols[1], drapeaux(cols[2:])
        ex = avec_gb(exemple_impose(d, "adj", adj) or ch.choisir(adj, [adj], "adj"))
        e = {"mot": adj, "traduction": fr, "exemple": ex[0], "exemple_fr": ex[1]}
        if adj not in mots_a1.SANS_COMPARATIF:
            c, s = comparatif(adj)
            e["formes"] = {"comparatif": c, "superlatif": s}
        g = dict(e, exemple=phrase_gb(ex))
        if "gb" in d:
            g["mot"] = d["gb"]
            e["registre"], e["vergleich"] = "variante_gb", d["gb"]
            g["registre"], g["vergleich"] = "variante_us", adj
            if "formes" in e:
                c, s = comparatif(d["gb"])
                g["formes"] = {"comparatif": c, "superlatif": s}
        a_us.append(e)
        a_gb.append(g)
    us["adjectifs.json"] = {"A1": a_us}
    gb["adjectifs.json"] = {"A1": a_gb}

    # --- Les adverbes
    RAPPORT.append("== ADVERBES")
    ad_us, ad_gb = [], []
    for cols in lignes(mots_a1.ADVERBES):
        adv, fr, cat = cols[0], cols[1], cols[2]
        d = drapeaux(cols[3:])
        ex = avec_gb(exemple_impose(d, "adv", adv) or ch.choisir(adv, [adv], "adv"))
        e = {"mot": adv, "traduction": fr, "kategorie": cat, "exemple": ex[0], "exemple_fr": ex[1]}
        ad_us.append(e)
        ad_gb.append(dict(e, exemple=phrase_gb(ex)))
    us["adverbes.json"] = {"A1": ad_us}
    gb["adverbes.json"] = {"A1": ad_gb}

    # --- Les expressions et les mots-outils : phrases ecrites a la main.
    ex_us, ex_gb = [], []
    for cols in lignes(phrases_a1.EXPRESSIONS):
        mot, fr, cat, en, efr = cols[:5]
        e = {"mot": mot, "traduction": fr, "kategorie": cat, "exemple": en, "exemple_fr": efr}
        ex_us.append(e)
        ex_gb.append(dict(e, mot=vers_gb(mot), exemple=vers_gb(en)))
    us["expressions.json"] = {"A1": ex_us}
    gb["expressions.json"] = {"A1": ex_gb}

    f_us, f_gb = {}, {}
    for cle, bloc in phrases_a1.FONCTIONNELS.items():
        f_us[cle], f_gb[cle] = [], []
        for cols in lignes(bloc):
            mot, fr, cat, en, efr = cols[:5]
            e = {"mot": mot, "traduction": fr, "kategorie": cat, "exemple": en,
                 "exemple_fr": efr, "niveau": "A1"}
            f_us[cle].append(e)
            f_gb[cle].append(dict(e, exemple=vers_gb(en)))
    us["fonctionnels.json"] = f_us
    gb["fonctionnels.json"] = f_gb

    # La grammaire et ses series : communes aux deux anglais (le moteur va
    # chercher dans datos/ ce que datos-gb/ n'a pas). Le format est celui des
    # fiches espagnoles et japonaises (abrirGramatica, startExerciseSet).
    fiches, jeux = [], {}
    for f in grammaire_a1.FICHES:
        fiche = {k: f[k] for k in ("id", "titre", "resume", "regle", "tableau", "exemples", "attention")}
        # La serie de la fiche : index.html cree la fonction « exercice » a
        # partir de « serie » (brancherSeriesAnglaises), sans liste en dur.
        fiche["exercice"] = "exercicesFicheEn_" + f["id"].replace("-", "_")
        fiche["serie"] = f["serie"]
        fiche["statut"] = "brouillon"
        fiches.append(fiche)
        qs = []
        for cols in lignes(f["questions"]):
            question, bonne, fausses, trad, expl = cols[:5]
            options = [bonne] + [x.strip() for x in fausses.split("/")]
            # La bonne reponse n'est pas toujours la premiere : un ordre
            # melange, mais stable d'une construction a l'autre.
            random.Random(question).shuffle(options)
            qs.append({"topic": f["id"], "question": question, "question_en": question,
                       "translation": trad, "translation_en": trad,
                       "answers": [bonne], "correct": bonne, "correctEn": bonne,
                       "explanation": expl, "explanation_en": expl,
                       "options": options, "optionsEn": options})
        jeux[f["serie"]] = qs
    textes = dict(grammaire_a1.TEXTES)
    for f in grammaire_a1.FICHES:
        textes["kicker_" + f["serie"]] = f["kicker"]
    textes.update(parcours_debutant.prononciation_a1.TITRES)
    us["grammaire.json"] = {"textes": {"fr": textes}, "fiches": fiches}
    us["exercices.json"] = {"jeux": jeux}
    print("Grammaire : %d fiches, %d questions." % (len(fiches), sum(len(q) for q in jeux.values())))

    # Le parcours debutant : reperes, prononciation, feuilles, Premiers pas.
    parcours_debutant.construire(us, gb, vers_gb)

    # Les niveaux A2-C1 (niveaux.py), apres l'A1, qu'ils ne touchent pas.
    import niveaux
    niveaux.construire(us, gb, ch, vers_gb)

    # Pas de cle « _lisez_moi » dans les fichiers : le chargeur des verbes
    # prend chaque cle pour un niveau (il retombait sur sa liste de secours
    # allemande). La notice vit dans anglais/datos/LISEZ-MOI.md.
    for dossier, jeu in (("anglais/datos", us), ("anglais/datos-gb", gb)):
        for nom, donnees in jeu.items():
            ecrire(dossier + "/" + nom, donnees)

    n = {k: (sum(len(t["mots"]) for t in v["themes"]) if k == "themes.json"
             else sum(len(x) for x in v.values())) for k, v in us.items()}
    print("Construit :", n)
    sans = [l for l in RAPPORT if "AUCUNE PHRASE" in l]
    autre = [l for l in RAPPORT if "autre mot" in l]
    with open(os.path.join(ICI, "rapport.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("Phrases d'exemple : %d sans phrase, %d prises a un autre mot.\n\n" % (len(sans), len(autre)))
        f.write("\n".join(RAPPORT) + "\n")
    print("Sans phrase : %d ; phrase d'un autre mot : %d (voir anglais/outils/rapport.txt)" % (len(sans), len(autre)))


if __name__ == "__main__":
    construire()
