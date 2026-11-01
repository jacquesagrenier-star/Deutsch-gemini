# Rapport — grammaire, prononciation, conjugaison, exercices (allemand, 1er nov. 2026)

## Fait

| part | fichier(s) | textes | contrôle |
|---|---|---|---|
| grammaire | `grammaire.de.json` | 302 / 302 | 0 faute, 19 avis (balises ajoutées, titres courts) — le premier passage donnait 19 « fautes » sur des cellules d'espagnol seul ; `poser_autres.py` a été corrigé entre-temps (pas par moi), le contrôle relancé passe |
| prononciation | `prononciation.de.json` | 20 / 20 | 0 faute, 0 avis |
| conjugaison | `conjugaison-01.de.json` | 224 / 224 | 0 faute, 2 avis (titres courts) |
| exercices | `ejercicios-01.txt` … `ejercicios-14.txt` | 1 343 / 1 343 (13 × 100 + 43) | chaque lot : « N entrees verifiees (essai, rien n'est ecrit) » ; `poser.py etat` reste à 0 / 1343 (rien n'a été posé) |

Rien d'autre n'a été touché. (`git status` montre `index.html`, `.claude/launch.json` et `a1-voyage-0?.de.json` modifiés ou ajoutés : ce n'est pas moi.)

### Cellules d'espagnol seul (recopiées telles quelles)

19 cellules de `grammaire` sont du pur espagnol et sont recopiées sans changement, comme le lot arabe : `fiches/futuro-condicional/tableau/7/1`, `fiches/imperativo/tableau/2/1`, `/8/1`, `fiches/subjuntivo/tableau/0/1` à `/3/1`, `fiches/hay-preguntas/tableau/0/1`, `fiches/numeros-hora/tableau/0/1`, `/1/1`, `/4/1`, `/7/1`, `fiches/demostrativos-posesivos/resume`, `fiches/conectores/tableau/1/1` à `/6/1`. Le premier `controle` les comptait comme « identique au francais » ; le script a été corrigé pendant mon travail (pas par moi) et le contrôle final passe à 0 faute.

## Méthode pour les exercices

- Jeux à explications formulaires (exercises, praeteritum, perfekt, konjunktiv2, infinitiv, adverbienNuance, futuro, condicional, imperativo, verbosConPreposicion ×37, subjuntivoImperfecto, oracionesSi, compuestos, pasiva) : l'explication allemande est construite par gabarit depuis le français (un gabarit allemand écrit à la main par phrase-type, les « … » espagnols et les listes de formes recopiés). Les gabarits sont dans mon scratchpad (`build.py`, `TEMPLATES`) ; les phrases allemandes qu'ils produisent sont donc **les mêmes pour toutes les lignes d'un même type** — une relecture par type suffit.
- Tous les autres (serEstar, porPara, falsosAmigos, gustar, acentos, perifrasis, numeros, demostrativos, preposiciones, preposicionesViaje, 13 verbosConPreposicion) : explication écrite ligne à ligne.
- Les 1 343 `translation_de` sont écrites une à une depuis l'espagnol.
- `hint_de` : `=` pour les indices espagnols ; les indices français fixes d'un jeu traduits une fois ; gustar : chaque indice « mot à mot » réécrit avec „gefallen“ ; infinitiv : « (présent, je) » → « (Presente, ich) » ; `(importar — te … : 3e personne)` → « 3. Person ».
- `question_de` : infinitiv (70) « — Wie lautet der Infinitiv? », adverbienNuance (56) « Welche Familie für „hoy“? ».
- `optionsDe` : `infinitivExercises` a des `options` (infinitifs espagnols) mais **pas d'`optionsEn`** → `poser.py` ne copiera pas `optionsDe` pour ce jeu. Vérifier que l'app retombe sur `options` ; sinon le copier à la main (70 entrées, neutres).

## Doutes (id précis)

- `exercises|9` (bailamos), `|30` (remamos), `|41` (presenciamos), `infinitivExercises|35` (remamos), `|53` (conversamos) : la forme espagnole est un **présent** (c'est ce que demande l'explication) mais le français traduit au **passé composé** (« nous avons dansé »). J'ai traduit au présent. Source à corriger.
- `exercises|27, 28, 45, 46, 47, 48, 51, 59` : l'explication dit « il/elle : deja », la phrase est un **impératif** (« Laisse les clés… », « Choisis celui que tu préfères » — `te guste` l'impose). J'ai suivi le français (impératif allemand), l'explication allemande dit toujours « er/sie ». Source incohérente.
- `exercises|9` et `praeteritumExercises|13` : « ustedes » rendu par „Sie“ (vouvoiement pluriel).
- `fiches/presente/titre` : « Le présent » → „Das Presente“ (nom espagnol du temps, comme les consignes) ; de même „Der Imperativo“, „Der Subjuntivo“, „Futuro und Condicional“. Si le PC préfère „Das Präsens“, c'est un seul mot à changer.
- `fiches/concordancia/titre` : „Die Angleichung“ (plutôt que „Kongruenz“, trop savant).
- `fiches/numeros-hora/tableau/8/1` et `exemples/1/1` : j'ai ajouté le piège „y media = halb + heure suivante“ (las tres y media = halb vier), absent de la source, parce qu'il est propre aux germanophones.
- `textes|redewendungen_piege` : l'exemple « il pleut des cordes » remplacé par „Es gießt wie aus Kübeln“ ≠ *llueve como de cubos* (forme inventée pour montrer le faux calque).
- `gustarExercises|34` : la source cite le portugais (« as costas ») — retiré.
- `falsosAmigosExercises` : pièges réorientés. Gardés tels quels (valent pour l'allemand) : 1, 2, 5, 6, 10, 11, 13, 15, 16, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 37, 38, 39, 40, 43, 45, 48, 49, 51. Présentés comme ressemblance trompeuse avec **l'anglais** : 0 (embarrassed), 3/4 (exit, success), 7/8 (carpet), 9 (large), 14 (quit), 36 (actual), 41 (fabric), 42 (lecture), 44 (introduce), 46 (excited), 47 (success). Propres à l'allemand : 28 (firma ≠ Firma), 29/30 (mantel ≠ Mantel), 24 (rubio ≠ rubinrot), 35 (preservativos = Präservativ, le piège est l'anglais), 50 (bizarro ≠ bizarr), 12 (ropa ≠ Robe), 34 (sueldo ≈ Sold). `|18` (sufrir/subir) et `|52`-like n'ont pas d'équivalent allemand : expliqués sans piège.
- `condicionalExercises|46` « J'imaginais que tu serais à la maison » → „Ich dachte mir, du wärst zu Hause.“ (Konjunktiv II allemand, Condicional espagnol : la correspondance est voulue).
- `pasivaExercises|14` « Se buscan camareros » → „Kellner gesucht.“ (affiche) ; `|32` « Se dan clases de guitarra » → „Gitarrenunterricht wird erteilt.“ — formulations d'annonce, pas de phrases complètes.
- `preposicionesExercises|8` : j'ai ajouté « — nicht „mit“ » (en tren ≠ mit dem Zug) ; `|14` : « kein Genitiv-s ».

## Sources fautives ou douteuses

- `textes|verbentemps_perfekt` (fr) explique par l'imparfait français ; l'anglais dit « English gives no help » — j'ai suivi la logique anglaise (le Präteritum ne départage pas).
- `fiches/genero/*`, `fiches/pasados/*`, `fiches/subjuntivo/attention`, `fiches/pronombres/attention`, `fiches/concordancia/*`, `fiches/pronominales/resume` : écrits pour un francophone ; réécrits entièrement (voir la liste des comparaisons).
- `fiches/hay-preguntas/tableau/0/1` (fr) « un, una, unos, dos, mucho, ningún… » et `/1/1` : la première est du pur espagnol (recopiée), la seconde finit par « un prénom » → „ein Name“.
- `conjugaison /niveaux/A2/5/a`, `/B1/7/a`, `/B2/2/a` : « Comme en français… » réécrits contre l'allemand.
- `conjugaison /niveaux/B1/9/l/5/1` « il m'a dit qu'il avait fini » → „er sagte mir, er sei fertig gewesen“ (Konjunktiv I du discours indirect, naturel en allemand).

## Comparaisons avec l'allemand écrites (pour la relecture)

### grammaire.de.json
- `textes|adverbien_artweise` : „Im Deutschen dient das Adjektiv unverändert als Adverb („schnell“); das Spanische hängt -mente an die weibliche Form“.
- `textes|adverbien_frage` : „dónde … adónde — wie „wo“ und „wohin““.
- `textes|adverbien_gradmenge` : „Das deutsche „sehr“ passt auf beides; das Spanische trennt.“
- `textes|adverbien_grundfolge` : „Nach así que oder por eso bleibt es bei Subjekt – Verb, anders als nach „deshalb“ oder „also“ im Deutschen (deshalb bleiben wir).“
- `textes|adverbien_haeufigkeit` : „die doppelte Verneinung ist hier die Regel … und sie heißt nicht „nicht nie““.
- `textes|adverbien_ort` : „wo das Deutsche mit „hier“ und „dort“ auskommt“.
- `textes|adverbien_tekamolo_link` : „anders als im Deutschen, wo „ich bin immer zu spät gekommen“ genau das tut“ (trennt Hilfsverb et Partizip).
- `textes|adverbien_verbindung` : „das Deutsche sagt „auch“ und „auch nicht“; das Spanische hat dafür ein eigenes Wort.“
- `textes|redewendungen_pourquoi` : „man hat Hunger, wie im Deutschen; aber tengo frío, wo das Deutsche „mir ist kalt“ sagt.“
- `textes|verbentemps_konjunktiv2` : „Wo das Deutsche beim Indikativ bleibt („dass du kommst“), wechselt das Spanische die Form.“
- `textes|verbentemps_perfekt` : „Hier hilft das Deutsche nicht: „Ich sprach“ ist hablé oder hablaba … Ein „früher … immer“ zeigt auf hablaba.“
- `textes|verbentemps_praeteritum` : „Ob du im Deutschen „ich sprach“ oder „ich habe gesprochen“ sagst, spielt keine Rolle“.
- `fiches/presente/regle` : „anders als im Deutschen, wo „ich“ Pflicht ist“.
- `fiches/presente/exemples/1/1` : „wörtlich „ich habe zwanzig Jahre““ ; `/5/1` et `attention` : usted „wie él konjugiert — 3. Person Singular“, „Singular, nicht Plural wie das deutsche „Sie““.
- `fiches/ser-estar/regle` : „Das Deutsche hat nur „sein“ — hier entscheidet der Sinn.“
- `fiches/genero/resume`, `regle`, `attention` : „el sol / die Sonne, la luna / der Mond. Nur zwei Geschlechter, kein Neutrum, und die Artikel werden nie dekliniert“ ; „Fallen für Deutschsprachige: el sol, el coche, el libro …, la luna, la mesa, la leche“.
- `fiches/concordancia/resume`, `regle` : „la casa es blanca, las casas son blancas. Das Deutsche sagt „das Haus ist weiß“ ohne Endung; das Spanische nie.“
- `fiches/pasados/resume`, `regle`, `attention` : „Eine Wahl, die das Deutsche nicht kennt“ ; „Präteritum und Perfekt helfen hier nicht: „Ich aß“ kann beides sein“ ; „„Früher … immer“ zeigt auf comía“ ; „immer mit haber, nie mit „sein“: he ido = ich bin gegangen“.
- `fiches/futuro-condicional/regle` : „Kein Hilfsverb wie „werden“ oder „würde“ — eine einzige Form.“ ; `exemples/2/1` „wie „könntest““ ; `/5/1` „wie „er wird wohl““.
- `fiches/subjuntivo/resume`, `regle`, `exemples/1/1`, `attention` : „Viel häufiger als der deutsche Konjunktiv“ ; „Wo das Deutsche beim Indikativ bleibt („Ich will, dass du kommst“) … Quiero que vengas“ ; „im Deutschen bleibt „kommt““ ; „Nach cuando … bleibt das Deutsche im Indikativ („wenn ich ankomme“)“ ; „Der deutsche Konjunktiv („käme“, „würde“) ist kein Wegweiser“.
- `fiches/pronombres/regle`, `attention` : „Das Deutsche stellt es dahinter („ich sehe ihn“)“ ; „direkt (lo, la — wie der Akkusativ) und indirekt (le — wie der Dativ)“.
- `fiches/hay-preguntas/exemples/2/1` : „wie „es gibt“, auch im Plural“.
- `fiches/pronominales/resume`, `regle`, `exemples/4/1`, `attention` : „Wie „sich waschen“ — aber nicht immer dieselben Verben“ ; „kein „mich“ oder „mir““ ; „der Artikel, wie im Deutschen“ ; „im Spanischen reflexiv, im Deutschen nicht: ducharse, quedarse, casarse con, llamarse“.
- `fiches/numeros-hora/regle`, `tableau/8/1`, `exemples/1/1`, `/3/1` : „die Zehner zuerst, nicht wie „einunddreißig““ ; „y media … las tres y media = halb vier“ ; „la una y media ist halb zwei, nicht halb eins“ ; „nicht „neunzehnhundert““.
- `fiches/demostrativos-posesivos/attention` : „anders als im Deutschen verrät es weder den Besitzer noch dessen Geschlecht“.
- `fiches/preposiciones/regle`, `attention` : „Kein Fall dahinter — nach a, en, de bleibt das Nomen unverändert“ ; „die Frage „wo oder wohin?“ kennst du, nur beantwortet sie hier die Präposition, nicht der Fall“.
- `fiches/conectores/regle` : „Die Wortstellung bleibt dabei immer gleich — kein Verb wandert ans Ende.“

### prononciation.de.json (tout est écrit contre l'allemand)
- voyelles : kurz und voll, „wie in „Mama“, „Bett“, „Kind“, „Sonne“, „Mutter“, nur nie gedehnt … keine langen Vokale wie in „Liebe“ oder „Boot“, kein stummes e und kein Umlaut“.
- u : „nie „ü““ ; e-final : „voll wie in „Bett“ … nie das schwache e von „bitte““ ; sans-nasale : „wie in „Mann“, nicht wie in „Bahn““ ; diphtongues : „seis „se-is“, Europa „e-u-ropa“ — nie „ai“ oder „oi“ wie in „Seite““, „ie ist i + e (siete), nicht das lange i von „Liebe““.
- c-z, c-z.es, c-z.latam : „Nie „ts“ wie in „Zeit“ (oder „Zapfen“)“ ; c-qu : „Nie „kw“ wie in „Quelle“ oder „Qualität““.
- j : „der deutsche ach-Laut von „Bach“, „lachen“, „Buch“: jamón „chamón“ … Nie wie ein deutsches j!“ ; g-gu : „hartes g wie in „Garten““ ; ch : „„tsch“ wie in „Tschüss“ oder „Matsch“ … Nie der deutsche ach- oder ich-Laut“ ; ll-y : „kräftiges deutsches „j“ wie in „ja“ … Nie ein „l“ wie in „alle““ ; n-tilde : „„nj“ wie in „Cognac“ oder „Kastanie“, España „Espanja““ ; h : „Nie hauchen wie in „Haus““.
- r-rr : „Nie das deutsche Rachen-r — und nie verschluckt wie in „Vater““ ; b-v : „Nie das deutsche „w“ von „Wein“ — und nie „f“ wie in „Vater““ ; d : „Am Ende wird es nicht zu „t“ wie im deutschen „Rad““ ; s : „scharf wie in „Haus“ oder „Wasser“ … Das summende s von „Rose“ oder „Hase“ gibt es nicht … sp, st am Wortanfang bleiben „s-p“, „s-t“: España, estación — nie „schp“, „scht““.
- accent : „nicht wie im Deutschen auf die erste Silbe ziehen — es heißt „ca-FÉ“, nicht „CA-fe““.

### conjugaison-01.de.json
- `/A2/0/a` : „Ob du im Deutschen „ich sprach“ oder „ich habe gesprochen“ sagst, ist egal — hier zählt, dass es vorbei ist.“
- `/A2/3/a` : „Ein „früher … immer“ im Deutschen zeigt fast immer auf diese Zeit.“
- `/A2/5/a` : „Das Deutsche trennt das nicht — „es regnete“ und „ich ging hinaus“ stehen beide im Präteritum.“
- `/A2/6/a` : „immer mit haber, nie mit ser — auch dort, wo das Deutsche „sein“ nimmt: „Ella ha llegado“ = sie ist angekommen.“
- `/A2/7/a` : „dort, wo das Deutsche oft einfach das Präsens nimmt („morgen fahre ich“)“.
- `/A2/8/a` : „wie das deutsche „Sie“, aber in der Einzahl“.
- `/A2/9/a` : „das deutsche „gerade“ oder „dabei sein““.
- `/B1/0/a` : „eine einzige Form, ohne Hilfsverb wie „werden““ ; `/B1/2/a` : „das deutsche „würde“ oder der Konjunktiv II („hätte“, „könnte“), in einer einzigen Form“ ; `/B1/3/a` : „genau wie „könnten Sie““.
- `/B1/4/a`, `/B1/6/a`, `/B1/7/a` : „dort, wo das Deutsche einfach „dass du kommst“ sagt“ ; „Im Deutschen bleibt „dass du gehst“ im Indikativ“ ; „Wo das Deutsche „wenn du ankommst“ im Indikativ sagt, nimmt das Spanische den Subjuntivo“.
- `/B1/9/a` : „das deutsche Plusquamperfekt, aber immer mit haber („el tren había salido“ = der Zug war abgefahren)“.
- `/B2/1/a` : „hier trifft er sich mit dem deutschen Konjunktiv II („als wüsste er“)“ ; `/B2/2/a` : „Wie im Deutschen „hätte ich …, würde ich …“ … anders als das umgangssprachliche „wenn ich würde““.
- `/B2/3/a`, `/B2/4/a` : „beide Male mit haber, auch wo das Deutsche „wäre“ sagt (habría venido = ich wäre gekommen)“.
- `/B2/5/a` : „wie das deutsche „wohl““ ; `/B2/6/a` : „ähnlich dem deutschen „man““, „wie das deutsche Zustandspassiv“ ; `/B2/7/a` : „Kein Konjunktiv I wie im deutschen „er sei müde“: Das Spanische verschiebt die Zeit, nicht den Modus.“

### Exercices (gabarits et lignes)
- konjunktiv2 (gabarits « souhait », « émotion », « cuando », « conseil ») : „Das Deutsche bleibt hier beim Indikativ („ich hoffe, dass du kommst“)“ ; „auch wenn das Deutsche „ich freue mich, dass du da bist“ im Indikativ sagt“ ; „Das Deutsche sagt „wenn du ankommst“ im Indikativ; das Spanische nimmt nie das Futuro“ ; „Das Deutsche sagt hier oft „zu + Infinitiv““.
- condicional (gabarits) : „wie „er sagte, er würde …““ ; „wie „könntest du“ oder „ich hätte gern““.
- oracionesSi (gabarit irréel présent) : „wie im Deutschen: hätte ich …, würde ich reisen“.
- imperativo (gabarit nosotros) : „„Lasst uns …““.
- gustar : tous les indices et explications réécrits avec „gefallen“ („wie bei „gefallen“ und „schmecken““ ; `|4` „ich bin das Objekt, wie „mir“ im Deutschen“ ; `|31` „genau wie im Deutschen“ ; `|38` „wie im Deutschen“).
- serEstar `|42` : „nicht „verlegen“ (englisch embarrassed)“.
- numeros `|2`, `|3`, `|13`, `|20`, `|25`, `|26`, `|45` : „anders als „einunddreißig““, „nicht „fünfundachtzig“ herum“, „anders als „eintausend““, „nicht „neunzehnhundert…““, „la una y media ist halb zwei, nicht halb eins“, „„acht weniger Viertel““, „„zwei weniger fünfundzwanzig““.
- preposiciones `|8` „nicht „mit““, `|12`/`|42` „das Deutsche sagt „aus Holz“ / „aus Baumwolle““, `|14` „kein Genitiv-s“, `|15` „das Deutsche fragt „wem““, `|16` „braucht im Spanischen ein de“, `|23` „das Deutsche sagt „an““, `|24` „ohne Entsprechung im Deutschen“, `|9` „„zu Fuß““.
- verbosConPreposicion `|1` „Im Spanischen träumt man MIT, nicht „von““, `|2` „Hier passt die deutsche Präposition“, `|6` „nicht ohne Präposition wie im Deutschen“, `|7` „Man verliebt sich VON jemandem, nicht „in““, `|26` „anders als „Fußball spielen“ ohne Präposition“.
- perifrasis `|4` „das deutsche „man muss““, `|8` „wie „weiter“ im Deutschen“, `|18` „ich muss nicht, ich brauche nicht“.
- demostrativos `|46` „das Deutsche sagt „deins“ nach dem Auto, das Spanische richtet sich nach coche“.
- falsosAmigos : voir la liste des pièges ci-dessus (28 Firma, 29/30 Mantel, 24 rubinrot, 35 Präservativ, 36 aktuell, 50 bizarr, 12 Robe, 34 Sold).
