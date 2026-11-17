# Rapport — corpus-themes-C1-02 (15 nov. 2026)

## Fait

- `corpus-themes-C1-02.es.json` : **240 cartes sur 240** (n° 3892 à 4131), chacune `traduction` + `exemple`.
  Treize thèmes C1 : Bildung, Wissen und Medien (24), Gefühle und Charakter (24), Technik, Form und
  Gestaltung (20), Umwelt (20), Gesundheit (20), Einkaufen und Geld (19), Verkehr (18), Ethik und
  Werte (18), Politik und Gesellschaft (17), Geschichte und Erinnerung (17), Wohnen (15), Natur (15),
  Familie (13).
- Contrôle `corpus_lots.py controle` : **0 faute, 0 avis**.
- Doublons cherchés dans chaque thème contre les lots A1 à B2 déjà rendus (même `contexte`) par
  `themes-C1-02_verif.py` (scratchpad). `corpus-themes-C1-01` porte dix autres thèmes : aucun
  thème commun, donc aucun croisement possible avec lui.
- Vocabulaire aligné sur les niveaux inférieurs : Miete = « la renta » (4011, 4013), Lastschrift =
  « el débito automático » (4033), carro, apartamento, confiable.

## Doublons acceptés

- **3985 Rehabilitation = « la rehabilitación »**, comme **Reha** (B1, Gesundheit) : Reha n'est que
  l'abréviation du même mot ; l'espagnol n'en a qu'un.

Voisins proches mais non identiques (laissés ainsi, aucun mot plus juste) :
- 4064 Staatsangehörigkeit « la nacionalidad, la ciudadanía » / Staatsbürgerschaft (B1) « la ciudadanía, la nacionalidad » : synonymes en allemand aussi, seul l'ordre diffère.
- 4044 Umstieg « el transbordo, el cambio (a otra cosa) » / Umsteigen (B2) « el transbordo ».
- 3917 Rücksichtnahme « la consideración (hacia los demás) » / Rücksicht (B1) « la consideración ».
- 3951 Wartung (Technik) et 4010 Instandhaltung (Wohnen) partagent « el mantenimiento », mais dans deux thèmes ; 4010 est rendu « la conservación, el mantenimiento ».
- 4131 Moor : « la turbera, la ciénaga » pour ne pas reprendre « el pantano » de Sumpf (B2).

## Doutes (à relire)

- **3892** : « zweiter Bildungsweg » rendu « la educación para adultos » (comme le français) ; l'institution allemande n'a pas d'équivalent exact.
- **3923 Übermut** : « por exceso de confianza » ; l'allemand porte aussi l'idée d'exubérance.
- **3931** : « erst spät erkannt » → « tardó en reconocerse ».
- **3953 Machart** : « la factura, la hechura » (factura au sens artisanal, risque de lecture « facture à payer »).
- **4002 Bausubstanz** : « la estructura del edificio » (le bâti existant, pas seulement la structure porteuse).
- **4007 Leerstand** : « la desocupación (de inmuebles) » ; « desocupación » seul veut dire chômage en Argentine, d'où la précision gardée jusque dans la phrase.
- **4022 Abgabe** : « el gravamen, la contribución obligatoria » ; phrase rendue par « se descuentan las contribuciones ».
- **4054 Mehrheitsverhältnis** : « la correlación de fuerzas » ; « escaños » dans la phrase (curul au Mexique et en Colombie, banca en Argentine).
- **4088 Zumutbarkeit** : pas de nom espagnol ; « la exigibilidad (lo que es razonable exigir) ».
- **4103 Vorbehaltlosigkeit** : « la incondicionalidad ».
- **4109 Fürsorglichkeit**, **4111 Geborgenheit** : mots sans équivalent ; « la actitud protectora, la solicitud », « la seguridad afectiva, el cobijo ».
- **4114 Wiederannäherung** : « el reacercamiento » (courant en presse, absent du DLE).
- **4130 Geröll** : rendu au pluriel « las piedras sueltas, el pedregal » pour un neutre singulier.

## Sources fautives ou écartées de l'allemand

- **3894** : le français dit « deux redoublements » ; l'allemand « zwei Wiederholungen » parle de deux nouvelles tentatives à l'examen (l'anglais « retakes » est juste). Suivi l'allemand : « dos repeticiones ».
- **4006** : « plan local d'urbanisme » est plus large que le Bebauungsplan (plan de détail d'un secteur) ; rendu « el plan urbanístico (local) ».
- **4119 Mündung** : le français ajoute « confluent » ; gardé « la desembocadura » seul.
- Aucune faute relevée dans l'allemand.

## À trancher

- **3995 Beipackzettel** : « el prospecto » (Argentine, Chile, compris partout) ; le Mexique dit « el instructivo », la Colombie « el inserto ». À faire relire par un soignant.
- **3975 Feinstaub** : « las partículas finas, el material particulado » (les deux se disent selon les pays).
- **3984 Impfschutz**, **3997 Nachsorge**, **3998 Beschwerdefreiheit**, **3993 Selbstheilungskräfte** : termes de soins (« la protección de la vacuna », « el seguimiento posterior (al tratamiento) », « la ausencia de síntomas », « las fuerzas de autocuración ») à faire relire par un soignant.
- **4014 Untermiete** : « el subarriendo » (Colombie, Chili) ; le Mexique dit plutôt « el subarrendamiento », ailleurs « el subalquiler ».
- **4020 Pfand** : « 25 Cent » rendu « 25 céntimos » (le nom officiel du centime d'euro en espagnol), et non « centavos ».
- **4033 Rücklastschrift** : « la devolución de un débito automático » ; pas de terme commun à toute l'Amérique (« cargo rechazado », « domiciliación devuelta »).
- **4044** : « Hannover » laissé tel quel (l'exonyme « Hanóver » existe mais reste peu employé).
- **4056 Stimmzettel** : « la boleta electoral » (Mexique, Argentine) ; « el tarjetón » en Colombie, « la papeleta » ailleurs ; les deux premiers sont donnés.
- **4061 Lobbyismus** : « el cabildeo » (Mexique, Colombie) avec « el lobby » en second.
