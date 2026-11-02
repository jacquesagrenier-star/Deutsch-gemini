# L'anglais enseigné en espagnol : consignes de traduction (2 nov. 2026)

Wortando enseigne l'anglais à des francophones. Jacques l'ouvre maintenant aux
**hispanophones** (demande du 2 nov. 2026) : l'interface est en espagnol, l'apprenant
lit des mots et des phrases **anglais**, et tout ce qui les explique doit être en espagnol.

Les textes à traduire sont dans `anglais/es/sources/`. Tu écris tes traductions dans
`anglais/es/lots/`. Tu ne touches à **aucun autre fichier**.

## Interdits (absolus)

- **Pas de `git commit`, pas de `git push`**, aucune commande git qui écrit
  (`add`, `stash`, `reset`, `checkout`, `switch`…). `git diff` / `git status` en lecture : oui.
- **Pas d'API payante**, pas d'appel réseau, pas de service de traduction : c'est toi qui traduis.
- **Pas d'autre agent** : ne lance aucun sous-agent ni aucune session.
- **Jamais de script Python par heredoc dans Git Bash** (il mange les antislashs). Si tu as
  besoin d'un script, écris-le avec l'outil Write dans ton dossier scratchpad, puis lance-le.
- N'écris que dans `anglais/es/lots/`. Ne lance jamais `poser_autres.py pose` (seul
  `poser_autres.py controle` t'est permis).
- Sous Windows, lance Python avec `PYTHONIOENCODING=utf-8`.

## L'espagnol voulu : neutre, en attendant le choix de Jacques

Jacques n'a pas encore choisi entre l'espagnol d'Amérique latine et celui d'Espagne.
Écris donc un **espagnol neutre**, que les deux lisent sans accroc :

- **Tutoiement** (« tú », impératif « Toca », « Elige », « Escribe »), comme le reste de l'app ;
  jamais « usted » pour l'usager. **Jamais « vosotros »** ni le **voseo** (« vos tenés »).
  Au pluriel (rare), « ustedes ».
- **Pas de régionalismes** : choisis le mot commun aux deux (« el teléfono », pas « el celular »
  ni « el móvil » ; « la pantalla », « el dispositivo »). Quand aucun mot commun n'existe,
  écris la forme d'Amérique latine **et note l'id** dans ton rapport, section « À trancher »
  (ex. : `computadora / ordenador`, `jugo / zumo`, `carro / coche`, `manejar / conducir`).
  Note aussi tout nombre décimal (3,90 € : virgule en Espagne, point au Mexique).
- Ton simple et chaleureux, celui d'une bonne app pour adultes. Phrases courtes.
- **Pas de genre supposé pour l'usager** : pas de « bienvenido », « listo », « seguro »,
  « cansado » qui le visent ; écris « Te damos la bienvenida », « ¿Todo listo? », « Hola ».
  « Principiante », « estudiante » sont épicènes : permis.
- Ponctuation espagnole : **¿…?** et **¡…!**, guillemets **«…»** autour d'un mot cité.
- Majuscules : seulement au premier mot d'un titre (« Mi práctica de hoy », pas
  « Mi Práctica De Hoy ») ; jours, mois, langues en minuscules (« inglés », « lunes »).

## Ce qui ne bouge pas

- **Les mots et phrases anglais restent en anglais**, exactement comme dans la source :
  `big · bigger · the biggest`, `<b>do / does</b>`, *She works in Boston.*
- **Les balises HTML et les marques restent intactes** : `<b>`, `<em>`, `<strong>`, `<br>`,
  `{n}`, `{x}`, `{titre}`, `%s`, emojis, `⚠️`, ` · `, `→`. Même nombre de balises que la
  source, bien fermées. Ne traduis jamais un nom de marque (`{n}`), ni « Wortando ».
- Les noms de niveau **A1, A2, B1, B2, C1** restent tels quels.

## Les langues nommées dans les textes

- L'interface espagnole ne sert **que quand on apprend l'anglais**. Mais le dictionnaire
  `i18n` est celui de toute l'app : beaucoup de ses textes parlent d'apprendre
  « l'allemand ». **Traduis-les tels quels** (« el alemán ») : quand on apprend l'anglais,
  ils sont remplacés par `surcharge-en` ou ne s'affichent pas.
- La langue **connue** de l'usager devient l'espagnol : « en allemand ou en français » →
  « en alemán o en español » ; « Sens : FR → EN » → « Sentido: ES → EN » ; « la traduction
  française » → « la traducción al español ». Un texte qui dit « en français » au sens
  de « dans ta langue » devient « en español ».
- Quand le texte parle du **français comme langue d'interface parmi d'autres** (liste des
  langues, « Français »), garde « francés ».

## Glossaire de l'interface (le même pour tous)

| français | espagnol |
|---|---|
| la séance (du jour) | la práctica ; « Ma séance du jour » → «Mi práctica de hoy» ; « Commencer la séance » → «Empezar la práctica» (« sesión » est réservé à « Iniciar sesión ») |
| la carte | la tarjeta |
| Mettre de côté / Mis de côté | «Apartar» / «Apartadas» |
| Encore / Continuer / Je savais | «Otra vez» / «Continuar» / «Lo sabía» |
| Premiers pas | «Primeros pasos» |
| la scène / Explorer les scènes | la escena / «Explorar las escenas» |
| Écouter, répéter | «Escuchar, repetir» |
| le tableau (de la mosaïque) / la galerie / la mosaïque | el cuadro / la galería / el mosaico |
| Réglages | Ajustes |
| le niveau (A1…C1) / Débutant | el nivel / «Principiante» |
| Thèmes, Mots, Vocabulaire | Temas, Palabras, Vocabulario |
| Noms, Verbes, Adjectifs, Adverbes, Expressions, Mots-outils | Sustantivos, Verbos, Adjetivos, Adverbios, Expresiones, Palabras funcionales |
| Grammaire / une fiche (de grammaire) | Gramática / una ficha |
| un exercice / M'entraîner / une série | un ejercicio / «Practicar» / una serie |
| Écrire / la dictée | Escribir / el dictado |
| maîtrisé / en cours | dominada(s) / en progreso (accord avec « palabra(s) ») |
| la série de jours (flamme) | la racha |
| l'objectif du jour | la meta del día |
| Tout le contenu | «Todo el contenido» |
| Mes épisodes | «Mis episodios» |
| Signaler un problème ou une idée | «Enviar un problema o una idea» |
| Se connecter / Se déconnecter / Créer un compte / mot de passe | «Iniciar sesión» / «Cerrar sesión» / «Crear una cuenta» / la contraseña |
| code d'invitation | el código de invitación |
| l'abonnement / l'essai gratuit | la suscripción / la prueba gratis |
| la prononciation / la voix | la pronunciación / la voz |
| les repères (nombres, jours, mois) | «Lo básico» |
| l'article (der/die/das, a/an/the) | el artículo |
| les temps (présent, passé…) | los tiempos verbales ; noms anglais des temps gardés (*present simple*, *past simple*, *present perfect*) |
| l'Espagne / l'Amérique latine / les États-Unis / le Royaume-Uni | España / Latinoamérica / Estados Unidos / el Reino Unido |
| anglais américain / britannique | inglés estadounidense / británico |

## Formats

### Autres textes (`sources/<nom>.json`) → `lots/<nom>.es.json`

Chaque source est une liste `{"id", "fr", "en"}` (`en` peut être vide). Rends un objet
JSON `{ "<id>": "<texte espagnol>", … }` avec **tous** les id de la source, dans le même
ordre. Un gros fichier se rend en morceaux : `lots/<nom>-01.es.json`, `lots/<nom>-02.es.json`…
(permis pour `i18n`).

- `i18n` : l'interface entière de l'app (1 607 clés). Traduis depuis le français ; l'anglais
  en regard aide à lever un doute (c'est l'interface anglaise de l'allemand appris).
- `surcharge-en` : l'interface propre à l'anglais appris (48 clés). Là où la source dit
  « anglais ou français », écris « inglés o español ».
- Écris le JSON avec l'outil Write (UTF-8, pas d'échappement \u). Vérifie :
  `PYTHONIOENCODING=utf-8 python anglais/es/poser_autres.py controle <nom>` → 0 faute.
  Les « avis » sont à regarder, pas forcément à corriger (« mot francais « est » » dans un
  texte qui cite une phrase française, par exemple).

## Fin

Quand ta part est faite, écris un compte rendu court dans `anglais/es/lots/RAPPORT-<ta-part>.md` :
ce qui est fait (chiffres), ce dont tu doutes (liste précise d'id), toute source qui te semblait
fautive, et la section **« À trancher »** (ids où l'Espagne et l'Amérique latine diffèrent,
avec les deux formes).

---

# Palier 2 : le contenu (2 nov. 2026)

**Décision de Jacques (2 nov.) : deux espagnols.** L'**Amérique latine** est la base (le
défaut) : c'est elle que tu écris partout. L'**Espagne** n'est qu'une table de différences :
pour une **carte** dont le mot ou la phrase se dit autrement en Espagne (el carro / el coche,
la computadora / el ordenador, el celular / el móvil, el jugo / el zumo, manejar / conducir,
la cuadra / la manzana, el departamento / el piso, rentar / alquilar, la papa / la patata,
el boleto / el billete, ustedes / vosotros dans une phrase qui s'adresse à plusieurs), tu
donnes aussi la forme d'Espagne (format ci-dessous). Les textes longs (fiches, explications)
s'écrivent en espagnol **neutre**, sans régionalisme : ils servent aux deux.

## Écrire CONTRE l'espagnol (pas traduire le français)

Les explications françaises comparent l'anglais au français (« comme en français »,
« contrairement au français »). **Réécris-les pour un hispanophone** : retire la comparaison
avec le français ; ajoute celle avec l'espagnol quand elle aide vraiment. Une comparaison
fausse est pire que pas de comparaison. Les pièges d'un hispanophone :

- **le sujet obligatoire** : *It's raining*, *It is important* (*Llueve*, *Es importante*) —
  erreur n° 1 : « Is raining » ; *there is / there are* = *hay* ;
- **l'adjectif avant le nom, invariable** : *a red car*, *two red cars* (jamais « reds ») ;
- **do / does / did** pour la question et la négation (*¿Hablas inglés?* = *Do you speak
  English?*, *No trabaja* = *She doesn't work*) ; le **-s** de la 3ᵉ personne ;
- **to be** pour l'âge et les sensations : *I'm 20*, *I'm hungry* (*tengo 20 años, tengo
  hambre*) ; un seul *to be* pour *ser* et *estar* ;
- le **possessif selon le possesseur** : *his / her* (*su* ne le dit pas) ;
- **pas d'article pour les généralités** : *Dogs are loyal*, *I like music* ;
- **like ≠ gustar** : *I like dogs* (la personne est le sujet ; *me gustan los perros*) ;
- **present perfect** ≠ *pretérito perfecto* dans l'usage ; *for / since* ≠ *desde hace / desde* ;
  *I've lived here for ten years* = *Vivo aquí desde hace diez años* ;
- **faux amis** : *actually* (en realidad), *embarrassed* (avergonzado ≠ embarazada),
  *library* (biblioteca ≠ librería), *carpet* (alfombra), *exit* (salida ≠ éxito), *realize*
  (darse cuenta), *assist* (ayudar), *attend* (asistir), *sensible* (sensato), *large* (grande),
  *argument* (discusión), *fabric* (tela), *constipated* (estreñido). Un faux ami **français**
  de la source qui ne trompe pas un hispanophone : remplace-le par le piège espagnol s'il
  existe, sinon dis simplement le sens.

## La prononciation, expliquée à un hispanophone

Les transcriptions « à la française » de la source (« ZI-rô », « OUANN », « gôou ») ne valent
rien pour un hispanophone : **refais-les avec l'orthographe espagnole** (*zero* « SÍ-rou »,
*one* « UAN », *two* « TU », *five* « FAIV », *go* « GÓU ») ; une lettre que l'espagnol n'a pas
se garde entre crochets API ([θ], [ð], [ʃ], [z], [v], [ʌ], [ə]). Repères :
- voyelles **longues et courtes** (*ship / sheep*, *full / fool*) : l'espagnol n'en a qu'une ;
- le **e ajouté** devant s + consonne : *speak*, pas « espeak » ; *school*, pas « escul » ;
- **v ≠ b** : *very*, la lèvre du bas sur les dents ; *b* les deux lèvres ;
- **h aspiré**, léger, plus doux que la *j* espagnole ; jamais muet (*house*, *happy*) ;
- **th** : [θ] comme la *z* d'Espagne (*think*) ; [ð] sonore (*the*) — en Amérique latine, pas
  d'équivalent : la langue entre les dents ;
- **z** et le **s** sonore de *is*, *roses* : une abeille, la gorge vibre ;
- **sh** [ʃ] (*she*) ≠ **ch** (*cheese*) ; **j** = [dʒ] (*job*), jamais la *j* de *jamón* ;
- le **r** américain ne roule pas : la langue recule, ne touche rien ;
- finales **-ed** ([t], [d], [ɪd]) et **-s** ([s], [z], [ɪz]) ; le **schwa** et l'accent tonique.

## Formats

### Cartes → `lots/corpus-<fichier>-NN.es.json`

Sources : `sources/a1-corpus-<fichier>.json` (entrées `id`, `mot`, `fr` = le sens français,
`ex` = la phrase anglaise, `ex_fr` = sa traduction, parfois `es_existant` = une phrase de
NOTRE corpus espagnol dont la phrase anglaise est la traduction : reprends-la si elle est
juste et neutre, adapte-la sinon). Rends `{id: [traduction, phrase]}`, ou
`{id: [traduction, phrase, traduction d'Espagne, phrase d'Espagne]}` quand l'Espagne dit
autrement (une colonne d'Espagne vide = comme l'Amérique latine).
- `traduction` : le sens espagnol du mot anglais ; un **nom** avec son article (*el perro*,
  *la casa*) ; un **verbe** à l'infinitif (*trabajar*) ; un **adjectif** au masculin
  (*cansado*). Deux sens : séparés par « , » comme le français.
- `phrase` : la traduction **de la phrase anglaise** (le français n'est qu'une aide).
- **Deux cartes d'un même groupe ne reçoivent pas la même traduction** quand leurs mots anglais
  diffèrent : départage par une précision entre parenthèses (*grande (big)* …) ou un synonyme.
- Contrôle : `PYTHONIOENCODING=utf-8 python anglais/es/poser.py controle <fichier>` → 0 faute.

### Textes → `lots/textes-NN.es.json`

Source : `sources/a1-textes.json` (`id`, `fr`, `contexte`). Rends `{id: texte espagnol}`, tous
les id, dans l'ordre ; en morceaux de 250 à 400 entrées. Les mots et phrases **anglais** restent
en anglais ; balises et `{marques}` intactes. Contrôle :
`PYTHONIOENCODING=utf-8 python anglais/es/poser_textes.py controle textes` → 0 faute.

### Exercices → `lots/exercices-NN.es.json`

Source : `sources/a1-exercices.json` (`id`, `question` anglaise, `options`, `correct`,
`translation` = la phrase en français, `explanation` = l'explication française). Rends
`{id: [traduction espagnole de la phrase, explication espagnole]}`. L'explication est
**réécrite contre l'espagnol** (voir plus haut), courte comme la source. Contrôle :
`PYTHONIOENCODING=utf-8 python anglais/es/poser_textes.py controle exercices` → 0 faute.

Interdits de la page précédente inchangés : n'écris que dans `anglais/es/lots/`, aucune
commande `pose`, aucun git qui écrit, aucun autre agent, aucun service en ligne.
