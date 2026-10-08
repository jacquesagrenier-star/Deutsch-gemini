# teinte (r-b) : la peau est rouge, l'affiche grise -- python rgb.py axe fixe a b pas
import os, sys
from PIL import Image
im = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "visuel", "prototype", "arztpraxis-visage-mark.webp")).convert("RGB")
px = lambda v: (v - 43) / 13.6 * im.width
py = lambda v: (v - 28) / 13.6 * im.height
axe, fixe, a, b, pas = sys.argv[1], *map(float, sys.argv[2:])
out = []
v = a
while v <= b + 1e-9:
    r, g, bl = im.getpixel((int(px(v)), int(py(fixe))) if axe == "x" else (int(px(fixe)), int(py(v))))
    out.append("%.2f:%d/%d" % (v, r - bl, (r + g + bl) // 3))
    v = round(v + pas, 4)
for i in range(0, len(out), 6): print("  ".join(out[i:i+6]))
