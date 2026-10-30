"""Les candidats de la mosaique PORTUGAISE (29 oct. 2026), recoltes pour que
Jacques choisisse et ordonne sur une page cliquable, comme l'anglais
(anglais/mosaique/) et l'espagnol (espanol/mosaique/).

Decide par Jacques le 29 oct. 2026 : une version de Wortando pour apprendre le
portugais du Portugal. Chaque langue a sa collection : ici, des peintres
PORTUGAIS (Malhoa, Columbano, Silva Porto, Pousao, Marques de Oliveira, Sousa
Pinto, Aurelia de Souza, Amadeo de Souza-Cardoso...). Rien n'est branche dans
l'app avant son choix.

REGLE DE DROIT, comme l'espagnol : PEINTRE MORT AVANT 1926 (le Mexique protege
100 ans apres la mort ; l'app se diffuse partout). Ceux qui sont morts entre
1926 et 1955 sont libres en Europe (70 ans) : ils sont recoltes A PART
(groupe « europe », numeros E1, E2...), pour que Jacques decide -- Malhoa
(1933), Columbano (1929), Marques de Oliveira (1927), Sousa Pinto (1939),
Carlos Reis, Antonio Carneiro, Veloso Salgado... Pour eux, oeuvre d'avant 1931
seulement (le domaine public americain), comme l'anglais. Ce n'est pas un avis
juridique, c'est une marge de prudence.

Comme l'espagnol et l'anglais (decisions de Jacques) : a l'horizontale, rien de
religieux, ni nu, ni sang, ni guerre ; les plus colores d'abord (eclat mesure
sur l'image brute, avant le traitement « vif »). Licence lue fichier par
fichier sur Commons : domaine public ou CC0 seulement. En bonne definition :
au moins LARGEUR_MIN pixels de large ; sous LARGEUR_BONNE (la largeur
des images de l'app), la page le signale (« petite »).

Relancer : python portugais/mosaique/recolter.py  ->  candidats.json + recolte.txt
Les vignettes restent hors de OneDrive (C:/Users/jacqu/.wortando/portugais-mosaique-brut).
Puis : python portugais/mosaique/construire_choix.py <dossier>  ->  la page de choix.
"""
import json, os, re, sys, time, urllib.parse, urllib.request
from PIL import Image, ImageEnhance, ImageOps

ICI = os.path.dirname(os.path.abspath(__file__))
BRUT = os.environ.get("WORTANDO_BRUT", "C:/Users/jacqu/.wortando/portugais-mosaique-brut")
UA = {"User-Agent": "Wortando-selection/1.0 (jacques.a.grenier@gmail.com)"}
LIBRE_AVANT = 1926      # libre partout (regle de l'espagnol)
EUROPE_AVANT = 1956     # libre en Europe : a part, Jacques decide
OEUVRE_AVANT = 1931     # pour le groupe « europe » seulement
RMIN, RMAX = 1.1, 2.1
LARGEUR_MIN = 600
LARGEUR_BONNE = 900

# (nom, identifiant Wikidata, combien au plus avant le tri commun)
PEINTRES = [
    # morts avant 1926
    ("Silva Porto", "Q610761", 30),
    ("Henrique Pousão", "Q3847723", 15),
    ("Aurélia de Souza", "Q3324919", 12),
    ("Amadeo de Souza-Cardoso", "Q451771", 25),
    ("Alfredo Keil", "Q1437304", 15),
    ("António Ramalho", "Q10357323", 10),
    ("Miguel Ângelo Lupi", "Q3543874", 6),
    ("Tomás da Anunciação", "Q7820534", 10),
    ("João Cristino da Silva", "Q10311369", 10),
    ("Francisco Metrass", "Q1441879", 3),
    ("Manuel Henrique Pinto", "Q10294815", 8),
    ("José Rodrigues", "Q2837500", 6),
    ("Leonel Marques Pereira", "Q10317380", 2),
    ("Francisco José Resende", "Q10284861", 10),
    ("Constantino Fernandes", "Q52156250", 3),
    ("Santa-Rita Pintor", "Q2223220", 2),
    ("Carlos Ier de Portugal", "Q158874", 8),
    ("Domingos Sequeira", "Q1234389", 2),   # presque tout religieux ou allegorique
    ("Josefa de Óbidos", "Q269338", 2),     # les natures mortes seulement
    # ajoutes apres la premiere recolte (64 tableaux seulement avant 1926)
    ("Luís Tomasini", "Q52154937", 6),
    ("João Pedroso", "Q10312040", 4),
    ("José Ferreira Chaves", "Q10309390", 6),
    ("António Manuel da Fonseca", "Q12345227", 4),
    ("Vieira Portuense", "Q1617507", 4),
    ("Fernando II de Portugal", "Q60721", 4),
    ("Alfredo de Andrade", "Q3611528", 2),
    # morts entre 1926 et 1955 : groupe « europe »
    ("José Malhoa", "Q720979", 35),
    ("Columbano Bordalo Pinheiro", "Q1112288", 15),
    ("Marques de Oliveira", "Q303936", 15),
    ("José Júlio de Souza Pinto", "Q3186346", 18),
    ("Artur Loureiro", "Q714598", 10),
    ("João Vaz", "Q10312299", 15),
    ("Carlos Reis", "Q549850", 20),
    ("António Carneiro", "Q3847713", 12),
    ("Ernesto Condeixa", "Q10274053", 10),
    ("José Veloso Salgado", "Q3555368", 12),
    ("Alfredo Roque Gameiro", "Q10364494", 3),
    ("Luciano Freire", "Q10320300", 3),
    ("Adriano de Sousa Lopes", "Q12344672", 10),
]

# Wikidata ne recense qu'une partie des tableaux (Malhoa : 102 fiches, 173
# fichiers dans sa categorie de Commons) : on lit aussi ces categories, comme
# l'espagnol. Une cle « c... » est un fichier de Commons sans fiche Wikidata ;
# son titre et son annee viennent de la fiche du fichier (ObjectName, date).
CATEGORIES = {
    "Silva Porto": ["Paintings by Silva Porto"],
    "Henrique Pousão": ["Paintings by Henrique Pousão"],
    "Aurélia de Souza": ["Paintings by Aurélia de Sousa"],
    "Amadeo de Souza-Cardoso": ["Paintings by Amadeo de Souza-Cardoso"],
    "Alfredo Keil": ["Paintings by Alfredo Keil"],
    "António Ramalho": ["Paintings by António Ramalho Júnior"],
    "Miguel Ângelo Lupi": ["Paintings by Miguel Ângelo Lupi"],
    "João Cristino da Silva": ["Paintings by João Cristino da Silva"],
    "Manuel Henrique Pinto": ["Paintings by Manuel Henrique Pinto"],
    "Carlos Ier de Portugal": ["Paintings by Carlos I of Portugal"],
    "José Malhoa": ["Paintings by José Malhoa"],
    "Columbano Bordalo Pinheiro": ["Paintings by Columbano Bordalo Pinheiro"],
    "Marques de Oliveira": ["Paintings by João Marques de Oliveira"],
    "José Júlio de Souza Pinto": ["Paintings by José Júlio de Souza Pinto"],
    "Artur Loureiro": ["Paintings by Artur Loureiro"],
    "Carlos Reis": ["Paintings by Carlos Reis"],
    "António Carneiro": ["Paintings by António Carneiro"],
    "Ernesto Condeixa": ["Paintings by Ernesto Condeixa"],
    "José Veloso Salgado": ["Paintings by Veloso Salgado"],
}

# Premier tri seulement (titres en portugais, en francais ou en anglais) : c'est
# l'oeil de Jacques qui decide sur la page.
EXCLUS = re.compile(r"\bnua?s?\b|\bnu\b|desnud|nude|naked|banho|banhista|bath|baigneu|"
                    r"m[aá]rtir|martyr|crucif|\bmort[eo]s?\b|morte|death|dead|"
                    r"guerra|\bwar\b|batalha|battle|bataille|combate|sangue|blood|"
                    r"cad[aá]ver|corpse|enterro|funeral|fun[eé]rai|luto|"
                    # rien de religieux (Jacques, 14 oct.) ; mais « Sao », « Santa »,
                    # « Saint » restent permis : ce sont d'abord des noms de lieux
                    # (Sao Martinho do Porto, Santa Luzia), et l'oeil tranche.
                    r"virgem|virgin|vierge|madonna|nossa senhora|\bcristo\b|christ|jesus|j[eé]sus|"
                    r"imaculad|immaculate|sagrad|holy|"
                    r"\banjos?\b|angel|ange|ap[oó]stol|apostle|anuncia|annunciation|adora[cç]|"
                    r"nativi|natividade|presépio|piedade|piet[aà]|prociss|freira|\bnun\b|"
                    r"frade|friar|monge|monk|igreja|church|[eé]glise|capela|chapel|chapelle|"
                    r"\bmissa\b|\bmass\b|ora[cç][aã]o|prayer|pri[eè]re|religi|b[ií]blic|profeta|prophet|"
                    r"ermida|calv[aá]rio|calvary|via sacra|ressurrei|resurrection|"
                    r"estudo para|study for|[eé]tude pour|esbo[cç]o|sketch|desenho|drawing", re.I)

# Ecartes a l'oeil sur la premiere recolte (29 oct.) : ce que le titre ne disait
# pas. Les numeros sont ceux de cette premiere recolte, avant ces retraits.
EXCLUS_ID = {
    'c23876ee16dcb',   # 9     Carlos Ier : dessin
    'Q59692539',       # 13    Sequeira : religieux (saint Jean-Baptiste)
    'Q99415336',       # 14    Ferreira Chaves : dessin sepia sur papier
    'c927063925819',   # 18    Silva Porto : photo avec le cadre
    'cbd03a7435c14',   # 32    Silva Porto : photo avec le cadre (doublon de Madrugada)
    'Q59647326',       # 34    Josefa de Obidos : photo avec le cadre
    'c7e21d8b41376',   # 35    Silva Porto : dos de la toile
    'c2ea147d26c4c',   # 36    Carlos Ier : image abimee
    'Q59692262',       # 39    Sequeira : religieux (le Christ)
    'Q28680950',       # 47    Vieira Portuense : adoubement, armes
    'Q59647273',       # 51    Josefa de Obidos : photo avec le cadre
    'Q18925521',       # 53    Sequeira : allegorie aux putti nus
    'Q63087595',       # 56    Sequeira : allegorie aux nus
    'c331891548a9b',   # 64    Pousao : ovale sur fond noir
    'c5cf356665fa4',   # 69    nu (de Columbano, range chez Silva Porto)
    'Q60388499',       # 76    Souza-Cardoso : ovale
    'Q59647353',       # 81    Josefa de Obidos : photo avec le cadre
    'Q59647391',       # 83    Josefa de Obidos : photo avec le cadre
    'c827df67301ad',   # 92    photo d'une salle d'exposition (Armory Show)
    'c12f9614a9f08',   # 7     Silva Porto : doublon de Madrugada
    'cc2b045a77f55',   # 74    Silva Porto : doublon de Charneca de Belas
    'c071daa0b6974',   # E1    Columbano : nus
    'ce6557dd0bb91',   # E8    Malhoa : putti nus
    'cfca6287223c7',   # E13   Malhoa : doublon de Uma boa compra
    'c3a7dcf7b7992',   # E18   Malhoa : doublon de Cocegas (detail)
    'c6c3442343129',   # E46   Malhoa : doublon de Cocegas
    'cba3d445417b3',   # E22   Malhoa : esquisse, la signature au centre
    'c83aae06c87ff',   # E23   Malhoa : photo avec le cadre (Os Bebados)
    'cb67a52912773',   # E31   Malhoa : photo avec le cadre
    'Q28680984',       # E35   Malhoa : religieux (As Promessas)
    'Q28680942',       # E37   Souza Pinto : deuil, naufrage
    'Q28680948',       # E39   Columbano : nus
    'c736d2e2bf9a3',   # E43   Veloso Salgado : doublon de Geres (photo de salle)
    'Q10338740',       # E49   Malhoa : nu
    'Q25444545',       # E50   Columbano : meurtre d'Ines de Castro
    'c1276bb5adf69',   # E53   Malhoa : medaillon rond
    'Q59393441',       # E61   Sousa Lopes : photo avec le mur
    'c62001e04ae64',   # E64   Veloso Salgado : gravure
    'Q28680990',       # E67   Malhoa : nu
    'Q67201161',       # E68   Loureiro : doublon de Ponte de Lima
    'Q98878763',       # E69   Columbano : religieux (cardinal)
    'Q98925654',       # E75   Columbano : crane
    'Q28680976',       # E82   Carneiro : nus
    'Q98971964',       # E90   Carlos Reis : religieux (bapteme)
    'Q23011972',       # E94   Malhoa : doublon de Regresso do campo
    'Q98881215',       # E98   Columbano : portrait militaire
    'c841652cdf657',   # E99   Columbano : dessin au trait
    'Q59377180',       # E101  Carneiro : photo avec le cadre
    # deuxieme passage (numeros de la deuxieme recolte)
    'Q59695115',       # 47    Sequeira : allegorie aux anges nus
    'Q28680887',       # 71    Sequeira : Junot, ange, armee francaise
    'Q59656595',       # 74    Josefa de Obidos : religieux (ange)
    'Q18748965',       # 75    Josefa de Obidos : religieux (Agnus Dei)
    'Q10260541',       # 78    Josefa de Obidos : religieux (Agnus Dei)
    'cb52ffe73dd0e',   # E85   Malhoa : detail de la signature
    'c83e8a2e390bd',   # E87   Veloso Salgado : gravure
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


def sparql(q):
    return get("https://query.wikidata.org/sparql", {"query": q, "format": "json"})["results"]["bindings"]


def mort(q):
    b = sparql("SELECT ?d WHERE { wd:%s wdt:P570 ?d }" % q)
    return int(b[0]["d"]["value"][:4]) if b else None


def tableaux(q):
    b = sparql("""SELECT ?i ?img ?pt ?fr ?en ?date ?collLabel WHERE {
      ?i wdt:P170 wd:%s; wdt:P31 wd:Q3305213; wdt:P18 ?img.
      # ni art religieux, ni nu, ni histoire, ni mythologie (genre P136) ;
      # ni Jesus, Marie, ange, nudite parmi ce qui est represente (P180).
      FILTER NOT EXISTS { ?i wdt:P136 ?g . VALUES ?g { wd:Q2864737 wd:Q40446 wd:Q742333 wd:Q3374376 } }
      FILTER NOT EXISTS { ?i wdt:P180 ?d . VALUES ?d { wd:Q302 wd:Q345 wd:Q235113 wd:Q10791 } }
      OPTIONAL { ?i rdfs:label ?pt FILTER(LANG(?pt) = "pt") }
      OPTIONAL { ?i rdfs:label ?fr FILTER(LANG(?fr) = "fr") }
      OPTIONAL { ?i rdfs:label ?en FILTER(LANG(?en) = "en") }
      OPTIONAL { ?i wdt:P571 ?date }
      OPTIONAL { ?i wdt:P195 ?coll . ?coll rdfs:label ?collLabel FILTER(LANG(?collLabel) = "pt") } }""" % q)
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
             "titre": (x.get("pt") or {}).get("value", ""), "titre_fr": (x.get("fr") or {}).get("value", ""),
             "titre_en": (x.get("en") or {}).get("value", ""),
             "annee": (x.get("date") or {}).get("value", "")[:4], "collection": [coll] if coll else []}
        vus[cle] = t
        sortie.append(t)
    return sortie


def fichiers_categorie(cat):
    """Les fichiers image d'une categorie de Commons (sans ses sous-categories,
    qui melangent dessins, details et photos de salle)."""
    import hashlib
    d = get("https://commons.wikimedia.org/w/api.php", {"action": "query", "format": "json",
            "list": "categorymembers", "cmtitle": "Category:" + cat, "cmtype": "file", "cmlimit": 500})
    sortie = []
    for x in d.get("query", {}).get("categorymembers", []):
        f = x["title"].split(":", 1)[1]
        if not re.search(r"\.(jpe?g|png|tiff?)$", f, re.I):
            continue
        sortie.append({"wikidata": "c" + hashlib.sha1(f.encode("utf-8")).hexdigest()[:12],
                       "fichier": f, "titre": "", "titre_fr": "", "titre_en": "", "annee": "",
                       "collection": [], "de_categorie": True})
    return sortie


def texte_brut(v):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", v or "")).strip()


# Les noms courts sous lesquels Commons signe les fichiers (« - José Malhoa »,
# « (Columbano) », « - D. Carlos ») : on les retire du titre.
SIGNATURES = r"Malh[oô]a|Columbano|Bordalo|Carlos|Keil|Pous[aã]o|Salgado|Oliveira|Loureiro|Condeixa|" \
             r"Ernesto|Tomazini|Tomasini|Souza|Sousa|Porto|Carneiro|Reis|Vaz|Cardoso"


def titre_propre(brut):
    """Le titre portugais d'une fiche Commons. ObjectName melange les langues
    (« Watermill label QS:Len,... label QS:Lpt,"Azenha, margens do Ave" ») et
    les noms de fichiers portent la signature et l'annee. Rend (titre, annee)."""
    t = brut
    m = re.search(r'(?:label QS:Lpt,|pt:)"([^"]+)"', t)
    if m:
        t = m.group(1)
    t = re.split(r"\s+(?:label|title) QS:", t)[0]
    t = re.sub(r"^(?:Portuguese|French|English|Português|Français):\s*", "", t)
    annee = ""
    a = re.search(r"\((1[6-9]\d\d)\)|,\s*(1[6-9]\d\d)\b", t)
    if a:
        annee = a.group(1) or a.group(2)
    # « - Marques de Oliveira (CP-MA, Inv. 84.794) », « , José Malhôa », « - D. Carlos I » :
    # tout ce qui suit la signature part avec elle.
    t = re.sub(r"\s*[-,–]\s+(?:D\.\s*)?(?:(?:[A-ZÀ-Ý][\wÀ-ÿ]*|de|da|do|dos)\s+){0,4}?(?:%s)\b.*$" % SIGNATURES, "", t)
    t = re.sub(r"\s*\((?:[^()]*?(?:%s)[^()]*)\)\s*$" % SIGNATURES, "", t)
    t = re.sub(r"\s*\((1[6-9]\d\d)\)|,\s*1[6-9]\d\d\b", "", t)
    return t.strip(" -,"), annee


def infos_commons(fichiers):
    sortie = {}
    for k in range(0, len(fichiers), 50):
        lot = fichiers[k:k + 50]
        d = get("https://commons.wikimedia.org/w/api.php", {"action": "query", "format": "json",
                "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": 400,
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
                "nom_objet": texte_brut(em.get("ObjectName", {}).get("value", ""))[:120],
                "date_fichier": texte_brut(em.get("DateTimeOriginal", {}).get("value", ""))[:80],
                "l": ii.get("width"), "h": ii.get("height"),
                "vignette": ii.get("thumburl"), "page": ii.get("descriptionurl"),
                "original": ii.get("url")}
    return sortie


def libre(licence):
    l = licence.lower()
    return "public domain" in l or l.startswith("pd") or "cc0" in l


def vif(im):
    """Le traitement de l'allemand (branding/mosaique), comme l'espagnol et l'anglais."""
    im = ImageOps.autocontrast(im, cutoff=(1.2, 0.8))
    im = ImageEnhance.Brightness(im).enhance(1.12)
    im = ImageEnhance.Color(im).enhance(1.45)
    return ImageEnhance.Contrast(im).enhance(1.10)


def eclat_brut(im):
    """Saturation x luminosite moyenne sur l'image telle qu'elle est (sans « vif »),
    et sa luminosite : la mesure de la recolte « couleur » de l'anglais."""
    im = im.convert("RGB").resize((200, max(1, round(200 * im.height / im.width)))).convert("HSV")
    px = list(im.getdata())
    return (round(sum(sat * val for _, sat, val in px) / len(px) / 650.25, 1),
            round(sum(val for _, _, val in px) / len(px) / 2.55, 1))


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


def main(peintres=PEINTRES, categories=CATEGORIES, exclus_id=EXCLUS_ID, exclus=EXCLUS,
         prefixes=(("libre", ""), ("europe", "E")), sortie="candidats.json", recolte="recolte.txt"):
    """Les arguments servent a la recolte bresilienne (recolter_bresil.py), qui
    passe ses peintres, ses prefixes (B, BE) et ses fichiers de sortie."""
    os.makedirs(BRUT, exist_ok=True)
    tous, rapport = [], []
    for nom, q, plafond in peintres:
        m = mort(q)
        if not m or m >= EUROPE_AVANT:
            rapport.append("%-28s ECARTE (wikidata %s, mort %s)" % (nom, q, m))
            print(rapport[-1])
            continue
        groupe = "libre" if m < LIBRE_AVANT else "europe"
        liste = tableaux(q)
        deja = {t["fichier"] for t in liste}
        for cat in categories.get(nom, []):
            for t in fichiers_categorie(cat):
                if t["fichier"] not in deja:
                    deja.add(t["fichier"])
                    liste.append(t)
        infos = infos_commons([t["fichier"] for t in liste])
        gardes, raisons = [], {}
        for t in liste:
            def non(r):
                raisons[r] = raisons.get(r, 0) + 1
            if t["wikidata"] in exclus_id:
                non("oeil"); continue
            i = infos.get(t["fichier"])
            if t.get("de_categorie") and i:
                # Titre et annee tires de la fiche du fichier ; a defaut, du nom du fichier.
                titre, annee = titre_propre(i["nom_objet"] or re.sub(r"\.(jpe?g|png|tiff?)$", "", t["fichier"], flags=re.I))
                t["titre"] = titre
                a = re.search(r"\b(1[6-9]\d\d)\b", i["date_fichier"])
                t["annee"] = a.group(1) if a else annee
            an = int(t["annee"]) if t["annee"][:4].isdigit() else None
            if groupe == "europe" and ((an is None and m >= OEUVRE_AVANT) or (an is not None and an >= OEUVRE_AVANT)):
                non("date"); continue
            if not i or not libre(i["licence"]) or not i["vignette"] or not i["l"]:
                non("licence"); continue
            if not (RMIN <= i["l"] / i["h"] <= RMAX):
                non("hauteur"); continue
            if i["l"] < LARGEUR_MIN:
                non("petite"); continue
            titres = " ".join([t["titre"], t["titre_fr"], t["titre_en"]])
            if exclus.search(titres) or not titres.strip():
                non("sujet"); continue
            im = vignette(i["vignette"], t["wikidata"])
            if im is None:
                non("telechargement"); continue
            brut, lum = eclat_brut(im)
            t.update(i, peintre=nom, wikidata_peintre=q, mort=m, groupe=groupe,
                     eclat_brut=brut, luminosite=lum, cle=t["wikidata"],
                     petite=i["l"] < LARGEUR_BONNE)
            t["score"] = round(brut + 0.25 * lum, 1)
            gardes.append(t)
        gardes.sort(key=lambda t: -t["score"])
        tous.extend(gardes[:plafond])
        rapport.append("%-28s %-10s +%d %-6s %3d tableaux, %3d gardes, %2d retenus  (ecartes : %s)"
                       % (nom, q, m, groupe, len(liste), len(gardes), min(plafond, len(gardes)),
                          ", ".join("%s %d" % kv for kv in sorted(raisons.items())) or "aucun"))
        print(rapport[-1])
    for g, pref in prefixes:
        lot = sorted([t for t in tous if t["groupe"] == g], key=lambda t: -t["score"])
        for n, t in enumerate(lot, 1):
            t["num"] = pref + str(n)
        par = {}
        for t in lot:
            par[t["peintre"]] = par.get(t["peintre"], 0) + 1
        rapport.append("\nGroupe %s (%d) : %s" % (g, len(lot), ", ".join(
            "%s %d" % (p, k) for p, k in sorted(par.items(), key=lambda x: -x[1]))))
        print(rapport[-1])
    tous.sort(key=lambda t: (t["groupe"] != "libre", -t["score"]))
    json.dump(tous, open(os.path.join(ICI, sortie), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    open(os.path.join(ICI, recolte), "w", encoding="utf-8").write("\n".join(rapport) + "\n")


if __name__ == "__main__":
    main()
