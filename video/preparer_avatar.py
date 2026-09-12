# -*- coding: utf-8 -*-
"""Le panier d'un plan pour OmniHuman : l'image allegee, la piste, la base.

    python video/preparer_avatar.py --plan 5
    python video/preparer_avatar.py --plan 5 6 8 9        (plusieurs d'un coup)
    python video/preparer_avatar.py --reste               (tout ce qui manque)

CE QU'IL FAIT, ET POURQUOI CHAQUE ETAPE EXISTE
  1. L'IMAGE, en JPEG de qualite 2 A SA RESOLUTION D'ORIGINE. BytePlus
     refuse au-dela de 5 Mo et nos PNG montent a 6,2 -- mais un PNG est
     sans perte : ses megaoctets paient l'exactitude, pas la finesse. On
     ne reduit la TAILLE qu'en dernier recours (voir alleger()). Le nom
     de l'image vient de A-REFAIRE.txt, jamais devine ni recopie de
     A-REFAIRE-AUDIO.txt, dont les numeros ont derive.

  2. LA PISTE, extraite du clip DEJA MONTE (04-lipsync/planNN.mp4), pas
     d'une piste de tournage.
     ⚠️ C'est la seule facon d'avoir la meme longueur, la meme voix et le
     meme placement de la parole que la prise a laquelle on se compare. Le
     12 septembre 2026, une base mesuree sur 5,04 s contre un essai de
     2,12 s a fait passer la MEME prise d'une LSE-D de 6,49 a 12,55. Une
     ligne de base ne vaut que si elle a la forme de ce qu'on lui compare.

  3. LA LIGNE DE BASE au syncnet, gardee AVANT l'essai. Sans elle, on
     compare le retour a un souvenir.

  Le panier part dans _a-televerser/ ; les prises revenues vivent dans
  _essai-avatar/retours/, les mesures dans _essai-avatar/.

⚠️ NE PAS RACCOURCIR LA PISTE POUR ECONOMISER. Le silence final est la
   marge dont la bouche a besoin pour se refermer -- mesure sur le plan 16,
   ou elle met environ 1,4 s a redescendre apres le dernier mot. Quelques
   dizaines de cents contre une prise a refaire.

⚠️ ET LES DUREES DE A-REFAIRE.txt SONT PERIMEES par endroits : elle
   annonce 7,08 s de parole au plan 13, la piste en donne 4,57. On mesure,
   on ne recopie pas.
"""
import argparse
import io
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402
import syncnet as S                                         # noqa: E402

PRIX = 0.12            # BytePlus, releve sur leur fiche le 12 sept. 2026
PARLANTS = [5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


PLAFOND = 5 * 1024 * 1024      # BytePlus refuse une image de plus de 5 Mo


def alleger(F, src, dst):
    """Passer sous les 5 Mo en gardant TOUS LES PIXELS.

    ⚠️ LEUR FICHE LE DIT : « the clearer the input image, the better the
    generation effect ». Le 12 septembre 2026 j'ai reduit toutes les images
    a 1080 de large parce qu'UNE d'entre elles (mark-serre-b.png, 6,2 Mo)
    depassait le plafond -- et j'ai applique au reste une contrainte qui ne
    valait que pour elle. Anna partait d'un PNG de 1536x2752 ; elle est
    arrivee chez le modele en 1080 de large.

    Un PNG est SANS PERTE : ses megaoctets paient l'exactitude, pas la
    finesse. Un JPEG de qualite 2 a la MEME resolution tient dans le
    cinquieme du poids et garde les pixels. On ne reduit la taille qu'en
    dernier recours, et on le dit quand ca arrive.
    """
    for q in (2, 4, 6, 8):
        subprocess.run([F, "-y", "-v", "error", "-i", src, "-q:v", str(q), dst],
                       check=True)
        if os.path.getsize(dst) <= PLAFOND:
            return q, False
    subprocess.run([F, "-y", "-v", "error", "-i", src, "-vf", "scale=1080:-2",
                    "-q:v", "2", dst], check=True)
    return 2, True


# ⚠️ LA FEUILLE QUI FAIT FOI EST A-REFAIRE.txt, PAS A-REFAIRE-AUDIO.txt.
# Les deux ont des blocs « PLAN 13 » et ce ne sont PAS le meme plan :
#
#   A-REFAIRE.txt        anna serre, zoom, « Nehmen Sie die S-Bahn. Die
#                        Fahrkarte kaufen Sie am Automaten, unten in der
#                        Halle. »            -> anna-serre.png
#   A-REFAIRE-AUDIO.txt  anna, 5 s, « Nehmen Sie die S-Bahn. » seulement
#                                            -> anna-moyen-serre-c.png
#
# La feuille audio a redecoupe les longues repliques en morceaux, et ses
# numeros ont cesse de suivre le montage. C'est aussi pourquoi
# audio/scenes/13-anna.mp3 ne fait que 1,23 s.
#
# Cette version du script a d'abord lu la mauvaise feuille : elle aurait
# envoye la mauvaise image a plusieurs plans, et RIEN ne s'en serait
# plaint -- le modele aurait obei, le fichier serait arrive, et la scene
# aurait change de cadrage au milieu. C'est exactement l'avertissement de
# 01-images/_lisez-moi.txt sur la numerotation abandonnee du 8 septembre.
#
# ⚠️ Verifier avec --carte avant toute serie : la carte imprime le plan,
# l'image et la replique cote a cote. Une correspondance qu'on ne relit
# pas est une correspondance qu'on suppose.
FEUILLE = "A-REFAIRE.txt"


def _bloc(ep, n):
    t = io.open(os.path.join(ep, FEUILLE), encoding="utf-8").read()
    parts = re.split(r"(?m)^PLAN %02d\b" % n, t)
    return parts[1] if len(parts) > 1 else ""


def image_du_plan(ep, n):
    m = re.search(r"Start Frame : (\S+)", _bloc(ep, n))
    return m.group(1) if m else None


def replique(ep, n):
    m = re.search(r"<< (.+?) >>", _bloc(ep, n), re.S)
    return " ".join(m.group(1).split()) if m else ""


def un_plan(F, ep, dos, n, refaire):
    nom_img = image_du_plan(ep, n)
    if not nom_img:
        print("  plan %02d : pas de @img1 dans la feuille -- ignore" % n)
        return 0.0
    src_img = os.path.join(ep, "01-images", nom_img)
    src_vid = os.path.join(ep, "04-lipsync", "plan%02d.mp4" % n)
    if not os.path.exists(src_img) or not os.path.exists(src_vid):
        print("  plan %02d : source manquante -- ignore" % n)
        return 0.0

    # ⚠️ Ce qui se TELEVERSE vit a part de ce qui REVIENT. Jacques, le 12
    # septembre : « je suis oblige de chercher a travers de plus en plus
    # d images ». Un dossier ou l on cherche est un dossier ou l on se
    # trompe de fichier.
    tel = os.path.join(os.path.dirname(dos), "_a-televerser")
    if not os.path.isdir(tel):
        os.makedirs(tel)
    dst_img = os.path.join(tel, "plan%02d-%s.jpg" % (n, os.path.splitext(nom_img)[0]))
    dst_mp3 = os.path.join(tel, "plan%02d-pleine.mp3" % n)
    base_f = os.path.join(dos, "plan%02d-avant.json" % n)

    if refaire or not os.path.exists(dst_img):
        alleger(F, src_img, dst_img)
    if refaire or not os.path.exists(dst_mp3):
        subprocess.run([F, "-y", "-v", "error", "-i", src_vid, "-vn",
                        "-ar", "44100", "-ac", "1", "-b:a", "192k", dst_mp3],
                       check=True)

    duree = M.duree(F, dst_mp3)
    tete, queue, _ = M.parole(F, dst_mp3)
    print("\n  PLAN %02d   « %s »" % (n, replique(ep, n)))
    print("    image : %-38s %6.0f ko" % (os.path.basename(dst_img),
                                          os.path.getsize(dst_img) / 1024.0))
    print("    audio : %-38s %6.2f s   parole %.2f-%.2f"
          % (os.path.basename(dst_mp3), duree, tete, queue))
    print("    cout  : %.2f $" % (duree * PRIX))

    if not os.path.exists(base_f):
        import json
        r = S.mesurer(src_vid)
        if r:
            img, d, c = r
            val = {"clip": os.path.relpath(src_vid, RACINE), "offset_images": img,
                   "offset_ms": round(img / S.IPS_SYNCNET * 1000.0, 1),
                   "lse_d": round(d, 3), "lse_c": round(c, 3)}
            io.open(base_f, "w", encoding="utf-8", newline="").write(
                json.dumps(val, ensure_ascii=False, indent=1) + "\n")
            print("    base  : offset %+.0f ms   LSE-D %.3f   LSE-C %.3f"
                  % (val["offset_ms"], val["lse_d"], val["lse_c"]))
        else:
            print("    base  : aucun visage suivi -- comparaison boiteuse")
    else:
        import json
        v = json.load(io.open(base_f, encoding="utf-8"))
        print("    base  : offset %+.0f ms   LSE-D %.3f   LSE-C %.3f  (deja prise)"
              % (v["offset_ms"], v["lse_d"], v["lse_c"]))
    return duree


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=int, nargs="*", default=[])
    ap.add_argument("--reste", action="store_true",
                    help="tous les plans parlants sans prise revenue")
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--refaire", action="store_true")
    ap.add_argument("--carte", action="store_true",
                    help="imprimer plan / image / replique, et s'arreter")
    a = ap.parse_args()

    ep = os.path.join(RACINE, "video", "episode-%s" % a.scene)
    if a.carte:
        print("  plan   image de depart              replique")
        print("  " + "-" * 74)
        vues = {}
        for n in PARLANTS:
            img = image_du_plan(ep, n) or "INTROUVABLE"
            vues.setdefault(img, []).append(n)
            ok = "" if os.path.exists(os.path.join(ep, "01-images", img)) else "  ABSENTE"
            print("  %02d     %-28s %s%s" % (n, img, replique(ep, n)[:34], ok))
        # ⚠️ Une image servie deux fois = le personnage repart de la position
        # identique, et ca se voit. C'est le defaut de boucle de decouper.py.
        for img, ns in sorted(vues.items()):
            if len(ns) > 1:
                print("\n  ⚠️ %s sert aux plans %s -- meme pose de depart, ca se voit."
                      % (img, ", ".join("%02d" % n for n in ns)))
        return
    dos = os.path.join(ep, "_essai-avatar")
    if not os.path.isdir(dos):
        os.makedirs(dos)

    plans = list(a.plan)
    if a.reste:
        plans = [n for n in PARLANTS
                 if not os.path.exists(os.path.join(dos, "plan%02d-omnihuman.mp4" % n))]
    if not plans:
        sys.exit("  Rien a preparer. Donner --plan N, ou --reste.")

    F = M.ffmpeg()
    total = sum(un_plan(F, ep, dos, n, a.refaire) for n in plans)
    print("\n  " + "-" * 56)
    print("  %d plan(s), %.2f s au total = %.2f $ a %.2f $/s"
          % (len(plans), total, total * PRIX, PRIX))


if __name__ == "__main__":
    main()
