# L'anglais A2 à C1 : le plan

## 28 oct. 2026 : « tous les mots » — la couverture face à l'allemand

Consigne de Jacques (27 oct.) : « Et tous les mots. Le compléter et de faire entièrement. »
Chaque mot allemand A2-C1 a été cherché en anglais (`python anglais/outils/manques_allemand.py`,
en cumulé : un mot allemand B1 est couvert s'il est en anglais au B1 ou plus bas). Les
absents ont été versés dans les listes (`ajouter_manques.py`), sauf ceux qui ne passent pas
en anglais, écartés **mot par mot avec leur raison** dans `anglais/outils/ecartes/<niveau>.txt`.

| Noms allemands couverts | A2 | B1 | B2 | C1 |
|---|---|---|---|---|
| Avant (v987) | 91 % | 88 % | 80 % | 64 % |
| Maintenant | 97 % | 92 % | 88 % | 69 % |

| Écartés, par raison | A2 | B1 | B2 | C1 |
|---|---|---|---|---|
| Déjà là sous une autre forme (« vegetables » → vegetable, « crime story » → crime novel) | 15 | 56 | 18 | 14 |
| Propre à l'Allemagne ou à l'Europe (Brezel, Bürgeramt, Gymnasium, Kripo, Wohngeld, TVA, IBAN) | 3 | 32 | 12 | — |
| Tournure ou composé sans équivalent anglais d'un mot (Zielvereinbarung, Betreuungsschlüssel…) | 6 | 62 | 46 | 367 |
| Britannique (l'anglais de base est américain : fetch, revision, overtake…) | 3 | 4 | 6 | — |
| Autre classe ou autre place (jours et nombres dans les repères, « be + adjectif », prépositions) | 25 | 43 | 21 | — |

Les verbes, adjectifs, adverbes et expressions suivent la même règle (ils sont dans les mêmes
fichiers). Au C1, presque tout l'écart restant vient des composés administratifs allemands
(Kommissionierung, Notendurchschnitt, Vorsorgeuntersuchung…) : un mot anglais n'existe pas,
seulement une glose. Ce sont ces listes, à montrer à Jacques, qui décident s'il faut en
reprendre certains malgré tout.

## État au 27 oct. 2026, au soir : les quatre niveaux sont construits (essai admin)

Mesuré par `python anglais/outils/couverture_comptes.py` (référence : l'espagnol, sur les 37
scènes gardées ; l'allemand pour le C1, que l'espagnol n'a pas) :

| | A2 | B1 | B2 | C1 |
|---|---|---|---|---|
| Noms | 657 (es 539) | 974 (515) | 374 (236) | 489 (de 948) |
| Verbes | 298 (274) | 354 (314) | 178 (162) | 166 (de 272) |
| Adjectifs | 189 (154) | 386 (261) | 122 (101) | 202 (de 291) |
| Adverbes | 78 (51) | 123 (119) | 53 (30) | 36 (de 52) |
| Expressions | 118 (82) | 116 (55) | 133 (69) | 102 (de 100) |
| Mots-outils | 46 (27) | 28 (20) | 18 (16) | 14 (de 0) |
| Fiches de grammaire | 9 | 10 | 10 | 9 |
| Questions de grammaire | 108 | 120 | 120 | 108 |
| Feuilles de conjugaison | 10 (10) | 10 (10) | 8 (8) | 8 (de 8) |
| Questions de scènes | 282 (282) | 281 (267) | 218 (218) | 156 (de 156) |

- A2, B1, B2 : chaque ligne atteint ou dépasse l'espagnol.
- **C1 : l'écart de vocabulaire avec l'allemand est voulu.** Le C1 allemand compte
  ~330 noms composés administratifs (« Betreuungsschlüssel », « Kommissionierung »…)
  sans équivalent anglais d'un mot : ils ont été écartés, et remplacés en partie par
  ~250 mots savants anglais écrits à la main (verbes, adjectifs, adverbes, idiomes, thème
  « Academic English »).
- Grammaire : 51 fiches en tout (A1-C1), 582 questions ; l'espagnol a 17 fiches et 1 343
  questions, mais sans niveau (24 séries d'environ 55 questions). Allonger les séries
  anglaises est la suite naturelle.
- Chaque mot a sa phrase d'exemple anglaise et sa traduction française ; 164 phrases sur
  ~4 000 viennent d'un autre mot que celui de la carte (liste dans `rapport.txt`).
- L'A1 n'a pas bougé (vérifié à l'octet près à chaque construction).

**Attend Jacques** : une relecture par un anglophone (tout est « brouillon ») ; la voix
(ElevenLabs, sur son accord ; la voix du téléphone en attendant).

## Le plan d'origine (27 oct. 2026, au matin)

27 octobre 2026. Mandat de Jacques, transmis par le chef d'orchestre : développer les
niveaux A2, B1, B2 et C1 de l'anglais (essai admin, même moteur). Session « anglais
A2-C1 », branche `claude/anglais-a2-c1-d6b41b`. Rien n'est payé : ni voix, ni génération,
ni rafale d'agents.

## Le principe : un fichier source par niveau, l'A1 n'est pas touché

La session « anglais » finit l'A1 et fait la mosaïque dans les mêmes dossiers. Pour ne
pas se marcher dessus, tout l'A2-C1 vit dans des fichiers à part :

| Fichier source (`anglais/outils/`) | Contenu |
|---|---|
| `noms_a2.py`, `noms_b1.py`, `noms_b2.py`, `noms_c1.py` | les noms par thème, même format que `noms_a1.py` |
| `mots_a2.py` … `mots_c1.py` | verbes, adjectifs, adverbes, expressions, même format que `mots_a1.py` |
| `irreguliers.py` | les verbes irréguliers au-delà de l'A1 (≈ 130), avec la forme britannique |
| `fonctionnels_a2c1.py` | les mots-outils de niveau (connecteurs, quantifieurs, relatifs…) |
| `grammaire_a2.py` … `grammaire_c1.py` | les fiches de grammaire en français et leurs séries |
| `conjugaison_a2c1.py` | les feuilles de conjugaison A2-C1 |
| `niveaux.py` | le constructeur des niveaux, appelé par `construire.py` |
| `extraire_niveaux.py` | l'outil (à usage unique, documenté) qui a tiré les listes de nos corpus |
| `couverture_comptes.py` | la mesure de chaque niveau contre l'espagnol et l'allemand |
| `anglais/scenes/<scène>.json` | les couches A2-C1 de chaque scène, **écrites pour l'anglais** |

Trois fichiers communs sont touchés, chacun d'une ligne ou d'un bloc court, annoncés au
chef avant : `construire.py` (un appel à `niveaux.construire`), `scenes.py` (fusionner
les couches de `anglais/scenes/`), et peut-être `index.html` (des intertitres A1, A2…
dans la liste des fiches de grammaire, seulement si une fiche porte un niveau : rien ne
change pour l'allemand et l'espagnol).

## 1. Le vocabulaire (américain, et britannique par `construire.py`)

D'où il vient : comme l'A1, de nos corpus. Chaque mot allemand (A1-C1) et espagnol
(A1-B2) porte sa traduction anglaise et une phrase **traduite en anglais et en français**.
Union mesurée des têtes anglaises, sans celles déjà en A1, au plus bas niveau où elles
paraissent :

| | A2 | B1 | B2 | C1 |
|---|---|---|---|---|
| Noms | 690 | 1 141 | 483 | 771 |
| Verbes | 294 | 457 | 222 | 177 |
| Adjectifs | 202 | 413 | 134 | 215 |
| Adverbes | 113 | 186 | 106 | 30 |
| Expressions | 159 | 196 | 202 | 90 |

On trie : une glose qui n'est pas un mot anglais courant (« to accept something as a
price »), un mot trop lié à l'Allemagne ou à l'Espagne (Pfand, tapas, Bürgeramt), un
doublon de sens, sortent. La phrase d'exemple est celle écrite **pour ce mot**, sinon
la banque de 11 500 phrases de l'A1 ; Berlin, Madrid et les euros en dernier recours.
Les noms sont regroupés en thèmes anglais (≈ 20 à 30 par niveau), pas en reprenant les
150 thèmes sources. Le britannique suit par la table de `variante.py`, enrichie des
paires A2-B1 de l'ancien `english_britam.json` (flat, lift, queue, pavement…).

Le C1 : l'espagnol n'a **pas** de vocabulaire C1. L'anglais le prend à l'allemand
(948 noms, 272 verbes, 291 adjectifs).

## 2. La grammaire en français, avec ses séries

Une liste par niveau, choisie sur le CECR et sur ce qui piège un francophone :

**A2 (9 fiches)** — le present perfect et le prétérit (for / since, already, yet, ever,
never) ; le past continuous ; les futurs (will, going to, présent en -ing) ; comparatifs
et superlatifs ; les modaux d'obligation (must, have to, should, mustn't ≠ don't have
to) ; les quantifieurs (some / any, much / many, a few / a little) ; verbe + -ing ou to
(enjoy doing, want to do) ; used to ; les prépositions de temps (for, since, during,
ago, until).
*Pourquoi* : c'est le cœur de l'A2 anglais, et le present perfect est LE piège du
francophone (« j'ai vu » ≠ toujours *I have seen*).

**B1 (10 fiches)** — le present perfect continu ; le past perfect ; les conditionnels
1 et 2 (if + présent / prétérit) ; le passif ; le discours indirect ; les relatives
(who, which, that, whose, where) ; les modaux de déduction (must, might, can't) ;
used to / be used to / get used to ; les phrasal verbs (1) ; gérondif ou infinitif
(stop doing / stop to do, remember, try).
*Pourquoi* : le seuil du B1 est de raconter au passé, faire des hypothèses et rapporter
ce qu'on a dit.

**B2 (10 fiches)** — le conditionnel 3 et les mixtes ; wish / if only ; le passif
avancé (have something done, it is said that) ; futur continu et futur antérieur ; les
modaux au passé (should have, must have, could have) ; le discours indirect avancé
(verbes introducteurs : suggest, deny, admit) ; relatives non définissantes et réduites ;
les connecteurs (although, despite, whereas, unless) ; les phrasal verbs (2) ; les faux
amis B2 (eventually, actually, sensible, library…).

**C1 (9 fiches)** — l'inversion (Never have I…, Not only…, Hardly had…) ; les clivées
(What I need is…, It was … who) ; le subjonctif (I suggest that he be) ; ellipse et
substitution (so do I, I hope so, neither) ; les participiales (Having finished…) ; les
nuances des modaux (needn't have, would rather, had better) ; l'emphase (do, such, so) ;
registre et collocations (formel / courant) ; les faux amis C1.

Chaque fiche a sa série « M'entraîner » (≈ 12 à 15 questions), comme l'A1. Total visé :
38 fiches, ≈ 500 questions.

## 3. Les feuilles de conjugaison

Format de l'A1 et de l'espagnol (`espanol/datos/conjugaison.json`) : un tableau court, la
forme entre [ ], le sens, une astuce, la série qui suit.
- **A2 (8)** : present perfect, present perfect négatif et questions, past continuous,
  will, going to, have to, could / was able to, used to.
- **B1 (8)** : present perfect continu, past perfect, would, passif présent, passif
  passé, conditionnel 1, conditionnel 2, discours indirect (le recul des temps).
- **B2 (7)** : futur continu, futur antérieur, conditionnel passé (would have),
  modaux au passé, passif aux temps composés, wish, have something done.
- **C1 (6)** : past perfect continu, subjonctif, inversion, passif des modaux,
  participes composés (having done), futur dans le passé (was going to, would).

L'espagnol en a 10, 10 et 8 (A2-B2).

## 4. Les couches A2-C1 des scènes

Les 37 scènes gardées pour Boston. Les questions **enseignent l'anglais** ; elles
s'appuient sur les **faits de l'image** déjà établis (même zone visée `f`, même repère
`r`), comme l'espagnol l'a fait.
- **A2 — Where is it? les prépositions de lieu** (in, on, under, next to, between,
  behind, in front of, above) : chaque fait de position de l'image, en anglais.
- **B1 — raconter : present perfect et prétérit**, les irréguliers (Mark has cut the
  carrot / He cut it ten minutes ago).
- **B2 — passif et relatives** (The carrot is being cut ; the table on which…).
- **C1 — hypothèses : must, might, can't (have)** (He must be expecting guests).

Visé : ≈ 7 questions par couche A2, 5 à 6 en B1-B2, 4 en C1, soit ≈ 800 questions
(l'espagnol : 1 078 sur 43 scènes, dont 6 écartées pour l'anglais).

## 5. La mesure de la couverture

`python anglais/outils/couverture_comptes.py` compte, niveau par niveau, l'anglais contre
l'espagnol (et contre l'allemand pour le C1, que l'espagnol n'a pas) : noms, verbes,
adjectifs, adverbes, expressions, mots-outils, fiches, questions, feuilles, questions de
scènes. Un niveau n'est dit « complet » que lorsque chaque ligne atteint l'espagnol, ou
qu'un écart est expliqué.

## 6. L'ordre

A2 d'abord, en entier (vocabulaire, grammaire, conjugaison, scènes), mesuré, vérifié,
poussé sur `main` avec le feu vert du chef ; puis B1, B2, C1, une version à la fois.
Avant chaque push : synchroniser avec `main`, relancer `construire.py` et `scenes.py`,
`python tests/verifier.py`, `node tests/syntaxe.js`, et les parcours allemand et espagnol
à 0 écart si `index.html` change.

## 7. Ce qui attendra Jacques

- une **relecture par un anglophone** de tout l'A2-C1 (tout reste « brouillon ») ;
- la **voix** (ElevenLabs) : rien sans son accord, la voix du téléphone en attendant.
