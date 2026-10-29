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

## La deuxième récolte, plus colorée (29 oct. 2026)

Jacques, devant les planches : « tu n'as rien trouvé de plus coloré ? ». La première
tenait en 9 peintres, avec beaucoup de marines tonalistes et sombres.
`python anglais/mosaique/recolter.py --couleur` → `candidats-couleur.json`,
`recolte-couleur.txt`, `planche-couleur-1.jpg` à `-4.jpg`.

- **120 tableaux nouveaux** (aucun n'est déjà dans `candidats.json`), de 19 peintres :
  Prendergast 16, Glackens 12, Chase 12, Hassam 12, Lawson 10, Metcalf 10, Bellows 10,
  Cooper 9, Twachtman 5, Henri 5, Potthast 4, DeCamp 3, Frieseke 3, Vonnoh 2,
  Wendel 2, Rose 2, Benson 1, Miller 1, Robinson 1.
- **Triés par éclat mesuré sur l'image brute** (`eclat_brut`, saturation × luminosité,
  avant le rehaussement des planches) plus un quart de la luminosité (`luminosite`) ;
  la Nouvelle-Angleterre n'est plus qu'un bonus de 4 points (10 tableaux). Éclat brut
  médian : 15,5 pour la première récolte, 19,5 pour celle-ci.
- Mêmes règles de droit et de sujet ; licence lue fichier par fichier : 113 domaine
  public, 7 CC0. Écartés à l'œil (`EXCLUS_ID_COULEUR`) : quatre photos avec le cadre,
  un nu, deux doublons, le Carpathia après le Titanic.
- Peu de Frieseke, de Guy Rose et de Lilla Cabot Perry : Wikidata en recense peu, et
  la plupart sont en hauteur ou sans licence lisible.

## Le choix de Jacques et le branchement (29 oct. 2026, v1013)

67 tableaux, dans l'ordre de son choix (page à cocher du chef d'orchestre, recopiée dans
`decisions/DECISIONS.md`) : 36 de la récolte « couleur » (C…), 31 de la première.

1. `python anglais/mosaique/selection_depuis_choix.py` → `selection.json` (rang = ordre
   d'apparition).
2. `python anglais/mosaique/construire.py` → `app/img/a01.jpg` … `a67.jpg`, `app/img/info.jpg`
   (copie du dernier, pour l'écran « Comment ça marche ») et `app/mosaiques.json`. Les images
   de 1800 px de Commons restent hors de OneDrive (`anglais-mosaique-brut/hd`). Même
   traitement « vif » que l'espagnol ; recadrage au centre au-delà de 1,6 (7 tableaux).
   `FICHIER_HD` prend un fichier Commons plus grand du même tableau (Shinnecock, de Chase).
3. `app/peintres.json` : une notice par peintre (19), en français seulement — l'interface
   de l'anglais n'a que le français. Écrites d'après `sources_peintres.json`
   (`python anglais/mosaique/sources_peintres.py`, résumés Wikipedia anglais et français).
4. Dans `index.html` : `MOSAIQUE_BASE` vaut `anglais/mosaique/app/` pour l'anglais ;
   `#carteMosaique` et `#tuileTableau` ne sont plus dans la liste blanche ; les textes
   « un peintre américain » (`mosaique_reste`, `mosaique_intro_texte`, `ip_tableau_1`)
   sont dans `I18N_ANGLAIS`.

À savoir :
- **Images petites** : *Iris and Lilies* de Benson (n° 47) n'existe sur Commons qu'en
  282 × 200 px ; *Bowlers, La Ciotat* (n° 1, 608 px) et *The Garden Parasol* (n° 9, 640 px)
  sont modestes. L'espagnol avait remplacé ses images de moins de 450 px, avec l'accord
  de Jacques.
- *The Sunken Road, Ransart* (n° 35, Sargent, 1918, Imperial War Museum) est une scène de
  tranchée de 1914-1918 que le titre ne disait pas ; Jacques l'a choisie.
- Le tableau de la démonstration (visite « Découvrir ») n'a pas d'équivalent anglais :
  `DEMO_TABLEAU` ne trouve pas son peintre et l'étape montre le vrai tableau.
