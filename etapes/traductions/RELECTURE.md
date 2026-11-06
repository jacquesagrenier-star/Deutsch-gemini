# Relire une traduction des étapes et des lignes « Tu sais… »

Lis d'abord `CONSIGNE.md` : c'est ce qu'on a demandé au traducteur. Ici, tu relis son travail **sans rien modifier**.

## Ce que tu as

- `a-traduire-<langue>.json` : chaque texte français, avec son `contexte`.
- `<langue>.json` : `{texte français: traduction}`.

## Ce que tu cherches

Uniquement ce qui se **constate**. Note chaque point avec la clé française exacte et la correction proposée.

1. **Contresens ou sens perdu** : la traduction dit autre chose que le français. Un point de grammaire nommé à la place d'une situation compte aussi.
2. **Langue fautive** : accord, cas, conjugaison, orthographe, mot qui n'existe pas, mauvais terme d'examen ou de grammaire.
3. **Une ligne « Tu sais… » qui ne se lit pas après les deux amorces de la langue** (les clés « Tu sais maintenant… » et « Cette semaine, tu as appris à… »). Essaie chaque ligne derrière chacune des deux amorces.
4. **Incohérence** : deux lignes de forme différente (infinitif ici, nom verbal là), tutoiement puis vouvoiement, deux mots différents pour la même chose d'une ligne à l'autre.
5. **Registre** : il doit suivre celui que l'app emploie déjà dans cette langue (bloc de la langue dans `index.html`, par exemple `av_fin_a1_texte`). Le genre de l'élève se dit-il là où une tournure neutre existait ?

Les préférences de naturel (« j'aurais dit autrement ») vont dans une section à part, « Avis », séparée des faits. Ne propose jamais un mot qui changerait le sens du français.

## Ce que tu rends

Le fichier `etapes/traductions/relecture-<langue>.md`, en français. D'abord une ligne « N faits, M avis ». Puis une section **Faits** : un point par ligne, `clé française` → traduction actuelle → correction → pourquoi, en une phrase. Puis une section **Avis**, dans la même forme.

Écris-le avec l'outil Write. Ne modifie aucun autre fichier. Pas de commit, pas d'API payante, pas d'autres agents.
