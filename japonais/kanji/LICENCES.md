# Licences — mnémotechniques kanji N5

Les fichiers de ce dossier combinent des données de trois sources. Les textes des mnémotechniques et les noms des composants sont originaux, mais ils sont publiés **dans les mêmes fichiers** que des données sous licence à partage identique : l'ensemble (`mnemoniques_n5.json`, `composants.json`, `a-relire.html`) se diffuse donc sous **CC BY-SA 4.0**, avec les attributions ci-dessous.

## 1. KANJIDIC2 — EDRDG

- **Ce qui en vient** : les sens français et anglais des kanji (`sens_fr_candidats`, `sens_en_candidats`, et les sens retenus, choisis parmi eux), les lectures on et kun, le nombre de traits.
- **Lu dans** : `japonais/kanji.json` (branche `japonais-donnees`), construit à partir de `kanjidic2.xml.gz`, version `2025-310` du 6 novembre 2025.
- **Licence** : Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0) — https://creativecommons.org/licenses/by-sa/4.0/ ; conditions de l'EDRDG : https://www.edrdg.org/edrdg/licence.html
- **Attribution** : « Cette application utilise le fichier de dictionnaire KANJIDIC. Ce fichier est la propriété de l'Electronic Dictionary Research and Development Group et est utilisé conformément à la licence du groupe (https://www.edrdg.org/edrdg/licence.html). »

## 2. KanjiVG — Ulrich Apel

- **Ce qui en vient** : la décomposition de chaque kanji en composants (groupes `kvg:element` des fichiers SVG), et donc la liste de `composants.json`.
- **Lu dans** : le dépôt https://github.com/KanjiVG/kanjivg, commit `70a0b7ae0c18ceb5cb358274b029cce0234a43bc` (30 septembre 2026). Le commit exact utilisé est noté dans `meta.sources.kanjivg` de chaque fichier généré.
- **Licence** : Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) — https://creativecommons.org/licenses/by-sa/3.0/
- **Attribution** : « Décompositions des kanji : KanjiVG, © Ulrich Apel, CC BY-SA 3.0 (https://kanjivg.tagaini.net/). »
- La CC BY-SA 3.0 permet de rediffuser une adaptation sous une version ultérieure de la même licence, d'où la CC BY-SA 4.0 de l'ensemble.

## 3. Listes JLPT — Jonathan Waller

- **Ce qui en vient** : la liste des kanji N5 et les mots N5 (écriture, lecture en kana, sens anglais) qui servent à compter les lectures et à donner les exemples.
- **Lu dans** : `japonais/mots.json` et `japonais/kanji.json`, voir `japonais/LICENCES.md` pour les copies effectivement lues.
- **Licence** : Creative Commons Attribution (CC BY) — https://creativecommons.org/licenses/by/4.0/
- **Attribution** : « Listes de vocabulaire et de kanji JLPT : Jonathan Waller, https://www.tanos.co.uk/jlpt/ (CC BY). »

## En pratique

Une application qui affiche ces mnémotechniques doit montrer les trois attributions (EDRDG, KanjiVG, Waller), par exemple dans sa carte « Crédits », et publier les fichiers de données dérivés sous CC BY-SA 4.0.
