# -*- coding: utf-8 -*-
"""La mosaique JAPONAISE de l'app : 42 paravents a fond d'or et 18 rouleaux
d'Ito Jakuchu, choisis par Jacques le 26 oct. 2026.

    python japonais/mosaique/construire_app.py   ->  app/img/j01.jpg ... + app/mosaiques.json

Sources : candidats2.json (seconde recolte du 25 oct. : Cleveland Museum of Art
en CC0, Wikimedia Commons en domaine public ou CC0). Les originaux haute
definition restent hors de OneDrive (C:/Users/jacqu/.wortando/japonais-mosaique-hd).

Ce qui differe de l'allemand et de l'espagnol :
- PAS DE RECADRAGE DES PANORAMAS. L'espagnol coupait au-dela de 1,6 de large ;
  un paravent fait 2 a 3,4, et c'est justement le format du bandeau 3/1 de
  l'accueil. Les carreaux restent carres : le moteur fixe les colonnes et
  adapte les rangees.
- LES ROULEAUX DE JAKUCHU SANS LEUR SOIE, et une hauteur de cadrage par
  rouleau (« centre », 0 = haut, 1 = bas) : le bandeau de l'accueil n'en montre
  qu'une tranche, posee a l'oeil sur le sujet (option B, choisie par Jacques).
- Titres en francais ET en anglais (titre, titre_en) : les deux langues
  d'interface du japonais.

Traitement « vif » identique aux deux autres collections : autocontrast 1,2/0,8,
luminosite x1,12, saturation x1,45, contraste x1,10 ; 900 px de large, qualite 72.
"""
import json, os, sys, time, urllib.parse, urllib.request
from PIL import Image, ImageEnhance, ImageOps
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ICI, "app")
HD = "C:/Users/jacqu/.wortando/japonais-mosaique-hd"
WEB = "C:/Users/jacqu/.wortando/japonais-mosaique-web"
UA = {"User-Agent": "Wortando-mosaique/1.0 (jacques.a.grenier@gmail.com)"}
Image.MAX_IMAGE_PIXELS = None

# L'ordre de la mosaique (p01 -> p60). Iris de Korin en ouverture, Fujin-Raijin
# de Sotatsu en cloture, un Jakuchu tous les trois ou quatre tableaux.
ORDRE = [1237, 1064, 1302, 1092, 1333, 1294, 1254, 1039, 1022, 1279, 1099, 1264,
         1286, 1003, 1089, 1298, 1038, 1343, 1280, 1100, 1008, 1281, 1061, 1330,
         1018, 1288, 1132, 1031, 1285, 1147, 1002, 1293, 1233, 1332, 1284, 1049,
         1005, 1030, 1301, 1059, 1069, 1283, 1344, 1146, 1292, 1050, 1034, 1303,
         1043, 1004, 1299, 1128, 1023, 1042, 1296, 1247, 1027, 1297, 1058, 1274]

# Le cadrage des rouleaux (planche tranches-jakuchu.jpg, revue avec Jacques).
CENTRE = {1302: 0.42, 1294: 0.30, 1279: 0.16, 1286: 0.38, 1298: 0.33, 1280: 0.30,
          1281: 0.35, 1288: 0.42, 1285: 0.35, 1293: 0.55, 1284: 0.25, 1301: 0.42,
          1283: 0.68, 1292: 0.84, 1303: 0.30, 1299: 0.55, 1296: 0.49, 1297: 0.32}

KORIN, SOTATSU, JAKUCHU = "Ogata Kōrin", "Tawaraya Sōtatsu", "Itō Jakuchū"
ANONYME = "Anonyme"
# num : (peintre, titre fr, titre en, annee affichee « Peint en ... » -- vide
# quand le musee ne donne qu'un siecle : une annee absente vaut mieux qu'une fausse)
FICHES = {
    1237: (KORIN, "Iris (paravent de droite)", "Irises (right screen)", ""),
    1064: ("Watanabe Shikō", "Iris", "Irises", ""),
    1092: (ANONYME, "Vues célèbres d'Ōmi", "Famous Views of Ōmi", ""),
    1333: ("Hasegawa Tōhaku", "Érable (détail)", "Maple (detail)", "1593"),
    1254: (KORIN, "Pruniers rouges et blancs", "Red and White Plum Blossoms", ""),
    1039: ("Shibata Zeshin", "Le palais de Nagisa, d'après les Contes d'Ise", "Nagisa Palace, from The Tales of Ise", ""),
    1022: (KORIN, "Chrysanthèmes au bord d'un ruisseau", "Chrysanthemums by a Stream", ""),
    1099: ("Tosa Mitsuyoshi", "Phénix et paulownias", "Phoenixes and Paulownia", ""),
    1264: (KORIN, "Le dieu du vent et le dieu du tonnerre", "The Wind God and the Thunder God", ""),
    1003: ("Watanabe Shikō", "Fleurs et arbres des quatre saisons (paravent de gauche)", "Flowers and Trees of the Four Seasons (left screen)", ""),
    1089: ("Maruyama Ōkyo", "Héron sur une branche de saule", "Heron on a Willow Branch", ""),
    1038: ("Fukae Roshū", "Le chemin aux lierres", "Ivy Lane", ""),
    1343: ("Kanō Takanobu", "Scènes dans et autour de Kyoto (attribué)", "Scenes in and around Kyoto (attributed)", ""),
    1100: ("Tosa Mitsuyoshi", "Paons et bambous", "Peacocks and Bamboo", ""),
    1008: ("Sakai Hōitsu", "Paulownias et chrysanthèmes", "Paulownias and Chrysanthemums", ""),
    1061: ("École Tosa", "Scènes du Dit du Genji", "Scenes from The Tale of Genji", ""),
    1330: ("Kanō Eitoku", "Cyprès (attribué)", "Cypress Trees (attributed)", "1590"),
    1018: ("Tatebayashi Kagei", "Les Trente-Six Immortels de la poésie", "The Thirty-Six Immortal Poets", ""),
    1132: ("Yamaguchi Sekkei", "Lions et tigres, pivoines et bambous", "Lions and Tigers among Peonies and Bamboo", "1668"),
    1031: ("Kanō Mitsunobu", "Fleurs et oiseaux", "Birds and Flowers", ""),
    1147: ("Shikibu Terutada", "Pan Lang (éventail)", "Pan Lang (fan)", ""),
    1002: (ANONYME, "L'écurie", "Horse Stable", ""),
    1233: (KORIN, "Iris à Yatsuhashi (paravent de droite)", "Irises at Yatsuhashi (right screen)", ""),
    1332: ("Kanō Hideyori", "Promeneurs sous les érables", "Maple Viewers", ""),
    1049: ("Tosa Mitsuyoshi", "Paons et phénix", "Peafowl and Phoenixes", ""),
    1005: (ANONYME, "L'arrivée des Barbares du Sud", "Arrival of the Southern Barbarians", ""),
    1030: ("Kanō Shōei", "Fleurs et oiseaux", "Birds and Flowers", ""),
    1059: (ANONYME, "Scènes du Dit du Genji", "Scenes from The Tale of Genji", ""),
    1069: ("Kitagawa Sōsetsu", "Fleurs et herbes", "Flowers and Grasses", ""),
    1344: ("Iwasa Matabei", "Scènes dans et autour de Kyoto (paravents Funaki)", "Scenes in and around Kyoto (Funaki screens)", ""),
    1146: ("Shikibu Terutada", "Canard en vol (éventail)", "Duck in Flight (fan)", ""),
    1050: ("Kō Sūkoku", "Travaux des champs au printemps et en automne", "Spring and Autumn Farming", ""),
    1034: ("Shibata Zeshin", "Les personnages des peintures d'Ōtsu", "Gathering of Ōtsu-e Subjects", ""),
    1043: (ANONYME, "Scènes de fête", "Festival Scenes", ""),
    1004: ("Watanabe Shikō", "Fleurs et arbres des quatre saisons (paravent de droite)", "Flowers and Trees of the Four Seasons (right screen)", ""),
    1128: ("Kanō Naonobu", "Paysage d'hiver, pruniers et faisans", "Winter Scene with Plum Trees and Pheasants", ""),
    1023: (ANONYME, "Course de chevaux au sanctuaire de Kamo", "Horse Race at the Kamo Shrine", ""),
    1042: (ANONYME, "Scènes des Contes d'Ise", "Scenes from The Tales of Ise", ""),
    1247: (KORIN, "Iris à Yatsuhashi (paravent de gauche)", "Irises at Yatsuhashi (left screen)", ""),
    1027: ("Matsumura Goshun", "Scènes des Heures oisives", "Scenes from Essays in Idleness", ""),
    1058: (SOTATSU, "Le dieu du tonnerre", "The God of Thunder", ""),
    1274: (SOTATSU, "Le dieu du vent et le dieu du tonnerre", "The Wind God and the Thunder God", ""),
    # Le Royaume colore des etres vivants (Doshoku sai-e), 30 rouleaux, 1757-1766.
    1302: (JAKUCHU, "Érable et petits oiseaux", "Maple Tree and Small Birds", ""),
    1294: (JAKUCHU, "Pivoines et petits oiseaux", "Peonies and Small Birds", ""),
    1279: (JAKUCHU, "Vieux pin et paon", "Old Pine Tree and Peacock", ""),
    1286: (JAKUCHU, "Coq noir et nandina", "Black Rooster and Nandina", ""),
    1298: (JAKUCHU, "Roses et petit oiseau", "Roses and Small Bird", ""),
    1280: (JAKUCHU, "Pruniers en fleurs et grues", "Plum Blossoms and Cranes", ""),
    1281: (JAKUCHU, "L'étang et les insectes", "Pond and Insects", ""),
    1288: (JAKUCHU, "Cacatoès dans un vieux pin", "Cockatoos in an Old Pine", ""),
    1285: (JAKUCHU, "Oiseaux sur un prunier en fleurs", "Birds on a Blossoming Plum", ""),
    1293: (JAKUCHU, "Canards mandarins sous la neige", "Mandarin Ducks in the Snow", "1759"),
    1284: (JAKUCHU, "Oiseaux sur un pêcher en fleurs", "Birds on a Blossoming Peach Tree", ""),
    1301: (JAKUCHU, "Oie blanche et roseaux", "White Goose and Reeds", ""),
    1283: (JAKUCHU, "Ketmies et volailles", "Rose Mallows and Fowl", ""),
    1292: (JAKUCHU, "Pivoines et papillons", "Peonies and Butterflies", ""),
    1303: (JAKUCHU, "Les coqs", "Group of Roosters", ""),
    1299: (JAKUCHU, "Coquillages", "Shells", ""),
    1296: (JAKUCHU, "Coq et tournesols", "Rooster and Sunflowers", "1759"),
    1297: (JAKUCHU, "Coq et poule", "Rooster and Hen", ""),
}
# Sotatsu : mort vers 1640, date incertaine -- pas de croix plutot qu une fausse precision.
MORT = {KORIN: 1716, JAKUCHU: 1800, "Watanabe Shikō": 1755, "Hasegawa Tōhaku": 1610,
        "Shibata Zeshin": 1891, "Tosa Mitsuyoshi": 1613, "Maruyama Ōkyo": 1795, "Fukae Roshū": 1757,
        "Kanō Takanobu": 1618, "Sakai Hōitsu": 1828, "Kanō Eitoku": 1590, "Yamaguchi Sekkei": 1732,
        "Kanō Mitsunobu": 1608, "Kanō Shōei": 1592, "Iwasa Matabei": 1650, "Kō Sūkoku": 1804,
        "Matsumura Goshun": 1811, "Kanō Naonobu": 1650}


def vif(im):
    im = ImageOps.autocontrast(im, cutoff=(1.2, 0.8))
    im = ImageEnhance.Brightness(im).enhance(1.12)
    im = ImageEnhance.Color(im).enhance(1.45)
    return ImageEnhance.Contrast(im).enhance(1.10)


def get_json(url):
    for essai in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        except Exception:
            time.sleep(3 * (essai + 1))
    raise RuntimeError("reponse impossible : " + url)


def url_hd(c):
    """Commons : une vignette de 1800 px (certains originaux depassent 100 Mo).
    Cleveland : l'image « print » de l'API Open Access."""
    u = c["img_full"]
    if "upload.wikimedia.org" not in u:
        return u
    # Le nom du fichier vient de la page Commons : l'adresse de l'image porte
    # un suffixe de suivi (?utm_source=...) que l'API ne reconnait pas.
    s = c.get("source") or ""
    nom = urllib.parse.unquote(s.split("File:", 1)[1]) if "File:" in s \
        else urllib.parse.unquote(u.split("?", 1)[0].rsplit("/", 1)[1])
    d = get_json("https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo"
                 "&iiprop=url&iiurlwidth=1800&titles=" + urllib.parse.quote("File:" + nom))
    ii = next(iter(d["query"]["pages"].values()))["imageinfo"][0]
    return ii.get("thumburl") or ii["url"]


def telecharge(c):
    f = os.path.join(HD, c["cle"] + ".jpg")
    if os.path.exists(f) and os.path.getsize(f) > 20000:
        return f
    url = url_hd(c)
    for essai in range(5):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=240).read()
            open(f, "wb").write(data)
            time.sleep(1)
            return f
        except Exception as e:
            print("   reessai", essai + 1, e)
            time.sleep(6 * (essai + 1))
    raise RuntimeError("telechargement impossible : " + url)


def cadre_sans_soie(im):
    """La soie bleue de la monture (rouleaux de Jakuchu) : on avance depuis
    chaque bord tant que la colonne ou la ligne est franchement bleue. Rend
    la boite en FRACTIONS, pour l'appliquer a l'image haute definition."""
    im = im.convert("RGB")
    im.thumbnail((400, 800))
    px = im.load()
    W, H = im.size
    def bleu(x, y):
        r, g, b = px[x, y]
        return b > r + 25 and b > g - 10
    def part_col(x):
        ys = range(0, H, 5)
        return sum(bleu(x, y) for y in ys) / len(ys)
    def part_lig(y):
        xs = range(0, W, 5)
        return sum(bleu(x, y) for x in xs) / len(xs)
    g, d, h, b = 0, W - 1, 0, H - 1
    while g < W // 3 and part_col(g) > 0.45: g += 1
    while d > 2 * W // 3 and part_col(d) > 0.45: d -= 1
    while h < H // 4 and part_lig(h) > 0.45: h += 1
    while b > 3 * H // 4 and part_lig(b) > 0.45: b -= 1
    m = 0.035 * H   # la bordure de brocart en haut et en bas
    return ((g + 4) / W, (h + m) / H, (d - 4) / W, (b - m) / H)


def main():
    os.makedirs(HD, exist_ok=True)
    os.makedirs(os.path.join(APP, "img"), exist_ok=True)
    C = {x["num"]: x for x in json.load(open(os.path.join(ICI, "candidats2.json"), encoding="utf-8"))}
    assert len(ORDRE) == 60 and len(set(ORDRE)) == 60 and set(ORDRE) == set(FICHES)
    sortie = []
    for rang, n in enumerate(ORDRE, 1):
        c = C[n]
        peintre, titre, titre_en, annee = FICHES[n]
        im = Image.open(telecharge(c)).convert("RGB")
        if n in CENTRE:
            web = os.path.join(WEB, c["cle"] + ".jpg")
            g, h, d, b = cadre_sans_soie(Image.open(web if os.path.exists(web) else os.path.join(HD, c["cle"] + ".jpg")))
            im = im.crop((round(g * im.width), round(h * im.height), round(d * im.width), round(b * im.height)))
        if im.width > 900:
            im = im.resize((900, round(900 * im.height / im.width)), Image.LANCZOS)
        im = vif(im)
        nom = "j%02d.jpg" % rang
        im.save(os.path.join(APP, "img", nom), quality=72, optimize=True)
        e = {"rang": rang, "fichier": nom, "l": im.width, "h": im.height,
             "peintre": peintre, "mort": MORT.get(peintre), "titre": titre, "titre_en": titre_en,
             "annee": annee, "source": c["source"], "musee": c["musee"], "licence": c["licence"],
             "recadrage": "soie de la monture retiree" if n in CENTRE else None}
        if n in CENTRE:
            e["centre"] = CENTRE[n]
        sortie.append(e)
        print(nom, n, peintre[:20], im.size)
    json.dump({"_note": "La mosaique du japonais : 42 paravents a fond d'or et 18 rouleaux d'Ito Jakuchu, "
                        "choisis et ordonnes avec Jacques le 26 oct. 2026 (construire_app.py). "
                        "« centre » : hauteur du bandeau de l'accueil sur un rouleau vertical (0 = haut, 1 = bas).",
               "_traitement": "vif : autocontrast 1.2/0.8, luminosite x1.12, saturation x1.45, contraste x1.10 ; "
                              "900 px de large, qualite 72 ; pas de recadrage des paravents",
               "images": sortie},
              open(os.path.join(APP, "mosaiques.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(sortie), "tableaux -> app/mosaiques.json")


if __name__ == "__main__":
    main()
