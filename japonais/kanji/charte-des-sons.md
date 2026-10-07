# Charte des sons : le japonais difficile et son rendu en français

**Une règle par son, fixée une fois pour toutes.** Une mnémotechnique française fait entendre la lecture japonaise par un mot ou un bout de phrase français, le morceau en **gras**. Ce tableau dit, pour chaque son japonais qu'un francophone entend mal, comment ce morceau doit l'écrire, et ce qui est refusé.

- `construire.py` lit les identifiants de la première colonne (entre accents graves). Pour chaque lecture, il repère les sons de la charte qu'elle contient. Chaque mnémotechnique doit alors donner un verdict pour chacun de ces sons, dans son champ `charte` : `"ok"`, ou `"écart : …"` avec la raison.
- Une mnémotechnique qui a un écart est **hors charte**, même si Jacques l'a validée. Elle est à réécrire.
- Les sons faciles (a, i, k, m, p, t…) ne sont pas dans la charte : le français les a tels quels.
- Les sons se jugent à l'oreille, pas sur l'orthographe : « dos » rend bien *do*, parce que le s ne se prononce pas.

## Voyelles

| id | Son japonais | Ce qu'il faut entendre | Rendu français retenu | Refusé |
|---|---|---|---|---|
| `u` | う et toutes les syllabes en u (ku, su, mu, yu…) | un « ou » détendu, lèvres peu arrondies | **« ou »** : *cou*, *mouche*, *sous*, *gag cou(rt)* | le u français [y] : *suis*, *tu*, *bus* |
| `voyelle-longue` | ō, ū, ā, ē, ii (おう, とお, くう, ちい…) | la même voyelle, tenue deux fois plus longtemps | **la voyelle seule**, de bonne couleur ; pour ō, un o fermé : *tôt*, *côte*, *au*, *eau*. La longueur n'a pas d'équivalent en français : c'est le macron du romaji qui l'enseigne. | un o ouvert pour ō (*cotte*, *col*) ; deux syllabes (*o-o*) |
| `ei` | えい (めい, せい) | presque toujours un « é » long, pas « é-i » | **« é », « è », « ai » (lu è)** : *seize*, *mai*, *mère* | « a-i » ou « é-i » en deux sons : *maïs*, *pays* |

## Consonnes

| id | Son japonais | Ce qu'il faut entendre | Rendu français retenu | Refusé |
|---|---|---|---|---|
| `r` | ら り る れ ろ | une seule frappe de la langue derrière les dents, entre l et d | **« l »** : *lit* pour り, *l'ail* pour ライ, *lot* pour ろ | le r français, roulé dans la gorge : *rit*, *rail*, *roue*, *sirop* |
| `h` | は ひ へ ほ (et ひゃ…) | un souffle audible, comme dans *hop !* | **un h qui s'entend** : interjection ou mot anglais prononcé avec son souffle (*hop*, *ha !*, *hi*, *hello*, *hot-dog*) | un h muet ou « aspiré » du français, qui ne s'entend pas : *honneur*, *hanneton*, *haricot* ; ou pas de h du tout (*yakuza* pour ひゃく) |
| `fu` | ふ | souffle entre les deux lèvres, entre f et h | **« fou »** : *foot*, *fourmi* | « fu » [fy], « hu » |
| `tsu` | つ | t et s collés, comme dans *tsar* | **« ts » + « ou »**, dans un mot (*tsunami*, *tsé-tsé*) ou à cheval sur deux (*guette sous*, *hits ou*) | « tu », « sou » ou « tou » seuls |
| `chi` | ち (et ちゃ, ちょ…) | « tchi » | **« tch »** : *litchi*, *tchin*, *match* | « chi » [ʃi], qui est し : *chichis*, *chiche* |
| `shi` | し (et しゃ, しょ…) | « chi » | **« ch »** : *chat*, *chaud*, *nichée* | « s » : *sirop*, *si* |
| `ji` | じ (et じゃ, じょ…) | « dji », d et j collés | **« dj »** : *Djibouti*, *djinn*, *jingle*, *jean* (dit djinn), *jazz* | le j français seul [ʒ] : *jaune*, *j'y*, *gîte*, *gigantesque* |
| `g` | ぎ, げ | toujours le g dur de *gare* | **« gui », « gue »** : *guide*, *guette* | « gi », « ge » lus j : *girafe*, *gens* |
| `s` | さ す せ そ | toujours le s sourd de *sac* | **un s qui se dit s** : en début de mot, ou « ss », « c », « ç » | un s entre deux voyelles, lu z : *rose*, *maison* |
| `w` | わ | « oua » | **« oua »** : *ouah*, *Ouagadougou* | « va », « wa » lu va |
| `yoon` | consonne + ゃ ゅ ょ (きゃ, ひゃ, りょ…) | la consonne et le son « ya / yu / yo » d'un seul coup | **consonne + « ia », « iou », « io »** dans une syllabe : *kiosque* (kyo), *hiatus*… ; ryo = « lio », ryu = « liou » (voir `r`) | perdre la consonne : *yakuza* pour ひゃく (hyaku) |
| `n-final` | ん (n de fin de syllabe) | un vrai n, après une voyelle restée orale | **voyelle + n qui se prononce** : *manette*, *cane*, *scène*, *Seine*, *Denver*, *cône*, *banane* | la voyelle nasale française, où le n disparaît : *an*, *Nantes*, *nan*, *tente*, *bon* |
| `geminee` | っ (petit tsu : consonne double) | un temps d'arrêt avant la consonne | **une coupure entre deux mots** : *hop-pop* | le double qui ne s'entend pas : *botte*, *pomme* |

## Ce que la charte ne règle pas

- **L'accent de hauteur** du japonais (haut / bas) : le français n'en a pas, une mnémotechnique ne peut pas le porter.
- **Le u final souvent soufflé** (*desu* dit « dess ») : le rendu « ou » reste juste, on ne demande pas de le faire disparaître.
- **La lecture elle-même** (on ou kun, laquelle apprendre) : c'est le champ `lecture_enseignee`, pas la charte.
