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
3. Un écran de fin (score, « Encore une fois », « Terminer »).

**Toutes les phrases sont fabriquées depuis les données** (`personnages.json`, `familia.json`), jamais écrites à la
main : une image ne dit que ce qu'elle montre, et aucune question ne la contredit. Les questions validées par
Jacques (« Ça me convient », 3 nov.) : 8 sortes pour la famille, 7 pour Décrire.

**La réserve : au moins 100 questions différentes par thème et par langue** (« J'irais une centaine de questions
par thème »), mesurées, jamais supposées : `python tests/themes_illustres.py`. Au 3 nov. : famille ≈ 2 400 (es et
de) ; Décrire ≈ 650 (es), 625 (de). On élargit par de nouvelles combinaisons dans les sortes validées, jamais par du
remplissage ni des quasi-doublons : la même question avec d'autres leurres n'en est pas une nouvelle (c'est pourquoi
« completa » avec le visage ne s'ajoute pas à « yeux »). Une description partielle doit désigner **une seule**
personne parmi celles montrées ; un trait inconnu (les yeux d'Anna) n'exclut jamais personne.

## Faire un thème, pas à pas

1. **Le sujet** : vérifier les règles 2 (pas de scène refaite) et la cohérence de l'histoire. Écrire les mots
   allemands et espagnols et vérifier qu'ils sont au corpus (`themes.json`, `espanol/datos/temas.json`,
   `adjetivos.json`, `adjectif.json`). Un mot qui manque : le proposer (allemand : JSON racine ; espagnol :
   `espanol/ajouter_mots.py espanol/ajouts/<fichier>.json`, mêmes clés que ses voisins, fr en pt ar de) — ses voix
   demandent l'accord de Jacques.
2. **Les personnes** : réutiliser d'abord celles qui existent. Une personne neuve : un script comme
   `visuel/familia/familia.py` (fal, `fal-ai/nano-banana-pro`, **0,15 $ l'image** ; `--montrer` est gratuit).
   **Annoncer le coût du lot avant de le lancer**, puis **vérifier chaque image contre sa description** ; une image
   ratée se refait. Mark et Anna ne se régénèrent pas : leur image sert de référence (retouche
   `nano-banana-pro/edit`). Puis `detourer.py` (BiRefNet, quelques centimes) et `web.py` (les webp : en pied
   900 px, visage carré pris sur la silhouette détourée — la tête d'un enfant n'est pas celle d'un adulte). Les
   originaux restent hors du dépôt (`visuel/<thème>/img/`, dans `.gitignore`).
3. **La page** : copier `familia.html` ou `descripcion.html`, garder le protocole, les textes `TEXTES` dans les
   **10 langues d'interface** (fr en tr uk fa ar pt pl ru de), `dir="ltr"` sur tout texte de la langue apprise et sur
   le compteur (sinon « 10 / 5 » en arabe), les couleurs en variables avec leur version `html.nuit`.
4. **L'app** (`index.html`) : une entrée dans `THEMES_ILLUSTRES` (page, clé du titre, titre court, tuile) — c'est
   elle qui nourrit le ruban de l'accueil, le tour de rôle de la séance et l'ouverture ; une tuile dans la section
   « Thèmes illustrés » de Tout le contenu ; les clés de texte dans les **onze** blocs `I18N` (fr en tr uk fa ar pt
   pl ru de es) ; rien à ajouter aux listes blanches du japonais, de l'anglais et du portugais (le bloc et la
   section y sont déjà cachés).
5. **La vignette** : une fonction de plus dans `visuel/vignettes_themes.py` (3:4), qui dise le sujet autrement.
6. **Contrôler** : `python tests/themes_illustres.py` (≥ 100 questions, séries propres), `node tests/syntaxe.js`,
   `python tests/verifier.py`, les deux parcours (`fusion-espagnol/parcours.py --app de` et `--app es-moteur`),
   chaque écart vérifié ligne à ligne et la nouvelle référence écrite dans CLAUDE.md ; à l'écran, au format du
   téléphone, de jour, de nuit, en arabe ou en persan.

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
| `visuel/descripcion/`, `visuel/familia/` | les scripts des images (génération, détourage, webp) |
| `visuel/vignettes_themes.py` → `visuel/prototype/themes/` | les vignettes de l'accueil |
| `index.html` : `THEMES_ILLUSTRES`, `ouvrirThemeIllustre()`, `majExplorerThemes()`, `themeDuJour()`, `insererThemeIllustre()`, `ouvrirArretTheme()` | l'app |
| `visuel/prototype/themes/tirage.js` | le tirage par mots, commun à tous les thèmes |
| `tests/themes_illustres.py` | la réserve de questions et les parties |
