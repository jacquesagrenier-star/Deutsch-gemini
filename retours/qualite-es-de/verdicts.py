# -*- coding: utf-8 -*-
"""Les verdicts de la relecture complete : tri, puis application.

    python retours/qualite-es-de/verdicts.py <dossier> --a-trier        # signalements sans decision
    python retours/qualite-es-de/verdicts.py <dossier> --etat           # lots faits, decisions
    python retours/qualite-es-de/verdicts.py <dossier> --ecrire         # applique les « appliquer »

Chaque signalement recoit une decision dans triage.json (a cote de ce script),
cle = "NNN|fichier|chemin|champ" :
    {"decision": "appliquer" | "trancher" | "ecarter", "apres": "...", "raison": "..."}
« apres » remplace la proposition du relecteur quand elle ne convient pas.
L'application verifie que le texte ACTUEL est bien celui que le relecteur a
cite : si le fichier a change, ou si la citation etait inexacte, elle refuse.
La langue apprise (allemand, espagnol) a sa voix enregistree : une decision
qui la touche passe par « trancher », jamais par « appliquer ».
"""
import glob
import io
import json
import os
import re
import sys

from commun import RACINE

TRIAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "triage.json")


def verdicts(dossier):
    out = []
    for f in sorted(glob.glob(os.path.join(dossier, "verdict-*.json"))):
        n = re.search(r"verdict-(\d+)\.json$", f).group(1)
        try:
            lst = json.load(io.open(f, encoding="utf-8"))
        except ValueError:
            print("ILLISIBLE", f)
            continue
        for v in lst if isinstance(lst, list) else []:
            v["lot"] = n
            v["cle"] = "%s|%s|%s|%s" % (n, v.get("fichier"), v.get("chemin"), v.get("champ"))
            out.append(v)
    return out


def jetons(s):
    out = []
    for morceau in re.findall(r"[^.\[\]]+|\[\d+\]", s or ""):
        out.append(int(morceau[1:-1]) if morceau.startswith("[") else morceau)
    return out


def parent_et_cle(doc, fichier, chemin, champ):
    """L'objet qui porte le champ, et le nom du champ."""
    if fichier.endswith("grammaire.json") and chemin.startswith("textes.*."):
        return doc["textes"][champ], chemin[len("textes.*."):]
    j = jetons(chemin) + jetons(champ)
    o = doc
    if fichier.endswith("themes.json") or fichier.endswith("temas.json"):
        o = next(t for t in doc["themes"] if t["id"] == j[0])
        j = j[1:]
    for k in j[:-1]:
        if isinstance(o, dict) and k not in o and isinstance(k, str) and "jeux" in o:
            o = o["jeux"]
        o = o[k]
    return o, j[-1]


def format_de(rel):
    raw = io.open(os.path.join(RACINE, rel), encoding="utf-8", newline="").read().replace("\r\n", "\n")
    d = json.loads(raw)
    for ind in (None, 1, 2, 4):
        for sep in ((",", ": "), (", ", ": "), (",", ":")):
            s = json.dumps(d, ensure_ascii=False, indent=ind, separators=sep)
            for fin in ("", "\n"):
                if s + fin == raw:
                    return ind, sep, fin
    raise SystemExit("format inconnu : " + rel)


def main():
    dossier = sys.argv[1]
    V = verdicts(dossier)
    T = json.load(io.open(TRIAGE, encoding="utf-8")) if os.path.exists(TRIAGE) else {}
    if "--a-trier" in sys.argv:
        for v in V:
            if v["cle"] not in T:
                print(json.dumps({k: v.get(k) for k in ("cle", "actuel", "probleme", "propose", "certitude")},
                                 ensure_ascii=False))
        return
    if "--etat" in sys.argv:
        faits = len(glob.glob(os.path.join(dossier, "verdict-*.json")))
        dec = {}
        for v in V:
            d = T.get(v["cle"], {}).get("decision", "a trier")
            dec[d] = dec.get(d, 0) + 1
        print("lots relus : %d ; signalements : %d ; %s" % (faits, len(V), dec))
        return
    if "--ecrire" in sys.argv:
        docs, journal = {}, []
        # « manuel|fichier|chemin|champ » : une correction que le relecteur a
        # suggeree en passant (dans son texte) sans en faire un signalement
        for cle, t in T.items():
            if cle.startswith("manuel|"):
                _, f, ch, champ = cle.split("|")
                V.append({"cle": cle, "fichier": f, "chemin": ch, "champ": champ,
                          "actuel": t["avant"], "propose": t["apres"]})
        for v in V:
            t = T.get(v["cle"])
            if not t or t.get("decision") != "appliquer":
                continue
            f = v["fichier"]
            if f not in docs:
                docs[f] = json.load(io.open(os.path.join(RACINE, f), encoding="utf-8"))
            o, k = parent_et_cle(docs[f], f, v.get("chemin", ""), v.get("champ", ""))
            if t.get("supprimer"):
                if k in o and o[k] == t.get("avant", v.get("actuel")):
                    journal.append({"cle": v["cle"], "avant": o.pop(k), "apres": None, "raison": t.get("raison")})
                continue
            apres = t.get("apres", v.get("propose"))
            if o.get(k) == apres:
                continue
            avant = t.get("avant", v.get("actuel"))
            if o.get(k) != avant:
                print("REFUS %s : actuel %r, cite %r" % (v["cle"], o.get(k), avant))
                continue
            o[k] = apres
            journal.append({"cle": v["cle"], "avant": avant, "apres": apres, "raison": t.get("raison", v.get("probleme"))})
            # Le meme mot recopie ailleurs (chapitres VHS, autres niveaux) avec
            # EXACTEMENT le meme texte fautif : meme correction.
            if (f.endswith("themes.json") or f.endswith("temas.json")) and isinstance(k, str) and "mot" in o:
                for th in docs[f]["themes"]:
                    for cle_l in ("mots", "verben", "adjektive"):
                        for i, m in enumerate(th.get(cle_l, [])):
                            # meme mot ET meme sens (traduction francaise) : Betreuer est un
                            # directeur de memoire a l'universite, un animateur en sortie
                            if m is not o and m.get("mot") == o["mot"] and m.get(k) == avant \
                                    and m.get("traduction") == o.get("traduction"):
                                m[k] = apres
                                journal.append({"cle": "copie|%s|%s.%s[%d]|%s" % (f, th["id"], cle_l, i, k),
                                                "avant": avant, "apres": apres, "raison": "copie de " + v["cle"]})
        for f, d in docs.items():
            ind, sep, fin = format_de(f)
            with io.open(os.path.join(RACINE, f), "w", encoding="utf-8", newline="\n") as h:
                h.write(json.dumps(d, ensure_ascii=False, indent=ind, separators=sep) + fin)
        prec = os.path.join(os.path.dirname(TRIAGE), "corrections-relecture.json")
        ancien = json.load(io.open(prec, encoding="utf-8")) if os.path.exists(prec) else []
        json.dump(ancien + journal, io.open(prec, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("%d corrections appliquees" % len(journal))


if __name__ == "__main__":
    main()
