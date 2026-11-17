# Rapport — corpus-themes-C1-03 (15 nov. 2026)

## Fait

- `corpus-themes-C1-03.es.json` : **240 cartes** C1 (n° 4132 à 4371), 240 traductions + 240 exemples.
- Contrôle `corpus_lots.py controle` : **240 cartes, 0 faute, 0 avis**.
- 16 thèmes : Natur (1 carte, Heide), Sicherheit und Krisen, Konsum und Handel, Bühne/Text/Klang,
  Erziehung und Kindheit, Landwirtschaft und Boden, Körperteile, Wetter, Handwerk und Material,
  Meer und Küste, Alter und Abschied, Küche und Kochen, Kleidung, Dienstleistung und Kundschaft,
  Glaube und Sinn, Stadt und Gebäude (7 premières cartes ; la suite du thème est dans un autre lot).
- Comparé aux niveaux A1-B2 des mêmes thèmes (`traduction_es` de `themes.json`) et à Moor (C1-02) :
  aucune réponse identique pour deux mots allemands différents.

## Départages (précision ou mot distinct, à cause d'un voisin du même thème)

- 4365 Stadtviertel « el barrio (de una ciudad) » — Quartier (B1) = « el barrio », Wohnviertel (A2) = « el barrio residencial ».
- 4371 Gehweg « la acera, la vereda » — Bürgersteig (B1) = « la acera ».
- 4369 Aufwertung « la revalorización » — Gentrifizierung (B2) = « la gentrificación » (le français donnait aussi « gentrification »).
- 4318 Gewebe « el tejido » — Stoff (B1) = « la tela ».
- 4243 Luftfeuchtigkeit « la humedad del aire » — Feuchtigkeit (B1) = « la humedad ».
- 4241 Hagelschauer « la granizada » — Hagel (A2) = « el granizo ».
- 4267 Brandung « la rompiente, las olas que rompen » / 4270 Seegang « el oleaje, el estado del mar ».
- 4250 Verarbeitung / 4252 Feinschliff / 4258 Nachbearbeitung : « el acabado, la elaboración » / « el pulido final, los últimos retoques » / « el retoque, el trabajo posterior ».
- 4336 Bereitschaft « la guardia, la disposición » / 4340 Erreichbarkeit « la disponibilidad (para ser contactado) ».
- 4335 Serviceleistung « el servicio (prestado) » / 4345 Zusatzleistung « el servicio adicional ».
- 4195 Entwicklungsschritt « el paso del desarrollo » (pour laisser « etapa » à 4186 Trotzphase).

## Doublons acceptés

Aucun.

## Doutes (à relire)

- 4150 Schutzsuchende : la source donne `genre: die`, pluriel identique, et un sens pluriel en fr/en ; rendu au pluriel « las personas que buscan protección ».
- 4137 Waffenstillstand : « el cese al fuego » (suit le français « cessez-le-feu ») ; au sens strict, « el armisticio ».
- 4183 Nachspiel : « las consecuencias, la secuela » (sens figuré de l'exemple ; le sens musical « postludio » n'est pas donné).
- 4203 Weidewirtschaft : « la ganadería de pastoreo » (plutôt que « economía pastoril »).
- 4255 Vorrichtung : « el dispositivo, el montaje » (le « jig » d'atelier n'a pas de mot commun).
- 4263 Gewinde, exemple : « La rosca está barrida » (courant au Mexique et en Colombie ; ailleurs « pasada », « robada »).
- 4275 Seenot : « el peligro en el mar » (pas de nom espagnol établi ; « in Seenot geraten » rendu « verse en peligro en el mar »).
- 4280 Wattenmeer : « el mar de Wadden, la llanura de mareas » (on dit aussi « mar de Frisia »).
- 4306 Teigführung : « el proceso de la masa (reposo y fermentación) » — terme de boulangerie sans équivalent court.
- 4310 Einkochen : « la elaboración de conservas (en frascos) » ; exemple rendu par « Hacer conservas… ».
- 4317 Bündchen : « el puño elástico, el resorte ».
- 4340 Erreichbarkeit, exemple : « La atención telefónica termina… » (plus naturel que « la disponibilidad telefónica »).
- 4348 Andacht : « el oficio breve, el recogimiento ».
- 4370 Straßenzug : « el tramo de calle (con sus edificios) ».

## Sources fautives ou écarts fr / en

- 4148 : l'allemand « war zwei Jahre lang bekannt » = connue **pendant** deux ans ; le français dit « depuis deux ans ». Suivi l'allemand.
- 4143 : « nach zwölf Minuten » = au bout de douze minutes ; le français dit « en douze minutes ». Suivi l'allemand (« a los doce minutos »).
- 4159 : le français abrège (« Fidéliser coûte moins cher que conquérir ») ; l'espagnol garde « clientes nuevos ».
- 4323 : l'allemand « nach dritter Wäsche » (sans article, style télégraphique) ; rendu « después de la tercera lavada » (le français dit « après trois lavages »).
- 4350 : « sprach » rendu à l'imparfait d'habitude (« decía una oración »), comme le français ; un fait unique (« dijo ») est aussi possible.
- 4354 : « führt über achtzig Kilometer » rendu « recorre ochenta kilómetros » (parcours de 80 km, pas « plus de »).

## À trancher (l'Amérique latine hésite)

- 4186 Trotzphase : « la etapa de los berrinches » (Mexique, Colombie comprend ; Colombie dit aussi « pataletas »).
- 4161 Kindergarten dans l'exemple : « jardín infantil » (Colombie, Chili) ; Mexique : « jardín de niños / kínder ».
- 4163 Verpackungsmüll : « los residuos de empaques » (Espagne : « envases »).
- 4217 Muskelkater : « el dolor muscular (después del ejercicio) » — « agujetas » écarté (Espagne ; au Mexique, ce sont les lacets).
- 4228 / 4229 : « ruptura » de tendón / de ligamentos (Espagne : « rotura ») — **à relire par un soignant**.
- 4218 Verspannung « la contractura, la tensión muscular », 4223 Körperspannung « la tensión corporal, el tono muscular », 4227 Überlastung « la sobrecarga » — à relire par un soignant.
- 4283 Pflegeheim « el hogar de ancianos (con cuidados) » (Mexique : « asilo », Colombie : « hogar geriátrico »), 4284 Betreuungskraft « el cuidador, la cuidadora », 4285 Patientenverfügung « la voluntad anticipada (documento) » (Espagne : « testamento vital ») — à relire par un soignant.
- 4234 / 4235 : « zona de alta / baja presión » (« borrasca » écarté, Espagne).
- 4293 : « años de cotización » (Colombie : « semanas / años cotizados », Cône sud : « aportes »).
- 4333 Kostenvoranschlag : « la cotización, el presupuesto ».
- 4338 Beschwerdemanagement : « la gestión de reclamos » (Mexique dit aussi « quejas » ; Espagne « reclamaciones »).
- 4344 Selbstbeteiligung : « el deducible » (Espagne : « franquicia »).
- 4366 Grünfläche : « el área verde » (Espagne : « zona verde », aussi courant en Colombie).
- 4367 Verkehrsberuhigung : « la pacificación del tráfico » (aussi « del tránsito »).
- 4371 : « cochecitos de bebé » (Mexique : « carriolas » ; Colombie : « coches »), et « vereda » comme second sens (Cône sud, Pérou ; en Colombie, « vereda » est un hameau, « andén » le trottoir ; Mexique : « banqueta »).
- 4312 Speisenfolge : « el orden de los platos » (Mexique : « platillos »).
