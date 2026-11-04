# Thèmes illustrés : le mode d'emploi du modèle

Le modèle des thèmes illustrés de Wortando, tiré des deux premiers : **« Décrire une personne »** (Descripción
física, `visuel/prototype/descripcion.html`) et **« La famille »** (`visuel/prototype/familia.html`). C'est la base
des thèmes suivants : émotions et caractère d'abord, puis vêtements, puis le corps.

Jacques, 2-3 nov. 2026 : des thèmes « plus vivants », imagés, « quelque chose de solide. Complet. Autant pour
l'allemand que l'espagnol ». Ses décisions sont dans `decisions/DECISIONS.md` : les relire avant de commencer.

## Les règles (validées par Jacques le 3 nov. 2026, « Je suis d'accord. »)

1. **Jamais une scène ET un thème le même jour dans la séance** : le thème *remplace* l'arrêt de scène
   (`insererThemeIllustre()` dans `index.html`).
2. **Pas de thème qui refait une scène.** Un sujet qui a déjà sa scène (la cuisine, le marché…) prend un autre
   angle (les gestes, les personnes) ou n'a pas de thème.
3. **Un mot appris compte partout** : scène, thème et cartes partagent la même progression. Chaque question d'un
   thème envoie `{type:"reponse", mot, genre, cat, juste}` pour le mot qu'elle teste, à la forme du corpus (abuela,
   la ; Großmutter, die ; alto, adjectif), et `revisionDeScene()` fait le reste, comme pour une scène : un mot neuf
   entre dans les cartes, une erreur le fait revenir dans deux minutes, une bonne réponse ne le fait avancer que
   s'il est dû. Vérifié sur un profil vierge (3 nov.).
4. **Deux blocs distincts sur l'accueil**, chacun avec sa phrase : « Explorer les scènes », puis « Thèmes illustrés ».
5. **Le tirage suit les mots** (Jacques, 3 nov. : « on ne demandera plus de questions sur Tío. Avant 16 jours. »).
   Une partie ne tire pas des questions : elle choisit d'abord des MOTS dans la progression des cartes, puis habille
   chacun d'une question (`visuel/prototype/themes/tirage.js`, commun à tous les thèmes) :
   - la page donne la liste de ses mots (message `etats`) ; l'app rend l'état de chacun (`etatsDesMots()`) :
     neuf, dû, pas encore dû, hors jeu (absent du corpus ou hors de l'offre gratuite) ;
   - l'ordre : les **dus** (les plus en retard d'abord), puis les **ratés récemment**, puis au plus **10 nouveaux**
     par partie (3 dans la séance) ;
   - un mot **pas encore dû n'est jamais demandé** ; un mot raté dans la partie y revient trois questions plus loin ;
   - plus rien de dû ni de nouveau : « **Tout est revu pour aujourd'hui** » et la prochaine échéance, sans reposer
     des mots déjà sus ;
   - « **Encore des questions** » (Jacques : « on pourrait toujours offrir des questions supplémentaires ») : un
     bouton sur cet écran ET en fin de partie, jamais dans la séance. C'est l'élève qui choisit, rien ne se lance
     seul. Ces questions portent sur des mots **déjà vus** du thème (`Tirage.supplement()`), au hasard ; elles ne
     faussent pas la répétition espacée, puisque `revisionDeScene()` ne fait pas avancer un mot pas encore dû et
     qu'une erreur le fait revenir plus tôt ;
   - chaque sorte de question sait **viser un mot** (`EX.<sorte>(w)`, false si elle ne peut pas) ; les sortes qui
     ne testent pas un mot à elles seules (« combien », les mots de groupe) ne font qu'habiller un mot choisi ;
   - la réserve de questions reste invisible : elle sert à ce qu'un mot revenu ne revienne pas avec la même phrase.
   Vérifié par simulation sur 45 jours (profil vierge, 15 % d'erreurs) : aucun mot pas dû demandé, chaque question
   sur le mot prévu, tous les mots tournent, les rares autant que les autres (tío 12, suegra 14, nuera 12) ; et sur
   un profil avancé : les mots maîtrisés absents 15 jours, de retour le 16e.

S'y ajoutent les décisions qui les précèdent :
- des personnes **photoréalistes**, jamais de 3D ni de bande dessinée (« on a toujours été avec des vrais
  personnages ») ; fond de studio gris clair ; détourées et rangées **à l'échelle de leur taille** ;
- des **personnages réutilisables** d'un thème à l'autre (les 12 de Descripción, les 14 de la famille) ;
- **la cohérence avec l'histoire** (`scenes/personnages.json`, bloc `_arc`) : la famille en Allemagne est celle
  d'**Anna** (celle de Mark est à Montréal) ; Anna n'a ni compagnon ni enfant ;
- **la vignette dit le sujet autrement qu'une rangée de personnes** (Jacques : « On dirait deux groupes de
  familles ») : l'arbre pour la famille, la toise pour Décrire.

## Ce qu'est un thème

Une page autonome `visuel/prototype/<thème>.html`, ses images dans `visuel/prototype/<thème>/`, ouverte par l'app
dans le cadre des scènes (`sceneCadre`). Elle parle comme une scène, par `postMessage` (`source: "wortando-scene"`) :
- `exercice` `{juste}` à chaque réponse, `bonne` si elle est juste (objectif du jour, série, carreaux) ;
- `fini` `{bons, faits}` à la fin, `fermer` sur le rond « ‹ ».

Paramètres : `apprendre=es|de`, `lang=<langue d'interface>`, `nuit=1`, `seance=1` (depuis la séance : 6 questions,
sans découverte), `variante=es|latam` et `r=<AUDIO_REVISION>` (la voix de la découverte).

Le déroulé, dans la page :
1. **Une découverte** : on touche, on voit, on entend. L'arbre et les fiches de la famille ; les yeux, les cheveux,
   la toise et les accessoires de Décrire. La voix **seulement** pour un mot qui a déjà son fichier (sha1 du texte,
   16 caractères, `https://deutschai-b6fbb.web.app/[es-es/|es-419/]<id>.mp3`), empreintes calculées au chargement
   (sur iPhone, `play()` doit partir dans le geste). Un mot sans voix : en faire la liste, Jacques donne son accord
   avant toute dépense ElevenLabs (voix v2 seulement).
2. **Jusqu'à 20 questions** (Jacques : « 10 questions, ça ne me paraît pas beaucoup »), une par mot de la file
   (règle 5), **jamais deux fois la même sorte de suite**, **jamais deux fois la même question dans une partie**
   (`cleQuestion()`). Dans la séance : 6. Moins quand il y a moins de mots à revoir : c'est voulu.
3. Un écran de fin (score, « Encore des questions » hors séance, « Terminer »).

**Les boutons d'action toujours tout en bas** (Jacques, 3 nov. 2026, la règle des scènes : « commencer les exercices
ou continuer soit toujours en bas complètement de l'écran ») : Commencer, Suivant, Terminer, « Encore des questions »
sont des boutons fixes (`.suite`, `position:fixed`, `bottom: calc(12px + env(safe-area-inset-bottom))`, `z-index:5000`),
jamais dans le flux ; le second (« Encore des questions ») juste au-dessus du premier ; le contenu garde assez de place
en bas (`padding-bottom` ≥ deux boutons + 24 px + la zone de sécurité). Modèle : `ropa.html` (`boutonsDeFin()`).

**La traduction dans la langue d'interface** (Jacques, 3 nov. : « Il n'y a pas la traduction française. Qui serait
importante ») : une ligne plus petite, grise, en italique (`.trad`), **sous le mot dans la découverte** et **après la
réponse, sous la phrase juste** — jamais avant, elle donnerait la réponse. Comment, dans `familia.html` et
`descripcion.html` :
- en **français, anglais, portugais** (et en **allemand** pour qui apprend l'espagnol), la phrase entière, fabriquée
  par un objet `TRADS[langue]` à partir des **mêmes choix** que la question (les mêmes personnes, le même lien, le
  même possessif, le même groupe, les mêmes traits) ; chaque `EX.<sorte>` pose `trad` à côté de `motQ`, et `juger()`
  l'affiche. Les accords sont dans l'objet (d'Anna, ma tante, « un frère et une sœur », o pai dela, a/an) ;
- dans les **autres langues** (arabe, turc, ukrainien, persan, polonais, russe), le mot de la question et sa
  traduction tirée du **corpus relu** (`<thème>/gloses.json`, fait par `visuel/familia/gloses.py`) : « la abuela —
  бабуся ». Une phrase fabriquée aux cas de ces langues, avec des prénoms étrangers, serait souvent fausse et
  personne ne la relirait ;
- les **cases de la découverte**, de courtes expressions (« los ojos azules »), sont traduites à la main dans les
  dix langues (`TRAD_DECOUVERTE`), les prénoms restant écrits comme à l'écran.

**La voix** (Jacques, 3 nov. : « il manquait aussi des paroles » ; « Pour le moment, on va mettre les voix du
téléphone. Quand il n'y a pas de voix. ») : une seule fonction pour tous les thèmes, `Voix.dire(texte)`
(`visuel/prototype/themes/voix.js`) :
- le **fichier enregistré** s'il existe (sha1 du texte écrit ; Aurora, Lolita ou Monica selon la langue et la
  variante), sinon **la voix du téléphone**, choisie comme dans l'app (la meilleure voix locale de la langue et de la
  variante, jamais une voix fantaisie de `VOIX_A_FUIR`) ;
- la page sait **avant de jouer** quels textes ont un fichier (`themes/sons.json`) : sur iPhone, `play()` et
  `speak()` doivent partir dans le geste ; attendre l'échec d'un fichier ferait taire la page ;
- ce qu'on dit : dans la découverte, la fiche ou le mot touché ; **après une réponse, la phrase affichée EN
  ENTIER** (Jacques, 3 nov. : « Oui, partout », règle de TOUS les thèmes) — la phrase juste de la question
  (`juger(ok, bonne, phrase)` la reçoit et la dit), sinon le mot clé à la forme du corpus (« la tía », « alto ») ;
  une flèche de paire (« el tío → la tía ») se dit comme une virgule. Le fichier enregistré s'il existe pour ce
  texte exact, sinon la voix du téléphone : ces phrases se fabriquent depuis les données, beaucoup n'ont pas encore
  de fichier, et leur enregistrement attend l'accord de Jacques ;
- chaque page expose `textesAVoix()` : les fiches et les mots ; `python visuel/voix_themes.py` les relève, **joue
  des parties** (`PARTIES_VOIX`, 150) pour relever les phrases dites après les réponses, et le tout
  (→ `visuel/<thème>/voix.json`, que lisent `audio/manifest.py` et `audio/manifest_es.py`, source `<thème>`),
  écrit `themes/sons.json` et chiffre ce qui manque. Un texte à chiffres demande sa lecture en lettres dans
  `audio/lectures/<langue>.json` (« Tiene setenta y nueve años. »).
- Enregistrer (accord de Jacques, v2 seulement) : `python audio/manifest.py --ecrire`, puis `generer_es.py --variante
  es|latam --niveaux A1 --sources <thème>` et `generer.py --niveaux A1 --sources <thème>`, la normalisation
  (`generer_es.py --normaliser`, `normaliser.py --niveaux A1`), `controler_sons.py` (aucun SATURE, CLIC, TRAINE sur les
  fichiers neufs), **`python visuel/voix_themes.py` pour refaire `sons.json`**, `audio/deposer.py`, et
  `AUDIO_REVISION` + 1.

**Agrandir les images** (Jacques, 3 nov. : « dans les thèmes, on devrait faire comme dans les scènes, donc avoir la
possibilité d'agrandir les images [...] c'est un peu loin pour voir la couleur des yeux ») : **toute page de thème
charge `themes/zoom.js`** et appelle `Zoom.init({direct, loupe, langue})`. Une visionneuse plein écran, fond
sombre, bouton « × » : dedans, le zoom des scènes (deux doigts jusqu'à ×4 autour du point entre les doigts, un doigt
pour se déplacer, double toucher ×2,5 et retour, molette à l'ordinateur), et l'indice « Écarte deux doigts » de la
v1068, deux fois au plus, plus jamais après un premier agrandissement (même clé que les scènes,
`wortando_pinceZoome`). Ce qui l'ouvre :
- **deux doigts** sur n'importe quelle image de l'exercice (`main img`, `main svg`) : le geste des scènes, il ouvre
  la visionneuse et continue dedans ;
- `direct` : les images qui ne sont **pas** des réponses (un visage, une photo, une fiche) s'ouvrent au toucher ;
- `loupe` : ce qu'on touche **pour répondre** (une personne de la rangée, l'arbre, une case de la découverte) porte
  une petite loupe, pour ne jamais répondre en voulant regarder. Un élément qui n'est pas une image (l'arbre en SVG)
  est copié dans la visionneuse ; `data-zoom="<image>"` y montre une autre image (une personne en pied s'agrandit en
  son visage, faute de pixels dans l'image en pied).
- **L'app s'en sert aussi** pour les tableaux de la galerie (Jacques, 3 nov., « Oui, les deux ») : `index.html`
  charge `visuel/prototype/themes/zoom.js`, **une seule source** ; l'option `pincer` dit ce que deux doigts
  agrandissent (sinon toute image de `main`), une toile (canvas) s'ouvre copiée en image (un tableau en cours tel
  qu'il est peint, rien de plus), `data-zoom` donne l'image entière d'un tableau gagné, et `langue` peut être une
  fonction. Un changement de `zoom.js` vaut pour l'app ET les thèmes : essayer les deux.
- **Les yeux se lisent à 375 px** : une question sur les yeux d'une personne montre son gros plan à toute la largeur
  (`<Nom>-yeux.webp`, fait par `visuel/descripcion/yeux_personnes.py`, la place des yeux relevée à l'œil), jamais le
  petit visage ; les yeux de la découverte sont en deux colonnes. Une image neuve où l'on doit voir un détail : la
  regarder au format du téléphone avant de la publier.

**Le mot choisi, quand il est faux** (Jacques, 3 nov. : « quand je dis le mauvais, on devrait avoir l'affichage
traduit aussi. Pour le mauvais mot. ») : sous la bonne réponse et sa traduction, une ligne de plus, « Tu as choisi :
<le mot> — <sa traduction> » (`.trad.faux`, clé `choix` des `TEXTES`), dans la langue d'interface. La page pose
`choixFaux = {texte, trad}` au clic, avant `juger()`, qui l'affiche ; `montrer()` le remet à `null`. La traduction
vient du **corpus relu** (`<thème>/gloses.json`), sinon d'une traduction **écrite à la main** de la page (les cases
de la découverte : « les yeux marron », jamais « châtain » pour des yeux) ; une description choisie se traduit
entière par `TRADS`. **Rien de plus** quand le choix n'a pas de traduction sûre : un prénom, une personne touchée,
un nombre, vrai / faux, un possessif seul (mi / su), un accord (alto / alta). Modèle : `familia.html`
(`tradDuChoix`), `descripcion.html` (`tradTrait`).

**Les boutons du bas** (Jacques, 3 nov., la règle des scènes depuis la v1059 : « commencer les exercices ou
continuer soit toujours en bas complètement de l'écran ») : **tout bouton qui fait avancer est fixé en bas de
l'écran**, au-dessus de tout (`z-index: 5000`, comme les scènes), dans le même verre vert : « Commencer »,
« Continuer » (`.suite`) et ceux de la fin, « Encore des questions » et « Terminer », côte à côte dans
`<div class="bas">` (fin de partie et « Tout est revu »). Le contenu garde en bas la place du bouton : `padding-bottom`
du `body` d'au moins 54 px + 24 px + 12 px + la zone sûre (`calc(env(safe-area-inset-bottom,0px) + 90px)`), pour
qu'aucune réponse ne passe dessous. À vérifier à 375 px sur la question la plus longue, défilée jusqu'en bas
(Décrire : « elige », la description à choisir), de jour et de nuit. Modèle : `familia.html`, `descripcion.html`.

**La page a la hauteur de l'écran, comme une scène** (Jacques, iPhone, 3 nov. : « Commencer » « pas complètement
en bas », alors que le navigateur le montrait au bon endroit). Le document d'une scène ne dépasse jamais son cadre ;
celui d'un thème défilait (Décrire : 2 500 px), et sur iPhone un bouton fixe dans un cadre dont le document déborde
ne tombe pas au bas de l'écran. Donc `html{height:100%;overflow:hidden}` et `body{height:100%;overflow-y:auto}` :
le contenu défile DANS le body, `document.documentElement.scrollHeight` reste celui du cadre (le mesurer : il doit
valoir `innerHeight`), et la remise en haut d'une question fait aussi `document.body.scrollTop = 0`. Rappel : un
cadre ne reçoit jamais `env(safe-area-inset-*)` (c'est l'app qui pose la marge, `#sceneSeance`) ; le bouton tombe
donc à 12 px du bas du cadre, exactement comme le « Continuer » des scènes.

**Les noms des boutons, fixes, partout** (Jacques, 3 nov. : « les noms des contrôles doivent être identiques
partout ») : on ne dit jamais « Suivant ». Les clés des `TEXTES` d'une page, et les textes communs de `tirage.js` :

| clé | fr | en | de | les autres langues |
|---|---|---|---|---|
| `commencer` | Commencer | Start | Starten | tr Başla, uk Почати, fa شروع, ar ابدأ, pt Começar, pl Zacznij, ru Начать |
| `suivant` (le bouton qui avance) | Continuer | Continue | Weiter | le mot des scènes (`suite` de `visuel/prototype/index.html`) : tr Devam, uk Далі, fa ادامه, ar متابعة, pt Continuar, pl Dalej, ru Дальше |
| `terminer` | Terminer | Finish | Beenden | tr Bitir, uk Завершити, fa پایان, ar إنهاء, pt Terminar, pl Zakończ, ru Завершить |
| `TIRAGE_TEXTES.encore` | Encore des questions | More questions | Weitere Fragen | dans `themes/tirage.js` |
| `TIRAGE_TEXTES.revu` | Tout est revu pour aujourd'hui. | Everything is reviewed for today. | — | dans `themes/tirage.js` |

**Toutes les phrases sont fabriquées depuis les données** (`personnages.json`, `familia.json`), jamais écrites à la
main : une image ne dit que ce qu'elle montre, et aucune question ne la contredit. Les questions validées par
Jacques (« Ça me convient », 3 nov.) : 8 sortes pour la famille, 7 pour Décrire.

**La réserve : au moins 100 questions différentes par thème et par langue** (« J'irais une centaine de questions
par thème »), mesurées, jamais supposées : `python tests/themes_illustres.py`. Au 3 nov. : famille ≈ 2 400 (es et
de) ; Décrire ≈ 650 (es), 625 (de) ; les contraires 215 (es), 200 (de) ; « Où est le chat ? » 606 (es), 582 (de), dont 235 et 212 sans compter les
départs des questions de mouvement ; Manger et goûter ≈ 1 560 (es), 1 580 (de), dont ≈ 1 110 additions de la carte
du café (« ¿Cuánto es? », autant de commandes différentes) et ≈ 440-470 pour tout le reste ; les métiers 589 (es), 636 (de), dont ≈ 220 hors du vrai ou faux ; les transports 985 (es), 977 (de), dont ≈ 420 trajets du plan de métro et 192 situations de guichet ; les loisirs 1 009 (es), 939 (de), dont ≈ 480 et 415 hors du vrai ou faux. On élargit par de nouvelles combinaisons dans les sortes validées, jamais par du
remplissage ni des quasi-doublons : la même question avec d'autres leurres n'en est pas une nouvelle (c'est pourquoi
« completa » avec le visage ne s'ajoute pas à « yeux »). Une description partielle doit désigner **une seule**
personne parmi celles montrées ; un trait inconnu (les yeux d'Anna) n'exclut jamais personne.

**Un thème de choses** (« Les contraires », `contrarios.html`) : une image par mot, et pour chaque image la liste
des mots **clairement faux** pour elle (`faux`, dans `visuel/contrarios/contrarios.py`) ; un leurre ou le faux
d'un « vrai ou faux » n'est jamais pris ailleurs. Une vieille bicyclette n'est pas forcément laide, une valise pas
forcément neuve : ce que l'image ne tranche pas n'est jamais proposé. Ser / estar n'est demandé que sur les mots
où un seul verbe est juste (la taille, la largeur ; ouvert, fermé, plein, vide).

## Faire un thème, pas à pas

1. **Le sujet** : vérifier les règles 2 (pas de scène refaite) et la cohérence de l'histoire. Écrire les mots
   allemands et espagnols et vérifier qu'ils sont au corpus (`themes.json`, `espanol/datos/temas.json`,
   `adjetivos.json`, `adjectif.json`). Un mot qui manque : le proposer (allemand : JSON racine ; espagnol :
   `espanol/ajouter_mots.py espanol/ajouts/<fichier>.json`, mêmes clés que ses voisins, fr en pt ar de) — ses voix
   demandent l'accord de Jacques.
2. **Les lieux, AVANT toute image** (Jacques, 3 nov. : la continuité des lieux) : une image de thème qui montre un
   lieu connu (l'appartement de Mark, celui d'Anna, une pièce des scènes ou des vidéos) reprend les mêmes meubles,
   couleurs et disposition que les scènes et `video/LIEUX.md` ; un lieu nouveau s'ajoute à `video/LIEUX.md`. Se
   vérifie avant de lancer la génération, pas après.
3. **Les personnes** : réutiliser d'abord celles qui existent. Une personne neuve : un script comme
   `visuel/familia/familia.py` (fal, `fal-ai/nano-banana-pro`, **0,15 $ l'image** ; `--montrer` est gratuit).
   **Annoncer le coût du lot avant de le lancer**, puis **vérifier chaque image contre sa description** ; une image
   ratée se refait. Mark et Anna ne se régénèrent pas : leur image sert de référence (retouche
   `nano-banana-pro/edit`). Puis `detourer.py` (BiRefNet, quelques centimes) et `web.py` (les webp : en pied
   900 px, visage carré pris sur la silhouette détourée — la tête d'un enfant n'est pas celle d'un adulte). Les
   originaux restent hors du dépôt (`visuel/<thème>/img/`, dans `.gitignore`).
4. **La page** : copier `familia.html` ou `descripcion.html`, garder le protocole, les textes `TEXTES` dans les
   **10 langues d'interface** (fr en tr uk fa ar pt pl ru de), `dir="ltr"` sur tout texte de la langue apprise et sur
   le compteur (sinon « 10 / 5 » en arabe), les couleurs en variables avec leur version `html.nuit`.
5. **L'app** (`index.html`) : voir « Le branchement » ci-dessous.
6. **La vignette** : une fonction de plus dans `visuel/vignettes_themes.py` (4:3,4), qui dise le sujet autrement.
7. **Contrôler** : `python tests/themes_illustres.py` (≥ 100 questions, séries propres), `node tests/syntaxe.js`,
   `python tests/verifier.py`, les deux parcours (`fusion-espagnol/parcours.py --app de` et `--app es-moteur`),
   chaque écart vérifié ligne à ligne et la nouvelle référence écrite dans CLAUDE.md ; à l'écran, au format du
   téléphone, de jour, de nuit, en arabe ou en persan.

## Un thème d'objets dans une pièce : « Où est le chat ? » (3 nov. 2026)

Les prépositions de lieu (`gato.html`, `visuel/gato/gato.py`, la seule source). Ce qu'il apprend aux thèmes suivants :
- **une pièce vide, puis des retouches** (`nano-banana-pro/edit`, la pièce + la première image du chat en références) :
  même cadrage, mêmes meubles, seule la place du chat change. Sur 31 retouches, 9 ont montré autre chose que le prompt :
  4 sont devenues ce qu'elles montrent (le chat sur le panier au lieu de la fenêtre, à côté de la table au lieu d'entre
  les chaises…), 2 places ont été abandonnées après trois essais (sur la chaise, sous la table : le modèle met le chat
  sur la table, ajoute une deuxième table ou change de cadrage). **Vérifier chaque image agrandie**, pas sur une planche ;
- **où est le chat** se mesure (`--mesurer` : la différence avec la pièce vide) : la flèche du mouvement va d'une place
  à l'autre, et la page **recadre** chaque image autour du chat (à 375 px, la pièce entière montre un chat de 15 px) ;
- **le mouvement** (Wohin + accusatif) : l'image d'AVANT et une flèche dans la question, l'image d'APRÈS dans la réponse ;
- une préposition est un mot du thème : `{mot: "hinter", cat: "praep"}` fait avancer la carte des Prépositions
  (`carteDeScene()`, cat « praep ») ;
- deux places vraies sur une même image (le sac d'Anna est devant le canapé) : `AUSSI` dans `gato.py`, jamais l'une
  pour leurre de l'autre ; en espagnol, toutes les formes justes d'une place (encima de / sobre / en la mesa) ;
- les voix à enregistrer : `visuel/gato/voix.json` (fait par `gato.py`).

## Un thème de gestes et de documents : « Les transports » (3 nov. 2026, vague 2)

Se déplacer (`transportes.html`, `visuel/transportes/transportes.py`, la seule source). Ce qu'il apprend aux thèmes suivants :
- **l'angle** (règle 2) : les scènes U-Bahn, Zug, Kreuzung et Flughafen font nommer leurs objets ; ici, des personnes
  qui se déplacent et les gestes du voyage (mit dem Bus / en autobús, ein-, aus-, umsteigen / subir al, bajar del,
  cambiar de línea, l'heure du départ, le billet) ;
- **ce qui a du texte se DESSINE**, jamais ne se demande à un modèle d'image : le tableau des départs, le plan du
  métro (trois lignes qui se croisent deux à deux une seule fois, d'où une seule correspondance par trajet) et les
  billets sont tracés par la page depuis la donnée, lisibles à 375 px, et gratuits ;
- **les lieux des scènes** (décision du 3 nov. sur la continuité) : une photo prise à l'arrêt de bus ou dans la station
  reçoit l'image de la scène « pour le lieu » (`LIEUX`, `LIEU_TXT`), et une image de scène qui montre déjà le geste se
  **recadre** au lieu de se payer (`ubahn-ein` : Mark à la porte de la rame) ; les lieux neufs sont dans `video/LIEUX.md` ;
- **les nombres** : chaque texte à chiffres a sa lecture en lettres dans `transportes.json` (`lectures`), que la page
  donne à la voix du téléphone (« acht Uhr fünfzehn », « veintinueve euros con noventa ») ; à recopier dans
  `audio/lectures/<langue>.json` le jour où l'on enregistre. La sorte `prix` fait choisir le prix écrit en lettres, avec
  des leurres qui ressemblent (29 / 92, 16 / 60, sesenta / setenta ; « sesenta y un euros », jamais « y uno ») ;
- **l'heure en mots** : les leurres sont toujours faux pour l'heure montrée (halb acht pour 8 h 30, jamais « drei
  Viertel neun », régional mais juste) ; ni midi ni 13 h (halb eins, la una) ;
- le relevé exhaustif des phrases (`visuel/transportes/toutes-les-phrases.json`, ~61 000 caractères en allemand) est un
  plafond ; ce qui s'enregistre est l'inventaire de `visuel/voix_themes.py` (`voix.json`).

## La séance

Un jour sur trois (`themeDuJour()`), le thème illustré prend la place de l'arrêt de scène (même place : la séance
n'en est pas plus longue ; sans arrêt ce jour-là, il se place au milieu). A1 et A2 seulement ; ni pendant Premiers
pas, ni pendant la première semaine d'un vrai débutant (la rampe de l'objectif, v882), ni pendant les escales de
l'A1 voyage. Les thèmes à tour de rôle, dans l'ordre de `THEMES_ILLUSTRES`, au numéro du jour. La fin du thème
ramène aux cartes (`revenirDeLArret()`).

## Où est quoi

| | |
|---|---|
| `visuel/prototype/<thème>.html` | la page (découverte, questions, fin) |
| `visuel/prototype/<thème>/` | ses images web et ses données (`personnages.json`, `familia.json`) |
| `visuel/descripcion/`, `visuel/familia/`, `visuel/emociones/`, `visuel/contrarios/` | les scripts des images (génération, détourage, webp) |
| `visuel/vignettes_themes.py` → `visuel/prototype/themes/` | les vignettes de l'accueil |
| `index.html` : `THEMES_ILLUSTRES`, `ouvrirThemeIllustre()`, `majExplorerThemes()`, `themeDuJour()`, `insererThemeIllustre()`, `ouvrirArretTheme()` | l'app |
| `visuel/prototype/themes/tirage.js` | le tirage par mots, commun à tous les thèmes |
| `visuel/prototype/themes/voix.js`, `themes/sons.json`, `visuel/voix_themes.py` | la voix commune, les fichiers qui existent, l'inventaire |
| `visuel/prototype/themes/zoom.js` | agrandir les images, commun à tous les thèmes |
| `visuel/descripcion/yeux_personnes.py` | les gros plans des yeux de Décrire |
| `tests/themes_illustres.py` | la réserve de questions et les parties |

## Le branchement : le modèle à suivre pour un thème neuf

Ce qu'un thème neuf touche, et rien d'autre. Le reste (ruban de l'accueil, panneau de « N › » où sont TOUS les thèmes — `orbPanelData("themes_illustres")`, une option et sa vignette par thème de `THEMES_ILLUSTRES`, le retour au panneau en fin de thème —, séance, ouverture, retour, voix, tirage,
progression des mots) se fait tout seul à partir de ces quatre gestes.

**1. Dans `index.html`, une ligne dans `THEMES_ILLUSTRES`.** L'ordre de la table est celui du ruban de l'accueil et
du tour de rôle dans la séance.

```js
const THEMES_ILLUSTRES = {familia: {page: "familia.html", titre: "fam_tuile", tuile: "tuileFamilia"},
                          descripcion: {page: "descripcion.html", titre: "desc_tuile", court: "desc_court", tuile: "tuileDescripcion"},
                          emociones: {page: "emociones.html", titre: "emo_tuile", tuile: "tuileEmociones"}};
```

- `page` : le fichier dans `visuel/prototype/` ;
- `titre` : la clé I18N du nom du thème, `court` (facultatif) celle d'un nom court pour la vignette (« Décrire ») ;
- `tuile` : l'id de sa tuile dans Tout le contenu, rendue visible en es et de par la même boucle.

**2. Dans `index.html`, la tuile**, dans la section « Thèmes illustrés » (après `id="tuileDescripcion"`), sur le
modèle des deux autres : `<div class="orb hidden" data-orbid="emociones" id="tuileEmociones"
onclick="ouvrirThemeIllustre('emociones')" role="button" tabindex="0">`, une icône SVG, `data-i18n="emo_tuile"`.
Et ses clés (`emo_tuile`, et `emo_court` s'il y a un nom court) dans les **onze** blocs `I18N` (fr en tr uk fa ar pt
pl ru de es, dans cet ordre de blocs dans le fichier). Rien à ajouter aux listes blanches du japonais, de l'anglais
et du portugais : le bloc de l'accueil et la section y sont déjà cachés, et une tuile neuve y est cachée par
`data-orbid`.

**3. La vignette** : une fonction dans `visuel/vignettes_themes.py` (`VIGNETTES`), qui écrit
`visuel/prototype/themes/<thème>.webp` en **4:3,4 (600 × 510)**, le format des vignettes des scènes : l'accueil
les montre au même gabarit, trois par page (Jacques : « la même hauteur que ce qu'on a pour les scènes »). Le dessin
est composé pour ce format, rien n'y est coupé.

**4. La page `visuel/prototype/<thème>.html`**, qui charge `themes/tirage.js`, `themes/voix.js` et `themes/zoom.js`
(avec son `Zoom.init({direct: "...", loupe: "...", langue: LANGUE})`, voir « Agrandir les images ») et fournit au
tirage :

| ce que la page définit | à quoi ça sert |
|---|---|
| `motsDuTheme()` → `[{mot, genre?, cat?, ...}]` | les mots du thème, à la forme du CORPUS (« la abuela » : `{mot: "abuela", genre: "la"}` ; un adjectif : `{mot: "alto", cat: "adjectif"}`) ; ils servent de clés pour la progression |
| `EX.<sorte>(w)` → `true` / `false` | chaque sorte de question, capable de viser le mot `w` (false si elle ne peut pas) ; sans `w`, un tirage au hasard (les contrôles) |
| `motQ` | le mot que la question en cours teste, envoyé par `juger()` (`reponse`) |
| `SORTES`, `NB` (20, 6 en séance), `NEUFS_MAX` (10, 3 en séance) | |
| `montrer()`, `fin()`, `toutRevu()`, `demarrer()`, `encoreDesQuestions()` | la partie : les recopier de `familia.html`, elles sont identiques d'un thème à l'autre |

Le protocole avec l'app : `etats` (la page demande, l'app répond avec l'état de chaque mot, `etatsDesMots()`),
`exercice`, `bonne`, `reponse` (le mot testé), `fini`, `fermer`.

**Un mot à deux sens : `sens`** (3 nov. 2026, v1082). Quand le corpus a deux entrées pour le même mot, chacune a sa
carte : « rico » est « délicieux » (la comida está rica) ET « riche » (es rico). Sans précaution, une réponse sur
« es rico » ferait avancer la carte « délicieux ». Le même piège existait pour « sauer » (acide / fâché) et pour
« aburrido » (ennuyeux / qui s'ennuie). La règle, générale :
- le mot porte **`sens`**, la traduction française EXACTE de l'entrée du corpus que le thème enseigne
  (`{mot: "rico", cat: "adjectif", sens: "riche"}`) ; la page l'envoie dans `reponse`, et `tirage.js` dans `etats` ;
- `carteDeScene()` (`index.html`) prend alors la carte qui porte cette traduction (rang 1 d'un adjectif, rang 3 d'un nom,
  `traduction` d'un verbe) ; **sans `sens`, ou si aucune carte ne le porte, rien ne change** : la première, comme
  avant, pour les scènes comme pour les autres thèmes ;
- au corpus espagnol, un second sens d'un adjectif entre par `espanol/ajouter_mots.py` avec `"_second_sens": true`
  sur sa ligne (sans cette marque, un mot déjà présent n'est jamais rajouté) ;
- dans `emociones.html`, `sens` vient d'`emociones.json` (clé `sens`, tirée du corpus par `visuel/emociones/emociones.py`,
  `SENS_VOULU` pour les mots dont le thème ne prend pas la première entrée) ; les gloses suivent la même entrée.
Vérifié sur un profil vierge : une bonne réponse sur « rico » (riche) fait avancer la carte riche et laisse
« délicieux » neuve, et l'inverse ; sans sens, la carte rendue est celle d'avant.

**Contrôle** : ajouter le thème à `THEMES` dans `tests/themes_illustres.py`, puis le lancer.

## L'anglais (essai admin, 3 nov. 2026)

Jacques : « Pour que l'anglais suive aussi. Les thèmes qu'on implémente, les thèmes dans l'apprentissage de
l'anglais. » **La même page, les mêmes images, la même mécanique** (tirage, progression, traduction) : chaque page
accepte `apprendre=en` et a son objet `EN`, à côté de `ES` et `DE`. **Les phrases et les questions sont écrites pour
l'anglais**, jamais traduites de l'espagnol : elles enseignent la grammaire anglaise.

- **Le branchement** : `en: true` sur la ligne du thème dans `THEMES_ILLUSTRES` (index.html). Sans lui, le thème
  reste caché en anglais (accueil, Tout le contenu, séance : `themesIllustresOuverts()`). La liste blanche CSS de
  l'anglais laisse passer toute tuile `onclick="ouvrirThemeIllustre(…)"` et la place **en dernier** dans Tout le
  contenu (`order: 1`) : les sections cachées de l'anglais y laissent couler leurs tuiles.
- **L'interface est en français** : `TRADS.fr` traduit les phrases anglaises, `T()` retombe sur le français.
- **Américain ou britannique** : l'app passe `variante=us|gb` (`voixThemeIllustre()`). La page change les mots qui
  diffèrent (Mom / Mum, gray / grey, mustache / moustache, color / colour) et le dit dans une note.
- **Les mots** : `genre: ""` (le corpus anglais n'a pas d'article) ; un mot qui manque au corpus s'ajoute dans
  `anglais/outils/mots_<niv>.py` ou `noms_<niv>.py`, puis `python anglais/outils/construire.py` (plus de 5 minutes),
  `frequence.py --ecrire` et `voisins.py --ecrire`. Ajoutés le 3 nov. : chubby, slim, wavy (A2), earring (A2) ; open (A1), disgusting (A2). ⚠️ Un `construire.py` complet change aussi des phrases d'exemple d'autres mots (les sources ont bougé depuis la dernière construction) : on ne pose alors que les mots ajoutés, pris dans la reconstruction, dans la version du dépôt.
- **La voix** : aucune voix nouvelle (décision du 3 nov., écoute à l'aveugle Sarah / Google / Azure d'abord). Ce qui
  a un fichier `en-us/` se dit avec Sarah (américain), le reste avec la voix du téléphone (`en-US`, `en-GB`). Le
  britannique : toujours le téléphone. Il manque à Sarah, dans « Décrire » : *light brown*, *wavy*, *of medium
  height*. La famille n'a pas de voix (comme en espagnol et en allemand).
- **Ce que chaque thème enseigne en anglais** :
  - **La famille** : le génitif (« Peter is Anna's father », et pour un couple « Peter and Monika's daughter ») —
    une sorte de plus, `genitif` ; his / her selon celui qui possède ; our et their ; les noms de groupe du corpus,
    comme en allemand (parents, siblings, grandparents) ; les beaux-parents en -in-law. « cousin » ne dit pas le
    sexe : un seul mot du thème (`s: "*"`), pas de paire cousin → cousin.
  - **Décrire une personne** : is / has / wears ; l'ordre des adjectifs devant *hair* (longueur, forme, couleur,
    sans virgule) — la sorte `ordre`, à la place de l'accord espagnol ; *chubby* plutôt que *fat*, *dark eyes* et
    jamais *black eyes* (deux notes dans la découverte) ; le superlatif à trois (« Who is the tallest? »).
  - **Les contraires** : l'adjectif invariable après *be* (« The door is open. »), *the one* (« The one on the right
    is ___. »), et deux sortes de plus : `comparatif` (-er, more, good → better, bad → worse ; les pièges : le double
    comparatif *more bigger*, *beautifuler*, le superlatif) et `article` (*a* ou *an* devant l'adjectif : *an old
    bike*, *an ugly vase*). Le britannique change les noms des phrases sans image (flat, film, jumper, High Street).
    Le sens du mot et la traduction des phrases de l'image viennent de l'espagnol de la même image.
- **Contrôle** : `ANGLAIS` dans `tests/themes_illustres.py` (le thème y passe en `en` et en `en&variante=gb`).

Deux ajouts de « La journée » (3 nov. 2026), utiles aux thèmes suivants :
- **un adverbe compte aussi** : `carteDeScene()` accepte `{mot, cat: "adverbe"}` (la carte d'`adverbienTheme`,
  siempre / immer, zuerst) ; un mot que le corpus n'a pas reste « hors jeu », la page n'a rien à prévoir ;
- **une question en plusieurs gestes** (remettre quatre étapes dans l'ordre) : la page définit `testerOrdre()`, qui
  la résout et rend la réponse ; le contrôle l'appelle quand la question a un `.ordre`.
- **chaque mot a au moins deux sortes** : un mot qu'une seule sorte sait viser (les adverbes de fréquence, les moments
  de la journée) fait se suivre deux fois la même sorte dès que deux de ces mots se suivent dans la file.
