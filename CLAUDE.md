# DeutschAI

Application web d'apprentissage du vocabulaire et de la grammaire allemande, destinée à des francophones. Interface en français, contenu en allemand.

## Dépôt

- GitHub : https://github.com/jacquesagrenier-star/Deutsch-gemini
- Branche principale : `main`

## Marque

- Nom retenu pour l'entreprise de cours de langue : **Wortando** (« Wort », mot en allemand, + « -ando », suffixe évoquant un geste répété jusqu'à devenir naturel). Choisi pour se prononcer sans effort en français, anglais et allemand.
- Vérifié disponible (20 août 2026) : domaines `wortando.com`, `.de`, `.ca`, `.fr` ; comptes `@wortando` sur Instagram et TikTok ; aucune marque déposée ni entreprise existante sous ce nom.
- Logo retenu (validé) : monogramme en W (encre pleine, #1C2430) surmonté de deux points ambre (#E8A23A) façon tréma allemand. Concept complet et rationale : voir l'artefact publié — https://claude.ai/code/artifact/0cef1150-b272-415d-aa02-4add8320a338
- Fichiers finaux dans `branding/` :
  - `wortando-app-icon.png` — icône seule, carré plein 1024×1024, fond papier opaque (pour icône iOS, pas de texte).
  - `wortando-logo-pale.png` — icône + mot « Wortando », fond transparent (pour les sections claires de l'app).
  - `wortando-logo-dark.png` — icône seule, trait clair, fond transparent (pour les sections foncées de l'app).

## Architecture

C'est une app **statique, sans build**, en un seul fichier HTML autonome :

- `index.html` — toute l'application (CSS et JS inline, pas de fichiers séparés, pas de bundler, pas de `npm install`). Ouvrir le fichier directement dans un navigateur suffit pour tester en local.
- Authentification via **Firebase Auth** (email/mot de passe), projet Firebase `deutschai-b6fbb`. La clé API Firebase dans le code est une clé cliente publique (normal pour Firebase web) — pas un secret à protéger comme un mot de passe.
- `AUTH_REQUIRED = true` dans le code : l'authentification est obligatoire pour utiliser l'app, avec inscription restreinte par **code d'invitation** (chaque code ne sert qu'une fois). L'écran d'authentification a deux onglets séparés « Se connecter » / « Créer un compte ».
- Un **tableau de bord admin** (visible seulement pour le compte administrateur, via les réglages) permet de générer/supprimer des codes d'invitation et de voir la progression des testeurs.
- La progression de l'utilisateur est synchronisée dans le cloud via **Firestore**.

## Données (important)

Les fichiers de données sont chargés **à l'exécution, directement depuis GitHub**, pas empaquetés dans le HTML :

```
https://raw.githubusercontent.com/jacquesagrenier-star/Deutsch-gemini/main/verbe.json
https://raw.githubusercontent.com/jacquesagrenier-star/Deutsch-gemini/main/adjectif.json
https://raw.githubusercontent.com/jacquesagrenier-star/Deutsch-gemini/main/themes.json
```

**Conséquence : un `git push` sur `main` met à jour les données en production immédiatement**, sans étape de déploiement séparée. Il n'y a pas d'environnement de test — toute modification poussée sur `main` est visible tout de suite par l'app.

Structure des fichiers JSON, organisés par niveau CECR (`A1`, `A2`, ...) :

- **`adjectif.json`** : liste d'adjectifs — `mot`, `traduction`, `exemple` (allemand), `exemple_fr` (traduction français).
- **`verbe.json`** : liste de verbes — `infinitif`, `traduction`, conjugaisons (`praesens`, `perfekt`, `praeteritum`, `konjunktiv2`), `exemple`/`exemple_fr` pour chaque temps.
- **`themes.json`** : thèmes de vocabulaire (ex. `Familie`) avec un id, un niveau, une icône SVG inline, et une liste de `mots`.

⚠️ **`Indexbackup.json`** malgré son extension `.json`, contient en fait du HTML (une ancienne sauvegarde de `index.html`). Ne pas essayer de le parser comme du JSON.

## Conventions pour les contributions

- Respecter la structure existante des entrées JSON (mêmes clés, mêmes niveaux CECR) lors de l'ajout de vocabulaire.
- Toujours fournir la paire allemand/français (`exemple` + `exemple_fr`, ou équivalent) pour rester cohérent avec les données existantes.
- Comme il n'y a pas de build ni de tests automatisés, valider les changements en ouvrant `index.html` dans un navigateur avant de pousser sur `main`.
- Le dossier local du projet est synchronisé via OneDrive (`Desktop/Mes Projets/DeutschAI`) — éviter les opérations git lourdes ou concurrentes qui pourraient entrer en conflit avec la synchronisation OneDrive.
