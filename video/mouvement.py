# -*- coding: utf-8 -*-
"""Anime un plan de DECOR chez fal : image + prompt de mouvement -> clip.

    python video/mouvement.py --scene 02-beim-buergeramt --simuler
    python video/mouvement.py --scene 02-beim-buergeramt --plan 2
    python video/mouvement.py --scene 02-beim-buergeramt --reste

CE QUE CA REMPLACE
    Le dernier geste manuel de la chaine. Les images sont passees chez fal en
    septembre (image_plan.py) quand les credits Artlist se sont epuises ; les
    CLIPS de decor, eux, se faisaient encore a la main dans Artlist Directing
    avec Seedance 2.0 Mini, puis se rapatriaient depuis Telechargements.

    fal sert le meme modele -- bytedance/seedance-2.0/fast/image-to-video --
    et le prompt vient du depot au lieu d'etre colle dans un formulaire.
    Une prise qu'on ne peut pas rejouer n'est pas une prise.

⚠️ generate_audio EST A true PAR DEFAUT, ET C'EST UN PIEGE.
    Seedance fabrique une piste et fait articuler des mots inventes. Tout
    l'outillage du projet existe pour s'en debarrasser (rapatrier.py coupait
    le son au retour). On le desactive a la source : la voix vient
    d'ElevenLabs et se pose au montage. Garder les deux revient a se demander
    trois semaines plus tard laquelle on ecoute.

⚠️ LA DUREE EST UN ENTIER DE SECONDES, ET LE MONTAGE TRONQUE.
    Le modele n'accepte que 4 a 15 s entieres. monter_avatar.py, lui, prend
        min(longueur du clip ; 0,35 amorce + narration + 0,90 queue)
    -- donc un clip trop LONG ne coute que de l'argent, un clip trop COURT
    coupe la narration en cours de phrase sans la moindre erreur. On arrondit
    donc a l'entier SUPERIEUR, jamais au plus proche.

⚠️ 9:16 EXPLICITE, JAMAIS « auto ».
    A-TOURNER.txt : « Format 9:16 -- A VERIFIER A CHAQUE FOIS. Il s'est
    reinitialise en 16:9 tout seul le 8 septembre 2026. » Une valeur deduite
    de l'image est une valeur qu'on ne controle pas.

LE PROMPT SE LIT DANS A-TOURNER.txt, IL NE SE RECOPIE PAS
    Bloc « PROMPT DE MOUVEMENT », jusqu'a la ligne de tirets ou au ⚠️ suivant.
    Le fichier reste la source unique : un prompt recopie ici divergerait le
    jour ou l'on corrige la-bas.

LA CLE N'EST PAS DANS LE CODE
    fal.secret a la racine (ignore par git) ou FAL_KEY.
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402

MODELE = "bytedance/seedance-2.0/fast/image-to-video"
FILE = "https://queue.fal.run/" + MODELE
PRIX = 0.2419            # $ la seconde en 720p, tier rapide -- releve le 15/09/2026
RESOLUTION = "720p"      # comme l'episode 1 ; le 480p coute moitie moins et se voit
AMORCE, QUEUE = 0.35, 0.90       # les memes que monter_avatar.py

# ⚠️ H3 MAX POUR LES PLANS FIXES (memoire du 17 sept. 2026 : « plan fixe, meme a
#    deux personnages, reussit » ; il marche au RALENTI sur un plan de marche).
#    Branche le 21 oct. pour la serie espagnole : 0,08 $/s contre 0,24.
#    prompt_expansion_mode « disabled » : par defaut H3 REECRIT le prompt avant
#    de generer ; on paierait alors un texte que personne n'a relu (acquis du
#    22 sept. : « imprimer le prompt EXACT avant l'envoi »).
MODELES = {
    "seedance": ("bytedance/seedance-2.0/fast/image-to-video", 0.2419, "720p"),
    "h3": ("minimax/h3-max/image-to-video", 0.08, "768P"),
}


def choisir_modele(nom):
    global MODELE, FILE, PRIX, RESOLUTION
    MODELE, PRIX, RESOLUTION = MODELES[nom]
    FILE = "https://queue.fal.run/" + MODELE


def queues_particulieres(scene):
    """Les queues par plan, dans _queues.txt, a cote des plans.

    ⚠️ LE MEME FICHIER QUE monter_avatar.py, ET C'EST TOUT L'INTERET. Si ce
       script gardait la queue commune pendant que le montage en applique une
       autre, on paierait une prise trop courte pour le plan qu'on vient
       justement d'allonger -- et rien ne s'en plaindrait.
    """
    chemin = os.path.join(RACINE, "video", "episode-" + scene, "_queues.txt")
    out = {}
    if not os.path.exists(chemin):
        return out
    for ligne in io.open(chemin, encoding="utf-8").read().splitlines():
        ligne = ligne.split("#")[0].strip()
        if not ligne:
            continue
        bouts = ligne.replace(",", " ").split()
        if len(bouts) >= 2:
            out[int(bouts[0])] = float(bouts[1])
    return out


def duree_a_generer(narration, queue=QUEUE):
    """Ce qu'il faut demander au modele : entier de secondes, arrondi en HAUT."""
    besoin = AMORCE + float(narration) + queue
    return max(4, min(15, int(besoin) + (1 if besoin > int(besoin) else 0)))


def prompt_du_plan(scene, n):
    """Le bloc « PROMPT DE MOUVEMENT » du plan n, dans A-TOURNER.txt."""
    chemin = os.path.join(RACINE, "video", "episode-" + scene, "A-TOURNER.txt")
    if not os.path.exists(chemin):
        sys.exit("  A-TOURNER.txt introuvable : %s" % chemin)
    txt = io.open(chemin, encoding="utf-8").read()
    # On borne d'abord AU PLAN, sinon le « PROMPT DE MOUVEMENT » trouve peut
    # etre celui du plan suivant -- l'erreur qui envoie la bonne image avec le
    # mauvais mouvement, et dont rien dans le retour ne se plaint.
    debut = re.search(r"^PLAN %02d\b" % n, txt, re.M)
    if not debut:
        sys.exit("  pas de bloc « PLAN %02d » dans A-TOURNER.txt" % n)
    suite = re.search(r"^PLAN \d\d\b", txt[debut.end():], re.M)
    bloc = txt[debut.start(): debut.end() + (suite.start() if suite else len(txt))]

    # ⚠️ \Z ET NON $. En mode multiligne, $ marque la fin de CHAQUE ligne :
    #    une simple LIGNE VIDE terminait donc le prompt. Un prompt ecrit en
    #    plusieurs paragraphes partait ampute de tout ce qui suivait la
    #    premiere ligne vide -- sans erreur, et apres avoir paye la prise.
    #    Vu le 22 septembre 2026 en imprimant le prompt avant l'envoi : le
    #    plan 18 n'aurait envoye que sa premiere phrase.
    m = re.search(r"^PROMPT DE MOUVEMENT[^\n]*\n(.*?)(?=\n\s*(?:-{10,}|⚠|PROMPT )|\Z)",
                  bloc, re.S | re.M)
    if not m:
        sys.exit("  plan %02d : aucun bloc « PROMPT DE MOUVEMENT »" % n)
    return " ".join(m.group(1).split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", required=True)
    ap.add_argument("--plan", type=int, nargs="*")
    ap.add_argument("--reste", action="store_true",
                    help="tous les decors qui n'ont pas encore de prise")
    ap.add_argument("--simuler", action="store_true",
                    help="dit tout et n'envoie rien -- A LIRE AVANT DE PAYER")
    ap.add_argument("--modele", default="seedance", choices=sorted(MODELES))
    ap.add_argument("--fin-identique", dest="fin_identique", action="store_true",
                    help="H3 : la MEME image en premiere et en derniere image, pour que le cadre "
                         "ne puisse pas deriver (21 oct. 2026, plan 09 d'es-02 : H3 avancait la camera "
                         "malgre « the camera is locked on a tripod »)")
    a = ap.parse_args()
    choisir_modele(a.modele)

    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"),
                          encoding="utf-8"))
    ep = os.path.join(RACINE, "video", "episode-" + a.scene)
    prises = os.path.join(ep, "02-prises")

    decors = [p for p in d["plans"] if p["type"] == "decor"]
    if a.plan:
        decors = [p for p in decors if p["n"] in a.plan]
    elif a.reste:
        decors = [p for p in decors
                  if not any(f.startswith("plan%02d-" % p["n"])
                             for f in (os.listdir(prises)
                                       if os.path.isdir(prises) else []))]
    if not decors:
        sys.exit("  aucun plan de decor a faire.")

    queues = queues_particulieres(a.scene)
    if queues:
        print("  queues particulieres : %s"
              % ", ".join("plan %02d -> %.2f s" % (k, queues[k])
                          for k in sorted(queues)))

    lots, total = [], 0.0
    for p in decors:
        # ⚠️ L'EXTENSION ECRITE DANS LA SCENE NE FAIT PAS FOI. Les plans de
        # decor y portent « …jpg » alors que 01-images/ ne contient que des
        # PNG : le champ a garde l'extension d'une epoque ou les images
        # venaient d'Artlist. On resout donc sur le disque plutot que de
        # concatener -- et on refuse plutot que de deviner.
        base = os.path.splitext(p["image"])[0]
        img = next((c for c in (os.path.join(ep, "01-images", base + e)
                                for e in (".png", ".jpg", ".jpeg", ".webp"))
                    if os.path.exists(c)), None)
        if not img:
            sys.exit("  plan %02d : aucune image « %s.* » dans 01-images/"
                     % (p["n"], base))
        sec = duree_a_generer(p.get("duree_audio") or 0, queues.get(p["n"], QUEUE))
        cout = sec * PRIX
        total += cout
        lots.append((p, img, sec, cout, prompt_du_plan(a.scene, p["n"])))

    print("  modele %s" % MODELE)
    print("  %s · %s · audio DESACTIVE · %.4f $/s\n" % (RESOLUTION, "9:16", PRIX))
    for p, img, sec, cout, pr in lots:
        print("  plan %02d  %-28s narration %.2f s -> %2d s   %.2f $"
              % (p["n"], os.path.basename(img), p.get("duree_audio") or 0,
                 sec, cout))
        print("           %s" % (pr[:150] + ("…" if len(pr) > 150 else "")))
    print("\n  %d plan(s), %.2f $" % (len(lots), total))

    if a.simuler:
        print("\n  (simulation -- rien n'a ete envoye)")
        return

    os.makedirs(prises, exist_ok=True)
    cle = O.cle()
    for p, img, sec, cout, pr in lots:
        print("\n  plan %02d -> envoi" % p["n"])
        # Depot en deux temps, gratuit : seul l'appel au modele est facture.
        url, octets = O.deposer(img, "image/png" if img.lower().endswith(".png") else "image/jpeg", cle)
        print("           image deposee, %.1f Mo" % (octets / 1e6))
        corps = {"prompt": pr, "image_url": url, "resolution": RESOLUTION,
                 "duration": str(sec), "aspect_ratio": "9:16",
                 # ⚠️ voir l'entete : la piste inventee du modele n'a rien a
                 # faire ici, la voix vient d'ElevenLabs.
                 "generate_audio": False}
        if a.modele == "h3":
            # Ni aspect_ratio ni generate_audio dans son schema : le format
            # suit l'image (9:16), et une piste eventuelle est retiree au
            # telechargement.
            corps = {"prompt": pr, "image_url": url, "resolution": RESOLUTION,
                     "duration": sec, "prompt_expansion_mode": "disabled"}
            if a.fin_identique:
                corps["end_image_url"] = url
        soum = O._json(FILE, cle, corps)
        print("           requete %s" % soum.get("request_id", "?"))
        res = O.attendre(soum["status_url"], soum["response_url"], cle)
        lien = (res.get("video") or {}).get("url")
        if not lien:
            sys.exit("  reponse sans video : %s" % json.dumps(res)[:300])
        # Plusieurs prises par plan, comme partout : un modele video ne rend
        # jamais deux fois la meme chose, et on juge sur une serie.
        k = 1
        while os.path.exists(os.path.join(prises, "plan%02d-%02d.mp4" % (p["n"], k))):
            k += 1
        dst = os.path.join(prises, "plan%02d-%02d.mp4" % (p["n"], k))
        n_octets = O.telecharger(lien, dst)
        if a.modele == "h3":
            muet = dst + ".muet.mp4"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", dst, "-an", "-c:v", "copy", muet],
                           check=True)
            os.replace(muet, dst)
        print("  ecrit : %s  (%.1f Mo, %.2f $)"
              % (os.path.basename(dst), (n_octets or 0) / 1e6, cout))

    print("\n  Ensuite : REGARDER, puis python video/retenir.py --plans …")


main()
