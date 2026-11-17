# Rapport — fiches de grammaire en espagnol (15 nov. 2026)

## Fait

- `interface-es/lots/grammaire.es.json` : **237 textes sur 237**, dans l'ordre de la source.
- Contrôle `textes.py` : **0 faute, 2 avis**, tous deux des mots allemands hors `<em>` :
  « du » dans le tableau des pronoms (`personal_table`) et « des » dans `relativ_gen_warning` («des»/«der»).
- Tutoiement partout, y compris dans les textes d'examen (`pruefung_info_*`), que la source française vouvoie.
- Les deux tableaux HTML (`personal_table`, `demonstrativ_text`) sont repris de la source par remplacement
  (fém. → fem., neutre → neutro, pluriel → plural, politesse → cortesía, 1<sup>re</sup> → 1<sup>a</sup>…), pas retapés.
- Glossaire : M'ENTRAÎNER → PRACTICAR, VOCABULAIRE → VOCABULARIO, FLASHCARDS → TARJETAS (comme le bloc espagnol
  déjà dans `index.html` : « Vocabulario: tarjetas »), « Structure » → « Orden de las palabras » (le
  `wortstellung_title` espagnol déjà en place).

## Comparaisons RÉÉCRITES (17) — le français retiré, l'espagnol à la place

| Clé | Source | Mis à la place |
|---|---|---|
| `adverbien_artweise` | pas de « -ment » | pas de «-mente» |
| `adverbien_ort` | le français dit « ici » dans les deux cas | l'espagnol sépare «¿dónde?» / «¿adónde?» dans la question, mais dit «aquí» dans la réponse |
| `demonstrativ_title` | celui-ci, celui-là | este, ese, aquel (trois degrés, comme dieser / der / jener) |
| `indefinit_text` | man = le « on » français ; « tous connaissent » | man = le «se» impersonal (ou «uno») ; jeder comme «cada uno», là où l'espagnol dirait «todos conocen» |
| `indefinit_title` | on, quelqu'un, personne | se, alguien, nadie |
| `indefinit_piege` (2e paragraphe) | « on » = « nous » → wir | le «se» espagnol n'est *man* que s'il est impersonnel («se dice» = *Man sagt*) ; le «se» de «él se lava» est *sich* |
| `personal_intro` | le français fait pareil (je / me / moi) | l'espagnol ne décline que ses pronoms (él / lo / le) : lo, la ≈ Akkusativ, le ≈ Dativ |
| `personal_piege` | vous de politesse ; ihr = vous (tutoiement pluriel) ; « il pleut » avec sujet vide | Sie = usted / ustedes ; ihr = ustedes entre amis, et la phrase « l'Amérique latine dit ustedes pour tous, l'allemand sépare ihr et Sie » ; l'espagnol dit «llueve», «hace frío» sans sujet, l'allemand exige *es* |
| `possessiv_base` | son/sa/ses, votre/vos, leur/leurs | les six «su/sus» départagés : de él, de ella, de ustedes (tutoyés), de ellos/ellas, de usted/ustedes (politesse) |
| `reflexiv_text` (dernier paragraphe) | réfléchis en allemand mais pas en français : sich bewerben, sich verlieben | ces deux-là SONT pronominaux en espagnol (postularse, enamorarse) : remplacés par *sich bedanken* (agradecer) et *sich ausruhen* (descansar), plus le sens inverse («quedarse», «llamarse» = bleiben, heißen) |
| `relativ_intro` | « qui », « que », « à qui » | l'espagnol dit presque toujours «que» (parfois «quien», «a quien»), l'allemand décline |
| `relativ_gen_intro` | « dont » | «cuyo», «cuya» |
| `redewendungen_piege` | « j'ai le cafard » ≠ *ich habe die Kakerlake* | «me estás tomando el pelo» ≠ *du nimmst mir das Haar* |
| `zahlen_bruch` | contrairement au français, pas de préposition | a diferencia del español («en 1990») |
| `zahlen_umgekehrt` | difficulté n° 1 pour un francophone ; « un-et-vingt » | pour un hispanohablante ; «uno-y-veinte», à l'inverse de «treinta y uno» |
| `verbentemps_perfekt_title` | le passé composé | el pasado de la conversación (« pretérito perfecto » aurait fait croire à *he jugado*) |
| `verbentemps_praeteritum_title` | le prétérit | el pasado de los relatos (« pretérito » = *jugué* en espagnol, soit plutôt le Perfekt parlé) |

## Comparaisons AJOUTÉES (17) — la source n'en avait pas, un piège d'hispanophone s'y logeait

- `kasus_box_akkusativ` : «Veo al hombre — la «a» personal no se traduce».
- `art_table_indef_note` : pas de «unos, unas».
- `indefinit_text` : une seule négation (*Das ändert nichts* / «no cambia nada»).
- `possessiv_agree` : «mi» ne change pas avec le genre, *mein / meine* si.
- `praep_contract_intro` : comme «al» et «del», avec bien plus de prépositions.
- `praep_wechsel_tip` : l'astuce reformulée en «¿adónde?» (Akkusativ) / «¿dónde?» (Dativ).
- `relativ_gen_genre` : à l'inverse de «cuyo», qui s'accorde avec le possédé.
- `verbentemps_konjunktiv2` : couvre le condicional et l'imperfecto de subjuntivo.
- `verbentemps_perfekt` : un seul auxiliaire en espagnol («haber») ; là où l'Amérique latine dit «jugué», l'allemand parlé dit le Perfekt. Exemples traduits au pretérito (Jugué. Fui.).
- `verbentemps_praesens` : le pronom sujet ne s'omet pas («juego» = «ich spiele»).
- `wortstellung_frage` : l'espagnol marque la question par l'intonation et «¿», l'allemand par la place du verbe.
- `wortstellung_nicht` : à l'inverse du «no» espagnol, placé devant le verbe.
- `zahlen_grund` : *eins / ein* comme «uno / un».
- `zahlen_ordnung` : *am dritten Mai* — l'allemand dit l'ordinal, l'espagnol «el 3 de mayo».
- `zuinf_never_movement` : «Voy a nadar» précisé (ce n'est pas un futur).
- `zuinf_wahrnehmung` : l'espagnol fait la même construction (Veo a los niños jugar).
- `redewendungen_pourquoi` : *keine Ahnung* («ni idea»).

## Doutes

- `redewendungen_piege` : *du nimmst mir das Haar* est un faux allemand voulu (comme *ich habe die Kakerlake* dans la source), placé dans `<em>`. À faire relire.
- `possessiv_agree` / `possessiv_agree_title` : la source dit « jamais de la personne qui possède » ; j'ai retiré ce « jamais », car pour un hispanophone le possesseur compte bel et bien en allemand (*sein* / *ihr* pour «su»). Titre : « La terminación sigue a lo poseído, no al poseedor ».
- `praep_contract_*` (am, ans, aufs, beim…) : traduits depuis le français seul, la phrase allemande n'est pas dans la source. `aufs` : « Espero con ganas el fin de semana » (sich freuen auf) ; `beim` : « Estoy en el médico » (familier mais général).
- `verbentemps_praeteritum` : « Fui al cine. Jugué fútbol. » — «jugar fútbol» (Mexique, Colombie) plutôt que «jugar al fútbol».
- `pruefung_info_unterschied` : « contestadora » (répondeur) est mexicain ; « contrato de alquiler » plutôt que « de renta ».
- `personal_intro` : « El alemán va más lejos, pero es regular » remplace « l'allemand est plus régulier [que le français] », qui n'avait plus d'objet.
- Ordinaux en exposant : 1<sup>a</sup>, 3<sup>a</sup> persona, 1<sup>o</sup>… (les balises `<sup>` devaient rester) ; dans le texte courant, « 2.ª posición ».
- `possessiv_base` : *unser* rendu « nuestro/nuestros » (la source dit « notre/nos »).
- `partikel_*` : équivalents de ton, forcément approximatifs (« ¡Dilo y ya! », « ¡Ni se te ocurra ir allá! »).

## Source fautive ou discutable

- `verbentemps_praeteritum` (fr) : « J'allais au cinéma. Je jouais au football. » — l'imparfait pour *ging / spielte* ; l'anglais et le sens premier donnent un fait accompli. Espagnol : pretérito.
- `reflexiv_text` (fr) : rien de faux, mais la liste dépend de la langue de l'apprenant — à refaire pour chaque langue d'interface (voir ci-dessus).
- `adverbien_ort` (fr) : « Allez tout droit » pour *Gehen Sie* ; rendu par usted (« Siga derecho »).
- `adverbien_zeit`, `adverbien_gradmenge` (fr) : verbe au singulier (« Situe », « Dose ») pour une liste de mots ; l'espagnol garde le singulier pour Zeit et met le pluriel pour Grad/Menge (« Miden… Nunca van solos »), comme la suite de la phrase source.

## À trancher

- « TARJETAS » pour FLASHCARDS (aligné sur le bloc espagnol existant) — à confirmer si l'interface garde ailleurs « flashcards ».
- « contestadora » / « contestador automático » ; « jugar fútbol » / « jugar al fútbol ».
