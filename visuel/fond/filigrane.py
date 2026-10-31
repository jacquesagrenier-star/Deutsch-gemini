# Fabrique carte-filigrane.svg, la carte du filigrane de la carte de seance (v1047), a partir de
# carte-langues-jour.svg : memes pays, memes regions, mais
#   - les quatre gris des regions deviennent quatre jaunes dores (les tons de la proposition 4 du 31 oct. 2026,
#     mesures sur le filtre sepia de l'essai, un peu ecartes pour que les regions se distinguent) ;
#   - les frontieres, deux traits blancs de .3 et .7, sont epaissies pour se lire comme dans la proposition 3
#     (Jacques : « les tons du 4 [...] le decoupage des pays [...] comme le 3 »), puis
#     un peu adoucies (« des frontieres legerement moins prononcees »).
# Fichier DERIVE : corriger ce script, pas le SVG. Lancer : python visuel/fond/filigrane.py
import os, re
ICI = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(ICI, "carte-langues-jour.svg"), encoding="utf-8").read()
TONS = {"#ADBECB": "#FFEE78", "#B6C5D1": "#FFF39A", "#C3D0DA": "#FFF8B8", "#CCD7E0": "#FFFCD4"}
for gris, dore in TONS.items():
    s = s.replace(f'fill="{gris}"', f'fill="{dore}" fill-opacity=".42"')
s = s.replace('stroke="#FFFFFF" stroke-width=".3" opacity=".6"', 'stroke="#FFFFFF" stroke-width=".8" opacity=".55"')
s = s.replace('stroke="#FFFFFF" stroke-width=".7"', 'stroke="#FFFFFF" stroke-width="1.1" opacity=".65"')
reste = set(re.findall(r'fill="(#[0-9A-F]{6})"', s)) - set(TONS.values()) - {"#FFFFFF"}
assert not reste, reste
assert s.count('stroke-width=".8"') == 1 and s.count('stroke-width="1.1"') == 1
open(os.path.join(ICI, "carte-filigrane.svg"), "w", encoding="utf-8", newline="\n").write(s)
print("carte-filigrane.svg :", len(s), "octets")
