# L'espagnol en arabe : ce qu'un arabophone doit relire en priorité

Dressé le 1er nov. 2026. Le texte arabe de l'espagnol est complet depuis la v808 (15 oct.) ; le 1er nov.
ont été ajoutés les 61 mots du cours de Jacques, les notices des 22 peintres, la prononciation des nombres et
les sous-titres des épisodes. Traduit par des modèles, relu par d'autres modèles, **jamais par un
arabophone**. Historique et doutes déjà notés : `espanol/AVANCEMENT-AR.md`, `espanol/ar/lots/RAPPORT-*.md`.

L'arabe est un **arabe standard moderne**. À dire au relecteur : il ne s'agit pas de dialectaliser, mais de
repérer ce qui sonne traduit, faux ou trop littéraire pour un apprenant adulte.

## 1. Les 17 fiches de grammaire et la prononciation (le plus important)

- `espanol/datos/grammaire.json`, clé `ar` (259 textes) et `textes.ar` (43) : **réécrites pour un
  arabophone**. Vérifier les comparaisons avec l'arabe : l'ordre « se lo doy » (déjà corrigé une fois le
  15 oct.), le genre (l'arabe a aussi deux genres, mais pas les mêmes mots), ser/estar face à la phrase
  nominale arabe sans verbe « être », le subjuntivo (gardé en espagnol : « صيغة subjuntivo »).
- `espanol/datos/prononciation.json` (dérivé de `tests/prononciation_es.py`, dictionnaire `AR`) : les
  transcriptions en lettres arabes (« خامون » pour jamón, « ثيوذاذ » pour ciudad) et les cinq voyelles
  expliquées avec trois.

## 2. Nouveau le 1er nov. : jamais relu par personne

- **La prononciation des nombres** (`tests/reperes_suite.py`, `PRONONCIATION_NOMBRES_ES_AR`), en lettres
  arabes : « θِيرو » (affiché ثِيرو en Espagne, سِيرو en Amérique latine), « كواترو », « نْوِيبِه »,
  « بِيْنتِه ». Questions : la kasra + ي suffit-elle à faire lire « e » et non « i » ? Faut-il marquer la
  syllabe forte (l'arabe n'a pas de capitales ; rien ne la marque aujourd'hui) ?
- **Les 61 mots du cours de Jacques** : `espanol/ajouts/cours-jacques-pt-ar.json`, colonnes 4 et 5. Les
  exemples à « il/elle » sont rendus par « ـه/ـها » (« شعره/شعرها ») : lourd, à alléger si le relecteur
  préfère un seul genre.
- **Les notices des 22 peintres** de la mosaïque espagnole : `espanol/ar/lots/peintres-ar.json`. Les noms
  propres (ثيرثيديا pour Cercedilla, فالباراييسو, أغواسكالينتس) et les titres d'œuvres.
- **Les sous-titres arabes des 4 épisodes** (`scenes/traductions-es-pt-ar.json`, clé `ar`) : les jeux de
  mots, où le mot espagnol reste en lettres latines dans la phrase arabe (« «carro»؟ أنت مكسيكي! »). Vérifier
  sur la vidéo gravée que l'ordre des mots est juste (`python video/controler_rtl.py`).

Corrigé le 1er nov. : au verso d'une carte de verbe, les phrases d'exemple du pretérito, de l'imperfecto,
du perfecto, du futur, du conditionnel et du subjonctif s'affichaient en ANGLAIS (le chargeur oubliait les
champs `exemple_<temps>_ar`, pourtant remplis depuis le 15 oct.). À relire maintenant qu'elles se voient.

## 3. Les exercices

`espanol/datos/ejercicios.json`, champs `*_ar`. Priorité : `serEstarExercises`, `porParaExercises`,
`gustarExercises`, `falsosAmigosExercises` (l'indice arabe dit franchement « le mot qui ressemble au français
ou à l'anglais » : c'est honnête, mais un arabophone qui ne parle ni l'un ni l'autre n'y voit pas de piège ;
une série propre serait mieux), `acentosExercises`.
- Les flèches « → / ← » : appliquées par `espanol/ar/fleches.py` (règle dans `AVANCEMENT-AR.md`) ; signaler
  toute ligne qui se lit à l'envers.

## 4. L'interface

`index.html`, `I18N_ESPAGNOL.ar` (142 clés). Corrigé le 1er nov. : l'abonnement annonçait les 7 700 mots et
les examens de l'allemand ; il dit « 3700 كلمة من المستوى A1 إلى B2 » et « لهجة إسبانيا أو أمريكا
اللاتينية ».

## 5. Connu, pas à relire

- Pas de dictionnaire espagnol-arabe (WikDict n'a pas la paire) ; pas de voix de visite guidée en arabe.
- (Corrigé le 1er nov. : la première colonne des tableaux de grammaire, en français jusque-là, est
  traduite — `espanol/ar/colonne_fiches.py` ; à relire avec les fiches.)
- Corrigé le 1er nov. : « الكتابة » (Écrire) et « تركيب الجملة » (Construire la phrase) montraient la phrase
  ANGLAISE à traduire ; ils montrent maintenant la phrase arabe.
