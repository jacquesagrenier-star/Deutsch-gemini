# -*- coding: utf-8 -*-
"""Assemble l'episode : les 19 plans dans l'ordre, chacun avec sa replique.

    python video/montage.py --scene 01-ankunft-berlin

CE QU'IL FAIT, ET CE QU'IL NE FAIT PAS
    Il colle bout a bout les clips de 03-final/ dans l'ordre du scenario et
    pose sur chacun sa piste ElevenLabs. Il ne fait NI lip-sync NI
    sous-titres : le lip-sync se fait avant, plan par plan, chez sync.so, et
    les sous-titres sont affiches par l'application, pas incrustes.

    C'est donc un montage de travail -- celui qui permet de voir l'episode
    pour la premiere fois et de juger le rythme.

LE SILENCE AVANT ET APRES CHAQUE REPLIQUE
    Les clips durent 4 a 7 secondes, les repliques 1,5 a 7. L'ecart n'est pas
    du gaspillage : un plan ne peut pas commencer sur la premiere syllabe ni
    finir sur la derniere. On pose donc la voix avec un retard (AMORCE), et
    ce qui reste apres elle est la respiration du plan.

    Si la replique est plus longue que le clip -- ca arrive, plan 13 -- on
    part a zero et on laisse deborder : mieux vaut une fin serree qu'une
    phrase coupee.

ON NE REENCODE LA VIDEO QU'UNE FOIS
    Chaque plan est mux avec son audio sans toucher au flux video (-c:v copy).
    Le seul reencodage a lieu au collage final, et il est inevitable : les
    clips viennent tous du meme modele avec les memes reglages, mais concat
    exige un flux continu.
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Le retard de la voix sur le debut du plan. Assez pour qu'on voie le
# personnage avant qu'il parle, assez peu pour que le plan ne traine pas.
AMORCE = 0.35


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def duree(ff, chemin):
    r = subprocess.run([ff, "-hide_banner", "-i", chemin],
                       capture_output=True, text=True, errors="replace")
    m = re.search(r"Duration: \d+:(\d+):([\d.]+)", r.stderr)
    return int(m.group(1)) * 60 + float(m.group(2)) if m else None


def ff(cmd, quoi):
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if r.returncode != 0:
        sys.exit("  echec sur %s :\n%s" % (quoi, r.stderr[-700:]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--queue", type=float, default=None, metavar="SECONDES",
                    help="couper chaque plan parlant SECONDES apres la fin de "
                         "la replique. Sans lui, le plan va jusqu'au bout.")
    a = ap.parse_args()

    F = ffmpeg()
    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"), encoding="utf-8"))
    dv = os.path.join(RACINE, "video", "episode-" + a.scene)
    da = os.path.join(RACINE, "audio", "scenes", a.scene)
    tmp = os.path.join(dv, "_montage")
    os.makedirs(tmp, exist_ok=True)

    morceaux = []
    synchro = 0
    print("  plan   clip    voix   %s" % "assemblage")
    for p in d["plans"]:
        # LE PLAN SYNCHRONISE PASSE AVANT L'ORIGINAL. lipsync.py ecrit dans
        # 04-lipsync sans jamais toucher a 03-final : on peut donc remonter
        # l'episode avant, pendant et apres la synchro, et il prend a chaque
        # fois ce qui existe de mieux. Un plan absent de 04-lipsync -- les
        # decors, qui n'ont pas de visage -- retombe sur son clip d'origine.
        v = os.path.join(dv, "04-lipsync", "plan%02d.mp4" % p["n"])
        synchronise = os.path.exists(v)
        if synchronise:
            synchro += 1
        else:
            v = os.path.join(dv, "03-final", "plan%02d.mp4" % p["n"])
        s = os.path.join(da, "%02d-%s.mp3" % (p["n"], p["locuteur"]))
        if not os.path.exists(v):
            sys.exit("  Plan %02d : clip manquant (%s)" % (p["n"], os.path.basename(v)))
        if not os.path.exists(s):
            sys.exit("  Plan %02d : replique manquante (%s)" % (p["n"], os.path.basename(s)))

        dv_, da_ = duree(F, v), duree(F, s)
        out = os.path.join(tmp, "plan%02d.mp4" % p["n"])

        # COUPER PLUTOT QU'ETIRER. Le 8 septembre, cherchant a supprimer le
        # silence ou la bouche du clip s'agite pour rien, on a mesure ce qu'il
        # faudrait pour le combler avec la voix : un ralenti de 0,40 a 0,64
        # fois selon les plans -- 55 a 150 % plus long. Une diction d'endormi,
        # et ElevenLabs v3 ignore de toute facon le reglage de vitesse.
        #
        # La queue, elle, ne coute rien : on garde l'amorce, la replique, et
        # le temps demande apres elle. Ce qu'on perd est la respiration du
        # plan ; ce qu'on gagne est de ne plus montrer une machoire qui parle
        # sur du silence. C'est un choix de rythme, donc il se regarde.
        # ON NE COUPE PAS DEUX FOIS. Quand le plan vient de 04-lipsync, il a
        # DEJA ete raccourci par lipsync.py avant l'envoi -- le recouper ici
        # rognerait un dixieme de plus, et surtout :
        #
        # -c:v copy NE COUPE PAS A LA MILLISECONDE. Il garde des paquets
        # entiers, donc l'image tombe ou elle peut (2,83 s) pendant que
        # l'audio, lui, est coupe net (2,73 s). L'ecart de 0,10 s par plan
        # revenait par la fenetre apres qu'on l'ait chasse par la porte.
        #
        # La duree du plan est donc CELLE DU FICHIER, mesuree, et l'audio se
        # cale dessus. Jamais l'inverse.
        fin = dv_
        if a.queue is not None and p["type"] == "replique" and not synchronise:
            vise = min(dv_, AMORCE + da_ + a.queue)
            if vise < dv_ - 0.02:
                coupe = os.path.join(tmp, "_coupe%02d.mp4" % p["n"])
                ff([F, "-hide_banner", "-nostats", "-loglevel", "error", "-y",
                    "-i", v, "-t", "%.3f" % vise, "-c", "copy", "-an", coupe],
                   "coupe du plan %02d" % p["n"])
                v, fin = coupe, duree(F, coupe)

        # APAD N'EST PAS UN DETAIL DE CONFORT, C'EST CE QUI TIENT LE MONTAGE.
        #
        # Une replique de 2,4 s dans un plan de 5 s laissait une piste audio
        # PLUS COURTE QUE L'IMAGE. Le demultiplexeur concat assemble les deux
        # flux separement : chaque trou d'audio remonte tout ce qui suit. Sur
        # l'episode 1, le decalage atteignait +4,7 s au comptoir et +9,9 s a
        # la fin -- la voix d'Anna arrivait avant que Mark ne soit devant elle.
        #
        # Repere par Jacques le 8 septembre : « la discussion arrive plusieurs
        # secondes avant que Marc arrive au comptoir ». Le defaut etait dans
        # TOUS les montages de la journee, et rien ne l'avait signale : ffmpeg
        # ne s'en plaint pas, les durees totales sont justes, et le tableau a
        # l'ecran montrait des plans parfaitement normaux.
        #
        # On complete donc chaque piste par du silence jusqu'a la derniere
        # image du plan. Image et son font exactement la meme longueur, et le
        # collage ne peut plus deriver.
        if synchronise:
            # LE PLAN SYNCHRONISE PORTE DEJA SA VOIX, ET AU BON ENDROIT.
            # lipsync.py lui a envoye une piste calee sur la duree du clip,
            # amorce comprise : c'est exactement celle que le montage aurait
            # posee. La reposer par-dessus ferait un doublon decale.
            amorce, note = AMORCE, "  sync"
            entree = ["-i", v, "-map", "0:v", "-map", "0:a"]
        else:
            # La voix tient-elle avec l'amorce ? Sinon on la colle au debut.
            amorce = AMORCE if (da_ + AMORCE) <= dv_ else 0.0
            note = "" if amorce else "  <- voix au ras, la replique remplit le plan"
            entree = ["-i", v, "-itsoffset", "%.3f" % amorce, "-i", s,
                      "-map", "0:v", "-map", "1:a"]
        ff([F, "-hide_banner", "-nostats", "-loglevel", "error", "-y"]
           + entree
           + ["-af", "apad", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
              "-ar", "44100", "-t", "%.3f" % fin, out],
           "plan %02d" % p["n"])
        morceaux.append(out)
        if fin < dv_ - 0.02:
            note += "  coupe a %.2f s (-%.2f)" % (fin, dv_ - fin)
        print("  %02d    %5.2f  %5.2f   +%.2f%s"
              % (p["n"], dv_, da_, amorce, note))

    # LE CONTROLE QUI AURAIT ATTRAPE LA DERIVE. Un segment dont le son est
    # plus court que l'image decale tout ce qui suit, et rien d'autre ne le
    # dit. On le verifie donc a chaque montage, sur chaque segment.
    boiteux = []
    for m in morceaux:
        r = subprocess.run([F, "-hide_banner", "-i", m, "-map", "0:a",
                            "-c", "copy", "-f", "null", "-"],
                           capture_output=True, text=True, errors="replace")
        t = re.search(r"time=\d+:(\d+):([\d.]+)", r.stderr)
        son = int(t.group(1)) * 60 + float(t.group(2)) if t else 0.0
        img = duree(F, m)
        if abs(img - son) > 0.05:
            boiteux.append((os.path.basename(m), img, son))
    if boiteux:
        print("\n  DERIVE : ces segments n'ont pas la meme duree d'image et de")
        print("  son. Le collage fera remonter tout ce qui les suit.")
        for nom, img, son in boiteux:
            print("    %s  image %.2f  son %.2f  (%+.2f)" % (nom, img, son, img - son))
        sys.exit("  Montage abandonne.")

    liste = os.path.join(tmp, "_liste.txt")
    io.open(liste, "w", encoding="utf-8", newline="").write(
        "".join("file '%s'\n" % os.path.basename(m) for m in morceaux))

    final = os.path.join(dv, "EPISODE-%s.mp4" % a.scene.split("-")[0])
    ff([F, "-hide_banner", "-nostats", "-loglevel", "error", "-y",
        "-f", "concat", "-safe", "0", "-i", liste,
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
        final], "collage final")

    print("\n  %s" % os.path.relpath(final, RACINE))
    print("  %.1f secondes, %d plans" % (duree(F, final), len(morceaux)))
    print("  image et son de meme duree sur les %d segments." % len(morceaux))
    parlants = sum(1 for p in d["plans"] if p["type"] == "replique")
    if synchro < parlants:
        print("  %d/%d plans parlants passes au lip-sync -- les autres bougent"
              " encore les levres au hasard." % (synchro, parlants))


if __name__ == "__main__":
    main()
