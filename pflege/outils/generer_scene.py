# -*- coding: utf-8 -*-
"""L'image d'une scene de soins, chez fal. ET C'EST FACTURE (0,15 $).

    python pflege/outils/generer_scene.py soins-zimmer                # montre, ne paie rien
    python pflege/outils/generer_scene.py soins-zimmer --format 9:16 --payer
    python pflege/outils/generer_scene.py soins-zimmer-aufstehen --ref soins-zimmer --payer

C'EST visuel/generer_scene.py, SANS EN CHANGER UNE LIGNE
    Meme controle (video/verifier_prompt.py, jeu image), meme regle de
    paiement (--payer), meme rangement des prises precedentes. Seuls les
    chemins changent, pour que la section Soins ne touche a rien du
    dossier des scenes generales :
      - le prompt vit dans le depot : pflege/scenes/<nom>.prompt.txt ;
      - l'image ORIGINALE (PNG 2K) vit HORS du depot et hors de OneDrive :
        ~/.wortando/pflege/scenes/<nom>.png (comme visuel/*/img/) ;
      - le recu fal (<nom>-fal.json : prompt, references, cout) revient dans
        le depot, a cote du prompt.
    Une reference nommee sans chemin (« soins-zimmer ») designe l'original
    d'une scene de soins deja generee : c'est ainsi qu'un gros plan ou une
    retouche part de l'image maitresse (continuite-du-decor-video).
"""
import io
import os
import shutil
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SOURCES = os.path.join(RACINE, "pflege", "scenes")
ORIGINAUX = os.path.join(os.path.expanduser("~"), ".wortando", "pflege")

sys.path.insert(0, os.path.join(RACINE, "visuel"))
import generer_scene as G                                    # noqa: E402


def cle_fal():
    """La cle vit dans fal.secret a la racine du dossier principal (un
    worktree n'en a pas). On la passe par l'environnement, sans l'afficher."""
    if os.environ.get("FAL_KEY"):
        return
    for d in (RACINE, os.path.normpath(os.path.join(RACINE, "..", "..", ".."))):
        c = os.path.join(d, "fal.secret")
        if os.path.exists(c):
            os.environ["FAL_KEY"] = io.open(c, encoding="utf-8-sig").read().strip()
            return


def main():
    args = sys.argv[1:]
    noms = [a for a in args if not a.startswith("--")]
    if not noms:
        sys.exit(__doc__)
    nom = noms[0]
    src = os.path.join(SOURCES, nom + ".prompt.txt")
    if not os.path.exists(src):
        sys.exit("  introuvable : %s" % src)
    os.makedirs(os.path.join(ORIGINAUX, "scenes"), exist_ok=True)
    shutil.copyfile(src, os.path.join(ORIGINAUX, "scenes", nom + ".prompt.txt"))

    # Les references : un nom seul = l'original d'une scene de soins.
    neufs, dans_ref = [], False
    for a in args:
        if a == "--ref":
            dans_ref = True
        elif a.startswith("--"):
            dans_ref = False
        elif dans_ref and not os.path.splitext(a)[1]:
            a = os.path.join(ORIGINAUX, "scenes", a + ".png")
        neufs.append(a)
    if "--format" not in args:
        neufs += ["--format", "9:16"]

    cle_fal()
    if not os.environ.get("SSL_CERT_FILE"):
        try:
            import certifi
            os.environ["SSL_CERT_FILE"] = certifi.where()
        except ImportError:
            pass
    G.ICI = ORIGINAUX
    sys.argv = [sys.argv[0]] + neufs
    G.main()
    recu = os.path.join(ORIGINAUX, "scenes", nom + "-fal.json")
    if os.path.exists(recu) and "--payer" in args:
        shutil.copyfile(recu, os.path.join(SOURCES, nom + "-fal.json"))
        print("  recu copie : pflege/scenes/%s-fal.json" % nom)


if __name__ == "__main__":
    main()
