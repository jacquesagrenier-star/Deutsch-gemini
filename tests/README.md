# Vérificateur

```bash
python tests/verifier.py
```

À lancer avant chaque `git push`. Aucune dépendance : ni npm, ni navigateur.
Sort en code 0 si tout va bien, 1 sinon.

## Ce qu'il vérifie

**Données** — les 5 fichiers JSON : champs obligatoires présents et non vides,
niveaux CECR valides, catégories connues, genres valides, conjugaisons au
présent complètes (6 personnes), aucun doublon de mot entre niveaux.

**Traductions** — aucune clé en double (la dernière écrase silencieusement la
première), le français et l'anglais ont exactement le même jeu de clés, et
toute clé citée dans le HTML ou via `t()` / `tf()` existe réellement.

**Interface** — chaque `onclick` vise une fonction définie, chaque
`showScreen("x")` vise une `<section id="x">` existante, chaque action de
panneau (`action:"nom"`, appelée par `window[nom]()`) correspond à une
fonction, et chaque mode de flashcard a un écran de retour explicite dans
`FLASHCARD_RETURN_SCREENS`.

**Export** — les CSV de `export/` sont-ils encore le reflet des JSON ? Un
avertissement, pas une erreur : une donnée modifiée sans export refait n'est
pas une régression, seulement un export à relancer.

# Exportateur

```bash
python tests/exporter.py            # réécrit les 11 CSV de export/
python tests/exporter.py --verifier # compare sans rien écrire
```

Les CSV sont des fichiers **dérivés** des JSON du dépôt. L'outil qui les
produisait ne vivait pas ici, et ils ont pris quatre versions de retard sans
que rien ne le signale — d'où ce script, et le contrôle ajouté au vérificateur.

Ils ne sont pas versionnés (`export/` reste hors de git) : une commande suffit
à les refaire.

Le format est reproduit à l'identique : UTF-8 avec BOM, séparateur `;`, fins de
ligne CRLF, guillemets seulement quand le contenu l'exige. La preuve tient en
une ligne : au moment où le script a été écrit, il reproduisait **à l'octet
près** les huit CSV dont les données sources n'avaient pas changé.

# Ajout d'exercices d'examen

```bash
python tests/ajouter_pruefung.py mon_lot.json
```

`pruefung.json` — les quatre épreuves de la tuile Préparation — **ne s'édite
pas à la main**. Le lot d'entrée a la même forme que le fichier cible (un objet
dont les clés sont `sprechen`, `schreiben`, `lesen`, `hoeren`) mais ne contient
que les entrées à ajouter.

Trois défauts de ce contenu-là ne se voient ni au vérificateur ni en relisant
le JSON, et se paient en jouant la série :

- **un `bon` différent de 0.** Le fichier garde la bonne réponse en première
  position et le mélange se fait à la construction de l'exercice. Une entrée
  qui dérogerait resterait juste, mais la prochaine relecture humaine lirait la
  mauvaise réponse comme la bonne.
- **des listes d'options de longueurs différentes selon la langue.** L'écran
  affiche les options de la langue d'interface et les compare au texte de la
  bonne réponse : une liste plus courte en turc fait disparaître la bonne
  réponse des boutons — l'exercice devient impossible **dans cette langue
  seulement**, donc invisible à qui teste en français.
- **un champ absent.** Le convertisseur d'`index.html` lit `o.erkl_en` sans
  filet ; un champ manquant s'affiche en « undefined ».

Il refuse aussi une reconstruction de moins de trois blocs (elle se résout au
hasard) et tout doublon. Le vérificateur du projet ne voit rien de tout cela :
`pruefung.json` n'est pas un fichier de vocabulaire, il n'a pas la même
grammaire.

**Le seul vrai contrôle reste de rejouer les séries dans le navigateur**, en
cliquant, aux trois niveaux.

## Ce qu'il ne vérifie pas

La qualité d'une traduction, la justesse d'une phrase d'exemple, une mise en
page. Il vérifie que rien n'est cassé, pas que c'est bien.

## Vérifier le filet lui-même

Un filet qui dit toujours « OK » ne sert à rien. Le vérificateur accepte un
chemin en argument, ce qui permet de lui soumettre une copie volontairement
cassée et de confirmer qu'il la refuse :

```bash
python tests/verifier.py chemin/vers/copie_cassee.html
```
