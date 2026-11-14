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
2. ~~La borner à 4 000 caractères~~ : non, voir « ce qui est prêt » ci-dessous (aucun champ JSON n'est borné,
   pour la limite des 1 000 expressions ; l'app garde 20 examens au plus).
3. `index.html`, `syncProgressToCloud()` : écrire `soinsExamensJson: JSON.stringify(lireExamensSoins())`
   **seulement si la liste n'est pas vide** ; à la relecture, réunir par date comme `seancesJson`.
4. Ordre de mise en ligne, **impératif** : (a) Jacques colle les nouvelles règles, (b) puis la version qui
   écrit la clé. Dans l'autre ordre, la sauvegarde ENTIÈRE des comptes qui ont passé un examen blanc serait
   refusée (une clé inconnue fait échouer tout le document).
5. Contrôles : le banc des règles (`securite/essai-regles/`), `tests/verifier.py` (« clés Firestore »), et
   la mesure du budget de 1 000 expressions (une clé de plus et une borne de plus : quelques expressions).

### Proposition A : ce qui est prêt (14 nov. 2026)

Décision du chef : la règle A est proposée à Jacques **au moment où l'examen blanc est intégré et prêt à
publier**, pas avant. Tout est prêt ici pour ce jour-là.

**1. Le bloc à coller.** Le fichier complet des règles, prêt à coller dans la console Firebase
(Firestore → Règles), est `securite/regles-soins/firestore-avec-soins.rules`. C'est la copie exacte des
règles en ligne (`securite/firestore-corrige.rules` = `firestore.rules`, vérifié identique le 14 nov.)
avec **une seule différence**, dans la fonction `champsProgression()` :

```diff
               'langueApprise', 'essaiDebut', 'adresseLieeLe'];
---
               'langueApprise', 'essaiDebut', 'adresseLieeLe',
               // Wortando Pflege (proposition A, pflege/AGENCE-DONNEES.md) : les examens blancs de la section Soins.
               // Une CLE, pas un controle de plus (limite des 1 000 expressions) : comme les autres champs JSON.
               'soinsExamensJson'];
```

**Pas de borne de taille** (la proposition de départ disait 4 000 caractères) : les règles ne bornent aucun
champ JSON, parce que chaque contrôle compte dans la limite des 1 000 expressions (une sauvegarde complète
était refusée le 12 nov.) ; une clé, elle, ne coûte presque rien. L'app borne elle-même la liste
(20 examens, ≈ 1 700 caractères).

⚠️ Si les règles en ligne ont changé entre-temps (`firestore.rules` différent de
`securite/firestore-corrige.rules`), refaire le fichier à partir des nouvelles : la seule ligne à ajouter
est `'soinsExamensJson'` dans `champsProgression()`.

**2. Le banc d'essai.** `securite/essai-regles/essai.js` porte trois cas de plus (« soins : … ») :

```bash
cd securite/essai-regles
firebase emulators:exec --only firestore --project demo-wortando "node essai.js"
```

→ avec les règles en ligne, la clé est **refusée** (et toute la sauvegarde avec elle) : c'est la preuve de
l'ordre imposé.

```bash
REGLES=../regles-soins/firestore-avec-soins.rules AVEC_SOINS=1 firebase emulators:exec --only firestore --project demo-wortando "node essai.js"
```

→ avec les règles proposées, la clé est **acceptée**, sauvegarde complète comprise (le budget des 1 000
expressions tient), et les 247 autres cas restent justes.

**Résultat du 14 nov. 2026** (émulateur local, projet fictif `demo-wortando`) :

| Règles | Les 3 cas « soins » | Total |
|---|---|---|
| En ligne (`firestore-corrige.rules`) | refusés, comme attendu (sauvegarde complète, clé seule, compte sans compte) | **250 ok, 0 échec** |
| Proposées (`regles-soins/firestore-avec-soins.rules`) | acceptés, sauvegarde complète de 20 examens comprise | **250 ok, 0 échec** |

**3. Le code, à appliquer APRÈS que Jacques a collé les règles** (même version que l'intégration de
l'examen blanc, ou la suivante) :

- `syncProgressToCloud()`, à côté de `premiersPasJson` — la clé n'est écrite **que** si la liste n'est
  pas vide, pour que les comptes sans examen blanc ne l'envoient jamais :

```js
            // Wortando Pflege : les examens blancs telc Pflege (pflege/AGENCE-DONNEES.md, proposition A).
            ...(lireExamensSoins().length ? { soinsExamensJson: JSON.stringify(lireExamensSoins()) } : {}),
```

- la relecture, à côté de celle de `premiersPasJson` — la réunion des deux listes par date, sans doublon :

```js
        try{
            if(typeof data.soinsExamensJson === "string" && data.soinsExamensJson){
                const nuage = JSON.parse(data.soinsExamensJson);
                if(Array.isArray(nuage)){
                    const parDate = {};
                    lireExamensSoins().concat(nuage).forEach(x => { if(x && x.d) parDate[x.d] = x; });
                    const l = Object.values(parDate).sort((a, b) => Date.parse(a.d) - Date.parse(b.d)).slice(-SOINS_EXAMENS_MAX);
                    localStorage.setItem(SOINS_EXAMENS_KEY, JSON.stringify(l));
                }
            }
        }catch(e){}
```

- `securite/firestore-corrige.rules` et `firestore.rules` remplacés par le fichier collé (sinon
  `tests/verifier.py`, contrôle « clés Firestore », refuse la clé écrite par l'app) ;
- le suivi lit déjà `soinsExamensJson` (`bilanSoinsDuCompte`) : rien à changer de ce côté.

**4. L'ordre, à suivre à la lettre** :

1. Jacques colle `securite/regles-soins/firestore-avec-soins.rules` dans la console et publie.
2. On vérifie (une sauvegarde d'un compte ordinaire passe toujours : le tableau de bord admin le dit).
3. Seulement alors, la version qui écrit la clé.

Dans l'autre ordre, tout compte qui a passé un examen blanc verrait **toute** sa sauvegarde refusée.

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
