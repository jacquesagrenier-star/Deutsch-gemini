# Les lieux qui reviennent — un seul décor par lieu, pour toute la série

Demandé par Jacques le 24 oct. 2026 : « s'assurer que lorsqu'on est dans une pièce, la pièce reste
la même. Quand on va être dans l'appartement de Mark ou celui d'Anna, c'est un défi pour ce genre
de vidéo : les meubles au même endroit, les couleurs des murs les mêmes. »

Le modèle d'image **remeuble la pièce à chaque plan** (voir la mémoire « continuité du décor » et
`video/verifier_prompt.py`). La seule parade qui tient : **une image maîtresse VIDE par lieu**, une
**carte écrite** du lieu, et cette image donnée en référence « POUR LE LIEU » à **chaque** image
tournée dans ce lieu, dans **tous** les épisodes.

## La règle, en quatre gestes

1. **Avant d'écrire une scène ou un épisode** : relire `scenes/personnages.json` (la source sur
   Mark et Anna) et la fiche `.claude/histoire-personnages.md`, puis ce fichier. ⚠️ Le 24 oct.,
   faute de l'avoir fait, un épisode envoyait Mark à un cours d'allemand alors que sa mère est
   allemande (sa fiche le dit depuis le 7 sept.).
2. **Un lieu qui revient a UNE entrée ici** : son image maîtresse vide, sa carte (gauche / droite
   DE L'IMAGE, d'où vient la lumière), et la liste de ce qui ne bouge jamais (couleur des murs,
   meubles et leur place, sol, fenêtres, objets marquants).
3. **Chaque image tournée dans ce lieu** reçoit l'image maîtresse « POUR LE LIEU » et reprend,
   dans son prompt, les éléments fixes qui sont dans le cadre. On ne décrit jamais un meuble
   « de mémoire » : on regarde l'image maîtresse.
4. **À la réception**, on compare l'image au maître (même mur, même meuble au même endroit) AVANT
   de la garder. Un lieu nouveau s'ajoute ici le jour où il est tourné.

⚠️ Une image d'une SCÈNE de l'app peut servir de base au maître (c'est le même monde), à condition
   d'être une photo : une retouche ne change pas un dessin en photo (règle « retouche-de-style »).
   Pour vider une pièce de ses personnages : la retouche qui RETIRE quelqu'un (acquis du 11 oct.).

---

## Les lieux de la série allemande (Berlin)

### La colocation de Mark — À FAIRE AVANT LE PREMIER ÉPISODE CHEZ LUI
- **Source : les scènes de l'app**, déjà en photo, déjà son appartement :
  - le **salon** : `visuel/prototype/vignettes/wohnzimmer.webp` (prompt :
    `visuel/scenes/wohnzimmer.prompt.txt`) — canapé gris à gauche, grande fenêtre au fond, parquet
    clair, murs blancs, armoire en bois à gauche, plante, vélo contre le mur ;
  - la **cuisine** : `visuel/prototype/vignettes/kueche.webp` (`visuel/scenes/kueche.prompt.txt`)
    — mur **vert sauge**, réfrigérateur blanc à gauche, table en bois, horloge ronde, étagère à
    vaisselle, fenêtre à droite.
- **À fabriquer** : pour chaque pièce, le maître VIDE (retouche qui retire les personnes et le
  désordre de fête), en pleine résolution, rangé dans `video/lieux/mark-salon.png`,
  `video/lieux/mark-cuisine.png`. Puis la carte et la liste ici.

### L'appartement d'Anna — À CRÉER le jour où un épisode y va
- Aucune source pour l'instant (les scènes `schlafzimmer` et `umzug` de l'app ne nomment personne).
  On le conçoit une fois, vide, on l'écrit ici, et il ne change plus.

### La boulangerie du Kiez — épisode 04 « Schrippe »
- Maîtres : `video/episode-04-schrippe/01-images/baeckerei-aussen.png` (dehors) et
  `baeckerei-theke.png` (dedans, vide).
- Dehors : devanture de bois **vert foncé**, planche peinte **sans lettres**, porte vitrée au
  centre, vitrine de pains à gauche, arbre nu et vélo noir à gauche, trottoir pavé ; soleil bas
  venant de la GAUCHE.
- Dedans : comptoir vitré dans la moitié DROITE de l'image, du premier plan vers le fond ; paniers
  d'osier de Schrippen, UN plateau de beignets sucrés ; sacs en papier brun et pince en acier sur
  le verre ; étagères de bois de pains sombres au fond ; trois lampes suspendues chaudes ; vitrine
  et lumière du jour à GAUCHE ; carrelage usé.
- ⚠️ Ce n'est PAS la boulangerie de la scène `baeckerei` de l'app (autre décor) : la vidéo fait foi
  pour la série.

### La Volkshochschule — épisode 05 « Zweiter Stock » (à tourner)
- Lieu **récurrent** : le cours d'espagnol de Mark et d'Anna, chaque mardi soir. Carte complète
  dans `video/episode-05-vhs/A-TOURNER.txt` (écrite le 26 oct.). Les maîtres sont à fabriquer,
  vides, dans `video/episode-05-vhs/01-images/` :
  - `vhs-fassade` : bâtiment des années 60, quatre niveaux de fenêtres éclairées, porte vitrée
    au milieu, vélos à GAUCHE, réverbère à DROITE, sans aucune lettre ;
  - `vhs-treppe` : marches de pierre grise, rampe de bois, soubassement **vert pâle**, lampes
    rondes ; la porte vitrée (noire le soir) à GAUCHE, l'escalier qui monte vers la DROITE ;
  - `vhs-flur` : le couloir du **premier** étage, portes de bois fermées **sans numéro** à
    DROITE, la cage d'escalier ouverte à GAUCHE ;
  - `kurs-raum` : **la salle**, vue du fond, coin gauche. Tableau blanc **vide** au fond, porte
    dans le mur de DROITE près du tableau, deux rangées de tables de bois clair, fenêtres
    noires du soir à GAUCHE. Anna au 2e rang côté fenêtres ; **la chaise de Mark à sa droite,
    chaque semaine**. Aucun poster, aucune horloge.

### Les lieux d'un seul épisode (gardés pour mémoire)
- L'aéroport (épisode 1), le Bürgeramt (épisode 2), la piste cyclable (épisode 3) : voir leurs
  `A-TOURNER.txt`. S'ils reviennent, leur maître est dans `01-images/` de l'épisode.

## Les lieux de la série espagnole (Madrid)

- **Le bar** — es-03 « El café » : `video/episode-es-03-el-cafe/01-images/mad_bar_manana.png`
  (zinc, carrelage blanc, machine à café chromée) ; voir sa feuille.
- **Le bureau et l'ascenseur** — es-04 : `mad_oficina_manana.png` (fenêtres et toits de Madrid à
  DROITE, cuisine au fond à gauche, portes d'ascenseur au fond) et `mad_ascensor_vacio.png`
  (acier brossé, panneau de boutons à droite).
- **La boutique d'Ana** — es-05 « La tienda de Ana » (à tourner). Lieu **récurrent** ; carte
  complète dans `video/episode-es-05-la-tienda/A-TOURNER.txt` (26 oct.). Maître à fabriquer,
  vide : `tienda.png`. On la voit depuis l'entrée.
  - À GAUCHE : un portant de bois le long du mur, avec trois vestes moutarde au bout, et la
    cabine d'essayage au fond (rideau de lin écru), devant laquelle Mark se tient toujours.
  - À DROITE : le comptoir de bois clair, Ana derrière, et des étagères de pulls pliés.
  - La lumière : soleil bas par la vitrine, à DROITE.
  - Dehors : `mad_calle_tienda.png`, une devanture **bleu foncé** (pas le vert de la
    boulangerie de Berlin).
