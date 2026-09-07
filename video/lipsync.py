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


def appel(url, cle_api, corps=None, typ=None, methode="GET"):
    req = urllib.request.Request(url, data=corps, method=methode,
                                 headers={"x-api-key": cle_api})
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

    src = os.path.join(RACINE, "video", a.scene)
    aud = os.path.join(RACINE, "audio", "scenes", a.scene)
    dst = os.path.join(src, "final")
    os.makedirs(dst, exist_ok=True)

    travail = []
    for p in plans:
        v = os.path.join(src, "plan%02d-%s.mp4" % (p["n"], p["locuteur"]))
        s = os.path.join(aud, "%02d-%s.mp3" % (p["n"], p["locuteur"]))
        if not os.path.exists(v):
            sys.exit("  video manquante : %s" % os.path.basename(v))
        if not os.path.exists(s):
            sys.exit("  audio manquant : %s" % os.path.basename(s))
        travail.append((p, v, s))

    secondes = sum(p["duree"] for p, _, _ in travail)
    print("  %s — %d plans, %d s" % (d["situation"], len(travail), secondes))
    print("  modele %s : environ %.2f $" % (a.modele, secondes * TARIF[a.modele]))
    if not a.pour_de_vrai:
        print("\n  Essai a blanc. Relancer avec --pour-de-vrai pour depenser.")
        return

    k = cle()
    etat_f = os.path.join(dst, "etat.json")
    etat = json.load(io.open(etat_f, encoding="utf-8")) if os.path.exists(etat_f) else {}

    def sauver():
        io.open(etat_f, "w", encoding="utf-8", newline="").write(
            json.dumps(etat, ensure_ascii=False, indent=2) + "\n")

    # 1. soumettre ce qui ne l'est pas encore
    for p, v, s in travail:
        n = str(p["n"])
        if etat.get(n, {}).get("id"):
            continue
        corps, typ = multipart({"model": a.modele}, {"video": v, "audio": s})
        print("  plan%02d envoi..." % p["n"], end="", flush=True)
        r = appel(API, k, corps, typ, "POST")
        etat[n] = {"id": r.get("id"), "statut": r.get("status")}
        sauver()   # AVANT toute autre chose : un identifiant perdu est une generation payee deux fois
        print(" %s" % r.get("id", "?")[:8])

    # 2. attendre, puis rapatrier
    restants = {n for n, x in etat.items() if not x.get("fichier")}
    print("\n  attente de %d generation(s)" % len(restants))
    debut = time.time()
    while restants and time.time() - debut < 1800:
        for n in sorted(restants, key=int):
            r = appel(API + "/" + etat[n]["id"], k)
            st = r.get("status")
            etat[n]["statut"] = st
            if st == "COMPLETED" and r.get("outputUrl"):
                p = next(x for x in plans if x["n"] == int(n))
                f = os.path.join(dst, "plan%02d.mp4" % p["n"])
                with urllib.request.urlopen(r["outputUrl"], timeout=300) as w:
                    open(f, "wb").write(w.read())
                etat[n]["fichier"] = os.path.basename(f)
                restants.discard(n)
                print("  plan%02d  %d Ko" % (p["n"], os.path.getsize(f) // 1024))
            elif st in ("FAILED", "REJECTED"):
                etat[n]["erreur"] = r.get("error") or st
                restants.discard(n)
                print("  plan%02s  ECHEC : %s" % (n, etat[n]["erreur"]))
            sauver()
        if restants:
            time.sleep(15)

    faits = [x for x in etat.values() if x.get("fichier")]
    print("\n  %d/%d plans synchronises dans video/%s/final/"
          % (len(faits), len(travail), a.scene))
    for n, x in sorted(etat.items(), key=lambda y: int(y[0])):
        if not x.get("fichier"):
            print("     plan%02s : %s" % (n, x.get("erreur") or x.get("statut")))


if __name__ == "__main__":
    main()
