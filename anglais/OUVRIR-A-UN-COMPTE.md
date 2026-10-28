# Ouvrir l'anglais à un compte

Décidé le 28 oct. 2026 : Jacques veut ouvrir l'anglais à un proche. L'anglais reste un essai, mais l'admin peut maintenant l'ouvrir à **un compte précis**, et le refermer. Les autres comptes ne voient toujours rien.

## Comment ça marche

- Dans le tableau de bord de l'admin, chaque ligne de compte porte un bouton **« OUVRIR L'ANGLAIS »**, sur les lignes allemandes (DE) comme sur les espagnoles (ES). Il écrit `essais: ["anglais"]` dans le document `users/<uid>`, commun à toutes les langues, puis le recopie dans le résumé de la ligne (`resumes` ou `resumenesEs`). Une fois l'anglais ouvert, le bouton devient **« ANGLAIS OUVERT ✓ — RETIRER »**.
- Le compte peut entrer en anglais depuis l'allemand comme depuis l'espagnol. Le retour se fait toujours vers la langue de départ (`wortando_avantAnglais`) : **« ESPAÑOL — REVENIR À L'ESPAGNOL → »** ou **« DEUTSCH — REVENIR À L'ALLEMAND → »**. Un accès retiré renvoie aussi vers cette langue.
- L'anglais range sa progression à part : `wortandoEn_` sur l'appareil, `usersEn` / `resumesEn` dans Firestore. La progression espagnole (`wortandoEs_`, `usuariosEs`) et l'allemande ne sont pas touchées. Le champ `langueApprise` du compte n'est jamais écrit à « en » : sur un appareil neuf, un compte espagnol retrouve l'espagnol.
- Le code de l'app ne contient aucune adresse ni aucun nom (le dépôt est public). C'est le champ du compte qui décide.
- L'app du compte lit ce champ avec son document (`loadVhsKapitelAccessFlag`) et le retient sur l'appareil sous `wortando_essaisCompte`. La valeur est stockée avec l'uid et sans préfixe de langue, pour que la garde puisse la lire avant la réponse de Firestore.
- Si l'anglais est ouvert au compte, ses réglages montrent une carte **« English »** avec le bouton **« ENGLISH — APPRENDRE L'ANGLAIS → »**. En anglais, ce même bouton devient **« DEUTSCH — REVENIR À L'ALLEMAND → »**. L'admin, lui, garde son bouton dans Administration.
- `gardeEssaiJaponais()` laisse passer ce compte en `?apprendre=en`.
- Si l'admin retire l'accès, la lecture suivante du document vide cette mémoire et renvoie le compte vers l'allemand.
- `accorderLangueAuCompte()` compte désormais `en` et `ja` comme un choix fait sur l'appareil. Avant ce changement, un compte ouvert en `?apprendre=en` dont le document disait « de » repartait aussitôt en allemand.

## Ce que Jacques doit faire une fois : coller les règles Firestore

Ces règles permettent deux choses : écrire le nouveau champ `essais`, et garder la progression anglaise dans le nuage (`usersEn` / `resumesEn`). Sans elles :

- le bouton du tableau de bord affiche « Refusé par Firestore : colle d'abord les nouvelles règles » ;
- l'anglais marche, mais la progression reste sur le téléphone.

Étapes :

1. Ouvrir https://console.firebase.google.com/project/deutschai-b6fbb/firestore/rules
2. Tout sélectionner dans l'éditeur et le remplacer par le contenu entier de `firestore.rules` (à la racine du dépôt).
3. Cliquer **Publier**.

## Vérifié

Les essais ont été faits avec un compte **simulé**, sans aucun appel à Firebase : impossible de créer un vrai compte de test sans code d'invitation, sur la vraie base.

Le cas d'un compte espagnol passe 15 vérifications sur 15 : il part de l'espagnol avec une progression, ouvre l'anglais, revient, puis l'accès lui est retiré pendant qu'il est en anglais. À la fin, ses clés `wortandoEs_` sont identiques, sauf le journal des ouvertures de l'app, qui s'allonge à chaque ouverture. Le compte garde « es » et la ligne espagnole du tableau de bord écrit dans `resumenesEs`.

Le cas général passe 14 vérifications sur 14 :

- un compte sans accès n'a pas de carte ;
- un compte avec accès a la carte, et le bouton ouvre l'anglais ;
- l'admin n'a pas de carte ;
- en anglais, la garde laisse passer le compte et la carte ramène à l'allemand ;
- la mémoire d'un autre compte ne suffit pas ;
- un accès retiré renvoie vers l'allemand ;
- le bouton de l'admin écrit `essais` sans effacer un autre essai ouvert ;
- un compte non admin ne peut rien écrire.
