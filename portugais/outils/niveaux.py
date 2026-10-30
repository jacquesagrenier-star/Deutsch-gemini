# -*- coding: utf-8 -*-
"""Les niveaux A2 a C1 du portugais (du Portugal), ajoutes aux donnees de l'A1.

Appele par construire.py, APRES l'A1 et avant l'ecriture (une ligne) :

    import niveaux; niveaux.construire(jeu)

`jeu` est le dictionnaire {nom de fichier: donnees} que construire.py ecrit
dans portugais/datos. L'A1 n'y bouge pas : on ajoute des themes, des niveaux
aux listes, des fiches, des feuilles. Essai sans toucher au disque :

    python portugais/outils/niveaux.py            (bilan, avec un A1 vide ou celui de portugais/datos)
    python portugais/outils/niveaux.py --ecrire DOSSIER   (ecrit un jeu complet ailleurs, pour regarder)

Les sources, par niveau (on corrige la, jamais dans portugais/datos) :
  noms_<niv>.py            les noms par theme (format de noms_a1.py)
  mots_<niv>.py            verbes, adjectifs, adverbes, expressions (format de mots_a1.py)
  fonctionnels_niveaux.py  les mots-outils de niveau (connecteurs, relatifs...)
  grammaire_<niv>.py       les fiches de grammaire et leurs series
  temps_<niv>.py           l'ecran « S'entrainer par temps » : une serie par temps
  conjugaison_niveaux.py   les feuilles de conjugaison
  irreguliers.py           toutes les formes (mesoclise, conjuntivo futuro...)

Un mot deja present a un niveau plus bas (A1 compris) est saute et signale :
un mot n'a qu'une carte. Le mot bresilien (drapeau br=) va dans
variantes-br.json, comme pour l'A1.
"""
import importlib, io, json, os, random, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import irreguliers as I

NIVEAUX = ["A2", "B1", "B2", "C1"]
RAPPORT = []
CLES_PRESENT = ["ich", "du", "er_sie_es", "wir", "ihr", "sie_Sie"]


def module(nom):
    try:
        return importlib.import_module(nom)
    except ImportError:
        return None


def lignes(bloc):
    for l in (bloc or "").strip("\n").splitlines():
        if l.strip() and not l.strip().startswith("#"):
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


# ---------------------------------------------------------------- le pluriel
# La regle de construire.py (session socle), reprise ici pour que niveaux.py
# tourne seul ; les cas que la regle ne trouve pas sont ecrits (pl=) dans les listes.
PLUR_AES = set("pão cão alemão capitão capelão escrivão tabelião charlatão sacristão catalão".split())
PLUR_AOS = set("mão irmão cidadão cristão órgão órfão sótão bênção grão chão vão desvão cortesão pagão acórdão".split())


def pluriel_mot(m):
    if m.endswith("ão"):
        return m[:-2] + "ães" if m in PLUR_AES else (m + "s" if m in PLUR_AOS else m[:-2] + "ões")
    if re.search(r"[aeiouáéíóúâêô]$", m):
        return m + "s"
    if m.endswith("m"):
        return m[:-1] + "ns"
    if re.search(r"[rz]$", m):
        return m + "es"
    if m.endswith("s"):
        if m.endswith(("ês", "és")):
            return m[:-2] + "eses"
        if m.endswith(("ás", "ís", "ós", "ús")):
            return m + "es"
        return m
    if m.endswith("al"):
        return m[:-1] + "is"
    if m.endswith("el"):
        return m[:-2] + ("eis" if re.search(r"[áéíóúâêô]", m) else "éis")
    if m.endswith("ol"):
        return m[:-2] + "óis"
    if m.endswith("ul"):
        return m[:-1] + "is"
    if m.endswith("il"):
        return m[:-2] + ("eis" if re.search(r"[áéíóúâêô]", m) else "is")
    if m.endswith("x"):
        return m
    return m + "s"


def pluriel(mot):
    for sep in (" de ", " da ", " do ", " das ", " dos ", " em ", " a ", " à "):
        if sep in mot:
            tete, _, reste = mot.partition(" ")
            return pluriel_mot(tete) + " " + reste
    if " " in mot:
        return " ".join(pluriel_mot(x) for x in mot.split(" "))
    if "-" in mot:
        a, b = mot.split("-", 1)
        return pluriel_mot(a) + "-" + pluriel_mot(b)
    return pluriel_mot(mot)


# ---------------------------------------------------------------- les mots deja pris
class Deja:
    """Les mots deja pris, par classe : un mot n'a qu'une carte."""
    def __init__(self, jeu):
        self.vus = {"nom": set(), "verbe": set(), "adj": set(), "adv": set(), "expr": set()}
        for t in jeu.get("themes.json", {}).get("themes", []):
            for m in t["mots"]:
                self.vus["nom"].add(m["mot"].lower())
        for cl, f in (("verbe", "verbes.json"), ("adj", "adjectifs.json"), ("adv", "adverbes.json"),
                      ("expr", "expressions.json")):
            for liste in jeu.get(f, {}).values():
                if isinstance(liste, list):
                    for m in liste:
                        self.vus[cl].add(m["mot"].lower().strip("!?."))

    def prendre(self, cl, mot, niv):
        cle = mot.lower().strip("!?.")
        if cle in self.vus[cl]:
            RAPPORT.append("  %-26s DEJA A UN NIVEAU PLUS BAS (%s, saute)" % (mot, niv))
            return False
        self.vus[cl].add(cle)
        return True


def icones():
    ic = {}
    for f in ("espanol/datos/temas.json", "themes.json"):
        try:
            with io.open(os.path.join(RACINE, f), encoding="utf-8") as fh:
                for t in json.load(fh)["themes"]:
                    ic.setdefault(t["id"], t.get("svg", ""))
        except OSError:
            pass
    return ic


def sans_phrase(cl, mot, niv, ex, exfr):
    if ex and exfr:
        return False
    RAPPORT.append("  %-26s SANS PHRASE (%s %s, saute)" % (mot, cl, niv))
    return True


# ---------------------------------------------------------------- vocabulaire
def noms(niv, src, jeu, deja, ic, variantes):
    n = 0
    for tid, nom, source in src.THEMES:
        mots = []
        for cols in lignes(src.NOMS[tid]):
            tete, fr = cols[0], cols[1]
            ex, exfr = (cols[2], cols[3]) if len(cols) > 3 else ("", "")
            d = drapeaux(cols[4:])
            art, _, mot = tete.partition(" ") if tete.split(" ", 1)[0] in ("o", "a", "os", "as") else ("", "", tete)
            mot = mot.strip()
            if sans_phrase("nom", mot, niv, ex, exfr) or not deja.prendre("nom", mot, niv):
                continue
            sans = d.get("u") or art in ("os", "as")
            pl = "—" if sans else d.get("pl", pluriel(mot))
            e = {"mot": mot, "genre": art, "pluriel": pl, "traduction": fr, "exemple": ex, "exemple_fr": exfr}
            if "br" in d:
                variantes["noms"][mot] = d["br"]
            mots.append(e)
        if mots:
            jeu["themes.json"]["themes"].append({"id": tid, "niveau": niv, "svg": ic.get(source, ""),
                                                  "nom_theme": nom, "mots": mots})
            n += len(mots)
    return n


def entree_verbe(inf, fr, ex, exfr):
    c = I.conjuguer(inf)
    pron = inf.endswith("-se")
    im = c["imperativo"]
    return {"mot": inf, "infinitif": inf, "traduction": fr, "exemple": ex, "exemple_fr": exfr,
            "praesens": dict(zip(CLES_PRESENT, c["presente"])),
            "perfeito": c["perfeito"], "imperfeito": c["imperfeito"],
            "futuro": c["futuro"], "condicional": c["condicional"], "conjuntivo": c["conj_presente"],
            "imperativo": {"tu": im["tu"], "voce": im["voce"], "voces": im["voces"]},
            # Les temps de l'A2-C1 (au-dela de ceux de l'A1) :
            "conj_imperfeito": c["conj_imperfeito"], "conj_futuro": c["conj_futuro"],
            "mais_que_perfeito": c["mais_que_perfeito"], "perfeito_composto": c["perfeito_composto"],
            "participio": c["participio"], "gerundio": c["gerundio"],
            "irregulier": c["irregulier"], "pronominal": pron}


def formes_verbe(inf):
    c = I.conjuguer(inf)
    fs = {inf.replace("-se", "")}
    for v in c.values():
        if isinstance(v, list):
            for f in v:
                fs.update(x for x in re.split(r"[\s-]", f) if len(x) > 1)
        elif isinstance(v, dict):
            fs.update(x.split("-")[0] for x in v.values())
    p = c["participio"]
    if p.endswith("o"):
        fs.update([p[:-1] + "a", p + "s", p[:-1] + "as"])
    return fs - set("tinha tinhas tínhamos tínheis tinham tenho tens tem temos tendes têm que quando se me te nos vos".split())


def verbes(niv, src, jeu, deja, variantes):
    out = []
    for cols in lignes(src.VERBES):
        inf, fr = cols[0], cols[1]
        ex, exfr = (cols[2], cols[3]) if len(cols) > 3 else ("", "")
        d = drapeaux(cols[4:])
        if sans_phrase("verbe", inf, niv, ex, exfr) or not deja.prendre("verbe", inf, niv):
            continue
        if not any(re.search(r"(?<![\wÀ-ú])" + re.escape(f) + r"(?![\wÀ-ú])", ex, re.I) for f in formes_verbe(inf)):
            RAPPORT.append("  %-26s VERBE ABSENT DE SA PHRASE : %s" % (inf, ex))
        if "br" in d:
            variantes["verbes"][inf] = d["br"]
        out.append(entree_verbe(inf, fr, ex, exfr))
    jeu["verbes.json"][niv] = out
    return len(out)


COMPARATIFS = {"bom": "melhor", "mau": "pior", "grande": "maior", "pequeno": "mais pequeno"}
NON_GRADUES = set("""morto grávida único divorciado casado nascido digital online automático teórico
renovável masculino feminino marinho máximo mínimo duplo central clássico atual desempregado incluído
mobilado proibido noivo atrasado anual diário semanal mensal médico legal ilegal político económico
social nacional internacional público privado nuclear financeiro físico químico biológico musical técnico
vegetariano vegano absoluto total completo inteiro final inicial anterior antigo principal ideal perfeito
vazio cheio certo errado quadrado redondo oval retangular triangular móvel local regional federal municipal
urbano rural étnico melhor pior maior menor superior inferior""".split())


def adjectifs(niv, src, jeu, deja, variantes):
    out = []
    for cols in lignes(src.ADJECTIFS):
        m, f, fr = cols[0], cols[1], cols[2]
        ex, exfr = (cols[3], cols[4]) if len(cols) > 4 else ("", "")
        d = drapeaux(cols[5:])
        if sans_phrase("adj", m, niv, ex, exfr) or not deja.prendre("adj", m, niv):
            continue
        pl = d.get("pl", pluriel(m))
        fpl = pl if f == m else pluriel(f)
        formes = {"feminin": f, "pluriel": pl, "feminin_pluriel": fpl}
        # Pas de comparatif aux adjectifs de relation (nationalite, -ico, -al...).
        gradue = not (" " in m or m in NON_GRADUES or d.get("nc")
                      or m.endswith(("ês", "ense", "ista", "ico", "ário", "al", "ar", "eiro")))
        if gradue or m in COMPARATIFS or d.get("comp"):
            c = COMPARATIFS.get(m, "mais " + m)
            formes["comparatif"], formes["superlatif"] = c, "o " + c
        if not re.search(r"(?<![\wÀ-ú])(" + "|".join(re.escape(x) for x in {m, f, pl, fpl}) + r")(?![\wÀ-ú])", ex, re.I):
            RAPPORT.append("  %-26s ADJECTIF ABSENT DE SA PHRASE : %s" % (m, ex))
        if "br" in d:
            variantes["adjectifs"][m] = d["br"]
        out.append({"mot": m, "traduction": fr, "exemple": ex, "exemple_fr": exfr, "formes": formes})
    jeu["adjectifs.json"][niv] = out
    return len(out)


def simples(niv, bloc, cl, deja):
    out = []
    for cols in lignes(bloc):
        if len(cols) < 5:
            RAPPORT.append("  %-26s LIGNE INCOMPLETE (%s %s)" % (cols[0], cl, niv))
            continue
        m, fr, cat, ex, exfr = cols[:5]
        if sans_phrase(cl, m, niv, ex, exfr) or not deja.prendre(cl, m, niv):
            continue
        out.append({"mot": m, "traduction": fr, "kategorie": cat, "exemple": ex, "exemple_fr": exfr})
    return out


def fonctionnels(jeu):
    src = module("fonctionnels_niveaux")
    if not src:
        return 0
    n = 0
    f = jeu.setdefault("fonctionnels.json", {})
    # Un mot n'apparait qu'a UN niveau dans une categorie (comme l'allemand et l'anglais).
    vus = {(cle, e["mot"].lower()) for cle, l in f.items() for e in l}
    for niv, blocs in src.FONCTIONNELS.items():
        if niv not in NIVEAUX:
            continue
        for cle, bloc in blocs.items():
            for cols in lignes(bloc):
                mot, fr, cat, ex, exfr = cols[:5]
                assert (cle, mot.lower()) not in vus, "mot-outil deja present (%s, %s) : %s" % (cle, niv, mot)
                vus.add((cle, mot.lower()))
                f.setdefault(cle, []).append({"mot": mot, "traduction": fr, "kategorie": cat, "exemple": ex,
                                              "exemple_fr": exfr, "niveau": niv})
                n += 1
    return n


# ---------------------------------------------------------------- grammaire
def question(topic, q, bonne, fausses, trad, expl):
    options = [bonne] + [x for x in fausses if x != bonne]
    random.Random(q).shuffle(options)
    return {"topic": topic, "question": q, "question_en": q,
            "translation": trad, "translation_en": trad,
            "answers": [bonne], "correct": bonne, "correctEn": bonne,
            "explanation": expl, "explanation_en": expl,
            "options": options, "optionsEn": options}


def questions(topic, bloc):
    vues, qs = set(), []
    for cols in lignes(bloc):
        q, bonne, fausses, trad, expl = cols[:5]
        assert q not in vues, "question en double : " + q
        vues.add(q)
        fausses = [x.strip() for x in fausses.split("/")]
        assert bonne not in fausses, "bonne reponse parmi les fausses : " + q
        qs.append(question(topic, q, bonne, fausses, trad, expl))
    return qs


def grammaire(niv, src, jeu):
    fiches = jeu["grammaire.json"]["fiches"]
    jeux = jeu["exercices.json"]["jeux"]
    textes = jeu["grammaire.json"]["textes"]["fr"]
    ids = {f["id"] for f in fiches}
    nq = 0
    for f in src.FICHES:
        assert f["id"] not in ids, "fiche en double : " + f["id"]
        assert f["serie"] not in jeux, "serie en double : " + f["serie"]
        fiche = {k: f[k] for k in ("id", "titre", "resume", "regle", "tableau", "exemples", "attention")}
        fiche["exercice"] = "exercicesFicheEn_" + f["id"].replace("-", "_")
        fiche["serie"] = f["serie"]
        fiche["niveau"] = niv
        fiche["statut"] = "brouillon"
        fiches.append(fiche)
        ids.add(f["id"])
        qs = questions(f["id"], f["questions"])
        jeux[f["serie"]] = qs
        textes["kicker_" + f["serie"]] = f["kicker"]
        nq += len(qs)
    return len(src.FICHES), nq


def temps(jeu):
    """L'ecran « S'entrainer par temps » : une serie par temps, rangee par
    niveau (temps_<niv>.py), sous la cle « temps » de grammaire.json, comme l'anglais."""
    liste = jeu["grammaire.json"].setdefault("temps", [])
    jeux = jeu["exercices.json"]["jeux"]
    textes = jeu["grammaire.json"]["textes"]["fr"]
    nq = 0
    for niv in NIVEAUX:
        src = module("temps_" + niv.lower())
        if not src:
            continue
        for t in src.TEMPS:
            assert t["serie"] not in jeux, "serie en double : " + t["serie"]
            liste.append({"id": t["id"], "niveau": niv, "titre": t["titre"], "texte": t["texte"], "serie": t["serie"]})
            jeux[t["serie"]] = questions(t["id"], t["questions"])
            textes["kicker_" + t["serie"]] = t["kicker"]
            nq += len(jeux[t["serie"]])
    return len(liste), nq


def conjugaison(jeu):
    """Les feuilles de conjugaison A2-C1 (format de l'anglais : t, l, a)."""
    src = module("conjugaison_niveaux")
    if not src:
        return 0
    c = jeu.setdefault("conjugaison.json", {})
    c.setdefault("niveaux", {})
    jeux = jeu["exercices.json"]["jeux"]
    n = 0
    for niv, feuilles in src.FEUILLES.items():
        if niv not in NIVEAUX:
            continue
        out = []
        for f in feuilles:
            if f["serie"] not in jeux:
                RAPPORT.append("  feuille %-18s serie inconnue : %s" % (f["id"], f["serie"]))
            out.append({"id": f["id"], "serie": f["serie"], "temps": None, "t": {"fr": f["t"]},
                        "l": [[a, {"fr": b}] for a, b in f["l"]], "a": {"fr": f["a"]}})
        c["niveaux"][niv] = out
        n += len(out)
    return n


# ---------------------------------------------------------------- tout
def construire(jeu):
    deja = Deja(jeu)
    ic = icones()
    variantes = jeu.setdefault("variantes-br.json", {"noms": {}, "verbes": {}, "adjectifs": {}})
    for k in ("noms", "verbes", "adjectifs"):
        variantes.setdefault(k, {})
    for k in ("verbes.json", "adjectifs.json", "adverbes.json", "expressions.json"):
        jeu.setdefault(k, {})
    jeu.setdefault("themes.json", {"themes": []})
    jeu.setdefault("grammaire.json", {"textes": {"fr": {}}, "fiches": []})
    jeu["grammaire.json"].setdefault("textes", {}).setdefault("fr", {})
    jeu.setdefault("exercices.json", {"jeux": {}})
    bilan = []
    for niv in NIVEAUX:
        RAPPORT.append("== " + niv)
        n_src, m_src, g_src = module("noms_" + niv.lower()), module("mots_" + niv.lower()), module("grammaire_" + niv.lower())
        nn = noms(niv, n_src, jeu, deja, ic, variantes) if n_src else 0
        nv = na = nad = nex = 0
        if m_src:
            nv = verbes(niv, m_src, jeu, deja, variantes)
            na = adjectifs(niv, m_src, jeu, deja, variantes)
            jeu["adverbes.json"][niv] = simples(niv, m_src.ADVERBES, "adv", deja)
            jeu["expressions.json"][niv] = simples(niv, m_src.EXPRESSIONS, "expr", deja)
            nad, nex = len(jeu["adverbes.json"][niv]), len(jeu["expressions.json"][niv])
        nf = nq = 0
        if g_src:
            nf, nq = grammaire(niv, g_src, jeu)
        bilan.append("%s : %d noms, %d verbes, %d adjectifs, %d adverbes, %d expressions, %d fiches (%d questions)"
                     % (niv, nn, nv, na, nad, nex, nf, nq))
    nte, qte = temps(jeu)
    nfo = fonctionnels(jeu)
    nco = conjugaison(jeu)
    for l in bilan:
        print("Niveaux -- " + l)
    print("Niveaux -- %d mots-outils, %d feuilles de conjugaison, %d series par temps (%d questions)" % (nfo, nco, nte, qte))
    p = os.path.join(ICI, "rapport_niveaux.txt")
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(RAPPORT) + "\n")
    print("Niveaux -- rapport : portugais/outils/rapport_niveaux.txt (%d lignes)" % len(RAPPORT))
    return jeu


def charger_a1():
    """Le jeu A1 deja construit (portugais/datos), ou un jeu vide."""
    jeu = {}
    d = os.path.join(RACINE, "portugais", "datos")
    for nom in ("themes.json", "verbes.json", "adjectifs.json", "adverbes.json", "expressions.json",
                "fonctionnels.json", "grammaire.json", "exercices.json", "conjugaison.json", "variantes-br.json"):
        p = os.path.join(d, nom)
        if os.path.exists(p):
            with io.open(p, encoding="utf-8") as f:
                jeu[nom] = json.load(f)
    # Sans A1 construit : les niveaux A1 de jeu restent vides (essai seul).
    for k in ("verbes.json", "adjectifs.json", "adverbes.json", "expressions.json"):
        if k in jeu:
            jeu[k] = {n: v for n, v in jeu[k].items() if n not in NIVEAUX}
    if "themes.json" in jeu:
        jeu["themes.json"]["themes"] = [t for t in jeu["themes.json"]["themes"] if t.get("niveau") not in NIVEAUX]
    return jeu


if __name__ == "__main__":
    jeu = construire(charger_a1())
    if "--ecrire" in sys.argv:
        dossier = sys.argv[sys.argv.index("--ecrire") + 1]
        os.makedirs(dossier, exist_ok=True)
        for nom, donnees in jeu.items():
            with io.open(os.path.join(dossier, nom), "w", encoding="utf-8", newline="\n") as f:
                json.dump(donnees, f, ensure_ascii=False, indent=1)
                f.write("\n")
        print("Ecrit dans", dossier)
