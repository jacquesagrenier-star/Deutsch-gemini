# L'allemand enseigné en espagnol : consignes de traduction (15 nov. 2026)

Wortando enseigne l'**allemand**. Jusqu'ici, ses explications existaient en neuf langues
(français, anglais, turc, ukrainien, persan, arabe, portugais du Brésil, polonais, russe).
Jacques ajoute l'**espagnol d'Amérique latine** (décision du 15 nov. 2026) : des soignants et
des étudiants du Mexique, de Colombie et d'Amérique du Sud qui apprennent l'allemand pour
travailler en Allemagne. L'apprenant lit des mots et des phrases **allemands** ; tout ce qui
les explique doit être en espagnol.

Les textes à traduire sont dans `interface-es/sources/`. Tu écris tes traductions dans
`interface-es/lots/`. Tu ne touches à **aucun autre fichier**.

## Interdits (absolus)

- **Pas de `git commit`, pas de `git push`**, aucune commande git qui écrit
  (`add`, `stash`, `reset`, `checkout`, `switch`…). `git diff` / `git status` en lecture : oui.
- **Pas d'API payante**, pas d'appel réseau, pas de service de traduction : c'est toi qui traduis.
- **Pas d'autre agent** : ne lance aucun sous-agent ni aucune session.
- **Jamais de script Python par heredoc dans Git Bash** (il mange les antislashs). Si tu as
  besoin d'un script, écris-le avec l'outil Write dans ton dossier scratchpad, puis lance-le.
- N'écris que dans `interface-es/lots/`. Ne lance jamais `corpus_lots.py pose` (seul
  `corpus_lots.py controle` t'est permis).
- Sous Windows, lance Python avec `PYTHONIOENCODING=utf-8`.

## L'espagnol voulu : Amérique latine, neutre

- **Tutoiement** dans les consignes et les explications (« tú », « Elige », « Escribe »).
- **Jamais « vosotros »** (ni *vuestro*, *os*, *sois*, *habláis*), **jamais le voseo** (*vos tenés*).
  Le contrôle refuse ces formes.
- Les pronoms allemands se rendent ainsi : **du → tú**, **Sie → usted** (ou *ustedes* au
  pluriel), **ihr → ustedes**. Une phrase allemande qui dit *ihr* devient *ustedes* ; c'est
  normal, l'Amérique latine n'a pas d'autre forme.
- **Le vocabulaire commun du Mexique et de la Colombie**, compris partout en Amérique :
  el celular, la computadora, el carro, manejar, el jugo, la papa, los frijoles, el durazno,
  la fresa, el boleto, rentar, el apartamento, la cuadra, la recámara / el dormitorio (préfère
  *el dormitorio*), el refrigerador, la estufa, la regadera (ducha : préfère *la ducha*),
  el bolígrafo, la cuenta (au restaurant), tomar (le bus, un café), el autobús.
  Pas de mots propres à l'Espagne (*coche, ordenador, móvil, zumo, patata, piso, coger*).
  Un mot d'Espagne que l'Amérique dit autrement, et dont tu doutes : écris la forme
  américaine et note la carte dans la section « À trancher » de ton rapport.
- **Les noms de lieux** : l'exonyme espagnol quand il est courant (*Berlín, Múnich, Colonia,
  Viena, Suiza, Alemania, el Rin*) ; sinon le nom allemand (*Leipzig, Potsdam*).
- **Les sommes en euros restent en euros**, avec les chiffres de la source (« 3,90 € »).
- Ponctuation espagnole : **¿…?** et **¡…!** ; guillemets **«…»** autour d'un mot cité.

## Les cartes (`sources/corpus-<fichier>-<niveau>-NN.json`)

Chaque entrée porte : `n` (le numéro de la carte, à recopier), `mot` (le mot allemand, à
recopier tel quel), `genre` / `pluriel` pour un nom, `contexte` (le thème), `fr` et `en` (ses
traductions française et anglaise), `champs` (ce qu'il faut rendre, dans l'ordre), puis pour
chaque phrase `[allemand, français, anglais]`, et parfois `pistes` : des mots espagnols de
**notre** corpus d'espagnol (appris) dont la traduction allemande est ce mot. Les pistes sont
des **aides** : elles peuvent être d'Espagne (adapte-les à l'Amérique latine), ou viser un
**homographe** (la piste de *sein* « être » est *su*, « son » : à ignorer).

### Ce que tu rends

`lots/corpus-<fichier>-<niveau>-NN.es.json` (même nom que la source, avec `.es`) :

```json
{"fichier": "themes.json",
 "e": {"3": ["Schwester", "la hermana", "Mi hermana vive en Berlín."],
       "0": ["sein", "ser, estar", "Soy estudiante.", "He sido estudiante.", "Yo era maestro.", "Me gustaría ser maestro."]}}
```

Une ligne par carte de la source, **toutes**, clé = `n` en texte ; la liste commence par
`mot` recopié, puis une valeur par élément de `champs`, dans l'ordre :

- `traduction` — le **sens** du mot allemand, dans le sens de **son thème** (*die Bank* est un
  banc dans « Le parc », une banque dans « L'argent ») :
  - un **nom** avec son article : *el padre*, *la hermana* ; un nom allemand qui n'existe
    qu'au pluriel avec l'article pluriel (*die Eltern* → *los padres*) ;
  - un **verbe** à l'infinitif ; un verbe pronominal allemand (*sich waschen*) en pronominal
    espagnol (*lavarse*) quand l'espagnol l'est aussi ;
  - un **adjectif** au masculin singulier (*cansado*) ;
  - deux sens, séparés par « , » comme dans le français (*ser, estar*) ;
  - **deux cartes d'un même thème ne reçoivent pas la même réponse** quand leurs mots allemands
    diffèrent : choisis le mot qui distingue, ou ajoute une précision courte entre parenthèses
    (*el pasillo*, *el corredor (en un edificio)*). Mais **ne prends jamais un mot rare ou
    faux pour éviter un doublon** : si l'espagnol n'a vraiment qu'un mot (*öffnen / aufmachen*
    → *abrir*), garde-le et note la paire dans ton rapport.
- `exemple`, `perfekt`, `praeteritum`, `konjunktiv2` — la traduction de **la phrase
  allemande** (le français et l'anglais ne sont que des aides ; s'ils s'écartent de
  l'allemand, suis l'allemand). Espagnol naturel, fidèle, court comme la source :
  - **Perfekt** → en Amérique latine, le **pretérito** (*Ayer comí pizza*) pour un fait
    passé et fini ; le *pretérito perfecto* (*He comido*) seulement quand le sens touche le
    présent (*Ya he comido*, *Nunca he estado en Berlín*) ;
  - **Präteritum** → pretérito ou imperfecto selon le sens (*Ich war müde* → *Estaba cansado*) ;
  - **Konjunktiv II** → conditionnel (*Me gustaría…*, *Podría…*), ou imperfecto de subjuntivo
    après *si* (*Si tuviera tiempo…*) ;
  - garde le **genre de la personne** de la phrase allemande (*Ich bin Lehrerin* → *Soy
    maestra*) ; *Lehrer* : *maestro* à l'école primaire, *profesor* au lycée et à l'université.
- `kategorie` (mots-outils) — la catégorie traduite (*Präposition (Dativ)* → *preposición
  (dativo)*) ; les termes de grammaire allemands se gardent en allemand quand la source les
  garde (*Dativ*, *Akkusativ*, *Konjunktiv II*).

Écris le JSON avec l'outil **Write** (UTF-8, pas d'échappement \u), puis vérifie :

    PYTHONIOENCODING=utf-8 python interface-es/outils/corpus_lots.py controle interface-es/lots/<ton lot>.es.json

→ **0 FAUTE**. Les « avis » sont à regarder, pas forcément à corriger (une précision allemande
gardée exprès, un mot identique à l'anglais comme *el hotel*).

## Fin

Quand ta part est faite, écris un compte rendu court dans
`interface-es/lots/RAPPORT-<ta-part>.md` : ce qui est fait (chiffres), ce dont tu doutes
(liste précise de numéros), toute **source fautive** (une phrase française ou anglaise qui ne
dit pas ce que dit l'allemand, une faute dans l'allemand), les **doublons acceptés** (avec la
raison) et la section **« À trancher »** (cartes où l'Amérique latine elle-même hésite, ou
qu'un soignant devrait relire).

---

## Les exercices (`sources/exos-NN.json`)

Chaque entrée est un exercice de grammaire allemande : `id` (« jeu#rang », à recopier),
`_question` (la question telle qu'elle est dans l'app, **à recopier à l'identique** : elle sert de
clé de contrôle), `topic`, `reponse` (la bonne réponse allemande), `champs` (ce qu'il faut rendre),
puis pour chaque champ `{fr, en}` :

- `translation` — la traduction espagnole de la **phrase allemande complète** (la question avec la
  bonne réponse à la place du trou) ; le français n'est qu'une aide ;
- `hint` — l'indice : traduis ce qui est en français ; ce qui est allemand reste allemand
  (« (lernen, Perfekt) » → « (lernen, Perfekt) » ; « (au passé) » → « (en pasado) ») ;
- `explanation` — l'explication, **réécrite pour un hispanophone** quand elle compare au français
  (même règle que les fiches : retire « comme en français », mets l'espagnol quand il aide ; un
  piège qui n'existe pas en espagnol n'est pas annoncé comme un piège). Courte comme la source.
  Les formes allemandes citées restent allemandes ;
- `question` — une consigne française (« Remets les mots dans le bon ordre : ») à traduire
  (« Ordena las palabras: ») ;
- `correct`, `options` — quand elles sont en français (des sens à choisir), traduis-les ; une liste
  garde **le même nombre d'éléments, dans le même ordre** ; si `correct` est traduit, il doit être
  **exactement** l'un des `options` traduits.

### Ce que tu rends

`lots/exos-NN.es.json` :

```json
{"exercises#0": {"_question": "Ich ___ jeden Tag Deutsch.",
                 "translation": "Estudio alemán todos los días.",
                 "explanation": "Con «ich», el verbo regular «lernen» toma la terminación -e: ich lerne."}}
```

Toutes les entrées de la source, chacune avec `_question` recopiée et **exactement** les champs de
`champs`. Contrôle :

    PYTHONIOENCODING=utf-8 python interface-es/outils/exos.py controle interface-es/lots/exos-NN.es.json

→ 0 FAUTE. Jamais `exos.py pose` ni `exos.py extraire`.
