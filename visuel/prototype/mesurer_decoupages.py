# -*- coding: utf-8 -*-
"""La mesure des decoupages : ce qui cloche dans les contours, scene par scene.

    python visuel/prototype/mesurer_decoupages.py              # toutes les scenes
    python visuel/prototype/mesurer_decoupages.py museum hotel # celles-ci
    python visuel/prototype/mesurer_decoupages.py --json sortie.json

POURQUOI (Jacques, 2 nov. 2026)
    « tous les decoupages, pas seulement des vetements, tous les objets ». Le
    chandail sous le veston debordait sous le veston ; agrandis a x4, les petits
    objets montraient les facettes de leur polygone ; la veste du musee avait
    deux polygones et des boucles. On ne corrige pas 1 700 zones a l'oeil : on
    mesure d'abord, on regarde les pires.

CE QU'IL MESURE (ne lit que les masques-<scene>.js et les points.json)
    chevauchement  deux zones SOEURS dont les masques se recouvrent : ni l'une
                   contenue dans l'autre (Anna contient son pull), ni posee sur
                   l'autre (« sur »), ni un fond plein (mur, sol). Le recouvrement
                   est dessine deux fois : le pull sous la veste.
    vetements      un vetement de dessous qui recouvre un vetement de dessus
                   (couches ci-dessous), meme quand l'un contient l'autre.
    facettes       la longueur moyenne d'un cote, rapportee a la taille de
                   l'objet, et les sommets d'un contour courbe dont l'angle se
                   voit (entre 12 et 70 degres, cotes de 8 px et plus). Un
                   trace en arcs (« q ») est mesure sur sa courbe, echantillonnee.
    morceaux       plus d'un polygone, dont des miettes (< 8 % du plus grand).
    boucles        un polygone qui se coupe lui-meme.
    debord         la part du trace qui sort du masque (hors zones rigides et
                   enveloppes, ou c'est voulu).
    hors_boite     la part du masque hors des boites de la zone (elargies d'un
                   quart) : SAM a pris un autre objet, ou un voisin avec (la
                   cravate du musee emportait la moustache). A regarder a l'oeil.
                   Au-dela de HORS_BOITE, la zone est listee : le 7 nov., il a
                   trouve trois zones tombees sur autre chose (le coquillage de
                   la plage sur les pieds et les lunettes, les pommes de terre
                   sur la soupe et la salade, les lampes de l'aeroport sur le
                   plafond) ; les cles de l'hotel, sur tout le casier, n'avaient
                   que 15 % hors de leurs boites, sous le seuil.
                   Il ne voit PAS une zone dont les boites elles-memes sont sur
                   le mauvais objet : SAM rend alors son masque dans la boite
                   (essai du 6 nov. : 17 zones fausses, toutes a plus de 80 %
                   dans leur boite). Celles-la, seule la planche les montre.
    doigt          trop petite pour un doigt : sur un iPhone de 375 px, sans
                   zoom, le cadre de la zone fait moins de 44 px de cote dans
                   les deux sens, meme avec la marge que l'app ajoute aux
                   petits objets (7 pixels du masque de chaque cote, sous
                   0,4 % de l'image). Jacques, 6 nov. : « des objets mal
                   decoupes » -- dont ceux qu'on ne touche qu'en zoomant.
"""
import io
import json
import math
import os
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))

import detourer as D

# Les couches des vetements : celles de detourer.py (etape 2).
COUCHES = D.VETEMENTS
# Au-dela, une zone est listee « hors de ses boites ». Mesure du 7 nov. sur les
# masques d'avant la correction : le coquillage de la plage 82 %, les lampes de
# l'aeroport 46 %, les pommes de terre 41 % ; les pierres du camping, justes mais
# plus grandes que leurs boites, 26 % (fausse alerte acceptee) ; les cles de
# l'hotel, fausses, 15 % seulement : elles passent dessous.
HORS_BOITE = 0.20


def lire_masques(nom):
    t = io.open(os.path.join(ICI, "masques-%s.js" % nom), encoding="utf-8").read()
    return json.loads(t[t.index("{"):t.rindex("}") + 1])


def derle(plages, w, h):
    bits = np.zeros(w * h, bool)
    i, v = 0, False
    for n in plages:
        if v:
            bits[i:i + n] = True
        i += n
        v = not v
    return bits.reshape(h, w)


def aire(p):
    x, y = p[:, 0], p[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


def se_coupe(p):
    """Nombre de paires de cotes non voisins qui se croisent."""
    n = len(p)
    if n < 4:
        return 0
    a, b = p, np.roll(p, -1, axis=0)
    def orient(p1, p2, p3):
        return np.sign((p2[..., 0] - p1[..., 0]) * (p3[..., 1] - p1[..., 1])
                       - (p2[..., 1] - p1[..., 1]) * (p3[..., 0] - p1[..., 0]))
    A, B = a[:, None, :], b[:, None, :]
    C, D = a[None, :, :], b[None, :, :]
    o1, o2 = orient(A, B, C), orient(A, B, D)
    o3, o4 = orient(C, D, A), orient(C, D, B)
    x = (o1 * o2 < 0) & (o3 * o4 < 0)
    i, j = np.triu_indices(n, 2)
    garde = ~((i == 0) & (j == n - 1))
    return int(x[i[garde], j[garde]].sum())


def facettes(p):
    """(longueur moyenne d'un cote, sommets d'angle visible sur une courbe)."""
    v = np.roll(p, -1, axis=0) - p
    lg = np.hypot(v[:, 0], v[:, 1])
    u = np.roll(v, 1, axis=0)
    lu = np.roll(lg, 1)
    cos = (u * v).sum(1) / np.maximum(lu * lg, 1e-9)
    ang = np.degrees(np.arccos(np.clip(cos, -1, 1)))
    vus = (ang > 12) & (ang < 70) & (lg >= 8) & (lu >= 8)
    return float(lg.mean()), int(vus.sum())


def remplir(polys, w, h, red):
    """Le trace rempli (pair-impair : un trou reste vide), a la taille du
    masque a toucher."""
    import cv2
    m = np.zeros((h, w), np.uint8)
    for p in polys:
        pts = (D.points_du_trace(p, np) / red * 16).round().astype(np.int32)
        couche = np.zeros_like(m)
        cv2.fillPoly(couche, [pts], 1, lineType=cv2.LINE_8, shift=4)
        m ^= couche
    return m.astype(bool)


def mesurer(nom):
    import cv2
    S = json.load(io.open(os.path.join(ICI, nom + ".points.json"), encoding="utf-8"))
    M = lire_masques(nom)
    w, h, W = M["w"], M["h"], M["W"]
    red = W / w
    P = {z["id"]: z for z in S["points"]}
    mas = {i: derle(r, w, h) for i, r in M["zones"].items() if i in P}
    zones, paires = [], []
    for i, m in mas.items():
        z = P[i]
        polys = [D.points_du_trace(p, np) for p in M["traces"].get(i, [])]
        aires = [aire(p) for p in polys]
        grand = max(aires) if aires else 0
        d_eq = math.sqrt(4 * sum(aires) / math.pi) if aires else 0
        lm, vus, boucles = 0.0, 0, 0
        for p in polys:
            a, b = facettes(p)
            lm = max(lm, a)
            vus += b
            boucles += se_coupe(p)
        trace = remplir(M["traces"].get(i, []), w, h, red)
        large = cv2.dilate(m.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)
        debord = (trace & ~large).sum() / max(trace.sum(), 1)
        manque = (m & ~cv2.dilate(trace.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)).sum() / max(m.sum(), 1)
        bx = np.zeros_like(m)
        for b in D.boites_de(z) + ([z["sam"]] if z.get("sam") and not isinstance(z["sam"][0], (list, tuple))
                                   else list(z.get("sam") or [])):
            mx, my = b[2] * 0.25 + 1, b[3] * 0.25 + 1
            x0, y0 = int(max(0, (b[0] - mx) / 100 * w)), int(max(0, (b[1] - my) / 100 * h))
            x1, y1 = int(min(w, (b[0] + b[2] + mx) / 100 * w + 1)), int(min(h, (b[1] + b[3] + my) / 100 * h + 1))
            bx[y0:y1, x0:x1] = True
        hors = float((m & ~bx).sum() / max(m.sum(), 1))
        ys, xs = np.nonzero(m)
        marge = 14 if m.sum() < w * h * 0.004 else 0          # sous() : 7 px de chaque cote
        ecran = [round(float((xs.max() - xs.min() + 1 + marge) * 375 / w)),
                 round(float((ys.max() - ys.min() + 1 + marge) * 375 / w))]
        zones.append({"hors_boite": round(hors, 3), "ecran": ecran,
                      "doigt": bool(ecran[0] < 44 and ecran[1] < 44),
            "scene": nom, "id": i, "mot": z["mot"], "pixels": int(m.sum()),
            "polys": len(polys), "miettes": sum(1 for a in aires if a < 0.08 * grand),
            "boucles": boucles, "cote_moyen": round(lm, 1),
            "finesse": round(lm / d_eq, 3) if d_eq else 0,
            "angles_vus": vus, "sommets": int(sum(len(p) for p in polys)),
            "debord": round(float(debord), 3), "manque": round(float(manque), 3),
            "volontaire": bool(z.get("rigide") or z.get("enveloppe") or z.get("plein")
                               or z.get("ellipses")),
        })
    ids = list(mas)
    def parents(i):
        out, z, k = set(), P[i], 0
        while z.get("sur") and k < 5:
            out.add(z["sur"])
            z = P.get(z["sur"], {})
            k += 1
        return out
    for a in range(len(ids)):
        for b in range(a + 1, len(ids)):
            A, B = ids[a], ids[b]
            inter = int((mas[A] & mas[B]).sum())
            if inter < 20:
                continue
            na, nb = int(mas[A].sum()), int(mas[B].sum())
            petit = min(na, nb)
            part = inter / petit
            ca, cb = COUCHES.get(P[A]["mot"]), COUCHES.get(P[B]["mot"])
            vet = ca is not None and cb is not None and ca != cb
            if not vet:
                if part > 0.85 or part < 0.03:
                    continue          # contenu dans l'autre, ou a peine touche
                if A in parents(B) or B in parents(A):
                    continue          # pose dessus
                if P[A].get("plein") or P[B].get("plein"):
                    continue          # un fond plein : tout est devant lui
            paires.append({"scene": nom, "a": A, "b": B, "mot_a": P[A]["mot"], "mot_b": P[B]["mot"],
                           "recouvre": inter, "part": round(part, 3), "vetements": vet})
    return zones, paires


def scenes():
    return sorted(f[:-len(".points.json")] for f in os.listdir(ICI)
                  if f.endswith(".points.json") and os.path.exists(os.path.join(ICI, "masques-" + f[:-len(".points.json")] + ".js")))


def main():
    args = sys.argv[1:]
    sortie = None
    if "--json" in args:
        k = args.index("--json")
        sortie = args[k + 1]
        del args[k:k + 2]
    noms = args or scenes()
    Z, PA = [], []
    for n in noms:
        z, p = mesurer(n)
        Z += z
        PA += p
    vet = [p for p in PA if p["vetements"]]
    autres = [p for p in PA if not p["vetements"]]
    grossiers = [z for z in Z if not z["volontaire"] and (z["finesse"] > 0.12 or z["angles_vus"] >= 6)]
    morceaux = [z for z in Z if z["miettes"]]
    boucles = [z for z in Z if z["boucles"]]
    debords = [z for z in Z if not z["volontaire"] and z["debord"] > 0.04]
    hors = [z for z in Z if not z["volontaire"] and z["hors_boite"] > HORS_BOITE]
    doigts = [z for z in Z if z["doigt"]]
    bilan = {
        "scenes": len(noms), "zones": len(Z),
        "chevauchements_vetements": len(vet), "chevauchements_autres": len(autres),
        "zones_grossieres": len(grossiers), "zones_a_miettes": len(morceaux),
        "zones_a_boucles": len(boucles), "zones_qui_debordent": len(debords),
        "zones_hors_de_leurs_boites": len(hors),
        "trop_petites_pour_un_doigt": len(doigts),
        "sommets": sum(z["sommets"] for z in Z),
        "angles_vus": sum(z["angles_vus"] for z in Z if not z["volontaire"]),
        "finesse_mediane": round(float(np.median([z["finesse"] for z in Z if not z["volontaire"] and z["finesse"]])), 3),
    }
    print("BILAN", json.dumps(bilan, ensure_ascii=False))
    print("\nVETEMENTS SUPERPOSES (recouvrement en px du petit masque)")
    for p in sorted(vet, key=lambda p: -p["recouvre"])[:40]:
        print("  %-18s %-12s %-12s %5d px  %4.0f %%" % (p["scene"], p["a"], p["b"], p["recouvre"], 100 * p["part"]))
    print("\nAUTRES CHEVAUCHEMENTS")
    for p in sorted(autres, key=lambda p: -p["recouvre"])[:40]:
        print("  %-18s %-14s %-14s %5d px  %4.0f %%" % (p["scene"], p["a"], p["b"], p["recouvre"], 100 * p["part"]))
    print("\nLES PLUS GROSSIERS (finesse = cote moyen / diametre)")
    for z in sorted(grossiers, key=lambda z: -(z["finesse"] + z["angles_vus"] / 100))[:40]:
        print("  %-18s %-14s finesse %.2f  angles vus %2d  sommets %3d  %6d px" % (
            z["scene"], z["id"], z["finesse"], z["angles_vus"], z["sommets"], z["pixels"]))
    print("\nMIETTES ET BOUCLES")
    for z in sorted(set(id(z) for z in morceaux + boucles) and morceaux + [b for b in boucles if b not in morceaux],
                    key=lambda z: -(z["miettes"] + z["boucles"]))[:40]:
        print("  %-18s %-14s polys %d miettes %d boucles %d" % (z["scene"], z["id"], z["polys"], z["miettes"], z["boucles"]))
    print("\nDEBORDS (part du trace hors du masque)")
    for z in sorted(debords, key=lambda z: -z["debord"])[:25]:
        print("  %-18s %-14s %4.0f %%" % (z["scene"], z["id"], 100 * z["debord"]))
    print("\nHORS DE LEURS BOITES (part du masque hors des boites elargies d'un quart)")
    for z in sorted(hors, key=lambda z: -z["hors_boite"])[:25]:
        print("  %-18s %-14s %4.0f %%  %6d px" % (z["scene"], z["id"], 100 * z["hors_boite"], z["pixels"]))
    print("\nTROP PETITES POUR UN DOIGT (cadre a l'ecran de 375 px, en px)")
    for z in sorted(doigts, key=lambda z: z["ecran"][0] * z["ecran"][1])[:25]:
        print("  %-18s %-14s %3d x %3d px" % (z["scene"], z["id"], z["ecran"][0], z["ecran"][1]))
    if sortie:
        json.dump({"bilan": bilan, "zones": Z, "paires": PA}, io.open(sortie, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
