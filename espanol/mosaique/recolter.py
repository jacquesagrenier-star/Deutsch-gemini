"""Les candidats de la mosaique ESPAGNOLE (14 oct. 2026), recoltes pour que
Jacques choisisse sur planches, comme pour l'allemand (11-12 sept.) et le
japonais (4 oct.).

Decide avec Jacques le 14 oct. 2026 : UNE seule serie pour l'espagnol, qui
melange l'Espagne et l'Amerique latine. L'Amerique latine a moins de tableaux
libres : l'Espagne complete.

REGLE DE DROIT : PEINTRE MORT AVANT 1926. La serie est vue en Espagne ET en
Amerique latine ; le Mexique protege 100 ans apres la mort, c'est la duree la
plus longue du monde hispanophone, donc celle qui s'applique a toute la serie.
(L'Espagne protege 80 ans les auteurs morts avant 1987.) Ce n'est pas un avis
juridique, c'est une marge de prudence.

Usage familial, comme le japonais : ni nudite, ni sang, ni guerre. Le filtre
par mots du titre n'est qu'un premier tri : c'est l'oeil de Jacques qui
decide sur les planches.

Source : Wikidata (oeuvres de type « peinture » avec image) puis Commons pour
la licence, lue fichier par fichier (domaine public ou CC0 seulement).

Relancer : python recolter.py   ->  candidats.json + planche-*.jpg
"""
import json, math, os, re, sys, time, urllib.parse, urllib.request
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

ICI = os.path.dirname(os.path.abspath(__file__))
BRUT = os.environ.get("WORTANDO_BRUT", "C:/Users/jacqu/.wortando/espagnol-mosaique-brut")
UA = {"User-Agent": "Wortando-selection/1.0 (jacques.a.grenier@gmail.com)"}
MORT_AVANT = 1926
# Jacques, 14 oct. : « des tableaux a l'horizontale, pas a la verticale ».
RMIN, RMAX = 1.1, 2.0

# (nom cherche dans Wikidata, pays, combien au plus sur les planches)
# Jacques, 14 oct. 2026 : « rien de religieux, impressionnistes seraient le
# mieux ». Le Siecle d'or et Goya sont retires ; impressionnistes, luministes
# et paysagistes de la fin du XIXe, morts avant 1926.
PEINTRES = [
    ("Joaquín Sorolla", "Espagne", 90),
    ("Darío de Regoyos", "Espagne", 25),
    ("Aureliano de Beruete", "Espagne", 25),
    ("Martín Rico", "Espagne", 15),
    ("Ignacio Pinazo Camarlench", "Espagne", 8),
    ("Francisco Iturrino", "Espagne", 6),
    ("Isidre Nonell", "Espagne", 8),
    ("Marià Fortuny", "Espagne", 15),
    ("Raimundo de Madrazo", "Espagne", 6),
    ("Antonio Muñoz Degrain", "Espagne", 15),
    ("José Navarro Llorens", "Espagne", 3),
    ("Joaquim Vayreda", "Espagne", 10),
    ("Modest Urgell", "Espagne", 6),
    ("Juan Martínez Abades", "Espagne", 2),
    ("Emilio Sala Francés", "Espagne", 6),
    ("Baldomer Galofre", "Espagne", 8),
    ("Arturo Michelena", "Venezuela", 10),
    ("Cristóbal Rojas", "Venezuela", 6),
    ("Martín Malharro", "Argentine", 14),
    ("Eduardo Sívori", "Argentine", 8),
    ("Prilidiano Pueyrredón", "Argentine", 12),
    ("Ángel Della Valle", "Argentine", 6),
    ("Francisco Oller", "Porto Rico", 4),
    ("Alberto Valenzuela Llanos", "Chili", 12),
    ("Pedro Lira", "Chili", 4),
    ("Alfredo Valenzuela Puelma", "Chili", 6),
    ("José María Velasco Gómez", "Mexique", 12),
    ("Saturnino Herrán", "Mexique", 4),
    ("José Agustín Arrieta", "Mexique", 4),
    ("Hermenegildo Bustos", "Mexique", 4),
    ("Juan Manuel Blanes", "Uruguay", 8),
    ("Guillermo Collazo", "Cuba", 1),
    ("Francisco Laso", "Pérou", 2),
    ("Epifanio Garay", "Colombie", 1),
    # Plus modernes, toujours morts avant 1926 (ajoutes le 14 oct.).
    ("Ramon Pichot", "Espagne", 15),
    ("Lluïsa Vidal", "Espagne", 10),
    ("Alexandre de Riquer", "Espagne", 10),
    ("Ramón Silva", "Argentine", 12),
    ("Walter de Navazio", "Argentine", 12),
    ("Teófilo Castillo Guas", "Pérou", 10),
    ("Emilio Boggio", "Venezuela", 12),
    ("Carlos María Herrera", "Uruguay", 8),
]

# Wikidata ne repertorie presque rien de certains peintres (un tableau pour
# Pichot, aucun pour Boggio) : on lit aussi ces categories de Commons.
CATEGORIES = {
    "Ramon Pichot": ["Ramon Pichot i Gironès", "Google Art Project works by Ramon Pichot Gironés"],
    "Lluïsa Vidal": ["Lluïsa Vidal"],
    "Alexandre de Riquer": ["Alexandre de Riquer", "Art works by Alexandre de Riquer",
                            "Google Art Project works by Alexandre de Riquer"],
    "Ramón Silva": ["Ramón Silva", "Google Art Project works by Ramón Silva"],
    "Walter de Navazio": ["Walter de Navazio", "Google Art Project works by Walter de Navazio"],
    "Teófilo Castillo Guas": ["Paintings by Teófilo Castillo", "Google Art Project works by Teófilo Castillo"],
    "Emilio Boggio": ["Emilio Boggio"],
    "Carlos María Herrera": ["Paintings by Carlos María Herrera"],
}

# Premier tri seulement (titres en espagnol ou en anglais).
EXCLUS = re.compile(r"desnud|\bnud|naked|nude|bañ|bath|m[aá]rtir|martyr|crucif|muert|death|dead|"
                    r"guerra|\bwar\b|batalla|battle|combate|fusil|ejecuci|execution|sangre|blood|"
                    r"degoll|decapit|cad[aá]ver|corpse|\bsaturno?\b|entierro|burial|"
                    r"tortur|brujas|witch|aquelarre|sabbath|disparate|"
                    # rien de religieux (Jacques, 14 oct.)
                    r"virgen|virgin|madonna|\bcristo\b|christ|jes[uú]s|\bsan\b|\bsanta\b|\bsanto|saint|"
                    r"inmaculad|immaculate|sagrad|holy|[aá]ngel|apóstol|apostle|anunciaci|annunciation|"
                    r"adoraci|adoration|nativi|purísima|dolorosa|piedad|pietà|procesi|monja|nun\b|"
                    r"fraile|friar|monje|monk|iglesia|church|capilla|chapel|misa\b|\bmass\b|oraci[oó]n|prayer|"
                    r"religio|biblic|b[ií]blic|profeta|prophet|ermita", re.I)


# Ecartes a l'oeil sur la premiere planche (14 oct.) : un nu que le titre ne
# dit pas, ou une photo prise avec le cadre.
EXCLUS_ID = {"Q106323210", "Q28663534", "Q133366856",          # nus
             "Q135642613", "Q6106794", "Q121826975",            # cadres
             "Q27954628", "Q27954630", "Q27954536",
             # deuxieme planche, apres le passage aux impressionnistes (retirer.py)
             "Q105444911", "Q105609265", "Q106716143", "Q109942288", "Q109951736",
             "Q114388286", "Q114394460", "Q115650361", "Q130261265", "Q130569539",
             "Q130616872", "Q130616941", "Q136413386", "Q140183331", "Q140450801",
             "Q17636322", "Q27954617", "Q28093517", "Q28808821", "Q54004917",
             # troisieme planche, triee sur l'eclat (retirer.py)
             "Q111179324", "Q113588999", "Q134366916", "Q20816827", "Q27951311",
             "Q28796199", "Q5642417", "Q59828333",
             # quatrieme planche, a l'horizontale (retirer.py)
             "Q105605812", "Q105605814", "Q105606075", "Q108767970", "Q115649107",
             "Q115650310", "Q121237535", "Q130989879", "Q18719637", "Q19162485",
             "Q19913144", "Q20199857", "Q23935855", "Q27950946", "Q27954826",
             "Q28796757", "Q2997939", "Q3207835", "Q71434880", "Q99964776",
             # cinquieme planche, peintres plus modernes (retirer.py) ; les cles
             # « c... » sont des fichiers de Commons sans fiche Wikidata
             "Q27954354", "Q27954790", "c037e9241a27d", "c3c6dc67c3ab9", "c476268ca45d5",
             "c491884e7cc2b", "c76728f13127b", "c93ef160336fc", "c9cd7596e208d",
             "cab688127643e", "ce2126d12f679"}


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
            "language": "es", "format": "json", "limit": 5, "type": "item"})
    for r in d.get("search", []):
        if "paint" in (r.get("description") or "").lower() or "pint" in (r.get("description") or "").lower():
            return r["id"]
    return d["search"][0]["id"] if d.get("search") else None


def sparql(q):
    return get("https://query.wikidata.org/sparql", {"query": q, "format": "json"})["results"]["bindings"]


def mort(q):
    b = sparql("SELECT ?d WHERE { wd:%s wdt:P570 ?d }" % q)
    return int(b[0]["d"]["value"][:4]) if b else None


def tableaux(q):
    b = sparql("""SELECT ?i ?img ?es ?en ?date WHERE {
      ?i wdt:P170 wd:%s; wdt:P31 wd:Q3305213; wdt:P18 ?img.
      # ni art religieux, ni nu, ni histoire, ni mythologie (genre P136) ;
      # ni Jesus, Marie, ange, nudite parmi ce qui est represente (P180).
      FILTER NOT EXISTS { ?i wdt:P136 ?g . VALUES ?g { wd:Q2864737 wd:Q40446 wd:Q742333 wd:Q3374376 } }
      FILTER NOT EXISTS { ?i wdt:P180 ?d . VALUES ?d { wd:Q302 wd:Q345 wd:Q235113 wd:Q10791 } }
      OPTIONAL { ?i rdfs:label ?es FILTER(LANG(?es) = "es") }
      OPTIONAL { ?i rdfs:label ?en FILTER(LANG(?en) = "en") }
      OPTIONAL { ?i wdt:P571 ?date } }""" % q)
    vus, sortie = set(), []
    for x in b:
        fichier = urllib.parse.unquote(x["img"]["value"].rsplit("/", 1)[-1])
        if fichier in vus:
            continue
        vus.add(fichier)
        sortie.append({"wikidata": x["i"]["value"].rsplit("/", 1)[-1], "fichier": fichier,
                       "titre": (x.get("es") or x.get("en") or {}).get("value", ""),
                       "titre_en": (x.get("en") or {}).get("value", ""),
                       "annee": (x.get("date") or {}).get("value", "")[:4]})
    return sortie


def fichiers_categorie(cat):
    """Les fichiers image d'une categorie de Commons, comme des oeuvres sans
    fiche Wikidata : la cle est tiree du nom du fichier, le titre aussi."""
    import hashlib
    d = get("https://commons.wikimedia.org/w/api.php", {"action": "query", "format": "json",
            "list": "categorymembers", "cmtitle": "Category:" + cat, "cmtype": "file", "cmlimit": 500})
    sortie = []
    for x in d.get("query", {}).get("categorymembers", []):
        f = x["title"].split(":", 1)[1]
        if not re.search(r"\.(jpe?g|png|tiff?)$", f, re.I):
            continue
        titre = re.sub(r"\.(jpe?g|png|tiff?)$", "", f, flags=re.I)
        sortie.append({"wikidata": "c" + hashlib.sha1(f.encode("utf-8")).hexdigest()[:12],
                       "fichier": f, "titre": titre, "titre_en": "", "annee": ""})
    return sortie


def infos_commons(fichiers):
    """Licence, taille et vignette de chaque fichier, par lots de 50."""
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
                "l": ii.get("width"), "h": ii.get("height"),
                "vignette": ii.get("thumburl"), "page": ii.get("descriptionurl"),
                "original": ii.get("url")}
    return sortie


def libre(licence):
    l = licence.lower()
    return "public domain" in l or l.startswith("pd") or "cc0" in l or "domaine public" in l


def couleur(im):
    """Indice de couleur de Hasler & Suesstrunk (2003), comme l'allemand."""
    im = im.convert("RGB").resize((300, max(1, round(300 * im.height / im.width))))
    px = list(im.getdata())
    rg = [r - g for r, g, b in px]
    yb = [0.5 * (r + g) - b for r, g, b in px]
    def ms(v):
        m = sum(v) / len(v)
        return m, math.sqrt(sum((x - m) ** 2 for x in v) / len(v))
    mrg, srg = ms(rg); myb, syb = ms(yb)
    return round(math.sqrt(srg ** 2 + syb ** 2) + 0.3 * math.sqrt(mrg ** 2 + myb ** 2), 1)


def eclat(im):
    """Ce que l'oeil appelle « colore » (Jacques, 14 oct. : « pas tres colore
    si on compare aux Allemands ») : une couleur SATUREE et LUMINEUSE.
    L'indice de Hasler & Suesstrunk recompense aussi les bruns contrastes --
    Rojas, Nonell et Madrazo passaient en tete. Moyenne de S x V, sur 0-100,
    mesuree APRES le traitement « vif », comme l'image que l'app montrera."""
    im = vif(im.convert("RGB")).resize((200, max(1, round(200 * im.height / im.width)))).convert("HSV")
    px = list(im.getdata())
    return round(sum(sat * val for _, sat, val in px) / len(px) / 650.25, 1)


def vif(im):
    """Le traitement de l'allemand (branding/mosaique) : autocontrast 1,2/0,8,
    luminosite x1,12, saturation x1,45, contraste x1,10."""
    im = ImageOps.autocontrast(im, cutoff=(1.2, 0.8))
    im = ImageEnhance.Brightness(im).enhance(1.12)
    im = ImageEnhance.Color(im).enhance(1.45)
    return ImageEnhance.Contrast(im).enhance(1.10)


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
    for nom, pays, plafond in PEINTRES:
        q = qid(nom)
        m = mort(q) if q else None
        if not q or not m or m >= MORT_AVANT:
            rapport.append("%-28s ECARTE (wikidata %s, mort %s)" % (nom, q, m))
            continue
        liste = tableaux(q)
        deja = {t["fichier"] for t in liste}
        for cat in CATEGORIES.get(nom, []):
            for t in fichiers_categorie(cat):
                if t["fichier"] not in deja:
                    deja.add(t["fichier"])
                    liste.append(t)
        infos = infos_commons([t["fichier"] for t in liste])
        gardes, vus = [], set()
        for t in liste:
            # Une oeuvre peut avoir plusieurs photos (P18) : une seule par oeuvre.
            if t["wikidata"] in vus or t["wikidata"] in EXCLUS_ID:
                continue
            i = infos.get(t["fichier"])
            if not i or not libre(i["licence"]) or not i["vignette"] or not i["l"]:
                continue
            r = i["l"] / i["h"]
            if not (RMIN <= r <= RMAX):
                continue
            # Les TITRES seulement : le nom de fichier porte celui du peintre, et
            # « Cristobal » ou « Saturnino » tombaient sous « cristo » et « saturn ».
            if EXCLUS.search(t["titre"] + " " + t["titre_en"]):
                continue
            cle = t["wikidata"]
            im = vignette(i["vignette"], cle)
            if im is None:
                continue
            t.update(i, peintre=nom, pays=pays, mort=m, couleur=couleur(im), eclat=eclat(im), cle=cle)
            gardes.append(t)
            vus.add(t["wikidata"])
        gardes.sort(key=lambda t: -t["eclat"])
        tous.extend(gardes[:plafond])
        rapport.append("%-28s %-11s +%d  %3d tableaux, %3d gardes apres filtres, %2d sur les planches"
                       % (nom, pays, m, len(liste), len(gardes), min(plafond, len(gardes))))
        print(rapport[-1])
    tous.sort(key=lambda t: -t["eclat"])
    for n, t in enumerate(tous, 1):
        t["num"] = n
    json.dump(tous, open(os.path.join(ICI, "candidats.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    open(os.path.join(ICI, "recolte.txt"), "w", encoding="utf-8").write("\n".join(rapport) + "\n")
    planches(tous)


def planches(tous):
    try:
        f = ImageFont.truetype("arialbd.ttf", 17)
        p = ImageFont.truetype("arial.ttf", 14)
    except Exception:
        f = p = ImageFont.load_default()
    CEL, COLS, PARPL = 240, 6, 36
    for k in range(0, len(tous), PARPL):
        lot = tous[k:k + PARPL]
        rows = (len(lot) + COLS - 1) // COLS
        im = Image.new("RGB", (COLS * CEL, rows * (CEL + 24)), "white")
        d = ImageDraw.Draw(im)
        for i, t in enumerate(lot):
            v = vif(Image.open(os.path.join(BRUT, "v-" + t["cle"] + ".jpg")).convert("RGB"))
            v.thumbnail((CEL - 12, CEL - 44))
            x, y = (i % COLS) * CEL, (i // COLS) * (CEL + 24)
            im.paste(v, (x + (CEL - v.width) // 2, y + 26))
            d.text((x + 6, y + 4), "%d" % t["num"], fill="black", font=f)
            d.text((x + 52, y + 6), t["peintre"][:24], fill=(90, 90, 90), font=p)
            d.text((x + 6, y + CEL - 14), t["pays"], fill=(150, 90, 20), font=p)
        im.save(os.path.join(ICI, "planche-%d.jpg" % (k // PARPL + 1)), quality=82)


if __name__ == "__main__":
    main()
