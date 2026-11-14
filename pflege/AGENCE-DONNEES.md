# Wortando Pflege : les données du tableau de bord de l'agence

14 nov. 2026. Ce que le suivi lit aujourd'hui, ce qu'il lui manque, et **ce qui demanderait de changer les
règles Firestore** (donc Jacques, qui les colle dans la console). Rien de ce fichier n'est en ligne.

## 1. Aujourd'hui (commit 01c6e42 et suivant), sans changer une règle

La carte « Suivi Soins » du tableau de bord admin :

| Donnée | D'où | Remarque |
|---|---|---|
| La cohorte | `resumes/<uid>.essais` contient « soins » | recopié par `basculerEssaiCompte` |
| Dernière activité | `users/<uid>.updatedAt` et `seancesJson` | |
| Jours actifs sur 7, séances finies | `users/<uid>.seancesJson` (7 jours, champs `d`, `p`, `f`) | |
| Mots des Soins vus / maîtrisés, par niveau | `users/<uid>.progressJson`, clés `soins_*` | rapportés au total de `pflege/datos/themes.json` |
| Alertes | calculées | 5 jours sans activité ; 3 séances laissées en route ; examen blanc sans certificat |
| Export | CSV (séparateur « ; », UTF-8 avec BOM, pour Excel) | |

Le détail lit le **document complet** de chaque compte de la cohorte, à la demande (bouton) : c'est lourd
mais juste pour une cohorte de quelques dizaines de comptes, et l'admin a déjà le droit de lire `users`.

## 2. Ce qui manque : les examens blancs

L'examen blanc (session « examen », `visuel/prototype/telc-pflege/`) envoie à la fin
`{type: "resultat_examen", examen: "soins_telc", points: {hls, schreiben, sprechen}}`. L'app :

- borne les points (0-59, 0-20, 0-100), **recalcule** le certificat (`certificatSoins`, contrôlé par
  `node tests/pflege_certificat.js` contre le tableau officiel) ;
- garde les 20 derniers résultats dans le stockage de l'appareil (`deutschAI_soinsExamens`) ;
- en tire « prêt pour l'examen » (`pretPourExamenSoins`) : vert = B2 au dernier examen blanc, orange = B1,
  rouge = aucun certificat, « — » = aucun examen.

**Mais ces résultats ne quittent pas l'appareil**, et le suivi de l'admin ne les voit donc pas. Pour qu'ils
remontent, il faut une clé de plus dans la sauvegarde, donc dans les règles.

### Proposition A (minimale) : une clé de progression

1. `securite/firestore-corrige.rules`, fonction `champsProgression()` : ajouter `'soinsExamensJson'`.
2. `progressionValide(d)` : la borner comme les petits champs JSON (une chaîne de moins de 4 000 caractères :
   20 résultats de ~80 caractères).
3. `index.html`, `syncProgressToCloud()` : écrire `soinsExamensJson: JSON.stringify(lireExamensSoins())`
   **seulement si la liste n'est pas vide** ; à la relecture, réunir par date comme `seancesJson`.
4. Ordre de mise en ligne, **impératif** : (a) Jacques colle les nouvelles règles, (b) puis la version qui
   écrit la clé. Dans l'autre ordre, la sauvegarde ENTIÈRE des comptes qui ont passé un examen blanc serait
   refusée (une clé inconnue fait échouer tout le document).
5. Contrôles : le banc des règles (`securite/essai-regles/`), `tests/verifier.py` (« clés Firestore »), et
   la mesure du budget de 1 000 expressions (une clé de plus et une borne de plus : quelques expressions).

### Proposition B (plus tard) : un résumé Soins

Pour éviter de lire les documents complets : un champ `soinsJson` dans `resumes/<uid>` (`champsResume()`),
de moins de 1 000 caractères, `{v, m, j7, f7, ex, pret}` (mots vus, maîtrisés, jours actifs, séances
finies, examens blancs, prêt). Le suivi lirait alors les seuls résumés, comme la liste des testeurs.
Même ordre de mise en ligne qu'en A.

## 3. L'accès d'une agence (quand Jacques le décidera)

Décision du 14 nov. : « on verra comment on va le gérer ». Le plan (`PLAN.md`, § 4.8) recommande, le jour
venu :

- une collection `agences/{id}` (nom, gestionnaires, cohortes, licences), écrite par l'admin seul ;
- un **rapport calculé** par agence, `agences/{id}/rapports/{date}`, qu'une Cloud Function écrit chaque nuit
  avec les seules colonnes de l'export ci-dessus ; le gestionnaire ne lit que les rapports de son agence ;
- **aucune** règle qui laisserait un compte non admin lire les documents d'autres comptes ;
- un contrat de sous-traitance RGPD et une mention à l'inscription (`PROFILS-RELECTURE.md`, le juriste).

Les colonnes de l'export CSV d'aujourd'hui sont celles de ce futur rapport : un même format du premier
jour (l'admin) au dernier (l'agence).
