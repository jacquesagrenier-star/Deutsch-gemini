# L'espagnol, 10e langue d'interface de l'allemand : le plan (étape 1)

15 nov. 2026. Session « espagnol, interface de l'allemand », branche `espagnol-interface-de`
(tirée de `main` à f0f5518). Décision de Jacques du 15 nov. (DECISIONS.md, ligne 616).
**Rien n'est codé : ce plan attend l'accord du chef.**

## 1. Ce qui existe déjà (mesuré)

| Pièce | État pour l'espagnol | Pourquoi |
|---|---|---|
| `I18N.es` (interface) | **1 831 clés**, contre 1 816 pour le russe | traduit le 2 nov. pour l'anglais appris, **depuis la base française, qui parle de l'allemand** (« alemán » 42 fois, comme « allemand » 33 fois en français) : il vaut tel quel pour l'allemand appris. Manquent 76 clés de la base (ajoutées depuis). |
| `SUFFIXE_LANGUE`, `SUFFIXE_CHAMEAU`, `DRAPEAUX_LANGUE` (🇲🇽), `LOCALES_ABO` (es-419), `LANGUE_TAG` (es-MX), `RANGS_CARTE` (rangs es après ceux de de) | **déjà posés** | même raison |
| `champEs()`, `VARIANTE_INTERFACE_ES`, `I18N_ES_ESPAGNE` (28 clés) | prêts, mais ne servent qu'à l'anglais appris | la variante d'Espagne de l'interface existe donc déjà |
| Corpus allemand (`*_es`) | **0** | aucun champ, sauf `praesens.er_sie_es` (le pronom allemand, 1 498 fois) |
| Mots espagnols des scènes | 482 dans `visuel/prototype/espanol/mots.json` | l'espagnol APPRIS (base Espagne, `variantes.json` pour l'Amérique) : source à reprendre, à vérifier contre l'Amérique latine |
| Paires espagnol → allemand | 4 068 `traduction_de` dans `espanol/datos/` | l'interface allemande de l'espagnol : sert au **contraste mécanique** (voir § 5) |

## 2. Le périmètre (étalon : le russe, compté champ par champ)

| Bloc | Textes | Caractères |
|---|---:|---:|
| Corpus : themes, verbe (4 temps), adjectif, redewendung, adverbe, funktionswort (≈ 8 100 cartes) | 20 870 | 543 000 |
| `exercices.json` | 14 070 | 604 000 |
| `pruefung.json` (examen) | 1 076 | 72 000 |
| `grammaire.json` (fiches, **à réécrire contre l'espagnol**) | 237 | 45 000 |
| Premiers pas, A1 voyage, étapes, conjugaison, repères, prononciation, je-sais, étoiles | 2 260 | 61 000 |
| Scènes (`scene-*.js`) et thèmes illustrés (`visuel/prototype/`) | 5 900 | 75 000 |
| telc / DTZ (`visuel/prototype/telc*`) | 360 | 24 000 |
| **Pflege** (`pflege/datos/`) | 3 720 | 192 000 |
| `index.html` : 76 clés + ≈ 25 textes en dur (catégories, etc.) | ≈ 100 | ≈ 3 000 |
| **Total** | **≈ 48 500** | **≈ 1,6 M** |

## 3. Le piège « es » : relevé (134 tests dans index.html)

- **109 tests `LANGUE_APPRISE === "es"`** : l'espagnol APPRIS. Aucun ne lit `getUiLang()` ; ils ne bougent pas.
- **4 tests `getUiLang() === "es"`** : le « ¡ » du salut (juste aussi pour l'allemand), « ¿Qué español? » (37310), les familles d'expressions anglaises (anglais seul, table), le `varianteEs` passé à la page des scènes. Aucun ne fait basculer vers l'espagnol appris.
- **Le reste** : variante `"es"`/`"latam"`, code d'invitation `apprendre=es`, `nombreEnMots(n, "es")` (langue de la voix), garde de `?apprendre=` en tête : tous lisent la langue APPRISE, jamais `getUiLang()`.
- `UI_LANG_KEY` est préfixé par la langue apprise (`wortando_` / `wortandoEs_`) : une interface « es » de l'allemand ne peut pas fuir vers l'app espagnole, ni l'inverse.
- Le moteur n'appelle **jamais** la langue apprise « es » en interne (contrairement à « de » : `pickVoice("de")`, `entry.de`) : vérifié pour l'anglais le 2 nov., revérifié ici (aucun `entry.es`, `ph.es`, `:lang(es)`).

**Ce qu'il faut changer, et seulement ça :**
1. `UI_LANGS` de l'allemand : `+ "es"`, **sous garde d'essai** (§ 6).
2. `REPLI_LANGUE.es` vaut `["es","fr"]` à cause de l'anglais appris (jamais par la langue apprise). Pour l'allemand : `["es","en","fr"]`, comme les 8 autres → une ternaire sur `LANGUE_APPRISE`.
3. Les cinq chargeurs de cartes ne remplissent les rangs es que `LANGUE_APPRISE === "en"` (40907, 41008, 41226, 41267, 41312) : ajouter la branche allemande (rangs de « de » laissés vides).
4. Le bouton « Español » des réglages n'est montré que pour l'anglais (37303) ; « ¿Qué español? » sera **caché pour l'allemand** (§ 7).
5. `LANGUES_PRUEFUNG`, catégories d'expressions et d'adverbes, index de recherche, `construire.py` (CHAMPS_MOT) des scènes, `prononciation.py`, `LANGUES` des outils Pflege, `langueImposee` du tableau de bord.
6. Outils : `es` dans `tests/langue.py`, `trous_langue.py`, `relecture_langue.py`, `trous_francais.py`, `francais_ailleurs.py`. ⚠️ **chaque outil doit ignorer `er_sie_es`** (sinon 1 498 « traductions » fantômes).

## 4. L'ordre des lots

| Lot | Contenu | Livre |
|---|---|---|
| 0 | Câblage inerte (§ 3), 76 clés + textes en dur, outils étendus | l'essai admin s'ouvre, l'interface est en espagnol, les cartes retombent sur l'anglais |
| 1 | Corpus A1-A2 (cartes, exemples, 4 temps des verbes) | un débutant peut travailler |
| 2 | Fiches de grammaire **réécrites contre l'espagnol**, Premiers pas, A1 voyage, étapes, repères, conjugaison, prononciation, je-sais | le parcours débutant complet |
| 3 | `exercices.json` | |
| 4 | Corpus B1-C1 | |
| 5 | Examen (`pruefung.json`), telc, DTZ, étoiles | |
| 6 | Scènes (42, via `construire.py`) et thèmes illustrés | |
| 7 | **Pflege**, en dernier : son contenu bouge encore (sessions pflege-* au travail). Clé prévue par `pflege/PLAN.md` § E : `es` dans `LANGUES` des outils, dossier `pflege/sources/traductions/es/` | |
| 8 | Relecture croisée complète, captures, mesure langue × contenu = 100 % | proposition d'ouvrir à tous |

Outillage repris tel quel : `corpus_langue.py --langue es` (pose par numéro, trois garde-fous), `poser_examen.py`, `patch_articles.py`, le gabarit `russe/outils/cablage_ru.py`, les consignes et le glossaire `anglais/es/CONSIGNES.md` (espagnol neutre).

## 5. Le contrôle

1. **Mécanique, après chaque lot** : `relecture_langue.py --langue es --suspects` et `--collisions` (jusqu'à 0, collisions acceptées écrites avec leur raison), `trous_langue.py`, `trous_francais.py`, `francais_ailleurs.py`.
2. **Contraste par nos propres paires**, à la place de DeepL (pas de clé, et 1,6 M caractères dépasseraient l'offre gratuite) : chaque carte allemande dont le mot existe dans `espanol/datos/` (4 068 paires `traduction_de`) doit recevoir une réponse espagnole compatible ; un écart est une question, pas une correction.
3. **Relecture croisée par un autre modèle**, lots de 100 cartes, vagues de 3 à 5 ; n'appliquer que les faits ; journal dans `interface-es/RELECTURE.md`. La traduction par agents Fable (consigne « Déléguer à Fable »), la relecture par un modèle d'une autre famille Claude. La limite reste : deux Claude ne sont pas deux avis indépendants ; un relecteur hispanophone (mexicain ou colombien) serait l'idéal, surtout pour la Pflege.
4. **Parcours** `--app de` et `--app es-moteur` : 0 écart à chaque lot ; `verifier.py`, `syntaxe.js` ; captures au téléphone simulé, jour et nuit, en interface espagnole.

## 6. Inerte tant que ce n'est pas complet

« es » n'entre dans `UI_LANGS` de l'allemand que si l'admin l'a ouvert sur l'appareil (bouton dans Réglages → Administration, « ESPAÑOL — ESSAI INTERFACE », drapeau local). Sinon un téléphone réglé en espagnol s'ouvrirait en espagnol dès le lot 0 (`langueDuTelephone()`). À l'ouverture finale, la garde tombe : une ligne.

## 7. Variante

**Amérique latine neutre** : tú pour du, usted pour Sie, **ustedes pour ihr ET pour Sie au pluriel**, pas de vosotros, pas de voseo. C'est le seul vrai point de grammaire contrastive neuf : les fiches et la conjugaison doivent expliquer que l'allemand distingue *ihr* et *Sie* là où l'Amérique latine dit « ustedes » (« ihr = ustedes, entre amigos »). Vocabulaire mexicain/colombien commun (celular, computadora, carro/auto, jugo).

**Pas de variante d'Espagne dans ce chantier.** « ¿Qué español? » sera caché pour l'allemand appris (sinon il afficherait 🇪🇸 et 28 clés d'Espagne sur un contenu d'Amérique). La structure (`_esp`, `champEs()`, `I18N_ES_ESPAGNE`) permet de l'ajouter plus tard sans rien refaire. Un argument pour plus tard, à soumettre à Jacques : l'Espagne a fourni des milliers d'infirmières à l'Allemagne (vague 2012-2015) ; si un contact Pflege recrute en Espagne, la variante vaut un lot de plus.

## 8. Temps et coût

- **Coût : 0 $.** Aucune voix (la langue apprise reste l'allemand ; la voix de la traduction est celle du téléphone, es-MX), aucune image, pas de DeepL. La traduction se fait par agents sur le forfait.
- **Temps** (étalon : le polonais et le russe, faits en un à deux jours chacun) : lot 0 une demi-journée ; lots 1-6 deux à trois jours ; relecture un jour ; Pflege un demi-jour une fois son contenu figé. **Environ quatre à cinq jours de session**, publiables par paliers (lot 0 + 1 + 2 = premier palier admin).
- Le diff touchera `index.html` (câblage) et beaucoup de données ; je passerai par la file de publication du chef à chaque palier, sans version sur la branche.

## 9. Questions au chef

1. Feu vert pour ce plan et cet ordre ?
2. D'accord pour l'essai admin par drapeau local (§ 6) ?
3. Variante d'Espagne : je la laisse de côté (§ 7). La proposer à Jacques maintenant ou plus tard ?
4. Pflege : je coordonne avec quelle session pflege-* pour le moment où son contenu est figé ?
