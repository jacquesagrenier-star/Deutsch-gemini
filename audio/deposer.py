# -*- coding: utf-8 -*-
"""Depose les fichiers audio sur Firebase Hosting.

    python audio/deposer.py --verifier    # controle sans rien envoyer
    python audio/deposer.py               # depose

POURQUOI HOSTING PLUTOT QUE STORAGE
    - Aucune cle a proteger : Hosting s'authentifie par une connexion dans le
      navigateur, la ou Storage demande un fichier de compte de service, donc
      un secret de plus a ranger et a ne pas divulguer.
    - Un CDN. Hosting distribue depuis un reseau mondial ; Storage sert depuis
      une seule region, ce qui s'entend au demarrage d'un son quand on ecoute
      depuis la Turquie ou le Canada.
    - Compromis assume : 360 Mo de trafic par jour en gratuit contre 1 Go pour
      Storage. A ~9 Ko le fichier, cela represente environ 400 sessions par
      jour -- de quoi lancer, pas de quoi grandir. Le jour ou ca serre, c'est
      le forfait Blaze qu'il faut, pas un autre hebergeur.

CE QUE CE SCRIPT NE FAIT PAS
    Il n'installe rien et ne se connecte pas a ta place : ces deux gestes
    passent par ton navigateur et t'appartiennent. Il verifie, il compte, et
    il lance le depot.

    Il n'appelle JAMAIS `firebase deploy` tout court -- toujours
    `--only hosting`. Sans ce garde-fou, la commande redeploierait aussi les
    Cloud Functions du projet, qui n'ont rien demande.
"""
import io
import json
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOSSIER = os.path.join(RACINE, "audio", "mp3")
MANIFESTE = os.path.join(RACINE, "audio", "manifest.json")
PROJET = "deutschai-b6fbb"


def outil_present(nom):
    for ext in ("", ".cmd", ".exe"):
        try:
            subprocess.run([nom + ext, "--version"], capture_output=True, timeout=60)
            return nom + ext
        except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
            continue
    return None


def controler():
    """Renvoie (fichiers, octets) ou sort en expliquant ce qui manque."""
    if not os.path.isdir(DOSSIER):
        print("  Le dossier audio/mp3/ n'existe pas. Lance d'abord la generation.")
        sys.exit(1)
    fichiers = [f for f in os.listdir(DOSSIER) if f.endswith(".mp3")]
    octets = sum(os.path.getsize(os.path.join(DOSSIER, f)) for f in fichiers)
    if not fichiers:
        print("  Aucun fichier a deposer.")
        sys.exit(1)

    print("  fichiers : %d" % len(fichiers))
    print("  poids    : %.1f Mo" % (octets / 1048576.0))

    # Un fichier vide est un fichier que la generation a rate : mieux vaut le
    # voir ici que sur le telephone d'un utilisateur.
    vides = [f for f in fichiers
             if os.path.getsize(os.path.join(DOSSIER, f)) < 500]
    if vides:
        print("  ATTENTION : %d fichiers de moins de 500 octets, probablement"
              " rates :" % len(vides))
        for f in vides[:5]:
            print("      %s" % f)
        print("  Supprime-les et relance la generation, elle les refera.")

    # Croiser avec le manifeste : un fichier qu'aucune entree ne reclame ne
    # sera jamais joue, et signale que le manifeste a change depuis.
    if os.path.exists(MANIFESTE):
        with io.open(MANIFESTE, encoding="utf-8") as f:
            attendus = {e["id"] for e in json.load(f)}
        sur_disque = {f[:-4] for f in fichiers}
        orphelins = sur_disque - attendus
        if orphelins:
            print("  ATTENTION : %d fichiers qu'aucune entree du manifeste ne"
                  " reclame." % len(orphelins))
        print("  reconnus par le manifeste : %d" % len(sur_disque & attendus))
    return len(fichiers), octets


def main():
    print("  dossier  : audio/mp3/")
    fichiers, octets = controler()

    if "--verifier" in sys.argv:
        print("\n  (verification seule -- rien n'a ete envoye)")
        return

    firebase = outil_present("firebase")
    if not firebase:
        print("\n  firebase-tools n'est pas installe. Une seule fois :")
        print("      npm install -g firebase-tools")
        print("      firebase login")
        print("  Puis relance cette commande.")
        sys.exit(1)

    print("\n  depot sur le projet %s ..." % PROJET)
    # --only hosting : ne jamais toucher aux Cloud Functions du projet.
    code = subprocess.call([firebase, "deploy", "--only", "hosting",
                            "--project", PROJET], cwd=RACINE)
    if code != 0:
        print("\n  le depot a echoue (code %d)." % code)
        print("  Si c'est la premiere fois : firebase login, puis relance.")
        sys.exit(code)

    print("\n  Depose. Les fichiers sont a :")
    print("      https://%s.web.app/<empreinte>.mp3" % PROJET)
    print("\n  Il reste a poser cette adresse dans index.html :")
    print('      const AUDIO_BASE = "https://%s.web.app/";' % PROJET)


if __name__ == "__main__":
    main()
