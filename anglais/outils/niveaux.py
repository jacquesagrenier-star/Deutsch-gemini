# -*- coding: utf-8 -*-
"""Les niveaux A2 a C1 de l'anglais, ajoutes aux donnees de l'A1.

Appele par construire.py, APRES l'A1 (une ligne) : l'A1 ne bouge pas.

    niveaux.construire(us, gb, ch, vers_gb)

Les sources, par niveau (on corrige la, jamais dans anglais/datos) :
  noms_<niv>.py        les noms par theme (format de noms_a1.py)
  mots_<niv>.py        verbes, adjectifs, adverbes, expressions
  fonctionnels_niveaux.py   les mots-outils de niveau (connecteurs, quantifieurs...)
  grammaire_<niv>.py   les fiches de grammaire et leurs series
  conjugaison_niveaux.py    les feuilles de conjugaison
  irreguliers.py, variante_niveaux.py   les formes et le britannique

Un mot deja present a un niveau plus bas (A1 compris) est saute et signale :
un mot n'a qu'une carte.
"""
import importlib, os, random, re

import construire as C
import mots_a1
import irreguliers
import variante
import variante_niveaux as VN

ICI = os.path.dirname(os.path.abspath(__file__))
# Les niveaux branches : un niveau entre ici quand ses listes ont ete relues.
NIVEAUX = ["A2"]

ORTHO_US = [(b, a) for a, b in VN.ORTHOGRAPHE if a not in VN.PAS_DANS_LES_PHRASES]
ORTHO_GB = [(a, b) for a, b in VN.ORTHOGRAPHE if a not in VN.PAS_DANS_LES_PHRASES]

# Ne se comparent pas : on ne calcule ni comparatif ni superlatif.
NON_GRADUES = set("""
dead pregnant unique divorced married born digital wireless online automatic theoretical renewable eco-friendly
religious male female marine maximum minimum double central classical current unemployed included furnished
forbidden engaged delayed known numerous medium daily weekly monthly annual wooden plastic metal electric
electrical medical legal illegal political economic social national international public private nuclear
financial physical chemical biological musical technical vegetarian vegan absolute total complete entire
whole final initial previous former main chief sole mere ideal perfect empty full right wrong square round
oval rectangular triangular dual mobile local regional federal municipal urban rural ethnic racial
""".split())


def module(nom):
    try:
        return importlib.import_module(nom)
    except ImportError:
        return None


def en_us(t):
    return C.remplacer_mots(t, ORTHO_US) if t else t


def en_gb(t, vers_gb):
    return C.remplacer_mots(vers_gb(t), ORTHO_GB) if t else t


def etendre_formes():
    for base, f in irreguliers.IRREGULIERS.items():
        mots_a1.IRREGULIERS.setdefault(base, f)
    mots_a1.DOUBLENT.update(irreguliers.DOUBLENT)
    mots_a1.DOUBLENT_GB.update(irreguliers.DOUBLENT_GB)


def formes_verbe(verbe, d, gb=False):
    if d.get("reg"):
        base, _, particule = verbe.partition(" ")
        suite = (" " + particule) if particule else ""
        p = C.passe_regulier(base, gb) + suite
        return {"troisieme": C.troisieme(base) + suite, "preterit": p, "participe": p,
                "ing": C.ing(base, gb) + suite}
    return C.formes_verbe(verbe, gb)


def icones():
    ic = {}
    for f in ("espanol/datos/temas.json", "themes.json"):
        for t in C.charger(f)["themes"]:
            ic.setdefault(t["id"], t.get("svg", ""))
    return ic


class Deja:
    """Les mots deja pris, par classe : un mot n'a qu'une carte."""
    def __init__(self, us):
        self.vus = {"nom": set(), "verbe": set(), "adj": set(), "adv": set(), "expr": set()}
        for t in us["themes.json"]["themes"]:
            for m in t["mots"]:
                self.vus["nom"].add(m["mot"].lower())
        for cl, f in (("verbe", "verbes.json"), ("adj", "adjectifs.json"), ("adv", "adverbes.json"),
                      ("expr", "expressions.json")):
            for liste in us[f].values():
                for m in liste:
                    self.vus[cl].add(m["mot"].lower().strip("!?."))

    def prendre(self, cl, mot, niv):
        cle = mot.lower().strip("!?.")
        if cle in self.vus[cl]:
            C.RAPPORT.append("  %-22s DEJA A UN NIVEAU PLUS BAS (%s, saute)" % (mot, niv))
            return False
        self.vus[cl].add(cle)
        return True


def en_amerique(en, fr):
    """Les villes et la monnaie europeennes d'une phrase de la banque -> l'Amerique,
    dans l'anglais ET le francais (les deux sont la traduction l'un de l'autre)."""
    for a, b in VN.LIEUX:
        en = C.remplacer_mots(en, [(a, b)])
        fr = C.remplacer_mots(fr, [(a, b)])
    return en, fr


def choisir(ch, d, classe, mot, formes):
    ex = C.exemple_impose(d, classe, mot)
    if ex:
        ex = (ex[0], ex[1], d.get("exgb") or ex[2])
    else:
        en, fr = en_amerique(*ch.choisir(mot, formes, classe))
        ex = (en, fr, None)
    return (en_us(ex[0]), ex[1], ex[2])


def phrase_gb(ex, vers_gb, paires=()):
    """La phrase britannique ; `paires` : le mot americain et son pluriel ->
    le mot britannique, pour que la carte de « roommate » dise « flatmate »
    dans sa phrase aussi."""
    if ex[2]:
        return ex[2]
    t = C.remplacer_mots(ex[0], [p for p in paires if p[0] and p[1] and p[0] != "—"])
    return C.corriger_a_an(en_gb(t, vers_gb))


# ---------------------------------------------------------------- vocabulaire
def noms(niv, src, us, gb, ch, vers_gb, deja, ic):
    C.RAPPORT.append("== NOMS " + niv)
    for tid, nom, source in src.THEMES:
        m_us, m_gb = [], []
        for cols in C.lignes(src.NOMS[tid]):
            mot, fr, d = cols[0], cols[1], C.drapeaux(cols[2:])
            if not deja.prendre("nom", mot, niv):
                continue
            sans_pluriel = d.get("u") or d.get("plt")
            pl = "—" if sans_pluriel else d.get("pl", C.pluriel(mot))
            ex = choisir(ch, d, "nom", mot, [mot] + ([] if sans_pluriel else [pl]))
            e = {"mot": mot, "genre": "", "pluriel": pl, "traduction": fr, "exemple": ex[0], "exemple_fr": ex[1]}
            g = dict(e, exemple=phrase_gb(ex, vers_gb))
            if "gb" in d:
                g["mot"] = d["gb"]
                g["pluriel"] = "—" if sans_pluriel else (d.get("plgb") or C.pluriel(d["gb"]))
                g["exemple"] = phrase_gb(ex, vers_gb, [(pl, g["pluriel"]), (mot, d["gb"])])
                e["registre"], e["vergleich"] = "variante_gb", d["gb"]
                g["registre"], g["vergleich"] = "variante_us", mot
            else:
                g["mot"] = en_gb(mot, vers_gb)
                if g["mot"] != mot and not sans_pluriel:
                    g["pluriel"] = C.pluriel(g["mot"]) if "pl" not in d else en_gb(pl, vers_gb)
            m_us.append(e)
            m_gb.append(g)
        if not m_us:
            continue
        base = {"id": tid, "niveau": niv, "svg": ic.get(source, "")}
        us["themes.json"]["themes"].append(dict(base, nom_theme=nom, mots=m_us))
        gb["themes.json"]["themes"].append(dict(base, nom_theme=en_gb(nom, vers_gb), mots=m_gb))


def verbes(niv, src, us, gb, ch, vers_gb, deja):
    C.RAPPORT.append("== VERBES " + niv)
    v_us, v_gb = [], []
    for cols in C.lignes(src.VERBES):
        verbe, fr, d = cols[0], cols[1], C.drapeaux(cols[2:])
        if not deja.prendre("verbe", verbe, niv):
            continue
        f = formes_verbe(verbe, d)
        toutes = [verbe, f["troisieme"], f["ing"]] + f["preterit"].split("/") + f["participe"].split("/")
        ex = choisir(ch, d, "verbe", verbe, [x.strip() for x in toutes])
        e = {"mot": verbe, "infinitif": verbe, "traduction": fr, "exemple": ex[0], "exemple_fr": ex[1],
             "praesens": C.praesens(verbe), "formes": f,
             "irregulier": (not d.get("reg")) and C.est_irr(verbe.partition(" ")[0])}
        v_us.append(e)
        v_gb.append(dict(e, mot=en_gb(verbe, vers_gb), infinitif=en_gb(verbe, vers_gb),
                         exemple=phrase_gb(ex, vers_gb), formes=formes_verbe(verbe, d, gb=True)))
    us["verbes.json"][niv] = v_us
    gb["verbes.json"][niv] = v_gb


def adjectifs(niv, src, us, gb, ch, vers_gb, deja):
    C.RAPPORT.append("== ADJECTIFS " + niv)
    a_us, a_gb = [], []
    for cols in C.lignes(src.ADJECTIFS):
        adj, fr, d = cols[0], cols[1], C.drapeaux(cols[2:])
        if not deja.prendre("adj", adj, niv):
            continue
        ex = choisir(ch, d, "adj", adj, [adj])
        e = {"mot": adj, "traduction": fr, "exemple": ex[0], "exemple_fr": ex[1]}
        gradue = not (d.get("nc") or adj[:1].isupper() or " " in adj or "-" in adj
                      or adj.lower() in NON_GRADUES or adj in mots_a1.SANS_COMPARATIF
                      or re.search(r"(ed|ing|ic|al|ous|ive|ary|ible|able|ese|ish|ian)$", adj) and C.syllabes(adj) > 2)
        if gradue or d.get("comp"):
            c, s = C.comparatif(adj)
            e["formes"] = {"comparatif": c, "superlatif": s}
        g = dict(e, mot=en_gb(adj, vers_gb), exemple=phrase_gb(ex, vers_gb))
        if "gb" in d:
            g["mot"] = d["gb"]
            g["exemple"] = phrase_gb(ex, vers_gb, [(adj, d["gb"])])
            e["registre"], e["vergleich"] = "variante_gb", d["gb"]
            g["registre"], g["vergleich"] = "variante_us", adj
        a_us.append(e)
        a_gb.append(g)
    us["adjectifs.json"][niv] = a_us
    gb["adjectifs.json"][niv] = a_gb


def adverbes(niv, src, us, gb, ch, vers_gb, deja):
    C.RAPPORT.append("== ADVERBES " + niv)
    ad_us, ad_gb = [], []
    for cols in C.lignes(src.ADVERBES):
        adv, fr, cat = cols[0], cols[1], cols[2]
        d = C.drapeaux(cols[3:])
        if not deja.prendre("adv", adv, niv):
            continue
        ex = choisir(ch, d, "adv", adv, [adv])
        e = {"mot": adv, "traduction": fr, "kategorie": cat, "exemple": ex[0], "exemple_fr": ex[1]}
        ad_us.append(e)
        ad_gb.append(dict(e, mot=en_gb(adv, vers_gb), exemple=phrase_gb(ex, vers_gb)))
    us["adverbes.json"][niv] = ad_us
    gb["adverbes.json"][niv] = ad_gb


def expressions(niv, src, us, gb, vers_gb, deja):
    ex_us, ex_gb = [], []
    for cols in C.lignes(src.EXPRESSIONS):
        mot, fr, cat, en, efr = cols[:5]
        if not mot.lower().startswith("to "):
            mot = mot[:1].upper() + mot[1:]
            fr = fr[:1].upper() + fr[1:]
        if not deja.prendre("expr", mot, niv):
            continue
        en = en_us(en)
        e = {"mot": mot, "traduction": fr, "kategorie": cat, "exemple": en, "exemple_fr": efr}
        ex_us.append(e)
        ex_gb.append(dict(e, mot=en_gb(mot, vers_gb), exemple=en_gb(en, vers_gb)))
    us["expressions.json"][niv] = ex_us
    gb["expressions.json"][niv] = ex_gb


def fonctionnels(us, gb, vers_gb):
    src = module("fonctionnels_niveaux")
    if not src:
        return 0
    n = 0
    for niv, blocs in src.FONCTIONNELS.items():
        for cle, bloc in blocs.items():
            for cols in C.lignes(bloc):
                mot, fr, cat, en, efr = cols[:5]
                e = {"mot": mot, "traduction": fr, "kategorie": cat, "exemple": en,
                     "exemple_fr": efr, "niveau": niv}
                us["fonctionnels.json"].setdefault(cle, []).append(e)
                gb["fonctionnels.json"].setdefault(cle, []).append(dict(e, exemple=en_gb(en, vers_gb)))
                n += 1
    return n


# ---------------------------------------------------------------- grammaire
def grammaire(niv, src, us):
    """Les fiches du niveau, au format de construire.py (A1), avec leur niveau."""
    fiches = us["grammaire.json"]["fiches"]
    jeux = us["exercices.json"]["jeux"]
    textes = us["grammaire.json"]["textes"]["fr"]
    nq = 0
    for f in src.FICHES:
        fiche = {k: f[k] for k in ("id", "titre", "resume", "regle", "tableau", "exemples", "attention")}
        fiche["exercice"] = "exercicesFicheEn_" + f["id"].replace("-", "_")
        fiche["serie"] = f["serie"]
        fiche["niveau"] = niv
        fiche["statut"] = "brouillon"
        assert f["serie"] not in jeux, "serie en double : " + f["serie"]
        fiches.append(fiche)
        qs = []
        for cols in C.lignes(f["questions"]):
            question, bonne, fausses, trad, expl = cols[:5]
            options = [bonne] + [x.strip() for x in fausses.split("/")]
            random.Random(question).shuffle(options)
            qs.append({"topic": f["id"], "question": question, "question_en": question,
                       "translation": trad, "translation_en": trad,
                       "answers": [bonne], "correct": bonne, "correctEn": bonne,
                       "explanation": expl, "explanation_en": expl,
                       "options": options, "optionsEn": options})
        jeux[f["serie"]] = qs
        textes["kicker_" + f["serie"]] = f["kicker"]
        nq += len(qs)
    return len(src.FICHES), nq


def conjugaison(us, gb, vers_gb):
    src = module("conjugaison_niveaux")
    if not src:
        return 0
    n = 0
    for jeu, est_gb in ((us, False), (gb, True)):
        conv = (lambda s: en_gb(s, vers_gb)) if est_gb else (lambda s: s)
        for niv, feuilles in src.FEUILLES.items():
            out = []
            for f in feuilles:
                out.append({"id": f["id"], "serie": f["serie"], "temps": None, "t": {"fr": f["t"]},
                            "l": [[conv(a), {"fr": b}] for a, b in f["l"]], "a": {"fr": f["a"]}})
            jeu["conjugaison.json"]["niveaux"][niv] = out
            if not est_gb:
                n += len(out)
    return n


# ---------------------------------------------------------------- tout
def construire(us, gb, ch, vers_gb):
    etendre_formes()
    deja = Deja(us)
    ic = icones()
    bilan = []
    for niv in NIVEAUX:
        n_src, m_src = module("noms_" + niv.lower()), module("mots_" + niv.lower())
        if n_src:
            noms(niv, n_src, us, gb, ch, vers_gb, deja, ic)
        if m_src:
            verbes(niv, m_src, us, gb, ch, vers_gb, deja)
            adjectifs(niv, m_src, us, gb, ch, vers_gb, deja)
            adverbes(niv, m_src, us, gb, ch, vers_gb, deja)
            expressions(niv, m_src, us, gb, vers_gb, deja)
        g_src = module("grammaire_" + niv.lower())
        nf = nq = 0
        if g_src:
            nf, nq = grammaire(niv, g_src, us)
        n_noms = sum(len(t["mots"]) for t in us["themes.json"]["themes"] if t["niveau"] == niv)
        bilan.append("%s : %d noms, %d verbes, %d adjectifs, %d adverbes, %d expressions, %d fiches (%d questions)" % (
            niv, n_noms, len(us["verbes.json"].get(niv, [])), len(us["adjectifs.json"].get(niv, [])),
            len(us["adverbes.json"].get(niv, [])), len(us["expressions.json"].get(niv, [])), nf, nq))
    nfo = fonctionnels(us, gb, vers_gb)
    nco = conjugaison(us, gb, vers_gb)
    for l in bilan:
        print("Niveaux -- " + l)
    print("Niveaux -- %d mots-outils, %d feuilles de conjugaison" % (nfo, nco))
