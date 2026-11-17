# Relecture de l'espagnol (interface de l'allemand) : bilan du 15 nov. 2026

## Contrôles mécaniques (sur tout)

- `tests/relecture_langue.py --langue es --suspects` : **0 champ suspect** (aucun mot d'un caractère,
  aucune phrase trop courte, aucun champ perdu) sur les 8 106 cartes.
- `--collisions` : 88 groupes où deux mots allemands avaient la même réponse espagnole → **41 départagés**
  (49 corrections, `lots/collisions-corrections.json`), **47 acceptés** avec leur raison
  (`lots/collisions-acceptees.txt`, recopié dans `relecture_es/collisions-acceptees.txt`, que l'outil
  lit). Après la pose : **0 carte à regarder**.
- `tests/trous_francais.py --langues es` : 11 signalements, tous de l'espagnol pris pour du français
  (« de la »).
- Les contrôles de chaque pose (corpus, exercices, examen, textes) : 0 faute.

## Relecture croisée par un autre modèle (échantillon)

Traduction : Fable. Relecture : Sonnet, puis un lot ré-étalonné par Opus.

| Lot | Entrées | Bons | Fautes | Avis |
|---|---:|---:|---:|---:|
| 01 | 100 | 98 | 0 | 2 |
| 02 | 100 | 99 | 0 | 1 |
| 03 | 100 | 98 | 0 | 2 |
| 04 | 100 | 97 | 0 | 3 |
| 05 | 67 | 68 sur 69 entrées du lot | 0 | 1 |
| **Total** | **467** | **460** | **0** | **9** |
| 03, étalonnage Opus | 100 | 95 | 0 | 5 |

Échantillon : 12 cartes par fichier et par niveau (A1-C1, six fichiers), 2 exercices par jeu (48 jeux),
30 textes de fiches ; tirage fixe (`outils/echantillon.py`, graine 20261115).

**Ce que dit l'étalonnage** : aucune faute de fond (contresens, temps, forme d'Espagne) dans ce lot, ni pour
Sonnet ni pour Opus ; mais les avis ne se recoupent pas — Opus relève des calques et des usages régionaux que
le passage rapide de Sonnet (une demi-minute par lot) ne voit pas. Lecture honnête : **≈ 95 % sans réserve,
le reste en tournures à polir**, aucune faute grave trouvée. Pour comparer : polonais 94,6 %, russe 96,4 %.

**Appliqué** (faits seulement, 8) : *allmählich* rendu par un adjectif → « poco a poco, gradualmente » ;
*Leerstand* « la desocupación » (= le chômage en Amérique latine) → « la vacancia (de inmuebles) » ;
*Krankenkasse* « la caja de seguro médico » (calque) → « la aseguradora de salud » ; « pregunta privada » →
« personal » ; « ya era más que hora » → « ya era hora » ; un exercice *wenn* au mauvais temps ; deux fiches
(« el oral » d'Espagne → « la prueba oral » ; une tournure confuse).
**Non appliqué** (style, ou un seul pays) : « ejotes » (Mexique seul), mitfühlen, schleichend, deux tournures.

## Ce qui reste à une relecture humaine

- Un **locuteur natif** (mexicain ou colombien), comme pour le polonais et le russe : les choix régionaux
  listés dans chaque `lots/RAPPORT-*.md`, section « À trancher » (pastel / torta, alberca / piscina, renta /
  arriendo, ayuntamiento / alcaldía…).
- Un **soignant** hispanophone pour le vocabulaire de santé (cartes et scènes de soins signalées dans les
  rapports ; *Hospiz* rendu « hospicio », à revoir).
- Deux questions de fond, pour Jacques ou le chef : dans les séries *wann / wenn* et *aber / sondern*, la
  traduction espagnole (« cuándo / cuando », « pero / sino ») donne la réponse, alors que le français ne la
  donnait pas ; et le Perfekt rendu au *pretérito* (« Ayer comí ») ou au *pretérito perfecto* selon le sens.
- Neuf mots allemands présents dans deux thèmes ont deux réponses espagnoles différentes (Annonce, Impfpass,
  Leitung…) : souvent deux sens voulus, à vérifier.
