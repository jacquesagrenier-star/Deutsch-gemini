# -*- coding: utf-8 -*-
"""Anime un plan chez fal : image + piste -> prise d'avatar. ET C'EST FACTURE.

    python video/omnihuman.py --scene 02-beim-buergeramt --plan 3 --simuler
    python video/omnihuman.py --scene 02-beim-buergeramt --plan 3
    python video/omnihuman.py --scene 02-beim-buergeramt --reste

CE QUE CA REMPLACE
    Jusqu'au 13 septembre 2026, chaque prise se faisait A LA MAIN dans
    l'interface de BytePlus (Vision AI Studio -> Dreamina Omnihuman 1.5) :
    televerser l'image, televerser la piste, coller le prompt, attendre,
    telecharger. Treize fois pour l'episode 2.

    Le compte BytePlus n'a jamais pu s'ouvrir -- le choix Personal/Business
    est irreversible et leur support renvoyait a un formulaire de vente.
    fal sert le MEME modele au MEME prix, par API. Le va-et-vient disparait.

⚠️ ET LE PROMPT DEVIENT UN FICHIER, ce qui est le vrai gain.
    Les prompts de l'episode 1 ont ete tapes dans un formulaire web et sont
    PERDUS : il n'en reste que le gabarit et un seul exemple complet, celui
    du plan 05. Ici le prompt vit dans _essai-avatar/prompts/planNN.txt,
    versionne, relisible, comparable d'un plan a l'autre. Une prise qu'on ne
    peut pas rejouer n'est pas une prise, c'est un accident heureux.

LE PANIER VIENT DE preparer_avatar.py, ON NE LE REFABRIQUE PAS
    _a-televerser/planNN-<image>.jpg   l'image allegee
    _a-televerser/planNN-pleine.mp3    la piste tiree du clip DEJA MONTE
    ⚠️ Ne jamais raccourcir la piste : le silence final est la marge dont la
       bouche a besoin pour se refermer (~1,4 s, mesure au plan 16).

CE QUE LE MODELE ACCEPTE  (fal-ai/bytedance/omnihuman/v1.5)
    image_url    requis     l'image de reference
    audio_url    requis     NOTRE piste -- il ne synthetise pas la voix
    prompt       optionnel  le gabarit de gabarit-prompt.txt
    resolution   1080p (audio < 30 s) ou 720p (audio < 60 s)
    turbo_mode   plus rapide, qualite en leger retrait
    ⚠️ PAS DE PARAMETRE DE FORMAT D'IMAGE : c'est l'image de reference qui
       impose le cadre. Nos planches en portrait donnent du portrait.

LE PRIX EST AU TEMPS DE SORTIE, ET LA SORTIE SUIT LA PISTE
    0,16 $ la seconde, facture sur la duree que le modele renvoie -- pas sur
    la duree demandee. Une piste de 4 s coute 0,64 $. Le recu de chaque plan
    est ecrit dans _essai-avatar/planNN-fal.json : identifiant de requete,
    duree facturee, cout. C'est ce qui permet de verifier un releve.

⚠️ LE PLAFOND EXISTE POUR UNE RAISON. Un --reste distrait sur treize plans
   engage 8,32 $ en une touche. Le script refuse de depasser --plafond
   (2,00 $ par defaut) et annonce le total AVANT d'appeler quoi que ce soit.

LA CLE N'EST PAS DANS LE CODE
    fal.secret a la racine (ignore par git, *.secret ligne 13) ou la variable
    d'environnement FAL_KEY. Le depot est public.
"""
import argparse
import glob
import io
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import montage as M                                         # noqa: E402

MODELE = "fal-ai/bytedance/omnihuman/v1.5"
PRIX = 0.16                      # $ la seconde, releve sur la fiche du modele
INITIER = "https://rest.alpha.fal.ai/storage/upload/initiate"
FILE = "https://queue.fal.run/" + MODELE

# Les limites viennent de la fiche du modele : au-dela, il refuse.
DUREE_MAX = {"1080p": 30.0, "720p": 60.0}


# --------------------------------------------------------------------------
#  La cle

def cle():
    """fal.secret d'abord, la variable d'environnement ensuite. Meme geste que
    sync.secret et elevenlabs.secret."""
    c = (os.environ.get("FAL_KEY") or "").strip()
    chemin = os.path.join(RACINE, "fal.secret")
    if not c and os.path.exists(chemin):
        c = io.open(chemin, encoding="utf-8-sig").read().strip()
    if not c or len(c.split()) > 1 or ":" not in c:
        sys.exit("  Cle absente ou mal formee. Colle-la seule sur une ligne dans\n"
                 "  fal.secret, a la racine du projet. Forme attendue : uuid:hexa.")
    return c


# --------------------------------------------------------------------------
#  Le reseau

def _json(url, cle_api, corps=None, methode=None, essais=3):
    """urllib plutot qu'une dependance : le depot n'en a aucune, et trois
    appels ne justifient pas d'en ajouter une."""
    d = json.dumps(corps).encode("utf-8") if corps is not None else None
    for i in range(essais):
        r = urllib.request.Request(url, data=d, method=methode, headers={
            "Authorization": "Key " + cle_api,
            "Content-Type": "application/json",
        })
        try:
            with urllib.request.urlopen(r, timeout=120) as rep:
                return json.loads(rep.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            corps_err = e.read().decode("utf-8", "replace")[:400]
            # 4xx : la requete est fautive, reessayer ne repare rien.
            if e.code < 500 or i == essais - 1:
                sys.exit("  HTTP %s sur %s\n  %s" % (e.code, url, corps_err))
        except Exception as e:
            if i == essais - 1:
                sys.exit("  %s sur %s : %s" % (type(e).__name__, url, e))
        time.sleep(2 * (i + 1))


def deposer(chemin, type_mime, cle_api):
    """Depot en deux temps : on demande une URL signee, on y pousse les
    octets. GRATUIT -- seul l'appel au modele est facture."""
    rep = _json(INITIER, cle_api, {"content_type": type_mime,
                                   "file_name": os.path.basename(chemin)})
    octets = io.open(chemin, "rb").read()
    r = urllib.request.Request(rep["upload_url"], data=octets, method="PUT",
                               headers={"Content-Type": type_mime})
    with urllib.request.urlopen(r, timeout=300) as _:
        pass
    return rep["file_url"], len(octets)


def attendre(status_url, response_url, cle_api, bavard=True):
    """On suit les URL que la soumission nous a RENDUES, on ne les reconstruit
    pas : le chemin de file d'attente d'un modele a sous-chemins ne se devine
    pas depuis son identifiant."""
    debut = time.time()
    vu = None
    while True:
        e = _json(status_url, cle_api)
        s = e.get("status")
        if s != vu and bavard:
            print("    %-12s %4.0f s" % (s, time.time() - debut))
            vu = s
        if s == "COMPLETED":
            return _json(response_url, cle_api)
        if s in ("FAILED", "CANCELLED", "ERROR"):
            sys.exit("  la requete a echoue : %s" % json.dumps(e)[:400])
        if time.time() - debut > 900:
            sys.exit("  aucune reponse apres 15 minutes. Requete abandonnee ;\n"
                     "  verifie le tableau de bord avant de relancer, elle peut\n"
                     "  avoir abouti et etre facturee.")
        time.sleep(3)


def telecharger(url, dst):
    with urllib.request.urlopen(url, timeout=600) as rep:
        octets = rep.read()
    io.open(dst, "wb").write(octets)
    return len(octets)


# --------------------------------------------------------------------------
#  Le panier d'un plan

def dossiers(scene):
    ep = os.path.join(RACINE, "video", "episode-%s" % scene)
    if not os.path.isdir(ep):
        sys.exit("  episode introuvable : %s" % ep)
    return ep, os.path.join(ep, "_a-televerser"), os.path.join(ep, "_essai-avatar")


def panier(tel, essai, n):
    """Retourne (image, piste, prompt) ou explique precisement ce qui manque.
    Un message qui dit seulement « fichier absent » fait perdre dix minutes."""
    imgs = [f for f in sorted(glob.glob(os.path.join(tel, "plan%02d-*.jpg" % n)))
            if not f.endswith("-pleine.mp3")]
    mp3 = os.path.join(tel, "plan%02d-pleine.mp3" % n)
    pr = os.path.join(essai, "prompts", "plan%02d.txt" % n)
    manque = []
    if not imgs:
        manque.append("  l'image : aucun %s/plan%02d-*.jpg\n"
                      "    -> python video/preparer_avatar.py --plan %d" % (
                          os.path.basename(tel), n, n))
    if not os.path.exists(mp3):
        manque.append("  la piste : %s absent\n"
                      "    -> python video/preparer_avatar.py --plan %d" % (
                          os.path.basename(mp3), n))
    if not os.path.exists(pr):
        manque.append("  le prompt : %s absent\n"
                      "    -> l'ecrire d'apres video/episode-01-ankunft-berlin/"
                      "_essai-avatar/notes/gabarit-prompt.txt" % (
                          os.path.relpath(pr, RACINE)))
    if manque:
        sys.exit("  plan %d -- il manque :\n%s" % (n, "\n".join(manque)))
    return imgs[0], mp3, pr


_FF = [None]


def duree_mp3(chemin):
    """On mesure, on ne calcule pas : a debit variable, la taille du fichier ne
    dit pas sa duree, et c'est a la seconde qu'on est facture.

    ⚠️ Par montage.duree(), pas par ffprobe. Le depot localise ffmpeg via
    imageio_ffmpeg et ne suppose rien du PATH -- un ffprobe qui se trouve la
    marche jusqu'au jour ou il n'y est plus."""
    if _FF[0] is None:
        _FF[0] = M.ffmpeg()
    return M.duree(_FF[0], chemin) or 0.0


# --------------------------------------------------------------------------

def un_plan(scene, n, cle_api, resolution, turbo, simuler, refaire):
    ep, tel, essai = dossiers(scene)
    img, mp3, pr = panier(tel, essai, n)
    sortie = os.path.join(essai, "plan%02d-omnihuman.mp4" % n)
    recu = os.path.join(essai, "plan%02d-fal.json" % n)

    if os.path.exists(sortie) and not refaire:
        print("  plan %d : deja la (%s). --refaire pour la remplacer."
              % (n, os.path.basename(sortie)))
        return 0.0

    d = duree_mp3(mp3)
    if d > DUREE_MAX[resolution]:
        sys.exit("  plan %d : piste de %.2f s, le maximum est %.0f s en %s.\n"
                 "  Passer en 720p, ou couper le plan en deux."
                 % (n, d, DUREE_MAX[resolution], resolution))
    print("  plan %d : %s + %s  (%.2f s, ~%.2f $)"
          % (n, os.path.basename(img), os.path.basename(mp3), d, d * PRIX))

    prompt = io.open(pr, encoding="utf-8").read().strip()
    if simuler:
        print("    SIMULATION -- rien n'est appele, rien n'est facture.")
        print("    prompt : %d mots, %d caracteres" % (len(prompt.split()), len(prompt)))
        return 0.0

    os.makedirs(essai, exist_ok=True)
    u_img, o_img = deposer(img, "image/jpeg", cle_api)
    u_mp3, o_mp3 = deposer(mp3, "audio/mpeg", cle_api)
    print("    depose : image %.1f Mo, piste %.0f ko" % (o_img / 1e6, o_mp3 / 1e3))

    corps = {"image_url": u_img, "audio_url": u_mp3, "prompt": prompt,
             "resolution": resolution}
    if turbo:
        corps["turbo_mode"] = True

    soum = _json(FILE, cle_api, corps)
    print("    requete %s" % soum.get("request_id", "?"))
    res = attendre(soum["status_url"], soum["response_url"], cle_api)

    facturee = float(res.get("duration") or d)
    cout = facturee * PRIX
    octets = telecharger(res["video"]["url"], sortie)
    print("    -> %s  (%.1f Mo, %.2f s facturees, %.2f $)"
          % (os.path.basename(sortie), octets / 1e6, facturee, cout))

    io.open(recu, "w", encoding="utf-8").write(json.dumps({
        "modele": MODELE, "request_id": soum.get("request_id"),
        "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "image": os.path.basename(img), "piste": os.path.basename(mp3),
        "resolution": resolution, "turbo": bool(turbo),
        "duree_piste": round(d, 3), "duree_facturee": round(facturee, 3),
        "cout_usd": round(cout, 4), "prompt": prompt,
    }, ensure_ascii=False, indent=1))
    return cout


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--scene", default="02-beim-buergeramt")
    p.add_argument("--plan", type=int, nargs="+")
    p.add_argument("--reste", action="store_true",
                   help="tous les plans dont le panier existe et la prise non")
    p.add_argument("--resolution", default="1080p", choices=["1080p", "720p"])
    p.add_argument("--turbo", action="store_true")
    p.add_argument("--simuler", action="store_true",
                   help="tout verifier sans rien appeler ni facturer")
    p.add_argument("--refaire", action="store_true")
    p.add_argument("--plafond", type=float, default=2.0,
                   help="dollars ; le lot est refuse au-dela (defaut 2,00)")
    a = p.parse_args()

    ep, tel, essai = dossiers(a.scene)
    if a.reste:
        ns = []
        for f in sorted(glob.glob(os.path.join(tel, "plan*-pleine.mp3"))):
            n = int(os.path.basename(f)[4:6])
            if a.refaire or not os.path.exists(
                    os.path.join(essai, "plan%02d-omnihuman.mp4" % n)):
                ns.append(n)
    elif a.plan:
        ns = a.plan
    else:
        sys.exit("  Preciser --plan N [N...] ou --reste.")
    if not ns:
        print("  rien a faire : toutes les prises sont la.")
        return

    # Le devis AVANT le premier appel : c'est la seule occasion de reculer.
    total = 0.0
    for n in ns:
        try:
            _, mp3, _ = panier(tel, essai, n)
            total += duree_mp3(mp3) * PRIX
        except SystemExit:
            raise
    print("%d plan(s) : %s" % (len(ns), " ".join(str(n) for n in ns)))
    print("devis : %.2f $  (plafond %.2f $)" % (total, a.plafond))
    if total > a.plafond and not a.simuler:
        sys.exit("  Au-dessus du plafond. Relance avec --plafond %.2f si c'est\n"
                 "  voulu, ou traite les plans par petits lots." % (total + 0.01))

    c = cle() if not a.simuler else ""
    depense = 0.0
    for n in ns:
        depense += un_plan(a.scene, n, c, a.resolution, a.turbo,
                           a.simuler, a.refaire)
    print("depense reelle : %.2f $" % depense)


if __name__ == "__main__":
    main()
