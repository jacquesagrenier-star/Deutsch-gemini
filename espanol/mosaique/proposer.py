"""Les 65 candidats les plus eclatants (Jacques, 14 oct. 2026 : « prends les
65 plus colores et montre-les-moi »), sur une planche a part : apercu-65.jpg.
Les numeros restent ceux des planches 1 a 7.
"""
import collections, json, os, sys
from PIL import Image, ImageDraw, ImageFont
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import recolter

N = 65
c = json.load(open(os.path.join(ICI, "candidats.json"), encoding="utf-8"))
top = sorted(c, key=lambda t: -t["eclat"])[:N]
top.sort(key=lambda t: t["num"])
json.dump([t["num"] for t in top], open(os.path.join(ICI, "apercu-65.json"), "w"), indent=0)

try:
    f = ImageFont.truetype("arialbd.ttf", 17)
    p = ImageFont.truetype("arial.ttf", 14)
except Exception:
    f = p = ImageFont.load_default()
CEL, COLS = 240, 7
rows = (len(top) + COLS - 1) // COLS
im = Image.new("RGB", (COLS * CEL, rows * (CEL + 24)), "white")
d = ImageDraw.Draw(im)
for i, t in enumerate(top):
    v = recolter.vif(Image.open(os.path.join(recolter.BRUT, "v-" + t["cle"] + ".jpg")).convert("RGB"))
    v.thumbnail((CEL - 12, CEL - 44))
    x, y = (i % COLS) * CEL, (i // COLS) * (CEL + 24)
    im.paste(v, (x + (CEL - v.width) // 2, y + 26))
    d.text((x + 6, y + 4), "%d" % t["num"], fill="black", font=f)
    d.text((x + 52, y + 6), t["peintre"][:24], fill=(90, 90, 90), font=p)
    d.text((x + 6, y + CEL - 14), t["pays"], fill=(150, 90, 20), font=p)
im.save(os.path.join(ICI, "apercu-65.jpg"), quality=82)

print("eclat du 65e :", sorted(t["eclat"] for t in top)[0])
print(collections.Counter(t["peintre"] for t in top).most_common())
print("Amerique latine :", sum(1 for t in top if t["pays"] != "Espagne"))
