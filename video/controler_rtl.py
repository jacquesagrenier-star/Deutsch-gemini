# -*- coding: utf-8 -*-
"""Controle des sous-titres persans et arabes graves : chaque ligne, a cote du rendu de Chrome.

    python video/controler_rtl.py --scene 04-schrippe --langue ar --video audio/mp3/episodes/de/ep04-v2.ar.mp4
    python video/controler_rtl.py --scene 04-schrippe --langue fa --video ... --plans 7,15,16

Ne de la soiree du 26 oct. 2026 : les sous-titres persans et arabes des quatre
episodes allemands etaient sortis dans le mauvais sens (ponctuation deplacee, et
les lignes melees d'un mot latin -- « Schrippe », « Berliner » -- dans le
desordre). Je les avais « verifies a l'oeil » quatre jours plus tot : je ne sais
pas juger l'ordre des glyphes arabes sur une image. Chrome, lui, applique
l'algorithme bidirectionnel correctement : la planche pose a gauche la bande
gravee, a droite le meme texte rendu par Chrome (dir=rtl). Les deux doivent
dire la meme chose dans le meme ordre ; seul le retour a la ligne peut differer.

Par defaut : tous les plans dont la ligne contient une lettre latine (les plus
fragiles), plus deux autres. La planche va dans le dossier temporaire du
systeme, JAMAIS a cote de la video : audio/mp3 est le dossier publie par
Firebase Hosting, une image posee la partirait au prochain depot.
"""
import argparse, json, os, re, subprocess, sys, tempfile

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--scene", required=True, help="ex. 04-schrippe (scenes/<scene>.json)")
    a.add_argument("--langue", required=True, choices=["fa", "ar"])
    a.add_argument("--video", required=True, help="video gravee a controler")
    a.add_argument("--feuille", help="_plans.json du montage (defaut : video/episode-<scene>/_montage-avatar/_plans.json)")
    a.add_argument("--plans", help="numeros de plans, separes par des virgules")
    a = a.parse_args()
    from PIL import Image
    from playwright.sync_api import sync_playwright

    scene = json.load(open(os.path.join(RACINE, "scenes", a.scene + ".json"), encoding="utf-8"))
    feuille = a.feuille or os.path.join(RACINE, "video", "episode-" + a.scene, "_montage-avatar", "_plans.json")
    temps = {p["n"]: p for p in json.load(open(feuille, encoding="utf-8"))}
    textes = {p["n"]: p.get(a.langue) for p in scene["plans"] if p.get(a.langue) and p["n"] in temps}
    if a.plans:
        choix = [int(x) for x in a.plans.split(",")]
    else:
        latins = [n for n, t in textes.items() if re.search("[A-Za-z]", t)]
        autres = [n for n in textes if n not in latins][:2]
        choix = sorted(latins + autres)
    if not choix:
        sys.exit("Aucun plan a controler.")

    # Hauteur de la video, pour couper la bande du bas ou vivent les sous-titres.
    h = int(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=height", "-of", "csv=p=0", a.video],
                           capture_output=True, text=True).stdout.strip() or 1280)
    w = int(h * 9 / 16)
    bande = int(h * 0.12)
    base = os.path.join(tempfile.gettempdir(), os.path.splitext(os.path.basename(a.video))[0])
    tmp = base + "-rtl-tmp.png"
    rangees = []
    with sync_playwright() as p:
        nav = p.chromium.launch()
        page = nav.new_page(viewport={"width": w, "height": bande})
        for n in choix:
            info = temps[n]
            t = info["debut"] + info["duree"] * 0.6
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "%.2f" % t, "-i", a.video, "-frames:v", "1",
                            "-vf", "crop=%d:%d:0:%d" % (w, bande, h - bande), tmp], check=True)
            gravee = Image.open(tmp).convert("RGB")
            page.set_content("<body style='margin:0;background:#333;color:#fff;font:%dpx Arial;"
                             "display:flex;align-items:center;justify-content:center;height:%dpx'>"
                             "<p dir='rtl' style='text-align:center;margin:0 30px'>%s</p></body>"
                             % (int(h * 0.027), bande, textes[n]))
            page.screenshot(path=tmp)
            chrome = Image.open(tmp).convert("RGB")
            r = Image.new("RGB", (w * 2, bande))
            r.paste(gravee, (0, 0))
            r.paste(chrome, (w, 0))
            rangees.append(r)
        nav.close()
    os.remove(tmp)
    planche = Image.new("RGB", (w * 2, bande * len(rangees)))
    for i, r in enumerate(rangees):
        planche.paste(r, (0, bande * i))
    dest = base + "-rtl.png"
    planche.save(dest)
    print("Plans controles : %s" % ", ".join(str(n) for n in choix))
    print("A gauche la video, a droite Chrome : %s" % dest)


if __name__ == "__main__":
    main()
