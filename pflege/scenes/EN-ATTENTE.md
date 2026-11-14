# Scènes de soins en attente des soignants

14 nov. 2026. Trois scènes ont un soignant dans l'image : elles attendent la validation des
personnages par Jacques (contrat `pflege/FORMAT-DONNEES.md`, règle 8). Rien n'est payé.

| Scène | Prompt | Références prévues (dans l'ordre du prompt) |
|---|---|---|
| `soins-bad` (salle de bain, toilette) | `soins-bad.prompt.txt` (prêt) | 1. `soins-zimmer` (style, bâtiment) ; 2. `~/.wortando/pflege/personnages/frau-lehmann.png` ; 3. Elif (à créer) |
| `soins-uebergabe` (relève au lit) | à écrire | `soins-aufnahme` (même chambre), Frau Lehmann, sa fille, Elif, Jonas (au plus 4 références : regrouper Elif et Jonas sur une planche) |
| `soins-visite` (visite médicale) | à écrire | `soins-zimmer` (même chambre), `herr-brandt.png`, Dr. Sommer, Elif |

Les images de référence des patients sont découpées dans les scènes gardées (hors du dépôt) :
`~/.wortando/pflege/personnages/herr-brandt.png` (de `soins-zimmer-aufstehen`),
`frau-lehmann.png` et `frau-krueger.png` (de `soins-aufnahme`).

Avant de lancer : créer l'image maîtresse de chaque soignant (une par personnage, de face, fond
neutre), puis annoncer le lot au chef avec son coût.
