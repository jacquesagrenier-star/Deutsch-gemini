# Phrases d'exemple Tatoeba pour le vocabulaire JLPT N5–N3

**Pas encore généré (4 octobre 2026).** La session automatique qui devait le produire n'a pas pu joindre les sources : la politique réseau de son environnement refuse `downloads.tatoeba.org` et `www.tanos.co.uk`. Aucun chiffre n'est donc donné ici, et aucun n'a été estimé.

Pour le produire : `python construire.py` depuis ce dossier, sur une machine qui a accès à ces deux domaines (quelques centaines de Mo de téléchargements, mis en cache dans `brut/`). Le script réécrit ce fichier avec :

- par niveau : mots avec au moins une candidate au français lié directement, mots avec un français indirect seulement (via l'anglais), mots sans aucune phrase ;
- les phrases écartées par chaque filtre ;
- vingt exemples tirés au hasard (graine fixe) pour juger le français à l'œil.

## Ce qui a été vérifié

Le script a tourné de bout en bout sur un petit jeu d'essai fabriqué à la main (hors dépôt) : lecture des pages de tanos, des lignes B de `jpn_indices` (y compris un mot en kana indexé sous sa forme kanji, `林檎(りんご){りんご}`), liens directs et indirects, étiquettes douteuses, filtre lexical, repli sur la sous-chaîne, rapport. Ce qui ne l'a **pas** été : le format exact des vraies pages de tanos et des vrais exports, à confirmer au premier lancement réel, et les 20 entrées à comparer à Tatoeba.
