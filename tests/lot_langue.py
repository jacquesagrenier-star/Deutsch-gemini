# -*- coding: utf-8 -*-
"""Sort le prochain lot de cartes a traduire, et dit ce qui reste.

    python tests/lot_langue.py --langue uk --etat
    python tests/lot_langue.py --langue uk --lot themes.json A1 Familie
    python tests/lot_langue.py --langue uk --lot verbe.json A1 --taille 40

CE QUE CE SCRIPT NE FAIT PAS : ecrire. Il ne sert qu'a poser sous les yeux
l'allemand, le francais et l'anglais des cartes qui n'ont pas encore la langue
cible -- dans l'ordre du fichier, par paquets d'une taille choisie. La pose se
fait par tests/patch_langue.py, qui porte le garde-fou d'aller-retour.

POURQUOI SEPARER LES DEUX. Le turc a perdu 673 entrees parce qu'une boucle
d'extraction et une boucle d'ecriture vivaient dans le meme script : une
erreur de type dans la premiere a fait ecrire un caractere par entree, et rien
ne l'a vu parce que le champ existait et n'etait pas vide. Un script qui ne
peut pas ecrire ne peut pas abimer le corpus.

L'ANGLAIS EST SORTI EN MEME TEMPS QUE LE FRANCAIS, ET C'EST UTILE. Le francais
tranche parfois un sens que l'allemand laisse ouvert ; l'anglais le tranche
autrement. Voir les deux ensemble evite de recopier l'arbitrage francais dans
une langue qui n'en avait pas besoin.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from langue import Langue, FICHIERS, NIVEAUX          # noqa: E402

TEMPS = ["exemple", "perfekt", "praeteritum", "konjunktiv2"]


def charger(nom):
    return json.load(io.open(os.path.join(RACINE, nom), encoding="utf-8"))


def entrees(fichier, niveau=None, theme=None):
    """Toutes les entrees d'un fichier, avec leur niveau et leur theme."""
    d = charger(fichier)
    out = []
    if fichier == "themes.json":
        for t in d.get("themes", d):
            if niveau and t.get("niveau") != niveau:
                continue
            if theme and t.get("nom_theme") != theme:
                continue
            for m in t.get("mots", []):
                out.append((m, t.get("niveau"), t.get("nom_theme")))
    elif fichier == "funktionswort.json":
        for classe, liste in d.items():
            if not isinstance(liste, list):
                continue
            for m in liste:
                if niveau and m.get("niveau") != niveau:
                    continue
                out.append((m, m.get("niveau"), classe))
    else:
        for niv in NIVEAUX:
            if niveau and niv != niveau:
                continue
            for m in d.get(niv, []):
                out.append((m, niv, None))
    return out


def manque(m, lg, fichier):
    """L'entree attend-elle encore quelque chose dans la langue cible ?"""
    if not m.get(lg.champ("traduction")):
        return True
    if fichier == "verbe.json":
        return any(m.get(t) and not m.get(lg.champ(t)) for t in TEMPS)
    return bool(m.get("exemple")) and not m.get(lg.champ("exemple"))


def etat(lg):
    total = restant = 0
    for cat, (fichier, cle) in sorted(FICHIERS.items()):
        for niveau in ("A1", "A2", "B1", "B2", "C1"):
            liste = entrees(fichier, niveau)
            if not liste:
                continue
            n = sum(1 for m, _, _ in liste if manque(m, lg, fichier))
            total += len(liste)
            restant += n
            if n:
                print("   %-12s %-3s : %4d a faire sur %4d"
                      % (cat, niveau, n, len(liste)))
    # funktionswort n'est pas dans FICHIERS : il n'a pas de relecture croisee,
    # mais il a bien des cartes et il faut les compter.
    for niveau in ("A1", "A2", "B1", "B2", "C1"):
        liste = entrees("funktionswort.json", niveau)
        n = sum(1 for m, _, _ in liste if manque(m, lg, "funktionswort.json"))
        total += len(liste)
        restant += n
        if n:
            print("   %-12s %-3s : %4d a faire sur %4d"
                  % ("mots-outils", niveau, n, len(liste)))
    print("   ---")
    print("   %s : %d cartes a faire sur %d (%.1f %% faites)"
          % (lg.code, restant, total, 100.0 * (total - restant) / total))


def lot(lg, fichier, niveau, theme, taille):
    cle = "infinitif" if fichier == "verbe.json" else "mot"
    n = 0
    for m, niv, th in entrees(fichier, niveau, theme):
        if not manque(m, lg, fichier):
            continue
        n += 1
        if n > taille:
            break
        tete = m.get(cle, "")
        if m.get("genre"):
            tete = m["genre"] + " " + tete
        print("- %s%s" % (tete, (" [%s]" % th) if th else ""))
        print("    fr %s | en %s" % (m.get("traduction", ""), m.get("traduction_en", "")))
        if fichier == "verbe.json":
            for t in TEMPS:
                if m.get(t) and not m.get(lg.champ(t)):
                    print("    %-12s %s" % (t, m[t]))
                    print("       fr %s" % m.get(t + "_fr", ""))
        elif m.get("exemple"):
            print("    de %s" % m["exemple"])
            print("    fr %s" % m.get("exemple_fr", ""))
    print("\n(%d cartes sorties)" % min(n, taille))


def main():
    a = sys.argv[1:]
    lg = Langue("uk")
    if "--langue" in a:
        lg = Langue(a[a.index("--langue") + 1])
    taille = 40
    if "--taille" in a:
        taille = int(a[a.index("--taille") + 1])
    if "--etat" in a:
        etat(lg)
        return 0
    if "--lot" in a:
        i = a.index("--lot")
        reste = [x for x in a[i + 1:] if not x.startswith("--")]
        # on retire les valeurs des options qui suivent
        if "--taille" in a and str(taille) in reste:
            reste.remove(str(taille))
        fichier = reste[0]
        niveau = reste[1] if len(reste) > 1 else None
        theme = reste[2] if len(reste) > 2 else None
        lot(lg, fichier, niveau, theme, taille)
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
