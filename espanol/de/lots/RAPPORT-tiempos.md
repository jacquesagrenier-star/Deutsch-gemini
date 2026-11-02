# Rapport : phrases des temps (tiempos) en allemand — 1er nov. 2026

## Fait

- **873 verbes × 6 temps**, traduits depuis l'espagnol, dans `lots/tiempos-01.txt` à `lots/tiempos-15.txt`
  (60 verbes par lot, 33 dans le dernier). Chaque lot passe `poser.py pose --essai` (« N entrees verifiees »).
- Colonnes vides respectées : seul `337 soler` a des cases vides (preterito, futuro, condicional), comme la source.
- Choix de temps : indefinido → Perfekt le plus souvent (allemand parlé), Präteritum pour sein/haben/Modalverben et
  les narrations ; imperfecto → Präteritum (avec „früher“, „immer“, „gerade“ quand la phrase le porte) ;
  perfecto → Perfekt ; futuro → Präsens + Zeitangabe ou „wird … “ ; condicional → „würde“ / Konjunktiv II
  (hätte, wäre, könnte) ; subjuntivo → indicatif après „Ich will, dass …“, „Ich hoffe, dass …“, „Es ist wichtig, dass …“.
- Le contrôle « mot-outil allemand » (liste `OUTILS`) a fait reformuler 7 phrases courtes au passif ou sans article
  (206, 251, 253, 283, 472, 473, 535, 727, 835) : elles portent maintenant „hat“, „man“, „in dem“, etc. Sens inchangé.

## Doutes (à relire)

- `286 deber dinero`, `727 juzgar moralmente`, `732 importar bienes`, `736 intervenir diplomáticamente`,
  `739 entrenar un modelo`, `740 generar contenido`, `742 investigar a fondo`, `744 publicar resultados`,
  `748 inspirar confianza`, `752 supervisar el avance`, `755 contrastar fuentes`, `760 persuadir con datos`,
  `763 reciclarse profesionalmente`, `764 adaptarse al cambio`, `766 estimular la economía`, `770 silenciar el pasado`,
  `773 analizar un texto`, `775 intervenir en el debate` : entrées « verbe + complément » — traduites comme des
  locutions complètes, pas comme un verbe seul.
- `121 quedarse` perfecto : « Nos hemos quedado sin pan » → „Wir haben kein Brot mehr“ (sens, pas forme).
- `316 echar` futuro : « Te echaré de menos » → „Ich werde dich vermissen“ (locution).
- `336 sentar` : sens « faire du bien / mal » (me sentó mal) rendu par „bekommen“ / „gut tun“.
- `337 soler` : „gewöhnlich“ pour rendre l'habitude ; le perfecto « ha solido » est rare en espagnol même.
- `409 importar` : les 5 phrases non commerciales rendues par „egal sein“ / „etwas ausmachen“.
- `473 suceder` subjuntivo : « Pase lo que pase, suceda lo que suceda » → deux tournures „Was auch passiert, was auch
  immer geschieht“ (redondance voulue par la source).
- `684 ahogar` subjuntivo : « ahogarse en un vaso de agua » → „aus einer Mücke einen Elefanten machen“ (équivalent
  idiomatique, pas littéral).
- `705 manejar`, `811 disponer`, `815 rendir`, `803 corresponder` : verbes polysémiques, chaque phrase traduite selon
  son sens propre ; la carte n'a donc pas un seul verbe allemand pour les six phrases.
- `253 nacer` preterito : « Nací en Montreal » → „Ich bin … geboren“ (Perfekt d'état, le seul naturel).
- Les prénoms (Ana, Lucía, Pablo, Tobi) et lieux (Prado, Serrat, Lorca, Camino del Norte) sont gardés tels quels.

## Sources qui semblaient fautives ou étranges

- `337 soler` perfecto : « Siempre ha solido llegar temprano » — forme peu usitée ; traduite quand même.
- `473 suceder` subjuntivo : phrase doublée (« Pase lo que pase, suceda lo que suceda ») ; probablement voulue pour
  montrer deux synonymes.
- `727 juzgar moralmente` imperfecto : « se juzgaba moralmente a las madres solteras » — passif réfléchi ; rendu par „man“.
- Aucune phrase vide inattendue ; aucune ligne avec un « | » parasite.

## Comparaisons avec l'allemand

Aucune : ce sont des phrases d'exemple, pas des explications. Pas de note grammaticale ajoutée.
