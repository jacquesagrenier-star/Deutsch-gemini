# App Check et limites : ce que Jacques clique (préparé le 12 nov. 2026)

**Rien ne s'active avant le feu vert du chef.** L'ordre compte : d'abord la
clé (étape 1), ensuite l'app qui la porte (une version publiée par Claude),
enfin l'enregistrement dans Firebase (étape 2). Aucune étape ne bloque qui
que ce soit : App Check reste en **surveillance** tant que personne ne clique
« Enforce » (étape 5, plus tard, sur les chiffres).

## Pourquoi

Avec le mode sans compte, n'importe qui obtient un compte Firebase en un clic,
depuis l'app ou par un script qui recopie la clé publique du code. Les règles
Firestore disent **qui** écrit **quoi**. App Check ajoute : **depuis notre
app**, servie par wortando.com. Les apps iPhone et Android chargent cette
même page : elles sont couvertes sans recompilation.

## 1. Créer la clé reCAPTCHA (Google Cloud, 5 minutes)

1. Ouvrir <https://console.cloud.google.com/security/recaptcha?project=deutschai-b6fbb>.
   Si la page demande d'**activer l'API reCAPTCHA Enterprise** : « Activer ».
2. « **Créer une clé** » (Create key).
   - Nom : `Wortando web`
   - Type d'application : **Site Web** (Web)
   - Domaines, un par ligne :
     `wortando.com`, `deutsch-gemini.pages.dev`, `jacquesagrenier-star.github.io`, `localhost`
     (un domaine couvre ses sous-domaines : les prévisualisations Cloudflare sont comprises)
   - **Ne pas** cocher l'utilisation d'un test (« challenge ») : un score
     invisible seulement, personne n'a d'images à cliquer.
3. « Créer ». **Copier l'identifiant de la clé** (une suite de lettres et
   chiffres, commence souvent par `6L`). Ce n'est pas un secret : il ira dans
   le code de la page.
4. **Le prix** : la page affiche le palier gratuit (10 000 évaluations par mois
   au 12 nov. 2026, à relire à ce moment-là). Avec un jeton valable un jour,
   il faut compter environ une évaluation par appareil actif et par jour.
   Le noter et l'envoyer au chef avec la clé.
5. Envoyer la clé au chef. Claude la met dans `APP_CHECK_CLE` (index.html) et
   publie une version, selon la procédure habituelle.

## 2. Enregistrer l'app dans App Check (Firebase, après la publication)

1. Ouvrir <https://console.firebase.google.com/project/deutschai-b6fbb/appcheck>.
2. Onglet **Apps** → l'app web (`1:915434419015:web:…`) → **reCAPTCHA Enterprise**.
3. Coller l'identifiant de la clé de l'étape 1.
4. Durée de vie du jeton : **1 jour** (moins d'évaluations, donc moins de coût).
5. **Enregistrer**. **Ne cliquer « Enforce » nulle part.**

## 3. Alerte de budget (Google Cloud, 2 minutes)

Le compte est sur Blaze (paiement à l'usage) : une alerte prévient d'une
dépense anormale, quelle qu'en soit la cause.

1. Ouvrir <https://console.cloud.google.com/billing> → le compte de
   facturation de deutschai-b6fbb → **Budgets et alertes** → « Créer un budget ».
2. Projet : deutschai-b6fbb. Montant : celui que Jacques juge normal par mois
   (par exemple 10 $). Seuils d'alerte : 50 %, 90 %, 100 %. Courriel : le sien.
3. Enregistrer. (Une alerte ne coupe rien : elle prévient.)

## 4. Quota d'inscriptions par adresse IP (Firebase Authentication, 1 minute)

1. Ouvrir <https://console.firebase.google.com/project/deutschai-b6fbb/authentication/settings>.
2. Section **Protection contre l'utilisation abusive** / « User actions » /
   **Quota d'inscription** (selon l'intitulé du moment).
3. Noter la valeur actuelle et l'envoyer au chef (la valeur par défaut de
   Firebase est de 100 créations de compte par heure et par adresse IP).
   Ne rien changer sans en parler : une classe entière derrière la même
   connexion (le cours de Marina) crée plusieurs comptes d'un coup.

## 5. Plus tard : imposer (après 7 à 14 jours de surveillance)

Dans **App Check → APIs**, Firebase montre pour **Cloud Firestore** et
**Authentication** la part des demandes vérifiées. On regarde ensemble :
- surtout les apps iPhone et Android (reCAPTCHA dans une vue web d'app, le
  point à surveiller) ;
- si la part non vérifiée vient de vieux téléphones ou de nos essais.

Puis, sur décision : « **Enforce** » sur Cloud Firestore d'abord,
Authentication ensuite. **Retour en arrière** : « Unenforce », effet en
quelques minutes. Si les apps natives montrent trop de rejets, la parade est
App Attest (iPhone) et Play Integrity (Android), par une recompilation
(phase 2 du plan) : pas avant d'avoir vu les chiffres.

## Ce que fait le code (pour mémoire)

- `index.html` : `APP_CHECK_CLE` vide = **rien ne change** (le module App
  Check est chargé, pas initialisé ; `window.appCheckEtat` vaut « inerte »).
  Remplie : App Check s'initialise avant tout autre service Firebase, en
  reCAPTCHA Enterprise invisible, jeton renouvelé seul. Sur `localhost` /
  `127.0.0.1` : le fournisseur de débogage (les parcours et sondes ne passent
  pas par reCAPTCHA). Une erreur d'App Check ne bloque jamais l'app.
- Les règles Firestore (`securite/firestore-corrige.rules`, une seule version
  à coller, voir `securite/REGLES-FIRESTORE.md`) bornent ce qu'un compte peut
  écrire : les clés permises dans chaque document de progression, leur type,
  la taille des petits champs. `tests/verifier.py` refuse tout push où l'app
  écrirait une clé que les règles ne permettent pas.
