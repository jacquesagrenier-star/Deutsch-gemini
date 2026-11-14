# Scènes de soins avec soignants

14 nov. 2026. Les personnages sont validés par Jacques et les 8 portraits maîtres sont faits
(`~/.wortando/pflege/personnages/<id>.png`, planche `planche-soignants.jpg`, prompts
`portraits.py`). Les trois scènes ci-dessous attendent l'accord du chef sur leur lot.

| Scène | Prompt | Références (dans l'ordre du prompt) |
|---|---|---|
| `soins-bad` (salle de bain, toilette) — Elif aide Frau Lehmann | `soins-bad.prompt.txt` | `soins-zimmer` (style, bâtiment), `frau-lehmann.png`, `elif.png` |
| `soins-uebergabe` (relève au lit, 13 h 30) — Elif transmet à Jonas, devant Frau Lehmann et sa fille (dialogue d06) | `soins-uebergabe.prompt.txt` | `soins-aufnahme` (même chambre), `frau-lehmann.png`, `frau-krueger.png`, `duo-elif-jonas.png` |
| `soins-visite` (visite médicale) — Dr. Sommer et Elif chez Herr Brandt | `soins-visite.prompt.txt` | `soins-zimmer` (même chambre), `herr-brandt.png`, `sommer.png`, `elif.png` |

Commande (un nom seul = original d'une scène, un chemin = un fichier) :

    P=~/.wortando/pflege/personnages
    python -X utf8 pflege/outils/generer_scene.py soins-bad --ref soins-zimmer $P/frau-lehmann.png $P/elif.png --payer
    python -X utf8 pflege/outils/generer_scene.py soins-uebergabe --ref soins-aufnahme $P/frau-lehmann.png $P/frau-krueger.png $P/duo-elif-jonas.png --payer
    python -X utf8 pflege/outils/generer_scene.py soins-visite --ref soins-zimmer $P/herr-brandt.png $P/sommer.png $P/elif.png --payer

Les objets suivent l'annexe B des scènes (« Maricel » et « Dr. Aydın » y sont devenus Elif et
Dr. Sommer). Ni horloge ni calendrier : l'heure et les dates feraient des chiffres.
