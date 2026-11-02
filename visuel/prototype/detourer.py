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
    Redetoure ces zones meme si le cache les a ; les autres sont reprises du
    cache (~/.wortando/decoupages) quand leur description n'a pas change --
    un reglage de points se refait dix fois. Une zone dont la boite ou les
    points ont change est redetouree d'office : --zones ne sert plus qu'a
    forcer. --tout ignore le cache ; --retracer refuse de lancer SAM et ne
    refait que l'arbitrage, les miettes et les traces.

UN OBJET EN PLUSIEURS MORCEAUX : « sam » en LISTE de boites (16 oct. 2026)
    Le pull de Mark a la pharmacie n'est visible qu'en deux endroits, la
    capuche et une bande sur le ventre ; les deux paires de chaussures de la
    salle de musique sont a un metre l'une de l'autre ; l'impermeable d'Anna
    au supermarche est coupe en deux par son pull. La boite ENGLOBANTE de ces
    morceaux couvre surtout ce qu'il y a entre eux (la veste, le pied du
    lutrin, le pull), et SAM rend ca. Quand « sam » est une liste de boites
        "sam": [[59, 38.5, 5, 4.5], [51.5, 49.5, 3.5, 10.5]]
    la zone est detouree boite par boite et les masques sont reunis. Les
    « points_sam » restent permis : chaque boite ne recoit que les points qui
    tombent dedans. Les « boites » de la zone ne bougent pas : construire.py
    les recopie dans scene-<nom>.js (la place de l'etiquette), « sam » ne
    sert qu'ici.

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

LA REPRISE DU 2 NOV. 2026 : QUATRE ETAPES DE PLUS
    Jacques : « tous les decoupages, pas seulement des vetements, tous les
    objets » -- le chandail ne doit garder que sa partie VISIBLE, et les petits
    objets agrandis a x4 montraient les facettes de leur polygone. Mesure avant
    et apres : mesurer_decoupages.py ; rapport : RAPPORT-DECOUPAGES.md.

    1. AFFINER, sur demande : « affiner »: true sur une zone (ou --affiner
       pour toutes). Sur l'image entiere, SAM voit la scene reduite au tiers :
       son masque a une maille d'une dizaine de pixels, et sur un petit objet
       il prend ce qui l'entoure (le crayon avec la main, la cravate avec la
       moustache). On le relance sur une TUILE de 768 px recadree autour de
       l'objet, ou il voit 3,6 fois plus fin, et l'on prend sa proposition la
       mieux ajustee a la boite (qui reste dans l'ancien masque, n'en est pas
       une miette, ne contredit aucun point). Pourquoi pas pour toutes les
       zones : une tuile coute un encodage (une douzaine de secondes, bien
       plus quand le PC travaille a autre chose) et, sans un oeil, rien ne
       dit que la tuile a raison -- sur le musee, elle a rendu la cravate avec
       la moustache, le veston avec la tete, un tableau sans la moitie de son
       cadre. Avec --affiner, une proposition n'est prise que si elle recouvre
       l'ancien masque a AFFINE_MEME au moins (elle precise, elle ne change
       pas d'objet) ; « affiner »: true sur une zone, verifiee a l'oeil, leve
       ce garde-fou.
    2. ARBITRER qui est devant qui, entre vetements (couches ci-dessous) et la
       ou points.json le dit (« devant_de »: [ids] : cette zone CACHE celles-
       la). Un vetement contenu dans un autre est devant lui (l'echarpe sur la
       veste, le chemisier dans l'ouverture de la veste) : le grand le perd.
       Un recouvrement partiel se tranche a la COULEUR : chaque pixel va au
       vetement dont il a la couleur (le pull beige qui depasse du manteau
       vert). Couleurs trop proches : le vetement de dessus le garde. Tout
       autre recouvrement PARTIEL (Mark devant la chaise, le crayon dans la
       main) se tranche aussi a la couleur, et reste tel quel si elle ne
       tranche pas ; un objet contenu dans un autre (la chaine du velo) ou
       pose dessus (« sur ») n'est pas touche -- sauf entre deux objets poses
       sur le meme support (le stylo et la carte sur le bureau) : le petit
       est devant.
    3. MIETTES : un morceau detache, petit, et d'une autre couleur que le
       corps de l'objet (le bout de bougie dans le gilet du marchand) part.
    4. TRACER EN COURBES : le bord du masque, lisse le long du contour (les
       marches d'un pixel deviennent des droites), simplifie a 1,5 px au lieu
       de 2,5 (les ondulations de SAM disparaissent toujours), puis chaque
       facette d'une courbe devient un petit arc (adoucir) : plus de facettes
       a x4, et un bord droit reste droit, un coin reste un coin. Un premier
       essai a 0,45 px sans arcs suivait chaque ondulation de SAM (le
       radiateur du musee en devenait mou). Le trace s'ecrit alors en chemin
       SVG (« M L Q Z », au dixieme de pixel) : les arcs y tiennent en une
       commande, et le fichier reste leger. Le moteur (chemin()) le dessine
       tel quel.
       Un trou assez grand (le sac devant la veste) est trace aussi. Les zones
       rigides et pleines gardent leur trace (decide le 6 oct.).

    Le CACHE (~/.wortando/decoupages, hors du depot) garde le masque pleine
    resolution de chaque zone : une zone dont la description n'a pas change
    n'est pas redetouree, et --retracer refait les etapes 2 a 4 sans SAM.

CE QU'IL NE FAIT PAS
    Le PLAN du toucher (champ devant, herite par sur) reste celui de l'app :
    l'etape 2 ne retire que des pixels CACHES, elle ne decide pas qui gagne un
    doigt pose sur deux objets visibles.
"""
import hashlib
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
MODELES = os.path.join(os.path.expanduser("~"), ".wortando", "modeles")
CACHE = os.path.join(os.path.expanduser("~"), ".wortando", "decoupages")
REDUCTION = 3            # le masque A TOUCHER garde 1 pixel sur 3 : 360 x 645
NETTOYAGE = 7            # px : trous bouches et poussieres retirees en dessous
MIETTE = 400             # px2 : un morceau de masque plus petit n'est pas trace
SIMPLIFICATION = 2.5     # px : ecart toléré entre le trace et le bord de SAM
# Un objet RIGIDE (champ rigide : la table, la porte...) : on bouche plus large
# (les mains et les cahiers posés sur le bord y creusaient des encoches) et on
# simplifie bien plus fort, pour que ses bords soient de vraies droites.
NETTOYAGE_RIGIDE = 25
SIMPLIFICATION_RIGIDE = 7
# Les quatre etapes du 2 nov. (docstring)
TUILE = 768              # px : cote de la tuile ou SAM affine un petit objet
AFFINER = 440            # px : plus grand cote d'une boite qu'on affine
AFFINE_MEME = 0.88       # recouvrement minimal entre la tuile et l'image entiere
LISSAGE = 1.5            # points : ecart-type du lissage le long du contour
FINESSE = 1.5            # px : ecart tolere avant d'arrondir les facettes
COIN = 65                # degres : au-dela, un sommet est un vrai coin
ARC_MAX = 15             # px : un arc ne mord pas plus loin sur un cote
TROU = 0.04              # un trou plus petit que 4 % de la zone n'est pas trace
CHAINE = "2026-11-02.2"   # change = tout le cache redetoure
# Les couches des vetements, du plus pres du corps au plus loin : a couleurs
# egales, la couche haute garde le recouvrement.
VETEMENTS = {
    "Unterhose": 0, "Socke": 0, "靴下": 0,
    "T-Shirt": 1, "Hemd": 1, "Bluse": 1, "Kleid": 1, "Trikot": 1, "Hose": 1,
    "Jeans": 1, "Rock": 1,
    "Pullover": 2, "Schuh": 2, "Stiefel": 2, "Turnschuh": 2, "Sandale": 2,
    "靴": 2, "スリッパ": 2,
    "Jacke": 3, "Anzug": 3, "Schürze": 3,
    "Mantel": 4, "コート": 4,
    "Schal": 5, "Krawatte": 5, "Gürtel": 5,
    "Rucksack": 6, "Tasche": 6, "リュック": 6, "かばん": 6, "Handschuh": 6,
    "Kopfhörer": 6, "Brille": 6, "Mütze": 6, "Hut": 6, "Helm": 6, "帽子": 6,
}
# Les personnes (et leurs parties) qui portent des zones « sur » elles.
PERSONNES = {"Patient", "Ärztin", "Arzt", "Frau", "Mann", "Lehrer", "Lehrerin", "Teilnehmer",
             "Teilnehmerin", "Student", "Studentin", "Radfahrer", "Kind", "Junge", "Mädchen",
             "Baby", "Kellner", "Kellnerin", "Nachbar", "Bruder", "Mutter", "Vater", "Oma", "Opa",
             "Onkel", "Cousin", "Tochter", "Pilot", "Spieler", "Fahrgast", "Fußgänger", "Kopf",
             "Knie", "Hand", "Schneemann", "男", "女", "女の子", "駅員", "客", "店員", "おばあさん"}
# Les vetements qui ont de vraies parties fines (etape 3 : pas de « queue »).
MINCES = {"Krawatte", "Gürtel", "Brille", "Kopfhörer", "Schal", "Rucksack",
          "Tasche", "リュック", "かばん", "Handschuh", "Socke", "靴下", "Sandale", "スリッパ"}


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


def unites(z, W, H):
    """Ce que SAM detoure pour une zone : [(boite en px, points ou None)].
    Une zone en « sam » liste a une unite par boite (chacune avec les points
    qui tombent dedans), les autres une seule."""
    def px(x, y, bw, bh):
        return [W * x / 100, H * y / 100, W * (x + bw) / 100, H * (y + bh) / 100]
    sam_b = z.get("sam")
    if sam_b and isinstance(sam_b[0], (list, tuple)):
        return [(px(*bb), [p for p in z.get("points_sam") or []
                           if bb[0] <= p[0] <= bb[0] + bb[2] and bb[1] <= p[1] <= bb[1] + bb[3]] or None)
                for bb in sam_b]
    return [(px(*(sam_b or englobe(boites_de(z)))), z.get("points_sam") or None)]


def empreinte(z, image):
    """Ce qui decide du masque d'une zone : si rien n'a change, le cache vaut."""
    st = os.stat(image)
    utile = {k: z.get(k) for k in ("sam", "points_sam", "boite", "boites", "ellipses",
                                   "plein", "rigide", "fond", "enveloppe", "affiner")}
    return hashlib.sha1(json.dumps([CHAINE, st.st_size, int(st.st_mtime), utile],
                                   sort_keys=True).encode()).hexdigest()[:16]


def lire_cache(nom, np):
    f = os.path.join(CACHE, nom + ".npz")
    if not os.path.exists(f):
        return {}, {}
    d = np.load(f)
    meta = json.loads(str(d["__meta__"]))
    forme = tuple(meta.pop("__forme__"))
    def deplier(k):
        return np.unpackbits(d[k])[:forme[0] * forme[1]].reshape(forme).astype(bool)
    return ({i: (meta[i], deplier(i), deplier(i + "__entier")) for i in meta if i in d.files}, meta)


def ecrire_cache(nom, masques, np):
    os.makedirs(CACHE, exist_ok=True)
    meta, tab = {}, {}
    for i, (emp, m, entier) in masques.items():
        meta[i] = emp
        tab[i] = np.packbits(m.ravel())
        tab[i + "__entier"] = np.packbits(entier.ravel())
        meta["__forme__"] = list(m.shape)
    np.savez_compressed(os.path.join(CACHE, nom + ".npz"), __meta__=json.dumps(meta), **tab)


def tuiles(boites, W, H):
    """Range les boites a affiner dans le moins de tuiles possible : une tuile
    coute un encodage (une douzaine de secondes), un prompt presque rien."""
    T = min(TUILE, W, H)
    def marge(b):
        m = 0.15 * max(b[2] - b[0], b[3] - b[1]) + 16
        return [b[0] - m, b[1] - m, b[2] + m, b[3] + m]
    def dedans(b, t):
        return t[0] <= b[0] and t[1] <= b[1] and b[2] <= t[0] + T and b[3] <= t[1] + T
    faites, rang = [], {}
    for k in sorted(range(len(boites)), key=lambda k: (boites[k][1], boites[k][0])):
        b = marge(boites[k])
        for n, t in enumerate(faites):
            if dedans(b, t):
                rang[k] = n
                break
        else:
            # La tuile laisse un tiers de sa marge libre a gauche et en haut :
            # assez de contexte autour de l'objet pour SAM, et de la place a
            # droite et dessous pour les boites suivantes. Jamais hors de l'image.
            x0 = int(min(max(0, b[0] - (T - (b[2] - b[0])) / 3), W - T))
            y0 = int(min(max(0, b[1] - (T - (b[3] - b[1])) / 3), H - T))
            faites.append((x0, y0))
            rang[k] = len(faites) - 1
    return T, faites, rang


def candidats(sam, image, b, points, W, H, noyau, cv2, np):
    """Toutes les propositions de SAM pour une boite (et ses points), nettoyees,
    avec le nombre de points qu'elles contredisent et leur note."""
    pix = [(min(W - 1, round(W * x / 100)), min(H - 1, round(H * y / 100)), int(l))
           for x, y, l in points or []]
    pos = [(x, y) for x, y, l in pix if l]
    neg = [(x, y) for x, y, l in pix if not l]
    cands = propositions(sam, image, {"bboxes": [b]})
    if pix:
        cands += propositions(sam, image, {"bboxes": [b],
                                           "points": [[[float(x), float(y)] for x, y, _ in pix]],
                                           "labels": [[l for _, _, l in pix]]})
    out = []
    for m, score in cands:
        m8 = cv2.morphologyEx(m.astype(np.uint8) * 255, cv2.MORPH_CLOSE, noyau)
        m8 = cv2.morphologyEx(m8, cv2.MORPH_OPEN, noyau)
        if pix:
            m8 = elaguer(m8, pos, neg, cv2)
        large = cv2.dilate(m8, np.ones((9, 9), np.uint8))
        contredits = sum(1 for x, y in pos if not large[y, x]) + sum(1 for x, y in neg if m8[y, x])
        out.append((m8 > 127, score, contredits))
    return out


def ajustement(m, b, np):
    """Combien un masque tient dans la boite de l'objet : la part de ses pixels
    dedans (boite elargie de 10 % et 6 px), plus la moitie de la part de la
    boite que son cadre couvre. La cravate qui emporte le visage deborde de sa
    boite ; un bouton de la veste n'en couvre qu'un coin."""
    ys, xs = np.nonzero(m)
    if not len(xs):
        return 0.0
    bw, bh = b[2] - b[0], b[3] - b[1]
    mx, my = 0.1 * bw + 6, 0.1 * bh + 6
    dans = ((xs >= b[0] - mx) & (xs <= b[2] + mx) & (ys >= b[1] - my) & (ys <= b[3] + my)).mean()
    couvre = (min(1, (xs.max() - xs.min() + 1) / max(bw, 1)) + min(1, (ys.max() - ys.min() + 1) / max(bh, 1))) / 2
    return float(dans + 0.5 * couvre)


def affiner(entier, cands, points, b, force, cv2, np):
    """La proposition de la tuile qui PRECISE le masque de l'image entiere
    (docstring, etape 1), ou None. Elle doit recouvrir l'ancien masque a
    AFFINE_MEME au moins, ne contredire aucun point, et tenir dans la boite
    au moins aussi bien que lui ; entre plusieurs, la mieux ajustee a la boite
    puis la mieux notee. Rend aussi la raison, pour le journal.

    Le garde-fou qui compte est le recouvrement (essai du musee, 2 nov.) : la
    meilleure note et le meilleur ajustement a la boite n'ont empeche ni la
    cravate d'emporter la moustache, ni le veston la tete, ni un tableau de
    perdre la moitie de son cadre -- chaque fois sous 0,75 de recouvrement.
    Au-dela de AFFINE_MEME, la tuile ne fait que preciser le meme contour ;
    en dessous, un oeil doit trancher : « affiner »: true sur la zone (le
    recouvrement n'est plus exige, seulement de rester dans l'ancien masque
    et d'en garder au moins 15 %)."""
    n = int(entier.sum())
    if not n:
        return None, "masque vide"
    large = cv2.dilate(entier.astype(np.uint8), np.ones((25, 25), np.uint8)).astype(bool)
    avant = ajustement(entier, b, np)
    ok, meilleur_iou = [], 0.0
    for m, score, contredits in cands:
        k = int(m.sum())
        if not k or (points and contredits > 0):
            continue
        iou = (m & entier).sum() / max((m | entier).sum(), 1)
        meilleur_iou = max(meilleur_iou, iou)
        if force:
            if (m & large).sum() / k < 0.85 or k < 0.15 * n:
                continue
        elif iou < AFFINE_MEME:
            continue
        aj = ajustement(m, b, np)
        if aj < avant - 0.05:
            continue
        ok.append((aj + 0.5 * score, score, aj, iou, m))
    if not ok:
        return None, "aucune proposition ne precise l'ancienne (IoU max %.2f)" % meilleur_iou
    _, score, aj, iou, m = max(ok, key=lambda t: t[0])
    return m, "note %.2f, ajustement %.2f (avant %.2f), IoU %.2f" % (score, aj, avant, iou)


def par_couleur(A, B, inter, M, cle, cv2, np):
    """Le recouvrement de A et B tranche a la couleur : (pixels qui vont a A,
    ressemblance des deux couleurs), ou (None, ressemblance) quand elles sont
    trop proches pour trancher. Chaque pixel va a la zone dont l'histogramme
    (Lab, 12 cases par axe, pris sur ce que chacune a EN PROPRE) le rend le
    plus probable ; un filtre median efface le grain."""
    noyau = np.ones((11, 11), np.uint8)
    seul_a = cv2.erode((M[A] & ~M[B]).astype(np.uint8), noyau).astype(bool)
    seul_b = cv2.erode((M[B] & ~M[A]).astype(np.uint8), noyau).astype(bool)
    if seul_a.sum() < 300 or seul_b.sum() < 300:
        return None, 1.0
    ha = np.bincount(cle[seul_a], minlength=1728).astype(float) + 0.5
    hb = np.bincount(cle[seul_b], minlength=1728).astype(float) + 0.5
    ha /= ha.sum()
    hb /= hb.sum()
    bc = float(np.sqrt(ha * hb).sum())
    if bc >= 0.6:
        return None, bc
    ys, xs = np.nonzero(inter)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    dans = inter[y0:y1, x0:x1]
    k = cle[y0:y1, x0:x1]
    brut = np.where(ha[k] >= hb[k], 255, 0).astype(np.uint8)
    med = cv2.medianBlur(np.where(dans, brut, 128).astype(np.uint8), 9)   # 128 : neutre
    va = np.zeros_like(inter)
    va[y0:y1, x0:x1] = dans & ((med > 128) | ((med == 128) & (brut == 255)))
    return va, bc


def arbitrer(zones, M, lab, cv2, np, journal):
    """Etape 2 (docstring) : chaque pixel CACHE est retire de la zone de
    derriere. M : {id: masque pleine resolution}, modifie en place.

    Dans l'ordre : ce que points.json dit (« devant_de ») ; les vetements
    entre eux (contenu = devant ; partiel = couleur, sinon couche) ; puis tout
    autre recouvrement PARTIEL, a la couleur seulement (Mark devant la chaise,
    le crayon dans la main). Un objet CONTENU dans un autre sans etre un
    vetement, ni son voisin sur le meme support, n'est pas touche : c'est souvent une partie du tout (la chaine
    du velo, la roue) ; un objet pose (« sur ») non plus ; ni les fonds pleins
    et les parties du corps en ellipses."""
    P = {z["id"]: z for z in zones}
    def parents(i):
        out, z, k = set(), P[i], 0
        while z.get("sur") and k < 5:
            out.add(z["sur"])
            z = P.get(z["sur"], {})
            k += 1
        return out
    q = (lab // 22).astype(np.int32)           # 12 cases par axe
    cle = q[..., 0] * 144 + q[..., 1] * 12 + q[..., 2]
    faits = set()
    for z in zones:
        for j in z.get("devant_de") or []:
            if z["id"] in M and j in M:
                n = int((M[j] & M[z["id"]]).sum())
                M[j] &= ~M[z["id"]]
                faits.add(frozenset((z["id"], j)))
                journal.append(["devant_de", z["id"], j, n])
    ids = [i for i in M if not P[i].get("plein") and not P[i].get("ellipses") and not P[i].get("detail")]
    cadres = {}
    for i in ids:
        ys, xs = np.nonzero(M[i].any(axis=1))[0], np.nonzero(M[i].any(axis=0))[0]
        cadres[i] = (xs.min(), ys.min(), xs.max(), ys.max()) if len(xs) else (0, 0, -1, -1)
    def se_touchent(A, B):
        a, b = cadres[A], cadres[B]
        return a[0] <= b[2] and b[0] <= a[2] and a[1] <= b[3] and b[1] <= a[3]
    vet = [i for i in ids if P[i]["mot"] in VETEMENTS]
    paires = [(A, B) for k, A in enumerate(vet) for B in vet[k + 1:]]
    paires += [(A, B) for k, A in enumerate(ids) for B in ids[k + 1:]
               if not (A in vet and B in vet)]
    for A, B in paires:
        if frozenset((A, B)) in faits or A in parents(B) or B in parents(A) or not se_touchent(A, B):
            continue
        inter = M[A] & M[B]
        n = int(inter.sum())
        if n < 200:
            continue
        na, nb = int(M[A].sum()), int(M[B].sum())
        petit, grand = (A, B) if na <= nb else (B, A)
        vetements = A in vet and B in vet
        # Deux objets poses sur le meme support (le stylo et la carte sur le
        # bureau du cabinet medical) ne sont pas l'un une partie de l'autre :
        # si l'un contient l'autre, c'est que SAM a pris les deux, et le petit
        # est devant -- comme pour deux vetements.
        # Pas sur une PERSONNE : la jambe et le pantalon de Mark sont tous deux
        # « sur » lui, et l'une est bien dans l'autre.
        support = P.get(P[A].get("sur") or "", {})
        voisins = (bool(support) and P[A].get("sur") == P[B].get("sur")
                   and support.get("mot") not in PERSONNES and not support.get("personne"))
        if n >= 0.85 * min(na, nb):
            if vetements or voisins:
                M[grand] &= ~M[petit]
                journal.append(["contenu", petit, grand, n])
            continue
        if not vetements and n < 0.03 * min(na, nb):
            continue
        va, bc = par_couleur(A, B, inter, M, cle, cv2, np)
        if va is not None:
            M[B] &= ~va
            M[A] &= ~(inter & ~va)
            journal.append(["couleur (%.2f)" % bc, A, B, n, int(va.sum()), n - int(va.sum())])
        elif vetements:
            ca, cb = VETEMENTS[P[A]["mot"]], VETEMENTS[P[B]["mot"]]
            haut = A if ca > cb else B if cb > ca else petit
            bas = B if haut == A else A
            M[bas] &= ~M[haut]
            journal.append(["couche, couleurs proches (%.2f)" % bc, haut, bas, n])


def oter_miettes(m8, z, lab, cv2, np):
    """Etape 3 : un morceau detache, petit, d'une autre couleur que le corps ;
    et, sur un vetement, une QUEUE : une bande de moins de 13 px qui pend du
    vetement (la veste du gardien du musee descendait le long du pied de la
    chaise). Un vetement n'a pas de partie aussi fine -- sauf ceux de MINCES."""
    if z.get("plein") or z.get("ellipses") or (z.get("sam") and isinstance(z["sam"][0], (list, tuple))):
        return m8, 0
    otes = 0
    if z["mot"] in VETEMENTS and z["mot"] not in MINCES:
        ouvert = cv2.morphologyEx(m8, cv2.MORPH_OPEN,
                                  cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13)))
        reste = cv2.bitwise_and(m8, cv2.bitwise_not(ouvert))
        # Seules les bandes qui partent sont des queues ; le reste de ce que
        # l'ouverture a rogne (les coins) revient.
        nr, cr, sr, _ = cv2.connectedComponentsWithStats(reste, connectivity=8)
        for i in range(1, nr):
            lw, lh = sr[i, cv2.CC_STAT_WIDTH], sr[i, cv2.CC_STAT_HEIGHT]
            if sr[i, cv2.CC_STAT_AREA] >= 120 and max(lw, lh) >= 30 and max(lw, lh) >= 2.5 * min(lw, lh):
                m8[cr == i] = 0
                otes += 1
    n, cc, stats, _ = cv2.connectedComponentsWithStats(m8, connectivity=8)
    if n <= 2:
        return m8, 0
    aires = stats[1:, cv2.CC_STAT_AREA]
    grand = 1 + int(np.argmax(aires))
    corps = lab[cc == grand].mean(axis=0)
    for i in range(1, n):
        a = stats[i, cv2.CC_STAT_AREA]
        if i == grand or a >= 0.12 * aires.max():
            continue
        ecart = float(np.sqrt(((lab[cc == i].mean(axis=0) - corps) ** 2).sum()))
        if a < 0.015 * aires.max() or ecart > 20:
            m8[cc == i] = 0
            otes += 1
    return m8, otes


def lisser(pts, np):
    """Lissage gaussien d'un contour ferme, le long du contour."""
    if len(pts) < 12:
        return pts
    r = int(3 * LISSAGE)
    k = np.exp(-0.5 * (np.arange(-r, r + 1) / LISSAGE) ** 2)
    k /= k.sum()
    ext = np.concatenate([pts[-r:], pts, pts[:r]])
    return np.stack([np.convolve(ext[:, j], k, mode="valid") for j in range(2)], axis=1)


def adoucir(p, np, arc_max=ARC_MAX):
    """Le chemin SVG d'un polygone ferme dont les facettes deviennent des arcs ;
    les droites et les coins francs restent. Un sommet ou le contour tourne de
    4 a COIN degres est la facette d'une courbe : il devient un arc (Bezier
    quadratique, « Q », dont il est le point de controle) entre deux points
    pris sur ses cotes, a 45 % au plus de leur longueur (deux arcs voisins ne
    se touchent jamais) et a ARC_MAX px au plus (un bord droit reste droit
    jusqu'a son coin). Sous 4 degres, c'est une droite ; au-dela de COIN, un
    vrai coin (un col, l'angle d'une boite). L'app dessine le chemin tel quel."""
    n = len(p)
    if n < 3:
        return ""
    morceaux = []                      # ("L", point) ou ("Q", controle, point)
    for i in range(n):
        a, b, c = p[i - 1], p[i], p[(i + 1) % n]
        u, v = b - a, c - b
        lu, lv = float(np.hypot(*u)), float(np.hypot(*v))
        ang = 0.0
        if lu > 1e-6 and lv > 1e-6:
            ang = float(np.degrees(np.arccos(np.clip(np.dot(u, v) / (lu * lv), -1, 1))))
        if ang < 4 or ang > COIN or not arc_max:
            morceaux.append(("L", b))
            continue
        d = min(0.45 * min(lu, lv), arc_max)
        morceaux.append(("L", b - u / lu * d))
        morceaux.append(("Q", b, b + v / lv * d))
    # Le chemin part d'un point pose (un arc ne peut pas l'ouvrir), puis tout
    # s'ecrit en RELATIF (« l », « q ») au dixieme de pixel : des ecarts de
    # quelques pixels au lieu de coordonnees a quatre chiffres, le fichier
    # reste leger. Les ecarts sont pris entre points DEJA arrondis : aucune
    # derive le long du contour.
    k = next(i for i, m in enumerate(morceaux) if m[0] == "L")
    morceaux = morceaux[k:] + morceaux[:k]
    def r(q):
        return (int(round(float(q[0]) * 10)), int(round(float(q[1]) * 10)))
    def f(*vals):
        s = ""
        for x in vals:
            e = ("%.1f" % (x / 10)).rstrip("0").rstrip(".")
            e = e.replace("-0.", "-.") if e.startswith("-0.") else e[1:] if e.startswith("0.") else e
            s += e if (not s or e.startswith("-")) else " " + e
        return s
    cur = r(morceaux[0][1])
    d = "M%s" % f(*cur)
    for m in morceaux[1:]:
        if m[0] == "L":
            q = r(m[1])
            d += "l" + f(q[0] - cur[0], q[1] - cur[1])
            cur = q
        else:
            c, e = r(m[1]), r(m[2])
            d += "q" + f(c[0] - cur[0], c[1] - cur[1], e[0] - cur[0], e[1] - cur[1])
            cur = e
    return d + "z"


def se_recoupe(p, np):
    """Vrai si le polygone ferme p se coupe lui-meme (deux cotes non voisins
    qui se croisent)."""
    n = len(p)
    if n < 4:
        return False
    a, b = p, np.roll(p, -1, axis=0)
    def orient(p1, p2, p3):
        return np.sign((p2[..., 0] - p1[..., 0]) * (p3[..., 1] - p1[..., 1])
                       - (p2[..., 1] - p1[..., 1]) * (p3[..., 0] - p1[..., 0]))
    for k in range(0, n, 400):              # par paquets : n peut depasser 2000
        A, B = a[k:k + 400, None, :], b[k:k + 400, None, :]
        C, D = a[None, :, :], b[None, :, :]
        x = (orient(A, B, C) * orient(A, B, D) < 0) & (orient(C, D, A) * orient(C, D, B) < 0)
        i = np.arange(k, min(n, k + 400))[:, None]
        j = np.arange(n)[None, :]
        voisins = (abs(i - j) <= 1) | (abs(i - j) == n - 1)
        if (x & ~voisins).any():
            return True
    return False


def points_du_trace(t, np, pas=6):
    """Un trace (liste de sommets, ou chemin « M l q z » d'adoucir) en
    polygone dense, pour mesurer et dessiner hors de l'app."""
    if not isinstance(t, str):
        return np.array(t, float).reshape(-1, 2)
    import re
    out, cur = [], np.zeros(2)
    for cmd, nums in re.findall(r"([MLQZmlqz])([^MLQZmlqz]*)", t):
        v = [float(x) for x in re.findall(r"-?(?:\d+\.?\d*|\.\d+)", nums)]
        base = cur if cmd.islower() else np.zeros(2)
        if cmd in "MLml":
            cur = base + np.array(v[:2])
            out.append(cur)
        elif cmd in "Qq":
            c, e = base + np.array(v[:2]), base + np.array(v[2:4])
            for s in np.linspace(0, 1, pas + 1)[1:]:
                out.append((1 - s) ** 2 * cur + 2 * (1 - s) * s * c + s ** 2 * e)
            cur = e
    return np.array(out)


def tracer(m8, z, cv2, np):
    """Etape 4 : les polygones du contour (et des grands trous)."""
    if z.get("rigide") or z.get("plein"):
        forme = geometrie(m8, z.get("rigide"), cv2, np) if z.get("rigide") else m8
        contours, _ = cv2.findContours(forme, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        eps = SIMPLIFICATION_RIGIDE if z.get("rigide") else SIMPLIFICATION
        return [[int(v) for v in cv2.approxPolyDP(c, eps, True).ravel()]
                for c in contours if cv2.contourArea(c) >= MIETTE]
    contours, hier = cv2.findContours(m8, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    total = int((m8 > 0).sum())
    polys = []
    for k, c in enumerate(contours):
        a = cv2.contourArea(c)
        trou = hier[0][k][3] >= 0
        if a < (max(2000, TROU * total) if trou else MIETTE):
            continue
        lisse = lisser(c.reshape(-1, 2).astype(np.float64), np).astype(np.float32).reshape(-1, 1, 2)
        # Dans un passage etroit (entre deux doigts, sous un bras), deux arcs
        # voisins peuvent se croiser, ou la simplification elle-meme couper le
        # passage : le contour se recoupe et dessine une boucle. On arrondit
        # alors moins, puis plus du tout, puis on simplifie moins.
        for eps, arc in ((FINESSE, ARC_MAX), (FINESSE, ARC_MAX / 3), (FINESSE, 0), (0.5, 0)):
            p = cv2.approxPolyDP(lisse, eps, True).reshape(-1, 2).astype(np.float64)
            d = adoucir(p, np, arc)
            if not d or not se_recoupe(points_du_trace(d, np), np):
                break
        if d:
            polys.append(d)
    return polys


def detourer_entier(z, sam, modele, image, W, H, noyau, cv2, np, bilans):
    """Le masque de l'image entiere, unite par unite (le calcul d'avant le
    2 nov., inchange) : [masque par unite]."""
    us = unites(z, W, H)
    separe = len(us) > 1 or (z.get("sam") and isinstance(z["sam"][0], (list, tuple)))
    out = []
    for b, points in us:
        if points:
            pts = points if separe else z["points_sam"]
            mi, bilan = choisir(sam, image, b, pts, W, H, noyau, cv2, np)
            if mi is None:
                sys.exit("  SAM ne propose aucun masque pour %s" % z["id"])
            bilans.append("  %-13s %s" % (z["id"], bilan))
        else:
            res = modele(image, bboxes=[b], verbose=False)[0]
            if not separe and (res.masks is None or len(res.masks.data) == 0):
                # Une boite tres mince (un cahier vu par la tranche) peut ne rien
                # rendre : on reessaie en l'agrandissant de 8 px de chaque cote.
                b2 = [max(0, b[0] - 8), max(0, b[1] - 8), min(W, b[2] + 8), min(H, b[3] + 8)]
                res = modele(image, bboxes=[b2], verbose=False)[0]
            if res.masks is None or len(res.masks.data) == 0:
                sys.exit("  SAM ne rend aucun masque pour %s" % z["id"])
            mi = res.masks.data[0].cpu().numpy().astype(bool)
        out.append(mi)
    return out


def sam_a_faire_ids(zones):
    return [z["id"] for z in zones if not (z.get("plein") or z.get("ellipses"))]


def nettoyer(m, z, pixels, noyau, noyau_rigide, cv2, np):
    """Bouche, depoussiere, rend le fond, enveloppe : le masque d'une zone."""
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
    return m8 > 127


def dessine(z, W, H, cv2, np):
    """Une zone « plein » ou en ellipses : son masque est sa forme."""
    m = np.zeros((H, W), np.uint8)
    if z.get("plein"):
        # UNE CAGETTE DU MARCHE (9 oct. 2026) : la zone EST le rectangle.
        # SAM rendait le tas de fruits ou le bois, jamais les deux ; une
        # cagette vue de face est deja un rectangle, on le prend tel quel.
        for x, y, bw, bh in boites_de(z):
            cv2.rectangle(m, (round(W * x / 100), round(H * y / 100)),
                          (round(W * (x + bw) / 100), round(H * (y + bh) / 100)), 1, -1)
    else:
        for cx, cy, rx, ry in z["ellipses"]:
            cv2.ellipse(m, (round(W * cx / 100), round(H * cy / 100)),
                        (round(W * rx / 100), round(H * ry / 100)), 0, 0, 360, 1, -1)
    return m.astype(bool)


def main():
    import numpy as np
    from PIL import Image
    import cv2

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
    if seulement is not None:
        inconnues = seulement - {z["id"] for z in zones}
        if inconnues:
            sys.exit("  --zones : pas de zone %s dans %s.points.json"
                     % (", ".join(sorted(inconnues)), nom))
    # Ce que le cache sait deja (docstring) ; --tout l'ignore, --zones aussi
    # pour ces zones-la.
    cache, _ = ({}, {}) if "--tout" in args else lire_cache(nom, np)
    if cache and next(iter(cache.values()))[1].shape != (H, W):
        cache = {}
    masques, a_detourer = {}, []
    for z in zones:
        emp = empreinte(z, image)
        c = cache.get(z["id"])
        if c and c[0] == emp and (seulement is None or z["id"] not in seulement):
            masques[z["id"]] = c
        else:
            a_detourer.append(z)
    if "--retracer" in args and a_detourer:
        sys.exit("  --retracer : %d zone(s) sans masque a jour dans le cache (%s) -- lancer sans --retracer"
                 % (len(a_detourer), ", ".join(z["id"] for z in a_detourer[:8])))

    pixels = np.array(Image.open(image).convert("RGB")).astype(np.int16)
    noyau = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (NETTOYAGE, NETTOYAGE))
    noyau_rigide = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,
                                             (NETTOYAGE_RIGIDE, NETTOYAGE_RIGIDE))
    journal = {"affiner": [], "arbitrer": [], "miettes": []}
    ancien = os.path.join(CACHE, nom + ".journal.json")
    if not sam_a_faire_ids(a_detourer) and os.path.exists(ancien):
        # Rien a redetourer : le journal de l'affinage d'avant reste vrai.
        journal["affiner"] = json.load(io.open(ancien, encoding="utf-8")).get("affiner", [])
    sam_a_faire = [z for z in a_detourer if not (z.get("plein") or z.get("ellipses"))]
    print("  %d zones, %d a detourer (%d par SAM), image %dx%d"
          % (len(zones), len(a_detourer), len(sam_a_faire), W, H))
    for z in a_detourer:
        if z.get("plein") or z.get("ellipses"):
            m = dessine(z, W, H, cv2, np)
            m = nettoyer(m, z, pixels, noyau, noyau_rigide, cv2, np)
            masques[z["id"]] = (empreinte(z, image), m, m)
    if sam_a_faire:
        from ultralytics import SAM
        os.makedirs(MODELES, exist_ok=True)
        avant = os.getcwd()
        os.chdir(MODELES)              # ultralytics telecharge dans le dossier courant
        try:
            modele = SAM("sam2.1_b.pt")
        finally:
            os.chdir(avant)
        # L'image est ENCODEE UNE FOIS (set_image) : c'est l'encodeur qui coute
        # (une douzaine de secondes par appel sur processeur), le decodeur qui
        # suit un prompt ne coute presque rien. Les appels modele(image, ...)
        # ci-dessous retrouvent ces memes traits et rendent la meme chose.
        modele(image, bboxes=[[0, 0, W, H]], verbose=False)   # cree le predicteur
        sam = modele.predictor
        sam.set_image(image)
        # UNE ZONE PAR APPEL. Toutes les boites d'un coup, SAM a rendu 38 masques
        # pour 39 zones (6 oct., apres l'ajout des cahiers) -- sans dire lequel il
        # avait laisse tomber, donc sans qu'on sache a quelle zone va quel masque.
        entiers, bilans = {}, []
        for z in sam_a_faire:
            entiers[z["id"]] = detourer_entier(z, sam, modele, image, W, H, noyau, cv2, np, bilans)
        print("\n".join(bilans))
        # Etape 1 : affiner les petits objets, tuile par tuile.
        # Seulement sur demande (docstring, etape 1) : une zone « affiner »:
        # true, ou --affiner pour toutes (avec le garde-fou AFFINE_MEME).
        a_affiner = [(z, k, b, pts) for z in sam_a_faire
                     if (z.get("affiner") is True or ("--affiner" in args and z.get("affiner") is not False))
                     and not z.get("rigide") and not z.get("enveloppe")
                     for k, (b, pts) in enumerate(unites(z, W, H))
                     if max(b[2] - b[0], b[3] - b[1]) <= AFFINER]
        T, places, rang = tuiles([b for _, _, b, _ in a_affiner], W, H)
        bgr = np.ascontiguousarray(pixels[:, :, ::-1].astype(np.uint8))
        affines = {}
        print("  affiner : %d boite(s) en %d tuile(s) de %d px" % (len(a_affiner), len(places), T))
        for n, (x0, y0) in enumerate(places):
            tuile = np.ascontiguousarray(bgr[y0:y0 + T, x0:x0 + T])
            sam.set_image(tuile)
            for k, (z, u, b, pts) in enumerate(a_affiner):
                if rang[k] != n:
                    continue
                bb = [b[0] - x0, b[1] - y0, b[2] - x0, b[3] - y0]
                pts_t = [[(W * px / 100 - x0) / T * 100, (H * py / 100 - y0) / T * 100, l]
                         for px, py, l in pts or []]
                cands = candidats(sam, tuile, bb, pts_t, T, T, noyau, cv2, np)
                entier = entiers[z["id"]][u][y0:y0 + T, x0:x0 + T]
                hors = entiers[z["id"]][u].sum() - entier.sum()
                if hors > 0.05 * max(entier.sum(), 1):
                    # Le masque entier deborde de la tuile : on ne compare pas
                    # ce qu'on ne voit pas.
                    journal["affiner"].append([z["id"], u, "garde : deborde de la tuile"])
                    continue
                m, raison = affiner(entier, cands, pts, bb, z.get("affiner") is True, cv2, np)
                journal["affiner"].append([z["id"], u, ("PRIS : " if m is not None else "garde : ") + raison])
                if m is not None:
                    plein = np.zeros((H, W), bool)
                    plein[y0:y0 + T, x0:x0 + T] = m
                    affines[(z["id"], u)] = plein
        for z in sam_a_faire:
            ent = np.zeros((H, W), bool)
            fin = np.zeros((H, W), bool)
            for u, mi in enumerate(entiers[z["id"]]):
                ent |= mi
                fin |= affines.get((z["id"], u), mi)
            masques[z["id"]] = (empreinte(z, image),
                                nettoyer(fin, z, pixels, noyau, noyau_rigide, cv2, np),
                                nettoyer(ent, z, pixels, noyau, noyau_rigide, cv2, np))
    ecrire_cache(nom, {z["id"]: masques[z["id"]] for z in zones}, np)

    # Etapes 2 a 4, sur toutes les zones (docstring).
    lab = cv2.cvtColor(pixels.astype(np.uint8), cv2.COLOR_RGB2LAB)
    M = {z["id"]: masques[z["id"]][1].copy() for z in zones}
    arbitrer(zones, M, lab, cv2, np, journal["arbitrer"])
    w, h = W // REDUCTION, H // REDUCTION
    sortie, traces, petits = {}, {}, []
    for z in zones:
        m8 = M[z["id"]].astype(np.uint8) * 255
        m8, otes = oter_miettes(m8, z, lab, cv2, np)
        if otes:
            journal["miettes"].append([z["id"], otes])
        traces[z["id"]] = tracer(m8, z, cv2, np)
        petit = np.array(Image.fromarray(m8).resize((w, h), Image.BILINEAR)) > 127
        petits.append(petit)
        sortie[z["id"]] = rle(petit.ravel().tolist())
    for ligne in journal["arbitrer"]:
        print("  arbitre  %s" % " ".join(str(v) for v in ligne))
    pris = sum(1 for l in journal["affiner"] if l[2].startswith("PRIS"))
    print("  affines : %d sur %d ; miettes otees dans %d zone(s)"
          % (pris, len(journal["affiner"]), len(journal["miettes"])))
    os.makedirs(CACHE, exist_ok=True)
    json.dump(journal, io.open(os.path.join(CACHE, nom + ".journal.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    js = ("// GENERE par detourer.py (SAM 2) -- ne pas modifier a la main.\n"
          "window.MASQUES = " + json.dumps({"w": w, "h": h, "zones": sortie,
                                            "W": W, "H": H, "traces": traces},
                                           separators=(",", ":"), ensure_ascii=False) + ";\n")
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
