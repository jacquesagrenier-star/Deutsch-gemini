Tu travailles sur le dépôt `jacquesagrenier-star/Deutsch-gemini` : **Wortando**, une app web d'allemand (en ligne, avec une quinzaine de testeurs, camarades de cours de Jacques). Jacques est francophone : écris-lui en français, simplement.

## Le contexte (décidé le 8 oct. 2026)

L'app quitte GitHub Pages pour **Cloudflare Pages**, puis le dépôt deviendra **privé** (pour protéger le code et pour pouvoir tout y rassembler, afin que les sessions cloud voient tout ce que voit le PC).

- Aujourd'hui l'app est servie à `https://jacquesagrenier-star.github.io/Deutsch-gemini/`. Les apps iPhone et Android (Capacitor, projet `wortando-ios`, **hors de ta portée**) chargent cette même adresse.
- Adresse cible, **technique et définitive** : `https://deutsch-gemini.pages.dev/` (projet Cloudflare Pages déjà branché sur ce dépôt ; il fait déjà les prévisualisations de PR). Un nom de domaine de marque s'ajoutera **plus tard** par-dessus ; il n'est pas décidé, n'en mets aucun en dur.
- **Étape 1 faite (v717)** : `RACINE_DEPOT` dans `index.html` — les données viennent du dossier de la page, plus de `raw.githubusercontent.com` (repli seulement pour `file://`). Lis `CLAUDE.md` en entier avant tout : ses règles s'imposent (service worker qui n'intercepte que la page, CSS coupé en deux, `python tests/verifier.py` ET `node tests/syntaxe.js` avant chaque commit, pas de heredoc pour écrire du code).
- Plan de la suite : (2) Cloudflare en production + domaines autorisés Firebase — **Jacques le fait dans les consoles** ; (3) recompiler les apps avec la nouvelle adresse — Jacques ; (4) **rediriger l'ancien lien**, attendre que tous les testeurs aient la nouvelle version, rendre le dépôt privé ; (5) rassembler les sources ; (6) écrire la règle de travail des sessions cloud.

## Ta tâche : préparer les étapes 4 et 6, sans rien activer

### A. La redirection de l'ancien lien

Le jour J, le dépôt actuel sera renommé et rendu privé, et un **nouveau petit dépôt public nommé `Deutsch-gemini`** prendra sa place pour que l'ancienne adresse GitHub Pages continue de répondre. Prépare-en le contenu complet dans un dossier `demenagement/depot-redirection/` (il sera copié tel quel dans ce nouveau dépôt) :

1. `index.html` et `404.html` qui renvoient vers la même page sur `deutsch-gemini.pages.dev`, **en gardant le chemin, la requête et le fragment** (`/Deutsch-gemini/espanol/?x` → `/espanol/?x`, `/Deutsch-gemini/confidentialite.html` → `/confidentialite.html`, `/Deutsch-gemini/visuel/prototype/?scene=arztpraxis` → idem). `location.replace` + `<meta http-equiv="refresh">` + un lien visible, pour les navigateurs sans JS. `.nojekyll`.
2. **Le piège principal, à traiter sérieusement** : les testeurs qui ont installé l'app sur l'écran d'accueil ont un **service worker** (`firebase-messaging-sw.js`) enregistré sur l'ancienne adresse, qui sert `index.html` **depuis son cache**. Ils ne verraient jamais la page de redirection. Lis `firebase-messaging-sw.js` et le code d'enregistrement dans `index.html`, puis prévois la parade. Deux pistes, à évaluer toutes les deux :
   - **dans l'app elle-même** : une constante `ADRESSE_DEFINITIVE` dans `index.html`, **vide = inerte**. Remplie, l'app servie depuis `*.github.io` se remplace elle-même par la même page à cette adresse (garde-fou contre toute boucle ; ne jamais rediriger depuis `file://`, `localhost` ou `pages.dev`). Comme tous les testeurs auront la version qui la contient avant la fermeture, c'est sans doute la voie principale. **Écris-la dans `index.html`, inerte**.
   - **en filet de sécurité** dans le dépôt de redirection : un `firebase-messaging-sw.js` « de remplacement » qui, quand le navigateur le récupère, vide les caches, se désinscrit et recharge les onglets, pour qu'ils tombent sur la redirection. ⚠️ Il porte le même nom que celui des notifications : explique ce qu'on perd (les notifications sur l'ancienne adresse — elles n'ont plus de raison d'y être).
3. **Inventaire de ce que perd un testeur en changeant d'adresse.** Pour un navigateur, une nouvelle adresse est un nouveau site : `localStorage`, `sessionStorage`, IndexedDB et la session de connexion Firebase ne suivent pas. Mesure dans `index.html` (grep, donne les commandes) : quelles clés `localStorage` sont restaurées depuis Firestore après connexion, et lesquelles **ne vivent que sur l'appareil** et seraient perdues. Pour celles qui comptent, propose comment les sauver (les ajouter à la synchronisation avant le jour J, par exemple). Note aussi : chacun devra **retaper son mot de passe** — vérifie que « mot de passe oublié » fonctionne et dis-le.
4. `demenagement/JOUR-J.md` : la procédure pas à pas du jour J, dans l'ordre, avec pour chaque geste **qui le fait** (Jacques dans une console, ou une session Claude) et **comment vérifier** qu'il a marché. Inclure : renommer le dépôt actuel, le rendre privé, créer le dépôt de redirection, activer Pages dessus, remplir `ADRESSE_DEFINITIVE`, ce que deviennent les liens de `espanol/`, de la politique de confidentialité et du prototype des scènes (`baseScenes()` dans `index.html` contient encore une adresse `github.io` en dur : traite-la), et comment revenir en arrière si quelque chose casse.

### B. La règle de travail des sessions cloud (étape 6)

Ajoute à `CLAUDE.md` une section courte, « Travailler depuis une session cloud » : une branche par chantier, jamais de push sur `main` ; une pull request ; **le lien de prévisualisation Cloudflare** de la branche (vérifie le format exact des adresses de branche de Cloudflare Pages, sans l'inventer) donné à Jacques pour qu'il essaie sur son téléphone ; il répond « fusionne » ; pas de changement de numéro de version sur une branche (le PC le fait à la fusion, sinon les branches se marchent dessus). Dis aussi ce qu'une prévisualisation **ne permet pas** : la connexion Firebase n'y marche que si son adresse est autorisée dans la console, et Firebase n'accepte pas de joker — propose une adresse d'essai fixe (une branche dédiée, par exemple) que Jacques autorisera une fois.

## Règles

- **Nouvelle branche `demenagement-redirection`** depuis `origin/main`. **Ne pousse jamais sur `main`.** Ouvre une pull request vers `main` à la fin ; **ne la fusionne pas**.
- **Rien ne doit changer pour les testeurs** si la PR est fusionnée : `ADRESSE_DEFINITIVE` reste vide. Ne change pas le numéro de version.
- Les deux vérificateurs passent avant chaque commit. Teste ce qui peut l'être dans un navigateur sans tête : la page de redirection (chemins, requête, fragment) et la constante inerte puis remplie (sur un serveur local, en simulant l'hôte si besoin).
- Dépôt **public** aujourd'hui : aucun prix, aucun nom de testeur, aucune clé.
- `node tests/retours.js` ne peut pas tourner chez toi (la clé est sur le PC) : ne t'en soucie pas.

## Message final, en français, court

La branche et la PR ; ce que tu as préparé ; **ce que Jacques devra faire lui-même, et dans quel ordre** ; les clés `localStorage` qui seraient perdues ; ce que tu n'as pas pu vérifier.
