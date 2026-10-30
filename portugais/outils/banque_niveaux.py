# -*- coding: utf-8 -*-
"""La banque de phrases portugaises de l'A2-C1 : toutes les paires (portugais,
francais) de nos corpus allemand et espagnol, CONVERTIES au portugais d'Europe
(variante_niveaux.py). Une phrase que la conversion ne sait pas rendre
proprement n'entre pas dans la banque.

    python portugais/outils/banque_niveaux.py            (bilan)
    python portugais/outils/banque_niveaux.py --rejets   (les phrases refusees)
    python portugais/outils/banque_niveaux.py --echantillon 60
"""
import io, json, os, random, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
import variante_niveaux as V

NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]


def charger(p):
    with io.open(os.path.join(RACINE, p), encoding="utf-8") as f:
        return json.load(f)


def tete_pt(pt):
    """« o favor » -> favor ; « aproximar, passar » -> aproximar."""
    pt = re.sub(r"\(.*?\)|\[.*?\]", "", pt or "")
    p = re.split(r"[,;/]", pt)[0].strip().strip(".!?")
    p = re.sub(r"^(o|a|os|as)\s+", "", p)
    return re.sub(r"\s+", " ", p).strip().lower()


# Les villes et pays de nos corpus -> le Portugal, dans les deux langues.
LIEUX = [("Berlim", "Lisboa"), ("Berlin", "Lisbonne"), ("Madrid", "Lisboa"), ("Madri", "Lisboa"),
         ("Munique", "Porto"), ("Munich", "Porto"), ("Hamburgo", "Porto"), ("Hambourg", "Porto"),
         ("Barcelona", "Porto"), ("Barcelone", "Porto"), ("Sevilha", "Coimbra"), ("Séville", "Coimbra"),
         ("Colônia", "Braga"), ("Cologne", "Braga"), ("Viena", "Évora"), ("Vienne", "Évora"),
         ("Frankfurt", "Faro"), ("Francfort", "Faro"), ("Valência", "Aveiro"), ("Valence", "Aveiro")]


def portugaliser(pt, fr):
    for a, b in LIEUX:
        pt = V.remplacer_mots(pt, [(a, b)])
        fr = V.remplacer_mots(fr, [(a, b)])
    return pt, fr


def banque(rejets=None):
    paires = []

    def ajouter(e, niveau, classe, cle_pt="exemple_pt", cle_fr="exemple_fr"):
        if not isinstance(e, dict):
            return
        pt, fr = e.get(cle_pt), e.get(cle_fr)
        if not (pt and fr):
            return
        conv, raison = V.phrase_europeenne(pt.strip())
        if conv is None:
            if rejets is not None:
                rejets.append((raison, pt))
            return
        conv, fr = portugaliser(conv, fr.strip())
        conv = V.accorder_au_francais(conv, fr)
        paires.append({"pt": conv, "fr": fr, "tete": tete_pt(e.get("traduction_pt")),
                       "niveau": niveau, "classe": classe,
                       "europe": bool(re.search(r"\b(alemã|alemão|alemães|Alemanha|Espanha|espanhol|espanhola)\b", conv))})

    for f in ("themes.json", "espanol/datos/temas.json"):
        for t in charger(f)["themes"]:
            for m in t.get("mots", []):
                ajouter(m, (t.get("niveau") or "C1").upper(), "nom")
    classes = {"verbe": "verbe", "verbos": "verbe", "adjectif": "adj", "adjetivos": "adj",
               "adverbe": "adv", "adverbios": "adv", "redewendung": "expr", "expresiones": "expr"}
    infs = []
    for f in ("verbe.json", "adjectif.json", "adverbe.json", "redewendung.json",
              "espanol/datos/verbos.json", "espanol/datos/adjetivos.json",
              "espanol/datos/adverbios.json", "espanol/datos/expresiones.json"):
        d = charger(f)
        classe = classes[os.path.basename(f)[:-5]]
        for n, liste in d.items():
            if not isinstance(liste, list):
                continue
            for e in liste:
                niv = n.upper() if n.upper() in NIVEAUX else "C1"
                if classe == "verbe" and isinstance(e, dict):
                    infs.append(tete_pt(e.get("traduction_pt")))
                ajouter(e, niv, classe)
                # Les phrases des temps espagnols et allemands : autant de phrases de plus.
                for k in ("preterito", "imperfecto", "subjuntivo", "perfecto", "futuro", "condicional"):
                    ajouter(e, niv, classe, "exemple_%s_pt" % k, "exemple_%s_fr" % k)
                for k in ("perfekt", "praeteritum", "konjunktiv2"):
                    ajouter(e, niv, classe, k + "_pt", k + "_fr")
    vus, propres = set(), []
    for p in paires:
        if p["pt"] in vus:
            continue
        vus.add(p["pt"])
        propres.append(p)
    return propres, infs


def preparer():
    """Charge les infinitifs connus (pour la mesoclise) PUIS construit la banque."""
    _, infs = banque([])  # premier passage : les infinitifs
    V.connaitre_infinitifs(infs)
    return banque()[0]


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    _, infs = banque([])
    V.connaitre_infinitifs(infs)
    rej = []
    b, _ = banque(rej)
    print("Banque : %d paires gardees, %d refusees." % (len(b), len(rej)))
    from collections import Counter
    c = Counter()
    for r, _ in rej:
        for x in r.split(", "):
            c[x] += 1
    for k, n in c.most_common(25):
        print("  %5d  %s" % (n, k))
    if "--rejets" in sys.argv:
        for r, p in rej:
            print("%-40s %s" % (r[:40], p))
    if "--echantillon" in sys.argv:
        n = int(sys.argv[sys.argv.index("--echantillon") + 1])
        random.seed(7)
        for p in random.sample(b, n):
            print(p["niveau"], p["classe"], "|", p["pt"], "|", p["fr"])
