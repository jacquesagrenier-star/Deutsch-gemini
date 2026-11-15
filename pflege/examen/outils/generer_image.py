# -*- coding: utf-8 -*-
"""Une photo de l'oral de l'examen blanc telc Pflege, chez fal. AVEC --payer, C'EST FACTURE (0,15 $).

    python pflege/examen/outils/generer_image.py oral-1a              # controle le prompt et les references, ne paie rien
    python pflege/examen/outils/generer_image.py oral-1a --payer      # APRES l'accord (chef ET Jacques)
    python pflege/examen/outils/generer_image.py --web                 # les PNG faits -> visuel/prototype/telc-pflege/img/*.webp
                                                                       # et leur « src » dans donnees/sprechen.json
    python pflege/examen/outils/generer_image.py entr-2a-1 --prompts pflege/examen/images/prompts_entrainement.py
        # une AUTRE liste de photos (le manuel, 15 nov.) : meme PHOTOS = {nom: {"refs": [...]}} et memes <nom>.prompt.txt
        # dans pflege/examen/images/ ; --web ne place que l'examen blanc, la session place ses images elle-meme

C'EST visuel/generer_scene.py, SANS EN CHANGER UNE LIGNE, comme pflege/outils/generer_scene.py de pflege-scenes :
meme controle (video/verifier_prompt.py), meme regle de paiement (--payer), meme rangement des prises precedentes.
Ce qui change :
  - le prompt vient de pflege/examen/images/<nom>.prompt.txt (fait par images/prompts.py) ;
  - les references viennent de prompts.py (REFS), dans l'ordre ou le prompt les nomme : « perso:<id> » est le
    portrait maitre ~/.wortando/pflege/personnages/<id>.png de pflege-scenes, « scene:<nom> » une de ses scenes
    ~/.wortando/pflege/scenes/<nom>.png ; une reference absente arrete tout, avant tout appel ;
  - l'original (PNG 2K) vit hors du depot : ~/.wortando/pflege/examen/scenes/<nom>.png ; le recu fal revient dans
    pflege/examen/images/<nom>-fal.json ;
  - le format est 4:3 (une photo d'examen, posee a plat).
"""
import importlib.util
import io
import json
import os
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
IMAGES = os.path.join(RACINE, "pflege", "examen", "images")
PFLEGE_LOCAL = os.path.join(os.path.expanduser("~"), ".wortando", "pflege")
ORIGINAUX = os.path.join(PFLEGE_LOCAL, "examen")
WEB = os.path.join(RACINE, "visuel", "prototype", "telc-pflege", "img")
SPRECHEN = os.path.join(RACINE, "visuel", "prototype", "telc-pflege", "donnees", "sprechen.json")
# la photo de chaque image dans les donnees : la tache 1A, puis les trois photos de chaque sujet de 2A
PLACE = {"oral-1a": ("sp1a", None, None),
         "oral-schmerz-1": ("sp2a", "schmerz", 0), "oral-schmerz-2": ("sp2a", "schmerz", 1), "oral-schmerz-3": ("sp2a", "schmerz", 2),
         "oral-schicht-1": ("sp2a", "schicht", 0), "oral-schicht-2": ("sp2a", "schicht", 1), "oral-schicht-3": ("sp2a", "schicht", 2)}


def charger_prompts(chemin=None):
    spec = importlib.util.spec_from_file_location("prompts_oral", chemin or os.path.join(IMAGES, "prompts.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.PHOTOS


def chemin_ref(r):
    genre, nom = r.split(":", 1)
    return os.path.join(PFLEGE_LOCAL, "personnages" if genre == "perso" else "scenes", nom + ".png")


def cle_fal():
    if os.environ.get("FAL_KEY"):
        return
    for d in (RACINE, os.path.normpath(os.path.join(RACINE, "..", "..", ".."))):
        c = os.path.join(d, "fal.secret")
        if os.path.exists(c):
            os.environ["FAL_KEY"] = io.open(c, encoding="utf-8-sig").read().strip()
            return


def web():
    from PIL import Image
    os.makedirs(WEB, exist_ok=True)
    d = json.load(io.open(SPRECHEN, encoding="utf-8"))
    taches = {t["cle"]: t for t in d["series"][0]["taches"]}
    faits = 0
    for nom, (cle, theme, k) in PLACE.items():
        src = os.path.join(ORIGINAUX, "scenes", nom + ".png")
        if not os.path.exists(src):
            print("  pas encore : %s" % nom)
            continue
        im = Image.open(src).convert("RGB")
        im.thumbnail((1400, 1400))
        im.save(os.path.join(WEB, nom + ".webp"), "WEBP", quality=82, method=6)
        t = taches[cle]
        cible = t["bild"] if theme is None else next(x for x in t["themen"] if x["id"] == theme)["bilder"][k]
        cible["src"] = "img/" + nom + ".webp"
        faits += 1
        print("  %s -> img/%s.webp" % (nom, nom))
    io.open(SPRECHEN, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print("%d image(s) en place." % faits)


def main():
    args = sys.argv[1:]
    if "--web" in args:
        return web()
    noms = [a for a in args if not a.startswith("--")]
    if not noms:
        sys.exit(__doc__)
    nom = noms[0]
    autre = args[args.index("--prompts") + 1] if "--prompts" in args else None
    if autre:
        noms = [n for n in noms if n != autre]
        nom = noms[0] if noms else sys.exit(__doc__)
    photos = charger_prompts(os.path.join(RACINE, autre) if autre and not os.path.isabs(autre) else autre)
    if nom not in photos:
        sys.exit("  inconnue : %s (connues : %s)" % (nom, ", ".join(photos)))
    src = os.path.join(IMAGES, nom + ".prompt.txt")
    if not os.path.exists(src):
        sys.exit("  prompt absent : lancer d'abord python pflege/examen/images/prompts.py")
    refs = [chemin_ref(r) for r in photos[nom]["refs"]]
    manquent = [r for r in refs if not os.path.exists(r)]
    if manquent:
        sys.exit("  reference(s) absente(s), rien n'est appele :\n    " + "\n    ".join(manquent))
    os.makedirs(os.path.join(ORIGINAUX, "scenes"), exist_ok=True)
    shutil.copyfile(src, os.path.join(ORIGINAUX, "scenes", nom + ".prompt.txt"))

    sys.path.insert(0, os.path.join(RACINE, "visuel"))
    import generer_scene as G                                    # noqa: E402
    cle_fal()
    if not os.environ.get("SSL_CERT_FILE"):
        try:
            import certifi
            os.environ["SSL_CERT_FILE"] = certifi.where()
        except ImportError:
            pass
    G.ICI = ORIGINAUX
    sys.argv = [sys.argv[0], nom, "--format", "4:3", "--ref"] + refs + (["--payer"] if "--payer" in args else [])
    G.main()
    recu = os.path.join(ORIGINAUX, "scenes", nom + "-fal.json")
    if os.path.exists(recu) and "--payer" in args:
        shutil.copyfile(recu, os.path.join(IMAGES, nom + "-fal.json"))
        print("  recu copie : pflege/examen/images/%s-fal.json" % nom)


if __name__ == "__main__":
    main()
