## Kanji N5 (branche claude/fervent-noether-2iwytm)

Suite de `.claude/brief-cloud-kanji.md`. Branche `claude/fervent-noether-2iwytm`, partie de `japonais-kanji-mnemo` ; la pull request vise `japonais-kanji-mnemo`, jamais `main`. Tout est dans `japonais/kanji/`.

### Ce qui est fait

1. **Deuxième note, « lien image-sens »**, pour les 79 kanji (`lien` + `lien_pourquoi` dans `textes/textes_n5.json`). Une mnémotechnique n'est proposée que si le son et le lien valent au moins « moyenne ». Lien : haute 41, moyenne 21, basse 17.
2. **Verdicts du pilote du 4 oct.** dans `avis_jacques` (16 ok, 4 refusés), chacun avec le texte jugé ; un verdict ne vaut que pour ce texte-là. Les remarques de Jacques n'étaient pas dans le brief : `remarque` vide.
3. **Deux réécritures pour 男 天 時 何** (`propositions_fr`). Celles de 時 (« j'y », « gigantesque ») et la version 1 de 何 (« Nantes ») étaient hors charte : remplacées par « djinn », « jingle » et « Nanette ».
4. **Charte des sons** (`charte-des-sons.md`, demandée par Jacques le 7 oct.) : un rendu français fixé pour 16 sons difficiles (u, voyelle longue, ei, r, h, fu, tsu, chi, shi, ji, g, s, w, yoon, n final, consonne double). `construire.py` repère ces sons dans chaque lecture et exige un verdict par son (`charte` : `ok` ou `écart : …`), pour le texte comme pour les réécritures.
   - **13 mnémotechniques hors charte** : 上 (ji : « jaune »), 人 (r), 円 (r), 来 (r), 左 (r), 白 (r et shi : « sirop »), 半 (h muet : « hanneton »), 本 (h muet : « honneur »), 東 (h : « il gâchit »), 百 (h et consonne perdue : « yakuzas »), 名 (ei : « maïs » dit ma-is), 水 (u : « suis »), 父 (chi : « chichis » dit chi, pas tchi). Plus 何, déjà refusé (« Nan » nasal).
   - **Dont deux validées par Jacques le 4 oct. : 東 et 白.** La charte les fait repasser à réécrire.
5. **Lecture enseignée** (demandée le 7 oct.) : champ `lecture_enseignee` (type on / kun + kana) dans chaque texte, vérifié contre la lecture retenue, affiché dans `a-relire.html` (« on (sino-japonaise) » ou « kun (japonaise) »). Le script calcule aussi la lecture **la plus utile** = celle que portent le plus de mots JLPT N5 à N1.
   - **Écart net** (8 kanji, la plus utile porte au moins deux fois plus de mots, et 5 de plus) : 中 なか → チュウ (9 / 36 mots), 人 り → ジン (4 / 33), 女 おんな → ジョ (3 / 9), 小 ちい → ショウ (2 / 9), 山 やま → サン (1 / 8), 長 なが → チョウ (3 / 19), 食 た → ショク (2 / 16), 高 たか → コウ (4 / 12).
   - **Écart faible** (19 kanji, petits comptes) : 万 五 休 入 円 前 北 十 南 友 四 大 子 左 日 東 読 間 雨.
   - Limite : c'est un compte de mots dans les listes JLPT, pas une fréquence d'usage. Il favorise les lectures on, qui servent dans les composés des niveaux avancés ; un débutant croise d'abord les kun (山 やま, 女 おんな). À trancher avec Jacques, puis un relecteur natif.
6. **`a-relire.html` refait** : le lot en cours (lot 1 = les quatre réécritures) avec, pour chaque version, son, lien, charte et lecture enseignée ; puis le tableau des 79 kanji avec leur état. Vérifié dans Chromium en clair, sombre et largeur téléphone.

États au 7 oct. : validée 14, refusée 4, hors charte 13, à juger 37, à réécrire 11.

### Ce que Jacques a validé ou refusé

- 4 oct. (pilote) : ok 一 山 火 大 中 出 北 休 東 高 今 毎 間 電 九 白 ; refusés 男 天 時 何. Depuis la charte, 東 et 白 sont hors charte.
- 7 oct. : il a fixé deux règles (charte des sons ; lecture enseignée affichée). **Verdict sur le lot 1 (réécritures de 男 天 時 何) : en attente.**

### À vérifier avec lui

- L'hypothèse « l'image mène au sens » n'explique pas tout le pilote : 電 (Denver), 毎 (maïs), 北 ont passé avec un lien lâche, 九 et 白 avec un son noté bas.
- Les choix de la charte sont fermes et discutables : r rendu par « l » (pas par le r français), « dj » obligatoire pour じ, h qui doit s'entendre. Les changer change le nombre de mnémotechniques hors charte.
- Quelle lecture enseigner quand la plus utile n'est pas la retenue (8 écarts nets) : changer de lecture (`lecture_derogation`), ou écrire une deuxième mnémotechnique pour l'autre lecture.

### Ce qui reste

- Le verdict de Jacques sur le lot 1, puis les autres kanji par lots de 20 : d'abord les 13 hors charte et les 11 à réécrire (nombres et directions surtout), puis les 37 à juger.
- Le périmètre : `kanji.json` compte 79 kanji N5, pas 103 ; les 23 de l'ancien niveau 4 rangés en N4 ne sont pas traités.
- Un relecteur japonais natif pour les lectures et pour la charte elle-même.
- `node tests/retours.js` n'a pas pu tourner : la clé de lecture est sur le poste de Jacques, pas dans le conteneur cloud.
