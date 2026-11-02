# Fabrique les calques du PAYS DE LA LANGUE APPRISE, poses sur la carte du monde de l'accueil (v1066, idee de
# Marc-Antoine, 1er nov. 2026 ; choix de Jacques : teinte pleine ambre, turquoise a travers la carte de la seance).
#   visuel/fond/pays/<code>.svg       le pays en ambre, sur la carte du fond (#fondMonde .fm-pays)
#   visuel/fond/pays/<code>-fili.svg  le meme en turquoise, dans le filigrane de la seance (.spf-pays)
# Meme projection que carte-langues-jour.svg : equirectangulaire, viewBox 1200 x 473, 180 O a gauche, 84 N en haut
# (mesure : le 49e parallele entre le Canada et les Etats-Unis tombe a y = 116,6). Les deux pistes la montrent a
# 960 x 378 en repeat-x ; le calque prend le meme fond, il defile donc avec elle sans rien calculer.
# Source : world-atlas 2.0.2 (countries-50m, Natural Earth, domaine public), hors du depot :
#   C:/Users/jacqu/.wortando/carte-pays/countries-50m.json
# Fichiers DERIVES : corriger ce script, pas les SVG. Lancer : python visuel/fond/pays.py
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(os.path.expanduser("~"), ".wortando", "carte-pays", "countries-50m.json")
W, H, PX = 1200, 473, 1200 / 360
# les codes de drapeauLangueApprise() ; l'Amerique latine (mx) : les pays hispanophones des Ameriques
PAYS = {
    "de": ["276", "040"],                        # l'Autriche aussi (Jacques, 1er nov. 2026)
    "es": ["724"],
    "mx": ["484", "320", "340", "222", "558", "188", "591", "192", "214", "630", "170", "862", "218", "604", "068", "152", "032", "858", "600"],
    "pt": ["620"],
    "br": ["076"],
    "us": ["840"],
    "gb": ["826"],
    "ja": ["392"],
}
COULEURS = {"": ("#E8A23A", "#FFFFFF", ".7"), "-fili": ("#2BB5AA", "#FFFFFF", ".9")}

topo = json.load(open(SOURCE, encoding="utf-8"))
sx, sy = topo["transform"]["scale"]
tx, ty = topo["transform"]["translate"]
arcs = []
for arc in topo["arcs"]:
    x = y = 0
    pts = []
    for dx, dy in arc:
        x += dx; y += dy
        pts.append((x * sx + tx, y * sy + ty))
    arcs.append(pts)

def anneau(idx):
    pts = []
    for i in idx:
        a = arcs[i] if i >= 0 else arcs[~i][::-1]
        pts.extend(a if not pts else a[1:])
    return pts

def projeter(lon, lat):
    return (lon + 180) * PX, (84 - lat) * PX

par_id = {str(g.get("id")).zfill(3): g for g in topo["objects"]["countries"]["geometries"]}
os.makedirs(os.path.join(ICI, "pays"), exist_ok=True)
for code, ids in PAYS.items():
    d = []
    for pid in ids:
        g = par_id[pid]
        polys = g["arcs"] if g["type"] == "MultiPolygon" else [g["arcs"]]
        for poly in polys:
            for r in poly:
                xy = [projeter(lon, lat) for lon, lat in anneau(r)]
                xs = [p[0] for p in xy]
                if max(xs) - min(xs) > W / 2: continue      # un anneau a cheval sur l'antimeridien (Aleoutiennes)
                if all(p[1] > H for p in xy): continue       # sous le bas de la carte (84 N a 57,9 S)
                pts, prec = [], None
                for x, y in xy:
                    q = (round(x, 1), round(y, 1))
                    if q != prec: pts.append(q)
                    prec = q
                if len(pts) < 3: continue
                d.append("M" + "L".join(f"{x:g},{y:g}" for x, y in pts) + "Z")
    for suffixe, (fond, trait, epais) in COULEURS.items():
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"><path d="{"".join(d)}" fill="{fond}" '
               f'stroke="{trait}" stroke-width="{epais}" stroke-linejoin="round" fill-rule="evenodd"/></svg>\n')
        chemin = os.path.join(ICI, "pays", code + suffixe + ".svg")
        open(chemin, "w", encoding="utf-8", newline="\n").write(svg)
        print(f"pays/{code}{suffixe}.svg : {len(svg)} octets")
