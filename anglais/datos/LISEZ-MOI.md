# Les données anglaises de l'app

Même structure que l'espagnol (`espanol/datos/`). Deux jeux complets, mêmes mots dans
le même ordre (la progression d'un élève suit quand il change de variante) :

- `anglais/datos/` : **anglais américain**, la base (décidé par Jacques le 27 oct. 2026) ;
- `anglais/datos-gb/` : **anglais britannique**, calculé (vocabulaire : *flat*, *lift*,
  *biscuit*… ; orthographe : *colour*, *centre*… ; formes : *learnt*, *got*).

| Fichier | Contenu | Équivalent espagnol |
|---|---|---|
| `themes.json` | les noms, en 19 thèmes A1 (`family_a1`, `home_a1`…) | `temas.json` |
| `verbes.json` | les verbes, avec `formes` (3ᵉ personne, prétérit, participe, -ing) et `irregulier` | `verbos.json` |
| `adjectifs.json` | les adjectifs, avec `formes` (comparatif, superlatif) | `adjetivos.json` |
| `adverbes.json` | les adverbes (`kategorie` affichée telle quelle) | `adverbios.json` |
| `expressions.json` | saluer, se présenter, politesse, en classe… | `expresiones.json` |
| `fonctionnels.json` | articles, quantité, démonstratifs, pronoms, possessifs, mots interrogatifs, prépositions, conjonctions | `funcionales.json` |

**Ces fichiers sont dérivés : ne jamais les corriger à la main.** On corrige les
listes de `anglais/outils/` (`noms_a1.py`, `mots_a1.py`, `phrases_a1.py`,
`exemples_imposes.py`, `variante.py`), puis :

```
python anglais/outils/construire.py
```

`anglais/outils/rapport.txt` dit d'où vient chaque phrase d'exemple.

## D'où viennent les mots et les phrases

- Les **listes de mots** ont été choisies le 27 oct. 2026 à partir de l'union des A1
  allemand et espagnol (683 têtes anglaises), plus les mots-outils propres à l'anglais.
- Les **phrases d'exemple** viennent de nos propres corpus : chaque mot allemand et
  espagnol porte une phrase traduite en anglais **et** en français (≈ 10 500 paires
  alignées). Les phrases trop européennes ou britanniques sont écartées du cours
  américain ; 70 phrases sont écrites à la main (`exemples_imposes.py`).
- **`statut : brouillon`** : rien n'a encore été relu par un anglophone.

Aucune source extérieure n'est reprise : pas de licence à citer pour l'instant.
