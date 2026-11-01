# L'espagnol en anglais : ce qu'un anglophone natif doit relire en priorité

Dressé le 1er nov. 2026 (chantier « finir l'espagnol pour l'anglais, le portugais du Brésil et l'arabe »).
Tout le texte anglais de l'espagnol est présent (aucune clé, aucun champ manquant) ; il a été écrit par
des modèles et relu par d'autres modèles, **jamais par un anglophone**. L'anglais est la langue du lancement
« Learn Spanish » : c'est la relecture qui compte le plus.

Le relecteur n'a pas besoin du code : chaque point dit le fichier, la clé et ce qu'il faut regarder. Un
relecteur qui ne lit pas l'espagnol peut faire les points 1, 3 et 5 ; les points 2 et 4 demandent de lire
l'espagnol.

## 1. Les 17 fiches de grammaire (le plus important)

`espanol/datos/grammaire.json`, clé `en` de chaque texte (et `textes.en`, 43 libellés d'écran).
Dans l'app : « All content » → chaque tuile de grammaire → la fiche.

Elles ont été **réécrites contre l'anglais**, pas traduites du français (« A choice English doesn't make »,
« A whole mood English lost ») : vérifier que ces comparaisons sont **justes et naturelles** pour un
anglophone, en particulier :
- `ser-estar`, `por-para` : les règles et les exemples de contraste ;
- `pasados` (pretérito / imperfecto) : la comparaison avec le passé anglais ;
- `subjuntivo` : « a whole mood English lost » — vrai pour le lecteur ?
- `pronombres` : l'ordre « se lo doy » comparé à l'anglais ;
- `genero` : « English gives you nothing to go on » ;
- le ton : tutoiement implicite, phrases courtes ; repérer tout calque du français (« the polite you »).

**Corrigé le 1er nov.** : la première colonne de 19 lignes de tableaux était en français dans toutes les
langues (« vosotros (Espagne) », « tú (négatif) », « l'heure », « concéder »). Elle est traduite
(`espanol/ar/colonne_fiches.py`) : « vosotros (Spain) », « tú (negative) », « the time », « conceding »…
À relire avec le reste.

## 2. Les exercices de pièges, à relire pour un anglophone

`espanol/datos/ejercicios.json`, champs `hint_en`, `explanation_en`, `translation_en`.

**a. Les faux amis (`falsosAmigosExercises`, 52 questions).** L'indice dit à tous « the word that looks
familiar is often the trap ». Une partie des pièges a été écrite pour l'anglais (carpeta/carpet,
largo/large, éxito/exit, actual/actual, conservantes/preservatives, emocionado/excited) ; **une dizaine
restent des pièges de francophone**, qui ne trompent pas un anglophone :

| question (réponse) | le piège visé | pour un anglophone |
|---|---|---|
| Me duele la ___ derecha. (pierna) | gamba ≈ fr. *jambe* | gamba ne ressemble à rien |
| Pon el ___ en la mesa… (mantel) / Hace frío: ponte el ___ (abrigo) | mantel ≈ fr. *manteau* | idem |
| Viven en una ___ con vacas… (granja) | firma ≈ fr. *ferme* | idem |
| La empresa ___ grandes pérdidas. (sufrió) | subir ≈ fr. *subir* | idem |
| ___ al tercer piso… (Subí) | montar ≈ fr. *monter* | idem |
| No te ___: habla más alto. (oigo) | entender ≈ fr. *entendre* | idem |
| En enero hay ___ en todas las tiendas. (rebajas) | sueldo ≈ fr. *soldes* | idem |
| Mi padre cobra la ___ desde 2020. (jubilación) | retirada ≈ fr. *retraite* | à moitié (*retirement*) |
| La empresa lo ___… (despidió) | reenviar ≈ fr. *renvoyer* | idem |
| Hay ___ de Picasso en el salón. (un cuadro) | tabla ≈ fr. *tableau* | à moitié (*table*) |
| Mis ___ viven en Lyon… (padres) | parientes ≈ fr. *parents* | **vrai piège aussi** (*parents*) |

Décision à prendre (Jacques) : garder ces questions comme vocabulaire en retirant le mot « trap » de leur
explication anglaise, ou les remplacer par des faux amis anglais. Déjà présents : embarazada, constipado,
librería/library, carpeta/carpet, largo/large, éxito/exit, actual, conservantes, emocionado, fábrica/fabric,
lectura/lecture, introducir, registrar. Candidats à ajouter : sensible, molestar, asistir, realizar,
recordar, ropa/rope, colegio/college, disgusto/disgust.

**b. Corrigé le 1er nov.** : trois explications de prépositions disaient « French says « en bois » »,
« « à qui » », « « en coton » » (source `fusion-espagnol/exos_fiches.py`, recopiée dans `ejercicios.json`).
Réécrites : « Material: de, as in “made of wood” », « ¿de quién? = whose? (literally “of whom?”) ».

**c. À relire en entier, dans cet ordre** (les explications font la leçon) : `serEstarExercises` (51),
`porParaExercises` (50), `gustarExercises` (57, écrit à partir du mot à mot « chocolate PLEASES ME »),
`subjuntivoImperfectoExercises` (51), `oracionesSiExercises` (50), `pasivaExercises` (51),
`perifrasisExercises` (51), `preposicionesExercises` (51), `verbosConPreposicionExercises` (50).

## 3. L'interface propre à l'espagnol

`index.html`, bloc `I18N_ESPAGNOL.en` (142 clés). Les libellés de tuiles, les écrans de séance, l'abonnement.
- **Corrigé le 1er nov.** : l'écran d'abonnement de l'espagnol annonçait « 7,700 words from A1 to C1 » et
  « Exam preparation for A2, B1 and DTZ » (les chiffres et les examens de l'allemand). Il dit maintenant
  « 3,700 words from A1 to B2 » et « A Spain or Latin American accent ».
- **Corrigé le 1er nov.** : « Good morning ! » (espace française avant « ! ») dans toutes les langues sauf
  le français.
- **Américain ou britannique ?** Les données de l'espagnol sont en anglais **britannique** (comptés le
  1er nov. dans `espanol/datos/` : flat 32, neighbour 17, trousers 11, colour 11, the bill 12, organised 2 ;
  américain : apartment 1, meter 2, aucun « neighbor », « color », « pants », « check »). La fiche magasin
  vise l'en-US, et l'anglais appris dans l'app a choisi l'américain (27 oct.). À trancher par Jacques :
  garder le britannique (cohérent, compris partout) ou tout passer à l'américain (≈ 100 mots à changer).

Corrigé aussi le 1er nov., pour toutes les langues autres que fr/en (et l'allemand en profite) : les
écrans « Write » et « Build the sentence » montraient la phrase anglaise à un usager en portugais ou en
arabe (`phrasesTraduisibles()` ne portait que fr et en).

## 4. Premiers pas et les escales A1

`espanol/datos/premiers-pas.json` et `a1-voyage.json`, clé `en`.
- ⚠️ Premiers pas enseigne « ¿Habla francés? » (« Do you speak French? ») et en fait une phrase à
  reconstruire, avec « ¿Habla inglés? » comme leurre. Pour un anglophone, c'est l'inverse qui sert.
  Le format n'a qu'une phrase espagnole pour toutes les langues : changer la phrase change aussi le
  parcours français. À trancher par Jacques (« ¿Habla inglés? » pour tous serait utile aux deux publics).
- Relire les sens anglais des cartes de voyage (registre : « the bill » ou « the check » ?).

## 5. Les nombres prononcés (nouveau, 1er nov.)

`tests/reperes_suite.py`, `PRONONCIATION_NOMBRES_ES_EN` → `espanol/datos/reperes.json` (repères de la
séance, A1). La prononciation figurée sous chaque nombre n'existait qu'en français ; l'anglaise est neuve :
« θEH-roh » (affiché THEH-roh en Espagne, SEH-roh en Amérique latine), « KWAH-troh », « SAYS » (seis),
« BAYN-teh » (veinte). Vérifier qu'un anglophone lit bien ces syllabes (eh, ay, oh, oo, ee), la syllabe forte
en capitales.

## 6. Ce qui n'est pas à relire ici

- Le vocabulaire (3 700 mots, `traduction_en`, `exemple_en`) : vient des dictionnaires et des relectures
  déjà faites ; une relecture par échantillon (50 mots tirés au hasard) suffit.
- Les scènes (`visuel/prototype/espanol/*.json`, `n_en`) : vérifiées à l'écran le 1er nov. sur la cuisine,
  A1 à C1.
