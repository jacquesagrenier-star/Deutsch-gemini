# À relire : l'espagnol en interface allemande (1er nov. 2026)

Pour un relecteur ou une relectrice **germanophone**. Tout a été traduit par Claude (modèle
Fable, sous contrôle de Claude Opus) à partir du français et de l'anglais, puis contrôlé
mécaniquement : aucun texte recopié du français, balises et {marques} conservées, aucune
collision (deux mots espagnols d'une même catégorie avec la même réponse allemande). **Aucun
germanophone ne l'a encore lu.**

## Comment l'ouvrir

`https://wortando.com/?apprendre=es` (ou la prévisualisation de la branche), puis
Einstellungen → Sprache → **Deutsch**. Un téléphone réglé en allemand l'ouvre directement en
allemand. L'allemand n'est proposé que pour apprendre l'espagnol.

## À relire en priorité (dans cet ordre)

1. **L'interface** — 1 607 textes + 142 propres à l'espagnol. Le vocabulaire retenu est à
   valider d'abord, il revient partout :

   | français | allemand choisi |
   |---|---|
   | la séance du jour | „Meine Lerneinheit heute“, „Lerneinheit starten“ |
   | Mettre de côté / Mis de côté / le coffre | „Zurücklegen“ / „Zurückgelegt“ / „die Ablage“ |
   | Encore / Continuer / Je savais | „Nochmal“ / „Weiter“ / „Gewusst“ |
   | Premiers pas / escale / étape | „Erste Schritte“ / „Etappe“ / „Schritt“ |
   | Explorer les scènes / Écouter, répéter | „Szenen entdecken“ / „Hören, nachsprechen“ |
   | le tableau, la galerie, la mosaïque, un carreau | Gemälde, Galerie, Mosaik, Kachel |
   | maîtrisé / en cours / à rencontrer | „sicher“ / „im Lernen“ / „noch neu“ |
   | Débutant (niveau) / Repères | „Einstieg“ / „Orientierung“ |
   | Tout le contenu / Mes épisodes | „Alle Inhalte“ / „Meine Folgen“ |
   | gel de série | „Serien-Schutz“ |
   | une fiche de grammaire / l'accord | „Übersicht“ / „die Angleichung“ |

   Tutoiement partout ; noms des temps espagnols gardés en espagnol (presente, pretérito,
   imperfecto, subjuntivo…), comme les manuels allemands. Questions ouvertes :
   « Das Presente » ou « Das Präsens » en titre de fiche ? « Angleichung » ou « Kongruenz » ?

2. **Les 17 fiches de grammaire** (`espanol/datos/grammaire.json`, clé `de`) — elles ne sont pas
   traduites mais **réécrites contre l'allemand**. Vérifier que chaque comparaison est juste :
   ser/estar (« Das Deutsche hat nur „sein“ »), genre (deux genres, pas de neutre, articles jamais
   déclinés, el sol / die Sonne), accord de l'adjectif même en attribut, pretérito/imperfecto
   (« „Ich aß“ kann beides sein »), pretérito perfecto toujours avec haber (he ido = ich bin
   gegangen), subjonctif là où l'allemand garde l'indicatif, place du pronom (lo veo), usted à la
   3e personne du singulier, « las tres y media = halb vier ». Liste complète par identifiant :
   `espanol/de/lots/RAPPORT-grammaire-exercices.md`, section « Comparaisons ».

3. **La prononciation** (20 règles, écran 🔊) — écrite pour une oreille allemande : j = ach-Laut,
   z/c jamais « ts », s toujours sourd (jamais celui de „Rose“), v = b, qu jamais « kw »,
   sp/st sans « schp/scht », ei = e-i, ie = i-e. Et les **transcriptions des nombres** (Repères),
   écrites pour un lecteur allemand : « ßE-is », « ßJE-te », « o-TSCHEN-ta », θ gardé pour le
   « th » d'Espagne. Le « ß » en tête de syllabe pour le s sourd est un choix à valider.

4. **Les faux amis** (`falsosAmigosExercises`) — réorientés : pièges propres aux germanophones
   (firma ≠ Firma, mantel ≠ Mantel, ropa ≠ Robe, bizarro ≠ bizarr, rubio ≠ rubinrot) ou
   présentés comme pièges venus de l'anglais (embarrassed, exit, carpet, actual…).

5. **gustar** — expliqué par „gefallen“ / „schmecken“ (« Wörtlich: die Schokolade gefällt mir »).

6. **Un échantillon du corpus** (3 898 mots et phrases) et des **notes des scènes** (2 430 textes) :
   naturel des phrases, articles des noms, registre.

## Doutes précis laissés par les traducteurs

Rassemblés avec leurs identifiants dans `espanol/de/lots/RAPPORT-interface.md`,
`RAPPORT-grammaire-exercices.md`, `RAPPORT-scenes-parcours.md` et `RAPPORT-tiempos.md`. Les
principaux :

- « enchanté · enchantée » → „freut mich (sagt ein Mann · sagt eine Frau)“ ;
- « Tengo mucha … » → „Ich habe großen · große …“ (prisa → „Ich habe es sehr eilig“) ;
- l'empadronamiento → „Wohnsitzanmeldung“ ;
- « Anna a froid » → „Anna friert.“ (corrigé à la relecture : la traduction disait „Anna ist kalt“) ;
- deux défauts de la **source** (pas de l'allemand) : des phrases au présent traduites au passé
  composé en français (`exercises` 9, 30, 41 ; `infinitivExercises` 35, 53) et des impératifs
  étiquetés « il/elle » (`exercises` 27, 28, 45-48, 51, 59).

## Ce qui reste en anglais pour un germanophone (pas encore traduit)

- le **dictionnaire** intégré (WikDict n'est câblé qu'en espagnol-français et espagnol-anglais) ;
- les **épisodes** vidéo (français et anglais seulement) ;
- la **visite guidée** : affichée en allemand, mais sans voix (comme en portugais et en arabe).

## Ajouté le 6 nov. 2026 (v1120)

Les textes du lot de l'évaluation (fin de séance, écran court, bandeau, bulle du micro, attente après la connexion) : voir `A-RELIRE-INTERFACE-LOT-EVALUATION.md` (leurs textes allemands sont dans le bloc `de` d'`I18N`).
