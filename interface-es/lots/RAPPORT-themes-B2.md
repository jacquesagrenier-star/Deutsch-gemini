# Rapport — themes B2-01 et B2-02 (cartes 85 à 3651, niveau B2)

## Fait

- **449 cartes sur 449**, toutes des noms (traduction + exemple) :
  `lots/corpus-themes-B2-01.es.json` (240, de *Familie* à *Arbeit und Büro*) et
  `lots/corpus-themes-B2-02.es.json` (209, de *Arbeit und Büro* à *Grundwortschatz*).
- Contrôle `corpus_lots.py controle` : **0 faute, 0 avis** sur chacun.
- Voisins des mêmes thèmes, **tous niveaux** (les `traduction_es` déjà dans `themes.json` et les lots
  rendus des autres parts, en lecture seule) : 11 réponses identiques trouvées pour un mot allemand
  différent, toutes départagées (liste plus bas) ; il n'en reste aucune.

## Choix à connaître

- Loyer : « la renta » (comme les lots précédents et la consigne « rentar ») : 596, 597, 598, 601, 2315.
- Les noms féminins de personne gardent le féminin dans la traduction (231 *la aprendiz*, 234 *la
  trabajadora por cuenta propia*, 235 *la empleada*, 239 *la jefa*) ; la phrase suit l'allemand, qui est
  souvent au pluriel générique (*Die Angestellten* → « Los empleados »).
- 94 *Erziehungsberechtigte* : « la responsable legal (de un menor) », pour la séparer de 87 *Vormund*
  « el tutor legal ».
- 1361 *Abitur* : « el bachillerato (examen final alemán) » ; 2624 *Grundgesetz* : « la Ley Fundamental
  (constitución alemana) » ; 1418 *Habilitation* : « la habilitación (título posdoctoral) ».
- 1014 *Reh* : « el corzo (un venado pequeño) » — l'animal n'existe pas en Amérique, le mot seul ne dit rien.
- 834 *Blase*, 1113 *Weide*, 3547 *Bruch*, 2613 *Bund*, 2614 *Orden*, 2617 *Revision*, 3641 *Ebene*,
  3642 *Stand*, 3644 *Antrieb* : deux sens comme dans le français ; la phrase illustre l'un des deux.
- 516 *Absatz* (thème Kleidung) : « el tacón » seul (le sens « paragraphe » du français n'est pas celui du thème).

## Doublons départagés (même thème, autre niveau)

| Carte | Mot | Rendu | Voisin déjà traduit |
|---|---|---|---|
| 358 | Ernährungsgewohnheit | el hábito de alimentación | Essgewohnheit (B1) : el hábito alimenticio |
| 696 | Putzmittel | el limpiador, el producto para limpiar | Reinigungsmittel (B1) : el producto de limpieza |
| 758 | Spülbecken | el fregadero (la pila) | Spüle (A2) : el fregadero |
| 838 | Hirn | el cerebro, los sesos | Gehirn (B1) : el cerebro |
| 1157 | Wettervorhersage | el pronóstico meteorológico | Wetterbericht (A2) : el pronóstico del tiempo |
| 1238 | Vierteljahr | el trimestre, los tres meses | Quartal (B1) : el trimestre |
| 1373 | Schulbuch | el libro escolar | Lehrbuch (A2) : el libro de texto |
| 1693 | Ticketautomat | la máquina expendedora de boletos | Fahrkartenautomat (A2) : la máquina de boletos |
| 1696 | Geschwindigkeitsbegrenzung | la limitación de velocidad | Geschwindigkeitsbeschränkung (B1) : el límite de velocidad |
| 2076 | Kunstströmung | el movimiento artístico | Stilrichtung (B1) : la corriente artística |
| 2678 | Windkraft | la energía del viento | Windenergie (A2) : la energía eólica |

Ce sont de vrais synonymes allemands : la différence en espagnol est de forme, pas de sens. Si l'on
préfère le même mot des deux côtés (surtout 758, 838, 1238), il suffit de reprendre celui du voisin.

## Doublons acceptés

Aucune réponse identique. Recouvrements **partiels** laissés (un sens commun parmi deux, mots allemands
vraiment voisins) : 239 *Vorgesetzte* « la jefa, la superior » / *Chefin* « la jefa » ; 841 *Gesäß* /
*Po* (« las nalgas ») ; 943 *Genesung* / *Besserung* (« la recuperación ») ; 1557 *Unterlage* /
*Dokument* (« el documento ») ; 1694 *Umsteigen* / *Anschluss* (« el transbordo ») ; 1931 *Zeitvertreib*
/ *Hobby*, *Rätsel* (« el pasatiempo ») ; 2074 *Aufführung* / *Vorführung* (« la función ») ; 2082
*Entwurf* / *Skizze* (« el boceto ») ; 2202 *Sendung* / *Programm* (« el programa ») ; 2406 *Vertrauen* /
*Zuversicht* (« la confianza ») ; 3639 *Anteil* / *Teil* (« la parte ») ; 3642 *Stand* et 3645
*Bedingung* / *Zustand* (« el estado », « la condición »). Deux cartes de thèmes différents ont « la
diferencia » : 3546 *Differenz* (Zahlen und Mengen) et 3651 *Unterschied* (Grundwortschatz).

## Doutes (à relire)

- 224 *Handwerker* : « el trabajador de oficio, el artesano » — l'allemand désigne le plombier,
  l'électricien, le menuisier ; « artesano » seul ferait penser à l'artisanat d'art.
- 228 *Quereinsteiger* : pas de nom espagnol ; « el profesional que viene de otro campo », phrase
  reformulée (« Como venía de otra profesión… »).
- 95 *Pflegekind* : « el niño de acogida » (aussi : *en acogimiento familiar*, *hijo de crianza* en Colombie).
- 233 *Freiberufler* : « in die Kasse einzahlen » rendu par « paga él mismo sus aportes al seguro ».
- 360 *Bekömmlichkeit* : « la digestibilidad » (mot savant, comme l'allemand).
- 369 *Imbiss* : « el puesto de comida rápida » (sens de la phrase ; le français donne « snack, casse-croûte »).
- 1153 *Kälteeinbruch* : « el descenso brusco de temperatura » (au Mexique on dirait aussi *frente frío*).
- 1156 *Glätte* : « el hielo en las calles » (pas de nom espagnol pour la chaussée glissante).
- 1233 *Verzug* : « la mora, la demora (en un contrato) ».
- 1367 *Klassenlehrer* : « el maestro titular (de un grupo) » ; 1368 *Elternsprechtag* : « el día de
  reunión de padres y maestros ».
- 1371 *Pausenbrot* : « el refrigerio para el recreo » (*lonche* au Mexique, *lonchera* en Colombie).
- 1561 *Ablage* : « el archivo de documentos » (l'action de classer).
- 1567 *Betriebsrat* : « el comité de empresa » (institution allemande, sans équivalent exact).
- 1869 *Gewerbegebiet* : « el parque empresarial ».
- 1921 *Ehrenamt* : « el cargo voluntario (sin sueldo) », pour le séparer de 1920 *Freiwilligenarbeit*
  « el trabajo voluntario » (la piste donnait « el voluntariado » aux deux).
- 1932 *Muße* : « el ocio, el sosiego ».
- 2617 *Revision* : « el recurso (judicial) » — en droit allemand, proche du *recurso de casación*.
- 2626 *Behörde* : « la autoridad, la dependencia pública ».

## Sources fautives ou à signaler

- 94 *die Erziehungsberechtigte* : la carte est au féminin singulier, le français et l'anglais donnent
  un neutre (« titulaire », « legal guardian ») et la phrase est au pluriel.
- 231 *die Auszubildende*, 234 *die Selbstständige*, 235 *die Angestellte*, 239 *die Vorgesetzte* : le
  français donne le masculin ou « (e) » pour une carte féminine.
- 516 *Absatz* (Kleidung) et 3547 *Bruch* (Zahlen) : le français ajoute un second sens hors thème
  (« paragraphe », « fracture ») ; gardé pour *Bruch*, retiré pour *Absatz*.
- 1232 *Zeitspanne* : la phrase est presque celle de 1230 *Zeitraum* (« In dieser Zeitspanne hat sich
  viel verändert » / « In diesem Zeitraum hat sich vieles verändert »).
- 2615 *Führer* : rangé dans « Politik und Gesellschaft » avec le seul sens « guide » (phrase du château).
- 946 *Leiche* et 947 *Zelle* : le français porte l'article (« le cadavre ») contrairement aux cartes voisines.
- Aucune faute relevée dans l'allemand.

## À trancher (l'Amérique latine hésite)

- 89 *Patchworkfamilie* : « la familia ensamblada » (aussi *reconstituida*).
- 362 *Haltbarkeitsdatum* : « la fecha de vencimiento, la fecha de caducidad » (Colombie / Mexique) ;
  la phrase dit *vencimiento*.
- 434 *Süßkartoffel* : « el camote, la batata » (Mexique, Pérou / Colombie, Argentine) ; la piste était
  *boniato* (Espagne).
- 503 *Strumpfhose* : « las pantimedias » (Colombie : *medias veladas*).
- 510 *Bügel* : « el gancho (para ropa) » (Espagne : *percha*).
- 514 *Leder* : « el cuero » (Mexique : souvent *la piel*).
- 517 *Schnürsenkel* : « el cordón (de zapato) » (Mexique : *agujeta*).
- 599 *Eigentumswohnung* : « el apartamento propio » (Mexique : *departamento*).
- 607 *Einbauküche* : « la cocina integral ».
- 685 *Geschirrspülmaschine* : « el lavavajillas » (aussi *lavaplatos*, qui en Colombie est l'évier).
- 693 *Teppichboden* : « la alfombra de pared a pared » (Espagne : *moqueta*).
- 694 *Glühbirne* : « el foco, el bombillo » (Mexique / Colombie) ; la piste était *bombilla*.
- 695 *Wischmopp* : « el trapeador » (Colombie : *trapero* ; la piste *fregona* est d'Espagne).
- 753 *Auflaufform* : « la fuente para horno » (Mexique : *refractario*).
- 756 *Herdplatte* : « la hornilla » (aussi *quemador*, *fogón*).
- 758 *Spülbecken* : « el fregadero » (Colombie : *lavaplatos*).
- 1422 *Studienplatz* : « el cupo (en la universidad) » (Mexique : *lugar* ; Espagne : *plaza*).
- 1689 *Fahrzeugschein* : « la tarjeta de circulación » (Colombie : *tarjeta de propiedad*).
- 1690 *Parkhaus* : « el edificio de estacionamiento » (Colombie : *parqueadero*).
- 1695 *Kreisverkehr* : « la glorieta, la rotonda ».
- 1697 *Panne* : « la avería » (Mexique : *descompostura* ; Colombie : *varada*).
- 1764 *Visum* : « la visa » (la piste *visado* est d'Espagne).
- 2316 *Kontoauszug* : « el estado de cuenta » (Colombie : *extracto*).
- 2318 *Wechselgeld* : « el cambio, el vuelto » (Colombie : *las vueltas*).
- 2451 *Torte* : « el pastel de capas, la torta » (*torta* est un sandwich au Mexique, d'où « pastel »
  dans la phrase).
- 2622 *Fraktion* : « el grupo parlamentario » (Amérique latine : aussi *la bancada*).

### À faire relire par un soignant

- 841 *Gesäß* : « los glúteos, las nalgas » ; phrase « La inyección se le pone en el glúteo. »
- 948 *Hausarzt* : « el médico de cabecera » (aussi *médico familiar*, *médico general*).
- 949 *Krankenkasse* : « la caja de seguro médico » (institution allemande ; au Mexique on penserait
  à l'IMSS, en Colombie à l'EPS).
- 950 *Krankenschein* : « la incapacidad médica, el certificado médico » (*incapacidad* se dit au
  Mexique et en Colombie ; ailleurs *licencia médica*, *reposo*).
- 944 *Vorsorgeuntersuchung* : « el chequeo preventivo » ; 954 *Krankengymnastik* : « la fisioterapia » ;
  942 *Rettungsdienst* dans la phrase : « servicio de emergencias ».
- 840 *Kniekehle* : « la corva (parte de atrás de la rodilla) » — terme exact (*hueco poplíteo* en
  anatomie), peu connu, d'où la précision.
