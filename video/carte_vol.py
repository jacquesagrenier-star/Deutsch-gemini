# -*- coding: utf-8 -*-
"""Le plan de carte : Montreal -> Berlin, en pointilles.

    python carte_vol.py --sortie plan00-carte.mp4

POURQUOI DESSINE ET NON GENERE
    C'est le seul type de plan ou l'outillage bat le modele genratif a tous
    les coups. Les cartes, les noms de villes et les traits de cote sont
    exactement ce que ces modeles ratent : on obtient un « MONTREAL »
    approximatif sur un continent qui n'existe pas, et il faut vingt essais
    pour s'en apercevoir. Ici : zero credit, zero essai, et le trait tombe au
    pixel pres.

CE QU'ON NE DESSINE PAS, ET C'EST UN CHOIX
    Pas de carte du monde. Sans un fond cartographique juste, une cote
    approximative se lit comme une faute -- et un apprenant qui vient d'un
    de ces pays la voit. On garde donc l'abstraction honnete : deux points
    nommes, un arc, une grille de meridiens. Personne ne peut y trouver une
    erreur de geographie, parce qu'on n'en affirme aucune.

LA DISTANCE EST CALCULEE, PAS INVENTEE
    Haversine sur les coordonnees reelles des deux aeroports. Un nombre faux
    sur un plan de trois secondes est une faute qui dure tout l'episode.
"""
import argparse
import math
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

L, H, IPS = 1080, 1920, 25
ENCRE = (28, 36, 48)
PAPIER = (242, 238, 226)
AMBRE = (232, 162, 58)
SEPIA = (107, 101, 88)

YUL = (45.4706, -73.7408)   # Montreal-Trudeau
BER = (52.3667, 13.5033)    # Berlin Brandenburg


def km(a, b):
    R = 6371.0
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    dp = p2 - p1
    dl = math.radians(b[1] - a[1])
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def police(taille, gras=True):
    for nom in (("seguisb.ttf" if gras else "segoeui.ttf"),
                ("arialbd.ttf" if gras else "arial.ttf"),
                "DejaVuSans-Bold.ttf" if gras else "DejaVuSans.ttf"):
        for dossier in ("C:/Windows/Fonts/", "/usr/share/fonts/truetype/dejavu/", ""):
            try:
                return ImageFont.truetype(dossier + nom, taille)
            except Exception:
                continue
    return ImageFont.load_default()


def bezier(t, p0, p1, p2):
    u = 1 - t
    return (u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
            u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1])


def lisser(x):
    """Depart et arrivee doux : l'avion accelere puis se pose."""
    return x * x * (3 - 2 * x)


def dessiner(i, n, d_km):
    im = Image.new("RGB", (L, H), ENCRE)
    g = ImageDraw.Draw(im, "RGBA")
    t = i / (n - 1)

    # --- les meridiens, tres faibles : ils disent « la Terre » sans rien affirmer
    entree = min(1.0, t / 0.12)
    for k in range(-3, 4):
        x = L // 2 + k * 150
        a = int(22 * entree * (1 - abs(k) / 5.0))
        g.line([(x, 300), (x, H - 300)], fill=(242, 238, 226, a), width=1)
    for k in range(5):
        y = 520 + k * 220
        g.line([(80, y), (L - 80, y)], fill=(242, 238, 226, int(16 * entree)), width=1)

    A = (210, 1180)                     # Montreal, en bas a gauche
    B = (880, 760)                      # Berlin, en haut a droite
    C = ((A[0] + B[0]) / 2, A[1] - 470)  # le ventre de l'arc : la courbure du globe

    # --- l'arc en pointilles, qui se dessine
    av = lisser(max(0.0, min(1.0, (t - 0.10) / 0.62)))
    pas, saut, pos = 9, 16, 0.0
    trace = []
    while pos < 1.0:
        trace.append(pos)
        pos += (pas + saut) / 900.0
    for p in trace:
        if p > av:
            break
        q = min(av, p + pas / 900.0)
        g.line([bezier(p, A, C, B), bezier(q, A, C, B)], fill=AMBRE + (235,), width=5)

    # --- l'avion, oriente sur la tangente
    if 0.0 < av < 1.0:
        ici = bezier(av, A, C, B)
        avant = bezier(max(0.0, av - 0.02), A, C, B)
        ang = math.atan2(ici[1] - avant[1], ici[0] - avant[0])
        c, s = math.cos(ang), math.sin(ang)
        forme = [(26, 0), (-14, 15), (-6, 0), (-14, -15)]
        g.polygon([(ici[0] + x * c - y * s, ici[1] + x * s + y * c) for x, y in forme],
                  fill=PAPIER)

    # --- les deux points, et leurs noms
    f_ville = police(46)
    f_code = police(30)
    f_km = police(28, gras=False)

    for (pt, ville, code, actif, aligne) in (
            (A, "MONTRÉAL", "YUL", entree, "gauche"),
            (B, "BERLIN", "BER", lisser(max(0.0, min(1.0, (t - 0.70) / 0.18))), "dessus")):
        r = 9
        couleur = tuple(int(SEPIA[k] + (PAPIER[k] - SEPIA[k]) * actif) for k in range(3))
        g.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=couleur + (255,))
        if actif > 0.02:
            a = int(255 * actif)
            if aligne == "dessus":
                # ⚠️ AU-DESSUS ET CENTRE. A gauche du point, l'etiquette
                # passait par-dessus le dernier pointille : l'arc traversait
                # le « N » de BERLIN.
                g.text((pt[0], pt[1] - 112), ville, font=f_ville,
                       fill=couleur + (a,), anchor="ma")
                g.text((pt[0], pt[1] - 56), code, font=f_code,
                       fill=AMBRE + (a,), anchor="ma")
            else:
                g.text((pt[0] + 24, pt[1] - 44), ville, font=f_ville,
                       fill=couleur + (a,), anchor="la")
                g.text((pt[0] + 24, pt[1] + 4), code, font=f_code,
                       fill=AMBRE + (a,), anchor="la")

    # --- la distance, calculee
    dk = lisser(max(0.0, min(1.0, (t - 0.76) / 0.16)))
    if dk > 0.02:
        g.text((L / 2, 1420), "%s km" % ("{:,}".format(int(round(d_km))).replace(",", "\u202f")),
               font=police(34), fill=AMBRE + (int(255 * dk),), anchor="ma")
        g.text((L / 2, 1472), "vol direct", font=f_km,
               fill=SEPIA + (int(255 * dk),), anchor="ma")
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", default="plan00-carte.mp4")
    ap.add_argument("--duree", type=float, default=3.0)
    ap.add_argument("--ffmpeg", required=True)
    a = ap.parse_args()

    n = int(round(a.duree * IPS))
    d = km(YUL, BER)
    tmp = os.path.join(os.path.dirname(os.path.abspath(a.sortie)), "_carte-images")
    os.makedirs(tmp, exist_ok=True)
    for i in range(n):
        dessiner(i, n, d).save(os.path.join(tmp, "f%04d.png" % i))
    # ⚠️ UNE PISTE MUETTE, PAS L'ABSENCE DE PISTE. Le montage concatene en
    # copie : un clip sans audio face a des clips qui en ont fait echouer le
    # raccord, ou pire, le fait passer en desynchronisant tout ce qui suit.
    subprocess.run([a.ffmpeg, "-y", "-v", "error", "-framerate", str(IPS),
                    "-i", os.path.join(tmp, "f%04d.png"),
                    "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
                    "-shortest",
                    "-c:v", "libx264", "-crf", "17", "-preset", "medium",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
                    a.sortie], check=True)
    for f in os.listdir(tmp):
        os.remove(os.path.join(tmp, f))
    os.rmdir(tmp)
    print("  %s   %d images, %.1f s, %.0f km" % (a.sortie, n, a.duree, d))


if __name__ == "__main__":
    main()
