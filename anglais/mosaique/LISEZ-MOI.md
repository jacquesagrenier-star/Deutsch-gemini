# La mosaïque anglaise : les candidats

Décidé par Jacques le 27 oct. 2026 (« Peintres américains ») : des peintres américains
liés à Boston et à la Nouvelle-Angleterre. **Rien n'est branché dans l'app** : Jacques
choisit et ordonne sur les planches, comme pour l'espagnol (`espanol/mosaique/`).

## Les planches

`planche-1.jpg` à `planche-4.jpg` (non versionnées : `python anglais/mosaique/recolter.py`
les refait). 123 tableaux, numérotés, triés avec **Boston et la Nouvelle-Angleterre en
tête** (titre en bleu), puis les plus lumineux.

- **Planches 1 et 2 (n° 1-72) : la proposition.** 53 tableaux de Nouvelle-Angleterre
  (Appledore et les Isles of Shoals, Gloucester, Boston Harbor, Charles River, Maine…).
  Hassam 22, Lane 14, Prendergast 12, Homer 11, Sargent 5, Eakins 4, Benson 2, Cassatt 2.
- **Planches 3 et 4 (n° 73-123) : la réserve**, surtout Sargent, Cassatt, Benson, Tarbell.

## Les règles

- Peintre mort **avant 1956**, œuvre **d'avant 1931** ; une œuvre sans date n'est gardée
  que si le peintre est mort avant 1931.
- **Licence lue fichier par fichier sur Wikimedia Commons** : domaine public (113) ou CC0 (10),
  rien d'autre. Le musée vient de Wikidata (champ `collection` de `candidats.json`) :
  Metropolitan Museum of Art 15, Museum of Fine Arts Boston 11, Smithsonian 10,
  Philadelphia 4, Art Institute of Chicago 3, Yale 2… (28 sans musée indiqué).
- À l'horizontale ; ni nu, ni guerre, ni sujet religieux (filtre des titres, puis 12 toiles
  écartées à l'œil, la liste est dans `recolter.py`).
- Les vignettes restent hors de OneDrive : `C:/Users/jacqu/.wortando/anglais-mosaique-brut`.

## Ensuite (après le choix de Jacques)

Comme l'espagnol : `selection.json`, les originaux en haute définition (hors OneDrive),
`construire.py` → `mosaiques.json` et `peintres.json` (notices en français), puis le
branchement dans l'app (`MOSAIQUE_BASE` pour `LANGUE_APPRISE === "en"`).
