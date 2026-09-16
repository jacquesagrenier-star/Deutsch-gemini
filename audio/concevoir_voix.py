# -*- coding: utf-8 -*-
"""Concevoir une voix par Voice Design, et l'ecouter avant de la garder.

    python audio/concevoir_voix.py --nom dame --texte-essai "..." \\
        --description "A native German woman in her late fifties..."
    python audio/concevoir_voix.py --garder dame --lequel B --nom-final "Dame-01"

POURQUOI PAS LA VOICE LIBRARY.

Meme raisonnement que pour Anna, le 8 septembre 2026, et que pour les
visages : une voix CONCUE n'appartient a personne. Pas de consentement a
obtenir ni a maintenir, contrairement au clonage d'une voix reelle.

⚠️ LES NEGATIONS FINALES FONT LA MOITIE DU TRAVAIL, ET C'EST L'INVERSE DE
   NOTRE REGLE POUR LES IMAGES. La fiche d'Anna le dit : sans << not breathy,
   not girlish >>, toutes ces voix tombent dans le meme travers, l'accueil
   trop enjoue. Voice Design COMPREND les negations. Les generateurs
   d'images n'ont aucun canal pour elles et fabriquent ce qu'on interdit.
   Deux moteurs, deux grammaires -- ne pas transporter la lecon de l'un a
   l'autre.

⚠️ ET ON ECOUTE AVANT DE GARDER. Trois apercus reviennent par description.
   Le projet a deja note que Mark-VD-03 et Anna ont ete choisies sans test a
   l'aveugle, et que ces decisions << tiennent mais ne valent pas celle qui a
   donne Aurora >>. Ici on etiquette A, B, C et on ne commente pas avant.

⚠️ LE TEXTE D'ESSAI EST UNE VRAIE REPLIQUE DU PERSONNAGE, jamais une phrase
   neutre. Une voix se juge sur ce qu'elle aura a faire -- l'indignation
   polie de la dame, la bascule du cycliste de l'agacement a la pedagogie.
   Une phrase quelconque les fait toutes sonner pareil.
"""
import argparse
import base64
import io
import json
import os
import sys
import urllib.error
import urllib.request

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                                            # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")

APERCUS = "https://api.elevenlabs.io/v1/text-to-voice/create-previews"
GARDER = "https://api.elevenlabs.io/v1/text-to-voice/create-voice-from-preview"
DOSSIER = os.path.join(RACINE, "audio", "a_ecouter_voix", "conception")


def poster(url, corps, cle):
    r = urllib.request.Request(url, data=json.dumps(corps).encode("utf-8"),
                               method="POST",
                               headers={"xi-api-key": cle,
                                        "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r, timeout=180) as rep:
            return json.loads(rep.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit("  HTTP %s\n  %s"
                 % (e.code, e.read().decode("utf-8", "replace")[:400]))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--nom", required=True)
    p.add_argument("--description")
    p.add_argument("--texte-essai", dest="texte")
    p.add_argument("--garder", action="store_true")
    p.add_argument("--lequel", help="A, B ou C")
    p.add_argument("--nom-final")
    a = p.parse_args()
    cle = generer.cle_api()
    if not os.path.isdir(DOSSIER):
        os.makedirs(DOSSIER)
    recu = os.path.join(DOSSIER, a.nom + ".json")

    if a.garder:
        if not (a.lequel and a.nom_final):
            sys.exit("  Preciser --lequel A|B|C et --nom-final.")
        d = json.load(io.open(recu, encoding="utf-8"))
        i = "ABC".index(a.lequel.upper())
        gid = d["apercus"][i]["generated_voice_id"]
        res = poster(GARDER, {"voice_name": a.nom_final,
                              "voice_description": d["description"],
                              "generated_voice_id": gid}, cle)
        print("  voix gardee : %s\n  voice_id : %s"
              % (a.nom_final, res.get("voice_id")))
        d["retenu"] = {"lequel": a.lequel.upper(), "nom": a.nom_final,
                       "voice_id": res.get("voice_id")}
        io.open(recu, "w", encoding="utf-8").write(
            json.dumps(d, ensure_ascii=False, indent=1))
        return

    if not (a.description and a.texte):
        sys.exit("  Preciser --description et --texte-essai.")
    if len(a.description) > 500:
        sys.exit("  la description fait %d caracteres ; le champ est plafonne "
                 "a 500." % len(a.description))

    res = poster(APERCUS, {"voice_description": a.description,
                           "text": a.texte,
                           "auto_generate_text": False}, cle)
    apercus = res.get("previews", [])
    print("  %d apercus pour « %s »" % (len(apercus), a.nom))
    garde = []
    for i, ap in enumerate(apercus):
        lettre = "ABC"[i] if i < 3 else str(i)
        dst = os.path.join(DOSSIER, "%s-%s.mp3" % (a.nom, lettre))
        io.open(dst, "wb").write(base64.b64decode(ap["audio_base_64"]))
        print("    %s  %6.1f ko  %s"
              % (lettre, os.path.getsize(dst) / 1024.0, dst))
        garde.append({"lettre": lettre,
                      "generated_voice_id": ap["generated_voice_id"]})
    io.open(recu, "w", encoding="utf-8").write(json.dumps(
        {"nom": a.nom, "description": a.description, "texte": a.texte,
         "apercus": garde}, ensure_ascii=False, indent=1))
    print("  recu : %s" % recu)


if __name__ == "__main__":
    main()
