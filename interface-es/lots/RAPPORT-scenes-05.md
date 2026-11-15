# Rapport — scenes-05 (15 nov. 2026)

## Fait

- `lots/scenes-05.es.json` : **300 textes sur 300** (fin de markt-gemuese-frucht 37, markt-gemuese-wurzel 49,
  markt-obst-heimisch 49, markt-obst-sued 49, museum 59, musik 57 — la scène musik s'arrête à
  `sens¦C1 | Die Geige könnte der Lehrerin gehören.`, la suite est dans scenes-06).
- Contrôle `scenes_textes.py controle` : **0 faute, 8 avis**, tous voulus : sept « je » (le mot allemand de
  `je … desto`, dans trois titres de couche et quatre explications) et un « du » (`du → sollst`).
- Fabriqué par une liste ordonnée (script de brouillon `scenes-05_construire.py`, clés reprises de la source) ;
  le script vérifie aussi le nombre de `<b>` et qu'un même français donne un même espagnol. Une seule
  variante, voulue : « Possession, antécédent masculin → dessen » reçoit « (cuyos tallos) » ou « (cuyas hojas) »
  selon la phrase.
- Relu une fois en entier à l'écriture ; pas de seconde relecture séparée.

## Titres de couche

- Repris de scenes-01 / scenes-04 : « Sustantivos y artículos », « Wo? — las preposiciones », « En el mercado »,
  « Wo? — las preposiciones en el mercado », « Hacer las compras: cantidades y precios »,
  « Pasiva, relativas y adjetivos », « Hypothèses » → **« Suposiciones »** (museum, musik).
- ⚠️ « Hypothèses, je … desto, génitif » → **« Hipótesis, je … desto, genitivo »**, comme scenes-04 l'a écrit pour
  la première vue du marché (même scène, quatre vues). Ici « Hipótesis » se défend (la couche contient de vraies
  conditions irréelles : *Wäre der Kürbis nicht so schwer…*), mais c'est un écart avec « Suposiciones » : à trancher
  pour les quatre vues ensemble.
- Nouveaux : « Los interrogativos: welcher? was für ein? », « El modo: indem, dadurch dass »,
  « Los verbos modales », « La declinación del adjetivo ».
- Vues du marché : « Raíces y coles », « Frutas de la región » (comme le `autre_vue` de scenes-04), « Frutas del sur »,
  « → Otras verduras », « → Verduras ».

## Explications réécrites contre l'espagnol (clés)

- `markt-gemuese-frucht¦questions¦B2 | Der Mangold, dessen Stiele…`, `markt-gemuese-wurzel¦questions¦B2 | Der Lauch, dessen Blätter…` :
  ajout de « (cuyos tallos / cuyas hojas). Al revés que «cuyo», concuerda con el poseedor » (formule de scenes-01).
- `markt-obst-sued¦questions¦B2 | Die Mango, deren Schale…` : « dont la peau » → « (cuya cáscara). Se elige según el
  poseedor, no según lo poseído como «cuyo» » (formule de scenes-03, buero).
- `markt-gemuese-frucht¦questions¦B2 | Die Kürbisse sind schon geerntet.` : « invariable » → « como «estar» + participio;
  pero el participio alemán no cambia » (en espagnol il s'accorde : cosechadas).
- `markt-obst-sued¦questions¦B2 | Die Kokosnuss ist schon geöffnet.` : « elle EST ouverte » → « ESTÁ abierto » (el coco ; « estar » dit
  déjà l'état).
- `markt-obst-sued¦questions¦B1 | Sind die Mangos schon reif?` : « il ne s'accorde pas » → « no concuerda, al revés que en
  español (maduros) ».
- `museum¦questions¦B2 | Anna lernt, indem sie die Skulptur zeichnet.` : « en (+ participe présent) » → « el gerundio del
  español (dibujando) ».
- `museum¦questions¦B1 | Was für ein Bild ist das?` : ajout de « como «¿qué tipo de…?» ».
- `museum` et `musik`, `questions¦C1 | … muss …` : « como «debe de» + infinitivo » (comme scenes-01).
- Les `je … desto` : « plus …, plus … » → « cuanto más…, más… » ; `obwohl` = « aunque » ; `sollte` = « uno debería » ;
  `müssen` (obligation) = « tener que, deber » ; `Ich hätte gern` / `möchte` = « quisiera ».
- `markt-gemuese-wurzel¦questions¦B1 | … eine Knolle Knoblauch …` : tête / gousse → « cabeza de ajo » / « diente ».

## Choix à connaître

- Les `sens` suivent l'allemand : Perfekt et passif au prétérit → pretérito ou « se » (« se cosecharon »), passif présent →
  « se cosechan », « se cultivan » ; dürfte → « Probablemente… » ; soll → « Dicen que… » ; muss (déduction) → « debe de… ».
- `museum¦sens¦C1 | Der junge Mann könnte Kunst studieren.` → « Puede que el joven estudie arte » (et non « podría
  estudiar », qui se lirait comme une capacité) ; `musik … könnte der Lehrerin gehören` → « podría ser de la profesora ».
- Mots repris du corpus déjà traduit : calabaza, calabacín, hongo, frijol, acelga, repollo, col de Bruselas, colinabo,
  puerro, apio, rábano, arándano, grosella espinosa, albaricoque, durazno, piña, aguacate, toronja, sandía, audífonos,
  radiador, abrigo, bufanda, violín, estante, banca (banc), piso (à l'intérieur).
- `Die Lehrerin` du cours de guitare → « la profesora » ; `der Mann` (le gardien) reste « el hombre » dans les sens,
  « un vigilante » dans l'alt.

## À trancher (l'Amérique latine hésite)

- **die Bananen → los plátanos** (Mexique ; Colombie « bananos » ; le corpus donne « el plátano, el banano »).
- **die Zitronen → los limones / die Limetten → las limas** : au Mexique et en Colombie, « limón » est le petit citron
  vert ; « lima » y désigne parfois un autre fruit. Le corpus dit « la lima, el limón verde ».
- **die Süßkartoffeln → los camotes** (Mexique, Pérou ; Colombie « batatas »).
- **Rote Bete → las remolachas** (Mexique « betabeles »).
- **die Aprikosen → los albaricoques** (Mexique « chabacanos », cône sud « damascos »).
- **die Erdbeeren → las fresas** (consignes) ; **die Pfirsiche → los duraznos**.
- **eine Schale (barquette) → una canastilla** (aussi « cajita », « canastita ») ; **die Kiste / la cagette → la caja**
  (comme scenes-04).
- **ein Pfund → una libra** : compris en Colombie (500 g), moins au Mexique ; l'explication dit « 500 gramos ».
- **Südfrüchte** : titre de vue « Frutas del sur » (le sud vu d'Allemagne), mais dans la phrase B2 « Las frutas
  tropicales » ; un Latino-Américain ne dit pas « frutas del sur » pour ses propres fruits.
- **braune Jacke → chaqueta café** (Mexique, Colombie ; « marrón » ailleurs) ; **T-Shirt → la camiseta** (Mexique « playera »).
- **der Kronleuchter / le lustre → una lámpara de araña** ; **le gardien → el vigilante** ; **le pupitre → el atril**.
- **Sellerie → el apio** : à l'étal des racines c'est sans doute le céleri-rave (« apio nabo ») ; suivi le corpus.

## Sources fautives ou à regarder

- `markt-obst-heimisch¦champs¦alt` : le français dit « groseilles » là où les phrases disent « groseilles à maquereau »
  (Stachelbeeren) ; rendu « grosellas espinosas » partout.
- `markt-gemuese-frucht¦sens¦C1 | Artischocken sollte man…` et `markt-obst-sued¦sens¦C1 | Avocados sollte man nicht…` :
  le français dit « Il faut / Il ne faut pas », plus fort que *sollte* ; suivi l'allemand (« deberían »).
- `markt-gemuese-frucht¦sens¦B2 | Der Mangold, dessen Stiele…` et les deux autres relatives en dessen / deren : le
  français contourne (« aux tiges… ») ; l'espagnol garde la relative (« cuyos tallos… »), qui est le point de la question.
- `markt-gemuese-frucht¦sens¦B1 | Kommt der Spargel aus der Region?` : rendu « ¿… son de la región? » (kommen aus).
- `museum¦sens¦B1 | Mit was für einem Stift…? — Mit einem Bleistift.` : *Stift* et *Bleistift* n'ont qu'un mot naturel
  en espagnol ; rendu « lápiz » / « lápiz de grafito ».
- `museum¦sens¦A2 | Der Student steht am Fenster.` : « de pie » ajouté (steht), le français ne le dit pas.
- Aucune faute d'allemand relevée dans les clés.
