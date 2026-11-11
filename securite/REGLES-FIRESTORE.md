# Règles Firestore corrigées (11 nov. 2026)

Audit de lancement, point 1. Les règles sont **prêtes, pas publiées** : c'est
Jacques qui les colle dans la console. Le texte à coller est le fichier
[`firestore-corrige.rules`](firestore-corrige.rules), **en entier**.

## Pourquoi

Le tableau de bord admin affiche ce que chaque compte écrit dans son
« résumé » : prénom, adresse, appareil, retours, mots demandés, compteurs. Les
règles actuelles laissent chacun y écrire **n'importe quoi** : un prénom de
mille caractères, du code à la place d'un nombre, l'adresse d'un autre testeur.
Elles laissent aussi chacun s'ouvrir lui-même un essai réservé (l'anglais, les
examens) ou les chapitres VHS. Et un compte peut se créer sans code
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
| Progression, codes d'invitation, lectures | inchangés | inchangés |

Bornes des résumés : prénom 60 caractères, retours 20 000, mots demandés 150,
appareil 20, version 10, langue 10, compteurs entre 0 et 10 millions.
Les plus grands mesurés le 11 nov. : prénom 15, retours 11 917. L'app coupe
déjà le résumé à ces bornes (depuis ce correctif) : une écriture normale n'est jamais refusée.

## Éprouvé avant d'être proposé

Dans l'émulateur Firebase local (un projet fictif, rien n'est parti vers le
vrai Firebase), 146 cas, avec le SDK de l'app :

- **Nouvelles règles : 146 sur 146.** Toutes les écritures normales passent
  (inscription, sauvegarde, résumé, notifications, suppression du compte,
  boutons admin, « Reconstruire les résumés », codes d'invitation), et toutes
  les attaques sont refusées.
- **Règles actuelles : 53 attaques passent** (prénom trop long, compteur en
  texte, champ inconnu, adresse d'un autre, essai ou VHS auto-attribué…).

Le banc d'essai se relance ainsi (Java et Firebase CLI sont installés) :
`securite/essai-regles/` → voir son `LISEZ-MOI.md`.

## Quand coller

**Après** la publication de la version de ce correctif (l'app qui coupe le résumé aux bornes).
Avant, une vieille version ouverte sur un téléphone pourrait encore envoyer un
résumé trop long : il serait refusé (le tableau de bord ne serait plus à jour
pour ce compte ; sa progression, elle, est dans un autre document et part
quand même).

## Pas à pas pour Jacques

1. Ouvrir <https://console.firebase.google.com/project/deutschai-b6fbb/firestore/rules>.
2. **Garder une copie de l'ancien texte** : tout sélectionner dans l'éditeur
   (Ctrl+A), copier (Ctrl+C), coller dans un fichier
   `C:\Users\jacqu\.wortando\regles-console-2026-11-11-avant.txt`.
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
- **Taille des documents de progression** : pas bornée ici. Firestore refuse
  de lui-même au-delà de 1 Mio, et une borne plus basse risquerait de refuser
  en silence la sauvegarde d'un testeur assidu.
- **Si l'abonnement écrit un jour un droit dans Firestore** (par exemple une
  date d'accès offert), ce champ doit rejoindre `accesReserves()`, sinon
  chacun pourrait se l'accorder. Aujourd'hui, l'essai de 7 jours lit la date
  de création du compte Firebase, que personne ne peut réécrire.
