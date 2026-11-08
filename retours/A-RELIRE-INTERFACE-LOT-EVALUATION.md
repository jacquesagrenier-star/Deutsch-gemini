# À relire : les textes du lot de l'évaluation (v1120, 6 nov. 2026)

Pour des relecteurs **natifs** de chaque langue d'interface. Les textes ont été écrits en français, puis
traduits par Claude (Opus) dans les dix autres langues, **sans relecture humaine**. Ils vivent dans les
blocs `I18N` d'`index.html` (fr, en, tr, uk, fa, ar, pt, pl, ru, de, es), à côté de `badge_unlocked_prefix`.

## Où les voir

- **La fin de la séance du jour** : « Séance terminée », les fêtes gagnées, « Tu as raté 3 mots. On les
  refait ? », « Les refaire ».
- **« ‹ » au milieu de la séance** : « Tu t'arrêtes ici », « 12 sur 20 aujourd'hui », « Il reste 9 cartes
  dans la séance. », les mots à revoir, « Continuer la séance », « Revenir à l'accueil ».
- **L'accueil, après une app fermée en pleine séance** : le bandeau « Gagné pendant ta dernière séance ».
- **La première séance sur un appareil** : la bulle du micro et du haut-parleur.
- **Après la connexion** : « Ouverture de ton accueil… » sous les deux points ambre.
- **L'écran de connexion** : la 2e ligne de la carte (auth_value_2) et la phrase de « Se connecter » (auth_desc).

Captures (allemand, espagnol, arabe ; jour et nuit) : https://claude.ai/artifact/D62huHXtncDNpTzWzfqD2c

## Les clés (17 nouvelles, 2 réécrites)

| clé | français |
|---|---|
| `fin_seance_titre` | Séance terminée |
| `fin_court_titre` | Tu t'arrêtes ici |
| `fin_court_resume` | {n} sur {cible} aujourd'hui |
| `fin_court_reste_un` / `fin_court_reste_n` | Il reste 1 carte / {n} cartes dans la séance. |
| `fin_court_a_revoir_un` / `fin_court_a_revoir_n` | Un mot à revoir, il reviendra… / {n} mots à revoir, ils reviendront à ta prochaine séance : |
| `fin_court_reprendre` | Continuer la séance |
| `fin_court_accueil` | Revenir à l'accueil |
| `fin_fetes_bandeau` | Gagné pendant ta dernière séance |
| `fin_erreurs_un` / `fin_erreurs_n` | Tu as raté 1 mot. On le refait ? / Tu as raté {n} mots. On les refait ? |
| `fin_erreurs_refaire_un` / `fin_erreurs_refaire` | Le refaire / Les refaire |
| `fin_reecouter` | Réécouter (lu par les lecteurs d'écran) |
| `tr_bulle` | Le micro et le haut-parleur : touche le micro si tu ne peux pas parler à voix haute (l'oral devient écrit)… |
| `attente_accueil` | Ouverture de ton accueil… |
| `auth_value_2` (réécrite) | Chaque jour, une courte séance : des mots, de la grammaire, une scène illustrée, l'écoute et l'oral. |
| `auth_desc` (réécrite) | Content de te revoir : connecte-toi pour retrouver ta progression. |

## Points à surveiller

- **Les pluriels** : en ukrainien, en russe, en polonais et en arabe, les phrases à nombre sont tournées
  pour éviter l'accord (« Слова з помилкою: {n} »). Une tournure plus naturelle est bienvenue, à condition
  de marcher pour 2, 5 et 21.
- **Le registre** : tutoiement partout, comme le reste de l'interface. En allemand, le `de` est
  l'interface de l'**espagnol** (voir `A-RELIRE-INTERFACE-DE.md`).
- **`tr_bulle`** : la phrase est longue pour une bulle de 300 px. Plus court est mieux, si le sens reste.
