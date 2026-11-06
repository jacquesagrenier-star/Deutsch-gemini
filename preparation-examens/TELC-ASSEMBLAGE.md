# Le bloc telc A2·B1 : qui fait quoi, et comment les parties s'assemblent

6 nov. 2026. Jacques a lancé l'accélération du telc (décision `1c40ee6`). Quatre sessions font chacune leur partie ;
la session « examens DTZ / telc » garde le bloc et l'assemblage. **Branche de départ** :
`claude/examens-dtz-telc-774170` (elle contient la branche `claude/dtz-hoeren-lesen-965077`, donc
`visuel/prototype/dtz/commun.js` et `commun.css`).

À lire d'abord : `preparation-examens/FORMAT-TELC.md` (le format relevé dans l'Übungstest gratuit du telc :
parties, nombre de questions, points, seuils) et `preparation-examens/PLAN-DTZ-TELC.md`, section 3.

**Droits d'auteur** : le FORMAT du telc (durées, types de tâches, nombre de questions), jamais son contenu. Tout texte,
son ou image est écrit pour Wortando. Mark Garnier (Montréal, Gartenstraße 12 à Berlin), Anna (allemande), la
Hausverwaltung Kern (Frau Brandt) : `scenes/personnages.json`, `video/LIEUX.md`.

## Les fichiers, et à qui ils sont

Tout vit dans `visuel/prototype/telc/`.

| fichier | partie | session |
|---|---|---|
| `telc.html` | la page, le profil `PROFIL_EXAMEN`, les tuiles, les `<script>` de tous les modules (déjà en place) | assemblage — **ne pas toucher** |
| `telc-commun.js` | `textesTelc()`, `champTelc()`, `TELC.epreuve()`, `niveauTelc()`, les textes communs en anglais | assemblage — **ne pas toucher** |
| `sprachbausteine.js`, `donnees/sprachbausteine.json` | SB, le modèle à suivre | assemblage ; la **relecture** est à telc-lire, qui corrige directement `donnees/sprachbausteine.json` |
| `lesen.js`, `donnees/lesen.json` | L, Lesen Teile 1-4 (items 1-18) | **telc-lire** (`local_6ceacc3e…`) |
| `lesen-schreiben.js`, `donnees/lesen-schreiben.json` | LS, le courriel reçu (items 29-30) puis le courriel à écrire (31) | **telc-ecrire** (`local_836e50e6…`) |
| `schreiben.js`, `donnees/schreiben.json` | S, la réponse courte (57) et les critères II-IV de l'écrit | **telc-ecrire** |
| `hoeren.js`, `donnees/hoeren.json` | H, Hören Teile 1-4 (items 32-51) | **telc-ecouter** (`local_5c7a4eaa…`) |
| `hoeren-schreiben.js`, `donnees/hoeren-schreiben.json` | HS, les 5 messages de répondeur à noter (52-56) | **telc-ecouter** |
| `sprechen.js` + `oral.html` | Sp : `sprechen.js` s'inscrit comme partie et ouvre `oral.html` | **telc-parler-blanc** (`local_fe22d1c6…`) |
| `examen-blanc.js` | l'examen blanc, `DTZ.examen({…})` | **telc-parler-blanc** |
| `outils/relecture_<partie>.py` | la relecture germanophone de sa partie | chaque session (voir plus bas) |
| `tests/telc_<partie>.py` | le contrôle du format de sa partie | chaque session |

**On ne touche pas** :
- `index.html` : le panneau du bloc telc. L'assemblage y ajoutera une option par partie, `ouvrirTelc("L")` etc.
- `visuel/prototype/dtz/*` : `commun.js` et `commun.css`. Un changement s'y demande à la session
  « DTZ : écouter et lire » (`local_4a10c4f4…`), en correctif.
- `visuel/prototype/dtz-oral.html` : **on le copie**, on ne le modifie pas.
- `telc.html`, `telc-commun.js`, `sprachbausteine.js`, `tests/telc.py`, `outils/relecture.py`.
- `preparation-examens/*` et `retours/A-RELIRE-TELC.md`, qui est dérivé.

Pour un besoin dans un fichier qu'on ne touche pas, écrire à l'assemblage (`SendMessage`).

## Le modèle d'un module

Copier la forme de `sprachbausteine.js`.

1. **Les textes**, en français ET en anglais. On fait comme dans `sprachbausteine.js` : une table `X_EN`, puis
   `textesTelc({ en: X_EN, fr: {…} })`. Le français vient en dernier dans l'appel, mais la fonction verse le
   français d'abord, puis la langue d'interface par-dessus. Ensuite `T("cle")` partout. Aucune chaîne en dur dans le
   HTML produit.
2. **Les données** : `donnees/<module>.json`, `{ "_note": "…", "series": [ {"id": 1, …}, … ] }`.
   - Les champs pour l'élève se suffixent `_fr`, `_en` (`erkl_fr`, `erkl_en`, `situation_fr`…), lus par
     `champTelc(o, "erkl")`.
   - L'allemand de l'examen n'a pas de suffixe.
   - Une bonne réponse s'écrit par son indice (`bon`), et aucune lettre ne doit porter plus de la moitié des bonnes
     réponses d'une série.
   - Les nombres s'écrivent en chiffres dans le texte ; si la voix doit les dire, leur lecture va dans
     `audio/lectures/de.json`.
3. **Le chargement et l'inscription** :
   ```js
   DTZ.charger(fetch("donnees/lesen.json", {cache: "no-cache"}).then(r => r.json()).then(d => { … }));
   DTZ.partie({ id: "L", ordre: 10, titre: T("…"), sous: T("…"), ouvrir: () => … });
   ```
   Les `ordre` sont : L 10, SB 20, LS 30, H 40, HS 50, S 60, Sp 70. La série du jour vient de
   `await choisirSerie(series, motsDe, "L")`. Le profil garde 0 série pour l'examen blanc (`seriesExamen: 0`) : on
   pourra en réserver plus tard.
4. **L'organisation**, décidée par Jacques le 4 nov. :
   - une page par exercice, avec en tête « Section · … » ;
   - des points de progression qu'on peut toucher ;
   - « Continuer » en bas (le bouton `#suite`) ;
   - un récapitulatif avec Refaire la section / Section suivante / Toutes les sections.
   C'est exactement ce que fait `sprachbausteine.js` (`points()`, `recap()`, `toutesLesSections()` avec
   `TELC.direct`), et `dtz-oral.html` pour l'oral.
5. **Le retour ‹** : `DTZ.surRetour(fn)`. Si la page a été ouverte directement sur la partie (`TELC.direct`), « Toutes
   les sections » ferme le cadre (`parler("fermer")`) et ramène au panneau du bloc telc de l'app.
6. **Parler à l'app** :
   - `parler("exercice", {juste})` après chaque réponse : cela compte pour l'objectif du jour ;
   - `resultat("<id>", {…})` à la fin, pour garder le dernier résultat ;
   - le micro : `parler("micro", …)` (voir `dtz-oral.html`).
7. **L'examen blanc** : `TELC.epreuve({id, ordre, minutes, sur: {Lesen: …}, lancer: fini => …})`, avec les points
   **par compétence** (le détail est en tête de `telc-commun.js`). `examen-blanc.js` enchaîne les épreuves inscrites
   et calcule le niveau avec `niveauTelc()`.
8. **La voix** : `dire(texte, wer)` de `commun.js` (la voix du téléphone, avec une hauteur par personne). La session
   « DTZ : écouter et lire » a un outil de voix enregistrées (ElevenLabs v2) : le lui demander. **Aucune dépense sans
   l'accord de Jacques, écrit dans sa session, avec le coût annoncé.**

## Tester

- La page se sert par HTTP : `python -m http.server <port> --directory <dépôt>`, puis
  `/visuel/prototype/telc/telc.html?partie=L&lang=en`. Le paramètre `nuit=1` donne le mode nuit.
- Un navigateur piloté par script (Playwright) passe sous le verrou `~/.wortando/verrou-parcours`. Le panneau du
  navigateur de l'app, lui, n'est pas concerné.
- `node tests/syntaxe.js` et `python tests/verifier.py` ne lisent pas ces pages : chaque session fait son
  `tests/telc_<partie>.py`.

## La relecture germanophone

Chaque session écrit `outils/relecture_<partie>.py` avec une fonction `section(lignes)` qui ajoute ses textes au
format de `retours/A-RELIRE-TELC.md` : le texte allemand, puis une ligne « → ». Ensuite on relance
`python visuel/prototype/telc/outils/relecture.py`, qui les ramasse tous.

## L'assemblage

- Chaque session pousse sa branche et prévient l'assemblage (`SendMessage`).
- L'assemblage fusionne les branches dans `claude/examens-dtz-telc-774170` et ajoute les options du panneau.
- Il lance les contrôles et les parcours de et es sous le verrou.
- La publication se fait en **une seule version**, sous la file, au signal du chef.
