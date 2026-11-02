# -*- coding: utf-8 -*-
"""Outils communs du controle de qualite espagnol + allemand (2 nov. 2026).

Un « groupe » est un texte francais et ses traductions, tel que les donnees le
rangent. Les donnees en ont quatre formes, et le marcheur les reconnait toutes :

    exemple / exemple_fr / exemple_en ...     (source dans « exemple »)
    traduction / traduction_en ...            (le francais sans suffixe)
    correct / correctEn / correctTr ...       (exercices allemands)
    {"fr": ..., "en": ..., "pt": ...}         (fiches, Premiers pas, reperes)

Chaque groupe sort avec son chemin dans le fichier, pour qu'un signalement
renvoie a un endroit precis.
"""
import io
import json
import os
import re
import unicodedata

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LANGUES = {
    # langue apprise -> langues d'interface autres que le francais
    "de": ["en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"],
    "es": ["en", "pt", "ar", "de"],
}
TOUTES = {"fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru", "de", "es"}
SUFFIXE = re.compile(r"_(fr|en|tr|uk|fa|ar|pt|pl|ru|de)$")

FICHIERS = {
    "de": ["themes.json", "verbe.json", "adjectif.json", "adverbe.json",
           "redewendung.json", "funktionswort.json", "grammaire.json",
           "conjugaison.json", "prononciation.json", "reperes.json",
           "premiers-pas.json", "a1-voyage.json", "exercices.json",
           "pruefung.json"],
    "es": ["espanol/datos/" + f for f in (
        "temas.json", "verbos.json", "adjetivos.json", "adverbios.json",
        "expresiones.json", "funcionales.json", "grammaire.json",
        "conjugaison.json", "prononciation.json", "reperes.json",
        "premiers-pas.json", "a1-voyage.json", "ejercicios.json",
        "variantes.json")],
}


def charger(rel):
    with io.open(os.path.join(RACINE, rel), encoding="utf-8") as f:
        return json.load(f)


def en_texte(v):
    if isinstance(v, str):
        return v
    if isinstance(v, list) and all(isinstance(x, str) for x in v):
        return " | ".join(v)
    return None


def groupes(obj, langues, chemin=""):
    """Rend (chemin, cle, fr, {langue: texte ou None}, source ou None, dict)."""
    if isinstance(obj, list):
        for i, e in enumerate(obj):
            yield from groupes(e, langues, "%s[%d]" % (chemin, i))
        return
    if not isinstance(obj, dict):
        return
    # forme 4 : un dictionnaire de langues
    if isinstance(obj.get("fr"), (str, list)) and any(l in obj for l in langues):
        fr = en_texte(obj["fr"])
        if fr is not None:
            yield (chemin, "", fr, {l: en_texte(obj.get(l)) if l in obj else None
                                    for l in langues}, None, obj)
    for k, v in obj.items():
        if isinstance(v, (dict, list)) and not en_texte(v):
            yield from groupes(v, langues, "%s.%s" % (chemin, k))
            continue
        t = en_texte(v)
        if t is None:
            continue
        if k.endswith("_fr"):
            base = k[:-3]
            src = en_texte(obj.get(base)) if base in obj else None
            yield (chemin, base, t, {l: en_texte(obj.get(base + "_" + l))
                                     if (base + "_" + l) in obj else None
                                     for l in langues}, src, obj)
        elif not SUFFIXE.search(k) and (k + "_fr") not in obj and \
                any((k + "_" + l) in obj for l in langues):
            yield (chemin, k, t, {l: en_texte(obj.get(k + "_" + l))
                                  if (k + "_" + l) in obj else None
                                  for l in langues}, None, obj)
        elif not SUFFIXE.search(k) and any((k + l.capitalize()) in obj for l in langues):
            yield (chemin, k, t, {l: en_texte(obj.get(k + l.capitalize()))
                                  if (k + l.capitalize()) in obj else None
                                  for l in langues}, None, obj)


# ---------------------------------------------------------------- ecritures

def ecritures(t):
    lat = cyr = arb = 0
    for ch in t:
        if not ch.isalpha():
            continue
        o = ord(ch)
        if 0x0400 <= o <= 0x04FF:
            cyr += 1
        elif 0x0600 <= o <= 0x06FF or 0x0750 <= o <= 0x077F or 0xFB50 <= o <= 0xFEFF:
            arb += 1
        elif o < 0x0250 or 0x1E00 <= o <= 0x1EFF:
            lat += 1
    return lat, cyr, arb


CITATION = re.compile(r"«[^»]*»|„[^“”]*[“”]|“[^”]*”|\"[^\"]*\"|\([^)]*\)|\[[^\]]*\]")


def sans_citations(t):
    return CITATION.sub(" ", t)


def mots(t):
    return re.findall(r"[^\W\d_]+(?:'[^\W\d_]+)?", t.lower())


# Marqueurs choisis pour ne pas exister dans la langue cible (voir le rapport).
MARQUEURS_FR = {"les", "une", "est", "avec", "dans", "nous", "vous", "elle",
                "très", "sont", "pour", "cette", "leur", "votre", "notre",
                "être", "avoir", "aussi", "beaucoup", "toujours", "déjà",
                "c'est", "n'est", "qu'il", "aujourd'hui", "j'ai", "il",
                "ils", "elles", "mon", "ton", "ses", "ces", "quand"}
MARQUEURS_EN = {"the", "and", "with", "you", "are", "this", "that", "have",
                "has", "of", "is", "for", "what", "where", "my", "your",
                "it", "they", "we", "today"}
MARQUEURS_ES = {"muy", "el", "los", "las", "y", "pero", "también", "hay",
                "mucho", "ella", "usted", "hoy", "qué", "dónde", "yo"}
# exceptions par langue cible : ces formes existent aussi dans la langue
EXCEPTIONS = {
    "tr": {"il", "on", "en", "son", "mon", "ses", "ton"},
    "pl": {"je", "pas", "mon", "ton", "ten", "it"},
    "pt": {"mais", "les", "une", "ses", "quando", "son", "y"},
    "de": {"des", "je", "mon", "ton", "ses", "so", "was", "an", "in", "hat",
           "die", "it", "elf", "ist"},
    "en": {"les", "son", "mon", "ton", "ses", "est", "elle"},
}


def marqueurs(t, langue, jeu):
    mm = set(mots(sans_citations(t)))
    return sorted((mm & jeu) - EXCEPTIONS.get(langue, set()))


LETTRES_PERSANES = set("پچژگیک")  # پ چ ژ گ ی ک
LETTRES_ARABES_SEULES = set("يك")                      # ي ك
LETTRES_RUSSES = set("ыэъёЫЭЪЁ")
LETTRES_UKRAINIENNES = set("іїєґІЇЄҐ")


def nombres(t):
    t = t.translate(str.maketrans("٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹", "01234567890123456789"))
    out = []
    for n in re.findall(r"\d[\d.,٫٬ ]*\d|\d", t):
        n = re.sub(r"[.,٫٬ ]", "", n)
        out.append(n.lstrip("0") or "0")
    return sorted(out)


def question(t):
    return "?" in t or "؟" in t


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def ecrire_json(rel, donnees):
    with io.open(os.path.join(RACINE, rel), "w", encoding="utf-8", newline="\n") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)
        f.write("\n")
