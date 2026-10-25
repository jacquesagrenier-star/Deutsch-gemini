# Licences — mnémotechniques kanji N5

Les fichiers de ce dossier combinent des données de trois sources. Les textes des mnémotechniques sont originaux (voir la section 4, « Mnémoniques ») ; les noms des composants sont originaux ou repris des sens de KANJIDIC2, chacun avec son origine. Les uns et les autres sont publiés **dans les mêmes fichiers** que des données sous licence à partage identique : l'ensemble (`mnemoniques_n5.json`, `composants.json`, `a-relire.html`) se diffuse donc sous **CC BY-SA 4.0**, avec les attributions ci-dessous.

## 1. KANJIDIC2 — EDRDG

- **Ce qui en vient** : les sens français et anglais des kanji (`sens_fr_candidats`, `sens_en_candidats`, et les sens retenus, choisis parmi eux), les lectures on et kun, le nombre de traits, et 29 des 80 noms de composants (ceux dont `origine` vaut « KANJIDIC … » dans `textes/noms_composants.json` : le nom est un sens KANJIDIC2 du composant, comme « bouche » pour 口).
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

## 4. Mnémoniques

- **Écrites pour Wortando**, sans source extérieure : les mnémotechniques françaises et anglaises (`mnemo_fr`, `mnemo_en`, `propositions_fr`, `autres_lectures`), les notes et leurs raisons, et `charte-des-sons.md`. Les seules données reprises sont celles des sections 1 à 3 (sens, lectures, composants, mots).
- **Règle de droit d'auteur** (Jacques, 7 octobre 2026), pour tout le chantier kanji :
  - Ne **jamais consulter** WaniKani, Heisig (*Remembering the Kanji*, *Les kanji dans la tête*), KanjiDamage ni les histoires de Kanji Koohii, et **n'en reproduire rien, même traduit** : ni histoire, ni nom de composant (« radical »), ni ordre d'apprentissage.
  - Si une mnémotechnique qui vient à l'esprit ressemble à une histoire connue de ces méthodes, **en écrire une autre**.
  - Les noms de composants (`textes/noms_composants.json`) sont des sens KANJIDIC2 du composant ou des noms écrits pour Wortando ; chacun porte son `origine`, que `construire.py` vérifie. Aucun ne doit venir d'une de ces méthodes.
- **Les images qui viennent du dessin lui-même** (le soleil derrière l'arbre pour 東, l'homme adossé à l'arbre pour 休) suivent l'explication traditionnelle du caractère, qui n'appartient à aucune méthode ; leur rédaction est la nôtre.
- **Origine des noms, vérifiée le 7 octobre 2026** contre KANJIDIC2 (version du 6 novembre 2025) : 29 noms sont un sens KANJIDIC2 du composant, 51 ont été inventés pour Wortando par la session pilote du 4 octobre, sans source notée. La comparaison avec WaniKani est impossible sans consulter WaniKani, ce que la règle interdit : voir le compte rendu du 7 octobre pour les noms à surveiller.

## En pratique

Une application qui affiche ces mnémotechniques doit montrer les trois attributions (EDRDG, KanjiVG, Waller), par exemple dans sa carte « Crédits », et publier les fichiers de données dérivés sous CC BY-SA 4.0.
