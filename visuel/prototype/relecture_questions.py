# -*- coding: utf-8 -*-
"""Relecture croisee des questions A2-C1 des scenes, par d'autres IA, a l'aveugle.

    python visuel/prototype/relecture_questions.py preparer
        -> reports/relecture-scenes/lot-NN.md (a coller tel quel dans Gemini
           puis dans ChatGPT, chacune dans sa propre conversation) + cle.json

    python visuel/prototype/relecture_questions.py importer gemini REPONSE.txt
    python visuel/prototype/relecture_questions.py comparer

Les questions sont des BROUILLONS ecrits le 6 et le 9 oct. 2026 : de
l'allemand que des apprenants vont retenir. Methode de relecture croisee
(memoire « relecture-croisee-methode ») : chaque relecteur voit la question,
la reponse visee, la phrase complete et l'explication -- jamais l'avis d'un
autre relecteur. On ne corrige ensuite que ce qui se verifie.
"""
import glob
import io
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
DOSSIER = os.path.join(RACINE, "reports", "relecture-scenes")
CLE = os.path.join(DOSSIER, "cle.json")
REPONSES = os.path.join(DOSSIER, "reponses")
TAILLE_LOT = 55
VERDICTS = ["BON", "A_AMELIORER", "A_REMPLACER", "FAUX"]

CONSIGNE = """Tu relis des exercices d'allemand pour des francophones (niveaux CECR A2 a C1). Chaque exercice se joue sur une PHOTO que tu ne vois pas : une salle de classe, un cabinet medical, un marche.

IMPORTANT : les objets, les personnes et leurs positions ont DEJA ete verifies sur la photo. La description de la scene ci-dessous est un simple resume et ne cite pas tout : un objet absent du resume EST bien sur la photo. Ne signale donc jamais « absent de la scene » ni « position non precisee ». Les phrases a hypotheses (muss, koennte, duerfte, soll) sont guidees par leur amorce (« Ich bin mir fast sicher », « Vielleicht », « Wahrscheinlich », « Man sagt ») : juge si l'amorce impose bien la reponse, pas si la photo la prouve. Juge la LANGUE.

Pour chaque exercice tu recois : la question, les choix (la reponse visee est marquee *), la phrase complete qui sera lue a voix haute, et l'explication montree a l'eleve (en francais).

Verifie :
1. La reponse visee est-elle correcte ?
2. Un AUTRE choix serait-il aussi correct (ambiguite) ?
3. La phrase complete est-elle de l'allemand correct et naturel ?
4. L'explication est-elle juste, et sans erreur de grammaire ou de terminologie ?
5. Le niveau indique est-il raisonnable ?

Reponds UNIQUEMENT par une ligne par exercice, dans l'ordre, sans en sauter :
CODE | VERDICT | remarque
VERDICT = BON (rien a changer), A_AMELIORER (juste mais maladroit ou imprecis), A_REMPLACER (ambigu ou mal concu), FAUX (erreur d'allemand ou reponse fausse).
La remarque est vide pour BON ; sinon une phrase en francais qui dit le probleme et propose la correction.
Si tu dois t'arreter avant la fin, ecris en derniere ligne : ARRET APRES CODE.

"""

SCENES = {
    "klassenzimmer": "un cours d'espagnol du soir a Berlin : le prof devant le tableau, Mark et Anna assis cote a cote, d'autres eleves, un manteau et une veste aux crochets de la porte",
    "arztpraxis": "Mark assis sur la table d'examen, pansement au genou, la medecin assise a cote de lui avec une bande ; un bureau, une affiche anatomique, un ballon sur un sac de sport",
    "untersuchung": "Mark debout en boxer, de face ; sa medecin l'ausculte au stethoscope ; un pese-personne avec toise contre le mur",
    "untersuchung-dos": "la meme scene, Mark de dos : la medecin ausculte son dos ; ses paumes sont tournees vers l'arriere",
    "markt-obst-heimisch": "un etal de fruits d'ici au marche (framboises, myrtilles, raisins, prunes, rhubarbe, noix, poires, groseilles, groseilles a maquereau, cerises, mures, abricots, fraises, peches, pommes) ; Anna, de dos, prend une pomme",
    "markt-obst-sued": "un etal de fruits du Sud (pasteques, ananas, noix de coco, melons, oranges, avocats, papayes, citrons, kiwis, mandarines, figues, citrons verts, pamplemousses, mangues, bananes, grenades) ; Anna prend des bananes",
    "markt-gemuese-wurzel": "un etal de legumes (betteraves, choux-fleurs, celeri, pommes de terre, choux-raves, oignons, choux, poireaux, carottes, choux de Bruxelles, fenouil, brocolis, ail, radis, patates douces) ; Anna prend une botte de radis",
    "markt-gemuese-frucht": "un etal de legumes (petits pois, laitues, asperges, citrouilles, poivrons, mais, champignons, haricots, blettes, artichauts, aubergines, concombres, courgettes, tomates, epinards) ; Anna prend des tomates",
}


def nettoyer(html):
    return re.sub(r"<[^>]+>", "", html or "").replace("&nbsp;", " ").strip()


def preparer():
    items = []
    for f in sorted(glob.glob(os.path.join(ICI, "*.points.json"))):
        nom = os.path.basename(f)[:-len(".points.json")]
        d = json.load(io.open(f, encoding="utf-8"))
        for niv, couche in (d.get("couches") or {}).items():
            for k, q in enumerate(couche.get("qs") or []):
                items.append({"scene": nom, "niveau": niv, "rang": k, "q": q})
    os.makedirs(DOSSIER, exist_ok=True)
    cle, n_lot = {}, 0
    for debut in range(0, len(items), TAILLE_LOT):
        n_lot += 1
        lot = items[debut:debut + TAILLE_LOT]
        scenes = sorted({it["scene"] for it in lot})
        lignes = [CONSIGNE, "Les scenes de ce lot :"]
        lignes += ["- %s : %s" % (s, SCENES.get(s, "")) for s in scenes]
        lignes.append("")
        for k, it in enumerate(lot, debut + 1):
            code = "Q%03d" % k
            q = it["q"]
            choix = " / ".join(("*" if j == 0 else "") + c for j, c in enumerate(q["c"]))
            lignes.append("%s [%s, %s]\n  Question : %s\n  Choix : %s\n  Phrase : %s\n  Explication : %s\n"
                          % (code, it["scene"], it["niveau"], q["q"], choix, q["phrase"], nettoyer(q["n"])))
            cle[code] = {"scene": it["scene"], "niveau": it["niveau"], "rang": it["rang"],
                         "q": q["q"], "phrase": q["phrase"], "lot": n_lot}
        io.open(os.path.join(DOSSIER, "lot-%02d.md" % n_lot), "w", encoding="utf-8").write("\n".join(lignes))
    io.open(CLE, "w", encoding="utf-8").write(json.dumps(cle, ensure_ascii=False, indent=1))
    print("%d questions, %d lots dans %s" % (len(items), n_lot, DOSSIER))


LIGNE = re.compile(r"^\W*(Q\d{3})\s*\|\s*([A-Z_ÉÈ]+)\s*(?:\|\s*(.*))?$")


def importer(modele, fichier):
    cle = json.load(io.open(CLE, encoding="utf-8"))
    os.makedirs(REPONSES, exist_ok=True)
    chemin = os.path.join(REPONSES, modele + ".json")
    deja = json.load(io.open(chemin, encoding="utf-8")) if os.path.exists(chemin) else {}
    lus, refus = {}, []
    for ligne in io.open(fichier, encoding="utf-8").read().splitlines():
        m = LIGNE.match(ligne.strip().replace("｜", "|"))
        if not m:
            continue
        code, verdict, rem = m.groups()
        verdict = verdict.replace("É", "E")
        if code not in cle or verdict not in VERDICTS:
            refus.append(ligne.strip())
            continue
        lus[code] = {"verdict": verdict, "remarque": (rem or "").strip()}
    lots = {cle[c]["lot"] for c in lus}
    manquants = sorted(c for c, v in cle.items() if v["lot"] in lots and c not in lus)
    deja.update(lus)
    io.open(chemin, "w", encoding="utf-8").write(json.dumps(deja, ensure_ascii=False, indent=1))
    print("%s : %d verdicts lus (lots %s), %d au total" % (modele, len(lus), sorted(lots), len(deja)))
    if manquants:
        print("  MANQUANTS, a redemander : " + ", ".join(manquants))
    if refus:
        print("  illisibles : %d" % len(refus))


def comparer():
    cle = json.load(io.open(CLE, encoding="utf-8"))
    juges = {os.path.basename(f)[:-5]: json.load(io.open(f, encoding="utf-8"))
             for f in sorted(glob.glob(os.path.join(REPONSES, "*.json")))}
    lignes = ["# Questions des scenes : ce que les relecteurs signalent", "",
              "Relecteurs : %s. Seules les questions qu'au moins un relecteur n'a pas jugees BON." % ", ".join(juges), ""]
    n = 0
    for code, it in cle.items():
        avis = {j: r[code] for j, r in juges.items() if code in r}
        if not avis or all(a["verdict"] == "BON" for a in avis.values()):
            continue
        n += 1
        lignes.append("## %s · %s · %s" % (code, it["scene"], it["niveau"]))
        lignes.append("- Question : %s" % it["q"])
        lignes.append("- Phrase : %s" % it["phrase"])
        for j, a in avis.items():
            lignes.append("- **%s** : %s — %s" % (j, a["verdict"], a["remarque"]))
        lignes.append("")
    sortie = os.path.join(DOSSIER, "a-trancher.md")
    io.open(sortie, "w", encoding="utf-8").write("\n".join(lignes))
    print("%d questions signalees -> %s" % (n, sortie))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    if a[:1] == ["preparer"]:
        preparer()
    elif a[:1] == ["importer"] and len(a) == 3:
        importer(a[1], a[2])
    elif a[:1] == ["comparer"]:
        comparer()
    else:
        sys.exit(__doc__)
