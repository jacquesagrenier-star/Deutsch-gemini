# -*- coding: utf-8 -*-
"""Les textes Soins : dialogues, grammaire, ecrit (pflege/sources/LISEZ-MOI.md).

    python pflege/outils/textes.py extraire              # prepare traductions/<langue>/ (garde l'existant)
    python pflege/outils/textes.py extraire --langue tr  # une seule langue
    python pflege/outils/textes.py construire            # fait pflege/datos/{dialogues,grammaire,ecrit}.json
    python pflege/outils/textes.py etat                  # ce qui reste a traduire, par langue et par famille

Regle d'unite : tout objet qui a une cle "fr" est un texte a traduire ; ses traductions sont ses cles soeurs.
Les noms sont des gabarits ({elif}, {brandt:dat}) remplaces a la construction depuis noms.json.
"""
import copy, io, json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PFLEGE = os.path.join(RACINE, "pflege")
SOURCES = os.path.join(PFLEGE, "sources")
TRAD = os.path.join(SOURCES, "traductions")
DATOS = os.path.join(PFLEGE, "datos")
LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]
AUTRES = LANGUES[1:]
FAMILLES = ["dialogues", "grammaire", "ecrit"]
GABARIT = re.compile(r"\{([a-z_]+)(?::([a-z]+))?\}")
# Cles qui ne sont jamais des textes a traduire, meme dans un objet qui a "fr".
NON_TEXTE = {"t", "dit", "relire", "relire_note", "qui", "air", "va", "faux", "repete", "pose", "si", "juste",
             "options", "morceaux", "type", "id", "valeur", "prononce", "couvre", "de"}


def lire(chemin):
    with io.open(chemin, encoding="utf-8") as f:
        return json.load(f)


def ecrire(chemin, donnees, compact=False):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with io.open(chemin, "w", encoding="utf-8", newline="\n") as f:
        if compact:
            json.dump(donnees, f, ensure_ascii=False, separators=(",", ":"))
        else:
            json.dump(donnees, f, ensure_ascii=False, indent=1)
        f.write("\n")


def sources(famille):
    """[(id, chemin, donnees)] dans l'ordre des noms de fichiers."""
    dossier = os.path.join(SOURCES, famille)
    if not os.path.isdir(dossier):
        return []
    out = []
    for nom in sorted(os.listdir(dossier)):
        if nom.endswith(".json"):
            out.append((nom[:-5], os.path.join(dossier, nom), lire(os.path.join(dossier, nom))))
    return out


def unites(obj, chemin=""):
    """Chaque objet a traduire (qui a "fr"), avec son chemin stable : noeuds.klingel.choix.0.puis.1"""
    if isinstance(obj, dict):
        if "fr" in obj and isinstance(obj["fr"], str):
            yield chemin, obj
        for k, v in obj.items():
            if k in LANGUES or k.startswith("_"):
                continue
            if isinstance(v, (dict, list)):
                yield from unites(v, (chemin + "." if chemin else "") + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from unites(v, (chemin + "." if chemin else "") + str(i))


def chemin_traduction(langue, famille, ident):
    return os.path.join(TRAD, langue, famille, ident + ".json")


# ---------------------------------------------------------------- noms

def noms():
    """{langue: {id: {forme: texte}}} : allemand, francais (source), puis les traductions."""
    src = lire(os.path.join(SOURCES, "noms.json"))["personnes"]
    out = {"de": {}, "fr": {}}
    for ident, p in src.items():
        out["de"][ident] = p.get("de", {})
        out["fr"][ident] = p.get("fr", {})
    for l in AUTRES:
        ch = os.path.join(TRAD, l, "noms.json")
        out[l] = lire(ch).get("personnes", {}) if os.path.exists(ch) else {}
    return out


def remplacer(texte, langue, table, manques, forme_dit=False):
    if not isinstance(texte, str):
        return texte

    def r(m):
        ident, forme = m.group(1), m.group(2) or ""
        formes = table.get(langue, {}).get(ident)
        if formes is None:
            manques.append("%s : nom inconnu {%s}" % (langue, m.group(0)[1:-1]))
            return m.group(0)
        if forme_dit and forme == "" and "dit" in formes:
            v = formes["dit"]
        elif forme not in formes:
            manques.append("%s : {%s} sans la forme « %s »" % (langue, ident, forme))
            v = formes.get("", m.group(0))
        else:
            v = formes[forme]
        # Debut de phrase : majuscule (« la docteure Sommer » -> « La docteure Sommer »).
        avant = texte[:m.start()].rstrip(" \u00ab\u00a0\"'(")
        if v and (avant == "" or avant[-1] in ".?!\u2026\n"):
            v = v[0].upper() + v[1:]
        return v
    return GABARIT.sub(r, texte)


# ---------------------------------------------------------------- extraire

def extraire(langues=None):
    for l in (langues or AUTRES):
        for famille in FAMILLES:
            for ident, _, d in sources(famille):
                ch = chemin_traduction(l, famille, ident)
                ancien = lire(ch).get("cles", {}) if os.path.exists(ch) else {}
                cles = {}
                for chemin, u in unites(d):
                    e = {"fr": u["fr"]}
                    if "t" in u:
                        e["de"] = u["t"]
                    vieux = ancien.get(chemin)
                    if vieux and vieux.get(l):
                        if vieux.get("fr") == u["fr"] and vieux.get("de") == u.get("t"):
                            e[l] = vieux[l]
                        else:
                            e[l] = vieux[l]
                            e["perime"] = True
                    else:
                        e[l] = ""
                    cles[chemin] = e
                ecrire(ch, {"_langue": l, "_source": "pflege/sources/%s/%s.json" % (famille, ident), "cles": cles})
        # Les noms : une entree par personne, avec les formes du francais a remplir (les cas en plus, si besoin).
        chn = os.path.join(TRAD, l, "noms.json")
        anc = lire(chn).get("personnes", {}) if os.path.exists(chn) else {}
        src = lire(os.path.join(SOURCES, "noms.json"))["personnes"]
        pers = {}
        for ident, p in src.items():
            formes = dict(anc.get(ident, {}))
            for forme in p.get("fr", {}):
                if forme in ("a", "de"):  # formes propres au francais (contraction de l'article)
                    continue
                formes.setdefault(forme, "")
            pers[ident] = formes
        ecrire(chn, {"_langue": l, "_note": "Les noms dans cette langue. \"\" = forme courante ; voc = pour s'adresser a la personne ; ajouter les cas utilises par les traductions (gen, dat, acc, ins, loc...).", "personnes": pers})
    print("extraire : fait (%s)" % ", ".join(langues or AUTRES))


# ---------------------------------------------------------------- construire

def fusionner(famille, ident, d, manques):
    """Copie de la source avec les traductions versees dans chaque unite."""
    d = copy.deepcopy(d)
    index = dict(unites(d))
    for l in AUTRES:
        ch = chemin_traduction(l, famille, ident)
        cles = lire(ch).get("cles", {}) if os.path.exists(ch) else {}
        for chemin, u in index.items():
            e = cles.get(chemin)
            if not e or not e.get(l):
                manques.append("%s : %s/%s %s : pas de traduction" % (l, famille, ident, chemin))
                continue
            if e.get("perime") or e.get("fr") != u["fr"] or e.get("de") != u.get("t"):
                manques.append("%s : %s/%s %s : traduction perimee" % (l, famille, ident, chemin))
                continue
            u[l] = e[l]
    return d


def resoudre(obj, table, manques, langue_cle=None):
    """Remplace les gabarits de noms : "t"/"dit" en allemand, chaque cle de langue dans sa langue."""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k in ("t", "titre_de") and isinstance(v, str):
                out[k] = remplacer(v, "de", table, manques)
            elif k == "dit" and isinstance(v, str):
                out[k] = remplacer(v, "de", table, manques, forme_dit=True)
            elif k in LANGUES and isinstance(v, str):
                out[k] = remplacer(v, k, table, manques)
            elif k in ("options", "morceaux", "juste", "valeur") and isinstance(v, (list, str)):
                out[k] = resoudre(v, table, manques, "de")
            else:
                out[k] = resoudre(v, table, manques, langue_cle)
        return out
    if isinstance(obj, list):
        return [resoudre(v, table, manques, langue_cle) for v in obj]
    if isinstance(obj, str) and langue_cle == "de":
        return remplacer(obj, "de", table, manques)
    return obj


def chemin_juste(d):
    """Le chemin modele : premier choix juste de chaque noeud, jusqu'a la fin. Sert a « remettre dans l'ordre »
    et a « jouer son role ». Chaque element : {qui, t, dit?, langues...} ; qui = le role pour l'apprenant."""
    out, vus, n = [], set(), d.get("debut")
    while n is not None and n not in vus:
        vus.add(n)
        noeud = d["noeuds"][n]
        for r in noeud.get("dit", []):
            if "qui" in r:
                out.append({k: v for k, v in r.items() if k not in ("air", "relire", "relire_note")})
        justes = [c for c in noeud.get("choix", []) if not c.get("faux") and not c.get("repete")]
        if not justes:
            break
        c = justes[0]
        ligne = {"qui": d["role"]}
        ligne.update({k: v for k, v in c.items() if k in ["t", "dit"] + LANGUES})
        out.append(ligne)
        for r in c.get("puis", []):
            out.append({k: v for k, v in r.items() if k not in ("air", "relire", "relire_note")})
        n = c.get("va")
    return out


def construire_tout(ecrire_fichiers=True):
    """Fait les trois fichiers de datos/. Rend (donnees_par_famille, manques)."""
    table = noms()
    manques, res = [], {}
    for famille in FAMILLES:
        elements = []
        for ident, _, d in sources(famille):
            m = fusionner(famille, ident, d, manques)
            m = resoudre(m, table, manques)
            if famille == "dialogues":
                m["chemin"] = chemin_juste(m)
            elements.append(m)
        cle = {"dialogues": "dialogues", "grammaire": "points", "ecrit": "taches"}[famille]
        doc = {"_note": "DERIVE de pflege/sources/%s/ par pflege/outils/textes.py construire : ne pas corriger a la main (pflege/sources/LISEZ-MOI.md). Langues : %s." % (famille, " ".join(LANGUES)),
               "langues": LANGUES, cle: elements}
        if famille == "dialogues":
            doc["personnes"] = {i: {"genre": p.get("genre"), "role": p.get("role")}
                                for i, p in lire(os.path.join(SOURCES, "noms.json"))["personnes"].items()}
        res[famille] = doc
        if ecrire_fichiers and elements:
            ecrire(os.path.join(DATOS, famille + ".json"), doc, compact=True)
    return res, manques


def etat():
    _, manques = construire_tout(ecrire_fichiers=False)
    compte = {}
    for m in manques:
        l = m.split(" : ")[0]
        compte[l] = compte.get(l, 0) + 1
    for l in LANGUES + ["de"]:
        if l in compte:
            print("  %s : %d manques" % (l, compte[l]))
    if not manques:
        print("  rien ne manque")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    if not a or a[0] not in ("extraire", "construire", "etat"):
        print(__doc__)
        sys.exit(1)
    if a[0] == "extraire":
        langues = [a[a.index("--langue") + 1]] if "--langue" in a else None
        extraire(langues)
    elif a[0] == "construire":
        _, manques = construire_tout()
        print("construire : pflege/datos/ fait, %d manques (traductions ou noms)" % len(manques))
        for m in manques[:15]:
            print("  " + m)
    else:
        etat()
