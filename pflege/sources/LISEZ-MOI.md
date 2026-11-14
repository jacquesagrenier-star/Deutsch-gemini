# Wortando Pflege : les textes (dialogues, grammaire, écrit)

Session « dialogues, grammaire, écrit », 14 nov. 2026. Ce dossier contient ce qu'on **écrit et corrige à la
main** ; `pflege/datos/` en est **dérivé** (règle du PLAN § 4.2) et ne se corrige jamais à la main.

```
pflege/sources/
  noms.json                         ← les personnages : leurs noms en allemand et en français (formes)
  dialogues/dNN-<id>.json           ← un dialogue (allemand + français)
  grammaire/gNN-<id>.json           ← un point de grammaire : fiche + série (allemand + français)
  ecrit/<id>.json                   ← une tâche d'écrit : fiche de départ, briques, modèle, grille
  traductions/<langue>/...          ← les 7 autres langues, un fichier par source (même chemin)
pflege/outils/textes.py             ← extraire (prépare les traductions), construire (fait datos/)
pflege/datos/dialogues.json         ← DÉRIVÉ : les 12 dialogues, 9 langues, noms remplacés
pflege/datos/grammaire.json         ← DÉRIVÉ : les 21 fiches et leurs séries
pflege/datos/ecrit.json             ← DÉRIVÉ : les tâches d'écrit
tests/pflege_dialogues.py           ← le contrôle (clés, 9 langues, niveaux, nombres, noms, balises)
```

## Les langues

Les 9 langues d'interface de l'allemand : `fr en tr uk fa ar pt pl ru` (`pt` = portugais du Brésil, comme
partout dans l'interface). Le français est écrit dans la source ; les 7 autres (et l'anglais) vivent dans
`traductions/<langue>/`, pour que plusieurs traducteurs travaillent sans toucher au même fichier.

**La règle d'unité** : tout objet qui a une clé `"fr"` est un texte à traduire. Ses traductions vont dans les
clés sœurs (`"en"`, `"tr"`…). C'est le format des conversations jouées (`visuel/CONVERSATIONS.md`) et des fiches
espagnoles (`espanol/datos/grammaire.json`) : `{"t": "<allemand>", "fr": "…", "en": "…"}` pour une réplique,
`{"fr": "…", "en": "…"}` pour un texte d'interface (titre, consigne, aide).

`python pflege/outils/textes.py extraire` écrit, pour chaque langue, la liste des unités à traduire
(`traductions/<langue>/<famille>/<id>.json` : `{chemin: {"de": …, "fr": …, "<langue>": ""}}`) en gardant ce qui
est déjà traduit. Si le français d'une unité change, sa traduction est marquée **périmée** (le contrôle la refuse
tant qu'elle n'est pas refaite).

## Les noms (remplaçables)

Les noms ne sont jamais écrits en dur : `{elif}`, `{brandt}`, `{brandt:dat}` (« Herrn Brandt »),
`{brandt:voc}` (« monsieur Brandt » en français, « пане Брандте » en ukrainien). `noms.json` donne chaque forme
en allemand et en français ; `traductions/<langue>/noms.json` dans les autres langues (les langues à
déclinaison y mettent leurs cas). `construire` remplace les gabarits : **changer un nom = changer `noms.json`
(et ses 7 traductions), puis reconstruire.** Le contrôle refuse un gabarit sans sa forme dans la langue.

Limite connue : un nom remplacé peut demander un autre suffixe (turc `{elif}'e` / `Arun'a`, harmonie
vocalique) ou un autre genre (« die Ärztin » pour Dr. Sommer). Le contrôle ne le voit pas : relire les phrases
du personnage changé.

## Les nombres

Toute phrase allemande **prononcée** qui contient un chiffre a sa lecture en lettres dans `"dit"` (règle de
CLAUDE.md, « les nombres se disent en lettres ») : `{"t": "Blutdruck 130 zu 80.", "dit": "Blutdruck
hundertdreißig zu achtzig."}`. Le contrôle refuse un chiffre sans `dit`, et un `dit` qui garde un chiffre.
Prononcé : répliques, choix, Redemittel, exemples et phrases des séries. Non prononcé (exempté) : les fiches de
départ et les modèles de l'écrit (`"prononce": false`). Au moment de la voix, les lectures iront dans
`audio/lectures/de.json`.

## À relire par l'infirmière

`"relire": true` sur toute unité dont le **contenu de soin** doit être validé (geste, ordre des gestes, dose,
valeur, protocole, limite de compétence), avec `"relire_note"` en français : ce qu'il faut vérifier. Le contrôle
compte ces unités ; la liste sort par `python tests/pflege_dialogues.py --relire`.

## Un dialogue (`dialogues/dNN-<id>.json`)

Le format des conversations jouées (`visuel/CONVERSATIONS.md`), plus ce qu'il faut à la section Soins :

```json
{
 "id": "d02-schmerzen", "numero": 2, "niveau": "B1", "registre": "Sie",
 "lieu": "klinikum", "role": "elif", "personnes": ["brandt"],
 "titre": {"de": "Schmerzen erfragen", "fr": "…"}, "intro": {"fr": "…"}, "but": {"fr": "…"},
 "grammaire": ["g05", "g06", "g09"], "telc": ["oral-1", "oral-3", "hoeren"],
 "redemittel": [{"t": "Wo genau tut es weh?", "fr": "…"}],
 "debut": "klingel",
 "noeuds": {
  "klingel": {
   "dit": [{"recit": {"fr": "…"}}, {"qui": "brandt", "air": "attentive", "t": "…", "fr": "…"}],
   "choix": [
    {"t": "…", "fr": "…", "va": "skala", "puis": [{"qui": "brandt", "t": "…", "fr": "…"}]},
    {"faux": true, "t": "…", "fr": "…", "puis": […], "aide": {"fr": "<b>…</b> …"}},
    {"repete": true, "t": "…", "fr": "…", "va": "klingel", "puis": […]}
   ]
  }
 },
 "ecouter": [{"q": {"t": "Wo hat {brandt} Schmerzen?", "fr": "…"},
              "options": [{"t": "…", "fr": "…"}, …], "juste": 0}]
}
```

- `role` : le soignant que joue l'apprenant (ses répliques sont les `choix`) ; `personnes` : les autres.
- `t` : l'allemand ; `dit` : sa lecture si elle diffère (nombres) ; `air` : `sourire`, `question`, `attentive`,
  `surprise`, `perplexe`, `amuse` (les visages des conversations, repli compris).
- `va` : le nœud suivant, `null` = fin. `faux` : une faute (de langue **ou de soin**) ; la personne réagit, `aide`
  explique, on réessaie (pas de `va`). `repete` : demander de répéter, revient au même nœud. Toujours une fin
  réussie ; chaque nœud a au moins une réponse juste.
- Les trois exercices du plan : **écouter et répondre** = `ecouter` (questions en allemand, la réponse est dans
  les répliques communes à tous les chemins) ; **remettre dans l'ordre** et **jouer son rôle** = dérivés du
  chemin juste (premier choix juste de chaque nœud) par `construire` (`chemin` dans `datos/dialogues.json`),
  rien à écrire.
- `registre` : `Sie` partout, sauf le dialogue 11 (`du` entre collègues, `Sie` avec la cadre : `registre:
  "du+Sie"`, chaque nœud dit le sien).

## Un point de grammaire (`grammaire/gNN-<id>.json`)

La fiche suit les fiches espagnoles (`titre`, `resume`, `regle`, `tableau`, `exemples`), plus le renvoi vers la
fiche générale de l'allemand et la série de 10 questions :

```json
{
 "id": "g10", "cle": "passiv-praesens", "numero": 10, "niveau": "B1",
 "titre": {"fr": "…"}, "resume": {"fr": "…"}, "regle": {"fr": "…"},
 "tableau": [["", {"fr": "…"}], ["Aktiv", {"t": "Ich wechsle den Verband.", "fr": "…"}]],
 "exemples": [{"t": "Der Verband wird jeden Tag gewechselt.", "fr": "…"}],
 "piege": {"fr": "…"},
 "renvoi": "verbenTempsInfo",
 "dialogues": ["d03", "d06"],
 "serie": [
  {"type": "trou", "t": "Der Blutzucker ___ viermal täglich gemessen.", "options": ["wird", "ist", "hat"],
   "juste": "wird", "phrase": {"t": "Der Blutzucker wird viermal täglich gemessen.", "fr": "…"},
   "explication": {"fr": "…"}}
 ]
}
```

Types de question : `trou` (un mot à choisir), `choix` (une phrase juste parmi trois : `options` en allemand),
`ordre` (remettre les morceaux : `morceaux` dans l'ordre juste). `renvoi` : l'écran de la fiche générale
(`<section id>` d'`index.html`), vérifié par le contrôle ; `null` s'il n'y en a pas.

## Une tâche d'écrit (`ecrit/<id>.json`)

```json
{
 "id": "aufnahme-1", "genre": "aufnahmebericht", "niveau": "B1-B2", "examen": true, "prononce": false,
 "titre": {"fr": "…"}, "consigne": {"t": "Schreiben Sie …", "fr": "…"},
 "fiche": {"titre": "Pflegeanamnese", "rubriques": [{"t": "Name", "valeur": "…"}, …]},
 "points": [{"id": "p1", "t": "aufgenommen am 12.11. wegen Sturz", "fr": "…"}],
 "briques": [{"t": "… wurde am … mit … aufgenommen.", "fr": "…"}],
 "modele": {"niveau": "B2", "t": "…", "fr": "…"},
 "modele_b1": {"t": "…", "fr": "…"},
 "grille": "telc-pflege"
}
```

- `points` : les informations de la fiche, une par ligne : c'est le critère **contenu** du barème (« reprendre
  toutes les informations ») ; le modèle les reprend toutes, le contrôle vérifie qu'aucune n'est oubliée dans la
  liste de contrôle du modèle (`modele.couvre`).
- `grille` : la grille d'auto-évaluation commune (`ecrit/grille-telc-pflege.json`), sur les quatre critères du
  barème (`pflege/FORMAT-TELC-PFLEGE.md`) : contenu, forme du texte, correction, vocabulaire, 0 à 5 chacun.
- Aucun texte du test modèle telc n'est repris : fiches, personnes et modèles sont écrits pour Wortando.
