# -*- coding: utf-8 -*-
"""La couche « Situation » parlée des scènes des Soins, TIRÉE DES DIALOGUES (mandat D, 15 nov. 2026).

    python pflege/outils/situations_scenes.py                       # écrit les couches SIT et leurs traductions
    python pflege/outils/situations_scenes.py --verifier            # montre seulement ce qui serait écrit
    python pflege/outils/situations_scenes.py --branche claude/pflege-bcc9b8   # dialogues lus dans une branche
    puis : python pflege/outils/construire_scenes.py --toutes

LA RÈGLE (pflege/PLAN.md, décisions de Jacques du 15 nov., § D)
    Une personne de l'image parle (patient, proche, collègue, médecin), on choisit la bonne réponse.
    AUCUNE PHRASE N'EST ÉCRITE ICI : la réplique entendue, la bonne réponse, les deux mauvaises et
    l'explication sont reprises MOT POUR MOT des dialogues (pflege/sources/dialogues/dNN-*.json),
    traductions comprises (pflege/sources/traductions/<langue>/dialogues/), pour que la scène et le
    dialogue ne divergent jamais. Un dialogue corrigé : relancer ce script, la scène suit.
      - la réplique : la dernière ligne « dit » du nœud, sinon la réponse (« puis ») qui y mène ;
      - c[0] : un choix juste du nœud ; c[1] : le choix « faux » du nœud ; c[2] : un autre choix
        « faux » d'un dialogue, faux ici aussi ;
      - n : l'aide (« aide ») du choix faux du nœud, ⚕️ si un des deux choix est à relire ;
      - sens : la traduction du choix juste.
    Les nombres : la forme « dit » du dialogue (en lettres) est prise quand elle existe, car aucun
    chiffre ne se dit à voix haute (pflege/FORMAT-DONNEES.md, règle 4) ; un chiffre restant arrête le script.
    Seuls s'écrivent ici le cadre de la question (« Herr Brandt fragt: „…“ », « Am Telefon … »),
    le titre de la couche et la zone de l'image où la personne se trouve.

    Les noms restent des gabarits dans les dialogues ({brandt}, {sommer:a}) : ils sont remplacés
    avec pflege/sources/noms.json (allemand, français) et traductions/<langue>/noms.json.

CE QUI MANQUE ENCORE (15 nov.)
    La salle de bain et la visite n'ont pas de dialogue à elles : la salle de bain reprend le
    pansement de d03 (après la toilette), la visite le refus de d04. Les dialogues 13 à 26 (session
    dialogues) viendront s'ajouter : d13 à l'admission, d14 à la salle de bain, d17 à la visite,
    d19 et d25 aux soins à domicile. Un nœud sans choix « faux » n'est pas repris (pas d'explication).
"""
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
PROTO = os.path.join(RACINE, "visuel", "prototype")
SOURCES = os.path.join(RACINE, "pflege", "sources")
LANGUES = ["en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]          # + fr = les 9

TITRE = {"fr": "Que répondez-vous ?", "en": "What do you answer?", "tr": "Ne cevap verirsiniz?",
         "uk": "Що ви відповісте?", "fa": "چه جواب می‌دهید؟", "pt": "O que responder?",
         "ar": "ما الردّ المناسب؟", "pl": "Co odpowiedzieć?", "ru": "Что ответить?"}


def Q(d, noeud, bon, faux, autre, cadre=None, r=None):
    """d, noeud : le nœud du dialogue ; bon, faux : les rangs des choix ; autre = (dialogue, nœud, rang)
    d'un autre choix faux ; cadre : la question, avec {nom} (qui parle, {nom_dat} au datif) et {t} (sa réplique)."""
    return {"d": d, "noeud": noeud, "bon": bon, "faux": faux, "autre": autre, "cadre": cadre, "r": r}


D01, D02, D03, D04, D05, D06 = ("d01-vorstellung", "d02-schmerzen", "d03-verbandswechsel",
                                "d04-ablehnung", "d05-angehoerige", "d06-uebergabe")
D07, D08, D09, D10, D11, D12 = ("d07-sbar", "d08-sturz", "d09-essen-anreichen",
                                "d10-medikamente", "d11-dienst-tauschen", "d12-nachts-demenz")

TELEFON = "Am Telefon fragt {nom}: „{t}“"
SCENES = {
    # 1. La chambre : Herr Brandt au lit (d01, d02). Les vues gardent chacune au moins une question.
    "soins-zimmer": {"niveau": "B1", "qui": {"brandt": "patient"}, "qs": [
        Q(D01, "neu", 0, 2, (D01, "tuer", 2)),
        Q(D01, "schmerz", 1, 2, (D02, "lage", 2)),
        Q(D02, "klingel", 0, 2, (D02, "skala", 2)),
        Q(D02, "seit", 0, 2, (D01, "schlaf", 2)),
    ]},
    "soins-zimmer-nachttisch": {"niveau": "B1", "qui": {"brandt": "patient"}, "qs": [
        Q(D02, "mittel", 1, 2, (D10, "frage", 2), r="wasserglas"),
    ]},
    "soins-zimmer-aufstehen": {"niveau": "B1", "qui": {"brandt": "patient"}, "qs": [
        Q(D01, "klingel", 1, 2, (D04, "angebot", 2), r="klingel",
          cadre="Sie helfen {nom_dat}, sich aufzusetzen. Er sagt: „{t}“"),
    ]},
    # 2. Le poste de soins : personne dans l'image, on parle au téléphone (d07, d11) ou devant le planning.
    "soins-stationszimmer": {"niveau": "B2", "qui": {"kraemer": "telefon", "hoffmann": "telefon",
                                                     "jonas": "dienstplan"}, "qs": [
        Q(D07, "melden", 1, 2, (D11, "anruf", 2), cadre="Nachts rufen Sie den Dienstarzt an. Er meldet sich: „{t}“"),
        Q(D07, "hintergrund", 1, 2, (D07, "einschaetzung", 2), cadre=TELEFON),
        Q(D07, "einschaetzung", 0, 2, (D07, "empfehlung", 2), cadre=TELEFON),
        Q(D07, "wiederholen", 0, 2, (D07, "melden", 2), cadre="Am Telefon sagt {nom}: „{t}“"),
        Q(D11, "fragen", 0, 2, (D11, "angebot", 2), cadre="Vor dem Dienstplan fragt {nom}: „{t}“"),
        Q(D11, "anruf", 0, 2, (D07, "wiederholen", 2),
          cadre="Sie sind krank und rufen früh morgens Ihre Stationsleitung an. Sie meldet sich: „{t}“"),
    ]},
    # 3. La salle de bain : Frau Lehmann, le pansement du pied changé après la toilette (d03).
    "soins-bad": {"niveau": "B1", "qui": {"lehmann": "patientin"}, "qs": [
        Q(D03, "ankuendigen", 0, 2, (D01, "messen", 2),
          cadre="Nach dem Waschen soll der Verband am Fuß gewechselt werden. {nom} fragt: „{t}“"),
        Q(D03, "warum", 0, 2, (D04, "verstehen", 2)),
        Q(D03, "ablauf", 0, 2, (D03, "ankuendigen", 2), r="handschuh"),
        Q(D03, "weh", 0, 2, (D01, "schmerz", 2)),
        Q(D03, "wunde", 1, 2, (D05, "sorgen", 2)),
    ]},
    # 4. La relève au lit : Jonas, devant Frau Lehmann et sa fille (d06).
    "soins-uebergabe": {"niveau": "B2", "qui": {"jonas": "pflegefachmann"}, "qs": [
        Q(D06, "start", 0, 2, (D06, "zucker", 2)),
        Q(D06, "zucker", 0, 2, (D06, "start", 2), r="fieberkurve"),
        Q(D06, "mobi", 1, 2, (D04, "erklaeren", 2), cadre="{nom} fragt nach Herrn Brandt, Zimmer zwölf: „{t}“"),
    ]},
    # 5. L'admission : Frau Krüger, la fille de Frau Lehmann (d05).
    "soins-aufnahme": {"niveau": "B2", "qui": {"lehmann_tochter": "tochter"}, "qs": [
        Q(D05, "sorgen", 0, 2, (D01, "schmerz", 2)),
        Q(D05, "befund", 0, 2, (D03, "wunde", 2)),
        Q(D05, "termin", 0, 2, (D05, "flur", 2)),
    ]},
    # 6. La visite : Herr Brandt refuse de se lever, devant la docteure Sommer (d04).
    "soins-visite": {"niveau": "B2", "qui": {"brandt": "patient"}, "qs": [
        Q(D04, "verstehen", 0, 2, (D04, "angebot", 2)),
        Q(D04, "erklaeren", 0, 2, (D03, "warum", 2)),
        Q(D04, "kompromiss", 0, 2, (D02, "lage", 2)),
        Q(D04, "entscheidung", 1, 2, (D01, "schmerz", 2)),
    ]},
    # 7. La maison de retraite : Frau Weber (d08), Herr Schulze (d09, d12).
    "soins-altenheim": {"niveau": "B1", "qui": {"weber": "frau-weber", "schulze": "herr-schulze"}, "qs": [
        Q(D08, "finden", 0, 2, (D08, "pruefen", 2),
          cadre="Sie finden {nom} neben ihrem Bett auf dem Boden. Sie sagt: „{t}“"),
        Q(D08, "hilfe", 0, 2, (D04, "angebot", 2), cadre="Sie fragen {nom}, ob sie mit dem Kopf aufgeschlagen ist. Sie sagt: „{t}“"),
        Q(D09, "heiss", 0, 2, (D09, "platz", 2), cadre="Beim Mittagessen sagt {nom}: „{t}“"),
        Q(D09, "verschluckt", 0, 2, (D09, "wahl", 2)),
        Q(D12, "flur", 0, 2, (D12, "nacht", 2), cadre="Nachts steht {nom} angezogen im Flur: „{t}“"),
        Q(D12, "begleiten", 0, 2, (D04, "verstehen", 2), cadre="Nachts im Flur sagt {nom}: „{t}“"),
    ]},
    # 8. Les soins à domicile : Frau Kowalski et sa nouvelle tablette (d10).
    "soins-ambulant": {"niveau": "B1", "qui": {"kowalski": "klientin"}, "qs": [
        Q(D10, "frage", 1, 2, (D02, "mittel", 2), r="dispenser"),
        Q(D10, "wann", 1, 2, (D01, "fruehstueck", 2)),
        Q(D10, "teilen", 0, 2, (D01, "schmerz", 2)),
    ]},
}


class Sources:
    """Les dialogues, leurs traductions et les noms : sur le disque, ou dans une branche (--branche)."""

    def __init__(self, branche=None):
        self.branche = branche
        self.cache = {}

    def lire(self, rel):
        if rel not in self.cache:
            if self.branche:
                r = subprocess.run(["git", "show", "%s:pflege/sources/%s" % (self.branche, rel)],
                                   cwd=RACINE, capture_output=True)
                if r.returncode:
                    sys.exit("introuvable dans %s : pflege/sources/%s" % (self.branche, rel))
                self.cache[rel] = json.loads(r.stdout.decode("utf-8"))
            else:
                chemin = os.path.join(SOURCES, rel)
                if not os.path.exists(chemin):
                    sys.exit("pflege/sources/%s absent : les dialogues sont sur la branche des dialogues "
                             "(relancer avec --branche claude/pflege-bcc9b8)" % rel)
                self.cache[rel] = json.load(io.open(chemin, encoding="utf-8"))
        return self.cache[rel]

    def dialogue(self, d):
        return self.lire("dialogues/%s.json" % d)

    def trad(self, d, langue):
        return self.lire("traductions/%s/dialogues/%s.json" % (langue, d))["cles"]

    def noms(self, langue):
        if langue in ("de", "fr"):
            return {k: v.get(langue, {}) for k, v in self.lire("noms.json")["personnes"].items()}
        return self.lire("traductions/%s/noms.json" % langue)["personnes"]


def remplacer(texte, noms, manque):
    """{brandt} → Herr Brandt, {brandt:dat} → Herrn Brandt (la forme courante si la forme manque)."""
    out, i = [], 0
    while True:
        a = texte.find("{", i)
        if a < 0:
            out.append(texte[i:])
            return "".join(out)
        b = texte.index("}", a)
        cle, _, forme = texte[a + 1:b].partition(":")
        formes = noms.get(cle) or {}
        v = formes.get(forme) or formes.get("")
        if not v:
            manque.append(texte[a:b + 1])
            v = texte[a:b + 1]
        out.append(texte[i:a])
        out.append(v)
        i = b + 1


def replique(dlg, noeud):
    """La ligne entendue : le dernier « dit » parlé du nœud, sinon la réponse qui mène au nœud."""
    nd = dlg["noeuds"][noeud]
    lignes = [l for l in nd.get("dit", []) if l.get("qui")]
    if lignes:
        return lignes[-1]
    for autre in dlg["noeuds"].values():
        for c in autre.get("choix", []):
            if c.get("va") == noeud and not c.get("faux"):
                p = [l for l in c.get("puis", []) if l.get("qui")]
                if p:
                    return p[-1]
    sys.exit("%s/%s : aucune réplique ne mène à ce nœud" % (dlg["id"], noeud))


def construire(src):
    """Pour chaque scène : la couche SIT (allemand, français) et, par langue, les traductions."""
    noms = {l: src.noms(l) for l in ["de", "fr"] + LANGUES}
    manque, fautes, sortie = [], [], {}
    for scene, conf in SCENES.items():
        qs, trads = [], {l: {"questions": {}, "sens": {}} for l in LANGUES}
        for item in conf["qs"]:
            dlg = src.dialogue(item["d"])
            nd = dlg["noeuds"][item["noeud"]]
            bon, faux = nd["choix"][item["bon"]], nd["choix"][item["faux"]]
            if bon.get("faux") or not faux.get("faux") or not faux.get("aide"):
                fautes.append("%s/%s : choix %d juste et %d faux avec son aide attendus"
                              % (item["d"], item["noeud"], item["bon"], item["faux"]))
                continue
            ad, an, ak = item["autre"]
            autre = src.dialogue(ad)["noeuds"][an]["choix"][ak]
            if not autre.get("faux"):
                fautes.append("%s/%s : le choix %d n'est pas « faux »" % (ad, an, ak))
            ligne = replique(dlg, item["noeud"])
            zone = conf["qui"].get(ligne["qui"])
            if not zone:
                fautes.append("%s/%s : %s parle, sans zone dans %s" % (item["d"], item["noeud"], ligne["qui"], scene))
            de = lambda t: remplacer(t, noms["de"], manque)
            parle = de(ligne.get("dit") or ligne["t"])     # « dit » : les nombres en lettres (contrat, règle 4)
            cadre = item["cadre"] or ("{nom} fragt: „{t}“" if "?" in parle else "{nom} sagt: „{t}“")
            formes = noms["de"].get(ligne["qui"]) or {}
            nom = formes.get("") or ligne["qui"]
            c = [de(x.get("dit") or x["t"]) for x in (bon, faux, autre)]
            if any(ch.isdigit() for x in c + [parle, cadre] for ch in x):
                fautes.append("%s/%s : un chiffre dans l'allemand dit (règle 4)" % (item["d"], item["noeud"]))
            if len(set(c)) != 3:
                fautes.append("%s/%s : choix en double" % (item["d"], item["noeud"]))
            relire = bon.get("relire") or faux.get("relire")
            q = {"q": cadre.format(nom=nom, nom_dat=formes.get("dat") or nom, t=parle), "c": c, "f": zone, "type": "situation", "phrase": c[0],
                 "sens": remplacer(bon["fr"], noms["fr"], manque),
                 "n": remplacer(faux["aide"]["fr"], noms["fr"], manque) + (" ⚕️" if relire else ""),
                 "source": "%s/%s" % (item["d"], item["noeud"])}
            if item["r"]:
                q["r"] = item["r"]
            qs.append(q)
            base = "noeuds.%s.choix." % item["noeud"]
            for l in LANGUES:
                t = src.trad(item["d"], l)
                tb = (t.get(base + str(item["bon"])) or {}).get(l)
                ta = (t.get(base + "%d.aide" % item["faux"]) or {}).get(l)
                if not tb or not ta:
                    fautes.append("%s : traduction absente de %s/%s" % (l, item["d"], item["noeud"]))
                    continue
                cle = "SIT | " + q["phrase"]
                trads[l]["sens"][cle] = {"fr": q["sens"], "trad": remplacer(tb, noms[l], manque)}
                trads[l]["questions"][cle] = {"fr": q["n"],
                                              "trad": remplacer(ta, noms[l], manque) + (" ⚕️" if relire else "")}
        sortie[scene] = {"couche": {"titre": TITRE["fr"], "niveau": conf["niveau"], "qs": qs}, "trads": trads}
    if manque:
        fautes.append("noms sans forme : %s" % ", ".join(sorted(set(manque))))
    return sortie, fautes


def ecrire_json(chemin, d):
    io.open(chemin, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n")


def remplacer_sit(texte, sit):
    """Remplace le seul bloc "SIT" d'un points.json, dans la mise en forme du fichier : les scènes
    sont écrites à la main, une zone par ligne pour certaines ; tout réécrire noierait le diff."""
    j = json.dumps
    a = texte.index('"SIT":', texte.index('"couches"'))
    debut = a + len('"SIT":')
    while texte[debut] in " \t":
        debut += 1
    _, fin = json.JSONDecoder().raw_decode(texte, debut)
    nl = "\r\n" if "\r\n" in texte else "\n"
    if texte[debut:fin].startswith('{"titre"'):                      # forme compacte, une question par bloc
        lignes = []
        for q in sit["qs"]:
            tete = ", ".join('"%s": %s' % (k, j(q[k], ensure_ascii=False)) for k in ("q", "c", "f", "type") if k in q)
            mil = ", ".join('"%s": %s' % (k, j(q[k], ensure_ascii=False)) for k in ("phrase", "sens"))
            bas = ", ".join('"%s": %s' % (k, j(q[k], ensure_ascii=False)) for k in ("n", "source", "r") if k in q)
            lignes.append("   {%s,%s    %s,%s    %s}" % (tete, nl, mil, nl, bas))
        bloc = '{"titre": %s, "niveau": %s, "qs": [%s%s%s  ]}' % (
            j(sit["titre"], ensure_ascii=False), j(sit["niveau"]), nl, ("," + nl).join(lignes), nl)
    else:                                                            # indentation d'un espace, au 3e niveau
        bloc = j(sit, ensure_ascii=False, indent=1).replace("\n", nl + "  ")
    return texte[:debut] + bloc + texte[fin:]


def appliquer(sortie):
    for scene, s in sortie.items():
        chemin = os.path.join(PROTO, scene + ".points.json")
        texte = io.open(chemin, encoding="utf-8", newline="").read()
        if '"SIT":' in texte:
            texte = remplacer_sit(texte, s["couche"])
            json.loads(texte)                                        # le fichier reste du JSON
            io.open(chemin, "w", encoding="utf-8", newline="").write(texte)
        else:
            pts = json.loads(texte)
            pts.setdefault("couches", {})["SIT"] = s["couche"]       # SIT reste la dernière couche
            ecrire_json(chemin, pts)
        for l, groupes in s["trads"].items():
            tc = os.path.join(PROTO, "traductions", "%s.%s.json" % (scene, l))
            tr = json.load(io.open(tc, encoding="utf-8"))
            tr.setdefault("couches", {})["SIT"] = {"fr": TITRE["fr"], "trad": TITRE[l]}
            for g in ("questions", "sens"):
                garde = {k: v for k, v in tr.get(g, {}).items() if not k.startswith("SIT | ")}
                garde.update(groupes[g])
                tr[g] = garde
            ecrire_json(tc, tr)


def main():
    branche = sys.argv[sys.argv.index("--branche") + 1] if "--branche" in sys.argv else None
    sortie, fautes = construire(Sources(branche))
    for scene, s in sortie.items():
        print("== %s : %d question(s)" % (scene, len(s["couche"]["qs"])))
        if "--verifier" in sys.argv:
            for q in s["couche"]["qs"]:
                print("   [%s] %s\n      + %s\n      - %s\n      - %s" % (q["source"], q["q"], *q["c"]))
    for f in fautes:
        print("  ⚠ %s" % f)
    if fautes:
        sys.exit("%d faute(s) : rien n'est écrit" % len(fautes))
    if "--verifier" not in sys.argv:
        appliquer(sortie)
        print("écrit : couches SIT et traductions (%d langues)" % len(LANGUES))


if __name__ == "__main__":
    main()
