# -*- coding: utf-8 -*-
"""Deplace un plan dans le montage, et renumerote tout ce qui le suit.

    python scenes/renumeroter.py --deplacer 14 --apres 18
    python scenes/renumeroter.py --deplacer 14 --apres 18 --pour-de-vrai

POURQUOI CE N'EST PAS QU'UN DEPLACEMENT DANS UN JSON
    Le numero de plan est une CLE D'IDENTITE, pas une simple position : il
    nomme le clip (03-final/plan14.mp4), la voix (14-erzaehler.mp3), les
    prises (02-prises/plan14-01.mp4), l'image de decor, la ligne du
    manifeste, et l'entree de MISE_EN_SCENE dans production.py. Deplacer le
    plan dans le seul fichier de scene ferait lire au montage le mauvais clip
    -- sans erreur, sans avertissement, juste un episode faux.

    On renomme donc tout ensemble, ou rien.

LE RENOMMAGE SE FAIT EN DEUX TEMPS
    Un deplacement produit un CYCLE : 14 devient 18, mais 18 devient 17, qui
    devient 16... Renommer dans l'ordre ecraserait un fichier a chaque pas.
    On passe donc tout par un nom temporaire avant de poser les vrais.

CE QU'IL NE TOUCHE PAS
    Les commentaires de production.py qui citent des numeros en toutes lettres
    (<< plans 15-16 moyen serre >>). Une regle qui les reecrirait toucherait
    aussi des numeros qui ne sont pas des plans. Le script les signale ; c'est
    a la main que ca se corrige, en relisant.
"""
import argparse
import io
import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = "__renum__"


def nouvel_ordre(plans, quoi, apres):
    """L'ordre des plans une fois `quoi` glisse juste apres `apres`."""
    reste = [p for p in plans if p["n"] != quoi]
    bouge = next(p for p in plans if p["n"] == quoi)
    i = next(k for k, p in enumerate(reste) if p["n"] == apres)
    return reste[:i + 1] + [bouge] + reste[i + 1:]


def renommer(couples, quoi):
    """couples : [(source, destination)]. Deux passes, via un nom temporaire."""
    faits = []
    for src, dst in couples:
        if src == dst or not os.path.exists(src):
            continue
        mid = os.path.join(os.path.dirname(dst), TMP + os.path.basename(dst))
        os.rename(src, mid)
        faits.append((mid, dst))
    for mid, dst in faits:
        os.rename(mid, dst)
    if faits:
        print("  %-14s %d fichier(s)" % (quoi, len(faits)))
    return len(faits)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", default="01-ankunft-berlin")
    ap.add_argument("--deplacer", type=int, required=True)
    ap.add_argument("--apres", type=int, required=True,
                    help="numero du plan derriere lequel il vient se poser")
    ap.add_argument("--pour-de-vrai", action="store_true")
    a = ap.parse_args()

    fs = os.path.join(RACINE, "scenes", a.scene + ".json")
    d = json.load(io.open(fs, encoding="utf-8"))
    plans = d["plans"]
    for n in (a.deplacer, a.apres):
        if not any(p["n"] == n for p in plans):
            sys.exit("  Le plan %d n'existe pas dans %s." % (n, a.scene))
    if a.deplacer == a.apres:
        sys.exit("  Un plan ne se pose pas derriere lui-meme.")

    ordre = nouvel_ordre(plans, a.deplacer, a.apres)
    carte = {p["n"]: i + 1 for i, p in enumerate(ordre)}
    parle = {p["n"]: p["locuteur"] for p in plans}
    bouges = {v: k for k, v in carte.items() if k != v}

    print("  %s" % d["situation"])
    print("  le plan %d se pose derriere le plan %d" % (a.deplacer, a.apres))
    print()
    print("  ancien  nouveau  locuteur   replique")
    for p in ordre:
        if carte[p["n"]] != p["n"]:
            print("    %2d   ->  %2d     %-9s %s"
                  % (p["n"], carte[p["n"]], p["locuteur"], p.get("de", "")[:52]))
    if not bouges:
        sys.exit("\n  Rien ne bouge.")

    if not a.pour_de_vrai:
        print("\n  Essai a blanc. Relancer avec --pour-de-vrai.")
        return

    print()
    da = os.path.join(RACINE, "audio", "scenes", a.scene)
    dv = os.path.join(RACINE, "video", "episode-" + a.scene)

    # Les voix : le nom porte le numero ET le locuteur, les deux voyagent.
    for sous in (da, os.path.join(da, "_brut")):
        renommer([(os.path.join(sous, "%02d-%s.mp3" % (o, parle[o])),
                   os.path.join(sous, "%02d-%s.mp3" % (n, parle[o])))
                  for o, n in carte.items()],
                 "brut" if sous.endswith("_brut") else "voix")

    # Les clips montes.
    f = os.path.join(dv, "03-final")
    renommer([(os.path.join(f, "plan%02d.mp4" % o),
               os.path.join(f, "plan%02d.mp4" % n)) for o, n in carte.items()],
             "clips")

    # Les prises, y compris les ratees : elles coutent 200 credits piece.
    pr = os.path.join(dv, "02-prises")
    couples = []
    if os.path.isdir(pr):
        for nom in os.listdir(pr):
            m = re.match(r"plan(\d\d)-(\d\d)\.mp4$", nom)
            if m and int(m.group(1)) in carte:
                couples.append((os.path.join(pr, nom),
                                os.path.join(pr, "plan%02d-%s.mp4"
                                             % (carte[int(m.group(1))], m.group(2)))))
    renommer(couples, "prises")

    # ⚠️ LES PLANS SYNCHRONISES, ET CE QUE LEUR OUBLI PRODUISAIT (10 sept. 2026)
    #
    # 04-lipsync n'etait pas renomme. Apres un deplacement, le montage
    # trouvait 04-lipsync/plan14.mp4 -- la synchro de l'ANCIEN plan 14 -- et
    # la servait pour le nouveau. Le garde-fou « synchro perimee » du montage
    # ne pouvait rien voir : il compare les dates d'un clip d'origine et de sa
    # synchro, et quand le clip d'origine n'existe pas encore (un plan neuf),
    # il n'y a rien a comparer. Un episode faux, sans une ligne d'avertissement.
    #
    # C'est exactement le defaut que ce script existe pour empecher, et il le
    # produisait sur les seuls fichiers qui coutent de l'argent a refaire.
    f4 = os.path.join(dv, "04-lipsync")
    renommer([(os.path.join(f4, "plan%02d.mp4" % o),
               os.path.join(f4, "plan%02d.mp4" % n)) for o, n in carte.items()],
             "synchros")

    # etat.json de lipsync.py : ses cles SONT les numeros de plan. Sans cette
    # reecriture, une relance croirait le nouveau plan deja synchronise.
    fe = os.path.join(f4, "etat.json")
    if os.path.exists(fe):
        e = json.load(io.open(fe, encoding="utf-8"))
        neuf = {}
        for cle, val in e.items():
            neuf[str(carte.get(int(cle), int(cle)))] = val
        io.open(fe, "w", encoding="utf-8", newline="").write(
            json.dumps(neuf, ensure_ascii=False, indent=2) + chr(10))
        print("  etat.json      %d cle(s)" % len(neuf))

    # Le journal des prises retenues et les fenetres de bouche mesurees : ils
    # nomment des prises, donc ils suivent. On ne REECRIT PAS l'histoire des
    # lignes datees -- on renomme le fichier qu'elles designent, ce qui est
    # la meme chose que pour _sources.txt.
    ret = os.path.join(dv, "03-final", "_retenues.txt")
    if os.path.exists(ret):
        lignes = []
        for l in io.open(ret, encoding="utf-8"):
            m = re.search(r"plan(\d\d)\s+plan(\d\d)-(\d\d)\.mp4", l)
            if m and int(m.group(1)) in carte:
                l = l.replace(m.group(0), "plan%02d  plan%02d-%s.mp4"
                              % (carte[int(m.group(1))],
                                 carte[int(m.group(2))], m.group(3)))
            lignes.append(l)
        io.open(ret, "w", encoding="utf-8", newline="").write("".join(lignes))
        print("  registre       _retenues.txt")

    pj = os.path.join(pr, "_parole.json")
    if os.path.exists(pj):
        mes = json.load(io.open(pj, encoding="utf-8"))
        neuf = {}
        for nom, val in mes.items():
            m = re.match(r"plan(\d\d)-(\d\d)\.mp4$", nom)
            if m and int(m.group(1)) in carte:
                nom = "plan%02d-%s.mp4" % (carte[int(m.group(1))], m.group(2))
            neuf[nom] = val
        io.open(pj, "w", encoding="utf-8", newline="").write(
            json.dumps(neuf, ensure_ascii=False, indent=1) + chr(10))
        print("  fenetres       _parole.json")

    # Le registre d'empreintes de rapatrier.py suit les noms de prises.
    reg = os.path.join(pr, "_sources.txt")
    if os.path.exists(reg):
        lignes = []
        for l in io.open(reg, encoding="utf-8"):
            m = re.search(r"plan(\d\d)-(\d\d)\.mp4", l)
            if m and int(m.group(1)) in carte:
                l = l.replace(m.group(0), "plan%02d-%s.mp4"
                              % (carte[int(m.group(1))], m.group(2)))
            lignes.append(l)
        io.open(reg, "w", encoding="utf-8", newline="").write("".join(lignes))
        print("  registre       _sources.txt")

    # Les images de decor.
    im = os.path.join(dv, "01-images")
    couples = []
    if os.path.isdir(im):
        for nom in os.listdir(im):
            m = re.match(r"decor-plan(\d\d)(.*)\.png$", nom)
            if m and int(m.group(1)) in carte:
                couples.append((os.path.join(im, nom),
                                os.path.join(im, "decor-plan%02d%s.png"
                                             % (carte[int(m.group(1))], m.group(2)))))
    renommer(couples, "images")

    # Le manifeste audio.
    fm = os.path.join(da, "manifeste.json")
    if os.path.exists(fm):
        mf = json.load(io.open(fm, encoding="utf-8"))
        for x in mf["plans"]:
            x["plan"] = carte[x["plan"]]
            x["fichier"] = "%02d-%s.mp3" % (x["plan"], x["locuteur"])
        mf["plans"].sort(key=lambda x: x["plan"])
        io.open(fm, "w", encoding="utf-8", newline="").write(
            json.dumps(mf, ensure_ascii=False, indent=2) + chr(10))
        print("  manifeste      %d lignes" % len(mf["plans"]))

    # MISE_EN_SCENE, en deux temps lui aussi.
    fp = os.path.join(RACINE, "scenes", "production.py")
    t = io.open(fp, encoding="utf-8").read()
    for o, n in carte.items():
        t = re.sub(r"(?m)^(    )%d: dict\(" % o, r"\g<1>%s%d: dict(" % (TMP, n), t)
    t = t.replace("    %s" % TMP, "    ")
    io.open(fp, "w", encoding="utf-8", newline=chr(10)).write(t)
    print("  production.py  cles de MISE_EN_SCENE")

    # La scene, en dernier : c'est elle qui fait foi.
    for p in plans:
        p["n"] = carte[p["n"]]
    d["plans"] = sorted(plans, key=lambda p: p["n"])
    io.open(fs, "w", encoding="utf-8", newline=chr(10)).write(
        json.dumps(d, ensure_ascii=False, indent=2) + chr(10))
    print("  scene          %s.json" % a.scene)

    print("\n  A RELIRE A LA MAIN : les commentaires de production.py citent des")
    print("  numeros de plan en toutes lettres. Le script ne les touche pas.")
    print("  Puis : python scenes/production.py")
    print("         python video/montage.py --scene %s" % a.scene)


if __name__ == "__main__":
    main()
