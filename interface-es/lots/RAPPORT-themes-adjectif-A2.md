# Rapport : corpus-themes-A2-03 et corpus-adjectif-A2-01 (15 nov. 2026)

## Fait

- `lots/corpus-themes-A2-03.es.json` : **143 cartes sur 143** (thèmes A2 : Medien und Technologie,
  Einkaufen und Geld, Gefühle und Charakter, Feste und Feiertage, Politik und Gesellschaft, Umwelt,
  Farben und Formen, Zahlen und Mengen, Grundwortschatz), chacune avec `traduction` et `exemple`
  (aucun verbe ni adjectif de thème dans cette part).
- `lots/corpus-adjectif-A2-01.es.json` : **153 adjectifs sur 153** (n° 106 à 258), `traduction` et `exemple`.
- Contrôle `corpus_lots.py controle` :
  - thèmes : **143 cartes, 0 faute, 1 avis** (2486 « Suiza », nom de pays sans article : voulu) ;
  - adjectifs : **153 cartes, 0 faute, 6 avis** (147 « normal », 156 « probable », 168 « sociable » :
    mots identiques au français ou à l'anglais, justes ; doublon « necesario », voir plus bas).
- Aucune relecture par un hispanophone : tout est de ma main, en un passage. Les traductions des
  cartes sœurs déjà rendues (A1, A2-01) ont été relues pour s'aligner (el celular, la pantalla,
  la factura / la cuenta, la Pascua, el Año Nuevo, el pastel…).

## Doutes (à relire en priorité)

Thèmes
- **2107 Netz** : « Aquí la red es muy débil. » (on dirait plutôt « la señal » ; « red » gardé pour le mot).
- **2110 Apparat / 2112 Gerät** : « el aparato » / « el aparato (eléctrico), el dispositivo ».
- **2117 PC** : « la computadora, la PC ».
- **2233 Automat** : « la máquina expendedora » ; phrase « Compro el boleto en la máquina. ».
- **2240 Ermäßigung** : « la tarifa reducida, la reducción », pour ne pas doubler « el descuento » (2224 Rabatt).
- **2227 Geldbeutel / 2241 Geldbörse** : « la billetera » / « el monedero » (les deux mots allemands sont
  synonymes ; distinction un peu forcée).
- **2422 Hexe** : « Das Kind » rendu « El niño está disfrazado de bruja. ».
- **2466 Wahl** : singulier gardé (« La elección tiene lugar… ») ; l'usage dit souvent « las elecciones ».
- **2476 Gott** : carte « el dios », phrase « Ella cree en Dios. ».
- **2481 Heimat** : « la tierra natal, la patria ».
- **2484 Deutsche** : « el alemán, la alemana » (le français donne les deux genres).
- **2639 Mülltrennung** : « bei uns » rendu « Aquí ».
- **3564 Zeile** : « la línea (de texto), el renglón » (« la línea » seule est prise par Linie, autre thème).
- **3568 Chance** : « Du bekommst noch eine Chance » → « Tienes otra oportunidad. ».
- **3574 Dank** : « el agradecimiento, las gracias ».

Adjectifs
- **120 falsch** : « incorrecto, falso » ; phrase « la cuenta era incorrecta ».
- **132 klug / 228 intelligent** : « listo, inteligente » / « inteligente ».
- **141 spannend / 142 aufregend** : « apasionante, emocionante » / « emocionante » (« excitante » évité).
- **160 undeutlich / 162 unklar** : « poco claro, poco nítido » / « confuso, poco claro » ;
  160 phrase adoucie : « Su letra no es muy clara. » (l'allemand dit « ziemlich undeutlich »).
- **165 tapfer** : « valiente (ante el dolor o el peligro) », pour le distinguer de 129 mutig « valiente ».
- **174 berufstätig** : « que trabaja, con empleo » (pas d'adjectif simple).
- **188 gemein** : « cruel, malo » ; **189 böse** : « enojado, malo » (phrase « No te enojes conmigo »).
- **191 brav** : « bien portado, obediente » ; phrase « El niño se portó muy bien hoy. ».
- **196 unternehmungslustig** : « activo, con ganas de salir y hacer cosas » (pas d'équivalent court).
- **200 anstrengend** : « agotador, cansado » (« cansado » au sens mexicain de « fatigant »).
- **207 still** : phrase « En el bosque todo estaba en silencio. » (le mot de la carte n'y paraît pas).
- **211 recht** : « justo, correcto » ; la phrase est l'expression « recht haben » → « Tienes razón ».
- **224 froh, 231 nervös, 135 faul, 209 satt** : « ich » rendu au masculin, comme le français.
- **244 willkommen** : « ¡Bienvenido a Berlín! » (singulier masculin choisi ; l'allemand ne dit rien).
- **248 romantisch** : « Abend » rendu « noche ».

## Sources fautives ou curieuses

- **2231 Gold, 2232 Silber** rangés dans « Einkaufen und Geld » ; **2643 Eisen** dans « Umwelt » ;
  **2476 Gott**, **2477 Ordnung** (phrase sur une chambre rangée) dans « Politik und Gesellschaft » ;
  **2344 Stimme** dans « Gefühle » alors que 2467 emploie « Stimmen » au sens de « votes ».
- **2481 Heimat** : le français « pays d'origine » va mal avec la phrase (« … ist ein kleines Dorf »).
- **2486** : le français dit « Cet été », l'allemand « Im Sommer » (« En verano ») : j'ai suivi l'allemand.
- **115 voll** : le français dit « plein à craquer », l'allemand « sehr voll » : suivi l'allemand.
- **138 gemütlich** : le français de la phrase dit « confortable » ; rendu « acogedor ».
- **137 unsicher** : le français « incertain » ; l'allemand veut dire « peu sûr de lui » → « inseguro ».
- **209 satt** : le français contourne (« je n'ai plus faim ») ; rendu « estoy satisfecho ».
- **156, 157, 159, 218, 221, 151** : le mot est employé comme adverbe dans la phrase (carte adjectif).
- **226 geboren** : la phrase garde « Lyon » (exemple pensé pour un francophone).

## Doublons acceptés ou évités

- **152 notwendig / 153 nötig** : « necesario » pour les deux (avis du contrôle). L'espagnol n'a qu'un
  mot courant ; « preciso » aurait heurté 157 genau.
- **129 mutig / 165 tapfer** : évité par une précision entre parenthèses.
- **2224 Rabatt / 2240 Ermäßigung**, **2227 / 2241**, **2110 / 2112** : évités (voir Doutes).
- **2235 Paket** (Einkaufen) et **2731 Packung** (Zahlen) : « el paquete » dans deux thèmes différents.
- Cartes déjà rendues à l'A1 avec le même mot allemand (Handy, Bildschirm, Rechnung, Weihnachten…) :
  même traduction reprise.

## À trancher (l'Amérique latine hésite)

- **2102 Lautsprecher** : « el altavoz » ; Mexique « la bocina », Colombie « el parlante ».
- **2101 Kopfhörer** : « los audífonos » ; Cône sud « los auriculares ».
- **2118 Tablet** : « la tableta » ; beaucoup disent « la tablet ».
- **2225 Kassenbon** : « el recibo » ; Mexique « el ticket », Colombie « la tirilla ».
- **2227 Geldbeutel** : « la billetera » ; Mexique « la cartera ».
- **2230 Girokonto** : « la cuenta corriente » ; Mexique « la cuenta de cheques ».
- **2244 Einkaufswagen** : « el carrito de compras » ; Colombie « el carrito de mercado ».
- **2419 Muttertag** : « el Día de la Madre » ; Mexique « el Día de las Madres ».
- **2421 Silvester** : « la víspera de Año Nuevo » ; aussi « la Nochevieja », « el fin de año ».
- **2479 Rathaus** (phrase) : « el ayuntamiento » ; Colombie « la alcaldía », Mexique « el palacio municipal ».
- **2480 Ausweis** : « el documento de identidad » ; Colombie « la cédula », Mexique « la credencial ».
- **2485 parken** (phrase) : « estacionar » ; Colombie « parquear ».
- **2487 / 250** : « austriaco » ; « austríaco » est aussi admis.
- **2488 Visum** (phrase) : « visa » (Amérique) et non « visado ».
- **2643 Eisen** : « el hierro » ; Mexique dit aussi « el fierro ».
- **2725, 2728, 3565 Kuchen / Torte** : « el pastel », comme la part A2-01 (Colombie « la torta, el ponqué »).
- **2732 Tomaten** (phrase) : « tomates » ; Mexique « jitomates ».
- **135 faul** : « perezoso, flojo ».
- **152 Reservierung** (phrase) : « una reserva » ; Mexique « una reservación ».
- **176 Kellner** (phrase) : « el mesero » ; Cône sud « el mozo ».
- **197 gesprächig** : « conversador, hablador » ; Mexique « platicador ».
- **203 Fließband** (phrase) : « la línea de montaje » ; aussi « línea de ensamblaje », « cadena de montaje ».
- **217 amerikanisch** : « estadounidense, americano » (en Amérique latine, « americano » seul est délicat).
- **220 blond** : « rubio » ; Mexique « güero », Colombie « mono ».
- **235 Lehrer** (phrase) : « maestro » (rien ne dit l'école ; « profesor » possible).
- **240 eilig** : « apurado, urgente » ; phrase « Tengo prisa. » (Colombie « Tengo afán », Cône sud « Estoy apurado »).
- **241 Führerschein** (phrase) : « la licencia de conducir » ; Mexique « de manejar », Colombie « el pase ».
- **252 verlegen** : « avergonzado, apenado » (« apenado » = gêné au Mexique et en Colombie, « triste » ailleurs).
- **254 unhöflich** : « descortés, maleducado » (la piste « grosero » est plus forte).
- À faire relire par un soignant : **172** (embarazada), **118** (débil, après une maladie),
  **165** (valiente con el médico), **209** (satisfecho, lleno).
