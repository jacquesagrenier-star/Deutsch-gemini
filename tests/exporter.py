# -*- coding: utf-8 -*-
"""
Regenere les CSV de export/ a partir des fichiers JSON du depot.

    python tests/exporter.py            # ecrit dans export/
    python tests/exporter.py --verifier # compare sans rien ecrire

Pourquoi ce fichier existe : les CSV sont des fichiers DERIVES, et l'outil qui
les produisait ne vivait pas dans le depot. Ils ont donc pris quatre versions
de retard sans que rien ne le signale. Ici, ils se refont en une commande, et
--verifier dit en un coup d'oeil s'ils sont a jour.

Format reproduit a l'identique : UTF-8 avec BOM, separateur ";", fins de ligne
CRLF, guillemets seulement quand le contenu l'exige (QUOTE_MINIMAL). Preuve :
au moment ou ce fichier a ete ecrit, il reproduisait a l'octet pres les huit
CSV dont les donnees sources n'avaient pas change.
"""
import csv, io, json, os, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT = os.path.join(RACINE, "export")
NIVEAUX = ["A1", "A2", "B1", "B2", "C1"]
BOM = "﻿"
FIN = "\r\n"

ENTETE_VOCAB = ["type", "niveau", "categorie", "allemand", "francais", "anglais",
                "exemple_de", "exemple_fr", "exemple_en"]
ENTETE_CONJ = ["niveau", "infinitif", "traduction", "regime", "preposition",
               "sans_complement", "reflechi", "temps", "phrase_de", "phrase_fr",
               "phrase_en"]


def charger(nom):
    with io.open(os.path.join(RACINE, nom), encoding="utf-8") as f:
        return json.load(f)


def est_vhs(theme):
    return str(theme.get("id", "")).startswith("vhs_kapitel")


def libelle_vhs(theme):
    """vhs_kapitel12_b1 -> "Kapitel 12 (VHS)"."""
    num = "".join(c for c in str(theme.get("id", "")).split("_")[1] if c.isdigit())
    return "Kapitel %s (VHS)" % num


# --------------------------------------------------------------------------
#  UNE SEULE passe construit tout
# --------------------------------------------------------------------------
# wortando-vocabulaire-complet.csv est la sortie de reference : themes.json
# parcouru dans son ordre (un chapitre VHS livrant ses noms, puis ses verbes,
# puis ses adjectifs), puis les listes plates. Chaque fichier par type n'est
# qu'un FILTRE de cette liste -- c'est ce qui explique que verbe.csv commence
# par les chapitres VHS alors que nom.csv commence par le theme Familie.
def toutes_les_lignes():
    out = []

    def ajouter(type_, niveau, categorie, e, champ_mot="mot", prefixe=""):
        mot = e.get(champ_mot, "")
        if prefixe:
            mot = ("%s %s" % (e.get(prefixe, ""), mot)).strip()
        out.append([type_, niveau, categorie, mot,
                    e.get("traduction", ""), e.get("traduction_en", ""),
                    e.get("exemple", ""), e.get("exemple_fr", ""), e.get("exemple_en", "")])

    for t in charger("themes.json")["themes"]:
        niv = t.get("niveau", "")
        if est_vhs(t):
            cat = libelle_vhs(t)
            for m in t.get("mots", []) or []:
                ajouter("nom (chapitre VHS)", niv, cat, m, prefixe="genre")
            for v in t.get("verben", []) or []:
                ajouter("verbe (chapitre VHS)", niv, cat, v, champ_mot="infinitif")
            for a in t.get("adjektive", []) or []:
                ajouter("adjectif (chapitre VHS)", niv, cat, a)
        else:
            cat = t.get("nom_theme", "")
            for m in t.get("mots", []) or []:
                ajouter("nom", niv, cat, m, prefixe="genre")

    d = charger("verbe.json")
    for niv in NIVEAUX:
        for v in d.get(niv, []):
            ajouter("verbe", niv, "", v, champ_mot="infinitif")

    # adjectif.json n'a pas de champ kategorie : la colonne reste vide.
    d = charger("adjectif.json")
    for niv in NIVEAUX:
        for e in d.get(niv, []):
            ajouter("adjectif", niv, "", e)

    for fichier, type_ in [("adverbe.json", "adverbe"), ("redewendung.json", "expression")]:
        d = charger(fichier)
        for niv in NIVEAUX:
            for e in d.get(niv, []):
                ajouter(type_, niv, e.get("kategorie", ""), e)

    d = charger("funktionswort.json")
    for cle, type_ in [("konjunktionen", "conjonction"), ("partikeln", "particule modale"),
                       ("praepositionen", "preposition"), ("zahlen", "nombre")]:
        for e in d.get(cle, []) or []:
            ajouter(type_, e.get("niveau", ""), e.get("kategorie", ""), e)

    return out


def lignes_conjugaisons():
    """Un verbe = quatre lignes, une par temps."""
    TEMPS = [("Präsens", "exemple"), ("Perfekt", "perfekt"),
             ("Präteritum", "praeteritum"), ("Konjunktiv II", "konjunktiv2")]
    out = []
    d = charger("verbe.json")
    for niv in NIVEAUX:
        for v in d.get(niv, []):
            for etiquette, champ in TEMPS:
                out.append([niv, v.get("infinitif", ""), v.get("traduction", ""),
                            v.get("rektion", ""), v.get("praeposition", ""),
                            "oui" if v.get("intransitiv") else "",
                            "oui" if v.get("reflexiv") else "",
                            etiquette, v.get(champ, ""),
                            v.get(champ + "_fr", ""), v.get(champ + "_en", "")])
    return out


# Chaque fichier par type : les types de lignes qu'on garde de la passe unique.
PAR_TYPE = [
    ("wortando-nom.csv",              ["nom", "nom (chapitre VHS)"]),
    ("wortando-verbe.csv",            ["verbe", "verbe (chapitre VHS)"]),
    ("wortando-adjectif.csv",         ["adjectif", "adjectif (chapitre VHS)"]),
    ("wortando-adverbe.csv",          ["adverbe"]),
    ("wortando-expression.csv",       ["expression"]),
    ("wortando-conjonction.csv",      ["conjonction"]),
    ("wortando-particule-modale.csv", ["particule modale"]),
    ("wortando-preposition.csv",      ["preposition"]),
    ("wortando-nombre.csv",           ["nombre"]),
]


def rendre(entete, lignes):
    tampon = io.StringIO()
    w = csv.writer(tampon, delimiter=";", lineterminator=FIN, quoting=csv.QUOTE_MINIMAL)
    w.writerow(entete)
    w.writerows(lignes)
    return BOM + tampon.getvalue()


def produire():
    """Le contenu attendu de chaque CSV, sans rien ecrire sur le disque.

    Separe de main() pour que tests/verifier.py puisse s'en servir et signaler
    un export en retard sans avoir a le regenerer.
    """
    maitre = toutes_les_lignes()
    produits = {"wortando-vocabulaire-complet.csv": rendre(ENTETE_VOCAB, maitre),
                "wortando-verbe-conjugaisons.csv": rendre(ENTETE_CONJ, lignes_conjugaisons())}
    for nom, types in PAR_TYPE:
        garde = set(types)
        produits[nom] = rendre(ENTETE_VOCAB, [l for l in maitre if l[0] in garde])
    return produits


def main():
    verifier = "--verifier" in sys.argv
    ecarts = 0
    produits = produire()

    for nom in sorted(produits):
        chemin = os.path.join(EXPORT, nom)
        neuf = produits[nom]
        ancien = None
        if os.path.exists(chemin):
            ancien = io.open(chemin, encoding="utf-8-sig", newline="").read()
            if ancien and not ancien.startswith(BOM):
                ancien = BOM + ancien
        nb = neuf.count(FIN) - 1
        if ancien == neuf:
            print("   %-38s identique   (%d lignes)" % (nom, nb))
        elif ancien is None:
            print("   %-38s NOUVEAU     (%d lignes)" % (nom, nb))
            ecarts += 1
        else:
            a, b = ancien.split(FIN), neuf.split(FIN)
            diff = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
            print("   %-38s DIFFERE     (%d -> %d lignes, 1er ecart ligne %d)"
                  % (nom, len(a) - 1, nb, diff + 1))
            if verifier and diff < min(len(a), len(b)):
                print("        - %s" % a[diff][:150])
                print("        + %s" % b[diff][:150])
            ecarts += 1
        if not verifier:
            io.open(chemin, "w", encoding="utf-8", newline="").write(neuf)

    if verifier:
        print("")
        print("Les CSV sont a jour." if not ecarts
              else "%d fichier(s) a regenerer : python tests/exporter.py" % ecarts)
        return 1 if ecarts else 0
    print("")
    print("%d fichiers ecrits dans export/" % len(produits))
    return 0


if __name__ == "__main__":
    sys.exit(main())
