# L'espagnol, langue d'interface de l'allemand : avancement

Décision de Jacques du 15 nov. 2026 (`decisions/DECISIONS.md`) ; plan accordé par le chef
d'orchestre le même jour (`interface-es/PLAN.md`). Branche `espagnol-interface-de`.
Espagnol d'**Amérique latine neutre** (tú, usted, ustedes pour *ihr*, pas de vosotros) ; pas de
variante d'Espagne (« ¿Qué español? » reste caché pour l'allemand appris).

**En ESSAI ADMIN tant que ce n'est pas complet** : « es » n'entre dans `UI_LANGS` de l'allemand
que si l'admin l'a ouvert **sur l'appareil** (Réglages → Administration → « ESPAÑOL — ESSAI
INTERFACE », clé locale `deutschAI_essaiInterfaceEs`). Sans elle, un téléphone réglé en espagnol
s'ouvre toujours en anglais. L'ouverture à tous = retirer la garde dans `UI_LANGS` (une ligne).

## Journal

| Lot | Contenu | État |
|---|---|---|
| 0 | Câblage (`outils/cablage_es.py`), 76 clés d'interface (`outils/cles_i18n.py`), outils de `tests/` étendus, sonde (`outils/sonde_essai.py`) | publié en v1205 |
| 1 | Corpus A1-A2 : 2 133 cartes sur 2 133 (`outils/corpus_lots.py`, sources `sources/corpus-*`, lots `lots/corpus-*`), traduction, phrase et, pour les verbes, les trois temps | publié en v1205 |
| 2 | Fiches (`grammaire.json`, 237 textes, 17 comparaisons réécrites contre l'espagnol), Premiers pas (666), A1 voyage (646), conjugaison (336), étapes et « Tu sais… » (161, `etapes/traductions/es.json`), repères (57, `tests/reperes_es.json`), prononciation (25 règles réécrites sur les sons de l'espagnol, table `ES` de `tests/prononciation.py`) | publié en v1205 |
| 3 | `exercices.json` complet (2 721 exercices ; 3 594 champs allemands recopiés ; 20 lots), exercices d'articles codés en dur (219 textes, `outils/patch_articles_es.py`) | publié en v1205 |
| 4 | Corpus B1-C1 : le corpus entier est à **8 106 / 8 106** | publié en v1205 |
| 5 | Examen (`pruefung.json`, 720 textes, `LANGUES_PRUEFUNG`), pages telc (1 454 textes, `telc/langues/es.json` → `es.js`, `LANGUES_PAGES_TELC`), `dtz/commun.js`, `telc.html`, `oral.html`, `telc-pflege/telc.html` ouverts à `lang=es` (`outils/cablage_telc_es.py`) ; étoiles : déjà en espagnol | publié en v1205 |
| 6 | Scènes : 53 scènes, 3 021 textes (`visuel/prototype/traductions/<scène>.es.json`, `outils/scenes_textes.py`) et le mot de chaque zone (`construire.py`), page des scènes au repli es → en → fr ; **thèmes illustrés : en attente** de la fusion de la ligne 96 (alignement-langues), qui touche leur générateur (et `themes/tirage.js`, `themes/zoom.js`) | scènes faites, thèmes à faire |
| 7 | Pflege (`LANGUES` des outils Pflege, dossier `pflege/sources/traductions/es/`, `tests/pflege*.py`), et le lecteur des dialogues des Soins (`visuel/prototype/conversation.html?soins=1` : `LANGUES_UI` + un bloc `UI_SOINS.es`, 35 textes). En dernier : la session Pflege architecture prévient quand le contenu est figé (d13-d26, paires, cartes-phrases arrivent la semaine du 15 nov.) | à faire |
| 8 | Contrôles mécaniques (0 suspect, collisions 41 départagées / 47 acceptées), relecture croisée d'un échantillon de 467 entrées + étalonnage (`relecture/BILAN.md`) | fait ; relecture native à venir |

**Pflege, l'examen et le manuel** (15 nov., par pflege-examen, branche `claude/pflege-examen-1cc3a5`,
commit d69d3fb, pas encore sur main) : interface de telc-pflege (226 clés), examen blanc 1 (160 aides),
examen blanc 2 (déjà en 10 langues), manuel (sommaire, chapitres 0-4, 7, 8 ; 5 et 6 chez manuel-sprechen).
Termes douteux : `pflege/examen/RELIRE-LANGUES.md`. **À vérifier au navigateur** (`telc-pflege/telc.html?lang=es`)
quand les deux branches seront sur main : l'ouverture de `dtz/commun.js` à `lang=es` est ici.

## Le câblage (lot 0)

Ce que `outils/cablage_es.py` a changé dans `index.html` (il refuse de tourner deux fois) :

- `CLE_ESSAI_INTERFACE_ES`, `ESSAI_INTERFACE_ES`, et `UI_LANGS` de l'allemand `+ "es"` sous garde ;
- `REPLI_LANGUE.es` : `es → fr` pour l'anglais appris (inchangé), `es → en → fr` pour l'allemand ;
- les cinq tuples de cartes (noms, adjectifs, mots-outils, expressions, adverbes) remplissent les
  rangs es de `RANGS_CARTE` aussi pour l'allemand (rangs de « de » laissés vides) ;
- le chargeur des verbes : `traduction_es`, `exemple_es`, `perfekt_es`, `praeteritum_es`,
  `konjunktiv2_es` ; les rangs es de Premiers pas (`RANGS_PP`) ;
- la recherche, le quiz des articles, l'écoute et les phrases à construire, les copies
  `correctEs` / `optionsEs` / `explanation_es` ; les 15 libellés de catégories ; la phrase
  d'essai de la voix ;
- les boutons « Español » des deux choisisseurs, montrés pour l'allemand quand l'essai est
  ouvert ; le bouton de l'essai dans la carte Administration (`majEntreeEssaiInterfaceEs`,
  `basculerEssaiInterfaceEs`).

Restent pour leurs lots : les exercices d'articles codés en dur (lot 3, données
`ARTICLE_*`), `LANGUES_PRUEFUNG` (lot 5), `LANGUES_PAGES_TELC` (lot 5).

**Hors périmètre, signalé au chef** : les épisodes « Mark in Berlin » ont des sous-titres
**gravés** (`EPISODES_LANGUES.de`, neuf langues) ; une interface espagnole y prend l'anglais
tant que des sous-titres espagnols ne sont pas gravés (travail vidéo à part).

## Les fichiers dérivés : où vit l'espagnol

Ne jamais corriger l'espagnol dans un fichier dérivé ; le corriger dans sa source, puis reconstruire :

| Fichier | Source de l'espagnol | Reconstruire |
|---|---|---|
| `etapes.json`, `je-sais.json` | `etapes/traductions/es.json` ({français: espagnol}) | `python tests/etapes_construire.py` |
| `reperes.json` | `tests/reperes_es.json` ({français: espagnol}, appliqué par `ajouter_espagnol()` à l'allemand seulement) | voir ci-dessous |
| `prononciation.json` | table `ES` de `tests/prononciation.py` | `python tests/prononciation.py --ecrire` (dossier principal : il exige les voix d'Aurora) |
| les autres (`themes.json`, `grammaire.json`, `premiers-pas.json`…) | le fichier lui-même | — |

⚠️ **`tests/reperes_construire.py` est destructeur pour l'espagnol appris** (constaté le 15 nov., antérieur à ce chantier) : `espanol/datos/reperes.json` porte une interface allemande posée directement dans le fichier dérivé, que le constructeur ne connaît pas ; le relancer l'efface. D'où, pour ne refaire que l'allemand :
`python -c "import sys,os; sys.path.insert(0,'tests'); import reperes_construire as rc; rc.ecrire(os.path.join(rc.RACINE,'reperes.json'), rc.ajouter_espagnol(rc.construire('de')))"`.
De même, `tests/premiers_pas.py` signale 667 « langue inattendue « de » » dans `espanol/datos/premiers-pas.json` : antérieur, non touché.

## Le piège « es »

Relevé des 134 tests d'`index.html` : 109 `LANGUE_APPRISE === "es"` (l'espagnol appris, jamais
touchés) ; 4 `getUiLang() === "es"` (le « ¡ » du salut, « ¿Qué español? » dans la branche de
l'anglais, les familles anglaises, le `varianteEs` des scènes), aucun ne bascule vers l'espagnol
appris ; le reste lit la langue apprise. `UI_LANG_KEY` est préfixé par la langue apprise.
⚠️ Les outils ne cherchent jamais un champ espagnol par le seul suffixe `_es` : `verbe.json` et
`themes.json` portent 1 498 clés `praesens.er_sie_es` (le pronom allemand).

## Contrôles

- `python interface-es/outils/sonde_essai.py --port 8806` (sous le verrou des navigateurs) :
  inerte sans la clé (es-MX → anglais, aucun bouton), ouvert avec elle ; espagnol et anglais
  appris inchangés.
- `python interface-es/outils/corpus_lots.py etat | controle <lot>` ; `python tests/trous_langue.py` ;
  `python tests/relecture_langue.py --langue es --suspects | --collisions`.
- `tests/verifier.py`, `node tests/syntaxe.js` ; parcours `--app de` et `--app es-moteur` à 0 écart
  avant publication.
