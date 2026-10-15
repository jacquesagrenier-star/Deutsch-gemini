# Rapport — « Autres textes » en arabe (15 oct. 2026)

## Fait

| Lot | Ids | Vérifié |
|---|---|---|
| `i18n.ar.json` | 131 / 131 | JSON, ids, ordre, balises, `{…}` |
| `categories.ar.json` | 25 / 25 | idem |
| `mots-outils.ar.json` | 74 / 74 (listes de 3) | idem |
| `variantes.ar.json` | 1 / 1 | idem |
| `prononciation.ar.json` | 20 / 20 (listes de 2) | idem |
| `grammaire.ar.json` | 302 / 302 | idem — même nombre de `<b>`, `<em>`, `<strong>`, `<i>`, `<br>` que le français |
| `scenes-01.ar.json` … `scenes-04.ar.json` | 266 + 217 + 278 + 270 = 1031 / 1031 | idem, ordre de la source conservé d'un lot à l'autre |

Contrôle : script `verif.py` (scratchpad) — charge le JSON, compare les ids à la source,
compare les balises HTML et les `{…}` de chaque texte au français, refuse `→` et `|`.
Aucun `→` ne subsiste : toutes les flèches sont « A ← B » (sens de lecture), comme `ejercicios-01.txt`.

## Choix de terminologie (à garder d'un lot à l'autre)

- Noms des temps et modes laissés en espagnol, comme le bloc allemand garde Präsens / Konjunktiv II :
  subjuntivo, indicativo, condicional, imperfecto, pretérito (indefinido / perfecto), gerundio, pluscuamperfecto.
  Le subjonctif est présenté comme « أقرب شيء إلى أن + المضارع المنصوب » (`fiches/subjuntivo/resume`, `/regle`, `textes|verbentemps_konjunktiv2`).
- « fiche (de grammaire) » = ملخّص (ملخّصات القواعد), pour ne pas entrer en collision avec « carte » = بطاقة.
- « accord » = المطابقة ; « article » = أداة التعريف ; « pronom complément » = ضمير المفعول ;
  « complément direct / indirect » = المفعول به المباشر / غير المباشر ; « participe » = اسم المفعول ;
  « infinitif » = المصدر ; « relative » = الجملة الموصولة ; « passif » = المبني للمجهول ;
  « périphrase » = تركيب فعلي ; « verbe pronominal » = فعل انعكاسي (comme « انعكاسي (sich) » du bloc allemand).
- Interface reprise du bloc `ar:` de `index.html` (mêmes phrases, « الألمانية » → « الإسبانية ») :
  `home_*`, `auth_*`, `search_*`, `carte_dire_desc`, `carte_phrase_desc`, `tuiles_menu_desc`, `dec_t0_texte`, etc.

## Doutes (ids précis)

- `flip_direction_fr` / `flip_direction_de` : écrits « 🔁 الاتجاه: AR ← ES » / « ES ← AR », sur le modèle du bloc
  allemand (« FR ← DE »). À regarder à l'écran : avec des lettres latines des deux côtés, le navigateur peut
  afficher la flèche dans l'autre sens.
- `orb_zuinf_title` = « Subjuntivo » seul ; `fiches/subjuntivo/titre` = « صيغة subjuntivo ». Si on préfère un
  terme arabe partout : « صيغة النصب » serait le plus proche, mais aucun manuel ne l'emploie pour l'espagnol.
- `verbentemps_es_condicional_title` et `fiches/futuro-condicional/titre` : condicional rendu « صيغة الشرط ».
- `op_es_falsos_d` : « ressemble au français » → « تشبه الفرنسية أو الإنجليزية » (consigne « faux amis »).
- `dec_t4_d5` : titre du tableau laissé en espagnol entre « », peintre translittéré « خواكين سورويا ».
- `fiches/genero/attention` : la liste des pièges a été refaite pour l'arabe (la leche, la sal, la sangre, la nariz,
  la luna féminins ; el sol, el árbol masculins) ; el color / el dolor / el calor retirés — ils ne piègent pas un
  arabophone (اللون، الألم، الحرّ sont masculins). À relire par un arabophone.
- `fiches/concordancia/exemples/0/1` : ajout « جمع غير العاقل لا يُعامَل كمفرد مؤنث » (vraie interférence arabe → pequeñas, pas pequeña).
- `fiches/numeros-hora/attention` : ajout « le nom reste au pluriel après le nombre » (contre خمسة عشر كتاباً).
- `fiches/ser-estar/regle` : ouvre sur la جملة اسمية (pas de « être » au présent en arabe).
- `textes|redewendungen_piege` : « il pleut des cordes » remplacé par l'idiome arabe « تمطر كأفواه القِرب » (calque es inventé en face, comme dans la source).
- `prononciation` : transcriptions refaites en lettres arabes ; `voyelles` ajoute les pièges e/i (peso ≠ piso) et
  o/u (coro ≠ curo) ; `g-gu` décrit le g « كالجيم القاهرية » ; `b-v` ajoute la mise en garde p ≠ b (peso ≠ beso)
  faute d'entrée propre pour le p. `r-rr` : transcription « رّ ».
- Balises : partout où j'ai ajouté un exemple espagnol dans une réécriture, il est **sans** `<b>` pour garder le même
  compte de balises que la source (`fiches/por-para/attention`, `fiches/pasados/attention`, `fiches/subjuntivo/regle`,
  `fiches/perifrasis/attention`, `fiches/numeros-hora/attention`, `fiches/preposiciones/attention`).
- Scènes : `klassenzimmer|B2|1`, `klassenzimmer|B2|1|latam`, `wohnzimmer|B2|2` — « cuyo = dont le » rendu
  « الذي… ـه (ملكية) », un peu lourd ; `park|B1|6` — la glose « remé = je, remo = je (présent) » rendue
  « remé = أنا (ماضٍ)، remo = أنا (مضارع) » ; `fruehstueck|B1|3` — pasar = يناول.
- `mots-outils` : traductions d'un mot-outil par deux ou trois équivalents arabes séparés par « ، » (ex. `praep|por`),
  comme le font fr/pt. `partikeln|venga` = « هيا، هيا بنا » (sans dialecte).

## Sources qui me semblaient fautives ou incomplètes

- `grammaire` : la **colonne 0** de plusieurs tableaux est en français dans `espanol/datos/grammaire.json` mais
  **absente de la source** (donc pas traduite) : `fiches/conectores/tableau/0..6/0` (« ajouter, opposer, concéder,
  cause, conséquence, organiser, condition »), « vosotros (Espagne) » (presente, futuro-condicional, imperativo,
  pronominales), « tú (négatif) », « irréguliers », « tú irréguliers », « l'heure », « a (personnel) »,
  « estar + gérondif », « seguir + gérondif ». Elles resteront en français pour l'arabophone si la pose ne les traite pas.
- `i18n|search_hint` : fr/pt disent « près de 150 000 mots », en dit « over 250,000 » (et le bloc allemand arabe dit 250 000). J'ai suivi fr/pt : « نحو 150 000 كلمة ».
- `mots-outils|partikeln|*` : la 3e valeur (catégorie) est vide en `en`, remplie en fr/pt — j'ai mis « أداة خطاب ».
- `prononciation|c-z.es` et `c-z.latam` : `exemples` vide (les mots cités dans le texte suffisent).
- `scenes|park|B1|6` : glose française « remé = je, remo = je (présent) » peu claire (voir ci-dessus).
