# -*- coding: utf-8 -*-
"""Pose une langue dans pruefung.json, en refusant les traductions amputees.

    python tests/poser_pruefung_uk.py corrections_uk/pruefung_uk_sprechen.json
    python tests/poser_pruefung_uk.py --etat

Le lot est un objet { "sprechen|5": { "erkl_uk": "...", ... }, ... }. La cle
est celle de completer_tr_pruefung.py -- « sprechen|5 », « hoeren|12 »,
« lesen|3|1 » pour la deuxieme question du quatrieme texte -- et les index
sont ceux du fichier, pas ceux d'un niveau filtre.

LE GARDE-FOU EST CELUI QUI A DEJA SERVI, ET IL EST REPRIS TEL QUEL.
Le turc de ce fichier avait ete ecrit plus court que le francais : les
explications gardaient la premiere phrase et perdaient la seconde -- celle qui
dit ce que l'erreur coute. Ni verifier.py ni ajouter_pruefung.py ne voient
cela : le champ existe et n'est pas vide.

On compare donc la LONGUEUR et le NOMBRE DE PHRASES avec le francais, et on
refuse d'ecrire une explication qui aurait perdu une phrase en route. Le
defaut s'est produit une fois ; il n'y a aucune raison qu'une autre langue en
soit dispensee.

⚠️ ON N'ECRASE JAMAIS. Un champ deja pose reste : un lot rejoue ne peut pas
defaire une correction faite entre-temps. Le compte le dit a chaque passage.
"""
import argparse
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIBLE = os.path.join(RACINE, "pruefung.json")
BASES = ["erkl", "frage", "trad", "consigne", "aufgabe"]


def phrases(t):
    """Les phrases utiles : sous 12 signes, c'est une abreviation, pas une phrase.

    ⚠️ ON NE COUPE PAS DEVANT UN GUILLEMET FERMANT. Le francais met une espace
    avant « ? » et « » » : « Faut-il interdire les telephones a l'ecole ? »
    compte alors pour DEUX phrases, alors que c'en est une seule citee. Les
    langues qui ne mettent pas cette espace -- l'ukrainien, l'anglais -- en
    comptent une, et le garde-fou refusait leur traduction comme amputee.
    Refuser une traduction juste est aussi grave qu'en accepter une fausse :
    la prochaine fois, on desarme le controle au lieu de le corriger.
    """
    return len([x for x in re.split(r"(?<=[.!?])\s+(?!»)", t.strip()) if len(x) > 12])


def entree(d, cle):
    p = cle.split("|")
    if p[0] == "lesen":
        return d["lesen"][int(p[1])]["fragen"][int(p[2])]
    return d[p[0]][int(p[1])]


def cles(d):
    """Toutes les cles du fichier, dans l'ordre, avec l'objet qu'elles designent."""
    for i, o in enumerate(d.get("sprechen", [])):
        yield "sprechen|%d" % i, o
    for i, o in enumerate(d.get("schreiben", [])):
        yield "schreiben|%d" % i, o
    for i, o in enumerate(d.get("hoeren", [])):
        yield "hoeren|%d" % i, o
    for i, t in enumerate(d.get("lesen", [])):
        for j, o in enumerate(t.get("fragen", [])):
            yield "lesen|%d|%d" % (i, j), o


def etat(d, langue):
    manque = total = 0
    par_section = {}
    for cle, o in cles(d):
        sec = cle.split("|")[0]
        for b in BASES:
            if o.get(b + "_fr"):
                total += 1
                if not o.get(b + "_" + langue):
                    manque += 1
                    par_section[sec] = par_section.get(sec, 0) + 1
    for sec in sorted(par_section):
        print("   %-12s %4d a faire" % (sec, par_section[sec]))
    print("   ---")
    print("   %s : %d champ(s) a faire sur %d (%.1f %% faits)"
          % (langue, manque, total, 100.0 * (total - manque) / total if total else 100.0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lot", nargs="?")
    ap.add_argument("--langue", default="uk")
    ap.add_argument("--etat", action="store_true")
    a = ap.parse_args()

    brut = io.open(CIBLE, encoding="utf-8", newline="").read()
    d = json.loads(brut)
    if a.etat or not a.lot:
        etat(d, a.langue)
        return

    # LE FICHIER DOIT SE REPRODUIRE A L'IDENTIQUE AVANT QU'ON Y TOUCHE.
    # Sans ce controle, une reserialisation avec une autre indentation ferait
    # un diff ou personne ne verrait la traduction ajoutee.
    #
    # ⚠️ LES FINS DE LIGNE NE COMPTENT PAS DANS CETTE COMPARAISON. Le depot est
    # sur Windows et sous OneDrive : git rend le fichier en CRLF, json.dumps
    # ecrit en LF. Comparer octet a octet ferait echouer le controle sur une
    # difference qui n'est pas la notre. On reecrit ensuite avec la convention
    # trouvee dans le fichier, pour ne pas transformer tout le fichier en diff.
    crlf = "\r\n" in brut
    plat = brut.replace("\r\n", "\n")
    for indent in (1, 2):
        refait = json.dumps(d, ensure_ascii=False, indent=indent) + (
            "\n" if plat.endswith("\n") else "")
        if refait == plat:
            break
    else:
        sys.exit("pruefung.json ne se reproduit pas a l'identique : "
                 "mise en forme inconnue, on ne reecrit pas.")

    lot = json.load(io.open(a.lot, encoding="utf-8"))
    poses, sautes, rates = 0, 0, []
    for cle, champs in lot.items():
        try:
            o = entree(d, cle)
        except (KeyError, IndexError, ValueError):
            rates.append("CLE INCONNUE : " + cle)
            continue
        for k, v in champs.items():
            base = k.rsplit("_", 1)[0]
            if base not in BASES:
                rates.append("CHAMP INCONNU : %s (%s)" % (k, cle))
                continue
            fr = o.get(base + "_fr")
            if not fr:
                rates.append("PAS DE FRANCAIS : %s (%s)" % (k, cle))
                continue
            if not v or not v.strip():
                rates.append("VIDE : %s (%s)" % (k, cle))
                continue
            if phrases(v) < phrases(fr) or len(v) < 0.55 * len(fr):
                rates.append("AMPUTE : %s (%s) — %d phrases / %d, %d signes / %d"
                             % (k, cle, phrases(v), phrases(fr), len(v), len(fr)))
                continue
            if o.get(k):
                sautes += 1
                continue
            o[k] = v
            poses += 1
    if rates:
        print("REFUS : %d" % len(rates))
        for r in rates[:15]:
            print("   " + r)
        sys.exit(1)
    sortie = json.dumps(d, ensure_ascii=False, indent=indent) + (
        "\n" if plat.endswith("\n") else "")
    io.open(CIBLE, "w", encoding="utf-8", newline="").write(
        sortie.replace("\n", "\r\n") if crlf else sortie)
    print("%s : %d champ(s) pose(s)%s"
          % (os.path.basename(a.lot), poses,
             (", %d deja presents" % sautes) if sautes else ""))


if __name__ == "__main__":
    main()
