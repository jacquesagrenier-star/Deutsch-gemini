# -*- coding: utf-8 -*-
"""L'ambiance d'aeroport sous le dialogue : traiter, doser, melanger.

    python video/ambiance.py --annonce audio/ambiance/annonce-de.mp3
    python video/ambiance.py --clip <une video> --lit audio/ambiance/hall.mp3
                            --annonce ... --a 4.0 --sortie sonorise.mp4

CE QUE CA FAIT
    1. L'ANNONCE devient une annonce de haut-parleur : bande passante de
       telephone, bosses a 1 k / 2 k / 4 k, puis une grande reverberation de
       hall. C'est la REVERBERATION qui fait l'aeroport -- le filtre seul
       donne un talkie-walkie.
    2. LES LITS d'ambiance -- un par LIEU -- sont mis en boucle et enchaines
       en fondu aux instants ou la scene change d'endroit.
       ⚠️ Un lit unique sur tout l'episode contredit le montage. Jacques,
       12 septembre : « quand il change d'endroit, le son devrait changer ;
       on devrait entendre les roulettes ». Un hall d'arrivee, un tapis a
       bagages et une sortie n'ont pas la meme signature, et l'oreille le
       sait avant l'oeil.
    3. TOUT EST DOSE PAR RAPPORT AU DIALOGUE, mesure, pas devine.

⚠️ AU MOINS 20 dB SOUS LA PAROLE -- et ce n'est pas une convention de gout.
    C'est le critere WCAG 1.4.7, « Low or No Background Audio ». Pour une
    app d'apprentissage la raison est plus forte encore : un apprenant qui
    decode de l'allemand n'a aucune attention a depenser sur un fond trop
    present. Le lit descend donc a -24 dB sous le dialogue, l'annonce a -20
    -- assez pour s'entendre, trop peu pour qu'on l'ecoute.

⚠️ L'AMBIANCE NE VA JAMAIS DANS LA PISTE QUI PILOTE L'AVATAR.
    OmniHuman fabrique la bouche A PARTIR DU SON. Une annonce dans le mp3
    televerse ferait articuler le personnage sur elle. L'ambiance se pose
    ICI, au montage, sur le clip deja genere.

⚠️ ET L'ANNONCE DOIT RESTER ININTELLIGIBLE.
    Une voix allemande comprehensible derriere le dialogue entre en
    concurrence avec la lecon. C'est d'ailleurs comme ca que sonne une
    vraie annonce a vingt metres : on entend qu'elle parle, pas ce qu'elle
    dit. Le traitement n'est pas un effet, c'est ce qui la rend utilisable.

⚠️ ET RIEN DE CE QUE MARK DEMANDE NE DOIT SORTIR DU HAUT-PARLEUR.
    Pas de Gepaeckausgabe, pas de S-Bahn, pas de billets ni de centre-ville.
    Le lisez-moi de l'episode le dit deja pour les panneaux : « un panneau
    lisible qui indique GEPAECKAUSGABE rendrait absurde la question du plan
    5 ». Une annonce a exactement le meme pouvoir.
"""
import argparse
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

SOUS_LIT = 24.0        # dB sous le dialogue pour le lit d'ambiance
FONDU = 0.8            # le croisement entre deux lits, en secondes
SOUS_ANNONCE = 20.0    # dB sous le dialogue pour l'annonce

# La chaine du haut-parleur. Bande de telephone, puis les trois bosses que
# les praticiens citent, puis la reverberation du hall.
PA = ("highpass=f=420,lowpass=f=3600,"
      "equalizer=f=1000:width_type=o:width=1:g=4,"
      "equalizer=f=2000:width_type=o:width=1:g=6,"
      "equalizer=f=4000:width_type=o:width=1:g=3,"
      "acompressor=threshold=-18dB:ratio=4:attack=5:release=120,"
      # ⚠️ ffmpeg n'a pas de reverberation a convolution sans reponse
      # impulsionnelle : on empile des echos. Trois retards inegaux, sinon
      # on entend un peigne au lieu d'un hall.
      "aecho=0.8:0.85:63|97|131:0.30|0.22|0.15,"
      "aecho=0.7:0.6:211|307:0.18|0.12")


def loudness(F, chemin):
    """La loudness integree, en LUFS. None si la mesure echoue."""
    r = subprocess.run([F, "-hide_banner", "-nostats", "-i", chemin,
                        "-map", "0:a", "-af", "ebur128=peak=true",
                        "-f", "null", "-"],
                       capture_output=True, text=True, errors="ignore")
    m = re.findall(r"I:\s*(-?\d+\.\d+)\s*LUFS", r.stderr)
    return float(m[-1]) if m else None


def a_le_son(F, chemin):
    r = subprocess.run([F, "-hide_banner", "-i", chemin],
                       capture_output=True, text=True, errors="ignore")
    return "Audio:" in r.stderr


def lits_demandes(valeurs, duree):
    """« fichier@instant » -> [(fichier, debut, fin)], bornes a la duree."""
    lus = []
    for v in valeurs:
        if "@" in v:
            f, t = v.rsplit("@", 1)
            lus.append((f, float(t)))
        else:
            lus.append((v, 0.0))
    lus.sort(key=lambda e: e[1])
    out = []
    for i, (f, debut) in enumerate(lus):
        fin = lus[i + 1][1] if i + 1 < len(lus) else duree
        if fin > debut:
            out.append((f, debut, min(fin, duree)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clip", help="la video a sonoriser")
    ap.add_argument("--lit", action="append", default=[], metavar="FICHIER@T",
                    help="un lit d'ambiance et l'instant ou il prend le relais. "
                         "Repetable : --lit hall.mp3@0 --lit tapis.mp3@27.3")
    ap.add_argument("--annonce", help="l'annonce brute, voix seche")
    ap.add_argument("--a", type=float, default=None, metavar="SECONDES",
                    help="a quel instant poser l'annonce")
    ap.add_argument("--sortie")
    a = ap.parse_args()

    F = M.ffmpeg()

    # --------------------------------------- l'annonce seule, pour l'ecouter
    if a.annonce and not a.clip:
        dst = a.sortie or os.path.splitext(a.annonce)[0] + "-hautparleur.mp3"
        subprocess.run([F, "-y", "-v", "error", "-i", a.annonce, "-af", PA,
                        "-ar", "44100", "-b:a", "192k", dst], check=True)
        print("  %s" % os.path.relpath(dst, RACINE))
        print("  Ecoute-la seule : si tu COMPRENDS les mots, il en faut plus.")
        return

    if not a.clip:
        sys.exit("  Donner --clip, ou --annonce seule pour entendre l'effet.")
    if not a_le_son(F, a.clip):
        sys.exit("  Ce clip n'a pas de piste sonore.")

    duree = M.duree(F, a.clip)
    ref = loudness(F, a.clip)
    if ref is None:
        sys.exit("  Impossible de mesurer la loudness du dialogue.")
    print("  dialogue : %.1f LUFS, %.2f s\n" % (ref, duree))

    # ⚠️ COMPTER LES ENTREES, PAS LES MOTS. « -stream_loop -1 -i fichier »
    # fait quatre mots pour une seule entree : un len()//2 se trompe.
    entrees, n_ent = ["-i", a.clip], 1
    chaines, pistes = [], ["[0:a]"]
    cible = ref - SOUS_LIT

    for f, debut, fin in lits_demandes(a.lit, duree):
        if not os.path.exists(f):
            sys.exit("  Lit introuvable : %s" % f)
        i = n_ent
        # ⚠️ -stream_loop AVANT -i, sinon il ne s'applique pas.
        entrees += ["-stream_loop", "-1", "-i", f]
        n_ent += 1
        g = cible - (loudness(F, f) or -20.0)
        # Le segment deborde de FONDU sur le suivant : les deux fondus se
        # croisent, ce qui fait le raccord sans trou ni bosse.
        lg = (fin - debut) + (FONDU if fin < duree else 0.0)
        e_in = FONDU if debut > 0 else 0.3
        chaines.append(
            "[%d:a]atrim=0:%.3f,volume=%.2fdB,"
            "afade=t=in:st=0:d=%.2f,afade=t=out:st=%.3f:d=%.2f,"
            "adelay=%d:all=1,aresample=44100[lit%d]"
            % (i, lg, g, e_in, max(0.0, lg - FONDU), FONDU,
               int(round(debut * 1000)), i))
        pistes.append("[lit%d]" % i)
        print("  lit      : %-16s %6.2f -> %6.2f s   %+.1f dB"
              % (os.path.basename(f), debut, fin, g))

    if a.annonce:
        i = n_ent
        entrees += ["-i", a.annonce]
        n_ent += 1
        c2 = ref - SOUS_ANNONCE
        g = c2 - (loudness(F, a.annonce) or -20.0)
        d = int(round((a.a if a.a is not None else duree * 0.15) * 1000))
        chaines.append("[%d:a]%s,volume=%.2fdB,adelay=%d:all=1,apad,"
                       "aresample=44100[pa]" % (i, PA, g, d))
        pistes.append("[pa]")
        print("  annonce  : %-16s %6.2f s          %+.1f dB  (%.0f dB sous)"
              % (os.path.basename(a.annonce), d / 1000.0, g, SOUS_ANNONCE))

    if len(pistes) < 2:
        sys.exit("  Rien a ajouter : donner --lit et/ou --annonce.")

    chaines.append("%samix=inputs=%d:duration=first:normalize=0,"
                   "alimiter=limit=0.97[out]" % ("".join(pistes), len(pistes)))

    dst = a.sortie or os.path.splitext(a.clip)[0] + "-sonorise.mp4"
    subprocess.run([F, "-y", "-v", "error"] + entrees +
                   ["-filter_complex", ";".join(chaines),
                    "-map", "0:v", "-map", "[out]", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-t", "%.3f" % duree, dst],
                   check=True)
    apres = loudness(F, dst)
    print("\n%s" % os.path.relpath(dst, RACINE))
    if apres is not None:
        print("  melange  : %.1f LUFS  (le dialogue etait a %.1f)" % (apres, ref))
        # ⚠️ Si le melange monte de plus de ~1 dB, le fond n'est plus un fond.
        if apres - ref > 1.0:
            print("  ⚠️ Le melange a gagne %.1f dB : l'ambiance s'entend trop."
                  % (apres - ref))


if __name__ == "__main__":
    main()
