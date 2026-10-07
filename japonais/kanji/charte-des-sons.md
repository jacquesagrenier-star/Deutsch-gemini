# Charte des sons : le japonais difficile et son rendu en français

> **Le principe (Jacques, 7 oct. 2026) : un rendu français n'est refusé que s'il fait retenir un autre son japonais.**
> Une approximation qui ne peut pas tromper est acceptée : l'audio apprendra la vraie prononciation. Une approximation qui fait entendre une autre syllabe japonaise est refusée, parce que c'est elle que l'on retiendra.
> Exemples : le r français est accepté, le japonais n'ayant qu'un son entre r et l ; « chichis » est refusé, parce qu'il fait retenir しし au lieu de ちち.

**Une règle par son, fixée une fois pour toutes.** Une mnémotechnique française fait entendre la lecture japonaise par un mot ou un bout de phrase français, le morceau en **gras**. Ce tableau dit, pour chaque son japonais qu'un francophone entend mal, comment ce morceau doit l'écrire, et ce qui est refusé.

- `construire.py` lit les identifiants de la première colonne (entre accents graves). Pour chaque lecture, il repère les sons de la charte qu'elle contient. Chaque mnémotechnique doit alors donner un verdict pour chacun de ces sons, dans son champ `charte` : `"ok"`, ou `"écart : …"` avec la raison.
- Une mnémotechnique qui a un écart est **hors charte**, même si Jacques l'a validée. Elle est à réécrire.
- Restent stricts (7 oct.) : **h, chi, tsu, u, n final**. Là, l'erreur fait retenir un autre son. Les autres lignes appliquent le même principe.
- Les sons faciles (a, i, k, m, p, t…) ne sont pas dans la charte : le français les a tels quels.
- Les sons se jugent à l'oreille, pas sur l'orthographe : « dos » rend bien *do*, parce que le s ne se prononce pas.

## Voyelles

| id | Son japonais | Ce qu'il faut entendre | Rendu français retenu | Refusé |
|---|---|---|---|---|
| `u` | う et toutes les syllabes en u (ku, su, mu, yu…) | un « ou » détendu, lèvres peu arrondies | **« ou »** : *cou*, *mouche*, *sous*, *gag cou(rt)* | le u français [y] : *suis*, *tu*, *bus* |
| `voyelle-longue` | ō, ū, ā, ē, ii (おう, とお, くう, ちい…) | la même voyelle, tenue deux fois plus longtemps | **la voyelle seule** : *tôt*, *côte*, *collège*. O ouvert ou fermé, peu importe : le japonais n'a qu'un o. La longueur n'a pas d'équivalent en français : c'est le macron du romaji qui l'enseigne. | une autre voyelle (*cou* pour こう) |
| `ei` | えい (めい, せい) | presque toujours un « é » long | **« é », « è », « ai » (lu è)**, ou « é-i » : *seize*, *mai*, *Mélanie* | « a-i », qui fait retenir あい : *maïs* (ma-is) |

## Consonnes

| id | Son japonais | Ce qu'il faut entendre | Rendu français retenu | Refusé |
|---|---|---|---|---|
| `r` | ら り る れ ろ | une seule frappe de la langue derrière les dents, entre l et d | **le r français ou « l »** : *rit*, *rail*, *ma roue*, *lit*. Le japonais n'a qu'un son entre r et l : aucun des deux ne peut faire retenir une autre syllabe. (Assoupli le 7 oct.) | perdre le son : *Dario* lu « Dao » |
| `h` | は ひ へ ほ (et ひゃ…) | un souffle audible, comme dans *hop !* | **un h qui s'entend** : interjection ou rire qui se souffle (*hop !*, *ha !*, *hi hi hi*, *ho ho ho*, le *hia !* du karatéka). Attention à l'anglais *hi*, qui se dit « haï ». | un h muet ou « aspiré » du français, qui ne s'entend pas (*honneur*, *hanneton*, *haricot*) : il fait retenir おん, あん ; ou pas de h du tout (*yakuza* pour ひゃく) |
| `fu` | ふ | souffle entre les deux lèvres, entre f et h | **« fou »** : *foot*, *fourmi* | « fu » [fy], « hu » |
| `tsu` | つ | t et s collés, comme dans *tsar* | **« ts » + « ou »**, dans un mot (*tsunami*, *tsé-tsé*) ou à cheval sur deux (*guette sous*, *hits ou*) | « tu », « sou » ou « tou » seuls |
| `chi` | ち (et ちゃ, ちょ…) | « tchi » | **« tch »** : *litchi*, *tchin*, *match* | « chi » [ʃi], qui est し : *chichis*, *chiche* |
| `shi` | し (et しゃ, しょ…) | « chi » | **« ch »** : *chat*, *chaud*, *nichée* | « s » : *sirop*, *si* |
| `ji` | じ (et じゃ, じょ…) | « dji », d et j collés, souvent adouci en « ji » | **« dj » ou le j français** : *Djibouti*, *djinn*, *jaune*, *Joconde*. Le j français est une prononciation courante de じ en japonais. (Assoupli le 7 oct.) | « ch » ou « z », qui font retenir し ou ず |
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
