# -*- coding: utf-8 -*-
"""Fabrique un comparatif de voix A L'AVEUGLE, pret a faire ecouter.

    python audio/comparatif_voix.py --personnage marc
    python audio/comparatif_voix.py --personnage marc --sans-doublon

CE QUE FAIT LE SCRIPT
    Il prend les voix candidates listees dans audio/candidats_<personnage>.json,
    leur fait dire LES MEMES repliques, egalise la sonie, melange, et depose le
    tout sous des noms neutres -- VOIX-A, VOIX-B... -- avec un fichier de cle
    range a part. Celui qui ecoute ne peut pas savoir laquelle est laquelle.

POURQUOI A L'AVEUGLE
    Aurora a ete choisie ainsi le 3 septembre 2026 : six echantillons
    anonymises presentes a Barbara, dont l'un etait Nadja, la voix ALORS EN
    LIGNE. Elle l'a ecartee sans savoir que c'etait la notre. C'est le seul
    verdict qui vaille, parce qu'il ne peut pas etre poli par la politesse ni
    par le cout de changer d'avis. Voir a_ecouter_voix/CLE-du-comparatif.json.

POURQUOI LA SONIE EST EGALISEE AVANT, ET POURQUOI C'EST OBLIGATOIRE
    ElevenLabs sort entre -7 et -15 dBFS selon la voix. Un ecart pareil ne
    s'entend pas comme un ecart de volume : il s'entend comme de la presence,
    de l'assurance, de la chaleur. Faire ecouter des echantillons non egalises,
    c'est faire choisir le plus fort en croyant faire choisir le meilleur.
    Le script REFUSE de produire un comparatif si ffmpeg est absent -- un
    comparatif fausse est pire que pas de comparatif, parce qu'il porte
    l'autorite d'un test.

POURQUOI UN DOUBLON PAR DEFAUT
    Une des voix est presentee DEUX FOIS, sous deux lettres differentes. Si
    l'auditeur les classe loin l'une de l'autre, le test n'a pas mesure la
    voix : il a mesure l'humeur, la fatigue ou l'ordre d'ecoute. C'est le seul
    moyen de savoir si le verdict tient, et ca ne coute qu'un echantillon.
    Le doublon est note dans la cle, jamais dans ce qu'on fait ecouter.

LES REPLIQUES SONT CELLES DU ROLE
    On ne juge pas une voix de personnage sur « Fruehstueck ». Les textes
    viennent de scenes/<scene>.json, des repliques que ce personnage dira
    vraiment : une question, une explication longue, une formule de politesse.
    Une voix peut tenir sur cinq mots et s'effondrer sur trois phrases.

LA CLE API NE SAIT PAS LISTER LES VOIX
    Celle du projet est limitee au Text to Speech et recoit 401 sur
    /v1/voices -- c'est deja consigne dans CLE-du-comparatif.json. Les
    identifiants candidats se relevent donc a la main dans l'interface
    ElevenLabs, et se collent dans candidats_<personnage>.json.
"""
import argparse
import io
import json
import os
import random
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))

# On IMPORTE generer et normaliser au lieu de recopier leur contenu. Le code
# reseau de generer.py porte des annees d'accidents -- le 429 qu'il faut
# retenter, le 403 « violate our Terms » qui vise le TEXTE et pas la cle, le
# format et les reglages fixes pour tout le corpus. Le comparatif doit faire
# entendre CE QUE LA PRODUCTION FERA ENTENDRE : meme modele, memes reglages,
# meme graine. Une copie divergerait, et on choisirait une voix qu'on
# n'entendrait jamais.
import generer                                            # noqa: E402
import normaliser                                         # noqa: E402

SORTIE = os.path.join(RACINE, "audio", "a_ecouter_voix")


def repliques(personnage, scene):
    """Les repliques du role, prises dans la scene elle-meme."""
    chemin = os.path.join(RACINE, "scenes", scene + ".json")
    d = json.load(io.open(chemin, encoding="utf-8"))
    textes = [p["de"] for p in d["plans"] if p.get("locuteur") == personnage]
    if not textes:
        sys.exit("  %s ne dit rien dans %s." % (personnage, scene))
    return textes


def candidats(personnage):
    chemin = os.path.join(RACINE, "audio", "candidats_%s.json" % personnage)
    if not os.path.exists(chemin):
        modele = {
            "_lisez_moi": [
                "Les voix a comparer. Releve nom et voice_id dans l'interface",
                "ElevenLabs : la cle du projet est limitee au Text to Speech et",
                "recoit 401 sur /v1/voices, elle ne peut pas les lister.",
                "",
                "Quatre a six candidates. En dessous de quatre le choix est trop",
                "etroit ; au-dela de six l'oreille ne distingue plus.",
                "",
                "Une voix fabriquee par Voice Design se colle ici comme les",
                "autres : c'est un voice_id ordinaire une fois creee."
            ],
            "voix": [
                {"nom": "", "voice_id": ""},
                {"nom": "", "voice_id": ""},
                {"nom": "", "voice_id": ""},
                {"nom": "", "voice_id": ""}
            ]
        }
        io.open(chemin, "w", encoding="utf-8", newline="").write(
            json.dumps(modele, ensure_ascii=False, indent=2) + "\n")
        sys.exit("  Modele ecrit dans audio/candidats_%s.json.\n"
                 "  Colle les identifiants dedans, puis relance." % personnage)

    d = json.load(io.open(chemin, encoding="utf-8"))
    v = [x for x in d.get("voix", []) if x.get("voice_id")]
    if len(v) < 2:
        sys.exit("  Il faut au moins deux voix renseignees dans %s."
                 % os.path.basename(chemin))
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--personnage", required=True,
                    help="cle du locuteur dans la scene, p. ex. marc")
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--modele", default="v2", choices=sorted(generer.MODELES))
    ap.add_argument("--sans-doublon", action="store_true",
                    help="retirer le controle de coherence (deconseille)")
    a = ap.parse_args()

    # L'EGALISATION N'EST PAS UNE OPTION : sans elle, on fait choisir le plus
    # fort. Mieux vaut s'arreter que produire un test qui a l'air d'en etre un.
    normaliser.FF = normaliser.ffmpeg()
    if not normaliser.FF:
        sys.exit("  ffmpeg est indispensable : sans egalisation de la sonie,\n"
                 "  l'echantillon le plus fort gagne le comparatif et le\n"
                 "  resultat ne veut rien dire. Rien n'a ete produit.")

    textes = repliques(a.personnage, a.scene)
    voix = candidats(a.personnage)
    cle = generer.cle_api()
    modele, cout = generer.MODELES[a.modele]

    # Le doublon : une candidate tiree au sort passe deux fois.
    lots = list(voix)
    doublon = None
    if not a.sans_doublon:
        doublon = random.choice(voix)
        lots.append(doublon)

    caracteres = sum(len(t) for t in textes) * len(lots)
    print("  %d voix (%s doublon) x %d repliques = %d caracteres, environ %d credits"
          % (len(voix), "sans" if a.sans_doublon else "avec",
             len(textes), caracteres, int(caracteres * cout)))

    dossier = os.path.join(SORTIE, a.personnage)
    brut = os.path.join(dossier, "_brut")
    os.makedirs(brut, exist_ok=True)

    random.shuffle(lots)
    lettres = [chr(ord("A") + i) for i in range(len(lots))]
    cle_json = []

    for lettre, v in zip(lettres, lots):
        print("  VOIX-%s ..." % lettre, end="", flush=True)
        morceaux = []
        for i, t in enumerate(textes):
            # generer.synthetiser() lit la voix dans la globale du module :
            # on la deplace le temps de l'appel plutot que de dupliquer tout
            # le code de reprise sur erreur, qui est la vraie valeur du module.
            avant = generer.VOIX
            generer.VOIX = v["voice_id"]
            try:
                octets = generer.synthetiser(t, modele, cle)
            except generer.TexteBloque:
                print(" texte refuse, replique sautee", end="")
                continue
            finally:
                generer.VOIX = avant
            f = os.path.join(brut, "VOIX-%s-%02d.mp3" % (lettre, i + 1))
            io.open(f, "wb").write(octets)
            morceaux.append(f)

        # Egalisation, exactement celle du corpus : ce que l'auditeur entend
        # est ce que l'application servira.
        for f in morceaux:
            normaliser.normaliser(f, os.path.join(dossier, os.path.basename(f)))
        mesures = [normaliser.mesurer(os.path.join(dossier, os.path.basename(f)))
                   for f in morceaux]
        print(" %d fichiers" % len(morceaux))

        cle_json.append({"lot": lettre, "nom": v.get("nom") or "(sans nom)",
                         "voice_id": v["voice_id"],
                         "doublon_de": None, "sonie": mesures})

    if doublon:
        vus = [c for c in cle_json if c["voice_id"] == doublon["voice_id"]]
        for c in vus[1:]:
            c["doublon_de"] = vus[0]["lot"]

    # LA CLE NE VA PAS DANS LE DOSSIER D'ECOUTE. On la range d'un cran au-dessus :
    # un fichier « cle » a cote des echantillons finit toujours par etre ouvert.
    chemin_cle = os.path.join(SORTIE, "CLE-du-comparatif-%s.json" % a.personnage)
    io.open(chemin_cle, "w", encoding="utf-8", newline="").write(json.dumps({
        "_lisez_moi": [
            "Cle du comparatif a l'aveugle pour le personnage « %s »." % a.personnage,
            "NE PAS OUVRIR avant que le verdict soit rendu et ecrit.",
            "Les echantillons sont dans a_ecouter_voix/%s/." % a.personnage,
            "",
            "Le champ nom est rempli des maintenant : en septembre 2026, l'avoir",
            "omis a coute une heure, une comparaison d'empreintes MD5 et un",
            "detour par le compte ElevenLabs pour retrouver le choix de Barbara.",
            "",
            "doublon_de : cette lettre est la MEME voix qu'une autre. Si",
            "l'auditeur les a classees loin l'une de l'autre, le comparatif a",
            "mesure l'humeur et non la voix -- a refaire."
        ],
        "personnage": a.personnage, "scene": a.scene,
        "modele": modele, "reglages": generer.REGLAGES, "seed": generer.SEED,
        "repliques": textes,
        "sonie_cible_lufs": -14.0,
        "lots": cle_json,
        "choix": {"lot": None, "nom": None, "voice_id": None,
                  "choisi_par": None, "date": None, "aveugle": True}
    }, ensure_ascii=False, indent=2) + "\n")

    print("\n  A faire ecouter : audio/a_ecouter_voix/%s/" % a.personnage)
    print("  Cle (a ne pas ouvrir avant) : %s" % os.path.basename(chemin_cle))
    print("  Ne dis pas combien il y a de voix : le doublon doit rester invisible.")


if __name__ == "__main__":
    main()
