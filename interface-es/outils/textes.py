# -*- coding: utf-8 -*-
"""Controle d'un lot de textes {cle: espagnol} contre sa source [{cle, fr, en}].

    python interface-es/outils/textes.py controle interface-es/sources/<nom>.json interface-es/lots/<nom>.es.json

Garde-fous (une FAUTE arrete la pose) : chaque cle de la source a sa
traduction et aucune en trop ; aucune n'est vide ; les {marques} et les
balises HTML sont celles du francais ; pas de vosotros ni de forme d'Espagne
en -ais / -eis. Les AVIS sont a regarder : texte identique au francais alors
que l'anglais differe, mots qui ne peuvent etre que francais.
"""
import io
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARQUE = re.compile(r"\{[a-zA-Z_0-9]+\}")
BALISE = re.compile(r"</?([a-zA-Z]+)[^>]*>")
VOSOTROS = re.compile(r"(?<![\w])(vosotros|vosotras|vuestro|vuestra|vuestros|vuestras|sois|estáis|habéis|tenéis|"
                      r"[a-zñ]+áis|[a-zñ]+éis)(?![\w])", re.I)
FRANCAIS = re.compile(r"(?<![\w'’])(je|nous|vous|avec|pour|dans|est|sont|chez|très|aussi|mais|déjà|leur|cette|ces|"
                      r"pas|ton|tes|aux|du|des|et)(?![\w'’])", re.I)
LETTRES_FR = re.compile(r"[çèêëàâîïôûùœ]")


def sans_balises(t):
    return re.sub(r"<[^>]+>", " ", t)


def sans_allemand(t):
    """Retire ce qui est en italique (<em>…</em>, les phrases allemandes) avant de chercher du francais."""
    return re.sub(r"<em>.*?</em>", " ", t, flags=re.S)


def controle(source, lot, silencieux=False):
    src = {x["cle"]: x for x in json.load(io.open(source, encoding="utf-8"))}
    trad = json.load(io.open(lot, encoding="utf-8"))
    fautes, avis = [], []
    for k in src:
        if k not in trad:
            fautes.append("sans traduction : " + k)
    for k in trad:
        if k not in src:
            fautes.append("en trop : " + k)
    for k, v in trad.items():
        if k not in src:
            continue
        f, e = src[k]["fr"], src[k].get("en", "")
        if not isinstance(v, str) or not v.strip():
            fautes.append("vide : " + k)
            continue
        if sorted(MARQUE.findall(v)) != sorted(MARQUE.findall(f)):
            fautes.append("marques differentes : %s %s / %s" % (k, MARQUE.findall(f), MARQUE.findall(v)))
        if sorted(BALISE.findall(v)) != sorted(BALISE.findall(f)):
            fautes.append("balises differentes : %s (%s / %s)" % (k, sorted(BALISE.findall(f)), sorted(BALISE.findall(v))))
        lisible = sans_balises(sans_allemand(v))
        m = next((x.group(0) for x in VOSOTROS.finditer(lisible)
                  if x.group(0).lower() not in ("dieciséis", "veintiséis")), None)
        if m:
            fautes.append("vosotros ou forme d'Espagne : %s (%r)" % (k, m))
        if v == f and len(f) > 3 and e != f:
            avis.append("identique au francais : " + k)
        if LETTRES_FR.search(lisible) or FRANCAIS.search(lisible):
            mm = LETTRES_FR.search(lisible) or FRANCAIS.search(lisible)
            avis.append("du francais ? %s (%r)" % (k, mm.group(0)))
    if not silencieux:
        print("%s : %d textes, %d fautes, %d avis" % (lot, len(trad), len(fautes), len(avis)))
        for x in fautes:
            print("  FAUTE " + x)
        for x in avis:
            print("  avis  " + x)
    return fautes, avis


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] != "controle":
        sys.exit(__doc__)
    f, _ = controle(sys.argv[2], sys.argv[3])
    sys.exit(1 if f else 0)
