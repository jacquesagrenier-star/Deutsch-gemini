# -*- coding: utf-8 -*-
"""Les couches A2 des scenes en portugais (« Onde está? », les prepositions
de lieu), tirees des FAITS de l'image allemande : la couche A2 allemande dit
ou est chaque objet (« Wo steht der Topf? → neben der Pfanne ») ; on en garde
le fait, et on l'ecrit en portugais avec les mots de la table du socle
(portugais/outils/scenes.py, MOTS).

    python portugais/outils/couches_a2.py [--mots CHEMIN/scenes.py] [--ecraser]

OUTIL A USAGE UNIQUE (29 oct. 2026). Il ecrit la couche « A2 » de chaque
portugais/scenes/<scene>.json (et la cree au besoin) ; les couches B1-C1 de ces
fichiers sont ecrites a la main et il n'y touche pas. Ensuite, les fichiers
sont LA SOURCE : on les corrige a la main. Un fait qu'il ne sait pas ecrire
(adjectif, sujet a deux mots...) est saute et liste.
"""
import glob, importlib.util, io, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype")
SORTIE = os.path.join(RACINE, "portugais", "scenes")
sys.path.insert(0, ICI)
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import niveaux

# preposition allemande -> (preposition portugaise, ce qu'elle contracte : de, em, a, ou rien)
PREP = {
    "neben": ("ao lado de", "de"), "auf": ("em cima de", "de"), "über": ("por cima de", "de"),
    "unter": ("debaixo de", "de"), "vor": ("à frente de", "de"), "hinter": ("atrás de", "de"),
    "in": ("em", "em"), "bei": ("ao pé de", "de"), "gegenüber": ("em frente de", "de"),
}
CONTR = {
    "de": {"o": "do", "a": "da", "os": "dos", "as": "das"},
    "em": {"o": "no", "a": "na", "os": "nos", "as": "nas"},
    "a": {"o": "ao", "a": "à", "os": "aos", "as": "às"},
}
# « an » : accroche (na parede), a table ou a la fenetre (à mesa, à janela), sinon pres de.
AN_EM = {"Wand", "Tür", "Decke", "Haken", "Kühlschrank", "Baum", "Tafel", "Regal", "Wäscheleine",
         "Kleiderständer", "Stange", "Garderobe", "Pinnwand", "Spiegel", "Schrank", "Ast", "Zaun"}
AN_EM |= {"Turm", "Haus", "Haltestelle", "Lampe", "Kasse", "Mast", "Laterne", "Gebäude", "Säule"}
AN_A = {"Tisch", "Fenster", "Schreibtisch", "Theke", "Tresen"}
# « auf » : em cima de seulement sur un meuble ou un objet (le dessus) ; sinon em
# (no chão, no sofá, na rua, no joelho).
AUF_DESSUS = {"Tisch", "Schrank", "Kühlschrank", "Schreibtisch", "Waschmaschine", "Schalter", "Theke", "Kommode",
              "Klavier", "Fernseher", "Ofen", "Herd", "Dach", "Mauer", "Kiste", "Tresen", "Nachttisch", "Couchtisch",
              "Regal", "Waage", "Koffer", "Karton", "Hocker", "Trockner", "Stapel"}
PRENOMS = {"Mark": ("o", "Mark"), "Anna": ("a", "Anna"), "Lena": ("a", "Lena"), "Tom": ("o", "Tom"),
           "Max": ("o", "Max"), "Oma": ("a", "avó"), "Opa": ("o", "avô")}
VERBE_ACCROCHE = re.compile(r"^Wo (hängt|hängen)\b")
ARTICLES_DE = {"der", "die", "das", "dem", "den", "des", "einem", "einer", "einen", "ein", "eine"}
CONTRACTIONS_DE = {"im": ("in", "dem"), "ins": ("in", "das"), "am": ("an", "dem"), "ans": ("an", "das"),
                   "beim": ("bei", "dem"), "vom": ("von", "dem"), "zum": ("zu", "dem"), "zur": ("zu", "der")}
PLURIEL_DE = re.compile(r"^Wo (stehen|liegen|sind|hängen|sitzen|wachsen)\b")


def charger_mots(chemin):
    spec = importlib.util.spec_from_file_location("scenes_socle", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.MOTS


class Echec(Exception):
    pass


def nom_pt(mots, nom_de, pluriel=False):
    """« Pfanne » -> ("a", "frigideira") ; au pluriel : ("as", "frigideiras")."""
    for essai in (nom_de, nom_de[:-1], nom_de[:-2]):
        v = mots.get(essai)
        if v:
            break
    else:
        raise Echec("mot inconnu : " + nom_de)
    tete, _, drap = v.partition("|")
    art, _, mot = tete.partition(" ")
    if art not in ("o", "a", "os", "as"):
        raise Echec("sans article : " + v)
    est_pluriel = pluriel or (essai != nom_de and art in ("o", "a") and nom_de.endswith(("n", "e", "s")) and False)
    if est_pluriel and art in ("o", "a"):
        pl = dict(x.split("=", 1) for x in drap.split("|") if "=" in x).get("pl") if drap else None
        mot, art = pl or niveaux.pluriel(mot), art + "s"
    return art, mot


def lieu_pt(mots, groupe, accroche=False):
    """« neben der Pfanne » -> ("ao lado da frigideira", note)."""
    t = groupe.split()
    if not t:
        raise Echec("vide")
    p = t[0]
    if p in CONTRACTIONS_DE:
        p, art_de = CONTRACTIONS_DE[p]
        t = [p, art_de] + t[1:]
    if p == "zwischen":
        reste = " ".join(t[1:])
        a, sep, b = reste.partition(" und ")
        if not sep:
            raise Echec("zwischen sans und")
        g1, g2 = [x.split() for x in (a, b)]
        if len(g1) != 2 or len(g2) != 2 or g1[0] not in ARTICLES_DE or g2[0] not in ARTICLES_DE:
            raise Echec("zwischen complexe : " + groupe)
        (a1, m1), (a2, m2) = nom_pt(mots, g1[1]), nom_pt(mots, g2[1])
        return "entre %s %s e %s %s" % (a1, m1, a2, m2), "<b>entre</b> … <b>e</b> … = entre … et …"
    if len(t) != 3 or t[1] not in ARTICLES_DE:
        raise Echec("groupe : " + groupe)
    nom_de = t[2]
    pluriel = t[1] == "den" and nom_de.endswith("n") and p != "in" or (t[1] == "den" and nom_de.endswith(("en", "ern")))
    indef = t[1].startswith("ein")
    if p == "an":
        prep, c = ("em", "em") if (nom_de in AN_EM or accroche) else (("a", "a") if nom_de in AN_A else ("junto de", "de"))
    elif p == "auf":
        prep, c = ("em cima de", "de") if nom_de in AUF_DESSUS else ("em", "em")
    elif p in PREP:
        prep, c = PREP[p]
    else:
        raise Echec("preposition : " + p)
    if nom_de == "Decke" and p == "an":
        return "no teto", "em + o teto = <b>no</b> teto."
    art, mot = nom_pt(mots, nom_de, pluriel)
    if indef:
        un = {"o": "um", "a": "uma"}.get(art)
        if not un:
            raise Echec("indefini pluriel")
        if c == "em":
            g = ("num " if art == "o" else "numa ") + mot
            return g, "em + %s = <b>%s</b>." % (un, g.split()[0])
        if c == "de":
            return "%s %s %s" % (prep, un, mot), "<b>%s</b> + %s %s." % (prep, un, mot)
        return "%s %s %s" % (prep, un, mot), ""
    contracte = CONTR[c][art]
    base = prep[:-len(c)].strip() if prep.endswith(" " + c) or prep == c else prep
    g = ("%s %s %s" % (base, contracte, mot)).strip()
    note = "<b>%s</b> + %s %s = <b>%s %s</b> %s." % (prep, art, mot, base, contracte, mot) if base else \
           "<b>%s</b> + %s = <b>%s</b> : %s." % (prep, art, contracte, g)
    note = note.replace("  ", " ").replace("<b> ", "<b>")
    return g, note


SENS_PREP = {"ao lado de": "à côté de", "em cima de": "sur", "por cima de": "au-dessus de", "debaixo de": "sous",
             "à frente de": "devant", "atrás de": "derrière", "em": "dans, sur (contact)", "ao pé de": "près de, au pied de",
             "em frente de": "en face de", "junto de": "près de, contre", "a": "à (à table, à la fenêtre)"}


def question(mots, q, points):
    f = q.get("f")
    pt_f = points.get(f)
    if not pt_f:
        raise Echec("point inconnu : %s" % f)
    pluriel = bool(PLURIEL_DE.match(q["q"]))
    sujet = re.match(r"^Wo \w+ (\w+)\?$", q["q"])
    if sujet and sujet.group(1) in PRENOMS:
        art, mot = PRENOMS[sujet.group(1)]
    else:
        art, mot = nom_pt(mots, pt_f, pluriel)
    verbe = "estão" if art in ("os", "as") else "está"
    accroche = bool(VERBE_ACCROCHE.match(q["q"]))
    choix, note = [], ""
    for i, ch in enumerate(q["c"]):
        g, n = lieu_pt(mots, ch, accroche)
        choix.append(g)
        if i == 0:
            note = n
    if len(set(choix)) != len(choix):
        raise Echec("choix en double")
    prep_sens = next((k for k in sorted(SENS_PREP, key=len, reverse=True) if choix[0].startswith(k.split()[0])), None)
    if prep_sens and prep_sens in ("ao lado de", "em cima de", "por cima de", "debaixo de", "à frente de", "atrás de",
                                   "ao pé de", "em frente de", "junto de"):
        note = "<b>%s</b> = %s. %s" % (prep_sens, SENS_PREP[prep_sens], note)
    return {"q": "Onde %s %s %s?" % (verbe, art, mot), "c": choix, "f": f, "r": q.get("r"),
            "phrase": "%s %s %s %s." % (art.capitalize(), mot, verbe, choix[0]), "sens": q.get("sens", ""),
            "n": note, "_de": "%s → %s" % (q["q"], q["c"][0])}


def main():
    chemin = os.path.join(ICI, "scenes.py")
    if "--mots" in sys.argv:
        chemin = sys.argv[sys.argv.index("--mots") + 1]
    mots = charger_mots(chemin)
    os.makedirs(SORTIE, exist_ok=True)
    total, echecs = 0, []
    for f in sorted(glob.glob(os.path.join(PROTO, "*.points.json"))):
        nom = os.path.basename(f)[:-len(".points.json")]
        d = json.load(io.open(f, encoding="utf-8"))
        a2 = d.get("couches", {}).get("A2")
        if not a2:
            continue
        points = {p["id"]: p.get("mot") for p in d.get("points", [])}
        qs = []
        for q in a2.get("qs", []):
            try:
                qs.append(question(mots, q, points))
            except Echec as e:
                echecs.append("%-22s %-40s %s" % (nom, q["q"][:40], e))
        sortie = os.path.join(SORTIE, nom + ".json")
        doc = {"_lisez_moi": ("Couches A2-C1 de la scene « %s » en portugais du Portugal, ECRITES pour le portugais sur les "
                              "faits de l'image (memes zones f et reperes r que l'allemand). SOURCE : on corrige ici. "
                              "La couche A2 a ete tiree des faits allemands par portugais/outils/couches_a2.py (29 oct. 2026), "
                              "les autres ecrites a la main. Le champ _de rappelle le fait allemand ; il n'est pas copie dans la scene." % nom),
               "couches": {}}
        if os.path.exists(sortie):
            doc = json.load(io.open(sortie, encoding="utf-8"))
            if "A2" in doc.get("couches", {}) and "--ecraser" not in sys.argv:
                print("  %s : couche A2 deja la (--ecraser pour la refaire)" % nom)
                continue
        if qs:
            doc["couches"]["A2"] = {"titre": "Onde está? — les prépositions de lieu", "qs": qs}
            ordre = {k: doc["couches"][k] for k in ("A2", "B1", "B2", "C1") if k in doc["couches"]}
            doc["couches"] = ordre
            with io.open(sortie, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(doc, fh, ensure_ascii=False, indent=1)
                fh.write("\n")
        total += len(qs)
    print("Couches A2 : %d questions ecrites, %d faits sautes." % (total, len(echecs)))
    for e in echecs:
        print("  saute :", e)


if __name__ == "__main__":
    main()
