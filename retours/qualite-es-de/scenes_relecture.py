# -*- coding: utf-8 -*-
"""Les signalements de scenes de la relecture complete (decision « scene » de
triage.json) : applique les corrections EVIDENTES, celles dont la proposition
est un texte de remplacement complet, dans les SOURCES des scenes :
  - visuel/prototype/traductions/<scene>.<langue>.json : champ « trad » d'une
    paire {fr, trad} (groupes champs, couches, questions, sens) ;
  - visuel/prototype/espanol/<scene>.json : les champs traduits d'une question
    (sens_<langue>, n_<langue>).
Le reste (options d'exercice, phrases espagnoles, notes francaises, causes dans
l'allemand ou le francais source) est liste pour un tri a la main.
Chaque remplacement verifie le texte actuel. Apres --ecrire : construire.py
<scene> pour chaque scene touchee (fait scene-<scene>.js et .es.js).

    python retours/qualite-es-de/scenes_relecture.py            # montre
    python retours/qualite-es-de/scenes_relecture.py --ecrire   # applique
"""
import io
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
sys.argv_orig = list(sys.argv)
ECRIRE = "--ecrire" in sys.argv
sys.argv = sys.argv[:1]
import verdicts as V  # noqa: E402

# Mots qui trahissent une consigne au lieu d'un texte de remplacement
CONSIGNE = re.compile(r"\b(Remplacer|Ajouter|Choisir|Mettre|Lever|Rendre|Expliquer|reformuler|accepter)\b|\(ou\b| ou : ", re.I)
# Causes a soumettre a Jacques (la faute est dans la source)
A_JACQUES = ("Worauf wartest du", "Schokolade haben wollen")
LANGUES = ("en", "pt", "ar", "de", "tr", "uk", "fa", "pl", "ru", "fr")


def cible_traduction(doc, champ):
    """(objet {fr, trad}, 'trad') pour « sens.<cle>.trad », « sens[<cle>].trad »…"""
    m = re.match(r"^(champs|couches|questions|sens)(?:\.|\[)(.+?)(?:\])?(?:\.trad)?$", champ)
    if not m:
        return None
    groupe, cle = m.group(1), m.group(2)
    g = doc.get(groupe, {})
    for k in (cle, cle.rstrip("]")):
        if k in g and isinstance(g[k], dict) and "trad" in g[k]:
            return g[k], "trad"
    return None


def cible_espagnol(doc, champ):
    m = re.match(r"^couches\.(\w+)\.qs\[(\d+)\]\.((?:sens|n)_(\w+))$", champ)
    if not m or m.group(4) not in LANGUES:
        return None
    q = doc["couches"][m.group(1)]["qs"][int(m.group(2))]
    return q, m.group(3)


def main():
    T = json.load(io.open(os.path.join(ICI, "triage.json"), encoding="utf-8"))
    vs = {v["cle"]: v for v in V.verdicts(os.environ["TEMP"] + "/claude/qualite/complet")}
    docs, touches, journal, a_main = {}, set(), [], []
    for cle, t in sorted(T.items()):
        if t.get("decision") != "scene":
            continue
        v = vs.get(cle, {})
        f, champ = v.get("fichier", ""), v.get("champ", "")
        avant, apres = v.get("actuel"), v.get("propose")
        if any(x in cle or x in champ for x in A_JACQUES):
            a_main.append(("JACQUES", cle))
            continue
        if not isinstance(apres, str) or CONSIGNE.search(apres) or not isinstance(avant, str):
            a_main.append(("A LA MAIN", cle))
            continue
        chemin = os.path.join(RACINE, f)
        if f not in docs:
            docs[f] = json.load(io.open(chemin, encoding="utf-8"))
        if "/traductions/" in f:
            c = cible_traduction(docs[f], champ)
        else:
            c = cible_espagnol(docs[f], champ)
        if not c:
            a_main.append(("A LA MAIN", cle))
            continue
        o, k = c
        if o.get(k) == apres:
            continue
        if o.get(k) != avant:
            print("REFUS %s : actuel %r" % (cle, str(o.get(k))[:80]))
            continue
        o[k] = apres
        touches.add(f)
        journal.append({"cle": cle, "avant": avant, "apres": apres})
        t["decision"] = "fait"
        t["raison"] = (t.get("raison") or "") + " -- corrigé à la source de la scène (scenes_relecture.py)"
    for genre, c in a_main:
        print(genre, c[:150])
    print("\n%d corrections dans %d fichiers ; %d à la main ou à Jacques" % (len(journal), len(touches), len(a_main)))
    if not ECRIRE:
        return
    # Remplacement dans le texte brut, pour garder la mise en forme de chaque
    # fichier (certains ne sortent pas a l'identique de json.dumps) : le texte
    # encode de l'ancienne valeur doit y figurer une seule fois.
    par_fichier = {}
    for j in journal:
        par_fichier.setdefault(j["cle"].split("|")[1], []).append(j)
    for f, liste in par_fichier.items():
        chemin = os.path.join(RACINE, f)
        raw = io.open(chemin, encoding="utf-8", newline="").read()
        for j in liste:
            vieux = json.dumps(j["avant"], ensure_ascii=False)
            neuf = json.dumps(j["apres"], ensure_ascii=False)
            assert raw.count(vieux) == 1, "texte introuvable ou repete dans %s : %s" % (f, vieux[:60])
            raw = raw.replace(vieux, neuf)
        assert json.loads(raw) == docs[f], "le remplacement brut ne donne pas le document attendu : " + f
        io.open(chemin, "w", encoding="utf-8", newline="").write(raw)
    json.dump(T, io.open(os.path.join(ICI, "triage.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    p = os.path.join(ICI, "corrections-scenes.json")
    ancien = json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else []
    json.dump(ancien + journal, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("scenes a reconstruire :", " ".join(sorted({os.path.basename(f).split(".")[0] for f in touches})))


if __name__ == "__main__":
    main()
