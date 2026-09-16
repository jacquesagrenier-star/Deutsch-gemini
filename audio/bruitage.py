# -*- coding: utf-8 -*-
"""Les BRUITS PONCTUELS d'un episode -- une sonnette, une porte, un klaxon.

    python audio/bruitage.py --episode 03
    python audio/bruitage.py --nom sonnette --texte "..." --duree 3

CE QUE CE N'EST PAS : un lit d'ambiance. lit_ambiance.py fabrique un FOND
continu, qui tourne en boucle sous tout un lieu a -24 dB. Ici on fabrique un
EVENEMENT : ca arrive une fois, a un instant precis, et ca doit s'entendre.

POURQUOI L'EPISODE 3 EN A BESOIN, ET CE N'EST PAS UN ORNEMENT.

Jacques, 16 septembre 2026, sur le montage complet : << il dit que les gens
sonnent, mais on n'entend rien. Puis la femme qui passe en velo garde la
bouche grande ouverte, sans dire un mot. >>

Deux fois le meme defaut, et il est structurel : au plan 08 Mark demande
<< Warum klingeln alle? >> -- pourquoi tout le monde sonne -- alors qu'aucune
sonnette n'a sonne. La replique ne commente rien. Et au plan 07 la cycliste
crie sans qu'on l'entende : un cri muet ne se lit pas comme de la colere, il
se lit comme un defaut de fabrication.

⚠️ LE BRUIT SE POSE AU MONTAGE, JAMAIS DANS LA PISTE TELEVERSEE. C'etait deja
   ecrit dans A-TOURNER.txt au plan 07, et ByteDance le dit aussi de son cote :
   << remove background noise >> de l'audio pilote. Une sonnette dans le mp3
   ferait articuler l'avatar dessus.

⚠️ ET LA CYCLISTE NE DIT PAS DE MOTS. On lui donne un eclat de voix sans
   parole -- un << hey >> etouffe par la distance. Lui faire dire une phrase
   allemande demanderait une voix de plus, un lip-sync, et ferait croire a
   l'apprenant qu'il y a la une replique a comprendre. Ce n'est pas une
   replique, c'est un bruit de rue.
"""
import argparse
import io
import json
import os
import sys
import urllib.error
import urllib.request

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
import generer                                             # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")

URL = "https://api.elevenlabs.io/v1/sound-generation"
DOSSIER = os.path.join(RACINE, "audio", "bruitage")

EPISODES = {
    "03": [
        ("sonnette-double", 3.0,
         "Two sharp rings of a classic bicycle bell, close by, one after the "
         "other, on a quiet city street. Bright metallic ping. Nothing else."),
        ("sonnettes-plusieurs", 4.0,
         "Several bicycle bells ringing one after another on a city street, "
         "some close and some further away, insistent, over faint tyre noise "
         "on asphalt. No voices, no music."),
        # ⚠️ ELLE DIT << HEY! HEY! >>, ET C EST JACQUES QUI A TRANCHE.
        #    J avais fait un cri SANS PAROLE, en craignant qu une phrase
        #    allemande fasse croire a l apprenant qu il y a la une replique a
        #    comprendre. Son objection : << Hey >> n est pas du vocabulaire
        #    allemand, c est une interjection que tout le monde comprend. Elle
        #    ne charge donc rien, et elle rend le cri LISIBLE -- un cri sans
        #    mots se lit comme un defaut de fabrication, pas comme de la
        #    colere.
        ("cri-hey", 2.5,
         "A woman shouting \"Hey! Hey!\" outdoors as she rides past on a "
         "city street, annoyed and warning someone. Two short bursts, "
         "carrying but not screamed."),
    ],
}


def fabriquer(nom, texte, duree, influence, cle):
    dst = os.path.join(DOSSIER, nom + ".mp3")
    if os.path.exists(dst) and os.path.getsize(dst) > 1024:
        print("  %-20s deja la (%d ko) -- on ne repaie pas"
              % (nom, os.path.getsize(dst) // 1024))
        return
    corps = json.dumps({"text": texte, "duration_seconds": duree,
                        "prompt_influence": influence}).encode("utf-8")
    r = urllib.request.Request(URL, data=corps, method="POST",
                               headers={"xi-api-key": cle,
                                        "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r, timeout=180) as rep:
            octets = rep.read()
    except urllib.error.HTTPError as e:
        sys.exit("  HTTP %s sur %s\n  %s"
                 % (e.code, nom, e.read().decode("utf-8", "replace")[:300]))
    if not os.path.isdir(DOSSIER):
        os.makedirs(DOSSIER)
    io.open(dst, "wb").write(octets)
    print("  %-20s %6.1f ko   %s" % (nom, len(octets) / 1024.0, dst))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--episode")
    p.add_argument("--nom")
    p.add_argument("--texte")
    p.add_argument("--duree", type=float, default=3.0)
    p.add_argument("--influence", type=float, default=0.75)
    a = p.parse_args()
    cle = generer.cle_api()
    if a.episode:
        lot = EPISODES.get(a.episode)
        if not lot:
            sys.exit("  aucun bruitage ecrit pour l'episode %s" % a.episode)
        print("  %d bruit(s), influence %.0f %%" % (len(lot), a.influence * 100))
        for nom, duree, texte in lot:
            fabriquer(nom, texte, duree, a.influence, cle)
        return
    if not (a.nom and a.texte):
        sys.exit("  Preciser --episode NN, ou --nom et --texte.")
    fabriquer(a.nom, a.texte, a.duree, a.influence, cle)


if __name__ == "__main__":
    main()
