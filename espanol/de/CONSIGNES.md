# L'espagnol enseigné en allemand : consignes de traduction (1er nov. 2026)

Wortando enseigne l'espagnol à des francophones, des anglophones, des lusophones et
des arabophones. Jacques l'ouvre maintenant aux **germanophones** (décision du 1er nov.
2026) : l'interface est en allemand, l'apprenant lit des mots et des phrases
**espagnols**, et tout ce qui les explique doit être en allemand.

Les textes à traduire sont dans `espanol/de/sources/` (et, pour le corpus et les
exercices, sortis par `python espanol/de/poser.py reste …`). Tu écris tes traductions
dans `espanol/de/lots/`. Tu ne touches à **aucun autre fichier**.

## Interdits (absolus)

- **Pas de `git commit`, pas de `git push`**, aucune commande git qui écrit
  (`add`, `stash`, `reset`, `checkout`, `switch`…). `git diff` / `git status` en lecture : oui.
- **Pas d'API payante**, pas d'appel réseau, pas de service de traduction : c'est toi qui traduis.
- **Pas d'autre agent** : ne lance aucun sous-agent ni aucune session.
- **Jamais de script Python par heredoc dans Git Bash** (il mange les antislashs). Si tu as
  besoin d'un script, écris-le avec l'outil Write dans ton dossier scratchpad, puis lance-le.
- N'écris que dans `espanol/de/lots/`. Ne lance jamais `poser.py pose` sans `--essai`,
  ni `poser_autres.py pose` (seul `poser_autres.py controle` t'est permis).
- Sous Windows, lance Python avec `PYTHONIOENCODING=utf-8` (sinon l'affichage plante sur « → »).

## L'allemand voulu

- **Hochdeutsch d'Allemagne**, orthographe réformée (dass, ß), simple et chaleureux, celui
  d'une bonne app pour adultes. **Tutoiement** (« du », « dein », impératif « Tippe », « Wähle »),
  comme le reste de l'app ; jamais « Sie » pour s'adresser à l'usager.
- **Pas de genre supposé pour l'usager** : évite « Anfänger », « Lerner », « Nutzer » quand une
  tournure neutre existe (« für den Einstieg », « wer Spanisch lernt », « dein Konto »).
- Guillemets allemands **„…“** autour d'un mot cité dans une phrase allemande ; garde les
  guillemets tels qu'ils sont dans une balise ou une cellule de tableau espagnole.
  Nombres : virgule décimale (3,90 €), espace insécable avant € et % comme en allemand.
- **Les mots et phrases espagnols restent en espagnol**, exactement comme dans la source,
  avec leurs accents, ¿ et ¡ : `«estar»` devient `„estar“`, `<b>al lado de</b>` reste tel quel.
- **Les balises HTML et les marques restent intactes** : `<b>`, `<em>`, `<strong>`, `<br>`,
  `{n}`, `{x}`, `{titre}`, `%s`, emojis, `⚠️`, ` · `, `→`. Même nombre de balises que la
  source, bien fermées. Ne traduis jamais un nom de marque (`{n}`) ni un nom de clé.
- Un texte qui n'est fait que d'espagnol (« (vivir) », « (comer — yo) », « Con tener — tener
  ganas ») garde sa partie espagnole ; seule la partie française se traduit.
- Mentions françaises du type « présent, je » → « Präsens, ich ». Personnes : yo = ich,
  tú = du, él/ella = er/sie, usted = Sie, nosotros = wir, vosotros = ihr, ellos/ellas = sie,
  ustedes = Sie (Plural) / ihr (Lateinamerika).
- Noms des temps espagnols : garde les noms espagnols, comme les manuels allemands
  (Klett, Cornelsen) : *presente*, *pretérito indefinido*, *imperfecto*, *pretérito perfecto*,
  *futuro*, *condicional*, *subjuntivo*, *imperativo*, *gerundio*. Pour les temps allemands
  cités en contraste : Präsens, Präteritum, Perfekt, Konjunktiv II.
- Les **traductions de phrases** espagnoles se font **depuis l'espagnol** (le français n'est
  qu'une aide pour lever un doute) : allemand naturel, même registre, mêmes prénoms.
- Un nom traduit porte son article allemand : `casa` → `das Haus`, `mesa` → `der Tisch`
  (comme le français dit « la maison »). Un verbe se traduit par l'infinitif (`sprechen`),
  un adjectif par sa forme de base (`groß`).

## Glossaire de l'interface (le même pour tous les traducteurs)

| français | allemand |
|---|---|
| la séance (du jour) | die Lerneinheit ; « Ma séance du jour » → „Meine Lerneinheit heute“ ; « Commencer la séance » → „Lerneinheit starten“ |
| la carte | die Karte |
| Mettre de côté / Mis de côté | „Zurücklegen“ / „Zurückgelegt“ |
| Encore / Continuer / Je savais | „Nochmal“ / „Weiter“ / „Gewusst“ |
| Premiers pas | „Erste Schritte“ |
| la scène / Explorer les scènes | die Szene / „Szenen entdecken“ |
| Écouter, répéter | „Hören, nachsprechen“ |
| le tableau (de la mosaïque) / la galerie | das Gemälde / die Galerie (la mosaïque : das Mosaik) |
| Réglages | Einstellungen |
| le niveau (A1…C1) / Débutant | das Niveau / „Einstieg“ |
| Thèmes, Mots, Vocabulaire | Themen, Wörter, Wortschatz |
| Noms, Verbes, Adjectifs, Adverbes, Expressions | Nomen, Verben, Adjektive, Adverbien, Redewendungen |
| Grammaire / une fiche (de grammaire) | Grammatik / eine Übersicht |
| un exercice / M'entraîner | eine Übung / „Üben“ |
| Écrire / la dictée | Schreiben / das Diktat |
| maîtrisé / en cours | sicher / im Lernen |
| la série de jours (flamme) | die Serie |
| l'objectif du jour | das Tagesziel |
| Tout le contenu | „Alle Inhalte“ |
| Mes épisodes | „Meine Folgen“ |
| Signaler un problème ou une idée | „Problem oder Idee melden“ |
| Se connecter / Créer un compte / mot de passe | „Anmelden“ / „Konto erstellen“ / Passwort |
| code d'invitation | Einladungscode |
| l'abonnement / l'essai gratuit | das Abo / die kostenlose Testphase |
| l'Espagne / l'Amérique latine | Spanien / Lateinamerika |

## Écrire CONTRE l'allemand (pas traduire le français mot à mot)

La source française explique l'espagnol à un francophone (« comme en français… »,
« contrairement au français… »). **Réécris pour un germanophone** : retire les comparaisons
avec le français, et ajoute la comparaison avec l'allemand quand elle aide vraiment. Une
comparaison fausse est pire que pas de comparaison. Repères :

- **Genre** : deux genres (el / la), pas de neutre, et ils ne coïncident pas avec l'allemand :
  el sol / die Sonne, la luna / der Mond, el coche / das Auto, la leche / die Milch,
  el problema (masculin malgré le -a). **Pas de déclinaison** : el / la / los / las ne changent
  jamais selon le cas (pas de der/den/dem) — un vrai soulagement à dire.
- **Adjectif** : en général APRÈS le nom (una casa blanca), et il s'accorde **aussi en
  attribut** : la casa es blanca / las casas son blancas, alors que l'allemand dit
  „das Haus ist weiß“ sans terminaison.
- **ser / estar** : l'allemand n'a que „sein“. Explique par le sens (identité, nature,
  origine, profession → ser ; lieu, état passager, résultat → estar).
- **Pronom sujet** : la terminaison suffit, le pronom tombe (hablo = „ich spreche“).
  L'allemand, lui, l'exige toujours : c'est une différence à nommer.
- **usted / ustedes** : comme „Sie“, mais le verbe est à la **3e personne du singulier**
  (¿Usted habla español? = „Sprechen Sie Spanisch?“) ; ustedes = Plural (3e pers. du pluriel).
  vosotros ≈ „ihr“ (Espagne seulement).
- **Ordre des mots** : pas de verbe en deuxième position obligatoire, pas de verbe rejeté à
  la fin de la subordonnée : porque no tengo tiempo = „weil ich keine Zeit habe“.
- **Négation** : no avant le verbe ; double négation obligatoire (No veo nada = „Ich sehe
  nichts“, pas de « nicht nichts » en allemand).
- **Passés** : *indefinido* (action terminée, un point dans le passé) contre *imperfecto*
  (décor, habitude, ce qui durait : „früher … immer“). Le Präteritum et le Perfekt allemands
  ne départagent PAS ces deux-là : ne les donne pas comme équivalents. Le *pretérito
  perfecto* (he hablado) ressemble au Perfekt („ich habe gesprochen“), mais il se fait
  **toujours avec haber**, même là où l'allemand prend „sein“ : he ido = „ich bin gegangen“ ;
  et en Espagne il marque un passé lié au présent (hoy, esta semana, ya).
- **Subjonctif** : bien plus fréquent que le Konjunktiv ; après quiero que, es importante que,
  ojalá, cuando + futur… là où l'allemand garde l'indicatif („Ich will, dass du kommst“ =
  Quiero que vengas).
- **gustar** : l'allemand fait comme l'espagnol avec „gefallen“ et „schmecken“ ! me gusta el
  libro = „mir gefällt das Buch“, me gustan los libros = „mir gefallen die Bücher“ : la chose
  aimée est le sujet, le verbe s'accorde avec elle. Le mot à mot de la source (« le chocolat
  ME PLAÎT ») devient „die Schokolade schmeckt MIR“ / „gefällt MIR“.
- **a personnel** : veo **a** María (complément d'objet humain) — rien de tel en allemand.
- **Faux amis** (`falsosAmigosExercises`) : ils sont pensés pour un francophone. Garde le
  piège quand il vaut aussi pour un germanophone, sinon présente-le comme une ressemblance
  trompeuse avec le français ou l'anglais, et donne toujours le vrai sens en allemand.
  Pièges propres aux germanophones, à citer quand ils se présentent : la carta („Brief“,
  pas Karte), el gimnasio (Fitnessstudio, pas Gymnasium), el regalo (Geschenk, pas Regal),
  la taza (Tasse) / la tasa (Gebühr), el mantel (Tischdecke, pas Mantel), bravo (wild,
  mutig — pas brav), la rata (Ratte, pas Rate), el pastel (Kuchen).
- **Prononciation**, écrite contre l'allemand :
  - j (et g devant e, i) = le „ch“ de „Bach“, „lachen“ (ach-Laut) ; plus doux en Amérique latine ;
  - ll et y ≈ le „j“ de „ja“ (plus appuyé en Espagne, „sch“ à Buenos Aires) ;
  - ñ ≈ „nj“ (España ≈ „Espanja“) ; ch = „tsch“ comme dans „Tschüss“ ;
  - **s toujours sourd**, même entre voyelles (casa : pas le „s“ voisé de „Rose“) ;
  - **z, et c devant e/i** : jamais „ts“ comme dans „Zeit“ ! En Espagne, langue entre les dents
    (l'anglais „th“) ; en Amérique latine, un „s“ sourd ;
  - **v = b** : jamais le „w“ allemand (vino ≈ „bino“) ;
  - qu = „k“ (que, queso), **jamais „kw“** comme dans „Quelle“ ; gu + e/i = „g“ (guerra) ;
  - h toujours muet (hola = „ola“) ;
  - r battu d'un coup de langue (comme un „d“ rapide), rr roulé avec la pointe de la langue —
    pas le r guttural allemand ;
  - **sp / st en début de mot** : jamais „schp“ / „scht“ (España, estación) ;
  - voyelles **brèves et pleines**, sans voyelle longue ni réduite ; **ei** = e-i et **eu** = e-u
    (seis, Europa — pas „ai“, „oi“) ; **ie** = i-e (siete), pas le „ie“ long de „Liebe“ ;
    le e final se prononce pleinement (noche).
  Les transcriptions entre « » de la source (pensées pour un francophone, « kassa ») se
  refont pour un lecteur allemand ou se retirent si elles n'aident pas.

## Formats

### Exercices → `lots/ejercicios-NN.txt`

`python espanol/de/poser.py reste ejercicios 100 --depuis K` sort, ligne par ligne :
`jeu¦idx|question|question_en|translation|hint|explanation` (français). Écris, 100 lignes
par fichier au plus, en commençant par `#fichier ejercicios` :

    jeu|idx|debut|translation_de|hint_de|explanation_de|[question_de]

- `jeu|idx` : le `jeu¦idx` de la source avec `|` au lieu de `¦`.
- `debut` : les **20 premiers caractères** de la question espagnole, recopiés tels quels.
- `hint_de` : `=` si l'indice n'est fait que d'espagnol (« (vivir) ») ; sinon sa traduction.
- `question_de` (7e colonne) : **seulement si `question_en` n'est pas vide ET diffère de
  `question`** (la question est formulée dans la langue de l'usager) ; sinon pas de 7e colonne.
- Aucun `|` à l'intérieur d'un texte (remplace-le par « / »).
- Contrôle après chaque lot : `python espanol/de/poser.py pose --essai espanol/de/lots/<lot>.txt`
  doit répondre « N entrees verifiees (essai, rien n'est ecrit) ». Sinon corrige.
  ⚠️ `reste` liste ce qui n'est pas encore POSÉ (rien ne l'est avant la fin) : avance avec
  `--depuis` (le numéro de ligne dans l'ordre du fichier, pas l'idx), sans sauter ni doubler.

### Corpus → `lots/<fichier>-NN.txt` (temas, verbos, adjetivos, adverbios, expresiones, funcionales)

`python espanol/de/poser.py reste temas 100 --depuis K` sort :
`num|mot|genre niveau theme|traduction fr|traduction en|exemple es|exemple fr` (les autres
fichiers n'ont pas la 3e colonne). Lot :

    #fichier temas
    num|mot|traduction_de|exemple_de

`traduction_de` : le mot allemand (avec son article pour un nom ; deux sens séparés par
« , » si le français en donne deux). `exemple_de` : la phrase espagnole traduite.
**Deux cartes d'une même catégorie ne doivent pas recevoir la même réponse allemande**
quand leurs mots espagnols diffèrent (sinon la carte est indécidable) : départage par une
précision entre parenthèses ou un synonyme (« der Rock », « die Jacke »).

### Phrases des temps → `lots/tiempos-NN.txt`

`python espanol/de/poser.py reste tiempos 100 --depuis K` sort
`num|verbe|preterito|imperfecto|perfecto|futuro|condicional|subjuntivo` (phrases espagnoles).
Lot : `#fichier tiempos` puis `num|verbe|<6 phrases allemandes>` dans cet ordre ; une colonne
vide SEULEMENT là où la source est vide. Traduis le temps fidèlement (imperfecto → souvent
„früher … immer“ / Präteritum ; subjuntivo → la tournure allemande naturelle).

### Autres textes (`sources/<nom>.json`) → `lots/<nom>.de.json`

Chaque source est une liste `{"id", "fr", "en", …}`. Rends un objet JSON
`{ "<id>": "<texte allemand>", … }` avec **tous** les id de la source, dans le même ordre.
Un gros fichier se rend en morceaux : `lots/<nom>-01.de.json`, `lots/<nom>-02.de.json`…
(permis pour `i18n`, `scenes`, `premiers-pas`, `a1-voyage`, `reperes`, `conjugaison`).
- `i18n` : l'interface entière de l'app (1 607 clés). Les textes qui parlent d'apprendre
  « l'allemand » se traduisent tels quels („Deutsch“) : quand on apprend l'espagnol, ils sont
  remplacés par `surcharge-es` ou ne s'affichent pas. Garde le glossaire ci-dessus.
- `surcharge-es` : l'interface propre à l'espagnol. Là où la source dit « en espagnol ou en
  français », écris „auf Spanisch oder auf Deutsch“.
- `mots-outils` : la valeur est une liste de trois textes `[traduction, exemple, catégorie]`
  (l'exemple traduit la phrase `exemple_es`).
- `prononciation` : une liste de deux textes `[court, explication]`, écrits contre l'allemand
  (voir plus haut), avec les mots espagnols des exemples.
- `grammaire` : les fiches de grammaire, **les textes les plus importants**. Réécris-les pour
  un germanophone. Les ids `textes|…` sont des titres et paragraphes d'écran ; les
  `fiches/…/titre`, `resume`, `regle`, `tableau`, `exemples` sont dans les fiches. Une cellule
  de tableau faite d'espagnol (« hablo · como · vivo ») se recopie telle quelle.
- `scenes` : les notes « n » sont affichées après une question sur une image (`question` et
  `phrase` sont là pour le contexte, ne les traduis pas) ; `…|titre` est le titre d'une couche ;
  `…|alt` décrit l'image (pour les lecteurs d'écran), `…|consigne` est la consigne affichée.
- `premiers-pas`, `a1-voyage`, `conjugaison`, `reperes` : titres, sens de phrases toutes faites,
  explications des feuilles de conjugaison (écrites contre l'allemand, comme la grammaire).
- `peintres` : notices de peintres (fidèles, sans rien ajouter).
- Écris le JSON avec l'outil Write (UTF-8, pas d'échappement \u). Vérifie :
  `PYTHONIOENCODING=utf-8 python espanol/de/poser_autres.py controle <nom>` → 0 faute.
  (Les « avis » sont à regarder, pas forcément à corriger : « aucun mot-outil allemand »
  sur un titre court est normal.)

## Fin

Quand ta part est faite, écris un compte rendu court dans `espanol/de/lots/RAPPORT-<ta-part>.md` :
ce qui est fait (chiffres), ce dont tu doutes (liste précise d'id), toute source qui te semblait
fautive, et les phrases où tu as écrit une comparaison avec l'allemand (pour la relecture).
