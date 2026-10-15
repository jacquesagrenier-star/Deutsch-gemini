# L'espagnol en arabe : avancement

**15 oct. 2026 : FAIT et proposé dans l'app (v808).** `LANGUES_UI_AVEC_ESPAGNOL` et
`UI_LANGS` (branche espagnole) valent `["fr", "en", "pt", "ar"]` : un usager en arabe voit
la porte de l'espagnol, et l'espagnol s'ouvre en arabe, de droite à gauche.

Historique : chantier commencé le 13 oct. au soir (corpus, verbes, 150 exercices), arrêté
quand le crédit de Fable s'est épuisé ; ces champs ont été publiés inertes le 15 oct. (commit
0394d27) ; le reste a été fait le même jour, traduit par Fable en trois lots parallèles,
relu et posé par Claude. Le modèle était le chantier portugais (`AVANCEMENT-PT.md`, v784).

## Fait

| Où | Quoi | Compte |
|---|---|---|
| `espanol/datos/temas.json` | `traduction_ar` + `exemple_ar` | 1 777 / 1 777 (dont les 18 mots des scènes du 14-15 oct.) |
| `verbos`, `adjetivos`, `adverbios`, `expresiones`, `funcionales` | idem, plus `exemple_<temps>_ar` pour les verbes | 873, 597, 228, 245, 152 |
| `espanol/datos/ejercicios.json` | `translation_ar`, `hint_ar`, `explanation_ar` ; `question_ar` sur les 126 questions formulées ; `optionsAr` / `correctAr` recopiés | 1 041 / 1 041 |
| `espanol/datos/grammaire.json` | `textes.ar` (43) + clé `ar` après chaque `pt` des 17 fiches, **réécrites pour un arabophone** | 43 + 259 |
| `espanol/datos/prononciation.json` | dérivé : dictionnaire `AR` de `tests/prononciation_es.py`, écrit contre l'arabe (3 voyelles : e/i, o/u ; ni p ni v ; j ≈ خ ; h ≠ ه) | 18 règles + 2 variantes |
| `espanol/datos/variantes.json` | `verbes.coger.remarque.ar` | 1 |
| `index.html` | bloc `I18N_ESPAGNOL.ar` (toutes les clés du bloc `fr`) ; `ar:` sur les 25 libellés de catégories (branches es) ; `MOTS_OUTILS_ES_AR` (rangs 23-25) ; `UI_LANGS` et `LANGUES_UI_AVEC_ESPAGNOL` += `"ar"` | 131 clés, 25 libellés, 74 mots-outils |
| `index.html`, `abrirGramatica` | `dir="auto"` sur la 1re colonne du tableau, sa ligne d'exemple et la phrase espagnole : sans lui, en arabe, « ¿El libro? Lo tengo yo. » perdait son point à gauche. Sans effet en fr/en/pt. | |
| `visuel/prototype/espanol/*.json` | `titre_ar` (après `titre_pt`) et `n_ar` (après `n_pt`, latam compris) | 35 scènes, 1 031 textes |
| `visuel/prototype/construire.py` | porte `ar` dans `scene-<scène>.es.js` : sens des mots (du corpus espagnol, et non plus du mot allemand), titres, notes | 35 `.es.js` refaits, aucun `.js` allemand touché |
| `tests/verifier.py` | exige `ar` comme `pt` : clés de `I18N_ESPAGNOL`, prononciation, et `verifier_arabe_espagnol` (un champ `_pt` sans son `_ar` dans `espanol/datos`, une scène `n_pt` sans `n_ar`) | |

Relecture (15 oct.) : 60 entrées du corpus, ~105 exercices des quatre lots, les 131 textes
d'interface, **les 302 textes des fiches**, les 20 règles de prononciation, ~45 notes de scènes,
15 mots-outils, les 25 catégories. Corrigés : une coquille, une erreur de fond (la fiche des
pronoms opposait « se lo doy » à « أعطيه إياه », alors que l'arabe suit le même ordre),
« الديكور » → « الخلفية » (8 explications), un bouton « تمارين PRESENTE ».

Vérifié à l'écran (mobile, de droite à gauche) : accueil, fiche des pronoms, exercice gustar
(et son explication), scène de la cuisine en A2, prononciation, carte de nom.

## Les flèches (à retenir)

Le français écrit « A → B » ; en arabe on écrit « A ← B ». MAIS entre deux mots latins, le
navigateur range la flèche dans le segment latin, qui s'affiche de gauche à droite : « la
pelota ← la » se lit alors à l'envers. `python espanol/ar/fleches.py` applique la règle
(voisins forts tous deux latins → « → », sinon « ← ») ; 175 textes corrigés le 15 oct.
À relancer après tout nouveau lot.

## Reste

- **Relecture par un natif arabophone** (comme pour le polonais et le russe). Doutes de Fable
  listés avec leurs id dans `espanol/ar/lots/RAPPORT-*.md`.
- **La voix de la visite guidée** pour l'espagnol en arabe : `VOIX_VISITE.languesEs` ne connaît
  que fr et en (comme pour le portugais). La visite se lit sans narration.
- Le dictionnaire (WikDict) n'a pas de paire espagnol-arabe : la recherche trouve les cartes en
  arabe, puis retombe sur le dictionnaire anglais (comme le portugais).
- Défauts **préexistants**, vus en passant, pour toutes les langues :
  - dans la cuisine, le couvercle (« Deckel ») devient « la tapa » = les tapas (corpus
    `el_restaurante`) : fr « la tapa », en « the tapa », ar « تاباس » ;
  - la 1re colonne de plusieurs tableaux de `grammaire.json` est une chaîne française
    (« vosotros (Espagne) », « tú (négatif) », « l'heure »…) affichée telle quelle partout ;
  - `espanol/datos/synonymes.json` absent (404 relevé par le parcours, déjà dans la référence).

## Reprendre

- `python espanol/ar/poser.py etat | reste | pose [--essai] | controle` : corpus et exercices.
- `python espanol/ar/extraire.py` refait `espanol/ar/sources/` (textes hors corpus) ;
  `python espanol/ar/poser_autres.py controle | pose` pose `lots/<nom>.ar.json`.
- Consignes données à Fable : `espanol/ar/CONSIGNES-FABLE.md`.
