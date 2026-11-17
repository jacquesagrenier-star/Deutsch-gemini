# Rapport — examen-1 (Sprechen, Schreiben, Lesen) en espagnol d'Amérique latine

## Chiffres

| Source | Clés | Lot | Contrôle `textes.py` |
|---|---|---|---|
| `examen-sprechen.json` | 105 (35 consigne, 35 trad, 35 erkl) | `examen-sprechen.es.json` | 0 faute, 3 avis (« du » allemand cité) |
| `examen-schreiben.json` | 81 (27 aufgabe, 27 trad, 27 erkl) | `examen-schreiben.es.json` | 0 faute, 0 avis |
| `examen-lesen.json` | 174 (58 frage, 58 options, 58 erkl) | `examen-lesen.es.json` | 58 « fautes » = les 58 listes d'options (le contrôle n'attend que du texte) ; 1 avis (« Je » allemand cité) |

- Options vérifiées à part : 58 listes, toutes de la même longueur que la source, même ordre (la bonne réponse reste en tête).
- Pose à blanc (`poser_examen_es.py pruefung.json es …`, sans `--ecrire`) : « es : 360 champs poses, 360 encore manquants » (les manquants sont l'écoute). `pruefung.json` n'est pas modifié.

## Choix de registre

- **Usted partout où la source vouvoie** : les 35 consignes de l'oral, les 27 sujets d'écrit (« Usted le escribe a… Ordene la carta. ») et les explications qui s'adressent au candidat (« usted hizo una exposición », « le dice dónde está el matiz »). Aucune clé ne tutoie l'usager, parce qu'aucune source ne le tutoie. Si Jacques veut le tutoiement de l'app ici aussi, c'est un passage mécanique à faire sur les trois lots.
- Dans les `trad`, du → tú, Sie → usted, ihr → ustedes (« ¿Cómo lo ven ustedes? », schreiben/15 et 16).
- Perfekt → pretérito (« fui a Viena », « compré una lavadora ») ; perfecto seulement quand le présent est touché (« hasta ahora no he recibido respuesta », schreiben/12 ; « ha cambiado de fondo », sprechen/31).
- Lettres : « Estimados señores y señoras: », « Estimada señora X: », « Querida X: », « Hola, X: » ; « Atentamente, » pour *Mit freundlichen Grüßen*, « Un abrazo, » pour *Liebe Grüße*, « Saludos, » pour *Viele Grüße*.
- Genre de la personne : suivi de l'allemand ou, s'il ne tranche pas, du français (sprechen/2 « casado », sprechen/15 « preparada », schreiben/0 « enferma » — signé Amina). Tournures neutres quand c'était possible (sprechen/6 « me alegré », schreiben/3 « Les agradecería »).

## Explications réécrites contre l'espagnol

- sprechen/1 : « als Krankenpfleger » sans article — ajouté « igual que «como enfermero» en español ».
- sprechen/2 : « zur = zu der, comme « au » pour à le » → « como «al» por «a el» en español ».
- sprechen/14 : sein / haben au Perfekt — ajouté que l'espagnol n'a que « haber » (le français, lui, connaît les deux : la source ne le disait pas, mais le piège est plus grand pour un hispanophone).
- sprechen/25 : « brauchen » = « tardar », pas « necesitar » ; « sans complément d'objet » rendu par « con una duración » (plus juste : *wie lange* est bien un complément).
- sprechen/29 : présent pour le futur — « como en español ».
- schreiben/8 : « Könnten Sie » — « como «¿podrían…?» en español ».
- schreiben/18 : irréel du passé — « como «sin ti no lo habría logrado» ».
- schreiben/23 : passif impersonnel — « como «se examinarán» en español ».
- lesen/0/1 : le « faux ami » *frei* / *libre* n'en est pas un en espagnol (« entrada libre » = gratuit) : l'explication dit maintenant « como «entrada libre» », et garde l'avertissement sur « libre de elegir ».
- lesen/9/1 : « en personne, pas personnellement » — en espagnol « personalmente » veut aussi dire en personne ; réécrit en « hay que ir al café, no escribir ».
- lesen/12/1 : « telefonisch, un adverbe, pas un simple conseil » — l'opposition adverbe / conseil ne tient pas ; rendu par « es una condición, no un simple consejo ».
- lesen/14/2 : « sondern » — « como «sino» en español ».
- lesen/6/0 : « loyer froid » → « renta fría », avec « Nebenkosten (gastos adicionales) » ; lesen/17/0 : « Hauptgericht (plato fuerte) » glosé.

## Doutes

- sprechen/6 trad : « No le entendí a nadie » (Perfekt, fait fini) là où le français met l'imparfait ; « No entendía a nadie » serait aussi défendable.
- sprechen/15 trad : « zum Amt » → « a la oficina pública » ; même mot pour « administration » dans lesen/4/2, lesen/10/2 et schreiben/2. « La dependencia » (Mexique) ou « la entidad » (Colombie) sont plus locaux.
- sprechen/32 trad : « rechnerisch, nicht erlebbar » → « en los números y no en la experiencia » (libre).
- schreiben/7 : la source française dit « votre enfant » ; l'allemand dit *meine Tochter* → « a su hija ».
- schreiben/18 aufgabe : « une amie qui vous a aidé » → « que lo ayudó » (masculin générique de la source), alors que la lettre est signée Amina.
- schreiben/25 : *Bescheid* → « resolución », *Widerspruch einlegen* → « interponer un recurso », *Aktenzeichen* → « expediente » : à faire relire par quelqu'un qui connaît l'administration.
- lesen/21/2 : « Al puro comienzo » (« tout début ») est familier au Mexique et en Colombie ; « Justo al comienzo » serait plus neutre.

## Sources fautives ou flottantes

- sprechen/6 : le français dit « Je ne comprenais personne » et « J'étais quand même heureux » pour deux Perfekt (*habe verstanden*, *habe mich gefreut*) ; j'ai suivi l'allemand.
- sprechen/16 : *Dann haben alle frei* rendu en français par « Comme ça tout le monde est libre » ; l'allemand dit « ce jour-là » → « Ese día todos están libres ».
- sprechen/17 erkl : l'explication dit « je vous en confie une » alors que la réponse tutoie (*Übernimmst du*) ; gardé tel quel (« le confío otra a usted » s'adresse au candidat).
- sprechen/25 erkl : « brauchen sans complément d'objet » est inexact (voir plus haut).
- schreiben/6 trad : le français raccourcit (« Quand pourrais-je visiter ? », « un logement ») ; l'allemand répète *die Wohnung* → suivi.
- schreiben/13 trad : le français rend *Viele Grüße* par « Cordialement » ; « Saludos » en espagnol.
- schreiben/15 trad : *die Geräte* rendu « les » en français ; « los aparatos » en espagnol.
- lesen/12/1 erkl : « telefonisch, un adverbe, pas un simple conseil » (voir plus haut).

## À trancher (l'Amérique latine hésite)

- sprechen/2 : *Kindergarten* → « el jardín de niños » (Mexique) ; Colombie « jardín infantil », ailleurs « kínder ».
- sprechen/8 : *grillen / Grillfest* → « una parrillada » ; « asado » (Colombie, Cône sud), « carne asada » (Mexique).
- sprechen/9 : *Kuchen* → « un pastel » (Mexique) ; Colombie « una torta » / « un ponqué ».
- sprechen/17, lesen/2 : *Transporter* → « la camioneta » ; « rentar » (Mexique) contre « alquilar / arrendar » (Colombie) ; de même « la renta » (schreiben/16, lesen/6/0, lesen/10/0).
- schreiben/1 : *kaputt* → « descompuesta » (Mexique) ; Colombie « dañada ». *Handwerker* → « un técnico ».
- schreiben/1, 6, 10, 21 : « apartamento » (consigne) ; le Mexique dit « departamento ».
- schreiben/14 : *Pflegehelferin* → « auxiliar de enfermería » (à relire par un soignant).
- schreiben/7 : *Nussallergie* → « alérgica a las nueces » (au sens strict *Nuss* couvre plus que la noix : « frutos secos »).
- lesen/7 : *Waschküche* → « el cuarto de lavado » ; *Hausmeister* → « el conserje ».
- lesen/15 : *Abholstationen* → « estaciones de recogida » ; *die Post* → « el correo ».
- lesen/19 : *Kita* → « la guardería ».
- Heures : gardées en 24 h dans la lecture (« las 22 horas », comme l'affiche allemande que l'on lit), mais dites à l'espagnole dans les lettres traduites (« después de las 6 de la tarde », schreiben/21 et 22).
