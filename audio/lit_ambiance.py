# -*- coding: utf-8 -*-
"""Fabriquer un LIT d'ambiance -- le fond sonore d'un lieu.

    python audio/lit_ambiance.py --episode 02
    python audio/lit_ambiance.py --nom couloir --texte "..." --duree 22

POURQUOI UN LIT PAR LIEU.

Jacques, 12 septembre 2026 : << quand il change d'endroit, le son devrait
changer ; on devrait entendre les roulettes >>. Un lit unique sur tout
l'episode contredit le montage -- un hall, un couloir et une rue n'ont pas la
meme signature, et l'oreille le sait avant l'oeil.

⚠️ LA CASE QUI COMPTE EST << AMELIORATION OFF >>. L'amelioration reecrit le
   prompt, et elle peut gommer le << no intelligible speech >> -- la clause qui
   empeche des voix de se glisser dans le fond. Ici on n'envoie tout
   simplement pas ce reglage : l'API prend le texte tel quel.

⚠️ ET RIEN DE CE QUE LE PERSONNAGE DEMANDE NE DOIT S'ENTENDRE. Pas
   d'annonce qui reponde a sa question, pas de numero appele, aucun mot
   reconnaissable. Un fond qui renseigne rend la scene absurde -- la regle
   date de l'annonce d'aeroport de l'episode 1, qui avait failli coûter le
   plan 5.

⚠️ LE LIT NE VA JAMAIS DANS LA PISTE TELEVERSEE chez fal. Il se pose au
   montage, par `video/ambiance.py`, a -24 dB sous le dialogue (WCAG 1.4.7).
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

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

URL = "https://api.elevenlabs.io/v1/sound-generation"
DOSSIER = os.path.join(RACINE, "audio", "ambiance")

# Les lieux de l'episode 2. Les instants ou le lit change sont dans
# video/episode-02-beim-buergeramt/AMBIANCE-a-faire.txt, mesures sur le
# montage reel et non estimes.
EPISODES = {
    # ⚠️ L EPISODE 3 SE PASSE DANS UNE SEULE RUE, et c est ecrit en tete de son
    #    decoupage : le carrefour au debut, la piste au milieu, le carrefour
    #    suivant au bout. Deux lits suffisent donc, et ils se ressemblent a
    #    dessein -- c est le MEME endroit vu a deux endroits.
    #
    #    Ce qui les separe est ce qu on y entend : au carrefour, des gens qui
    #    attendent et une rue qui passe ; sur la piste, des velos qui roulent
    #    tout pres. C est cette difference-la qui dit au spectateur qu il a
    #    change de place sans qu on le lui montre.
    "03": [
        # ⚠️ PAS DE PAS. Premiere version : << footsteps of people waiting on
        #    the pavement >>. Jacques : << il y a comme des bruits de pas qui
        #    n ont pas rapport ; il faudrait entendre des velos qui roulent,
        #    des autos, un tramway au loin >>.
        #
        #    Il a raison, et la raison est de mise en scene : dans CE plan les
        #    gens attendent IMMOBILES au feu -- c est meme tout le propos de la
        #    scene. Des pas contredisent l image. Le fond d une rue n est pas
        #    une liste de bruits de rue : c est ce que FAIT cette rue-la.
        ("rue-carrefour",
         "A Berlin street corner on a weekday morning, heard from the "
         "pavement: cars and vans rolling past on the road, a tram rumbling "
         "and squealing somewhere further off, bicycle tyres humming by, a "
         "bicycle bell once in the distance, a faint wash of city traffic "
         "behind it all. Open air, unhurried, no footsteps, no intelligible "
         "speech."),
        ("piste-cyclable",
         "A Berlin cycle lane heard close up: bicycle tyres rolling on "
         "asphalt, a freewheel clicking as a bicycle coasts past, a chain "
         "turning, another bicycle passing further off, cars on the road "
         "beyond and a distant tram. Open air, no footsteps, no intelligible "
         "speech."),
    ],
    "02": [
        ("rue-berlin",
         "A quiet Berlin side street on a Monday morning: distant traffic on "
         "a larger street, a tram passing far away, occasional footsteps on "
         "the pavement, a bicycle bell once. Calm, open air, no intelligible "
         "speech."),
        ("buergeramt",
         "The inside of a small German municipal office: quiet room tone, a "
         "fluorescent light hum, a printer working somewhere behind a wall, a "
         "chair moving on a hard floor, a keyboard now and then, a door "
         "closing at a distance. Muffled, unhurried, no intelligible speech."),
        ("couloir",
         "A long stone corridor in an old public building: footsteps echoing "
         "on a tiled floor, a heavy door closing far away, a faint hum. "
         "Empty, resonant, no intelligible speech."),
    ],
}


def fabriquer(nom, texte, duree, influence, cle):
    dst = os.path.join(DOSSIER, nom + ".mp3")
    if os.path.exists(dst) and os.path.getsize(dst) > 1024:
        print("  %-14s deja la (%d ko) -- on ne repaie pas"
              % (nom, os.path.getsize(dst) // 1024))
        return
    corps = json.dumps({"text": texte,
                        "duration_seconds": duree,
                        "prompt_influence": influence,
                        "loop": True}).encode("utf-8")
    r = urllib.request.Request(URL, data=corps, method="POST",
                               headers={"xi-api-key": cle,
                                        "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r, timeout=180) as rep:
            octets = rep.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:300]
        sys.exit("  HTTP %s sur %s\n  %s" % (e.code, nom, detail))
    if not os.path.isdir(DOSSIER):
        os.makedirs(DOSSIER)
    io.open(dst, "wb").write(octets)
    print("  %-14s %6.1f ko   %s" % (nom, len(octets) / 1024.0, dst))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--episode", help="fabrique tous les lits de cet episode")
    p.add_argument("--nom")
    p.add_argument("--texte")
    p.add_argument("--duree", type=float, default=22.0)
    p.add_argument("--influence", type=float, default=0.6)
    a = p.parse_args()
    cle = generer.cle_api()
    if a.episode:
        lits = EPISODES.get(a.episode)
        if not lits:
            sys.exit("  aucun lit ecrit pour l'episode %s" % a.episode)
        print("  %d lit(s) de %.0f s, influence %.0f %%"
              % (len(lits), a.duree, a.influence * 100))
        for nom, texte in lits:
            fabriquer(nom, texte, a.duree, a.influence, cle)
        return
    if not (a.nom and a.texte):
        sys.exit("  Preciser --episode NN, ou --nom et --texte.")
    fabriquer(a.nom, a.texte, a.duree, a.influence, cle)


if __name__ == "__main__":
    main()
