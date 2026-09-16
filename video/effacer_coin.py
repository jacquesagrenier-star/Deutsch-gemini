# -*- coding: utf-8 -*-
"""Effacer un intrus au bord du cadre, sans repasser par le modele.

    python video/effacer_coin.py <clip.mp4>
    python video/effacer_coin.py <clip.mp4> --zone 90x450+0+0 --fondu 30
    python video/effacer_coin.py <clip.mp4> --mesurer      (ne modifie rien)

POURQUOI CET OUTIL EXISTE.

OmniHuman fait entrer, de temps en temps, quelqu'un qui ne devrait pas etre
la : une nuque, des cheveux, une epaule floue au bord du cadre. Le prompt
l'interdit sur dix lignes -- et c'est peut-etre ce qui l'appelle, ces modeles
n'ayant aucun canal pour les negations (le schema de l'API n'a ni
`negative_prompt` ni `seed`). Regenerer coute 0,70 $ et ne garantit rien : le
tirage suivant peut refaire la meme chose.

Or la camera de ces plans est VERROUILLEE et le fond y est un mur uni. Ce que
l'intrus recouvre ne bouge donc jamais : il suffit de recopier ce coin depuis
une image ou il est absent, sur toute la duree. Recopier un mur immobile sur
un mur immobile ne se voit pas.

⚠️ CE QUE CET OUTIL NE SAIT PAS FAIRE, ET QU'IL NE FAUT PAS LUI DEMANDER.
   Il ne repare qu'un fond FIXE. Si l'intrus passe devant le personnage, s'il
   traverse une zone ou quelque chose bouge (la main, la feuille, un reflet),
   le rustine gelerait ce mouvement. Dans ce cas-la, il faut regenerer.
   `--mesurer` sert justement a verifier d'abord OU et QUAND ca bouge.

⚠️ ET L'IMAGE DE REFERENCE N'EST PAS TOUJOURS LA PREMIERE. L'intrus arrive
   souvent apres une demi-seconde, mais pas toujours : `--mesurer` compare
   chaque image a la premiere, et si la premiere est deja sale, tout l'ecart
   se lit a l'envers. Regarder la sortie avant de faire confiance.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ffmpeg(args, muet=True):
    c = ["ffmpeg", "-v", "error" if muet else "info", "-y"] + args
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode:
        sys.exit("  ffmpeg a echoue :\n  " + (r.stderr or "")[-600:])
    return r


def dimensions(clip):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream=width,height,nb_frames",
                        "-of", "csv=p=0", clip], capture_output=True, text=True)
    p = (r.stdout or "").strip().split(",")
    return int(p[0]), int(p[1])


def mesurer(clip, large, haut):
    """Ou et quand le bord change-t-il ? Gratuit, et a lire AVANT de rustiner."""
    import io
    W, H = 80, 120
    brut = os.path.join(os.environ.get("TEMP", "."), "_coin.raw")
    ffmpeg(["-i", clip, "-vf",
            "crop=%d:%d:0:0,format=gray,scale=%d:%d" % (large, haut, W, H),
            "-f", "rawvideo", brut])
    d = io.open(brut, "rb").read()
    n = len(d) // (W * H)
    ref = d[:W * H]
    print("  %d images, zone %dx%d en haut a gauche" % (n, large, haut))
    vu = False
    for i in range(n):
        f = d[i * W * H:(i + 1) * W * H]
        forts = [k for k in range(W * H) if abs(f[k] - ref[k]) > 28]
        if not forts:
            continue
        vu = True
        xs = [k % W for k in forts]
        ys = [k // W for k in forts]
        if i % 5 == 0:
            print("    %5.2f s  %4d px   x 0-%3d px   y 0-%3d px"
                  % (i / 25.0, len(forts),
                     max(xs) * large // W, max(ys) * haut // H))
    if not vu:
        print("    rien ne change dans cette zone.")
    os.remove(brut)


def bouge(clip, x, y, large, haut, image_ref):
    """De combien la zone s'ecarte-t-elle de l'image qu'on va y recopier ?

    ⚠️ CETTE MESURE EST OBLIGATOIRE, ET ELLE EST NEE D'UNE FAUTE. Le
    16 septembre 2026 j'ai recopie la zone des MAINS du plan 17 depuis une
    image plus tardive, pour que la feuille soit la des le debut. Jacques :
    << c'est comme une image par-dessus l'autre, on voit que ce n'est pas
    naturel ; sa main droite a l'air immobile, et on voit une main qui
    apparait en dessous. >> Il avait raison. Mesure faite APRES coup : la zone
    s'ecartait de 54 a 57 niveaux de gris pendant la premiere demi-seconde --
    la main bougeait enormement.

    Le mode d'emploi de cet outil disait deja, des sa premiere version, qu'il
    ne repare qu'un fond FIXE. Je l'avais ecrit, et je l'ai quand meme fait.
    D'ou cette mesure, qui n'est plus une recommandation mais une porte.
    """
    import io as _io
    W, H = 60, 60
    brut = os.path.join(os.environ.get("TEMP", "."), "_zone.raw")
    ffmpeg(["-i", clip, "-vf",
            "crop=%d:%d:%d:%d,format=gray,scale=%d:%d"
            % (large, haut, x, y, W, H), "-f", "rawvideo", brut])
    d = _io.open(brut, "rb").read()
    n = len(d) // (W * H)
    i_ref = min(max(0, int(image_ref * 25)), n - 1)
    ref = d[i_ref * W * H:(i_ref + 1) * W * H]
    ecarts = []
    for i in range(n):
        f = d[i * W * H:(i + 1) * W * H]
        ecarts.append(sum(abs(f[k] - ref[k]) for k in range(W * H)) / float(W * H))
    os.remove(brut)

    # ⚠️ CE QU'IL FAUT MESURER N'EST PAS << LA ZONE CHANGE-T-ELLE >>. Bien sur
    # qu'elle change : l'intrus qui arrive EST un changement. La premiere
    # version de ce garde-fou refusait donc TOUS les cas legitimes, y compris
    # celui qu'il etait cense autoriser.
    #
    # La vraie question est : LE FOND, LUI, EST-IL IMMOBILE ? On la lit dans la
    # fenetre PROPRE -- de la premiere image jusqu'a l'arrivee de l'intrus. Si
    # rien n'y bouge et que l'image de reference est dedans, la rustine recopie
    # un fond fixe sur un fond fixe, et ne se voit pas. Si l'image de reference
    # est PRISE APRES cette fenetre -- ce que j'ai fait sur les mains du plan
    # 17 -- alors on colle du tard sur du tot, et ca se voit tout de suite.
    arrivee = n
    for i, e in enumerate(ecarts):
        if e > 12:
            arrivee = i
            break
    propre = ecarts[:arrivee] or [0.0]
    remuant = max(propre)
    quand = arrivee / 25.0
    hors_fenetre = i_ref >= arrivee
    return remuant, quand, hors_fenetre


def effacer(clip, x, y, large, haut, fondu, image_ref, forcer=False):
    W, H = dimensions(clip)
    if x + large > W or y + haut > H:
        sys.exit("  la zone deborde du cadre (%dx%d)." % (W, H))

    remuant, arrivee, hors_fenetre = bouge(clip, x, y, large, haut, image_ref)
    print("  fond propre jusqu'a %.2f s, et il y remue de %.1f niveaux de gris"
          % (arrivee, remuant))
    if not forcer and (remuant > 10 or hors_fenetre):
        sys.exit(
            "\n  RUSTINE REFUSEE.\n"
            + ("  Le fond bouge de %.1f dans la fenetre propre (au-dela de 10,\n"
               "  ce n'est plus un fond fixe).\n" % remuant if remuant > 10 else "")
            + ("  L'image de reference (%.2f s) est PRISE APRES l'arrivee de\n"
               "  l'intrus (%.2f s) : on collerait du tard sur du tot. C'est\n"
               "  exactement la faute des mains du plan 17, le 16 sept. 2026,\n"
               "  et elle s'est vue tout de suite.\n" % (image_ref, arrivee)
               if hors_fenetre else "")
            + "  --forcer si tu sais pourquoi.")

    base = os.path.splitext(clip)[0]
    garde = base + "-AVANT-coin.mp4"
    if not os.path.exists(garde):
        shutil.copy2(clip, garde)
        print("  prise d'origine gardee : %s" % os.path.basename(garde))

    tmp = os.path.join(os.environ.get("TEMP", "."), "_ref.png")
    rustine = os.path.join(os.environ.get("TEMP", "."), "_rustine.png")
    ffmpeg(["-ss", str(image_ref), "-i", clip, "-vframes", "1", tmp])

    # Le fondu vit dans l'alpha, et seulement sur les cotes INTERIEURS.
    #
    # ⚠️ LA PREMIERE VERSION FONDAIT TOUJOURS A DROITE ET EN BAS. Pour un coin
    # en haut a gauche c'etait juste ; pour un coin en BAS a gauche, le fondu
    # du bas tombait sur le bord de l'image -- la rustine s'y effacait, et
    # l'intrus reapparaissait sur les trente derniers pixels, exactement la ou
    # on croyait l'avoir retire. Un cote colle au bord du cadre ne se fond pas :
    # il n'a rien a rejoindre.
    cotes = []
    if x > 0:
        cotes.append("X/%d" % fondu)
    if x + large < W:
        cotes.append("(%d-X)/%d" % (large, fondu))
    if y > 0:
        cotes.append("Y/%d" % fondu)
    if y + haut < H:
        cotes.append("(%d-Y)/%d" % (haut, fondu))
    # min() de ffmpeg ne prend que deux arguments : on les emboite.
    expr = "1"
    for c in cotes:
        expr = "min(%s,%s)" % (expr, c)
    alpha = "255*" + expr
    ffmpeg(["-i", tmp, "-vf",
            "crop=%d:%d:%d:%d,format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='%s'"
            % (large, haut, x, y, alpha), rustine])

    sortie = base + "-propre.mp4"
    ffmpeg(["-i", clip, "-i", rustine, "-filter_complex",
            "[0:v][1:v]overlay=%d:%d" % (x, y),
            "-c:a", "copy", "-c:v", "libx264", "-crf", "17", "-preset", "slow",
            "-pix_fmt", "yuv420p", sortie])
    os.replace(sortie, clip)
    for f in (tmp, rustine):
        try:
            os.remove(f)
        except OSError:
            pass
    print("  zone %dx%d en (%d,%d) recouverte depuis l'image de %.2f s, fondu %d px"
          % (large, haut, x, y, image_ref, fondu))
    print("  ecrit : %s" % os.path.basename(clip))


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("clip")
    p.add_argument("--zone", default="90x450+0+0",
                   help="LxH+X+Y en pixels (defaut 90x450+0+0)")
    p.add_argument("--fondu", type=int, default=30,
                   help="largeur du fondu des bords interieurs, en pixels")
    p.add_argument("--ref", type=float, default=0.0,
                   help="seconde de l'image PROPRE a recopier (defaut 0)")
    p.add_argument("--mesurer", action="store_true",
                   help="dire ou et quand le bord change, sans rien modifier")
    p.add_argument("--forcer", action="store_true",
                   help="rustiner une zone qui bouge (voir bouge())")
    a = p.parse_args()

    if not os.path.exists(a.clip):
        sys.exit("  introuvable : %s" % a.clip)

    m = re.match(r"^(\d+)x(\d+)\+(\d+)\+(\d+)$", a.zone)
    if not m:
        sys.exit("  --zone attend la forme LxH+X+Y, par exemple 90x450+0+0")
    large, haut, x, y = (int(g) for g in m.groups())

    if a.mesurer:
        mesurer(a.clip, max(large, 400), max(haut, 600))
        return
    effacer(a.clip, x, y, large, haut, a.fondu, a.ref, a.forcer)


if __name__ == "__main__":
    main()
