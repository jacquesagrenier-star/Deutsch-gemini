# -*- coding: utf-8 -*-
"""Fabrique plusieurs DICTIONS d'une meme replique, pour choisir a l'oreille.

    python audio/essai_diction.py --scene 02-beim-buergeramt --plan 8
    python audio/essai_diction.py --scene 02-beim-buergeramt --plan 8 --pour-de-vrai

POURQUOI CET OUTIL EXISTE
    Le 15 septembre 2026, Jacques a ecoute les deux prises du plan 8 et
    tranche : la v3 avec [surprised] sonne AGRESSIVE, pas etonnee. La balise
    a depasse la cible. Mais la v2 neutre tombe a plat -- il veut « une
    question dans la voix, comme si c'etait bizarre, mais sans agressivite ».

    ⚠️ ON RESTE EN v2, ET CE N'EST PAS NEGOCIABLE. Dix-huit des dix-neuf
    repliques y sont ; melanger deux modeles dans une scene est un defaut
    documente -- timbre et prosodie ne se recollent pas. La direction de jeu
    doit donc venir d'ailleurs que d'une balise, que v2 PRONONCERAIT au lieu
    de la jouer.

LES DEUX SEULS LEVIERS QUE v2 OFFRE, ET ILS SONT REELS
    1. LA PONCTUATION. C'est elle qui porte l'intonation. « Ich wohne doch
       schon hier. » descend ; « Ich wohne doch schon hier? » monte. Les
       points de suspension ouvrent une hesitation avant la montee.
    2. LE CONTEXTE (previous_text / next_text). v2 l'accepte -- v3 le refuse.
       Le modele enchaine la prosodie au lieu de repartir de zero.

⚠️ CE QU'ON MODIFIE N'EST PAS LE TEXTE DE LA SCENE. Un point d'interrogation
    sur une phrase declarative est une convention de DICTION : il dit au
    modele de monter. A l'ecran, l'apprenant doit lire l'allemand correct de
    la scene. D'ou le champ `de_diction`, lu par la synthese SEULEMENT --
    `de` continue de nourrir les sous-titres et le lexique. Sans cette
    separation, on apprendrait une ponctuation fausse a l'apprenant pour
    regler un probleme de comedien.

⚠️ RIEN N'EST ECRIT DANS LA SCENE NI DANS LE MONTAGE. Les essais sortent dans
    _essais-diction/ et ne remplacent rien. C'est l'oreille de Jacques qui
    tranche ensuite -- toutes les anomalies de voix de ce projet ont ete
    trouvees par elle, aucune par une mesure.
"""
import argparse
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                                             # noqa: E402
import normaliser                                          # noqa: E402

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


# --------------------------------------------------------------------------
# Les dictions ecrites pour une replique precise.
# --------------------------------------------------------------------------
# ⚠️ LES VARIANTES GENERIQUES PLUS BAS CHERCHENT L'ETONNEMENT -- elles ont ete
# ecrites pour le plan 08, ou la question etait << est-ce que ca monte ? >>.
# Pour les quatre repliques de Mark, la question est autre : Jacques a demande
# de l'HUMOUR et de la LEGERETE, << que ca reste leger >>, et un personnage
# auquel on s'attache. Une montee interrogative n'y repond pas.
#
# ⚠️ ET v2 NE SAIT PAS RIRE. Un demi-rire ne s'obtient pas par la ponctuation ;
# une balise serait PRONONCEE. Ce que la ponctuation peut faire, c'est poser
# une respiration avant le mot qui bat Mark, laisser tomber une phrase au lieu
# de la durcir, ou suspendre un calcul pour que l'absurdite s'entende. C'est
# la limite honnete de ce qu'on essaie ici -- si rien ne convient, la question
# devient << passe-t-on ce plan-la en v3 >>, et c'est une autre decision.
DICTIONS = {
    ("02-beim-buergeramt", 5): [
        ("a-tel-quel", "Nein. Kann ich heute einen bekommen?",
         "la prise actuelle, pour comparer dans les memes conditions"),
        ("b-reprise", "Nein … Kann ich heute einen bekommen?",
         "un temps de reprise apres le << non >> : il encaisse, puis il rebondit"),
        ("c-leger", "Nein. Kann ich heute einen bekommen, vielleicht?",
         "il demande comme on demande quand on croit que ca va s'arranger"),
    ],
    ("02-beim-buergeramt", 10): [
        ("a-tel-quel", "Vierzehn Tage. Und der Termin ist in sechs Wochen.",
         "la prise actuelle"),
        ("b-suspens", "Vierzehn Tage … Und der Termin ist in sechs Wochen.",
         "le calcul s'arrete au milieu : l'absurdite tombe dans le silence"),
        ("c-complice", "Vierzehn Tage. Und der Termin ist in sechs Wochen …?",
         "il enonce et attend qu'on la corrige -- << vous l'entendez aussi ? >>"),
    ],
    ("02-beim-buergeramt", 14): [
        ("a-tel-quel", "Welche Papiere brauche ich?",
         "la prise actuelle"),
        ("b-pratique", "Also, welche Papiere brauche ich?",
         "il tourne la page et redevient pratique : plus leger que resigne"),
    ],
    ("02-beim-buergeramt", 16): [
        ("a-tel-quel", "Die … was, bitte?",
         "la prise actuelle"),
        ("b-abandon", "Die Wohnungs … was, bitte?",
         "il ESSAIE le mot et abandonne en route -- l'echec s'entend"),
        ("c-deux-temps", "Die …? Was, bitte?",
         "deux questions au lieu d'une : il renonce, puis il redemande"),
        ("d-sourire", "Die … was, bitte …?",
         "la fin retombe au lieu de durcir : le demi-sourire plutot que l'agacement"),
    ],
}


def variantes(de, scene=None, plan=None):
    """Les dictions a essayer -- ecrites pour la replique si on les a."""
    sur_mesure = DICTIONS.get((scene, plan))
    if sur_mesure:
        return sur_mesure
    base = de.rstrip()
    sans_point = base[:-1] if base.endswith((".", "!", "?")) else base
    # ⚠️ TOUTES LES VARIANTES RESTENT DE L'ALLEMAND ECRIVABLE. Une ponctuation
    # malformee -- « Sechs Wochen?, Ich wohne… » -- ne donne pas une diction
    # intermediaire, elle donne une prise dont on ne peut rien conclure. Le
    # premier essai en contenait une ; elle est retiree avant d'avoir coute un
    # credit.
    tete, reste = (base.split("? ", 1) + [""])[:2] if "? " in base else (base, "")
    return [
        ("a-tel-quel", base,
         "la prise actuelle, pour comparer dans les memes conditions"),
        ("b-question", sans_point + "?",
         "toute la replique monte : l'etonnement porte jusqu'au bout"),
        ("c-suspension", sans_point + " …?",
         "affirmation, puis une montee retenue -- « c'est bizarre » sans hausser le ton"),
        ("d-tete", (tete + " …? " + reste) if reste else base,
         "l'etonnement se pose sur le NOMBRE, la suite reste calme"),
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", required=True)
    ap.add_argument("--plan", type=int, required=True)
    ap.add_argument("--pour-de-vrai", action="store_true")
    a = ap.parse_args()

    fs = os.path.join(RACINE, "scenes", a.scene + ".json")
    d = json.load(io.open(fs, encoding="utf-8"))
    plans = d["plans"]
    p = next((x for x in plans if x["n"] == a.plan), None)
    if not p:
        sys.exit("  plan %d absent de %s" % (a.plan, a.scene))

    # Le contexte, comme scene_audio.py le passe : les repliques voisines.
    def texte(n):
        v = next((x for x in plans if x["n"] == n), None)
        return (v or {}).get("de") or None
    avant, apres = texte(a.plan - 1), texte(a.plan + 1)

    dossier = os.path.join(RACINE, "audio", "scenes", a.scene)
    fm = os.path.join(dossier, "manifeste.json")
    man = json.load(io.open(fm, encoding="utf-8"))
    modele = man["modele"]
    if modele != generer.MODELES["v2"][0]:
        sys.exit("  cette scene n'est pas en v2 (%s) : la ponctuation n'est "
                 "pas le bon levier, voir les balises." % modele)
    # ⚠️ LE GAIN NE SE RECALCULE PAS -- meme raison que dans refaire_plan.py :
    # il est mesure sur la scene entiere, pas sur un fichier.
    gain = man["gain_applique_db"]
    # Les reglages de la scene, pas ceux du corpus : scene_audio.py les a
    # ouverts (stability 0,4 / style 0,45) pour laisser respirer le jeu.
    generer.REGLAGES = dict(man["reglages"])

    # ⚠️ CHAQUE LOCUTEUR A SA VOIX, ET LE MODULE N'EN SAIT RIEN.
    # generer.VOIX vaut par defaut celle de l'ERZAEHLER. scene_audio.py la
    # remplace avant chaque replique ; la premiere version de ce script ne le
    # faisait pas, et les quatre prises du 15 septembre sont sorties avec le
    # narrateur disant le texte de Mark. Jacques l'a entendu en une ecoute --
    # aucune mesure ne l'aurait vu, le fichier etait valide et a la bonne
    # duree. Un defaut de casting ne ressemble pas a une panne.
    locuteurs = d.get("locuteurs") or {}
    fiche = locuteurs.get(p["locuteur"]) or {}
    voix = fiche.get("voice_id")
    if not voix:
        sys.exit("  « %s » n'a pas de voice_id dans %s.json : on s'arrete AVANT "
                 "de depenser." % (p["locuteur"], a.scene))
    generer.VOIX = voix

    sortie = os.path.join(dossier, "_essais-diction")
    liste = variantes(p["de"], a.scene, a.plan)
    print("  plan %d · %s · voix %s (%s)"
          % (a.plan, p["locuteur"], voix, fiche.get("nom", "?")))
    print("  contexte  avant : %s" % (avant or "(aucun)"))
    print("            apres : %s" % (apres or "(aucun)"))
    print("  reglages  %s | gain %+.2f dB" % (man["reglages"], gain))
    print()
    for nom, texte_dit, pourquoi in liste:
        print("  %-14s %-46s %s" % (nom, texte_dit, pourquoi))
    total = sum(len(t) for _, t, _ in liste)
    print()
    print("  %d variantes, %d caracteres -> environ %d credits"
          % (len(liste), total, total))
    if not a.pour_de_vrai:
        print("\n  (essai a blanc -- relancer avec --pour-de-vrai)")
        return

    os.makedirs(sortie, exist_ok=True)
    cle = generer.cle_api()
    # Le meme filtre que refaire_plan.py : le gain de scene, puis le limiteur
    # qui empeche un pic de depasser -1 dBFS. Pas de nouvelle mesure de sonie.
    normaliser.FF = normaliser.ffmpeg()
    filtre = "volume=%.2fdB,alimiter=limit=0.891" % gain
    for nom, texte_dit, _ in liste:
        brut = os.path.join(sortie, "%02d-%s-brut.mp3" % (a.plan, nom))
        # ⚠️ ON NE REGENERE PAS UN BRUT DEJA LA. Le premier passage du
        # 15 septembre a produit un brut puis s'est arrete sur un mauvais nom
        # de fonction ; le relancer aurait repaye la meme prise -- et v2 n'est
        # pas deterministe hors graine, donc on aurait AUSSI perdu la prise.
        if not os.path.exists(brut):
            octets = generer.synthetiser(texte_dit, modele, cle,
                                         avant=avant, apres=apres)
            io.open(brut, "wb").write(octets)
        final = os.path.join(sortie, "%02d-%s.mp3" % (a.plan, nom))
        if not normaliser._ff(brut, final, filtre):
            sys.exit("  ffmpeg a echoue sur %s" % nom)
        print("  ecrit : %-22s %.2f s"
              % (os.path.basename(final), normaliser.duree(final)))
    print("\n  Rien n'a ete remplace. Ecoute, puis dis lequel.")


main()
