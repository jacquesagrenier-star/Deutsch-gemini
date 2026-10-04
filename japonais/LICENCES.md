# Licences des données japonaises

Toutes les sources ci-dessous permettent un usage commercial, à condition de respecter l'attribution, et pour l'EDRDG le partage à l'identique.

## 1. Listes JLPT de Jonathan Waller (« Tanos »)

- **Source** : Jonathan Waller, *JLPT Resources* — https://www.tanos.co.uk/jlpt/
- **Licence** : Creative Commons Attribution (CC BY) — https://creativecommons.org/licenses/by/4.0/
- **Attribution exigée** : citer Jonathan Waller et le lien vers son site, par exemple :
  « Listes de vocabulaire et de kanji JLPT : Jonathan Waller, https://www.tanos.co.uk/jlpt/ (CC BY). »
- **Copies effectivement lues** (le site d'origine était injoignable lors de la construction) :
  - vocabulaire : https://github.com/stephenmk/yomitan-jlpt-vocab (dossier `original_data/`). Ce dépôt est publié sous **CC BY-SA 4.0** et ajoute aux listes de Waller une colonne d'identifiants JMdict : reprendre ses fichiers impose donc aussi d'attribuer stephenmk et de rester en CC BY-SA 4.0 (ce que JMdict impose de toute façon) ;
  - niveaux des kanji : https://github.com/davidluzgouveia/kanji-data (champ `jlpt_new`, relevé sur le site Tanos ; dépôt sous licence MIT).
- Les listes JLPT ne sont pas officielles : la Japan Foundation ne publie plus de liste depuis 2010. Celles de Waller sont une estimation.

## 2. JMdict

- **Source** : Electronic Dictionary Research and Development Group (EDRDG), projet JMdict/EDICT — https://www.edrdg.org/jmdict/j_jmdict.html
- **Fichiers** : http://ftp.edrdg.org/pub/Nihongo/JMdict.gz , ou sa conversion JSON https://github.com/scriptin/jmdict-simplified (même licence).
- **Licence** : Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0) — https://creativecommons.org/licenses/by-sa/4.0/ ; conditions de l'EDRDG : https://www.edrdg.org/edrdg/licence.html
- **Attribution exigée** : mentionner que l'application utilise le fichier JMdict, propriété de l'EDRDG, utilisé conformément à sa licence, avec un lien vers https://www.edrdg.org/ et vers la page de licence. Exemple :
  « Cette application utilise les fichiers de dictionnaire JMdict et KANJIDIC. Ces fichiers sont la propriété de l'Electronic Dictionary Research and Development Group et sont utilisés conformément à la licence du groupe (https://www.edrdg.org/edrdg/licence.html). »
- Les gloses françaises de JMdict ont leurs propres contributeurs, crédités dans la documentation de JMdict ; ils sont couverts par la même attribution à l'EDRDG.
- **État** : JMdict n'a pas pu être téléchargé lors de la construction (voir RAPPORT.md). Il n'est donc pas encore dans `mots.json`.

## 3. KANJIDIC2

- **Source** : EDRDG, projet KANJIDIC — https://www.edrdg.org/wiki/index.php/KANJIDIC_Project
- **Fichier** : https://www.edrdg.org/kanjidic/kanjidic2.xml.gz
- **Copie effectivement lue** : le même fichier, non modifié, dans le paquet source Ubuntu `kanjidic` 2025.11.06 (http://archive.ubuntu.com/ubuntu/pool/universe/k/kanjidic/), version `2025-310` du 6 novembre 2025.
- **Licence et attribution** : identiques à JMdict (CC BY-SA 4.0, attribution à l'EDRDG, phrase ci-dessus).
- KANJIDIC2 réunit des contributions de plusieurs personnes (sens français, espagnols, portugais, codes de recherche…). La page du projet les énumère ; l'attribution à l'EDRDG les couvre.

## Ce que cela implique pour une application publiée

1. **Partage à l'identique.** `mots.json` et `kanji.json` sont des œuvres dérivées de JMdict et KANJIDIC2 : ils restent sous **CC BY-SA 4.0**, comme toute donnée qu'on en tirera (traductions françaises ajoutées dans ces fichiers comprises). Le code de l'application n'est pas concerné ; les données, si.
2. **Mise à jour régulière.** La licence de l'EDRDG demande qu'une application ou un site qui publie ces données les **mette à jour régulièrement**, pour ne pas diffuser de versions périmées. Une app publiée devra donc prévoir de relancer `construire.py` et de republier les données. La page de licence étant injoignable lors de la rédaction, la fréquence exacte exigée n'est pas citée ici : la lire sur https://www.edrdg.org/edrdg/licence.html avant publication.
3. **Attribution visible** dans l'application, à la manière de la carte « Crédits » de Wortando : Waller (CC BY) et EDRDG (CC BY-SA 4.0), avec les liens ci-dessus.
