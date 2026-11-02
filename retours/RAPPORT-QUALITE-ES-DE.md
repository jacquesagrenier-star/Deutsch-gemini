# Contrôle de qualité : l'espagnol et l'allemand

2 novembre 2026, à la demande de Jacques : « une analyse de qualité du contenu, avec des analyses croisées », pour les deux langues déployées en premier.

## En bref

- **Le contenu est sain.** Les contrôles mécaniques ont passé environ 530 000 textes au crible : mots, phrases, conjugaisons, exercices, fiches, scènes, dans toutes les langues d'interface. Ensuite, un autre modèle (Sonnet) a relu 290 entrées tirées au hasard. Il n'a trouvé **aucune** faute dans les 90 entrées allemandes en 9 langues. Sur les 110 entrées espagnoles en 5 langues, il a relevé **un doute**. Dans les 90 exercices, il n'a trouvé **aucune** réponse fausse.
- **Les défauts trouvés sont localisés** : des textes restés en anglais ou en français, des explications abrégées dans certaines langues, des articles français mal accordés. Aucun mot ne porte un faux genre ou un faux pluriel. Les 873 conjugaisons espagnoles sont justes.
- **891 champs corrigés** dans 6 fichiers sources, tous côté traduction ou interface. Le détail est dans `retours/qualite-es-de/corrections.json`.
- **Aucune phrase allemande ni espagnole n'a été touchée.** Chacune a sa voix enregistrée, nommée d'après son texte : la modifier la rendrait muette, et la refaire coûte de l'argent. Les 8 phrases à revoir sont donc dans « À trancher ».

## Ce qui a été corrigé

| Défaut | Où | Langues | Champs |
|---|---|---|---|
| Exercices en **anglais** servis aux turcophones (phrase à construire, traduction, 1re phrase de l'explication) | `exercices.json`, « blocs connecteurs » et « ordre inversé » | tr | 43 |
| Option « Ça dépend (Wechselpräposition) » sans traduction : elle s'affichait en **anglais** (« It depends ») | `exercices.json`, « Quel cas ? » des prépositions, 50 exercices | tr, uk, fa, ar, pt, pl, ru | 700 (options et réponses) |
| Explication restée en **français** | `exercices.json`, Konjunktiv II n° 18 | fa | 1 |
| Indice faux : « verbe conjugué « bringen » » (le verbe est à l'infinitif après un modal), et la particule séparable oubliée | `exercices.json`, « Quel infinitif ? » | tr | 7 |
| Explications des der-/ein-Wörter **sans l'exemple allemand** (« Sujet, féminin. » au lieu de « die Frau → diese ») | `exercices.json`, 33 exercices | tr, uk, fa | 99 |
| **Article français** collé à la traduction et faux : « la une personne », « le un plat », « l'conjoint », « la appartement de vacances »… | `themes.json`, 25 noms (28 entrées) | fr | 28 |
| Exercice des nombres espagnols : la traduction portugaise écrivait le nombre **en toutes lettres** (« setecentos »), ce qui donnait presque la réponse (« setecientos ») | `espanol/datos/ejercicios.json` | pt | 4 |
| Fiches espagnoles **amputées en anglais**, alors que l'anglais est la priorité « Learn Spanish » : manquaient *cuando llegue* et *espero que vengas* (subjonctif), *explícamelo* et *se lo doy* (pronoms), *he comido* en Espagne et *comí* en Amérique latine (passés) | `espanol/datos/grammaire.json`, encadrés « attention » des fiches pasados, subjuntivo, pronombres | en | 3 |
| Faute de français : « mais de la débat sur elle » | `pruefung.json`, Hören n° 116 | fr | 1 |
| *auffallen* au Präteritum (« Mir fiel auf ») traduit par un imparfait de durée (« Je remarquais », « I was noticing ») ; pt, ar, pl et ru disaient déjà « j'ai remarqué » | `verbe.json` B1 | fr, en, tr, uk, fa | 5 |

**Ces traductions sont les miennes. Aucun locuteur natif ne les a relues** (turc, ukrainien, persan, arabe, portugais, polonais, russe). Elles remplacent de l'anglais, du français ou un texte faux : elles ne peuvent pas être pires que ce qu'elles remplacent, mais elles méritent un coup d'œil natif.

## Ce qui a été vérifié

Les outils sont dans `retours/qualite-es-de/` et se relancent depuis la racine du dépôt (voir « Relancer »).

| Contrôle | Quoi | Volume | Résultat |
|---|---|---|---|
| `langues.py de` / `es` | Chaque texte français et ses traductions. Champ manquant ou vide ; copie du français ou de l'anglais ; mauvais alphabet ; lettres russes dans l'ukrainien (et l'inverse), persanes dans l'arabe (et l'inverse) ; mots-marqueurs français, anglais ou espagnols ; chiffres et questions alignés sur la source ; traduction identique à celle de l'enregistrement **voisin** (décalage) | 319 904 textes allemands, 84 860 espagnols | Les défauts du tableau ci-dessus. Le reste : contenu commun (formes allemandes ou espagnoles citées), nombres écrits en lettres, synonymes légitimes chez deux voisins |
| `scenes_es.py` + `traductions-decalees/scenes_check.py` | Couches A2-C1 des scènes espagnoles ; traductions des scènes allemandes ; articles de `mots.json` | 9 376 + 2 507 × 8 | Rien : 0 traduction périmée, 0 orpheline, articles conformes au corpus |
| `mots.py` | Même mot dans plusieurs thèmes : genre, pluriel, traductions ; la phrase contient-elle le mot ; article français ; espagnol : pluriel contre la règle, genre contre WikDict, article allemand de `traduction_de` contre le corpus allemand | 4 275 noms allemands, 1 796 espagnols | Articles français (corrigés). Aucun genre ni pluriel faux. `tests/contraste.py` (WikDict) ne donne que des cas connus et justes : Tor, See, Gehalt, Golf… |
| `verbes_de.py` | Chaque phrase de verbe (présent, Perfekt, Präteritum, Konjunktiv II) contient-elle une forme de CE verbe (squelette du radical, ablaut compris) | 5 256 phrases | 8 phrases qui enseignent un autre verbe (À trancher) |
| `verbes_es.py` | Les temps se recoupent : un seul participe au perfecto, conditionnel = radical du futur, imparfait régulier, subjonctif tiré du « yo », impératif usted/ustedes = subjonctif, vosotros, nosotros… | 873 verbes | Rien |
| `regulier_es.py` | Présent et prétérit comparés à la forme régulière ; les 117 écarts relus un à un | 873 verbes | Tous des irréguliers justes |
| `exercices.py` | Réponse parmi les options ; options en double ; options traduites de même longueur et **réponse au même rang** dans chaque langue ; explication qui cite une autre option que la bonne ; morceaux à ordonner ; espagnol : la réponse est bien la forme du tableau pour le verbe de l'indice | 2 721 exercices allemands, 1 343 espagnols | Rien de faux. Les 36 « explications » signalées sont des explications communes à une série, justes |
| `fiches.py` | Chaque exemple allemand ou espagnol cité en gras ou entre guillemets dans le français se retrouve-t-il dans chaque traduction ; balises | 116 713 + 30 633 textes | Les fiches espagnoles **réécrites pour chaque public** (anglophones, lusophones, germanophones, arabophones) expliquent la plupart des écarts. Restaient l'anglais amputé (corrigé) et les explications abrégées (corrigées en partie, voir À trancher) |
| Relecture Sonnet, lot allemand | 90 entrées au hasard (noms, verbes, adjectifs, adverbes, expressions), mot + phrase, 9 langues | ≈ 1 600 textes | **0 faute** |
| Relecture Sonnet, lot espagnol | 110 entrées au hasard, mot + phrase, 5 langues | ≈ 1 100 textes | 1 doute (« reseñar ») |
| Relecture Sonnet, exercices et verbes | 90 exercices au hasard des deux langues, et les 96 phrases de verbes que `verbes_de.py` n'avait pas su trancher | 186 entrées | 0 réponse fausse ; 8 phrases de verbes, 1 explication, 1 traduction |

Tous les signalements ont été vérifiés dans le fichier lui-même avant d'être retenus, jamais sur la seule citation du relecteur.

**Limite de la relecture par un autre modèle.** Sonnet et moi ne sommes pas deux avis indépendants : nous partageons une partie de nos angles morts, surtout pour les langues rares de l'interface. L'échantillon borne le taux de fautes de sens sous ≈ 3 % (0 sur 90, à 95 %), sans l'exclure. Pour aller plus loin, il faut un autre fournisseur ou un locuteur natif.

## À trancher par Jacques

### 1. Huit phrases allemandes qui n'illustrent pas le verbe enseigné

Elles ne sont pas fausses en allemand, mais elles enseignent un autre verbe. Les corriger changerait le texte, donc la voix enregistrée (dépense ElevenLabs à approuver). Proposition :

| Verbe (`verbe.json`) | Temps | Phrase actuelle | Proposition |
|---|---|---|---|
| entsorgen (B1) | Konjunktiv II | Alte Batterien würde ich nie in den Hausmüll **werfen**. | … nie **im Hausmüll entsorgen**. |
| wirken (B2) | Perfekt | Seine Worte haben lange **nachgewirkt**. | Seine Worte haben lange **gewirkt**. |
| gucken (B1) | Konjunktiv II | Ich würde lieber ein Buch lesen als **fernzugucken**. | … als **Fernsehen gucken**. (« als fernzugucken » est aussi bancal) |
| lassen (A2) | Konjunktiv II | Ich würde das nicht **zulassen**. | Ich **ließe** das nicht zu… ou une phrase avec *lassen* seul |
| lügen (A2) | Perfekt | Sie hat mich nie **angelogen**. | Sie hat nie **gelogen**. |
| blasen (B1) | Perfekt | Der Wind hat das Laub **weggeblasen**. | Der Wind hat stark **geblasen**. |
| kommen (A1) | Konjunktiv II | Er **käme** gern **mit**, wenn er könnte. | (mitkommen ; acceptable, à toi de voir) |
| legen, hängen (A1) | Konjunktiv II | … woanders **hinlegen** / **aufhängen** | (composés transparents ; le relecteur ne les signale pas) |

Une phrase changée doit garder ses traductions dans les 9 langues. Pour les quatre premières, le sens ne bouge pas : les traductions restent justes.

### 2. Points de sens ou de cohérence

- **Espagnol, « reseñar »** (`verbos.json` B2) est traduit « recenser, chroniquer ». En français courant, « recenser » veut dire « compter ». Proposition : « faire la critique de, chroniquer ».
- **Espagnol, « reciente »** (`adjetivos.json`) : la traduction allemande « kürzlich, jüngst » donne deux adverbes pour un adjectif, et la phrase dit « aktuelle ». Proposition : « neu, jüngst » (à faire relire par la germanophone, `retours/A-RELIRE-INTERFACE-DE.md`).
- **Espagnol, pimiento** : « die Paprika » dans la traduction allemande, « der Paprika » dans le corpus allemand. Les deux genres existent ; faut-il les harmoniser ?
- **Allemand, aber / sondern n° 28** : l'explication renvoie à « la phrase précédente du même couple » (« its twin »). Si la série est mélangée, l'apprenant ne la voit pas.
- **Espagnol, Arabe, scène du musée (B2)** : « escuchar ← escuchando » est une flèche entre deux mots latins dans un texte arabe, cas déjà connu (`espanol/ar/fleches.py`). À regarder à l'écran.

### 3. Explications abrégées (rien de faux, moins d'aide)

- **Turc, examen** (`pruefung.json`) : une douzaine d'explications Sprechen, Schreiben, Lesen et Hören perdent la citation allemande qui les illustre (« danach FAHRE ICH », « Mit freundlichen Grüßen »…). Les remettre demande d'écrire du turc ; je ne l'ai pas fait.
- **Fiches espagnoles en anglais, « genre »** : l'encadré ne cite pas les pièges du genre (*el color*, *la leche*…), propres aux francophones. Pour un anglophone, sans genre, c'est défendable.
- **VHS (cours de Jacques)** : les mots repris dans `vhs_kapitel1_b1` ont un article en anglais et en arabe (« the hair », « الشعر ») là où le corpus n'en met pas. C'est une question de style.

## Contrôles avant publication

| Contrôle | Résultat |
|---|---|
| `python tests/verifier.py` | 46 106 contrôles passés, aucun problème |
| `node tests/syntaxe.js` | OK, les 8 blocs `<script>` |
| `python tests/trous_francais.py` | aucun texte français recopié dans une langue cible |
| Parcours allemand contre `de-v1055` | 128 chemins, **0 écart** |
| Parcours espagnol (`es-moteur`) contre `es-v1042` | 77 chemins, **0 écart** |

Zéro écart est attendu : les parcours se font en français. Or aucune correction ne touche le texte français que ces chemins affichent : ils ne tirent aucun des 28 noms corrigés, ni l'examen.

## Relancer

Depuis la racine du dépôt :

```
python retours/qualite-es-de/langues.py de sortie-de.json
python retours/qualite-es-de/langues.py es sortie-es.json
python retours/qualite-es-de/mots.py sortie-mots.json
python retours/qualite-es-de/verbes_de.py
python retours/qualite-es-de/verbes_es.py
python retours/qualite-es-de/regulier_es.py
python retours/qualite-es-de/exercices.py
python retours/qualite-es-de/fiches.py
python retours/qualite-es-de/scenes_es.py
python retours/qualite-es-de/lots_relecture.py <dossier>      # lots tirés au hasard, graine fixe
python retours/qualite-es-de/corriger.py [--ecrire]           # idempotent : relancé, il ne change plus rien
```

Le plus utile à garder : `langues.py`, qui prend une quinzaine de secondes. Il aurait vu le turc resté en anglais et l'option « It depends » le jour où ils sont entrés.
