# -*- coding: utf-8 -*-
"""La planche des couleurs d'yeux de « Descripcion fisica » : cinq tres gros plans photoreealistes, un par couleur.
ET C'EST FACTURE : 0,15 $ l'image, chez fal.

    python visuel/descripcion/yeux.py            # ceux qui manquent -> visuel/descripcion/img/yeux-<couleur>.png
    python visuel/descripcion/yeux.py --montrer  # les prompts seuls, gratuit

Jacques, 2 nov. 2026 : « avoir une planche qui montre les yeux de differentes couleurs. Tout ce qui peut etre
realiste. » Les noms sont ceux des exercices (verdes, azules, castanos, negros, grises).
"""
import io, json, os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

MODELE, PRIX = "fal-ai/nano-banana-pro", 0.15
BASE = ("A photorealistic extreme close-up photograph of a pair of human eyes and the bridge of the nose, framed "
        "from the eyebrows to just below the eyes, both eyes fully open and looking straight at the camera, soft "
        "even daylight, sharp focus on the irises, natural skin texture, no makeup, no glasses, no text. ")
YEUX = {
    "verdes":   "IRISES: clearly green, a vivid natural green. Fair skin.",
    "azules":   "IRISES: clearly blue, a bright natural blue. Fair skin.",
    "castanos": "IRISES: warm medium brown, clearly brown, not black. Olive skin.",
    "negros":   "IRISES: very dark brown, almost black, the pupil barely distinguishable. Medium brown skin.",
    "grises":   "IRISES: clearly grey, a cool light grey with no blue or green tint. Fair skin.",
}


def main():
    montrer = "--montrer" in sys.argv
    os.makedirs(os.path.join(ICI, "img"), exist_ok=True)
    a_faire = [c for c in YEUX if not os.path.exists(os.path.join(ICI, "img", "yeux-%s.png" % c))]
    print("  %d image(s), %.2f $" % (len(a_faire), len(a_faire) * PRIX))
    cle = None if montrer else O.cle()
    for c in a_faire:
        prompt = BASE + YEUX[c]
        print("\n  %s\n  %s" % (c, prompt))
        if montrer:
            continue
        corps = {"prompt": prompt, "aspect_ratio": "21:9", "resolution": "1K", "output_format": "png", "num_images": 1}
        soum = O._json("https://queue.fal.run/" + MODELE, cle, corps)
        res = O.attendre(soum["status_url"], soum["response_url"], cle, bavard=False)
        sortie = os.path.join(ICI, "img", "yeux-%s.png" % c)
        O.telecharger(res["images"][0]["url"], sortie)
        io.open(os.path.join(ICI, "img", "yeux-%s-fal.json" % c), "w", encoding="utf-8").write(json.dumps({
            "modele": MODELE, "request_id": soum.get("request_id"), "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "prompt": prompt, "prix": PRIX}, ensure_ascii=False, indent=1))
        print("  ->", os.path.relpath(sortie, RACINE), "(%.2f $)" % PRIX)


if __name__ == "__main__":
    main()
