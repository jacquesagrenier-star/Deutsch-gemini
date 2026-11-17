# Rapport : adverbes, expressions et mots-outils B1 (15 nov. 2026)

## Fait

| Lot | Cartes | Contrôle |
|---|---|---|
| `corpus-adverbe-B1-01.es.json` | 147 / 147 | 0 faute, 1 avis |
| `corpus-redewendung-B1-01.es.json` | 151 / 151 | 0 faute, 0 avis |
| `corpus-funktionswort-B1-01.es.json` | 46 / 46 | 0 faute, 1 avis |

344 cartes rendues, toutes celles des trois sources. Les deux avis (adverbe #261 *je*,
mot-outil #22 *umso*) viennent du « je… desto / je… umso » allemand cité exprès dans la
traduction : laissés.

Contrôle en plus (script `motsoutils-B1_doublons.py` du scratchpad) : aucune traduction B1
identique à une autre carte du même fichier, A1 et A2 compris (champ `traduction_es`).

## Choix à connaître (alignés sur l'A1 et l'A2)

- **Catégories** : libellés de l'A1-A2 repris tels quels (« conjunción subordinante /
  coordinante », « partícula modal », « siempre Dativ / Akkusativ », « Números grandes »,
  « Años », « Ordinales — primero, segundo… », « determinante indefinido »). Nouvelles :
  « siempre Genitiv », « pronombre enfático » (pronom d'insistance), « pronombre demostrativo »,
  « pronombre recíproco ».
- **Registre** : *bereits*, *stets*, *gegenwärtig* portent « (registro formal) » pour se séparer
  de *schon*, *immer*, *zurzeit* ; *drin*, *raus*, *rauf*, *wieso*, *selber* portent
  « (coloquial) ».
- **hin- / her-** (#169-#172) : « hacia adentro / afuera (alejándose de quien habla) » et
  « (hacia quien habla) » ; les phrases disent simplement « entró », « salió », « ¡Pase! ».
- **Perfekt → pretérito** (adverbes #153, #154, #158, #167, #168, #186, #190-#193, #195, #197 ;
  expressions #183, #187, #190, #195, #207…) ; pretérito perfecto gardé pour #212 (« han
  subido »), #262 (« ¿Has estado alguna vez…? ») et l'expression #243 (« Hemos tomado nota »).
- **Particules modales (#27-#35)** : la traduction décrit l'effet, comme l'A2 ; les phrases le
  rendent par « Así es y ya. », « ¡Pero si eso está claro! », « ¡Dilo y ya! ».
- **Nombres** : en lettres comme la source ; le millésime 1848 en chiffres (comme l'A2) ; les
  ordinaux dans les phrases au cardinal, seul naturel (« el siglo veintiuno », « el treinta de
  abril », « su cumpleaños número cien »).
- **Mot-outil #113 eine Milliarde** : le français signale le faux ami de l'anglais « billion » ;
  pour un hispanophone le piège est « un billón » (= *eine Billion*) : rendu « mil millones — no
  es «un billón» ».
- **Expression #206 Kompromiss** : faux ami de « compromiso » ; rendu « encontrar un punto
  medio, llegar a un arreglo ».
- Vocabulaire d'Amérique : *el carro*, *el celular*, *la renta*, *el apartamento*, *el
  estacionamiento*, *medio tiempo*, *tomar vacaciones*, *horas extras*, *llenar una solicitud*,
  *chao*, *acá*, « no te apures ».

## Doutes

Adverbes :
- #159 *zunächst* : « antes que nada, en un primer momento » (pour ne pas répéter « primero »
  de *zuerst*).
- #160 *mittlerweile* : « a estas alturas, ahora ya » (*inzwischen*, A2, a pris « mientras
  tanto »).
- #164 *nachts* : « de noche, durante la noche » (l'A2 dit « en las noches » pour *abends*).
- #196 *gezielt* : « específicamente, de manera dirigida ».
- #201 : « Subió la escalera a duras penas. » (*hochgeschleppt*, « s'est traîné », n'est pas
  rendu mot à mot).
- #215 *knapp* « con lo justo, por muy poco » / #273 *beinahe* « casi, por poco » (A1 *fast*
  « casi », A2 *kaum* « apenas, casi no »).
- #223 : « tocó mal » — *gespielt* après *geübt* lu comme un instrument ; ce pourrait être un
  match (« jugó mal »).
- #232 *nämlich* : « es que (da la razón); a saber ».
- #235 *immerhin* « al menos eso, algo es algo » / #236 *zumindest* « cuando menos » ; les
  phrases disent « al menos » et « por lo menos », plus naturels.
- #239 *ebenfalls* : traduction « asimismo, de igual modo », phrase « también ».
- #241 : *Nebenkosten* rendu « los gastos adicionales » (à aligner sur le thème du logement).
- #251 *erst* : « no antes de, apenas, solo » ; phrase « El tren no llega hasta las ocho. »
- #253 *Tasche* : « el bolso ».
- #274 *dahin* : « hasta ahí, hasta entonces » (la phrase est *bis dahin*).
- #285 *circa* : « unos, como (cantidad aproximada) » (A2 : *ungefähr*, *etwa*).
- #287 : *Schönen Abend!* rendu « ¡Que pases una linda noche! ».
- #291 *voraus* : « por adelantado, por delante », phrase « de antemano ».

Expressions :
- #169 : « En la reunión se trata del nuevo presupuesto. » (correct, un peu raide).
- #172 *Frührentner* : « Está jubilado anticipadamente ».
- #174 *unter Umständen* : « dado el caso, según las circunstancias ».
- #184 *beim Amt* : « en la oficina pública ».
- #186 *sich freuen auf* : « esperar con ilusión, tener muchas ganas de (algo que viene) ».
- #209 *Verein* : « asociación » ; « Bienvenido » au masculin singulier.
- #228 : « Por favor, encárguese de que haya silencio en la sala. » (*Sie* lu au singulier).
- #255 *Nicht zuletzt* : « en buena medida, y no en último lugar ».
- #264 : « Ni bajo presión pierde ella la cabeza. »
- #280 *Den Überblick behalten* : « llevar el control, no perder la visión de conjunto ».
- #296 *Lass von dir hören* : « da señales de vida, no te pierdas ».
- #299 *Man sieht sich* : « ya nos veremos, nos vemos por ahí ».
- #312 : « Ella pagó el viaje de su propio bolsillo. » (l'allemand : « elle a voyagé à ses
  frais »).

Mots-outils :
- #20 *solange* : « mientras (todo el tiempo que), en tanto que » ; phrase à l'indicatif
  (habitude) : « Mientras hay luz… ».
- #21 *indem* : « gerundio (-ando, -iendo), al + infinitivo: indica el medio » (pas de mot
  espagnol équivalent).
- #23 *soviel* : « hasta donde (yo sé), por lo que (sé) ».
- #30 *schon* : « ¡Claro que lo vas a lograr! ».
- #32 *eigentlich* : « Por cierto, ¿tú qué haces? ».
- #67 : « El precio es válido con las bebidas incluidas. »
- #114 : « por centenas: «dieciocho cientos» cuarenta y ocho » (explication de la forme
  allemande, comme l'A2 #115).
- #147 *im selben Haus* : « en la misma casa » (« el mismo edificio » si *Haus* est un immeuble).

## Source fautive ou douteuse

- **adverbe #187 jeweils** : le français « chaque lundi » efface *jeweils* ; rendu « tiene lugar
  cada lunes ».
- **adverbe #258 inklusive, #278 gegenüber, #295 minus, #296 plus, #289 netto** : prépositions
  ou adjectifs rangés dans les adverbes ; *gegenüber* est aussi dans les mots-outils (#52), avec
  presque la même phrase.
- **adverbe #288 los** : le mot seul (« allons-y ») et la phrase (*Was ist los?*) n'ont pas le
  même sens ; les deux sont dans la traduction.
- **adverbe #261 je / mot-outil #22 umso** : même phrase allemande à un mot près (*desto* /
  *umso*) ; même phrase espagnole.
- **adverbe #240 ebenso / #256 genauso** : même phrase type (« Der zweite … war ebenso /
  genauso … ») ; les deux phrases espagnoles disent « igual de ».
- **redewendung #177 / #318** (*eine Rolle spielen* / *Keine Rolle spielen*) : deux cartes, et
  la phrase de #177 est déjà à la forme négative (*spielt keine Rolle*).
- **redewendung #176 / #260** (*mit anderen Worten* / *Anders gesagt*), **#171 / #250**
  (*einerseits… andererseits* / *Zum einen… zum anderen*), **#194 / #284** (*sich Zeit nehmen* /
  *lassen*) : même français deux fois (« autrement dit », « d'une part… d'autre part »,
  « prendre son temps »).
- **redewendung #303 Sich Gedanken machen über** : le français « se faire du souci » est celui
  de #185 *sich Sorgen machen* ; l'allemand dit plutôt « réfléchir, se poser des questions » :
  rendu « darle vueltas a, pensar mucho en ».
- **redewendung #273** : *Antrag* rendu « formulaire » en français, « solicitud » ici (comme
  #184).
- **redewendung #317 Hand anlegen** : la phrase dit *mit angelegt* sans *Hand* (« Alle haben
  mit angelegt. ») ; attendu : « Alle haben mit Hand angelegt. »
- **redewendung #213** : tiret « – » dans la source, « — » dans l'adverbe #287 ; recopiés tels
  quels.
- **mot-outil #10 bevor** : phrase rendue par l'infinitif (« antes de venir »), la conjonction
  « antes de que » n'y paraît pas ; même chose pour #11 *nachdem*.
- **mot-outil #136** : le français « le trentième jour d'avril » est forcé ; rendu « El treinta
  de abril ».
- **mot-outil #147 derselbe** : la phrase montre *im selben*, pas *derselbe*.

## Doublons acceptés

Aucune traduction identique entre deux cartes d'un même fichier (A1-A2 compris). Paires
voisines départagées :
- *schon* « ya » / *bereits* « ya (registro formal) » ; *immer* / *stets* « siempre (registro
  formal) » ; *zurzeit* « actualmente, por ahora » / *gegenwärtig* « en la actualidad (registro
  formal) ».
- *ständig* « constantemente, todo el tiempo » / *dauernd* « sin parar, a cada rato » / *immer
  wieder* « una y otra vez ».
- *ab und zu* (A2) « de vez en cuando » / *gelegentlich* « ocasionalmente, en ocasiones ».
- *vorsichtig* (A2) « con cuidado » / *sorgfältig* « cuidadosamente, con esmero ».
- *äußerst* « extremadamente » / *überaus* « sumamente, en extremo ».
- *einigermaßen* « hasta cierto punto, medianamente » / *halbwegs* « a medias, más o menos ».
- *total* (A2) « totalmente » / *ganz* (A2) / *völlig* « por completo, absolutamente ».
- *folglich* « por consiguiente » / *somit* « por ende, con ello » / *infolgedessen* « como
  consecuencia, a raíz de ello » / *demnach* « según eso » / *dementsprechend* « en
  consecuencia » / *daraufhin* « a raíz de eso, tras lo cual » : l'espagnol n'a pas six mots
  bien distincts.
- *sonst* (A2) « si no, de lo contrario » / *andernfalls* « en caso contrario » / *ansonsten*
  « por lo demás, aparte de eso ».
- *trotzdem* (A2) « aun así, de todos modos » / *dennoch* « no obstante » / *jedoch* « sin
  embargo » / *allerdings* « eso sí, aunque ».
- *außerdem* (A2) « además » / *zudem* « además de eso, adicionalmente ».
- *dafür* (A2) « en cambio, para eso » / *hingegen* « por el contrario » / *dagegen* « en cambio
  (por contraste); en contra ».
- *auch* « también » / *ebenfalls* « asimismo, de igual modo » / *ebenso* « de igual manera,
  tan … como » / *genauso* « exactamente igual, igual de » / *gleichfalls* « igualmente (al
  devolver un deseo) ».
- *warum* « por qué » / *wieso* « cómo es que, por qué (coloquial) » / *weshalb* « por qué
  motivo, por qué razón ».
- *worüber* « sobre qué, de qué » / *worum* « de qué (se trata), acerca de qué ».
- *wenigstens* (A2) « por lo menos, al menos » / *immerhin* / *zumindest* (voir Doutes).
- *wieder* « otra vez, de nuevo » / *nochmals* « nuevamente, una vez más ».
- *drinnen* « adentro » / *innen* « por dentro, en el interior » / *drin* « dentro, adentro
  (coloquial) » ; *draußen* « afuera » / *außen* « por fuera » / *raus* « afuera, para afuera
  (coloquial) ».
- Expressions : *Bescheid sagen* (A2) « avisar » / *Bescheid geben* « dar aviso, informar »
  (même sens, l'espagnol n'a qu'« avisar » : la phrase dit « Avísame ») ; *Auf der einen Seite*
  (A2) « por un lado » / *einerseits… andererseits* « por una parte… por otra » / *Zum einen…
  zum anderen* « por un lado ... por otro » ; *Bescheid wissen* (A2) « estar al tanto » / *auf
  dem Laufenden bleiben* « mantenerse al corriente » / *auf dem neuesten Stand* « actualizado,
  al día » ; *Sich beteiligen an* « tomar parte en » / *Teilnehmen an* « participar en » ;
  *Sich kümmern um* (A2) « ocuparse de » / *Sich beschäftigen mit* « dedicarse a » / *Sorgen
  für* « encargarse de » ; *Angst haben* (A1) « tener miedo » / *Sich fürchten vor* « tenerle
  miedo a, temer » ; *Ohne Zweifel* (A2) / *Mit Sicherheit* « con toda seguridad » / *Das steht
  außer Frage* « eso está fuera de duda » ; *Das finde ich auch* (A2) / *Das sehe ich genauso*
  « yo lo veo igual » ; *Tschüss* (A1) « chao, nos vemos » / *Man sieht sich* « ya nos veremos ».
- Mots-outils : *während* conjonction « mientras » / *solange* « mientras (todo el tiempo
  que), en tanto que » / *während* préposition « durante » ; *wenn* (A1) « si, cuando… » /
  *ob* « si (pregunta indirecta) » / *falls* « en caso de que, si » ; *bis* préposition
  « hasta » / conjonction « hasta que » ; *in* « en, dentro de » / *innerhalb* « dentro de, en
  un plazo de » ; *durch* « a través de, por » / *per* « por (medio de envío o de transporte) » ;
  *selbst* « yo mismo, uno mismo; incluso » / *selber* « uno mismo (coloquial) ».

## À trancher

1. **Adverbe #261 / mot-outil #22** : « Mientras más se practica, mejor sale. » *Mientras
   más* est courant dans toute l'Amérique ; le Mexique et la Colombie disent aussi « entre
   más » ; la norme écrite préfère « cuanto más » (donné en second dans la traduction).
2. **Adverbe #251 erst** : « recién » (Amérique du Sud) écarté ; le Mexique dirait « no llega
   sino hasta las ocho ».
3. **Adverbe #176** : *Ausweis* « mi identificación » (comme l'A2 #75 ; Colombie : « la
   cédula »).
4. **Adverbe #180 rückwärts** : « en reversa » (Mexique, Colombie) ; le Sud dit « marcha
   atrás » (donné en second).
5. **Adverbe #198 Lehrer** : « el maestro » (niveau scolaire non précisé) ; expression #319
   *Direktorin* « la directora ».
6. **Adverbe #257 halbtags** : « medio tiempo » (Mexique, Colombie) / « media jornada ».
7. **Expression #214 Sich bewerben um** : « postularse a, solicitar (un puesto) » ; la
   Colombie dit beaucoup « aplicar a », le Mexique « solicitar empleo ».
8. **Expression #274 Sich krankmelden** : « reportarse enfermo » (Mexique) ; ailleurs « avisar
   que uno está enfermo », « presentar incapacidad » (Colombie), « dar parte de enfermo »
   (Sud) — à relire par un soignant, c'est son quotidien.
9. **Expression #271 Jemandem peinlich sein** : « darle vergüenza a alguien » ; « darle pena »
   (Mexique, Colombie) écarté pour son double sens, comme à l'A2.
10. **Expression #263 Sich Mühe geben** : « esforzarse, echarle ganas » (*echarle ganas* est
    surtout mexicain).
11. **Expression #283 Auf Nummer sicher gehen** : « ir a la segura » (Mexique : « irse a la
    segura » ; Colombie : « ir a la fija »).
12. **Expression #188 / #189** : « estar hasta la coronilla », « sacar de quicio » — compris
    partout, mais chaque pays a son familier.
13. **Expression #190 Stau** : « no hubo tráfico » (« trancón » en Colombie,
    « embotellamiento » ailleurs).
14. **Expression #235 Praktikum** : « las prácticas » (Mexique : aussi « la pasantía » /
    « el servicio »).
15. **Expression #299** : « chao » (comme l'A1 pour *Tschüss*).
16. **Mot-outil #28 wohl** : « Eso debe de ser cierto. » (Mexique : « Ha de ser cierto. »).
17. **Mot-outil #136** : « día feriado » (Mexique : aussi « día festivo », Colombie : « festivo »).
