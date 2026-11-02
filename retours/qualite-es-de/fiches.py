# -*- coding: utf-8 -*-
"""Fiches, tableaux, explications : chaque traduction garde-t-elle les memes
exemples dans la langue apprise que le francais ?

Une explication traduite peut reformuler ; elle ne doit ni perdre ni changer un
exemple allemand ou espagnol. On releve ce que le francais met en <b>, en <i>
ou entre guillemets et qui appartient a la langue apprise, puis on le cherche
dans chaque traduction.

    python retours/qualite-es-de/fiches.py [sortie.json]

  exemple_perdu    un exemple de la langue apprise absent de la traduction
  balises          nombre de <b> / <i> / <br> different du francais
"""
import collections
import json
import re
import sys

from commun import LANGUES, charger, groupes, norm

FICHIERS = {
    "de": ["grammaire.json", "conjugaison.json", "premiers-pas.json", "a1-voyage.json",
           "reperes.json", "prononciation.json", "exercices.json", "pruefung.json"],
    "es": ["espanol/datos/" + f for f in ("grammaire.json", "conjugaison.json", "premiers-pas.json",
                                          "a1-voyage.json", "reperes.json", "prononciation.json",
                                          "ejercicios.json", "variantes.json")],
}
SEGMENT = re.compile(r"<b>(.*?)</b>|<i>(.*?)</i>|«\s*([^»]+?)\s*»|„([^“”]+)[“”]")


def vocabulaire(app):
    """Les mots de la langue apprise, tires des donnees (pour reconnaitre un exemple)."""
    v = set()
    if app == "de":
        for t in charger("themes.json")["themes"]:
            for m in t["mots"]:
                v |= set(re.findall(r"\w+", m["exemple"].lower()))
        for f in ("verbe.json", "adjectif.json", "adverbe.json", "redewendung.json"):
            for lst in charger(f).values():
                for e in lst:
                    v |= set(re.findall(r"\w+", (e.get("exemple") or "").lower()))
    else:
        for t in charger("espanol/datos/temas.json")["themes"]:
            for m in t["mots"]:
                v |= set(re.findall(r"\w+", m["exemple"].lower()))
        for f in ("verbos.json", "adjetivos.json", "adverbios.json", "expresiones.json", "funcionales.json"):
            for lst in charger("espanol/datos/" + f).values():
                for e in lst:
                    v |= set(re.findall(r"\w+", (e.get("exemple") or "").lower()))
    return v


FR_COURANTS = {"le", "la", "les", "de", "des", "un", "une", "et", "ou", "est", "en", "à", "au",
               "du", "il", "elle", "on", "ne", "pas", "que", "qui", "se", "ce", "je", "tu",
               "nous", "vous", "ils", "mais", "pour", "par", "avec", "sur", "dans", "sans"}


def est_apprise(seg, vocab):
    mots = re.findall(r"\w+", seg.lower())
    if not mots:
        return False
    connus = [m for m in mots if m in vocab and m not in FR_COURANTS]
    return len(connus) >= max(1, (len(mots) + 1) // 2)


def main():
    out = []
    for app in ("de", "es"):
        vocab = vocabulaire(app)
        n = 0
        for f in FICHIERS[app]:
            d = charger(f)
            for chemin, cle, fr, trads, src, obj in groupes(d, LANGUES[app]):
                if src:      # exemple / exemple_fr : la source est a part, pas citee
                    continue
                segs = []
                for m in SEGMENT.finditer(fr):
                    s = next(g for g in m.groups() if g is not None)
                    s = re.sub(r"<[^>]+>", "", s).strip(" .,;:!?")
                    if s and est_apprise(s, vocab):
                        segs.append(s)
                tags = {t: len(re.findall("<%s>" % t, fr)) for t in ("b", "i")}
                for l, t in trads.items():
                    if not t:
                        continue
                    n += 1
                    nt = norm(t)
                    perdus = [s for s in segs if norm(s) not in nt]
                    if perdus:
                        out.append({"app": app, "fichier": f, "chemin": chemin, "cle": cle, "langue": l,
                                    "code": "exemple_perdu", "perdus": perdus, "fr": fr, "texte": t})
                    tt = {x: len(re.findall("<%s>" % x, t)) for x in ("b", "i")}
                    if tt != tags and sum(tags.values()):
                        out.append({"app": app, "fichier": f, "chemin": chemin, "cle": cle, "langue": l,
                                    "code": "balises", "fr_balises": tags, "balises": tt, "fr": fr, "texte": t})
        print(app, "textes compares :", n)
    c = collections.Counter((o["app"], o["code"], o["langue"]) for o in out)
    for k, v in sorted(c.items()):
        print("  ", k, v)
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
