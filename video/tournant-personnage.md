# Le tournant de personnage — quatre angles, une fois pour la série

Écrit le 13 septembre 2026, sur une question de Jacques : *« on ne devrait pas
tout de suite demander à Artlist, à partir de l'image de face, une image de
profil et une image de dos ? »*

Oui. Et plus large que ça.

## Le manque, nommé

L'image maîtresse de Mark est un **portrait tête et épaules**. Sa fiche le dit
déjà, et elle dit aussi ce qui arrive quand on cadre plus bas :

> ⚠️ *« À joindre à `apparence` dès que le cadrage dépasse la poitrine. Au-delà
> de la poitrine le générateur invente le corps, et il invente **mince par
> défaut**. »*

C'est exactement ce qui a raté au plan de dos de l'aéroport — *« ça ne
correspondait pas tout à fait à lui »*. Le personnage écrit est un triathlète
massif ; sans ancrage, le générateur rend un coureur.

Le texte du champ `corps` corrige en partie. **Une image corrige mieux** : un
générateur suit une référence visuelle plus fidèlement qu'une description, et
il n'a plus à interpréter « solid and rectangular rather than V-shaped ».

## Ce qu'il faut générer

Quatre vues, **en pied**, même personnage, même tenue neutre, même lumière,
fond uni :

| vue | à quoi elle sert |
|---|---|
| **face, en pied** | la seule qui manque vraiment aujourd'hui — l'actuelle s'arrête aux épaules |
| **trois-quarts** | l'angle le plus utilisé en dialogue, au comptoir |
| **profil** | les plans latéraux, et les scènes à deux |
| **dos** | les plans 01 et 18 de l'épisode 2, et tous les « il s'en va » de la série |

⚠️ **Tenue neutre, pas une des tenues de garde-robe.** Le tournant ancre le
CORPS, pas un épisode. Un t-shirt et un pantalon simples : la garde-robe se
change ensuite par-dessus, comme elle le fait déjà.

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

À lancer dans Artlist, mode Framing, avec `personnages/Mark.png` en référence.
Un lancement par vue — le même bloc, en changeant la dernière phrase.

```
Full-body character reference of the same man as in the reference image,
standing against a plain neutral light grey background, even soft studio
light, no shadows on the backdrop, photorealistic, documentary realism.

He wears a plain dark t-shirt and plain dark trousers, no branding, no
jacket. Bare feet or plain dark shoes.

BODY: tall — about 1.86 m — with a long-limbed frame, long legs relative to
the torso and long forearms, and powerfully built with it, compact rather
than lean. Broad shoulders and a thick neck, a full chest, and arms that fill
a sleeve with visible deltoid and bicep mass. The waist is moderate rather
than sharply tapered, so the silhouette reads solid and rectangular rather
than V-shaped. Long, strong legs with well-developed thighs and calves. A
triathlete's build, not a marathon runner's.

POSTURE: upright and relaxed, weight settled on one leg, shoulders open, arms
hanging naturally. Nothing stiff, nothing posed, no presenter's stance.

VIEW: seen from directly in front, facing camera.
```

Puis la même chose en remplaçant la dernière ligne :

```
VIEW: seen from three quarters, turned about forty-five degrees to his left.
VIEW: seen from the side, in full profile.
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
