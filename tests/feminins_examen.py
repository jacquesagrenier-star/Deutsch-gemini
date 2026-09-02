# -*- coding: utf-8 -*-
"""Les feminins des listes d'examen : carte a part, ou champ sur le masculin ?

    python tests/feminins_examen.py             # ce qui serait rempli
    python tests/feminins_examen.py --ecrire    # remplit le champ `feminin`

LE COURS SAIT DEJA FAIRE LES PAIRES. Un nom de personne porte un champ
`feminin` (ou `masculin`), et la carte affiche « Feminin : die Aerztin » sous
« der Arzt ». Le commentaire du code dit pourquoi : donner « der Arzt » sans
« die Aerztin » laisse l'apprenant fabriquer le feminin au juge, et il est
irregulier une fois sur trois.

LES LISTES OFFICIELLES, ELLES, COMPTENT LES DEUX FORMES SEPAREMENT. « Autorin »
et « Bewohnerin » figurent au B1 comme entrees a part entiere. Les prendre au
mot donnerait quarante cartes de plus, chacune avec sa propre progression, pour
un mot que l'apprenant a deja vu au dos de son masculin.

ON REMPLIT DONC LE CHAMP, PAS UNE CARTE. Le mot compte alors comme couvert --
il est bien enseigne -- sans doubler le paquet. C'est le meme raisonnement que
pour le champ `pruefung` : poser l'information sur la carte qui existe plutot
que d'en fabriquer une nouvelle.

LA REGLE DE FORMATION EST VOLONTAIREMENT ETROITE : masculin + « in », avec le
« e » final qui tombe (Kunde -> Kundin) et l'Umlaut possible (Arzt -> Aerztin).
Tout ce qui n'entre pas dans ce moule est laisse de cote plutot que devine --
une paire fausse est pire qu'une paire absente.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMENS = os.path.join(RACINE, "examens")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import listes_examen as X                                   # noqa: E402

UMLAUT = {"a": "ä", "o": "ö", "u": "ü"}


def masculins_possibles(feminin):
    """« Autorin » -> {« Autor »}, « Kundin » -> {« Kunde », « Kund »}...

    On rend les candidats, pas une reponse : c'est la presence au cours qui
    tranche. Une forme inventee qui ne correspond a aucune carte est ignoree.
    """
    if not feminin.endswith("in") or len(feminin) < 5:
        return set()
    base = feminin[:-2]
    if base.endswith("n") and feminin.endswith("nin"):
        base = base[:-1]          # Chefin/Chef, mais Freundin -> Freund
    out = {base, base + "e"}
    # Le pluriel en -innen laisse parfois une consonne doublee.
    for i, c in enumerate(base):
        if c in UMLAUT.values():
            for clair, mod in UMLAUT.items():
                if c == mod:
                    out.add(base[:i] + clair + base[i + 1:])
                    out.add(base[:i] + clair + base[i + 1:] + "e")
    return {m for m in out if len(m) >= 3}


def noms_du_cours():
    """mot -> (theme, entree). Seuls les noms peuvent porter une paire."""
    chemin = os.path.join(RACINE, "themes.json")
    donnees = json.load(io.open(chemin, encoding="utf-8"))
    out = {}
    for t in donnees.get("themes", donnees):
        for m in t.get("mots", []):
            mot = (m.get("mot") or "").strip()
            if mot:
                out.setdefault(mot, []).append(m)
    return out


def serialiser(donnees, saut_final):
    texte = json.dumps(donnees, ensure_ascii=False, indent=2)
    return texte + "\n" if saut_final else texte


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    ecrire = "--ecrire" in sys.argv

    listes = X.charger()
    union = set()
    for mots in listes.values():
        union |= mots

    chemin = os.path.join(RACINE, "themes.json")
    brut = io.open(chemin, encoding="utf-8", newline="").read()
    donnees = json.loads(brut)
    saut = brut.endswith("\n")
    if serialiser(donnees, saut) != brut:
        print("  ! themes.json ne se reproduit pas a l'identique -- rien ecrit")
        return 1

    cours = noms_du_cours()
    poses, deja, orphelins = 0, 0, []
    for feminin in sorted(union):
        if not feminin.endswith("in") or feminin in cours:
            continue
        trouve = None
        for cand in masculins_possibles(feminin):
            if cand in cours:
                trouve = cand
                break
        if trouve is None:
            orphelins.append(feminin)
            continue
        for entree in cours[trouve]:
            if (entree.get("feminin") or "").strip() == feminin:
                deja += 1
                continue
            if entree.get("feminin") or entree.get("masculin"):
                deja += 1
                continue
            entree["feminin"] = feminin
            poses += 1
            print("  %-22s -> %s" % (trouve, feminin))

    print()
    print("  %d paire(s) %s, %d deja renseignee(s), %d sans masculin au cours"
          % (poses, "posee(s)" if ecrire else "a poser", deja, len(orphelins)))
    if orphelins:
        chemin_o = os.path.join(EXAMENS, "feminins-orphelins.txt")
        with io.open(chemin_o, "w", encoding="utf-8", newline="\n") as f:
            f.write("# Feminins des listes dont le masculin n'est pas au cours (%d).\n"
                    % len(orphelins))
            f.write("# Ceux-la ont besoin d'une vraie carte, ou de rien.\n\n")
            f.write("\n".join(orphelins) + "\n")
        print("  ecrit : examens/feminins-orphelins.txt")

    if ecrire and poses:
        with io.open(chemin, "w", encoding="utf-8", newline="") as f:
            f.write(serialiser(donnees, saut))
    return 0


if __name__ == "__main__":
    sys.exit(main())
