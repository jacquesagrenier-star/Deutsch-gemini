# Les données japonaises de l'app

Le japonais a la **même structure que l'espagnol** (`espanol/datos/`) : des thèmes de
noms, des verbes, des adjectifs, des adverbes, des expressions et des mots-outils,
rangés par niveau, chacun avec sa traduction française et anglaise et une phrase
d'exemple traduite.

| Fichier | Contenu | Équivalent espagnol |
|---|---|---|
| `themes.json` | les noms, un thème par domaine et par niveau (`maison_a1`, `maison_a2`…) | `temas.json` |
| `verbes.json` | les verbes, avec toutes leurs formes (`formes.masu`, `formes.te`, `formes.nai`…) | `verbos.json` |
| `adjectifs.json` | adjectifs en い et en な (`type`), avec leurs formes | `adjetivos.json` |
| `adverbes.json` | adverbes et onomatopées (`kategorie`) | `adverbios.json` |
| `expressions.json` | expressions et interjections (`kategorie`) | `expresiones.json` |
| `fonctionnels.json` | particules, conjonctions, pronoms, démonstratifs, compteurs, préfixes, suffixes | `funcionales.json` |

**Ces fichiers sont dérivés : ne jamais les corriger à la main.** On corrige la
décision (`japonais/cartes/decisions/`), puis :

```
python japonais/cartes/outils/construire.py
python japonais/datos/construire.py
```

## Ce qui diffère de l'espagnol

- **Pas de genre ni d'article.** À la place : `lecture` (kana), `romaji` (Hepburn,
  calculé), `furigana` (la lecture de chaque kanji, pour l'afficher au-dessus),
  `kanji` (les kanji contenus).
- **Niveaux** : N5 → A1, N4 → A2, N3 → B1, N2 → B2, N1 → C1, pour que le moteur
  garde ses cinq niveaux. Le niveau JLPT d'origine est dans `jlpt`.
- **`id`** (« jmdict:1198180 », « ja:prt:wa ») : la clé de progression de l'élève,
  stable pour toujours.
- **Les formes des verbes et des adjectifs sont calculées** par
  `japonais/conjugaison/conjugaison.js` (284 593 vérifications), jamais écrites à la main.
- **`statut: "brouillon"` partout** : rien n'a été relu par un natif. Le verdict de
  la machine (`verdict_machine` : BON, A_AMELIORER, A_REMPLACER, FAUX) dit où regarder.
- **`exemple_source`** : les phrases viennent de Tatoeba, sous CC BY ; l'auteur de
  chaque phrase doit pouvoir être cité.

## Sources et licences

JMdict et KANJIDIC2 (EDRDG, CC BY-SA 4.0), listes JLPT de Jonathan Waller (CC BY),
Tatoeba (CC BY 2.0 FR). Traductions choisies ou écrites par Wortando (Claude, modèles
Opus et Fable), à relire.
