# -*- coding: utf-8 -*-
"""Monter l'episode avec les prises AVATAR, pour le regarder.

    python video/monter_avatar.py
    python video/monter_avatar.py --queue 0.9 --amorce 0.35

POURQUOI PAS montage.py
    montage.py choisit ses clips dans 04-lipsync puis 03-final, et calcule
    ses coupes a partir de audio/scenes/<scene>/NN-<locuteur>.mp3.
    ⚠️ Or cette numerotation-la a derive : audio/scenes/13-anna.mp3 fait
    1,23 s alors que la replique du plan 13 en fait 4,57 -- la feuille
    A-REFAIRE-AUDIO.txt a redecoupe les longues repliques et les numeros ont
    cesse de se correspondre. Tant que ce noeud n'est pas demele, un montage
    qui s'appuie dessus coupe au mauvais endroit sans le dire.

    Celui-ci ne s'appuie que sur ce qu'on a verifie aujourd'hui : les pistes
    de _a-televerser, dont on sait qu'elles viennent du montage lui-meme, et
    dont importer_prise.py a confirme la correspondance par correlation.

CE QU'IL ASSEMBLE
    les 12 plans parlants  -> _essai-avatar/retours/planNN-omnihuman.mp4,
                              coupes a amorce + replique + queue
    les 7 plans de decor   -> 03-final/planNN.mp4 pour l'image,
                              PLUS audio/scenes/<scene>/NN-erzaehler.mp3
                              pour la NARRATION (01, 02, 03, 04, 07, 18, 19)

⚠️ LES CLIPS DE DECOR N'ONT AUCUNE PISTE SONORE, ET LEUR VOIX VIT AILLEURS.
   Premiere version : j'y ai mis du silence, et l'episode entier a perdu sa
   narration -- sept plans sur dix-neuf. Jacques, en le regardant : « il
   manque la narration », et « il manque un plan lorsqu'il repond qu'il vient
   de Montreal ». Le plan 07 EXISTE, c'est le narrateur entre la question
   d'Anna et la reponse de Mark ; muet, il se lit comme un trou.
   Un plan silencieux au montage ne signale rien : il passe pour une
   respiration voulue.

⚠️ TOUT EST RAMENE AU MEME FORMAT AVANT CONCATENATION. Les prises avatar
   sortent en 1088x1920 a 25 im/s, les plans de decor en 720x1280 a 24. Un
   concat de formats differents echoue, ou pire : il passe et le lecteur
   saute a chaque raccord.
"""
import argparse
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

ORDRE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
PARLANTS = {5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
L, H, IPS = 1080, 1920, 25


def a_du_son(F, src):
    r = subprocess.run([F, "-hide_banner", "-i", src],
                       capture_output=True, text=True, errors="ignore")
    return "Audio:" in r.stderr


def normaliser(F, src, dst, debut=None, duree=None):
    """⚠️ TOUT SEGMENT SORT AVEC UNE PISTE SONORE, MEME MUETTE.

    Les plans de decor de 03-final n'ont AUCUNE piste audio. Sans cette
    precaution, leurs segments sortaient en video seule, et le concat
    demuxer -- qui exige le meme nombre de flux partout -- laissait tomber
    le son de TOUT l'episode, sans une ligne d'avertissement. Le montage
    s'ouvrait normalement et il etait muet d'un bout a l'autre.
    """
    muet = not a_du_son(F, src)
    cmd = [F, "-y", "-v", "error"]
    if debut is not None:
        cmd += ["-ss", "%.3f" % debut]
    if duree is not None:
        cmd += ["-t", "%.3f" % duree]
    cmd += ["-i", src]
    if muet:
        cmd += ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"]
    cmd += ["-map", "0:v:0", "-map", "1:a:0" if muet else "0:a:0",
            "-vf", "scale=%d:%d:force_original_aspect_ratio=decrease,"
                   "pad=%d:%d:-1:-1:color=black,fps=%d" % (L, H, L, H, IPS),
            "-c:v", "libx264", "-crf", "18", "-preset", "medium",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
            "-shortest", dst]
    subprocess.run(cmd, check=True)


def narrer(F, src, voix, dst, duree, amorce):
    """L'image du decor, la narration posee dessus apres une courte amorce."""
    subprocess.run(
        [F, "-y", "-v", "error", "-i", src, "-i", voix,
         "-filter_complex",
         "[0:v]scale=%d:%d:force_original_aspect_ratio=decrease,"
         "pad=%d:%d:-1:-1:color=black,fps=%d[v];"
         "[1:a]adelay=%d:all=1,apad,aresample=44100[a]"
         % (L, H, L, H, IPS, int(round(amorce * 1000))),
         "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-crf", "18", "-preset", "medium",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-ar", "44100", "-ac", "2", "-t", "%.3f" % duree, dst], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--amorce", type=float, default=0.35)
    ap.add_argument("--queue", type=float, default=0.90)
    ap.add_argument("--sortie")
    a = ap.parse_args()

    F = M.ffmpeg()
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    tel = os.path.join(ep, "_a-televerser")
    ret = os.path.join(ep, "_essai-avatar", "retours")
    tmp = os.path.join(ep, "_montage-avatar")
    os.makedirs(tmp, exist_ok=True)

    morceaux, manquants, total, feuille = [], [], 0.0, []
    print("  plan  source            duree   ce qu'on garde")
    print("  " + "-" * 62)
    for n in ORDRE:
        dst = os.path.join(tmp, "plan%02d.mp4" % n)
        if n in PARLANTS:
            src = os.path.join(ret, "plan%02d-omnihuman.mp4" % n)
            piste = os.path.join(tel, "plan%02d-pleine.mp3" % n)
            if not os.path.exists(src):
                manquants.append(n)
                print("  %02d    MANQUANT -- la prise avatar n'est pas la" % n)
                continue
            tete, queue, _ = M.parole(F, piste)
            debut = max(0.0, tete - a.amorce)
            duree = (queue - debut) + a.queue
            duree = min(duree, M.duree(F, src) - debut)
            normaliser(F, src, dst, debut, duree)
            print("  %02d    avatar          %6.2f s   %.2f -> %.2f"
                  % (n, duree, debut, debut + duree))
        else:
            src = os.path.join(ep, "03-final", "plan%02d.mp4" % n)
            if not os.path.exists(src):
                manquants.append(n)
                print("  %02d    MANQUANT -- %s" % (n, os.path.basename(src)))
                continue
            voix = os.path.join(RACINE, "audio", "scenes", a.scene,
                                "%02d-erzaehler.mp3" % n)
            if not os.path.exists(voix):
                duree = M.duree(F, src)
                normaliser(F, src, dst)
                print("  %02d    decor           %6.2f s   ⚠️ sans narration"
                      % (n, duree))
            else:
                dv = M.duree(F, voix)
                duree = min(M.duree(F, src), a.amorce + dv + a.queue)
                narrer(F, src, voix, dst, duree, a.amorce)
                print("  %02d    decor + voix    %6.2f s   narration %.2f s"
                      % (n, duree, dv))
        # ⚠️ LE MONTAGE EST LE SEUL A SAVOIR OU COMMENCE CHAQUE PLAN.
        # Recalculer ces instants ailleurs, avec « les memes regles », c'est
        # se garantir qu'ils divergeront le jour ou l'une des deux change.
        # Il ecrit donc la feuille, et les sous-titres la lisent.
        feuille.append({"n": n, "debut": round(total, 3),
                        "duree": round(duree, 3),
                        "type": "replique" if n in PARLANTS else "narration"})
        morceaux.append(dst)
        total += duree

    if not morceaux:
        sys.exit("  Rien a monter.")

    liste = os.path.join(tmp, "_liste.txt")
    io.open(liste, "w", encoding="utf-8", newline="\n").write(
        "".join("file '%s'\n" % m.replace("\\", "/") for m in morceaux))
    dst = a.sortie or os.path.join(ep, "EPISODE-01-avatar.mp4")
    subprocess.run([F, "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", liste, "-c", "copy", dst], check=True)

    fjson = os.path.join(tmp, "_plans.json")
    io.open(fjson, "w", encoding="utf-8", newline="").write(
        json.dumps(feuille, ensure_ascii=False, indent=1) + "\n")

    print("\n  %s" % os.path.relpath(dst, RACINE))
    print("  %d plans, %.2f s   (feuille : %s)"
          % (len(morceaux), M.duree(F, dst), os.path.relpath(fjson, RACINE)))
    if manquants:
        print("  ⚠️ MANQUE : %s" % ", ".join("%02d" % n for n in manquants))


if __name__ == "__main__":
    main()
