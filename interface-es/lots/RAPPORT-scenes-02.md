# Rapport — scenes-02 (15 nov. 2026)

## Ce qui est fait

- `lots/scenes-02.es.json` : **300 textes sur 300** (buergeramt 54, buero 59, camping 59,
  fahrradwerkstatt 59, familie 59, flughafen 10 — ses 10 premiers).
- Par groupe : 10 `champs` (5 alt, 5 consignes), 27 `couches`, 133 `questions`, 130 `sens`.
- Contrôle `scenes_textes.py controle` : **0 faute, 5 avis**, tous attendus : `weder … noch = ni… ni`
  (identique au français, et juste en espagnol), `je … desto` et trois `<b>des</b>` (mots allemands
  pris pour du français).
- Chaque texte relu ligne à ligne contre sa clé (phrase allemande) après l'écriture.
- Script de brouillon : scratchpad `scenes-02_lot.py` (les 300 textes dans l'ordre de la source).

## Choix de vocabulaire (constants dans le lot)

- Cas : **dativo, acusativo, genitivo** en espagnol, parce que la source française dit « datif »,
  « accusatif », « génitif » ; `Konjunktiv II`, `Wo?` restent allemands comme dans la source.
  (Les lots d'exercices emploient plus souvent « Dativ » : à harmoniser si l'on veut une seule forme.)
- « Hypothèses » → **Hipótesis** ; « Noms et articles » → **Sustantivos y artículos** ;
  « Touche un objet » → **Toca un objeto** ; « particule » → **partícula**.
- das Bürgeramt → *la oficina de atención ciudadana* ; die Anmeldung → *el registro de domicilio* ;
  das Praktikum → *las prácticas*.
- Mots repris des cartes du corpus : el basurero, la carpeta, el estante, el armario, la carpa,
  el bote, la olla, el balde, los alicates, el cartel, el hongo, la canasta, la pizarra, la báscula.
- Amérique latine : el carro, las papas, el jugo, el bolígrafo, el boleto, el piso (le sol), el mouse.

## Explications réécrites contre l'espagnol (clés)

- `fahrradwerkstatt¦questions¦B1 | Man braucht eine Zange für die Kette.` — « on » → **«se» impersonal
  o «uno»**.
- `fahrradwerkstatt¦questions¦B1 | Das Rad ist in Ordnung, nichts fehlt.` — la négation unique est un
  vrai piège pour un hispanophone : « sin el «no» del español («no falta nada») ».
- `fahrradwerkstatt¦questions¦B1 | Im Laden ist niemand außer Mark und dem Mechaniker.` — même piège :
  « donde el español dice «no hay nadie» ».
- `fahrradwerkstatt¦questions¦B2 | Hier repariert man Fahrräder.` — ajout « como «se» en español ».
- `fahrradwerkstatt¦questions¦B2 | Die Kette lässt sich leicht reparieren.` — exemple rendu par la
  passive réfléchie : « la cadena se puede reparar ».
- `buergeramt¦questions¦B1 | Die Frau arbeitet bei dem Bürgeramt.` — « chez, employé de » n'a pas
  d'équivalent : « en, el lugar donde uno trabaja ».
- `buero¦questions¦B2 | Die Kollegin, deren Haare grau sind, liest einen Brief.` — « dont » → « cuyo »,
  avec la différence qui trompe : *deren* suit le possesseur, *cuyo* la chose possédée.
- `buero¦questions¦B2 | Das Heft ist schon halb vollgeschrieben.` — passif d'état rapproché de
  « estar + participio ».
- `camping¦questions¦B2 | Wenn es nicht so dunkel wäre, würden sie schwimmen gehen.` — « como
  «si… estuviera» ».
- `camping¦questions¦B2 | Wenn der Mann Hunger hätte, würde er die Wurst essen.` — « el condicional
  del español ».
- `familie¦questions¦B1 | Ihr Vater serviert Kartoffeln.` — « su » ne distingue pas *sein* / *ihr* :
  phrase ajoutée (« El «su» del español no distingue; el alemán sí »).
- `familie¦questions¦B1` (sein Glas, ihr Baby, ihre Großeltern) — « à lui / à elle / à eux » →
  « de él / de ella / de ellos ».

## Doutes

- `buero¦sens¦B2 | Das Heft ist schon halb vollgeschrieben.` — rendu « ya está escrito hasta la
  mitad » (le français dit « à moitié rempli »).
- `buergeramt¦sens¦B2 | Das Büro ist zwar klein, aber hell.` — « Es cierto que… pero… » pour garder
  *zwar* ; un peu plus long que la source.
- `fahrradwerkstatt¦sens¦C1 | Es muss kaputt sein.` — « Debe de estar rota » (la rueda, comme le
  français « Elle ») ; *Es* peut aussi être das Fahrrad.
- `fahrradwerkstatt¦sens¦B2 | Die Werkstatt wird um achtzehn Uhr geschlossen.` — « a las dieciocho
  horas », fidèle à *achtzehn Uhr* ; l'usage courant dirait « a las seis de la tarde ».
- *dürfte* rendu par « probablemente + subjuntivo » (cita, puesto, reparación, pastel) et par
  « deben de ser » (l'heure).
- `familie` : *die Katze* → « el gato » (comme le français « le chat »).

## Sources fautives ou qui s'écartent de l'allemand

- `camping¦…¦B2 | Ich könnte gern so gut Gitarre spielen wie Anna.` — **allemand douteux** : un souhait
  se dit « Ich würde gern so gut … spielen können » ou « Könnte ich doch… » ; « Ich könnte gern »
  n'est pas idiomatique. Traduit selon le sens voulu (« Me gustaría poder… »). À faire relire.
- `fahrradwerkstatt¦sens¦B1 | Kann mir jemand helfen?` et `… | Hat jemand mein Werkzeug gesehen?` — le
  français ajoute « , demande Mark » / « , demande le mécanicien », absents de l'allemand. Gardés
  (« , pregunta Mark »), comme dans les autres langues.
- `fahrradwerkstatt¦sens¦B1 | Im Laden ist niemand…` — le français dit « Dans l'atelier » ; l'allemand
  dit *Laden* : « En la tienda ».
- `camping¦sens¦A2 | Die Lampe liegt neben dem Holz.` — l'objet de l'image est une lampe de poche
  (alt : « linterna ») ; la phrase dit *Lampe* : « La lámpara ».
- `buero¦sens¦B1 | Mark legt den Hörer gleich auf.` — le français « va raccrocher » ; rendu au
  présent, « cuelga el teléfono enseguida ».
- `buero¦sens¦B2 | Die Kollegin, deren Haare grau sind…` — le français contourne la relative (« aux
  cheveux gris ») ; l'espagnol la garde (« cuyo cabello es gris »), puisque c'est le point enseigné.

## À trancher

- **Bürgeramt** : « la oficina de atención ciudadana » (4 textes) — ou garder « el Bürgeramt ».
- **Praktikum** : « prácticas » (Mexique) contre « pasantía » (Colombie, Cône sud) — buero, 4 textes.
- **comptoir d'enregistrement** : « mostrador de check-in » (flughafen, alt) — « de documentación »
  au Mexique, « facturación » est d'Espagne ; et « registra su maleta » (consigne) contre
  « documenta » (Mexique).
- **ampoule** : « un foco » (Mexique) contre « un bombillo » (Colombie) — fahrradwerkstatt, alt.
- **vitrine** : « la vitrina » (Colombie) contre « el aparador » (Mexique) — fahrradwerkstatt, alt.
- **souris** : « un mouse » (buero, alt) plutôt que « ratón ».
- **Kuchen** : « pastel » (Mexique) contre « torta / ponqué » — familie C1.
- **seau** : « el balde » (corpus) contre « la cubeta » (Mexique) — fahrradwerkstatt.
