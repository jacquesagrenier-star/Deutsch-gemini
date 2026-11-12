# La question à Apple : un essai de 7 jours géré par l'app, sans achat intégré

Préparé le 11 nov. 2026 (décision du 11 nov. : « Vérifier d'abord la règle d'Apple sur un accès gratuit limité dans le temps géré par l'app »). **Rien n'est envoyé** : c'est Jacques qui l'envoie, depuis son compte développeur.

> ⏸ **En attente** (décision de Jacques, 11 nov., `decisions/DECISIONS.md`) : rien n'est envoyé à Apple au sujet de l'abonnement, et le contrat Paid Apps n'est pas signé, **tant que l'adresse de l'entreprise n'est pas corrigée chez Apple**.

## Pourquoi la question se pose

Ce que disent les règles d'Apple (App Review Guidelines, à relire sur la page en ligne avant l'envoi — la lecture du 11 nov. n'a pu en obtenir qu'un résumé fidèle, pas le texte mot pour mot) :

- **3.1.1** : débloquer des fonctions ou du contenu (abonnements, contenu premium, version complète) doit passer par l'achat intégré. Les apps **sans abonnement** peuvent offrir un essai gratuit limité dans le temps par un achat non consommable à 0 € nommé « XX-day Trial » ; avant le début de l'essai, l'app doit dire clairement sa durée, ce qui ne sera plus accessible à la fin et ce qu'il faudra payer ensuite.
- **3.1.2(a)** : les apps à **abonnement auto-renouvelable** peuvent offrir une période d'essai gratuite « en fournissant les informations prévues dans App Store Connect » — c'est-à-dire l'**offre d'introduction** d'Apple.

Notre modèle B — tout ouvert 7 jours après la création du compte, sans achat, puis l'écran d'abonnement ou la version gratuite — n'est décrit par aucune des deux phrases. Il peut être lu comme du contenu gratuit (permis) ou comme un essai qui contourne l'offre d'introduction (risque de refus 3.1.1 / 3.1.2). D'où la question, posée avant d'envoyer la version qui vend.

## Où l'envoyer

- **Contacter l'App Review** : https://developer.apple.com/contact/app-store/ (« Contact Us », sujet App Review ; c'est le lien que la page des règles donne pour « contacting App Review »). Se connecter avec le compte développeur.
- En plus, dans la prochaine version envoyée (celle qui contient les abonnements) : le même texte en résumé dans **App Review Information → Notes**, pour que le réviseur ait la réponse sous les yeux.
- Pour une réponse plus rapide, Apple propose aussi des consultations avec l'App Review (« Meet with Apple », rubrique App Store) quand des créneaux existent : à regarder sur https://developer.apple.com/events/ le jour de l'envoi.

## Le message (en anglais, prêt à copier)

> **Subject:** Guideline 3.1.1 / 3.1.2 — app-managed 7-day free access before a subscription
>
> Hello App Review team,
>
> We are preparing the first paid version of **Wortando** (Apple ID 6817122301, bundle ID com.wortando.app), a vocabulary and grammar app for learning German and Spanish. Version 1.0 is currently free; the next version will add two auto-renewable subscriptions (monthly and yearly) through In-App Purchase, managed with RevenueCat. Before submitting it, we would like to confirm that the following model complies with guidelines 3.1.1 and 3.1.2.
>
> **What we would like to do**
>
> 1. When a person creates an account (email and password, no payment information), all content is available for free for 7 days. No purchase, no payment method and no App Store transaction are involved during these 7 days. The 7 days are counted from the account creation date on our server, so the same rule applies on iPhone, Android and the web.
> 2. During these 7 days, the app shows how many days are left, and on day 5 a reminder (an in-app message, and a local notification if the person allowed notifications) says when the free period ends and what happens next.
> 3. On day 8, the app shows the subscription screen. The person can subscribe through In-App Purchase (monthly or yearly auto-renewable subscription), or close the screen and keep a **free version** with no time limit: a sample of every part of the app (10 words in each of five themes, 10 verbs, 10 adjectives, the first exercises of each grammar topic, a sample of each exam section). Words already studied during the 7 days keep coming back for review in the free version.
> 4. Nothing is ever unlocked by any other means than In-App Purchase: no codes, no external payment, no link to a website to pay. The subscription is only sold in the app (App Store on iPhone, Google Play on Android).
> 5. Before the free period starts, at account creation, the app will state its duration (7 days), what remains available afterwards (the free version) and the subscription prices.
>
> We do **not** plan to use an App Store introductory offer (free trial), because the 7 days are not linked to a purchase: they are free access given to every new account, on every platform, without asking for payment information.
>
> **Our questions**
>
> 1. Is this app-managed, time-limited free access to all content, followed by an In-App Purchase subscription or a permanent free version, acceptable under guidelines 3.1.1 and 3.1.2 for an app that sells auto-renewable subscriptions?
> 2. If it is not, would the following be acceptable: on iPhone only, an App Store introductory offer (7-day free trial) on both subscriptions, while the rest of the app (free version) stays as described?
> 3. Is there any wording you would require on the subscription screen or on the account creation screen about the 7 free days?
>
> Thank you for your help.
>
> Jacques Grenier — Wortando
> contact@wortando.com

## Le plan de repli : l'offre d'introduction d'Apple, sur l'iPhone seulement

Si Apple répond non (ou ne répond pas avant la sortie et qu'on ne veut pas risquer un refus) :

1. **App Store Connect** : sur les deux abonnements, une **offre d'introduction** « Essai gratuit, 1 semaine », pour les nouveaux abonnés. Apple montre lui-même la durée, le prix qui suivra et la date du premier paiement.
2. **Dans l'app, sur l'iPhone seulement** : pas d'essai géré par l'app ; un compte neuf commence dans la version gratuite, et l'écran d'abonnement dit « 7 jours gratuits, puis 49,99 € par an » avec un bouton « Commencer mes 7 jours gratuits » (les textes du premier écran, v690, qui existent encore dans les 11 langues : `abo_sous_titre`, `abo_bouton`, le calendrier `abo_jour7`). La carte est demandée par Apple dès le début de l'essai, contrairement à Android.
3. **Ce que ça coûte** : une règle de plus dans `infoAcces()` (sur iOS natif, pas d'état « essai » tiré de la date de création) et le choix du texte de l'écran selon le canal. Environ une demi-journée, plus la vérification. À ne construire que si la réponse est non.
4. **La cohérence entre appareils** : un compte créé sur Android puis ouvert sur l'iPhone garde l'essai de l'app (il a été donné au compte) ; un compte créé sur l'iPhone ne reçoit que l'essai d'Apple. L'essai d'Apple ne vaut qu'une fois par identifiant Apple et par groupe d'abonnements : RevenueCat le sait (`intro eligibility`).
5. **Google Play ne change pas** : les offres `essai-7-jours` y restent éteintes.

## À ajouter de toute façon (Apple comme Google)

La règle 3.1.1 demande qu'**avant le début d'un essai**, l'app dise sa durée, ce qui disparaît à la fin et ce qu'il faudra payer. Aujourd'hui, l'écran de création de compte n'en dit rien (le compte à rebours n'apparaît qu'à l'accueil). Proposition : une ligne sous « Créer un compte », visible seulement après la sortie :

> *7 jours d'accès complet offerts, sans carte. Ensuite : l'abonnement (6,99 € par mois ou 49,99 € par an) ou la version gratuite.*

À valider par Jacques (texte et emplacement) avant de l'écrire dans les 11 langues.
