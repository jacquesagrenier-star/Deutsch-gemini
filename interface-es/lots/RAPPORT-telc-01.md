# Rapport — telc-01 (pages d'entraînement telc A2·B1, interface espagnole)

## Chiffres

- Source : `interface-es/sources/telc-01.json`, 728 textes. Lot : `interface-es/lots/telc-01.es.json`, **728 clés sur 728**.
- Contrôle `textes.py controle` : **2 FAUTES, toutes deux dues à la source** (voir ci-dessous), 14 avis.
- Les 14 avis sont tous de l'allemand cité (`du`, `des` dans « du oder Sie », « Kannst du … », « wegen des schlechten Wetters ») : rien à corriger.

## Les 2 fautes restantes : source fautive, pas la traduction

Dans `telc-commun.js`, 17 entrées ont un `fr` **vide** (n° 353-355, 358-362, 364-372 de la source). Le contrôle compare les `{marques}`
de l'espagnol à celles du français ; pour deux d'entre elles l'anglais porte des marques et le français vide n'en a aucune :

- `Last mock exam: {s} — {n}` → « Último simulacro de examen: {s} — {n} »
- `out of {n}` → « de {n} »

J'ai **gardé les marques** (comme le russe : « из {n} ») : les retirer ferait 0 FAUTE mais casserait l'affichage. À régler côté
source (remplir `fr`) ou côté contrôle (comparer à `en` quand `fr` est vide). Les 15 autres entrées à `fr` vide ont été traduites depuis l'anglais seul.

## Choix de vocabulaire (constants dans tout le lot)

- Noms allemands gardés : Lesen, Sprachbausteine, Hören, Schreiben, Sprechen, Hören und Schreiben, Mündliche Prüfung, Teil, richtig / falsch, Volkshochschule, Frau Becker, et tous les mots cités.
- courriel → **correo** ; le courrier postal (Post) → **la correspondencia** (pour ne pas confondre) ; petites annonces → anuncios clasificados ; annonces (Hören 3) → anuncios.
- trou → **espacio** ; formule d'appel → **saludo** ; salutation → **despedida** ; examen blanc → **simulacro de examen** ; corrigé → las respuestas ; grille → la tabla ; compétence → habilidad ; l'écoute → la comprensión auditiva (titre : Escuchar) ; l'écrit / l'oral → la parte escrita, el examen escrito / el examen oral ; répondeur → buzón de voz.
- « In English: {t} » / « En français : {t} » → **« En español: {t} »** (le russe a fait « По-русски »).
- Tutoiement partout (le français tutoie) ; vouvoiement / tutoiement allemands → « el trato de usted » / « el tuteo ».
- Heures : « 18 heures » → « las 18:00 » ; sommes et pourcentages comme la source (« 70 % »).
- Citations allemandes entre « … » sans espaces, comme le veut la ponctuation espagnole.

## Sources fautives ou divergentes

- n° 380 (`„Viertel nach sechs“…`) : l'anglais dit « Halb sechs (5:30) », le français « (17:30) ». J'ai suivi le français (17:30), cohérent avec 18:15.
- n° 644 : « la responsable du cours d'espagnol de Mark » : gardé tel quel (« curso de español ») ; un lecteur hispanophone trouvera peut-être curieux que Mark apprenne l'espagnol, mais c'est l'histoire.
- n° 422 : le français garde « Frühschichten » en allemand, l'anglais traduit « early shifts » ; j'ai gardé l'allemand comme le français. Même chose pour Nudelsalat / Kartoffelsalat (417), Getränkemarkt (418), Ausweis, Versichertenkarte.
- n° 259, 288, 289 : « en Écouter » rendu « en Escuchar » (nom de la section).

## Doutes

- n° 38, 41 : « Rendre ma copie » → « Entregar mi examen » ; « ta copie est rendue » → « tu examen quedó entregado ».
- n° 167-168 : « La grille : à toi de juger » → « La tabla: te toca juzgar » (« rúbrica » serait plus scolaire, moins transparent).
- n° 257 : « de trop » (une solution qui reste) → « sobra ».
- n° 296 : « Le déroulé » → « El desarrollo ».
- n° 331 : « Passer l'oral » → « Presentar el examen oral » (usage du Mexique et de la Colombie ; l'Espagne dirait « hacer »).
- n° 390 : « la moitié avant huit heures » → « la media antes de las ocho ».
- n° 494 : « Je suis content quand… » → « Me alegra que no haya animales en mi edificio » (tournure sans genre).
- n° 553-561 : participes de la source (« acheté », « mangé ») rendus au pretérito, 3e personne (« compró mazapán », « comió pescado »), puisque la question est « ¿Qué hizo Anna…? ».

## À trancher (l'Amérique latine hésite)

- n° 407, 415 : barbecue → **la parrilla** (Mexique : aussi « el asador »).
- n° 408, 377 : gâteau → **el pastel** (Colombie : « la torta », « el ponqué »).
- n° 724-725 : eau brune → **agua café** (Mexique, Colombie ; ailleurs « marrón »).
- n° 493, 501 : propriétaire (Vermieter) → **el dueño** (aussi « el arrendador », « el casero »).
- n° 430, 476-477 : cantine → **el comedor** (« cantina » = bar en Amérique latine).
- n° 434 : Gleis → **el andén** (aussi « la vía »).
- n° 438 : bouchon → **el embotellamiento** (Colombie : « el trancón »).
- n° 511, 514 : encombrants (Sperrmüll) → **la basura voluminosa** (pas d'équivalent établi).
- n° 474, 727 : artisans (Handwerker) → « los técnicos » (474), « los trabajadores » (727).
- n° 586 : éboueurs → « el camión de la basura ».
- n° 378, 646, 655, 660 : salle de cours (Raum) → **el salón** (aussi « el aula »).
