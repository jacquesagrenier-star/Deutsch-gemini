# -*- coding: utf-8 -*-
"""Les textes Soins : dialogues, grammaire, ecrit (pflege/sources/LISEZ-MOI.md).

    python pflege/outils/textes.py extraire              # prepare traductions/<langue>/ (garde l'existant)
    python pflege/outils/textes.py extraire --langue tr  # une seule langue
    python pflege/outils/textes.py construire            # fait pflege/datos/{dialogues,grammaire,ecrit,redemittel}.json
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
LANGUES = ["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]   # l'ordre du contrat (pflege/FORMAT-DONNEES.md)
AUTRES = LANGUES[1:]
FAMILLES = ["dialogues", "grammaire", "ecrit", "redemittel"]
# Les cartes-phrases (FORMAT-DONNEES.md, 2 bis) : les fonctions et les groupes (tenus ici), les cartes sans dialogue
# (pflege/sources/redemittel/<groupe>.json, ecrites par pflege-examen) ; les cartes des dialogues viennent de leur
# champ « redemittel ».
FONCTIONS_RM = os.path.join(SOURCES, "redemittel-fonctions.json")
GROUPE_DIALOGUE = {1: "patient", 2: "patient", 3: "patient", 4: "negociation", 5: "famille", 6: "releve", 7: "sbar",
                   8: "patient", 9: "patient", 10: "patient", 11: "collegues", 12: "patient", 13: "patient",
                   14: "patient", 15: "patient", 16: "collegues", 17: "visite", 18: "negociation", 19: "telephone",
                   20: "collegues", 21: "collegues", 22: "collegues", 23: "famille", 24: "famille", 25: "patient",
                   26: "famille"}
GABARIT = re.compile(r"\{([a-z_]+)(?::([a-z]+))?\}")
TUTOIEMENT = re.compile(r"\b(du|dich|dir|dein\w*)\b")
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
    out = []
    if famille == "redemittel":
        out.append(("fonctions", FONCTIONS_RM, lire(FONCTIONS_RM)))
    if not os.path.isdir(dossier):
        return out
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
                    if u.get(l):
                        e[l] = u[l]   # ecrite dans la source : recopiee telle quelle
                    elif vieux and vieux.get(l):
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
            if u.get(l):
                continue   # une traduction ecrite dans la source l'emporte (cartes de pflege-examen, fonctions)
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
            m.setdefault("id", ident)
            if famille == "dialogues":
                m["chemin"] = chemin_juste(m)
            elements.append(m)
        cle = {"dialogues": "dialogues", "grammaire": "points", "ecrit": "taches", "redemittel": "sources"}[famille]
        doc = {"_note": "DERIVE de pflege/sources/%s/ par pflege/outils/textes.py construire : ne pas corriger a la main (pflege/sources/LISEZ-MOI.md). Langues : %s." % (famille, " ".join(LANGUES)),
               "langues": LANGUES, cle: elements}
        if famille == "dialogues":
            doc["personnes"] = {i: {"genre": p.get("genre"), "role": p.get("role")}
                                for i, p in lire(os.path.join(SOURCES, "noms.json"))["personnes"].items()}
        res[famille] = doc
    if ecrire_fichiers:
        for famille, doc in exporter(res).items():
            ecrire(os.path.join(DATOS, famille + ".json"), doc, compact=True)
    return res, manques


# ---------------------------------------------------------------- le format du contrat (pflege/FORMAT-DONNEES.md)
# Ce qui sort dans pflege/datos/ : les champs du contrat (§ 2, 3, 4), puis, en plus, ce que le contrat ne prevoit
# pas encore (l'arbre des branches, les modeles B1, la grille), sous des cles qui ne gênent pas sa lecture.

SCENE = {1: "soins-zimmer", 2: "soins-zimmer", 3: "soins-zimmer", 4: "soins-zimmer", 5: "soins-stationszimmer",
         6: "soins-uebergabe", 7: "soins-stationszimmer", 8: "soins-altenheim", 9: "soins-altenheim",
         10: "soins-ambulant", 11: "soins-stationszimmer", 12: "soins-altenheim",
         13: "soins-aufnahme", 14: "soins-zimmer", 15: "soins-zimmer", 16: "soins-zimmer", 17: "soins-visite",
         18: "soins-stationszimmer", 19: "soins-stationszimmer", 20: "soins-stationszimmer",
         21: "soins-stationszimmer", 22: "soins-uebergabe", 23: "soins-stationszimmer", 24: "soins-altenheim",
         25: "soins-zimmer", 26: "soins-altenheim"}
LIEU = {1: "chambre", 2: "chambre", 3: "chambre", 4: "chambre", 5: "couloir", 6: "poste de soins",
        7: "poste de soins, la nuit", 8: "maison de retraite, chambre", 9: "maison de retraite",
        10: "domicile", 11: "salle du personnel, téléphone", 12: "maison de retraite, couloir, la nuit",
        13: "admission", 14: "chambre", 15: "chambre", 16: "chambre, urgence", 17: "visite médicale",
        18: "poste de soins", 19: "poste de soins, téléphone", 20: "poste de soins", 21: "bureau de la cadre",
        22: "salle du personnel", 23: "poste de soins, téléphone", 24: "maison de retraite",
        25: "chambre, sortie", 26: "maison de retraite, chambre"}
PREPARE = {"oral-1": "sprechen_1", "oral-2": "sprechen_2", "oral-3": "sprechen_3", "hoeren": "hoeren_2",
           "lesen": "lesen_3", "schreiben": "schreiben"}
PREPARE_HOEREN = {6: "hoeren_3", 7: "hoeren_1", 11: "hoeren_1", 19: "hoeren_1", 23: "hoeren_1"}   # relève = réunion d'équipe ; téléphone = messages
TYPE_ECRIT = {"aufnahmebericht": "aufnahme", "biografiebericht": "biografie", "pflegebericht": "pflegebericht",
              "sturzprotokoll": "sturz", "nachricht": "nachricht"}


def trad(u):
    return {l: u[l] for l in LANGUES if isinstance(u, dict) and u.get(l)}


def texte_de(u, cle="de"):
    """{de, trad, lecture?} d'une unité qui a "t"."""
    out = {cle: u["t"], "trad": trad(u)}
    if u.get("dit"):
        out["lecture"] = u["dit"]
    if u.get("relire_note"):
        out["relire"] = u["relire_note"]
    return out


def cellule(x):
    return texte_de(x) if isinstance(x, dict) and "t" in x else (trad(x) if isinstance(x, dict) else x)


def notes_relire(el):
    notes = []
    if el.get("relire_notes"):
        notes.append(el["relire_notes"]["fr"])
    for chemin, u in unites(el):
        if u.get("relire") and u.get("relire_note") and not chemin.startswith("chemin."):
            notes.append("%s : %s" % (u.get("t", "")[:60], u["relire_note"]))
    return ("⚕️ " + " · ".join(notes)) if notes else ""


def lignes_lecture(obj):
    """L'arbre des branches, avec « lecture » à la place de « dit » sur une réplique (le contrat)."""
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if k == "dit" and isinstance(v, str):
                out["lecture"] = v
            else:
                out[k] = lignes_lecture(v)
        return out
    if isinstance(obj, list):
        return [lignes_lecture(v) for v in obj]
    return obj


def exporter(res):
    ids_g = {p["id"]: "soins_gr_%02d_%s" % (p["numero"], p["cle"].replace("-", "_")) for p in res["grammaire"]["points"]}
    ids_d = {}
    for d in res["dialogues"]["dialogues"]:
        ids_d[d["id"][:3]] = "soins_dlg_%02d_%s" % (d["numero"], d["id"][4:].replace("-", "_"))
    note = ("DERIVE de pflege/sources/ par pflege/outils/textes.py construire : ne pas corriger a la main. "
            "Format : pflege/FORMAT-DONNEES.md (§ 2 a 4) ; en plus du contrat : %s.")
    # Dialogues
    dialogues = []
    for d in res["dialogues"]["dialogues"]:
        n = d["numero"]
        prepare = []
        for t in d.get("telc", []):
            p = PREPARE_HOEREN.get(n, PREPARE[t]) if t == "hoeren" else PREPARE[t]
            if p not in prepare:
                prepare.append(p)
        repliques = []
        for r in d["chemin"]:
            x = {"qui": r["qui"], "de": r["t"], "trad": trad(r)}
            if r.get("dit"):
                x["lecture"] = r["dit"]
            repliques.append(x)
        questions = [{"type": "choix", "de": q["q"]["t"], "trad": trad(q["q"]),
                      "choix": [{"de": o["t"], "trad": trad(o)} for o in q["options"]], "bon": q["juste"]}
                     for q in d["ecouter"]]
        dialogues.append({
            "id": ids_d[d["id"][:3]], "source": d["id"], "numero": n, "niveau": d["niveau"],
            "titre_de": d["titre"]["t"], "titre": trad(d["titre"]), "lieu": LIEU[n], "scene": SCENE[n],
            "personnages": [d["role"]] + d["personnes"], "apprenant": d["role"], "registre": d["registre"],
            "intro": trad(d["intro"]), "but": trad(d["but"]),
            "repliques": repliques, "redemittel": [texte_de(r) for r in d["redemittel"]], "questions": questions,
            "grammaire": [ids_g[g] for g in d["grammaire"] if g in ids_g], "prepare": prepare,
            "relire": notes_relire(d),
            "debut": d["debut"], "noeuds": lignes_lecture(d["noeuds"]),
        })
    # Grammaire
    points = []
    for p in res["grammaire"]["points"]:
        serie = []
        for q in p["serie"]:
            x = {"type": "ordre" if q["type"] == "ordre" else "choix"}
            if q["type"] == "trou":
                x.update({"de": q["t"], "choix": q["options"], "bon": q["options"].index(q["juste"])})
            elif q["type"] == "choix":
                x.update({"de": "___", "choix": q["options"], "bon": q["juste"]})
            else:
                x["mots"] = q["morceaux"]
            if q.get("consigne"):
                x["consigne"] = trad(q["consigne"])
            x.update({"phrase": q["phrase"]["t"], "trad": trad(q["phrase"]), "note": trad(q["explication"])})
            if q["phrase"].get("dit"):
                x["lecture"] = q["phrase"]["dit"]
            serie.append(x)
        points.append({
            "id": ids_g[p["id"]], "source": p["id"], "numero": p["numero"], "niveau": p["niveau"],
            "titre": trad(p["titre"]), "resume": trad(p["resume"]), "regle": trad(p["regle"]),
            "tableau": [[cellule(c) for c in ligne] for ligne in p.get("tableau", [])],
            "exemples": [texte_de(e) for e in p["exemples"]], "piege": trad(p["piege"]),
            "renvoi": p.get("renvoi") or "", "dialogues": [ids_d[x] for x in p.get("dialogues", []) if x in ids_d],
            "serie": serie, "relire": notes_relire(p),
        })
    # Écrit
    taches = {t["id"]: t for t in res["ecrit"]["taches"]}
    banques = {i: t for i, t in taches.items() if i.startswith("briques")}
    sujets, rang = [], {}
    for t in res["ecrit"]["taches"]:
        if t["id"].startswith(("briques", "grille")):
            continue
        typ = TYPE_ECRIT[t["genre"]]
        rang[typ] = rang.get(typ, 0) + 1
        b = t.get("briques")
        groupes = banques[b]["groupes"] if isinstance(b, str) else ([{"briques": b}] if b else [])
        niv = t["niveau"].split("-")
        s = {"id": "soins_ecrit_%s_%02d" % (typ, rang[typ]), "source": t["id"], "type": typ,
             "niveau": niv[0], "niveau_max": niv[-1], "examen": bool(t.get("examen")), "lieu": t.get("lieu"),
             "titre_de": t["titre"]["t"], "titre": trad(t["titre"]),
             "consigne_de": t["consigne"]["t"], "consigne": trad(t["consigne"]),
             "fiche": {"titre_de": t["fiche"]["titre"]["t"], "titre": trad(t["fiche"]["titre"]),
                       "rubriques": [{"rubrique_de": r["t"], "rubrique": trad(r), "texte_de": r["valeur"]}
                                     for r in t["fiche"]["rubriques"]]},
             "briques": [texte_de(x) for g in groupes for x in g["briques"]],
             "briques_groupes": [{"titre_de": g["titre"]["t"], "titre": trad(g["titre"]),
                                  "briques": [texte_de(x) for x in g["briques"]]} for g in groupes if g.get("titre")],
             "corrige_de": t["modele"]["t"], "corrige": trad(t["modele"]), "corrige_niveau": t["modele"]["niveau"],
             "points_cles": [p["t"] for p in t["points"]],
             "points": [{"id": p["id"], "de": p["t"], "trad": trad(p)} for p in t["points"]],
             "pieges": [trad(x) for x in t.get("pieges", [])], "grille": t.get("grille") or "",
             "relire": notes_relire(t)}
        if t.get("modele_b1"):
            s["corrige_b1_de"] = t["modele_b1"]["t"]
            s["corrige_b1"] = trad(t["modele_b1"])
        sujets.append(s)
    grilles = {}
    for i, g in taches.items():
        if i.startswith("grille"):
            grilles[i] = {"titre": trad(g["titre"]), "intro": trad(g["intro"]),
                          "echelle": [{"points": e["points"], "texte": trad(e)} for e in g["echelle"]],
                          "criteres": [{"id": c["id"], "titre": trad(c["titre"]), "question": trad(c["question"]),
                                        "conseil": trad(c["conseil"]),
                                        "niveaux": [{"points": n["points"], "texte": trad(n)} for n in c["niveaux"]]}
                                       for c in g["criteres"]],
                          "seuils": trad(g["seuils"])}
    # Cartes-phrases (FORMAT-DONNEES.md, 2 bis)
    srm = {x["id"]: x for x in res["redemittel"]["sources"]}
    fonctions = srm["fonctions"]
    ordre_f = [f["id"] for f in fonctions["fonctions"]]
    cartes = []
    for d, dx in zip(res["dialogues"]["dialogues"], dialogues):
        for i, r in enumerate(d["redemittel"]):
            reg = r.get("registre") or d["registre"]
            if reg == "du+Sie":
                reg = "du" if TUTOIEMENT.search(GABARIT.sub(" ", r["t"])) else "Sie"
            c = {"id": "soins_rm_%02d_%d" % (d["numero"], i), "fonction": r.get("fonction", ""),
                 "groupe": r.get("groupe") or GROUPE_DIALOGUE.get(d["numero"], ""), "niveau": r.get("niveau") or d["niveau"],
                 "registre": reg}
            c.update(texte_de(r))
            c["situation"] = trad(r["situation"]) if r.get("situation") else trad(d["titre"])
            c.update({"dialogue": dx["id"], "apprenant": d["role"], "son": "%s/rm/%d" % (dx["id"], i),
                      "relire": c.pop("relire", "")})
            cartes.append(c)
    for ident, src in srm.items():
        if ident == "fonctions":
            continue
        groupe = src.get("groupe") or ident
        for i, r in enumerate(src.get("cartes", [])):
            if r.get("retire"):
                continue
            cid = "soins_rm_%s_%d" % (groupe, i)
            c = {"id": cid, "fonction": r.get("fonction", ""), "groupe": groupe, "niveau": r.get("niveau", ""),
                 "registre": r.get("registre", "")}
            c.update(texte_de(r))
            c["situation"] = trad(r["situation"]) if r.get("situation") else {}
            c.update({"dialogue": "", "apprenant": "", "son": cid, "relire": c.pop("relire", "")})
            cartes.append(c)
    rang_n = {"A2": 0, "B1": 1, "B2": 2, "C1": 3}
    cartes.sort(key=lambda c: (ordre_f.index(c["fonction"]) if c["fonction"] in ordre_f else 99,
                               rang_n.get(c["niveau"], 9), 0 if c["dialogue"] else 1))
    redemittel = {"_note": note % "tout le fichier (cartes-phrases, FORMAT-DONNEES.md 2 bis) : fonctions, groupes, cartes ; l'id d'une carte est stable, son « son » est sa clé de sons.json",
                  "langues": LANGUES,
                  "fonctions": [{"id": f["id"], "titre": trad(f["titre"]), "conseil": trad(f["conseil"])} for f in fonctions["fonctions"]],
                  "groupes": [{"id": g["id"], "titre": trad(g["titre"])} for g in fonctions["groupes"]],
                  "cartes": cartes}
    return {
        "redemittel": redemittel,
        "dialogues": {"_note": note % "source, registre, intro, et l'arbre des branches (debut, noeuds : le format des conversations jouées, visuel/CONVERSATIONS.md)",
                      "langues": LANGUES, "dialogues": dialogues},
        "grammaire": {"_note": note % "source, resume, tableau, piege, dialogues ; une question « choix » sans trou a de = « ___ » et une consigne",
                      "langues": LANGUES, "points": points},
        "ecrit": {"_note": note % "source, titre, consigne_de, rubrique (traduite), briques_groupes, corrige (traduit), corrige_b1, points, pieges, grille, et les grilles d'auto-évaluation (grilles)",
                  "langues": LANGUES, "sujets": sujets, "grilles": grilles},
    }


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
