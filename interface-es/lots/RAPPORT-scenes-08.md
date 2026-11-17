# Rapport — scenes-08 (textes des scènes, espagnol d'Amérique latine)

## Fait

- `interface-es/lots/scenes-08.es.json` : **300 textes sur 300**, contrôle `scenes_textes.py controle` → **0 faute, 1 avis**.
- L'avis : `stadtplatz¦questions¦B2 | Es ist so warm, als ob schon Sommer wäre.` « identique au français » — le texte n'est fait que d'allemand (`als ob` + `wäre`, « Konjunktiv II de sein ») ; rien à changer.
- Scènes couvertes : fin de `soins-uebergabe` (sens B2, C1, SIT), `soins-visite`, `soins-zimmer-aufstehen`, `soins-zimmer-nachttisch`, `soins-zimmer`, `sportplatz`, `stadtplatz`, début de `strand`.
- Titres de couche repris de `scenes-01.es.json` (Sustantivos y artículos ; Wo? — las preposiciones ; Suposiciones ; Relativas y participios) ; « Que faites-vous ? » → « ¿Qué hace usted? » comme dans les lots déjà rendus.
- Cas écrits comme la source : « datif / accusatif / génitif / nominatif » → dativo, acusativo, genitivo, nominativo ; Konjunktiv I / II, Präteritum, Perfekt, Partizip I gardés en allemand.

## Explications réécrites contre l'espagnol (clés)

- `soins-visite¦questions¦A2 | Haben Sie noch Schmerzen?` — le pluriel allemand opposé à « tengo dolor ».
- `soins-visite¦questions¦B1 | Die Ärztin erhöht die Dosis vom Blutdruckmittel.` et `… reduziert das Blutdruckmittel.` — « reduzieren = reducir » (mot transparent).
- `soins-visite¦questions¦C1 | Könnten Sie mir die Dosis bitte noch einmal nennen?` — « como «¿Podría…?» ».
- `soins-zimmer¦questions¦A2 | Die Hausschuhe stehen auf dem Boden.` — l'espagnol dit « están » pour stehen et liegen.
- `soins-zimmer¦questions¦A2 | Der Desinfektionsmittelspender hängt an der Wand.` — l'espagnol dit « en » pour an et auf.
- `soins-zimmer¦questions¦B2 | Das Kopfteil ist schon hochgestellt: …` et `strand¦questions¦B2 | Das Eis ist schon halb gegessen.` — passif d'état = « estar » + participio.
- `sportplatz¦questions¦B2 | Als Mark das Tor schoss, klatschte die Trainerin.` — l'espagnol dit « cuando » pour als et wenn.
- `sportplatz¦questions¦C1 | Das muss sein erstes Tor sein.`, `stadtplatz¦questions¦C1 | Sie muss den Hund lustig finden.`, `strand¦questions¦C1 | Sie muss sich im Urlaub sehr wohlfühlen.` — « como «debe de…» » (comme les lots 01-06).
- `stadtplatz¦questions¦B1 | Heute isst Anna ein Eis.` — « El español puede decir «Hoy Anna come»; el alemán no. »
- `stadtplatz¦questions¦B2 | Der Hund schaut, als ob er Hunger hätte.` et `… einen Witz erzählt hätte.` — rapprochés de « como si tuviera / como si hubiera contado ».
- `strand¦questions¦B1 | Anna ist nach Spanien geflogen.` — « donde el español siempre usa «haber» ».
- `strand¦questions¦B2 | Der Junge, dessen Ball bunt ist, spielt im Wasser.` — dessen = « cuya pelota ».

## Vocabulaire des soins retenu (à harmoniser avec scenes-07, que je n'ai pas pu lire)

- Übergabe → la entrega de turno (déjà dans les lots rendus) ; Akte → el expediente ; Hintergrund → el contexto, Vorgeschichte → antecedentes, Einschätzung → la evaluación, Empfehlung → la recomendación.
- Infusion → el suero ; Infusionsständer → el portasueros ; abhängen → retirar.
- anordnen / Anordnung → indicar / la indicación (médica) plutôt que « prescribir » (réservé en Amérique latine à l'ordonnance) ; eintragen → registrar ; ansetzen / absetzen → iniciar / suspender.
- Rollator → el andador (comme soins-altenheim) ; Klingel → el timbre ; Sichtschutz → el biombo ; Bettgitter → la baranda (de la cama) ; Nachttisch → la mesita de noche ; Bettdecke → la cobija ; Nasenbrille → la cánula nasal ; Brille → los lentes ; Hörgerät → el audífono ; Schnabelbecher → vaso con boquilla.
- « transmissions » (titre C1) → « El estilo de los registros de enfermería ».
- La médecin → la doctora (comme scenes-01). Dans les « sens », « Herr Brandt » → « el Sr. Brandt » (comme soins-altenheim) ; dans les descriptions et consignes, « Herr Brandt » et « Dr. Sommer » restent comme dans la source.

## Doutes / à trancher

- `soins-uebergabe¦sens¦C1 | Danach kommt der Hintergrund: …` — le schéma SBAR se dit en espagnol « Situación, Antecedentes, Evaluación, Recomendación » ; j'ai gardé « contexto » pour Hintergrund parce que « antecedentes » sert déjà à Vorgeschichte dans la même phrase. À aligner sur les questions de la même scène (scenes-07).
- `soins-uebergabe¦sens¦B2 | Das Kissen, auf dem der Fuß liegt, …` — « la almohada » (un coussin de positionnement ; « el cojín » possible).
- `soins-visite¦questions¦C1 | Ich wiederhole kurz: …` — « la comunicación en circuito cerrado » pour « vérification en boucle fermée » : à faire relire par un soignant.
- `soins-zimmer¦questions¦B2 | Das Bettgitter wird nur mit Einwilligung …` — « la autorización del juzgado » pour le tribunal allemand (Betreuungsgericht) ; « medida privativa de la libertad » (aussi `soins-zimmer¦questions¦C1 | Bettgitter auf Wunsch …` et `soins-zimmer-aufstehen¦questions¦SIT | Ich bleibe bei ihm …`).
- `soins-zimmer¦sens¦B1 | Setzen Sie sich bitte auf.` — « Incorpórese, por favor. » (sich aufsetzen = se redresser ; le français « Asseyez-vous » est moins précis).
- `soins-zimmer¦sens¦SIT | Ich sage sofort der verantwortlichen Pflegefachkraft Bescheid.` — « a la enfermera o al enfermero responsable ».
- `soins-zimmer-nachttisch¦sens¦C1 | Trinkmenge bis zehn Uhr: …` et les deux transmissions avec « Pat. » — abrégé « pac. » en espagnol.
- Mexique / Colombie : « lentes » (Colombie : gafas), « el basurero » (comme les lots 01-06), « la banca », « el pasto », « la cobija », « los tenis », « el portero », « atajar ».
- `stadtplatz¦sens¦B1 | Am Samstag kommen viele Leute auf den Platz.` — « El sábado » (l'allemand est au singulier ; le français dit « Le samedi », habituel).

## Sources fautives ou flottantes

- `soins-visite¦sens¦A2 | Haben Sie noch Schmerzen?`… : le français des « sens » écrit tantôt « Herr Brandt » (soins-visite), tantôt « M. Brandt » (soins-zimmer) ; l'espagnol dit partout « el Sr. Brandt ».
- `soins-zimmer¦sens¦C1 | Sauerstoffgabe über Nasenbrille, Pat. atmet ruhig, keine Atemnot.` — le français dit « patient calme » ; l'allemand dit « respire calmement » : j'ai suivi l'allemand (« pac. respira tranquilo »).
- `soins-zimmer¦sens¦B1 | Setzen Sie sich bitte auf.` — français « Asseyez-vous » pour sich aufsetzen (se redresser), voir plus haut.
- `stadtplatz¦sens¦C1 | Der Hund könnte ein Stück Eis bekommen.` — le français « aura peut-être » ; rendu « podría recibir », plus près de könnte.
- Aucune faute relevée dans l'allemand des clés.
