# -*- coding: utf-8 -*-
"""Les images web de la famille d'Anna, a cote de la page des exercices (visuel/prototype/familia/) :
    <Nom>.webp          la personne detouree (fond transparent), 900 px de haut, pour les rangees a l'echelle
    <Nom>-visage.webp   le visage, carre, pour les ronds de l'arbre
    familia.json        l'arbre (copie de visuel/familia/familia.json)
    planche.jpg         (dans img/, hors depot) toute la famille cote a cote, pour la verifier d'un coup d'oeil

    python visuel/familia/web.py

Le visage se trouve SUR LA SILHOUETTE DETOUREE, pas par un rectangle fixe comme dans Descripcion : la tete d'un
enfant de quatre ans occupe une part de l'image bien plus grande que celle de son grand-pere. On prend le haut
de la silhouette, une hauteur de tete proportionnee a l'age, et on centre sur la masse de la tete.
Fichiers DERIVES des originaux (visuel/familia/img/, hors du depot) : les refaire, pas les corriger.
"""
import os, shutil, sys
from PIL import Image
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)
from familia import FAMILLE, ecrire_json   # noqa: E402
SORTIE = os.path.join(RACINE, "visuel", "prototype", "familia")


def tete(nom):
    """La part de la hauteur du corps qu'occupe la tete (du sommet du crane au menton), selon l'age."""
    age = FAMILLE[nom][4]
    return 0.23 if age < 5 else 0.19 if age < 10 else 0.135


def visage(d, nom):
    """Un carre autour de la tete, pris sur la silhouette detouree (canal alpha)."""
    a = d.getchannel("A")
    x0, y0, x1, y1 = a.getbbox()
    h = y1 - y0
    ht = int(h * tete(nom))
    bande = a.crop((x0, y0, x1, y0 + ht)).point(lambda v: 255 if v > 128 else 0)
    bx0, _, bx1, _ = bande.getbbox()
    cx = x0 + (bx0 + bx1) // 2
    cote = int(ht * 1.25)
    cy = y0 + int(ht * 0.52)
    return (cx - cote // 2, cy - cote // 2, cx + cote // 2, cy + cote // 2)


def main():
    ecrire_json()
    os.makedirs(SORTIE, exist_ok=True)
    planche = []
    for nom in FAMILLE:
        chemin = os.path.join(ICI, "img", nom + "-detoure.png")
        if not os.path.exists(chemin):
            print("  manque :", nom)
            continue
        d = Image.open(chemin).convert("RGBA")
        boite = visage(d, nom)
        orig = Image.open(os.path.join(ICI, "img", ("Anna-quotidien" if nom == "Anna" else nom) + ".png")).convert("RGB")
        v = orig.crop(boite)
        v = v.resize((360, 360), Image.LANCZOS)
        v.save(os.path.join(SORTIE, nom + "-visage.webp"), "WEBP", quality=84, method=6)
        c = d.crop(d.getbbox())
        c = c.resize((round(c.size[0] * 900 / c.size[1]), 900), Image.LANCZOS)
        c.save(os.path.join(SORTIE, nom + ".webp"), "WEBP", quality=82, method=6)
        planche.append((nom, c, v))
    shutil.copyfile(os.path.join(ICI, "familia.json"), os.path.join(SORTIE, "familia.json"))
    # la planche de controle : en pied a l'echelle de la taille, et les visages dessous
    if planche:
        maxm = max(FAMILLE[n][1] for n, _, _ in planche)
        H = 600
        corps = [c.resize((max(1, round(c.size[0] * H * FAMILLE[n][1] / maxm / c.size[1])), round(H * FAMILLE[n][1] / maxm))) for n, c, _ in planche]
        W = sum(c.size[0] for c in corps) + 10 * len(corps)
        W = max(W, 130 * len(planche))
        p = Image.new("RGB", (W, H + 150), (236, 236, 236))
        x = 0
        for c in corps:
            p.paste(c, (x, H - c.size[1]), c)
            x += c.size[0] + 10
        for i, (_, _, v) in enumerate(planche):
            p.paste(v.resize((120, 120)), (i * 130, H + 15))
        p.save(os.path.join(ICI, "img", "planche.jpg"), quality=85)
    total = sum(os.path.getsize(os.path.join(SORTIE, f)) for f in os.listdir(SORTIE))
    print("  %d fichiers, %.0f ko dans %s" % (len(os.listdir(SORTIE)), total / 1024, os.path.relpath(SORTIE, RACINE)))


if __name__ == "__main__":
    main()
