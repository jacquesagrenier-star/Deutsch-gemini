# Consigne du relecteur — relecture complète espagnol + allemand

Tu relis une partie du contenu de Wortando, une app d'apprentissage de l'allemand (interface en fr, en, tr, uk, fa, ar, pt-BR, pl, ru) et de l'espagnol d'Espagne (interface en fr, en, pt-BR, ar, de). Les lots se trouvent dans `C:\Users\jacqu\AppData\Local\Temp\claude\qualite\complet\` (`lot-NNN.json`).

Règles de travail :

- Tu travailles en **lecture seule** sur le dépôt.
- Tu n'écris **que** les fichiers `verdict-NNN.json` de ce dossier.
- Tu ne lances aucun autre agent, tu ne vas pas sur internet, tu ne touches pas à git.

Chaque lot est une liste d'entrées `{app, famille, fichier, chemin, entree}` :

- `app` vaut « de » si la langue apprise est l'allemand, « es » si c'est l'espagnol ;
- `entree` est l'objet tel qu'il est dans le fichier.

Les champs suffixés `_fr`, `_en`, `_tr`… (ou `En`, `Tr`… pour `options` et `correct`) sont les traductions. Un champ sans suffixe est soit le texte dans la langue apprise (`mot`, `exemple`, `question`…), soit le français (`traduction`, `translation`, `hint`, `explanation`).

## Ce que tu cherches : SEULEMENT des fautes de fait

1. **Traduction fausse** : mauvais sens, faux ami, sens d'un AUTRE mot. Ou une traduction de phrase qui ne correspond pas à la phrase source : autre phrase, négation perdue, sujet, nombre ou temps qui change le sens. Ou une traduction qui appartient visiblement à l'entrée voisine.
2. **Langue apprise fausse** : genre, article ou pluriel faux ; conjugaison fausse ; faute de grammaire ou d'orthographe (accents, umlauts) dans l'allemand ou l'espagnol.
3. **Phrase d'exemple** qui n'utilise pas le mot enseigné, ou qui n'est pas au temps annoncé.
4. **Exercice** :
   - la réponse attendue est fausse ;
   - une autre option serait aussi juste (distracteur ambigu) ;
   - la phrase complétée est fautive ;
   - l'explication contredit la réponse ;
   - l'indice induit en erreur.
5. **Mauvaise langue** : de l'anglais ou du français dans un champ d'une autre langue, du russe dans l'ukrainien, de l'arabe dans le persan (et l'inverse), de l'espagnol dans le portugais.
6. **Faute** de grammaire ou d'orthographe dans une traduction : français, anglais, turc, ukrainien, persan, arabe, portugais, polonais, russe, allemand.
7. **Fiche ou explication de grammaire** : une règle fausse, ou un exemple qui contredit la règle.

Ne signale PAS :

- le style ou un synonyme possible ;
- une tournure « plus naturelle » ;
- un registre discutable ;
- une variante régionale légitime (le portugais d'Europe dans le champ pt n'est pas une faute) ;
- une traduction libre qui garde le sens ;
- une explication raccourcie qui reste juste.

Si tu hésites, mets la certitude « moyenne ». Si tu hésites beaucoup, ne signale pas.

## Ce que tu écris

Pour CHAQUE lot qu'on te confie, écris `verdict-NNN.json` (même numéro), même s'il est vide. C'est ce fichier qui marque le lot comme fait.

Le fichier contient une liste JSON d'objets :

```json
{"fichier": "...", "chemin": "...", "champ": "exemple_uk",
 "actuel": "le texte EXACT tel qu'il est dans le lot",
 "probleme": "en français, une phrase",
 "propose": "la correction",
 "certitude": "haute" | "moyenne"}
```

`fichier` et `chemin` sont copiés de l'entrée. `champ` est le nom exact de la clé (avec son chemin interne si l'entrée est imbriquée, par exemple `praesens.du` ou `couches.B1.qs[2].sens_ar`).

Lis chaque lot EN ENTIER (outil Read ; s'il dépasse 2 000 lignes, plusieurs lectures avec offset) avant d'écrire son verdict. Quand tous tes lots sont faits, réponds en quelques lignes : les lots relus, le nombre de signalements par lot, les trois plus graves.
