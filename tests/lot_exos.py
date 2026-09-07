# -*- coding: utf-8 -*-
"""Extraire et poser une langue dans exercices.json.

exercices.json n'est pas du vocabulaire : ce sont 1 682 exercices, chacun
avec sa question, sa traduction, son indice et son explication. lot_langue.py
ne sait pas les lire -- il connait cinq fichiers de cartes, pas celui-la.

    python tests/lot_exos.py --etat
    python tests/lot_exos.py --langue fa --jeu perfektExercises --taille 40
    python tests/lot_exos.py --langue fa --poser corrections_fa/exos_perfekt_01.json

Le fichier de correction a la meme forme que ceux de corrections_fa/ :

    { "jeu": "perfektExercises",
      "entrees": [ {"question": "<la question ALLEMANDE, telle quelle>",
                    "translation_fa": "...", "hint_fa": "...",
                    "explanation_fa": "..."} ] }

La question allemande sert de cle : elle est deja unique dans un jeu, et
elle rend le fichier de correction lisible sans compter les rangs.

GARDE-FOU : comme patch_langue.py, on exige que le fichier se reproduise a
l'octet pres AVANT toute modification. Un exercices.json reecrit avec une
autre indentation ferait un diff de 1,6 Mo ou personne ne verrait rien.
"""
import argparse
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHEMIN = os.path.join(RACINE, "exercices.json")

# Les champs traduits, et leur suffixe. correct/options suivent la casse
# chameau (correctEn, optionsTr) : deux conventions dans le meme objet, comme
# partout ailleurs dans ce projet.
CHAMPS_SOULIGNE = ["question", "translation", "hint", "explanation"]
CHAMPS_CHAMEAU = ["correct", "options"]

CHAMEAU = {"fr": "", "en": "En", "tr": "Tr", "uk": "Uk", "fa": "Fa"}


def cle_souligne(base, langue):
    return base if langue == "fr" else base + "_" + langue


def cle_chameau(base, langue):
    return base + CHAMEAU[langue]


def lire():
    brut = io.open(CHEMIN, encoding="utf-8", newline="").read()
    return json.loads(brut), brut


def serialiser(donnees, brut):
    """Meme mise en forme que le fichier sur disque, saut final compris.

    exercices.json est COMPACT (1,6 Mo sans indentation) la ou les cinq
    fichiers de vocabulaire sont indentes. On releve la convention du
    fichier au lieu d'en imposer une -- le reserialiser autrement ferait
    un diff ou personne ne verrait la traduction ajoutee."""
    if brut.startswith("{\n"):
        texte = json.dumps(donnees, ensure_ascii=False, indent=2)
    else:
        texte = json.dumps(donnees, ensure_ascii=False, separators=(",", ":"))
    return texte + "\n" if brut.endswith("\n") else texte


def controle_aller_retour(donnees, brut):
    refait = serialiser(donnees, brut)
    if refait == brut:
        return True, ""
    n = min(len(brut), len(refait))
    i = 0
    while i < n and brut[i] == refait[i]:
        i += 1
    return False, ("premiere divergence a l'octet %d\n    disque : %r\n    refait : %r"
                   % (i, brut[max(0, i - 40):i + 40], refait[max(0, i - 40):i + 40]))


def a_faire(exo, langue):
    """L'exercice manque-t-il d'une traduction dans cette langue ?

    On ne reclame que ce que le TURC possede deja : un exercice sans
    hint_tr n'a pas d'indice du tout, en reclamer un en persan
    inventerait du contenu qui n'existe dans aucune langue."""
    for base in CHAMPS_SOULIGNE:
        if exo.get(cle_souligne(base, "tr")) and not exo.get(cle_souligne(base, langue)):
            return True
    for base in CHAMPS_CHAMEAU:
        if exo.get(cle_chameau(base, "tr")) and not exo.get(cle_chameau(base, langue)):
            return True
    return False


def etat(donnees, langue):
    total = reste = 0
    for nom, liste in sorted(donnees["jeux"].items()):
        n = sum(1 for e in liste if a_faire(e, langue))
        total += len(liste)
        reste += n
        if n:
            print("   %-40s %4d a faire sur %4d" % (nom, n, len(liste)))
    faites = total - reste
    print("   ---")
    print("   %s : %d exercices a faire sur %d (%.1f %% faits)"
          % (langue, reste, total, 100.0 * faites / total if total else 100.0))


def extraire(donnees, langue, jeu, taille):
    liste = donnees["jeux"].get(jeu)
    if liste is None:
        print("jeu inconnu : %s" % jeu)
        sys.exit(1)
    manquants = [e for e in liste if a_faire(e, langue)]
    print("# %s : %d a faire" % (jeu, len(manquants)))
    for exo in manquants[:taille]:
        bouts = ["Q: " + exo.get("question", "")]
        # Une question identique d'un exercice a l'autre (« Remets les mots
        # dans le bon ordre ») ne peut pas servir de cle a elle seule : on
        # ajoute la traduction francaise, qui, elle, distingue.
        if len([e for e in liste if e.get("question") == exo.get("question")]) > 1:
            bouts.append("CLE-TRAN: " + exo.get("translation", ""))
        for base in CHAMPS_SOULIGNE[1:]:
            fr = exo.get(base, "")
            if exo.get(cle_souligne(base, "tr")) and fr:
                bouts.append("%s: %s" % (base[:4].upper(), fr))
        for base in CHAMPS_CHAMEAU:
            if exo.get(cle_chameau(base, "tr")):
                v = exo.get(cle_chameau(base, "tr"))
                bouts.append("%s(tr): %s" % (base[:4].upper(), v if isinstance(v, str)
                                             else " | ".join(v)))
        print(" || ".join(bouts))


def poser(donnees, brut, langue, chemin_corr, remplacer):
    corr = json.load(io.open(chemin_corr, encoding="utf-8"))
    jeu = corr["jeu"]
    liste = donnees["jeux"].get(jeu)
    if liste is None:
        print("jeu inconnu : %s" % jeu)
        sys.exit(1)
    par_question = {}
    for exo in liste:
        par_question.setdefault(exo.get("question", ""), []).append(exo)

    poses = 0
    absents = []
    for entree in corr["entrees"]:
        q = entree["question"]
        cibles = par_question.get(q) or []
        # « cle_translation » est la traduction FRANCAISE, utilisee comme
        # second discriminant la ou la question se repete a l'identique.
        if entree.get("cle_translation"):
            cibles = [e for e in cibles if e.get("translation") == entree["cle_translation"]]
        if not cibles:
            absents.append(q + (" || " + entree["cle_translation"]
                                if entree.get("cle_translation") else ""))
            continue
        if len(cibles) > 1 and not entree.get("cle_translation"):
            print("QUESTION AMBIGUE (%d exercices), ajoute \"cle_translation\" : %s"
                  % (len(cibles), q))
            sys.exit(1)
        for exo in cibles:
            for base in CHAMPS_SOULIGNE:
                k = base + "_" + langue
                if k in entree and entree[k] and (remplacer or not exo.get(k)):
                    exo[k] = entree[k]
                    poses += 1
            for base in CHAMPS_CHAMEAU:
                k = base + CHAMEAU[langue]
                if k in entree and entree[k] and (remplacer or not exo.get(k)):
                    exo[k] = entree[k]
                    poses += 1

    if absents:
        print("ABSENTS DU JEU :")
        for q in absents:
            print("   " + q)
        sys.exit(1)

    io.open(CHEMIN, "w", encoding="utf-8", newline="").write(serialiser(donnees, brut))
    print("  %-24s %s : %3d champ(s) pose(s)" % (jeu, langue, poses))


def recopier_formes(donnees, brut, langue):
    """Les tuiles de reponse qui sont de l'ALLEMAND, pas de la traduction.

    Dans la moitie des jeux, correct/options portent des formes allemandes
    (« dieser », « diesem »...) et correctTr vaut exactement correct : le
    turc n'a rien traduit, il a recopie. Les redemander en persan ferait
    retaper des centaines de mots allemands, avec le risque de faute que
    cela suppose. On recopie donc, et on ne laisse au traducteur que les
    tuiles REELLEMENT traduites."""
    poses = 0
    paires = ([(b, cle_souligne, cle_souligne) for b in CHAMPS_SOULIGNE]
              + [(b, cle_chameau, cle_chameau) for b in CHAMPS_CHAMEAU])
    for liste in donnees["jeux"].values():
        for exo in liste:
            for base, _, cle in paires:
                fr = exo.get(base)
                tr = exo.get(cle(base, "tr"))
                cible = cle(base, langue)
                if fr is None or tr is None or exo.get(cible):
                    continue
                if tr == fr:
                    exo[cible] = fr if isinstance(fr, str) else list(fr)
                    poses += 1
    io.open(CHEMIN, "w", encoding="utf-8", newline="").write(serialiser(donnees, brut))
    print("  %d tuile(s) allemande(s) recopiee(s) en %s" % (poses, langue))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langue", default="fa")
    ap.add_argument("--etat", action="store_true")
    ap.add_argument("--jeu")
    ap.add_argument("--taille", type=int, default=40)
    ap.add_argument("--poser")
    ap.add_argument("--remplacer", action="store_true")
    ap.add_argument("--recopier-formes", dest="recopier", action="store_true")
    a = ap.parse_args()

    donnees, brut = lire()
    ok, detail = controle_aller_retour(donnees, brut)
    if not ok:
        print("ALLER-RETOUR REFUSE, rien n'a ete touche :\n    " + detail)
        sys.exit(1)

    if a.etat:
        etat(donnees, a.langue)
    elif a.recopier:
        recopier_formes(donnees, brut, a.langue)
    elif a.poser:
        poser(donnees, brut, a.langue, a.poser, a.remplacer)
    elif a.jeu:
        extraire(donnees, a.langue, a.jeu, a.taille)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
