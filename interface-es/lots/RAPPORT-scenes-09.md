# Rapport — scenes-09 (espagnol, interface de l'allemand)

## Fait

- `interface-es/lots/scenes-09.es.json` : **300 textes sur 300** (strand fin, supermarkt, ubahn, umzug,
  untersuchung-dos, untersuchung début).
- Contrôle `scenes_textes.py controle` : **300 textes, 0 faute, 0 avis**.
- Une seule passe d'écriture, relue en entier ; fabriqué par `scenes-09_construire.py` (scratchpad), les
  clés sont reprises de la source par leur rang, jamais retapées.
- Titres de couche repris de scenes-01 (« Sustantivos y artículos », « Wo? — las preposiciones »,
  « Suposiciones ») ; « Hypothèses et Konjunktiv II » → « Suposiciones y Konjunktiv II ».
- Cas : la source dit « datif / accusatif » → « dativo / acusativo ». « plus-que-parfait » et « prétérit »
  → **Plusquamperfekt**, **Präteritum** (comme les lots 01-06 ; « pretérito » serait ambigu en espagnol).
  « participe II » → « participio II ».

## Explications réécrites contre l'espagnol (clés)

- `supermarkt¦questions¦B1 | Das Mädchen ist kleiner als Anna.` — ajout « (más pequeña que) ».
- `… | Die Bananen sind so gelb wie …` — « (tan … como) ».
- `… | Anna findet Milch gut, aber Käse findet sie besser.` — « como bueno → mejor ».
- `supermarkt¦questions¦B2 | Könnten Sie mir bitte eine Tüte geben?` et `Wären Sie so nett…` — « como
  «¿podría…?» », « como «¿sería tan amable…?» ».
- `… | An Ihrer Stelle würde ich…` — « (Yo en su lugar…) ».
- **müssen** (4 clés C1 : supermarkt, ubahn, umzug, untersuchung) — « como «debe de querer / estar / hacer» »,
  comme les lots 01-04.
- `ubahn¦questions¦B1 | Der Mann singt nicht, sondern…` et `Der Hund bellt nicht, sondern…` — l'espagnol a
  le mot exact : « sondern = sino », « no …, sino … » (au lieu de « mais au contraire »).
- `ubahn¦questions¦B1 | Mark beeilt sich, denn…` — « pues, porque ».
- `ubahn¦questions¦B2 | Man darf nur einsteigen, wenn…` — « indicativo, como en español ».
- `umzug¦questions¦B2 | Bis heute Abend wird Anna…` — « como «habrá desempacado» ».
- `umzug¦questions¦B2 | In einer Stunde wird der Bruder … gegangen sein.` — « El español siempre usa «haber» ».
- `umzug¦questions¦B2 | Anna ist müde. Sie wird viel getragen haben.` — le futur de supposition existe en
  espagnol : « como en español … (habrá cargado mucho) » ; les deux `sens` correspondants emploient ce futur
  (« Habrá cargado mucho », « La habrá pedido el hermano »).
- `untersuchung-dos¦questions¦B1 | Er hält die Hände so, dass man…` — « man … como «uno» ».
- `untersuchung-dos¦questions¦B2 | … dessen / deren` et `untersuchung¦questions¦B2 | … dessen Brust` — « (cuya
  espalda) », « (cuyo estetoscopio) », « (cuyo pecho) ».
- `untersuchung-dos¦questions¦B2 | Nachdem er sich umgedreht hatte…` — « Un verbo reflexivo toma haben » :
  gardé, mais ce n'est un piège que pour un francophone (être) ; en espagnol c'est déjà « haber ».

## Choix de vocabulaire

- der Korb → la canasta ; die Tüte → la bolsa ; die Tasche → el bolso ; das Regal → el estante ;
  die Dosen → las latas ; die Kasse → la caja ; der Boden → el suelo (pas « piso », ambigu avec l'Espagne).
- die U-Bahn → el metro ; die Fahrkarte → el boleto ; der Bahnsteig → el andén ; die Brezel → el pretzel ;
  der Koffer du musicien → el estuche (comme le français « étui »), celui de la dame → la maleta.
- Soins : die Ärztin → la doctora (comme scenes-01) ; abhören → auscultar ; die Waage → la báscula ;
  toise → el tallímetro ; ein-/ausatmen → inhalar / exhalar ; die Kniekehlen → las corvas ;
  die Schulterblätter → los omóplatos ; röntgen lassen → mandar a hacerse una radiografía.
- Perfekt → pretérito (« Anna voló a España ») ; dürfte → « probablemente » ; könnte → « podría » ;
  sollen → « Dicen que… ».

## À trancher

- `strand¦sens¦A2 | Der Eimer steht neben dem Korb.` — « el balde » (Colombie, Amérique du Sud) ; le Mexique
  dit « la cubeta ».
- `umzug¦champs¦alt` et `umzug¦sens¦B2 | Gleich wird der Bruder die Glühbirne…` — « el foco » (Mexique,
  Pérou, Équateur) ; la Colombie dit « el bombillo ».
- `ubahn¦sens¦B1 | Mark beeilt sich…` — « se apura » (américain) plutôt que « se da prisa ».
- `ubahn¦champs¦alt` — « un basurero » (poubelle), « tenis » (baskets), « chaqueta acolchada » (doudoune) ;
  le Mexique dirait aussi « bote de basura », « chamarra ».
- `untersuchung-dos¦sens¦A2 | Seine Hände sind neben seinem Po.` — « las nalgas » ; un soignant préférera
  peut-être « los glúteos ». « las corvas » (Kniekehlen) est le mot juste mais peu courant : à relire par
  un soignant, comme « tallímetro » (aussi « estadímetro »).
- `untersuchung*¦champs¦autre_vue` — « ↻ Girar a Mark » (aussi possible : « Voltear a Mark »).
- `supermarkt¦sens¦B1 | Die Tüte ist größer als die Tasche.` — « el bolso » ; au Mexique un sac à main est
  « la bolsa », ce qui aurait donné deux fois le même mot dans la phrase.

## Sources fautives ou à regarder

- `umzug¦questions¦C1 | Die Bücher könnten ins weiße Regal kommen.` — l'explication met en gras
  **könnte** alors que la phrase dit **könnten** (fr et en) ; rendu tel quel.
- `untersuchung-dos¦sens¦B1 | Mark hat sich umgedreht, damit sie … abhören kann.` — le français dit « pour
  qu'elle puisse ausculter son dos » ; rien de faux, signalé seulement parce que l'espagnol demande le
  datif d'intérêt (« auscultarle la espalda »).
- `ubahn¦sens¦C1 | Die Frau könnte zum Flughafen fahren.` — le français « part peut-être à l'aéroport » ;
  rendu sur l'allemand : « podría ir al aeropuerto ».
- `strand¦sens¦C1 | Das Wasser dürfte schon ziemlich warm sein.` — le français « doit déjà être » efface
  la différence dürfte / müssen ; rendu « probablemente ».
