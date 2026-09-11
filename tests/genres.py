# -*- coding: utf-8 -*-
"""Mesure le taux reel de chaque terminaison sur NOS noms.

⚠️ POURQUOI MESURER PLUTOT QUE RECOPIER. Une grammaire annonce « les noms en
-ung sont feminins » sans dire si c'est 100 % ou 94 %. Or la difference decide de
la formulation : « toujours » se dit d'une regle sans exception, « presque
toujours » d'une regle qui en a -- et enoncer comme absolue une regle qui a des
contre-exemples enseigne une fausse certitude. Jacques l'avait dit lui-meme a
propos de -e : « la majorite du temps, c'est feminin ».

Le corpus est le notre, pas l'allemand entier : le taux vaut pour ce que
l'etudiant rencontrera DANS l'app, ce qui est exactement la garantie utile.

    python tests/genres.py            # le tableau
    python tests/genres.py --ecrire   # ecrit branding/regles-genre.json
"""
import io, json, os, sys, collections

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Terminaisons candidates, groupees par genre attendu. L'ordre compte : la plus
# longue gagne, sinon « -ung » serait attrape par « -g » et « -heit » par « -t ».
CANDIDATES = [
    ("-ung", "die"), ("-heit", "die"), ("-keit", "die"), ("-schaft", "die"),
    ("-tion", "die"), ("-sion", "die"), ("-tät", "die"), ("-ität", "die"),
    ("-ie", "die"), ("-ik", "die"), ("-ur", "die"), ("-anz", "die"),
    ("-enz", "die"), ("-age", "die"), ("-ei", "die"), ("-in", "die"),
    ("-chen", "das"), ("-lein", "das"), ("-ment", "das"), ("-um", "das"),
    ("-ma", "das"), ("-tum", "das"), ("-nis", "das"),
    ("-er", "der"), ("-ling", "der"), ("-ismus", "der"), ("-ant", "der"),
    ("-or", "der"), ("-eur", "der"), ("-ist", "der"), ("-ig", "der"),
    ("-e", "die"),
]

def charger_noms():
    d = json.load(io.open(os.path.join(RACINE, "themes.json"), encoding="utf-8"))
    out = []
    for t in d["themes"]:
        for w in t.get("mots", []):
            g = w.get("genre")
            if g in ("der", "die", "das"):
                out.append((w["mot"], g, t.get("niveau", "")))
    return out

def mesurer(noms):
    resultats = []
    for suffixe, attendu in CANDIDATES:
        fin = suffixe[1:]
        # ⚠️ On EXCLUT les mots plus courts que la terminaison plus deux lettres :
        # « Ei » n'illustre pas la regle du suffixe « -ei », c'est le mot entier.
        pris = [(m, g) for m, g, _ in noms
                if m.lower().endswith(fin) and len(m) >= len(fin) + 2]
        if len(pris) < 4:
            continue
        bons = [x for x in pris if x[1] == attendu]
        exceptions = [x for x in pris if x[1] != attendu]
        resultats.append({
            "suffixe": suffixe, "genre": attendu,
            "total": len(pris), "conformes": len(bons),
            "taux": round(len(bons) * 100.0 / len(pris), 1),
            "exceptions": sorted(set("%s %s" % (g, m) for m, g in exceptions))[:8],
            "exemples": sorted(set(m for m, g in bons))[:4],
        })
    resultats.sort(key=lambda r: (-r["taux"], -r["total"]))
    return resultats

def main():
    noms = charger_noms()
    res = mesurer(noms)
    print("\n%d noms mesures\n" % len(noms))
    print("%-9s %-5s %6s %7s   %s" % ("fin", "genre", "mots", "taux", "exceptions"))
    print("-" * 78)
    for r in res:
        exc = ", ".join(r["exceptions"][:4]) if r["exceptions"] else "aucune"
        print("%-9s %-5s %6d %6.1f%%   %s" % (r["suffixe"], r["genre"], r["total"], r["taux"], exc[:44]))

    sures = [r for r in res if r["taux"] == 100.0 and r["total"] >= 8]
    fortes = [r for r in res if 90 <= r["taux"] < 100 and r["total"] >= 8]
    print("\nsans exception dans nos donnees (>= 8 mots) : %d" % len(sures))
    print("fortes mais avec exceptions (90-99 %%)      : %d" % len(fortes))

    if "--ecrire" in sys.argv:
        garde = [r for r in res if r["total"] >= 8 and r["taux"] >= 80]
        dest = os.path.join(RACINE, "branding", "regles-genre.json")
        json.dump({"_note": "Genere par tests/genres.py -- ne pas editer a la main. "
                            "Les taux sont mesures sur les noms de themes.json, pas "
                            "recopies d'une grammaire.",
                   "_mesure": "%d noms" % len(noms),
                   "regles": garde},
                  io.open(dest, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("\necrit : %s (%d regles)" % (dest, len(garde)))

if __name__ == "__main__":
    main()
