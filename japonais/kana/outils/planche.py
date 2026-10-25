# -*- coding: utf-8 -*-
"""Génère planche.html à partir de kana.json : tous les signes avec leur
romaji, leur nombre de traits et le SVG KanjiVG, pour une relecture à l'œil.

Usage : python japonais/kana/outils/planche.py
"""
import html
import json
import os

KANA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOY = ["a", "i", "u", "e", "o"]


def cellule(s):
    if s is None:
        return '<td class="vide"></td>'
    imgs = "".join('<img src="%s" alt="">' % c["svg"] for c in s["composants"])
    cls = " rare" if s["statut"] != "courant" else ""
    return ('<td class="c%s"><div class="k">%s</div><div class="r">%s</div>'
            '<div class="t">%d tr. · %s</div><div class="svg">%s</div></td>'
            % (cls, html.escape(s["signe"]), html.escape(s["romaji"]), s["traits"], s["groupe"], imgs))


def grille(signes, titre, rangees):
    lignes = ['<h2>%s</h2><table><tr><th></th>%s</tr>' % (titre, "".join("<th>%s</th>" % v for v in VOY))]
    for gyo in rangees:
        cases = {s["gojuon"]["voyelle"]: s for s in signes if s["gojuon"] and s["gojuon"]["gyo"] == gyo}
        lignes.append("<tr><th>%s</th>%s</tr>" % (gyo, "".join(cellule(cases.get(v)) for v in VOY)))
    return "".join(lignes) + "</table>"


def liste(signes, titre, par_ligne=6):
    out = ['<h2>%s</h2><table>' % titre]
    for i in range(0, len(signes), par_ligne):
        out.append("<tr>%s</tr>" % "".join(cellule(s) for s in signes[i:i + par_ligne]))
    return "".join(out) + "</table>"


def main():
    d = json.load(open(os.path.join(KANA, "kana.json"), encoding="utf-8"))
    S = d["signes"]
    parts = []
    for ecr in ("hiragana", "katakana"):
        de = [s for s in S if s["ecriture"] == ecr]
        base = [s for s in de if s["categorie"] == "base"]
        parts.append(grille([s for s in base if s["gojuon"]["voyelle"]],
                            "%s — 46 signes de base" % ecr.capitalize(),
                            ["あ行", "か行", "さ行", "た行", "な行", "は行", "ま行", "や行", "ら行", "わ行"]))
        parts.append(liste([s for s in base if not s["gojuon"]["voyelle"]], "%s — ん" % ecr.capitalize()))
        parts.append(grille([s for s in de if s["categorie"] in ("dakuten", "handakuten")],
                            "%s — dakuten et handakuten (25)" % ecr.capitalize(),
                            ["が行", "ざ行", "だ行", "ば行", "ぱ行"]))
        parts.append(liste([s for s in de if s["categorie"] == "yoon"],
                           "%s — yōon (33)" % ecr.capitalize(), 3))
    parts.append(liste([s for s in S if s["categorie"] in ("petit-tsu", "allongement")],
                       "Petit tsu et allongement"))
    parts.append(liste([s for s in S if s["categorie"] == "etendu"],
                       "Katakana étendus (notice de 1991, tableaux 1 puis 2)"))
    parts.append(liste([s for s in S if s["categorie"] == "rare"], "Signes obsolètes"))
    page = """<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Planche des kana</title>
<style>
:root{--fond:#fbf8f2;--encre:#1c2430;--doux:#6b7280;--trait:#ddd5c6;--rare:#f3e6cf}
@media (prefers-color-scheme:dark){:root{--fond:#161b22;--encre:#e8e3d8;--doux:#9aa3ad;--trait:#333b46;--rare:#3a3222}
 .svg img{filter:invert(1)}}
body{background:var(--fond);color:var(--encre);font-family:system-ui,sans-serif;margin:0 16px 40px}
h1{font-size:1.4rem}h2{font-size:1.05rem;margin:28px 0 8px}
p{color:var(--doux);max-width:60em}
table{border-collapse:collapse}
th{font-weight:500;color:var(--doux);padding:4px 8px}
td{border:1px solid var(--trait);text-align:center;padding:6px;width:150px;vertical-align:top}
td.vide{background:transparent}td.rare{background:var(--rare)}
.k{font-size:2.2rem;line-height:1.2;font-family:"Noto Sans JP","Hiragino Sans","Yu Gothic",sans-serif}
.r{font-weight:600}.t{font-size:.7rem;color:var(--doux)}
.svg img{width:72px;height:72px}
</style></head><body>
<h1>Planche de contrôle des kana</h1>
<p>Générée depuis <code>kana.json</code> par <code>outils/planche.py</code>. Chaque case : le signe,
son romaji Hepburn, son nombre de traits, son groupe d'apprentissage et le tracé KanjiVG avec ses
traits numérotés. Fond coloré = signe à statut particulier (particule seulement, obsolète).
Ordre des traits : KanjiVG (kanjivg.tagaini.net), CC BY-SA 3.0.</p>
%s
</body></html>
""" % "\n".join(parts)
    open(os.path.join(KANA, "planche.html"), "w", encoding="utf-8").write(page)
    print("planche.html écrite")


if __name__ == "__main__":
    main()
