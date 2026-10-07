# Compte rendu : mnémoniques des kanji N5 (session cloud du 7 oct. 2026)

Suite de `.claude/brief-cloud-kanji.md`. Travail sur la branche `claude/fervent-noether-2iwytm`, partie de `japonais-kanji-mnemo`. La pull request vise `japonais-kanji-mnemo`, jamais `main`.

## Ce qui est fait

1. **Deuxième note, « lien image-sens »**, pour les 79 kanji (`lien` + `lien_pourquoi` dans `textes/textes_n5.json`). `construire.py` la vérifie, en tire un `etat` et ne propose une mnémotechnique que si les deux notes valent au moins « moyenne ».
   - Lien : haute 41, moyenne 21, basse 17.
   - États : validée 16, refusée 4, à juger 44, à réécrire 15.
   - À réécrire (une note basse) : 七 万 五 八 六 十 千 半 南 右 左 年 本 校 百. Constat : **les nombres** (七 八 六 十 千 百 万 五) et **les directions** (南 右 左) tombent presque tous en lien bas. Un nombre ou une direction n'a pas d'image propre ; il faudra une idée par kanji, ou une convention (par ex. pour les nombres, une scène où l'on *compte* les objets du dessin, comme 三 = trois tranches).
2. **Verdicts du pilote du 4 oct. enregistrés** dans `avis_jacques` (16 ok, 4 refusés), chacun avec le texte jugé. Les remarques de Jacques n'étaient pas dans le brief : champ `remarque` vide.
3. **Deux réécritures pour 男 天 時 何** (`propositions_fr`), vérifiées par `construire.py` (sens, lecture, gras, composants).
4. **`a-relire.html` refait** : le lot en cours (lot 1 = ces quatre réécritures), puis le tableau des 79 kanji avec leurs deux notes et leur état.

## Ce que Jacques a validé ou refusé

- Le 4 oct. (pilote) : ok 一 山 火 大 中 出 北 休 東 高 今 毎 間 電 九 白 ; refusés 男 天 時 何.
- Le 7 oct. (lot 1, réécritures) : **en attente de son verdict.**

## À vérifier avec lui

- L'hypothèse « l'image mène au sens » n'explique pas tout : 電 (Denver), 毎 (maïs), 北 (« qui t'a envoyé au nord ») ont été acceptés avec un lien lâche, et 九, 白 avec un son noté bas. À confirmer sur les réécritures avant d'étendre.

## Ce qui reste

- Le verdict de Jacques sur le lot 1, puis, si la règle se confirme, les 59 kanji non jugés par lots de 20 (dont les 15 à réécrire).
- Le périmètre : `kanji.json` compte 79 kanji N5, pas 103 (voir LISEZ-MOI, « Écart 79 / 103 ») ; les 23 de l'ancien niveau 4 rangés en N4 ne sont pas traités.
- Un relecteur japonais natif pour les lectures (inchangé).
- `node tests/retours.js` n'a pas pu tourner : la clé de lecture est sur le poste de Jacques, pas dans le conteneur cloud.
