# Le tournant de personnage — trois vues à faire, une fois pour la série

Écrit le 13 septembre 2026, sur une question de Jacques : *« on ne devrait pas
tout de suite demander à Artlist, à partir de l'image de face, une image de
profil et une image de dos ? »*

Oui. Et plus large que ça.

## ⚠️ Ce que j'avais écrit de faux, le premier jour

J'avais écrit ici que l'image maîtresse était un portrait tête et épaules, et
bâti tout ce document dessus. **C'est faux.** `personnages/Mark.png` est déjà
un **plein pied de face** : debout, fond studio gris uni, lumière douce, veste
coquille grise sur t-shirt noir, jeans, baskets. Une vraie planche de
référence.

J'avais lu le champ `apparence` — qui dit *« in a head-and-shoulders portrait »*
— **au lieu d'ouvrir le fichier**. Le champ décrit le prompt d'une version
antérieure ; l'image a évolué depuis. Corrigé par Jacques.

La leçon est celle que le dépôt répète ailleurs : **l'artefact fait foi, pas sa
description.** C'est déjà la règle d'ancrage — *« un personnage se génère
toujours à partir de son IMAGE maîtresse, jamais à partir de sa description »*
— et elle vaut aussi pour qui écrit les fiches.

## Ce qu'il reste à générer : trois vues, pas quatre

| vue | état |
|---|---|
| face, en pied | **elle existe** — `personnages/Mark.png` |
| **trois-quarts** | à faire — l'angle le plus utilisé en dialogue, au comptoir |
| **profil** | à faire — les plans latéraux, les scènes à deux |
| **dos** | à faire — les plans 01 et 18, et tous les « il s'en va » de la série |

⚠️ **MÊME TENUE QUE L'IMAGE EXISTANTE**, et c'est un renversement de ce que
j'avais écrit. Je recommandais une tenue neutre : juste dans l'abstrait, faux
ici. Trois vues en t-shirt uni à côté d'une face en veste grise ne font pas un
tournant, elles font quatre photos différentes. On s'aligne sur l'existant :
**veste coquille grise ouverte, t-shirt noir, jeans bleu foncé, baskets
sombres.** La garde-robe se change ensuite par-dessus, comme elle le fait déjà.

## ⚠️ Une divergence à trancher avant de lancer

Le champ `corps` décrit un triathlète massif : *« arms that fill a shirt sleeve
with visible deltoid and bicep mass »*, *« solid and rectangular rather than
V-shaped »*. **L'image maîtresse montre un homme athlétique plutôt mince.**

Les deux ne disent pas la même chose, et pour le tournant il faut choisir :

- **s'aligner sur l'image** (recommandé) — elle est le canon par la règle
  d'ancrage. Alors il faut **alléger le bloc `corps` dans le prompt**, sinon on
  génère trois vues plus massives que la face.
- **s'aligner sur le texte** — alors c'est la face qu'il faut refaire, et le
  personnage change d'allure dans l'épisode 1 déjà tourné.

C'est une décision de Jacques, pas une correction à faire en silence.

## Ce que ça ne résout pas, et il faut le savoir

⚠️ **Le dos est une invention.** Aucune référence ne dit à quoi ressemble
l'arrière de la tête de Mark. Le générateur la fabrique, plausiblement mais
arbitrairement — et dès qu'on l'accepte, **elle devient canon pour soixante-et-
onze épisodes**. Elle se choisit donc avec le même soin que l'image maîtresse,
et une seule fois.

Regarder en particulier : la ligne de nuque, la façon dont les cheveux tombent
à l'arrière, la largeur d'épaules par rapport à la taille. C'est ce qui se
reconnaît de dos, à distance.

## Pourquoi maintenant, et pourquoi ce n'est pas contre la règle

`personnages.json` avertit : *« n'ajouter un récurrent que quand un épisode
écrit en a besoin — le 7 septembre, six portraits de Mark ont été itérés avant
qu'un seul plan existe, et c'est ce qui a vidé un mois de crédits. »*

Cette règle vise les personnages **spéculatifs**. Mark existe, il est dans les
71 épisodes, et **deux plans écrits ont besoin de son dos aujourd'hui**. Le
besoin est établi, pas anticipé.

## Le prompt

À lancer dans Artlist, mode Framing, **avec `personnages/Mark.png` en
référence**. Un lancement par vue — le même bloc, en changeant la
dernière ligne.

⚠️ Le prompt ne redécrit ni le visage ni la carrure : **c'est l'image qui les
porte.** Il ne dit que ce que l'image ne peut pas dire — l'angle.

```
The same man as in the reference image, same face, same build, same clothes:
open grey shell jacket over a plain black t-shirt, dark blue jeans, dark
trainers. Full body, standing, on a plain light grey studio background with
even soft light and no shadow on the backdrop. Photorealistic.

POSTURE: upright and relaxed, arms hanging naturally at his sides, weight
settled evenly. Nothing stiff, nothing posed, no presenter's stance.

VIEW: seen from three quarters, turned about forty-five degrees to his left.
```

Puis les deux autres, en ne changeant que la dernière ligne :

```
VIEW: seen from the side, in full profile, facing frame left.
VIEW: seen from directly behind, back to camera, head not turned.
```

## Où ça se range

`personnages/Mark-face.png`, `-troisquarts.png`, `-profil.png`, `-dos.png`.

⚠️ **Hors dépôt** — `personnages/` n'est pas suivi par git, et c'est voulu :
le dépôt est public, et ces images sont l'ancrage du personnage.

Puis dans `personnages.json`, le champ `image_maitresse` devient un objet :
une entrée par angle, et `_image_maitresse` dit laquelle sert à quoi.

## À faire pour Anna aussi

Pas maintenant — aucun plan écrit n'a besoin de son dos. Mais le jour où un
épisode la montre s'éloigner, c'est le même tournant, le même prompt, et son
`corps` à la place de celui de Mark.
