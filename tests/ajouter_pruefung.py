# -*- coding: utf-8 -*-
"""Ajoute des exercices d'examen a pruefung.json, en refusant ce qui est faux.

    python tests/ajouter_pruefung.py mon_lot.json

Le fichier d'entree a la meme forme que pruefung.json -- un objet dont les
cles sont « sprechen », « schreiben », « lesen », « hoeren » -- mais ne
contient que les entrees a ajouter.

POURQUOI UN OUTIL PLUTOT QU'UN COPIER-COLLER. Trois defauts de ce contenu-la
ne se voient pas en relisant le JSON, et se paient en jouant la serie :

  1. Un « bon » different de 0. Le fichier tient la bonne reponse en premiere
     position, et le melange se fait a la construction de l'exercice. Une
     entree qui derogerait a la convention resterait juste, mais la prochaine
     relecture humaine lirait la mauvaise reponse comme la bonne.
  2. Des listes d'options de longueurs differentes selon la langue. L'ecran
     affiche les options de la langue d'interface et compare au texte de la
     bonne reponse : une liste plus courte en turc fait disparaitre la bonne
     reponse des boutons, et l'exercice devient impossible -- en turc
     seulement, donc invisible a qui teste en francais.
  3. Un champ absent. Le convertisseur de index.html lit `o.erkl_en` sans
     filet ; un champ manquant donne « undefined » a l'ecran.

Le verificateur du projet ne voit rien de tout cela : pruefung.json n'est pas
un fichier de vocabulaire, il n'a pas la meme grammaire.
"""
import io
import json
import os
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIBLE = os.path.join(RACINE, "pruefung.json")

LANGUES = ("fr", "en", "tr")

# Les champs exiges, section par section. Le nom nu (« frage », « text »,
# « audio ») porte l'allemand ; les suffixes portent les trois langues
# d'interface.
CHAMPS = {
    "sprechen":  ["niveau", "teil", "frage", "chunks",
                  "consigne_", "trad_", "erkl_"],
    "schreiben": ["niveau", "typ", "chunks",
                  "aufgabe_", "trad_", "erkl_"],
    "hoeren":    ["niveau", "audio", "bon",
                  "frage_", "options_", "erkl_"],
    "lesen":     ["niveau", "typ", "text", "fragen"],
}
CHAMPS_QUESTION = ["bon", "frage_", "options_", "erkl_"]


def developper(champs):
    """« erkl_ » devient erkl_fr, erkl_en, erkl_tr ; le reste ne bouge pas."""
    out = []
    for c in champs:
        if c.endswith("_"):
            out.extend(c + lg for lg in LANGUES)
        else:
            out.append(c)
    return out


class Refus(Exception):
    pass


def verifier_options(o, ou):
    n = len(o["options_fr"])
    for lg in LANGUES:
        if len(o["options_" + lg]) != n:
            raise Refus("%s : %d options en fr mais %d en %s -- la bonne "
                        "reponse disparaitrait des boutons dans cette langue"
                        % (ou, n, len(o["options_" + lg]), lg))
    if o["bon"] != 0:
        raise Refus("%s : bon = %d. La convention du fichier est que la bonne "
                    "reponse vienne en premier (bon = 0)." % (ou, o["bon"]))


def verifier(section, entree, ou):
    manquants = [c for c in developper(CHAMPS[section]) if c not in entree]
    if manquants:
        raise Refus("%s : champ(s) absent(s) -- %s" % (ou, ", ".join(manquants)))

    if entree["niveau"] not in ("A1", "A2", "B1", "B2", "C1"):
        raise Refus("%s : niveau inattendu « %s »" % (ou, entree["niveau"]))

    if section in ("sprechen", "schreiben"):
        if len(entree["chunks"]) < 3:
            raise Refus("%s : %d blocs seulement -- l'exercice se resout au "
                        "hasard" % (ou, len(entree["chunks"])))
    elif section == "hoeren":
        verifier_options(entree, ou)
    elif section == "lesen":
        if not entree["fragen"]:
            raise Refus("%s : texte sans aucune question" % ou)
        for i, q in enumerate(entree["fragen"]):
            oq = "%s, question %d" % (ou, i + 1)
            absents = [c for c in developper(CHAMPS_QUESTION) if c not in q]
            if absents:
                raise Refus("%s : champ(s) absent(s) -- %s"
                            % (oq, ", ".join(absents)))
            verifier_options(q, oq)


def identite(section, e):
    """De quoi reconnaitre un doublon, section par section."""
    if section == "lesen":
        return e["text"]
    if section == "hoeren":
        return e["audio"]
    return e["frage"] if section == "sprechen" else e["aufgabe_fr"]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1

    with io.open(sys.argv[1], encoding="utf-8") as f:
        lot = json.load(f)
    with io.open(CIBLE, encoding="utf-8") as f:
        cible = json.load(f)

    ajoutes = refuses = 0
    for section, entrees in lot.items():
        if section not in CHAMPS:
            print("  ! section inconnue « %s » -- ignoree" % section)
            continue
        deja = {identite(section, e) for e in cible[section]}
        for e in entrees:
            ou = "%s / %s" % (section, str(identite(section, e))[:45]
                              .replace("\n", " / "))
            try:
                verifier(section, e, ou)
                if identite(section, e) in deja:
                    raise Refus("%s : deja present" % ou)
            except Refus as err:
                print("  ! %s" % err)
                refuses += 1
                continue
            cible[section].append(e)
            deja.add(identite(section, e))
            ajoutes += 1

    if ajoutes:
        with io.open(CIBLE, "w", encoding="utf-8") as f:
            json.dump(cible, f, ensure_ascii=False, indent=1)
            f.write(u"\n")

    print("  %d ajoutes, %d refuses" % (ajoutes, refuses))
    for s in ("sprechen", "schreiben", "lesen", "hoeren"):
        n = len(cible[s])
        extra = ""
        if s == "lesen":
            extra = " (%d questions)" % sum(len(o["fragen"]) for o in cible[s])
        print("     %-10s %3d%s" % (s, n, extra))
    return 1 if refuses else 0


if __name__ == "__main__":
    sys.exit(main())
