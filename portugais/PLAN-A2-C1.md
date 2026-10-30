# Le portugais A2 à C1 : le plan et l'état

29-30 octobre 2026. Mandat de Jacques, transmis par le chef d'orchestre : une
version de Wortando pour apprendre le portugais, **du Portugal** (« On va
commencer par le portugais du Portugal »), puis « avance le plus possible tout
ce que tu peux pour le portugais ». Session « Portugais A2-C1 », branche
`claude/vigilant-lichterman-c91627`, en parallèle de la session socle (A1,
moteur, scènes `.pt.js`) et de la session mosaïque. Rien n'a été payé : ni voix,
ni génération, ni agent. **Tout est brouillon** : à faire relire par un
lusophone du Portugal.

## En bref

- **Les quatre niveaux sont construits par les outils** : vocabulaire, grammaire,
  séries « par temps », feuilles de conjugaison, mots-outils, et les couches
  A2-C1 des **43** scènes.
- **Au-dessus de l'espagnol partout en A2-B2** pour le vocabulaire, au niveau de
  l'anglais ; le C1 est en dessous de l'allemand pour la même raison que
  l'anglais (ses composés administratifs n'ont pas d'équivalent d'un mot).
- **Portugais d'Europe** : chaque phrase vient de nos corpus (où elle était
  brésilienne) et passe par un convertisseur qui la refuse plutôt que de la
  laisser brésilienne.
- **Construit avec l'A1 du socle** (branche à jour avec `main`, v1026) : son
  `construire.py` appelle `niveaux.construire(jeu, variantes)` et son `scenes.py`
  fusionne les couches ; `portugais/datos` et les scènes `.pt.js` contiennent
  l'A2-C1. L'affichage (temps en plus, séries par temps, feuilles par niveau) est
  à brancher dans `index.html` par le socle.

## Les chiffres (mesurés par `python portugais/outils/couverture_comptes.py`)

Entre parenthèses : l'espagnol et l'anglais (A2-B2), l'allemand et l'anglais (C1).

| | A2 | B1 | B2 | C1 |
|---|---|---|---|---|
| Noms | **708** (es 539 · en 692) | **1074** (es 515 · en 1036) | **431** (es 236 · en 418) | **612** (de 948 · en 548) |
| Verbes | **321** (es 274 · en 309) | **436** (es 314 · en 385) | **189** (es 162 · en 182) | **127** (de 272 · en 175) |
| Adjectifs | **204** (es 154 · en 194) | **342** (es 261 · en 395) | **114** (es 101 · en 124) | **110** (de 291 · en 213) |
| Adverbes | **99** (es 51 · en 92) | **162** (es 119 · en 143) | **86** (es 30 · en 82) | **25** (de 52 · en 44) |
| Expressions | **79** (es 82 · en 126) | **94** (es 55 · en 129) | **118** (es 69 · en 146) | **53** (de 100 · en 111) |
| Mots-outils | **59** (es 27 · en 57) | **35** (es 20 · en 52) | **20** (es 16 · en 18) | **13** (de 0 · en 13) |
| Fiches de grammaire | **10** (en 15) | **10** (en 14) | **10** (en 13) | **9** (en 9) |
| Questions de grammaire (fiches + temps) | **198** (en 748) | **189** (en 753) | **152** (en 534) | **142** (en 502) |
| Feuilles de conjugaison | **10** (es 10 · en 12) | **10** (es 10 · en 12) | **8** (es 8 · en 10) | **8** (de 8 · en 8) |
| Questions de scènes | **307** (es 332 · en 282) | **331** (es 312 · en 281) | **254** (es 254 · en 218) | **180** (de 180 · en 156) |

Ce qui reste en dessous, et pourquoi :

- **Les questions de grammaire** : 681 en A2-C1 (39 fiches, 12 séries par temps),
  quand l'anglais a allongé ses séries à 35-55 questions chacune. L'espagnol, lui,
  en a 1 343 en tout, sans niveau. Allonger les séries (une source
  `series_<niveau>.py`, comme l'anglais) est la suite naturelle.
- **Le C1** : comme pour l'anglais, les ~330 composés administratifs allemands
  (Betreuungsschlüssel, Kommissionierung…) n'ont pas de mot portugais ; leur
  traduction est une glose, écartée par l'extracteur.
- **Les cartes mises de côté** : 329 mots dont la phrase ne contient pas le mot
  (181 noms, 20 verbes, 128 adjectifs) et 108 sans phrase du tout. Plutôt que de
  publier des cartes bancales, `niveaux.py` les saute et les liste dans
  `portugais/outils/rapport_niveaux.txt` ; il suffit d'écrire leur phrase dans la
  source (colonnes 3 et 4) pour qu'elles entrent. L'anglais, lui, en avait gardé
  164.
- **Les expressions A2** : 79 contre 82 en espagnol.
- **32 mots déjà dans l'A1 du socle** sont sautés (un mot n'a qu'une carte).

## Comment c'est fait

### Le principe : un fichier source par niveau, l'A1 n'est pas touché

Tout vit dans des fichiers à part de ceux du socle ; aucun fichier n'a été
touché par les deux sessions.

| Fichier (`portugais/outils/`) | Contenu |
|---|---|
| `noms_a2.py` … `noms_c1.py` | les noms par thème : « article nom \| traduction \| phrase \| sa traduction \| drapeaux » (format de `noms_a1.py`) |
| `mots_a2.py` … `mots_c1.py` | verbes, adjectifs (masculin \| féminin \| …), adverbes, expressions (format de `mots_a1.py`) |
| `grammaire_a2.py` … `grammaire_c1.py` | 39 fiches en français et leurs séries (format de `grammaire_a1.py`) |
| `temps_a2.py` … `temps_c1.py` | « S'entraîner par temps » : 12 séries (clé `temps` de grammaire.json, comme l'anglais) |
| `conjugaison_niveaux.py` | 36 feuilles de conjugaison (format de l'anglais : t, l, a ; chacune renvoie à une série existante) |
| `fonctionnels_niveaux.py` | 127 mots-outils de niveau, avec leurs phrases |
| `irreguliers.py` | **le conjugueur** du portugais d'Europe (voir plus bas) |
| `variante_niveaux.py` | **le convertisseur** Brésil → Portugal (voir plus bas) |
| `banque_niveaux.py` | la banque de 18 000 phrases converties (de nos corpus) |
| `extraire_niveaux.py` | outil à usage unique qui a écrit les brouillons `noms_*` et `mots_*` |
| `niveaux.py` | **le constructeur**, appelé par `construire.py` du socle après l'A1 |
| `couches_a2.py` | outil à usage unique : la couche A2 des scènes, tirée des faits de l'image |
| `couches_b1c1.py` | **source** des couches B1, B2, C1 des 43 scènes, écrites à la main |
| `couverture_comptes.py` | la mesure ci-dessus |
| `portugais/scenes/<scène>.json` | les couches A2-C1 de chaque scène (format de `anglais/scenes/`) |

### Le convertisseur (`variante_niveaux.py`)

Nos corpus allemand et espagnol portent, pour chaque mot, une traduction et une
phrase en portugais : celles de l'interface **pt-BR**, donc brésiliennes (« Meu
primo mora em Berlim », « Você me passa o sal? »). Le convertisseur :

- remplace le **vocabulaire** (autocarro, comboio, telemóvel, pequeno-almoço,
  casa de banho, frigorífico, sumo, equipa, desporto, adepto, guarda-redes,
  passadeira, peão, renda, ementa, talho, esquadra, câmara municipal…) ;
- corrige l'**orthographe** (facto, contacto, registo, receção, económico,
  fenómeno, génio, bebé, ténis…) ;
- met l'**article devant le possessif** (o meu primo, da minha mãe) ;
- fait le **progressif** à la portugaise (estou a fazer, et non estou fazendo) ;
- place le **pronom après le verbe** (chama-se, encontramo-nos), sauf après
  não, que, já, também… ; fait la **mésoclise** au futur (levantar-se-á) ;
- dit **ter de** (et non ter que), **precisar de**, **há** (et non tem) ;
- ramène les villes à Lisbonne, Porto, Coimbra…

Et il **refuse** ce qu'il ne sait pas convertir proprement : « você » et sa
conjugaison, « a gente », un « o / a » pronom devant le verbe, les mots qui
changent de genre d'un pays à l'autre (o cardápio → a ementa). 1 709 phrases
refusées sur 19 800 ; il en reste 18 055.

### Le conjugueur (`irreguliers.py`)

Toutes les formes, pour chaque verbe : présent, perfeito (falámos, avec
l'accent du Portugal), imperfeito, futuro, condicional, conjuntivo présent,
imparfait et futur, mais-que-perfeito composto, perfeito composto, impératif,
participe (aceite, entregue, pago…), gérondif ; les verbes pronominaux avec
l'enclise et la mésoclise (lembrar-me-ei) ; les composés de pôr, ter, vir,
fazer, dizer, ver ; les alternances (sinto, durmo, sobes, progrido) ; les -uir
et -air (incluíssemos, saíres). Les verbes A2-C1 portent ces temps dans des clés
en plus de celles de l'A1 : `conj_imperfeito`, `conj_futuro`,
`mais_que_perfeito`, `perfeito_composto`, `participio`, `gerundio`.

### Les scènes

- **A2, « Onde está? »** : les prépositions de lieu, tirées des faits de la couche
  allemande (« Wo steht der Topf? → neben der Pfanne » → « Onde está o tacho? →
  ao lado da frigideira »), avec les mots de la table du socle. 307 questions ;
  25 faits sautés (adjectif, groupe compliqué).
- **B1, B2, C1** : écrites à la main sur les **mêmes faits** que l'allemand. Là où
  l'allemand enseigne le datif ou la déclinaison, le portugais enseigne ce qui se
  trompe au même endroit : le pronom lhe, l'accord de l'adjectif, le perfeito,
  em ou para, le passif, cujo, como se, la mésoclise ; le C1, partout, les
  hypothèses (deve, talvez, pode ser que, futur de supposition, dizem que, le
  conditionnel de la rumeur). 765 questions.
- Lisbonne : la poste est « os correios », la mairie « a Loja do Cidadão », la
  ferme « a quinta », le tram « o elétrico », Hambourg et Berlin deviennent
  Lisbonne.

## Le branchement (pour la session socle)

1. `construire.py` appelle `niveaux.construire(jeu, variantes)` : fait (socle, v1026).
2. `scenes.py` fusionne `portugais/scenes/<scène>.json` : fait (socle, v1026).
3. `index.html` : lire pour le portugais la clé `temps` de grammaire.json,
   `niveaux` de conjugaison.json, le niveau des fiches, et (si voulu) les temps
   en plus dans la carte de verbe.
4. Avant de pousser : `python tests/verifier.py`, `node tests/syntaxe.js`, et les
   deux parcours de / es à 0 écart (le socle touche `index.html`).

## Pour une future variante brésilienne

Tout ce qui distingue les deux pays est rangé dans `variante_niveaux.py`, prêt à
servir à l'envers : la table de vocabulaire `BR_PT_VOCAB` (≈ 200 paires), les
orthographes `ORTHO_LISTE` et la règle des voyelles ouvertes (económico /
econômico), les mots qui changent de genre `GENRE_CHANGE`, et la syntaxe (article
devant le possessif, a + infinitif, place du pronom, ter de, há). La fiche C1
« Portugal ou Brésil ? » les enseigne déjà à l'apprenant. Les phrases d'origine,
brésiliennes, sont toujours dans nos corpus (champs `exemple_pt`).

## Vérifié

- `python portugais/outils/niveaux.py` construit les quatre niveaux sans erreur ;
  chaque série a sa bonne réponse hors des mauvaises, aucune question en double.
- `node tests/syntaxe.js` : les 8 blocs de `index.html` s'analysent.
- `python tests/verifier.py` : 206 problèmes, **tous antérieurs** à cette branche
  (sons d'Aurora absents de ce dossier, 4 CSV d'export en retard) ; cette branche
  ne touche que `portugais/`.
- Pas de parcours de / es : rien de l'allemand ni de l'espagnol n'est touché ici.

## Questions pour Jacques

1. **Qui relit ?** Tout est brouillon. Une relecture par un lusophone **du
   Portugal** est nécessaire avant d'ouvrir le portugais à d'autres que toi :
   les phrases converties surtout (elles viennent du Brésil), puis les fiches.
2. **Le C1 plus court que l'allemand** : comme pour l'anglais, les composés
   administratifs allemands sont écartés faute de mot portugais. Même choix ?
3. **La grammaire** : viser le volume de l'anglais (≈ 750 questions par niveau,
   séries allongées) ou en rester au niveau actuel (≈ 170 par niveau, proche de
   la densité de l'espagnol) ?

## La suite possible

- Écrire les phrases des 437 cartes mises de côté (liste dans `rapport_niveaux.txt`).
- Allonger les séries de grammaire (`series_<niveau>.py`, comme l'anglais).
- Les tuiles de grammaire portugaises (pronoms, prépositions, connecteurs…),
  comme `tuiles_niveaux.py` de l'anglais.
- La fréquence et les mots voisins (Leipzig portugais), comme l'anglais.
