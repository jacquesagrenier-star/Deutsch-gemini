# Traduire les étapes et les lignes « Tu sais… »

Wortando enseigne l'allemand et l'espagnol. L'interface existe en plusieurs langues. Ces textes s'afficheront dans l'interface, **dans la langue de l'élève** (pas dans la langue apprise).

## Ce qu'il y a à traduire

`a-traduire-<langue>.json` : une liste de `{fr, contexte}`. Trois sortes de textes :

1. **Les deux amorces** du bilan : « Tu sais maintenant… » et « Cette semaine, tu as appris à… ». Une liste de lignes « Tu sais… » s'affiche juste en dessous, une ligne par puce.
2. **Les lignes « Tu sais… »** (`contexte` : « ligne « Tu sais… » ») : un groupe infinitif à la 2e personne du singulier, familière (« te présenter », « ton chemin »). Chaque ligne doit se lire naturellement **après chacune des deux amorces**. Choisis donc des amorces qui acceptent ta forme de liste : un infinitif, un nom verbal, ou ce que ta langue emploie. Garde cette même forme pour toutes les lignes. La ligne dit une situation de la vraie vie, jamais un point de grammaire. Elle est courte : environ 60 signes au plus. Pas de majuscule au début, sauf si ta langue l'exige ; pas de point final.
3. **Les noms des groupes d'étapes et les titres des étapes** : des titres courts. Les noms des groupes sont à la première personne (« Raconter ma vie », « Me faire ma place », « Réussir mon A2 »). Garde tels quels les codes de niveau (A2, B1, C1), les noms d'examens, et les termes allemands ou espagnols cités (« Konjunktiv I »). Les guillemets suivent l'usage de ta langue.

## Le registre

Suis celui que l'app emploie déjà dans ta langue. Lis son bloc dans `index.html` : cherche par exemple `av_fin_a1_texte` et `av_jalon_change` dans le bloc de ta langue. Le tutoiement, le genre et la variante doivent rester les mêmes : le portugais est celui du Brésil (« você »), l'arabe est standard, l'allemand tutoie (« du »). Quand le genre de l'élève s'entend (un passé en russe, en polonais, en ukrainien ou en arabe), préfère une tournure neutre. S'il n'y en a pas de naturelle, suis la convention que l'app emploie déjà.

## Ce que tu rends

`etapes/traductions/<langue>.json` : **un seul objet JSON**, `{"texte français exact": "traduction", …}`, avec **toutes** les entrées de `a-traduire-<langue>.json`. Chaque clé est une copie exacte du champ `fr`, apostrophes typographiques et « … » compris. Écris le fichier avec l'outil Write, jamais par un heredoc, puis vérifie qu'il s'analyse : `python -c "import json;json.load(open('etapes/traductions/<langue>.json',encoding='utf-8'))"`. Lance ensuite `python tests/etapes_construire.py` : il ne doit plus manquer aucune traduction dans ta langue.

## Interdits

- Pas de commit, pas de push.
- Ne modifie aucun autre fichier.
- Aucune API payante, et pas d'autres agents.
