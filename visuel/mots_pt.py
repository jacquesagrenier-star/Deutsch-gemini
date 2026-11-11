# -*- coding: utf-8 -*-
"""Les mots portugais des themes illustres : sont-ils au corpus, sous quelle forme au Bresil ?

    python visuel/mots_pt.py porta copo cheio "pequeno-almoço" estar
    python visuel/mots_pt.py --theme gato          # les mots que la page envoie (motsDuTheme), via le navigateur : non

Cherche chaque mot dans portugais/datos (Portugal) et, a la meme place, portugais/datos-br (Bresil, derive par
portugais/outils/bresil.py) : noms (themes.json, genre o / a), adjectifs, verbes (infinitif), adverbes, mots
fonctionnels. Un mot absent s'ajoute dans portugais/outils (noms_<niv>.py, mots_<niv>.py ; la forme du Bresil par
br= et bresil.py), puis python portugais/outils/construire.py -- jamais a la main dans portugais/datos.
"""
import json, os, sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def charger(dossier, f):
    return json.load(open(os.path.join(R, "portugais", dossier, f + ".json"), encoding="utf-8"))


def entrees(dossier):
    """(cat, niveau, mot, genre, traduction, position) pour tout le corpus d'un dossier"""
    out = []
    for th in charger(dossier, "themes")["themes"]:
        for n, m in enumerate(th["mots"]):
            out.append(("nom", th.get("niveau", ""), m["mot"], m.get("genre", ""), m.get("traduction", ""), ("t", th["id"], n), th["id"]))
    for f, cat, cle in (("adjectifs", "adjectif", "mot"), ("verbes", "verbe", "infinitif"), ("adverbes", "adverbe", "mot")):
        for niv, l in charger(dossier, f).items():
            for n, m in enumerate(l):
                out.append((cat, niv, m.get(cle) or m.get("mot", ""), "", m.get("traduction", ""), (f, niv, n), ""))
    for cle, l in charger(dossier, "fonctionnels").items():
        for n, m in enumerate(l if isinstance(l, list) else []):
            mot = m[0] if isinstance(m, list) else m.get("mot", "") if isinstance(m, dict) else ""
            tr = m[1] if isinstance(m, list) and len(m) > 1 else (m.get("traduction", "") if isinstance(m, dict) else "")
            out.append((cle, "", mot, "", tr, ("f", cle, n), ""))
    return out


def sans_accent(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def main():
    pt, br = entrees("datos"), entrees("datos-br")
    par_pos = {e[5]: e for e in br}
    for q in [a for a in sys.argv[1:] if not a.startswith("--")]:
        trouves = [e for e in pt if e[2] == q] or [e for e in pt if sans_accent(e[2]) == sans_accent(q)]
        trouves_br = [e for e in br if e[2] == q and not any(t[5] == e[5] for t in trouves)]
        if not trouves and not trouves_br:
            print("%-22s ABSENT du corpus" % q)
            continue
        for e in trouves:
            b = par_pos.get(e[5])
            print("%-22s %-11s %-3s %-2s %-28s Bresil : %s%s" % (q, e[0], e[1], e[3], e[4][:28], b[2] if b else "?", "" if not e[6] else "   [" + e[6] + "]"))
        for e in trouves_br:
            print("%-22s %-11s %-3s %-2s %-28s (forme du BRESIL seulement)" % (q, e[0], e[1], e[3], e[4][:28]))


if __name__ == "__main__":
    main()
