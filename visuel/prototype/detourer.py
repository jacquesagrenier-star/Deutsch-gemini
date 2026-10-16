# -*- coding: utf-8 -*-
"""Le contour exact de chaque objet de la scene, par SAM 2. Gratuit, local.

    python visuel/prototype/detourer.py                    # la classe
    python visuel/prototype/detourer.py arztpraxis --voir  # une autre scene, + controle
    python visuel/prototype/detourer.py hotel --zones anzug,mantel   # ces zones seules

QUAND LA BOITE NE SUFFIT PAS : DES POINTS (16 oct. 2026)
    Une boite qui touche plusieurs objets rend n'importe lequel : la boite du
    costume de l'hotel prenait le mur a gauche et lachait le bras ; celle du
    manteau de Mark debordait sur son pantalon. Une zone peut porter
    « points_sam » : des points en % de l'image, chacun suivi de 1 (SUR
    l'objet) ou 0 (a EXCLURE) :
        "points_sam": [[8, 48, 1], [20, 52, 1], [3, 40, 0]]
    Les points servent d'abord a CHOISIR, ensuite a guider. SAM propose trois
    masques pour la boite seule et trois pour la boite avec les points ; on
    retire de chacun les morceaux detaches qui portent un point 0 (le combine
    du telephone sous le costume) ; on garde celui qui contredit le moins de
    points, puis le mieux note par SAM. Pourquoi pas les points seuls :
    passes en prompt, ils DEFORMENT le masque (treize points sur la vieille
    dame ont rendu des lambeaux de canape), alors que la boite seule proposait
    deja un masque propre -- il suffisait de savoir lequel des trois.
    Deux ou trois points sur l'objet la ou il est le plus large, un point sur
    chaque voisin que SAM confond avec lui, et peu : un point 1 pose A COTE de
    l'objet (sur le canape, pour les jambes) elimine la bonne proposition.
    Regarder le resultat, deplacer, recommencer. Les points ne remplacent pas
    la boite (« sam » ou l'englobante des boites) : elle dit toujours OU
    chercher, et une boite plus courte vaut souvent mieux qu'un point 0.

--zones id1,id2
    Ne recalcule QUE ces zones ; les autres sont reprises telles quelles du
    masques-<scene>.js existant (un passage complet sur processeur prend de
    longues minutes, un reglage de points se refait dix fois).

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


def propositions(sam, image, prompts):
    """Les trois masques que SAM propose pour un prompt, avec leurs notes."""
    sam.set_prompts(dict(prompts))
    res = sam(image, multimask_output=True, verbose=False)[0]
    if res.masks is None or len(res.masks.data) == 0:
        return []
    return list(zip(res.masks.data.cpu().numpy().astype(bool),
                    res.boxes.conf.cpu().numpy().tolist()))


def elaguer(m8, pos, neg, cv2):
    """Retire les morceaux detaches qui portent un point 0 et aucun point 1."""
    n, lab = cv2.connectedComponents(m8)
    for i in range(1, n):
        if any(lab[y, x] == i for x, y in neg) and not any(lab[y, x] == i for x, y in pos):
            m8[lab == i] = 0
    return m8


def choisir(sam, image, b, points, W, H, noyau, cv2, np):
    """Le masque d'une zone a points : la proposition qui contredit le moins
    de points, puis la mieux notee (voir la docstring du module)."""
    pix = [(min(W - 1, round(W * x / 100)), min(H - 1, round(H * y / 100)), int(l))
           for x, y, l in points]
    pos = [(x, y) for x, y, l in pix if l]
    neg = [(x, y) for x, y, l in pix if not l]
    cands = propositions(sam, image, {"bboxes": [b]})
    cands += propositions(sam, image, {"bboxes": [b],
                                       "points": [[[float(x), float(y)] for x, y, _ in pix]],
                                       "labels": [[l for _, _, l in pix]]})
    notes = []
    for m, score in cands:
        m8 = cv2.morphologyEx(m.astype(np.uint8) * 255, cv2.MORPH_CLOSE, noyau)
        m8 = cv2.morphologyEx(m8, cv2.MORPH_OPEN, noyau)
        m8 = elaguer(m8, pos, neg, cv2)
        large = cv2.dilate(m8, np.ones((9, 9), np.uint8))
        manques = sum(1 for x, y in pos if not large[y, x])
        intrus = sum(1 for x, y in neg if m8[y, x])
        notes.append((manques + intrus, -score, m8))
    if not notes:
        return None, None
    notes.sort(key=lambda t: t[:2])
    contredits, score, m8 = notes[0]
    return m8 > 127, "%d propositions, gardee : note %.3f, %d point(s) contredit(s)" % (
        len(notes), -score, contredits)


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


def derle(plages, w, h):
    """L'inverse de rle() : le petit masque (h, w) d'une zone deja ecrite."""
    import numpy as np
    bits = np.zeros(w * h, bool)
    i, courant = 0, False
    for n in plages:
        if courant:
            bits[i:i + n] = True
        i += n
        courant = not courant
    return bits.reshape(h, w)


def lire_existant(chemin, W, H):
    """Le masques-<scene>.js en place, pour --zones ; refuse une autre image."""
    if not os.path.exists(chemin):
        sys.exit("  --zones demande un %s existant : lancer d'abord sans --zones"
                 % os.path.basename(chemin))
    js = io.open(chemin, encoding="utf-8").read()
    data = json.loads(js[js.index("{"):js.rindex("}") + 1])
    if (data.get("W"), data.get("H")) != (W, H):
        sys.exit("  %s a ete fait sur une image %sx%s, celle-ci fait %dx%d : "
                 "tout refaire, sans --zones" % (os.path.basename(chemin),
                                                 data.get("W"), data.get("H"), W, H))
    return data


def main():
    import numpy as np
    from PIL import Image
    from ultralytics import SAM

    args = sys.argv[1:]
    noms, seulement = [], None
    for i, a in enumerate(args):
        if a == "--zones":
            if i + 1 >= len(args) or args[i + 1].startswith("--"):
                sys.exit("  --zones attend une liste : --zones anzug,mantel")
            seulement = set(args[i + 1].split(","))
        elif not a.startswith("--") and (i == 0 or args[i - 1] != "--zones"):
            noms.append(a)
    nom = noms[0] if noms else "klassenzimmer"
    scene = json.load(io.open(os.path.join(ICI, nom + ".points.json"),
                              encoding="utf-8"))
    image = os.path.join(ICI, scene["image"])
    W, H = Image.open(image).size
    chemin = os.path.join(ICI, "masques-%s.js" % nom)
    zones = scene["points"]
    existant = None
    if seulement is not None:
        inconnues = seulement - {z["id"] for z in zones}
        if inconnues:
            sys.exit("  --zones : pas de zone %s dans %s.points.json"
                     % (", ".join(sorted(inconnues)), nom))
        existant = lire_existant(chemin, W, H)

    os.makedirs(MODELES, exist_ok=True)
    avant = os.getcwd()
    os.chdir(MODELES)              # ultralytics telecharge dans le dossier courant
    try:
        modele = SAM("sam2.1_b.pt")
    finally:
        os.chdir(avant)

    import cv2
    pixels = np.array(Image.open(image).convert("RGB")).astype(np.int16)
    w, h = W // REDUCTION, H // REDUCTION
    sortie, traces, petits = {}, {}, []
    noyau = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (NETTOYAGE, NETTOYAGE))
    noyau_rigide = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                             (NETTOYAGE_RIGIDE, NETTOYAGE_RIGIDE))
    a_faire = len(zones) if seulement is None else len(seulement)
    print("  %d zones, image %dx%d, SAM 2 sur processeur..." % (a_faire, W, H))
    # L'image est ENCODEE UNE FOIS (set_image) : c'est l'encodeur qui coute
    # (une vingtaine de secondes par appel sur processeur), le decodeur qui
    # suit un prompt ne coute presque rien. Les appels modele(image, ...)
    # ci-dessous retrouvent ces memes traits et rendent la meme chose.
    modele(image, bboxes=[[0, 0, W, H]], verbose=False)   # cree le predicteur
    sam = modele.predictor
    sam.set_image(image)
    # UNE ZONE PAR APPEL. Toutes les boites d'un coup, SAM a rendu 38 masques
    # pour 39 zones (6 oct., apres l'ajout des cahiers) -- sans dire lequel il
    # avait laisse tomber, donc sans qu'on sache a quelle zone va quel masque.
    for z in zones:
        if seulement is not None and z["id"] not in seulement:
            # Reprise telle quelle : la zone n'a pas change, on ne la recalcule
            # pas. (Une zone ajoutee depuis le dernier passage n'a rien a
            # reprendre : elle est calculee.)
            if z["id"] in existant["zones"]:
                sortie[z["id"]] = existant["zones"][z["id"]]
                traces[z["id"]] = existant["traces"].get(z["id"], [])
                petits.append(derle(sortie[z["id"]], w, h))
                continue
        x, y, bw, bh = z.get("sam") or englobe(boites_de(z))
        b = [W * x / 100, H * y / 100, W * (x + bw) / 100, H * (y + bh) / 100]
        if z.get("plein"):
            # UNE CAGETTE DU MARCHE (9 oct. 2026) : la zone EST le rectangle.
            # SAM rendait le tas de fruits ou le bois, jamais les deux ; une
            # cagette vue de face est deja un rectangle, on le prend tel quel.
            m = np.zeros((H, W), np.uint8)
            for x, y, bw, bh in boites_de(z):
                cv2.rectangle(m, (round(W * x / 100), round(H * y / 100)),
                              (round(W * (x + bw) / 100), round(H * (y + bh) / 100)), 1, -1)
            m = m.astype(bool)
        elif z.get("ellipses"):
            m = np.zeros((H, W), np.uint8)
            for cx, cy, rx, ry in z["ellipses"]:
                cv2.ellipse(m, (round(W * cx / 100), round(H * cy / 100)),
                            (round(W * rx / 100), round(H * ry / 100)),
                            0, 0, 360, 1, -1)
            m = m.astype(bool)
        elif z.get("points_sam"):
            # Les points (points_sam) voyagent avec la boite : SAM 2 les
            # recoit en pixels, (1, n, 2) et leurs etiquettes (1, n) -- une
            # seule zone, donc un seul lot. Ultralytics colle la boite devant
            # (deux coins etiquetes 2 et 3) et le tout fait UN prompt. Puis
            # on CHOISIT parmi les propositions (docstring du module).
            m, bilan = choisir(sam, image, b, z["points_sam"], W, H, noyau, cv2, np)
            if m is None:
                sys.exit("  SAM ne propose aucun masque pour %s" % z["id"])
            print("  %-13s %s" % (z["id"], bilan))
        else:
            res = modele(image, bboxes=[b], verbose=False)[0]
            if res.masks is None or len(res.masks.data) == 0:
                # Une boite tres mince (un cahier vu par la tranche) peut ne rien
                # rendre : on reessaie en l'agrandissant de 8 px de chaque cote.
                b2 = [max(0, b[0] - 8), max(0, b[1] - 8), min(W, b[2] + 8), min(H, b[3] + 8)]
                res = modele(image, bboxes=[b2], verbose=False)[0]
            if res.masks is None or len(res.masks.data) == 0:
                sys.exit("  SAM ne rend aucun masque pour %s, meme agrandie" % z["id"])
            m = res.masks.data[0].cpu().numpy().astype(bool)

        # Nettoyer a pleine resolution : fermer les petits trous, retirer les
        # poussieres (le flanc du bureau en etait crible).
        n = noyau_rigide if z.get("rigide") else noyau
        m8 = cv2.morphologyEx(m.astype(np.uint8) * 255, cv2.MORPH_CLOSE, n)
        m8 = cv2.morphologyEx(m8, cv2.MORPH_OPEN, noyau)
        if z.get("fond"):
            m8 = retirer_fond(m8, pixels, z["fond"], cv2, np)
        if z.get("enveloppe"):
            # LES VELOS DU CARREFOUR (11 oct. 2026) : des tubes fins et des
            # rayons. Le masque de SAM suit les tubes, et un doigt pose entre
            # deux rayons tombait sur le trottoir. La zone devient l'enveloppe
            # convexe du masque -- pour toucher ET pour le dessin.
            pts = cv2.findNonZero(m8)
            if pts is not None:
                m8 = np.zeros_like(m8)
                cv2.fillPoly(m8, [cv2.convexHull(pts)], 255)
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
        petits.append(petit)
        couverture = petit.mean() * 100
        boite = z.get("sam") or englobe(boites_de(z))
        part = couverture / (boite[2] * boite[3] / 100) * 100 if boite[2] * boite[3] else 0
        print("  %-13s %5.2f %% de l'image, %3.0f %% de sa boite" % (z["id"], couverture, part))
        sortie[z["id"]] = rle(petit.ravel().tolist())

    js = ("// GENERE par detourer.py (SAM 2) -- ne pas modifier a la main.\n"
          "window.MASQUES = " + json.dumps({"w": w, "h": h, "zones": sortie,
                                            "W": W, "H": H, "traces": traces},
                                           separators=(",", ":")) + ";\n")
    io.open(chemin, "w", encoding="utf-8").write(js)
    print("  -> masques-%s.js (%d Ko)" % (nom, os.path.getsize(chemin) // 1024))

    if "--voir" in sys.argv:
        rng = np.random.default_rng(3)
        fond = np.array(Image.open(image).convert("RGB").resize((w, h))).astype(float)
        for petit in petits:
            fond[petit] = fond[petit] * 0.45 + rng.integers(60, 255, 3) * 0.55
        controle = os.path.join(os.environ.get("TMP", ICI), "masques-%s.png" % nom)
        Image.fromarray(fond.astype(np.uint8)).save(controle)
        print("  controle : %s" % controle)


if __name__ == "__main__":
    main()
