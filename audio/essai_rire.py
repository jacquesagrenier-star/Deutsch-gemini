# -*- coding: utf-8 -*-
"""Le rire : ce que v2 ne sait pas faire et que v3 sait, sur UNE replique.

    python audio/essai_rire.py --scene 02-beim-buergeramt --plan 16
    python audio/essai_rire.py --scene 02-beim-buergeramt --plan 16 --pour-de-vrai

POURQUOI CE SCRIPT EXISTE, ET IL EXISTE PARCE QUE JE ME SUIS TROMPE.

Le 16 septembre 2026, j'ai ecrit a Jacques que << la v2 ne sait pas rire >> en
laissant entendre que le rire etait hors de portee. Sa reponse : << je ne
comprends pas la limite au niveau du rire ; j'ai vu des videos ou les
personnages rient a gorge deployee. >>

Il a raison, et ma phrase etait fausse par omission. Ce qui est vrai :

    eleven_multilingual_v2  PRONONCE les balises. << [laughs] >> sort en
                            toutes lettres. C'est le modele de cette scene.
    eleven_v3               LIT les balises comme une direction de jeu --
                            [laughs], [chuckles], [sighs]. C'est ce qu'on
                            entend dans les videos dont il parle.

La limite n'est donc pas le rire : c'est LE MELANGE. Dix-huit des dix-neuf
repliques de la scene sont en v2, et melanger deux modeles dans une meme scene
est un defaut documente ici -- timbre et prosodie ne se recollent pas.

⚠️ ET LE PRECEDENT DU PLAN 08 NE DIT PAS CE QU'ON CROIT. La v3 y avait sonne
   AGRESSIVE, et on en avait conclu que v3 ne convenait pas. Le journal de ce
   jour-la est plus precis : << ce n'est pas "la surprise ne s'entend pas",
   c'est "la balise a depasse la cible" >> -- [surprised] a stability 0.0.
   Une balise a stabilite nulle sur-joue ; la meme a 0.5 se tient. On essaie
   donc la balise ET la stabilite, pas la balise seule.

CE QUE CE SCRIPT NE FAIT PAS : il ne remplace rien, il n'ecrit ni dans la
scene ni dans le montage. Il pose des fichiers a ecouter. C'est l'oreille de
Jacques qui tranche -- toutes les anomalies de voix de ce projet ont ete
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

# (nom, texte, stabilite, ce qu'on cherche)
#
# ⚠️ LA BALISE SE MET LA OU LE RIRE ARRIVE, PAS EN TETE. Une balise en tete
# colore toute la replique ; ici l'amusement doit venir APRES l'echec, jamais
# avant -- c'est la note de direction du plan 16 : << le demi-sourire ne doit
# pas etre la au debut >>.
def essais(de):
    return [
        ("v3-nu",        de,                     0.5,
         "v3 sans balise : entendre d'abord ce que le modele change TOUT SEUL"),
        ("v3-chuckles",  de + " [chuckles]",     0.5,
         "un petit rire APRES la question -- il rit de lui-meme"),
        ("v3-amused",    "[amused] " + de,       0.5,
         "l'amusement colore toute la replique, sans rire audible"),
        ("v3-laughs",    de + " [laughs]",       0.5,
         "franchement drole : le rire est la, pas seulement le sourire"),
        ("v3-chuckles-souple", de + " [chuckles]", 0.3,
         "meme balise, moins de tenue : plus joue, au risque du sur-jeu"),
    ]


# --------------------------------------------------------------------------
# LA BASCULE DE MARK EN v3 (16 septembre 2026, choix B de Jacques).
# --------------------------------------------------------------------------
# Mark passe en v3, le fonctionnaire et le narrateur restent en v2. La raison
# n'est pas l'argent : c'est Mark qui porte l'humour et l'attachement, et le
# fonctionnaire DOIT rester neutre -- une balise d'emotion serait contre son
# personnage. Le melange de modeles tombe donc entre DEUX VOIX DIFFERENTES,
# la ou il ne s'entend pas, au lieu d'etre a l'interieur d'une meme voix.
#
# ⚠️ LA STABILITE EST A 0.5, ET C'EST LA LECON DU PLAN 08. Le 15 septembre,
# [surprised] a stability 0.0 avait donne de l'indignation, pas de
# l'etonnement -- << la balise a depasse la cible >>. Une balise ne se juge
# jamais sans sa stabilite.
#
# ⚠️ ET LE PLAN 03 N'A PAS DE BALISE, EXPRES. C'est la ligne de base : Mark y
# est prepare et un peu fier de l'etre. Tout le contraste de l'episode se
# mesure a partir de la ; la colorer, c'est perdre l'echelle.
MARK_V3 = {
    3:  [("nu", "Guten Tag. Ich möchte mich anmelden.", 0.5,
          "la ligne de base, sans balise : prepare, pas encore surpris")],
    5:  [("curieux", "Nein. [curious] Kann ich heute einen bekommen?", 0.5,
          "la premiere fissure, mais il croit encore que ca s'arrange"),
         ("espoir", "Nein. [hopeful] Kann ich heute einen bekommen?", 0.5,
          "la meme, en plus ouvert")],
    8:  [("surpris", "[surprised] Sechs Wochen? Ich wohne doch schon hier.", 0.5,
          "la balise que la v3 avait sur-jouee a stabilite 0 -- ici tenue a 0,5"),
         ("incredule", "Sechs Wochen? [confused] Ich wohne doch schon hier.", 0.5,
          "l'incredulite arrive APRES le nombre, comme la diction retenue hier")],
    10: [("amuse", "[amused] Vierzehn Tage. Und der Termin ist in sechs Wochen.", 0.5,
          "il trouve le calcul drole avant de le trouver injuste"),
         ("sec", "Vierzehn Tage. Und der Termin ist in sechs Wochen.", 0.5,
          "sans balise : v3 seul, pour mesurer ce qu'ajoute la balise")],
    14: [("pratique", "Welche Papiere brauche ich?", 0.5,
          "pratique et leger : rien a colorer")],
    16: [("rire", "Die … was, bitte? [chuckles]", 0.5,
          "le moment ou on l'adopte : il rit de lui-meme"),
         ("amuse", "[amused] Die … was, bitte?", 0.5,
          "amuse d'un bout a l'autre, sans rire audible")],
}


def bascule_mark(a, d, man, dossier, sortie, cle):
    """Les six repliques de Mark en v3, a ecouter avant de remplacer quoi que
    ce soit. ⚠️ RIEN N'EST INSTALLE ICI."""
    generer.VOIX = ((d.get("locuteurs") or {}).get("mark") or {})["voice_id"]
    modele = generer.MODELES["v3"][0]
    normaliser.FF = normaliser.ffmpeg()
    filtre = "volume=%.2fdB,alimiter=limit=0.891" % man["gain_applique_db"]
    total = sum(len(t) for v in MARK_V3.values() for _, t, _, _ in v)
    print("  %d essais sur %d repliques -> environ %d credits"
          % (sum(len(v) for v in MARK_V3.values()), len(MARK_V3), total))
    if not a.pour_de_vrai:
        print("\n  (essai a blanc -- relancer avec --pour-de-vrai)")
        return
    print()
    for n in sorted(MARK_V3):
        for nom, texte, stab, pourquoi in MARK_V3[n]:
            brut = os.path.join(sortie, "%02d-v3-%s-brut.mp3" % (n, nom))
            # ⚠️ NON VIDE, PAS SEULEMENT PRESENT. Un appel rate laisse un
            # fichier de 0 octet -- et le 16 septembre, ce fichier-la s'est
            # fait prendre pour une prise valide : cinq essais annonces, un
            # jamais produit, et Jacques a entendu << aucune difference >>.
            if not (os.path.exists(brut) and os.path.getsize(brut) > 1024):
                generer.REGLAGES = dict(man["reglages"])
                generer.REGLAGES["stability"] = stab
                io.open(brut, "wb").write(
                    generer.synthetiser(texte, modele, cle))
            final = os.path.join(sortie, "%02d-v3-%s.mp3" % (n, nom))
            if not normaliser._ff(brut, final, filtre):
                sys.exit("  ffmpeg a echoue sur %s" % nom)
            print("  %02d  %-10s %5.2f s   %s"
                  % (n, nom, normaliser.duree(final), pourquoi))
    print()
    print("  Rien n'a ete remplace. Ecoute, puis dis lesquelles.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", required=True)
    ap.add_argument("--plan", type=int)
    ap.add_argument("--mark", action="store_true",
                    help="les six repliques de Mark en v3 (bascule d'essai)")
    ap.add_argument("--pour-de-vrai", action="store_true")
    a = ap.parse_args()
    if a.mark:
        d = json.load(io.open(os.path.join(RACINE, "scenes",
                                           a.scene + ".json"), encoding="utf-8"))
        dossier = os.path.join(RACINE, "audio", "scenes", a.scene)
        man = json.load(io.open(os.path.join(dossier, "manifeste.json"),
                                encoding="utf-8"))
        sortie = os.path.join(dossier, "_essais-diction")
        if not os.path.isdir(sortie):
            os.makedirs(sortie)
        bascule_mark(a, d, man, dossier, sortie, generer.cle_api())
        return
    if not a.plan:
        sys.exit("  Preciser --plan N ou --mark.")

    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                          encoding="utf-8"))
    p = next((x for x in d["plans"] if x["n"] == a.plan), None)
    if not p:
        sys.exit("  plan %d absent de %s" % (a.plan, a.scene))

    fiche = (d.get("locuteurs") or {}).get(p["locuteur"]) or {}
    voix = fiche.get("voice_id")
    if not voix:
        sys.exit("  « %s » n'a pas de voice_id : on s'arrete AVANT de depenser."
                 % p["locuteur"])

    dossier = os.path.join(RACINE, "audio", "scenes", a.scene)
    man = json.load(io.open(os.path.join(dossier, "manifeste.json"),
                            encoding="utf-8"))
    gain = man["gain_applique_db"]
    sortie = os.path.join(dossier, "_essais-diction")
    if not os.path.isdir(sortie):
        os.makedirs(sortie)

    de = p.get("de_diction") or p["de"]
    liste = essais(de)
    print()
    print("  plan %d · %s · voix %s" % (a.plan, p["locuteur"], voix))
    print("  ⚠️ la scene est en %s ; ces essais sont en eleven_v3." % man["modele"])
    print("     Les ecouter A COTE d'une replique voisine, pas seuls : ce qu'on")
    print("     juge, c'est si le timbre se recolle, pas seulement si le rire")
    print("     est bon.")
    print()
    for nom, texte, stab, pourquoi in liste:
        print("  %-20s %-44s stab %.1f  %s" % (nom, texte, stab, pourquoi))
    n = sum(len(t) for _, t, _, _ in liste)
    print()
    print("  %d essais, %d caracteres -> environ %d credits" % (len(liste), n, n))
    if not a.pour_de_vrai:
        print()
        print("  (essai a blanc -- relancer avec --pour-de-vrai)")
        return

    generer.VOIX = voix
    modele = generer.MODELES["v3"][0]
    cle = generer.cle_api()
    normaliser.FF = normaliser.ffmpeg()
    # Le gain de la scene, pas un gain recalcule : il est mesure sur les
    # dix-neuf repliques ensemble. Un essai qu'on ecoute plus fort que ses
    # voisines se juge plus genereusement -- c'est la lecon de la ligne de
    # base de l'episode 1.
    filtre = "volume=%.2fdB,alimiter=limit=0.891" % gain
    print()
    for nom, texte, stab, _ in liste:
        # ⚠️ ON NE REGENERE PAS UN BRUT DEJA LA -- meme raison que dans
        # essai_diction.py : v3 n'est pas deterministe, relancer repaierait la
        # prise ET la perdrait.
        brut = os.path.join(sortie, "%02d-%s-brut.mp3" % (a.plan, nom))
        if not os.path.exists(brut):
            generer.REGLAGES = dict(man["reglages"])
            generer.REGLAGES["stability"] = stab
            # ⚠️ AUCUN CONTEXTE : v3 refuse previous_text / next_text (HTTP 400,
            # 14 septembre 2026). C'est le prix de la balise.
            io.open(brut, "wb").write(generer.synthetiser(texte, modele, cle))
        final = os.path.join(sortie, "%02d-%s.mp3" % (a.plan, nom))
        if not normaliser._ff(brut, final, filtre):
            sys.exit("  ffmpeg a echoue sur %s" % nom)
        print("  ecrit : %-26s %5.2f s" % (os.path.basename(final),
                                           normaliser.duree(final)))
    print()
    print("  Rien n'a ete remplace.")


if __name__ == "__main__":
    main()
