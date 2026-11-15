# Rapport — scenes-01 (15 nov. 2026)

## Fait

- `lots/scenes-01.es.json` : **300 textes sur 300** (apotheke 59, arztpraxis 59, baeckerei 59,
  bauernhof 59, bibliothek 59, début de buergeramt 5).
- Contrôle `scenes_textes.py controle` : **0 faute, 3 avis**, tous voulus :
  - deux « identique au français » : `Konjunktiv I de sollen → <b>solle</b>` et
    `Konjunktiv I de sein → <b>sei</b>` (le texte est le même dans les deux langues) ;
  - un « du » : le pronom allemand dans `du → <b>dich</b>`.
- Relu en entier une fois, après la traduction ; le nombre de balises `<b>` est vérifié par le contrôle.

## Explications réécrites contre l'espagnol (clés)

- `arztpraxis¦questions¦B2 | Der Patient, dessen Knie verletzt ist…` et
  `bibliothek¦questions¦B2 | Der Student, dessen Haare lockig sind…` : « dont » → **« cuyo »**, avec la
  phrase ajoutée « Al revés que «cuyo», concuerda con el poseedor » (cuyo s'accorde avec la chose
  possédée, dessen avec le possesseur : c'est le piège propre à l'hispanophone).
- `arztpraxis¦questions¦B2 | Das Fenster ist geschlossen.`,
  `… | Das Pflaster ist schon aufgeklebt.`, `bibliothek¦questions¦B2 | Das Buch ist schon zur Hälfte gelesen.` :
  le passif d'état rapproché de **« estar » + participe** (está cerrada, está puesta, estar leído).
- `bibliothek¦questions¦B2 | Hier wird nicht laut gesprochen.` : le passif impersonnel rapproché du
  **« se » impersonnel** (« aquí no se habla en voz alta »).
- `arztpraxis¦questions¦B1 | Der Ball liegt auf der Tasche.` : liegen / legen, avec l'ajout
  « El español dice «estar» y «poner» para todo ».
- `arztpraxis¦questions¦B1 | Mark hat seine Jacke neben die Tür gehängt.` : « on a accroché / elle
  était accrochée » → « alguien la colgó / estaba colgada ».
- `bauernhof¦questions¦B1 | Anna freut sich über das Pferd.` : sich rapproché de **« se »**.
- `bibliothek¦questions¦B1` (verbes à préposition) : l'équivalent espagnol donné avec **sa**
  préposition, qui n'est pas celle du français — denken an = pensar **en**, träumen von = soñar **con**,
  sich konzentrieren auf = concentrarse **en**, sich interessieren für = interesarse **por**,
  warten auf = esperar « en español, sin preposición », sich freuen auf = « esperar con ilusión ».
- Les `müssen` des couches C1 (5 scènes) et `arztpraxis … gestürzt sein` : ajout de l'équivalent
  **« debe de + infinitivo »** (debe de estar, debe de haberse caído).
- Les trois Plusquamperfekt de `baeckerei¦questions¦B2` : ajout de « como «había horneado / trabajado / pagado» ».
- `baeckerei¦questions¦B2 | Als Anna hereinkam, hatte der Nachbar sich schon gesetzt.` : rendu tel
  quel (« sich setzen → haben ») ; le piège de l'auxiliaire être n'existe pas en espagnol, rien n'est annoncé.

## Choix à connaître

- Couche C1 « Hypothèses » → **« Suposiciones »** (les modaux de supposition ; « Hipótesis » ferait
  attendre le conditionnel). Six fois, toujours pareil. À aligner avec les autres parts des scènes.
- Les `sens` suivent l'allemand : Perfekt → pretérito (« Mark puso… », « Mark colgó… »), könnte →
  « podría », dürfte → « probablemente », soll → « Dicen que… ».
- « Bürgeramt » gardé en allemand, comme dans le français ; « Kiez » → « barrio » ; Brandebourg → « Brandeburgo ».

## À trancher (l'Amérique latine hésite)

- **das Pflaster → la curita** (Mexique, Colombie ; « tirita » serait d'Espagne).
- **die Brille → los lentes** (Mexique) ; la Colombie dit « las gafas ».
- **der Mülleimer / la corbeille → el basurero** (Mexique : « bote de basura », Colombie : « caneca »).
- **die Waage → la báscula** (Colombie : aussi « la pesa », « la balanza »).
- **die Tasche (sac de sport) → la bolsa** / « bolsa deportiva » (Colombie : « el maletín », « el bolso »).
- **die Socken → los calcetines** (Colombie : « las medias »).
- **die Jacke → la chaqueta** (Mexique : « la chamarra »).
- **der Kuchen → el pastel** (Colombie : « la torta », « el ponqué ») ; tarte aux fraises → « tarta de fresas ».
- **die Brötchen → los panecillos** (aucun mot commun ; « bolillos » ne vaut qu'au Mexique).
- **der Eimer → el balde** (Mexique : « la cubeta »).
- **das Poster → el póster** (Mexique « cartel », Colombie « afiche »).
- **die Bank → la banca** (banc) ; **der Boden → el piso** à l'intérieur, **el suelo** à la ferme.
- Ces mots doivent s'accorder avec la traduction des **mots** des scènes (table à part, hors de ce lot) :
  je ne l'ai pas consultée.
- Soignant à relire : « camilla » (table d'examen), « venda » (Verband), « resfriado » (Erkältung et
  Schnupfen rendus par le même mot), « lastimada » (verletzt).

## Sources fautives ou à regarder

- `arztpraxis¦questions¦B2 | Das Fenster ist geschlossen.` : le français dit « elle est fermée »
  (la fenêtre), sans faute ; rien à corriger.
- `bauernhof¦questions¦C1 | Die Eier dürften von heute Morgen sein.` : l'explication cite
  `<b>dürfte</b>` alors que la phrase porte **dürften** (pluriel). Recopié tel quel.
- `apotheke¦sens¦B1 | Mark hat kein Fieber, nur Schnupfen.` : le français dit « un rhume » pour
  Schnupfen (le nez qui coule) comme pour Erkältung ; suivi (« un resfriado »).
- `baeckerei¦sens¦B2 | Nachdem er den Kaffee getrunken hatte, las er die Zeitung.` : rien de fautif.
- Aucune faute d'allemand relevée dans les clés.
