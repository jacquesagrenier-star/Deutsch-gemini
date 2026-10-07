# Brief pour une session cloud : les mnémoniques des kanji N5 (7 oct. 2026)

Tu reprends Wortando Japonais. Tu n'as pas les notes de la session locale : tout ce qu'il te faut est ici, plus `CLAUDE.md` et `japonais/moteur/CONCEPTION.md` (branche `japonais-moteur`) si tu veux le contexte large.

## Le projet en bref

- Une app par langue apprise, sous la marque Wortando, sur un moteur partagé avec l'app allemande. Public : **francophones d'abord**, interface en français et en anglais seulement.
- L'angle retenu : Duolingo couvre le japonais jusqu'à A2, et Bunpro est en français jusqu'au N3 pour la grammaire. Notre trou de marché, ce sont **les kanji avec des mnémoniques écrites en français**, plus un examen blanc JLPT.
- Jacques (le propriétaire) est francophone et **ne parle pas japonais** : c'est le lecteur cible idéal pour juger si une mnémonique se retient.

## Règles de cette session

- Pars de la branche **`japonais-kanji-mnemo`** (fichiers : `japonais/kanji/mnemoniques_n5.json`, `textes/textes_n5.json`, `a-relire.html`, `construire.py`). Continue sur cette branche et termine par une pull request. **Ne pousse rien sur `main`.**
- Sens et lectures viennent de KANJIDIC, jamais de ta mémoire. Toi, tu écris seulement le **pont en français**.
- Les mnémoniques s'écrivent par langue (jeux de mots), elles ne se traduisent pas. Le français d'abord.
- Écris tes scripts de modification dans un fichier, jamais en heredoc.
- Avant de finir : un compte rendu dans `.claude/compte-rendu-kanji.md` sur la branche (ce qui est fait, ce que Jacques a validé ou refusé, ce qui reste), puis pousse.

## Ce que Jacques a jugé le 4 oct. (pilote de 20 kanji)

**16 sur 20 marchent** : 一 山 火 大 中 出 北 休 東 高 今 毎 間 電 九 白.

**4 refusés** :

| kanji | lecture | mnémonique refusée | confiance que la session avait donnée |
|---|---|---|---|
| 男 homme | otoko | « Un homme bande le muscle au-dessus de la rizière, couvert d'**autoco**llants. » | haute |
| 天 ciel | ten | « Un géant lève une planche et l'envoie au ciel : un smash de **ten**nis ! » | haute |
| 時 heure | ji | « Le soleil cogne sur le temple comme à **Dji**bouti : c'est l'heure de la sieste. » | haute |
| 何 quoi | nan | « Quoi ? Encore un formulaire ? **Nan** ! » | basse |

**La leçon** : trois refus sur quatre étaient notés « haute ». Cette note ne jugeait que **le son**. Or l'histoire doit aussi relier **naturellement** l'image au sens. Des autocollants pour un homme, Djibouti pour l'heure ou un smash de tennis pour le ciel sont des liens arbitraires, qui ne se retiennent pas. Règle : **l'image mène au sens.** Jacques n'a pas encore confirmé cette hypothèse : vérifie-la avec lui sur les réécritures.

## La tâche, dans cet ordre

1. **Ajoute une deuxième note** à chaque mnémonique : « le lien image-sens va de soi » (haute / moyenne / basse), à côté de la note du son. Une mnémonique n'est proposée que si les deux sont au moins « moyenne ».
2. **Réécris 男 天 時 何** avec la règle « l'image mène au sens ». Propose 2 versions par kanji et fais-les juger par Jacques **dans la conversation**, sous forme de tableau (kanji, sens, lecture, mnémonique, les deux notes).
3. Si la règle se confirme, **étends aux autres kanji N5** (103 en tout), **par lots de 20**, chaque lot jugé par Jacques dans la conversation avant le suivant. Garde ses verdicts dans le JSON (champ `avis_jacques` : `ok` / `refuse` + sa remarque).
4. Regénère `a-relire.html` avec `construire.py` pour qu'il reflète l'état final.

À ne pas faire : fabriquer du son (aucune voix japonaise ici, et ElevenLabs est une dépense qui demande son accord), toucher à l'app allemande, toucher aux branches `japonais-donnees`, `-images`, `-phrases`.
