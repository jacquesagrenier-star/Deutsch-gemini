# Un moteur, deux langues : conception de Wortando Japonais

*Document de conception, sans code applicatif. Branche `japonais-moteur`, 6 octobre 2026.
Base mesurée : `index.html` v709 (`APP_VERSION = 709`, 36 539 lignes, 2 250 744 octets).*

Tous les comptes de ce document se relancent :

```
python3 japonais/moteur/inventaire.py          # section 1 : ce qui est encore allemand
python3 japonais/moteur/verifier_capacites.py  # section 1.4 : les portes sans capacité
python3 japonais/moteur/construire_exemples.py # section 2 : exemples tirés des branches
python3 japonais/moteur/mesurer_polices.py     # section 3.2 : poids des polices (réseau)
```

---

## Résumé (une page)

**La recommandation.** On garde **un seul `index.html`** et on le publie à **deux adresses** : `/` pour l'allemand, `/ja/` pour le japonais. La langue enseignée se déduit de l'adresse au démarrage, dans une table `LANGUES` qui prolonge `LANGUE_ENSEIGNEE`. Il n'y a ni générateur ni fork. Ce que la langue ne déclare pas disparaît : chaque porte de l'interface (tuile, option, exercice) déclare une **capacité**, et une langue ne voit que les capacités qu'elle déclare. Le vérificateur refuse une porte qui n'en déclare aucune. Une nouveauté allemande ne peut donc plus apparaître en japonais par oubli : pour exister quelque part, elle doit dire où.

Le japonais n'entre pas dans les tuples de l'allemand. Ses entrées sont des **fiches** : un identifiant stable, des champs nommés, et pour chaque champ sa source et son statut de relecture. Les formes fléchies ne sont pas stockées : elles sont calculées par le moteur de `japonais-conjugaison`, qui passe ses 284 593 vérifications. L'allemand pourra passer aux fiches plus tard sans perdre de progression : chaque fiche portera la clé exacte sous laquelle `cleMot()` range aujourd'hui sa progression.

**Les trois décisions que Jacques doit trancher.**

1. **Une adresse par langue sur le même domaine** (recommandé : `…github.io/Deutsch-gemini/ja/`, puis `wortando.com/ja/`), ou bien une app unique avec un sélecteur de langue. Ce choix détermine les fiches magasin, les icônes d'écran d'accueil et la façon dont Capacitor charge l'app (§5).
2. **Un seul compte Wortando pour toutes les langues.** Cela veut dire le même projet Firebase `deutschai-b6fbb` et les mêmes codes d'invitation. Recommandé : la progression japonaise va dans un **document Firestore à part** (`users/{uid}/cours/ja`), ce qui demande de modifier `firestore.rules`. L'autre voie est un projet Firebase séparé. Le document unique actuel a une limite de taille (§8).
3. **D'où vient la traduction française affichée des mots.** C'est bloquant pour les données : `mots.json` contient **0 glose française sur 8 293** entrées, car JMdict était injoignable au moment de la construction. Il faut choisir entre :
   - les gloses françaises de JMdict, avec un choix manuel ;
   - une traduction depuis l'anglais, marquée « brouillon » et relue ;
   - et dans les deux cas, décider **qui relit** : un natif japonais, un francophone, ou les deux.

**Le premier pas sûr (étape 1 du §6).** Il ne change rien d'interface :
- ajouter `capacites` à `LANGUE_ENSEIGNEE`, avec la liste complète pour l'allemand ;
- poser `data-capacite` sur les 29 tuiles de l'accueil ;
- ajouter au vérificateur la règle « pas de tuile sans capacité ».

L'allemand déclare tout, donc il ne perd rien. La preuve se fait en comparant la liste des tuiles visibles avant et après le changement. Le prototype du contrôle tourne déjà : `verifier_capacites.py` liste les 29 tuiles à annoter.

**Taille du chantier (estimation, détail au §6).**
- Côté allemand, environ **300 lignes touchées**, en 10 étapes livrables une à une, sans changement visible.
- Côté japonais, du code neuf derrière ses capacités, à peu près **2 000 à 3 000 lignes** : écrans kana et kanji, fiches, furigana, suivi de deux objets liés.
- Les données japonaises demandent un travail à part (gloses, relecture) qui dépasse le code.

**Écarts entre la consigne et les données réelles** (à lire avant le §2) :
- `mots.json` n'a ni glose française, ni JMdict, ni partie du discours. Le constat « gloses françaises en vrac alphabétique » **ne se reproduit pas** : les seules gloses françaises sont celles des kanji, rangées dans l'ordre de KANJIDIC2 (88 listes triées sur 1 413, soit le hasard).
- Il y a **79 kanji N5**, pas 103, dans `kanji.json` comme dans `mnemoniques_n5.json`.
- Les 16 validations de Jacques **ne sont inscrites nulle part** : les 79 entrées portent toutes `"statut": "brouillon à relire"`.
- `phrases.json` n'a jamais été produit, car Tatoeba était bloqué.

---

## 1. Inventaire mesuré de ce qui est encore allemand dans `index.html`

La source est `python3 japonais/moteur/inventaire.py`. Chaque ligne donne un nombre de **lignes** d'`index.html` qui contiennent le motif, avec la regex (ERE) utilisée. Ces comptes portent sur des lignes, pas sur des occurrences. Le dictionnaire I18N compte : un terme allemand apparaît dans 6 langues d'interface.

### 1.a Déjà paramétré : le point de départ

| Élément | Lignes | Ce qu'il fait | Motif |
|---|---:|---|---|
| `LANGUE_ENSEIGNEE` (l. 9762) | 9 | `{code:"de", nom, voix:"de-DE", donnees, audio}` | `LANGUE_ENSEIGNEE` |
| `urlDonnees()` (l. 9786) | 14 | Les **12** `fetch` de données passent tous par elle | `urlDonnees\(` |
| `ASSETS_BASE` (l. 9782) | 2 | Logo, vidéos : ce qui appartient à la marque | `ASSETS_BASE` |
| `prefixeLangue()` (l. 21268) | 3 | `""` pour `de`, sinon `code + "__"` | `prefixeLangue\(` |
| `progressKey()` / `directionScopedKey()` | 10 / 33 | Rangent progression, série, objectif, XP | |
| `exercices.json` → `startExerciseSet` (l. 35711) | 7 | v392 : 31 jeux, un seul goulot | |
| `grammaire.json` | 4 | v393 : 16 écrans | |
| `AUDIO_BASE = LANGUE_ENSEIGNEE.audio` (l. 30395) | 7 | Base des mp3 | |

Le vérificateur protège déjà une règle : `verifier_langue_enseignee()` (`tests/verifier.py` l. 337) refuse `code = "en"`.

**À savoir.** Le fork espagnol **garde `code: "de"`**. Il isole sa progression en renommant `STORAGE_KEY` en `wortandoEs_progress_v4`, avec 43 clés `wortandoEs_` (`grep -c wortandoEs_ espanol/index.html`). Le préfixe `es__` n'a donc jamais servi.

### 1.b Propre à l'allemand : à désactiver pour une autre langue

| Sujet | Lignes | Où (fonction ou constante) | Motif |
|---|---:|---|---|
| Tuiles d'accueil allemandes | **15** | `<div class="orb orb-de" data-orbid=…>` (l. 6641 et suivantes) | `class="orb orb-de"` |
| Tuiles du module anglais | 14 | `orb-en`, affichées par `body[data-learning-dir="en"]` (CSS l. 1157) | `class="orb orb-en"` |
| Panneaux de tuile | **17** | `orbPanelData(id)` (l. 22938, 352 lignes), **93** `action:"…"` | `if\(id === "…"\)\{` |
| Exercices `start…Uebung/Exercise` | 29 | ex. `startWortstellungV2Exercise`, `startAlsWennUebung` | `^function start…` |
| Écrans d'explication `open…Info` | 16 | ex. `openPraepInfo`, `openPartikelnInfo` | `^function open…Info\(` |
| Cas grammaticaux | 408 | écrans `kasusInfo`, `praepInfo`, I18N | `Akkusativ\|Dativ\|Genitiv\|Nominativ` |
| Articles der/die/das | 38 | tuple de thème, rang 1 (`w.genre \|\| "der"`, l. 18745) | |
| Quiz d'article | 8 | `startQuizArticle`, `startDerEinUebung` | |
| Couleur de l'article | 5 | écran de découverte (`dec_t1_texte`, l. 10406) | |
| Konjunktiv II | 45 | champ `konjunktiv2` de `verbe.json`, exercices | `[Kk]onjunktiv` |
| Temps allemands | 115 | `praesens{ich,du,er_sie_es,…}`, `perfekt`, `praeteritum` | |
| Rection, verbes à cas | 79 | `rektion`, `kasusverben` | |
| zu-Infinitiv, séparables | 12 | tuile `zuinfinitiv`, `zuinf_separable` | |
| Examens Goethe / telc / DTZ | **323** | `pruefung.json`, rang 14 des thèmes, tuile `pruefung` | `[Pp]ruefung\|Goethe\|telc\|…` |
| Chapitres VHS | 149 | `vhsKapitelListe`, droit `vhsChaptersEnabled` (firestore.rules) | `vhs\|VHS` |
| Déclinaison de l'adjectif | 9 | `adjektiveDeklination` | |
| Ordre des mots | 122 | tuile `wortstellung`, `tekamolo` | |

### 1.c Général mais écrit en dur pour l'allemand : à généraliser

| Mécanisme | Lignes | Où | Ce qu'il faut |
|---|---:|---|---|
| **Niveaux CECR** en tableaux littéraux | 12 | `loadAdjektiveJson` l. 18417, `loadRedewendungenJson`, `loadAdverbienJson`, l. 23041, 24350, 26400… | `LANGUE.niveaux` (`N5…N1`) |
| Constantes de niveaux | 38 | `LEVELS` (l. 21402), `NIVEAUX_VOCAB` (l. 33283), `NIVEAUX_CECR` (l. 33414) | une seule source |
| Suffixe de niveau dans les id de thème | 1 | `/_(a1\|a2\|b1\|b2\|c1)$/i` (l. 18738) | dérivé de `niveaux` |
| **Forme de carte** | 18 | `flashcardMode === '…'` : 17 modes, dont 21 branches dans `loadFlashcard()` (l. 27699, **623 lignes**) | un mode `fiche` générique |
| **Rangs de tuple** dans `loadFlashcard` | 50 | `card[0]` … `card[16]` | accès par nom |
| Rangs de tuple, tout le fichier | 125 | `w[N]`, `word[N]`, `card[N]`, `e[N]`, `c[N]` | |
| Une colonne par langue d'interface | 38 | `traduction_en/_tr/_uk/_fa` posées une à une dans chaque chargeur | `gloses.{fr,en}` |
| Voix | 5 + 4 | `findGermanVoice()` = `pickVoice(LANGUE_ENSEIGNEE.code)` ; `LANGUE_TAG` sans `ja` (l. 28760) | ajouter `ja: "ja-JP"` |
| Lecture | 15 | `direAllemand()` (l. 31137, 191 lignes) | renommer, alias gardé |
| **Empreinte audio** | 7 | `empreinteAudio(texte)` = `sha1Hex(texte).slice(0,16)`, **sans langue** (l. 30614) | espace de noms par langue |
| Sens de la carte | 17 | `frontIsFrench`, libellé « FR⇄DE » | « connue ⇄ apprise » |
| Direction anglaise | 32 + 9 | `dir === 'en'`, `withGermanProgress` | devient la capacité `module_anglais` |
| **Clé de progression = position** | 5 | `CLES_STABLES` ne couvre que `verben` (l. 21309). Les autres listes rangent la progression **sous l'indice** | id stable obligatoire pour les fiches |
| Fréquence | 42 | `chargerFrequence()` : rang **par chaîne** (`e.m`) | par id |
| Nom d'un mot | 4 | `motDeLaCarte()` : `w[0]` ou `w.infinitif` ou `w.mot` | `fiche.id` |

**Les rangs diffèrent d'un chargeur à l'autre** :

| Chargeur | Forme | Rang du niveau | Rang `pruefung` |
|---|---|---|---|
| `loadThemesJson` (mots de thème) | tuple de 19 | aucun : le niveau est sur le thème | 14 |
| `loadAdjektiveJson` | tuple de 17 | 3 | 9 |
| `loadAdverbienJson`, `loadRedewendungenJson` | tuple de 21 | 8 | 13 |
| `loadFunktionswoerterJson` | tuple de 20 | 8 | 12 |
| `loadEnglishModuleJson` | tuple de 9 | 7 | — |
| `loadVerbeJson` | **objet** nommé | `niveau` | `pruefung` |

On le vérifie en lisant les chargeurs, l. 18349 à 18800. Les verbes sont déjà des objets : ce sont eux qui annoncent le format fiche.

### 1.4 Le mécanisme des capacités

**Le constat.** Le seul tri qui existe aujourd'hui passe par le CSS : `.orb-en{display:none}` et `body[data-learning-dir="en"] .orb-de{display:none}` (l. 1157). Le fork espagnol a empilé **36 sélecteurs** `.orb-opt[onclick*=…]{display:none !important}`. Les deux méthodes partagent le même défaut : on cache par défaut ce qu'on connaît, donc **ce qu'on ne connaît pas encore s'affiche**. C'est exactement ainsi que les examens, l'audio et le quiz der/die/das ont traversé le fork.

**La proposition** inverse la règle : rien ne s'affiche si la langue ne le demande pas.

1. Un registre `capacites.json` liste les capacités (27 proposées, dont 19 pour l'allemand, 10 pour l'espagnol, 12 pour le japonais). La table `LANGUES.<code>.capacites` dit lesquelles une langue déclare. Elle vit **dans `index.html`** : c'est du comportement, pas de la donnée.
2. Chaque porte déclare sa capacité :
   - une tuile porte `data-capacite="cas"` ;
   - une option de `orbPanelData()` porte `cap:"cas"` ou hérite de sa tuile ;
   - un jeu de `exercices.json` porte `"cap"` ;
   - un thème porte `"cap"` quand il dépend d'une capacité, par exemple `kasusverben`.
3. Au démarrage, `appliquerCapacites()` **retire du DOM** les portes non déclarées. Le CSS ne suffit pas : une porte retirée ne peut plus être atteinte par un `onclick` voisin. Les goulots refusent aussi ces portes : `startExerciseSet`, la séance du jour (`ACTIONS_DE_LA_SEANCE`), la révision (`getDueItems`) et `showScreen()`. Un appel à une section non déclarée renvoie à l'accueil et laisse une trace dans le journal.
4. Le vérificateur (`tests/verifier.py`) **échoue** dans trois cas :
   - une tuile `.orb`, une option ou un jeu sans capacité, hors des portes « moteur » listées (`seance`, `monvocab`) ;
   - une capacité absente du registre ;
   - une langue qui déclare une capacité dont aucun fournisseur n'existe, par exemple `conjugaison` sans moteur de flexion.

**Pourquoi une nouveauté allemande ne peut plus traverser en silence.** Prenons une tuile ajoutée en v720 pour l'allemand :
- sans `data-capacite`, le vérificateur échoue, avant tout push ;
- avec `data-capacite="cas"`, elle n'apparaît qu'en allemand, puisque `ja` ne déclare pas `cas` ;
- avec une capacité nouvelle, par exemple `pronoms_relatifs`, le registre doit l'accueillir et **aucune autre langue ne la déclare par défaut**.

Le seul moyen de la faire apparaître en japonais est d'écrire `pronoms_relatifs` dans la liste japonaise : c'est un acte explicite, relu. Le défaut se renverse : un oubli cache, il n'expose plus.

**Ce que la mesure dit aujourd'hui** (`verifier_capacites.py`) : 31 tuiles, dont 2 « moteur », donc **29 à annoter**, et **93 options** de panneau, aucune annotée. Avec les attributions proposées, l'allemand garde ses 29 tuiles, l'espagnol en verrait 9 et le japonais 6 de l'accueil actuel, plus les siennes (kana, kanji).

**Taille des chantiers de la section 1** (nombre d'endroits touchés, mesuré par l'inventaire) :

| Chantier | Endroits | Risque pour l'allemand |
|---|---:|---|
| Capacités : tuiles et options | 29 + 93 annotations, 1 fonction, 1 contrôle | Nul si `de` déclare tout |
| Capacités : goulots | ~6 fonctions (`startExerciseSet`, séance, révision, `showScreen`, quiz, mosaïque) | Faible |
| Niveaux | 12 tableaux + 38 usages de constantes + 1 regex | Faible : valeurs identiques |
| Voix et lecture | 15 appels à `direAllemand` (alias) + `LANGUE_TAG` | Nul |
| Empreinte audio | 1 fonction (`empreinteAudio`) | Nul si `de` garde l'empreinte nue |
| Forme de carte | nouveau mode `fiche`, sans toucher les 125 accès par rang | Nul : chemin parallèle |
| Fréquence par id | `chargerFrequence`, `motDeLaCarte` | Faible |

---

## 2. Le modèle de données japonais

### 2.1 Pourquoi un format nouveau plutôt que des tuples

Une entrée japonaise ne tient pas dans un tuple sans 30 rangs ou davantage. Elle contient :
- trois écritures ;
- un découpage furigana, qui est une liste de segments ;
- des gloses à deux niveaux (affichée et autres) dans deux langues ;
- un statut et une source par champ ;
- des liens vers les kanji.

La convention des rangs a déjà produit des écarts : le niveau est au rang 3, 7 ou 8 selon le type, ou absent (§1.c). Et le motif « une colonne `traduction_xx` par langue » (38 lignes) se multiplierait.

Les verbes allemands sont **déjà** des objets nommés (`loadVerbeJson`). Le format **fiche** en est la suite logique.

### 2.2 Le schéma

Le schéma est commenté dans `schema-fiche.json` (JSON Schema). En résumé :

```jsonc
{
  "sources": { "tanos": {"nom":…, "licence":"CC BY", "fichier":…}, … },  // déclarées une fois par fichier
  "entree": {
    "id": "jmdict:1358280",        // STABLE : c'est la clé de progression (voir 2.5)
    "type": "mot",                 // mot | kanji | kana | phrase
    "niveau": "N5",                // pris dans LANGUE.niveaux
    "ecritures": {                 // chaque feuille = {v, src, statut}
      "kanji":  {"v":"食べる","src":"tanos","statut":"brouillon"},
      "kana":   {"v":"たべる", …},
      "romaji": {"v":"taberu","src":"calcul", …}   // calculé, jamais saisi
    },
    "furigana": {"v":[["食","た"],["べる",null]], "src":"calcul"},   // segments [texte, lecture|null]
    "classe":   {"v":"v1","src":"jmdict"},         // code JMdict : c'est ce que demande la conjugaison
    "flexion":  {"moteur":"conjugaison","classe_cle":"classe"},       // les formes NE SONT PAS stockées
    "gloses": {
      "fr": {"affichee": {"v":…, "src":…, "statut":…}, "autres":[…], "pistes":[…]},
      "en": {"affichee": {"v":"to eat","src":"tanos"}, "autres":[]}
    },
    "kanji": ["食"],               // lien mot → kanji (le lien inverse est calculé)
    "phrases": [],                 // ids de phrases (Tatoeba), chacune avec son propre statut
    "image": null                  // voir §4
  }
}
```

**Statuts de relecture**, dans l'ordre : `manquant` < `brouillon` (machine ou script) < `source` (copié tel quel d'une source de référence : KANJIDIC2, JMdict) < `relu` (relu par Jacques, francophone) < `relu_natif` (relu par un natif japonais) < `valide`.
- Le moteur peut **filtrer par statut minimal**. Par exemple, il ne montre aux testeurs une mnémotechnique qu'à partir de `relu`.
- Pour les mnémotechniques, Jacques demande un deuxième critère : on note séparément **le son** (`confiance`) et **« l'image mène au sens »** (`image_mene_au_sens`).

**Source et licence par champ.** Chaque feuille porte `src`, une clé de `sources`. La licence vient de la source, sans répétition dans chaque entrée. Les sources réelles sont listées dans le tableau suivant.

| Clé | Source | Licence |
|---|---|---|
| `tanos` | listes JLPT de Waller | CC BY |
| `jmdict` | JMdict | CC BY-SA 4.0, mise à jour régulière exigée |
| `kanjidic2` | KANJIDIC2 2025-310 | CC BY-SA 4.0 |
| `kanjivg` | KanjiVG | CC BY-SA 3.0 |
| `tatoeba` | Tatoeba | CC BY 2.0 FR |
| `wortando` | textes originaux | licence à choisir |

**Gloses : « affichée » et « autres ».** `affichee` est **un choix**, avec son propre statut. `autres` garde le reste, et `pistes` garde ce qui n'est pas une glose du mot mais peut aider à la choisir, par exemple le sens du kanji. Le moteur n'affiche que `affichee`. Les quiz à choix multiple acceptent `autres` comme réponses correctes.

**Formes fléchies : déléguées, pas stockées.**
- `conjugaison.js` (branche `japonais-conjugaison`, 19 Ko) prend `(kanji, kana, classe)` et rend 21 formes de verbe et 12 formes d'adjectif.
- Les tests passent : *« Tout passe : 284593 vérifications »* (rapport de lancement de `node tests.js`).
- Stocker les formes doublerait les données et les ferait diverger du moteur.
- Le moteur japonais fournit la capacité `conjugaison` en déclarant `flexion: Conjugaison.conjuguer`. L'allemand continuera à fournir des formes **stockées** (`praesens{…}`) : c'est un autre fournisseur de la même capacité.

`construire_exemples.py` le prouve en faisant conjuguer 食べる par le moteur : `masu` donne 食べます / たべます, et `potentiel` donne 食べられる.

### 2.3 Trois exemples réels

Ils sont générés depuis les branches par `construire_exemples.py`, sans rien taper à la main :
- `exemples/mot-mizu.json` : 水 / みず, tiré de `mots.json` l. 601 de `n5.csv` ;
- `exemples/verbe-taberu.json` : 食べる / たべる, classe `v1` tirée de `jmdict-courants.json` ;
- `exemples/kanji-mizu.json` : 水, à partir de `kanji.json` et de `mnemoniques_n5.json`.

Ce que les exemples montrent sur les données **réelles** :

| Champ | 水 (nom) | 食べる (verbe) | Kanji 水 |
|---|---|---|---|
| Glose FR affichée | **manquant** (piste : « eau », le sens du kanji) | **manquant** (pistes : manger, nourriture) | « eau » (KANJIDIC2, choisie) |
| Glose EN | « water » (Waller) | « to eat » | « water » |
| Classe | **manquant** : `jmdict-courants.json` ne couvre que les mots fléchis, et JMdict n'est pas apparié | `v1` | — |
| Furigana | `[["水","みず"]]` (calcul) | `[["食","た"],["べる",null]]` | — |
| Romaji | `mizu` (repris de `mnemoniques_n5.json`) | `taberu` | lecture retenue `sui` (on) |
| Mnémotechnique FR | — | — | « La fontaine m'arrose d'eau : je **suis** (sui) trempé. » (confiance haute, `brouillon`) |
| Lien | `kanji: ["水"]` | `kanji: ["食"]` | `mots: [jmdict:1371260, jmdict:1372190]` (calculé) |

### 2.4 Les liens entre entités

- **Mot vers kanji** : stocké (`kanji: [...]`), calculé au build à partir de l'écriture. **Aujourd'hui aucun fichier ne le porte** : `construire.py` de `kanji-mnemo` le recalcule à la volée et n'en garde qu'un compte.
- **Kanji vers mots** : un index inverse **calculé au build**, jamais tenu à la main.
- **Kanji vers composants** : la liste des `element` KanjiVG, joints par caractère à `composants.json` (80 composants, noms FR/EN). Ces noms sont **stables et cumulatifs** : un composant nommé « passant » (亻) garde ce nom dans tous les kanji suivants. Les mnémotechniques en dépendent.
- **Mot vers phrases** : par id de phrase. Chaque phrase porte son propre statut, car la qualité Tatoeba est estimée à 80 %.

### 2.5 Identifiants stables et progression

**Leçon de la v315** (`CLES_STABLES`, l. 21309). Une progression rangée sous la position d'un mot se décale dès qu'on insère un mot. Pour le japonais, **la clé de progression est `fiche.id` dès le premier jour**, et la position ne sert jamais.

**Quel id ?** Le numéro de séquence JMdict (`jmdict:1358280`), parce qu'EDRDG le garde stable d'une édition à l'autre. C'est un souvenir de la documentation JMdict : **à vérifier avant de figer**.
- La valeur actuelle vient de `jmdict_seq_tanos`, recopiée par stephenmk, **non vérifiée**.
- Repli quand aucun numéro n'existe : `ja:<kanji>|<kana>`.
- 行く a deux entrées (いく et ゆく), d'où le kana dans la clé.
- Le kanji a pour id `kanji:<caractère>`, et le kana `kana:<id de kana.json>` (par exemple `kana:h-a`).

**Rangement.** Les cartes japonaises vont sous des `themeId` propres : `ja_mots`, `ja_kanji`, `ja_kana`. `progressKey()` les préfixe déjà en `ja__ja_mots`. Aucun code allemand n'est touché.

### 2.6 Comment l'allemand pourrait migrer vers les fiches plus tard, sans rien casser

1. Un script de `tests/` convertit `verbe.json`, `themes.json`, etc. en fiches. Chaque fiche porte un champ `cle_progression: {theme, k}` **copié de ce que `cleMot(themeId, index)` rend aujourd'hui** :
   - pour les verbes, le lemme ;
   - pour les autres listes, l'**indice actuel**, figé au moment de la conversion.
2. Le moteur lit `getWordState(cle.theme, cle.k)`. La clé lue est identique octet pour octet à la clé écrite par la v709. **Aucune migration de progression n'est nécessaire.**
3. Une fois la clé figée dans la fiche, on peut insérer, retirer et réordonner librement. C'est le bénéfice de la v315, étendu à toutes les listes.
4. **Preuve exigée** dans le commit : un test node charge la progression d'un compte réel (copie locale) et vérifie que, pour 100 % des fiches, `cle_progression` retrouve exactement l'état qu'avait l'ancien chemin.
5. On convertit une catégorie à la fois, en commençant par les adverbes (petits, tuple de 21) et en finissant par les thèmes (7 000 mots).

---

## 3. Ce qui est propre au japonais

### 3.1 Furigana (ruby)

- Le rendu passe par `<ruby>食<rt>た</rt></ruby>べる`, construit à partir des segments `furigana`. La balise ruby est native dans les navigateurs modernes : connaissance générale, non testée ici sur les appareils des testeurs.
- Le réglage apprenant a trois positions : *toujours* / *seulement les kanji pas encore acquis* / *jamais*. La position du milieu **relie les deux répétitions espacées** (§3.6) : un kanji passé `mastered` dans `ja_kanji` perd son furigana partout.
- Tout nœud japonais porte **`lang="ja"`**. Sans cela, l'unification Han peut faire afficher des glyphes chinois sur certains systèmes (connaissance générale). L'attribut est posé par la fonction de rendu, jamais à la main.
- Le CSS de `<ruby>` va dans le `<style>` du `<body>` (règle v256), pas dans le `<head>`.

### 3.2 Polices : mesure

Mesure faite par `mesurer_polices.py` sur le serveur Google Fonts, le 6 octobre 2026 :

| Ce qui est chargé | Fichiers | Poids |
|---|---:|---:|
| Noto Sans JP 400, **police entière** | 124 tranches | **2 867 Ko** |
| Tranches déclenchées par kana + 79 kanji N5 | 25 | **296 Ko** |
| Sous-ensemble `&text=` des mêmes 257 caractères | 1 | **56 Ko** |
| *Pour comparer : polices latines actuelles de l'app* | 3 | 314 Ko |

**Proposition.**
1. **Pile système d'abord** : `"Hiragino Kaku Gothic ProN", "Hiragino Sans", "Yu Gothic", "Noto Sans CJK JP", "Noto Sans JP", sans-serif`. iOS, macOS, Android et Windows livrent une police japonaise. C'est une connaissance générale, **à vérifier sur les appareils des testeurs**.
2. Noto Sans JP via Google Fonts, en **`unicode-range`** : le navigateur ne tire que les tranches utiles. Il faut compter environ 300 Ko au niveau N5, ce qui équivaut aux polices latines actuelles. La police **ne passe jamais par le service worker**, comme aujourd'hui.
3. Le sous-ensemble `&text=` est écarté pour le contenu, qui change avec les données. Il reste possible pour le seul logo ou titre.
4. Le **tracé** des kanji ne dépend d'aucune police : il vient des SVG KanjiVG, ce qui garantit l'ordre et le sens des traits.

### 3.3 Saisie

- **Ne jamais exiger de taper du japonais** avant N4. Les exercices de production se font par tuiles à choisir (kana, kanji, mots), qui existent déjà sous la forme de `unplaceChunk`.
- La saisie libre reste en français ou en anglais, dans le sens japonais → langue connue.
- Plus tard, on pourra proposer une conversion romaji → kana intégrée, une petite table, pour qui n'a pas d'IME. L'IME du téléphone reste accepté, mais **la réponse ne doit jamais dépendre de lui** : la composition IME déclenche des événements `input` intermédiaires (connaissance générale). Il faut valider sur `compositionend` ou sur un bouton.
- Le moteur porte une capacité `saisie_libre` par langue : l'allemand la déclare, le japonais non au départ.

### 3.4 Voix `ja-JP` et audio pré-généré

- **Synthèse du navigateur.** Ajouter `ja: "ja-JP"` à `LANGUE_TAG`. Il n'y est pas aujourd'hui : `grep -n "const LANGUE_TAG" index.html` le montre. Aujourd'hui `pickVoice("ja")` rendrait `null` sans erreur, exactement le piège décrit en commentaire pour l'ukrainien. La disponibilité d'une voix japonaise varie selon les appareils : il faut un message clair quand elle manque.
- **La collision déjà vécue.** `empreinteAudio(texte) = sha1Hex(texte).slice(0,16)`, sans marque de langue. Le fork espagnol a dû poser `AUDIO_BASE = ""` pour qu'une voix allemande ne lise pas ses cartes. La proposition :
  1. **Chaque langue a sa base audio** (`LANGUES.ja.audio = ".../ja/"`).
  2. **L'empreinte inclut la langue, sauf pour l'allemand** : `code === "de" ? sha1(texte) : sha1(code + "\n" + texte)`. Les 25 298 mp3 allemands gardent leur nom. C'est la même règle que le préfixe de progression : le vide de l'allemand est sa compatibilité.
  3. **En japonais, on hache la lecture et pas l'écriture** : `sha1("ja\n" + kana)`. 今日 se lit きょう ou こんにち : l'écriture ne dit pas la prononciation, la lecture si.
- Le script de génération, l'équivalent japonais d'`audio/generer.py`, applique **la même fonction**. Un test croisé sur 100 empreintes, Python contre JS, va dans `tests/`, comme `sha1Hex` l'est déjà avec `audio/manifest.py`.

### 3.5 Le kanji, objet d'étude à part entière

Un nouveau type de carte, `kanji`, dans le mode `fiche`. Il montre :
- le **tracé animé** depuis le SVG KanjiVG, nommé par point de code sur 5 chiffres hexadécimaux comme pour les kana (`03042.svg`) ;
- les **composants**, avec leurs noms stables ;
- le **sens retenu** et la **lecture retenue** ;
- la **mnémotechnique de la langue d'interface**. Elle ne se traduit pas : `mnemo.fr` et `mnemo.en` sont deux textes indépendants, chacun relu à part. En interface anglaise sans `mnemo.en` relu, rien ne s'affiche ; le moteur ne retombe pas sur le texte français.

Les SVG des kanji ne sont **pas encore extraits** : seuls les 177 SVG de kana le sont (branche `japonais-kana`).

### 3.6 Répétition espacée sur deux objets liés

- Deux listes distinctes, `ja_kanji` et `ja_mots`, ont chacune leur état `{mastered, due, reviews, srsDailyStreak}`, avec le même moteur que l'allemand (`SRS_DAILY_LADDER_DAYS = [1,3,7,16,35]`, l. 31915).
- **Pas de double comptage.** Réussir 食べる ne fait pas avancer l'échéance de 食. Cela pose seulement une **exposition** (`st.vu`, déjà utilisé l. 34891). Un kanji n'avance que sur sa propre carte.
- **Ordre d'introduction.**
  - Un mot devient « neuf disponible » quand tous ses kanji ont été **vus**, pas forcément maîtrisés.
  - Avant cela, il peut apparaître en kana seul.
  - C'est la seule dépendance. Elle se calcule à partir de `fiche.kanji`, sans stockage supplémentaire.
- **Retour du mot vers le kanji.** Un échec sur 食べる dont la cause est la lecture de 食 (exercice « lis ce mot ») replanifie aussi 食 à court terme. Le moteur le sait parce que l'exercice déclare ce qu'il teste (`teste: "lecture_kanji"`).

---

## 4. La place du visuel

*Ni les exercices ni l'interaction ne sont conçus ici. Cette section réserve seulement leur place.*

- **Où vit une scène.**
  - L'image et ses points appartiennent à **Wortando**, pas à une langue. Ils vont donc sous `ASSETS_BASE` : `illustrations/<id>.json` et `illustrations/<id>.webp`.
  - Le fichier contient `{id, image, licence, auteur, points:[{p, x, y, r}]}`. `x`, `y` et `r` sont en **% de l'image**.
  - Chaque langue fournit ensuite son **correspondant** dans ses données : `illustrations.json`, qui associe `{<id scène>: {<p>: <fiche.id>}}`. Exemple : `"cuisine-01": {"p3": "jmdict:1371260"}`.
  - Une même image sert toutes les langues. Les mots sont posés par l'app, jamais dessinés dans l'image.
  - ⚠️ **Ne pas l'appeler `scenes/`.** Ce dossier existe déjà pour les **situations vidéo** (`scenes/01-ankunft-berlin.json`, plans HeyGen), un autre objet.
- **Une réponse dans une scène = une révision du même mot.**
  - Aujourd'hui la notation passe par `scheduleReview()`, `reviewGood()`, `reviewAgain()` et `markMastered()`. Ces fonctions lisent `currentCards[currentFlashcard]` : elles sont liées à l'écran des cartes.
  - L'étape 7 du §6 en extrait **`noterRevision(themeId, cle, verdict, origine)`**, appelée par les cartes et par les scènes.
  - L'état écrit est le même (`setWordState`), donc la même échéance. `origine: "scene"` sert seulement aux statistiques.
- **Qui la déclare.** La capacité `scenes_illustrees`, au registre. Une langue sans correspondant pour une scène ne la voit pas.
- **L'image d'un mot sur sa carte.** Le champ `fiche.image` vaut `{scene, p}` : on recadre la scène autour du point, sans fichier de plus. Il peut aussi valoir `{fichier}` sous `ASSETS_BASE/illustrations/mots/`. Il ne contient jamais de texte.

---

## 5. Options d'architecture

| | **A. Un seul `index.html`, une adresse, langue choisie à l'ouverture** | **B. Le même fichier à deux adresses (`/` et `/ja/`), langue déduite de l'adresse** ✅ | **C. Un générateur qui produit `ja/index.html`** |
|---|---|---|---|
| Risque pour l'allemand | Moyen : le sélecteur touche l'accueil allemand, et une erreur de choix de langue frappe tout le monde | **Faible** : `/` reste `de` par défaut ; `/ja/` n'existe que s'il est publié | Faible au départ, **élevé ensuite** : c'est `fork.py`, avec 84 versions de retard en 3 semaines |
| Maintenance | Un fichier | Un fichier + une **copie identique** vérifiée par empreinte (`tests/verifier.py`) | Deux fichiers qui divergent, des correctifs par motif qui « cessent de mordre » |
| « Une app par langue » (décision prise) | ✗ Une seule icône, un seul manifeste | ✓ Un manifeste par dossier (`ja/manifest.json`, nom « Wortando Japonais ») | ✓ |
| « Sans build » (CLAUDE.md) | ✓ | ✓ La copie est une copie, pas un build | ✗ Étape de génération |
| Firebase Auth | Même projet, même session | Même projet. Même origine, donc **session partagée** : on se connecte une fois pour les deux (persistance par origine) | Au choix |
| Progression Firestore | `users/{uid}` partagé, préfixe `ja__` | Même compte. Progression japonaise dans **`users/{uid}/cours/ja`** (décision 2) | Au choix |
| `localStorage` | Partagé, clés `deutschAI_*` mélangées | **Partagé par l'origine** : chaque langue doit avoir son préfixe de clés (`deutschAI_` pour `de`, inchangé ; `wortandoJa_` pour `ja`), comme l'a fait l'espagnol | Idem B |
| Service worker | Un seul, inchangé | **Un par dossier** : `ja/firebase-messaging-sw.js` (copie), portée `/ja/`. La portée la plus précise l'emporte, et `estLaPage()` du worker racine ne touche déjà pas `/ja/`. ⚠️ Voir le défaut du cache ci-dessous | Idem B |
| Notifications | Une seule inscription | Une inscription push par worker, donc deux jetons FCM par appareil si les deux apps sont installées | Idem B |
| Capacitor (iPhone/Android) | Une app native | **Une app native par langue**, chacune pointe vers son adresse. ⚠️ Non vérifié : la configuration Capacitor n'est pas dans ce dépôt | Idem B |

**Recommandation : B.** C'est la seule option qui tient à la fois les décisions déjà prises (une app par langue, un moteur partagé) et la règle « sans build ». Elle laisse aussi l'adresse allemande exactement où elle est. Elle coûte une copie de fichier et un contrôle d'identité, qui est beaucoup moins cher qu'un générateur.

**Défaut réel trouvé en préparant B, déjà présent aujourd'hui.** Le `activate` de `firebase-messaging-sw.js` (l. 122-123) et celui de `espanol/sw.js` (l. 35-36) suppriment **tous** les caches de l'origine dont le nom n'est pas le leur. CacheStorage est partagé par l'origine : c'est la spécification des service workers, connaissance générale.
- L'activation du worker espagnol (`wortando-es-v2`) efface donc le cache de démarrage allemand (`wortando-page-v1`), et l'inverse.
- Il n'y a aucune perte de données, seulement la perte du démarrage instantané (v257) jusqu'au rechargement suivant.
- Avec `/ja/`, le défaut toucherait trois apps.
- Correctif à prévoir : ne supprimer que les caches **de son propre préfixe** (`wortando-page-`).

---

## 6. Plan de migration en petites étapes

Chaque étape est livrable seule sur l'app allemande, **sans rien changer pour les testeurs** :
- les données passent d'abord, toutes seules ;
- chaque étape a un seul goulot ;
- le vérificateur est mis à jour dans le même commit ;
- `python tests/verifier.py` et `node tests/syntaxe.js` sont lancés avant chaque push, comme toujours.

| # | Ce qui change | Comment prouver que l'allemand n'a pas bougé | Ce que le japonais y gagne | Taille |
|---|---|---|---|---|
| 1 | `LANGUE_ENSEIGNEE.capacites` (liste complète pour `de`), `data-capacite` sur 29 tuiles, `appliquerCapacites()`, règle du vérificateur | Script node qui liste les `data-orbid` visibles dans le DOM pour `de` et pour `en` : identiques avant et après. `verifier_capacites.py` passe de « 29 sans capacité » à 0 | Le tri inversé existe | ~45 lignes |
| 2 | `cap:` sur les 93 options et sur les jeux d'`exercices.json` (données poussées d'abord) ; goulots `startExerciseSet`, séance, révision, `showScreen` | Même liste d'options par panneau avant et après, même nombre de cartes dans la séance du jour sur une progression figée | Aucune porte allemande ne peut fuir | ~120 lignes |
| 3 | `LANGUE.niveaux` remplace 12 tableaux littéraux et 3 constantes ; la regex de suffixe en dérive | Le vérificateur refuse `["A1", "A2"` hors de la table ; comptes par niveau identiques (`getLevelMasteryStats`) | N5…N1 sans toucher le code | ~55 lignes |
| 4 | `direLangueEnseignee()` (alias `direAllemand`), `LANGUE_TAG.ja`, empreinte audio par langue (vide pour `de`) | Test : 100 empreintes allemandes identiques à `audio/manifest.py` ; journal audio sans hausse de replis | Audio japonais sans collision possible | ~25 lignes |
| 5 | Préfixe des clés `localStorage` par langue (`deutschAI_` pour `de`, inchangé) ; `activate` du worker limité à son préfixe | `grep -c '"deutschAI_' index.html` inchangé (47) ; clés lues identiques | Cohabitation sur la même origine | ~50 lignes |
| 6 | Mode de carte **`fiche`** et chargeur `chargerFiches(fichier)`, dormants : aucune donnée allemande ne l'utilise | Rien ne l'appelle pour `de` ; un test node rend les 3 exemples de `exemples/` | Les cartes japonaises existent | ~300 lignes neuves |
| 7 | `noterRevision(themeId, cle, verdict, origine)` extrait de `scheduleReview` / `reviewGood` / `reviewAgain` / `markMastered` | Mêmes états écrits : test node qui rejoue 1 000 notations sur l'ancien et le nouveau chemin | Les scènes et les kanji notent par le même goulot | ~60 lignes touchées |
| 8 | Progression par langue dans Firestore : `de` reste sur `users/{uid}.progressJson` ; une autre langue écrit `users/{uid}/cours/<code>` ; `firestore.rules` étendu | `de` n'emprunte pas le nouveau chemin ; règles testées sur l'émulateur ou en lecture seule | Pas de limite de taille partagée | ~40 lignes + règles |
| 9 | Table `LANGUES = {de:{…}, ja:{…}}`, `LANGUE_ENSEIGNEE` choisie par l'adresse (`/ja/` donne `ja`, sinon `de`) | `/` sans changement : même version, même liste de tuiles (test de l'étape 1) | Le japonais démarre, vide | ~30 lignes |
| 10 | Furigana (ruby, `lang="ja"`), police à la demande, cartes kana et kanji : tout derrière les capacités japonaises | `de` ne déclare aucune de ces capacités : vérifié par le contrôle de l'étape 1 | L'app japonaise elle-même | ~1 500 à 2 500 lignes neuves |
| 11 | Publication de `ja/` : copie d'`index.html` et du worker, `ja/manifest.json`, données sous `japonais/donnees/` ; empreinte d'identité ajoutée au vérificateur | `/` intact ; `/ja/` derrière code d'invitation | Testeurs japonais | ~10 lignes + copies |

**Total.** Environ **300 lignes touchées dans le code allemand existant** (étapes 1 à 5, 7 à 9), et **2 000 à 3 000 lignes neuves** derrière les capacités japonaises. C'est une estimation fondée sur les comptes du §1, pas sur une implémentation.

⚠️ **Rappel de production.** Tant que l'app lit ses données sur `main` (`urlDonnees`), il ne faut pas pousser sur `main` des données japonaises qu'un `index.html` ne demande pas encore. Les données passent d'abord, mais **seules**, et sans effet sur l'allemand.

---

## 7. Le cas espagnol

L'espagnol entrerait comme troisième entrée de `LANGUES`, sans `fork.py` :
- `code: "es"`, adresse `/espanol/` (déjà utilisée), `donnees: "espanol/datos/"` ;
- clés `localStorage` `wortandoEs_`, **gardées** pour que les testeurs espagnols ne perdent pas leur progression ;
- `capacites` : les 10 du registre.

Ses données (`datos/*.json`) ont **déjà la forme allemande** : clés `praesens`, `rektion` (qui contient le type de conjugaison), jeux nommés `konjunktiv2Exercises` (qui contiennent le subjonctif). Elles passent donc par les chargeurs actuels, puis migrent vers les fiches comme l'allemand (§2.6).

Deux différences doivent devenir des **réglages de langue** et non des correctifs :
- **pas de comptes** : `auth: false`, avec la porte à code et les empreintes SHA-256 ;
- **interface fr/en seulement**, comme pour le japonais.

Les 36 masquages CSS deviennent l'absence de 9 capacités. `articuloPlural()` et `tablaConjugacionES()` deviennent les fournisseurs espagnols des capacités `genre_nominal` et `conjugaison`. Le fork a **84 versions de retard** (base v625, amont v709) : la rejoindre par le moteur coûte moins qu'une nouvelle passe de `fork.py`.

---

## 8. Risques et questions ouvertes

| # | Risque ou question | Ce qu'on en sait | Proposition |
|---|---|---|---|
| 1 | **Gloses françaises absentes** (0 / 8 293) | JMdict était bloqué (403) au moment de la construction ; la couverture française de JMdict n'est pas mesurée ici | Décision 3 ; relancer `construire.py` quand JMdict est joignable, puis **mesurer** la couverture FR avant de choisir |
| 2 | Identifiant `jmdict_seq` non vérifié | Recopié par stephenmk | Vérifier contre JMdict avant la première progression japonaise : un id qui change efface la progression |
| 3 | **Taille du document Firestore** | Toute la progression est une chaîne (`progressJson`) dans `users/{uid}`. Firestore limite un document à 1 Mio : limite documentée par Google, de mémoire, non revérifiée. Un état de mot fait environ 90 octets en JSON ; allemand (7 704 entrées) + japonais (8 293 mots + 2 211 kanji) touchés en entier dépasseraient la limite | Étape 8 : un document par langue |
| 4 | Comptes de mots JLPT décalés | Écarts −59 / −44 / +109 / −98 / +340 par niveau, non résolus (RAPPORT.md de `japonais-donnees`) | À trancher avant d'afficher « 100 % du N5 » |
| 5 | 79 kanji N5 et non 103 | `kanji.json` et `mnemoniques_n5.json` comptent 79 ; l'ancien niveau 4 de KANJIDIC en compte 102 | Quelle liste fait foi ? |
| 6 | Validations de Jacques non enregistrées | Les 79 entrées sont toutes « brouillon à relire » | Le champ `statut` par mnémotechnique (§2.2) ; reporter les 16 validations |
| 7 | Phrases | `phrases.json` jamais produit ; qualité estimée à 80 % | Statut par phrase obligatoire ; rien d'affiché sous `relu` |
| 8 | Voix japonaise absente sur certains appareils | Non mesuré | Message explicite ; audio pré-généré si la décision est prise |
| 9 | Licence des textes originaux | Mnémotechniques kana et kanji : « à choisir par le propriétaire » | À choisir avant publication sur un dépôt public |
| 10 | Données payantes sur un dépôt public | Le code espagnol se contredit : `urlDonnees` dit « dépôt PRIVÉ », un autre bloc dit « adresse publique ». `espanol/datos/` est bien dans ce dépôt public | Décider où vivent les données d'une app vendue |
| 11 | Environnement de test | `CLAUDE.md` dit qu'il n'y en a pas ; le tableau de bord admin cite `wortando-staging.netlify.app`, branche `staging` (`admin_deploy_desc`, l. 10860) | Si ce staging existe, c'est là que l'étape 9 se prouve |
| 12 | Capacitor | La configuration native n'est pas dans ce dépôt. Seul `window.Capacitor` est testé (l. 338) | Vérifier comment l'app native charge la page avant de fixer l'adresse `/ja/` |

**Non vérifié dans ce travail.**
- Le rendu réel : aucun navigateur n'a été lancé, et rien n'a été modifié dans `index.html`.
- La couverture française de JMdict.
- Les polices système japonaises présentes sur les téléphones des testeurs.
- La stabilité des numéros JMdict.
- La limite exacte de Firestore.
- La configuration Capacitor.
- `node tests/retours.js`, prescrit en début de session : la clé de service (`C:/Users/jacqu/.wortando/admin.json`) n'existe pas dans ce conteneur.
- Note : dans ce checkout, `index.html` est en **LF** et non en CRLF.

---

## Fichiers de ce dossier

| Fichier | Rôle |
|---|---|
| `CONCEPTION.md` | Ce document |
| `inventaire.py` | §1 : comptes par motif dans `index.html` (lecture seule) |
| `capacites.json` | §1.4 : registre des capacités, déclarations par langue, attribution des 29 tuiles (proposition) |
| `verifier_capacites.py` | §1.4 : prototype du contrôle, mesure des portes à annoter |
| `schema-fiche.json` | §2 : schéma JSON commenté d'une fiche |
| `construire_exemples.py` | §2.3 : fabrique `exemples/*.json` depuis les branches, et fait conjuguer 食べる |
| `exemples/` | 3 fiches réelles : 水 (nom), 食べる (verbe), 水 (kanji) |
| `mesurer_polices.py` | §3.2 : poids réseau de Noto Sans JP |
