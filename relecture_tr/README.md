# Relecture croisée du turc

Même méthode que pour l'allemand, **même ordre** : le contrôle mécanique
d'abord, la relecture par un autre modèle ensuite, et n'appliquer que les faits.

Tout est produit par `tests/relecture_tr.py`.

## 1. Le contrôle mécanique — avant toute IA

```
python tests/relecture_tr.py --suspects
python tests/relecture_tr.py --collisions
```

- **`suspects.md`** — les champs turcs qui ne peuvent pas être une traduction :
  un caractère unique en guise de mot, une phrase de moins de huit caractères.
  Ce ne sont pas des traductions faibles, ce sont des **données perdues**. Elles
  ne se relisent pas, elles se refont — et elles sont exclues des lots.
- **`collisions.md`** — un même mot turc qui répond à plusieurs mots allemands
  distincts de la même catégorie. La carte devient indécidable : quoi que
  l'apprenant réponde, il ne peut pas avoir raison. Aucune relecture par lots ne
  peut les voir, puisque la collision se joue entre deux lots.

Toutes les collisions ne sont pas des erreurs : deux quasi-synonymes allemands
peuvent légitimement partager un mot turc si la langue n'en a pas deux. Mais
chacune doit être **regardée**.

## 2. Les lots à distribuer

```
python tests/relecture_tr.py --niveaux A1,A2
python tests/relecture_tr.py                     # tous les niveaux
python tests/relecture_tr.py --categories noms   # une seule catégorie
```

Un lot = un fichier `<catégorie>_<niveau>_lot_NN.json`, 100 cartes (40 pour les
verbes, qui portent cinq fragments turcs chacun). **Un lot ne mélange jamais
deux niveaux** : le relecteur doit juger le registre contre le niveau annoncé.

À joindre à chaque envoi : **`CONSIGNE.md`**.

Rythme éprouvé : **trois à cinq relecteurs en parallèle**, pas plus — à sept ça
cale, et à 330 cartes par lot aussi.

## 3. Le dépouillement

Récupérer chaque réponse sous `verdict_<nom du lot>.json` dans ce dossier, puis :

```
python tests/relecture_tr.py --rapport
```

Produit **`divergences_tr.md`**. Il ne corrige **rien** : l'application est en
service, ce qui remonte s'examine, ne s'applique pas en bloc. Côté allemand,
3 signalements sur 5 ont été appliqués — tous des contradictions internes à une
fiche, pas des jugements de naturel.

## La limite, à redire à chaque fois

Le relecteur est un autre modèle, pas un autre esprit : il partage une partie de
nos données d'entraînement, donc une partie de nos angles morts — et c'est le
plus vrai sur le régional. Son accord n'est pas une preuve. Pour trancher ce qui
reste, il faut un autre fournisseur, ou une locutrice native.

## Ce qui est versionné, et ce qui ne l'est pas

Les lots sont **dérivés** des JSON : une commande les refait, ils ne sont pas
versionnés. Les verdicts, `collisions.md`, `suspects.md` et `divergences_tr.md`
le sont.
