# Jour J : fermer l'ancienne adresse

Préparé le 8 octobre 2026 (branche `demenagement-redirection`). **Rien n'est activé** :
`ADRESSE_DEFINITIVE` est vide dans `index.html`, et le dépôt de redirection n'existe
encore que dans `demenagement/depot-redirection/`.

- Ancienne adresse : `https://jacquesagrenier-star.github.io/Deutsch-gemini/`
- Adresse définitive (technique) : `https://deutsch-gemini.pages.dev/`

Qui fait quoi : **Jacques** = un geste dans une console (GitHub, Firebase,
Cloudflare, Google Cloud, App Store, Play) ; **Claude** = une session Claude
(branche + pull request, ou sur le PC).

---

## Le principe, en deux voies

Une nouvelle adresse est un nouveau site pour le navigateur. Le piège : un testeur
qui a installé l'app a un service worker (`firebase-messaging-sw.js`) qui sert
`index.html` **depuis le cache du téléphone**. Une page de redirection posée à
l'ancienne adresse, il ne la verrait pas — essai fait dans Chromium : après la
mise en place de la redirection, un rechargement affiche encore l'ancienne app.

1. **Voie principale, dans l'app** : la constante `ADRESSE_DEFINITIVE` (dans le
   `<head>` d'`index.html`). Remplie, l'app servie depuis `*.github.io` se remplace
   par la même page à la nouvelle adresse, avant le premier rendu, en gardant la
   requête et le fragment. Elle ne fait jamais rien depuis `file://`, `localhost`,
   `pages.dev`, un futur domaine, ni dans l'app native. Comme chacun aura cette
   version dans son cache **avant** la fermeture, c'est elle qui déménage les gens.
2. **Filet de sécurité, dans le dépôt de redirection** : pour ceux qui n'auraient
   pas ouvert l'app entre-temps.
   - `index.html` = `404.html` : renvoi vers la même page sur `pages.dev`
     (`location.replace`, balise `refresh` pour les navigateurs sans JS, lien visible).
   - `firebase-messaging-sw.js` et `espanol/sw.js` **de remplacement** : le
     navigateur re-télécharge le fichier du service worker à la navigation (au plus
     tard toutes les 24 h) ; la nouvelle version vide les caches, se désinscrit et
     recharge les onglets, qui tombent sur la redirection. Essai Chromium :
     cache `wortando-page-v1` présent → après mise à jour : 0 cache, 0 inscription,
     page de redirection affichée.
     ⚠️ **Ce qu'on perd** : les notifications sur l'ancienne adresse (c'est le
     même nom de fichier, et la désinscription coupe l'abonnement push). Elles
     n'ont plus de raison d'y être : sur la nouvelle adresse, la personne les
     réactive — un nouveau site redemande de toute façon la permission.
   - `version.json` = 999999 : une ancienne app encore ouverte voit « nouvelle
     version », recharge avec `?v=…`, ce qui court-circuite son cache.

---

## Ce que perd un testeur en changeant d'adresse

`localStorage`, `sessionStorage`, IndexedDB et la session Firebase restent attachés
à l'ancienne adresse.

**1. Tout le monde devra retaper son mot de passe.** « Mot de passe oublié » marche
(`envoyerReinitialisation()` dans `index.html`) : le lien de retour est l'adresse
courante (`location.origin + location.pathname`), donc `pages.dev` une fois
déménagé. Si ce domaine n'est pas autorisé dans Firebase, le code renvoie quand
même le courriel, sans adresse de retour (page Firebase en anglais, le mot de passe
se change quand même). Un lien de réinitialisation reçu *avant* le jour J, qui
pointe vers github.io, arrive entier grâce à la redirection (requête gardée — essai
fait avec `?mode=resetPassword&oobCode=…`).

**2. Les clés `localStorage`.** Mesure : `python demenagement/inventaire_cles.py`
(lit les corps de `syncProgressToCloud` et `restoreProgressFromCloud`). Commandes
brutes équivalentes :

```
grep -oE 'localStorage\.(get|set|remove)Item\([^,)]+' index.html | sort | uniq -c
grep -n 'const [A-Z_]*\(KEY\|CLE\)[A-Z_]* *= *"deutschAI_' index.html
```

Résultat du 8 octobre (v717) : 42 clés, **12 reviennent du nuage** après connexion —
la progression (`progress_v4`), XP, série et gels, objectif du jour, jours
travaillés, badges, mosaïque, grammaire, mon vocabulaire, mots demandés, découverte
guidée. Le reste ne vit que sur l'appareil :

| Ce qui serait perdu | Clé | Gravité |
|---|---|---|
| **Le niveau de la séance du jour** (repart en A1) | `niveauSeance` | ⚠️ à sauver : un testeur B1 recevrait des mots A1 |
| **L'historique des retours** | `retours` | ⚠️ **pire qu'une perte**, voir ci-dessous |
| Étapes du départ, séances des 7 jours, journal des versions, synonymes écartés | `parcours`, `seances`, `journalVersion`, `synonymesEcartes` | ⚠️ même mécanisme que `retours` |
| Langue de l'interface (redevinée d'après le téléphone) | `uiLang` | moyen : sauvée, jamais relue |
| Niveau déclaré à l'accueil, portée choisie, niveau de l'anneau d'accueil | `niveauDeclare`, `porteeNoms`, `homeLevel` | faible, se rechoisit |
| Thème, voix, musique, réglages d'écoute, notifications | `theme`, `voiceChoice`, `laisserMusique`, `ecoute`, `notificationsEnabled` | faible, réglages |
| Cartes « clé » vues, mots neufs du jour, scène faite, aperçu gratuit, essais coupés | `cleVues3`, `neufsDuJour`, `sceneFaite`, `apercuGratuit`, `essaisCoupes` | faible, compteurs du jour |
| Journaux techniques, brouillon de retour, `setupDone`, `onboardingSeen`, `masteryLog`, `dailyActivity` | — | sans conséquence (`setupDone` se repose seul à la connexion) |

⚠️ **Le vrai danger : les champs « sauvés mais jamais relus » sont ÉCRASÉS.** La
sauvegarde écrit `retoursUsager: localStorage.getItem("deutschAI_retours") || ""`
avec `{ merge: true }`. Sur la nouvelle adresse, le localStorage est vide : la
première sauvegarde remplace **l'historique des retours dans Firestore par une
chaîne vide**. Même chose pour `parcoursJson`, `seancesJson`,
`journalVersionJson` et `synonymesEcartes`. Ce n'est pas nouveau (un changement
d'appareil le fait déjà), mais le jour J le ferait **pour tout le monde le même jour**.

**Parade proposée (chantier à part, Claude, avant de remplir la constante)** : dans
`restoreProgressFromCloud`, recopier ces champs vers le localStorage quand la clé
locale est vide (`retoursUsager` → `deutschAI_retours`, `parcoursJson`,
`seancesJson`, `journalVersionJson`, `synonymesEcartes`), et ajouter
`niveauSeance` (et `uiLang`, déjà envoyée sous `langueInterface`) à la
sauvegarde + restauration, sur le modèle de `dailyGoalTarget` (« seulement si
absent localement »). En attendant, avant le jour J : `node tests/retours.js --tout`
sur le PC pour garder une copie des retours.

---

## Avant le jour J

| # | Geste | Qui | Vérifier |
|---|---|---|---|
| A1 | ✅ **Fait le 8 oct.** (la production suivait `staging`, figée en v260 ; passée sur `main`). Cloudflare Pages en production sur `main` (étape 2). | Jacques (Cloudflare) | `https://deutsch-gemini.pages.dev/version.json` affiche le même numéro que github.io. |
| A2 | ✅ **Fait le 8 oct.** : `deutsch-gemini.pages.dev` et `essai.deutsch-gemini.pages.dev` autorisés ; la clé API répond aussi avec le référent pages.dev (vérifié par l'API Identity Toolkit). Ajouter `deutsch-gemini.pages.dev` aux **domaines autorisés** Firebase (Authentication → Paramètres). Si la clé API a des **restrictions de référent** (Google Cloud → Identifiants), y ajouter `https://deutsch-gemini.pages.dev/*`. | Jacques (Firebase, Google Cloud) | Sur pages.dev : se connecter, puis « mot de passe oublié » → le lien du courriel ramène sur pages.dev, page traduite. |
| A3 | Apps iPhone et Android recompilées sur la nouvelle adresse (étape 3), et installées par les testeurs. ⚠️ Une **ancienne** app native resterait sur github.io : la constante ne s'y active pas (changer d'hôte y ouvrirait Safari), et après fermeture elle tomberait sur la page de redirection, qui ouvrirait le navigateur. | Jacques | `node tests/versions.js` : les ouvertures `natif: true` portent la nouvelle version. |
| A4 | ✅ **Fait le 8 oct. (v721, espagnol v37).** Icône du service worker relative à sa portée ; les 4 adresses de `espanol/index.html` en `../` (corrigées À LA MAIN dans la copie publiée : `fork.py` ancre encore sur `BASE_DE` = l'ancienne adresse raw et devra les reproduire à la prochaine régénération, de toute façon cassée par 90 versions de retard). Reste seulement le repli `file://` de `RACINE_DEPOT`, voulu. Plus aucune adresse `raw.githubusercontent.com` : l'icône des notifications dans `firebase-messaging-sw.js` (ligne `const ICONE`, à remplacer par `new URL("branding/wortando-app-icon.png", self.registration.scope).href`), les 5 de `espanol/index.html`, et le repli `file://` de `RACINE_DEPOT` (une fois privé, tester en local par `python -m http.server`, pas en ouvrant le fichier). | Claude | `grep -rn raw.githubusercontent --include=*.html --include=*.js .` ne trouve plus que des commentaires. |
| A5 | ✅ **Fait le 8 oct.** v718 : les cinq champs écrasés sont fusionnés à la restauration (`restoreProgressFromCloud`, `fusionnerRetoursDuNuage`). v720 : `niveauSeance` sauvé et restauré, `langueInterface` restaurée, tous deux « seulement si absent localement ». La parade des clés ci-dessus (restauration des champs écrasés + `niveauSeance`). | Claude | Navigateur privé sur pages.dev, connexion avec un compte de test : les retours et le niveau reviennent ; Firestore garde `retoursUsager` après la première sauvegarde. |
| A6 | Prévenir les testeurs : nouvelle adresse, mot de passe à retaper, notifications à réactiver. | Jacques | — |
| A7 | **Remplir la constante** : `const ADRESSE_DEFINITIVE = "https://deutsch-gemini.pages.dev/";` (https, barre finale) + numéro de version, publier. Désormais, ouvrir l'ancienne adresse déménage. | Claude (PR) → Jacques fusionne | `python demenagement/verifier_redirection.py` dit l'adresse ; sur le téléphone, ouvrir l'ancienne icône → on arrive sur pages.dev. |
| A8 | Attendre que chacun soit passé. | Jacques | `node tests/parcours.js` / `versions.js` : chaque compte actif a ouvert une version ≥ celle d'A7 (une version qui contient la constante ne peut plus se sauvegarder depuis github.io : elle en part avant de démarrer). |

## Le jour J, dans l'ordre

| # | Geste | Qui | Vérifier |
|---|---|---|---|
| J1 | Renommer le dépôt `Deutsch-gemini` (Settings → General → Repository name), par ex. `wortando-app`. | Jacques (GitHub) | La page du dépôt s'ouvre sous le nouveau nom. L'ancienne adresse GitHub Pages ne répond plus (normal, quelques minutes). |
| J2 | ⚠️ **Tout de suite** : changer l'adresse du dépôt partout où elle est écrite. Sur le PC : `git remote set-url origin https://github.com/jacquesagrenier-star/wortando-app.git`. Vérifier aussi : projet Cloudflare Pages (toujours lié ?), environnement des sessions cloud et routines Claude, `CLAUDE.md` (« Dépôt »). **Pourquoi d'abord** : dès que J4 recrée un dépôt nommé `Deutsch-gemini`, GitHub cesse de rediriger l'ancien nom — un `git push` resté sur l'ancienne adresse enverrait le code de l'app dans le dépôt **public** de redirection. | Jacques (PC, Cloudflare, claude.ai) | `git remote -v` montre le nouveau nom ; un petit push sur une branche déclenche une prévisualisation Cloudflare. |
| J3 | Rendre le dépôt renommé **privé** (Settings → Danger Zone → Change visibility). | Jacques (GitHub) | Déconnecté, `https://github.com/jacquesagrenier-star/wortando-app` → 404 ; `https://deutsch-gemini.pages.dev/` charge toujours ses mots (les données viennent d'à côté de la page, v717). |
| J4 | Créer un dépôt **public** `Deutsch-gemini` et y copier **le contenu** de `demenagement/depot-redirection/` (y compris `.nojekyll`), à la racine. | Jacques (GitHub, ou glisser-déposer « Add file → Upload ») ou Claude | Le dépôt montre `index.html`, `404.html`, `firebase-messaging-sw.js`, `espanol/`, `version.json`, `.nojekyll`, `README.md`. |
| J5 | Activer Pages sur ce dépôt : Settings → Pages → Deploy from a branch → `main` / `(root)`. | Jacques (GitHub) | Après ~1 min, ouvrir chacune de ces adresses : elles doivent arriver sur la même page de pages.dev (voir « Les liens » ci-dessous). |
| J6 | Mettre à jour les adresses publiées ailleurs : politique de confidentialité dans App Store Connect et Google Play Console (`https://deutsch-gemini.pages.dev/confidentialite.html`), tout lien partagé aux testeurs. | Jacques | Le lien des fiches de store ouvre la politique. |

Adresses à essayer en J5 (navigateur privé, puis sur un téléphone qui avait l'ancienne icône) :

```
https://jacquesagrenier-star.github.io/Deutsch-gemini/                       -> https://deutsch-gemini.pages.dev/
https://jacquesagrenier-star.github.io/Deutsch-gemini/espanol/?x             -> https://deutsch-gemini.pages.dev/espanol/?x
https://jacquesagrenier-star.github.io/Deutsch-gemini/confidentialite.html   -> https://deutsch-gemini.pages.dev/confidentialite.html
https://jacquesagrenier-star.github.io/Deutsch-gemini/visuel/prototype/?scene=arztpraxis -> idem sur pages.dev
https://jacquesagrenier-star.github.io/Deutsch-gemini/version.json           -> {"version": 999999} (voulu)
```

## Les liens

- **`espanol/`** : servi par pages.dev à `/espanol/` comme aujourd'hui ; l'ancien lien y
  arrive (chemin gardé). Son service worker `espanol/sw.js` est remplacé comme celui
  de l'app. Il n'a pas de constante `ADRESSE_DEFINITIVE` : ses utilisateurs passent
  par le filet (service worker de remplacement + `version.json` à 999999). Ses
  adresses `raw.githubusercontent.com` doivent être corrigées avant J3 (A4).
- **Politique de confidentialité** : `confidentialite.html` arrive sur pages.dev
  (chemin gardé) ; l'adresse est à changer dans les deux stores (J6).
- **Prototype des scènes** : `baseScenes()` fabrique l'adresse à côté de la page
  quand elle est servie en http(s) — rien à faire sur pages.dev. Son **repli** (app
  hors http, par ex. Capacitor sans `server.url`) contenait github.io en dur : il suit
  maintenant `ADRESSE_DEFINITIVE` quand elle est remplie, et la vérification d'origine
  des messages de la scène suit d'elle-même (`new URL(baseScenes()).origin`).
- **Texte du tableau de bord admin** (`admin_deploy_desc`, 6 langues) : mentionne
  encore github.io et netlify ; cosmétique, à refaire après coup.

## Revenir en arrière

- **Avant J1** (seule la constante est remplie) : la remettre à `""` et publier.
  Les gens déjà passés sur pages.dev y restent, ce qui ne casse rien — c'est la même
  app, les mêmes données.
- **Après J4/J5** : supprimer (ou renommer) le dépôt de redirection, renommer le
  dépôt de l'app en `Deutsch-gemini`, le rendre public, réactiver Pages
  (`main` / root), et refaire `git remote set-url` sur le PC. Les téléphones qui ont
  reçu le service worker de remplacement n'ont plus de worker ni de cache :
  l'app réinscrit le sien à la visite suivante (`enregistrerServiceWorker()`), rien à faire.
- **Si pages.dev tombe** : rien ne dépend de github.io pour la servir ; voir le
  tableau de bord Cloudflare (déploiements → revenir au précédent).

## Ce qui n'a pas pu être vérifié depuis la session cloud (8 oct.)

- Les adresses réelles : le réseau de la session refusait `pages.dev` et `github.io`.
  Les essais ont simulé les deux hôtes dans Chromium sans tête (redirection : 9 cas ;
  constante vide, remplie, sans boucle depuis pages.dev ; service worker de remplacement).
- Que le projet Cloudflare reste lié après le renommage (J2) — à constater.
- Le comportement exact de Safari iOS et de l'app installée sur l'écran d'accueil :
  les essais sont sur Chromium. La mise à jour du fichier du service worker est
  standard, mais iOS met parfois longtemps à la faire — d'où la constante comme voie principale.
