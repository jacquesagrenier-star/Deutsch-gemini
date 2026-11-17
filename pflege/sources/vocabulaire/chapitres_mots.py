# -*- coding: utf-8 -*-
"""Le chapitre de « Ma journée au service » de chaque mot qui ne suit pas le chapitre de son thème
(décision de Jacques du 16 nov. 2026 ; chapitres : pflege/sources/chapitres.py, ids définitifs).

Un mot sans ligne ici prend le chapitre de son thème (THEME_DEFAUT de chapitres.py). Les paires
(soins_sprache) et les objets des scènes (soins_szenen) n'ont pas de chapitre par défaut : ils sont
tous ici. Un mot nouveau porte plutôt son chapitre dans sa source (option chapitre="…").

Le chapitre ne touche pas à la progression (rangée par thème, niveau et rang) : on peut déplacer un
mot d'un chapitre à l'autre sans rien perdre.

Clé : le module de la source (tNN_*), puis le mot tel que la carte l'affiche (pour une paire : le côté
du service).
"""

AUFNAHME, MORGEN, MOBIL, ESSEN, MEDIK, VISITE, SCHMERZ, UEBERGABE, DOKU, TELEFON, ANGEH, NOTFALL, ENTLASS, PAUSE = (
    "ch01_aufnahme", "ch02_morgenpflege", "ch03_mobilisation", "ch04_essen", "ch05_medikamente", "ch06_visite",
    "ch07_schmerz", "ch08_uebergabe", "ch09_dokumentation", "ch10_telefon", "ch11_angehoerige", "ch12_notfall",
    "ch13_entlassung", "ch14_pause")


def _table(**groupes):
    t = {}
    for ch, mots in groupes.items():
        for m in mots:
            assert m not in t, m
            t[m] = ch
    return t


CHAPITRES_MOTS = {
    # ── les soins de base : se lever, bouger, s'installer (le reste suit « Les soins du matin ») ──
    "t02_grundpflege": _table(**{
        MOBIL: ["aufstehen", "sich hinlegen", "sich hinsetzen", "Rollstuhl", "lagern", "umlagern",
                "die Seitenlage / die Rückenlage", "das Kopfteil hochstellen", "mobilisieren", "Mobilisation",
                "an die Bettkante setzen", "Rollator", "Gehhilfe", "Unterstützung brauchen", "selbstständig",
                "die aktivierende Pflege", "Ressource", "Druckentlastung", "30-Grad-Lagerung",
                "Wechseldruckmatratze", "Kontrakturenprophylaxe", "Sturzprophylaxe", "Thromboseprophylaxe",
                "Pneumonieprophylaxe", "Kompressionsstrumpf", "Transfer", "rückenschonend arbeiten",
                "Rutschbrett", "Patientenlifter", "Gangunsicherheit", "die Teilbelastung / die Vollbelastung"],
    }),
    # ── la documentation : l'admission, la relève, le téléphone, la sortie ──
    "t09_dokumentation": _table(**{
        AUFNAHME: ["Formular", "Geburtsdatum", "unterschreiben", "Unterschrift", "Aufnahmebogen", "Pflegeanamnese",
                   "Strukturierte Informationssammlung (SIS)", "die AEDL / die ATL", "Vorerkrankung", "Hilfebedarf",
                   "Einverständniserklärung", "Aufklärungsgespräch"],
        UEBERGABE: ["Übergabe", "übergeben", "Beobachtung", "Allgemeinzustand", "o. B. (ohne Befund)",
                    "Pat. hat gut geschlafen.", "AZ / EZ", "reduzierter AZ"],
        TELEFON: ["zurückrufen", "durchstellen", "Durchwahl", "Ich verbinde Sie.", "SBAR-Schema", "Laborwerte",
                  "Schweigepflicht", "Schweigepflichtentbindung"],
        ENTLASS: ["Entlassmanagement", "Überleitungsbogen", "Pflegegrad", "Medizinische Dienst (MD)", "Entlassbrief",
                  "Anschlussheilbehandlung (AHB)"],
    }),
    "t08_team": _table(**{
        AUFNAHME: ["Station", "Zimmer", "Patient"],
        UEBERGABE: ["Frühdienst", "Spätdienst", "Nachtdienst", "die Bezugspflege / die Bereichspflege", "zuständig",
                    "Zuständigkeit"],
        VISITE: ["Arzt", "Visite"],
    }),
    "t10_angehoerige": _table(**{
        TELEFON: ["Auskunft"],
        ENTLASS: ["Kurzzeitpflege"],
    }),
    # ── les objets des scènes : le chapitre de leur scène, ou de leur usage ──
    "t11_szenen": _table(**{
        AUFNAHME: ["Gehstock", "Mappe", "Einweisungsschein", "Allergiepass", "Wertsachen", "Wertsachenbeutel",
                   "Messlatte", "Anamnese", "Patientenarmband"],
        MORGEN: ["Hörgerät", "Bettdecke", "Prothesendose", "Desinfektionsmittelspender", "Sichtschutz",
                 "Zahnputzbecher", "Duschstuhl", "Haltegriff", "Notrufschnur", "Toilettensitzerhöhung",
                 "Antirutschmatte"],
        MOBIL: ["Hausschuh", "Pflegebett", "Bettgitter", "Kopfteil", "Handlauf", "Krücke"],
        ESSEN: ["Wasserglas", "Becher", "Trinkstation"],
        MEDIK: ["Infusionsständer", "Medikamentenschrank", "Medikamentenwagen", "Betäubungsmittelschrank"],
        VISITE: ["Nasenbrille", "Sauerstoff", "Visitenwagen", "Röntgenbild"],
        UEBERGABE: ["Übergabeliste", "Klemmbrett", "Notizblock"],
        PAUSE: ["Pinnwand", "Spind", "Wasserkocher", "Brotdose"],
    }),
    # ── les paires « dit le patient / dit le service » : là où on les entend ──
    "t12_sprache": _table(**{
        SCHMERZ: ["die Abdominalschmerzen", "die thorakalen Schmerzen", "stechende Schmerzen",
                  "ausstrahlende Schmerzen", "die Lumbalgie", "die Parästhesien", "die Übelkeit", "erbrechen",
                  "der Schwindel", "der Tinnitus", "der Juckreiz", "die Schlafstörung", "der Tremor"],
        MORGEN: ["die Inkontinenzvorlage", "der Stuhlgang", "Wasser lassen", "die Miktion", "die Obstipation",
                 "die Diarrhö", "der Meteorismus", "die Harninkontinenz", "der häufige Harndrang", "die Nykturie",
                 "die Dysurie", "die Hämaturie", "der Teerstuhl", "der Dekubitus", "das Hämatom", "das Exanthem",
                 "eitrig sezernierend", "die Zahnprothese", "die Ganzkörperwäsche", "die Intimpflege",
                 "das Steckbecken", "die Urinflasche", "der Toilettengang"],
        MOBIL: ["mobilisieren", "umlagern", "der Rollstuhl", "die Kontrakturenprophylaxe", "die Bettruhe",
                "die Physiotherapie", "die Pneumonieprophylaxe", "die Thromboseprophylaxe"],
        ESSEN: ["die Schluckstörung (Dysphagie)", "die Appetitlosigkeit", "die Exsikkose", "die Sondenkost",
                "die passierte Kost", "die Flüssigkeitsbilanz", "die Magensonde", "der Reflux",
                "der Diabetes mellitus"],
        MEDIK: ["die Diuretika", "das Antikoagulans", "das Hypnotikum", "das Analgetikum", "das Suppositorium",
                "die subkutane Injektion", "die Infusion", "das Sedativum", "das Laxans", "das Klysma",
                "die Überdosierung", "die mangelnde Compliance", "intravenös (i.v.)"],
        VISITE: ["die Beinödeme", "die Dyspnoe", "die Tachykardie", "die Herzrhythmusstörung", "die Hypertonie",
                 "subfebril", "das Sputum", "die Pneumonie", "der Harnwegsinfekt", "der Verdacht auf Thrombose",
                 "die Blutentnahme", "das EKG", "die Gastroskopie", "die Koloskopie", "die Sonografie", "die MRT",
                 "der Abstrich", "die Visite", "die Vitalzeichen kontrollieren", "die Nahtentfernung",
                 "der Blasenkatheter", "das Stoma", "die Allgemeinanästhesie"],
        AUFNAHME: ["die Anamnese", "nüchtern bleiben", "die Pflegefachkraft", "die Patientenrufanlage"],
        UEBERGABE: ["der reduzierte Allgemeinzustand", "somnolent", "verwirrt", "zeitlich desorientiert",
                    "die nächtliche Unruhe", "die depressive Verstimmung", "kaltschweißig", "die Zyanose",
                    "der Ikterus"],
        NOTFALL: ["die Atemnot", "die Synkope", "die Sepsis", "der Apoplex (Schlaganfall)", "der Myokardinfarkt",
                  "der Krampfanfall", "nicht ansprechbar", "reanimieren", "der Sturz", "die Sprachstörung",
                  "die Lähmung (Parese)", "die Hypoglykämie"],
        ANGEH: ["die Vorsorgevollmacht", "die gesetzliche Betreuung", "der Verzicht auf Reanimation", "versterben",
                "die Sterbephase", "die Rasselgeräusche"],
        ENTLASS: ["die Entlassung", "die Rehabilitation", "die stationäre Langzeitpflege", "der Pflegegrad"],
    }),
}
