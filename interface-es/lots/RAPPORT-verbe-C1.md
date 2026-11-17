# Rapport — verbes C1 (corpus-verbe-C1-01 et -02)

## Fait

- `corpus-verbe-C1-01.es.json` : 240 verbes (n 1042 à 1281), 5 champs chacun → **0 faute, 0 avis**.
- `corpus-verbe-C1-02.es.json` : 32 verbes (n 1282 à 1313) → **0 faute, 0 avis**.
- 272 traductions + 1 088 phrases. Écrit en cinq passes (60 + 60 + 60 + 60 + 32), assemblées par
  script (scratchpad `verbe-C1_fusion.py`), qui vérifie aussi `mot` recopié et les doublons.
- Doublons : **aucune réponse identique** entre deux verbes C1, ni avec les 1 042 `traduction_es`
  des niveaux A1-B2 de `verbe.json` (comparaison de la réponse entière).
- Temps : Perfekt → pretérito, sauf sens lié au présent (1127 « han ratificado », 1154 « todavía no
  se han revisado », 1186, 1219, 1236-1238, 1240) ; passifs « ist … worden » → « se + pretérito »
  ou « fue + participe » ; Präteritum → pretérito ou imperfecto selon le sens ; Konjunktiv II →
  conditionnel. Registre soutenu gardé (ratificar, consagrar, incumbir, revestir, encomendar).

## Paires proches départagées (pas de doublon, mais à connaître)

- negar : 1089 leugnen « negar » / 1061 abstreiten « negar, rechazar (una acusación) » / 1090 dementieren « desmentir (oficialmente) ».
- deducir : 1046 folgern « concluir, inferir » / 1047 ableiten « derivar, deducir » / 1058 herleiten « deducir, demostrar (paso a paso) ».
- amortiguar : 1067 auffangen « absorber, amortiguar (un golpe) » / 1068 abfedern « amortiguar, paliar ».
- amonestar : 1102 ermahnen / 1125 abmahnen / 1151 verwarnen / 1152 mahnen (quatre formulations distinctes).
- aprobar : 1073 genehmigen « autorizar, aprobar » / 1199 bewilligen « aprobar, asignar (fondos, un permiso) » / 1202 billigen « aprobar, dar el visto bueno a ».
- sancionar : 1204 ahnden « castigar, penalizar (una infracción) » / 1205 sanktionieren « sancionar » ; 1076 auferlegen / 1077 verhängen.
- ocultar : 1081 verschweigen, 1114 vertuschen, 1115 verschleiern, 1116 kaschieren, 1233 tarnen, 1105 vorenthalten.
- 1309 umschreiben « describir con otras palabras, decir con un rodeo » / 1310 paraphrasieren « parafrasear ».
- 1120 durchhalten / 1293 durchstehen / 1294 überstehen / 1296 verkraften / 1295 wegstecken.
- 1165 umschichten « reasignar, redistribuir » / 1197 umwidmen « destinar a otro uso, reconvertir » / 1271 zuweisen / 1272 zuteilen / 1269 abstellen.
- 1189 pauken « estudiar duro, memorizar (coloquial) » / 1190 büffeln « matarse estudiando (coloquial) » : quasi-synonymes en allemand.

## Doutes (à relire)

- 1049 (konjunktiv2) : « Ich würde es nicht so zuspitzen » rendu « Yo no lo plantearía de forma tan tajante » (sens transitif, différent de l'entrée pronominale).
- 1082 (praeteritum) : « Sie beschönigte den Aufwand » → « Ella maquillaba el esfuerzo necesario ».
- 1088 : beteuern (« proclamar su inocencia », « asegurar ») ; konjunktiv2 « yo no lo aseguraría tanto ».
- 1154 (praeteritum) : « das Wrack » rendu « los restos » (épave de bateau ou d'avion, non précisé).
- 1185 : mitfühlen n'a pas de verbe simple naturel en espagnol (« Comparto lo que sientes »).
- 1208 (perfekt) : « ist diskret angebahnt worden » → « Se preparó discretamente un encuentro ».
- 1220 (praeteritum) : « drei Meister » gardé ambigu, « tres maestros » (le français dit « champions »).
- 1225 (praeteritum) : « der Ofen » → « el horno » (poêle de chauffage ; « la estufa » est la cuisinière dans les consignes).
- 1240 : gleichziehen (« empata », « ponerse a la par »).
- 1265 : mitgestalten (« contribuir a dar forma a »).
- 1297 (konjunktiv2) : « mit links » → « con los ojos cerrados ».

## Sources fautives ou bancales

- 1049 `sich zuspitzen` : le français de l'entrée (« exacerber, radicaliser ») est transitif, l'entrée est pronominale ; le konjunktiv2 emploie le verbe transitif.
- 1052 `sich abschwächen` : même chose (« atténuer, affaiblir ») ; l'exemple et le konjunktiv2 emploient « abschwächen » transitif.
- 1208 `sich anbahnen` : le perfekt est un passif du verbe transitif (« ist … angebahnt worden »).
- 1083 : l'`exemple` est au Präteritum (« Ein Satz genügte… »), pas au présent.
- 1232 et 1233 : le champ `perfekt` porte un passif d'état au Präteritum (« war gefälscht », « war getarnt »), pas un Perfekt.
- 1296 (exemple) : le français met un conditionnel (« serait insupportable »), l'allemand un indicatif ; j'ai suivi l'allemand.
- 1093 (perfekt) : le français ajoute « toute » (« toute la semaine ») ; suivi l'allemand.
- 1243 (perfekt) : le français ajoute « seul » (« un seul sujet ») ; suivi l'allemand.

## À trancher (l'Amérique latine hésite)

- 1128, 1215, 1222 : « la renta » (Mexique) pour die Miete — « el arriendo » en Colombie, « el alquiler » ailleurs.
- 1144 : « el pastel » (Mexique) — « la torta » / « el ponqué » ailleurs.
- 1180 : « el ayuntamiento » pour das Rathaus — « la alcaldía » en Colombie, « la municipalidad » au sud.
- 1133 : « el portero » — « el arquero » en Amérique du Sud.
- 1166 : « la bodega » (entrepôt) ; 1223 : « el suéter » ; 1288 : « el carro » ; 1212 : « round » (boxe).
- 1189, 1190 : pauken / büffeln — pas d'équivalent familier commun (machetear au Mexique, tragar en Argentine) : j'ai mis un espagnol neutre avec « (coloquial) ».
- 1198 : « incautar » pour sicherstellen (la police) — « asegurar » au Mexique, « decomisar » ailleurs.
- 1274 : « comisionar » pour abordnen (détachement d'un fonctionnaire) — usuel au Mexique et en Colombie, moins au sud.
- 1126 : « desescalar » (admis, récent) à côté de « bajar la tensión ».
- 1215, 1270 : « el estado federado » pour das Land ; 1267 : « el comité de empresa » pour der Betriebsrat ; 1072 : « el permiso parental » pour die Elternzeit — réalités allemandes, à harmoniser avec les autres lots.
