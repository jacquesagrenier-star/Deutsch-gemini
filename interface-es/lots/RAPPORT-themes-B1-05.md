# Rapport : corpus-themes-B1-05 (15 nov. 2026)

## Fait

- `interface-es/lots/corpus-themes-B1-05.es.json` : **240 cartes sur 240** (traduction + exemple), n° 2192 à 2598.
  Thèmes : Medien und Technologie (5), Einkaufen und Geld (64), Gefühle und Charakter (44),
  Feste und Feiertage (20), Politik und Gesellschaft (107).
- Contrôle `corpus_lots.py controle` : **0 faute, 3 avis** (noms sans article, voulus : *Pentecostés*,
  *Turquía*, *Ucrania*, comme *Suiza* déjà posé).
- Doublons vérifiés à la main contre les `traduction_es` de `themes.json` et contre les lots
  B1-03 / B1-04 des mêmes thèmes (lecture seule) : aucun mot allemand différent ne porte la même réponse.

## Précisions ajoutées pour départager (le mot déjà pris est entre crochets)

- 2245 Quittung → *el comprobante de pago, el recibo* [Kassenbon = el recibo]
- 2253 Sonderangebot → *la oferta especial* ; 2276 Aktion → *la promoción* [Angebot = la oferta]
- 2283 Kauf → *la compra (adquisición)* [Einkauf = la compra]
- 2271 Lieferant → *el proveedor* ; 2275 Anbieter → *el proveedor (de un servicio)*
- 2295 Bancomat → *el cajero automático (en Suiza y Austria)* [Geldautomat = el cajero automático]
- 2294 EC-Karte → *la tarjeta de débito* ; 2307 Bankomat-Karte → *la tarjeta bancaria (en Austria)*
- 2297 Brieftasche → *la cartera (para billetes y documentos)* ; 2301 Portemonnaie → *el portamonedas*
  [Geldbeutel = la billetera, Geldbörse = el monedero]
- 2279 Gebühr → *el cargo, la tasa* ; 2303 Beitrag → *la cuota, la aportación* ; 2305 Tarif → *la tarifa*
- 2195 Mailbox → *el buzón de voz* ; 2196 Mobilbox → *el buzón de voz (del celular)*
- 2355 Furcht → *el temor* [Angst = el miedo] ; 2354 Gelassenheit → *la serenidad* [Ruhe = la calma]
- 2351 Zuversicht → *la confianza, el optimismo* ; 2353 Selbstvertrauen → *la confianza en sí mismo*
- 2438 Fasching → *el carnaval (en el sur de Alemania y Austria)* ; 2444 Fasnacht → *el carnaval (en Suiza
  y el suroeste de Alemania)* [Karneval = el carnaval]
- 2439 Glückwunsch → *las felicitaciones* ; 2440 Gratulation → *la felicitación*
- 2432 Geist → *el espíritu, el fantasma* ; 2434 Gespenst → *el fantasma*
- 2426 Hochzeit → *la boda* ; 2445 Trauung → *la ceremonia de matrimonio*
- 2505 Recht → *el derecho* ; 2509 Anspruch → *el derecho (a recibir algo), la pretensión*
- 2498 Befehl → *la orden* ; 2496 Gesellschaftsordnung → *el orden social* [Ordnung = el orden]
- 2596 Genehmigung → *el permiso (oficial), la aprobación* [Erlaubnis = el permiso, la autorización]
- 2584 Personenstand → *el estado civil* ; 2593 Zivilstand → *el estado civil (en Suiza)*
- 2517 Antrag *la solicitud* / 2538 Anliegen *la petición, el asunto* / 2558 Aufforderung *el requerimiento* /
  2563 Forderung *la exigencia, la demanda* / 2564 Förderung *la subvención, el apoyo económico* /
  2521 Unterstützung *el apoyo*
- 2510 Einbrecher → *el ladrón (que entra a robar a una casa)* ; 2511 Einbruch → *el robo (a una casa)*
  (l'espagnol d'Amérique n'a pas de mot courant propre au cambriolage)

## Doublons acceptés

Aucun dans le thème. Entre thèmes (permis) : *la costumbre* pour Gewohnheit (2359, avec *el hábito*) et
Brauch (2429).

## Doutes

- 2301 Portemonnaie → *el portamonedas* : mot juste mais moins courant que *el monedero* (déjà pris par Geldbörse).
- 2385 Gedanke : l'exemple « Ich mache mir Gedanken über die Prüfung » est une tournure figée ; rendu
  « Me preocupa el examen. » : le mot *pensamiento* n'y paraît pas (comme *pensée* n'est pas dans le français).
- 2386 Mühe : « ¡Gracias por tomarte la molestia! » (plutôt que *esfuerzo*).
- 2391 Ehre : « conocerlo » (usted, genre non dit par l'allemand ; masculin par défaut).
- 2435 Narr : « En el carnaval todos son bufones. » (le *Narr* du carnaval rhénan n'a pas d'équivalent).
- 2536 Migrationshintergrund → *el origen inmigrante* (on lit aussi *antecedentes migratorios*).
- 2551 Kriminalpolizei → *la policía criminal* (calque ; *policía judicial / de investigación* selon le pays).
- 2556 / 2558 Amt → *la oficina pública* (Mexique : *la dependencia* ; neutre gardé).
- 2564 « vom Land » → *del estado federado*.
- 2543 « im 19. Jahrhundert » → *en el siglo XIX* (chiffres romains, usage espagnol).
- 2258 « rund um die Uhr » → *a toda hora*.

## Sources fautives ou à regarder

- 2290 Schein : « Haben Sie es kleiner? Ich habe nur einen großen Schein. » : les deux phrases ne sont pas
  du même locuteur (la caissière demande, le client répond) ; le français « Vous avez de la monnaie ? » s'écarte
  de l'allemand. Rendu d'après l'allemand : « ¿Tiene algo más pequeño? Solo tengo un billete grande. »
- 2302 Schuld : fr « faute ; dette », mais le thème est « Einkaufen und Geld » et l'exemple illustre la faute
  (« Das ist nicht deine Schuld »), pas la dette. Rendu *la culpa, la deuda*, exemple suivi tel quel.
- 2503 Opfer / 2576 Tote : deux exemples presque identiques (« Bei dem Unfall gab es … keine Opfer / Toten »).
- 2253 / 2276 : même phrase d'exemple pour Sonderangebot et Aktion.
- 2565 / 2580 : même phrase d'exemple pour Konsulat et Botschaft.
- 2571 Politiker : fr « homme politique » ; rendu *el político* (neutre).
- 2530 fr « mairesse » (québécisme) : sans effet sur l'espagnol (*la alcaldesa*).

## À trancher (l'Amérique latine hésite)

- 2266 Taschengeld → *la mesada, el dinero de bolsillo* (Mexique : *el domingo* ; Colombie, Cône sud : *la mesada*).
- 2273 Schaufenster → *la vitrina, el aparador* (Colombie / Amérique du Sud : *vitrina* ; Mexique : *aparador* ;
  la piste *el escaparate* est d'Espagne et du Mexique soutenu).
- 2250 Ratenzahlung → *el pago a plazos, el pago en cuotas* (Mexique : *a meses / a plazos* ; Colombie : *a cuotas*).
- 2248 Reklamation → *la reclamación, el reclamo* (Mexique : *reclamación* ; Amérique du Sud : *reclamo*).
- 2261, 2277, 2278 : *la renta* pour Miete (suit les consignes et les cartes déjà posées ; Colombie : *el arriendo*).
- 2550 Geburtsurkunde → *el acta de nacimiento, la partida de nacimiento* (Mexique : *acta* ; Colombie : *registro
  civil de nacimiento* ; ailleurs : *partida*).
- 2522 Bescheinigung → *la constancia, el certificado* (*constancia* très mexicain et colombien ; ailleurs *certificado*).
- 2306 Verfallsdatum → *la fecha de vencimiento, la fecha de caducidad* (Mexique : *caducidad*).
- 2287 Mehrwertsteuer → *el IVA (impuesto al valor agregado)* (Colombie dit aussi *valor agregado* ; Espagne *añadido*).
- 2443 Buffet → *el bufé, el buffet* (les deux graphies circulent).
- 2529 Rathaus dans l'exemple → *la alcaldía* (carte déjà posée : *la alcaldía, el ayuntamiento*).
