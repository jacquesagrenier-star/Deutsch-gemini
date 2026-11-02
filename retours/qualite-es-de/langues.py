# -*- coding: utf-8 -*-
"""Langue x contenu : chaque texte francais a-t-il sa traduction, dans la bonne
langue, alignee sur la source ?

    python retours/qualite-es-de/langues.py de|es [sortie.json]

Familles de signalements (cle « code ») :
  manquant        le champ n'existe pas alors que d'autres langues l'ont
  vide            le champ existe, vide
  copie_fr        identique au francais, alors que l'anglais en differe
  copie_en        identique a l'anglais (langue autre que l'anglais), le francais differe
  ecriture        uk/ru sans cyrillique, fa/ar sans alphabet arabe, ou l'inverse
  uk_russe / ru_ukrainien / ar_persan / fa_arabe   lettres de la langue voisine
  francais / anglais / espagnol   au moins deux mots-marqueurs hors citation
  chiffres        les nombres de la traduction ne sont pas ceux de la source
  question        la source est une question et pas la traduction (ou l'inverse)
  voisin          la traduction est celle de l'enregistrement voisin
"""
import collections
import json
import re
import sys

from commun import (sans_citations, mots, LANGUES, FICHIERS, charger, groupes, ecritures, marqueurs,
                    MARQUEURS_FR, MARQUEURS_EN, MARQUEURS_ES, LETTRES_PERSANES,
                    LETTRES_ARABES_SEULES, LETTRES_RUSSES, LETTRES_UKRAINIENNES,
                    nombres, question)

CHAMPS_PHRASE = ("exemple", "translation", "trad", "phrase", "frage", "consigne",
                 "perfekt", "praeteritum", "konjunktiv2")


def est_phrase(cle):
    return any(cle.startswith(c) for c in CHAMPS_PHRASE) or cle == ""


FORTS_FR = {"les", "une", "est", "avec", "dans", "nous", "vous", "elle",
            "très", "sont", "pour", "cette", "leur", "votre", "notre", "être",
            "avoir", "aussi", "beaucoup", "toujours", "déjà", "c'est",
            "n'est", "qu'il", "aujourd'hui", "j'ai", "pluriel", "singulier",
            "masculin", "neutre", "féminin", "ça", "dépend", "réponse", "ou",
            "et", "le", "du", "au", "aux", "je"}


# champs ecrits dans la langue apprise : identiques partout, ce n'est pas un oubli
CLES_SOURCE = {"question", "options", "correct", "answers", "chunks"}


def signal_fr(fr):
    return bool(set(mots(sans_citations(fr))) & FORTS_FR)


def juger(app, cle, fr, l, t, tous, src):
    if cle == "article":          # article_fr : l'article francais seul, sans traduction
        return []
    pb = []
    en = tous.get("en")
    neutre = (en is None or en == fr) and (not signal_fr(fr) or cle in CLES_SOURCE)
    if t is None:
        return [] if neutre else ["manquant"]
    if not t.strip():
        return ["vide"] if fr.strip() else []
    if neutre and t == fr:
        return []
    lettres_fr = sum(c.isalpha() for c in fr)
    plusieurs = len(fr.split()) >= 2
    if t == fr and lettres_fr >= 4 and en is not None and en != fr and l != "en"             and t != src and (plusieurs or l not in ("pt", "de")):
        pb.append("copie_fr")
    if l == "en" and t == fr and plusieurs and signal_fr(fr) and t != src:
        pb.append("copie_fr")
    if l != "en" and en and t == en and en != fr and sum(c.isalpha() for c in en) >= 4             and t != src and (len(en.split()) >= 3 or marqueurs(en, l, MARQUEURS_EN)):
        pb.append("copie_en")
    lat, cyr, arb = ecritures(t)
    if l in ("uk", "ru") and lat >= 3 and cyr == 0:
        pb.append("ecriture")
    elif l in ("fa", "ar") and lat >= 3 and arb == 0:
        pb.append("ecriture")
    elif l not in ("uk", "ru", "fa", "ar") and (cyr or arb):
        pb.append("ecriture")
    if l == "uk" and set(t) & LETTRES_RUSSES:
        pb.append("uk_russe")
    if l == "ru" and set(t) & LETTRES_UKRAINIENNES:
        pb.append("ru_ukrainien")
    if l == "ar" and set(t) & LETTRES_PERSANES:
        pb.append("ar_persan")
    if l == "fa" and set(t) & LETTRES_ARABES_SEULES:
        pb.append("fa_arabe")
    if l in ("en", "tr", "pt", "pl", "de"):
        if len(marqueurs(t, l, MARQUEURS_FR)) >= 2:
            pb.append("francais")
        if l != "en" and len(marqueurs(t, l, MARQUEURS_EN)) >= 2:
            pb.append("anglais")
        if l == "pt" and app == "es" and est_phrase(cle) and \
                len(marqueurs(t, l, MARQUEURS_ES)) >= 2:
            pb.append("espagnol")
    ref = src if src else fr
    if est_phrase(cle) and nombres(ref) != nombres(t) and nombres(fr) != nombres(t):
        pb.append("chiffres")
    if est_phrase(cle) and src and question(src) != question(t) and question(fr) != question(t):
        pb.append("question")
    return pb


def voisins(donnees, app):
    """Une traduction egale a celle du voisin immediat, quand le francais differe."""
    out = []

    def listes(o, ch):
        if isinstance(o, list):
            if len(o) > 1 and all(isinstance(e, dict) for e in o):
                yield ch, o
            for i, e in enumerate(o):
                yield from listes(e, "%s[%d]" % (ch, i))
        elif isinstance(o, dict):
            for k, v in o.items():
                yield from listes(v, "%s.%s" % (ch, k))

    for ch, lst in listes(donnees, ""):
        for i in range(len(lst) - 1):
            a, b = lst[i], lst[i + 1]
            for k, va in a.items():
                if not isinstance(va, str) or len(va) < 6:
                    continue
                m = SUFFIXE_L.match(k)
                if not m:
                    continue
                base, l = m.group(1), m.group(2)
                if l == "fr" or l not in LANGUES[app]:
                    continue
                vb = b.get(k)
                if va != vb:
                    continue
                fa_, fb = a.get(base + "_fr", a.get(base)), b.get(base + "_fr", b.get(base))
                if fa_ == fb:
                    continue
                autres = [x for x in LANGUES[app] if x != l and isinstance(a.get(base + "_" + x), str)]
                pareils = sum(a.get(base + "_" + x) == b.get(base + "_" + x) for x in autres)
                if autres and pareils / len(autres) >= 0.5:
                    continue
                out.append({"chemin": "%s[%d]/[%d]" % (ch, i, i + 1), "cle": k, "code": "voisin",
                            "langue": l, "fr_a": fa_, "fr_b": fb, "texte": va,
                            "src_a": a.get(base) if base + "_fr" in a else None,
                            "src_b": b.get(base) if base + "_fr" in b else None})
    return out


import re
SUFFIXE_L = re.compile(r"^(.*)_(fr|en|tr|uk|fa|ar|pt|pl|ru|de)$")


def main():
    app = sys.argv[1]
    sortie = sys.argv[2] if len(sys.argv) > 2 else None
    langues = LANGUES[app]
    tous = []
    total = collections.Counter()
    for f in FICHIERS[app]:
        d = charger(f)
        for chemin, cle, fr, trads, src, obj in groupes(d, langues):
            for l, t in trads.items():
                total[(f, l)] += 1
                for code in juger(app, cle, fr, l, t, trads, src):
                    tous.append({"fichier": f, "chemin": chemin, "cle": cle, "langue": l,
                                 "code": code, "fr": fr, "src": src, "texte": t,
                                 "en": trads.get("en")})
        for v in voisins(d, app):
            v["fichier"] = f
            tous.append(v)
    par = collections.Counter((x["code"], x["langue"]) for x in tous)
    print("Textes examines :", sum(total.values()))
    for (code, l), n in sorted(par.items()):
        print("  %-14s %-3s %6d" % (code, l, n))
    if sortie:
        json.dump({"total": {"%s|%s" % k: v for k, v in total.items()}, "signalements": tous},
                  open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
