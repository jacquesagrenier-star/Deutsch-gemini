# -*- coding: utf-8 -*-
"""Les cles d'interface (dictionnaire I18N d'index.html) qui manquent au bloc « es ».

    python interface-es/outils/cles_i18n.py extraire   -> interface-es/sources/i18n-manquantes.json
    python interface-es/outils/cles_i18n.py controle   lit interface-es/lots/i18n-manquantes.es.json
    python interface-es/outils/cles_i18n.py pose       ecrit les cles a la fin du bloc « es » d'I18N

Le bloc « es » d'I18N a ete traduit le 2 nov. 2026 pour l'anglais appris, MAIS
depuis la base francaise, qui parle de l'allemand : il vaut tel quel pour
l'allemand appris. Il lui manque les cles ajoutees a la base depuis.

⚠️ On ne cherche jamais « es: { » dans tout le fichier (l'espagnol APPRIS a ses
propres tables « es: { ... } ») : seulement dans le dictionnaire I18N, dont on
trouve d'abord les bornes.

Garde-fous de la pose : chaque cle demandee a sa traduction et aucune en trop ;
aucune ne recopie le francais ; les {marques} et les balises sont celles du
francais ; apres l'ecriture, le bloc relu contient chaque cle avec la valeur
demandee. Une faute arrete tout, rien n'est ecrit.
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RACINE = os.path.dirname(ICI)
INDEX = os.path.join(RACINE, "index.html")
SOURCE = os.path.join(ICI, "sources", "i18n-manquantes.json")
LOT = os.path.join(ICI, "lots", "i18n-manquantes.es.json")
MARQUE = re.compile(r"\{[a-zA-Z_0-9]+\}")
BALISE = re.compile(r"</?([a-zA-Z]+)[^>]*>")
CLE = re.compile(r'^        (?:([A-Za-z_][A-Za-z0-9_]*)|"([^"]+)")\s*:\s*(.*?),?\s*$')


def lire():
    return io.open(INDEX, encoding="utf-8", newline="").read()


def blocs(s):
    """{langue: (debut, fin)} des blocs du dictionnaire I18N (fin = la ligne « }, » du bloc)."""
    d = s.index("\nconst I18N = {")
    f = s.index("\n};", d)
    bornes = [(m.start(), m.group(1)) for m in re.finditer(r"^    ([a-z]{2}): \{\s*$", s[d:f], re.M)]
    out = {}
    for i, (b, lg) in enumerate(bornes):
        e = bornes[i + 1][0] if i + 1 < len(bornes) else f - d
        out[lg] = (d + b, d + e)
    return out


def valeurs(s, debut, fin):
    """Les cles d'un bloc et leur valeur JavaScript brute (une cle par ligne)."""
    out = {}
    for l in s[debut:fin].splitlines():
        m = CLE.match(l)
        if m:
            out[m.group(1) or m.group(2)] = m.group(3)
    return out


def js_texte(brut):
    """La valeur JS « "…" » en texte, ou None si ce n'est pas une chaine simple."""
    brut = brut.strip()
    if len(brut) >= 2 and brut[0] == '"' and brut[-1] == '"':
        try:
            return json.loads(brut)
        except ValueError:
            return None
    return None


def extraire():
    s = lire()
    b = blocs(s)
    fr = valeurs(s, *b["fr"])
    en = valeurs(s, *b["en"])
    es = valeurs(s, *b["es"])
    manq = [k for k in fr if k not in es]
    if not manq:
        # Ne pas ecraser la source du dernier lot pose : elle sert encore au controle.
        print("aucune cle manquante : le bloc es d'I18N est complet")
        return
    out, complexes = [], []
    for k in manq:
        t = js_texte(fr[k])
        if t is None:
            complexes.append(k)
            continue
        out.append({"cle": k, "fr": t, "en": js_texte(en.get(k, "")) or ""})
    os.makedirs(os.path.dirname(SOURCE), exist_ok=True)
    io.open(SOURCE, "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print("%d cles manquantes, %d ecrites dans %s" % (len(manq), len(out), os.path.relpath(SOURCE, RACINE)))
    if complexes:
        print("valeurs qui ne sont pas des chaines simples (a traiter a la main) :", complexes)


def controle():
    src = {x["cle"]: x for x in json.load(io.open(SOURCE, encoding="utf-8"))}
    lot = json.load(io.open(LOT, encoding="utf-8"))
    fautes = []
    for k in set(src) - set(lot):
        fautes.append("sans traduction : " + k)
    for k in set(lot) - set(src):
        fautes.append("en trop : " + k)
    for k, v in lot.items():
        if k not in src:
            continue
        f = src[k]["fr"]
        if not isinstance(v, str) or not v.strip():
            fautes.append("vide : " + k)
            continue
        # Un nom propre (« Goethe-Zertifikat B1 ») est le meme partout : identique
        # au francais n'est une faute que si l'anglais, lui, differe.
        if v == f and len(f) > 3 and src[k]["en"] != f:
            fautes.append("recopie le francais : " + k)
        if sorted(MARQUE.findall(v)) != sorted(MARQUE.findall(f)):
            fautes.append("marques differentes : %s %s / %s" % (k, MARQUE.findall(f), MARQUE.findall(v)))
        if sorted(BALISE.findall(v)) != sorted(BALISE.findall(f)):
            fautes.append("balises differentes : " + k)
    if fautes:
        sys.exit("\n".join(sorted(fautes)))
    print("controle : %d cles, aucune faute" % len(lot))
    return src, lot


def pose():
    src, lot = controle()
    s = lire()
    nl = "\r\n" if "\r\n" in s else "\n"
    b = blocs(s)
    debut, fin = b["es"]
    deja = valeurs(s, debut, fin)
    if set(lot) & set(deja):
        sys.exit("deja dans le bloc es : %s" % sorted(set(lot) & set(deja))[:5])
    bloc = s[debut:fin]
    # la fermeture du bloc : la derniere ligne « }, » ou « } »
    m = list(re.finditer(r"^    \},?\s*$", bloc, re.M))[-1]
    corps = bloc[:m.start()].rstrip()
    if not corps.endswith(","):
        corps += ","
    ordre = [x["cle"] for x in json.load(io.open(SOURCE, encoding="utf-8"))]
    ajout = nl + "        // Les cles ajoutees a la base depuis le 2 nov. 2026 (interface-es, 15 nov. 2026)." + nl
    ajout += ("," + nl).join("        %s: %s" % (k if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", k) else json.dumps(k),
                                                 json.dumps(lot[k], ensure_ascii=False)) for k in ordre)
    nouveau = corps + ajout + nl + bloc[m.start():]
    s2 = s[:debut] + nouveau + s[fin:]
    b2 = blocs(s2)
    relu = valeurs(s2, *b2["es"])
    for k in ordre:
        if js_texte(relu.get(k, "")) != lot[k]:
            sys.exit("relecture : %s differe" % k)
    io.open(INDEX, "w", encoding="utf-8", newline="").write(s2)
    print("pose : %d cles ecrites dans le bloc es d'I18N" % len(ordre))


if __name__ == "__main__":
    {"extraire": extraire, "controle": controle, "pose": pose}[sys.argv[1] if len(sys.argv) > 1 else "extraire"]()
