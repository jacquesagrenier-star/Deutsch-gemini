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
