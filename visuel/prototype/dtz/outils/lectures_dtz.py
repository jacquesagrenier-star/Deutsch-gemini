"""Les lectures en lettres des textes du DTZ (Hoeren) qui contiennent des chiffres, versees dans audio/lectures/de.json.

    python visuel/prototype/dtz/outils/lectures_dtz.py           # verse ce qui manque, dit ce qui reste sans lecture

LA REGLE DU PROJET (28 oct. 2026) : les nombres se disent en lettres ; l'ecrit garde ses chiffres (l'eleve doit lire
« 17:42 Uhr », c'est ce qu'il verra en Allemagne), seule la voix recoit la lecture, ecrite et relue a la main, rangee
dans audio/lectures/de.json ({ ecrit : dit }). On ecrit ici, par commodite, seulement LE MORCEAU qui change
(« 17:42 Uhr » -> « siebzehn Uhr zweiundvierzig ») ; le script fabrique la phrase entiere et la verse dans le fichier
commun. Une phrase a chiffres sans lecture arrete voix.py avant toute depense.
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
DTZ = os.path.dirname(ICI)
DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(DTZ)))
LECTURES = os.path.join(DEPOT, "audio", "lectures", "de.json")

# morceau ecrit -> morceau dit, appliques dans cet ordre (le plus long d'abord quand deux se recouvrent)
MORCEAUX = [
    ("Teil 1.", "Teil eins."), ("Teil 2.", "Teil zwei."), ("Teil 3.", "Teil drei."), ("Teil 4.", "Teil vier."),
    ("von 9 bis 15 Uhr", "von neun bis fünfzehn Uhr"),
    ("Information zu Gleis 4:", "Information zu Gleis vier:"),
    ("Regionalexpress RE 1 nach Frankfurt (Oder)", "Regionalexpress R E eins nach Frankfurt an der Oder"),
    ("Abfahrt 17:42 Uhr", "Abfahrt siebzehn Uhr zweiundvierzig"),
    ("die S-Bahn S 3 von Gleis 15", "die S-Bahn S drei von Gleis fünfzehn"),
    ("von 8 bis 18 Uhr", "von acht bis achtzehn Uhr"),
    ("in Raum 204 und nicht wie sonst in Raum 112", "in Raum zweihundertvier und nicht wie sonst in Raum hundertzwölf"),
    ("Auf der A 100", "Auf der A hundert"),
    ("5 Kilometer Stau", "fünf Kilometer Stau"),
    ("um 10 Grad", "um zehn Grad"), ("bis minus 2 Grad", "bis minus zwei Grad"), ("aber nur 5 Grad", "aber nur fünf Grad"),
    ("Von 10 bis 16 Uhr", "Von zehn bis sechzehn Uhr"),
    ("kostet er 10 Euro im Jahr", "kostet er zehn Euro im Jahr"),
    ("um 20 Uhr", "um zwanzig Uhr"),
    ("unter 030 22 00 44", "unter null dreißig, zweiundzwanzig, null null, vierundvierzig"),
    ("von 9 bis 14 Uhr", "von neun bis vierzehn Uhr"),
    ("aus der Gartenstraße 12", "aus der Gartenstraße zwölf"),
    ("um 15 Uhr", "um fünfzehn Uhr"),
    ("kostet 10 Euro", "kostet zehn Euro"),
    ("Ich suche Raum 112", "Ich suche Raum hundertzwölf"),
    ("in Raum 204", "in Raum zweihundertvier"),
    ("Seite 18", "Seite achtzehn"),
]


def textes_dits():
    """Tous les textes que la voix dira : consignes, et chaque replique de chaque serie."""
    H = json.load(io.open(os.path.join(DTZ, "donnees", "hoeren.json"), encoding="utf-8"))
    out = [c["de"] for c in H["consignes"].values()]
    for s in H["series"]:
        for t in ("T1", "T2", "T3"):
            for it in s[t]:
                out += [l["text"] for l in it.get("audio") or []]
        out += [l["text"] for l in s["T4"]["intro"]]
        for a in s["T4"]["aussagen"]:
            out += [l["text"] for l in a["audio"]]
    return out


def dire(texte):
    for ecrit, dit in MORCEAUX:
        texte = texte.replace(ecrit, dit)
    return texte


def main():
    table = json.load(io.open(LECTURES, encoding="utf-8"))
    ajouts, restes = 0, []
    for t in textes_dits():
        if not re.search(r"\d", t):
            continue
        d = dire(t)
        if re.search(r"\d", d):
            restes.append(t)
            continue
        if table.get(t) != d:
            table[t] = d
            ajouts += 1
    io.open(LECTURES, "w", encoding="utf-8", newline="\n").write(json.dumps(table, ensure_ascii=False, indent=1) + "\n")
    print("%d lecture(s) versee(s) dans audio/lectures/de.json" % ajouts)
    if restes:
        print("\n%d texte(s) a chiffres SANS lecture (ajouter un morceau dans MORCEAUX) :" % len(restes))
        for t in restes:
            print("  - " + t)
        sys.exit(1)


if __name__ == "__main__":
    main()
