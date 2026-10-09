# -*- coding: utf-8 -*-
"""Le contour exact de chaque objet de la scene, par SAM 2. Gratuit, local.

    python visuel/prototype/detourer.py                    # la classe
    python visuel/prototype/detourer.py arztpraxis --voir  # une autre scene, + controle

LES PARTIES DU CORPS NE PASSENT PAS PAR SAM
    SAM detoure un OBJET : demande-lui un genou, il rend la jambe, ou le
    pantalon. Une zone qui porte « ellipses » ([cx, cy, rx, ry] en % de
    l'image, une ou plusieurs) est dessinee telle quelle : le genou, l'epaule,
    le ventre de Mark chez le medecin (6 oct. 2026).

POURQUOI
    Jacques, 6 oct. 2026 : « comme sur Apple, l'objet au complet selectionne,
    meme avec les pattes de la table ». Les rectangles de
    klassenzimmer.points.json attrapaient le mur autour de l'horloge et
    manquaient les pattes de la table. On touche maintenant les PIXELS de
    l'objet, et le surlignage suit son contour.

COMMENT
    Les rectangles ne servent plus a toucher : ils servent a DIRE a SAM 2 ou
    chercher (un rectangle par zone, celui qui englobe toutes ses boites). SAM
    rend un masque par zone. On le reduit a 1/3 de la resolution et on l'ecrit
    en longueurs de plages (RLE), ce qui tient en quelques dizaines de Ko.

    Le modele (sam2.1_b.pt, ~80 Mo, Meta, Apache 2.0) vit dans
    ~/.wortando/modeles : hors du depot, hors de OneDrive.

CE QU'IL NE FAIT PAS
    Decider qui est devant qui. Les masques se recouvrent (le manteau passe
    derriere l'epaule de Mark) ; c'est le PLAN (champ devant, herite par sur)
    qui tranche dans l'app, comme avec les rectangles.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
MODELES = os.path.join(os.path.expanduser("~"), ".wortando", "modeles")
REDUCTION = 3            # le masque A TOUCHER garde 1 pixel sur 3 : 360 x 645
NETTOYAGE = 7            # px : trous bouches et poussieres retirees en dessous
MIETTE = 400             # px2 : un morceau de masque plus petit n'est pas trace
SIMPLIFICATION = 2.5     # px : ecart toléré entre le trace et le bord de SAM
# Un objet RIGIDE (champ rigide : la table, la porte...) : on bouche plus large
# (les mains et les cahiers posés sur le bord y creusaient des encoches) et on
# simplifie bien plus fort, pour que ses bords soient de vraies droites.
NETTOYAGE_RIGIDE = 25
SIMPLIFICATION_RIGIDE = 7


def boites_de(z):
    """Les rectangles d'une zone ; une zone en ellipses a les leurs."""
    if z.get("boites") or z.get("boite"):
        return z.get("boites") or [z["boite"]]
    return [[cx - rx, cy - ry, 2 * rx, 2 * ry] for cx, cy, rx, ry in z["ellipses"]]


def englobe(boites):
    x = min(b[0] for b in boites)
    y = min(b[1] for b in boites)
    return [x, y, max(b[0] + b[2] for b in boites) - x,
            max(b[1] + b[3] for b in boites) - y]


def geometrie(m8, mode, cv2, np):
    """La FORME d'un objet rigide, reconstruite au lieu d'etre suivie.

    Suivre le bord de SAM ne donne jamais une droite sur une table : SAM ne
    compte pas comme table ce qui est POSE dessus (cahiers, stylo, mains), et
    le contour du plateau contournait chaque cahier (Jacques, 6 oct. : « il y a
    encore des ondulations, surtout dans le devant de la table »).

    mode "table" : le plateau (ce qui est large) devient son enveloppe convexe
                   -- elle englobe les cahiers -- et chaque patte (ce qui est
                   mince) son rectangle ; on reunit le tout.
    autre        : l'enveloppe convexe de l'objet (porte, fenetre, tableau,
                   bureau, portable...) : des cotes droits.
    Le TOUCHER garde le vrai masque ; ceci ne sert qu'au dessin."""
    toile = np.zeros_like(m8)
    if mode == "table":
        # Le plateau : ce qui survit a une ouverture par un trait horizontal
        # plus large qu'une patte.
        plateau = cv2.morphologyEx(m8, cv2.MORPH_OPEN,
                                   cv2.getStructuringElement(cv2.MORPH_RECT, (61, 1)))
        n, lab, stats, _ = cv2.connectedComponentsWithStats(plateau)
        if n > 1:
            grand = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
            pts = cv2.findNonZero((lab == grand).astype(np.uint8))
            cv2.fillPoly(toile, [cv2.convexHull(pts)], 255)
        # Les pattes : ce qui reste sous le plateau, chacune en rectangle.
        reste = cv2.bitwise_and(m8, cv2.bitwise_not(cv2.dilate(toile, np.ones((9, 9), np.uint8))))
        n, lab, stats, _ = cv2.connectedComponentsWithStats(reste)
        for i in range(1, n):
            if stats[i, cv2.CC_STAT_AREA] < 400:
                continue
            pts = cv2.findNonZero((lab == i).astype(np.uint8))
            boite = cv2.boxPoints(cv2.minAreaRect(pts)).astype(np.int32)
            cv2.fillPoly(toile, [boite], 255)
        # recoudre la patte au plateau (la bande retiree par la dilatation)
        toile = cv2.morphologyEx(toile, cv2.MORPH_CLOSE, np.ones((15, 3), np.uint8))
        return toile
    contours, _ = cv2.findContours(m8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    gros = [c for c in contours if cv2.contourArea(c) >= 400]
    if not gros:
        return toile
    pts = np.vstack(gros)
    if mode == "rectangle":
        # mode "rectangle" : une porte, une fenetre, un tableau caches en partie
        # (la porte derriere la tete de Mark). L'enveloppe convexe coupait le
        # coin cache en diagonale ; le rectangle rend la porte entiere.
        cv2.fillPoly(toile, [cv2.boxPoints(cv2.minAreaRect(pts)).astype(np.int32)], 255)
    else:
        cv2.fillPoly(toile, [cv2.convexHull(pts)], 255)
    return toile


def retirer_fond(m8, pixels, fond, cv2, np):
    """Rendre au MUR ce que SAM a pris autour d'un personnage (champ fond).

    Jacques, 9 oct. 2026, sur l'examen : « autour de sa tete, comme une petite
    ligne, ce n'est pas beau ». Le projecteur eclaire le masque de Mark et
    assombrit le reste ; or SAM avait garde des bouts de mur vert entre les
    boucles, pres de l'oreille et du cou -- des taches claires collees a la
    tete. Sur un mur UNI, la couleur suffit a les reconnaitre : la couleur du
    fond est la mediane d'un anneau autour du masque, et l'on retire du masque
    tout pixel plus proche d'elle que `fond` (distance RVB ; true = 30)."""
    tol = 30 if fond is True else float(fond)
    anneau = cv2.dilate(m8, np.ones((31, 31), np.uint8)) & ~m8
    couleur = np.median(pixels[anneau > 127], axis=0)
    proche = np.sqrt(((pixels - couleur) ** 2).sum(axis=2)) < tol
    m8 = m8.copy()
    m8[proche] = 0
    m8 = cv2.morphologyEx(m8, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, lab, stats, _ = cv2.connectedComponentsWithStats(m8)
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] < MIETTE:
            m8[lab == i] = 0
    return m8


def rle(bits):
    """Longueurs alternees, en commencant par une plage de 0."""
    plages, courant, n = [], 0, 0
    for b in bits:
        if b == courant:
            n += 1
        else:
            plages.append(n)
            courant, n = b, 1
    plages.append(n)
    return plages


def main():
    import numpy as np
    from PIL import Image
    from ultralytics import SAM

    noms = [a for a in sys.argv[1:] if not a.startswith("--")]
    nom = noms[0] if noms else "klassenzimmer"
    scene = json.load(io.open(os.path.join(ICI, nom + ".points.json"),
                              encoding="utf-8"))
    image = os.path.join(ICI, scene["image"])
    W, H = Image.open(image).size

    os.makedirs(MODELES, exist_ok=True)
    avant = os.getcwd()
    os.chdir(MODELES)              # ultralytics telecharge dans le dossier courant
    try:
        modele = SAM("sam2.1_b.pt")
    finally:
        os.chdir(avant)

    zones = scene["points"]
    boites = []
    for z in zones:
        x, y, w, h = z.get("sam") or englobe(boites_de(z))
        boites.append([W * x / 100, H * y / 100, W * (x + w) / 100, H * (y + h) / 100])
    print("  %d zones, image %dx%d, SAM 2 sur processeur..." % (len(zones), W, H))
    # UNE ZONE PAR APPEL. Toutes les boites d'un coup, SAM a rendu 38 masques
    # pour 39 zones (6 oct., apres l'ajout des cahiers) -- sans dire lequel il
    # avait laisse tomber, donc sans qu'on sache a quelle zone va quel masque.
    import cv2
    masques = []
    for z, b in zip(zones, boites):
        if z.get("ellipses"):
            m = np.zeros((H, W), np.uint8)
            for cx, cy, rx, ry in z["ellipses"]:
                cv2.ellipse(m, (round(W * cx / 100), round(H * cy / 100)),
                            (round(W * rx / 100), round(H * ry / 100)),
                            0, 0, 360, 1, -1)
            masques.append(m.astype(bool))
            continue
        res = modele(image, bboxes=[b], verbose=False)[0]
        if res.masks is None or len(res.masks.data) == 0:
            # Une boite tres mince (un cahier vu par la tranche) peut ne rien
            # rendre : on reessaie en l'agrandissant de 8 px de chaque cote.
            b2 = [max(0, b[0] - 8), max(0, b[1] - 8), min(W, b[2] + 8), min(H, b[3] + 8)]
            res = modele(image, bboxes=[b2], verbose=False)[0]
        if res.masks is None or len(res.masks.data) == 0:
            sys.exit("  SAM ne rend aucun masque pour %s, meme agrandie" % z["id"])
        masques.append(res.masks.data[0].cpu().numpy().astype(bool))
    masques = np.stack(masques)                              # (N, H, W)

    pixels = np.array(Image.open(image).convert("RGB")).astype(np.int16)
    w, h = W // REDUCTION, H // REDUCTION
    sortie, traces = {}, {}
    noyau = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (NETTOYAGE, NETTOYAGE))
    noyau_rigide = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                             (NETTOYAGE_RIGIDE, NETTOYAGE_RIGIDE))
    for k, (z, m) in enumerate(zip(zones, masques)):
        # Nettoyer a pleine resolution : fermer les petits trous, retirer les
        # poussieres (le flanc du bureau en etait crible).
        n = noyau_rigide if z.get("rigide") else noyau
        m8 = cv2.morphologyEx(m.astype(np.uint8) * 255, cv2.MORPH_CLOSE, n)
        m8 = cv2.morphologyEx(m8, cv2.MORPH_OPEN, noyau)
        if z.get("fond"):
            m8 = retirer_fond(m8, pixels, z["fond"], cv2, np)
        masques[k] = m8 > 127
        m = masques[k]
        # Le TRACE : un polygone simplifie (Douglas-Peucker). Un bord presque
        # droit devient une ligne droite -- le dessus et les pattes de la table --
        # au lieu de l'escalier d'un masque reduit puis etire (Jacques, 6 oct.).
        forme = geometrie(m8, z.get("rigide"), cv2, np) if z.get("rigide") else m8
        contours, _ = cv2.findContours(forme, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        polys = []
        for c in contours:
            if cv2.contourArea(c) < MIETTE:
                continue
            eps = SIMPLIFICATION_RIGIDE if z.get("rigide") else SIMPLIFICATION
            a = cv2.approxPolyDP(c, eps, True).reshape(-1, 2)
            polys.append([int(v) for v in a.ravel()])
        traces[z["id"]] = polys
        petit = np.array(Image.fromarray(m8).resize((w, h), Image.BILINEAR)) > 127
        couverture = petit.mean() * 100
        boite = z.get("sam") or englobe(boites_de(z))
        part = couverture / (boite[2] * boite[3] / 100) * 100 if boite[2] * boite[3] else 0
        print("  %-13s %5.2f %% de l'image, %3.0f %% de sa boite" % (z["id"], couverture, part))
        sortie[z["id"]] = rle(petit.ravel().tolist())

    js = ("// GENERE par detourer.py (SAM 2) -- ne pas modifier a la main.\n"
          "window.MASQUES = " + json.dumps({"w": w, "h": h, "zones": sortie,
                                            "W": W, "H": H, "traces": traces},
                                           separators=(",", ":")) + ";\n")
    chemin = os.path.join(ICI, "masques-%s.js" % nom)
    io.open(chemin, "w", encoding="utf-8").write(js)
    print("  -> masques-%s.js (%d Ko)" % (nom, os.path.getsize(chemin) // 1024))

    if "--voir" in sys.argv:
        rng = np.random.default_rng(3)
        fond = np.array(Image.open(image).convert("RGB").resize((w, h))).astype(float)
        for z, m in zip(zones, masques):
            petit = np.array(Image.fromarray(m.astype(np.uint8) * 255).resize((w, h))) > 127
            fond[petit] = fond[petit] * 0.45 + rng.integers(60, 255, 3) * 0.55
        controle = os.path.join(os.environ.get("TMP", ICI), "masques-%s.png" % nom)
        Image.fromarray(fond.astype(np.uint8)).save(controle)
        print("  controle : %s" % controle)


if __name__ == "__main__":
    main()
