# -*- coding: utf-8 -*-
"""Repose les champs turcs perdus (voir relecture_tr/suspects.md).

    python tests/patch_tr_perdus.py corrections/adverbe_B1.json
    python tests/patch_tr_perdus.py corrections/*.json --verifier

CE QU'IL REPARE. 673 entrees d'`adverbe.json` et `redewendung.json`, aux
niveaux B1, B2 et C1, portent UN SEUL CARACTERE en guise de traduction turque
-- « bereits » traduit par « c ». Nees ainsi en v364, jamais correctes.

LA FORME D'UN FICHIER DE CORRECTIONS

    {
      "fichier": "adverbe.json",
      "niveau": "B1",
      "entrees": [
        {"mot": "bereits", "traduction_tr": "zaten",
         "exemple_tr": "Kayit suresi zaten dolmus."}
      ]
    }

LE GARDE-FOU D'ALLER-RETOUR, ET POURQUOI IL N'EST PAS NEGOCIABLE. Avant
d'ecrire quoi que ce soit, on relit le fichier, on le re-serialise avec les
memes options, et on exige l'egalite OCTET POUR OCTET avec ce qui est sur le
disque. Si ca ne correspond pas, on s'arrete sans rien toucher : sinon le diff
part en reformatage complet et la vraie modification s'y perd -- on ne peut
plus relire ce qu'on a change, ni le defaire proprement.

ON NE REMPLACE QUE DU PERDU. Une entree dont le champ turc fait plus d'un
caractere n'est pas ecrasee, meme si le fichier de corrections en propose une
autre : ce script repare une perte, il n'arbitre pas une traduction. Ce qu'il
refuse est affiche, pas avale en silence.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]

# Un mot turc d'un seul caractere n'existe pas ; une phrase de moins de huit
# caracteres non plus. Memes seuils que relecture_tr.py --suspects.
def perdu(valeur, phrase=False):
    v = (valeur or "").strip()
    return len(v) < 8 if phrase else len(v) <= 1


def lire_json(chemin):
    return json.load(io.open(chemin, encoding="utf-8"))


def serialiser(donnees):
    return json.dumps(donnees, ensure_ascii=False, indent=2) + "\n"


def controle_aller_retour(chemin, donnees):
    """Le fichier se reproduit-il a l'octet pres ? Sinon on ne touche a rien."""
    sur_disque = io.open(chemin, encoding="utf-8", newline="").read()
    refait = serialiser(donnees)
    if sur_disque == refait:
        return True, ""
    # On dit OU ca diverge : sans ca, le message est inexploitable.
    n = min(len(sur_disque), len(refait))
    i = 0
    while i < n and sur_disque[i] == refait[i]:
        i += 1
    return False, ("premiere divergence a l'octet %d\n    disque : %r\n    refait : %r"
                   % (i, sur_disque[max(0, i - 40):i + 40],
                      refait[max(0, i - 40):i + 40]))


def appliquer(chemin_corrections, verifier_seulement):
    corr = lire_json(chemin_corrections)
    nom_fichier = corr["fichier"]
    niveau = corr["niveau"]
    chemin = os.path.join(RACINE, nom_fichier)

    donnees = lire_json(chemin)
    ok, detail = controle_aller_retour(chemin, donnees)
    if not ok:
        print("  ! %s ne se reproduit pas a l'identique -- ABANDON" % nom_fichier)
        print("    %s" % detail)
        return 1

    if niveau not in donnees:
        print("  ! niveau %s absent de %s" % (niveau, nom_fichier))
        return 1
    index = {}
    for m in donnees[niveau]:
        index.setdefault(m.get("mot"), m)

    poses = refuses = absents = 0
    for e in corr["entrees"]:
        mot = e.get("mot")
        cible = index.get(mot)
        if cible is None:
            print("    absent du corpus : %s" % mot)
            absents += 1
            continue
        for champ, est_phrase in (("traduction_tr", False), ("exemple_tr", True)):
            neuf = e.get(champ)
            if not neuf:
                continue
            if not perdu(cible.get(champ), est_phrase):
                print("    deja rempli, non ecrase : %s.%s = %r"
                      % (mot, champ, cible.get(champ)))
                refuses += 1
                continue
            if perdu(neuf, est_phrase):
                print("    correction elle-meme trop courte, refusee : %s.%s = %r"
                      % (mot, champ, neuf))
                refuses += 1
                continue
            cible[champ] = neuf
            poses += 1

    print("  %-18s %s : %3d champ(s) pose(s)%s%s"
          % (nom_fichier, niveau, poses,
             (", %d refuse(s)" % refuses) if refuses else "",
             (", %d absent(s)" % absents) if absents else ""))

    if verifier_seulement:
        print("    (--verifier : rien n'a ete ecrit)")
        return 0
    if not poses:
        return 0
    with io.open(chemin, "w", encoding="utf-8", newline="") as f:
        f.write(serialiser(donnees))
    return 0


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    verifier = "--verifier" in sys.argv
    if not args:
        print(__doc__)
        return 1
    code = 0
    for chemin in args:
        code = appliquer(chemin, verifier) or code
    return code


if __name__ == "__main__":
    sys.exit(main())
