# -*- coding: utf-8 -*-
"""Tire de nos corpus allemand et espagnol les listes SOURCES de l'A2-C1 portugais.

    python portugais/outils/extraire_niveaux.py            (ecrit les brouillons)
    python portugais/outils/extraire_niveaux.py --ecraser  (reecrit les listes)

OUTIL A USAGE UNIQUE (29 oct. 2026), sur le modele de anglais/outils/
extraire_niveaux.py. Il ecrit noms_a2.py ... noms_c1.py et mots_a2.py ...
mots_c1.py, qui sont ensuite LES SOURCES : on les corrige a la main, on ne
relance pas ce script (il refuse d'ecraser une liste sans --ecraser, et
--ecraser perdrait les corrections).

Ce qu'il fait. Chaque mot allemand (A1-C1) et espagnol (A1-B2) porte sa
traduction portugaise (BRESILIENNE : celle de l'interface pt-BR) et une phrase.
On en tire la tete (« aproximar, passar » -> aproximar), convertie au portugais
d'Europe (variante_niveaux.py : ônibus -> autocarro, econômico -> económico),
gardee au plus bas niveau ou elle parait, sans celles de l'A1. Le genre vient
de l'article de la traduction, de la phrase, ou de la terminaison (« g? » quand
il est devine). La phrase d'exemple est ECRITE dans la source (ex=... # ...),
convertie elle aussi : c'est la qu'un relecteur la corrige.
"""
import io, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import variante_niveaux as V
import banque_niveaux as B
import irreguliers as I

NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
CIBLES = ["A2", "B1", "B2", "C1"]


def charger(p):
    with io.open(os.path.join(RACINE, p), encoding="utf-8") as f:
        return json.load(f)


# ------------------------------------------------------------------ les tetes
VIDES = re.compile(r"\b(algo|alguém|alg\.|alguma coisa|sb|sth)\b", re.I)


def tete(pt, classe):
    """(tete convertie, article trouve ou None)."""
    pt = re.sub(r"\(.*?\)|\[.*?\]", "", pt or "")
    p = re.split(r"[,;/]", pt)[0].strip().strip(".!?")
    art = None
    m = re.match(r"^(o|a|os|as)\s+(.*)$", p)
    if m and classe == "nom":
        art, p = m.group(1), m.group(2)
    p = re.sub(r"\s+", " ", p).strip()
    if classe != "expr" and not (p[:1].isupper() and classe == "nom"):
        p = p.lower() if classe != "nom" or not p[:1].isupper() else p
    return V.mot_europeen(p), art


def tete_valide(h, classe):
    if not h or not re.match(r"^[A-Za-zÀ-ú][A-Za-zÀ-ú' -]*[A-Za-zÀ-ú.!?']$", h):
        return False
    n = len(h.split())
    if VIDES.search(h):
        return False
    if classe == "nom" and n > 4:
        return False
    if classe == "verbe" and (n > 3 or not re.search(r"^\S+(ar|er|ir|or|ôr)(-se)?(\s|$)", h)):
        return False
    if classe in ("adj", "adv") and n > 3:
        return False
    if classe == "expr" and (n < 2 or n > 8):
        return False
    if V.bresilianismes(h):
        return False
    return True


def francais_nom(m):
    fr = (m.get("traduction") or "").strip()
    art = m.get("article_fr")
    if art and not re.match(r"^(le|la|les|l'|un|une|des)\b", fr):
        fr = art + fr
    return fr


# ------------------------------------------------------------------ le genre
DET_M = set("o os um uns do dos no ao aos pelo pelos este estes esse esses aquele aqueles deste destes desse "
            "desses neste nestes nesse num dum meu meus teu teus seu seus nosso nossos todo todos outro outros "
            "novo primeiro último mesmo próprio".split())
DET_F = set("a as uma umas da das na nas à às pela pelas esta estas essa essas aquela aquelas desta destas "
            "dessa dessas nesta nestas nessa numa duma minha minhas tua tuas sua suas nossa nossas toda todas "
            "outra outras nova primeira última mesma própria".split())


def genre_par_terminaison(mot):
    m = mot.lower().split(" ")[0]
    if m.endswith(("ção", "são", "dade", "tude", "gem", "ice", "ez", "eza", "ura", "ia", "ise")):
        return "a", m.endswith(("ção", "dade", "tude", "gem", "eza", "ura"))
    if m.endswith(("ema", "ama", "oma")) and len(m) > 4:
        return "o", False
    if m.endswith("a"):
        return "a", False
    if m.endswith(("o", "ão", "or", "ume", "ês", "al", "el", "il", "ol", "ul")):
        return "o", m.endswith(("o", "or"))
    return "o", False


def genre(mot, art, phrase_br, es_genre):
    """(o/a, sur ?)."""
    if mot.lower() in V.GENRE_EUROPEEN:
        return V.GENRE_EUROPEEN[mot.lower()][0], True
    if art in ("o", "os"):
        return "o", True
    if art in ("a", "as"):
        return "a", True
    m, f = 0, 0
    tete_mot = mot.lower().split(" ")[0]
    for ph in (phrase_br or "",):
        mots = re.findall(r"[\wÀ-ú]+", ph.lower())
        for i, w in enumerate(mots):
            if w.startswith(tete_mot[:max(3, len(tete_mot) - 2)]) and len(w) <= len(tete_mot) + 3:
                for j in (i - 1, i - 2):
                    if j >= 0:
                        if mots[j] in DET_M:
                            m += 2 if j == i - 1 else 1
                            break
                        if mots[j] in DET_F and mots[j] != "a":
                            f += 2 if j == i - 1 else 1
                            break
                        if mots[j] == "a" and j == i - 1:
                            f += 1
                            break
    g_t, sur_t = genre_par_terminaison(mot)
    if m > f:
        return "o", m >= 2 and (g_t == "o" or not sur_t)
    if f > m:
        return "a", f >= 2 and (g_t == "a" or not sur_t)
    if es_genre in ("el", "la"):
        g_es = "o" if es_genre == "el" else "a"
        return g_es, g_es == g_t and sur_t
    return g_t, sur_t


# ------------------------------------------------------------------ le pluriel
PLUR_AES = set("pão cão alemão capitão capelão escrivão tabelião charlatão sacristão catalão".split())
PLUR_AOS = set("mão irmão cidadão cristão órgão órfão sótão bênção grão chão vão desvão cortesão pagão acórdão "
               "girassol".split()) - {"girassol"}


def pluriel(mot):
    """Le pluriel d'un nom (sans article) ; None si invariable."""
    if " de " in mot or " da " in mot or " do " in mot or " das " in mot or " dos " in mot:
        a, sep, b = mot.partition(" d")
        return pluriel(a) + sep + b
    if " " in mot:  # nom + adjectif : les deux
        return " ".join(pluriel(w) if not w in ("e",) else w for w in mot.split(" "))
    if "-" in mot:
        a, b = mot.split("-", 1)
        return pluriel(a) + "-" + (pluriel(b) if not re.match(r"^(de|da|do)$", b) else b)
    m = mot
    if m.endswith("ão"):
        if m in PLUR_AES:
            return m[:-2] + "ães"
        if m in PLUR_AOS:
            return m + "s"
        return m[:-2] + "ões"
    if m.endswith(("x",)) or re.search(r"[aeiou]s$", m) and not re.search(r"(ês|ás|ós|ís|ús|és)$", m) and len(m) > 3:
        return m  # lápis, vírus, ténis, tórax
    if re.search(r"(ês)$", m):
        return m[:-2] + "eses"
    if m.endswith(("ás", "ós", "ís", "ús")):
        return m[:-2] + {"ás": "ases", "ós": "oses", "ís": "ises", "ús": "uses"}[m[-2:]]
    if m.endswith(("r", "z")):
        return m + "es"
    if m.endswith("m"):
        return m[:-1] + "ns"
    if m.endswith("al"):
        return m[:-2] + "ais"
    if m.endswith("ol"):
        return m[:-2] + "óis"
    if m.endswith("ul"):
        return m[:-2] + "uis"
    if m.endswith("el"):
        # papel -> papéis ; nível -> níveis (accent deja sur une autre syllabe)
        return m[:-2] + ("eis" if re.search(r"[áéíóúâêô]", m[:-2]) else "éis")
    if m.endswith("il"):
        return m[:-2] + ("eis" if re.search(r"[áéíóúâêô]", m[:-2]) else "is")
    if m.endswith("n"):
        return m + "s"
    return m + "s"


def pluriel_risque(mot, pl):
    return mot.endswith(("ão", "s", "x", "il", "el")) or " " in mot or "-" in mot or pl == mot


# ------------------------------------------------------------------ les formes
def feminin(adj):
    a = adj
    if " " in a:
        return a
    if a.endswith("o"):
        return a[:-1] + "a"
    if a.endswith("ês") and a not in ("cortês", "descortês"):
        return a[:-2] + "esa"
    if a.endswith("ão"):
        return a[:-2] + "ã"
    if a.endswith("eu") and a not in ("judeu",):
        return a[:-2] + "eia"
    if a.endswith("or") and a not in ("melhor", "pior", "maior", "menor", "superior", "inferior", "anterior",
                                       "posterior", "exterior", "interior", "ulterior", "multicor", "incolor"):
        return a + "a"
    if a.endswith("u") and a.endswith(("nu", "cru")):
        return a + "a"
    return a


def formes_mot(cl, mot):
    if cl == "nom":
        p = pluriel(mot)
        return [mot] + ([p] if p else [])
    if cl == "verbe":
        try:
            t = I.conjuguer(mot)
        except Exception:
            return [mot]
        fs = {mot.replace("-se", "")}
        for k, v in t.items():
            if isinstance(v, list):
                for f in v:
                    fs.update(x for x in re.split(r"[\s-]", f) if len(x) > 2)
            elif isinstance(v, dict):
                fs.update(re.split(r"-", v["tu"])[0:1])
                fs.update(x.split("-")[0] for x in v.values())
        if t.get("participio"):
            p = t["participio"]
            if p.endswith("o"):
                fs.update([p, p[:-1] + "a", p + "s", p[:-1] + "as"])
        fs.discard("tinha")
        fs -= set("tinha tinhas tínhamos tínheis tinham tenho tens tem temos tendes têm que quando nos vos".split()) - {mot}
        return sorted(fs, key=len, reverse=True)
    if cl == "adj":
        f = feminin(mot)
        return list({mot, f, pluriel(mot), pluriel(f)})
    return [mot]


class Choisisseur:
    def __init__(self, banque):
        self.banque = banque
        self.prises = set()

    def choisir(self, mot, formes, classe):
        motifs = [re.compile(r"(?<![\wÀ-ú])" + re.escape(f) + r"(?![\wÀ-ú])", re.I)
                  for f in sorted(set(formes), key=len, reverse=True) if f]
        meilleur, score_max = None, None
        for p in self.banque:
            if p["pt"] in self.prises or not any(m.search(p["pt"]) for m in motifs):
                continue
            # « favor » ne s'illustre pas par « por favor »
            if mot.lower() == "favor" and "por favor" in p["pt"].lower():
                continue
            n = len(p["pt"].split())
            if n < 3:
                continue
            score = 0
            if p["tete"] == mot.lower() and p["classe"] == classe:
                score += 20
            elif p["tete"] == mot.lower():
                score += 4
            if p["classe"] == classe:
                score += 3
            score += {"A1": 6, "A2": 4, "B1": 2}.get(p["niveau"], 0)
            score -= abs(n - 7) * 0.6
            if p["europe"]:
                score -= 8
            if score_max is None or score > score_max:
                meilleur, score_max = p, score
        if meilleur:
            self.prises.add(meilleur["pt"])
            return meilleur["pt"], meilleur["fr"]
        return None


def contient(phrase, formes):
    return any(re.search(r"(?<![\wÀ-ú])" + re.escape(f) + r"(?![\wÀ-ú])", phrase, re.I) for f in formes if f)


# ------------------------------------------------------------------ les themes
THEMES_PT = [
    ("familia",    "Família e relações",       ["familie", "familia", "relaciones", "etapas", "alter_abschied", "erziehung", "vida_diaria"]),
    ("trabalho",   "Trabalho e profissões",    ["berufe", "arbeit_buero", "oficina", "trabajo", "empresa", "comunicacion_profesional", "futuro_trabajo", "liderazgo", "gestion", "dienstleistung", "logistik"]),
    ("comida",     "Comida e cozinha",         ["essen", "kueche", "obst", "cocina", "frutas", "verduras", "gastronomia", "alimentacion", "lebensfuehrung", "comida", "restaurante"]),
    ("casa",       "A casa",                   ["wohnen", "moebel", "casa", "vivienda", "tareas", "herramientas", "taller", "heimwerken", "handwerk", "garten", "materiales"]),
    ("saude",      "O corpo e a saúde",        ["koerper", "gesundheit", "salud", "cuerpo", "medicina", "bienestar", "pflege", "discapacidad"]),
    ("roupa",      "Roupa e aparência",        ["kleidung", "moda", "aspecto", "ropa", "vhs_kapitel1_b1"]),
    ("natureza",   "Natureza e ambiente",      ["tiere", "natur", "wetter", "umwelt", "naturaleza", "medioambiente", "energia", "agricultura", "landwirtschaft", "meer", "geografia", "paisaje", "astronomia", "sostenible", "animales", "clima"]),
    ("viagens",    "Viagens e transportes",    ["verkehr", "reisen", "viaje", "hotel", "aeropuerto", "vacaciones", "orientarse", "movilidad", "transporte"]),
    ("cidade",     "A cidade",                 ["stadt", "urbanismo", "arquitectura", "servicios", "ciudad"]),
    ("escola",     "Escola e estudos",         ["schule", "universitaet", "estudios", "educacion", "investigacion", "ciencia", "escuela"]),
    ("cultura",    "Tempos livres e cultura",  ["freizeit", "musik", "arte", "musica", "cine", "espectaculo", "cultura", "literatura", "critica", "estetica", "buehne", "bild_aufnahme", "feste", "fiestas", "ocio", "vereinsleben", "technik_kunst"]),
    ("desporto",   "Desporto",                 ["sport", "deporte"]),
    ("media",      "Media e comunicação",      ["medien", "tecnologia", "redes", "medios", "datos", "_ia", "periodismo", "comunicacion", "sprache", "bildung_medien", "publicidad", "retorica"]),
    ("dinheiro",   "Dinheiro e economia",      ["einkaufen", "dinero", "economia", "finanzas", "consumo", "konsum", "wirtschaft", "macroeconomia", "industria", "versicherung", "compras"]),
    ("sentimentos", "Sentimentos e caráter",   ["gefuehle", "emociones", "personalidad", "psicologia", "interior", "denken", "incertidumbre"]),
    ("sociedade",  "Sociedade e política",     ["politik", "sociedad", "politica", "inmigracion", "problemas_sociales", "igualdad", "voluntariado", "democracia", "globalizacion", "gesellschaft", "actualidad", "sociologia", "antropologia", "geopolitica", "derechos"]),
    ("lei",        "Lei e segurança",          ["recht", "justicia", "polizei", "sicherheit", "seguridad"]),
    ("ideias",     "Ideias e debate",          ["filosofia", "etica", "bioetica", "religion", "glaube", "ethik", "historia", "geschichte", "memoria", "argument", "pensamiento", "debate", "matices", "registro", "ursache", "konflikt", "negociacion"]),
    ("tempo",      "O tempo",                  ["zeit", "tiempo"]),
    ("quotidiano", "Palavras do dia a dia",    ["grundwortschatz", "zahlen", "farben", "cantidad", "problemas", "movimientos", "vhs_kapitel"]),
]
TAILLE_MAX = 40


def theme_pt(source_id):
    for cle, _, motifs in THEMES_PT:
        if any(m in (source_id or "") for m in motifs):
            return cle
    return "quotidiano"


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
    return [w for w in re.findall(r"[\wÀ-ú]+", t.lower())
            if w not in ("o", "a", "os", "as", "um", "uma", "de", "do", "da", "em", "no", "na", "se", "que", "e", "com",
                         "por", "para", "alguém", "algo")]


def expression_dans_exemple(expr, ex):
    pleins = mots_pleins(expr)
    if not pleins:
        return False
    ex = ex.lower()
    ok = sum(1 for w in pleins if w[:4] in ex)
    return ok / len(pleins) >= 0.6


# ------------------------------------------------------------------ la recolte
def recolter():
    banque = B.preparer()
    ch = Choisisseur(banque)
    trouve = {cl: {} for cl in ("nom", "verbe", "adj", "adv", "expr")}
    a1 = {cl: set() for cl in trouve}

    def prendre(cl, niveau, e, fr, source_theme=None, cat=None, es_genre=None):
        if niveau not in NIVEAUX:
            return
        h, art = tete(e.get("traduction_pt"), cl)
        if not tete_valide(h, cl):
            return
        cle = h.lower()
        if niveau == "A1":
            a1[cl].add(cle)
            return
        ancien = trouve[cl].get(cle)
        if ancien and NIVEAUX.index(ancien["niveau"]) <= NIVEAUX.index(niveau):
            return
        trouve[cl][cle] = {"mot": h, "art": art, "fr": fr.replace("|", "/").strip(), "niveau": niveau,
                           "theme": source_theme, "cat": cat, "es_genre": es_genre,
                           "ex_br": (e.get("exemple_pt") or "").strip(), "ex_fr": (e.get("exemple_fr") or "").strip()}

    for f in ("espanol/datos/temas.json", "themes.json"):
        for t in charger(f)["themes"]:
            for m in t.get("mots", []):
                prendre("nom", (t.get("niveau") or "").upper(), m, francais_nom(m), t["id"],
                        es_genre=(m.get("genre") if f.startswith("espanol") else None))
    for cl, fs in (("verbe", ("espanol/datos/verbos.json", "verbe.json")),
                   ("adj", ("espanol/datos/adjetivos.json", "adjectif.json")),
                   ("adv", ("espanol/datos/adverbios.json", "adverbe.json")),
                   ("expr", ("espanol/datos/expresiones.json", "redewendung.json"))):
        for f in fs:
            for niv, liste in charger(f).items():
                if not isinstance(liste, list):
                    continue
                for e in liste:
                    cat = e.get("kategorie") or e.get("categoria")
                    prendre(cl, niv.upper(), e, (e.get("traduction") or "").strip(), None,
                            (CAT_ADV if cl == "adv" else CAT_EXPR).get(cat, "Tournures" if cl == "expr" else "Manière"))
    # l'A1 (approche : les mots A1 de nos corpus ; niveaux.py controle contre le vrai A1)
    for cl in trouve:
        for cle in list(trouve[cl]):
            if cle in a1[cl]:
                del trouve[cl][cle]
    # les phrases
    stats = {"propre": 0, "banque": 0, "propre_sans_mot": 0, "aucune": 0}
    for cl in ("expr", "nom", "verbe", "adj", "adv"):
        for cle, m in sorted(trouve[cl].items(), key=lambda kv: (NIVEAUX.index(kv[1]["niveau"]), kv[0])):
            formes = formes_mot(cl, m["mot"])
            conv, _ = V.phrase_europeenne(m["ex_br"]) if m["ex_br"] else (None, None)
            if conv:
                conv, fr = B.portugaliser(conv, m["ex_fr"])
                conv = V.accorder_au_francais(conv, fr)
            if conv and (contient(conv, formes) or (cl == "expr" and expression_dans_exemple(m["mot"], conv))):
                m["ex"], m["exfr"] = conv, fr
                ch.prises.add(conv)
                stats["propre"] += 1
                continue
            if cl == "expr":
                m["ex"] = None
                stats["aucune"] += 1
                continue
            x = ch.choisir(m["mot"], formes, cl)
            if x:
                m["ex"], m["exfr"] = x
                stats["banque"] += 1
            elif conv:
                m["ex"], m["exfr"] = conv, fr
                m["douteux"] = True
                stats["propre_sans_mot"] += 1
            else:
                m["ex"] = None
                stats["aucune"] += 1
            if cl == "nom":
                g, sur = genre(m["mot"], m["art"], m["ex_br"], m["es_genre"])
                m["g"], m["g_sur"] = g, sur
    for cle, m in trouve["nom"].items():
        if "g" not in m:
            g, sur = genre(m["mot"], m["art"], m["ex_br"], m["es_genre"])
            m["g"], m["g_sur"] = g, sur
    print("Phrases :", stats)
    return trouve


# ------------------------------------------------------------------ l'ecriture
def phrase_cols(m):
    """Les deux colonnes de la phrase, au format du socle (noms_a1.py)."""
    if not m.get("ex"):
        return ["", ""]
    return [m["ex"].replace("|", "/"), m["exfr"].replace("|", "/")]


def drap_ex(m):
    if not m.get("ex"):
        return ["ex=?"]
    return ["ex?"] if m.get("douteux") else []


def ligne_nom(m):
    mot = m["mot"]
    # Un nom toujours au pluriel (os avós, as férias, os óculos) : article au pluriel.
    plt = mot.endswith("s") and m["fr"].lower().startswith("les ") and not mot.endswith(("ês", "ás", "ós", "ís", "ús"))
    art = (m["g"] + "s") if plt else m["g"]
    cols = ["%s %s" % (art, mot), m["fr"]] + phrase_cols(m)
    if not m["g_sur"]:
        cols.append("g?")
    pl = pluriel(mot)
    if not plt and pluriel_risque(mot, pl):
        cols.append("pl=" + pl)
    return " | ".join(cols + drap_ex(m))


ENTETE = '''# -*- coding: utf-8 -*-
"""%s SOURCE : c'est ici qu'on corrige, puis
python portugais/outils/construire.py (qui appelle niveaux.py apres l'A1).

Tire de nos corpus allemand et espagnol par extraire_niveaux.py (29 oct. 2026),
converti au portugais d'Europe (variante_niveaux.py), puis relu. Meme format
que %s (session socle). BROUILLON : a faire relire par un lusophone du Portugal.

Drapeaux en plus de ceux de l'A1 : « g? » genre devine (a verifier) ; « ex? »
la phrase ne contient pas le mot (a revoir) ; « ex=? » aucune phrase (a ecrire).
"""
'''


def ecrire_niveau(niv, trouve, ecraser):
    n_path = os.path.join(ICI, "noms_%s.py" % niv.lower())
    m_path = os.path.join(ICI, "mots_%s.py" % niv.lower())
    for p in (n_path, m_path):
        if os.path.exists(p) and not ecraser:
            print("  %s existe : on n'y touche pas (--ecraser pour le refaire)" % os.path.basename(p))
            return
    par_theme, icone_theme = {}, {}
    for m in sorted(trouve["nom"].values(), key=lambda x: x["mot"].lower()):
        if m["niveau"] != niv:
            continue
        cle = theme_pt(m["theme"])
        par_theme.setdefault(cle, []).append(m)
        icone_theme.setdefault(cle, {}).setdefault(m["theme"], 0)
        icone_theme[cle][m["theme"]] += 1
    themes, blocs = [], []
    for cle, nom, _ in THEMES_PT:
        mots = par_theme.get(cle, [])
        if not mots:
            continue
        icone = max(icone_theme[cle].items(), key=lambda kv: kv[1])[0]
        parts = [mots[i:i + TAILLE_MAX] for i in range(0, len(mots), TAILLE_MAX)]
        if len(parts) > 1 and len(parts[-1]) < 12:
            reste = parts.pop()
            parts[-1] = parts[-1] + reste
        for i, part in enumerate(parts):
            tid = "%s_%s_pt%s" % (cle, niv.lower(), "" if i == 0 else "_%d" % (i + 1))
            tnom = nom if len(parts) == 1 else "%s %d" % (nom, i + 1)
            themes.append((tid, tnom, icone))
            blocs.append('"%s": """\n%s\n""",' % (tid, "\n".join(ligne_nom(m) for m in part)))
    with io.open(n_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTETE % ("Les noms du %s portugais, par theme." % niv, "noms_a1.py"))
        f.write("\nNIVEAU = %r\n\n# (id du theme, nom portugais, theme source dont on reprend l'icone)\nTHEMES = [\n" % niv)
        for t in themes:
            f.write("    (%r, %r, %r),\n" % t)
        f.write("]\n\nNOMS = {\n" + "\n".join(blocs) + "\n}\n")

    def bloc(cl):
        out = []
        for m in sorted(trouve[cl].values(), key=lambda x: x["mot"].lower()):
            if m["niveau"] != niv:
                continue
            if cl == "expr":
                if m.get("ex"):
                    out.append(" | ".join([m["mot"], m["fr"], m["cat"]] + phrase_cols(m)))
                continue
            if cl == "verbe":
                cols = [m["mot"], m["fr"]] + phrase_cols(m) + (["pron"] if m["mot"].endswith("-se") else [])
            elif cl == "adj":
                cols = [m["mot"], feminin(m["mot"]), m["fr"]] + phrase_cols(m)
            else:
                cols = [m["mot"], m["fr"], m["cat"]] + phrase_cols(m)
            out.append(" | ".join(cols + drap_ex(m)))
        return "\n".join(out)
    with io.open(m_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTETE % ("Verbes, adjectifs, adverbes et expressions du %s portugais." % niv,
                          "mots_a1.py et phrases_a1.py"))
        f.write("\nNIVEAU = %r\n" % niv)
        f.write('\n# « infinitif | traduction | phrase | sa traduction | drapeaux » (formes : irreguliers.py).\nVERBES = """\n%s\n"""\n' % bloc("verbe"))
        f.write('\n# « masculin | feminin | traduction | phrase | sa traduction | drapeaux ».\nADJECTIFS = """\n%s\n"""\n' % bloc("adj"))
        f.write('\n# « adverbe | traduction | categorie | phrase | sa traduction ».\nADVERBES = """\n%s\n"""\n' % bloc("adv"))
        f.write('\n# « expression | traduction | categorie | phrase | sa traduction ».\nEXPRESSIONS = """\n%s\n"""\n'
                % bloc("expr"))
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
