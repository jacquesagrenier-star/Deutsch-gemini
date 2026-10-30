"""Les tableaux de la mosaique PORTUGAISE, prepares comme ceux de l'anglais
(anglais/mosaique/construire.py) et de l'espagnol : choisis et ordonnes par
Jacques (selection.json, tire de son choix par selection_depuis_choix.py).

Traitement « vif » identique : autocontrast 1,2/0,8, luminosite x1,12,
saturation x1,45, contraste x1,10 ; 900 px de large, JPEG qualite 72.
Au-dela de 1,6 de large pour 1 de haut, recadrage au centre a 1,45.

Les images de depart sont des vignettes de 1800 px servies par Commons ; elles
restent hors de OneDrive (C:/Users/jacqu/.wortando/portugais-mosaique-brut/hd).
img/info.jpg (l'ecran « Comment ca marche ») est une copie du dernier, comme
l'espagnol et l'anglais.

  python portugais/mosaique/construire.py   ->  app/img/p01.jpg ... + app/mosaiques.json
"""
import json, os, shutil, sys, time, urllib.request
from PIL import Image
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import recolter

BRUT = os.path.join(recolter.BRUT, "hd")
APP = os.path.join(ICI, "app")

# TITRES EN PORTUGAIS, comme l'espagnol garde les siens en espagnol et l'anglais
# en anglais. Wikidata et Commons donnent parfois un nom de fichier ou un titre
# d'inventaire : on corrige ici, cle = identifiant Wikidata ou cle Commons « c... ».
# Valeur : (titre, annee) ; annee None = garder celle de selection.json.
TITRES = {
    "Q60392628": ("Sem título", None),                       # n° 1, « (1913) » dans le titre
    "Q60386887": ("Sem título", None),                       # n° 12
    "Q141593803": ("Cavaleiros", None),                      # n° 36, entre parentheses
    "Q109374469": ("Caminho da Pena", None),                 # n° 40, sans titre (nom du fichier)
    "Q109367039": ("A Boca do Inferno", None),               # n° 74, point final
    "c34634e54cd57": ("Visita régia aos Açores", None),      # E20, titre de 112 caracteres
    "Q60254236": ("Gerês", None),                            # E31, l'annee dans le titre
    "c398f1e2d04b6": ("Regresso do campo", None),            # E50, titre anglais
    "ce469cc870d91": ("Carlos Relvas monta o cavalo Pérola", None),  # E53, lieu retire
}
# Un fichier Commons plus grand du MEME tableau, quand celui de Wikidata est
# petit (verifie a l'oeil ; domaine public lu sur sa fiche).
FICHIER_HD = {
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
    sys.stdout.reconfigure(encoding="utf-8")
    os.makedirs(BRUT, exist_ok=True)
    os.makedirs(os.path.join(APP, "img"), exist_ok=True)
    sel = json.load(open(os.path.join(ICI, "selection.json"), encoding="utf-8"))["tableaux"]
    sortie = []
    for t in sel:
        brut = os.path.join(BRUT, t["wikidata"] + ".jpg")
        if not os.path.exists(brut):
            telecharge(url_hd(FICHIER_HD.get(t["wikidata"], t["fichier_commons"])), brut)
        im = Image.open(brut).convert("RGB")
        coupe = None
        r = im.width / im.height
        if r > LMAX:
            w = round(im.height * 1.45); x = (im.width - w) // 2
            im = im.crop((x, 0, x + w, im.height)); coupe = "centre, de %.2f a 1,45" % r
        if im.width > 900:
            im = im.resize((900, round(900 * im.height / im.width)), Image.LANCZOS)
        im = recolter.vif(im)
        nom = "p%02d.jpg" % t["rang"]
        im.save(os.path.join(APP, "img", nom), quality=72, optimize=True)
        titre, annee = TITRES.get(t["wikidata"], (t["titre"], None))
        sortie.append({"rang": t["rang"], "fichier": nom, "l": im.width, "h": im.height,
                       "peintre": t["peintre"], "mort": t["mort"], "pays": t.get("pays", "Portugal"),
                       "titre": titre, "annee": t["annee"] if annee is None else annee,
                       "source": t["page"], "licence": t["licence"], "recadrage": coupe})
        print(nom, t["peintre"][:28], im.size, coupe or "")
    shutil.copyfile(os.path.join(APP, "img", sortie[-1]["fichier"]), os.path.join(APP, "img", "info.jpg"))
    json.dump({"_note": "Les mosaiques du portugais, dans l'ordre d'apparition choisi par Jacques. "
                        "Peintres portugais ; domaine public ou CC0 (licence lue fichier par fichier). "
                        "Voir selection.json et LISEZ-MOI.md.",
               "_traitement": "vif : autocontrast 1.2/0.8, luminosite x1.12, saturation x1.45, "
                              "contraste x1.10 ; 900 px de large, qualite 72",
               "images": sortie},
              open(os.path.join(APP, "mosaiques.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
