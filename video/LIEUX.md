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

- **Ce qui existe déjà en photo** (relevé le 4 nov. 2026 pour le thème « Le logement », qui les reprend telles
  quelles, `visuel/logement/logement.py`) : sa **chambre** (« La journée », `visuel/prototype/journee/mark-1.webp`,
  `mark-8.webp` : lit en bois clair, murs blancs, rideaux blancs devant la fenêtre à gauche, une chaise couverte de
  vêtements) ; sa **salle de bains** (`mark-3.webp`, `mark-4.webp` : carrelage gris, douche à porte de verre, grand
  miroir avec une rampe lumineuse au-dessus, petite fenêtre) ; le salon rangé avec un petit bureau devant la grande
  fenêtre (`mark-6.webp`) et la cuisine le soir (`mark-7.webp`, même mur vert sauge).
- **L'entrée (à générer, thème « Le logement », 4 nov.)** : même parquet clair et mêmes murs blancs que le salon,
  portes blanches à panneaux ; un long couloir étroit, des patères avec vestes et sac à dos, un grand miroir à
  cadre de bois accroché au mur, un plafonnier à boule de papier blanc, un long tapis rayé. Référence : le salon.

### L'appartement d'Anna — en partie en photo (4 nov. 2026)
- Les scènes `schlafzimmer` et `umzug` ne nomment personne dans l'image, mais leurs textes disent Anna
  (« Anna packt ihren Koffer », « Anna emménage dans son nouvel appartement »).
- ⚠️ **Deux chambres différentes** : celle de la scène `schlafzimmer` (grand lit en bois, couvre-lit beige, tapis
  rond bleu, bureau sous la fenêtre) ne ressemble pas à celle de « La journée » (`journee/anna-1.webp`, `anna-4`,
  `anna-10` : lit blanc, couette gris clair, table de chevet en bois avec une lampe, armoire en bois). Le thème
  « Le logement » ne reprend QUE celle de « La journée », cohérente avec sa cuisine. À trancher avant un épisode.
- La **cuisine** (« La journée », `anna-5`, `anna-9`) : buffets **bleu clair** vitrés à gauche, plan de travail en
  bois, petite table ronde devant la fenêtre à deux battants, radiateur blanc dessous, étagère murale à droite,
  plafonnier blanc. La **douche** (`anna-3`) : carrelage blanc, porte de verre, petite fenêtre. Le **salon**, le jour
  de l'emménagement (`umzug`) : parquet, murs blancs, grande fenêtre au fond, canapé sous plastique avec un coussin
  jaune, grand miroir posé contre le mur, lampadaire blanc, étagère blanche, tableau de mer.
- **Le balcon (à générer, thème « Le logement », 4 nov.)** : étroit, garde-corps en fer forgé noir, petite table
  ronde de bistrot en métal et deux chaises pliantes, plantes vertes et géraniums rouges en pots de terre cuite ;
  derrière, les arbres d'une cour berlinoise. Référence : sa cuisine (le même immeuble, les mêmes fenêtres).

### L'appartement de Jan et Katrin (la famille d'Anna) — en photo (4 nov. 2026)
- Le **salon** de « Où est le chat ? » (`visuel/prototype/gato/piece.webp`, porte blanche à gauche, armoire sombre,
  canapé gris clair, étagère blanche, table en pin). « La journée » : la **chambre des enfants** (`familia-1`, `-7`,
  `-8` : deux lits en bois clair, peluches, tapis rayé multicolore, rideaux beiges), la **cuisine** (`familia-2`,
  `-6` : table en bois, suspension blanche, deux fenêtres), la **salle de bains** (`familia-3` : lavabo, miroir,
  baignoire, rideau de douche blanc) et l'**entrée** (`familia-4` : patères, banc à chaussures blanc, plafonnier).

### L'appartement que visite Lena (die Besichtigung, thème « Le logement », 4 nov. 2026) — à générer
- Un appartement à louer, **vide**, dans un Altbau de Berlin : murs blancs fraîchement peints, parquet de chêne
  clair, hauts plafonds à moulure blanche, hautes fenêtres doubles blanches, radiateurs blancs sous les fenêtres,
  aucun meuble. Cuisine équipée blanche (plan de travail en bois clair, évier inox, cuisinière blanche, grand
  réfrigérateur blanc) ; salle de bains carrelée de blanc avec baignoire, lavabo et miroir ; salon vide avec une
  porte-fenêtre sur un balcon à garde-corps noir.
- **Frau Becker**, la propriétaire (personne neuve) : la soixantaine, cheveux gris courts, lunettes sans monture,
  gilet beige sur un chemisier bleu clair, une chemise cartonnée bleu foncé. **Lena** (25 ans, la petite sœur
  d'Anna, `visuel/familia/`) visite. La première image (la cuisine) sert de référence aux trois autres.

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

### Les lieux du thème « Les transports » (thème illustré, 3 nov. 2026)
Source : `visuel/transportes/transportes.py` (`LIEUX`, `LIEU_TXT`, `IMAGES`).
- **Le carrefour du Kiez** = la scène Kreuzung (`visuel/prototype/kreuzung.webp`), donnée « pour le lieu » : l'arrêt
  de bus (abri vitré, panneau rond jaune), le bus BLANC, le tram JAUNE, le taxi CRÈME, la piste cyclable ROUGE, les
  immeubles crème et beige, les pavés gris mouillés, un jour d'automne couvert. Mark y monte dans le bus et en
  descend, Lena y prend le tram, Mark y sort du taxi, Mark y passe à vélo, Anna y marche.
- **La station de U-Bahn** = la scène U-Bahn (`visuel/prototype/ubahn.webp`) : carrelage vert pâle, sol de granit
  gris et sa bande podotactile sombre, rame jaune, horloge suspendue. Mark y monte dans la rame (l'image de la scène,
  recadrée), y achète son billet au distributeur contre le mur carrelé ; Anna est assise dans la rame.
- **NOUVEAU — le quai de la grande gare** (Hauptbahnhof de Berlin, verrière) : quai de béton gris, ligne blanche
  au bord, piliers d'acier, train grandes lignes blanc à bande rouge. Anna y descend du train avec sa petite valise
  rouge foncé, puis y remonte (même cadrage : `zug-ein` est une retouche de `zug-aus`).
- **NOUVEAU — une rue résidentielle arborée** (Felix au volant d'une petite voiture grise) et **l'intérieur d'un
  avion** (Felix au hublot, l'aile et les nuages).
### Les lieux du thème « Les vacances et le voyage » (thème illustré, 5 nov. 2026)
Source : `visuel/vacances/vacances.py` (`IMAGES`, `REPRISES`). Trois voyages, hors de Berlin pour l'essentiel :
- **La chambre d'Anna** = celle de « La journée » (lit blanc, table de chevet en bois et sa lampe, armoire en bois, fenêtre et
  radiateur blancs) : elle y fait sa **petite valise à roulettes rouge foncé**, celle de la scène `flughafen` et du quai de gare des transports.
- **Málaga** (Anna, en octobre) : la plage de la scène `strand` (recadrée), la place de la cathédrale (pierre claire, orangers), une rue
  de la vieille ville et son étal de céramiques peintes. Anna en robe d'été et chapeau de paille ; à l'aéroport de Berlin, son manteau bleu marine et l'écharpe rouge.
- **Hambourg** (Mark, un week-end de pluie) : l'hôtel de la scène `hotel` (recadrée), le train grandes lignes, le bateau du tour du port
  (grues, Speicherstadt de brique rouge), une baraque à Fischbrötchen, un musée maritime, un café. Mark porte toujours le **manteau de
  laine gris** de l'hôtel sur un pull bleu foncé, et son **sac à dos noir**.
- **La mer Baltique** (Jan, Katrin, Ben, Mia, l'été dernier) : une maison blanche de bord de mer, **porte bleue**, roses grimpantes, la
  mer derrière les dunes (l'appartement de vacances, `familia-wohnung`, référence de l'intérieur) ; la plage aux Strandkörbe.
### Le salon de Jan et Katrin (chez Ben et Mia) — thèmes « Où est le chat ? » et « La météo »
- Maître : `visuel/gato/img/piece.png` (la pièce vide du chat Moritz ; copie dans
  `~/.wortando/meteo/ref/salon-jan-katrin.png`), webp publié `visuel/prototype/gato/piece.webp`. Toute image qui y
  revient est une **retouche** de cette pièce (mêmes meubles, mêmes couleurs, même fenêtre), jamais une description.
- La météo y met Anna (la tante) qui lit un livre à Mia sur le canapé, la pluie à la fenêtre.

### La place du Kiez (Prenzlauer Berg) — thème « La météo et les saisons » (3 nov. 2026)
- Lieu **nouveau**, extérieur : une petite place pavée, maisons anciennes de cinq étages aux couleurs pastel (jaune
  pâle, vert clair, rose) avec balcons, un grand tilleul au milieu et son banc rond en bois, à droite un petit café
  (trois tables rondes, deux grands parasols blancs), à gauche un réverbère en fonte vert foncé et un range-vélos.
  Vue à hauteur de piéton, le ciel au tiers supérieur.
- Maître : `~/.wortando/meteo/img/sommer.png` (l'été, texte → image) ; les sept autres temps en sont des
  **retouches** (`visuel/meteo/meteo.py`, `GARDE`). Une vidéo qui passe sur une place du quartier repart de lui.

### La ferme de l'oncle d'Anna (Brandebourg) — la scène `bauernhof`, le thème « Les animaux »
- Maître : `visuel/scenes/bauernhof.png` (la scène de l'app, une photo, un matin d'automne). Les
  images du thème « Les animaux » en sont des **retouches**, ce maître en référence
  (`visuel/animales/animales.py`, décision du 3 nov. 2026 sur la continuité des lieux).
- Ce qui ne bouge jamais : la **maison en briques rouges** et la grange (échelle, bois empilé), le
  puits, le pommier, les **clôtures de bois** clair, la prairie verte et la colline des moutons ;
  la cour en terre sablonneuse ; lumière dorée d'automne.
- Ses bêtes : une vache **Holstein noire et blanche**, un cheval **alezan à liste blanche**, un
  cochon **rose à quelques taches brunes**, des moutons blancs sur la colline, des poules
  **rousses**, un **border collie noir et blanc**, un chat tigré sur le muret.
- Les gens de la ferme : l'oncle d'Anna (dans l'arbre de `visuel/familia`, son seul oncle est Frank,
  59 ans, le mari de Sabine) et l'enfant au chapeau de paille, qui est **le fils de Felix**, le cousin
  d'Anna (décision de Jacques du 4 nov. 2026 : « prendre l'enfant de Félix pour la ferme »), et non
  un « petit cousin ». Ce fils n'est pas encore dans l'arbre de la famille. Les images du thème « Les
  animaux » ne montrent personne.

### Le salon de Jan et Katrin (Berlin) — « Où est le chat ? », « Les animaux »
- Maître : `visuel/gato/img/piece.png` (la pièce vide ; carte et éléments fixes dans
  `visuel/gato/gato.py`, `PIECE`). Le chat de la maison : **Moritz**, noir et blanc (smoking).

### Les magasins du quartier — thème illustré « Faire les courses » (4 nov. 2026)
- **Les magasins qui ont leur scène dans l'app gardent son image**, telle quelle et pour tout moment qui s'y passe
  (retouche avec la scène en référence « POUR LE LIEU ») :
  - la **boulangerie** : `visuel/prototype/baeckerei.webp` — comptoir vitré et caisse à GAUCHE, étagères de pains en
    bois au fond, fenêtre et réverbère à DROITE, carrelage clair ; la boulangère : blouse blanche, **bonnet blanc**,
    souriante. ⚠️ Ce n'est pas la boulangerie du Kiez de l'épisode 04 (autre décor) : le thème suit l'app ;
  - le **supermarché** : `visuel/prototype/supermarkt.webp` — étagères blanches, sol gris, grandes vitres au fond,
    caddie et panier rouge ; la caissière (à créer avec la première image de caisse) : la cinquantaine, chignon
    foncé, polo de travail **bleu foncé**, comme l'employé du rayon ;
  - la **pharmacie** : `visuel/prototype/apotheke.webp` ;
  - le **marché** : `visuel/prototype/markt-obst-heimisch.webp` — auvent vert, cageots de bois ; le marchand de
    fruits (à créer) : la soixantaine, barbe grise courte, tablier vert foncé.
- **Quatre magasins neufs**, au format et dans le style des scènes (9:16, la boulangerie en référence de style), aucune
  lettre, aucune enseigne, aucun prix :
  - la **boucherie** (Metzgerei) : long comptoir vitré dans la moitié DROITE (saucisses, jambon, viandes sur plateaux
    blancs), le boucher derrière (la quarantaine, cheveux bruns courts, blouse et tablier blancs), une balance sur le
    comptoir, murs carrelés blancs, fenêtre à GAUCHE ;
  - le **kiosque** (Kiosk, un Späti) : journaux et magazines aux couvertures vierges à GAUCHE, frigo de boissons au fond,
    comptoir et caisse à DROITE ; le kiosquier : la cinquantaine, moustache grise, gilet vert foncé ;
  - la **droguerie** (Drogerie, allemand seulement) : longues étagères blanches (dentifrice, savon, shampoing), caisse
    à l'avant DROITE, la vendeuse : la trentaine, queue de cheval foncée, polo blanc ; sol gris ;
  - la **librairie** (Buchhandlung) : étagères de bois pleines de livres, table de livres au centre, comptoir à DROITE ;
    la libraire : la soixantaine, cheveux gris courts, lunettes rondes, gilet rouge foncé ; fenêtre à GAUCHE, parquet.
- Les clients sont **Mark** et **Anna** (leurs images de référence) ; les vendeurs restent sans nom.
- La source : `visuel/courses/courses.py` (LIEUX, MOMENTS). Un moment dans la boucherie reprend l'image de la boucherie.

### L'école de Ben et la Kita de Mia — thème illustré « L'école et la garderie » (5 nov. 2026)
Source : `visuel/ecole/ecole.py` (`IMAGES`, `KITA`, `CLASSE`, `SOURCES`). Les enfants de Jan et Katrin : Ben (7 ans,
2e année, classe 2b) et Mia (4 ans).
- **La Grundschule de Ben** (« Grundschule am Kiez ») = la façade de « La journée » (`visuel/prototype/journee/familia-5.webp` :
  immeuble crème à grande porte vitrée, rue pavée de Berlin, réverbères). Le retour de l'école (`schule-abholen`) et la
  cour de récréation (`pause` : un grand marronnier, une structure à grimper) la reçoivent « pour le lieu ».
- **NOUVEAU — la classe 2b** (`klasse`, le maître des images de classe) : petits pupitres et chaises de bois clair en
  rangées, grand tableau VERT entièrement vide, peintures d'enfants sans écriture sur un panneau de liège à DROITE,
  fenêtre à GAUCHE, murs crème. **Frau Weber**, l'enseignante (personne neuve, sans image de référence avant `klasse`) : la
  quarantaine, cheveux bruns mi-longs, lunettes, pull bleu foncé. La porte de la classe (`lehrerin`) et la réunion de
  parents (`elternabend`, le soir, les parents sur les petites chaises) reprennent `klasse`.
- **NOUVEAU — la Kita de Mia** (« Kita Pusteblume », `kita-bringen`, le maître des images de la Kita) : vestiaire clair,
  parquet pâle, murs blancs, bancs bas en bois et rangée de petites patères avec vestes et petits sacs à dos, dessins
  d'enfants sans écriture, grandes fenêtres. **Frau Krüger**, l'éducatrice (personne neuve) : la quarantaine, cheveux
  courts blond vénitien, gilet vert, jean. `kita-abholen` (Mark vient chercher Mia), `anmelden` (le bureau de la
  directrice : la cinquantaine, chignon gris, écharpe rouge) et `malen` (la salle de jeux) reprennent `kita-bringen`.
- **Chez Jan et Katrin** : la chambre des enfants (`journee/familia-1`) pour `krank` et `packen`, la cuisine
  (`journee/familia-2`) pour `hausaufgaben`. Mark vient chercher Mia : c'est un ami de la famille.
### Le quartier de Mark, dans la rue — thème illustré « En ville : s'orienter » (4 nov. 2026)
- **Maître : la scène `kreuzung` de l'app** (`visuel/prototype/kreuzung.webp`, prompt
  `visuel/scenes/kreuzung.prompt.txt`) : façades crème et ocre pâle du vieux Berlin, quatre étages,
  hautes fenêtres, rez-de-chaussée commerçants ; trottoir pavé, lumière claire un peu couverte de fin
  de matinée ; rien d'écrit nulle part (pas d'enseigne, de nom, de plaque). La boulangerie, la
  pharmacie à la croix verte, la poste jaune, le café à l'auvent bordeaux et l'arrêt de bus au
  panneau rond jaune et vert viennent tels quels de cette image (recadrés, `visuel/ciudad/ciudad.py
  --recadrer`).
- Chaque photo d'un autre lieu du quartier (gare, mairie, banque, hôpital, musée, cinéma…) reçoit
  `kreuzung.webp` en première référence « pour la rue » et garde ces façades et cette lumière ; un
  lieu se reconnaît à ce qu'il montre (la croix, le guichet, l'horloge de gare), jamais à une
  enseigne.
- **Le plan du quartier** est dessiné par la page, pas photographié : la Gartenstraße (la rue de Mark,
  Gartenstraße 12) et la Bergstraße, croisées par la Lindenstraße, la Schulstraße et la Parkstraße.
  En espagnol, le même plan porte des noms de Madrid (calle Mayor, calle del Sol, calle de la Luna,
  calle de la Paz, calle del Prado) ; les photos restent celles de Berlin, comme les scènes.
### Les lieux du thème « Les fêtes et les invitations » (thème illustré, 5 nov. 2026)
- **Le salon de Jan et Katrin à Noël** (`visuel/prototype/fetes/weihnachten.webp`) : la pièce du chat, retouchée
  depuis son maître (armoire sombre à gauche, canapé gris clair aux coussins moutarde, étagère blanche, table en pin,
  hautes fenêtres à rideaux blancs) ; un sapin aux boules rouges et dorées devant le canapé. Anna y fête Noël avec Ben
  et Mia. Le **goûter d'anniversaire de Ben** (8 ans) s'y tiendra aussi (image à faire, même maître).
- **La rue de Silvester** (`silvester.webp`) : une rue d'Altbauten de Berlin la nuit, façades claires, un peu de
  neige au bord des trottoirs ; Anna, Lena et Felix aux cierges magiques.
- **Le jardin de Pâques** (`ostern.webp`) : une pelouse sous des pommiers en fleurs, des jonquilles ; Ben et Mia et
  leur panier d'œufs. Le jardin n'a pas de propriétaire dans l'histoire : ne pas le dire celui de quelqu'un sans le
  décider.
- **La cuisine de Mark** (`planen.webp`, mur vert sauge, réfrigérateur blanc à gauche, horloge ronde, étagère à
  vaisselle, table en bois) : Mark et Anna y préparent une fête.
- **Une porte d'appartement et sa cage d'escalier sombre** (`mitbringen.webp`) : Mark arrive avec un saladier chez
  une amie (inconnue, cheveux bruns en chignon). Pas encore l'appartement d'Anna.
- Madrid : **le salon des douze raisins** (`uvas.webp`) : guirlandes de papier multicolores, ballons dorés, la
  télévision qui montre l'horloge de la Puerta del Sol ; Carmen, Javier et Inés. Dans le thème, la Nochevieja a lieu
  chez Inés (calle del Pez 8).

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
