# Rapport : scènes et parcours en allemand (1er nov. 2026)

Part « scènes et parcours » de l'espagnol enseigné en allemand. Tout est écrit dans `espanol/de/lots/`, contrôlé par `poser_autres.py controle` (0 faute partout).

## Ce qui est fait

| Source | Textes | Lots | Contrôle |
|---|---|---|---|
| `scenes.json` | 2 430 | `scenes-01.de.json` … `scenes-08.de.json` (≈300 par morceau, le 8e en compte 330) | 0 faute, 122 avis |
| `premiers-pas.json` | 667 | `premiers-pas-01.de.json`, `premiers-pas-02.de.json` | 0 faute, 7 avis |
| `a1-voyage.json` | 746 | `a1-voyage-01.de.json`, `a1-voyage-02.de.json` | 0 faute, 4 avis |
| `reperes.json` | 55 | `reperes.de.json` | 0 faute, 5 avis |

Les avis restants sont tous du type « aucun mot-outil allemand » sur des titres courts, des listes de mots (jours, mois) ou des notes faites surtout d'espagnol (« <b>de + el = del</b>, immer. »), plus « Mai » identique au français. Rien à corriger.

## Choix de traduction (pour la cohérence de la relecture)

- Notes récurrentes des scènes, toujours rendues par la même formule :
  - « la est féminin → en la » → „<b>la</b> ist weiblich → <b>en la</b>.“
  - « el est masculin → en el, qui ne se contracte jamais » → „<b>el</b> ist männlich → <b>en el</b>, das nie verschmilzt.“
  - « de la, sans contraction. Seul de + el devient del » → „<b>de la</b>, ohne Verschmelzung. Nur <b>de + el</b> wird zu <b>del</b>.“
  - « hay présente une chose nouvelle ; está situe une chose déjà connue » → „<b>hay</b> führt etwas Neues ein („es gibt“); <b>está</b> sagt, wo etwas schon Bekanntes ist.“
  - « deber de + infinitif = une déduction » → „<b>deber de</b> + Infinitiv = eine Schlussfolgerung („muss wohl“).“
  - « puede que … → toujours le subjonctif » → „… → immer der <b>subjuntivo</b>.“
  - « Le futur exprime une supposition sur le présent » → „Das <b>futuro</b> drückt eine Vermutung über die Gegenwart aus — wie „wird wohl …“ im Deutschen.“
  - « dicen que rapporte une affirmation → indicatif » → „<b>dicen que</b> gibt eine Behauptung wieder → <b>Indikativ</b>.“
- Noms des temps gardés en espagnol (indefinido, imperfecto, pretérito perfecto, pluscuamperfecto, futuro perfecto, condicional, subjuntivo, gerundio), les temps allemands en contraste (Plusquamperfekt, Futur II, Konjunktiv II).
- « Quería …, por favor » (phrases toutes faites) → „Ich hätte gern …, bitte.“ ; « Quiero » dans Premiers pas → „Ich möchte“ (une note dit que quiero n'est pas brusque comme „Ich will“).
- « vous (poli) » → „Sie (höflich)“ ; « à plusieurs » (ustedes / vosotros) → „mehrere Personen“ / „ihr“.
- Les leurres (`l/0`, `l/1`) des phrases de Premiers pas sont traduits fidèlement et restent distincts de la bonne réponse.
- `|sens` : traduit depuis l'espagnol ; le genre grammatical suit l'allemand (la pelota → der Ball, donc « Mark hat ihn … »), et la note l'explique quand le pronom espagnol (la) surprendrait.

## Comparaisons avec l'allemand écrites (à relire)

Principales, par id :
- `apotheke|B2|0`, `|B2|4` (si + Präsens « wie im Deutschen »), `apotheke|B2|3` (futur dans la principale, là où l'allemand garde le présent), `apotheke|C1|3`, `baeckerei|B2|0` (indicatif après dicen/dice que, pas de Konjunktiv I).
- `arztpraxis|B1|0`, `arztpraxis|B2|0`, `familie|B1|3` (le genre / l'accord suit le mot espagnol, pas l'allemand ; cuyo suit le possédé).
- `baeckerei|B1|2`, `buero|B1|0` (estar + gerundio : forme absente de l'allemand).
- `bauernhof|B1|0`, `|B1|4`, `|B1|6`, `friseur|B1|0`, `|B1|1`, `|B1|3`, `untersuchung|A2|3`, `untersuchung-dos|A2|0` (réfléchis et article aux parties du corps : me lavo las manos ≈ « mir die Hände »).
- `bauernhof|B2|0`, `|B2|3`, `|B2|5`, `fruehstueck|B1|1` (gustar / doler comme « gefallen », « schmecken », « ihm schmerzt »).
- `bibliothek|B1|3`, `escales/9/tableau/a` (a personnel : rien de tel en allemand).
- `buergeramt|B2|0`, `|B2|5`, `kueche|B1|3`, `|B1|4`, `flughafen|B2|3`, `schlafzimmer|B1|5` (toujours haber, jamais « sein »).
- `camping|B1|2` (futur en une terminaison, pas de « werden »), `camping|B2|0`, `stadtplatz|B2|0`, `klassenzimmer|C1|3`, `arztpraxis|C1|2` (subjuntivo / condicional là où l'allemand a le Konjunktiv II).
- `fahrradwerkstatt|B1|3` (double négation obligatoire, pas « nicht nichts »), `fahrradwerkstatt|B2|0`, `|B2|1`, `|B2|3`, `markt-obst-heimisch|C1|3` (pas de verbe rejeté après como, porque, por eso, aunque).
- `flughafen|B1|3` (gracias por / para Anna : deux « für »), `flughafen|B2|1` (indefinido / perfecto que l'allemand ne distingue pas), `park|B1|1`, `|B1|5` (imperfecto ≈ « früher … immer »).
- `heimwerken|B1|0` (pásame en un mot), `heimwerken|B1|4`, `untersuchung|B1|4` (impératif négatif = subjuntivo, autre forme qu'à l'affirmatif).
- `hotel|B1|2`, `/etapes/3/cartes/19/1`, `/etapes/7/cartes/9/3` (« halb » : neuf heures et demie = halb zehn), `hotel|B1|4` (el viernes sans « am »), `hotel|B2|0` (subjuntivo dans la relative : pas d'équivalent allemand).
- `kleidergeschaeft|B1|0`, `|B1|3` (adjectif après le nom et accordé aussi en attribut), `markt-gemuese-wurzel|A2|0`, `/reperes/8/a` (genres qui ne coïncident pas : la col / der Kohl, la mesa / der Tisch).
- `musik|B2|0`, `waschsalon|B1|0`, `|B2|0`, `sportplatz|B2|3` (subjuntivo après querer que, no creer que, cuando + futur, là où l'allemand reste à l'indicatif).
- `restaurant|B1|1` (trois degrés este / ese / aquel), `restaurant|B2|0` (lo neutre), `supermarkt|B1|0` (más + adj. plutôt qu'une terminaison), `ubahn|B1|5`, `|B1|6` (sino = « sondern »), `untersuchung|B2|5` (mientras / durante = deux « während »), `weihnachtsmarkt|B1|0`, `|B1|3`, `|B2|0` (hace frío, tener frío, ponerse / volverse : un seul « werden » en allemand), `zug|B1|0`, `|B1|4` (en tren, pas « mit » ; pas de wo / wohin).
- Repères : `/reperes/0/a`, `/reperes/1/a` (ordre des chiffres : treinta y uno vs einunddreißig), `/reperes/6/a` (j = ch de « Bach », v jamais « w »), `/reperes/9/a` (pluriel sans Umlaut).
- Premiers pas / A1 voyage : `/etapes/0/tableau/a`, `/etapes/4/tableau/a` (usted à la 3e personne), `/etapes/1/tableau/a`, `/etapes/2/tableau/a` (ser / estar, articles sans déclinaison), `/etapes/6/tableau/a` (infinitif sans « zu »), `/escales/0/tableau/a`, `/suite/1/tableau/a`, `/suite/5/tableau/a`, `/installe/0/tableau/a` (vivir = wohnen et leben), `/suite/2/tableau/a` (poner = stellen / legen / setzen).

## Doutes (à trancher à la relecture)

- `kreuzung|A2|titre`, `markt-*|A2|titre` : « ¿Dónde está? — en la ciudad / au marché » rendu „— in der Stadt“ / „— auf dem Markt“ ; les autres titres A2 gardent la forme „— estar und die Präpositionen“.
- `arztpraxis|B1|0|sens` : « Mark l'a laissé sur le sac » (la pelota) → „Mark hat ihn auf der Tasche liegen lassen“ (der Ball) : le pronom allemand ne montre plus le féminin espagnol ; la note le signale.
- `/etapes/0/cartes/11/1` « enchanté · enchantée » → „freut mich (sagt ein Mann · sagt eine Frau)“ : l'allemand n'a pas la paire, j'ai explicité.
- `/etapes/3/cartes/19/1` « y media · y cuarto » → „halb (… und dreißig) · Viertel nach“ : le décalage « neuf et demie = halb zehn » est traité dans les phrases, pas dans l'étiquette.
- `/escales/1/blocs/4/s` « Tengo mucha …. » (hambre / sed / prisa) → „Ich habe großen · große ….“ ; la variante « prisa » devient „Ich habe es sehr eilig“ (pas de « grand » possible).
- `/escales/9/blocs/3/s` « ¡Feliz …! » → „Frohe(n) …!“ ; les variantes donnent les formules idiomatiques (Alles Gute zum Geburtstag, Frohe Weihnachten, Frohes neues Jahr).
- `/escales/9/blocs/5/s` « Me gusta …. » → „Ich mag ….“, variantes „Ich tanze gern“ / „Ich singe gern“ : la structure change selon le complément.
- `/installe/1/blocs/1` « l'inscription à la commune » (empadronamiento) → „Wohnsitzanmeldung“, l'équivalent allemand le plus proche ; la note du tableau garde le mot espagnol.
- `supermarkt|B2|2` « ¿Sería tan amable de…? » → „Wären Sie so freundlich …“ ; `supermarkt|B1|0` « bolsa de papel / bolso » → „Papiertüte / Handtasche“.
- `winter|B1|0|sens` « Anna a froid » → „Anna ist kalt“ (datif), volontairement, pour que la note tener frío ≠ « sein » ait du sens.
- `ubahn|A2|3`, `ubahn|B1|2` : « pretzels » laissé « Brezeln » ; `ubahn|B2|1|sens` et `|B2|4|sens` « Bonne journée / Bon voyage » rendus par les formules allemandes sans verbe („Einen schönen Tag, Mark!“, „Gute Reise, meine Dame!“) : la note explique que le subjuntivo porte le souhait.

## Sources qui m'ont semblé fautives ou fragiles

- `weihnachtsmarkt|A2|6` : « Hay luna en el cielo » / « Il y a la lune dans le ciel » — tournure étrange en espagnol comme en français (on attendrait « La luna está en el cielo » ou « Hay luna llena ») ; traduit „Am Himmel steht der Mond“, la note hay/está reste celle de la source.
- `kueche|A2|5|sens` : « La toalla cuelga del horno » / « Le torchon » : toalla = serviette, le torchon serait « el trapo » ; rendu par „Handtuch“ pour coller à l'espagnol.
- `arztpraxis|B2|5` : la note dit « es puesta serait l'action, au passif » ; exact mais peu naturel en espagnol (« se pone »). Gardé tel quel en allemand.
- `klassenzimmer|B1|7|sens`, `|B1|7` : « sonriendo » rendu „lächeln gerade“ ; la source française « sont en train de sourire » est lourde, l'allemand n'a pas la forme progressive.
- `sportplatz|B1|2` « Eux → -ieron » et `camping|B1|1` « Eux → van a » : « eux » (ellos) rendu „Sie (Plural)“ pour ne pas être confondu avec « Sie » de politesse.
- `/etapes/3/cartes/15/3` : « Je voudrais deux cafés » traduit « Quiero dos cafés » : l'étiquette dit « je veux » ailleurs ; j'ai mis „Ich möchte zwei Kaffee, bitte.“
- `/reperes/7/a` : « 96 à 100 % de nos mots » gardé tel quel („96 bis 100 %“) ; chiffre non vérifié par moi.
- `premiers-pas` `/etapes/0/cartes/7/1` et `/etapes/0/cartes/7/3`, `/etapes/0/cartes/9/1` et `|9/3` : étiquette et exemple identiques en français (« Comment vous appelez-vous ? ») ; identiques aussi en allemand, c'est voulu par la source.

## Ce qui n'est pas fait

Rien de cette part ne reste à faire. Aucun `poser_autres.py pose` n'a été lancé (interdit) : la pose dans `visuel/prototype/espanol/<scène>.json` et `espanol/datos/<nom>.json` revient à la session principale.
