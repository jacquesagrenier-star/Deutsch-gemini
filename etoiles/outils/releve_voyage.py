# -*- coding: utf-8 -*-
"""Refait les releves des 42 figures du voyage (voyage.py) dans etoiles/sources/. A ne relancer que si l'on change
les etoiles d'une figure : construire.py, lui, ne lit que les fichiers ecrits ici.

    python etoiles/outils/releve_voyage.py

Ecrit :
- simbad_voyage.txt : la reponse de SIMBAD (miroir de Harvard, sim-script), une ligne par designation de voyage.py,
  dans l'ordre de designations_voyage(), puis celles de PARALLAXE_DU_SYSTEME ;
- simbad_voyage_parallaxes.tsv : TOUTES les parallaxes que SIMBAD connait pour ces etoiles (table mesPLX, service TAP),
  pour comparer Hipparcos (van Leeuwen 2007) et Gaia ;
- bsc5_extrait.txt : les lignes du Yale Bright Star Catalogue (5e ed.) qu'on utilise (V_DU_BSC), telles quelles ;
- IAU-CSN.txt : la liste officielle des noms d'etoiles de l'UAI (WGSN), telle que publiee ;
- wikipedia_noms.json : le titre de l'article de chaque constellation dans les Wikipedia de nos langues (Wikidata),
  pour controle.py."""
import gzip, io, json, os, sys, urllib.parse, urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCES = os.path.join(os.path.dirname(ICI), "sources")
sys.path.insert(0, ICI)
from voyage import VOYAGE, PARALLAXE_DU_SYSTEME, V_DU_BSC, designations_voyage

SIMBAD = "https://simbad.harvard.edu/simbad/"
AGENT = {"User-Agent": "wortando-ciel/1.0"}
LANGUES_WIKI = ["fr", "de", "es", "pt", "ja", "tr", "pl", "ru", "uk", "ar", "fa", "en"]
# La constellation de chaque figure, par l'article de Wikipedia en anglais (pour retrouver l'objet Wikidata).
ARTICLE_EN = {
 "UMi": "Ursa Minor", "Leo": "Leo (constellation)", "Tau": "Taurus (constellation)", "Boo": "Boötes",
 "And": "Andromeda (constellation)", "Per": "Perseus (constellation)", "Her": "Hercules (constellation)",
 "Dra": "Draco (constellation)", "Aql": "Aquila (constellation)", "Tri": "Triangulum", "Vir": "Virgo (constellation)",
 "Sco": "Scorpius", "Sgr": "Sagittarius (constellation)", "CMa": "Canis Major", "Ari": "Aries (constellation)",
 "Cnc": "Cancer (constellation)", "Lib": "Libra (constellation)", "Cap": "Capricornus", "Aqr": "Aquarius (constellation)",
 "Psc": "Pisces (constellation)", "Oph": "Ophiuchus", "Lep": "Lepus (constellation)", "Cet": "Cetus",
 "Hya": "Hydra (constellation)", "Crt": "Crater (constellation)", "Col": "Columba (constellation)",
 "Eri": "Eridanus (constellation)", "Cen": "Centaurus", "Car": "Carina (constellation)", "Vel": "Vela (constellation)",
 "Pup": "Puppis", "Lup": "Lupus (constellation)", "Ara": "Ara (constellation)", "CrA": "Corona Australis",
 "TrA": "Triangulum Australe", "Pav": "Pavo (constellation)", "Gru": "Grus (constellation)",
 "Phe": "Phoenix (constellation)", "PsA": "Piscis Austrinus", "Tuc": "Tucana", "Mus": "Musca", "Hyi": "Hydrus",
}
QID = {"Cet": "Q8839", "Eri": "Q10433"}   # titres anglais ambigus : l'objet Wikidata directement


def poster(url, champs):
    data = urllib.parse.urlencode(champs).encode()
    return urllib.request.urlopen(urllib.request.Request(url, data=data, headers=AGENT), timeout=180).read().decode("utf-8")


def obtenir(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=AGENT), timeout=180).read()


def releve_simbad(ids):
    script = ('output console=off script=off\n'
              'format object "%MAIN_ID|%COO(d;A D)|%FLUXLIST(B;F)|%FLUXLIST(V;F)|%PLX(V E Q B)|%IDLIST(HIP)|%IDLIST(HR)"\n'
              + "\n".join(ids) + "\n")
    txt = poster(SIMBAD + "sim-script", {"script": script})
    lignes = [l for l in txt.splitlines() if l.startswith("*")]
    # Le miroir glisse parfois dans sa section « ::error:: » des messages d'autres requetes : seul compte qu'il y ait
    # une ligne par identifiant demande.
    if len(lignes) != len(ids):
        raise SystemExit("SIMBAD ne reconnait pas un identifiant :\n" + txt.split("::data::")[0][:3000])
    tete = ("# Reponse de SIMBAD (miroir de Harvard, simbad.harvard.edu), releve par etoiles/outils/releve_voyage.py,\n"
            "# requete sim-script, format object \"%MAIN_ID|%COO(d;A D)|%FLUXLIST(B;F)|%FLUXLIST(V;F)|%PLX(V E Q B)|"
            "%IDLIST(HIP)|%IDLIST(HR)\" :\n"
            "# designation principale | ascension droite et declinaison en degres (ICRS, J2000) | magnitudes B et V |\n"
            "# parallaxe (mas), son erreur, sa qualite, sa reference | numeros Hipparcos et HR. Une ligne par identifiant\n"
            "# demande, dans l'ordre ci-dessous (voyage.py). Reproduit tel quel ; un champ vide est une valeur absente.\n"
            "# Identifiants demandes : " + " ; ".join(ids) + "\n")
    return tete + "\n".join(lignes) + "\n"


def releve_parallaxes(ids):
    sortie = []
    for i in range(0, len(ids), 60):
        lot = []
        for x in ids[i:i + 60]:
            # la forme normalisee de la table ident : « * alf Leo », « *  41 Ari » (numeros sur trois caracteres)
            t = x.split()
            lot.append("'* " + (t[0].rjust(3) if t[0].isdigit() else t[0]) + " " + " ".join(t[1:]) + "'")
        q = ("SELECT i.id, m.plx, m.plx_err, m.bibcode FROM ident AS i JOIN mesPLX AS m ON m.oidref = i.oidref "
             "WHERE i.id IN (" + ",".join(lot) + ")")
        l = poster(SIMBAD + "sim-tap/sync", {"request": "doQuery", "lang": "adql", "format": "tsv", "query": q}).splitlines()
        sortie += l if not sortie else l[1:]
    sortie = sortie[:1] + sorted(sortie[1:])
    tete = ("# Toutes les parallaxes connues de SIMBAD pour les etoiles du voyage (table mesPLX, service TAP du miroir de\n"
            "# Harvard), releve par etoiles/outils/releve_voyage.py. Colonnes : identifiant, parallaxe (mas), erreur, reference.\n")
    return tete + "\n".join(sortie) + "\n"


def extrait_bsc():
    brut = gzip.decompress(obtenir("http://tdc-www.harvard.edu/catalogs/ybsc5.gz")).decode("latin-1").splitlines()
    voulus = sorted({hr for l in V_DU_BSC.values() for hr in l})
    lignes = [l for l in brut if l[:4].strip().isdigit() and int(l[:4]) in voulus]
    assert len(lignes) == len(voulus)
    tete = ("# Yale Bright Star Catalogue, 5e edition revisee (Hoffleit et Warren 1991 ; NASA ADC / CDS V/50), version ASCII\n"
            "# du Telescope Data Center de Harvard (tdc-www.harvard.edu/catalogs/ybsc5.gz). Les lignes utilisees, telles\n"
            "# quelles (format : ybsc5.readme ; V en colonnes 103-107, B-V en 110-114). Domaine public.\n")
    return tete + "\n".join(lignes) + "\n"


def noms_wikipedia():
    titres = {c: ARTICLE_EN[c] for c in ARTICLE_EN if c not in QID}
    out = {}
    sites = "|".join(l + "wiki" for l in LANGUES_WIKI)
    lots = [("titles", list(titres.values())[i:i + 40]) for i in range(0, len(titres), 40)] + [("ids", list(QID.values()))]
    inverse = {v: k for k, v in titres.items()}
    for cle, lot in lots:
        champs = {"action": "wbgetentities", "props": "sitelinks", "sitefilter": sites, "format": "json", cle: "|".join(lot)}
        if cle == "titles":
            champs["sites"] = "enwiki"
        d = json.loads(obtenir("https://www.wikidata.org/w/api.php?" + urllib.parse.urlencode(champs)))
        for qid, e in d["entities"].items():
            liens = {s[:-4]: v["title"] for s, v in e.get("sitelinks", {}).items()}
            con = next((k for k, v in QID.items() if v == qid), None) or inverse.get(liens.get("en"))
            if con:
                out[con] = dict(wikidata=qid, articles=liens)
    assert set(out) == set(ARTICLE_EN), set(ARTICLE_EN) - set(out)
    return out


def main():
    ids = designations_voyage()
    tous = ids + [v for v in PARALLAXE_DU_SYSTEME.values() if v not in ids]
    open(os.path.join(SOURCES, "simbad_voyage.txt"), "w", encoding="utf-8").write(releve_simbad(tous))
    open(os.path.join(SOURCES, "simbad_voyage_parallaxes.tsv"), "w", encoding="utf-8").write(releve_parallaxes(tous))
    open(os.path.join(SOURCES, "bsc5_extrait.txt"), "w", encoding="utf-8").write(extrait_bsc())
    csn = obtenir("https://www.pas.rochester.edu/~emamajek/WGSN/IAU-CSN.txt").decode("utf-8")
    open(os.path.join(SOURCES, "IAU-CSN.txt"), "w", encoding="utf-8").write(csn)
    json.dump(noms_wikipedia(), open(os.path.join(SOURCES, "wikipedia_noms.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, sort_keys=True)
    print(len(tous), "identifiants releves")


if __name__ == "__main__":
    main()
