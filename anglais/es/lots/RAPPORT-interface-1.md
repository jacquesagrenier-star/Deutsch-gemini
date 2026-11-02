# Rapport — interface espagnole, part 1 (2 nov. 2026)

Part : `i18n` entrées 1 à 800 (indices 0-799, `onboarding_home_button` → `kicker_quiz_terminaisons`)
et `surcharge-en` (48 entrées). Traduit depuis le français, selon `anglais/es/CONSIGNES.md`.

## Fait

| fichier | entrées | contrôle |
|---|---|---|
| `lots/i18n-01.es.json` | 200 (0-199) | 0 faute, 0 avis |
| `lots/i18n-02.es.json` | 200 (200-399) | 0 faute, 0 avis |
| `lots/i18n-03.es.json` | 200 (400-599) | 0 faute, 0 avis |
| `lots/i18n-04.es.json` | 200 (600-799) | 0 faute, 0 avis |
| `lots/surcharge-en.es.json` | 48 | **5 fautes « identique au francais »**, voir ci-dessous |

Ordre des id identique à la source dans les cinq fichiers (vérifié). `poser_autres.py controle i18n`
donne 0 faute sur les 1 607 entrées (les lots 05-09 de l'autre moitié étaient déjà là).

### Les 5 « fautes » de surcharge-en sont voulues

`orb_adjektive_sub`, `op_adjektive_sub` (`big · bigger · the biggest`), `orb_adverbien_sub`,
`op_adverbien_sub` (`always · often · never`), `orb_redewendungen_sub` (`hello · thank you · of course`) :
ce sont des mots anglais, que les consignes imposent de garder **tels quels**. Le contrôleur les
compte « identique au francais » parce que la source a `en` vide (`fr != en` est vrai). Rien à
changer dans le lot ; à régler côté source ou contrôleur (poser `en = fr` pour ces cinq entrées
dans `extraire.py`, ou exempter un texte sans lettre ni mot français). Je n'ai pas touché à ces fichiers.

## Choix de traduction récurrents (hors glossaire)

- « séance » → « práctica » partout ; « Session terminée » (`session_ended`, fin d'une série
  d'exercices) → « Ronda terminada » (« sesión » réservé à « Iniciar sesión »).
- « le coffre » → « el cofre » ; « Gardés » / « Garder » (anciens libellés cités dans
  `ip_seance_gardes`, `srs_aide_garder`) → « Apartadas » / « Apartar », comme la fonction actuelle.
- « acquis » (bilan, série) → « dominada(s) » ; « mots rencontrés / à rencontrer » → « palabras vistas / por ver » ;
  « sus » → « dominadas » ; « jours travaillés » → « días de práctica ».
- « Escale » → « escala », « carnet (de phrases) » → « cuaderno (de frases) », « feuille » → « hoja »,
  « paquet » → « mazo », « éclat » (mosaïque) → « pieza », « cartouche » → « cartela »,
  « tuile » (de l'accueil) → « recuadro », « Choisis une tuile. » → « Elige una opción. ».
- « Je le connais déjà » → « Ya lo sé » ; « Je ne savais pas » → « No lo sabía » (glossaire : « Lo sabía »).
- « Bravo ! » → « ¡Muy bien! » ; « C'est bon ! » → « ¡Eso es! » ; « Passer » → « Saltar » ;
  « VÉRIFIER » → « VERIFICAR » ; « Vérifie ta connexion » → « Revisa tu conexión ».
- Langue connue → espagnol : `seance_choix_langue` (« Français » → « Español », c'est la porte
  « dans ta langue »), `search_title`, `search_placeholder`, `search_hint`, `flip_direction_fr/de`
  (« ES → DE », « DE → ES »).
- Pas de genre pour l'usager : `av_date_invite`, `av_depart_rythme`, `av_pp_e2` (« être prêt » →
  « tenerlo todo listo »), `av_depart_pret` (« ¡lo tienes todo listo! »), `qual_50` (« ¡Vas muy bien! »),
  `qual_80` (« ¡Casi nivel experto! »).
- Passé : pretérito indefinido partout (« Escribiste: », « Repasaste », « viste ») ; l'Espagne
  dirait souvent « Has escrito ». Compris des deux côtés, voir « À trancher ».

## Doutes (à relire)

- `or_entendu` « Oí: » ; `cp_tu_as_ecrit` « Escribiste: » — courts, à voir à l'écran.
- `cp_presque` « Solo un pequeño error al teclear: la contamos como correcta. »
- `seance_scene_untersuchung` « Mark con su doctora » (« chez sa médecin »).
- `seance_scene_arztpraxis` « Mark se lesionó la rodilla ».
- `seance_scene_heimwerken` « Mark monta un estante » (voir À trancher).
- `bilan_notion_titre` / `bilan_notions_titre` « La noción que trabajar » / « Las nociones que trabajar ».
- `srs_etat_1` à `srs_etat_4` « empiezo / avanzo / ya casi / la domino » (étiquettes très courtes).
- `niveau_clair_C1` « Experto: expresarte con soltura y matices » (« Expérimenté »).
- `reperes_mots`, `reperes_phrase` « recuadro » pour « tuile ».
- `en_module_mastered_label` « ✅ Dominada » (accord avec « palabra », source masculine).
- `praeteritum_ecrit` « se usa el perfecto » (« le parfait », Perfekt allemand).
- `grp_smalltalk` « Saludos & small talk » (anglicisme gardé, comme en français).
- `examen_aide_1` « Tres referencias oficiales del alemán » — gardé « alemán » comme demandé ;
  quand on apprend l'anglais, ce texte n'a pas de surcharge : vérifier qu'il ne s'affiche pas.
- `credits_video` « Animación de apertura: Created with Grok. » (mention anglaise gardée).
- surcharge `credits_dict` « pendiente de revisión por un anglohablante ».
- surcharge `tuiles_menu_desc` « El banco tiene una o dos palabras de más » (« le banc »).

## Sources qui m'ont paru fautives ou fragiles

- `surcharge-en` : `en` vide pour les cinq textes anglais ci-dessus → fausses fautes du contrôleur.
- `i18n` `orb_en_pitfalls_sub` : fr « actually ≠ actuellement », en « false friends » (pas aligné) ;
  traduit « actually ≠ actualmente » (même faux ami en espagnol).
- `i18n` `qual_50`, `qual_80` : « avancé(e) », « expert(e) » visent l'usager avec un genre ; rendus neutres.
- `i18n` `badge_xp_500_desc` dit « 50 points » alors que l'id dit `xp_500` (idem 2000/200, 5000/500) :
  traduit tel quel.
- `i18n` `examen_aide_1`, `credits_voix`, `credits_examens`, `mosaique_reste`, `ip_tableau_1` parlent
  d'allemand ; `mosaique_reste`, `mosaique_intro_texte`, `ip_tableau_1`, `credits_dict`, `credits_freq`
  ont leur surcharge anglaise, les autres non (`credits_voix` « Voz alemana: Aurora » s'afficherait-il
  en apprenant l'anglais ?).

## À trancher (Espagne / Amérique latine)

J'ai écrit la forme d'Amérique latine quand il fallait choisir, sinon le mot commun.

| id | écrit | Espagne | Amérique latine |
|---|---|---|---|
| `seance_scene_buergeramt` | el ayuntamiento | el ayuntamiento | la alcaldía / la municipalidad |
| `seance_scene_heimwerken` | Mark monta un estante | monta una estantería | arma un estante / una repisa |
| `seance_scene_supermarkt` | Anna hace las compras | hace la compra | hace las compras |
| `seance_scene_zug` | Mark toma el tren | coge el tren | toma el tren (« coger » à éviter) |
| `seance_scene_ubahn` | Mark en el metro | el metro | el metro (el subte à Buenos Aires) |
| `seance_scene_schlafzimmer` | Anna hace la maleta | la maleta | la maleta (la valija en Argentine) |
| `carte_dire_desc`, `carte_phrase_desc` (i18n et surcharge) | el altavoz | el altavoz | el altoparlante / el parlante / la bocina |
| `myvocab_add_title`, `myvocab_added`, `myvocab_deja_cours`, `myvocab_full`, `reglage_questions_desc`, `search_none_scope`, `voice_none`, `voice_only_one` | añadir | añadir | agregar |
| `settings_title`, `reperes_reglages`, `cp_micro_muet`, `legende_seance`, `legende_objectif`, `voice_none`, `voice_only_one` | Ajustes (glossaire) | Ajustes (iOS) | Configuración (Android, usage courant) |
| `verify_button` | VERIFICAR | COMPROBAR | VERIFICAR |
| `or_lentement`, `cp_lent` | Despacio / Más lento | despacio | despacio / más lento |
| `av_jalon_k`, `tableau_pct`, `en_module_mastered_hint`, `ip_seance_commencer` | « {p} % » (espace avant %) | 50 % | 50% (Mexique) |
| `search_hint` | « 250 000 » (espace fine) | 250.000 | 250,000 (Mexique) / 250.000 (Argentine) |
| passé composé des messages (`cp_tu_as_ecrit`, `revoir_niveau_fini`, `myvocab_full`, `legende_rencontres`, `av_jalon_change`, `av_fin_a1_texte`…) | pretérito indefinido (« Escribiste ») | pretérito perfecto (« Has escrito ») | indefinido |

Aucun nombre décimal (3,90 €) dans ma part.
