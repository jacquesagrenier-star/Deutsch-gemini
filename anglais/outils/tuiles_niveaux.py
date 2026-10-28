# -*- coding: utf-8 -*-
"""Les tuiles de grammaire de l'anglais (28 oct. 2026) : ce que chaque panneau
propose, comme les tuiles allemandes. Lu par niveaux.tuiles().

Une option est l'une de trois choses :
  {"fiche": id}        ouvre une fiche de grammaire anglaise
  {"vocab": fonction}  lance un vocabulaire de mots-outils deja dans l'app
  {"serie": nom, ...}  une serie dediee, dont les questions sont dans tuiles_series_*.py

SOURCE : on corrige ici, puis python anglais/outils/construire.py.
"""
import tuiles_series_a as A
import tuiles_series_b as B
import tuiles_series_c as C

FICHES = C.FICHES
Q = dict(A.Q, **B.Q, **C.Q)


def serie(nom, id, titre, desc, niveau, kicker):
    return {"serie": nom, "id": id, "titre": titre, "desc": desc, "niveau": niveau,
            "kicker": kicker, "questions": Q[nom]}


TUILES = {
"pronomen": {"sous_titre": "I, me, my, mine, myself", "options": [
    {"fiche": "pronoms", "titre": "Comprendre les pronoms", "desc": "I, me, my, mine — la fiche"},
    {"fiche": "relatives", "titre": "Les relatifs", "desc": "who, which, that, whose — la fiche B1"},
    serie("pronomsSujetObjetEnExercises", "pronoms-sujet-objet", "Sujet ou complément ?", "I ou me, she ou her · A1", "A1", "Sujet ou complément"),
    serie("possessifsEnExercises", "possessifs", "Les possessifs", "my ou mine, its ou it's · A1", "A1", "Les possessifs"),
    serie("reflechisEnExercises", "reflechis", "Réfléchis et réciproques", "myself, each other · A2", "A2", "Réfléchis et réciproques"),
    {"vocab": "startPronomenVokabular", "titre": "Vocabulaire · pronoms", "desc": "Les cartes des pronoms"},
    {"vocab": "startArtikelwoerterVokabular", "titre": "Vocabulaire · déterminants", "desc": "a, the, some, every, each…"},
]},
"zahlen": {"sous_titre": "one, first, a quarter past", "options": [
    {"fiche": "nombres", "titre": "Comprendre les nombres", "desc": "L'âge, l'heure, les prix — la fiche"},
    serie("heureDatesEnExercises", "heure-dates", "L'heure et les dates", "a quarter past, on May 12th · A1", "A1", "L'heure et les dates"),
    serie("prixQuantitesEnExercises", "prix-quantites", "Prix, quantités, grands nombres", "four fifty, a dozen, a billion · A2", "A2", "Prix et quantités"),
    {"vocab": "startZahlenVokabular", "titre": "Vocabulaire · nombres", "desc": "Les grands nombres et les ordinaux"},
]},
"praep": {"sous_titre": "in, on, at, to, for", "options": [
    {"fiche": "prepositions", "titre": "Comprendre les prépositions", "desc": "in, on, at — la fiche"},
    serie("prepTempsEnExercises", "prep-temps", "Le temps : in, on, at, for, since", "at eight, on Monday, in May · A1", "A1", "Prépositions de temps"),
    serie("prepLieuEnExercises", "prep-lieu", "Le lieu : in, on, at, into", "in the kitchen, at the station · A1", "A1", "Prépositions de lieu"),
    serie("prepLaquelleEnExercises", "prep-laquelle", "Laquelle ? by, with, from, of", "by car, made of wood · A2", "A2", "Quelle préposition ?"),
    serie("prepVerbesEnExercises", "prep-verbes", "Verbes et adjectifs à préposition", "depend on, good at, afraid of · B1", "B1", "Verbes à préposition"),
    {"vocab": "startPraepVokabular", "titre": "Vocabulaire · prépositions", "desc": "Les cartes des prépositions"},
]},
"konjunktionen": {"sous_titre": "because, although, so, unless", "options": [
    {"fiche": "connecteurs", "titre": "Comprendre les connecteurs", "desc": "although, despite, unless — la fiche B2"},
    serie("becauseAlthoughEnExercises", "because-although", "because ou although ?", "et because of, despite · A2", "A2", "because ou although"),
    serie("soButEnExercises", "so-but", "so, but, however, therefore", "conséquence ou contraste · A2", "A2", "so, but, however"),
    serie("whenWhileEnExercises", "when-while", "when, while, until, as soon as", "les liens du temps · B1", "B1", "when, while, until"),
    serie("ifWhetherEnExercises", "if-whether", "if, whether, unless, in case", "la condition · B1", "B1", "if, whether, unless"),
    {"vocab": "startKonjunktionenVokabular", "titre": "Vocabulaire · connecteurs", "desc": "Les cartes des conjonctions"},
    {"vocab": "startPartikelnVokabular", "titre": "Vocabulaire · mots de l'oral", "desc": "you know, I mean, kind of, though"},
]},
"wortstellung": {"sous_titre": "sujet, verbe, complément", "options": [
    {"fiche": "ordre-des-mots", "titre": "Comprendre l'ordre des mots", "desc": "La fiche A2"},
    serie("placeAdverbesEnExercises", "place-adverbes", "La place de always, never, already", "avant le verbe, après be · A2", "A2", "La place des adverbes"),
    serie("questionsIndirectesEnExercises", "questions-indirectes", "Questions directes et indirectes", "Where is it? — Do you know where it is? · B1", "B1", "Les questions indirectes"),
    {"fiche": "questions", "titre": "Poser une question", "desc": "do, does, did — la fiche A1"},
]},
"adverbien": {"sous_titre": "always, often, never", "options": [
    {"fiche": "adverbes", "titre": "Comprendre les adverbes", "desc": "quickly, well, always — la fiche A2"},
    serie("adverbesFamilleEnExercises", "adverbes-famille", "Identifier la famille", "manière, temps, lieu, fréquence, degré", "A2", "La famille des adverbes"),
    {"vocab": "openAdverbienVokabular", "titre": "Vocabulaire", "desc": "Les adverbes par niveau"},
    {"vocab": "startDicteeAdverbes", "titre": "Dictée", "desc": "Écouter et écrire"},
]},
}
