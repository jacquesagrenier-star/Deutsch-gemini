## Kanji N5 (branche claude/fervent-noether-2iwytm)

Suite de `.claude/brief-cloud-kanji.md`. Branche `claude/fervent-noether-2iwytm`, partie de `japonais-kanji-mnemo` ; la pull request vise `japonais-kanji-mnemo`, jamais `main`. Tout est dans `japonais/kanji/`.

### Ce qui est fait

1. **Deuxième note, « lien image-sens »**, pour les 79 kanji (`lien` + `lien_pourquoi` dans `textes/textes_n5.json`). Une mnémotechnique n'est proposée que si le son et le lien valent au moins « moyenne ».
2. **Verdicts de Jacques** dans `avis_jacques`, chacun avec le texte jugé (un verdict ne vaut que pour ce texte-là).
3. **Charte des sons** (`charte-des-sons.md`) : un rendu français fixé pour 16 sons difficiles. `construire.py` repère ces sons dans chaque lecture et exige un verdict par son (`charte` : `ok` ou `écart : …`), pour le texte, les réécritures et les deuxièmes lectures. Principe écrit en tête par Jacques : *un rendu n'est refusé que s'il fait retenir un autre son japonais*. Appliqué aussi à la voyelle longue (o ouvert accepté, le japonais n'a qu'un o) et à ei (« é-i » accepté, « a-i » refusé).
4. **Lecture enseignée** : champ `lecture_enseignee` (on / kun + kana) dans chaque texte, vérifié, affiché dans `a-relire.html`. Le script calcule la lecture la plus utile (celle du plus de mots JLPT N5 à N1) et signale les écarts, nets ou faibles.
5. **Deuxièmes mnémotechniques** (`autres_lectures`) pour les 8 écarts nets, avec exemples pris sur tous les niveaux : 中 チュウ (« tchou »), 人 ジン (« jean »), 女 ジョ (« Joconde »), 小 ショウ (« chausson »), 山 サン (« sanatorium »), 長 チョウ (« match aussi long »), 食 ショク (« show-cooking »), 高 コウ (« koala »). Pas encore de version anglaise.
6. **Lot 2 préparé** : une réécriture pour chacun des 20 kanji hors charte ou à note basse (七 万 五 八 六 十 千 南 右 左 年 校 百 半 本 東 名 水 父 白). Les nombres prennent une image qui porte le nombre (sept nains, pieuvre à huit bras, mouche à six pattes, X romain, mille-pattes, Ritz cinq étoiles) ; les h passent par un rire ou un cri soufflé.
7. **`a-relire.html`** : le lot en cours (avec texte actuel, réécriture et deuxième lecture, chacun noté son / lien / charte), puis le tableau des 79 kanji. Vérifié dans Chromium, clair, sombre et largeur téléphone.

États : validée 18, à juger 41, à réécrire 12, hors charte 8 (半 本 東 百 名 水 父 白, tous réécrits dans le lot 2).

### Ce que Jacques a validé ou refusé

- 4 oct. (pilote) : ok 一 山 火 大 中 出 北 休 東 高 今 毎 間 電 九 白 ; refusés 男 天 時 何. Depuis la charte, 東 et 白 sont hors charte (h ; « sirop » dit si et non chi) et ont une réécriture dans le lot 2.
- 7 oct. :
  - deux règles : la charte des sons, la lecture enseignée affichée ;
  - charte assouplie : r et j français acceptés ; h, chi, tsu, u, n final stricts ; principe « refusé seulement s'il fait retenir un autre son » ;
  - lot 1 : 男 version 1 (« Otto, costaud »), 天 version 1 (Atlas, « Athènes »), 時 version 1 (« djinn »), 何 version 1 (« Nanette ») ;
  - les 8 écarts nets : garder la lecture enseignée, ajouter une mnémotechnique pour la plus utile.
- **Lot 2 : en attente de son verdict.**

### À vérifier avec lui

- Le principe touche deux textes que la charte ne voit pas, parce que le son en trop vient du mot français et non de la lecture : « djinn » (時 ji, qu'il a choisi) fait entendre じん, et « tchin » (小 chii) fait entendre ちん. Faut-il une règle « son en trop » ?
- Le h : le français ne le prononce pas. Les réécritures passent par un rire (« hi hi hi », « ho ho ho ») ou un cri (« Hia ! »). C'est le mieux qu'on puisse écrire ; l'audio fera le reste.
- La lecture « la plus utile » est un compte de mots dans les listes JLPT, pas une fréquence d'usage. Il reste 19 écarts faibles, non traités.

### Ce qui reste

- Le verdict de Jacques sur le lot 2.
- Lot 3 : les 8 deuxièmes lectures et 12 kanji à juger ; lot 4 : 20 à juger ; lot 5 : les 9 derniers.
- Le périmètre : `kanji.json` compte 79 kanji N5, pas 103 ; les 23 de l'ancien niveau 4 rangés en N4 ne sont pas traités.
- Les versions anglaises des réécritures et des deuxièmes lectures.
- Un relecteur japonais natif pour les lectures et pour la charte.
- La pull request vers `japonais-kanji-mnemo`, à la fin des lots.
- `node tests/retours.js` n'a pas pu tourner : la clé de lecture est sur le poste de Jacques, pas dans le conteneur cloud.
