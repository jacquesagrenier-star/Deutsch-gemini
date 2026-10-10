# Brief pour une session cloud : la scène compte comme révision, et les mots qui manquent au corpus (10 oct. 2026)

Tu reprends un travail commencé en local. Tu n'as pas les notes de mémoire de la session locale : tout ce qu'il te faut est ici, plus `CLAUDE.md` (lis-le d'abord, en entier).

## Règles de cette session

- **Deux chantiers, deux branches, deux pull requests**, faits l'un APRÈS l'autre : `scenes-revision` puis `corpus-mots-scenes`, chacune partant de `main`. **Rien sur `main`.**
- Pas de changement de numéro de version.
- **Pas d'agents en parallèle** : ta session puise dans la même limite de 5 h que le PC de Jacques.
- Avant chaque PR : `python tests/verifier.py` et `node tests/syntaxe.js`.
- Scripts de modification dans un **fichier**, jamais en heredoc.
- Une autre session cloud travaille en même temps sur la branche `scenes-traduction` (la langue passée à la scène, le RTL, `visuel/prototype/traductions/`). Touche le moins possible à `ouvrirSceneSeance()` et au bloc `TEXTES` du prototype pour éviter les conflits.
- Compte rendu par branche : `.claude/compte-rendu-scenes-revision.md`, `.claude/compte-rendu-corpus-mots-scenes.md`.

## Contexte

Les scènes interactives : une image photoréaliste, l'élève touche le mot demandé (« Trouve ! ») ou répond à des questions par couche de niveau. Prototype : `visuel/prototype/index.html?scene=<nom>`, contenu dans `visuel/prototype/<nom>.points.json`, regénéré par `python visuel/prototype/construire.py <nom>`. L'app ouvre la scène dans une iframe (`ouvrirSceneSeance()`), derrière l'essai `scenes` (état `"admin"`, objet `ESSAIS`). La scène parle à l'app par `postMessage` (`source: "wortando-scene"`, types `fini` et `fermer` aujourd'hui).

## Chantier 1 — branche `scenes-revision` : une réponse dans la scène = une révision du mot

Décidé avec Jacques : la scène arrive dans la séance du jour **comme un type de carte**, et une réponse compte comme une révision du mot, pour la répétition espacée.

1. Lis comment l'app enregistre une révision de carte (état du mot, progression, synchronisation Firestore). ⚠️ `getWordState()` / `getProgress()` ont été un piège O(n²) (réparé en v100) : ne réintroduis pas de boucle sur toute la progression par réponse.
2. Le prototype envoie un message (nouveau type, par ex. `reponse`) avec le mot allemand visé et juste/faux. Pour « Trouve ! », le mot est la cible. Pour une question A2-C1, le mot est celui que la question fait travailler, s'il y en a un clairement (sinon ne rien compter : mieux vaut ne pas noter qu'enregistrer une révision fausse).
3. L'app retrouve le mot dans le corpus (attention aux articles, aux formes `aussi` et aux synonymes régionaux) et l'enregistre comme une révision, **seulement quand la scène est ouverte depuis la séance** (`seance=1`), pas en Découvrir ni depuis le tableau admin.
4. Ce que vaut une réponse juste au premier toucher, après une erreur, ou fausse : aligne-toi sur ce que fait déjà une carte. Explique ton choix dans le compte rendu.
5. Vérifier l'origine du message (le contrôle existe déjà dans le gestionnaire : garde-le).
6. Test : une page headless, une séance avec scène, trois réponses, et la preuve que l'état des trois mots a changé (et pas celui des autres).

## Chantier 2 — branche `corpus-mots-scenes` : les mots des scènes absents du corpus

Ces mots apparaissent dans les scènes mais pas dans `themes.json` (vérifie chacun avant d'ajouter, l'article et l'orthographe peuvent différer) :

- Classe : **die Armbanduhr, der Heizkörper, die Kreide** (der Schwamm et der Haken y sont déjà).
- Examen médical : **der Po** (ou das Gesäß : choisis le plus usuel pour un apprenant et mets l'autre en synonyme si la structure le permet), **die Unterhose** (elle est dans une question B1), **das Stethoskop**, **der Bauchnabel**.

Pour chacun : le bon thème et le bon niveau CECR, la traduction, l'exemple allemand + `exemple_fr` (et l'anglais, et toutes les langues que portent les autres mots du même thème : regarde un mot voisin et remplis **les mêmes clés**, aucune de moins). Puis, dans les points.json concernés, fais pointer les zones de l'image vers ces mots s'ils y sont seulement en texte libre.

L'audio (voix Aurora, ElevenLabs) ne peut pas se faire depuis le cloud : la clé est sur le PC. Liste dans le compte rendu les mots et les phrases d'exemple qui n'ont pas encore de fichier son, pour que le PC les génère.

Lancer `python tests/frequence.py --ecrire` si le vérificateur dit que `frequence.json` est en retard (fichier dérivé, jamais à la main).
