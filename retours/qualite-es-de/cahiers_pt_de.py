# -*- coding: utf-8 -*-
"""Erreurs des donnees de l'app trouvees par les traducteurs des cahiers pt et
de (13 nov. 2026, note partagee cahiers-pt-de.md, « a corriger dans l'app »).
Remplacements bruts, chacun verifie (le texte actuel doit y figurer, autant de
fois qu'attendu), pour garder la mise en forme de chaque fichier.

  1. la leche / die Milch : la fiche du genre (attention.de) et les consignes
     de traduction la donnaient comme genre different ; die Milch est feminin.
     -> la sal / das Salz.
  2. « hace + durée » : du francais dans explanation_pt et explanation_de de
     sept exercices au preterit -> « hace + duração », „hace + Zeitraum“.
  3. « casar com » : la fiche pronominales (pt) rangeait casarse con parmi les
     verbes non pronominaux en portugais ; casar-se com est la norme
     -> darse cuenta de (perceber).
  4. Kämm et sept autres : huit exercices du present (« ___ a la niña antes del
     colegio ») sont des imperatifs tu (Adivina quién…, Escoge el que más te
     guste) et traduits comme tels dans les cinq langues ; l'explication disait
     « Present, il/elle ». Elle dit maintenant l'imperatif, et que la forme est
     celle du present il/elle.

    python retours/qualite-es-de/cahiers_pt_de.py            # montre
    python retours/qualite-es-de/cahiers_pt_de.py --ecrire   # applique
"""
import io
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
ECRIRE = "--ecrire" in sys.argv

# (fichier, ancien, nouveau, nombre d'occurrences attendu)
R = [
    ("espanol/datos/grammaire.json",
     "<b>la luna</b>, <b>la mesa</b>, <b>la leche</b> (der Mond, der Tisch, die Milch)",
     "<b>la luna</b>, <b>la mesa</b>, <b>la sal</b> (der Mond, der Tisch, das Salz)", 1),
    ("espanol/de/CONSIGNES.md", "la leche / die Milch", "la sal / das Salz", 1),
    ("espanol/datos/ejercicios.json", "« hace + durée » (… atrás)", "« hace + duração » (… atrás)", 7),
    ("espanol/datos/ejercicios.json", "„hace + durée“ (vor …)", "„hace + Zeitraum“ (vor …)", 7),
    ("espanol/datos/grammaire.json",
     "<b>quedarse</b> (ficar), <b>casarse con</b> (casar com)",
     "<b>quedarse</b> (ficar), <b>darse cuenta de</b> (perceber)", 1),
]

# 4. Les huit imperatifs : (rang dans « exercises », verbe, forme)
IMPERATIFS = [(27, "dejar", "deja"), (28, "peinar", "peina"), (45, "anotar", "anota"),
              (46, "adivinar", "adivina"), (47, "escoger", "escoge"), (48, "simplificar", "simplifica"),
              (51, "vigilar", "vigila"), (59, "detallar", "detalla")]
EXPL = {
    "explanation": ("Présent de « {v} », il/elle : {f}.",
                    "Impératif de « {v} », tú : {f} — la même forme que le présent, il/elle."),
    "explanation_en": ("Present of « {v} », he/she: {f}.",
                       "Imperative of « {v} », tú: {f} — the same form as the present, he/she."),
    "explanation_pt": ("Presente de « {v} », ele/ela: {f}.",
                       "Imperativo de « {v} », tú: {f} — a mesma forma do presente, ele/ela."),
    "explanation_ar": ("المضارع من «{v}»، هو/هي: {f}.",
                       "الأمر من «{v}»، tú: {f} — وهي صيغة المضارع نفسها مع هو/هي."),
    "explanation_de": ("Presente von „{v}“, er/sie: {f}.",
                       "Imperativ von „{v}“, tú: {f} — dieselbe Form wie das Presente, er/sie."),
}

j = lambda s: json.dumps(s, ensure_ascii=False)
raws, journal = {}, []


def lire(f):
    if f not in raws:
        raws[f] = io.open(os.path.join(RACINE, f), encoding="utf-8", newline="").read()
    return raws[f]


for f, a, b, n in R:
    raw = lire(f)
    a2, b2 = (a, b) if f.endswith(".md") else (j(a)[1:-1], j(b)[1:-1])
    assert raw.count(a2) == n, (f, a[:50], raw.count(a2))
    raws[f] = raw.replace(a2, b2)
    journal.append((f, n, a, b))

F = "espanol/datos/ejercicios.json"
avant = json.loads(lire(F))["jeux"]["exercises"]
for rang, v, forme in IMPERATIFS:
    e = avant[rang]
    assert e["correct"] == forme and e["question"].startswith("___"), (rang, e["correct"])
    for k, (vieux, neuf) in EXPL.items():
        vieux, neuf = vieux.format(v=v, f=forme), neuf.format(v=v, f=forme)
        assert e[k] == vieux, (rang, k, e[k])
        a2, b2 = '"%s": %s' % (k, j(vieux)), '"%s": %s' % (k, j(neuf))
        # le texte « Présent de « dejar »... » existe ailleurs pour d'autres phrases :
        # on remplace celui qui suit la question de CET exercice
        raw = raws[F]
        debut = raw.index('"question": %s' % j(e["question"]))
        p = raw.index(a2, debut)
        raws[F] = raw[:p] + b2 + raw[p + len(a2):]
        journal.append((F, 1, "exercises[%d].%s" % (rang, k), neuf))

for f in raws:
    if f.endswith(".json"):
        json.loads(raws[f])
apres = json.loads(raws[F])["jeux"]["exercises"]
for rang, v, forme in IMPERATIFS:
    assert apres[rang]["explanation"].startswith("Impératif"), rang
for f, n, a, b in journal:
    print("%s ×%d\n   - %s\n   + %s" % (f, n, a[:100], b[:100]))
print("\n%d remplacements" % sum(n for _, n, _, _ in journal))
if ECRIRE:
    for f, raw in raws.items():
        io.open(os.path.join(RACINE, f), "w", encoding="utf-8", newline="").write(raw)
    print("ecrit")
