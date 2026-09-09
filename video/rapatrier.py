# -*- coding: utf-8 -*-
"""Rapatrie une prise depuis Telechargements, lui coupe le son, et la classe.

    python video/rapatrier.py --plan 13
    python video/rapatrier.py --plan 13 --fichier "C:/chemin/vers/clip.mp4"

POURQUOI COUPER LE SON
    Seedance fabrique une piste audio et fait articuler au personnage des mots
    inventes. La voix, elle, vient d'ElevenLabs et se pose au montage. Garder
    les deux revient a se demander trois semaines plus tard laquelle on ecoute.

    Ce que le personnage semblait articuler n'a aucune importance : sync.so
    reecrit la zone de la bouche par-dessus. Seule compte la nettete du visage.

ON NE REENCODE PAS
    -c copy recopie le flux video tel quel et jette la piste audio. Aucune
    perte, et c'est instantane. Un reencodage a cette etape abimerait l'image
    avant meme le lip-sync, qui la reencodera de toute facon une fois.

PLUSIEURS PRISES PAR PLAN, ET C'EST VOULU
    Un modele video ne rend jamais deux fois la meme chose. On juge sur une
    serie, pas sur un essai. Le numero s'incremente tout seul : plan13-01,
    plan13-02... On garde les ratees jusqu'a ce que la bonne soit choisie --
    elles coutent 200 credits chacune et ne se refont pas a l'identique.
"""
import argparse
import glob
import hashlib
import io
import json
import os
import subprocess
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEOS = (".mp4", ".mov", ".webm", ".m4v")


def ffmpeg():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("  ffmpeg introuvable. Il vient avec le paquet imageio-ffmpeg.")


def telechargements():
    """Le dossier de telechargement, quel que soit son nom -- il est en francais
    sur certaines installations et en anglais sur d'autres."""
    base = os.path.expanduser("~")
    for nom in ("Downloads", "Telechargements", u"T\u00e9l\u00e9chargements"):
        d = os.path.join(base, nom)
        if os.path.isdir(d):
            return d
    return None


def plus_recente(dossier):
    fichiers = [f for f in glob.glob(os.path.join(dossier, "*"))
                if f.lower().endswith(VIDEOS)]
    return max(fichiers, key=os.path.getmtime) if fichiers else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=int, required=True)
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--fichier", help="a defaut, la video la plus recente des telechargements")
    a = ap.parse_args()

    src = a.fichier
    if not src:
        d = telechargements()
        if not d:
            sys.exit("  Dossier de telechargement introuvable. Passe --fichier.")
        src = plus_recente(d)
        if not src:
            sys.exit("  Aucune video dans %s.\n"
                     "  Clique << Download >> sur la prise dans Artlist, puis relance." % d)
    if not os.path.exists(src):
        sys.exit("  Introuvable : %s" % src)

    # Le plan existe-t-il vraiment dans la scene ? Une faute de frappe sur --plan
    # classerait la prise sous un numero qui n'a pas de replique.
    fs = os.path.join(RACINE, "scenes", a.scene + ".json")
    if os.path.exists(fs):
        d = json.load(io.open(fs, encoding="utf-8"))
        p = next((x for x in d["plans"] if x["n"] == a.plan), None)
        if not p:
            sys.exit("  Le plan %d n'existe pas dans %s." % (a.plan, a.scene))
        print("  plan %02d  %s  (%s s)" % (a.plan, p["locuteur"], p["duree"]))
        if p.get("de"):
            print("  << %s >>" % p["de"])

    dst = os.path.join(RACINE, "video", "episode-" + a.scene, "02-prises")
    if not os.path.isdir(dst):
        os.makedirs(dst)
    n = 1
    while os.path.exists(os.path.join(dst, "plan%02d-%02d.mp4" % (a.plan, n))):
        n += 1
    out = os.path.join(dst, "plan%02d-%02d.mp4" % (a.plan, n))

    # DEJA RAPATRIE ? Le 8 septembre, faute d avoir telecharge la nouvelle prise,
    # le clip du plan 3 a ete classe une deuxieme fois sous le plan 7 : meme
    # fichier, deux numeros, et une planche de controle qui montrait le mauvais
    # plan. On garde donc l empreinte de chaque source rapatriee.
    registre = os.path.join(dst, "_sources.txt")
    emp = hashlib.md5(open(src, "rb").read()).hexdigest()
    deja = {}
    if os.path.exists(registre):
        for ligne in io.open(registre, encoding="utf-8"):
            if " " in ligne:
                h, q = ligne.strip().split(" ", 1)
                deja[h] = q
    if emp in deja:
        sys.exit("  DEJA RANGE sous %s -- la nouvelle prise n a pas ete "
                 "telechargee. Clique Download dans Artlist, puis relance."
                 % deja[emp])

    # ⚠️ MESURER LA VOIX DE SEEDANCE AVANT DE LA JETER (9 septembre 2026)
    #
    # Depuis qu'on lui donne la voix en reference, Seedance ne la place PAS ou
    # on la lui donne : il decale l'attaque d'environ 0,35 s, et sur les
    # longues repliques il ETIRE l'articulation. Sa piste generee est le seul
    # temoin exact de sa machoire -- les deux naissent dans la meme passe.
    #
    # Elle est coupee une ligne plus bas et ne revient jamais. On la mesure
    # donc ici, une fois, et on ecrit le resultat a cote de la prise :
    #
    #   plan 11   piste donnee 0,51-2,97   Seedance a mis 0,87-3,99
    #   plan 14   piste donnee 0,50-1,97   Seedance a mis 0,84-2,27
    #
    # Le decalage se rattrape au montage. L'ETIREMENT, NON : au plan 11 la
    # bouche articule 3,12 s pour une replique de 2,47 -- Jacques : « la bouche
    # d'Anna continue a bouger apres qu'elle a arrete de parler ». Un plan
    # etire est a refaire, pas a recaler, et ce script le dit maintenant.
    sys.path.insert(0, os.path.join(RACINE, "video"))
    import montage as MM                                    # noqa: E402
    # 10 % : la piste de Seedance porte l'ambiance du hall. Voir montage.parole.
    b0, b1, _ = MM.parole(ffmpeg(), src, seuil=0.10)
    mp3 = os.path.join(RACINE, "audio", "scenes", a.scene,
                       "%02d-%s.mp3" % (a.plan, p["locuteur"])) if p else None
    v0 = v1 = None
    if mp3 and os.path.exists(mp3):
        v0, v1, _ = MM.parole(ffmpeg(), mp3)

    r = subprocess.run([ffmpeg(), "-hide_banner", "-nostats", "-loglevel", "error",
                        "-y", "-i", src, "-c", "copy", "-an", out],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit("  echec ffmpeg :\n%s" % r.stderr[-600:])

    print("  %s  ->  video/episode-%s/02-prises/%s  (%d Ko, muet)"
          % (os.path.basename(src), a.scene, os.path.basename(out),
             os.path.getsize(out) // 1024))
    io.open(registre, "a", encoding="utf-8", newline="").write(emp + " " + os.path.basename(out) + chr(10))

    # La fiche de parole, a cote des prises. montage.py y lira ou poser la voix.
    fiche = os.path.join(dst, "_parole.json")
    tout = {}
    if os.path.exists(fiche):
        tout = json.load(io.open(fiche, encoding="utf-8"))
    tout[os.path.basename(out)] = {"bouche": [round(b0, 2), round(b1, 2)]}
    io.open(fiche, "w", encoding="utf-8", newline=chr(10)).write(
        json.dumps(tout, ensure_ascii=False, indent=1, sort_keys=True) + chr(10))

    print("  bouche de %.2f a %.2f s" % (b0, b1), end="")
    if v0 is not None:
        parle, dit = b1 - b0, v1 - v0
        print("   (la replique dure %.2f s, la bouche articule %.2f s)"
              % (dit, parle))
        if parle - dit > 0.15:
            print("  ⚠️ ETIREE de %.2f s : la bouche continuera de bouger apres"
                  " le dernier mot." % (parle - dit))
            print("     Un decalage se recale au montage, un etirement non."
                  " Cette prise est a refaire.")
    else:
        print()
    print("  L'original reste dans les telechargements : rien n'est efface.")


if __name__ == "__main__":
    main()
