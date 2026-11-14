"""Le controle de l'examen blanc telc Deutsch B1·B2 Pflege (visuel/prototype/telc/pflege/).

    python tests/pflege_examen.py            # tout : 59 questions, ecrit, oral, 9 langues, bareme
    python tests/pflege_examen.py --partiel  # une epreuve pas encore ecrite n'est pas une faute (pendant le travail)

Ce qu'il verifie (pflege/FORMAT-TELC-PFLEGE.md) :
  1. le FORMAT : 4 + 10 + 6 + 3 questions d'ecoute, 4 + 5 + 6 + 3 de lecture, 8 + 10 d'elements de langue, numerotees
     1 a 59 dans l'ordre de l'examen ; l'exemple de l'ecoute 1 et de l'ecoute 4 ; les six phrases de l'ecoute 4
     (deux en trop), les six objets de la lecture 1, les huit lignes du plan de soins (une phrase en « x »), les dix
     mots de SB 1 (deux en trop) ;
  2. UNE SEULE BONNE REPONSE par question : l'indice existe, les choix sont distincts, une association n'utilise
     pas deux fois la meme solution ; aucune lettre ne porte plus de la moitie des bonnes reponses d'une partie a
     choix a, b, c ;
  3. les AIDES : chaque question a son explication en francais et en anglais, chaque objet traduit a sa cle ;
  4. les 9 LANGUES : l'interface (interface.json fr et en, langues/interface.<l>.json pour les 7 autres) et les
     aides de chaque epreuve (langues/<epreuve>.<l>.json) ont toutes les cles du francais, non vides ;
  5. l'AUDIO : aucun chiffre dans un texte dit (les nombres en lettres), chaque voix a son identifiant ;
  6. l'ECRIT : A et B, chaque information de la fiche retrouvee dans le texte modele, le modele entre 120 et 170 mots ;
  7. l'ORAL : les cinq taches et leurs points (5, 5, 15, 5, 20), deux sujets d'expose, chaque reponse modele
     remplissant les criteres de sa tache ;
  8. le BAREME (bareme.js, par node) : chaque seuil (26/27, 42/43 ; 6/7, 14/15 ; 34,5/35, 74,5/75), les 13 cas du
     B1 et les 3 du B2 du tableau officiel, les planchers (19 sur 59, 4 sur 20), l'oral qui decide, le contenu a 0,
     l'expose lu ;
  9. le CODE : chaque T("pf_…") de pflege-examen.js existe dans l'interface.
"""
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICI = os.path.join(DEPOT, "visuel", "prototype", "telc", "pflege")
DONNEES = os.path.join(ICI, "donnees")
MODELL = os.path.join(DONNEES, "modell-1")
LANGUES = ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"]
AUTRES = LANGUES[2:]
EPREUVES = ["hoeren", "lesen", "sprachbausteine", "schreiben", "sprechen"]
FORMAT = {"hoeren": [4, 10, 6, 3], "lesen": [4, 5, 6, 3], "sprachbausteine": [8, 10]}
DEBUT = {"hoeren": 1, "lesen": 24, "sprachbausteine": 42}
PARTIEL = "--partiel" in sys.argv

fautes, notes = [], []
faute = fautes.append


def lire(chemin):
    return json.load(io.open(chemin, encoding="utf-8")) if os.path.exists(chemin) else None


def items_de(teil):
    if "items" in teil:
        return teil["items"]
    groupes = teil.get("gespraeche") or teil.get("texte") or []
    return [it for g in groupes for it in g["items"]]


def objets_traduits(x, chemin=""):
    """Chaque objet qui porte un champ « X_fr » : (objet, [X…])."""
    if isinstance(x, dict):
        champs = [k[:-3] for k in x if k.endswith("_fr") and isinstance(x[k], str)]
        if champs:
            yield x, champs, chemin
        for k, v in x.items():
            yield from objets_traduits(v, chemin + "/" + k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from objets_traduits(v, chemin + "[%d]" % i)


def textes_dits(x):
    """Toutes les repliques {wer, text} des listes « audio », « audio_consigne », « dit »."""
    if isinstance(x, dict):
        for k, v in x.items():
            if k in ("audio", "audio_consigne", "dit") and isinstance(v, list):
                for l in v:
                    if isinstance(l, dict) and "text" in l:
                        yield l
            else:
                yield from textes_dits(v)
    elif isinstance(x, list):
        for v in x:
            yield from textes_dits(v)


def mots(t):
    return len(re.findall(r"[A-Za-zÄÖÜäöüß0-9-]+", t or ""))


# ------------------------------------------------------------------ les donnees
D = {e: lire(os.path.join(MODELL, e + ".json")) for e in EPREUVES}
for e in EPREUVES:
    if D[e] is None:
        (notes if PARTIEL else fautes).append("%s.json absent" % e)

# 1-2. le format et les bonnes reponses
tous_nr = []
for e, nombres in FORMAT.items():
    d = D[e]
    if not d:
        continue
    teile = d.get("teile", [])
    if [len(items_de(t)) for t in teile] != nombres:
        faute("%s : %s questions par partie, le telc en demande %s" % (e, [len(items_de(t)) for t in teile], nombres))
    nr = [it["nr"] for t in teile for it in items_de(t)]
    attendu = list(range(DEBUT[e], DEBUT[e] + sum(nombres)))
    if nr != attendu:
        faute("%s : numeros %s, attendus %d a %d dans l'ordre" % (e, nr, attendu[0], attendu[-1]))
    tous_nr += nr
    for t in teile:
        its = items_de(t)
        wahl = t.get("wahl")
        abc = []
        for it in its + ([t["beispiel"]] if t.get("beispiel") else []):
            ou = "%s %s n%s" % (e, t["cle"], it.get("nr"))
            typ, bon = it.get("typ"), it.get("bon")
            if typ == "abc":
                o = it.get("o") or []
                if len(o) != 3 or len(set(o)) != 3:
                    faute(ou + " : trois choix distincts attendus")
                if bon not in (0, 1, 2):
                    faute(ou + " : « bon » hors des trois choix")
                if it is not t.get("beispiel"):
                    abc.append(bon)
                if not it.get("frage"):
                    faute(ou + " : pas de question")
            elif typ == "rf":
                if bon not in (0, 1):
                    faute(ou + " : vrai / faux sans 0 ou 1")
                if not it.get("frage"):
                    faute(ou + " : pas d'affirmation")
            elif typ == "zuord":
                if not wahl:
                    faute(ou + " : association sans liste « wahl »")
                elif not (bon == "x" and t.get("mitX")) and not (isinstance(bon, int) and 0 <= bon < len(wahl)):
                    faute(ou + " : « bon » hors de la liste")
            else:
                faute(ou + " : type inconnu %r" % typ)
            if it is not t.get("beispiel") and not (it.get("erkl_fr") and it.get("erkl_en")):
                faute(ou + " : explication fr / en manquante")
        if len(abc) >= 4:
            for k in range(3):
                if abc.count(k) * 2 > len(abc):
                    faute("%s %s : la lettre %s porte %d bonnes reponses sur %d" % (e, t["cle"], "abc"[k], abc.count(k), len(abc)))
        if wahl:
            if len(set(json.dumps(w, ensure_ascii=False) for w in wahl)) != len(wahl):
                faute("%s %s : deux choix identiques dans « wahl »" % (e, t["cle"]))
            bons = [it["bon"] for it in its if it.get("typ") == "zuord"] + ([t["beispiel"]["bon"]] if t.get("beispiel") else [])
            pris = [b for b in bons if b != "x"]
            if len(set(pris)) != len(pris):
                faute("%s %s : une meme solution sert deux fois" % (e, t["cle"]))
            reste = len(wahl) - len(pris)
            attendu_reste = {("hoeren", 4): 2, ("lesen", 1): 2, ("lesen", 2): 4, ("sprachbausteine", 1): 2}.get((e, t["teil"]))
            if attendu_reste is not None and reste != attendu_reste:
                faute("%s %s : %d choix sans question, le format en laisse %d" % (e, t["cle"], reste, attendu_reste))
            if (e, t["teil"]) == ("lesen", 2) and (bons.count("x") != 1 or len(wahl) != 8 or not t.get("mitX")):
                faute("lesen L2 : huit lignes du plan et exactement une phrase « x » attendues")
        # un trou {n} du document pour chaque question des elements de langue
        if e == "sprachbausteine":
            texte = " ".join((t.get("doc") or {}).get("absaetze", []))
            trous = [int(n) for n in re.findall(r"\{(\d+)\}", texte)]
            if trous != [it["nr"] for it in its]:
                faute("%s : les trous du texte %s ne suivent pas les questions" % (t["cle"], trous))
if not PARTIEL and len(tous_nr) != 59:
    faute("%d questions en tout, le telc en compte 59" % len(tous_nr))
if D["hoeren"]:
    for t in D["hoeren"]["teile"]:
        if t["teil"] in (1, 4) and not t.get("beispiel"):
            faute("hoeren T%d : l'exemple manque" % t["teil"])

# 3. les cles des objets traduits
for e in EPREUVES:
    if not D[e]:
        continue
    vues = {}
    for o, champs, ch in objets_traduits(D[e]):
        if "cle" not in o:
            faute("%s %s : objet traduit sans « cle »" % (e, ch))
            continue
        if o["cle"] in vues and vues[o["cle"]] is not o:
            faute("%s : cle %s en double" % (e, o["cle"]))
        vues[o["cle"]] = o
        for c in champs:
            if not o.get(c + "_en"):
                faute("%s %s.%s : pas d'anglais" % (e, o["cle"], c))

# 4. les 9 langues
UI = lire(os.path.join(DONNEES, "interface.json")) or {}
if set(UI.get("fr", {})) != set(UI.get("en", {})):
    faute("interface.json : fr et en n'ont pas les memes cles (%s)" % sorted(set(UI.get("fr", {})) ^ set(UI.get("en", {}))))
for l in AUTRES:
    L = lire(os.path.join(DONNEES, "langues", "interface.%s.json" % l))
    if L is None:
        (notes if PARTIEL else fautes).append("langues/interface.%s.json absent" % l)
        continue
    manque = [k for k in UI["fr"] if not (L.get(k) or "").strip()]
    if manque:
        faute("interface %s : %d cle(s) manquante(s) : %s" % (l, len(manque), ", ".join(manque[:6])))
    for k, v in L.items():
        if k in UI["fr"]:
            for x in re.findall(r"\{[a-z]+\}", UI["fr"][k]):
                if x not in v:
                    faute("interface %s.%s : la valeur %s n'y est pas" % (l, k, x))
    for e in EPREUVES:
        if not D[e]:
            continue
        T = lire(os.path.join(MODELL, "langues", "%s.%s.json" % (e, l)))
        if T is None:
            (notes if PARTIEL else fautes).append("langues/%s.%s.json absent" % (e, l))
            continue
        manque = [o["cle"] + "." + c for o, champs, _ in objets_traduits(D[e]) if "cle" in o for c in champs
                  if not (T.get(o["cle"] + "." + c) or "").strip()]
        if manque:
            faute("%s %s : %d aide(s) sans traduction : %s" % (e, l, len(manque), ", ".join(manque[:5])))

# 5. l'audio
for e in ("hoeren", "sprechen"):
    if not D[e]:
        continue
    voix = dict((D["hoeren"] or {}).get("voix", {}))
    voix.update(D[e].get("voix", {}))
    for l in textes_dits(D[e]):
        if re.search(r"\d", l["text"]):
            faute("%s : chiffres dans un texte dit (a ecrire en lettres) : %s" % (e, l["text"][:60]))
        if not (voix.get(l["wer"]) or {}).get("voice_id"):
            faute("%s : la voix « %s » n'a pas d'identifiant" % (e, l["wer"]))

# 6. l'ecrit
S = D["schreiben"]
if S:
    if [a["id"] for a in S.get("aufgaben", [])] != ["A", "B"]:
        faute("schreiben : les taches A et B attendues")
    for a in S.get("aufgaben", []):
        if len(a.get("infos", [])) < 10:
            faute("schreiben %s : %d informations sur la fiche, trop peu" % (a["id"], len(a.get("infos", []))))
        modele = " ".join(a.get("modele", [])).lower()
        n = mots(modele)
        if not 120 <= n <= 170:
            faute("schreiben %s : le modele fait %d mots (120 a 170)" % (a["id"], n))
        for i in a.get("infos", []):
            try:
                ok = any(re.search(m, modele, re.I) for m in i["mots"])
            except re.error as x:
                faute("schreiben %s %s : mot repere invalide (%s)" % (a["id"], i["cle"], x))
                continue
            if not ok:
                faute("schreiben %s : l'information %s n'est pas dans le modele" % (a["id"], i["cle"]))
        if not a.get("redemittel"):
            faute("schreiben %s : pas de tournures utiles" % a["id"])

# 7. l'oral
SP = D["sprechen"]
if SP:
    attendu = [("sp1a", 5), ("sp1b", 5), ("sp2a", 15), ("sp2b", 5), ("sp3", 20)]
    if [(t["cle"], t["sur"]) for t in SP.get("taches", [])] != attendu:
        faute("sprechen : taches %s, attendues %s" % ([(t["cle"], t["sur"]) for t in SP.get("taches", [])], attendu))
    t2a = next((t for t in SP.get("taches", []) if t.get("themen")), None)
    if not t2a or len(t2a["themen"]) != 2:
        faute("sprechen : deux sujets d'expose attendus en 2A")
    ids = [th["id"] for th in (t2a or {}).get("themen", [])]

    def verifier_muster(nom, kriterien, muster):
        t = " ".join(muster or [])
        if not t:
            faute("sprechen %s : pas de reponse modele" % nom)
            return
        for k in kriterien or []:
            ok = True
            if k.get("min_woerter"):
                ok = ok and mots(t) >= k["min_woerter"]
            if k.get("mots"):
                ok = ok and sum(1 for m in k["mots"] if re.search(m, t, re.I)) >= k.get("mindestens", 1)
            if not ok:
                faute("sprechen %s : la reponse modele ne remplit pas « %s »" % (nom, k.get("label_fr")))

    for t in SP.get("taches", []):
        if t.get("themen"):
            for th in t["themen"]:
                verifier_muster(t["cle"] + "/" + th["id"], th.get("kriterien"), th.get("muster"))
        elif t.get("tours_nach_thema"):
            if sorted(t["tours_nach_thema"]) != sorted(ids):
                faute("sprechen %s : des tours pour chaque sujet attendus" % t["cle"])
            for th in ids:
                verifier_muster(t["cle"] + "/" + th, (t.get("kriterien_nach_thema") or {}).get(th) or t.get("kriterien"),
                                (t.get("muster_nach_thema") or {}).get(th) or t.get("muster"))
        else:
            if not t.get("tours"):
                faute("sprechen %s : pas de tours de parole" % t["cle"])
            verifier_muster(t["cle"], t.get("kriterien"), t.get("muster"))
        for tour in (t.get("tours") or []) + [x for ts in (t.get("tours_nach_thema") or {}).values() for x in ts]:
            if tour.get("consigne") and tour["consigne"] not in UI.get("fr", {}):
                faute("sprechen %s : consigne %s absente de l'interface" % (t["cle"], tour["consigne"]))
            if not tour.get("limite"):
                faute("sprechen %s : un tour sans limite de temps" % t["cle"])

# 8. le bareme, par node
SONDE = r"""
const B = require(process.argv[1]);
const r = [];
const eq = (nom, a, b) => r.push([nom, JSON.stringify(a) === JSON.stringify(b), a, b]);
eq("hls 26", B.niveauHLS(26), "unter"); eq("hls 27", B.niveauHLS(27), "b1");
eq("hls 42", B.niveauHLS(42), "b1"); eq("hls 43", B.niveauHLS(43), "b2"); eq("hls 59", B.niveauHLS(59), "b2");
eq("schr 6", B.niveauSchreiben(6), "unter"); eq("schr 7", B.niveauSchreiben(7), "b1");
eq("schr 14", B.niveauSchreiben(14), "b1"); eq("schr 15", B.niveauSchreiben(15), "b2");
eq("spr 34,5", B.niveauSprechen(34.5), "unter"); eq("spr 35", B.niveauSprechen(35), "b1");
eq("spr 74,5", B.niveauSprechen(74.5), "b1"); eq("spr 75", B.niveauSprechen(75), "b2");
// des points representatifs de chaque niveau : sous B1 au-dessus du plancher, B1, B2
const H = {u: 20, b1: 30, b2: 50}, S = {u: 5, b1: 10, b2: 18}, P = {b1: 50, b2: 80};
// les 13 cas du B1 et les 3 du B2 (tableau officiel, dans l'ordre) : [hls, schreiben, sprechen]
const B1 = [["b1","b1","b1"],["b1","u","b1"],["u","b1","b1"],["b2","b2","b1"],["b2","b1","b1"],["b1","b2","b1"],
            ["b2","u","b1"],["u","b2","b1"],["b1","b1","b2"],["u","b1","b2"],["b1","u","b2"],["b2","u","b2"],["u","b2","b2"]];
const B2 = [["b2","b2","b2"],["b2","b1","b2"],["b1","b2","b2"]];
B1.forEach((c, i) => eq("B1 cas " + (i + 1), B.zertifikat({hls: H[c[0]], schreiben: S[c[1]], sprechen: P[c[2]]}), "b1"));
B2.forEach((c, i) => eq("B2 cas " + (i + 1), B.zertifikat({hls: H[c[0]], schreiben: S[c[1]], sprechen: P[c[2]]}), "b2"));
// l'oral decide
eq("oral 34,5, ecrit B2", B.zertifikat({hls: 59, schreiben: 20, sprechen: 34.5}), null);
eq("oral 35, ecrit B2", B.zertifikat({hls: 59, schreiben: 20, sprechen: 35}), "b1");
eq("oral 75, ecrit 43 et 7", B.zertifikat({hls: 43, schreiben: 7, sprechen: 75}), "b2");
eq("oral 75, ecrit 43 et 6", B.zertifikat({hls: 43, schreiben: 6, sprechen: 75}), "b1");
eq("oral 75, ecrit 42 et 15", B.zertifikat({hls: 42, schreiben: 15, sprechen: 75}), "b2");
eq("oral 74,5, ecrit B2 B2", B.zertifikat({hls: 59, schreiben: 20, sprechen: 74.5}), "b1");
// deux ecrits sous B1 : rien
eq("deux ecrits sous B1", B.zertifikat({hls: 26, schreiben: 6, sprechen: 100}), null);
// les planchers
eq("plancher hls 19", B.zertifikat({hls: 19, schreiben: 7, sprechen: 35}), "b1");
eq("plancher hls 18", B.zertifikat({hls: 18, schreiben: 7, sprechen: 35}), null);
eq("plancher schr 4", B.zertifikat({hls: 27, schreiben: 4, sprechen: 35}), "b1");
eq("plancher schr 3", B.zertifikat({hls: 27, schreiben: 3, sprechen: 35}), null);
eq("plancher hls 18, oral B2", B.zertifikat({hls: 18, schreiben: 20, sprechen: 100}), null);
// les grilles
eq("ecrit maxi", B.punkteSchreiben({inhalt: 5, gestaltung: 5, korrektheit: 5, wortschatz: 5}), 20);
eq("ecrit contenu 0", B.punkteSchreiben({inhalt: 0, gestaltung: 5, korrektheit: 5, wortschatz: 5}), 0);
eq("ecrit crans", B.punkteSchreiben({inhalt: 3, gestaltung: 2, korrektheit: 4, wortschatz: 1}), 10);
eq("oral maxi", B.punkteSprechen({t1a: 5, t1b: 5, t2a: 15, t2b: 5, t3: 20, aussprache: 15, fluessigkeit: 10, korrektheit: 10, wortschatz: 15}), 100);
eq("oral lu", B.punkteSprechen({t1a: 5, t1b: 5, t2a: 15, t2b: 5, t3: 20, aussprache: 15, fluessigkeit: 10, korrektheit: 10, wortschatz: 15, abgelesen: true}), 88);
eq("cran hors bareme", B.borner(15, 13), 12);
eq("contenu complet", B.inhaltPunkte(16, 16), 5); eq("contenu 2 oublis", B.inhaltPunkte(16, 14), 5);
eq("contenu 3 oublis", B.inhaltPunkte(16, 13), 4); eq("contenu 12 oublis", B.inhaltPunkte(16, 4), 1);
eq("contenu rien", B.inhaltPunkte(16, 0), 0);
console.log(JSON.stringify(r));
"""
try:
    sortie = subprocess.run(["node", "-e", SONDE, os.path.join(ICI, "bareme.js")], capture_output=True, text=True, encoding="utf-8", timeout=60)
    res = json.loads(sortie.stdout)
    for nom, ok, a, b in res:
        if not ok:
            faute("bareme %s : %r au lieu de %r" % (nom, a, b))
    notes.append("bareme : %d cas verifies" % len(res))
except Exception as x:
    faute("bareme : node n'a pas pu tourner (%s)" % x)

# 9. le code
code = io.open(os.path.join(ICI, "pflege-examen.js"), encoding="utf-8").read()
for k in sorted(set(re.findall(r'T\("(pf_[a-z0-9_]+)"', code))):
    if k.endswith("_"):
        continue
    if k not in UI.get("fr", {}):
        faute("pflege-examen.js : T(\"%s\") absent de l'interface" % k)
familles = [("pf_e_", ["hoeren", "lesen", "schreiben", "vorbereitung", "sprechen", "grilles"], ["", "_s", "_q"]),
            ("pf_epr_", EPREUVES, ["", "_s"]),
            ("pf_jonas_", ["hoeren", "lesen", "sprachbausteine", "schreiben", "b1", "b2", "rien"], [""]),
            ("pf_pourquoi_", ["oral", "b1", "b2", "ecrit"], [""]),
            ("pf_crit_", ["inhalt", "gestaltung", "korrektheit", "wortschatz", "aussprache", "fluessigkeit"], [""])]
for pre, noms, suffixes in familles:
    for n in noms:
        for s in suffixes:
            if pre + n + s not in UI.get("fr", {}):
                faute("interface : %s%s%s manque" % (pre, n, s))
for epr, crits in (("schreiben", ["gestaltung", "korrektheit", "wortschatz"]), ("sprechen", ["aussprache", "fluessigkeit", "korrektheit", "wortschatz"])):
    for c in crits:
        for k in range(6):
            if "pf_desc_%s_%s_%d" % (epr, c, k) not in UI.get("fr", {}):
                faute("interface : pf_desc_%s_%s_%d manque" % (epr, c, k))

for n in notes:
    print("· " + n)
if fautes:
    print("\n%d faute(s) :" % len(fautes))
    for f in fautes:
        print("  ✗ " + f)
    sys.exit(1)
print("Examen telc Pflege : aucun probleme%s." % (" (partiel)" if PARTIEL else ""))
