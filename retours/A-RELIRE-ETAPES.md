# À relire par des natifs : les étapes A2-C1 et les lignes « Tu sais… »

6 nov. 2026. Les textes viennent de `etapes/structure.py` (français) et de `etapes/traductions/<langue>.json`. Ils ont été traduits par Fable, puis relus par un autre modèle. **Seuls les faits ont été corrigés** (fichiers `etapes/traductions/corrections/`). Deux modèles du même fournisseur ne sont pas deux avis indépendants : ce qui suit attend un locuteur natif.

## Ce qui a été corrigé (les faits)

| Langue | Corrections | Les principales |
|---|---|---|
| en | 0 | orthographe britannique, comme l'interface anglaise |
| pt | 0 | burocracia, feira, hobbies jugés justes au Brésil |
| de (interface de l'espagnol) | 6 | l'amorce « Diese Woche hast du gelernt: » ; « was du dir von anderen wünschst » au lieu de « sollen » ; « das aktuelle Geschehen » partout |
| tr | 5 | « soutenu » = özenli (pas resmî) ; « bilgilendirici metin » ; « Olabilecekler » |
| ar | 6 | « دون استخدام » ; « وجبة » (repas, pas banquet) ; « رسالة » partout ; participe étendu |
| ru | 3 | « soutenu » = литературным языком (pas « официальном стиле ») |
| fa | 5 | « soutenu » = فاخر (pas رسمی) ; deux constructions |
| pl | 7 | l'amorce « Po tym tygodniu potrafisz… » ; wyszukany styl ; przedstawić się ; gdzie cię boli |
| uk | 64 | toutes les lignes à l'infinitif imperfectif, après « навчитися » |

## Ce qui reste à trancher par un natif (les avis)

Les avis sont dans `etapes/traductions/relecture-<langue>.md`, section « Avis ». Les plus utiles à faire trancher :

- **de :** « von dir erzählen » ou « über dich sprechen » (raconter / parler de), « Dienste » ou « Dienstleistungen », « Wenn ich … hätte ».
- **pt :** « hobbies » dans les lignes, alors que la tuile du thème dit « Lazer ».
- **ar :** quelques titres restés au masculin (« لا تفعل ذلك! », « حين تأتي », « أردت أن تأتي »), faute de tournure neutre.
- **fa :** les noms de groupes au subjonctif de la 1re personne (« زندگی‌ام را تعریف کنم ») : objectif personnel ou titre ?
- **ru, uk, pl :** les termes de grammaire du C1 (participe étendu, Nominalstil), longs ou approximatifs.
- **toutes :** les amorces qui finissent par « : » (tr, ru, de) et celles qui finissent par « … » s'affichent-elles bien à l'écran ? À voir sur une capture.
