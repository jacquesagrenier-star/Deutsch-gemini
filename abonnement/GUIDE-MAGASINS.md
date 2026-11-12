# L'abonnement de Wortando : ce que Jacques fait dans les consoles

Rédigé le 11 nov. 2026 (v1165), pour le lancement avec l'**essai de 7 jours sans carte, géré par l'app** (modèle B, décision du 11 nov.), puis l'abonnement : **6,99 € / mois, 49,99 € / an** (9,99 / 69,99 $ CA ; grille complète du 2 nov. dans `decisions/DECISIONS.md`).

Rien ici ne demande de dépense. Aucune clé **secrète** ne doit jamais entrer dans le dépôt : seules les deux clés **publiques** du SDK RevenueCat (`goog_…`, `appl_…`) vont dans `index.html`, comme la clé Firebase.

## Comment les morceaux s'emboîtent

```
Compte Firebase (uid)  ──►  identifiant RevenueCat = le même uid
        │                         │
        │                 droit « premium »  ◄── Google Play : wortando_premium (mensuel, annuel)
        │                         │          ◄── App Store : deux abonnements auto-renouvelables
        │                         ▼
  app installée  ◄──── module RevenueCat (déjà dans les apps depuis le 30 oct.)
  site web       ◄──── jeton Firebase (extension RevenueCat de Firebase, étape E)
```

- **L'essai ne passe ni par Google ni par Apple** : l'app ouvre tout pendant 7 jours après la création du compte. Les magasins ne voient que l'achat, au 8e jour ou plus tôt si la personne le veut.
- **Un seul abonnement pour toutes les langues** (décision du 2 nov.).
- Tant que `ACCES.actif` vaut `false` dans `index.html`, rien ne change pour personne ; seul le compte admin peut essayer un achat de test.

---

## A. Google Play Console

1. **Monétiser → Abonnements → `wortando_premium`.**
   - Activer les deux **forfaits de base** : `mensuel` et `annuel` (bouton « Activer » de chaque forfait).
   - ⚠️ **NE PAS activer les offres `essai-7-jours` et `essai-7-jours-mensuel`.** L'essai est géré par l'app ; ces offres donneraient un second essai, avec carte, par-dessus le nôtre. Les laisser en brouillon (ou les supprimer).
   - Vérifier les prix pays par pays (zone euro 6,99 € / 49,99 €, Canada 9,99 / 69,99 $ CA, etc.). Rappel du 3 nov. : la cellule d'un pays prend le prix **TTC** ; le dialogue « Set prices » prend un prix **hors taxes**.
2. **Testeurs de licence** (Paramètres → Test de licence) : ajouter l'adresse Gmail de Jacques. Ses achats sont alors des achats de test, jamais facturés ; un abonnement mensuel s'y renouvelle toutes les 5 minutes.
3. **Accès de RevenueCat à Google Play** (une seule fois) :
   - Google Cloud (projet relié à la Play Console) → IAM → Comptes de service → créer `revenuecat` → Clés → Ajouter une clé JSON → télécharger le fichier.
     ⚠️ Ce fichier est un **secret** : il va dans RevenueCat (étape C.2) et dans `C:/Users/jacqu/.wortando/`, **jamais** dans le dépôt ni dans OneDrive.
   - Play Console → Utilisateurs et autorisations → Inviter l'adresse du compte de service, avec les droits : « Afficher les données financières », « Gérer les commandes et les abonnements ».
   - Google met jusqu'à 36 heures à rendre ces droits effectifs : le faire tôt.
4. **Notifications en temps réel** (recommandé) : RevenueCat → app Google → « Connect to Google » propose de créer le sujet Pub/Sub ; sinon, Play Console → Monétiser → Configuration de la monétisation → Notifications en temps réel pour les développeurs → coller le nom du sujet donné par RevenueCat.
5. Rappel ouvert depuis le 30 oct. : l'inscription au **programme des frais de service de 15 %** (Play Console → paramètres du compte de paiement / groupe de comptes).

## B. App Store Connect

0. ⚠️ **Préalable bloquant : le contrat « Paid Apps ».** Accords, taxes et banque → Paid Apps → accepter, puis formulaires fiscaux et compte bancaire. Il attend la correction de l'adresse Business (Ville-Marie) demandée au soutien d'Apple le 30 oct. **Sans ce contrat, les abonnements ne se chargent pas, même en bac à sable** : l'iPhone ne pourra rien vendre ni rien tester.
1. **App → Monétisation → Abonnements → créer un groupe** « Wortando Premium » (nom affiché localisé : fr, en, de, es au moins).
2. Dans ce groupe, **deux abonnements auto-renouvelables** :
   | Nom de référence | Identifiant du produit (définitif, ne se réutilise jamais) | Durée | Prix |
   |---|---|---|---|
   | Wortando mensuel | `wortando_premium_mensuel` | 1 mois | 6,99 € (zone euro), 9,99 $ CA, 6,99 $ US… |
   | Wortando annuel | `wortando_premium_annuel` | 1 an | 49,99 € (zone euro), 69,99 $ CA, 49,99 $ US… |
   - Prix : choisir les États-Unis comme pays de base (6,99 $ / 49,99 $, la conversion automatique d'Apple part du $ US, décision du 2 nov.), puis régler à la main la zone euro, le Canada, le Royaume-Uni, la Suisse, le Brésil et le Mexique sur la grille du 2 nov. (le point de prix Apple le plus proche si le montant exact n'existe pas).
   - Pour chacun : nom affiché et description localisés, **capture de l'écran d'abonnement** (pour la révision ; Claude la fournira), notes au réviseur.
   - **Pas d'offre d'introduction** (essai gratuit Apple) : l'essai est géré par l'app. Sauf si Apple refuse ce modèle : voir `abonnement/QUESTION-APPLE.md`, plan de repli.
3. **Clé d'achat intégré** (Utilisateurs et accès → Intégrations → Achats intégrés → générer une clé) : télécharger le `.p8`, noter l'« Issuer ID » et le « Key ID ». Le `.p8` est un **secret** : dans RevenueCat (C.2) et `C:/Users/jacqu/.wortando/`, jamais dans le dépôt.
4. **Notifications du serveur** : App → Informations sur l'app → Notifications du serveur App Store → coller l'adresse que RevenueCat donne (production et bac à sable), version 2.
5. **Testeur Sandbox** : Utilisateurs et accès → Bac à sable → Testeurs → créer une adresse de test (une adresse qui n'est pas un identifiant Apple existant).
6. Les premiers abonnements partent **avec une nouvelle version de l'app** (case « Achats intégrés et abonnements » de la page de version) : la 1.0 (compilation 11) envoyée le 27 oct. n'a pas le module d'achat. Voir H.

## C. RevenueCat (projet « Wortando », créé le 26 oct.)

1. **Apps** : vérifier qu'il y a bien une app **Google Play** (`com.wortando.app`) et une app **App Store** (bundle `com.wortando.app`).
2. **Identifiants** :
   - app Google : téléverser le JSON du compte de service (A.3) ;
   - app App Store : téléverser la clé d'achat intégré `.p8` avec son Issuer ID et son Key ID (B.3).
3. **Produits** (Product catalog → Products) : importer `wortando_premium:mensuel` et `wortando_premium:annuel` (Google ; identifiant = abonnement:forfait), `wortando_premium_mensuel` et `wortando_premium_annuel` (Apple).
4. **Droit** (Entitlements) : créer **`premium`** et y attacher les **quatre** produits. Ce nom est écrit dans le code (`REVENUECAT.droit`) : ne pas en choisir un autre sans le dire.
5. **Offre** (Offerings) : une offre `default`, marquée **Current**, avec deux paquets :
   - `$rc_monthly` (Monthly) → `wortando_premium:mensuel` + `wortando_premium_mensuel` ;
   - `$rc_annual` (Annual) → `wortando_premium:annuel` + `wortando_premium_annuel`.
   Le code choisit le paquet par son type (Monthly / Annual) : rien d'autre à configurer.
6. **Clés publiques du SDK** (Project settings → API keys) : copier la clé publique de l'app Google (`goog_…`) et celle de l'app Apple (`appl_…`) et les **donner au chef d'orchestre**. Elles sont publiques, faites pour être dans l'app : Claude les pose dans `REVENUECAT.cleAndroid` / `cleIos`. ⚠️ **Jamais la clé secrète `sk_…`.**
7. (Pour le web, étape E) Integrations → Webhooks : l'adresse et le secret que donnera l'extension Firebase.

## D. Firebase : les règles

Les règles de l'abonnement sont **fusionnées dans celles de l'audit de sécurité** (11 nov., `e85153f`) : une seule version à coller, `securite/firestore-corrige.rules`, expliquée dans `securite/REGLES-FIRESTORE.md`. Ce qu'elles garantissent pour l'abonnement :
- la personne ne peut **jamais** écrire `accesAVie` ni `accesJusqua` : seul l'admin les pose, dans `users/<uid>` ;
- elle n'écrit `essaiDebut` **qu'une fois**, et seulement à l'heure du serveur.

Même si une personne réécrivait `essaiDebut`, l'app garde le **plus tôt** de `essaiDebut` et de la date de création du compte (Firebase Auth) : l'essai ne peut que raccourcir.

## E. Le web (« on ne vend pas sur le web »)

Sur wortando.com, l'écran d'abonnement n'a pas de bouton d'achat ; il dit (texte proposé, dans les 11 langues) :

> **L'abonnement se prend dans l'app Wortando, sur ton téléphone. C'est le même compte partout : une fois abonné, tout s'ouvre aussi ici.**
> Google Play · App Store
> *Déjà abonné ? Ton accès suit ton compte : connecte-toi ici avec la même adresse.*

⚠️ La promesse « tout s'ouvre aussi ici » demande **l'extension Firebase de RevenueCat** (Firebase → Extensions → « Enable In-App Purchases with RevenueCat », gratuite, le projet est déjà en Blaze) :
- à l'installation : activer les **custom claims** (le droit `premium` est alors porté par le jeton Firebase, sous `revenueCatEntitlements`, que le code lit déjà) ;
- elle donne une adresse de webhook et un secret, à coller dans RevenueCat → Integrations → Webhooks ;
- coût : une petite fonction Cloud appelée à chaque événement d'abonnement, largement dans le gratuit de Blaze.

Sans l'extension, un abonné voit sur le web la version gratuite (dans l'app, tout marche). Dans ce cas, il faut retirer la deuxième phrase du texte : dire au chef laquelle des deux voies on prend.

## F. Ce que Claude fait ensuite, dans l'ordre

**Trois étapes à faire au moment de brancher les magasins** (décision du chef, 11 nov. : pas avant) :

- **Les clés publiques RevenueCat** : Jacques les copie depuis RevenueCat (C.5), `goog_…` et `appl_…`, et les donne au chef. Elles vont dans `REVENUECAT.cleAndroid` / `cleIos`. Jamais de clé `sk_…`.
- **La recompilation Android** avec `launchMode="singleTop"` (section H). Recommandée, pas obligatoire : la compilation 19 contient déjà le module d'achat.
- **La recompilation iPhone** (section H). OBLIGATOIRE pour vendre sur iPhone, et elle attend le contrat Paid Apps (B.1), toujours bloqué par l'adresse.

1. Recevoir les deux clés publiques → les poser dans `REVENUECAT` (une version de l'app, rien ne change pour personne : `ACCES.actif` reste `false`).
2. Achat de test par Jacques, compte admin, sur Android (testeur de licence) : Réglages → Administration → « Écran d'abonnement » → S'abonner. Puis « Restaurer un achat », puis résiliation dans Google Play. Même chose sur iPhone dès que la nouvelle compilation et le contrat Paid Apps existent.
3. **Le jour de la sortie** : `ACCES.lancement = "AAAA-MM-JJ"` (la date du jour), **puis** `ACCES.actif = true`, une version. Tout compte créé avant cette date reste gratuit à vie (promesse du 2 oct.).
4. **Les testeurs du Play Store et de TestFlight (4 mois offerts)** : dans la console Firebase, document `users/<uid>` de chacun, champ `accesJusqua` (texte) = la date de fin, par ex. `2027-03-31` (accès complet jusqu'à la fin de ce jour). Ensuite, essai fini → version gratuite ou abonnement. ⚠️ Mais un testeur dont le compte a été créé **avant** la sortie est déjà gratuit à vie : le champ ne sert qu'à ceux qui créent leur compte après.

## G. Les essais côté app (déjà construits, éteints)

- Tableau admin → **« Essai de 7 jours »** : JOUR 1, 5, 7, 8, 30, ARRÊTER. L'app se comporte sur l'appareil de l'admin comme un compte neuf au jour choisi (compte à rebours, bulle du jour 5, écran du 8e jour, version gratuite). Rien ne change pour les autres comptes.
- `node tests/essai.js` : jours 1, 5, 7, 8, 30, testeur à vie, 4 mois offerts, abonné, horloge du téléphone reculée, inertie avant la sortie.

## H. Les apps natives (dépôt `wortando-ios`, qui fait aussi Android)

Rien n'est à écrire dans les dépôts pour **brancher** l'achat : `@revenuecat/purchases-capacitor` 13.7.4 y est depuis le 30 oct. (`9d7bfd0`), la page lui parle par le pont de Capacitor (`Capacitor.Plugins.Purchases`), et les règles R8 de la branche `r8-android` le gardent déjà.

- **Android** : la compilation 19 (branche `r8-android`, `7deff54`) contient le module → **pas de recompilation obligatoire pour vendre.**
  Recommandé à la prochaine compilation Android : `android:launchMode="singleTop"` au lieu de `singleTask` dans `android/app/src/main/AndroidManifest.xml`. RevenueCat le conseille : avec `singleTask`, un achat qui fait quitter l'app (validation par l'appli de la banque, 3-D Secure) peut revenir annulé. À essayer avant : le bouton Retour et l'ouverture depuis une notification.
- **iPhone** : **recompilation obligatoire.** La 1.0 (compilation 11, envoyée le 27 oct.) a été faite avant l'ajout du module ; elle ne peut rien vendre (l'écran dirait « mets d'abord Wortando à jour »). Compiler depuis un commit qui contient `9d7bfd0` — `main`, ou mieux `r8-android` fusionnée dans `main` (elle garde l'achat dans `ios.includePlugins` et apporte le numéro de compilation dans le user agent). Aucune capacité Xcode à ajouter : l'achat intégré est ouvert d'office sur l'identifiant de l'app. Cette compilation part avec les deux abonnements (B.6).
- Le choix de la compilation iPhone dépend de la réponse d'Apple (`abonnement/QUESTION-APPLE.md`) : si Apple impose son offre d'introduction, rien ne change dans le natif non plus ; seule la page change (plan de repli décrit dans ce fichier, à construire seulement si Apple répond non).

## I. Ce qui reste à décider (par le chef, avec Jacques)

1. Le web : installer l'extension Firebase de RevenueCat (abonnés reconnus sur wortando.com), ou retirer la phrase « tout s'ouvre aussi ici » ?
2. La date de fin des 4 mois offerts aux testeurs des magasins (4 mois à partir de quand : la sortie, ou la fin du test ?).
3. Le texte des magasins mentionne-t-il l'essai ? Google demande que la fiche ne promette pas un essai « Google » qui n'existe pas : écrire « 7 jours d'accès complet offerts à l'inscription, sans carte ».
4. L'avantage « toutes les langues » (un abonnement pour toutes, 2 nov.) n'apparaît pas encore dans la liste de l'écran d'abonnement.
