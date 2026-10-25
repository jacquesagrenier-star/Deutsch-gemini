# Consigne de jugement (fichiers `decisions/<niveau>-<nnn>.json`)

Ces fichiers sont **les seuls écrits à la main** (par la machine qui juge, puis corrigés par Jacques). Tout le reste est refait par `outils/construire.py`. Un lot à juger, `lots/<niveau>-<nnn>.json`, se refait avec `python japonais/cartes/outils/construire.py --lots` (le dossier `lots/` n'est pas versionné).

## Format

Un fichier = une liste JSON, une décision par mot du lot, dans l'ordre du lot :

```json
{
  "id": "jmdict:1198180",
  "fr": "rencontrer ; voir",
  "fr_src": "jmdict",
  "fr_autres": ["se rencontrer", "retrouver"],
  "en": "to meet",
  "en_autres": ["to see", "to encounter"],
  "phrases": [161638],
  "verdict": "BON",
  "raison": "« rencontrer » est juste et courant.",
  "note": "facultatif : pourquoi ce choix n'est pas évident",
  "note_phrase": "obligatoire si phrases est vide : pourquoi aucune candidate ne va"
}
```

## Règles

**`fr`, la traduction affichée au dos de la carte.** Courte. Le sens le plus courant du mot (le sens anglais n° 1 de JMdict fait foi, Waller aide), deux sens au plus séparés par ` ; ` (espace, point-virgule, espace).
- Si une ou deux gloses de `fr_jmdict` conviennent, les recopier **à l'identique** (caractère pour caractère, parenthèses comprises) et mettre `"fr_src": "jmdict"`. Le script refuse une glose « jmdict » qui n'est pas mot pour mot dans la liste.
- Sinon (glose absente, fausse, trop rare, trop longue, ou retouchée même d'un mot), écrire la traduction et mettre `"fr_src": "wortando"`.
- Verbe : à l'infinitif (« manger »). Adjectif en -i : forme masculine (« bleu »). Nom : sans article, sauf si l'article lève une ambiguïté. Quand le genre ou la forme pronominale importe, l'écrire (« se lever »).
- Mots de politesse, particules, interjections, compteurs : une traduction qui dit l'usage (« merci », « (marque du complément d'objet) ») ; ajouter `note` pour expliquer.
- Français standard compris partout (France, Québec, Belgique, Suisse), pas d'argot régional.

**`fr_autres`** : d'autres traductions **justes** du même mot, qu'un quiz comptera bonnes (0 à 5). Peuvent venir de JMdict ou être écrites. Jamais une glose fausse.

**`en` / `en_autres`** : même règle en anglais, à partir des sens anglais JMdict ou de Waller. Court (« to meet », « blue »).

**`phrases`** : l'id `jpn` d'**une** phrase (deux au plus), prise **uniquement** parmi les `phrases` du lot (les candidates « sous-chaîne » sont déjà retirées). Ordre de préférence : `niveau ok`, puis `longueur ok`, puis `fr direct`. Mais d'abord : **le français doit dire ce que dit le japonais**, et la phrase doit employer le mot **dans le sens affiché**. Lire l'anglais pour contrôler. Un contresens, une traduction très libre, un registre vulgaire ou un sujet pénible (violence, mort) : rejeter. Si aucune ne va : `"phrases": []` et `note_phrase`. Ne jamais écrire de phrase japonaise.

**`verdict`** juge **ce que JMdict proposait en français** (`fr_jmdict`), pas ta propre traduction :
- `BON` : une glose JMdict, prise telle quelle, est une bonne traduction de carte (il suffisait de la choisir).
- `A_AMELIORER` : la bonne glose est là mais imparfaite (trop longue, maladroite, un sens secondaire en tête, il manque une précision) ; tu l'as retouchée ou tu l'as gardée avec une réserve dans `note`.
- `A_REMPLACER` : rien d'utilisable pour une carte (liste vide, gloses d'un autre sens, trop rares, trop vagues) ; tu as écrit la traduction.
- `FAUX` : JMdict donne une glose fausse pour le sens courant (左 « droite »), ou une glose fausse risque d'être prise pour la bonne.

**`id_douteux`** (facultatif, texte) : quand l'entrée JMdict du lot n'est **pas le mot que vise la liste JLPT** (un homonyme : ボタン apparié à 牡丹 « pivoine » au lieu de « bouton », コップ à « cop », これ à l'interjection « hé ! »). Les sens anglais n'ont alors rien à voir avec `waller`. Écrire la traduction du vrai mot (`fr_src: "wortando"`, verdict `A_REMPLACER`), et dans `id_douteux` dire en une phrase quel mot l'id désigne. L'id est la clé de progression : c'est à corriger dans la source avant toute mise en service. Attention : Waller se trompe aussi parfois (N3 surtout : 人気 « sign of life ») ; si c'est Waller qui se trompe et que JMdict a le bon mot, pas d'`id_douteux`.

**`raison`** : une phrase courte, en français, que Jacques lit pour savoir où regarder. **`note`** (facultative) dès que le choix n'est pas évident.

Tout reste `brouillon` : ne jamais écrire « validé » ni « vérifié ».

Pour contrôler un lot : `python japonais/cartes/outils/construire.py --sec` (vérifie sans rien écrire).
