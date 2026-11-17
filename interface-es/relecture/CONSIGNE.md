# Relecture croisée de l'espagnol (interface de l'allemand appris) — consigne

Wortando enseigne l'allemand ; l'espagnol d'**Amérique latine** (Mexique, Colombie : tú pour
l'usager, usted pour un Sie, ustedes pour ihr, jamais vosotros) devient sa 10e langue
d'interface. Un autre modèle a traduit ; tu relis un **échantillon** pour mesurer la qualité.

Ton lot : `interface-es/relecture/lot-NN.json`, 100 entrées de trois types :
- `carte` : un mot allemand (`mot`, `niveau`, `contexte` = son thème), sa traduction française
  (`fr`) et espagnole (`es`), la phrase allemande (`phrase_de`) et sa traduction (`phrase_es`), parfois
  les trois temps d'un verbe (`perfekt_de`/`_es`, `praeteritum_…`, `konjunktiv2_…`) ;
- `exercice` : la phrase à trou allemande (`question_de`), la bonne réponse, la traduction espagnole de
  la phrase et l'explication (française et espagnole) ;
- `fiche` : un texte de fiche de grammaire, français et espagnol (l'espagnol peut comparer à l'espagnol
  là où le français comparait au français : c'est voulu).

## Ce que tu juges, et seulement ça

Un **fait** : un contresens (l'espagnol ne dit pas ce que dit l'allemand), une faute d'espagnol
(accord, conjugaison, préposition, orthographe, accent), un temps faux, un registre faux pour la
situation, une forme d'Espagne (vosotros, coche, ordenador, zumo, coger…), une explication fausse
sur l'allemand ou sur l'espagnol. Pas une préférence de style : si c'est juste et naturel au Mexique
ou en Colombie, c'est « bon », même si tu aurais dit autrement.

⚠️ Avant de dire qu'une phrase espagnole ne dit pas l'allemand, relis l'allemand **du lot** : ne
cite jamais une phrase qui n'y est pas.

## Ce que tu rends

`interface-es/relecture/lot-NN.verdict.json` : un objet avec **toutes** les entrées du lot :
`{"<id>": "bon"}` ou
`{"<id>": {"verdict": "faute", "champ": "es | phrase_es | perfekt_es | explanation_es…",
"actuel": "...", "propose": "...", "raison": "une phrase, factuelle"}}`.
Pour un doute (ce n'est pas sûr, ou c'est régional), `"verdict": "avis"` dans la même forme.

Puis 3 lignes en réponse : nombre de bons / fautes / avis, et la faute la plus grave.

Interdits : tu n'écris que `interface-es/relecture/lot-NN.verdict.json` ; aucune commande git qui
écrit ; aucun autre agent ; aucun service en ligne.
