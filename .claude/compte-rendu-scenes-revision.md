# Compte rendu — branche `scenes-revision` (session cloud, 10 oct. 2026)

Une réponse dans la scène compte désormais comme une révision du mot, pour la
répétition espacée — seulement quand la scène est ouverte depuis la séance.

## Ce qui a changé

**Le prototype** (`visuel/prototype/index.html`) envoie un nouveau message
`{source: "wortando-scene", type: "reponse", mot, genre, theme, cat, juste}`,
seulement avec `?seance=1` :

- « Trouve ! » (A1, et l'étape A1 glissée dans une séance A2) : la cible.
- Question A2-C1 : seulement si elle porte la clé **`revise`** dans son
  `.points.json`. Hors de ces cas, rien n'est envoyé. Le bloc `TEXTES` et
  `ouvrirSceneSeance()` n'ont pas été touchés (branche `scenes-traduction`
  en parallèle).

**`revise`, posé à la main sur 35 questions** (`construire.py` le résout dans
le corpus et s'arrête si le mot n'y est pas) :

- B1 stehen/stellen, liegen/legen, sitzen, hängen : le verbe de la bonne réponse.
- « Was nimmt Anna? » (choix entre trois fruits ou légumes) : le nom (Tomate, Apfel, Banane, Radieschen).
- « Zwei Kilo ___ » / « Ein Kilo ___ » / « drei ___ » : Kartoffel, Apfel, Zitrone.
- Comparatifs (größer, länger) : groß, lang. « schon ___? reif » : reif. « Was ___ die Himbeeren? » : kosten.
- Examen : ausziehen, stellen, stehen, untersuchen, umdrehen, lassen, sehen.
- **Pas de `revise`** : les « Wo…? » A2 (on y travaille la préposition et le
  datif, pas un mot), les articles, pronoms relatifs, particules séparables
  (um, ab, aus), auxiliaires, passifs, modaux et Konjunktiv II du C1, les
  déclinaisons d'adjectifs (frische, aufgeschnittene). Mieux vaut ne pas noter
  qu'enregistrer une révision fausse. À revoir par Jacques : la liste est
  dans `git diff main -- visuel/prototype/*.points.json`.

**`construire.py`** : résout `revise` (nom → thème, verbe, adjectif) et ajoute
le thème aux formes `aussi`, pour que l'app retrouve la bonne entrée. Les huit
`scene-*.js` ont été refaits (aucun autre changement : la génération sur `main`
était à jour).

**L'app** (`index.html`) :

- `programmerEcheance()` et `programmerMaitrise()` : ce que `scheduleReview()`
  et `markMastered()` faisaient à l'état du mot, sorti **tel quel** (pur
  déplacement, vérifiable dans le diff). Les cartes et la scène passent par le
  même calcul.
- `carteDeScene()` retrouve le mot : nom nu dans `themes` (le thème que la
  scène nomme d'abord, sinon le premier ; le genre départage les homographes),
  verbe par infinitif (clé stable `verben#stehen`), adjectif par mot. Les
  formes `aussi` et les synonymes régionaux sont des entrées à part du corpus :
  c'est le mot demandé qui est révisé. Trois parcours du corpus par scène,
  aucune boucle sur la progression (piège v100).
- `revisionDeScene()`, appelée par le gestionnaire de messages (contrôle
  d'origine conservé) **seulement si `sceneOuverteDepuis === "seance"`**.
  Rien depuis le tableau admin, rien en Découvrir (la scène n'y juge rien),
  rien en direction anglaise, rien en version gratuite pour un mot neuf hors
  échantillon.

## Ce que vaut une réponse — et pourquoi

Aligné sur la carte :

| Dans la scène | Équivaut à | Effet |
|---|---|---|
| Juste | « Je savais » | +1 pastille ; 1re réussite → 10 min, puis 1 j, 3 j…, 4e → maîtrisé (entretien 16 j, 35 j…) |
| Faux | « Encore » | pastilles à zéro, retour dans 2 min, échelle des jours à zéro |

- **« Juste après une erreur » n'existe pas** dans la scène, comme sur une
  carte : le premier geste juge et verrouille la question. Seule exception
  déjà existante : le bon mot touché sur la mauvaise personne (l'oreille de la
  médecin) n'est pas compté ; la réponse suivante l'est.
- **Une différence voulue** : un mot juste qui n'est **pas encore échu** ne
  bouge pas. La séance ne sert une carte que neuve ou échue ; la scène, elle,
  demande ce que l'image montre. Faire monter un mot prévu dans trois jours
  comprimerait l'espacement (deux réussites dans la même heure ne valent pas
  une réussite à trois jours). Une erreur, elle, compte toujours.
- Un mot neuf compte dans la dose du jour (`noterMotNeuf`), comme une carte.
- L'objectif du jour et la série avancent (`recordDailyActivity`), mais **sans
  la fête du palier par-dessus la scène** (elle couvrirait l'image au milieu
  d'une question).

## Limites à connaître

- Un mot raté revient « dans 2 min ». Si l'élève passe aux cartes moins de
  deux minutes après, il n'est pas encore échu et n'entre pas dans le paquet
  de ce jour-là ; il reviendra à la séance suivante.
- La synchronisation Firestore passe par `setWordState()` → `saveProgress()`
  → `scheduleCloudSync()`, comme pour une carte : rien de neuf de ce côté.

## Vérifié

- `python tests/verifier.py` : 27 639 contrôles, aucun problème (seul
  avertissement : les CSV d'`export/`, absents du cloud).
- `node tests/syntaxe.js` : les 5 blocs s'analysent.
- **`node tests/scene_revision.js`** (nouveau) : page headless, vraie scène
  en séance, trois réponses (juste, faux, juste) → exactement ces trois mots
  ont changé, comme après une carte, et aucun autre ; mot non échu intact ;
  4e réussite → maîtrise ; questions B1 sans `revise` → rien ; admin → rien ;
  hors séance → aucun message ; les 451 mots qu'une scène peut envoyer se
  retrouvent tous dans le corpus.

## Pour Jacques

- Essayer depuis la séance (essai `scenes`) sur `essai` : les mots de la
  scène doivent ensuite apparaître comme vus (pastille) dans les cartes.
- Relire la liste des questions qui portent un mot (ci-dessus).
