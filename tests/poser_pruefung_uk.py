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

    ⚠️ DEUX CHOSES QUE CE COMPTEUR PRENAIT POUR DES FINS DE PHRASE, ET QUI
    N'EN SONT PAS. Les deux viennent de la typographie FRANCAISE, et les deux
    ont fait refuser des traductions ukrainiennes correctes :

      - L'ESPACE AVANT « ? » ET « » ». « Faut-il interdire les telephones a
        l'ecole ? » comptait pour deux phrases alors que c'en est une seule,
        citee. Les langues qui ne mettent pas cette espace en comptaient une.

      - LE POINT D'ABREVIATION. « Que doit faire M. Sow… » se coupait apres
        « M. », et « Que doit faire M. » fait dix-sept signes -- au-dessus du
        seuil des douze, donc compte comme une phrase.

    Refuser une traduction juste est aussi grave qu'en accepter une fausse :
    la fois suivante, on desarme le controle au lieu de le corriger. Ce qui
    est corrige ici, c'est le COMPTEUR, pas le seuil -- une phrase perdue
    reste attrapee exactement comme avant.
    """
    # Le point d'une abreviation devient un point de liaison, qui ne coupe
    # pas. Il disparait avec la variable locale.
    #
    # Deux familles : les abreviations en capitale (M., Dr., Nr.) se
    # reconnaissent a leur forme ; les minuscules ne se reconnaissent qu'a
    # leur liste, parce qu'un point apres un mot minuscule EST normalement
    # une fin de phrase. On ne devine donc pas -- on nomme.
    t = re.sub(r"\b([A-ZÄÖÜ][A-Za-zÄÖÜäöü]{0,2})\.(?=\s)", "\\1\u2024", t.strip())
    t = re.sub(r"\b(ca|inkl|ggf|max|min|bzw|usw|etc|env|ex)\.(?=\s)",
               "\\1\u2024", t)
    return len([x for x in re.split(r"(?<=[.!?])\s+(?!»)", t) if len(x) > 12])


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
            # LE RAPPORT DE LONGUEUR NE VAUT QUE SUR LES CHAMPS LONGS.
            #
            # 0,55 a ete calibre sur des EXPLICATIONS turques amputees de leur
            # seconde phrase. Applique a une question de six mots, il ne
            # mesure plus la completude : il mesure la compacite d'une langue.
            # « Quand les stations de retrait sont-elles accessibles ? » fait
            # 54 signes ; « Коли доступні станції видачі? » en fait 29, dit
            # exactement la meme chose, et tombait a un demi-signe du seuil.
            #
            # C'est la DEUXIEME fois que ce garde-fou refuse une traduction
            # juste parce qu'il a ete regle sur une seule langue. Sous 80
            # signes, seul le compte de phrases tranche -- une phrase perdue
            # reste attrapee, et une phrase courte n'a plus a se justifier
            # d'etre courte.
            trop_court = len(fr) >= 80 and len(v) < 0.55 * len(fr)
            if phrases(v) < phrases(fr) or trop_court:
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
