# -*- coding: utf-8 -*-
"""Fabrique les fichiers audio ANGLAIS : une voix americaine, A1-A2.

    python audio/generer_en.py --a-blanc                 # ce que ca couterait, ne depense rien
    python audio/generer_en.py --plafond 110000          # produit (accord de Jacques requis)
    python audio/generer_en.py --normaliser              # sonie, apres coup

ACCORDE PAR JACQUES LE 29 OCT. 2026 : « J'ai ajoute des credits, donc fais les
voix pour A1. Et A2. » Seulement l'AMERICAIN (la base, decidee le 27 oct.) et
seulement A1-A2 : le britannique et B1-C1 se feront sur sa demande. Le reste
de l'anglais garde la voix du telephone -- l'app la prend des qu'un fichier
manque (voir LANGUE_ANGLAIS.audio dans index.html).

LA VOIX est celle que Jacques choisit au comparatif a l'aveugle
(anglais/outils/echantillons_voix.py, audio/a_ecouter_voix/anglais_us/). Tant
qu'elle n'est pas choisie, VOIX["us"] est vide et le script refuse de tourner.

MULTILINGUAL V2 SEULEMENT. Flash est interdit depuis le 12 oct. 2026 (voix
« metallique ») : --modele n'existe pas ici, a dessein.

CE QUI EST REPRIS DE L'ESPAGNOL, tel quel (generer_es.py) :
  - les reglages (stabilite 0,75, graine fixe, mp3 64 kbit/s) ;
  - LES MOTS SEULS DANS UNE PORTEUSE : « Word: <mot>. » a vitesse 0,80, puis
    on garde ce qui suit la plus grande pause (recouper.py). Seulement les
    textes SANS espace ;
  - les nombres en lettres (audio/lectures/en.json) : la voix ne recoit
    jamais de chiffres, le fichier garde le nom sha1(texte ECRIT)[:16] ;
  - la normalisation de sonie (generer_es.normaliser), original archive.

L'INVENTAIRE est anglais/outils/manifest_voix.py : les textes que l'app dit,
dedoublonnes, chacun au niveau le plus bas ou on l'entend.

REPRENABLE : un fichier present est un fichier fait ; relancer fait le reste.
Les refus du decoupage vont dans audio/en_refus_<dossier>.json : ces mots-la
restent a la voix du telephone (ou se reprennent avec --reprendre-refus).
"""
import argparse, io, json, os, sys, time

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "audio"))
sys.path.insert(0, os.path.join(RACINE, "anglais", "outils"))
import generer                      # noqa : cle, format, reglages, modeles
import lectures                     # noqa : les nombres en lettres
import manifest_voix                # noqa : l'inventaire anglais
from generer_es import appeler, normaliser   # noqa : meme appel, meme sonie
from recouper import recouper, Refus         # noqa

# La voix choisie par Jacques, puis son dossier sur Firebase Hosting
# (https://deutschai-b6fbb.web.app/en-us/<id>.mp3). Le britannique aura le sien
# (en-gb) le jour ou il le demandera.
VOIX = {
    "us": ("", "en-us"),
}
NIVEAUX_AVEC_VOIX = ("A1", "A2")
PORTEUSE = "Word: %s."
VITESSE_PORTEUSE = 0.80
MODELE = "v2"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--variante", choices=sorted(VOIX), default="us")
    p.add_argument("--niveaux", default=",".join(NIVEAUX_AVEC_VOIX))
    p.add_argument("--plafond", type=int, default=110000, help="credits au plus pour cette execution")
    p.add_argument("--a-blanc", action="store_true")
    p.add_argument("--normaliser", action="store_true")
    p.add_argument("--reprendre-refus", action="store_true",
                   help="ne refaire que les refus, avec la porteuse de --porteuse")
    p.add_argument("--porteuse", default=PORTEUSE)
    p.add_argument("--sources", default="",
                   help="ne produire que ces sources (prefixes, ex. noms,verbes)")
    a = p.parse_args()

    voix, dossier = VOIX[a.variante]
    if a.normaliser:
        normaliser(dossier)
        return
    niveaux = [n.strip() for n in a.niveaux.split(",")]
    hors = [n for n in niveaux if n not in NIVEAUX_AVEC_VOIX]
    if hors:
        sys.exit("Niveaux non accordes : %s. Jacques n'a demande que %s."
                 % (",".join(hors), ",".join(NIVEAUX_AVEC_VOIX)))
    sortie = os.path.join(RACINE, "audio", "mp3", dossier)
    bruts = os.path.join(RACINE, "audio", "bruts_en", dossier)
    modele, taux = generer.MODELES[MODELE]
    refus_chemin = os.path.join(RACINE, "audio", "en_refus_%s.json" % dossier)
    refus = json.load(io.open(refus_chemin, encoding="utf-8")) if os.path.exists(refus_chemin) else {}
    a_faire = [e for e in manifest_voix.entrees(a.variante)
               if e["niveau"] in niveaux and not os.path.exists(os.path.join(sortie, e["id"] + ".mp3"))]
    if a.sources:
        prefixes = tuple(s.strip() for s in a.sources.split(","))
        a_faire = [e for e in a_faire if e["source"].startswith(prefixes)]
    if a.reprendre_refus:
        a_faire = [e for e in a_faire if e["id"] in refus]
        for e in a_faire:
            del refus[e["id"]]
        bruts = os.path.join(bruts, "".join(c if c.isalnum() else "_" for c in a.porteuse))
    dit = lambda e: lectures.lecture("en", e["texte"])
    texte_de = lambda e: (a.porteuse % dit(e)) if " " not in e["texte"] else dit(e)
    sans, _ = lectures.controler("en", [e["texte"] for e in a_faire])
    if sans:
        sys.exit("%d textes a chiffres sans lecture (audio/lectures/en.json), dont : %s"
                 % (len(sans), sans[0]))
    cout = int(sum(len(texte_de(e)) for e in a_faire) * taux)
    print("voix %s -> audio/mp3/%s/   modele %s" % (voix or "(pas encore choisie)", dossier, modele))
    print("%d fichiers a produire (%d mots seuls en porteuse), environ %d credits"
          % (len(a_faire), sum(1 for e in a_faire if " " not in e["texte"]), cout))
    if a.a_blanc or not a_faire:
        return
    if not voix:
        sys.exit("Aucune voix choisie : Jacques choisit d'abord au comparatif a l'aveugle.")

    os.makedirs(sortie, exist_ok=True)
    os.makedirs(bruts, exist_ok=True)
    cle = generer.cle_api()
    depense = faits = 0
    debut = time.time()
    try:
        for e in a_faire:
            if e["id"] in refus:
                continue
            texte = texte_de(e)
            prix = int(len(texte) * taux)
            if depense + prix > a.plafond:
                print("plafond atteint (%d credits). Relancer reprend la suite." % depense)
                break
            cible = os.path.join(sortie, e["id"] + ".mp3")
            try:
                if " " in e["texte"]:
                    son = appeler(voix, texte, generer.REGLAGES, modele, cle)
                    open(cible + ".part", "wb").write(son)
                    os.replace(cible + ".part", cible)
                else:
                    brut = os.path.join(bruts, e["id"] + ".mp3")
                    if not os.path.exists(brut):
                        son = appeler(voix, texte, dict(generer.REGLAGES, speed=VITESSE_PORTEUSE), modele, cle)
                        open(brut, "wb").write(son)
                    try:
                        recouper(brut, cible + ".part", texte=e["texte"])
                        os.replace(cible + ".part", cible)
                    except Refus as err:
                        refus[e["id"]] = {"texte": e["texte"], "raison": str(err)}
                        if os.path.exists(cible + ".part"):
                            os.remove(cible + ".part")
            except generer.TexteBloque:
                refus[e["id"]] = {"texte": e["texte"], "raison": "refuse par ElevenLabs"}
            depense += prix
            faits += 1
            if faits % 100 == 0:
                ecoule = time.time() - debut
                print("  %5d/%d  %7d credits  reste ~%d min" % (faits, len(a_faire), depense,
                      int((len(a_faire) - faits) * ecoule / faits / 60)), flush=True)
                json.dump(refus, io.open(refus_chemin, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    except KeyboardInterrupt:
        print("interrompu -- ce qui est fait est garde.")
    json.dump(refus, io.open(refus_chemin, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("fait : %d appels, %d credits, %d refus au total" % (faits, depense, len(refus)))


if __name__ == "__main__":
    main()
