# L'espagnol enseigné en arabe : consignes de traduction (15 oct. 2026)

Wortando enseigne l'espagnol à des francophones, des anglophones et des lusophones.
On l'ouvre maintenant aux **arabophones** : l'interface est en arabe, l'apprenant lit
des mots et des phrases **espagnols**, et tout ce qui les explique doit être en arabe.
Ce dossier contient les textes à traduire (`sources/`) ; tu écris tes traductions
dans `lots/`. Tu ne touches à **aucun autre fichier**.

## Interdits (absolus)

- **Pas de `git commit`, pas de `git push`**, aucune commande git qui écrit
  (`add`, `stash`, `reset`, `checkout`, `switch`…). `git diff` / `git status` en lecture : oui.
- **Pas d'API payante**, pas d'appel réseau, pas de service de traduction : c'est toi qui traduis.
- **Pas d'autre agent** : ne lance aucun sous-agent ni aucune session.
- **Jamais de script Python par heredoc dans Git Bash** (il mange les antislashs).
  Si tu as besoin d'un script, écris-le avec l'outil Write dans ton dossier scratchpad, puis lance-le.
- Ne modifie **aucun** fichier de `espanol/datos/`, ni `index.html`, ni `visuel/`, ni `tests/` :
  tu écris uniquement dans `espanol/ar/lots/`. La pose est faite ensuite par une autre session.
- Ne lance pas `python espanol/ar/poser.py pose` sans `--essai`.

## L'arabe voulu

- **Arabe standard moderne** (فصحى), simple et clair, celui d'un manuel pour adultes ;
  pas de dialecte. Tutoiement au masculin générique, comme le reste de l'app en arabe
  (« اكتب », « اختر », « تعلّم »).
- Ponctuation arabe : « ، » « ؛ » « ؟ ». Guillemets « … » autour des mots espagnols cités.
- **Les mots et phrases espagnols restent en espagnol, en lettres latines**, exactement
  comme dans la source (avec leurs accents) : `«estar»`, `<b>al lado de</b>`. On ne les
  translittère jamais.
- **Les balises HTML et les marques restent intactes** : `<b>`, `<em>`, `<strong>`, `<br>`,
  `{n}`, `{x}`, `%s`, emojis, `⚠️`, ` · `. Même nombre de balises que la source, bien fermées.
- **Flèches** : la source écrit « A → B ». En arabe (de droite à gauche), écris « A ← B »
  (la flèche suit le sens de lecture), comme dans le lot `ejercicios-01.txt` déjà fait.
- Un texte qui n'est fait que d'espagnol (« (vivir) », « (comer — yo) », « Con tener — tener ganas »)
  garde sa partie espagnole ; seule la partie française/anglaise se traduit.
- Pronoms de personne dans les indices : « (hablar — yo) » reste tel quel (c'est de l'espagnol).
  Les mentions françaises du type « présent, je » deviennent « المضارع، أنا ».

## Écrire CONTRE l'arabe (pas traduire le français mot à mot)

La source française explique l'espagnol à un francophone (« comme en français… »,
« contrairement au français… »). Le portugais (`pt`) l'a déjà réécrit pour un lusophone :
lis-le, il montre l'esprit voulu. **Toi, réécris pour un arabophone** : retire les
comparaisons avec le français, et ajoute la comparaison avec l'arabe quand elle aide
vraiment. Repères utiles :

- **Genre** : l'arabe a aussi masculin/féminin, mais les genres ne coïncident pas
  (el sol / الشمس مؤنثة ; la leche / الحليب مذكر). L'article el/la n'a pas d'équivalent
  séparé : « ال » ne marque pas le genre. L'indéfini un/una n'existe pas comme mot en arabe (tanwīn).
- **ser / estar** : l'arabe n'a pas de verbe « être » au présent (جملة اسمية) ; les deux
  verbes espagnols sont donc une vraie nouveauté. Explique par le sens (identité,
  nature, origine → ser ; lieu, état passager → estar).
- **Conjugaison** : comme en arabe, la terminaison suffit et le pronom sujet tombe
  souvent (hablo = أتكلّم). Bon appui.
- **Passés** : l'arabe a un seul passé (الماضي) ; l'espagnol distingue pretérito
  (action terminée) et imperfecto (décor, habitude, ce qui durait — كان يفعل). « كان + المضارع »
  est le meilleur équivalent de l'imparfait.
- **Subjonctif** : rapprocher de « أن + المضارع المنصوب » (quiero que vengas ≈ أريد أن تأتي).
- **gustar** : l'arabe fait exactement comme l'espagnol ! « me gusta el chocolate » =
  « تعجبني الشوكولاتة » : c'est la chose aimée qui est le sujet, et le verbe s'accorde avec
  elle (me gustan los libros = تعجبني الكتب). Le mot à mot de la source (« le chocolat ME PLAÎT »)
  devient en arabe « الشوكولاتة تُعجبني ».
- **Faux amis** (`falsosAmigosExercises`) : ils sont pensés pour un francophone ou un
  anglophone. Beaucoup d'arabophones connaissent le français ou l'anglais : présente le
  piège comme « une ressemblance trompeuse avec le français ou l'anglais », et donne
  toujours le sens réel en arabe.
- **Prononciation** : l'arabe n'a que trois voyelles (a, i, u) → piège e/i et o/u ;
  pas de p (≠ b) ni de v ; le r espagnol ≈ ر ; j (et g devant e, i) ≈ خ ; ll et y ≈ ي ;
  ñ ≈ ني ; ch ≈ تش ; c/z d'Espagne ≈ ث, d'Amérique latine ≈ س ; d doux entre voyelles ≈ ذ ;
  h toujours muet (≠ ه). Les transcriptions entre « » de la source se refont avec ces
  équivalents (ou se retirent si elles n'aident pas un arabophone).
- Les **traductions de phrases** espagnoles se font de l'espagnol (le français n'est
  qu'une aide) ; garde le registre et les prénoms.

## Formats

### Exercices (`sources/ejercicios-a.txt`, `-b.txt`) → `lots/ejercicios-NN.txt`

Chaque ligne source : `jeu¦idx|question|question_en|translation|hint|explanation` (français).
Écris dans tes lots, 100 lignes par fichier au plus, en commençant par `#fichier ejercicios` :

    jeu|idx|debut|translation_ar|hint_ar|explanation_ar|[question_ar]

- `jeu|idx` : le `jeu¦idx` de la source avec `|` au lieu de `¦`.
- `debut` : les **20 premiers caractères** de la question espagnole, recopiés tels quels.
- `hint_ar` : `=` si l'indice n'est fait que d'espagnol (« (vivir) », « (comer — yo) ») ;
  sinon sa traduction arabe.
- `question_ar` (7e colonne) : **seulement si `question_en` n'est pas vide ET diffère de
  `question`** (la question a été formulée dans la langue de l'usager) ; sinon pas de 7e colonne.
- Aucun `|` à l'intérieur d'un texte (remplace-le par « ، » ou « / »).
- Contrôle après chaque lot : `python espanol/ar/poser.py pose --essai espanol/ar/lots/<ton-lot>.txt`
  doit répondre « N entrees verifiees (essai, rien n'est ecrit) ». Sinon corrige.

### Corpus (`sources/temas.txt`) → `lots/temas-07.txt`

Source : `num|mot|genre niveau theme|traduction fr|exemple es|exemple fr`. Lot :

    #fichier temas
    num|mot|traduction_ar|exemple_ar

`traduction_ar` : le mot arabe (avec l'article « ال » si naturel, comme les lots
`temas-0*.txt` déjà faits — regarde-les pour le style). `exemple_ar` : la phrase espagnole traduite.
Contrôle : `pose --essai` comme ci-dessus.

### Autres textes (`sources/<nom>.json`) → `lots/<nom>.ar.json`

Chaque source est une liste `{"id", "fr", "en", "pt", …}`. Rends un objet JSON
`{ "<id>": "<texte arabe>", … }` avec **tous** les id de la source, dans le même ordre.
- `mots-outils` : la valeur est une liste de trois textes `[traduction, exemple, catégorie]`
  (l'exemple traduit la phrase `exemple_es`).
- `prononciation` : une liste de deux textes `[court, explication]` ; écris-les contre
  l'arabe (voir plus haut), avec les mots espagnols des exemples.
- `scenes` : le fichier est gros ; tu peux le rendre en plusieurs morceaux
  `lots/scenes-01.ar.json`, `scenes-02.ar.json`… (ensemble, tous les id). Les « n » sont des
  notes courtes affichées après une question sur une image ; `question` et `phrase` sont
  là pour le contexte, ne les traduis pas.
- `grammaire` : les fiches de grammaire. **Réécris-les pour un arabophone** (voir les repères) ;
  ce sont les textes les plus importants. Les ids `textes|…` sont des titres et des
  paragraphes d'écran ; les `fiches/…/titre`, `resume`, `regle`, `tableau`, `exemples` sont
  dans les fiches. Une cellule de tableau faite d'espagnol (« hablo · como · vivo ») se recopie telle quelle.
- `i18n` : l'interface de l'app quand on apprend l'espagnol. Là où la source dit
  « en espagnol ou en français » / « em espanhol ou em português », écris « بالإسبانية أو بالعربية ».
- Écris le JSON avec l'outil Write (UTF-8, pas d'échappement \u). Vérifie qu'il se lit :
  `python -c "import json;json.load(open('espanol/ar/lots/<nom>.ar.json',encoding='utf-8'))"`.

## Fin

Quand ta part est faite, écris un compte rendu court dans
`espanol/ar/lots/RAPPORT-<ta-part>.md` : ce qui est fait, ce dont tu doutes (liste
précise d'id), et toute source qui te semblait fautive.
