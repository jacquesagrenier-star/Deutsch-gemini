# Scènes de Lisbonne — rapport du pilote (1er nov. 2026)

> Pour Jacques. Ta réponse : « Fais les cinq au complet. » — les cinq propositions
> de `HISTOIRE-LISBONNE.md` acceptées (Léo, 30 scènes, la liste, le Brésil sur les
> images de Lisbonne, la dépense du pilote). Tout le portugais est un **brouillon**.

## Ce qui est fait

1. **Léo en quatre vues** : `personnages/Leo.png`, `Leo-gauche.png`,
   `Leo-droite.png`, `Leo-dos.png` (dossier OneDrive, hors du dépôt), par
   `video/leo.py`. Coton ouaté bleu roi à bande rouge (les couleurs des
   Canadiens, sans logo), foulard crème brodé de fleurs bleues.
2. **Le pilote**, une prise chacune, Léo en référence (`visuel/scenes/<nom>.png`) :
   | Scène | Ce qu'on voit | Remarques |
   |---|---|---|
   | 1 `aeroporto-lisboa` | Léo au téléphone, sa valise verte fait le tour du tapis toute seule, une fillette la montre du doigt | réussie |
   | 3 `casa-graca` | le palier aux azulejos verts, Dona Fernanda présente son canari, Léo s'incline trop bas | réussie |
   | 4 `pastelaria` | Léo et sa bica, Beatriz qui retient son rire, Sr. Albano à la machine | le gag de la tasse minuscule se lit moins : il boit plutôt qu'il ne s'étonne ; quelques étiquettes de bouteilles en faux texte (à effacer en local, gratuit) |
   | 6 `miradouro` | Léo essoufflé en haut des marches, la dame de 80 ans qui le dépasse avec ses sacs (et un poireau), la ville, le château, le pont | réussie |
3. **Les références des personnages qui reviennent**, découpées dans le pilote :
   `personnages/lisbonne/fernanda.png`, `beatriz.png`, `albano.png`. Rui et Lucas
   seront découpés de leur première scène (albergue, aula-portugues), avant les
   scènes où ils reviennent (fado, cacilheiro, feira-da-ladra, despedida).
4. **Les 26 autres prompts** (`visuel/scenes/<nom>.prompt.txt`), fabriqués par
   `portugais/lisbonne/prompts.py` : **0 faute** au vérificateur des prompts.
   Un gag visible dans chacun ; aucun mot ni chiffre dans les images (le
   tableau du cours montre deux bus dessinés et un signe =, pas « autocarro »
   et « ônibus » ; aux Finanças, Léo s'endort sur l'épaule de son voisin au
   lieu du ticket 347). Un lieu qui revient (la pastelaria du match, le hall
   du départ) entre par l'image de sa première scène.
5. **Les mots** : `portugais/lisbonne/mots-prevus.json`, contrôlés par
   `verifier_mots.py` (0 faute) : **424 mots** déjà au corpus, **88 mots
   distincts à y ajouter** (le corpus portugais, dérivé de la liste allemande,
   n'a ni « o mar » ni « o lago » ; plus les mots de Lisbonne : o estendal,
   a mola, o cravo, o manjerico, a calçada, o cacilheiro, a bifana…).

## Coût

**1,20 $** : Léo 0,60 $ (face + trois vues) et le pilote 0,60 $ (quatre images
à 0,15 $, aucune reprise). Rien d'autre n'a été payé.

## La suite

1. **Les 26 autres images** : 26 × 0,15 = **3,90 $**, plus 1 à 2 $ de reprises
   probables. J'ai lu « les cinq » comme les cinq questions, dont la dernière
   ne parlait que du pilote : elles attendent ton mot.
2. Puis, sans dépense : effacer le faux texte, poser les zones et les masques
   (SAM 2, local), ajouter les 88 mots au corpus avec phrase et traduction,
   faire les `scene-<nom>.pt.js` et brancher les scènes dans l'essai portugais,
   écrire les couches A2 et B1 pour le portugais.
