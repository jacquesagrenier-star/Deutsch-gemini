# Wortando Pflege : le format des données que l'app charge

**Le contrat entre les sessions Pflege** (14 nov. 2026). La session « architecture » (claude/pflege-bcc9b8)
est la seule à toucher `index.html` ; elle intègre les branches des autres. Chaque session écrit ses
fichiers **à ce format**, et un changement de format se décide ici d'abord.

## Règles communes

1. **Partir de la phase 1.** Votre branche est partie de `fb28c88`, avant la phase 1 (`510b6a7` :
   `pflege/sources/`, `pflege/outils/construire.py`, `pflege/datos/themes.json`, `tests/pflege.py`).
   Faites `git merge claude/pflege-bcc9b8` (les fichiers ne se recouvrent pas) avant d'écrire.
2. **Préfixe `soins_` pour tout identifiant** (thème, dialogue, point de grammaire, sujet, scène,
   examen). **Jamais `pflege_`** : le corpus a déjà un thème `pflege_betreuung_c1`, et l'app confondrait.
3. **Les 9 langues d'interface de l'allemand, dans cet ordre** : `fr, en, tr, uk, fa, pt, ar, pl, ru`
   (`pt` = portugais du **Brésil**). Toute traduction est un objet `{"fr": …, "en": …, …, "ru": …}`
   avec les 9 clés, jamais vide.
4. **Aucun chiffre dans un texte allemand dit à voix haute** (phrases, répliques, exemples, écoutes) : la
   voix dit les nombres en lettres, et un chiffre demande une lecture écrite à la main (CLAUDE.md). Si un
   chiffre est indispensable (« 130 zu 85 », « 1-0-1 »), mettez à côté `"lecture": "hundertdreißig zu
   fünfundachtzig"`.
5. **⚕️ = `"relire"`** : un champ texte libre (en français) sur l'élément que l'infirmière relectrice doit
   vérifier en priorité. Vide ou absent sinon.
6. **Des sources, puis un fichier dérivé.** On écrit dans `pflege/sources/` (Python ou JSON), un script de
   `pflege/outils/` fabrique `pflege/datos/` ; `python tests/pflege.py` contrôle. Jamais de correction à
   la main dans `pflege/datos/`.
7. **L'ordre des mots d'un thème est définitif dès la publication** : la progression d'un apprenant est
   rangée par (thème, niveau, rang du mot). On **ajoute en fin de liste** ; on ne réordonne ni ne retire
   un mot publié (le marquer `"retire": true` si besoin).
8. **Les personnages** (`pflege/PERSONNAGES.md`) sont **validés par Jacques** (14 nov., « je valide ») :
   Elif, Amira, Arun, Yusuf, Olena, Jonas, Frau Hoffmann, Dr. Sommer, et les patients, résidents et proches
   (Herr Brandt, Frau Lehmann et sa fille, Herr Schulze, Frau Weber, Frau Kowalski). Leurs prénoms sont
   **définitifs** dans les textes. **Images** : tous permis, soignants compris ; chaque lot annoncé au chef
   avec son coût (règle 9).
9. **Dépenses** (images fal, voix ElevenLabs v2, jamais Flash) : chaque lot annoncé au chef avec son coût
   avant d'être lancé ; hors plan ou au-delà de +20 % de l'estimation, nouvel accord.

---

## 1. Les thèmes de vocabulaire — `pflege/datos/themes.json` (session « vocabulaire »)

**Source** : un fichier par thème, `pflege/sources/<thème>.py`, avec `THEME` et `MOTS`, puis le nom du
thème ajouté à la liste `THEMES` de `pflege/outils/construire.py` (dans l'ordre de l'annexe A).
Modèle : `pflege/sources/vitalzeichen.py` (phase 1, 31 noms).

```python
THEME = {
    "base": "soins_koerper",                       # id du thème, sans niveau
    "nom_theme": "Körper, Schmerzen und Symptome", # le nom allemand, affiché
    "nom_theme_fr": "Le corps, la douleur, les symptômes",
    "nom_theme_trad": {"fr": …, "en": …, "tr": …, "uk": …, "fa": …, "pt": …, "ar": …, "pl": …, "ru": …},
    "svg": '<svg viewBox="0 0 24 24">…</svg>',     # une icône au trait, comme les thèmes du corpus
}
MOTS = [ … ]   # une entrée par mot, au format ci-dessous
```

**Une entrée de `MOTS`**, au choix :

- **le tuple des noms** de la phase 1 (`(niveau, genre, mot, pluriel, article_fr, {langue: (traduction,
  exemple)}, exemple_de, relire)`), toujours accepté ;
- **le dictionnaire**, obligatoire pour tout ce qui n'est pas un nom :

```python
{
    "niveau": "B1",                 # A2, B1, B2 ou C1
    "sorte": "nom",                 # nom | verbe | adjectif | expression
    "mot": "Schmerz",               # nom : sans article ; verbe : l'infinitif ; expression : la phrase entière
    "genre": "der",                 # nom seulement : der | die | das
    "pluriel": "Schmerzen",         # nom seulement ; "—" s'il n'y en a pas
    "article_fr": "la ",            # nom seulement : l'article français de la traduction (« la », « le », « l' », « les »)
    "perfekt": "hat wehgetan",      # verbe seulement : auxiliaire + participe passé
    "exemple": "Wo tut es Ihnen weh?",            # l'exemple allemand, en situation de soins, sans chiffre
    "trad": {"fr": ("douleur", "Où avez-vous mal ?"), …, "ru": (…, …)},  # (traduction, exemple traduit), 9 langues
    "corpus": False,                # True si le mot existe déjà dans themes.json (tests/pflege.py le signale)
    "relire": "",                   # ⚕️
}
```

- La traduction est le **terme du métier** dans la langue cible (« escarre », *pressure ulcer*), pas un
  mot à mot.
- Un thème a **ses quatre sortes ensemble**, dans l'ordre d'apprentissage voulu ; l'app range les cartes
  par sorte (noms, verbes, adjectifs, expressions) et par niveau.
- Les noms déjà au corpus (`"corpus": True`) restent dans la liste, avec leur exemple de soins : la phase
  d'intégration décidera s'ils rejoignent la fiche du corpus.

**Sortie** (fabriquée par `construire.py`, ne pas écrire à la main) : `{"_note", "themes": [ {id
"soins_<thème>_<niveau>", nom_theme, nom_theme_fr, nom_theme_trad, niveau, svg, mots: [ {mot, sorte,
genre, pluriel, perfekt, traduction (fr), traduction_<langue>, exemple, exemple_<langue>, article_fr,
corpus, relire} ] } ] }`.

---

## 2. Les dialogues — `pflege/datos/dialogues.json` (session « dialogues »)

```json
{"_note": "…", "dialogues": [{
  "id": "soins_dlg_02_schmerz",
  "numero": 2,
  "niveau": "B1",
  "titre_de": "Schmerzen erfragen",
  "titre": {"fr": "La douleur de 0 à 10", "en": …, …, "ru": …},
  "lieu": "chambre",
  "scene": "soins-zimmer",
  "personnages": ["elif", "brandt"],
  "apprenant": "elif",
  "but": {"fr": …, …},
  "repliques": [
    {"qui": "elif", "de": "Haben Sie Schmerzen, Herr Brandt?", "trad": {"fr": …, …}, "lecture": ""},
    {"qui": "brandt", "de": "Ja, an der Hüfte.", "trad": {…}}
  ],
  "redemittel": [{"de": "Wo genau tut es weh?", "trad": {…}}],
  "questions": [
    {"type": "vrai_faux", "de": "Herr Brandt hat keine Schmerzen.", "trad": {…}, "bon": false},
    {"type": "choix", "de": "Wo hat Herr Brandt Schmerzen?", "trad": {…},
     "choix": [{"de": "an der Hüfte", "trad": {…}}, {…}, {…}], "bon": 0}
  ],
  "grammaire": ["soins_gr_09_indirekte_fragen"],
  "prepare": ["sprechen_1", "hoeren_2"],
  "relire": "⚕️ …"
}]}
```

- `apprenant` : le personnage dont l'apprenant joue les répliques (« jouer son rôle »).
- `qui` : un id de personnage en minuscules (`elif`, `jonas`, `hoffmann`, `sommer`, `brandt`, `lehmann`,
  `lehmann_tochter`, `schulze`, `weber`, `kowalski`, `amira`, `arun`, `yusuf`, `olena`, `kraemer`).
  `kraemer` = **Dr. Krämer**, médecin de garde (un homme), rôle secondaire retenu avec l'examen blanc
  (14 nov. ; le chef a écarté « Neumann »). Trois rôles de l'examen blanc parlent aussi dans les dialogues
  (accord de l'architecture, 15 nov.) : `aksoy` (Frau Aksoy, laboratoire) et `richter` (Herr Richter, pharmacie)
  dans d19, `schulze_tochter` (Monika Schulze, la fille de Herr Schulze) dans d24 et d26.
- L'allemand **parlé** (*mal*, *genau*, *ne*), 12 à 20 répliques en principe ; `repliques` est le **chemin
  modèle** (jusqu'à 24, comme d01).
- **Champs en plus, acceptés** (14 nov., session « dialogues ») : `source`, `registre`, `intro`, et l'arbre
  des branches `debut` + `noeuds`, au format des conversations jouées (`visuel/prototype/conversation/` :
  choix justes, fautes avec leur aide, répétitions). L'app lira l'arbre quand il existe, sinon `repliques`.
- `prepare` : les parties du telc qu'il prépare (`hoeren_1`…`hoeren_4`, `lesen_1`…, `sprechen_1`…`sprechen_3`,
  `schreiben`).

## 2 bis. Les cartes-phrases (« Redemittel » par fonction) — `pflege/datos/redemittel.json` (session « dialogues »)

> **Accepté par l'architecture le 15 nov.** (proposition de la session « dialogues »), avec les groupes demandés
> par le chef. **Cette sortie est la source unique des Redemittel** : le chapitre 6 du manuel B2 (session
> pflege-examen) la lit au lieu d'avoir son propre fichier.

**Deux sources, une sortie.**
1. **Les cartes des dialogues** : le champ `redemittel` de chaque dialogue (5 à 10 par dialogue), déjà
   traduit et déjà lu par la voix d'Aurora (`<id>/rm/<n>` dans `pflege/datos/sons.json`). On ne le recopie
   pas : on lui ajoute une **fonction**.
2. **Les cartes sans dialogue** : `pflege/sources/redemittel/<groupe>.json`, **écrites par pflege-examen,
   dans ces fichiers-là seulement** ; la chaîne de la session « dialogues » les construit, les contrôle et
   les fait lire.

Les 7 fonctions et les 8 groupes (titre, conseil, 9 langues) sont dans `pflege/sources/redemittel-fonctions.json`,
tenu par la session « dialogues » (hors du dossier des groupes, pour ne pas le gêner).

**Une carte de dialogue** (`pflege/sources/dialogues/dNN-*.json`, dans `redemittel`) :

```json
{"t": "Ich mache mir Sorgen. Ich glaube, er muss schnell untersucht werden.", "fr": "…",
 "fonction": "transmettre",
 "situation": {"fr": "Tu appelles le médecin de garde la nuit et tu dis ton inquiétude."}}
```

- `fonction` (**obligatoire**) : `annoncer` · `demander` · `rassurer` · `refuser` · `reformuler` · `transmettre` ·
  `redemander`. Une seule par carte : celle qu'on apprend en la disant.
- `situation` (facultatif) : quand on la dit, en une phrase, traduite comme tout texte. **Absente, elle vaut le
  titre du dialogue**, déjà traduit.
- `groupe` (facultatif) : `patient` · `famille` · `collegues` · `releve` · `sbar` · `visite` · `negociation` ·
  `telephone`. **Absent, il se déduit du dialogue** (`GROUPE_DIALOGUE` dans `pflege/outils/textes.py`).
- Le registre vient du dialogue ; dans un dialogue « du+Sie », il se lit sur la phrase (du / dich / dir / dein).

**Une carte sans dialogue** (`pflege/sources/redemittel/<groupe>.json`, le nom du fichier = le groupe) :

```json
{"groupe": "telephone",
 "cartes": [
  {"t": "Können Sie mir bitte Ihren Namen buchstabieren?", "fr": "Pouvez-vous m'épeler votre nom, s'il vous plaît ?",
   "en": "…", "tr": "…", "uk": "…", "fa": "…", "pt": "…", "ar": "…", "pl": "…", "ru": "…",
   "fonction": "redemander", "niveau": "B1", "registre": "Sie",
   "situation": {"fr": "Au téléphone, tu n'as pas compris le nom.", "en": "…", …}}
 ]}
```

- `t`, `fr`, `fonction`, `niveau` (A2 à C1), `registre` (`du` ou `Sie`) et `situation` **obligatoires** ; un chiffre dans `t`
  demande un `dit` en lettres (règle 4) ; un nom de personnage passe par un gabarit (`{brandt:dat}`).
- Les traductions peuvent être **écrites dans la source** (les 9 langues sur la carte), ou laissées à la
  chaîne de traduction (`traductions/<langue>/redemittel/<groupe>.json`, préparé par `textes.py extraire`) ;
  **une traduction écrite dans la source l'emporte toujours** (corriger une langue = corriger la source).
- **On ajoute en fin de liste** ; on ne retire ni ne réordonne une carte publiée (`"retire": true`).

**Sortie** (fabriquée par `textes.py construire`, ne pas écrire à la main) : `pflege/datos/redemittel.json`

```json
{"_note": "…", "langues": ["fr", …, "ru"],
 "fonctions": [{"id": "annoncer", "titre": {"fr": "Annoncer ce qu'on va faire", …}, "conseil": {…}}, …],
 "groupes": [{"id": "patient", "titre": {"fr": "Avec le patient", …}}, …],
 "cartes": [{
   "id": "soins_rm_07_4",              // dialogue : numéro + rang ; sans dialogue : soins_rm_<groupe>_<rang>
   "fonction": "transmettre", "groupe": "sbar",
   "niveau": "B2", "registre": "Sie",
   "de": "Ich mache mir Sorgen. …", "lecture": "", "trad": {"fr": …, …, "ru": …},
   "situation": {"fr": …, …},
   "dialogue": "soins_dlg_07_sbar", "apprenant": "yusuf",   // "" pour une carte sans dialogue
   "son": "soins_dlg_07_sbar/rm/4",    // la clé de sons.json ; une carte sans dialogue a son id pour clé
   "relire": ""
 }]}
```

- **L'id est stable** (règle 7) : la progression d'un apprenant sur une carte est rangée par `id`. Le rang part
  de 0, comme les clés `rm`.
- Les cartes sont rangées par fonction, puis par niveau, les cartes de dialogue avant les autres.
- **Jamais deux fois le même `de`** dans toute la sortie (le contrôle le refuse) : c'est ce qui évite les
  doublons entre le manuel et les dialogues. Une carte à trou (« Ich wiederhole die Dosierung: … ») reste une
  carte : les points de suspension disent ce qu'on complète.
- État au 15 nov. : **185 cartes**, toutes de dialogue (d01-d26) ; 82 ont déjà leur son (d01-d12), celles de
  d13-d26 font partie du lot de voix des 14 dialogues, et les cartes sans dialogue y ajouteront le leur.
- Contrôle : `python tests/pflege_dialogues.py` (fonction, groupe, niveau, registre, situation, id, doublons).

## 3. La grammaire du métier — `pflege/datos/grammaire.json` (session « dialogues »)

```json
{"_note": "…", "points": [{
  "id": "soins_gr_01_sie_imperativ",
  "numero": 1,
  "niveau": "A2",
  "titre": {"fr": "Sie et l'impératif poli", …},
  "regle": {"fr": "Une ou deux phrases.", …},
  "exemples": [{"de": "Setzen Sie sich bitte auf.", "trad": {…}}],
  "renvoi": "",
  "serie": [
    {"type": "choix", "de": "___ Sie sich bitte auf die Seite.", "choix": ["Drehen", "Dreht", "Drehst"], "bon": 0,
     "phrase": "Drehen Sie sich bitte auf die Seite.", "trad": {…}, "note": {"fr": …, …}}
  ]
}]}
```

- `type` : `choix` (trou à choix), `ordre` (remettre les mots dans l'ordre : `mots` au lieu de `choix`),
  `vrai_faux`. 10 questions par série.
- `renvoi` : l'**id de la `<section>`** d'`index.html` qui explique la règle générale (`praepInfo`,
  `konjunktionenInfo`, `relativInfo`, `wortstellungInfo`, `verbenTempsInfo`, `adverbienInfo`,
  `personalpronomenInfo`…), ou `""`. L'app l'ouvre par `showScreen(renvoi)`.
- **Champs en plus, acceptés** : `resume`, `tableau`, `piege`, `dialogues` (les dialogues où le point sert).
  Une question « choisir la bonne phrase » est un `choix` avec `"de": "___"` et une `consigne`.

## 4. L'écrit — `pflege/datos/ecrit.json` (session « dialogues »)

```json
{"_note": "…", "sujets": [{
  "id": "soins_ecrit_aufnahme_01",
  "type": "aufnahme",
  "niveau": "B1",
  "consigne": {"fr": …, …},
  "fiche": {
    "titre_de": "Pflegeanamnese / Aufnahmebogen",
    "rubriques": [
      {"rubrique_de": "Sehen", "champs": [{"label_de": "Brille", "coche": true}, {"label_de": "Hörgerät", "coche": false}]},
      {"rubrique_de": "Sich bewegen", "texte_de": "Rollator, Beaufsichtigung beim Gehen"}
    ]
  },
  "briques": [{"de": "Frau L. wurde am … aufgenommen.", "trad": {…}}],
  "corrige_de": "Le texte modèle, en phrases complètes.",
  "points_cles": ["Brille", "Rollator", "Beaufsichtigung"],
  "relire": "⚕️ …"
}]}
```

- `type` : `aufnahme` et `biografie` (les deux tâches de l'examen), puis `pflegebericht`, `sturz`,
  `nachricht`.
- `points_cles` : chaque information de la fiche qu'un bon texte reprend (sert à l'autocorrection :
  l'examen enlève des points pour chaque information oubliée).
- `niveau` : `"B1"`, avec **`niveau_max`** `"B2"` pour les 8 sujets d'examen (aufnahme, biografie).
- **Champs en plus, acceptés** : `titre`, `consigne_de`, la rubrique traduite, `briques_groupes`, `corrige`
  (traduit), `corrige_b1_de` / `corrige_b1` (un texte modèle de niveau B1 à côté du B2), `points` (avec `id`
  et traduction), `pieges`, `grille` ; et au niveau du fichier, **`grilles`** : la grille d'auto-évaluation
  sur les quatre critères du telc (contenu, forme, correction, vocabulaire).
- Ces trois fichiers sont fabriqués par **`pflege/outils/textes.py`** à partir de
  `pflege/sources/{dialogues,grammaire,ecrit}/` ; contrôle : `python tests/pflege_dialogues.py`.

## 5. Les scènes — `visuel/prototype/soins-<nom>.points.json` (session « scènes »)

- **Le format des scènes existantes, à l'identique** (`visuel/prototype/arztpraxis.points.json`, et son
  `_lisez_moi`) : `image`, `titre`, `alt`, `consigne`, `points` (`id`, `mot`, `boite`/`boites`, `sur`,
  `aussi`), `couches`, `gros_plans`, et les masques par la chaîne habituelle (`detourer.py`).
- **Le nom des fichiers commence par `soins-`** : `soins-zimmer`, `soins-stationszimmer`, `soins-bad`,
  `soins-uebergabe`, `soins-aufnahme`, `soins-visite`, `soins-altenheim`, `soins-ambulant`.
- **Le mot d'un point** doit exister dans `pflege/datos/themes.json` **ou** dans le corpus général. Un mot
  qui manque aux deux : le signaler à la session « vocabulaire » (et à moi), ne pas l'inventer dans la
  scène.
- **Une couche `A1` au titre seul** (« Les objets de la chambre ») est permise : c'est elle qui ouvre
  Découvrir et Trouve !, le toucher des mots, comme dans toutes les scènes. Aucune question A1.
- **Les couches** : `A2`, `B1`, `B2`, `C1`, au format des scènes (`titre`, `qs` : `q`, `c`, `f`, `r`,
  `phrase`, `sens`, `n`), plus **`SIT`** pour la couche « Situation » : mêmes champs, et `"type":
  "situation"` sur chaque question (la bonne réponse est toujours `c[0]`, comme ailleurs).
- `sens` et `n` : en français dans le `points.json` (comme les scènes actuelles) ; les 8 autres langues
  dans `traductions/soins-<nom>.<langue>.json`, au format des traductions de scènes existantes.
- **Pas de `.es.js`, `.en.js`, `.pt.js`** pour l'instant : c'est moi qui fais lire
  `pflege/datos/themes.json` par `construire.py` et qui lui fais sauter les variantes des scènes `soins-`.
  En attendant, construisez avec `--de-seulement` si l'option existe, sinon dites-le-moi.
- Images **neutres** (décision du 14 nov., Q8) : aucun écriteau, rien de propre à l'Allemagne, pour
  servir plus tard l'espagnol médical.
- **Ne touchez pas à `index.html`** (`SCENES_TOUTES`, séance) : je branche les scènes à l'intégration.

## 6. L'examen blanc — `visuel/prototype/telc-pflege/` (session « examen »)

- **Une page à part, sur le modèle exact du module telc A2·B1** (`visuel/prototype/telc/` : `telc.html`,
  `telc-commun.js`, un module par partie, `examen-blanc.js`, `donnees/*.json`, `langues/`). Copiez-en la
  structure dans `visuel/prototype/telc-pflege/` ; **ne modifiez pas** `visuel/prototype/telc/`.
- **Mêmes paramètres d'URL** que `telc.html` : `apprendre=de`, `lang=<langue d'interface>`, `nuit=1`,
  `partie=<partie>` ; même façon de rendre la main à l'app (lisez `telc-commun.js`). Je l'ouvrirai depuis
  l'écran Soins par une fonction `ouvrirTelcPflege(partie)`, copie de `ouvrirTelc`.
- **Les données** : `visuel/prototype/telc-pflege/donnees/{hoeren,lesen,sprachbausteine,schreiben,sprechen}.json`,
  au format des fichiers de `visuel/prototype/telc/donnees/` (`series`, `T1`, `T2`…, `bon` en indice,
  champs d'élève suffixés `_fr`, `_en`…, l'allemand sans suffixe).
- **Le format exact de l'examen** : `pflege/FORMAT-TELC-PFLEGE.md` (23 + 18 + 18 questions, l'écrit A / B
  sur quatre critères, l'oral en cinq temps sur 100, le calcul du certificat B1 / B2). Textes **écrits
  pour Wortando**, jamais copiés du test modèle (qui reste hors du dépôt).
- **Le résultat** : à la fin d'un examen blanc, la page envoie à l'app (par le même canal que le telc)
  `{type: "resultat_examen", examen: "soins_telc", date, points: {hls: n, schreiben: n, sprechen: n},
  certificat: "B2" | "B1" | "aucun"}` ; c'est ce que lira le tableau de bord (« prêt pour l'examen »).
- Les voix des écoutes : un lot à chiffrer et à annoncer au chef avant de les produire.

---

## Ce que je fais de mon côté (architecture)

- `construire.py` accepte le dictionnaire et la `sorte` (dès maintenant) ; `tests/pflege.py` contrôle les
  quatre fichiers à mesure qu'ils arrivent.
- L'app : les cartes par sorte, l'écran Soins en blocs (Mots · Scènes · Dialogues · Grammaire · Écrire ·
  Examen), la lecture de `dialogues.json`, `grammaire.json`, `ecrit.json`, l'ouverture des scènes `soins-`
  et de `telc-pflege/`, puis le suivi (tableau de bord).
- L'intégration de vos branches : prévenez-moi (SendMessage) quand un lot est prêt, avec le commit.
