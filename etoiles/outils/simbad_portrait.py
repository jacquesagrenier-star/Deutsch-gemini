# -*- coding: utf-8 -*-
"""Le portrait des etoiles (ligne 160, livraison B) : RELEVE, a relancer seulement pour rafraichir les mesures.

    python etoiles/outils/simbad_portrait.py

Pour chacune des 434 etoiles du ciel (designations de etoiles/sources-etoiles.json), SIMBAD donne :
  - le type spectral (table basic : sp_type, sa qualite et sa reference) ;
  - les diametres angulaires mesures (table mesDiameter, en mas), dont on garde chaque mesure avec sa reference.
Ecrit etoiles/sources/simbad_types.tsv et etoiles/sources/simbad_diametres.tsv, lus par etoiles/outils/portrait.py.

Le serveur de Strasbourg refusait les requetes automatiques le 20 nov. 2026 ; le miroir de Harvard sert la meme base
(simbad.harvard.edu, meme schema TAP). Donnees SIMBAD : CDS, Strasbourg (Wenger et al. 2000, A&AS 143, 9).
"""
import csv
import io
import json
import os
import sys
import time
import urllib.parse
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
SERVEURS = ["https://simbad.harvard.edu/simbad/sim-tap/sync", "https://simbad.cds.unistra.fr/simbad/sim-tap/sync"]


def tap(adql):
    derniere = None
    for url in SERVEURS:
        q = urllib.parse.urlencode({"request": "doQuery", "lang": "adql", "format": "csv", "query": adql}).encode()
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=q, headers={"User-Agent": "wortando-etoiles/1.0"}), timeout=120) as r:
                txt = r.read().decode("utf-8")
            if txt.lstrip().startswith("<"):
                derniere = "page HTML de " + url
                continue
            return list(csv.DictReader(io.StringIO(txt)))
        except Exception as e:
            derniere = "%s : %s" % (url, e)
    raise SystemExit("SIMBAD injoignable (%s)" % derniere)


def main():
    src = json.load(open(os.path.join(RACINE, "sources-etoiles.json"), encoding="utf-8"))["constellations"]
    ids = [" ".join(e["simbad"].split()) for c in src.values() for e in c]
    types, diam = {}, []
    for k in range(0, len(ids), 60):
        lot = ids[k:k + 60]
        liste = ",".join("'* %s'" % i.replace("'", "''") for i in lot)
        for r in tap("SELECT i.id, b.main_id, b.sp_type, b.sp_qual, b.sp_bibcode FROM ident AS i JOIN basic AS b ON i.oidref = b.oid "
                     "WHERE i.id IN (%s)" % liste):
            types[" ".join(r["id"][2:].split())] = r
        for r in tap("SELECT i.id, d.diameter, d.qual, d.unit, d.error, d.filter, d.method, d.bibcode FROM ident AS i "
                     "JOIN mesDiameter AS d ON i.oidref = d.oidref WHERE i.id IN (%s)" % liste):
            r["id"] = " ".join(r["id"][2:].split())
            diam.append(r)
        time.sleep(1)
        print("  %d / %d" % (min(k + 60, len(ids)), len(ids)), flush=True)
    manque = [i for i in ids if i not in types]
    with open(os.path.join(RACINE, "sources", "simbad_types.tsv"), "w", encoding="utf-8", newline="") as f:
        f.write("# Types spectraux SIMBAD (table basic), releve du %s par etoiles/outils/simbad_portrait.py. CDS, Strasbourg.\n" % time.strftime("%Y-%m-%d"))
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["designation", "main_id", "sp_type", "sp_qual", "sp_bibcode"])
        for i in ids:
            r = types.get(i)
            if r:
                w.writerow([i, r["main_id"], r["sp_type"], r["sp_qual"], r["sp_bibcode"]])
    with open(os.path.join(RACINE, "sources", "simbad_diametres.tsv"), "w", encoding="utf-8", newline="") as f:
        f.write("# Diametres angulaires mesures SIMBAD (table mesDiameter), releve du %s par etoiles/outils/simbad_portrait.py. CDS, Strasbourg.\n" % time.strftime("%Y-%m-%d"))
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["designation", "diameter", "unit", "error", "qual", "filter", "method", "bibcode"])
        for r in sorted(diam, key=lambda x: (ids.index(x["id"]) if x["id"] in ids else 9999, x["bibcode"])):
            w.writerow([r["id"], r["diameter"], r["unit"], r["error"], r["qual"], r["filter"], r["method"], r["bibcode"]])
    print("types : %d / %d (sans type : %s) ; mesures de diametre : %d, pour %d etoiles" % (
        len(types), len(ids), manque[:10], len(diam), len({r["id"] for r in diam})))


if __name__ == "__main__":
    main()
