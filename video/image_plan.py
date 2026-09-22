# -*- coding: utf-8 -*-
"""L'image fixe d'un plan, chez fal. ET C'EST FACTURE.

    python video/image_plan.py --scene 02-beim-buergeramt --plan 1 --montrer
    python video/image_plan.py --scene 02-beim-buergeramt --plan 1 \\
        --ref personnages/Mark-dos.png personnages/Mark.png

CE QUE CA REMPLACE
    Artlist / Framing, dont les credits sont epuises. Le meme geste : un
    prompt, des images de reference, une image verticale en retour.

DEUX MODELES, ET LE CHOIX N'EST PAS QUE FINANCIER
    sans --ref   fal-ai/nano-banana-pro          texte -> image
    avec --ref   fal-ai/nano-banana-pro/edit     1 a 4 references
    0,15 $ l'image dans les deux cas (le 4K double ; on reste en 2K).

    ⚠️ TOUT PLAN QUI CONTIENT UN PERSONNAGE PASSE PAR --ref, meme s'il est
       petit et de dos. La coherence de personnage est LE defaut recurrent du
       projet : les deux Annas du 8 septembre, le plan de dos de l'aeroport
       le 12. Un plan sans ancrage ne rate pas a moitie, il rate entierement,
       et il se voit au montage, pas au retour.

LE PROMPT SE LIT DANS A-TOURNER.txt, IL NE SE RECOPIE PAS
    Bloc « PROMPT D'IMAGE (Framing) », jusqu'au premier ⚠️, « Reference » ou
    « PROMPT DE MOUVEMENT ». Le fichier reste la source unique : un prompt
    recopie ici divergerait le jour ou l'on corrige la-bas.

    ⚠️ TOUJOURS LIRE --montrer AVANT DE PAYER. C'est gratuit, ca affiche le
       prompt exact et les references, et c'est la seule occasion de voir
       qu'on s'apprete a envoyer autre chose que ce qu'on croit.

LA CLE N'EST PAS DANS LE CODE
    fal.secret a la racine (ignore par git) ou FAL_KEY.
"""
import argparse
import io
import json
import os
import re
import sys
import time
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, "video"))
import omnihuman as O                                        # noqa: E402
import verifier_prompt as VP                                # noqa: E402

TEXTE = "fal-ai/nano-banana-pro"
EDIT = "fal-ai/nano-banana-pro/edit"
PRIX = 0.15                      # $ l'image, releve sur la fiche du modele
MIMES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
         ".webp": "image/webp"}


def bloc_plan(txt, n):
    """Le bloc d'un plan dans A-TOURNER.txt, de son titre au suivant."""
    m = re.search(r"^PLAN %02d\b.*?(?=^PLAN \d\d\b|\Z)" % n, txt, re.S | re.M)
    if not m:
        sys.exit("  A-TOURNER.txt n'a pas de « PLAN %02d »." % n)
    return m.group(0)


def prompt_image(bloc, n):
    """Le prompt de Framing : de son titre jusqu'a ce qui n'est plus lui.

    ⚠️ On s'arrete au premier ⚠️, « Reference » ou « PROMPT DE MOUVEMENT ».
    Ces lignes-la sont des consignes A NOUS, pas au modele -- les envoyer
    ferait payer une image ou le generateur essaie d'obeir a du francais."""
    m = re.search(r"PROMPT D'IMAGE \(Framing\)\s*\n(.*?)"
                  r"(?=\n\s*(?:⚠|REFERENCE|Reference|Visage neuf|Position neuve"
                  r"|Image a nommer|PROMPT DE MOUVEMENT)|\Z)",
                  bloc, re.S)
    if not m or not m.group(1).strip():
        sys.exit("  plan %02d : pas de bloc « PROMPT D'IMAGE (Framing) »." % n)
    return "\n".join(l.rstrip() for l in m.group(1).strip().splitlines())


# Ce qui compte comme UNE IMAGE DE PERSONNAGE. Tout ce qui vit dans
# personnages/, plus les images maitresses de l'episode, qui portent le nom du
# personnage en tete de fichier.
PORTRAIT = re.compile(r"(?i)(^|[\\/])(personnages[\\/]"
                      r"|(mark|anna|dame|cycliste|erzaehler)[-_.])")


def visage_neuf(bloc):
    """Ce plan fabrique-t-il un visage qui n'existe pas encore ?

    ⚠️ LA REGLE QUI MANQUAIT, ET CE QU'ELLE A COUTE. Le 16 septembre 2026,
       cycliste-jaune a ete fabrique avec `--ref mark-marche.png` et rien
       d'autre -- pour tenir le LIEU. Le cycliste est sorti avec le visage de
       Mark, et il servait de maitre a CINQ plans. Jacques l'a vu du premier
       coup d'oeil : << le probleme de l'image cycliste, c'est Marc, avec un
       veston jaune >>.

       Une image de reference sert a transporter un VISAGE. C'est sa fonction,
       pas un effet de bord -- et c'est exactement pour ca que la regle du
       projet impose --ref des qu'il y a un personnage. Le prompt disait
       pourtant << a man in his forties >> : un prompt ne gagne jamais contre
       une reference sur le visage.

       Donc : un plan qui INTRODUIT quelqu'un le declare, et ne recoit alors
       que des references SANS visage. Le lieu se tient tres bien avec un
       decor vide."""
    return re.search(r"(?im)^\s*Visage neuf\s*:\s*oui\s*$", bloc) is not None


def position_neuve(bloc):
    """Ce plan deplace-t-il quelqu'un par rapport aux plans voisins ?

    ⚠️ LE PENDANT DE << Visage neuf >>, ET IL A COUTE AUTANT. Le 16 septembre
       2026, le plan 12 devait montrer les baskets sur le GRIS. Deux images
       payees avec --ref bande-rouge-pieds -- une photo ou les pieds sont sur
       le ROUGE -- les ont gardees sur le rouge, malgre un texte qui disait
       explicitement le contraire, puis malgre un texte qui comptait les
       paires. La septieme a reussi du premier coup, sans aucune reference.

       Une reference transporte ce qu'elle MONTRE : un visage, et aussi une
       position. Ce n'est pas un effet de bord, c'est sa fonction.

    Ici on refuse TOUTE reference, pas seulement les portraits : le piege du
    plan 12 n'etait pas un visage mais une paire de chaussures. Pour tenir le
    lieu malgre tout, il reste la description -- et elle a suffi."""
    return re.search(r"(?im)^\s*Position neuve\s*:\s*oui\s*$",
                     bloc) is not None


def nom_image(bloc, n):
    """Le nom du fichier, EXTENSION COMPRISE.

    ⚠️ A-TOURNER.txt ecrit les noms sans extension (<< Image a nommer :
    carrefour-rouge >>), et jusqu'au 16 septembre 2026 l'outil ecrivait le
    fichier tel quel. Un fichier sans extension n'a pas de type MIME : il ne
    peut donc PAS servir de reference a l'image suivante -- alors que tout
    l'episode est construit sur des images qui derivent l'une de l'autre. Le
    dossier 01-images en garde la trace, des paires << nom >> et << nom.png >>
    recopiees a la main."""
    m = re.search(r"Image a nommer\s*:\s*(\S+)", bloc)
    nom = m.group(1) if m else "plan%02d" % n
    return nom if os.path.splitext(nom)[1] else nom + ".png"


def archiver(chemin):
    """Ranger la prise precedente au lieu de l'ecraser.

    ⚠️ UNE PRISE PAYEE NE S'ECRASE PAS. Le 13 septembre, --refaire a detruit
    la premiere facade du Buergeramt -- 0,15 $ et une composition que Jacques
    n'a pas pu comparer a la suivante. On ne sait qu'APRES coup laquelle des
    deux etait la bonne, et c'est precisement pour ca qu'il faut les deux.
    (Recuperable sous l'onglet Requests de fal, mais a la main.)"""
    base, ext = os.path.splitext(chemin)
    i = 1
    while os.path.exists("%s-v%d%s" % (base, i, ext)):
        i += 1
    # L'image et son recu partent ensemble : un recu orphelin ne prouve plus
    # rien, et une prise sans recu ne se rattache plus a une facture.
    paires = [(chemin, "%s-v%d%s" % (base, i, ext)),
              (base + "-fal.json", "%s-v%d-fal.json" % (base, i))]
    for vieux, neuf in paires:
        if os.path.exists(vieux):
            os.replace(vieux, neuf)
            print("  prise precedente rangee : %s" % os.path.basename(neuf))
    return paires[0][1]          # ou l'image vient d'etre rangee


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--scene", default="02-beim-buergeramt")
    p.add_argument("--plan", type=int, required=True)
    p.add_argument("--ref", nargs="*", default=[],
                   help="1 a 4 images de reference, chemins depuis la racine")
    p.add_argument("--format", default="9:16", dest="ratio")
    p.add_argument("--resolution", default="2K", choices=["1K", "2K", "4K"])
    p.add_argument("--montrer", action="store_true",
                   help="afficher le prompt et les references, ne rien appeler")
    p.add_argument("--refaire", action="store_true",
                   help="generer une autre prise ; la precedente est RANGEE "
                        "en -v1, -v2... jamais ecrasee")
    a = p.parse_args()

    ep = os.path.join(RACINE, "video", "episode-%s" % a.scene)
    feuille = os.path.join(ep, "A-TOURNER.txt")
    if not os.path.exists(feuille):
        sys.exit("  introuvable : %s" % feuille)
    bloc = bloc_plan(io.open(feuille, encoding="utf-8").read(), a.plan)
    prompt = prompt_image(bloc, a.plan)
    nom = nom_image(bloc, a.plan)
    sortie = os.path.join(ep, "01-images", nom)

    if len(a.ref) > 4:
        sys.exit("  au plus 4 references ; %d donnees." % len(a.ref))
    refs = []
    for r in a.ref:
        c = r if os.path.isabs(r) else os.path.join(RACINE, r)
        if not os.path.exists(c):
            sys.exit("  reference introuvable : %s" % c)
        refs.append(c)

    if position_neuve(bloc) and refs:
        sys.exit("\n  Ce plan porte « Position neuve : oui » : il deplace\n"
                 "  quelqu'un par rapport aux plans voisins. Or une reference\n"
                 "  transporte la POSITION qu'elle montre, comme elle\n"
                 "  transporte un visage -- c'est sa fonction.\n\n"
                 "  Le plan 12 de l'episode 3 a coute DEUX images a cause de\n"
                 "  ca : la reference montrait les pieds sur le rouge, ils y\n"
                 "  sont restes. La septieme prise a reussi du premier coup,\n"
                 "  sans reference. Rien n'a ete facture.\n\n"
                 "  Relancer sans --ref, et decrire le lieu.")

    if visage_neuf(bloc):
        coupables = [os.path.basename(r) for r in refs
                     if PORTRAIT.search(os.path.relpath(r, RACINE))]
        if coupables:
            sys.exit("\n  Ce plan porte « Visage neuf : oui » : il fabrique\n"
                     "  quelqu'un qui n'existe pas encore. Or ces references\n"
                     "  portent un visage deja connu :\n    %s\n\n"
                     "  Une reference TRANSPORTE le visage -- c'est sa\n"
                     "  fonction. Le cycliste de l'episode 3 est sorti avec\n"
                     "  celui de Mark pour cette raison exacte, et il servait\n"
                     "  de maitre a cinq plans. Rien n'a ete facture.\n\n"
                     "  Pour tenir le LIEU, referencer un decor sans personne\n"
                     "  (carrefour-rouge, deux-bandes...)."
                     % "\n    ".join(coupables))

    modele = EDIT if refs else TEXTE
    cout = PRIX * (2 if a.resolution == "4K" else 1)
    print("plan %02d -> %s" % (a.plan, os.path.relpath(sortie, RACINE)))
    print("  modele     %s" % modele)
    print("  format     %s, %s" % (a.ratio, a.resolution))
    print("  references %s" % (", ".join(os.path.basename(r) for r in refs)
                               or "aucune (texte seul)"))
    print("  cout       %.2f $" % cout)
    print("  prompt     %d mots, %d caracteres" % (len(prompt.split()), len(prompt)))

    # ⚠️ LE CONTROLE PASSE AVANT LA DEPENSE, ET IL PASSE AUSSI SOUS --montrer.
    #    Jusqu'au 16 septembre 2026 cet outil payait sans rien verifier : seul
    #    omnihuman.py etait garde. C'est par cette breche que sont parties les
    #    deux images de mark-marche avec leur panneau -- la faute etait dans le
    #    prompt, et rien ne l'a lue avant de facturer.
    fautes = VP.dire(nom, VP.controler(prompt, image=True), bavard=False)

    if a.montrer:
        print("\n" + "-" * 70)
        print(prompt)
        print("-" * 70)
        print("\n  RIEN N'A ETE APPELE. Relance sans --montrer pour generer.")
        return

    if fautes and not os.environ.get("WORTANDO_FORCER"):
        sys.exit("\n  %d faute(s) connue(s) dans ce prompt : rien n'a ete\n"
                 "  televerse, et rien n'a ete facture. Corrige A-TOURNER.txt,\n"
                 "  ou relance avec WORTANDO_FORCER=1 si tu sais pourquoi."
                 % fautes)

    if os.path.exists(sortie):
        if not a.refaire:
            sys.exit("  %s existe deja. --refaire pour en generer une autre." % nom)
        ancien = archiver(sortie)
        # ⚠️ UNE RETOUCHE SE REFERENCE ELLE-MEME, et --refaire venait de
        #    deplacer le fichier sous les pieds du televersement. 22 sept.
        #    2026, plan 17 : la reference etait il-attend.png, archivee en
        #    il-attend-v1.png une ligne plus haut, et l'outil s'est arrete
        #    sur un FileNotFoundError au moment de deposer -- avant l'appel,
        #    donc sans rien facturer, mais avec l'image d'origine deja
        #    renommee. On suit le deplacement.
        refs = [ancien if os.path.abspath(c) == os.path.abspath(sortie) else c
                for c in refs]

    cle = O.cle()
    corps = {"prompt": prompt, "aspect_ratio": a.ratio,
             "resolution": a.resolution, "output_format": "png",
             "num_images": 1}
    if refs:
        urls = []
        for c in refs:
            mime = MIMES.get(os.path.splitext(c)[1].lower(), "image/png")
            u, o = O.deposer(c, mime, cle)
            print("    depose %s (%.1f Mo)" % (os.path.basename(c), o / 1e6))
            urls.append(u)
        corps["image_urls"] = urls

    soum = O._json("https://queue.fal.run/" + modele, cle, corps)
    print("    requete %s" % soum.get("request_id", "?"))
    res = O.attendre(soum["status_url"], soum["response_url"], cle)

    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    octets = O.telecharger(res["images"][0]["url"], sortie)
    print("    -> %s  (%.1f Mo, %.2f $)" % (nom, octets / 1e6, cout))

    recu = os.path.splitext(sortie)[0] + "-fal.json"
    io.open(recu, "w", encoding="utf-8").write(json.dumps({
        "modele": modele, "request_id": soum.get("request_id"),
        "quand": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "references": [os.path.relpath(r, RACINE) for r in refs],
        "format": a.ratio, "resolution": a.resolution,
        "cout_usd": cout, "prompt": prompt,
        "description": res.get("description", ""),
    }, ensure_ascii=False, indent=1))
    if res.get("description"):
        print("    le modele decrit : %s" % res["description"][:200])


if __name__ == "__main__":
    main()
