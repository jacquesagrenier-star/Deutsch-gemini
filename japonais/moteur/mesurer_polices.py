# -*- coding: utf-8 -*-
"""Combien pese une police japonaise pour l'app, mesure et non suppose.

Trois mesures, sur le serveur reel de Google Fonts :
  1. la police ENTIERE (toutes les tranches unicode-range de Noto Sans JP,
     un seul poids) -- ce que tirerait un navigateur qui afficherait tout ;
  2. les tranches qu'un ecran N5 typique declencherait (kana + kanji N5) ;
  3. une police SOUS-ENSEMBLE construite par Google avec `&text=` sur ces
     memes caracteres -- une seule requete.
Et, pour comparer, les polices que l'app allemande charge deja.

    python japonais/moteur/mesurer_polices.py [fichier_de_caracteres.txt]

Sans argument : kana (U+3041-U+30FC) + les 103 kanji N5 lus sur la branche
japonais-kanji-mnemo si git la connait, sinon les kana seuls.
Bibliotheque standard seulement. A besoin du reseau.
"""
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")  # sinon pas de woff2


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def poids(url):
    return len(get(url))


def faces(css):
    """[(url, [(debut, fin), ...]), ...] pour chaque @font-face."""
    out = []
    for bloc in re.findall(r"@font-face\s*\{(.*?)\}", css, re.S):
        url = re.search(r"url\((https://[^)]+)\)", bloc).group(1)
        plages = []
        m = re.search(r"unicode-range:\s*([^;]+);", bloc)
        if m:
            for p in m.group(1).split(","):
                p = p.strip()[2:]
                if "-" in p:
                    a, b = p.split("-")
                    plages.append((int(a, 16), int(b, 16)))
                else:
                    plages.append((int(p, 16), int(p, 16)))
        out.append((url, plages))
    return out


def caracteres_par_defaut():
    kana = "".join(chr(c) for c in range(0x3041, 0x3097)) + \
           "".join(chr(c) for c in range(0x30A1, 0x30FD))
    try:
        brut = subprocess.run(
            ["git", "show", "origin/japonais-kanji-mnemo:japonais/kanji/mnemoniques_n5.json"],
            capture_output=True, check=True).stdout.decode("utf-8")
        texte = brut
        kanji = sorted({c for c in texte if 0x4E00 <= ord(c) <= 0x9FFF})
        # On ne garde que les cles d'entree si la forme le permet.
        d = json.loads(brut)
        entrees = d.get("kanji", d) if isinstance(d, dict) else d
        if isinstance(entrees, dict):
            kanji = [k for k in entrees if len(k) == 1]
        elif isinstance(entrees, list):
            kanji = [e.get("kanji") or e.get("caractere") for e in entrees
                     if isinstance(e, dict)]
            kanji = [k for k in kanji if k]
        return kana, "".join(kanji)
    except Exception as e:
        print("  (kanji N5 non lus : %s -- kana seuls)" % e)
        return kana, ""


def main():
    if len(sys.argv) > 1:
        texte = open(sys.argv[1], encoding="utf-8").read()
        kana, kanji = texte, ""
    else:
        kana, kanji = caracteres_par_defaut()
    texte = kana + kanji
    print("Caracteres mesures : %d (dont %d kanji)" % (len(set(texte)), len(set(kanji))))

    css = get("https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400&display=swap").decode()
    fs = faces(css)
    total = 0
    touchees = 0
    poids_touchees = 0
    besoins = {ord(c) for c in texte}
    for url, plages in fs:
        n = poids(url)
        total += n
        if any(a <= c <= b for c in besoins for a, b in plages):
            touchees += 1
            poids_touchees += n
    print("1. Noto Sans JP 400, police entiere : %d tranches, %d Ko" % (len(fs), total // 1024))
    print("2. Tranches declenchees par ces caracteres : %d, %d Ko" % (touchees, poids_touchees // 1024))

    q = urllib.parse.quote("".join(sorted(set(texte))))
    css2 = get("https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400&display=swap&text=" + q).decode()
    sous = sum(poids(u) for u, _ in faces(css2))
    print("3. Sous-ensemble &text= (une requete) : %d Ko" % (sous // 1024))

    css3 = get("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,200..800"
               "&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&display=swap").decode()
    lat = [(u, p) for u, p in faces(css3) if any(a <= 0x41 <= b for a, b in p)]
    print("Reference -- polices actuelles de l'app, tranches latines : %d fichiers, %d Ko"
          % (len(lat), sum(poids(u) for u, _ in lat) // 1024))


if __name__ == "__main__":
    main()
