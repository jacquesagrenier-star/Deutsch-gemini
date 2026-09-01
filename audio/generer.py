# -*- coding: utf-8 -*-
"""Fabrique les fichiers audio allemands via l'API ElevenLabs.

    python audio/generer.py --essai
        Genere les mots difficiles dans LES DEUX modeles, pour trancher a
        l'oreille. Une centaine de credits.

    python audio/generer.py --niveaux A1,A2 --modele v2 --plafond 110000
        Genere pour de bon. Reprenable : relancer saute ce qui existe deja.

    python audio/generer.py --niveaux A1 --a-blanc
        Compte et n'appelle rien.

REPRENABLE PAR CONSTRUCTION
    15 622 appels reseau ne se terminent pas du premier coup : coupure, quota,
    lenteur passagere. Le script ne tient donc aucun etat -- il regarde ce qui
    est deja sur le disque et fait le reste. On peut l'interrompre au clavier
    et le relancer le mois suivant, il reprend ou il en etait.

LA CLE N'EST PAS DANS LE CODE
    Elle est lue dans elevenlabs.secret (ignore par git) ou dans la variable
    d'environnement ELEVENLABS_API_KEY. Elle ne doit jamais entrer dans
    index.html : l'application est statique et publique, tout ce qu'elle
    contient est lisible par n'importe qui.
"""
import argparse
import io
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORTIE = os.path.join(RACINE, "audio", "mp3")
MANIFESTE = os.path.join(RACINE, "audio", "manifest.json")

# Nadja - Authentic and Clear. C'est l'identifiant qui fait foi, pas le nom :
# une voix de la Voice Library peut etre renommee ou retiree par son createur.
VOIX = "iOLZqmXTaFktMrY5oZ2z"

MODELES = {
    "v2":    ("eleven_multilingual_v2", 1.0),   # 1 credit par caractere
    "flash": ("eleven_flash_v2_5",      0.5),   # moitie prix
}

# 64 kbit/s mono suffit pour de la parole et divise le poids par deux face au
# 128 : sur huit heures d'audio, 230 Mo au lieu de 460.
FORMAT = "mp3_44100_64"

# Fixes pour tout le corpus. La stabilite est haute a dessein : la generation
# n'est pas deterministe, et sur 15 622 fichiers on ne peut ni tout reecouter
# ni choisir les bonnes prises. Mieux vaut resserrer la distribution que
# chercher l'exception reussie.
REGLAGES = {"stability": 0.75, "similarity_boost": 0.75,
            "style": 0.0, "use_speaker_boost": True}
SEED = 20260901          # rend une prise reproductible a l'identique

# Les mots ou une synthese allemande se casse : umlaut, les deux ch, le
# durcissement final, la longueur de voyelle, le ss, un compose long.
ESSAI = ["Frühstück", "Mädchen", "Buch", "Tag", "Staat", "Stadt", "Straße",
         "Krankenversicherung", "Die Ahnentafel reicht bis 1750 zurück.",
         "Die Krankenschwester kümmert sich um die Patienten."]


def cle_api():
    cle = (os.environ.get("ELEVENLABS_API_KEY") or "").strip()
    if not cle:
        chemin = os.path.join(RACINE, "elevenlabs.secret")
        if os.path.exists(chemin):
            with io.open(chemin, encoding="utf-8") as f:
                cle = f.read().strip()
    # Le fichier existe souvent avant la cle : on le cree vide pour eviter le
    # piege de Notepad, qui enregistrerait "elevenlabs.secret.txt".
    if not cle:
        print("Cle absente. Ouvre elevenlabs.secret a la racine du projet et\n"
              "colle la cle dedans, seule, sur une ligne. Ou exporte\n"
              "ELEVENLABS_API_KEY.")
        sys.exit(1)
    if len(cle.split()) > 1 or len(cle) < 20:
        print("Le contenu d'elevenlabs.secret ne ressemble pas a une cle\n"
              "(%d caracteres, %d mots). Elle doit y etre seule, sans guillemets\n"
              "ni prefixe." % (len(cle), len(cle.split())))
        sys.exit(1)
    return cle


def synthetiser(texte, modele, cle):
    """Renvoie les octets MP3. Retente sur 429 et sur les erreurs serveur."""
    url = ("https://api.elevenlabs.io/v1/text-to-speech/%s?output_format=%s"
           % (VOIX, FORMAT))
    corps = json.dumps({"text": texte, "model_id": modele,
                        "voice_settings": REGLAGES, "seed": SEED}).encode("utf-8")
    for essai in range(5):
        req = urllib.request.Request(url, data=corps, method="POST", headers={
            "xi-api-key": cle, "Content-Type": "application/json",
            "Accept": "audio/mpeg"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:200]
            # 429 = cadence trop rapide, 5xx = hoquet de leur cote : on attend.
            # 401/403 = cle ou permission : inutile d'insister.
            if e.code in (429, 500, 502, 503, 504) and essai < 4:
                attente = 2 ** essai
                print("    HTTP %d, nouvelle tentative dans %ds" % (e.code, attente))
                time.sleep(attente)
                continue
            raise RuntimeError("HTTP %d : %s" % (e.code, detail))
        except urllib.error.URLError as e:
            if essai < 4:
                time.sleep(2 ** essai)
                continue
            raise RuntimeError("reseau : %s" % e)
    raise RuntimeError("cinq tentatives echouees")


def charger_manifeste():
    if not os.path.exists(MANIFESTE):
        print("Manifeste absent. Lance d'abord :\n"
              "    python audio/manifest.py --ecrire")
        sys.exit(1)
    with io.open(MANIFESTE, encoding="utf-8") as f:
        return json.load(f)


def a_produire(niveaux):
    """Ce qui manque encore sur le disque, pour ces niveaux.

    Extrait de main() pour que solde.py compte exactement la meme chose : deux
    facons de repondre a « combien en reste-t-il » finiraient par diverger, et
    c'est ce chiffre qui decide d'un achat de credits.
    """
    voulus = [e for e in charger_manifeste() if e["niveau"] in niveaux]
    restants = [e for e in voulus
                if not os.path.exists(os.path.join(SORTIE, e["id"] + ".mp3"))]
    return voulus, restants


def mode_essai(cle):
    """Les memes mots dans les deux modeles, pour comparer a l'oreille."""
    dossier = os.path.join(RACINE, "audio", "essai")
    os.makedirs(dossier, exist_ok=True)
    total = 0
    for court, (modele, taux) in MODELES.items():
        for i, texte in enumerate(ESSAI, 1):
            nom = "%02d_%s.mp3" % (i, court)
            chemin = os.path.join(dossier, nom)
            if os.path.exists(chemin):
                print("  = %s" % nom)
                continue
            octets = synthetiser(texte, modele, cle)
            with open(chemin, "wb") as f:
                f.write(octets)
            total += len(texte) * taux
            print("  + %-16s %-40s %6d o" % (nom, texte[:38], len(octets)))
    print("\n  %d fichiers dans audio/essai/, environ %d credits." %
          (len(ESSAI) * 2, int(total)))
    print("  Ecoute les paires 01_v2 / 01_flash, etc. Si l'ecart ne s'entend")
    print("  pas, Flash divise par deux le cout des 15 622 fichiers.")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--niveaux", default="A1")
    p.add_argument("--modele", default="v2", choices=sorted(MODELES))
    p.add_argument("--plafond", type=int, default=110000,
                   help="credits a ne pas depasser sur cette execution")
    p.add_argument("--a-blanc", action="store_true")
    p.add_argument("--essai", action="store_true")
    a = p.parse_args()

    if a.essai:
        mode_essai(cle_api())
        return

    modele, taux = MODELES[a.modele]
    niveaux = a.niveaux.split(",")
    os.makedirs(SORTIE, exist_ok=True)

    voulus, restants = a_produire(niveaux)
    cout = int(sum(len(e["texte"]) for e in restants) * taux)

    print("  niveaux %s | modele %s | %d entrees, %d deja faites"
          % (",".join(niveaux), a.modele, len(voulus), len(voulus) - len(restants)))
    print("  a produire : %d fichiers, environ %d credits" % (len(restants), cout))
    if cout > a.plafond:
        print("  -> depasse le plafond de %d : le script s'arretera en route."
              % a.plafond)
    if a.a_blanc:
        print("\n  (a blanc -- rien n'a ete appele)")
        return
    if not restants:
        print("\n  rien a faire.")
        return

    # La cle n'est reclamee qu'ici : on doit pouvoir chiffrer un lot avant
    # meme d'avoir cree la cle.
    cle = cle_api()

    depense, faits, debut = 0, 0, time.time()
    try:
        for e in restants:
            prix = len(e["texte"]) * taux
            if depense + prix > a.plafond:
                print("\n  plafond atteint. Relance plus tard, la reprise est"
                      " automatique.")
                break
            octets = synthetiser(e["texte"], modele, cle)
            with open(os.path.join(SORTIE, e["id"] + ".mp3"), "wb") as f:
                f.write(octets)
            depense += prix
            faits += 1
            if faits % 25 == 0 or faits == len(restants):
                ecoule = time.time() - debut
                reste = (len(restants) - faits) * ecoule / faits
                print("  %5d/%d  %6d credits  reste ~%d min"
                      % (faits, len(restants), int(depense), int(reste / 60)))
    except KeyboardInterrupt:
        print("\n  interrompu -- les fichiers deja ecrits sont conserves.")
    except RuntimeError as err:
        print("\n  ARRET : %s" % err)
        print("  Les fichiers deja ecrits sont conserves ; relance pour"
              " reprendre.")

    print("\n  %d fichiers produits, environ %d credits depenses." % (faits, int(depense)))
    print("  Dossier : audio/mp3/")


if __name__ == "__main__":
    main()
