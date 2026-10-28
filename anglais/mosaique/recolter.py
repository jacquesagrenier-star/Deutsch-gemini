"""Les candidats de la mosaique ANGLAISE (27 oct. 2026), recoltes pour que
Jacques choisisse sur planches, comme l'allemand, le japonais et l'espagnol.

Decide par Jacques le 27 oct. 2026 (« Peintres americains ») : des peintres
americains lies a Boston et a la Nouvelle-Angleterre -- Sargent, Homer,
Hassam, Cassatt, Lane au coeur ; Benson, Tarbell, Prendergast, Eakins si la
selection le demande. Il choisit et ordonne sur les planches ; rien n'est
branche dans l'app avant.

REGLE DE DROIT (consigne du chef d'orchestre) : peintre mort avant 1956,
oeuvre faite avant 1931 (domaine public aux Etats-Unis ; et 70 ans apres la
mort ailleurs). Une oeuvre sans date n'est gardee que si le peintre est mort
avant 1931. La licence de CHAQUE fichier est lue sur Commons : domaine public
ou CC0 seulement ; la collection (le musee) vient de Wikidata.

Comme l'espagnol (decisions de Jacques du 14 oct.) : a l'horizontale, rien de
religieux, ni nu, ni sang, ni guerre ; les plus lumineux d'abord. En plus :
Boston et la Nouvelle-Angleterre passent devant (titre qui les nomme).

Relancer : python anglais/mosaique/recolter.py  ->  candidats.json + planche-*.jpg
Les vignettes restent hors de OneDrive (C:/Users/jacqu/.wortando/anglais-mosaique-brut).
"""
import json, math, os, re, sys, time, urllib.parse, urllib.request
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

ICI = os.path.dirname(os.path.abspath(__file__))
BRUT = os.environ.get("WORTANDO_BRUT", "C:/Users/jacqu/.wortando/anglais-mosaique-brut")
UA = {"User-Agent": "Wortando-selection/1.0 (jacques.a.grenier@gmail.com)"}
MORT_AVANT = 1956
OEUVRE_AVANT = 1931
RMIN, RMAX = 1.1, 2.1

# (nom cherche dans Wikidata, combien au plus sur les planches)
PEINTRES = [
    ("John Singer Sargent", 22),
    ("Winslow Homer", 22),
    ("Childe Hassam", 22),
    ("Mary Cassatt", 12),
    ("Fitz Henry Lane", 14),
    ("Frank Weston Benson", 8),
    ("Edmund C. Tarbell", 6),
    ("Maurice Prendergast", 12),
    ("Thomas Eakins", 6),
]

# Boston et la Nouvelle-Angleterre dans le titre : ces tableaux passent devant.
NOUVELLE_ANGLETERRE = re.compile(
    r"boston|gloucester|massachusetts|cape ann|marblehead|salem|nahant|beverly|newburyport|rockport|"
    r"maine|prout|kennebunk|ogunquit|camden|mount desert|penobscot|portland|"
    r"new hampshire|appledore|isles? of shoals|portsmouth|"
    r"rhode island|newport|connecticut|old lyme|cos cob|vermont|nantucket|martha|cape cod|provincetown|"
    r"charles river|common|beacon|back bay|new england|concord|lexington|plymouth|manchester", re.I)

EXCLUS = re.compile(r"nude|naked|bath(?!ing)|bather|martyr|crucif|death|dead|dying|war\b|battle|"
                    r"wounded|gun|rifle|execution|blood|corpse|burial|funeral|hanging|shipwreck|wreck|"
                    r"drown|aeroplane|arras|hospital tent|ypres|trench|tommies|soldier|troops|veteran|"
                    r"galilee|jerusalem|bethlehem|nazareth|olives|"
                    r"virgin|madonna|christ|jesus|\bsaint|holy|angel|apostle|annunciation|nativity|"
                    r"church|chapel|cathedral|prayer|religio|biblic|prophet|crucifix|gassed|"
                    r"study for|sketch|drawing|cartoon", re.I)
# Ecartes a l'oeil sur la premiere recolte (27 oct.) : ce que le titre ne disait pas.
EXCLUS_ID = {
    'Q50818079',   # 28 lieu religieux (mont des Oliviers)
    'Q134100785',   # 33 nu au centre
    'Q19930492',   # 56 guerre (le veteran)
    'Q138007627',   # 72 bebe nu
    'Q7720125',   # 81 guerre de Secession
    'Q20170657',   # 82 camp de la guerre de Secession
    'Q111671296',   # 84 nu
    'Q59510847',   # 88 titre militaire
    'Q106357008',   # 95 guerre, photo avec le cadre
    'Q57458229',   # 101 photo avec le cadre
    'Q104445859',   # 106 enfant nu
    'Q117662765',   # 123 portrait sombre
}


def get(url, params=None):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    for essai in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return json.loads(r.read())
        except Exception as e:
            print("   reessai", essai + 1, e)
            time.sleep(4 * (essai + 1))
    raise RuntimeError(url)


def qid(nom):
    d = get("https://www.wikidata.org/w/api.php", {"action": "wbsearchentities", "search": nom,
            "language": "en", "format": "json", "limit": 5, "type": "item"})
    # Le peintre, pas un tableau qui porte son nom (« painting by... ») :
    # « painting by Charles Hovey Pepper » passait pour Prendergast.
    for r in d.get("search", []):
        desc = (r.get("description") or "").lower()
        if ("paint" in desc or "artist" in desc) and not desc.startswith("painting by"):
            return r["id"]
    return d["search"][0]["id"] if d.get("search") else None


def sparql(q):
    return get("https://query.wikidata.org/sparql", {"query": q, "format": "json"})["results"]["bindings"]


def mort(q):
    b = sparql("SELECT ?d WHERE { wd:%s wdt:P570 ?d }" % q)
    return int(b[0]["d"]["value"][:4]) if b else None


def tableaux(q):
    b = sparql("""SELECT ?i ?img ?en ?fr ?date ?collLabel WHERE {
      ?i wdt:P170 wd:%s; wdt:P31 wd:Q3305213; wdt:P18 ?img.
      FILTER NOT EXISTS { ?i wdt:P136 ?g . VALUES ?g { wd:Q2864737 wd:Q40446 wd:Q742333 wd:Q3374376 } }
      FILTER NOT EXISTS { ?i wdt:P180 ?d . VALUES ?d { wd:Q302 wd:Q345 wd:Q235113 wd:Q10791 } }
      OPTIONAL { ?i rdfs:label ?en FILTER(LANG(?en) = "en") }
      OPTIONAL { ?i rdfs:label ?fr FILTER(LANG(?fr) = "fr") }
      OPTIONAL { ?i wdt:P571 ?date }
      OPTIONAL { ?i wdt:P195 ?coll . ?coll rdfs:label ?collLabel FILTER(LANG(?collLabel) = "en") } }""" % q)
    vus, sortie = {}, []
    for x in b:
        fichier = urllib.parse.unquote(x["img"]["value"].rsplit("/", 1)[-1])
        cle = x["i"]["value"].rsplit("/", 1)[-1]
        coll = (x.get("collLabel") or {}).get("value", "")
        if cle in vus:
            if coll and coll not in vus[cle]["collection"]:
                vus[cle]["collection"].append(coll)
            continue
        t = {"wikidata": cle, "fichier": fichier,
             "titre": (x.get("en") or {}).get("value", ""), "titre_fr": (x.get("fr") or {}).get("value", ""),
             "annee": (x.get("date") or {}).get("value", "")[:4], "collection": [coll] if coll else []}
        vus[cle] = t
        sortie.append(t)
    return sortie


def infos_commons(fichiers):
    sortie = {}
    for k in range(0, len(fichiers), 50):
        lot = fichiers[k:k + 50]
        d = get("https://commons.wikimedia.org/w/api.php", {"action": "query", "format": "json",
                "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": 320,
                "titles": "|".join("File:" + f for f in lot)})
        norm = {n["to"]: n["from"] for n in d["query"].get("normalized", [])}
        for p in d["query"]["pages"].values():
            if "imageinfo" not in p:
                continue
            ii = p["imageinfo"][0]
            em = ii.get("extmetadata", {})
            titre = norm.get(p["title"], p["title"])
            sortie[titre.split(":", 1)[1]] = {
                "licence": em.get("LicenseShortName", {}).get("value", ""),
                "credit": re.sub(r"<[^>]+>", "", em.get("Credit", {}).get("value", ""))[:160],
                "l": ii.get("width"), "h": ii.get("height"),
                "vignette": ii.get("thumburl"), "page": ii.get("descriptionurl"),
                "original": ii.get("url")}
    return sortie


def libre(licence):
    l = licence.lower()
    return "public domain" in l or l.startswith("pd") or "cc0" in l


def vif(im):
    """Le traitement de l'allemand (branding/mosaique)."""
    im = ImageOps.autocontrast(im, cutoff=(1.2, 0.8))
    im = ImageEnhance.Brightness(im).enhance(1.12)
    im = ImageEnhance.Color(im).enhance(1.45)
    return ImageEnhance.Contrast(im).enhance(1.10)


def eclat(im):
    """Couleur saturee et lumineuse (moyenne de S x V apres « vif »), comme l'espagnol."""
    im = vif(im.convert("RGB")).resize((200, max(1, round(200 * im.height / im.width)))).convert("HSV")
    px = list(im.getdata())
    return round(sum(sat * val for _, sat, val in px) / len(px) / 650.25, 1)


def vignette(url, cle):
    f = os.path.join(BRUT, "v-" + cle + ".jpg")
    if not (os.path.exists(f) and os.path.getsize(f) > 2000):
        for essai in range(4):
            try:
                data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
                open(f, "wb").write(data)
                break
            except Exception as e:
                print("   reessai vignette", essai + 1, e)
                time.sleep(4 * (essai + 1))
        else:
            return None
        time.sleep(0.2)
    return Image.open(f)


def main():
    os.makedirs(BRUT, exist_ok=True)
    tous, rapport = [], []
    for nom, plafond in PEINTRES:
        q = qid(nom)
        m = mort(q) if q else None
        if not q or not m or m >= MORT_AVANT:
            rapport.append("%-24s ECARTE (wikidata %s, mort %s)" % (nom, q, m))
            print(rapport[-1])
            continue
        liste = tableaux(q)
        infos = infos_commons([t["fichier"] for t in liste])
        gardes = []
        for t in liste:
            if t["wikidata"] in EXCLUS_ID:
                continue
            an = int(t["annee"]) if t["annee"][:4].isdigit() else None
            if (an is None and m >= OEUVRE_AVANT) or (an is not None and an >= OEUVRE_AVANT):
                continue
            i = infos.get(t["fichier"])
            if not i or not libre(i["licence"]) or not i["vignette"] or not i["l"]:
                continue
            if not (RMIN <= i["l"] / i["h"] <= RMAX):
                continue
            if EXCLUS.search(t["titre"] + " " + t["titre_fr"]) or not t["titre"]:
                continue
            im = vignette(i["vignette"], t["wikidata"])
            if im is None:
                continue
            t.update(i, peintre=nom, mort=m, eclat=eclat(im), cle=t["wikidata"],
                     nouvelle_angleterre=bool(NOUVELLE_ANGLETERRE.search(t["titre"])))
            # Boston et la Nouvelle-Angleterre devant, a eclat egal ou presque.
            t["score"] = t["eclat"] + (25 if t["nouvelle_angleterre"] else 0)
            gardes.append(t)
        gardes.sort(key=lambda t: -t["score"])
        tous.extend(gardes[:plafond])
        rapport.append("%-24s +%d  %3d tableaux, %3d gardes apres filtres (%d de Nouvelle-Angleterre), %2d sur les planches"
                       % (nom, m, len(liste), len(gardes), sum(t["nouvelle_angleterre"] for t in gardes),
                          min(plafond, len(gardes))))
        print(rapport[-1])
    tous.sort(key=lambda t: -t["score"])
    for n, t in enumerate(tous, 1):
        t["num"] = n
    json.dump(tous, open(os.path.join(ICI, "candidats.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    open(os.path.join(ICI, "recolte.txt"), "w", encoding="utf-8").write("\n".join(rapport) + "\n")
    planches(tous)


def planches(tous):
    try:
        f = ImageFont.truetype("arialbd.ttf", 17)
        p = ImageFont.truetype("arial.ttf", 13)
    except Exception:
        f = p = ImageFont.load_default()
    CEL, COLS, PARPL = 260, 6, 36
    for k in range(0, len(tous), PARPL):
        lot = tous[k:k + PARPL]
        rows = (len(lot) + COLS - 1) // COLS
        im = Image.new("RGB", (COLS * CEL, rows * (CEL + 30)), "white")
        d = ImageDraw.Draw(im)
        for i, t in enumerate(lot):
            v = vif(Image.open(os.path.join(BRUT, "v-" + t["cle"] + ".jpg")).convert("RGB"))
            v.thumbnail((CEL - 12, CEL - 50))
            x, y = (i % COLS) * CEL, (i // COLS) * (CEL + 30)
            im.paste(v, (x + (CEL - v.width) // 2, y + 26))
            d.text((x + 6, y + 4), "%d" % t["num"], fill="black", font=f)
            d.text((x + 48, y + 6), t["peintre"][:28], fill=(90, 90, 90), font=p)
            d.text((x + 6, y + CEL - 16), (t["titre"][:30] + (" · " + t["annee"] if t["annee"] else "")),
                   fill=(30, 70, 140) if t["nouvelle_angleterre"] else (110, 110, 110), font=p)
        im.save(os.path.join(ICI, "planche-%d.jpg" % (k // PARPL + 1)), quality=82)


if __name__ == "__main__":
    main()
