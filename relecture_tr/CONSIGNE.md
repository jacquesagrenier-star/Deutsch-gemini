# Consigne de relecture — traduction turque de Wortando

Tu relis la traduction TURQUE d'un cours d'allemand. Le fichier joint contient
une centaine de cartes.

## Ce qui est la source, et ce qui ne l'est pas

- **L'allemand est l'original.** C'est lui que la traduction turque doit rendre.
- **Le francais est donne uniquement pour fixer le sens voulu**, quand le mot
  allemand est ambigu hors contexte. Ne juge pas la qualite du francais, et ne
  reproche pas au turc de s'ecarter du francais s'il rend bien l'allemand.
- **Le turc est ce que tu juges.**

## Ce qu'on te demande de signaler

1. `contresens` — la traduction turque ne veut pas dire ce que dit l'allemand.
2. `phrase_infidele` — la phrase turque ne dit pas ce que dit la phrase
   allemande (sens, temps, aspect, personne, negation).
3. `turc_peu_naturel` — c'est comprehensible mais aucun locuteur ne le dirait
   ainsi ; donne la formulation naturelle.
4. `registre` — le turc est trop familier ou trop soutenu pour le niveau
   annonce (A1 a C1), ou pour la situation de la phrase.
5. `incoherence` — deux champs de la MEME carte se contredisent (le mot est
   traduit d'une facon, la phrase d'une autre).

## Ce qu'on ne te demande PAS

- Ne juge pas le genre ni le pluriel allemands : ils ont deja ete verifies.
- Ne signale pas qu'un mot turc pourrait avoir un synonyme. On ne cherche pas
  la meilleure variante possible, on cherche ce qui est FAUX ou INUTILISABLE.
- Ne signale pas les collisions entre deux cartes : elles sont detectees
  mecaniquement sur le corpus entier, tu n'en vois qu'un fragment.
- Si tu hesites, ne signale pas. Une liste courte et sure vaut mieux qu'une
  liste longue a trier.

## Le format de ta reponse

Un tableau JSON, et rien d'autre. Un objet par signalement :

```json
[
  {
    "mot": "Vater",
    "champ": "traduction_tr",
    "verdict": "contresens",
    "suggestion": "baba — « ata » veut dire ancetre, pas pere"
  }
]
```

- `mot` : la valeur du champ `cle` de la carte, recopiee telle quelle.
- `champ` : `traduction_tr`, `exemple_tr`, ou pour un verbe `perfekt_tr`,
  `praeteritum_tr`, `konjunktiv2_tr`.
- `verdict` : un des cinq mots ci-dessus.
- `suggestion` : la correction, et en une phrase pourquoi.

Si tu ne trouves rien, reponds `[]`.

Enregistre ta reponse sous `verdict_<nom du lot>.json` dans le dossier
`relecture_tr/`.
