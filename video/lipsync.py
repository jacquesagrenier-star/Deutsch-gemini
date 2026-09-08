# -*- coding: utf-8 -*-
"""Passe les plans d'une scene au lip-sync de sync.so.

    python video/lipsync.py --scene 01-ankunft-berlin              # a blanc
    python video/lipsync.py --scene 01-ankunft-berlin --pour-de-vrai

A BLANC PAR DEFAUT, comme scene_audio.py : chaque seconde envoyee est
facturee, et un lancement par megarde se paie.

IL REPREND OU IL S'ETAIT ARRETE, ET C'EST LE POINT IMPORTANT
    Chaque generation soumise recoit un identifiant, note aussitot dans
    etat.json. Une relance ne resoumet donc jamais un plan deja envoye : elle
    va reprendre son identifiant et redemander ou il en est.

    Sans ca, une coupure reseau au onzieme plan sur douze couterait douze
    generations de plus a la reprise -- on paierait deux fois un travail deja
    fait, et sans le savoir.

CE QUE FAIT LE LIP-SYNC, ET CE QU'IL NE FAIT PAS
    Il reecrit la bouche du personnage pour qu'elle suive l'audio fourni. Le
    reste de l'image ne bouge pas. C'est pour cela que nos clips sont muets et
    que le personnage n'y « dit » rien : ce qu'il semblait articuler n'a aucune
    importance, seule compte la nettete de son visage.
"""
import argparse
import io
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.request
import uuid

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.sync.so/v2/generate"
TARIF = {"lipsync-2": 0.04, "lipsync-2-pro": 0.08}


def cle():
    chemin = os.path.join(RACINE, "sync.secret")
    c = (os.environ.get("SYNC_API_KEY") or "").strip()
    if not c and os.path.exists(chemin):
        c = io.open(chemin, encoding="utf-8").read().strip()
    if not c or len(c.split()) > 1 or len(c) < 20:
        sys.exit("  Cle absente ou mal formee. Colle-la seule sur une ligne dans\n"
                 "  sync.secret, a la racine du projet.")
    return c


def multipart(champs, fichiers):
    """Encode un corps multipart. urllib ne sait pas le faire, et ajouter une
    dependance pour trois lignes ne vaut pas le coup."""
    b = "----wortando" + uuid.uuid4().hex
    out = []
    for k, v in champs.items():
        out.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"\r\n\r\n%s\r\n"
                    % (b, k, v)).encode("utf-8"))
    for k, chemin in fichiers.items():
        nom = os.path.basename(chemin)
        typ = mimetypes.guess_type(nom)[0] or "application/octet-stream"
        out.append(("--%s\r\nContent-Disposition: form-data; name=\"%s\"; filename=\"%s\"\r\n"
                    "Content-Type: %s\r\n\r\n" % (b, k, nom, typ)).encode("utf-8"))
        out.append(open(chemin, "rb").read())
        out.append(b"\r\n")
    out.append(("--%s--\r\n" % b).encode("utf-8"))
    return b"".join(out), "multipart/form-data; boundary=" + b


# Cloudflare renvoie 403 « error code: 1010 » sur la signature par defaut
# d'urllib -- « Python-urllib/3.x ». Ce n'est pas la cle qui est refusee, c'est
# le client : un agent ordinaire suffit a passer, et rien n'est soumis tant
# qu'on ne passe pas, donc l'echec ne coute rien.
AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
         "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def appel(url, cle_api, corps=None, typ=None, methode="GET"):
    req = urllib.request.Request(url, data=corps, method=methode,
                                 headers={"x-api-key": cle_api,
                                          "User-Agent": AGENT,
                                          "Accept": "application/json"})
    if typ:
        req.add_header("Content-Type", typ)
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        raise RuntimeError("HTTP %d — %s" % (e.code, detail))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--modele", default="lipsync-2", choices=sorted(TARIF))
    ap.add_argument("--pour-de-vrai", action="store_true")
    a = ap.parse_args()

    d = json.load(io.open(os.path.join(RACINE, "scenes", a.scene + ".json"), encoding="utf-8"))
    plans = [p for p in d["plans"] if p["type"] == "replique"]

    # L'arborescence de l'episode : les clips muets retenus sont dans
    # 03-final/, les plans synchronises vont a cote dans 04-lipsync/. On ne
    # remplace jamais un clip d'origine -- une prise Artlist ne se refait pas
    # a l'identique, et un lip-sync rate ne doit rien pouvoir ecraser.
    src = os.path.join(RACINE, "video", "episode-" + a.scene, "03-final")
    aud = os.path.join(RACINE, "audio", "scenes", a.scene)
    dst = os.path.join(RACINE, "video", "episode-" + a.scene, "04-lipsync")
    os.makedirs(dst, exist_ok=True)

    travail = []
    for p in plans:
        v = os.path.join(src, "plan%02d.mp4" % p["n"])
        s = os.path.join(aud, "%02d-%s.mp3" % (p["n"], p["locuteur"]))
        if not os.path.exists(v):
            sys.exit("  video manquante : 03-final/%s" % os.path.basename(v))
        if not os.path.exists(s):
            sys.exit("  audio manquant : %s" % os.path.basename(s))
        travail.append((p, v, s))

    secondes = sum(p["duree"] for p, _, _ in travail)
    print("  %s — %d plans a synchroniser sur %d"
          % (d["situation"], len(travail), len(d["plans"])))
    for p, _, _ in travail:
        print("    plan%02d  %-5s %2d s  %s"
              % (p["n"], p["locuteur"], p["duree"], p.get("de", "")[:46]))
    print("  %d s au total — modele %s : environ %.2f $"
          % (secondes, a.modele, secondes * TARIF[a.modele]))
    if not a.pour_de_vrai:
        print("\n  Essai a blanc. Relancer avec --pour-de-vrai pour depenser.")
        return

    k = cle()
    etat_f = os.path.join(dst, "etat.json")
    etat = json.load(io.open(etat_f, encoding="utf-8")) if os.path.exists(etat_f) else {}

    def sauver():
        io.open(etat_f, "w", encoding="utf-8", newline="").write(
            json.dumps(etat, ensure_ascii=False, indent=2) + "\n")

    # UN PLAN A LA FOIS. Le plan gratuit de sync.so n'autorise qu'une
    # generation simultanee : envoyer les douze d'un coup fait echouer la
    # deuxieme sur un 429, et les dix suivantes avec elle. On soumet donc,
    # on attend, on rapatrie, puis on passe au suivant.
    for p, v, s_aud in travail:
        n = str(p["n"])
        if etat.get(n, {}).get("fichier"):
            print("  plan%02d  deja fait" % p["n"])
            continue

        if not etat.get(n, {}).get("id"):
            corps, typ = multipart({"model": a.modele}, {"video": v, "audio": s_aud})
            print("  plan%02d envoi..." % p["n"], end="", flush=True)
            r = appel(API, k, corps, typ, "POST")
            etat[n] = {"id": r.get("id"), "statut": r.get("status")}
            sauver()   # AVANT tout le reste : un identifiant perdu est une generation payee deux fois
            print(" %s" % (r.get("id") or "?")[:8], end="", flush=True)

        debut = time.time()
        while time.time() - debut < 900:
            time.sleep(10)
            r = appel(API + "/" + etat[n]["id"], k)
            st = r.get("status")
            etat[n]["statut"] = st
            sauver()
            if st == "COMPLETED" and r.get("outputUrl"):
                f = os.path.join(dst, "plan%02d.mp4" % p["n"])
                dl = urllib.request.Request(r["outputUrl"], headers={"User-Agent": AGENT})
                with urllib.request.urlopen(dl, timeout=300) as w:
                    open(f, "wb").write(w.read())
                etat[n]["fichier"] = os.path.basename(f)
                sauver()
                print("  ->  %d Ko" % (os.path.getsize(f) // 1024))
                break
            if st in ("FAILED", "REJECTED"):
                etat[n]["erreur"] = r.get("error") or st
                sauver()
                print("  ->  ECHEC : %s" % etat[n]["erreur"])
                break
        else:
            print("  ->  toujours en cours apres 15 min, on passe")

    faits = [x for x in etat.values() if x.get("fichier")]
    print("\n  %d/%d plans synchronises dans video/episode-%s/04-lipsync/"
          % (len(faits), len(travail), a.scene))
    if len(faits) == len(travail):
        print("  montage.py les prend tout seul : il regarde 04-lipsync avant 03-final.")
    for n, x in sorted(etat.items(), key=lambda y: int(y[0])):
        if not x.get("fichier"):
            print("     plan%02s : %s" % (n, x.get("erreur") or x.get("statut")))


if __name__ == "__main__":
    main()
