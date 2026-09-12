# -*- coding: utf-8 -*-
"""Les deux saletes de fin de phrase -- le « tss » et le « toc ».

    python video/nettoyer_queue.py                 (rapport seul)
    python video/nettoyer_queue.py --appliquer     (nettoie les pistes)
    python video/nettoyer_queue.py --appliquer --clips
                                   (et remplace le son des prises revenues)

CE QU'ON CHERCHE
    Jacques, 12 septembre 2026, sur le plan 11 : « il y a un petit tss a la
    fin de sa phrase ». Mesure de la piste :

        2,89 s   la voix s'eteint
        2,90 s   silence
        2,98 s   un souffle isole reparait, faible en energie mais DOMINE
        3,06 s   PAR L'AIGU (rapport aigu/energie de 1,2 a 1,6)

    C'est le « t » final de « Burgeramt » relache tout seul, 90 ms apres le
    mot. Detache de sa syllabe, il s'entend comme un sifflement.

⚠️ LE CRITERE N'EST PAS L'ENERGIE, C'EST LA COULEUR.
    Ce souffle est BEAUCOUP plus faible que la parole -- un seuil de volume
    ne le distingue pas d'un silence. Ce qui le trahit, c'est que son energie
    est dans l'aigu : on compare le signal a sa difference premiere, qui
    accentue les hautes frequences. Sur de la voix ce rapport tourne autour
    de 0,1 a 0,4 ; sur ce souffle il depasse 1,0.

⚠️ ON NE TOUCHE QU'APRES LA DERNIERE VOIX, jamais dedans. Un « s » ou un
    « ch » AU MILIEU d'un mot a exactement la meme signature -- c'est de la
    parole, et l'effacer mangerait une consonne. La fenetre de travail
    commence apres la derniere baisse durable d'energie.

⚠️ ET ON RAMPE LES BORDS. Couper net dans un signal non nul produit un clic,
    qui est PIRE que le souffle qu'on enleve. 10 ms de fondu de chaque cote.

    Le son des prises deja revenues peut etre remplace sans les regenerer :
    OmniHuman laisse passer l'audio tel quel (verifie, correlation 1,0000),
    et le souffle tombe dans une zone ou la bouche est fermee.
"""
import argparse
import math
import os
import struct
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

SR = 16000
PAS = 0.01                 # la fenetre d'analyse
RAPPORT = 1.0              # aigu/energie au-dela duquel c'est un souffle
PLANCHER = 5.0             # en dessous, c'est du silence, rien a enlever
PLAFOND = 1500.0           # au-dessus, c'est de la parole : on n'y touche pas
CALME = 200.0              # l'energie sous laquelle la voix est consideree finie
# ⚠️ DEUX SEUILS, ET ILS NE PEUVENT PAS ETRE LE MEME.
# RAPPORT identifie le souffle ; VOIX_SOURDE ferme la parole. Avec un seuil
# unique a 1,0, une fenetre du souffle a 0,99 comptait encore comme de la
# voix et repoussait la fenetre de recherche APRES ce qu'on cherchait. La
# voix reelle tient entre 0,05 et 0,4 ; le souffle depasse 0,5. On ferme
# donc la parole a 0,5 et on ne reconnait le souffle qu'au-dessus de 1,0 --
# la bande entre les deux n'est ni l'un ni l'autre, et on n'y touche pas.
VOIX_SOURDE = 0.5          # au-dessus, ce n'est plus de la voix franche
FONDU = 0.010              # 10 ms de rampe de chaque cote

# ⚠️ LE « TOC » EST UN AUTRE DEFAUT, ET IL SE CACHE A 16 kHz.
# Jacques, sur le plan 09 : « il semble y avoir un toc a la fin de sa
# phrase ». Le detecteur de souffle ne voyait rien, et un controle de
# coupure nette a 16 kHz concluait « aucune » -- FAUX. A 44,1 kHz la
# fenetre de 2,535 s montre une crete de 9 226 pour une energie de 257 :
# une impulsion de quelques echantillons dans le silence. Un clic.
#
# ⚠️ UNE ANALYSE A 16 kHz LISSE LES TRANSITOIRES BREFS ET LES FAIT
# DISPARAITRE. Pour chercher un clic, il faut la frequence pleine.
#
# La signature d'un clic est le RAPPORT crete/energie : la voix tient
# autour de 2 a 5, un clic depasse 25. Le remede n'est pas de l'effacer
# -- ce serait un trou -- mais de FONDRE la fin juste avant lui.
SR_CLIC = 44100
CLIC_RAPPORT = 25.0        # crete/energie au-dela duquel c'est une impulsion
CLIC_CRETE = 1500          # en dessous, meme pointu, ca ne s'entend pas
CLIC_FONDU = 0.020         # 20 ms de descente avant l'impulsion
PARLANTS = [5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


def lire(F, chemin, sr=SR):
    r = subprocess.run([F, "-hide_banner", "-nostats", "-loglevel", "error",
                        "-i", chemin, "-map", "0:a", "-ac", "1", "-ar", str(sr),
                        "-f", "s16le", "-"], capture_output=True)
    return list(struct.unpack("<%dh" % (len(r.stdout) // 2), r.stdout))


def souffles(x, sr=SR):
    """Les fenetres (debut, fin) a effacer, apres la derniere vraie voix."""
    n = int(sr * PAS)
    prof = []
    for i in range(0, len(x) - n, n):
        b = x[i:i + n]
        e = sum(abs(v) for v in b) / n
        hf = sum(abs(b[k + 1] - b[k]) for k in range(n - 1)) / (n - 1)
        prof.append((i / float(sr), e, hf))
    if not prof:
        return []

    # ⚠️ LA FIN DE LA VOIX SE DEFINIT PAR LA COULEUR AUTANT QUE PAR LE VOLUME.
    # Premiere version : « la derniere fenetre dont l'energie depasse CALME ».
    # Elle ne trouvait rien -- parce que LE SOUFFLE LUI-MEME passait ce seuil
    # (jusqu'a 1047 sur le plan 11) et devenait donc la fin de la voix. La
    # fenetre de recherche commencait apres ce qu'on cherchait.
    # La fin de la voix est la derniere fenetre qui est forte ET SOURDE.
    fin_voix = 0.0
    for t, e, hf in prof:
        if e > CALME and hf / max(e, 1.0) < VOIX_SOURDE:
            fin_voix = t
    depart = fin_voix + 0.04

    zones, cour = [], None
    for t, e, hf in prof:
        if t < depart:
            continue
        souffle = PLANCHER < e < PLAFOND and hf / e > RAPPORT
        if souffle and cour is None:
            cour = [t, t + PAS]
        elif souffle:
            cour[1] = t + PAS
        elif cour is not None:
            zones.append(tuple(cour))
            cour = None
    if cour is not None:
        zones.append(tuple(cour))
    return [z for z in zones if z[1] - z[0] >= 0.03]


def clic(F, chemin):
    """L'instant du premier clic apres la parole, ou None. Pleine frequence."""
    r = subprocess.run([F, "-hide_banner", "-nostats", "-loglevel", "error",
                        "-i", chemin, "-map", "0:a", "-ac", "1",
                        "-ar", str(SR_CLIC), "-f", "s16le", "-"],
                       capture_output=True)
    x = list(struct.unpack("<%dh" % (len(r.stdout) // 2), r.stdout))
    _, queue, _ = M.parole(F, chemin)
    w = int(SR_CLIC * 0.005)
    for i in range(max(0, int((queue - 0.05) * SR_CLIC)), len(x) - w, w):
        b = x[i:i + w]
        crete = max(abs(v) for v in b)
        if crete < CLIC_CRETE:
            continue
        e = sum(abs(v) for v in b) / w
        if crete / max(e, 1.0) > CLIC_RAPPORT:
            return i / float(SR_CLIC), crete, crete / max(e, 1.0)
    return None


def fondre_fin(F, chemin, t_clic):
    """Fondre les 20 ms avant le clic, puis silence. Pas d'effacement sec."""
    d = max(0.0, t_clic - CLIC_FONDU)
    tmp = chemin + ".tmp.mp3"
    subprocess.run([F, "-y", "-v", "error", "-i", chemin,
                    "-af", "afade=t=out:st=%.4f:d=%.4f" % (d, CLIC_FONDU),
                    "-ar", "44100", "-b:a", "192k", tmp], check=True)
    os.replace(tmp, chemin)


def effacer(x, zones, sr=SR):
    y = list(x)
    f = max(1, int(sr * FONDU))
    for d, fin in zones:
        a, b = int(d * sr), min(len(y), int(fin * sr))
        for k in range(a, b):
            y[k] = 0
        for k in range(max(0, a - f), a):          # rampe descendante
            y[k] = int(y[k] * (0.5 - 0.5 * math.cos(math.pi * (a - k) / f)))
        for k in range(b, min(len(y), b + f)):     # rampe montante
            y[k] = int(y[k] * (0.5 - 0.5 * math.cos(math.pi * (k - b) / f)))
    return y


def ecrire(F, x, dst, sr=SR):
    tmp = dst + ".raw"
    with open(tmp, "wb") as f:
        f.write(struct.pack("<%dh" % len(x), *x))
    subprocess.run([F, "-y", "-v", "error", "-f", "s16le", "-ar", str(sr),
                    "-ac", "1", "-i", tmp, "-ar", "44100", "-b:a", "192k",
                    dst], check=True)
    os.remove(tmp)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--appliquer", action="store_true")
    ap.add_argument("--clips", action="store_true",
                    help="remplacer aussi le son des prises deja revenues")
    a = ap.parse_args()

    F = M.ffmpeg()
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    tel = os.path.join(ep, "_a-televerser")
    ret = os.path.join(ep, "_essai-avatar", "retours")

    print("  plan   souffles trouves apres la voix")
    print("  " + "-" * 52)
    total = 0
    for n in PARLANTS:
        p = os.path.join(tel, "plan%02d-pleine.mp3" % n)
        if not os.path.exists(p):
            continue
        x = lire(F, p)
        z = souffles(x)
        c = clic(F, p)
        if not z and not c:
            print("  %02d     -" % n)
            continue
        if c:
            print("  %02d     CLIC a %.3f s  (crete %d, rapport %.0f)"
                  % (n, c[0], c[1], c[2]))
            if a.appliquer:
                fondre_fin(F, p, c[0])
                print("         fondu avant le clic")
                x = lire(F, p)
        if not z:
            if a.appliquer and c:
                total += 1
                clip = os.path.join(ret, "plan%02d-omnihuman.mp4" % n)
                if a.clips and os.path.exists(clip):
                    tmp = clip + ".tmp.mp4"
                    subprocess.run([F, "-y", "-v", "error", "-i", clip, "-i", p,
                                    "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                                    "-c:a", "aac", "-b:a", "160k", "-shortest", tmp],
                                   check=True)
                    os.replace(tmp, clip)
                    print("         son remplace dans la prise revenue")
            continue
        total += len(z)
        print("  %02d     %s" % (n, ", ".join("%.2f-%.2f s" % w for w in z)))
        if not a.appliquer:
            continue
        ecrire(F, effacer(x, z), p)
        print("         piste nettoyee")

        clip = os.path.join(ret, "plan%02d-omnihuman.mp4" % n)
        if a.clips and os.path.exists(clip):
            tmp = clip + ".tmp.mp4"
            subprocess.run([F, "-y", "-v", "error", "-i", clip, "-i", p,
                            "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                            "-c:a", "aac", "-b:a", "160k", "-shortest", tmp],
                           check=True)
            os.replace(tmp, clip)
            print("         son remplace dans la prise revenue")

    print("\n  %d souffle(s) au total." % total)
    if total and not a.appliquer:
        print("  Relancer avec --appliquer (et --clips pour les prises revenues).")


if __name__ == "__main__":
    main()
