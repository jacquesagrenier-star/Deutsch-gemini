# Rapport — scenes-07 (espagnol d'Amérique latine, interface de l'allemand)

## Fait

- `interface-es/lots/scenes-07.es.json` : **300 textes sur 300**, contrôle `scenes_textes.py controle` → **0 faute, 2 avis**.
- Scènes : `soins-ambulant` (60, sans `champs`), `soins-aufnahme` (62), `soins-bad` (64),
  `soins-stationszimmer` (62), `soins-uebergabe` (52 : la source s'arrête au milieu de la couche B2 des `sens` ;
  la suite — sens B2 fin, C1, SIT — est dans scenes-08).
- Par groupe : 8 `champs` (4 alt, 4 consignes), 30 titres de couche, 135 explications, 127 sens.
- Les 2 avis (« du français ? ») sont le **du allemand** cité exprès : « Entre colegas: <b>du</b> »
  (`soins-stationszimmer¦questions¦B1 | Kannst du morgen…`, `soins-uebergabe¦questions¦B2 | Das ist das Trinkprotokoll…`).
- Brouillon : `scratchpad/scenes-07_construire.py` (les 300 textes dans l'ordre de la source), `scenes-07_dump.py`.

## Harmonisation

- Cas écrits comme la source française : dativo, acusativo, genitivo ; Konjunktiv I / II, Perfekt, Präteritum gardés en allemand.
- Titres repris de scenes-01 à 04 : « Los verbos reflexivos », « Las preguntas indirectas », « El Perfekt »
  (pour « Le passé composé »), « verbos separables » (pour « verbes à particule », comme `buero¦couches¦B1`),
  « estilo indirecto » (pour « discours rapporté », comme `apotheke¦couches¦B2`).
- **« Que faites-vous ? » (couche SIT, 5 fois) → « ¿Qué haces? »** (tutoiement des consignes). Aucun précédent
  dans scenes-01 à 04 : à aligner avec les autres lots de soins (scenes-05, 06, 08).
- « Frau Lehmann » (gardé en allemand dans le français des alt et de certains sens) et « Mme Lehmann » →
  « la señora Lehmann » dans les alt et consignes, « la Sra. Lehmann » dans les sens.
- Sie → usted partout ; du entre collègues → tú.

## Explications réécrites contre l'espagnol

- `soins-aufnahme¦questions¦A2 | Wie heißen Sie?` — ajout : comme le « ¿cómo? » de l'espagnol.
- `soins-aufnahme¦questions¦A2 | Welche Medikamente nehmen Sie?` — « quels, quelles » → « qué, cuáles ».
- `soins-aufnahme¦questions¦A2 | Wo ist Ihre Versichertenkarte?` — « votre » → « su (de usted) ».
- `soins-aufnahme¦questions¦B2 | Seit wann haben Sie die Wunde am Fuß?` — « le français dit aussi "depuis quand" » →
  l'espagnol aussi met le présent (« ¿desde cuándo tiene…? »).
- `soins-aufnahme¦questions¦B2 | Tut es weh, wenn Sie mit dem Fuß auftreten?` — ajout : l'espagnol dit « cuando » pour wenn et als.
- `soins-bad¦questions¦B2 | Bevor Elif die Waschschüssel füllt…` — « là où le français met un infinitif » → l'espagnol
  aussi (« antes de llenar »).
- `soins-bad¦questions¦B2 | Seit Frau Lehmann im Krankenhaus ist…` — « le français dit aussi le présent » → l'espagnol aussi.
- `soins-stationszimmer¦questions¦A2 | Es ist halb zwei.` — « Le piège des francophones » → « La trampa para los
  hispanohablantes » (le piège est le même : « la una y media »).
- `soins-stationszimmer¦questions¦A2 | Die Übergabe beginnt…` — « la una y cuarto » ; « cuarto para las dos »
  (forme d'Amérique, pas « las dos menos cuarto »).
- `soins-stationszimmer¦questions¦B2 | Betäubungsmittel dürfen nur…` — « ne … que » → « solo se permite ».
- `soins-stationszimmer¦questions¦B2 | Gebrauchte Nadeln dürfen nicht…` — « le piège du français "ne doit pas" » →
  « "no debe" interdit en espagnol, mais "nicht müssen" non ».
- `soins-uebergabe¦questions¦B1 | Der Blutzucker war heute Morgen zu hoch.` — wäre = « estaría » (la phrase se dit avec estar).
- `soins-uebergabe¦questions¦B2 | Die Patientin, deren Wunde…` et `… | Der Herr, dessen Hüfte…` — réécrites autour de
  « cuyo » : deren / dessen suivent le possesseur, à l'inverse de « cuyo », qui s'accorde avec la chose possédée.

## Doutes

- `soins-ambulant¦questions¦SIT | Ich rufe die Pflegedienstleitung an…` : « ne jamais forcer seule » rendu
  « nunca forzar nada sola » — la question (la porte qui ne s'ouvre pas ?) n'est pas dans la source ; à relire avec elle.
- `soins-ambulant¦sens¦A2 | Die Tasche steht auf dem Stuhl.` : « El bolso » (si c'est la sacoche de soins : « el maletín »).
- `soins-ambulant¦sens¦B2 | Ihr Blutzucker ist heute Morgen…` : « Ihr » en tête de phrase lu « su » (de Mme Kowalski),
  comme le français ; « su » couvre de toute façon les deux lectures.
- `soins-stationszimmer¦sens¦B1 | Frau Hoffmann ist im Gespräch.` : « está atendiendo a alguien » (ni « en entretien » ni « en réunion »).
- `soins-stationszimmer¦sens¦B1 | Jonas stellt die Tabletten für den Abend bereit.` : « para la noche » (Abend).
- `soins-uebergabe¦sens¦B1 | Heute Nacht hatte sie keine Schmerzen.` : « Anoche » (la nuit qui vient de finir).
- `soins-bad¦sens¦SIT | Ich bleibe bei ihr…` : « jalo » (Mexique, Colombie ; « halo » ailleurs).

## À trancher (un soignant hispanophone devrait relire)

Les pays d'Amérique ne disent pas tous pareil ; j'ai pris le mot le plus largement compris :

- Akte / dossier → **el expediente** (Mexique ; Colombie : « la historia clínica ») — déjà 14 fois dans les autres lots.
- Blutzucker / glycémie → **la glucosa** (« medirse la glucosa ») ; autre choix : « el azúcar en la sangre ».
  Traubenzucker → « pastillas de glucosa ».
- Rollator → **el andador** (Mexique : « la andadera » ; Colombie : « el caminador »).
- Klientin (soins à domicile) → **la usuaria** (autre choix : « la paciente », plus courant mais efface la nuance allemande).
- Hausärztin → **la médica de cabecera** ; Ärztin → « la doctora ».
- Übergabe / relève → **la entrega de turno** ; Spätdienst, Nachtdienst → « turno de la tarde / de la noche ».
- Stationszimmer / poste de soins → **la estación de enfermería** (Mexique : « la central de enfermeras »).
- Stationsleitung → « la jefa de la unidad » ; Pflegedienstleitung → « la jefa del servicio de enfermería ».
- Abwurfbehälter / collecteur d'aiguilles → **el contenedor para agujas** (Mexique : « de punzocortantes » ; Colombie : « el guardián »).
- Notfallwagen → **el carro de paro** (aussi « carro rojo »).
- Betäubungsmittel → **los estupefacientes** (Mexique : « medicamentos controlados »).
- Patientenverfügung → **la voluntad anticipada** (terme légal au Mexique et en Colombie).
- Kompressionsstrümpfe → « medias de compresión » ; Verband → « el vendaje » ; Dekubitus/escarre → « úlcera por presión ».
- Waschbecken → **el lavamanos** (Mexique : « el lavabo ») ; Waschschüssel → « la palangana » ; Waschlappen → « la toallita ».
- Messlatte / toise → « el tallímetro » (Mexique : « estadímetro ») ; Blutdruckmessgerät → « el tensiómetro » (Mexique : « baumanómetro »).
- Dienstplan → « el horario de turnos » ; Trinkprotokoll → « el registro de líquidos » ; abzeichnen → « firmar con iniciales ».

## Sources fautives ou inégales

- Le français écrit tantôt « Frau Lehmann », tantôt « Mme Lehmann » dans les `sens` (soins-bad : Frau ; soins-stationszimmer,
  soins-aufnahme : Mme) — sans effet sur l'espagnol, uniformisé.
- `soins-uebergabe¦questions¦C1 | Das gehört zur Einschätzung.` : l'explication cite « reizlos », qui n'est ni dans la clé
  ni dans la source (il vient de la question) — traduit tel quel.
- `soins-ambulant¦sens¦B2 | Darf ich das kurz wiederholen…` : le français omet « kurz » ; rendu (« un momento »).
- `soins-aufnahme¦sens¦B1 | Darf ich fragen, mit wem Sie zu Hause wohnen?` : le français omet « zu Hause » ; rendu (« en su casa »).
- Aucune faute relevée dans l'allemand.
