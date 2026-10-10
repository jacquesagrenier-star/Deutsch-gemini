# Compte rendu — branche `corpus-mots-scenes` (session cloud, 10 oct. 2026)

## Ce qui manquait vraiment (vérifié mot par mot)

| Mot du brief | Constat | Fait |
|---|---|---|
| die Armbanduhr | absente | ajoutée, **kleidung_a2** |
| der Heizkörper | absent (die Heizung est en wohnen A2) | ajouté, **wohnen_b1** |
| die Kreide | absente | ajoutée, **schule_a2** |
| der Schwamm | ⚠️ **absent aussi**, contrairement au brief (seul « Schwammerl », le champignon autrichien, existe) | **pas ajouté** : aucune éponge dans l'image de la classe. À ajouter si Jacques le veut (schule A2) |
| der Haken | présent (moebel_haushalt_a2), déjà une zone | rien |
| der Po / das Gesäß | der Po présent (koerperteile_a2), le plus usuel : il reste le mot principal | **das Gesäß** ajouté en **koerperteile_b2**, `registre: schriftlich`, même traduction (fesses / bottom) : `synonymes.json` (dérivé, refait par `tests/synonymes.py`) les relie désormais. C'est la structure de synonyme qui existe. |
| die Unterhose | absente | ajoutée, **kleidung_a2** (à côté de die Unterwäsche) |
| das Stethoskop | absent | ajouté, **gesundheit_b1** |
| der Bauchnabel | absent (der Bauch est en A1) | ajouté, **koerperteile_b1** |

Chaque entrée porte **les mêmes clés que ses voisines** : fr, en, tr, uk, fa (traduction + exemple), pluriel, `article_fr`. Ajoutées avec `tests/ajouter_mots.py ajouts/mots-scenes.json`, qui refuse doublon, champ manquant et champ inconnu (0 refus). Le lot reste dans `ajouts/`.
Pas de clé `pruefung` : elle se calcule sur le PC à partir des listes officielles (`marquer_examen.py`), qui ne sont pas dans le dépôt.

## Les zones dans les scènes

Aucun de ces mots n'était dans une zone : `construire.py` refuse un mot absent du corpus. Ils n'apparaissaient qu'en texte libre (les questions, et les lignes « mots absents » des `_lisez_moi`).

- **Classe** : `kreide`, le petit morceau blanc dans la main du prof (`sur: lehrer`). **die Armbanduhr et der Heizkörper ne se voient pas dans l'image** (personne n'a de montre visible, le radiateur est caché ou absent) : ils sont au corpus, mais sans zone. → l'œil de Jacques.
- **Examen, de face** : `bauchnabel`, `unterhose` (`sur: mark`), `stethoskop` (l'embout sur la poitrine et la fourche près de l'oreille, `sur: aerztin`, donc devant Mark).
- **Examen, de dos** : `stethoskop` (embout sur le dos, fourche). La zone du Po *est* le caleçon : elle porte maintenant aussi `Gesäß` et `Unterhose` (`aussi`). « Trouve ! » ne demande Gesäß qu'à partir d'une séance B2.
- **Cabinet (arztpraxis)** : `stethoskop` au cou de la médecin (embout et deux tuyaux).
- **Questions relinkées** : « Wo hält die Ärztin das Stethoskop? » et « Die Ärztin ___ das Stethoskop auf … » (face et dos) visaient la poitrine ou le dos, c'est-à-dire **la réponse**, allumée avant qu'on réponde. Elles visent maintenant `f: stethoskop`, et la poitrine ou le dos s'allume après la réponse (`r`). « Mark hat sich bis auf die Unterhose ___ » allume le caleçon après la réponse.

### Les masques, sans SAM

Une zone sans masque fait planter la scène, et `detourer.py` demande SAM 2 (modèle sur le PC). Or ces zones sont des **ellipses**, qui ne passent pas par SAM. Nouveau script `visuel/prototype/masques_ellipses.py <scène>` : il fait **exactement** le calcul de `detourer.py` (même code, mêmes constantes), mais seulement pour les zones qui manquent au fichier. Les masques SAM existants ne bougent pas : j'ai vérifié que le fichier se relit et se réécrit à l'octet près. Relancer `detourer.py` sur le PC refera ces zones à l'identique.

Vérification à l'œil : capture headless de chaque zone, avec son contour et son étiquette. Craie, nombril, caleçon et les deux stéthoscopes tombent sur leur objet. Le caleçon de face est fait de quatre ellipses : le contour est un peu « en nuage ». Si Jacques le veut plus net, on peut lui donner une boîte et le passer par SAM sur le PC.

## Vérifié

- `python tests/verifier.py` : 27 632 contrôles, aucun problème. Il ne signale **pas** `frequence.json` en retard, donc pas de `--ecrire`. Les 7 mots neufs n'ont simplement pas de rang : ils passent après les mots classés de leur catégorie. Pour les classer, il faut relancer `python tests/frequence.py --ecrire` sur le PC (archives Leipzig hors dépôt).
- `node tests/syntaxe.js` : OK.
- `construire.py` sur les 8 scènes : tous les mots sont trouvés dans le corpus.

## Pour le PC : l'audio (voix Aurora, ElevenLabs)

Le cloud ne peut ni générer ni même vérifier : `deutschai-b6fbb.web.app` est hors de son réseau. Voici les 28 textes de ces mots, au format de `audio/manifest.py` (mot, mot avec article, pluriel, exemple). `generer.py` saute ce qui existe déjà, donc il suffit de relancer manifeste puis génération pour A2, B1 et B2.

| Empreinte | Texte |
|---|---|
| e6efd063689bacd6 | Armbanduhr |
| da1ee1e026c9084d | die Armbanduhr |
| c8da6e41fd8948a5 | die Armbanduhren |
| 52739a593b11197d | Meine Armbanduhr geht fünf Minuten vor. |
| f2c55eaa7f2b74a0 | Unterhose |
| 1ba850b8edcd4ee5 | die Unterhose |
| e26fdc40029aca75 | die Unterhosen |
| e93798379d3d33e0 | Ich packe fünf Unterhosen in den Koffer. |
| 5e517135a66ca040 | Kreide |
| dda816f74ff64e1f | die Kreide |
| 638dd79316b1cdc5 | die Kreiden |
| 181c47e0f9b67960 | Der Lehrer schreibt mit Kreide an die Tafel. |
| 7e4f75fa686ec6c5 | Heizkörper |
| bbb25b8d69a8c485 | der Heizkörper |
| 44ef1ad479e2fb39 | die Heizkörper |
| df93bb3ccc06faad | Dreh den Heizkörper bitte etwas auf, mir ist kalt. |
| 19308affedee9970 | Stethoskop |
| 0393cf8ead5a098e | das Stethoskop |
| ef86b2247cd7c15d | die Stethoskope |
| 2ceb5695ab08c0e7 | Die Ärztin hört meine Lunge mit dem Stethoskop ab. |
| 08c68d22a2408008 | Bauchnabel |
| 6748c8a7e9c0d567 | der Bauchnabel |
| 77bdbd0c2a893d34 | die Bauchnabel |
| 26d9726d4e3646f5 | Im Sommer trägt sie ein kurzes Top, man sieht ihren Bauchnabel. |
| 1f89f7c7384a2d9b | Gesäß |
| 4c08a1c8db9be1c5 | das Gesäß |
| fe98d25881c41fb4 | die Gesäße |
| 06bb135853b93d5d | Die Spritze bekommen Sie ins Gesäß. |

## Pour Jacques

- Relire les traductions et exemples (surtout tr, uk, fa) et les niveaux choisis.
- Armbanduhr, Heizkörper (et Schwamm) : faut-il une image où ils se voient, ou des retouches de la scène ?
- Essayer les zones sur la prévisualisation : `?scene=klassenzimmer`, `?scene=untersuchung` (« Retourner Mark »), `?scene=arztpraxis`.
