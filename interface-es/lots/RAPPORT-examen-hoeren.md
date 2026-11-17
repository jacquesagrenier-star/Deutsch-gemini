# Rapport : épreuves d'écoute d'examen (`examen-hoeren`)

Lot : `interface-es/lots/examen-hoeren.es.json` (15 nov. 2026).

## Chiffres

- 360 clés sur 360 : 120 `frage`, 120 `options` (listes de 3, même ordre que le français), 120 `erkl`.
  Aucune base `consigne` ni `trad` dans cette source ; le champ `de` y est vide partout (j'ai lu
  l'allemand dans le champ `audio` de `pruefung.json`, en lecture seule, pour les cas douteux).
- `textes.py controle` : 120 « FAUTE vide » qui sont **toutes** les listes d'options (le contrôle
  n'accepte que des chaînes) ; longueurs vérifiées par le script de brouillon (3 éléments, tous
  distincts, même ordre) et par la pose. **0 autre faute.** 3 avis, tous de l'allemand cité
  (« des Ausweises », « Brauchst du », « Ton »).
- Pose à blanc (`poser_examen_es.py pruefung.json es …`, sans `--ecrire`) :
  « es : 360 champs poses, 360 encore manquants », sans arrêt.

## Choix de traduction

- Tutoiement partout dans les explications, y compris là où le français vouvoie (« ce qu'on attend
  de vous » → « lo que se espera de ti », « cherchez » → « busca »). Aucun candidat vouvoyé dans
  cette source, donc aucun « usted ».
- Les citations allemandes restent telles quelles entre «…» (sans espaces), majuscules d'insistance
  gardées (SONDERN, DAGEGEN, SELBST, UND).
- Heures : format de la source (« 18 h », « 21:30 »). Euros inchangés.
- Lieux : Salzburgo, Núremberg, Fráncfort, Colonia ; Bonn, Düsseldorf, Hannover tels quels.
- Vocabulaire : andén, tranvía, autobús de reemplazo, carro, embotellamiento, presupuesto
  (Kostenvoranschlag), deducible (Selbstbeteiligung), la renta (loyer), acta de nacimiento,
  efectivo, receta, cita, paquete, piscina, ascensor, boletos, teletrabajo, trenes suburbanos
  (S-Bahn), ayuntamiento (alignés sur les lots déjà rendus).

## Explications réécrites (contre l'espagnol)

- `hoeren/15` : « Dafür » ne veut pas dire « pour cela » → «para eso» / «en cambio».
- `hoeren/49` : « à l'envers du français » → « al revés que en español: la unidad antes de la decena ».
- `hoeren/52` : « montags » / « am Montag » appuyé sur l'opposition espagnole «los lunes» / «el lunes».
- `hoeren/65` : « participation personnelle » → «participación propia» ; franchise → *el deducible*.
- `hoeren/76` : « deux idées que le français distingue moins nettement » retiré (l'espagnol distingue
  *vencimiento* et *aplazamiento*) → « dos ideas que conviene no confundir ».
- `hoeren/92` : « en apparence — et non "apparemment" » → «solo en apariencia», y no «al parecer».
- `hoeren/39` : l'idiome rendu par un idiome espagnol, «ser harina de otro costal».
- `hoeren/80` : « sinon » → «si no».

## Sources fautives ou imprécises

- `hoeren/49|erkl` : l'explication parle de « l'unité avant la dizaine », mais l'exemple est
  « zweihundertvierzig » (240), qui n'a pas d'unité ; le piège réel est 240 / 250 et le « siebzehn »
  de l'heure. Traduit tel quel.
- `hoeren/66|erkl` : le français dit « Le cours n'est pas garanti », l'anglais « The place » ;
  l'allemand dit « Sollte ein Platz frei werden » : j'ai suivi l'allemand (« El lugar no está garantizado »).
- `hoeren/13|frage` : l'anglais dit « during the closure », le français « pendant les vacances » ;
  l'allemand dit seulement « geschlossen ». J'ai suivi le français.
- `hoeren/33|options` : le français dit « Dans l'ascenseur », l'anglais « By the lift » ; rendu « En el ascensor ».
- `hoeren/50|frage` : « Où le train s'arrête-t-il » = terminus (« nur bis Köln ») → « ¿Hasta dónde
  llega hoy el tren? », options en « Hasta … » (dont « Hasta el andén 11 », distracteur).

## Doutes

- `hoeren/4` : *Zugbegleiter* → « el encargado del tren » (« revisor » est d'Espagne, « inspector » évoque le contrôle des billets).
- `hoeren/19` : *Personalausweis* → « cédula de identidad » (pour le distinguer du passeport) ;
  *Meldebescheinigung* → « constancia de domicilio » (Mexique ; Colombie : « certificado de residencia »).
- `hoeren/10` : *Anwohner* → « los vecinos de la calle ».
- `hoeren/13` : « la contestadora » (Mexique) pour le répondeur ; « el contestador » ailleurs.
- `hoeren/33` : « el salón 203 » (salle de cours) ; `hoeren/20` garde « la sala » (salle de réunion).
- `hoeren/55` : *Kassenbon* → « el recibo de compra » ; `hoeren/83` : *Ausweis* d'élève → « credencial vigente ».
- `hoeren/62` : *Bewerbung* → « solicitud de empleo » ; `hoeren/105` : *Bewerbungen* (université) → « solicitudes », places → « cupos ».
- `hoeren/78` : « bis Ende der Woche » → « Hasta el final de la semana » (surtout pas « fin de semana », le week-end).
- `hoeren/57` : « Ir con el Dr. Hoffmann » (tournure mexicaine, comprise ailleurs).

## À trancher

- « ayuntamiento » (Mexique) ou « alcaldía » (Colombie) pour *Rathaus* (`hoeren/2`, `hoeren/45`) : les lots précédents emploient les deux.
- « la renta » (Mexique) pour le loyer (`hoeren/79`, `84`, `114`) : « el arriendo » en Colombie, « el alquiler » ailleurs.
- « piscina » gardé (compris partout) plutôt que « alberca ».
