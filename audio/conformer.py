# -*- coding: utf-8 -*-
"""Etire la voix pour qu'elle epouse la bouche du plan -- la methode ADR.

    python audio/conformer.py --plan 11 --prise plan11-03.mp4
    python audio/conformer.py --plan 11 --prise plan11-03.mp4 --limite 0.20

CE QUE FONT LES MONTEURS, ET QU'ON NE FAISAIT PAS
    « Lock picture first, conform audio to picture second, verify on consonants
    third. » Quand une replique ne colle pas a l'image, le cinema ne retourne
    pas le plan : il refait le son pour qu'il colle. C'est le doublage, l'ADR,
    et c'est un siecle de metier.

    Le 9 septembre 2026 on a fait l'inverse toute la journee -- forcer l'image a
    suivre le son, et repayer l'image quand ca ratait. Les praticiens le
    nomment d'ailleurs comme l'erreur type : « regenerating video until the
    mouth happens to match burns credits and never fully locks ».

CE QUE CE SCRIPT NE DEGRADE PAS
    La hauteur ni le timbre : atempo change la vitesse sans toucher au pitch.
    C'est VOTRE enregistrement ElevenLabs, avec sa prononciation exacte --
    contrairement au Speech-to-Speech, ou Jacques avait entendu tout de suite
    que la voix perdait en clarte.

LA LIMITE, ET D'OU ELLE VIENT
    Un etirement s'entend. La limite est a 25 %, et c'est un chiffre ECOUTE :
    le plan 11 conforme a +25,7 % a passe l'oreille de Jacques. J'avais
    d'abord pose 15 % au juge, comme tous les autres seuils de la journee --
    et comme eux il etait faux.

    Au-dela, le script refuse plutot que de rendre une piste molle en silence.

    Un plan tres etire n'est pas a conformer, il est a refaire : le plan 12,
    dont la bouche articule 2,4 fois la replique, ne se rattrape pas ici.
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


def atempo(facteur):
    """atempo n'accepte que 0,5 a 2,0 ; on enchaine si besoin."""
    f, chaine = facteur, []
    while f < 0.5:
        chaine.append("atempo=0.5")
        f /= 0.5
    while f > 2.0:
        chaine.append("atempo=2.0")
        f /= 2.0
    chaine.append("atempo=%.6f" % f)
    return ",".join(chaine)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--plan", type=int, required=True)
    p.add_argument("--prise", required=True, help="le nom du fichier dans 02-prises")
    p.add_argument("--scene", default="01-ankunft-berlin")
    # 25 %, ET C'EST UN CHIFFRE ECOUTE, PAS SUPPOSE. J'avais pose 15 % au
    # jugé. Le plan 11 conforme a +25,7 % a ete valide a l'oreille par Jacques
    # le 9 septembre 2026 -- sa seule reserve portait sur un clic de fin, qui
    # venait d'ailleurs. Tous les autres seuils de la journee ont ete faux ;
    # celui-ci vient d'une ecoute.
    p.add_argument("--limite", type=float, default=0.25,
                   help="etirement maximal accepte (0,25 = 25 %%)")
    p.add_argument("--queue", type=float, default=0.6)
    a = p.parse_args()

    F = M.ffmpeg()
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    pr = os.path.join(ep, "02-prises")
    clip = os.path.join(pr, a.prise)
    if not os.path.exists(clip):
        sys.exit("  Introuvable : %s" % clip)

    fiche = os.path.join(pr, "_parole.json")
    par = json.load(io.open(fiche, encoding="utf-8")) if os.path.exists(fiche) else {}
    if a.prise not in par:
        sys.exit("  Pas de mesure de bouche pour %s dans _parole.json.\n"
                 "  Elle s'ecrit au rapatriement -- la prise est-elle anterieure ?"
                 % a.prise)
    b0, b1 = par[a.prise]["bouche"]

    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                          encoding="utf-8"))
    p_ = next(x for x in d["plans"] if x["n"] == a.plan)
    voix = os.path.join(RACINE, "audio", "scenes", a.scene,
                        "%02d-%s.mp3" % (a.plan, p_["locuteur"]))
    # parole_nette : sans le bruit isole qu'ElevenLabs laisse parfois
    # apres le dernier mot. C'etait la source du « tss ».
    tete, queue, _ = M.parole_nette(F, voix)
    dite, articulee = queue - tete, b1 - b0
    facteur = dite / articulee            # <1 : on ralentit la voix

    print("  plan %02d   << %s >>" % (a.plan, p_["de"]))
    print("  la bouche articule %.2f s   la voix en dit %.2f s" % (articulee, dite))
    print("  etirement necessaire : %+.1f %%" % ((1 / facteur - 1) * 100))
    if abs(1 / facteur - 1) > a.limite:
        print()
        print("  REFUS : au-dela de %.0f %% l'etirement s'entend -- la diction"
              " traine." % (a.limite * 100))
        print("  Cette prise est a refaire, pas a conformer.")
        return 1

    # ⚠️ GARDER UNE MARGE AUTOUR DE LA PAROLE. Le seuil de detection ne voit
    # pas le relachement d'une consonne finale : « Bürgeramt » finit sur un t
    # presque muet, et le couper au ras produit un clic -- Jacques, a la
    # premiere ecoute : « juste a la fin il y a un petit tss ». On prend donc
    # 80 ms de part et d'autre, et on termine par un fondu de 15 ms.
    MARGE, FONDU = 0.08, 0.015
    tmp = os.path.join(ep, "_montage")
    os.makedirs(tmp, exist_ok=True)
    # On etire la voix NUE (silence retire), puis on la pose a l'attaque de la
    # bouche : etirer le silence avec elle deplacerait l'attaque.
    etiree = os.path.join(tmp, "conforme%02d.mp3" % a.plan)
    deb = max(0.0, tete - MARGE)
    fin_v = queue + MARGE
    duree_etiree = (fin_v - deb) / facteur
    subprocess.run([F, "-y", "-v", "error", "-ss", "%.3f" % deb,
                    "-to", "%.3f" % fin_v, "-i", voix,
                    "-af", "%s,afade=t=out:st=%.3f:d=%.3f"
                    % (atempo(facteur), max(0.0, duree_etiree - FONDU), FONDU),
                    "-ar", "44100", "-ac", "1",
                    "-b:a", "160k", etiree], check=True)
    v0, v1, _ = M.parole(F, etiree)
    print("  voix etiree : %.2f s   (visait %.2f s)" % (v1 - v0, articulee))

    fin = min(M.duree(F, clip), b1 + a.queue)
    out = os.path.join(ep, "plan%02d-conforme.mp4" % a.plan)
    subprocess.run([F, "-y", "-v", "error", "-i", clip, "-i", etiree,
                    "-filter_complex", "[1:a]adelay=%d:all=1,apad[a]"
                    % int(round(max(0.0, b0 - v0) * 1000)),
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                    "-t", "%.3f" % fin, out], check=True)
    print("  ->  %s" % os.path.relpath(out, RACINE))
    print("  A ECOUTER : la diction traine-t-elle ?")
    return 0


if __name__ == "__main__":
    sys.exit(main())
