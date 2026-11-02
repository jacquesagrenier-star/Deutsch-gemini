# Rapport — l'interface en allemand (1er nov. 2026)

Part « interface » de l'espagnol enseigné en allemand. Tout est dans `espanol/de/lots/`,
rien d'autre n'a été touché.

## Fait

| source | lot(s) | textes | contrôle |
|---|---|---|---|
| i18n | `i18n-01` … `i18n-07.de.json` (7 morceaux) | 1 607 | 0 faute, 49 avis |
| surcharge-es | `surcharge-es.de.json` | 140 | 0 faute, 12 avis |
| categories | `categories.de.json` | 25 | 0 faute, 1 avis |
| mots-outils | `mots-outils.de.json` (listes `[traduction, exemple, catégorie]`) | 74 | 0 faute, 2 avis |
| vignettes | `vignettes.de.json` | 39 | 0 faute |
| page-scenes | `page-scenes.de.json` | 33 | 0 faute, 1 avis |
| peintres | `peintres.de.json` | 22 | 0 faute |
| variantes | `variantes.de.json` | 1 | 0 faute |

Tous les avis restants sont des « aucun mot-outil allemand » sur des titres courts ou des
listes d'exemples espagnols, et des « identique au français » sur des mots qui sont les mêmes
en allemand (`Niveau A1`, `E-Mail`, `Administration`, `Part. {pp}`, `{p} %`). Aucun avis de
balise ni de marque.

## Glossaire appliqué

Lerneinheit (séance), Karte, Zurücklegen / Zurückgelegt, Nochmal / Weiter, Erste Schritte,
Szene / Szenen entdecken, Hören, nachsprechen, Gemälde / Galerie / Mosaik, Einstellungen,
Niveau / Einstieg, Themen / Wörter / Wortschatz, Nomen / Verben / Adjektive / Adverbien /
Redewendungen, Grammatik / Übersicht, Übung / Üben, Schreiben / Diktat, sicher / im Lernen,
Serie, Tagesziel, Alle Inhalte, Meine Folgen, Problem oder Idee melden, Anmelden / Konto
erstellen / Passwort, Einladungscode, Abo / kostenlose Testphase, Spanien / Lateinamerika.

Choix hors glossaire, à connaître pour la relecture :
- « le coffre » (des mots mis de côté) → **die Ablage** (`garde_sortir`, `settings_vider_coffre`,
  `confirm_vider_coffre`, `vider_coffre_fait`, `gardes_vide`, `coffre_suivante_sous`,
  `srs_aide_garder`, `ip_seance_gardes`).
- « maîtrisé » → **sicher** partout (`vocab_sus`, `echeance_maitrise`, `review_mastered`,
  `settings_revoir_maitrises`…) ; « à rencontrer » → **noch neu** ; « acquis » → **gelernt**.
- « Essentiel » (marque d'examen) → **Grundwortschatz** ; « Pour aller plus loin » →
  **Der nächste Schritt** / **Der Wortschatz für den nächsten Schritt**.
- « Repères » (bloc 🧭) → **Orientierung** ; « points de découverte » → **Entdeckungspunkte**.
- « Escale » (A1 voyage) → **Etappe** ; « étape » (la suite de l'A1, Premiers pas) → **Schritt**.
- « carnet » → **Heft** (`av_carnet_*`) ; « feuille » (conjugaison) → **Blatt**.
- « éclat » (mosaïque) → **Splitter** ; « carreau » → **Kachel** ; « cartouche » → **Schildchen**.
- « gel de série » → **Serien-Schutz**.
- « l'accord » (espagnol) → **die Angleichung** ; « marqueurs du discours » → **Diskursmarker** ;
  « périphrases » → **Verbalperiphrasen** ; « verbes pronominaux » → **reflexive Verben**.
- « Crédits » → **Quellen** ; « Tableau de bord » (admin) → **Übersicht**.
- Noms des temps espagnols gardés en espagnol (presente, pretérito, imperfecto, subjuntivo…),
  titres `verbentemps_es_*_title` en « Futuro – das Futur », « Condicional – der Konditional »,
  « Imperativo – der Imperativ » ; `orb_es_presente` → « Das presente ».
- Tutoiement partout, aucun « Anfänger / Lerner / Nutzer » ; `niveau_clair_A1` « Einstieg »,
  `qual_50` « Schon weit gekommen! » (neutre, pas de (e)).

## Comparaisons avec l'allemand écrites (à relire)

- `surcharge-es` `dec_t1_texte_plusieurs` : « Nicht immer wie im Deutschen: el sol, die Sonne. »
  (la source donnait la leche / le lait, qui ne marche pas contre l'allemand : la leche et die
  Milch sont du même genre).
- `surcharge-es` `op_es_gustar_d` : « me gusta el chocolate = die Schokolade schmeckt mir ».
- `surcharge-es` `op_es_falsos_d` : exemples remplacés par des pièges germanophones
  « la carta, el regalo, el gimnasio, embarazada … das Wort, das vertraut klingt, ist oft die Falle. »
- `surcharge-es` `verbentemps_es_imperativo` : « der subjuntivo (hable, no hables) ».
- `mots-outils` : les catégories disent « subjuntivo » là où le français disait « subjonctif ».

## Doutes (id précis)

1. **Textes du bloc `i18n` qui nomment le français comme langue de l'usager.** L'anglais de la
   source dit « German or English » : la seconde langue est celle de l'interface. En allemand,
   la langue de l'usager EST l'allemand, ce qui n'a de sens que par la surcharge espagnole.
   J'ai mis **Deutsch** là où c'est la langue de l'usager : `seance_choix_langue` (« Deutsch »,
   comme l'anglais dit « English »), `voice_lang_fr` (« Deutsche Stimme (Übersetzungen im
   Hörmodus) »), `tuiles_menu_desc` (« in deiner Sprache »). J'ai laissé « Französisch » dans
   `search_title`, `search_placeholder`, `search_hint` du bloc i18n (ils parlent d'apprendre
   l'allemand et sont remplacés par `surcharge-es` : « Spanisch oder Deutsch »). À trancher
   si le bloc `de` d'I18N doit un jour servir à autre chose que l'espagnol.
2. `surcharge-es` `flip_direction_fr` / `flip_direction_de` : écrits « DE → ES » / « ES → DE »
   (la source dit FR → ES ; en allemand la langue connue est DE).
3. `categories` : les neuf lignes « Con tener — tener ganas, tener prisa »… sont **purement
   espagnoles** dans toutes les langues (fr, en, pt, ar identiques) ; le contrôle refuse la
   copie (« identique au français »). J'ai écrit **« Mit tener — … »** (l'allemand de « con »),
   lisible et parallèle à « Tiempo — Zeit ». Si on préfère garder « Con tener » comme les autres
   langues, c'est à changer à la pose (le contrôle le refusera tel quel).
4. Même contrainte sur 15 clés `i18n` et 8 clés `surcharge-es` faites d'exemples
   allemands/anglais/espagnols que la source donne déjà tels quels (`orb_kasus_sub`,
   `op_relativ_sub`, `op_pronomen_o1_d`, `op_verben_o4_d`, `orb_en_phrasal_sub`,
   `orb_zuinf_sub`, `orb_redewendungen_sub`, `op_konjunktionen_o12_t`, `op_adjektive_o4_d`,
   `orb_zahlen_sub`…) : j'ai varié la ponctuation (« · » ↔ « , ») ou ajouté un exemple de la
   même famille (« · put on », « · ojalá », « · deren », « · des », « -dad », « good · better ·
   the best »). Aucun sens changé ; à vérifier que la longueur passe dans les tuiles.
5. `i18n` `dec_t1_texte_plusieurs` (bloc allemand) : « oft anders als in anderen Sprachen » au lieu
   de « souvent différent du français » (un germanophone lisant l'allemand n'a pas de repère
   français). `op_verben_o5_d`, `op_konjunktionen_o9_d`/`o10_d`/`o11_d` gardent « im Französischen »
   (ces tuiles n'apparaissent qu'en apprenant l'allemand).
6. `i18n` `vocab_reste` / `examen_pied` : « à rencontrer » → « noch neu » (court, pour la barre) ;
   « à rencontrer » se dirait plus littéralement « noch zu sehen ».
7. `i18n` `credits_voix` « Deutsche Stimme: Aurora » : vaut pour l'allemand ; l'espagnol a ses
   voix (Lolita, Monica) — la clé n'est pas dans `surcharge-es`, donc l'allemand affichera la
   phrase allemande dans les crédits de l'espagnol, comme le font déjà les autres langues.
8. `mots-outils` `praep|a` : « nach, zu, an » (trois sens, aucun ne couvre seul « à ») ;
   `konjunktionen|ni` : « noch, auch nicht » ; `partikeln|hombre` : « Mensch, na klar ».
9. `vignettes` : « L'examen » → « Die Untersuchung » ; « Le médecin » → « Beim Arzt » (le
   personnage est une médecin, mais « Beim Arzt » est la tournure générique) ; « Les vélos » →
   « Die Fahrräder » ; « La neige » → « Der Schnee » ; « La valise » → « Der Koffer ».
10. `page-scenes` `sur` → « auf » et `cestQui` « Das ist {a}. Such {b} auf {c}. » : « sur » veut
    dire sur une image/zone ; si {c} est un lieu (« la table »), « auf » convient ; sinon à voir.

## Sources qui semblaient fautives ou à discuter

- `categories` : voir le doute 3 (les neuf lignes sans aucune partie à traduire).
- `surcharge-es` `dec_t1_texte_plusieurs` : l'exemple « la leche, le lait » est pensé pour le
  français ; remplacé (voir plus haut).
- `i18n` `en_module_pitfalls_cat_desc` et `orb_en_pitfalls_sub` : « actually ≠ actuellement » est
  un faux ami français ; rendu « actually ≠ aktuell », qui vaut aussi en allemand.
- `i18n` `search_hint` dit « plus de 250 000 mots » et `surcharge-es` « près de 150 000 » : repris
  tels quels.
