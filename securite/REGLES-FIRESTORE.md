# Règles Firestore corrigées (11 nov. 2026)

Audit de lancement, point 1. Les règles sont **EN LIGNE depuis le 12 nov. 2026,
15 h 03** : Jacques a collé le fichier
[`firestore-corrige.rules`](firestore-corrige.rules), **en entier**, dans la
console (ses trois vérifications passées : liste des testeurs, « OUVRIR
L'ANGLAIS » puis « RETIRER », sauvegarde « il y a quelques secondes »).
[`../firestore.rules`](../firestore.rules) en est la copie exacte (ce qui est
en ligne). Les anciennes règles sont gardées hors du dépôt, dans
`C:\Users\jacqu\.wortando\regles-console-2026-11-12-avant.txt` : pour revenir
en arrière, les recoller et « Publier ». Toute correction future se fait dans
les deux fichiers à la fois, puis se colle.

## Pourquoi

Le tableau de bord admin affiche ce que chaque compte écrit dans son
« résumé » : prénom, adresse, appareil, retours, mots demandés, compteurs. Les
règles actuelles laissent chacun y écrire **n'importe quoi** : un prénom de
mille caractères, du code à la place d'un nombre, l'adresse d'un autre testeur.
Elles laissent aussi chacun s'ouvrir lui-même un essai réservé (l'anglais, les
examens) ou les chapitres VHS, et — ce que relève la session de l'abonnement
(section D de `abonnement/GUIDE-MAGASINS.md`, fusionnée ici le 11 nov.) — se
poser `accesAVie` ou `accesJusqua` dans `users/<uid>`, donc **s'offrir
l'abonnement**, ou réécrire le début de son essai de 7 jours. Et un compte peut se créer sans code
d'invitation (la vérification se fait dans l'app, pas chez Firebase).

L'app est corrigée de son côté (version de ce correctif : tout texte venu d'un compte s'affiche
comme du texte). Les règles ferment la porte du côté de Firebase.

## Ce qui change

| | Avant | Après |
|---|---|---|
| Qui est l'admin | celui dont l'adresse est celle de Jacques | le compte de Jacques lui-même (son identifiant, qui ne se choisit pas) |
| Résumés | n'importe quel champ, n'importe quel contenu | les 13 champs que l'app écrit, chacun de son type et de sa taille |
| Adresse dans le résumé | libre | forcément celle du compte connecté |
| S'ouvrir un essai ou les VHS | possible | refusé : seul l'admin les ouvre |
| S'offrir l'abonnement (`accesAVie`, `accesJusqua`) | possible | refusé : seul l'admin les pose, dans `users` ; personne ne peut les écrire dans les autres langues ni dans les résumés |
| Début de l'essai (`essaiDebut`) | libre | écrit une seule fois, à l'heure du serveur ; ni réécrit, ni effacé, ni posé par l'admin |
| Documents de progression (`users`, `usuariosEs`, `usersEn`, `usersPt`, `usersJa`) | n'importe quelle clé, n'importe quel contenu jusqu'à 1 Mio | les clés que l'app écrit (`champsProgression()`), compteurs en nombres, dates en dates, adresse, prénom et appareil bornés ; les gros champs (vocabulaire, retours, journal) seulement par le 1 Mio de Firestore |
| Codes d'invitation, lectures | inchangés | inchangés |

Bornes des résumés : prénom 60 caractères, retours 20 000, mots demandés 150,
appareil 20, version 10, langue 10, compteurs entre 0 et 10 millions.
Les plus grands mesurés le 11 nov. : prénom 15, retours 11 917. L'app coupe
déjà le résumé à ces bornes (depuis ce correctif) : une écriture normale n'est jamais refusée.

**Documents de progression** (12 nov., avec le mode sans compte : un uid
s'obtient en un clic). Mesure en lecture seule le 12 nov. : 56 documents, le
plus gros 319 Ko (l'ancienne carte `progress`, que l'app efface), médiane
3,8 Ko, au plus 47 clés. Les 41 clés de la sauvegarde sont identiques sur main
et sur les cinq branches en file.
- ⚠️ **Une clé ajoutée à la sauvegarde doit l'être à `champsProgression()`**,
  sinon toute la sauvegarde de chacun est refusée, sans message.
  `tests/verifier.py` le contrôle avant chaque push (« cles Firestore »).
- ⚠️ **Firestore n'évalue pas plus de 1 000 expressions par requête.** Une
  sauvegarde complète la dépassait dans une première version (le banc l'a vu :
  toute la sauvegarde refusée). Marge mesurée : 10 contrôles de champ de plus
  passent, 15 non ; une clé de plus dans la liste ne coûte presque rien (100
  essayées, et 25 clés réellement écrites en plus). Ne pas ajouter de contrôle
  sans relancer le banc.

## Éprouvé avant d'être proposé

Dans l'émulateur Firebase local (un projet fictif, rien n'est parti vers le
vrai Firebase), 245 cas, avec le SDK de l'app (146 pour l'audit, 49 pour
l'abonnement, 16 pour le mode sans compte, 30 pour la forme des documents de
progression, 4 pour les codes d'invitation utilisés) :

- **Nouvelles règles : 245 sur 245.** Toutes les écritures normales passent
  (inscription, sauvegarde, résumé, notifications, suppression du compte,
  boutons admin, « Reconstruire les résumés », codes d'invitation, début de
  l'essai écrit par l'app, accès offert par l'admin puis sauvegarde ordinaire,
  compte sans compte, la sauvegarde réelle complète dans les cinq langues,
  un compte ancien avec ses clés d'autrefois),
  et toutes les attaques sont refusées.
- **Anciennes règles (en ligne jusqu'au 12 nov., 15 h 03) : 114 cas sur 241 donnent un autre résultat** (attaques qui passent (prénom trop long, compteur en
  texte, champ inconnu, adresse d'un autre, essai ou VHS auto-attribué,
  accès à vie ou 4 mois offerts à soi-même, début d'essai réécrit, clé
  inconnue de 900 000 caractères dans une progression…, et les écritures du
  mode sans compte, qu'elles ne connaissent pas).
- **Codes d'invitation utilisés (12 nov. 2026)** : les règles en ligne depuis
  15 h 03 laissent l'admin supprimer un code utilisé (244 sur 245, seul échec
  « l'admin supprime un code utilisé : refusé »). Un code utilisé est la seule
  preuve du testeur à vie (`usedBy == uid`) : `allow delete: if isAdmin() &&
  resource.data.used != true;` le refuse, l'app aussi (`deleteInviteCode`).

Le banc d'essai se relance ainsi (Java et Firebase CLI sont installés) :
`securite/essai-regles/` → voir son `LISEZ-MOI.md`.

## Quand coller

**Après** la publication de la v1180 (App Check inerte et le garde-fou des clés ; l'app
qui coupe le résumé aux bornes est en ligne depuis la v1165).
Avant, une vieille version ouverte sur un téléphone pourrait encore envoyer un
résumé trop long : il serait refusé (le tableau de bord ne serait plus à jour
pour ce compte ; sa progression, elle, est dans un autre document et part
quand même).

## Pas à pas pour Jacques

1. Ouvrir <https://console.firebase.google.com/project/deutschai-b6fbb/firestore/rules>.
2. **Garder une copie de l'ancien texte** : tout sélectionner dans l'éditeur
   (Ctrl+A), copier (Ctrl+C), coller dans un fichier
   `C:\Users\jacqu\.wortando\regles-console-2026-11-12-avant.txt`.
   (C'est le chemin du retour en arrière.)
3. Ouvrir `securite/firestore-corrige.rules` dans le dépôt, tout copier.
4. Dans l'éditeur de la console : tout sélectionner, coller à la place.
5. Cliquer **« Publier »**. Si la console signale une erreur, ne rien publier
   et envoyer la capture au chef.
6. Vérifier, dans l'app, connecté avec le compte admin :
   - Réglages → Administration : la liste des testeurs s'affiche.
   - Un bouton « OUVRIR L'ANGLAIS » sur une ligne, puis « RETIRER » : les deux
     marchent.
   - Faire un exercice, attendre 10 secondes, rouvrir le tableau : sa propre
     ligne dit « il y a quelques secondes ».
7. Le dire au chef : la session qui a fait l'audit recopie alors
   `firestore-corrige.rules` dans `firestore.rules` (la copie de ce qui est
   en ligne).

**Retour en arrière** : recoller le fichier de l'étape 2 et publier.

## Ce que les règles ne font pas (à décider à part)

- **Inscription sans code** : un compte Firebase peut toujours se créer sans
  passer par l'app. Les règles pourraient exiger un code consommé pour écrire
  quoi que ce soit, mais le lancement se fait **sans code** (essai de 7 jours) :
  ce serait à défaire aussitôt. La vraie protection d'une inscription ouverte
  est ailleurs : App Check, quota d'inscriptions par adresse IP
  (Authentication → Paramètres) et alerte de budget.
- **Taille totale des documents de progression** : Firestore refuse de
  lui-même au-delà de 1 Mio ; les gros champs ne sont pas bornés plus bas, une
  borne risquerait de refuser en silence la sauvegarde d'un testeur assidu.
  Le coût d'un abus se règle par App Check et le quota d'inscriptions
  (`securite/APP-CHECK.md`).
- **Un champ de droit d'accès ajouté plus tard** doit rejoindre
  `accesReserves()`, sinon chacun pourrait se l'accorder. L'abonnement payé,
  lui, n'est pas dans Firestore : RevenueCat le dit à l'app.
