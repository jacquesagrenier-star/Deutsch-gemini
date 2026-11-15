"""Le controle de l'examen blanc telc Deutsch B1·B2 Pflege (visuel/prototype/telc-pflege/).

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
  4. les 9 LANGUES (contrat pflege/FORMAT-DONNEES.md) : interface.json a les 9 langues avec les cles du francais, et
     chaque champ traduit X d'un objet a X_fr … X_ru, non vides, avec les memes {x} ;
  5. l'AUDIO : aucun chiffre dans un texte dit (les nombres en lettres), chaque voix a son identifiant ;
  6. l'ECRIT : A et B, chaque information de la fiche retrouvee dans le texte modele, le modele entre 120 et 170 mots ;
  7. l'ORAL : les cinq taches et leurs points (5, 5, 15, 5, 20), deux sujets d'expose, chaque reponse modele
     remplissant les criteres de sa tache ;
  8. le BAREME (bareme.js, par node) : chaque seuil (26/27, 42/43 ; 6/7, 14/15 ; 34,5/35, 74,5/75), les 13 cas du
     B1 et les 3 du B2 du tableau officiel, les planchers (19 sur 59, 4 sur 20), l'oral qui decide, le contenu a 0,
     l'expose lu ;
  9. le CODE : chaque T("pf_…") de examen.js existe dans l'interface ; la page envoie le resultat au format du contrat
     (resultat_examen, soins_telc).
Les donnees sont en « series » (une serie = un examen blanc complet) : chaque serie est controlee.
 10. le MANUEL (pflege/examen/FORMAT-MANUEL.md) : les series d'entrainement (entrainement/<epreuve>.json : id 101 et
     plus, des parties entieres au format et a la numerotation de l'examen) ; la RESERVE (aucune phrase allemande d'un
     examen blanc dans l'entrainement) ; le sommaire (dix chapitres) et chaque chapitre (sortes de blocs, 9 langues,
     memes [[allemand]] et {x} que le francais, cles uniques, series et renvois existants, phrases dites sans
     chiffres). L'espagnol, 10e langue prevue, est compte, pas encore exige.
"""
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICI = os.path.join(DEPOT, "visuel", "prototype", "telc-pflege")
DONNEES = os.path.join(ICI, "donnees")
LANGUES = ["fr", "en", "tr", "uk", "fa", "pt", "ar", "pl", "ru"]
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
FICHIERS = {e: lire(os.path.join(DONNEES, e + ".json")) for e in EPREUVES}
for e in EPREUVES:
    if FICHIERS[e] is None:
        (notes if PARTIEL else fautes).append("%s.json absent" % e)
    elif not FICHIERS[e].get("series"):
        faute("%s.json : pas de « series »" % e)
IDS = sorted({s["id"] for f in FICHIERS.values() if f for s in f.get("series", [])})
for e in EPREUVES:
    if FICHIERS[e] and sorted(s["id"] for s in FICHIERS[e]["series"]) != IDS:
        faute("%s.json : les series %s, les autres epreuves ont %s" % (e, [s["id"] for s in FICHIERS[e]["series"]], IDS))

def controler(D, tous_nr, complet=True, ou=""):
    """Les controles 1 a 7 sur une serie : D = {epreuve: contenu de la serie (avec « voix »)}.
    complet=False : une serie d'ENTRAINEMENT (FORMAT-MANUEL.md, § 3) : des parties entieres, pas toutes."""
    # 1-2. le format et les bonnes reponses
    for e, nombres in FORMAT.items():
        d = D[e]
        if not d:
            continue
        teile = d.get("teile", [])
        if complet:
            if [len(items_de(t)) for t in teile] != nombres:
                faute("%s : %s questions par partie, le telc en demande %s" % (e, [len(items_de(t)) for t in teile], nombres))
            nr = [it["nr"] for t in teile for it in items_de(t)]
            attendu = list(range(DEBUT[e], DEBUT[e] + sum(nombres)))
            if nr != attendu:
                faute("%s : numeros %s, attendus %d a %d dans l'ordre" % (e, nr, attendu[0], attendu[-1]))
        else:
            if not teile:
                faute("%s%s : aucune partie" % (e, ou))
            vus = [t.get("teil") for t in teile]
            if len(set(vus)) != len(vus) or vus != sorted(vus):
                faute("%s%s : parties %s, chacune une fois et dans l'ordre" % (e, ou, vus))
            nr = []
            for t in teile:
                k = t.get("teil")
                if k not in range(1, len(nombres) + 1):
                    faute("%s%s : partie %r inconnue" % (e, ou, k))
                    continue
                n_t = [it["nr"] for it in items_de(t)]
                debut = DEBUT[e] + sum(nombres[:k - 1])
                if n_t != list(range(debut, debut + nombres[k - 1])):
                    faute("%s%s T%d : numeros %s, attendus %d a %d (ceux de l'examen)" % (e, ou, k, n_t, debut, debut + nombres[k - 1] - 1))
                nr.extend(n_t)
        tous_nr.extend(nr)
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

    # 4. les 9 langues, dans les objets
    for e in EPREUVES:
        if not D[e]:
            continue
        for o, champs, ch in objets_traduits(D[e]):
            for c in champs:
                fr = o[c + "_fr"]
                for l in LANGUES[1:]:
                    v = (o.get(c + "_" + l) or "").strip()
                    if not v:
                        faute("%s %s.%s : pas de %s" % (e, o.get("cle", ch), c, l))
                    elif sorted(re.findall(r"\{[a-z]+\}", v)) != sorted(re.findall(r"\{[a-z]+\}", fr)):
                        faute("%s %s.%s %s : les {x} different du francais" % (e, o.get("cle", ch), c, l))

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
        if complet and [a["id"] for a in S.get("aufgaben", [])] != ["A", "B"]:
            faute("schreiben : les taches A et B attendues")
        if not complet:
            ids_a = [a.get("id") for a in S.get("aufgaben", [])]
            if not ids_a or len(set(ids_a)) != len(ids_a):
                faute("schreiben%s : des taches aux id uniques attendues (%s)" % (ou, ids_a))
            for a in S.get("aufgaben", []):
                if a.get("art") not in ("A", "B"):
                    faute("schreiben%s %s : « art » A ou B attendu" % (ou, a.get("id")))
            if not S.get("consigne_de"):
                faute("schreiben%s : pas de consigne_de" % ou)
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
        faites = [(t["cle"], t["sur"]) for t in SP.get("taches", [])]
        if complet and faites != attendu:
            faute("sprechen : taches %s, attendues %s" % (faites, attendu))
        if not complet and (not faites or [x for x in attendu if x in faites] != faites):
            faute("sprechen%s : taches %s, des taches de l'examen (cle et points) dans l'ordre attendues" % (ou, faites))
        t2a = next((t for t in SP.get("taches", []) if t.get("themen")), None)
        if (complet or t2a or any(t["cle"] == "sp2b" for t in SP.get("taches", []))) and (not t2a or len(t2a["themen"]) != 2):
            faute("sprechen%s : deux sujets d'expose attendus en 2A" % ou)
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



UI = lire(os.path.join(DONNEES, "interface.json")) or {}
for l in LANGUES:
    if l not in UI:
        faute("interface.json : la langue %s manque" % l)
        continue
    manque = [k for k in UI["fr"] if not (UI[l].get(k) or "").strip()]
    if manque:
        faute("interface %s : %d cle(s) manquante(s) : %s" % (l, len(manque), ", ".join(manque[:6])))
    en_trop = [k for k in UI[l] if k not in UI["fr"]]
    if en_trop:
        faute("interface %s : cle(s) inconnue(s) : %s" % (l, ", ".join(en_trop[:6])))
    for k, v in UI[l].items():
        if k in UI["fr"] and sorted(re.findall(r"\{[a-z]+\}", v)) != sorted(re.findall(r"\{[a-z]+\}", UI["fr"][k])):
            faute("interface %s.%s : les {x} different du francais" % (l, k))

for sid in IDS:
    D = {}
    for e in EPREUVES:
        f = FICHIERS[e]
        s = next((x for x in (f or {}).get("series", []) if x["id"] == sid), None) if f else None
        D[e] = dict(s, voix=f.get("voix", {})) if s else None
    tous = []
    controler(D, tous)
    if not PARTIEL and len(tous) != 59:
        faute("serie %s : %d questions en tout, le telc en compte 59" % (sid, len(tous)))
    notes.append("serie %s : %d questions controlees" % (sid, len(tous)))

# ------------------------------------------------------------------ 10. le manuel (pflege/examen/FORMAT-MANUEL.md)
# Les series d'entrainement (donnees/entrainement/<epreuve>.json), la reserve des examens blancs, le sommaire et les
# chapitres (donnees/manuel/). L'espagnol, 10e langue prevue, n'est pas exige : on compte ce qui manque.
LANGUES_MANUEL = LANGUES + ["es"]
manque_es = []


def langues_de(o, c, ou, exiger):
    """Le champ traduit c d'un objet o : 9 langues (si exiger), memes {x} et memes [[…]] que le francais."""
    fr = o.get(c + "_fr") or ""
    if not fr.strip():
        faute("%s.%s : pas de francais" % (ou, c))
        return
    for l in LANGUES_MANUEL[1:]:
        v = (o.get(c + "_" + l) or "").strip()
        if not v:
            if l == "es":
                if exiger:
                    manque_es.append(ou + "." + c)
            elif exiger or l == "en":
                faute("%s.%s : pas de %s" % (ou, c, l))
            continue
        if sorted(re.findall(r"\{[a-z]+\}", v)) != sorted(re.findall(r"\{[a-z]+\}", fr)):
            faute("%s.%s %s : les {x} different du francais" % (ou, c, l))
        if sorted(re.findall(r"\[\[([^\]]+)\]\]", v)) != sorted(re.findall(r"\[\[([^\]]+)\]\]", fr)):
            faute("%s.%s %s : les [[allemand]] different du francais" % (ou, c, l))
    for l in LANGUES_MANUEL:
        v = o.get(c + "_" + l) or ""
        if v.count("[[") != v.count("]]"):
            faute("%s.%s %s : [[ … ]] mal fermes" % (ou, c, l))


def allemand_de(x):
    """Les phrases allemandes d'une serie (questions, choix, documents, repliques, modeles), pour la reserve."""
    if isinstance(x, dict):
        for k, v in x.items():
            if k in ("frage", "titre", "betreff", "text", "consigne_de") and isinstance(v, str):
                yield v
            elif k in ("o", "absaetze", "modele", "muster", "wahl", "aussagen", "redemittel", "stichworte") and isinstance(v, list):
                for w in v:
                    if isinstance(w, str):
                        yield w
                    else:
                        yield from allemand_de(w)
            else:
                yield from allemand_de(v)
    elif isinstance(x, list):
        for v in x:
            yield from allemand_de(v)


ENTR_DIR = os.path.join(DONNEES, "entrainement")
ENTR = {e: lire(os.path.join(ENTR_DIR, e + ".json")) for e in EPREUVES}
# la reserve : aucune phrase allemande d'un examen blanc dans l'entrainement (consignes et titres communs exceptes :
# ce sont ceux du telc, identiques d'une serie a l'autre)
communs = set()
for e in EPREUVES:
    for s in (FICHIERS[e] or {}).get("series", []):
        for t in s.get("teile", []):
            communs.update(x for x in (t.get("consigne_de"), t.get("titre")) if x)
            # les noms des AEDL et des ATL (titres des lignes d'un plan de soins) reviennent dans tout plan
            communs.update(w["titre"] for w in t.get("wahl") or [] if isinstance(w, dict) and w.get("titre"))
        communs.update(x for x in (s.get("consigne_de"),) if x)
        for t in s.get("taches", []):
            communs.update(x for x in (t.get("consigne_de"), t.get("teil")) if x)
examen_de = {}
for e in EPREUVES:
    for s in (FICHIERS[e] or {}).get("series", []):
        for phrase in allemand_de(s):
            if len(phrase) >= 25 and phrase not in communs:
                examen_de[phrase] = "%s modele %s" % (e, s["id"])
n_series = 0
for e in EPREUVES:
    f = ENTR[e]
    if f is None:
        continue
    series = f.get("series")
    if not isinstance(series, list):
        faute("entrainement/%s.json : pas de « series »" % e)
        continue
    ids = [s.get("id") for s in series]
    if len(set(ids)) != len(ids) or any(not isinstance(i, int) or i < 101 for i in ids):
        faute("entrainement/%s.json : id %s, uniques et a partir de 101 attendus" % (e, ids))
    voix = dict((FICHIERS["hoeren"] or {}).get("voix", {}))
    voix.update((FICHIERS[e] or {}).get("voix", {}))
    voix.update(f.get("voix", {}))
    for s in series:
        ou = " (entrainement %s)" % s.get("id")
        D = {x: None for x in EPREUVES}
        D[e] = dict(s, voix=voix)
        tous = []
        controler(D, tous, complet=False, ou=ou)
        if e in FORMAT and len(tous) != len(set(tous)):
            faute("%s%s : un numero en double" % (e, ou))
        for phrase in allemand_de(s):
            if phrase in examen_de:
                faute("%s%s reprend une phrase de l'examen blanc (%s) : %s" % (e, ou, examen_de[phrase], phrase[:60]))
        for o, champs, ch in objets_traduits(s):
            for c in champs:
                if o.get(c + "_fr") and not o.get(c + "_es"):
                    manque_es.append("%s%s %s.%s" % (e, ou, o.get("cle", ch), c))
        n_series += 1
    m = lire(os.path.join(ENTR_DIR, "voix-" + e + ".json"))
    if m is not None and any(not k.startswith("_") and not re.match(r"s1\d\d-", k) for k in m):
        faute("entrainement/voix-%s.json : une cle hors des series d'entrainement (s101-…)" % e)
notes.append("entrainement : %d serie(s) controlee(s)" % n_series)

# le sommaire
MANUEL = os.path.join(DONNEES, "manuel")
ATTENDUS = [("examen", None), ("hoeren", "hoeren"), ("lesen", "lesen"), ("sprachbausteine", "sprachbausteine"),
            ("schreiben", "schreiben"), ("sprechen", "sprechen"), ("kommunikation", None), ("beruf", None),
            ("grammatik", None), ("examens", None)]
SOM = lire(os.path.join(MANUEL, "sommaire.json"))
if SOM is None:
    faute("manuel/sommaire.json absent")
    SOM = {"chapitres": []}
chap = SOM.get("chapitres", [])
if [(c.get("id"), c.get("epreuve")) for c in chap] != ATTENDUS or [c.get("nr") for c in chap] != list(range(len(ATTENDUS))):
    faute("manuel/sommaire.json : chapitres %s, attendus %s numerotes de 0 a 9" % ([(c.get("id"), c.get("epreuve"), c.get("nr")) for c in chap], ATTENDUS))
for c in chap:
    for champ in ("titre", "resume"):
        langues_de(c, champ, "sommaire " + str(c.get("id")), True)

# les chapitres
VOIX_CHAPITRES = ["sprechen"]
VOIX_EXAMEN = dict((FICHIERS["hoeren"] or {}).get("voix", {}))
VOIX_EXAMEN.update((FICHIERS["sprechen"] or {}).get("voix", {}))
for c in VOIX_CHAPITRES:
    m = lire(os.path.join(DONNEES, "manuel", "voix-" + c + ".json"))
    if m is None:
        faute("manuel/voix-%s.json absent (la page le charge)" % c)
    elif any(not k.startswith("_") and not k.startswith("m-") for k in m):
        faute("manuel/voix-%s.json : une cle hors des exemples enregistres (m-…)" % c)
GROUPES_RM = ["patient", "famille", "collegues", "releve", "sbar", "visite", "negociation", "telephone"]
RM = lire(os.path.join(DEPOT, "pflege", "datos", "redemittel.json"))
BLOCS = {"p", "titre", "liste", "de", "piege", "tableau", "doc", "redemittel", "exercice", "serie", "renvoi"}
# les renvois portent les id de la section Soins (pflege/datos/) : soins_dlg_07_sbar, soins_ecrit_aufnahme_01,
# soins_gr_01_sie_imperativ, soins_<theme>, une scene par son nom ; verifies contre pflege/datos/ quand il est la
VERS = re.compile(r"^dialogue:soins_dlg_\d\d_[a-z0-9_]+$|^ecrit:soins_ecrit_[a-z0-9_]+$|^grammaire:soins_gr_\d\d_[a-z0-9_]+$"
                  r"|^theme:soins_[a-z0-9_]+$|^scene:[a-z0-9_-]+$|^chapitre:(%s)$" % "|".join(i for i, _ in ATTENDUS))
IDS_SOINS = {}
for genre, fichier, liste in (("dialogue", "dialogues", "dialogues"), ("ecrit", "ecrit", "sujets"), ("grammaire", "grammaire", "points")):
    d = lire(os.path.join(DEPOT, "pflege", "datos", fichier + ".json"))
    if d:
        IDS_SOINS[genre] = {x.get("id") for x in d.get(liste, [])}
cles_manuel = {}
n_chap = n_blocs = n_ex = 0
fichiers = sorted(x for x in os.listdir(MANUEL) if x.endswith(".json") and x != "sommaire.json" and not x.startswith("voix-")) if os.path.isdir(MANUEL) else []
for nom in fichiers:
    cid = nom[:-5]
    exemple = cid.startswith("_")
    if not exemple and cid not in [i for i, _ in ATTENDUS]:
        faute("manuel/%s : pas un chapitre du sommaire" % nom)
        continue
    if cid == "examens":
        faute("manuel/examens.json : le chapitre 9 n'a pas de fichier (la page liste les modeles)")
    C = lire(os.path.join(MANUEL, nom))
    if C.get("id") != cid:
        faute("manuel/%s : « id » %r, attendu %r" % (nom, C.get("id"), cid))
    rub = C.get("rubriques")
    if not isinstance(rub, list) or (exemple and not rub):
        faute("manuel/%s : « rubriques » doit etre une liste (vide = a venir)" % nom)
        rub = []
    r_ids = [r.get("id") for r in rub]
    if len(set(r_ids)) != len(r_ids) or not all(r_ids):
        faute("manuel/%s : id de rubrique manquant ou en double %s" % (nom, r_ids))
    exiger = not exemple
    n_chap += 1 if rub and not exemple else 0
    for r in rub:
        ou = "manuel/%s %s" % (cid, r.get("id"))
        if r.get("id") not in ("attendu", "pieges", "strategies", "guide"):
            langues_de(r, "titre", ou, exiger)
        if not r.get("blocs"):
            faute(ou + " : rubrique vide")
        for k, b in enumerate(r.get("blocs") or []):
            n_blocs += 1
            ob = "%s bloc %d (%s)" % (ou, k + 1, b.get("t"))
            t = b.get("t")
            if t not in BLOCS:
                faute(ob + " : sorte de bloc inconnue")
                continue
            for cle_de in ("de",):
                if cle_de in b and ("[[" in str(b[cle_de])):
                    faute(ob + " : pas de [[…]] dans un champ allemand")
            if t in ("p", "titre"):
                langues_de(b, "texte", ob, exiger)
            elif t == "liste":
                if not b.get("items"):
                    faute(ob + " : liste vide")
                for i in b.get("items") or []:
                    langues_de(i, "texte", ob, exiger)
            elif t == "de":
                if not b.get("de"):
                    faute(ob + " : pas d'allemand")
                if b.get("texte_fr"):
                    langues_de(b, "texte", ob, exiger)
                if b.get("cle"):
                    # un exemple enregistre : sa cle unique, ses repliques (« audio »), en lettres, aux voix connues
                    if b["cle"] in cles_manuel:
                        faute(ob + " : cle %r en double" % b["cle"])
                    cles_manuel[b["cle"]] = ob
                    if cid not in VOIX_CHAPITRES:
                        faute(ob + " : un exemple enregistre hors des chapitres %s (examen.js, VOIX_CHAPITRES)" % VOIX_CHAPITRES)
                    if not b.get("audio"):
                        faute(ob + " : « cle » sans « audio » ([{wer, text}])")
                    for l in b.get("audio") or []:
                        if re.search(r"\d", l.get("text", "")):
                            faute(ob + " : chiffres dans un texte dit (en lettres) : %s" % l.get("text", "")[:60])
                        if not (VOIX_EXAMEN.get(l.get("wer")) or {}).get("voice_id"):
                            faute(ob + " : la voix %r n'existe pas dans hoeren.json ni sprechen.json" % l.get("wer"))
            elif t == "piege":
                langues_de(b, "texte", ob, exiger)
                if b.get("titre_fr"):
                    langues_de(b, "titre", ob, exiger)
            elif t == "tableau":
                lignes = b.get("lignes") or []
                larg = {len(l) for l in lignes} | ({len(b["entetes"])} if b.get("entetes") else set())
                if not lignes or len(larg) != 1:
                    faute(ob + " : lignes de largeurs differentes ou tableau vide")
                for cel in (b.get("entetes") or []) + [c for l in lignes for c in l]:
                    if "de" not in cel:
                        langues_de(cel, "texte", ob, exiger)
            elif t == "doc":
                if not (b.get("doc") or {}).get("absaetze"):
                    faute(ob + " : document sans paragraphes")
            elif t == "redemittel":
                # une reference a la source unique (pflege/datos/redemittel.json, FORMAT-DONNEES.md § 2 bis)
                if b.get("phrases"):
                    faute(ob + " : pas de phrases ici, la source est pflege/datos/redemittel.json (« ref »)")
                if b.get("ref") not in GROUPES_RM:
                    faute(ob + " : « ref » %r, un des groupes %s" % (b.get("ref"), ", ".join(GROUPES_RM)))
                elif RM is not None and not any(c.get("groupe") == b["ref"] and not c.get("retire") for c in RM.get("cartes", [])):
                    notes.append("%s : aucune carte « %s » encore dans redemittel.json" % (ob, b["ref"]))
                if b.get("titre_fr"):
                    langues_de(b, "titre", ob, exiger)
            elif t == "exercice":
                n_ex += 1
                if not b.get("cle") or b["cle"] in cles_manuel:
                    faute(ob + " : cle %r manquante ou en double" % b.get("cle"))
                cles_manuel[b.get("cle")] = ob
                langues_de(b, "consigne", ob, exiger)
                its = b.get("items") or []
                if [it.get("nr") for it in its] != list(range(1, len(its) + 1)) or not its:
                    faute(ob + " : questions numerotees 1, 2, 3… attendues")
                for it in its:
                    oi = "%s n%s" % (ob, it.get("nr"))
                    if it.get("typ") == "abc":
                        if len(it.get("o") or []) != 3 or len(set(it["o"])) != 3 or it.get("bon") not in (0, 1, 2):
                            faute(oi + " : trois choix distincts et « bon » 0, 1 ou 2 attendus")
                    elif it.get("typ") == "rf":
                        if it.get("bon") not in (0, 1):
                            faute(oi + " : vrai / faux sans 0 ou 1")
                    else:
                        faute(oi + " : type %r (abc ou rf)" % it.get("typ"))
                    if not it.get("frage"):
                        faute(oi + " : pas de question")
                    langues_de(it, "erkl", oi, exiger)
                    if "pas_fr" in it:
                        pas = it["pas_fr"]
                        if not isinstance(pas, list) or not pas:
                            faute(oi + " : pas_fr doit etre une liste")
                        for l in LANGUES_MANUEL[1:]:
                            v = it.get("pas_" + l)
                            if v is None:
                                if l == "es":
                                    if exiger:
                                        manque_es.append(oi + ".pas")
                                elif exiger or l == "en":
                                    faute(oi + " : pas de pas_%s" % l)
                            elif not isinstance(v, list) or len(v) != len(pas):
                                faute(oi + " : pas_%s n'a pas les %d etapes du francais" % (l, len(pas)))
            elif t == "serie":
                e = b.get("epreuve")
                ids = [s.get("id") for s in ((ENTR.get(e) or {}).get("series") or [])]
                if e not in EPREUVES:
                    faute(ob + " : epreuve %r" % e)
                elif b.get("serie") not in ids and not exemple:
                    faute(ob + " : la serie %s n'existe pas dans entrainement/%s.json" % (b.get("serie"), e))
                if b.get("texte_fr"):
                    langues_de(b, "texte", ob, exiger)
            elif t == "renvoi":
                v = b.get("vers") or ""
                if not VERS.match(v):
                    faute(ob + " : « vers » %r ; les id de pflege/datos/ (dialogue:soins_dlg_07_sbar, ecrit:soins_ecrit_aufnahme_01, "
                               "grammaire:soins_gr_01_sie_imperativ, theme:soins_…, scene:…) ou chapitre:<id>" % v)
                elif v.split(":")[0] in IDS_SOINS and v.split(":", 1)[1] not in IDS_SOINS[v.split(":")[0]]:
                    faute(ob + " : %s n'existe pas dans pflege/datos/" % v)
                langues_de(b, "titre", ob, exiger)
notes.append("manuel : %d chapitre(s) ecrit(s) sur 9, %d bloc(s), %d exercice(s)" % (n_chap, n_blocs, n_ex))
# ce qu'une infirmiere doit valider : relire: true sur un bloc, une phrase de Redemittel, une question d'exercice
a_relire = []
for nom in fichiers:
    if nom.startswith("_"):
        continue
    C = lire(os.path.join(MANUEL, nom)) or {}
    for r in C.get("rubriques") or []:
        for k, b in enumerate(r.get("blocs") or []):
            for o in [b] + list(b.get("phrases") or []) + list(b.get("items") or []):
                if o.get("relire"):
                    a_relire.append("%s %s bloc %d : %s" % (nom[:-5], r.get("id"), k + 1, (o.get("de") or o.get("frage") or o.get("texte_fr") or o.get("titre_fr") or "")[:90]))
notes.append("manuel : %d point(s) a relire par une infirmiere (--relire pour la liste)" % len(a_relire))
if "--relire" in sys.argv:
    for x in a_relire:
        print("  ⚕ " + x)
if manque_es:
    notes.append("espagnol (10e langue, pas encore exigee) : %d texte(s) a traduire" % len(manque_es))

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
// les 13 cas de la session architecture (tests/pflege_certificat.js, certificatSoins d'index.html) : la page et
// l'app doivent dire la meme chose
const CAS = [[59,20,100,"B2"],[43,7,75,"B2"],[42,15,75,"B2"],[42,14,75,"B1"],[43,3,75,"aucun"],[43,4,75,"B1"],
  [18,15,80,"aucun"],[19,7,80,"B1"],[50,18,74.5,"B1"],[50,18,34.5,"aucun"],[26,6,90,"aucun"],[27,0,40,"aucun"],[27,4,40,"B1"]];
CAS.forEach(([h, s, o, att]) => { const z = B.zertifikat({hls: h, schreiben: s, sprechen: o}); eq("app " + h + "/" + s + "/" + o, z ? z.toUpperCase() : "aucun", att); });
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
code = io.open(os.path.join(ICI, "examen.js"), encoding="utf-8").read()
if 'parler("resultat_examen"' not in code or 'examen: "soins_telc"' not in code:
    faute("examen.js : le resultat ne part pas au format du contrat (resultat_examen, soins_telc)")
for k in sorted(set(re.findall(r'T\("(pf_[a-z0-9_]+)"', code))):
    if k.endswith("_"):
        continue
    if k not in UI.get("fr", {}):
        faute("examen.js : T(\"%s\") absent de l'interface" % k)
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
