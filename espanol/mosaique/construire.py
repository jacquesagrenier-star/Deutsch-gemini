"""Les 66 tableaux de la mosaique ESPAGNOLE, prepares comme ceux de l'allemand
(branding/mosaique/) : choisis et ordonnes par Jacques le 14 oct. 2026
(selection.json, tire de la page « Tableaux espagnols »).

Traitement « vif » identique : autocontrast 1,2/0,8, luminosite x1,12,
saturation x1,45, contraste x1,10 ; 900 px de large, JPEG qualite 72.
Au-dela de 1,6 de large pour 1 de haut, recadrage au centre a 1,45 -- la
meme borne que le japonais : un panorama trop etire ferait des carreaux
trop plats.

Les images de depart sont des vignettes de 1800 px servies par Commons (les
originaux depassent parfois 100 Mo) ; elles restent hors de OneDrive.

  python construire.py   ->  img/e01.jpg ... + mosaiques.json
"""
import json, os, sys, time, urllib.parse, urllib.request
from PIL import Image
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import recolter

BRUT = os.path.join(recolter.BRUT, "hd")

# TITRES EN ESPAGNOL, comme l'allemand garde les siens en allemand. Wikidata
# et Commons donnaient parfois un nom de fichier (« Silva002 »), un titre
# anglais ou rien ; les vrais titres viennent de la fiche Commons de chaque
# image (champ « Obra/name » pour Silva). Une annee absente vaut mieux qu'une
# fausse : « 1850 » est la precision « XIXe siecle » de Wikidata, et Navazio
# est ne en 1887. Cle = identifiant Wikidata, ou cle Commons « c... ».
TITRES = {
    "c31f9dde85e0a": ("Panel decorativo del Círculo del Liceo", None),
    "c0c6b7b6a5cfd": ("Alrededores de París", None),
    "Q130569498": ("Señoritas en el campo", None),
    "Q139719649": ("El faisán", None),
    "Q105606670": ("William E. B. Starkweather pescando", None),
    "c0a64d3d2bd95": ("El pavo azul", "1913"),
    "c0cb5e98efcee": ("Cielo gris sobre el mar", "1908"),
    "c66a5b0763064": ("Nubes en la sierra", "1917"),
    "Q27954369": ("Paisaje de Italia", ""),
    "Q106879152": ("Siete Picos, Guadarrama", None),
    "c6f9beb422abd": ("Parvas al sol", "1914"),
    "Q139719710": ("Paisaje", None),
    "Q118129464": ("Venecia", None),
    "Q19162510": ("Paisaje", None),
    "Q130616906": ("Paisaje del Paraíso", None),
    "Q132167920": ("Casa de campo, Alcira", None),
    "Q18749251": ("Recogiendo naranjas, Granada", ""),
    "Q21789840": ("Las lavanderas", None),
    "Q27954607": ("Paisaje (Suiza)", ""),
    "Q105608548": ("Sacando la barca, luz de tarde", None),
    "Q100149983": ("Estudio de playa", None),
    "Q100292173": ("Sacando la barca", None),
    "Q98438877": ("Playa", None),
}
LMAX = 1.6
Image.MAX_IMAGE_PIXELS = None


def url_hd(fichier):
    d = recolter.get("https://commons.wikimedia.org/w/api.php", {"action": "query", "format": "json",
        "prop": "imageinfo", "iiprop": "url|size", "iiurlwidth": 1800, "titles": "File:" + fichier})
    p = next(iter(d["query"]["pages"].values()))
    ii = p["imageinfo"][0]
    return ii.get("thumburl") or ii["url"]


def telecharge(url, f):
    if os.path.exists(f) and os.path.getsize(f) > 5000:
        return
    for essai in range(5):
        try:
            data = urllib.request.urlopen(urllib.request.Request(url, headers=recolter.UA), timeout=180).read()
            open(f, "wb").write(data)
            time.sleep(1)
            return
        except Exception as e:
            print("   reessai", essai + 1, e)
            time.sleep(6 * (essai + 1))
    raise RuntimeError("telechargement impossible : " + url)


def main():
    os.makedirs(BRUT, exist_ok=True)
    os.makedirs(os.path.join(ICI, "img"), exist_ok=True)
    sel = json.load(open(os.path.join(ICI, "selection.json"), encoding="utf-8"))["tableaux"]
    sortie = []
    for t in sel:
        brut = os.path.join(BRUT, t["wikidata"] + ".jpg")
        if not os.path.exists(brut):
            telecharge(url_hd(t["fichier_commons"]), brut)
        im = Image.open(brut).convert("RGB")
        coupe = None
        r = im.width / im.height
        if r > LMAX:
            w = round(im.height * 1.45); x = (im.width - w) // 2
            im = im.crop((x, 0, x + w, im.height)); coupe = "centre, de %.2f a 1,45" % r
        if im.width > 900:
            im = im.resize((900, round(900 * im.height / im.width)), Image.LANCZOS)
        im = recolter.vif(im)
        titre, annee = TITRES.get(t["wikidata"], (None, None))
        titre = titre or t["titre"]
        annee = t["annee"] if annee is None else annee
        nom = "e%02d.jpg" % t["rang"]
        im.save(os.path.join(ICI, "img", nom), quality=72, optimize=True)
        sortie.append({"rang": t["rang"], "fichier": nom, "l": im.width, "h": im.height,
                       "peintre": t["peintre"], "mort": t["mort"], "pays": t["pays"],
                       "titre": titre, "annee": annee, "source": t["page"],
                       "recadrage": coupe})
        print(nom, t["peintre"][:24], im.size, coupe or "")
    json.dump({"_note": "Les mosaiques de l'espagnol, dans l'ordre d'apparition choisi par Jacques le "
                        "14 oct. 2026. Peintres d'Espagne et d'Amerique latine morts avant 1926 "
                        "(domaine public au Mexique, 100 ans). Voir selection.json.",
               "_traitement": "vif : autocontrast 1.2/0.8, luminosite x1.12, saturation x1.45, "
                              "contraste x1.10 ; 900 px de large, qualite 72",
               "images": sortie},
              open(os.path.join(ICI, "mosaiques.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
