# Rapport : adverbes, expressions et mots-outils A1 (15 nov. 2026)

## Fait

| Lot | Cartes | Contrôle |
|---|---|---|
| `corpus-adverbe-A1-01.es.json` | 52 / 52 | 0 faute, 0 avis |
| `corpus-redewendung-A1-01.es.json` | 68 / 68 | 0 faute, 0 avis |
| `corpus-funktionswort-A1-01.es.json` | 63 / 63 | **2 fautes, toutes deux un faux positif du contrôle** (voir ci-dessous), 0 avis |

183 cartes rendues, toutes celles des trois sources.

## Le contrôle refuse « dieciséis » (faux positif, non contourné)

Carte **#86 sechzehn** de `funktionswort` : la traduction « 16 (dieciséis) — … » et l'exemple
« A los dieciséis años no se puede manejar aquí. » sont signalés « vosotros ou forme
d'Espagne ('dieciséis') ». Le motif `\w+éis` de `VOSOTROS` (`corpus_lots.py`, ligne 41)
attrape le nombre 16, qui n'a rien d'une forme de vosotros. Je n'ai pas le droit de toucher à
l'outil, et écrire « 16 » en chiffres ou tourner la phrase autrement aurait abîmé une carte
dont le but est justement le mot « dieciséis ». J'ai donc laissé l'espagnol correct et les
deux fautes. À corriger dans l'outil : excepter `dieciséis` (et `veintiséis`, qui viendra avec
les autres nombres).

## Choix à connaître

- **Catégories des prépositions mixtes** : gardé « Wechselpräposition (Wo=Dativ,
  Wohin=Akkusativ) » tel quel, comme le français (l'anglais dit « two-way preposition »).
  Les autres : « siempre Akkusativ / Dativ », « Grundzahlen — contar », « Zehner — las
  decenas », « Números compuestos — el orden se invierte », « Ordinales — primero, segundo… »,
  « conjunción coordinante / subordinante », « pronombre … », « artículo … »,
  « determinante negativo ».
- **Perfekt → pretérito** : #7 adverbe (« llegué »), #7 et #10 expressions (« perdí tu
  llamada », « Olvidé el pan »), #67 (« ya comí »), #141 mots-outils (« abrió »).
- Vocabulaire d'Amérique : *manejar* (#62 expressions, #86 mots-outils), *boletos* (#72),
  *estacionar* (#138), *autobús*, *afuera / adentro* (#19, #20 adverbes), *allá* (#14).
- Mots cités entre «…» : « sin la s de «sechs» » (#86, #94), « sin el -en de «sieben» »
  (#87, #95).

## Doutes

Adverbes :
- #6 *Am Montag stehe ich früh auf* : rendu « El lunes… » (l'allemand est au singulier ; le
  français et l'anglais disent l'habitude, « Le lundi », « On Mondays »).
- #28 *gern* : « con gusto » pour le mot, « Me gusta tomar café » pour la phrase (l'espagnol
  n'a pas d'adverbe équivalent).
- #32 *laut*, #33 *leise* : « fuerte, con mucho ruido » / « en voz baja, sin hacer ruido ».

Expressions :
- #5 : la phrase garde le mot de la carte (« ¡Felicidades por tu cumpleaños! ») plutôt que
  « ¡Feliz cumpleaños! ».
- #13 *Ich finde* : « Me parece, opino » ; #38 *Ich denke* : « pienso » ; #12 : « Creo ».
- #43 *Müde sein* : « estar cansado » (la piste « tener sueño » dit autre chose).
- #44 *Das freut mich* : « me alegra, qué gusto ».

Mots-outils :
- #48 *von* : « El regalo es de parte de mi hermana » (« es de mi hermana » se lirait « il
  appartient à ma sœur »).
- #89 : « a las diecinueve horas » gardé pour le nombre, bien qu'on dise plutôt « a las siete
  de la noche ».
- #127 *Heute ist der fünfte Mai* : « Hoy es cinco de mayo » — l'espagnol dit la date au
  cardinal ; la traduction du mot reste « 5.º, quinto ».
- #139 *es* : « ello (sujeto impersonal, no se traduce) ».
- #151 *das* : « el, la (neutro) » — l'espagnol n'a pas d'article neutre devant un nom.
- #153 *kein* : « ningún, ninguno » ; la phrase se rend par « No tengo tiempo ».

## Source fautive ou douteuse

- **funktionswort #71 eins** : *Es ist eins nach Mitternacht* veut dire au mot à mot « une
  minute après minuit » ; le français et l'anglais disent « une heure du matin ». J'ai suivi
  le sens visé par les aides (« Es la una de la madrugada. »), mais la phrase allemande est
  à revoir (*Es ist eins in der Nacht* / *Es ist ein Uhr nachts*).
- **funktionswort #49 zu** : l'anglais « my girlfriend's place » ; l'allemand et le français
  disent « amie » → « mi amiga ».
- **adverbe #12 hier** : l'anglais retourne la phrase ; rendu d'après l'allemand (« Aquí está
  mi lugar. »).

## Doublons acceptés

Aucune traduction identique entre deux cartes d'un même fichier. Les paires voisines sont
départagées :
- *Guten Abend* (#26) « buenas noches (al llegar) » / *Gute Nacht* (#27) « buenas noches (al
  ir a dormir) » : l'espagnol n'a qu'une formule, d'où la précision.
- *Schade* (#11) « Qué lástima » / *Das ist schade* (#49) « es una lástima ».
- *Freut mich* (#30) « mucho gusto » / *Das freut mich* (#44) « me alegra, qué gusto ».
- adverbes *dann* « luego, entonces » / *danach* « después » / *später* « más tarde » /
  *also* « así que, entonces ».
- mots-outils *aus* « de / fuera de » / *von* « de / de parte de » ; *nach* « después de / a,
  hacia » / *zu* « a / a casa de » ; *in* « en, dentro de » / *an* « en / junto a (vertical) ».

## À trancher

1. **Expressions #29 Tschüss** : « chao, nos vemos ». *Chao* est courant en Colombie et en
   Amérique du Sud, moins au Mexique (« adiós », « bye », « nos vemos »).
2. **Expressions #26 Guten Abend** : « buenas noches (al llegar) » ; selon l'heure, l'Amérique
   latine dit encore « buenas tardes » à 18-19 h.
3. **Expressions #17 Wie bitte?** : « ¿Cómo?, ¿Perdón? » ; le Mexique dit « ¿Mande? », laissé
   de côté parce que propre au Mexique.
4. **Expressions #39 Ich bin dabei** : « me apunto, cuenta conmigo » (*me apunto* s'entend
   surtout au Mexique ; la Colombie dirait « ¡yo voy! », « me le mido »).
5. **Expressions #53 Einkaufen gehen** : « ir de compras, ir a hacer las compras » ; pour
   l'épicerie, le Mexique dit « ir al súper / hacer el mandado », la Colombie « hacer
   mercado ».
6. **Expressions #61 Rad fahren** : « andar en bicicleta » (Mexique, Cône sud), « montar en
   bicicleta » (Colombie) ; les deux dans la traduction, *andar* dans la phrase.
7. **Expressions #28 Auf Wiedersehen** : « adiós (formal) » ; au Mexique, « hasta luego » est
   le congé poli le plus courant, mais il sert déjà à *Bis später* (#2).
8. **Mots-outils, catégorie « Wechselpräposition »** : la garder en allemand (comme le
   français) ou l'expliquer (« preposición de doble caso ») ?
9. **Mots-outils #151 das / #139 es** : la façon de dire « neutre » et « sujet impersonnel »
   à un hispanophone (voir Doutes).
10. **Adverbe #41** : « en la noche » (Mexique, Colombie) plutôt que « por la noche ».
