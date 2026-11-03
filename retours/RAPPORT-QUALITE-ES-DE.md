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

### 1. Huit phrases allemandes qui n'illustrent pas le verbe enseigné — TRANCHÉ, v1069

> **Décision de Jacques (2 nov.) : « Oui, corrige-les ».** Les six premières sont corrigées dans la **v1069**. Leurs traductions ont été réécrites dans les 9 langues quand le sens changeait (lassen, lügen, blasen). Leurs voix ont été refaites : Aurora, `eleven_multilingual_v2`, **220 crédits**. Les six sons sont sains (`controler_sons`) et en ligne. mitkommen, hinlegen et aufhängen restent tels quels. `AUDIO_REVISION` n'est pas monté : les phrases neuves ont de nouveaux noms de fichiers, il n'y a aucun cache à invalider. Outils : `retours/qualite-es-de/phrases_verbes.py` et `voix_phrases.py`.

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

## La passe visuelle (demandée le 2 nov. : « autant le contenu […] que le visuel »)

Tous les écrans ont été passés au téléphone (375 × 812), de jour et de nuit, dans chaque langue d'interface. Ce sont les écrans que `tests/francais_ailleurs.py` sait ouvrir : les écrans directs, puis chaque tuile et chaque option de ses panneaux. Au total, environ 250 écrans par langue pour l'allemand et 130 pour l'espagnol. L'outil `retours/qualite-es-de/visuel.py` mesure au lieu de regarder :

- un texte rogné ou à moitié hors de l'écran ;
- un texte qui déborde de son bouton ;
- une page qui défile en largeur ;
- un écran vide ;
- en arabe et en persan, un bloc arabe écrit de gauche à droite ;
- de nuit, le contraste (`tests/audit-contraste.js`).

Le détecteur a été **étalonné** sur trois défauts fabriqués (texte rogné, bouton trop étroit, texte hors de l'écran) avant d'être cru : la première version en ratait deux.

| Passe | Langues | Résultat |
|---|---|---|
| Allemand, jour, complet | fr, en, tr, uk, fa, ar, pt, pl, ru | **1 défaut** : le radar des réglages, étiquette rognée en ukrainien (« Прикметники ») et en russe (« Прилагательные ») |
| Espagnol, jour, complet | fr, en, pt, ar, de | **1 défaut** : le même radar, en français (« Marqueurs ») et en portugais (« Marcadores »). En espagnol il n'a que 5 branches, et l'étiquette de gauche dépasse le cadre de 10 px |
| Nuit | fr, ar, fa (de) ; fr, ar, de (es) | Aucun texte rogné. Le contraste signale surtout des faux positifs (boutons en dégradé que l'audit ne sait pas mesurer). Restent quelques textes sous 4,5:1 sans être illisibles : « /10 » sous l'anneau (3,8), la rangée A2-C1 (4,3), les points des badges (4,0) |
| RTL (ar, fa) | — | Aucun bloc arabe écrit de gauche à droite |
| Écrans vides | — | Aucun. La « scène de la séance » est vue vide parce que son texte vit dans un iframe, que l'outil ne mesure pas |
| Scènes | de : fr, ar, ru, tr, fa ; es : fr, en, ar, de, pt — 43 scènes, 8 060 zones touchées par app | **1 défaut** : dans le cabinet médical, l'étiquette de la carte d'assurance maladie sort de l'écran à droite, en russe (« карточка медицинского страхования ») et en portugais (« o cartão do plano de saúde… »). La traduction est trop longue et l'étiquette ne passe pas à la ligne. Transmis à la session des scènes, qui tient `visuel/prototype/` |

**Corrigé dans la v1069** : `overflow: visible` sur le radar (`#progressRadar`). Une ligne de style suffit : l'étiquette déborde dans la marge de la carte au lieu d'être coupée.

Les signaux « zone cachée » (au centre de son cadre, le doigt tombe sur un autre objet) ne sont pas des défauts : le centre d'une chaise est souvent sur la table. 122 par app, liste dans le dossier de travail.

## La relecture complète (décision de Jacques : « passer à travers tout au complet »)

Tout le contenu est découpé en **1 309 lots**, soit environ 650 000 textes (`lots_complets.py`, découpage déterministe). Chaque lot est relu en entier par Sonnet, à 3 relecteurs à la fois au plus. Chaque signalement est trié à la main dans `triage.json` (appliquer, écarter ou à trancher), avec sa raison. Il est ensuite appliqué par `verdicts.py --ecrire`, qui vérifie le texte actuel avant de le remplacer. Une même faute recopiée dans un chapitre VHS est corrigée avec l'original, mais seulement si le sens français est le même : Betreuer est directeur de mémoire à l'université, animateur dans une sortie d'enfants.

Ce que la relecture a rapporté de plus, que les contrôles mécaniques ne voyaient pas :

- **une faute systématique en persan**, « روان است » (« fluide ») pour « gilt / läuft » (« est en vigueur, court »), dans 15 phrases, toutes corrigées ;
- **des traductions d'une autre phrase**, par exemple annehmen au Konjunktiv II en tr, uk et fa (« à ta place, je supposerais le meilleur ») ;
- **des sens parasites d'homonymes** : Leitung = tuyau, Lager = camp, die Leiter = chef, Einnahme = prise de médicament ;
- **des faux amis** : solar system, sistema solar, café da manhã ;
- **des articles français faux** : « la guide », « la vacances », « la pot » ;
- **un « a » latin caché dans un mot cyrillique**. Il est vérifié mécaniquement : c'est le seul cas du corpus (`homoglyphes.py`).

### Journal d'avancement

| Étape | État |
|---|---|
| Lots relus | voir `python retours/qualite-es-de/verdicts.py <dossier> --etat` ; dernier relevé dans la ligne ci-dessous |
| Relevé au 2 nov., 10 h | 225 lots sur 1 309 (noms allemands A1-C1, chapitres VHS, verbes A1-A2) ; 240 signalements : 214 à appliquer, 16 écartés, 9 à trancher |
| Publié, lot 1 (2 nov., ≈ 10 h 15) | 254 champs corrigés dans `themes.json` et `verbe.json`, traductions seulement (une forme féminine fautive retirée : das Zeug → « Zeugin ») ; vérificateur 46 171 OK, parcours de-v1055 0 écart. Détail : `retours/qualite-es-de/corrections-relecture.json` |
| Publié, lot 2 (2 nov.) | lots 226 à 353 (verbes B1-C1, adjectifs A1-C1, adverbes A1-B2) ; 138 champs corrigés dans `verbe.json`, `adjectif.json` et `adverbe.json`, traductions seulement (persan 50, russe 16, polonais 13, turc 17, ukrainien 18, arabe 10, portugais 8, français 6) ; vérificateur 47 963 OK, parcours de-v1055 0 écart |
| Publié, lot 3 (2 nov.) | lots 354 à 407 (adverbes B2-C1, expressions A1-C1, mots-outils, exercices jusqu'au Konjunktiv II) : 64 champs corrigés, traductions et deux distracteurs d'exercice, « du aßt » et « du last », qui sont aussi justes (remplacés par isst et liest) ; et les **phrases allemandes à voix**, accord de Jacques du 2 nov. (« Oui, jusqu'à 5 000 ») : 92 « Perfekt » de B2-C1 refaits (86 passifs au Präteritum en « ist … worden », 5 passifs d'état, hochfahren avec sein), 16 phrases isolées (dont le Plusquamperfekt d’einkalkulieren) et leurs traductions quand le sens change, le pluriel Geburtsurkunden, deux formes fautives d'übersehen (übersehet), erschrecken aligné sur ses phrases (verbe faible, « effrayer »), krankmelden réfléchi. **110 voix Aurora v2, 4 723 crédits** (dont 43 pour une prise refaite) ; `controler_sons.py` sans défaut (un clic d'attaque réparé par 80 ms de silence et un fondu de 8 ms) ; déposées. Détail : `corrections-phrases-voix.json` ; scripts `phrases_relecture.py`, `voix_relecture.py` |
| Publié, lot 4 (2 nov., sans voix) | lots 408 à 521 (exercices : cas, relatifs, déclinaison, prépositions, ordre des mots, connecteurs, particules) : 280 champs corrigés, traductions et exercices. Corrections groupées : l'indice hors sujet de 9 exercices de relatifs au génitif (9 langues), la réponse de « zuerst » (Zeit, pas Verbindung) avec son explication, deux options persane et arabe des particules qui reprenaient le mot d'une autre option (50 exercices), un point combinant parasite dans le turc ; 30 « перед » + nominatif en ukrainien ; les possessifs ukrainiens його / її inversés. Vérificateur 47 904 OK, parcours de-v1073 0 écart |
| Publié, lot 5 (2 nov.) | lots 522 à 610 (exercices de connecteurs, particules, prépositions, passif, Konjunktiv, examen) : 76 champs corrigés, dont « Ohne Karte **hätten** wir uns verlaufen » (sich verlaufen prend haben ; une voix, 36 crédits, total 4 759 sur 5 000), une explication de passif qui décrivait le passif d'état, l'explication de « linke / rechte » à l'examen (8 langues), cinq distracteurs aussi justes que la réponse, « nachweislich » dans une lettre de recours (5 langues). Parcours de-v1073 0 écart |
| Relecture terminée (3 nov.) | **1 309 lots relus sur 1 309**, allemand et espagnol, sans échantillon. Les 315 derniers lots (espagnol) relus après la reprise décidée par Jacques (« Oui, relance-le ») |
| Publié, correctif des réponses traduites (3 nov., 7e9cd09) | défaut d'affichage trouvé en relisant : l'écran juge l'option choisie contre `answers` (fr, en, tr) alors qu'il affiche `options<Langue>` ; en uk, fa, pt, ar, pl, ru la bonne option était comptée fausse. 1 066 réponses ajoutées dans 152 exercices allemands, 7 dans l'espagnol ; `reponses_traduites.py --controle` : 0 défaut |
| Publié, lots 6 et 7 (v1084) | 186 champs de et es (fiches, Premiers pas, conjugaison, prononciation corrigée à la source, traductions des verbes, adjectifs, expressions, exercices et examen espagnols) ; les décisions de Jacques du 3 nov. (wissen/kennen à deux réponses, l'explication de kannte, schließlich = Zeit, Glückspilz à deux réponses, « Ich gehe nicht, sondern ich bleibe », « Serían las diez » = conditionnel de probabilité). Aucune voix. Vérificateur 48 072 OK ; de-v1083 : 1 écart voulu (« Personnels et réfléchis ») ; es-v1083 : 0 écart ; références de-v1084, es-v1084 |
| Publié, scènes (données, sans numéro) | Les 101 signalements de scènes triés : 93 corrigés sans voix dans 78 sources (`scenes_relecture.py`, `scenes_relecture2.py`, journal `corrections-scenes.json`) — traductions des scènes, sens et notes espagnols (le « futur de supposition » de sept C1 qui parlaient de l'avenir), distracteurs qui donnaient une seconde phrase juste remplacés par une forme fautive, et le chocolat de supermarkt remis au présent (« Elle doit vouloir du chocolat », comme l'allemand) dans le français et ses huit traductions ; 2 écartés (l'image tranche) ; 1 à un arabophone (Akkord rendu par « وتر », corde, dans musik). Vérificateur 48 139 OK ; de-v1084 : 1 écart, tirage de konjunktionen ; es-v1084 : 0 écart |
| Reste | À Jacques, avec voix (`qualite-es-de/A-JACQUES-VOIX.md`, environ 650 crédits) : bibliothek « Auf wen wartest du? », cinq phrases espagnoles de scènes (comida, viaja por, piloto, velas, guardado), « fue sólido », « Mantuvieron una reunión secreta ». À trancher : les 33 notes « construccion » des verbes espagnols en anglais, « Habrá tráfico » (explication), oponer / oponerse |
| Lot 6, prêt et NON publié | dans `~/.wortando/wt-publier` (non validé) : 25 champs (fiches de grammaire, Premiers pas en 6 langues, conjugaison, « viel » corrigé à la source d'`prononciation.json`, qui est régénéré). Vérificateur 47 904 OK. Parcours contre de-v1073 : **1 écart voulu**, la fiche « Personnels et réfléchis » en français. Pour publier : pull, version **1074** (accordée par le chef), référence `de-v1074`, CLAUDE.md (comparaison et historique), es-moteur à 0 écart, push, wortando.com/version.json |
| Ce qui attend dans `triage.json` | **68 signalements de scènes** (décision « scene ») : à corriger dans `visuel/prototype/traductions/<scène>.<langue>.json` puis `construire.py <scène>` et les chaînes anglaise et portugaise ; deux viennent de la source : l'allemand de bibliothek (« Worauf wartest du? — Auf meine Freundin » → « Auf wen », voix) et le français de supermarkt (« Elle a dû vouloir » pour une déduction au présent, 10 signalements). **10 à trancher par Jacques** : schließlich, cinq distracteurs wissen/kennen et une explication, « Ich kann nicht, sondern ich bleibe », « Du bist vielleicht ein Glückspilz », l'arabe de « zwei Geschwister ». Aucun « appliquer » en attente hors lot 6 |
| Voix | 4 759 crédits dépensés sur 5 000 accordés ; reste 241 |
| Reprise après une interruption | refaire les lots (`lots_complets.py <dossier>`, même découpage) ; relancer les relecteurs sur les lots sans `verdict-NNN.json` ; les verdicts et `triage.json` sont gardés |

### Phrases allemandes à voix

Faites le 2 nov. (lot 3 ci-dessus), avec l'accord de Jacques et dans son plafond de 5 000 crédits : il en reste **277** pour les phrases que la suite de la relecture trouvera. Une phrase allemande signalée par la suite passe par `phrases_relecture.py` (liste ISOLEES, avec ses traductions), puis `audio/manifest.py --ecrire`, `voix_relecture.py <manifeste-avant> --a-blanc` pour le compte, la génération, `controler_sons.py` et `deposer.py`.

Restent à trancher par Jacques, sans voix : l'arabe de « Ich habe zwei Geschwister » (« un frère et une sœur » précise les sexes ; l'arabe n'a pas de mot neutre).

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
