# La mosaïque portugaise : les candidats

Demandé par Jacques le 29 oct. 2026 : une version de Wortando pour apprendre le portugais
du Portugal. Chaque langue a sa collection de tableaux. Pour le portugais, ce sont des
peintres **portugais**. **Rien n'est branché dans l'app** : Jacques choisit et ordonne sur
la page de choix, comme pour l'anglais (`anglais/mosaique/`) et l'espagnol (`espanol/mosaique/`).

## La page de choix

**https://claude.ai/artifact/2WobnZrCYSuz5TpGavMwR3** (« Tableaux portugais »), construite par
`python portugais/mosaique/construire_choix.py <dossier>` à partir de `choix-modele.html`
et de `candidats.json`. Elle n'est pas versionnée (les vignettes pèsent 4,7 Mo).
Même page que celle des tableaux américains : on touche les toiles dans l'ordre voulu,
chacune prend son rang, et « Copier mon choix » donne une ligne du genre
« Mosaïque portugaise, dans cet ordre : n° 3, 12, E4… » à coller dans la conversation.

159 tableaux, en deux groupes, chacun du plus coloré au moins coloré :

- **N° 1 à 74 : libres partout.** Peintres morts **avant 1926**, la règle de l'espagnol
  (le Mexique protège 100 ans après la mort ; l'app se diffuse partout).
  Souza-Cardoso 20, Silva Porto 13, Keil 7, Tomasini 6, Cristino da Silva 6,
  Tomás da Anunciação 4, Carlos Ier 3, et 15 toiles de neuf autres peintres.
- **N° E1 à E85 : à décider, libres en Europe.** Peintres morts **entre 1926 et 1955**,
  œuvres d'avant 1931 (le domaine public américain). Libres au Portugal, en Europe et aux
  États-Unis, pas encore au Mexique. Malhoa 25, Veloso Salgado 11, Columbano 11, João Vaz 10,
  Marques de Oliveira 8, Condeixa 7, Carneiro 4, Souza Pinto 3, Sousa Lopes 2, Loureiro 2,
  Carlos Reis 2. C'est à Jacques de dire s'il les prend.

Éclat brut médian (saturation × luminosité sur l'image telle quelle) : 17,4 et 17,7,
entre la première récolte anglaise (15,5) et sa récolte « couleur » (19,5). Le tri est
déjà fait sur cette mesure : pas de deuxième récolte « plus colorée » pour l'instant.

## Les règles

- Licence **lue fichier par fichier** sur Wikimedia Commons : domaine public ou CC0, rien
  d'autre. Environ la moitié des fichiers portugais de Commons sont des photos prises au
  musée sous CC BY-SA (souvent avec le cadre) : elles sont écartées.
- À l'horizontale (1,1 à 2,1) ; au moins 600 px de large. Sous 900 px (la largeur des
  images de l'app), la page affiche « petite ».
- Ni nu, ni guerre, ni violence, ni sujet religieux : filtre des titres (portugais, français,
  anglais) et des genres Wikidata, puis **48 toiles écartées à l'œil** (`EXCLUS_ID`, avec la
  raison de chacune : cadres, dos de toile, doublons, nus, Agnus Dei, meurtre d'Inès de Castro…).
  « São », « Santa », « Saint » ne sont pas filtrés : ce sont d'abord des noms de lieux.
- Domingos Sequeira et Josefa de Óbidos plafonnés à 2 : presque tout le reste est religieux.
- Sources : les œuvres de Wikidata, plus les catégories « Paintings by … » de Commons
  (Malhoa : 102 fiches Wikidata, 173 fichiers dans sa catégorie). Une clé « c… » est un
  fichier de Commons sans fiche Wikidata ; son titre vient de la fiche du fichier
  (`titre_propre()` retire la signature et l'année).
- Les vignettes restent hors de OneDrive : `C:/Users/jacqu/.wortando/portugais-mosaique-brut`.

Relancer `recolter.py` **change la numérotation** : ne pas le relancer avant le choix de Jacques.

## Le Brésil (30 oct. 2026)

Jacques, le 30 oct. : « J'aimerais qu'on entre aussi l'aspect portugais-Brésil. En apprentissage. »
Le brésilien devient une variante, comme le britannique pour l'anglais, et la mosaïque suit
l'espagnol (Espagne + Amérique latine) : des peintres **brésiliens** sur la même page, après
ceux du Portugal. `python portugais/mosaique/recolter_bresil.py` → `candidats-bresil.json` et
`recolte-bresil.txt`, numérotés **B1…** (libres partout) et **BE1…** (à décider), pour que les
numéros du Portugal ne bougent pas. Il reprend les fonctions de `recolter.py` avec ses peintres,
son filtre (il ajoute exécution, fusillade, naufrage, suicide, châtiment) et ses écarts à l'œil.

- **Droit brésilien** : 70 ans après la mort, comptés du 1er janvier suivant (loi 9.610/98,
  art. 41). Un peintre mort en 1955 ou avant est libre au Brésil en 2026, comme en Europe.
  D'où les mêmes deux groupes : morts avant 1926 (libres partout, la règle du Mexique) et
  morts entre 1926 et 1955, œuvres d'avant 1931 (à décider).
- Peintres nés ailleurs qui ont fait leur œuvre au Brésil (Castagneto, Facchinetti, Taunay,
  Andersen, Brocos) : gardés. Voyageurs de passage (Debret, Rugendas, Ender) : non.
- Oscar Pereira da Silva, Henrique Bernardelli, Bertha Worms, Décio Villares, Georg Grimm :
  aucune toile ne passe (verticales, trop petites ou après 1931).

## Après le choix de Jacques

1. Recopier son choix dans `decisions/DECISIONS.md`, puis dans `CHOIX` de
   `selection_depuis_choix.py` ; `python portugais/mosaique/selection_depuis_choix.py`
   → `selection.json` (rang = ordre d'apparition).
2. `python portugais/mosaique/construire.py` → `app/img/p01.jpg`, `p02.jpg`…,
   `app/img/info.jpg` (copie du dernier, pour l'écran « Comment ça marche ») et
   `app/mosaiques.json`. Même traitement « vif » que l'espagnol et l'anglais ; 900 px de
   large ; recadrage au centre au-delà de 1,6. Les images de 1800 px de Commons restent
   hors de OneDrive (`portugais-mosaique-brut/hd`). Les titres à corriger vont dans `TITRES`.
3. `python portugais/mosaique/sources_peintres.py` → `sources_peintres.json` (résumés
   Wikipédia fr, pt, en), puis `app/peintres.json` écrit à la main d'après ces résumés,
   une notice par peintre, en français (comme l'anglais).
4. Le branchement dans `index.html` revient à la session du socle portugais : `MOSAIQUE_BASE`
   vaut `portugais/mosaique/app/` pour le portugais, comme l'anglais.
