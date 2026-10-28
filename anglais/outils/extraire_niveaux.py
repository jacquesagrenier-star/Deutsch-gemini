# -*- coding: utf-8 -*-
"""Tire de nos corpus allemand et espagnol les listes SOURCES de l'A2-C1 anglais.

    python anglais/outils/extraire_niveaux.py            (ecrit les brouillons)
    python anglais/outils/extraire_niveaux.py --ecraser  (reecrit les listes)

OUTIL A USAGE UNIQUE (27 oct. 2026). Il a ecrit noms_a2.py ... noms_c1.py et
mots_a2.py ... mots_c1.py, qui sont depuis LES SOURCES : on les corrige a la
main, on ne relance pas ce script (il refuse d'ecraser une liste existante sans
--ecraser, et --ecraser perdrait les corrections).

Ce qu'il fait. Chaque mot allemand (A1-C1) et espagnol (A1-B2) porte sa
traduction anglaise : on en tire la tete anglaise (« to claim, to assert » ->
claim), on la garde au plus bas niveau ou elle parait, sans celles deja dans
l'A1 anglais. On ecarte les gloses qui ne sont pas des mots anglais courants,
les mots trop lies a l'Allemagne ou a l'Espagne, et on ramene a l'americain
les tetes britanniques (flat -> apartment, gb=flat ; colour -> color).
La traduction francaise est celle du mot source (meme sens). Les noms sont
regroupes en une vingtaine de themes anglais par niveau.
"""
import io, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import variante
import variante_niveaux as vn

NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
CIBLES = ["A2", "B1", "B2", "C1"]


def charger(p):
    with io.open(os.path.join(RACINE, p), encoding="utf-8") as f:
        return json.load(f)


# ------------------------------------------------------------------ les tetes
VIDES = re.compile(r"\b(sth|sb|something|someone|somebody|one's|oneself)\b", re.I)


def tete(en, classe):
    en = re.sub(r"\(.*?\)|\[.*?\]", "", en or "")
    p = re.split(r"[,;/]", en)[0].strip().strip(".!?")
    if classe != "expr":
        p = re.sub(r"^(the|a|an)\s+", "", p, flags=re.I)
    if classe == "verbe":
        p = re.sub(r"^to\s+", "", p, flags=re.I)
    p = re.sub(r"\s+", " ", p).strip()
    return p


def tete_valide(h, classe):
    if not h or not re.match(r"^[A-Za-z][A-Za-z' -]*[A-Za-z.!?']$", h):
        return False
    n = len(h.split())
    if classe == "nom" and (n > 3 or VIDES.search(h)):
        return False
    if classe == "verbe":
        if n > 3 or VIDES.search(h) or h.lower().startswith(("be ", "become ", "feel ")):
            return False
    if classe in ("adj", "adv") and n > 2:
        return False
    if classe == "expr" and (n < 2 or n > 8):
        return False
    if h.lower() in vn.ECARTES:
        return False
    return True


def vers_americain(h):
    """La tete britannique -> (tete americaine, mot britannique ou None)."""
    bas = h.lower()
    if bas in vn.GB_VERS_US_VOCAB:
        return vn.GB_VERS_US_VOCAB[bas], h
    if bas in vn.US_VERS_GB_VOCAB:
        return h, vn.US_VERS_GB_VOCAB[bas]
    for a, b in variante.ORTHOGRAPHE + vn.ORTHOGRAPHE:
        if bas == b:
            return a, None
    return h, None


def francais_nom(m):
    fr = (m.get("traduction") or "").strip()
    art = m.get("article_fr")
    if art and not re.match(r"^(le|la|les|l'|un|une|des)\b", fr):
        fr = art + fr
    return fr


# ------------------------------------------------------------------ les themes
# Chaque theme source (allemand ou espagnol) -> un theme anglais. Les cles
# inconnues tombent dans « everyday » (signale a l'ecran).
THEMES_EN = [
    ("family",    "Family and relationships", ["familie", "familia", "relaciones", "etapas", "alter_abschied", "erziehung", "vida_diaria"]),
    ("work",      "Work and careers",         ["berufe", "arbeit_buero", "oficina", "trabajo", "empresa", "comunicacion_profesional", "futuro_trabajo", "liderazgo", "gestion", "dienstleistung", "logistik"]),
    ("food",      "Food and cooking",         ["essen", "kueche", "obst", "cocina", "frutas", "verduras", "gastronomia", "alimentacion", "lebensfuehrung", "comida", "restaurante"]),
    ("home",      "Home and DIY",             ["wohnen", "moebel", "casa", "vivienda", "tareas", "herramientas", "taller", "heimwerken", "handwerk", "garten", "materiales"]),
    ("health",    "Body and health",          ["koerper", "gesundheit", "salud", "cuerpo", "medicina", "bienestar", "pflege", "discapacidad"]),
    ("clothes",   "Clothes and appearance",   ["kleidung", "moda", "aspecto", "ropa", "vhs_kapitel1_b1"]),
    ("nature",    "Nature and the environment", ["tiere", "natur", "wetter", "umwelt", "naturaleza", "medioambiente", "energia", "agricultura", "landwirtschaft", "meer", "geografia", "paisaje", "astronomia", "sostenible", "animales", "clima"]),
    ("travel",    "Travel and transportation", ["verkehr", "reisen", "viaje", "hotel", "aeropuerto", "vacaciones", "orientarse", "movilidad", "transporte"]),
    ("city",      "The city",                 ["stadt", "urbanismo", "arquitectura", "servicios", "ciudad"]),
    ("education", "School and studies",       ["schule", "universitaet", "estudios", "educacion", "investigacion", "ciencia", "escuela"]),
    ("culture",   "Free time and culture",    ["freizeit", "musik", "arte", "musica", "cine", "espectaculo", "cultura", "literatura", "critica", "estetica", "buehne", "bild_aufnahme", "feste", "fiestas", "ocio", "vereinsleben", "technik_kunst"]),
    ("sports",    "Sports",                   ["sport", "deporte"]),
    ("media",     "Media and communication",  ["medien", "tecnologia", "redes", "medios", "datos", "_ia", "periodismo", "comunicacion", "sprache", "bildung_medien", "publicidad", "retorica"]),
    ("money",     "Money and the economy",    ["einkaufen", "dinero", "economia", "finanzas", "consumo", "konsum", "wirtschaft", "macroeconomia", "industria", "versicherung", "compras"]),
    ("feelings",  "Feelings and character",   ["gefuehle", "emociones", "personalidad", "psicologia", "interior", "denken", "incertidumbre"]),
    ("society",   "Society and politics",     ["politik", "sociedad", "politica", "inmigracion", "problemas_sociales", "igualdad", "voluntariado", "democracia", "globalizacion", "gesellschaft", "actualidad", "sociologia", "antropologia", "geopolitica", "derechos"]),
    ("law",       "Law and safety",           ["recht", "justicia", "polizei", "sicherheit", "seguridad"]),
    ("ideas",     "Ideas and debate",         ["filosofia", "etica", "bioetica", "religion", "glaube", "ethik", "historia", "geschichte", "memoria", "argument", "pensamiento", "debate", "matices", "registro", "ursache", "konflikt", "negociacion"]),
    ("time",      "Time",                     ["zeit", "tiempo"]),
    ("everyday",  "Everyday words",           ["grundwortschatz", "zahlen", "farben", "cantidad", "problemas", "movimientos", "vhs_kapitel"]),
]
TAILLE_MAX = 40   # au-dela, le theme est coupe en parties (Work 1, Work 2)


def theme_anglais(source_id):
    for cle, _, motifs in THEMES_EN:
        if any(m in source_id for m in motifs):
            return cle
    print("  theme source sans theme anglais :", source_id)
    return "everyday"


# ------------------------------------------------------------------ categories
CAT_ADV = {"Zeit": "Temps", "Art und Weise": "Manière", "Grad/Menge": "Quantité", "Verbindung/Logik": "Liaison",
           "Ort/Richtung": "Lieu", "Häufigkeit": "Fréquence", "Grund/Folge": "Cause et conséquence",
           "Nuance/Ton": "Nuance", "Frageadverbien": "Question", "modo": "Manière", "tiempo": "Temps",
           "cantidad": "Quantité", "discurso": "Liaison", "lugar": "Lieu", "afirmacion": "Affirmation",
           "frecuencia": "Fréquence", "duda": "Doute"}
CAT_EXPR = {"Feste Verbindungen": "Tournures", "Diskussion/Nuance": "Discuter", "Alltag/Organisation": "Au quotidien",
            "Gefühle/Reaktionen": "Réagir", "Meinung/Zustimmung": "Donner son avis", "Begrüßung/Small Talk": "Bavarder",
            "cotidiano": "Au quotidien", "modismo": "Tournures", "cortesia": "Politesse", "saludo": "Saluer",
            "conectar": "Discuter", "matiz": "Nuance", "reaccion": "Réagir", "interjeccion": "Réagir"}


def mots_pleins(t):
    return [w for w in re.findall(r"[a-z']+", t.lower())
            if w not in ("to", "a", "an", "the", "one's", "sb", "sth", "something", "someone", "it", "be", "of")]


def expression_dans_exemple(expr, ex):
    pleins = mots_pleins(expr)
    if not pleins:
        return False
    ex = ex.lower()
    ok = sum(1 for w in pleins if w[:4] in ex)
    return ok / len(pleins) >= 0.6


# ------------------------------------------------------------------ l'A1 deja la
def deja_en_a1():
    d = {"nom": set(), "verbe": set(), "adj": set(), "adv": set(), "expr": set()}
    for t in charger("anglais/datos/themes.json")["themes"]:
        for m in t["mots"]:
            d["nom"].add(m["mot"].lower())
            if m.get("vergleich"):
                d["nom"].add(m["vergleich"].lower())
    for cl, f in (("verbe", "verbes"), ("adj", "adjectifs"), ("adv", "adverbes"), ("expr", "expressions")):
        for v in charger("anglais/datos/%s.json" % f).values():
            for m in v:
                d[cl].add(m["mot"].lower().strip("!?."))
    for v in charger("anglais/datos/fonctionnels.json").values():
        for m in v:
            for cl in ("adv", "expr", "adj"):
                d[cl].add(m["mot"].lower())
    return d


# ------------------------------------------------------------------ la recolte
def recolter():
    deja = deja_en_a1()
    trouve = {cl: {} for cl in ("nom", "verbe", "adj", "adv", "expr")}

    def prendre(cl, niveau, e, fr, source_theme=None, cat=None):
        if niveau not in NIVEAUX:
            return
        h = tete(e.get("traduction_en"), cl)
        if not tete_valide(h, cl):
            return
        us, gb = (vers_americain(h) if cl in ("nom", "adj") else (h, None))
        cle = us.lower()
        if cle in deja[cl]:
            return
        ancien = trouve[cl].get(cle)
        if ancien and NIVEAUX.index(ancien["niveau"]) <= NIVEAUX.index(niveau):
            return
        trouve[cl][cle] = {"mot": us, "gb": gb, "fr": fr.replace("|", "/"), "niveau": niveau,
                           "theme": source_theme, "cat": cat,
                           "ex_en": (e.get("exemple_en") or "").strip(), "ex_fr": (e.get("exemple_fr") or "").strip()}

    for f in ("themes.json", "espanol/datos/temas.json"):
        for t in charger(f)["themes"]:
            for m in t.get("mots", []):
                prendre("nom", (t.get("niveau") or "").upper(), m, francais_nom(m), t["id"])
    for cl, fs in (("verbe", ("verbe.json", "espanol/datos/verbos.json")),
                   ("adj", ("adjectif.json", "espanol/datos/adjetivos.json")),
                   ("adv", ("adverbe.json", "espanol/datos/adverbios.json")),
                   ("expr", ("redewendung.json", "espanol/datos/expresiones.json"))):
        for f in fs:
            for niv, liste in charger(f).items():
                if not isinstance(liste, list):
                    continue
                for e in liste:
                    cat = e.get("kategorie") or e.get("categoria")
                    prendre(cl, niv.upper(), e, (e.get("traduction") or "").strip(), None,
                            (CAT_ADV if cl == "adv" else CAT_EXPR).get(cat, "Tournures" if cl == "expr" else "Manière"))
    return trouve


# ------------------------------------------------------------------ l'ecriture
def drapeaux_nom(m):
    mot = m["mot"]
    d = []
    bas = mot.lower()
    dernier = bas.split()[-1]
    if bas in vn.PLURIELS_IRREGULIERS or dernier in vn.PLURIELS_IRREGULIERS:
        pl = vn.PLURIELS_IRREGULIERS.get(bas) or bas.rsplit(" ", 1)[0] + " " + vn.PLURIELS_IRREGULIERS[dernier]
        d.append("pl=" + pl)
    elif bas in vn.PLURIEL_SEUL or dernier in vn.PLURIEL_SEUL:
        d.append("plt")
    elif bas in vn.INDENOMBRABLES or dernier in vn.INDENOMBRABLES:
        d.append("u")
    elif bas.endswith("ics") or (bas.endswith("ness") and not bas.endswith(
            ("witness", "business", "harness", "wilderness"))):
        d.append("u")
    if m["gb"] and m["gb"].lower() != bas:
        d.append("gb=" + m["gb"])
    return d


def ligne(m, extra=()):
    cols = [m["mot"], m["fr"]] + list(extra)
    return " | ".join(c for c in cols if c is not None)


ENTETE = '''# -*- coding: utf-8 -*-
"""%s SOURCE : c'est ici qu'on corrige, puis
python anglais/outils/construire.py.

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (27 oct. 2026),
puis relu. Meme format que %s. BROUILLON : a faire relire par un anglophone.
"""
'''


def ecrire_niveau(niv, trouve, ecraser):
    n_path = os.path.join(ICI, "noms_%s.py" % niv.lower())
    m_path = os.path.join(ICI, "mots_%s.py" % niv.lower())
    for p in (n_path, m_path):
        if os.path.exists(p) and not ecraser:
            print("  %s existe : on n'y touche pas (--ecraser pour le refaire)" % os.path.basename(p))
            return
    # Les noms, par theme anglais.
    par_theme, icone_theme = {}, {}
    for m in sorted(trouve["nom"].values(), key=lambda x: x["mot"].lower()):
        if m["niveau"] != niv:
            continue
        cle = theme_anglais(m["theme"])
        par_theme.setdefault(cle, []).append(m)
        icone_theme.setdefault(cle, {}).setdefault(m["theme"], 0)
        icone_theme[cle][m["theme"]] += 1
    themes, blocs = [], []
    for cle, nom, _ in THEMES_EN:
        mots = par_theme.get(cle, [])
        if not mots:
            continue
        icone = max(icone_theme[cle].items(), key=lambda kv: kv[1])[0]
        parts = [mots[i:i + TAILLE_MAX] for i in range(0, len(mots), TAILLE_MAX)]
        if len(parts) > 1 and len(parts[-1]) < 12:
            reste = parts.pop()
            parts[-1] = parts[-1] + reste
        for i, part in enumerate(parts):
            tid = "%s_%s%s" % (cle, niv.lower(), "" if i == 0 else "_%d" % (i + 1))
            tnom = nom if len(parts) == 1 else "%s %d" % (nom, i + 1)
            themes.append((tid, tnom, icone))
            blocs.append('"%s": """\n%s\n""",' % (tid, "\n".join(ligne(m, drapeaux_nom(m)) for m in part)))
    with io.open(n_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTETE % ("Les noms du %s anglais, par theme." % niv, "noms_a1.py"))
        f.write("\nNIVEAU = %r\n\n# (id, nom du theme en anglais, theme source dont on reprend l'icone)\nTHEMES = [\n" % niv)
        for t in themes:
            f.write("    (%r, %r, %r),\n" % t)
        f.write("]\n\nNOMS = {\n" + "\n".join(blocs) + "\n}\n")
    # Verbes, adjectifs, adverbes, expressions.
    def bloc(cl, avec_cat=False, avec_ex=False):
        out = []
        for m in sorted(trouve[cl].values(), key=lambda x: x["mot"].lower()):
            if m["niveau"] != niv:
                continue
            extra = []
            if avec_cat:
                extra.append(m["cat"])
            if avec_ex:
                if not (m["ex_en"] and m["ex_fr"] and expression_dans_exemple(m["mot"], m["ex_en"])):
                    continue
                extra += [m["ex_en"].replace("|", "/"), m["ex_fr"].replace("|", "/")]
            if cl == "adj" and m["gb"]:
                extra.append("gb=" + m["gb"])
            out.append(ligne(m, extra))
        return "\n".join(out)
    with io.open(m_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTETE % ("Verbes, adjectifs, adverbes et expressions du %s anglais." % niv, "mots_a1.py et phrases_a1.py"))
        f.write("\nNIVEAU = %r\n" % niv)
        f.write('\n# « verbe | traduction | drapeaux » ; les formes sont calculees (irreguliers.py).\nVERBES = """\n%s\n"""\n' % bloc("verbe"))
        f.write('\n# « adjectif | traduction | drapeaux » (gb=, ex=).\nADJECTIFS = """\n%s\n"""\n' % bloc("adj"))
        f.write('\n# « adverbe | traduction | categorie | drapeaux ».\nADVERBES = """\n%s\n"""\n' % bloc("adv", avec_cat=True))
        f.write('\n# « expression | traduction | categorie | exemple anglais | exemple francais ».\nEXPRESSIONS = """\n%s\n"""\n'
                % bloc("expr", avec_cat=True, avec_ex=True))
    print("  %s : %d themes de noms ecrits" % (niv, len(themes)))


def main():
    ecraser = "--ecraser" in sys.argv
    trouve = recolter()
    for cl, d in trouve.items():
        print(cl, {n: sum(1 for m in d.values() if m["niveau"] == n) for n in CIBLES})
    for niv in [a.upper() for a in sys.argv[1:] if not a.startswith("--")] or CIBLES:
        ecrire_niveau(niv, trouve, ecraser)


if __name__ == "__main__":
    main()
