# -*- coding: utf-8 -*-
"""Repose les champs turcs perdus (voir relecture_tr/suspects.md).

    python tests/patch_tr_perdus.py corrections/adverbe_B1.json
    python tests/patch_tr_perdus.py corrections/*.json --verifier

CE QU'IL REPARE. 673 entrees d'`adverbe.json` et `redewendung.json`, aux
niveaux B1, B2 et C1, portent UN SEUL CARACTERE en guise de traduction turque
-- « bereits » traduit par « c ». Nees ainsi en v364, jamais correctes.

IL TRAITE LES CINQ FICHIERS. adverbe, adjectif et redewendung ont la meme
forme ; verbe.json porte son mot sous `infinitif` et non `mot` ; themes.json
range ses mots dans des themes, et c'est le THEME qui porte le niveau. Voir
indexer() -- c'est le seul endroit ou cette difference apparait.

UN MOT PRESENT PLUSIEURS FOIS EST CORRIGE PARTOUT. « Fachmann » figure dans
« Berufe » et dans le chapitre 15 du manuel : les deux recoivent la meme
traduction. Lui en donner deux selon le paquet serait un defaut pire que
celui qu'on repare.

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

`--remplacer` LEVE CE REFUS, ET N'EST PAS UN CONFORT. Il sert au seul cas ou
la reparation elle-meme doit etre corrigee : `--collisions` a montre qu'une
reponse fraichement posee en doublait une autre, et il faut la remplacer. Ne
jamais l'employer pour un lot entier -- le refus est justement ce qui empeche
d'ecraser en masse des traductions qui allaient bien.
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


# LE SAUT DE LIGNE FINAL N'EST PAS LE MEME PARTOUT. Quatre fichiers en ont un,
# themes.json n'en a pas. Le garde-fou d'aller-retour l'a vu du premier coup --
# c'est precisement ce qu'on lui demande -- mais l'imposer aurait reecrit le
# dernier octet du fichier au passage. On releve donc la convention du fichier
# au lieu d'en decider une.
def serialiser(donnees, saut_final=True):
    texte = json.dumps(donnees, ensure_ascii=False, indent=2)
    return texte + "\n" if saut_final else texte


def controle_aller_retour(chemin, donnees, saut_final):
    """Le fichier se reproduit-il a l'octet pres ? Sinon on ne touche a rien."""
    sur_disque = io.open(chemin, encoding="utf-8", newline="").read()
    refait = serialiser(donnees, saut_final)
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


# TROIS FORMES DE FICHIER, UN SEUL POINT OU CA SE VOIT.
#
#   adverbe / adjectif / redewendung : { "A1": [ {mot, ...} ], ... }
#   verbe                            : { "A1": [ {infinitif, ...} ], ... }
#   themes                           : { "themes": [ {niveau, mots:[...]} ] }
#
# Le champ "niveau" du fichier de corrections sert de filtre dans les trois
# cas ; pour themes.json il filtre les THEMES, la cle etant portee par le
# theme et non par le mot.
#
# UN MOT PEUT FIGURER DANS PLUSIEURS THEMES, et c'est frequent : « Fachmann »
# est a la fois dans « Berufe » et dans le chapitre 15 du manuel. Toutes ses
# occurrences sont alors modifiees, et c'est le seul comportement correct --
# un meme mot allemand qui recevrait deux traductions turques selon le paquet
# ou on le rencontre serait un defaut pire que celui qu'on repare.
#
# L'index rend donc TOUJOURS une liste, meme quand elle ne contient qu'un
# element : c'est ce qui evite d'avoir deux chemins d'ecriture a maintenir.
def indexer(donnees, nom_fichier, niveau):
    index = {}
    if nom_fichier == "themes.json":
        themes = donnees.get("themes", donnees)
        vu_niveau = False
        for t in themes:
            if t.get("niveau") != niveau:
                continue
            vu_niveau = True
            for m in t.get("mots", []):
                index.setdefault(m.get("mot"), []).append(m)
        if not vu_niveau:
            return None, "aucun theme de niveau %s dans themes.json" % niveau
        return index, None

    if niveau not in donnees:
        return None, "niveau %s absent de %s" % (niveau, nom_fichier)
    champ = "infinitif" if nom_fichier == "verbe.json" else "mot"
    for m in donnees[niveau]:
        index.setdefault(m.get(champ), []).append(m)
    return index, None


def appliquer(chemin_corrections, verifier_seulement, remplacer=False):
    corr = lire_json(chemin_corrections)
    nom_fichier = corr["fichier"]
    niveau = corr["niveau"]
    chemin = os.path.join(RACINE, nom_fichier)

    donnees = lire_json(chemin)
    saut_final = io.open(chemin, encoding="utf-8", newline="").read().endswith("\n")
    ok, detail = controle_aller_retour(chemin, donnees, saut_final)
    if not ok:
        print("  ! %s ne se reproduit pas a l'identique -- ABANDON" % nom_fichier)
        print("    %s" % detail)
        return 1

    index, err = indexer(donnees, nom_fichier, niveau)
    if err:
        print("  ! %s" % err)
        return 1

    poses = refuses = absents = 0
    for e in corr["entrees"]:
        mot = e.get("mot")
        cibles = index.get(mot)
        if not cibles:
            print("    absent du corpus : %s" % mot)
            absents += 1
            continue
        # TOUS LES CHAMPS TURCS, PAS SEULEMENT LES DEUX PREMIERS. Une carte de
        # verbe en porte cinq -- le verbe et ses quatre temps -- et le premier
        # verdict de relecture a signale une phrase au preterit. On prend donc
        # ce que le fichier de corrections nomme, quel que soit le champ,
        # plutot qu'une liste figee ici.
        champs = [k for k in e if k.endswith("_tr")]
        for cible in cibles:
            for champ in champs:
                est_phrase = champ != "traduction_tr"
                neuf = e.get(champ)
                if not neuf:
                    continue
                if not perdu(cible.get(champ), est_phrase) and not remplacer:
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
        f.write(serialiser(donnees, saut_final))
    return 0


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  errors="replace")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    verifier = "--verifier" in sys.argv
    remplacer = "--remplacer" in sys.argv
    if not args:
        print(__doc__)
        return 1
    code = 0
    for chemin in args:
        code = appliquer(chemin, verifier, remplacer) or code
    return code


if __name__ == "__main__":
    sys.exit(main())
