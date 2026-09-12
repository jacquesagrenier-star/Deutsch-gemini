# -*- coding: utf-8 -*-
"""Ranger une prise revenue, en VERIFIANT d'abord de quel plan elle est.

    python video/importer_prise.py                (tout ce qui traine)
    python video/importer_prise.py --source <dossier>

⚠️ POURQUOI ON NE SE FIE PAS AU NOM DU FICHIER.
    Le 12 septembre 2026, une prise du plan 16 a ete sauvegardee sous le nom
    « Mark12 ». Je l'ai mesuree contre la ligne de base du plan 12, j'ai
    trouve 1,39 d'ecart avec la prise precedente, et j'en ai tire une
    conclusion spectaculaire : la dispersion du modele ecrasait tous nos
    effets. J'ai releve les seuils de bruit, reecrit le journal, pousse le
    commit. Tout etait faux.

    UN FICHIER MAL NOMME EST UNE MESURE FAUSSE QUI SE PRESENTE BIEN : des
    chiffres plausibles, un verdict lisible, et une conclusion d'autant plus
    seduisante qu'elle etait surprenante. Rien dans le resultat n'avertit.

    L'identite se lit dans le SON : OmniHuman laisse passer la piste telle
    quelle (verifie, correlation 1,0000). On correle donc la piste du clip
    avec les douze pistes televersees, et celle qui repond 1,0 dit le plan.
    Trente secondes de calcul contre une journee de conclusions fausses.
"""
import argparse
import os
import shutil
import struct
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

PARLANTS = [5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
SEUIL = 0.90           # en dessous, on ne range rien : on demande


def ech(F, p, sr=16000):
    r = subprocess.run([F, "-hide_banner", "-nostats", "-loglevel", "error",
                        "-i", p, "-map", "0:a", "-ac", "1", "-ar", str(sr),
                        "-f", "s16le", "-"], capture_output=True)
    return list(struct.unpack("<%dh" % (len(r.stdout) // 2), r.stdout))


def correle(x, y):
    n = min(len(x), len(y))
    if n < 8000:
        return 0.0
    x, y = x[:n], y[:n]
    mx, my = sum(x) / n, sum(y) / n
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    dx = sum((a - mx) ** 2 for a in x) ** 0.5
    dy = sum((b - my) ** 2 for b in y) ** 0.5
    return num / (dx * dy) if dx and dy else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=os.path.join(
        os.path.expanduser("~"), "OneDrive", "Desktop", "episodes"))
    ap.add_argument("--scene", default="01-ankunft-berlin")
    a = ap.parse_args()

    F = M.ffmpeg()
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    tel = os.path.join(ep, "_a-televerser")
    ret = os.path.join(ep, "_essai-avatar", "retours")
    os.makedirs(ret, exist_ok=True)

    pistes = {}
    for n in PARLANTS:
        p = os.path.join(tel, "plan%02d-pleine.mp3" % n)
        if os.path.exists(p):
            pistes[n] = ech(F, p)
    if not pistes:
        sys.exit("  Aucune piste de reference dans _a-televerser.")

    trouves = sorted((f for f in os.listdir(a.source) if f.lower().endswith(".mp4")),
                     key=lambda f: os.path.getmtime(os.path.join(a.source, f)))
    if not trouves:
        sys.exit("  Rien a importer dans %s" % a.source)

    for f in trouves:
        src = os.path.join(a.source, f)
        x = ech(F, src)
        scores = sorted(((correle(x, y), n) for n, y in pistes.items()),
                        reverse=True)
        c, n = scores[0]
        if c < SEUIL:
            print("  %-16s  INCERTAIN -- meilleur candidat plan %02d a %.3f."
                  % (f, n, c))
            print("  %-16s  rien range. Verifier a la main." % "")
            continue
        dst = os.path.join(ret, "plan%02d-omnihuman.mp4" % n)
        remplace = os.path.exists(dst)
        # ⚠️ LA PRISE GARDE SON IMAGE ; LE SON VIENT TOUJOURS DE NOTRE PISTE.
        # OmniHuman renvoie l'audio qu'on lui a donne, inchange (verifie,
        # correlation 1,0000). Mais notre piste a pu etre CORRIGEE depuis --
        # un « tss » ou un « toc » retire par nettoyer_queue.py. Le 12
        # septembre 2026, un simple re-import a ecrase trois pistes
        # nettoyees par leurs versions d'origine, en silence. Re-poser notre
        # piste a chaque import rend la chose impossible.
        subprocess.run([F, "-y", "-v", "error", "-i", src,
                        "-i", os.path.join(tel, "plan%02d-pleine.mp3" % n),
                        "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                        "-c:a", "aac", "-b:a", "160k", "-shortest", dst],
                       check=True)
        print("  %-16s -> plan %02d  (correlation %.4f)%s"
              % (f, n, c, "   ⚠️ remplace la precedente" if remplace else ""))
        print("  %-16s    python video/essai_avatar.py --plan %d --mesurer %s"
              % ("", n, os.path.relpath(dst, RACINE).replace("\\", "/")))


if __name__ == "__main__":
    main()
