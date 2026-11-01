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

## Les 26 autres (1er nov. 2026, « Oui, les 26 »)

Toutes faites, une prise chacune, **sauf le tram (`eletrico-28`), fait trois
fois** : les deux premières prises sont sorties en plusieurs panneaux (les
trois bandes du prompt lues comme trois photos). Le gabarit dit maintenant
« one single continuous view », et le tram regarde l'allée d'un bout à
l'autre. Rui et Lucas ont été découpés de leur première scène (`albergue`,
`aula-portugues`) avant les scènes où ils reviennent.

Les gags qui se lisent moins que prévu (les questions les raconteront) :
le parapluie de la pluie n'est pas retourné, les joues pleines de raisins du
Nouvel An se voient peu, Léo tient la chaussette au lieu de la laisser tomber
(`estendal`), le palais de Pena se devine un peu trop dans le brouillard, Léo
est petit et loin sur sa planche de surf, et au départ le Québécois qu'il
reprend se tient au fond.

Faux texte effacé en local (gratuit) : le titre du dictionnaire du cours
(`aula-portugues-propre.png`), deux étiquettes de bouteilles et le sac en
papier de la pastelaria (`pastelaria-propre.png`). Les autres étiquettes de
la pastelaria restent : elles touchent le chignon de Beatriz, que la retouche
abîmait. Les chiffres des horloges et des étiquettes de prix du marché
restent (une horloge a ses chiffres).

## Coût

**5,40 $** en tout, à 0,15 $ l'image : Léo, 4 images (0,60 $) ; les scènes,
32 images (4,80 $) — le pilote 4, les 26 autres 26, et 2 reprises du tram.

## La suite, sans dépense

Poser les zones et les masques (SAM 2, local), ajouter les 88 mots au corpus
avec phrase et traduction, faire les `scene-<nom>.pt.js` et brancher les
scènes dans l'essai portugais, écrire les couches A2 et B1 pour le portugais.
