# -*- coding: utf-8 -*-
"""De la musique ORIGINALE, generee -- jamais une chanson existante.

    python audio/musique.py --episode 03
    python audio/musique.py --nom essai --texte "..." --duree 20

POURQUOI PAS UNE VRAIE CHANSON BERLINOISE.

Jacques, 16 septembre 2026 : << une musique tres populaire de Berlin de
l'epoque, en arriere-son, qui n'a pas de droit d'auteur >>.

Le piege est que << libre de droits >> ne veut pas dire ce qu'on espere. DEUX
droits se superposent :

  la COMPOSITION      tombe dans le domaine public 70 ans apres la mort de
                      l'auteur. Pour un titre de cabaret des annees 1920,
                      c'est souvent passe.
  l'ENREGISTREMENT    porte son propre droit voisin, 70 ans apres sa
                      publication dans l'UE. Un vieil enregistrement trouve
                      en ligne n'est donc PAS libre, meme si la partition
                      l'est.

Pour une app commerciale, se tromper la-dessus ne coute pas un avertissement,
ca coute un retrait. On genere donc une musique originale -- meme raisonnement
que pour les voix concues et les visages : ce qui est fabrique n'appartient a
personne d'autre.

⚠️ ET LA MUSIQUE N'EST PAS UNE AMBIANCE. Un lit de rue se pose a -24 dB sous
   le dialogue et l'oreille l'oublie. Une musique attire l'oreille meme basse,
   et la regle du projet est ecrite : << un apprenant qui decode de l'allemand
   n'a aucune attention a depenser sur un fond trop present >>. Elle a donc sa
   place a L'OUVERTURE et sur LA CHUTE, pas sous les repliques.

⚠️ LA PERMISSION EST A PART. La cle du projet a recu sound_generation en
   septembre, mais music_generation est une case distincte -- verifie le
   16 septembre 2026 : l'API repond 401 sans elle. Et un 422 ne prouve rien,
   la validation du corps passe AVANT le controle de permission.
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

URL = "https://api.elevenlabs.io/v1/music"
DOSSIER = os.path.join(RACINE, "audio", "musique")

# Trois directions franchement differentes, pour que le choix soit un choix.
ESSAIS = {
    "03": [
        ("cabaret", 22000,
         "Light instrumental Berlin cabaret in the old style: clarinet, "
         "upright piano and a soft accordion, brushed snare, walking bass. "
         "Playful and a little cheeky, mid tempo, major key. No vocals. "
         "Leaves plenty of room, nothing dramatic."),
        ("electro-doux", 22000,
         "Warm minimal Berlin electronic underscore: soft analogue pulse, "
         "muted bass, a few clean synth notes, gentle hi-hat. Modern, calm "
         "and friendly rather than clubby. No vocals, no build-up, no drop."),
        ("pizzicato", 22000,
         "A light comic underscore: pizzicato strings, glockenspiel, a "
         "clarinet answering, soft brushed drums. Curious and good-natured, "
         "the sound of a small misunderstanding. No vocals, understated."),
    ],
}


def fabriquer(nom, texte, ms, cle):
    dst = os.path.join(DOSSIER, nom + ".mp3")
    if os.path.exists(dst) and os.path.getsize(dst) > 1024:
        print("  %-14s deja la (%d ko) -- on ne repaie pas"
              % (nom, os.path.getsize(dst) // 1024))
        return
    corps = json.dumps({"prompt": texte, "music_length_ms": ms}).encode("utf-8")
    r = urllib.request.Request(URL, data=corps, method="POST",
                               headers={"xi-api-key": cle,
                                        "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r, timeout=300) as rep:
            octets = rep.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:300]
        if e.code == 401 and "music_generation" in detail:
            sys.exit("  La cle n'a pas la permission « music_generation ».\n"
                     "  ElevenLabs > Profile > API Keys > la cle > cocher "
                     "Music.\n  (C'est une case distincte de Sound Effects.)")
        sys.exit("  HTTP %s sur %s\n  %s" % (e.code, nom, detail))
    if not os.path.isdir(DOSSIER):
        os.makedirs(DOSSIER)
    io.open(dst, "wb").write(octets)
    print("  %-14s %6.1f ko   %s" % (nom, len(octets) / 1024.0, dst))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--episode")
    p.add_argument("--nom")
    p.add_argument("--texte")
    p.add_argument("--duree", type=float, default=22.0)
    a = p.parse_args()
    cle = generer.cle_api()
    if a.episode:
        lot = ESSAIS.get(a.episode)
        if not lot:
            sys.exit("  aucun essai ecrit pour l'episode %s" % a.episode)
        print("  %d essai(s)" % len(lot))
        for nom, ms, texte in lot:
            fabriquer(nom, texte, ms, cle)
        return
    if not (a.nom and a.texte):
        sys.exit("  Preciser --episode NN, ou --nom et --texte.")
    fabriquer(a.nom, a.texte, int(a.duree * 1000), cle)


if __name__ == "__main__":
    main()
