# Rapport : corpus-themes-C1-04 (15 nov. 2026)

## Fait

- `corpus-themes-C1-04.es.json` : **228 cartes sur 228** (n° 4372 à 4599), traduction + exemple, 16 thèmes C1
  (Stadt und Gebäude, Logistik, Musik, Medien, Reisen, Tiere, Versicherung, Schule, Garten, Sport, Bild,
  Polizei, Heimwerken, Lebensführung, Vereinsleben, Pflege).
- Contrôle `corpus_lots.py controle` : **0 faute, 0 avis**.
- Comparaison (script de brouillon `themes-C1-04_verif.py`) avec les `traduction_es` des mêmes thèmes dans
  `themes.json` (A1-B2) et avec les lots C1-01 à C1-03 : un seul doublon restant, accepté (ci-dessous).
  Alignements faits sur les niveaux inférieurs : Zeugnis = *el boletín*, Note = *la nota*, Buchung = *la reserva*,
  Miete = *la renta*, Heim = *la residencia*, Krankenkasse = *la caja de seguro*, Mitglied = *el miembro*.

## Doublons acceptés

- **4472 Notenschnitt** = *el promedio de notas*, comme **Notendurchschnitt** (B2, Schule) : synonymes
  stricts en allemand, l'espagnol n'a qu'un mot.

Doublons évités par un autre mot ou une précision :
- 4432 Gepäckaufgabe : *el registro de equipaje* (Gepäckausgabe A2 est *la entrega de equipaje*).
- 4413 Datensicherung : *el respaldo de datos* (Sicherheitskopie B2 est *la copia de seguridad*).
- 4435 Fremdenverkehr : *el turismo (sector)* (Tourismus B1 est *el turismo*).
- 4447 Rudel : *la manada (de lobos), la jauría* (Herde B1 est *la manada, el rebaño*).
- 4441 Beutetier : *la presa (animal)* ; 4399 / 4400 Partitur / Notenblatt : *la partitura (de orquesta)* / *la hoja de música*.

## Doutes

- 4373 Aufenthaltsqualität : *la calidad de estancia (espacio público)*, calque du terme d'urbanisme ; pas de mot établi.
- 4387 Lieferengpass : *el cuello de botella en el suministro* (long ; *la escasez de suministro* serait plus court mais moins exact).
- 4459 Leistungsfall : *el siniestro cubierto* ; l'exemple dit « die Kasse » (caisse maladie), rendu *la caja de seguro*.
- 4460 Obliegenheit : *la obligación contractual (del asegurado)*, la précision sert à la distinguer d'une simple *obligación*.
- 4466 Berufsunfähigkeit : *la incapacidad profesional* (et non *laboral*, qui est plutôt Arbeitsunfähigkeit).
- 4473 Versetzung : l'exemple garde « a pesar del cinco » (la note 5 allemande, insuffisante) sans l'expliquer.
- 4483 Übertritt : *Gymnasium* laissé en allemand dans l'exemple, comme la carte B1.
- 4485 Aussaat : « die Eisheiligen » rendu *los Santos de Hielo* (référence inconnue en Amérique latine).
- 4517 Belichtung : « um zwei Blenden daneben » = *desviada por dos pasos de diafragma*.
- 4523 Farbstich : *la dominante de color* (terme de photographe).
- 4561 Genussmittel : *el producto de disfrute (café, alcohol…)*, pas d'équivalent ; calqué sur la glose française.
- 4571 Lebensführung : *la manera de llevar la vida* (pour ne pas reprendre *el estilo / modo de vida*).
- 4581 Schirmherrschaft : *el patrocinio honorífico* (*patrocinio* seul ferait penser à un commanditaire).
- 4583 Gemeinnützigkeit : *la utilidad pública* ; en Amérique latine on dit aussi *sin fines de lucro*.
- 4593 Kurzzeitpflege, 4592 Entlastungsangebot, 4586 Pflegegrad : notions du système allemand, traductions descriptives.

## Sources fautives ou qui s'écartent de l'allemand

- 4597 Hospiz : le français dit « unité de soins palliatifs » ; un Hospiz est un établissement de fin de vie
  distinct (la Palliativstation est le service hospitalier). J'ai suivi l'allemand.
- 4598 Pflegefachkraft : le français « infirmier diplômé » est masculin, le mot allemand est neutre quant au sexe ;
  rendu *el profesional de enfermería titulado*.
- 4373 : l'anglais (« no reason to linger ») paraphrase ; suivi de l'allemand.
- 4541 : « gegen unbekannt » rendu *contra desconocidos* (le français et l'anglais ne posent pas de problème).
- Aucune faute relevée dans l'allemand.

## À trancher

Vocabulaire où le Mexique et la Colombie divergent (forme retenue en premier) :

- 4385 Palette : *la tarima, el palé* (Mexique *tarima*, Colombie *estiba*).
- 4484 Beet / 4499 Hochbeet : *el cantero, la cama de cultivo* / *el cantero elevado* (Mexique *arriate*, Colombie *era*).
- 4490 Kompost : *el compost* (Mexique *la composta*).
- 4544 Dübel : *el taco de pared, el taquete* (Mexique *taquete*, Colombie *chazo*).
- 4547 Schraubzwinge : *la prensa de carpintero, el sargento*.
- 4550 Grundierung : *la capa base, la imprimación* (on dit aussi *el primer*, *el sellador*).
- 4551 Spachtelmasse : *la masilla (para resanar)*.
- 4553 Silikon : *la silicona* (Mexique *el silicón*).
- 4556 Ersatzteilliste : *la lista de repuestos* (Mexique *refacciones* ; la carte B1 dit *el repuesto, la refacción*).
- 4432 Gepäckaufgabe : *el registro de equipaje* (Mexique *documentación de equipaje* ; l'Espagne dit *facturación*).
- 4501 Anpfiff (exemple) : *el pitazo inicial* (Mexique *silbatazo*).
- 4509 / 4511 Nachspielzeit : *el tiempo añadido* (Mexique *tiempo de compensación*, Colombie *tiempo de reposición*).
- 4531 Durchsuchung : *el registro, el allanamiento* (Mexique *el cateo*).
- 4468 Versicherungsnehmer : *el tomador del seguro* (Mexique *el contratante*).
- 4471 / 4478 : *el boletín* repris de la carte B1 (Mexique *la boleta*).

À faire relire par un soignant (Pflege und Betreuung) :

- 4586 Pflegegrad *el grado de dependencia* ; 4589 Medikamentengabe *la administración de medicamentos* ;
  4592 Entlastungsangebot *el servicio de respiro (para cuidadores)* ; 4593 Kurzzeitpflege *el cuidado de corta estancia* ;
  4594 Tagespflege *el centro de día, la atención diurna* ; 4597 Hospiz *el hospicio (para enfermos terminales)*
  (*hospicio* peut évoquer un orphelinat ou un asile dans certains pays) ; 4598 Pflegefachkraft ;
  4599 Überleitung *la transferencia (de un paciente)*.
