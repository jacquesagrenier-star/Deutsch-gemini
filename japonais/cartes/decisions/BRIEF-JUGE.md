# Brief du juge (25 oct. 2026)

Tu travailles pour Wortando, une app d'apprentissage des langues pour francophones.
Jacques, le propriétaire, est francophone et ne parle pas japonais. Tout ce que tu
écris est en français. On fabrique les cartes de vocabulaire japonais, du N3 au N1,
comme on l'a déjà fait pour le N5 et le N4 (1 297 mots jugés, à prendre pour modèle :
`japonais/cartes/decisions/n5-001.json`, `n4-010.json`).

Dossier de travail : `C:/Users/jacqu/.wortando/wt-japonais` (une copie git, branche
`japonais`). **Aucune commande git.** N'écris que tes propres fichiers
`japonais/cartes/decisions/<lot>.json`.

## Ce que tu fais, pour chacun de tes lots

1. Lis d'abord **en entier** `japonais/cartes/decisions/CONSIGNE.md` (le format et
   les règles, y compris les « Ajouts du 25 octobre ») et
   `japonais/cartes/domaines.json` (les domaines permis).
2. Lis le lot `japonais/cartes/lots/<lot>.json` : 50 mots, chacun avec ses sens
   anglais JMdict (dans l'ordre, du plus courant au plus rare), la définition de
   Waller, les gloses françaises JMdict en vrac (`fr_jmdict`) et jusqu'à trois
   phrases Tatoeba candidates.
3. Écris `japonais/cartes/decisions/<lot>.json` : une liste JSON, **une décision
   par mot, dans l'ordre du lot**, au format de la consigne, avec le champ
   `domaine`. UTF-8, JSON valide. Écris le fichier d'un coup quand le lot est fini.
4. Vérifie : `PYTHONIOENCODING=utf-8 python japonais/cartes/outils/construire.py --sec`
   depuis le dossier de travail. Corrige chaque erreur qui cite **ton** fichier.
   D'autres juges écrivent en même temps : ignore les erreurs des autres fichiers.

## Les points qui comptent le plus

- **La traduction affichée est courte** (le dos d'une carte), dans le sens le plus
  courant (le sens anglais n° 1 fait foi). Gloses JMdict recopiées **à l'identique**
  si elles conviennent (`fr_src: "jmdict"`), sinon écrites (`"wortando"`).
- **La phrase doit employer le mot dans le sens affiché, et son français doit dire
  ce que dit le japonais.** Lis l'anglais pour contrôler. Une traduction libre, un
  contresens, un sujet pénible (violence, mort, sexe) : rejeter. Aucune ne va :
  `"phrases": []` et `note_phrase`. **N'écris jamais de phrase japonaise.**
- `verdict` juge ce que JMdict proposait en français, pas ton choix.
- Un homonyme (l'id JMdict n'est pas le mot que vise la liste JLPT) : `id_douteux`.
- Tout reste brouillon : n'écris jamais « validé » ni « vérifié ».

## À la fin

Réponds en cinq lignes au plus : tes lots, le nombre de mots par verdict, le nombre
de mots sans phrase, et les `id_douteux` que tu as signalés.
