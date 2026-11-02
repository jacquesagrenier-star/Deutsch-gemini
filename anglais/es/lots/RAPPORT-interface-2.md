# Rapport — interface espagnole de l'anglais appris, part 2 (i18n, entrées 801 à 1607)

Session du 2 nov. 2026. Source : `anglais/es/sources/i18n.json`, indices 800 à 1606 de la liste
(du `regles_kicker` au `admin_user_stats`). Consignes suivies : `anglais/es/CONSIGNES.md`.

## Ce qui est fait

| lot | entrées | de … à |
|---|---|---|
| `i18n-05.es.json` | 161 | `regles_kicker` → `dec_te_essai` |
| `i18n-06.es.json` | 160 | `dec_te_repete` → `op_kasus_title` |
| `i18n-07.es.json` | 179 | `op_kasus_sub` → `op_pruefung_sprechen_d` |
| `i18n-08.es.json` | 151 | `kicker_pruefung_hoeren` → `op_adverbien_o3_t` |
| `i18n-09.es.json` | 156 | `op_konjunktionen_title` → `admin_user_stats` |

**807 entrées**, dans l'ordre de la source, aucun id manquant ni en trop sur ma part (vérifié
par script). `poser_autres.py controle i18n` : **0 faute, 0 avis** sur mes entrées (les seuls
messages restants sont les « non traduit » des entrées 1 à 800, qui appartiennent à l'autre session).

⚠️ **Frontière** : la consigne disait « la première après ta frontière suit l'id `regles_kicker`,
qui n'est PAS à toi », mais `regles_kicker` est l'indice **800** de la liste (l'entrée 801), donc
dans la plage « indices 800 à 1606 » que j'avais aussi. L'indice 799 est `kicker_quiz_terminaisons`.
J'ai **inclus** `regles_kicker` (« El género de los sustantivos ») : si l'autre session l'a
traduit aussi à l'identique, le contrôle ne dit rien ; si elle l'a traduit autrement, il signalera
« traduit deux fois, differemment » et il suffira de retirer la ligne de l'un des deux lots.

## Choix de traduction à connaître

- Glossaire respecté : práctica (jamais « sesión » hors « Iniciar sesión / Cerrar sesión »),
  tarjeta, Apartar/apartadas, racha, meta del día, Ajustes, Lo básico, etc.
- `alert_session_ended`, `alert_session_ended_saved`, `hl_fin_titre`, `ecoute_etat_fin` :
  « Práctica terminada » (pas « Sesión »).
- « Flashcards » (kickers `kicker_*_flashcards`, `redewendungen_vocab_title`) → « Tarjetas ».
- « Gel de série » (`streak_freeze_*`) → « Protector de racha » (forme courante des apps).
- « Testeurs » (`admin_users_title`, `settings_admin_desc`, `admin_requests_desc`, `admin_no_users`)
  → « usuarios de prueba » (« probadores » désigne des cabines d'essayage).
- « Découverte guidée / la visite » (`dec_*`) → « recorrido (guiado) ».
- « carreau » de la mosaïque (`dec_t4_texte`) → « pieza ».
- « la petite pousse » 🌱 (`dec_t5_texte`) → « el brotecito ».
- Genre de l'usager évité : « Te damos la bienvenida » (`auth_kicker`, `setup_kicker`,
  `dec_t0_titre`), « Sesión iniciada como: » (`auth_logged_in_as`), « para mantener la motivación »
  (`auth_value_2`), « para llegar a tiempo » (`setup_voyage_note`), « COMO PRINCIPIANTE » (`dec_admin_btn_zero`).
- « Tous les verbes … sont maîtrisés » → « ¡Ya dominas todos los verbos… ! » (évite l'accord).
- La langue connue devient l'espagnol : `tuiles_menu_desc` (« la frase en español »),
  `voice_lang_fr` (« Voz en español »), `dec_t1_texte_plusieurs` (« distinto del español »),
  `op_konjunktionen_o9_d`, `_o10_d` (« en español »).
- Nombres : « 4199 sustantivos » (`regles_intro`), « 7700 palabras » (`abo_av_mots`) sans
  séparateur, règle RAE pour quatre chiffres ; pourcentages avec espace (« {taux} % », « {n} % »).

## Doutes (par id)

- `op_verben_o5_d` : la source dit « Un seul verbe en français, deux en allemand » ; c'est faux
  pour l'espagnol, qui a saber / conocer. Écrit : « Dos verbos en alemán, como «saber» y «conocer» ».
- `op_konjunktionen_o11_d` : « Un seul « mais » en français » ; l'espagnol a pero / sino, exactement
  aber / sondern. Écrit : « Como «pero» y «sino» en español — y dos condiciones que comprobar ».
- `op_konjunktionen_o9_d`, `op_konjunktionen_o10_d` : « si » et « cuando » sont bien uniques en
  espagnol, traduits tels quels avec « en español ».
- `op_kasus_sub` : source allemande seule (« der · den · dem · ein · kein »), que le contrôle
  refuse comme « identique au francais » parce que l'anglais diffère. Écrit
  « der · den · dem · ein · kein — los casos » pour passer ; à simplifier si on préfère.
- `op_scenes_blessure_d` : « chez la médecin » → « en la consulta de la doctora » (« consulta »
  se comprend des deux côtés ; « consultorio » est plus latino-américain).
- `op_scenes_bricolage_d` : « Bricoler » → « Los arreglos en casa » (« bricolaje » est surtout
  espagnol d'Espagne).
- `settings_trademark` : « marque de commerce » → « marca comercial » (« marca registrada »
  affirmerait l'enregistrement).
- `rappel_propose_texte` : « Bravo pour ce palier ! » → « ¡Felicidades por este logro! »
  (« Enhorabuena » est d'Espagne).
- `admin_deploy_title` : « Despliegue » (Espagne et usage technique courant ; « implementación »
  en Amérique latine). Admin seulement.
- `auth_forgot_sent` : « indésirables » → « correo no deseado » (plutôt que « spam »).
- `op_zahlen_sub` : « compter, dater, chiffrer » → « contar, fechas, cifras » (noms, pas verbes,
  pour rester lisible).
- `kicker_ordre_inverse`, `op_konjunktionen_o15_t` : « Retourner » → « Invertir ».

## Sources qui semblent fautives

- `dec_admin_desc` : le français dit « Les cinq étapes », l'anglais « The six steps ». J'ai suivi
  le français (« Los cinco pasos »). À vérifier contre l'écran réel.
- `op_kasus_sub` : le français (« der · den · dem · ein · kein ») et l'anglais (« Cas & articles ·
  der · ein · kein ») ne disent pas la même chose ; l'anglais mélange un titre français.
- `op_pronomen_title` (« Pronoms » / en « Pronoms ») et `op_zahlen_title` (« Nombres » / en
  « Nombres ») : l'anglais recopie le français.
- `op_english_*` : l'ancien module anglais pour germanophones (masqué depuis la v727) ; traduit
  quand même, titres allemands gardés (Wortschatz, Verben, Zeiten…).

## À trancher (Espagne / Amérique latine)

Aucun mot sans forme commune n'a été nécessaire ; partout un mot neutre existait (teléfono,
pantalla, dispositivo, navegador, correo electrónico, ajustes, compras, trámites, bicicleta,
peluquería, mudanza, lavandería, cafetería). Les ids ci-dessous portent un mot compris des deux
côtés mais dont la forme la plus naturelle diffère :

| id | écrit (neutre / Am. latine) | Espagne |
|---|---|---|
| `op_scenes_hiver_d` | el clima | el tiempo |
| `op_scenes_bricolage_d` | los arreglos en casa | el bricolaje |
| `op_scenes_blessure_d` | la consulta (de la doctora) | la consulta / le consultorio est l'inverse (Am. lat.) |
| `admin_deploy_title` | despliegue (gardé, usage technique) | despliegue — Am. lat. : implementación |
| `rappel_propose_texte` | ¡Felicidades! | ¡Enhorabuena! |
| `auth_forgot_sent` | correo no deseado | spam / correo basura |
| `op_scenes_boulangerie_d` | los pasteles | les deux, « pasteles » commun ; Mexique : « pan dulce » |
| `op_scenes_famille_d` | la comida (le repas) | commun ; en Espagne « comida » = aussi le déjeuner |
| `dec_t4_texte` et `dec_t5_texte` | la pantalla de inicio | commun |

Nombres décimaux : aucun dans ma part (seuls `{prix}` et des pourcentages entiers). Les prix
viennent du magasin via `{prix}` : la virgule / le point se décidera là, pas dans l'i18n.
