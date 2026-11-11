# -*- coding: utf-8 -*-
"""Les mots que les pages des themes envoient en portugais existent-ils dans le corpus ACTIF, avec leur genre ?

    python visuel/mots_themes_pt.py <dossier des echantillons>

Lit les lignes « MOTS : » des sorties de visuel/echantillon_theme.py (ech-<theme>-pt.log : Portugal, portugais/datos ;
ech-<theme>-br.log : Bresil, portugais/datos-br) et cherche chaque mot comme le fait l'app (carteDeScene) : un nom par
son mot ET son genre, un adjectif / verbe / adverbe / preposition par son mot. Un mot absent ne casse rien (pas de
carte, donc pas de progression pour lui) : la liste dit ce qui manque encore.
"""
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = sys.argv[1]


def corpus(dossier):
    c = lambda f: json.load(open(os.path.join(R, "portugais", dossier, f + ".json"), encoding="utf-8"))
    noms = {(m["mot"], m.get("genre", "")) for th in c("themes")["themes"] for m in th["mots"]}
    autres = {}
    for f, cat, cle in (("adjectifs", "adjectif", "mot"), ("verbes", "verbe", "infinitif"), ("adverbes", "adverbe", "mot")):
        autres[cat] = {m.get(cle) for l in c(f).values() for m in l}
    autres["praep"] = {(m[0] if isinstance(m, list) else m.get("mot")) for m in c("fonctionnels").get("praepositionen", [])}
    return noms, autres


total = 0
for var, dossier in (("pt", "datos"), ("br", "datos-br")):
    noms, autres = corpus(dossier)
    for f in sorted(glob.glob(os.path.join(D, "ech-*-%s.log" % var))):
        th = os.path.basename(f)[4:-len("-%s.log" % var)]
        ligne = next((l for l in open(f, encoding="utf-8") if l.startswith("MOTS : ")), None)
        if not ligne:
            print("%-11s %s : pas de liste (echantillon a refaire)" % (th, var)); continue
        manque = []
        for e in ligne[7:].strip().split(", "):
            m = re.match(r"^(.*?)(?:\((o|a|os|as)\))?/(\w*)$", e)
            if not m: continue
            mot, genre, cat = m.group(1), m.group(2) or "", m.group(3)
            ok = (mot, genre) in noms if genre or cat in ("", "nom") else mot in autres.get(cat, set())
            if not ok and not genre and cat in ("", "nom"): ok = any(n[0] == mot for n in noms)
            if not ok: manque.append(mot + ("(" + genre + ")" if genre else "") + "/" + cat)
        total += len(manque)
        print("%-11s %s : %s" % (th, var, "tous au corpus" if not manque else "%d hors corpus : %s" % (len(manque), ", ".join(manque))))
print("hors corpus en tout :", total)
