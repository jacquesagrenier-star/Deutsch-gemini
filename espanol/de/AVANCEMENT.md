# L'espagnol en allemand : avancement

**1er nov. 2026 : chantier « interface allemande »** (branche `claude/interface-allemande-2fd6e4`).
Décision de Jacques du 1er nov. : ouvrir l'espagnol aux germanophones (« Anglais,
portugais du Brésil, puis on va faire aussi l'allemand. Puis on va faire aussi l'arabe »).
L'allemand devient une **langue d'interface**, proposée **seulement quand on apprend
l'espagnol** (`UI_LANGS` de l'espagnol = fr, en, pt, ar, de). L'app allemande ne la
propose jamais : une interface allemande pour apprendre l'allemand donnerait le mot
pour sa propre traduction.

Modèle : la chaîne arabe (`espanol/ar/`, 15 oct.), elle-même copie du portugais.

## Comment c'est fait

| Étape | Outil |
|---|---|
| Sortir les textes à traduire (hors corpus) | `python espanol/de/extraire.py` → `espanol/de/sources/` |
| Corpus, phrases des temps, exercices | `python espanol/de/poser.py etat \| reste \| pose [--essai] \| controle` |
| Le reste (interface, grammaire, scènes, parcours…) | `python espanol/de/poser_autres.py controle \| pose [nom…]` |
| Consignes données aux traducteurs | `espanol/de/CONSIGNES.md` (glossaire commun, « écrire contre l'allemand ») |
| Lots traduits | `espanol/de/lots/` ; comptes rendus `RAPPORT-*.md` |

## ⚠️ « de » désignait déjà la langue APPRISE

Dans une partie du code, « de » ne veut pas dire « allemand » mais « la langue qu'on
apprend » (héritage d'avant la fusion de l'espagnol) : la voix (`pickVoice("de")` = voix
espagnole en espagnol), l'écoute (`ecouteLangues()` : `cible: "de"`), l'index de
recherche (`entry.de` = le mot appris), les phrases (`ph.de`). Une interface « de »
y entrait en collision :

- **Écouter** lisait deux fois le mot espagnol (connu = cible = « de ») → `connuAllemand`
  dans `contenuEcoute()`, voix `VOIX_ALLEMAND_CONNU` (« de-connu », une voix allemande) ;
- **la recherche** affichait le mot espagnol comme sa propre traduction → `tradRecherche()` ;
- **les réglages des voix** n'offraient pas de voix pour la langue connue → ligne « de-connu ».

Les champs `*_de` eux-mêmes n'existaient nulle part : aucune donnée allemande n'en porte.

## Ce qui est branché dans `index.html`

`SUFFIXE_LANGUE`, `SUFFIXE_CHAMEAU`, `DRAPEAUX_LANGUE` (🇩🇪), `REPLI_LANGUE` (de → en → fr),
`RANGS_CARTE` (de : nomen 27-28, adjektive 25-26, funktionswort 32-34, expression 33-35),
les chargeurs (rangs ajoutés **en espagnol seulement** : l'objet allemand ne change pas),
`RANGS_PP` (Premiers pas, 33-35), `NOM_LANGUE_NATIF`, `LOCALES_ABO`, la consigne de la
dictée, « Écrire » (`question_de`), l'écoute de phrases, les boutons « Deutsch » (cachés
hors de l'espagnol), `UI_LANGS` et `LANGUES_UI_AVEC_ESPAGNOL`. Données : bloc `de:` de
`I18N`, `"de"` de `I18N_ESPAGNOL`, `MOTS_OUTILS_ES_DE`, `de:` des catégories et de
`SCENES_COURTS`. Page des scènes : `TEXTES.de`, `LANGUE`, `REPLI`. `construire.py` porte
l'allemand dans les `scene-*.es.js` (les `scene-*.js` allemands ne bougent pas).

## Reste

Voir la fin de ce fichier, mise à jour à la fin du chantier.
