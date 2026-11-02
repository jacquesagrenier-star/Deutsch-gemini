# Les découpages des scènes : reprise du 2 nov. 2026

Demande de Jacques : « tous les découpages, pas seulement des vêtements, tous les objets ». En particulier : un vêtement recouvert ne garde que sa partie **visible**, et les contours doivent épouser l'objet sans montrer de facettes une fois agrandis ×4.

## Ce qui a changé (detourer.py)

1. **Arbitrer qui est devant qui.**
   - Entre vêtements : un vêtement **contenu** dans un autre est devant lui (l'écharpe sur la doudoune, le chemisier dans l'ouverture de la veste).
   - Un recouvrement **partiel** se tranche à la **couleur** : le pull beige qui dépasse du manteau vert. Si les couleurs sont trop proches, le vêtement de dessus garde la zone.
   - Tout autre recouvrement partiel se tranche aussi à la couleur : Mark devant la chaise, le crayon dans la main.
   - Deux objets posés sur le même support ne se contiennent pas : le petit est devant.
   - On peut l'écrire à la main dans `points.json` : `"devant_de": [ids]`.
2. **Miettes et queues.** On retire :
   - un morceau détaché, petit et d'une autre couleur que l'objet ;
   - sur un vêtement, une bande de moins de 13 px qui pend.
3. **Tracé en courbes.** Les facettes deviennent des arcs (`q` dans un chemin SVG) ; les droites et les vrais coins restent. Les zones rigides et pleines gardent leur tracé du 6 oct. Le moteur (`chemin()` dans `index.html`) dessine ces chemins tels quels.
4. **Recadrer pour affiner**, mais seulement sur demande : `"affiner": true` sur une zone, ou `--affiner` pour toutes. Essayé sur tout le musée, le recadrage avait rendu la cravate avec la moustache et le veston avec la tête : sans un œil pour vérifier, il ne doit pas décider seul.
5. **Un cache** des masques pleine résolution, dans `~/.wortando/decoupages`, hors du dépôt. Une zone inchangée n'est pas redétourée, et `--retracer` refait les étapes 1 à 3 sans SAM.

Outils :

- `mesurer_decoupages.py` : la mesure.
- `comparer_decoupages.py` : les captures avant/après, l'avant étant lu dans git.

## Chiffres (43 scènes, 1 612 zones ; les 3 scènes japonaises ne sont pas touchées)

| Mesure | Avant | Après |
|---|---|---|
| Vêtements qui se recouvrent | 87 | 2 (20 et 31 px, du bruit) |
| Autres recouvrements entre zones sœurs | 297 | 131 (surtout des parties du corps en ellipses, voulues) |
| Zones grossières pour leur taille | 1 242 | 9 |
| Sommets à facette visible | 33 816 | 319 |
| Zones avec des miettes | 139 | 57 (surtout des zones en plusieurs boîtes, voulues) |
| Tracés qui sortent du masque | 26 | 1 |
| Tracés qui se recoupent | 1 | 3 (contours pincés sur un pixel) |
| Poids des masques, gzip | 584 Ko | 961 Ko (+9 Ko par scène) |

## Corrigé à la source (`points.json`)

| Scène | Zone | Ce qui n'allait pas |
|---|---|---|
| Musée | krawatte | elle prenait la moustache |
| Pharmacie | bildschirm | il prenait des flacons |
| Pharmacie | pflanze | elle prenait la manche |
| Pharmacie | muelleimer | il prenait la porte |
| Mairie | tastatur, maus, muelleimer | |
| Mairie | brille | mieux, mais elle garde un bout de front |
| Bibliothèque | buch-2 | |
| Salon de coiffure | pullover | le point « sur » était posé sur le magazine |
| Classe | rock | |
| Atelier de vélos | hose-2, schuh-2 | |

## Captures (`rapport-decoupages/`, ambre = avant, cyan = après)

| Capture | Scène | Ce qu'elle montre |
|---|---|---|
| 01 | Métro | la capuche, l'écharpe et la doudoune séparées |
| 02 | Hôtel | le pull ne garde que la bande entre les revers du manteau |
| 03 | Boulangerie | le manteau et le pull |
| 04 | Musée | la veste sans boucles, la cravate, le pantalon |
| 05, 10 | Musée, pharmacie | des contours vus à ×4 |
| 06, 09 | Pharmacie, mairie | les corrections à la source |
| 07 | Salon de coiffure | le gilet |
| 08 | Classe | la jupe |

## À reprendre (vu à l'œil, pas corrigé)

- **Restaurant**, déjà faux avant : jacke, pullover-2, hemd, hemd-4, hose.
- **Cabinet médical** : stift, qui garde la carte.
- **Mairie** : papier-3.
- **Atelier de vélos** : kette, qui prend une partie du cadre et la pince.
- **Bibliothèque** : stuhl-2.
- **Revue à l'œil incomplète.** J'ai regardé :
  - toutes les zones de 6 scènes : pharmacie, cabinet médical, ferme, boulangerie, bibliothèque, mairie ;
  - les vêtements de 21 scènes.

  Les autres zones n'ont été vues que par la mesure.
