# Scènes japonaises — prototypes (12 oct. 2026)

Trois scènes interactives pour la future version japonaise de Wortando, au stade
de **prototype** : image, zones, masques SAM 2 et lexique. **Rien n'est branché
dans l'app** — le moteur (`index.html`, `construire.py`) ne connaît pas le
japonais. Aucune scène allemande ou espagnole n'a été touchée.

Dépense : **3 appels fal à 0,15 $ = 0,45 $**, une seule prise par scène, comme
convenu. Les deux retouches (konbini, eki) sont locales et gratuites
(`visuel/effacer_texte.py`).

| Scène | Image source | Prompt | Zones | Mots | Masques |
|---|---|---|---|---|---|
| `konbini` — コンビニで | `visuel/scenes/konbini-propre.png` (retouche de `konbini.png`) | `visuel/scenes/konbini.prompt.txt` | 36 | 40 | `masques-konbini.js`, 36/36 |
| `eki` — 駅で | `visuel/scenes/eki-propre.png` (retouche de `eki.png`) | `visuel/scenes/eki.prompt.txt` | 30 | 39 | `masques-eki.js`, 30/30 |
| `genkan` — 玄関で | `visuel/scenes/genkan.png` (telle quelle) | `visuel/scenes/genkan.prompt.txt` | 39 | 47 | `masques-genkan.js`, 39/39 |

Les images web (`<nom>.webp`, 1536 px, qualité 90) et les `<nom>.points.json`
sont dans ce dossier, les reçus fal (`<nom>-fal.json`) et les zones d'effacement
(`<nom>-effacer.json`) dans `visuel/scenes/`. Les PNG sources restent hors
dépôt, comme pour les autres scènes.

## Ce qui a été fait

1. **Prompts** sur le modèle des scènes allemandes (photo réelle, 9:16, 24 mm,
   bandes du bas vers le haut, « every surface is plain »), relus contre les
   34 règles de `video/verifier_prompt.py` : les trois passent le contrôle
   (jeu `POUR_IMAGE`, 0 faute). Au Japon tout est écrit : chaque prompt dit
   explicitement que les emballages sont d'une couleur unie, les étiquettes des
   cartes blanches vierges, les écrans sombres, les panneaux des rectangles
   unis — sans jamais employer une négation (règle `garde-negative`).
2. **Génération** : `python visuel/generer_scene.py <nom> --format 9:16 --payer`,
   une fois chacune. Les trois sont des **photos** (pas des dessins), la
   composition suit le prompt bande par bande, les visages et les mains sont
   justes.
3. **Zones** mesurées sur une grille de 1 % (outil de scratchpad, source
   1536 × 2752), avec les règles de la mémoire : une cible est un MOT et tous
   ses exemplaires (cinq paires de chaussures, quatre portillons, trois
   coussins, trois affiches), un rôle vaut pour le groupe (客 pour la cliente ET
   le vieux monsieur, 人 sur chaque personne, 乗客 sur les trois voyageurs), ce
   qui est posé SUR un objet a `sur` (le chat sur le coussin, le vase sur le
   meuble, les onigiri dans la vitrine). Objets partiellement cachés en
   `rigide: "rectangle"` (fenêtres, télés, affiches, distributeur, guichet,
   meuble à chaussures) ; sols, murs, plafond, quai en `plein`.
4. **Détourage** : `python visuel/prototype/detourer.py <nom> --voir` (SAM 2
   local). Chaque masque a été regardé sur un rendu des tracés vectoriels
   (deux moitiés d'image par scène) : **tous collent à leur objet**, aucune
   reprise n'a été nécessaire. Détails ci-dessous.

## Format : ce qui change pour le japonais

Les `points.json` gardent **exactement** les champs des scènes allemandes
(`id`, `mot`, `boite`/`boites`, `aussi`, `sur`, `rigide`, `sam`, `plein`,
`devant`, `exclus`, `titre`, `alt`, `consigne`, `image`, `source`) : `detourer.py`
les lit tels quels. Deux ajouts, qui ne cassent rien :

- `mot` et `aussi` contiennent des **mots japonais**, dans la forme du corpus
  (kanji quand le corpus l'écrit en kanji, sinon kana : 時計, かばん, テレビ).
- une table **`lexique`** à la racine du fichier : pour chaque mot de la scène,
  `kana` (lecture), `fr` (traduction), `jmdict` (id de l'entrée, `null` hors
  corpus), `niveau` (N5/N4/N3, ou « hors N5-N3 »), et `fr_source: "manuel"`
  quand le corpus N3 n'a pas encore sa glose française (j'ai écrit la mienne).
- `titre_fr` à côté de `titre` (le titre est en japonais).

Source des mots : `origin/japonais-cartes:japonais/cartes/mots-n5.json`,
`mots-n4.json`, `mots-n3.json` (champs `ecritures`, `gloses.fr.affichee`,
`id`). Le choix de forme suit le corpus : `お弁当` (N5, jmdict:1513065) plutôt
que `弁当` (N3) ; `かばん` en kana.

## Défauts des images (aucune régénération faite)

**konbini** — les six gobelets de nouilles du rayon de gauche portaient une
marque lisible en lettres latines (« CUP NOODLE », exactement la leçon
`fruit-a-etiquette` : nommer un produit convoque son emballage). Effacé en
local : les quatre gobelets de devant sont repeints en blanc uni
(`konbini-effacer.json`, mode `poly` + `echantillon`), les deux de derrière
inpaintés ; il reste des bribes de lettres sur les gobelets du fond, illisibles
à la taille de l'app. Le reste du faux texte (badge du caissier, cartes des
bento, étiquettes des bouteilles) est illisible à toute taille. Si Jacques
veut une image sans retouche : ajouter au prompt « instant-noodle cups with
plain white paper sides and a plain white lid ».

**eki** — l'afficheur de destination du train montrait deux kanji en rouge
(le prompt disait « dark » : un écran éteint s'est quand même allumé), et le
panneau au-dessus du distributeur de billets était un vrai plan de lignes avec
ses noms de gares en petit (« plain grey map board » a donné un plan). Les deux
sont effacés en local (`eki-effacer.json`, mode `tout`) : afficheur sombre,
panneau gris uni. Reste du faux texte minuscule sur les portillons (numéros
« 4 »), le distributeur de boissons et les écrans du distributeur de billets :
illisible. Prompt corrigé proposé : « above the doors, a dark unlit
rectangular panel » et « a plain mid-grey board, empty, above it ».

**genkan** — aucun texte. Un écart d'usage à montrer à Jacques : le jeune homme
a encore **une chaussure au pied posée sur le plancher** de la maison (le
prompt la voulait sur le carrelage, l'autre pied en chaussette sur le bois ; le
modèle a inversé). Au Japon on ne pose pas une chaussure sur le plancher. Pour
une reprise : « he sits on the step facing the door, both feet on the tiles,
one shoe already off beside him ». Le sceau rouge et la signature de l'estampe
du Fuji sont une œuvre, pas une étiquette ; le climatiseur au mur du salon n'a
pas de zone (エアコン absent du corpus).

## État des masques

- **konbini** (36) : tous justes. Le frigo (冷蔵庫) a deux encoches là où SAM a
  exclu le bras du vieux monsieur et la bouteille qu'il tient (la bouteille
  est sa propre zone お茶) ; la caisse (レジ) = comptoir + tiroir-caisse ; les
  boissons dans le frigo sont une zone `plein` posée `sur` le frigo.
- **eki** (30) : tous justes. Le train passe derrière le pilier et le
  distributeur sans trou ; le banc est coupé par la vieille dame (39 % de sa
  boîte, normal) ; les quatre portillons sont quatre zones ; les lignes jaunes
  (deux bandes) et le quai (deux bandes) sont `plein` avec deux boîtes.
- **genkan** (39) : tous justes, jusqu'aux clés dans leur coupelle et aux deux
  tasses. Le kotatsu = plateau + couverture ; le coussin de droite est
  minuscule (36 % de sa boîte, il est presque caché par la table).
- ⚠️ **Rien n'a été vérifié au toucher dans un navigateur** : la page
  `index.html` du prototype lit `scene-<nom>.js`, que seul `construire.py`
  produit, et il refuse tout mot absent de `themes.json`. Les zones viennent
  de la grille, pas d'un clic.

## Mots hors du corpus N5-N3

À ajouter au corpus japonais (ou à décider) avant que ces scènes soient
jouables — avec la lecture et la traduction que j'ai mises dans `lexique` :

- konbini : コンビニ (titre), おにぎり, 電子レンジ (でんしレンジ), カップ麺
  (カップめん), ショーケース — お弁当, lui, est dans le corpus (N5).
- eki : 改札 (かいさつ), 券売機 (けんばいき), 自動販売機 (じどうはんばいき),
  駅員 (えきいん), 窓口 (まどぐち), 線路 (せんろ), 柱 (はしら), ごみ箱 (ごみばこ),
  リュック, 制服 (せいふく).
- genkan : こたつ, 座布団 (ざぶとん), 急須 (きゅうす), みかん, 障子 (しょうじ),
  靴箱 (くつばこ) / 下駄箱 (げたばこ), 傘立て (かさたて), 上がり框 (あがりかまち).

Glose française écrite à la main (N3 sans traduction dans le corpus) : 広告,
瓶, かご, 袋, ジュース, 床, 屋根, 列車, 乗客, ベンチ, ホーム, 植物, 居間.

## Ce qu'il faudra au moteur pour jouer ces scènes en japonais

1. **Un corpus japonais lisible par `construire.py`** (aujourd'hui il ne lit
   que `themes.json`, `verbe.json`, `adjectif.json` allemands) : les trois
   `mots-nX.json` de la branche, avec les mots hors corpus ajoutés.
2. **Pas de genre, pas d'article** : les étiquettes allemandes affichent
   « der/die/das + mot » ; en japonais l'étiquette doit montrer le **mot, sa
   lecture en kana (furigana) et la traduction**, et la couche A1 s'appelle
   autrement que « Noms et articles ». Prévoir l'affichage du furigana
   au-dessus des kanji (le corpus a le champ `furigana`).
3. **Trouve ! en japonais** : la question « Où est … ? » devient
   「…はどこ？」 ; la voix (ElevenLabs japonais, à choisir et à payer) ; les
   mots à plusieurs lectures.
4. **Les couches A2-C1** (N4-N3 ici) ne sont pas écrites : particules de lieu
   (に / で / の上に / の中に), verbes de position (ある / いる), compteurs
   (一つ, 一本, 一足 pour les chaussures), formes polies au konbini
   (「温めますか？」). Même logique que le salon allemand : une couche par
   niveau, sur la même image.
5. **Polices** : vérifier qu'une police japonaise est servie (sinon les kanji
   tombent en police système, inégale selon l'appareil) et que le `lang="ja"`
   est posé sur les étiquettes (les glyphes han diffèrent entre ja et zh).
6. La page de prototype suppose un « genre » et un « theme » par mot
   (`sens(m)`, `m["genre"]`) : à rendre optionnels.

## Mots de la scène `konbini` — コンビニで (Au konbini)

| Mot | Lecture | Français | Niveau | JMdict | Zones |
|---|---|---|---|---|---|
| おじいさん | おじいさん | grand-père ; homme âgé | N5 | jmdict:1002320 | ojiisan (aussi) |
| お弁当 | おべんとう | bento | N5 | jmdict:1513065 | obentou |
| お茶 | おちゃ | thé (vert) | N5 | jmdict:1002430 | ocha |
| お菓子 | おかし | friandises ; gâteaux | N5 | jmdict:1001710 | okashi |
| お金 | おかね | argent | N5 | jmdict:1001820 | okane |
| かばん | かばん | sac | N5 | jmdict:1208910 | kaban |
| コート | コート | manteau | N5 | jmdict:1049000 | kyaku (aussi) |
| テレビ | テレビ | télévision | N5 | jmdict:1080510 | terebi |
| ドア | ドア | porte (à l'occidentale) | N5 | jmdict:1087820 | mado (aussi) |
| パン | パン | pain | N5 | jmdict:1103090 | pan |
| 人 | ひと | personne | N5 | jmdict:1580640 | ten-in (aussi), kyaku (aussi), ojiisan (aussi) |
| 傘 | かさ | parapluie | N5 | jmdict:1301940 | kasa |
| 冷蔵庫 | れいぞうこ | réfrigérateur | N5 | jmdict:1557110 | reizouko |
| 女 | おんな | femme | N5 | jmdict:1344930 | kyaku (aussi) |
| 帽子 | ぼうし | chapeau | N5 | jmdict:1519170 | boushi |
| 時計 | とけい | montre ; horloge | N5 | jmdict:1316140 | tokei |
| 水 | みず | eau | N5 | jmdict:1371260 | nomimono (aussi) |
| 牛乳 | ぎゅうにゅう | lait | N5 | jmdict:1231590 | nomimono (aussi) |
| 男 | おとこ | homme | N5 | jmdict:1419990 | ten-in (aussi), ojiisan (aussi) |
| 窓 | まど | fenêtre | N5 | jmdict:1401400 | mado |
| 箱 | はこ | boîte | N5 | jmdict:1585650 | hako |
| 車 | くるま | voiture | N5 | jmdict:1323080 | kuruma |
| 電気 | でんき | électricité ; lumière (électrique) | N5 | jmdict:1443000 | denki |
| 飲み物 | のみもの | boisson | N5 | jmdict:1600430 | ocha (aussi), nomimono |
| サンドイッチ | サンドイッチ | sandwich | N4 | jmdict:1058580 | sandoitchi |
| レジ | レジ | caisse (de paiement) | N4 | jmdict:1145130 | reji |
| 壁 | かべ | mur | N4 | jmdict:1509290 | kabe |
| 客 | きゃく | invité ; client | N4 | jmdict:1226630 | kyaku, ojiisan |
| 店員 | てんいん | vendeur ; employé de magasin | N4 | jmdict:1440670 | ten-in |
| 棚 | たな | étagère | N4 | jmdict:1416700 | tana-ushiro, tana-hidari, shookeesu (aussi) |
| かご | かご | panier *(manuel)* | N3 | jmdict:1590200 | kago-reji, kago |
| ジュース | ジュース | jus (de fruits) *(manuel)* | N3 | jmdict:1065950 | nomimono (aussi) |
| 広告 | こうこく | publicité ; affiche *(manuel)* | N3 | jmdict:1278510 | koukoku-hidari, koukoku-ue, koukoku-migi |
| 床 | ゆか | sol ; plancher *(manuel)* | N3 | jmdict:1349380 | yuka |
| 瓶 | びん | bouteille *(manuel)* | N3 | jmdict:1491120 | bin, ocha (aussi), nomimono (aussi) |
| 袋 | ふくろ | sac (en plastique, en papier) *(manuel)* | N3 | jmdict:1411070 | fukuro |
| おにぎり | おにぎり | boulette de riz (onigiri) | hors N5-N3 | — | onigiri |
| カップ麺 | カップめん | nouilles instantanées en gobelet | hors N5-N3 | — | kappumen |
| ショーケース | ショーケース | vitrine réfrigérée | hors N5-N3 | — | shookeesu |
| 電子レンジ | でんしレンジ | four à micro-ondes | hors N5-N3 | — | denshi-renji |

## Mots de la scène `eki` — 駅で (À la gare)

| Mot | Lecture | Français | Niveau | JMdict | Zones |
|---|---|---|---|---|---|
| おばあさん | おばあさん | grand-mère ; vieille dame | N5 | jmdict:1002330 | obaasan |
| かばん | かばん | sac | N5 | jmdict:1208910 | kaban, ryukku (aussi) |
| コート | コート | manteau | N5 | jmdict:1049000 | obaasan (aussi) |
| ドア | ドア | porte (à l'occidentale) | N5 | jmdict:1087820 | doa |
| 人 | ひと | personne | N5 | jmdict:1580640 | otoko (aussi), onnanoko (aussi), obaasan (aussi), ekiin (aussi) |
| 地図 | ちず | carte ; plan | N5 | jmdict:1421290 | chizu |
| 女 | おんな | femme | N5 | jmdict:1344930 | obaasan (aussi) |
| 女の子 | おんなのこ | fille ; petite fille | N5 | jmdict:1344970 | onnanoko |
| 学生 | がくせい | étudiant | N5 | jmdict:1206900 | onnanoko (aussi) |
| 帽子 | ぼうし | chapeau | N5 | jmdict:1519170 | boushi |
| 時計 | とけい | montre ; horloge | N5 | jmdict:1316140 | tokei |
| 男 | おとこ | homme | N5 | jmdict:1419990 | otoko, ekiin (aussi) |
| 窓 | まど | fenêtre | N5 | jmdict:1401400 | mado-densha, madoguchi (aussi) |
| 背広 | せびろ | costume (pour homme) | N5 | jmdict:1472740 | otoko (aussi) |
| 荷物 | にもつ | bagages | N5 | jmdict:1195430 | suutsukeesu (aussi) |
| 階段 | かいだん | escalier | N5 | jmdict:1203090 | kaidan |
| 電車 | でんしゃ | train | N5 | jmdict:1443530 | densha |
| 飲み物 | のみもの | boisson | N5 | jmdict:1600430 | nomimono |
| 黄色 | きいろ | jaune | N5 | jmdict:1576760 | sen (aussi) |
| ごみ | ごみ | ordures ; déchets | N4 | jmdict:1369900 | gomibako (aussi) |
| スーツ | スーツ | costume | N4 | jmdict:1066680 | otoko (aussi) |
| スーツケース | スーツケース | valise | N4 | jmdict:1066690 | suutsukeesu |
| 線 | せん | ligne | N4 | jmdict:1391780 | sen |
| ベンチ | ベンチ | banc *(manuel)* | N3 | jmdict:1120280 | benchi |
| ホーム | ホーム | quai *(manuel)* | N3 | jmdict:1121740 | hoomu |
| 乗客 | じょうきゃく | passager ; voyageur *(manuel)* | N3 | jmdict:1580490 | otoko (aussi), onnanoko (aussi), obaasan (aussi) |
| 列車 | れっしゃ | train *(manuel)* | N3 | jmdict:1558370 | densha (aussi) |
| 屋根 | やね | toit *(manuel)* | N3 | jmdict:1182700 | yane |
| 床 | ゆか | sol ; plancher *(manuel)* | N3 | jmdict:1349380 | yuka |
| ごみ箱 | ごみばこ | poubelle | hors N5-N3 | — | gomibako |
| リュック | リュック | sac à dos | hors N5-N3 | — | ryukku |
| 制服 | せいふく | uniforme | hors N5-N3 | — | ekiin (aussi) |
| 券売機 | けんばいき | distributeur de billets | hors N5-N3 | — | kenbaiki |
| 改札 | かいさつ | portillon (de gare) ; contrôle des billets | hors N5-N3 | — | kaisatsu-1, kaisatsu-2, kaisatsu-3, kaisatsu-4 |
| 柱 | はしら | pilier ; poteau | hors N5-N3 | — | hashira |
| 窓口 | まどぐち | guichet | hors N5-N3 | — | madoguchi |
| 線路 | せんろ | voie ferrée ; rails | hors N5-N3 | — | senro |
| 自動販売機 | じどうはんばいき | distributeur automatique (de boissons) | hors N5-N3 | — | jihanki |
| 駅員 | えきいん | employé de gare | hors N5-N3 | — | ekiin |

## Mots de la scène `genkan` — 玄関で (À l'entrée de la maison)

| Mot | Lecture | Français | Niveau | JMdict | Zones |
|---|---|---|---|---|---|
| お茶 | おちゃ | thé (vert) | N5 | jmdict:1002430 | kyuusu (aussi) |
| カップ | カップ | tasse | N5 | jmdict:1037670 | chawan (aussi) |
| コート | コート | manteau | N5 | jmdict:1049000 | kooto |
| スリッパ | スリッパ | pantoufles | N5 | jmdict:1073900 | surippa |
| ズボン | ズボン | pantalon | N5 | jmdict:1074260 | otoko (aussi) |
| セーター | セーター | pull-over | N5 | jmdict:1074270 | otoko (aussi) |
| テレビ | テレビ | télévision | N5 | jmdict:1080510 | terebi |
| テーブル | テーブル | table | N5 | jmdict:1078630 | kotatsu (aussi) |
| 上着 | うわぎ | veste ; manteau | N5 | jmdict:1580340 | kooto (aussi) |
| 人 | ひと | personne | N5 | jmdict:1580640 | onna (aussi), otoko (aussi) |
| 傘 | かさ | parapluie | N5 | jmdict:1301940 | kasa |
| 女 | おんな | femme | N5 | jmdict:1344930 | onna |
| 帽子 | ぼうし | chapeau | N5 | jmdict:1519170 | boushi |
| 廊下 | ろうか | couloir | N5 | jmdict:1560670 | rouka |
| 戸 | と | porte (à la japonaise) | N5 | jmdict:1266970 | to |
| 時計 | とけい | montre ; horloge | N5 | jmdict:1316140 | tokei |
| 果物 | くだもの | fruit | N5 | jmdict:1193060 | mikan (aussi) |
| 猫 | ねこ | chat | N5 | jmdict:1467640 | neko |
| 玄関 | げんかん | entrée ; hall d'entrée | N5 | jmdict:1263400 | genkan |
| 男 | おとこ | homme | N5 | jmdict:1419990 | otoko |
| 窓 | まど | fenêtre | N5 | jmdict:1401400 | mado |
| 絵 | え | dessin ; peinture | N5 | jmdict:1202270 | e |
| 花 | はな | fleur | N5 | jmdict:1194500 | hana |
| 花瓶 | かびん | vase (à fleurs) | N5 | jmdict:1194870 | kabin |
| 茶碗 | ちゃわん | bol ; tasse | N5 | jmdict:1597530 | chawan |
| 部屋 | へや | pièce ; chambre | N5 | jmdict:1499320 | heya |
| 鍵 | かぎ | clé | N5 | jmdict:1260490 | kagi |
| 電気 | でんき | électricité ; lumière (électrique) | N5 | jmdict:1443000 | denki |
| 靴 | くつ | chaussure | N5 | jmdict:1246700 | kutsu-te, kutsu-kuro, kutsu-chairo, kutsu-shiro, kutsu-aka |
| 靴下 | くつした | chaussettes | N5 | jmdict:1246740 | kutsushita |
| 壁 | かべ | mur | N4 | jmdict:1509290 | kabe |
| 女性 | じょせい | femme | N4 | jmdict:1345250 | onna (aussi) |
| 棚 | たな | étagère | N4 | jmdict:1416700 | tana, kutsubako (aussi) |
| 畳 | たたみ | tatami | N4 | jmdict:1356750 | tatami |
| 電灯 | でんとう | lumière électrique ; lampe | N4 | jmdict:1443660 | denki (aussi) |
| 居間 | いま | salon ; pièce à vivre *(manuel)* | N3 | jmdict:1231720 | heya (aussi) |
| 床 | ゆか | sol ; plancher *(manuel)* | N3 | jmdict:1349380 | rouka (aussi) |
| 植物 | しょくぶつ | plante *(manuel)* | N3 | jmdict:1357300 | shokubutsu |
| こたつ | こたつ | kotatsu (table basse chauffante) | hors N5-N3 | — | kotatsu |
| みかん | みかん | mandarine (satsuma) | hors N5-N3 | — | mikan |
| 上がり框 | あがりかまち | marche du genkan | hors N5-N3 | — | agarikamachi |
| 下駄箱 | げたばこ | meuble à chaussures (getabako) | hors N5-N3 | — | kutsubako (aussi) |
| 傘立て | かさたて | porte-parapluies | hors N5-N3 | — | kasatate |
| 座布団 | ざぶとん | coussin de sol (zabuton) | hors N5-N3 | — | zabuton-1, zabuton-2, zabuton-3 |
| 急須 | きゅうす | théière (japonaise) | hors N5-N3 | — | kyuusu |
| 障子 | しょうじ | cloison coulissante en papier (shōji) | hors N5-N3 | — | to (aussi) |
| 靴箱 | くつばこ | meuble à chaussures | hors N5-N3 | — | kutsubako |

