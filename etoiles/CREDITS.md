# Les étoiles : sources et licences

`etoiles/ciel.json` (les constellations de « Ton ciel ») est un fichier **dérivé** : `python etoiles/outils/construire.py`. Il ne contient aucune mesure inventée ; la source de chaque étoile (désignation SIMBAD, parallaxe, erreur, référence, catalogue) est dans `etoiles/sources-etoiles.json`, dérivé lui aussi, que seuls les outils lisent.

| Ce qu'on prend | D'où | Licence, conditions |
|---|---|---|
| Positions (ICRS, J2000), magnitudes B et V, parallaxes, numéros HIP et HR | **SIMBAD**, CDS, Strasbourg (miroir de Harvard), relevés du 7 nov. 2026 (`sources/simbad_positions.txt`, `simbad_parallaxes.txt`) et du 11 nov. 2026 (`sources/simbad_voyage.txt`, `simbad_voyage_parallaxes.tsv`) | Données factuelles d'accès libre. Le CDS demande, en cas d'usage, la mention : « This research has made use of the SIMBAD database, operated at CDS, Strasbourg, France » (Wenger et al. 2000, A&AS 143, 9). |
| Parallaxes Hipparcos | **Hipparcos, nouvelle réduction** (van Leeuwen 2007, A&A 474, 653) ; Hipparcos (ESA 1997, Perryman et al., A&A 323, L49), via SIMBAD | Catalogues publics de l'ESA. |
| Parallaxes Gaia | **Gaia EDR3** (Gaia Collaboration 2021, A&A 649, A1) et **Gaia DR2** (2018, A&A 616, A1), via SIMBAD | ESA/Gaia/DPAC, **CC BY-SA 3.0 IGO** : attribution demandée (« ESA/Gaia/DPAC »). Nous n'en reprenons que des valeurs isolées (une parallaxe par étoile), pas une base de données. |
| Magnitude V de 9 étoiles que SIMBAD ne donne pas | **Yale Bright Star Catalogue**, 5e éd. révisée (Hoffleit et Warren 1991), version du Telescope Data Center de Harvard (`sources/bsc5_extrait.txt`) | Domaine public (NASA ADC). |
| Noms propres des étoiles | **UAI, IAU Catalog of Star Names** (Working Group on Star Names), version du 4 avril 2022 (`sources/IAU-CSN.txt`) | Produits de l'UAI sous **CC BY** : citer la source (https://www.iau.org/public/themes/naming_stars/). |
| Contrôle des noms des constellations | Titres des articles de Wikipedia, via **Wikidata** (`sources/wikipedia_noms.json`) | Wikidata : **CC0**. Ne sert qu'à vérifier ; aucun texte de Wikipedia n'est repris. |
| Tracés des figures | Dessinés pour Wortando (`outils/figures.py`, `outils/voyage.py`) à partir des positions réelles, en suivant le dessin usuel de chaque constellation | Les nôtres. Aucun tracé copié d'une carte publiée. |
| Noms des constellations dans les 12 langues | Usage de chaque langue, écrits pour Wortando et comparés aux titres de Wikipedia (`outils/controle.py`) | Les nôtres (des noms usuels, non protégeables). |

## Ce que l'app devrait afficher

Rien n'oblige à une mention pour SIMBAD, Hipparcos, le BSC ou les noms usuels. Deux sources demandent une **attribution** :

- **les noms de l'UAI** (CC BY) ;
- **Gaia** (CC BY-SA 3.0 IGO, « ESA/Gaia/DPAC »).

Elles sont dans la carte « Crédits » des réglages (groupe « Compte et aide »), à côté de WikDict et de Leipzig, clé `credits_ciel` dans les 11 langues d'interface, cachée en japonais et en anglais, qui n'ont pas de ciel (décision de Jacques du 11 nov. 2026) :

> Étoiles : noms de l'Union astronomique internationale (CC BY 4.0) ; positions et distances de SIMBAD (CDS, Strasbourg) et des missions Hipparcos et Gaia de l'ESA (Gaia : ESA/Gaia/DPAC, CC BY-SA 3.0 IGO).

## Refaire les relevés

- `python etoiles/outils/releve_voyage.py` : refait les relevés des 42 figures du voyage (réseau requis ; seulement si l'on change les étoiles d'une figure).
- `python etoiles/outils/construire.py` : refait `ciel.json` à partir des relevés, sans réseau.
- `python etoiles/outils/controle.py` : contrôle chaque figure, chaque étoile, chaque nom.
- `python etoiles/outils/planche.py [sortie.png] [--toutes]` : la planche des figures, pour les montrer.
