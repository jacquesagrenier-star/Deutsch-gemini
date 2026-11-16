# -*- coding: utf-8 -*-
"""« L'heure et les dates » (theme illustre, 16 nov. 2026) : les mots du theme, tires du CORPUS, et leurs traductions.

    python visuel/heure/heure.py        # ecrit visuel/prototype/heure/heure.json

Les phrases ne sont pas ici : elles sortent de visuel/prototype/heure/dire.js (une heure, une date, un rendez-vous ->
la phrase de chaque langue). Ce script ne fait que la liste des mots que la page fait travailler (cles de la
progression commune aux cartes, a la forme du corpus) et, pour chacun, sa traduction dans chaque langue d'interface,
prise dans le corpus relu (themes.json, adjectif.json, adverbe.json ; espanol/datos ; anglais/datos). Un mot absent
du corpus ARRETE le script : il serait « hors jeu » dans l'app, jamais demande.

Les images sont dessinees par la page (horloges, montres, calendriers, agenda) : aucune generation payante.
"""
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
SORTIE = os.path.join(RACINE, "visuel", "prototype", "heure", "heure.json")

JOURS_DE = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
MOIS_DE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
JOURS_ES = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MOIS_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
JOURS_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MOIS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# (mot, genre ou None, cat ou None) -- la forme du corpus ; nom : genre ; adjectif, adverbe : cat
MOTS = {
    "de": [("Uhr", "die", None), ("Uhrzeit", "die", None), ("Viertel", "das", None), ("halb", None, "adjectif"),
           ("Stunde", "die", None), ("Minute", "die", None), ("Mittag", "der", None), ("Mitternacht", "die", None),
           ("morgens", None, "adverbe"), ("mittags", None, "adverbe"), ("abends", None, "adverbe"), ("nachts", None, "adverbe")]
          + [(j, "der", None) for j in JOURS_DE] + [(m, "der", None) for m in MOIS_DE]
          + [("Datum", "das", None), ("Termin", "der", None), ("Geburtstag", "der", None), ("Kalender", "der", None),
             ("Wochenende", "das", None), ("heute", None, "adverbe"), ("morgen", None, "adverbe"), ("gestern", None, "adverbe")],
    "es": [("hora", "la", None), ("minuto", "el", None), ("reloj", "el", None), ("mediodía", "el", None), ("medianoche", "la", None),
           ("mañana", "la", None), ("tarde", "la", None), ("noche", "la", None)]
          + [(j, "el", None) for j in JOURS_ES] + [(m, "el", None) for m in MOIS_ES]
          + [("fecha", "la", None), ("cita", "la", None), ("cumpleaños", "el", None), ("calendario", "el", None),
             ("fin de semana", "el", None), ("hoy", None, "adverbe"), ("mañana", None, "adverbe"), ("ayer", None, "adverbe")],
    "en": [("clock", "", None), ("watch", "", None), ("hour", "", None), ("minute", "", None), ("half", "", None), ("quarter", "", None),
           ("noon", "", None), ("midnight", "", None), ("morning", "", None), ("afternoon", "", None), ("evening", "", None), ("night", "", None)]
          + [(j, "", None) for j in JOURS_EN] + [(m, "", None) for m in MOIS_EN]
          + [("date", "", None), ("appointment", "", None), ("birthday", "", None), ("calendar", "", None), ("weekend", "", None),
             ("today", None, "adverbe"), ("tomorrow", None, "adverbe"), ("yesterday", None, "adverbe")],
}
# les langues d'interface de chaque langue apprise (le francais d'abord) et le champ du corpus qui les traduit
UI = {"de": ["fr", "en", "tr", "uk", "fa", "ar", "pt", "pl", "ru"], "es": ["fr", "en", "pt", "ar", "de"], "en": ["fr"]}


def lire(chemin):
    return json.load(open(os.path.join(RACINE, chemin), encoding="utf-8"))


def entrees(o, out):
    """Toutes les entrees {mot: ...} d'un fichier, ou qu'elles soient."""
    if isinstance(o, dict):
        if isinstance(o.get("mot"), str):
            out.append(o)
        for v in o.values():
            entrees(v, out)
    elif isinstance(o, list):
        for v in o:
            entrees(v, out)
    return out


SOURCES = {
    "de": {"nom": ["themes.json"], "adjectif": ["adjectif.json"], "adverbe": ["adverbe.json"]},
    "es": {"nom": ["espanol/datos/temas.json"], "adjectif": ["espanol/datos/adjetivos.json"], "adverbe": ["espanol/datos/adverbios.json"]},
    "en": {"nom": ["anglais/datos/themes.json"], "adjectif": ["anglais/datos/adjectifs.json"], "adverbe": ["anglais/datos/adverbes.json"]},
}


def main():
    sortie = {"mots": {}, "gloses": {}}
    manque = []
    for L, mots in MOTS.items():
        corpus = {k: [e for f in fs for e in entrees(lire(f), [])] for k, fs in SOURCES[L].items()}
        sortie["mots"][L], sortie["gloses"][L] = [], {}
        for mot, genre, cat in mots:
            liste = corpus[cat or "nom"]
            # un nom : le genre doit concorder (un nom anglais a le genre "" au corpus)
            e = next((x for x in liste if x["mot"] == mot and (cat or genre is None or (x.get("genre") or "") == genre)), None)
            if not e:
                manque.append("%s : %s (%s)" % (L, mot, cat or genre))
                continue
            m = {"mot": mot}
            if cat:
                m["cat"] = cat
            else:
                m["genre"] = genre
            # la cle : deux cartes d'un meme mot (la manana, le matin ; manana, demain)
            cle = mot + ("~adv" if cat == "adverbe" and any(x[0] == mot and not x[2] for x in mots) else "")
            if cle != mot:
                m["cle"] = cle
            sortie["mots"][L].append(m)
            sortie["gloses"][L][cle] = {lg: (e.get("traduction") if lg == "fr" else e.get("traduction_" + lg)) or "" for lg in UI[L]}
            vides = [lg for lg, v in sortie["gloses"][L][cle].items() if not v]
            if vides:
                print("  sans traduction : %s %s -> %s" % (L, mot, ", ".join(vides)))
    if manque:
        print("ABSENTS DU CORPUS (a ajouter avant tout) :\n  " + "\n  ".join(manque))
        sys.exit(1)
    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    with open(SORTIE, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    print("ecrit : %s (%s)" % (os.path.relpath(SORTIE, RACINE), ", ".join("%s %d mots" % (L, len(v)) for L, v in sortie["mots"].items())))


if __name__ == "__main__":
    main()
